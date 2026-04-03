# Stage 7 — Integration Test Report

Date: 2026-04-02T21:25:26.714515

## Gate: PASSED
Aggregate: 82.9/70

## Component Scores
- identification: 90/100
- code: 75/100
- paper: 80/100
- polish: 72.5/100
- replication: 100/100

## Replication
- Scripts ran: Yes
- Outputs reproducible: Yes

## Code Validation
=== AUTOMATED VALIDATION RESULTS ===
HARD checks: 12/12 passed  | SOFT checks: 4/8 passed
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
  [SOFT] [PASS] figures_exist: Found 4 figure(s): fig1_balance_smd.pdf, fig2_main_effects.pdf, fig3_cate_quintile.pdf, fig4_permutation.pdf
  [HARD] [PASS] results_summary_exists: Found at C:\Users\jesus\Desktop\papers-HQ-\projects\data_first_20260402_195004\data\clean\results_summary.md
  [HARD] [PASS] outputs_non_empty: All 16 output files are non-empty
  [SOFT] [PASS] results_summary_has_numbers: Found 78 numeric values
  [SOFT] [PASS] seed_set:00_clean.py: Random seed found
  [SOFT] [FAIL] se_clustering:01_main.py: No SE clustering detected — verify this is intentional
  [SOFT] [FAIL] se_clustering:02_robustness.py: No SE clustering detected — verify this is intentional
  [SOFT] [PASS] stats_library_imported: Statistical library imported
  [SOFT] [FAIL] referee_checklist_coverage: Referee checklist: 4/30 MUST requirements detected in code (13%)
  [SOFT] [FAIL] referee_checklist_missing: Possibly unimplemented: [DOMAIN] randomization_check: Produce a covariate balance table (treatment vs co; [DOMAIN] estimation: Primary OLS specification: ICC_referral_support ~ apartheid; [DOMAIN] estimation: LASSO covariate selection must use cross-validated lambda (; [DOMAIN] estimation: If ICC referral support is ordinal (Likert), report both OL; [DOMAIN] estimation: Report unadjusted (no covariates) treatment effect alongsid ... and 21 more

## Paper Validation
=== AUTOMATED VALIDATION RESULTS ===
HARD checks: 3/3 passed  | SOFT checks: 4/6 passed
  [HARD] [PASS] main_tex_exists: main.tex found
  [HARD] [PASS] all_sections_exist: All 8 sections found
  [HARD] [PASS] references_bib_exists: references.bib has 19 entries
  [SOFT] [PASS] citation_keys_matched: All 18 citation keys found in .bib
  [SOFT] [PASS] table_references_valid: No \input{tables/...} references found
  [SOFT] [PASS] figure_references_valid: No \includegraphics{figures/...} references found
  [SOFT] [PASS] latex_compiled: PDF compiled successfully
  [SOFT] [FAIL] word_count: 4722 words (outside 5000-15000 range)
  [SOFT] [FAIL] numbers_consistent: No numeric overlap between abstract (6 numbers) and results_summary (53 numbers)

## Integration Validation
=== AUTOMATED VALIDATION RESULTS ===
HARD checks: 6/6 passed  | SOFT checks: 9/11 passed
  [HARD] [PASS] code_tables_produced: All 4 tables from 03_output.py found on disk
  [SOFT] [PASS] results_summary_substantive: results_summary.md has 246 words
  [SOFT] [FAIL] results_in_paper: 0/53 key numbers from results appear in paper (0%)
  [SOFT] [FAIL] abstract_has_results: Abstract contains NO numbers from results_summary — main finding may be missing or fabricated
  [HARD] [PASS] pdf_exists: main.pdf exists (295 KB)
  [HARD] [PASS] all_sections_present: All 8 sections found in main.tex
  [HARD] [PASS] all_citations_resolved: All 18 citations have .bib entries
  [HARD] [PASS] table_refs_valid: All 0 table references valid
  [HARD] [PASS] figure_refs_valid: All 0 figure references valid
  [SOFT] [PASS] table_has_data:table1_balance.tex: Contains numbers and tabular structure
  [SOFT] [PASS] table_has_data:table2_main.tex: Contains numbers and tabular structure
  [SOFT] [PASS] table_has_data:table3_cate.tex: Contains numbers and tabular structure
  [SOFT] [PASS] table_has_data:table4_robustness.tex: Contains numbers and tabular structure
  [SOFT] [PASS] figure_non_trivial:fig1_balance_smd.pdf: 18 KB
  [SOFT] [PASS] figure_non_trivial:fig2_main_effects.pdf: 16 KB
  [SOFT] [PASS] figure_non_trivial:fig3_cate_quintile.pdf: 16 KB
  [SOFT] [PASS] figure_non_trivial:fig4_permutation.pdf: 16 KB