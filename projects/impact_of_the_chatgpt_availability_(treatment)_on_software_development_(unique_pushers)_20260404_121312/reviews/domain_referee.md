## Referee Report

**Journal of Economic Policy / Journal of Development Economics (domain: economics of technology, digital markets)**

---

### Summary

This paper exploits policy-imposed ChatGPT access restrictions—persistent blocks in China, Russia, Iran, Syria, and Cuba, and Italy's 28-day temporary ban—as a natural experiment to estimate the causal effect of generative AI availability on open-source software development. Using a 177-country panel of GitHub push activity over 23 quarters (Q1 2020–Q3 2025), the authors implement a two-way fixed effects difference-in-differences design and a synthetic control for Italy. The baseline DiD estimate is −0.389 log points (marginally insignificant conventionally but p=0.006 via permutation), with large country-specific effects for China (−1.386) and Russia (−0.549) and a null for Italy's temporary ban.

---

### Main Assessment

The paper addresses a timely and genuinely important question. The authors deserve credit for unusual transparency: they disclose pre-trend violations, the OECD null result, and inability to separate ChatGPT effects from concurrent geopolitical shocks. However, this transparency also reveals that the identification problems are more severe than a minor-revision program can address. The pre-trend violation (p=0.0003) combined with the OECD-only null (p=0.922) together constitute a fundamental credibility problem that permutation inference cannot resolve. Russia's inclusion as a treated unit is untenable given that the Russia-Ukraine war—with its documented IT-sector brain drain—predates ChatGPT by nine months. China's estimated 75% reduction in GitHub pushers strains credulity absent engagement with VPN circumvention and Gitee migration evidence. The paper requires substantially improved identification or repositioning as a descriptive study before publication.

---

### Major Comments

**1. The pre-trend violation is not adequately addressed and the diagnosis is internally inconsistent.**

The joint F-test rejects parallel pre-trends at p=0.0003, which fundamentally undermines the DiD design. Yet the paper simultaneously claims "individual pre-period coefficients are small and individually insignificant." These two claims are in tension: if individual pre-period interactions are economically trivial, the joint rejection is being driven by the large number of pre-period dummies (10 dummies, many with CIs spanning ±0.5–0.9 log points), not by systematic divergence. The paper needs to clearly diagnose which pre-periods drive the rejection and conduct a formal sensitivity analysis. Rambachan and Roth (2023, *Review of Economic Studies*, "A More Credible Approach to Parallel Trends") provide the appropriate tools to bound the treatment effect under restrictions on the magnitude of pre-trend violations. This is not optional given the formal rejection.

**2. The OECD-null result is the most informative finding and deserves to be the central analysis, not a robustness footnote.**

When the control group is restricted to OECD-comparable countries, the estimated effect is −0.026 (p=0.922). This is not a minor sensitivity check—it is the result of comparing treated countries to their most economically similar peers, which is the conceptually correct comparison group for DiD. The fact that the effect vanishes entirely strongly suggests the baseline result reflects divergent development trajectories between restricted countries (which are a mix of authoritarian states with tech crackdowns, sanctioned economies, and geopolitical pariahs) and the global average of 172 developing countries. The paper needs to directly confront this alternative: construct a matched control group using pre-ChatGPT GDP per capita, internet penetration, and GitHub activity growth rates, rather than accepting the status quo of either all countries or only OECD.

**3. Russia is not a valid treated unit for this identification design.**

The Russia-Ukraine war began February 24, 2022—nine months before ChatGPT's November 30, 2022 launch. During 2022 Q1–Q3 (the paper's pre-treatment period), Russia experienced large-scale IT-sector emigration (industry estimates of 50,000–100,000 developers departing), international sanctions disrupting software licensing and payment infrastructure, and withdrawal of major development tool providers. These shocks broke Russia's GitHub growth trend before the treatment began, creating a mechanically violated pre-trend that the paper's design cannot correct for. The event study's Q4 2022 coefficient of −0.163 (p=0.009)—the very first post-ChatGPT quarter—is better explained by the cumulative effect of nine months of war-driven emigration than by one month of ChatGPT unavailability. Russia should either be excluded from the main specification with its own clearly caveated analysis, or the authors should provide direct evidence (e.g., using GitHub data on developer location changes or Russian IT employment records) that emigration does not explain the pattern.

**4. China's GitHub decline is better explained by Gitee migration than by ChatGPT restriction, and the paper does not test this.**

