# EDA Outputs Guide and Power BI Implementation Reference

Generated on: 2026-04-02   

---

## 1) Overview

This document describes the nine primary output files produced by the advanced NLP EDA pipeline (`EDA_Reddit.ipynb`) and provides step-by-step instructions for building a Power BI dashboard from them.

The nine files collectively provide four analytical lenses on Reddit mental health discourse (1,107,302 posts, 28 subreddits, 2018–2020):

| Lens | Files |
|---|---|
| Vocabulary signatures | s3_word_freq_by_group.csv, s4_tfidf_distinctive_terms.csv |
| Phrase and association patterns | s5_ngram_freq.csv, s13_pmi_pairs.csv |
| Latent topic structure | s10_lda_topic_words.csv, s10_lda_topic_dist.csv |
| Community linguistic relationships | s11_cosine_similarity_matrix.csv, s11_cosine_delta_matrix.csv |
| Pipeline inventory | s14_run_manifest.csv |

> **Scope note:** Five additional artifact files are present in the pipeline output directory and listed in the run manifest — s6_sentiment_by_group.csv, s7_liwc_group_profile.csv, s8_lexicon_signals.csv, s9_readability_profile.csv, and s12_effect_sizes.csv. These are excluded from this guide because their outputs are covered as scope in other parts of the wider project. They remain available and can be incorporated into the Power BI model on request.

---

## 2) File Reference

---

### 2.1) s3_word_freq_by_group.csv

**Segment:** S3 — Word Frequency Analysis  
**Rows:** 300 (150 terms × 2 groups)  
**Size:** 6.7 KB

**Schema:**

| Column | Type | Description |
|---|---|---|
| word | str | Surface-form token (lowercased, min 3 characters) |
| count | int | Total raw occurrence count across all posts in the group |
| group | str | Community label: `mental_health` or `non_mh` |

**Key statistics:**

| Rank | MH Word | MH Count | Non-MH Word | Non-MH Count |
|---|---|---:|---|---:|
| 1 | not | 463,396 | not | 636,082 |
| 2 | don't | 278,239 | year | 405,364 |
| 3 | life | 277,614 | month | 262,812 |
| 4 | year | 256,725 | day | 245,356 |
| 5 | day | 238,412 | work | 221,915 |

**Interpretation:**
The high frequency of negation tokens ("not", "don't") in the MH corpus is a deliberate feature of the preprocessing pipeline — negation words were explicitly preserved because they carry sentiment signal. This means raw word frequency alone is not a proxy for positivity or negativity. The Non-MH vocabulary shifts toward temporal and transactional terms (year, month, work) reflecting subreddit communities focused on finance, employment, and logistics.

**Notes and flags:**
- Counts reflect the full 1.1M-row dataset, not the 50k sample
- Domain stop-words were applied (e.g., `like`, `just`, `know` excluded); standard English stop-words were also removed
- This file contains surface-form words, not stems — contrast with s4 which uses stemmed forms

---

### 2.2) s4_tfidf_distinctive_terms.csv

**Segment:** S4 — TF-IDF Distinctive Terms  
**Rows:** 256  
**Size:** 13.7 KB

**Schema:**

| Column | Type | Description |
|---|---|---|
| term | str | Stemmed/lemmatised token from the TF-IDF vocabulary |
| mh_mean | float | Mean TF-IDF weight for this term across all MH posts |
| nonmh_mean | float | Mean TF-IDF weight for this term across all Non-MH posts |
| diff | float | Discriminative score: mh_mean − nonmh_mean |
| abs_diff | float | Absolute value of diff |

**Key statistics:**

| Term (stem) | Readable Form | diff |
|---|---|---:|
| feel | feel | +0.0638 |
| depress | depression | +0.0388 |
| anxieti | anxiety | +0.0359 |
| life | life | +0.0341 |
| like | like | +0.0297 |
| would | would | −0.0251 |
| month | month | −0.0243 |
| us | us | −0.0231 |
| question | question | −0.0197 |
| ask | ask | −0.0188 |

Discriminative score range: −0.025 to +0.064 across all 256 terms.

**Interpretation:**
Positive `diff` means the term is more characteristic of MH communities; negative `diff` means it is more characteristic of Non-MH communities. The magnitude reflects how strongly the term separates the two groups in TF-IDF space. A `diff` of +0.064 for "feel" is the strongest signal in the vocabulary — mental health posts are consistently oriented around subjective emotional experience.

