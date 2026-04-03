## Referee Report

**Journal Submission Review**
**Manuscript:** "Apartheid or Persecution? A Randomized Experiment on the Effect of Legal Labels on Public Support for ICC Accountability"

---

### Summary

This paper reports a pre-registered survey experiment (N=784 recruited, N=760 analyzed) in which U.S. respondents read a vignette about Israeli government policies characterized as either "apartheid" or "persecution" under international law, with support for ICC accountability as the primary outcome. Across three pre-registered specifications, the authors find a precisely estimated null effect (point estimates ranging from −0.070 to −0.078 SD, all p > 0.27), with confidence intervals ruling out effects larger than roughly 0.22 SD. The paper is framed as an informative null with direct implications for advocacy organizations.

---

### Main Assessment

**Strengths.** The research design is clean and the identification strategy is credible. The pre-registration, multiple robustness checks, double LASSO specification, permutation inference, and multiple-testing corrections all represent best-practice experimental methods. The framing of a null as informative, following Lakens (2017), is appropriate and honest. The paper is well-written and the analysis is internally consistent across most specifications.

**Weaknesses.** There are three issues of varying severity that require attention before publication: (1) a verifiable error in Table 3's footnote regarding the Lee bounds; (2) an unexplained discrepancy between the recruited sample (N=784) and the analytic sample (N=760); (3) insufficient engagement with the highly specific and legally evolving context in which this experiment was conducted, which bears on both the institutional framing and external validity.

---

### Major Comments

**1. Lee bounds do not include zero — Table 3 footnote is incorrect.**
The evidence packet shows Lee bounds of [−0.118, −0.053]. Both endpoints are strictly negative; zero is not in this interval. Table 3's footnote states "All bounds include zero, confirming the null," which is factually wrong given the authors' own reported numbers. The robustness section text partially contradicts this footnote by correctly stating "both bounds are negative," but then characterizes the result as "consistent with the confidence intervals from the parametric models that include zero," which is misleading: the Lee bounds and the OLS confidence intervals are not directly comparable objects, and the fact that the Lee bounds *exclude* zero is non-trivial. Under any monotone selection model, the Lee bounds suggest a consistently negative ATE in the range of 5–12% of a SD. This deserves honest discussion rather than rhetorical assimilation to a "null." The authors should either (a) reinterpret the Lee bounds correctly, or (b) provide a formal argument for why the attrition pattern makes these particular Lee bounds uninformative.

**2. Analytic sample discrepancy (N=784 vs. N=760) is unacknowledged.**
The abstract, introduction, and design sections repeatedly state N=784. All regression tables (from the evidence packet) use N=760 or 759. This 24–25 observation discrepancy is almost certainly due to item non-response on the primary outcome, but it is never explained. This matters because: (a) the balance checks should be assessed on the analytic sample; (b) if attrition is differential on observables, the balance claim requires qualification; and (c) Lee bounds are specifically motivated by this kind of attrition, yet the paper is silent on its source and extent. A brief attrition analysis—rates by condition, predictors of attrition—is needed.

**3. Missing engagement with the 2024–2025 legal developments that define the paper's context.**
The experiment was conducted against the backdrop of the most legally active period in ICC history concerning this conflict. The ICC Prosecutor's application for arrest warrants against Israeli and Hamas leaders (May 2024), the ICJ's July 2024 advisory opinion on the legal consequences of Israeli occupation (which used "apartheid" language in some dissents and submissions), and the major civil society reports by Amnesty International (December 2024) and Human Rights Watch (2021) classifying Israeli policies as apartheid all substantially raised the salience and connotational content of the "apartheid" label relative to prior periods. The paper does not tell us *when* the survey was fielded, which is critical. If fielded in late 2024 or 2025, respondents may already have high exposure to the "apartheid" label, which would explain the null under the "prior attitude crystallization" mechanism the authors themselves invoke—but the paper should make this causal claim explicitly, with dates. If fielded before these developments, the external validity claim is limited to a pre-saturation environment. Either way, the absence of any discussion of this legal-political timeline is a significant gap for a paper making institutional and policy claims.

