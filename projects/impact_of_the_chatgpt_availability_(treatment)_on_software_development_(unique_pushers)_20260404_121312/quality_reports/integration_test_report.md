# Stage 7 — Integration Test Report

Date: 2026-04-04T14:24:46.274774

## Gate: FAILED
Aggregate: 86.8/85

## Component Scores
- identification: 84/100
- code: 89/100
- paper: 97/100
- polish: 63.5/100
- replication: 100/100

## Replication
- Scripts ran: Yes
- Outputs reproducible: Yes

## Code Validation
=== AUTOMATED VALIDATION RESULTS ===
HARD checks: 12/12 passed  | SOFT checks: 6/10 passed
  [HARD] [PASS] script_exists:00_clean.py: 00_clean.py found
  [HARD] [PASS] script_exists:01_main.py: 01_main.py found
  [HARD] [PASS] script_exists:02_robustness.py: 02_robustness.py found
  [HARD] [PASS] script_exists:03_output.py: 03_output.py found
  [HARD] [PASS] script_ran:00_clean.py: ran OK
  [HARD] [PASS] script_ran:01_main.py: ran OK
  [HARD] [PASS] script_ran:02_robustness.py: ran OK
  [HARD] [PASS] script_ran:03_output.py: ran OK
  [HARD] [PASS] clean_data_exists: Found 8 data file(s) in data/clean/
  [HARD] [PASS] tables_exist: Found 4 .tex table(s), inline tables in main.tex, 1 summary file(s)
  [SOFT] [PASS] figures_exist: Found 4 figure(s): fig1_raw_trends.pdf, fig2_event_study.pdf, fig3_synthetic_control_italy.pdf, fig4_permutation_test.pdf
  [HARD] [PASS] results_summary_exists: Found at C:\Users\jesus\Desktop\papers-HQ-\projects\impact_of_the_chatgpt_availability_(treatment)_on_software_development_(unique_pushers)_20260404_121312\data\clean\results_summary.md
  [HARD] [PASS] outputs_non_empty: All 17 output files are non-empty
  [SOFT] [PASS] results_summary_has_numbers: Found 35 numeric values
  [SOFT] [FAIL] seed_set:00_clean.py: No random seed set
  [SOFT] [PASS] se_clustering:01_main.py: Clustering pattern found
  [SOFT] [PASS] se_clustering:02_robustness.py: Clustering pattern found
  [SOFT] [PASS] stats_library_imported: Statistical library imported
  [SOFT] [PASS] pretrend_test: Pre-trend or placebo test found
  [SOFT] [FAIL] wild_cluster_bootstrap: No wild cluster bootstrap detected — recommended for <50 clusters
  [SOFT] [FAIL] referee_checklist_coverage: Referee checklist: 21/53 MUST requirements detected in code (40%)
  [SOFT] [FAIL] referee_checklist_missing: Possibly unimplemented: [DOMAIN] estimation: Italy synthetic control: implement Abadie (2010) SCM via cv; [DOMAIN] estimation: Synthetic DiD (Arkhangelsky et al. 2021) as the primary est; [DOMAIN] estimation: For China/Russia: separate Abadie SCM for each country indi; [DOMAIN] estimation: For Russia: include a separate treatment indicator for the ; [DOMAIN] robustness: Placebo treatment dates: for Italy SCM, shift ban date by ± ... and 27 more

## Paper Validation
=== AUTOMATED VALIDATION RESULTS ===
HARD checks: 4/4 passed  | SOFT checks: 4/5 passed
  [HARD] [PASS] main_tex_exists: main.tex found
  [HARD] [PASS] all_sections_exist: All 8 sections found
  [HARD] [PASS] references_bib_exists: references.bib has 15 entries
  [SOFT] [PASS] citation_keys_matched: All 8 citation keys found in .bib
  [SOFT] [PASS] table_references_valid: No \input{tables/...} references found
  [HARD] [PASS] figure_references_valid: All 4 figure references resolved
  [SOFT] [PASS] latex_compiled: PDF compiled successfully
  [SOFT] [FAIL] word_count: 2693 words (outside 5000-15000 range)
  [SOFT] [PASS] numbers_consistent: 8 number(s) in abstract match results_summary: -1.386, -0.549, -0.389, 0.0, 0.006

## Integration Validation
=== AUTOMATED VALIDATION RESULTS ===
HARD checks: 7/7 passed  | SOFT checks: 11/11 passed
  [HARD] [PASS] method_alignment: Strategy specifies 'synthetic control' — code contains: synthetic, synth, donor
  [HARD] [PASS] code_tables_produced: All 4 tables from 03_output.py found on disk
  [SOFT] [PASS] results_summary_substantive: results_summary.md has 191 words
  [SOFT] [PASS] results_in_paper: 17/23 key numbers from results appear in paper (74%)
  [SOFT] [PASS] abstract_has_results: Abstract contains 8 numbers from results
  [HARD] [PASS] pdf_exists: main.pdf exists (749 KB)
  [HARD] [PASS] all_sections_present: All 8 sections found in main.tex
  [HARD] [PASS] all_citations_resolved: All 8 citations have .bib entries
  [HARD] [PASS] table_refs_valid: All 0 table references valid
  [HARD] [PASS] figure_refs_valid: All 4 figure references valid
  [SOFT] [PASS] table_has_data:table1_summary.tex: Contains numbers and tabular structure
  [SOFT] [PASS] table_has_data:table2_main_did.tex: Contains numbers and tabular structure
  [SOFT] [PASS] table_has_data:table3_event_study.tex: Contains numbers and tabular structure
  [SOFT] [PASS] table_has_data:table4_robustness.tex: Contains numbers and tabular structure
  [SOFT] [PASS] figure_non_trivial:fig1_raw_trends.pdf: 20 KB
  [SOFT] [PASS] figure_non_trivial:fig2_event_study.pdf: 19 KB
  [SOFT] [PASS] figure_non_trivial:fig3_synthetic_control_italy.pdf: 17 KB
  [SOFT] [PASS] figure_non_trivial:fig4_permutation_test.pdf: 18 KB