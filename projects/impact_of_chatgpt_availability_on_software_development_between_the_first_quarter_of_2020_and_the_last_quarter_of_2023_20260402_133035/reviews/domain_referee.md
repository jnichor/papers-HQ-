## Referee Report

### Summary

This paper examines whether ChatGPT's November 2022 release altered the concentration of programming language ecosystems using a country-level panel of GitHub push activity for 177 countries over 23 quarters (Q1 2020–Q3 2025). The authors construct Herfindahl-Hirschman and Shannon entropy measures and implement an event study design. Their headline finding is a cautionary null: while raw post-ChatGPT estimates suggest diversification, these results vanish under country-specific linear time trends, are replicated by placebo tests at pre-ChatGPT dates, and are largely explained by mechanical composition effects (language entry into country-quarter cells).

---

### Main Assessment

**Strengths.** The paper is unusually transparent about a null result and the fundamental identification barrier of simultaneous universal treatment. The robustness battery—placebo timing, country-specific trends, balanced panel, composition-adjusted HHI—is comprehensive and clearly reported. The composition effects analysis (Section 4.4) is genuinely novel and important: documenting that language entry mechanically drives most of the HHI decline, then quantifying the residual effect at −0.002 after controlling for it, is the paper's most credible contribution. The methodological caution regarding simultaneous-treatment designs is a useful service to the applied literature.

**Weaknesses.** A notable sign inconsistency in Section 4.1 creates confusion about the direction of results. The entire pre-treatment window coincides with COVID-19, which is underaddressed as a confound. The paper does not exploit the quasi-experimental variation offered by differential country-level access restrictions on ChatGPT. The heterogeneity analysis is undertheorized. Key industry and academic references on programming language ecosystem dynamics are absent.

---

### Major Comments

**1. Internal inconsistency in event study sign description (Section 4.1).**
The paper reports that post-treatment HHI coefficients are "positive and significant, ranging from +0.039 to +0.079" and that pre-treatment coefficients are also positive (+0.071 to +0.121). Taken at face value, all event-time dummies being positive implies HHI in every period—pre *and* post—is *above* the reference period Q3 2022 (t=−1). This means HHI at the reference period is a local *minimum*, and post-ChatGPT HHI is *higher* than at t=−1, which is concentration, not diversification. Yet the baseline ATT is −0.027 and the paper's narrative throughout is diversification. The authors must reconcile this. The most likely resolution is that the ATT is computed as the average post-treatment coefficient minus the average pre-treatment coefficient (capturing the change in trend, not the level relative to the reference period), but this interpretation is non-standard and should be stated explicitly. The current text is misleading and will confuse readers.

**2. COVID-19 pre-period confound is underaddressed.**
The entire pre-treatment window (Q1 2020–Q3 2022) coincides with the COVID-19 pandemic. The pandemic caused well-documented, dramatic shifts in GitHub activity, remote work, and open-source contribution patterns. The "diversification trend" the paper attributes to secular forces may be partly or largely COVID-driven and may not extrapolate to the post-pandemic counterfactual. The authors acknowledge this in passing (Section 3.3, Identification Threat 3) but offer no robustness check addressing it. At minimum, the authors should present specifications restricting the pre-period to Q3 2021 or Q1 2022 onward—after acute pandemic disruption subsided—to assess whether the claimed secular trend holds in a more stable pre-period. Without this, the country-specific trend robustness check is absorbing both the secular trend *and* COVID dynamics, making it difficult to interpret.

**3. Unexploited quasi-experimental variation from differential access restrictions.**
The paper treats ChatGPT's rollout as simultaneous across all countries, but this is not entirely accurate. Italy temporarily banned ChatGPT in March–April 2023. China effectively blocked it throughout the post-period. Several Gulf states and smaller markets had delayed or restricted access. This differential access provides genuine quasi-experimental variation that could be used to identify a ChatGPT-specific effect separate from the global time trend. The paper should either (a) demonstrate why this variation is insufficient (sample size, measurement difficulties), or (b) present a specification using countries with documented early restrictions as a comparison group. Failing to engage with this variation is a missed opportunity, especially given the paper's own complaint about lacking a control group.

