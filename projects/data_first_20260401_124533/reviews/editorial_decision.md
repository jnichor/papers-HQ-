```json
{
  "avg_referee_score": 62.5,
  "must_address": [
    "Sign reversal between TWFE (Table 1: fair trial bust β = −0.199) and event-study bust average (Table 2: +0.489): opposite sign and larger magnitude in the same specification. Authors must either identify a coding/labeling error and correct it, or provide a substantive reconciliation (e.g., reference-period normalization at t=−1 driving bias). Until resolved, the empirical claims of the paper rest on inconsistent estimates. [ADDRESSABLE only if traceable to a correctable error; otherwise FATAL]",
    "Staggered DiD not addressed: The paper applies TWFE to 31 episodes with heterogeneous timing but never engages with Goodman-Bacon (2021), Callaway-Sant'Anna (2021), or Sun-Abraham (2021). Given the paper's own emphasis on heterogeneous and time-varying treatment effects, this omission is internally inconsistent. Authors must either implement a heterogeneity-robust estimator or provide a detailed defense of TWFE with diagnostics (e.g., Bacon decomposition, share of negative weights).",
    "Symmetry test mischaracterized in narrative: For assembly, religion, and fair trial, both bust and recovery event-study averages are positive — this constitutes asymmetric improvement, not a ratchet. The ratchet pattern (deterioration during bust, incomplete restoration during recovery) is supported only for freedom of movement. Abstract, introduction, and conclusion must be revised to accurately characterize which liberties exhibit the ratchet and which do not.",
    "Sample period inconsistency and COVID-19 confounding: The paper must clarify whether the estimation sample ends in 2018 or 2024. If post-2018 data are included, the 2020 COVID-19 emergency movement restrictions constitute a large, policy-driven confounder for exactly the liberty dimension (freedom of movement) identified as exhibiting the ratchet. A robustness check excluding 2020–2021 is required."
  ],
  "should_address": [
    "Multiple testing correction: The two headline results (fair trial p = 0.020, movement symmetry p = 0.029) do not survive Bonferroni correction across 10 joint tests. Authors should report Benjamini-Hochberg FDR-adjusted p-values and discuss sensitivity of conclusions to the correction procedure.",
    "Wild cluster bootstrap inference: With 80 country clusters and as few as 21 recovery episodes, cluster-robust standard errors may be unrereliable. Wild cluster bootstrap (Roodman et al. 2019) should be reported alongside the baseline SEs, particularly for near-threshold results.",
    "Permutation placebo tests for the wrong outcomes: The reported placebo is for freedom of expression, which is already insignificant in TWFE. Placebo tests should instead be reported for fair trial and freedom of movement — the outcomes that drive the paper's conclusions."
  ],
  "may_address": [
    "Discussion of episode selection criteria and potential endogeneity in identifying bust/recovery episodes (e.g., whether countries with worse baseline institutions are more likely to have detectable episodes, affecting external validity).",
    "Heterogeneity analysis by region, income group, or regime type to characterize for which countries the ratchet mechanism is most operative.",
    "Clarification of how the CTOT index aggregates across liberty dimensions and whether index-level vs. dimension-level analysis would yield different conclusions."
  ],
  "fatal_issues": [
    "Sign reversal on fair trial between Table 1 and Table 2 is conditionally fatal: if it cannot be attributed to a correctable coding or labeling error and reconciled with a coherent interpretation, the core empirical apparatus of the paper is unreliable and the paper cannot be published in its current form."
  ]
}
```

**Editorial note for handling:** The average score of 62.5 is below the threshold for routine advancement, and one conditionally fatal issue is flagged. The recommended editorial action is **Revise and Resubmit** contingent on resolution of the sign-reversal inconsistency — which, if it proves irreconcilable, would convert to a desk reject. Authors should be given explicit notice that the revision must include a point-by-point response on all `must_address` items before the paper will be re-reviewed.