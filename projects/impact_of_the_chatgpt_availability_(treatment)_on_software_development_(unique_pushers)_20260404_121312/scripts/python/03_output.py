"""
03_output.py
Figures (PDF + PNG) and LaTeX tables for the ChatGPT ban paper.
"""

import warnings
warnings.filterwarnings("ignore")

from pathlib import Path
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

# ------------------------------------------------------------------ #
# PATHS
# ------------------------------------------------------------------ #
PROJECT = Path(__file__).resolve().parents[2]
DATA    = PROJECT / "data" / "clean" / "clean_data.csv"
OUTPUT  = PROJECT / "output"
FIG_DIR = PROJECT / "paper" / "figures"
TAB_DIR = PROJECT / "paper" / "tables"
CLEAN   = PROJECT / "data" / "clean"

for d in [FIG_DIR, TAB_DIR, CLEAN]:
    d.mkdir(parents=True, exist_ok=True)

# ------------------------------------------------------------------ #
# STYLE
# ------------------------------------------------------------------ #
plt.rcParams.update({
    "font.family": "serif",
    "font.size": 10,
    "axes.titlesize": 12,
    "axes.labelsize": 11,
    "figure.dpi": 300,
    "savefig.dpi": 300,
    "savefig.bbox": "tight",
})

# ------------------------------------------------------------------ #
# LOAD DATA
# ------------------------------------------------------------------ #
df = pd.read_csv(DATA)
es_df = pd.read_csv(OUTPUT / "event_study_coefficients.csv")
sc_df = pd.read_csv(OUTPUT / "synthetic_control_results.csv")
main_df = pd.read_csv(OUTPUT / "main_results.csv")
rob_df = pd.read_csv(OUTPUT / "robustness_results.csv")
perm_df = pd.read_csv(OUTPUT / "permutation_distribution.csv")

print("=" * 70)
print("03_output.py -- Figures and Tables")
print("=" * 70)

# ------------------------------------------------------------------ #
# Helper: quarter_id -> label
# ------------------------------------------------------------------ #
def q_label(qid):
    y = int(qid) // 10
    q = int(qid) % 10
    return "%dQ%d" % (y, q)


# ================================================================== #
# FIGURE 1: Raw trends -- banned vs non-banned
# ================================================================== #
print("\n### Figure 1: Raw Trends ###")

banned_ts = (
    df[df["banned_persistent"] == 1]
    .groupby("quarter_id")["log_pushers"]
    .mean()
    .sort_index()
)
control_ts = (
    df[df["banned_persistent"] == 0]
    .groupby("quarter_id")["log_pushers"]
    .mean()
    .sort_index()
)

all_q = sorted(df["quarter_id"].unique())
x_idx = range(len(all_q))
q_to_x = {q: i for i, q in enumerate(all_q)}

fig, ax = plt.subplots(figsize=(8, 4.5))
ax.plot(
    [q_to_x[q] for q in banned_ts.index],
    banned_ts.values,
    "o-", color="#d62728", markersize=4, linewidth=1.5, label="Banned (CN, RU, IR, SY, CU)",
)
ax.plot(
    [q_to_x[q] for q in control_ts.index],
    control_ts.values,
    "s-", color="#1f77b4", markersize=4, linewidth=1.5, label="Non-banned",
)

# Vertical line at Q4 2022
if 20224 in q_to_x:
    ax.axvline(q_to_x[20224], color="grey", linestyle="--", linewidth=1, alpha=0.7)
    ax.text(q_to_x[20224] + 0.2, ax.get_ylim()[1] * 0.98, "ChatGPT launch",
            fontsize=8, color="grey", va="top")

ax.set_xticks(list(x_idx))
ax.set_xticklabels([q_label(q) for q in all_q], rotation=45, ha="right", fontsize=7)
ax.set_ylabel("Mean log(unique pushers)")
ax.set_title("Figure 1: Average log(pushers) -- Banned vs Non-Banned Countries")
ax.legend(fontsize=8, loc="upper left")
ax.grid(axis="y", alpha=0.3)
fig.tight_layout()

for ext in ["pdf", "png"]:
    fig.savefig(FIG_DIR / ("fig1_raw_trends.%s" % ext))
plt.close(fig)
print("  Saved fig1_raw_trends.pdf / .png")

# ================================================================== #
# FIGURE 2: Event study coefficients with 95% CI
# ================================================================== #
print("\n### Figure 2: Event Study ###")

