#!/usr/bin/env python3
"""Audit post-restructuration : vérifie la structure cible 12 labels.

Usage:
    python gmail-audit-labels.py
"""

from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

SCRIPT_DIR = Path(__file__).parent
spec = importlib.util.spec_from_file_location("gmail_common", SCRIPT_DIR / "gmail-common.py")
gc = importlib.util.module_from_spec(spec)
spec.loader.exec_module(gc)

EXPECTED = {
    "🎓 schoolsWP",
    "🎓 schoolsWP/🤝 Partenariats",
    "🎓 schoolsWP/💰 Affiliation",
    "🎓 schoolsWP/🎬 Contenus",
    "🎓 schoolsWP/📚 Communauté",
    "🏠 Maison",
    "📊 Factures",
    "🧰 SaaS",
    "🛒 Achats",
    "📰 Newsletters",
    "🔔 Notifications",
    "🤖 Automatisations",
}


def main() -> int:
    service = gc.get_service()
    labels = gc.list_labels(service)
    user_names = {lbl["name"] for lbl in labels if lbl.get("type") == "user"}

    missing = EXPECTED - user_names
    extra = user_names - EXPECTED - {"🛍️ Petit Papier Magique"}  # toléré

    print(f"Labels utilisateur totaux: {len(user_names)} (cible: 12-13)")
    print(f"\n✅ Présents ({len(EXPECTED & user_names)}/{len(EXPECTED)}):")
    for name in sorted(EXPECTED & user_names):
        print(f"  {name}")

    if missing:
        print(f"\n❌ Manquants ({len(missing)}):")
        for name in sorted(missing):
            print(f"  {name}")

    if extra:
        print(f"\n⚠️ Labels non attendus ({len(extra)}):")
        for name in sorted(extra):
            print(f"  {name}")

    return 0 if not missing else 1


if __name__ == "__main__":
    sys.exit(main())
