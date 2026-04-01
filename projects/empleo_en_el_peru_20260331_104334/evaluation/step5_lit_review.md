## Literature Review: COVID-19 and Formality Recovery in Peru

---

### 1. Closest Existing Papers

**Paper 1: Bosch, Cruces, González, Silva-Porto (2025)**
*"Large Firms and the Intensive Margin of Labor Informality: Evidence from an Enforcement Intervention in Peru." Journal of Development Economics.*

Main result: SUNAFIL deterrence letters increase formal social-security enrollment by 9.8% in treated large firms, concentrated during peak demand seasons. Cost-benefit ratio 50–78x.

**Difference from proposed idea**: This is the supply-side (firm) complement. It asks *what pushes firms to formalize*. The proposed paper asks *what happened to displaced workers* after the COVID shock and whether they recover — a worker-side, demand-shock question. Bosch et al. have no panel tracking individual worker trajectories, no teleworkability instrument, and no recovery path analysis. The proposed paper is literally the "missing worker-side panel" the Bosch et al. paper cannot speak to.

---

**Paper 2: Saltiel, Fernando (2020)**
*"Who Can Work from Home in Developing Countries?" Journal of Development Economics 161.*

Main result: Only ~13% of jobs in developing countries are teleworkable (vs. ~38% in the US), with stark urban-rural and skill gradients. Applies Dingel-Neiman O\*NET scores to developing-country household surveys including LAC nations. Informality strongly predicts non-teleworkability.

**Difference from proposed idea**: Saltiel (2020) is a cross-sectional characterization exercise — it documents *who* is exposed at a point in time. It does not use the teleworkability score as an instrument for treatment in a DiD, does not follow workers longitudinally, and does not study the recovery trajectory. The proposed paper moves from Saltiel's descriptive map to a causal panel design. Critically, Saltiel's finding that informal workers are disproportionately in non-teleworkable jobs is the very mechanism the proposed paper exploits — making Saltiel (2020) both a citation and a threat-to-identification to discuss.

---

**Paper 3: Gottlieb, Grobovšek, Poschke & Saltiel (2021)**
*"Working from Home in Developing Countries." European Economic Review 132.*

Main result: Self-employment and informality are the primary reasons why teleworkability is lower in developing countries relative to rich countries. Within-country, formal salaried workers can work from home at rates closer to advanced economies. Develops a structural decomposition.

**Difference from proposed idea**: Again cross-sectional and structural — no panel, no COVID event study, no recovery path. The proposed paper's DiD design would be the first to use this cross-sectoral variation *causally* in a within-Peru longitudinal framework. The structural model also cannot identify hysteresis vs. full recovery.

---

**Paper 4: Mongey, Pilossoph & Weinberg (2021)**
*"Which Workers Bear the Burden of Social Distancing Policies?" Journal of Economic Perspectives 35(3): 141–162.*

Main result: Workers in low-work-from-home, high-physical-proximity occupations are disproportionately low-income, minority, and without college degrees. Documents differential labor market impacts during COVID using a composite exposure index.

**Difference from proposed idea**: US-focused, short-horizon, no formality dimension (irrelevant in the US context), no recovery analysis. The proposed paper transplants this exposure-based logic into a developing-country informality frame with a 5-year recovery window — a methodologically distinct and substantively richer application.

---

**Paper 5: Herrera & Rosas Shady (2003)**
*"Labor Market Transitions in Peru." IAD/Göttingen Discussion Paper 109.*

Main result: Peruvian labor mobility is dominated by employment-inactivity flows; first-order Markov tests confirm state dependence in employment status.

**Difference from proposed idea**: Uses 1997–1999 ENAHO panel — pre-digital economy, pre-COVID, no teleworkability concept. The proposed paper's contribution to the same Markovian question is to ask whether the COVID shock created a *new absorbing state* in informality, i.e., whether hysteresis broke the pre-existing transition pattern Herrera & Rosas Shady documented.

---

### 2. Methodological Precedents

**Precedent 1: Dingel & Neiman (2020)**
*"How Many Jobs Can be Done at Home?" Journal of Public Economics 189.*

Identification: Cross-occupational variation in teleworkability derived from O\*NET task characteristics — not an IV in the causal sense, but the source of the proposed paper's treatment-exposure variable. The measure has been critiqued on two grounds: (a) O\*NET is calibrated to US workers and may mis-classify occupations in lower-income settings (Saltiel addresses this directly); (b) the index is binary-collapsed from continuous task measures, losing information. **Design lesson**: The proposed paper should validate the Dingel-Neiman scores against Peru's CIIU occupation codes carefully, report the distribution of scores by sector (not just a median), and consider the continuous version rather than the binary cut.

**Precedent 2: Acemoglu, Autor, Dorn, Hanson & Price (2016)**
*"Import Competition and the Great Divergence." American Economic Review 106(5).*

Identification: Local labor market exposure DiD using Chinese import penetration interacted with pre-period industry composition. This is the canonical "Bartik-style" design that the proposed paper echoes — a worker is exposed to COVID via their sector's teleworkability, which is arguably predetermined and orthogonal to individual trends. Critique in the literature (Adão, Kolesár, Morales 2019): inference in Bartik designs can be invalid when shocks are correlated across locations/sectors, requiring leave-one-out corrections or clustering at the shift-share level. **Design lesson**: Cluster SEs at the sector level (not individual), and test robustness to alternative occupation-code aggregation levels.

