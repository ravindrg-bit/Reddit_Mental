# Advanced NLP EDA — Code Documentation

Generated on: 2026-04-02  
Notebook: EDA_Reddit.ipynb  

---

## 1) Project Context

This notebook extends the foundational NLP EDA already completed across three earlier notebooks (01_load_and_merge, 02_Clean_and_Preprocess, 03_basic_nlp_eda). It applies a suite of advanced text analysis methods to the cleaned, lemmatised Reddit dataset to characterise how mental health communities differ from non-mental-health communities in vocabulary, topic structure, and linguistic proximity — and how those patterns shifted around the onset of COVID-19.

The full dataset at this stage:
- Rows: 1,107,302
- Subreddits: 28
- Mental health share: 42.6%
- COVID period share (post timeframe): 28.9%
- Total columns in parquet: 357 (342 loaded selectively)

Segments covered in this notebook: S1 · S2 · S3 · S4 · S5 · S10 · S11 · S13 · S14

> **Scope note:** Segments S6 (sentiment by group), S7 (LIWC group profile), S8 (lexicon signals), S9 (readability profile), and S12 (effect sizes) are present in the pipeline and reflected in the run manifest (S14). They are excluded from this documentation because their outputs are covered as scope in other parts of the wider project. They can be unlocked and documented on request.

---

## 2) S1 — Setup and Configuration

### Purpose
Install additional dependencies, import all required libraries, mount Google Drive, configure all project paths, and build a validated column manifest from the parquet schema before any data is loaded.

### Libraries installed
- `wordcloud`: word cloud generation
- `gensim`: LDA topic modelling and coherence scoring
- `networkx`: co-occurrence network graph construction

### Libraries imported
Standard scientific stack (numpy, pandas, matplotlib, seaborn, scipy), plus pyarrow for selective parquet reads, sklearn for vectorisation and cosine similarity, networkx for graphs, and wordcloud for visual EDA.

### Path configuration
```
PROJECT_ROOT  → /content/drive/MyDrive
PROCESSED_DIR → PROJECT_ROOT/Data/processed
ARTIFACT_DIR  → PROCESSED_DIR/eda_artifacts/advanced_eda/
PARQUET_PATH  → PROCESSED_DIR/reddit_mh_clean.parquet
SAMPLE_PATH   → PROCESSED_DIR/reddit_mh_clean_sample_50000.parquet
```
Both parquet paths are validated with `assert p.exists()` before proceeding.

### Column manifest (built dynamically from schema)
Rather than hardcoding column names, the manifest is built by reading the parquet schema and applying prefix/suffix matching rules:

| Group | Selection Rule | Count |
|---|---|---:|
| metadata | Hardcoded list | 4 |
| text | Hardcoded (clean_text) | 1 |
| sentiment | Starts with `sent_` | 4 |
| liwc | Starts with `liwc_` | 62 |
| lexicon | Ends with `_total` | 6 |
| tfidf | Starts with `tfidf_` | 256 |
| readability | Named list intersected with schema | 9 |
| **Total loaded** | | **342 of 357** |

Columns excluded from load: `post` (raw text), `author`, `tokens`, `source_text_col`. This reduces memory footprint without losing analytical columns.

Global constants set here:
- `RANDOM_STATE = 42` — used consistently across all stochastic operations

---

## 3) S2 — Selective Data Load

### Purpose
Load only the columns specified in the S1 manifest using PyArrow (faster and lower-memory than pandas default), downcast numeric types to reduce RAM usage, and generate the 50k stratified sample directly from the validated full dataset.

### Key implementation details

**Selective PyArrow read:**
```python
tbl = pq.read_table(str(PARQUET_PATH), columns=LOAD_COLS)
df = downcast_df(tbl.to_pandas())
```
The `downcast_df` helper converts int64 → smallest integer type and float64 → float32 wherever possible, skipping text and metadata columns. The raw table object is immediately deleted and garbage collected after conversion.

**Post-load cleaning:**
- `clean_text` filled with empty string and stripped
- `is_mental_health` and `covid_period` cast explicitly to int
- Derived display labels added: `group_label` (Mental Health / Non-MH), `period_label` (2018 / 2019 / Pre-COVID / Post-COVID)

