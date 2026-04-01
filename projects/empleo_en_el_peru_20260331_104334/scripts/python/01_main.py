"""01_main.py - TWFE DiD Event Study: COVID and Informality in Peru.

R1 fixes: (1) Cluster SEs at ISCO 2-digit level, (2) Winsorized weights,
(3) Continuous treatment as primary spec, binary as robustness.
"""

import os
import warnings
import numpy as np
import pandas as pd
import statsmodels.api as sm
from scipy import stats

warnings.filterwarnings("ignore")

PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
CLEAN_DIR = os.path.join(PROJECT_DIR, "data", "clean")
TABLES_DIR = os.path.join(PROJECT_DIR, "paper", "tables")
FIGURES_DIR = os.path.join(PROJECT_DIR, "paper", "figures")
os.makedirs(TABLES_DIR, exist_ok=True)
os.makedirs(FIGURES_DIR, exist_ok=True)

print("=" * 60)
print("01_main.py - DiD Event Study (R1: clustered SEs, continuous treatment)")
print("=" * 60)

# -- Load --
print("\n[1/7] Loading data...")
df = pd.read_csv(os.path.join(CLEAN_DIR, "clean_data.csv"), low_memory=False)
df = df[(df["employed"] == 1) & (df["working_age"] == True)].copy()
df = df.dropna(subset=["pid", "year", "informal", "telework_score", "weight", "isco_2d"])
df["year"] = df["year"].astype(int)
for c in ["informal", "telework_low", "telework_score", "female", "lima", "large_firm", "weight"]:
    if c in df.columns:
        df[c] = pd.to_numeric(df[c], errors="coerce")
df["isco_2d"] = df["isco_2d"].astype(str).str.strip()

n_obs = len(df)
n_pid = df["pid"].nunique()
n_clusters = df["isco_2d"].nunique()
print(f"  Sample: {n_obs:,} obs, {n_pid:,} individuals, {n_clusters} ISCO clusters")

years = sorted(df["year"].unique())
ref_year = 2020
post_years = [y for y in years if y != ref_year]

# Year dummies and interactions (continuous + binary)
for y in post_years:
    df[f"yr_{y}"] = (df["year"] == y).astype(int)
    df[f"yr_{y}_x_tw"] = df[f"yr_{y}"] * df["telework_score"]       # continuous
    df[f"yr_{y}_x_twlow"] = df[f"yr_{y}"] * df["telework_low"]       # binary
yr_cols = [f"yr_{y}" for y in post_years]
int_cont_cols = [f"yr_{y}_x_tw" for y in post_years]
int_bin_cols = [f"yr_{y}_x_twlow" for y in post_years]

# -- 2. PRIMARY: Continuous treatment DiD (WLS, clustered SEs) --
print("\n[2/7] Primary spec: continuous treatment (WLS, ISCO-clustered SEs)...")
X_cont = sm.add_constant(df[yr_cols + int_cont_cols + ["telework_score"]])
mod_cont = sm.WLS(df["informal"], X_cont, weights=df["weight"].clip(lower=0.01), missing="drop")
res_cont = mod_cont.fit(cov_type="cluster", cov_kwds={"groups": df["isco_2d"]})

print("\n  Continuous treatment interactions (ref=2020):")
cont_results = [{"year": ref_year, "yr_coef": 0, "yr_se": 0, "int_coef": 0, "int_se": 0, "int_pval": np.nan}]
for y in post_years:
    yr_c = res_cont.params.get(f"yr_{y}", 0)
    yr_s = res_cont.bse.get(f"yr_{y}", 0)
    int_c = res_cont.params.get(f"yr_{y}_x_tw", 0)
    int_s = res_cont.bse.get(f"yr_{y}_x_tw", 0)
    int_p = res_cont.pvalues.get(f"yr_{y}_x_tw", np.nan)
    stars = "***" if int_p < 0.01 else "**" if int_p < 0.05 else "*" if int_p < 0.1 else ""
    print(f"    {y}: yr={yr_c:.4f}, interaction={int_c:.4f}{stars} (SE={int_s:.4f})")
    cont_results.append({"year": y, "yr_coef": yr_c, "yr_se": yr_s,
                         "int_coef": int_c, "int_se": int_s, "int_pval": int_p})

