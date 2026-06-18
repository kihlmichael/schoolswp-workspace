"""Telecharge le README cadrage offre v4 (PDF Drive) et grep les anciens IDs."""
import io
import re
import sys
from pathlib import Path
from google.oauth2.credentials import Credentials
from google.auth.transport.requests import Request
from googleapiclient.discovery import build
from googleapiclient.http import MediaIoBaseDownload

SCOPES = ["https://www.googleapis.com/auth/drive"]
TOKEN = Path(__file__).parent / "token-gdrive-migration.json"
README_ID = "1Fta7nj-cBh_3Ju928OO1LCKOk1v2F68q"
OLD_IDS = [
    "1BS09iOUJfHZMVLEbScpVPmP_81x2MKr5",
    "1ATJZuGTDKwtIOIWcowFxZblD3j6Lelp5",
    "1PZykbxls1DKfz1NN4v4UJYMDrTCha8zx",
]

creds = Credentials.from_authorized_user_file(str(TOKEN), SCOPES)
if creds.expired and creds.refresh_token:
    creds.refresh(Request())
service = build("drive", "v3", credentials=creds)

request = service.files().get_media(fileId=README_ID)
fh = io.BytesIO()
downloader = MediaIoBaseDownload(fh, request)
done = False
while not done:
    _, done = downloader.next_chunk()
raw = fh.getvalue()

found = {oid: oid.encode() in raw for oid in OLD_IDS}
matches_drive_url = re.findall(rb"file/d/([A-Za-z0-9_-]{20,})", raw)
print("README size (bytes):", len(raw))
print("Old IDs found:", found)
print("Any file/d/ URLs detected (count):", len(matches_drive_url))
if matches_drive_url:
    unique = sorted(set(m.decode() for m in matches_drive_url))
    print("Unique file IDs referenced:")
    for f in unique:
        print(" -", f)
