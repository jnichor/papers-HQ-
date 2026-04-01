## Referee Report

**Journal:** Working Paper Review
**Title:** "The Ratchet Effect: Commodity Busts Erode Civil Liberties That Booms Do Not Restore"

---

### Summary

This paper tests whether commodity price busts produce asymmetric, path-dependent erosion of civil liberties using an asymmetric event study on 80 commodity-dependent countries over 1975–2024. The author disaggregates political outcomes into five liberty dimensions from the Civil Liberty Dataset and exploits exogenous variation in the IMF's Commodity Terms of Trade index. The main claim is that freedom of movement exhibits a statistically significant ratchet effect (bust erosion unreversed by recovery), while fair trial rights significantly deteriorate during busts.

---

### Main Assessment

The paper addresses a genuinely important question—whether commodity-driven democratic erosion is cyclical or cumulative—and the disaggregated, asymmetric design is a meaningful methodological contribution over the existing resource curse literature. However, the paper contains a critical internal inconsistency that undermines confidence in the core results, does not engage with the modern staggered difference-in-differences literature that directly threatens identification, and mischaracterizes the symmetry test results for four of five liberty dimensions. These are not minor presentation issues; they require substantive revision before the empirical claims can be taken at face value.

---

### Major Comments

**1. Critical Internal Inconsistency Between Table 1 and Table 2 (TWFE vs. Event Study)**

The most serious problem in the paper is an unaddressed sign reversal between the TWFE estimates and the event study averages for fair trial rights. Table 1 reports a TWFE bust coefficient of −0.199 (p = 0.020), indicating that busts *reduce* fair trial rights. Table 2 reports an event study bust average of +0.489 for the same outcome, indicating that busts *improve* fair trial rights by nearly half a point in the post-episode window. This is not a small discrepancy—the sign is opposite and the magnitude is more than twice as large. The paper discusses both results without acknowledging or explaining this inconsistency.

The likely explanation is that the event study compares post-bust periods to t = −1, and if the 3-year cumulative threshold creates a reference period (t = −1) that is already significantly below the long-run country mean (because the CTOT decline was gradual), post-bust coefficients can be mechanically positive even as the absolute level remains depressed. This would constitute a reference period bias that invalidates the event study interpretation. The author must demonstrate that t = −1 levels are not anomalously low and reconcile the TWFE and event study estimates explicitly.

**2. Staggered DiD Bias Not Addressed**

The identification relies on two-way fixed effects (TWFE) with staggered episode timing. Since Goodman-Bacon (2021), Callaway and Sant'Anna (2021), and Sun and Abraham (2021), it is well established that TWFE estimates in staggered settings are weighted averages of heterogeneous treatment effects that can be negatively weighted when treatment effects vary across cohorts or over time—precisely the heterogeneous dynamics the paper is trying to document. This literature is entirely absent from the paper.

Given that the paper's central claim is that effects are asymmetric (busts ≠ recoveries), the heterogeneous treatment effects concern is not hypothetical—it is directly relevant. The author should either implement a heterogeneity-robust estimator (e.g., Callaway-Sant'Anna stacked regression) or provide a detailed argument for why conventional TWFE is adequate in this specific setting.

**3. Symmetry Test Mischaracterized for Four of Five Liberties**

Table 2 reports that symmetry is rejected (p < 0.001) for assembly, religion, and fair trial, but inspection reveals that for these three dimensions, *both* the bust average and the recovery average are positive. For assembly, bust avg = +0.369 and recovery avg = +0.408. This is not a ratchet—it is an asymmetric *improvement* in two liberties that happen to improve at different rates during busts and recoveries. Labeling this as evidence of a "pervasive ratchet effect" is incorrect.

The only dimension consistent with the paper's narrative is freedom of movement (bust avg = −0.220, recovery avg = −0.024), where the bust causes deterioration that is not reversed. The paper's conclusion that "pervasive asymmetry across liberty dimensions challenges the implicit assumption of symmetric political oscillations" over-interprets the symmetry rejections for non-movement liberties. The abstract, introduction, and conclusion should be revised to accurately represent that the ratchet finding applies to one dimension.

**4. COVID-19 and Post-2018 Period**

The strategy memo indicates the original sample was 1975–2018, but the paper claims 1975–2024. If the post-2018 years are included, the 2020 commodity price collapse (oil briefly negative) and the COVID-19-induced emergency restrictions on civil liberties—including movement restrictions adopted independently of commodity conditions—are major confounders for the exact liberty dimension showing the ratchet effect. The paper must clarify the sample period and, if post-2018 data is used, address the COVID-19 period explicitly (e.g., with a post-2019 exclusion robustness check).