> **Important — stemmed vocabulary:** All 256 terms are lemmatised or stemmed forms produced during preprocessing. Stems that may require display-name mapping for readability include: `depress` → depression, `anxieti` → anxiety, `veri` → very, `whi` → why, `worri` → worry, `suicid` → suicide, `anymor` → anymore. A lookup table should be applied in Power BI before displaying these as chart labels.

**Notes and flags:**
- `diff` and `abs_diff` are computed on the full 1.1M-row dataset (all timeframes combined)
- This file does not contain COVID-period shift data; that analysis is visualised in `s4_tfidf_covid_shift.png` but not separately exported as a CSV

---

### 2.3) s5_ngram_freq.csv

**Segment:** S5 — N-gram Analysis  
**Rows:** 90 (25 bigrams + 20 trigrams × 2 groups)  
**Size:** 2.7 KB

**Schema:**

| Column | Type | Description |
|---|---|---|
| phrase | str | Bigram or trigram phrase (space-separated tokens) |
| count | int | Document frequency in the 50k stratified sample |
| n | int | Phrase length: 2 = bigram, 3 = trigram |
| group | str | Community label: `mental_health` or `non_mh` |

**Key statistics:**

**Mental health — top bigrams:**

| Phrase | Count |
|---|---:|
| feel like | 8,864 |
| don know | 3,546 |
| don want | 1,887 |
| mental health | 1,338 |
| panic attack | 1,284 |

**Non-MH — top bigrams:**

| Phrase | Count |
|---|---:|
| feel like | 3,447 |
| tl dr | 2,840 |
| don know | 2,443 |
| year old | 2,434 |
| credit card | 2,046 |

**Mental health — top trigrams:**

| Phrase | Count |
|---|---:|
| make feel like | 247 |
| feel like going | 207 |
| long story short | 196 |
| don know anymore | 195 |
| don feel like | 191 |

**Interpretation:**
"feel like" is the dominant MH bigram at 8,864 occurrences — 2.5× more frequent than the second-ranked phrase. It anchors a family of subjective-experience constructions present in the top trigrams ("make feel like", "feel like going", "don feel like"). The Non-MH bigrams include community-specific discourse markers ("tl dr") and transactional topics ("credit card", "year old" — common in r/relationships and r/legaladvice threads).

**Notes and flags:**
- Counts are from the 50k sample, not the full dataset — scale accordingly for any proportional comparison with S3
- English stop-words applied via `CountVectorizer`; `min_df=3` means phrases appearing in fewer than 3 documents are excluded
- Conjunctions and articles are removed, which produces fragments like "don know" instead of "don't know" — this is expected behaviour

---

### 2.4) s10_lda_topic_words.csv

**Segment:** S10 — LDA Topic Modelling  
**Rows:** 150 (15 words × 10 topics)  
**Size:** 2.8 KB

**Schema:**

| Column | Type | Description |
|---|---|---|
| topic | int | Topic number (1–10) |
| rank | int | Word rank within topic by probability (1 = highest) |
| word | str | Stemmed token |
| probability | float | Probability of this word given the topic |

**Topic inventory with provisional labels:**

> **Analyst note — labels are interpretive:** The following topic labels are provisional, assigned based on the top 5 words per topic. They should be validated by the analyst before use in any presented output. Topics 7 and 8 contain ambiguous top words that may reflect preprocessing artefacts (see flags below).

| Topic | Top Words | Provisional Label |
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

> *Topic 7 ("x", "b"): these tokens likely reflect Unicode zero-width spaces (x200b) or abbreviated measurement units that survived preprocessing. The presence of "weight" and "body" alongside them suggests a physical health cluster but should be verified by inspecting sample documents with high topic_7 probability. Topic 8 ("mg"): suggests medication dosage discussion, but "car" and "call" introduce ambiguity — possible blending of medication threads and general logistics posts.

**Interpretation:**
This file defines the semantic content of each topic. It is used in conjunction with s10_lda_topic_dist.csv (which records per-document topic prevalences) to understand what the communities are discussing and how those themes vary by group and period.

---

### 2.5) s10_lda_topic_dist.csv

**Segment:** S10 — LDA Topic Modelling  
**Rows:** 49,986  
**Size:** 6,588.8 KB (largest file)

