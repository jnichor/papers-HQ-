## Referee Report

### Summary

This paper tests whether commodity price busts permanently erode civil liberties using an asymmetric event study across 80 commodity-dependent countries (1975–2018). The author disaggregates political outcomes into five civil liberty dimensions and exploits exogenous variation from the IMF's Commodity Terms of Trade (CTOT) index. The central finding is that busts selectively erode fair trial rights (β = −0.199, p = 0.020) while leaving the other four liberties statistically unaffected, and that an initial "ratchet effect" for freedom of movement does not survive COVID-era exclusion or placebo tests.

---

### Main Assessment

**Strengths.** The disaggregated approach to civil liberties is the paper's most significant contribution. Using five distinct liberty dimensions rather than a composite democracy index allows the author to identify heterogeneity that aggregate indices obscure. The CTOT instrument is well-motivated as a source of plausibly exogenous variation, the COVID-era robustness check is properly handled, and the pre-trend evidence is credibly reported. The paper is also unusually candid about its limitations—the placebo test inconsistency and power concerns are disclosed rather than buried.

**Weaknesses.** The paper's central finding rests on a significant internal tension: the permutation (placebo) p-value for fair trial (p = 0.389) is far above the parametric p-value (p = 0.020). This gap is acknowledged but systematically understated. Separately, for the paper's headline outcome (fair trial), the event-study bust average is *positive* (+0.489) while the TWFE coefficient is *negative* (−0.199). The offered explanation—sample composition and reference-period normalization—is insufficient for a sign reversal. The mechanism linking busts to judicial erosion is asserted rather than tested. Missing engagement with the judicial independence and political economy of resources literatures is a further gap.

---

### Major Comments

**1. Permutation test failure is more consequential than acknowledged.**
The author reports a fair trial placebo p-value of 0.389, meaning that 38.9% of 999 random permutations of bust timing yield a coefficient at least as extreme as the observed one. This is not "consistent with a modest effect"—it is a permutation-based non-result. The discrepancy with the parametric p = 0.020 almost certainly reflects serial correlation in the outcome that the cluster-robust SEs inadequately absorb even with 80 clusters. The author should either (a) reconcile the two p-values explicitly with a diagnostic (e.g., compare AR(1) residuals before and after busts), or (b) treat the permutation test as the preferred inference and acknowledge that the fair trial result does not survive it. As written, the paper selectively reports the parametric result in the abstract and introduction while burying the permutation failure in the robustness section.

**2. The sign reversal between TWFE and event-study requires a dedicated subsection.**
Table 2 shows that for fair trial, the event-study bust average is +0.491 (improvement), yet the TWFE coefficient is −0.199 (deterioration). For freedom of movement, both event-study averages are negative, yet the TWFE coefficient is near zero (−0.009). The current one-paragraph reconciliation invoking "sample composition" and "reference-period normalization" is inadequate for results that point in opposite directions. A sign reversal is not a quantitative discrepancy; it requires the author to show precisely which countries/episodes enter the event study but not the TWFE, and why their inclusion reverses the sign. If this cannot be shown transparently, the paper cannot simultaneously use TWFE as the "preferred causal estimate" and the event study for "dynamics"—the two specifications are telling contradictory stories for the headline outcome.

**3. Staggered TWFE dismissal is too casual.**
The author argues that transitory (non-absorbing) treatments mitigate the negative-weighting bias identified by Callaway-Sant'Anna and Sun-Abraham. This is a reasonable intuition but incomplete. Heterogeneous treatment effects across cohorts can still contaminate TWFE estimates even when treatments are transitory, particularly when episodes cluster by decade (e.g., oil-producing states in the early 1980s bust). At minimum, a Goodman-Bacon (2021) decomposition showing the share of the TWFE estimate attributable to "clean" 2×2 comparisons versus "forbidden comparisons" would substantially strengthen the identification claim. The argument as written asserts that standard estimators are inapplicable without providing the diagnostic evidence.

