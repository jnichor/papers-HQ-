"""
00_clean.py — Data Cleaning & Panel Construction
=================================================
Loads languages.csv + ef_epi_2025.csv, audits missingness,
constructs the country×quarter analysis panel with HHI and Shannon entropy.

Outputs:
  - data/clean/clean_data.csv          (country×quarter panel)
  - data/clean/summary_stats.csv       (summary statistics table)
  - data/clean/missingness_report.txt  (missingness audit log)
"""

import sys
from pathlib import Path
import numpy as np
import pandas as pd
from scipy import stats

# ── Paths ─────────────────────────────────────────────────────────────────────
PROJECT = Path(__file__).resolve().parents[2]
RAW_DATA = Path(r"C:\Users\jesus\Documents\data\languages.csv")
EPI_DATA = PROJECT / "data" / "external" / "ef_epi_2025.csv"
CLEAN_DIR = PROJECT / "data" / "clean"
CLEAN_DIR.mkdir(parents=True, exist_ok=True)

REPORT_PATH = CLEAN_DIR / "missingness_report.txt"
report_lines = []

def log(msg):
    print(msg)
    report_lines.append(msg)


# ═══════════════════════════════════════════════════════════════════════════════
# 1. LOAD RAW DATA
# ═══════════════════════════════════════════════════════════════════════════════
log("=" * 70)
log("00_clean.py — Data Cleaning & Panel Construction")
log("=" * 70)

df = pd.read_csv(RAW_DATA)
log(f"\n[load] languages.csv: {df.shape[0]:,} rows x {df.shape[1]} cols")
log(f"[load] Columns: {list(df.columns)}")

epi = pd.read_csv(EPI_DATA)
log(f"[load] ef_epi_2025.csv: {epi.shape[0]} rows x {epi.shape[1]} cols")


# ═══════════════════════════════════════════════════════════════════════════════
# 2. MISSINGNESS AUDIT
# ═══════════════════════════════════════════════════════════════════════════════
log("\n" + "=" * 70)
log("MISSINGNESS AUDIT")
log("=" * 70)

# (a) Missingness table: % missing per variable
log("\n[miss] Percentage missing per variable:")
miss_pct = df.isnull().mean() * 100
for col in df.columns:
    log(f"  {col:20s}: {miss_pct[col]:6.2f}%  ({df[col].isnull().sum():,} missing)")

total_missing = df.isnull().any(axis=1).sum()
log(f"\n[miss] Rows with ANY missing value: {total_missing:,} / {len(df):,} ({total_missing/len(df)*100:.2f}%)")

# (b) Test MCAR vs MAR vs MNAR
if total_missing > 0:
    log("\n[miss] MCAR/MAR/MNAR test:")
    # Little's MCAR test approximation: compare missingness patterns
    # across observed variables using chi-squared test
    miss_indicator = df.isnull().astype(int)
    any_missing_cols = [c for c in df.columns if df[c].isnull().any()]

    for col in any_missing_cols:
        # Test if missingness in col is related to observed values in other cols
        miss_mask = df[col].isnull()
        numeric_cols = df.select_dtypes(include=[np.number]).columns.tolist()
        for other_col in numeric_cols:
            if other_col == col:
                continue
            obs_when_miss = df.loc[miss_mask, other_col].dropna()
            obs_when_present = df.loc[~miss_mask, other_col].dropna()
            if len(obs_when_miss) > 1 and len(obs_when_present) > 1:
                t_stat, p_val = stats.ttest_ind(obs_when_miss, obs_when_present, equal_var=False)
                if p_val < 0.05:
                    log(f"  [MAR] Missingness in '{col}' associated with '{other_col}' (t={t_stat:.2f}, p={p_val:.4f})")

    log("\n[miss] Strategy: Listwise deletion (drop rows with missing values)")
    log(f"  Justification: Missing rate is {total_missing/len(df)*100:.2f}%. "
        "At this level, listwise deletion introduces minimal bias and "
        "is the most transparent approach for referee review.")
else:
    log("\n[miss] NO MISSING VALUES DETECTED — no imputation needed.")
    log("[miss] Strategy: Complete case analysis (no rows dropped).")

