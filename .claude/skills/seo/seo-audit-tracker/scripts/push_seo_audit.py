"""
Push a single SEO audit synthesis row into the cumulative tracker Google Sheet
(tabs FR / DE / EN), and optionally create a detailed per-audit spreadsheet.

Deterministic Sheets I/O for the `seo-audit-tracker` skill. The LLM produces the
analysis as a JSON payload; this script writes it. Auth reuses the repo-standard
`gws auth export` -> Google Sheets REST API pattern (see
.claude/skills/.registry/push_sheet_classification.py).

The tracker Sheet ID is NEVER hardcoded. It is read from --sheet-id, then the
SEO_AUDIT_SHEET_ID env var, then scripts/.env. The example/test ID lives in
scripts/.env.example only.

Run from project root (projects/schoolswp/):
  .venv/Scripts/python .claude/skills/seo/seo-audit-tracker/scripts/push_seo_audit.py \
      --data path/to/payload.json --lang FR
  ... --dry-run        # show plan, write nothing
  ... --detailed       # also create the per-audit multi-tab spreadsheet
"""

import argparse
import json
import os
import shutil
import subprocess
import urllib.error
import urllib.parse
import urllib.request

SHEETS_API = "https://sheets.googleapis.com/v4/spreadsheets"
DRIVE_API = "https://www.googleapis.com/drive/v3/files"

# Fixed tracker columns (order matters - do not reorder).
HEADER = [
    "Date audit",
    "Langue",
    "URL article",
    "Mot-clé cible",
    "Score SEO",
    "Score contenu",
    "Score intention de recherche",
    "Score maillage interne",
    "Score opportunité IA / citation IA",
    "Problèmes prioritaires",
    "Recommandations concrètes",
    "Actions à faire",
    "Priorité",
    "Statut",
    "Notes",
]

# tracker_row JSON keys mapped to HEADER, in column order.
ROW_KEYS = [
    "date_audit",
    "langue",
    "url",
    "mot_cle",
    "score_seo",
    "score_contenu",
    "score_intention",
    "score_maillage",
    "score_ia",
    "problemes",
    "recommandations",
    "actions",
    "priorite",
    "statut",
    "notes",
]

VALID_LANGS = ("FR", "DE", "EN")
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))


def load_dotenv(path):
    """Minimal .env loader (KEY=VALUE lines). Does not override existing env."""
    if not os.path.isfile(path):
        return
    with open(path, encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#") or "=" not in line:
                continue
            key, _, val = line.partition("=")
            key, val = key.strip(), val.strip().strip('"').strip("'")
            if key and key not in os.environ:
                os.environ[key] = val


def resolve_sheet_id(cli_value):
    if cli_value:
        return cli_value
    load_dotenv(os.path.join(SCRIPT_DIR, ".env"))
    sheet_id = os.environ.get("SEO_AUDIT_SHEET_ID")
    if not sheet_id:
        raise SystemExit(
            "No tracker Sheet ID. Pass --sheet-id, set SEO_AUDIT_SHEET_ID, "
            "or add it to scripts/.env (see scripts/.env.example)."
        )
    return sheet_id


def get_gws_bin():
    gws = shutil.which("gws") or shutil.which("gws.cmd")
    if not gws:
        raise SystemExit("gws CLI not found in PATH. Authenticate gws first (see gws-shared skill).")
    return gws


def get_access_token():
    """Pull refresh_token from gws keyring, exchange for an access_token."""
    res = subprocess.run(
        [get_gws_bin(), "auth", "export", "--unmasked"],
        capture_output=True,
        text=True,
        encoding="utf-8",
    )
    if res.returncode != 0:
        raise SystemExit(f"gws auth export failed: {res.stderr}")
    out = res.stdout
    creds = json.loads(out[out.index("{") :])
    if creds.get("token"):
        return creds["token"]
    refresh_token = creds.get("refresh_token")
    client_id = creds.get("client_id")
    client_secret = creds.get("client_secret")
    if not (refresh_token and client_id and client_secret):
        raise SystemExit(f"Missing OAuth fields. Keys: {list(creds.keys())}")
    body = urllib.parse.urlencode(
        {
            "grant_type": "refresh_token",
            "refresh_token": refresh_token,
            "client_id": client_id,
            "client_secret": client_secret,
        }
    ).encode("utf-8")
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
            "User-Agent": "schoolswp-seo-audit-tracker/1.0",
        },
    )
    try:
        with urllib.request.urlopen(req, timeout=60) as resp:
            return resp.status, json.loads(resp.read().decode("utf-8") or "{}")
    except urllib.error.HTTPError as e:
        body_err = e.read().decode("utf-8", errors="replace")
        raise SystemExit(f"HTTP {e.code} on {method} {url}\n{body_err}")


def a1_range(tab, cells):
    """Build an A1 range, quoting the tab name (handles spaces / non-ASCII)."""
    return f"'{tab}'!{cells}"


