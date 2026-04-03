# Referee Preview: Code Requirements Checklist

Generated: 2026-04-02T20:09:21.875174

## MUST-HAVE (30 requirements)
- [DOMAIN] randomization_check: Produce a covariate balance table (treatment vs control) with standardized mean differences (SMD) and p-values from t-tests. Flag any covariate with SMD > 0.1 or p < 0.10 as a balance failure requiring investigation.
- [DOMAIN] estimation: Primary OLS specification: ICC_referral_support ~ apartheid_vs_persecution_treat + LASSO_selected_covariates, with HC2 heteroskedasticity-robust standard errors (not HC1/HC3). Report coefficient, 95% CI, and effect size in outcome SD units.
- [DOMAIN] estimation: LASSO covariate selection must use cross-validated lambda (cv.glmnet or sklearn equivalent with CV). Document the exact lambda chosen and how many of the 126 columns survive selection. Do NOT include post-LASSO variables mechanically; run OLS on selected set using standard SEs (Post-LASSO OLS, not LASSO coefficients directly).
- [DOMAIN] estimation: CATE by pro_israel_score quintile: estimate treatment effect within each quintile via OLS with quintile-x-treatment interactions. Report point estimates + 95% CIs for all five quintiles in a single table. Test joint significance of heterogeneity (F-test on interaction terms).
- [DOMAIN] estimation: If ICC referral support is ordinal (Likert), report both OLS and ordered probit as parallel specifications. Confirm conclusions are qualitatively identical across both; if not, explain divergence.
- [DOMAIN] estimation: Report unadjusted (no covariates) treatment effect alongside adjusted specification in the same table. This documents how much LASSO covariate adjustment moves the estimate — a large shift suggests residual confounding from imperfect randomization.
- [DOMAIN] robustness: Permutation/randomization inference: reshuffle treatment label 2000+ times and recompute the t-statistic. Report the exact p-value under sharp null. This is especially important given N=1185 which may be underpowered for small effects.
- [DOMAIN] power: Report post-hoc MDE (minimum detectable effect) at 80% power given N=1185 and observed outcome variance. If the detected effect is close to the MDE, flag underpowering explicitly rather than overclaiming precision.
- [DOMAIN] cate_estimation: For CATE quintiles, report cell N per quintile x treatment cell. Flag any cell with N < 30 as unreliable; widen to terciles if quintile cells are too sparse.
- [DOMAIN] construction: Document pro_israel_score construction in code and appendix: which columns, what aggregation (sum, mean, factor score), and whether it was standardized pre- or post-analysis. If factor analysis, report Cronbach's alpha.
- [DOMAIN] construction: Assert that treatment assignment is binary (0/1) with no partial assignment, missing values, or third conditions. Any respondent in a third label condition (e.g., 'genocide') must be explicitly excluded or coded as control with justification.
- [DOMAIN] construction: Verify that casualty salience variables are balanced or held constant between arms — this is stated as a design control. Run a specific balance test on all casualty-related columns and report it in Table 1.
- [DOMAIN] reporting: Report Cohen's d for the main treatment effect. Editors in political psychology / public opinion journals now require standardized effect sizes, not just p-values.
- [METHODS] inference: Use HC2 heteroskedasticity-robust standard errors (not HC1/White) for the main OLS estimator. HC2 has better finite-sample properties than HC1 and is preferred for N~1000 experiments. Report alongside 95% CIs.
- [METHODS] inference: Apply Double/Debiased LASSO (Belloni, Chernozhukov & Hansen 2014) for post-selection inference — NOT naive post-LASSO OLS. Naive post-selection OLS produces invalid SEs and biased estimates due to omitted-variable bias from the selection step. Use 'doubleml' Python package or implement the partialling-out estimator manually.
- [METHODS] inference: For CATE estimates across pro_israel_score quintiles (5 comparisons), apply Benjamini-Hochberg FDR correction in addition to reporting unadjusted p-values. Report both. Do NOT rely solely on unadjusted p-values for the heterogeneity analysis.
- [METHODS] inference: Conduct a joint F-test (or chi-squared Wald test) for treatment effect heterogeneity across quintiles (H0: all five quintile-specific CATEs are equal). A pattern of 'some quintiles significant, some not' is NOT sufficient evidence of heterogeneity without this joint test.
- [METHODS] specification: Run a covariate balance check: regress the treatment indicator on all pre-treatment covariates and report a joint F-test (H0: all coefficients = 0). This verifies randomization integrity. A significant F-statistic is a red flag requiring investigation.
- [METHODS] specification: Check for differential attrition or non-response by treatment arm. If treatment completion rates differ, the estimand shifts from ATE to a selected population. Report completion rates per arm and test equality.
- [METHODS] specification: Report LASSO lambda selection method (cross-validation vs. BIC vs. theory-driven). For Double-LASSO, use separate LASSO for (a) regressing outcome on controls and (b) regressing treatment on controls. Document the number of covariates selected in each step.
- [METHODS] robustness: Report three specifications in a single table: (1) Raw difference in means with HC2 SEs, no controls; (2) OLS with pre-specified baseline controls only (no LASSO); (3) Double-LASSO. The coefficient stability across these three is the primary credibility check.
- [METHODS] robustness: Estimate CATE using a continuous interaction (treatment × pro_israel_score as a continuous variable) in addition to the quintile split. Report both. Quintile splits can be sensitive to binning choices and may mask or manufacture heterogeneity.
- [METHODS] presentation: Main results table must include: treatment coefficient, HC2 SE in parentheses, 95% CI in brackets, N, R², control set description, and a note on lambda selection for LASSO specifications. No asterisks without also reporting CIs.
- [METHODS] presentation: Covariate balance table must be included in the paper or appendix: columns for treatment arm, control arm, difference, and p-value of t-test. Cover all major demographic and attitudinal covariates including pro_israel_score.
- [METHODS] presentation: CATE plot: show point estimates with 95% CIs for each pro_israel_score quintile, clearly labeled. Overlay the ATE as a horizontal reference line. Use the BH-adjusted significance threshold as the decision boundary for heterogeneity claims.
- [METHODS] presentation: Report the exact wording of both treatment conditions ('apartheid' and 'persecution' labels) and the control condition in the paper body, not just the appendix. Label framing is the core mechanism — exact wording is critical for replication.
- [METHODS] pitfall: DO NOT use naive post-LASSO OLS (run LASSO, note selected variables, re-run OLS on those variables with standard HC2 SEs). This is a known error that produces anti-conservative inference. The Double-LASSO partialling-out approach is the correct procedure.
- [METHODS] pitfall: DO NOT treat the five quintile CATE estimates as independent hypothesis tests without correction. With 5 tests at alpha=0.05, expected false positives under global null = 0.25. BH correction or joint F-test is required.
- [METHODS] pitfall: DO NOT include post-treatment variables as controls in the main OLS. If pro_israel_score or any attitudinal variable could be affected by the treatment (even partially), controlling for it induces bad-control bias. Verify all LASSO covariate candidates are pre-treatment or demographic.
- [METHODS] pitfall: DO NOT interpret the treatment effect as 'apartheid label increases support more than persecution label' if the design has no pure control (no-label) arm. The coefficient measures the DIFFERENCE between the two label treatments, not the level effect of either. State the estimand precisely.

