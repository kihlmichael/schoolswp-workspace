# schoolsWP Second Brain (graphify) - MVP Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build the `graphify-brain` guardrail wrapper so graphify can map the schoolsWP repo as a queryable second brain, while schoolsWP decides what is indexed, what egresses to Gemini, and logs every refresh.

**Architecture:** graphify is the engine; a small Python package `schoolswp-brain/tools/graphify-brain/` wraps it. An `allowlist.yml` is the single source of truth for indexable roots and exclusions; it compiles to a `.graphifyignore`. Markdown is scanned locally for structure (no LLM); code is AST-extracted offline; content semantics reach Gemini only after an explicit `--yes` gate that follows a mandatory dry-run + pre-send secret scan. Every refresh appends to a log. Index-in-place: nothing is migrated, the graph output lives gitignored under `schoolswp-brain/.graphify/`.

**Tech Stack:** Python 3.11 (project venv), PyYAML, stdlib (argparse, subprocess, re, json, pathlib, datetime), pytest. graphify pinned to 0.8.40 (`graphifyy[openai]`, CLI on PATH). Lint: ruff (E,F,W,I; line 120). Filenames kebab-case; Python modules use underscores.

**Spec:** `docs/superpowers/specs/2026-06-16-schoolswp-brain-graphify-design.md`

---

## File Structure

```
schoolswp-brain/
├── .graphify/                              # graphify output (GITIGNORED); graphify creates graphify-out/ inside
├── 07_graph/
│   ├── logs/.gitkeep                       # refresh logs (committed dir)
│   └── (.brain-state.json at runtime)      # last indexed commit (gitignored)
└── tools/graphify-brain/
    ├── allowlist.yml                       # roots + excludes (source of truth)
    ├── config.py                           # env + allowlist load; .graphifyignore compilation
    ├── md_local_index.py                   # local markdown structural scan (no LLM)
    ├── changes.py                          # git changed-files since last indexed commit
    ├── secrets_scan.py                     # pre-send secret pattern scan
    ├── cost.py                             # token/cost heuristic estimate
    ├── logbook.py                          # append-only refresh log + state file
    ├── graphify_runner.py                  # subprocess wrappers around the graphify CLI
    ├── brain.py                            # CLI entry point (argparse)
    └── tests/
        ├── conftest.py
        ├── test_config.py
        ├── test_md_local_index.py
        ├── test_changes.py
        ├── test_secrets_scan.py
        ├── test_cost.py
        ├── test_logbook.py
        └── test_brain_cli.py
```

Root-level change: `.gitignore` gains `schoolswp-brain/.graphify/` and `schoolswp-brain/07_graph/.brain-state.json`.

Interfaces locked across tasks (names are final):

- `config.Root(path: str, type: str, backend: str)` ; `config.BrainConfig(repo_path, obsidian_bridge_path, output_path, roots, exclude, gemini_model)`
- `config.load_config(allowlist_file, env) -> BrainConfig`
- `config.compile_graphifyignore(cfg, mode) -> str` with `mode in {"code-only", "full"}`
- `md_local_index.MdDoc(path, title, headings, wikilinks, tags, frontmatter)` ; `scan_markdown_file(path) -> MdDoc` ; `scan_tree(root, exclude) -> list[MdDoc]`
- `changes.ChangedSet(new: list[str], modified: list[str])` ; `changed_files(repo, since_commit, roots, exclude) -> ChangedSet` ; `split_local_vs_egress(changed, roots) -> tuple[list[str], list[str]]`
- `secrets_scan.SecretHit(path, line, pattern)` ; `scan_files(paths) -> list[SecretHit]`
- `cost.CostEstimate(files, total_chars, est_tokens, est_usd)` ; `estimate(paths, model) -> CostEstimate`
- `logbook.RefreshLogEntry(...)` ; `append_log(log_dir, entry) -> Path` ; `read_state(state_file) -> dict` ; `write_state(state_file, commit) -> None`
- `graphify_runner.run_extract / run_cluster / run_query / run_explain / run_path`

---

## Task 0: Scaffold + allowlist + gitignore

**Files:**

- Create: `schoolswp-brain/tools/graphify-brain/allowlist.yml`
- Create: `schoolswp-brain/tools/graphify-brain/tests/conftest.py`
- Create: `schoolswp-brain/07_graph/logs/.gitkeep`
- Modify: `.gitignore`

- [ ] **Step 1: Create directory tree and gitkeep**

```bash
mkdir -p "schoolswp-brain/tools/graphify-brain/tests"
mkdir -p "schoolswp-brain/07_graph/logs"
: > "schoolswp-brain/07_graph/logs/.gitkeep"
```

- [ ] **Step 2: Write `allowlist.yml`**

```yaml
# Source of truth for the schoolsWP second brain. Nothing outside `roots` is indexed.
# backend governs MARKDOWN egress only. Code (.py/.ps1/...) in any root is ALWAYS offline.
roots:
  - { path: core/, type: code, backend: offline }
  - { path: tools/, type: code, backend: offline }
  - { path: docs/, type: content, backend: gemini }
  - { path: content/articles/, type: content, backend: gemini }
  - { path: content/audits/, type: content, backend: gemini }
  - { path: content/decisions/, type: content, backend: gemini }
  - { path: schoolswp-agents/, type: content, backend: gemini }
  - { path: obsidian-bridge/, type: content, backend: gemini }
exclude:
  - "**/.env*"
  - "**/*.key"
  - "**/*.pem"
  - ".credentials/**"
  - "**/_drafts/**"
  - "**/_workspace/**"
  - "tmp_*/**"
  - ".tmp-*/**"
  - "node_modules/**"
  - "**/.venv/**"
  - "obsidian-bridge/logs/**"
gemini_model: "gemini-2.5-flash"
```

- [ ] **Step 3: Add gitignore entries**

Append to `.gitignore`:

```gitignore
# schoolsWP second brain (graphify): derived graph output stays local
schoolswp-brain/.graphify/
schoolswp-brain/07_graph/.brain-state.json
```

- [ ] **Step 4: Write `tests/conftest.py` (make sibling modules importable)**