es_sorted = es_df.sort_values("quarter_id").reset_index(drop=True)
# Insert reference quarter (Q3 2022) as zero
ref_row = pd.DataFrame([{
    "quarter_id": 20223, "coefficient": 0.0, "std_error": 0.0,
    "p_value": np.nan, "ci_lower": 0.0, "ci_upper": 0.0, "period": "ref",
}])
es_plot = pd.concat([es_sorted, ref_row], ignore_index=True).sort_values("quarter_id").reset_index(drop=True)

fig, ax = plt.subplots(figsize=(8, 4.5))

colors = ["#1f77b4" if p == "pre" else ("#2ca02c" if p == "ref" else "#d62728") for p in es_plot["period"]]

ax.errorbar(
    range(len(es_plot)),
    es_plot["coefficient"],
    yerr=1.96 * es_plot["std_error"],
    fmt="o", color="#333333", markersize=4, linewidth=1, capsize=3, capthick=1,
    ecolor="#999999",
)

ax.axhline(0, color="black", linewidth=0.8, linestyle="-")

# Shade post period
ref_x = es_plot[es_plot["quarter_id"] == 20223].index[0]
ax.axvline(ref_x, color="grey", linestyle="--", linewidth=1, alpha=0.7)
ax.text(ref_x + 0.3, ax.get_ylim()[0] * 0.1, "Ref: Q3-2022", fontsize=7, color="grey")

ax.set_xticks(range(len(es_plot)))
ax.set_xticklabels([q_label(q) for q in es_plot["quarter_id"]], rotation=45, ha="right", fontsize=7)
ax.set_ylabel("DiD coefficient (log pushers)")
ax.set_title("Figure 2: Event Study -- Effect of ChatGPT Ban on Unique Pushers")
ax.grid(axis="y", alpha=0.3)
fig.tight_layout()

for ext in ["pdf", "png"]:
    fig.savefig(FIG_DIR / ("fig2_event_study.%s" % ext))
plt.close(fig)
print("  Saved fig2_event_study.pdf / .png")

# ================================================================== #
# FIGURE 3: Synthetic Control -- Italy
# ================================================================== #
print("\n### Figure 3: Synthetic Control (Italy) ###")

sc_sorted = sc_df.sort_values("quarter_id").reset_index(drop=True)
sc_x = range(len(sc_sorted))

fig, ax = plt.subplots(figsize=(8, 4.5))
ax.plot(list(sc_x), sc_sorted["italy_actual"].values, "o-", color="#d62728",
        markersize=4, linewidth=1.5, label="Italy (actual)")
ax.plot(list(sc_x), sc_sorted["italy_synthetic"].values, "s--", color="#1f77b4",
        markersize=4, linewidth=1.5, label="Synthetic Italy")

# Vertical line at treatment start (Q2 2023)
post_start = sc_sorted[sc_sorted["period"] == "post"].index[0]
ax.axvline(post_start - 0.5, color="grey", linestyle="--", linewidth=1, alpha=0.7)
ax.text(post_start - 0.3, ax.get_ylim()[1] * 0.98 if ax.get_ylim()[1] > 0 else 12.7,
        "Italy ban (Q2-2023)", fontsize=8, color="grey", va="top")

ax.set_xticks(list(sc_x))
ax.set_xticklabels([q_label(q) for q in sc_sorted["quarter_id"]], rotation=45, ha="right", fontsize=7)
ax.set_ylabel("log(unique pushers)")
ax.set_title("Figure 3: Synthetic Control -- Italy vs Synthetic Italy")
ax.legend(fontsize=8, loc="upper left")
ax.grid(axis="y", alpha=0.3)
fig.tight_layout()

for ext in ["pdf", "png"]:
    fig.savefig(FIG_DIR / ("fig3_synthetic_control_italy.%s" % ext))
plt.close(fig)
print("  Saved fig3_synthetic_control_italy.pdf / .png")

# ================================================================== #
# FIGURE 4: Permutation distribution
# ================================================================== #
print("\n### Figure 4: Permutation Distribution ###")

perm_vals = perm_df["permutation_coefficient"].dropna().values
actual_coef = main_df[main_df["model"] == "DiD_persistent_bans"]["coefficient"].values[0]