**4. Missing literature on programming language ecosystem dynamics.**
The paper claims to provide "the first ecosystem-level analysis of programming language concentration dynamics," but does not engage with the substantial evidence base on language adoption trends. GitHub's annual *Octoverse* reports, Stack Overflow's *Developer Surveys* (published annually since 2011), the *TIOBE Index*, and *RedMonk* rankings all document multi-year trends in language popularity that directly bear on this paper's findings. The diversification trend the authors observe may already be well-characterized in these sources, which would either validate or complicate the paper's "secular trend" interpretation. The authors should also engage with the academic literature on technology diffusion and platform ecosystem dynamics (e.g., Parker & Van Alstyne on platform competition; work on programming language network effects), and more specifically with studies on AI coding assistant usage at the individual level (Ziegler et al. 2022 on GitHub Copilot; Vaithilingam et al. 2022).

**5. Heterogeneity analysis is undertheorized.**
The English proficiency channel is motivated by ChatGPT's "initially English-first interface," but this rationale is weak for code generation: code syntax is language-agnostic and ChatGPT's code generation performance does not depend substantially on the user's natural language proficiency. The null result on English proficiency is unsurprising. More economically meaningful moderators would include: (a) the pre-treatment share of activity in languages with strong LLM support (Python, JavaScript), (b) developer community size (total pushers), (c) internet infrastructure quality, or (d) the share of developers in tech-exporting industries. The current heterogeneity analysis should either be more theoretically motivated or replaced with more informative moderators.

---

### Minor Comments

1. **Composition effect magnitude unclear.** Section 4.4 states the number of observed languages per country-quarter increases by "+48 languages on average, $p < 0.001$." Given Table 1 reports a mean of 45.1 languages, this implies a near-doubling. This figure seems implausibly large relative to the pre-to-post change in Table 1 (+7.4 languages on average: 41.4 → 48.8). The authors should clarify whether "+48" refers to the coefficient in a regression, a different unit, or whether there is a transcription error.

2. **Subsequent AI releases in the post-period.** The post-treatment window (Q1 2023–Q3 2025) encompasses GPT-4 (March 2023), Google Bard/Gemini (March 2023), Llama 2 open-source release (July 2023), and multiple subsequent major LLM events. The paper conflates all post-Q4 2022 effects under the "ChatGPT treatment." To the extent the paper is about *generative AI broadly* rather than *ChatGPT specifically*, the framing should be updated. If the goal is ChatGPT-specific identification, the authors must grapple with contamination from these subsequent releases.

3. **Raw HHI omitted from Table 1.** The evidence packet confirms raw HHI values (0.1513 full, 0.1588 pre, 0.1440 post) that do not appear in the paper. Reporting both raw and normalized HHI in Table 1 would improve transparency and allow readers to assess the normalization's impact.

4. **Pusher measure conflates extensive and intensive margins.** Language shares are based on unique pushers, so a developer with one Python commit and one Rust commit is treated identically to one with 1,000 Python commits and one Rust commit. This conflation may cause HHI to mechanically appear more diverse than commit-weighted shares would suggest. The authors should discuss whether commit-weighted shares yield different concentration patterns.

5. **Partial treatment of Q4 2022.** The decision to exclude Q4 2022 as a "partial treatment" quarter is reasonable, but robustness to including it (with a fractional indicator of 1/3, as mentioned in the strategy memo) should be reported. This is noted as planned but does not appear in Table 2.

6. **JEL classification.** L15 (Information and Product Quality; Standardization and Compatibility) and O31 (Innovation and Invention) are more precise additions alongside the listed O33, J24, L86.

---

### Recommendation: **Major Revision**

The paper makes a useful empirical contribution through its honest null result and thorough robustness analysis, particularly the composition effects decomposition. However, the sign inconsistency in Section 4.1 must be resolved, the COVID confound requires a dedicated robustness check, the differential access restriction variation should be addressed, and the literature positioning requires substantial improvement. These are not insurmountable revisions, and the paper's core honesty about its identification limitations makes it worth developing further.