```python
import sys
from pathlib import Path

# Make the graphify-brain package modules importable as top-level modules in tests.
PKG_DIR = Path(__file__).resolve().parent.parent
if str(PKG_DIR) not in sys.path:
    sys.path.insert(0, str(PKG_DIR))
```

- [ ] **Step 5: Smoke-check graphify is on PATH**

Run: `graphify --version`
Expected: prints `graphify 0.8.40` (if missing: `uv tool install "graphifyy[openai]==0.8.40" --force`).

- [ ] **Step 6: Commit**

```bash
git add schoolswp-brain/tools/graphify-brain/allowlist.yml schoolswp-brain/tools/graphify-brain/tests/conftest.py schoolswp-brain/07_graph/logs/.gitkeep .gitignore
git commit -m "feat(brain): scaffold graphify-brain wrapper (allowlist, dirs, gitignore)"
```

---

## Task 1: config.py - load env + allowlist

**Files:**

- Create: `schoolswp-brain/tools/graphify-brain/config.py`
- Test: `schoolswp-brain/tools/graphify-brain/tests/test_config.py`

- [ ] **Step 1: Write the failing test**

```python
# tests/test_config.py
from pathlib import Path
import config


def _write_allowlist(tmp_path: Path) -> Path:
    f = tmp_path / "allowlist.yml"
    f.write_text(
        "roots:\n"
        "  - { path: core/, type: code, backend: offline }\n"
        "  - { path: docs/, type: content, backend: gemini }\n"
        "exclude:\n"
        '  - "**/.env*"\n'
        "gemini_model: \"gemini-2.5-flash\"\n",
        encoding="utf-8",
    )
    return f


def test_load_config_parses_roots_and_env(tmp_path):
    allow = _write_allowlist(tmp_path)
    env = {
        "SCHOOLSWP_REPO_PATH": str(tmp_path),
        "OBSIDIAN_BRIDGE_PATH": str(tmp_path / "obsidian-bridge"),
        "GRAPHIFY_OUTPUT_PATH": str(tmp_path / "schoolswp-brain" / ".graphify"),
    }
    cfg = config.load_config(allow, env)
    assert cfg.repo_path == tmp_path
    assert cfg.output_path == tmp_path / "schoolswp-brain" / ".graphify"
    assert [r.path for r in cfg.roots] == ["core/", "docs/"]
    assert cfg.roots[0].backend == "offline"
    assert cfg.gemini_model == "gemini-2.5-flash"
    assert "**/.env*" in cfg.exclude


def test_load_config_defaults_output_under_repo(tmp_path):
    allow = _write_allowlist(tmp_path)
    env = {"SCHOOLSWP_REPO_PATH": str(tmp_path)}  # no output/obsidian set
    cfg = config.load_config(allow, env)
    assert cfg.output_path == tmp_path / "schoolswp-brain" / ".graphify"
    assert cfg.obsidian_bridge_path == tmp_path / "obsidian-bridge"
```

- [ ] **Step 2: Run test to verify it fails**

Run: `.venv/Scripts/python -m pytest schoolswp-brain/tools/graphify-brain/tests/test_config.py -v`
Expected: FAIL with `ModuleNotFoundError: No module named 'config'`

- [ ] **Step 3: Write `config.py`**

```python
"""Load the brain env + allowlist, and compile the .graphifyignore."""
from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path
from typing import Mapping

import yaml

DOC_GLOBS = ("*.md", "*.markdown", "*.mdx", "*.txt", "*.rst", "*.pdf")


@dataclass(frozen=True)
class Root:
    path: str          # repo-relative, trailing slash e.g. "core/"
    type: str          # "code" | "content"
    backend: str       # "offline" | "gemini" (governs markdown egress only)


@dataclass(frozen=True)
class BrainConfig:
    repo_path: Path
    obsidian_bridge_path: Path
    output_path: Path
    roots: list[Root]
    exclude: list[str] = field(default_factory=list)
    gemini_model: str = "gemini-2.5-flash"


def load_config(allowlist_file: Path, env: Mapping[str, str]) -> BrainConfig:
    data = yaml.safe_load(Path(allowlist_file).read_text(encoding="utf-8")) or {}
    repo = Path(env["SCHOOLSWP_REPO_PATH"]).resolve()
    obsidian = Path(env.get("OBSIDIAN_BRIDGE_PATH", str(repo / "obsidian-bridge"))).resolve()
    out = Path(env.get("GRAPHIFY_OUTPUT_PATH", str(repo / "schoolswp-brain" / ".graphify"))).resolve()
    roots = [Root(r["path"], r["type"], r["backend"]) for r in data.get("roots", [])]
    return BrainConfig(
        repo_path=repo,
        obsidian_bridge_path=obsidian,
        output_path=out,
        roots=roots,
        exclude=list(data.get("exclude", [])),
        gemini_model=data.get("gemini_model", "gemini-2.5-flash"),
    )
```

- [ ] **Step 4: Run test to verify it passes**

Run: `.venv/Scripts/python -m pytest schoolswp-brain/tools/graphify-brain/tests/test_config.py -v`
Expected: PASS (2 passed)

- [ ] **Step 5: Commit**

```bash
git add schoolswp-brain/tools/graphify-brain/config.py schoolswp-brain/tools/graphify-brain/tests/test_config.py
git commit -m "feat(brain): config loader for env + allowlist"
```

---

## Task 2: compile_graphifyignore (code-only vs full)

**Files:**

- Modify: `schoolswp-brain/tools/graphify-brain/config.py`
- Test: `schoolswp-brain/tools/graphify-brain/tests/test_config.py`

- [ ] **Step 1: Add the failing test**

