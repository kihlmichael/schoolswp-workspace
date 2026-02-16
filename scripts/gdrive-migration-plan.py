#!/usr/bin/env python3
"""
Google Drive Migration Plan -- schoolsWP
========================================
Genere un plan de migration DRY-RUN a partir de l'inventaire d'audit.
Ne modifie RIEN sur le Drive. Travaille uniquement sur les CSV locaux.

Sorties generees :
  - migration_mapping.csv    (ancien chemin -> nouveau chemin + action)
  - target_tree.md           (arborescence cible)
  - migration_summary.json   (resume des actions planifiees)

Usage :
  python gdrive-migration-plan.py
  python gdrive-migration-plan.py --inventory path/to/inventory.csv
  python gdrive-migration-plan.py --output-dir path/to/output
"""

import argparse
import csv
import json
import os
import re
import unicodedata
from collections import Counter, defaultdict
from datetime import datetime


# ---------------------------------------------------------------------------
# Config
# ---------------------------------------------------------------------------
DEFAULT_INVENTORY = "output/gdrive-audit/inventory.csv"
DEFAULT_OUTPUT = "output/gdrive-migration"

# ---------------------------------------------------------------------------
# Architecture cible -- Regles de mapping
# ---------------------------------------------------------------------------

# Dossiers racine orphelins schoolsWP -> destination dans la structure cible
ORPHAN_MAPPING = {
    "blog": "01_Projets/schoolsWP/02_Contenu/01_Blog",
    "newsletter": "01_Projets/schoolsWP/02_Contenu/02_Newsletter",
    "linkedin": "01_Projets/schoolsWP/02_Contenu/04_Reseaux-Sociaux/LinkedIn",
    "facebook": "01_Projets/schoolsWP/02_Contenu/04_Reseaux-Sociaux/Facebook",
    "medias": "01_Projets/schoolsWP/04_Assets",
    "branding": "01_Projets/schoolsWP/04_Assets/01_Branding",
    "templates": "01_Projets/schoolsWP/08_IA-et-Prompts/02_Templates",
    "concurrence": "01_Projets/schoolsWP/09_Veille",
    "automatisation": "01_Projets/schoolsWP/07_Automatisation",
    "wordpress": "01_Projets/schoolsWP/06_Technique",
    "ia_llm_seo": "01_Projets/schoolsWP/08_IA-et-Prompts",
    "outils": "02_Ressources/Outils",
}

# Systeme A (MAJUSCULES) -> Cible
SYSTEM_A_MAPPING = {
    "00_START-HERE": "02_Ressources/Organisation",
    "01_ADMIN": "03_Admin",
    "02_PROJETS": "01_Projets",
    "03_RESSOURCES": "02_Ressources",
    "04_ASSETS": "01_Projets/schoolsWP/04_Assets",
    "05_CLIENTS": "99_Archives/Clients",
    "06_CONTENUS": "01_Projets/schoolsWP/02_Contenu",
    "07_personnel": "04_Personnel",
    "99_ARCHIVES": "99_Archives",
}

# Systeme B (minuscules) -> Mapping vers cible
# Ces dossiers contiennent du contenu reel a migrer
SYSTEM_B_MAPPING = {
    "00_boite_de_reception": "00_Inbox",
    "01_projets_actifs": "01_Projets",
    "02_ressources_transverses": "02_Ressources",
    "03_contenus": "01_Projets/schoolsWP/02_Contenu",
    "04_admin_legal": "03_Admin",
    "05_formations": "02_Ressources/Formations",
    "06_archive": "99_Archives",
}

# Dossiers speciaux racine
SPECIAL_MAPPING = {
    "MÉDICALE": "04_Personnel/Medical",
    "PROMPTS_schoolsWP": "01_Projets/schoolsWP/08_IA-et-Prompts",
    "_BACKUP_DRIVE_2026-02-09": "99_Archives/2026-02-09_Backup-Drive",
}

