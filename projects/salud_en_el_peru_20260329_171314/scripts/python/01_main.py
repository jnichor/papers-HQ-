# =============================================================================
# 01_main.py  --  Main Estimation: OLS + CQR + Two-Part Model + RIF-QR
# Referee Checklist Compliant: survey weights, two-part model, RIF-OLS,
# Wald tests, 200 bootstrap reps, cell-level reporting
# =============================================================================
import warnings
warnings.filterwarnings("ignore", category=FutureWarning)
warnings.filterwarnings("ignore", category=RuntimeWarning)

import numpy as np
import pandas as pd
from pathlib import Path
import statsmodels.api as sm
from statsmodels.regression.quantile_regression import QuantReg
from statsmodels.regression.linear_model import WLS
from statsmodels.discrete.discrete_model import Probit
from scipy.stats import norm, gaussian_kde
from joblib import Parallel, delayed

np.random.seed(42)

PROJECT = Path(__file__).resolve().parent.parent.parent
CLEAN_DIR = PROJECT / "data" / "clean"
TABLE_DIR = PROJECT / "paper" / "tables"
TABLE_DIR.mkdir(parents=True, exist_ok=True)

N_BOOT = 200
TAUS = [0.10, 0.25, 0.50, 0.75, 0.90]

SEP = "=" * 68
print(SEP)
print("01_main.py -- Main Estimation (Referee Checklist Compliant)")
print(SEP)

# -- Load data -----------------------------------------------------------------
df = pd.read_csv(CLEAN_DIR / "clean_data.csv")
print(f"Loaded {len(df):,} households")
print(f"Zero OOP: {df['zero_oop'].mean()*100:.1f}%")

# -- Setup variables -----------------------------------------------------------
OUTCOME = "oop_share"
TREATMENTS = ["ins_sis", "ins_essalud"]
CONTROLS = ["age_head", "age_head_sq", "female_head", "educ_years",
            "hh_size", "children_u5", "elderly_65", "rural",
            "hospitalized", "chronic_any"]

for q in [2, 3, 4, 5]:
    df[f"q{q}"] = (df["quintile"] == q).astype(int)
QUINTILE_D = ["q2", "q3", "q4", "q5"]

INTERACTIONS = []
for treat in TREATMENTS:
    for q in [2, 3, 4, 5]:
        col = f"{treat}_x_q{q}"
        df[col] = df[treat] * df[f"q{q}"]
        INTERACTIONS.append(col)

dept_dummies = pd.get_dummies(df["department"], prefix="dept", drop_first=True, dtype=int)
df = pd.concat([df, dept_dummies], axis=1)
REGION_FE = list(dept_dummies.columns)

ALL_X = TREATMENTS + QUINTILE_D + INTERACTIONS + CONTROLS + REGION_FE
df = df.dropna(subset=[OUTCOME] + ALL_X + ["FACTOR07"]).reset_index(drop=True)
print(f"Analysis sample: {len(df):,}")

df["w"] = df["FACTOR07"] / df["FACTOR07"].mean()

def stars_fn(p):
    if p is None or not np.isfinite(p): return ""
    if p < 0.01: return "***"
    if p < 0.05: return "**"
    if p < 0.10: return "*"
    return ""

key_show = TREATMENTS + QUINTILE_D + INTERACTIONS[:4]

# ==============================================================================
# PART 1: OLS BENCHMARK (weighted, cluster-robust)
# ==============================================================================
print(f"\n{'='*40}\n[1] OLS Benchmark (weighted)\n{'='*40}")

y = df[OUTCOME].astype(float).values
X = sm.add_constant(df[ALL_X].astype(float), has_constant="add")

ols_mod = WLS(y, X, weights=df["w"].values).fit(
    cov_type="cluster", cov_kwds={"groups": df["CONGLOME"].values}
)
print(f"  N={int(ols_mod.nobs):,}, R2={ols_mod.rsquared:.4f}")
for v in key_show:
    if v in ols_mod.params.index:
        c, s, p = ols_mod.params[v], ols_mod.bse[v], ols_mod.pvalues[v]
        print(f"    {v:25s}: {c:+.4f} ({s:.4f}) {stars_fn(p)}")