```python
# append to tests/test_config.py
import config


def test_compile_graphifyignore_whitelists_roots_and_excludes(tmp_path):
    allow = _write_allowlist(tmp_path)
    cfg = config.load_config(allow, {"SCHOOLSWP_REPO_PATH": str(tmp_path)})
    full = config.compile_graphifyignore(cfg, mode="full")
    # whitelist style: ignore everything, then re-include each root
    assert full.splitlines()[0] == "*"
    assert "!core/" in full and "!core/**" in full
    assert "!docs/" in full and "!docs/**" in full
    assert "**/.env*" in full  # exclude still applied (re-ignored after whitelist)


def test_compile_graphifyignore_code_only_excludes_markdown(tmp_path):
    allow = _write_allowlist(tmp_path)
    cfg = config.load_config(allow, {"SCHOOLSWP_REPO_PATH": str(tmp_path)})
    code = config.compile_graphifyignore(cfg, mode="code-only")
    # in code-only mode, doc globs are re-ignored so graphify stays offline
    assert "*.md" in code
    assert "*.pdf" in code
```

- [ ] **Step 2: Run test to verify it fails**

Run: `.venv/Scripts/python -m pytest schoolswp-brain/tools/graphify-brain/tests/test_config.py -k graphifyignore -v`
Expected: FAIL with `AttributeError: module 'config' has no attribute 'compile_graphifyignore'`

- [ ] **Step 3: Implement `compile_graphifyignore` in `config.py`**

```python
def compile_graphifyignore(cfg: BrainConfig, mode: str) -> str:
    """Whitelist-style .graphifyignore.

    mode="full": index all allowlisted roots (code + markdown).
    mode="code-only": same roots, but re-ignore doc globs so graphify needs no LLM.
    """
    if mode not in ("full", "code-only"):
        raise ValueError(f"unknown mode: {mode}")
    lines = ["# AUTO-GENERATED by graphify-brain. Do not edit by hand.", "*"]
    for r in cfg.roots:
        p = r.path.rstrip("/")
        lines.append(f"!{p}/")
        lines.append(f"!{p}/**")
    # re-ignore the global excludes (after the whitelist, so they win)
    lines.extend(cfg.exclude)
    if mode == "code-only":
        lines.extend(DOC_GLOBS)
    return "\n".join(lines) + "\n"
```

- [ ] **Step 4: Run test to verify it passes**

Run: `.venv/Scripts/python -m pytest schoolswp-brain/tools/graphify-brain/tests/test_config.py -v`
Expected: PASS (4 passed)

- [ ] **Step 5: Commit**

```bash
git add schoolswp-brain/tools/graphify-brain/config.py schoolswp-brain/tools/graphify-brain/tests/test_config.py
git commit -m "feat(brain): compile whitelist .graphifyignore (code-only / full)"
```

---

## Task 3: md_local_index.py - local markdown scan

**Files:**

- Create: `schoolswp-brain/tools/graphify-brain/md_local_index.py`
- Test: `schoolswp-brain/tools/graphify-brain/tests/test_md_local_index.py`

- [ ] **Step 1: Write the failing test**

```python
# tests/test_md_local_index.py
import md_local_index as mli


SAMPLE = """---
title: Avis DataForSEO
tags: [seo, api]
---

# Titre principal

Voir [[autre-note]] et [[cluster-securite]].

## Sous-section

Texte avec #wordpress et #seo.
"""


def test_scan_markdown_file_extracts_structure(tmp_path):
    f = tmp_path / "note.md"
    f.write_text(SAMPLE, encoding="utf-8")
    doc = mli.scan_markdown_file(f)
    assert doc.title == "Titre principal"
    assert "Sous-section" in doc.headings
    assert "autre-note" in doc.wikilinks
    assert "cluster-securite" in doc.wikilinks
    assert "wordpress" in doc.tags
    assert doc.frontmatter.get("tags") == ["seo", "api"]


def test_scan_tree_respects_exclude(tmp_path):
    (tmp_path / "keep.md").write_text("# Keep", encoding="utf-8")
    drafts = tmp_path / "_drafts"
    drafts.mkdir()
    (drafts / "skip.md").write_text("# Skip", encoding="utf-8")
    docs = mli.scan_tree(tmp_path, exclude=["**/_drafts/**"])
    paths = [d.path for d in docs]
    assert any(p.endswith("keep.md") for p in paths)
    assert not any("skip.md" in p for p in paths)
```

- [ ] **Step 2: Run test to verify it fails**

Run: `.venv/Scripts/python -m pytest schoolswp-brain/tools/graphify-brain/tests/test_md_local_index.py -v`
Expected: FAIL with `ModuleNotFoundError: No module named 'md_local_index'`

- [ ] **Step 3: Write `md_local_index.py`**

```python
"""Local, LLM-free structural scan of markdown: title, headings, [[links]], #tags, frontmatter."""
from __future__ import annotations

import fnmatch
import re
from dataclasses import dataclass, field
from pathlib import Path

import yaml

_HEADING = re.compile(r"^(#{1,6})\s+(.*?)\s*#*\s*$", re.MULTILINE)
_WIKILINK = re.compile(r"\[\[([^\]|#]+)")
_TAG = re.compile(r"(?:^|\s)#([A-Za-z0-9_\-/]+)")
_FRONTMATTER = re.compile(r"^---\n(.*?)\n---\n", re.DOTALL)


@dataclass
class MdDoc:
    path: str
    title: str | None
    headings: list[str] = field(default_factory=list)
    wikilinks: list[str] = field(default_factory=list)
    tags: list[str] = field(default_factory=list)
    frontmatter: dict = field(default_factory=dict)


def scan_markdown_file(path: Path) -> MdDoc:
    text = Path(path).read_text(encoding="utf-8", errors="replace")
    frontmatter: dict = {}
    m = _FRONTMATTER.match(text)
    if m:
        try:
            frontmatter = yaml.safe_load(m.group(1)) or {}
        except yaml.YAMLError:
            frontmatter = {}
        body = text[m.end():]
    else:
        body = text
    headings = [h[1] for h in _HEADING.findall(body)]
    title = frontmatter.get("title") or (headings[0] if headings else None)
    body_headings = headings[1:] if (title and headings and headings[0] == title) else headings
    wikilinks = [w.strip() for w in _WIKILINK.findall(body)]
    tags = sorted({t for t in _TAG.findall(body)})
    return MdDoc(
        path=str(path),
        title=title,
        headings=body_headings,
        wikilinks=wikilinks,
        tags=tags,
        frontmatter=frontmatter if isinstance(frontmatter, dict) else {},
    )


def _excluded(rel: str, exclude: list[str]) -> bool:
    rel = rel.replace("\\", "/")
    return any(fnmatch.fnmatch(rel, pat) or fnmatch.fnmatch(rel, pat.rstrip("/*") + "/*") for pat in exclude)


def scan_tree(root: Path, exclude: list[str]) -> list[MdDoc]:
    root = Path(root)
    docs: list[MdDoc] = []
    for p in sorted(root.rglob("*.md")):
        rel = str(p.relative_to(root)).replace("\\", "/")
        if _excluded(rel, exclude):
            continue
        docs.append(scan_markdown_file(p))
    return docs
```