**Schema:**

| Column | Type | Description |
|---|---|---|
| topic_1 … topic_10 | float | Per-document probability for each of the 10 topics (rows sum to ~1.0) |
| is_mental_health | int | Binary label: 1 = MH subreddit, 0 = Non-MH |
| covid_period | int | Binary label: 1 = post timeframe, 0 = all other timeframes |
| subreddit | str | Source subreddit name |

**Key statistics — mean topic probability by group:**

| Topic | Non-MH (MH=0) | Mental Health (MH=1) |
|---|---:|---:|
| topic_1 (Eating) | 0.028 | 0.010 |
| topic_2 (General) | 0.086 | 0.087 |
| topic_3 (Financial) | 0.121 | 0.014 |
| topic_4 (Help-Seeking) | 0.053 | 0.046 |
| topic_5 (Family) | 0.052 | 0.027 |
| topic_6 (Anxiety) | 0.082 | 0.076 |
| topic_7 (Physical) | 0.066 | 0.035 |
| topic_8 (Medical) | 0.123 | 0.021 |
| topic_9 (Work) | 0.079 | 0.020 |
| topic_10 (Emotional) | 0.273 | **0.545** |

**COVID period shift (pre vs post):** Minimal at the topic level. The largest individual change is approximately +0.006 on topic_10 post-COVID. Topic-level distributions were broadly stable across the pandemic onset, while more granular vocabulary shifts are captured in S4 and S11.

**Interpretation:**
Topic 10 (Emotional Disclosure) dominates MH posts with a mean probability of 0.545 — nearly double its Non-MH prevalence. Topic 3 (Financial Stress) and Topic 9 (Work & Employment) are nearly absent in MH communities (0.014 and 0.020) but prominent in Non-MH (0.121 and 0.079). Topic 8 (Medical/Medication), interestingly, is higher in Non-MH (0.123) than MH (0.021) — possibly reflecting the practical medication-logistics threads common in non-clinical subreddits like r/legaladvice or r/fitness.

**Notes and flags:**
- This file contains 49,986 rows (one per document in the 50k sample) — it is the largest file and may require query-time aggregation in Power BI rather than row-level display
- Topic probabilities per row do not sum to exactly 1.0 due to `minimum_probability=0` filtering in Gensim's `get_document_topics`

---

### 2.6) s11_cosine_similarity_matrix.csv

**Segment:** S11 — Cosine Similarity Between Subreddits  
**Rows:** 28  
**Size:** 8.5 KB

**Schema:**
Square matrix. The first column (unnamed, loaded as index) contains subreddit names. All remaining 28 columns are also subreddit names. Cell value = cosine similarity between the two subreddits' mean TF-IDF vectors.

| Property | Value |
|---|---|
| Dimensions | 28 × 28 |
| Diagonal values | 1.0 (self-similarity) |
| Value range | 0.522 – 1.000 |
| Mean non-self similarity | 0.761 |

**Most similar non-self pairs:**

| Subreddit A | Subreddit B | Similarity |
|---|---|---:|
| depression | mentalhealth | 0.952 |
| bipolarreddit | schizophrenia | 0.944 |
| depression | suicidewatch | 0.943 |

**Interpretation:**
All subreddits share a high baseline similarity (minimum 0.522) because Reddit's shared language and posting norms dominate the TF-IDF space. The highest similarities are between MH subreddits that share clinical vocabulary. Hierarchical clustering of this matrix (s11_cosine_clustermap.png) reveals two macro-clusters corresponding broadly to MH and Non-MH communities.

**Notes and flags:**
- The matrix is symmetric — each pair appears twice (A→B and B→A). Filter to the upper or lower triangle in Power BI to avoid duplicate pairs in rankings
- Diagonal (self-similarity = 1.0) should be excluded from any "most similar pair" analysis

---

### 2.7) s11_cosine_delta_matrix.csv

**Segment:** S11 — Cosine Similarity Between Subreddits  
**Rows:** 27  
**Size:** 9.7 KB

**Schema:**
Square matrix. Same structure as s11_cosine_similarity_matrix.csv. Cell value = post-COVID similarity minus pre-COVID similarity. Positive = more similar post-COVID (convergence); negative = less similar post-COVID (divergence).