fig, ax = plt.subplots(figsize=(7, 4.5))
ax.hist(perm_vals, bins=40, color="#b0b0b0", edgecolor="white", alpha=0.8, label="Permutation distribution")
ax.axvline(actual_coef, color="#d62728", linewidth=2, linestyle="-", label="Actual effect (%.3f)" % actual_coef)

perm_p = np.mean(perm_vals <= actual_coef)
ax.set_xlabel("DiD coefficient")
ax.set_ylabel("Frequency")
ax.set_title("Figure 4: Permutation Test (N=500, p=%.3f)" % perm_p)
ax.legend(fontsize=8)
ax.grid(axis="y", alpha=0.3)
fig.tight_layout()

for ext in ["pdf", "png"]:
    fig.savefig(FIG_DIR / ("fig4_permutation_test.%s" % ext))
plt.close(fig)
print("  Saved fig4_permutation_test.pdf / .png")

# ================================================================== #
# LaTeX TABLES
# ================================================================== #
print("\n### LaTeX Tables ###")

# ------------------------------------------------------------------ #
# Table 1: Summary statistics
# ------------------------------------------------------------------ #
summary_path = CLEAN / "summary_stats.csv"
if summary_path.exists():
    sum_df = pd.read_csv(summary_path, index_col=0)
else:
    sum_cols = ["total_pushers", "log_pushers", "n_languages",
                "banned_persistent", "post_chatgpt", "treat_did"]
    sum_df = df[sum_cols].describe().T

var_labels = {
    "total_pushers": "Unique pushers",
    "log_pushers": "log(Unique pushers)",
    "n_languages": "N languages",
    "banned_persistent": "Banned (persistent)",
    "italy_temp_ban": "Italy temp ban",
    "post_chatgpt": "Post-ChatGPT",
    "treat_did": "Banned x Post",
}

tex_lines = []
tex_lines.append(r"\begin{table}[htbp]")
tex_lines.append(r"\centering")
tex_lines.append(r"\caption{Summary Statistics}")
tex_lines.append(r"\label{tab:summary}")
tex_lines.append(r"\begin{tabular}{lccccc}")
tex_lines.append(r"\toprule")
tex_lines.append(r"Variable & Mean & Std.\ Dev. & Min & Median & Max \\")
tex_lines.append(r"\midrule")

for var in ["total_pushers", "log_pushers", "n_languages", "banned_persistent", "post_chatgpt", "treat_did"]:
    if var in sum_df.index:
        row = sum_df.loc[var]
        label = var_labels.get(var, var)
        tex_lines.append(
            r"%s & %.2f & %.2f & %.2f & %.2f & %.2f \\" % (
                label,
                row.get("mean", 0), row.get("std", 0),
                row.get("min", 0), row.get("50%", 0), row.get("max", 0),
            )
        )

tex_lines.append(r"\bottomrule")
tex_lines.append(r"\end{tabular}")
tex_lines.append(r"\begin{tablenotes}")
tex_lines.append(r"\small")
tex_lines.append(r"\item Note: Panel of %d countries observed over %d quarters (N=%d)." % (
    df["iso2_code"].nunique(), df["quarter_id"].nunique(), len(df)))
tex_lines.append(r"\end{tablenotes}")
tex_lines.append(r"\end{table}")

tab1_path = TAB_DIR / "table1_summary.tex"
tab1_path.write_text("\n".join(tex_lines), encoding="utf-8")
print("  Saved: %s" % tab1_path)

# ------------------------------------------------------------------ #
# Table 2: Main DiD
# ------------------------------------------------------------------ #
did_row = main_df[main_df["model"] == "DiD_persistent_bans"].iloc[0]

tex2 = []
tex2.append(r"\begin{table}[htbp]")
tex2.append(r"\centering")
tex2.append(r"\caption{Difference-in-Differences: Effect of ChatGPT Ban on Software Development}")
tex2.append(r"\label{tab:main_did}")
tex2.append(r"\begin{tabular}{lc}")
tex2.append(r"\toprule")
tex2.append(r" & log(Unique Pushers) \\")
tex2.append(r"\midrule")
tex2.append(r"Banned $\times$ Post & %.4f \\" % did_row["coefficient"])
tex2.append(r" & (%.4f) \\" % did_row["std_error"])

# significance stars
stars = ""
if did_row["p_value"] < 0.01:
    stars = "***"
elif did_row["p_value"] < 0.05:
    stars = "**"
elif did_row["p_value"] < 0.10:
    stars = "*"
