import json
import os
import re
import sys
from datetime import datetime

import requests

# Importer les clients locaux
sys.path.append(os.path.dirname(__file__))
import sheets_client
from transcribe_elevenlabs import run_transcription_pipeline


def load_env_variables():
    """
    Loads environment variables from local .env files.
    Skips any placeholder values starting with '__'.
    """
    # 1. Tente de lire le .env local au niveau du script
    script_dir = os.path.dirname(os.path.dirname(__file__))
    env_paths = [
        os.path.join(script_dir, ".env"),
        os.path.join(os.getcwd(), ".env"),  # Racine du projet
    ]

    for env_path in env_paths:
        if os.path.exists(env_path):
            with open(env_path, "r", encoding="utf-8") as f:
                for line in f:
                    line = line.strip()
                    if line and not line.startswith("#") and "=" in line:
                        k, v = line.split("=", 1)
                        k = k.strip()
                        v = v.strip()
                        # Ignore les placeholders
                        if v.startswith("__"):
                            continue
                        os.environ[k] = v


def get_video_id(url):
    """
    Extracts the unique YouTube Video ID from any valid URL format.
    """
    youtube_regex = r"(?:v=|youtu\.be\/|youtube\.com\/shorts\/)([A-Za-z0-9_-]{11})"
    match = re.search(youtube_regex, url)
    if not match:
        raise ValueError(f"URL YouTube invalide ou motif non détecté : {url}")
    return match.group(1)


def read_prompt_template(filename):
    """
    Reads prompt text template from prompts directory.
    """
    script_dir = os.path.dirname(os.path.dirname(__file__))
    prompt_path = os.path.join(script_dir, "prompts", filename)
    with open(prompt_path, "r", encoding="utf-8") as f:
        return f.read()


def call_ollama_completion(prompt, system_instruction=None):
    """
    Calls local Ollama server using OpenAI compatible endpoint.
    """
    ollama_url = os.getenv("OLLAMA_BASE_URL", "http://127.0.0.1:11434/v1").rstrip("/") + "/chat/completions"
    model_writer = os.getenv("MODEL_WRITER", "ollama:qwen2.5:7b")
    model_name = model_writer.replace("ollama:", "") if model_writer.startswith("ollama:") else model_writer

    print(f"[INFO] Appel de secours local Ollama (Modèle: {model_name})...")

    messages = []
    if system_instruction:
        messages.append({"role": "system", "content": system_instruction})
    messages.append({"role": "user", "content": prompt})

    payload = {"model": model_name, "messages": messages, "temperature": 0.5}

    try:
        response = requests.post(ollama_url, json=payload, timeout=300)
        if response.status_code == 200:
            data = response.json()
            return data["choices"][0]["message"]["content"].strip()
        else:
            raise RuntimeError(f"Ollama returned HTTP {response.status_code}: {response.text}")
    except Exception as e:
        raise RuntimeError(f"Échec de l'appel local Ollama : {e}")


def generate_script_brief(transcript, user_brief, output_lang, api_key):
    """
    Calls Claude 3.5 Sonnet to generate the 100% original schoolsWP video script.
    Falls back to local Ollama if Anthropic API fails (e.g. out of credits).
    """
    print("[INFO] Génération du script de brief original via Claude 3.5 Sonnet...")

    template = read_prompt_template("write_brief_sonnet.txt")
    prompt = template.format(transcript=transcript, user_brief=user_brief, output_lang=output_lang)

    try:
        url = "https://api.anthropic.com/v1/messages"
        headers = {"x-api-key": api_key, "anthropic-version": "2023-06-01", "content-type": "application/json"}

        payload = {
            "model": "claude-3-5-sonnet-20241022",
            "max_tokens": 2500,
            "temperature": 0.6,
            "messages": [{"role": "user", "content": prompt}],
        }

        response = requests.post(url, headers=headers, json=payload)
        if response.status_code != 200:
            raise requests.HTTPError(f"Anthropic API Error (Sonnet): {response.status_code} - {response.text}")

        data = response.json()
        script_content = data["content"][0]["text"].strip()
        print("[SUCCESS] Script de brief rédigé avec succès via Claude 3.5 Sonnet.")
        return script_content

    except Exception as e:
        print(f"[WARNING] Échec de l'appel Anthropic Sonnet ({e}). Bascule sur la solution locale Ollama...")
        try:
            script_content = call_ollama_completion(prompt)
            print("[SUCCESS] Script de brief rédigé avec succès via Ollama.")
            return script_content
        except Exception as ollama_err:
            print(f"[ERROR] Échec de la solution de secours Ollama : {ollama_err}")
            raise e