## SHOULD-HAVE (15 requirements)
- [DOMAIN] robustness: Estimate CATE using a continuous interaction (treatment x pro_israel_score, centered) in addition to quintile binning. Quintile results must not reverse sign relative to the continuous specification.
- [DOMAIN] robustness: Sensitivity to outcome coding: if support is measured on a scale (e.g., 1-7), re-run primary OLS with outcome dichotomized at the median AND at 'strong support' threshold. Confirm sign and significance stability.
- [DOMAIN] robustness: Attrition/missing-data analysis: report missingness rates by treatment arm for outcome and key covariates. If differential missingness > 2% between arms, run inverse-probability-weighting (IPW) as a robustness check.
- [DOMAIN] robustness: Manipulation check / awareness covariate: if the survey includes any measure of prior familiarity with 'apartheid' terminology, include it as a moderator. Respondents who already knew the term may respond differently from naive ones — this is a referee red flag for framing experiments.
- [DOMAIN] robustness: Multiple-outcome correction: if ICC referral support is one of several outcomes tested, report Benjamini-Hochberg adjusted q-values alongside raw p-values. Even if it is the sole pre-specified primary outcome, document this explicitly.
- [DOMAIN] robustness: Exclude top and bottom 1% of pro_israel_score as outlier robustness check. Verify CATE quintile results do not hinge on extreme scorers.
- [DOMAIN] cate_estimation: Report whether the CATE monotonically increases or decreases across quintiles, or is non-monotonic. Non-monotonicity must be explicitly discussed — it changes the political economy interpretation.
- [DOMAIN] reporting: Include a CONSORT-style participant flow diagram: total recruited → screened out → randomized to each arm → completed outcome → analytic sample. Required for any survey experiment.
- [METHODS] inference: If survey respondents were recruited in batches, waves, or via MTurk HITs with natural groupings, cluster SEs at that grouping level. If individual randomization with no natural clusters, document this explicitly and confirm HC2 suffices. Do NOT cluster arbitrarily.
- [METHODS] specification: If the ICC referral support outcome is measured on a Likert scale (e.g., 1-5 or 1-7), test whether treating it as continuous is defensible: report the empirical distribution, check for mass points at endpoints, and run ordered logit/probit as a robustness check.
- [METHODS] specification: Check variance of the outcome by treatment arm (Levene/Breusch-Pagan test). Heteroskedasticity that is correlated with treatment is theoretically expected if the treatment shifts both mean and variance of beliefs — HC2 SEs handle this but it should be documented.
- [METHODS] robustness: Placebo test: re-run the main specification with a randomly assigned pseudo-treatment (same sample size and balance) to verify the inferential procedure's Type I error rate under the null. Repeat 500+ times and confirm rejection rate ≈ 0.05.
- [METHODS] robustness: Run the main specification excluding respondents who failed attention checks or completed the survey in implausibly short time (speeders). Report N excluded and verify results are stable.
- [METHODS] robustness: Test sensitivity of CATE results to quintile cutpoint choice: re-run with terciles and quartiles. If heterogeneity patterns change substantially across binning choices, that is a major credibility concern to flag.
- [METHODS] pitfall: Avoid demand characteristic confounding: if respondents infer the researcher's intent from the label (e.g., 'apartheid' signals a more politically charged framing), the mechanism may be demand effects rather than the label per se. Discuss this limitation explicitly.