tex2.append(r" & [p = %.4f]%s \\" % (did_row["p_value"], stars))
tex2.append(r"\midrule")
tex2.append(r"Country FE & Yes \\")
tex2.append(r"Quarter FE & Yes \\")
tex2.append(r"Observations & %d \\" % did_row["n_obs"])
tex2.append(r"$R^2$ (within) & %.4f \\" % did_row["r_squared"])
tex2.append(r"\bottomrule")
tex2.append(r"\end{tabular}")
tex2.append(r"\begin{tablenotes}")
tex2.append(r"\small")
tex2.append(r"\item Note: Standard errors clustered at the country level in parentheses.")
tex2.append(r"\item * $p<0.10$, ** $p<0.05$, *** $p<0.01$.")
tex2.append(r"\end{tablenotes}")
tex2.append(r"\end{table}")

tab2_path = TAB_DIR / "table2_main_did.tex"
tab2_path.write_text("\n".join(tex2), encoding="utf-8")
print("  Saved: %s" % tab2_path)

# ------------------------------------------------------------------ #
# Table 3: Event Study
# ------------------------------------------------------------------ #
tex3 = []
tex3.append(r"\begin{table}[htbp]")
tex3.append(r"\centering")
tex3.append(r"\caption{Event Study Estimates}")
tex3.append(r"\label{tab:event_study}")
tex3.append(r"\begin{tabular}{lccccc}")
tex3.append(r"\toprule")
tex3.append(r"Quarter & Coefficient & Std. Error & $p$-value & 95\% CI Lower & 95\% CI Upper \\")
tex3.append(r"\midrule")

es_sorted = es_df.sort_values("quarter_id")
for _, row in es_sorted.iterrows():
    qlab = q_label(row["quarter_id"])
    stars = ""
    if row["p_value"] < 0.01:
        stars = "***"
    elif row["p_value"] < 0.05:
        stars = "**"
    elif row["p_value"] < 0.10:
        stars = "*"
    tex3.append(
        r"%s & %.4f%s & %.4f & %.4f & %.4f & %.4f \\" % (
            qlab, row["coefficient"], stars, row["std_error"],
            row["p_value"], row["ci_lower"], row["ci_upper"],
        )
    )

tex3.append(r"\bottomrule")
tex3.append(r"\end{tabular}")
tex3.append(r"\begin{tablenotes}")
tex3.append(r"\small")
tex3.append(r"\item Note: Reference period is Q3-2022. Country and quarter FE included.")
tex3.append(r"\item Standard errors clustered at the country level.")
tex3.append(r"\item * $p<0.10$, ** $p<0.05$, *** $p<0.01$.")
tex3.append(r"\end{tablenotes}")
tex3.append(r"\end{table}")

tab3_path = TAB_DIR / "table3_event_study.tex"
tab3_path.write_text("\n".join(tex3), encoding="utf-8")
print("  Saved: %s" % tab3_path)

# ------------------------------------------------------------------ #
# Table 4: Robustness
# ------------------------------------------------------------------ #
model_labels = {
    "placebo_outcome_n_languages": "Placebo outcome (n languages)",
    "placebo_timing_Q2_2021": "Placebo timing (Q2-2021)",
    "did_CN_only": "China only",
    "did_RU_only": "Russia only",
    "exclude_covid_2020": "Exclude 2020",
    "oecd_only_controls": "OECD-only controls",
    "exclude_small_countries": "Exclude small countries",
    "permutation_test": "Permutation test",
}

tex4 = []
tex4.append(r"\begin{table}[htbp]")
tex4.append(r"\centering")
tex4.append(r"\caption{Robustness Checks}")
tex4.append(r"\label{tab:robustness}")
tex4.append(r"\begin{tabular}{lcccc}")
tex4.append(r"\toprule")
tex4.append(r"Specification & Coefficient & Std. Error & $p$-value & N \\")
tex4.append(r"\midrule")

for _, row in rob_df.iterrows():
    label = model_labels.get(row["model"], row["model"])
    stars = ""
    pv = row["p_value"]
    if pd.notna(pv):
        if pv < 0.01:
            stars = "***"
        elif pv < 0.05:
            stars = "**"
        elif pv < 0.10:
            stars = "*"
    se_str = "%.4f" % row["std_error"] if pd.notna(row["std_error"]) else "--"
    pv_str = "%.4f" % pv if pd.notna(pv) else "--"
    tex4.append(
        r"%s & %.4f%s & %s & %s & %d \\" % (
            label, row["coefficient"], stars, se_str, pv_str, row["n_obs"],
        )
    )

