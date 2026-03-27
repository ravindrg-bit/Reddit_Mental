# Mental Health NLP Pipeline - Progress README

Generated on: 2026-03-27 18:21:28 GMT  
Prepared for: Ganenthra Ravindran

## 1) Project Context
This project builds a structured NLP workflow over Reddit data related to mental health and non-mental-health communities.

Current high-level workflow completed so far:
1. Load and merge many subreddit CSV feature files.
2. Add metadata labels from file names.
3. Clean and normalize text for NLP usage.
4. Generate exploratory NLP diagnostics and subgroup summaries.
5. Save reusable processed datasets and EDA artifacts.

## 2) Current Workspace Organization
- Data/raw: Source CSV files named using pattern <subreddit>_<timeframe>_features_tfidf_256.csv.
- Data/processed: Main processed parquet outputs.
- Data/processed/eda_artifacts: EDA summary CSV files.
- Notebooks:
  - 01_load_and_merge.ipynb
  - 02_Clean_and_Preprocess.ipynb
  - 03_basic_nlp_eda.ipynb

## 3) Steps Completed So Far (Detailed)

### Notebook 1: 01_load_and_merge.ipynb
Goal: Build one merged dataset from all raw CSV files.

Completed logic:
1. Imports and setup:
   - pathlib.Path, re, pandas.
2. Robust path resolution:
   - Detects project root whether notebook is run from Notebooks/ or project root.
   - Validates Data/raw exists.
3. Input/output directory setup:
   - Reads from Data/raw.
   - Ensures Data/processed exists.
4. File discovery:
   - Collects all CSV files in raw directory.
5. Filename parsing with regex:
   - Extracts subreddit and timeframe where timeframe is one of 2018, 2019, pre, post.
6. Label engineering for each loaded CSV:
   - subreddit column added.
   - timeframe column added.
   - is_mental_health created using a curated subreddit set.
   - covid_period set to 1 only for post timeframe.
7. Merge operation:
   - Concatenates all valid frames into merged_df.
8. Save output:
   - Writes Data/processed/reddit_mh_merged.parquet.
9. Logging:
   - Reports loaded file count, skipped file count, merged shape, output path.

Key implementation detail:
- This notebook explicitly prevents labeling 2019 as COVID period by using only timeframe == post for covid_period.

### Notebook 2: 02_Clean_and_Preprocess.ipynb
Goal: Clean and preprocess Reddit text into model-friendly form.

Completed logic:
1. Imports and dependencies:
   - pathlib.Path, re, pandas, nltk.
   - Stopwords and WordNet lemmatizer from NLTK.
2. NLTK resource download:
   - stopwords, wordnet, omw-1.4.
3. Data load:
   - Loads Data/processed/reddit_mh_merged.parquet.
   - Auto-detects text field from candidate columns: post, text, body, content.
4. Text normalization pipeline:
   - Lowercasing.
   - URL removal.
   - Reddit reference removal (r/... and u/...).
   - Removal of removed/deleted markers.
   - HTML entity replacement.
   - Non-alphanumeric cleanup while preserving apostrophes.
   - Whitespace normalization.
5. Tokenization and filtering:
   - Token regex for alphabetic terms and contractions.
   - Stopword removal with explicit preservation of negations.
6. Lemmatization:
   - Applies WordNet lemmatizer token-by-token.
7. New NLP columns:
   - clean_text.
   - tokens.
   - clean_word_count.
   - source_text_col.
8. Save output:
   - Writes Data/processed/reddit_mh_clean.parquet.

Key implementation detail:
- Negation words such as no, nor, not, never and contraction negations are intentionally preserved.

### Notebook 3: 03_basic_nlp_eda.ipynb
Goal: Perform foundational NLP EDA and generate downstream artifacts.

Completed logic:
1. Imports and display setup:
   - numpy, pandas, matplotlib, seaborn, ast, re.
2. Data and artifact path setup:
   - Loads Data/processed/reddit_mh_clean.parquet.
   - Ensures Data/processed/eda_artifacts exists.
3. Data validation:
   - Checks required columns: clean_text, subreddit, timeframe, is_mental_health, covid_period.
   - Captures null clean_text count before fill operations for accurate reporting.
4. Token handling robustness:
   - Normalizes token representations from list-like, string-like, or fallback parsing.
5. Feature engineering for EDA:
   - char_count_clean.
   - token_count_clean.
   - unique_token_count.
   - type_token_ratio.
   - avg_token_length.
   - negation_count.
6. Quality diagnostics:
   - rows, columns, duplicate_rows, duplicate_clean_text, null_clean_text, empty_clean_text, empty_token_rows.
7. Statistical summaries:
   - Feature distributions via describe with high percentiles.
8. Visual EDA:
   - Histograms and boxplots for key text-length and lexical-diversity metrics.
   - Subgroup plots by subreddit, is_mental_health, and covid_period.
