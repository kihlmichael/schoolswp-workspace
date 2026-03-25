#!/usr/bin/env python3
"""
Google Drive Progressive Renaming -- schoolsWP
================================================
Detecte les problemes de nommage et propose des corrections.
Travaille dossier par dossier pour un controle progressif.

Conventions appliquees :
  Dossiers : XX_Nom-Du-Dossier (kebab-case, pas d'accents, pas d'espaces)
  Fichiers : corrections legeres (accents, emojis, speciaux, tirets longs) -- espaces conserves

Securite :
  - Dry-run par defaut (--apply pour executer)
  - Genere rename_mapping.csv pour review avant application
  - Journalise tout
  - Peut cibler un dossier specifique (--folder-id)

Usage :
  python gdrive-rename.py                        # Scan complet, dry-run
  python gdrive-rename.py --folder-id XXX        # Scan un dossier
  python gdrive-rename.py --severity high        # Uniquement les problemes graves
  python gdrive-rename.py --apply                # Appliquer les renommages
  python gdrive-rename.py --apply --limit 20     # Appliquer par lots de 20
"""

import argparse
import csv
import json
import os
import re
import sys
import unicodedata
from datetime import datetime

# Fix Windows console encoding (cp1252 ne supporte pas tous les caracteres)
if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

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


# ---------------------------------------------------------------------------
# Config
# ---------------------------------------------------------------------------
SCOPES = ["https://www.googleapis.com/auth/drive"]
TOKEN_FILE = "token-gdrive-migration.json"
CREDENTIALS_FILE = "credentials-gdrive-audit.json"
OUTPUT_DIR = "output/gdrive-rename"
PAGE_SIZE = 1000

# Extensions Google Docs (pas d'extension visible)
GOOGLE_MIME_TYPES = {
    "application/vnd.google-apps.document",
    "application/vnd.google-apps.spreadsheet",
    "application/vnd.google-apps.presentation",
    "application/vnd.google-apps.form",
    "application/vnd.google-apps.drawing",
    "application/vnd.google-apps.script",
}


# ---------------------------------------------------------------------------
# Renaming rules
# ---------------------------------------------------------------------------
def remove_accents(text):
    """Supprime les accents d'une chaine."""
    nfkd = unicodedata.normalize("NFKD", text)
    return "".join(c for c in nfkd if not unicodedata.combining(c))


def remove_emojis(text):
    """Supprime les emojis."""
    emoji_pattern = re.compile(
        r"[\U0001f300-\U0001f9ff\U0001fa00-\U0001fa6f\U0001fa70-\U0001faff"
        r"\u2600-\u26ff\u2700-\u27bf\u200d\ufe0f]"
    )
    return emoji_pattern.sub("", text).strip()


def fix_separators(text):
    """Normalise les separateurs : tiret entre mots, underscore entre segments."""
    # Remplacer les tirets longs par des tirets courts
    text = text.replace("\u2013", "-").replace("\u2014", "-").replace("\u2012", "-")
    # Remplacer les underscores multiples
    text = re.sub(r"_+", "_", text)
    # Remplacer les tirets multiples
    text = re.sub(r"-+", "-", text)
    # Supprimer espaces en debut/fin
    text = text.strip()
    # Remplacer doubles espaces
    text = re.sub(r"\s+", " ", text)
    return text


def fix_special_chars(text):
    """Supprime les caracteres speciaux problematiques."""
    # Garder : lettres, chiffres, tirets, underscores, points, espaces, parentheses
    text = re.sub(r'[#%&{}\\<>*?/$!\'"`:@+|=\[\]]', "", text)
    return text.strip()


def fix_version_chaos(text):
    """Remplace les patterns de version chaos par v01 standard."""
    # "final" / "FINAL" / "Final" -> _FINAL
    text = re.sub(
        r"[\s_-]*(?:final|FINAL|Final|def|DEF|Def|last|LAST|Last)[\s_-]*$",
        "_FINAL",
        text,
    )
    # "copie de " / "Copy of " au debut
    text = re.sub(r"^(?:Copie de |Copy of |copie de )", "", text, flags=re.IGNORECASE)
    # "v3_last" -> "v03"
    text = re.sub(r"_?v?(\d+)_?(?:last|final|def)$", r"_v\1_FINAL", text, flags=re.IGNORECASE)
    return text


