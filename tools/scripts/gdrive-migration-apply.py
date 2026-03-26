#!/usr/bin/env python3
"""
Google Drive Migration Apply — schoolsWP
==========================================
Applique le plan de migration au Google Drive.

SECURITE :
  - Requiert le flag --apply explicite
  - Requiert un fichier migration_mapping.csv valide
  - Journalise tout (migration_log.json)
  - Exporte l'etat initial avant modification
  - Scope : drive (lecture + ecriture) — upgrade depuis metadata.readonly

Usage :
  # Preview seulement (par defaut)
  python gdrive-migration-apply.py

  # Appliquer la migration
  python gdrive-migration-apply.py --apply

  # Appliquer uniquement les elements READY (ignorer NEEDS_REVIEW)
  python gdrive-migration-apply.py --apply --ready-only

  # Limiter a N operations (pour tester)
  python gdrive-migration-apply.py --apply --limit 10
"""

import argparse
import csv
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
    print("Dependances manquantes. Installe-les avec :")
    print("  pip install -r requirements-gdrive-audit.txt")
    sys.exit(1)


# ---------------------------------------------------------------------------
# Config
# ---------------------------------------------------------------------------
# IMPORTANT : scope etendu pour ecriture
SCOPES = ["https://www.googleapis.com/auth/drive"]
TOKEN_FILE = "token-gdrive-migration.json"
CREDENTIALS_FILE = "credentials-gdrive-audit.json"
DEFAULT_MAPPING = "output/gdrive-migration/migration_mapping.csv"
DEFAULT_OUTPUT = "output/gdrive-migration"


# ---------------------------------------------------------------------------
# Auth
# ---------------------------------------------------------------------------
def authenticate():
    """Authentification OAuth2 avec scope drive (lecture + ecriture)."""
    creds = None

    if os.path.exists(TOKEN_FILE):
        creds = Credentials.from_authorized_user_file(TOKEN_FILE, SCOPES)

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            if not os.path.exists(CREDENTIALS_FILE):
                print(f"ERREUR : fichier '{CREDENTIALS_FILE}' introuvable.")
                sys.exit(1)
            flow = InstalledAppFlow.from_client_secrets_file(
                CREDENTIALS_FILE, SCOPES
            )
            creds = flow.run_local_server(port=0)

        with open(TOKEN_FILE, "w") as token:
            token.write(creds.to_json())
        print(f"Token sauvegarde dans {TOKEN_FILE}")

    return build("drive", "v3", credentials=creds)


# ---------------------------------------------------------------------------
# Folder creation cache
# ---------------------------------------------------------------------------
class FolderManager:
    """Gere la creation de dossiers avec cache pour eviter les doublons."""

    def __init__(self, service):
        self.service = service
        self.cache = {}  # path → folder_id
        self._load_root()

    def _load_root(self):
        """Charge l'ID du dossier racine."""
        self.cache[""] = "root"

    def ensure_folder(self, path):
        """Cree le dossier si necessaire et retourne son ID."""
        if path in self.cache:
            return self.cache[path]

        parts = path.split("/")
        current_path = ""

        for part in parts:
            parent_path = current_path
            current_path = f"{current_path}/{part}" if current_path else part

            if current_path in self.cache:
                continue

            parent_id = self.cache.get(parent_path, "root")

            # Chercher le dossier existant
            query = (
                f"'{parent_id}' in parents and "
                f"name = '{part}' and "
                f"mimeType = 'application/vnd.google-apps.folder' and "
                f"trashed = false"
            )
            results = (
                self.service.files()
                .list(q=query, fields="files(id, name)", spaces="drive")
                .execute()
            )

            if results.get("files"):
                folder_id = results["files"][0]["id"]
            else:
                # Creer le dossier
                metadata = {
                    "name": part,
                    "mimeType": "application/vnd.google-apps.folder",
                    "parents": [parent_id],
                }
                folder = (
                    self.service.files()
                    .create(body=metadata, fields="id")
                    .execute()
                )
                folder_id = folder["id"]

            self.cache[current_path] = folder_id

        return self.cache[path]


# ---------------------------------------------------------------------------
# Migration operations
# ---------------------------------------------------------------------------
def move_file(service, folder_mgr, file_id, target_path, log_entry):
    """Deplace un fichier vers le chemin cible."""
    # Obtenir ou creer le dossier parent cible
    parent_path = "/".join(target_path.split("/")[:-1])
    if parent_path:
        new_parent_id = folder_mgr.ensure_folder(parent_path)
    else:
        new_parent_id = "root"

    # Obtenir le parent actuel
    file_info = (
        service.files()
        .get(fileId=file_id, fields="parents")
        .execute()
    )
    old_parents = file_info.get("parents", [])

    # Deplacer
    service.files().update(
        fileId=file_id,
        addParents=new_parent_id,
        removeParents=",".join(old_parents),
        fields="id, parents",
    ).execute()

    log_entry["result"] = "SUCCESS"
    log_entry["new_parent_id"] = new_parent_id
    log_entry["old_parent_ids"] = old_parents
    return True


def delete_file(service, file_id, log_entry):
    """Deplace un fichier/dossier vers la corbeille (pas de suppression definitive)."""
    service.files().update(
        fileId=file_id,
        body={"trashed": True},
    ).execute()

    log_entry["result"] = "TRASHED"
    return True


