```json
{
  "code_requirements": [
    {
      "category": "estimation",
      "requirement": "Implement TWFE DiD as the baseline: regress informality_indicator on treatment_intensity × post_covid dummies with individual FE + year FE. Use linearmodels or statsmodels with absorbed FEs. Report Mundlak-style robustness (add individual-level means of time-varying controls).",
      "priority": "MUST"
    },
    {
      "category": "estimation",
      "requirement": "Implement Sun-Abraham (2021) interaction-weighted estimator as the PRIMARY event-study estimator, not TWFE. Use pyfixest's `feols` with `i()` syntax or manually construct cohort×time interactions. This replaces any reference to 'Roth-Sant'Anna' in the proposal.",
      "priority": "MUST"
    },
    {
      "category": "estimation",
      "requirement": "Implement de Chaisemartin & D'Haultfœuille (2020) DIDM estimator as a robustness check on TWFE sign and magnitude. Even if treatment is continuous rather than binary, their decomposition test checks whether TWFE aggregates negative-weighted ATTs.",
      "priority": "MUST"
    },
    {
      "category": "estimation",
      "requirement": "Run Callaway-Sant'Anna (2021) as a second heterogeneity-robust estimator. Define 'first treated cohort' as the first ENAHO wave where a worker's sector drops below median formality. Compare ATT(g,t) estimates against Sun-Abraham — divergence signals treatment effect heterogeneity worth reporting.",
      "priority": "SHOULD"
    },
    {
      "category": "estimation",
      "requirement": "Cluster standard errors at the sector×region level (not individual) since treatment (teleworkability) is assigned at the sector level. Also report two-way clustering at sector + year to bound inference. Use pyfixest or linearmodels cluster options. Never use heteroskedasticity-only SEs.",
      "priority": "MUST"
    },
    {
      "category": "estimation",
      "requirement": "Pre-trend F-test: jointly test all pre-period event-study coefficients = 0 using a Wald test. Separately report Roth (2022) sensitivity: compute the slope of pre-trend that would be needed to explain away the main effect (use the `HonestDiD` approach or manual extrapolation). Do NOT just say 'pre-trends look flat' visually.",
      "priority": "MUST"
    },
    {
      "category": "estimation",
      "requirement": "Heterogeneity subgroup DiD: interact treatment_intensity with indicators for (a) micro-firm (<5 workers), (b) female, (c) Lima vs. rest-of-Peru, (d) youth (18-24). Use fully-interacted TWFE, not separate subgroup regressions, to allow joint significance tests.",
      "priority": "MUST"
    },
    {
      "category": "estimation",
      "requirement": "Stacked DiD as additional robustness: for each year t, stack a 'clean' pre-period dataset against post-period, run within-stack TWFE. This avoids contamination from already-treated units acting as controls in later periods.",
      "priority": "SHOULD"
    },
    {
      "category": "estimation",
      "requirement": "If using a continuous teleworkability score as treatment, split into terciles (low/mid/high contact-intensity) and re-run all event studies. This checks linearity of dose-response and gives referees an intuitive comparison group.",
      "priority": "MUST"
    },
    {
      "category": "robustness",
      "requirement": "Informality definition sensitivity: construct and run ALL THREE INEI-standard informality measures — (1) no contributory social security affiliation, (2) no written labor contract, (3) firm-size proxy (<10 workers). Run the main TWFE specification under each. The coefficients must be reported in a single comparison table.",
      "priority": "MUST"
    },
    {
      "category": "robustness",
      "requirement": "Teleworkability measure sensitivity: use Dingel-Neiman (2020) US scores as the primary measure AND Saltiel (2020) LAC-reweighted scores as a robustness check. Document the CIUO/CNO occupation code crosswalk explicitly — flag any occupation codes that fail to match and show their employment share is <5% of the sample.",
      "priority": "MUST"
    },
    {
      "category": "robustness",
      "requirement": "Balanced vs. unbalanced panel comparison: run all main specifications on (a) the full unbalanced panel and (b) the balanced panel of workers observed in ALL waves. If estimates diverge materially, implement Inverse Probability Weighting (IPW) for attrition using logit-predicted survival probability on pre-COVID observables.",
      "priority": "MUST"
    },
    {
      "category": "robustness",
      "requirement": "Composition effect decomposition: replace the binary informality outcome with a multinomial outcome — (1) formal employment, (2) informal employment, (3) inactivity/unemployment. Run a multinomial logit or three separate LPM regressions. The informality effect may be mechanically attenuated if workers exit to inactivity rather than transitioning to informal jobs.",
      "priority": "MUST"
    },
    {
      "category": "robustness",
      "requirement": "Survey mode robustness: ENAHO switched to telephone/mixed-mode interviewing in 2020 Q2-Q3. Create a flag for phone-interview observations and (a) add it as a control, (b) drop flagged observations and rerun. If coefficients change >20%, treat mode change as a threat to internal validity and say so.",
      "priority": "MUST"
    },
    {
      "category": "robustness",
      "requirement": "Placebo test: re-run the main event study using 2017 or 2018 as a fake 'COVID year' on the pre-COVID subsample. The placebo coefficients must be indistinguishable from zero.",
      "priority": "SHOULD"
    },
    {
      "category": "robustness",
      "requirement": "Exclude Lima Metropolitan Area (stratified separately in ENAHO) and re-run — Lima's labor market has structurally different formality dynamics, and its over-representation in high-telework sectors could be driving the main result.",
      "priority": "SHOULD"
    },
    {
      "category": "data_construction",
      "requirement": "Panel linkage: ENAHO uses a rotating-panel design with a household-individual linking key. Document the exact merge variables used (conglome + vivienda + hogar + codperso). Report the percentage of individuals linked across each wave pair (2019-2020, 2020-2021, etc.). Any linkage rate below 60% for consecutive years must be investigated and reported.",
      "priority": "MUST"
    },
    {
      "category": "data_construction",
      "requirement": "Attrition analysis table: for each survey wave, report N total, N linked to prior wave, % attrited, and a logit regression testing whether attrition predicts baseline (2019) characteristics (informality status, sector, gender, region, education). Include this as a formal appendix table.",
      "priority": "MUST"
    },
    {
      "category": "data_construction",
      "requirement": "Occupation code stability: workers may change occupations between waves. Flag workers who switch 1-digit CIUO categories and test whether (a) excluding them changes results and (b) they are disproportionately in high-contact sectors. This is a composition threat independent of attrition.",
      "priority": "MUST"
    },
    {
      "category": "data_construction",
      "requirement": "ENAHO complex survey design: the dataset has strata, cluster (UPM), and expansion weight variables. All descriptive statistics and means must use survey weights. For regression, use either survey-weighted regression or at minimum cluster at the UPM level and document the choice.",
      "priority": "MUST"
    },
    {
      "category": "data_construction",
      "requirement": "Pre-period extension: load 2017 and 2018 ENAHO waves and append to the panel. This is not optional — without ≥3 pre-COVID years the parallel trends assumption is unverifiable, and referees at journals like JDE, World Development, or Labour Economics will require it.",
      "priority": "MUST"
    },
    {
      "category": "data_construction",
      "requirement": "Sector-level collapse for teleworkability assignment: assign Dingel-Neiman and Saltiel scores at the 3-digit CIUO level (not 1-digit). Aggregate to worker level via crosswalk. Document mean teleworkability score and its standard deviation within each 1-digit sector group for the methods section.",
      "priority": "MUST"
    },
    {
      "category": "data_construction",
      "requirement": "Outlier/top-code check on hours and wages: ENAHO wage distributions have coding errors and extreme outliers. Winsorize wages at 1st and 99th percentiles within year before any analysis. Hours >100/week are likely coding errors — recode or drop and document.",
      "priority": "SHOULD"
    },
    {
      "category": "data_construction",
      "requirement": "Treatment timing: COVID shock hits Peru in Q1 2020 (national emergency declared March 15). If ENAHO waves are quarterly, the 'treatment' is not uniform within 2020. Construct a partial-year treatment intensity variable using the fraction of the survey reference week that fell under mobility restrictions. Otherwise use annual waves only.",
      "priority": "SHOULD"
    },
    {
      "category": "tables_required",
      "requirement": "Table 1 — Descriptive statistics: by high-telework vs. low-telework sector (split at median), report N, mean formality rate, mean age, % female, % Lima, % micro-firm, % with contract, for pre-COVID (2017-2019) and post-COVID (2020-2022) separately.",
      "priority": "MUST"
    },
    {
      "category": "tables_required",
      "requirement": "Table 2 — Panel retention/attrition: rows = survey waves, columns = (N individuals, % retained from baseline, p-value of attrition-on-baseline-informality test, p-value of attrition-on-baseline-sector test). Footnote: IPW weights constructed if attrition is non-random.",
      "priority": "MUST"
    },
    {
      "category": "tables_required",
      "requirement": "Table 3 — Main TWFE results: columns = (1) no controls, (2) baseline controls, (3) with region×year FE, (4) with sector×year FE. Rows = treatment intensity coefficient, N, R², cluster level. This is the horse-race table showing FE choices matter.",
      "priority": "MUST"
    },
    {
      "category": "tables_required",
      "requirement": "Table 4 — Informality definition robustness: same TWFE specification run under all three INEI definitions side-by-side. If all three point estimates are in the same direction and significance, the measurement-choice concern is resolved.",
      "priority": "MUST"
    },
    {
      "category": "tables_required",
      "requirement": "Table 5 — Heterogeneity interactions: single table with triple-interaction coefficients (treatment × post × subgroup) for firm size, gender, and region. Include joint F-test for each interaction group.",
      "priority": "MUST"
    },
    {
      "category": "tables_required",
      "requirement": "Table 6 — Robustness omnibus: rows = specification variants (balanced panel, IPW-weighted, Lima excluded, Saltiel measure, phone-mode flag added, top-coded wages). Columns = point estimate, SE, N. Allows referee to scan all robustness in one place.",
      "priority": "MUST"
    },
    {
      "category": "tables_required",
      "requirement": "Table 7 — Composition decomposition: multinomial/LPM results for transitions to (a) informality, (b) inactivity, (c) unemployment. Shows whether the 'informality effect' is partly displacement to out-of-labor-force.",
      "priority": "MUST"
    },
    {
      "category": "tables_required",
      "requirement": "Appendix Table A1 — Teleworkability crosswalk: list all 3-digit CIUO codes in sample, their assigned Dingel-Neiman score, Saltiel score, and employment share. Flag unmatched codes. Referees will want to verify the crosswalk.",
      "priority": "MUST"
    },
    {
      "category": "figures_required",
      "requirement": "Figure 1 — Event study (TWFE): coefficients for each year relative to 2019 (or last pre-COVID year) with 95% CIs. Normalize t=-1 to zero. Include N per period in a note. Separately plot for high-vs-low teleworkability sectors.",
      "priority": "MUST"
    },
    {
      "category": "figures_required",
      "requirement": "Figure 2 — Sun-Abraham event study: same axes as Figure 1 but using interaction-weighted estimator. Plot TWFE and SA estimates on the same axes with different markers to show divergence (or lack thereof).",
      "priority": "MUST"
    },
    {
      "category": "figures_required",
      "requirement": "Figure 3 — Raw parallel trends: plot mean informality rate over time (2017-2022) separately for high-telework and low-telework sectors. No regression, just weighted means with confidence bands. The visual case for parallel pre-trends.",
      "priority": "MUST"
    },
    {
      "category": "figures_required",
      "requirement": "Figure 4 — Attrition hazard: Kaplan-Meier survival curve showing fraction of 2019 baseline cohort still in panel by survey wave, separately for high-contact vs. low-contact sector workers.",
      "priority": "SHOULD"
    },
    {
      "category": "figures_required",
      "requirement": "Figure 5 — Heterogeneity event studies: 2×2 panel of event-study plots for subgroups (female/male, Lima/non-Lima, micro-firm/larger firm, youth/adult). Each with SA estimator.",
      "priority": "MUST"
    },
    {
      "category": "figures_required",
      "requirement": "Figure 6 — Teleworkability distribution: histogram of sector-level teleworkability scores weighted by pre-COVID employment, separately for Dingel-Neiman and Saltiel measures. Shows Peru's occupation mix relative to the US baseline the index was calibrated on.",
      "priority": "SHOULD"
    },
    {
      "category": "figures_required",
      "requirement": "Figure 7 — Composition flows: stacked area chart showing year-by-year transitions between formal, informal, and inactive/unemployed status for high-contact sector workers. Visualizes the decomposition in Table 7.",
      "priority": "SHOULD"
    }
  ],
  "data_warnings": [
    "ENAHO panel linkage rates drop sharply in 2020 due to COVID survey disruptions — expect 30-50% attrition in the 2019-2020 link. Code must handle this gracefully and not silently drop observations.",
    "The 348,505 × 7,337 wide-panel structure suggests the raw ENAHO is still in its original wide format with one column per variable×wave combination. Reshape to long (individual × year) before any analysis — failure to reshape will produce nonsensical regressions.",
    "ENAHO 2020 used emergency telephone interviewing for urban areas. This introduces a non-classical measurement error in labor market variables (underreporting of informal work on phone vs. in-person) that could bias estimates toward finding more formality loss.",
    "Teleworkability scores are calibrated to US occupational tasks via O*NET. Peru's occupation mix within 3-digit CIUO categories may differ substantially — particularly in agriculture and informal services. The Saltiel (2020) LAC reweighting partially addresses this but document the residual concern.",
    "ENAHO individual identifiers are not perfectly stable — household address changes can break links even when the same individual is re-interviewed. Always validate panel links using demographic consistency checks (age should increment by ~1, gender must not change, education should be non-decreasing).",
    "Informality variables in ENAHO are scattered across modules (employment module, earnings module, social security module). Confirm all three informality definitions draw from the correct module and reference week. Mismatched reference periods between modules are a known ENAHO data quality issue.",
    "The 2017 ENAHO redesigned several occupation code variables — ensure the CIUO crosswalk is consistent across the 2017-2022 period before appending waves.",
    "ENAHO expansion weights change across waves and should not be used for regression without normalization within each wave. Unweighted panel regressions are acceptable if individual FE are included, but this must be stated explicitly.",
    "Peru had multiple overlapping emergency decrees in 2020-2021 with sector-specific exemptions (mining, agriculture). These exemptions create within-sector variation in effective restrictions that the aggregate teleworkability score misses — flag as a limitation.",
    "Firm size reported in ENAHO is self-reported by the worker and may change due to reclassification rather than actual firm changes. Use lagged firm size or baseline (2019) firm size for heterogeneity splits to avoid endogenous subgroup definition."
  ],
  "tables_required": [
    "Table 1: Pre/post descriptive statistics by teleworkability tercile (high/low contact) — formality rate, N, demographics, sector shares",
    "Table 2: Panel retention by wave with attrition-on-baseline-characteristics test (formal logit test, not visual inspection)",
    "Table 3: Main TWFE horse-race across FE specifications (individual+year, +region×year, +sector×year)",
    "Table 4: Informality definition robustness (social security, contract, firm-size) — all three in columns",
    "Table 5: Heterogeneity triple-interactions (treatment×post×subgroup) for gender, region, firm size, age",
    "Table 6: Omnibus robustness table — balanced panel, IPW, Lima-excluded, Saltiel measure, survey mode control",
    "Table 7: Composition decomposition — LPM for informality, inactivity, and unemployment as separate outcomes",
    "Appendix A1: Full teleworkability crosswalk with CIUO codes, DN score, Saltiel score, employment share",
    "Appendix A2: Placebo test results (fake 2018 COVID year on pre-COVID sample)"
  ],
  "figures_required": [
    "Figure 1: TWFE event study with pre-trend Wald F-test statistic reported in figure note",
    "Figure 2: Sun-Abraham (2021) event study overlaid with TWFE estimates for direct comparison",
    "Figure 3: Raw (regression-free) parallel trends — mean informality by high/low telework sector, 2017-2022",
    "Figure 4: Kaplan-Meier panel survival curve by high/low contact sector (attrition visualization)",
    "Figure 5: Heterogeneity event studies — 2×2 panel for gender, region, firm size, age subgroups",
    "Figure 6: Teleworkability score distribution — histogram weighted by employment, DN vs Saltiel overlay",
    "Figure 7: Composition flow diagram — formal/informal/inactive shares over time for high-contact workers"
  ]
}
```

---

**Key judgment calls embedded in this checklist:**

- **Sun-Abraham is MUST, not SHOULD** — with a staggered or continuous treatment and potential heterogeneous effects across Peru's diverse labor market, TWFE alone will not clear peer review at JDE/World Development tier journals.
- **Composition decomposition is MUST** — Peru's labor market has documented employment-inactivity margins that dwarf formal-informal margins during recessions (Herrera & Rosas type findings). Ignoring inactivity conflates the mechanism.
- **Survey mode flag is MUST** — the 2020 ENAHO phone-mode change is a well-known data quality issue that referees familiar with Peru data will immediately raise. Silence on this is a rejection risk.
- **Saltiel (2020) crosswalk is MUST** — using US O*NET scores unadjusted for Latin American task content is the most credible measurement-error threat; the LAC-adjusted version should be primary, not a robustness check.