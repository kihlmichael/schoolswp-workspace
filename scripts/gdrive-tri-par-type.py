#!/usr/bin/env python3
"""
Trie les fichiers à la racine du Google Drive par type MIME dans des dossiers _TRI_*.

Mode preview par défaut. Ajouter --apply pour exécuter.

Usage :
  python gdrive-tri-par-type.py                # preview
  python gdrive-tri-par-type.py --apply         # appliquer
  python gdrive-tri-par-type.py --apply --limit 10  # tester sur 10
"""

import argparse
import json
import os
import sys
from datetime import datetime

try:
    from google.auth.transport.requests import Request
    from google.oauth2.credentials import Credentials
    from google_auth_oauthlib.flow import InstalledAppFlow
    from googleapiclient.discovery import build
    from googleapiclient.errors import HttpError
except ImportError:
    print("Dependances manquantes.")
    print("  pip install -r requirements-gdrive-audit.txt")
    sys.exit(1)

SCOPES = ["https://www.googleapis.com/auth/drive"]
TOKEN_FILE = "token-gdrive-migration.json"
CREDENTIALS_FILE = "credentials-gdrive-audit.json"
OUTPUT_DIR = "output/gdrive-migration"

# Mapping type MIME → nom de dossier _TRI_
MIME_TO_FOLDER = {
    "application/vnd.google-apps.spreadsheet": "_TRI_Google-Sheets",
    "application/vnd.google-apps.document": "_TRI_Google-Docs",
    "application/vnd.google-apps.presentation": "_TRI_Google-Slides",
    "application/pdf": "_TRI_PDF",
    "image/png": "_TRI_Images",
    "image/jpeg": "_TRI_Images",
    "image/gif": "_TRI_Images",
    "image/webp": "_TRI_Images",
    "image/svg+xml": "_TRI_Images",
    "image/bmp": "_TRI_Images",
}

FALLBACK_FOLDER = "_TRI_Autres"