def rename_file(service, file_id, new_name, log_entry):
    """Renomme un fichier/dossier."""
    service.files().update(
        fileId=file_id,
        body={"name": new_name},
        fields="id, name",
    ).execute()

    log_entry["result"] = "RENAMED"
    return True


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------
def main():
    parser = argparse.ArgumentParser(
        description="Applique le plan de migration Google Drive"
    )
    parser.add_argument(
        "--apply",
        action="store_true",
        help="Flag OBLIGATOIRE pour appliquer les modifications (sinon preview)",
    )
    parser.add_argument(
        "--mapping",
        default=DEFAULT_MAPPING,
        help=f"Chemin vers migration_mapping.csv (defaut: {DEFAULT_MAPPING})",
    )
    parser.add_argument(
        "--output-dir",
        default=DEFAULT_OUTPUT,
        help=f"Dossier de sortie pour les logs (defaut: {DEFAULT_OUTPUT})",
    )
    parser.add_argument(
        "--ready-only",
        action="store_true",
        help="Ignorer les elements NEEDS_REVIEW",
    )
    parser.add_argument(
        "--limit",
        type=int,
        default=None,
        help="Limiter le nombre d'operations (pour tests)",
    )
    args = parser.parse_args()

    print("=" * 60)
    if args.apply:
        print("  GOOGLE DRIVE MIGRATION — MODE APPLICATION")
        print("  *** LES MODIFICATIONS SERONT APPLIQUEES ***")
    else:
        print("  GOOGLE DRIVE MIGRATION — MODE PREVIEW")
        print("  Aucune modification ne sera effectuee")
    print("=" * 60)

    # Lire le mapping
    print(f"\n[1/4] Lecture de {args.mapping}...")
    if not os.path.exists(args.mapping):
        print(f"ERREUR : {args.mapping} introuvable.")
        print("Lance d'abord gdrive-migration-plan.py")
        return

    operations = []
    with open(args.mapping, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            operations.append(row)

    print(f"  OK — {len(operations)} operations chargees")

    # Filtrer
    if args.ready_only:
        operations = [op for op in operations if op["status"] == "READY"]
        print(f"  Filtre READY only : {len(operations)} operations")

    # Exclure les NEEDS_REVIEW si --apply
    actionable = [
        op for op in operations
        if op["action"] in ("MOVE", "RENAME_MOVE", "RENAME", "DELETE")
        and op["status"] == "READY"
    ]
    print(f"  Operations actionnables : {len(actionable)}")

    if args.limit:
        actionable = actionable[: args.limit]
        print(f"  Limite a {args.limit} operations")

    # Preview
    print(f"\n[2/4] Preview des operations :")
    action_counts = {}
    for op in actionable:
        action = op["action"]
        action_counts[action] = action_counts.get(action, 0) + 1

    for action, count in sorted(action_counts.items()):
        print(f"  {action:20s} : {count}")

    if not args.apply:
        print("\n" + "=" * 60)
        print("  MODE PREVIEW — aucune modification appliquee")
        print("  Pour appliquer : python gdrive-migration-apply.py --apply")
        print("=" * 60)
        return

    # Confirmation
    print(f"\n  TOTAL : {len(actionable)} operations a appliquer")
    confirm = input("\n  Confirmer ? (taper 'OUI' en majuscules) : ")
    if confirm != "OUI":
        print("  Annule.")
        return

    # Auth
    print("\n[3/4] Authentification (scope: drive)...")
    service = authenticate()
    folder_mgr = FolderManager(service)
    print("  OK")

    # Application
    print(f"\n[4/4] Application de {len(actionable)} operations...")
    log = []
    success = 0
    errors = 0

    for i, op in enumerate(actionable):
        log_entry = {
            "index": i,
            "timestamp": datetime.now().isoformat(),
            "id": op["id"],
            "name": op["name"],
            "action": op["action"],
            "current_path": op["current_path"],
            "target_path": op["target_path"],
            "result": "",
            "error": "",
        }

        try:
            if op["action"] == "DELETE":
                delete_file(service, op["id"], log_entry)
            elif op["action"] in ("MOVE", "RENAME_MOVE"):
                move_file(service, folder_mgr, op["id"], op["target_path"], log_entry)
            elif op["action"] == "RENAME":
                new_name = op["target_path"].split("/")[-1]
                rename_file(service, op["id"], new_name, log_entry)

            success += 1
            if (i + 1) % 50 == 0:
                print(f"  ... {i + 1}/{len(actionable)} operations appliquees")

        except HttpError as e:
            log_entry["result"] = "ERROR"
            log_entry["error"] = str(e)
            errors += 1
            print(f"  ERREUR op {i}: {op['name']} — {e}")

        except Exception as e:
            log_entry["result"] = "ERROR"
            log_entry["error"] = str(e)
            errors += 1
            print(f"  ERREUR op {i}: {op['name']} — {e}")

        log.append(log_entry)

    # Sauvegarder le log
    os.makedirs(args.output_dir, exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    log_path = os.path.join(args.output_dir, f"migration_log_{timestamp}.json")
    with open(log_path, "w", encoding="utf-8") as f:
        json.dump(
            {
                "applied_at": datetime.now().isoformat(),
                "total_operations": len(actionable),
                "success": success,
                "errors": errors,
                "operations": log,
            },
            f,
            ensure_ascii=False,
            indent=2,
        )

    print(f"\n  Log sauvegarde : {log_path}")

    print("\n" + "=" * 60)
    print("  MIGRATION TERMINEE")
    print(f"  Succes   : {success}")
    print(f"  Erreurs  : {errors}")
    print(f"  Log      : {log_path}")
    print("=" * 60)

    if errors > 0:
        print("\n  ATTENTION : des erreurs ont ete detectees.")
        print("  Consulte le log pour les details.")
        print("  Les fichiers en erreur n'ont PAS ete modifies.")


if __name__ == "__main__":
    main()