**Full dataset confirmed stats:**
```
Rows          : 1,107,302
Columns loaded: 344
MH share      : 42.6%
COVID period  : 28.9%
Subreddits    : 28
```

**50k sample generation:**
The sample is generated directly from the loaded `df` (not from the pre-saved sample parquet) to ensure metadata consistency. Stratification is by `is_mental_health` using proportional allocation:
```python
df_sample = df_valid.groupby('is_mental_health').apply(get_sample)
```
Sample result: 49,999 rows, 42.6% MH, all 28 subreddits represented. This sample is used for all computationally intensive sections (S5, S10, S13) that cannot run efficiently over 1.1 million rows.

---

## 4) S3 — Word Frequency Analysis

### Purpose
Build vocabulary frequency profiles for mental health and non-mental-health communities, identify the most common terms in each group, and visualise the difference through bar charts and word clouds.

### Method
A chunked counter approach is used to avoid loading all tokens into RAM simultaneously. Text is processed in windows of 50,000 rows; each window contributes to a running `Counter` object.

**Domain stop-word augmentation:**
Standard English stop-words are augmented with a curated set of high-frequency but low-signal Reddit terms (e.g., `like`, `just`, `know`, `get`, `im`, `ive`, `dont`). This prevents generic discourse terms from dominating the visualisation. Negation words are retained — a deliberate design choice carried forward from preprocessing.

**Minimum token length:** 3 characters.

### Key findings

| Rank | Mental Health | Count | Non-MH | Count |
|---|---|---:|---|---:|
| 1 | not | 463,396 | not | 636,082 |
| 2 | don't | 278,239 | year | 405,364 |
| 3 | life | 277,614 | month | 262,812 |
| 4 | year | 256,725 | day | 245,356 |
| 5 | day | 238,412 | work | 221,915 |

The high frequency of "not" and "don't" in the MH corpus reflects the intentional preservation of negation tokens during preprocessing — these carry sentiment signal not captured by removing them. The Non-MH top vocabulary shifts toward temporal and practical terms (year, month, work), consistent with subreddits focused on finance, relationships, and daily logistics.

### Outputs
- `s3_word_freq_top30.png` — side-by-side horizontal bar charts, top 30 terms per group
- `s3_wordclouds.png` — word clouds for top 300 terms per group (Blues / Oranges palette)
- `s3_word_freq_by_group.csv` — top 150 terms per group with raw counts

---

## 5) S4 — TF-IDF Distinctive Terms

### Purpose
Identify which of the 256 pre-computed TF-IDF vocabulary terms most strongly discriminate mental health subreddits from non-mental-health subreddits, and detect which terms rose or fell in salience after COVID-19 onset.

### Method
This section performs pure numeric aggregation — no text is re-scanned. The 256 `tfidf_*` columns already present in the dataset are grouped by `is_mental_health` and by `covid_period`, and mean TF-IDF weights are computed per group.

**Discriminative score:** `diff = MH mean − Non-MH mean` for each of the 256 terms.

> **Important — stemmed vocabulary:** The 256 TF-IDF terms are lemmatised/stemmed forms, not surface words. Terms such as `depress`, `anxieti`, `feel`, and `veri` are stems produced by the WordNet lemmatiser in preprocessing. Display labels in any downstream visualisation should map these to readable equivalents (e.g., `depress` → `depression`, `anxieti` → `anxiety`, `veri` → `very`).

### Key findings

**Top terms distinctive of Mental Health (positive diff):**

| Term (stemmed) | MH Mean | Non-MH Mean | Diff |
|---|---:|---:|---:|
| feel | 0.0863 | 0.0226 | +0.0638 |
| depress | 0.0418 | 0.0030 | +0.0388 |
| anxieti | 0.0383 | 0.0024 | +0.0359 |
| life | 0.0459 | 0.0118 | +0.0341 |
| like | 0.0697 | 0.0377 | +0.0297 |

**Top terms distinctive of Non-MH (negative diff):**

| Term (stemmed) | MH Mean | Non-MH Mean | Diff |
|---|---:|---:|---:|
| would | 0.0238 | 0.0489 | −0.0251 |
| month | 0.0160 | 0.0403 | −0.0243 |
| us | 0.0146 | 0.0376 | −0.0231 |
| question | 0.0079 | 0.0277 | −0.0198 |
| ask | 0.0090 | 0.0268 | −0.0188 |