def generate_seo_metadata(script_content, api_key):
    """
    Calls Claude 3.5 Haiku to extract and format YouTube SEO metadata in strict JSON.
    Falls back to local Ollama if Anthropic API fails.
    """
    print("[INFO] Génération des métadonnées SEO via Claude 3.5 Haiku...")

    template = read_prompt_template("write_seo_haiku.txt")
    prompt = template.format(script=script_content)

    try:
        url = "https://api.anthropic.com/v1/messages"
        headers = {"x-api-key": api_key, "anthropic-version": "2023-06-01", "content-type": "application/json"}

        payload = {
            "model": "claude-3-5-haiku-20241022",
            "max_tokens": 800,
            "temperature": 0.3,
            "messages": [{"role": "user", "content": prompt}],
        }

        response = requests.post(url, headers=headers, json=payload)
        if response.status_code != 200:
            raise requests.HTTPError(f"Anthropic API Error (Haiku): {response.status_code} - {response.text}")

        data = response.json()
        raw_json_str = data["content"][0]["text"].strip()

    except Exception as e:
        print(f"[WARNING] Échec de l'appel Anthropic Haiku ({e}). Bascule sur la solution locale Ollama...")
        try:
            raw_json_str = call_ollama_completion(
                prompt,
                system_instruction="Tu dois répondre uniquement en format JSON brut valide sans explications ni markdown.",
            )
        except Exception as ollama_err:
            print(f"[ERROR] Échec de la solution de secours Ollama : {ollama_err}")
            raise e

    # Nettoyage d'éventuelles balises markdown json
    if raw_json_str.startswith("```json"):
        raw_json_str = raw_json_str[7:]
    if raw_json_str.startswith("```"):
        raw_json_str = raw_json_str[3:]
    if raw_json_str.endswith("```"):
        raw_json_str = raw_json_str[:-3]
    raw_json_str = raw_json_str.strip()

    try:
        seo_data = json.loads(raw_json_str)
        print("[SUCCESS] Métadonnées SEO générées et décodées avec succès.")
        return seo_data
    except json.JSONDecodeError as e:
        print(f"[ERROR] Impossible de parser le JSON brut retourné par le LLM : {raw_json_str}")
        raise e


def send_telegram_notification(token, chat_id, title_fr, yt_url):
    """
    Sends a success notification to the user back on Telegram.
    """
    print(f"[INFO] Envoi de la notification de succès sur Telegram (Chat ID: {chat_id})...")
    url = f"https://api.telegram.org/bot{token}/sendMessage"

    text = (
        f"✅ *Brief schoolsWP prêt.*\n\n"
        f"*Titre proposé :* {title_fr}\n"
        f"*Vidéo source :* {yt_url}\n"
        f"*Statut Sheet :* ready\n\n"
        f"🚀 *Prochaine étape :* produis ta vidéo HeyGen + ElevenLabs et colle l'URL Google Drive "
        f"partagée dans la colonne `url_video` du Sheet. Le robot publiera automatiquement."
    )

    payload = {"chat_id": chat_id, "text": text, "parse_mode": "Markdown"}

    response = requests.post(url, json=payload)
    if response.status_code != 200:
        print(f"[WARNING] Échec de la notification Telegram : {response.text}")
    else:
        print("[SUCCESS] Notification Telegram délivrée.")


def send_discord_notification(webhook_url, title_fr, yt_url):
    """
    Sends a log notification to the Discord channel webhook.
    """
    print("[INFO] Envoi de la notification de log sur Discord...")
    payload = {
        "content": (
            f"**[W209] Brief YouTube schoolsWP généré**\n\n"
            f"- **Titre** : {title_fr}\n"
            f"- **Source** : {yt_url}\n"
            f"- **Statut** : ready (en attente vidéo HeyGen)"
        )
    }

    response = requests.post(webhook_url, json=payload)
    if response.status_code not in (200, 204):
        print(f"[WARNING] Échec de la notification Discord : {response.text}")
    else:
        print("[SUCCESS] Log Discord délivré.")