n_before = len(df)
df = df.dropna()
n_after = len(df)
log(f"\n[miss] Observations dropped: {n_before - n_after:,}")
log(f"[miss] Observations remaining: {n_after:,}")


# ═══════════════════════════════════════════════════════════════════════════════
# 3. DATA VALIDATION
# ═══════════════════════════════════════════════════════════════════════════════
log("\n" + "=" * 70)
log("DATA VALIDATION")
log("=" * 70)

# Create quarter_id for temporal ordering
df["quarter_id"] = df["year"].astype(int) * 10 + df["quarter"].astype(int)
quarters_sorted = sorted(df["quarter_id"].unique())
log(f"\n[val] Unique quarter_ids: {quarters_sorted}")
log(f"[val] N quarters: {len(quarters_sorted)}")
log(f"[val] N countries: {df['iso2_code'].nunique()}")
log(f"[val] N languages: {df['language'].nunique()}")

# Verify num_pushers is positive
assert (df["num_pushers"] > 0).all(), "ERROR: num_pushers contains non-positive values"
log("[val] num_pushers: all positive [OK]")

# Check for duplicates at language x country x quarter level
dupes = df.duplicated(subset=["language", "iso2_code", "year", "quarter"], keep=False)
if dupes.any():
    log(f"[val] WARNING: {dupes.sum()} duplicate language×country×quarter rows found — aggregating")
    df = df.groupby(["language", "language_type", "iso2_code", "year", "quarter"], as_index=False)["num_pushers"].sum()
    df["quarter_id"] = df["year"].astype(int) * 10 + df["quarter"].astype(int)
else:
    log("[val] No duplicate language x country x quarter rows [OK]")


# ═══════════════════════════════════════════════════════════════════════════════
# 4. CONSTRUCT COUNTRY×QUARTER PANEL
# ═══════════════════════════════════════════════════════════════════════════════
log("\n" + "=" * 70)
log("PANEL CONSTRUCTION")
log("=" * 70)

# Step 1: Compute language shares within each country-quarter
df["total_pushers_cq"] = df.groupby(["iso2_code", "year", "quarter"])["num_pushers"].transform("sum")
df["share"] = df["num_pushers"] / df["total_pushers_cq"]

log(f"\n[panel] Language-level rows: {len(df):,}")

# Step 2: Aggregate to country x quarter
def compute_hhi_entropy(group):
    shares = group["share"].values
    n_langs = len(shares)

    # Raw HHI
    hhi_raw = np.sum(shares ** 2)

    # Normalized HHI: (raw - 1/N) / (1 - 1/N)
    if n_langs > 1:
        hhi_norm = (hhi_raw - 1 / n_langs) / (1 - 1 / n_langs)
    else:
        hhi_norm = 1.0

    # Shannon entropy
    entropy = -np.sum(shares * np.log(shares + 1e-15))

    return pd.Series({
        "hhi_raw": hhi_raw,
        "hhi_norm": hhi_norm,
        "entropy": entropy,
        "n_languages": n_langs,
        "total_pushers": group["num_pushers"].sum(),
        "log_pushers": np.log(group["num_pushers"].sum()),
    })


panel = (
    df.groupby(["iso2_code", "year", "quarter", "quarter_id"])
    .apply(compute_hhi_entropy, include_groups=False)
    .reset_index()
)

log(f"[panel] Country×quarter panel: {len(panel):,} rows")
log(f"[panel] N countries: {panel['iso2_code'].nunique()}")
log(f"[panel] N quarters: {panel['quarter_id'].nunique()}")

# Step 3: Check panel balance
full_panel_size = panel["iso2_code"].nunique() * panel["quarter_id"].nunique()
log(f"[panel] Expected balanced panel size: {full_panel_size:,}")
log(f"[panel] Actual panel size: {len(panel):,}")
log(f"[panel] Balance rate: {len(panel) / full_panel_size * 100:.1f}%")

# Flag balanced countries (present in all quarters)
n_quarters_total = panel["quarter_id"].nunique()
country_quarters = panel.groupby("iso2_code")["quarter_id"].nunique()
balanced_countries = country_quarters[country_quarters == n_quarters_total].index
panel["balanced"] = panel["iso2_code"].isin(balanced_countries)
log(f"[panel] Balanced countries (all {n_quarters_total} quarters): {len(balanced_countries)}")
log(f"[panel] Unbalanced countries: {panel['iso2_code'].nunique() - len(balanced_countries)}")


