"""Sync 3 PDFs Novamira v4.1 vers Drive: trash anciens + upload nouveaux."""
from pathlib import Path
from google.oauth2.credentials import Credentials
from google.auth.transport.requests import Request
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload

SCOPES = ["https://www.googleapis.com/auth/drive"]
TOKEN = Path(__file__).parent / "token-gdrive-migration.json"
PARENT_FOLDER = "1wX5-5mnd1GRQxBLwnA3XiYuK2RzBu3yM"

OLD_IDS = {
    "01": "1BS09iOUJfHZMVLEbScpVPmP_81x2MKr5",
    "02": "1ATJZuGTDKwtIOIWcowFxZblD3j6Lelp5",
    "04": "1PZykbxls1DKfz1NN4v4UJYMDrTCha8zx",
}

PDFS = {
    "01": (
        "01-cadrage-et-page-de-vente-courte.pdf",
        "01 - Cadrage et page de vente courte (v4.1).pdf",
    ),
    "02": (
        "02-bonus-et-sequencement.pdf",
        "02 - Bonus et sequencement (v4.1).pdf",
    ),
    "04": (
        "04-checkout-order-bump-et-upsells.pdf",
        "04 - Page de paiement option et offre complementaire (v4.1).pdf",
    ),
}

LOCAL_DIR = Path(
    "d:/VS Code/CLAUDE CODE/projects/schoolswp/content/decisions/_novamira-pv-tmp"
)


def main() -> None:
    creds = Credentials.from_authorized_user_file(str(TOKEN), SCOPES)
    if creds.expired and creds.refresh_token:
        creds.refresh(Request())
    service = build("drive", "v3", credentials=creds)

    for key, file_id in OLD_IDS.items():
        service.files().update(fileId=file_id, body={"trashed": True}).execute()
        print(f"Trashed {key}: {file_id}")

    for key, (local_name, drive_name) in PDFS.items():
        local_path = LOCAL_DIR / local_name
        media = MediaFileUpload(str(local_path), mimetype="application/pdf")
        metadata = {"name": drive_name, "parents": [PARENT_FOLDER]}
        result = (
            service.files()
            .create(body=metadata, media_body=media, fields="id,name")
            .execute()
        )
        print(f"Uploaded {key}: {result['id']} - {result['name']}")


if __name__ == "__main__":
    main()