cont_df = pd.DataFrame(cont_results)
cont_df["int_ci_lo"] = cont_df["int_coef"] - 1.96 * cont_df["int_se"]
cont_df["int_ci_hi"] = cont_df["int_coef"] + 1.96 * cont_df["int_se"]
cont_df.to_csv(os.path.join(CLEAN_DIR, "main_event_study.csv"), index=False)
print(f"  N={int(res_cont.nobs):,}, clusters={n_clusters}")

# -- 3. SECONDARY: Binary treatment DiD (WLS, clustered SEs) --
print("\n[3/7] Secondary spec: binary treatment (WLS, ISCO-clustered SEs)...")
X_bin = sm.add_constant(df[yr_cols + int_bin_cols + ["telework_low"]])
mod_bin = sm.WLS(df["informal"], X_bin, weights=df["weight"].clip(lower=0.01), missing="drop")
res_bin = mod_bin.fit(cov_type="cluster", cov_kwds={"groups": df["isco_2d"]})

bin_results = [{"year": ref_year, "int_coef": 0, "int_se": 0, "int_pval": np.nan}]
for y in post_years:
    c = res_bin.params.get(f"yr_{y}_x_twlow", 0)
    s = res_bin.bse.get(f"yr_{y}_x_twlow", 0)
    p = res_bin.pvalues.get(f"yr_{y}_x_twlow", np.nan)
    stars = "***" if p < 0.01 else "**" if p < 0.05 else "*" if p < 0.1 else ""
    print(f"    {y}: binary interaction={c:.4f}{stars} (SE={s:.4f})")
    bin_results.append({"year": y, "int_coef": c, "int_se": s, "int_pval": p})

bin_df = pd.DataFrame(bin_results)
bin_df.to_csv(os.path.join(CLEAN_DIR, "binary_event_study.csv"), index=False)

# -- 4. Within-estimator (FE) with continuous treatment --
print("\n[4/7] Within-estimator (individual FE, continuous treatment)...")
all_vars = ["informal"] + yr_cols + int_cont_cols + ["telework_score"]
df_dm = df[["pid", "isco_2d"] + all_vars].copy()
for v in all_vars:
    df_dm[v] = df_dm[v] - df_dm.groupby("pid")[v].transform("mean")

X_fe = sm.add_constant(df_dm[yr_cols + int_cont_cols])
mod_fe = sm.OLS(df_dm["informal"], X_fe, missing="drop")
res_fe = mod_fe.fit(cov_type="cluster", cov_kwds={"groups": df["isco_2d"]})

fe_results = [{"year": ref_year, "int_coef": 0, "int_se": 0, "int_pval": np.nan}]
for y in post_years:
    c = res_fe.params.get(f"yr_{y}_x_tw", 0)
    s = res_fe.bse.get(f"yr_{y}_x_tw", 0)
    p = res_fe.pvalues.get(f"yr_{y}_x_tw", np.nan)
    print(f"    {y}: FE continuous interaction={c:.4f} (SE={s:.4f}, p={p:.4f})")
    fe_results.append({"year": y, "int_coef": c, "int_se": s, "int_pval": p})

pd.DataFrame(fe_results).to_csv(os.path.join(CLEAN_DIR, "fe_event_study.csv"), index=False)

# -- 5. Heterogeneous effects (FE, binary treatment, clustered) --
print("\n[5/7] Heterogeneous effects...")
all_vars_bin = ["informal"] + yr_cols + int_bin_cols + ["telework_low"]

