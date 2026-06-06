"""ElevenLabs TTS generation for Samaritain Security M1 narration.

Two modes:
  --test : generates 4 short MP3s (3 priority test phrases + scene 1 hook)
           to validate voice + technical-term pronunciation before the batch
  --batch: generates the 10 scenes of the M1 module

Voice = Michael KIHL clone (env override possible).
Output = content/formations/samaritain-security/production/audio-m1/

Usage:
  .venv/Scripts/python.exe tools/elevenlabs-tts-samaritain/generate.py --test
  .venv/Scripts/python.exe tools/elevenlabs-tts-samaritain/generate.py --batch
"""

from __future__ import annotations

import argparse
import os
import sys
from pathlib import Path

import requests
from dotenv import load_dotenv

PROJECT_ROOT = Path(__file__).resolve().parents[2]
load_dotenv(PROJECT_ROOT / ".env")

API_KEY = os.environ.get("ELEVENLABS_API_KEY")
VOICE_ID = (
    os.environ.get("ELEVENLABS_VOICE_ID_OVERRIDE")
    or os.environ.get("ELEVENLABS_VOICE_ID")
    or "r8Nv8JDxL3hOIt4MZtwT"  # clone Michael KIHL
)

OUT_DIR = PROJECT_ROOT / "content" / "formations" / "samaritain-security" / "production" / "audio-m1"

MODEL_ID = "eleven_multilingual_v2"
VOICE_SETTINGS = {
    "stability": 0.45,        # lowered from 0.55: less monotone, more natural
    "similarity_boost": 0.75, # 75 per script doc
    "style": 0.05,            # lowered from 0.15: conversational, not performative
    "use_speaker_boost": True,
}

TEST_PHRASES = [
    (
        "test-1-menus-wp",
        "Direction Extensions, Ajouter, Téléverser. Tu sélectionnes le fichier ZIP qu'on t'a envoyé.",
    ),
    (
        "test-2-wp-login",
        "L'ancienne adresse wp-login.php n'existe plus.",
    ),
    (
        "test-3-rescue",
        "Samaritain te fournit aussi une URL de secours, avec un paramètre samaritain rescue dans l'adresse.",
    ),
    (
        "test-4-scene1-hook",
        "Tu as un site WordPress et tu veux le sécuriser, mais tu n'as ni le temps "
        "ni l'envie de devenir expert en cybersécurité. Dans les quatre prochaines "
        "minutes, je te montre comment installer Samaritain Security et te mettre "
        "à l'abri, en deux minutes chrono.",
    ),
]

BATCH_SCENES = [
    (
        "M1-S01-hook",
        "Tu as un site WordPress et tu veux le sécuriser, mais tu n'as ni le temps "
        "ni l'envie de devenir expert en cybersécurité. Dans les quatre prochaines "
        "minutes, je te montre comment installer Samaritain Security et te mettre "
        "à l'abri, en deux minutes chrono.",
    ),
    (
        "M1-S02-desactiver",
        "Premier réflexe avant d'installer Samaritain Security : un seul plugin de "
        "sécurité actif à la fois. Si tu utilises Wordfence, SecuPress, iThemes "
        "Security ou Solid Security, désactive-le. Samaritain détecte les conflits, "
        "mais autant éviter le double filtrage qui peut alourdir ton site ou produire "
        "des comportements imprévus.",
    ),
    (
        "M1-S03-televerser",
        "Direction Extensions, Ajouter, Téléverser. Tu sélectionnes le fichier ZIP "
        "qu'on t'a envoyé. Tu cliques Installer maintenant. Et tu actives. Un nouveau "
        "menu Samaritain apparaît à gauche, dans ta barre latérale d'administration. "
        "C'est tout pour l'installation. Maintenant on passe à l'activation de la licence.",
    ),
    (
        "M1-S04-licence",
        "Tu vas dans Samaritain, Licence. Tu colles la clé qui t'a été envoyée par "
        "email lors de ton achat. Tu cliques sur Activer la licence... et voilà. "
        "Le récapitulatif apparaît avec ton nom, ton email, ta date d'expiration et "
        "même une clé de récupération qui est déjà configurée pour toi. C'est fait. "
        "Tu as maintenant accès à toutes les fonctionnalités du plugin.",
    ),
    (
        "M1-S05-nouvelle-url",
        "Maintenant, attention, c'est important. La première chose à savoir : "
        "Samaritain a déjà changé ton URL de connexion. Elle est affichée juste ici. "
        "Note-la dans ton gestionnaire de mots de passe maintenant. Vraiment "
        "maintenant. Parce qu'à partir de cet instant, l'ancienne adresse "
        "wp-login.php n'existe plus. Si tu fermes ce navigateur sans avoir noté "
        "la nouvelle URL, tu risques de te retrouver bloqué hors de ton propre site.",
    ),
    (
        "M1-S06-preuve-404",
        "Tu veux la preuve que ça marche ? Regarde. Je tape michaelkihl point fr "
        "slash wp-login.php en navigation privée. Et là, je tombe sur une "
        "page 404, comme si elle n'existait pas. Les milliers de robots qui scrutent "
        "Internet à la recherche de cette URL bien connue ne trouveront plus rien "
        "chez toi. C'est déjà une énorme partie du travail de fait.",
    ),
    (
        "M1-S07-nouvelle-url-ok",
        "Et avec ta nouvelle URL personnalisée, j'arrive bien sur l'écran de connexion "
        "normal. Tu vois ? Toujours en navigation privée. À retenir : note cette "
        "URL avant de fermer ton navigateur, et conserve-la dans ton gestionnaire "
        "de mots de passe.",
    ),
    (
        "M1-S08-url-secours",
        "Et juste au cas où tu perdrais ta nouvelle URL... Samaritain te fournit "
        "aussi une URL de secours, avec un paramètre samaritain rescue "
        "dans l'adresse. Tu la trouves sur cette page Licence. Note-la également "
        "dans ton gestionnaire de mots de passe. C'est ta bouée de sauvetage. En "
        "cas de problème, elle te permet de débloquer ton IP et de te reconnecter "
        "en 15 minutes.",
    ),
    (
        "M1-S09-dashboard",
        "Direction le tableau de bord. Premier coup d'œil : ton score de sécurité. "
        "Là moi je suis à 96 sur cent avec une note A, parce que je vais utiliser "
        "ce site pour cette formation et que j'ai déjà fait pas mal de choses. Toi, "
        "tu vas probablement démarrer entre 75 et 85, et c'est tout à fait normal. "
        "Ne t'inquiète pas. On va voir ensemble, dans les modules suivants, comment "
        "monter à un score A. Étape par étape.",
    ),
    (
        "M1-S10-outro",
        "Voilà pour le module 1. Tu as ton plugin installé, ta licence activée, "
        "ta nouvelle URL de connexion notée et ton URL de secours en sécurité. "
        "Dans le module 2, on rentre dans le tableau de bord pour décoder ton score. "
        "À tout de suite.",
    ),
]


