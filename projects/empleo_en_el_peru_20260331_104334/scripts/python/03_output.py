"""03_output.py - Tables, figures, and results summary."""

import os
import warnings
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker

warnings.filterwarnings("ignore")

PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
CLEAN_DIR = os.path.join(PROJECT_DIR, "data", "clean")
TABLES_DIR = os.path.join(PROJECT_DIR, "paper", "tables")
FIGURES_DIR = os.path.join(PROJECT_DIR, "paper", "figures")
PAPER_DIR = os.path.join(PROJECT_DIR, "paper")
os.makedirs(TABLES_DIR, exist_ok=True)
os.makedirs(FIGURES_DIR, exist_ok=True)

plt.rcParams.update({"font.size": 11, "figure.dpi": 150, "savefig.dpi": 300, "savefig.bbox": "tight"})

print("=" * 60)
print("03_output.py - Tables, Figures, Summary")
print("=" * 60)

# -- Load --
df = pd.read_csv(os.path.join(CLEAN_DIR, "clean_data.csv"), low_memory=False)
df_emp = df[(df["employed"] == 1) & (df["working_age"] == True)].copy()
for c in ["informal", "telework_low", "telework_score", "female", "rural", "weight", "i524a1", "p208a"]:
    if c in df_emp.columns:
        df_emp[c] = pd.to_numeric(df_emp[c], errors="coerce")

# -- Table 1: Descriptive stats --
print("\n[1/5] Table 1: Descriptive statistics...")
low_tw = df_emp[df_emp["telework_low"] == 1]
high_tw = df_emp[df_emp["telework_low"] == 0]

desc_vars = [("informal", "Informality rate"), ("p208a", "Age"), ("female", "Female"),
             ("rural", "Rural"), ("i524a1", "Monthly income (soles)")]
rows = []
for var, label in desc_vars:
    if var not in df_emp.columns:
        continue
    l_mean = low_tw[var].mean()
    h_mean = high_tw[var].mean()
    rows.append({"Variable": label,
                 "Low-TW Mean": f"{l_mean:.3f}" if l_mean < 10 else f"{l_mean:.0f}",
                 "Low-TW N": f"{low_tw[var].notna().sum():,}",
                 "High-TW Mean": f"{h_mean:.3f}" if h_mean < 10 else f"{h_mean:.0f}",
                 "High-TW N": f"{high_tw[var].notna().sum():,}",
                 "Diff": f"{l_mean - h_mean:.3f}" if abs(l_mean - h_mean) < 10 else f"{l_mean - h_mean:.0f}"})

desc_df = pd.DataFrame(rows)
desc_df.to_csv(os.path.join(TABLES_DIR, "table1_descriptive.csv"), index=False)

latex = "\\begin{table}[htbp]\n\\centering\n"
latex += "\\caption{Descriptive Statistics by Teleworkability}\n\\label{tab:descriptive}\n"
latex += "\\begin{tabular}{lccccc}\n\\toprule\n"
latex += " & \\multicolumn{2}{c}{Contact-Intensive} & \\multicolumn{2}{c}{Teleworkable} & \\\\\n"
latex += "\\cmidrule(lr){2-3} \\cmidrule(lr){4-5}\n"
latex += "Variable & Mean & N & Mean & N & Diff \\\\\n\\midrule\n"
for _, r in desc_df.iterrows():
    latex += f"{r['Variable']} & {r['Low-TW Mean']} & {r['Low-TW N']} & {r['High-TW Mean']} & {r['High-TW N']} & {r['Diff']} \\\\\n"
latex += "\\bottomrule\n\\end{tabular}\n"
latex += "\\begin{tablenotes}\\small\n\\item Notes: Contact-intensive = teleworkability score $<$ 0.20. "
latex += "Teleworkable = score $\\geq$ 0.20. Working-age employed sample (15--65), 2020--2024.\n"
latex += "\\end{tablenotes}\n\\end{table}\n"
with open(os.path.join(TABLES_DIR, "table1_descriptive.tex"), "w") as f:
    f.write(latex)
