## Referee Report

**Journal:** Economics of Technology / Industrial and Corporate Change

---

### Summary

This paper investigates whether ChatGPT's release in November 2022 altered programming language ecosystem concentration across countries, using a panel of 177 countries, 23 quarters, and HHI/Shannon entropy measures derived from GitHub push activity. The authors find a statistically significant post-ChatGPT diversification in the baseline specification but demonstrate, creditably, that this result is not robust to placebo tests, country-specific trends, or composition adjustments. The core conclusion is that programming language diversification predates ChatGPT and the evidence for a causal discontinuity is weak.

---

### Main Assessment

**Strengths.** The paper's primary virtue is intellectual honesty: the authors construct a thorough robustness battery and reach a null conclusion that is itself informative. The decomposition of mechanical composition effects from behavioral effects (Section 4.4) is methodologically sound and represents the paper's clearest contribution. The identification threat inventory in Section 3.3 is unusually candid for an empirical paper.

**Weaknesses.** The fundamental identification problem—simultaneous universal treatment with no control group—renders causal claims inherently fragile, and the paper does not sufficiently explore what the event study is actually identifying absent a clean counterfactual. The results section contains a material sign inconsistency between the described event study coefficients and the reported ATT. The entropy result, which survives the balanced panel but not the country-trends specification, is insufficiently reconciled with the null conclusion. The literature positioning misses several directly relevant bodies of work.

---

### Major Comments

**1. The event study coefficients and ATT have irreconcilable signs as described.**

Section 4.1 states that all post-treatment HHI coefficients are "positive and significant, ranging from +0.039 to +0.079," yet Section 4.2 reports an ATT of −0.027, which represents a *decline* in HHI (diversification). These statements are only consistent if the post-treatment coefficients are, on average, smaller than the pre-treatment coefficients—meaning the "treatment effect" is identified from a change in the level of the (positive) deviation from the reference period, not from a change in sign. The paper never makes this explicit. A reader following the narrative will conclude the authors made a sign error. The description of the event study results must be rewritten to clarify that the ATT captures the *difference in trajectory* between pre- and post-treatment event-time coefficients, not the direction of the post-treatment coefficients themselves. A table of event-time coefficients would help.

**2. The entropy result is inconsistent with the claimed null finding and receives insufficient attention.**

The balanced-panel entropy ATT is +0.213 (SE = 0.019, p < 0.001), a robust and large result. This is dismissed because it is eliminated by country-specific trends. However, the paper applies the same country-trends argument to HHI (ATT eliminated) to reach a null conclusion, yet the entropy result disappears only when country-trends are added—and the authors acknowledge entropy may be capturing genuine behavioral shifts not fully accounted for by composition. The paper cannot simultaneously claim (a) the null result is robust because trends eliminate it, and (b) the entropy finding is also null because trends eliminate it, without addressing whether country-specific trends are themselves absorbing a real ChatGPT effect that differentially affected entropy. The paper needs a cleaner reconciliation of the HHI null with the persistent entropy signal in the balanced panel, including a discussion of whether the normalized HHI and Shannon entropy should be expected to respond symmetrically to composition changes.

**3. The simultaneous universal treatment design renders the entire event study non-identifying without additional structure, and this limitation is understated.**

The paper correctly notes in Section 3.1 that event-time dummies are collinear with quarter effects, and that "we cannot separate the ChatGPT effect from any other global shock occurring at the same time." This is not a minor caveat—it is a fatal identification problem for causal inference. The post-treatment period (Q1 2023–Q3 2025) includes GPT-4 (March 2023), Google Bard/Gemini (March 2023), GitHub Copilot's paid expansion, Meta Llama releases (February 2023, July 2023), and the general proliferation of code-assistant tools. The paper treats these as confounds to ChatGPT, but they are confounds to each other as well. The paper should reframe its contribution more modestly: it cannot isolate ChatGPT specifically, and the more appropriate framing is the effect of the *AI coding assistance era* beginning Q1 2023—with the null conclusion that even this framing yields no robust ecosystem-level effect. The current framing as a "ChatGPT event study" overstates what the design can deliver.

**4. The pre-treatment window is entirely within the COVID-19 pandemic and this threatens the validity of the secular trend interpretation.**

The authors note COVID-19 as an identification threat (Section 3.3, item 3) but do not pursue it. The entire pre-treatment period (Q1 2020–Q4 2022) was characterized by extraordinary shocks to digital work: a global shift to remote work, a surge in developer hiring, GitHub's own platform expansion, and the pandemic-era acceleration of open-source contributions. The "secular diversification trend" identified in the robustness section could reflect post-COVID normalization rather than a stable pre-existing trend that one can extrapolate through late 2022 to benchmark against. The placebo tests at Q1 2021 and Q1 2022 identify effects of comparable magnitude to the main result, but these placebo dates also fall within the pandemic period, which may itself be the source of the trend rather than evidence of a long-run pre-ChatGPT dynamic. The paper should either (a) show the trend extends before Q1 2020, or (b) explicitly acknowledge that the "secular trend" interpretation is contaminated by pandemic-era dynamics.

