import json
import os
import re
import sys
import tempfile
from datetime import datetime

import requests

# Importer les clients locaux
sys.path.append(os.path.dirname(__file__))
import blotato_client
import drive_client
import sheets_client
from run_pipeline import load_env_variables


def extract_drive_id(url):
    """
    Extracts the unique Google Drive File ID from a share URL.
    """
    m1 = re.search(r"\/file\/d\/([A-Za-z0-9_-]{10,})", url)
    if m1:
        return m1.group(1)

    m2 = re.search(r"[?&]id=([A-Za-z0-9_-]{10,})", url)
    if m2:
        return m2.group(1)

    raise ValueError(f"Impossible de détecter un ID de fichier Google Drive dans l'URL : {url}")


def send_discord_published_notification(webhook_url, title_fr, yt_url, privacy_status):
    """
    Sends a Discord notification confirming successful publication on YouTube.
    """
    print("[INFO] Envoi de la notification de publication sur Discord...")
    payload = {
        "content": (
            f"🎉 **[W209a] Vidéo publiée sur YouTube schoolsWP**\n\n"
            f"- **Titre** : {title_fr}\n"
            f"- **Confidentialité** : {privacy_status}\n"
            f"- **Source inspirante** : {yt_url}\n\n"
            f"👀 _Veuillez valider visuellement la vidéo sur la chaîne avant de la passer en Public._"
        )
    }

    response = requests.post(webhook_url, json=payload)
    if response.status_code not in (200, 204):
        print(f"[WARNING] Échec de la notification de publication Discord : {response.text}")
    else:
        print("[SUCCESS] Log de publication Discord délivré.")


def run_w209a_publisher():
    """
    Orchestration of the auto-publishing W209a pipeline.
    """
    # 1. Charger l'environnement
    load_env_variables()

    # 2. Charger les configurations
    script_dir = os.path.dirname(os.path.dirname(__file__))
    settings_path = os.path.join(script_dir, "config", "settings.json")
    with open(settings_path, "r", encoding="utf-8") as f:
        settings = json.load(f)

    spreadsheet_id = os.getenv("GOOGLE_SHEETS_SPREADSHEET_ID", settings.get("sheet_id"))
    sheet_tab = settings.get("sheet_tab", "Untitled")
    youtube_privacy = settings.get("youtube_privacy", "unlisted")

    blotato_key = os.getenv("BLOTATO_API_KEY")
    blotato_account = os.getenv("BLOTATO_ACCOUNT_ID")
    discord_webhook = os.getenv("DISCORD_WEBHOOK_SEO") or os.getenv("DISCORD_ROUTINES_WEBHOOK")

    # 3. Lire les lignes prêtes dans Sheets
    ready_rows = sheets_client.read_ready_rows(spreadsheet_id, sheet_tab)
    if not ready_rows:
        print("[INFO] Aucun brief n'est actuellement au statut 'ready' dans Sheets.")
        return 0

    published_count = 0

    for row in ready_rows:
        video_id = row.get("video_id")
        url_video = row.get("url_video", "").strip()
        title_fr = row.get("title_fr", "Titre Inconnu")
        description_fr = row.get("description_fr", "")
        yt_url = row.get("url", "")

        # Vérifier si l'URL de la vidéo produite est renseignée
        if not url_video:
            print(
                f"[INFO] Ligne {row.get('_row_number')} ({title_fr}) : en attente du dépôt de la vidéo finale par l'éditeur (url_video vide)."
            )
            continue

        print(f"\n[INFO] Traitement de la ligne {row.get('_row_number')} : '{title_fr}'...")

        temp_video_path = None
        try:
            # 4. Extraire l'ID Drive et télécharger la vidéo binaire
            drive_file_id = extract_drive_id(url_video)

            # Créer un fichier de stockage temporaire
            temp_dir = tempfile.gettempdir()
            temp_video_path = os.path.join(temp_dir, f"{video_id}_final.mp4")

            drive_client.download_file_from_drive(drive_file_id, temp_video_path)

            # 5. Publier la vidéo sur YouTube via Blotato
            blotato_client.run_blotato_publishing(
                file_path=temp_video_path,
                title=title_fr,
                description=description_fr,
                privacy_status=youtube_privacy,
                account_id=blotato_account,
                api_key=blotato_key,
            )

            # 6. Marquer comme "published" dans Sheets
            published_at_iso = datetime.utcnow().isoformat() + "Z"
            sheets_client.update_published_row(
                spreadsheet_id=spreadsheet_id, sheet_tab=sheet_tab, video_id=video_id, published_at_iso=published_at_iso
            )

            # 7. Notification Discord de succès de publication
            if discord_webhook and not discord_webhook.startswith("__"):
                send_discord_published_notification(discord_webhook, title_fr, yt_url, youtube_privacy)

            published_count += 1

        except Exception as e:
            print(f"[ERROR] Échec de la publication pour '{title_fr}' : {e}", file=sys.stderr)
        finally:
            # Nettoyage du binaire temporaire téléchargé
            if temp_video_path and os.path.exists(temp_video_path):
                try:
                    os.remove(temp_video_path)
                    print(f"[INFO] Nettoyage de la vidéo temporaire : {temp_video_path}")
                except Exception as ex:
                    print(f"[WARNING] Impossible de supprimer la vidéo temporaire : {ex}")

    print(f"\n[ORCHESTRATE COMPLETE] {published_count} vidéo(s) publiée(s) lors de cette routine.")
    return published_count


if __name__ == "__main__":
    try:
        run_w209a_publisher()
    except Exception as e:
        print(f"[CRITICAL ERROR] Échec de la routine de publication : {e}", file=sys.stderr)
        sys.exit(1)