ols_df = pd.DataFrame({"variable": ols_mod.params.index, "coef": ols_mod.params.values,
                        "se": ols_mod.bse.values, "pvalue": ols_mod.pvalues.values})
ols_df.to_csv(CLEAN_DIR / "ols_results.csv", index=False)

# ==============================================================================
# PART 2: CONDITIONAL QUANTILE REGRESSION (cluster bootstrap)
# ==============================================================================
print(f"\n{'='*40}\n[2] Conditional Quantile Regression\n{'='*40}")

clusters = df["CONGLOME"].values
unique_clusters = np.unique(clusters)
y_arr = df[OUTCOME].astype(float).values
X_arr = sm.add_constant(df[ALL_X].astype(float), has_constant="add").values
col_names = ["const"] + ALL_X

# Precompute cluster -> index mapping once to avoid O(n) scans per bootstrap rep
cluster_to_idx = {c: np.where(clusters == c)[0] for c in unique_clusters}

def _one_boot_all_taus(seed, y, X, cluster_to_idx, unique_clusters, taus):
    """Single bootstrap rep fitting QR for all taus -- reduces parallel overhead."""
    rng = np.random.default_rng(seed)
    boot_cl = rng.choice(unique_clusters, size=len(unique_clusters), replace=True)
    boot_idx = np.concatenate([cluster_to_idx[c] for c in boot_cl])
    y_b, X_b = y[boot_idx], X[boot_idx]
    results = {}
    for tau in taus:
        try:
            results[tau] = QuantReg(y_b, X_b).fit(q=tau, max_iter=5000).params
        except Exception:
            results[tau] = np.full(X.shape[1], np.nan)
    return results

print(f"  Bootstrap ({N_BOOT} reps across {len(TAUS)} quantiles, parallel)...")
rng_master = np.random.default_rng(12345)
seeds = rng_master.integers(0, 2**31, size=N_BOOT)

# Use default loky backend (process-based) -- avoids GIL for CPU-bound QR fits
boot_all = Parallel(n_jobs=-1)(
    delayed(_one_boot_all_taus)(
        int(s), y_arr, X_arr, cluster_to_idx, unique_clusters, TAUS
    )
    for s in seeds
)

# Organize results: boot_coefs[tau] = array of shape (n_boot, n_params)
boot_coefs_by_tau = {tau: np.array([rep[tau] for rep in boot_all]) for tau in TAUS}

qr_results = {}
all_rows = []

for tau in TAUS:
    print(f"\n  tau = {tau}:")
    mod = QuantReg(y_arr, X_arr).fit(q=tau, max_iter=5000)
    coefs = pd.Series(mod.params, index=col_names)

    boot_coefs = boot_coefs_by_tau[tau]
    valid = np.isfinite(boot_coefs).all(axis=1)
    n_valid = int(valid.sum())
    print(f"    Bootstrap: {n_valid}/{N_BOOT} valid ({N_BOOT - n_valid} discarded)")

    if n_valid >= 20:
        valid_coefs = boot_coefs[valid]
        ses_arr = np.std(valid_coefs, axis=0, ddof=1)
        ses_arr[ses_arr > 0.5] = np.nan
    else:
        ses_arr = np.full(X_arr.shape[1], np.nan)

    ses = pd.Series(ses_arr, index=col_names)
    pvals = pd.Series(2 * (1 - norm.cdf(np.abs(coefs / ses))), index=col_names)

    try:
        pr2 = mod.prsquared
    except Exception:
        pr2 = np.nan

    qr_results[tau] = {"coefs": coefs, "ses": ses, "pvals": pvals, "pr2": pr2, "model": mod}

    for v in key_show:
        c, s, p = coefs.get(v, np.nan), ses.get(v, np.nan), pvals.get(v, np.nan)
        print(f"    {v:25s}: {c:+.4f} ({s:.4f}) {stars_fn(p) if np.isfinite(p) else ''}")

    for v in col_names:
        all_rows.append({"tau": tau, "variable": v, "coef": coefs.get(v, np.nan),
                         "se": ses.get(v, np.nan), "pvalue": pvals.get(v, np.nan), "pseudo_r2": pr2})

