# Strategy Memo

## Title
Did ChatGPT Concentrate or Diversify the Language Ecosystem? A Country-Level Event Study of HHI

## Research Question
Did ChatGPT's release cause within-country language ecosystem concentration (fewer languages dominating) or diversification (long-tail growth), and does this vary by country English proficiency?

## Identification Strategy
Event study (distributed lag model) with country and quarter fixed effects. Treatment: ChatGPT public release, Q4 2022 (November 30, 2022). Since treatment is simultaneous across all countries, this is an interrupted time series with country FEs — NOT staggered DiD.

### Main Specification
```
Y_{c,q} = alpha_c + gamma_q + sum_{k=-K}^{K} beta_k * D_{q=event+k} + epsilon_{c,q}
```
- Y: HHI (primary) and Shannon entropy (secondary) of programming language shares within country c, quarter q
- alpha_c: country fixed effects (absorb time-invariant country characteristics)
- gamma_q: quarter fixed effects (absorb global trends)
- D_{q=event+k}: event-time dummies, reference period = t-1 (Q3 2022)
- K = 4+ leads and lags
- Clustering: country level (wild cluster bootstrap if N_clusters < 50)

### Heterogeneity Specification
```
Y_{c,q} = alpha_c + gamma_q + sum_k beta_k * D_{q=event+k} + sum_k delta_k * (EPI_c * D_{q=event+k}) + epsilon_{c,q}
```
- EPI_c: EF English Proficiency Index score (continuous, from ef_epi_2025.csv)
- Also run with binary high/low split (above/below median EPI) and terciles

### Treatment Timing
- Q4 2022 is a PARTIAL treatment quarter (ChatGPT launched Nov 30 = ~1 month of quarter)
- Main specification: treat Q1 2023 as period +1, drop Q4 2022 from event window
- Robustness: include Q4 2022 with fractional indicator (1/3)

## Data
- **Main dataset**: languages.csv (161,922 rows: num_pushers x language x language_type x iso2_code x year x quarter)
- **External**: ef_epi_2025.csv (123 countries: iso2_code x country x epi_score x epi_rank x proficiency_band)
- **Merge**: left join on iso2_code at country level

## Construction Steps
1. Aggregate language-level data to country x quarter: compute language shares, HHI, Shannon entropy, N_languages per cell
2. Merge EF-EPI scores on iso2_code
3. Create event-time variable relative to Q1 2023 (or Q4 2022 for robustness)
4. Create balanced panel indicator (countries present in all quarters)

## Outcomes
- **HHI**: sum of squared language shares within country-quarter (normalized)
- **Shannon entropy**: -sum(share * log(share)) within country-quarter
- **N_languages**: count of distinct languages per country-quarter (composition check)

## Required Robustness Checks
1. Placebo timing tests: fake treatment at Q1 2021, Q1 2022, Q1 2024
2. Alternative treatment timing: Q4 2022, Q1 2023, Q2 2023
3. Country-specific linear time trends
4. Balanced panel only
5. Winsorized outcomes (1st/99th percentile)
6. Minimum language threshold (drop countries with < 3 languages)
7. Normalized vs raw HHI
8. Composition-adjusted HHI (balanced language set)
9. Wild cluster bootstrap for inference
10. Confounding AI tools: restrict post-period to Q1 2023 only (before GPT-4/Bard)

## Scripts
- `00_clean.py`: Load, clean, construct panel, missingness audit
- `01_main.py`: Main event study, heterogeneity analysis, pre-trend tests
- `02_robustness.py`: All robustness checks and placebos
- `03_output.py`: Publication-quality figures and tables
