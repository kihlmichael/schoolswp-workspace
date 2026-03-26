"""Read all README files from Drive folder and save content locally."""
import sys
import os
import json
from googleapiclient.discovery import build
from google.oauth2.credentials import Credentials

FOLDER_ID = "1bZPi-D-DlBpJNrQG68FMsYtBH5EF_PaG"
TOKEN_PATH = os.path.join(os.path.dirname(__file__), "token-gdrive-audit.json")

creds = Credentials.from_authorized_user_file(TOKEN_PATH)
service = build("drive", "v3", credentials=creds)

# List all files in folder
results = service.files().list(
    q=f"'{FOLDER_ID}' in parents and trashed=false",
    fields="files(id, name, mimeType)",
    pageSize=100
).execute()

files = results.get("files", [])
print(f"Fichiers dans le dossier: {len(files)}", flush=True)

readme_files = []
for f in files:
    print(f"  {f['name']} ({f['mimeType']})", flush=True)
    if "README" in f["name"].upper():
        readme_files.append(f)

print(f"\nREADME trouvés: {len(readme_files)}", flush=True)

output = {}
for rf in readme_files:
    fid = rf["id"]
    name = rf["name"]
    mime = rf["mimeType"]

    print(f"\n--- {name} ---", flush=True)

    if "google-apps.document" in mime:
        # Export Google Doc as plain text
        content = service.files().export(fileId=fid, mimeType="text/plain").execute()
        text = content.decode("utf-8")
    else:
        # Download regular file
        content = service.files().get_media(fileId=fid).execute()
        text = content.decode("utf-8")

    sys.stdout.buffer.write((text[:500] + "\n").encode("utf-8"))
    sys.stdout.buffer.flush()
    output[name] = text

# Save to local JSON
out_path = os.path.join(os.path.dirname(__file__), "readmes-content.json")
with open(out_path, "w", encoding="utf-8") as f:
    json.dump(output, f, ensure_ascii=False, indent=2)

print(f"\nSauvegardé dans {out_path}", flush=True)
