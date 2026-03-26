#!/usr/bin/env python3
"""
Dispatche les PDFs du dossier _TRI_PDF vers les bons dossiers.

Mode preview par défaut. Ajouter --apply pour exécuter.
"""

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

SOURCE_FOLDER = "1-Fe7JiFc1UFlXNrY_DTSzXfjm4OV9l4m"

# Dossiers cibles
MEDICAL = "1FTXIcCPXiZITZtnvKJyIkGGJeiGBkJ5k"       # 08_PERSONNEL/01_Medical
PERSONNEL = "1j7qtlbP9ysT1ZGMKvJJwusSawViO_2qZ"      # 08_PERSONNEL
SEO = "1QwHLKJ8QTmCvUU08WRJiPENVgxr671XN"            # 02_PROJETS/schoolsWP/02_SEO
PROMPT = "1Z6LcLQqYhnT7f0IpYI2YHROJChHKtD6u"         # 02_PROJETS/schoolsWP/04_Prompt
PDF_ASSETS = "14BRdge7rzTrt_9RBe0RX1NT6scGsZhao"     # 02_PROJETS/schoolsWP/01_Assets/04_PDF-Documents
ADMIN = "1CVEHeKlVJl4EzJtwKKVbbeO5Es-gWAnU"           # 01_ADMIN

# Mots-cles medicaux
MEDICAL_KEYWORDS = [
    "Randrianjohany", "Laugros", "Labaki", "Eyer",
    "CARDIO", "HOLTER", "IRM", "EMG", "neurologie",
    "CR CS", "imagerie medicale", "dimagerie",
    "CONSULTATION", "KIHL.MICHAEL", "KIHL.pdf",
    "VM REPRISE",
]

# Mapping explicite par nom (partiel)
EXPLICIT_MAP = {
    "ORIGINAL Paul Grillet SEO": SEO,
    "TBL WEEK-END Monetisation": SEO,
    "ORIGINAL WP Sensei Prompt Affiliation": PROMPT,
    "Modele de Rapport dAudit Technique": PDF_ASSETS,
    "Label-OL": ADMIN,
    "Catch-Booking": ADMIN,
    "Katoen Natie": ADMIN,
    "Bilan-periodique-KIHL-Mae": PERSONNEL,
}


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


def classify(name):
    """Determine le dossier cible en fonction du nom."""
    # Mapping explicite d'abord
    for pattern, target in EXPLICIT_MAP.items():
        if pattern in name:
            return target

    # Mots-cles medicaux
    for kw in MEDICAL_KEYWORDS:
        if kw.lower() in name.lower():
            return MEDICAL

    # Fallback
    return None


FOLDER_LABELS = {
    MEDICAL: "08_PERSONNEL/01_Medical",
    PERSONNEL: "08_PERSONNEL",
    SEO: "02_PROJETS/schoolsWP/02_SEO",
    PROMPT: "02_PROJETS/schoolsWP/04_Prompt",
    PDF_ASSETS: "01_Assets/04_PDF-Documents",
    ADMIN: "01_ADMIN",
}


def main():
    apply_mode = "--apply" in sys.argv

    mode = "APPLICATION" if apply_mode else "PREVIEW"
    print("=" * 60)
    print(f"  DISPATCH PDF — MODE {mode}")
    print("=" * 60)

    print("\n[1/3] Authentification...")
    service = authenticate()
    print("  OK")

    print("\n[2/3] Scan du dossier _TRI_PDF...")
    all_files = []
    page_token = None
    while True:
        results = (
            service.files()
            .list(
                q=f"'{SOURCE_FOLDER}' in parents and trashed = false",
                pageSize=500,
                fields="nextPageToken, files(id, name, parents)",
                pageToken=page_token,
            )
            .execute()
        )
        all_files.extend(results.get("files", []))
        page_token = results.get("nextPageToken")
        if not page_token:
            break

    print(f"  Trouves : {len(all_files)} fichiers\n")

    # Classifier
    classified = []
    unclassified = []
    for f in all_files:
        target = classify(f["name"])
        if target:
            classified.append((f, target))
        else:
            unclassified.append(f)

    # Afficher par destination
    by_dest = {}
    for f, target in classified:
        by_dest.setdefault(target, []).append(f)

    for target, files in by_dest.items():
        label = FOLDER_LABELS.get(target, target)
        print(f"  -> {label} ({len(files)} fichiers)")
        for f in files:
            print(f"     - {f['name'][:80]}")
        print()

    if unclassified:
        print(f"  ?? NON CLASSES ({len(unclassified)} fichiers)")
        for f in unclassified:
            print(f"     - {f['name'][:80]}")
        print()

    if not apply_mode:
        print("=" * 60)
        print("  MODE PREVIEW — aucune modification")
        print("  Pour appliquer : ajouter --apply")
        print("=" * 60)
        return

    # Confirmation
    print(f"  {len(classified)} fichiers seront deplaces.")
    if unclassified:
        print(f"  {len(unclassified)} fichiers non classes seront ignores.")
    confirm = input("  Confirmer ? (taper 'OUI') : ")
    if confirm != "OUI":
        print("  Annule.")
        return

    print(f"\n[3/3] Deplacement de {len(classified)} fichiers...")
    success = 0
    errors = 0
    log = []

    for f, target in classified:
        entry = {
            "id": f["id"],
            "name": f["name"],
            "target": FOLDER_LABELS.get(target, target),
            "timestamp": datetime.now().isoformat(),
        }
        try:
            old_parents = f.get("parents", [SOURCE_FOLDER])
            service.files().update(
                fileId=f["id"],
                addParents=target,
                removeParents=",".join(old_parents),
                fields="id, parents",
            ).execute()
            entry["result"] = "SUCCESS"
            success += 1
        except HttpError as e:
            entry["result"] = "ERROR"
            entry["error"] = str(e)
            errors += 1
            print(f"  ERREUR : {f['name'][:60]} — {e}")
        log.append(entry)

    os.makedirs(OUTPUT_DIR, exist_ok=True)
    ts = datetime.now().strftime("%Y%m%d_%H%M%S")
    log_path = os.path.join(OUTPUT_DIR, f"dispatch_pdf_{ts}.json")
    with open(log_path, "w", encoding="utf-8") as fp:
        json.dump(
            {
                "applied_at": datetime.now().isoformat(),
                "total": len(classified),
                "success": success,
                "errors": errors,
                "skipped": len(unclassified),
                "operations": log,
            },
            fp,
            ensure_ascii=False,
            indent=2,
        )

    print(f"\n  Log : {log_path}")
    print("\n" + "=" * 60)
    print(f"  TERMINE — {success} deplaces, {errors} erreurs, {len(unclassified)} ignores")
    print("=" * 60)


if __name__ == "__main__":
    main()
