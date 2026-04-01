"""03_output.py - Publication-quality figures and LaTeX tables."""

import numpy as np
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from pathlib import Path

np.random.seed(42)

PROJECT = Path(r"C:\Users\jesus\Documents\paper-HQ-sin API\projects\data_first_20260401_124533")
DATA_CLEAN = PROJECT / "data" / "clean"
FIGURES = PROJECT / "paper" / "figures"
TABLES = PROJECT / "paper" / "tables"
FIGURES.mkdir(parents=True, exist_ok=True)
TABLES.mkdir(parents=True, exist_ok=True)

LIBERTY_LABELS = {"freexp": "Expression", "freass": "Assembly", "frerel": "Religion",
                  "fremov": "Movement", "fairtrial": "Fair Trial"}
COLORS = {"bust": "#C0392B", "recovery": "#27AE60"}

plt.rcParams.update({"font.family": "serif", "font.size": 11, "figure.dpi": 150})

print("=" * 70)
print("03_output.py - Tables and Figures")
print("=" * 70)

# ══════════════════════════════════════════════════════════════════════════════
# 1. ASYMMETRIC EVENT STUDY PLOT (main figure)
# ══════════════════════════════════════════════════════════════════════════════
print("\n[1] Asymmetric event study plot...")
es_file = DATA_CLEAN / "event_study_coefficients.csv"
if es_file.exists():
    es = pd.read_csv(es_file)
    liberties = es["liberty"].unique()

    fig, axes = plt.subplots(2, 3, figsize=(14, 9), sharey=False)
    axes = axes.flatten()

    for i, lib in enumerate(liberties):
        ax = axes[i]
        for phase, color, marker in [("bust", COLORS["bust"], "o"), ("recovery", COLORS["recovery"], "s")]:
            data = es[(es["liberty"] == lib) & (es["phase"] == phase)].sort_values("rel_time")
            if len(data) > 0:
                ax.errorbar(data["rel_time"], data["coef"],
                            yerr=[data["coef"] - data["ci_lower"], data["ci_upper"] - data["coef"]],
                            fmt=marker, color=color, capsize=2, capthick=1, linewidth=1.2,
                            markersize=4, label=phase.title(), alpha=0.85)
        ax.axhline(0, color="gray", linewidth=0.7)
        ax.axvline(-0.5, color="gray", linestyle="--", linewidth=0.7, alpha=0.5)
        ax.set_title(LIBERTY_LABELS.get(lib, lib), fontsize=12)
        ax.set_xlabel("Years from episode onset")
        if i % 3 == 0:
            ax.set_ylabel("Coefficient")
        ax.legend(fontsize=8, loc="lower left")
        ax.grid(axis="y", alpha=0.2)

    # Hide unused subplot
    if len(liberties) < 6:
        axes[-1].set_visible(False)

    fig.suptitle("Asymmetric Event Study: Commodity Busts vs. Recoveries", fontsize=14, y=1.01)
    fig.tight_layout()
    fig.savefig(FIGURES / "fig1_asymmetric_event_study.pdf", bbox_inches="tight")
    plt.close("all")
    print(f"    Saved fig1_asymmetric_event_study.pdf")

# ══════════════════════════════════════════════════════════════════════════════
# 2. SYMMETRY TEST BAR CHART
# ══════════════════════════════════════════════════════════════════════════════
print("\n[2] Symmetry test chart...")
sym_file = DATA_CLEAN / "symmetry_test.csv"
if sym_file.exists():
    sym = pd.read_csv(sym_file)

    fig, ax = plt.subplots(figsize=(8, 5))
    x = np.arange(len(sym))
    w = 0.35
    ax.bar(x - w/2, sym["bust_avg"], w, color=COLORS["bust"], label="Bust effect", alpha=0.85)
    ax.bar(x + w/2, sym["recovery_avg"], w, color=COLORS["recovery"], label="Recovery effect", alpha=0.85)

    # Add significance stars
    for i, (_, row) in enumerate(sym.iterrows()):
        if row["p_symmetry"] < 0.05:
            y_max = max(abs(row["bust_avg"]), abs(row["recovery_avg"])) + 0.02
            ax.annotate("**", xy=(i, y_max), ha="center", fontsize=12, color="red")
        elif row["p_symmetry"] < 0.1:
            y_max = max(abs(row["bust_avg"]), abs(row["recovery_avg"])) + 0.02
            ax.annotate("*", xy=(i, y_max), ha="center", fontsize=12, color="red")

    ax.set_xticks(x)
    ax.set_xticklabels([LIBERTY_LABELS.get(l, l) for l in sym["liberty"]], rotation=30)
    ax.axhline(0, color="gray", linewidth=0.7)
    ax.set_ylabel("Average post-episode coefficient")
    ax.set_title("Bust vs. Recovery: Testing the Ratchet Hypothesis")
    ax.legend()
    ax.grid(axis="y", alpha=0.2)
    fig.tight_layout()
    fig.savefig(FIGURES / "fig2_symmetry_test.pdf", bbox_inches="tight")
    plt.close("all")
    print(f"    Saved fig2_symmetry_test.pdf")

