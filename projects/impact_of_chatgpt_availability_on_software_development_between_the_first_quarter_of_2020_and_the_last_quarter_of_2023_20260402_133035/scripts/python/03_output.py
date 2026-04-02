"""
03_output.py — Publication-Quality Figures & Tables
====================================================
Generates all required figures and tables for the paper.

Figures:
  1. Raw trends (HHI & entropy by quarter, high/low EPI)
  2. Main event study plot (HHI panel A, entropy panel B)
  3. Heterogeneity event study (high vs low EPI)
  4. Placebo event study overlay
  A1. Country-level scatter (pre-post HHI change vs EPI)
  A2. Distribution of HHI (pre vs post)

Tables:
  - results_summary.md (formatted for paper)
"""

import warnings
warnings.filterwarnings("ignore")

from pathlib import Path
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker

# ── Paths ─────────────────────────────────────────────────────────────────────
PROJECT = Path(__file__).resolve().parents[2]
CLEAN_DIR = PROJECT / "data" / "clean"
FIG_DIR = PROJECT / "paper" / "figures"
TAB_DIR = PROJECT / "paper" / "tables"
FIG_DIR.mkdir(parents=True, exist_ok=True)
TAB_DIR.mkdir(parents=True, exist_ok=True)

panel = pd.read_csv(CLEAN_DIR / "clean_data.csv")
coefs = pd.read_csv(CLEAN_DIR / "event_study_coefficients.csv")
main_results = pd.read_csv(CLEAN_DIR / "main_results.csv")
robustness = pd.read_csv(CLEAN_DIR / "robustness_results.csv")
summary = pd.read_csv(CLEAN_DIR / "summary_stats.csv")

print("=" * 70)
print("03_output.py -- Publication-Quality Figures & Tables")
print("=" * 70)

# ── Style ─────────────────────────────────────────────────────────────────────
plt.rcParams.update({
    "font.family": "serif",
    "font.size": 11,
    "axes.labelsize": 12,
    "axes.titlesize": 13,
    "legend.fontsize": 10,
    "figure.dpi": 150,
    "savefig.dpi": 300,
    "savefig.bbox": "tight",
})

# Quarter labels for x-axis
quarter_labels = {}
for _, row in panel[["quarter_id", "year", "quarter"]].drop_duplicates().iterrows():
    qid = int(row["quarter_id"])
    quarter_labels[qid] = f"Q{int(row['quarter'])}\n{int(row['year'])}"

event_time_labels = {}
for _, row in panel[["event_time", "quarter_id"]].drop_duplicates().iterrows():
    et = int(row["event_time"])
    qid = int(row["quarter_id"])
    event_time_labels[et] = quarter_labels.get(qid, str(et))


# ═══════════════════════════════════════════════════════════════════════════════
# FIGURE 1: Raw Trends
# ═══════════════════════════════════════════════════════════════════════════════
print("\n[fig1] Raw trends...")

fig, axes = plt.subplots(1, 2, figsize=(14, 5))

# Split by EPI group
panel_epi = panel.dropna(subset=["epi_high"])

for ax, outcome, title in zip(axes, ["hhi_norm", "entropy"],
                                ["HHI (Normalized)", "Shannon Entropy"]):
    for grp, label, color in [(1, "High English Proficiency", "#2166ac"),
                               (0, "Low English Proficiency", "#b2182b")]:
        sub = panel_epi[panel_epi["epi_high"] == grp]
        ts = sub.groupby("quarter_id")[outcome].mean()
        ax.plot(ts.index, ts.values, marker="o", label=label, color=color,
                linewidth=2, markersize=5)

    # ChatGPT release line
    ax.axvline(x=20224, color="grey", linestyle="--", alpha=0.7, linewidth=1)
    ax.text(20224, ax.get_ylim()[1] * 0.98, "ChatGPT\nrelease",
            ha="center", va="top", fontsize=9, color="grey")

    ax.set_title(title)
    ax.set_xlabel("Quarter")
    ax.set_ylabel(title)
    ax.legend(loc="best")

    # Format x-axis
    xticks = sorted(panel["quarter_id"].unique())
    ax.set_xticks(xticks)
    ax.set_xticklabels([quarter_labels.get(q, str(q)) for q in xticks],
                        rotation=45, fontsize=8)

fig.suptitle("Figure 1: Language Ecosystem Concentration Before and After ChatGPT",
             fontsize=14, fontweight="bold", y=1.02)