**5. The English proficiency heterogeneity analysis excludes the highest-proficiency, highest-activity countries.**

The EF EPI covers 123 countries but explicitly excludes native English-speaking nations (US, GB, AU, CA, NZ, IE). The paper acknowledges this (Section 2.2) but does not discuss the implications: these excluded countries are among the most GitHub-active and would, by definition, be in the highest-proficiency group. Their exclusion from the heterogeneity analysis creates a selected sample in which the "high EPI" group does not actually include the countries most likely to respond to an English-first interface. The null heterogeneity result may simply reflect that the analysis cannot be run in the subsample where the effect would be largest. The paper should either (a) assign excluded native-English countries to the top EPI group and rerun the analysis, or (b) more clearly discuss that the heterogeneity test is substantially underpowered for the stated mechanism.

---

### Minor Comments

1. **Section 2.1, language shares construction**: The paper computes shares as $s_{l,c,q} = \text{pushers}_{l,c,q} / \sum_l \text{pushers}_{l,c,q}$, summing across pushers within a country-quarter. A single developer who pushes in five languages would be counted five times in the denominator. This is correct for computing language shares among *push events*, but means the "shares" do not correspond to an individual developer's portfolio. The interpretation should clarify whether HHI captures concentration of *developer-time* or *commit activity*.

2. **Table 1 sign note**: The summary statistics in the paper report normalized HHI mean as 0.075, consistent with the evidence packet (0.0747). However, the evidence packet also reports raw HHI mean of 0.1513 while the paper's Table 1 only presents normalized HHI. A brief note on whether the normalized measure behaves well when N is small (as it can for developing-country cells with few languages) would strengthen transparency.

3. **Figure 2 description is internally inconsistent**: The caption references "fig2_event_study.png" but the figure in the Appendix section references "fig1_raw_trends.png." The numbering between inline and appendix figures should be checked.

4. **100 million users in two months** (Introduction): This claim requires a citation. Commonly cited sources are Similarweb/UBS estimates published in February 2023.

5. **Data horizon**: The dataset runs through Q3 2025 but the paper does not discuss whether the longer post-treatment window (10+ quarters post-treatment) offers additional analytical leverage. An extended event study window is potentially informative about persistence.

6. **"Min 3 languages" robustness** (Table 2): The Min-3 specification shows ATT = +0.007 (p = 0.000) for HHI, which is positive and significant—opposite sign to the baseline. This is never discussed in the text. It is notable that restricting to multi-language cells reverses the HHI sign and should be explained.

7. **Winsorization**: The winsorized specification is identical to baseline (ATT = −0.027). What threshold was used? The large standard deviation of pushers (SD = 470,615 against a mean of 146,254) suggests heavy right-skewing; the lack of sensitivity to winsorization should be briefly noted.

---

### Missing Literature

- **GitHub Octoverse annual reports** (GitHub, 2020–2025): GitHub's own analysis of language trends is directly relevant institutional evidence and should be cited or noted as a complementary source.
- **Ray et al. (2014), "A Large Scale Study of Programming Languages and Code Quality in GitHub"** (*FSE 2014*): Foundational empirical work on language distributions in GitHub ecosystems.
- **Vasilescu et al. (2015), work on GitHub activity and community structure**: Context for interpreting "pushers" as a measure of developer activity.
- **Borges et al. (2016) on trending GitHub repositories**: Relevant to understanding GitHub activity dynamics.
- **TIOBE Index / RedMonk rankings**: These alternative language popularity measures provide corroboration or contrast for the GitHub-based findings and are widely used in practitioner and academic contexts.
- **Stack Overflow Developer Survey**: Annual data on self-reported language use that would complement or benchmark the GitHub-based concentration measures.
- **Rogers (1962/2003), Diffusion of Innovations**: The conclusion's discussion of Rust/TypeScript/Kotlin maturation as an alternative explanation maps directly onto technology diffusion theory, which should be cited.
- **Barke et al. (2023), "Grounded Copilot: How Programmers Interact with Code-Generating Models"** (*OOPSLA 2023*): Micro-level evidence on which languages developers use AI assistance for, directly relevant to the stated mechanism.
- **GitHub Copilot internal studies (Kalliamvakou 2022; Dohmke 2023)**: Industry evidence on Copilot's effect on developer productivity and language use patterns.

---

### Recommendation: **Major Revision**

