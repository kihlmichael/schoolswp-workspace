# tests/test_logbook.py
import json

import logbook


def test_append_log_writes_jsonl(tmp_path):
    entry = logbook.RefreshLogEntry(
        date="2026-06-16T10:00:00",
        command="refresh --local",
        files_analyzed=42,
        files_sent=0,
        model=None,
        est_cost_usd=None,
        real_cost_usd=None,
        result="ok",
    )
    out = logbook.append_log(tmp_path, entry)
    assert out.exists()
    rows = [json.loads(line) for line in out.read_text(encoding="utf-8").splitlines()]
    assert rows[-1]["command"] == "refresh --local"
    assert rows[-1]["files_sent"] == 0


def test_state_round_trip(tmp_path):
    state_file = tmp_path / ".brain-state.json"
    assert logbook.read_state(state_file) == {}
    logbook.write_state(state_file, "abc123")
    assert logbook.read_state(state_file)["last_indexed_commit"] == "abc123"