| Property | Value |
|---|---|
| Dimensions | 27 × 27 |
| Subreddits | 27 (subreddits present in both pre and post periods) |
| Value range | approximately −0.035 to +0.031 |
| Diagonal values | 0.0 (self-delta is always zero) |

**Most convergent pairs (post-COVID):**

| Subreddit A | Subreddit B | Delta |
|---|---|---:|
| addiction | ptsd | +0.031 |
| addiction | jokes | +0.030 |
| jokes | ptsd | +0.028 |

**Most divergent pairs (post-COVID):**

| Subreddit A | Subreddit B | Delta |
|---|---|---:|
| autism | teaching | −0.035 |
| EDAnonymous | teaching | −0.029 |
| EDAnonymous | conspiracy | −0.029 |

**Interpretation:**
Delta values are small in absolute magnitude (max ±0.035), indicating that the overall linguistic similarity structure between subreddits was relatively stable before and after COVID onset. The convergence of r/addiction and r/ptsd is the most notable signal — these communities moved closer linguistically post-COVID, possibly reflecting shared themes of crisis, isolation, and treatment disruption. The divergence of r/teaching from multiple communities may reflect the sudden and specific vocabulary shift around remote schooling.

**Notes and flags:**
- One subreddit present in pre-COVID data was absent from post-COVID data and is excluded, producing a 27×27 matrix rather than 28×28
- Symmetric matrix — apply the same upper/lower triangle filter as with the similarity matrix
- Diagonal values are 0.0 (not 1.0 as in the similarity matrix)

---

### 2.8) s13_pmi_pairs.csv

**Segment:** S13 — Word Relationships and PMI Co-occurrence  
**Rows:** 70 (35 pairs × 2 groups)  
**Size:** 3.4 KB

**Schema:**

| Column | Type | Description |
|---|---|---|
| bigram | str | The word pair as a space-separated string |
| w1 | str | First word in the pair |
| w2 | str | Second word in the pair |
| pmi | float | Pointwise Mutual Information score (log₂ scale) |
| freq | int | Raw co-occurrence count in the 50k sample |
| group | str | Community label: `mental_health` or `non_mh` |

**Key statistics:**

**Mental health — top 10 PMI pairs:**

| Bigram | PMI | Frequency |
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

**Non-MH — top 10 PMI pairs:**

| Bigram | PMI | Frequency |
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

**Interpretation:**
PMI captures associative strength, not frequency. "anti depressant" (PMI 6.02, freq 145) is the highest-frequency clinically meaningful MH pair — the relatively high count makes it a more reliable signal than low-frequency pairs. Non-MH pairs reflect legal and financial community contexts (lump sum, authorized user, bi weekly) and interpersonal advice (domestic violence, passive aggressive, mixed signal).

> **PMI noise flag:** The top two MH pairs — "pin needle" and "ups down" — are preprocessing artefacts. "Pins and needles" (a somatic anxiety symptom) and "ups and downs" (an idiom for emotional variability) have had their conjunctions stripped during text cleaning, creating artificially tight pairs. These should be relabelled or excluded in any presented output. Similarly, "blah blah" (top in both groups) is a Reddit discourse marker with no analytical value.

---

### 2.9) s14_run_manifest.csv

**Segment:** S14 — Artifact Export  
**Rows:** 14  
**Size:** reference

**Schema:**

| Column | Type | Description |
|---|---|---|
| file_name | str | Output filename |
| segment | str | Notebook segment that generated this file |
| row_count | int | Number of data rows in the file |
| column_count | int | Number of columns |
| file_size_kb | float | File size in kilobytes |
| generated_at | datetime | Timestamp of generation |

**Full manifest:**

