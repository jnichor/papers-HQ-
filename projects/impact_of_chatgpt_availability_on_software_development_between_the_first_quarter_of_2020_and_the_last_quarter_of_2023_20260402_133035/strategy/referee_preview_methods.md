```json
{
  "code_requirements": [
    {
      "category": "inference",
      "requirement": "Cluster standard errors at the COUNTRY level (the level at which treatment — ChatGPT release — varies). With ~161 countries this is above the 50-cluster threshold, so asymptotic two-way cluster-robust SEs (country × quarter) are acceptable as the primary method. However, implement wild cluster bootstrap (Rademacher weights, 999 replications) as a robustness check using the 'wildboottest' package, because language-ecosystem outcomes likely exhibit strong within-country serial correlation that inflates effective cluster count.",
      "priority": "MUST"
    },
    {
      "category": "inference",
      "requirement": "Since treatment is SIMULTANEOUS for all countries (ChatGPT released November 2022, Q4 2022), Sun & Abraham (2021) and Callaway & Sant'Anna (2021) estimators are NOT required — staggered-adoption bias does not apply here. Standard TWFE with country and quarter fixed effects is the correct baseline estimator. Do NOT apply heterogeneity-robust staggered estimators; their assumptions are violated when all units share the same treatment date.",
      "priority": "MUST"
    },
    {
      "category": "inference",
      "requirement": "Q4 2022 is a PARTIAL-TREATMENT quarter (ChatGPT launched November 30, 2022, covering only ~1 month of the quarter). Code must handle this explicitly: either (a) drop Q4 2022 from the event window and treat Q1 2023 as period +1, or (b) include Q4 2022 with a fractional treatment indicator (1/3 of quarter treated). Both approaches must be run; coefficients should agree qualitatively. Document which choice is the main specification.",
      "priority": "MUST"
    },
    {
      "category": "specification",
      "requirement": "PRE-TREND TEST (causal identification check): Run a joint F-test (or chi-squared Wald test) of H0: all pre-treatment event-time coefficients = 0. With Q1 2020 – Q3 2022 as pre-period, this is a test on ~11 leads. Report the p-value prominently. A rejection at p < 0.10 must trigger a discussion of identification validity, not silence.",
      "priority": "MUST"
    },
    {
      "category": "specification",
      "requirement": "Implement Roth (2022) sensitivity analysis ('HonestDiD' Python port or R package called via subprocess) to quantify how large a pre-trend violation would need to be to overturn the main result. Report the breakdown coefficient M* alongside the main event-study figure. This is required because pre-trend tests have low power with short pre-periods.",
      "priority": "MUST"
    },
    {
      "category": "specification",
      "requirement": "Explicitly state and normalize the REFERENCE PERIOD in the event study. The omitted period must be t = -1 (the quarter immediately before treatment, i.e., Q3 2022). Using t = 0 as the reference or silently dropping an arbitrary period invalidates pre-trend interpretation. The coefficient at t = -1 must be mechanically zero by construction and labeled as such in all figures.",
      "priority": "MUST"
    },
    {
      "category": "specification",
      "requirement": "Test for ANTICIPATION EFFECTS: ChatGPT was demoed and widely discussed before November 2022. Run a specification that allows t = -2 (Q2 2022) and t = -3 (Q1 2022) to absorb anticipation. If these coefficients are non-zero and statistically significant, the treatment date should be revised backward or the anticipation window explicitly modeled.",
      "priority": "MUST"
    },
    {
      "category": "specification",
      "requirement": "Run PLACEBO TESTS: (1) Assign a false treatment date of Q1 2021 (placebo timing), restricting data to the pre-ChatGPT period Q1 2020–Q3 2022. The placebo event-study coefficients should be centered on zero. (2) Permutation placebo: reassign English-proficiency group labels randomly across countries (999 permutations) and verify that the true interaction coefficient lies in the tail of the permutation distribution. Both placebos must be reported.",
      "priority": "MUST"
    },
    {
      "category": "specification",
      "requirement": "Check for CONFOUNDING CO-TREATMENTS: GitHub Copilot (October 2021 GA), GPT-4 (March 2023), and Google Bard (March 2023) are contemporaneous AI coding tools. The code must either (a) include these as additional treatment indicators in the main spec, or (b) restrict the post-period to Q1 2023 only (before GPT-4/Bard) as a clean post-window robustness check. Failure to address confounders makes the ChatGPT-specific interpretation invalid.",
      "priority": "MUST"
    },
    {
      "category": "specification",
      "requirement": "Test for COMPOSITION EFFECTS in HHI: If the set of languages observed per country×quarter changes (language entry/exit), HHI and entropy change mechanically even with no behavioral shift. The code must (a) document the number of distinct languages per country×quarter and test whether this count changes around treatment, and (b) run a robustness spec computing HHI on a BALANCED set of languages (only those present in every quarter for a given country). If composition effects are present, they must be acknowledged as a threat to interpretation.",
      "priority": "MUST"
    },
    {
      "category": "robustness",
      "requirement": "Run the main event study with COUNTRY-SPECIFIC LINEAR TIME TRENDS added (i.e., country_i × t as a covariate). This absorbs differential pre-existing trends across countries. If point estimates change substantially, the parallel-trends assumption is fragile and must be discussed.",
      "priority": "MUST"
    },
    {
      "category": "robustness",
      "requirement": "Estimate a BALANCED PANEL robustness check: restrict to countries present in every quarter from Q1 2020 through Q4 2023. Compare sample size and main coefficients to the unbalanced spec. Large differences signal attrition bias.",
      "priority": "MUST"
    },
    {
      "category": "robustness",
      "requirement": "Run with ALTERNATIVE TREATMENT TIMING: (1) GPT-4 release (Q1 2023) as the event date, (2) a placebo at Q4 2021 (two years prior). The GPT-4 spec tests whether observed effects accelerate with a more capable model; the placebo tests the null.",
      "priority": "SHOULD"
    },
    {
      "category": "robustness",
      "requirement": "Because HHI ∈ [0,1] is a BOUNDED OUTCOME, run a fractional logit (quasi-MLE, Papke-Wooldridge) as a robustness check alongside the linear TWFE. If the linear model predicts fitted values outside [0,1] for any observation, report the share of out-of-bounds predictions; this is prima facie evidence the linear spec is misspecified.",
      "priority": "SHOULD"
    },
    {
      "category": "robustness",
      "requirement": "For the ENGLISH PROFICIENCY HETEROGENEITY analysis, discretize English proficiency into at minimum three groups (low/medium/high) rather than a single binary split. Report interaction coefficients and a joint test that all group-specific post-treatment effects are equal. Additionally, control for baseline GDP per capita and internet penetration to rule out confounding with development level, since English proficiency is strongly correlated with both.",
      "priority": "MUST"
    },
    {
      "category": "robustness",
      "requirement": "Report results for BOTH outcomes (HHI and Shannon entropy) in every table and figure. These measures capture different aspects of concentration (HHI is top-heavy, entropy is tail-sensitive). If they yield qualitatively opposite results, the conclusion is ambiguous and must be presented as such rather than selectively reported.",
      "priority": "MUST"
    },
    {
      "category": "robustness",
      "requirement": "Apply a MULTIPLE TESTING correction (Benjamini-Hochberg FDR at q=0.10) when reporting results across the two outcomes and multiple heterogeneity cuts. Report both uncorrected and corrected p-values. Do not claim significance on a sub-group result that fails after correction without explicit justification.",
      "priority": "SHOULD"
    },
    {
      "category": "presentation",
      "requirement": "EVENT STUDY FIGURE must show: (a) point estimates for each event-time period, (b) 95% confidence intervals as error bars, (c) a horizontal zero line, (d) a vertical line at treatment onset, (e) the reference period t=-1 explicitly labeled as zero, (f) the number of observations per period in a note. Do not use shaded bands without also showing point estimates.",
      "priority": "MUST"
    },
    {
      "category": "presentation",
      "requirement": "REGRESSION TABLES must include for every specification: point estimate, standard error (in parentheses), 95% CI in brackets, number of observations N, number of countries, number of quarters, within-R² (not overall), country FE indicator (Yes/No), quarter FE indicator (Yes/No), country time trend indicator (Yes/No), and clustering level. Use the standard econometrics table format (stars optional but SEs always shown).",
      "priority": "MUST"
    },
    {
      "category": "presentation",
      "requirement": "Report SUMMARY STATISTICS TABLE with: mean, SD, p10, p50, p90, min, max for HHI and Shannon entropy overall and separately for pre- and post-treatment periods. Also report the number of languages per country×quarter (mean and SD) to document potential composition effects.",
      "priority": "MUST"
    },
    {
      "category": "presentation",
      "requirement": "Include a DATA APPENDIX documenting: (1) exact definition of HHI denominator (is it share of queries, users, posts, or lines of code?), (2) how countries are assigned to English-proficiency groups (source, year, cutoff), (3) treatment of ties or missing language data, (4) whether the platform from which data is drawn is representative of the full language ecosystem. Reviewers will ask.",
      "priority": "MUST"
    },
    {
      "category": "pitfall",
      "requirement": "DO NOT interpret the TWFE estimate as the average treatment effect on the treated (ATT) without verifying parallel trends. With simultaneous treatment, TWFE is identified under parallel trends across countries — not staggering. The correct language is 'the difference-in-differences estimate under the parallel trends assumption,' not 'the causal effect of ChatGPT.'",
      "priority": "MUST"
    },
    {
      "category": "pitfall",
      "requirement": "DO NOT use the REPEATED CROSS-SECTIONS structure as if it were a balanced panel without verifying which countries appear in all periods. The data description says 'repeated cross-sections,' meaning the panel may be unbalanced or entry/exit is present. All panel estimators must account for this, and the share of balanced vs. unbalanced observations must be reported.",
      "priority": "MUST"
    },
    {
      "category": "pitfall",
      "requirement": "AVOID ENDPOINT BIAS in the event study: if the post-period has only 4–5 quarters (Q1–Q4 2023), the last coefficient is estimated from fewer observations and has wider CIs. Do not over-interpret a flattening or acceleration in the last period. Flag this explicitly in the figure note.",
      "priority": "SHOULD"
    },
    {
      "category": "pitfall",
      "requirement": "DO NOT aggregate language-level data to country×quarter HHI using simple averages if the underlying data is user- or query-weighted. The HHI construction must use WEIGHTED shares (e.g., share of total activity in that country×quarter, not mean of binary language indicators). Document the aggregation formula explicitly in code comments.",
      "priority": "MUST"
    },
    {
      "category": "pitfall",
      "requirement": "BEWARE of the ECOLOGICAL INFERENCE FALLACY: country-level HHI changes do not imply individual-level language switching. The paper may only claim that the distribution of language activity shifted at the country level; it cannot claim individual programmers switched languages. All causal language must be scoped to the country-level aggregate.",
      "priority": "MUST"
    }
  ],
  "method_warnings": [
    "Simultaneous treatment (all countries, Q4 2022) means there is no clean control group — every country is treated. Identification rests entirely on parallel pre-trends across countries and the assumption that no other global shock hit language ecosystems in Q4 2022–Q1 2023. This is a fundamentally weaker identification strategy than staggered adoption; the paper must be explicit about this.",
    "HHI is mechanically sensitive to the NUMBER of languages in the denominator. If ChatGPT caused new (niche) languages to appear on the platform, HHI falls mechanically. If it caused some languages to disappear, HHI rises mechanically. Neither is a behavioral effect. Composition-adjusted HHI is essential, not optional.",
    "English proficiency at the country level is endogenous to development status, historical colonialism, and internet access. The heterogeneity analysis cannot be given a causal interpretation — it is purely descriptive effect modification. Do not use the word 'mechanism' to describe this split without an instrument for English proficiency.",
    "The 6-column dataset with 161,922 rows is very sparse relative to the richness of a country×language×quarter panel. Verify that the panel is not dominated by a few high-observation countries (e.g., US, India, UK) that drive the aggregate result. Report country-level weights in the regression and check whether results hold when weighting equally by country rather than by observation count.",
    "Stack Overflow, GitHub, or similar platforms have self-selected user bases. The 'language ecosystem' being measured is the ecosystem of platform users, not the global developer population. Generalizability claims must be scoped accordingly.",
    "With only ~4 post-treatment quarters, the event study has low power to detect delayed treatment effects or to distinguish a one-time level shift from a trend change. The paper should acknowledge this limitation and avoid claiming the long-run effect has been identified."
  ],
  "must_not_claim": [
    "Must NOT claim Sun & Abraham (2021) or Callaway & Sant'Anna (2021) estimators were used for bias correction — these are irrelevant under simultaneous treatment and their use would be methodologically incorrect.",
    "Must NOT claim a causal effect of ChatGPT without passing the joint pre-trend F-test at conventional significance levels and without conducting the Roth (2022) sensitivity analysis.",
    "Must NOT claim the English-proficiency heterogeneity result identifies a mechanism — it is descriptive effect modification only.",
    "Must NOT extrapolate the HHI result to 'language diversity globally' — the data covers only one (unnamed) platform and its user base.",
    "Must NOT treat the Q4 2022 partial-treatment period as equivalent to a full post-treatment quarter without adjustment or sensitivity analysis.",
    "Must NOT claim the result is robust to confounders without explicitly controlling for or testing against co-occurring AI tool releases (Copilot GA, GPT-4, Bard).",
    "Must NOT report only the overall treatment effect if the pre-trend test fails — in that case, the event-study plot is the only permissible display, with an explicit statement that causal interpretation is compromised."
  ]
}
```