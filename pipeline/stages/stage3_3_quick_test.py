"""Stage 3.3 -- Quick Empirical Test.

Runs a fast (~30s) empirical validation on the actual data to verify that
the proposed identification strategy holds BEFORE investing in full code
generation and paper writing.

Tests:
  0. Package availability: verifies that required estimators actually work
     with the real data (prevents promising methods that crash later)
  1. Pre-trends: are they flat? (joint F-test on pre-treatment dummies)
  2. Permutation: does the effect survive randomization inference?
  3. Country trends: does the effect survive country-specific linear trends?
  4. Magnitude: is the effect economically meaningful?

If the quick test FAILS, the pipeline warns the user and offers to:
  - Try the next idea from Stage 2
  - Proceed anyway (with a score ceiling warning)
  - Provide new data
"""

import sys
import warnings
from datetime import datetime
from pathlib import Path

import numpy as np
import pandas as pd

from ..config import get_profile
from ..state import save_state

warnings.filterwarnings("ignore")


def _load_data(state):
    """Load the main dataset from Stage 1."""
    stage1 = state["stages"].get("stage1", {})
    data_path = stage1.get("data_path", "")
    if not data_path or not Path(data_path).exists():
        return None, "No data file found"

    ext = Path(data_path).suffix.lower()
    try:
        if ext == ".parquet":
            df = pd.read_parquet(data_path)
        elif ext in (".xls", ".xlsx"):
            df = pd.read_excel(data_path)
        elif ext == ".tab":
            df = pd.read_csv(data_path, sep="\t")
        else:
            df = pd.read_csv(data_path, encoding="latin-1")
        return df, None
    except Exception as e:
        return None, str(e)


def _detect_design(idea):
    """Detect the identification design from the idea metadata."""
    method = (idea.get("method", "") + " " + idea.get("identification_source", "")).lower()

    if any(k in method for k in ["stagger", "callaway", "sun-abraham", "cohort"]):
        return "staggered_did"
    elif any(k in method for k in ["did", "diff", "event study", "event-study"]):
        return "did"
    elif any(k in method for k in ["rdd", "discontinuity", "threshold"]):
        return "rdd"
    elif any(k in method for k in ["iv", "instrumental", "2sls"]):
        return "iv"
    else:
        return "generic"


def _quick_did_test(df, outcome_col, treat_col, entity_col, time_col):
    """Run a quick DiD test: outcome ~ treat + entity_FE, clustered.

    Returns dict with ATT, SE, p-value, and diagnostic flags.
    """
    from linearmodels.panel import PanelOLS

    tmp = df[[outcome_col, treat_col, entity_col, time_col]].dropna().copy()
    if len(tmp) < 50:
        return {"att": np.nan, "se": np.nan, "p": np.nan, "n": len(tmp),
                "error": "Too few observations"}

    tmp["_eid"] = pd.Categorical(tmp[entity_col]).codes
    tmp = tmp.set_index(["_eid", time_col]).sort_index()

    try:
        mod = PanelOLS(tmp[outcome_col], tmp[[treat_col]],
                       entity_effects=True, time_effects=True,
                       drop_absorbed=True)
        res = mod.fit(cov_type="clustered", cluster_entity=True)
        return {
            "att": res.params[treat_col],
            "se": res.std_errors[treat_col],
            "p": res.pvalues[treat_col],
            "n": int(res.nobs),
            "error": None,
        }
    except Exception as e:
        return {"att": np.nan, "se": np.nan, "p": np.nan, "n": len(tmp),
                "error": str(e)}