- [ ] **Step 4: Run test to verify it passes**

Run: `.venv/Scripts/python -m pytest schoolswp-brain/tools/graphify-brain/tests/test_md_local_index.py -v`
Expected: PASS (2 passed)

- [ ] **Step 5: Commit**

```bash
git add schoolswp-brain/tools/graphify-brain/md_local_index.py schoolswp-brain/tools/graphify-brain/tests/test_md_local_index.py
git commit -m "feat(brain): local markdown structural index (no LLM)"
```

---

## Task 4: changes.py - changed files + local/egress split

**Files:**

- Create: `schoolswp-brain/tools/graphify-brain/changes.py`
- Test: `schoolswp-brain/tools/graphify-brain/tests/test_changes.py`

- [ ] **Step 1: Write the failing test** (uses a real throwaway git repo)

```python
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
    (repo / "core" / "a.py").write_text("x = 2\n", encoding="utf-8")   # modified
    (repo / "docs" / "new.md").write_text("# New\n", encoding="utf-8")  # new (untracked)
    cs = changes.changed_files(repo, since_commit=base, roots=ROOTS, exclude=[])
    assert any(p.endswith("a.py") for p in cs.modified)
    assert any(p.endswith("new.md") for p in cs.new)


def test_split_local_vs_egress(tmp_path):
    repo = _init_repo(tmp_path)
    cs = changes.ChangedSet(new=["docs/new.md", "core/b.py"], modified=["core/a.py", "docs/g.md"])
    local, egress = changes.split_local_vs_egress(cs, ROOTS)
    assert "core/a.py" in local and "core/b.py" in local
    assert "docs/new.md" in egress and "docs/g.md" in egress
    assert "docs/new.md" not in local
```

- [ ] **Step 2: Run test to verify it fails**

Run: `.venv/Scripts/python -m pytest schoolswp-brain/tools/graphify-brain/tests/test_changes.py -v`
Expected: FAIL with `ModuleNotFoundError: No module named 'changes'`

- [ ] **Step 3: Write `changes.py`**

```python
"""Detect files changed since the last indexed commit, intersected with the allowlist."""
from __future__ import annotations

import fnmatch
import subprocess
from dataclasses import dataclass, field
from pathlib import Path

from config import Root

DOC_EXT = (".md", ".markdown", ".mdx", ".txt", ".rst", ".pdf")


@dataclass
class ChangedSet:
    new: list[str] = field(default_factory=list)
    modified: list[str] = field(default_factory=list)


def _in_roots(rel: str, roots: list[Root]) -> bool:
    return any(rel.startswith(r.path) for r in roots)


def _excluded(rel: str, exclude: list[str]) -> bool:
    return any(fnmatch.fnmatch(rel, pat) for pat in exclude)


def _git(repo: Path, *args: str) -> str:
    return subprocess.run(["git", *args], cwd=repo, capture_output=True, text=True, check=True).stdout


def changed_files(repo: Path, since_commit: str | None, roots: list[Root], exclude: list[str]) -> ChangedSet:
    repo = Path(repo)
    cs = ChangedSet()
    if since_commit:
        # committed + working-tree changes vs the indexed commit
        out = _git(repo, "diff", "--name-status", since_commit)
        for line in out.splitlines():
            parts = line.split("\t")
            if len(parts) < 2:
                continue
            status, rel = parts[0], parts[-1].replace("\\", "/")
            if not _in_roots(rel, roots) or _excluded(rel, exclude):
                continue
            (cs.new if status.startswith("A") else cs.modified).append(rel)
    # untracked files (always "new")
    for rel in _git(repo, "ls-files", "--others", "--exclude-standard").splitlines():
        rel = rel.replace("\\", "/")
        if _in_roots(rel, roots) and not _excluded(rel, exclude):
            cs.new.append(rel)
    if since_commit is None:
        # first run: everything tracked under roots counts as new
        for rel in _git(repo, "ls-files").splitlines():
            rel = rel.replace("\\", "/")
            if _in_roots(rel, roots) and not _excluded(rel, exclude):
                cs.new.append(rel)
    cs.new = sorted(set(cs.new))
    cs.modified = sorted(set(cs.modified))
    return cs


def split_local_vs_egress(changed: ChangedSet, roots: list[Root]) -> tuple[list[str], list[str]]:
    """Code files -> local (always). Markdown under a gemini root -> egress."""
    gemini_roots = [r.path for r in roots if r.backend == "gemini"]
    local: list[str] = []
    egress: list[str] = []
    for rel in sorted(set(changed.new) | set(changed.modified)):
        is_doc = rel.lower().endswith(DOC_EXT)
        under_gemini = any(rel.startswith(p) for p in gemini_roots)
        if is_doc and under_gemini:
            egress.append(rel)
        else:
            local.append(rel)
    return local, egress
```

- [ ] **Step 4: Run test to verify it passes**

Run: `.venv/Scripts/python -m pytest schoolswp-brain/tools/graphify-brain/tests/test_changes.py -v`
Expected: PASS (2 passed)

- [ ] **Step 5: Commit**

```bash
git add schoolswp-brain/tools/graphify-brain/changes.py schoolswp-brain/tools/graphify-brain/tests/test_changes.py
git commit -m "feat(brain): changed-files detection + local/egress split"
```

---

## Task 5: secrets_scan.py - pre-send secret scan

**Files:**

- Create: `schoolswp-brain/tools/graphify-brain/secrets_scan.py`
- Test: `schoolswp-brain/tools/graphify-brain/tests/test_secrets_scan.py`