pd.DataFrame(all_rows).to_csv(CLEAN_DIR / "qr_results.csv", index=False)

# ==============================================================================
# PART 3: WALD TESTS (inter-quantile equality)
# ==============================================================================
print(f"\n{'='*40}\n[3] Wald Tests\n{'='*40}")

wald_results = []
for v in ["ins_sis", "ins_essalud"]:
    for tau_lo, tau_hi in [(0.25, 0.75), (0.50, 0.90)]:
        if tau_lo in qr_results and tau_hi in qr_results:
            diff = qr_results[tau_hi]["coefs"].get(v, 0) - qr_results[tau_lo]["coefs"].get(v, 0)
            se_lo = qr_results[tau_lo]["ses"].get(v, np.nan)
            se_hi = qr_results[tau_hi]["ses"].get(v, np.nan)
            se_diff = np.sqrt(se_lo**2 + se_hi**2) if np.isfinite(se_lo) and np.isfinite(se_hi) else np.nan
            z = diff / se_diff if (np.isfinite(se_diff) and se_diff > 0) else np.nan
            p = 2 * (1 - norm.cdf(abs(z))) if np.isfinite(z) else np.nan
            print(f"  {v} [{tau_lo} vs {tau_hi}]: diff={diff:+.4f}, z={z:.2f}, p={p:.3f} {stars_fn(p)}")
            wald_results.append({"variable": v, "tau_lo": tau_lo, "tau_hi": tau_hi,
                                 "diff": diff, "se_diff": se_diff, "z": z, "pvalue": p})

pd.DataFrame(wald_results).to_csv(CLEAN_DIR / "wald_tests.csv", index=False)

# ==============================================================================
# PART 4: TOTAL EFFECT MATRIX
# ==============================================================================
print(f"\n{'='*40}\n[4] Total Effect Matrix\n{'='*40}")

total_effects = []
for tau in TAUS:
    r = qr_results[tau]
    for q in [1, 2, 3, 4, 5]:
        for treat, label in [("ins_sis", "SIS"), ("ins_essalud", "EsSalud")]:
            base = r["coefs"].get(treat, 0)
            inter = r["coefs"].get(f"{treat}_x_q{q}", 0) if q > 1 else 0
            total = base + inter
            base_se = r["ses"].get(treat, np.nan)
            inter_se = r["ses"].get(f"{treat}_x_q{q}", np.nan) if q > 1 else 0
            total_se = np.sqrt(base_se**2 + inter_se**2) if np.isfinite(base_se) else np.nan
            total_p = 2 * (1 - norm.cdf(abs(total / total_se))) if (np.isfinite(total_se) and total_se > 0) else np.nan
            total_effects.append({"tau": tau, "quintile": q, "insurance": label,
                                  "total_effect": total, "se": total_se, "pvalue": total_p})

te_df = pd.DataFrame(total_effects)
te_df.to_csv(CLEAN_DIR / "total_effects.csv", index=False)

for _, r in te_df[te_df["insurance"] == "SIS"].iterrows():
    print(f"  SIS Q{int(r['quintile'])} tau={r['tau']}: {r['total_effect']:+.4f}{stars_fn(r['pvalue'])}")

# ==============================================================================
# PART 5: TWO-PART MODEL
# ==============================================================================
print(f"\n{'='*40}\n[5] Two-Part Model\n{'='*40}")

# Part 1: Probit
print("  Part 1: Probit for Pr(OOP > 0)...")
y_binary = (df["health_expend"] > 0).astype(int).values
X_probit = sm.add_constant(df[TREATMENTS + QUINTILE_D + CONTROLS + REGION_FE].astype(float))

try:
    probit_mod = Probit(y_binary, X_probit).fit(disp=0, cov_type="cluster",
                                                 cov_kwds={"groups": df["CONGLOME"].values})
    probit_mfx = probit_mod.get_margeff()
    print(f"  N={int(probit_mod.nobs):,}, Pseudo-R2={probit_mod.prsquared:.4f}")
    for v in TREATMENTS:
        if v in probit_mfx.summary_frame().index:
            row = probit_mfx.summary_frame().loc[v]
            print(f"    {v:25s}: ME={row['dy/dx']:+.4f} ({row['Std. Err.']:.4f}) {stars_fn(row['Pr(>|z|)'])}")
    probit_mfx.summary_frame().to_csv(CLEAN_DIR / "probit_marginal_effects.csv")
