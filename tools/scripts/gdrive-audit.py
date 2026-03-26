#!/usr/bin/env python3
"""
Google Drive Audit Script — schoolsWP
======================================
Audit en lecture seule du Google Drive personnel.
Ne modifie, deplace ou supprime RIEN.

Scope minimal : drive.metadata.readonly

Sorties generees dans le dossier output/ :
  - inventory.csv         (inventaire complet)
  - naming_issues.csv     (problemes de nommage detectes)
  - duplicates_suspects.csv (doublons potentiels)
  - depth_report.csv      (analyse de profondeur)
  - audit_summary.json    (resume global)

Usage :
  python gdrive-audit.py                  # audit complet My Drive
  python gdrive-audit.py --folder-id XXX  # audit un sous-dossier specifique
  python gdrive-audit.py --max-depth 5    # limiter la profondeur
"""

import argparse
import csv
import hashlib
import json
import os
import re
import sys
from collections import Counter, defaultdict
from datetime import datetime
from pathlib import Path

try:
    from google.auth.transport.requests import Request
    from google.oauth2.credentials import Credentials
    from google_auth_oauthlib.flow import InstalledAppFlow
    from googleapiclient.discovery import build
except ImportError:
    print("Dependances manquantes. Installe-les avec :")
    print("  pip install -r requirements-gdrive-audit.txt")
    sys.exit(1)


# ---------------------------------------------------------------------------
# Config
# ---------------------------------------------------------------------------
SCOPES = ["https://www.googleapis.com/auth/drive.metadata.readonly"]
TOKEN_FILE = "token-gdrive-audit.json"
CREDENTIALS_FILE = "credentials-gdrive-audit.json"
OUTPUT_DIR = "output/gdrive-audit"
PAGE_SIZE = 1000

# Categories de types MIME
MIME_CATEGORIES = {
    "document": [
        "application/vnd.google-apps.document",
        "application/msword",
        "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
    ],
    "spreadsheet": [
        "application/vnd.google-apps.spreadsheet",
        "application/vnd.ms-excel",
        "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
    ],
    "presentation": [
        "application/vnd.google-apps.presentation",
        "application/vnd.ms-powerpoint",
        "application/vnd.openxmlformats-officedocument.presentationml.presentation",
    ],
    "image": ["image/"],
    "video": ["video/"],
    "audio": ["audio/"],
    "pdf": ["application/pdf"],
    "archive": ["application/zip", "application/x-rar", "application/x-7z"],
    "code": [
        "text/x-python",
        "application/javascript",
        "application/json",
        "text/html",
        "text/css",
        "text/plain",
    ],
    "folder": ["application/vnd.google-apps.folder"],
}

# Patterns problematiques pour l'audit de nommage
NAMING_RULES = {
    "accents": re.compile(r"[àâäéèêëïîôùûüÿçœæÀÂÄÉÈÊËÏÎÔÙÛÜŸÇŒÆ]"),
    "special_chars": re.compile(r"[#%&{}\\<>*?/$!'\":@+`|=]"),
    "emojis": re.compile(
        r"[\U0001f300-\U0001f9ff\U0001fa00-\U0001fa6f\U0001fa70-\U0001faff"
        r"\u2600-\u26ff\u2700-\u27bf]"
    ),
    "mixed_separators": re.compile(r"(?=.*[ ])(?=.*[-_])"),
    "double_spaces": re.compile(r"  +"),
    "leading_trailing_spaces": re.compile(r"^\s+|\s+$"),
    "version_chaos": re.compile(
        r"(?:final|FINAL|Final|def|DEF|last|LAST|copie|copy|Copy)"
        r"(?:_|\s|-)*(?:\d*|v?\d+)?",
        re.IGNORECASE,
    ),
    "date_inconsistent_ymd": re.compile(r"\b\d{4}[-/.]\d{2}[-/.]\d{2}\b"),
    "date_inconsistent_dmy": re.compile(r"\b\d{2}[-/.]\d{2}[-/.]\d{4}\b"),
    "date_inconsistent_mdy": re.compile(r"\b\d{2}[-/.]\d{2}[-/.]\d{2}\b"),
    "ambiguous_names": re.compile(
        r"^(?:Divers|Nouveau dossier|Sans titre|Untitled|À trier|A trier"
        r"|Test|test|Temp|tmp|Brouillon|Draft|Copie de|Copy of|Nouveau"
        r"|New folder|backup|old|ancien|archive\d*)$",
        re.IGNORECASE,
    ),
    "numbering_no_padding": re.compile(r"(?<!\d)\b[1-9]\b(?!\d)"),
}


