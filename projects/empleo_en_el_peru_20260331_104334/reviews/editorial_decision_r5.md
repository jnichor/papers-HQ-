```json
{
  "avg_referee_score": 60.0,
  "fatal_issues": [
    "Wild cluster bootstrap absent with 40 clusters: headline t-statistics (1.97, 2.00) fall below the t(39) 5% critical value of 2.023, rendering ** significance notation incorrect and primary inference invalid — main results may not be statistically significant under correct procedure",
    "Reactiva Perú (S/. 60bn payroll-conditioned credit program, 2020–2021) unaddressed: teleworkable-sector firms were disproportionate beneficiaries and the channel is observationally indistinguishable from the teleworkability mechanism, constituting a first-order threat to identification",
    "Pre-pandemic parallel trends test (ENAHO 2017–2019, publicly available from INEI) not implemented and deferred to future research for a third consecutive round: 32 pp rurality gap and 19 pp gender gap between groups make common trends structurally implausible without empirical validation, invalidating the DiD design"
  ],
  "must_address": [
    "Implement wild cluster bootstrap (Rademacher weights, ≥999 reps) as the primary inference method; demote conventional clustered SEs to secondary/robustness status; correct or remove ** significance stars if results do not survive",
    "Add a substantive discussion of Reactiva Perú and attempt empirical separation of the credit-access channel from the teleworkability channel (e.g., firm-size heterogeneity, sector-level Reactiva uptake data, placebo on non-teleworkable formality outcomes)",
    "Implement pre-2020 parallel trends test using ENAHO 2017–2019; if trends diverge, the DiD estimate cannot be given a causal interpretation and the paper's framing must change accordingly",
    "Revise all causal language in the conclusion and abstract to be consistent with the actual identification assumptions; remove or heavily caveat 'causal interpretation confirmed by fixed effects' pending resolution of the three fatal issues above"
  ],
  "should_address": [
    "Resolve income variable ambiguity: state explicitly whether S/. 14,495 (and all Table 1 income figures) are monthly or annual, confirm deflation status and reference year, and document the income variable construction pipeline",
    "Report distributional statistics (25th/75th percentiles) for income by group in Table 1 to make the S/. 14,495 median intelligible given 44% rural composition and concentration in agriculture and manual services"
  ],
  "may_address": [
    "Consider whether Table 1 notes should be expanded with a brief description of how contact-intensity classification was constructed, to aid replication and reduce reader confusion about group definitions"
  ]
}
```