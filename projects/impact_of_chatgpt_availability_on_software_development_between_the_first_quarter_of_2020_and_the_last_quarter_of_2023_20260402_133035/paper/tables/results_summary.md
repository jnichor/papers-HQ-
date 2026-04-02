# Results Summary

## Table 1: Summary Statistics

| Variable | Period | Mean | SD | p10 | p50 | p90 | N |
|----------|--------|------|----|-----|-----|-----|---|
| hhi_raw | Full sample | 0.1513 | 0.1584 | 0.0572 | 0.1009 | 0.3339 | 3586 |
| hhi_norm | Full sample | 0.0747 | 0.1448 | 0.0252 | 0.0531 | 0.0806 | 3586 |
| entropy | Full sample | 2.4949 | 0.8315 | 1.0978 | 2.6949 | 3.4555 | 3586 |
| n_languages | Full sample | 45.1347 | 51.4870 | 3.0000 | 26.0000 | 118.0000 | 3586 |
| total_pushers | Full sample | 146253.9353 | 470615.6071 | 698.5000 | 17499.0000 | 308810.5000 | 3586 |
| hhi_raw | Pre-treatment | 0.1588 | 0.1750 | 0.0580 | 0.1014 | 0.3352 | 1787 |
| hhi_norm | Pre-treatment | 0.0808 | 0.1664 | 0.0278 | 0.0519 | 0.0778 | 1787 |
| entropy | Pre-treatment | 2.4545 | 0.8510 | 1.0959 | 2.6546 | 3.4247 | 1787 |
| n_languages | Pre-treatment | 41.4270 | 47.5269 | 3.0000 | 24.0000 | 107.4000 | 1787 |
| total_pushers | Pre-treatment | 122882.9530 | 384033.7014 | 666.0000 | 14236.0000 | 244893.8000 | 1787 |
| hhi_raw | Post-treatment | 0.1440 | 0.1396 | 0.0557 | 0.1006 | 0.3337 | 1799 |
| hhi_norm | Post-treatment | 0.0686 | 0.1193 | 0.0211 | 0.0545 | 0.0835 | 1799 |
| entropy | Post-treatment | 2.5351 | 0.8099 | 1.0981 | 2.7122 | 3.5038 | 1799 |
| n_languages | Post-treatment | 48.8177 | 54.9058 | 3.0000 | 27.0000 | 130.0000 | 1799 |
| total_pushers | Post-treatment | 169469.0245 | 542239.2754 | 746.6000 | 20468.0000 | 359309.6000 | 1799 |
| hhi_raw | Low EPI | 0.1521 | 0.1207 | 0.0760 | 0.1094 | 0.2776 | 1402 |
| hhi_norm | Low EPI | 0.0666 | 0.0994 | 0.0253 | 0.0590 | 0.0826 | 1402 |
| entropy | Low EPI | 2.3662 | 0.7028 | 1.3221 | 2.5779 | 3.1025 | 1402 |
| n_languages | Low EPI | 34.4551 | 40.6243 | 4.0000 | 21.5000 | 86.0000 | 1402 |
| total_pushers | Low EPI | 118499.9429 | 384305.7114 | 838.2000 | 10629.5000 | 269261.3000 | 1402 |
| hhi_raw | High EPI | 0.0892 | 0.0353 | 0.0530 | 0.0834 | 0.1325 | 1403 |
| hhi_norm | High EPI | 0.0575 | 0.0148 | 0.0409 | 0.0540 | 0.0782 | 1403 |
| entropy | High EPI | 2.9250 | 0.4749 | 2.2744 | 2.9245 | 3.5228 | 1403 |
| n_languages | High EPI | 57.1397 | 43.9520 | 13.0000 | 44.0000 | 124.0000 | 1403 |
| total_pushers | High EPI | 110054.9665 | 162093.4296 | 6131.0000 | 49840.0000 | 290856.4000 | 1403 |

## Table 2: Main Event Study Results

- **HHI**: N=3428, Countries=177, Quarters=22, Within-R2=0.0226
  - Pre-trend F-test p-value: nan
- **Entropy**: N=3428, Countries=177, Quarters=22, Within-R2=0.3403
  - Pre-trend F-test p-value: nan

## Table 4: Robustness Panel

