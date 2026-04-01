```json
{
  "code_requirements": [
    {
      "category": "estimation",
      "requirement": "Baseline TWFE: regress civil-liberties index on country FE, year FE, and separate indicators/continuous measures for bust and recovery phases. Compute clustered SE at the country level (not the country-year level) to account for within-country serial correlation in both the outcome and the treatment.",
      "priority": "MUST"
    },
    {
      "category": "estimation",
      "requirement": "Asymmetric specification: interact price-change measure with a bust dummy and a recovery dummy so each phase gets its own coefficient. The ratchet hypothesis predicts bust_coef < 0 and recovery_coef ≈ 0 (or abs(recovery_coef) << abs(bust_coef)).",
      "priority": "MUST"
    },
    {
      "category": "estimation",
      "requirement": "Joint symmetry Wald/F-test: H0: bust_coef + recovery_coef = 0. Report p-value and 95% CI for the difference. This is the paper's headline test — fail to include it and the paper is desk-rejected.",
      "priority": "MUST"
    },
    {
      "category": "estimation",
      "requirement": "Event-study plots for both bust and recovery phases: estimate leads (t-3 to t-1) and lags (t+1 to t+5 or end-of-episode) separately and plot coefficients with 95% CI bands. Pre-trend coefficients must be jointly insignificant (pre-trends F-test reported).",
      "priority": "MUST"
    },
    {
      "category": "estimation",
      "requirement": "Staggered-treatment robustness: run Callaway-Sant'Anna (2021) or Sun-Abraham (2021) estimator because episodes begin in different years across countries. Standard TWFE with staggered timing can produce sign-reversed estimates if treatment effects are heterogeneous. Report both TWFE and the heterogeneity-robust estimator side-by-side.",
      "priority": "MUST"
    },
    {
      "category": "estimation",
      "requirement": "Bacon-Goodman decomposition: quantify what fraction of the TWFE estimate comes from 'already-treated vs. not-yet-treated', 'treated vs. never-treated', and 'treated vs. timing' comparisons. Flag if the negative-weighting share exceeds 10%.",
      "priority": "MUST"
    },
    {
      "category": "estimation",
      "requirement": "Wild cluster bootstrap p-values (Cameron-Gelbach-Miller or Roodman boottest): necessary if the number of unique country clusters is < 50. With 9 292 rows and 11 columns the panel is likely ~100-200 countries x ~30-50 years, so cluster count may be borderline. Compute both asymptotic and WCB p-values and report both.",
      "priority": "MUST"
    },
    {
      "category": "estimation",
      "requirement": "Continuous treatment variant: replace binary bust/recovery indicators with the signed log-change in the commodity price index to test dose-response and avoid threshold-sensitivity bias.",
      "priority": "SHOULD"
    },
    {
      "category": "estimation",
      "requirement": "Ordered-outcome robustness: if the civil-liberties index is ordinal (e.g., Freedom House 1-7 or V-Dem 0-1 bounded), run an ordered logit / beta regression alongside OLS-FE and verify sign/significance are preserved.",
      "priority": "SHOULD"
    },
    {
      "category": "estimation",
      "requirement": "Heterogeneous treatment effects by initial repression level: split sample into 'already authoritarian' vs. 'hybrid/democratic' at episode onset and interact bust/recovery dummies with regime type. The ratchet should be stronger where institutions are weaker.",
      "priority": "SHOULD"
    },
    {
      "category": "estimation",
      "requirement": "Placebo commodity assignment: randomly reassign commodity-exposure labels across countries 1 000 times and re-estimate; the true estimate should lie outside the 95th percentile of the placebo distribution.",
      "priority": "SHOULD"
    },
    {
      "category": "estimation",
      "requirement": "Time-varying controls inclusion: add GDP per capita growth, conflict incidence (UCDP), trade openness, and political polity score as controls. Verify that adding controls does not substantially change the bust/recovery coefficients (coefficient stability is an identification argument here).",
      "priority": "SHOULD"
    },
    {
      "category": "estimation",
      "requirement": "Linear time trends by country: augment the baseline TWFE with country-specific linear trends to absorb slow-moving country divergence that could confound price shocks.",
      "priority": "SHOULD"
    },
    {
      "category": "estimation",
      "requirement": "Multiple-episode handling: countries may experience more than one bust-recovery cycle. Code must decide explicitly — and justify — whether to (a) use the first episode only, (b) use all episodes with a 'clean window' restriction, or (c) include episode FE. The decision materially affects sample size and interpretation.",
      "priority": "MUST"
    },
    {
      "category": "estimation",
      "requirement": "Conley spatial standard errors: commodity price shocks are correlated across commodity-linked neighbors. If geography data are available, add Conley (1999) SE as a robustness check on the clustered-SE results.",
      "priority": "NICE"
    },
    {
      "category": "data_construction",
      "requirement": "Episode-definition transparency: document the exact algorithm for classifying bust vs. recovery. Specify: (1) price decline threshold (e.g., ≥15% peak-to-trough), (2) minimum episode length, (3) recovery completion criterion (return to pre-bust price level vs. price-change sign flip). Sensitivity analysis over threshold values ±5 pp is required.",
      "priority": "MUST"
    },
    {
      "category": "data_construction",
      "requirement": "Country-commodity exposure weights: if exposure is constructed (e.g., export share × commodity price), document the base year and source. Verify no look-ahead bias — exposure weights must be predetermined relative to price shocks.",
      "priority": "MUST"
    },
    {
      "category": "data_construction",
      "requirement": "Balanced vs. unbalanced panel declaration: explicitly test and report whether the panel is balanced. If unbalanced, check whether attrition is correlated with pre-period civil-liberties trends (attrition-on-outcome bias).",
      "priority": "MUST"
    },
    {
      "category": "data_construction",
      "requirement": "Outcome variable source and interpolation: name the exact dataset (Freedom House Political Rights/Civil Liberties, V-Dem Liberal Democracy Index, CIRI, etc.). If any years are interpolated, flag them and exclude interpolated observations from the main sample; use them only in robustness.",
      "priority": "MUST"
    },
    {
      "category": "data_construction",
      "requirement": "Overlapping episode guard: if a recovery episode begins before the prior bust window closes (episode contamination), the code must detect and resolve this — either by truncating windows or dropping the observation from both samples.",
      "priority": "MUST"
    },
    {
      "category": "data_construction",
      "requirement": "Global price trend partialling: if the commodity price index includes a global demand component correlated with global democratization waves (e.g., 1989-1991, post-GFC), the year fixed effects may not fully absorb this. Consider region-by-year FE or a global factor control.",
      "priority": "SHOULD"
    },
    {
      "category": "robustness",
      "requirement": "Alternative civil-liberties measures: if main spec uses Freedom House, replicate with V-Dem Physical Integrity Index and CIRI Empowerment Rights Index. Show that the asymmetry is not measure-specific.",
      "priority": "MUST"
    },
    {
      "category": "robustness",
      "requirement": "Subsample by commodity type: oil/gas exporters may respond differently from agricultural or mineral exporters due to revenue fungibility and Dutch disease. Report results separately for fuel vs. non-fuel commodity exporters.",
      "priority": "SHOULD"
    },
    {
      "category": "robustness",
      "requirement": "Excluding top commodity-revenue countries: some resource-rich states (e.g., Gulf monarchies) are permanent autocracies where the civil-liberties floor is already at the minimum — the ratchet cannot operate below the floor. Exclude countries where the civil-liberties index is at its floor value for >75% of the sample.",
      "priority": "SHOULD"
    },
    {
      "category": "robustness",
      "requirement": "Varying event window lengths: run the event study with windows of ±3, ±5, and ±7 years around each episode. Show that point estimates and the symmetry test conclusion are stable.",
      "priority": "SHOULD"
    },
    {
      "category": "robustness",
      "requirement": "Drop one-region-at-a-time jackknife: rerun the main specification excluding each of the 6-7 world regions in turn. Ensures results are not driven by one region (e.g., Sub-Saharan Africa or MENA).",
      "priority": "SHOULD"
    }
  ],
  "data_warnings": [
    "FLOOR/CEILING CENSORING: Civil-liberties indices are bounded. Countries at the maximum-repression floor during a bust cannot worsen further — this mechanically suppresses the bust coefficient and biases toward finding symmetry (null ratchet). Flag and separately analyze floor-censored observations.",
    "EPISODE LENGTH IMBALANCE: Busts and recoveries may differ systematically in duration. If recoveries are always shorter (left-censored by sample end), the event study lags for recovery will have smaller N and wider CIs, making asymmetry appear even when none exists. Document average episode lengths for both phases.",
    "UNIT-OF-OBSERVATION AMBIGUITY: With 9 292 rows and 11 columns, the panel could be ~200 countries × 46 years or ~100 countries × 93 years. The cluster count radically changes inference strategy. Confirm N_countries before finalizing SE approach.",
    "STAGGERED TIMING NEGATIVE WEIGHTS: TWFE with staggered bust/recovery onset can assign negative weights to early-treated units in later periods, potentially reversing the sign of the true ATT. The Bacon decomposition is diagnostic — if negative-weight share is large, the Callaway-Sant'Anna estimate supersedes TWFE as the headline result.",
    "COMMODITY INDEX CONSTRUCTION ENDOGENEITY: If the commodity price index uses current-year export shares as weights, price shocks and exposure are jointly determined. Use lagged (t-5 or earlier) export shares to construct exposure weights.",
    "GLOBAL CONFOUNDERS: The 2008-09 commodity bust coincides with the Global Financial Crisis; the 2014-16 oil bust coincides with democratic backsliding in MENA and Latin America. Year FE absorb global trends but not differential regional exposure. Region-by-year FE or explicit GFC/post-GFC controls may be necessary.",
    "SELECTIVE RECOVERY DEFINITION: If recovery is defined as price returning to pre-bust levels, countries that never recover are dropped from the recovery sample. This is survivorship bias — repressive states may be precisely those where prices (and liberties) never recover. Keep non-recovering bust episodes in a separate 'no-recovery' category and compare their trajectory.",
    "CIVIL-LIBERTIES INDEX REVISIONS: Freedom House and V-Dem retroactively revise historical scores. Specify the exact vintage/download date of the data so results are replicable.",
    "MEASUREMENT LAG: Civil-liberties assessments are often published with a one-year lag relative to the reference year. Verify whether the index year refers to the assessment year or the reference year and align accordingly with price data.",
    "SERIAL CORRELATION IN OUTCOME: Civil liberties exhibit very high AR(1) persistence (~0.95). Standard errors that do not account for this will be too small. Clustered SE at the country level partially addresses this, but verify residual autocorrelation in the FE residuals and consider AR-robust inference if needed."
  ],
  "tables_required": [
    "Table 1 — Summary Statistics: N, mean, SD, min, max for civil-liberties index, commodity price index, bust indicator, recovery indicator, and all controls. Stratified by bust/recovery/tranquil periods.",
    "Table 2 — Episode Inventory: count of bust and recovery episodes by region and decade; mean episode duration; fraction of country-years in each phase. This is descriptive but essential for external validity.",
    "Table 3 — Main TWFE Results: four columns — (1) bust only, (2) recovery only, (3) bust + recovery joint, (4) bust + recovery + controls. Report country FE, year FE, clustered SE, R², N for each. Bottom rows: symmetry Wald test statistic and p-value.",
    "Table 4 — Bacon Decomposition: weighted average TWFE contribution by comparison type ('early vs. late treated', 'treated vs. never-treated', 'treated vs. not-yet-treated'). One row per type, flagging negative-weight groups.",
    "Table 5 — Heterogeneity by Regime Type: split columns by initial regime (Polity2 < 0 vs. ≥ 0 or autocracy/anocracy/democracy). Bust and recovery coefficients and symmetry test for each subgroup.",
    "Table 6 — Robustness Panel: rows = specifications (alternative outcomes, continuous treatment, country trends, region-by-year FE, ordered logit, WCB p-values, Conley SE); columns = bust coefficient, recovery coefficient, symmetry p-value. Compact format for referee scanning.",
    "Table A1 (Appendix) — Pre-Trends F-Test: joint F-statistic and p-value for leads t-3, t-2, t-1 in both bust and recovery event studies.",
    "Table A2 (Appendix) — Callaway-Sant'Anna / Sun-Abraham estimates alongside TWFE for the main specification."
  ],
  "figures_required": [
    "Figure 1 — Commodity Price Index Over Time: global or country-weighted average price index with bust and recovery episodes shaded. Motivates the empirical variation.",
    "Figure 2 — Civil Liberties Distribution by Episode Phase: kernel density or violin plots of the civil-liberties index level in pre-bust, bust, and recovery periods across countries. Shows the raw pattern before any regression.",
    "Figure 3 — Event Study: Bust Phase: point estimates and 95% CI for t-3 through t+5 (relative to bust onset), normalized to t-1 = 0. Pre-trend coefficients should be near zero; post-onset coefficients should decline.",
    "Figure 4 — Event Study: Recovery Phase: same structure for recovery onset. The key visual — if recovery coefficients do NOT mirror Figure 3's decline (i.e., they stay flat or rise slowly), that is the ratchet in picture form.",
    "Figure 5 — Symmetry Test Visual: coefficient plot showing bust coefficient (with CI) and recovery coefficient (with CI) on the same axis, plus the difference and its CI. Referee-friendly presentation of the Wald test.",
    "Figure 6 — Heterogeneity Heatmap or Coefficient Plot: bust and recovery coefficients by region or regime type, showing whether the ratchet is universal or concentrated in specific contexts.",
    "Figure A1 (Appendix) — Geographic Map of Episode Incidence: countries colored by number of bust episodes experienced. Helps referee assess geographic clustering.",
    "Figure A2 (Appendix) — Bacon Decomposition Visualization: scatter plot of comparison-group TWFE estimates (x-axis: weight, y-axis: estimate) by comparison type, following Goodman-Bacon (2021) standard presentation."
  ]
}
```

**Critical judgment calls the code must make explicit:**

1. **The ratchet is testable only where recovery actually occurs.** If you define the sample as "countries that experienced a bust," the recovery sample is a selected subset. The paper must either (a) use the full bust sample and code non-recovery as a zero-change recovery, or (b) explicitly acknowledge the selection and bound the estimand.

2. **Asymmetry vs. level-shift vs. persistence.** The ratchet story implies the *level* of repression does not return — not just that the *rate of change* is asymmetric. The event study must show *levels* (normalized to pre-bust baseline), not just marginal changes.

3. **The symmetry test is necessary but not sufficient.** Symmetric coefficients of bust = +0.1 and recovery = -0.1 would pass the symmetry test but still show a net positive effect if the bust lasted 5 years and recovery only 2. Report cumulative impulse-response magnitudes alongside the point estimates.