"""Stage 1 - Discovery.

Path A (--topic only):  Multi-agent dataset search (web + APIs + GitHub).
                        Consolidator evaluates and ranks by causal potential.
Path B (--data given):  Profile user dataset, early warning, recommend methods.
"""

import json
import sys
from datetime import datetime
from pathlib import Path
from typing import Optional

import functools
print = functools.partial(print, flush=True)  # type: ignore[assignment]

from ..config import get_profile
from ..claude_runner import run_claude
from ..json_utils import extract_json
from ..state import save_state


# ── Path A: API-based dataset searchers ───────────────────────────────────────

def _search_dataverse(topic: str, max_results: int = 5) -> list[dict]:
    """Search Harvard Dataverse for datasets related to the topic."""
    try:
        import requests
    except ImportError:
        return []

    print(f"  [dataverse] Searching for '{topic}'...")
    try:
        r = requests.get(
            "https://dataverse.harvard.edu/api/search",
            params={
                "q": topic,
                "type": "dataset",
                "per_page": max_results,
                "sort": "date",
                "order": "desc",
                "fq": 'subject_ss:"Social Sciences"',
            },
            timeout=20,
        )
        r.raise_for_status()
        items = r.json().get("data", {}).get("items", [])
        results = []
        for item in items:
            results.append({
                "name": item.get("name", ""),
                "provider": "Harvard Dataverse",
                "url": item.get("url", ""),
                "description": (item.get("description", "") or "")[:300],
                "published": item.get("published_at", "")[:10],
                "source_api": "dataverse",
            })
        print(f"  [dataverse] Found {len(results)} datasets")
        return results
    except Exception as e:
        print(f"  [dataverse] Error: {e}")
        return []


def _search_zenodo(topic: str, max_results: int = 5) -> list[dict]:
    """Search Zenodo for datasets related to the topic."""
    try:
        import requests
    except ImportError:
        return []

    print(f"  [zenodo] Searching for '{topic}'...")
    try:
        r = requests.get(
            "https://zenodo.org/api/records",
            params={
                "q": f"{topic} econometrics OR panel OR causal",
                "type": "dataset",
                "size": max_results,
                "sort": "mostrecent",
            },
            timeout=20,
        )
        r.raise_for_status()
        hits = r.json().get("hits", {}).get("hits", [])
        results = []
        for item in hits:
            meta = item.get("metadata", {})
            files = [f.get("key", "") for f in item.get("files", [])[:5]]
            results.append({
                "name": meta.get("title", ""),
                "provider": "Zenodo",
                "url": f"https://zenodo.org/records/{item.get('id', '')}",
                "doi": meta.get("doi", ""),
                "description": (meta.get("description", "") or "")[:300],
                "files": files,
                "published": meta.get("publication_date", ""),
                "source_api": "zenodo",
            })
        print(f"  [zenodo] Found {len(results)} datasets")
        return results
    except Exception as e:
        print(f"  [zenodo] Error: {e}")
        return []


def _search_github(topic: str, max_results: int = 5) -> list[dict]:
    """Search GitHub for replication packages related to the topic."""
    try:
        import requests
    except ImportError:
        return []

    print(f"  [github] Searching for '{topic}'...")
    try:
        # Build queries in English for better GitHub coverage
        # Extract key English terms from topic
        _translations = {
            "educación": "education", "salud": "health", "empleo": "employment",
            "trabajo": "labor", "pobreza": "poverty", "comercio": "trade",
            "migración": "migration", "desigualdad": "inequality",
            "agricultura": "agriculture", "clima": "climate",
            "vivienda": "housing", "criminalidad": "crime",
            "género": "gender", "desarrollo": "development",
        }
        topic_en = topic.lower()
        for es, en in _translations.items():
            topic_en = topic_en.replace(es, en)

        queries = [
            f"{topic_en} replication data",
            f"{topic_en} dataset causal",
            f"{topic} replication",
        ]
        seen_repos = set()
        results = []

        for q in queries:
            if len(results) >= max_results:
                break
            r = requests.get(
                "https://api.github.com/search/repositories",
                params={"q": q, "sort": "stars", "per_page": max_results},
                timeout=20,
            )
            r.raise_for_status()
            for item in r.json().get("items", []):
                repo_name = item.get("full_name", "")
                if repo_name in seen_repos:
                    continue
                seen_repos.add(repo_name)
                results.append({
                    "name": repo_name,
                    "provider": "GitHub",
                    "url": item.get("html_url", ""),
                    "description": (item.get("description", "") or "")[:300],
                    "stars": item.get("stargazers_count", 0),
                    "language": item.get("language", ""),
                    "updated": (item.get("updated_at", "") or "")[:10],
                    "source_api": "github",
                })

        print(f"  [github] Found {len(results)} repos")
        return results
    except Exception as e:
        print(f"  [github] Error: {e}")
        return []


# ── Path A: download dataset from repo (legacy, kept for reference) ───────────

def _download_repo_dataset(repos: list[dict], project_dir: Path) -> Optional[str]:
    """Try to download a dataset from the best GitHub repo.

    Attempts each repo in order. Returns the local path if successful, None otherwise.
    """
    try:
        import requests
    except ImportError:
        print("  [warn] requests not installed — skipping repo dataset download")
        return None

    data_dir = project_dir / "data" / "raw"
    data_dir.mkdir(parents=True, exist_ok=True)

    SUPPORTED_EXTS = {".csv", ".dta", ".xlsx", ".xls", ".parquet", ".json"}

    for repo in repos[:3]:  # Try top 3 repos
        url = repo.get("url", "")
        dataset_url = repo.get("dataset_url", "")

        # If Claude provided a direct dataset URL, use it
        if dataset_url:
            try:
                print(f"  [download] Trying direct URL: {dataset_url[:80]}...")
                resp = requests.get(dataset_url, timeout=60, allow_redirects=True)
                if resp.status_code == 200 and len(resp.content) > 1000:
                    # Guess extension from URL or content-type
                    from urllib.parse import urlparse
                    parsed = urlparse(dataset_url)
                    ext = Path(parsed.path).suffix.lower()
                    if ext not in SUPPORTED_EXTS:
                        ext = ".csv"  # default
                    local_path = data_dir / f"repo_dataset{ext}"
                    local_path.write_bytes(resp.content)
                    size_mb = len(resp.content) / (1024 * 1024)
                    print(f"  [download] Saved {local_path.name} ({size_mb:.1f} MB)")
                    return str(local_path)
            except Exception as e:
                print(f"  [download] Direct URL failed: {e}")

        # Try GitHub API to find dataset files in the repo
        if "github.com" in url:
            try:
                # Extract owner/repo from URL
                parts = url.rstrip("/").split("github.com/")[-1].split("/")
                if len(parts) >= 2:
                    owner, repo_name = parts[0], parts[1]
                    api_url = f"https://api.github.com/repos/{owner}/{repo_name}/git/trees/main?recursive=1"
                    resp = requests.get(api_url, timeout=30)
                    if resp.status_code != 200:
                        # Try 'master' branch
                        api_url = api_url.replace("/main?", "/master?")
                        resp = requests.get(api_url, timeout=30)

                    if resp.status_code == 200:
                        tree = resp.json().get("tree", [])
                        # Find data files, prefer .csv and .dta
                        data_files = []
                        for item in tree:
                            if item["type"] == "blob":
                                fpath = item["path"]
                                ext = Path(fpath).suffix.lower()
                                if ext in SUPPORTED_EXTS:
                                    # Prioritize files in data/ directories or with data-like names
                                    priority = 0
                                    fl = fpath.lower()
                                    if "data" in fl:
                                        priority += 2
                                    if ext == ".dta":
                                        priority += 1  # Stata files more likely to be analysis-ready
                                    if ext == ".csv":
                                        priority += 1
                                    data_files.append((priority, fpath, ext))

                        if data_files:
                            data_files.sort(key=lambda x: -x[0])
                            best_priority, best_path, best_ext = data_files[0]
                            raw_url = f"https://raw.githubusercontent.com/{owner}/{repo_name}/main/{best_path}"
                            print(f"  [download] Found {best_path} in {owner}/{repo_name}...")
                            resp = requests.get(raw_url, timeout=120)
                            if resp.status_code != 200:
                                raw_url = raw_url.replace("/main/", "/master/")
                                resp = requests.get(raw_url, timeout=120)

                            if resp.status_code == 200 and len(resp.content) > 500:
                                local_path = data_dir / f"repo_dataset{best_ext}"
                                local_path.write_bytes(resp.content)
                                size_mb = len(resp.content) / (1024 * 1024)
                                print(f"  [download] Saved {local_path.name} ({size_mb:.1f} MB)")
                                return str(local_path)
            except Exception as e:
                print(f"  [download] GitHub API failed for {url}: {e}")

    print("  [download] Could not download dataset from any repo")
    return None


# ── Path B: data profiling ───────────────────────────────────────────────────

def _load_dataframe(data_path: str):
    """Load a dataset into a pandas DataFrame."""
    import pandas as pd

    p = Path(data_path)
    if not p.exists():
        print(f"  [error] Dataset not found: {data_path}")
        sys.exit(1)

    ext = p.suffix.lower()
    if ext == ".csv":
        try:
            df = pd.read_csv(p, encoding="utf-8", low_memory=False)
        except UnicodeDecodeError:
            df = pd.read_csv(p, encoding="latin-1", low_memory=False)
    elif ext in (".xls", ".xlsx"):
        df = pd.read_excel(p)
    elif ext == ".dta":
        df = pd.read_stata(p)
    elif ext == ".parquet":
        df = pd.read_parquet(p)
    elif ext == ".json":
        df = pd.read_json(p)
    elif ext in (".tab", ".tsv"):
        try:
            df = pd.read_csv(p, sep="\t", encoding="utf-8", low_memory=False)
        except UnicodeDecodeError:
            df = pd.read_csv(p, sep="\t", encoding="latin-1", low_memory=False)
    else:
        raise ValueError(f"Unsupported format: {ext}. Use .csv, .xlsx, .dta, .parquet, .tab, or .json")

    return df