# Sous-dossiers de 03_RESSOURCES avec doublons vides a supprimer
RESSOURCES_EMPTY_DUPES = {
    "03_Prompts_IA",
    "04_Methodes_ et _Formations",
    "05_Outils_ et _Docs_Techniques",
}

# Fichiers volants racine (par nom) -> destination
ROOT_FILE_MAPPING = {
    "schoolsWP – Index Global": "01_Projets/schoolsWP",
    "schoolsWP – Mapping Migration": "99_Archives/2026-02-09_Backup-Drive",
    "schoolsWP – Full Drive Index": "99_Archives/2026-02-09_Backup-Drive",
    "schoolsWP – Full Drive Mapping": "99_Archives/2026-02-09_Backup-Drive",
    "schoolsWP – Archive Migration": "99_Archives/2026-02-09_Backup-Drive",
    "schoolsWP Drive Organizer": "99_Archives/2026-02-09_Backup-Drive",
    "_schoolsWP_audit_data.json": "99_Archives/2026-02-09_Backup-Drive",
    "schoolsWP-linkedin-reboot.md": "01_Projets/schoolsWP/02_Contenu/04_Reseaux-Sociaux/LinkedIn",
    "Guide ultime pour vendre des sites web": "01_Projets/schoolsWP/05_Marketing",
    "schoolsWP - YouTube Competitor Analysis": "01_Projets/schoolsWP/09_Veille",
    "Suivi Affiliés Plugins (RSS-Promos)": "01_Projets/schoolsWP/05_Marketing/01_Affiliation",
    "2026-01-20 – BuddyBoss – Affiliation – Fiches": "01_Projets/schoolsWP/05_Marketing/01_Affiliation",
    "https://schoolswp.com/-Performance-on-Search-2026-02-06": "01_Projets/schoolsWP/10_Analytics",
    "Adobe Scan 05 févr. 2026.pdf": "00_Inbox",
    "PROJET PSE LOGIFARE.pdf": "00_Inbox",
    "Avocat - January 21, 2026-esv2-90p-bg-10p.mp3": "04_Personnel",
}

# Mapping des sous-dossiers 06_CONTENUS vers la structure cible
CONTENUS_SUBFOLDER_MAPPING = {
    "01_Backlog": "01_Projets/schoolsWP/02_Contenu/01_Blog/01_Backlog",
    "02_En-cours": "01_Projets/schoolsWP/02_Contenu/01_Blog/02_En-cours",
    "03_A-optimiser": "01_Projets/schoolsWP/02_Contenu/01_Blog/03_A-optimiser",
    "04_Publies": "01_Projets/schoolsWP/02_Contenu/01_Blog/04_Publies",
    "05_Lead-magnets": "01_Projets/schoolsWP/02_Contenu/05_Lead-magnets",
    "06_Newsletters": "01_Projets/schoolsWP/02_Contenu/02_Newsletter",
    "07_Scripts-video-audio": "01_Projets/schoolsWP/02_Contenu/03_YouTube",
    "99_ARCHIVES": "01_Projets/schoolsWP/02_Contenu/99_Archive",
}

# Mapping des sous-dossiers 04_ASSETS vers la structure cible
ASSETS_SUBFOLDER_MAPPING = {
    "01_Logos-Branding": "01_Projets/schoolsWP/04_Assets/01_Branding",
    "02_Images": "01_Projets/schoolsWP/04_Assets/03_Illustrations",
    "03_Videos": "01_Projets/schoolsWP/04_Assets/06_Videos",
    "04_PDF-Documents": "01_Projets/schoolsWP/04_Assets/07_PDF",
    "05_Canva-Figma-PSD": "01_Projets/schoolsWP/04_Assets/05_Sources-Design",
    "99_ARCHIVES": "01_Projets/schoolsWP/04_Assets/99_Archive",
}


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------
def remove_accents(text):
    """Supprime les accents d'une chaine."""
    nfkd = unicodedata.normalize("NFKD", text)
    return "".join(c for c in nfkd if not unicodedata.combining(c))


