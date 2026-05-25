import io

from googleapiclient.discovery import build
from googleapiclient.http import MediaIoBaseDownload
from sheets_client import get_google_credentials


def get_drive_service():
    creds = get_google_credentials()
    return build("drive", "v3", credentials=creds)


def get_file_metadata(file_id):
    """
    Retrieves the metadata of a file on Google Drive (like its name).
    """
    svc = get_drive_service()
    return svc.files().get(fileId=file_id, fields="name, mimeType").execute()


def download_file_from_drive(file_id, destination_path):
    """
    Downloads a binary file from Google Drive and writes it to the destination path.
    """
    svc = get_drive_service()

    # Récupérer les métadonnées pour logguer le nom réel
    meta = get_file_metadata(file_id)
    file_name = meta.get("name", "inconnu")
    mime_type = meta.get("mimeType", "inconnu")

    print(f"[INFO] Début du téléchargement de '{file_name}' ({mime_type}) depuis Google Drive...")

    request = svc.files().get_media(fileId=file_id)
    fh = io.FileIO(destination_path, "wb")
    downloader = MediaIoBaseDownload(fh, request, chunksize=1024 * 1024 * 5)  # chunk de 5MB

    done = False
    while not done:
        status, done = downloader.next_chunk()
        if status:
            print(f"[INFO] Téléchargement : {int(status.progress() * 100)}% ...")

    print(f"[SUCCESS] Fichier téléchargé avec succès et enregistré sous : {destination_path}")
    return True
