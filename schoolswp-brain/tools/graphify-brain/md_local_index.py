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


def is_excluded(rel: str, exclude: list[str]) -> bool:
    """gitignore-ish matcher for the patterns used by the allowlist excludes."""
    rel = rel.replace("\\", "/")
    segments = rel.split("/")
    base = segments[-1]
    for raw in exclude:
        pat = raw.replace("\\", "/")
        if pat.startswith("**/") and pat.endswith("/**"):
            d = pat[3:-3]
            if any(fnmatch.fnmatch(seg, d) for seg in segments[:-1]):
                return True
        elif pat.startswith("**/"):
            sub = pat[3:]
            if fnmatch.fnmatch(base, sub) or fnmatch.fnmatch(rel, sub):
                return True
        elif pat.endswith("/**"):
            pref = pat[:-3].split("/")
            if len(segments) > len(pref) and all(fnmatch.fnmatch(segments[i], pref[i]) for i in range(len(pref))):
                return True
        elif fnmatch.fnmatch(rel, pat) or fnmatch.fnmatch(base, pat):
            return True
    return False


def scan_markdown_file(path: Path) -> MdDoc:
    text = Path(path).read_text(encoding="utf-8", errors="replace")
    frontmatter: dict = {}
    m = _FRONTMATTER.match(text)
    if m:
        try:
            loaded = yaml.safe_load(m.group(1))
            frontmatter = loaded if isinstance(loaded, dict) else {}
        except yaml.YAMLError:
            frontmatter = {}
        body = text[m.end() :]
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
        frontmatter=frontmatter,
    )


def scan_tree(root: Path, exclude: list[str]) -> list[MdDoc]:
    root = Path(root)
    docs: list[MdDoc] = []
    for p in sorted(root.rglob("*.md")):
        rel = str(p.relative_to(root)).replace("\\", "/")
        if is_excluded(rel, exclude):
            continue
        docs.append(scan_markdown_file(p))
    return docs
