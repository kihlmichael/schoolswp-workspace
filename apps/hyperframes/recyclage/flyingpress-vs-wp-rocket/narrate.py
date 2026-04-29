"""Génère la narration FR de la vidéo FlyingPress vs WP Rocket via ElevenLabs.

Texte calibré pour ~40s sur la voix configurée dans .env (multilingual_v2).
Output : narration.mp3 dans le dossier de l'article.

Mux ensuite avec ffmpeg :
  ffmpeg -y -i renders/recyclage-fp-vs-wpr-16x9-1920x1080.mp4 \\
         -i .../narration.mp3 -c:v copy -c:a aac -b:a 192k -shortest \\
         renders/recyclage-fp-vs-wpr-16x9-narrated.mp4
"""

from __future__ import annotations

import os
from pathlib import Path

import requests
from dotenv import load_dotenv

ROOT = Path(__file__).parent
PROJECT_ROOT = ROOT.parent.parent.parent.parent
load_dotenv(PROJECT_ROOT / ".env")

API_KEY = os.environ["ELEVENLABS_API_KEY"]
# Voix par défaut Charlie (premade, "Deep, Confident, Energetic"), accessible en
# tier free. La voix custom de l'env (Michaël KIHL clone) requiert un plan payant.
# Override possible via .env ou export ELEVENLABS_VOICE_ID_OVERRIDE.
VOICE_ID = os.environ.get(
    "ELEVENLABS_VOICE_ID_OVERRIDE",
    "IKne3meq5aSn9XLyUdCD",  # Charlie
)

# Texte calibré scène par scène, pauses naturelles via points pour matcher
# le rythme de la timeline GSAP (40s total).
SCRIPT = (
    "FlyingPress contre WP Rocket. Lequel booste vraiment ton WordPress ? "
    "Sur PageSpeed Mobile, FlyingPress décroche 96. WP Rocket, 92. "
    "Avantage FlyingPress. "
    "Sur le même site, le LCP passe de 3,1 secondes à 1,5. "
    "Une chute de 52 pour cent. "
    "Côté tarif : 42 dollars par an chez FlyingPress, 59 chez WP Rocket. "
    "Soit 17 dollars d'écart. "
    "C'est pour ça que la stack officielle schoolsWP, c'est FlyingPress. "
    "WP Rocket reste solide pour qui veut la doc 100 pour cent française. "
    "Comparatif complet sur schoolswp.com slash comparaison flyingpress wp rocket."
)


def generate_audio(text: str, out_path: Path) -> None:
    url = f"https://api.elevenlabs.io/v1/text-to-speech/{VOICE_ID}"
    headers = {
        "xi-api-key": API_KEY,
        "Content-Type": "application/json",
        "Accept": "audio/mpeg",
    }
    body = {
        "text": text,
        "model_id": "eleven_multilingual_v2",
        "voice_settings": {
            "stability": 0.55,
            "similarity_boost": 0.75,
            "style": 0.25,
            "use_speaker_boost": True,
        },
    }
    response = requests.post(url, json=body, headers=headers, timeout=120)
    response.raise_for_status()
    out_path.write_bytes(response.content)
    print(f"OK saved {out_path.name} ({len(response.content)} bytes)")


if __name__ == "__main__":
    out = ROOT / "narration.mp3"
    generate_audio(SCRIPT, out)
