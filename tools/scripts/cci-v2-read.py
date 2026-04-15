"""Read source Sheet 'CCI Metz - Formations 2026 - schoolsWP' for diagnosis."""

import json
from pathlib import Path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build

SHEET_ID = "1YLtlrrOgZAdyamYdEu_uOLz5lzvSJKfS4ykDCSfjKm8"
TOKEN = Path(__file__).parent / "token-cci-v2.json"
SCOPES = ["https://www.googleapis.com/auth/drive", "https://www.googleapis.com/auth/spreadsheets"]

creds = Credentials.from_authorized_user_file(str(TOKEN), SCOPES)
if creds.expired and creds.refresh_token:
    creds.refresh(Request())
    TOKEN.write_text(creds.to_json())

svc = build("sheets", "v4", credentials=creds)
meta = svc.spreadsheets().get(spreadsheetId=SHEET_ID).execute()
print("TITLE:", meta["properties"]["title"])
print("SHEETS:")
for s in meta["sheets"]:
    p = s["properties"]
    print(
        f"  - {p['title']} (id={p['sheetId']}, rows={p['gridProperties']['rowCount']}, cols={p['gridProperties']['columnCount']})"
    )

# Read first tab fully
first = meta["sheets"][0]["properties"]["title"]
vals = svc.spreadsheets().values().get(spreadsheetId=SHEET_ID, range=first).execute().get("values", [])
print(f"\n=== TAB '{first}' — {len(vals)} rows ===")
out = Path(__file__).parent.parent.parent / "data" / "cci-source-dump.json"
out.parent.mkdir(exist_ok=True)
out.write_text(
    json.dumps(
        {"tab": first, "rows": vals, "all_tabs": [s["properties"]["title"] for s in meta["sheets"]]},
        ensure_ascii=False,
        indent=2,
    ),
    encoding="utf-8",
)
print(f"Dumped to {out}")
if vals:
    print("\nHEADERS:", vals[0])
    print(f"Sample row 2: {vals[1] if len(vals) > 1 else '(empty)'}")