def _detect_wide_panel_suffixes(df) -> dict:
    """Detect wide-format panel data where time is encoded in column name suffixes.

    Common patterns:
      - variable_20, variable_21, variable_22  (2-digit year suffixes)
      - variable_2020, variable_2021           (4-digit year suffixes)
      - variable_t1, variable_t2               (wave suffixes)

    Returns dict with keys: detected (bool), year_suffixes, n_periods,
    suffix_pattern, base_variables, suffix_to_year_map.
    """
    import re
    from collections import Counter

    cols = list(df.columns)
    result = {"detected": False}

    # ── Pattern 1: 2-digit year suffixes (_20, _21, _22, etc.) ─────────
    # Match columns ending in _DD where DD is a plausible 2-digit year
    suffix_2d = re.compile(r'^(.+?)[_](\d{2})$')
    two_digit_suffixes = Counter()
    two_digit_bases = {}
    for col in cols:
        m = suffix_2d.match(col)
        if m:
            base, suffix = m.group(1), m.group(2)
            year_int = int(suffix)
            # Plausible 2-digit years: 00-30 (2000-2030) or 80-99 (1980-1999)
            if (0 <= year_int <= 30) or (80 <= year_int <= 99):
                two_digit_suffixes[suffix] += 1
                if suffix not in two_digit_bases:
                    two_digit_bases[suffix] = []
                two_digit_bases[suffix].append(base)

    # ── Pattern 2: 4-digit year suffixes (_2020, _2021, etc.) ──────────
    suffix_4d = re.compile(r'^(.+?)[_](\d{4})$')
    four_digit_suffixes = Counter()
    four_digit_bases = {}
    for col in cols:
        m = suffix_4d.match(col)
        if m:
            base, suffix = m.group(1), m.group(2)
            year_int = int(suffix)
            if 1980 <= year_int <= 2030:
                four_digit_suffixes[suffix] += 1
                if suffix not in four_digit_bases:
                    four_digit_bases[suffix] = []
                four_digit_bases[suffix].append(base)

    # ── Decide which pattern is dominant ───────────────────────────────
    # A suffix group is "real" if at least 3 different suffixes share many
    # base variable names, indicating the same variables across years
    best_pattern = None
    best_suffixes = {}
    best_bases = {}

    for label, sfx_counts, sfx_bases in [
        ("2-digit-year", two_digit_suffixes, two_digit_bases),
        ("4-digit-year", four_digit_suffixes, four_digit_bases),
    ]:
        if len(sfx_counts) < 2:
            continue
        # Check how many bases are shared across at least 2 suffixes
        all_base_sets = {s: set(bases) for s, bases in sfx_bases.items()}
        suffix_list = sorted(all_base_sets.keys())
        # Count bases that appear in 2+ suffix groups
        base_counter = Counter()
        for s in suffix_list:
            for b in all_base_sets[s]:
                base_counter[b] += 1
        shared_bases = sum(1 for b, c in base_counter.items() if c >= 2)

        # Need a meaningful number of shared bases (at least 10 or 5% of columns)
        min_shared = max(10, len(cols) * 0.02)
        if shared_bases >= min_shared:
            # This pattern is stronger than current best?
            if best_pattern is None or shared_bases > sum(1 for b, c in Counter(
                b for bases in best_bases.values() for b in bases
            ).items() if c >= 2):
                best_pattern = label
                best_suffixes = sfx_counts
                best_bases = sfx_bases

    if best_pattern is None:
        return result

    # ── Build the result ───────────────────────────────────────────────
    sorted_suffixes = sorted(best_suffixes.keys())
    n_periods = len(sorted_suffixes)

    # Map suffixes to full years
    if best_pattern == "2-digit-year":
        suffix_to_year = {}
        for s in sorted_suffixes:
            y = int(s)
            suffix_to_year[s] = 2000 + y if y <= 30 else 1900 + y
    else:
        suffix_to_year = {s: int(s) for s in sorted_suffixes}

    # Find base variables shared across ALL suffixes (core panel vars)
    all_base_sets = {s: set(bases) for s, bases in best_bases.items()}
    core_bases = set.intersection(*all_base_sets.values()) if all_base_sets else set()

    # Find columns that DON'T have any year suffix (time-invariant / IDs)
    suffixed_cols = set()
    for bases in best_bases.values():
        for b in bases:
            for s in sorted_suffixes:
                cand = f"{b}_{s}"
                if cand in df.columns:
                    suffixed_cols.add(cand)
    unsuffixed_cols = [c for c in cols if c not in suffixed_cols]

    result = {
        "detected": True,
        "pattern": best_pattern,
        "year_suffixes": sorted_suffixes,
        "year_values": [suffix_to_year[s] for s in sorted_suffixes],
        "n_periods": n_periods,
        "n_suffixed_vars_per_period": {s: best_suffixes[s] for s in sorted_suffixes},
        "n_core_base_vars": len(core_bases),
        "core_base_vars_sample": sorted(list(core_bases))[:20],
        "unsuffixed_cols": unsuffixed_cols[:30],
        "suffix_to_year": suffix_to_year,
    }
    return result


def _detect_id_and_time_columns(df) -> dict:
    """Detect likely ID columns and time columns using heuristics.

    Handles both long-format (time in a column) and wide-format (time encoded
    in column name suffixes like variable_20, variable_21).

    Returns dict with keys: id_cols, time_cols, structure, panel_details,
    wide_panel (optional).
    """
    rows = len(df)
    cols_lower = {c: c.lower() for c in df.columns}

    # ── Check for wide-format panel first ──────────────────────────────
    wide_info = _detect_wide_panel_suffixes(df)

    # ── Candidate ID columns ────────────────────────────────────────────
    # Common ID column name patterns
    id_patterns = [
        "id", "codigo", "codperso", "cod_perso", "conglome", "vivienda",
        "hogar", "nconglom", "ubigeo", "folio", "ident", "person",
        "household", "hh_id", "pid", "hhid", "indiv",
    ]
    id_candidates = []
    for col in df.columns:
        cl = cols_lower[col]
        if any(pat in cl for pat in id_patterns):
            id_candidates.append(col)

    # ── Candidate time columns ──────────────────────────────────────────
    time_patterns = [
        "año", "anio", "year", "mes", "month", "periodo", "period",
        "trimestre", "quarter", "fecha", "date", "wave", "round",
    ]
    time_candidates = []
    for col in df.columns:
        cl = cols_lower[col]
        if any(pat in cl for pat in time_patterns):
            time_candidates.append(col)

    # Also check for datetime dtype columns
    for col in df.columns:
        if str(df[col].dtype).startswith("datetime"):
            if col not in time_candidates:
                time_candidates.append(col)

    # ── If wide panel detected, filter out suffixed false positives ────
    # Columns like aÑo_20, aÑo_21 are NOT real time columns — they are
    # year-suffixed variants of the same variable
    if wide_info["detected"]:
        import re
        suffixes = wide_info["year_suffixes"]
        suffix_pattern = re.compile(r'^(.+?)[_](' + '|'.join(suffixes) + r')$')
        # Remove time candidates that are actually suffixed columns
        time_candidates_clean = []
        for col in time_candidates:
            if not suffix_pattern.match(col):
                time_candidates_clean.append(col)
        time_candidates = time_candidates_clean

        # Similarly clean ID candidates — remove suffixed versions
        id_candidates_clean = []
        for col in id_candidates:
            if not suffix_pattern.match(col):
                id_candidates_clean.append(col)
        id_candidates = id_candidates_clean

    # ── Determine data structure ────────────────────────────────────────
    structure = "cross-sectional"  # default
    panel_details = {}

    # ── Wide-format panel takes priority if detected ───────────────────
    if wide_info["detected"] and wide_info["n_periods"] >= 2:
        structure = "wide-panel"
        panel_details = {
            "format": "wide",
            "n_time_periods": wide_info["n_periods"],
            "time_values": wide_info["year_values"],
            "year_suffixes": wide_info["year_suffixes"],
            "suffix_pattern": wide_info["pattern"],
            "n_core_vars": wide_info["n_core_base_vars"],
            "core_vars_sample": wide_info["core_base_vars_sample"],
            "unsuffixed_cols": wide_info["unsuffixed_cols"],
            "vars_per_period": wide_info["n_suffixed_vars_per_period"],
            "note": (
                "Data is in WIDE format — each time period's variables have a year suffix "
                f"(e.g., {wide_info['core_base_vars_sample'][0]}_{wide_info['year_suffixes'][0]}, "
                f"{wide_info['core_base_vars_sample'][0]}_{wide_info['year_suffixes'][-1]}). "
                "Must reshape to long format for panel econometrics."
            ) if wide_info["core_base_vars_sample"] else "Wide-format panel detected.",
        }
        # Also try long-format detection as secondary info
        if id_candidates and time_candidates:
            panel_details["long_format_id_candidates"] = id_candidates[:5]
            panel_details["long_format_time_candidates"] = time_candidates[:5]

    elif id_candidates and time_candidates:
        # Standard long-format detection
        best_id = id_candidates[0]
        best_time = time_candidates[0]

        n_unique_ids = df[best_id].nunique()
        n_unique_times = df[best_time].nunique()

        # Panel = same IDs appear across multiple time periods
        # Key test: group by ID, count distinct time values per ID
        if n_unique_times >= 2:
            times_per_id = df.groupby(best_id)[best_time].nunique()
            ids_with_multiple_times = (times_per_id > 1).sum()
            pct_panel = ids_with_multiple_times / n_unique_ids * 100

            if pct_panel >= 30:
                structure = "panel"
                panel_details = {
                    "format": "long",
                    "id_column": best_id,
                    "time_column": best_time,
                    "n_unique_ids": int(n_unique_ids),
                    "n_time_periods": int(n_unique_times),
                    "time_values": sorted(df[best_time].dropna().unique().tolist())[:20],
                    "pct_ids_multiple_periods": round(pct_panel, 1),
                    "avg_obs_per_id": round(rows / n_unique_ids, 1),
                }
            else:
                structure = "pooled-cross-sections"
                panel_details = {
                    "format": "long",
                    "id_column": best_id,
                    "time_column": best_time,
                    "n_unique_ids": int(n_unique_ids),
                    "n_time_periods": int(n_unique_times),
                    "time_values": sorted(df[best_time].dropna().unique().tolist())[:20],
                    "pct_ids_multiple_periods": round(pct_panel, 1),
                    "note": "Different individuals sampled each period — NOT panel tracking",
                }
        elif n_unique_times == 1:
            structure = "cross-sectional"
            panel_details = {
                "time_column": best_time,
                "single_period": str(df[best_time].iloc[0]),
            }
    elif time_candidates and not id_candidates:
        best_time = time_candidates[0]
        n_unique_times = df[best_time].nunique()
        if n_unique_times >= 2:
            structure = "repeated-cross-sections"
            panel_details = {
                "time_column": best_time,
                "n_time_periods": int(n_unique_times),
                "time_values": sorted(df[best_time].dropna().unique().tolist())[:20],
                "note": "Multiple time periods but no individual ID for tracking",
            }

    return {
        "id_cols": id_candidates,
        "time_cols": time_candidates,
        "structure": structure,
        "panel_details": panel_details,
        "wide_panel": wide_info if wide_info["detected"] else None,
    }


