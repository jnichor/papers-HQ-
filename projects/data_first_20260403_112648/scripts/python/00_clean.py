"""
00_clean.py - Data cleaning and validation for factorial RCT
============================================================
Loads JN_FinalSubmission.tab, filters to experimental sample,
validates outcome variables, produces balance/summary tables.
"""

import sys
import warnings
import numpy as np
import pandas as pd
from pathlib import Path

warnings.filterwarnings("ignore")

# ── paths ───────────────────────────────────────────────────────────────────
PROJECT = Path(__file__).resolve().parents[2]
RAW = PROJECT / "data" / "external" / "JN_FinalSubmission.tab"
CLEAN = PROJECT / "data" / "clean"
CLEAN.mkdir(parents=True, exist_ok=True)

print("=" * 70)
print("00_clean.py  --  Data Cleaning & Validation")
print("=" * 70)

# ── 1. Load data ────────────────────────────────────────────────────────────
print("\n[1] Loading data...")
df_raw = pd.read_csv(RAW, sep="\t", low_memory=False)
print(f"  Raw dataset: {df_raw.shape[0]} rows x {df_raw.shape[1]} cols")

# Filter to experimental sample
df = df_raw[df_raw["treatstat"].notna()].copy()
print(f"  Experimental sample (treatstat not NaN): {df.shape[0]} rows")

# Create treatment arm label
df["arm"] = "Control"
df.loc[(df["voucher"] == 1) & (df["training"] == 0), "arm"] = "Voucher"
df.loc[(df["voucher"] == 0) & (df["training"] == 1), "arm"] = "Training"
df.loc[(df["voucher"] == 1) & (df["training"] == 1), "arm"] = "Both"

print(f"\n  Treatment arms:")
for arm in ["Control", "Voucher", "Training", "Both"]:
    n = (df["arm"] == arm).sum()
    print(f"    {arm}: n={n}")

# ── 2. Outcome validation: correlations with voucher ────────────────────────
print("\n[2] Outcome validation: top 20 correlations with voucher")
numeric_cols = df.select_dtypes(include=[np.number]).columns.tolist()
# Exclude treatment variables themselves
exclude = {"voucher", "training", "both", "treatstat", "seatno"}
numeric_cols = [c for c in numeric_cols if c not in exclude]

corrs = {}
for c in numeric_cols:
    valid = df[["voucher", c]].dropna()
    if len(valid) > 30:
        corrs[c] = valid["voucher"].corr(valid[c])

corr_series = pd.Series(corrs).sort_values(key=lambda x: x.abs(), ascending=False)
print("  Top 20 absolute correlations with voucher:")
for i, (col, r) in enumerate(corr_series.head(20).items()):
    marker = " <-- KEY OUTCOME" if col in ["mid_x", "end_x", "mid_salary", "end_salary", "mid_lfp", "end_lfp"] else ""
    print(f"    {i+1:2d}. {col:40s} r = {r:+.4f}{marker}")

# Check that key outcomes are among top correlates
key_outcomes = ["mid_x", "mid_salary", "end_x", "end_salary"]
top50 = set(corr_series.head(50).index)
found = [k for k in key_outcomes if k in top50]
missing = [k for k in key_outcomes if k not in top50]
print(f"\n  Key outcomes in top-50 correlates: {found}")
if missing:
    print(f"  WARNING: Not in top-50: {missing}")
else:
    print("  VALIDATED: All key outcomes have meaningful treatment correlation.")

# ── 3. Missingness audit ────────────────────────────────────────────────────
print("\n[3] Missingness audit")
outcomes = ["mid_x", "mid_salary", "mid_lfp", "mid_ever",
            "end_x", "end_lfp", "end_salary", "end_reg_ssc",
            "end2_x", "end2_lfp", "end2_salary", "end2_reg_ssc"]

miss_report = []
for var in outcomes:
    if var in df.columns:
        n_total = len(df)
        n_miss = df[var].isna().sum()
        pct = 100 * n_miss / n_total
        miss_report.append({"variable": var, "n_total": n_total, "n_missing": n_miss, "pct_missing": round(pct, 1)})
        print(f"  {var:20s}: {n_miss:4d} / {n_total} missing ({pct:.1f}%)")
    else:
        print(f"  {var:20s}: COLUMN NOT FOUND")
        miss_report.append({"variable": var, "n_total": len(df), "n_missing": len(df), "pct_missing": 100.0})

