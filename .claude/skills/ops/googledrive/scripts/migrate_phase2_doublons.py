#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Google Drive Migration - Phase 2 : Nettoyage Doublons
=====================================================
Identifie et nettoie les fichiers en doublon :
- Fichiers avec (1), (2), (copie), copy
- Fichiers identiques dans différents dossiers
- Versions multiples non gérées

Mode: DRY-RUN par défaut (prévisualisation sans suppression)
Utiliser --apply pour déplacer vers corbeille

Usage:
    python migrate_phase2_doublons.py                    # Dry-run
    python migrate_phase2_doublons.py --apply            # Déplacer vers corbeille
    python migrate_phase2_doublons.py --strategy newest  # Garder le plus récent

Prérequis:
    pip install -r requirements.txt
"""

import re
import csv
import argparse
from datetime import datetime
from collections import defaultdict

# Module commun Google Drive (authentification + config)
from google_drive_common import get_drive_service, HttpError

# Patterns de doublons
DUPLICATE_PATTERNS = [
    r'\s*\(\d+\)\s*$',           # (1), (2), etc.
    r'\s*-\s*Copie\s*\d*$',      # - Copie, - Copie 2
    r'\s*-\s*Copy\s*\d*$',       # - Copy
    r'\s*copie\s*\d*$',          # copie, copie 2
    r'\s*copy\s*\d*$',           # copy
    r'\s*\(copie\)\s*$',         # (copie)
    r'\s*\(copy\)\s*$',          # (copy)
]


def normalize_name(name):
    """Normalise un nom pour comparaison (sans extension ni suffixes de copie)."""
    # Retirer l'extension
    base = name
    if '.' in name:
        parts = name.rsplit('.', 1)
        if len(parts[1]) <= 5:  # Extension probable
            base = parts[0]

    # Retirer les patterns de doublon
    for pattern in DUPLICATE_PATTERNS:
        base = re.sub(pattern, '', base, flags=re.IGNORECASE)

    # Normaliser espaces et casse
    base = base.strip().lower()
    base = re.sub(r'\s+', ' ', base)

    return base


def is_duplicate_name(name):
    """Vérifie si le nom contient un pattern de doublon."""
    for pattern in DUPLICATE_PATTERNS:
        if re.search(pattern, name, re.IGNORECASE):
            return True
    return False


class DuplicateCleaner:
    """Nettoyeur de doublons Google Drive."""

    def __init__(self, dry_run=True, strategy='newest'):
        self.service = None
        self.dry_run = dry_run
        self.strategy = strategy  # newest, oldest, largest, smallest
        self.items = []
        self.duplicate_groups = defaultdict(list)
        self.to_delete = []
        self.stats = {
            'scanned': 0,
            'duplicates_found': 0,
            'groups': 0,
            'to_delete': 0,
            'deleted': 0,
            'space_saved_bytes': 0,
            'errors': 0,
        }

    def authenticate(self):
        """Authentification via module commun (écriture)."""
        self.service = get_drive_service(write_access=True, verbose=False)
        if self.service:
            mode = "DRY-RUN" if self.dry_run else "APPLY"
            print(f"[OK] Authentification reussie (MODE {mode})")
        return self.service is not None

    def scan_drive(self, folder_id='root', path=''):
        """Scan récursif pour trouver tous les fichiers."""
        try:
            query = f"'{folder_id}' in parents and trashed = false"
            page_token = None

            while True:
                results = self.service.files().list(
                    q=query,
                    spaces='drive',
                    fields='nextPageToken, files(id, name, mimeType, size, createdTime, modifiedTime, md5Checksum)',
                    pageToken=page_token,
                    pageSize=1000
                ).execute()

                items = results.get('files', [])

                for item in items:
                    self.stats['scanned'] += 1
                    item_path = f"{path}/{item['name']}" if path else item['name']
                    is_folder = item['mimeType'] == 'application/vnd.google-apps.folder'

                    if not is_folder:
                        self.items.append({
                            'id': item['id'],
                            'name': item['name'],
                            'path': item_path,
                            'parent_path': path or '(racine)',
                            'size': int(item.get('size', 0)),
                            'created': item.get('createdTime', ''),
                            'modified': item.get('modifiedTime', ''),
                            'md5': item.get('md5Checksum', ''),
                            'normalized': normalize_name(item['name']),
                            'is_copy_pattern': is_duplicate_name(item['name']),
                        })

                    # Récursion pour les dossiers
                    if is_folder:
                        self.scan_drive(item['id'], item_path)

                page_token = results.get('nextPageToken')
                if not page_token:
                    break

        except HttpError as e:
            print(f"[ERREUR] API: {e}")
            self.stats['errors'] += 1

    def find_duplicates(self):
        """Identifie les groupes de doublons."""
        # Grouper par nom normalisé
        name_groups = defaultdict(list)
        for item in self.items:
            name_groups[item['normalized']].append(item)

        # Filtrer les groupes avec plus d'un fichier
        for name, items in name_groups.items():
            if len(items) > 1:
                self.duplicate_groups[name] = items
                self.stats['duplicates_found'] += len(items)

        self.stats['groups'] = len(self.duplicate_groups)

        # Pour chaque groupe, déterminer lequel garder
        for name, items in self.duplicate_groups.items():
            keeper = self._select_keeper(items)
            for item in items:
                if item['id'] != keeper['id']:
                    item['action'] = 'DELETE'
                    item['reason'] = f"Doublon de: {keeper['name']}"
                    self.to_delete.append(item)
                else:
                    item['action'] = 'KEEP'
                    item['reason'] = f"Strategie: {self.strategy}"

        self.stats['to_delete'] = len(self.to_delete)
        self.stats['space_saved_bytes'] = sum(item['size'] for item in self.to_delete)

    def _select_keeper(self, items):
        """Sélectionne le fichier à garder selon la stratégie."""
        if self.strategy == 'newest':
            return max(items, key=lambda x: x['modified'] or x['created'] or '')
        elif self.strategy == 'oldest':
            return min(items, key=lambda x: x['modified'] or x['created'] or 'z')
        elif self.strategy == 'largest':
            return max(items, key=lambda x: x['size'])
        elif self.strategy == 'smallest':
            return min(items, key=lambda x: x['size'])
        elif self.strategy == 'original':
            # Préférer celui sans pattern de copie
            originals = [i for i in items if not i['is_copy_pattern']]
            if originals:
                return max(originals, key=lambda x: x['modified'] or '')
            return max(items, key=lambda x: x['modified'] or '')
        else:
            return items[0]

    def apply_deletions(self):
        """Déplace les doublons vers la corbeille."""
        if self.dry_run:
            print("\n[DRY-RUN] Aucune suppression effectuee.")
            print("          Utilisez --apply pour deplacer vers la corbeille.")
            return

        print(f"\n[APPLY] Deplacement de {len(self.to_delete)} fichiers vers la corbeille...")

        for i, item in enumerate(self.to_delete, 1):
            try:
                self.service.files().update(
                    fileId=item['id'],
                    body={'trashed': True}
                ).execute()

                self.stats['deleted'] += 1
                print(f"  [{i}/{len(self.to_delete)}] Corbeille: {item['name'][:50]}...")

            except HttpError as e:
                self.stats['errors'] += 1
                print(f"  [{i}/{len(self.to_delete)}] ERREUR: {item['name'][:50]}...")

    def generate_report(self, output_base='migration_phase2'):
        """Génère le rapport CSV."""
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')

        # CSV des doublons
        csv_file = f"{output_base}_{timestamp}.csv"
        with open(csv_file, 'w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=[
                'group', 'action', 'name', 'path', 'size_kb', 'modified', 'reason', 'id'
            ])
            writer.writeheader()

            for group_name, items in self.duplicate_groups.items():
                for item in items:
                    writer.writerow({
                        'group': group_name[:50],
                        'action': item.get('action', ''),
                        'name': item['name'],
                        'path': item['parent_path'],
                        'size_kb': round(item['size'] / 1024, 1),
                        'modified': item['modified'][:10] if item['modified'] else '',
                        'reason': item.get('reason', ''),
                        'id': item['id'],
                    })

        print(f"\n[RAPPORT] {csv_file}")
        return csv_file

    def print_preview(self, limit=15):
        """Affiche un aperçu des groupes de doublons."""
        print(f"\n{'='*70}")
        print(f"GROUPES DE DOUBLONS ({min(limit, len(self.duplicate_groups))}/{len(self.duplicate_groups)} groupes)")
        print('='*70)

        for i, (name, items) in enumerate(list(self.duplicate_groups.items())[:limit]):
            print(f"\n  GROUPE {i+1}: \"{name[:40]}...\" ({len(items)} fichiers)")
            for item in items:
                action = item.get('action', '?')
                size_kb = round(item['size'] / 1024, 1)
                marker = "[KEEP]  " if action == 'KEEP' else "[DELETE]"
                print(f"    {marker} {item['name'][:45]}... ({size_kb} KB)")
                print(f"             @ {item['parent_path'][:50]}")

        if len(self.duplicate_groups) > limit:
            print(f"\n  ... et {len(self.duplicate_groups) - limit} autres groupes")

    def print_summary(self):
        """Affiche le résumé."""
        print(f"\n{'='*70}")
        print("RESUME PHASE 2 - NETTOYAGE DOUBLONS")
        print('='*70)
        print(f"\n  Fichiers scannes      : {self.stats['scanned']:,}")
        print(f"  Groupes de doublons   : {self.stats['groups']:,}")
        print(f"  Fichiers en doublon   : {self.stats['duplicates_found']:,}")
        print(f"  A supprimer           : {self.stats['to_delete']:,}")
        print(f"  Espace a liberer      : {self.stats['space_saved_bytes'] / (1024*1024):.1f} MB")

        if not self.dry_run:
            print(f"\n  Supprimes (corbeille) : {self.stats['deleted']:,}")
            print(f"  Erreurs               : {self.stats['errors']:,}")

        print(f"\n  Strategie utilisee    : {self.strategy}")
        print('='*70)


def main():
    parser = argparse.ArgumentParser(description='Migration Phase 2 - Nettoyage Doublons')
    parser.add_argument('--apply', action='store_true', help='Deplacer vers corbeille (sinon dry-run)')
    parser.add_argument('--strategy', default='original',
                       choices=['newest', 'oldest', 'largest', 'smallest', 'original'],
                       help='Strategie pour choisir quel fichier garder (defaut: original)')
    parser.add_argument('--output', default='migration_phase2', help='Prefixe du fichier de sortie')
    parser.add_argument('--preview-limit', type=int, default=15, help='Nombre de groupes a previsualiser')
    args = parser.parse_args()

    mode = "APPLY" if args.apply else "DRY-RUN"
    print(f"\n{'='*70}")
    print(f"MIGRATION GOOGLE DRIVE - PHASE 2 NETTOYAGE DOUBLONS")
    print(f"Mode: {mode} | Strategie: {args.strategy}")
    print('='*70)

    if args.apply:
        print("\n[ATTENTION] Mode APPLY actif - Les fichiers seront mis a la corbeille!")
        print("            (Recuperables pendant 30 jours)")
        confirm = input("Confirmer? (oui/non): ")
        if confirm.lower() not in ['oui', 'o', 'yes', 'y']:
            print("Annule.")
            return

    cleaner = DuplicateCleaner(dry_run=not args.apply, strategy=args.strategy)

    if not cleaner.authenticate():
        return

    print("\n[SCAN] Analyse des fichiers en cours...")
    cleaner.scan_drive()

    print("[ANALYSE] Detection des doublons...")
    cleaner.find_duplicates()

    cleaner.print_preview(args.preview_limit)
    cleaner.print_summary()

    csv_file = cleaner.generate_report(args.output)

    if not args.apply:
        print(f"\n[NEXT] Pour appliquer les suppressions:")
        print(f"       python migrate_phase2_doublons.py --apply --strategy {args.strategy}")
    else:
        cleaner.apply_deletions()
        print(f"\n[OK] Phase 2 terminee. Fichiers dans la corbeille (recuperables 30j).")


if __name__ == '__main__':
    main()