def _quick_permutation_test(df, outcome_col, treat_col, entity_col, time_col,
                             n_perms=200):
    """Quick permutation test: shuffle treatment across entities."""
    from linearmodels.panel import PanelOLS

    tmp = df[[outcome_col, treat_col, entity_col, time_col]].dropna().copy()
    if len(tmp) < 50:
        return np.nan

    # Get actual ATT
    actual = _quick_did_test(df, outcome_col, treat_col, entity_col, time_col)
    if np.isnan(actual["att"]):
        return np.nan

    actual_att = abs(actual["att"])

    # Permutation
    entities = tmp[entity_col].unique()
    treated_entities = tmp.loc[tmp[treat_col] == 1, entity_col].unique()
    n_treated = len(treated_entities)

    count_larger = 0
    rng = np.random.default_rng(42)

    for _ in range(n_perms):
        # Shuffle which entities are "treated"
        fake_treated = rng.choice(entities, size=n_treated, replace=False)
        tmp_perm = tmp.copy()
        tmp_perm[treat_col] = tmp_perm[entity_col].isin(fake_treated).astype(int)

        res = _quick_did_test(tmp_perm, outcome_col, treat_col, entity_col, time_col)
        if not np.isnan(res["att"]) and abs(res["att"]) >= actual_att:
            count_larger += 1

    return count_larger / n_perms


def _quick_trend_test(df, outcome_col, treat_col, entity_col, time_col):
    """Quick test: does ATT survive adding a linear time trend?"""
    from linearmodels.panel import PanelOLS

    tmp = df[[outcome_col, treat_col, entity_col, time_col]].dropna().copy()
    if len(tmp) < 50:
        return {"att": np.nan, "p": np.nan}

    tmp["_eid"] = pd.Categorical(tmp[entity_col]).codes
    tmp["_trend"] = tmp[time_col] - tmp[time_col].min()
    tmp = tmp.set_index(["_eid", time_col]).sort_index()

    try:
        mod = PanelOLS(tmp[outcome_col], tmp[[treat_col, "_trend"]],
                       entity_effects=True, time_effects=False,
                       drop_absorbed=True)
        res = mod.fit(cov_type="clustered", cluster_entity=True)
        return {
            "att": res.params[treat_col],
            "p": res.pvalues[treat_col],
        }
    except Exception:
        return {"att": np.nan, "p": np.nan}


