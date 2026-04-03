"""
03_output.py
------------
Figures (PDF), LaTeX tables, results summary.
"""

import warnings
warnings.filterwarnings("ignore")

from pathlib import Path
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

# ── paths ──────────────────────────────────────────────────────────────
PROJECT = Path(__file__).resolve().parents[2]
CLEAN   = PROJECT / "data" / "clean"
FIGS    = PROJECT / "paper" / "figures"
TABLES  = PROJECT / "paper" / "tables"
FIGS.mkdir(parents=True, exist_ok=True)
TABLES.mkdir(parents=True, exist_ok=True)

# ── load ───────────────────────────────────────────────────────────────
balance = pd.read_csv(CLEAN / "balance_table.csv")
main    = pd.read_csv(CLEAN / "main_results.csv")
cate    = pd.read_csv(CLEAN / "cate_results.csv")
perm    = pd.read_csv(CLEAN / "permutation_distribution.csv")
robust  = pd.read_csv(CLEAN / "robustness_results.csv")

# =====================================================================
# FIGURE 1: Balance table visualization (SMDs with 95% CIs)
# =====================================================================
fig, ax = plt.subplots(figsize=(7, 6))
y_pos = np.arange(len(balance))
# CI for SMD: approximate SE = sqrt(1/n1 + 1/n2 + smd^2/(2*(n1+n2)))
# But simpler: use t_stat to back out SE of diff, then smd_se = se_diff / pooled_sd
# Since SMD = diff / pooled_sd, and we have the t-stat from diff,
# we use smd_se approx = |smd / t_stat| where t_stat != 0
smd_se = np.where(
    np.abs(balance["t_stat"]) > 1e-8,
    np.abs(balance["smd"] / balance["t_stat"]),
    0
)
ci_lo = balance["smd"] - 1.96 * smd_se
ci_hi = balance["smd"] + 1.96 * smd_se

ax.errorbar(balance["smd"], y_pos, xerr=1.96 * smd_se,
            fmt="o", color="steelblue", capsize=3, markersize=5)
ax.axvline(0, color="black", linewidth=0.8, linestyle="--")
ax.axvspan(-0.1, 0.1, alpha=0.1, color="green")
ax.set_yticks(y_pos)
ax.set_yticklabels(balance["variable"], fontsize=8)
ax.set_xlabel("Standardized Mean Difference (SMD)")
ax.set_title("Figure 1: Covariate Balance (Treatment vs. Control)")
ax.invert_yaxis()
plt.tight_layout()
fig.savefig(FIGS / "fig1_balance_smd.pdf", bbox_inches="tight")
plt.close()
print("Figure 1 saved.")

# =====================================================================
# FIGURE 2: Main treatment effects (3 specs)
# =====================================================================
specs = main[main["specification"].isin([
    "Raw difference in means",
    "OLS with baseline controls",
    "Double LASSO",
])].copy()
# Handle case where Double LASSO has different name
if len(specs) < 3:
    specs = main.iloc[:3].copy()

fig, ax = plt.subplots(figsize=(7, 4))
y_pos = np.arange(len(specs))
labels = specs["specification"].values
coefs = specs["coef"].values.astype(float)
ci_lo = specs["ci_lower"].values.astype(float)
ci_hi = specs["ci_upper"].values.astype(float)
xerr_lo = coefs - ci_lo
xerr_hi = ci_hi - coefs

ax.errorbar(coefs, y_pos, xerr=[xerr_lo, xerr_hi],
            fmt="s", color="darkred", capsize=4, markersize=7)
ax.axvline(0, color="black", linewidth=0.8, linestyle="--")
ax.set_yticks(y_pos)
ax.set_yticklabels(labels, fontsize=9)
ax.set_xlabel("Treatment Effect on ICC Referral Support")
ax.set_title("Figure 2: ATE Across Specifications (95% CI)")
ax.invert_yaxis()
plt.tight_layout()
fig.savefig(FIGS / "fig2_main_effects.pdf", bbox_inches="tight")
plt.close()
print("Figure 2 saved.")