plt.tight_layout()
fig.savefig(FIG_DIR / "fig1_raw_trends.pdf")
fig.savefig(FIG_DIR / "fig1_raw_trends.png")
plt.close()
print(f"  Saved: {FIG_DIR / 'fig1_raw_trends.pdf'}")


# ═══════════════════════════════════════════════════════════════════════════════
# FIGURE 2: Main Event Study
# ═══════════════════════════════════════════════════════════════════════════════
print("[fig2] Main event study...")

fig, axes = plt.subplots(1, 2, figsize=(14, 5))

for ax, outcome, title, panel_label in zip(
    axes,
    ["hhi_norm", "entropy"],
    ["HHI (Normalized)", "Shannon Entropy"],
    ["(A)", "(B)"]
):
    c = coefs[coefs["specification"] == f"main_{outcome}"].sort_values("event_time")

    ax.errorbar(c["event_time"], c["coef"], yerr=1.96 * c["se"],
                fmt="o-", color="#2166ac", capsize=3, linewidth=1.5, markersize=5)

    ax.axhline(y=0, color="black", linewidth=0.8)
    ax.axvline(x=-0.5, color="grey", linestyle="--", alpha=0.7, linewidth=1)

    # Label reference period
    ref = c[c["event_time"] == -1]
    if not ref.empty:
        ax.annotate("ref (t=-1)", xy=(-1, 0), fontsize=8, ha="center",
                    va="bottom", color="grey")

    ax.set_title(f"{panel_label} {title}")
    ax.set_xlabel("Event Time (quarters relative to Q1 2023)")
    ax.set_ylabel(f"Coefficient (β)")

    # N per period note
    n_obs = main_results[main_results["outcome"] == outcome]["n_obs"].values
    if len(n_obs) > 0:
        ax.text(0.02, 0.02, f"N={int(n_obs[0]):,}", transform=ax.transAxes,
                fontsize=9, va="bottom")

fig.suptitle("Figure 2: Event Study — Effect of ChatGPT on Language Ecosystem Concentration",
             fontsize=13, fontweight="bold", y=1.02)
plt.tight_layout()
fig.savefig(FIG_DIR / "fig2_event_study.pdf")
fig.savefig(FIG_DIR / "fig2_event_study.png")
plt.close()
print(f"  Saved: {FIG_DIR / 'fig2_event_study.pdf'}")


# ═══════════════════════════════════════════════════════════════════════════════
# FIGURE 3: Heterogeneity Event Study (High vs Low EPI)
# ═══════════════════════════════════════════════════════════════════════════════
print("[fig3] Heterogeneity event study...")

fig, axes = plt.subplots(1, 2, figsize=(14, 5))

for ax, outcome, title in zip(axes, ["hhi_norm", "entropy"],
                                ["HHI (Normalized)", "Shannon Entropy"]):
    for tercile, color, ls in [("high", "#2166ac", "-"),
                                ("low", "#b2182b", "--")]:
        spec = f"epi_tercile_{tercile}_{outcome}"
        c = coefs[coefs["specification"] == spec].sort_values("event_time")
        if c.empty:
            continue
        ax.errorbar(c["event_time"], c["coef"], yerr=1.96 * c["se"],
                    fmt="o", color=color, capsize=3, linewidth=1.5,
                    markersize=4, linestyle=ls,
                    label=f"{tercile.title()} English Proficiency")

    ax.axhline(y=0, color="black", linewidth=0.8)
    ax.axvline(x=-0.5, color="grey", linestyle="--", alpha=0.7, linewidth=1)
    ax.set_title(title)
    ax.set_xlabel("Event Time (quarters relative to Q1 2023)")
    ax.set_ylabel("Coefficient (β)")
    ax.legend(loc="best")

fig.suptitle("Figure 3: Heterogeneous Effects by English Proficiency",
             fontsize=13, fontweight="bold", y=1.02)
plt.tight_layout()
fig.savefig(FIG_DIR / "fig3_heterogeneity.pdf")
fig.savefig(FIG_DIR / "fig3_heterogeneity.png")
plt.close()
print(f"  Saved: {FIG_DIR / 'fig3_heterogeneity.pdf'}")


# ═══════════════════════════════════════════════════════════════════════════════
# FIGURE 4: Placebo Event Study
# ═══════════════════════════════════════════════════════════════════════════════
print("[fig4] Placebo comparison...")

fig, ax = plt.subplots(1, 1, figsize=(8, 5))