**4. Missing engagement with the judicial independence literature.**
The paper's central interpretive claim—that executives strategically target courts during fiscal crises—is compelling but entirely unsupported by citations. A substantial literature on judicial independence and political economy is absent: Ríos-Figueroa (2011) on judicial corruption and executive relations; Helmke (2002, 2005) on strategic defection in Argentine courts; Epperly (2019, *Journal of Politics*) specifically on economic conditions and judicial independence; Staton and Moore (2011) on judicial power and rights protection. Without engaging this literature, the mechanism remains speculative. The author need not demonstrate the mechanism empirically, but should position the finding relative to existing theoretical accounts.

**5. Missing literature on the resource curse and democracy.**
The paper cites Ross (2015) as a survey but omits foundational and revisionist work: Ross (2001), which established the oil–democracy relationship; Haber and Menaldo (2011, *American Political Science Review*), which contested it using within-country variation; Ramsay (2011, *Journal of Politics*), which raised endogeneity concerns; and Morrison (2009) on non-tax revenue and regime stability. The contribution claim ("commodity busts erode democratic governance") must be positioned relative to this debate, particularly the Haber-Menaldo critique that resource-democracy correlations are driven by cross-country heterogeneity rather than within-country dynamics.

**6. Unexplained sample reduction for fair trial (N = 6,824 vs. 7,330).**
The fair trial specification uses 506 fewer observations than the other four outcomes. This is a non-trivial difference (approximately 7% of the sample) and is unexplained anywhere in the paper. If fair trial data are missing non-randomly—e.g., if the V-Dem coders have less coverage for authoritarian regimes where such rights are most contested—this could introduce selection bias precisely in the direction of attenuating the true effect, or alternatively inflating it if coverage correlates with crisis periods. The author must characterize the missing data pattern.

---

### Minor Comments

**1. The 1–4 ordinal scale deserves acknowledgment.** Using OLS on a bounded four-point ordinal outcome is standard in political science but introduces a compression bias near ceiling and floor values. Given that movement (mean 3.16) and religion (mean 3.27) have means well above the midpoint, the null results for these outcomes may partly reflect ceiling effects rather than genuine insensitivity to busts. An ordered probit robustness check, or at least acknowledgment of this limitation, would strengthen the paper.

**2. Bust episode sparsity should be reported.** With 31 episodes across 80 countries, an average of 0.39 busts per country, the event study estimates for each horizon coefficient are identified from very few observations. The paper should report the effective N contributing to the endpoints of the event study window (k = −3 and k = +5), where compositional changes in the estimation sample are most severe.

**3. The title overpromises.** "Commodity Busts and the Selective Erosion of Civil Liberties" implies the paper establishes selective erosion across the sample period. Given that the main result does not survive the permutation test and the event-study sign is reversed from TWFE, a more accurate title might reference the "differential" or "asymmetric" response rather than confirmed "erosion."

**4. JEL classification.** Given the paper's substantial focus on judicial independence, adding K40 (Legal Procedure, the Courts, and Judicial Behavior) would improve discoverability.

**5. The symmetry test formula in equation (2) is mislabeled.** The null H₀: β̄ᵇᵘˢᵗₚₒₛₜ + β̄ʳᵉᶜᵒᵛᵉʳʸₚₒₛₜ = 0 is formally equivalent to H₀: β̄ᵇᵘˢᵗₚₒₛₜ = −β̄ʳᵉᶜᵒᵛᵉʳʸₚₒₛₜ, which is symmetric effects. This is correct as stated, but the paper should be explicit that this formulation assumes the recovery is measured as a positive change, and clarify that the asymmetry column in Table 2 reports the sum rather than the difference, which is non-standard.

**6. COVID-19 robustness is correctly handled but should reference institutional literature.** The decision to exclude 2020–2021 is well-motivated. However, some governments used COVID emergency powers precisely to delay or suspend judicial proceedings, which means COVID contamination may affect fair trial rights as well as movement—in the direction of *strengthening* the fair trial result during 2020–2021. The author should check whether excluding COVID years changes the fair trial estimate substantially (the change from −0.199 to −0.189 is small, suggesting it does not, but this should be noted explicitly).

---

### Missing Literature