def normalize_name(name):
    """Propose un nom normalise selon les conventions."""
    # Supprimer accents
    cleaned = remove_accents(name)
    # Supprimer caracteres speciaux problematiques
    cleaned = re.sub(r'[#%&{}\\<>*?/$!\'"`:@+|=]', "", cleaned)
    # Remplacer doubles espaces
    cleaned = re.sub(r"\s+", " ", cleaned).strip()
    return cleaned


def get_root_folder(path):
    """Extrait le dossier racine d'un chemin."""
    parts = path.split("/")
    return parts[0] if parts else ""


def get_second_level(path):
    """Extrait le deuxieme niveau d'un chemin."""
    parts = path.split("/")
    return parts[1] if len(parts) > 1 else ""


# ---------------------------------------------------------------------------
# Mapping engine
# ---------------------------------------------------------------------------
def compute_mapping(items):
    """Calcule le mapping ancien -> nouveau pour chaque element."""
    mapping = []

    for item in items:
        path = item["_path"]
        name = item["name"]
        depth = int(item["_depth"])
        mime = item["mimeType"]
        is_folder = mime == "application/vnd.google-apps.folder"

        result = {
            "id": item["id"],
            "name": name,
            "current_path": path,
            "mime_type": mime,
            "size": item.get("size", ""),
            "target_path": "",
            "action": "",
            "status": "",
            "notes": "",
        }

        root = get_root_folder(path)

        # --- Fichiers/dossiers a la racine (depth=0) ---
        if depth == 0:
            # Systeme B -> Mapper vers cible (contient du contenu)
            if name in SYSTEM_B_MAPPING:
                target = SYSTEM_B_MAPPING[name]
                result["action"] = "MOVE"
                result["target_path"] = target
                result["status"] = "READY"
                result["notes"] = f"Systeme B {name} -> {target}"
                mapping.append(result)
                continue

            # Dossiers orphelins schoolsWP
            if name in ORPHAN_MAPPING:
                target = ORPHAN_MAPPING[name]
                result["action"] = "MOVE"
                result["target_path"] = target
                result["status"] = "READY"
                result["notes"] = "Orphelin schoolsWP -> structure cible"
                mapping.append(result)
                continue

            # Dossiers speciaux
            if name in SPECIAL_MAPPING:
                target = SPECIAL_MAPPING[name]
                result["action"] = "MOVE"
                result["target_path"] = target
                result["status"] = "READY"
                result["notes"] = "Dossier special -> structure cible"
                mapping.append(result)
                continue

            # Systeme A
            if name in SYSTEM_A_MAPPING:
                target = SYSTEM_A_MAPPING[name]
                result["action"] = "RENAME_MOVE"
                result["target_path"] = target
                result["status"] = "READY"
                result["notes"] = f"Systeme A -> {target}"
                mapping.append(result)
                continue

            # Fichiers volants racine
            if not is_folder:
                if name in ROOT_FILE_MAPPING:
                    result["action"] = "MOVE"
                    result["target_path"] = ROOT_FILE_MAPPING[name]
                    result["status"] = "READY"
                    result["notes"] = "Fichier volant racine -> destination"
                else:
                    result["action"] = "MOVE"
                    result["target_path"] = "00_Inbox"
                    result["status"] = "READY"
                    result["notes"] = "Fichier racine non mappe -> Inbox pour tri"
                mapping.append(result)
                continue

            # Cas non prevu
            result["action"] = "REVIEW"
            result["status"] = "NEEDS_REVIEW"
            result["notes"] = "Element racine non mappe"
            mapping.append(result)
            continue

        # --- Elements sous 06_CONTENUS (depth >= 1) ---
        if root == "06_CONTENUS":
            second = get_second_level(path)
            if second in CONTENUS_SUBFOLDER_MAPPING:
                old_prefix = f"06_CONTENUS/{second}"
                new_prefix = CONTENUS_SUBFOLDER_MAPPING[second]
                result["target_path"] = path.replace(old_prefix, new_prefix, 1)
                result["action"] = "MOVE"
                result["status"] = "READY"
                result["notes"] = "06_CONTENUS redistribue"
            else:
                result["target_path"] = path.replace(
                    "06_CONTENUS", "01_Projets/schoolsWP/02_Contenu", 1
                )
                result["action"] = "MOVE"
                result["status"] = "NEEDS_REVIEW"
                result["notes"] = "06_CONTENUS sous-dossier non mappe"
            mapping.append(result)
            continue

        # --- Elements sous 04_ASSETS (depth >= 1) ---
        if root == "04_ASSETS":
            second = get_second_level(path)
            if second in ASSETS_SUBFOLDER_MAPPING:
                old_prefix = f"04_ASSETS/{second}"
                new_prefix = ASSETS_SUBFOLDER_MAPPING[second]
                result["target_path"] = path.replace(old_prefix, new_prefix, 1)
                result["action"] = "MOVE"
                result["status"] = "READY"
                result["notes"] = "04_ASSETS redistribue"
            else:
                result["target_path"] = path.replace(
                    "04_ASSETS", "01_Projets/schoolsWP/04_Assets", 1
                )
                result["action"] = "MOVE"
                result["status"] = "NEEDS_REVIEW"
                result["notes"] = "04_ASSETS sous-dossier non mappe"
            mapping.append(result)
            continue

        # --- Elements sous 03_RESSOURCES (depth >= 1) ---
        if root == "03_RESSOURCES":
            second = get_second_level(path)
            # Doublons vides a supprimer
            if second in RESSOURCES_EMPTY_DUPES and depth == 1 and is_folder:
                result["action"] = "DELETE"
                result["status"] = "READY"
                result["notes"] = "Doublon vide dans 03_RESSOURCES"
                mapping.append(result)
                continue
            # Inspirations -> Archive
            if second == "06_Inspirations":
                result["target_path"] = path.replace(
                    "03_RESSOURCES/06_Inspirations",
                    "99_Archives/Inspirations",
                    1,
                )
                result["action"] = "MOVE"
                result["status"] = "READY"
                result["notes"] = "Inspirations (2.1 Go) -> archive"
                mapping.append(result)
                continue
            # Reste -> 02_Ressources
            result["target_path"] = path.replace("03_RESSOURCES", "02_Ressources", 1)
            result["action"] = "MOVE"
            result["status"] = "READY"
            result["notes"] = "03_RESSOURCES -> 02_Ressources"
            mapping.append(result)
            continue

        # --- Elements sous 02_PROJETS (depth >= 1) ---
        if root == "02_PROJETS":
            result["target_path"] = path.replace("02_PROJETS", "01_Projets", 1)
            result["action"] = "MOVE"
            result["status"] = "READY"
            result["notes"] = "02_PROJETS -> 01_Projets"
            mapping.append(result)
            continue

        # --- Elements sous 01_ADMIN (depth >= 1) ---
        if root == "01_ADMIN":
            result["target_path"] = path.replace("01_ADMIN", "03_Admin", 1)
            result["action"] = "MOVE"
            result["status"] = "READY"
            result["notes"] = "01_ADMIN -> 03_Admin"
            mapping.append(result)
            continue

        # --- Elements sous 07_personnel ---
        if root == "07_personnel":
            result["target_path"] = path.replace("07_personnel", "04_Personnel", 1)
            result["action"] = "MOVE"
            result["status"] = "READY"
            result["notes"] = "07_personnel -> 04_Personnel"
            mapping.append(result)
            continue

        # --- Elements sous 99_ARCHIVES ---
        if root == "99_ARCHIVES":
            result["target_path"] = path.replace("99_ARCHIVES", "99_Archives", 1)
            result["action"] = "RENAME"
            result["status"] = "READY"
            result["notes"] = "Renommage casse 99_ARCHIVES -> 99_Archives"
            mapping.append(result)
            continue

        # --- Elements sous PROMPTS_schoolsWP ---
        if root == "PROMPTS_schoolsWP":
            result["target_path"] = path.replace(
                "PROMPTS_schoolsWP", "01_Projets/schoolsWP/08_IA-et-Prompts", 1
            )
            result["action"] = "MOVE"
            result["status"] = "READY"
            result["notes"] = "PROMPTS_schoolsWP -> IA-et-Prompts"
            mapping.append(result)
            continue

        # --- Elements sous MEDICALE ---
        if root == "MÉDICALE":
            result["target_path"] = path.replace(
                "MÉDICALE", "04_Personnel/Medical", 1
            )
            result["action"] = "MOVE"
            result["status"] = "READY"
            result["notes"] = "MEDICALE -> 04_Personnel/Medical"
            mapping.append(result)
            continue

        # --- Elements sous _BACKUP ---
        if root == "_BACKUP_DRIVE_2026-02-09":
            result["target_path"] = path.replace(
                "_BACKUP_DRIVE_2026-02-09",
                "99_Archives/2026-02-09_Backup-Drive",
                1,
            )
            result["action"] = "MOVE"
            result["status"] = "READY"
            result["notes"] = "Backup -> Archives"
            mapping.append(result)
            continue

        # --- Elements sous 00_START-HERE -> 02_Ressources ---
        if root == "00_START-HERE":
            result["target_path"] = path.replace(
                "00_START-HERE", "02_Ressources/Organisation", 1
            )
            result["action"] = "MOVE"
            result["status"] = "READY"
            result["notes"] = "00_START-HERE -> 02_Ressources/Organisation"
            mapping.append(result)
            continue

        # --- Elements sous 05_CLIENTS -> 99_Archives/Clients ---
        if root == "05_CLIENTS":
            result["target_path"] = path.replace(
                "05_CLIENTS", "99_Archives/Clients", 1
            )
            result["action"] = "MOVE"
            result["status"] = "READY"
            result["notes"] = "05_CLIENTS -> 99_Archives/Clients"
            mapping.append(result)
            continue

        # --- Elements sous dossiers orphelins (contenu des orphelins) ---
        if root in ORPHAN_MAPPING:
            target_root = ORPHAN_MAPPING[root]
            result["target_path"] = path.replace(root, target_root, 1)
            result["action"] = "MOVE"
            result["status"] = "READY"
            result["notes"] = f"Contenu orphelin {root} -> {target_root}"
            mapping.append(result)
            continue

        # --- Elements sous dossiers systeme B (contenu reel) ---
        if root in SYSTEM_B_MAPPING:
            target_root = SYSTEM_B_MAPPING[root]
            result["target_path"] = path.replace(root, target_root, 1)
            result["action"] = "MOVE"
            result["status"] = "READY"
            result["notes"] = f"Systeme B {root} -> {target_root}"
            mapping.append(result)
            continue

        # --- Catch-all ---
        result["action"] = "REVIEW"
        result["status"] = "NEEDS_REVIEW"
        result["notes"] = f"Element non mappe (racine: {root})"
        mapping.append(result)

    return mapping


