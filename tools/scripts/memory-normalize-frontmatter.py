#!/usr/bin/env python3
"""
Normalise les frontmatters des mémoires schoolsWP (dossier mémoire interne
Claude Code) au format canonique :

---
name: <filename-sans-.md>
description: <ligne unique préservée>
metadata:
  type: <user|feedback|project|reference|hardware>
  originSessionId: <si présent>
---

Met aussi à jour les wikilinks [[old_name]] -> [[new_name]] dans tous les corps
quand un name a changé.

Usage :
  python memory-normalize-frontmatter.py --dry-run
  python memory-normalize-frontmatter.py --apply
"""

from __future__ import annotations

import re
import shutil
import sys
from datetime import datetime
from pathlib import Path

MEMORY_DIR = Path(
    r"C:\Users\conta\.claude\projects\d--VS-Code-CLAUDE-CODE-projects-schoolswp\memory"
)
SKIP_FILES = {"MEMORY.md", "LOG.md"}
VALID_TYPES = {"user", "feedback", "project", "reference", "hardware"}


def parse_frontmatter(content: str):
    """Return (fm_dict, body_str). fm_dict supports one level of nesting."""
    if not content.startswith("---\n"):
        return None, content
    end = content.find("\n---\n", 4)
    if end == -1:
        return None, content
    fm_text = content[4:end]
    body = content[end + 5 :]

    fm: dict = {}
    current_block = None
    for raw in fm_text.split("\n"):
        if not raw.strip() or raw.lstrip().startswith("#"):
            continue
        is_indented = raw.startswith(" ") or raw.startswith("\t")
        if not is_indented:
            current_block = None
            if ":" not in raw:
                continue
            k, _, v = raw.partition(":")
            k = k.strip()
            v = v.strip()
            if not v:
                current_block = k
                fm[k] = {}
            else:
                fm[k] = _unquote(v)
        else:
            if current_block and ":" in raw:
                k, _, v = raw.partition(":")
                k = k.strip()
                v = v.strip()
                if isinstance(fm.get(current_block), dict):
                    fm[current_block][k] = _unquote(v)
    return fm, body


def _unquote(v: str) -> str:
    if len(v) >= 2 and v[0] == v[-1] and v[0] in ('"', "'"):
        inner = v[1:-1]
        if v[0] == '"':
            inner = _yaml_unescape_double(inner)
        elif v[0] == "'":
            inner = inner.replace("''", "'")
        return inner
    return v


def _yaml_unescape_double(s: str) -> str:
    """Decode YAML double-quoted escapes : \\\\ -> \\, \\" -> ", \\n -> newline, \\t -> tab."""
    out: list[str] = []
    i = 0
    while i < len(s):
        if s[i] == "\\" and i + 1 < len(s):
            n = s[i + 1]
            if n == "\\":
                out.append("\\")
                i += 2
                continue
            if n == '"':
                out.append('"')
                i += 2
                continue
            if n == "n":
                out.append("\n")
                i += 2
                continue
            if n == "t":
                out.append("\t")
                i += 2
                continue
        out.append(s[i])
        i += 1
    return "".join(out)


def _yaml_quote(v: str) -> str:
    """Quote a single-line string for YAML using double quotes."""
    escaped = v.replace("\\", "\\\\").replace('"', '\\"')
    return f'"{escaped}"'


def build_frontmatter(name: str, description: str, ftype: str, origin: str | None) -> str:
    lines = ["---", f"name: {name}", f"description: {_yaml_quote(description)}", "metadata:"]
    lines.append(f"  type: {ftype}")
    if origin:
        lines.append(f"  originSessionId: {origin}")
    lines.append("---")
    return "\n".join(lines) + "\n"


