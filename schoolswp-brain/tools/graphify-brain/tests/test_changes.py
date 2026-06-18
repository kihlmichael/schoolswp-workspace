# tests/test_changes.py
import subprocess
from pathlib import Path

import changes
from config import Root


def _git(repo: Path, *args: str) -> str:
    return subprocess.run(["git", *args], cwd=repo, capture_output=True, text=True, check=True).stdout


def _init_repo(tmp_path: Path) -> Path:
    repo = tmp_path
    _git(repo, "init")
    _git(repo, "config", "user.email", "t@t.t")
    _git(repo, "config", "user.name", "t")
    (repo / "core").mkdir()
    (repo / "core" / "a.py").write_text("x = 1\n", encoding="utf-8")
    (repo / "docs").mkdir()
    (repo / "docs" / "g.md").write_text("# G\n", encoding="utf-8")
    _git(repo, "add", "-A")
    _git(repo, "commit", "-m", "base")
    return repo


ROOTS = [Root("core/", "code", "offline"), Root("docs/", "content", "gemini")]


def test_changed_files_detects_new_and_modified(tmp_path):
    repo = _init_repo(tmp_path)
    base = _git(repo, "rev-parse", "HEAD").strip()
    (repo / "core" / "a.py").write_text("x = 2\n", encoding="utf-8")  # modified
    (repo / "docs" / "new.md").write_text("# New\n", encoding="utf-8")  # new (untracked)
    cs = changes.changed_files(repo, since_commit=base, roots=ROOTS, exclude=[])
    assert any(p.endswith("a.py") for p in cs.modified)
    assert any(p.endswith("new.md") for p in cs.new)


def test_split_local_vs_egress(tmp_path):
    _init_repo(tmp_path)
    cs = changes.ChangedSet(new=["docs/new.md", "core/b.py"], modified=["core/a.py", "docs/g.md"])
    local, egress = changes.split_local_vs_egress(cs, ROOTS)
    assert "core/a.py" in local and "core/b.py" in local
    assert "docs/new.md" in egress and "docs/g.md" in egress
    assert "docs/new.md" not in local
