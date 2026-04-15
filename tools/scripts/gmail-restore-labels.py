#!/usr/bin/env python3
"""Restauration labels Gmail depuis backup JSON (rollback).

Recrée les labels supprimés et ré-applique le mapping messages↔labels.
Ne touche pas aux labels existants non présents dans le backup.

Usage:
    python gmail-restore-labels.py --from data/gmail-backup-YYYY-MM-DD.json [--execute]
"""

from __future__ import annotations

import argparse
import importlib.util
import json
import sys
from pathlib import Path

SCRIPT_DIR = Path(__file__).parent
spec = importlib.util.spec_from_file_location("gmail_common", SCRIPT_DIR / "gmail-common.py")
gc = importlib.util.module_from_spec(spec)
spec.loader.exec_module(gc)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--from", dest="backup", required=True, help="Chemin du backup JSON")
    parser.add_argument("--execute", action="store_true", help="Exécuter (défaut: dry-run)")
    args = parser.parse_args()
    dry = not args.execute

    backup = json.loads(Path(args.backup).read_text(encoding="utf-8"))
    service = gc.get_service()
    current_labels = gc.list_labels(service)
    current_by_name = {lbl["name"]: lbl for lbl in current_labels}

    prefix = "[DRY-RUN] " if dry else ""
    backup_user_labels = [lbl for lbl in backup["labels"] if lbl.get("type") == "user"]

    # Phase A — recréer les labels manquants
    print(f"{prefix}=== Recréation labels manquants ===")
    recreated_id_map: dict[str, str] = {}  # ancien id → nouveau id
    for lbl in backup_user_labels:
        if lbl["name"] in current_by_name:
            recreated_id_map[lbl["id"]] = current_by_name[lbl["name"]]["id"]
            continue
        print(f"  CREATE {lbl['name']}")
        if not dry:
            body = {
                "name": lbl["name"],
                "labelListVisibility": lbl.get("labelListVisibility", "labelShow"),
                "messageListVisibility": lbl.get("messageListVisibility", "show"),
            }
            created = service.users().labels().create(userId="me", body=body).execute()
            recreated_id_map[lbl["id"]] = created["id"]

    # Phase B — ré-appliquer mappings messages
    print(f"\n{prefix}=== Ré-application mappings ===")
    for old_id, data in backup.get("messages_by_label", {}).items():
        new_id = recreated_id_map.get(old_id)
        msg_ids = data["message_ids"]
        if not new_id or not msg_ids:
            continue
        print(f"  RETAG {data['name']}  ({len(msg_ids)} messages)")
        if not dry:
            gc.batch_modify(service, msg_ids, add=[new_id])

    if dry:
        print("\nMode dry-run. Relance avec --execute pour restaurer.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
