# Referee Preview: Code Requirements Checklist

Generated: 2026-04-03T11:51:19.353888

## MUST-HAVE (31 requirements)
- [DOMAIN] estimation: Primary specification: OLS/LPM with the 2x2 factorial interaction — Y = α + β₁V + β₂T + β₃(V×T) + Xγ + ε. β₃ is the superadditivity test. Report all four arms' means alongside coefficients.
- [DOMAIN] estimation: ITT estimates as the headline. If compliance < 1, also report LATE via 2SLS using assignment dummies as instruments for actual take-up. Must clearly distinguish ITT from LATE throughout.
- [DOMAIN] estimation: ANCOVA specification: include baseline value of the outcome (or closest pre-treatment proxy) as a covariate. This is the efficiency-maximizing estimator for RCTs and referees will expect it.
- [DOMAIN] estimation: Heterogeneity analysis via triple interactions: Y = ... + δ₁(V×T×Female) + δ₂(V×T×LowSES) + all lower-order terms. Run as a single saturated model, not separate subgroup regressions.
- [DOMAIN] estimation: Cluster standard errors at the unit of randomization. If randomization was individual, use HC2 (not HC1) heteroskedasticity-robust SEs. Document this choice explicitly in code comments.
- [DOMAIN] estimation: Multiple-outcomes correction: implement Benjamini-Hochberg FDR adjustment across all primary outcome variables. Report both raw p-values and adjusted q-values in every results table.
- [DOMAIN] estimation: Randomization inference (permutation test) for the key β₃ interaction coefficient. Permute treatment assignment 1,000+ times within strata. Required because β₃ may be estimated imprecisely with N=2,322.
- [DOMAIN] estimation: Wave/period fixed effects for pooled cross-sections. Verify whether the same individuals appear in multiple waves; if so, include individual FE or note explicitly this is a pure cross-section pool.
- [DOMAIN] estimation: Power calculation for the interaction term β₃ ex-post. With N≈2,322 split into 4 arms (~580/arm), compute minimum detectable effect for the interaction and report it. Referees will ask.
- [DOMAIN] robustness: Lee (2009) trimming bounds for any outcome affected by attrition or sample selection (e.g., wages conditional on employment). Report point estimate alongside upper/lower bounds.
- [DOMAIN] data_construction: With 1,420 columns, implement explicit variable selection logic before running regressions. Document which variables are outcomes, which are controls, and which are neither. Use a data dictionary or codebook-driven column classifier.
- [DOMAIN] data_construction: Verify 2×2 factorial balance: each of the 4 cells (V=0/T=0, V=1/T=0, V=0/T=1, V=1/T=1) must have sufficient n. If any cell has < 100 observations, flag a power warning.
- [DOMAIN] data_construction: Construct a binary 'complier' indicator: individuals who received the assigned treatment. Report compliance rates by arm. If compliance is endogenous (e.g., training take-up depends on voucher), document this clearly.
- [DOMAIN] data_construction: Attrition analysis: regress an attrition indicator on treatment arms and baseline covariates. Test for differential attrition by treatment arm using F-test across all arms jointly.
- [DOMAIN] data_construction: SES index construction: if SES is derived from multiple columns, document the aggregation method (PCA, sum score, terciles). Verify the index is constructed using only pre-treatment data.
- [DOMAIN] data_construction: Verify no post-randomization conditioning: controls added to regressions must be pre-treatment. Flag any variable that could be a mediator (post-treatment) and exclude from main controls.
- [DOMAIN] data_construction: Pooled cross-section: add survey wave dummies and document whether outcomes are measured at the same point post-treatment across waves. Heterogeneous follow-up timing is a major confound.
- [METHODS] specification: SUPERADDITIVITY TEST CORRECTLY SPECIFIED: The test for superadditivity is H0: β_interaction = 0 (one-sided: β_interaction > 0). The combined effect is β_voucher + β_training + β_interaction. Report these separately. Do NOT conflate 'significant combined effect' with 'significant superadditivity' — they answer different questions.
- [METHODS] specification: BALANCE TABLE ACROSS ALL FOUR ARMS: Report balance for Control / Voucher-only / Training-only / Both arms. A two-group balance table is insufficient for a 2×2 factorial. Run a joint F-test for each covariate across all arms, not just pairwise t-tests.
- [METHODS] inference: ESTABLISH RANDOMIZATION UNIT: Determine whether randomization was individual-level or cluster-level (village, firm, school). If cluster-randomized: use cluster-robust SEs at the randomization cluster level. If fewer than 50 clusters, wild cluster bootstrap (Rademacher weights, ≥999 replications) is the PRIMARY inference method — asymptotic cluster SEs are unreliable. Use 'wildboottest' Python package.
- [METHODS] specification: MULTIPLE TESTING CORRECTION: With 1420 columns against 2322 rows, the dataset is severely underdetermined and presents extreme specification-search risk. Code must pre-declare a primary outcome variable and a finite list of secondary outcomes. Apply Benjamini-Hochberg FDR correction across all tested outcomes. Flag any outcome explored post-hoc as exploratory.
- [METHODS] specification: ITT AS PRIMARY SPECIFICATION: Report Intent-to-Treat as the primary estimate. If non-compliance exists in either program, report compliance rates by arm and instrument with treatment assignment for a LATE/IV estimate. Non-compliance in one arm that is not modeled produces attenuated interaction estimates and misleads on complementarity.
- [METHODS] robustness: ATTRITION / MISSING OUTCOME ANALYSIS: For pooled cross-sections, differential attrition across arms can masquerade as treatment effects. Compute differential attrition rates by arm (joint F-test). Compute Lee (2009) trimming bounds for the primary outcome if attrition exceeds 5% in any arm.
- [METHODS] specification: HETEROGENEITY SUBGROUP REGRESSIONS: For gender and SES heterogeneity, estimate triple interactions Voucher × Training × Gender and Voucher × Training × SES in a single saturated model. Do NOT run separate regressions for each subgroup and compare p-values informally — that is not a test of differential effects.
- [METHODS] inference: INTERACTION TERM POWER: The precision of β_interaction is roughly 4× lower than the precision of main effects in balanced 2×2 designs. Report an ex-post MDE (minimum detectable effect) for the interaction term. If the MDE exceeds plausible effect sizes from the literature, explicitly caveat that the study may be underpowered to detect complementarity even if it exists.
- [METHODS] presentation: TABLE REQUIREMENTS: Every regression table must include: (1) β estimates for V, T, and V×T separately, (2) SEs and 95% CIs (not just stars), (3) p-value for H0: β_V + β_T + β_VT = combined effect, (4) p-value for H0: β_VT = 0 (superadditivity test), (5) N per arm, (6) R², (7) specification of SE type (HC2/HC3/cluster/wild bootstrap). Report effect sizes in standardized units (Cohen's d) alongside raw coefficients.
- [METHODS] presentation: MEANS TABLE: Include a table of raw means and SDs by arm (2×2 grid: Control, V-only, T-only, Both) for the primary outcome. This is the most transparent presentation of a factorial design and should precede any regression.
- [METHODS] pitfall: DO NOT INTERPRET INSIGNIFICANT INTERACTION AS EVIDENCE OF ADDITIVITY: p > 0.05 for β_VT does not confirm additivity — the study may simply be underpowered. Frame null results as 'no detected superadditivity' not 'programs are additive.'
- [METHODS] pitfall: DO NOT OVER-CONTROL WITH 1420 COLUMNS: With N=2322 and 1420 variables, adding many covariates risks collinearity and post-treatment bias if any covariate is affected by treatment. Limit covariate adjustment to pre-specified baseline variables. Flag and exclude any variable measured after randomization.
- [METHODS] pitfall: AVOID MULTIPLE INFERENCE ON SUBGROUPS WITHOUT CORRECTION: Gender × SES subgroup cells in a 2×2×K design multiply fast. With, e.g., 3 SES groups × 2 genders = 6 subgroup interaction tests on the same outcome, apply Bonferroni or Holm correction. Report uncorrected and corrected p-values side by side.
- [METHODS] inference: HC2 HETEROSKEDASTICITY-ROBUST SEs AS MINIMUM: If randomization is individual-level, use HC2 (not HC1/default OLS) robust SEs. HC2 is unbiased under heteroskedasticity and preferred over HC3 at N=2322. Standard OLS SEs are invalid by default in treatment-effect regressions.

## SHOULD-HAVE (13 requirements)
- [DOMAIN] robustness: Probit/logit marginal effects as robustness to LPM for binary outcomes. If LPM predicts outside [0,1] for any observation, flag and report the share affected.
- [DOMAIN] robustness: Specification curve: vary the control variable set (none, demographics only, full baseline controls) and show β₃ is stable. At minimum show 3 nested specifications in a single table.
- [DOMAIN] robustness: Spillover/SUTVA test: if treatment was assigned at individual level within shared labor markets, test for spillovers using Baird et al. (2018) style partial-population experiment logic or geographic distance-based analysis.
- [DOMAIN] robustness: Placebo test on pre-treatment outcomes: regress baseline variables on treatment assignment. If data structure allows a pre-period, verify β₃ ≈ 0 on pre-treatment employment.
- [DOMAIN] robustness: Winsorize continuous outcomes (wages, hours) at 1st/99th percentile. Run both winsorized and log-transformed versions. Report which is preferred and why.
- [DOMAIN] robustness: Stacked regression by cohort/wave if pooling across multiple experimental waves — do not pool naively if treatment timing differs across waves.
- [METHODS] robustness: RANDOMIZATION INFERENCE / PERMUTATION TEST: Compute a permutation p-value for β_interaction by reshuffling treatment assignment within strata (≥1000 permutations). This provides exact finite-sample inference for the key quantity of interest and is especially valuable when cluster count is uncertain.
- [METHODS] robustness: COVARIATE ADJUSTMENT SENSITIVITY: Report (a) raw difference-in-means across 4 arms, (b) regression-adjusted estimate with pre-specified covariates, (c) LASSO-selected covariates (post-double-selection, Belloni et al.). If β_interaction is significant only under one specification, flag instability.
- [METHODS] robustness: SUTVA / SPILLOVER CHECK: In factorial RCTs, individuals assigned to Voucher-only may learn about or interact with Training-arm individuals, creating cross-arm contamination. If geographic or social proximity data exist, test for spillovers using a distance-to-treated-arm variable or Rosenbaum (2007) interference bounds.
- [METHODS] specification: SATURATED vs. ADDITIVE MODEL COMPARISON: Estimate both (a) fully saturated model with 3 dummies (V, T, V×T) and (b) a model imposing β_interaction=0. Report an F-test for the restriction. If the saturated model is not significantly better, be cautious about claiming evidence of complementarity.
- [METHODS] robustness: POOLED CROSS-SECTION TIMING CONTROLS: Since data are pooled cross-sections (not a panel), include survey-wave fixed effects or time-period dummies to absorb secular trends. Check whether the composition of treatment arms is stable across waves; compositional change confounds the interaction estimate.
- [METHODS] presentation: HETEROGENEITY FOREST PLOT: For gender and SES subgroup results, present a coefficient plot showing β_interaction with 95% CIs by subgroup. Include a formal interaction p-value (triple interaction term) alongside subgroup-specific estimates.
- [METHODS] pitfall: DO NOT POOL SES GROUPS WITHOUT TESTING POOLABILITY: If SES is ordinal or continuous, a single interaction V×T×SES imposes linearity. Test whether the interaction effect is monotone in SES or has a non-linear pattern (e.g., J-shape). Consider tertile splits with a joint test across groups.

## NICE-TO-HAVE (2 requirements)
- [METHODS] robustness: QUANTILE TREATMENT EFFECTS FOR EMPLOYMENT OUTCOME: If the employment outcome has a mass point at zero (binary or censored), also estimate QTE at the 50th, 75th, and 90th percentiles. An average effect of zero can mask positive effects at upper quantiles (program raises ceiling not floor). Use Firpo (2007) unconditional QTE or interquantile regression.
- [METHODS] robustness: CAUSAL FOREST / CATE ESTIMATION FOR HETEROGENEITY: Use a causal forest (grf package) or T-learner with cross-fitting to estimate conditional average treatment effects of the interaction. Report variable importance for which baseline characteristics moderate complementarity. This is exploratory but guards against cherry-picked subgroups.

## WARNINGS
- [DATA] 1,420 columns for 2,322 rows creates extreme multiple-testing risk. Any unrestricted search across columns will produce spurious findings. Pre-register or explicitly separate confirmatory from exploratory outcomes.
- [DATA] Pooled cross-sections ≠ panel data. If the same individuals are tracked across waves, the correct estimator is panel FE or first-differences, NOT pooled OLS. Verify individual identifiers and test for duplicates.
- [DATA] Factorial RCTs with unequal cell sizes (due to attrition or partial compliance) break the orthogonality assumption. Recheck balance after attrition and re-weight if necessary.
- [DATA] With ~580 obs per arm, the interaction term β₃ is estimated from only ~580 'complements-arm' observations. The MDE for β₃ is roughly 2× larger than for main effects — low power is a real threat.
- [DATA] Gender and SES heterogeneity via triple interactions further halves cell sizes (~290/subgroup). Report these with appropriate caveats about exploratory status and multiple testing.
- [DATA] If training take-up was voluntary after assignment, there is a strong risk of compliance selection bias — participants who take up training when also holding a voucher may differ systematically. Model compliance explicitly.
- [DATA] Wage/earnings outcomes are only observed for employed individuals (selected sample). Any wage analysis without Lee bounds or Heckman correction will be invalid for peer review.
- [DATA] 1,420 columns likely contain many highly correlated variables (e.g., asset indices, consumption sub-components). Avoid including collinear blocks of controls — use VIF checks or PCA-reduced control sets.
- [METHOD] COLUMN/ROW RATIO WARNING: 1420 columns vs. 2322 rows (ratio ≈ 0.61) creates extreme risk of specification fishing. Without a pre-analysis plan, any significant β_VT result is suspect. Code must hard-code the outcome variable and covariate list at the top of the script — no dynamic selection.
- [METHOD] POOLED CROSS-SECTIONS ≠ PANEL: Cannot estimate within-person learning trajectories or use individual fixed effects. Heterogeneity in pre-treatment outcomes across waves can confound treatment effects if wave composition differs by arm.
- [METHOD] INTERACTION POWER IS LOW: A properly powered study to detect a meaningful interaction (e.g., 0.2 SD) at 80% power typically requires ~4× the sample needed for a main effect of the same size. With N=2322 split across 4 arms (~580 per arm), MDE for β_VT is likely ≥0.15–0.20 SD — document this explicitly.
- [METHOD] COMPLIANCE ASYMMETRY: Take-up rates for vocational training programs are typically lower and more endogenous than voucher take-up. If non-compliance is differential (e.g., more motivated workers take up both programs), the interaction estimate conflates program complementarity with selection complementarity.
- [METHOD] POOLED CROSS-SECTION WAVE EFFECTS: If survey waves post-date treatment assignment by different durations, the 'combined' arm may have higher or lower follow-up time than the single-program arms, confounding the interaction.
- [METHOD] BINARY EMPLOYMENT OUTCOMES: If the outcome is binary (employed/not), OLS linear probability model produces valid ATEs but the interaction term interpretation requires care — margins are not guaranteed additive on the probability scale. Consider logit margins as a robustness check, but prefer LPM as primary for interpretability of β_VT.

## MUST NOT CLAIM
- Must NOT claim 'programs are complementary' based solely on a significant combined effect (β_V + β_T + β_VT > 0) — complementarity requires β_VT > 0 specifically.
- Must NOT claim 'no complementarity' based on a non-significant β_VT without reporting the MDE and acknowledging possible underpowering.
- Must NOT use the pooled cross-section structure to make within-person causal claims about learning trajectories or skill accumulation over time.
- Must NOT treat the 1420 columns as a covariate menu to try different specifications and report the most significant — this invalidates standard p-values entirely.
- Must NOT interpret subgroup heterogeneity (gender, SES) without a formal triple-interaction test — differences in subgroup-specific estimates are not statistically meaningful without an interaction test.
- Must NOT report only aggregate employment effects without checking for mass-at-zero in the outcome distribution — average effects on a censored outcome mask distributional shifts.
- Must NOT claim the RCT design eliminates all identification concerns without addressing non-compliance, attrition, and SUTVA violations specific to this factorial structure.

## REQUIRED TABLES
- Table 1: Balance table — means and SDs of baseline covariates by treatment arm (all 4 cells), with F-test p-value for joint balance. Include both individual arm tests and the interaction cell.
- Table 2: Attrition analysis — attrition rate by arm, regression of attrition indicator on treatment dummies with p-value for differential attrition.
- Table 3: Compliance table — take-up rates by assigned arm for voucher and training separately, and for the joint arm.
- Table 4: Main ITT results — primary employment outcomes across 3 specifications (no controls, demographics, full controls). Rows: V, T, V×T (β₃). Include arm means in panel below.
- Table 5: LATE estimates — 2SLS for actual take-up if compliance < 100%, with first-stage F-statistics.
- Table 6: Heterogeneity by gender — triple interaction estimates (V×T×Female) with all lower-order terms. Report subgroup means.
- Table 7: Heterogeneity by SES — triple interaction estimates (V×T×LowSES). Include SES index construction details in footnote.
- Table 8: Multiple outcomes — all pre-registered outcomes with raw p-values and BH-adjusted q-values. Must include employment, earnings, hours, job quality (if available).
- Table A1 (Appendix): Robustness — probit marginal effects, winsorized outcomes, and randomization inference p-values for β₃.
- Table A2 (Appendix): Lee bounds for wage/earnings outcomes showing point estimate, lower bound, and upper bound.

## REQUIRED FIGURES
- Figure 1: CONSORT-style flow diagram — randomization → assignment → compliance → analysis sample for each of the 4 arms.
- Figure 2: Treatment arm means plot — bar chart with 95% CIs for the primary employment outcome across all 4 arms, with the predicted additive benchmark overlaid to visually demonstrate (or refute) superadditivity.
- Figure 3: Coefficient plot — β₁ (V), β₂ (T), β₃ (V×T) with 90% and 95% CIs from the main specification. Include a horizontal reference line at zero.
- Figure 4: Heterogeneity forest plot — β₃ estimated separately for gender × SES subgroups (4 cells), showing point estimates and CIs to visualize effect modification.
- Figure 5: Permutation distribution — histogram of β₃ under 1,000 random permutations with the observed β₃ marked, showing the randomization inference p-value.
- Figure A1 (Appendix): Specification curve for β₃ — ordered point estimates across all robustness specifications (control sets, functional forms, sample restrictions).

## AVAILABLE PYTHON ESTIMATORS (verified on real data)
These estimators were tested on the actual dataset and work:
- pyfixest
- linearmodels
- csdid

These FAILED and must NOT be used:
- pyfixest feols failed: zero-size array to reduction operation maximum which has no identity