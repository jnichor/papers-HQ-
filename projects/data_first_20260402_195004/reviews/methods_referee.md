## Referee Report

**Manuscript:** "Apartheid or Persecution? A Randomized Experiment on the Effect of Legal Labels on Public Support for ICC Accountability"

---

### Summary of Methodology

This paper uses a two-arm randomized vignette experiment (N=784 U.S. respondents) to estimate the ATE of labeling Israeli policies as "apartheid" versus "persecution" on a composite ICC accountability support index. The identification strategy is experimental randomization; the authors report three pre-registered specifications (raw difference-in-means, OLS with controls, and double LASSO) alongside ordered probit, logit, Lee attrition bounds, and permutation inference as robustness checks. The headline result is a precisely estimated null (ATE ≈ −0.07 SD, 95% CI ruling out effects beyond ≈ 0.22 SD).

---

### Main Methodological Assessment

The experimental design is sound in principle, and the analysis is methodologically sophisticated for a survey experiment. However, several verifiable errors and significant omissions prevent me from recommending acceptance without major revision. Most critically, the Lee attrition bounds are misrepresented in a way that contradicts the paper's central null-result claim. Additionally, the absence of a manipulation check, an unexplained discrepancy between the advertised and actual sample sizes, and an implausible education variable mean raise serious concerns about the reliability of the evidence packet.

---

### Major Concerns

**1. Lee Bounds Are Misrepresented (Verifiable Error)**

The evidence packet reports Lee bounds of [−0.118, −0.053]. Both endpoints are negative and exclude zero. The paper nonetheless states that "the interval is consistent with the confidence intervals from the parametric models that include zero." This is incorrect as stated. Lee bounds are worst-case *point* bounds on the ATE, not a confidence interval. If the true ATE lies within [−0.118, −0.053] under worst-case differential attrition, that is evidence of a negative effect, not a null.

*The likely explanation* is that the authors mean the *confidence intervals around the Lee bounds* include zero — but these are never reported. The authors must: (a) compute and report 95% CIs around each Lee bound endpoint (e.g., via the delta method or bootstrap), and (b) explicitly clarify whether it is the point bounds or confidence intervals that include zero. Failing this, the robustness section is potentially misleading about whether attrition threatens the null interpretation.

**2. Unexplained N Discrepancy**

The abstract, introduction, and sample description consistently state N=784 (398 treated, 386 control). All regression tables in the evidence packet show N=760 (and N=759 for specifications with baseline controls). This is a discrepancy of 24–25 observations — roughly 3% of the sample. The paper does not explain where these observations went. The Lee bounds section also uses N=760. Authors must explicitly state: (a) the source of these 24 missing outcome observations, (b) whether they are missing at random, and (c) whether there is differential attrition by treatment arm that motivates the Lee bounds exercise.

**3. No Manipulation Check**

The treatment is a single substitution of one legal term for another in a vignette. For framing experiments of this type, a manipulation check — asking respondents which label appeared in their vignette, or whether they noticed a characterization by international legal experts — is essential. Without it, the null result is observationally equivalent to two scenarios: (a) respondents processed the label but it did not move attitudes, and (b) respondents did not process the label at all (inattention/skimming). These have very different substantive implications for the policy conclusions. The absence of a manipulation check prevents distinguishing between a true null framing effect and a design failure.

**4. Implausible Education Coding in Balance Table**

The balance table reports mean education of −11.035 for the treatment group and +4.627 for the control group, a difference of −15.662 (p=0.158). No standard coding of educational attainment (years of schooling, 1–7 ordinal category, etc.) yields negative means. This strongly suggests either a data cleaning error (e.g., mistaken variable transformation or merge) or an undocumented coding convention. Because education is used as a covariate in specification (2) and is one of the 126 variables available for double LASSO selection, a miscoded education variable could affect the OLS-with-controls and double LASSO results. Authors must clarify the coding and, if an error exists, rerun affected specifications.

**5. Pre-Registration Not Linked**

The paper repeatedly describes itself as "pre-registered" and uses this status as a key credibility claim. No registration number, platform (AsPredicted, OSF, EGAP, etc.), or link to the PAP is provided anywhere in the manuscript. Without this, it is impossible to verify that the three specifications, the CATE quintile analysis, the BH correction procedure, or the choice of primary outcome were truly pre-specified rather than chosen post-hoc. Authors must provide the pre-registration link and, if any deviations from the PAP occurred, disclose them explicitly.

---

### Minor Concerns

**1. Balance on `over_65` Not Adjusted**

The balance table shows `over_65` significant at p=0.037 (SMD=−0.149, a non-trivial standardized difference). The paper states that "none of the 126 baseline covariates differ significantly between treatment and control at the 5% level after adjusting for multiple comparisons," but the balance table reports only unadjusted p-values. With 126 covariates, at least one false rejection at 5% is expected by chance, and this single p=0.037 likely survives no correction. However, to make the balance claim credible, authors should either (a) display BH-adjusted p-values in Table 1, or (b) verify that the main result is robust to controlling for `over_65`.

