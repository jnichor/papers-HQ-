## Literature Fact-Check

### Citation Verification

**All cited papers appear real and correctly attributed:**

| Citation | Verification | Notes |
|---|---|---|
| Bazzi & Blattman (2014) | **VERIFIED** | "Economic Shocks and Conflict: Evidence from Commodity Prices," *AEJ: Macroeconomics*. Finding described (commodity prices → conflict/institutions) is accurate, though the paper finds limited effects on conflict *onset* specifically. |
| Dube & Vargas (2013) | **VERIFIED** | "Commodity Price Shocks and Civil Conflict: Evidence from Colombia," *Review of Economic Studies*. Correctly attributed. |
| Goodman-Bacon (2021) | **VERIFIED** | "Difference-in-differences with variation in treatment timing," *Journal of Econometrics*. |
| de Chaisemartin & D'Haultfœuille (2020) | **VERIFIED** | "Two-Way Fixed Effects Estimators with Heterogeneous Treatment Effects," *American Economic Review*. |
| Callaway & Sant'Anna (2021) | **VERIFIED** | "Difference-in-Differences with Multiple Time Periods," *Journal of Econometrics*. |
| Sun & Abraham (2021) | **VERIFIED** | "Estimating dynamic treatment effects in event studies with heterogeneous treatment effects," *Journal of Econometrics*. |
| Ross (2001, 2012) | **VERIFIED** | "Does Oil Hinder Democracy?" (*World Politics*, 2001); *The Oil Curse* (Princeton UP, 2012). |
| Levitsky & Ziblatt (2018) | **VERIFIED** | *How Democracies Die*, Crown Publishers. |
| Bermeo (2016) | **VERIFIED** | "On Democratic Backsliding," *Journal of Democracy*. |
| Haggard & Kaufman (1995) | **VERIFIED** | *The Political Economy of Democratic Transitions*, Princeton UP. |
| Gruss-Kebhaj CTOT | **VERIFIED** | IMF Working Paper WP/19/21 (2019). Described coverage (~2018 vintage) is accurate. |
| V-Dem | **VERIFIED** | Coverage from 1789, ~180+ countries, as described. |

**One minor accuracy flag**: Bazzi & Blattman (2014) is somewhat mischaracterized as studying "commodity shocks and institutions" — the paper is primarily about conflict, and its findings on institutions are secondary/indirect. This is not fabrication but a slight overreach in the description.

---

### Missing Key Papers

Several significant omissions:

**DiD Methodology** — the review cites Goodman-Bacon, de Chaisemartin, Callaway-Sant'Anna, and Sun-Abraham, but omits:
- **Borusyak, Jaravel & Spiess (2024)** — "Revisiting Event Study Designs: Robust and Efficient Estimation," *Review of Economic Studies*. This is now a standard reference alongside Callaway-Sant'Anna for staggered DiD and is particularly relevant for event-study designs like the one proposed.
- **Roth et al. (2023)** — "What's Trending in Difference-in-Differences? A Synthesis of the Recent Econometrics Literature," *Journal of Econometrics*. A referee would expect this survey cited.

**Commodity Shocks & Political Outcomes** — directly relevant omissions:
- **Brückner & Ciccone (2010)** — "International Commodity Prices, Growth and the Outbreak of Civil War in Sub-Saharan Africa," *Economic Journal*. Uses commodity prices as instruments for income shocks and political outcomes in a design close to what is proposed here.
- **Arezki & Brückner (2011)** — "Oil Rents, Corruption, and State Stability: Evidence from Panel Data Regressions," *European Economic Review*. Directly tests commodity windfalls and institutional quality.

**Ratchet/Crisis Consolidation** — the specific theoretical mechanism has prior work:
- **Pepinsky (2009)** — *Economic Crises and the Breakdown of Authoritarian Regimes* (Cambridge UP). Studies how economic crises interact with authoritarian persistence — directly relevant to whether crises consolidate rather than reverse repression.
- **Ferejohn & Pasquino (2004)** — "The Law of the Exception: A Typology of Emergency Powers," *International Journal of Constitutional Law*. Foundational for the theoretical mechanism of emergency powers persisting post-crisis.

**Resource Curse Baseline**:
- **Sachs & Warner (1995/1997)** — the foundational resource curse paper is conspicuously absent given the paper's positioning in this literature.

---

### Gap Assessment

**The gap is genuine but partially filled by working papers.** The causal identification literature on *asymmetric* political responses to commodity cycles is thin. However:

- The gap is partly a **data/method limitation** rather than pure oversight: identifying full bust-recovery cycles requires long panels and clean episode definitions, which explains why prior work focuses on shocks rather than cycles.
- Several **NBER/SSRN working papers** in the political-economy-of-crises space (post-2020) likely address adjacent questions. A thorough search before submission is warranted.
- The gap is **genuinely valuable to fill**: policymakers and IFIs implicitly assume recovery symmetry; disconfirming evidence would have real policy stakes.

---

### Risk Assessment

**Null result risk: MEDIUM.** Bazzi & Blattman (2014) itself finds that commodity price effects on conflict onset are surprisingly limited (though incidence effects exist). If the civil liberties channel is similarly muted, the ratchet test may simply confirm symmetric near-zero effects. The disaggregation by liberty type partly mitigates this — some dimensions (assembly, expression) may show stronger signals than aggregate indices.

**Identification critique risk: HIGH.** The staggered TWFE problem is well-known and referees in top journals will flag it immediately. The evaluation correctly identifies this as the core weakness. Brückner & Ciccone (2010) used a similar commodity-price IV design and received close scrutiny on confounding; this paper will face the same.

**Competition risk: MEDIUM.** The commodity-institutions space is active (multiple groups work on resource curse + V-Dem combinations), but the specific ratchet/asymmetry framing with recovery cycles is distinctive enough to reduce direct overlap risk.

---

```json
{
  "citations_verified": true,
  "suspicious_citations": [
    "Bazzi & Blattman (2014) is accurately cited but slightly mischaracterized as an 'institutions' paper — it is primarily a conflict paper; institutional findings are secondary"
  ],
  "missing_key_papers": [
    "Borusyak, Jaravel & Spiess (2024) — staggered DiD, Review of Economic Studies",
    "Roth et al. (2023) — DiD synthesis survey, Journal of Econometrics",
    "Brückner & Ciccone (2010) — commodity prices and political outcomes, Economic Journal",
    "Arezki & Brückner (2011) — oil rents and state stability, European Economic Review",
    "Pepinsky (2009) — economic crises and authoritarian persistence, Cambridge UP",
    "Sachs & Warner (1995/1997) — foundational resource curse paper",
    "Ferejohn & Pasquino (2004) — emergency powers persistence, theoretical mechanism"
  ],
  "gap_confirmed": true,
  "null_result_risk": "MEDIUM",
  "competition_risk": "MEDIUM"
}
```