def _generate_data_summary(df) -> str:
    """Generate a compact, structured summary of the dataset for Claude.

    Groups variables by prefix to keep the summary under ~3K chars even for
    datasets with 1000+ columns (e.g., ENAHO with 1425 variables).
    """
    import re
    rows, cols = df.shape

    lines = [
        f"Rows: {rows:,}",
        f"Columns: {cols}",
        f"Numeric: {len(df.select_dtypes(include='number').columns)} | "
        f"Categorical: {len(df.select_dtypes(include='object').columns)} | "
        f"Datetime: {len(df.select_dtypes(include='datetime').columns)}",
    ]

    # ── Group variables by prefix ─────────────────────────────────────
    # Extract prefix: letters before digits (P500 -> P5, UBIGEO -> UBIGEO)
    prefix_groups = {}
    for col in df.columns:
        match = re.match(r'^([A-Za-z]+\d{0,2})', col)
        prefix = match.group(1) if match else col[:6]
        if prefix not in prefix_groups:
            prefix_groups[prefix] = []
        prefix_groups[prefix].append(col)

    # Sort by prefix, merge small groups
    lines.append("\n## Variable Groups (by prefix)")
    sorted_prefixes = sorted(prefix_groups.keys())
    for prefix in sorted_prefixes:
        group_cols = prefix_groups[prefix]
        n_vars = len(group_cols)
        if n_vars == 1:
            # Single variable — show inline stats
            col = group_cols[0]
            nuniq = df[col].nunique()
            miss_pct = df[col].isnull().mean() * 100
            if df[col].dtype in ("float64", "int64", "float32", "int32"):
                lines.append(
                    f"  {col}: numeric, {nuniq} unique, "
                    f"mean={df[col].mean():.2f}, miss={miss_pct:.0f}%"
                )
            else:
                vals = df[col].dropna().unique().tolist()[:5]
                lines.append(
                    f"  {col}: {nuniq} unique vals, miss={miss_pct:.0f}% — {vals}"
                )
        else:
            # Group of variables — show summary
            col_range = f"{group_cols[0]}..{group_cols[-1]}" if n_vars > 2 else ", ".join(group_cols)
            avg_miss = df[group_cols].isnull().mean().mean() * 100
            n_numeric = sum(1 for c in group_cols if df[c].dtype in ("float64", "int64", "float32", "int32"))
            lines.append(
                f"  {prefix}* ({n_vars} vars): {col_range} | "
                f"{n_numeric} numeric, {n_vars - n_numeric} categorical | "
                f"avg miss={avg_miss:.0f}%"
            )

    # ── Key variables: show detailed stats for top 20 most relevant ───
    # Heuristic: low missingness + high variance = more useful
    lines.append("\n## Key Variables (detailed stats, top 20)")
    numeric_cols = df.select_dtypes(include="number").columns
    if len(numeric_cols) > 0:
        # Score by: low missingness + moderate-to-high unique count
        col_scores = {}
        for col in numeric_cols:
            miss = df[col].isnull().mean()
            nuniq = df[col].nunique()
            # Prefer columns with low missingness and decent variation
            col_scores[col] = (1 - miss) * min(nuniq / 20, 1.0)
        top_cols = sorted(col_scores, key=col_scores.get, reverse=True)[:20]

        for col in top_cols:
            s = df[col]
            miss_pct = s.isnull().mean() * 100
            lines.append(
                f"  {col}: mean={s.mean():.2f}, median={s.median():.2f}, "
                f"std={s.std():.2f}, min={s.min()}, max={s.max()}, "
                f"unique={s.nunique()}, miss={miss_pct:.0f}%"
            )

    # ── Categorical variables with few unique values ──────────────────
    cat_cols = df.select_dtypes(include="object").columns
    useful_cats = [(c, df[c].nunique()) for c in cat_cols if df[c].nunique() <= 20]
    if useful_cats:
        lines.append("\n## Categorical Variables (<=20 unique)")
        for col, nuniq in sorted(useful_cats, key=lambda x: x[1])[:15]:
            vals = df[col].dropna().unique().tolist()[:10]
            lines.append(f"  {col}: {nuniq} unique — {vals}")

    # ── High missingness warning ──────────────────────────────────────
    miss = df.isnull().mean()
    high_miss = miss[miss > 0.5].sort_values(ascending=False)
    if len(high_miss) > 0:
        lines.append(f"\n## High Missingness (>50%): {len(high_miss)} variables")
        for col, pct in high_miss.head(5).items():
            lines.append(f"  {col}: {pct:.0%} missing")

    return "\n".join(lines)


def _profile_dataset(data_path: str) -> dict:
    """Run deep profiling on the user's dataset.

    Returns keys: rows, cols, columns, dtypes, missing_pct, structure,
    panel_details, data_summary, sample_rows.
    """
    try:
        import pandas as pd
    except ImportError:
        print("  [error] pandas is required for Path B. Run: pip install pandas")
        sys.exit(1)

    df = _load_dataframe(data_path)
    rows, cols = df.shape
    missing = df.isnull().mean().to_dict()

    # Deep structure detection
    structure_info = _detect_id_and_time_columns(df)
    data_summary = _generate_data_summary(df)

    print(f"  [data] Structure detected: {structure_info['structure']}")
    if structure_info["id_cols"]:
        print(f"  [data] ID columns: {', '.join(structure_info['id_cols'][:5])}")
    if structure_info["time_cols"]:
        print(f"  [data] Time columns: {', '.join(structure_info['time_cols'][:5])}")
    if structure_info.get("wide_panel"):
        wp = structure_info["wide_panel"]
        print(f"  [data] Wide-format panel detected: {wp['n_periods']} periods")
        print(f"  [data] Year suffixes: {', '.join(wp['year_suffixes'])}")
        print(f"  [data] Years: {wp['year_values']}")
        print(f"  [data] Core variables across periods: {wp['n_core_base_vars']}")
        if wp["core_base_vars_sample"]:
            sample = ', '.join(wp['core_base_vars_sample'][:10])
            print(f"  [data] Sample base vars: {sample}")
    elif structure_info["panel_details"]:
        pd_info = structure_info["panel_details"]
        if "pct_ids_multiple_periods" in pd_info:
            print(f"  [data] IDs in multiple periods: {pd_info['pct_ids_multiple_periods']}%")
        if "n_time_periods" in pd_info:
            print(f"  [data] Time periods: {pd_info['n_time_periods']}")

    profile = {
        "rows": rows,
        "cols": cols,
        "columns": list(df.columns),
        "dtypes": {c: str(df[c].dtype) for c in df.columns},
        "missing_pct": {c: round(v * 100, 1) for c, v in missing.items()},
        "structure": structure_info["structure"],
        "panel_flag": structure_info["structure"] in ("panel", "wide-panel"),
        "panel_details": structure_info["panel_details"],
        "id_cols": structure_info["id_cols"],
        "time_cols": structure_info["time_cols"],
        "wide_panel": structure_info.get("wide_panel"),
        "data_summary": data_summary,
        "sample_rows": df.head(5).to_string(),
    }

    return profile


