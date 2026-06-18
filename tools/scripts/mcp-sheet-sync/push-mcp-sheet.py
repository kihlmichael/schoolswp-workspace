"""Sync : pousse les rows de mcp-sheet-rows.json dans le Sheet schoolsWP - MCP Servers.

Usage :
    .venv/Scripts/python tools/scripts/mcp-sheet-sync/push-mcp-sheet.py

Pour rafraichir le sheet apres ajout d'un MCP : editer mcp-sheet-rows.json puis
relancer ce script (il clear pas — append seulement; clear manuel A2:G1000 avant
relance pour un full refresh).

Prerequis : gws CLI authentifie (cf. memoire reference_gws_oauth_refresh.md).
"""

import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).parent
SHEET_ID = "1IAYk6TPU1s8W81lfV4r0mEGH_0VyfwsZo53GkuEwe9k"
ROWS_FILE = ROOT / "mcp-sheet-rows.json"

all_rows = json.loads(ROWS_FILE.read_text(encoding="utf-8"))["values"]
BATCH = 8  # Windows cmd line ~8K limit, payload large -> split en lots de 8 rows

params = json.dumps(
    {
        "spreadsheetId": SHEET_ID,
        "range": "Feuille 1!A1",
        "valueInputOption": "RAW",
        "insertDataOption": "INSERT_ROWS",
    }
)

total = 0
for i in range(0, len(all_rows), BATCH):
    batch = all_rows[i : i + BATCH]
    body_json = json.dumps({"values": batch})
    cmd = [
        "gws",
        "sheets",
        "spreadsheets",
        "values",
        "append",
        "--params",
        params,
        "--json",
        body_json,
    ]
    res = subprocess.run(cmd, capture_output=True, text=True, shell=True)
    if res.returncode != 0:
        print(f"FAIL batch {i // BATCH + 1}", file=sys.stderr)
        print("stderr:", res.stderr[:500], file=sys.stderr)
        sys.exit(res.returncode)
    print(f"batch {i // BATCH + 1} OK ({len(batch)} rows)")
    total += len(batch)

print(f"\nTotal pushed: {total} rows")
