## Referee Report

**Journal of Development Economics / American Economic Journal: Applied Economics**

---

### Summary

This paper reports a 2×2 factorial RCT in Jordan testing a six-month private-sector wage voucher and a short vocational-training course, separately and in combination, among young men. At midline, the voucher triples employment (39.9 pp, Cohen's d = 0.88), but the effect nearly vanishes by endline (+3.0 pp, p = 0.351); vocational training is uniformly ineffective; and the interaction term is small and insignificant throughout, ruling out superadditivity. The sole persistent voucher effect is a 10.1 pp increase in labor-force participation at endline.

---

### Main Assessment

**Strengths.** The factorial RCT is genuinely rare in the ALMP literature. The design is clean, randomization succeeded (joint F-test p = 0.74), and the robustness battery—permutation inference, Lee bounds, logit, Benjamini-Hochberg correction—is exemplary. The fade-out finding is among the sharpest documented in experimental labor economics, and the null interaction result is policy-relevant. The paper is well-written and honest about limitations.

**Weaknesses.** Several internal inconsistencies between the paper's narrative and the accompanying data tables raise credibility concerns. The population description conflicts with the data. The control-group salary figure reported in the paper does not match the data-audit evidence. A dramatic decline in control-group LFP between midline and endline is not discussed. These are not minor slips; they bear on the interpretation of the central findings.

---

### Major Comments

**1. Sample population mismatch.** The paper describes its participants as young men "who had completed or left secondary school and were not enrolled in tertiary education," using the Tawjihi exam as the key credential. Yet the balance table in the data audit includes a variable `b_communitycollege` (mean ≈ 4.4–4.6, varying across arms), the strategy memo refers to "community college graduates," and the sample mean age is approximately 21 years—entirely consistent with a community college cohort, not a secondary-school-leavers cohort. In Jordan, community colleges (كليات المجتمع) award two-year diplomas and are considered part of the tertiary system. If the sample is community college graduates or current enrollees, the institutional description in Section 3.2 is materially wrong, the Tawjihi framing is misleading, and external validity to secondary-school leavers is overstated. The authors must clarify which population was actually recruited, reconcile this with `b_communitycollege`, and revise the paper accordingly.

**2. Control-group salary discrepancy.** Table 2 (midline OLS) reports the constant as 38.22 JD and labels it "Control mean = 38.22 JD." The data-audit arm-means table reports the control-group mean of `mid_salary` as 24.93 JD. In an OLS of Y on treatment dummies with no controls (column 3), the constant must equal the control-group mean in the regression sample. A discrepancy of ~13 JD (53%) cannot be attributed to sample restrictions. If this reflects a variable-construction difference (e.g., conditional vs. unconditional salary, or a different deflation), the paper must clarify. If it reflects an error in the reported table, it must be corrected. This inconsistency also propagates to the claim that the voucher represents "a 172 percent increase" over the control mean, which changes materially depending on which figure is correct.

**3. Dramatic LFP collapse in the control group is unexplained.** The data audit shows control-group LFP at midline of 77.1% and at endline of 48.0%—a 29 percentage-point decline in less than 12 months. The paper describes the endline LFP effect (+10.1 pp) as evidence that "vouchers drew some men into the labor force who would otherwise have been inactive," treating the endline control LFP level as a stable baseline. But if control-group LFP is in freefall, the +10.1 pp voucher effect is better described as partial mitigation of discouragement rather than an absolute labor-market attachment gain. This pattern—high midline LFP, low endline LFP in the control—is consistent with a community college sample where students temporarily enter the labor market after graduation and subsequently withdraw; it is inconsistent with the paper's framing of participants as already labor-market-attached secondary completers. The authors must describe and explain the trajectory of the control group across time, including its implications for the paper's central narrative.

**4. Sample size discrepancies require reconciliation.** Three different figures appear across the submission: N = 2,322 (strategy memo), N = 1,347 (data audit), and N = 1,207–1,255 (regression tables). The paper reports arm sizes of ~400/~300/~280/~280, but the data audit shows 449/299/300/299. The paper must include a clear CONSORT-style diagram showing: initial enrollment → post-exclusions → baseline sample → midline respondents → endline respondents, with attrition rates and tests for differential attrition. The current attrition discussion (Section 6.3) is insufficient given these discrepancies.

**5. Interpretation of fade-out is underdetermined.** The paper asserts that the employer-learning mechanism is favored over the labor-demand constraint and reservation-wage mechanisms, but provides no evidence distinguishing among them. The test proposed—whether more-educated workers exhibit slower fade-out—is uninformative about the demand-side constraint mechanism, because if the constraint is aggregate (too few vacancies), it would affect all workers uniformly regardless of education. More useful would be: (a) evidence on whether subsidized workers in sectors with tighter labor markets (more private-sector activity) showed slower fade-out; (b) evidence on whether workers' search intensity post-voucher differs from the control group (the LFP data partially address this, but search intensity is not measured); or (c) whether voucher firms continued to post vacancies at the unsubsidized wage. Without such tests, the paper should be more agnostic about mechanism, treating all three as consistent with the evidence rather than endorsing one.

**6. Displacement effects are not addressed.** The voucher reduced the cost of hiring Jordanian nationals to near zero for six months. In a labor market where employers routinely substitute foreign workers for nationals at lower cost, the voucher may have increased employment for participants by displacing foreign workers in participating firms, rather than creating net new employment. This is a well-known concern in wage-subsidy evaluation (Crépon et al. 2013 is cited but the displacement logic for this specific mechanism is not applied). If the voucher merely reshuffles jobs from Egyptian or South Asian workers to Jordanian nationals, the social welfare interpretation of the massive midline effect changes substantially. The authors should discuss this and, where possible, examine whether treated firms show changes in foreign-worker employment.

---

### Minor Comments

**1. Missing outcome: endline salary Lee bounds.** The robustness table in the data audit shows endline salary Lee bounds of [+1.26, +18.94 JD]—a positive lower bound, suggesting a significant persistent wage effect even accounting for selection. This contradicts the paper's characterization that all endline effects have "faded." If the endline salary estimate (+6.95 JD, p = 0.273) is bounded away from zero at the lower Lee bound, this is an important qualification and should be reported and discussed in Section 6.3 or Section 7.

**2. Midline LFP is measured but not reported.** The data audit includes `mid_lfp` (Control = 0.771, Voucher = 0.799), yet the paper designates LFP as an "endline only" primary outcome. If midline LFP was collected, the authors should report it or explain its exclusion. The robustness table shows mid_lfp voucher OR = 1.181, p = 0.381, which is insignificant—this is informative for understanding the trajectory and not suppressing the variable creates no adverse incentive.

**3. `end_reg_ssc` (social security registration) is not analyzed.** The data contains a job formality indicator (end_reg_ssc; control mean ≈ 12.3%). In a context where the key policy concern is formal private-sector employment—and where foreign workers in Jordan frequently work informally—this variable is directly relevant to the policy implications. A brief analysis or discussion should be included.

**4. Coefficient discrepancies between text and tables.** Several small discrepancies appear: (a) the endline LFP interaction term is reported as -0.048 (p = 0.377) in the text but -0.058 (p = 0.305) in the data tables; (b) the logit OR for endline LFP is stated as 1.52 in the text but 1.484 in the robustness table; (c) the endline employment control mean is stated as 0.242 in Table 3 but the arm-means table shows 0.212. These should be verified against the estimation code and corrected.

**5. Voucher value and wage context need clarification.** The paper describes the voucher as "approximately 200 JD per month (roughly 70 percent of the prevailing entry-level wage)." If the control-group mean salary (including zeros) is ~25 JD (as in the data), employed workers earn roughly 25/0.18 ≈ 139 JD, implying that 200 JD is not 70% but substantially above the typical entry-level wage received by this population. The "prevailing entry-level wage" figure should be sourced, contextualized, and reconciled with the salary data.

**6. Missing citation: complementarity and multidimensional poverty.** The paper would benefit from engaging with Duflo, Banerjee et al. (2021, *American Economic Review*) on the ultra-poor graduation approach, which has now been subjected to careful factorial decomposition. Egger et al. (2022) is cited for additive effects; the literature on productive complementarities in human capital investment (Cunha and Heckman 2007) is relevant to the theoretical framework for why bundling might or might not generate superadditivity.

**7. The public-sector queue narrative needs a citation.** The paper asserts that "young men wait for government positions rather than accepting private-sector jobs." While this is qualitatively well-known, it is stated as mechanism without direct evidence. Assaad and colleagues have documented this in quantitative terms; a specific citation to a study measuring queue duration or the wage premium for public employment in Jordan would strengthen the claim.

**8. Female generalizability caveat is understated.** The paper notes the all-male sample as limitation but does not engage with the possibility that wage vouchers for women might have qualitatively larger or smaller effects given different constraints (social norms, mobility, household bargaining). Given recent RCT evidence from MENA on women's employment (e.g., Campos et al. on Saudi Arabia), a brief forward reference to what an analogous design for women might find would strengthen the policy section.

---

### Missing Literature

- Crépon et al. (2013, *QJE*): Displacement effects of active labor market programs—directly relevant to the voucher's aggregate employment impact.
- Caliendo and Künn (2011, *Labour Economics*): Heterogeneity in persistence of wage-subsidy effects; useful for the fade-out mechanisms.
- Acemoglu and Pischke (1999, *QJE*): Employer-provided training and imperfect labor markets—relevant to why training fails when employers do not internalize returns.
- Campos et al. (2017/2020): MENA female employment experiments—relevant to external validity section.
- Duflo et al. (2021, *AER*): Updated ultra-poor graduation evidence with component decomposition.
- McKenzie (2021, *JEL* review of entrepreneurship programs): broader context for why skills programs fail in low-demand environments.

---

### Recommendation: **Major Revision**

The paper makes a genuine contribution—factorial RCT evidence on ALMP interaction effects is rare, and the fade-out result is important. But the population description inconsistency (secondary-school leavers vs. community college graduates), the salary discrepancy, and the unaddressed LFP dynamics are substantive issues that require revision before the paper is publishable. The core results survive scrutiny and I expect they will be robust to corrections, but the current draft cannot be accepted as written.

---

```json
{
  "score": 70,
  "decision": "MAJOR_REVISIONS",
  "dimension_scores": {
    "contribution_novelty": 80,
    "literature_positioning": 73,
    "substantive_arguments": 62,
    "external_validity": 68,
    "journal_fit": 76
  },
  "major_comments": [
    "Sample population mismatch: paper describes secondary-school leavers but data variable b_communitycollege and strategy memo reference community college graduates — a different and arguably tertiary-educated population. Institutional description and external validity claims must be revised accordingly.",
    "Control-group salary discrepancy: paper reports control mean salary of 38.22 JD in midline OLS constant, but data audit shows 24.93 JD. A 53% discrepancy in the OLS intercept (which must equal the control mean) must be explained and corrected; all percentage-increase claims derived from this figure are affected.",
    "Unexplained LFP collapse in control group: control LFP drops from 77.1% at midline to 48.0% at endline — a 29 pp decline — which is not discussed and substantially alters the interpretation of the 10.1 pp endline LFP voucher effect (mitigation of discouragement vs. net LFP gain).",
    "Sample size reconciliation: three incompatible sample counts appear (N=2322 in strategy memo, N=1347 in data audit, N=1207-1255 in regressions). A CONSORT flow diagram with arm-specific attrition is required.",
    "Fade-out mechanism is asserted rather than tested: the employer-learning vs. labor-demand constraint vs. reservation-wage explanations are observationally equivalent with the available data; the paper should acknowledge this and not claim one is 'favored'.",
    "Displacement effects of the voucher are not addressed: in a labor market where employers substitute foreign workers for nationals, a near-zero cost voucher may shift jobs rather than create them, changing the welfare interpretation of the midline effect."
  ],
  "minor_comments": [
    "Endline salary Lee bounds [+1.26, +18.94 JD] suggest a positive lower bound — evidence of a persistent wage effect that contradicts the 'full fade-out' narrative and should be reported.",
    "Midline LFP variable (mid_lfp) is collected but excluded from reported outcomes without explanation; should be reported or exclusion justified.",
    "end_reg_ssc (social security registration, ~12% control mean) is a formality measure directly relevant to policy but is not analyzed.",
    "Minor coefficient discrepancies between text and tables: endline LFP interaction (-0.048 vs -0.058), logit OR for endline LFP (1.52 vs 1.484), endline employment control mean (0.242 vs 0.212 in arm-means table).",
    "Voucher value description (200 JD = 70% of entry-level wage) conflicts with the salary data; source and reconcile.",
    "Public-sector queue mechanism should be supported with a direct citation measuring queue duration or public/private wage premium in Jordan.",
    "Female generalizability caveat should engage with recent MENA female employment RCTs rather than simply noting the limitation."
  ],
  "missing_literature": [
    "Crépon, Duflo, Gurgand, Rathelot, Zamora (2013, QJE) — displacement effects of ALMPs, directly relevant to voucher aggregate impact",
    "Caliendo and Künn (2011, Labour Economics) — heterogeneity in persistence of wage-subsidy effects",
    "Acemoglu and Pischke (1999, QJE) — employer training under imperfect competition, relevant to training failure mechanism",
    "Duflo, Banerjee et al. (2021, AER) — updated graduation program evidence with component evaluation",
    "McKenzie (2021, JEL) — review of entrepreneurship and skills programs in low-demand environments"
  ]
}
```