def _early_warning(profile: dict) -> list[str]:
    """Check if the dataset is likely inadequate.  Returns a list of warnings."""
    warnings = []
    if profile["rows"] < 100:
        warnings.append(f"Very small sample: {profile['rows']} rows (< 100). Econometric power may be insufficient.")
    if profile["cols"] < 5:
        warnings.append(f"Very few variables: {profile['cols']} columns (< 5). Limited scope for controls / heterogeneity.")
    high_miss = [c for c, v in profile["missing_pct"].items() if v > 50]
    if high_miss:
        warnings.append(f"High missingness (>50%): {', '.join(high_miss[:5])}")
    return warnings


def _causal_design_warning(profile: dict) -> None:
    """Detect limitations in the data structure that will cap the paper's score.

    Prints warnings about missing pre-treatment data, limited time dimension,
    or cross-sectional design — BEFORE the user invests hours in the pipeline.
    """
    structure = profile.get("structure", "cross-sectional")
    panel_details = profile.get("panel_details", {})
    wide_panel = profile.get("wide_panel")

    # Determine time coverage
    time_values = panel_details.get("time_values", [])
    year_suffixes = panel_details.get("year_suffixes", [])
    n_periods = panel_details.get("n_time_periods", len(time_values) or len(year_suffixes))

    # Try to determine the earliest year in the data
    earliest_year = None
    if time_values:
        try:
            earliest_year = min(int(y) for y in time_values if str(y).isdigit())
        except (ValueError, TypeError):
            pass
    if not earliest_year and year_suffixes:
        try:
            raw = min(int(s) for s in year_suffixes)
            earliest_year = 2000 + raw if raw < 100 else raw
        except (ValueError, TypeError):
            pass

    # ── Print causal design assessment ─────────────────────────────────
    print(f"\n  {'=' * 60}")
    print(f"  CAUSAL DESIGN ASSESSMENT")
    print(f"  {'=' * 60}")

    issues = []
    score_ceiling = 95

    # Check 1: No time dimension at all
    if structure == "cross-sectional":
        score_ceiling = min(score_ceiling, 70)
        issues.append({
            "issue": "CROSS-SECTIONAL DATA (no time dimension)",
            "impact": "Cannot use DiD, event study, or individual FE. Score ceiling: ~70/100.",
            "fix": "Provide panel or repeated cross-section data spanning multiple years.",
        })

    # Check 2: Panel/temporal data but no pre-treatment period
    if structure in ("panel", "wide-panel", "pooled-cross-sections", "repeated-cross-sections"):
        # Detect if all data is post-2020 (COVID shock)
        if earliest_year and earliest_year >= 2020:
            score_ceiling = min(score_ceiling, 75)
            issues.append({
                "issue": f"NO PRE-TREATMENT DATA (earliest year: {earliest_year})",
                "impact": (
                    "Cannot test parallel trends or establish a clean pre-shock baseline. "
                    "Referees WILL ask for pre-trends. Score ceiling: ~75/100."
                ),
                "fix": (
                    "Provide data from 2017-2019 (at least 2-3 pre-treatment years). "
                    "For ENAHO: https://proyectos.inei.gob.pe/microdatos/"
                ),
            })

        # Check if only 1-2 pre-treatment years (weak pre-trends)
        elif earliest_year and earliest_year >= 2019 and n_periods <= 3:
            score_ceiling = min(score_ceiling, 80)
            issues.append({
                "issue": f"LIMITED PRE-TREATMENT DATA (only from {earliest_year}, {n_periods} periods)",
                "impact": "Pre-trend test possible but weak (only 1-2 pre-periods). Score ceiling: ~80/100.",
                "fix": "Add 1-2 more pre-treatment years for robust pre-trend testing.",
            })

    # Check 3: Short panel (few periods)
    if n_periods and n_periods < 3 and structure in ("panel", "wide-panel"):
        score_ceiling = min(score_ceiling, 80)
        issues.append({
            "issue": f"SHORT PANEL ({n_periods} periods only)",
            "impact": "Limited power for event study dynamics. Cannot show pre/post trajectory.",
            "fix": "Extend the panel to at least 4-5 periods (2+ pre, 2+ post treatment).",
        })

    # Check 4: Panel with very few time periods for dynamic effects
    if structure in ("panel", "wide-panel") and n_periods and n_periods >= 3:
        pre_periods = sum(1 for y in (time_values or []) if isinstance(y, (int, float)) and y < 2020)
        if wide_panel and year_suffixes:
            pre_periods = sum(1 for s in year_suffixes
                              if (2000 + int(s) if int(s) < 100 else int(s)) < 2020)
        post_periods = n_periods - pre_periods - 1  # -1 for treatment year
        if pre_periods == 0 and post_periods >= 2:
            # Already covered by Check 2, but add specific note
            pass
        elif pre_periods >= 2 and post_periods >= 2:
            print(f"\n  [ok] STRONG DESIGN POTENTIAL")
            print(f"       {pre_periods} pre-treatment + {post_periods} post-treatment periods")
            print(f"       Enables: DiD, event study with pre-trends, individual FE")
            print(f"       Score ceiling: ~90-95/100")

    # Print issues
    if issues:
        print(f"\n  Score ceiling with current data: ~{score_ceiling}/100\n")
        for i, w in enumerate(issues, 1):
            print(f"  [{i}] {w['issue']}")
            print(f"      Impact: {w['impact']}")
            print(f"      To fix: {w['fix']}")
            print()

        print(f"  These limitations are inherent to the DATA, not the methodology.")
        print(f"  The pipeline will proceed, but the final score will be capped")
        print(f"  regardless of how well the paper is written.")
    else:
        if score_ceiling >= 85:
            print(f"\n  [ok] Data structure supports strong causal designs.")
            print(f"       Score ceiling: ~{score_ceiling}/100")
        else:
            print(f"\n  [ok] No major structural limitations detected.")
            print(f"       Score ceiling: ~{score_ceiling}/100")

    print(f"  {'=' * 60}")


# ── Path C: data-first discovery ──────────────────────────────────────────────

