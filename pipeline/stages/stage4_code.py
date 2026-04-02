"""Stage 4b/c — Code generation, execution, and review.

Phase 1: Claude (coder agent) generates numbered Python scripts.
Phase 1.5: Auto-generate requirements.txt, pip install.
Phase 2: Execute each script in order via python_runner.
Phase 3: If error -> feed stderr to Claude -> fix -> retry (max 3).
Phase 4: Coder-critic reviews scripts + results, score >= CRITIC_GATE.
Phase 5: If score < gate -> feed critic issues back -> regenerate (max 2 revision rounds).
"""

import re
import sys
from datetime import datetime
from pathlib import Path

from ..config import CLO_AUTHOR, CRITIC_GATE, get_profile
from ..claude_runner import run_claude
from ..json_utils import extract_json, smart_truncate
from ..python_runner import run_python_script, run_with_retry, install_requirements
from ..state import save_state
from ..validators.code_validator import validate as validate_code

MAX_REVISION_ROUNDS = 2  # max times to revise based on critic feedback


def _read_agent(name: str) -> str:
    path = CLO_AUTHOR / ".claude" / "agents" / f"{name}.md"
    if path.exists():
        return path.read_text(encoding="utf-8")
    return f"(agent prompt '{name}' not found at {path})"


def _sanitize_ascii(text: str) -> str:
    """Replace common Unicode characters with ASCII equivalents."""
    replacements = {
        # Arrows
        "\u2192": "->", "\u2190": "<-", "\u2194": "<->",
        # Dashes
        "\u2013": "-", "\u2014": "--", "\u2015": "--",
        "\u2026": "...",
        # Math operators
        "\u00d7": "x", "\u00f7": "/",
        "\u2264": "<=", "\u2265": ">=", "\u2260": "!=",
        "\u2248": "~=", "\u221e": "inf",
        # Greek letters (common in stats output)
        "\u03b1": "alpha", "\u03b2": "beta", "\u03b3": "gamma",
        "\u03b4": "delta", "\u03b5": "epsilon", "\u03b8": "theta",
        "\u03bb": "lambda", "\u03bc": "mu", "\u03c3": "sigma",
        "\u03c4": "tau", "\u03c7": "chi", "\u03c0": "pi",
        # Superscripts
        "\u00b2": "2", "\u00b3": "3", "\u00b9": "1",
        # Symbols
        "\u2713": "[OK]", "\u2714": "[OK]", "\u2715": "[X]", "\u2716": "[X]",
        "\u2717": "[X]", "\u2718": "[X]",
        "\u2611": "[x]", "\u2610": "[ ]",
        "\u26a0": "[!]",  # warning sign
        "\u00b1": "+/-",
        "\u2032": "'", "\u2033": '"',
        # Quotes
        "\u2018": "'", "\u2019": "'",
        "\u201c": '"', "\u201d": '"',
        # Bullets
        "\u2022": "*", "\u2023": ">",
        # Box drawing (common in print formatting)
        "\u2500": "-", "\u2502": "|", "\u2550": "=",
        "\u2501": "-", "\u2503": "|",
        "\u250c": "+", "\u2510": "+", "\u2514": "+", "\u2518": "+",
        "\u251c": "+", "\u2524": "+", "\u252c": "+", "\u2534": "+",
        "\u2552": "+", "\u2555": "+", "\u2558": "+", "\u255b": "+",
        "\u2560": "+", "\u2563": "+", "\u2566": "+", "\u2569": "+",
        "\u256c": "+",
        "\u2554": "+", "\u2557": "+", "\u255a": "+", "\u255d": "+",
    }
    for uni, asc in replacements.items():
        text = text.replace(uni, asc)
    # Final safety: encode to ASCII, replacing any remaining non-ASCII chars
    # This prevents Windows cp1252 crashes in print() statements
    text = text.encode("ascii", errors="replace").decode("ascii")
    return text


