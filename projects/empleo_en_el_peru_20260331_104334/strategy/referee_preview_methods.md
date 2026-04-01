```json
{
  "code_requirements": [
    {
      "category": "inference",
      "requirement": "Cluster standard errors at the occupation-group level — the level at which the Dingel-Neiman teleworkability index is assigned — NOT at the individual level. Treatment variation is at the occupation×time cell; clustering below the treatment level understates uncertainty. Report the number of clusters explicitly in every table.",
      "priority": "MUST"
    },
    {
      "category": "inference",
      "requirement": "If the number of occupation clusters is fewer than 50, implement wild cluster bootstrap (Cameron–Gelbach–Miller 2008) with ≥999 replications. Report both analytical cluster-robust SEs and wild-bootstrap p-values side by side. The decision threshold must be documented in the code.",
      "priority": "MUST"
    },
    {
      "category": "inference",
      "requirement": "For all subgroup analyses (firm size, gender, region), apply Holm correction for multiple comparisons across the three heterogeneity dimensions. Report both raw and corrected p-values. Do NOT selectively report only significant subgroup results.",
      "priority": "MUST"
    },
    {
      "category": "inference",
      "requirement": "Consider two-way clustering on occupation × year as a robustness check, since the COVID shock induces within-year correlation across occupation groups. Compare SEs under one-way vs. two-way clustering.",
      "priority": "SHOULD"
    },
    {
      "category": "specification",
      "requirement": "Use Sun–Abraham (2021) interaction-weighted estimator as the PRIMARY event-study specification. TWFE event-study coefficients may only appear as a comparison column, never as the headline result. Staggered recovery paths produce heterogeneous treatment effects that contaminate TWFE with negative weights.",
      "priority": "MUST"
    },
    {
      "category": "specification",
      "requirement": "Run a formal joint F-test (χ² for large N) of all pre-period event-study coefficients being jointly zero. Report the test statistic, degrees of freedom, and p-value on the event-study plot and in the corresponding table note. This is the primary parallel-trends diagnostic.",
      "priority": "MUST"
    },
    {
      "category": "specification",
      "requirement": "Implement Bacon (2021) decomposition to document relative weights on each 2×2 DiD component. With a continuous treatment, adapt to the Callaway–Sant'Anna continuous-treatment framework and plot the weight distribution. Any negative weights must be flagged.",
      "priority": "MUST"
    },
    {
      "category": "specification",
      "requirement": "Conduct ENAHO panel retention analysis: for each wave 2020–2023 report (a) fraction of baseline individuals matched, (b) probit regression of attrition on pre-COVID baseline characteristics (informality status, sector teleworkability, firm size, gender, region), (c) p-value for H₀: teleworkability does not predict attrition. This must appear as a standalone numbered table.",
      "priority": "MUST"
    },
    {
      "category": "specification",
      "requirement": "Implement inverse-probability weighting (IPW) for the balanced-panel subsample using predicted retention probabilities from the attrition probit. Present balanced-panel + IPW results alongside the full unbalanced-panel estimates. If they diverge materially, this must be discussed as a threat to validity, not a footnote.",
      "priority": "MUST"
    },
    {
      "category": "specification",
      "requirement": "Implement Roth (2022) sensitivity analysis: compute the minimum confounding pre-trend magnitude that would render post-period estimates statistically insignificant. Report this as a robustness bound. Never cite a non-significant pre-trend test as 'validating' parallel trends.",
      "priority": "SHOULD"
    },
    {
      "category": "specification",
      "requirement": "Run Callaway–Sant'Anna (2021) group-time ATT estimator as a secondary specification, defining 'group' as the year a worker's sector first experienced a mobility restriction above a documented threshold. Use the 'never-treated' or 'not-yet-treated' control group explicitly — document the choice.",
      "priority": "SHOULD"
    },
    {
      "category": "specification",
      "requirement": "Test for anticipation effects: interact the 2019 year dummy with teleworkability and verify the coefficient is not statistically or economically significant. If it is, shift the base period back one year.",
      "priority": "SHOULD"
    },
    {
      "category": "specification",
      "requirement": "Run all main specifications both with and without ENAHO survey probability weights to test whether the stratified sampling design materially changes estimates. ENAHO uses a complex stratified cluster design; unweighted estimates may not be representative.",
      "priority": "SHOULD"
    },
    {
      "category": "robustness",
      "requirement": "Test all three INEI informality definitions in a single side-by-side table: (1) no contributory social security access, (2) no written labor contract or statutory benefits, (3) employed in firm with ≤5 workers. The headline definition must be pre-committed and justified; the other two are robustness columns.",
      "priority": "MUST"
    },
    {
      "category": "robustness",
      "requirement": "Use Saltiel (2020) LAC-reweighted teleworkability scores as the PRIMARY treatment measure; Dingel–Neiman (2020) original US-calibrated scores are a robustness column. Include a binned scatter plot and correlation table comparing the two indices across occupation codes.",
      "priority": "MUST"
    },
    {
      "category": "robustness",
      "requirement": "Composition-effect decomposition: separately estimate the DiD for (a) formal→informal transitions, (b) employed→inactive/unemployed transitions, and (c) informal→inactive transitions. The main result must not conflate informalization with labor-force withdrawal, which is historically large in Peru.",
      "priority": "MUST"
    },
    {
      "category": "robustness",
      "requirement": "Present results for three panel definitions side by side: (a) full unbalanced panel, (b) workers observed in every wave (balanced), (c) balanced + IPW. If estimates diverge, the explanation must be structural, not methodological hand-waving.",
      "priority": "MUST"
    },
    {
      "category": "robustness",
      "requirement": "Implement de Chaisemartin & D'Haultfœuille (2020) did_multiplegt estimator as an additional robustness check for the TWFE heterogeneous-treatment critique. If this estimator and Sun–Abraham diverge, investigate and report why.",
      "priority": "SHOULD"
    },
    {
      "category": "robustness",
      "requirement": "Placebo treatment test: randomly reassign each worker's teleworkability score to a different occupation code, re-estimate the main specification 500 times, and verify the actual estimate lies in the tail of the placebo distribution. Report the empirical p-value.",
      "priority": "SHOULD"
    },
    {
      "category": "robustness",
      "requirement": "Test three functional forms for the continuous teleworkability treatment: (a) linear, (b) four quartile dummies, (c) above/below-median binary split. Estimates must be directionally consistent. If they are not, investigate occupation-group nonlinearities.",
      "priority": "SHOULD"
    },
    {
      "category": "robustness",
      "requirement": "Leave-one-occupation-group-out sensitivity: re-estimate the headline specification dropping one occupation group at a time, plot the distribution of resulting coefficients. If any single group drives the result, flag it prominently.",
      "priority": "NICE"
    },
    {
      "category": "robustness",
      "requirement": "Synthetic control or interrupted time series benchmark for Lima as a single treated unit (large, high-teleworkability capital region) vs. rest-of-Peru. Not required as primary evidence, but addresses the partial-equilibrium scope of the DiD.",
      "priority": "NICE"
    },
    {
      "category": "presentation",
      "requirement": "Every regression table must include: point estimate, cluster-robust SE in parentheses, 95% CI in brackets, N (observations), number of clusters, within-R², and a fixed-effects row explicitly marking individual FE and year FE as Yes/No.",
      "priority": "MUST"
    },
    {
      "category": "presentation",
      "requirement": "Event-study plot must show: Sun–Abraham coefficients with 95% CIs for each relative year (normalize last pre-COVID year to zero), vertical reference line at t=-1, horizontal zero line, and the joint pre-trend F-test statistic and p-value annotated directly on the figure.",
      "priority": "MUST"
    },
    {
      "category": "presentation",
      "requirement": "Attrition table: wave-by-wave retention rates, attrition probit marginal effects with SEs, and p-value for whether teleworkability score predicts attrition — presented as a standalone numbered table, not a footnote or appendix afterthought.",
      "priority": "MUST"
    },
    {
      "category": "presentation",
      "requirement": "Treatment distribution table: occupation-group cell counts, mean and SD of teleworkability by quartile, fraction of sample in each quartile, and pre-COVID baseline informality rate (all three definitions) by teleworkability quartile. This is the primary validity-of-variation table.",
      "priority": "MUST"
    },
    {
      "category": "presentation",
      "requirement": "Heterogeneity results (firm size, gender, region) must be presented as coefficient plots with 95% CIs, not separate regression tables alone, enabling visual comparison of magnitudes and overlap across subgroups.",
      "priority": "SHOULD"
    },
    {
      "category": "presentation",
      "requirement": "For binary informality outcome estimated via LPM: report the fraction of predicted values outside [0,1] and compare LPM marginal effects against logit average marginal effects in a robustness table. If >5% of predictions are out-of-bounds, logit marginal effects should be co-primary.",
      "priority": "SHOULD"
    },
    {
      "category": "pitfall",
      "requirement": "DO NOT build the multi-year panel by row-binding annual ENAHO flat files without first constructing and validating the composite individual identifier (conglome + vivienda + hogar + codperso). Duplicate or incorrectly merged IDs silently corrupt fixed-effects estimation. Validate match rates against official INEI documentation.",
      "priority": "MUST"
    },
    {
      "category": "pitfall",
      "requirement": "DO NOT reshape from wide to long using pd.melt or equivalent without asserting uniqueness of the panel identifier post-reshape. Add an assertion: assert df.duplicated(['id','year']).sum() == 0 immediately after reshaping.",
      "priority": "MUST"
    },
    {
      "category": "pitfall",
      "requirement": "DO NOT run subgroup DiDs in separate samples and claim differential effects. Subgroup heterogeneity requires a formal triple-interaction term (teleworkability × post × subgroup_indicator) estimated on the full sample with a joint significance test on the interaction.",
      "priority": "MUST"
    },
    {
      "category": "pitfall",
      "requirement": "DO NOT treat ENAHO's rotating panel as a standard balanced panel. ENAHO households are surveyed for 5 consecutive quarters then rotated out; multi-year annual linkages depend on wave-to-wave matching with documented match rates. The effective attrition for a 4-year (2019–2023) panel is substantial — document it explicitly.",
      "priority": "MUST"
    },
    {
      "category": "pitfall",
      "requirement": "DO NOT interpret a non-significant pre-trend test as confirming parallel trends. With ≤2 pre-period dummies the test has very low power against smooth confounders. The claim must be hedged: 'we cannot reject parallel pre-trends' with explicit reference to power limitations.",
      "priority": "MUST"
    },
    {
      "category": "pitfall",
      "requirement": "AVOID absorbing occupation fixed effects in a specification that also includes individual fixed effects when occupation is time-varying. If workers change occupations, occupation FE and individual FE are not collinear and the model is identified — but this must be explicitly checked and documented.",
      "priority": "SHOULD"
    },
    {
      "category": "pitfall",
      "requirement": "DO NOT use the within-R² from a binary LPM TWFE as the primary model-fit metric. Within-R² for binary outcomes has no standard probabilistic interpretation. Report it but do not anchor inferential conclusions on it.",
      "priority": "SHOULD"
    }
  ],
  "method_warnings": [
    "TWFE + continuous dose-response treatment + multiple post-periods: the standard Bacon decomposition applies but the continuous-treatment extension (Callaway–Sant'Anna 2021, 'did' R package ≥ v2.1) is required to correctly weight group-time ATTs by treatment intensity. Discretizing to above/below-median is a valid simplification but must be flagged as such.",
    "ENAHO is a rotating panel survey, not a cohort follow-up. Constructing a 4-year (2019–2023) individual panel requires matching annual waves on the composite ID. The match rate will degrade in each successive year; a 4-wave balanced panel likely retains <40% of 2019 respondents. This survivorship creates non-random selection that IPW only partially corrects.",
    "The Dingel–Neiman index was built on US O*NET task data. Saltiel (2020) documents 15–20 pp reattribution for LAC occupations, systematically concentrated in skilled manual and informal service jobs. Using D-N as the primary measure introduces measurement error correlated with skill level — itself correlated with informality — creating a threat to the exclusion restriction that must be named and bounded.",
    "Peru's baseline informality rate (~70% by social-security definition pre-COVID) creates a near-ceiling effect for the most contact-intensive informal sectors. The marginal effect of COVID on informality in these sectors is mechanically compressed relative to high-formality sectors, biasing the treatment coefficient toward zero. Examine the distribution of pre-COVID informality rates across the teleworkability distribution and discuss ceiling effects explicitly.",
    "Gender heterogeneity in Peru is confounded by strong sectoral segregation: women are overrepresented in domestic service and retail, both high-contact and high-informality sectors. The gender × teleworkability interaction will partly reflect sectoral composition, not gender-specific treatment. Include an occupation-within-gender balance table.",
    "Multiple hypothesis testing: three informality definitions × three heterogeneity cuts × at least two estimators (TWFE, Sun–Abraham) × two panel definitions (balanced/unbalanced) yields ~18–36 reported estimates before robustness. Without pre-registration or systematic FWER/FDR correction, selective emphasis on significant results is a credibility threat."
  ],
  "must_not_claim": [
    "Must not claim 'parallel trends are confirmed' or 'validated' based on a non-significant pre-trend test. Correct language: 'we cannot reject the parallel pre-trends assumption; however, with [N] pre-period observations the test has limited power against smooth alternatives (Roth 2022).'",
    "Must not claim that the TWFE coefficient 'isolates the causal effect of teleworkability on informality' without acknowledging that ISCO→ENAHO occupation crosswalk errors induce classical measurement error in the treatment variable, biasing estimates toward zero (attenuation) by an unknown factor.",
    "Must not claim 'hysteresis in formality recovery' without (a) a formal structural-break or mean-reversion test at 2022–2023, and (b) explicitly ruling out that persistence reflects differential survivor bias — re-formalized workers exiting the panel at higher rates than persistently informal workers.",
    "Must not claim that Sun–Abraham estimates 'fully resolve heterogeneous treatment effects' — they correct for the specific negative-weighting problem in TWFE but still require the parallel-trends assumption and are sensitive to the choice of reference period and control group.",
    "Must not claim the Saltiel and Dingel–Neiman measures are 'consistent' without reporting their correlation and systematic divergence across occupation quartiles. Asserting consistency without this evidence is an unverifiable claim.",
    "Must not claim gender differences in treatment effects represent causal gender-differential impacts of COVID on informality without controlling for, or at minimum testing, sectoral composition differences between male and female workers in the estimation sample.",
    "Must not claim results generalize beyond Peru. The identification exploits Peru-specific mobility restriction timing, ENAHO survey design, and Peru's unusually high baseline informality (~70%). Cross-country claims require direct comparative evidence.",
    "Must not claim that non-rejection of 'attrition is random conditional on observables' implies attrition on unobservables is absent. The observable-conditional test is only informative about the variables included in the attrition probit; it is silent on latent factors like motivation or employer-worker bargaining."
  ]
}
```

---

**Key judgment calls explained:**

| Decision | Rationale |
|---|---|
| Sun–Abraham as primary, not robustness | Recovery paths are heterogeneous by construction; TWFE negative weights are not a theoretical concern here, they are near-certain |
| Clustering at occupation, not individual | Treatment is assigned at occupation×time; individual clustering is anti-conservative by 1–2 orders of magnitude in typical DiD settings |
| Wild bootstrap flagged as MUST (conditional) | ENAHO occupation groups at any useful level of aggregation likely fall below the 50-cluster threshold where asymptotic clustering is unreliable |
| Composition decomposition as MUST | Peru's employment-inactivity flows are large (~8–12 pp swing around recessions); conflating informalization with withdrawal is the most common substantive error in Peruvian labor-market DiDs |
| Saltiel as primary treatment measure | The LAC measurement-error issue is not minor — it is correlated with the outcome (skill↔informality), so D-N as primary would be a biased baseline, not a conservative one |