def _run_path_c(project_dir: Path, state: dict) -> dict:
    """Path C: Search for high-quality datasets first, then suggest topics.

    1. Search APIs with broad queries for panel/causal datasets
    2. Download and profile top candidates
    3. Run feasibility assessment — keep only score_ceiling >= 85
    4. For qualifying datasets, ask Claude to suggest research topics
    5. User picks dataset + topic
    """
    from concurrent.futures import ThreadPoolExecutor
    from .stage1_5_data_loading import (
        _profile_dataset, _early_warning, _assess_feasibility,
        _try_download_dataverse, _try_download_zenodo, _try_download_direct,
    )
    import time as _time

    print(f"\n{'=' * 60}")
    print(f"STAGE 1: Discovery - Path C (data-first)")
    print("=" * 60)
    print("  Searching for high-quality datasets worldwide...")
    print("  Goal: find datasets that can support a 85+ score paper\n")

    t0 = _time.time()

    # ── Phase 1: Broad API search for panel datasets ──────────────────
    all_candidates = []

    # ── Strategy: Use Claude to find TOP JOURNAL papers with replication data,
    # then download from Dataverse/Zenodo using the DOIs Claude finds.
    # This is much more effective than blind API queries.

    print("  [search] Phase 1: Loading curated replication packages from top journals...")

    # Curated list of VERIFIED replication packages from Harvard Dataverse.
    # Every DOI confirmed to return downloadable data files (verified Apr 2026).
    # Priority order: RCT > Field Experiment > Natural Experiment > Staggered DiD > Panel
    # RCTs and experiments go FIRST because they have the highest score ceiling (~95)
    CURATED_PACKAGES = [
        # ══ TIER 1: RCTs and Field Experiments (score ceiling ~95) ═══
        {
            "title": "Wage Subsidies RCT Jordan (REStat)",
            "dataverse_doi": "10.7910/DVN/XJI9LO",
            "method": "RCT", "area": "labor / development",
            "design_tier": 1,
        },
        {
            "title": "Cash Transfer Replication Data",
            "dataverse_doi": "10.7910/DVN/U4QVLA",
            "method": "RCT", "area": "development",
            "design_tier": 1,
        },
        {
            "title": "Socially Responsible Consumers (QJE)",
            "dataverse_doi": "10.7910/DVN/49CETN",
            "method": "Field experiment", "area": "industrial organization",
            "design_tier": 1,
        },
        {
            "title": "Fairness in Winner-Take-All Competition (REStat)",
            "dataverse_doi": "10.7910/DVN/EZBJDL",
            "method": "Experiment", "area": "behavioral",
            "design_tier": 1,
        },
        {
            "title": "Household Plot Soil Rainfall Price Panel (Agricultural)",
            "dataverse_doi": "10.7910/DVN/NXILME",
            "method": "Panel / RCT", "area": "agriculture",
            "design_tier": 1,
        },
        {
            "title": "Elite Study Survey Data (Crime and Policing)",
            "dataverse_doi": "10.7910/DVN/WO36SX",
            "method": "Survey / Experiment", "area": "crime",
            "design_tier": 1,
        },
        # ══ TIER 2: Natural Experiments / Staggered DiD (ceiling ~85-90) ═══
        {
            "title": "Wages and Value of Nonemployment (Jaeger et al., QJE)",
            "dataverse_doi": "10.7910/DVN/GBRHTC",
            "method": "Event study", "area": "labor",
            "design_tier": 2,
        },
        {
            "title": "Labor in the Boardroom (Jaeger, Schoefer, Heining, QJE)",
            "dataverse_doi": "10.7910/DVN/WYWCBP",
            "method": "DiD / Panel", "area": "labor",
            "design_tier": 2,
        },
        {
            "title": "Oil, Gas and Political Institutions (Ross-Mahdavi 1932-2014)",
            "dataverse_doi": "10.7910/DVN/ZTPW0Y",
            "method": "Panel IV", "area": "political economy",
            "design_tier": 2,
        },
        # ══ TIER 3: Observational Panel (ceiling ~75-85) ═══
        {
            "title": "Government Austerity and World Values Survey Panel",
            "dataverse_doi": "10.7910/DVN/V7RQQ4",
            "method": "Panel FE", "area": "political economy",
            "design_tier": 3,
        },
        {
            "title": "Lexical Index of Electoral Democracy (LIED v6)",
            "dataverse_doi": "10.7910/DVN/WPKNIT",
            "method": "Panel", "area": "political science",
            "design_tier": 3,
        },
        {
            "title": "Afrobarometer Microdata Round 9 (Migration & Corruption)",
            "dataverse_doi": "10.7910/DVN/OASFBM",
            "method": "Survey / IV", "area": "development",
            "design_tier": 3,
        },
    ]

    # ── Also search Dataverse API live for fresh datasets ─────────
    print("  [search] Also searching Dataverse API for fresh datasets...")
    live_queries = [
        # PRIORITY: RCTs and experiments (highest score ceiling)
        "randomized controlled trial RCT replication data",
        "field experiment treatment control replication",
        "lab experiment behavioral economics data",
        "RCT education health development replication",
        # Natural experiments and policy discontinuities
        "regression discontinuity threshold eligibility",
        "staggered rollout policy reform panel",
        "natural experiment ban restriction access",
        # Standard high-quality panels
        "difference in differences policy change state",
        "panel health expenditure insurance household",
        "minimum wage employment county quarterly",
    ]
    for q in live_queries:
        results = _search_dataverse(q, max_results=2)
        for r in results:
            CURATED_PACKAGES.append({
                "title": r.get("name", "")[:70],
                "dataverse_doi": "",
                "url": r.get("url", ""),
                "method": "unknown", "area": "mixed",
                "provider": "Harvard Dataverse",
            })

    # Sort by design tier (RCTs first), shuffle within each tier
    import random
    random.seed(int(_time.time()) % 10000)
    packages = CURATED_PACKAGES.copy()
    # Group by tier, shuffle within tier, concatenate in tier order
    tier_groups = {}
    for p in packages:
        tier = p.get("design_tier", 9)
        tier_groups.setdefault(tier, []).append(p)
    packages = []
    for tier in sorted(tier_groups.keys()):
        group = tier_groups[tier]
        random.shuffle(group)
        packages.extend(group)
    print(f"  [search] Priority: {sum(1 for p in packages if p.get('design_tier') == 1)} RCTs, "
          f"{sum(1 for p in packages if p.get('design_tier') == 2)} natural experiments, "
          f"{sum(1 for p in packages if p.get('design_tier', 9) >= 3)} observational")

    replication_papers = packages
    print(f"  [search] {len(replication_papers)} curated packages available")

    # Convert packages to candidates with DOIs or URLs
    for paper in replication_papers:
        doi = paper.get("dataverse_doi", "")
        direct_url = paper.get("url", "")

        if doi:
            url = f"https://doi.org/{doi}" if not doi.startswith("http") else doi
        elif direct_url:
            url = direct_url
        else:
            continue

        all_candidates.append({
            "name": paper.get("title", "Unknown"),
            "provider": paper.get("provider", "Harvard Dataverse"),
            "url": url,
            "description": paper.get("data_description", ""),
            "method": paper.get("method", ""),
            "area": paper.get("area", ""),
        })

    # ── Fallback: also search APIs directly if curated list somehow empty
    if len(all_candidates) < 3:
        print("  [search] Phase 2: Supplementing with direct API search...")
        for q in ["replication wages panel", "replication education RCT"]:
            results = _search_dataverse(q, max_results=2)
            all_candidates.extend(results)

    # Deduplicate by URL
    seen_urls = set()
    unique_candidates = []
    for c in all_candidates:
        url = c.get("url", "")
        if url and url not in seen_urls:
            seen_urls.add(url)
            unique_candidates.append(c)

    elapsed = _time.time() - t0
    print(f"\n  [search] Found {len(unique_candidates)} unique candidates ({elapsed:.0f}s)")

    # ── Phase 2: Download and profile ─────────────────────────────────
    print(f"\n  [download] Attempting to download top candidates...\n")
    data_dir = project_dir / "data" / "external"
    data_dir.mkdir(parents=True, exist_ok=True)

    qualified = []  # datasets with score_ceiling >= 85
    attempted = 0
    MAX_ATTEMPTS = 15  # try more candidates to find qualifying datasets

    for i, candidate in enumerate(unique_candidates[:MAX_ATTEMPTS]):
        attempted += 1
        name = candidate.get("name", "Unknown")[:60]
        url = candidate.get("url", "")
        provider = candidate.get("provider", "").lower()
        print(f"  [{attempted}/{min(len(unique_candidates), MAX_ATTEMPTS)}] {name}")

        # Try to download
        local_path = None
        if "dataverse" in provider or "doi.org/10.7910" in url or "dataverse" in url:
            local_path = _try_download_dataverse(url, data_dir)
        elif "zenodo" in provider or "zenodo.org" in url:
            local_path = _try_download_zenodo(url, data_dir)
        if not local_path:
            local_path = _try_download_direct(url, data_dir)

        if not local_path:
            print(f"       [skip] Could not download")
            continue

        # Profile
        try:
            profile = _profile_dataset(local_path)
            warnings = _early_warning(profile)
            feasibility = _assess_feasibility(
                [{"profile": profile, "dataset": candidate, "local_path": local_path, "warnings": warnings}],
                [],
            )
            ceiling = feasibility["score_ceiling"]
            tier = feasibility["max_tier"]

            # Boost ceiling for RCTs/experiments (identification is built-in)
            method_lower = candidate.get("method", "").lower()
            design_tier = candidate.get("design_tier", 9)
            if design_tier == 1 or any(k in method_lower for k in ["rct", "experiment", "randomiz"]):
                ceiling = max(ceiling, 90)  # RCTs have minimum 90 ceiling
                tier = min(tier, 1)
            elif design_tier == 2 or any(k in method_lower for k in ["natural experiment", "stagger", "did"]):
                ceiling = max(ceiling, 85)

            print(f"       [ok] {profile['rows']:,} rows x {profile['cols']} cols | "
                  f"Structure: {profile['structure']} | "
                  f"Ceiling: {ceiling}/100 | Tier: {tier}"
                  + (" [RCT BOOST]" if design_tier == 1 else ""))

            if ceiling >= 85:
                qualified.append({
                    "candidate": candidate,
                    "local_path": local_path,
                    "profile": profile,
                    "feasibility": feasibility,
                    "warnings": warnings,
                })
                print(f"       *** QUALIFIES (score ceiling >= 85) ***")

        except Exception as e:
            print(f"       [error] Could not profile: {e}")

        # Stop early if we have 3+ qualified datasets
        if len(qualified) >= 3:
            print(f"\n  [ok] Found {len(qualified)} qualifying datasets, stopping search")
            break

    # ── Phase 3: If no qualified datasets, let user provide ───────────
    if not qualified:
        print(f"\n  No datasets with score ceiling >= 85 found automatically.")
        print(f"  You can provide a dataset path, or try Path A with a specific topic.\n")
        print("\a", end="", flush=True)
        while True:
            choice = input("  Enter dataset path (or 'quit' to exit): ").strip().strip('"')
            if choice.lower() == "quit":
                import sys
                sys.exit(0)
            elif choice and Path(choice).exists():
                try:
                    profile = _profile_dataset(choice)
                    warnings = _early_warning(profile)
                    feasibility = _assess_feasibility(
                        [{"profile": profile, "dataset": {"name": Path(choice).name},
                          "local_path": choice, "warnings": warnings}],
                        [],
                    )
                    qualified.append({
                        "candidate": {"name": Path(choice).name, "url": "user-provided"},
                        "local_path": choice,
                        "profile": profile,
                        "feasibility": feasibility,
                        "warnings": warnings,
                    })
                    print(f"  [ok] Profiled: {profile['rows']:,} rows x {profile['cols']} cols "
                          f"(ceiling: {feasibility['score_ceiling']})")
                    break
                except Exception as e:
                    print(f"  [error] {e}")
            else:
                print(f"  File not found: {choice}")

    # ── Phase 4: Show qualifying datasets and suggest topics ──────────
    print(f"\n  {'=' * 60}")
    print(f"  QUALIFYING DATASETS (score ceiling >= 85)")
    print(f"  {'=' * 60}")

    for i, q in enumerate(qualified, 1):
        f = q["feasibility"]
        p = q["profile"]
        print(f"\n  [{i}] {q['candidate'].get('name', '?')[:70]}")
        print(f"      File:      {Path(q['local_path']).name}")
        print(f"      Rows:      {p['rows']:,}")
        print(f"      Columns:   {p['cols']}")
        print(f"      Structure: {p['structure']}")
        print(f"      Ceiling:   {f['score_ceiling']}/100")
        print(f"      Max tier:  {f['max_tier']} ({f['tier_label']})")
        print(f"      Methods:   {', '.join(f['allowed_methods'][:5])}")
        if p.get("columns"):
            vars_preview = ", ".join(p["columns"][:15])
            print(f"      Variables: {vars_preview}")
            if len(p["columns"]) > 15:
                print(f"                 ... ({p['cols']} total)")

    # ── Phase 5: Ask Claude to suggest topics ─────────────────────────
    print(f"\n  [topics] Generating research topic suggestions...")

    # Build data summary for Claude
    data_summaries = []
    for i, q in enumerate(qualified, 1):
        p = q["profile"]
        f = q["feasibility"]
        cols = ", ".join(p.get("columns", [])[:30])
        data_summaries.append(
            f"Dataset {i}: {q['candidate'].get('name', '?')}\n"
            f"  Rows: {p['rows']:,}, Cols: {p['cols']}\n"
            f"  Structure: {p['structure']}\n"
            f"  Max tier: {f['max_tier']} ({f['tier_label']})\n"
            f"  Allowed methods: {', '.join(f['allowed_methods'])}\n"
            f"  Variables: {cols}\n"
            f"  Data summary: {p.get('data_summary', 'N/A')[:500]}\n"
        )

    topic_prompt = f"""You are a research advisor specializing in CAUSAL IDENTIFICATION.
Below are datasets that have been downloaded and profiled.

YOUR #1 PRIORITY: Find the EXOGENOUS VARIATION in each dataset.
Before suggesting any topic, ask: "What in this data creates a situation where
some units are treated and others are not, for reasons outside their control?"

IDENTIFICATION-FIRST APPROACH:
1. Look at the variables. Is there a POLICY CHANGE that affected some units first?
   (staggered rollout, regional reform, age threshold, income cutoff)
2. Is there a GEOGRAPHIC BOUNDARY that creates a discontinuity?
   (state borders, district lines, distance to something)
3. Is there a THRESHOLD that creates a sharp cutoff?
   (eligibility criteria, test scores, age limits, income limits)
4. Is there a NATURAL EXPERIMENT embedded in the data?
   (weather shock, unexpected policy, legal change, natural disaster)
5. Is there CROSS-SECTIONAL VARIATION in treatment intensity?
   (some regions more exposed than others for pre-determined reasons)

If you CANNOT find exogenous variation in a dataset, say so explicitly.
Do NOT propose a before-after design with universal treatment — these always
score below 80 and are rejected by referees.

DATASETS:
{"".join(data_summaries)}

For each dataset, suggest 2 specific research topics. Each MUST have:
- A source of exogenous variation that creates a credible comparison group
- Identification level A (control group) or B (dose variation) — NEVER level C
- A method that is compatible with the data structure

Return a JSON block:
```json
{{
  "suggestions": [
    {{
      "dataset_index": 1,
      "topic": "Short topic name",
      "research_question": "...",
      "method": "DiD with staggered adoption",
      "identification_level": "A",
      "identification": "Policy X was adopted by states at different times (2010-2015), creating staggered treatment variation",
      "control_group": "States that adopted later serve as controls for early adopters",
      "score_potential": "Level A identification + panel data + 5 pre-treatment years = 90+ potential"
    }}
  ]
}}
```
"""
    p_profile = get_profile("stage1")
    topic_response = run_claude(
        topic_prompt,
        model=p_profile["model"], effort=p_profile["effort"],
        allowed_tools=[],
        timeout=120,
        label="topic-suggestion",
    )
    suggestions = extract_json(topic_response)
    topic_list = suggestions.get("suggestions", []) if suggestions else []

    if topic_list:
        print(f"\n  {'=' * 60}")
        print(f"  SUGGESTED RESEARCH TOPICS")
        print(f"  {'=' * 60}")
        for i, s in enumerate(topic_list, 1):
            ds_idx = s.get("dataset_index", 1)
            ds_name = qualified[ds_idx - 1]["candidate"].get("name", "?")[:40] if ds_idx <= len(qualified) else "?"
            id_level = s.get("identification_level", "?")
            print(f"\n  [{i}] {s.get('topic', '?')}")
            print(f"      Dataset:  {ds_name}")
            print(f"      RQ:       {s.get('research_question', '?')}")
            print(f"      Method:   {s.get('method', '?')}  [ID Level: {id_level}]")
            print(f"      ID:       {s.get('identification', '?')[:120]}")
            control = s.get("control_group", "")
            if control:
                print(f"      Control:  {control[:120]}")
            print(f"      Score:    {s.get('score_potential', '?')[:120]}")
    else:
        print("  [warn] Could not generate topic suggestions")

    # ── Phase 6: User selects ─────────────────────────────────────────
    print(f"\n  {'=' * 60}")
    print(f"  Select a topic by number, or enter your own topic.")
    print(f"  {'=' * 60}")
    print("\a", end="", flush=True)

    selected_topic = None
    selected_dataset_idx = 0

    while True:
        choice = input("\n  >> ").strip()
        if choice.isdigit() and 1 <= int(choice) <= len(topic_list):
            sel = topic_list[int(choice) - 1]
            selected_topic = sel.get("topic", "research")
            selected_dataset_idx = sel.get("dataset_index", 1) - 1
            print(f"  [ok] Selected: {selected_topic}")
            break
        elif choice:
            selected_topic = choice
            if len(qualified) > 1:
                ds_choice = input(f"  Which dataset? [1-{len(qualified)}]: ").strip()
                selected_dataset_idx = int(ds_choice) - 1 if ds_choice.isdigit() else 0
            print(f"  [ok] Custom topic: {selected_topic}")
            break

    # ── Phase 7: Save state ───────────────────────────────────────────
    selected = qualified[min(selected_dataset_idx, len(qualified) - 1)]
    profile = selected["profile"]
    feasibility = selected["feasibility"]

    state["stages"]["stage1"] = {
        "status": "completed",
        "topic": selected_topic,
        "path": "C",
        "output_file": str(project_dir / "stage1_discovery.md"),
        "completed_at": datetime.now().isoformat(),
        "data_path": selected["local_path"],
        "data_profile": {
            "rows": profile["rows"],
            "cols": profile["cols"],
            "columns": profile["columns"],
            "structure": profile["structure"],
            "panel_flag": profile["panel_flag"],
            "panel_details": profile.get("panel_details", {}),
            "id_cols": profile.get("id_cols", []),
            "time_cols": profile.get("time_cols", []),
            "wide_panel": profile.get("wide_panel"),
        },
        "recommended_data_sources": [q["candidate"] for q in qualified],
    }

    # Also save Stage 1.5 as completed (data already profiled)
    state["stages"]["stage1_5"] = {
        "status": "completed",
        "completed_at": datetime.now().isoformat(),
        "n_downloaded": len(qualified),
        "n_not_downloaded": 0,
        "feasibility": feasibility,
        "downloaded_datasets": [
            {
                "name": q["candidate"].get("name", ""),
                "local_path": q["local_path"],
                "warnings": q["warnings"],
                "profile": {
                    "rows": q["profile"]["rows"],
                    "cols": q["profile"]["cols"],
                    "columns": q["profile"]["columns"],
                    "structure": q["profile"]["structure"],
                    "panel_flag": q["profile"]["panel_flag"],
                    "panel_details": q["profile"].get("panel_details", {}),
                    "id_cols": q["profile"].get("id_cols", []),
                    "time_cols": q["profile"].get("time_cols", []),
                    "wide_panel": q["profile"].get("wide_panel"),
                    "data_summary": q["profile"].get("data_summary", ""),
                },
            }
            for q in qualified
        ],
    }

    # Save discovery output
    output_file = project_dir / "stage1_discovery.md"
    output_file.parent.mkdir(parents=True, exist_ok=True)
    output_file.write_text(
        json.dumps({
            "path": "C",
            "topic": selected_topic,
            "qualified_datasets": len(qualified),
            "selected_dataset": selected["candidate"].get("name", ""),
            "feasibility": feasibility,
            "suggestions": topic_list,
        }, indent=2, ensure_ascii=False),
        encoding="utf-8",
    )

    save_state(project_dir, state)

    print(f"\n  {'=' * 60}")
    print(f"  STAGE 1 PATH C — COMPLETE")
    print(f"  {'=' * 60}")
    print(f"  Topic:     {selected_topic}")
    print(f"  Dataset:   {Path(selected['local_path']).name}")
    print(f"  Rows:      {profile['rows']:,}")
    print(f"  Columns:   {profile['cols']}")
    print(f"  Structure: {profile['structure']}")
    print(f"  Ceiling:   {feasibility['score_ceiling']}/100")
    print(f"  Tier:      {feasibility['max_tier']} ({feasibility['tier_label']})")
    print(f"  {'=' * 60}")

    return state