def fix_date_format(text):
    """Convertit les dates non standard en YYYY-MM-DD."""
    # "January 21, 2026" -> "2026-01-21"
    months = {
        "january": "01", "february": "02", "march": "03", "april": "04",
        "may": "05", "june": "06", "july": "07", "august": "08",
        "september": "09", "october": "10", "november": "11", "december": "12",
        "jan": "01", "feb": "02", "mar": "03", "apr": "04",
        "jun": "06", "jul": "07", "aug": "08", "sep": "09",
        "oct": "10", "nov": "11", "dec": "12",
        "janvier": "01", "fevrier": "02", "fevr": "02", "mars": "03",
        "avril": "04", "mai": "05", "juin": "06", "juillet": "07",
        "aout": "08", "septembre": "09", "octobre": "10",
        "novembre": "11", "decembre": "12",
    }
    # English: "Month DD, YYYY"
    pattern_en = re.compile(
        r"(\w+)\s+(\d{1,2}),?\s+(\d{4})", re.IGNORECASE
    )
    match = pattern_en.search(text)
    if match:
        month_name = match.group(1).lower().rstrip(".")
        if month_name in months:
            day = match.group(2).zfill(2)
            year = match.group(3)
            iso_date = f"{year}-{months[month_name]}-{day}"
            text = text[: match.start()] + iso_date + text[match.end() :]

    # French: "DD month YYYY" (e.g. "05 fevr. 2026")
    pattern_fr = re.compile(
        r"(\d{1,2})\s+(\w+\.?)\s+(\d{4})", re.IGNORECASE
    )
    match = pattern_fr.search(text)
    if match:
        month_name = match.group(2).lower().rstrip(".")
        if month_name in months:
            day = match.group(1).zfill(2)
            year = match.group(3)
            iso_date = f"{year}-{months[month_name]}-{day}"
            text = text[: match.start()] + iso_date + text[match.end() :]

    # DD/MM/YYYY or DD-MM-YYYY -> YYYY-MM-DD
    pattern_dmy = re.compile(r"\b(\d{2})[/.-](\d{2})[/.-](\d{4})\b")
    match = pattern_dmy.search(text)
    if match:
        day, month, year = match.group(1), match.group(2), match.group(3)
        if 1 <= int(month) <= 12 and 1 <= int(day) <= 31:
            iso_date = f"{year}-{month}-{day}"
            text = text[: match.start()] + iso_date + text[match.end() :]

    return text


def compute_new_name(name, mime_type):
    """Calcule un nouveau nom corrige selon les conventions."""
    is_folder = mime_type == "application/vnd.google-apps.folder"
    is_google_doc = mime_type in GOOGLE_MIME_TYPES
    original = name

    # Separer nom et extension pour les fichiers
    if not is_folder and not is_google_doc and "." in name:
        base, ext = name.rsplit(".", 1)
    else:
        base = name
        ext = None

    # 1. Supprimer emojis
    base = remove_emojis(base)

    # 2. Supprimer le suffixe Google Docs "- Ressource" (fichiers seulement)
    if not is_folder:
        base = re.sub(r"\s*[-\u2013\u2014]\s*Ressource\s*$", "", base)

    # 3. Corriger les dates
    base = fix_date_format(base)

    # 4. Corriger le chaos de version
    base = fix_version_chaos(base)

    # 5. Supprimer les caracteres speciaux
    base = fix_special_chars(base)

    # 6. Supprimer les accents
    base = remove_accents(base)

    # 7. Normaliser les separateurs (strategie differente dossiers/fichiers)
    if is_folder:
        # Dossiers : full kebab-case, pas d'espaces
        base = fix_separators(base)
        base = base.replace(" ", "-")
    else:
        # Fichiers : garder les espaces, corriger tirets longs et doubles espaces
        base = base.replace("\u2013", "-").replace("\u2014", "-").replace("\u2012", "-")
        base = re.sub(r"\s+", " ", base)
        base = base.strip()

    # 8. Supprimer tirets/underscores en debut/fin
    base = base.strip("-_")

    # 9. Supprimer doubles tirets/underscores
    base = re.sub(r"-+", "-", base)
    base = re.sub(r"_+", "_", base)

    # Reconstruire le nom
    if ext:
        new_name = f"{base}.{ext}"
    else:
        new_name = base

    # Ne retourner que si le nom a change
    if new_name != original and new_name.strip():
        return new_name
    return None


