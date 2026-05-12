"""
Push the classified skills_registry.csv (12 cols) into the Google Sheet.

Uses Google Sheets REST API directly (single batchUpdate call) with a token
obtained from `gws auth export --unmasked`. Avoids Windows cmdline length
limits that hit `gws values update` with large payloads.

Run from project root:
  .venv/Scripts/python .claude/skills/.registry/push_sheet_classification.py
  .venv/Scripts/python .claude/skills/.registry/push_sheet_classification.py --dry-run
"""

import argparse
import csv
import json
import os
import shutil
import subprocess
import sys
import urllib.request
import urllib.error
import urllib.parse

SHEET_ID = "1fA0BNReT0sBWEYJ7Jiq-9V-VxC7XBTUZBnZhgBdGIsk"
TAB = "skills_registry"
CSV_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "skills_registry.csv")
SHEETS_API = "https://sheets.googleapis.com/v4/spreadsheets"

parser = argparse.ArgumentParser()
parser.add_argument("--dry-run", action="store_true", help="Show plan, don't write")
args = parser.parse_args()

GWS_BIN = shutil.which("gws") or shutil.which("gws.cmd")
if not GWS_BIN:
    raise SystemExit("gws CLI not found in PATH")


def get_access_token():
    """Pull refresh_token from gws keyring, exchange for access_token."""
    res = subprocess.run(
        [GWS_BIN, "auth", "export", "--unmasked"],
        capture_output=True,
        text=True,
        encoding="utf-8",
    )
    if res.returncode != 0:
        raise SystemExit(f"gws auth export failed: {res.stderr}")
    out = res.stdout
    creds = json.loads(out[out.index("{"):])
    if creds.get("token"):
        return creds["token"]
    refresh_token = creds.get("refresh_token")
    client_id = creds.get("client_id")
    client_secret = creds.get("client_secret")
    if not (refresh_token and client_id and client_secret):
        raise SystemExit(f"Missing OAuth fields. Keys: {list(creds.keys())}")
    body = urllib.parse.urlencode({
        "grant_type": "refresh_token",
        "refresh_token": refresh_token,
        "client_id": client_id,
        "client_secret": client_secret,
    }).encode("utf-8")
    req = urllib.request.Request(
        "https://oauth2.googleapis.com/token",
        data=body,
        method="POST",
        headers={"Content-Type": "application/x-www-form-urlencoded"},
    )
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            tok = json.loads(resp.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        raise SystemExit(f"OAuth refresh failed: HTTP {e.code} {e.read().decode('utf-8', 'replace')}")
    return tok["access_token"]


def http_request(method, url, token, body=None):
    data = json.dumps(body).encode("utf-8") if body is not None else None
    req = urllib.request.Request(
        url,
        data=data,
        method=method,
        headers={
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json",
            "User-Agent": "schoolswp-skills-registry/1.0",
        },
    )
    try:
        with urllib.request.urlopen(req, timeout=60) as resp:
            return resp.status, json.loads(resp.read().decode("utf-8") or "{}")
    except urllib.error.HTTPError as e:
        body_err = e.read().decode("utf-8", errors="replace")
        raise SystemExit(f"HTTP {e.code} on {method} {url}\n{body_err}")


# ── Load CSV ────────────────────────────────────────────────────────────────
with open(CSV_PATH, encoding="utf-8-sig") as f:
    rows = list(csv.reader(f, delimiter="\t"))

print(f"CSV : {len(rows)} rows × {len(rows[0])} cols")
assert len(rows[0]) == 12, f"Expected 12 cols, got {len(rows[0])}"
total_data = len(rows) - 1
end_row = len(rows)  # 1 header + N data
range_full = f"{TAB}!A1:L{end_row}"
range_clear = f"{TAB}!A1:Z1100"
print(f"Header  : {rows[0]}")
print(f"Range   : {range_full}")
print(f"Clear   : {range_clear}")
print(f"Skills  : {total_data}")

if args.dry_run:
    print("\n[DRY-RUN] No HTTP calls made.")
    sys.exit(0)

# ── Auth ────────────────────────────────────────────────────────────────────
print("\n[auth] fetching access token from gws keyring ...")
token = get_access_token()
print(f"  token len={len(token)} (masked)")

# ── Step 1 : clear ─────────────────────────────────────────────────────────
print(f"\n[1/2] Clearing {range_clear} ...")
url_clear = f"{SHEETS_API}/{SHEET_ID}/values/{urllib.parse.quote(range_clear)}:clear"
status, resp = http_request("POST", url_clear, token, body={})
print(f"  HTTP {status} clearedRange={resp.get('clearedRange')}")

# ── Step 2 : single batchUpdate (header + all data) ───────────────────────
print(f"\n[2/2] Pushing {len(rows)} rows via batchUpdate ...")
url_update = f"{SHEETS_API}/{SHEET_ID}/values:batchUpdate"
body = {
    "valueInputOption": "RAW",
    "data": [{"range": range_full, "majorDimension": "ROWS", "values": rows}],
}
status, resp = http_request("POST", url_update, token, body=body)
print(
    f"  HTTP {status} totalUpdatedCells={resp.get('totalUpdatedCells')}"
    f" totalUpdatedRows={resp.get('totalUpdatedRows')}"
    f" totalUpdatedColumns={resp.get('totalUpdatedColumns')}"
)

print(f"\nDone. Sheet : https://docs.google.com/spreadsheets/d/{SHEET_ID}/edit")
