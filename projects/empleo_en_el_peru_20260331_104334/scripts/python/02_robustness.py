"""02_robustness.py - Robustness checks for DiD informality study."""

import os
import warnings
import numpy as np
import pandas as pd
import statsmodels.api as sm

warnings.filterwarnings("ignore")

PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
CLEAN_DIR = os.path.join(PROJECT_DIR, "data", "clean")

print("=" * 60)
print("02_robustness.py - Robustness Checks")
print("=" * 60)

# -- Load --
print("\n[1/5] Loading data...")
df = pd.read_csv(os.path.join(CLEAN_DIR, "clean_data.csv"), low_memory=False)
df = df[(df["employed"] == 1) & (df["working_age"] == True)].copy()
df = df.dropna(subset=["pid", "year", "informal", "telework_score"])
df["year"] = df["year"].astype(int)
for c in ["informal", "informal_noseg", "informal_nocontract", "informal_smallfirm",
          "telework_low", "weight", "female", "rural"]:
    if c in df.columns:
        df[c] = pd.to_numeric(df[c], errors="coerce")

years = sorted(df["year"].unique())
ref_year = 2020
post_years = [y for y in years if y != ref_year]
for y in post_years:
    df[f"yr_{y}"] = (df["year"] == y).astype(int)
    df[f"yr_{y}_x_twlow"] = df[f"yr_{y}"] * df["telework_low"]
yr_cols = [f"yr_{y}" for y in post_years]
int_cols = [f"yr_{y}_x_twlow" for y in post_years]
print(f"  Sample: {len(df):,} obs")

# -- 2. Alternative informality definitions --
print("\n[2/5] Alternative informality definitions...")
alt_results = []
for defn, label in [("informal_noseg", "no_social_security"),
                     ("informal_nocontract", "no_contract"),
                     ("informal_smallfirm", "small_firm")]:
    if defn not in df.columns:
        continue
    sub = df.dropna(subset=[defn]).copy()
    sub[defn] = sub[defn].astype(float)
    X = sm.add_constant(sub[yr_cols + int_cols + ["telework_low"]])
    mod = sm.WLS(sub[defn], X, weights=sub["weight"].clip(lower=0.01), missing="drop")
    r = mod.fit(cov_type="HC1")
    for y in post_years:
        int_c = r.params.get(f"yr_{y}_x_twlow", 0)
        int_s = r.bse.get(f"yr_{y}_x_twlow", 0)
        int_p = r.pvalues.get(f"yr_{y}_x_twlow", np.nan)
        alt_results.append({"definition": label, "year": y,
                            "int_coef": int_c, "int_se": int_s, "int_pval": int_p})
    print(f"  {label}: N={int(r.nobs):,}, interaction_2021={r.params.get('yr_2021_x_twlow', 0):.4f}")

if alt_results:
    pd.DataFrame(alt_results).to_csv(os.path.join(CLEAN_DIR, "alt_definitions.csv"), index=False)

# -- 3. Balanced vs unbalanced panel --
print("\n[3/5] Balanced vs unbalanced panel...")
pid_yr = df.groupby("pid")["year"].nunique()
balanced_pids = pid_yr[pid_yr == len(years)].index
df_bal = df[df["pid"].isin(balanced_pids)].copy()
print(f"  Full: {df['pid'].nunique():,} individuals")
print(f"  Balanced: {len(balanced_pids):,} individuals ({100*len(balanced_pids)/df['pid'].nunique():.1f}%)")

bal_results = []
for label, sub in [("full", df), ("balanced", df_bal)]:
    if len(sub) < 500:
        continue
    X = sm.add_constant(sub[yr_cols + int_cols + ["telework_low"]])
    mod = sm.WLS(sub["informal"], X, weights=sub["weight"].clip(lower=0.01), missing="drop")
    r = mod.fit(cov_type="HC1")
    for y in [ref_year] + post_years:
        if y == ref_year:
            bal_results.append({"spec": label, "year": y, "int_coef": 0, "int_se": 0})
        else:
            bal_results.append({"spec": label, "year": y,
                                "int_coef": r.params.get(f"yr_{y}_x_twlow", 0),
                                "int_se": r.bse.get(f"yr_{y}_x_twlow", 0)})
    print(f"  {label}: N={int(r.nobs):,}")