# True event study
c_true = coefs[coefs["specification"] == "main_hhi_norm"].sort_values("event_time")
ax.errorbar(c_true["event_time"], c_true["coef"], yerr=1.96 * c_true["se"],
            fmt="o-", color="#2166ac", capsize=3, linewidth=2,
            markersize=5, label="True (Q1 2023)")

# Placebo estimates from robustness
placebo_results = robustness[robustness["label"].str.contains("Placebo") &
                              robustness["outcome"].eq("hhi_norm")]
colors_placebo = {"Q1 2021": "#fdae61", "Q1 2022": "#d73027"}
for _, row in placebo_results.iterrows():
    name = row["label"].split(":")[0].replace("Placebo ", "")
    color = colors_placebo.get(name, "grey")
    ax.scatter(0, row["att"], marker="x", s=100, color=color, zorder=5, label=f"Placebo {name}")
    if not np.isnan(row.get("ci_low", np.nan)):
        ax.errorbar(0, row["att"],
                    yerr=[[row["att"] - row["ci_low"]], [row["ci_high"] - row["att"]]],
                    fmt="none", color=color, capsize=5)

ax.axhline(y=0, color="black", linewidth=0.8)
ax.axvline(x=-0.5, color="grey", linestyle="--", alpha=0.7)
ax.set_xlabel("Event Time")
ax.set_ylabel("Coefficient (β)")
ax.set_title("Figure 4: True vs Placebo Treatment Effects on HHI")
ax.legend(loc="best")
plt.tight_layout()
fig.savefig(FIG_DIR / "fig4_placebo.pdf")
fig.savefig(FIG_DIR / "fig4_placebo.png")
plt.close()
print(f"  Saved: {FIG_DIR / 'fig4_placebo.pdf'}")


# ═══════════════════════════════════════════════════════════════════════════════
# FIGURE A1: Country-Level Scatter
# ═══════════════════════════════════════════════════════════════════════════════
print("[figA1] Country-level scatter...")

panel_epi_clean = panel.dropna(subset=["epi_score"])
pre = panel_epi_clean[panel_epi_clean["post"] == 0].groupby("iso2_code")["hhi_norm"].mean()
post = panel_epi_clean[panel_epi_clean["post"] == 1].groupby("iso2_code")["hhi_norm"].mean()
epi_country = panel_epi_clean.groupby("iso2_code")["epi_score"].first()

scatter_df = pd.DataFrame({
    "delta_hhi": post - pre,
    "epi_score": epi_country,
}).dropna()

fig, ax = plt.subplots(figsize=(8, 6))
ax.scatter(scatter_df["epi_score"], scatter_df["delta_hhi"],
           alpha=0.6, s=30, color="#2166ac")

# Regression line
if len(scatter_df) > 5:
    z = np.polyfit(scatter_df["epi_score"], scatter_df["delta_hhi"], 1)
    p = np.poly1d(z)
    x_range = np.linspace(scatter_df["epi_score"].min(), scatter_df["epi_score"].max(), 100)
    ax.plot(x_range, p(x_range), color="#b2182b", linewidth=2, linestyle="--",
            label=f"Slope: {z[0]:.5f}")

ax.axhline(y=0, color="grey", linewidth=0.8)
ax.set_xlabel("EF English Proficiency Score")
ax.set_ylabel("Change in HHI (Post - Pre)")
ax.set_title("Figure A1: Pre-Post HHI Change vs English Proficiency")
ax.legend()
plt.tight_layout()
fig.savefig(FIG_DIR / "figA1_scatter.pdf")
fig.savefig(FIG_DIR / "figA1_scatter.png")
plt.close()
print(f"  Saved: {FIG_DIR / 'figA1_scatter.pdf'}")


# ═══════════════════════════════════════════════════════════════════════════════
# FIGURE A2: Distribution of HHI (Pre vs Post)
# ═══════════════════════════════════════════════════════════════════════════════
print("[figA2] HHI distribution...")

fig, ax = plt.subplots(figsize=(8, 5))
pre_hhi = panel[panel["post"] == 0]["hhi_norm"]
post_hhi = panel[panel["post"] == 1]["hhi_norm"]

ax.hist(pre_hhi, bins=40, alpha=0.5, color="#2166ac", label="Pre-ChatGPT", density=True)
ax.hist(post_hhi, bins=40, alpha=0.5, color="#b2182b", label="Post-ChatGPT", density=True)
ax.set_xlabel("HHI (Normalized)")
ax.set_ylabel("Density")
ax.set_title("Figure A2: Distribution of HHI Before and After ChatGPT")
ax.legend()
plt.tight_layout()
fig.savefig(FIG_DIR / "figA2_hhi_distribution.pdf")
fig.savefig(FIG_DIR / "figA2_hhi_distribution.png")
plt.close()
print(f"  Saved: {FIG_DIR / 'figA2_hhi_distribution.pdf'}")