- [ ] **Step 1: Write the failing test**

```python
# tests/test_secrets_scan.py
import secrets_scan


def test_detects_private_key_and_api_keys(tmp_path):
    clean = tmp_path / "clean.md"
    clean.write_text("# Article propre, aucun secret.\n", encoding="utf-8")
    leak = tmp_path / "leak.md"
    leak.write_text(
        "intro\n"
        "GEMINI_API_KEY=AIzaSyABCDEF1234567890abcdefABCDEF12345\n"
        "-----BEGIN PRIVATE KEY-----\n",
        encoding="utf-8",
    )
    hits = secrets_scan.scan_files([clean, leak])
    leaked_paths = {h.path for h in hits}
    assert str(leak) in leaked_paths
    assert str(clean) not in leaked_paths
    assert len(hits) >= 2  # api key + PEM header


def test_clean_set_returns_no_hits(tmp_path):
    f = tmp_path / "ok.md"
    f.write_text("Juste un article sur WordPress.\n", encoding="utf-8")
    assert secrets_scan.scan_files([f]) == []
```

- [ ] **Step 2: Run test to verify it fails**

Run: `.venv/Scripts/python -m pytest schoolswp-brain/tools/graphify-brain/tests/test_secrets_scan.py -v`
Expected: FAIL with `ModuleNotFoundError: No module named 'secrets_scan'`

- [ ] **Step 3: Write `secrets_scan.py`**

```python
"""Defense-in-depth scan: refuse to send a file set that looks like it contains secrets."""
from __future__ import annotations

import re
from dataclasses import dataclass
from pathlib import Path

PATTERNS: list[tuple[str, re.Pattern]] = [
    ("pem-private-key", re.compile(r"-----BEGIN [A-Z ]*PRIVATE KEY-----")),
    ("google-api-key", re.compile(r"AIza[0-9A-Za-z\-_]{35}")),
    ("openai-key", re.compile(r"sk-[A-Za-z0-9]{20,}")),
    ("aws-access-key", re.compile(r"AKIA[0-9A-Z]{16}")),
    ("slack-token", re.compile(r"xox[baprs]-[0-9A-Za-z\-]{10,}")),
    ("github-pat", re.compile(r"ghp_[0-9A-Za-z]{36}")),
    ("assigned-secret", re.compile(r"(?i)(api[_-]?key|secret|token|password)\s*[:=]\s*['\"]?[A-Za-z0-9/\+_\-]{16,}")),
]


@dataclass
class SecretHit:
    path: str
    line: int
    pattern: str


def scan_files(paths: list[Path]) -> list[SecretHit]:
    hits: list[SecretHit] = []
    for p in paths:
        try:
            lines = Path(p).read_text(encoding="utf-8", errors="replace").splitlines()
        except OSError:
            continue
        for i, line in enumerate(lines, start=1):
            for name, rx in PATTERNS:
                if rx.search(line):
                    hits.append(SecretHit(path=str(p), line=i, pattern=name))
    return hits
```

- [ ] **Step 4: Run test to verify it passes**

Run: `.venv/Scripts/python -m pytest schoolswp-brain/tools/graphify-brain/tests/test_secrets_scan.py -v`
Expected: PASS (2 passed)

- [ ] **Step 5: Commit**

```bash
git add schoolswp-brain/tools/graphify-brain/secrets_scan.py schoolswp-brain/tools/graphify-brain/tests/test_secrets_scan.py
git commit -m "feat(brain): pre-send secret scan"
```

---

## Task 6: cost.py - token/cost heuristic

**Files:**

- Create: `schoolswp-brain/tools/graphify-brain/cost.py`
- Test: `schoolswp-brain/tools/graphify-brain/tests/test_cost.py`

- [ ] **Step 1: Write the failing test**

```python
# tests/test_cost.py
import cost


def test_estimate_counts_chars_tokens_and_usd(tmp_path):
    a = tmp_path / "a.md"
    a.write_text("x" * 4000, encoding="utf-8")  # ~1000 tokens
    b = tmp_path / "b.md"
    b.write_text("y" * 4000, encoding="utf-8")
    est = cost.estimate([a, b], model="gemini-2.5-flash")
    assert est.files == 2
    assert est.total_chars == 8000
    assert est.est_tokens == 2000  # chars // 4
    assert est.est_usd > 0


def test_estimate_empty_is_zero():
    est = cost.estimate([], model="gemini-2.5-flash")
    assert est.files == 0 and est.est_tokens == 0 and est.est_usd == 0.0
```

- [ ] **Step 2: Run test to verify it fails**

Run: `.venv/Scripts/python -m pytest schoolswp-brain/tools/graphify-brain/tests/test_cost.py -v`
Expected: FAIL with `ModuleNotFoundError: No module named 'cost'`

- [ ] **Step 3: Write `cost.py`**

```python
"""Heuristic token + USD estimate for a set of files about to reach Gemini.

Pricing is approximate input-token pricing; update PRICE_PER_MTOK_USD as needed.
The real cost is captured later (phase 2); this is a guardrail estimate only.
"""
from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

CHARS_PER_TOKEN = 4
PRICE_PER_MTOK_USD = {
    "gemini-2.5-flash": 0.30,   # approx input price; adjust to billing reality
    "gemini-2.5-pro": 1.25,
}
DEFAULT_PRICE = 0.30


@dataclass
class CostEstimate:
    files: int
    total_chars: int
    est_tokens: int
    est_usd: float


def estimate(paths: list[Path], model: str) -> CostEstimate:
    total_chars = 0
    n = 0
    for p in paths:
        try:
            total_chars += len(Path(p).read_text(encoding="utf-8", errors="replace"))
            n += 1
        except OSError:
            continue
    est_tokens = total_chars // CHARS_PER_TOKEN
    price = PRICE_PER_MTOK_USD.get(model, DEFAULT_PRICE)
    est_usd = round(est_tokens / 1_000_000 * price, 4)
    return CostEstimate(files=n, total_chars=total_chars, est_tokens=est_tokens, est_usd=est_usd)
```

- [ ] **Step 4: Run test to verify it passes**

