# RQ2 Power BI Visualisation Guide
# Mental Disorder Association Analysis and ICD-11 Alignment

Generated: 2026-03-31  
Prepared by: Ganenthra Ravindran

---

## 1. Dashboard Purpose

This dashboard is designed to communicate the findings of the RQ2 analysis to three different audiences operating from the same data model:

- **Researchers** — exploring which disorder proxies the model associates linguistically and what vocabulary drives those associations.
- **Clinicians (informational)** — reviewing which ICD-11 chapter groups show the strongest cross-category language overlap, noting that all mappings are Reddit proxies, not clinical diagnoses.
- **Auditors and reviewers** — verifying the confidence and uncertainty of every subreddit-to-ICD-11 mapping before interpreting any finding.

The dashboard answers four core questions:

1. Which subreddits map to which ICD-11 disorder categories, and how confident are we in those mappings?
2. How reliably can a text classifier identify mental health content versus general Reddit content?
3. Which disorder proxies are linguistically confused with each other, and how strongly?
4. What words drive the association between two disorders?

---

## 2. Data Model

Load all ten files into Power BI. The recommended model follows a star schema with two dimension tables and eight fact tables.

### Dimension Tables (reference data — one row per entity)

| Table | File | Primary Key |
|---|---|---|
| `dim_icd_mapping` | `dim_icd_mapping.csv` | `subreddit` |
| `dim_sources` | `dim_sources.csv` | `name` |

### Fact Tables (one row per measurement)

| Table | File | Foreign Key(s) |
|---|---|---|
| `fact_binary_metrics` | `fact_binary_metrics.csv` | `model_name` |
| `fact_multiclass_metrics` | `fact_multiclass_metrics.csv` | `model_name`, `label` (joins to `proxy_disorder_label` in dim) |
| `fact_confusion_matrix` | `fact_confusion_matrix.csv` | `model_name`, `true_label`, `predicted_label` |
| `fact_regularization` | `fact_regularization.csv` | `model_name`, `penalty`, `C` |
| `fact_disorder_association` | `fact_disorder_association.csv` | `true_label`, `predicted_label` |
| `fact_mapping_uncertainty` | `fact_mapping_uncertainty.csv` | `subreddit` |
| `fact_feature_importance` | `fact_feature_importance.csv` | `proxy_disorder_label` |
| `disorder_association_matrix` | `disorder_association_matrix.csv` | `true_label` (row index) |

### Key Relationships to Create in Power BI

- `fact_multiclass_metrics[label]` → `dim_icd_mapping[proxy_disorder_label]` (many-to-one)
- `fact_disorder_association[true_label]` → `dim_icd_mapping[proxy_disorder_label]` (many-to-one)
- `fact_feature_importance[proxy_disorder_label]` → `dim_icd_mapping[proxy_disorder_label]` (many-to-one)
- `fact_mapping_uncertainty[subreddit]` → `dim_icd_mapping[subreddit]` (many-to-one)

`dim_sources` does not join to any fact table — it is a standalone reference displayed on the Audit page.

---

## 3. File-by-File Column Guide

### 3.1 `dim_icd_mapping.csv`
28 rows — one per subreddit.

| Column | Type | Meaning |
|---|---|---|
| `subreddit` | text | Reddit community name — the primary join key |
| `mapping_status` | text | `mapped_proxy` (MH subreddit), `control_group` (non-MH), `review_required` |
| `is_mental_health_proxy` | integer | 1 = mental health proxy, 0 = control |
| `proxy_disorder_label` | text | Specific ICD-11-aligned disorder label (e.g., `depressive_disorder_related`) |
| `proxy_group_label` | text | Broader ICD-11 chapter group (e.g., `mood_disorders`) |
| `icd_proxy_category` | text | Top-level ICD chapter; `not_applicable` for controls |
| `confidence` | text | `high`, `medium`, or `low` — reflects reliability of the subreddit-to-disorder link |
| `include_in_main_multiclass` | boolean | Whether this subreddit entered the 13-class multiclass model |
| `uncertainty_reason` | text | Plain-language audit note explaining any ambiguity in the mapping |
| `icd_version` | text | Always `ICD-11` — the classification standard used |
| `is_uncertain` | boolean | True for any confidence level other than `high` — use this as a dashboard filter flag |