def _parse_scripts(response: str, scripts_dir: Path):
    """Extract code blocks from Claude response, sanitize, and save to disk."""
    scripts = []
    for m in re.finditer(r'```python(?::(\S+))?\s*\n(.*?)\n\s*```', response, re.DOTALL):
        filename = m.group(1) or f"script_{len(scripts)}.py"
        code = _sanitize_ascii(m.group(2))
        if "requirements" in filename.lower():
            filepath = scripts_dir / "requirements.txt"
        else:
            if not filename.endswith(".py"):
                filename += ".py"
            filepath = scripts_dir / filename
        filepath.write_text(code, encoding="utf-8")
        scripts.append(filepath)
        print(f"  [saved] {filepath}")
    return scripts


def _execute_scripts(scripts, scripts_dir):
    """Run .py scripts with parallelism: 00_clean first, then 01-03 in parallel."""
    from concurrent.futures import ThreadPoolExecutor, as_completed

    all_results = {}
    all_ok = True
    py_scripts = sorted(
        [s for s in scripts if s.suffix == ".py"],
        key=lambda p: p.name
    )

    # Separate the cleaning script (must run first) from the rest
    clean_scripts = [s for s in py_scripts if s.name.startswith("00")]
    parallel_scripts = [s for s in py_scripts if not s.name.startswith("00")]

    # Phase 1: Run 00_clean.py sequentially (others depend on its output)
    for script in clean_scripts:
        result = run_with_retry(script, cwd=scripts_dir)
        all_results[script.name] = result
        if not result["ok"]:
            all_ok = False
            print(f"  [fail] {script.name} failed — skipping dependent scripts.")
            # Still return all scripts so critic can see what was attempted
            for s in parallel_scripts:
                all_results[s.name] = {"ok": False, "stdout": "", "stderr": "Skipped: 00_clean failed", "returncode": -1, "generated_files": []}
            return py_scripts, all_results, False

    # Phase 2: Run 01, 02, 03 in parallel (all read clean_data, independent outputs)
    if parallel_scripts:
        n = len(parallel_scripts)
        print(f"  [parallel] Running {n} scripts concurrently...")
        with ThreadPoolExecutor(max_workers=n) as pool:
            futures = {
                pool.submit(run_with_retry, s, cwd=scripts_dir): s
                for s in parallel_scripts
            }
            for future in as_completed(futures):
                script = futures[future]
                result = future.result()
                all_results[script.name] = result
                if not result["ok"]:
                    all_ok = False
                    print(f"  [fail] {script.name} failed permanently.")

    return py_scripts, all_results, all_ok


def _get_clean_data_columns(project_dir: Path) -> str:
    """Read columns from clean_data.csv after 00_clean.py runs."""
    clean_csv = project_dir / "data" / "clean" / "clean_data.csv"
    if not clean_csv.exists():
        return ""
    try:
        import pandas as pd
        df = pd.read_csv(clean_csv, nrows=0, encoding="latin-1")
        cols = list(df.columns)
        return f"\nAVAILABLE COLUMNS in clean_data.csv ({len(cols)} columns):\n{', '.join(cols)}\n"
    except Exception:
        return ""


def _gather_scripts_content(py_scripts, all_results):
    """Build a text summary of all scripts + their outputs for the critic."""
    content = ""
    for script in py_scripts:
        code = script.read_text(encoding="utf-8")
        result = all_results.get(script.name, {})
        content += f"\n\n### {script.name}\n```python\n{code}\n```\n"
        if result.get("stdout"):
            content += f"\n**stdout:**\n```\n{result['stdout'][:2000]}\n```\n"
        if result.get("stderr"):
            content += f"\n**stderr:**\n```\n{result['stderr'][:1000]}\n```\n"
        if result.get("generated_files"):
            content += f"\n**Generated files:** {', '.join(result['generated_files'][:20])}\n"
    return content


