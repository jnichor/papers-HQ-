# Strategy Memo: The Ratchet Effect — Commodity Booms Don't Undo What Busts Destroy

## Research Question
When commodity prices recover after a bust, do civil liberties restore symmetrically, or does repression exhibit a ratchet — easily installed during crises but resistant to reversal during recoveries?

## Identification Strategy
**Method**: Asymmetric TWFE Event Study with joint symmetry test

**Treatment**: Commodity terms-of-trade (CTOT) bust episodes, defined as a cumulative decline of >= 20% in the CTOT index over a 3-year window. Recovery episodes defined as subsequent cumulative increase of >= 20%.

**Outcome variables** (from CLD dataset):
- `freexp` — Freedom of expression (0-4 scale)
- `freass` — Freedom of assembly (0-4 scale)
- `frerel` — Freedom of religion (0-4 scale)
- `fremov` — Freedom of movement (0-4 scale)
- `fairtrial` — Fair trial rights (0-4 scale)

**Unit of analysis**: Country-year panel, ~182 countries, 1975-2018

**Identification**: CTOT shocks are exogenous — driven by world commodity prices weighted by fixed export shares, not domestic policy. The asymmetric event study compares the magnitude and speed of liberty erosion during busts vs. liberty recovery during booms.

## Data Sources

| Source | File | Role | Merge Key |
|--------|------|------|-----------|
| Civil Liberty Dataset (CLD) | CLD_2.10.xlsx | Outcome variables | ID (ISO3) + YEAR |
| IMF CTOT | dataset_...CTOT...csv | Treatment (commodity shocks) | COUNTRY + year |

## Pseudo-code

### 00_clean.py
```
1. Load CLD_2.10.xlsx (9,292 rows x 11 cols)
2. Load CTOT CSV (wide format, 865 cols)
   - Filter to annual CTOT index (net export price, GDP-weighted)
   - Reshape from wide to long: country, year, ctot_index
   - Extract ISO3 from SERIES_CODE
3. Merge CLD + CTOT on ISO3 + year
4. Define bust episodes: cumulative CTOT decline >= 20% over 3 years
5. Define recovery episodes: cumulative CTOT increase >= 20% after bust
6. Create event-time variables relative to bust onset and recovery onset
7. Missingness analysis, MCAR test, log all steps
8. Save clean_data.csv
```

### 01_main.py
```
1. TWFE baseline: liberty_it = alpha_i + gamma_t + beta * bust_it + epsilon_it
   For each of the 5 civil liberties separately
2. Asymmetric event study:
   - Bust event study: coefficients at t-3 to t+5 relative to bust onset
   - Recovery event study: coefficients at t-3 to t+5 relative to recovery onset
3. Joint symmetry test: H0: bust coefficients = -recovery coefficients
   (Wald test on the difference)
4. Pre-trend F-test on pre-bust coefficients
5. Cluster SEs at country level
```

### 02_robustness.py
```
1. Alternative bust threshold: 15% and 25% (sensitivity)
2. Placebo bust dates (permutation test, 999 reps)
3. Exclude oil exporters (OPEC countries)
4. Regional heterogeneity (Africa, Asia, Latin America)
5. Missingness robustness (listwise vs interpolation)
6. Power analysis (MDE at 80%)
```

### 03_output.py
```
1. Asymmetric event study plot (bust vs recovery, side by side)
2. Main results table (5 liberties x bust + recovery coefficients)
3. Symmetry test table
4. Robustness table
5. Summary statistics table
6. plt.close('all') after every savefig()
```

## Standard Errors
- Cluster-robust at country level (~182 clusters — sufficient for asymptotic)
- Report wild cluster bootstrap as robustness check

## Key Threats
1. **Endogenous commodity dependence**: countries with weak institutions may be more commodity-dependent
   - Addressed by: country FE (absorb time-invariant confounders), pre-trend test
2. **Concurrent shocks**: busts may coincide with other crises
   - Addressed by: year FE, excluding financial crisis years as robustness
3. **Ordinal outcomes**: 0-4 scale is discrete, not continuous
   - Addressed by: ordered probit as robustness, but TWFE is standard in this literature