**Note:** The `proxy_disorder_label` column in this table is the join key connecting dimension data to multiclass fact tables. Ensure Power BI does not auto-detect an ambiguous relationship; set the join direction explicitly.

---

### 3.2 `dim_sources.csv`
6 rows — one per verified reference source.

| Column | Type | Meaning |
|---|---|---|
| `name` | text | Short name of the source (e.g., `WHO ICD Overview`) |
| `url` | text | Full URL of the source |
| `use` | text | How the source was used in the analysis pipeline |

Display this table as a static reference table on the Audit page. No joins to fact tables are required.

---

### 3.3 `fact_binary_metrics.csv`
12 rows — 4 models × 3 splits.

| Column | Type | Meaning |
|---|---|---|
| `model_name` | text | Identifier: `dummy_stratified`, `multinomial_nb_count`, `multinomial_nb_tfidf`, `linearsvc_l2_tfidf` |
| `split_name` | text | `train`, `valid`, or `test` |
| `accuracy` | decimal | Overall accuracy on the split |
| `precision` | decimal | Positive predictive value — of predicted MH posts, how many are truly MH |
| `recall` | decimal | Sensitivity — of all true MH posts, how many were correctly identified |
| `f1` | decimal | Harmonic mean of precision and recall — primary summary metric |
| `fpr` | decimal | False positive rate — proportion of non-MH posts incorrectly labelled as MH |
| `tp`, `fp`, `fn`, `tn` | integer | Raw confusion matrix counts for binary classification |

**Key filter:** Always filter to `split_name = test` for headline metrics on the dashboard. Use `train` vs `test` comparisons to show overfitting behaviour.

---

### 3.4 `fact_multiclass_metrics.csv`
156 rows — 4 models × 3 splits × 13 labels.

| Column | Type | Meaning |
|---|---|---|
| `task_name` | text | Always `multiclass` in this table |
| `model_name` | text | Identifies which of the four multiclass models produced this row |
| `split_name` | text | `train`, `valid`, or `test` |
| `label` | text | The disorder proxy label this row measures (joins to `dim_icd_mapping[proxy_disorder_label]`) |
| `support` | integer | Number of instances of this label in the split |
| `precision` | decimal | Of all instances predicted as this label, the fraction that were correct |
| `recall` | decimal | Of all true instances of this label, the fraction that were correctly identified |
| `fpr` | decimal | False positive rate — how often this label was incorrectly predicted for other disorders |
| `f1` | decimal | Harmonic mean of precision and recall for this label |

**Note:** The `alcohol_related_disorder` label has `support = 0` on the test split due to sampling. Its test metrics are 0.0 by definition, not a model failure. Flag this in any dashboard tooltip for that label.

---

### 3.5 `fact_confusion_matrix.csv`
2,076 rows — covers both binary and multiclass tasks across all models and splits.

| Column | Type | Meaning |
|---|---|---|
| `task_name` | text | `binary` or `multiclass` — always filter this when building visuals |
| `model_name` | text | Which model produced this confusion row |
| `split_name` | text | `train`, `valid`, or `test` |
| `true_label` | text | The actual label (or `0`/`1` for binary) |
| `predicted_label` | text | What the model predicted |
| `count` | integer | Number of instances in this true/predicted combination |

**Usage:** Use the diagonal cells (`true_label == predicted_label`) for a correct-classification heatmap. Use off-diagonal cells for the association heatmap. Always filter to `task_name = multiclass` and `model_name = multiclass_svc_l1` and `split_name = test` for the primary association heatmap.

---

### 3.6 `fact_regularization.csv`
18 rows — 6 model configurations × 3 splits.

