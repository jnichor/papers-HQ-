## Literature Review Fact-Check

**Preliminary observation:** The document submitted is a research *evaluation* and *meta-review*, not a literature review. It contains almost no citations — only two informal references appear in Section 4. I will assess those references and evaluate completeness against what a proper literature review for this design should contain.

---

### 1. Citation Accuracy

Only two citations appear in the entire document:

**"Banerjee et al. graduation programs"**
- Plausible. The most likely referent is Banerjee et al. (2015, *Science*), "A multifaceted program causes lasting progress for the very poor" — a 6-country RCT of graduation programs. The claim that it "does not cleanly decompose complementarity" is accurate: that paper evaluates a bundled package without a factorial design.
- Verdict: **Plausible, not fabricated**, but imprecise.

**"some Uganda/Kenya vocational training trials"**
- Plausible referents exist: Blattman & Annan (2016, *AEJ:Applied*) on Uganda; Hicks et al. (2011) on Kenya vocational training; Alfonsi et al. (2020, *JPE*) on Uganda. The characterization that these don't "cleanly decompose complementarity" is accurate for most of them.
- Verdict: **Vague but not fabricated.** No specific paper is misattributed.

---

### 2. Completeness — Missing Key Papers

The literature review is severely thin. A credible review for a factorial RCT on job vouchers × vocational training should include:

| Paper | Why It Belongs |
|-------|---------------|
| Crépon et al. (2013, *QJE*) — French job placement RCT | Canonical design for job search assistance; SUTVA/GE concerns explicitly modeled |
| Card, Kluve & Weber (2018, *Economic Journal*) — ALMP meta-analysis | Benchmark for effect sizes on employment; prior on null result risk |
| McKenzie (2017, *World Bank Research Observer*) — ALMPs in developing countries | Directly relevant; documents typical effect magnitudes |
| Alfonsi et al. (2020, *JPE*) — Uganda vocational training | Recent, high-profile, same region |
| Bandiera et al. (2017, *QJE*) — Uganda women's empowerment | Tests complementarities between assets and skills; most structurally similar to proposed design |
| Heckman, LaLonde & Smith (1999, *Handbook of Labor Economics*) | Seminal treatment of training program evaluation |
| Muralidharan & Niehaus (2017, *JEP*) — Factorial designs in development | Methodological precedent for 2×2 designs |
| Bitler, Gelbach & Hoynes (2006, *AER*) | On distributional effects obscured by ATE in social programs |
| Gechter & Taber (2021) | Power calculations for interaction terms — directly addresses the paper's critical weakness |

**Most critical omission:** Bandiera et al. (2017) is the closest existing study. The gap claim in Section 4 would need to directly engage with this paper to survive peer review.

---

### 3. Gap Assessment

**Is the gap genuine?**
- Partially. Clean factorial RCTs decomposing complementarity between job matching and training are rare. The gap is real but narrower than stated.
- Bandiera et al. (2017) comes close. The Targeting the Ultra Poor (TUP) literature bundles transfers + training in ways that approximate this design.
- Working papers: Given active interest from IGC, J-PAL, and IPA in ALMP bundling, it would be surprising if no working paper addresses this. The gap claim should be verified against NBER, SSRN, and J-PAL registries before submission.

**Is the gap data/method-limited or a genuine opportunity?**
- Likely data-limited historically (four-arm RCTs are expensive). The opportunity is real but the bar for "we're first" is higher than the evaluation acknowledges.

---

### 4. Risk Assessment

**Null result risk: MEDIUM-HIGH**
Card et al. (2018) meta-analysis finds median employment effects of vocational training programs are modest (ITT ~2–4 pp). Interaction effects are typically smaller than main effects. Prior literature makes a precisely estimated zero β₃ quite plausible, which the evaluation correctly flags but the literature review does not support with base-rate evidence.

**Competition risk: MEDIUM**
J-PAL and IPA have active pipelines in exactly this space. The evaluation does not address this at all.

**Identification critique risk: LOW**
The 2×2 factorial RCT is methodologically robust. No credible critique of this identification approach exists in the literature.

---

### Summary

```json
{
  "citations_verified": false,
  "suspicious_citations": [
    "No fabricated citations found, but both citations are too vague to verify precisely — no author-year-journal triples are provided"
  ],
  "missing_key_papers": [
    "Bandiera et al. (2017, QJE) — Uganda women's empowerment, closest structural analogue",
    "Crépon et al. (2013, QJE) — canonical job search RCT with GE analysis",
    "Card, Kluve & Weber (2018, Economic Journal) — ALMP meta-analysis for prior effect sizes",
    "Alfonsi et al. (2020, JPE) — Uganda vocational training RCT",
    "McKenzie (2017, World Bank Research Observer) — developing country ALMP benchmark",
    "Gechter & Taber (2021) — power for interaction terms (directly relevant to fatal weakness)"
  ],
  "gap_confirmed": true,
  "null_result_risk": "MEDIUM",
  "competition_risk": "MEDIUM"
}
```

**Bottom line:** The evaluation is sound, but it overstates the novelty because it does not engage with Bandiera et al. (2017) or the TUP bundling literature. The gap exists but is narrower than claimed. The null result risk is understated — the prior from meta-analyses of ALMPs should anchor expectations toward small or zero β₃.