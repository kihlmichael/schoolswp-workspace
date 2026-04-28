"""Generate 3 avatar options for the @schoolsWP_bot (welcome) bot via Gemini.

One-shot script. Does NOT regenerate the 8 existing avatars.
Writes to assets/telegram-avatars/09-welcome-option{1,2,3}.png.

Reads GEMINI_API_KEY from projects/schoolswp/.env.
"""

from __future__ import annotations

import base64
import json
import os
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ENV_FILE = ROOT / ".env"
OUTPUT_DIR = ROOT / "assets" / "telegram-avatars"

MODEL = "gemini-2.5-flash-image"
ENDPOINT = f"https://generativelanguage.googleapis.com/v1beta/models/{MODEL}:generateContent"

AVATARS: list[tuple[str, str]] = [
    (
        "09-welcome-option1-letter-s.png",
        "Flat minimal logo icon. Solid vibrant pure grass green background, a saturated clean green color. Centered composition. Single visual element: a pure white letter 'S' in bold modern geometric sans-serif typography, with clean rounded terminals, like a premium brand monogram. The letter 'S' occupies 55 percent of the canvas and is perfectly centered. No other letters, no numbers, no text. No gradient on background. No shadow. No 3D. No outline. Clean vector style. Square 1024x1024. Letter strictly inside the central 70 percent safe zone for circle crop.",
    ),
    (
        "09-welcome-option2-house.png",
        "Flat minimal logo icon. Solid vibrant pure grass green background, a saturated clean green color. Centered composition. Single visual element: a pure white house silhouette with a triangular pitched roof and a rectangular base, clean geometric lines, simplified shape, no windows, no door, just the outer silhouette. The house occupies 55 percent of the canvas and is perfectly centered. No text, no letters, no numbers. No gradient on background. No shadow. No 3D. No outline. Clean vector style. Square 1024x1024. Symbol strictly inside the central 70 percent safe zone for circle crop.",
    ),
    (
        "09-welcome-option3-waving-hand.png",
        "Flat minimal logo icon. Solid vibrant pure grass green background, a saturated clean green color. Centered composition. Single visual element: a pure white open hand raised with palm facing forward in a friendly waving gesture, all five fingers visible and clearly separated, simplified silhouette, clean geometric lines. The hand occupies 55 percent of the canvas and is perfectly centered. No text, no letters, no numbers. No gradient on background. No shadow. No 3D. No outline. Clean vector style. Square 1024x1024. Symbol strictly inside the central 70 percent safe zone for circle crop.",
    ),
]


def load_api_key() -> str:
    if ENV_FILE.exists():
        for line in ENV_FILE.read_text(encoding="utf-8").splitlines():
            if line.startswith("GEMINI_API_KEY="):
                return line.split("=", 1)[1].strip()
    if key := os.environ.get("GEMINI_API_KEY"):
        return key
    raise RuntimeError("GEMINI_API_KEY not found in .env or env")


def generate_one(filename: str, prompt: str, api_key: str, max_retries: int = 2) -> str:
    body = json.dumps(
        {
            "contents": [{"parts": [{"text": prompt}]}],
            "generationConfig": {"responseModalities": ["IMAGE"]},
        }
    ).encode("utf-8")

    for attempt in range(1, max_retries + 1):
        req = urllib.request.Request(
            ENDPOINT,
            data=body,
            headers={"x-goog-api-key": api_key, "Content-Type": "application/json"},
            method="POST",
        )
        try:
            with urllib.request.urlopen(req, timeout=120) as resp:
                payload = json.loads(resp.read().decode("utf-8"))
            break
        except urllib.error.HTTPError as exc:
            err = exc.read().decode("utf-8", errors="replace")
            if attempt < max_retries and ("API_KEY_INVALID" in err or exc.code == 429 or exc.code >= 500):
                backoff = 45
                print(f"  rate-limited, cooling down {backoff}s (attempt {attempt}/{max_retries})")
                time.sleep(backoff)
                continue
            return f"HTTP {exc.code}: {err[:200]}"

    try:
        parts = payload["candidates"][0]["content"]["parts"]
        img_b64 = next(p["inlineData"]["data"] for p in parts if "inlineData" in p)
    except (KeyError, IndexError, StopIteration):
        return f"no image in response: {json.dumps(payload)[:300]}"

    out = OUTPUT_DIR / filename
    out.write_bytes(base64.b64decode(img_b64))
    return f"OK ({out.stat().st_size // 1024} KB)"


def main() -> int:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    api_key = load_api_key()
    print(f"Generating {len(AVATARS)} welcome avatar options -> {OUTPUT_DIR}")
    errors = 0
    for i, (fn, pr) in enumerate(AVATARS, 1):
        print(f"[{i}/{len(AVATARS)}] {fn} ...", flush=True)
        status = generate_one(fn, pr, api_key)
        marker = "OK" if status.startswith("OK") else "FAIL"
        print(f"    [{marker}] {status}")
        if not status.startswith("OK"):
            errors += 1
        if i < len(AVATARS):
            time.sleep(15)
    return errors


if __name__ == "__main__":
    sys.exit(main())