Run: `.venv/Scripts/python -m pytest schoolswp-brain/tools/graphify-brain/tests/test_cost.py -v`
Expected: PASS (2 passed)

- [ ] **Step 5: Commit**

```bash
git add schoolswp-brain/tools/graphify-brain/cost.py schoolswp-brain/tools/graphify-brain/tests/test_cost.py
git commit -m "feat(brain): heuristic token/cost estimate"
```

---

## Task 7: logbook.py - refresh log + state

**Files:**

- Create: `schoolswp-brain/tools/graphify-brain/logbook.py`
- Test: `schoolswp-brain/tools/graphify-brain/tests/test_logbook.py`

- [ ] **Step 1: Write the failing test**

```python
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
```

- [ ] **Step 2: Run test to verify it fails**

Run: `.venv/Scripts/python -m pytest schoolswp-brain/tools/graphify-brain/tests/test_logbook.py -v`
Expected: FAIL with `ModuleNotFoundError: No module named 'logbook'`

- [ ] **Step 3: Write `logbook.py`**

```python
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
    Path(state_file).write_text(
        json.dumps({"last_indexed_commit": commit}, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
```

- [ ] **Step 4: Run test to verify it passes**

Run: `.venv/Scripts/python -m pytest schoolswp-brain/tools/graphify-brain/tests/test_logbook.py -v`
Expected: PASS (2 passed)

- [ ] **Step 5: Commit**

```bash
git add schoolswp-brain/tools/graphify-brain/logbook.py schoolswp-brain/tools/graphify-brain/tests/test_logbook.py
git commit -m "feat(brain): refresh log (jsonl) + state file"
```

---

## Task 8: graphify_runner.py - subprocess wrappers

**Files:**

- Create: `schoolswp-brain/tools/graphify-brain/graphify_runner.py`
- Test: `schoolswp-brain/tools/graphify-brain/tests/test_graphify_runner.py`

The key safety property (testable without graphify installed): the OFFLINE runner must strip every LLM key from the child env, and the GEMINI runner must keep the key. We test the env construction, not the real subprocess.

- [ ] **Step 1: Write the failing test**

```python
# tests/test_graphify_runner.py
import graphify_runner as gr

LLM_KEYS = ["GEMINI_API_KEY", "GOOGLE_API_KEY", "OPENAI_API_KEY", "ANTHROPIC_API_KEY", "OLLAMA_HOST"]


def test_offline_env_strips_all_llm_keys():
    base = {k: "secret" for k in LLM_KEYS} | {"PATH": "/usr/bin"}
    env = gr.offline_env(base)
    for k in LLM_KEYS:
        assert k not in env
    assert env["PATH"] == "/usr/bin"


def test_gemini_env_keeps_key():
    base = {"GEMINI_API_KEY": "secret", "PATH": "/usr/bin"}
    env = gr.gemini_env(base)
    assert env["GEMINI_API_KEY"] == "secret"
```

- [ ] **Step 2: Run test to verify it fails**

Run: `.venv/Scripts/python -m pytest schoolswp-brain/tools/graphify-brain/tests/test_graphify_runner.py -v`
Expected: FAIL with `ModuleNotFoundError: No module named 'graphify_runner'`

- [ ] **Step 3: Write `graphify_runner.py`**

```python
"""Thin subprocess wrappers around the graphify CLI, with explicit egress control."""
from __future__ import annotations

import subprocess
from pathlib import Path
from typing import Mapping

LLM_KEYS = (
    "GEMINI_API_KEY", "GOOGLE_API_KEY", "OPENAI_API_KEY", "ANTHROPIC_API_KEY",
    "DEEPSEEK_API_KEY", "KIMI_API_KEY", "MOONSHOT_API_KEY", "OLLAMA_HOST",
    "OPENAI_BASE_URL", "ANTHROPIC_BASE_URL",
)


def offline_env(base: Mapping[str, str]) -> dict:
    env = dict(base)
    for k in LLM_KEYS:
        env.pop(k, None)
    return env


def gemini_env(base: Mapping[str, str]) -> dict:
    return dict(base)


def _run(args: list[str], env: dict) -> subprocess.CompletedProcess:
    return subprocess.run(args, env=env, capture_output=True, text=True)


def run_extract(repo: Path, out: Path, env: dict) -> subprocess.CompletedProcess:
    return _run(["graphify", "extract", str(repo), "--out", str(out)], env)


def run_cluster(out: Path, env: dict, *, label: bool, backend: str | None, model: str | None) -> subprocess.CompletedProcess:
    args = ["graphify", "cluster-only", str(out)]
    if not label:
        args.append("--no-label")
    if backend:
        args.append(f"--backend={backend}")
    if model:
        args.append(f"--model={model}")
    return _run(args, env)


def run_query(graph: Path, question: str, env: dict) -> str:
    return _run(["graphify", "query", question, "--graph", str(graph)], env).stdout


def run_explain(graph: Path, node: str, env: dict) -> str:
    return _run(["graphify", "explain", node, "--graph", str(graph)], env).stdout


def run_path(graph: Path, a: str, b: str, env: dict) -> str:
    return _run(["graphify", "path", a, b, "--graph", str(graph)], env).stdout
```

- [ ] **Step 4: Run test to verify it passes**

Run: `.venv/Scripts/python -m pytest schoolswp-brain/tools/graphify-brain/tests/test_graphify_runner.py -v`
Expected: PASS (2 passed)

- [ ] **Step 5: Commit**

```bash
git add schoolswp-brain/tools/graphify-brain/graphify_runner.py schoolswp-brain/tools/graphify-brain/tests/test_graphify_runner.py
git commit -m "feat(brain): graphify subprocess wrappers with egress-controlled env"
```

---

## Task 9: brain.py - CLI + the GO gate

**Files:**

- Create: `schoolswp-brain/tools/graphify-brain/brain.py`
- Test: `schoolswp-brain/tools/graphify-brain/tests/test_brain_cli.py`

Wires everything. The critical, testable safety property: `refresh --gemini` WITHOUT `--yes` must NEVER call the gemini runner. We inject a fake runner to assert this.

- [ ] **Step 1: Write the failing test**

