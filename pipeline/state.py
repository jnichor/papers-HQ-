"""Pipeline state management — load, save, and query project state."""

import json
from datetime import datetime
from pathlib import Path

from .config import PAPERS_HQ


def ensure_project_dir(project_name: str) -> Path:
    """Create and return the project workspace inside papers-HQ/projects/."""
    project_dir = PAPERS_HQ / "projects" / project_name
    project_dir.mkdir(parents=True, exist_ok=True)
    return project_dir


def load_state(project_dir: Path) -> dict:
    """Load pipeline state for a project, or return a fresh skeleton."""
    state_file = project_dir / "pipeline_state.json"
    if state_file.exists():
        return json.loads(state_file.read_text(encoding="utf-8"))
    return {
        "project": project_dir.name,
        "created_at": datetime.now().isoformat(),
        "current_stage": 0,
        "stages": {},
    }


def save_state(project_dir: Path, state: dict):
    """Persist pipeline state to disk.  Called before every human checkpoint
    so that Ctrl-C never loses progress."""
    state["updated_at"] = datetime.now().isoformat()
    (project_dir / "pipeline_state.json").write_text(
        json.dumps(state, indent=2, ensure_ascii=False), encoding="utf-8"
    )


def mark_stage(state: dict, stage_key: str, *, status: str = "completed", **extra) -> dict:
    """Helper to mark a stage as completed (or failed/skipped) and attach extra metadata."""
    entry = {"status": status, "completed_at": datetime.now().isoformat()}
    entry.update(extra)
    state["stages"][stage_key] = entry
    return state