**5. Sparsity of Episodes and Cluster Size**

With 31 bust episodes and 21 recovery episodes across 80 countries, the average country experiences 0.39 busts and 0.26 recoveries. This means the identification is driven by a small subset of countries with multiple episodes. With N = 80 clusters, conventional cluster-robust inference may be unreliable (Cameron and Miller 2015 recommend caution below 50 clusters that are genuinely heterogeneous). The paper should report wild cluster bootstrap p-values (Roodman et al. 2019) alongside standard cluster-robust SEs, particularly for the fair trial and movement results that are close to conventional significance thresholds.

---

### Minor Comments

1. **Peacock-Wiseman citation missing.** The paper invokes the displacement effect but does not give the original reference: Peacock, A. and J. Wiseman (1961), *The Growth of Public Expenditure in the United Kingdom*.

2. **Haber-Menaldo debate absent.** Haber and Menaldo (2011, "Do Natural Resources Fuel Authoritarianism?", *American Political Science Review*) directly challenges the resource curse hypothesis using within-country fixed effects. The paper should engage with this debate rather than treating the resource curse as settled.

3. **Caselli and Tesei (2016) not cited.** "Resource Windfalls, Political Regimes, and Political Stability" (*Review of Economics and Statistics*) provides direct evidence on asymmetric effects of commodity windfalls on regime type and is highly relevant to the paper's mechanism.

4. **Path dependence theory.** The paper invokes institutional path dependence as the mechanism for the ratchet but does not cite foundational work: Pierson (2000, "Increasing Returns, Path Dependence, and the Study of Politics," *APSR*) and North (1990, *Institutions, Institutional Change and Economic Performance*).

5. **Scale inconsistency.** The paper text describes the CLD as an "ordinal (1–4) scale" while the strategy memo states "(0–4 scale)." The summary statistics confirm min = 1.0, supporting 1–4, but this should be stated consistently throughout.

6. **Placebo test scope.** The reported placebo test covers only freedom of expression (the insignificant result). A more informative placebo would randomize bust dates for freedom of movement and fair trial—the paper's two claimed positive findings.

7. **Episode overlap.** The paper does not address whether bust and recovery episodes can overlap across countries in the same year, and whether this creates econometric complications for the joint symmetry test.

8. **Positive bust effects unexplained.** Three liberties (expression, assembly, religion) show positive event study bust averages. The paper never discusses why civil liberties in these dimensions might *improve* during commodity busts. An interpretation—even a brief one—is warranted, as it contradicts the paper's general framing.

---

### Missing Literature

- Haber, S. and V. Menaldo (2011). "Do Natural Resources Fuel Authoritarianism?" *APSR* 105(1): 1–26.
- Caselli, F. and A. Tesei (2016). "Resource Windfalls, Political Regimes, and Political Stability." *Review of Economics and Statistics* 98(3): 573–590.
- Goodman-Bacon, A. (2021). "Difference-in-differences with variation in treatment timing." *Journal of Econometrics* 225(2): 254–277.
- Callaway, B. and P.H.C. Sant'Anna (2021). "Difference-in-Differences with multiple time periods." *Journal of Econometrics* 225(2): 200–230.
- Sun, L. and S. Abraham (2021). "Estimating dynamic treatment effects in event studies with heterogeneous treatment effects." *Journal of Econometrics* 225(2): 175–199.
- Pierson, P. (2000). "Increasing Returns, Path Dependence, and the Study of Politics." *APSR* 94(2): 251–267.
- Ross, M. (2004). "Does Oil Hinder Democracy?" *World Politics* 53(3): 325–361.
- Roodman, D., M.Ø. Nielsen, J.G. MacKinnon, and M.D. Webb (2019). "Fast and wild: Bootstrap inference in Stata using boottest." *The Stata Journal* 19(1): 4–60.
- Davenport, C. (2007). "State Repression and the Domestic Democratic Peace." Cambridge University Press.

---

### Recommendation

**Major Revision**

The paper addresses a compelling question with a novel empirical design, and the freedom of movement ratchet finding is potentially important. However, the unreconciled sign reversal between the TWFE and event study estimates for fair trial rights, the absence of any engagement with the staggered DiD heterogeneity literature, and the systematic mischaracterization of the symmetry test results for non-movement liberties represent substantive problems that prevent acceptance in the current form. The author should (a) reconcile or explain the TWFE/event study discrepancy, (b) implement a heterogeneity-robust event study estimator or defend conventional TWFE, (c) revise the framing of the symmetry results to distinguish ratchets from asymmetric improvements, and (d) address the post-2018 sample period concern.