## NICE-TO-HAVE (0 requirements)

## WARNINGS
- [DATA] 126 columns on 1185 rows creates a 10:1 column-to-row ratio — LASSO must use cross-validation strictly; manual variable selection post-LASSO inflates false positive rates.
- [DATA] pro_israel_score constructed from survey items may be endogenous to the treatment itself if any score items were measured post-treatment. Verify the temporal ordering in the survey instrument.
- [DATA] Framing experiments on politically charged topics (Israel-Palestine) are prone to social desirability bias and survey satisficing — check for response time data or straight-lining patterns if available.
- [DATA] Quintile cutpoints for pro_israel_score are sample-dependent; if computed in-sample, report the actual score thresholds so the paper is replicable.
- [DATA] With N=1185 split across quintiles, each quintile x arm cell is ~118 observations — CATE estimates at the extremes will have wide confidence intervals and low power for detecting heterogeneity.
- [DATA] The 'apartheid' label carries legal connotations that may interact with respondent legal literacy or news consumption; these potential confounders should be checked against available covariates.
- [DATA] If the survey was fielded on MTurk or Prolific, report platform, completion rate, and whether attention checks were used to filter responses — reviewers in public opinion research will ask.
- [DATA] Missing outcome data in survey experiments is rarely MCAR; test whether missingness on ICC referral support predicts treatment arm or pro_israel_score.
- [METHOD] LASSO covariate selection followed by naive OLS (not Double-LASSO) is one of the most common and consequential errors in applied ML-assisted causal inference. The inferential invalidity is not cosmetic — SEs can be severely anti-conservative.
- [METHOD] With N=1185 and only two treatment arms, the study is reasonably powered for the ATE but may be underpowered for detecting heterogeneity across 5 quintile groups (each quintile ~237 observations). Pre-register a minimum detectable effect for the heterogeneity tests or explicitly acknowledge power limitations.
- [METHOD] pro_israel_score is likely a continuous composite. Quintile splitting discards within-quintile variation and may be sensitive to outliers in the tails. The continuous interaction robustness check is essential, not optional.
- [METHOD] If ICC referral support is binary or near-binary (e.g., yes/no), LPM-OLS is defensible but should be accompanied by logit/probit marginal effects as robustness. Large predicted probabilities outside [0,1] would be a warning sign.
- [METHOD] Survey experiments on politically sensitive topics (Israel-Palestine, ICC) are susceptible to social desirability bias and acquiescence bias that may be differential by treatment arm if labels prime different identity cues. Discuss as a threat to internal validity.