| File | Segment | Rows | Columns | KB | Generated |
|---|---|---:|---:|---:|---|
| s10_lda_topic_dist.csv | S10 | 49,986 | 13 | 6,588.8 | 2026-04-02 03:43:41 |
| s10_lda_topic_words.csv | S10 | 150 | 4 | 2.8 | 2026-04-02 03:43:41 |
| s11_cosine_delta_matrix.csv | S11 | 27 | 28 | 9.7 | 2026-04-02 03:43:41 |
| s11_cosine_similarity_matrix.csv | S11 | 28 | 29 | 8.5 | 2026-04-02 03:43:41 |
| s12_effect_sizes.csv | S12 | 12 | 6 | 0.7 | 2026-04-02 03:43:41 |
| s12_temporal_signal_pivot.csv | S12 | 8 | 10 | 1.2 | 2026-04-02 03:43:41 |
| s13_pmi_pairs.csv | S13 | 70 | 6 | 3.4 | 2026-04-02 03:43:41 |
| s3_word_freq_by_group.csv | S3 | 300 | 3 | 6.7 | 2026-04-02 03:43:41 |
| s4_tfidf_distinctive_terms.csv | S4 | 256 | 5 | 13.7 | 2026-04-02 03:43:41 |
| s5_ngram_freq.csv | S5 | 90 | 4 | 2.7 | 2026-04-02 03:43:41 |
| s6_sentiment_by_group.csv | S6 | 108 | 7 | 6.1 | 2026-04-02 03:43:41 |
| s7_liwc_group_profile.csv | S7 | 55 | 65 | 25.3 | 2026-04-02 03:43:41 |
| s8_lexicon_signals.csv | S8 | 108 | 9 | 7.6 | 2026-04-02 03:43:41 |
| s9_readability_profile.csv | S9 | 28 | 11 | 2.0 | 2026-04-02 03:43:41 |

> **Scope note:** S6, S7, S8, S9, and S12 are present in the manifest and in the pipeline output directory. They are excluded from this guide because those outputs are covered as scope in other parts of the wider project. They can be incorporated into the Power BI model on request.

---

## 3) Power BI — Ingestion Steps

### Step 1 — Load the nine CSV files

1. Open Power BI Desktop → Home → Get Data → Text/CSV
2. Load each of the nine files in sequence. Suggested table names:

| File | Power BI Table Name |
|---|---|
| s3_word_freq_by_group.csv | WordFreq |
| s4_tfidf_distinctive_terms.csv | TFIDFTerms |
| s5_ngram_freq.csv | Ngrams |
| s10_lda_topic_words.csv | TopicWords |
| s10_lda_topic_dist.csv | TopicDist |
| s11_cosine_similarity_matrix.csv | CosineSimilarity |
| s11_cosine_delta_matrix.csv | CosineDelta |
| s13_pmi_pairs.csv | PMIPairs |
| s14_run_manifest.csv | RunManifest |

3. For `s10_lda_topic_dist.csv` (49,986 rows, 6.6 MB): Power BI will load this without issue, but ensure all `topic_1` through `topic_10` columns are typed as Decimal Number, and `is_mental_health` and `covid_period` as Whole Number.

### Step 2 — Data type enforcement

Apply these type overrides in Power Query (Transform Data) for each table:

**WordFreq:**
- word → Text
- count → Whole Number
- group → Text

**TFIDFTerms:**
- term → Text
- mh_mean, nonmh_mean, diff, abs_diff → Decimal Number

**Ngrams:**
- phrase → Text
- count → Whole Number
- n → Whole Number
- group → Text

**TopicWords:**
- topic → Whole Number
- rank → Whole Number
- word → Text
- probability → Decimal Number

**TopicDist:**
- topic_1 through topic_10 → Decimal Number
- is_mental_health, covid_period → Whole Number
- subreddit → Text

**CosineSimilarity / CosineDelta:**
- These load as wide matrices. Use the Unpivot Columns transformation (select the subreddit name columns → Transform → Unpivot Columns) to convert to long format with three columns: Subreddit_A (the index column, rename from "Column1"), Subreddit_B (the Attribute column), Value (the Value column).

**PMIPairs:**
- bigram, w1, w2, group → Text
- pmi → Decimal Number
- freq → Whole Number

### Step 3 — Transform the cosine matrices to long format

For both CosineSimilarity and CosineDelta after loading:

1. In Power Query, select the first column (subreddit names) → Right-click → Do Not Unpivot This Column
2. Select all remaining columns → Transform → Unpivot Columns
3. Rename resulting columns: the original index column → `Subreddit_A`, Attribute → `Subreddit_B`, Value → `Similarity` (or `Delta`)
4. For CosineSimilarity: add a filter step to exclude rows where Subreddit_A = Subreddit_B (self-pairs with value 1.0)
5. For CosineDelta: add a filter step to exclude rows where Subreddit_A = Subreddit_B (self-pairs with value 0.0)
6. To avoid duplicate pairs (A→B and B→A), add a conditional column: `keep_row = if Subreddit_A < Subreddit_B then 1 else 0` and filter to keep_row = 1