def detect_issues(name, mime_type):
    """Detecte les problemes de nommage et retourne la liste + severite max."""
    issues = []
    is_folder = mime_type == "application/vnd.google-apps.folder"

    emoji_pattern = re.compile(
        r"[\U0001f300-\U0001f9ff\U0001fa00-\U0001fa6f\U0001fa70-\U0001faff"
        r"\u2600-\u26ff\u2700-\u27bf\u200d\ufe0f]"
    )
    accent_pattern = re.compile(r"[àâäéèêëïîôùûüÿçœæÀÂÄÉÈÊËÏÎÔÙÛÜŸÇŒÆ]")
    special_pattern = re.compile(r'[#%&{}\\<>*?/$!\'"`:@+|=\[\]]')
    version_pattern = re.compile(
        r"(?:final|FINAL|def|DEF|last|LAST|copie|copy)", re.IGNORECASE
    )
    space_pattern = re.compile(r"\s")

    if emoji_pattern.search(name):
        issues.append(("emojis", "medium"))
    if accent_pattern.search(name):
        issues.append(("accents", "medium"))
    if special_pattern.search(name):
        issues.append(("special_chars", "high"))
    if version_pattern.search(name):
        issues.append(("version_chaos", "high"))
    if re.search(r"  +", name):
        issues.append(("double_spaces", "low"))
    if name != name.strip():
        issues.append(("leading_trailing_spaces", "high"))
    if is_folder and space_pattern.search(name):
        issues.append(("spaces", "low"))

    # Long dash
    if "\u2013" in name or "\u2014" in name or "\u2012" in name:
        issues.append(("long_dash", "low"))

    # Google Docs suffix "- Ressource" (fichiers seulement)
    if not is_folder and re.search(r"\s*[-\u2013\u2014]\s*Ressource\s*$", name):
        issues.append(("google_suffix", "medium"))

    severity_order = {"high": 3, "medium": 2, "low": 1}
    max_severity = "low"
    for _, sev in issues:
        if severity_order.get(sev, 0) > severity_order.get(max_severity, 0):
            max_severity = sev

    return issues, max_severity


# ---------------------------------------------------------------------------
# Auth
# ---------------------------------------------------------------------------
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


