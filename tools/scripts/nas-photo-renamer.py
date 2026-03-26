#!/usr/bin/env python3
"""
NAS Photo Renamer
=================
Renomme les photos d'un dossier NAS en utilisant Gemini Vision.

Usage :
  python nas-photo-renamer.py --folder "\\\\192.168.18.109\\Photo\\photo\\2006\\CAP D'AGDE" --dry-run
  python nas-photo-renamer.py --folder "\\\\192.168.18.109\\Photo\\photo\\2006\\CAP D'AGDE" --execute
"""

import argparse
import base64
import getpass
import json
import os
import subprocess
import sys
import time
import urllib.request
import urllib.error
from pathlib import Path

sys.stdout.reconfigure(encoding='utf-8')

GEMINI_API_KEY = 'AIzaSyAb8-0N3EOn_T27-L6bB9sEeRu88JcRUX0'
GEMINI_URL     = 'https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent'

IMAGE_EXTENSIONS = {'.jpg', '.jpeg', '.png', '.heic', '.heif', '.webp', '.bmp', '.tiff', '.tif'}

GEMINI_PROMPT = (
    'Analyse cette photo. '
    'Retourne UNIQUEMENT un objet JSON valide (sans bloc markdown ni texte avant/après) avec ces propriétés : '
    '- city : string ou null (ville/lieu reconnaissable) '
    '- landmark : string ou null (monument identifiable) '
    '- scene_description : string (description brève en français, max 8 mots) '
    '- quality : objet avec overall (entier 1-10) '
    '- suggested_filename : string sans extension ni espace '
    '  (format: Lieu_Description_Detail — ex: CapdAgde_Plage_Coucher_Soleil, Paris_TourEiffel_Nuit). '
    '  Utilise la date ou le contexte visible si possible.'
)

MIME_MAP = {
    '.jpg': 'image/jpeg', '.jpeg': 'image/jpeg',
    '.png': 'image/png',  '.heic': 'image/heic',
    '.heif': 'image/heif', '.webp': 'image/webp',
    '.bmp': 'image/bmp',  '.tiff': 'image/tiff', '.tif': 'image/tiff'
}


def analyze_with_gemini(image_bytes, mime_type='image/jpeg'):
    image_b64 = base64.b64encode(image_bytes).decode('utf-8')
    payload = {
        'contents': [{
            'parts': [
                {'text': GEMINI_PROMPT},
                {'inline_data': {'mime_type': mime_type, 'data': image_b64}}
            ]
        }]
    }
    body = json.dumps(payload, ensure_ascii=False).encode('utf-8')
    req = urllib.request.Request(
        GEMINI_URL,
        data=body,
        headers={
            'x-goog-api-key': GEMINI_API_KEY,
            'Content-Type': 'application/json',
            'User-Agent': 'Mozilla/5.0'
        },
        method='POST'
    )
    try:
        with urllib.request.urlopen(req, timeout=60) as r:
            resp = json.loads(r.read())
    except urllib.error.HTTPError as e:
        raise RuntimeError(f"Gemini {e.code}: {e.read().decode()[:300]}")

    text = resp['candidates'][0]['content']['parts'][0]['text'].strip()
    if text.startswith('```'):
        text = text.split('\n', 1)[1].rsplit('```', 1)[0]
    return json.loads(text.strip())


def safe_filename(name):
    """Nettoie le nom pour éviter les caractères interdits Windows."""
    forbidden = r'\/:*?"<>|'
    for c in forbidden:
        name = name.replace(c, '_')
    return name.strip('. ')


