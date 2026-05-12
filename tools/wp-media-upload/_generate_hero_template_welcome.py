"""One-shot: generate the hero image for the lead magnet page
"template-welcome-fluentcrm" via Gemini 2.5 Flash Image (Nano Banana).

Reads GEMINI_API_KEY from projects/schoolswp/.env (priority over shell
because the shell key is stale, cf. feedback_env_priority_over_os_environ.md).
Writes the PNG to the article inbox folder for wp-media-upload.
"""

from __future__ import annotations

import base64
import json
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path

ROOT = Path("d:/VS Code/CLAUDE CODE/projects/schoolswp")
ENV_FILE = ROOT / ".env"
INBOX_DIR = ROOT / "tools" / "wp-media-upload" / "inbox" / "template-welcome-fluentcrm"
OUT_FILE = INBOX_DIR / "01-hero-template-welcome-fluentcrm.png"

GEMINI_MODEL = "gemini-2.5-flash-image"
GEMINI_ENDPOINT = f"https://generativelanguage.googleapis.com/v1beta/models/{GEMINI_MODEL}:generateContent"

PROMPT = """Wide 16:9 hero illustration, brand asset for a French lead magnet landing page. Strict minimalist editorial design.

Background: full bleed soft warm off-white, almost white with a hint of gray (very subtle paper tone, NOT bright white, NOT cream, NOT beige). Plenty of negative space. Completely flat, no texture, no grain.

Two-column composition. Layout strictly landscape 16 by 9.

LEFT COLUMN (about 55 percent width, left aligned, vertically centered, comfortable left padding):
- At the top, a small pill-shaped badge with a vivid pure grass green left dot and uppercase tracked label reading "TEMPLATE GRATUIT FLUENTCRM" in dark charcoal, very small, clean sans-serif.
- Big multi-line headline in heavy bold black sans-serif (Inter or Plus Jakarta Sans look), tight line-height. Exactly three lines:
  Line 1: "Sequence Welcome"
  Line 2: "FluentCRM" (this word highlighted in vivid pure grass green, all other words in deep near-black)
  Line 3: "a copier"
- Below the headline, a short two-line subtitle in medium gray, regular weight, smaller: "4 emails prets a copier pour engager tes abonnes des l inscription sur WordPress."
- At the very bottom of the left column, a tiny gray signature line: "Michael KIHL . schoolsWP.com" with a small vivid grass green dot as separator.

RIGHT COLUMN (about 45 percent width, vertically centered):
- A single large rounded square card, pure white fill, very soft long subtle drop shadow underneath, generous internal padding. The card has a 4 pixel tall accent strip at the very top in pure vivid grass green.
- Inside the card, a flat 2D vector illustration of an email welcome sequence: four small rounded rectangles arranged horizontally with equal spacing, connected by thin straight dotted gray lines. Each rectangle is a stylized envelope icon in dark charcoal stroke (no fill), with a small numbered circle 1, 2, 3, 4 above each envelope in vivid grass green with white numerals. Below each envelope a tiny gray label E1 E2 E3 E4. Below the row of four envelopes a thin horizontal timeline in light gray with three tiny clock icons in green between the envelopes, representing wait times.

Style: corporate SaaS, editorial, calm, premium. Pure flat vectors only, no gradients except the very subtle card shadow, no 3D, no photorealistic elements, no glow, no neon, no glassmorphism. The only saturated color in the entire image is one specific vivid pure grass green used for accents, the highlighted word, the dots, and the top accent strip. Everything else strictly neutral: deep charcoal near-black for type, medium gray for secondary text, light gray for separator lines.

Aspect ratio strictly 16 by 9 landscape, target resolution 1920 by 1080.

DO NOT add any extra text beyond what is described. DO NOT write any hex code or color name visible in the image. DO NOT use cream, beige, blue, purple, yellow, red. DO NOT use any em-dash, only middle dot, colon, or short hyphen as separators. DO NOT include any logo or brand mark other than the schoolsWP signature line.
"""


def load_env_key(name: str) -> str:
    if ENV_FILE.exists():
        for line in ENV_FILE.read_text(encoding="utf-8").splitlines():
            if line.startswith(f"{name}="):
                return line.split("=", 1)[1].strip()
    raise RuntimeError(f"{name} not found in .env")


def generate(api_key: str, max_retries: int = 3) -> bytes:
    body = json.dumps(
        {
            "contents": [{"parts": [{"text": PROMPT}]}],
            "generationConfig": {"responseModalities": ["IMAGE"]},
        }
    ).encode("utf-8")

    last_err = None
    for attempt in range(1, max_retries + 1):
        req = urllib.request.Request(
            GEMINI_ENDPOINT,
            data=body,
            headers={"x-goog-api-key": api_key, "Content-Type": "application/json"},
            method="POST",
        )
        try:
            with urllib.request.urlopen(req, timeout=180) as resp:
                payload = json.loads(resp.read().decode("utf-8"))
            parts = payload["candidates"][0]["content"]["parts"]
            img_b64 = next(p["inlineData"]["data"] for p in parts if "inlineData" in p)
            return base64.b64decode(img_b64)
        except urllib.error.HTTPError as exc:
            err = exc.read().decode("utf-8", errors="replace")
            last_err = f"HTTP {exc.code}: {err[:300]}"
            if attempt < max_retries and (exc.code == 429 or exc.code >= 500):
                cool = 30 * attempt
                print(f"  retry in {cool}s ({attempt}/{max_retries}): {last_err[:120]}", file=sys.stderr)
                time.sleep(cool)
                continue
            raise RuntimeError(last_err) from exc
        except (KeyError, IndexError, StopIteration) as exc:
            raise RuntimeError(f"no image in response: {json.dumps(payload)[:300]}") from exc

    raise RuntimeError(last_err or "unknown error")


def main() -> int:
    key = load_env_key("GEMINI_API_KEY")
    INBOX_DIR.mkdir(parents=True, exist_ok=True)
    print(f"Generating hero -> {OUT_FILE}")
    img = generate(key)
    OUT_FILE.write_bytes(img)
    print(f"OK ({OUT_FILE.stat().st_size // 1024} KB)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
