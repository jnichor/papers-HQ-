# =============================================================================
# 03_output.py  --  Publication Figures & Results Summary
# Referee Checklist Compliant: zero-OOP documentation, CQR vs RIF comparison
# =============================================================================
import os
import warnings
warnings.filterwarnings("ignore")
os.environ["SOURCE_DATE_EPOCH"] = "0"

import numpy as np
import pandas as pd
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.colors import TwoSlopeNorm

np.random.seed(42)

def stars_fn(p):
    if p is None or not np.isfinite(p): return ""
    if p < 0.01: return "***"
    if p < 0.05: return "**"
    if p < 0.10: return "*"
    return ""

PROJECT = Path(__file__).resolve().parent.parent.parent
CLEAN_DIR = PROJECT / "data" / "clean"
TABLE_DIR = PROJECT / "paper" / "tables"
FIG_DIR = PROJECT / "paper" / "figures"
for d in [TABLE_DIR, FIG_DIR]:
    d.mkdir(parents=True, exist_ok=True)

SEP = "=" * 68
print(SEP)
print("03_output.py -- Figures & Summary (Referee Compliant)")
print(SEP)

plt.rcParams.update({"figure.dpi": 300, "font.size": 11,
                      "axes.spines.top": False, "axes.spines.right": False})

df = pd.read_csv(CLEAN_DIR / "clean_data.csv")
print(f"Loaded {len(df):,} households")

# -- Fig 1: KDE by insurance ---------------------------------------------------
print("\n[Fig 1] KDE...")
fig, ax = plt.subplots(figsize=(7, 4))
for grp, color in [("SIS", "steelblue"), ("EsSalud", "darkorange"), ("Uninsured", "gray")]:
    vals = df.loc[df["insurance_cat"] == grp, "health_expend"]
    vals = vals[vals > 0]
    if len(vals) > 10:
        np.log1p(vals).plot.kde(ax=ax, label=f"{grp} (N={len(vals):,})", color=color, lw=2)
ax.set_xlabel("log(1 + Health Expenditure)")
ax.set_ylabel("Density")
ax.set_title("Health Expenditure Distribution by Insurance")
ax.legend()
plt.tight_layout()
fig.savefig(FIG_DIR / "fig1_kde_expenditure.pdf", bbox_inches="tight")
plt.close()

# -- Fig 2: QTE Profile -------------------------------------------------------
print("[Fig 2] QTE profile...")
qr_file = CLEAN_DIR / "qr_results.csv"
if qr_file.exists():
    qr = pd.read_csv(qr_file)
    sis_qr = qr[qr["variable"] == "ins_sis"]
    if len(sis_qr) > 0:
        fig, ax = plt.subplots(figsize=(7, 4.5))
        taus = sis_qr["tau"].values
        coefs = sis_qr["coef"].values
        ses = sis_qr["se"].values
        ax.plot(taus, coefs, "o-", color="steelblue", lw=2, ms=8, label="CQR coefficient")
        ax.fill_between(taus, coefs - 1.96*ses, coefs + 1.96*ses, alpha=0.2, color="steelblue")
        # Add OLS reference
        ols_file = CLEAN_DIR / "ols_results.csv"
        if ols_file.exists():
            ols = pd.read_csv(ols_file)
            ols_sis = ols[ols["variable"] == "ins_sis"]
            if len(ols_sis) > 0:
                ax.axhline(ols_sis.iloc[0]["coef"], color="red", ls="--", lw=1, label="OLS (weighted)")
        # Add RIF reference
        rif_file = CLEAN_DIR / "rif_results.csv"
        if rif_file.exists():
            rif = pd.read_csv(rif_file)
            rif_sis = rif[rif["variable"] == "ins_sis"]
            if len(rif_sis) > 0:
                ax.plot(rif_sis["tau"], rif_sis["coef"], "s--", color="green", lw=1.5, ms=6, label="RIF-OLS")
        ax.axhline(0, color="black", lw=0.5, ls="--")
        ax.set_xlabel("Quantile (tau)")
        ax.set_ylabel("SIS Coefficient")
        ax.set_title("CQR vs RIF-OLS: SIS Association with OOP Share")
        ax.legend()
        plt.tight_layout()
        fig.savefig(FIG_DIR / "fig2_qte_plot.pdf", bbox_inches="tight")
        plt.close()

