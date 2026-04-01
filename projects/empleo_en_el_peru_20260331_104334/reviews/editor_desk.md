## Desk Review Decision

**Paper:** "COVID-19 and the Formality Recovery Path in Peru: A Worker-Level Panel DiD Using Sectoral Teleworkability"

---

### Assessment

**Scope and fit** ✓ — Well-defined question with clear policy relevance. Permanent vs. transitory informality scarring in a high-informality developing economy is an important gap in the literature. The 4-year window post-shock is a genuine contribution over existing work.

**Methodological soundness** ✓ with flags — The Dingel-Neiman teleworkability DiD is now standard in the COVID literature and the logic is sound. However, two issues warrant referee scrutiny: (1) no pre-2020 baseline makes parallel trends untestable by design, and (2) the "panel" is effectively a repeated cross-section (96.9% attrition by 2024, only 0.5% balanced). Authors acknowledge both, which is in their favor, but the causal claim of "worker-level scarring" is stronger than the design supports.

**Data adequacy** ✓ with flags — ENAHO is appropriate and well-characterized. The sharp divergence across informality definitions (social security: 0.089; contract: 0.002; firm size: 0.047) is substantively interesting but also raises measurement concerns about what is actually being identified.

**Presentation quality** ✓ — Clear, well-organized, limitations honestly disclosed.

**Potential contribution** ✓ — First long-run causal estimate of COVID informality scarring in Peru with a large sample. Policy implication (portable social protection) is novel and direct.

---

### Decision

```json
{
  "desk_decision": "PROCEED",
  "reason": "The paper addresses a well-defined and policy-relevant question using a credible identification strategy on a large, nationally representative dataset. The main findings are clearly presented and the authors honestly disclose the key limitations (no pre-trends test, rotating panel, baseline contamination). The divergence across informality definitions and the US-to-Peru teleworkability crosswalk validity are open questions that merit referee scrutiny rather than desk rejection. The paper clears the minimum bar for peer review.",
  "referee_1_type": "CREDIBILITY",
  "referee_2_type": "MEASUREMENT"
}
```

---

### Guidance for Referees

**CREDIBILITY referee** should focus on:
- The untestable parallel trends assumption — are teleworkable and contact-intensive workers plausibly on common pre-trends given their large baseline differences (8.2 pp gap in 2020, lower incomes, different sectors)?
- Whether the "panel DiD" framing is defensible given ~97% attrition by 2024; the design is closer to repeated cross-sections, and the within-estimator results rest on very thin identifying variation
- The 2020 baseline contamination: if fieldwork straddled the March lockdown, the reference year is partially treated and DiD coefficients may understate the true effect
- Whether the non-differential attrition result is sufficient, or whether selective survival within the informal sector could still bias results

**MEASUREMENT referee** should focus on:
- Validity of the US O*NET → ISCO-08 crosswalk for Peru: task content in occupations like "agriculture" or "personal services" may differ materially between the US and Peru; the Saltiel (2020) developing-country adaptation should be implemented, not just recommended
- The striking divergence across informality definitions (social security coefficient 45× larger than the contract coefficient) — does this reflect measurement error in different survey items, differential compliance with different formality dimensions, or a genuine theoretical distinction that the paper should explain more rigorously?
- Whether 75.7% of workers falling in the "treated" group is a feature or a problem for identification — with so few teleworkable workers, the comparison group may not be representative of counterfactual trends