miss_df = pd.DataFrame(miss_report)

# ── 4. Balance table ────────────────────────────────────────────────────────
print("\n[4] Balance table across 4 arms")
baseline_vars = ["b_b1age", "b_communitycollege", "b_examresult",
                 "b_b3socialstatus", "b_b6desiretowork", "b_b7abilitytowork",
                 "b_d7prviouswork"]
# Keep only those that exist
baseline_vars = [v for v in baseline_vars if v in df.columns]

balance_rows = []
for var in baseline_vars:
    row = {"variable": var}
    for arm in ["Control", "Voucher", "Training", "Both"]:
        subset = df.loc[df["arm"] == arm, var].dropna()
        row[f"{arm}_mean"] = round(subset.mean(), 3) if len(subset) > 0 else np.nan
        row[f"{arm}_sd"] = round(subset.std(), 3) if len(subset) > 0 else np.nan
        row[f"{arm}_n"] = len(subset)
    balance_rows.append(row)

balance_df = pd.DataFrame(balance_rows)
print(balance_df.to_string(index=False))

# ── 5. Attrition check ─────────────────────────────────────────────────────
print("\n[5] Attrition by arm")
for att_var in ["mid_attrition", "end_attrition", "end2_attrition"]:
    if att_var in df.columns:
        print(f"\n  {att_var}:")
        for arm in ["Control", "Voucher", "Training", "Both"]:
            subset = df.loc[df["arm"] == arm, att_var].dropna()
            if len(subset) > 0:
                rate = subset.mean()
                print(f"    {arm:10s}: {rate:.3f} (n={len(subset)})")
    else:
        print(f"  {att_var}: not found")

# ── 6. Summary stats: means by arm ─────────────────────────────────────────
print("\n[6] Outcome means by treatment arm")
sum_outcomes = ["mid_x", "mid_salary", "mid_lfp", "mid_ever",
                "end_x", "end_lfp", "end_salary", "end_reg_ssc"]

arm_means_rows = []
for var in sum_outcomes:
    if var not in df.columns:
        continue
    row = {"outcome": var}
    for arm in ["Control", "Voucher", "Training", "Both"]:
        subset = df.loc[df["arm"] == arm, var].dropna()
        row[f"{arm}_mean"] = round(subset.mean(), 3) if len(subset) > 0 else np.nan
        row[f"{arm}_n"] = len(subset)
    arm_means_rows.append(row)
    print(f"  {var:15s}  C={row.get('Control_mean','?'):8}  V={row.get('Voucher_mean','?'):8}  "
          f"T={row.get('Training_mean','?'):8}  B={row.get('Both_mean','?'):8}")

arm_means_df = pd.DataFrame(arm_means_rows)

# Summary stats
summary_rows = []
for var in sum_outcomes:
    if var not in df.columns:
        continue
    s = df[var].dropna()
    summary_rows.append({
        "variable": var,
        "n": len(s),
        "mean": round(s.mean(), 3),
        "sd": round(s.std(), 3),
        "min": round(s.min(), 3),
        "max": round(s.max(), 3),
    })
summary_df = pd.DataFrame(summary_rows)

# ── 7. Save outputs ────────────────────────────────────────────────────────
print("\n[7] Saving outputs...")
df.to_csv(CLEAN / "clean_data.csv", index=False)
print(f"  Saved: clean_data.csv ({df.shape[0]} rows)")

balance_df.to_csv(CLEAN / "balance_table.csv", index=False)
print(f"  Saved: balance_table.csv")

summary_df.to_csv(CLEAN / "summary_stats.csv", index=False)
print(f"  Saved: summary_stats.csv")

arm_means_df.to_csv(CLEAN / "arm_means.csv", index=False)
print(f"  Saved: arm_means.csv")

with open(CLEAN / "missingness_report.txt", "w") as f:
    f.write("Missingness Report\n")
    f.write("=" * 50 + "\n")
    for _, row in miss_df.iterrows():
        f.write(f"{row['variable']:20s}: {row['n_missing']:4.0f} / {row['n_total']} ({row['pct_missing']:.1f}%)\n")
print(f"  Saved: missingness_report.txt")

print("\n" + "=" * 70)
print("00_clean.py COMPLETE")
print("=" * 70)