# =====================================================================
# FIGURE 3: CATE by pro_israel quintile
# =====================================================================
ate_row = main[main["specification"] == "Raw difference in means"].iloc[0]
ate_val = float(ate_row["coef"])

fig, ax = plt.subplots(figsize=(7, 5))
x = cate["quintile"].values
y = cate["cate"].values
ci_lo = cate["ci_lower"].values
ci_hi = cate["ci_upper"].values

ax.bar(x, y, color="steelblue", alpha=0.7, width=0.6, zorder=2)
ax.errorbar(x, y, yerr=[y - ci_lo, ci_hi - y],
            fmt="none", color="black", capsize=4, zorder=3)
ax.axhline(ate_val, color="red", linestyle="--", linewidth=1.2, label=f"ATE = {ate_val:.3f}")
ax.axhline(0, color="black", linewidth=0.5)

# Mark BH significance
if "p_bh_adjusted" in cate.columns:
    for i, row in cate.iterrows():
        if row["p_bh_adjusted"] < 0.05:
            ax.text(row["quintile"], ci_hi[i] + 0.02, "*",
                    ha="center", fontsize=14, fontweight="bold")

ax.set_xlabel("Pro-Israel Score Quintile")
ax.set_ylabel("CATE on ICC Referral")
ax.set_title("Figure 3: CATE by Pro-Israel Quintile (BH-adjusted)")
ax.set_xticks(x)
ax.legend()
plt.tight_layout()
fig.savefig(FIGS / "fig3_cate_quintile.pdf", bbox_inches="tight")
plt.close()
print("Figure 3 saved.")

# =====================================================================
# FIGURE 4: Permutation distribution
# =====================================================================
actual_diff = ate_val
fig, ax = plt.subplots(figsize=(7, 4))
ax.hist(perm["permutation_diff"], bins=50, color="gray", alpha=0.7, edgecolor="white")
ax.axvline(actual_diff, color="red", linewidth=2, linestyle="--",
           label=f"Observed diff = {actual_diff:.4f}")
ax.axvline(-actual_diff, color="red", linewidth=1, linestyle=":", alpha=0.5)
perm_p = (np.abs(perm["permutation_diff"]) >= np.abs(actual_diff)).mean()
ax.set_xlabel("Permuted Treatment Effect")
ax.set_ylabel("Frequency")
ax.set_title(f"Figure 4: Permutation Distribution (p = {perm_p:.4f})")
ax.legend()
plt.tight_layout()
fig.savefig(FIGS / "fig4_permutation.pdf", bbox_inches="tight")
plt.close()
print("Figure 4 saved.")

# =====================================================================
# LaTeX TABLES
# =====================================================================

def escape_latex(s):
    """Escape underscores for LaTeX."""
    if isinstance(s, str):
        return s.replace("_", r"\_")
    return s

# ── Table 1: Balance ──────────────────────────────────────────────────
with open(TABLES / "table1_balance.tex", "w") as f:
    f.write(r"\begin{table}[htbp]" + "\n")
    f.write(r"\centering" + "\n")
    f.write(r"\caption{Covariate Balance: Treatment vs.\ Control}" + "\n")
    f.write(r"\label{tab:balance}" + "\n")
    f.write(r"\begin{tabular}{lcccccc}" + "\n")
    f.write(r"\hline\hline" + "\n")
    f.write(r"Variable & Mean (T) & Mean (C) & Diff & $t$-stat & $p$-value & SMD \\" + "\n")
    f.write(r"\hline" + "\n")
    for _, row in balance.iterrows():
        name = escape_latex(row["variable"])
        f.write(f"{name} & {row['mean_treated']:.3f} & {row['mean_control']:.3f} & "
                f"{row['difference']:.3f} & {row['t_stat']:.2f} & {row['p_value']:.3f} & "
                f"{row['smd']:.3f} \\\\\n")
    f.write(r"\hline\hline" + "\n")
    f.write(r"\end{tabular}" + "\n")
    f.write(r"\end{table}" + "\n")
