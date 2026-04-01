# Data Audit Report

Generated: 2026-03-30T11:53:18.532842
Sample size: 33,691 observations

## CRITICAL ISSUES (1)
These must be resolved before proceeding to paper writing.
- **[insurance_distribution]** EsSalud (EsSalud (formal sector)): 648 HH (1.9%) — expected 15-45% nationally. Possible variable miscoding or wrong ENAHO variable used.

## WARNINGS (3)
These should be acknowledged in the paper or addressed if possible.
- **[insurance_distribution]** Private (Seguro privado / EPS): 20,680 HH (61.4%) — expected 0-10% nationally. Check if variable captures a broader category than intended.
- **[cell_sizes]** 6 cells with N < 30 in quintile x insurance_cat: {'quintile': 1, 'insurance_cat': 'EsSalud'}: N=8; {'quintile': 1, 'insurance_cat': 'Other'}: N=3; {'quintile': 2, 'insurance_cat': 'EsSalud'}: N=14; {'quintile': 2, 'insurance_cat': 'Other'}: N=2; {'quintile': 3, 'insurance_cat': 'Other'}: N=1; {'quintile': 5, 'insurance_cat': 'Other'}: N=3
- **[outcome_distribution]** Zero-OOP rate = 44.1%. Standard QR is uninformative at low quantiles. Report two-part model as complementary analysis.

## Data Summary (for referee review packet)

### Insurance Distribution
- Private: 20,680 (61.4%)
- SIS: 11,189 (33.2%)
- Uninsured: 1,165 (3.5%)
- EsSalud: 648 (1.9%)
- Other: 9 (0.0%)

### Cell Sizes (quintile x insurance)
```
insurance_cat  EsSalud  Other  Private   SIS  Uninsured
quintile                                               
1                    8      3     6845   677        453
2                   14      2     5247  1521        276
3                   31      1     4110  2188        197
4                  101      0     2938  2872        128
5                  494      3     1540  3931        111
```

### OOP Share Distribution
- Mean: 0.0240
- Median: 0.0026
- Std: 0.0840
- Zero rate: 44.1%
- P75: 0.0182
- P90: 0.0554
- P99: 0.2716