#!/usr/bin/env python3
"""Export complet des labels Gmail + mapping messages↔labels pour backup/rollback.

Usage:
    python gmail-export-labels.py --output data/gmail-backup-YYYY-MM-DD.json
"""

from __future__ import annotations

import argparse
import importlib.util
import json
import sys
from datetime import datetime
from pathlib import Path

SCRIPT_DIR = Path(__file__).parent
spec = importlib.util.spec_from_file_location("gmail_common", SCRIPT_DIR / "gmail-common.py")
gc = importlib.util.module_from_spec(spec)
spec.loader.exec_module(gc)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", required=True, help="Chemin du fichier JSON de backup")
    parser.add_argument(
        "--with-messages",
        action="store_true",
        default=True,
        help="Inclure le mapping message_id → label_ids (défaut: oui)",
    )
    args = parser.parse_args()

    service = gc.get_service()
    print("Récupération des labels…", file=sys.stderr)
    labels = gc.list_labels(service)
    user_labels = [lbl for lbl in labels if lbl.get("type") == "user"]
    print(f"  {len(user_labels)} labels utilisateur trouvés", file=sys.stderr)

    backup = {
        "exported_at": datetime.utcnow().isoformat() + "Z",
        "labels": labels,
        "messages_by_label": {},
    }

    if args.with_messages:
        for i, lbl in enumerate(user_labels, 1):
            print(f"  [{i}/{len(user_labels)}] {lbl['name']}", file=sys.stderr)
            ids = gc.list_messages_with_label(service, lbl["id"])
            backup["messages_by_label"][lbl["id"]] = {
                "name": lbl["name"],
                "message_ids": ids,
            }

    output_path = Path(args.output)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(json.dumps(backup, indent=2, ensure_ascii=False), encoding="utf-8")
    total_msgs = sum(len(v["message_ids"]) for v in backup["messages_by_label"].values())
    print(f"Backup écrit: {output_path} ({len(user_labels)} labels, {total_msgs} mappings)", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