The paper addresses an important and timely question with an honest and methodologically careful approach. The null finding, combined with the composition-effects decomposition, is a genuine contribution to the literature on AI and software ecosystems. However, four issues require substantive revision before publication: the sign inconsistency in the results presentation, the unresolved tension between the HHI null and the entropy result in the balanced panel, the insufficient engagement with the COVID-era pre-period as an alternative trend explanation, and the underpowered nature of the English-proficiency heterogeneity test given excluded native-speaking countries. The paper should also reframe its central claim to accurately reflect that the design identifies the effect of the AI coding tool era broadly, not ChatGPT specifically.

---

```json
{
  "score": 66,
  "decision": "MAJOR_REVISIONS",
  "dimension_scores": {
    "contribution_novelty": 72,
    "literature_positioning": 62,
    "substantive_arguments": 63,
    "external_validity": 60,
    "journal_fit": 70
  },
  "major_comments": [
    "Sign inconsistency: post-treatment HHI event study coefficients described as positive (+0.039 to +0.079) while ATT is reported as negative (−0.027). The logic that ATT is identified from the difference in trajectory between pre- and post-treatment coefficient magnitudes is never made explicit and will confuse readers. Full table of event-time coefficients required.",
    "The balanced-panel entropy ATT (+0.213, p<0.001) survives but is dismissed along with the HHI null. The paper cannot invoke country-specific trends as the decisive robustness test for both outcomes simultaneously without discussing whether trends absorb a real entropy signal. The asymmetric behavior of HHI and entropy under composition correction deserves a unified explanation.",
    "The simultaneous universal treatment design means event-time dummies identify the AI coding assistance era (Q1 2023 onward), not ChatGPT specifically. GPT-4, Bard, Copilot expansion, and Llama all launched in Q1–Q2 2023. The paper should reframe its contribution accordingly and avoid overclaiming ChatGPT-specific identification.",
    "The pre-treatment window (Q1 2020–Q4 2022) spans the entire COVID-19 pandemic. The placebo tests at Q1 2021 and Q1 2022 yield comparable effect sizes to the main result, but these placebo dates also fall inside the pandemic disruption window. The 'secular trend' interpretation requires evidence that the trend predates Q1 2020, or must acknowledge pandemic dynamics as an alternative explanation for the pre-existing pattern.",
    "The English proficiency heterogeneity analysis excludes the US, UK, Australia, Canada, NZ, and Ireland—the highest-GitHub-activity, highest-English-proficiency countries. The null heterogeneity result may simply reflect that the most relevant variation is excluded from the sample. The authors should assign native-English countries to the top EPI group and rerun, or clearly discuss this as a binding constraint on the heterogeneity test."
  ],
  "minor_comments": [
    "The 'pushers' measure double-counts developers active in multiple languages in the denominator. Clarify whether HHI reflects concentration of push-events or developer time-allocation.",
    "The 'Min 3 languages' robustness shows ATT = +0.007 (positive, significant) for HHI—opposite sign to baseline—but is never discussed in the text. This reversal requires explanation.",
    "The winsorization threshold used is not reported. Given extreme right-skew in total_pushers (mean 146K, SD 471K), the threshold choice matters and should be stated.",
    "The 100-million-users-in-two-months claim in the Introduction needs a citation.",
    "Figure numbering inconsistency between inline figures and appendix references should be corrected.",
    "The dataset ends at Q3 2025, providing 10+ post-treatment quarters. The paper does not exploit the extended window for testing effect persistence or fade-out, which would add analytical value.",
    "The conclusion speculates about Rust, TypeScript, and Kotlin maturation as an alternative explanation but provides no supporting citation or evidence. These claims should either be cited or removed."
  ],
  "missing_literature": [
    "GitHub Octoverse annual reports (2020–2025): directly relevant institutional documentation of language ecosystem trends on the platform used for the study's data.",
    "Ray et al. (2014), 'A Large Scale Study of Programming Languages and Code Quality in GitHub' (FSE 2014): foundational empirical work on language distributions in GitHub.",
    "TIOBE Index and RedMonk quarterly rankings: widely used alternative language popularity measures that could corroborate or contrast the HHI-based findings.",
    "Stack Overflow Developer Survey (annual): self-reported language use data that provides a complementary measure to push-based activity.",
    "Barke et al. (2023), 'Grounded Copilot: How Programmers Interact with Code-Generating Models' (OOPSLA 2023): micro-level evidence on AI-assisted language use patterns relevant to the stated mechanism.",
    "Rogers (2003), Diffusion of Innovations: foundational theory for the conclusion's alternative explanation of Rust/TypeScript/Kotlin maturation.",
    "Dohmke (2023) / Kalliamvakou (2022): GitHub internal evidence on Copilot adoption and language-use effects."
  ]
}
```