| Specification | Outcome | ATT | SE | p-value | 95% CI | N |
|--------------|---------|-----|----|---------|---------|----|
| Baseline: hhi_norm | hhi_norm | -0.0271 | 0.0079 | 0.0006 | [-0.0426, -0.0116] | 3428 |
| Baseline: entropy | entropy | +0.2509 | 0.0205 | 0.0000 | [0.2107, 0.2910] | 3428 |
| Placebo Q1 2021: hhi_norm | hhi_norm | -0.0355 | 0.0110 | 0.0013 | [-0.0572, -0.0139] | 1629 |
| Placebo Q1 2021: entropy | entropy | +0.2118 | 0.0178 | 0.0000 | [0.1770, 0.2466] | 1629 |
| Placebo Q1 2022: hhi_norm | hhi_norm | -0.0283 | 0.0091 | 0.0019 | [-0.0460, -0.0105] | 1629 |
| Placebo Q1 2022: entropy | entropy | +0.1818 | 0.0168 | 0.0000 | [0.1489, 0.2148] | 1629 |
| Placebo Q1 2024: hhi_norm | hhi_norm | -0.0229 | 0.0065 | 0.0004 | [-0.0356, -0.0102] | 3586 |
| Placebo Q1 2024: entropy | entropy | +0.2144 | 0.0180 | 0.0000 | [0.1791, 0.2496] | 3586 |
| Alt timing Q4 2022 (launch): hhi_norm | hhi_norm | -0.0268 | 0.0078 | 0.0006 | [-0.0421, -0.0116] | 3586 |
| Alt timing Q4 2022 (launch): entropy | entropy | +0.2452 | 0.0199 | 0.0000 | [0.2062, 0.2841] | 3586 |
| Alt timing Q1 2023 (mass adoption): hhi_norm | hhi_norm | -0.0272 | 0.0074 | 0.0003 | [-0.0418, -0.0126] | 3586 |
| Alt timing Q1 2023 (mass adoption): entropy | entropy | +0.2372 | 0.0193 | 0.0000 | [0.1993, 0.2750] | 3586 |
| Alt timing Q2 2023 (API/plugins): hhi_norm | hhi_norm | -0.0270 | 0.0072 | 0.0002 | [-0.0411, -0.0129] | 3586 |
| Alt timing Q2 2023 (API/plugins): entropy | entropy | +0.2277 | 0.0186 | 0.0000 | [0.1912, 0.2642] | 3586 |
| Country trends: hhi_norm | hhi_norm | +0.0028 | 0.0112 | 0.8030 | [-0.0192, 0.0248] | 3428 |
| Country trends: entropy | entropy | -0.0279 | 0.0149 | 0.0607 | [-0.0571, 0.0012] | 3428 |
| Balanced: hhi_norm | hhi_norm | +0.0010 | 0.0027 | 0.7207 | [-0.0043, 0.0063] | 3058 |
| Balanced: entropy | entropy | +0.2130 | 0.0190 | 0.0000 | [0.1758, 0.2502] | 3058 |
| Winsorized: hhi_norm | hhi_norm_wins | -0.0271 | 0.0079 | 0.0006 | [-0.0426, -0.0116] | 3428 |
| Winsorized: entropy | entropy_wins | +0.2504 | 0.0205 | 0.0000 | [0.2102, 0.2905] | 3428 |
| Min 3 langs: hhi_norm | hhi_norm | +0.0073 | 0.0010 | 0.0000 | [0.0054, 0.0091] | 3303 |
| Min 3 langs: entropy | entropy | +0.2058 | 0.0165 | 0.0000 | [0.1734, 0.2382] | 3303 |
| Composition-adjusted: hhi_balanced_norm | hhi_balanced_norm | +0.0020 | 0.0009 | 0.0210 | [0.0003, 0.0037] | 2992 |
| Clean post Q1-2023: hhi_norm | hhi_norm | -0.0388 | 0.0123 | 0.0017 | [-0.0630, -0.0146] | 1788 |
| Clean post Q1-2023: entropy | entropy | +0.2185 | 0.0211 | 0.0000 | [0.1771, 0.2598] | 1788 |
| EPI-matched only: hhi_norm | hhi_norm | -0.0039 | 0.0039 | 0.3219 | [-0.0115, 0.0038] | 2682 |
| All countries: hhi_norm | hhi_norm | -0.0271 | 0.0079 | 0.0006 | [-0.0426, -0.0116] | 3428 |