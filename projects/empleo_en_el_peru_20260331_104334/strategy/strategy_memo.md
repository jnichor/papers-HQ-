# Strategy Memo: COVID-19 and the Formality Recovery Path in Peru

## Research Question
Did workers in contact-intensive sectors experience a larger and more persistent
increase in informality after COVID-19, and how does the formality recovery
trajectory vary by firm size, gender, and region in Peru?

## Identification Strategy
**Method:** Two-Way Fixed Effects DiD + Event Study (Tier 1)

**Design:** Exploits differential sectoral exposure to COVID mobility restrictions
using the Dingel-Neiman (2020) teleworkability index as treatment intensity.
Workers in low-teleworkability (contact-intensive) occupations faced larger
exposure to lockdown-induced labor disruptions. The DiD compares informality
trajectories of high- vs. low-teleworkability workers before and after the
2020 shock.

**Specification:**
    informal_it = alpha_i + lambda_t + sum_k beta_k * (1[t=k] * TW_i) + X_it*gamma + epsilon_it

where TW_i is the teleworkability score (0-1, time-invariant), alpha_i are
individual FE, lambda_t are year FE, and beta_k are the event-study coefficients.
Reference year: 2020. Coefficients beta_k estimate the DIFFERENTIAL change in
informality for low- vs. high-teleworkability workers.

**Clustering:** Sector x region level (treatment assigned at occupation/sector level).

## Data
- **Primary:** ENAHO Module 500 panel 2020-2024 (348,505 individuals, parquet)
- **Teleworkability:** Dingel-Neiman (2020) crosswalk mapped to ISCO-08 2-digit
  codes, merged via ENAHO p505r4 occupation codes. File: isco2_telework_complete.csv.

## Key Variables

### Outcome: Informality (3 definitions)
1. **No social security** (p511a = 7): worker has no health insurance through employer
2. **No written contract** (p517 in {5,6}): no formal employment contract
3. **Small firm** (p510 in {1,2}): firm has <5 workers

### Treatment: Teleworkability score
- Continuous: telework_score (0-1) from Dingel-Neiman via ISCO-08 crosswalk
- Binary: telework_low = 1 if telework_score < 0.20 (contact-intensive)
- Terciles: low/mid/high contact-intensity

### Controls
- Age (p208a), gender (p207), education level, region (dominio), urban/rural (estrato)
- Survey weights: facpob07

### Panel ID
- conglome + vivienda + numper (time-invariant identifiers)

## Estimation Plan

### 00_clean.py
1. Load parquet (selective columns for memory)
2. Reshape wide to long (one row per worker-year)
3. Merge teleworkability crosswalk via p505r4 first 2 digits
4. Construct informality indicators
5. Restrict to working-age employed population (ocu500=1)

### 01_main.py
1. TWFE DiD event study: informality ~ individual FE + year FE + year*telework_low
2. Continuous treatment: informality ~ individual FE + year FE + year*telework_score
3. Heterogeneity: gender, region (Lima vs rest), firm size
4. Scarring test: Wald test beta_2024 = beta_2021

### 02_robustness.py
1. Alternative informality definitions (3 measures)
2. Balanced vs unbalanced panel
3. Attrition analysis
4. Benjamini-Hochberg correction

### 03_output.py
1. Descriptive statistics by high/low teleworkability
2. Event study plots
3. Regression tables (LaTeX)
4. Results summary
