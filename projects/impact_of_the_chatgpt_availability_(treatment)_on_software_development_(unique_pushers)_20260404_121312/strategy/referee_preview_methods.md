```json
{
  "code_requirements": [
    {
      "category": "inference",
      "requirement": "Wild cluster bootstrap (Rademacher weights, 999+ replications) as PRIMARY inference method for all TWFE DiD specifications. Country-level clustering almost certainly yields fewer than 50 clusters; asymptotic cluster-robust SEs are unreliable at this scale. Use 'wildboottest' (Python) or 'boottest' (Stata). Report p-values from wild bootstrap alongside analytical SEs.",
      "priority": "MUST"
    },
    {
      "category": "inference",
      "requirement": "For the China/Russia TWFE DiD specifically: with only 2 treated units, also report randomization inference (permutation test over all possible treatment assignments in the donor pool). This is a more honest uncertainty quantification than any bootstrap when N_treated is this small.",
      "priority": "MUST"
    },
    {
      "category": "inference",
      "requirement": "For Italy synthetic control: permutation inference (in-space placebo) by running synthetic control for every country in the donor pool and computing the distribution of post/pre RMSPE ratios. Italy's p-value = rank of its ratio among all placebos. Report exact p-value and figure showing all placebo paths.",
      "priority": "MUST"
    },
    {
      "category": "inference",
      "requirement": "Document exact clustering level in every table footnote. If any specification clusters below country level (e.g., country-quarter), justify why and show robustness to country-level clustering.",
      "priority": "MUST"
    },
    {
      "category": "specification",
      "requirement": "PRE-TREND TEST: Joint F-test (chi-squared test) that all pre-treatment period coefficients are jointly zero in the event-study specification. Use quarters (or months) as time periods. Report the F-statistic, degrees of freedom, and p-value. Failure to reject is necessary but not sufficient; also report the power of this test (Roth 2022 sensitivity).",
      "priority": "MUST"
    },
    {
      "category": "specification",
      "requirement": "NO-ANTICIPATION TEST: Include leads t-2 and t-3 (two and three periods before treatment) as separate regressors. If either is individually or jointly significant, the no-anticipation assumption is violated — this must be discussed prominently. Developers may migrate platforms or use VPNs in anticipation of announced bans.",
      "priority": "MUST"
    },
    {
      "category": "specification",
      "requirement": "STAGGERED TREATMENT AUDIT: Document the exact restriction dates for Italy (March 31, 2023 ban; April 28, 2023 lift), China (de facto from ChatGPT launch Nov 2022), and Russia (early 2023 restriction). If China and Russia have different effective treatment dates, this is a staggered DiD — confirm whether TWFE produces negatively-weighted estimates. With only 2 treated units, Sun-Abraham (2021) is impractical but de Chaisemartin & D'Haultfoeuille (2020) DIDM should be run as robustness for the China/Russia specification.",
      "priority": "MUST"
    },
    {
      "category": "specification",
      "requirement": "PARALLEL TRENDS VISUALIZATION: Plot raw trends in unique pushers for treatment and synthetic/matched control groups over the full sample window. The visual pre-trend alignment must be shown — a figure is required, not just the F-test.",
      "priority": "MUST"
    },
    {
      "category": "specification",
      "requirement": "SYNTHETIC CONTROL FIT QUALITY: Report pre-treatment RMSPE and post-treatment RMSPE separately. Compute the post/pre RMSPE ratio. If ratio < 2, interpret cautiously. Report the donor pool weights table — which countries receive non-trivial weight and why they are valid donors.",
      "priority": "MUST"
    },
    {
      "category": "specification",
      "requirement": "PREDICTOR BALANCE TABLE (synthetic control): Report a table comparing Italy vs. synthetic Italy on all predictors used to construct the synthetic control (pre-treatment average unique pushers, GDP per capita, internet penetration, developer population proxies). This is the synthetic control analog of a covariate balance table.",
      "priority": "MUST"
    },
    {
      "category": "specification",
      "requirement": "RAMBACHAN-ROTH (2023) HonestDiD breakdown point: For both Italy and China/Russia DiD specifications, compute the sensitivity parameter delta at which the confidence intervals include zero. This quantifies how much pre-trend violation would overturn the result. Use the 'HonestDiD' Python package.",
      "priority": "MUST"
    },
    {
      "category": "specification",
      "requirement": "STABLE COMPOSITION CHECK: Document entry and exit of countries in the sample across time periods. If countries enter or exit non-randomly, the balanced vs. unbalanced panel distinction matters. Show results are robust to a balanced country panel.",
      "priority": "MUST"
    },
    {
      "category": "specification",
      "requirement": "COMMON SUPPORT: Verify that treated and matched control countries overlap in pre-treatment unique pushers distribution. A propensity score overlap plot or a quantile-quantile comparison of pre-treatment outcomes between treated and control groups is required.",
      "priority": "MUST"
    },
    {
      "category": "specification",
      "requirement": "PLACEBO OUTCOME: Run the same DiD/synthetic control specification on at least one outcome that ChatGPT restrictions should NOT affect (e.g., number of commits in a language predating ChatGPT's training data, or a non-software metric). A significant placebo effect signals a confound.",
      "priority": "MUST"
    },
    {
      "category": "specification",
      "requirement": "PLACEBO TIMING: For Italy, re-run the synthetic control using a fake treatment date 4-6 quarters before the actual ban. The estimated effect should be near zero. For China/Russia TWFE, run with a false treatment date set 2 years prior to actual restrictions.",
      "priority": "MUST"
    },
    {
      "category": "specification",
      "requirement": "EXPECTED SIGN DECLARATION: Before running any regression, record in code comments the expected sign of the treatment coefficient (negative: restrictions reduce unique pushers). If any main result is positive (restrictions increase pushers), this must be explicitly discussed as an anomaly — not buried.",
      "priority": "MUST"
    },
    {
      "category": "specification",
      "requirement": "EFFECT MAGNITUDE BENCHMARKING: Convert estimated coefficients to percentage changes in unique pushers. Compare to prior literature estimates of ChatGPT's productivity effects (e.g., Peng et al. 2023, GitHub Copilot study). Flag if the implied effect exceeds 1 standard deviation of the pre-treatment outcome distribution.",
      "priority": "MUST"
    },
    {
      "category": "robustness",
      "requirement": "LEAVE-ONE-OUT DONOR POOL: For the Italy synthetic control, drop each high-weight donor country one at a time and re-estimate. Plot the distribution of post-treatment gaps. If the estimate is highly sensitive to one donor, this must be disclosed.",
      "priority": "MUST"
    },
    {
      "category": "robustness",
      "requirement": "VPN PENETRATION AS CONFOUNDER: Obtain VPN usage rate data (e.g., GlobalWebIndex, Top10VPN reports) for Italy, China, and Russia. VPN usage attenuates the treatment effect — if developers bypass restrictions via VPN, estimated effects are lower bounds. Include VPN penetration as a control or heterogeneity dimension. If VPN data unavailable, explicitly state this as a threat to internal validity.",
      "priority": "MUST"
    },
    {
      "category": "robustness",
      "requirement": "ITALY TEMPORARY BAN DYNAMICS: Italy's ban lasted approximately 28 days. Run separate regressions for: (1) during the ban only, (2) immediately post-lift (adjustment period), (3) longer run post-lift. A temporary ban may show immediate reversal — the dynamic path matters for interpretation.",
      "priority": "MUST"
    },
    {
      "category": "robustness",
      "requirement": "ALTERNATIVE CONTROL GROUP CONSTRUCTION: For China/Russia, report results using (1) propensity score matching, (2) synthetic control (treating China and Russia separately), and (3) all non-restricted countries as control. Main results should not depend critically on a single matching algorithm.",
      "priority": "MUST"
    },
    {
      "category": "robustness",
      "requirement": "EXCLUDING GEOGRAPHIC SPILLOVER COUNTRIES: Remove from the donor pool countries that share a border with or have high developer migration links to Italy/China/Russia. Spillovers via developer relocation or VPN routing would contaminate control group outcomes.",
      "priority": "MUST"
    },
    {
      "category": "robustness",
      "requirement": "EVENT WINDOW SENSITIVITY: Re-run all event studies with windows of ±3, ±6, ±12 months. The point estimate and significance should be stable across windows, or the instability must be explained.",
      "priority": "SHOULD"
    },
    {
      "category": "robustness",
      "requirement": "ALTERNATIVE OUTCOME DEFINITIONS: Run main specifications using (1) log(unique_pushers + 1), (2) level of unique pushers, (3) unique pushers normalized by internet users or developer population proxy. Log transformation is preferred but verify mass-at-zero structure first.",
      "priority": "SHOULD"
    },
    {
      "category": "robustness",
      "requirement": "HETEROGENEITY BY LANGUAGE: If data permits, decompose effects by programming language. Languages more associated with AI-assisted coding (Python, JavaScript) should show larger declines than lower-association languages (COBOL, Fortran). This is a theoretical prediction that strengthens causal interpretation if confirmed.",
      "priority": "SHOULD"
    },
    {
      "category": "robustness",
      "requirement": "INTERNET FREEDOM INDEX INTERACTION: Interact treatment with country-level internet freedom score (Freedom House or EF EPI). Countries with already-low internet freedom may show attenuated effects (developers more accustomed to circumvention tools).",
      "priority": "SHOULD"
    },
    {
      "category": "robustness",
      "requirement": "DE CHAISEMARTIN & D'HAULTFOEUILLE (2020) DIDM: Run as robustness for the China/Russia specification if their effective treatment dates differ. Report alongside TWFE estimate and note direction of any divergence.",
      "priority": "SHOULD"
    },
    {
      "category": "presentation",
      "requirement": "All regression tables must include: coefficient, standard error (analytical), wild bootstrap p-value, 95% CI (wild bootstrap), number of observations (N), number of clusters, R-squared (within), country fixed effects indicator, time fixed effects indicator. No table should omit cluster count.",
      "priority": "MUST"
    },
    {
      "category": "presentation",
      "requirement": "Synthetic control figures must show: (1) treated vs. synthetic control trends over full window with treatment date marked, (2) gap plot (treated minus synthetic) with zero reference line, (3) in-space placebo paths for all donor countries overlaid in gray with Italy highlighted.",
      "priority": "MUST"
    },
    {
      "category": "presentation",
      "requirement": "Event study coefficient plots must display: point estimates with 95% CI (wild bootstrap), pre-treatment reference period clearly labeled, treatment date marked, joint pre-trend F-test statistic and p-value in figure caption or note.",
      "priority": "MUST"
    },
    {
      "category": "presentation",
      "requirement": "Summary statistics table must include: mean, SD, min, max, and p25/p75 for unique pushers separately for treatment and control groups, both pre- and post-treatment. This allows readers to assess balance and effect magnitude.",
      "priority": "MUST"
    },
    {
      "category": "presentation",
      "requirement": "Report effect sizes in interpretable units: % change in unique pushers relative to pre-treatment mean, and absolute change. If available, translate to implied number of developers affected. Do not report only standardized coefficients.",
      "priority": "MUST"
    },
    {
      "category": "pitfall",
      "requirement": "CRITICAL — TWO TREATED UNITS (China, Russia): With only 2 treated countries in the TWFE DiD, the design is extremely underpowered for country-level effects. Asymptotic inference is invalid. All inferential weight must rest on wild bootstrap and/or randomization inference. Do NOT interpret p-values from OLS standard errors in this specification.",
      "priority": "MUST"
    },
    {
      "category": "pitfall",
      "requirement": "AVOID POOLING ITALY WITH CHINA/RUSSIA: The Italy treatment (temporary ban, democratic country, high VPN uptake, EU regulatory context) is qualitatively different from China/Russia (permanent restrictions, authoritarian context, pre-existing Great Firewall infrastructure). Pooling them in a single DiD destroys interpretability. Keep specifications separate throughout.",
      "priority": "MUST"
    },
    {
      "category": "pitfall",
      "requirement": "REPEATED CROSS-SECTIONS ≠ PANEL: The data structure is repeated cross-sections, not a balanced panel of individuals. Do not apply individual fixed effects or interpret within-person variation. The unit of observation is country-period. Document whether the country-period cells are balanced across time.",
      "priority": "MUST"
    },
    {
      "category": "pitfall",
      "requirement": "SURVIVORSHIP BIAS IN GITHUB DATA: GitHub activity data may undercount developers in restricted countries if VPN use shifts activity to alternative platforms (Gitee in China). A drop in GitHub unique pushers in China could reflect platform substitution rather than reduced development activity. Acknowledge and, if possible, test using Gitee or other platform data as a robustness check.",
      "priority": "MUST"
    },
    {
      "category": "pitfall",
      "requirement": "DO NOT USE TWFE WITH UNIT-SPECIFIC LINEAR TRENDS as a primary specification — it can overcontrol when treatment effects are persistent and linear. If included as robustness, interpret cautiously and explain why the trend assumption is plausible.",
      "priority": "SHOULD"
    },
    {
      "category": "pitfall",
      "requirement": "DONOR POOL CONTAMINATION: Exclude from the donor pool any country that (1) also restricted ChatGPT during the sample period, (2) is a major trading or migration partner that might absorb displaced developers, or (3) experienced a major GitHub policy change contemporaneously. Document exclusions explicitly.",
      "priority": "MUST"
    },
    {
      "category": "pitfall",
      "requirement": "DO NOT INTERPRET SYNTHETIC CONTROL GAPS AS CAUSAL WITHOUT ADDRESSING: the no-spillover SUTVA assumption (developers in donor countries unaffected by Italy/China/Russia restrictions) and the no-interference assumption (Italy's ban did not shift global developer behavior). Discuss briefly.",
      "priority": "MUST"
    },
    {
      "category": "pitfall",
      "requirement": "GITHUB DATA TIMING: Verify whether the GitHub push data reflects the time of the push commit or the time of repository creation. A systematic lag could misalign the treatment window. Document the timestamp definition used.",
      "priority": "SHOULD"
    },
    {
      "category": "pitfall",
      "requirement": "MULTIPLE TESTING: Three distinct analyses (Italy synthetic control, Italy DiD event study, China/Russia TWFE) plus robustness checks generate multiple comparisons. Apply Bonferroni or Benjamini-Hochberg correction when summarizing which specifications achieve significance, or explicitly acknowledge the multiple testing concern.",
      "priority": "SHOULD"
    }
  ],
  "method_warnings": [
    "POWER WARNING — ITALY: The Italian ChatGPT ban lasted ~28 days. With a monthly or quarterly time series, this translates to a single treated period. Statistical power to detect a short-duration effect is extremely low, especially after accounting for the wild bootstrap penalty. Pre-register a minimum detectable effect (MDE) calculation.",
    "POWER WARNING — CHINA/RUSSIA: Two treated country-units makes this design closer to a case study than a DiD. Treat the TWFE coefficient as directional evidence only; causal inference claims must be heavily qualified. Synthetic control applied separately to China and Russia may be more credible than TWFE pooling.",
    "VPN ATTENUATION BIAS: In all three countries, VPN usage partially bypasses restrictions. The treatment 'ChatGPT access restriction' is fuzzy and imperfectly implemented. Estimated effects are therefore attenuated lower bounds on the true effect. This must be stated in the abstract or introduction, not buried in robustness.",
    "CONFOUNDS CONTEMPORANEOUS WITH TREATMENT: China's restrictions on ChatGPT coincide with the post-COVID period and broader tech sector crackdowns; Russia's restrictions coincide with sanctions and developer emigration following the February 2022 invasion of Ukraine. Developer emigration from Russia is a major potential confound — if Russian developers relocated to other countries, GitHub pushers attributed to Russia fall for non-AI reasons. This confound is severe and must be addressed.",
    "SYNTHETIC CONTROL FOR SINGLE UNIT: Italy synthetic control is appropriate (single treated unit), but the post-treatment window being short (ban lifted quickly) limits power. The synthetic control is better suited to detecting persistent effects; for a temporary ban, the event-study DiD may actually be the more informative design.",
    "REPEATED CROSS-SECTION IDENTIFICATION: In repeated cross-sections, DiD identifies the ATT only under parallel trends at the aggregate (country-period) level. This is weaker than panel DiD because individual-level composition can change. If the composition of who pushes code changes systematically (e.g., casual contributors drop out more than core contributors in restricted countries), the measured decline in unique pushers conflates intensive and extensive margin changes.",
    "DATA SPARSITY: With 161,922 rows and 6 columns across multiple countries and time periods, check whether some country-period cells have very few underlying pushers. Outcomes based on small counts are noisy and may require count model robustness checks (Poisson QMLE with two-way FE)."
  ],
  "must_not_claim": [
    "Must NOT claim causal identification without passing the joint pre-trend F-test AND showing HonestDiD breakdown point is economically meaningful.",
    "Must NOT claim 'parallel trends holds' based solely on a visual plot — a formal statistical test is required.",
    "Must NOT pool Italy (temporary ban) with China/Russia (permanent restrictions) in a single treatment coefficient and call it a unified causal estimate.",
    "Must NOT interpret asymptotic cluster-robust standard errors as reliable when the number of clusters is below 50 — wild bootstrap is non-negotiable.",
    "Must NOT attribute the China effect exclusively to ChatGPT access restrictions without addressing the Russia-Ukraine war developer emigration confound (Russia) or the broader tech crackdown confound (China).",
    "Must NOT interpret a null result in the China/Russia specification as evidence that ChatGPT access does not matter — with 2 treated units, the design is severely underpowered and a null result is uninformative about the true effect.",
    "Must NOT claim the Italy estimate is representative of ChatGPT's contribution to software development globally — Italy is a single country with a brief, temporary, and partially circumventable ban.",
    "Must NOT use OLS p-values from analytical standard errors as the primary basis for hypothesis testing in any of the three main specifications.",
    "Must NOT claim the synthetic control estimate represents a causal effect without showing the in-space placebo p-value is below 0.10 (and ideally 0.05) — with small donor pools, exact p-values may be no better than 0.05-0.10 even under the null.",
    "Must NOT ignore platform substitution (GitHub → Gitee in China) as an alternative explanation for reduced GitHub activity in restricted countries."
  ]
}
```