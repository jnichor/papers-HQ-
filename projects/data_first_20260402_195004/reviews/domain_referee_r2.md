## Referee Report

**Journal: [Blind Review]**
**Manuscript:** *Apartheid or Persecution? A Randomized Experiment on the Effect of Legal Labels on Public Support for ICC Accountability*

---

### Summary

This paper reports a survey experiment (N = 784) in which U.S.-based respondents are randomly assigned to read a vignette characterizing Israeli government policies toward Palestinians as either "apartheid" or "persecution" under international law. The primary outcome is a standardized composite index of support for ICC accountability. Across three pre-specified specifications, the authors find a precisely estimated null—point estimates between −0.070 and −0.078 SD, with a tightest 95% CI of [−0.217, 0.061]—and interpret this as an informative null with implications for advocacy strategy. Robustness checks including ordered probit, binary logit, Lee attrition bounds, and permutation inference consistently support the main finding.

---

### Main Assessment

**Strengths.** The research question is genuinely important and underexplored experimentally. The methodological toolkit is appropriate and transparently deployed: randomized assignment, three estimation specifications with coherent motivation (raw difference → OLS controls → double LASSO), permutation inference, and multiple-testing correction for subgroup analyses. The authors correctly frame the null as informative using the Lakens (2017) equivalence-testing logic and are appropriately candid about the absence of pre-registration. The policy-implications section is measured and well-targeted.

**Weaknesses.** The paper has four significant problems that together require major revision: (1) a manipulation check is absent, making it impossible to distinguish a true null from experimental failure; (2) the education variable in the balance table reveals data anomalies beyond the single acknowledged outlier; (3) the Lee bounds finding—both bounds negative and excluding zero—is inconsistently characterized; and (4) the paper does not engage with the highly relevant institutional fact that the ICC had already opened a formal investigation and, depending on when this survey was fielded, issued actual arrest warrants in the Israeli-Palestinian situation, directly affecting vignette realism and respondent priors.

---

### Major Comments

**1. Absence of a manipulation check (critical for null interpretation).**
The paper's central claim is that the legal label does not matter. For this inference to be warranted, the authors must first demonstrate that respondents processed and retained the label manipulation. Without a manipulation check (e.g., "Which term did the legal experts use to characterize these policies?"), the observed null is consistent with two very different accounts: (a) respondents correctly read the label but it did not shift their attitudes, or (b) the manipulation was ineffective—respondents skimmed the vignette, anchored on pre-existing beliefs about the conflict, or failed to distinguish "apartheid" from "persecution." In a politically saturated topic like the Israeli-Palestinian conflict, inattention is a serious threat. The authors are commendably thorough with functional-form robustness but entirely silent on this most fundamental validity check. This must be reported before the null can be interpreted as informative.

**2. Data anomaly in the education variable.**
The balance table (Table 1 / `table1_balance.tex`) reports treatment-group mean education of −11.035 and control-group mean of 4.627. The paper acknowledges one respondent with an implausible value (−3105) that is winsorized to 5. However, winsorizing a single observation to 5 cannot produce a treatment-group mean of −11 when the variable is coded on a conventional integer scale. This strongly implies there are additional corrupted education values in the treatment arm that the paper does not acknowledge. The authors must (a) report the full distribution of education values before and after cleaning, (b) identify all anomalous values and the decision rule applied to each, and (c) verify that the anomalies are not systematically concentrated in one arm (the current balance table suggests possible imbalance on education: SMD = −0.101). The claim that "results are unchanged when this observation is dropped entirely" is insufficient if the underlying variable is more severely corrupted.

**3. The Lee bounds finding requires more careful treatment.**
The paper reports Lee (2009) attrition bounds of [−0.118, −0.053] and describes this result as consistent with the main null. It is not. Under worst-case differential attrition assumptions, both the lower and upper bounds are negative, and the interval excludes zero—implying a systematic negative effect of the apartheid label on ICC support. This is precisely opposite to the paper's null framing. The authors acknowledge this in a parenthetical ("weakly negative") but do not reconcile it with the headline null. Several interpretations are possible—the treatment-group had somewhat higher attrition, making the bounds mechanically negative; the trimmed sample may be qualitatively different—but the paper must be explicit about which interpretation is correct, show the attrition rates by arm, and clarify whether the Lee bounds are regarded as indicating a systematic directional effect or as an artifact of the trimming procedure.

