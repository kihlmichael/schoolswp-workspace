"""Smoke test narration : intro de la leçon 2.2 via ElevenLabs (voix clone Michaël).

Génère 2-2-intro.mp3 dans ce dossier pour valider le rendu voix avant le batch.
Lit ELEVENLABS_API_KEY dans le .env racine. Voix par défaut = clone Michaël KIHL.
"""

from __future__ import annotations

import os
from pathlib import Path

import requests
from dotenv import load_dotenv

ROOT = Path(__file__).resolve().parent
PROJECT_ROOT = Path(__file__).resolve().parents[4]
load_dotenv(PROJECT_ROOT / ".env")

API_KEY = os.environ["ELEVENLABS_API_KEY"]
VOICE_ID = (
    os.environ.get("ELEVENLABS_VOICE_ID_OVERRIDE")
    or os.environ.get("ELEVENLABS_VOICE_ID")
    or "r8Nv8JDxL3hOIt4MZtwT"  # clone Michaël KIHL
)

# Intro [INTRO - face camera] de wpsocialninja-masterclass-m2-l2.md, verbatim.
INTRO = (
    "Dans cette leçon, on attaque le feed le plus utile pour un créateur de "
    "contenu : le feed YouTube. L'idée est simple : afficher tes vidéos "
    "directement sur ton site WordPress, et les laisser se mettre à jour toutes "
    "seules quand tu publies.\n\n"
    "Mais avant d'afficher quoi que ce soit, il faut deux choses : connecter ton "
    "compte YouTube au plugin, puis choisir ce que tu veux montrer. On va voir les "
    "deux méthodes de connexion, puis les cinq types de feed disponibles. À la fin, "
    "tu sauras exactement lequel choisir selon ton besoin. C'est parti."
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
            "stability": 0.5,
            "similarity_boost": 0.8,
            "style": 0.2,
            "use_speaker_boost": True,
        },
    }
    response = requests.post(url, json=body, headers=headers, timeout=120)
    response.raise_for_status()
    out_path.write_bytes(response.content)
    print(f"OK saved {out_path.name} ({len(response.content)} bytes), voice={VOICE_ID}")


if __name__ == "__main__":
    out = ROOT / "2-2-intro.mp3"
    generate_audio(INTRO, out)
