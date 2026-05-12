"""
Clear + bulk push du tab `skills_registry` dans la Sheet 1fA0BNRe.

Reset total : vide la sheet, ecrit les 387 rows propres depuis le CSV local.
Elimine les orphelins, doublons et rows vides accumules par les anciennes syncs
appendOrUpdate.

Usage :
  python gsheets-rewrite-skills-registry.py            # dry-run (preview, ne touche rien)
  python gsheets-rewrite-skills-registry.py --apply    # clear + write effectif

Le token OAuth ajoute le scope Sheets en plus de Drive si necessaire.
"""

import argparse
import csv
import os
import sys

try:
    from google.auth.transport.requests import Request
    from google.oauth2.credentials import Credentials
    from google_auth_oauthlib.flow import InstalledAppFlow
    from googleapiclient.discovery import build
    from googleapiclient.errors import HttpError
except ImportError:
    print("Dependances manquantes : pip install google-api-python-client google-auth-oauthlib")
    sys.exit(1)

SCOPES = [
    "https://www.googleapis.com/auth/drive",
    "https://www.googleapis.com/auth/spreadsheets",
]
HERE = os.path.dirname(os.path.abspath(__file__))
TOKEN_FILE = os.path.join(HERE, "token-gdrive-migration.json")
CREDENTIALS_FILE = os.path.join(HERE, "credentials-gdrive-audit.json")

SPREADSHEET_ID = "1fA0BNReT0sBWEYJ7Jiq-9V-VxC7XBTUZBnZhgBdGIsk"
TAB_NAME = "skills_registry"
CSV_PATH = os.path.join(
    "d:/VS Code/CLAUDE CODE/projects/schoolswp/.claude/skills/.registry/skills_registry.csv"
)
HEADER = ["name", "description", "path", "last_modified", "status", "detected_at", "hash"]


def authenticate():
    creds = None
    if os.path.exists(TOKEN_FILE):
        creds = Credentials.from_authorized_user_file(TOKEN_FILE, SCOPES)
        # Si scope Sheets manquant, force re-auth
        if creds and not all(s in (creds.scopes or []) for s in SCOPES):
            creds = None
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(CREDENTIALS_FILE, SCOPES)
            creds = flow.run_local_server(port=0)
        with open(TOKEN_FILE, "w") as token:
            token.write(creds.to_json())
    return creds


def load_csv():
    rows = []
    with open(CSV_PATH, encoding="utf-8-sig") as f:
        reader = csv.DictReader(f, delimiter="\t")
        for r in reader:
            rows.append([r.get(h, "") for h in HEADER])
    return rows


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--apply", action="store_true", help="Clear + write effectif (defaut: dry-run)")
    args = parser.parse_args()

    creds = authenticate()
    sheets = build("sheets", "v4", credentials=creds)

    rows = load_csv()
    print(f"CSV charge : {len(rows)} skills + 1 header")

    # Get current sheet metadata
    meta = sheets.spreadsheets().get(spreadsheetId=SPREADSHEET_ID).execute()
    target_sheet = None
    for s in meta.get("sheets", []):
        if s["properties"]["title"] == TAB_NAME:
            target_sheet = s
            break
    if not target_sheet:
        print(f"ERREUR : tab '{TAB_NAME}' introuvable dans la Sheet.")
        sys.exit(2)
    grid = target_sheet["properties"]["gridProperties"]
    print(f"Tab actuel : {TAB_NAME} ({grid['rowCount']} rows x {grid['columnCount']} cols)")

    # Read current row count via values
    existing = (
        sheets.spreadsheets()
        .values()
        .get(spreadsheetId=SPREADSHEET_ID, range=f"{TAB_NAME}!A:A")
        .execute()
    )
    existing_rows = len(existing.get("values", []))
    print(f"Rows non-vides actuelles : {existing_rows}")

    if not args.apply:
        print("\n=== Dry-run ===")
        print(f"Action : clear A1:G{max(existing_rows, len(rows) + 1)}")
        print(f"Action : write {len(rows) + 1} rows (1 header + {len(rows)} data) dans A1")
        print(f"Sample new row 1 : {rows[0][:3]}")
        print(f"Sample new row last : {rows[-1][:3]}")
        print("\nRelancer avec --apply pour executer.")
        return

    # Clear all
    clear_range = f"{TAB_NAME}!A1:G{max(existing_rows, len(rows) + 1) + 10}"
    print(f"\n=== Clear {clear_range} ===")
    sheets.spreadsheets().values().clear(spreadsheetId=SPREADSHEET_ID, range=clear_range).execute()
    print("Cleared.")

    # Write header + data
    body = {"values": [HEADER] + rows}
    print(f"\n=== Write {len(body['values'])} rows en A1 ===")
    res = (
        sheets.spreadsheets()
        .values()
        .update(
            spreadsheetId=SPREADSHEET_ID,
            range=f"{TAB_NAME}!A1",
            valueInputOption="RAW",
            body=body,
        )
        .execute()
    )
    print(f"Updated cells : {res.get('updatedCells')}")
    print(f"Updated range : {res.get('updatedRange')}")
    print("\nReset termine. La sheet contient exactement les 387 skills du CSV.")


if __name__ == "__main__":
    main()