**4. Suspicious education variable coding.**
The balance table reports mean education values of −11.035 (treatment) and 4.627 (control). Negative means for an education variable are anomalous regardless of coding convention and suggest either a recoding error, a mean-centering applied to only one arm, or a variable that is not what it appears to be. The large raw difference (−15.66) with a t-statistic of only −1.42 (p=0.158) and SMD of −0.101 suggests high within-group variance that absorbs the large raw difference—but the coding needs explicit explanation. If this variable is mean-centered at the population level but not within the experimental arms, the SMD calculation may be unreliable.

---

### Minor Comments

**1. The abstract's CI characterization is asymmetric.** The double LASSO CI is [−0.217, 0.061], which rules out effects larger than 0.217 in the negative direction but only 0.061 in the positive direction. Saying the interval "rules out effects larger than 0.22 SD in magnitude" overstates precision on the positive side.

**2. The over_65 imbalance deserves mention.** Table 1 shows a statistically significant imbalance on the over_65 indicator (p=0.037). The paper's claim that no covariate differs significantly at the 5% level "after adjusting for multiple comparisons" is likely correct across 126 variables, but given that age may correlate with both familiarity with the apartheid/persecution terminology and with ICC attitudes, this specific imbalance should be briefly acknowledged and addressed via the OLS-with-controls specification.

**3. Survey platform not identified.** The paper refers to "an online survey platform" without naming it. Standard practice is to identify whether this is Lucid, Prolific, MTurk, or a similar platform, since known platform biases (e.g., the Democratic lean of Lucid, attentiveness on Prolific) bear on external validity and are now routinely discussed in this literature (see Coppock & McClellan 2019; Mullinix et al. 2015).

**4. No discussion of demand characteristics.** Given the extreme political salience of the topic and the relatively transparent experimental manipulation (respondents see a vignette directly naming an international law label), demand effects—particularly social desirability responding among politically engaged respondents—are worth at least a brief methodological discussion. The authors could note whether comprehension checks or attention filters were applied.

**5. The "first clean experimental test" claim.** The contribution claim that this is "the first clean experimental test" of legal labels on ICC attitudes is plausible but should be qualified. The broader literature on international law and public opinion (Brutger & Kertzer 2018; Chapman & Reiter 2004; Hillebrecht 2016) includes experiments on related questions. The authors should confirm this claim is limited to the specific ICC-label question.

---

### Missing Literature

- **Dugard & Reynolds (2013)** — "Apartheid, International Law, and the Occupied Palestinian Territory," *European Journal of International Law* — the foundational legal-academic treatment of the apartheid designation, directly relevant to the institutional framing.
- **Sikkink (2011)** — *The Justice Cascade* — the canonical work on accountability norms and their diffusion; provides the theoretical backdrop for why labels may (or may not) mobilize publics.
- **Murdie & Davis (2012)** — "Shaming and Blaming," *International Studies Quarterly* — experimental and observational evidence on naming effects in human rights.
- **Coppock & McClellan (2019)** — "Validating the Demographic, Political, Psychological, and Experimental Results Obtained from a New Source of Online Survey Respondents," *Research & Politics* — essential reference for characterizing online panel samples.
- **Brutger & Kertzer (2018)** — "A Dispositional Theory of Reputation Costs," *APSR* — best-practice experimental design on U.S. public opinion toward international institutions.
- **Slothuus & de Vreese (2010)** — "Political Parties, Motivated Reasoning, and Issue Framing Effects," *JOP* — important on how partisanship moderates framing effects; directly relevant to the null on pro-Israel heterogeneity.
- **Mullinix et al. (2015)** — "The Generalizability of Survey Experiments," *Journal of Experimental Political Science* — benchmarks for external validity of online experiments.