# ══════════════════════════════════════════════════════════════════════════════
# 3. MAIN RESULTS TABLE
# ══════════════════════════════════════════════════════════════════════════════
print("\n[3] Main results table...")
main_file = DATA_CLEAN / "main_results.csv"
if main_file.exists():
    results = pd.read_csv(main_file)
    lines = [
        r"\begin{table}[htbp]", r"\centering",
        r"\caption{TWFE Estimates: Effect of Commodity Busts on Civil Liberties}",
        r"\label{tab:main}", r"\begin{tabular}{lcccc}", r"\toprule",
        r"Civil Liberty & Coefficient & SE & p-value & N \\", r"\midrule",
    ]
    for _, r in results.iterrows():
        name = LIBERTY_LABELS.get(r["liberty"], r["liberty"])
        stars = "***" if r["pvalue"] < 0.01 else "**" if r["pvalue"] < 0.05 else "*" if r["pvalue"] < 0.1 else ""
        lines.append(f"  {name} & {r['coef']:.4f}{stars} & ({r['se']:.4f}) & {r['pvalue']:.3f} & {int(r['n']):,} \\\\")
    lines.extend([
        r"\midrule",
        r"\multicolumn{5}{l}{\footnotesize Country and year FE. Cluster-robust SEs.} \\",
        r"\multicolumn{5}{l}{\footnotesize $^{***}p<0.01$, $^{**}p<0.05$, $^{*}p<0.1$} \\",
        r"\bottomrule", r"\end{tabular}", r"\end{table}",
    ])
    with open(TABLES / "tab1_main_results.tex", "w") as f:
        f.write("\n".join(lines))
    print(f"    Saved tab1_main_results.tex")

# ══════════════════════════════════════════════════════════════════════════════
# 4. SYMMETRY TEST TABLE
# ══════════════════════════════════════════════════════════════════════════════
print("\n[4] Symmetry test table...")
if sym_file.exists():
    sym = pd.read_csv(sym_file)
    lines = [
        r"\begin{table}[htbp]", r"\centering",
        r"\caption{Ratchet Test: Symmetry of Bust and Recovery Effects}",
        r"\label{tab:symmetry}", r"\begin{tabular}{lccccc}", r"\toprule",
        r"Liberty & Bust avg. & Recovery avg. & Asymmetry & z-stat & p(symmetry) \\", r"\midrule",
    ]
    for _, r in sym.iterrows():
        name = LIBERTY_LABELS.get(r["liberty"], r["liberty"])
        ratchet = r"\checkmark" if r["ratchet"] == "YES" else ""
        lines.append(f"  {name} & {r['bust_avg']:.4f} & {r['recovery_avg']:.4f} & "
                     f"{r['asymmetry']:.4f} & {r['z_stat']:.3f} & {r['p_symmetry']:.3f} \\\\")
    lines.extend([
        r"\midrule",
        r"\multicolumn{6}{l}{\footnotesize H$_0$: bust effect $=$ $-$recovery effect (symmetry).} \\",
        r"\bottomrule", r"\end{tabular}", r"\end{table}",
    ])
    with open(TABLES / "tab2_symmetry.tex", "w") as f:
        f.write("\n".join(lines))
    print(f"    Saved tab2_symmetry.tex")

# ══════════════════════════════════════════════════════════════════════════════
# 5. SUMMARY STATS TABLE
# ══════════════════════════════════════════════════════════════════════════════
print("\n[5] Summary statistics table...")
summ_file = DATA_CLEAN / "summary_stats.csv"
if summ_file.exists():
    summ = pd.read_csv(summ_file, index_col=0)
    lines = [
        r"\begin{table}[htbp]", r"\centering", r"\caption{Summary Statistics}",
        r"\label{tab:summary}", r"\begin{tabular}{lccccc}", r"\toprule",
        r"Variable & Mean & SD & Min & Max & N \\", r"\midrule",
    ]
    for var in summ.index:
        name = LIBERTY_LABELS.get(var, var.replace("_", " ").title())[:25]
        r = summ.loc[var]
        lines.append(f"  {name} & {r['mean']:.2f} & {r['std']:.2f} & {r['min']:.1f} & {r['max']:.1f} & {int(r['count']):,} \\\\")
    lines.extend([r"\bottomrule", r"\end{tabular}", r"\end{table}"])
    with open(TABLES / "tab3_summary.tex", "w") as f:
        f.write("\n".join(lines))
    print(f"    Saved tab3_summary.tex")

print("\n" + "=" * 70)
print("03_output.py completed successfully")
print("=" * 70)
