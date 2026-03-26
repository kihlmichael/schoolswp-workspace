#!/usr/bin/env python3
"""
Déplace les articles schoolsWP d'une langue donnée de la racine vers un dossier cible.

Mode preview par défaut. Ajouter --apply pour exécuter.

Usage :
  python gdrive-move-articles.py --lang EN --target FOLDER_ID
  python gdrive-move-articles.py --lang EN --target FOLDER_ID --apply
  python gdrive-move-articles.py --lang DE --target FOLDER_ID --apply --limit 5
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


def find_articles(service, lang):
    """Trouve tous les fichiers '- Article - LANG' a la racine."""
    all_files = []
    page_token = None
    search_pattern = f"- Article - {lang}"

    while True:
        query = (
            "'root' in parents and "
            "trashed = false and "
            "mimeType = 'application/vnd.google-apps.document' and "
            f"name contains '{search_pattern}'"
        )
        results = (
            service.files()
            .list(
                q=query,
                pageSize=200,
                fields="nextPageToken, files(id, name, parents)",
                pageToken=page_token,
            )
            .execute()
        )
        all_files.extend(results.get("files", []))
        page_token = results.get("nextPageToken")
        if not page_token:
            break

    return all_files


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
        description="Deplace les articles d'une langue vers un dossier cible"
    )
    parser.add_argument(
        "--lang", required=True,
        help="Code langue (FR, EN, DE)",
    )
    parser.add_argument(
        "--target", required=True,
        help="ID du dossier cible Google Drive",
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

    lang = args.lang.upper()
    mode = "APPLICATION" if args.apply else "PREVIEW"
    print("=" * 60)
    print(f"  MIGRATION ARTICLES {lang} — MODE {mode}")
    print(f"  Cible : {args.target}")
    print("=" * 60)

    print("\n[1/3] Authentification...")
    service = authenticate()
    print("  OK")

    print(f"\n[2/3] Recherche des articles {lang} a la racine...")
    articles = find_articles(service, lang)
    print(f"  Trouves : {len(articles)} articles")

    if not articles:
        print("\n  Aucun article a deplacer.")
        return

    if args.limit:
        articles = articles[: args.limit]
        print(f"  Limite a {args.limit} articles")

    for i, f in enumerate(articles):
        print(f"  {i + 1:3d}. {f['name']}")

    if not args.apply:
        print("\n" + "=" * 60)
        print("  MODE PREVIEW — aucune modification")
        print(f"  Pour appliquer : ajouter --apply")
        print("=" * 60)
        return

    print(f"\n  {len(articles)} articles seront deplaces.")
    confirm = input("  Confirmer ? (taper 'OUI') : ")
    if confirm != "OUI":
        print("  Annule.")
        return

    print(f"\n[3/3] Deplacement de {len(articles)} articles...")
    success = 0
    errors = 0
    log = []

    for i, f in enumerate(articles):
        entry = {
            "id": f["id"],
            "name": f["name"],
            "timestamp": datetime.now().isoformat(),
        }
        try:
            old_parents = f.get("parents", ["root"])
            move_file(service, f["id"], old_parents, args.target)
            entry["result"] = "SUCCESS"
            success += 1
            if (i + 1) % 20 == 0:
                print(f"  ... {i + 1}/{len(articles)}")
        except HttpError as e:
            entry["result"] = "ERROR"
            entry["error"] = str(e)
            errors += 1
            print(f"  ERREUR : {f['name']} — {e}")
        log.append(entry)

    os.makedirs(OUTPUT_DIR, exist_ok=True)
    ts = datetime.now().strftime("%Y%m%d_%H%M%S")
    log_path = os.path.join(
        OUTPUT_DIR, f"move_articles_{lang.lower()}_{ts}.json"
    )
    with open(log_path, "w", encoding="utf-8") as fp:
        json.dump(
            {
                "applied_at": datetime.now().isoformat(),
                "lang": lang,
                "target_folder": args.target,
                "total": len(articles),
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
