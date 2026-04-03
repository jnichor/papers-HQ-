## Fact-Check Report

### 1. Citation Accuracy

The document contains only **two explicit citations** in the novelty section:

**Chong & Druckman (2007)**
- **Verified REAL.** Dennis Chong (Northwestern/USC) and James Druckman (Northwestern) are among the most prominent political scientists working on framing. The 2007 reference almost certainly points to "Framing Theory" (*Annual Review of Political Science*, 10:103–126) or their companion piece "A Theory of Framing and Opinion Formation in Competitive Elite Environments" (*Journal of Communication*, 2007). Both exist and are correctly described as foundational to the framing effects literature. Attribution is accurate.

**Sniderman & Theriault (2004)**
- **Verified REAL** but with a caveat. Paul Sniderman (Stanford) and Sean Theriault wrote "The Structure of Political Argument and the Logic of Issue Framing," which appears as a chapter in *Studies in Public Opinion* (Saris & Sniderman, eds., Princeton UP, 2004) — a book chapter, not a journal article. The citation is real and correctly attributed. The evaluation's claim that this paper is part of the "large and mature framing effects literature" is accurate.

No fabricated citations detected.

---

### 2. Completeness — Missing Key Papers

The review is sparse because it only gestures at the framing literature rather than reviewing it systematically. Several papers would be expected in a referee-quality review:

**Framing effects foundations (conspicuously absent):**
- Entman (1993) — "Framing: Toward Clarification of a Fractured Paradigm," *Journal of Communication* — the most-cited definition of framing; its absence is notable
- Tversky & Kahneman (1981) — original equivalency framing effects (*Science*) — relevant if the design involves gain/loss framing of legal categories
- Nelson, Clawson & Oxley (1997) — framing and tolerance (*American Political Science Review*) — directly relevant to opinion change via framing

**Survey experiment methodology (absent):**
- Gerber & Green (2012) — *Field Experiments* — standard reference for RCT credibility arguments
- Broockman & Kalla (2016) — "Durably reducing transphobia" (*Science*) — relevant for comparing persuasion durability on politically charged topics
- Kertzer & Brutger (2016) — decomposing audience costs (*American Journal of Political Science*) — methodologically closest to this design's CATE logic

**Public opinion on international law and ICC (directly relevant gap papers, all absent):**
- Tomz & Weeks (2013) — public opinion and international institutions (*American Political Science Review*)
- Kertzer & Zeitzoff (2017) — bottom-up microfoundations of international relations attitudes (*Journal of Conflict Resolution*)
- Brutger & Kertzer (2018) — public opinion and international courts — this line of work is the closest methodological cousin and its omission is the most significant gap in the review
- Hillebrecht & Stroh (2012) — public support for the ICC — directly on topic

**Challenging/contradicting papers (entirely absent):**
- Druckman (2001) — "The Implications of Framing Effects for Citizen Competence" (*Political Behavior*) — argues framing effects are often small and context-dependent; this would raise the null-result prior
- Leeper & Slothuus (2014) — "Political Parties, Motivated Reasoning, and Public Opinion Formation" — directly relevant to why partisan identity (here: `pro_israel_score`) may dominate label effects
- Broockman & Kalla (2022) — limits of persuasion literature — raises prior on null/small effects

---

### 3. Gap Assessment

**Is the claimed gap genuine?**

Partially. The specific claim — "first clean causal estimate of legal label precision on international justice preferences" — is plausible but the review does not demonstrate awareness of the closest existing work (Brutger & Kertzer; Tomz & Weeks). Without engaging those papers, the novelty claim is asserted rather than demonstrated.

**Could working papers fill this gap?**

Yes, and with high probability. The Israel/Gaza ICC proceedings became internationally prominent in late 2023 (the South Africa ICJ case) and the ICC arrest warrants for Netanyahu/Gallant issued in November 2024. Given the 12–18 month lag from data collection to working paper, there are almost certainly 3–8 working papers currently in circulation on public opinion and ICC support in this context. The APSA 2025 and EPSA 2025 programs would be the first places to check.

**Is the gap real or a data/method limitation?**

The gap is real. Prior work on ICC public opinion (Hillebrecht; Brutger & Kertzer) uses observational designs or post-treatment measurement. A clean experimental isolation of label effects is genuinely new. The gap is an opportunity, not an artifact.

---

### 4. Risk Assessment

**Null result risk: MEDIUM-HIGH**

The framing literature (Druckman 2001; Chong & Druckman 2010 follow-up) consistently shows that framing effects are attenuated or reversed among respondents with strong priors. Given that `pro_israel_score` likely captures strong prior positions — and high-prior respondents are unlikely to be moved by legal label precision — the average treatment effect could be statistically indistinguishable from zero. The most likely finding pattern is: small ATE, larger CATE for the low-prior subgroup. That is a publishable result but not a clean "yes, labeling matters" headline.

**Competition risk: HIGH**

This topic — Israel/Palestine + ICC + public opinion + framing — is among the most actively researched intersections in international relations right now. The window between the ICC arrest warrants (November 2024) and publication is extremely crowded. Prolific and Lucid panels make data collection fast; it is nearly certain that competing papers exist at the working paper stage.

---

### Corrections to the Evaluation Itself

The evaluation is methodologically sound but the novelty section (Section 4) overstates confidence in the "first clean causal estimate" claim without having reviewed the Brutger/Kertzer line of work. The 6/10 novelty score may be slightly generous if competing papers are already circulating — 5/10 would be defensible given competition risk.

---

```json
{
  "citations_verified": true,
  "suspicious_citations": [],
  "missing_key_papers": [
    "Entman (1993) - 'Framing: Toward Clarification of a Fractured Paradigm', Journal of Communication",
    "Brutger & Kertzer (2018) - public opinion and international courts, closest methodological cousin",
    "Tomz & Weeks (2013) - public opinion and international institutions, APSR",
    "Kertzer & Zeitzoff (2017) - microfoundations of IR attitudes, AJPS",
    "Druckman (2001) - 'Implications of Framing Effects for Citizen Competence', Political Behavior — challenges null-result prior",
    "Leeper & Slothuus (2014) - partisan identity dominates framing effects — directly relevant to pro_israel_score heterogeneity",
    "Hillebrecht & Stroh (2012) - public support for ICC — directly on-topic baseline"
  ],
  "gap_confirmed": true,
  "null_result_risk": "MEDIUM",
  "competition_risk": "HIGH"
}
```