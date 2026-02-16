#!/usr/bin/env python3
import os
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build

creds = Credentials.from_authorized_user_file(
    "token-gdrive-migration.json",
    ["https://www.googleapis.com/auth/drive"],
)
if not creds or not creds.valid:
    if creds and creds.expired and creds.refresh_token:
        creds.refresh(Request())

service = build("drive", "v3", credentials=creds)

results = (
    service.files()
    .list(
        q=(
            "'root' in parents and "
            "trashed = false and "
            "mimeType = 'application/vnd.google-apps.folder' and "
            "name contains '_TRI_'"
        ),
        fields="files(id, name)",
    )
    .execute()
)

folders = sorted(results.get("files", []), key=lambda f: f["name"])

for folder in folders:
    count_res = (
        service.files()
        .list(
            q=f"'{folder['id']}' in parents and trashed = false",
            fields="files(id)",
            pageSize=500,
        )
        .execute()
    )
    nb = len(count_res.get("files", []))
    status = "VIDE" if nb == 0 else f"{nb} fichiers"
    name = folder["name"].encode("ascii", errors="replace").decode()
    print(f"  {name:30s} : {status}")
