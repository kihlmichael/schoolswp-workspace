#!/usr/bin/env python3
"""
Déplace tout le contenu d'un dossier source vers un dossier cible.

Mode preview par défaut. Ajouter --apply pour exécuter.

Usage :
  python gdrive-move-folder-contents.py --source FOLDER_ID --target FOLDER_ID
  python gdrive-move-folder-contents.py --source FOLDER_ID --target FOLDER_ID --apply
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


def authenticate():
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


def list_folder(service, folder_id):
    all_files = []
    page_token = None
    while True:
        results = (
            service.files()
            .list(
                q=f"'{folder_id}' in parents and trashed = false",
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


def main():
    parser = argparse.ArgumentParser(
        description="Deplace tout le contenu d'un dossier vers un autre"
    )
    parser.add_argument("--source", required=True, help="ID du dossier source")
    parser.add_argument("--target", required=True, help="ID du dossier cible")
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
    print(f"  DEPLACEMENT DOSSIER > DOSSIER — MODE {mode}")
    print(f"  Source : {args.source}")
    print(f"  Cible  : {args.target}")
    print("=" * 60)

    print("\n[1/3] Authentification...")
    service = authenticate()
    print("  OK")

    print("\n[2/3] Scan du dossier source...")
    files = list_folder(service, args.source)
    print(f"  Trouves : {len(files)} fichiers")

    if not files:
        print("\n  Dossier vide, rien a deplacer.")
        return

    if args.limit:
        files = files[: args.limit]
        print(f"  Limite a {args.limit} fichiers")

    if not args.apply:
        for i, f in enumerate(files[:20]):
            print(f"  {i + 1:3d}. {f['name'][:80]}")
        if len(files) > 20:
            print(f"  ... et {len(files) - 20} autres")
        print("\n" + "=" * 60)
        print("  MODE PREVIEW — aucune modification")
        print("  Pour appliquer : ajouter --apply")
        print("=" * 60)
        return

    print(f"\n  {len(files)} fichiers seront deplaces.")
    confirm = input("  Confirmer ? (taper 'OUI') : ")
    if confirm != "OUI":
        print("  Annule.")
        return

    print(f"\n[3/3] Deplacement de {len(files)} fichiers...")
    success = 0
    errors = 0
    log = []

    for i, f in enumerate(files):
        entry = {
            "id": f["id"],
            "name": f["name"],
            "timestamp": datetime.now().isoformat(),
        }
        try:
            old_parents = f.get("parents", [args.source])
            service.files().update(
                fileId=f["id"],
                addParents=args.target,
                removeParents=",".join(old_parents),
                fields="id, parents",
            ).execute()
            entry["result"] = "SUCCESS"
            success += 1
            if (i + 1) % 50 == 0:
                print(f"    ... {i + 1}/{len(files)}")
        except HttpError as e:
            entry["result"] = "ERROR"
            entry["error"] = str(e)
            errors += 1
            print(f"  ERREUR : {f['name'][:60]} — {e}")
        log.append(entry)

    os.makedirs(OUTPUT_DIR, exist_ok=True)
    ts = datetime.now().strftime("%Y%m%d_%H%M%S")
    log_path = os.path.join(OUTPUT_DIR, f"move_folder_contents_{ts}.json")
    with open(log_path, "w", encoding="utf-8") as fp:
        json.dump(
            {
                "applied_at": datetime.now().isoformat(),
                "source": args.source,
                "target": args.target,
                "total": len(files),
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
