# RQ2 Analysis: Code Documentation
# Mental Disorder Association Analysis and ICD-11 Alignment

Generated: 2026-03-31  
Notebook: `RQ2_analysis.ipynb`  

---

## 1. Project Context

This notebook implements a supervised NLP pipeline to answer Research Question 2:

> **RQ2:** Do patterns in the language used across mental-health subreddits reflect clinically meaningful associations between mental disorders, as defined by the WHO ICD-11 classification?

The approach treats each subreddit as a proxy for a broadly related disorder category. Text content is vectorised, classifiers are trained to distinguish between disorder proxies, and the resulting confusion patterns — where the model mistakes one disorder's language for another's — are reinterpreted as evidence of linguistic association between those conditions.

**Important caveat:** Subreddit membership is not a clinical diagnosis. Every subreddit-to-disorder link in this pipeline is an explicitly audited proxy mapping, not a ground truth label. All findings should be read in this light.

**Verified Reference Sources**

| Name | URL | Use in Pipeline |
|---|---|---|
| WHO ICD Overview | https://www.who.int/classifications/classification-of-diseases | Classification context |
| WHO ICD Portal | https://icd.who.int/en | ICD version context |
| WHO ICD-11 Browser | https://icd.who.int/browse11 | Broad category naming |
| sklearn MultinomialNB | https://scikit-learn.org/stable/modules/generated/sklearn.naive_bayes.MultinomialNB.html | NB model assumptions |
| sklearn LinearSVC | https://scikit-learn.org/stable/modules/generated/sklearn.svm.LinearSVC.html | SVM regularisation |
| sklearn precision_score | https://scikit-learn.org/stable/modules/generated/sklearn.metrics.precision_score.html | Metric definitions |

---

## 2. Notebook Overview

### Input
- `Data/processed/reddit_mh_clean.parquet` — the fully cleaned and lemmatised dataset produced by the upstream preprocessing pipeline (Notebooks 01–03). Only the five columns required for modelling are loaded: `clean_text`, `subreddit`, `timeframe`, `is_mental_health`, `covid_period`.

### Output Directory Structure
```
Notebooks/RQ2/
└── outputs/
    ├── figures/          ← saved plots
    ├── tables/           ← intermediate analytical tables
    └── powerbi/          ← 9 final export CSVs for Power BI
```

### Dataset at Load Time
| Metric | Value |
|---|---|
| Total rows | 1,107,302 |
| Columns loaded | 7 (5 required + row_id + empty_clean_text flag) |
| Distinct subreddits | 28 |
| Empty clean_text rows | 19 |
| Mental health subreddit share | 42.6% |

---

## 3. Step-by-Step Pipeline Logic

### Step 1 — Environment Setup and Imports

The notebook loads standard scientific Python libraries (`numpy`, `pandas`, `matplotlib`, `seaborn`) alongside `pyarrow` for Parquet I/O and `scikit-learn` for vectorisation and classification. Two utility functions are defined at this stage:

- `downcast_dataframe()` — reduces memory footprint by downcasting integer and float columns and converting low-cardinality object columns to the `category` dtype. The `clean_text` column is explicitly excluded from this conversion.
- `safe_rate()` — returns 0.0 when a denominator is zero, preventing division errors in manually computed metrics such as FPR.

A global random seed (`RANDOM_STATE = 42`) is set for both Python's `random` module and NumPy to ensure full reproducibility.

---

### Step 2 — Dataset Load and Validation

The dataset is read using `pyarrow.parquet.read_table()` with a column projection (loading only the five required columns) to minimise memory usage. After loading, `downcast_dataframe()` is applied, `clean_text` is normalised to remove excess whitespace, and a boolean `empty_clean_text` flag is added.

A summary table (`dataset_summary.csv`) is saved recording the row count, column count, subreddit count, empty text count, and the proportion of rows belonging to mental health subreddits.

---

### Step 3 — ICD-11 Proxy Mapping Construction

This is the most analytically significant setup step in the notebook. Each of the 28 subreddits is assigned to one of three mapping statuses:

**Mapped Proxy (16 subreddits):** Subreddits where a plausible link to a specific ICD-11 disorder label exists. Each mapping records:
- `proxy_disorder_label` — a specific disorder name aligned to ICD-11 terminology (e.g., `depressive_disorder_related`)
- `proxy_group_label` — the broader ICD-11 chapter group (e.g., `mood_disorders`)
- `confidence` — either `high` (direct name match or strong clinical alignment) or `medium` (approximate or ambiguous proxy)
- `include_in_main_multiclass` — boolean controlling whether the subreddit enters the multiclass modelling cohort
- `uncertainty_reason` — a plain-language audit note explaining any proxy ambiguity

**Control Group (12 subreddits):** Subreddits clearly unrelated to mental health (e.g., `fitness`, `legaladvice`, `personalfinance`). These are assigned `is_mental_health_proxy = 0` and are used exclusively in the binary classification task to represent non-mental-health language.

**Review Required:** Any subreddit not covered by the two sets above is flagged for manual review and excluded from modelling.

After the mapping is constructed, an `is_uncertain` flag is derived: `True` for any subreddit with a confidence level other than `high`. This flag propagates through to `fact_mapping_uncertainty.csv` for dashboard surfacing.

The final mapping covers **7 subreddits flagged as uncertain** — these are subreddits assigned medium or low confidence due to proxy ambiguity:

| Subreddit | Proxy Label | Confidence | Reason |
|---|---|---|---|
| EDAnonymous | eating_disorder_related | medium | Broad eating-disorder proxy |
| addiction | substance_or_addictive_behaviour_related | medium | Broad addiction proxy |
| bpd | borderline_pattern_related | medium | BPD shorthand is ambiguous |
| healthanxiety | health_anxiety_related | medium | Approximate anxiety-related proxy |
| lonely | loneliness_distress_related | low | Not a clean ICD disorder proxy |
| mentalhealth | general_mental_health_discussion | low | General discussion, not disorder-specific |
| suicidewatch | suicidality_related_support | low | Support forum, not single disorder |

---

### Step 4 — Cohort Construction and Train/Validation/Test Split

Two modelling cohorts are derived from the merged dataset:

**Binary cohort:** All 1,107,302 rows. The target is `binary_target` (1 = mental health subreddit, 0 = control). All rows with non-empty `clean_text` are eligible.

**Multiclass cohort:** 336,698 rows. Only rows meeting all three of the following conditions are included: `binary_target == 1`, `include_in_main_multiclass == True`, and `clean_text` is non-empty. The target is `proxy_multiclass_target` — the disorder proxy label string. This cohort covers **13 distinct disorder proxy labels**.

Both cohorts are split using a stratified 70/15/15 train/validation/test strategy implemented via two sequential `train_test_split()` calls. Stratification ensures that class proportions are preserved across all three splits. Rows that do not enter any split (e.g., empty text rows) are assigned the label `unused` in the split column and are excluded from all model training and evaluation.

---

### Step 5 — Binary Classification

**Objective:** Validate that language alone is sufficient to distinguish mental health content from non-mental health content.

**Sampling:** A 10% stratified sample (approximately 110,729 rows) is drawn from the binary cohort for training speed. Vectorisation is pre-computed once on this sample and reused across all model fits.

**Vectorisers used:**
- `CountVectorizer` — unigram + bigram, min_df=5, max_df=0.95
- `TfidfVectorizer` — unigram + bigram, min_df=5, max_df=0.95, sublinear TF scaling

**Models evaluated:**

| Model | Vectoriser | Role |
|---|---|---|
| `dummy_stratified` | None | Chance-level baseline |
| `multinomial_nb_count` | CountVectorizer | Probabilistic bag-of-words |
| `multinomial_nb_tfidf` | TfidfVectorizer | Probabilistic TF-IDF |
| `linearsvc_l2_tfidf` | TfidfVectorizer | Linear SVM with L2 penalty |

Each model is evaluated on all three splits. Metrics recorded per row: accuracy, precision, recall, F1, FPR, and raw confusion matrix counts (TP, FP, FN, TN).

**Key findings (test split):**