# ═══════════════════════════════════════════════════════════════════════════════
# RESULTS SUMMARY TABLE
# ═══════════════════════════════════════════════════════════════════════════════
print("\n[table] Results summary...")

lines = []
lines.append("# Results Summary\n")

# Table 1: Summary stats
lines.append("## Table 1: Summary Statistics\n")
lines.append("| Variable | Period | Mean | SD | p10 | p50 | p90 | N |")
lines.append("|----------|--------|------|----|-----|-----|-----|---|")
for _, r in summary.iterrows():
    lines.append(f"| {r['variable']} | {r['period']} | {r['mean']:.4f} | "
                 f"{r['std']:.4f} | {r['p10']:.4f} | {r['p50']:.4f} | "
                 f"{r['p90']:.4f} | {int(r['N'])} |")

# Table 2: Main results
lines.append("\n## Table 2: Main Event Study Results\n")
main_hhi = main_results[main_results["outcome"] == "hhi_norm"].iloc[0] if len(main_results[main_results["outcome"] == "hhi_norm"]) > 0 else None
main_ent = main_results[main_results["outcome"] == "entropy"].iloc[0] if len(main_results[main_results["outcome"] == "entropy"]) > 0 else None

if main_hhi is not None:
    lines.append(f"- **HHI**: N={int(main_hhi['n_obs'])}, Countries={int(main_hhi['n_countries'])}, "
                 f"Quarters={int(main_hhi['n_quarters'])}, Within-R2={main_hhi['r2_within']:.4f}")
    lines.append(f"  - Pre-trend F-test p-value: {main_hhi['pretrend_p']:.4f}")
if main_ent is not None:
    lines.append(f"- **Entropy**: N={int(main_ent['n_obs'])}, Countries={int(main_ent['n_countries'])}, "
                 f"Quarters={int(main_ent['n_quarters'])}, Within-R2={main_ent['r2_within']:.4f}")
    lines.append(f"  - Pre-trend F-test p-value: {main_ent['pretrend_p']:.4f}")

# Table 4: Robustness
lines.append("\n## Table 4: Robustness Panel\n")
lines.append("| Specification | Outcome | ATT | SE | p-value | 95% CI | N |")
lines.append("|--------------|---------|-----|----|---------|---------|----|")
for _, r in robustness.iterrows():
    ci = f"[{r['ci_low']:.4f}, {r['ci_high']:.4f}]" if not np.isnan(r.get('ci_low', np.nan)) else "—"
    se = f"{r['se']:.4f}" if not np.isnan(r.get('se', np.nan)) else "—"
    att = f"{r['att']:+.4f}" if not np.isnan(r.get('att', np.nan)) else "—"
    pval = f"{r['pval']:.4f}" if not np.isnan(r.get('pval', np.nan)) else "—"
    n = int(r['n_obs']) if not np.isnan(r.get('n_obs', np.nan)) else "—"
    lines.append(f"| {r['label']} | {r['outcome']} | {att} | {se} | {pval} | {ci} | {n} |")

summary_text = "\n".join(lines)
(TAB_DIR / "results_summary.md").write_text(summary_text, encoding="utf-8")
print(f"  Saved: {TAB_DIR / 'results_summary.md'}")

# Also save to data/clean for pipeline
(CLEAN_DIR / "results_summary.md").write_text(summary_text, encoding="utf-8")


# =====================================================================
# LATEX TABLES (.tex files in paper/tables/)
# =====================================================================
print("\n[tex] Generating LaTeX tables...")

# Table 1: Summary Statistics
tex_summary = r"""\begin{table}[H]
\centering
\caption{Summary Statistics}
\label{tab:summary}
\small
\begin{tabular}{lccccccc}
\toprule
Variable & Period & Mean & SD & p10 & p50 & p90 & N \\
\midrule
"""
for period in ["Full sample", "Pre-treatment", "Post-treatment"]:
    sub = summary[summary["period"] == period]
    for _, r in sub.iterrows():
        vname = r["variable"].replace("_", r"\_")
        tex_summary += (f"{vname} & {period} & {r['mean']:.4f} & {r['std']:.4f} & "
                        f"{r['p10']:.4f} & {r['p50']:.4f} & {r['p90']:.4f} & "
                        f"{int(r['N']):,} \\\\\n")
    tex_summary += r"\midrule" + "\n"