# ---------------------------------------------------------------------------
# Auth
# ---------------------------------------------------------------------------
def authenticate():
    """Authentification OAuth2 avec scope minimal (metadata.readonly)."""
    creds = None

    if os.path.exists(TOKEN_FILE):
        creds = Credentials.from_authorized_user_file(TOKEN_FILE, SCOPES)

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            if not os.path.exists(CREDENTIALS_FILE):
                print(f"ERREUR : fichier '{CREDENTIALS_FILE}' introuvable.")
                print("Suis le guide de setup pour le creer.")
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
# Collecte recursive
# ---------------------------------------------------------------------------
def list_all_files(service, folder_id="root", max_depth=None):
    """Liste recursive de tous les fichiers/dossiers depuis folder_id."""
    all_items = []
    queue = [(folder_id, "", 0)]  # (id, path, depth)

    while queue:
        current_id, current_path, depth = queue.pop(0)

        if max_depth is not None and depth > max_depth:
            continue

        page_token = None
        while True:
            query = f"'{current_id}' in parents and trashed = false"
            results = (
                service.files()
                .list(
                    q=query,
                    pageSize=PAGE_SIZE,
                    fields=(
                        "nextPageToken, files(id, name, mimeType, size,"
                        " modifiedTime, createdTime, owners, parents,"
                        " shared, webViewLink)"
                    ),
                    pageToken=page_token,
                    supportsAllDrives=False,
                )
                .execute()
            )

            items = results.get("files", [])
            for item in items:
                item_path = f"{current_path}/{item['name']}" if current_path else item["name"]
                item["_path"] = item_path
                item["_depth"] = depth
                item["_parent_path"] = current_path
                all_items.append(item)

                if item["mimeType"] == "application/vnd.google-apps.folder":
                    queue.append((item["id"], item_path, depth + 1))

            page_token = results.get("nextPageToken")
            if not page_token:
                break

        # Progress
        file_count = len(all_items)
        if file_count % 500 == 0 and file_count > 0:
            print(f"  ... {file_count} elements trouves")

    return all_items


# ---------------------------------------------------------------------------
# Classification MIME
# ---------------------------------------------------------------------------
def categorize_mime(mime_type):
    """Classe un type MIME dans une categorie lisible."""
    for category, patterns in MIME_CATEGORIES.items():
        for pattern in patterns:
            if mime_type == pattern or mime_type.startswith(pattern):
                return category
    return "other"