def authenticate():
    """Auth OAuth2 avec scope drive (lecture + ecriture)."""
    creds = None
    if os.path.exists(TOKEN_FILE):
        creds = Credentials.from_authorized_user_file(TOKEN_FILE, SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            if not os.path.exists(CREDENTIALS_FILE):
                print(f"ERREUR : '{CREDENTIALS_FILE}' introuvable.")
                sys.exit(1)
            flow = InstalledAppFlow.from_client_secrets_file(
                CREDENTIALS_FILE, SCOPES
            )
            creds = flow.run_local_server(port=0)
        with open(TOKEN_FILE, "w") as token:
            token.write(creds.to_json())
    return build("drive", "v3", credentials=creds)


def list_root_files(service):
    """Liste tous les fichiers (non-dossiers) a la racine."""
    all_files = []
    page_token = None

    while True:
        results = (
            service.files()
            .list(
                q=(
                    "'root' in parents and "
                    "trashed = false and "
                    "mimeType != 'application/vnd.google-apps.folder'"
                ),
                pageSize=500,
                fields="nextPageToken, files(id, name, mimeType, parents)",
                pageToken=page_token,
            )
            .execute()
        )
        all_files.extend(results.get("files", []))
        page_token = results.get("nextPageToken")
        if not page_token:
            break

    return all_files


def get_or_create_folder(service, folder_name, cache):
    """Recupere ou cree un dossier a la racine. Utilise un cache."""
    if folder_name in cache:
        return cache[folder_name]

    # Chercher le dossier existant
    query = (
        "'root' in parents and "
        f"name = '{folder_name}' and "
        "mimeType = 'application/vnd.google-apps.folder' and "
        "trashed = false"
    )
    results = (
        service.files()
        .list(q=query, fields="files(id, name)", spaces="drive")
        .execute()
    )

    if results.get("files"):
        folder_id = results["files"][0]["id"]
    else:
        metadata = {
            "name": folder_name,
            "mimeType": "application/vnd.google-apps.folder",
            "parents": ["root"],
        }
        folder = (
            service.files()
            .create(body=metadata, fields="id")
            .execute()
        )
        folder_id = folder["id"]
        print(f"    Dossier cree : {folder_name}")

    cache[folder_name] = folder_id
    return folder_id


def move_file(service, file_id, old_parents, target_id):
    """Deplace un fichier vers le dossier cible."""
    service.files().update(
        fileId=file_id,
        addParents=target_id,
        removeParents=",".join(old_parents),
        fields="id, parents",
    ).execute()


def main():
    parser = argparse.ArgumentParser(
        description="Trie les fichiers racine par type dans des dossiers _TRI_*"
    )
    parser.add_argument(
        "--apply", action="store_true",
        help="Appliquer les deplacements (sinon preview)",
    )
    parser.add_argument(
        "--limit", type=int, default=None,
        help="Limiter le nombre d'operations",
    )
    args = parser.parse_args()

    mode = "APPLICATION" if args.apply else "PREVIEW"
    print("=" * 60)
    print(f"  TRI PAR TYPE MIME — MODE {mode}")
    print("=" * 60)

    print("\n[1/3] Authentification...")
    service = authenticate()
    print("  OK")

    print("\n[2/3] Scan des fichiers a la racine...")
    files = list_root_files(service)
    print(f"  Trouves : {len(files)} fichiers")

    if not files:
        print("\n  Aucun fichier a trier.")
        return

    # Classer par dossier cible
    buckets = {}
    for f in files:
        mime = f.get("mimeType", "")
        folder = MIME_TO_FOLDER.get(mime, FALLBACK_FOLDER)
        buckets.setdefault(folder, []).append(f)

    # Afficher le resume
    print("\n  Repartition :")
    for folder in sorted(buckets.keys()):
        count = len(buckets[folder])
        print(f"    {folder:30s} : {count:4d} fichiers")

    total = sum(len(v) for v in buckets.values())

    if args.limit:
        print(f"\n  Limite a {args.limit} operations")

    if not args.apply:
        # Afficher le detail par bucket
        for folder in sorted(buckets.keys()):
            print(f"\n  --- {folder} ({len(buckets[folder])}) ---")
            for i, f in enumerate(buckets[folder][:10]):
                mime_short = f["mimeType"].split(".")[-1] if "." in f["mimeType"] else f["mimeType"].split("/")[-1]
                print(f"    {i + 1:3d}. [{mime_short}] {f['name'][:80]}")
            if len(buckets[folder]) > 10:
                print(f"    ... et {len(buckets[folder]) - 10} autres")

        print("\n" + "=" * 60)
        print("  MODE PREVIEW — aucune modification")
        print("  Pour appliquer : ajouter --apply")
        print("=" * 60)
        return

    # Confirmation
    print(f"\n  {total} fichiers seront deplaces.")
    confirm = input("  Confirmer ? (taper 'OUI') : ")
    if confirm != "OUI":
        print("  Annule.")
        return

    print(f"\n[3/3] Deplacement de {total} fichiers...")
    folder_cache = {}
    success = 0
    errors = 0
    log = []
    ops_done = 0

    for folder in sorted(buckets.keys()):
        target_id = get_or_create_folder(service, folder, folder_cache)

        for f in buckets[folder]:
            if args.limit and ops_done >= args.limit:
                break

            entry = {
                "id": f["id"],
                "name": f["name"],
                "mimeType": f["mimeType"],
                "target_folder": folder,
                "timestamp": datetime.now().isoformat(),
            }
            try:
                old_parents = f.get("parents", ["root"])
                move_file(service, f["id"], old_parents, target_id)
                entry["result"] = "SUCCESS"
                success += 1
                ops_done += 1
                if ops_done % 50 == 0:
                    print(f"    ... {ops_done}/{total}")
            except HttpError as e:
                entry["result"] = "ERROR"
                entry["error"] = str(e)
                errors += 1
                ops_done += 1
                print(f"  ERREUR : {f['name'][:60]} — {e}")
            log.append(entry)

        if args.limit and ops_done >= args.limit:
            print(f"  Limite atteinte ({args.limit})")
            break

    # Sauvegarder le log
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    ts = datetime.now().strftime("%Y%m%d_%H%M%S")
    log_path = os.path.join(OUTPUT_DIR, f"tri_par_type_{ts}.json")
    with open(log_path, "w", encoding="utf-8") as fp:
        json.dump(
            {
                "applied_at": datetime.now().isoformat(),
                "total": ops_done,
                "success": success,
                "errors": errors,
                "operations": log,
            },
            fp,
            ensure_ascii=False,
            indent=2,
        )

    print(f"\n  Log : {log_path}")
    print("\n" + "=" * 60)
    print(f"  TERMINE — {success} deplaces, {errors} erreurs")
    print("=" * 60)


if __name__ == "__main__":
    main()
