#!/usr/bin/env python3
"""
Dispatche les Google Docs du dossier _TRI_Google-Docs vers les bons dossiers.

Mode preview par defaut. Ajouter --apply pour executer.
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

SOURCE_FOLDER = "1Juq8U6nOKF85phO9JcFsYQE2Y6WB84OH"

# Dossiers cibles
SEO = "1QwHLKJ8QTmCvUU08WRJiPENVgxr671XN"             # 02_PROJETS/schoolsWP/02_SEO
PROMPT = "1Z6LcLQqYhnT7f0IpYI2YHROJChHKtD6u"           # 02_PROJETS/schoolsWP/04_Prompt
AUTOMATISATION = "1U3ULsojI5imFfepgwcQ4fCEqVoKABpKj"    # 02_PROJETS/schoolsWP/03_Automatisation
AFFILIATION = "1BxKjv4i3lexjMHtXGvvMh00sHq70tyzT"       # 06_Monetisation/01_Affiliation
MONETISATION = "1bc64Ug-T2_0Go376kEKQSgZqDYa9F7NZ"      # 06_Monetisation
CONTENUS = "1VqnC6jiPNFycoJF_Eixuh6p6sfU88wci"          # 05_Contenus
CONTENUS_EN_COURS = "1RDoMm-IIIpM8pcMQ9BUQO_giCRR22RqA" # 05_Contenus/01_En-cours
ASSETS = "1Er1ep9cG8mouzC9Qh-AKX2MO1obTFpVb"            # 01_Assets
SCHOOLSWP = "1D10mjPHE_PEab5ajRUq7spoY4gleTSEY"         # 02_PROJETS/schoolsWP
START_HERE = "12BeOpPH3YO2fbrTcLjoiVAs4L_rH0Qq-"        # 00_START-HERE
ADMIN = "1CVEHeKlVJl4EzJtwKKVbbeO5Es-gWAnU"             # 01_ADMIN

FOLDER_LABELS = {
    SEO: "02_SEO",
    PROMPT: "04_Prompt",
    AUTOMATISATION: "03_Automatisation",
    AFFILIATION: "06_Monetisation/01_Affiliation",
    MONETISATION: "06_Monetisation",
    CONTENUS: "05_Contenus",
    CONTENUS_EN_COURS: "05_Contenus/01_En-cours",
    ASSETS: "01_Assets",
    SCHOOLSWP: "schoolsWP (racine)",
    START_HERE: "00_START-HERE",
    ADMIN: "01_ADMIN",
}


def classify(name):
    """Classe un fichier par son nom."""
    n = name.lower()

    # README et Nomenclature → 00_START-HERE
    if n.startswith("readme") or "nomenclature" in n:
        return START_HERE

    # Checklist ADMIN
    if "checklist - admin" in n:
        return ADMIN

    # Log-Creation-Structure ADMIN
    if "log-creation-structure" in n:
        return ADMIN

    # Suffixe - Template Email
    if "- template email" in n or "sequence email" in n:
        return MONETISATION

    # Suffixe - Affiliation
    if "- affiliation" in n:
        return AFFILIATION

    # Suffixe - SEO (explicite)
    if "- seo" in n:
        return SEO

    # Suffixe - Prompt
    if "- prompt" in n or n.startswith("prompt "):
        return PROMPT

    # Suffixe - Checklist
    if "- checklist" in n:
        return ASSETS

    # Suffixe - Template
    if "- template" in n:
        return ASSETS

    # Articles de blog (avis, test, guide complet, plugin review)
    article_kw = [
        "avis ", "avis-", "test complet", "guide complet",
        "le plugin", "la solution", "faut-il adopter",
        "fluentbooking", "fluentsmtp", "bit flows",
        "maintenance wordpress", "formation wordpress",
        "microthemer", "wp rocket", "droip", "affiliatepress",
        "linksgarden", "pulse avis", "suremembers", "sureforms",
        "suretriggers", "wpboutik",
    ]
    for kw in article_kw:
        if kw in n:
            return CONTENUS_EN_COURS

    # Lecons audit de contenu → SEO
    if "lecon" in n and "module" in n:
        return SEO
    if "audit de contenu" in n or "synthese de laudit" in n:
        return SEO

    # SEO keywords
    seo_kw = [
        "backlinks", "serp", "mots-cle", "seo quick wins",
        "strategie seo", "recherche de mots", "intention de recherche",
        "cold mailing",
    ]
    for kw in seo_kw:
        if kw in n:
            return SEO

    # Prompt keywords
    prompt_kw = [
        "prompt", "chatgpt", "gemini", "master brief",
        "modele de prompt", "gpt",
    ]
    for kw in prompt_kw:
        if kw in n:
            return PROMPT

    # Automatisation keywords
    auto_kw = [
        "autopilot", "thumbnail autopilot", "automatiser",
        "remotion", "personal-email-event",
    ]
    for kw in auto_kw:
        if kw in n:
            return AUTOMATISATION

    # Affiliation keywords
    affi_kw = ["affiliation", "affiliatepress"]
    for kw in affi_kw:
        if kw in n:
            return AFFILIATION

    # Monetisation
    if "monetisation" in n or "vendre des sites" in n:
        return MONETISATION

    # Contenu / articles
    contenu_kw = [
        "contenu", "du contenu", "linkedin", "publication",
        "formation", "workbook",
    ]
    for kw in contenu_kw:
        if kw in n:
            return CONTENUS

    # Strategie, etude marche
    if "strategie" in n or "etude marche" in n or "plan de formation" in n:
        return SCHOOLSWP

    # Fallback
    return SCHOOLSWP


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


def main():
    apply_mode = "--apply" in sys.argv

    mode = "APPLICATION" if apply_mode else "PREVIEW"
    print("=" * 60)
    print(f"  DISPATCH GOOGLE DOCS -- MODE {mode}")
    print("=" * 60)

    print("\n[1/3] Authentification...")
    service = authenticate()
    print("  OK")

    print("\n[2/3] Scan du dossier _TRI_Google-Docs...")
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
    for f in all_files:
        target = classify(f["name"])
        classified.append((f, target))

    # Afficher par destination
    by_dest = {}
    for f, target in classified:
        by_dest.setdefault(target, []).append(f)

    for target in sorted(by_dest.keys(), key=lambda t: FOLDER_LABELS.get(t, t)):
        files = by_dest[target]
        label = FOLDER_LABELS.get(target, target)
        print(f"  -> {label} ({len(files)} fichiers)")
        for f in files:
            safe_name = f["name"].encode("ascii", errors="replace").decode()[:80]
            print(f"     - {safe_name}")
        print()

    if not apply_mode:
        print("=" * 60)
        print("  MODE PREVIEW -- aucune modification")
        print("  Pour appliquer : ajouter --apply")
        print("=" * 60)
        return

    total = len(classified)
    print(f"  {total} fichiers seront deplaces.")
    confirm = input("  Confirmer ? (taper 'OUI') : ")
    if confirm != "OUI":
        print("  Annule.")
        return

    print(f"\n[3/3] Deplacement de {total} fichiers...")
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
            print(f"  ERREUR : {f['name'][:60]} -- {e}")
        log.append(entry)

    os.makedirs(OUTPUT_DIR, exist_ok=True)
    ts = datetime.now().strftime("%Y%m%d_%H%M%S")
    log_path = os.path.join(OUTPUT_DIR, f"dispatch_docs_{ts}.json")
    with open(log_path, "w", encoding="utf-8") as fp:
        json.dump(
            {
                "applied_at": datetime.now().isoformat(),
                "total": total,
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
    print(f"  TERMINE -- {success} deplaces, {errors} erreurs")
    print("=" * 60)


if __name__ == "__main__":
    main()
