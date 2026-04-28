#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Google Drive Migration - Phase 1 Quick Wins
============================================
Corrige les problèmes simples de nomenclature :
- Espaces parasites (début/fin)
- Caractère & → et
- Emojis → supprimés
- Espaces multiples → espace simple

Mode: DRY-RUN par défaut (prévisualisation sans modification)
Utiliser --apply pour exécuter les modifications

Usage:
    python migrate_phase1.py                    # Dry-run (prévisualisation)
    python migrate_phase1.py --apply            # Appliquer les modifications
    python migrate_phase1.py --output rapport   # Nom du fichier CSV

Prérequis:
    pip install -r requirements.txt
"""

import re
import csv
import argparse
from datetime import datetime

# Module commun Google Drive (authentification + config)
from google_drive_common import get_drive_service, HttpError

# === RÈGLES DE CORRECTION ===
EMOJI_PATTERN = re.compile(
    "["
    "\U0001F600-\U0001F64F"  # emoticons
    "\U0001F300-\U0001F5FF"  # symbols & pictographs
    "\U0001F680-\U0001F6FF"  # transport & map symbols
    "\U0001F1E0-\U0001F1FF"  # flags
    "\U00002702-\U000027B0"  # dingbats
    "\U000024C2-\U0001F251"  # enclosed characters
    "\U0001F900-\U0001F9FF"  # supplemental symbols
    "\U0001FA00-\U0001FA6F"  # chess symbols
    "\U0001FA70-\U0001FAFF"  # symbols extended
    "\U00002600-\U000026FF"  # misc symbols
    "]+",
    flags=re.UNICODE
)


def clean_name(name):
    """Applique les corrections Phase 1 à un nom."""
    original = name
    corrections = []

    # 1. Supprimer emojis
    new_name = EMOJI_PATTERN.sub('', name)
    if new_name != name:
        corrections.append('emoji_supprime')
        name = new_name

    # 2. Remplacer & par et (ou _et_ selon contexte)
    if '&' in name:
        # Si entouré d'espaces: " & " → " et "
        name = re.sub(r'\s*&\s*', ' et ', name)
        # Si collé: "A&B" → "A_et_B"
        name = re.sub(r'(\w)&(\w)', r'\1_et_\2', name)
        corrections.append('ampersand_remplace')

    # 3. Supprimer espaces en début/fin
    stripped = name.strip()
    if stripped != name:
        corrections.append('espaces_parasites')
        name = stripped

    # 4. Remplacer espaces multiples par espace simple
    new_name = re.sub(r'\s{2,}', ' ', name)
    if new_name != name:
        corrections.append('espaces_multiples')
        name = new_name

    # 5. Remplacer / par - (dans les noms, pas les chemins)
    if '/' in name:
        name = name.replace('/', '-')
        corrections.append('slash_remplace')

    # 6. Supprimer : si présent
    if ':' in name:
        name = name.replace(':', ' -')
        corrections.append('colon_remplace')

    # 7. Nettoyer tirets/espaces résultants
    name = re.sub(r'\s*-\s*-\s*', ' - ', name)
    name = re.sub(r'\s{2,}', ' ', name)
    name = name.strip()
    name = name.strip('-').strip()

    return name, corrections if name != original else []


class DriveMigrator:
    """Migrateur Google Drive - Phase 1."""

    def __init__(self, dry_run=True):
        self.service = None
        self.dry_run = dry_run
        self.changes = []
        self.errors = []
        self.stats = {
            'scanned': 0,
            'to_rename': 0,
            'renamed': 0,
            'skipped': 0,
            'errors': 0,
        }

    def authenticate(self):
        """Authentification via module commun (écriture)."""
        self.service = get_drive_service(write_access=True, verbose=False)
        if self.service:
            mode = "DRY-RUN" if self.dry_run else "APPLY"
            print(f"[OK] Authentification reussie (MODE {mode})")
        return self.service is not None

    def scan_and_prepare(self, folder_id='root', path=''):
        """Scan récursif et préparation des renommages."""
        try:
            query = f"'{folder_id}' in parents and trashed = false"
            page_token = None

            while True:
                results = self.service.files().list(
                    q=query,
                    spaces='drive',
                    fields='nextPageToken, files(id, name, mimeType)',
                    pageToken=page_token,
                    pageSize=1000
                ).execute()

                items = results.get('files', [])

                for item in items:
                    self.stats['scanned'] += 1
                    item_path = f"{path}/{item['name']}" if path else item['name']
                    is_folder = item['mimeType'] == 'application/vnd.google-apps.folder'

                    # Calculer le nouveau nom
                    new_name, corrections = clean_name(item['name'])

                    if corrections:
                        self.stats['to_rename'] += 1
                        self.changes.append({
                            'id': item['id'],
                            'old_name': item['name'],
                            'new_name': new_name,
                            'path': path or '(racine)',
                            'type': 'dossier' if is_folder else 'fichier',
                            'corrections': corrections,
                        })

                    # Récursion pour les dossiers
                    if is_folder:
                        self.scan_and_prepare(item['id'], item_path)

                page_token = results.get('nextPageToken')
                if not page_token:
                    break

        except HttpError as e:
            print(f"[ERREUR] API: {e}")
            self.stats['errors'] += 1

    def apply_changes(self):
        """Applique les renommages (seulement si dry_run=False)."""
        if self.dry_run:
            print("\n[DRY-RUN] Aucune modification effectuee.")
            print("          Utilisez --apply pour executer les changements.")
            return

        print(f"\n[APPLY] Application de {len(self.changes)} renommages...")

        for i, change in enumerate(self.changes, 1):
            try:
                self.service.files().update(
                    fileId=change['id'],
                    body={'name': change['new_name']}
                ).execute()

                self.stats['renamed'] += 1
                print(f"  [{i}/{len(self.changes)}] OK: {change['old_name'][:50]}...")

            except HttpError as e:
                self.stats['errors'] += 1
                self.errors.append({
                    'id': change['id'],
                    'name': change['old_name'],
                    'error': str(e)
                })
                print(f"  [{i}/{len(self.changes)}] ERREUR: {change['old_name'][:50]}...")

    def generate_report(self, output_base='migration_phase1'):
        """Génère le rapport CSV des changements."""
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')

        # CSV des changements
        csv_file = f"{output_base}_{timestamp}.csv"
        with open(csv_file, 'w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=[
                'status', 'type', 'old_name', 'new_name', 'path', 'corrections', 'id'
            ])
            writer.writeheader()

            for change in self.changes:
                status = 'RENAMED' if not self.dry_run and change['id'] not in [e['id'] for e in self.errors] else 'PENDING'
                writer.writerow({
                    'status': status,
                    'type': change['type'],
                    'old_name': change['old_name'],
                    'new_name': change['new_name'],
                    'path': change['path'],
                    'corrections': '|'.join(change['corrections']),
                    'id': change['id'],
                })

        print(f"\n[RAPPORT] {csv_file}")
        return csv_file

    def print_preview(self, limit=20):
        """Affiche un aperçu des changements."""
        print(f"\n{'='*70}")
        print(f"APERCU DES CHANGEMENTS ({min(limit, len(self.changes))}/{len(self.changes)})")
        print('='*70)

        for change in self.changes[:limit]:
            corrections_str = ', '.join(change['corrections'])
            print(f"\n  [{change['type'].upper()}] {change['path'][:40]}...")
            print(f"    AVANT : {change['old_name'][:60]}")
            print(f"    APRES : {change['new_name'][:60]}")
            print(f"    FIX   : {corrections_str}")

        if len(self.changes) > limit:
            print(f"\n  ... et {len(self.changes) - limit} autres changements")

    def print_summary(self):
        """Affiche le résumé."""
        print(f"\n{'='*70}")
        print("RESUME MIGRATION PHASE 1")
        print('='*70)
        print(f"\n  Elements scannes  : {self.stats['scanned']:,}")
        print(f"  A renommer        : {self.stats['to_rename']:,}")

        if not self.dry_run:
            print(f"  Renommes          : {self.stats['renamed']:,}")
            print(f"  Erreurs           : {self.stats['errors']:,}")

        # Stats par type de correction
        correction_counts = {}
        for change in self.changes:
            for corr in change['corrections']:
                correction_counts[corr] = correction_counts.get(corr, 0) + 1

        if correction_counts:
            print(f"\n  CORRECTIONS PAR TYPE:")
            for corr, count in sorted(correction_counts.items(), key=lambda x: -x[1]):
                print(f"    {corr}: {count}")

        print('='*70)


def main():
    parser = argparse.ArgumentParser(description='Migration Phase 1 - Quick Wins')
    parser.add_argument('--apply', action='store_true', help='Appliquer les modifications (sinon dry-run)')
    parser.add_argument('--output', default='migration_phase1', help='Prefixe du fichier de sortie')
    parser.add_argument('--preview-limit', type=int, default=20, help='Nombre d\'elements a previsualiser')
    args = parser.parse_args()

    mode = "APPLY" if args.apply else "DRY-RUN"
    print(f"\n{'='*70}")
    print(f"MIGRATION GOOGLE DRIVE - PHASE 1 QUICK WINS")
    print(f"Mode: {mode}")
    print('='*70)

    if args.apply:
        print("\n[ATTENTION] Mode APPLY actif - Les fichiers seront renommes!")
        confirm = input("Confirmer? (oui/non): ")
        if confirm.lower() not in ['oui', 'o', 'yes', 'y']:
            print("Annule.")
            return

    migrator = DriveMigrator(dry_run=not args.apply)

    if not migrator.authenticate():
        return

    print("\n[SCAN] Analyse en cours...")
    migrator.scan_and_prepare()

    migrator.print_preview(args.preview_limit)
    migrator.print_summary()

    csv_file = migrator.generate_report(args.output)

    if not args.apply:
        print(f"\n[NEXT] Pour appliquer les changements:")
        print(f"       python migrate_phase1.py --apply")
    else:
        migrator.apply_changes()
        print(f"\n[OK] Migration Phase 1 terminee.")


if __name__ == '__main__':
    main()
