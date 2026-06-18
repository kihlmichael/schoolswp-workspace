"""One-shot test: nano-banana (Gemini 2.5 Flash Image GA) direct API call.

Generates a single on-brand schoolsWP editorial illustration for an LMS WordPress
featured image. Reuses the validated GA model + brand style guide from generate.py.

Usage:
  .venv/Scripts/python tools/article_hero/_test_lms_nano_banana.py
"""

from __future__ import annotations

import base64
import json
import urllib.error
import urllib.request
from pathlib import Path

from dotenv import load_dotenv
import os

ROOT = Path(__file__).resolve().parents[2]
load_dotenv(ROOT / ".env")

GEMINI_MODEL = "gemini-2.5-flash-image"
GEMINI_ENDPOINT = f"https://generativelanguage.googleapis.com/v1beta/models/{GEMINI_MODEL}:generateContent"

STYLE_GUIDE = """Square 1024x1024 minimalist editorial illustration.

Background: very pale cool gray, almost white, the schoolsWP light brand tone (a desaturated near-white with the faintest hint of blue-gray).
Style: monochrome line-art outline illustration. Thin uniform strokes about 4 pixels wide, dark slate blue-gray color. No fills inside shapes, only outlines. Crisp, clean, geometric, premium editorial documentation aesthetic in the style of Linear, Stripe, Vercel, or Notion landing page illustrations.
Composition: centered, generous negative space around the main elements (15 to 20 percent padding on every side). Multiple discrete elements may be grouped or connected by thin dotted or solid lines. Subtle soft drop shadow below the main grouped elements to lift them slightly off the background.
Single accent: exactly one small element in vibrant pure grass green (a saturated clean green). The accent can be a tag, a small dot, a check mark, a tiny indicator, a single highlighted icon, or a single colored stroke. Everything else stays strictly monochrome dark slate blue-gray.
Strict rules:
- No text, no letters, no numbers, no logos, no watermarks
- No gradients, no 3D effects, no photorealism, no painterly style
- No background patterns, no decorative shapes outside the main composition
- No human faces or full bodies, only abstract or schematic representations
- Symmetrical or balanced composition preferred, premium feel mandatory

Concept to illustrate: a laptop screen showing an online course dashboard (a stacked list of video lesson modules with progress bars), connected by thin lines to a small graduation cap, a play button, and a certificate badge. One single module row marked with a green check accent.
"""


def main() -> int:
    key = os.environ.get("GEMINI_API_KEY")
    if not key:
        raise RuntimeError("GEMINI_API_KEY missing in env")

    out_path = ROOT / "tools" / "article_hero" / "_test-lms" / "nano-banana-lms.png"
    out_path.parent.mkdir(parents=True, exist_ok=True)

    body = json.dumps({
        "contents": [{"parts": [{"text": STYLE_GUIDE}]}],
        "generationConfig": {"responseModalities": ["IMAGE"]},
    }).encode("utf-8")

    req = urllib.request.Request(
        GEMINI_ENDPOINT,
        data=body,
        headers={"x-goog-api-key": key, "Content-Type": "application/json"},
        method="POST",
    )
    try:
        with urllib.request.urlopen(req, timeout=180) as resp:
            payload = json.loads(resp.read().decode("utf-8"))
    except urllib.error.HTTPError as exc:
        err_body = exc.read().decode("utf-8", errors="replace")
        raise RuntimeError(f"HTTP {exc.code}: {err_body[:400]}")

    parts = payload["candidates"][0]["content"]["parts"]
    b64 = next(p["inlineData"]["data"] for p in parts if "inlineData" in p)
    out_path.write_bytes(base64.b64decode(b64))
    print(f"OK -> {out_path}  ({out_path.stat().st_size // 1024} KB)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
