from pathlib import Path
import json
from datetime import datetime, timezone


def infer_definition(col: str) -> str:
    explicit = {
        "subreddit": "Source subreddit name extracted from filename.",
        "author": "Reddit author username as provided in source data.",
        "date": "Post date string from source dataset.",
        "post": "Original raw post text before cleaning.",
        "timeframe": "Temporal split extracted from filename (2018, 2019, pre, post).",
        "is_mental_health": "Binary label: 1 if subreddit belongs to curated mental-health set, else 0.",
        "covid_period": "Binary indicator: 1 for post period, 0 otherwise.",
        "clean_text": "Normalized and lemmatized text generated in preprocessing.",
        "tokens": "Token list produced from normalized text.",
        "clean_word_count": "Number of tokens in clean_text.",
        "source_text_col": "Original text column used as source during preprocessing.",
        "sent_neg": "VADER negative sentiment score.",
        "sent_neu": "VADER neutral sentiment score.",
        "sent_pos": "VADER positive sentiment score.",
        "sent_compound": "VADER compound sentiment score in [-1, 1].",
    }
    if col in explicit:
        return explicit[col]
    if col.startswith("tfidf_"):
        term = col.replace("tfidf_", "")
        return f"TF-IDF feature weight for token/ngram '{term}'."
    if col.startswith("liwc_"):
        cat = col.replace("liwc_", "")
        return f"LIWC-style linguistic category feature for '{cat}'."
    if col.endswith("_total"):
        group = col.replace("_total", "")
        return f"Lexicon/category total count for '{group}' terms in the post."
    if col.startswith("n_"):
        return "Text-length/readability count feature derived from source text."
    if col in {
        "automated_readability_index",
        "coleman_liau_index",
        "flesch_kincaid_grade_level",
        "flesch_reading_ease",
        "gulpease_index",
        "gunning_fog_index",
        "lix",
        "smog_index",
        "wiener_sachtextformel",
    }:
        return "Readability metric computed from the post text."
    if col == "punctuation":
        return "Punctuation-related text feature from the original dataset."
    return "Engineered feature carried from upstream data processing."


def infer_feature_group(col: str) -> str:
    if col in {"subreddit", "author", "date", "timeframe", "source_text_col"}:
        return "metadata"
    if col in {"post", "clean_text", "tokens"}:
        return "text"
    if col in {"is_mental_health", "covid_period"}:
        return "labels"
    if col.startswith("tfidf_"):
        return "tfidf"
    if col.startswith("liwc_"):
        return "liwc"
    if col.startswith("sent_"):
        return "sentiment"
    if col.endswith("_total"):
        return "lexicon_totals"
    if col.startswith("n_") or col in {
        "automated_readability_index",
        "coleman_liau_index",
        "flesch_kincaid_grade_level",
        "flesch_reading_ease",
        "gulpease_index",
        "gunning_fog_index",
        "lix",
        "smog_index",
        "wiener_sachtextformel",
        "punctuation",
        "clean_word_count",
    }:
        return "readability_length"
    return "other"


def fmt_num(value):
    if value is None:
        return ""
    if isinstance(value, float):
        return f"{value:.4f}"
    return str(value)


def main() -> None:
    project_root = Path(__file__).resolve().parents[1]
    profile_path = project_root / "Data" / "processed" / "eda_artifacts" / "clean_dataset_profile.json"
    out_path = project_root / "Data" / "data_dictionary.md"

    profile = json.loads(profile_path.read_text(encoding="utf-8"))
    rows = profile["shape"]["rows"]
    cols = profile["shape"]["columns"]

    group_counts = {}
    for c in profile["columns"]:
        g = infer_feature_group(c["name"])
        group_counts[g] = group_counts.get(g, 0) + 1

    generated_at = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")

    lines = []
    lines.append("# Data Dictionary: reddit_mh_clean.parquet")
    lines.append("")
    lines.append(f"Generated: {generated_at}")
    lines.append("")
    lines.append("## Dataset Overview")
    lines.append(f"- File: Data/processed/reddit_mh_clean.parquet")
    lines.append(f"- Rows: {rows:,}")
    lines.append(f"- Columns: {cols}")
    lines.append("")
    lines.append("## Feature Group Summary")
    lines.append("| Group | Column Count |")
    lines.append("|---|---:|")
    for g in sorted(group_counts):
        lines.append(f"| {g} | {group_counts[g]} |")

    lines.append("")
    lines.append("## Column Dictionary")
    lines.append("List format understanding of each column:")
    lines.append("")

    for i, c in enumerate(profile["columns"], start=1):
        name = c["name"]
        group = infer_feature_group(name)
        dtype = c.get("dtype", "")
        null_count = c.get("null_count", 0)
        null_pct = c.get("null_pct", 0)
        nunique = "" if c.get("n_unique") is None else str(c.get("n_unique"))
        definition = infer_definition(name).replace("|", "\\|")
        example = ""
        if c.get("examples"):
            example = str(c["examples"][0]).replace("|", "\\|").replace("\n", " ")
            if len(example) > 80:
                example = example[:80] + "..."

        stats = (
            f"nulls={null_count} ({fmt_num(null_pct)}%), unique={nunique or 'n/a'}, "
            f"min={fmt_num(c.get('min')) or 'n/a'}, q1={fmt_num(c.get('q1')) or 'n/a'}, "
            f"median={fmt_num(c.get('median')) or 'n/a'}, q3={fmt_num(c.get('q3')) or 'n/a'}, "
            f"max={fmt_num(c.get('max')) or 'n/a'}, mean={fmt_num(c.get('mean')) or 'n/a'}"
        )

        lines.append(f"{i}. {name}")
        lines.append(f"   - Group: {group}")
        lines.append(f"   - Type: {dtype}")
        lines.append(f"   - Understanding: {definition}")
        lines.append(f"   - Profile: {stats}")
        if example:
            lines.append(f"   - Example: {example}")
        lines.append("")

    lines.append("")
    lines.append("* Unique counts are reported for numeric columns; for large text/list columns they are intentionally omitted for profiling performance.")

    out_path.write_text("\n".join(lines), encoding="utf-8")
    print(f"Wrote data dictionary: {out_path}")


if __name__ == "__main__":
    main()