# ---------------------------------------------------------------------------
# Audit de nommage
# ---------------------------------------------------------------------------
def audit_naming(items):
    """Detecte les problemes de nommage sur chaque element."""
    issues = []

    for item in items:
        name = item["name"]
        item_issues = []

        # Accents
        if NAMING_RULES["accents"].search(name):
            item_issues.append(("accents", "medium", "Contient des accents"))

        # Caracteres speciaux
        if NAMING_RULES["special_chars"].search(name):
            item_issues.append(
                ("special_chars", "high", "Contient des caracteres speciaux problematiques")
            )

        # Emojis
        if NAMING_RULES["emojis"].search(name):
            item_issues.append(("emojis", "medium", "Contient des emojis"))

        # Separateurs mixtes
        if NAMING_RULES["mixed_separators"].search(name):
            item_issues.append(
                ("mixed_separators", "medium", "Melange espaces, tirets et underscores")
            )

        # Double espaces
        if NAMING_RULES["double_spaces"].search(name):
            item_issues.append(("double_spaces", "low", "Contient des espaces doubles"))

        # Espaces en debut/fin
        if NAMING_RULES["leading_trailing_spaces"].search(name):
            item_issues.append(
                ("leading_trailing_spaces", "high", "Espaces en debut ou fin de nom")
            )

        # Chaos de versioning
        if NAMING_RULES["version_chaos"].search(name):
            item_issues.append(
                ("version_chaos", "high", "Version non standard (final, copie, def...)")
            )

        # Dates multiples formats
        has_ymd = NAMING_RULES["date_inconsistent_ymd"].search(name)
        has_dmy = NAMING_RULES["date_inconsistent_dmy"].search(name)
        has_short = NAMING_RULES["date_inconsistent_mdy"].search(name)
        date_formats = sum(bool(x) for x in [has_ymd, has_dmy, has_short])
        if has_dmy or has_short:
            item_issues.append(
                ("date_format", "medium", "Format de date non standard (preferer YYYY-MM-DD)")
            )

        # Noms ambigus
        if NAMING_RULES["ambiguous_names"].search(name):
            item_issues.append(
                ("ambiguous_name", "high", "Nom generique/ambigu")
            )

        # Casing : detecter TOUT MAJUSCULES (hors acronymes courts)
        name_no_ext = Path(name).stem
        if len(name_no_ext) > 4 and name_no_ext == name_no_ext.upper():
            item_issues.append(
                ("all_caps", "low", "Nom entierement en majuscules")
            )

        # Profondeur excessive (>5)
        if item["_depth"] > 5:
            item_issues.append(
                ("deep_nesting", "medium", f"Profondeur {item['_depth']} (>5)")
            )

        for issue_type, severity, description in item_issues:
            issues.append({
                "id": item["id"],
                "name": name,
                "path": item["_path"],
                "mime_type": item["mimeType"],
                "issue_type": issue_type,
                "severity": severity,
                "description": description,
            })

    return issues


# ---------------------------------------------------------------------------
# Detection doublons
# ---------------------------------------------------------------------------
def detect_duplicates(items):
    """Detecte les doublons potentiels (meme nom + meme taille)."""
    # Grouper par nom normalise + taille
    groups = defaultdict(list)

    for item in items:
        if item["mimeType"] == "application/vnd.google-apps.folder":
            continue
        name_normalized = item["name"].strip().lower()
        size = item.get("size", "0")
        key = f"{name_normalized}|{size}"
        groups[key].append(item)

    duplicates = []
    for key, group_items in groups.items():
        if len(group_items) > 1:
            for item in group_items:
                duplicates.append({
                    "id": item["id"],
                    "name": item["name"],
                    "path": item["_path"],
                    "size": item.get("size", "N/A"),
                    "modified": item.get("modifiedTime", "N/A"),
                    "duplicate_group": hashlib.md5(key.encode()).hexdigest()[:8],
                    "group_count": len(group_items),
                })

    return duplicates


# ---------------------------------------------------------------------------
# Analyse de profondeur
# ---------------------------------------------------------------------------
def analyze_depth(items):
    """Analyse la profondeur de l'arborescence."""
    folders = [i for i in items if i["mimeType"] == "application/vnd.google-apps.folder"]
    depth_counts = Counter(i["_depth"] for i in items)
    folder_children = Counter()

    for item in items:
        folder_children[item.get("_parent_path", "")] += 1

    depth_report = []
    for folder in folders:
        child_count = folder_children.get(folder["_path"], 0)
        depth_report.append({
            "id": folder["id"],
            "name": folder["name"],
            "path": folder["_path"],
            "depth": folder["_depth"],
            "direct_children": child_count,
            "flag": (
                "TOO_DEEP" if folder["_depth"] > 5
                else "TOO_WIDE" if child_count > 50
                else "OK"
            ),
        })

    return depth_report, depth_counts