9. Subgroup aggregate table:
   - Grouped summary by is_mental_health, covid_period, timeframe with count/mean/median/std.
10. Artifact export:
   - Data/processed/eda_artifacts/quality_summary.csv
   - Data/processed/eda_artifacts/feature_summary.csv
   - Data/processed/eda_artifacts/subgroup_summary.csv
11. Sampling for downstream modeling:
   - Creates stratified sample up to 50,000 rows using label strata when available.
   - Saves Data/processed/reddit_mh_clean_sample_50000.parquet.
   - Includes guardrails to fill shortfalls and assert final sample size.

## 4) Outputs Confirmed Present in Workspace
The following output files are already present:
1. Data/processed/reddit_mh_merged.parquet
2. Data/processed/reddit_mh_clean.parquet
3. Data/processed/reddit_mh_clean_sample_50000.parquet
4. Data/processed/eda_artifacts/quality_summary.csv
5. Data/processed/eda_artifacts/feature_summary.csv
6. Data/processed/eda_artifacts/subgroup_summary.csv

## 5) End-to-End Data Flow Completed
1. Raw subreddit CSVs in Data/raw.
2. Merge + metadata labels in Notebook 1.
3. Text cleaning and lemmatization in Notebook 2.
4. NLP quality checks, EDA, and artifact generation in Notebook 3.
5. Saved cleaned full dataset + sampled dataset + EDA summary files.

## 6) Re-run Instructions
To reproduce from scratch:
1. Ensure the Python environment has pandas, pyarrow, nltk, numpy, matplotlib, seaborn.
2. Run notebooks in order:
   - 01_load_and_merge.ipynb
   - 02_Clean_and_Preprocess.ipynb
   - 03_basic_nlp_eda.ipynb
3. Verify the output files listed in Section 4.

## 7) Notes and Assumptions Embedded in Current Pipeline
1. Raw file naming convention must match <subreddit>_<timeframe>_features_tfidf_256.csv.
2. Timeframe values expected: 2018, 2019, pre, post.
3. covid_period is defined strictly as post timeframe.
4. Text column is auto-detected from post/text/body/content.
5. Negations are intentionally retained during preprocessing due to sentiment relevance.

## 8) Current Project Status
Status: Data loading, cleaning, baseline NLP EDA, and artifact generation are completed.

Likely next stage:
1. Feature engineering and train/validation/test split strategy.
2. Baseline classification modeling.
3. Model evaluation and error analysis.
4. Experiment tracking and reproducibility hardening.

## 9) Data Folder Understanding and Feature Engineering Recommendation

### What each Data folder represents
1. Data/raw
   - Original source files.
   - Contains per-subreddit, per-timeframe CSVs using the pattern <subreddit>_<timeframe>_features_tfidf_256.csv.
   - Best used as immutable input data for reproducibility and reprocessing.

2. Data/processed
   - Canonical outputs from your notebooks.
   - Current files:
     - reddit_mh_merged.parquet: merged dataset with parsed labels (subreddit, timeframe, is_mental_health, covid_period).
     - reddit_mh_clean.parquet: text-cleaned dataset with clean_text, tokens, clean_word_count, and source_text_col.
     - reddit_mh_clean_sample_50000.parquet: stratified sample for faster experimentation.

3. Data/processed/eda_artifacts
   - Analytics outputs produced for diagnostics and reporting.
   - Current files: quality_summary.csv, feature_summary.csv, subgroup_summary.csv.
   - Useful for understanding data quality and subgroup behavior, but not as direct model inputs.

4. Data/features
   - Intended location for engineered feature matrices.
   - Currently empty in this workspace.
   - Recommended place to store generated training-ready features (for example TF-IDF, embeddings, lexical/metadata features, target-ready tables).

### Recommendation: Which data to use for feature engineering
1. Primary recommendation
   - Use Data/processed/reddit_mh_clean.parquet as the main source for feature engineering.
   - Reason: it is already cleaned, tokenized, and enriched with core labels and metadata needed for supervised modeling.

2. When to use the sample file
   - Use Data/processed/reddit_mh_clean_sample_50000.parquet for prototyping, hyperparameter trials, and debugging pipelines quickly.
   - After pipeline stability, rerun feature generation on the full cleaned dataset.

3. When to use raw and merged data
   - Use Data/raw only for re-ingestion or if you need to change parsing/label assumptions.
   - Use Data/processed/reddit_mh_merged.parquet when you want to redesign the text-cleaning pipeline from an earlier stage.

4. Suggested operational pattern
   - Read from reddit_mh_clean.parquet.
   - Generate engineered features.
   - Save final feature tables into Data/features with versioned names (for example: mh_features_tfidf_v1.parquet, mh_features_dense_v1.parquet).
