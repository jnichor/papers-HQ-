## EVALUATION

---

### 1. Research Question Clarity — **8/10**

The question is specific, well-bounded, and directly answerable with the collected data. The causal claim is crisp: random assignment to "apartheid" vs. "persecution" label → ICC referral support. Holding casualty salience constant is an important design feature that isolates the labeling effect.

Minor deductions: the proposed mechanism is underdeveloped. "Historical weight" is asserted but not unpacked — is the mechanism (a) moral contagion from the apartheid prototype, (b) legal precision signaling, or (c) political identity activation? These have different implications for CATE patterns and would sharpen the hypothesis.

---

### 2. Identification Strategy — **8/10**

**Source of exogenous variation**: Random assignment to label condition within a survey experiment. This is clean, well-understood, and credible. The variation is researcher-generated, not found — no endogeneity of treatment assignment.

**Identification Tier: Tier 1 (RCT)**. The strategy satisfies the gold standard for internal validity.

**Design execution notes**:
- Balance checks are mentioned — appropriate
- LASSO covariate selection improves precision but introduces researcher degrees of freedom if not pre-registered; pre-registration is not mentioned, which is a red flag for credibility
- CATE by `pro_israel_score` quintile is a sensible and policy-relevant heterogeneity analysis
- N=1,185 is adequate for main effects; with 5 quintiles, each cell ≈ 237 × 2 arms ≈ 118/arm — tight but workable for CATE

**Internal validity** is strong. The primary concerns are survey-specific: demand effects, inattention, and comprehension — none addressed in the submission.

**Pre-trends**: Not applicable to RCT. No parallel trends test needed.

---

### 3. Data Feasibility — **9/10**

Data is already collected — eliminates the largest source of feasibility risk. Sample size is reasonable. The only deductions are: (1) sample source is unspecified (MTurk? Prolific? Nationally representative panel?), which matters for external validity; (2) key variable construction (`pro_israel_score`, ICC support measure) is not described.

---

### 4. Novelty & Contribution — **6/10**

The framing effects literature in political science is large and mature (Chong & Druckman 2007; Sniderman & Theriault 2004). Applying this paradigm to ICC referrals is the genuine contribution — this specific intersection (legal label precision × international criminal justice preferences) has limited prior work.

The claim of "first clean causal estimate of legal label precision on international justice preferences" is plausible and worth making. However, the contribution is incremental relative to the framing literature at large. The direct policy relevance for advocacy organizations partially compensates, but the theoretical advance is modest.

---

### 5. Policy Relevance / Impact — **7/10**

The context is live and high-stakes: ICC proceedings related to the Israeli-Palestinian conflict are active, and advocacy organizations genuinely face the framing choice described. The CATE by `pro_israel_score` adds practical value by identifying who is movable — a direct input into campaign targeting logic.

The main limitation: if the movable population is small (low-prior respondents only), the aggregate policy impact may be limited. Effect sizes on politically charged topics in survey experiments are often attenuated in non-WEIRD populations.

---

### 6. Threats to Validity

| Threat | Severity | Addressed? |
|--------|----------|------------|
| **Social desirability / demand effects**: Respondents may moderate answers on a politically toxic topic (Israel/ICC) toward perceived social norms, compressing true label effects | HIGH | No |
| **External validity / sample non-representativeness**: Without knowing the sampling frame, results may not generalize to general publics, policymakers, or international actors who matter for actual ICC referrals | HIGH | No — sample source unspecified |
| **Label comprehension failure**: If respondents cannot distinguish "apartheid" from "persecution" legally, the experiment measures label recognition (novelty/familiarity) rather than label meaning | MEDIUM | No — no comprehension check mentioned |
| **Construct validity of outcome**: ICC "referral support" operationalization unspecified — single item vs. index, framing of the scale item itself could interact with treatment | MEDIUM | No |
| **Pre-registration absence**: LASSO covariate selection and CATE specification may be post-hoc, inflating apparent precision | MEDIUM | No — not mentioned |

**Threats_addressed** = 10 − (2 unaddressed HIGH threats × 2) = **6**

---

### 7. Missing Elements (What a Referee Will Ask Immediately)

1. **Where is the sample from?** MTurk, Prolific, and YouGov panels have very different implications for generalizability.
2. **Was this pre-registered?** LASSO selection without pre-registration is HARK-adjacent.
3. **What is the control condition?** Is there a no-label arm? Without one, this estimates a relative effect between two active frames, not label presence vs. absence.
4. **How is ICC support measured?** Exact item wording and scale needed.
5. **How is "holding casualty salience constant" implemented?** Is casualty information present in all arms? Crossed with label? This matters for the design logic.
6. **How is `pro_israel_score` constructed?** Self-report? Index? Matters for the CATE interpretation.
7. **Power analysis?** Was N=1,185 determined by a power calculation?

---

### Composite Score Calculation

| Dimension | Score | Weight | Weighted |
|-----------|-------|--------|---------|
| Research Question | 8 | 0.15 | 1.20 |
| Identification | 8 | 0.30 | 2.40 |
| Data Feasibility | 9 | 0.20 | 1.80 |
| Novelty | 6 | 0.15 | 0.90 |
| Impact | 7 | 0.10 | 0.70 |
| Threats Addressed | 6 | 0.10 | 0.60 |
| **Total** | | | **7.60** |

---

```json
{
  "question_score": 8,
  "identification_score": 8,
  "data_score": 9,
  "novelty_score": 6,
  "impact_score": 7,
  "threats_addressed_score": 6,
  "composite_score": 7.6,
  "top_threats": [
    "social desirability / demand effects on politically toxic topic",
    "external validity — sample source unspecified, limits generalizability",
    "label comprehension failure — apartheid vs. persecution may be indistinguishable to lay respondents",
    "pre-registration absent — LASSO and CATE specification may be post-hoc"
  ],
  "verdict": "PROMISING",
  "one_line_summary": "Clean RCT design on a live policy question; strong internal validity but credibility hinges on pre-registration status, sample representativeness, and whether respondents can actually distinguish the two legal labels."
}
```

---

---

## META-REVIEW

**Fairness**: The evaluation appropriately rewards the Tier 1 identification strategy with a high score (8/10) — this is correct given the constraint that Tier 4 cannot exceed 6/10. The novelty score of 6/10 is fair: the framing effects literature is genuinely large and the contribution, while real, is domain-specific rather than methodologically transformative. The data score of 9/10 is justified given the data-in-hand situation.

**Consistency**: Narrative and scores are well-aligned throughout. The identification narrative explains why 8 rather than 9 or 10 (missing pre-registration, demand effects). The threats section correctly identifies two HIGH-severity unaddressed threats and applies the formula accordingly.

**Completeness**: The evaluation captures the main issues. One strength that could have been foregrounded more prominently: the CATE analysis by `pro_israel_score` is arguably the most scientifically and practically interesting aspect of the design — it turns a simple A/B test into a heterogeneous treatment effects study. This is well-noted but perhaps underweighted in the impact score. Conversely, the evaluation correctly flags the missing control arm, which is a non-trivial design ambiguity.

**Constructiveness**: Criticisms are specific and actionable. The referee questions in Section 7 give the researcher a concrete revision checklist. The threat table's "Addressed?" column is particularly useful for prioritization.

**One potential adjustment**: The identification score of 8 is defensible, but a referee might argue 7 is more appropriate given the absence of pre-registration documentation for LASSO specification — post-hoc covariate selection can substantially alter survey experiment results. However, 8 is within a reasonable range and not a misrepresentation.

**AGREE**