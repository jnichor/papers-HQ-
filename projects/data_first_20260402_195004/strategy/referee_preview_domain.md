```json
{
  "code_requirements": [
    {
      "category": "randomization_check",
      "requirement": "Produce a covariate balance table (treatment vs control) with standardized mean differences (SMD) and p-values from t-tests. Flag any covariate with SMD > 0.1 or p < 0.10 as a balance failure requiring investigation.",
      "priority": "MUST"
    },
    {
      "category": "estimation",
      "requirement": "Primary OLS specification: ICC_referral_support ~ apartheid_vs_persecution_treat + LASSO_selected_covariates, with HC2 heteroskedasticity-robust standard errors (not HC1/HC3). Report coefficient, 95% CI, and effect size in outcome SD units.",
      "priority": "MUST"
    },
    {
      "category": "estimation",
      "requirement": "LASSO covariate selection must use cross-validated lambda (cv.glmnet or sklearn equivalent with CV). Document the exact lambda chosen and how many of the 126 columns survive selection. Do NOT include post-LASSO variables mechanically; run OLS on selected set using standard SEs (Post-LASSO OLS, not LASSO coefficients directly).",
      "priority": "MUST"
    },
    {
      "category": "estimation",
      "requirement": "CATE by pro_israel_score quintile: estimate treatment effect within each quintile via OLS with quintile-x-treatment interactions. Report point estimates + 95% CIs for all five quintiles in a single table. Test joint significance of heterogeneity (F-test on interaction terms).",
      "priority": "MUST"
    },
    {
      "category": "estimation",
      "requirement": "If ICC referral support is ordinal (Likert), report both OLS and ordered probit as parallel specifications. Confirm conclusions are qualitatively identical across both; if not, explain divergence.",
      "priority": "MUST"
    },
    {
      "category": "estimation",
      "requirement": "Report unadjusted (no covariates) treatment effect alongside adjusted specification in the same table. This documents how much LASSO covariate adjustment moves the estimate — a large shift suggests residual confounding from imperfect randomization.",
      "priority": "MUST"
    },
    {
      "category": "robustness",
      "requirement": "Permutation/randomization inference: reshuffle treatment label 2000+ times and recompute the t-statistic. Report the exact p-value under sharp null. This is especially important given N=1185 which may be underpowered for small effects.",
      "priority": "MUST"
    },
    {
      "category": "robustness",
      "requirement": "Estimate CATE using a continuous interaction (treatment x pro_israel_score, centered) in addition to quintile binning. Quintile results must not reverse sign relative to the continuous specification.",
      "priority": "SHOULD"
    },
    {
      "category": "robustness",
      "requirement": "Sensitivity to outcome coding: if support is measured on a scale (e.g., 1-7), re-run primary OLS with outcome dichotomized at the median AND at 'strong support' threshold. Confirm sign and significance stability.",
      "priority": "SHOULD"
    },
    {
      "category": "robustness",
      "requirement": "Attrition/missing-data analysis: report missingness rates by treatment arm for outcome and key covariates. If differential missingness > 2% between arms, run inverse-probability-weighting (IPW) as a robustness check.",
      "priority": "SHOULD"
    },
    {
      "category": "robustness",
      "requirement": "Manipulation check / awareness covariate: if the survey includes any measure of prior familiarity with 'apartheid' terminology, include it as a moderator. Respondents who already knew the term may respond differently from naive ones — this is a referee red flag for framing experiments.",
      "priority": "SHOULD"
    },
    {
      "category": "robustness",
      "requirement": "Multiple-outcome correction: if ICC referral support is one of several outcomes tested, report Benjamini-Hochberg adjusted q-values alongside raw p-values. Even if it is the sole pre-specified primary outcome, document this explicitly.",
      "priority": "SHOULD"
    },
    {
      "category": "robustness",
      "requirement": "Exclude top and bottom 1% of pro_israel_score as outlier robustness check. Verify CATE quintile results do not hinge on extreme scorers.",
      "priority": "SHOULD"
    },
    {
      "category": "power",
      "requirement": "Report post-hoc MDE (minimum detectable effect) at 80% power given N=1185 and observed outcome variance. If the detected effect is close to the MDE, flag underpowering explicitly rather than overclaiming precision.",
      "priority": "MUST"
    },
    {
      "category": "cate_estimation",
      "requirement": "For CATE quintiles, report cell N per quintile x treatment cell. Flag any cell with N < 30 as unreliable; widen to terciles if quintile cells are too sparse.",
      "priority": "MUST"
    },
    {
      "category": "cate_estimation",
      "requirement": "Report whether the CATE monotonically increases or decreases across quintiles, or is non-monotonic. Non-monotonicity must be explicitly discussed — it changes the political economy interpretation.",
      "priority": "SHOULD"
    },
    {
      "category": "construction",
      "requirement": "Document pro_israel_score construction in code and appendix: which columns, what aggregation (sum, mean, factor score), and whether it was standardized pre- or post-analysis. If factor analysis, report Cronbach's alpha.",
      "priority": "MUST"
    },
    {
      "category": "construction",
      "requirement": "Assert that treatment assignment is binary (0/1) with no partial assignment, missing values, or third conditions. Any respondent in a third label condition (e.g., 'genocide') must be explicitly excluded or coded as control with justification.",
      "priority": "MUST"
    },
    {
      "category": "construction",
      "requirement": "Verify that casualty salience variables are balanced or held constant between arms — this is stated as a design control. Run a specific balance test on all casualty-related columns and report it in Table 1.",
      "priority": "MUST"
    },
    {
      "category": "reporting",
      "requirement": "Report Cohen's d for the main treatment effect. Editors in political psychology / public opinion journals now require standardized effect sizes, not just p-values.",
      "priority": "MUST"
    },
    {
      "category": "reporting",
      "requirement": "Include a CONSORT-style participant flow diagram: total recruited → screened out → randomized to each arm → completed outcome → analytic sample. Required for any survey experiment.",
      "priority": "SHOULD"
    }
  ],
  "data_warnings": [
    "126 columns on 1185 rows creates a 10:1 column-to-row ratio — LASSO must use cross-validation strictly; manual variable selection post-LASSO inflates false positive rates.",
    "pro_israel_score constructed from survey items may be endogenous to the treatment itself if any score items were measured post-treatment. Verify the temporal ordering in the survey instrument.",
    "Framing experiments on politically charged topics (Israel-Palestine) are prone to social desirability bias and survey satisficing — check for response time data or straight-lining patterns if available.",
    "Quintile cutpoints for pro_israel_score are sample-dependent; if computed in-sample, report the actual score thresholds so the paper is replicable.",
    "With N=1185 split across quintiles, each quintile x arm cell is ~118 observations — CATE estimates at the extremes will have wide confidence intervals and low power for detecting heterogeneity.",
    "The 'apartheid' label carries legal connotations that may interact with respondent legal literacy or news consumption; these potential confounders should be checked against available covariates.",
    "If the survey was fielded on MTurk or Prolific, report platform, completion rate, and whether attention checks were used to filter responses — reviewers in public opinion research will ask.",
    "Missing outcome data in survey experiments is rarely MCAR; test whether missingness on ICC referral support predicts treatment arm or pro_israel_score."
  ],
  "tables_required": [
    "Table 1: Covariate balance table — means by arm, SMD, p-values, with casualty-salience variables highlighted in a separate panel",
    "Table 2: Main OLS results — unadjusted, LASSO-adjusted, and ordered probit side-by-side with HC2 SEs and Cohen's d",
    "Table 3: CATE estimates by pro_israel_score quintile — point estimates, 95% CIs, cell N, F-test for heterogeneity",
    "Table 4: LASSO covariate selection summary — variables selected, their OLS coefficients in the adjusted specification",
    "Table A1 (appendix): Full OLS results with all LASSO-selected covariates reported",
    "Table A2 (appendix): Robustness to outcome coding (continuous, median-dichotomized, 'strong support' dichotomized)",
    "Table A3 (appendix): Permutation test results and IPW estimates if differential attrition is detected"
  ],
  "figures_required": [
    "Figure 1: Coefficient plot — treatment effect with 95% CI across all specifications (unadjusted, adjusted, ordered probit) on a single axis for visual comparison",
    "Figure 2: CATE by quintile — dot plot with 95% CIs across five quintiles, horizontal reference line at zero, annotated with cell N",
    "Figure 3: Distribution of pro_israel_score by treatment arm (overlaid histograms or density plots) to confirm balance on this key moderator",
    "Figure 4: Continuous CATE — predicted treatment effect as a function of pro_israel_score (continuous interaction), with pointwise confidence band"
  ]
}
```

**Top referee concerns for this design:**

1. **Endogeneity of pro_israel_score** — if any items composing that score were asked *after* the treatment vignette, the moderator is contaminated. This alone can sink the paper.

2. **Underpowered CATE** — 1185 respondents split five ways yields ~120/quintile/arm. Reviewers will note that quintile-level CATEs are underpowered; the paper needs to pre-empt this with honest MDE reporting.

3. **LASSO + inference** — using LASSO for selection and then running OLS on the same sample inflates Type I error unless Post-LASSO OLS (Belloni et al.) is implemented correctly. A reviewer familiar with double-selection LASSO will check this immediately.

4. **Manipulation check omission** — framing experiments without a comprehension or recall check get pushed back. Even one question ("What label was used to describe Israeli actions in what you just read?") would help.