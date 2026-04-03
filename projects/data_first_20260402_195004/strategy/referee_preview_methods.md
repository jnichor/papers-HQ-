```json
{
  "code_requirements": [
    {
      "category": "inference",
      "requirement": "Use HC2 heteroskedasticity-robust standard errors (not HC1/White) for the main OLS estimator. HC2 has better finite-sample properties than HC1 and is preferred for N~1000 experiments. Report alongside 95% CIs.",
      "priority": "MUST"
    },
    {
      "category": "inference",
      "requirement": "Apply Double/Debiased LASSO (Belloni, Chernozhukov & Hansen 2014) for post-selection inference — NOT naive post-LASSO OLS. Naive post-selection OLS produces invalid SEs and biased estimates due to omitted-variable bias from the selection step. Use 'doubleml' Python package or implement the partialling-out estimator manually.",
      "priority": "MUST"
    },
    {
      "category": "inference",
      "requirement": "For CATE estimates across pro_israel_score quintiles (5 comparisons), apply Benjamini-Hochberg FDR correction in addition to reporting unadjusted p-values. Report both. Do NOT rely solely on unadjusted p-values for the heterogeneity analysis.",
      "priority": "MUST"
    },
    {
      "category": "inference",
      "requirement": "Conduct a joint F-test (or chi-squared Wald test) for treatment effect heterogeneity across quintiles (H0: all five quintile-specific CATEs are equal). A pattern of 'some quintiles significant, some not' is NOT sufficient evidence of heterogeneity without this joint test.",
      "priority": "MUST"
    },
    {
      "category": "inference",
      "requirement": "If survey respondents were recruited in batches, waves, or via MTurk HITs with natural groupings, cluster SEs at that grouping level. If individual randomization with no natural clusters, document this explicitly and confirm HC2 suffices. Do NOT cluster arbitrarily.",
      "priority": "SHOULD"
    },
    {
      "category": "specification",
      "requirement": "Run a covariate balance check: regress the treatment indicator on all pre-treatment covariates and report a joint F-test (H0: all coefficients = 0). This verifies randomization integrity. A significant F-statistic is a red flag requiring investigation.",
      "priority": "MUST"
    },
    {
      "category": "specification",
      "requirement": "Check for differential attrition or non-response by treatment arm. If treatment completion rates differ, the estimand shifts from ATE to a selected population. Report completion rates per arm and test equality.",
      "priority": "MUST"
    },
    {
      "category": "specification",
      "requirement": "Report LASSO lambda selection method (cross-validation vs. BIC vs. theory-driven). For Double-LASSO, use separate LASSO for (a) regressing outcome on controls and (b) regressing treatment on controls. Document the number of covariates selected in each step.",
      "priority": "MUST"
    },
    {
      "category": "specification",
      "requirement": "If the ICC referral support outcome is measured on a Likert scale (e.g., 1-5 or 1-7), test whether treating it as continuous is defensible: report the empirical distribution, check for mass points at endpoints, and run ordered logit/probit as a robustness check.",
      "priority": "SHOULD"
    },
    {
      "category": "specification",
      "requirement": "Check variance of the outcome by treatment arm (Levene/Breusch-Pagan test). Heteroskedasticity that is correlated with treatment is theoretically expected if the treatment shifts both mean and variance of beliefs — HC2 SEs handle this but it should be documented.",
      "priority": "SHOULD"
    },
    {
      "category": "robustness",
      "requirement": "Report three specifications in a single table: (1) Raw difference in means with HC2 SEs, no controls; (2) OLS with pre-specified baseline controls only (no LASSO); (3) Double-LASSO. The coefficient stability across these three is the primary credibility check.",
      "priority": "MUST"
    },
    {
      "category": "robustness",
      "requirement": "Estimate CATE using a continuous interaction (treatment × pro_israel_score as a continuous variable) in addition to the quintile split. Report both. Quintile splits can be sensitive to binning choices and may mask or manufacture heterogeneity.",
      "priority": "MUST"
    },
    {
      "category": "robustness",
      "requirement": "Placebo test: re-run the main specification with a randomly assigned pseudo-treatment (same sample size and balance) to verify the inferential procedure's Type I error rate under the null. Repeat 500+ times and confirm rejection rate ≈ 0.05.",
      "priority": "SHOULD"
    },
    {
      "category": "robustness",
      "requirement": "Run the main specification excluding respondents who failed attention checks or completed the survey in implausibly short time (speeders). Report N excluded and verify results are stable.",
      "priority": "SHOULD"
    },
    {
      "category": "robustness",
      "requirement": "Test sensitivity of CATE results to quintile cutpoint choice: re-run with terciles and quartiles. If heterogeneity patterns change substantially across binning choices, that is a major credibility concern to flag.",
      "priority": "SHOULD"
    },
    {
      "category": "presentation",
      "requirement": "Main results table must include: treatment coefficient, HC2 SE in parentheses, 95% CI in brackets, N, R², control set description, and a note on lambda selection for LASSO specifications. No asterisks without also reporting CIs.",
      "priority": "MUST"
    },
    {
      "category": "presentation",
      "requirement": "Covariate balance table must be included in the paper or appendix: columns for treatment arm, control arm, difference, and p-value of t-test. Cover all major demographic and attitudinal covariates including pro_israel_score.",
      "priority": "MUST"
    },
    {
      "category": "presentation",
      "requirement": "CATE plot: show point estimates with 95% CIs for each pro_israel_score quintile, clearly labeled. Overlay the ATE as a horizontal reference line. Use the BH-adjusted significance threshold as the decision boundary for heterogeneity claims.",
      "priority": "MUST"
    },
    {
      "category": "presentation",
      "requirement": "Report the exact wording of both treatment conditions ('apartheid' and 'persecution' labels) and the control condition in the paper body, not just the appendix. Label framing is the core mechanism — exact wording is critical for replication.",
      "priority": "MUST"
    },
    {
      "category": "pitfall",
      "requirement": "DO NOT use naive post-LASSO OLS (run LASSO, note selected variables, re-run OLS on those variables with standard HC2 SEs). This is a known error that produces anti-conservative inference. The Double-LASSO partialling-out approach is the correct procedure.",
      "priority": "MUST"
    },
    {
      "category": "pitfall",
      "requirement": "DO NOT treat the five quintile CATE estimates as independent hypothesis tests without correction. With 5 tests at alpha=0.05, expected false positives under global null = 0.25. BH correction or joint F-test is required.",
      "priority": "MUST"
    },
    {
      "category": "pitfall",
      "requirement": "DO NOT include post-treatment variables as controls in the main OLS. If pro_israel_score or any attitudinal variable could be affected by the treatment (even partially), controlling for it induces bad-control bias. Verify all LASSO covariate candidates are pre-treatment or demographic.",
      "priority": "MUST"
    },
    {
      "category": "pitfall",
      "requirement": "DO NOT interpret the treatment effect as 'apartheid label increases support more than persecution label' if the design has no pure control (no-label) arm. The coefficient measures the DIFFERENCE between the two label treatments, not the level effect of either. State the estimand precisely.",
      "priority": "MUST"
    },
    {
      "category": "pitfall",
      "requirement": "Avoid demand characteristic confounding: if respondents infer the researcher's intent from the label (e.g., 'apartheid' signals a more politically charged framing), the mechanism may be demand effects rather than the label per se. Discuss this limitation explicitly.",
      "priority": "SHOULD"
    }
  ],
  "method_warnings": [
    "LASSO covariate selection followed by naive OLS (not Double-LASSO) is one of the most common and consequential errors in applied ML-assisted causal inference. The inferential invalidity is not cosmetic — SEs can be severely anti-conservative.",
    "With N=1185 and only two treatment arms, the study is reasonably powered for the ATE but may be underpowered for detecting heterogeneity across 5 quintile groups (each quintile ~237 observations). Pre-register a minimum detectable effect for the heterogeneity tests or explicitly acknowledge power limitations.",
    "pro_israel_score is likely a continuous composite. Quintile splitting discards within-quintile variation and may be sensitive to outliers in the tails. The continuous interaction robustness check is essential, not optional.",
    "If ICC referral support is binary or near-binary (e.g., yes/no), LPM-OLS is defensible but should be accompanied by logit/probit marginal effects as robustness. Large predicted probabilities outside [0,1] would be a warning sign.",
    "Survey experiments on politically sensitive topics (Israel-Palestine, ICC) are susceptible to social desirability bias and acquiescence bias that may be differential by treatment arm if labels prime different identity cues. Discuss as a threat to internal validity."
  ],
  "must_not_claim": [
    "Must not claim 'apartheid label causes higher ICC support' — the estimand is the differential effect of the apartheid label *relative to* the persecution label, not a level effect versus a no-label baseline.",
    "Must not claim heterogeneous treatment effects exist based solely on visual inspection of quintile-specific coefficients or selectively significant quintile p-values without a joint F-test.",
    "Must not claim LASSO 'controls for all relevant confounders' — LASSO selects among observed covariates only. Unobserved confounders are irrelevant for the ATE if randomization holds, but the balance check must confirm this.",
    "Must not claim double-LASSO results are robust to model misspecification — Double-LASSO requires approximate sparsity and correct functional form assumptions. These are not guaranteed with 126 columns.",
    "Must not extrapolate the treatment effect to non-survey populations or non-experimental settings — the sample composition (MTurk, opt-in panel, etc.) bounds the external validity claims."
  ]
}
```

**Key priorities summary:**

| # | Issue | Why critical |
|---|-------|-------------|
| 1 | Double-LASSO, not post-LASSO OLS | Naive post-selection inference is invalid — SEs are wrong |
| 2 | Joint F-test on CATE heterogeneity | 5 quintile tests at α=0.05 → expected 0.25 false positives |
| 3 | Covariate balance table | Validates randomization; without it, the causal claim is unverified |
| 4 | Estimand clarity | The coefficient measures **apartheid vs. persecution**, not label vs. no-label |
| 5 | No post-treatment controls in LASSO candidate set | Bad-control bias is irreversible post-estimation |