**2. No Formal Equivalence Test**

The paper invokes Lakens (2017) and frames the result as an "informative null," but never conducts the TOST (two one-sided tests) equivalence procedure. Given that the confidence interval is asymmetric (lower bound −0.217 SD, upper bound +0.061 SD), the paper can rule out a positive effect of 0.06 SD but a negative effect of only 0.22 SD. A formal TOST against a ±0.20 SD equivalence region would sharpen the claim, and the asymmetry should be acknowledged in the power discussion.

**3. Index Reliability Not Reported**

The primary outcome is a three-item composite index. No Cronbach's alpha, inter-item correlations, or factor loadings are reported. If the three items (investigate, arrest warrants, government cooperation) have low internal consistency, the composite index may mask item-specific effects. Authors should report at minimum Cronbach's alpha and consider reporting treatment effects on each item separately in an appendix.

**4. Repeated Emphasis on Uncorrected Finding**

The hawkishness Q2 effect (−0.310, p=0.031) appears in the introduction, the robustness section, and twice in the discussion — four mentions for a finding that explicitly does not survive multiple-testing correction. This disproportionate emphasis risks anchoring the reader on a finding the paper's own procedures deem unreliable. It should appear once, in the robustness section, with a clear statement that it is exploratory.

**5. Double LASSO Selection Not Reported**

The number and identity of variables selected by the double LASSO is never disclosed. At minimum, the number of variables selected for the outcome equation and the treatment propensity equation should be reported (an appendix table is sufficient). This matters because with 126 candidate variables and N=759, the LASSO may be selecting nearly as many variables as in a saturated OLS, or conversely may be selecting zero controls.

**6. Sample Platform Not Named**

The online survey platform is never identified. This is material for assessing representativeness: Lucid, Prolific, and MTurk panels have documented differences in political attitudes and survey engagement that can moderate framing effects. The data audit also flags the absence of survey weights. Authors should name the platform, report its claimed sampling strategy, and either apply appropriate weights or explicitly acknowledge that results may not be population-representative.

**7. Confidence Intervals Around Lee Bounds**

Separate from Major Concern 1, even if the authors clarify the Lee bounds presentation, standard practice (Imbens & Manski 2004; Stoye 2009) is to report confidence intervals for the identified set, not just the point-identified bounds. The current table provides no standard errors for the bounds.

---

### Recommendation

**Major Revision**

The paper addresses an interesting and practically relevant question with a credible experimental design. The finding of an informative null — if the methodology is sound — has clear policy value. However, the Lee bounds misrepresentation (a verifiable error that could be read as contradicting the main finding), the unexplained N attrition, the absence of a manipulation check, the education coding anomaly, and the missing pre-registration link collectively require substantive revision before the null result can be confidently characterized as robust.

---

```json
{
  "score": 72,
  "decision": "MAJOR_REVISIONS",
  "dimension_scores": {
    "identification_strategy": 78,
    "estimation_implementation": 65,
    "statistical_inference": 72,
    "robustness_sensitivity": 63,
    "replication_readiness": 58
  },
  "sanity_checks": {
    "sign": "PASS",
    "magnitude": "PASS",
    "dynamics": "NA",
    "consistency": "FAIL"
  },
  "major_comments": [
    "Lee bounds [−0.118, −0.053] exclude zero but are described as consistent with a null result. Authors must report CIs around the Lee bounds and clarify whether point bounds or inferential bounds include zero. As presented, this is a verifiable misrepresentation.",
    "N discrepancy: abstract and text state N=784 but all regressions use N=760. The 24 missing outcome observations are never explained. Source of attrition must be documented, and differential attrition by arm must be tested.",
    "No manipulation check reported. A framing experiment with a single-word treatment cannot distinguish a true null from a design-failure null (respondent inattention) without a comprehension or attention check.",
    "Education balance mean of −11.035 in treatment group is implausible under any standard coding convention. This raises concerns about data cleaning errors affecting the OLS-controls and double LASSO specifications.",
    "No pre-registration number, platform, or PAP link is provided despite the paper's repeated claims of pre-registration. This prevents verification of which specifications were pre-specified."
  ],
  "minor_comments": [
    "Balance table shows over_65 at p=0.037 (SMD=−0.149) with unadjusted p-values; the multiple-comparison adjustment claim is unverifiable without adjusted p-values in the table.",
    "No formal TOST equivalence test conducted despite invoking Lakens (2017). The CI is asymmetric (rules out +0.06 SD but not −0.22 SD), which should be acknowledged.",
    "No Cronbach's alpha or inter-item correlations for the three-item ICC accountability index.",
    "The hawkishness Q2 uncorrected finding (p=0.031) is mentioned four times and appears to receive disproportionate narrative emphasis given it fails BH correction.",
    "Double LASSO variable selection not reported (number and identity of selected controls).",
    "Survey platform not named; no survey weights applied despite data audit warning.",
    "Confidence intervals around Lee bound endpoints should be reported per Imbens-Manski/Stoye standards."
  ]
}
```