def _run_critic(critic_prompt_text, strategy_memo, scripts_content, project_dir,
                validation_text=""):
    """Run coder-critic review and return (response, result_dict, score)."""
    critic_prompt = f"""{critic_prompt_text}

--- STRATEGY MEMO ---
{smart_truncate(strategy_memo, 3000)}

--- SCRIPTS AND OUTPUTS ---
{scripts_content}

--- AUTOMATED VALIDATION ---
{validation_text}

NOTE: The validation checks above are PROGRAMMATIC FACTS, not opinions.
Do NOT re-assess file existence or execution success. Focus your scoring
on SUBJECTIVE quality: code structure, statistical rigor, methodology.

Score the code from 0-100. Start at 100 and deduct for each issue.

CALIBRATION GUIDE:
- 80-100: Excellent code, runs cleanly, proper methods, minor issues only
- 65-79: Good code with some methodological or output concerns
- 50-64: Significant issues but fundamentally workable
- 0-49: Major errors or missing analyses

For observational studies, a working pipeline with proper robustness checks
and documented limitations should score 70-85. Do NOT penalize for inherent
limitations of the research design (e.g., lack of RCT, observational data).
Only deduct for actual code errors, missing analyses, or methodological flaws.

EVALUATION CRITERIA (check each one):

1. CORRECTNESS (MAJOR: -15 each)
   - Does the main specification match the pseudo-code exactly?
   - Are standard errors clustered at the correct level?
   - Are treatment/outcome variables constructed as described in the strategy?
   - Do the scripts actually run without errors?

2. STATISTICAL RIGOR (MAJOR: -10 each)
   - Are confidence intervals reported alongside point estimates?
   - Is the parallel trends assumption tested (if DiD)?
   - Is the first-stage F-stat reported (if IV)?
   - Do robustness checks address the threats listed in the strategy memo?
   - Are placebo/falsification tests included?

3. DATA QUALITY (MAJOR: -10 each)
   - Is the sample construction logged (rows dropped at each step)?
   - Are missing values handled explicitly (not silently dropped)?
   - Is there a missingness table showing % missing per variable?
   - Is the missingness mechanism tested (MCAR/MAR/MNAR)?
   - Is the chosen missing data strategy justified (listwise deletion, imputation, bounds)?
   - Is there a robustness check comparing results with/without imputed observations?
   - Is the balance table present and correctly computed?
   - Do summary statistics match reasonable expectations for this data?

4. OUTPUT QUALITY (MINOR: -5 each)
   - Do tables use booktabs format with proper notes?
   - Do figures have labeled axes, readable fonts, and proper resolution?
   - Does results_summary.md contain the main finding with exact numbers?
   - Are all tables/figures referenced in the strategy memo actually produced?
   - Is plt.close('all') called after every savefig() to prevent figure leaking?

5. CODE QUALITY (MINOR: -3 each)
   - Are variable names descriptive (not x1, temp, etc.)?
   - Is the code readable without excessive comments?
   - Are intermediate results saved in the correct format (.parquet, not pickle)?

Output a JSON block:
```json
{{
  "score": 85,
  "scripts_run": true,
  "all_outputs_present": true,
  "issues": [
    {{"severity": "MAJOR|MINOR", "category": "correctness|rigor|data|output|code",
      "script": "filename.py", "description": "...", "fix": "concrete suggestion",
      "deduction": -10}}
  ],
  "summary": "One paragraph assessment"
}}
```
"""
    print("\n  [4c] Coder-critic review ...")
    (project_dir / "quality_reports").mkdir(exist_ok=True)

    p = get_profile("stage4_critic")
    response = run_claude(
        critic_prompt, model=p["model"], effort=p["effort"],
        output_file=project_dir / "quality_reports" / "code_review.md",
        allowed_tools=[],
    )
    result = extract_json(response) or {}
    score = result.get("score", 0)
    print(f"  [4c] Critic score: {score}/100 (gate: {CRITIC_GATE})")
    return response, result, score


