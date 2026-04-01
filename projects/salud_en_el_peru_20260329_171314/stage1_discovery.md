Here are three published papers covering distinct sub-topics in **Salud en el Perú**, each using methods compatible with cross-sectional data.

---

## Paper 1 — Health Financing / Informal Payments

**Title:** Informal payments in health facilities in Peru in 2018: Analysis of a cross-sectional survey

**Authors:** Laura Espinoza-Pajuelo, Patricia Mallma, Hannah Hogan Leslie, Patricia Jannet García

**Journal:** *PLOS Global Public Health*, 4(1): e0001837

**Year:** 2024

**DOI/URL:** [10.1371/journal.pgph.0001837](https://journals.plos.org/globalpublichealth/article?id=10.1371/journal.pgph.0001837)

**Summary:** Using the 2018 ENAHO nationally representative cross-sectional survey (n = 132,355), the study found that direct self-reports of informal payment in public health facilities were very low (<0.5%), but indirect indicators revealed substantially higher rates of undisclosed payments, with insured patients still incurring costs for services that should be free. Both direct and indirect measurement approaches pointed to SIS-MINSA beneficiaries as a particularly vulnerable group.

**Applicable method → your data:** The authors apply **bivariate and multivariate logistic regression** on a complex survey design — identical to the ENAHO structure of your dataset (it uses FACTOR07 as the expansion factor, plus CONGLOME/VIVIENDA/ESTRATO as strata/cluster identifiers). Because the model is estimated at a single cross-section, there is no need to follow individuals over time; the treatment variable (insurance type) varies across units observed simultaneously, which is exactly how your 2024 ENAHO module is structured.

**Sub-topic:** Health financing / out-of-pocket & informal payments

---

## Paper 2 — Child & Maternal Nutrition

**Title:** Exploring the magnitude and drivers of the double burden of malnutrition at maternal and dyad levels in peri-urban Peru: A cross-sectional study of low-income mothers, infants and young children

**Authors:** Pradeilles R, Landais E, Pareja R, Eymard-Duvernay S, Markey O, Holdsworth M, Rousham EK, Creed-Kanashiro HM

**Journal:** *Maternal & Child Nutrition*, 19(4): e13549

**Year:** 2023

**DOI/URL:** [10.1111/mcn.13549](https://onlinelibrary.wiley.com/doi/10.1111/mcn.13549)

**Summary:** In a cross-sectional sample of 244 low-income mother–child dyads from peri-urban Lima communities, the study found double burden of malnutrition (DBM) prevalence of 19.9% at the maternal level and 36.3% at the dyad level. Multivariate logistic regression revealed that dietary diversity and household socioeconomic position were key drivers of DBM independently of child age and sex.

**Applicable method → your data:** The paper uses **multivariate logistic regression with binary outcome construction** (overweight/obesity + anaemia combined indicator), a method entirely suited to cross-sectional data. Your dataset contains health-module variables (P40\* group) that can similarly be combined into composite nutritional or morbidity outcomes, and the socioeconomic stratification variables (ESTRATO, DOMINIO, UBIGEO) replicate the contextual controls used in this study.

**Sub-topic:** Child & maternal nutrition / double burden of malnutrition

---

## Paper 3 — Mental Health / Depression

**Title:** Disparities in the prevalence of screened depression at different altitudes in Peru: A retrospective analysis of the ENDES 2019

**Authors:** Zegarra-Rodríguez CA, Plasencia-Dueñas NR, Failoc-Rojas VE

**Journal:** *PLOS One*, 17(12): e0278947

**Year:** 2022

**DOI/URL:** [10.1371/journal.pone.0278947](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0278947)

**Summary:** Analyzing the 2019 ENDES cross-sectional survey, the study found that residence above 1,500 m.a.s.l. was independently associated with depressive symptoms (adjusted prevalence ratio ≈ 1.38–1.41) after controlling for sex, education, smoking, and disability status. The geographic gradient persisted across the three altitude strata, pointing to hypoxia-related or social isolation mechanisms beyond standard socioeconomic confounders.

**Applicable method → your data:** The authors apply **Poisson regression with robust variance** to estimate prevalence ratios (PRs) — the preferred alternative to logistic regression for common binary outcomes in cross-sectional data because odds ratios overestimate relative risk when prevalence exceeds 10%. Your dataset includes UBIGEO (down to the district level), which encodes altitude zones implicitly, and the P40\* / D41\* health variables can serve as mental health screening proxies. No time tracking of individuals is needed.

**Sub-topic:** Mental health / depression

---

```json
{
  "topic": "Salud en el Perú",
  "data_profile": {
    "rows": 110451,
    "cols": 901,
    "structure": "cross-sectional",
    "panel": false,
    "id_cols": ["CONGLOME", "VIVIENDA", "HOGAR", "CODPERSO", "UBIGEO"],
    "time_cols": ["AÑO", "MES"],
    "warnings": []
  },
  "seed_papers": [
    {
      "title": "Informal payments in health facilities in Peru in 2018: Analysis of a cross-sectional survey",
      "authors": "Espinoza-Pajuelo L, Mallma P, Leslie HH, García PJ",
      "journal": "PLOS Global Public Health",
      "year": 2024,
      "doi_or_url": "https://doi.org/10.1371/journal.pgph.0001837",
      "summary": "Using the 2018 ENAHO cross-sectional survey (n=132,355), the study found that direct reports of informal health payments were below 0.5% but indirect indicators revealed substantially higher undisclosed costs, especially among SIS-MINSA beneficiaries who should receive free services. Multivariate logistic regression identified insurance type and facility type as primary predictors of informal payment exposure.",
      "applicable_method": "Multivariate logistic regression on complex survey design (strata=ESTRATO, cluster=CONGLOME, weight=FACTOR07) — identical design to user's 2024 ENAHO dataset; no longitudinal tracking required."
    },
    {
      "title": "Exploring the magnitude and drivers of the double burden of malnutrition at maternal and dyad levels in peri-urban Peru: A cross-sectional study of low-income mothers, infants and young children",
      "authors": "Pradeilles R, Landais E, Pareja R, Eymard-Duvernay S, Markey O, Holdsworth M, Rousham EK, Creed-Kanashiro HM",
      "journal": "Maternal & Child Nutrition",
      "year": 2023,
      "doi_or_url": "https://doi.org/10.1111/mcn.13549",
      "summary": "In 244 low-income mother-child dyads from peri-urban Lima, DBM prevalence reached 19.9% at the maternal level and 36.3% at the dyad level. Logistic regression showed dietary diversity and household socioeconomic position as independent predictors of malnutrition outcomes, controlling for child age and sex.",
      "applicable_method": "Multivariate logistic regression with composite binary outcome — adaptable to user's P40*/D41* health variables to build nutritional or chronic disease indicators; DOMINIO and ESTRATO provide equivalent urban/socioeconomic stratification."
    },
    {
      "title": "Disparities in the prevalence of screened depression at different altitudes in Peru: A retrospective analysis of the ENDES 2019",
      "authors": "Zegarra-Rodríguez CA, Plasencia-Dueñas NR, Failoc-Rojas VE",
      "journal": "PLOS One",
      "year": 2022,
      "doi_or_url": "https://doi.org/10.1371/journal.pone.0278947",
      "summary": "Analyzing the 2019 ENDES cross-sectional survey, residence above 1,500 m.a.s.l. was independently associated with depressive symptoms (aPR 1.38–1.41) after controlling for sex, education, and disability. The altitude gradient persisted across three strata, suggesting mechanisms beyond conventional socioeconomic confounders.",
      "applicable_method": "Poisson regression with robust variance to estimate prevalence ratios — preferred for common binary outcomes in cross-sectional data; user's UBIGEO encodes altitude zones at the district level without requiring panel follow-up."
    }
  ]
}
```

---

Sources:
- [Informal payments in health facilities in Peru in 2018 — PLOS Global Public Health](https://journals.plos.org/globalpublichealth/article?id=10.1371/journal.pgph.0001837)
- [PubMed: Informal payments in health facilities in Peru in 2018](https://pubmed.ncbi.nlm.nih.gov/38241208/)
- [Double burden of malnutrition peri-urban Peru — Maternal & Child Nutrition](https://onlinelibrary.wiley.com/doi/10.1111/mcn.13549)
- [PubMed: Double burden of malnutrition peri-urban Peru](https://pubmed.ncbi.nlm.nih.gov/37485734/)
- [Disparities in depression at altitude Peru — PLOS One](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0278947)
- [PubMed: Disparities in depression at altitude Peru](https://pubmed.ncbi.nlm.nih.gov/36542597/)