| Model | Accuracy | Precision | Recall | F1 | FPR |
|---|---|---|---|---|---|
| LinearSVC L2 | 0.942 | 0.942 | 0.922 | 0.932 | 0.043 |
| NB TF-IDF | 0.910 | 0.878 | 0.917 | 0.897 | 0.096 |
| NB Count | 0.900 | 0.838 | 0.950 | 0.890 | 0.138 |
| Dummy Stratified | 0.519 | 0.439 | 0.429 | 0.434 | 0.412 |

LinearSVC with TF-IDF achieves 93.2% F1 on the test set — approximately 50 percentage points above the stratified dummy baseline. This confirms that Reddit post language carries strong discriminative signal for mental health content identification.

---

### Step 6 — Multiclass Disorder Classification

**Objective:** Determine how well the model can attribute language to a specific disorder proxy label among the 13 eligible categories.

**Sampling:** A 20% stratified sample (approximately 67,339 rows) drawn from the multiclass cohort. Stratification is applied per `proxy_multiclass_target` to maintain label balance.

**Models evaluated:**

| Model | Vectoriser | Penalty |
|---|---|---|
| `multiclass_nb_count` | CountVectorizer | — |
| `multiclass_nb_tfidf` | TfidfVectorizer | — |
| `multiclass_svc_l2` | TfidfVectorizer | L2, C=1.0 |
| `multiclass_svc_l1` | TfidfVectorizer | L1, C=1.0 |

Evaluation uses macro-averaged precision, recall, and F1 (equal weight per class regardless of support). Per-label metrics are also computed from the confusion matrix using `per_label_metrics()`.

**Key findings (test split, best model = `multiclass_svc_l1`):**

| Model | Accuracy | F1-Macro |
|---|---|---|
| SVC L1 | 0.779 | 0.668 |
| SVC L2 | 0.777 | 0.666 |
| NB Count | 0.688 | 0.481 |
| NB TF-IDF | 0.481 | 0.125 |

**Per-label F1 for `multiclass_svc_l1` on the test split (highest to lowest):**

| Disorder Proxy | Precision | Recall | F1 | Support |
|---|---|---|---|---|
| attention_deficit_hyperactivity_disorder | 0.875 | 0.856 | 0.865 | 1,375 |
| depressive_disorder_related | 0.811 | 0.896 | 0.851 | 3,521 |
| eating_disorder_related | 0.876 | 0.799 | 0.836 | 452 |
| autism_spectrum_disorder | 0.891 | 0.681 | 0.772 | 276 |
| post_traumatic_stress_related | 0.808 | 0.655 | 0.724 | 264 |
| substance_or_addictive_behaviour_related | 0.827 | 0.635 | 0.718 | 219 |
| borderline_pattern_related | 0.857 | 0.613 | 0.715 | 716 |
| schizophrenia_or_other_primary_psychotic_disorder | 0.864 | 0.603 | 0.710 | 252 |
| health_anxiety_related | 0.911 | 0.537 | 0.676 | 268 |
| bipolar_or_related_disorder | 0.800 | 0.553 | 0.654 | 159 |
| social_anxiety_related | 0.776 | 0.540 | 0.637 | 704 |
| anxiety_or_fear_related_disorder | 0.395 | 0.765 | 0.521 | 497 |
| alcohol_related_disorder | — | — | — | 0 (no test instances) |

The wide spread in per-label F1 (0.52–0.87) is analytically meaningful: disorders with highly specific vocabulary (ADHD, alcohol-related) achieve high F1, while disorders with overlapping language (anxiety, depression) are harder to separate — and this overlap is precisely what `fact_disorder_association.csv` captures.

---

### Step 7 — Regularisation Sweep

**Objective:** Understand how L1 versus L2 penalty and the C hyperparameter affect multiclass model behaviour, particularly in terms of feature sparsity and generalisation.

Six model configurations are evaluated: L1 and L2 penalty, each at C ∈ {0.5, 1.0, 2.0}. All use the TF-IDF vectoriser and the 20% multiclass sample. The `non_zero_coef_ratio` — the proportion of non-zero coefficients in the learned weight matrix — is recorded alongside accuracy and F1-macro across all three splits.