---

### Recommendation

**Major Revision.** The core experimental design is sound and the contribution is real. However, the Lee bounds error (Major Comment 1) requires correction and honest reinterpretation, the sample discrepancy (Major Comment 2) requires an attrition analysis, the legal-political context (Major Comment 3) requires temporal anchoring, and the education coding anomaly (Major Comment 4) requires explanation. None of these require new data collection; all can be addressed through revised analysis and writing.

---

```json
{
  "score": 68,
  "decision": "MAJOR_REVISIONS",
  "dimension_scores": {
    "contribution_novelty": 80,
    "literature_positioning": 65,
    "substantive_arguments": 62,
    "external_validity": 66,
    "journal_fit": 74
  },
  "major_comments": [
    "Lee bounds [-0.118, -0.053] exclude zero; Table 3 footnote claiming 'all bounds include zero' is factually incorrect. Both endpoints are negative. Under any monotone selection model this represents consistent evidence of a small negative effect, not a null. The discussion must be revised to either explain why this attrition pattern renders the Lee bounds uninformative or honestly acknowledge what the bounds imply.",
    "The recruited sample (N=784) and analytic sample (N=760/759) differ by 24-25 observations with no explanation. An attrition analysis by condition, rates of item non-response on the outcome, and predictors of attrition are required. Balance checks should be verified on the analytic sample.",
    "The paper does not report when the survey was fielded, which is critical given that the ICC Prosecutor issued arrest warrant applications in May 2024, the ICJ issued a landmark advisory opinion in July 2024, and major NGO reports had already saturated U.S. media with 'apartheid' framing. The timing determines whether the null reflects label equivalence or terminological saturation, and directly bears on external validity.",
    "The education variable shows means of -11.035 (treatment) and 4.627 (control) — negative means for an education variable are anomalous and suggest a possible coding error or mis-specified centering. This must be explained, and if a coding error exists, all results should be re-checked."
  ],
  "minor_comments": [
    "Abstract states CI 'rules out effects larger than 0.22 SD in magnitude' but the double LASSO CI is [-0.217, 0.061], which is asymmetric: the positive bound is only 0.061, not 0.22. The precision claim should be stated asymmetrically.",
    "The over_65 indicator shows a marginally significant imbalance (p=0.037) before multiple-testing correction. While this likely survives BH correction across 126 variables, it should be explicitly acknowledged given the plausible age-outcome correlation.",
    "The survey platform is not named. Identifying it as Lucid, Prolific, MTurk, or similar is now standard practice and necessary for assessing sample properties.",
    "No mention of comprehension checks, attention filters, or demand-effect mitigation strategies for what is an extremely politically salient manipulation in a transparent survey design.",
    "The 'first clean experimental test' claim should be explicitly scoped and defended against the broader experimental literature on ICC attitudes and international institution support."
  ],
  "missing_literature": [
    "Dugard & Reynolds (2013) 'Apartheid, International Law, and the Occupied Palestinian Territory,' EJIL — foundational legal source on the apartheid designation the paper discusses",
    "Sikkink (2011) The Justice Cascade — canonical work on accountability norm diffusion and public mobilization",
    "Murdie & Davis (2012) 'Shaming and Blaming,' ISQ — experimental evidence on naming effects in human rights contexts",
    "Brutger & Kertzer (2018) 'A Dispositional Theory of Reputation Costs,' APSR — best-practice experimental design on U.S. public opinion toward international institutions",
    "Slothuus & de Vreese (2010) 'Political Parties, Motivated Reasoning, and Issue Framing Effects,' JOP — directly relevant to why partisanship may null out framing effects",
    "Coppock & McClellan (2019) 'Validating... a New Source of Online Survey Respondents,' Research & Politics — essential for characterizing the online panel",
    "Mullinix et al. (2015) 'The Generalizability of Survey Experiments,' JEPS — benchmarks for external validity claims"
  ]
}
```