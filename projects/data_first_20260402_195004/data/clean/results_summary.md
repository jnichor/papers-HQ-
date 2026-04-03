# Results Summary

## Main Treatment Effects

- **Raw difference in means**: coef = -0.0700, SE = 0.0743, p = 0.3459 95% CI [-0.2155, 0.0755]
- **OLS with baseline controls**: coef = -0.0768, SE = 0.0730, p = 0.2926 95% CI [-0.2200, 0.0663]
- **Double LASSO**: coef = -0.0781, SE = 0.0711, p = 0.2720 95% CI [-0.2175, 0.0613]

Cohen's d = -0.0684

Permutation test p-value = 0.3670

## CATE by Pro-Israel Quintile

- Q1: CATE = 0.1596, p = 0.3166, p(BH) = 1.0000
- Q2: CATE = -0.0818, p = 0.5865, p(BH) = 1.0000
- Q3: CATE = -0.2584, p = 0.2246, p(BH) = 1.0000
- Q4: CATE = -0.1418, p = 0.4055, p(BH) = 1.0000
- Q5: CATE = -0.0633, p = 0.6651, p(BH) = 1.0000

## Robustness

- Ordered probit: -0.0724, p = 0.3564
- Logit (binary outcome): -0.0492, p = 0.7516
- Logit marginal effect: -0.0107, p = 0.7516
- CATE hawkish Q1: -0.1156, p = 0.4393
- CATE hawkish Q2: -0.3103, p = 0.0309
- CATE hawkish Q3: -0.1373, p = 0.4317
- CATE hawkish Q4: 0.1367, p = 0.3857
- CATE hawkish Q5: 0.2794, p = 0.1953
- CATE hostile_sexism T1: -0.0694, p = 0.5583
- CATE hostile_sexism T2: -0.1305, p = 0.2352
- CATE hostile_sexism T3: -0.0114, p = 0.9447
- Lee bounds: [-0.1180, -0.0533]
- Sensitivity: no controls: -0.0700, p = 0.3459
- Sensitivity: baseline controls: -0.0768, p = 0.2926
- Sensitivity: full controls: -0.0765, p = 0.2820
