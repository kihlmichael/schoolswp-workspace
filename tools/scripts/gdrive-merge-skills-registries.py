"""
One-shot : envoyer 2 anciens registres Skills (obsolètes) vers la corbeille Drive.

Le registre canonique reste : 1fA0BNReT0sBWEYJ7Jiq-9V-VxC7XBTUZBnZhgBdGIsk
("Claude Code Skills Registry — schoolsWP", target du webhook n8n actif).

Usage :
  python gdrive-merge-skills-registries.py            # dry-run (affiche, ne touche rien)
  python gdrive-merge-skills-registries.py --apply    # trash effectif

Reversible : les fichiers restent dans la corbeille 30 jours, restaurables via Drive UI.
"""

import argparse
import os
import sys

try:
    from google.auth.transport.requests import Request
    from google.oauth2.credentials import Credentials
    from google_auth_oauthlib.flow import InstalledAppFlow
    from googleapiclient.discovery import build
    from googleapiclient.errors import HttpError
except ImportError:
    print("Dependances manquantes : pip install google-api-python-client google-auth-oauthlib")
    sys.exit(1)

SCOPES = ["https://www.googleapis.com/auth/drive"]
HERE = os.path.dirname(os.path.abspath(__file__))
TOKEN_FILE = os.path.join(HERE, "token-gdrive-migration.json")
CREDENTIALS_FILE = os.path.join(HERE, "credentials-gdrive-audit.json")

OBSOLETE = [
    {
        "id": "1pC24icB3oUfO-l8Xd09ErrHf7Bm_03j0YZsM4rkOWpg",
        "expected_title": "skills_registry",
        "reason": "snapshot mars 2026, paths plats, supplante par 1fA0BNRe",
    },
    {
        "id": "1wOwVwuthNSGTtFIlayXXEqDHt4NhhW3ftO-PF6qrVHY",
        "expected_title": "01_schoolsWP_SkillsRegistry_20260407",
        "reason": "snapshot manuel avril 2026, fusionne dans 1fA0BNRe via webhook",
    },
]
CANONICAL_ID = "1fA0BNReT0sBWEYJ7Jiq-9V-VxC7XBTUZBnZhgBdGIsk"
CANONICAL_TITLE = "Claude Code Skills Registry — schoolsWP"


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
            flow = InstalledAppFlow.from_client_secrets_file(CREDENTIALS_FILE, SCOPES)
            creds = flow.run_local_server(port=0)
        with open(TOKEN_FILE, "w") as token:
            token.write(creds.to_json())
    return build("drive", "v3", credentials=creds)


def fetch_metadata(service, file_id):
    return (
        service.files()
        .get(fileId=file_id, fields="id, name, mimeType, modifiedTime, trashed")
        .execute()
    )


def trash_file(service, file_id):
    return (
        service.files()
        .update(fileId=file_id, body={"trashed": True}, fields="id, name, trashed")
        .execute()
    )


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--apply", action="store_true", help="Trash effectif (defaut: dry-run)")
    args = parser.parse_args()

    service = authenticate()

    print("\n=== Verification du registre canonique ===")
    canon = fetch_metadata(service, CANONICAL_ID)
    print(f"  KEEP  {canon['id']}  {canon['name']}  (modif {canon['modifiedTime']})")
    if canon["name"] != CANONICAL_TITLE:
        print(f"  ATTENTION : titre attendu '{CANONICAL_TITLE}', trouve '{canon['name']}'")
        print("  Aborting par securite.")
        sys.exit(2)
    if canon.get("trashed"):
        print("  ATTENTION : le canonique est dans la corbeille -- aborting.")
        sys.exit(2)

    print("\n=== Fichiers a envoyer en corbeille ===")
    for item in OBSOLETE:
        try:
            meta = fetch_metadata(service, item["id"])
        except HttpError as e:
            print(f"  SKIP  {item['id']}  introuvable ou pas d'acces : {e}")
            item["skip"] = True
            continue
        item["meta"] = meta
        marker = "DEJA TRASH" if meta.get("trashed") else "TRASH"
        print(f"  {marker}  {meta['id']}  {meta['name']}")
        print(f"        raison : {item['reason']}")
        if meta["name"] != item["expected_title"]:
            print(
                f"        WARN : titre attendu '{item['expected_title']}', trouve '{meta['name']}'"
            )

    if not args.apply:
        print("\nDry-run termine. Relancer avec --apply pour envoyer en corbeille.")
        return

    print("\n=== Trash en cours ===")
    for item in OBSOLETE:
        if item.get("skip"):
            continue
        meta = item.get("meta", {})
        if meta.get("trashed"):
            print(f"  SKIP  {item['id']}  deja trash")
            continue
        try:
            res = trash_file(service, item["id"])
            print(f"  OK    {res['id']}  trashed={res.get('trashed')}  ({res.get('name')})")
        except HttpError as e:
            print(f"  FAIL  {item['id']}  {e}")

    print("\nFusion terminee. Restauration possible 30j via Drive UI > Corbeille.")


if __name__ == "__main__":
    main()