### Step 4 — Add a stem-to-readable lookup table

Create a new table manually (Enter Data) to map stemmed TF-IDF terms to readable display names. Minimum recommended entries:

| stem | readable |
|---|---|
| depress | depression |
| anxieti | anxiety |
| suicid | suicide |
| anymor | anymore |
| worri | worry |
| veri | very |
| whi | why |
| realli | really |
| togeth | together |
| someth | something |

Relate this table to `TFIDFTerms[term]` on a many-to-one basis. Use the `readable` column in all TF-IDF visuals.

### Step 5 — Relationships

The files do not share a direct key column, but the following conceptual links are useful for cross-filtering:

| From Table | Column | To Table | Column | Relationship |
|---|---|---|---|---|
| TopicDist | subreddit | CosineSimilarity (long) | Subreddit_A | Many-to-Many (use as filter only) |
| PMIPairs | group | WordFreq | group | Many-to-One |
| Ngrams | group | WordFreq | group | Many-to-One |
| TopicWords | topic | TopicDist (aggregated measure) | topic | One-to-Many |

For most visuals, relationships are not strictly necessary — filters and slicers by `group` and `is_mental_health` drive the cross-filtering within individual pages.

---

## 4) Recommended Visuals per File

### WordFreq (s3)

**Visual 1 — Top N words by group (bar chart):**
- Type: Clustered horizontal bar chart
- Y-axis: word
- X-axis: count
- Legend: group
- Filter: Top N by count (recommended N = 20)
- Slicer: group (mental_health / non_mh)

**Visual 2 — Vocabulary overlap table:**
- Type: Table
- Columns: word, MH Count (measure filtered to mental_health), Non-MH Count (measure filtered to non_mh), MH Rank, Non-MH Rank
- Sort by MH Count descending

---

### TFIDFTerms (s4)