- Haber and Menaldo (2011, *APSR*): "Do Natural Resources Fuel Authoritarianism?" — core revisionist paper on resources and democracy
- Ramsay (2011, *JOP*): "Oil, Islam, and Women" / oil and democracy endogeneity
- Ross (2001): Original oil-democracy paper, more foundational than the 2015 survey cited
- Epperly (2019, *JOP*): Economic conditions and judicial independence
- Helmke (2002, *APSR*): Strategic defection in courts — mechanism for judicial erosion
- Ríos-Figueroa (2011): Judicial institutions and executive oversight
- Morrison (2009): Non-tax revenue and authoritarian stability
- Guriev and Treisman (2019): Informational autocracy — relevant for selectivity in repression
- Brancati (2014) or Pepinsky (2009) on economic crises and democratic breakdown

---

### Recommendation

**Major Revision.** The disaggregated empirical design and the COVID-era robustness check are genuine contributions. However, the permutation test failure for the headline result, the unexplained TWFE/event-study sign reversal, and the missing judicial independence literature collectively require substantial revision before the paper is ready for publication.

---

```json
{
  "score": 62,
  "decision": "MAJOR_REVISIONS",
  "dimension_scores": {
    "contribution_novelty": 80,
    "literature_positioning": 58,
    "substantive_arguments": 52,
    "external_validity": 68,
    "journal_fit": 72
  },
  "major_comments": [
    "Permutation test failure (p=0.389) contradicts parametric p=0.020 for fair trial; discrepancy suggests serial correlation in errors that cluster-robust SEs fail to absorb; paper understates severity by describing this as 'consistent with a modest effect'.",
    "Sign reversal between TWFE (β=-0.199) and event-study bust average (+0.491) for the headline outcome (fair trial) is unexplained; one-paragraph appeal to 'sample composition and reference-period normalization' is inadequate for opposite-signed results.",
    "Staggered TWFE dismissal is asserted without diagnostic evidence; a Goodman-Bacon decomposition showing clean vs. forbidden 2x2 comparisons is needed to support the claim that transitory treatment status eliminates negative-weighting concerns.",
    "The executive-targeting-of-courts mechanism is the paper's central interpretive contribution but has no supporting citations; key judicial independence literature (Epperly 2019, Helmke 2002/2005, Ríos-Figueroa 2011) is entirely absent.",
    "Missing engagement with revisionist resource-curse-and-democracy literature (Haber and Menaldo 2011 APSR, Ramsay 2011 JOP) makes the contribution claim impossible to evaluate relative to existing evidence.",
    "Unexplained 506-observation reduction for fair trial (N=6,824 vs 7,330) raises potential selection concerns; missing data pattern must be characterized and its implications for inference discussed."
  ],
  "minor_comments": [
    "OLS on 1-4 ordinal outcomes near ceiling (movement mean=3.16, religion mean=3.27) may attenuate null results via compression; ordered probit robustness or explicit acknowledgment warranted.",
    "Effective N at event-study window endpoints (k=-3, k=+5) should be reported given sparse episode count (31 episodes / 80 countries).",
    "Title 'Selective Erosion' overstates a finding that does not survive the permutation test; revision should use more hedged language.",
    "JEL K40 (Legal Procedure and Judicial Behavior) should be added given the paper's judicial independence interpretation.",
    "Symmetry test null in equation (2) is correct but non-standard; clarify that asymmetry column reports sum rather than difference, and confirm sign convention for recovery episodes.",
    "COVID exclusion may also affect fair trial through emergency suspension of judicial proceedings; confirm this does not bias the direction of the fair trial result."
  ],
  "missing_literature": [
    "Haber and Menaldo (2011, APSR) - revisionist resource-curse and democracy paper using within-country variation",
    "Ramsay (2011, JOP) - oil and democracy endogeneity critique",
    "Ross (2001, World Politics) - foundational oil-democracy paper more central than the 2015 survey",
    "Epperly (2019, JOP) - economic conditions and judicial independence",
    "Helmke (2002, APSR; 2005 book) - strategic judicial defection under executive pressure",
    "Ríos-Figueroa (2011) - judicial corruption and executive relations in comparative context",
    "Morrison (2009) - non-tax revenue and authoritarian regime stability",
    "Guriev and Treisman (2019, JEP) - informational autocracy and selective repression"
  ]
}
```