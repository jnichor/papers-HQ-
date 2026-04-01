# Stage 7 — Integration Test Report

Date: 2026-03-31T14:26:06.728417

## Gate: FAILED
Aggregate: 73.0/70

## Component Scores
- identification: 80/100
- code: 75/100
- paper: 80/100
- polish: 60.0/100
- replication: 50/100

## Replication
- Scripts ran: Yes
- Outputs reproducible: No
- Changed: paper\tables\table1_descriptive.tex, paper\tables\table2_main_did.tex

## Code Validation
=== AUTOMATED VALIDATION RESULTS ===
HARD checks: 12/12 passed  | SOFT checks: 3/6 passed
  [HARD] [PASS] script_exists:00_clean.py: 00_clean.py found
  [HARD] [PASS] script_exists:01_main.py: 01_main.py found
  [HARD] [PASS] script_exists:02_robustness.py: 02_robustness.py found
  [HARD] [PASS] script_exists:03_output.py: 03_output.py found
  [HARD] [PASS] script_ran:00_clean.py: ran OK
  [HARD] [PASS] script_ran:01_main.py: ran OK
  [HARD] [PASS] script_ran:02_robustness.py: ran OK
  [HARD] [PASS] script_ran:03_output.py: ran OK
  [HARD] [PASS] clean_data_exists: Found 16 data file(s) in data/clean/
  [HARD] [PASS] tables_exist: Found 2 table(s): table1_descriptive.tex, table2_main_did.tex
  [SOFT] [FAIL] figures_exist: No .pdf files in paper/figures/
  [HARD] [PASS] results_summary_exists: Found at C:\Users\jesus\Documents\paper-HQ-sin API\projects\empleo_en_el_peru_20260331_104334\paper\results_summary.md
  [HARD] [PASS] outputs_non_empty: All 19 output files are non-empty
  [SOFT] [PASS] results_summary_has_numbers: Found 23 numeric values
  [SOFT] [FAIL] seed_set:00_clean.py: No random seed set
  [SOFT] [PASS] se_clustering:01_main.py: Clustering pattern found
  [SOFT] [FAIL] se_clustering:02_robustness.py: No SE clustering detected — verify this is intentional
  [SOFT] [PASS] stats_library_imported: Statistical library imported

## Paper Validation
=== AUTOMATED VALIDATION RESULTS ===
HARD checks: 5/5 passed  | SOFT checks: 2/4 passed
  [HARD] [PASS] main_tex_exists: main.tex found
  [HARD] [PASS] all_sections_exist: All 8 section files found
  [HARD] [PASS] references_bib_exists: references.bib has 6 entries
  [SOFT] [PASS] citation_keys_matched: All 5 citation keys found in .bib
  [HARD] [PASS] table_references_valid: All 1 table references resolved
  [HARD] [PASS] figure_references_valid: All 3 figure references resolved
  [SOFT] [PASS] latex_compiled: PDF compiled successfully
  [SOFT] [FAIL] word_count: 2113 words (outside 5000-15000 range)
  [SOFT] [FAIL] numbers_consistent: No numeric overlap between abstract (5 numbers) and results_summary (9 numbers)

## Integration Validation
=== AUTOMATED VALIDATION RESULTS ===
HARD checks: 7/7 passed  | SOFT checks: 4/6 passed
  [HARD] [PASS] method_alignment: Strategy specifies 'event study' — code contains: event_study, event study
  [SOFT] [PASS] clustering_alignment: Strategy clusters at 'occupation' — found in code
  [HARD] [PASS] code_tables_produced: All 2 tables from 03_output.py found on disk
  [SOFT] [PASS] results_summary_substantive: results_summary.md has 89 words
  [SOFT] [FAIL] results_in_paper: 0/9 key numbers from results appear in paper (0%)
  [SOFT] [FAIL] abstract_has_results: Abstract contains NO numbers from results_summary — main finding may be missing or fabricated
  [HARD] [PASS] pdf_exists: main.pdf exists (819 KB)
  [HARD] [PASS] all_sections_present: All 8 sections found
  [HARD] [PASS] all_citations_resolved: All 5 citations have .bib entries
  [HARD] [PASS] table_refs_valid: All 1 table references valid
  [HARD] [PASS] figure_refs_valid: All 3 figure references valid
  [SOFT] [PASS] table_has_data:table1_descriptive.tex: Contains numbers and tabular structure
  [SOFT] [PASS] table_has_data:table2_main_did.tex: Contains numbers and tabular structure