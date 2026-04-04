"""
00_clean.py
-----------
Data cleaning and preparation script for the ChatGPT availability
difference-in-differences analysis.

Loads raw languages + bans data, aggregates to country-quarter level,
constructs treatment indicators, runs diagnostics, and saves clean outputs.
"""

import json
import sys
from pathlib import Path

import numpy as np
import pandas as pd

# ── Project root (two levels above scripts/python/) ──────────────────────
PROJECT = Path(__file__).resolve().parents[2]

# ── Output directory ─────────────────────────────────────────────────────
CLEAN_DIR = PROJECT / "data" / "clean"
CLEAN_DIR.mkdir(parents=True, exist_ok=True)

# =========================================================================
# 1. Load languages.csv
# =========================================================================
def load_languages() -> pd.DataFrame:
    """Try data/external/ first (any .csv or .tab), then fallback path."""
    ext_dir = PROJECT / "data" / "external"

    # First: look for csv/tab files in data/external/
    if ext_dir.exists():
        candidates = list(ext_dir.glob("*.csv")) + list(ext_dir.glob("*.tab"))
        for f in candidates:
            if "ban" not in f.stem.lower():
                print(f"[INFO] Found languages file: {f.name}")
                sep = "\t" if f.suffix == ".tab" else ","
                return pd.read_csv(f, sep=sep)

    # Second: check pipeline_state.json for a stored path
    ps_path = PROJECT / "pipeline_state.json"
    if ps_path.exists():
        with open(ps_path, "r", encoding="utf-8") as fh:
            ps = json.load(fh)
        data_path = ps.get("stages", {}).get("stage1", {}).get("data_path")
        if data_path and Path(data_path).exists():
            print(f"[INFO] Loading languages from pipeline_state: {data_path}")
            return pd.read_csv(data_path)

    # Third: hard-coded fallback
    fallback = Path(r"C:\Users\jesus\Documents\data\languages.csv")
    if fallback.exists():
        print(f"[INFO] Loading languages from fallback: {fallback}")
        return pd.read_csv(fallback)

    sys.exit("[ERROR] Could not locate languages.csv anywhere.")


# =========================================================================
# 2. Load chatgpt_bans.csv
# =========================================================================
def load_bans() -> pd.DataFrame:
    bans_path = PROJECT / "data" / "external" / "chatgpt_bans.csv"
    if not bans_path.exists():
        sys.exit(f"[ERROR] Bans file not found: {bans_path}")
    print(f"[INFO] Loaded bans file: {bans_path.name}")
    return pd.read_csv(bans_path)


