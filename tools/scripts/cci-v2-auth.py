"""Re-auth Google OAuth for Sheets v2 mission. Opens browser."""

from pathlib import Path

from google_auth_oauthlib.flow import InstalledAppFlow

CREDS = Path(__file__).parent / "credentials-gdrive-audit.json"
TOKEN = Path(__file__).parent / "token-cci-v2.json"
SCOPES = [
    "https://www.googleapis.com/auth/drive",
    "https://www.googleapis.com/auth/spreadsheets",
]

flow = InstalledAppFlow.from_client_secrets_file(str(CREDS), SCOPES)
creds = flow.run_local_server(port=0, prompt="consent")
TOKEN.write_text(creds.to_json(), encoding="utf-8")
print(f"OK → token saved to {TOKEN}")
