import os
import sys
import tempfile

import requests


def download_youtube_audio(yt_url, output_dir=None):
    """
    Downloads audio from a YouTube video URL using yt-dlp.
    Returns the absolute path of the downloaded audio file (MP3).
    """
    try:
        import yt_dlp
    except ImportError:
        print("[WARNING] yt_dlp non installé, tentative d'installation via subprocess...")
        import subprocess

        subprocess.check_call([sys.executable, "-m", "pip", "install", "yt-dlp"])
        import yt_dlp

    if not output_dir:
        output_dir = tempfile.gettempdir()

    # On utilise un nom basé sur un pattern temporaire propre
    output_template = os.path.join(output_dir, "%(id)s.%(ext)s")

    ydl_opts = {
        "format": "bestaudio/best",
        "postprocessors": [
            {
                "key": "FFmpegExtractAudio",
                "preferredcodec": "mp3",
                "preferredquality": "64",  # Qualité légère pour économiser de la bande passante
            }
        ],
        "outtmpl": output_template,
        "quiet": True,
        "no_warnings": True,
    }

    print(f"[INFO] Téléchargement de la piste audio de la vidéo source : {yt_url}")
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(yt_url, download=True)
        video_id = info.get("id")
        ext = "mp3"  # Grâce au FFmpegExtractAudio postprocessor
        audio_path = os.path.join(output_dir, f"{video_id}.{ext}")

        if os.path.exists(audio_path):
            print(f"[SUCCESS] Piste audio téléchargée localement : {audio_path}")
            return audio_path
        else:
            raise FileNotFoundError(f"Impossible de localiser le fichier audio téléchargé à : {audio_path}")


def transcribe_audio_elevenlabs(audio_path, api_key, model_id="scribe_v2", language_code="fra"):
    """
    Sends the local audio file to ElevenLabs Speech-to-Text API.
    Returns the full transcription text.
    """
    print(f"[INFO] Envoi de l'audio à l'API ElevenLabs Speech-to-Text (Model: {model_id}, Lang: {language_code})...")
    url = "https://api.elevenlabs.io/v1/speech-to-text"
    headers = {"xi-api-key": api_key}

    with open(audio_path, "rb") as f:
        files = {"file": f, "model_id": (None, model_id), "language_code": (None, language_code)}
        response = requests.post(url, headers=headers, files=files)

    if response.status_code != 200:
        raise requests.HTTPError(f"ElevenLabs API Error {response.status_code}: {response.text}")

    data = response.json()
    transcript_text = data.get("text", "").strip()
    word_count = len(transcript_text.split())

    print(f"[SUCCESS] Transcription réussie ! ({word_count} mots)")
    return {"clean_transcript": transcript_text, "word_count": word_count}


def run_transcription_pipeline(yt_url, api_key, model_id="scribe_v2", language_code="fra"):
    """
    Downloads and transcribes the YouTube video.
    """
    audio_path = None
    try:
        audio_path = download_youtube_audio(yt_url)
        result = transcribe_audio_elevenlabs(audio_path, api_key, model_id, language_code)
        return result
    finally:
        # Nettoyage du fichier audio temporaire
        if audio_path and os.path.exists(audio_path):
            try:
                os.remove(audio_path)
                print(f"[INFO] Nettoyage du fichier temporaire effectué : {audio_path}")
            except Exception as e:
                print(f"[WARNING] Impossible de supprimer le fichier temporaire : {e}")


if __name__ == "__main__":
    # Test unitaire rapide
    if len(sys.argv) < 3:
        print("Usage: python transcribe_elevenlabs.py <YT_URL> <ELEVENLABS_API_KEY>")
        sys.exit(1)

    yt_url = sys.argv[1]
    api_key = sys.argv[2]

    try:
        res = run_transcription_pipeline(yt_url, api_key)
        print("\n=== TRANSCRIPTION FINALE ===")
        print(res["clean_transcript"][:500] + "...")
    except Exception as e:
        print(f"[ERROR] Échec de la transcription : {e}", file=sys.stderr)
        sys.exit(1)
