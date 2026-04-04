```json
{
  "code_requirements": [
    {
      "category": "estimation",
      "requirement": "Italy synthetic control: implement Abadie (2010) SCM via cvxpy or synth-like optimization minimizing pre-treatment RMSPE on log(unique_pushers). Donor pool = EU27 minus Italy, restricted to countries with full pre-treatment data. Report V-matrix and W-weights.",
      "priority": "MUST"
    },
    {
      "category": "estimation",
      "requirement": "Italy event study: high-frequency (weekly or monthly) TWFE regression of log(unique_pushers) on relative-time dummies centered on ban date (2023-03-31) and separately on lift date (2023-04-28). Must include at least 12 pre-periods to test parallel trends.",
      "priority": "MUST"
    },
    {
      "category": "estimation",
      "requirement": "China/Russia TWFE DiD: two-way FE (country + time) on log(unique_pushers) with treatment = post-ChatGPT-launch (2022-11) × restricted_country dummy. Cluster SEs at country level. Given only 2 treated units, ALSO report wild cluster bootstrap p-values (Roodman et al. 2019) and permutation-based p-values.",
      "priority": "MUST"
    },
    {
      "category": "estimation",
      "requirement": "Synthetic DiD (Arkhangelsky et al. 2021) as the primary estimator for the China/Russia analysis — it is more credible than TWFE when treated units are few and pre-trends may differ. Report sdid point estimate, SE, and 95% CI.",
      "priority": "MUST"
    },
    {
      "category": "estimation",
      "requirement": "Pre-treatment parallel trends test: formal Wald test of joint significance of all pre-treatment interaction dummies in the TWFE event study for both Italy and China/Russia arms. Must report p-value in the main results table.",
      "priority": "MUST"
    },
    {
      "category": "estimation",
      "requirement": "For Italy SCM: in-space placebo tests — run SCM for every country in the donor pool, compute post/pre RMSPE ratio for each, plot rank of Italy. Report exact p-value = rank(Italy) / N_donors.",
      "priority": "MUST"
    },
    {
      "category": "estimation",
      "requirement": "For China/Russia: separate Abadie SCM for each country individually (China alone vs. donor; Russia alone vs. donor) to disaggregate the treatment effect and avoid pooling two structurally very different restrictions.",
      "priority": "MUST"
    },
    {
      "category": "estimation",
      "requirement": "Log-transform outcome: use log(unique_pushers + 1) throughout. Also run IHS transformation as sensitivity. Report both in robustness table.",
      "priority": "MUST"
    },
    {
      "category": "estimation",
      "requirement": "For Russia: include a separate treatment indicator for the Ukraine war onset (2022-02-24). Russia's GitHub activity may be confounded by developer emigration and sanctions. At minimum, drop Russia from the main DiD and report it as a standalone case study or sensitivity.",
      "priority": "MUST"
    },
    {
      "category": "robustness",
      "requirement": "Placebo treatment dates: for Italy SCM, shift ban date by ±1, ±2, ±3 months and re-estimate. True treatment date should produce the largest post/pre RMSPE ratio among all placebo dates.",
      "priority": "MUST"
    },
    {
      "category": "robustness",
      "requirement": "Leave-one-out donor robustness for Italy SCM: drop each donor country one at a time, re-estimate synthetic Italy, and overlay all leave-one-out gaps on the main gap plot.",
      "priority": "MUST"
    },
    {
      "category": "robustness",
      "requirement": "Alternative control group for China/Russia: (a) OECD matched sample; (b) propensity-score matched sample on pre-treatment pushers trend + internet penetration + GDP per capita. Show results are not sensitive to control group construction.",
      "priority": "MUST"
    },
    {
      "category": "robustness",
      "requirement": "COVID robustness: exclude 2020Q1–2021Q1 entirely and re-run all estimators. COVID caused a global spike in GitHub activity that may contaminate pre-treatment trends.",
      "priority": "MUST"
    },
    {
      "category": "robustness",
      "requirement": "Seasonality: include month-of-year fixed effects or deseasonalize the outcome before estimation. GitHub activity has strong annual patterns (December dip, summer slowdown).",
      "priority": "MUST"
    },
    {
      "category": "robustness",
      "requirement": "Population normalization: report results both in levels (log unique_pushers) and normalized by internet users or population. Referee will ask whether effects are driven by population changes (Russia emigration).",
      "priority": "SHOULD"
    },
    {
      "category": "robustness",
      "requirement": "Heterogeneity by language ecosystem: if language-level data available in the 6 columns, split by interpreted (Python/JS) vs. compiled (C/C++/Rust) languages to test whether ChatGPT effects concentrate in AI-assisted scripting languages.",
      "priority": "NICE"
    },
    {
      "category": "robustness",
      "requirement": "For Italy: test whether effect reverses after the ban is lifted (2023-04-28). A credible story requires pushers to rebound post-lift. Absence of reversal weakens the causal narrative.",
      "priority": "MUST"
    },
    {
      "category": "robustness",
      "requirement": "Anticipation effects: for Italy, add a pre-ban window dummy (−2 weeks to ban date) to test whether developers anticipated the ban (e.g., by self-censoring or migrating tools early).",
      "priority": "SHOULD"
    },
    {
      "category": "data_construction",
      "requirement": "Define treatment status precisely and document in code comments: Italy = banned 2023-03-31 through 2023-04-28 (partially treated in those months if aggregated monthly); China = treated from 2022-11-30 onward (ChatGPT never accessible); Russia = treated from 2022-11-30 onward (no official access). These are NOT symmetric — code must handle them separately.",
      "priority": "MUST"
    },
    {
      "category": "data_construction",
      "requirement": "Handle partial treatment periods: if data is monthly and Italy's ban spans parts of two months, create a fractional treatment intensity variable (share of days banned that month) and test sensitivity to how partial months are coded.",
      "priority": "MUST"
    },
    {
      "category": "data_construction",
      "requirement": "Verify balanced panel: check for country-period gaps. Report missingness by country and year. Countries with >10% missing periods should be excluded from SCM donor pool with documentation.",
      "priority": "MUST"
    },
    {
      "category": "data_construction",
      "requirement": "Outlier detection: flag country-periods with log(unique_pushers) more than 3 SD from country-specific mean. Investigate before dropping. Document all exclusions.",
      "priority": "MUST"
    },
    {
      "category": "data_construction",
      "requirement": "Construct a pre-treatment fit quality metric for SCM: compute RMSPE on the pre-treatment window and report it alongside results. If pre-treatment RMSPE > 0.1 log points, the synthetic control fit is poor and the estimator is unreliable.",
      "priority": "MUST"
    },
    {
      "category": "data_construction",
      "requirement": "Time aggregation sensitivity: if underlying data is daily or weekly, run the analysis at both monthly and weekly aggregation levels and confirm directional consistency of estimates.",
      "priority": "SHOULD"
    }
  ],
  "data_warnings": [
    "Russia confound: The Ukraine war (2022-02-24) caused large-scale developer emigration, international platform restrictions (GitHub itself briefly considered blocking Russia), and broad economic disruption — all occurring before the ChatGPT restriction becomes the treatment window. Russia effects are likely unidentified without a clean control for war-related disruption.",
    "China structural difference: China has had a broad internet firewall predating ChatGPT. Its developer population already adapted to VPN/proxy workflows. The 'no ChatGPT access' treatment for China may not bind in the same way as Italy's sudden ban. The parallel trends assumption is implausible if China's GitHub trajectory was already diverging from emerging markets for unrelated reasons.",
    "Italy ban was only 28 days: With monthly data, the treatment window collapses to 1-2 partially treated periods, making point estimates noisy and confidence intervals very wide. Weekly or daily granularity is essentially required for Italy to be informative.",
    "Repeated cross-sections vs. panel: With 161,922 rows and 6 columns, confirm whether this is a true country-time panel (balanced) or pooled cross-sections with varying country coverage over time. SCM requires a balanced pre-treatment panel for the donor pool.",
    "GitHub's own policy changes: In March-April 2023 GitHub introduced AI Copilot expansions and other platform changes that may have independently affected push activity globally — a potential violation of SUTVA for the Italy event study window.",
    "Small-N inference crisis: With 2 persistently treated countries (China, Russia), the asymptotic justification for clustered standard errors completely breaks down. Any t-test or chi-squared test is invalid. Must use exact/permutation inference.",
    "Selection into treatment: China and Russia are not randomly assigned restrictions. They differ from the comparison group on rule-of-law, internet freedom, developer ecosystem maturity, and geopolitics. All DiD estimates for these two countries are at best descriptive upper bounds, not causal.",
    "Definition of 'unique pushers': Confirm whether this counts distinct GitHub accounts or distinct humans. Bot accounts, automated CI pushers, and organization bots can inflate counts in ways that vary by country and time period.",
    "ChatGPT adoption lag: Even in unrestricted countries, ChatGPT adoption was gradual (Nov 2022 to mid-2023). The counterfactual assumes unrestricted countries immediately benefited, but if adoption was slow everywhere, the treatment effect estimate will be biased toward zero.",
    "Data sourced from GitHub public API: GitHub's sampling methodology and API rate limits can introduce non-random missingness, especially for smaller countries and earlier time periods. Document the data source and any known sampling limitations."
  ],
  "tables_required": [
    "Table 1: Summary statistics — N observations, mean/SD/min/max of unique_pushers (raw and log), by treatment group (Italy-pre, Italy-post-ban, Italy-post-lift, China, Russia, control EU, control emerging markets); include pre-treatment period only for trend comparison",
    "Table 2: Main DiD results — Italy SCM ATT (ban period), Italy SCM ATT (post-lift), China TWFE/SDiD ATT, Russia TWFE/SDiD ATT; for each: point estimate, SE, 95% CI, p-value, pre-treatment RMSPE or parallel-trends test p-value",
    "Table 3: Italy event study coefficients — all relative-time dummies (at least t-12 to t+6 relative to ban), SE, 95% CI; separate panel for ban-date event and lift-date event",
    "Table 4: Robustness panel — repeat main estimates under: (a) IHS vs. log transform, (b) exclude COVID period, (c) alternative control group (OECD matched), (d) population-normalized outcome, (e) exclude Russia from China/Russia pool",
    "Table 5: SCM donor weights — list all donor countries for Italy synthetic control with their assigned weights; analogous for China and Russia synthetic controls",
    "Table A1 (Appendix): Balance table — compare pre-treatment means of outcome and any available covariates between treated and control groups for the TWFE analysis; report standardized differences"
  ],
  "figures_required": [
    "Figure 1: Raw trends — time-series of mean log(unique_pushers) for Italy, synthetic Italy, and donor pool average; mark ban date and lift date with vertical lines; separate panel for China/Russia vs. matched emerging markets",
    "Figure 2: SCM gap plot for Italy — difference between actual and synthetic Italy from pre-treatment start through post-ban period; shade the ban window; include 95% bootstrap CI for the gap",
    "Figure 3: Italy event study plot — point estimates and 95% CIs for all relative-time dummies; separate panels for ban event and lift event; horizontal zero line; exclude t=-1 as reference period",
    "Figure 4: In-space placebo distribution for Italy — gap plots for all donor countries overlaid in gray with Italy in bold; include only donors with pre-treatment RMSPE ≤ 2× Italy's pre-treatment RMSPE",
    "Figure 5: Leave-one-out sensitivity for Italy SCM — all LOO gap plots in gray, main SCM gap in bold; visually confirms results are not driven by any single donor country",
    "Figure 6: China and Russia individual SCM gap plots — one panel each, with in-space placebos, marking ChatGPT launch date (2022-11-30) as treatment",
    "Figure A1 (Appendix): Pre-treatment parallel trends visualization — plot country-level trends (normalized to 0 at t=-1) for all treated and control countries over the pre-treatment window",
    "Figure A2 (Appendix): Placebo treatment dates for Italy — plot post/pre RMSPE ratios for ±6 month placebo dates vs. true ban date; true date should be at or near the maximum"
  ]
}
```

**Top 3 threats to publication that the code must address explicitly:**

1. **Russia is not identified** — the Ukraine war is a catastrophic confounder coinciding with the pre-treatment window. Either drop Russia from causal claims or add a war-control specification and present Russia results as descriptive only.

2. **28-day Italy ban + monthly data = near-undetectable signal** — if the raw data is monthly, the code must explicitly test whether the null result (if any) is a power problem, not a zero effect. Report MDE (minimum detectable effect) given your sample.

3. **Permutation inference for China/Russia TWFE** — a t-test with 2 treated units will be rejected at any competent journal. The `synth_did` package's bootstrap or a manual Fisher permutation test is non-negotiable for these estimates.