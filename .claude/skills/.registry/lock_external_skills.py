"""
Lock external skills — versionne par hash SHA-256 chaque skill importé d'un repo tiers.

Pattern inspiré de multica-ai/multica/skills-lock.json (volé le 2026-04-27 — voir reference_multica_skills_lock.md).

Usage:
  python lock_external_skills.py            # génère/met à jour external-skills-lock.json
  python lock_external_skills.py --check    # compare avec lockfile, reporte les drifts (exit 1 si drift)
  python lock_external_skills.py --diff     # comme --check, mais affiche le détail des fichiers modifiés
"""

import argparse
import hashlib
import json
import os
import sys
from datetime import datetime, timezone

SKILLS_ROOT = r"D:\VS Code\CLAUDE CODE\projects\schoolswp\.claude\skills"
LOCKFILE = os.path.join(SKILLS_ROOT, "external-skills-lock.json")

# Source GitHub par dossier external-* (à maintenir manuellement quand un nouveau import est fait)
SOURCES = {
    "external-antigravity": {"source": "sickn33/antigravity-awesome-skills", "source_type": "github"},
    "external-cc-design": {"source": "ZeroZ-lab/cc-design", "source_type": "github"},
    "external-design-systems": {"source": "nexu-io/open-design", "source_type": "github"},
    "external-ecc": {"source": "affaan-m/everything-claude-code", "source_type": "github"},
    "external-open-design": {"source": "nexu-io/open-design", "source_type": "github"},
    "external-hyperframes": {"source": "heygen-com/hyperframes", "source_type": "github"},
    "external-liveavatar": {"source": "heygen-com/liveavatar-web-sdk", "source_type": "github"},
    "external-obsidian": {"source": "kepano/obsidian-skills", "source_type": "github"},
    "external-video-use": {"source": "browser-use/video-use", "source_type": "github"},
}

# Fichiers et dossiers à ignorer dans le hash (artefacts locaux non versionnés upstream)
IGNORED = {".DS_Store", "Thumbs.db", ".env"}
IGNORED_DIRS = {
    "_to-delete",
    "_archive",
    ".registry",
    ".venv",
    "venv",
    "__pycache__",
    ".pytest_cache",
    ".mypy_cache",
    "node_modules",
    ".git",
}
IGNORED_SUFFIXES = (".pyc", ".egg-info")  # *.egg-info est un dir, géré dans la boucle


def find_skills(external_dir):
    """Retourne la liste des sous-dossiers qui contiennent un SKILL.md (ou s'il n'y en a pas, le dossier lui-même)."""
    skills = []
    for entry in sorted(os.listdir(external_dir)):
        if entry in IGNORED_DIRS:
            continue
        path = os.path.join(external_dir, entry)
        if not os.path.isdir(path):
            continue
        # un skill = un dossier avec SKILL.md à la racine
        if os.path.isfile(os.path.join(path, "SKILL.md")):
            skills.append((entry, path))
    # cas de dossier external-* sans sous-skill (ex: external-cc-design où SKILL.md est à la racine)
    if not skills and os.path.isfile(os.path.join(external_dir, "SKILL.md")):
        skills.append((".", external_dir))
    return skills


def hash_skill(skill_path):
    """SHA-256 du contenu de tous les fichiers sous skill_path, ordonnés par chemin relatif."""
    h = hashlib.sha256()
    files = []
    for root, dirs, names in os.walk(skill_path):
        dirs[:] = sorted(d for d in dirs if d not in IGNORED_DIRS and not d.endswith(".egg-info"))
        for name in sorted(names):
            if name in IGNORED or name.endswith(IGNORED_SUFFIXES):
                continue
            files.append(os.path.relpath(os.path.join(root, name), skill_path).replace("\\", "/"))
    files.sort()
    for rel in files:
        h.update(rel.encode("utf-8"))
        h.update(b"\x00")
        with open(os.path.join(skill_path, rel), "rb") as f:
            h.update(f.read())
        h.update(b"\x00")
    return h.hexdigest(), len(files)


def compute_lock():
    skills = {}
    for ext_folder, meta in SOURCES.items():
        ext_path = os.path.join(SKILLS_ROOT, ext_folder)
        if not os.path.isdir(ext_path):
            print(f"[warn] {ext_folder} introuvable, skip", file=sys.stderr)
            continue
        for skill_name, skill_path in find_skills(ext_path):
            key = f"{ext_folder}/{skill_name}" if skill_name != "." else ext_folder
            digest, n_files = hash_skill(skill_path)
            skills[key] = {
                "source": meta["source"],
                "source_type": meta["source_type"],
                "computed_hash": f"sha256:{digest}",
                "files_count": n_files,
            }
    return {
        "version": 1,
        "generated_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "skills": skills,
    }


def load_lock():
    if not os.path.isfile(LOCKFILE):
        return None
    with open(LOCKFILE, encoding="utf-8") as f:
        return json.load(f)


def write_lock(lock):
    with open(LOCKFILE, "w", encoding="utf-8") as f:
        json.dump(lock, f, indent=2, ensure_ascii=False)
        f.write("\n")


def diff_locks(old, new):
    """Retourne (added, removed, changed) — listes de skill keys."""
    old_skills = (old or {}).get("skills", {})
    new_skills = new.get("skills", {})
    added = sorted(set(new_skills) - set(old_skills))
    removed = sorted(set(old_skills) - set(new_skills))
    changed = sorted(
        k
        for k in (set(new_skills) & set(old_skills))
        if old_skills[k]["computed_hash"] != new_skills[k]["computed_hash"]
    )
    return added, removed, changed


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true", help="compare avec lockfile, exit 1 si drift")
    parser.add_argument("--diff", action="store_true", help="comme --check + détail")
    args = parser.parse_args()

    new_lock = compute_lock()
    old_lock = load_lock()

    if args.check or args.diff:
        if old_lock is None:
            print("[err] aucun lockfile existant. Lance sans --check pour générer.", file=sys.stderr)
            sys.exit(2)
        added, removed, changed = diff_locks(old_lock, new_lock)
        if not (added or removed or changed):
            print(f"[ok] lockfile à jour ({len(new_lock['skills'])} skills)")
            return
        print(f"[drift] {len(added)} added, {len(removed)} removed, {len(changed)} changed")
        for k in added:
            print(f"  + {k}")
        for k in removed:
            print(f"  - {k}")
        for k in changed:
            print(f"  ~ {k}")
        sys.exit(1)

    write_lock(new_lock)
    print(f"[ok] lockfile écrit : {LOCKFILE}")
    print(f"     {len(new_lock['skills'])} skills lockés depuis {len(SOURCES)} dossiers external-*")
    if old_lock is not None:
        added, removed, changed = diff_locks(old_lock, new_lock)
        if added or removed or changed:
            print(f"     diff vs ancien : +{len(added)} -{len(removed)} ~{len(changed)}")


if __name__ == "__main__":
    main()