def ensure_tab_with_header(sheet_id, token, tab):
    """Create the tab if missing, then ensure row 1 holds HEADER. Idempotent."""
    status, meta = http_request(
        "GET",
        f"{SHEETS_API}/{sheet_id}?fields=sheets.properties(title,sheetId)",
        token,
    )
    titles = [s["properties"]["title"] for s in meta.get("sheets", [])]
    if tab not in titles:
        print(f"  [tab] '{tab}' missing -> creating")
        http_request(
            "POST",
            f"{SHEETS_API}/{sheet_id}:batchUpdate",
            token,
            body={"requests": [{"addSheet": {"properties": {"title": tab}}}]},
        )
    # Check header row.
    rng = urllib.parse.quote(a1_range(tab, "A1:O1"))
    status, vals = http_request(
        "GET",
        f"{SHEETS_API}/{sheet_id}/values/{rng}",
        token,
    )
    existing = vals.get("values", [[]])
    if not existing or not existing[0]:
        print(f"  [header] writing header row on '{tab}'")
        http_request(
            "PUT",
            f"{SHEETS_API}/{sheet_id}/values/{rng}?valueInputOption=RAW",
            token,
            body={"values": [HEADER]},
        )


def append_tracker_row(sheet_id, token, tab, row):
    rng = urllib.parse.quote(a1_range(tab, "A:O"))
    url = f"{SHEETS_API}/{sheet_id}/values/{rng}:append?valueInputOption=RAW&insertDataOption=INSERT_ROWS"
    status, resp = http_request("POST", url, token, body={"values": [row]})
    updated = resp.get("updates", {})
    print(
        f"  [append] HTTP {status} range={updated.get('updatedRange')} "
        f"rows={updated.get('updatedRows')} cells={updated.get('updatedCells')}"
    )


def create_detailed_sheet(token, detailed, folder_id=None):
    """Create a new multi-tab spreadsheet from detailed.tabs and return its URL."""
    title = detailed.get("title") or "Audit SEO détaillé"
    tabs = detailed.get("tabs") or {}
    if not tabs:
        print("  [detailed] no tabs in payload -> skipped")
        return None
    body = {
        "properties": {"title": title},
        "sheets": [{"properties": {"title": name}} for name in tabs],
    }
    status, sheet = http_request("POST", f"{SHEETS_API}", token, body=body)
    new_id = sheet["spreadsheetId"]
    # Write each tab's values.
    data = []
    for name, rows in tabs.items():
        if rows:
            data.append({"range": a1_range(name, "A1"), "majorDimension": "ROWS", "values": rows})
    if data:
        http_request(
            "POST",
            f"{SHEETS_API}/{new_id}/values:batchUpdate",
            token,
            body={"valueInputOption": "RAW", "data": data},
        )
    # Optional: move to a Drive folder.
    if folder_id:
        try:
            http_request(
                "PATCH",
                f"{DRIVE_API}/{new_id}?addParents={folder_id}&removeParents=root&fields=id,parents",
                token,
            )
            print(f"  [detailed] moved to folder {folder_id}")
        except SystemExit as e:
            print(f"  [detailed] folder move failed (kept in My Drive root): {e}")
    url = f"https://docs.google.com/spreadsheets/d/{new_id}/edit"
    print(f"  [detailed] created: {url}")
    return url


def build_row(tracker_row):
    missing = [k for k in ROW_KEYS if k not in tracker_row]
    if missing:
        raise SystemExit(f"payload.tracker_row missing keys: {missing}")
    return [str(tracker_row[k]) for k in ROW_KEYS]


def main():
    parser = argparse.ArgumentParser(description="Push one SEO audit row to the tracker Sheet.")
    parser.add_argument("--data", required=True, help="Path to the JSON payload file")
    parser.add_argument("--lang", required=True, choices=VALID_LANGS, help="Tracker tab / language")
    parser.add_argument("--sheet-id", default=None, help="Tracker Sheet ID (else SEO_AUDIT_SHEET_ID)")
    parser.add_argument("--detailed", action="store_true", help="Also create the per-audit detailed Sheet")
    parser.add_argument("--dry-run", action="store_true", help="Show plan, write nothing")
    args = parser.parse_args()

    with open(args.data, encoding="utf-8") as f:
        payload = json.load(f)

    tracker_row = payload.get("tracker_row")
    if not tracker_row:
        raise SystemExit("payload missing 'tracker_row'")
    # --lang is authoritative: it picks the tab, so it must also be the Langue
    # column value. This guarantees the row never lands in a mismatched tab.
    tracker_row["langue"] = args.lang

    row = build_row(tracker_row)
    sheet_id = resolve_sheet_id(args.sheet_id)

    print(f"Tracker  : {sheet_id}")
    print(f"Tab      : {args.lang}")
    print(f"Row      : {row}")
    if args.detailed:
        det = payload.get("detailed") or {}
        print(f"Detailed : {det.get('title', '(no title)')} -> {list((det.get('tabs') or {}).keys())}")

    if args.dry_run:
        print("\n[DRY-RUN] No HTTP calls made.")
        return

    token = get_access_token()
    print("\n[1/2] Ensuring tab + header ...")
    ensure_tab_with_header(sheet_id, token, args.lang)
    print(f"[2/2] Appending row to '{args.lang}' ...")
    append_tracker_row(sheet_id, token, args.lang, row)

    if args.detailed:
        load_dotenv(os.path.join(SCRIPT_DIR, ".env"))
        folder_id = os.environ.get("SEO_AUDIT_FOLDER_ID")
        print("\n[detailed] Creating per-audit spreadsheet ...")
        create_detailed_sheet(token, payload.get("detailed") or {}, folder_id)

    print(f"\nDone. Tracker : https://docs.google.com/spreadsheets/d/{sheet_id}/edit")


if __name__ == "__main__":
    main()
