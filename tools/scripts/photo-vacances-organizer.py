#!/usr/bin/env python3
"""
Photo Vacances Organizer
========================
1. Liste les images dans le dossier Google Drive "01_A faire"
2. Analyse chacune avec Gemini Vision (gemini-2.5-flash)
3. Organise dans "02_Terminé/<ville>/" avec renommage
4. Crée un dossier "Meilleures photos" avec les 20 meilleures

Usage :
  python photo-vacances-organizer.py --dry-run    # voir sans modifier
  python photo-vacances-organizer.py --execute    # exécuter
  python photo-vacances-organizer.py --execute --limit 5   # tester sur 5 photos
"""

import argparse
import base64
import io
import json
import os
import sys
import time
import urllib.request
import urllib.error
from pathlib import Path

from dotenv import load_dotenv

sys.stdout.reconfigure(encoding='utf-8')
load_dotenv()

try:
    from google.auth.transport.requests import Request
    from google.oauth2.credentials import Credentials
    from google_auth_oauthlib.flow import InstalledAppFlow
    from googleapiclient.discovery import build
    from googleapiclient.http import MediaIoBaseDownload
except ImportError:
    print("Dépendances manquantes : pip install google-api-python-client google-auth-oauthlib")
    sys.exit(1)

# ── Config ────────────────────────────────────────────────────────────────────

SOURCE_FOLDER_ID = '1beNcu0IOEFgPksNZKKKI8hGgsANLyIaY'   # 01_A faire
DEST_FOLDER_ID   = '1Z_faJJyjNvwpK6eSTytbu0cKQ8Ijkflb'   # 02_Terminé
GEMINI_API_KEY   = os.getenv('GEMINI_API_KEY')
if not GEMINI_API_KEY:
    raise RuntimeError('GEMINI_API_KEY manquante — remplir .env (voir .env.example)')
GEMINI_URL       = 'https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent'
QUALITY_THRESHOLD = 6   # score overall >= 6 → photo conservée
TOP_N            = 20   # nombre de meilleures photos

SCOPES         = ['https://www.googleapis.com/auth/drive']
TOKEN_FILE     = Path(__file__).parent / 'token-photos-organizer.json'
CREDS_FILE     = Path(__file__).parent / 'credentials-gdrive-audit.json'

GEMINI_PROMPT = (
    'Analyse cette photo de vacances. '
    'Retourne UNIQUEMENT un objet JSON valide (sans bloc markdown ni texte avant/après) avec ces propriétés exactes : '
    '- city : string ou null (nom du lieu/ville reconnaissable) '
    '- city_confidence : "high", "medium" ou "low" '
    '- landmark : string ou null (monument ou lieu identifiable) '
    '- scene_description : string (description brève en français) '
    '- quality : objet avec sharpness, composition, lighting, visual_interest, overall (entiers 1-10) '
    '- is_duplicate_candidate : boolean '
    '- is_blurry : boolean '
    '- suggested_filename : string sans extension ni espace (ex: Paris_TourEiffel_Coucher_Soleil)'
)

# ── Auth Google Drive ─────────────────────────────────────────────────────────

def get_drive_service():
    creds = None

    if TOKEN_FILE.exists():
        creds = Credentials.from_authorized_user_file(str(TOKEN_FILE), SCOPES)

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            # Support env vars ou fichier credentials
            client_id     = os.environ.get('GOOGLE_WORKSPACE_CLI_CLIENT_ID')
            client_secret = os.environ.get('GOOGLE_WORKSPACE_CLI_CLIENT_SECRET')

            if client_id and client_secret:
                client_config = {
                    'installed': {
                        'client_id': client_id,
                        'client_secret': client_secret,
                        'redirect_uris': ['urn:ietf:wg:oauth:2.0:oob', 'http://localhost'],
                        'auth_uri': 'https://accounts.google.com/o/oauth2/auth',
                        'token_uri': 'https://oauth2.googleapis.com/token',
                    }
                }
                flow = InstalledAppFlow.from_client_config(client_config, SCOPES)
            elif CREDS_FILE.exists():
                flow = InstalledAppFlow.from_client_secrets_file(str(CREDS_FILE), SCOPES)
            else:
                print(f"[ERREUR] Credentials manquantes.")
                print(f"  Option 1 : variables d'env GOOGLE_WORKSPACE_CLI_CLIENT_ID + GOOGLE_WORKSPACE_CLI_CLIENT_SECRET")
                print(f"  Option 2 : fichier {CREDS_FILE}")
                sys.exit(1)

            creds = flow.run_local_server(port=0)

        TOKEN_FILE.write_text(creds.to_json(), encoding='utf-8')

    return build('drive', 'v3', credentials=creds)

