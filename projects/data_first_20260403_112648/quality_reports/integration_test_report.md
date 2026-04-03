# Stage 7 — Integration Test Report

Date: 2026-04-03T14:07:00.742540

## Gate: PASSED
Aggregate: 88.5/85

## Component Scores
- identification: 86/100
- code: 87/100
- paper: 97/100
- polish: 73.5/100
- replication: 100/100

## Replication
- Scripts ran: Yes
- Outputs reproducible: Yes

## Code Validation
=== AUTOMATED VALIDATION RESULTS ===
HARD checks: 12/12 passed  | SOFT checks: 5/9 passed
  [HARD] [PASS] script_exists:00_clean.py: 00_clean.py found
  [HARD] [PASS] script_exists:01_main.py: 01_main.py found
  [HARD] [PASS] script_exists:02_robustness.py: 02_robustness.py found
  [HARD] [PASS] script_exists:03_output.py: 03_output.py found
  [HARD] [PASS] script_ran:00_clean.py: ran OK
  [HARD] [PASS] script_ran:01_main.py: ran OK
  [HARD] [PASS] script_ran:02_robustness.py: ran OK
  [HARD] [PASS] script_ran:03_output.py: ran OK
  [HARD] [PASS] clean_data_exists: Found 7 data file(s) in data/clean/
  [HARD] [PASS] tables_exist: Found 4 .tex table(s), inline tables in main.tex
  [SOFT] [PASS] figures_exist: Found 4 figure(s): fig1_arm_means.pdf, fig2_treatment_effects.pdf, fig3_time_dynamics.pdf, fig4_permutation.pdf
  [HARD] [PASS] results_summary_exists: Found at C:\Users\jesus\Desktop\papers-HQ-\projects\data_first_20260403_112648\data\clean\results_summary.md
  [HARD] [PASS] outputs_non_empty: All 16 output files are non-empty
  [SOFT] [PASS] results_summary_has_numbers: Found 14 numeric values
  [SOFT] [FAIL] seed_set:00_clean.py: No random seed set
  [SOFT] [PASS] se_robust:01_main.py: HC robust SEs found (appropriate for individual-level RCT)
  [SOFT] [PASS] se_robust:02_robustness.py: HC robust SEs found (appropriate for individual-level RCT)
  [SOFT] [PASS] stats_library_imported: Statistical library imported
  [SOFT] [FAIL] validated_package: No validated econometrics package (pyfixest/csdid/linearmodels) detected
  [SOFT] [FAIL] referee_checklist_coverage: Referee checklist: 18/31 MUST requirements detected in code (58%)
  [SOFT] [FAIL] referee_checklist_missing: Possibly unimplemented: [DOMAIN] estimation: Primary specification: OLS/LPM with the 2x2 factorial inter; [DOMAIN] estimation: ITT estimates as the headline. If compliance < 1, also repo; [DOMAIN] estimation: ANCOVA specification: include baseline value of the outcome; [DOMAIN] estimation: Wave/period fixed effects for pooled cross-sections. Verify; [DOMAIN] data_construction: With 1,420 columns, implement explicit variable sele ... and 8 more

## Paper Validation
=== AUTOMATED VALIDATION RESULTS ===
HARD checks: 4/4 passed  | SOFT checks: 4/5 passed
  [HARD] [PASS] main_tex_exists: main.tex found
  [HARD] [PASS] all_sections_exist: All 8 sections found
  [HARD] [PASS] references_bib_exists: references.bib has 42 entries
  [SOFT] [PASS] citation_keys_matched: All 24 citation keys found in .bib
  [SOFT] [PASS] table_references_valid: No \input{tables/...} references found
  [HARD] [PASS] figure_references_valid: All 4 figure references resolved
  [SOFT] [PASS] latex_compiled: PDF compiled successfully
  [SOFT] [FAIL] word_count: 4690 words (outside 5000-15000 range)
  [SOFT] [PASS] numbers_consistent: 2 number(s) in abstract match results_summary: 0.035, 0.351

## Integration Validation
=== AUTOMATED VALIDATION RESULTS ===
HARD checks: 6/6 passed  | SOFT checks: 11/11 passed
  [HARD] [PASS] code_tables_produced: All 4 tables from 03_output.py found on disk
  [SOFT] [PASS] results_summary_substantive: results_summary.md has 144 words
  [SOFT] [PASS] results_in_paper: 6/8 key numbers from results appear in paper (75%)
  [SOFT] [PASS] abstract_has_results: Abstract contains 2 numbers from results
  [HARD] [PASS] pdf_exists: main.pdf exists (349 KB)
  [HARD] [PASS] all_sections_present: All 8 sections found in main.tex
  [HARD] [PASS] all_citations_resolved: All 24 citations have .bib entries
  [HARD] [PASS] table_refs_valid: All 0 table references valid
  [HARD] [PASS] figure_refs_valid: All 4 figure references valid
  [SOFT] [PASS] table_has_data:table1_balance.tex: Contains numbers and tabular structure
  [SOFT] [PASS] table_has_data:table2_arm_means.tex: Contains numbers and tabular structure
  [SOFT] [PASS] table_has_data:table3_main.tex: Contains numbers and tabular structure
  [SOFT] [PASS] table_has_data:table4_robustness.tex: Contains numbers and tabular structure
  [SOFT] [PASS] figure_non_trivial:fig1_arm_means.pdf: 16 KB
  [SOFT] [PASS] figure_non_trivial:fig2_treatment_effects.pdf: 19 KB
  [SOFT] [PASS] figure_non_trivial:fig3_time_dynamics.pdf: 15 KB
  [SOFT] [PASS] figure_non_trivial:fig4_permutation.pdf: 15 KB