"""Generate the Samaritain Security featured image via Gemini Imagen 4 / 2.5 Flash Image.

Reads GEMINI_API_KEY from .claude/settings.local.json (avoid putting it in env).
Tries several candidate models, returns the first one that works.
Saves the PNG locally for upload via Novamira.
"""

import base64
import json
import sys
import urllib.error
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SETTINGS = ROOT / ".claude" / "settings.local.json"
OUT = Path(__file__).resolve().parent / "samaritain-featured.png"

PROMPT = (
    "Modern dark banner for a WordPress security training course. "
    "Dark navy and charcoal gradient background. "
    "Vibrant electric green accent color used sparingly. "
    "Centered minimalist shield icon with a checkmark inside, drawn in clean white outline. "
    "Bold modern sans-serif typography reading 'Samaritain Security' as the main headline. "
    "Subtitle below reading 'Securiser ton WordPress en 1 clic'. "
    "Premium tech aesthetic, lots of negative space, no UI elements, no buttons, "
    "no faces, no people. 16:9 aspect ratio. "
    "Suitable as Open Graph featured image for a course landing page."
)

# Candidates ordered from most likely to least likely to be available
CANDIDATES = [
    "gemini-2.5-flash-image",
    "gemini-2.0-flash-exp-image-generation",
    "imagen-4.0-generate-001",
    "imagen-3.0-generate-002",
]


def load_key() -> str:
    data = json.loads(SETTINGS.read_text(encoding="utf-8"))
    key = data.get("env", {}).get("GEMINI_API_KEY")
    if not key:
        raise SystemExit("GEMINI_API_KEY not found in settings.local.json")
    return key


def try_generate_content(model: str, key: str) -> bytes | None:
    """generateContent flow (gemini-2.5-flash-image, gemini-2.0-flash-exp)."""
    url = f"https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent?key={key}"
    body = {
        "contents": [{"parts": [{"text": PROMPT}]}],
        "generationConfig": {"responseModalities": ["IMAGE"]},
    }
    req = urllib.request.Request(
        url,
        data=json.dumps(body).encode("utf-8"),
        headers={"Content-Type": "application/json"},
        method="POST",
    )
    try:
        with urllib.request.urlopen(req, timeout=60) as resp:
            payload = json.loads(resp.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        err_body = e.read().decode("utf-8", errors="ignore")
        print(f"  {model}: HTTP {e.code} - {err_body[:300]}", file=sys.stderr)
        return None
    except Exception as e:
        print(f"  {model}: {e}", file=sys.stderr)
        return None

    try:
        parts = payload["candidates"][0]["content"]["parts"]
        for p in parts:
            if "inlineData" in p:
                return base64.b64decode(p["inlineData"]["data"])
    except (KeyError, IndexError, TypeError):
        pass
    print(f"  {model}: response had no inlineData -> {json.dumps(payload)[:300]}", file=sys.stderr)
    return None


def try_imagen_predict(model: str, key: str) -> bytes | None:
    """predict flow (imagen-4.0-generate-001, imagen-3.0-generate-002)."""
    url = f"https://generativelanguage.googleapis.com/v1beta/models/{model}:predict?key={key}"
    body = {
        "instances": [{"prompt": PROMPT}],
        "parameters": {"sampleCount": 1, "aspectRatio": "16:9"},
    }
    req = urllib.request.Request(
        url,
        data=json.dumps(body).encode("utf-8"),
        headers={"Content-Type": "application/json"},
        method="POST",
    )
    try:
        with urllib.request.urlopen(req, timeout=60) as resp:
            payload = json.loads(resp.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        err_body = e.read().decode("utf-8", errors="ignore")
        print(f"  {model}: HTTP {e.code} - {err_body[:300]}", file=sys.stderr)
        return None
    except Exception as e:
        print(f"  {model}: {e}", file=sys.stderr)
        return None

    try:
        return base64.b64decode(payload["predictions"][0]["bytesBase64Encoded"])
    except (KeyError, IndexError, TypeError):
        print(f"  {model}: no bytesBase64Encoded -> {json.dumps(payload)[:300]}", file=sys.stderr)
        return None


def main() -> int:
    key = load_key()
    for model in CANDIDATES:
        print(f"Trying {model}...", file=sys.stderr)
        if "imagen" in model:
            img = try_imagen_predict(model, key)
        else:
            img = try_generate_content(model, key)
        if img:
            OUT.write_bytes(img)
            print(f"OK with {model}: {OUT} ({len(img)} bytes)")
            return 0
    print("All candidates failed", file=sys.stderr)
    return 1


if __name__ == "__main__":
    sys.exit(main())
