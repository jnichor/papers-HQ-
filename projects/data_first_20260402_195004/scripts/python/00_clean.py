"""
00_clean.py
-----------
Load Public_Study_Data.tab, audit missingness, verify treatment,
create quintiles, produce summary stats and balance table.
"""

import warnings
warnings.filterwarnings("ignore")

from pathlib import Path
import numpy as np
import pandas as pd
from scipy import stats
import statsmodels.api as sm

np.random.seed(42)

# ── paths ──────────────────────────────────────────────────────────────
PROJECT = Path(__file__).resolve().parents[2]
RAW     = PROJECT / "data" / "external" / "Public_Study_Data.tab"
CLEAN   = PROJECT / "data" / "clean"
CLEAN.mkdir(parents=True, exist_ok=True)

# ── 1. Load ────────────────────────────────────────────────────────────
df_full = pd.read_csv(RAW, sep="\t")
print(f"Full dataset: {df_full.shape[0]} rows x {df_full.shape[1]} cols")

# Keep only rows in the apartheid-vs-persecution arm
df = df_full.dropna(subset=["apartheid_vs_persecution_treat"]).copy()
df["apartheid_vs_persecution_treat"] = df["apartheid_vs_persecution_treat"].astype(int)
print(f"Analysis sample (treatment non-missing): {df.shape[0]} rows")

# ── 2. Missingness audit ──────────────────────────────────────────────
miss_pct = df.isnull().mean().sort_values(ascending=False)
miss_report = miss_pct[miss_pct > 0]

with open(CLEAN / "missingness_report.txt", "w") as f:
    f.write("Missingness Report (analysis sample)\n")
    f.write("=" * 50 + "\n\n")
    f.write(f"Sample size: {len(df)}\n")
    f.write(f"Variables with any missing: {(miss_pct > 0).sum()}\n\n")
    f.write(f"{'Variable':<40s} {'Pct Missing':>12s}\n")
    f.write("-" * 55 + "\n")
    for var, pct in miss_report.items():
        f.write(f"{var:<40s} {pct:>11.2%}\n")

    # Simple MCAR proxy: Little-style test — compare missingness patterns
    # We test whether the treatment is associated with missingness on key vars
    f.write("\n\nMCAR Proxy: Treatment vs. missingness indicators\n")
    f.write("-" * 55 + "\n")
    key_vars = ["ICC_referral", "ICC_referral_binary", "pro_israel_score",
                "respondent_age", "female", "education"]
    for v in key_vars:
        if df[v].isnull().any():
            missing_ind = df[v].isnull().astype(int)
            ct = pd.crosstab(df["apartheid_vs_persecution_treat"], missing_ind)
            if ct.shape == (2, 2):
                chi2, p, _, _ = stats.chi2_contingency(ct)
                f.write(f"  {v:<35s}  chi2={chi2:.3f}  p={p:.4f}\n")
            else:
                f.write(f"  {v:<35s}  no variation in missingness\n")
        else:
            f.write(f"  {v:<35s}  no missing values\n")

print("Missingness report saved.")

# ── 3. Verify treatment ───────────────────────────────────────────────
treat = df["apartheid_vs_persecution_treat"]
assert treat.isnull().sum() == 0, "Treatment has missing values!"
assert set(treat.unique()) == {0, 1}, "Treatment is not binary!"
print(f"Treatment verified: {treat.sum()} treated, {(1-treat).sum()} control")

# ── 4. Create pro_israel quintile ─────────────────────────────────────
df["pro_israel_quintile"] = pd.qcut(
    df["pro_israel_score"], q=5, labels=False, duplicates="drop"
) + 1  # 1-5
print(f"Pro-Israel quintiles created: {df['pro_israel_quintile'].value_counts().sort_index().to_dict()}")

# ── 5. Summary stats ─────────────────────────────────────────────────
summary_vars = [
    "ICC_referral", "ICC_referral_binary", "pro_israel_score",
    "respondent_age", "female", "white", "black", "education",
    "stronger_republican_8pt", "hawkish_aggregate",
    "hostile_sexism_agg", "benevolent_sexism_agg",
    "cosmopolitan", "knowledge_ir_agg"
]
# keep only vars that exist
summary_vars = [v for v in summary_vars if v in df.columns]

rows = []
for v in summary_vars:
    row = {
        "variable": v,
        "n": df[v].notna().sum(),
        "mean": df[v].mean(),
        "sd": df[v].std(),
        "min": df[v].min(),
        "p25": df[v].quantile(0.25),
        "median": df[v].median(),
        "p75": df[v].quantile(0.75),
        "max": df[v].max(),
    }
    rows.append(row)
summary_df = pd.DataFrame(rows)
summary_df.to_csv(CLEAN / "summary_stats.csv", index=False)
print("Summary stats saved.")

# ── 6. Balance table ──────────────────────────────────────────────────
balance_vars = [
    "respondent_age", "female", "white", "black", "education",
    "stronger_republican_8pt", "hawkish_aggregate",
    "hostile_sexism_agg", "benevolent_sexism_agg",
    "cosmopolitan", "knowledge_ir_agg", "pro_israel_score",
    "hhi", "over_65"
]
balance_vars = [v for v in balance_vars if v in df.columns]

treated = df[df["apartheid_vs_persecution_treat"] == 1]
control = df[df["apartheid_vs_persecution_treat"] == 0]

bal_rows = []
for v in balance_vars:
    t_vals = treated[v].dropna()
    c_vals = control[v].dropna()
    mean_t = t_vals.mean()
    mean_c = c_vals.mean()
    diff = mean_t - mean_c
    pooled_sd = np.sqrt((t_vals.var() + c_vals.var()) / 2)
    smd = diff / pooled_sd if pooled_sd > 0 else np.nan
    tstat, pval = stats.ttest_ind(t_vals, c_vals, equal_var=False)
    bal_rows.append({
        "variable": v,
        "mean_treated": round(mean_t, 4),
        "mean_control": round(mean_c, 4),
        "difference": round(diff, 4),
        "t_stat": round(tstat, 4),
        "p_value": round(pval, 4),
        "smd": round(smd, 4),
    })

balance_df = pd.DataFrame(bal_rows)
balance_df.to_csv(CLEAN / "balance_table.csv", index=False)
print("Balance table saved.")

# ── 7. Joint F-test ───────────────────────────────────────────────────
bal_sub = df[["apartheid_vs_persecution_treat"] + balance_vars].dropna()
y_ftest = bal_sub["apartheid_vs_persecution_treat"]
X_ftest = sm.add_constant(bal_sub[balance_vars])
model_f = sm.OLS(y_ftest, X_ftest).fit(cov_type="HC2")
ftest = model_f.f_test(np.eye(len(balance_vars), len(balance_vars) + 1, 1))
print(f"Joint F-test of balance: F={float(ftest.fvalue):.3f}, p={float(ftest.pvalue):.4f}")

# Append to missingness report
with open(CLEAN / "missingness_report.txt", "a") as f:
    f.write(f"\n\nJoint F-test of balance (treatment ~ covariates)\n")
    f.write(f"  F-stat = {float(ftest.fvalue):.4f}\n")
    f.write(f"  p-value = {float(ftest.pvalue):.4f}\n")

# ── 8. Save clean data ───────────────────────────────────────────────
df.to_csv(CLEAN / "clean_data.csv", index=False)
print(f"Clean data saved: {len(df)} rows")
print("00_clean.py complete.")