The full discriminative range across all 256 terms is −0.025 to +0.064.

**COVID TF-IDF shift:** A second chart shows terms that rose or fell in mean TF-IDF weight between the pre-COVID (2018, 2019, pre) and post-COVID (post) periods across all subreddits. Terms rising post-COVID include `hous`, `care`, `everyth`, `pleas`, `kill`, `health`. Terms falling include `experi`, `pretti`, `month`, `school`, `start`, `anxieti`. The falling of `anxieti` post-COVID is counterintuitive and may reflect compositional changes in subreddit activity rather than a true reduction in anxiety expression.

### Outputs
- `s4_tfidf_distinctive.png` — side-by-side bar charts, top 20 discriminative terms per group
- `s4_tfidf_covid_shift.png` — top 15 rising and falling terms, post vs pre-COVID
- `s4_tfidf_distinctive_terms.csv` — all 256 terms with mh_mean, nonmh_mean, diff, abs_diff

---

## 6) S5 — N-gram Analysis

### Purpose
Extract the most frequent bigrams (two-word phrases) and trigrams (three-word phrases) from each community using the 50k stratified sample, and visualise the co-occurrence structure of the top MH bigrams as a network graph.

### Method
`CountVectorizer` from scikit-learn is fitted on the sample text for each group separately. Parameters: `max_features=8000`, `min_df=3`, `stop_words="english"`. The top N phrases by document frequency are extracted.

A NetworkX spring-layout graph is built from the top 15 MH bigrams, where nodes are individual words and edge weight encodes co-occurrence count.

### Key findings

**Mental Health — top bigrams (50k sample):**

| Phrase | Count |
|---|---:|
| feel like | 8,864 |
| don know | 3,546 |
| don want | 1,887 |
| mental health | 1,338 |
| panic attack | 1,284 |

"feel like" occurs more than 2.5× as frequently as the second-ranked bigram, establishing it as the dominant phrase pattern in MH discourse — typically in constructions expressing subjective emotional state ("I feel like I'm failing", "feel like nobody understands").

**Non-MH — top bigrams (50k sample):**

| Phrase | Count |
|---|---:|
| feel like | 3,447 |
| tl dr | 2,840 |
| don know | 2,443 |
| year old | 2,434 |
| credit card | 2,046 |

Non-MH bigrams include both universal discourse patterns ("feel like", "don know") and community-specific transactional phrases ("credit card", "tl dr" — the Reddit shorthand for "too long, didn't read").

**Mental Health — top trigrams (50k sample):**

| Phrase | Count |
|---|---:|
| make feel like | 247 |
| feel like going | 207 |
| long story short | 196 |
| don know anymore | 195 |
| don feel like | 191 |

The MH trigrams are dominated by subjective experience constructions and expressions of resignation ("don know anymore"). Non-MH trigrams are more situational ("credit card debt", "long story short", "tl dr boyfriend").

### Outputs
- `s5_bigrams.png` — top 25 bigrams per group, horizontal bar charts
- `s5_trigrams.png` — top 20 trigrams per group, horizontal bar charts
- `s5_bigram_network_mh.png` — co-occurrence network for top 15 MH bigrams
- `s5_ngram_freq.csv` — all phrases with count, n (2 or 3), and group

---

## 7) S10 — LDA Topic Modelling

### Purpose
Discover latent thematic structure across the 50k sample using Latent Dirichlet Allocation (LDA), select the optimal number of topics through a coherence scan, fit a final high-quality model, and profile topic prevalence by mental health group and COVID period.

### Method

**Corpus construction (streaming):**
Gensim's `Dictionary` is built from tokenised `clean_text`, then filtered to tokens appearing in at least 10 documents and no more than 85% of the corpus, keeping the top 8,000 by frequency. The corpus is represented as a list of bag-of-words vectors.

```
Dictionary size : 8,000 tokens
Corpus size     : 49,986 documents
```

**Coherence scan:**
LDA models are fitted for topic counts 5 through 12, each with 1 pass (reduced for speed). Coherence is measured using the `c_v` metric from Gensim's `CoherenceModel`. The best score selects the final topic count.