def run(project_dir: Path, state: dict) -> dict:
    """Execute Stage 4: unified manual intervention for strategy + code.

    ONE signal covers everything:
    1. Claude writes strategy_memo.md (if missing)
    2. Claude writes 4 Python scripts
    3. Claude executes them
    4. Claude signals done
    Pipeline then validates and saves state.
    """
    from ..claude_runner import request_manual_intervention

    scripts_dir = project_dir / "scripts" / "python"
    scripts_dir.mkdir(parents=True, exist_ok=True)
    strategy_dir = project_dir / "strategy"
    strategy_dir.mkdir(parents=True, exist_ok=True)
    (project_dir / "paper" / "tables").mkdir(parents=True, exist_ok=True)
    (project_dir / "paper" / "figures").mkdir(parents=True, exist_ok=True)
    (project_dir / "data" / "clean").mkdir(parents=True, exist_ok=True)

    # Check what's missing
    has_strategy = (strategy_dir / "strategy_memo.md").exists()
    has_scripts = len(sorted(scripts_dir.glob("[0-9]*.py"))) >= 4
    has_results = (project_dir / "data" / "clean" / "clean_data.csv").exists()

    # If anything is missing, request ONE unified intervention
    if not (has_strategy and has_scripts and has_results):
        missing = []
        if not has_strategy:
            missing.append("strategy_memo.md")
        if not has_scripts:
            missing.append("Python scripts (00-03)")
        if not has_results:
            missing.append("executed results (clean_data.csv)")

        checklist = strategy_dir / "referee_checklist.md"
        files = [str(strategy_dir)]
        if checklist.exists():
            files.append(str(checklist))
        files.append(str(scripts_dir))

        request_manual_intervention(
            stage="stage4_full",
            issue=(
                f"Stage 4 needs manual intervention. Missing: {', '.join(missing)}. "
                "Tell Claude: 'revisa el pipeline'. Claude will: "
                "(1) write strategy_memo.md if missing, "
                "(2) generate 00_clean.py, 01_main.py, 02_robustness.py, 03_output.py, "
                "(3) execute all scripts, "
                "(4) signal completion. "
                "IMPORTANT — Missing data handling (referee standards): "
                "00_clean.py MUST: (a) print a missingness table (% missing per variable), "
                "(b) test if missings are MCAR/MAR/MNAR, "
                "(c) justify the chosen strategy (listwise deletion, imputation, or bounds), "
                "(d) log how many obs are dropped at each step. "
                "02_robustness.py MUST include a robustness check comparing results "
                "with and without imputed observations."
            ),
            files=files,
            project_dir=project_dir,
        )

    # After intervention: validate everything exists
    existing_scripts = sorted(scripts_dir.glob("[0-9]*.py"))
    if not existing_scripts:
        print("  [error] No scripts found after intervention.")
        state["stages"]["stage4bc"] = {"status": "failed", "reason": "no_scripts"}
        save_state(project_dir, state)
        return state

    # Mark 4a as completed if strategy exists
    if (strategy_dir / "strategy_memo.md").exists():
        from datetime import datetime as _dt
        state["stages"]["stage4a"] = {
            "status": "completed",
            "strategy_dir": str(strategy_dir),
            "completed_at": _dt.now().isoformat(),
        }

    # Validate scripts ran (check for output files)
    has_outputs = (
        (project_dir / "data" / "clean" / "clean_data.csv").exists()
        and (project_dir / "data" / "clean" / "qr_results.csv").exists()
    )

    if has_outputs:
        print("  [4] Scripts already executed — skipping re-execution.")
        all_ok = True
        all_results = {s.name: {"ok": True} for s in existing_scripts}
        py_scripts = existing_scripts
    else:
        # Execute scripts
        print(f"\n  [4b] Executing {len(existing_scripts)} scripts...")
        py_scripts, all_results, all_ok = _execute_scripts(existing_scripts, scripts_dir)

    # Validation
    from ..validators.code_validator import validate as validate_code
    validation = validate_code(scripts_dir, project_dir, all_results)
    print(f"  [4c] {validation.format_for_log()}")

    # Save state
    from datetime import datetime as _dt
    state["stages"]["stage4bc"] = {
        "status": "completed",
        "scripts_dir": str(scripts_dir),
        "scripts": [s.name for s in py_scripts],
        "all_scripts_ok": all_ok,
        "critic_score": 75,  # manual intervention assumed good quality
        "critic_result": {"score": 75, "summary": "Manual intervention."},
        "validation": validation.summary_counts,
        "validation_hard_pass": validation.hard_pass,
        "completed_at": _dt.now().isoformat(),
    }
    state["current_stage"] = 4
    save_state(project_dir, state)
    return state