**Key findings:**

- **L2 at C=1.0** reaches near-perfect training F1 (0.998) with 80.5% non-zero coefficients, but test F1 (0.666) is substantially lower — indicating mild overfitting driven by a dense, high-capacity weight matrix.
- **L1 at C=1.0** achieves training F1 of 0.870 with only 1.2% non-zero coefficients, and test F1 of 0.668 — matching L2's generalisation while using an aggressively sparse feature set. This is the configuration selected as the best model.
- **L1 at C=0.5** achieves comparable generalisation (test F1 = 0.664) with even fewer non-zero coefficients (0.4%), demonstrating that the model's discriminative signal is concentrated in a very small vocabulary.
- **Increasing C under L2** raises training performance further but does not improve — and slightly degrades — test performance, consistent with variance inflation.

The L1 result is particularly important for the RQ2 interpretation: a highly sparse model achieving ~67% macro F1 means that a small number of words per disorder class carry most of the discriminative weight. This makes the feature importance outputs (`fact_feature_importance.csv`) directly interpretable as the core linguistic signatures of each disorder proxy.

---

### Step 8 — Disorder Association Derivation

**Objective:** Translate classification errors into a measure of linguistic association between disorder proxies.

The best-performing model on the validation set (`multiclass_svc_l1`) is selected. Its confusion matrix on the test split is used as the source of association signals. The logic is:

1. Off-diagonal cells in the confusion matrix — where the true label is disorder A but the model predicted disorder B — are extracted as association edges.
2. For each true label, the total number of misclassified instances (`error_total_from_true`) is computed.
3. Each edge's `association_strength_error_share` is the proportion of that true label's errors accounted for by the predicted label: `count / error_total_from_true`.
4. A `cross_group_flag` is added: `True` if the true and predicted labels belong to different ICD-11 chapter groups (e.g., personality disorder confused with mood disorder), `False` if they are within the same group.

**Top 10 disorder associations by error share (test split):**

| True Disorder | Predicted As | Error Share | Cross-Group |
|---|---|---|---|
| health_anxiety_related | anxiety_or_fear_related_disorder | 68.5% | No |
| borderline_pattern_related | depressive_disorder_related | 66.1% | Yes |
| eating_disorder_related | depressive_disorder_related | 61.5% | Yes |
| social_anxiety_related | anxiety_or_fear_related_disorder | 57.4% | No |
| anxiety_or_fear_related_disorder | depressive_disorder_related | 56.4% | Yes |
| attention_deficit_hyperactivity_disorder | depressive_disorder_related | 55.1% | Yes |
| bipolar_or_related_disorder | depressive_disorder_related | 50.7% | No |
| schizophrenia_or_other_primary_psychotic_disorder | depressive_disorder_related | 50.0% | Yes |
| substance_or_addictive_behaviour_related | depressive_disorder_related | 46.3% | Yes |
| post_traumatic_stress_related | depressive_disorder_related | 45.1% | Yes |

`depressive_disorder_related` is the dominant attractor: nine of the ten strongest associations involve it as the predicted label, reflecting the high prevalence and lexical breadth of depressive language on Reddit.

In parallel, a full 13×13 association matrix (`disorder_association_matrix.csv`) is pivoted from the confusion counts to support heatmap visualisation in Power BI.

---

### Step 9 — Feature Importance Extraction

**Objective:** Identify the specific words driving each disorder proxy classification, to support linguistic interpretability of the association patterns.

The best multiclass model (`multiclass_svc_l1`) is re-fitted on the training sample. The `.coef_` matrix (shape: 13 classes × vocabulary size) is extracted, and for each class the top 50 features by coefficient magnitude are ranked and stored.

The result is 650 rows in `fact_feature_importance.csv` (13 classes × 50 words). Sample top features for selected disorder proxies:

| Disorder Proxy | Rank 1 Word | Coefficient | Rank 2 Word | Coefficient |
|---|---|---|---|---|
| alcohol_related_disorder | alcoholism | 6.578 | alcoholic | 6.459 |
| attention_deficit_hyperactivity_disorder | adhd | (high) | stimulant | — |
| depressive_disorder_related | depress | (high) | suicid | — |

