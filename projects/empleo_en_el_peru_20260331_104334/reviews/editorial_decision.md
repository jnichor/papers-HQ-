```json
{
  "avg_referee_score": 69.0,
  "must_address": [
    "Standard errors are misspecified: treatment is assigned at the 2-digit ISCO-08 level (~43 clusters), so HC1 SEs ignore within-occupation residual correlation (Moulton problem), likely understating SEs by a factor of 2–3. Must re-estimate with occupation-level clustered SEs and wild cluster bootstrap; all p<0.001 significance claims must be re-verified under the corrected SEs.",
    "The 'permanent scarring' interpretation is unsupported by the evidence as presented. The rotating panel design makes most cross-year comparisons cross-cohort rather than within-individual. The within-estimator attenuation (0.103 → 0.081) is inconsistent with permanence and is not reconciled in the text. Authors must either weaken the causal language or provide a model-based reconciliation of the within-estimator result.",
    "The 2020 baseline is partially treated (fieldwork straddles the March lockdown), which attenuates DiD estimates by an unquantified amount. Authors must either (a) use pre-lockdown subwave interviews to construct a cleaner pre-period or (b) formally bound the attenuation and discuss its direction. The current treatment is insufficient.",
    "Extreme survey weights (max/median ratio = 3,394×) are flagged in the data audit but unaddressed in the paper. WLS estimates may be dominated by a handful of high-weight observations. Winsorized-weight robustness checks are required and must be reported.",
    "Binary treatment classification (75.7% treated, 24.3% control) risks violating overlap assumptions and compounds baseline imbalance concerns (44% vs. 12% rural; 42% vs. 61% female). The continuous teleworkability score must become the primary specification; binary treatment should be relegated to a robustness check.",
    "The divergence between the social security formality definition (γ₂₀₂₁ = 0.089) and the written-contract definition (~0.002) — a 45× difference — is dispatched in one sentence. This is a substantive finding about the mechanism of deformalization, not a robustness failure. A joint worker-level analysis of whether the two margins move independently or jointly is necessary before any scarring claim can be sustained."
  ],
  "should_address": [
    "Provide parallel trends supporting evidence using ENAHO 2017–2019 cross-sections. While a strict panel pre-trend test is not possible, cross-sectional trends by teleworkability tercile would materially strengthen the identification narrative.",
    "The large observable baseline differences between treatment and control groups (rural share, female share) require a more substantive defense of the parallel trends assumption beyond the current Wald test, which is silent on aggregate confounds.",
    "Quantify the direction and plausible magnitude of the attenuation bias introduced by the partially treated 2020 baseline, even informally, so readers can assess how much the reported DiD estimates understate the true effect."
  ],
  "may_address": [
    "Clarify whether the Wald test for equality of industry-level effects is being used as a falsification test or a heterogeneity test — the framing in the text conflates the two.",
    "Consider reporting effect sizes in standardized units or alongside pre-pandemic means to aid economic interpretation across the two formality definitions."
  ],
  "fatal_issues": []
}
```