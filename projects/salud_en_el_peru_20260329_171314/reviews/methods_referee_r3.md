## Referee Report — Round 3 Review

**Journal of Development Economics / Health Economics**

---

### Summary of Methodology

This paper applies conditional quantile regression (CQR) to Peru's 2024 ENAHO to estimate whether the association between SIS insurance membership and OOP health expenditure share varies across the conditional spending distribution, using insurance–quintile interaction terms at τ = {0.50, 0.75, 0.90}. The paper complements CQR with a two-part model and 25 robustness checks, using cluster-bootstrapped standard errors at the PSU level. The revision has improved framing transparency substantially—the title now accurately reflects the regressive gradient finding, and limitations are disclosed prominently—but both issues designated CONDITIONALLY FATAL in Round 2 remain uncorrected in the data and estimation code.

---

### Main Methodological Assessment

The authors have made meaningful progress on presentation, framing, and interpretive discipline. The title rewrite, explicit restriction of CQR interpretation to τ ≥ 0.50, and the candid limitations section in the conclusion represent genuine improvements. However, the revision strategy adopted a **disclosure-without-correction** approach to both conditionally fatal data errors: the authors describe the errors accurately and state that correcting them is "a prerequisite for credible results," yet submit the paper with the errors intact. This is methodologically untenable. A paper cannot simultaneously declare its own results unreliable and claim a publishable contribution. The two unresolved fatal issues—EsSalud misconstruction contaminating the uninsured reference group, and mechanical quintile–OOP circularity—are not presentation problems; they are data construction errors that affect every coefficient in every table.

---

### Major Concerns

**1. [UNRESOLVED — CONDITIONALLY FATAL] EsSalud household-head assignment rule not corrected.**

Section 3 still reads: *"The household-level insurance variable is assigned based on the household head's coverage."* The conclusion correctly diagnoses the consequence—N = 648 (~2% coverage vs. ~30% nationally), misclassified EsSalud members contaminating the uninsured reference group, all SIS interaction estimates biased—and states that correction is a "prerequisite for credible results." But the correction has not been made. Restricting the abstract's primary comparison to SIS vs. uninsured does not resolve the contamination: households where a non-head member holds EsSalud coverage are wrongly coded as uninsured, and these misclassified households are included in the reference category against which all SIS coefficients are estimated. The appropriate fix is documented in Round 2 feedback and is technically straightforward: re-assign insurance status using any-household-member coverage across all individuals in Module 400, then aggregate to household level with EsSalud taking precedence. The paper cannot be accepted until this is implemented and results re-estimated.

*Required action*: Reconstruct the insurance variable using any-member coverage. Report N and share by insurance category before and after correction. Re-estimate all tables. If the corrected EsSalud N approaches the expected ~30% nationally, report EsSalud estimates; if coverage data is still unreliable for another reason, document explicitly why.

**2. [UNRESOLVED — CONDITIONALLY FATAL] Mechanical quintile–OOP circularity not corrected.**

Consumption quintiles are still constructed from GASHOG2D, which includes health expenditure—the same variable used in the OOP share numerator. The abstract acknowledges the gradient is "partly mechanical," and Section 5 notes the quintile–OOP correlation is "mechanically inflated." But the quintiles have not been reconstructed from non-health consumption. This circularity means that the central finding of the paper—a monotonic Q1→Q5 gradient in OOP share—is at least partially an algebraic artifact, not a behavioral regularity. Because the insurance–quintile interactions are estimated against this contaminated gradient, the sign, magnitude, and statistical significance of the SIS×Qq terms cannot be reliably distinguished from mechanical effects. The fix is well-defined: compute non-health consumption as GASHOG2D minus the health expenditure aggregate (P41601+P41602+P41603 annualized), then assign quintiles from non-health consumption. This is a single variable redefinition.

*Required action*: Reconstruct quintiles from non-health consumption. Re-estimate all tables. In robustness, show both quintile definitions to document how much of the gradient is mechanical vs. behavioral.

**3. [UNRESOLVED] Bootstrap replications still at 200.**

The abstract explicitly states "bootstrap inference uses 200 replications (below the 999 standard)." The headline SIS×Q5 estimate at τ = 0.90 (−1.94 pp, p < 0.01) is the paper's most prominent result, and it rests on upper-tail estimates where CQR estimates are most sensitive to bootstrap instability. The authors were instructed in Round 2 to re-estimate with ≥999 replications before any significance conclusions at upper quantiles can stand. This is computationally straightforward with joblib/multiprocessing parallelization on the existing codebase. Reporting provisional significance from a known-unstable estimator is not acceptable.

*Required action*: Re-estimate with ≥999 replications (1,999 preferred for upper-tail inference). Update all standard errors, p-values, and confidence intervals. If any headline results lose significance, revise claims accordingly.

**4. [UNRESOLVED] Non-health falsification test deferred to future work.**

Section 6 acknowledges that the random-treatment placebo is "weak" and that a non-health expenditure share falsification "would better rule out residual confounding." It then defers this test to future work. This is the same deferral from Round 2. A falsification test—regressing food or clothing expenditure share on insurance status and quintile interactions at the same τ values—requires no new data and no new methodology. If insurance predicts OOP share but not non-health expenditure shares at the same quantiles, this substantially strengthens the paper's descriptive case. If it does predict non-health shares similarly, this flags residual confounding by socioeconomic status that the controls do not fully absorb.

*Required action*: Implement the non-health falsification test (food share at τ = {0.50, 0.75, 0.90}) and include results in Section 6. This must not be deferred further.

---

### Minor Concerns

