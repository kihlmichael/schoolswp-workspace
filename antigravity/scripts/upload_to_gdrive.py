import os
import sys
import json
import mimetypes
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload

sys.stdout.reconfigure(encoding='utf-8')

# Scopes required
SCOPES = ['https://www.googleapis.com/auth/drive.file']

client_secrets_path = r"D:\VS Code\CLAUDE CODE\projects\schoolswp\.credentials\gsc-client-secrets.json"
token_path = r"d:\ANTIGRAVITY\.credentials\gdrive-token.json"
csv_file_path = r"d:\ANTIGRAVITY\outputs\schoolswp_plugins_inventory.csv"

os.makedirs(r"d:\ANTIGRAVITY\.credentials", exist_ok=True)

def main():
    creds = None
    # The file gdrive-token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first time.
    if os.path.exists(token_path):
        try:
            creds = Credentials.from_authorized_user_file(token_path, SCOPES)
        except Exception as e:
            print("Error loading existing token, re-authenticating...", e)

    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            try:
                creds.refresh(Request())
            except Exception as e:
                print("Failed to refresh token:", e)
                creds = None
        
        if not creds:
            if not os.path.exists(client_secrets_path):
                print(f"Error: Client secrets not found at {client_secrets_path}")
                return
            flow = InstalledAppFlow.from_client_secrets_file(client_secrets_path, SCOPES)
            creds = flow.run_local_server(port=0)
        
        # Save the credentials for the next run
        with open(token_path, 'w') as token:
            token.write(creds.to_json())

    service = build('drive', 'v3', credentials=creds)

    print("Checking if a spreadsheet named '📋 Inventaire Extensions schoolsWP' already exists...")
    # Search for an existing file to overwrite or update
    results = service.files().list(
        q="name = '📋 Inventaire Extensions schoolsWP' and mimeType = 'application/vnd.google-apps.spreadsheet' and trashed = false",
        spaces='drive',
        fields='files(id, name)'
    ).execute()
    files = results.get('files', [])

    file_metadata = {
        'name': '📋 Inventaire Extensions schoolsWP',
        'mimeType': 'application/vnd.google-apps.spreadsheet'
    }
    
    media = MediaFileUpload(
        csv_file_path,
        mimetype='text/csv',
        resumable=True
    )

    if files:
        file_id = files[0]['id']
        print(f"Found existing file with ID: {file_id}. Overwriting...")
        # Update the existing file
        file = service.files().update(
            fileId=file_id,
            media_body=media
        ).execute()
        print(f"[OK] File updated successfully! File ID: {file.get('id')}")
    else:
        print("No existing spreadsheet found. Creating a new one...")
        # Create a new file
        file = service.files().create(
            body=file_metadata,
            media_body=media,
            fields='id'
        ).execute()
        file_id = file.get('id')
        print(f"[OK] File created successfully! File ID: {file_id}")

    sheet_url = f"https://docs.google.com/spreadsheets/d/{file_id}/edit"
    print("\n=======================================================")
    print("🎉 Ton inventaire est disponible sur Google Drive !")
    print(f"Lien Direct : {sheet_url}")
    print("=======================================================")

if __name__ == '__main__':
    main()