| Column | Type | Meaning |
|---|---|---|
| `model_name` | text | Encodes both penalty and C value (e.g., `svc_l1_c1_0`) |
| `split_name` | text | `train`, `valid`, or `test` |
| `penalty` | text | `l1` or `l2` |
| `C` | decimal | Regularisation strength: 0.5, 1.0, or 2.0. Higher C = less regularisation |
| `accuracy` | decimal | Overall accuracy on the split |
| `f1_macro` | decimal | Macro-averaged F1 across all 13 disorder labels |
| `non_zero_coef_ratio` | decimal | Proportion of model weights that are non-zero (sparsity indicator) |

**Key insight to surface:** L1 at C=1.0 achieves test F1 comparable to L2 (0.668 vs 0.666) while using only 1.2% non-zero coefficients versus L2's 80.5%. This sparsity is what makes feature importance interpretable.

---

### 3.7 `fact_disorder_association.csv`
156 rows — all off-diagonal confusion pairs for the best model on the test split.

| Column | Type | Meaning |
|---|---|---|
| `task_name` | text | Always `multiclass` |
| `model_name` | text | Always `multiclass_svc_l1` (best model selected) |
| `split_name` | text | Always `test` |
| `true_label` | text | The disorder the post actually came from |
| `predicted_label` | text | The disorder the model confused it with |
| `count` | integer | Number of misclassified instances |
| `error_total_from_true` | integer | Total errors made for this true label (denominator) |
| `association_strength_error_share` | decimal | `count / error_total_from_true` — the primary association metric (0 to 1) |
| `true_group` | text | ICD-11 chapter group of the true label |
| `predicted_group` | text | ICD-11 chapter group of the predicted label |
| `cross_group_flag` | boolean | True if the two labels belong to different ICD-11 chapter groups |

**This is the core analytical table.** An error share of 0.685 for `health_anxiety_related → anxiety_or_fear_related_disorder` means that 68.5% of all health anxiety misclassifications went to the broader anxiety category — a strong within-group linguistic association. A `cross_group_flag = True` row (e.g., `borderline_pattern_related → depressive_disorder_related` at 66.1%) indicates a cross-diagnostic association that crosses ICD-11 chapter boundaries.

---

### 3.8 `fact_mapping_uncertainty.csv`
7 rows — one per medium- or low-confidence subreddit mapping.

This is a filtered subset of `dim_icd_mapping` containing only rows where `is_uncertain = True`. It contains the same 11 columns. Use it to power a dedicated uncertainty callout panel on the ICD Mapping page so that any visual using uncertain labels is explicitly flagged to the viewer.

---

### 3.9 `fact_feature_importance.csv`
650 rows — 13 disorder proxies × 50 top words each.

| Column | Type | Meaning |
|---|---|---|
| `proxy_disorder_label` | text | The disorder class these features belong to (join key to `dim_icd_mapping`) |
| `feature_word` | text | The TF-IDF token or bigram (note: lemmatised, so "alcoholism" not "alcoholisms") |
| `coefficient_value` | decimal | The linear SVM coefficient weight — higher = more diagnostic for this class |
| `importance_rank` | integer | 1 = most important word for this class; 50 = least important in the top 50 |

**Usage:** Filter to a single `proxy_disorder_label` and display as a ranked bar chart. The top-ranked words explain *why* two disorders are associated — if the same words appear highly ranked for two different classes, that lexical overlap is the mechanism behind the confusion.

---

### 3.10 `disorder_association_matrix.csv`
13×13 matrix — rows are `true_label`, columns are predicted disorder labels, values are confusion counts.

Load this as a separate table. Its primary use is a matrix visual (heatmap) showing the full confusion count grid. The diagonal is always zero in this file because it represents off-diagonal confusion only; the file was pivoted from the association edges table.

---

## 4. Recommended Report Pages

Build five pages in this order. Each page's scope and required tables are specified below.

---

### Page 1 — ICD Mapping Overview

**Purpose:** Orient the viewer to the 28 subreddits, their disorder labels, and the confidence level of each mapping before any model results are presented.

**Visuals to build:**