## MUST NOT CLAIM
- Must not claim 'apartheid label causes higher ICC support' — the estimand is the differential effect of the apartheid label *relative to* the persecution label, not a level effect versus a no-label baseline.
- Must not claim heterogeneous treatment effects exist based solely on visual inspection of quintile-specific coefficients or selectively significant quintile p-values without a joint F-test.
- Must not claim LASSO 'controls for all relevant confounders' — LASSO selects among observed covariates only. Unobserved confounders are irrelevant for the ATE if randomization holds, but the balance check must confirm this.
- Must not claim double-LASSO results are robust to model misspecification — Double-LASSO requires approximate sparsity and correct functional form assumptions. These are not guaranteed with 126 columns.
- Must not extrapolate the treatment effect to non-survey populations or non-experimental settings — the sample composition (MTurk, opt-in panel, etc.) bounds the external validity claims.

## REQUIRED TABLES
- Table 1: Covariate balance table — means by arm, SMD, p-values, with casualty-salience variables highlighted in a separate panel
- Table 2: Main OLS results — unadjusted, LASSO-adjusted, and ordered probit side-by-side with HC2 SEs and Cohen's d
- Table 3: CATE estimates by pro_israel_score quintile — point estimates, 95% CIs, cell N, F-test for heterogeneity
- Table 4: LASSO covariate selection summary — variables selected, their OLS coefficients in the adjusted specification
- Table A1 (appendix): Full OLS results with all LASSO-selected covariates reported
- Table A2 (appendix): Robustness to outcome coding (continuous, median-dichotomized, 'strong support' dichotomized)
- Table A3 (appendix): Permutation test results and IPW estimates if differential attrition is detected

## REQUIRED FIGURES
- Figure 1: Coefficient plot — treatment effect with 95% CI across all specifications (unadjusted, adjusted, ordered probit) on a single axis for visual comparison
- Figure 2: CATE by quintile — dot plot with 95% CIs across five quintiles, horizontal reference line at zero, annotated with cell N
- Figure 3: Distribution of pro_israel_score by treatment arm (overlaid histograms or density plots) to confirm balance on this key moderator
- Figure 4: Continuous CATE — predicted treatment effect as a function of pro_israel_score (continuous interaction), with pointwise confidence band