---

```json
{
  "score": 66,
  "decision": "MAJOR_REVISIONS",
  "dimension_scores": {
    "contribution_novelty": 72,
    "literature_positioning": 58,
    "substantive_arguments": 65,
    "external_validity": 63,
    "journal_fit": 70
  },
  "major_comments": [
    "Internal sign inconsistency in Section 4.1: post-treatment HHI event-study coefficients reported as positive (+0.039 to +0.079) imply HHI is above the reference period Q3 2022, yet the paper claims diversification (HHI declining). The ATT of -0.027 can only be reconciled if it is computed as the average post-treatment coefficient minus the average pre-treatment coefficient rather than the level relative to the reference period. This non-standard interpretation must be made explicit and the current description substantially revised.",
    "The entire pre-treatment window (Q1 2020 to Q3 2022) coincides with COVID-19, which drove documented shifts in GitHub activity and digital work patterns. The secular diversification trend may be COVID-driven and may not be a valid counterfactual for post-2022 dynamics. A dedicated robustness check restricting the pre-period to Q3 2021 or Q1 2022 onward is required.",
    "Differential country-level ChatGPT access restrictions (Italy's March-April 2023 ban, China's effective block, others) provide quasi-experimental variation that the paper ignores. The authors should either exploit this variation to identify a ChatGPT-specific effect or explicitly explain why it is insufficient.",
    "The paper claims to be the first ecosystem-level analysis of programming language concentration dynamics while ignoring GitHub Octoverse reports, Stack Overflow Developer Surveys, TIOBE Index, and RedMonk rankings — all of which track language adoption trends and directly bear on the paper's positioning and the magnitude of its findings.",
    "The English proficiency heterogeneity analysis is undertheorized: code generation performance is largely natural-language-agnostic, so the null result on EF EPI is unsurprising. More economically grounded moderators (pre-treatment share in Python/JS, developer community size, internet infrastructure quality) should replace or supplement the English proficiency analysis."
  ],
  "minor_comments": [
    "The claim that languages per country-quarter increased by '+48 on average' is inconsistent with Table 1's pre-to-post change of +7.4. Clarify whether this is a regression coefficient, a different unit of measurement, or a transcription error.",
    "The post-treatment window (Q1 2023 to Q3 2025) includes GPT-4, Llama 2, Google Bard/Gemini, and multiple other major AI releases. The paper should either reframe the treatment as 'generative AI broadly' or grapple with contamination from these subsequent events.",
    "Raw HHI (0.1513 full sample per the evidence packet) is absent from Table 1. Both raw and normalized HHI should be reported for transparency.",
    "Language shares based on unique pushers conflate extensive and intensive margins. Commit-weighted shares should be tested as a robustness check, with discussion of whether they yield materially different concentration patterns.",
    "The Q4 2022 fractional indicator robustness check mentioned in the strategy memo does not appear in the paper. It should be included in Table 2.",
    "JEL codes L15 and O31 are more precise for this topic alongside the current O33, J24, L86."
  ],
  "missing_literature": [
    "GitHub Octoverse annual reports on programming language trends (essential baseline for ecosystem concentration claims)",
    "Stack Overflow Developer Survey annual editions (primary source for developer language preferences over time)",
    "TIOBE Index and RedMonk rankings literature (industry benchmark for language popularity trends)",
    "Ziegler et al. (2022) on GitHub Copilot's measured impact on developer productivity and language use",
    "Vaithilingam et al. (2022) on programmer interactions with GitHub Copilot",
    "Cassano et al. (2022) MultiPL-E — benchmarks on LLM code generation performance by language, directly relevant to the heterogeneous-effects mechanism",
    "Work on technology diffusion and platform ecosystems (Parker & Van Alstyne; Evans & Schmalensee) for theoretical grounding on concentration dynamics",
    "Li et al. (2023) or equivalent on measuring ChatGPT's impact on programming language search/adoption at the developer level"
  ]
}
```