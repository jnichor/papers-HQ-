## Referee Report — Round 2
**Wage Subsidies vs. Vocational Training for Young Men: Experimental Evidence from a Factorial RCT**

---

### Summary

The paper evaluates a 2×2 factorial RCT that cross-randomizes employment vouchers and vocational training among 1,347 young men. Vouchers generate a 39.9 percentage point increase in employment at midline that largely fades by endline (3.0 pp, insignificant), while training is null at both horizons and the interaction is zero. The revision corrects the education variable labeling, clarifies the setting description, and appears to have reconciled most numerical discrepancies against the underlying data.

---

### Assessment

The revision has made genuine progress on several fronts: the education variable is now correctly described as an ordinal 1–8 scale throughout, balance table notes are improved, and the evidence packet confirms that the key regression coefficients in the paper match the data outputs. These were important corrections. However, three of the six Round 2 must-address issues remain substantively unresolved, and a previously raised structural concern (SUTVA) has not been acknowledged. The paper cannot be accepted in its current state.

---

### Major Comments

**1. LATE/2SLS estimates are still absent (Must-Address, unresolved)**

The Round 2 editorial decision explicitly required "ITT estimates accompanied by LATE estimates via 2SLS." This is not fulfilled in the revision. The strategy memo specifies "LATE/2SLS using assignment as instrument for take-up," but the paper reports only ITT. Without knowing the compliance rate—what fraction of voucher-assigned individuals actually took up the voucher and the fraction of training-assigned individuals who completed training—the ITT effect sizes cannot be translated into per-complier returns. The 39.9 pp ITT employment effect divided by a compliance rate well below 1.0 could imply an implausibly large LATE, or alternatively suggest the voucher bite is near-universal. The absence of take-up statistics is itself a reportable finding. The authors must: (a) report compliance/take-up rates by arm, (b) estimate the LATE via 2SLS using assignment as an instrument, and (c) revise any cost-effectiveness or policy-budget language to reflect per-complier rather than ITT magnitudes. The conclusion section currently states that "the marginal dollar is better spent expanding voucher coverage" without cost-per-complier data—this claim is unwarranted as written.

**2. The midline-to-endline sample increase is unexplained (Must-Address, unresolved)**

The paper now describes the sample variation across waves ("At midline, the effective sample size is 1,207...At endline, the sample ranges from 1,218 to 1,255") but offers no explanation for why more individuals are observed at endline than at midline. Standard panel attrition implies endline ≤ midline. An increase is possible under re-contact protocols, refreshment samples, or administrative record linkage, but each mechanism has distinct implications for the validity of the panel estimates and for interpreting the fade-out. The authors must explain the mechanism and assess whether the endline composition is comparable to the midline composition within arms. If the endline additions are concentrated in particular arms, the fade-out result could reflect compositional change rather than genuine employment dynamics.

**3. The 29-percentage-point decline in control-group LFP is never explained (Must-Address, unresolved)**

Control-group labor force participation falls from 77.1% at midline to 48.0% at endline—a 29 pp decline that is larger in absolute magnitude than the persistent treatment effect the paper highlights. The revision does not address this. The paper uses the endline control mean of 48.0% as the denominator for interpreting the 10.1 pp LFP voucher effect, yet this mean itself is anomalous. Possible explanations include survey-wave seasonality (if the endline occurred during a low-LFP season), differential survey timing, compositional change due to the unexplained sample additions (point 2 above), or genuine secular changes in the control population. Until this decline is explained and ruled out as a survey artifact, the headline persistence result—"vouchers may have induced individuals to remain engaged with the labor market"—rests on a fragile empirical foundation. At minimum the authors should: (a) document the gap in months between midline and endline surveys, (b) check whether the endline was conducted in a season with systematically lower male labor market activity, and (c) test whether the endline LFP drop is concentrated among particular subgroups or newly added observations.

**4. The 975 excluded individuals remain inadequately characterized**

The revision now acknowledges the exclusions: "The remaining 975 individuals were excluded from randomization, likely due to eligibility screening or logistical constraints." The word "likely" is insufficient for a paper making causal claims. The excluded group is 42% of the 2,322-person baseline sample. If exclusion was correlated with baseline characteristics that also predict outcomes, the experimental estimates may not generalize even within the platform from which participants were recruited, let alone to broader populations. The authors must: (a) describe, with actual data, how the 975 individuals differ from the 1,347 randomized individuals on observable characteristics; (b) provide at least a test of mean differences; and (c) clarify whether exclusion was determined before or after baseline data collection.

**5. SUTVA and general-equilibrium / displacement effects not discussed**

The Round 2 should-address feedback called for an explicit treatment of SUTVA and potential displacement effects. The revision does not engage with this. With approximately 600 treated individuals concentrated in local Jordanian labor markets (the setting is identifiable from the Groh et al. 2016 citation and the community college institutional context), vouchers could induce displacement of untreated workers rather than net job creation. The midline employment effect of 39.9 pp, if even partially redistributive, alters the welfare interpretation and the cost-effectiveness calculation substantially. The discussion section must address this at minimum as a scope condition on the headline result.

---

### Minor Comments

1. **Interaction coefficient rounding**: Table 3 reports the mid\_salary interaction as −3.217, while the data output in the evidence packet shows −3.216. This is trivial but should be consistent.