The estimated −1.386 log-point effect for China implies a 75% reduction in Chinese developer activity on GitHub—an extraordinary magnitude given that China has one of the world's largest developer ecosystems and sophisticated VPN infrastructure. The Chinese government began actively promoting Gitee as a domestic GitHub alternative in 2020–2021, with mandatory registration of open-source projects on domestic platforms enacted in regulation. If Gitee migration is the primary mechanism, the decline should be observable before Q4 2022. The paper's own event study is relevant here: Q4 2022 shows −0.163 (p=0.009) immediately at ChatGPT launch, with ChatGPT releasing November 30—giving developers fewer than 30 days to change workflows within the quarter. This timing is more consistent with a pre-existing migration trend than with a rapid ChatGPT-access response. The authors should directly test whether GitHub counts for China began declining before Q4 2022 and whether the decline is concentrated in the types of repositories (e.g., public open-source vs. corporate) consistent with platform migration rather than productivity loss.

**5. Missing critical literature on information access and VPN circumvention in China.**

Chen and Yang (2019, *Quarterly Journal of Economics*, "The Impact of Media Censorship: 1984 or Brave New World?") is essential reading for this paper and is absent from the literature review. They provide direct experimental evidence on VPN usage patterns among Chinese internet users and quantify the degree to which censorship is binding even on technically sophisticated users. Given that Chinese developers are disproportionately technically sophisticated, VPN circumvention may substantially attenuate the ChatGPT treatment, making −1.386 log points either (a) a severe overestimate of the ChatGPT-specific effect, or (b) entirely driven by Gitee migration and other factors. The paper acknowledges VPN attenuation qualitatively but does not engage with the empirical literature that could quantify it. Hjort and Poulsen (2019, *American Economic Review*, "The Arrival of Fast Internet and Employment in Africa") is the closest methodological parallel in this literature for estimating internet access effects on economic outcomes and should be cited.

**6. The identical standard errors for the China-only and Russia-only specifications are a data quality concern.**

Table 2 reports SE = 0.036 for both the China-only estimate (−1.386) and the Russia-only estimate (−0.549). These are separate regressions with different treatment country compositions, different control samples (N=3,494 in both, suggesting only the non-treated unit is dropped each time), and different coefficient magnitudes, yet identical standard errors to three decimal places. With one treated country and country-level clustering, the SE computation is non-standard. The authors must verify these are correctly computed—identical SEs across these two regressions are statistically implausible under correct clustered SE computation with one treated cluster.

---

### Minor Comments

1. **Permutation test precision.** With 500 draws from C(177,5) ≈ 10¹⁰ possible assignments, p=0.006 (approximately 3 extreme draws out of 500) is very imprecisely estimated. The authors should use at least 5,000 permutations and report a 95% confidence interval for the permutation p-value. Additionally, unrestricted random treatment assignment may be inappropriate: if China and Russia are outlier-sized developer ecosystems, random assignment will rarely pick equally large countries, making the test reject trivially because of size differences rather than ChatGPT effects.

2. **Synthetic control weight on Greece.** Italy's synthetic counterpart assigns 15% weight to Greece. Given the large disparity in developer ecosystem size between Italy and Greece, this weight deserves explanation. The authors should report the full weight vector and discuss whether Greece's inclusion reflects genuine pre-treatment trajectory similarity or a numerical artifact.

3. **Economic magnitude should be reported in levels for China.** A −1.386 log-point decline is technically correct but opaque. The paper should provide China's actual vs. counterfactual pushers in levels (e.g., "China had X actual pushers in Q3 2025 versus a counterfactual of Y") to allow readers to evaluate whether the implied magnitude is plausible.

4. **Incorrect JEL code.** F13 (Commercial Policy, Protection, Trade Negotiations) is not appropriate for this paper. Replace with O38 (Government Policy, Technological Change) or F68 (Economic Impacts of Globalization). O33 and J24 are correct.

5. **The growing post-treatment gap (reaching −0.80 by Q3 2025) conflates ChatGPT with 12 quarters of accumulating tech decoupling.** As the post-treatment window extends through 2024–2025, China's increasing tech nationalism (Gitee mandates, domestic cloud requirements) and Russia's continued economic isolation provide alternative explanations for widening divergence. The paper's "cumulative disadvantage" interpretation of the growing gap is speculative without controlling for these time-varying confounders.

6. **Synthetic control inference.** The paper should cite Abadie, Diamond, and Hainmueller (2010, *JASA*) and the methodological review Abadie (2021, *Journal of Economic Literature*) in addition to the current single Abadie (2010) citation. Inference via in-space permutation (as in Abadie et al. 2010) should be reported for the Italy SCM.