| Topics | Coherence (c_v) |
|---:|---:|
| 5 | 0.3198 |
| 6 | 0.3706 |
| 7 | 0.3494 |
| 8 | 0.3452 |
| 9 | 0.3496 |
| **10** | **0.3803** |
| 11 | 0.3691 |
| 12 | 0.3691 |

**Best: 10 topics (c_v = 0.3803)**

**Final model:** Fitted with 12 passes, `alpha="auto"`, `eta="auto"`, `chunksize=2000`, `random_state=42`.

> **Coherence caveat:** The scan-phase models (1 pass each) triggered Gensim warnings about insufficient updates. These models are used only for selection, not for interpretation. The final 12-pass model is substantially better trained. However, the c_v score of 0.38 indicates moderate — not high — topic coherence, which is typical for mixed-domain Reddit corpora. Topic labels should be treated as provisional interpretations.

### Topic inventory and provisional labels

The following labels are interpretive, assigned based on the top 5 words per topic. They should be validated against the full word distributions in `s10_lda_topic_words.csv`.

| Topic | Top 5 Words | Provisional Label |
|---|---|---|
| 1 | eat, food, eating, tax, binge | Eating & Nutrition |
| 2 | people, not, like, one, thought | General Discourse |
| 3 | money, year, pay, k, job | Financial Stress |
| 4 | would, help, looking, advice, anyone | Help-Seeking |
| 5 | mom, parent, year, kid, home | Family & Parenting |
| 6 | anxiety, get, day, help, time | Anxiety & Daily Life |
| 7 | x, b, weight, day, body | Physical Health Markers* |
| 8 | mg, not, car, call, got | Medical / Medication* |
| 9 | job, work, not, day, week | Work & Employment |
| 10 | like, feel, know, not, want | Emotional Disclosure |

> *Topics 7 and 8 contain ambiguous top words. "x" and "b" in Topic 7 likely reflect Unicode artefacts or abbreviated units (e.g., "x200b" — a zero-width space from Reddit markdown) that survived preprocessing. "mg" in Topic 8 suggests medication dosage discussion. These topics require manual inspection of the full word distribution before labelling with confidence.

### Topic distribution by group and COVID period

**Mean topic probability by mental health group:**

| Topic | MH=0 (Non-MH) | MH=1 (Mental Health) |
|---|---:|---:|
| topic_1 | 0.028 | 0.010 |
| topic_2 | 0.086 | 0.087 |
| topic_3 | 0.121 | 0.014 |
| topic_6 | 0.082 | 0.076 |
| topic_9 | 0.079 | 0.020 |
| **topic_10** | **0.273** | **0.545** |

Topic 10 (Emotional Disclosure) is the dominant topic for the MH group at a mean probability of 0.545 — roughly double its prevalence in Non-MH communities (0.273). Topic 3 (Financial Stress) is nearly absent in MH posts (0.014) but prominent in Non-MH (0.121), consistent with r/personalfinance and r/legaladvice driving that signal.

**COVID period shift:** Topic distributions across pre-COVID and post-COVID periods are very similar, with the largest individual shift being approximately 0.006 on topic 10. This suggests that the thematic structure of Reddit discourse at the topic level was broadly stable before and after COVID onset — though S4 (TF-IDF) and S11 (cosine similarity) reveal more granular vocabulary-level shifts.

### Outputs
- `s10_coherence_curve.png` — coherence score vs topic count, with best-n marker
- `s10_lda_top_words_grid.png` — 10-panel bar grid, top 12 words per topic
- `s10_topic_group_period.png` — bar chart (MH vs Non-MH) and heatmap (COVID period)
- `s10_lda_topic_words.csv` — top 15 words per topic with probability scores
- `s10_lda_topic_dist.csv` — per-document topic probability vectors with metadata

---

## 8) S11 — Cosine Similarity Between Subreddits

### Purpose
Compute pairwise linguistic similarity between all 28 subreddits using their mean TF-IDF vectors, identify which communities are most linguistically alike, and detect whether subreddit vocabularies converged or diverged during the COVID period.