2. **Social security registration heterogeneity**: The endline SSC registration rate is highest in the training-only arm (15.9%) and lowest in the combined arm (11.2%), yet neither the regression results nor the discussion engage with this pattern. If training—but not vouchers—shifts workers toward formal employment, this is an important heterogeneous margin that the null-training narrative obscures.

3. **Confidence interval on interaction**: The paper states that the 95% CI on β₃ for midline employment is approximately [−0.117, +0.087], which it uses to conclude that "we can reject the hypothesis that the combined program is substantially more effective." The authors should clarify what "substantially more effective" means quantitatively, since the upper bound of +8.7 pp on a control mean of 17.8% is not negligible. The claim of ruling out complementarity deserves more precision.

4. **Figure 3 caption discrepancy**: The figure caption for Figure 3 states the no-controls voucher employment effect at endline as +0.034, while the main text and Table 3 report +0.030 (with controls). The robustness section's sensitivity table shows the no-controls estimate is 0.396 at midline; the corresponding endline no-controls estimate should be explicitly reported to make the caption self-contained.

5. **Training mechanism**: The discussion of null training effects (Section 7.2) is useful but generic. Given that the same community college platform delivers both interventions, an observation about whether training-assigned participants actually attended and what the training curriculum covered would sharpen the interpretation. Was the training arm simply co-located with the voucher platform, or did it represent a qualitatively different type of human capital investment?

---

### Missing Literature

- **Crépon, B., Duflo, E., Gurgand, M., Rathelot, R., & Zamora, P. (2013)** is cited but the displacement mechanism it identifies—which is directly relevant to the SUTVA concern—is not engaged with substantively.
- **Darity & Goldsmith (1996)** and subsequent psychological scarring literature on the effects of unemployment spells on LFP—relevant to interpreting why LFP persists even as employment fades.
- **Blundell et al. (2004)** on evaluating active labor market policies with equilibrium effects, directly relevant to the SUTVA gap.
- **Bandiera et al. (2017)** "Labor Markets and Poverty in Village Economies" (QJE) on how wage subsidies interact with informal labor markets—relevant to the low SSC registration finding.

---

### Recommendation

**Major Revision**

The paper is a credible and well-executed RCT with genuinely novel findings on factorial program complementarity. The revision has corrected real problems from Round 2. However, three of the six must-address issues from the previous round remain substantively unresolved (LATE estimates, sample dynamics, control-group LFP decline), and these concern the paper's two central empirical claims: the magnitude of the treatment effect (requires LATE scaling) and its persistence (requires ruling out compositional artifacts). A further revision addressing points 1–5 above would substantially strengthen the paper.

---

```json
{
  "score": 73,
  "decision": "MAJOR_REVISIONS",
  "dimension_scores": {
    "contribution_novelty": 80,
    "literature_positioning": 74,
    "substantive_arguments": 69,
    "external_validity": 66,
    "journal_fit": 74
  },
  "major_comments": [
    "LATE/2SLS estimates are entirely absent despite being a Round 2 must-address requirement. Take-up rates are not reported, making ITT-based effect sizes uninterpretable for cost-effectiveness and policy-budget claims. Authors must report compliance rates by arm and estimate LATE via 2SLS.",
    "The midline-to-endline sample size increase (N=1,207 → N=1,255) is acknowledged but not explained. The mechanism — re-contact, refreshment sample, administrative additions — has direct implications for the validity of the fade-out result and must be disclosed and assessed.",
    "The 29 pp decline in control-group LFP from midline (77.1%) to endline (48.0%) is never explained. This anomaly is larger than the persistent treatment effect itself and could reflect survey seasonality, compositional change from unexplained sample additions, or differential attrition. The LFP persistence headline result is uninterpretable until this is ruled out as an artifact.",
    "The 975 excluded individuals (42% of the 2,322-person baseline) are described only as 'likely' excluded due to eligibility screening or logistical constraints. Authors must characterize who these individuals are relative to the randomized sample on observable baseline characteristics."
  ],
  "minor_comments": [
    "Mid-salary interaction coefficient is -3.217 in paper vs -3.216 in data output — trivial but should be consistent.",
    "Social security registration is highest in training-only arm (15.9%) and lowest in combined arm (11.2%). This pattern cuts against the null-training narrative and deserves at least a sentence of discussion.",
    "The 95% CI on the midline employment interaction [-0.117, +0.087] is stated to rule out 'meaningful complementarity'; the upper bound of +8.7 pp on a 17.8% control mean is non-negligible and the threshold for 'meaningful' should be stated explicitly.",
    "Figure 3 caption reports the no-controls endline voucher employment effect as +0.034 while Table 3 (with controls) reports +0.030. These should be reconciled or distinguished.",
    "SUTVA and general-equilibrium displacement effects are not discussed anywhere in the paper despite being raised in the Round 2 should-address comments. With ~600 treated individuals concentrated in local labor markets, the welfare interpretation of the headline result requires at least a qualitative treatment of this concern."
  ],
  "missing_literature": [
    "Blundell et al. (2004) on evaluating ALMPs with equilibrium effects — directly relevant to SUTVA gap.",
    "Bandiera et al. (2017, QJE) 'Labor Markets and Poverty in Village Economies' — relevant to low SSC registration and informal employment finding.",
    "Darity & Goldsmith (1996) on scarring effects of unemployment on LFP — relevant to interpreting persistent LFP effect after employment fade-out."
  ]
}
```