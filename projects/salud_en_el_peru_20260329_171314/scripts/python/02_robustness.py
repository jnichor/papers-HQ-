# =============================================================================
# 02_robustness.py  --  Robustness Checks (Referee Checklist Compliant)
# Includes: CHE thresholds, alt floors, urban/rural, weighted/unweighted,
# x12 annualization, placebo, control sensitivity, QR90
# =============================================================================
import warnings
warnings.filterwarnings("ignore")

import numpy as np
import pandas as pd
from pathlib import Path
import statsmodels.api as sm
from statsmodels.regression.linear_model import WLS
from statsmodels.regression.quantile_regression import QuantReg

np.random.seed(42)

PROJECT = Path(__file__).resolve().parent.parent.parent
CLEAN_DIR = PROJECT / "data" / "clean"
TABLE_DIR = PROJECT / "paper" / "tables"
TABLE_DIR.mkdir(parents=True, exist_ok=True)

SEP = "=" * 68
print(SEP)
print("02_robustness.py -- Robustness Checks (Referee Compliant)")
print(SEP)

df = pd.read_csv(CLEAN_DIR / "clean_data.csv")
print(f"Loaded {len(df):,} households")

OUTCOME = "oop_share"
TREATMENT = "ins_sis"
CONTROLS_DEMO = ["age_head", "age_head_sq", "female_head", "educ_years"]
CONTROLS_HH = ["hh_size", "children_u5", "elderly_65", "rural"]
CONTROLS_HEALTH = ["hospitalized", "chronic_any"]
CONTROLS_ALL = CONTROLS_DEMO + CONTROLS_HH + CONTROLS_HEALTH

dept_dummies = pd.get_dummies(df["department"], prefix="dept", drop_first=True, dtype=int)
df = pd.concat([df, dept_dummies], axis=1)
REGION_FE = list(dept_dummies.columns)

df["w"] = df["FACTOR07"] / df["FACTOR07"].mean()

def stars_fn(p):
    if p is None or not np.isfinite(p): return ""
    if p < 0.01: return "***"
    if p < 0.05: return "**"
    if p < 0.10: return "*"
    return ""

def run_ols(data, outcome, treatment, check_name, controls=None, weighted=True):
    if controls is None:
        controls = CONTROLS_ALL + REGION_FE
    xvars = [treatment] + controls
    d = data[[outcome, "CONGLOME", "w"] + xvars].replace([np.inf, -np.inf], np.nan).dropna()
    if len(d) < 50:
        print(f"  {check_name}: skipped (N={len(d)})")
        return None
    y = d[outcome].astype(float)
    X = sm.add_constant(d[xvars].astype(float), has_constant="add")
    try:
        if weighted:
            mod = WLS(y, X, weights=d["w"].values).fit(
                cov_type="cluster", cov_kwds={"groups": d["CONGLOME"].values})
        else:
            mod = sm.OLS(y, X).fit(
                cov_type="cluster", cov_kwds={"groups": d["CONGLOME"].values})
        c = mod.params.get(treatment, np.nan)
        s = mod.bse.get(treatment, np.nan)
        p = mod.pvalues.get(treatment, np.nan)
        print(f"  {check_name}: coef={c:+.4f}{stars_fn(p)} (SE={s:.4f}, p={p:.3f}, N={len(d):,})")
        return {"check": check_name, "outcome": outcome, "coef": c, "se": s, "pvalue": p, "n": len(d)}
    except Exception as e:
        print(f"  {check_name}: FAILED ({e})")
        return None

rob = []

# -- (a) OLS Comparison -------------------------------------------------------
print(f"\n{'='*40}\n(a) OLS Comparison\n{'='*40}")
r = run_ols(df, OUTCOME, TREATMENT, "a1-Weighted-FullControls"); rob.append(r) if r else None
r = run_ols(df, OUTCOME, TREATMENT, "a2-Weighted-NoRegionFE", CONTROLS_ALL); rob.append(r) if r else None
r = run_ols(df, OUTCOME, TREATMENT, "a3-Weighted-Bivariate", []); rob.append(r) if r else None
r = run_ols(df, OUTCOME, TREATMENT, "a4-Unweighted-FullControls", weighted=False); rob.append(r) if r else None

