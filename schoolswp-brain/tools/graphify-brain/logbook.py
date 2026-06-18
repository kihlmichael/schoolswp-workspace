"""Append-only refresh log (jsonl) + last-indexed-commit state."""

from __future__ import annotations

import json
from dataclasses import asdict, dataclass
from pathlib import Path


@dataclass
class RefreshLogEntry:
    date: str
    command: str
    files_analyzed: int
    files_sent: int
    model: str | None
    est_cost_usd: float | None
    real_cost_usd: float | None
    result: str


def append_log(log_dir: Path, entry: RefreshLogEntry) -> Path:
    log_dir = Path(log_dir)
    log_dir.mkdir(parents=True, exist_ok=True)
    out = log_dir / "refresh.jsonl"
    with out.open("a", encoding="utf-8") as fh:
        fh.write(json.dumps(asdict(entry), ensure_ascii=False) + "\n")
    return out


def read_state(state_file: Path) -> dict:
    p = Path(state_file)
    if not p.exists():
        return {}
    try:
        return json.loads(p.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return {}


def write_state(state_file: Path, commit: str) -> None:
    p = Path(state_file)
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(
        json.dumps({"last_indexed_commit": commit}, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
