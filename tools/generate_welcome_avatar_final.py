"""Generate final welcome avatar (09-welcome.png) — house silhouette, black bg + green icon.

One-shot script. Does NOT regenerate the 8 existing avatars.
Writes to assets/telegram-avatars/09-welcome.png.
"""

from __future__ import annotations

import base64
import json
import os
import sys
import urllib.error
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ENV_FILE = ROOT / ".env"
OUTPUT_DIR = ROOT / "assets" / "telegram-avatars"

MODEL = "gemini-2.5-flash-image"
ENDPOINT = f"https://generativelanguage.googleapis.com/v1beta/models/{MODEL}:generateContent"

FILENAME = "09-welcome.png"
PROMPT = (
    "Flat minimal logo icon. Solid pitch-black background, deepest jet black. "
    "Centered composition. Single visual element: a vibrant bright grass green "
    "house silhouette with a triangular pitched roof and a rectangular base, "
    "clean geometric lines, simplified shape, no windows, no door, just the "
    "outer silhouette filled with saturated clean green color. The house occupies "
    "55 percent of the canvas and is perfectly centered. No text, no letters, "
    "no numbers. No gradient on background. No shadow. No 3D. No outline. "
    "Clean vector style. Square 1024x1024. Symbol strictly inside the central "
    "70 percent safe zone for circle crop."
)


def load_api_key() -> str:
    if ENV_FILE.exists():
        for line in ENV_FILE.read_text(encoding="utf-8").splitlines():
            if line.startswith("GEMINI_API_KEY="):
                return line.split("=", 1)[1].strip()
    if key := os.environ.get("GEMINI_API_KEY"):
        return key
    raise RuntimeError("GEMINI_API_KEY not found in .env or env")


def main() -> int:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    api_key = load_api_key()
    print(f"Generating {FILENAME} -> {OUTPUT_DIR}")

    body = json.dumps(
        {
            "contents": [{"parts": [{"text": PROMPT}]}],
            "generationConfig": {"responseModalities": ["IMAGE"]},
        }
    ).encode("utf-8")

    req = urllib.request.Request(
        ENDPOINT,
        data=body,
        headers={"x-goog-api-key": api_key, "Content-Type": "application/json"},
        method="POST",
    )

    try:
        with urllib.request.urlopen(req, timeout=120) as resp:
            payload = json.loads(resp.read().decode("utf-8"))
    except urllib.error.HTTPError as exc:
        err = exc.read().decode("utf-8", errors="replace")
        print(f"FAIL HTTP {exc.code}: {err[:300]}")
        return 1

    try:
        parts = payload["candidates"][0]["content"]["parts"]
        img_b64 = next(p["inlineData"]["data"] for p in parts if "inlineData" in p)
    except (KeyError, IndexError, StopIteration):
        print(f"FAIL no image in response: {json.dumps(payload)[:300]}")
        return 1

    out = OUTPUT_DIR / FILENAME
    out.write_bytes(base64.b64decode(img_b64))
    print(f"OK {out} ({out.stat().st_size // 1024} KB)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
