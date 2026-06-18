#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
upload_session_brief.py -- Upload the end-of-session brief to Google Drive project folder.
"""

import os
import sys

try:
    from google.auth.transport.requests import Request
    from google.oauth2.credentials import Credentials
    from googleapiclient.discovery import build
    from googleapiclient.http import MediaFileUpload
except ImportError:
    print("[!] ERROR: google-api-python-client dependencies are missing in the active environment.")
    sys.exit(1)

SCOPES = ["https://www.googleapis.com/auth/drive"]
HERE = os.path.dirname(os.path.abspath(__file__))
TOKEN_FILE = os.path.join(HERE, "token-gdrive-migration.json")
CREDENTIALS_FILE = os.path.join(HERE, "credentials-gdrive-audit.json")

# target parent: schoolsWP (root folder on Drive)
SCHOOLSWP_FOLDER_ID = "1D10mjPHE_PEab5ajRUq7spoY4gleTSEY"

# local file to upload
LOCAL_FILE = r"d:\VS Code\CLAUDE CODE\projects\schoolswp\obsidian-bridge\outbox-to-obsidian\2026-06-01_synthese_recapitulatif-session-multi-agents.md"
TARGET_NAME = "2026-06-01_synthese_recapitulatif-session-multi-agents.md"

def authenticate():
    creds = None
    if os.path.exists(TOKEN_FILE):
        creds = Credentials.from_authorized_user_file(TOKEN_FILE, SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            print("[!] ERROR: Valid Google Drive token not found. Please authenticate first using a dynamic tool.")
            sys.exit(1)
    return build("drive", "v3", credentials=creds)

def upload_file():
    if not os.path.exists(LOCAL_FILE):
        print(f"[!] ERROR: Local brief file not found at {LOCAL_FILE}")
        sys.exit(1)
        
    print("[1/2] Authenticating with Google Drive...")
    service = authenticate()
    
    print(f"[2/2] Uploading '{TARGET_NAME}' to Drive folder '{SCHOOLSWP_FOLDER_ID}'...")
    file_metadata = {
        "name": TARGET_NAME,
        "parents": [SCHOOLSWP_FOLDER_ID],
        "mimeType": "text/markdown"
    }
    
    media = MediaFileUpload(
        LOCAL_FILE,
        mimetype="text/markdown",
        resumable=True
    )
    
    try:
        file = (
            service.files()
            .create(body=file_metadata, media_body=media, fields="id, name, webViewLink")
            .execute()
        )
        print("\n" + "=" * 50)
        print("[+] SUCCESS: Brief successfully uploaded to Google Drive!")
        print(f"    File Name : {file.get('name')}")
        print(f"    File ID   : {file.get('id')}")
        print(f"    Link      : {file.get('webViewLink')}")
        print("=" * 50)
    except Exception as e:
        print(f"[!] Failed to upload to Google Drive: {e}")
        sys.exit(1)

if __name__ == "__main__":
    upload_file()