1. **Mapping status summary card row** — three cards showing counts of `mapped_proxy`, `control_group`, and `review_required` rows from `dim_icd_mapping`. Filter to `is_uncertain = False` for the high-confidence count.

2. **Subreddit mapping table** — a table visual from `dim_icd_mapping` with columns: `subreddit`, `proxy_disorder_label`, `proxy_group_label`, `confidence`, `include_in_main_multiclass`, `uncertainty_reason`. Apply conditional formatting to colour the `confidence` column: green for `high`, amber for `medium`, red for `low`.

3. **Uncertainty callout panel** — a second, separate table showing only the 7 rows from `fact_mapping_uncertainty.csv`. Display `subreddit`, `confidence`, and `uncertainty_reason`. Add a text box above the table reading: *"Mappings below are proxy estimates. Interpret associated findings with caution."*

4. **ICD group bar chart** — a clustered bar from `dim_icd_mapping` showing count of subreddits per `proxy_group_label`, coloured by `confidence`. Helps the viewer see which ICD-11 chapters have the most data coverage.

**Slicers:** `confidence`, `include_in_main_multiclass`.

---

### Page 2 — Binary Model Validity

**Purpose:** Demonstrate that language alone can distinguish mental health Reddit content from general Reddit content, and show how far each model exceeds the chance-level baseline.

**Visuals to build:**

1. **Model comparison bar chart** — a clustered bar from `fact_binary_metrics`, filtered to `split_name = test`. Place `model_name` on the axis, with bars for `f1`, `precision`, and `recall`. Include a reference line at the dummy stratified F1 (0.434) to mark the chance-level threshold.

2. **Train vs Test F1 table** — a matrix visual from `fact_binary_metrics` with `model_name` as rows and `split_name` as columns, values as `f1`. This surfaces overfitting: the gap between `train` and `test` F1 should be small for good generalisers (LinearSVC gap: 0.999 → 0.932) and large for overfit models.

3. **Confusion count cards (best model)** — four KPI cards filtered to `model_name = linearsvc_l2_tfidf` and `split_name = test`, showing TP, FP, FN, and TN counts. Label them clearly: "Correctly identified MH posts", "Non-MH posts misclassified as MH", etc.

4. **FPR vs F1 scatter** — plot each model (filtered to test split) with FPR on the X-axis and F1 on the Y-axis. Annotate by `model_name`. This shows the precision-recall trade-off visually: NB-Count achieves high recall (0.950) at the cost of a much higher FPR (0.138) compared to LinearSVC (FPR = 0.043).

**Slicers:** `split_name` (lock default to `test` but allow exploration).

---

### Page 3 — Disorder Association Patterns

**Purpose:** This is the primary analytical page. It answers RQ2 directly: which disorder proxies are linguistically similar, how strong is the association, and does it cross ICD-11 chapter boundaries?

**Visuals to build:**

1. **Association heatmap** — use `disorder_association_matrix.csv`. Place `true_label` on the Y-axis and predicted label columns on the X-axis. Use a diverging colour scale from white (0) to dark red (high confusion count). This gives an at-a-glance view of which disorder pairs are most linguistically interchangeable. Label the axes clearly as "True Disorder Proxy" and "Model-Predicted As".

2. **Top association ranked bar** — from `fact_disorder_association.csv`, create a bar chart sorted descending by `association_strength_error_share`. Show the top 10 pairs. Label each bar with `true_label → predicted_label`. Apply conditional formatting: bars where `cross_group_flag = True` appear in orange (cross-diagnostic); bars where `cross_group_flag = False` appear in blue (within-group).

3. **Cross-group vs within-group donut** — a donut chart from `fact_disorder_association.csv` showing the split between `cross_group_flag = True` (cross-diagnostic associations) and `cross_group_flag = False` (within-group associations) by count of association edges and by sum of `count`. This contextualises whether linguistic overlap is primarily within or across ICD-11 chapters.

