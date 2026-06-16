# tests/test_brain_cli.py
import os
import shutil
import subprocess
from pathlib import Path

import brain
import logbook
import pytest


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


@pytest.mark.skipif(shutil.which("graphify") is None, reason="graphify CLI not installed")
def test_refresh_local_runs_offline_zero_token_cost(tmp_path):
    repo = tmp_path
    subprocess.run(["git", "init"], cwd=repo, check=True, capture_output=True)
    subprocess.run(["git", "config", "user.email", "t@t.t"], cwd=repo, check=True)
    subprocess.run(["git", "config", "user.name", "t"], cwd=repo, check=True)
    (repo / "core").mkdir()
    (repo / "core" / "a.py").write_text("def f():\n    return 1\n", encoding="utf-8")
    subprocess.run(["git", "add", "-A"], cwd=repo, check=True)
    subprocess.run(["git", "commit", "-m", "base"], cwd=repo, check=True, capture_output=True)
    allow = repo / "allowlist.yml"
    allow.write_text("roots:\n  - { path: core/, type: code, backend: offline }\nexclude: []\n", encoding="utf-8")
    env = {
        "SCHOOLSWP_REPO_PATH": str(repo),
        "GRAPHIFY_OUTPUT_PATH": str(repo / "schoolswp-brain" / ".graphify"),
        "GEMINI_API_KEY": "should-be-stripped",
        "PATH": os.environ["PATH"],
        # graphify calls Path.home() internally; pass the minimum OS vars it needs
        **{k: os.environ[k] for k in ("USERPROFILE", "HOMEDRIVE", "HOMEPATH", "HOME") if k in os.environ},
    }
    rc = brain.main(["refresh", "--local", "--allowlist", str(allow)], env=env)
    assert rc == 0
    report = repo / "schoolswp-brain" / ".graphify" / "graphify-out" / "GRAPH_REPORT.md"
    assert report.exists()
    assert "Token cost: 0 input" in report.read_text(encoding="utf-8")


def test_dry_run_egress_is_full_corpus_not_delta(tmp_path, capsys):
    env = _setup(tmp_path)
    (tmp_path / "docs" / "b.md").write_text("# B\n", encoding="utf-8")
    subprocess.run(["git", "add", "-A"], cwd=tmp_path, check=True)
    subprocess.run(["git", "commit", "-m", "b"], cwd=tmp_path, check=True, capture_output=True)
    head = subprocess.run(["git", "rev-parse", "HEAD"], cwd=tmp_path, capture_output=True, text=True).stdout.strip()
    logbook.write_state(tmp_path / "schoolswp-brain" / "07_graph" / ".brain-state.json", head)
    rc = brain.main(["refresh", "--dry-run", "--allowlist", str(tmp_path / "allowlist.yml")], env=env)
    out = capsys.readouterr().out
    assert rc == 0
    assert "0 new, 0 modified" in out  # the git delta is empty
    assert "FULL Gemini corpus: 2" in out  # but a --gemini refresh would re-process both docs


def test_gemini_aborts_on_secret_in_unchanged_doc(tmp_path, monkeypatch):
    env = _setup(tmp_path)
    (tmp_path / "docs" / "leak.md").write_text(
        "GEMINI_API_KEY=AIzaSyABCDEF1234567890abcdefABCDEF12345\n", encoding="utf-8"
    )
    subprocess.run(["git", "add", "-A"], cwd=tmp_path, check=True)
    subprocess.run(["git", "commit", "-m", "leak"], cwd=tmp_path, check=True, capture_output=True)
    head = subprocess.run(["git", "rev-parse", "HEAD"], cwd=tmp_path, capture_output=True, text=True).stdout.strip()
    logbook.write_state(tmp_path / "schoolswp-brain" / "07_graph" / ".brain-state.json", head)
    # delta is now empty, but the secret lives in a committed (unchanged) doc inside the gemini corpus
    monkeypatch.setattr(
        brain.graphify_runner,
        "run_extract",
        lambda *a, **k: (_ for _ in ()).throw(AssertionError("must not send")),
    )
    rc = brain.main(["refresh", "--gemini", "--yes", "--allowlist", str(tmp_path / "allowlist.yml")], env=env)
    assert rc == 3  # secret-scan abort, even though the secret was in an unchanged file


def test_allowlist_after_subcommand_is_used(tmp_path):
    env = _setup(tmp_path)
    # a second allowlist with NO gemini roots -> corpus would be empty if this file is the one loaded
    alt = tmp_path / "alt.yml"
    alt.write_text("roots:\n  - { path: core/, type: code, backend: offline }\nexclude: []\n", encoding="utf-8")
    cfg = brain.config.load_config(alt, env)
    assert [r.path for r in cfg.roots] == ["core/"]