# -- (b) Alternative Samples --------------------------------------------------
print(f"\n{'='*40}\n(b) Alternative Samples\n{'='*40}")
r = run_ols(df[df["rural"]==0], OUTCOME, TREATMENT, "b1-UrbanOnly"); rob.append(r) if r else None
r = run_ols(df[df["rural"]==1], OUTCOME, TREATMENT, "b2-RuralOnly"); rob.append(r) if r else None
r = run_ols(df[(df["age_head"]>=25)&(df["age_head"]<=65)], OUTCOME, TREATMENT, "b3-WorkingAge"); rob.append(r) if r else None
r = run_ols(df[df["zero_oop"]==0], OUTCOME, TREATMENT, "b4-PositiveOOP"); rob.append(r) if r else None

# -- (c) Alternative CHE Thresholds -------------------------------------------
print(f"\n{'='*40}\n(c) CHE Thresholds\n{'='*40}")
for thresh in [10, 25, 40]:
    col = f"che_{thresh}pct"
    if col in df.columns:
        r = run_ols(df, col, TREATMENT, f"c-CHE{thresh}pct"); rob.append(r) if r else None

# -- (d) Placebo / Falsification -----------------------------------------------
print(f"\n{'='*40}\n(d) Placebo\n{'='*40}")
placebo_rng = np.random.default_rng(99)
df["placebo_treat"] = placebo_rng.integers(0, 2, size=len(df))
r = run_ols(df, OUTCOME, "placebo_treat", "d1-RandomPlacebo"); rob.append(r) if r else None
df_falsif = df[df["insurance_cat"].isin(["EsSalud", "Uninsured"])].copy()
if len(df_falsif) > 50:
    r = run_ols(df_falsif, OUTCOME, "ins_essalud", "d2-EsSalud-vs-Unins"); rob.append(r) if r else None

# -- (e) Control Sensitivity ---------------------------------------------------
print(f"\n{'='*40}\n(e) Control Sensitivity\n{'='*40}")
r = run_ols(df, OUTCOME, TREATMENT, "e1-NoControls", []); rob.append(r) if r else None
r = run_ols(df, OUTCOME, TREATMENT, "e2-DemoOnly", CONTROLS_DEMO); rob.append(r) if r else None
r = run_ols(df, OUTCOME, TREATMENT, "e3-Demo+HH", CONTROLS_DEMO+CONTROLS_HH); rob.append(r) if r else None
r = run_ols(df, OUTCOME, TREATMENT, "e4-Full-NoRegion", CONTROLS_ALL); rob.append(r) if r else None
r = run_ols(df, OUTCOME, TREATMENT, "e5-Full+RegionFE", CONTROLS_ALL+REGION_FE); rob.append(r) if r else None

# -- (f) Alternative consumption floors ----------------------------------------
print(f"\n{'='*40}\n(f) Alt Consumption Floors\n{'='*40}")
for pct, label in [(0.01, "f1-Floor-1pct"), (0.10, "f2-Floor-10pct")]:
    floor = max(df["total_consumption"].quantile(pct), 500)
    df_alt = df.copy()
    df_alt["oop_share"] = df_alt["health_expend"] / df_alt["total_consumption"].clip(lower=floor)
    df_alt["oop_share"] = df_alt["oop_share"].clip(0, 1)
    r = run_ols(df_alt, OUTCOME, TREATMENT, label); rob.append(r) if r else None

# -- (g) x12 annualization robustness -----------------------------------------
print(f"\n{'='*40}\n(g) x12 Annualization\n{'='*40}")
r = run_ols(df, "oop_share_x12", TREATMENT, "g1-Annualize-x12"); rob.append(r) if r else None

# -- (h) No cap robustness ----------------------------------------------------
print(f"\n{'='*40}\n(h) No Cap\n{'='*40}")
df_nocap = df.copy()
df_nocap["oop_share"] = df_nocap["health_expend"] / df_nocap["total_consumption"].clip(
    lower=df_nocap["total_consumption"].quantile(0.05))
r = run_ols(df_nocap, OUTCOME, TREATMENT, "h1-NoCap"); rob.append(r) if r else None

