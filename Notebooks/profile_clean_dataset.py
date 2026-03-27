from pathlib import Path
import json

import pandas as pd


def main() -> None:
    project_root = Path(__file__).resolve().parents[1]
    input_path = project_root / "Data" / "processed" / "reddit_mh_clean.parquet"
    out_path = project_root / "Data" / "processed" / "eda_artifacts" / "clean_dataset_profile.json"

    df = pd.read_parquet(input_path)

    summary = {
        "shape": {"rows": int(df.shape[0]), "columns": int(df.shape[1])},
        "column_order": list(df.columns),
        "columns": [],
    }

    for col in df.columns:
        s = df[col]
        info = {
            "name": col,
            "dtype": str(s.dtype),
            "null_count": int(s.isna().sum()),
            "null_pct": round(float(s.isna().mean() * 100), 4),
        }

        if pd.api.types.is_numeric_dtype(s):
            # Numeric unique counts are typically cheap enough and useful for dictionary metadata.
            info["n_unique"] = int(s.nunique(dropna=True))
            d = s.describe(percentiles=[0.25, 0.5, 0.75])
            info["min"] = float(d.get("min")) if d.get("min") is not None else None
            info["q1"] = float(d.get("25%")) if d.get("25%") is not None else None
            info["median"] = float(d.get("50%")) if d.get("50%") is not None else None
            info["q3"] = float(d.get("75%")) if d.get("75%") is not None else None
            info["max"] = float(d.get("max")) if d.get("max") is not None else None
            info["mean"] = float(d.get("mean")) if d.get("mean") is not None else None
        else:
            # Skip global unique count for text/list-heavy columns to keep profiling runtime stable.
            info["n_unique"] = None
            vals = s.dropna().astype(str)
            info["examples"] = [
                v[:120] + ("..." if len(v) > 120 else "") for v in vals.head(3).tolist()
            ]

        summary["columns"].append(info)

    out_path.write_text(json.dumps(summary, indent=2), encoding="utf-8")
    print(f"Wrote profile to: {out_path}")
    print(f"Rows: {summary['shape']['rows']}, Columns: {summary['shape']['columns']}")


if __name__ == "__main__":
    main()