```python
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
        "roots:\n"
        "  - { path: docs/, type: content, backend: gemini }\n"
        "exclude: []\n"
        'gemini_model: "gemini-2.5-flash"\n',
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
    monkeypatch.setattr(brain.graphify_runner, "run_cluster",
                        lambda *a, **k: calls.__setitem__("gemini", calls["gemini"] + 1))
    rc = brain.main(["refresh", "--gemini", "--allowlist", str(tmp_path / "allowlist.yml")], env=env)
    assert rc != 0                 # refused
    assert calls["gemini"] == 0    # nothing sent


def test_dry_run_reports_and_sends_nothing(tmp_path, capsys, monkeypatch):
    env = _setup(tmp_path)
    monkeypatch.setattr(brain.graphify_runner, "run_extract",
                        lambda *a, **k: (_ for _ in ()).throw(AssertionError("must not run")))
    rc = brain.main(["refresh", "--changed", "--dry-run", "--allowlist", str(tmp_path / "allowlist.yml")], env=env)
    out = capsys.readouterr().out
    assert rc == 0
    assert "DRY-RUN" in out
    assert "Gemini" in out  # egress section present
```

- [ ] **Step 2: Run test to verify it fails**

Run: `.venv/Scripts/python -m pytest schoolswp-brain/tools/graphify-brain/tests/test_brain_cli.py -v`
Expected: FAIL with `ModuleNotFoundError: No module named 'brain'`

- [ ] **Step 3: Write `brain.py`**

```python
"""graphify-brain CLI: the guardrail wrapper. graphify maps; schoolsWP decides."""
from __future__ import annotations

import argparse
import os
import sys
import json
import subprocess
from dataclasses import asdict
from datetime import datetime, timezone
from pathlib import Path

import changes
import config
import cost
import graphify_runner
import logbook
import md_local_index
import secrets_scan

DEFAULT_ALLOWLIST = Path(__file__).resolve().parent / "allowlist.yml"


def _now() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="seconds")


def _head(repo: Path) -> str:
    out = subprocess.run(["git", "rev-parse", "HEAD"], cwd=repo, capture_output=True, text=True, check=True)
    return out.stdout.strip()


def _state_file(cfg: config.BrainConfig) -> Path:
    return cfg.repo_path / "schoolswp-brain" / "07_graph" / ".brain-state.json"


def _log_dir(cfg: config.BrainConfig) -> Path:
    return cfg.repo_path / "schoolswp-brain" / "07_graph" / "logs"


def _dry_run(cfg: config.BrainConfig, env: dict) -> tuple[list[str], list[str], cost.CostEstimate]:
    since = logbook.read_state(_state_file(cfg)).get("last_indexed_commit")
    cs = changes.changed_files(cfg.repo_path, since, cfg.roots, cfg.exclude)
    local, egress = changes.split_local_vs_egress(cs, cfg.roots)
    est = cost.estimate([cfg.repo_path / p for p in egress], cfg.gemini_model)
    print("=== DRY-RUN (nothing is sent) ===")
    print(f"new: {len(cs.new)}  modified: {len(cs.modified)}")
    print(f"stays LOCAL (code AST + md structural): {len(local)} file(s)")
    print(f"would go to Gemini ({cfg.gemini_model}): {len(egress)} file(s)")
    for p in egress:
        print(f"  -> {p}")
    print(f"est. tokens: {est.est_tokens}  est. cost: ${est.est_usd}")
    return local, egress, est


def cmd_refresh(args, cfg: config.BrainConfig, env: dict) -> int:
    if args.dry_run:
        _dry_run(cfg, env)
        return 0

    if args.local:
        # Couche 1: code AST offline. Couche 2: local markdown structural index (no LLM).
        ignore = config.compile_graphifyignore(cfg, mode="code-only")
        (cfg.repo_path / ".graphifyignore").write_text(ignore, encoding="utf-8")
        oenv = graphify_runner.offline_env(env)
        graphify_runner.run_extract(cfg.repo_path, cfg.output_path, oenv)
        graphify_runner.run_cluster(cfg.output_path, oenv, label=False, backend=None, model=None)
        docs = []
        for r in cfg.roots:
            root_dir = cfg.repo_path / r.path
            if root_dir.exists():
                docs.extend(md_local_index.scan_tree(root_dir, cfg.exclude))
        cfg.output_path.mkdir(parents=True, exist_ok=True)
        (cfg.output_path / "md-local-index.json").write_text(
            json.dumps([asdict(d) for d in docs], ensure_ascii=False, indent=2), encoding="utf-8")
        commit = _head(cfg.repo_path)
        logbook.write_state(_state_file(cfg), commit)
        logbook.append_log(_log_dir(cfg), logbook.RefreshLogEntry(
            date=_now(), command="refresh --local", files_analyzed=len(docs), files_sent=0,
            model=None, est_cost_usd=0.0, real_cost_usd=0.0, result="ok"))
        print(f"refresh --local done (offline, 0 egress; {len(docs)} md docs structurally indexed).")
        return 0

    if args.gemini:
        local, egress, est = _dry_run(cfg, env)
        if not args.yes:
            print("\nREFUSED: refresh --gemini requires explicit --yes after reviewing the dry-run.", file=sys.stderr)
            return 2
        hits = secrets_scan.scan_files([cfg.repo_path / p for p in egress])
        if hits:
            for h in hits:
                print(f"SECRET? {h.path}:{h.line} [{h.pattern}]", file=sys.stderr)
            print("ABORTED: secret-looking content in the egress set.", file=sys.stderr)
            return 3
        ignore = config.compile_graphifyignore(cfg, mode="full")
        (cfg.repo_path / ".graphifyignore").write_text(ignore, encoding="utf-8")
        genv = graphify_runner.gemini_env(env)
        graphify_runner.run_extract(cfg.repo_path, cfg.output_path, genv)
        graphify_runner.run_cluster(cfg.output_path, genv, label=True, backend="gemini", model=cfg.gemini_model)
        commit = _head(cfg.repo_path)
        logbook.write_state(_state_file(cfg), commit)
        logbook.append_log(_log_dir(cfg), logbook.RefreshLogEntry(
            date=_now(), command="refresh --gemini", files_analyzed=len(local) + len(egress),
            files_sent=len(egress), model=cfg.gemini_model, est_cost_usd=est.est_usd,
            real_cost_usd=None, result="ok"))
        print(f"refresh --gemini done ({len(egress)} file(s) sent to {cfg.gemini_model}).")
        return 0

    print("nothing to do: pass --local, --changed --dry-run, or --gemini --yes", file=sys.stderr)
    return 1


def _graph_path(cfg: config.BrainConfig) -> Path:
    return cfg.output_path / "graphify-out" / "graph.json"


def cmd_query(args, cfg, env):
    print(graphify_runner.run_query(_graph_path(cfg), args.question, env)); return 0


def cmd_explain(args, cfg, env):
    print(graphify_runner.run_explain(_graph_path(cfg), args.node, env)); return 0


def cmd_path(args, cfg, env):
    print(graphify_runner.run_path(_graph_path(cfg), args.a, args.b, env)); return 0


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(prog="brain", description="schoolsWP second brain (graphify wrapper)")
    p.add_argument("--allowlist", default=str(DEFAULT_ALLOWLIST))
    sub = p.add_subparsers(dest="cmd", required=True)

    r = sub.add_parser("refresh")
    r.add_argument("--local", action="store_true")
    r.add_argument("--changed", action="store_true")
    r.add_argument("--dry-run", action="store_true")
    r.add_argument("--gemini", action="store_true")
    r.add_argument("--yes", action="store_true")
    r.set_defaults(func=cmd_refresh)

    q = sub.add_parser("query"); q.add_argument("question"); q.set_defaults(func=cmd_query)
    e = sub.add_parser("explain"); e.add_argument("node"); e.set_defaults(func=cmd_explain)
    pa = sub.add_parser("path"); pa.add_argument("a"); pa.add_argument("b"); pa.set_defaults(func=cmd_path)
    return p


def main(argv: list[str] | None = None, env: dict | None = None) -> int:
    env = dict(env if env is not None else os.environ)
    args = build_parser().parse_args(argv)
    cfg = config.load_config(Path(args.allowlist), env)
    return args.func(args, cfg, env)


if __name__ == "__main__":
    raise SystemExit(main())
```

