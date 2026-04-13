"""Gmail API helpers — shared auth + label utilities.

Réutilise credentials-gdrive-audit.json comme OAuth client (Gmail API doit être
activée dans le projet Cloud). Token séparé : token-gmail.json.
"""

from __future__ import annotations

import sys
from pathlib import Path

try:
    from google.auth.transport.requests import Request
    from google.oauth2.credentials import Credentials
    from google_auth_oauthlib.flow import InstalledAppFlow
    from googleapiclient.discovery import build
except ImportError:
    print("pip install google-api-python-client google-auth-oauthlib")
    sys.exit(1)

SCRIPT_DIR = Path(__file__).parent
CREDENTIALS_FILE = SCRIPT_DIR / "credentials-gdrive-audit.json"
TOKEN_FILE = SCRIPT_DIR / "token-gmail.json"

SCOPES = [
    "https://www.googleapis.com/auth/gmail.labels",
    "https://www.googleapis.com/auth/gmail.modify",
]


def get_service():
    creds = None
    if TOKEN_FILE.exists():
        creds = Credentials.from_authorized_user_file(str(TOKEN_FILE), SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(str(CREDENTIALS_FILE), SCOPES)
            creds = flow.run_local_server(port=0)
        TOKEN_FILE.write_text(creds.to_json(), encoding="utf-8")
    return build("gmail", "v1", credentials=creds)


def list_labels(service) -> list[dict]:
    return service.users().labels().list(userId="me").execute().get("labels", [])


def find_label_by_name(labels: list[dict], name: str) -> dict | None:
    for lbl in labels:
        if lbl["name"] == name:
            return lbl
    return None


def list_messages_with_label(service, label_id: str) -> list[str]:
    ids, token = [], None
    while True:
        resp = (
            service.users().messages().list(userId="me", labelIds=[label_id], maxResults=500, pageToken=token).execute()
        )
        ids.extend(m["id"] for m in resp.get("messages", []))
        token = resp.get("nextPageToken")
        if not token:
            break
    return ids


def batch_modify(
    service, message_ids: list[str], add: list[str] | None = None, remove: list[str] | None = None
) -> None:
    """Batch modify par tranches de 1000 (limite API)."""
    for i in range(0, len(message_ids), 1000):
        chunk = message_ids[i : i + 1000]
        body = {"ids": chunk}
        if add:
            body["addLabelIds"] = add
        if remove:
            body["removeLabelIds"] = remove
        service.users().messages().batchModify(userId="me", body=body).execute()