# -- Fig 3: Heatmap -----------------------------------------------------------
print("[Fig 3] Heatmap...")
te_file = CLEAN_DIR / "total_effects.csv"
if te_file.exists():
    te = pd.read_csv(te_file)
    te_sis = te[te["insurance"] == "SIS"]
    if len(te_sis) > 0:
        pivot = te_sis.pivot(index="quintile", columns="tau", values="total_effect")
        fig, ax = plt.subplots(figsize=(8, 4))
        vmax = max(abs(pivot.values.min()), abs(pivot.values.max()), 0.01)
        norm = TwoSlopeNorm(vmin=-vmax, vcenter=0, vmax=vmax)
        im = ax.imshow(pivot.values, cmap="RdBu_r", norm=norm, aspect="auto")
        ax.set_xticks(range(len(pivot.columns)))
        ax.set_xticklabels([f"tau={t}" for t in pivot.columns])
        ax.set_yticks(range(len(pivot.index)))
        ax.set_yticklabels([f"Q{q}" for q in pivot.index])
        ax.set_title("Total SIS Association with OOP Share")
        for i in range(len(pivot.index)):
            for j in range(len(pivot.columns)):
                val = pivot.values[i, j]
                p_row = te_sis[(te_sis["quintile"]==pivot.index[i]) & (te_sis["tau"]==pivot.columns[j])]
                pv = p_row["pvalue"].values[0] if len(p_row) > 0 else 1
                st = "***" if pv < 0.01 else "**" if pv < 0.05 else "*" if pv < 0.10 else ""
                ax.text(j, i, f"{val:.3f}{st}", ha="center", va="center", fontsize=8)
        plt.colorbar(im, ax=ax, label="Association", shrink=0.8)
        plt.tight_layout()
        fig.savefig(FIG_DIR / "fig3_heatmap_total_effect.pdf", bbox_inches="tight")
        plt.close()

# -- Fig 4: CHE by insurance --------------------------------------------------
print("[Fig 4] CHE by insurance...")
groups = ["SIS", "EsSalud", "Uninsured"]
che_data = []
for g in groups:
    mask = df["insurance_cat"] == g
    if mask.sum() > 0:
        for thresh in [10, 25, 40]:
            col = f"che_{thresh}pct"
            if col in df.columns:
                che_data.append({"Insurance": g, "Threshold": f"{thresh}%",
                                "Rate": df.loc[mask, col].mean()})
if che_data:
    che_df = pd.DataFrame(che_data)
    fig, ax = plt.subplots(figsize=(7, 4.5))
    x = np.arange(len(groups))
    w = 0.25
    for i, thresh in enumerate(["10%", "25%", "40%"]):
        vals = [che_df.loc[(che_df["Insurance"]==g) & (che_df["Threshold"]==thresh), "Rate"].values
                for g in groups]
        vals = [v[0]*100 if len(v) > 0 else 0 for v in vals]
        ax.bar(x + i*w, vals, w, label=f"CHE > {thresh}")
    ax.set_xticks(x + w)
    ax.set_xticklabels(groups)
    ax.set_ylabel("CHE Incidence (%)")
    ax.set_title("Catastrophic Health Expenditure by Insurance")
    ax.legend()
    plt.tight_layout()
    fig.savefig(FIG_DIR / "fig4_che_by_insurance.pdf", bbox_inches="tight")
    plt.close()

# -- Fig 5: Robustness coefplot -----------------------------------------------
print("[Fig 5] Robustness coefplot...")
rob_file = CLEAN_DIR / "robustness_results.csv"
if rob_file.exists():
    rdf = pd.read_csv(rob_file)
    if len(rdf) > 0:
        fig, ax = plt.subplots(figsize=(8, max(4, len(rdf)*0.4)))
        y_pos = np.arange(len(rdf))
        coefs = rdf["coef"].values
        ci_lo = coefs - 1.96 * rdf["se"].values
        ci_hi = coefs + 1.96 * rdf["se"].values
        colors = ["steelblue" if p < 0.05 else "gray" for p in rdf["pvalue"]]
        ax.barh(y_pos, coefs, xerr=[coefs-ci_lo, ci_hi-coefs], color=colors, alpha=0.7, capsize=3)
        ax.set_yticks(y_pos)
        ax.set_yticklabels(rdf["check"], fontsize=7)
        ax.axvline(0, color="black", lw=0.5, ls="--")
        ax.set_xlabel("SIS Coefficient")
        ax.set_title("Robustness: SIS Association Across Specifications")
        ax.invert_yaxis()
        plt.tight_layout()
        fig.savefig(FIG_DIR / "fig5_robustness_coefplot.pdf", bbox_inches="tight")
        plt.close()

# -- Fig 6: OOP by quintile x insurance ----------------------------------------
print("[Fig 6] OOP by quintile...")
fig, ax = plt.subplots(figsize=(7, 4.5))
for grp, color in [("SIS", "steelblue"), ("EsSalud", "darkorange"), ("Uninsured", "gray")]:
    mask = df["insurance_cat"] == grp
    if mask.sum() > 10:
        means = df.loc[mask].groupby("quintile")["oop_share"].mean()
        ax.plot(means.index, means.values, "o-", color=color, lw=2, label=grp)