- [ ] **Step 4: Run test to verify it passes**

Run: `.venv/Scripts/python -m pytest schoolswp-brain/tools/graphify-brain/tests/test_brain_cli.py -v`
Expected: PASS (2 passed)

- [ ] **Step 5: Run the full suite + ruff**

Run: `.venv/Scripts/python -m pytest schoolswp-brain/tools/graphify-brain/tests/ -v && .venv/Scripts/python -m ruff check schoolswp-brain/tools/graphify-brain/`
Expected: all green; ruff clean (fix any line-length/import issues inline).

- [ ] **Step 6: Commit**

```bash
git add schoolswp-brain/tools/graphify-brain/brain.py schoolswp-brain/tools/graphify-brain/tests/test_brain_cli.py
git commit -m "feat(brain): CLI with mandatory dry-run + GO gate + secret-scan abort"
```

---

## Task 10: Offline-real test + first curated graph (acceptance)

**Files:**

- Test: `schoolswp-brain/tools/graphify-brain/tests/test_brain_cli.py` (add one integration test)

- [ ] **Step 1: Add the offline-real integration test (skips if graphify missing)**

```python
# append to tests/test_brain_cli.py
import shutil

import pytest


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
    env = {"SCHOOLSWP_REPO_PATH": str(repo),
           "GRAPHIFY_OUTPUT_PATH": str(repo / "schoolswp-brain" / ".graphify"),
           "GEMINI_API_KEY": "should-be-stripped", "PATH": __import__("os").environ["PATH"]}
    rc = brain.main(["refresh", "--local", "--allowlist", str(allow)], env=env)
    assert rc == 0
    report = repo / "schoolswp-brain" / ".graphify" / "graphify-out" / "GRAPH_REPORT.md"
    assert report.exists()
    assert "Token cost: 0 input" in report.read_text(encoding="utf-8")
```

- [ ] **Step 2: Run the integration test**

Run: `.venv/Scripts/python -m pytest schoolswp-brain/tools/graphify-brain/tests/test_brain_cli.py -k offline -v`
Expected: PASS (proves `refresh --local` is fully offline: keys stripped, token cost 0).

- [ ] **Step 3: First real curated graph (manual acceptance)**

```bash
# from repo root, with env set (SCHOOLSWP_REPO_PATH, GRAPHIFY_OUTPUT_PATH)
.venv/Scripts/python schoolswp-brain/tools/graphify-brain/brain.py refresh --local
.venv/Scripts/python schoolswp-brain/tools/graphify-brain/brain.py refresh --changed --dry-run
```

Manual check: open `schoolswp-brain/.graphify/graphify-out/graph.html`; confirm god nodes and code communities make sense, noise is tolerable. Review the dry-run output: confirm the egress list contains only expected markdown and the cost estimate is sane. Do NOT run `--gemini` yet unless you accept the egress.

- [ ] **Step 4: Commit the integration test + a short README**

Create `schoolswp-brain/tools/graphify-brain/README.md` documenting the 4 commands and the env vars, then:

```bash
git add schoolswp-brain/tools/graphify-brain/tests/test_brain_cli.py schoolswp-brain/tools/graphify-brain/README.md
git commit -m "test(brain): offline integration test + usage README"
```

---

## Definition of Done (maps to spec section 10)

1. `refresh --gemini` without `--yes` sends nothing (test_brain_cli: `test_gemini_without_yes_sends_nothing`).
2. Nothing outside allowlist + secret scan blocks egress (test_config whitelist + test_secrets_scan + brain abort path).
3. `--changed` detects new/modified since last indexed commit (test_changes).
4. Every refresh writes a log line (test_logbook + brain refresh paths).
5. `refresh --local` is 100% offline, token cost 0 (test_brain_cli: `test_refresh_local_runs_offline_zero_token_cost`).
6. First curated graph is useful (Task 10 Step 3, manual acceptance).