4. **Association detail table** — a full table from `fact_disorder_association.csv` with columns: `true_label`, `predicted_label`, `count`, `association_strength_error_share`, `true_group`, `predicted_group`, `cross_group_flag`. Sort by `association_strength_error_share` descending by default. Allow the user to filter by `true_group` or `cross_group_flag`.

**Slicers:** `true_group`, `cross_group_flag`, `proxy_group_label` (from dim, used to filter to a specific ICD chapter's disorders).

**Important tooltip to add:** On any bar or cell referencing an uncertain label (those in `fact_mapping_uncertainty`), add a tooltip note: *"This disorder mapping is medium or low confidence. See the ICD Mapping page for details."* This can be implemented by merging the `is_uncertain` flag from `dim_icd_mapping` into the visual's data.

---

### Page 4 — Linguistic Drivers

**Purpose:** Allow the viewer to drill into the vocabulary that drives classification — and by extension, association — for any selected disorder proxy.

**Visuals to build:**

1. **Disorder selector slicer** — a single-select slicer from `fact_feature_importance[proxy_disorder_label]`. This drives the rest of the page.

2. **Top 20 feature words bar chart** — from `fact_feature_importance`, filtered to the selected `proxy_disorder_label` and `importance_rank <= 20`. Place `feature_word` on the Y-axis (sorted by `importance_rank` ascending) and `coefficient_value` on the X-axis. This is the primary visual on the page.

3. **Side-by-side comparison panel** — duplicate the bar chart and place two slicers side by side, one for each panel. This allows the viewer to compare the vocabulary of two disorder proxies simultaneously. Shared words appearing in both lists are the lexical mechanism behind the confusion between those two disorders.

4. **Association context card** — a card or text visual that, when a disorder is selected, displays its top association partner from `fact_disorder_association.csv` (`true_label = selected disorder`, `rank 1 by association_strength_error_share`). Format as: *"When the model misclassifies [disorder], it most often predicts: [predicted_label] ([error share]%)"*.

5. **Mapping confidence badge** — a card showing the `confidence` value from `dim_icd_mapping` for the selected subreddit/disorder. Colour it green, amber, or red to match the confidence level. This reminds the viewer not to over-interpret the word-level findings for uncertain mappings.

**Slicers:** `proxy_disorder_label` (primary driver), `importance_rank` range filter (to let the viewer explore ranks 1–10 vs 11–50).

---

### Page 5 — Audit and Provenance

**Purpose:** Provide full methodological transparency for reviewers, enabling them to trace every finding back to its data source and modelling decision.

**Visuals to build:**

1. **Verified source log table** — a table visual directly from `dim_sources.csv` showing `name`, `url` (formatted as a hyperlink), and `use`. Title the section: *"Verified Reference Sources — All ICD-11 mappings and model design decisions reference the sources below."*

2. **Regularisation summary table** — from `fact_regularization.csv`, a matrix with `model_name` as rows and `split_name` as columns. Show `f1_macro` as values with a secondary column for `non_zero_coef_ratio`. Include a text annotation: *"L1 penalty at C=1.0 was selected as the best multiclass model: test F1-macro = 0.668 with only 1.2% non-zero coefficients, indicating a sparse and interpretable decision boundary."*

3. **Regularisation line chart** — from `fact_regularization.csv`, filtered to `split_name = test`. Plot `C` on the X-axis and `f1_macro` on the Y-axis, with separate lines for `penalty = l1` and `penalty = l2`. This shows the generalisation curve across regularisation strengths.

4. **Uncertainty summary panel** — a table from `fact_mapping_uncertainty.csv` (same as Page 1) listing all 7 uncertain subreddits with their `uncertainty_reason`. Add a header: *"The following subreddit-to-disorder links are medium or low confidence and should be interpreted as approximate proxies only."*

5. **Pipeline summary text box** — a static text box summarising the pipeline in plain language: dataset size (1,107,302 posts, 28 subreddits), split strategy (70/15/15 stratified), ICD version (ICD-11), model family (Naive Bayes and LinearSVC), and sampling rates (10% binary, 20% multiclass).

**No slicers needed on this page** — it is a static reference page.

---

## 5. Cross-Page Filters and Slicers

The following slicers should be consistent across pages that share their scope:

| Slicer | Recommended pages | Values |
|---|---|---|
| `split_name` | Pages 2, 3 | Default: `test`; allow `valid` and `train` for exploration |
| `model_name` | Pages 2, 3, 4 | Default: best models (`linearsvc_l2_tfidf` for binary; `multiclass_svc_l1` for multiclass) |
| `confidence` | Pages 1, 3 | Default: all; allow filtering to `high` only to hide uncertain mappings |
| `cross_group_flag` | Page 3 | Default: all; allow filter to `True` to focus on cross-diagnostic associations |

Use Power BI's **sync slicers** feature (View → Sync Slicers) to link `split_name` and `model_name` across pages so that changing a slicer on one page propagates to others.

---

## 6. Interpretation Guide

### Reading association strength
`association_strength_error_share` of 0.685 for `health_anxiety_related → anxiety_or_fear_related_disorder` means that of every 100 health anxiety posts the model gets wrong, 69 are predicted as general anxiety. This is not a modelling failure — it is a signal that the language used in health anxiety posts is largely indistinguishable from general anxiety language, which has potential clinical relevance.

### Reading cross_group_flag
A `cross_group_flag = True` row means the two confused disorders belong to different ICD-11 chapter groups. For example, `borderline_pattern_related` (personality disorders) being confused with `depressive_disorder_related` (mood disorders) at 66.1% error share suggests that self-reported language around borderline personality on Reddit frequently mirrors depressive framing rather than personality disorder framing. This aligns with known comorbidity patterns in the clinical literature.

### Why does depressive language dominate?
Nine of the ten strongest associations involve `depressive_disorder_related` as the predicted label. This reflects two things: (1) depression-related vocabulary is among the most common in the mental health Reddit dataset, making it the most frequent background prediction when the model is uncertain; and (2) many conditions share emotional distress vocabulary (hopelessness, exhaustion, inability to function) that overlaps heavily with depression's linguistic profile.

### Why do some labels have low F1?
Labels like `anxiety_or_fear_related_disorder` (F1 = 0.52) and `social_anxiety_related` (F1 = 0.64) have high recall but lower precision, meaning the model is over-predicting anxiety for posts from other conditions. This is linguistically expected — anxiety is a transdiagnostic feature present in many conditions. `alcohol_related_disorder` has zero test support due to sampling and should not be compared to other labels.

### Confidence and interpretation boundary
Any insight drawn from the seven uncertain mappings (`fact_mapping_uncertainty.csv`) should be qualified. For example, findings about `bpd → depressive` association are analytically valid as a language-level observation, but the claim that this reflects "borderline personality disorder" specifically is weakened by the medium confidence of the subreddit-to-disorder mapping.

---

## 7. Caveats and Limitations

1. **Subreddits are not diagnoses.** All subreddit-to-ICD-11 links are proxy mappings based on subreddit purpose and name. Posts in `r/depression` are not confirmed diagnoses of depressive disorder. All findings are language-level observations about Reddit communities.

2. **Sampling affects metric precision.** The binary task used 10% of the dataset (≈110,729 rows) and the multiclass task used 20% (≈67,339 rows). Displayed metrics are reliable estimates but would shift with full-dataset training. The direction of findings (relative model rankings, association patterns) is expected to be stable.

3. **ICD-11 alignment is approximate.** The `proxy_group_label` and `icd_proxy_category` columns are constructed from broad ICD-11 chapter names, not clinical coding. They should not be treated as equivalent to formal ICD-11 clinical coding.

4. **Association direction is asymmetric.** `health_anxiety → anxiety` having a high error share does not imply that `anxiety → health_anxiety` has the same strength. Always check the directionality of any association before making a claim.

5. **The analysis covers early COVID-19 period data.** Posts labelled `covid_period = 1` (the `post` timeframe) may reflect pandemic-related distress rather than pre-existing disorder patterns. This temporal confound is not controlled for in the RQ2 models and should be explored in subsequent research questions.
