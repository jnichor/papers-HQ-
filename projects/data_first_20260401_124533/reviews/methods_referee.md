## Referee Report

**Paper**: "The Ratchet Effect: Commodity Busts Erode Civil Liberties That Booms Do Not Restore"

---

### Summary of Methodology

The paper exploits exogenous variation in the IMF Commodity Terms of Trade (CTOT) index — constructed using fixed export-import baskets — to estimate the effects of commodity bust and recovery episodes on five disaggregated civil liberty measures across 80 countries, 1975–2024. A TWFE specification identifies average bust effects, while an asymmetric event-study design tracks dynamic responses around episode start dates. The central ratchet hypothesis — that bust-induced erosion is not reversed during recoveries — is formalized as a joint symmetry test on average post-episode event-study coefficients.

---

### Main Methodological Assessment

The identification strategy rests on a credible foundation: CTOT variation is plausibly exogenous because it is driven by global price movements and fixed (pre-determined) trade shares, and the pre-trend evidence is reassuring across all five outcomes. However, several serious problems undermine confidence in the reported results.

**Most critically**, there is a sign reversal between the TWFE coefficient for fair trial rights (Table 1: β = −0.199, indicating bust-induced deterioration) and the event-study average bust coefficient in the symmetry table (Table 2: bust avg = +0.489, implying bust-induced improvement). These two estimates carry opposite signs and the paper offers no reconciliation — this cannot be dismissed as a rounding or scaling artifact, as the discrepancy is roughly 0.7 index points.

**Second**, the symmetry test rejects the null for four of five liberties, but for qualitatively different reasons across outcomes. For freedom of movement, the ratchet story holds: bust avg = −0.220, recovery avg = −0.024 (both negative, indicating bust erosion is not restored). But for assembly, religion, and fair trial, both bust and recovery averages are *positive*. A symmetry rejection driven by unequal positive effects is not evidence of a ratchet; it is something else entirely. The paper conflates these distinct patterns under the single "asymmetry" label.

**Third**, with 31 bust episodes at different calendar dates across 80 countries, the TWFE estimator is susceptible to heterogeneity bias from staggered adoption. The sign divergence between Tables 1 and 2 for fair trial suggests this is not a purely theoretical concern.

---

### Major Concerns

**1. Critical sign inconsistency between Table 1 and Table 2 (fair trial)**

The TWFE in Table 1 yields β = −0.199 for fair trial, which the paper interprets as "commodity busts significantly erode fair trial rights." The symmetry table reports a bust event-study average of +0.489 for the same variable — the opposite sign. Possible causes: (a) the event-study reference period t=−1 may itself be depressed relative to the unconditional mean, mechanically inflating post-bust coefficients; (b) bust and recovery episodes may be interleaved in ways that contaminate the event-study baseline; (c) there may be a labeling or sign error in Table 2. The authors must provide a transparent reconciliation, including a figure overlaying the TWFE point estimate and the event-study path for fair trial, and must clarify which estimate is primary. This issue potentially invalidates the paper's first headline finding.

**2. Symmetry test mischaracterizes the ratchet hypothesis for three of four "rejections"**

The ratchet hypothesis requires: (i) bust coefficient is negative and (ii) recovery coefficient is insufficiently positive to restore baseline liberties. This holds for freedom of movement. However, for assembly (bust = +0.369, recovery = +0.408), religion (bust = +0.132, recovery = +0.146), and fair trial (bust = +0.489, recovery = +0.259), both coefficients are positive. The symmetry null is rejected because the two positive effects differ in magnitude, not because a negative bust effect is incompletely reversed. The paper should categorize rejections by the qualitative pattern driving them and restrict "ratchet" language to freedom of movement. Calling four of five liberties evidence of "pervasive asymmetry" consistent with the ratchet hypothesis is not supported.

**3. TWFE heterogeneity bias from staggered adoption not addressed**