ax.set_xlabel("Consumption Quintile")
ax.set_ylabel("Mean OOP Share")
ax.set_title("OOP Share by Quintile and Insurance")
ax.legend()
plt.tight_layout()
fig.savefig(FIG_DIR / "fig6_expend_by_quintile.pdf", bbox_inches="tight")
plt.close()

# -- Fig 7: Zero OOP rates by quintile x insurance ----------------------------
print("[Fig 7] Zero OOP rates...")
fig, ax = plt.subplots(figsize=(7, 4.5))
for grp, color in [("SIS", "steelblue"), ("EsSalud", "darkorange"), ("Uninsured", "gray")]:
    mask = df["insurance_cat"] == grp
    if mask.sum() > 10:
        rates = df.loc[mask].groupby("quintile")["zero_oop"].mean() * 100
        ax.plot(rates.index, rates.values, "o-", color=color, lw=2, label=grp)
ax.set_xlabel("Consumption Quintile")
ax.set_ylabel("Zero OOP Rate (%)")
ax.set_title("Share with Zero Health Expenditure")
ax.legend()
plt.tight_layout()
fig.savefig(FIG_DIR / "fig7_zero_oop_rates.pdf", bbox_inches="tight")
plt.close()

# -- Results Summary -----------------------------------------------------------
print("\n[Summary] Writing results_summary.md...")
lines = [
    "# Results Summary -- ENAHO 2024 CHE Analysis (Referee Compliant)",
    "",
    "## Research Question",
    "Are health expenditure correlates quantile-dependent, consistent with the middle-income squeeze?",
    "",
    "## Method",
    "Conditional quantile regression at tau = {0.10, 0.25, 0.50, 0.75, 0.90}",
    "with insurance x consumption-quintile interactions.",
    "Complemented by: RIF unconditional QR, two-part model (probit + conditional QR).",
    f"Outcome: OOP share (mean={df['oop_share'].mean():.4f}, SD={df['oop_share'].std():.4f}).",
    f"Zero OOP rate: {df['zero_oop'].mean()*100:.1f}%.",
    f"Cluster-bootstrapped SEs (200 reps) at PSU level.",
    "Survey-weighted OLS (FACTOR07). All estimates are conditional associations, not causal effects.",
    "",
    "## Sample",
    f"- Total: {len(df):,} HH",
    f"- SIS: {(df['insurance_cat']=='SIS').sum():,} ({100*(df['insurance_cat']=='SIS').mean():.1f}%)",
    f"- EsSalud: {(df['insurance_cat']=='EsSalud').sum():,}",
    f"- Uninsured: {(df['insurance_cat']=='Uninsured').sum():,}",
    f"- CHE 10%: {df['che_10pct'].mean()*100:.2f}%",
    f"- CHE 25%: {df['che_25pct'].mean()*100:.2f}%",
    f"- CHE 40%: {df['che_40pct'].mean()*100:.2f}%",
]

qr_file = CLEAN_DIR / "qr_results.csv"
if qr_file.exists():
    qr = pd.read_csv(qr_file)
    sis_qr = qr[qr["variable"] == "ins_sis"]
    if len(sis_qr) > 0:
        med = sis_qr[sis_qr["tau"] == 0.50]
        if len(med) > 0:
            c, p = med.iloc[0]["coef"], med.iloc[0]["pvalue"]
            lines.append(f"\n## Main Finding")
            lines.append(f"At tau=0.50, SIS is associated with {c:+.4f} change in OOP share (p={p:.4f}).")
        lines += ["\n## QTE (SIS base, Q1)", "",
                  "| tau | CQR Coef | SE | p-value |",
                  "|-----|----------|-----|---------|"]
        for _, r in sis_qr.iterrows():
            st = stars_fn(r["pvalue"])
            lines.append(f"| {r['tau']} | {r['coef']:+.4f}{st} | {r['se']:.4f} | {r['pvalue']:.4f} |")

rob_file = CLEAN_DIR / "robustness_results.csv"
if rob_file.exists():
    rob = pd.read_csv(rob_file)
    lines += [f"\n## Robustness", f"- Total checks: {len(rob)}",
              f"- Significant at 5%: {(rob['pvalue']<0.05).sum()}",
              f"- Negative coefficient: {(rob['coef']<0).sum()}/{len(rob)}"]

lines += ["", "---", "Generated by 03_output.py"]
(TABLE_DIR / "results_summary.md").write_text("\n".join(lines), encoding="utf-8")
(CLEAN_DIR / "results_summary.md").write_text("\n".join(lines), encoding="utf-8")

print(f"\n{SEP}\n03_output.py complete.\n{SEP}")