pd.DataFrame(bal_results).to_csv(os.path.join(CLEAN_DIR, "balanced_comparison.csv"), index=False)

# -- 4. Attrition analysis --
print("\n[4/5] Attrition analysis...")
baseline = df[df["year"] == 2020][["pid", "telework_low", "female", "rural", "p208a"]].drop_duplicates("pid")
att_results = []
for y in post_years:
    pids_in_year = set(df[df["year"] == y]["pid"].unique())
    bl = baseline.copy()
    bl["observed"] = bl["pid"].isin(pids_in_year).astype(int)
    bl["attrited"] = 1 - bl["observed"]

    overall = bl["attrited"].mean() * 100
    tw_low = bl[bl["telework_low"] == 1]["attrited"].mean() * 100
    tw_high = bl[bl["telework_low"] == 0]["attrited"].mean() * 100
    att_results.append({"year": y, "overall_pct": overall,
                        "contact_intensive_pct": tw_low, "teleworkable_pct": tw_high})
    print(f"  {y}: overall={overall:.1f}%, contact-intensive={tw_low:.1f}%, teleworkable={tw_high:.1f}%")

# Differential attrition test
bl_2024 = baseline.copy()
pids_2024 = set(df[df["year"] == 2024]["pid"].unique())
bl_2024["attrited"] = (~bl_2024["pid"].isin(pids_2024)).astype(int)
covars = [c for c in ["telework_low", "female", "rural", "p208a"] if c in bl_2024.columns]
bl_2024 = bl_2024.dropna(subset=covars)
if len(covars) > 0 and len(bl_2024) > 100:
    X_att = sm.add_constant(bl_2024[covars].astype(float))
    r_att = sm.OLS(bl_2024["attrited"], X_att).fit(cov_type="HC1")
    print(f"\n  Attrition predictors (2024):")
    for c in covars:
        print(f"    {c}: coef={r_att.params[c]:.4f}, p={r_att.pvalues[c]:.4f}")

pd.DataFrame(att_results).to_csv(os.path.join(CLEAN_DIR, "attrition_analysis.csv"), index=False)

# -- 5. BH correction --
print("\n[5/5] Benjamini-Hochberg correction...")
all_pvals = []
for fname in ["het_female.csv", "het_lima.csv", "het_firmsize.csv", "het_age.csv"]:
    fpath = os.path.join(CLEAN_DIR, fname)
    if os.path.exists(fpath):
        het = pd.read_csv(fpath)
        for _, row in het.dropna(subset=["pval"]).iterrows():
            all_pvals.append({"source": fname, "group": row.get("group", ""),
                              "year": int(row["year"]), "pval": row["pval"]})

if all_pvals:
    pv = pd.DataFrame(all_pvals).sort_values("pval").reset_index(drop=True)
    m = len(pv)
    pv["rank"] = range(1, m + 1)
    pv["bh_threshold"] = pv["rank"] / m * 0.05
    pv["bh_significant"] = pv["pval"] <= pv["bh_threshold"]
    pv.to_csv(os.path.join(CLEAN_DIR, "bh_correction.csv"), index=False)
    print(f"  Tests: {m}, raw sig: {(pv['pval']<0.05).sum()}, BH sig: {pv['bh_significant'].sum()}")

# Save summary
pd.DataFrame(att_results).to_csv(os.path.join(CLEAN_DIR, "robustness_summary.csv"), index=False)

print("\n" + "=" * 60)
print("[ok] 02_robustness.py DONE")
print("=" * 60)
