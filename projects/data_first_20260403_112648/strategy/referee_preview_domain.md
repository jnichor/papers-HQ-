```json
{
  "code_requirements": [
    {
      "category": "estimation",
      "requirement": "Primary specification: OLS/LPM with the 2x2 factorial interaction — Y = α + β₁V + β₂T + β₃(V×T) + Xγ + ε. β₃ is the superadditivity test. Report all four arms' means alongside coefficients.",
      "priority": "MUST"
    },
    {
      "category": "estimation",
      "requirement": "ITT estimates as the headline. If compliance < 1, also report LATE via 2SLS using assignment dummies as instruments for actual take-up. Must clearly distinguish ITT from LATE throughout.",
      "priority": "MUST"
    },
    {
      "category": "estimation",
      "requirement": "ANCOVA specification: include baseline value of the outcome (or closest pre-treatment proxy) as a covariate. This is the efficiency-maximizing estimator for RCTs and referees will expect it.",
      "priority": "MUST"
    },
    {
      "category": "estimation",
      "requirement": "Heterogeneity analysis via triple interactions: Y = ... + δ₁(V×T×Female) + δ₂(V×T×LowSES) + all lower-order terms. Run as a single saturated model, not separate subgroup regressions.",
      "priority": "MUST"
    },
    {
      "category": "estimation",
      "requirement": "Cluster standard errors at the unit of randomization. If randomization was individual, use HC2 (not HC1) heteroskedasticity-robust SEs. Document this choice explicitly in code comments.",
      "priority": "MUST"
    },
    {
      "category": "estimation",
      "requirement": "Multiple-outcomes correction: implement Benjamini-Hochberg FDR adjustment across all primary outcome variables. Report both raw p-values and adjusted q-values in every results table.",
      "priority": "MUST"
    },
    {
      "category": "estimation",
      "requirement": "Randomization inference (permutation test) for the key β₃ interaction coefficient. Permute treatment assignment 1,000+ times within strata. Required because β₃ may be estimated imprecisely with N=2,322.",
      "priority": "MUST"
    },
    {
      "category": "estimation",
      "requirement": "Wave/period fixed effects for pooled cross-sections. Verify whether the same individuals appear in multiple waves; if so, include individual FE or note explicitly this is a pure cross-section pool.",
      "priority": "MUST"
    },
    {
      "category": "estimation",
      "requirement": "Power calculation for the interaction term β₃ ex-post. With N≈2,322 split into 4 arms (~580/arm), compute minimum detectable effect for the interaction and report it. Referees will ask.",
      "priority": "MUST"
    },
    {
      "category": "robustness",
      "requirement": "Lee (2009) trimming bounds for any outcome affected by attrition or sample selection (e.g., wages conditional on employment). Report point estimate alongside upper/lower bounds.",
      "priority": "MUST"
    },
    {
      "category": "robustness",
      "requirement": "Probit/logit marginal effects as robustness to LPM for binary outcomes. If LPM predicts outside [0,1] for any observation, flag and report the share affected.",
      "priority": "SHOULD"
    },
    {
      "category": "robustness",
      "requirement": "Specification curve: vary the control variable set (none, demographics only, full baseline controls) and show β₃ is stable. At minimum show 3 nested specifications in a single table.",
      "priority": "SHOULD"
    },
    {
      "category": "robustness",
      "requirement": "Spillover/SUTVA test: if treatment was assigned at individual level within shared labor markets, test for spillovers using Baird et al. (2018) style partial-population experiment logic or geographic distance-based analysis.",
      "priority": "SHOULD"
    },
    {
      "category": "robustness",
      "requirement": "Placebo test on pre-treatment outcomes: regress baseline variables on treatment assignment. If data structure allows a pre-period, verify β₃ ≈ 0 on pre-treatment employment.",
      "priority": "SHOULD"
    },
    {
      "category": "robustness",
      "requirement": "Winsorize continuous outcomes (wages, hours) at 1st/99th percentile. Run both winsorized and log-transformed versions. Report which is preferred and why.",
      "priority": "SHOULD"
    },
    {
      "category": "robustness",
      "requirement": "Stacked regression by cohort/wave if pooling across multiple experimental waves — do not pool naively if treatment timing differs across waves.",
      "priority": "SHOULD"
    },
    {
      "category": "data_construction",
      "requirement": "With 1,420 columns, implement explicit variable selection logic before running regressions. Document which variables are outcomes, which are controls, and which are neither. Use a data dictionary or codebook-driven column classifier.",
      "priority": "MUST"
    },
    {
      "category": "data_construction",
      "requirement": "Verify 2×2 factorial balance: each of the 4 cells (V=0/T=0, V=1/T=0, V=0/T=1, V=1/T=1) must have sufficient n. If any cell has < 100 observations, flag a power warning.",
      "priority": "MUST"
    },
    {
      "category": "data_construction",
      "requirement": "Construct a binary 'complier' indicator: individuals who received the assigned treatment. Report compliance rates by arm. If compliance is endogenous (e.g., training take-up depends on voucher), document this clearly.",
      "priority": "MUST"
    },
    {
      "category": "data_construction",
      "requirement": "Attrition analysis: regress an attrition indicator on treatment arms and baseline covariates. Test for differential attrition by treatment arm using F-test across all arms jointly.",
      "priority": "MUST"
    },
    {
      "category": "data_construction",
      "requirement": "SES index construction: if SES is derived from multiple columns, document the aggregation method (PCA, sum score, terciles). Verify the index is constructed using only pre-treatment data.",
      "priority": "MUST"
    },
    {
      "category": "data_construction",
      "requirement": "Verify no post-randomization conditioning: controls added to regressions must be pre-treatment. Flag any variable that could be a mediator (post-treatment) and exclude from main controls.",
      "priority": "MUST"
    },
    {
      "category": "data_construction",
      "requirement": "Pooled cross-section: add survey wave dummies and document whether outcomes are measured at the same point post-treatment across waves. Heterogeneous follow-up timing is a major confound.",
      "priority": "MUST"
    }
  ],
  "data_warnings": [
    "1,420 columns for 2,322 rows creates extreme multiple-testing risk. Any unrestricted search across columns will produce spurious findings. Pre-register or explicitly separate confirmatory from exploratory outcomes.",
    "Pooled cross-sections ≠ panel data. If the same individuals are tracked across waves, the correct estimator is panel FE or first-differences, NOT pooled OLS. Verify individual identifiers and test for duplicates.",
    "Factorial RCTs with unequal cell sizes (due to attrition or partial compliance) break the orthogonality assumption. Recheck balance after attrition and re-weight if necessary.",
    "With ~580 obs per arm, the interaction term β₃ is estimated from only ~580 'complements-arm' observations. The MDE for β₃ is roughly 2× larger than for main effects — low power is a real threat.",
    "Gender and SES heterogeneity via triple interactions further halves cell sizes (~290/subgroup). Report these with appropriate caveats about exploratory status and multiple testing.",
    "If training take-up was voluntary after assignment, there is a strong risk of compliance selection bias — participants who take up training when also holding a voucher may differ systematically. Model compliance explicitly.",
    "Wage/earnings outcomes are only observed for employed individuals (selected sample). Any wage analysis without Lee bounds or Heckman correction will be invalid for peer review.",
    "1,420 columns likely contain many highly correlated variables (e.g., asset indices, consumption sub-components). Avoid including collinear blocks of controls — use VIF checks or PCA-reduced control sets."
  ],
  "tables_required": [
    "Table 1: Balance table — means and SDs of baseline covariates by treatment arm (all 4 cells), with F-test p-value for joint balance. Include both individual arm tests and the interaction cell.",
    "Table 2: Attrition analysis — attrition rate by arm, regression of attrition indicator on treatment dummies with p-value for differential attrition.",
    "Table 3: Compliance table — take-up rates by assigned arm for voucher and training separately, and for the joint arm.",
    "Table 4: Main ITT results — primary employment outcomes across 3 specifications (no controls, demographics, full controls). Rows: V, T, V×T (β₃). Include arm means in panel below.",
    "Table 5: LATE estimates — 2SLS for actual take-up if compliance < 100%, with first-stage F-statistics.",
    "Table 6: Heterogeneity by gender — triple interaction estimates (V×T×Female) with all lower-order terms. Report subgroup means.",
    "Table 7: Heterogeneity by SES — triple interaction estimates (V×T×LowSES). Include SES index construction details in footnote.",
    "Table 8: Multiple outcomes — all pre-registered outcomes with raw p-values and BH-adjusted q-values. Must include employment, earnings, hours, job quality (if available).",
    "Table A1 (Appendix): Robustness — probit marginal effects, winsorized outcomes, and randomization inference p-values for β₃.",
    "Table A2 (Appendix): Lee bounds for wage/earnings outcomes showing point estimate, lower bound, and upper bound."
  ],
  "figures_required": [
    "Figure 1: CONSORT-style flow diagram — randomization → assignment → compliance → analysis sample for each of the 4 arms.",
    "Figure 2: Treatment arm means plot — bar chart with 95% CIs for the primary employment outcome across all 4 arms, with the predicted additive benchmark overlaid to visually demonstrate (or refute) superadditivity.",
    "Figure 3: Coefficient plot — β₁ (V), β₂ (T), β₃ (V×T) with 90% and 95% CIs from the main specification. Include a horizontal reference line at zero.",
    "Figure 4: Heterogeneity forest plot — β₃ estimated separately for gender × SES subgroups (4 cells), showing point estimates and CIs to visualize effect modification.",
    "Figure 5: Permutation distribution — histogram of β₃ under 1,000 random permutations with the observed β₃ marked, showing the randomization inference p-value.",
    "Figure A1 (Appendix): Specification curve for β₃ — ordered point estimates across all robustness specifications (control sets, functional forms, sample restrictions)."
  ]
}
```

**Key design-specific flags for the programmer:**

1. **The superadditivity test is the paper.** `β₃` must be reported prominently with its randomization-inference p-value, not just the asymptotic one. A negative or zero `β₃` is still a publishable finding (substitutability), so do not suppress it.

2. **Power is tight.** With ~580/arm and a typical interaction MDE of 0.15–0.20 SD, a null `β₃` is nearly uninterpretable without the ex-post power calculation. Code must compute and report MDE unconditionally.

3. **The 1,420-column problem is critical.** The code must have a hard-coded, pre-specified list of primary outcomes before any data is seen — otherwise any reported result is exploratory, not confirmatory.