---

```json
{
  "score": 65,
  "decision": "MAJOR_REVISIONS",
  "dimension_scores": {
    "contribution_novelty": 74,
    "literature_positioning": 62,
    "substantive_arguments": 57,
    "external_validity": 63,
    "journal_fit": 68
  },
  "major_comments": [
    "Critical internal inconsistency: TWFE (Table 1) reports fair trial bust coefficient = -0.199, but event study symmetry table (Table 2) reports fair trial bust average = +0.489 — opposite sign, larger magnitude. This is unaddressed in the paper and likely reflects reference-period bias at t=-1 due to gradual pre-bust CTOT decline. Authors must reconcile these estimates or the empirical claims are unreliable.",
    "Staggered DiD not addressed: The paper uses TWFE with staggered episode timing but never engages with Goodman-Bacon (2021), Callaway-Sant'Anna (2021), or Sun-Abraham (2021). Given the paper's central claim of heterogeneous and time-varying treatment effects, TWFE estimates may be contaminated by negative-weight comparisons. A heterogeneity-robust estimator is required or a detailed defense of TWFE must be provided.",
    "Symmetry test mischaracterized: For assembly, religion, and fair trial, both bust and recovery event study averages are positive — this is asymmetric improvement, not a ratchet. The ratchet narrative applies only to freedom of movement. Abstract, introduction, and conclusion overstate the pervasiveness of the ratchet pattern and must be revised accordingly.",
    "COVID-19 and post-2018 period: Strategy memo indicates original sample ends 2018 but paper claims 1975-2024. If post-2018 is included, the 2020 COVID-19 emergency movement restrictions are a major confounder for exactly the liberty dimension (movement) showing the ratchet effect. The sample period must be clarified and a COVID-era exclusion robustness check reported.",
    "Episode sparsity and clustering: 31 busts and 21 recoveries across 80 countries yields thin identification. With N=80 clusters, wild cluster bootstrap inference (Roodman et al. 2019) should be reported alongside cluster-robust SEs, particularly for movement and fair trial results near conventional significance thresholds."
  ],
  "minor_comments": [
    "Peacock-Wiseman displacement effect invoked without original citation (Peacock and Wiseman 1961).",
    "Haber-Menaldo (2011) resource curse challenge is the central debate in this literature and is entirely absent.",
    "Positive bust effects on expression, assembly, and religion (visible in Table 2) are never discussed — the paper's framing that busts erode liberties is inconsistent with this pattern for three of five outcomes.",
    "Placebo test covers only the insignificant expression result; a placebo for movement and fair trial (the significant findings) would be more informative.",
    "Scale inconsistency: paper text says 1-4, strategy memo says 0-4. Summary statistics confirm 1-4 minimum; use consistent language throughout.",
    "Episode overlap across countries in the same year not discussed — possible complications for the symmetry test.",
    "Caselli and Tesei (2016) on asymmetric commodity windfalls and regime stability is directly relevant and missing.",
    "Pierson (2000) and North (1990) are foundational references for the path dependence mechanism invoked in the discussion and should be cited."
  ],
  "missing_literature": [
    "Haber, S. and Menaldo, V. (2011). Do Natural Resources Fuel Authoritarianism? APSR 105(1): 1-26.",
    "Caselli, F. and Tesei, A. (2016). Resource Windfalls, Political Regimes, and Political Stability. Review of Economics and Statistics 98(3): 573-590.",
    "Goodman-Bacon, A. (2021). Difference-in-differences with variation in treatment timing. Journal of Econometrics 225(2): 254-277.",
    "Callaway, B. and Sant'Anna, P.H.C. (2021). Difference-in-Differences with multiple time periods. Journal of Econometrics 225(2): 200-230.",
    "Sun, L. and Abraham, S. (2021). Estimating dynamic treatment effects in event studies with heterogeneous treatment effects. Journal of Econometrics 225(2): 175-199.",
    "Pierson, P. (2000). Increasing Returns, Path Dependence, and the Study of Politics. APSR 94(2): 251-267.",
    "Ross, M. (2004). Does Oil Hinder Democracy? World Politics 53(3): 325-361.",
    "Roodman, D. et al. (2019). Fast and wild: Bootstrap inference in Stata using boottest. Stata Journal 19(1): 4-60.",
    "Davenport, C. (2007). State Repression and the Domestic Democratic Peace. Cambridge University Press."
  ]
}
```