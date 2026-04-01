```json
{
  "score": 58,
  "scripts_run": true,
  "all_outputs_present": false,
  "issues": [
    {
      "severity": "MAJOR",
      "category": "correctness",
      "script": "00_clean.py",
      "description": "P4195 (EPS — private employer supplement) is ORed into `has_sis_i` at line ~34: `df['has_sis_i'] = ((df['P4191'] == '1') | (df['P4195'] == '1'))`. The strategy memo lists P4191=SIS and P4195=EPS as distinct schemes. The stdout reports 'Private/FFAA: 1,781' individuals who are consequently misclassified as SIS beneficiaries, contaminating the primary treatment variable. The `assign_insurance` function then routes these households to 'SIS' rather than 'Private', distorting the core insurance-category distribution.",
      "fix": "Remove P4195 from the SIS indicator: `df['has_sis_i'] = (df['P4191'] == '1').astype(int)`. P4195 should contribute only to `has_private_i`, i.e. `df['has_private_i'] = ((df['P4194'] == '1') | (df['P4193'] == '1') | (df['P4195'] == '1')).astype(int)`.",
      "deduction": -15
    },
    {
      "severity": "MAJOR",
      "category": "rigor",
      "script": "01_main.py",
      "description": "With 44.1% zero-OOP households, the 0.10 and 0.25 quantiles of `oop_share` are identically zero. The stdout confirms this: every coefficient at tau=0.10 and tau=0.25 is printed as exactly `0.0000` with SE `0.0000`. Fitting quantile regression at a mass-point quantile is degenerate — the solution is non-unique and all coefficients collapse to zero. Table 2 (`table2_qr_main.tex`) presents these two all-zero columns without any warning note, which is misleading. This affects the paper's central distributional claim about the lower tail.",
      "fix": "Add a table note: 'tau=0.10 and tau=0.25 coincide with the zero mass point (44% zero OOP); coefficients are degenerate and should not be interpreted. See two-part model results.' Consider restricting the main CQR table to tau ∈ {0.50, 0.75, 0.90} and relegating low-tau inference to the two-part model. A guard like `if np.isclose(q_tau, 0): print(f'  WARNING: tau={tau} at mass point, skipping CQR')` would catch this programmatically.",
      "deduction": -10
    },
    {
      "severity": "MAJOR",
      "category": "rigor",
      "script": "01_main.py",
      "description": "The RIF-OLS (Part 6, lines ~230–260) estimates the kernel density on the **positive-OOP subsample only**: `gaussian_kde(y_rif[y_rif > 0])`. The RIF formula for the tau-quantile requires f(q_tau) from the **full unconditional distribution**. When q_tau = 0 (as it is for tau ≤ 0.25), evaluating a truncated-positive KDE at zero yields a value near the left tail of that truncated distribution, not the density of the full distribution at its point mass. For tau ≥ 0.50 the issue is smaller but still present since the KDE ignores the 44% zero weight.",
      "fix": "Replace `gaussian_kde(y_rif[y_rif > 0])` with `gaussian_kde(y_rif)` using the full sample. For taus where `q_tau == 0`, the RIF value simplifies to `tau - I(y_i <= 0) / f(0+)` evaluated at the right-derivative of the CDF; in practice, skip or annotate those taus rather than propagating a mis-estimated density.",
      "deduction": -10
    },
    {
      "severity": "MINOR",
      "category": "output",
      "script": "03_output.py",
      "description": "`results_summary.md` is written to `TABLE_DIR` (`paper/tables/results_summary.md`) but the automated validator searches in `scripts/` and `data/clean/`. This causes the single HARD validation failure. Additionally, the summary file hardcodes '500 reps' (line ~290: `f'Cluster-bootstrapped SEs (500 reps) at PSU level.'`) while `N_BOOT = 200` in `01_main.py`, misstating the replication count.",
      "fix": "Change the save path to `CLEAN_DIR / 'results_summary.md'`. Replace the hardcoded '500 reps' with an f-string referencing `N_BOOT` (read from `qr_results.csv` metadata, or pass as a constant).",
      "deduction": -5
    },
    {
      "severity": "MINOR",
      "category": "data",
      "script": "00_clean.py",
      "description": "Strategy memo Table 2 is explicitly 'Balance/descriptive table by consumption quintile'. The code produces a balance table grouped by insurance category (`balance_table.tex`) but no balance table by quintile. A quintile-stratified table would let readers assess covariate balance across the income distribution — the paper's central focus.",
      "fix": "Add a block analogous to the insurance balance block, but `groupby('quintile')`. Report weighted means of `age_head`, `female_head`, `educ_years`, `hh_size`, `chronic_any`, `rural`, `zero_oop` for Q1–Q5, with a p-value from an F-test or Kruskal-Wallis across quintiles.",
      "deduction": -5
    },
    {
      "severity": "MINOR",
      "category": "rigor",
      "script": "01_main.py",
      "description": "The Wald test for inter-quantile equality (Part 3, lines ~165–185) computes `se_diff = sqrt(se_lo**2 + se_hi**2)`, treating the two bootstrap estimates as independent. They are not: every bootstrap replication fits both tau_lo and tau_hi on the same resample. Quantile coefficients are positively correlated across taus, so this formula systematically overstates `se_diff` and inflates the p-value, biasing toward failing to reject equality.",
      "fix": "Use the joint bootstrap distribution stored in `boot_coefs_by_tau`: `idx = col_names.index(v); diff_boots = boot_coefs_by_tau[tau_hi][:, idx] - boot_coefs_by_tau[tau_lo][:, idx]; se_diff = np.std(diff_boots[np.isfinite(diff_boots)], ddof=1)`. This correctly accounts for covariance without additional computation.",
      "deduction": -5
    },
    {
      "severity": "MINOR",
      "category": "rigor",
      "script": "01_main.py",
      "description": "The two-part model Part 2 (QR on positive spenders, lines ~290–310) uses built-in Koenker-Bassett sandwich SEs (`mod_pos.bse`, `mod_pos.pvalues`) rather than cluster bootstrap at CONGLOME level, inconsistent with the strategy memo's SE specification and the main QR estimation.",
      "fix": "Run cluster bootstrap on the positive-OOP subsample, resampling PSUs from `df_pos['CONGLOME']`. The existing `_one_boot_all_taus` helper can be reused with `df_pos` data. Report cluster-bootstrapped SEs in the two-part results CSV and table.",
      "deduction": -3
    },
    {
      "severity": "MINOR",
      "category": "code",
      "script": "01_main.py",
      "description": "Bootstrap SEs are silently capped and replaced with NaN at line ~170: `ses_arr[ses_arr > 0.5] = np.nan`. This threshold is arbitrary (a 50 percentage-point SE would only be implausible for an outcome bounded in [0,1] but could be legitimate for region FE in thin strata). With EsSalud cells of N=8 (Q1) and N=14 (Q2), large bootstrap SEs for those interactions are a real signal of unreliability, not noise. Silent NaN replacement causes those cells to show '(--)' in the table without explanation.",
      "fix": "Remove the cap. Instead, flag variables where bootstrap SE > 0.3 in the table notes: 'SE unreliable due to small cell (N < 30).' This makes the limitation transparent rather than hiding it.",
      "deduction": -3
    },
    {
      "severity": "MINOR",
      "category": "data",
      "script": "00_clean.py",
      "description": "EsSalud household counts are very thin in the lower quintiles: Q1=8, Q2=14, Q3=31 (from cell_sizes stdout). The OLS output already shows the consequence: `ins_essalud = +0.2375 (SE=0.2036)` — a 20-percentage-point SE for a variable with only 648 households nationwide. QR interactions `ins_essalud_x_q2` through `ins_essalud_x_q4` are estimated on 14, 31, and 101 observations respectively. No warning is raised and the table presents these estimates without a minimum-cell-size caveat.",
      "fix": "Add a post-aggregation check: `assert (cell_sizes >= 30).all(), 'WARNING: cells below minimum size'`. In the table notes, flag EsSalud × Q1–Q3 cells as unreliable. Consider collapsing EsSalud to a marginal effect (no quintile interaction) given the sparse cells.",
      "deduction": -3
    }
  ],
  "summary": "The pipeline is well-structured, runs end-to-end without errors, implements cluster bootstrap, weighted OLS, a two-part model, RIF-OLS, and comprehensive robustness checks — a solid empirical foundation. However, two MAJOR issues undermine core results: (1) P4195 (EPS, private employer insurance) is incorrectly ORed into the SIS indicator in 00_clean.py, misclassifying ~1,781 individuals as SIS beneficiaries and contaminating the primary treatment variable; and (2) the 44.1% zero-OOP rate means the 0.10 and 0.25 quantiles are identically zero, causing CQR to produce degenerate all-zero coefficients at these taus — which Table 2 presents without any warning, undermining the paper's distributional claims for the lower tail. A third MAJOR rigor issue is that the RIF density is estimated on positive spenders only, biasing unconditional quantile estimates. Additionally, results_summary.md is saved to the wrong directory (causing the hard validation failure), the strategy-specified balance-by-quintile table is missing, Wald tests assume independence across quantile estimates (correctable with existing bootstrap draws), and EsSalud interaction estimates in Q1–Q3 rest on cell sizes of 8–31 households without flagging. Fixing the two variable-construction issues and adding a table note about the zero mass point would be the highest-priority changes."
}
```