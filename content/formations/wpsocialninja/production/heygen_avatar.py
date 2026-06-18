"""Client HeyGen : produit une vidéo talking-head depuis un audio (lipsync).

Pipeline : upload mp3/wav vers HeyGen asset -> /v2/video/generate (avatar digital
twin + voice audio) -> poll /v1/video_status.get -> download MP4.

Auth : X-Api-Key = HEYGEN_API_KEY (lu dans le .env racine). API publique v2/v1.
Pas de TTS HeyGen, pas de voix clone HeyGen : l'audio (ElevenLabs) pilote le lipsync.

Usage :
  python heygen_avatar.py --list                 # liste les avatars du compte
  python heygen_avatar.py --audio 2-2-intro.mp3  # smoke test (défaut)
  python heygen_avatar.py --audio x.mp3 --test   # mode test (watermark, 0 crédit)
"""

from __future__ import annotations

import argparse
import json
import os
import re
import time
from pathlib import Path

import requests
from dotenv import load_dotenv

ROOT = Path(__file__).resolve().parent
PROJECT_ROOT = Path(__file__).resolve().parents[4]
load_dotenv(PROJECT_ROOT / ".env")

API = "https://api.heygen.com"
UPLOAD = "https://upload.heygen.com/v1/asset"


def _api_key() -> str:
    key = os.environ.get("HEYGEN_API_KEY", "")
    if not key:
        raise SystemExit("ERR: HEYGEN_API_KEY manquant dans le .env racine")
    return key


def _headers(content_type: str | None = None) -> dict[str, str]:
    h = {"X-Api-Key": _api_key()}
    if content_type:
        h["Content-Type"] = content_type
    return h


def resolve_avatar_id() -> str:
    """Digital twin look id : env > parse AVATAR-MICHAEL.md > constante connue."""
    env_id = os.environ.get("HEYGEN_AVATAR_ID")
    if env_id:
        return env_id
    avatar_md = PROJECT_ROOT / "AVATAR-MICHAEL.md"
    if avatar_md.exists():
        text = avatar_md.read_text(encoding="utf-8")
        for line in text.splitlines():
            if "digital_twin" in line and "|" in line:
                m = re.search(r"`([0-9a-f]{32})`", line)
                if m:
                    return m.group(1)
    return "bcc2e2951dff40ef8b1c860f691f02fa"


def list_avatars() -> None:
    r = requests.get(f"{API}/v2/avatars", headers=_headers(), timeout=60)
    r.raise_for_status()
    data = r.json().get("data", {})
    avatars = data.get("avatars", []) or []
    print(f"avatars: {len(avatars)}")
    target = resolve_avatar_id()
    for a in avatars:
        aid = a.get("avatar_id") or a.get("id")
        name = a.get("avatar_name") or a.get("name") or "?"
        flag = "  <-- digital twin (résolu)" if aid == target else ""
        print(f"  - {aid}  {name}{flag}")
    print(f"\navatar_id ciblé pour la génération : {target}")


def upload_audio(path: Path) -> str:
    ext = path.suffix.lower()
    content_type = "audio/wav" if ext == ".wav" else "audio/mpeg"
    with path.open("rb") as f:
        r = requests.post(UPLOAD, headers=_headers(content_type), data=f, timeout=120)
    r.raise_for_status()
    payload = r.json()
    if payload.get("code") != 100:
        raise SystemExit(f"ERR upload asset: {payload.get('message') or payload}")
    url = payload["data"]["url"]
    print(f"audio uploadé -> {url}")
    return url


def generate(avatar_id: str, audio_url: str, *, width: int, height: int,
             title: str, test: bool) -> str:
    config = {
        "test": test,
        "title": title,
        "dimension": {"width": width, "height": height},
        "video_inputs": [
            {
                "character": {
                    "type": "avatar",
                    "avatar_id": avatar_id,
                    "avatar_style": "normal",
                },
                "voice": {"type": "audio", "audio_url": audio_url},
            }
        ],
    }
    r = requests.post(
        f"{API}/v2/video/generate",
        headers=_headers("application/json"),
        json=config,
        timeout=120,
    )
    payload = r.json()
    if payload.get("error"):
        raise SystemExit(f"ERR generate: {payload['error']}")
    video_id = payload["data"]["video_id"]
    print(f"génération lancée, video_id={video_id} (test={test})")
    return video_id


def wait_for_video(video_id: str, *, max_wait_s: int = 1200, poll_s: int = 15) -> str:
    start = time.time()
    while time.time() - start < max_wait_s:
        r = requests.get(
            f"{API}/v1/video_status.get",
            params={"video_id": video_id},
            headers=_headers(),
            timeout=60,
        )
        data = r.json().get("data", {})
        status = data.get("status")
        elapsed = int(time.time() - start)
        print(f"  [{elapsed}s] {status}")
        if status == "completed":
            return data["video_url"]
        if status == "failed":
            raise SystemExit(f"ERR video failed: {data.get('error')}")
        time.sleep(poll_s)
    raise SystemExit("ERR timeout génération vidéo")


def download(url: str, out: Path, *, max_retries: int = 5) -> None:
    delay = 2.0
    for attempt in range(max_retries):
        try:
            r = requests.get(url, stream=True, timeout=120)
            r.raise_for_status()
            with out.open("wb") as f:
                for chunk in r.iter_content(chunk_size=8192):
                    f.write(chunk)
            print(f"OK MP4 -> {out} ({out.stat().st_size} bytes)")
            return
        except Exception as e:  # noqa: BLE001
            if attempt == max_retries - 1:
                raise
            print(f"  download retry {attempt + 1} dans {delay}s ({e})")
            time.sleep(delay)
            delay *= 2


def main() -> None:
    parser = argparse.ArgumentParser(description="HeyGen lipsync depuis un audio")
    parser.add_argument("--list", action="store_true", help="liste les avatars")
    parser.add_argument("--poll-id", default=None, help="poll un video_id existant puis download")
    parser.add_argument("--audio", default="2-2-intro.mp3", help="fichier audio")
    parser.add_argument("--avatar-id", default=None, help="override avatar_id")
    parser.add_argument("--out", default=None, help="chemin MP4 de sortie")
    parser.add_argument("--width", type=int, default=1920)
    parser.add_argument("--height", type=int, default=1080)
    parser.add_argument("--title", default="WPSN masterclass - smoke 2.2 intro")
    parser.add_argument("--test", action="store_true", help="mode test (watermark)")
    args = parser.parse_args()

    if args.list:
        list_avatars()
        return

    if args.poll_id:
        if args.out:
            out = Path(args.out) if Path(args.out).is_absolute() else (ROOT / args.out)
        else:
            out = ROOT / f"{args.poll_id}.mp4"
        video_url = wait_for_video(args.poll_id)
        download(video_url, out)
        return

    audio_path = (ROOT / args.audio) if not Path(args.audio).is_absolute() else Path(args.audio)
    if not audio_path.exists():
        raise SystemExit(f"ERR audio introuvable : {audio_path}")

    avatar_id = args.avatar_id or resolve_avatar_id()
    out = Path(args.out) if args.out else (ROOT / (audio_path.stem + ".mp4"))

    print(f"avatar_id={avatar_id}")
    audio_url = upload_audio(audio_path)
    video_id = generate(
        avatar_id, audio_url,
        width=args.width, height=args.height, title=args.title, test=args.test,
    )
    print(json.dumps({"video_id": video_id, "avatar_id": avatar_id}, ensure_ascii=False))
    video_url = wait_for_video(video_id)
    download(video_url, out)


if __name__ == "__main__":
    main()