def generate_audio(text: str, out_path: Path) -> int:
    """POST to ElevenLabs and write MP3 bytes to disk. Returns byte length."""
    url = f"https://api.elevenlabs.io/v1/text-to-speech/{VOICE_ID}"
    headers = {
        "xi-api-key": API_KEY,
        "Content-Type": "application/json",
        "Accept": "audio/mpeg",
    }
    body = {
        "text": text,
        "model_id": MODEL_ID,
        "voice_settings": VOICE_SETTINGS,
    }
    response = requests.post(url, json=body, headers=headers, timeout=180)
    if response.status_code != 200:
        raise RuntimeError(
            f"ElevenLabs HTTP {response.status_code}: {response.text[:300]}"
        )
    out_path.write_bytes(response.content)
    return len(response.content)


def run(items: list[tuple[str, str]]) -> int:
    if not API_KEY:
        print("ELEVENLABS_API_KEY missing in .env", file=sys.stderr)
        return 1
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    print(f"Voice ID: {VOICE_ID}")
    print(f"Output  : {OUT_DIR}")
    print(f"Items   : {len(items)}")
    print()
    total_bytes = 0
    total_chars = 0
    for name, text in items:
        chars = len(text)
        total_chars += chars
        out = OUT_DIR / f"{name}.mp3"
        print(f"  -> {name}.mp3  ({chars} chars)")
        size = generate_audio(text, out)
        total_bytes += size
        print(f"     {size:>7} bytes written")
    print()
    print(f"TOTAL: {len(items)} files, {total_chars} chars, {total_bytes} bytes")
    return 0


def main() -> int:
    p = argparse.ArgumentParser(description=__doc__)
    g = p.add_mutually_exclusive_group(required=True)
    g.add_argument("--test", action="store_true", help="3 priority phrases + scene 1")
    g.add_argument("--batch", action="store_true", help="full 10-scene M1 batch")
    g.add_argument(
        "--only",
        help="comma-separated scene names from BATCH_SCENES (e.g. M1-S07-nouvelle-url-ok,M1-S05-nouvelle-url)",
    )
    args = p.parse_args()
    if args.test:
        items = TEST_PHRASES
    elif args.batch:
        items = BATCH_SCENES
    else:
        wanted = {n.strip() for n in args.only.split(",") if n.strip()}
        items = [(n, t) for n, t in BATCH_SCENES if n in wanted]
        missing = wanted - {n for n, _ in items}
        if missing:
            print(f"Unknown scene name(s): {sorted(missing)}", file=sys.stderr)
            return 2
    return run(items)


if __name__ == "__main__":
    raise SystemExit(main())