# ═══════════════════════════════════════════════════════════════════════════════
# 5. EVENT TIME CONSTRUCTION
# ═══════════════════════════════════════════════════════════════════════════════
log("\n" + "=" * 70)
log("EVENT TIME CONSTRUCTION")
log("=" * 70)

# Treatment: ChatGPT released Nov 30, 2022 = Q4 2022
# Q4 2022 is partial treatment (~1 month). Main spec: Q1 2023 = period +1
# Reference period (t=-1): Q3 2022 = quarter_id 20223

# Create a proper time index
quarter_map = {qid: i for i, qid in enumerate(quarters_sorted)}
panel["t_index"] = panel["quarter_id"].map(quarter_map)

# Event time relative to Q1 2023 (first full treatment quarter)
# Q1 2023 = event_time 0
event_quarter = 20231  # Q1 2023
if event_quarter in quarter_map:
    event_idx = quarter_map[event_quarter]
else:
    # Fallback: find closest
    event_idx = quarter_map.get(20224, quarter_map[min(quarters_sorted, key=lambda x: abs(x - 20231))])

panel["event_time"] = panel["t_index"] - event_idx
panel["post"] = (panel["event_time"] >= 0).astype(int)

# Also create event time relative to Q4 2022 (for robustness)
event_quarter_alt = 20224
if event_quarter_alt in quarter_map:
    event_idx_alt = quarter_map[event_quarter_alt]
    panel["event_time_alt"] = panel["t_index"] - event_idx_alt
else:
    panel["event_time_alt"] = panel["event_time"] + 1  # shift by 1

log(f"[event] Main event date: Q1 2023 (first full treatment quarter)")
log(f"[event] Reference period: t=-1 (Q3 2022)")
log(f"[event] Event time range: [{panel['event_time'].min()}, {panel['event_time'].max()}]")
log(f"[event] Pre-treatment periods: {(panel['event_time'] < 0).sum()} obs")
log(f"[event] Post-treatment periods: {(panel['event_time'] >= 0).sum()} obs")

# Drop Q4 2022 from main specification (partial treatment quarter)
panel["drop_q4_2022"] = (panel["quarter_id"] == 20224)
n_q4 = panel["drop_q4_2022"].sum()
log(f"[event] Q4 2022 (partial treatment) observations: {n_q4} — flagged for exclusion in main spec")


# ═══════════════════════════════════════════════════════════════════════════════
# 6. MERGE EF-EPI
# ═══════════════════════════════════════════════════════════════════════════════
log("\n" + "=" * 70)
log("MERGE EF-EPI")
log("=" * 70)

epi_merge = epi[["iso2_code", "epi_score", "proficiency_band"]].copy()
n_before_merge = len(panel)
panel = panel.merge(epi_merge, on="iso2_code", how="left")
n_after_merge = len(panel)

assert n_before_merge == n_after_merge, "Merge changed row count — check for duplicates in EPI data"

matched = panel["epi_score"].notna().sum()
unmatched = panel["epi_score"].isna().sum()
log(f"[merge] Matched: {matched:,} obs ({matched/len(panel)*100:.1f}%)")
log(f"[merge] Unmatched (no EPI score): {unmatched:,} obs")

# Countries without EPI (likely native English-speaking: US, GB, AU, etc.)
unmatched_countries = panel.loc[panel["epi_score"].isna(), "iso2_code"].unique()
log(f"[merge] Countries without EPI score: {list(unmatched_countries)}")

# Create English proficiency groups
median_epi = panel["epi_score"].median()
panel["epi_high"] = (panel["epi_score"] >= median_epi).astype(float)
panel.loc[panel["epi_score"].isna(), "epi_high"] = np.nan

# Terciles
terciles = panel["epi_score"].quantile([1/3, 2/3])
panel["epi_tercile"] = pd.cut(
    panel["epi_score"],
    bins=[-np.inf, terciles.iloc[0], terciles.iloc[1], np.inf],
    labels=["low", "medium", "high"],
)

