# Strategy Memo: The Middle-Income Squeeze — Distributional Analysis of Health Expenditure Determinants in Peru

## Research Question
Are the conditional correlates of household health expenditure share quantile-dependent, consistent with the middle-income squeeze hypothesis? Specifically, do middle-income households face disproportionate catastrophic health expenditure (CHE) risk relative to both the poorest (who access SIS) and the wealthiest (who access EsSalud/private insurance)?

## Framing
**Descriptive/distributional** — NOT causal. We document conditional associations across the health expenditure distribution using quantile regression. We do not claim identification of causal effects.

## Data
- **Primary**: ENAHO 2024 Module 400 (health), 110,451 individuals
- **Consumption**: ENAHO 2024 Sumaria module (GASHOG2D for total household consumption)
- **Unit of analysis**: Household (aggregate to HH level using CONGLOME+VIVIENDA+HOGAR)

## Key Variables
- **Outcome**: OOP health expenditure share = health_expenditure / total_consumption
  - Health expenditure: sum of P41601-P41603 (consultation, medicine, other health costs) × 13 (annualize 4-week recall)
  - Total consumption: GASHOG2D from Sumaria
  - Floor: 5th percentile of Sumaria consumption
  - Cap at [0, 1]
- **CHE indicators**: Binary at 10%, 25%, 40% thresholds of consumption
- **Insurance**: P4191=SIS, P4192=EsSalud, P4195=EPS; construct 3 categories (SIS, EsSalud, Uninsured)
- **Controls**: age of head, female head, education, HH size, children <5, elderly 65+, rural, chronic illness, region FE
- **Consumption quintiles**: from Sumaria GASHOG2D

## Estimation
1. **OLS benchmark**: OOP_share = f(insurance, quintile, controls, region_FE)
2. **Quantile regression**: At tau = {0.10, 0.25, 0.50, 0.75, 0.90}
   - With insurance × quintile interactions
   - Cluster-robust SEs at PSU level (CONGLOME)
3. **Two-part model**: Probit(any_health_spending) + QR(OOP_share | positive spending)
4. **RIF unconditional QR**: For population-level distributional statements

## Robustness Checks
1. Alternative CHE thresholds (10%, 25%, 40%)
2. Urban vs rural sub-samples
3. Alternative consumption floor (1st percentile, 10th percentile)
4. Exclude top/bottom 1% of expenditure
5. Control sensitivity (stepwise addition)
6. Two-part model vs unconditional QR comparison
7. Weighted vs unweighted estimates

## Standard Errors
- Cluster bootstrap at PSU level (CONGLOME), 200 replications
- For robustness: HC3 sandwich SEs as comparison

## Tables
1. Summary statistics by insurance group
2. Balance/descriptive table by consumption quintile
3. OLS and QR main results (tau = 0.10, 0.25, 0.50, 0.75, 0.90)
4. Insurance × quintile interaction effects
5. Robustness checks summary
6. Two-part model results

## Figures
1. Distribution of OOP share by insurance type (KDE)
2. QTE profile across quantiles
3. Heatmap of insurance effects by quintile × quantile
4. CHE incidence by insurance and quintile
5. Robustness coefficient plot
