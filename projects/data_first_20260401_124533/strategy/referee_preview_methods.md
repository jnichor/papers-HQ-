```json
{
  "code_requirements": [
    {
      "category": "inference",
      "requirement": "Cluster standard errors at the country level (primary unit of treatment assignment). Report the number of clusters prominently in every table. If the effective cluster count for any subsample falls below 50, switch to wild cluster bootstrap (Rademacher weights, 999+ replications, 'wildboottest' Python or 'boottest' Stata) as the PRIMARY inference method — asymptotic cluster-robust SEs are unreliable below this threshold.",
      "priority": "MUST"
    },
    {
      "category": "inference",
      "requirement": "As secondary robustness, report two-way cluster-robust SEs (country × year) to absorb potential cross-sectional correlation in commodity price shocks that transmit to multiple countries simultaneously. Compare with one-way country clustering; if they diverge substantially, flag temporal correlation as an issue.",
      "priority": "SHOULD"
    },
    {
      "category": "inference",
      "requirement": "For the joint symmetry test (H0: bust-period event-study coefficients = −recovery-period coefficients at each horizon τ), report a Wald statistic with cluster-robust variance. This is the paper's core inferential claim — use a stacked Seemingly Unrelated Regression (SUR) or delta-method approach to construct the joint test across all post-event horizons simultaneously, not horizon-by-horizon t-tests alone.",
      "priority": "MUST"
    },
    {
      "category": "specification",
      "requirement": "PRE-TREND TEST (bust episodes): Run a joint F-test on all pre-bust event-time coefficients (τ = −k, …, −2), with τ = −1 as the omitted reference. Report the chi-squared statistic, degrees of freedom, and p-value. H0: all pre-period bust coefficients = 0. Failure to reject is necessary (not sufficient) for identifying bust effects.",
      "priority": "MUST"
    },
    {
      "category": "specification",
      "requirement": "PRE-TREND TEST (recovery episodes): Run the same joint F-test on pre-recovery event-time coefficients. Recovery episodes have their own identification assumption — the parallel-trends condition must hold separately for the recovery window, not just for the bust window.",
      "priority": "MUST"
    },
    {
      "category": "specification",
      "requirement": "Roth (2022) sensitivity analysis: use the 'HonestDiD' package to report how large a linear pre-trend would need to be to overturn the bust and recovery estimates. Report the breakdown value (M*) for each. This quantifies how much pre-trend power you actually have given the data.",
      "priority": "MUST"
    },
    {
      "category": "specification",
      "requirement": "HETEROGENEITY-ROBUST ESTIMATOR: Because bust and recovery episodes onset at different calendar times across countries (staggered treatment), standard TWFE can assign negative weights to some group-time ATTs and produce sign-reversed estimates. Implement Sun & Abraham (2021) interaction-weighted estimator (or Callaway & Sant'Anna 2021) for BOTH the bust and recovery event studies. Report TWFE and the heterogeneity-robust estimate side by side; flag any sign divergence.",
      "priority": "MUST"
    },
    {
      "category": "specification",
      "requirement": "PLACEBO TEST — false timing: Shift all bust episode start dates by T years (e.g., T = −3 or T = +3) and re-estimate. The placebo event-study coefficients should be jointly insignificant and centered at zero. Repeat for recovery episodes.",
      "priority": "MUST"
    },
    {
      "category": "specification",
      "requirement": "PLACEBO TEST — false treatment group: Estimate the same event study for countries that are NOT commodity-dependent (or low-commodity-export-share). These countries should show no civil liberties response to commodity price cycles.",
      "priority": "MUST"
    },
    {
      "category": "specification",
      "requirement": "Formally test for treatment-effect heterogeneity across commodity type (oil vs. metals vs. agricultural). The ratchet mechanism may differ: oil-exporting autocracies may face different political constraints than agricultural exporters. Interact episode dummies with commodity-type indicators and test the interaction jointly.",
      "priority": "SHOULD"
    },
    {
      "category": "specification",
      "requirement": "Check for floor/ceiling effects in the civil liberties outcome. If the distribution has mass at the minimum (most repressive) or maximum (most free), a linear TWFE estimate is mechanically attenuated. Report the share of country-years at the bounds and test the main results on the interior sample (countries not at the floor or ceiling).",
      "priority": "SHOULD"
    },
    {
      "category": "robustness",
      "requirement": "Episode definition sensitivity: the bust/recovery episode boundaries are likely threshold-based (e.g., price decline > X%). Re-estimate with at least two alternative threshold definitions (tighter and looser). Report a robustness table showing how the symmetry test p-value and magnitude change.",
      "priority": "MUST"
    },
    {
      "category": "robustness",
      "requirement": "Balanced event window: estimate using a balanced panel of event-time observations (same number of pre- and post-periods for every episode). Unbalanced windows can mechanically produce asymmetric-looking coefficients. Compare balanced vs. unbalanced results.",
      "priority": "MUST"
    },
    {
      "category": "robustness",
      "requirement": "Exclude truncated/partial episodes: episodes that are right-censored (recovery begins but data ends before full recovery window) or left-censored (bust begins before the panel starts). These partial episodes contaminate the symmetry test. Report results with and without them.",
      "priority": "MUST"
    },
    {
      "category": "robustness",
      "requirement": "Overlapping episode contamination: if a new bust begins during the recovery window of a prior episode, the recovery estimate is contaminated. Code an explicit indicator for 'clean' recovery episodes (no re-entry into bust within the event window) and estimate on the clean subsample.",
      "priority": "MUST"
    },
    {
      "category": "robustness",
      "requirement": "Alternate outcome indices: if the primary outcome is one civil liberties index (e.g., Freedom House), re-estimate with V-Dem's liberal democracy or physical integrity rights index. Ratchet findings should be robust across measurement approaches.",
      "priority": "SHOULD"
    },
    {
      "category": "robustness",
      "requirement": "Control for concurrent shocks: add controls for GDP growth, political regime type at episode start, and whether an IMF program was active during the episode. Commodity busts often co-occur with fiscal crises; separating repression due to price shock vs. fiscal crisis is essential.",
      "priority": "SHOULD"
    },
    {
      "category": "robustness",
      "requirement": "Country-specific commodity price index: if the treatment variable is a world price index, construct a country-specific shock as (world price change) × (country's pre-period commodity export share). This reduces confounding from global demand shocks that affect both prices and political outcomes through other channels.",
      "priority": "SHOULD"
    },
    {
      "category": "presentation",
      "requirement": "Every regression table must include: coefficient, cluster-robust SE in parentheses, 95% CI in brackets, N (country-year observations), number of clusters, within-R², and country and year FE indicators. The symmetry test Wald statistic and p-value must appear as a row at the bottom of the main results table.",
      "priority": "MUST"
    },
    {
      "category": "presentation",
      "requirement": "Event-study plots: produce three figures — (1) bust episode coefficients with 95% CIs across event-time horizons, (2) recovery episode coefficients, (3) a 'symmetry plot' overlaying the bust coefficients with the sign-reversed recovery coefficients. The visual gap between curves is the ratchet evidence.",
      "priority": "MUST"
    },
    {
      "category": "presentation",
      "requirement": "Report the Sun & Abraham ATT(g,t) estimates as a coefficient plot disaggregated by episode cohort (year of bust onset). If different cohorts tell qualitatively different stories, the pooled TWFE result is masking heterogeneity and should not be the headline estimate.",
      "priority": "SHOULD"
    },
    {
      "category": "presentation",
      "requirement": "Report the pre-trend test p-values and the Roth (2022) breakdown value M* directly in the main text or as a dedicated diagnostics table — not buried in an appendix. Readers need to assess identification quality without hunting for it.",
      "priority": "MUST"
    },
    {
      "category": "pitfall",
      "requirement": "AVOID endogenous episode boundaries: do not define bust/recovery episodes using political outcome variables (e.g., 'bust ends when stability is restored'). Episode timing must be determined purely by commodity price dynamics, external to the civil liberties outcome. Document and justify the episode algorithm explicitly.",
      "priority": "MUST"
    },
    {
      "category": "pitfall",
      "requirement": "AVOID asymmetric event windows by construction: if bust windows are longer than recovery windows (or vice versa) due to data constraints, the symmetry test will mechanically favor asymmetry. Either enforce equal-length windows or explicitly control for window length in the test.",
      "priority": "MUST"
    },
    {
      "category": "pitfall",
      "requirement": "AVOID controlling for GDP or fiscal variables as covariates in the main specification if these are themselves mediators of the commodity price → repression channel. Including mediators in TWFE will absorb the effect you are trying to measure. Estimate the reduced-form effect first; add mediator controls only as robustness to decompose channels.",
      "priority": "MUST"
    },
    {
      "category": "pitfall",
      "requirement": "AVOID the implicit assumption that 'no bust' countries form a valid counterfactual for 'bust then recovery' countries. Countries that never experience busts are structurally different (less commodity-dependent, different political economies). The comparison should be within commodity-dependent countries across their own episode/non-episode periods, not against non-commodity exporters.",
      "priority": "MUST"
    },
    {
      "category": "pitfall",
      "requirement": "AVOID horizon-by-horizon inference for the symmetry test without adjusting for multiple comparisons. If you test symmetry at τ=1,2,…,K separately, the family-wise error rate is inflated. Use the joint Wald test across all horizons as the primary test; individual horizon tests are descriptive only.",
      "priority": "MUST"
    },
    {
      "category": "pitfall",
      "requirement": "AVOID conflating the ratchet effect with a pure level shift. A genuine ratchet means: (a) bust causes deterioration AND (b) recovery does NOT restore the pre-bust level. You must explicitly test and report the cumulative effect at end-of-recovery window relative to the pre-bust baseline, not just show that recovery coefficients are smaller than bust coefficients in absolute value.",
      "priority": "MUST"
    },
    {
      "category": "pitfall",
      "requirement": "AVOID ignoring TWFE negative-weight contamination: with staggered timing, early-treated cohorts act as control units for late-treated cohorts in later periods — but if early-treated units have ongoing treatment effects (ratchet!), this biases the late-cohort estimates downward. The Sun-Abraham estimator is not optional here; it is the correct estimator given the ratchet hypothesis itself.",
      "priority": "MUST"
    }
  ],
  "method_warnings": [
    "The ratchet hypothesis is inherently about treatment effect dynamics persisting post-episode — this is precisely the setting where standard TWFE negative weights are most damaging, because 'already repressed' countries in their post-bust period corrupt the control group for recovery-episode countries. Sun-Abraham/CS estimators are essential, not optional.",
    "Commodity price shocks are correlated across countries (common global factor). This violates the independence across clusters assumption underlying cluster-robust SEs. Two-way clustering and/or a factor-augmented specification (absorbing global commodity price trends as a common factor) should be considered.",
    "Civil liberties indices (Freedom House, V-Dem) are bounded, ordinal, and updated annually with possible 'stickiness' built into the coding process — coders may be reluctant to reverse prior-year ratings absent strong evidence. This measurement artifact could itself generate a spurious ratchet pattern independent of true political dynamics. A falsification test using a continuously measured outcome (e.g., newspaper closures, political imprisonment counts) is needed.",
    "If bust episodes cluster in specific decades (e.g., 1980s debt crises, 2014–2016 oil crash), year fixed effects may not be sufficient to absorb contemporaneous global shocks. Region × year fixed effects or wave-specific indicators may be needed.",
    "The symmetry test's statistical power depends heavily on having enough recovery episodes of sufficient length. If most busts are followed by only 1–2 years of recovery before a new shock, the test is underpowered by design. Report the distribution of episode lengths and recovery window lengths explicitly."
  ],
  "must_not_claim": [
    "Must not claim causal identification without passing the joint pre-trend F-test for BOTH bust and recovery episodes separately.",
    "Must not claim 'the ratchet effect' is established based solely on the visual pattern in event-study plots — the joint symmetry Wald test must be statistically significant at conventional levels.",
    "Must not present TWFE point estimates as the headline result if the Sun-Abraham interaction-weighted estimator produces substantively different estimates — in that case, the heterogeneity-robust estimates are the credible ones.",
    "Must not interpret the symmetry test as evidence of a ratchet mechanism (institutional path dependence) without ruling out the alternative explanation that recovery episodes are simply too short in the data to observe full restoration — this is a power issue, not a ratchet.",
    "Must not claim generalizability beyond commodity-dependent countries; the identification strategy is only valid for the subset of countries for which commodity price shocks constitute genuine exogenous variation in fiscal/political conditions.",
    "Must not use the number of country-year observations (9,292) as the effective sample size for inference — the relevant count is the number of distinct bust and recovery episodes (event clusters), which is likely far smaller.",
    "Must not claim that controlling for GDP growth 'holds the commodity channel constant' — GDP is a mediator, and conditioning on it partially blocks the causal path of interest."
  ]
}
```

**Top concerns in priority order:**

1. **TWFE + staggered timing + ratchet hypothesis** is a perfect storm — the ratchet *itself* means treated units have persistent effects, making them bad controls for later-treated units. Sun-Abraham is structurally required here, not just a robustness check.

2. **Two separate pre-trend tests** — bust and recovery episodes have independent parallel-trends assumptions. Most papers only test the bust side and forget the recovery window entirely.

3. **Measurement artifact risk** — civil liberties indices are coded with known "stickiness" (coders anchor to prior-year scores). This could generate spurious ratchets mechanically. A continuously-measured falsification outcome is essential.

4. **Episode boundary endogeneity** — if bust/recovery timing is defined with any reference to political outcomes, identification collapses entirely.