### Method
Each subreddit is represented as the mean of its documents' 256-dimensional TF-IDF vectors, producing a 28×256 matrix. Scikit-learn's `cosine_similarity` computes the full 28×28 pairwise similarity matrix. A second pass computes separate matrices for pre-COVID and post-COVID periods; the delta (post − pre) reveals convergence or divergence.

### Key findings

**Overall similarity:**
- Mean non-self cosine similarity: 0.761
- Minimum cosine similarity: 0.522

All 28 subreddits share a high baseline similarity (minimum 0.52), which reflects the shared Reddit dialect — common words, discourse conventions, and posting norms dominate the TF-IDF space. Discriminative signal sits in the top terms identified in S4.

**Most similar subreddit pairs:**

| Pair | Cosine Similarity |
|---|---:|
| depression ↔ mentalhealth | 0.952 |
| bipolarreddit ↔ schizophrenia | 0.944 |
| depression ↔ suicidewatch | 0.943 |

Mental health subreddits form a tightly clustered linguistic group. The hierarchical clustermap (s11_cosine_clustermap.png) reveals two high-level clusters: MH communities and Non-MH communities, with some overlap at the periphery (e.g., r/lonely sits closer to MH despite not being labelled as such).

> **Self-similarity artefact:** The notebook printed `('suicidewatch', 'suicidewatch')` as the most similar pair with a score of 1.0. This is a code artefact — the `.replace(1.0, 0).idxmax()` logic did not correctly exclude self-pairs in that output line. The actual most similar non-self pair from the CSV data is depression–mentalhealth at 0.952, as reported above.

**COVID convergence/divergence (top pairs):**

| Direction | Pair | Delta |
|---|---|---:|
| Most convergent | addiction ↔ ptsd | +0.031 |
| Most convergent | addiction ↔ jokes | +0.030 |
| Most divergent | autism ↔ teaching | −0.035 |
| Most divergent | EDAnonymous ↔ teaching | −0.029 |

The convergence of r/addiction and r/ptsd post-COVID suggests these communities began using more similar vocabulary — potentially reflecting shared themes of isolation and crisis. The divergence of r/autism and r/teaching from each other may reflect pandemic-specific topic shifts pulling those communities in different directions.

### Outputs
- `s11_cosine_heatmap.png` — full 28×28 heatmap (YlOrRd)
- `s11_cosine_clustermap.png` — dendrogrammed clustermap
- `s11_cosine_delta.png` — post minus pre COVID delta heatmap (RdBu)
- `s11_cosine_similarity_matrix.csv` — full 28×28 similarity matrix
- `s11_cosine_delta_matrix.csv` — full 27×27 delta matrix (subreddits present in both periods)

---

## 9) S13 — Word Relationships and PMI Co-occurrence

### Purpose
Identify word pairs that co-occur together more often than would be expected by chance, using Pointwise Mutual Information (PMI). PMI surfaces semantically tight associations that raw frequency misses — rare but strongly coupled pairs score highly.

### Method
PMI is computed on the 50k stratified sample for each group separately:

```
PMI(x, y) = log₂ [ P(x, y) / (P(x) × P(y)) ]
```

`CountVectorizer` is used to build unigram and bigram frequency vectors (vocab_size=3,000, min_df=8). PMI is computed for all bigrams whose component words both appear in the unigram vocabulary and whose raw frequency meets the minimum threshold.

Network graphs are built from the top 20 PMI pairs per group, with edge weights proportional to PMI score.

### Key findings

**Mental Health — top PMI pairs:**

| Bigram | PMI Score | Frequency |
|---|---:|---:|
| pin needle | 7.40 | 32 |
| ups down | 6.83 | 49 |
| minimum wage | 6.65 | 33 |
| sexually assaulted | 6.57 | 36 |
| blah blah | 6.46 | 72 |
| cbd oil | 6.38 | 21 |
| discord server | 6.29 | 28 |
| downward spiral | 6.23 | 47 |
| anti depressant | 6.02 | 145 |
| bare minimum | 6.00 | 29 |

