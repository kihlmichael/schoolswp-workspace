# tests/test_brain_cli.py
import subprocess
from pathlib import Path

import brain


def _setup(tmp_path: Path) -> dict:
    subprocess.run(["git", "init"], cwd=tmp_path, check=True, capture_output=True)
    subprocess.run(["git", "config", "user.email", "t@t.t"], cwd=tmp_path, check=True)
    subprocess.run(["git", "config", "user.name", "t"], cwd=tmp_path, check=True)
    allow = tmp_path / "allowlist.yml"
    allow.write_text(
        'roots:\n  - { path: docs/, type: content, backend: gemini }\nexclude: []\ngemini_model: "gemini-2.5-flash"\n',
        encoding="utf-8",
    )
    (tmp_path / "docs").mkdir()
    (tmp_path / "docs" / "a.md").write_text("# A\n", encoding="utf-8")
    subprocess.run(["git", "add", "-A"], cwd=tmp_path, check=True)
    subprocess.run(["git", "commit", "-m", "base"], cwd=tmp_path, check=True, capture_output=True)
    return {
        "SCHOOLSWP_REPO_PATH": str(tmp_path),
        "GRAPHIFY_OUTPUT_PATH": str(tmp_path / "schoolswp-brain" / ".graphify"),
        "GEMINI_API_KEY": "x",
        "PATH": "/usr/bin",
    }


def test_gemini_without_yes_sends_nothing(tmp_path, monkeypatch):
    env = _setup(tmp_path)
    calls = {"gemini": 0}
    monkeypatch.setattr(
        brain.graphify_runner,
        "run_cluster",
        lambda *a, **k: calls.__setitem__("gemini", calls["gemini"] + 1),
    )
    rc = brain.main(["refresh", "--gemini", "--allowlist", str(tmp_path / "allowlist.yml")], env=env)
    assert rc != 0  # refused
    assert calls["gemini"] == 0  # nothing sent


def test_dry_run_reports_and_sends_nothing(tmp_path, capsys, monkeypatch):
    env = _setup(tmp_path)
    monkeypatch.setattr(
        brain.graphify_runner,
        "run_extract",
        lambda *a, **k: (_ for _ in ()).throw(AssertionError("must not run")),
    )
    rc = brain.main(["refresh", "--changed", "--dry-run", "--allowlist", str(tmp_path / "allowlist.yml")], env=env)
    out = capsys.readouterr().out
    assert rc == 0
    assert "DRY-RUN" in out
    assert "Gemini" in out  # egress section present