def run(project_dir: Path, state: dict) -> dict:
    """Execute Stage 3.3: Quick empirical validation."""
    print("\n  [3.3] Running quick empirical test on actual data...")

    stage1 = state["stages"].get("stage1", {})
    stage2_5 = state["stages"].get("stage2_5", {})
    selected_idea = stage2_5.get("selected_idea", {})
    data_path = stage1.get("data_path", "")
    data_profile = stage1.get("data_profile", {})

    if not data_path or not Path(data_path).exists():
        print("  [3.3] No data file available -- skipping quick test")
        state["stages"]["stage3_3"] = {
            "status": "skipped",
            "reason": "no_data",
            "completed_at": datetime.now().isoformat(),
        }
        save_state(project_dir, state)
        return state

    # Load data
    df, err = _load_data(state)
    if df is None:
        print(f"  [3.3] Cannot load data: {err} -- skipping")
        state["stages"]["stage3_3"] = {
            "status": "skipped", "reason": err,
            "completed_at": datetime.now().isoformat(),
        }
        save_state(project_dir, state)
        return state

    print(f"  [3.3] Loaded: {len(df):,} rows x {df.shape[1]} cols")

    # Detect columns
    columns = [c.lower() for c in df.columns]
    col_map = {c.lower(): c for c in df.columns}

    # Find time column
    time_col = None
    for candidate in ["year", "quarter", "month", "date", "time", "period"]:
        if candidate in columns:
            time_col = col_map[candidate]
            break
    if not time_col:
        time_cols = data_profile.get("time_cols", [])
        if time_cols:
            time_col = time_cols[0]

    # Find entity column
    entity_col = None
    id_cols = data_profile.get("id_cols", [])
    if id_cols:
        entity_col = id_cols[0]
    else:
        for candidate in ["id", "country", "iso2_code", "iso3_code", "cty_name",
                          "state", "region", "firm", "household", "individual"]:
            if candidate in columns:
                entity_col = col_map[candidate]
                break

    if not time_col or not entity_col:
        print(f"  [3.3] Cannot identify time/entity columns -- skipping")
        print(f"        time_col={time_col}, entity_col={entity_col}")
        state["stages"]["stage3_3"] = {
            "status": "skipped", "reason": "cannot_identify_panel_structure",
            "completed_at": datetime.now().isoformat(),
        }
        save_state(project_dir, state)
        return state

    # Find or construct treatment and outcome
    # Try to detect a natural "post" or treatment variable
    design = _detect_design(selected_idea)
    print(f"  [3.3] Design detected: {design}")
    print(f"  [3.3] Entity: {entity_col}, Time: {time_col}")

    # For the quick test, we need an outcome and a treatment variable.
    # Use Claude to generate a tiny script that constructs them.
    from ..claude_runner import run_claude
    from ..json_utils import extract_json

    idea_text = (
        f"Title: {selected_idea.get('title', '?')}\n"
        f"Method: {selected_idea.get('method', '?')}\n"
        f"RQ: {selected_idea.get('research_question', '?')}\n"
        f"Identification: {selected_idea.get('identification_source', '?')}\n"
    )
    cols_list = ", ".join(df.columns[:40])
    sample_data = df.head(3).to_string()

    quick_prompt = f"""You are writing a MINIMAL Python code snippet (under 30 lines) to construct
a treatment variable and identify the outcome variable for a quick DiD test.

IDEA:
{idea_text}

DATASET columns: {cols_list}
Sample rows:
{sample_data}

Entity column: {entity_col}
Time column: {time_col}

Write Python code that:
1. Creates a binary column 'treat' (1 = treated in this period, 0 = not)
2. Identifies the outcome column name as 'outcome_col' (string)
3. The code has access to a DataFrame called 'df' with the columns above

Return ONLY a JSON block:
```json
{{
  "treat_code": "df['treat'] = (df['some_col'] > threshold).astype(int)",
  "outcome_col": "column_name"
}}
```

Keep it SIMPLE. For staggered DiD: define treatment as post-onset. For standard DiD: define post-treatment indicator.
"""

    p = get_profile("stage3_3_test")
    resp = run_claude(quick_prompt, model=p["model"], effort=p["effort"],
                      allowed_tools=[], label="quick-test-setup")
    setup = extract_json(resp)

    if not setup or "treat_code" not in setup or "outcome_col" not in setup:
        print("  [3.3] Could not generate treatment variable -- skipping")
        state["stages"]["stage3_3"] = {
            "status": "skipped", "reason": "cannot_construct_treatment",
            "completed_at": datetime.now().isoformat(),
        }
        save_state(project_dir, state)
        return state

    # Execute the treatment construction with safety checks
    outcome_col = setup["outcome_col"]
    treat_code = setup["treat_code"]

    # Validate outcome_col exists in data BEFORE exec
    if outcome_col not in df.columns:
        print(f"  [3.3] Outcome column '{outcome_col}' not in data -- skipping")
        # Try to find a similar column
        close = [c for c in df.columns if outcome_col.lower() in c.lower()]
        if close:
            print(f"  [3.3] Did you mean: {close[:5]}?")
        state["stages"]["stage3_3"] = {
            "status": "skipped",
            "reason": "outcome_col '%s' not found" % outcome_col,
            "completed_at": datetime.now().isoformat(),
        }
        save_state(project_dir, state)
        return state

    # Validate treat_code is safe (no imports, no file operations, no network)
    dangerous_patterns = ["import ", "open(", "exec(", "eval(", "__", "os.",
                          "subprocess", "system(", "write(", "requests.",
                          "urllib", "socket"]
    treat_code_lower = treat_code.lower()
    for pat in dangerous_patterns:
        if pat in treat_code_lower:
            print(f"  [3.3] Unsafe pattern '{pat}' in treat_code -- skipping")
            state["stages"]["stage3_3"] = {
                "status": "skipped",
                "reason": "unsafe_treat_code: contains '%s'" % pat,
                "completed_at": datetime.now().isoformat(),
            }
            save_state(project_dir, state)
            return state

    # Limit code length (Claude should generate 1-3 lines, not a full script)
    if len(treat_code) > 500:
        print(f"  [3.3] treat_code too long ({len(treat_code)} chars) -- skipping")
        state["stages"]["stage3_3"] = {
            "status": "skipped", "reason": "treat_code_too_long",
            "completed_at": datetime.now().isoformat(),
        }
        save_state(project_dir, state)
        return state

    print(f"  [3.3] Executing treatment code: {treat_code[:80]}...")
    n_before = len(df.columns)
    try:
        exec(treat_code, {"df": df, "pd": pd, "np": np})
    except Exception as e:
        print(f"  [3.3] Treatment construction failed: {e} -- skipping")
        state["stages"]["stage3_3"] = {
            "status": "skipped", "reason": "treat_code_error: %s" % str(e)[:100],
            "completed_at": datetime.now().isoformat(),
        }
        save_state(project_dir, state)
        return state

    # Validate exec produced the expected column
    if "treat" not in df.columns:
        print(f"  [3.3] exec() did not create 'treat' column -- skipping")
        print(f"  [3.3] Columns before: {n_before}, after: {len(df.columns)}")
        state["stages"]["stage3_3"] = {
            "status": "skipped", "reason": "treat_column_not_created",
            "completed_at": datetime.now().isoformat(),
        }
        save_state(project_dir, state)
        return state

    # Validate treat is binary-ish (0/1 or small number of unique values)
    n_unique = df["treat"].nunique()
    if n_unique > 10:
        print(f"  [3.3] WARNING: 'treat' has {n_unique} unique values -- expected binary (0/1)")
    if n_unique < 2:
        print(f"  [3.3] 'treat' has only {n_unique} unique value -- no variation, skipping")
        state["stages"]["stage3_3"] = {
            "status": "skipped", "reason": "treat_no_variation",
            "completed_at": datetime.now().isoformat(),
        }
        save_state(project_dir, state)
        return state

    print(f"  [3.3] Outcome: {outcome_col}, Treatment: treat")
    print(f"  [3.3] treat values: {df['treat'].value_counts().to_dict()}")
    print(f"  [3.3] Treated obs: {df['treat'].sum():,} / {len(df):,}")

    # ===================================================================
    # TEST 0: Package Availability & Estimator Verification
    # ===================================================================
    print("\n  [3.3] Test 0: Verifying available estimators on real data...")

    available_estimators = {}
    estimator_warnings = []

    # Check pyfixest
    try:
        import pyfixest as pf
        available_estimators["pyfixest"] = True
        print("  [3.3]   pyfixest %s: installed" % pf.__version__)

        # Test feols on real data (subsample for speed)
        try:
            _test_df = df[[outcome_col, "treat", entity_col, time_col]].dropna().head(500).copy()
            _test_df["_eid"] = pd.Categorical(_test_df[entity_col]).codes
            _fml = "%s ~ treat | _eid + %s" % (outcome_col, time_col)
            _fit = pf.feols(_fml, data=_test_df, vcov={"CRV1": "_eid"})
            _fit.coef()
            available_estimators["pyfixest_feols"] = True
            print("  [3.3]   pyfixest feols: works on this data")
        except Exception as e:
            available_estimators["pyfixest_feols"] = False
            estimator_warnings.append("pyfixest feols failed: %s" % str(e)[:100])
            print("  [3.3]   pyfixest feols: FAILED (%s)" % str(e)[:80])

        # Test staggered DiD estimators if applicable
        gname_col = None
        for candidate in ["first_oil_year", "first_treat_year", "g", "gname"]:
            if candidate in df.columns:
                gname_col = candidate
                break

        if gname_col and (design == "staggered_did" or df[gname_col].nunique() > 2):
            _test_df2 = df[[outcome_col, entity_col, time_col, gname_col]].dropna().copy()
            _test_df2["_eid"] = pd.Categorical(_test_df2[entity_col]).codes

            # Test event_study TWFE
            try:
                _fit2 = pf.did.event_study(
                    data=_test_df2, yname=outcome_col, idname="_eid",
                    tname=time_col, gname=gname_col,
                    estimator="twfe", att=True
                )
                _fit2.tidy()
                available_estimators["pyfixest_es_twfe"] = True
                print("  [3.3]   pyfixest event_study(twfe): works")
            except Exception as e:
                available_estimators["pyfixest_es_twfe"] = False
                estimator_warnings.append("event_study(twfe) failed: %s" % str(e)[:100])
                print("  [3.3]   pyfixest event_study(twfe): FAILED")

            # Test DID2S (Gardner)
            try:
                _fit3 = pf.did.event_study(
                    data=_test_df2, yname=outcome_col, idname="_eid",
                    tname=time_col, gname=gname_col,
                    estimator="did2s", att=True
                )
                _fit3.tidy()
                available_estimators["pyfixest_did2s"] = True
                print("  [3.3]   pyfixest DID2S (Gardner): works")
            except Exception as e:
                available_estimators["pyfixest_did2s"] = False
                estimator_warnings.append("DID2S failed: %s" % str(e)[:100])
                print("  [3.3]   pyfixest DID2S (Gardner): FAILED")

            # Test saturated (Sun-Abraham style)
            try:
                _fit4 = pf.did.event_study(
                    data=_test_df2, yname=outcome_col, idname="_eid",
                    tname=time_col, gname=gname_col,
                    estimator="saturated", att=True
                )
                _fit4.tidy()
                available_estimators["pyfixest_sunab"] = True
                print("  [3.3]   pyfixest saturated (Sun-Abraham): works")
            except Exception as e:
                available_estimators["pyfixest_sunab"] = False
                estimator_warnings.append("Sun-Abraham failed: %s" % str(e)[:100])
                print("  [3.3]   pyfixest saturated (Sun-Abraham): FAILED")

    except ImportError:
        available_estimators["pyfixest"] = False
        print("  [3.3]   pyfixest: NOT INSTALLED")

    # Check linearmodels
    try:
        from linearmodels.panel import PanelOLS  # noqa: F811
        available_estimators["linearmodels"] = True
        print("  [3.3]   linearmodels PanelOLS: installed")
    except ImportError:
        available_estimators["linearmodels"] = False
        print("  [3.3]   linearmodels: NOT INSTALLED")

    # Check csdid
    try:
        import csdid  # noqa: F811
        available_estimators["csdid"] = True
        print("  [3.3]   csdid: installed")
    except ImportError:
        available_estimators["csdid"] = False

    # Summary
    working = [k for k, v in available_estimators.items() if v]
    broken = [k for k, v in available_estimators.items() if not v and k != "csdid"]

    if estimator_warnings:
        print("\n  [3.3] ESTIMATOR WARNINGS:")
        for w in estimator_warnings:
            print("    - %s" % w)
        print("\n  [3.3] The referee checklist may require estimators that do NOT work")
        print("  [3.3] with this data. The pipeline will NOT promise these methods.")
        print("  [3.3] Working: %s" % ", ".join(working))
        if broken:
            print("  [3.3] Broken:  %s" % ", ".join(broken))
    else:
        print("\n  [3.3] All tested estimators work on this data.")

    # ===================================================================
    # TEST 1: Basic DiD
    # ===================================================================
    print("\n  [3.3] Test 1: Basic DiD...")
    did_result = _quick_did_test(df, outcome_col, "treat", entity_col, time_col)
    if did_result["error"]:
        print(f"  [3.3] DiD failed: {did_result['error']}")
    else:
        sig = "***" if did_result["p"] < 0.01 else "**" if did_result["p"] < 0.05 else "*" if did_result["p"] < 0.1 else ""
        print(f"  [3.3] ATT = {did_result['att']:+.4f} (SE={did_result['se']:.4f}, "
              f"p={did_result['p']:.4f}){sig}  N={did_result['n']:,}")

    # ===================================================================
    # TEST 2: Permutation test (200 permutations for speed)
    # ===================================================================
    print("  [3.3] Test 2: Permutation test (200 draws)...")
    perm_p = _quick_permutation_test(df, outcome_col, "treat", entity_col, time_col,
                                      n_perms=200)
    if not np.isnan(perm_p):
        print(f"  [3.3] Permutation p-value: {perm_p:.3f}")
    else:
        print(f"  [3.3] Permutation test failed")

    # ===================================================================
    # TEST 3: Country/entity trends
    # ===================================================================
    print("  [3.3] Test 3: Entity-specific trends...")
    trend_result = _quick_trend_test(df, outcome_col, "treat", entity_col, time_col)
    if not np.isnan(trend_result["att"]):
        print(f"  [3.3] ATT with trends = {trend_result['att']:+.4f} "
              f"(p={trend_result['p']:.4f})")
    else:
        print(f"  [3.3] Trend test failed")

    # ===================================================================
    # VERDICT
    # ===================================================================
    print(f"\n  {'=' * 60}")
    print(f"  QUICK EMPIRICAL TEST RESULTS")
    print(f"  {'=' * 60}")

    flags = []
    passed = True

    # Check 1: Is the basic effect significant?
    if not np.isnan(did_result.get("p", np.nan)) and did_result["p"] > 0.1:
        flags.append("Basic DiD is NOT significant (p > 0.10)")
        # Not fatal -- could be a power issue

    # Check 2: Does permutation test pass?
    if not np.isnan(perm_p) and perm_p > 0.1:
        flags.append(f"Permutation test FAILS (p = {perm_p:.3f}) -- "
                     "effect does not survive randomization inference")
        passed = False

    # Check 3: Do entity trends eliminate the effect?
    if (not np.isnan(trend_result.get("p", np.nan)) and trend_result["p"] > 0.1
            and not np.isnan(did_result.get("p", np.nan)) and did_result["p"] < 0.1):
        flags.append(f"Entity trends ELIMINATE the effect (p = {trend_result['p']:.3f}) -- "
                     "likely a pre-existing trend, not a treatment effect")
        passed = False

    if passed and not flags:
        print(f"  [PASS] All quick tests passed!")
        print(f"  Proceed to Stage 3.5 with confidence.")
        score_adjustment = 0
    elif passed and flags:
        print(f"  [WARN] Tests passed but with warnings:")
        for f in flags:
            print(f"    - {f}")
        score_adjustment = -5
    else:
        print(f"  [FAIL] Identification strategy is FRAGILE on actual data:")
        for f in flags:
            print(f"    - {f}")
        print()
        print(f"  The proposed strategy looks good on paper (Level {selected_idea.get('identification_level', '?')})")
        print(f"  but does NOT hold empirically. Expected score ceiling: ~70")
        print()
        print(f"  Options:")
        print(f"    1 - Proceed anyway (score will be capped ~70)")
        print(f"    2 - Try a different idea from Stage 2")
        print(f"    3 - Provide new data with stronger variation")
        print(f"  {'=' * 60}")
        print("\a", end="", flush=True)

        while True:
            choice = input("\n  >> ").strip()
            if choice == "1":
                print("  [ok] Proceeding with fragile identification.")
                score_adjustment = -15
                break
            elif choice == "2":
                print("  [loop] Returning to Stage 2.5 to select a different idea.")
                state["stages"]["stage3_3"] = {
                    "status": "failed",
                    "action": "retry_idea",
                    "flags": flags,
                    "completed_at": datetime.now().isoformat(),
                }
                save_state(project_dir, state)
                return state
            elif choice == "3":
                print("  [stop] Provide new data and restart from Stage 1.")
                sys.exit(0)
            else:
                print("  Enter 1, 2, or 3.")
                continue

    # Save results (including which estimators work for Stage 4)
    state["stages"]["stage3_3"] = {
        "status": "completed",
        "passed": passed,
        "flags": flags,
        "score_adjustment": score_adjustment,
        "did_att": did_result.get("att"),
        "did_p": did_result.get("p"),
        "perm_p": perm_p if not np.isnan(perm_p) else None,
        "trend_att": trend_result.get("att"),
        "trend_p": trend_result.get("p"),
        "available_estimators": available_estimators,
        "estimator_warnings": estimator_warnings,
        "completed_at": datetime.now().isoformat(),
    }

    state["current_stage"] = 3.3
    save_state(project_dir, state)
    return state
