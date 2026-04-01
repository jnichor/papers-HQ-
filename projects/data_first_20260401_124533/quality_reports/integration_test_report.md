# Stage 7 — Integration Test Report

Date: 2026-04-01T13:51:55.912075

## Gate: FAILED
Aggregate: 78.4/70

## Component Scores
- identification: 80/100
- code: 75/100
- paper: 80/100
- polish: 62.5/100
- replication: 100/100

## Replication
- Scripts ran: Yes
- Outputs reproducible: Yes

## Code Validation
=== AUTOMATED VALIDATION RESULTS ===
HARD checks: 12/12 passed  | SOFT checks: 5/8 passed
  [HARD] [PASS] script_exists:00_clean.py: 00_clean.py found
  [HARD] [PASS] script_exists:01_main.py: 01_main.py found
  [HARD] [PASS] script_exists:02_robustness.py: 02_robustness.py found
  [HARD] [PASS] script_exists:03_output.py: 03_output.py found
  [HARD] [PASS] script_ran:00_clean.py: ran OK
  [HARD] [PASS] script_ran:01_main.py: ran OK
  [HARD] [PASS] script_ran:02_robustness.py: ran OK
  [HARD] [PASS] script_ran:03_output.py: ran OK
  [HARD] [PASS] clean_data_exists: Found 7 data file(s) in data/clean/
  [HARD] [PASS] tables_exist: Found 3 table(s): tab1_main_results.tex, tab2_symmetry.tex, tab3_summary.tex
  [SOFT] [PASS] figures_exist: Found 2 figure(s): fig1_asymmetric_event_study.pdf, fig2_symmetry_test.pdf
  [HARD] [PASS] results_summary_exists: Found at C:\Users\jesus\Documents\paper-HQ-sin API\projects\data_first_20260401_124533\data\clean\results_summary.md
  [HARD] [PASS] outputs_non_empty: All 13 output files are non-empty
  [SOFT] [PASS] results_summary_has_numbers: Found 25 numeric values
  [SOFT] [PASS] seed_set:00_clean.py: Random seed found
  [SOFT] [FAIL] se_clustering:01_main.py: No SE clustering detected — verify this is intentional
  [SOFT] [FAIL] se_clustering:02_robustness.py: No SE clustering detected — verify this is intentional
  [SOFT] [PASS] stats_library_imported: Statistical library imported
  [SOFT] [PASS] pretrend_test: Pre-trend or placebo test found
  [SOFT] [FAIL] wild_cluster_bootstrap: No wild cluster bootstrap detected — recommended for <50 clusters

## Paper Validation
=== AUTOMATED VALIDATION RESULTS ===
HARD checks: 4/5 passed  | SOFT checks: 2/4 passed

** HARD FAILURES (must be fixed before approval): **
  [HARD] [PASS] main_tex_exists: main.tex found
  [HARD] [FAIL] all_sections_exist: 7 section(s) MISSING: 01_introduction.tex, 02_literature.tex, 03_data.tex, 04_empirical_strategy.tex, 05_results.tex, 06_robustness.tex, 07_conclusion.tex
  [HARD] [PASS] references_bib_exists: references.bib has 13 entries
  [SOFT] [PASS] citation_keys_matched: All 11 citation keys found in .bib
  [HARD] [PASS] table_references_valid: All 3 table references resolved
  [HARD] [PASS] figure_references_valid: All 2 figure references resolved
  [SOFT] [PASS] latex_compiled: PDF compiled successfully
  [SOFT] [FAIL] word_count: 0 words (outside 5000-15000 range)
  [SOFT] [FAIL] numbers_consistent: No numeric overlap between abstract (6 numbers) and results_summary (23 numbers)

## Integration Validation
=== AUTOMATED VALIDATION RESULTS ===
HARD checks: 6/7 passed  | SOFT checks: 7/9 passed

** HARD FAILURES (must be fixed before approval): **
  [HARD] [PASS] method_alignment: Strategy specifies 'event study' — code contains: event_study, event study
  [SOFT] [PASS] clustering_alignment: Strategy clusters at 'country' — found in code
  [HARD] [PASS] code_tables_produced: All 0 tables from 03_output.py found on disk
  [SOFT] [PASS] results_summary_substantive: results_summary.md has 64 words
  [SOFT] [FAIL] results_in_paper: 0/23 key numbers from results appear in paper (0%)
  [SOFT] [FAIL] abstract_has_results: Abstract contains NO numbers from results_summary — main finding may be missing or fabricated
  [HARD] [PASS] pdf_exists: main.pdf exists (326 KB)
  [HARD] [FAIL] all_sections_present: 7 section(s) MISSING: 01_introduction.tex, 02_literature.tex, 03_data.tex, 04_empirical_strategy.tex, 05_results.tex, 06_robustness.tex, 07_conclusion.tex
  [HARD] [PASS] all_citations_resolved: All 11 citations have .bib entries
  [HARD] [PASS] table_refs_valid: All 3 table references valid
  [HARD] [PASS] figure_refs_valid: All 2 figure references valid
  [SOFT] [PASS] table_has_data:tab1_main_results.tex: Contains numbers and tabular structure
  [SOFT] [PASS] table_has_data:tab2_symmetry.tex: Contains numbers and tabular structure
  [SOFT] [PASS] table_has_data:tab3_summary.tex: Contains numbers and tabular structure
  [SOFT] [PASS] figure_non_trivial:fig1_asymmetric_event_study.pdf: 30 KB
  [SOFT] [PASS] figure_non_trivial:fig2_symmetry_test.pdf: 16 KB