for group_var, group_label in [("female", "Gender"), ("lima", "Lima"), ("large_firm", "Firm size")]:
    if group_var not in df.columns:
        continue
    het_results = []
    for gval in [0, 1]:
        sub = df[df[group_var] == gval].copy()
        if len(sub) < 500:
            continue
        sub_dm = sub[["pid", "isco_2d"] + all_vars_bin].copy()
        for v in all_vars_bin:
            sub_dm[v] = sub_dm[v] - sub_dm.groupby("pid")[v].transform("mean")

        X_h = sm.add_constant(sub_dm[yr_cols + int_bin_cols])
        r_h = sm.OLS(sub_dm["informal"], X_h, missing="drop").fit(
            cov_type="cluster", cov_kwds={"groups": sub["isco_2d"]})

        het_results.append({"group": f"{group_label}={gval}", "year": ref_year,
                            "coef": 0, "se": 0, "pval": np.nan})
        for y in post_years:
            c = r_h.params.get(f"yr_{y}_x_twlow", 0)
            s = r_h.bse.get(f"yr_{y}_x_twlow", 0)
            p = r_h.pvalues.get(f"yr_{y}_x_twlow", np.nan)
            het_results.append({"group": f"{group_label}={gval}", "year": y,
                                "coef": c, "se": s, "pval": p})
        print(f"  {group_label}={gval}: N={int(r_h.nobs):,}")

    if het_results:
        pd.DataFrame(het_results).to_csv(os.path.join(CLEAN_DIR, f"het_{group_var}.csv"), index=False)

# -- 6. Age heterogeneity --
print("\n[6/7] Age group heterogeneity...")
df["age_group"] = pd.cut(df["p208a"], bins=[14, 29, 44, 65],
                          labels=["youth_15_29", "prime_30_44", "senior_45_65"])
age_results = []
for ag in ["youth_15_29", "prime_30_44", "senior_45_65"]:
    sub = df[df["age_group"] == ag].copy()
    if len(sub) < 500:
        continue
    sub_dm = sub[["pid", "isco_2d"] + all_vars_bin].copy()
    for v in all_vars_bin:
        sub_dm[v] = sub_dm[v] - sub_dm.groupby("pid")[v].transform("mean")
    X_a = sm.add_constant(sub_dm[yr_cols + int_bin_cols])
    r_a = sm.OLS(sub_dm["informal"], X_a, missing="drop").fit(
        cov_type="cluster", cov_kwds={"groups": sub["isco_2d"]})
    age_results.append({"group": ag, "year": ref_year, "coef": 0, "se": 0, "pval": np.nan})
    for y in post_years:
        c = r_a.params.get(f"yr_{y}_x_twlow", 0)
        s = r_a.bse.get(f"yr_{y}_x_twlow", 0)
        p = r_a.pvalues.get(f"yr_{y}_x_twlow", np.nan)
        age_results.append({"group": ag, "year": y, "coef": c, "se": s, "pval": p})
    print(f"  {ag}: N={int(r_a.nobs):,}")
if age_results:
    pd.DataFrame(age_results).to_csv(os.path.join(CLEAN_DIR, "het_age.csv"), index=False)

# -- 7. Scarring test (continuous treatment) --
print("\n[7/7] Scarring test...")
c_2021 = cont_df.loc[cont_df["year"] == 2021, "int_coef"].values
s_2021 = cont_df.loc[cont_df["year"] == 2021, "int_se"].values
c_2024 = cont_df.loc[cont_df["year"] == 2024, "int_coef"].values
s_2024 = cont_df.loc[cont_df["year"] == 2024, "int_se"].values

if len(c_2021) > 0 and len(c_2024) > 0 and s_2021[0] > 0 and s_2024[0] > 0:
    diff = c_2024[0] - c_2021[0]
    se_diff = np.sqrt(s_2024[0]**2 + s_2021[0]**2)
    z = diff / se_diff if se_diff > 0 else 0
    p = 2 * (1 - stats.norm.cdf(abs(z)))
    print(f"  gamma_2021 = {c_2021[0]:.4f}, gamma_2024 = {c_2024[0]:.4f}")
    print(f"  Diff = {diff:.4f}, z = {z:.3f}, p = {p:.4f}")
    conclusion = "scarring_persists" if p > 0.05 else "effects_evolving"
    print(f"  Conclusion: {conclusion}")
    pd.DataFrame([{"coef_2021": c_2021[0], "coef_2024": c_2024[0],
                    "diff": diff, "z_stat": z, "p_val": p,
                    "conclusion": conclusion}]).to_csv(
        os.path.join(CLEAN_DIR, "scarring_test.csv"), index=False)

# Save qr_results
cont_df["specification"] = "continuous_did_clustered"
cont_df.to_csv(os.path.join(CLEAN_DIR, "qr_results.csv"), index=False)

print("\n" + "=" * 60)
print("[ok] 01_main.py DONE")
print("=" * 60)