# ---------------------------------------------------------------------------
# Generation du resume
# ---------------------------------------------------------------------------
def generate_summary(items, naming_issues, duplicates, depth_report, depth_counts):
    """Genere un resume JSON de l'audit."""
    folders = [i for i in items if i["mimeType"] == "application/vnd.google-apps.folder"]
    files = [i for i in items if i["mimeType"] != "application/vnd.google-apps.folder"]

    # Tailles par categorie
    size_by_category = defaultdict(int)
    count_by_category = defaultdict(int)
    for item in files:
        cat = categorize_mime(item["mimeType"])
        size_by_category[cat] += int(item.get("size", 0))
        count_by_category[cat] += 1

    # Top dossiers lourds (par nombre d'enfants)
    folder_sizes = defaultdict(int)
    for item in files:
        parent = item.get("_parent_path", "root")
        folder_sizes[parent] += int(item.get("size", 0))

    top_folders = sorted(folder_sizes.items(), key=lambda x: x[1], reverse=True)[:20]

    # Issues par type et severite
    issues_by_type = Counter(i["issue_type"] for i in naming_issues)
    issues_by_severity = Counter(i["severity"] for i in naming_issues)

    # Profondeur
    max_depth = max((i["_depth"] for i in items), default=0)
    avg_depth = sum(i["_depth"] for i in items) / len(items) if items else 0

    summary = {
        "audit_date": datetime.now().isoformat(),
        "totals": {
            "total_items": len(items),
            "total_folders": len(folders),
            "total_files": len(files),
            "total_size_bytes": sum(int(i.get("size", 0)) for i in files),
            "total_size_human": format_size(
                sum(int(i.get("size", 0)) for i in files)
            ),
        },
        "by_category": {
            cat: {
                "count": count_by_category[cat],
                "size_bytes": size_by_category[cat],
                "size_human": format_size(size_by_category[cat]),
            }
            for cat in sorted(count_by_category.keys())
        },
        "depth": {
            "max_depth": max_depth,
            "avg_depth": round(avg_depth, 1),
            "depth_distribution": dict(sorted(depth_counts.items())),
        },
        "naming_issues": {
            "total_issues": len(naming_issues),
            "by_type": dict(issues_by_type.most_common()),
            "by_severity": dict(issues_by_severity),
        },
        "duplicates": {
            "total_suspect_files": len(duplicates),
            "unique_groups": len(
                set(d["duplicate_group"] for d in duplicates)
            ),
        },
        "top_heavy_folders": [
            {"path": path, "size_human": format_size(size)}
            for path, size in top_folders
        ],
        "root_folders": sorted(
            [f["name"] for f in folders if f["_depth"] == 0]
        ),
        "flags": {
            "too_deep_folders": sum(
                1 for d in depth_report if d["flag"] == "TOO_DEEP"
            ),
            "too_wide_folders": sum(
                1 for d in depth_report if d["flag"] == "TOO_WIDE"
            ),
        },
    }
    return summary


def format_size(size_bytes):
    """Formate une taille en bytes vers une chaine lisible."""
    size_bytes = int(size_bytes)
    for unit in ["o", "Ko", "Mo", "Go", "To"]:
        if abs(size_bytes) < 1024:
            return f"{size_bytes:.1f} {unit}"
        size_bytes /= 1024
    return f"{size_bytes:.1f} Po"