def run_w209_pipeline(telegram_message_text, chat_id):
    """
    Orchestration of the W209 brief & SEO pipeline.
    """
    # 1. Charger l'environnement
    load_env_variables()

    # 2. Configurer les paramètres globaux
    script_dir = os.path.dirname(os.path.dirname(__file__))
    settings_path = os.path.join(script_dir, "config", "settings.json")
    with open(settings_path, "r", encoding="utf-8") as f:
        settings = json.load(f)

    output_lang = settings.get("output_lang", "francais")
    spreadsheet_id = os.getenv("GOOGLE_SHEETS_SPREADSHEET_ID", settings.get("sheet_id"))
    sheet_tab = settings.get("sheet_tab", "Untitled")
    scribe_model = settings.get("scribe_model", "scribe_v2")

    # Récupérer les clés d'API
    elevenlabs_key = os.getenv("ELEVENLABS_API_KEY")
    anthropic_key = os.getenv("ANTHROPIC_API_KEY")
    telegram_token = os.getenv("TELEGRAM_BOT_TOKEN") or os.getenv("NEMOCLAW_TELEGRAM_BOT_TOKEN")
    discord_webhook = os.getenv("DISCORD_WEBHOOK_SEO") or os.getenv("DISCORD_ROUTINES_WEBHOOK")

    # Validation basique
    if not elevenlabs_key or elevenlabs_key.startswith("__"):
        raise ValueError("Clé ELEVENLABS_API_KEY non renseignée dans le .env.")
    if not anthropic_key or anthropic_key.startswith("__"):
        raise ValueError("Clé ANTHROPIC_API_KEY non renseignée dans le .env.")
    if not telegram_token or telegram_token.startswith("__"):
        raise ValueError("Clé TELEGRAM_BOT_TOKEN (ou NEMOCLAW_TELEGRAM_BOT_TOKEN) non renseignée dans le .env.")

    # 3. Découper le message Telegram
    lines = [line.strip() for line in telegram_message_text.strip().split("\n") if line.strip()]
    if not lines:
        raise ValueError("Message vide. Format attendu : ligne 1 = URL, ligne 2+ = brief.")

    yt_url = lines[0]
    user_brief = " ".join(lines[1:]) if len(lines) > 1 else "(aucun brief fourni)"

    # 4. Extraire l'ID Vidéo
    video_id = get_video_id(yt_url)

    # 5. Ingestion initiale Google Sheets (status: received)
    # Vérifie d'abord si la vidéo existe déjà pour éviter les doublons
    try:
        all_rows = sheets_client.get_all_rows(spreadsheet_id, sheet_tab)
        video_exists = False
        for idx, r in enumerate(all_rows):
            if len(r) > 3 and r[3] == video_id:
                video_exists = True
                print(
                    f"[INFO] La vidéo {video_id} est déjà présente dans la feuille à la ligne {idx + 1}. Mise à jour directe prévue."
                )
                break
    except Exception as e:
        print(f"[WARNING] Impossible de vérifier les doublons dans Sheets ({e}), poursuite standard...")
        video_exists = False

    if not video_exists:
        date_iso = datetime.utcnow().isoformat() + "Z"
        sheets_client.append_received_row(
            spreadsheet_id=spreadsheet_id,
            sheet_tab=sheet_tab,
            date_iso=date_iso,
            url=yt_url,
            brief_user=user_brief,
            video_id=video_id,
            language=output_lang,
        )

    # 6. Transcription de l'audio de la vidéo via ElevenLabs
    trans_res = run_transcription_pipeline(
        yt_url=yt_url, api_key=elevenlabs_key, model_id=scribe_model, language_code="fra"
    )
    transcript_text = trans_res["clean_transcript"]

    # 7. Rédaction du Script de Brief écolesWP (Claude Sonnet)
    brief_schoolswp = generate_script_brief(
        transcript=transcript_text, user_brief=user_brief, output_lang=output_lang, api_key=anthropic_key
    )

    # 8. Rédaction des Métadonnées YouTube SEO (Claude Haiku)
    seo_data = generate_seo_metadata(script_content=brief_schoolswp, api_key=anthropic_key)

    title_fr = seo_data["title"]
    description_fr = seo_data["description"]
    tags_fr = ", ".join(seo_data["tags"])

    # 9. Ingestion finale Google Sheets (status: ready)
    sheets_client.update_ready_row(
        spreadsheet_id=spreadsheet_id,
        sheet_tab=sheet_tab,
        video_id=video_id,
        brief_schoolswp=brief_schoolswp,
        title_fr=title_fr,
        description_fr=description_fr,
        tags_fr=tags_fr,
    )

    # 10. Notifications (Telegram & Discord)
    send_telegram_notification(telegram_token, chat_id, title_fr, yt_url)
    if discord_webhook and not discord_webhook.startswith("__"):
        send_discord_notification(discord_webhook, title_fr, yt_url)

    print("[PIPELINE COMPLETE] W209 a été exécuté avec succès.")
    return {"video_id": video_id, "title": title_fr, "status": "ready"}


if __name__ == "__main__":
    # Test d'orchestration rapide en simulation locale
    if len(sys.argv) < 3:
        print("Usage: python run_pipeline.py <MESSAGE_TEXT> <CHAT_ID>")
        sys.exit(1)

    msg = sys.argv[1]
    cid = sys.argv[2]

    try:
        run_w209_pipeline(msg, cid)
    except Exception as e:
        print(f"[CRITICAL ERROR] Échec de l'exécution du pipeline : {e}", file=sys.stderr)
        sys.exit(1)