except Exception as e:
    print(f"  Probit failed: {e}")

# Part 2: QR on positive spenders
print("\n  Part 2: QR on positive OOP subsample...")
df_pos = df[df["health_expend"] > 0].copy().reset_index(drop=True)
print(f"  Positive OOP: {len(df_pos):,} ({100*len(df_pos)/len(df):.1f}%)")

y_pos = df_pos[OUTCOME].astype(float).values
X_pos = sm.add_constant(df_pos[ALL_X].astype(float), has_constant="add").values

twopart_rows = []
for tau in [0.25, 0.50, 0.75, 0.90]:
    try:
        mod_pos = QuantReg(y_pos, X_pos).fit(q=tau, max_iter=5000)
        coefs_pos = pd.Series(mod_pos.params, index=col_names)
        for v in TREATMENTS:
            idx = col_names.index(v)
            c, s, p = coefs_pos[v], mod_pos.bse[idx], mod_pos.pvalues[idx]
            print(f"    tau={tau} {v:15s}: {c:+.4f} ({s:.4f}) {stars_fn(p)}")
            twopart_rows.append({"tau": tau, "variable": v, "coef": c, "se": s, "pvalue": p})
    except Exception as e:
        print(f"    tau={tau}: FAILED ({e})")

pd.DataFrame(twopart_rows).to_csv(CLEAN_DIR / "twopart_qr_results.csv", index=False)

# ==============================================================================
# PART 6: RIF UNCONDITIONAL QR
# ==============================================================================
print(f"\n{'='*40}\n[6] RIF-OLS (Unconditional QR)\n{'='*40}")

rif_rows = []
RIF_VARS = TREATMENTS + QUINTILE_D + CONTROLS + REGION_FE

for tau in [0.25, 0.50, 0.75, 0.90]:
    print(f"  tau = {tau}:")
    y_rif = df[OUTCOME].astype(float).values
    q_tau = np.quantile(y_rif, tau)

    try:
        kde = gaussian_kde(y_rif, bw_method="silverman")  # full sample, not positive-only
        f_q = max(float(kde(q_tau)[0]), 1e-10)
    except Exception:
        f_q = 1.0

    rif_values = q_tau + (tau - (y_rif <= q_tau).astype(float)) / f_q

    X_rif = sm.add_constant(df[RIF_VARS].astype(float))
    try:
        rif_mod = WLS(rif_values, X_rif, weights=df["w"].values).fit(
            cov_type="cluster", cov_kwds={"groups": df["CONGLOME"].values}
        )
        for v in TREATMENTS + QUINTILE_D[:2]:
            if v in rif_mod.params.index:
                c, s, p = rif_mod.params[v], rif_mod.bse[v], rif_mod.pvalues[v]
                print(f"    {v:25s}: {c:+.4f} ({s:.4f}) {stars_fn(p)}")
                rif_rows.append({"tau": tau, "variable": v, "coef": c, "se": s, "pvalue": p})
    except Exception as e:
        print(f"    FAILED: {e}")

pd.DataFrame(rif_rows).to_csv(CLEAN_DIR / "rif_results.csv", index=False)

# ==============================================================================
# LATEX TABLES
# ==============================================================================
print(f"\n{'='*40}\n[7] LaTeX Tables\n{'='*40}")

# Table 2: Main QR + OLS
key_vars = TREATMENTS + QUINTILE_D + INTERACTIONS
tex = ["\\begin{table}[htbp]", "\\centering",
       "\\caption{Quantile Regression: Insurance Associations with OOP Share}",
       "\\label{tab:main_qr}", "\\scriptsize",
       "\\begin{tabular}{l" + "c" * (1 + len(TAUS)) + "}", "\\toprule",
       "& OLS & " + " & ".join(f"$\\tau={t}$" for t in TAUS) + " \\\\", "\\midrule"]

