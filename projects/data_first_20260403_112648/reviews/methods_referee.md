## Referee Report

### Summary of Methodology

This paper reports a 2×2 factorial RCT that cross-randomizes a six-month wage voucher and a vocational training course among approximately 1,260–1,347 young men in Jordan. The estimating equation is a standard factorial OLS augmented with an ANCOVA specification, with the interaction coefficient as the primary test for complementarity. The authors supplement asymptotic inference with permutation tests, Benjamini-Hochberg FDR correction, Lee bounds, and logistic regression robustness checks.

---

### Main Methodological Assessment

The identification strategy is exemplary: random assignment at the individual level ensures unbiased estimation of all factorial parameters, and the balance table confirms successful randomization. The main results are internally consistent with the arm-level means in the evidence packet, and the broad robustness battery is appropriate for an RCT of this design. However, I have identified **verifiable numerical errors** in the reported control means, **selective reporting of Lee bounds**, and **unreported outcome variables** present in the data—each of which requires revision before publication. These are not hypothetical concerns; they are directly verifiable from the evidence packet provided.

---

### Major Concerns

**1. Verifiable numerical errors in reported control means.**
The paper's Table 2 (midline) states the salary control mean is 38.22 JD, but the evidence packet's arm-means table shows the midline salary control mean is 24.93 JD. The regression coefficient of 65.34 JD is internally consistent with the arm means (89.72 − 24.93 ≈ 64.79 ≈ 65.34), so the coefficient itself is correct. But the constant term 38.22 matches the *endline* salary control mean (37.60 JD), not the midline one—suggesting a copy-paste error in table production. The textual claim that the voucher represents a "172 percent increase" over the control mean is therefore incorrect; the true midline salary control mean implies approximately a 262 percent increase.

The same error pattern appears in Table 3 (endline): the reported employment control mean (0.242) diverges from the arm mean (0.212), and the endline LFP control mean (0.544) diverges from the arm mean (0.480). The authors must reconcile regression constants with arm means and correct all affected percentage claims.

*Suggested fix:* Regenerate all tables from the final analysis dataset, verifying that the regression constant equals the actual control-group mean in that regression's sample. Report both arm means and regression constants side by side.

**2. Selective reporting of Lee bounds (salary at midline).**
The paper reports Lee bounds only for *employment* at midline ([0.361, 0.438]) and endline ([−0.012, 0.073]). The evidence packet also contains Lee bounds for *salary* outcomes: midline salary bounds are [−12.19, +45.04], which include zero. This is a materially different finding from the employment bounds and must be reported. Omitting it constitutes selective robustness reporting on a pre-specified check.

Conversely, the endline salary bounds ([+1.26, +18.94]) are strictly positive—meaning the endline salary effect, though non-significant at p = 0.273, survives worst-case attrition correction. This positive finding is also unreported and cuts against the "complete fade-out" narrative.

*Suggested fix:* Report Lee bounds for all three primary outcome variables (employment, salary, LFP) at both horizons. Discuss the salary-specific results explicitly.

**3. Unreported outcome variables in the dataset.**
The evidence packet includes two outcome variables absent from the paper: (a) `mid_ever` — whether the respondent was *ever* employed during the midline period (control mean 0.273, voucher mean 0.562, a ~29 pp difference), and (b) `end_reg_ssc` — apparently an indicator of social security registration (control 0.123, training 0.159, voucher 0.141, both 0.112). Without a pre-analysis plan, selectively excluding measured outcomes raises concerns about specification searching. The authors must either report these outcomes, explain why they were excluded ex ante, or cite a registered PAP that pre-specified the three reported outcomes.

*Suggested fix:* Provide a pre-analysis plan reference or append a outcomes-selection appendix. Report `mid_ever` and `end_reg_ssc` at minimum in supplementary tables with discussion.

**4. Sample size inconsistencies across tables and evidence packet.**
The paper's Table 2 reports N = 1,243 for midline employment and N = 1,231 for midline salary. The evidence packet (table3_main.tex) reports N = 1,207 for both. The data audit reports total N = 1,347, and arm-means tables sum to 1,237–1,287 depending on outcome. These cascading inconsistencies suggest that at least two different analysis samples are being used without documentation. The paper must provide a complete attrition flowchart (CONSORT-style) showing: enrolled → baseline N → midline N by arm → endline N by arm, for each outcome, and explain all exclusions.