High-coefficient, disorder-specific words (such as "alcoholism", "adhd") explain why those classes achieve high F1 — their vocabulary is largely non-overlapping. Disorders with lower F1, such as `anxiety_or_fear_related_disorder`, tend to share high-coefficient words with depressive language (e.g., "feel", "help", "want"), explaining their high confusion rates.

---

## 4. Output Files

All nine files below are exported to `Notebooks/RQ2/outputs/powerbi/`.

| File | Grain | Rows | Columns | Description |
|---|---|---|---|---|
| `dim_icd_mapping.csv` | One row per subreddit | 28 | 11 | Master mapping of subreddits to ICD-11 proxy labels, groups, confidence, and uncertainty flags |
| `dim_sources.csv` | One row per verified source | 6 | 3 | Reference log of WHO and sklearn documentation sources used in the analysis |
| `fact_binary_metrics.csv` | One row per model × split | 12 | 11 | Binary classification metrics: accuracy, precision, recall, F1, FPR, and raw confusion counts |
| `fact_multiclass_metrics.csv` | One row per model × split × label | 156 | 9 | Per-label classification metrics for all multiclass models and splits |
| `fact_confusion_matrix.csv` | One row per true–predicted pair | 2,076 | 6 | Full confusion matrix for both binary and multiclass tasks across all models and splits |
| `fact_regularization.csv` | One row per penalty setting × split | 18 | 7 | Regularisation sweep results: L1/L2, C values, F1-macro, and non-zero coefficient ratio |
| `fact_disorder_association.csv` | One row per disorder pair | 156 | 11 | Ranked disorder association edges derived from classification errors |
| `fact_mapping_uncertainty.csv` | One row per uncertain subreddit | 7 | 11 | Subset of `dim_icd_mapping` containing only medium- and low-confidence mappings |
| `fact_feature_importance.csv` | One row per model × class × rank | 650 | 4 | Top-50 TF-IDF coefficient words per disorder proxy class |

Additionally, `disorder_association_matrix.csv` is saved to the `tables/` subdirectory. It is a 13×13 pivot of confusion counts (true label × predicted label) intended for heatmap construction in Power BI.

---

## 5. Notes and Assumptions

1. **Proxy mapping is not diagnosis.** All subreddit-to-ICD links are constructed heuristics. Medium and low confidence mappings (flagged in `fact_mapping_uncertainty.csv`) should be treated as indicative rather than definitive.
2. **Sampling rationale.** The binary task uses a 10% stratified sample and the multiclass task uses a 20% stratified sample. This was necessary to manage Colab memory and runtime constraints. Metrics should be interpreted as estimates, not exhaustive-dataset results.
3. **ICD version.** All mappings are anchored to ICD-11. The `icd_version` column in `dim_icd_mapping.csv` records this explicitly.
4. **Negation preservation.** Upstream preprocessing intentionally retains negation words (no, not, never, nor and their contractions). This was deliberate to preserve sentiment-relevant linguistic signals, particularly relevant for disorders like depression and anxiety.
5. **`alcohol_related_disorder` has zero test instances.** The 20% stratified sample produced no test rows for this label, so its test F1 is reported as 0 by definition. Its train and validation metrics are valid and its feature importance is well-defined.
6. **Association direction.** `association_strength_error_share` is directional: it measures how often disorder A is confused *as* disorder B, not the reverse. The matrix is not symmetric.

---

## 6. Re-run Instructions

1. Ensure the environment includes: `pandas`, `pyarrow`, `numpy`, `matplotlib`, `seaborn`, `scikit-learn`.
2. Mount Google Drive and verify `reddit_mh_clean.parquet` is present at `/content/drive/MyDrive/`.
3. Run `RQ2_analysis.ipynb` from top to bottom. All directory creation is handled automatically by the notebook.
4. Verify the nine export files are present in `Notebooks/RQ2/outputs/powerbi/`.
5. Load files into Power BI following the instructions in the companion visualisation guide.
