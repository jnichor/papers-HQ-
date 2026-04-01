Here are 3 published academic papers on **Empleo en el Perú**, each covering a distinct sub-topic and using methods directly applicable to your wide-panel data.

---

## Paper 1 — Informality

**"Large Firms and the Intensive Margin of Labor Informality: Evidence from an Enforcement Intervention in Peru"**
Mariano Bosch, Guillermo Cruces, Stephanie González, María Teresa Silva-Porto
*Journal of Development Economics*, 2025
DOI/URL: [https://www.sciencedirect.com/science/article/pii/S0304387825002305](https://www.sciencedirect.com/science/article/pii/S0304387825002305)

**Summary:** Using a randomized mailing experiment with Peru's labor inspection authority (SUNAFIL), the paper shows that deterrence letters sent to large formal firms (>50 workers) increased formal social-security enrollment by ~9.8%, with effects concentrated in very large firms during high-demand seasons. The benefit-cost ratio of the intervention is estimated at 50–78x.

**Applicable method:** Event study with firm × month two-way fixed effects (TWFE). After reshaping your wide data to long format (one row per individual-year), you can implement TWFE with `individual FE + year FE` to estimate causal effects of a policy change (e.g., labor regulation enforcement) on employment outcomes, while controlling for time-invariant individual heterogeneity and aggregate time trends. Flat pre-trends are testable with the annual structure you already have (2020–2024).

**Sub-topic:** Informality / enforcement

---

## Paper 2 — Employment Transitions

**"Labor Market Transitions in Peru"**
Javier Herrera, Gerardo David Rosas Shady
*IAD Discussion Paper Series (Göttingen)*, 2003
URL: [https://ideas.repec.org/p/got/iaidps/109.html](https://ideas.repec.org/p/got/iaidps/109.html) | Semantic Scholar: [link](https://www.semanticscholar.org/paper/Labor-Market-Transitions-in-Peru-Herrera-Shady/b7e2f6adc58dc3248a4f7103841fec0f0b9ede00)

**Summary:** Using ENAHO panel data (1997–1999), the paper shows that Peru's labor market is characterized by high flows between employment and inactivity rather than between employment and unemployment, a pattern invisible in cross-sectional unemployment statistics. A first-order Markov process confirms that past employment state significantly predicts current state.

**Applicable method:** Markov transition matrices. After reshaping to long format, you construct an employment-state variable per individual-year and compute year-over-year transition probability matrices (e.g., employed → informal, informal → unemployed). Your 5-wave panel (2020–2024) yields 4 consecutive transition matrices, enabling comparison of mobility patterns across pre/post-COVID periods — directly matching the "dynamic panel" methods listed as applicable to your structure.

**Sub-topic:** Employment transitions / labor mobility

---

## Paper 3 — Gender Wage Gap

**"The Gender Wage Gap in Peru: Drivers, Evolution, and Heterogeneities"**
Giannina Vaccaro, Mirko Basurto, Arlette Beltrán, Lucía Montoya
*Social Inclusion*, Vol. 10(1), pp. 19–34, 2022
DOI: [10.17645/si.v10i1.4757](https://www.cogitatiopress.com/socialinclusion/article/view/4757)

**Summary:** Using ENAHO data (2007–2018), the paper finds that the unexplained gender wage gap has remained stagnant at ~17% throughout the study period despite improvements in women's educational endowments, pointing to structural discrimination and social norms as persistent drivers. Regional heterogeneities reveal smaller gaps where female headship rates are higher and GDP is larger.

**Applicable method:** Pooled OLS / correlated random effects with year fixed effects + Oaxaca-Blinder decomposition. After reshaping to long format, you can pool all 5 waves, regress log-wages on a gender indicator and controls with year fixed effects, then decompose the gap into endowment vs. coefficient components. Your panel structure also enables adding individual fixed effects to partial out time-invariant unobservables, going beyond what the original paper could do with repeated cross-sections.

**Sub-topic:** Gender wage gap / earnings inequality

---

```json
{
  "topic": "Empleo en el Perú",
  "data_profile": {
    "rows": 348505,
    "cols": 7337,
    "structure": "wide-panel",
    "panel": true,
    "id_cols": ["conglome", "vivienda"],
    "time_cols": [],
    "warnings": []
  },
  "seed_papers": [
    {
      "title": "Large Firms and the Intensive Margin of Labor Informality: Evidence from an Enforcement Intervention in Peru",
      "authors": "Mariano Bosch, Guillermo Cruces, Stephanie González, María Teresa Silva-Porto",
      "journal": "Journal of Development Economics",
      "year": 2025,
      "doi_or_url": "https://www.sciencedirect.com/science/article/pii/S0304387825002305",
      "summary": "RCT with SUNAFIL deterrence letters to large Peruvian firms shows a 9.8% increase in formal social-security enrollment, concentrated in very large firms during peak demand seasons. Cost-benefit ratio is 50–78x, implying low-cost enforcement can yield large formalization gains.",
      "applicable_method": "TWFE event study (firm/individual FE + year FE): after wide-to-long reshape, estimate causal policy effects on employment outcomes while controlling for individual heterogeneity and time trends; flat pre-trends testable over 2020–2024 waves."
    },
    {
      "title": "Labor Market Transitions in Peru",
      "authors": "Javier Herrera, Gerardo David Rosas Shady",
      "journal": "IAD/Göttingen Discussion Paper Series",
      "year": 2003,
      "doi_or_url": "https://ideas.repec.org/p/got/iaidps/109.html",
      "summary": "ENAHO panel (1997–1999) reveals that Peruvian labor mobility is dominated by employment-inactivity flows rather than employment-unemployment flows, explaining the paradox of moderate unemployment alongside high perceived labor insecurity. First-order Markov tests confirm state dependence in employment status.",
      "applicable_method": "Markov transition matrices: after reshape, compute annual employment-state transition probabilities across 4 consecutive year-pairs (2020–21, 21–22, 22–23, 23–24), enabling comparison of mobility regimes before and after COVID-19 recovery."
    },
    {
      "title": "The Gender Wage Gap in Peru: Drivers, Evolution, and Heterogeneities",
      "authors": "Giannina Vaccaro, Mirko Basurto, Arlette Beltrán, Lucía Montoya",
      "journal": "Social Inclusion",
      "year": 2022,
      "doi_or_url": "https://doi.org/10.17645/si.v10i1.4757",
      "summary": "Using ENAHO (2007–2018), the unexplained gender wage gap is stagnant at ~17% despite women's endowment improvements, with regional heterogeneities linked to female headship and GDP. Structural discrimination and social norms are identified as persistent barriers.",
      "applicable_method": "Pooled panel OLS with year FE + Oaxaca-Blinder decomposition: after reshape, pool 5 waves and decompose the gender earnings gap into endowment vs. coefficient components; the panel structure additionally allows individual FE to remove time-invariant unobservables, strengthening causal inference beyond the original paper."
    }
  ]
}
```

---

Sources:
- [Large Firms and the Intensive Margin of Labor Informality — ScienceDirect](https://www.sciencedirect.com/science/article/pii/S0304387825002305)
- [Chasing Informality: Evidence from Increasing Enforcement in Large Firms in Peru — IADB](https://publications.iadb.org/en/chasing-informality-evidence-increasing-enforcement-large-firms-peru)
- [Labor Market Transitions in Peru — IDEAS/RePEc](https://ideas.repec.org/p/got/iaidps/109.html)
- [Labor Market Transitions in Peru — Semantic Scholar](https://www.semanticscholar.org/paper/Labor-Market-Transitions-in-Peru-Herrera-Shady/b7e2f6adc58dc3248a4f7103841fec0f0b9ede00)
- [The Gender Wage Gap in Peru: Drivers, Evolution, and Heterogeneities — Social Inclusion](https://www.cogitatiopress.com/socialinclusion/article/view/4757)
- [The Gender Wage Gap in Peru — IDEAS/RePEC](https://ideas.repec.org/a/cog/socinc/v10y2022i1p19-34.html)