# ── Google Drive helpers ──────────────────────────────────────────────────────

def list_images(service, folder_id):
    images = []
    page_token = None
    query = f"'{folder_id}' in parents and mimeType contains 'image/' and trashed = false"
    while True:
        resp = service.files().list(
            q=query,
            fields='nextPageToken, files(id, name, mimeType, size)',
            pageSize=100,
            pageToken=page_token
        ).execute()
        images.extend(resp.get('files', []))
        page_token = resp.get('nextPageToken')
        if not page_token:
            break
    return images


def download_image(service, file_id):
    request = service.files().get_media(fileId=file_id)
    buf = io.BytesIO()
    downloader = MediaIoBaseDownload(buf, request)
    done = False
    while not done:
        _, done = downloader.next_chunk()
    return buf.getvalue()


def get_or_create_folder(service, name, parent_id):
    # Check if already exists
    query = f"'{parent_id}' in parents and name = '{name}' and mimeType = 'application/vnd.google-apps.folder' and trashed = false"
    resp = service.files().list(q=query, fields='files(id, name)').execute()
    files = resp.get('files', [])
    if files:
        return files[0]['id']
    # Create
    meta = {
        'name': name,
        'mimeType': 'application/vnd.google-apps.folder',
        'parents': [parent_id]
    }
    folder = service.files().create(body=meta, fields='id').execute()
    return folder['id']


def move_file(service, file_id, dest_folder_id, new_name=None, dry_run=False):
    if dry_run:
        return
    # Get current parents
    file_meta = service.files().get(fileId=file_id, fields='parents').execute()
    current_parents = ','.join(file_meta.get('parents', []))
    kwargs = {
        'fileId': file_id,
        'addParents': dest_folder_id,
        'removeParents': current_parents,
        'fields': 'id, parents'
    }
    if new_name:
        kwargs['body'] = {'name': new_name}
        file_meta_update = service.files().update(**{
            'fileId': file_id,
            'addParents': dest_folder_id,
            'removeParents': current_parents,
            'body': {'name': new_name},
            'fields': 'id'
        }).execute()
    else:
        service.files().update(**kwargs).execute()


def copy_file(service, file_id, dest_folder_id, new_name=None, dry_run=False):
    if dry_run:
        return None
    body = {'parents': [dest_folder_id]}
    if new_name:
        body['name'] = new_name
    result = service.files().copy(fileId=file_id, body=body, fields='id').execute()
    return result['id']

# ── Gemini Vision ─────────────────────────────────────────────────────────────

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
        raise RuntimeError(f"Gemini HTTP {e.code}: {e.read().decode()[:300]}")

    text = resp['candidates'][0]['content']['parts'][0]['text']
    # Nettoyer les blocs markdown éventuels
    text = text.strip()
    if text.startswith('```'):
        text = text.split('\n', 1)[1]
        text = text.rsplit('```', 1)[0]
    return json.loads(text.strip())