**Precedent 3: Bodnár, Fadejeva, Iordache et al. (2020)** *(European Central Bank Working Paper)*
*"How Does Working from Home Affect Wages and Employment? Panel Evidence from European Employers."*

Identification: Employer-employee matched panel DiD using sudden shift to remote work. Identification concerns: selection into remote work pre-COVID correlates with productivity; the COVID shock arguably resolves this by making adoption quasi-compulsory. **Design lesson**: The proposed paper benefits from the same logic — the COVID shock forced sectoral exposure regardless of firm or worker preference, strengthening the parallel-trends assumption. The proposed paper should make this argument explicitly in its identification section.

---

### 3. Gap Analysis

**What gap does this fill?**

The existing literature has three distinct clusters: (a) cross-sectional teleworkability exposure studies (Saltiel, Dingel-Neiman, Gottlieb et al.) that characterize *who* was exposed but cannot trace recovery; (b) Latin American COVID labor-market studies (ILO, IDB series) that use aggregate or short panels without causal identification; (c) Peru-specific labor market studies (Bosch et al., Herrera & Rosas Shady) that are either firm-side or pre-COVID. No paper combines: Peru + worker-level panel + teleworkability as causal exposure + 5-year recovery window + formality as the outcome. That intersection is empty.

**Is the gap genuine or artificial?**

Largely genuine, for three reasons: (1) The 2020–2024 ENAHO panel data only recently became available in its full 5-wave form — earlier papers simply lacked the data. (2) Matching Dingel-Neiman scores to ENAHO occupation codes (p507 variants at 2-digit CIIU) requires non-trivial crosswalk work that is a barrier to entry. (3) The "recovery path" framing is a more recent research question — most COVID papers were written during 2020–2021 and could not observe recovery.

**Could the gap be artificial?**

One legitimate concern: the ENAHO panel component has known attrition and rotation structure — it is a rotating panel, not a pure cohort. If COVID caused differential survey dropout (e.g., informal workers displaced to rural areas are harder to follow), the panel is not a random sample of pre-COVID workers and hysteresis estimates will be downward biased. This is not a reason the gap is artificial, but it is a reason careful papers have not rushed in. The proposed paper must address ENAHO's attrition and rotation design explicitly — this is the single largest methodological risk.

A second concern: the Dingel-Neiman scores were calibrated on US O\*NET data. Applying them to Peru without validation could introduce classical measurement error that attenuates estimates. This is addressable (Saltiel's reweighted scores exist) but needs to be handled.

---

### 4. Positioning Statement

This paper would be cited as the primary reference for the worker-side, panel-longitudinal response to the COVID formality shock in Peru, filling the gap between aggregate descriptive accounts of informal employment growth (ILO/IDB series) and firm-level intervention studies (Bosch et al. 2025). A future paper on Latin American labor market resilience would write: *"Using sectoral teleworkability as a source of differential exposure and five waves of ENAHO panel data, [Authors] (2026) document that contact-intensive sector workers experienced significant informality hysteresis in Peru, with recovery incomplete by 2024 and concentrated among women and micro-firm employees — establishing the persistence of the formality shock as a structural feature rather than a cyclical adjustment."*

---

```json
{
  "closest_papers": [
    "Bosch, Cruces, González, Silva-Porto (2025)",
    "Saltiel (2020)",
    "Gottlieb, Grobovšek, Poschke & Saltiel (2021)",
    "Mongey, Pilossoph & Weinberg (2021)",
    "Herrera & Rosas Shady (2003)"
  ],
  "gap_is_genuine": true,
  "gap_reason": "The 5-wave 2020–2024 ENAHO panel recently became complete; no paper combines Peru-specific worker-level panel data with teleworkability identification to trace the full formality recovery trajectory. The gap reflects data availability timing and crosswalk complexity, not an obvious or uninteresting answer.",
  "novelty_assessment": "HIGH",
  "methodological_risk": "MEDIUM",
  "positioning": "This paper would be the first to causally identify informality hysteresis at the worker level in Peru following COVID-19, using sectoral teleworkability as predetermined exposure variation in a 5-year event-study panel — providing the worker-side complement to firm-level enforcement studies and the causal identification missing from aggregate COVID-informality descriptives."
}
```

---

**Key risks to flag before execution:**

1. **ENAHO rotation structure**: Verify how many individuals appear in all 5 waves (2020–2024). True balanced panel may be small; rotating-panel attrition is non-random relative to informality status.
2. **Dingel-Neiman external validity**: Use Saltiel's LAC-reweighted scores if available, and test sensitivity to US vs. LAC calibration.
3. **Staggered treatment timing**: Sectoral restrictions were lifted at different dates — standard TWFE is biased under treatment effect heterogeneity. Use Callaway-Sant'Anna (2021) or Sun-Abraham (2021) robust estimators.
4. **Single pre-COVID year**: The 2020 ENAHO was partially collected before March lockdowns. Pre-trend testing with one pre-period year is fragile — be transparent about this limitation.