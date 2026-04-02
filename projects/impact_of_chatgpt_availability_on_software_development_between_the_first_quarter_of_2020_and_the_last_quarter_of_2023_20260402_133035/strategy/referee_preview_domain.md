```json
{
  "code_requirements": [
    {
      "category": "estimation",
      "requirement": "Implement a two-way fixed effects distributed lag model: outcome_ct = alpha_c + gamma_t + sum_{k=-K}^{K} beta_k * D_{t=event+k} + epsilon_ct, where the outcome is country-quarter HHI and Shannon entropy separately. Normalize beta_{-1} = 0 (omit one pre-period). Use K >= 4 leads and lags given the quarterly data.",
      "priority": "MUST"
    },
    {
      "category": "estimation",
      "requirement": "Cluster standard errors at the country level (the level at which treatment variation is absorbed by FEs). With ~100-200 countries this is marginal for cluster-robust SEs — report the country count and flag if <50 clusters, in which case wild cluster bootstrap (boottest) must be used instead.",
      "priority": "MUST"
    },
    {
      "category": "estimation",
      "requirement": "Since ChatGPT launched globally at a single date (not staggered), this is an interrupted time series with country FEs, NOT a staggered DiD. Frame and code it accordingly. Do NOT use Callaway-Sant'Anna or Sun-Abraham estimators (which require staggered timing). Instead use a single-breakpoint event study centered on Q1 2023 (or Q4 2022 if usage-based).",
      "priority": "MUST"
    },
    {
      "category": "estimation",
      "requirement": "Report a formal pre-trend test: joint F-test (or chi-squared) of all lead coefficients beta_{-K}...beta_{-2} = 0. Report the p-value in every main table.",
      "priority": "MUST"
    },
    {
      "category": "estimation",
      "requirement": "Run the heterogeneity analysis as an interaction model: include English_proficiency_c × post_t and English_proficiency_c × event_leads_lags_kt terms. Use a continuous EF index (e.g., EF Score) AND a binary high/low split for interpretability. Report both.",
      "priority": "MUST"
    },
    {
      "category": "estimation",
      "requirement": "Run all models on both HHI and Shannon entropy as dependent variables. If results diverge, provide an economic explanation — HHI is top-heavy (dominant languages), entropy is full-distribution. Divergence is a finding, not a bug.",
      "priority": "MUST"
    },
    {
      "category": "estimation",
      "requirement": "Construct the country-quarter panel BEFORE running regressions: aggregate raw language-level rows to country×quarter cells. Verify the final panel is balanced or document which country×quarters are missing and why. Report N_countries, N_quarters, and total N in every table header.",
      "priority": "MUST"
    },
    {
      "category": "robustness",
      "requirement": "Placebo test: shift the event date by +4 quarters (treat Q1 2024 as the event) and re-run the main specification. Should yield null results. Also run with -4 quarters (Q1 2022). Include a figure or table comparing placebo vs. true estimates.",
      "priority": "MUST"
    },
    {
      "category": "robustness",
      "requirement": "Alternative treatment timing: run separately treating the event as Q4 2022 (launch), Q1 2023 (mass adoption), and Q2 2023 (plugin/API proliferation). Check stability of post-period estimates.",
      "priority": "MUST"
    },
    {
      "category": "robustness",
      "requirement": "Trim or winsorize HHI and entropy at the 1st/99th percentile before running regressions. Report results with and without trimming. Small-language-count countries will have mechanically high HHI variance.",
      "priority": "MUST"
    },
    {
      "category": "robustness",
      "requirement": "Re-run excluding countries with fewer than a minimum language threshold (e.g., <3 languages observed in the panel). Report the N drop and coefficient stability.",
      "priority": "MUST"
    },
    {
      "category": "robustness",
      "requirement": "Add a linear country-specific time trend (country × time) to the TWFE specification to absorb differential pre-existing trends. If coefficients change substantially, the parallel trends assumption is suspect.",
      "priority": "SHOULD"
    },
    {
      "category": "robustness",
      "requirement": "Re-run with GDP per capita (log) and internet penetration rate as time-varying controls at the country-quarter level to rule out concurrent economic/tech confounders.",
      "priority": "SHOULD"
    },
    {
      "category": "robustness",
      "requirement": "Sensitivity to HHI construction: re-compute HHI using only languages above a minimum share threshold (e.g., >0.5% share) to separate genuine diversity from noise tokens. Compare main and trimmed-HHI results.",
      "priority": "SHOULD"
    },
    {
      "category": "robustness",
      "requirement": "Report results dropping the largest 5 countries by contribution to total language volume (likely English-dominant outliers). Coefficient stability confirms results are not driven by a few high-weight observations.",
      "priority": "SHOULD"
    },
    {
      "category": "robustness",
      "requirement": "Bootstrap confidence intervals (at least 500 draws, block bootstrap at country level) as a supplement to analytical cluster-robust SEs, especially for the heterogeneity estimates.",
      "priority": "NICE"
    },
    {
      "category": "data_construction",
      "requirement": "Document the HHI formula used (sum of squared shares, normalized or raw). A normalized HHI = (raw_HHI - 1/N) / (1 - 1/N) is preferable when N_languages varies by country-quarter. Specify which formula in the paper.",
      "priority": "MUST"
    },
    {
      "category": "data_construction",
      "requirement": "The 161,922 raw rows likely represent country×quarter×language triples. The regression dataset after aggregation to country×quarter will be far smaller (~1,600–3,200 obs). Confirm this aggregation step is correct and log the row count at each stage.",
      "priority": "MUST"
    },
    {
      "category": "data_construction",
      "requirement": "Verify that English proficiency data (EF EPI or equivalent) is matched to countries at the correct year. EF scores are published annually — do not use a single cross-sectional wave for a multi-year panel without noting the assumption of time-invariant proficiency.",
      "priority": "MUST"
    },
    {
      "category": "data_construction",
      "requirement": "Create a data provenance log: for each of the 6 columns, record the source, date of download, any transformations, and missing-value rate. Required for replication.",
      "priority": "MUST"
    },
    {
      "category": "data_construction",
      "requirement": "Check for and document country name/code harmonization across datasets (ISO 3166 alpha-2 or alpha-3). Mismatched keys silently drop countries.",
      "priority": "MUST"
    },
    {
      "category": "data_construction",
      "requirement": "Flag and handle countries that enter or exit the panel mid-sample (unbalanced panel). Document whether missing quarters are structural (country not covered) or random. Use a balanced sub-panel as one robustness check.",
      "priority": "SHOULD"
    }
  ],
  "data_warnings": [
    "With ChatGPT released globally at one date, there is NO clean control group — all countries are treated simultaneously. The identification assumption is that absent ChatGPT, within-country HHI would have followed the pre-treatment trend (parallel trends in time, not across units). Referees will push hard on this. State it explicitly.",
    "HHI is mechanically bounded [1/N, 1]. Countries with very few observed languages will have high HHI by construction, not necessarily reflecting genuine concentration. Control for log(N_languages) or use normalized HHI.",
    "Shannon entropy is unbounded and scales with N_languages. A country gaining new rare languages increases entropy mechanically even if dominant language share is unchanged. Decompose into intensive margin (share redistribution) vs. extensive margin (new language entry).",
    "Repeated cross-sections (not panel of the same users) means within-country changes in HHI could reflect compositional changes in who is producing content, not behavioral responses to ChatGPT. Acknowledge this as a key limitation.",
    "The COVID-19 period (Q1 2020–Q4 2021) is in-sample. COVID caused major shifts in digital activity and language patterns. Include a COVID-era control (e.g., stringency index) or at minimum test sensitivity to dropping 2020–2021.",
    "ChatGPT API access (March 2023) vs. consumer release (November 2022) creates ambiguity about when 'treatment' starts for content production. Developers vs. general users have different lags. Sensitivity to treatment timing is non-negotiable for referees.",
    "English-language countries may show differential patterns simply because ChatGPT is primarily English-trained, not because of proficiency per se. Disentangle English-as-dominant-language from English proficiency in the heterogeneity analysis.",
    "If the platform data is from a single source (e.g., GitHub, StackOverflow, Wikipedia), the HHI reflects that platform's ecosystem, not a general 'language ecosystem.' The paper's framing must match the data scope precisely.",
    "Small countries with sparse observations will have noisy HHI estimates. A minimum observations-per-cell threshold should be enforced and documented."
  ],
  "tables_required": [
    "Table 1: Summary statistics — mean, SD, min/max of HHI, Shannon entropy, N_languages, English proficiency, by pre/post period and by high/low English proficiency quartile",
    "Table 2: Main event study results — distributed lag coefficients for HHI (col 1) and Shannon entropy (col 2), with pre-trend F-test p-value, N_countries, N_quarters, N_obs in footer",
    "Table 3: Heterogeneity by English proficiency — interaction model coefficients, comparing high vs. low EF proficiency groups, for both HHI and entropy outcomes",
    "Table 4: Robustness panel — main post-period ATT estimate across: (i) baseline, (ii) country-specific trends, (iii) time-varying controls, (iv) balanced panel, (v) winsorized outcome, (vi) normalized HHI",
    "Table 5: Placebo tests — event study estimates under alternative (fake) treatment dates Q1 2022 and Q1 2024, alongside true Q1 2023 estimate",
    "Appendix Table A1: Country coverage — list of countries included, N_quarters observed, mean HHI, English proficiency score",
    "Appendix Table A2: Alternative treatment timing — post-period estimates under Q4 2022, Q1 2023, Q2 2023 event definitions"
  ],
  "figures_required": [
    "Figure 1: Raw trends — time series of mean HHI and mean Shannon entropy by quarter, with ChatGPT release marked, separately for high/low English proficiency country groups",
    "Figure 2: Main event study plot — beta_k coefficients with 95% CI for leads and lags, for HHI (panel A) and Shannon entropy (panel B). Must show pre-period flat (or show it is not flat and explain)",
    "Figure 3: Heterogeneity event study — separate event study plots for high vs. low English proficiency countries, overlaid or side-by-side",
    "Figure 4: Placebo event study — overlay of event study plots under true treatment date vs. placebo dates, for the main HHI outcome",
    "Appendix Figure A1: Country-level scatter — pre-post change in HHI vs. English proficiency score, with regression line, to motivate the heterogeneity analysis",
    "Appendix Figure A2: Distribution of HHI across country-quarters, pre vs. post, to document any distributional shifts beyond the mean"
  ]
}
```

**Key editorial notes beyond the checklist:**

The single most important issue a referee will raise: **there is no control group**. Every country got ChatGPT at (roughly) the same time, so the TWFE country FE is absorbing cross-sectional levels, not providing a control group. Your identification rests entirely on the parallel pre-trends assumption (within-country trend extrapolation). Be explicit about this in the paper — don't let a referee discover it for you.

Second concern: the **repeated cross-sections** structure means HHI changes could reflect who is on the platform changing, not how existing users changed behavior. This is a fundamental scope limitation that must be stated clearly, not buried in a footnote.

Third: the **normalized HHI vs. raw HHI** distinction will matter greatly given that N_languages almost certainly varies across country-quarters and may itself respond to ChatGPT.