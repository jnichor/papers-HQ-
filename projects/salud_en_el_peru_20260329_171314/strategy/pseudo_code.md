# Pseudo-Code: Middle-Income Squeeze CHE Analysis

## Data Construction (00_clean.py)
```
1. Load Module 400 (110,451 individuals)
2. Load Sumaria (household consumption)
3. Create insurance indicators per person:
   - has_sis = (P4191 == '1')
   - has_essalud = (P4192 == '1')
   - uninsured = (P4198 == '1')
4. Aggregate to household level:
   - Insurance: HH has_sis if ANY member has SIS (and no EsSalud)
   - Health expenditure: sum(P41601 + P41602 + P41603) per HH, annualize × 13
   - Demographics from head (CODPERSO==1)
5. Merge with Sumaria on CONGLOME+VIVIENDA+HOGAR
6. Construct OOP share:
   - floor = max(quantile_05(GASHOG2D), 500)
   - oop_share = health_expend / clip(GASHOG2D, lower=floor)
   - oop_share = clip(0, 1)
7. Quintiles from GASHOG2D
8. CHE flags: oop_share > {0.10, 0.25, 0.40}
```

## Main Estimation (01_main.py)
```
For tau in {0.10, 0.25, 0.50, 0.75, 0.90}:
    Q_tau(oop_share | X) = alpha + beta1*has_sis + beta2*has_essalud
                         + sum_q(gamma_q * I[quintile=q])
                         + sum_q(delta1_q * has_sis * I[quintile=q])
                         + sum_q(delta2_q * has_essalud * I[quintile=q])
                         + X'theta + region_FE

    SE: cluster bootstrap at CONGLOME level, 200 reps
    Total SIS effect for quintile q: beta1 + delta1_q
    Total EsSalud effect for quintile q: beta2 + delta2_q
```

## Robustness (02_robustness.py)
```
For each check in {OLS variants, alt samples, CHE thresholds, placebo,
                    control sensitivity, QR90, alt floors}:
    Run OLS: outcome ~ has_sis + controls + region_FE
    Cluster SE at CONGLOME
    Record: (check, outcome, coef, se, pval, N)
```