log(f"[merge] EPI median: {median_epi:.0f}")
log(f"[merge] EPI tercile cutoffs: {terciles.iloc[0]:.0f}, {terciles.iloc[1]:.0f}")


# ═══════════════════════════════════════════════════════════════════════════════
# 7. WINSORIZE OUTCOMES (for robustness)
# ═══════════════════════════════════════════════════════════════════════════════
for var in ["hhi_raw", "hhi_norm", "entropy"]:
    p1 = panel[var].quantile(0.01)
    p99 = panel[var].quantile(0.99)
    panel[f"{var}_wins"] = panel[var].clip(p1, p99)

log(f"\n[wins] Winsorized outcomes created (1st/99th percentile)")


# ═══════════════════════════════════════════════════════════════════════════════
# 8. SUMMARY STATISTICS
# ═══════════════════════════════════════════════════════════════════════════════
log("\n" + "=" * 70)
log("SUMMARY STATISTICS")
log("=" * 70)

stat_vars = ["hhi_raw", "hhi_norm", "entropy", "n_languages", "total_pushers"]

def stats_block(data, label):
    rows = []
    for v in stat_vars:
        s = data[v].describe()
        rows.append({
            "variable": v,
            "period": label,
            "mean": s["mean"],
            "std": s["std"],
            "min": s["min"],
            "p10": data[v].quantile(0.10),
            "p50": s["50%"],
            "p90": data[v].quantile(0.90),
            "max": s["max"],
            "N": int(s["count"]),
        })
    return rows

rows = []
rows += stats_block(panel, "Full sample")
rows += stats_block(panel[panel["post"] == 0], "Pre-treatment")
rows += stats_block(panel[panel["post"] == 1], "Post-treatment")

# By EPI group
for grp_name, grp_data in panel.groupby("epi_high"):
    label = "High EPI" if grp_name == 1 else "Low EPI"
    rows += stats_block(grp_data, label)

summary = pd.DataFrame(rows)
summary.to_csv(CLEAN_DIR / "summary_stats.csv", index=False)

# Print summary
for period in ["Full sample", "Pre-treatment", "Post-treatment"]:
    log(f"\n  {period}:")
    sub = summary[summary["period"] == period]
    for _, r in sub.iterrows():
        log(f"    {r['variable']:18s}: mean={r['mean']:8.4f}  sd={r['std']:8.4f}  "
            f"p10={r['p10']:8.4f}  p50={r['p50']:8.4f}  p90={r['p90']:8.4f}  N={int(r['N'])}")


# ═══════════════════════════════════════════════════════════════════════════════
# 9. SAVE
# ═══════════════════════════════════════════════════════════════════════════════
panel.to_csv(CLEAN_DIR / "clean_data.csv", index=False)
log(f"\n[save] Panel saved: {CLEAN_DIR / 'clean_data.csv'}")
log(f"[save] Summary stats saved: {CLEAN_DIR / 'summary_stats.csv'}")
log(f"[save] Final panel: {len(panel):,} rows, {panel.shape[1]} columns")

# Data provenance log
log("\n" + "=" * 70)
log("DATA PROVENANCE")
log("=" * 70)
log(f"  num_pushers : languages.csv — count of active GitHub pushers per language×country×quarter")
log(f"  language    : languages.csv — programming language name")
log(f"  language_type: languages.csv — markup vs programming")
log(f"  iso2_code   : languages.csv — ISO 3166 alpha-2 country code")
log(f"  year/quarter: languages.csv — time period")
log(f"  epi_score   : ef_epi_2025.csv — EF English Proficiency Index 2025 edition")
log(f"  hhi_raw     : Computed — sum of squared language shares within country×quarter")
log(f"  hhi_norm    : Computed — normalized HHI = (raw - 1/N) / (1 - 1/N)")
log(f"  entropy     : Computed — Shannon entropy = -sum(share * ln(share))")

# Save report
REPORT_PATH.write_text("\n".join(report_lines), encoding="utf-8")
log(f"\n[save] Missingness report: {REPORT_PATH}")

print("\n[00_clean] DONE [OK]")
