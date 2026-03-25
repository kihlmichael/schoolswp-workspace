"""
Ré-auth + création du README consolidé dans Google Drive.
Scope requis : drive.file (écriture), documents (création Google Doc).
"""
import os
import sys

# Fix encoding Windows
sys.stdout.reconfigure(encoding="utf-8")

from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.http import MediaInMemoryUpload

FOLDER_ID = "1bZPi-D-DlBpJNrQG68FMsYtBH5EF_PaG"
TOKEN_PATH = os.path.join(os.path.dirname(__file__), "token-gdrive-write.json")
CREDS_PATH = os.path.join(os.path.dirname(__file__), "..", "..", "credentials-gdrive-audit.json")
README_PATH = os.path.join(os.path.dirname(__file__), "README-WORKSPACE-CONSOLIDE.md")

SCOPES = [
    "https://www.googleapis.com/auth/drive.file",
]

# Auth
if os.path.exists(TOKEN_PATH):
    from google.oauth2.credentials import Credentials
    creds = Credentials.from_authorized_user_file(TOKEN_PATH)
    if not creds.valid:
        print("Token expiré — relancement du flow OAuth...")
        os.remove(TOKEN_PATH)
        creds = None
else:
    creds = None

if creds is None:
    print("Authentification requise (scope: drive.file)...")
    print("Un serveur local va démarrer sur http://localhost:8080")
    print("Copie l'URL dans ton navigateur si l'onglet ne s'ouvre pas.\n")
    flow = InstalledAppFlow.from_client_secrets_file(CREDS_PATH, SCOPES)
    creds = flow.run_local_server(
        port=8081,
        open_browser=False,
        success_message="Authentification réussie. Tu peux fermer cet onglet."
    )
    with open(TOKEN_PATH, "w") as f:
        f.write(creds.to_json())
    print(f"Token sauvegardé dans {TOKEN_PATH}\n")

service = build("drive", "v3", credentials=creds)

# Lire le README local
with open(README_PATH, "r", encoding="utf-8") as f:
    content = f.read()

# Créer le Google Doc dans le dossier cible
file_metadata = {
    "name": "README — Espace de travail",
    "mimeType": "application/vnd.google-apps.document",
    "parents": [FOLDER_ID],
}

# Upload en tant que texte plain (Drive le convertit en Google Doc)
media = MediaInMemoryUpload(
    content.encode("utf-8"),
    mimetype="text/plain",
    resumable=False,
)

print("Création du Google Doc dans Drive...")
file = service.files().create(
    body=file_metadata,
    media_body=media,
    fields="id, name, webViewLink"
).execute()

print(f"\nREADME créé avec succès !")
print(f"  Nom    : {file['name']}")
print(f"  ID     : {file['id']}")
print(f"  Lien   : {file['webViewLink']}")
