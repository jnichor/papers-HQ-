```json
{
  "code_requirements": [
    {
      "category": "specification",
      "requirement": "SUPERADDITIVITY TEST CORRECTLY SPECIFIED: The test for superadditivity is H0: β_interaction = 0 (one-sided: β_interaction > 0). The combined effect is β_voucher + β_training + β_interaction. Report these separately. Do NOT conflate 'significant combined effect' with 'significant superadditivity' — they answer different questions.",
      "priority": "MUST"
    },
    {
      "category": "specification",
      "requirement": "BALANCE TABLE ACROSS ALL FOUR ARMS: Report balance for Control / Voucher-only / Training-only / Both arms. A two-group balance table is insufficient for a 2×2 factorial. Run a joint F-test for each covariate across all arms, not just pairwise t-tests.",
      "priority": "MUST"
    },
    {
      "category": "inference",
      "requirement": "ESTABLISH RANDOMIZATION UNIT: Determine whether randomization was individual-level or cluster-level (village, firm, school). If cluster-randomized: use cluster-robust SEs at the randomization cluster level. If fewer than 50 clusters, wild cluster bootstrap (Rademacher weights, ≥999 replications) is the PRIMARY inference method — asymptotic cluster SEs are unreliable. Use 'wildboottest' Python package.",
      "priority": "MUST"
    },
    {
      "category": "specification",
      "requirement": "MULTIPLE TESTING CORRECTION: With 1420 columns against 2322 rows, the dataset is severely underdetermined and presents extreme specification-search risk. Code must pre-declare a primary outcome variable and a finite list of secondary outcomes. Apply Benjamini-Hochberg FDR correction across all tested outcomes. Flag any outcome explored post-hoc as exploratory.",
      "priority": "MUST"
    },
    {
      "category": "specification",
      "requirement": "ITT AS PRIMARY SPECIFICATION: Report Intent-to-Treat as the primary estimate. If non-compliance exists in either program, report compliance rates by arm and instrument with treatment assignment for a LATE/IV estimate. Non-compliance in one arm that is not modeled produces attenuated interaction estimates and misleads on complementarity.",
      "priority": "MUST"
    },
    {
      "category": "robustness",
      "requirement": "ATTRITION / MISSING OUTCOME ANALYSIS: For pooled cross-sections, differential attrition across arms can masquerade as treatment effects. Compute differential attrition rates by arm (joint F-test). Compute Lee (2009) trimming bounds for the primary outcome if attrition exceeds 5% in any arm.",
      "priority": "MUST"
    },
    {
      "category": "specification",
      "requirement": "HETEROGENEITY SUBGROUP REGRESSIONS: For gender and SES heterogeneity, estimate triple interactions Voucher × Training × Gender and Voucher × Training × SES in a single saturated model. Do NOT run separate regressions for each subgroup and compare p-values informally — that is not a test of differential effects.",
      "priority": "MUST"
    },
    {
      "category": "inference",
      "requirement": "INTERACTION TERM POWER: The precision of β_interaction is roughly 4× lower than the precision of main effects in balanced 2×2 designs. Report an ex-post MDE (minimum detectable effect) for the interaction term. If the MDE exceeds plausible effect sizes from the literature, explicitly caveat that the study may be underpowered to detect complementarity even if it exists.",
      "priority": "MUST"
    },
    {
      "category": "robustness",
      "requirement": "RANDOMIZATION INFERENCE / PERMUTATION TEST: Compute a permutation p-value for β_interaction by reshuffling treatment assignment within strata (≥1000 permutations). This provides exact finite-sample inference for the key quantity of interest and is especially valuable when cluster count is uncertain.",
      "priority": "SHOULD"
    },
    {
      "category": "robustness",
      "requirement": "COVARIATE ADJUSTMENT SENSITIVITY: Report (a) raw difference-in-means across 4 arms, (b) regression-adjusted estimate with pre-specified covariates, (c) LASSO-selected covariates (post-double-selection, Belloni et al.). If β_interaction is significant only under one specification, flag instability.",
      "priority": "SHOULD"
    },
    {
      "category": "robustness",
      "requirement": "SUTVA / SPILLOVER CHECK: In factorial RCTs, individuals assigned to Voucher-only may learn about or interact with Training-arm individuals, creating cross-arm contamination. If geographic or social proximity data exist, test for spillovers using a distance-to-treated-arm variable or Rosenbaum (2007) interference bounds.",
      "priority": "SHOULD"
    },
    {
      "category": "specification",
      "requirement": "SATURATED vs. ADDITIVE MODEL COMPARISON: Estimate both (a) fully saturated model with 3 dummies (V, T, V×T) and (b) a model imposing β_interaction=0. Report an F-test for the restriction. If the saturated model is not significantly better, be cautious about claiming evidence of complementarity.",
      "priority": "SHOULD"
    },
    {
      "category": "robustness",
      "requirement": "POOLED CROSS-SECTION TIMING CONTROLS: Since data are pooled cross-sections (not a panel), include survey-wave fixed effects or time-period dummies to absorb secular trends. Check whether the composition of treatment arms is stable across waves; compositional change confounds the interaction estimate.",
      "priority": "SHOULD"
    },
    {
      "category": "presentation",
      "requirement": "TABLE REQUIREMENTS: Every regression table must include: (1) β estimates for V, T, and V×T separately, (2) SEs and 95% CIs (not just stars), (3) p-value for H0: β_V + β_T + β_VT = combined effect, (4) p-value for H0: β_VT = 0 (superadditivity test), (5) N per arm, (6) R², (7) specification of SE type (HC2/HC3/cluster/wild bootstrap). Report effect sizes in standardized units (Cohen's d) alongside raw coefficients.",
      "priority": "MUST"
    },
    {
      "category": "presentation",
      "requirement": "MEANS TABLE: Include a table of raw means and SDs by arm (2×2 grid: Control, V-only, T-only, Both) for the primary outcome. This is the most transparent presentation of a factorial design and should precede any regression.",
      "priority": "MUST"
    },
    {
      "category": "presentation",
      "requirement": "HETEROGENEITY FOREST PLOT: For gender and SES subgroup results, present a coefficient plot showing β_interaction with 95% CIs by subgroup. Include a formal interaction p-value (triple interaction term) alongside subgroup-specific estimates.",
      "priority": "SHOULD"
    },
    {
      "category": "pitfall",
      "requirement": "DO NOT INTERPRET INSIGNIFICANT INTERACTION AS EVIDENCE OF ADDITIVITY: p > 0.05 for β_VT does not confirm additivity — the study may simply be underpowered. Frame null results as 'no detected superadditivity' not 'programs are additive.'",
      "priority": "MUST"
    },
    {
      "category": "pitfall",
      "requirement": "DO NOT OVER-CONTROL WITH 1420 COLUMNS: With N=2322 and 1420 variables, adding many covariates risks collinearity and post-treatment bias if any covariate is affected by treatment. Limit covariate adjustment to pre-specified baseline variables. Flag and exclude any variable measured after randomization.",
      "priority": "MUST"
    },
    {
      "category": "pitfall",
      "requirement": "DO NOT POOL SES GROUPS WITHOUT TESTING POOLABILITY: If SES is ordinal or continuous, a single interaction V×T×SES imposes linearity. Test whether the interaction effect is monotone in SES or has a non-linear pattern (e.g., J-shape). Consider tertile splits with a joint test across groups.",
      "priority": "SHOULD"
    },
    {
      "category": "pitfall",
      "requirement": "AVOID MULTIPLE INFERENCE ON SUBGROUPS WITHOUT CORRECTION: Gender × SES subgroup cells in a 2×2×K design multiply fast. With, e.g., 3 SES groups × 2 genders = 6 subgroup interaction tests on the same outcome, apply Bonferroni or Holm correction. Report uncorrected and corrected p-values side by side.",
      "priority": "MUST"
    },
    {
      "category": "inference",
      "requirement": "HC2 HETEROSKEDASTICITY-ROBUST SEs AS MINIMUM: If randomization is individual-level, use HC2 (not HC1/default OLS) robust SEs. HC2 is unbiased under heteroskedasticity and preferred over HC3 at N=2322. Standard OLS SEs are invalid by default in treatment-effect regressions.",
      "priority": "MUST"
    },
    {
      "category": "robustness",
      "requirement": "QUANTILE TREATMENT EFFECTS FOR EMPLOYMENT OUTCOME: If the employment outcome has a mass point at zero (binary or censored), also estimate QTE at the 50th, 75th, and 90th percentiles. An average effect of zero can mask positive effects at upper quantiles (program raises ceiling not floor). Use Firpo (2007) unconditional QTE or interquantile regression.",
      "priority": "NICE"
    },
    {
      "category": "robustness",
      "requirement": "CAUSAL FOREST / CATE ESTIMATION FOR HETEROGENEITY: Use a causal forest (grf package) or T-learner with cross-fitting to estimate conditional average treatment effects of the interaction. Report variable importance for which baseline characteristics moderate complementarity. This is exploratory but guards against cherry-picked subgroups.",
      "priority": "NICE"
    }
  ],
  "method_warnings": [
    "COLUMN/ROW RATIO WARNING: 1420 columns vs. 2322 rows (ratio ≈ 0.61) creates extreme risk of specification fishing. Without a pre-analysis plan, any significant β_VT result is suspect. Code must hard-code the outcome variable and covariate list at the top of the script — no dynamic selection.",
    "POOLED CROSS-SECTIONS ≠ PANEL: Cannot estimate within-person learning trajectories or use individual fixed effects. Heterogeneity in pre-treatment outcomes across waves can confound treatment effects if wave composition differs by arm.",
    "INTERACTION POWER IS LOW: A properly powered study to detect a meaningful interaction (e.g., 0.2 SD) at 80% power typically requires ~4× the sample needed for a main effect of the same size. With N=2322 split across 4 arms (~580 per arm), MDE for β_VT is likely ≥0.15–0.20 SD — document this explicitly.",
    "COMPLIANCE ASYMMETRY: Take-up rates for vocational training programs are typically lower and more endogenous than voucher take-up. If non-compliance is differential (e.g., more motivated workers take up both programs), the interaction estimate conflates program complementarity with selection complementarity.",
    "POOLED CROSS-SECTION WAVE EFFECTS: If survey waves post-date treatment assignment by different durations, the 'combined' arm may have higher or lower follow-up time than the single-program arms, confounding the interaction.",
    "BINARY EMPLOYMENT OUTCOMES: If the outcome is binary (employed/not), OLS linear probability model produces valid ATEs but the interaction term interpretation requires care — margins are not guaranteed additive on the probability scale. Consider logit margins as a robustness check, but prefer LPM as primary for interpretability of β_VT."
  ],
  "must_not_claim": [
    "Must NOT claim 'programs are complementary' based solely on a significant combined effect (β_V + β_T + β_VT > 0) — complementarity requires β_VT > 0 specifically.",
    "Must NOT claim 'no complementarity' based on a non-significant β_VT without reporting the MDE and acknowledging possible underpowering.",
    "Must NOT use the pooled cross-section structure to make within-person causal claims about learning trajectories or skill accumulation over time.",
    "Must NOT treat the 1420 columns as a covariate menu to try different specifications and report the most significant — this invalidates standard p-values entirely.",
    "Must NOT interpret subgroup heterogeneity (gender, SES) without a formal triple-interaction test — differences in subgroup-specific estimates are not statistically meaningful without an interaction test.",
    "Must NOT report only aggregate employment effects without checking for mass-at-zero in the outcome distribution — average effects on a censored outcome mask distributional shifts.",
    "Must NOT claim the RCT design eliminates all identification concerns without addressing non-compliance, attrition, and SUTVA violations specific to this factorial structure."
  ]
}
```