tex_summary += r"""\bottomrule
\end{tabular}
\end{table}
"""
(TAB_DIR / "table1_summary.tex").write_text(tex_summary, encoding="utf-8")
print(f"  Saved: table1_summary.tex")

# Table 4: Robustness
tex_robust = r"""\begin{table}[H]
\centering
\begin{threeparttable}
\caption{Robustness Panel: Post-Treatment ATT Estimates}
\label{tab:robustness}
\small
\begin{tabular}{lcccccc}
\toprule
Specification & \multicolumn{3}{c}{HHI (Normalized)} & \multicolumn{3}{c}{Entropy} \\
\cmidrule(lr){2-4} \cmidrule(lr){5-7}
 & ATT & SE & $p$ & ATT & SE & $p$ \\
\midrule
"""

# Group robustness results by specification (HHI and entropy side by side)
spec_names = []
for _, r in robustness.iterrows():
    base_label = r["label"].split(":")[0].strip()
    if base_label not in spec_names:
        spec_names.append(base_label)

for spec in spec_names:
    rows = robustness[robustness["label"].str.startswith(spec)]
    hhi_row = rows[rows["outcome"].str.contains("hhi", case=False)]
    ent_row = rows[rows["outcome"].str.contains("entropy", case=False)]

    def _fmt(row):
        if row.empty:
            return "--- & --- & ---"
        r = row.iloc[0]
        att = f"${r['att']:+.3f}$" if not np.isnan(r.get("att", np.nan)) else "---"
        se = f"{r['se']:.3f}" if not np.isnan(r.get("se", np.nan)) else "---"
        pval = f"{r['pval']:.3f}" if not np.isnan(r.get("pval", np.nan)) else "---"
        return f"{att} & {se} & {pval}"

    safe_spec = spec.replace("_", r"\_").replace(">=", r"$\geq$")
    tex_robust += f"{safe_spec} & {_fmt(hhi_row)} & {_fmt(ent_row)} \\\\\n"

tex_robust += r"""\bottomrule
\end{tabular}
\begin{tablenotes}
\small
\item \textit{Notes}: Each row reports the post-treatment ATT from a separate regression
with country fixed effects and clustered standard errors at the country level.
\end{tablenotes}
\end{threeparttable}
\end{table}
"""
(TAB_DIR / "table4_robustness.tex").write_text(tex_robust, encoding="utf-8")
print(f"  Saved: table4_robustness.tex")

# Table A1: Event study coefficients
tex_es = r"""\begin{table}[H]
\centering
\caption{Event Study Coefficients}
\label{tab:event_study_coefs}
\small
\begin{tabular}{rcccc}
\toprule
Event Time & \multicolumn{2}{c}{HHI (Normalized)} & \multicolumn{2}{c}{Entropy} \\
\cmidrule(lr){2-3} \cmidrule(lr){4-5}
 & Coef. & SE & Coef. & SE \\
\midrule
"""
hhi_coefs = coefs[coefs["specification"] == "main_hhi_norm"].sort_values("event_time")
ent_coefs = coefs[coefs["specification"] == "main_entropy"].sort_values("event_time")

for _, h in hhi_coefs.iterrows():
    et = int(h["event_time"])
    e_row = ent_coefs[ent_coefs["event_time"] == et]
    h_coef = f"${h['coef']:+.4f}$"
    h_se = f"({h['se']:.4f})" if h["se"] > 0 else "---"
    if not e_row.empty:
        er = e_row.iloc[0]
        e_coef = f"${er['coef']:+.4f}$"
        e_se = f"({er['se']:.4f})" if er["se"] > 0 else "---"
    else:
        e_coef, e_se = "---", "---"
    marker = r" $\leftarrow$ ref" if et == -1 else ""
    tex_es += f"${et:+d}${marker} & {h_coef} & {h_se} & {e_coef} & {e_se} \\\\\n"

tex_es += r"""\bottomrule
\end{tabular}
\end{table}
"""
(TAB_DIR / "tableA1_event_study.tex").write_text(tex_es, encoding="utf-8")
print(f"  Saved: tableA1_event_study.tex")

print(f"\n[03_output] DONE [OK]")
print(f"\nFigures saved to: {FIG_DIR}")
print(f"Tables saved to: {TAB_DIR}")
