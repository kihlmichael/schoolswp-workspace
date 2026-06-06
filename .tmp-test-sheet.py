from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
import os
import sys

SCOPES = ["https://www.googleapis.com/auth/spreadsheets", "https://www.googleapis.com/auth/drive"]
SHEET_ID = "1FjZgbUdSBVqTuFL2kdHKFKXcO4ZNWehINwfvWpD-vTs"

token_files = [
    "tools/scripts/token-cci-v2.json",
    "tools/scripts/token-gdrive-migration.json",
    "tools/scripts/token-gmail-filters.json",
    "tools/scripts/token-gmail.json",
    "tools/scripts/token-photos-organizer.json"
]

creds_path = "tools/scripts/credentials-gdrive-audit.json"

for token_path in token_files:
    if not os.path.exists(token_path):
        continue
    print(f"Testing token: {token_path}")
    try:
        creds = Credentials.from_authorized_user_file(token_path, SCOPES)
        if creds.expired and creds.refresh_token:
            creds.refresh(Request())
        svc = build("sheets", "v4", credentials=creds)
        res = svc.spreadsheets().values().get(
            spreadsheetId=SHEET_ID,
            range="sources!A1:Z1"
        ).execute()
        print(f"SUCCESS with token {token_path}!")
        print("Headers:", res.get("values", [[]])[0])
        # Save this working token as the one to use
        with open(".tmp-working-token.json", "w") as f:
            f.write(creds.to_json())
        break
    except Exception as e:
        print(f"Failed with token {token_path}: {e}")
