"""Dump all tabs of source sheet."""

import json
from pathlib import Path

from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build

SHEET_ID = "1YLtlrrOgZAdyamYdEu_uOLz5lzvSJKfS4ykDCSfjKm8"
TOKEN = Path(__file__).parent / "token-cci-v2.json"
SCOPES = ["https://www.googleapis.com/auth/drive", "https://www.googleapis.com/auth/spreadsheets"]
creds = Credentials.from_authorized_user_file(str(TOKEN), SCOPES)
svc = build("sheets", "v4", credentials=creds)
meta = svc.spreadsheets().get(spreadsheetId=SHEET_ID).execute()
out = {}
for s in meta["sheets"]:
    t = s["properties"]["title"]
    v = svc.spreadsheets().values().get(spreadsheetId=SHEET_ID, range=t).execute().get("values", [])
    out[t] = v
    print(f"{t}: {len(v)} rows")
Path(__file__).parent.parent.parent.joinpath("data/cci-source-all.json").write_text(
    json.dumps(out, ensure_ascii=False, indent=2), encoding="utf-8"
)
print("Dumped.")