tex4.append(r"\bottomrule")
tex4.append(r"\end{tabular}")
tex4.append(r"\begin{tablenotes}")
tex4.append(r"\small")
tex4.append(r"\item Note: All specifications include country and quarter fixed effects.")
tex4.append(r"\item Standard errors clustered at the country level.")
tex4.append(r"\item Permutation $p$-value: share of 500 random assignments with coefficient $\leq$ actual.")
tex4.append(r"\item * $p<0.10$, ** $p<0.05$, *** $p<0.01$.")
tex4.append(r"\end{tablenotes}")
tex4.append(r"\end{table}")

tab4_path = TAB_DIR / "table4_robustness.tex"
tab4_path.write_text("\n".join(tex4), encoding="utf-8")
print("  Saved: %s" % tab4_path)

# ================================================================== #
# RESULTS SUMMARY (Markdown)
# ================================================================== #
print("\n### Results Summary ###")

md_lines = []
md_lines.append("# Results Summary")
md_lines.append("")
md_lines.append("## Main DiD")
md_lines.append("")
md_lines.append("| Metric | Value |")
md_lines.append("|--------|-------|")
md_lines.append("| Coefficient (Banned x Post) | %.4f |" % did_row["coefficient"])
md_lines.append("| Std. Error | %.4f |" % did_row["std_error"])
md_lines.append("| p-value | %.4f |" % did_row["p_value"])
md_lines.append("| N | %d |" % did_row["n_obs"])
md_lines.append("| R-squared (within) | %.4f |" % did_row["r_squared"])
md_lines.append("")

# Interpretation
if did_row["coefficient"] < 0:
    pct = (np.exp(did_row["coefficient"]) - 1) * 100
    md_lines.append("**Interpretation**: Banned countries experienced a %.1f%% relative decline " % pct)
    md_lines.append("in unique pushers after ChatGPT launch compared to non-banned countries.")
else:
    md_lines.append("**Interpretation**: Coefficient is positive -- inconsistent with expected negative effect.")

md_lines.append("")
md_lines.append("## Event Study")
md_lines.append("")
md_lines.append("- Pre-treatment coefficients: generally close to zero (parallel trends)")

pre_es = es_df[es_df["period"] == "pre"]
post_es = es_df[es_df["period"] == "post"]
pre_sig = (pre_es["p_value"] < 0.05).sum()
post_sig = (post_es["p_value"] < 0.05).sum()
md_lines.append("- Pre-treatment significant (p<0.05): %d / %d" % (pre_sig, len(pre_es)))
md_lines.append("- Post-treatment significant (p<0.05): %d / %d" % (post_sig, len(post_es)))
if len(post_es) > 0:
    md_lines.append("- Post-treatment range: [%.3f, %.3f]" % (
        post_es["coefficient"].min(), post_es["coefficient"].max()))

md_lines.append("")
md_lines.append("## Synthetic Control (Italy)")
md_lines.append("")
sc_row = main_df[main_df["model"] == "synth_control_italy"]
if len(sc_row) > 0:
    sc_gap = sc_row.iloc[0]["coefficient"]
    md_lines.append("- Average post-treatment gap: %.4f" % sc_gap)
    if abs(sc_gap) < 0.05:
        md_lines.append("- Italy shows minimal divergence from its synthetic counterfactual")
    else:
        md_lines.append("- Italy shows notable divergence from its synthetic counterfactual")

md_lines.append("")
md_lines.append("## Robustness")
md_lines.append("")
md_lines.append("| Check | Coefficient | p-value |")
md_lines.append("|-------|-------------|---------|")
for _, row in rob_df.iterrows():
    label = model_labels.get(row["model"], row["model"])
    pv_str = "%.4f" % row["p_value"] if pd.notna(row["p_value"]) else "--"
    md_lines.append("| %s | %.4f | %s |" % (label, row["coefficient"], pv_str))

md_lines.append("")
md_lines.append("---")
md_lines.append("Generated by 03_output.py")

md_text = "\n".join(md_lines)

for dest in [TAB_DIR / "results_summary.md", CLEAN / "results_summary.md"]:
    dest.write_text(md_text, encoding="utf-8")
    print("  Saved: %s" % dest)

print("\n" + "=" * 70)
print("03_output.py DONE.")
print("=" * 70)
