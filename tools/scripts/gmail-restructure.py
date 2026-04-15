#!/usr/bin/env python3
"""Restructuration labels Gmail : 40 → 12 (phases 1-3).

Phase 1 — re-tag des messages depuis labels enfants vers label parent.
Phase 2 — rename `🧰 SaaS & Outils` → `🧰 SaaS`, création `📊 Factures`.
Phase 3 — suppression des labels vidés.

Usage:
    python gmail-restructure.py --dry-run      # simulation (défaut)
    python gmail-restructure.py --execute      # exécution réelle
"""

from __future__ import annotations

import argparse
import importlib.util
import sys
from pathlib import Path

SCRIPT_DIR = Path(__file__).parent
spec = importlib.util.spec_from_file_location("gmail_common", SCRIPT_DIR / "gmail-common.py")
gc = importlib.util.module_from_spec(spec)
spec.loader.exec_module(gc)


# Mapping source label name → target label name (phase 1)
RETAG_MAP: dict[str, str] = {
    # Contenus pipeline → parent
    "🎓 schoolsWP/🎬 Contenus/01. Idées": "🎓 schoolsWP/🎬 Contenus",
    "🎓 schoolsWP/🎬 Contenus/02. À produire": "🎓 schoolsWP/🎬 Contenus",
    "🎓 schoolsWP/🎬 Contenus/03. En cours": "🎓 schoolsWP/🎬 Contenus",
    "🎓 schoolsWP/🎬 Contenus/04. À publier": "🎓 schoolsWP/🎬 Contenus",
    "🎓 schoolsWP/🎬 Contenus/05. À mettre à jour": "🎓 schoolsWP/🎬 Contenus",
    "🎓 schoolsWP/🎬 Contenus/06. Recyclage": "🎓 schoolsWP/🎬 Contenus",
    # Admin → 📊 Factures (top-level, créé en phase 2)
    "🎓 schoolsWP/📊 Admin/01. Comptabilité": "📊 Factures",
    "🎓 schoolsWP/📊 Admin/02. Juridique": "📊 Factures",
    "🎓 schoolsWP/📊 Admin/03. Comptes & accès": "📊 Factures",
    # Communauté → parent
    "🎓 schoolsWP/📚 Communauté/01. Questions lecteurs": "🎓 schoolsWP/📚 Communauté",
    "🎓 schoolsWP/📚 Communauté/02. Retours & feedback": "🎓 schoolsWP/📚 Communauté",
    "🎓 schoolsWP/📚 Communauté/03. Discussions": "🎓 schoolsWP/📚 Communauté",
    # Tech → 🧰 SaaS (renommé en phase 2)
    "🎓 schoolsWP/🛠️ Tech & Outils/01. WordPress & plugins": "🧰 SaaS",
    "🎓 schoolsWP/🛠️ Tech & Outils/02. SEO & analytics": "🧰 SaaS",
    "🎓 schoolsWP/🛠️ Tech & Outils/03. IA & automatisation": "🧰 SaaS",
    "🎓 schoolsWP/🛠️ Tech & Outils/04. Hébergement & infra": "🧰 SaaS",
    # Maison sous-labels → parent
    "🏠 Maison/01. Famille": "🏠 Maison",
    "🏠 Maison/02. Administratif perso": "🏠 Maison",
    "🏠 Maison/03. Santé": "🏠 Maison",
    "🏠 Maison/04. Logement": "🏠 Maison",
    "🏠 Maison/05. Finances perso": "🏠 Maison",
    "🏠 Maison/06. Loisirs & projets perso": "🏠 Maison",
    "🏠 Maison/07. À traiter": "🏠 Maison",
    # Doublon top-level
    "💻 WordPress": "🧰 SaaS",
}

# Labels à supprimer après re-tag (inclut parents devenus vides)
LABELS_TO_DELETE: list[str] = list(RETAG_MAP.keys()) + [
    "🎓 schoolsWP/📊 Admin",
    "🎓 schoolsWP/🛠️ Tech & Outils",
    "🎓 schoolsWP/📥 À traiter",
    "KidKihl@gmail.com",
]

# Phase 2 — renames et créations
RENAME_MAP: dict[str, str] = {
    "🧰 SaaS & Outils": "🧰 SaaS",
}
NEW_LABELS: list[str] = ["📊 Factures"]


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--execute", action="store_true", help="Exécuter réellement (défaut: dry-run)")
    args = parser.parse_args()
    dry = not args.execute

    service = gc.get_service()
    labels = gc.list_labels(service)
    by_name = {lbl["name"]: lbl for lbl in labels}

    prefix = "[DRY-RUN] " if dry else ""
    print(f"{prefix}=== Phase 2a — Renames ===")
    for old, new in RENAME_MAP.items():
        lbl = by_name.get(old)
        if not lbl:
            print(f"  SKIP (introuvable): {old}")
            continue
        print(f"  RENAME {old} → {new}")
        if not dry:
            service.users().labels().patch(userId="me", id=lbl["id"], body={"name": new}).execute()
            by_name[new] = by_name.pop(old)
            by_name[new]["name"] = new

    print(f"\n{prefix}=== Phase 2b — Créations ===")
    for name in NEW_LABELS:
        if name in by_name:
            print(f"  SKIP (existe déjà): {name}")
            continue
        print(f"  CREATE {name}")
        if not dry:
            created = (
                service.users()
                .labels()
                .create(
                    userId="me",
                    body={"name": name, "labelListVisibility": "labelShow", "messageListVisibility": "show"},
                )
                .execute()
            )
            by_name[name] = created

    print(f"\n{prefix}=== Phase 1 — Re-tag messages ===")
    for src_name, dst_name in RETAG_MAP.items():
        src = by_name.get(src_name)
        dst = by_name.get(dst_name)
        if not src:
            print(f"  SKIP src absent: {src_name}")
            continue
        if not dst:
            print(f"  SKIP dst absent: {dst_name}")
            continue
        msg_ids = gc.list_messages_with_label(service, src["id"]) if not dry else []
        if dry:
            print(f"  RETAG {src_name} → {dst_name}  (messages comptés en execute)")
        else:
            print(f"  RETAG {src_name} → {dst_name}  ({len(msg_ids)} messages)")
            if msg_ids:
                gc.batch_modify(service, msg_ids, add=[dst["id"]], remove=[src["id"]])

    print(f"\n{prefix}=== Phase 3 — Suppressions ===")
    for name in LABELS_TO_DELETE:
        lbl = by_name.get(name)
        if not lbl:
            print(f"  SKIP (absent): {name}")
            continue
        print(f"  DELETE {name}")
        if not dry:
            service.users().labels().delete(userId="me", id=lbl["id"]).execute()

    if dry:
        print("\nMode dry-run. Relance avec --execute pour appliquer.")
    else:
        print("\nTerminé. Lance gmail-audit-labels.py pour vérifier.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