# ---------------------------------------------------------------------------
# Target tree generation
# ---------------------------------------------------------------------------
def generate_target_tree(mapping):
    """Genere l'arborescence cible a partir du mapping."""
    # Collecter tous les chemins cibles
    paths = set()
    for item in mapping:
        target = item["target_path"]
        if target and item["action"] not in ("DELETE",):
            # Ajouter le chemin complet et tous ses parents
            parts = target.split("/")
            for i in range(1, len(parts) + 1):
                paths.add("/".join(parts[:i]))

    # Ajouter les dossiers cibles structurels
    structural = [
        "00_Inbox",
        "01_Projets",
        "01_Projets/schoolsWP",
        "01_Projets/schoolsWP/00_README",
        "01_Projets/schoolsWP/01_Strategie",
        "01_Projets/schoolsWP/02_Contenu",
        "01_Projets/schoolsWP/02_Contenu/01_Blog",
        "01_Projets/schoolsWP/02_Contenu/02_Newsletter",
        "01_Projets/schoolsWP/02_Contenu/03_YouTube",
        "01_Projets/schoolsWP/02_Contenu/04_Reseaux-Sociaux",
        "01_Projets/schoolsWP/03_SEO",
        "01_Projets/schoolsWP/04_Assets",
        "01_Projets/schoolsWP/04_Assets/01_Branding",
        "01_Projets/schoolsWP/04_Assets/02_Thumbnails",
        "01_Projets/schoolsWP/04_Assets/03_Illustrations",
        "01_Projets/schoolsWP/04_Assets/04_Covers",
        "01_Projets/schoolsWP/04_Assets/05_Sources-Design",
        "01_Projets/schoolsWP/05_Marketing",
        "01_Projets/schoolsWP/05_Marketing/01_Affiliation",
        "01_Projets/schoolsWP/05_Marketing/02_Publicite",
        "01_Projets/schoolsWP/05_Marketing/03_Partenariats",
        "01_Projets/schoolsWP/06_Technique",
        "01_Projets/schoolsWP/07_Automatisation",
        "01_Projets/schoolsWP/08_IA-et-Prompts",
        "01_Projets/schoolsWP/08_IA-et-Prompts/01_Prompts",
        "01_Projets/schoolsWP/08_IA-et-Prompts/02_Templates",
        "01_Projets/schoolsWP/09_Veille",
        "01_Projets/schoolsWP/10_Analytics",
        "01_Projets/schoolsWP/99_Archive",
        "01_Projets/Mon-Mini-Electro",
        "02_Ressources",
        "02_Ressources/Outils",
        "03_Admin",
        "04_Personnel",
        "04_Personnel/Medical",
        "04_Personnel/Photos",
        "99_Archives",
    ]
    paths.update(structural)

    # Trier et formater en arbre
    sorted_paths = sorted(paths)
    tree_lines = ["# Arborescence cible Google Drive -- schoolsWP", "", "```"]

    for path in sorted_paths:
        depth = path.count("/")
        name = path.split("/")[-1]
        indent = "    " * depth
        prefix = "├── " if depth > 0 else ""
        tree_lines.append(f"{indent}{prefix}{name}/")

    tree_lines.append("```")
    tree_lines.append("")
    tree_lines.append(f"Total dossiers cibles : {len(sorted_paths)}")
    tree_lines.append(f"Genere le : {datetime.now().isoformat()}")

    return "\n".join(tree_lines)


