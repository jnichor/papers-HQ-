# Strategy Memo

## Title
Regulatory Wedge: ChatGPT Access Bans as a Natural Experiment for Open-Source Contribution

## Research Question
Does restricting ChatGPT access cause a measurable decline in unique GitHub pushers relative to comparable unrestricted countries?

## Identification Strategy
DiD with country + quarter FEs for China/Russia persistent blocks. Synthetic Control for Italy temporary ban. Treatment is policy-imposed ChatGPT access restriction.

### Treatment Groups
- **Persistent block**: CN, RU, IR, SY, CU — ChatGPT never available (from Q4 2022)
- **Temporary ban**: IT — banned Q2 2023 (March 31 - April 28, 2023)

### Control Group
All other countries with ChatGPT access (~170 countries)

### Main Specification
DiD: log(total_pushers + 1) ~ banned x post_chatgpt + country_FE + quarter_FE
SCM for Italy: minimize pre-treatment RMSPE using EU donor pool

## Data
- languages.csv: 161,922 rows (country x language x quarter), aggregated to country x quarter
- chatgpt_bans.csv: 6 countries with ChatGPT restrictions

## Scripts
- 00_clean.py: aggregate, merge bans, construct treatment
- 01_main.py: DiD + event study + synthetic control
- 02_robustness.py: placebos, alternative controls, leave-one-out
- 03_output.py: figures + LaTeX tables