for var in key_vars:
    label = var.replace("ins_sis_x_q", "SIS $\\times$ Q").replace("ins_essalud_x_q", "EsSalud $\\times$ Q")
    label = label.replace("ins_sis", "SIS").replace("ins_essalud", "EsSalud").replace("q", "Q")
    ols_c = ols_mod.params.get(var, np.nan)
    ols_s = ols_mod.bse.get(var, np.nan)
    ols_p = ols_mod.pvalues.get(var, np.nan)
    coef_cells = [f"{ols_c:.4f}{stars_fn(ols_p)}"]
    se_cells = [f"({ols_s:.4f})"]
    for tau in TAUS:
        r = qr_results[tau]
        c = r["coefs"].get(var, np.nan)
        s = r["ses"].get(var, np.nan)
        p = r["pvals"].get(var, np.nan)
        coef_cells.append(f"{c:.4f}{stars_fn(p) if np.isfinite(p) else ''}")
        se_cells.append(f"({s:.4f})" if np.isfinite(s) else "(--)")
    tex.append(f"  {label} & " + " & ".join(coef_cells) + " \\\\")
    tex.append(f"  & " + " & ".join(se_cells) + " \\\\")

tex.append("\\midrule")
tex.append(f"  N & {len(df):,} & " + " & ".join(f"{len(df):,}" for _ in TAUS) + " \\\\")
pr2_cells = [f"{ols_mod.rsquared:.4f}"]
for tau in TAUS:
    pr2 = qr_results[tau]["pr2"]
    pr2_cells.append(f"{pr2:.4f}" if np.isfinite(pr2) else "--")
tex.append(f"  R$^2$/Pseudo-R$^2$ & " + " & ".join(pr2_cells) + " \\\\")

tex += ["\\bottomrule", "\\end{tabular}",
        "\\begin{minipage}{\\textwidth}\\footnotesize",
        "\\textit{Notes:} Coefficients represent changes in the conditional $\\tau$-quantile of OOP",
        "health expenditure share, not average marginal effects. Causal interpretation is not warranted",
        "given non-random insurance assignment. OLS is survey-weighted (FACTOR07) with cluster-robust SEs.",
        f"QR uses cluster-bootstrapped SEs ({N_BOOT} reps, PSU-level). Q1 and Uninsured are omitted.",
        "*** p$<$0.01, ** p$<$0.05, * p$<$0.10.",
        "\\end{minipage}", "\\end{table}"]
(TABLE_DIR / "table2_qr_main.tex").write_text("\n".join(tex), encoding="utf-8")
print("  Table 2 saved.")

# Table 3: Total effect matrix
tex3 = ["\\begin{table}[htbp]", "\\centering",
        "\\caption{Total Insurance Association with OOP Share by Quintile}",
        "\\label{tab:total_effect}", "\\small",
        "\\begin{tabular}{ll" + "c" * len(TAUS) + "}", "\\toprule",
        "Insurance & Quintile & " + " & ".join(f"$\\tau={t}$" for t in TAUS) + " \\\\", "\\midrule"]
for lbl in ["SIS", "EsSalud"]:
    for q in [1, 2, 3, 4, 5]:
        cells = []
        for tau in TAUS:
            row = te_df[(te_df["tau"]==tau) & (te_df["quintile"]==q) & (te_df["insurance"]==lbl)]
            if len(row) > 0:
                val, p = row.iloc[0]["total_effect"], row.iloc[0]["pvalue"]
                cells.append(f"{val:+.4f}{stars_fn(p)}")
            else:
                cells.append("--")
        prefix = lbl if q == 1 else ""
        tex3.append(f"  {prefix} & Q{q} & " + " & ".join(cells) + " \\\\")
    if lbl == "SIS":
        tex3.append("\\midrule")
tex3 += ["\\bottomrule", "\\end{tabular}",
         "\\begin{minipage}{\\textwidth}\\footnotesize",
         "\\textit{Notes:} Total association = base coefficient + interaction.",
         f"Cluster-bootstrapped SEs ({N_BOOT} reps). *** p$<$0.01, ** p$<$0.05, * p$<$0.10.",
         "\\end{minipage}", "\\end{table}"]
(TABLE_DIR / "table3_total_effect.tex").write_text("\n".join(tex3), encoding="utf-8")
print("  Table 3 saved.")

print(f"\n{SEP}\n01_main.py complete.\n{SEP}")