def extract_fields(fm: dict, path: Path):
    """Pull (old_name, description, ftype, origin) from the parsed frontmatter."""
    old_name = (fm.get("name") or "").strip() if isinstance(fm.get("name"), str) else ""
    description = (fm.get("description") or "").strip() if isinstance(fm.get("description"), str) else ""

    ftype = ""
    origin = ""
    meta = fm.get("metadata")
    if isinstance(meta, dict):
        ftype = (meta.get("type") or "").strip()
        origin = (meta.get("originSessionId") or "").strip()
    if not ftype and isinstance(fm.get("type"), str):
        ftype = fm["type"].strip()
    if not origin and isinstance(fm.get("originSessionId"), str):
        origin = fm["originSessionId"].strip()

    if ftype not in VALID_TYPES:
        prefix = path.stem.split("_")[0]
        if prefix in VALID_TYPES:
            ftype = prefix

    return old_name, description, ftype, (origin or None)


def main() -> int:
    apply = "--apply" in sys.argv
    files = sorted(p for p in MEMORY_DIR.glob("*.md") if p.name not in SKIP_FILES)
    print(f"Trouvé {len(files)} fichiers topic dans {MEMORY_DIR}")

    plans: list[tuple[Path, str, str, str, str]] = []  # path, old_name, new_name, new_fm, body
    skipped: list[tuple[Path, str]] = []

    for p in files:
        content = p.read_text(encoding="utf-8")
        fm, body = parse_frontmatter(content)
        if fm is None:
            skipped.append((p, "pas de frontmatter"))
            continue
        old_name, description, ftype, origin = extract_fields(fm, p)
        if not description:
            skipped.append((p, "description vide"))
            continue
        if ftype not in VALID_TYPES:
            skipped.append((p, f"type invalide: {ftype!r}"))
            continue
        new_name = p.stem
        new_fm = build_frontmatter(new_name, description, ftype, origin)
        plans.append((p, old_name, new_name, new_fm, body))

    name_changes = {old: new for _, old, new, _, _ in plans if old and old != new}
    print(f"\nFichiers à écrire : {len(plans)} / Sautés : {len(skipped)}")
    if skipped:
        print("Sautés :")
        for p, why in skipped:
            print(f"  - {p.name} : {why}")
    print(f"Changements de `name:` : {len(name_changes)}")

    # Compter les wikilinks impactés
    wiki_total = 0
    for old in name_changes:
        pat = re.compile(r"\[\[" + re.escape(old) + r"\]\]")
        for p in files:
            try:
                wiki_total += len(pat.findall(p.read_text(encoding="utf-8")))
            except Exception:
                pass
    print(f"Wikilinks à réécrire : {wiki_total}")

    if not apply:
        print("\nDRY-RUN — relancer avec --apply pour exécuter.")
        print("\nExemples de renommage :")
        for _, old, new, _, _ in plans[:10]:
            if old != new:
                print(f"  '{old}' -> '{new}'")
        return 0

    # Apply — compute target content first, write only if différent
    wiki_patterns = [
        (re.compile(r"\[\[" + re.escape(old) + r"\]\]"), f"[[{new}]]")
        for old, new in name_changes.items()
    ]

    changes: list[tuple[Path, bytes]] = []
    wiki_done = 0
    for path, _, _, new_fm, body in plans:
        new_body = body
        for pat, repl in wiki_patterns:
            new_body, n = pat.subn(repl, new_body)
            wiki_done += n
        if new_body and not new_body.startswith("\n"):
            new_body = "\n" + new_body
        target = (new_fm + new_body).encode("utf-8")
        current = path.read_bytes()
        if target != current:
            changes.append((path, target))

    if not changes:
        print("\nAucun drift détecté, pas de backup ni d'écriture.")
        return 0

    stamp = datetime.now().strftime("%Y-%m-%dT%H-%M-%S")
    backup = MEMORY_DIR.parent / f"memory-backup-{stamp}"
    print(f"\nBackup -> {backup}")
    shutil.copytree(MEMORY_DIR, backup)

    for path, target in changes:
        path.write_bytes(target)

    print(f"\n{len(changes)} fichiers écrits, {wiki_done} wikilinks mis à jour.")
    print(f"Backup conservé : {backup}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