# ---------------------------------------------------------------------------
# Summary
# ---------------------------------------------------------------------------
def generate_summary(mapping):
    """Genere un resume JSON du plan de migration."""
    actions = Counter(m["action"] for m in mapping)
    statuses = Counter(m["status"] for m in mapping)
    needs_review = [m for m in mapping if m["status"] == "NEEDS_REVIEW"]

    return {
        "generated_at": datetime.now().isoformat(),
        "total_items": len(mapping),
        "actions": dict(actions.most_common()),
        "statuses": dict(statuses),
        "needs_review_count": len(needs_review),
        "needs_review_items": [
            {
                "name": m["name"],
                "current_path": m["current_path"],
                "action": m["action"],
                "notes": m["notes"],
            }
            for m in needs_review
        ],
        "ready_count": statuses.get("READY", 0),
        "delete_count": actions.get("DELETE", 0),
    }


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------
def main():
    parser = argparse.ArgumentParser(
        description="Genere un plan de migration Google Drive (dry-run)"
    )
    parser.add_argument(
        "--inventory",
        default=DEFAULT_INVENTORY,
        help=f"Chemin vers inventory.csv (defaut: {DEFAULT_INVENTORY})",
    )
    parser.add_argument(
        "--output-dir",
        default=DEFAULT_OUTPUT,
        help=f"Dossier de sortie (defaut: {DEFAULT_OUTPUT})",
    )
    args = parser.parse_args()

    print("=" * 60)
    print("  GOOGLE DRIVE MIGRATION PLAN -- schoolsWP")
    print("  Mode : DRY-RUN (aucune modification sur le Drive)")
    print("=" * 60)

    # Lire l'inventaire
    print(f"\n[1/4] Lecture de {args.inventory}...")
    if not os.path.exists(args.inventory):
        print(f"ERREUR : {args.inventory} introuvable.")
        print("Lance d'abord gdrive-audit.py pour generer l'inventaire.")
        return

    items = []
    with open(args.inventory, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            items.append(row)

    print(f"  OK -- {len(items)} elements charges")

    # Calculer le mapping
    print("\n[2/4] Calcul du mapping ancien -> nouveau...")
    mapping = compute_mapping(items)
    print(f"  OK -- {len(mapping)} elements mappes")

    # Generer les sorties
    os.makedirs(args.output_dir, exist_ok=True)

    # migration_mapping.csv
    print(f"\n[3/4] Export dans {args.output_dir}/")
    mapping_path = os.path.join(args.output_dir, "migration_mapping.csv")
    fieldnames = [
        "id", "name", "current_path", "target_path",
        "action", "status", "notes", "mime_type", "size",
    ]
    with open(mapping_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(mapping)
    print(f"  -> {mapping_path} ({len(mapping)} lignes)")

    # target_tree.md
    tree = generate_target_tree(mapping)
    tree_path = os.path.join(args.output_dir, "target_tree.md")
    with open(tree_path, "w", encoding="utf-8") as f:
        f.write(tree)
    print(f"  -> {tree_path}")

    # migration_summary.json
    summary = generate_summary(mapping)
    summary_path = os.path.join(args.output_dir, "migration_summary.json")
    with open(summary_path, "w", encoding="utf-8") as f:
        json.dump(summary, f, ensure_ascii=False, indent=2)
    print(f"  -> {summary_path}")

    # Resume console
    print("\n" + "=" * 60)
    print("  RESUME DU PLAN DE MIGRATION")
    print("=" * 60)
    print(f"  Elements total   : {summary['total_items']}")
    print(f"  Prets (READY)    : {summary['ready_count']}")
    print(f"  A revoir         : {summary['needs_review_count']}")
    print(f"  A supprimer      : {summary['delete_count']}")
    print(f"\n  Actions prevues :")
    for action, count in sorted(summary["actions"].items(), key=lambda x: -x[1]):
        print(f"    {action:20s} : {count}")

    if summary["needs_review_items"]:
        print(f"\n  Elements NEEDS_REVIEW ({summary['needs_review_count']}) :")
        for item in summary["needs_review_items"][:20]:
            print(f"    - [{item['action']}] {item['current_path']}")
            print(f"      -> {item['notes']}")

    print("\n" + "=" * 60)
    print("  PROCHAINES ETAPES :")
    print("  1. Verifier migration_mapping.csv (surtout les NEEDS_REVIEW)")
    print("  2. Valider target_tree.md")
    print("  3. Lancer gdrive-migration-apply.py --apply")
    print("=" * 60)

    # [4/4] Rapport NEEDS_REVIEW separe
    print("\n[4/4] Export rapport NEEDS_REVIEW...")
    review_items = [m for m in mapping if m["status"] == "NEEDS_REVIEW"]
    if review_items:
        review_path = os.path.join(args.output_dir, "needs_review.csv")
        with open(review_path, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(review_items)
        print(f"  -> {review_path} ({len(review_items)} elements a revoir)")
    else:
        print("  Aucun element a revoir -- tout est READY")


if __name__ == "__main__":
    main()