def main():
    parser = argparse.ArgumentParser(description='Renomme les photos NAS via Gemini Vision')
    parser.add_argument('--folder', required=True, help='Chemin du dossier (ex: \\\\192.168.18.109\\Photo\\photo\\2006\\CAP D\'AGDE)')
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument('--dry-run', action='store_true', default=True, help='Affiche sans renommer (défaut)')
    mode.add_argument('--execute', action='store_true', help='Renomme réellement les fichiers')
    parser.add_argument('--limit', type=int, default=0, help='Limiter à N photos (pour test)')
    parser.add_argument('--prefix-number', action='store_true', help='Ajouter un numéro séquentiel ex: 001_Paris_...')
    parser.add_argument('--user', default='', help='Utilisateur NAS (ex: admin)')
    parser.add_argument('--password', default='', help='Mot de passe NAS')
    args = parser.parse_args()

    dry_run = not args.execute
    label = '[DRY-RUN]' if dry_run else '[EXECUTE]'
    folder = Path(args.folder)

    print(f"\n{'='*60}")
    print(f"  NAS Photo Renamer {label}")
    print(f"  Dossier : {folder}")
    print(f"{'='*60}\n")

    # Connexion au partage NAS si credentials fournis
    if args.user:
        share = '\\\\' + '\\'.join(str(folder).lstrip('\\').split('\\')[:2])
        password = args.password or getpass.getpass(f"Mot de passe NAS pour {args.user} : ")
        print(f"Connexion à {share} en tant que {args.user}...")
        cmd = ['net', 'use', share, f'/user:{args.user}', password, '/persistent:no']
        r = subprocess.run(cmd, capture_output=True, text=True, encoding='cp850')
        if r.returncode != 0:
            print(f"[ERREUR] Connexion NAS échouée : {r.stdout.strip() or r.stderr.strip()}")
            sys.exit(1)
        print("Connecté.\n")

    if not folder.exists():
        print(f"[ERREUR] Dossier inaccessible : {folder}")
        print("  Vérifie que le NAS est bien connecté dans l'explorateur Windows.")
        sys.exit(1)

    # Liste des images
    images = sorted([
        f for f in folder.iterdir()
        if f.is_file() and f.suffix.lower() in IMAGE_EXTENSIONS
    ])

    if args.limit:
        images = images[:args.limit]

    print(f"{len(images)} image(s) trouvée(s)\n")

    if not images:
        print("Aucune image à traiter.")
        return

    results = []
    errors  = []

    for i, img_path in enumerate(images, 1):
        ext = img_path.suffix.lower()
        mime_type = MIME_MAP.get(ext, 'image/jpeg')
        print(f"[{i:03d}/{len(images):03d}] {img_path.name} ...", end=' ', flush=True)

        try:
            image_bytes = img_path.read_bytes()
            analysis = analyze_with_gemini(image_bytes, mime_type)

            raw_name = analysis.get('suggested_filename', img_path.stem)
            new_stem = safe_filename(raw_name) or img_path.stem
            if args.prefix_number:
                new_stem = f"{i:03d}_{new_stem}"
            new_name = f"{new_stem}{ext}"
            quality  = analysis.get('quality', {}).get('overall', '?')
            city     = analysis.get('city') or '?'

            print(f"OK → {new_name}  [{city}, qualité {quality}/10]")
            results.append({
                'original': img_path.name,
                'new_name': new_name,
                'path': img_path,
                'quality': quality,
                'city': city,
                'description': analysis.get('scene_description', ''),
            })
        except Exception as e:
            print(f"ERREUR — {e}")
            errors.append({'file': img_path.name, 'error': str(e)})

        time.sleep(1.2)  # rate limit Gemini

    print(f"\n  Analysées : {len(results)} | Erreurs : {len(errors)}\n")

    if dry_run:
        print("Mode DRY-RUN — aucun fichier modifié.")
        print("Relance avec --execute pour appliquer les renommages.\n")
        return

    # ── Renommage ──────────────────────────────────────────────────────────────
    print("=== Renommage ===\n")
    renamed = 0
    skipped = 0

    for r in results:
        src = r['path']
        dst = src.parent / r['new_name']

        if dst.exists() and dst != src:
            # Éviter les collisions
            stem, ext = dst.stem, dst.suffix
            dst = src.parent / f"{stem}_2{ext}"

        try:
            src.rename(dst)
            print(f"  ✓ {r['original']} → {r['new_name']}")
            renamed += 1
        except Exception as e:
            print(f"  ✗ {r['original']} — {e}")
            skipped += 1

    # Rapport JSON
    report_path = Path(__file__).parent.parent.parent / 'data' / 'nas-renamer-report.json'
    report_path.parent.mkdir(exist_ok=True)
    report = {
        'folder': str(folder),
        'total': len(images),
        'renamed': renamed,
        'skipped': skipped,
        'errors': errors,
        'files': [{'from': r['original'], 'to': r['new_name'], 'city': r['city'], 'quality': r['quality']} for r in results]
    }
    report_path.write_text(json.dumps(report, indent=2, ensure_ascii=False), encoding='utf-8')
    print(f"\nRapport : {report_path}")
    print(f"Terminé — {renamed} renommé(s), {skipped} ignoré(s).")


if __name__ == '__main__':
    main()