1. **Multiple testing disclosure without correction**: The paper now notes that 4/25 significant results at α = 0.05 is within chance range, which is appropriate. However, the quantile regression results in Section 5 report individual p-values for five SIS×Qq interactions across three quantiles (15 joint tests) with no familywise correction applied. The disclosure in Section 6 does not propagate back to the result tables or the abstract's confidence claims. At minimum, Holm-corrected p-values should be reported alongside uncorrected values in Table 2, or the interpretation of individual interaction significance should be explicitly qualified throughout Section 5 (not only in the robustness section).

2. **Two-part model integration**: The two-part model is described in the literature review and strategy sections as the appropriate complement to CQR given the 44.1% zero mass, but its results are not prominently integrated into Section 5. The extensive-margin estimates (probability of any OOP spending by insurance and quintile) are policy-relevant and should be co-reported with the intensive-margin CQR estimates, not treated as a separate appendix item.

3. **P41603 heterogeneity caveat placement**: Section 3 notes that "other health costs" (P41603) includes hospitalization, transport, dental, and optical expenses with high within-category variance. This caveat is raised once in the data section but not revisited when interpreting the upper-quantile results, where P41603 almost certainly dominates. Section 5's discussion of τ = 0.90 estimates should explicitly note that these represent the composite P41603 category rather than a clean health expenditure measure.

4. **Annualization × 13 assumption**: The × 13 factor (52/4) assumes the 4-week recall period is uniformly representative of annual spending. This assumption is noted but the × 12 sensitivity test showing "near-identical estimates" is presented as reassuring when it should not be: × 12 and × 13 differ by only 8%, so near-identical results are algebraically guaranteed regardless of whether the annualization assumption is appropriate. A more informative robustness check would use per-capita daily OOP (no annualization) or restrict the sample to households with chronic illness (for whom annualization is less distorting) and compare.

---

### Recommendation

**MAJOR REVISIONS** — with notice that rejection is the likely outcome of a third round if Concerns 1 and 2 remain unresolved.

The paper's intellectual honesty about its own limitations is unusual and commendable. The authors have accurately identified what needs to be fixed and why. The problem is that identifying but not fixing a conditionally fatal error does not constitute a revision. A revised paper that describes its own results as unreliable pending data reconstruction has not, in substance, been revised. The path to acceptance is narrow but clear: fix the EsSalud variable construction (Concern 1), reconstruct quintiles from non-health consumption (Concern 2), increase bootstrap replications (Concern 3), and implement the falsification test (Concern 4). These are all executable with the existing ENAHO data and existing codebase. If the corrected results survive in sign and rough magnitude, the paper has a publishable contribution about the distributional profile of OOP spending and the heterogeneous SIS association across the conditional distribution. If they do not survive, the honest conclusion is that the current data and methodology cannot support the claimed findings.

---

```json
{
  "score": 49,
  "decision": "MAJOR_REVISIONS",
  "dimension_scores": {
    "identification_strategy": 45,
    "estimation_implementation": 47,
    "statistical_inference": 43,
    "robustness_sensitivity": 52,
    "replication_readiness": 57
  },
  "sanity_checks": {
    "sign": "PASS",
    "magnitude": "PASS",
    "dynamics": "NA",
    "consistency": "FAIL"
  },
  "major_comments": [
    "UNRESOLVED FATAL: EsSalud household-head-only assignment still in place (03_data.tex line: 'assigned based on the household head's coverage'). N=648 (~2%) vs ~30% expected nationally. Uninsured reference group remains contaminated by misclassified EsSalud members. Authors accurately describe the error and state correction is 'a prerequisite for credible results' in the conclusion — but have not corrected it. Disclosure-without-correction is not a revision. Re-assign using any-household-member coverage across all Module 400 individuals before aggregating to household level.",
    "UNRESOLVED FATAL: Quintile circularity unresolved. Quintiles still assigned from GASHOG2D inclusive of health expenditure. Abstract acknowledges gradient is 'partly mechanical'; results section flags 'mechanically inflated correlation'. The fix (compute non-health consumption = GASHOG2D − annualized health expenditure, reassign quintiles) is a single variable redefinition. The entire insurance×quintile gradient — the paper's core finding — cannot be interpreted until this is done.",
    "UNRESOLVED ADDRESSABLE: Bootstrap replications remain at 200. Abstract self-describes this as 'below the 999 standard'. Headline SIS×Q5 estimate at τ=0.90 (−1.94pp, p<0.01) rests on upper-tail CQR estimates most sensitive to replication count. Re-estimate with ≥999 replications required before significance conclusions at τ=0.90 can stand.",
    "UNRESOLVED: Non-health expenditure falsification test deferred to future work for second consecutive round. Falsification (food or clothing share ~ insurance × quintile at τ={0.50,0.75,0.90}) requires no new data, no new methodology. Must be implemented and reported in Section 6 in the next revision."
  ],
  "minor_comments": [
    "Multiple testing acknowledgment in Section 6 does not propagate to Table 2 or the abstract's confidence claims. Holm-corrected p-values should appear alongside uncorrected values in the main QR table, or all individual interaction significance statements in Section 5 must be explicitly qualified — not just the robustness section note.",
    "Two-part model extensive-margin results should be co-reported with CQR in Section 5, not treated as appendix material. Given the 44.1% zero mass, the extensive margin (probability of any OOP spending by insurance × quintile) is arguably more interpretable than the conditional quantile function and should not be subordinated.",
    "P41603 ('other health costs') heterogeneity caveat raised in data section but not revisited in Section 5 discussion of τ=0.90 results, where P41603 almost certainly dominates variance. Upper-quantile interpretation should explicitly note this categorical heterogeneity.",
    "The ×12 vs ×13 annualization robustness check is uninformative as noted — an 8% scalar difference produces near-identical results algebraically. Replace with a more informative sensitivity: restrict to chronic illness households (for whom 4-week recall is more representative of annual patterns) and compare."
  ]
}
```