**Visual 1 — Discriminative terms bar chart:**
- Type: Clustered horizontal bar chart
- Y-axis: readable (from stem lookup table)
- X-axis: diff (or abs_diff for absolute magnitude)
- Conditional formatting on bars: positive diff in blue (#4A7BB5), negative diff in orange (#C96A45)
- Filter: Top 20 by abs_diff

**Visual 2 — Scatter plot (MH mean vs Non-MH mean):**
- Type: Scatter chart
- X-axis: nonmh_mean
- Y-axis: mh_mean
- Values: readable (term label)
- Reference line: diagonal (X = Y) to show parity
- Points above the diagonal = MH-distinctive; below = Non-MH-distinctive

---

### Ngrams (s5)

**Visual 1 — Bigram frequency by group:**
- Type: Clustered horizontal bar chart
- Y-axis: phrase
- X-axis: count
- Filter: n = 2
- Slicer: group
- Sort by count descending, Top 15

**Visual 2 — Trigram frequency by group:**
- Same configuration as Visual 1 with filter: n = 3

**Visual 3 — N-gram comparison table:**
- Type: Matrix
- Rows: phrase
- Columns: group
- Values: count
- Filter: n = 2 or n = 3 (use page slicer)

---

### TopicWords (s10_lda_topic_words.csv) and TopicDist (s10_lda_topic_dist.csv)

**Visual 1 — Topic word bar grid:**
- Type: One bar chart per topic (use small multiples or individual chart objects)
- Y-axis: word
- X-axis: probability
- Filter: one topic per chart (topic = 1 through 10)
- Recommended layout: 2 rows × 5 columns matching the notebook grid

**Visual 2 — Topic prevalence by community type (grouped bar chart):**
- Requires aggregation of TopicDist: create measures for mean topic probability per group
  - `MH_Topic1 = CALCULATE(AVERAGE(TopicDist[topic_1]), TopicDist[is_mental_health]=1)`
  - Repeat for all 10 topics and both groups
- Type: Clustered bar chart
- X-axis: topic label (use provisional topic names)
- Y-axis: mean probability
- Legend: Community (MH / Non-MH)

**Visual 3 — COVID period heatmap:**
- Requires aggregation by covid_period
- Type: Matrix
- Rows: covid_period (relabelled as Pre-COVID / Post-COVID)
- Columns: topic label
- Values: mean probability (formatted as 3 decimal places)
- Background colour scale: Blues

---

### CosineSimilarity and CosineDelta (s11)

**Visual 1 — Top similar pairs table:**
- From the long-format CosineSimilarity table
- Type: Table
- Columns: Subreddit_A, Subreddit_B, Similarity
- Filter: Subreddit_A ≠ Subreddit_B, keep upper triangle only
- Sort by Similarity descending
- Conditional formatting on Similarity: colour scale from white (low) to red (high)

**Visual 2 — Convergence/divergence ranked table:**
- From the long-format CosineDelta table
- Type: Table or bar chart
- Columns: Subreddit_A, Subreddit_B, Delta
- Sort by Delta descending (most convergent) or ascending (most divergent)
- Conditional formatting: positive delta in blue, negative in red

**Visual 3 — Subreddit similarity matrix (heatmap):**
- Note: Native matrix heatmaps in Power BI require the HTML Content visual or a custom visual (e.g., Charticulator or Deneb). The full 28×28 heatmap is best served by the pre-generated PNG (s11_cosine_heatmap.png) embedded as an image object on the dashboard page, with the Power BI tables providing the interactive drill-through layer.

---

### PMIPairs (s13)

**Visual 1 — PMI bar chart by group:**
- Type: Clustered horizontal bar chart
- Y-axis: bigram
- X-axis: pmi
- Slicer: group
- Recommended filter: exclude "blah blah", "pin needle", "ups down" (noise pairs — see flags in section 2.8)
- Sort by pmi descending, Top 20

**Visual 2 — PMI vs frequency scatter:**
- Type: Scatter chart
- X-axis: freq (log scale recommended)
- Y-axis: pmi
- Values: bigram
- Legend: group
- This view distinguishes high-PMI/low-frequency pairs (specific but noisy) from lower-PMI/high-frequency pairs (more reliable associations)

---

### RunManifest (s14)

**Visual — Artifact inventory table:**
- Type: Table
- Columns: file_name, segment, row_count, column_count, file_size_kb, generated_at
- Sort by segment ascending
- Use as a reference page or tooltip in the dashboard

---

## 5) Recommended Dashboard Layout

| Page | Title | Primary Files Used | Core Question |
|---|---|---|---|
| 1 | Community Overview | WordFreq, TFIDFTerms | How do MH and Non-MH communities differ in language? |
| 2 | Phrase Patterns | Ngrams, PMIPairs | What are the dominant phrases and word associations per community? |
| 3 | Topic Intelligence | TopicWords, TopicDist | What themes dominate each community, and did they shift post-COVID? |
| 4 | Community Relationships | CosineSimilarity, CosineDelta | How linguistically similar are subreddits, and did COVID change that? |
| 5 | Pipeline Reference | RunManifest | What artifacts were generated and when? |

**Page-level filters to apply consistently across all pages:**
- Slicer: group (mental_health / non_mh) — where applicable
- Slicer: is_mental_health (0 / 1) — for TopicDist aggregations
- Slicer: covid_period (0 = Pre / 1 = Post) — for COVID comparisons

---

## 6) General Notes for Power BI Implementation

1. **s10_lda_topic_dist.csv is row-level data, not summary data.** All topic visualisations from this file require DAX measures using CALCULATE and AVERAGE, not direct column references. Do not display raw row-level topic probabilities as-is.

2. **Matrix files (s11) must be unpivoted before use.** Loading them as wide matrices will prevent filtering and ranking. Apply the unpivot transformation described in Step 3 of Section 3.

3. **Stemmed terms in s4 require display mapping.** Do not use the `term` column directly in chart labels. Apply the stem-to-readable lookup table described in Step 4 of Section 3.

4. **PMI noise pairs should be excluded from headline visuals.** The pairs "pin needle", "ups down", and "blah blah" are preprocessing artefacts or discourse fillers. Filter these out before displaying PMI results to a non-technical audience.

5. **Counts in s5 (ngrams) are from the 50k sample.** Do not directly compare these counts with counts in s3 (full dataset). If proportional comparison is needed, normalise s5 counts by sample size (49,999) and s3 counts by group size.

6. **LDA topic labels are provisional.** Before finalising the dashboard, validate the topic labels in section 2.4 against the full `s10_lda_topic_words.csv` word distributions and, if possible, against a sample of documents with high probability on each topic.
