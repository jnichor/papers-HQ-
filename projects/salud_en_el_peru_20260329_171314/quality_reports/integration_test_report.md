# Stage 7 — Integration Test Report

Date: 2026-03-30T11:37:47.392780

## Gate: FAILED
Aggregate: 60.8/70

## Component Scores
- identification: 70/100
- code: 58/100
- paper: 80/100
- polish: 54.5/100
- replication: 0/100

## Replication
- Scripts ran: No
- Outputs reproducible: Yes

## Code Validation
=== AUTOMATED VALIDATION RESULTS ===
HARD checks: 11/12 passed  | SOFT checks: 6/6 passed

** HARD FAILURES (must be fixed before approval): **
  [HARD] [PASS] script_exists:00_clean.py: 00_clean.py found
  [HARD] [PASS] script_exists:01_main.py: 01_main.py found
  [HARD] [PASS] script_exists:02_robustness.py: 02_robustness.py found
  [HARD] [PASS] script_exists:03_output.py: 03_output.py found
  [HARD] [PASS] script_ran:00_clean.py: ran OK
  [HARD] [FAIL] script_ran:01_main.py: FAILED: unknown error
  [HARD] [PASS] script_ran:02_robustness.py: ran OK
  [HARD] [PASS] script_ran:03_output.py: ran OK
  [HARD] [PASS] clean_data_exists: Found 12 data file(s) in data/clean/
  [HARD] [PASS] tables_exist: Found 5 table(s): balance_table.tex, summary_stats.tex, table2_qr_main.tex, table3_total_effect.tex, table4_robustness.tex
  [SOFT] [PASS] figures_exist: Found 7 figure(s): fig1_kde_expenditure.pdf, fig2_qte_plot.pdf, fig3_heatmap_total_effect.pdf, fig4_che_by_insurance.pdf, fig5_robustness_coefplot.pdf
  [HARD] [PASS] results_summary_exists: Found at C:\Users\jesus\Documents\paper-HQ-sin API\projects\salud_en_el_peru_20260329_171314\data\clean\results_summary.md
  [HARD] [PASS] outputs_non_empty: All 25 output files are non-empty
  [SOFT] [PASS] results_summary_has_numbers: Found 55 numeric values
  [SOFT] [PASS] seed_set:00_clean.py: Random seed found
  [SOFT] [PASS] se_clustering:01_main.py: Clustering pattern found
  [SOFT] [PASS] se_clustering:02_robustness.py: Clustering pattern found
  [SOFT] [PASS] stats_library_imported: Statistical library imported

## Paper Validation
=== AUTOMATED VALIDATION RESULTS ===
HARD checks: 5/5 passed  | SOFT checks: 4/4 passed
  [HARD] [PASS] main_tex_exists: main.tex found
  [HARD] [PASS] all_sections_exist: All 8 section files found
  [HARD] [PASS] references_bib_exists: references.bib has 28 entries
  [SOFT] [PASS] citation_keys_matched: All 27 citation keys found in .bib
  [HARD] [PASS] table_references_valid: All 5 table references resolved
  [HARD] [PASS] figure_references_valid: All 5 figure references resolved
  [SOFT] [PASS] latex_compiled: PDF compiled successfully
  [SOFT] [PASS] word_count: 5867 words
  [SOFT] [PASS] numbers_consistent: 4 number(s) in abstract match results_summary: 0.50, 0.75, 0.90, 44.1

## Integration Validation
=== AUTOMATED VALIDATION RESULTS ===
HARD checks: 7/7 passed  | SOFT checks: 16/16 passed
  [HARD] [PASS] robustness_script_exists: 02_robustness.py found
  [SOFT] [PASS] clustering_alignment: Strategy clusters at 'psu' — found in code
  [HARD] [PASS] code_tables_produced: All 0 tables from 03_output.py found on disk
  [SOFT] [PASS] results_summary_substantive: results_summary.md has 202 words
  [SOFT] [PASS] results_in_paper: 11/27 key numbers from results appear in paper (41%)
  [SOFT] [PASS] abstract_has_results: Abstract contains 4 numbers from results
  [HARD] [PASS] pdf_exists: main.pdf exists (579 KB)
  [HARD] [PASS] all_sections_present: All 8 sections found
  [HARD] [PASS] all_citations_resolved: All 27 citations have .bib entries
  [HARD] [PASS] table_refs_valid: All 5 table references valid
  [HARD] [PASS] figure_refs_valid: All 5 figure references valid
  [SOFT] [PASS] table_has_data:balance_table.tex: Contains numbers and tabular structure
  [SOFT] [PASS] table_has_data:summary_stats.tex: Contains numbers and tabular structure
  [SOFT] [PASS] table_has_data:table2_qr_main.tex: Contains numbers and tabular structure
  [SOFT] [PASS] table_has_data:table3_total_effect.tex: Contains numbers and tabular structure
  [SOFT] [PASS] table_has_data:table4_robustness.tex: Contains numbers and tabular structure
  [SOFT] [PASS] figure_non_trivial:fig1_kde_expenditure.pdf: 19 KB
  [SOFT] [PASS] figure_non_trivial:fig2_qte_plot.pdf: 17 KB
  [SOFT] [PASS] figure_non_trivial:fig3_heatmap_total_effect.pdf: 18 KB
  [SOFT] [PASS] figure_non_trivial:fig4_che_by_insurance.pdf: 14 KB
  [SOFT] [PASS] figure_non_trivial:fig5_robustness_coefplot.pdf: 20 KB
  [SOFT] [PASS] figure_non_trivial:fig6_expend_by_quintile.pdf: 16 KB
  [SOFT] [PASS] figure_non_trivial:fig7_zero_oop_rates.pdf: 17 KB