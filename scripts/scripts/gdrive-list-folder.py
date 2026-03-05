#!/usr/bin/env python3
"""
Liste le contenu d'un dossier Google Drive avec détails.

Usage :
  python gdrive-list-folder.py FOLDER_ID
"""

import os
import sys

try:
    from google.auth.transport.requests import Request
    from google.oauth2.credentials import Credentials
    from google_auth_oauthlib.flow import InstalledAppFlow
    from googleapiclient.discovery import build
except ImportError:
    print("Dependances manquantes.")
    print("  pip install -r requirements-gdrive-audit.txt")
    sys.exit(1)

SCOPES = ["https://www.googleapis.com/auth/drive.metadata.readonly"]
TOKEN_FILE = "token-gdrive-audit.json"
CREDENTIALS_FILE = "credentials-gdrive-audit.json"


def authenticate():
    creds = None
    if os.path.exists(TOKEN_FILE):
        creds = Credentials.from_authorized_user_file(TOKEN_FILE, SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            if not os.path.exists(CREDENTIALS_FILE):
                print(f"ERREUR : '{CREDENTIALS_FILE}' introuvable.")
                sys.exit(1)
            flow = InstalledAppFlow.from_client_secrets_file(
                CREDENTIALS_FILE, SCOPES
            )
            creds = flow.run_local_server(port=0)
        with open(TOKEN_FILE, "w") as token:
            token.write(creds.to_json())
    return build("drive", "v3", credentials=creds)


def main():
    if len(sys.argv) < 2:
        print("Usage : python gdrive-list-folder.py FOLDER_ID")
        sys.exit(1)

    folder_id = sys.argv[1]
    service = authenticate()

    all_files = []
    page_token = None

    while True:
        results = (
            service.files()
            .list(
                q=f"'{folder_id}' in parents and trashed = false",
                pageSize=500,
                fields="nextPageToken, files(id, name, mimeType, size, modifiedTime)",
                orderBy="name",
                pageToken=page_token,
            )
            .execute()
        )
        all_files.extend(results.get("files", []))
        page_token = results.get("nextPageToken")
        if not page_token:
            break

    # Grouper par type MIME
    by_mime = {}
    for f in all_files:
        mime = f.get("mimeType", "inconnu")
        by_mime.setdefault(mime, []).append(f)

    print(f"\n  Dossier : {folder_id}")
    print(f"  Total : {len(all_files)} fichiers\n")

    for mime in sorted(by_mime.keys()):
        files = by_mime[mime]
        short = mime.split("/")[-1]
        print(f"  [{short}] — {len(files)} fichier(s)")
        for i, f in enumerate(files):
            name = f["name"][:90].encode("ascii", errors="replace").decode()
            print(f"    {i + 1:3d}. {name}")
        print()


if __name__ == "__main__":
    main()