7. **Low within-R².** The R² of 0.012 should be discussed more explicitly. The two-way FE design absorbs nearly all variation, leaving the treatment coefficient to explain 1.2% of residual variance. While not a flaw per se, this reinforces that country and quarter trends—not ChatGPT restrictions—account for essentially all observable variation in the panel.

---

### Missing Literature

- **Chen and Yang (2019, QJE)** — Essential on VPN circumvention in China; directly relevant to treatment attenuation
- **Hjort and Poulsen (2019, AER)** — Closest methodological parallel for internet access and economic outcomes; methodological benchmark
- **Rambachan and Roth (2023, ReStud)** — Pre-trend sensitivity analysis; mandatory given the formal rejection of parallel trends
- **Abadie, Diamond, Hainmueller (2010, JASA) and Abadie (2021, JEL)** — Synthetic control methods and inference
- **Goldfarb and Tucker (2019, JEL, "Digital Economics")** — Framework for digital regulation and economic consequences; would strengthen Section 2
- **Literature on Russian IT emigration post-2022** — Required to properly assess whether Russia belongs in the treatment group

---

### Recommendation: Major Revision

```json
{
  "score": 65,
  "decision": "MAJOR_REVISIONS",
  "dimension_scores": {
    "contribution_novelty": 78,
    "literature_positioning": 62,
    "substantive_arguments": 58,
    "external_validity": 64,
    "journal_fit": 70
  },
  "major_comments": [
    "Pre-trend violation (p=0.0003) is not adequately addressed. The internally inconsistent claim that individual coefficients are small but joint test rejects requires formal Rambachan-Roth sensitivity analysis, not verbal dismissal.",
    "The OECD-null result (p=0.922) is the most informative finding and should be the central robustness test, not a footnote. Effect vanishing against comparable peers strongly suggests general divergent trajectories rather than ChatGPT-specific effects.",
    "Russia is not a valid treated unit. The Russia-Ukraine war (February 2022) and associated IT-sector emigration predate ChatGPT by nine months, breaking Russia's pre-treatment trend before the design's post period begins.",
    "China's GitHub decline is more plausibly explained by Gitee migration (a government-promoted domestic alternative active since 2020-2021) than by ChatGPT restriction. The paper does not test whether the decline began before Q4 2022 or is concentrated in migration-consistent repository types.",
    "Critical VPN circumvention literature (Chen and Yang, 2019, QJE) is absent. Chinese developers' technical sophistication makes the treatment non-binding for a significant share of the population, undermining the -1.386 magnitude estimate.",
    "The identical standard errors (SE=0.036) for China-only and Russia-only regressions are statistically implausible and suggest a possible coding error in the clustered SE computation."
  ],
  "minor_comments": [
    "Permutation test should use ≥5,000 draws with a reported confidence interval for the p-value; unrestricted random assignment may favor rejection due to China/Russia being outlier-sized ecosystems.",
    "Synthetic Italy weight of 15% on Greece is unexpectedly large given size disparity; full weight vector and justification should be reported.",
    "China's -1.386 estimate should be translated into levels (actual vs. counterfactual pushers) for readers to evaluate plausibility.",
    "JEL code F13 (Commercial Policy, Trade Negotiations) is incorrect for this paper; replace with O38 or F68.",
    "The growing post-treatment gap through 2024-2025 conflates ChatGPT with accumulating tech decoupling and should not be labeled 'cumulative disadvantage' without controlling for time-varying tech nationalism measures.",
    "Synthetic control inference should use in-space permutation (Abadie et al. 2010, JASA) in addition to the gap statistic.",
    "Within-R² of 0.012 should be contextualized more explicitly as indicating the treatment explains 1.2% of residual within-country variation."
  ],
  "missing_literature": [
    "Chen and Yang (2019, QJE) - VPN circumvention in China: essential for treatment attenuation argument",
    "Hjort and Poulsen (2019, AER) - Internet access and economic outcomes: closest methodological parallel",
    "Rambachan and Roth (2023, ReStud) - Pre-trend sensitivity analysis: mandatory given formal rejection",
    "Abadie, Diamond, Hainmueller (2010, JASA) and Abadie (2021, JEL) - Synthetic control methods and inference",
    "Goldfarb and Tucker (2019, JEL) - Digital economics framework for regulation",
    "Empirical literature on Russian IT-sector emigration 2022-2023"
  ]
}
```