print("Table 1 saved.")

# ── Table 2: Main results ────────────────────────────────────────────
spec_rows = main[main["specification"].isin([
    "Raw difference in means",
    "OLS with baseline controls",
    "Double LASSO",
])].copy()
if len(spec_rows) < 3:
    spec_rows = main.iloc[:3].copy()

with open(TABLES / "table2_main.tex", "w") as f:
    f.write(r"\begin{table}[htbp]" + "\n")
    f.write(r"\centering" + "\n")
    f.write(r"\caption{Main Treatment Effects on ICC Referral Support}" + "\n")
    f.write(r"\label{tab:main}" + "\n")
    f.write(r"\begin{tabular}{lccc}" + "\n")
    f.write(r"\hline\hline" + "\n")
    f.write(r" & (1) No Controls & (2) Baseline & (3) Double LASSO \\" + "\n")
    f.write(r"\hline" + "\n")
    f.write(r"Treatment & ")
    coefs = []
    ses = []
    for _, row in spec_rows.iterrows():
        stars = ""
        pv = row["p_value"]
        if pd.notna(pv):
            if pv < 0.01:
                stars = "***"
            elif pv < 0.05:
                stars = "**"
            elif pv < 0.1:
                stars = "*"
        coefs.append(f"{row['coef']:.4f}{stars}")
        ses.append(f"({row['se_hc2']:.4f})")
    f.write(" & ".join(coefs) + r" \\" + "\n")
    f.write(r" & " + " & ".join(ses) + r" \\" + "\n")
    f.write(r"\hline" + "\n")
    for _, row in spec_rows.iterrows():
        pass
    ns = [str(int(row["n"])) if pd.notna(row.get("n")) else "" for _, row in spec_rows.iterrows()]
    r2s = [f"{row['r_squared']:.4f}" if pd.notna(row.get("r_squared")) else "" for _, row in spec_rows.iterrows()]
    f.write(r"$N$ & " + " & ".join(ns) + r" \\" + "\n")
    f.write(r"$R^2$ & " + " & ".join(r2s) + r" \\" + "\n")
    f.write(r"\hline\hline" + "\n")
    f.write(r"\multicolumn{4}{l}{\footnotesize HC2 robust standard errors in parentheses.} \\" + "\n")
    f.write(r"\multicolumn{4}{l}{\footnotesize * $p<0.10$, ** $p<0.05$, *** $p<0.01$} \\" + "\n")
    f.write(r"\end{tabular}" + "\n")
    f.write(r"\end{table}" + "\n")
print("Table 2 saved.")

# ── Table 3: CATE ────────────────────────────────────────────────────
with open(TABLES / "table3_cate.tex", "w") as f:
    f.write(r"\begin{table}[htbp]" + "\n")
    f.write(r"\centering" + "\n")
    f.write(r"\caption{CATE by Pro-Israel Score Quintile}" + "\n")
    f.write(r"\label{tab:cate}" + "\n")
    f.write(r"\begin{tabular}{lcccccc}" + "\n")
    f.write(r"\hline\hline" + "\n")
    f.write(r"Quintile & CATE & SE (HC2) & 95\% CI & $p$-value & $p$ (BH) \\" + "\n")
    f.write(r"\hline" + "\n")
    for _, row in cate.iterrows():
        stars = ""
        pbh = row.get("p_bh_adjusted", row["p_value"])
        if pd.notna(pbh):
            if pbh < 0.01:
                stars = "***"
            elif pbh < 0.05:
                stars = "**"
            elif pbh < 0.1:
                stars = "*"
        ci_str = f"[{row['ci_lower']:.3f}, {row['ci_upper']:.3f}]"
        f.write(f"Q{int(row['quintile'])} & {row['cate']:.4f}{stars} & {row['se_hc2']:.4f} & "
                f"{ci_str} & {row['p_value']:.4f} & {pbh:.4f} \\\\\n")
    f.write(r"\hline\hline" + "\n")
    f.write(r"\multicolumn{6}{l}{\footnotesize BH = Benjamini-Hochberg adjusted $p$-values.} \\" + "\n")
    f.write(r"\end{tabular}" + "\n")
    f.write(r"\end{table}" + "\n")