# ── Public runner ────────────────────────────────────────────────────────────

def run(project_dir: Path, topic: str, state: dict, data_path: Optional[str] = None, path_c: bool = False) -> dict:
    """Execute Stage 1 Discovery - Path A, B, or C."""
    if path_c:
        return _run_path_c(project_dir, state)

    path = "B" if data_path else "A"
    print(f"\n{'=' * 60}")
    print(f"STAGE 1: Discovery - Path {path}")
    print("=" * 60)

    profile = None
    early_warnings = []

    # ── Path B: profile the user dataset first ──────────────────────────
    if data_path:
        print("  [data] Profiling user dataset...")
        profile = _profile_dataset(data_path)
        print(f"  [data] {profile['rows']} rows x {profile['cols']} cols")
        if profile["panel_flag"]:
            print("  [data] Panel structure detected")

        early_warnings = _early_warning(profile)
        if early_warnings:
            print()
            for w in early_warnings:
                print(f"  [!] {w}")
            print()
            print("\a", end="", flush=True)  # Terminal bell — user input needed
            proceed = input("  Continue despite warnings? [y/N] ").strip().lower()
            if proceed != "y":
                print("  [stop] Aborted by user.")
                sys.exit(0)

        # Causal design assessment — warn early about score ceiling
        _causal_design_warning(profile)

        # Build a Path B prompt with rich data context
        cols_summary = ", ".join(profile["columns"][:30])
        if len(profile["columns"]) > 30:
            cols_summary += f", ... ({len(profile['columns'])} total)"

        # Structure-specific method guidance
        structure = profile["structure"]
        if structure == "wide-panel":
            pd_info = profile["panel_details"]
            core_sample = ", ".join(pd_info.get("core_vars_sample", [])[:10])
            suffixes = pd_info.get("year_suffixes", [])
            years = pd_info.get("time_values", [])
            unsuffixed = ", ".join(pd_info.get("unsuffixed_cols", [])[:15])
            vars_per = pd_info.get("vars_per_period", {})
            vars_per_str = ", ".join(f"{s}: {n} vars" for s, n in vars_per.items())
            structure_desc = (
                f"WIDE-FORMAT PANEL DATA — time is encoded in column name suffixes.\n"
                f"  Year suffixes: {', '.join(suffixes)}\n"
                f"  Corresponding years: {years}\n"
                f"  Time periods: {pd_info.get('n_time_periods', '?')}\n"
                f"  Variables per period: {vars_per_str}\n"
                f"  Core variables (shared across all periods): {pd_info.get('n_core_vars', '?')}\n"
                f"  Sample core vars: {core_sample}\n"
                f"  Time-invariant/ID columns: {unsuffixed}\n"
                f"\n"
                f"  IMPORTANT: Each variable appears once per year with a suffix "
                f"(e.g., {core_sample.split(',')[0].strip()}_{suffixes[0]}, "
                f"{core_sample.split(',')[0].strip()}_{suffixes[-1]}).\n"
                f"  The data MUST be reshaped from wide to long format before panel analysis.\n"
                f"  After reshaping, each row = one individual-year observation."
            )
            method_guidance = (
                "Applicable methods (after reshaping to long): DiD, event study, TWFE, "
                "individual fixed effects, dynamic panel (Arellano-Bond), Markov transition "
                "matrices, survival models, correlated random effects. "
                "The script generation stage MUST include a reshape step (wide_to_long or melt) "
                "before any econometric estimation."
            )
        elif structure == "panel":
            pd_info = profile["panel_details"]
            structure_desc = (
                f"TRUE PANEL DATA — the same individuals are tracked over time.\n"
                f"  ID column: {pd_info.get('id_column', '?')}\n"
                f"  Time column: {pd_info.get('time_column', '?')}\n"
                f"  Unique individuals: {pd_info.get('n_unique_ids', '?'):,}\n"
                f"  Time periods: {pd_info.get('n_time_periods', '?')}\n"
                f"  % IDs in 2+ periods: {pd_info.get('pct_ids_multiple_periods', '?')}%\n"
                f"  Avg obs per individual: {pd_info.get('avg_obs_per_id', '?')}"
            )
            method_guidance = (
                "Applicable methods: DiD, event study, TWFE, individual fixed effects, "
                "dynamic panel (Arellano-Bond), Markov transition matrices, survival models."
            )
        elif structure == "pooled-cross-sections":
            pd_info = profile["panel_details"]
            structure_desc = (
                f"POOLED CROSS-SECTIONS — different individuals sampled each period.\n"
                f"  ID column: {pd_info.get('id_column', '?')} (does NOT repeat across time)\n"
                f"  Time column: {pd_info.get('time_column', '?')}\n"
                f"  Time periods: {pd_info.get('n_time_periods', '?')}\n"
                f"  Time values: {pd_info.get('time_values', [])}\n"
                f"  CRITICAL: You CANNOT track individuals over time. "
                f"Only {pd_info.get('pct_ids_multiple_periods', 0)}% of IDs appear in 2+ periods."
            )
            method_guidance = (
                "Applicable methods: DiD at GROUP level (not individual), repeated cross-section DiD, "
                "IV, RDD, propensity score matching, Oaxaca-Blinder decomposition, "
                "synthetic control (aggregate), cohort analysis. "
                "NOT applicable: individual fixed effects, individual-level event study, "
                "Markov transition matrices, survival/hazard models tracking individuals."
            )
        elif structure == "repeated-cross-sections":
            pd_info = profile["panel_details"]
            structure_desc = (
                f"REPEATED CROSS-SECTIONS — multiple survey waves, no individual tracking.\n"
                f"  Time column: {pd_info.get('time_column', '?')}\n"
                f"  Time periods: {pd_info.get('n_time_periods', '?')}\n"
                f"  No individual ID column found."
            )
            method_guidance = (
                "Applicable methods: group-level DiD, repeated cross-section DiD, "
                "IV, RDD, decompositions, cohort/pseudo-panel analysis. "
                "NOT applicable: individual FE, individual event study, transition matrices."
            )
        else:
            structure_desc = (
                f"SINGLE CROSS-SECTION — one snapshot in time, no panel dimension."
            )
            method_guidance = (
                "Applicable methods: IV, RDD, matching (PSM, CEM), "
                "Oaxaca-Blinder decomposition, Heckman selection model, "
                "quantile regression, LASSO for variable selection. "
                "NOT applicable: DiD, event study, fixed effects, transition matrices."
            )

        prompt = f"""You are a research discovery assistant (Path B - user-provided data).

The researcher works in: **{topic}**

## Dataset Structure Analysis

{structure_desc}

{method_guidance}

## Dataset Details

- Rows: {profile['rows']:,}
- Columns: {profile['cols']}
- Variables: {cols_summary}
- ID columns detected: {', '.join(profile['id_cols'][:5]) if profile['id_cols'] else 'None'}
- Time columns detected: {', '.join(profile['time_cols'][:5]) if profile['time_cols'] else 'None'}

## Data Sample

{profile.get('data_summary', profile.get('sample_rows', 'N/A'))}

## CRITICAL RULES

1. You MUST respect the data structure classification above. If the data is
   "pooled cross-sections" or "cross-sectional", do NOT suggest methods that
   require tracking the same individual over time (panel FE, Markov transitions,
   individual event study, survival models).
2. Only suggest methods that are IMPLEMENTABLE with the actual variables present.
3. If the data has a time dimension but is NOT panel, you can use group-level
   variation over time (e.g., regional DiD, cohort DiD) but NOT individual-level.

## TASK

Based on the dataset structure above, summarize the key characteristics and
recommend the most promising causal methods for this data.

Output a JSON block:
```json
{{
  "topic": "{topic}",
  "data_profile": {{
    "rows": {profile['rows']},
    "cols": {profile['cols']},
    "structure": "{structure}",
    "panel": {str(profile['panel_flag']).lower()},
    "id_cols": {profile['id_cols'][:5]},
    "time_cols": {profile['time_cols'][:5]},
    "warnings": {early_warnings},
    "recommended_methods": ["method1", "method2", "method3"]
  }}
}}
```
"""

    # ── Path A: multi-agent dataset search ───────────────────────────────
    else:
        from concurrent.futures import ThreadPoolExecutor, as_completed
        import time as _time

        print(f"\n  [search] Launching 3 parallel searches...")
        t0 = _time.time()

        # ── Subagent 1: Claude web search (identification-first) ──────
        web_prompt = (
            f'You are searching for datasets to study "{topic}" with CAUSAL identification.\n'
            f'\n'
            f'IDENTIFICATION-FIRST APPROACH: Do NOT just search for data about {topic}.\n'
            f'Instead, search for NATURAL EXPERIMENTS related to {topic}:\n'
            f'  1. Policy reforms that were adopted at different times in different regions\n'
            f'     (staggered rollout = DiD with clean control group)\n'
            f'  2. Eligibility thresholds or cutoffs (age, income, score = RDD)\n'
            f'  3. Bans, restrictions, or access limitations that varied by jurisdiction\n'
            f'  4. Exogenous shocks that affected some units more than others\n'
            f'  5. Replication packages from TOP JOURNAL papers that used causal designs\n'
            f'     on topics related to "{topic}"\n'
            f'\n'
            f'Search: government microdata portals (IPUMS, DHS, LSMS, EU-SILC, CFPS),\n'
            f'international orgs (World Bank, OECD, UNESCO, ILO), Harvard Dataverse,\n'
            f'or any national statistics office worldwide.\n'
            f'Prefer panel data with staggered treatment or discontinuities.\n'
            f'Do NOT default to any specific country.\n'
            f'\n'
            f'CRITICAL: If the topic involves a UNIVERSAL SHOCK (e.g., a global product\n'
            f'launch, a pandemic), search for data where ACCESS or EXPOSURE varied across\n'
            f'units (country bans, regional restrictions, infrastructure differences).\n'
            f'A dataset with treatment variation is worth 10x a dataset without it.\n'
            f'\n'
            f'Return ONLY a JSON object:\n'
            f'{{"name": "...", "provider": "...", "url": "https://...",'
            f' "data_structure": "panel|cross-section|repeated-cross-sections",'
            f' "time_span": "...", "n_years": 0,'
            f' "natural_experiment": "SPECIFIC description of what creates treatment variation",'
            f' "control_group": "WHO is untreated and WHY",'
            f' "causal_methods_enabled": ["DiD"], "causal_score": 0,'
            f' "format": ".csv", "access": "free_direct|free_registration|restricted",'
            f' "files_needed": ["file.csv"], "limitations": "..."}}'
        )
        p = get_profile("stage1")

        # Run all 3 in parallel: Claude web search + Dataverse API + Zenodo/GitHub APIs
        api_results = {"dataverse": [], "zenodo": [], "github": []}
        web_result = ""

        def _run_web_search():
            return run_claude(
                web_prompt,
                model=p["model"], effort=p["effort"],
                allowed_tools=["WebSearch", "WebFetch"],
                timeout=120,
                max_retries=1,
                label="web-search",
            )

        def _run_api_searches():
            # Search both the topic directly AND natural experiment variants
            api_results["dataverse"] = _search_dataverse(topic)
            api_results["dataverse"] += _search_dataverse(f"{topic} replication natural experiment")
            api_results["zenodo"] = _search_zenodo(topic)
            api_results["zenodo"] += _search_zenodo(f"{topic} policy reform panel")
            api_results["github"] = _search_github(topic)

        with ThreadPoolExecutor(max_workers=2) as pool:
            future_web = pool.submit(_run_web_search)
            future_api = pool.submit(_run_api_searches)

            for future in as_completed([future_web, future_api]):
                try:
                    result = future.result()
                    if future == future_web:
                        web_result = result
                except Exception as e:
                    if future == future_web:
                        print(f"  [web-search] Timed out or failed — continuing with API results only")
                    else:
                        print(f"  [error] API search failed: {e}")

        elapsed = _time.time() - t0
        print(f"  [search] All searches done ({elapsed:.0f}s)")

        # ── Collect raw results from all sources ──────────────────────
        raw_web = []
        parsed = extract_json(web_result) if web_result else None
        if parsed:
            if isinstance(parsed, dict) and "name" in parsed:
                raw_web.append(parsed)
            elif isinstance(parsed, dict) and "data_sources" in parsed:
                raw_web.extend(parsed["data_sources"])
            elif isinstance(parsed, list):
                raw_web.extend(parsed)

        n_dv = len(api_results["dataverse"])
        n_zn = len(api_results["zenodo"])
        n_gh = len(api_results["github"])
        n_web = len(raw_web)
        print(f"  [search] Results: web={n_web}, dataverse={n_dv}, zenodo={n_zn}, github={n_gh}")

        # ── Subagent 4: Consolidator — evaluate and rank ──────────────
        all_candidates = json.dumps({
            "web_search_results": raw_web,
            "dataverse_results": api_results["dataverse"],
            "zenodo_results": api_results["zenodo"],
            "github_results": api_results["github"],
        }, indent=2, ensure_ascii=False)

        consolidator_prompt = f"""You are a dataset evaluator for causal empirical research.
Your #1 job: find datasets where TREATMENT VARIES ACROSS UNITS.

TOPIC: "{topic}"

Below are candidate datasets found from multiple sources. Select the TOP 3 datasets
that can produce a paper scoring 85+/100. The binding constraint is ALWAYS identification
— a dataset with treatment variation beats a bigger/cleaner dataset without it.

EVALUATION CRITERIA (RANKED BY IMPORTANCE):

1. EXOGENOUS VARIATION (most important — 50% of evaluation):
   Does the data contain a situation where some units are treated and others are not?
   - BEST: Staggered policy rollout (different regions treated at different times)
   - GOOD: Eligibility threshold creating a discontinuity (RDD)
   - OK: Universal treatment but intensity varies cross-sectionally (dose-response)
   - WEAK: Universal simultaneous treatment (before-after only = Level C)

   *** A dataset with clear treatment variation but only 5,000 obs is BETTER than
   a dataset with 500,000 obs but no treatment variation. ***

2. DATA STRUCTURE:
   - Panel data (same units tracked over time) >> repeated cross-sections >> cross-section
   - Pre-treatment periods: at least 3 years before treatment for credible pre-trends

3. STATISTICAL POWER:
   - Enough clusters for cluster-robust inference (30+ clusters)
   - Treatment/control groups large enough to detect meaningful effects

4. DATA QUALITY & ACCESS:
   - Publicly accessible, well-documented
   - Low attrition, consistent variable definitions

CAUSAL SCORE (1-5):
  5 = Staggered treatment + panel + 3+ pre-years + clear control group + accessible
  4 = Cross-sectional treatment variation + panel + plausible ID
  3 = Dose variation (continuous treatment) + panel + some pre-periods
  2 = Panel but universal treatment, or cross-section with strong IV/RDD
  1 = Universal simultaneous treatment with no control group

*** REJECT any dataset that can only support Level C identification (causal_score=1)
unless no better option exists. ***

CANDIDATE DATASETS:
{all_candidates}

Select the TOP 3 and return ONLY a JSON block:
```json
{{
  "topic": "{topic}",
  "data_sources": [
    {{
      "name": "Full dataset name",
      "provider": "Organization",
      "url": "https://...",
      "data_structure": "panel",
      "time_span": "2010-2024",
      "n_years": 15,
      "natural_experiment": "Description of exogenous variation",
      "causal_methods_enabled": ["DiD", "event study", "TWFE"],
      "causal_score": 4,
      "format": ".csv",
      "access": "free_direct",
      "files_needed": ["file1.csv"],
      "limitations": "Brief limitation"
    }}
  ]
}}
```
"""
        print(f"\n  [consolidator] Evaluating and ranking datasets...")
        consolidator_response = run_claude(
            consolidator_prompt,
            model=p["model"], effort=p["effort"],
            allowed_tools=[],
            timeout=120,
            label="consolidator",
        )
        papers_data = extract_json(consolidator_response)
        if not papers_data:
            # Fallback: use web search results directly
            papers_data = {"topic": topic, "data_sources": raw_web}

    output_file = project_dir / "stage1_discovery.md"

    if data_path:
        # Path B: single call with haiku, no web search
        p_b = get_profile("stage1_b")
        response = run_claude(
            prompt,
            model=p_b["model"], effort=p_b["effort"],
            allowed_tools=[],
            output_file=output_file,
        )
        papers_data = extract_json(response)
    else:
        # Path A: save consolidated results to output file
        output_file.parent.mkdir(parents=True, exist_ok=True)
        output_file.write_text(
            json.dumps(papers_data, indent=2, ensure_ascii=False),
            encoding="utf-8",
        )
        print(f"  [saved] {output_file}")

    state["stages"]["stage1"] = {
        "status": "completed",
        "topic": topic,
        "path": path,
        "output_file": str(output_file),
        "completed_at": datetime.now().isoformat(),
    }

    if data_path:
        state["stages"]["stage1"]["data_path"] = data_path
    if profile:
        state["stages"]["stage1"]["data_profile"] = {
            "rows": profile["rows"],
            "cols": profile["cols"],
            "columns": profile["columns"],
            "structure": profile["structure"],
            "panel_flag": profile["panel_flag"],
            "panel_details": profile.get("panel_details", {}),
            "id_cols": profile.get("id_cols", []),
            "time_cols": profile.get("time_cols", []),
            "wide_panel": profile.get("wide_panel"),
            "warnings": early_warnings,
        }

    # Save recommended data sources (Path A)
    if papers_data and "data_sources" in papers_data:
        state["stages"]["stage1"]["recommended_data_sources"] = papers_data["data_sources"]
        n_sources = len(papers_data["data_sources"])
        best_score = max((ds.get("causal_score", 0) for ds in papers_data["data_sources"]), default=0)
        print(f"  [ok] Found {n_sources} data sources (best causal score: {best_score}/5)")

    if not papers_data:
        print("  [warn] Could not parse structured JSON. Check stage1_discovery.md manually.")

    # ── Final summary: show user what data is available ────────────────
    print(f"\n  {'=' * 60}")
    print(f"  STAGE 1 DISCOVERY — SUMMARY")
    print(f"  {'=' * 60}")
    print(f"  Topic: {topic}")
    print(f"  Path:  {'B (user data)' if path == 'B' else 'A (dataset search)'}")

    if profile:
        print(f"\n  DATA LOADED:")
        print(f"    File:      {Path(data_path).name}")
        print(f"    Location:  {data_path}")
        print(f"    Rows:      {profile['rows']:,}")
        print(f"    Columns:   {profile['cols']}")
        print(f"    Structure: {profile['structure']}")
        if profile.get("id_cols"):
            print(f"    ID cols:   {', '.join(profile['id_cols'][:5])}")
        if profile.get("time_cols"):
            print(f"    Time cols: {', '.join(profile['time_cols'][:5])}")
        if early_warnings:
            print(f"\n  WARNINGS:")
            for w in early_warnings:
                print(f"    - {w}")
    elif papers_data and papers_data.get("data_sources"):
        sources = papers_data["data_sources"]
        sources.sort(key=lambda x: x.get("causal_score", 0), reverse=True)
        print(f"\n  RECOMMENDED DATASETS ({len(sources)} found):")
        for i, ds in enumerate(sources[:3], 1):
            print(f"\n    [{i}] {ds.get('name', '?')}")
            print(f"        URL:       {ds.get('url', 'N/A')}")
            fmt = ds.get("format", "N/A")
            files = ds.get("files_needed", [])
            if files:
                print(f"        Files:     {', '.join(files[:3])}")
                if len(files) > 3:
                    print(f"                   ... ({len(files)} total)")
            elif fmt:
                print(f"        Format:    {fmt}")
            print(f"        Structure: {ds.get('data_structure', 'N/A')}")
            print(f"        Time span: {ds.get('time_span', 'N/A')}")
            score = ds.get("causal_score", 0)
            print(f"        Causal:    {'*' * score}{'.' * (5 - score)} ({score}/5)")
            access = ds.get("access", "unknown")
            print(f"        Access:    {access}")
        print(f"\n  To use a dataset, re-run with:")
        print(f"  python run_pipeline.py --topic \"{topic}\" --data \"path/to/data.csv\"")
    else:
        print(f"\n  No structured data found. Check stage1_discovery.md for details.")

    print(f"  {'=' * 60}")

    state["current_stage"] = 1
    save_state(project_dir, state)
    return state