> **PMI noise flag:** "pin needle" and "ups down" are the top two MH PMI pairs. These are likely preprocessing artefacts — "pins and needles" (a sensory symptom) and "ups and downs" (an idiomatic phrase) have had their conjunctions stripped during cleaning, leaving tight but fragmented pairs. They are not clinically meaningful associations and should be excluded or relabelled in any downstream presentation. Pairs such as "sexually assaulted", "anti depressant", "downward spiral", and "coping mechanism" (further down the list) are substantively informative.

**Non-MH — top PMI pairs:**

| Bigram | PMI Score | Frequency |
|---|---:|---:|
| blah blah | 7.24 | 65 |
| north carolina | 6.61 | 78 |
| lump sum | 6.57 | 105 |
| domestic violence | 6.32 | 40 |
| pro con | 5.80 | 65 |
| mixed signal | 5.80 | 26 |
| passive aggressive | 5.78 | 42 |
| authorized user | 5.77 | 40 |
| south carolina | 5.67 | 41 |
| bi weekly | 5.63 | 48 |

Non-MH pairs reflect a mix of geographic references (north/south carolina — likely r/legaladvice threads), financial terminology (lump sum, authorized user, bi weekly), and interpersonal discourse (domestic violence, passive aggressive, mixed signal).

### Outputs
- `s13_pmi_bar_charts.png` — top 35 PMI pairs per group, horizontal bar charts
- `s13_pmi_networks.png` — top 20 PMI pairs per group as network graphs
- `s13_pmi_pairs.csv` — all pairs with bigram, w1, w2, PMI score, frequency, group

---

## 10) S14 — Artifact Export and Run Manifest

### Purpose
Generate a master inventory of all output files produced by the notebook, recording file name, originating segment, row count, column count, file size, and generation timestamp.

### Manifest contents

| File Name | Segment | Rows | Columns | Size (KB) |
|---|---|---:|---:|---:|
| s10_lda_topic_dist.csv | S10 | 49,986 | 13 | 6,588.8 |
| s10_lda_topic_words.csv | S10 | 150 | 4 | 2.8 |
| s11_cosine_delta_matrix.csv | S11 | 27 | 28 | 9.7 |
| s11_cosine_similarity_matrix.csv | S11 | 28 | 29 | 8.5 |
| s12_effect_sizes.csv | S12 | 12 | 6 | 0.7 |
| s12_temporal_signal_pivot.csv | S12 | 8 | 10 | 1.2 |
| s13_pmi_pairs.csv | S13 | 70 | 6 | 3.4 |
| s3_word_freq_by_group.csv | S3 | 300 | 3 | 6.7 |
| s4_tfidf_distinctive_terms.csv | S4 | 256 | 5 | 13.7 |
| s5_ngram_freq.csv | S5 | 90 | 4 | 2.7 |
| s6_sentiment_by_group.csv | S6 | 108 | 7 | 6.1 |
| s7_liwc_group_profile.csv | S7 | 55 | 65 | 25.3 |
| s8_lexicon_signals.csv | S8 | 108 | 9 | 7.6 |
| s9_readability_profile.csv | S9 | 28 | 11 | 2.0 |

Generated at: 2026-04-02 03:43:41

> **Scope note:** S6, S7, S8, S9, and S12 artifacts appear in the manifest and are present in the pipeline output directory. They are excluded from this documentation because those outputs are covered as scope in other parts of the wider project. They remain available and can be documented on request.

### Output
- `s14_run_manifest.csv` — master artifact inventory

---

## 11) Notes and Assumptions Embedded in This Notebook

1. The 50k stratified sample (S2) is regenerated from the full `df` at runtime rather than loaded from the pre-saved parquet. This ensures metadata columns are consistent with the current run.
2. Domain stop-words (S3) are manually curated and embedded in the cell. Any changes to this list will alter word frequency and PMI outputs.
3. LDA (S10) uses `passes=1` during the coherence scan and `passes=12` for the final model. The scan-phase models are discarded.
4. The 256 TF-IDF columns (S4, S11) are pre-computed in the raw feature files, not re-derived in this notebook. Their content reflects the vocabulary selected during the original feature engineering phase.
5. Word2Vec was explicitly excluded from S13 to maintain runtime within Google Colab free-tier limits. It can be added in a local environment without memory constraints.
6. PMI minimum frequency threshold is `min_df=8` for the sample. Lowering this threshold will surface more pairs but increase noise.