# ---------------------------------------------------------------------------
# Scan
# ---------------------------------------------------------------------------
def scan_folder(service, folder_id="root", max_depth=None, _depth=0, _path=""):
    """Scan recursif d'un dossier."""
    items = []
    page_token = None

    while True:
        results = (
            service.files()
            .list(
                q=f"'{folder_id}' in parents and trashed = false",
                pageSize=PAGE_SIZE,
                fields="nextPageToken, files(id, name, mimeType, parents)",
                pageToken=page_token,
            )
            .execute()
        )

        for item in results.get("files", []):
            item_path = f"{_path}/{item['name']}" if _path else item["name"]
            item["_path"] = item_path
            item["_depth"] = _depth
            items.append(item)

            if (
                item["mimeType"] == "application/vnd.google-apps.folder"
                and (max_depth is None or _depth < max_depth)
            ):
                children = scan_folder(
                    service, item["id"], max_depth, _depth + 1, item_path
                )
                items.extend(children)

        page_token = results.get("nextPageToken")
        if not page_token:
            break

    if _depth == 0 and len(items) % 500 == 0 and len(items) > 0:
        print(f"  ... {len(items)} elements scannes")

    return items


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------
def main():
    parser = argparse.ArgumentParser(
        description="Renommage progressif Google Drive"
    )
    parser.add_argument(
        "--apply", action="store_true",
        help="Appliquer les renommages (sinon preview)",
    )
    parser.add_argument(
        "--folder-id", default="root",
        help="ID du dossier a scanner (defaut: root)",
    )
    parser.add_argument(
        "--max-depth", type=int, default=None,
        help="Profondeur max de scan",
    )
    parser.add_argument(
        "--severity", default="all",
        choices=["all", "high", "medium", "low"],
        help="Filtrer par severite minimum (defaut: all)",
    )
    parser.add_argument(
        "--limit", type=int, default=None,
        help="Limiter le nombre de renommages",
    )
    parser.add_argument(
        "--output-dir", default=OUTPUT_DIR,
        help=f"Dossier de sortie (defaut: {OUTPUT_DIR})",
    )
    args = parser.parse_args()

    severity_filter = {"all": 0, "low": 1, "medium": 2, "high": 3}
    severity_order = {"low": 1, "medium": 2, "high": 3}
    min_severity = severity_filter[args.severity]

    print("=" * 60)
    if args.apply:
        print("  RENOMMAGE PROGRESSIF -- MODE APPLICATION")
    else:
        print("  RENOMMAGE PROGRESSIF -- MODE PREVIEW")
    print("=" * 60)

    # Auth
    print("\n[1/4] Authentification...")
    service = authenticate()
    print("  OK")

    # Scan
    print(f"\n[2/4] Scan (folder: {args.folder_id})...")
    items = scan_folder(service, args.folder_id, args.max_depth)
    print(f"  OK -- {len(items)} elements scannes")

    # Analyse
    print("\n[3/4] Analyse des noms...")
    rename_proposals = []

    for item in items:
        name = item["name"]
        mime = item["mimeType"]

        issues, max_sev = detect_issues(name, mime)
        if not issues:
            continue

        if severity_order.get(max_sev, 0) < min_severity:
            continue

        new_name = compute_new_name(name, mime)
        if new_name is None:
            continue

        rename_proposals.append({
            "id": item["id"],
            "current_name": name,
            "new_name": new_name,
            "path": item["_path"],
            "mime_type": mime,
            "issues": ", ".join(i[0] for i in issues),
            "severity": max_sev,
        })

    # Trier par severite (high d'abord)
    rename_proposals.sort(
        key=lambda x: -severity_order.get(x["severity"], 0)
    )

    if args.limit:
        rename_proposals = rename_proposals[: args.limit]

    print(f"  {len(rename_proposals)} renommages proposes")

    if not rename_proposals:
        print("\n  Aucun renommage necessaire.")
        return

    # Stats
    by_severity = {}
    by_issue = {}
    for p in rename_proposals:
        sev = p["severity"]
        by_severity[sev] = by_severity.get(sev, 0) + 1
        for issue in p["issues"].split(", "):
            by_issue[issue] = by_issue.get(issue, 0) + 1

    print(f"\n  Par severite :")
    for sev in ["high", "medium", "low"]:
        if sev in by_severity:
            print(f"    {sev:10s} : {by_severity[sev]}")

    print(f"\n  Par type de probleme :")
    for issue, count in sorted(by_issue.items(), key=lambda x: -x[1]):
        print(f"    {issue:25s} : {count}")

    # Exemples
    print(f"\n  Exemples de renommages (10 premiers) :")
    for p in rename_proposals[:10]:
        print(f"    [{p['severity']:6s}] {p['current_name']}")
        print(f"         -> {p['new_name']}")

    # Export mapping
    os.makedirs(args.output_dir, exist_ok=True)
    mapping_path = os.path.join(args.output_dir, "rename_mapping.csv")
    fieldnames = [
        "id", "current_name", "new_name", "path",
        "severity", "issues", "mime_type",
    ]
    with open(mapping_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rename_proposals)
    print(f"\n  Mapping exporte : {mapping_path}")

    if not args.apply:
        print(f"\n  Total : {len(rename_proposals)} renommages")
        print("  Verifie rename_mapping.csv puis relance avec --apply")
        return

    # Application
    print(f"\n[4/4] Application de {len(rename_proposals)} renommages...")
    confirm = input("  Confirmer ? (taper 'OUI') : ")
    if confirm != "OUI":
        print("  Annule.")
        return

    log = []
    success = 0
    errors = 0

    for i, p in enumerate(rename_proposals):
        entry = {
            "id": p["id"],
            "old_name": p["current_name"],
            "new_name": p["new_name"],
            "result": "",
        }
        try:
            service.files().update(
                fileId=p["id"],
                body={"name": p["new_name"]},
                fields="id, name",
            ).execute()
            entry["result"] = "RENAMED"
            success += 1
            if (i + 1) % 50 == 0:
                print(f"  ... {i + 1}/{len(rename_proposals)}")
        except HttpError as e:
            entry["result"] = f"ERROR: {e}"
            errors += 1
            print(f"  [ERREUR] {p['current_name']} -- {e}")
        log.append(entry)

    # Log
    ts = datetime.now().strftime("%Y%m%d_%H%M%S")
    log_path = os.path.join(args.output_dir, f"rename_log_{ts}.json")
    with open(log_path, "w", encoding="utf-8") as f:
        json.dump({
            "applied_at": datetime.now().isoformat(),
            "success": success,
            "errors": errors,
            "operations": log,
        }, f, ensure_ascii=False, indent=2)

    print(f"\n  Succes  : {success}")
    print(f"  Erreurs : {errors}")
    print(f"  Log     : {log_path}")


if __name__ == "__main__":
    main()