**5. Unequal arm allocation not justified.**
The control group contains approximately 449 participants while each treatment arm contains approximately 299—a 1.5:1 ratio that is never explained or justified. Standard 2×2 factorial designs use equal allocation to maximize power for both main effects and the interaction. Unequal allocation reduces power for the interaction test (the paper's primary test) and is consistent with an optimal design only if the cost of control-group observations is lower or prior variance information motivated it. The authors must state the allocation rule, justify it, and report the power implications for the interaction test under the actual allocation.

**6. Numerical discrepancy between paper text and evidence packet for endline LFP interaction.**
The paper text states the endline LFP interaction is −0.048 (p = 0.377), but the evidence packet (table3_main.tex) shows −0.058 (p = 0.305). While small, this type of discrepancy—combined with the control-mean errors above—suggests that the paper's text was not generated directly from the final analysis code. The authors must verify all reported coefficients, standard errors, and p-values against a single authoritative output.

---

### Minor Concerns

1. **Confidence intervals absent.** The tables report standard errors and p-values but not 95% confidence intervals. For the interaction test specifically—the policy-relevant estimand—reporting CI95 = [−0.116, +0.086] (approximate, midline employment interaction) would communicate the precision more directly to policy audiences than the point estimate and standard error alone.

2. **Power calculation for interaction test missing.** The paper claims precision sufficient to "rule out interactions larger than 10–15 percentage points" but provides no formal power calculation. Given that midline employment is 18% in the control group, an interaction of 10 pp would be substantively large relative to baseline. The authors should report the minimum detectable interaction effect (MDE) at 80% power given actual arm sizes and outcome variance, and compare it to what they regard as policy-relevant.

3. **SUTVA not discussed.** The voucher is redeemable at "participating private-sector firms." If the voucher program saturates employer capacity, voucher recipients may displace non-recipient job seekers—a violation of the stable unit treatment value assumption. Given individual-level randomization within a geographically concentrated labor market, some discussion of displacement/equilibrium effects is warranted.

4. **No pre-registration cited.** The paper adopts BH correction and permutation inference following McKenzie (2017), but does not cite a pre-registered PAP. This is an increasing norm for RCTs in development economics and the absence should be acknowledged.

5. **Falsification test design.** The evidence packet shows the falsification test regresses age (an immutable characteristic) on treatment indicators. Age should be perfectly balanced by randomization and is an unusual falsification target. More informative falsification tests would use pre-treatment outcome variables (e.g., retrospective baseline employment, earnings) as dependent variables—a practice the paper describes in the text ("pre-baseline earnings measure collected retrospectively") but which does not appear to be implemented.

6. **BH-adjusted p-values inconsistently reported.** BH-adjusted p-values appear in the midline table but the endline table suppresses them for non-voucher results (blank cells for ANCOVA columns). The correction should be applied uniformly across all reported hypotheses.

7. **Control group dynamics unaddressed.** The control group employment rate rises from 0.178 at midline to 0.212 at endline (+3.4 pp), while LFP falls from 0.771 to 0.480 (−29 pp). This large LFP drop in the control group over the study period is striking and may be the dominant secular trend against which treatment effects are measured at endline. The paper should discuss whether this reflects seasonal effects, survey fatigue, or labor market deterioration—and whether differential trends across arms affect interpretation.

8. **Male-only sample.** The paper notes this limitation but does not discuss whether single-sex randomization was pre-specified or whether operational constraints drove the design. This matters for external validity claims about ALMP effectiveness in MENA contexts where female employment is a policy priority.

---

### Recommendation: **Major Revision**

The factorial design is well-executed, the core identifying assumptions hold under randomization, and the main coefficients reported in the analysis appear consistent with arm-level data. The finding of a large-but-transient voucher effect and null training effect is credible and policy-relevant. However, the verified numerical errors in reported control means, selective Lee bounds reporting, and presence of unreported outcome variables constitute major concerns that must be addressed before publication. These issues require re-running and re-verifying all tables from a single clean analysis script.

---

```json
{
  "score": 71,
  "decision": "MAJOR_REVISIONS",
  "dimension_scores": {
    "identification_strategy": 84,
    "estimation_implementation": 64,
    "statistical_inference": 73,
    "robustness_sensitivity": 62,
    "replication_readiness": 67
  },
  "sanity_checks": {
    "sign": "PASS",
    "magnitude": "PASS",
    "dynamics": "PASS",
    "consistency": "FAIL"
  },
  "major_comments": [
    "Verifiable numerical error: paper reports midline salary control mean = 38.22 JD but evidence packet arm means show 24.93 JD (the 38.22 value matches the ENDLINE salary control mean). The regression coefficient is correct; the constant and the '172% increase' claim are not. Same error pattern affects endline employment (0.242 vs 0.212) and endline LFP (0.544 vs 0.480) control means.",
    "Selective Lee bounds reporting: midline salary Lee bounds are [-12.19, +45.04] — spanning zero — but not reported. Only the employment bounds (cleanly positive) are shown. This is selective robustness reporting that must be corrected. Simultaneously, the endline salary Lee bounds [+1.26, +18.94] are strictly positive and should be highlighted as a positive endline finding.",
    "Unreported outcome variables: the evidence packet contains mid_ever (ever-employed during midline period; voucher effect ~29 pp) and end_reg_ssc (social security registration; not discussed). Absence of a pre-analysis plan makes selective outcome reporting a credibility concern that must be addressed.",
    "Cascading sample-size inconsistencies: paper tables report N=1,243/1,231 for midline, evidence packet shows N=1,207, arm-means sum to 1,237, data audit states N=1,347. A CONSORT-style attrition flowchart disaggregated by arm and outcome is required.",
    "Unequal arm allocation (control ≈450 vs. treatment arms ≈300 each) is never explained or justified. This reduces power for the interaction test and must be motivated."
  ],
  "minor_comments": [
    "Report 95% confidence intervals alongside point estimates, especially for the interaction term.",
    "Provide a formal MDE calculation for the interaction test given actual arm sizes and outcome variance.",
    "Discuss SUTVA: voucher saturation at participating firms could cause displacement of non-voucher workers in a geographically concentrated labor market.",
    "Cite pre-registration or acknowledge its absence; specify whether PAP pre-specified the three reported primary outcomes.",
    "Redesign falsification tests around pre-treatment outcome variables rather than immutable characteristics (age).",
    "Apply BH correction uniformly across all reported hypotheses in both tables.",
    "Discuss the large control-group LFP decline from midline (0.771) to endline (0.480), which is the dominant secular trend at endline.",
    "Text-to-table discrepancy: endline LFP interaction reported as -0.048 (p=0.377) in text but evidence packet shows -0.058 (p=0.305). All figures must be verified against a single analysis output."
  ]
}
```