print("  Saved: table1_descriptive.tex/.csv")

# -- Table 2: Main DiD --
print("\n[2/5] Table 2: Main DiD regression...")
main_path = os.path.join(CLEAN_DIR, "main_event_study.csv")
if os.path.exists(main_path):
    main = pd.read_csv(main_path)
    latex2 = "\\begin{table}[htbp]\n\\centering\n"
    latex2 += "\\caption{DiD Event Study: COVID-19 and Informality by Teleworkability}\n"
    latex2 += "\\label{tab:main_did}\n"
    latex2 += "\\begin{tabular}{lcccc}\n\\toprule\n"
    latex2 += "Year & Year Effect & SE & Interaction (TW$_{low}$) & SE \\\\\n\\midrule\n"
    for _, r in main.iterrows():
        y = int(r["year"])
        if y == 2020:
            latex2 += f"{y} (ref) & 0.000 & --- & 0.000 & --- \\\\\n"
        else:
            stars = ""
            if r["int_pval"] < 0.01: stars = "***"
            elif r["int_pval"] < 0.05: stars = "**"
            elif r["int_pval"] < 0.10: stars = "*"
            latex2 += f"{y} & {r['yr_coef']:.4f} & ({r['yr_se']:.4f}) & {r['int_coef']:.4f}{stars} & ({r['int_se']:.4f}) \\\\\n"
    latex2 += "\\midrule\n"
    latex2 += "Survey weights & \\checkmark & & & \\\\\n"
    latex2 += "SE type & HC1 & & & \\\\\n"
    latex2 += "\\bottomrule\n\\end{tabular}\n"
    latex2 += "\\begin{tablenotes}\\small\n"
    latex2 += "\\item Notes: Pooled WLS DiD. Interaction = differential effect for contact-intensive workers "
    latex2 += "(teleworkability $<$ 0.20) relative to teleworkable workers. "
    latex2 += "*** p$<$0.01, ** p$<$0.05, * p$<$0.10.\n"
    latex2 += "\\end{tablenotes}\n\\end{table}\n"
    with open(os.path.join(TABLES_DIR, "table2_main_did.tex"), "w") as f:
        f.write(latex2)
    print("  Saved: table2_main_did.tex")

# -- Figure 1: Raw trends --
print("\n[3/5] Figure 1: Raw informality trends...")
fig, ax = plt.subplots(figsize=(8, 5))
for val, label, color in [(1, "Contact-intensive (TW < 0.20)", "red"),
                           (0, "Teleworkable (TW >= 0.20)", "blue")]:
    sub = df_emp[df_emp["telework_low"] == val]
    trend = sub.groupby("year")["informal"].mean()
    ax.plot(trend.index, trend.values, marker="o", color=color, label=label, linewidth=2)
ax.axvline(x=2020, color="gray", linestyle="--", alpha=0.5, label="COVID shock")
ax.set_xlabel("Year")
ax.set_ylabel("Informality Rate")
ax.set_title("Figure 1: Raw Informality Trends by Teleworkability")
ax.legend(loc="lower right")
ax.xaxis.set_major_locator(mticker.MaxNLocator(integer=True))
plt.tight_layout()
plt.savefig(os.path.join(FIGURES_DIR, "fig1_raw_trends.png"))
plt.close()
print("  Saved: fig1_raw_trends.png")

# -- Figure 2: DiD event study --
print("\n[4/5] Figure 2: DiD event study...")
if os.path.exists(main_path):
    main = pd.read_csv(main_path)
    fig, ax = plt.subplots(figsize=(8, 5))
    ax.errorbar(main["year"], main["int_coef"], yerr=1.96 * main["int_se"],
                fmt="o-", color="darkred", capsize=4, capthick=1.5,
                label="95% CI", linewidth=2, markersize=8)
    ax.fill_between(main["year"], main["int_coef"] - 1.645 * main["int_se"],
                    main["int_coef"] + 1.645 * main["int_se"],
                    alpha=0.15, color="darkred", label="90% CI")
    ax.axhline(y=0, color="black", linewidth=0.8)
    ax.axvline(x=2020, color="gray", linestyle="--", alpha=0.5, label="Ref year")
    ax.set_xlabel("Year")
    ax.set_ylabel("Differential Informality (contact-intensive vs teleworkable)")
    ax.set_title("Figure 2: DiD Event Study - Interaction Coefficients")
    ax.legend(loc="upper left")
    ax.xaxis.set_major_locator(mticker.MaxNLocator(integer=True))
    plt.tight_layout()
    plt.savefig(os.path.join(FIGURES_DIR, "fig2_event_study.png"))
    plt.close()
    print("  Saved: fig2_event_study.png")