print("Table 3 saved.")

# ── Table 4: Robustness ──────────────────────────────────────────────
with open(TABLES / "table4_robustness.tex", "w") as f:
    f.write(r"\begin{table}[htbp]" + "\n")
    f.write(r"\centering" + "\n")
    f.write(r"\caption{Robustness Checks}" + "\n")
    f.write(r"\label{tab:robustness}" + "\n")
    f.write(r"\begin{tabular}{lccccc}" + "\n")
    f.write(r"\hline\hline" + "\n")
    f.write(r"Test & Outcome & Coef & SE & $p$-value & $N$ \\" + "\n")
    f.write(r"\hline" + "\n")
    for _, row in robust.iterrows():
        test_name = escape_latex(str(row["test"]))
        outcome = escape_latex(str(row.get("outcome", "")))
        coef_s = f"{row['coef']:.4f}" if pd.notna(row.get("coef")) else str(row.get("note", ""))
        se_s = f"{row['se']:.4f}" if pd.notna(row.get("se")) else ""
        p_s = f"{row['p_value']:.4f}" if pd.notna(row.get("p_value")) else ""
        n_s = str(int(row["n"])) if pd.notna(row.get("n")) else ""
        f.write(f"{test_name} & {outcome} & {coef_s} & {se_s} & {p_s} & {n_s} \\\\\n")
    f.write(r"\hline\hline" + "\n")
    f.write(r"\end{tabular}" + "\n")
    f.write(r"\end{table}" + "\n")
print("Table 4 saved.")

# =====================================================================
# Results summary
# =====================================================================
with open(CLEAN / "results_summary.md", "w") as f:
    f.write("# Results Summary\n\n")

    f.write("## Main Treatment Effects\n\n")
    for _, row in spec_rows.iterrows():
        ci_str = ""
        if pd.notna(row.get("ci_lower")) and pd.notna(row.get("ci_upper")):
            ci_str = f" 95% CI [{row['ci_lower']:.4f}, {row['ci_upper']:.4f}]"
        f.write(f"- **{row['specification']}**: coef = {row['coef']:.4f}, "
                f"SE = {row['se_hc2']:.4f}, p = {row['p_value']:.4f}{ci_str}\n")

    # Cohen's d
    cd_row = main[main["specification"] == "Cohen's d"]
    if len(cd_row) > 0:
        f.write(f"\nCohen's d = {float(cd_row.iloc[0]['coef']):.4f}\n")

    # Permutation
    perm_row = main[main["specification"].str.contains("Permutation", na=False)]
    if len(perm_row) > 0:
        f.write(f"\nPermutation test p-value = {float(perm_row.iloc[0]['p_value']):.4f}\n")

    f.write("\n## CATE by Pro-Israel Quintile\n\n")
    for _, row in cate.iterrows():
        sig = ""
        pbh = row.get("p_bh_adjusted", row["p_value"])
        if pd.notna(pbh) and pbh < 0.05:
            sig = " (significant after BH correction)"
        f.write(f"- Q{int(row['quintile'])}: CATE = {row['cate']:.4f}, "
                f"p = {row['p_value']:.4f}, p(BH) = {pbh:.4f}{sig}\n")

    f.write("\n## Robustness\n\n")
    for _, row in robust.iterrows():
        coef_s = f"{row['coef']:.4f}" if pd.notna(row.get("coef")) else str(row.get("note", ""))
        p_s = f", p = {row['p_value']:.4f}" if pd.notna(row.get("p_value")) else ""
        f.write(f"- {row['test']}: {coef_s}{p_s}\n")

print("Results summary saved.")
print("03_output.py complete.")