# ── Main ──────────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(description='Organise les photos de vacances via Gemini Vision')
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument('--dry-run', action='store_true', default=True, help='Affiche les actions sans modifier (défaut)')
    mode.add_argument('--execute', action='store_true', help='Exécute les modifications sur Drive')
    parser.add_argument('--limit', type=int, default=0, help='Limiter à N photos (pour test)')
    args = parser.parse_args()

    dry_run = not args.execute
    label = '[DRY-RUN]' if dry_run else '[EXECUTE]'
    print(f"\n{'='*60}")
    print(f"  Photo Vacances Organizer {label}")
    print(f"{'='*60}\n")

    # Auth
    print("Connexion Google Drive...")
    service = get_drive_service()
    print("OK\n")

    # Liste des images
    print(f"Récupération des images dans 01_A faire...")
    images = list_images(service, SOURCE_FOLDER_ID)
    if args.limit:
        images = images[:args.limit]
    print(f"  {len(images)} image(s) trouvée(s)\n")

    if not images:
        print("Aucune image à traiter.")
        return

    # Analyse Gemini
    results = []
    errors = []

    for i, img in enumerate(images, 1):
        print(f"[{i}/{len(images)}] {img['name']} ({img.get('mimeType','?')})...", end=' ', flush=True)
        try:
            image_bytes = download_image(service, img['id'])
            analysis = analyze_with_gemini(image_bytes, img.get('mimeType', 'image/jpeg'))
            quality = analysis.get('quality', {})
            overall = quality.get('overall', 0)
            city = analysis.get('city') or 'Non_Classe'
            city = city.replace(' ', '_').replace('/', '_')
            print(f"OK — {city} (qualité {overall}/10)")
            results.append({
                'id': img['id'],
                'original_name': img['name'],
                'mime_type': img.get('mimeType', 'image/jpeg'),
                'city': city,
                'city_confidence': analysis.get('city_confidence', 'low'),
                'landmark': analysis.get('landmark'),
                'suggested_filename': analysis.get('suggested_filename', Path(img['name']).stem),
                'quality_overall': overall,
                'is_blurry': analysis.get('is_blurry', False),
                'is_duplicate': analysis.get('is_duplicate_candidate', False),
                'scene_description': analysis.get('scene_description', ''),
                'analysis': analysis
            })
        except Exception as e:
            print(f"ERREUR — {e}")
            errors.append({'file': img['name'], 'error': str(e)})
        # Pause pour éviter le rate limit Gemini
        time.sleep(1)

    print(f"\n  Analysées : {len(results)} | Erreurs : {len(errors)}\n")

    # Filtrage qualité
    kept    = [r for r in results if r['quality_overall'] >= QUALITY_THRESHOLD and not r['is_blurry']]
    excluded = [r for r in results if r['quality_overall'] < QUALITY_THRESHOLD or r['is_blurry']]
    print(f"  Conservées (score ≥ {QUALITY_THRESHOLD}) : {len(kept)}")
    print(f"  Exclues                               : {len(excluded)}\n")

    # Organisation par ville
    cities = {}
    for r in kept:
        cities.setdefault(r['city'], []).append(r)

    print("=== Plan d'organisation ===")
    for city, photos in sorted(cities.items()):
        print(f"  02_Terminé/{city}/ — {len(photos)} photo(s)")

    top20 = sorted(kept, key=lambda x: x['quality_overall'], reverse=True)[:TOP_N]
    print(f"  Meilleures photos/ — {len(top20)} photo(s)\n")

    if dry_run:
        print("Mode DRY-RUN : aucune modification effectuée.")
        print("Relance avec --execute pour appliquer.\n")
        return

    # ── Exécution ──────────────────────────────────────────────────────────────
    print("=== Exécution ===\n")
    city_folder_ids = {}

    # Créer les dossiers ville + déplacer les photos
    for city, photos in sorted(cities.items()):
        folder_id = get_or_create_folder(service, city, DEST_FOLDER_ID)
        city_folder_ids[city] = folder_id
        print(f"  Dossier : 02_Terminé/{city}/")

        for photo in photos:
            ext = Path(photo['original_name']).suffix or '.jpg'
            new_name = f"{photo['suggested_filename']}{ext}"
            try:
                move_file(service, photo['id'], folder_id, new_name=new_name)
                print(f"    ✓ {photo['original_name']} → {new_name}")
            except Exception as e:
                print(f"    ✗ {photo['original_name']} — {e}")
        time.sleep(0.3)

    # Dossier Meilleures photos (copies)
    best_folder_id = get_or_create_folder(service, 'Meilleures_photos', DEST_FOLDER_ID)
    print(f"\n  Dossier : 02_Terminé/Meilleures_photos/")
    for photo in top20:
        ext = Path(photo['original_name']).suffix or '.jpg'
        new_name = f"{photo['suggested_filename']}{ext}"
        try:
            copy_file(service, photo['id'], best_folder_id, new_name=new_name)
            print(f"    ✓ {photo['original_name']} (score {photo['quality_overall']})")
        except Exception as e:
            print(f"    ✗ {photo['original_name']} — {e}")
        time.sleep(0.2)

    # Rapport
    report = {
        'total_images': len(images),
        'analysed': len(results),
        'kept': len(kept),
        'excluded': len(excluded),
        'errors': errors,
        'cities': {city: len(photos) for city, photos in cities.items()},
        'top20': [{'name': r['original_name'], 'city': r['city'], 'score': r['quality_overall']} for r in top20]
    }
    report_path = Path('data') / 'photos-organizer-report.json'
    report_path.parent.mkdir(exist_ok=True)
    report_path.write_text(json.dumps(report, indent=2, ensure_ascii=False), encoding='utf-8')
    print(f"\nRapport sauvegardé : {report_path}")
    print(f"\nTerminé. {len(kept)} photo(s) organisée(s) dans {len(cities)} ville(s).")


if __name__ == '__main__':
    main()
