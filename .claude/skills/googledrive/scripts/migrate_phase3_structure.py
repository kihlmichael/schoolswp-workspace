#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Google Drive Migration - Phase 3 : Réorganisation Structure
============================================================
Réorganise le Drive selon l'arborescence cible schoolsWP :
- Crée les dossiers racine manquants
- Déplace les contenus existants vers la nouvelle structure
- Applique la nomenclature standardisée

Mode: DRY-RUN par défaut (prévisualisation sans modification)
Utiliser --apply pour exécuter les déplacements

Usage:
    python migrate_phase3_structure.py                    # Dry-run
    python migrate_phase3_structure.py --apply            # Appliquer
    python migrate_phase3_structure.py --create-only      # Créer dossiers seulement

Prérequis:
    pip install -r requirements.txt
"""

import re
import json
import csv
import argparse
from datetime import datetime
from collections import defaultdict

# Module commun Google Drive (authentification + config)
from google_drive_common import get_drive_service, HttpError

# === ARBORESCENCE CIBLE ===
TARGET_STRUCTURE = {
    '00_boite_de_reception': {
        'description': 'Zone tampon - Tri hebdo obligatoire',
        'subfolders': ['a_trier']
    },
    '01_projets_actifs': {
        'description': 'Projets en cours (< 6 mois activité)',
        'subfolders': ['schoolswp']  # + autres projets
    },
    '02_ressources_transverses': {
        'description': 'Assets partagés entre projets',
        'subfolders': ['branding', 'templates', 'medias', 'outils']
    },
    '03_contenus': {
        'description': 'Production de contenu',
        'subfolders': ['linkedin', 'youtube', 'facebook', 'blog', 'newsletter']
    },
    '04_admin_legal': {
        'description': 'Docs légaux et comptabilité',
        'subfolders': ['entreprise', 'comptabilite', 'banque', 'assurances']
    },
    '05_formations': {
        'description': 'Apprentissage personnel',
        'subfolders': ['en_cours', 'terminees']
    },
    '06_archive': {
        'description': 'Projets clôturés',
        'subfolders': ['2024', '2025', '2026']
    },
    '07_personnel': {
        'description': 'Non-pro (si Drive mixte)',
        'subfolders': []
    }
}

# === MAPPING EXISTANT → CIBLE ===
# Basé sur l'audit de ton Drive
FOLDER_MAPPING = {
    # Format: 'nom_existant_lowercase': 'dossier_cible'
    '00_start-here': '02_ressources_transverses/templates',
    '04_assets': '02_ressources_transverses',
    '06_contenus': '03_contenus',
    '99_archives': '06_archive/2025',
    'à trier plus tard': '00_boite_de_reception/a_trier',

    # Contenus spécifiques
    'linkedin': '03_contenus/linkedin',
    'youtube': '03_contenus/youtube',
    'facebook': '03_contenus/facebook',
    'blog': '03_contenus/blog',
    'articles': '03_contenus/blog',

    # Assets
    'logos': '02_ressources_transverses/branding',
    'branding': '02_ressources_transverses/branding',
    'images': '02_ressources_transverses/medias',
    'templates': '02_ressources_transverses/templates',

    # Admin
    'admin': '04_admin_legal',
    'legal': '04_admin_legal/entreprise',
    'comptabilite': '04_admin_legal/comptabilite',
    'factures': '04_admin_legal/comptabilite',
    'devis': '04_admin_legal/comptabilite',

    # Formations
    'formation': '05_formations',
    'cours': '05_formations',

    # Personnel / Médical
    'michael kihl': '07_personnel',
    'personnel': '07_personnel',

    # Projets
    'schoolswp': '01_projets_actifs/schoolswp',
    'schoolswp.com': '01_projets_actifs/schoolswp',
}


class StructureMigrator:
    """Migrateur de structure Google Drive."""

    def __init__(self, dry_run=True):
        self.service = None
        self.dry_run = dry_run
        self.root_folders = {}  # Dossiers à la racine
        self.created_folders = {}  # Cache des dossiers créés
        self.moves = []
        self.stats = {
            'folders_created': 0,
            'folders_moved': 0,
            'files_moved': 0,
            'errors': 0,
        }

    def authenticate(self):
        """Authentification via module commun (écriture)."""
        self.service = get_drive_service(write_access=True, verbose=False)
        if not self.service:
            return False
        mode = "DRY-RUN" if self.dry_run else "APPLY"
        print(f"[OK] Authentification reussie (MODE {mode})")
        return True

    def scan_root_folders(self):
        """Récupère les dossiers à la racine du Drive."""
        print("\n[SCAN] Analyse de la racine du Drive...")

        try:
            query = "'root' in parents and mimeType = 'application/vnd.google-apps.folder' and trashed = false"
            results = self.service.files().list(
                q=query,
                spaces='drive',
                fields='files(id, name)',
                pageSize=100
            ).execute()

            for folder in results.get('files', []):
                self.root_folders[folder['name'].lower()] = {
                    'id': folder['id'],
                    'name': folder['name']
                }

            print(f"  {len(self.root_folders)} dossiers trouves a la racine")
            return True

        except HttpError as e:
            print(f"[ERREUR] {e}")
            return False

    def create_target_structure(self):
        """Crée l'arborescence cible si elle n'existe pas."""
        print("\n[STRUCTURE] Creation de l'arborescence cible...")

        for folder_name, config in TARGET_STRUCTURE.items():
            # Vérifier si le dossier existe déjà
            if folder_name in self.root_folders:
                folder_id = self.root_folders[folder_name]['id']
                print(f"  [EXISTE] {folder_name}")
            else:
                # Créer le dossier
                folder_id = self._create_folder(folder_name, 'root')
                if folder_id:
                    print(f"  [CREE]   {folder_name}")
                    self.stats['folders_created'] += 1

            if folder_id:
                self.created_folders[folder_name] = folder_id

                # Créer les sous-dossiers
                for subfolder in config.get('subfolders', []):
                    subfolder_path = f"{folder_name}/{subfolder}"
                    existing = self._find_folder(subfolder, folder_id)

                    if existing:
                        self.created_folders[subfolder_path] = existing
                        print(f"    [EXISTE] {subfolder}")
                    else:
                        sub_id = self._create_folder(subfolder, folder_id)
                        if sub_id:
                            self.created_folders[subfolder_path] = sub_id
                            print(f"    [CREE]   {subfolder}")
                            self.stats['folders_created'] += 1

    def _create_folder(self, name, parent_id):
        """Crée un dossier sur Google Drive."""
        if self.dry_run:
            return f"DRY-RUN-{name}"

        try:
            file_metadata = {
                'name': name,
                'mimeType': 'application/vnd.google-apps.folder',
                'parents': [parent_id] if parent_id != 'root' else []
            }
            folder = self.service.files().create(
                body=file_metadata,
                fields='id'
            ).execute()
            return folder.get('id')

        except HttpError as e:
            print(f"    [ERREUR] Creation {name}: {e}")
            self.stats['errors'] += 1
            return None

    def _find_folder(self, name, parent_id):
        """Cherche un dossier par nom dans un parent."""
        try:
            query = f"name = '{name}' and '{parent_id}' in parents and mimeType = 'application/vnd.google-apps.folder' and trashed = false"
            results = self.service.files().list(
                q=query,
                spaces='drive',
                fields='files(id)',
                pageSize=1
            ).execute()

            files = results.get('files', [])
            return files[0]['id'] if files else None

        except HttpError:
            return None

    def analyze_moves(self):
        """Analyse les déplacements à effectuer."""
        print("\n[ANALYSE] Detection des deplacements necessaires...")

        for folder_name_lower, folder_info in self.root_folders.items():
            # Ignorer les dossiers cibles déjà en place
            if folder_name_lower in TARGET_STRUCTURE:
                continue

            # Chercher un mapping
            target = None
            for pattern, dest in FOLDER_MAPPING.items():
                if pattern in folder_name_lower:
                    target = dest
                    break

            if target:
                self.moves.append({
                    'type': 'folder',
                    'id': folder_info['id'],
                    'name': folder_info['name'],
                    'from': '(racine)',
                    'to': target,
                    'action': 'MOVE'
                })
            else:
                # Pas de mapping → suggérer boîte de réception
                self.moves.append({
                    'type': 'folder',
                    'id': folder_info['id'],
                    'name': folder_info['name'],
                    'from': '(racine)',
                    'to': '00_boite_de_reception/a_trier',
                    'action': 'SUGGEST'
                })

        print(f"  {len(self.moves)} deplacements identifies")

    def apply_moves(self):
        """Applique les déplacements."""
        if self.dry_run:
            print("\n[DRY-RUN] Aucun deplacement effectue.")
            return

        confirmed_moves = [m for m in self.moves if m['action'] == 'MOVE']
        print(f"\n[APPLY] Application de {len(confirmed_moves)} deplacements...")

        for i, move in enumerate(confirmed_moves, 1):
            target_path = move['to']
            target_id = self.created_folders.get(target_path)

            if not target_id:
                print(f"  [{i}] SKIP: Dossier cible '{target_path}' non trouve")
                continue

            try:
                # Récupérer les parents actuels
                file = self.service.files().get(
                    fileId=move['id'],
                    fields='parents'
                ).execute()

                previous_parents = ",".join(file.get('parents', []))

                # Déplacer
                self.service.files().update(
                    fileId=move['id'],
                    addParents=target_id,
                    removeParents=previous_parents,
                    fields='id, parents'
                ).execute()

                self.stats['folders_moved'] += 1
                print(f"  [{i}] OK: {move['name'][:40]}... -> {target_path}")

            except HttpError as e:
                self.stats['errors'] += 1
                print(f"  [{i}] ERREUR: {move['name'][:40]}...")

    def generate_report(self, output_base='migration_phase3'):
        """Génère le rapport CSV."""
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        csv_file = f"{output_base}_{timestamp}.csv"

        with open(csv_file, 'w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=[
                'action', 'type', 'name', 'from', 'to', 'id'
            ])
            writer.writeheader()

            for move in self.moves:
                writer.writerow(move)

        print(f"\n[RAPPORT] {csv_file}")
        return csv_file

    def print_preview(self):
        """Affiche un aperçu des changements."""
        print(f"\n{'='*70}")
        print("APERCU DES DEPLACEMENTS")
        print('='*70)

        moves_by_action = defaultdict(list)
        for move in self.moves:
            moves_by_action[move['action']].append(move)

        if moves_by_action['MOVE']:
            print(f"\n  DEPLACEMENTS AUTOMATIQUES ({len(moves_by_action['MOVE'])})")
            for move in moves_by_action['MOVE'][:15]:
                print(f"    {move['name'][:35]}...")
                print(f"      -> {move['to']}")

        if moves_by_action['SUGGEST']:
            print(f"\n  SUGGESTIONS (a trier manuellement) ({len(moves_by_action['SUGGEST'])})")
            for move in moves_by_action['SUGGEST'][:10]:
                print(f"    ? {move['name'][:40]}...")

    def print_summary(self):
        """Affiche le résumé."""
        print(f"\n{'='*70}")
        print("RESUME PHASE 3 - REORGANISATION STRUCTURE")
        print('='*70)
        print(f"\n  Dossiers a la racine   : {len(self.root_folders)}")
        print(f"  Dossiers cibles crees  : {self.stats['folders_created']}")
        print(f"  Deplacements prevus    : {len([m for m in self.moves if m['action'] == 'MOVE'])}")
        print(f"  A trier manuellement   : {len([m for m in self.moves if m['action'] == 'SUGGEST'])}")

        if not self.dry_run:
            print(f"\n  Dossiers deplaces      : {self.stats['folders_moved']}")
            print(f"  Erreurs                : {self.stats['errors']}")

        print('='*70)


def main():
    parser = argparse.ArgumentParser(description='Migration Phase 3 - Réorganisation Structure')
    parser.add_argument('--apply', action='store_true', help='Appliquer les modifications (sinon dry-run)')
    parser.add_argument('--create-only', action='store_true', help='Creer seulement les dossiers cibles')
    parser.add_argument('--output', default='migration_phase3', help='Prefixe du fichier de sortie')
    args = parser.parse_args()

    mode = "APPLY" if args.apply else "DRY-RUN"
    print(f"\n{'='*70}")
    print(f"MIGRATION GOOGLE DRIVE - PHASE 3 REORGANISATION")
    print(f"Mode: {mode}")
    print('='*70)

    if args.apply and not args.create_only:
        print("\n[ATTENTION] Mode APPLY actif - Les dossiers seront deplaces!")
        confirm = input("Confirmer? (oui/non): ")
        if confirm.lower() not in ['oui', 'o', 'yes', 'y']:
            print("Annule.")
            return

    migrator = StructureMigrator(dry_run=not args.apply)

    if not migrator.authenticate():
        return

    migrator.scan_root_folders()
    migrator.create_target_structure()

    if not args.create_only:
        migrator.analyze_moves()
        migrator.print_preview()

    migrator.print_summary()

    if not args.create_only:
        csv_file = migrator.generate_report(args.output)

    if args.apply and not args.create_only:
        migrator.apply_moves()
        print(f"\n[OK] Phase 3 terminee.")

    if not args.apply:
        if args.create_only:
            print(f"\n[NEXT] Pour creer les dossiers:")
            print(f"       python migrate_phase3_structure.py --apply --create-only")
        else:
            print(f"\n[NEXT] Pour appliquer les deplacements:")
            print(f"       python migrate_phase3_structure.py --apply")


if __name__ == '__main__':
    main()