# -- (i) QR tau=0.90 Robustness ------------------------------------------------
print(f"\n{'='*40}\n(i) QR tau=0.90\n{'='*40}")
xvars_qr = [TREATMENT] + CONTROLS_ALL + REGION_FE
def run_qr90(data, label):
    d = data[[OUTCOME, "CONGLOME", "w"] + xvars_qr].replace([np.inf, -np.inf], np.nan).dropna()
    if len(d) < 100: return None
    y = d[OUTCOME].astype(float).values
    X = sm.add_constant(d[xvars_qr].astype(float), has_constant="add").values
    try:
        mod = QuantReg(y, X).fit(q=0.90, max_iter=5000)
        c, s, p = mod.params[1], mod.bse[1], mod.pvalues[1]
        print(f"  {label}: coef={c:+.4f}{stars_fn(p)} (SE={s:.4f}, p={p:.3f}, N={len(d):,})")
        return {"check": label, "outcome": OUTCOME, "coef": c, "se": s, "pvalue": p, "n": len(d)}
    except Exception as e:
        print(f"  {label}: FAILED ({e})"); return None

r = run_qr90(df, "i1-QR90-FullSample"); rob.append(r) if r else None
r = run_qr90(df[df["rural"]==0], "i2-QR90-UrbanOnly"); rob.append(r) if r else None
r = run_qr90(df[df["rural"]==1], "i3-QR90-RuralOnly"); rob.append(r) if r else None

# -- Save results --------------------------------------------------------------
rob = [r for r in rob if r is not None]
rob_df = pd.DataFrame(rob)
rob_df.to_csv(CLEAN_DIR / "robustness_results.csv", index=False)
print(f"\nTotal checks: {len(rob_df)}")
print(f"Significant at 5%: {(rob_df['pvalue'] < 0.05).sum()}")
print(f"Negative coefficient: {(rob_df['coef'] < 0).sum()}/{len(rob_df)}")

# -- LaTeX Table 4 -------------------------------------------------------------
if len(rob_df) > 0:
    sections = {"a": "OLS Comparison", "b": "Alternative Samples",
                "c": "CHE Thresholds", "d": "Placebo/Falsification",
                "e": "Control Sensitivity", "f": "Alt Consumption Floors",
                "g": "x12 Annualization", "h": "No Cap", "i": "QR $\\tau$=0.90"}
    tex = ["\\begin{table}[htbp]", "\\centering",
           "\\caption{Robustness Checks}", "\\label{tab:robustness}", "\\scriptsize",
           "\\begin{tabular}{llrrrr}", "\\toprule",
           "Check & Outcome & Coef. & SE & p-value & N \\\\", "\\midrule"]
    cur = None
    for _, r in rob_df.iterrows():
        sec = str(r["check"])[0]
        if sec != cur and sec in sections:
            tex.append(f"\\multicolumn{{6}}{{l}}{{\\textit{{({sec}) {sections[sec]}}}}} \\\\")
            cur = sec
        st = stars_fn(float(r["pvalue"]))
        chk = str(r["check"]).replace("_", "\\_")
        out = str(r["outcome"]).replace("_", "\\_")
        cv = float(r["coef"])
        cs = f"$-${abs(cv):.4f}{st}" if cv < 0 else f"{cv:.4f}{st}"
        tex.append(f"  {chk} & {out} & {cs} & {float(r['se']):.4f} & {float(r['pvalue']):.3f} & {int(r['n']):,} \\\\")
    tex += ["\\bottomrule", "\\end{tabular}",
            "\\begin{minipage}{\\textwidth}\\footnotesize",
            "\\textit{Notes:} Panels (a)--(h): survey-weighted OLS with cluster-robust SE (CONGLOME).",
            "Panel (i): Koenker--Bassett sandwich SE. *** p$<$0.01, ** p$<$0.05, * p$<$0.10.",
            "\\end{minipage}", "\\end{table}"]
    (TABLE_DIR / "table4_robustness.tex").write_text("\n".join(tex), encoding="utf-8")
    print("LaTeX Table 4 saved.")

print(f"\n{SEP}\n02_robustness.py complete.\n{SEP}")
