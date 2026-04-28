"""Cherche un label Gmail par nom (partial match, case-insensitive) et retourne son ID.

Usage : python tools/scripts/gmail-find-label.py "newsletters"
"""

from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

SCRIPT_DIR = Path(__file__).parent
_spec = importlib.util.spec_from_file_location("gmail_common", SCRIPT_DIR / "gmail-common.py")
_gc = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_gc)


if __name__ == "__main__":
    query = (sys.argv[1] if len(sys.argv) > 1 else "").lower()
    service = _gc.get_service()
    labels = _gc.list_labels(service)
    matches = [l for l in labels if query in l["name"].lower()] if query else labels
    for l in sorted(matches, key=lambda x: x["name"]):
        print(f"{l['id']:20s}  |  {l['name']}")
