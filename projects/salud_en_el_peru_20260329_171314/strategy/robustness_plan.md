# Robustness Plan

## (a) OLS Comparison
- Full controls + region FE (baseline)
- No region FE
- Bivariate (no controls)
- **Threat**: model specification
- **Weakens if**: sign flips with controls

## (b) Alternative Samples
- Urban only
- Rural only
- Working-age heads (25-65)
- **Threat**: sample composition drives results
- **Weakens if**: effects disappear in subsamples

## (c) Alternative CHE Thresholds
- CHE at 10% of consumption
- CHE at 25%
- CHE at 40%
- **Threat**: results sensitive to threshold choice
- **Strengthens if**: gradient pattern holds across thresholds

## (d) Placebo/Falsification
- Random treatment assignment
- EsSalud vs Uninsured (different mechanism)
- **Threat**: spurious correlation
- **Weakens if**: placebo shows significant effect

## (e) Control Sensitivity
- No controls → Demo only → Demo+HH → Demo+HH+Health → Full+RegionFE
- **Threat**: omitted variable bias
- **Weakens if**: coefficient unstable across specifications

## (f) QR Robustness at tau=0.90
- Full sample, urban only, rural only
- **Threat**: upper-tail results driven by outliers
- **Strengthens if**: pattern consistent across subsamples

## (g) Alternative Consumption Floors
- 1st percentile floor
- 10th percentile floor
- **Threat**: OOP share sensitive to denominator floor
- **Weakens if**: results change substantially with floor choice