# ---------------------------------------------------------------------------
# Export CSV
# ---------------------------------------------------------------------------
def write_csv(filepath, rows, fieldnames):
    """Ecrit une liste de dicts en CSV."""
    with open(filepath, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)
    print(f"  -> {filepath} ({len(rows)} lignes)")


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------
def main():
    parser = argparse.ArgumentParser(
        description="Audit Google Drive en lecture seule"
    )
    parser.add_argument(
        "--folder-id",
        default="root",
        help="ID du dossier racine a auditer (defaut: root = My Drive)",
    )
    parser.add_argument(
        "--max-depth",
        type=int,
        default=None,
        help="Profondeur maximale d'exploration (defaut: illimitee)",
    )
    parser.add_argument(
        "--output-dir",
        default=OUTPUT_DIR,
        help=f"Dossier de sortie (defaut: {OUTPUT_DIR})",
    )
    args = parser.parse_args()

    print("=" * 60)
    print("  GOOGLE DRIVE AUDIT — schoolsWP")
    print("  Mode : LECTURE SEULE (aucune modification)")
    print(f"  Scope : {SCOPES[0]}")
    print("=" * 60)

    # Auth
    print("\n[1/5] Authentification...")
    service = authenticate()
    print("  OK — connecte a Google Drive")

    # Collecte
    print(f"\n[2/5] Inventaire recursif (depuis {args.folder_id})...")
    items = list_all_files(service, args.folder_id, args.max_depth)
    print(f"  OK — {len(items)} elements trouves")

    if not items:
        print("\nAucun element trouve. Verifie le folder-id ou les permissions.")
        sys.exit(0)

    # Audit nommage
    print("\n[3/5] Audit de nommage...")
    naming_issues = audit_naming(items)
    print(f"  OK — {len(naming_issues)} problemes detectes")

    # Doublons
    print("\n[4/5] Detection de doublons...")
    duplicates = detect_duplicates(items)
    print(f"  OK — {len(duplicates)} fichiers suspects")

    # Profondeur
    print("\n[5/5] Analyse de profondeur...")
    depth_report, depth_counts = analyze_depth(items)

    # Resume
    summary = generate_summary(
        items, naming_issues, duplicates, depth_report, depth_counts
    )

    # Export
    print(f"\nExport des resultats dans {args.output_dir}/")
    os.makedirs(args.output_dir, exist_ok=True)

    # inventory.csv
    inventory_fields = [
        "id", "name", "_path", "mimeType", "size", "modifiedTime",
        "createdTime", "_depth", "_parent_path", "shared",
    ]
    inventory_rows = []
    for item in items:
        row = {k: item.get(k, "") for k in inventory_fields}
        row["category"] = categorize_mime(item["mimeType"])
        row["owners"] = ", ".join(
            o.get("emailAddress", "?")
            for o in item.get("owners", [])
        )
        inventory_rows.append(row)

    write_csv(
        os.path.join(args.output_dir, "inventory.csv"),
        inventory_rows,
        inventory_fields + ["category", "owners"],
    )

    # naming_issues.csv
    if naming_issues:
        write_csv(
            os.path.join(args.output_dir, "naming_issues.csv"),
            naming_issues,
            ["id", "name", "path", "mime_type", "issue_type", "severity", "description"],
        )

    # duplicates_suspects.csv
    if duplicates:
        write_csv(
            os.path.join(args.output_dir, "duplicates_suspects.csv"),
            duplicates,
            ["id", "name", "path", "size", "modified", "duplicate_group", "group_count"],
        )

    # depth_report.csv
    if depth_report:
        write_csv(
            os.path.join(args.output_dir, "depth_report.csv"),
            depth_report,
            ["id", "name", "path", "depth", "direct_children", "flag"],
        )

    # audit_summary.json
    summary_path = os.path.join(args.output_dir, "audit_summary.json")
    with open(summary_path, "w", encoding="utf-8") as f:
        json.dump(summary, f, ensure_ascii=False, indent=2)
    print(f"  -> {summary_path}")

    # Affichage resume console
    print("\n" + "=" * 60)
    print("  RESUME DE L'AUDIT")
    print("=" * 60)
    t = summary["totals"]
    print(f"  Elements     : {t['total_items']} ({t['total_folders']} dossiers, {t['total_files']} fichiers)")
    print(f"  Taille       : {t['total_size_human']}")
    print(f"  Profondeur   : max {summary['depth']['max_depth']}, moy {summary['depth']['avg_depth']}")
    print(f"  Problemes    : {summary['naming_issues']['total_issues']} issues de nommage")
    print(f"  Doublons     : {summary['duplicates']['total_suspect_files']} suspects ({summary['duplicates']['unique_groups']} groupes)")
    print(f"  Dossiers racine : {', '.join(summary['root_folders'][:15])}")

    if summary["naming_issues"]["by_type"]:
        print("\n  Top problemes de nommage :")
        for issue_type, count in sorted(
            summary["naming_issues"]["by_type"].items(),
            key=lambda x: x[1],
            reverse=True,
        )[:10]:
            print(f"    - {issue_type}: {count}")

    print("\n" + "=" * 60)
    print(f"  Resultats complets dans : {args.output_dir}/")
    print("  Prochaine etape : analyser les CSV et valider la structure cible")
    print("=" * 60)


if __name__ == "__main__":
    main()