# -- Figure 3: Heterogeneous --
print("\n[5/5] Figure 3: Heterogeneous effects...")
fig, axes = plt.subplots(1, 3, figsize=(16, 5), sharey=True)
het_files = [("het_female.csv", "(a) By Gender", axes[0]),
             ("het_lima.csv", "(b) Lima vs Rest", axes[1]),
             ("het_firmsize.csv", "(c) By Firm Size", axes[2])]

colors = plt.cm.tab10(np.linspace(0, 1, 4))
for fname, title, ax in het_files:
    fpath = os.path.join(CLEAN_DIR, fname)
    if not os.path.exists(fpath):
        ax.set_title(title + " (no data)")
        continue
    het = pd.read_csv(fpath)
    for i, g in enumerate(sorted(het["group"].unique())):
        sub = het[het["group"] == g].sort_values("year")
        ax.errorbar(sub["year"], sub["coef"], yerr=1.96 * sub["se"],
                    fmt="o-", color=colors[i], capsize=3, label=g, linewidth=1.5)
    ax.axhline(y=0, color="black", linewidth=0.8)
    ax.axvline(x=2020, color="gray", linestyle="--", alpha=0.5)
    ax.set_title(title)
    ax.set_xlabel("Year")
    ax.legend(fontsize=8)
    ax.xaxis.set_major_locator(mticker.MaxNLocator(integer=True))
axes[0].set_ylabel("Differential Informality (interaction coef)")
fig.suptitle("Figure 3: Heterogeneous DiD Effects", fontsize=14)
plt.tight_layout()
plt.savefig(os.path.join(FIGURES_DIR, "fig3_heterogeneous.png"))
plt.close()
print("  Saved: fig3_heterogeneous.png")

# -- Results summary --
summary = "# Results Summary\n\n"
summary += "## COVID-19 and Formality Recovery: DiD with Teleworkability (2020-2024)\n\n"

if os.path.exists(main_path):
    main = pd.read_csv(main_path)
    summary += "### Main Finding\n"
    for _, r in main.iterrows():
        if r["year"] == 2020:
            continue
        stars = "***" if r["int_pval"] < 0.01 else "**" if r["int_pval"] < 0.05 else "*" if r["int_pval"] < 0.1 else ""
        summary += f"- {int(r['year'])}: interaction = {r['int_coef']:.4f}{stars} (SE={r['int_se']:.4f})\n"

scar_path = os.path.join(CLEAN_DIR, "scarring_test.csv")
if os.path.exists(scar_path):
    scar = pd.read_csv(scar_path)
    if len(scar) > 0:
        summary += f"\n### Scarring Test\n"
        summary += f"- Wald test (gamma_2024 = gamma_2021): p = {scar.iloc[0]['p_val']:.4f}\n"
        summary += f"- Conclusion: {scar.iloc[0]['conclusion']}\n"

summary += "\n### Tables and Figures\n"
summary += "- Table 1: Descriptive statistics by teleworkability\n"
summary += "- Table 2: Main DiD regression\n"
summary += "- Figure 1: Raw informality trends\n"
summary += "- Figure 2: DiD event study plot\n"
summary += "- Figure 3: Heterogeneous effects\n"

with open(os.path.join(PAPER_DIR, "results_summary.md"), "w") as f:
    f.write(summary)
print("  Saved: results_summary.md")

print("\n" + "=" * 60)
print("[ok] 03_output.py DONE")
print("=" * 60)
