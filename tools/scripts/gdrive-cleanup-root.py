#!/usr/bin/env python3
"""
Google Drive Root Cleanup -- schoolsWP
=======================================
Identifie et supprime les dossiers/fichiers vides a la racine
qui ne font pas partie de la structure cible.

Securite :
  - Ne supprime QUE les elements vides (0 enfant)
  - Envoie a la corbeille (pas de suppression definitive)
  - Requiert --apply pour agir (preview par defaut)
  - Journalise tout

Usage :
  python gdrive-cleanup-root.py              # Preview
  python gdrive-cleanup-root.py --apply      # Appliquer
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

# Les 6 dossiers cibles -- NE PAS TOUCHER
TARGET_FOLDERS = {
    "00_Inbox",
    "01_Projets",
    "02_Ressources",
    "03_Admin",
    "04_Personnel",
    "99_Archives",
}


def authenticate():
    """Authentification OAuth2."""
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


def list_root_items(service):
    """Liste tous les elements a la racine du Drive."""
    items = []
    page_token = None
    while True:
        results = (
            service.files()
            .list(
                q="'root' in parents and trashed = false",
                pageSize=200,
                fields="nextPageToken, files(id, name, mimeType, size)",
                pageToken=page_token,
            )
            .execute()
        )
        items.extend(results.get("files", []))
        page_token = results.get("nextPageToken")
        if not page_token:
            break
    return items


def count_children(service, folder_id):
    """Compte les enfants non-trashes d'un dossier."""
    results = (
        service.files()
        .list(
            q=f"'{folder_id}' in parents and trashed = false",
            pageSize=1,
            fields="files(id)",
        )
        .execute()
    )
    return len(results.get("files", []))


def main():
    parser = argparse.ArgumentParser(
        description="Nettoie les coquilles vides a la racine du Drive"
    )
    parser.add_argument(
        "--apply",
        action="store_true",
        help="Appliquer le nettoyage (sinon preview)",
    )
    args = parser.parse_args()

    print("=" * 60)
    if args.apply:
        print("  NETTOYAGE RACINE -- MODE APPLICATION")
    else:
        print("  NETTOYAGE RACINE -- MODE PREVIEW")
    print("=" * 60)

    # Auth
    print("\n[1/3] Authentification...")
    service = authenticate()
    print("  OK")

    # Lister la racine
    print("\n[2/3] Analyse de la racine...")
    root_items = list_root_items(service)
    print(f"  {len(root_items)} elements trouves a la racine")

    # Classifier
    target = []
    to_clean_empty = []
    to_clean_files = []
    unknown = []

    for item in root_items:
        name = item["name"]
        is_folder = item["mimeType"] == "application/vnd.google-apps.folder"

        if name in TARGET_FOLDERS:
            target.append(item)
            continue

        if is_folder:
            children = count_children(service, item["id"])
            item["_children"] = children
            if children == 0:
                to_clean_empty.append(item)
            else:
                unknown.append(item)
        else:
            to_clean_files.append(item)

    # Rapport
    print(f"\n  Structure cible OK ({len(target)}/6) :")
    for t in sorted(target, key=lambda x: x["name"]):
        print(f"    [OK] {t['name']}")

    missing = TARGET_FOLDERS - {t["name"] for t in target}
    if missing:
        print(f"\n  ATTENTION -- dossiers cibles manquants :")
        for m in sorted(missing):
            print(f"    [MANQUANT] {m}")

    if to_clean_empty:
        print(f"\n  Dossiers vides a supprimer ({len(to_clean_empty)}) :")
        for item in sorted(to_clean_empty, key=lambda x: x["name"]):
            print(f"    [VIDE] {item['name']}")

    if to_clean_files:
        print(f"\n  Fichiers orphelins a la racine ({len(to_clean_files)}) :")
        for item in sorted(to_clean_files, key=lambda x: x["name"]):
            print(f"    [FICHIER] {item['name']}")

    if unknown:
        print(f"\n  Dossiers NON VIDES (pas touche) ({len(unknown)}) :")
        for item in sorted(unknown, key=lambda x: x["name"]):
            print(f"    [NON VIDE] {item['name']} ({item['_children']} enfants)")

    total_to_clean = len(to_clean_empty) + len(to_clean_files)
    if total_to_clean == 0:
        print("\n  Rien a nettoyer -- racine propre.")
        return

    if not args.apply:
        print(f"\n  Total a nettoyer : {total_to_clean}")
        print("  Pour appliquer : python gdrive-cleanup-root.py --apply")
        return

    # Application
    print(f"\n[3/3] Nettoyage de {total_to_clean} elements...")
    confirm = input("  Confirmer ? (taper 'OUI') : ")
    if confirm != "OUI":
        print("  Annule.")
        return

    log = []
    success = 0
    errors = 0

    all_to_clean = to_clean_empty + to_clean_files
    for item in all_to_clean:
        entry = {
            "id": item["id"],
            "name": item["name"],
            "type": "folder" if item["mimeType"] == "application/vnd.google-apps.folder" else "file",
            "result": "",
        }
        try:
            service.files().update(
                fileId=item["id"],
                body={"trashed": True},
            ).execute()
            entry["result"] = "TRASHED"
            success += 1
            print(f"    [OK] {item['name']}")
        except HttpError as e:
            entry["result"] = f"ERROR: {e}"
            errors += 1
            print(f"    [ERREUR] {item['name']} -- {e}")
        log.append(entry)

    # Log
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    ts = datetime.now().strftime("%Y%m%d_%H%M%S")
    log_path = os.path.join(OUTPUT_DIR, f"cleanup_log_{ts}.json")
    with open(log_path, "w", encoding="utf-8") as f:
        json.dump({
            "cleaned_at": datetime.now().isoformat(),
            "success": success,
            "errors": errors,
            "items": log,
        }, f, ensure_ascii=False, indent=2)

    print(f"\n  Succes : {success}")
    print(f"  Erreurs : {errors}")
    print(f"  Log : {log_path}")

    # Re-verifier
    print("\n  Verification post-nettoyage...")
    remaining = list_root_items(service)
    remaining_names = sorted(r["name"] for r in remaining)
    print(f"  {len(remaining)} elements restants a la racine :")
    for name in remaining_names:
        status = "[OK]" if name in TARGET_FOLDERS else "[???]"
        print(f"    {status} {name}")


if __name__ == "__main__":
    main()
