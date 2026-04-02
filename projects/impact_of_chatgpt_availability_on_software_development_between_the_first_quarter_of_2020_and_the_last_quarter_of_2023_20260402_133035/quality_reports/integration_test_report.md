# Stage 7 — Integration Test Report

Date: 2026-04-02T15:57:12.229184

## Gate: PASSED
Aggregate: 80.1/70

## Component Scores
- identification: 80/100
- code: 75/100
- paper: 80/100
- polish: 74.0/100
- replication: 100/100

## Replication
- Scripts ran: Yes
- Outputs reproducible: Yes

## Code Validation
=== AUTOMATED VALIDATION RESULTS ===
HARD checks: 12/12 passed  | SOFT checks: 7/8 passed
  [HARD] [PASS] script_exists:00_clean.py: 00_clean.py found
  [HARD] [PASS] script_exists:01_main.py: 01_main.py found
  [HARD] [PASS] script_exists:02_robustness.py: 02_robustness.py found
  [HARD] [PASS] script_exists:03_output.py: 03_output.py found
  [HARD] [PASS] script_ran:00_clean.py: ran OK
  [HARD] [PASS] script_ran:01_main.py: ran OK
  [HARD] [PASS] script_ran:02_robustness.py: ran OK
  [HARD] [PASS] script_ran:03_output.py: ran OK
  [HARD] [PASS] clean_data_exists: Found 5 data file(s) in data/clean/
  [HARD] [PASS] tables_exist: Found 0 .tex table(s), inline tables in main.tex, 1 summary file(s)
  [SOFT] [PASS] figures_exist: Found 6 figure(s): fig1_raw_trends.pdf, fig2_event_study.pdf, fig3_heterogeneity.pdf, fig4_placebo.pdf, figA1_scatter.pdf
  [HARD] [PASS] results_summary_exists: Found at C:\Users\jesus\Desktop\papers-HQ-\projects\impact_of_chatgpt_availability_on_software_development_between_the_first_quarter_of_2020_and_the_last_quarter_of_2023_20260402_133035\data\clean\results_summary.md
  [HARD] [PASS] outputs_non_empty: All 12 output files are non-empty
  [SOFT] [PASS] results_summary_has_numbers: Found 359 numeric values
  [SOFT] [FAIL] seed_set:00_clean.py: No random seed set
  [SOFT] [PASS] se_clustering:01_main.py: Clustering pattern found
  [SOFT] [PASS] se_clustering:02_robustness.py: Clustering pattern found
  [SOFT] [PASS] stats_library_imported: Statistical library imported
  [SOFT] [PASS] pretrend_test: Pre-trend or placebo test found
  [SOFT] [PASS] wild_cluster_bootstrap: Wild cluster bootstrap found

## Paper Validation
=== AUTOMATED VALIDATION RESULTS ===
HARD checks: 4/4 passed  | SOFT checks: 3/5 passed
  [HARD] [PASS] main_tex_exists: main.tex found
  [HARD] [PASS] all_sections_exist: All 8 sections found
  [HARD] [PASS] references_bib_exists: references.bib has 16 entries
  [SOFT] [PASS] citation_keys_matched: All 13 citation keys found in .bib
  [SOFT] [PASS] table_references_valid: No \input{tables/...} references found
  [HARD] [PASS] figure_references_valid: All 5 figure references resolved
  [SOFT] [PASS] latex_compiled: PDF compiled successfully
  [SOFT] [FAIL] word_count: 3695 words (outside 5000-15000 range)
  [SOFT] [FAIL] numbers_consistent: No numeric overlap between abstract (7 numbers) and results_summary (232 numbers)

## Integration Validation
=== AUTOMATED VALIDATION RESULTS ===
HARD checks: 7/7 passed  | SOFT checks: 7/9 passed
  [HARD] [PASS] method_alignment: Strategy specifies 'event study' — code contains: event_study, event study
  [HARD] [PASS] code_tables_produced: All 0 tables from 03_output.py found on disk
  [SOFT] [PASS] results_summary_substantive: results_summary.md has 1026 words
  [SOFT] [FAIL] results_in_paper: 0/232 key numbers from results appear in paper (0%)
  [SOFT] [FAIL] abstract_has_results: Abstract contains NO numbers from results_summary — main finding may be missing or fabricated
  [HARD] [PASS] pdf_exists: main.pdf exists (1297 KB)
  [HARD] [PASS] all_sections_present: All 8 sections found in main.tex
  [HARD] [PASS] all_citations_resolved: All 13 citations have .bib entries
  [HARD] [PASS] table_refs_valid: All 0 table references valid
  [HARD] [PASS] figure_refs_valid: All 5 figure references valid
  [SOFT] [PASS] figure_non_trivial:fig1_raw_trends.pdf: 33 KB
  [SOFT] [PASS] figure_non_trivial:fig2_event_study.pdf: 32 KB
  [SOFT] [PASS] figure_non_trivial:fig3_heterogeneity.pdf: 34 KB
  [SOFT] [PASS] figure_non_trivial:fig4_placebo.pdf: 17 KB
  [SOFT] [PASS] figure_non_trivial:figA1_scatter.pdf: 18 KB
  [SOFT] [PASS] figure_non_trivial:figA2_hhi_distribution.pdf: 18 KB