# =========================================================================
# Main pipeline
# =========================================================================
def main() -> None:
    print("=" * 60)
    print("  00_clean.py  --  Data Cleaning Pipeline")
    print("=" * 60)

    lang_df = load_languages()
    bans_df = load_bans()

    print(f"\n[DATA] languages.csv : {lang_df.shape[0]:,} rows x {lang_df.shape[1]} cols")
    print(f"[DATA] chatgpt_bans.csv : {bans_df.shape[0]:,} rows x {bans_df.shape[1]} cols")

    # -----------------------------------------------------------------
    # 3. Aggregate to country x quarter
    # -----------------------------------------------------------------
    agg = (
        lang_df
        .groupby(["iso2_code", "year", "quarter"], as_index=False)
        .agg(
            total_pushers=("num_pushers", "sum"),
            n_languages=("language", "nunique"),
        )
    )
    print(f"\n[AGG] Country-quarter panel: {agg.shape[0]:,} rows")

    # -----------------------------------------------------------------
    # 4. Derived variables
    # -----------------------------------------------------------------
    agg["quarter_id"] = agg["year"] * 10 + agg["quarter"]
    agg["log_pushers"] = np.log(agg["total_pushers"] + 1)

    # -----------------------------------------------------------------
    # 5. Merge with bans -- construct treatment dummies
    # -----------------------------------------------------------------
    persistent_codes = {"CN", "RU", "IR", "SY", "CU"}
    italy_code = "IT"

    agg["banned_persistent"] = agg["iso2_code"].isin(persistent_codes).astype(int)
    agg["italy_temp_ban"] = (agg["iso2_code"] == italy_code).astype(int)

    # Attach ban metadata for reference (left join, keep all country-quarters)
    agg = agg.merge(
        bans_df[["iso2_code", "country", "treatment_type"]],
        on="iso2_code",
        how="left",
    )
    agg["treatment_type"] = agg["treatment_type"].fillna("none")
    agg["country"] = agg["country"].fillna("")

    # -----------------------------------------------------------------
    # 6. Post-ChatGPT indicator (>= Q4 2022)
    # -----------------------------------------------------------------
    agg["post_chatgpt"] = (agg["quarter_id"] >= 20224).astype(int)

    # -----------------------------------------------------------------
    # 7. DiD interaction: treat_did = banned_persistent * post_chatgpt
    # -----------------------------------------------------------------
    agg["treat_did"] = agg["banned_persistent"] * agg["post_chatgpt"]

    print(f"[VAR] post_chatgpt == 1 for {agg['post_chatgpt'].sum():,} / {len(agg):,} rows")
    print(f"[VAR] treat_did   == 1 for {agg['treat_did'].sum():,} / {len(agg):,} rows")

    # -----------------------------------------------------------------
    # 8. Missingness audit
    # -----------------------------------------------------------------
    print("\n" + "-" * 60)
    print("  MISSINGNESS AUDIT")
    print("-" * 60)
    miss = agg.isnull().sum()
    miss_pct = (agg.isnull().mean() * 100).round(2)
    miss_report = pd.DataFrame({"n_missing": miss, "pct_missing": miss_pct})
    print(miss_report.to_string())

    report_lines = [
        "MISSINGNESS REPORT",
        "=" * 40,
        f"Total rows: {len(agg):,}",
        "",
        miss_report.to_string(),
        "",
        "Note: country name is blank for non-banned countries (expected).",
    ]
    miss_path = CLEAN_DIR / "missingness_report.txt"
    miss_path.write_text("\n".join(report_lines), encoding="utf-8")
    print(f"[SAVE] {miss_path.relative_to(PROJECT)}")

    # -----------------------------------------------------------------
    # 9. Outcome validation: correlation(log_pushers, treat_did)
    # -----------------------------------------------------------------
    print("\n" + "-" * 60)
    print("  OUTCOME VALIDATION")
    print("-" * 60)
    corr = agg["log_pushers"].corr(agg["treat_did"])
    print(f"  Pearson corr(log_pushers, treat_did) = {corr:.4f}")
    if abs(corr) < 0.01:
        print("  -> Very weak correlation; treatment effect may be small or absent.")
    elif corr < 0:
        print("  -> Negative correlation: banned countries show fewer pushers post-ChatGPT.")
    else:
        print("  -> Positive correlation: banned countries show more pushers post-ChatGPT.")

    # -----------------------------------------------------------------
    # 10. Balance table: pre-treatment means (banned vs non-banned)
    # -----------------------------------------------------------------
    print("\n" + "-" * 60)
    print("  BALANCE TABLE (pre-treatment means)")
    print("-" * 60)
    pre = agg[agg["post_chatgpt"] == 0].copy()
    balance_vars = ["total_pushers", "log_pushers", "n_languages"]

    balance_rows = []
    for var in balance_vars:
        mean_ban = pre.loc[pre["banned_persistent"] == 1, var].mean()
        mean_ctrl = pre.loc[pre["banned_persistent"] == 0, var].mean()
        diff = mean_ban - mean_ctrl
        balance_rows.append(
            {
                "variable": var,
                "mean_banned": round(mean_ban, 4),
                "mean_control": round(mean_ctrl, 4),
                "difference": round(diff, 4),
            }
        )

    balance_df = pd.DataFrame(balance_rows)
    print(balance_df.to_string(index=False))

    # -----------------------------------------------------------------
    # 11. Summary statistics
    # -----------------------------------------------------------------
    print("\n" + "-" * 60)
    print("  SUMMARY STATISTICS")
    print("-" * 60)
    summary_cols = [
        "total_pushers", "log_pushers", "n_languages",
        "banned_persistent", "italy_temp_ban", "post_chatgpt", "treat_did",
    ]
    summary_df = agg[summary_cols].describe().T
    summary_df = summary_df.round(4)
    print(summary_df.to_string())

    # -----------------------------------------------------------------
    # 12. Save outputs
    # -----------------------------------------------------------------
    print("\n" + "-" * 60)
    print("  SAVING CLEAN OUTPUTS")
    print("-" * 60)

    clean_path = CLEAN_DIR / "clean_data.csv"
    agg.to_csv(clean_path, index=False)
    print(f"[SAVE] {clean_path.relative_to(PROJECT)}  ({agg.shape[0]:,} rows)")

    summary_path = CLEAN_DIR / "summary_stats.csv"
    summary_df.to_csv(summary_path)
    print(f"[SAVE] {summary_path.relative_to(PROJECT)}")

    balance_path = CLEAN_DIR / "balance_table.csv"
    balance_df.to_csv(balance_path, index=False)
    print(f"[SAVE] {balance_path.relative_to(PROJECT)}")

    print(f"[SAVE] {miss_path.relative_to(PROJECT)}")

    print("\n" + "=" * 60)
    print("  DONE  --  All clean files saved to data/clean/")
    print("=" * 60)


if __name__ == "__main__":
    main()