**4. Ecological validity: ICC proceedings were ongoing at survey time.**
The ICC situation regarding Palestine has been active: the Pre-Trial Chamber confirmed Palestinian Authority membership in 2015, a formal investigation was opened in 2021, and—critically—in May 2024 the ICC Prosecutor applied for arrest warrants for both Israeli leadership and Hamas figures, with warrants issued November 2024. Depending on when the survey was fielded (the paper provides no date), respondents likely had substantial real-world information about actual ICC proceedings that is inconsistent with the vignette's hypothetical framing ("International legal experts *have classified* these policies..."). This could contaminate responses in at least two ways: (a) respondents with high topic knowledge may override the vignette with their existing beliefs, further attenuating any label effect; (b) the hypothetical may be perceived as implausible by informed respondents. The paper must report the survey fielding date and engage explicitly with the concurrent institutional context. This also substantially affects the external validity argument in Section 6.

---

### Minor Comments

**1. Index reliability not reported.** The composite ICC accountability index (three items: investigate, arrest warrants, government cooperation) is used as the primary outcome but no reliability statistics are provided (Cronbach's alpha, item-total correlations). A composite index with low internal consistency inflates outcome variance and reduces power; given the null result, readers need assurance that the index is measuring a coherent construct.

**2. Survey platform not identified.** The paper describes recruitment through "an online survey platform" without naming it. Lucid, Prolific, MTurk, and Qualtrics panels have substantially different sample compositions, attention rates, and known response artifacts. This omission makes it difficult to assess the quality of the sample or to compare with related experiments.

**3. The control condition ("persecution") is not neutral.** "Persecution" is itself a legal term of art under the Rome Statute with strong historical connotations (Holocaust, religious violence). The paper correctly notes this in Section 2.3, but the discussion of mechanisms in Section 6.1 relies heavily on the idea that "apartheid" uniquely evokes strong associations. The possibility that "persecution" also triggers strong associations, but of a different character, could explain why the two conditions are indistinguishable—not because labels don't matter, but because both labels are equally activating. A fully neutral control (e.g., "human rights violations" or no legal characterization) would resolve this ambiguity and should be flagged as a limitation.

**4. No survey weights; no population representativeness claim.** The data audit confirms no survey weights exist. The paper is appropriately focused on U.S. respondents but does not describe the sampling frame or benchmark the sample against known population distributions (e.g., ANES or CPS). Given that the policy implications are framed in terms of aggregate U.S. public opinion, some characterization of representativeness is warranted.

**5. Glick (1996) citation.** The reference to Glick & Fiske's ambivalent sexism theory as a framework for understanding in-group identity in the Israeli-Palestinian context is a stretch. Ambivalent sexism concerns gender attitudes specifically and does not transfer straightforwardly to ethnic or national in-group dynamics. This citation should be replaced with a more appropriate reference to social identity theory (Tajfel & Turner 1979, Brewer 1999) or realistic conflict theory.

**6. Hawkishness CATE receives disproportionate attention.** The exploratory finding of −0.310 SD among moderately hawkish respondents (p = 0.031, not surviving correction) is mentioned in the abstract, the introduction, Section 5 (robustness), and Section 6.3 (policy implications). Given that the paper's stated purpose is to report a null result and the authors themselves apply BH correction that eliminates this finding, its repeated prominence risks leaving readers with an impression of a positive finding where none exists. I recommend consolidating discussion of this exploratory finding to one clearly labeled subsection.

**7. Missing literature.** Several important references should be incorporated:
- *Manipulation checks in survey experiments*: Berinsky, Margolis & Sances (2014) on satisficing; Clifford, Jewell & Waggoner (2015) on attention checks; Gaines, Kuklinski & Quirk (2007) on framing vs. persuasion distinction.
- *Online panel data quality*: Coppock & McClellan (2019) on Lucid samples; Heen, Liebman & Moffitt (2014) on MTurk.
- *ICC public legitimacy*: Simmons (2009) *Mobilizing for Human Rights*; Alter (2014) on compliance; Voeten (2008) on public support for international adjudication.
- *Polarization and framing*: Jerit & Barabas (2012) on partisan-motivated reasoning moderating framing effects; Levendusky & Malhotra (2016) on elite cues in polarized environments.
- *Null result standards*: Lakens et al. (2018) on equivalence testing in psychology (updating the 2017 article already cited).
- *Legal label politics*: Falk & Tilley (2017 UN Economic and Social Commission report), and the Human Rights Watch (2021) and Amnesty International (2022) reports on apartheid characterizations, which provide the real-world advocacy context motivating the paper.

---

### Recommendation

**Major Revision**

The paper addresses a genuinely important question with a competent experimental design and honest reporting of a null result. However, the absence of a manipulation check is a critical gap that prevents the null from being interpreted as theoretically informative rather than as experimental failure. The data quality concerns around the education variable require transparent resolution. The Lee bounds interpretation is internally inconsistent with the paper's framing. And the paper cannot credibly discuss ecological validity or policy implications without engaging with the actual ICC proceedings that were ongoing (or had recently concluded) at the time of the survey. These are substantive issues, not cosmetic ones, and require targeted but achievable revisions.

---

```json
{
  "score": 69,
  "decision": "MAJOR_REVISIONS",
  "dimension_scores": {
    "contribution_novelty": 78,
    "literature_positioning": 63,
    "substantive_arguments": 65,
    "external_validity": 62,
    "journal_fit": 75
  },
  "major_comments": [
    "No manipulation check is reported. For a null-result paper, the absence of a comprehension/recall check makes it impossible to distinguish a true null from experimental failure due to inattention or prior attitude anchoring. This must be added before the informative-null framing is credible.",
    "The balance table reports education means of -11.035 (treatment) and 4.627 (control) after the authors claim only one observation (coded -3105) was winsorized. Winsorizing one value to 5 cannot produce a group mean of -11 on a conventional education scale; additional corrupted values must be present. The full cleaning procedure must be documented and the extent of data anomalies transparently reported.",
    "The Lee attrition bounds [-0.118, -0.053] both exclude zero and are both negative. The paper characterizes this as consistent with the null, but under worst-case attrition assumptions these bounds imply a systematically negative treatment effect — the opposite of a null. The paper must reconcile this finding with the main analysis, show arm-specific attrition rates, and clearly state whether the bounds are substantively informative or mechanical artifacts of the trimming procedure.",
    "The paper does not report the survey fielding date or engage with the fact that ICC proceedings in the Israeli-Palestinian situation were active and high-profile during the period when this study was plausibly conducted (2024-2026). The ICC investigation was opened in 2021, arrest warrant applications were filed in May 2024, and warrants were issued November 2024. This institutional context directly affects vignette realism, respondent priors, and the ecological validity argument."
  ],
  "minor_comments": [
    "Composite index reliability (Cronbach's alpha, item-total correlations) is not reported. Given the null result, readers need confidence that low index coherence is not inflating outcome variance.",
    "The survey platform is not named. Lucid, Prolific, and MTurk have materially different sample quality profiles; this omission impedes assessment and replication.",
    "The control condition ('persecution') is itself a legally loaded term with strong historical associations. A neutral control would have helped distinguish between 'both labels are equally activating' and 'neither label moves opinion.' This should be acknowledged as a design limitation.",
    "No survey weights and no sample benchmarking against population distributions, despite policy-implications framing in terms of aggregate U.S. public opinion.",
    "The Glick (1996) ambivalent sexism citation is theoretically inappropriate for the in-group/out-group dynamics of national identity in conflict settings. Replace with Tajfel & Turner (1979) or Brewer (1999).",
    "The hawkishness CATE (p=0.031, not surviving correction) appears in the abstract, introduction, robustness section, and discussion section. This repetition creates a misleading impression of a positive finding for a paper claiming an informative null.",
    "Item-level results for the three components of the ICC accountability index are not reported. Showing that all three items individually yield nulls would strengthen the informative-null interpretation."
  ],
  "missing_literature": [
    "Berinsky, Margolis & Sances (2014) on satisficing and attention in survey experiments — essential for null-result credibility.",
    "Clifford, Jewell & Waggoner (2015) on attention checks and data quality in online panels.",
    "Coppock & McClellan (2019) on the properties of Lucid convenience samples.",
    "Jerit & Barabas (2012) on partisan motivated reasoning as a moderator of framing effects — directly relevant to the polarized topic.",
    "Simmons (2009) Mobilizing for Human Rights — foundational for ICC public legitimacy.",
    "Falk & Tilley (2017 UN report), Human Rights Watch (2021), Amnesty International (2022) — these institutional reports are the real-world policy context motivating the advocacy-strategy discussion.",
    "Lakens et al. (2018, Advances in Methods and Practices in Psychological Science) — updated equivalence testing guidance beyond the 2017 piece already cited.",
    "Levendusky & Malhotra (2016) on elite cues reducing persuasion in polarized environments."
  ]
}
```