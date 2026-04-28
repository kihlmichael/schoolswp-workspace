#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Google Drive Audit Script - schoolsWP
=====================================
Analyse l'arborescence Google Drive et détecte les problèmes de nomenclature.

Mode: DRY-RUN par défaut (lecture seule, aucune modification)

Usage:
    python audit_drive.py                    # Audit complet
    python audit_drive.py --folder-id XXX    # Audit d'un dossier spécifique
    python audit_drive.py --max-depth 5      # Limiter la profondeur
    python audit_drive.py --output rapport   # Nom du fichier de sortie

Prérequis:
    pip install -r requirements.txt
"""

import re
import json
import csv
import argparse
from datetime import datetime
from collections import defaultdict
from pathlib import Path

# Module commun Google Drive (authentification + config)
from google_drive_common import get_drive_service, HttpError, SCOPES_READ

# === RÈGLES D'AUDIT ===
NAMING_RULES = {
    'max_depth': 6,                    # Profondeur max recommandée
    'max_name_length': 100,            # Longueur max nom fichier
    'forbidden_chars': ['#', '%', '&', '{', '}', '\\', '<', '>', '*', '?', '/', '$', '!', "'", '"', ':', '@', '+', '`', '|', '='],
    'version_patterns': [
        r'_v\d+$', r'_V\d+$', r'\sv\d+$', r'\sV\d+$',
        r'_final$', r'_Final$', r'_FINAL$',
        r'_final_?\d*$', r'_copie$', r'_copy$', r'\(\d+\)$'
    ],
    'date_patterns': [
        r'\d{4}-\d{2}-\d{2}',          # 2024-01-15 (ISO - recommandé)
        r'\d{2}-\d{2}-\d{4}',          # 15-01-2024
        r'\d{2}/\d{2}/\d{4}',          # 15/01/2024
        r'\d{8}',                       # 20240115
    ],
    'case_styles': {
        'PascalCase': r'^[A-Z][a-zA-Z0-9]*$',
        'camelCase': r'^[a-z][a-zA-Z0-9]*$',
        'snake_case': r'^[a-z][a-z0-9_]*$',
        'kebab-case': r'^[a-z][a-z0-9-]*$',
        'UPPER_CASE': r'^[A-Z][A-Z0-9_]*$',
        'Title Case': r'^[A-Z][a-z]+(?: [A-Z][a-z]+)*$',
    }
}


class DriveAuditor:
    """Auditeur Google Drive avec analyse de nomenclature."""

    def __init__(self, max_depth=None):
        self.service = None
        self.max_depth = max_depth or NAMING_RULES['max_depth']
        self.items = []
        self.issues = defaultdict(list)
        self.stats = {
            'total_files': 0,
            'total_folders': 0,
            'total_size_bytes': 0,
            'max_depth_found': 0,
            'file_types': defaultdict(int),
            'naming_styles': defaultdict(int),
        }

    def authenticate(self):
        """Authentification via module commun (lecture seule)."""
        self.service = get_drive_service(write_access=False)
        return self.service is not None

    def scan_drive(self, folder_id='root', path='', depth=0):
        """Scan récursif du Drive."""
        if depth > self.max_depth:
            self.issues['profondeur_excessive'].append({
                'path': path,
                'depth': depth,
                'message': f"Profondeur {depth} > max {self.max_depth}"
            })
            return

        self.stats['max_depth_found'] = max(self.stats['max_depth_found'], depth)

        try:
            query = f"'{folder_id}' in parents and trashed = false"
            page_token = None

            while True:
                results = self.service.files().list(
                    q=query,
                    spaces='drive',
                    fields='nextPageToken, files(id, name, mimeType, size, createdTime, modifiedTime, owners)',
                    pageToken=page_token,
                    pageSize=1000
                ).execute()

                items = results.get('files', [])

                for item in items:
                    item_path = f"{path}/{item['name']}" if path else item['name']
                    is_folder = item['mimeType'] == 'application/vnd.google-apps.folder'

                    # Enregistrer l'item
                    self.items.append({
                        'id': item['id'],
                        'name': item['name'],
                        'path': item_path,
                        'type': 'folder' if is_folder else 'file',
                        'mimeType': item['mimeType'],
                        'size': int(item.get('size', 0)),
                        'depth': depth,
                        'created': item.get('createdTime', ''),
                        'modified': item.get('modifiedTime', ''),
                    })

                    # Stats
                    if is_folder:
                        self.stats['total_folders'] += 1
                    else:
                        self.stats['total_files'] += 1
                        self.stats['total_size_bytes'] += int(item.get('size', 0))
                        ext = Path(item['name']).suffix.lower() or '(sans extension)'
                        self.stats['file_types'][ext] += 1

                    # Analyser la nomenclature
                    self._analyze_naming(item, item_path, depth)

                    # Récursion pour les dossiers
                    if is_folder:
                        self.scan_drive(item['id'], item_path, depth + 1)

                page_token = results.get('nextPageToken')
                if not page_token:
                    break

        except HttpError as e:
            print(f"❌ Erreur API: {e}")

    def _analyze_naming(self, item, path, depth):
        """Analyse les problèmes de nomenclature."""
        name = item['name']

        # 1. Caractères interdits
        for char in NAMING_RULES['forbidden_chars']:
            if char in name:
                self.issues['caracteres_interdits'].append({
                    'path': path,
                    'char': char,
                    'message': f"Caractère interdit: '{char}'"
                })

        # 2. Longueur excessive
        if len(name) > NAMING_RULES['max_name_length']:
            self.issues['nom_trop_long'].append({
                'path': path,
                'length': len(name),
                'message': f"Nom trop long: {len(name)} caractères"
            })

        # 3. Patterns de version problématiques
        for pattern in NAMING_RULES['version_patterns']:
            if re.search(pattern, name, re.IGNORECASE):
                self.issues['versioning_chaotique'].append({
                    'path': path,
                    'pattern': pattern,
                    'message': f"Version non standard détectée"
                })
                break

        # 4. Espaces en début/fin
        if name != name.strip():
            self.issues['espaces_parasites'].append({
                'path': path,
                'message': "Espaces en début ou fin de nom"
            })

        # 5. Espaces multiples
        if '  ' in name:
            self.issues['espaces_multiples'].append({
                'path': path,
                'message': "Espaces multiples consécutifs"
            })

        # 6. Casing incohérent (dossiers uniquement)
        if item['mimeType'] == 'application/vnd.google-apps.folder':
            detected_style = self._detect_case_style(name)
            self.stats['naming_styles'][detected_style] += 1

        # 7. Dates incohérentes
        date_formats_found = []
        for pattern in NAMING_RULES['date_patterns']:
            if re.search(pattern, name):
                date_formats_found.append(pattern)
        if len(date_formats_found) > 1:
            self.issues['dates_multiformats'].append({
                'path': path,
                'formats': date_formats_found,
                'message': "Plusieurs formats de date détectés"
            })

        # 8. Noms génériques/ambigus
        generic_names = ['nouveau', 'new', 'test', 'temp', 'tmp', 'copie', 'copy',
                        'sans titre', 'untitled', 'document', 'fichier', 'dossier']
        if name.lower() in generic_names or any(name.lower().startswith(g) for g in generic_names):
            self.issues['noms_generiques'].append({
                'path': path,
                'message': f"Nom générique/ambigu: '{name}'"
            })

        # 9. Mélange de langues (FR/EN) dans un même nom
        fr_words = ['projet', 'dossier', 'fichier', 'archive', 'brouillon', 'final']
        en_words = ['project', 'folder', 'file', 'archive', 'draft', 'final']
        has_fr = any(w in name.lower() for w in fr_words)
        has_en = any(w in name.lower() for w in en_words if w not in fr_words)  # 'archive' et 'final' existent dans les deux
        if has_fr and has_en:
            self.issues['melange_langues'].append({
                'path': path,
                'message': "Mélange FR/EN dans le nom"
            })

    def _detect_case_style(self, name):
        """Détecte le style de casing d'un nom."""
        # Retirer l'extension si présent
        base_name = Path(name).stem

        for style, pattern in NAMING_RULES['case_styles'].items():
            if re.match(pattern, base_name):
                return style

        # Patterns composites
        if '_' in base_name and base_name[0].isupper():
            return 'Mixed_Case'
        if '-' in base_name and base_name[0].isupper():
            return 'Mixed-Case'
        if ' ' in base_name:
            return 'Avec espaces'

        return 'Autre/Mixte'

    def detect_duplicates(self):
        """Détecte les doublons potentiels."""
        name_map = defaultdict(list)

        for item in self.items:
            # Normaliser le nom pour comparaison
            normalized = item['name'].lower().strip()
            normalized = re.sub(r'[\s_-]+', ' ', normalized)
            normalized = re.sub(r'\s*\(\d+\)\s*$', '', normalized)  # Retirer (1), (2), etc.
            normalized = re.sub(r'\s*v\d+\s*$', '', normalized, flags=re.IGNORECASE)

            name_map[normalized].append(item)

        for name, items in name_map.items():
            if len(items) > 1:
                self.issues['doublons_potentiels'].append({
                    'name': name,
                    'count': len(items),
                    'paths': [i['path'] for i in items],
                    'message': f"{len(items)} fichiers similaires"
                })

    def generate_report(self, output_base='audit_drive'):
        """Génère les rapports JSON et CSV."""
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')

        # Rapport principal JSON
        report = {
            'metadata': {
                'generated_at': datetime.now().isoformat(),
                'mode': 'DRY-RUN (lecture seule)',
                'scope': SCOPES_READ[0],
            },
            'statistics': {
                'total_files': self.stats['total_files'],
                'total_folders': self.stats['total_folders'],
                'total_items': len(self.items),
                'total_size_gb': round(self.stats['total_size_bytes'] / (1024**3), 2),
                'max_depth': self.stats['max_depth_found'],
                'file_types': dict(sorted(self.stats['file_types'].items(), key=lambda x: -x[1])[:20]),
                'naming_styles': dict(self.stats['naming_styles']),
            },
            'issues_summary': {
                category: len(issues) for category, issues in self.issues.items()
            },
            'issues_detail': dict(self.issues),
            'recommendations': self._generate_recommendations(),
        }

        json_file = f"{output_base}_{timestamp}.json"
        with open(json_file, 'w', encoding='utf-8') as f:
            json.dump(report, f, indent=2, ensure_ascii=False)
        print(f"📄 Rapport JSON: {json_file}")

        # Export CSV des items
        csv_file = f"{output_base}_{timestamp}_items.csv"
        with open(csv_file, 'w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=['path', 'name', 'type', 'size', 'depth', 'mimeType', 'modified'])
            writer.writeheader()
            for item in sorted(self.items, key=lambda x: x['path']):
                writer.writerow({
                    'path': item['path'],
                    'name': item['name'],
                    'type': item['type'],
                    'size': item['size'],
                    'depth': item['depth'],
                    'mimeType': item['mimeType'],
                    'modified': item['modified'],
                })
        print(f"📄 Export CSV: {csv_file}")

        # Export CSV des problèmes
        issues_csv = f"{output_base}_{timestamp}_issues.csv"
        with open(issues_csv, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(['category', 'path', 'message', 'detail'])
            for category, issues in self.issues.items():
                for issue in issues:
                    writer.writerow([
                        category,
                        issue.get('path', issue.get('name', '')),
                        issue.get('message', ''),
                        json.dumps({k: v for k, v in issue.items() if k not in ['path', 'message']}, ensure_ascii=False)
                    ])
        print(f"📄 Problèmes CSV: {issues_csv}")

        return report

    def _generate_recommendations(self):
        """Génère des recommandations basées sur l'audit."""
        recs = []

        # Basé sur les problèmes trouvés
        if self.issues['profondeur_excessive']:
            recs.append({
                'priority': 'HAUTE',
                'category': 'Structure',
                'action': f"Réduire la profondeur (max trouvé: {self.stats['max_depth_found']}, recommandé: {NAMING_RULES['max_depth']})",
                'impact': 'Navigation simplifiée, moins de clics'
            })

        if self.issues['versioning_chaotique']:
            recs.append({
                'priority': 'HAUTE',
                'category': 'Versioning',
                'action': "Adopter une convention de version unique: _v01, _v02 ou utiliser l'historique Google Docs",
                'impact': 'Clarté, suppression des doublons'
            })

        if self.issues['doublons_potentiels']:
            count = sum(i['count'] for i in self.issues['doublons_potentiels'])
            recs.append({
                'priority': 'HAUTE',
                'category': 'Doublons',
                'action': f"Nettoyer {count} fichiers en doublon potentiel",
                'impact': f"Économie d'espace, clarté"
            })

        if len(self.stats['naming_styles']) > 3:
            recs.append({
                'priority': 'MOYENNE',
                'category': 'Nomenclature',
                'action': "Standardiser le style de nommage (recommandé: snake_case ou kebab-case pour dossiers)",
                'impact': 'Cohérence visuelle'
            })

        if self.issues['noms_generiques']:
            recs.append({
                'priority': 'MOYENNE',
                'category': 'Clarté',
                'action': f"Renommer {len(self.issues['noms_generiques'])} éléments aux noms génériques",
                'impact': 'Retrouver les fichiers plus facilement'
            })

        # Quick wins
        quick_wins = []
        if self.issues['espaces_parasites']:
            quick_wins.append(f"Supprimer espaces parasites ({len(self.issues['espaces_parasites'])} fichiers)")
        if self.issues['caracteres_interdits']:
            quick_wins.append(f"Corriger caractères interdits ({len(self.issues['caracteres_interdits'])} fichiers)")

        if quick_wins:
            recs.append({
                'priority': 'QUICK WIN',
                'category': 'Nettoyage rapide',
                'action': ' | '.join(quick_wins),
                'impact': 'Corrections simples, impact immédiat'
            })

        return recs

    def print_summary(self):
        """Affiche un résumé dans le terminal."""
        print("\n" + "="*60)
        print("📊 RÉSUMÉ DE L'AUDIT GOOGLE DRIVE")
        print("="*60)

        print(f"\n📁 STATISTIQUES")
        print(f"   Dossiers: {self.stats['total_folders']:,}")
        print(f"   Fichiers: {self.stats['total_files']:,}")
        print(f"   Taille totale: {self.stats['total_size_bytes'] / (1024**3):.2f} Go")
        print(f"   Profondeur max: {self.stats['max_depth_found']}")

        print(f"\n📛 STYLES DE NOMMAGE (dossiers)")
        for style, count in sorted(self.stats['naming_styles'].items(), key=lambda x: -x[1])[:5]:
            print(f"   {style}: {count}")

        print(f"\n⚠️  PROBLÈMES DÉTECTÉS")
        total_issues = sum(len(v) for v in self.issues.values())
        if total_issues == 0:
            print("   ✅ Aucun problème majeur détecté!")
        else:
            for category, issues in sorted(self.issues.items(), key=lambda x: -len(x[1])):
                if issues:
                    print(f"   {category}: {len(issues)}")

        print(f"\n   Total: {total_issues} problèmes")
        print("="*60)


def main():
    parser = argparse.ArgumentParser(description='Audit Google Drive - Mode DRY-RUN')
    parser.add_argument('--folder-id', default='root', help='ID du dossier à auditer (défaut: root)')
    parser.add_argument('--max-depth', type=int, default=10, help='Profondeur max de scan (défaut: 10)')
    parser.add_argument('--output', default='audit_drive', help='Préfixe des fichiers de sortie')
    args = parser.parse_args()

    print("\n🔍 AUDIT GOOGLE DRIVE - schoolsWP")
    print("   Mode: DRY-RUN (lecture seule)")
    print(f"   Dossier: {'Racine' if args.folder_id == 'root' else args.folder_id}")
    print(f"   Profondeur max: {args.max_depth}")
    print("-"*40)

    auditor = DriveAuditor(max_depth=args.max_depth)

    if not auditor.authenticate():
        return

    print("\n⏳ Scan en cours...")
    auditor.scan_drive(folder_id=args.folder_id)

    print("⏳ Détection des doublons...")
    auditor.detect_duplicates()

    print("\n⏳ Génération des rapports...")
    auditor.generate_report(args.output)

    auditor.print_summary()

    print("\n✅ Audit terminé. Aucune modification n'a été effectuée.")
    print("   Consultez les fichiers JSON et CSV pour le détail.")


if __name__ == '__main__':
    main()