With 31 bust episodes entering at different calendar times, the TWFE estimator computes a variance-weighted average of group-time ATTs that may assign negative weights to some comparisons, potentially producing sign reversals (de Chaisemartin and D'Haultfœuille 2020; Callaway-Sant'Anna 2021; Sun-Abraham 2021). The paper should replicate baseline results using at minimum one heterogeneity-robust estimator (Callaway-Sant'Anna group-time ATTs or Sun-Abraham interaction weights). Given the sign divergence already observed between TWFE and event-study averages, this concern is empirically live.

**4. Multiple testing correction absent**

The paper tests five outcomes with two hypotheses each (TWFE effect, symmetry test), implying ten joint tests. Under Bonferroni correction, significance requires p < 0.005. The paper's two headline results — fair trial TWFE (p = 0.020) and movement symmetry (p = 0.029) — both fail this threshold. The paper should apply Benjamini-Hochberg FDR correction and clearly disclose sensitivity of the main findings to multiple testing.

**5. Placebo test applied to the wrong variable**

The paper reports a permutation placebo p-value of 0.389 for freedom of expression — a variable that already shows an insignificant TWFE coefficient (β = 0.064, p = 0.483). A placebo test confirming that an insignificant result has no effect is uninformative. The permutation test must be reported for fair trial rights and freedom of movement, the two outcomes driving the paper's conclusions. A placebo p-value above 0.05 for these variables would substantially strengthen the causal claim; its absence is a notable gap.

---

### Minor Concerns

1. **Missing observations for fair trial**: Fair trial has 6,824 observations versus 7,330 for all other outcomes — 506 missing country-years. The source and potential systematicity of this missingness is never explained. If fair trial data is missing for particular country-types or years, the TWFE estimate may be identified on a selected subsample.

2. **Unmatched bust-recovery pairs**: There are 31 bust episodes but only 21 recovery episodes; the 10 unmatched busts are countries in ongoing busts or that never experienced a qualifying recovery. The paper does not explain how these are handled in the symmetry test. Results may be mechanically driven by this asymmetric sample if unmatched busts have different liberty trends.

3. **Multiple episodes per country not addressed**: With 31 busts across 80 countries over 50 years, repeated episodes within the same country are plausible. The paper should state how multiple within-country episodes are handled and confirm that clustering standard errors at the country level adequately accounts for within-country serial correlation across episodes.

4. **Alternative threshold results not tabulated**: Results for bust thresholds of −15%, −25%, and −30% are described as "qualitatively similar" without a table. For a core sensitivity test, the coefficients and p-values across all four threshold definitions should be reported in a robustness table.

5. **Implausibly high z-statistics for assembly, religion, and fair trial**: The symmetry test z-statistics of 5.483, 5.370, and 5.105 are unusually large for 80 country clusters and ~25 treatment episodes. These may reflect a standard error calculation that treats the event-study coefficients as known rather than estimated, omitting cross-equation covariance. The construction of the variance-covariance matrix underlying the symmetry test should be described explicitly.

6. **No economic controls**: The specification includes only country and year fixed effects. Commodity busts frequently coincide with fiscal crises, sovereign debt distress, and armed conflict — each of which can independently erode civil liberties. At minimum, the paper should test sensitivity to including GDP growth and a conflict indicator. This is particularly important for fair trial rights, where executive power grabs during fiscal crises are the proposed mechanism.

7. **Ceiling effects in religion variable**: Freedom of religion has a mean of 3.27 on a 1–4 scale (summary statistics table). OLS near a boundary may produce attenuated coefficients. An ordered logit sensitivity check is warranted for this variable specifically.

8. **Base year for fixed trade shares unspecified**: The CTOT exogeneity argument depends on trade shares being determined prior to the outcomes. If base-year shares are chosen in periods that correlate with civil liberty levels (e.g., boom years), the identifying variation may not be fully clean. The paper should specify the base year used by Gruss and Kebhaj (2019) and verify it predates the sample.

---

### Recommendation

**Major Revision**

The paper asks an important and underexplored question about the path dependence of civil liberty erosion, and the CTOT identification strategy provides a defensible foundation. However, the sign inconsistency between the TWFE and event-study estimates for fair trial (Major Concern 1), the mischaracterization of the symmetry test results as uniformly representing a ratchet (Concern 2), the unaddressed staggered-adoption bias (Concern 3), and the multiple testing problem (Concern 4) collectively require a substantial re-analysis. The core empirical contribution — the movement ratchet (p = 0.029) — may survive revision, but its credibility depends on resolving these issues first.

---

```json
{
  "score": 60,
  "decision": "MAJOR_REVISIONS",
  "dimension_scores": {
    "identification_strategy": 70,
    "estimation_implementation": 52,
    "statistical_inference": 58,
    "robustness_sensitivity": 55,
    "replication_readiness": 65
  },
  "sanity_checks": {
    "sign": "FAIL",
    "magnitude": "PASS",
    "dynamics": "FAIL",
    "consistency": "FAIL"
  },
  "major_comments": [
    "Sign reversal between TWFE (Table 1: fair trial β = −0.199) and event-study bust average (Table 2: +0.489) is unexplained and invalidates both as presented; authors must reconcile or acknowledge a coding/labeling error.",
    "Symmetry test rejections for assembly, religion, and fair trial are driven by both bust and recovery coefficients being positive, which is not the ratchet pattern; only freedom of movement exhibits the negative-bust/non-restoring-recovery structure described by the hypothesis.",
    "Staggered TWFE heterogeneity bias not addressed; with 31 episodes at different dates, forbidden comparisons may contaminate estimates; Callaway-Sant'Anna or Sun-Abraham replication required.",
    "Headline results (fair trial p=0.020, movement symmetry p=0.029) do not survive Bonferroni correction across 10 joint tests; Benjamini-Hochberg FDR correction must be applied and sensitivity disclosed.",
    "Permutation placebo test reported for freedom of expression (p=0.483 in TWFE, already insignificant), not for fair trial or movement — the variables that drive the paper's conclusions."
  ],
  "minor_comments": [
    "506 missing fair trial observations unexplained; potential for systematic missingness should be assessed.",
    "10 unmatched bust episodes (no subsequent recovery) create asymmetric samples for the symmetry test; treatment of these cases must be stated.",
    "Alternative threshold robustness results described but not tabulated; coefficient tables across −15/−20/−25/−30% thresholds required.",
    "Symmetry test z-statistics of 5.48, 5.37, and 5.11 implausibly large for 80 clusters; variance-covariance construction underlying the test must be disclosed.",
    "No economic controls (GDP growth, conflict) despite strong prior that busts co-occur with other liberty-eroding shocks.",
    "Freedom of religion mean 3.27/4.0 risks ceiling attenuation in OLS; ordered logit sensitivity check warranted.",
    "Base year for CTOT fixed trade shares not specified; exogeneity argument requires confirmation that shares predate the study window."
  ]
}
```