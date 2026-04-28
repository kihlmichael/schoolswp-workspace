"""Cree le label Gmail 'newsletter/plugins' (si absent) et retourne son ID.

Usage : python tools/scripts/gmail-create-label.py [NAME]
Default NAME = newsletter/plugins
"""

from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

SCRIPT_DIR = Path(__file__).parent
_spec = importlib.util.spec_from_file_location("gmail_common", SCRIPT_DIR / "gmail-common.py")
_gc = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_gc)

get_service = _gc.get_service
list_labels = _gc.list_labels
find_label_by_name = _gc.find_label_by_name


def create_or_get_label(name: str) -> dict:
    service = get_service()
    existing = find_label_by_name(list_labels(service), name)
    if existing:
        print(f"[OK] Label existant : {name} -> id={existing['id']}")
        return existing
    body = {
        "name": name,
        "labelListVisibility": "labelShow",
        "messageListVisibility": "show",
    }
    created = service.users().labels().create(userId="me", body=body).execute()
    print(f"[CREE] Label : {name} -> id={created['id']}")
    return created


if __name__ == "__main__":
    name = sys.argv[1] if len(sys.argv) > 1 else "newsletter/plugins"
    lbl = create_or_get_label(name)
    print(f"\nLABEL_ID={lbl['id']}")
