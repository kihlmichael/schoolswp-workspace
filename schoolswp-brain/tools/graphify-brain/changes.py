"""Detect files changed since the last indexed commit, intersected with the allowlist."""

from __future__ import annotations

import subprocess
from dataclasses import dataclass, field
from pathlib import Path

from config import Root
from md_local_index import is_excluded

DOC_EXT = (".md", ".markdown", ".mdx", ".txt", ".rst", ".pdf")


@dataclass
class ChangedSet:
    new: list[str] = field(default_factory=list)
    modified: list[str] = field(default_factory=list)


def _in_roots(rel: str, roots: list[Root]) -> bool:
    return any(rel.startswith(r.path) for r in roots)


def _git(repo: Path, *args: str) -> str:
    return subprocess.run(["git", *args], cwd=repo, capture_output=True, text=True, check=True).stdout


def changed_files(repo: Path, since_commit: str | None, roots: list[Root], exclude: list[str]) -> ChangedSet:
    repo = Path(repo)
    cs = ChangedSet()
    if since_commit:
        out = _git(repo, "diff", "--name-status", since_commit)
        for line in out.splitlines():
            parts = line.split("\t")
            if len(parts) < 2:
                continue
            status, rel = parts[0], parts[-1].replace("\\", "/")
            if not _in_roots(rel, roots) or is_excluded(rel, exclude):
                continue
            (cs.new if status.startswith("A") else cs.modified).append(rel)
    for rel in _git(repo, "ls-files", "--others", "--exclude-standard").splitlines():
        rel = rel.replace("\\", "/")
        if _in_roots(rel, roots) and not is_excluded(rel, exclude):
            cs.new.append(rel)
    if since_commit is None:
        for rel in _git(repo, "ls-files").splitlines():
            rel = rel.replace("\\", "/")
            if _in_roots(rel, roots) and not is_excluded(rel, exclude):
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


def gemini_corpus(repo: Path, roots: list[Root], exclude: list[str]) -> list[str]:
    """All doc/markdown files (repo-relative) under gemini-backed roots, excludes applied.

    This is what a --gemini refresh can egress: graphify re-processes the whole
    whitelisted markdown corpus and derives community summaries from the full graph,
    so egress accounting / secret scan / cost must cover this set, not just the git delta.
    """
    repo = Path(repo)
    out: list[str] = []
    for r in roots:
        if r.backend != "gemini":
            continue
        root_dir = repo / r.path
        if not root_dir.exists():
            continue
        for p in root_dir.rglob("*"):
            if not p.is_file() or p.suffix.lower() not in DOC_EXT:
                continue
            rel = str(p.relative_to(repo)).replace("\\", "/")
            if not is_excluded(rel, exclude):
                out.append(rel)
    return sorted(set(out))
