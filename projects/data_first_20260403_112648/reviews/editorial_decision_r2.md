```json
{
  "avg_referee_score": 72.0,
  "must_address": [
    "Systematic numerical discrepancies between paper tables and underlying data/code outputs across multiple outcomes (mean age, control N, end_lfp interaction, end_salary coefficients, midline/endline N). Authors must submit a versioned replication package and reconcile every reported statistic against a single, locked dataset. Until resolved, reported effect sizes cannot be trusted.",
    "Education variable is an ordinal 1–8 scale (mean ~4.5) but is labeled and described as 'years of education' (mean ~11.8) in the balance table. This is a factual misrepresentation that must be corrected with proper variable documentation throughout.",
    "975 observations (~42% of full dataset) excluded for missing treatment assignment with no explanation. Authors must characterize who these individuals are, test whether exclusion is exogenous, and assess sensitivity of main results to alternative inclusion rules.",
    "Sample size increases from midline (N≈1,207) to endline (N≈1,255), inconsistent with standard panel attrition. The mechanism (re-contact, refreshment sample, administrative additions) must be explained and its implications for the panel estimates assessed.",
    "No compliance or take-up rates are reported and no LATE/TOT estimates are provided, despite being planned in the research strategy. ITT estimates must be accompanied by LATE estimates via 2SLS; cost-effectiveness claims are uninterpretable without per-complier scaling.",
    "The 29 percentage-point decline in control-group LFP from midline (77.1%) to endline (48.0%) is larger than the persistent treatment effect itself and is never explained. Authors must rule out survey artifacts, seasonal confounds, and differential attrition as drivers before the headline LFP persistence result is interpretable."
  ],
  "should_address": [
    "Provide an explicit discussion of SUTVA and potential general-equilibrium / displacement effects. With ~600 treated individuals concentrated in local Jordanian labor markets and a Cohen's d of ~0.88 at midline, the question of net vs. redistributive employment creation is material to the paper's welfare conclusions.",
    "State the Tawjihi pass-rate threshold used to construct the binary variable from the continuous exam-score variable, and document all variable construction decisions in a data appendix.",
    "Clarify and reconcile control arm sample sizes across balance table, midline, and endline regressions; discrepancies (~300–400 in paper vs. ~440–449 in data) undermine confidence in the randomization checks."
  ],
  "may_address": [
    "Discuss heterogeneous treatment effects by pre-specified subgroups (e.g., education level, prior work experience) if sample power permits, given the policy relevance of targeting.",
    "Reframe cost-effectiveness language as preliminary/ITT-based pending LATE estimates, to avoid overstating the magnitude of the per-complier return."
  ],
  "fatal_issues": []
}
```

**Editorial note:** No single issue is classified as fatal in isolation, but the combination of (a) pervasive numerical discrepancies across multiple tables and (b) 42% unexplained exclusions creates a reproducibility concern serious enough that the paper should not advance to a second round without a verified replication package. If the discrepancies cannot be reconciled with a single locked dataset, the paper should be desk-rejected at that stage.