"""Generate 8 Telegram bot avatars via Gemini 2.5 Flash Image API.

Direct REST call. The nano-banana-mcp@1.0.3 package targets the deprecated
`gemini-2.5-flash-image-preview` model; this script uses the GA model name
`gemini-2.5-flash-image` instead.

Reads GEMINI_API_KEY from projects/schoolswp/.env.
Writes PNG files to projects/schoolswp/assets/telegram-avatars/.
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
    # 01-orchestrator.png est généré séparément (copie du logo SWP officiel, pas via API)
    (
        "02-studio.png",
        "Flat minimal logo icon. Solid vibrant pure grass green background, a saturated clean green color. Centered composition. Single visual element: a pure white feather quill pen, elegant and simple, with a clean curved tip and smooth contours, rendered as a solid flat silhouette with crisp edges. The feather occupies 55 percent of the canvas and is perfectly centered. No text, no letters, no numbers. No gradient on background. No shadow. No 3D. No outline. Clean vector style. Square 1024x1024. Symbol strictly inside the central 70 percent safe zone for circle crop.",
    ),
    (
        "03-flow.png",
        "Flat minimal logo icon. Solid vibrant pure grass green background, a saturated clean green color. Centered composition. Single visual element: two pure white curved arrows forming a closed circular loop, like a refresh or sync icon, with clean geometric arrowheads. The loop occupies 55 percent of the canvas and is perfectly centered. Symmetrical. No text, no letters, no numbers. No gradient on background. No shadow. No 3D. Clean vector style. Square 1024x1024. Symbol strictly inside the central 70 percent safe zone for circle crop.",
    ),
    (
        "04-radar.png",
        "Flat minimal logo icon. Solid vibrant pure grass green background, a saturated clean green color. Centered composition. Single visual element: three pure white concentric radar waves radiating outward from a central white dot, with consistent stroke width, like a sonar or wifi signal symbol. The waves occupy 60 percent of the canvas and are perfectly centered. Symmetrical. No text, no letters, no numbers. No gradient on background. No shadow. No 3D. Clean vector style. Square 1024x1024. Symbol strictly inside the central 70 percent safe zone for circle crop.",
    ),
    (
        "05-pulse.png",
        "Flat minimal logo icon. Solid vibrant pure grass green background, a saturated clean green color. Centered composition. Single visual element: a horizontal pure white ECG heartbeat pulse line with one clean upward peak and one downward trough, consistent stroke width, flat endpoints on both sides. The line occupies 65 percent of canvas width, perfectly centered vertically and horizontally. No text, no letters, no numbers. No gradient on background. No shadow. No 3D. Clean vector style. Square 1024x1024. Symbol strictly inside the central 70 percent safe zone for circle crop.",
    ),
    (
        "06-claudecodeswp.png",
        "Flat minimal logo icon. Solid pitch-black background, deepest jet black. Centered composition. Single visual element: a bright vibrant grass green symbol composed of exactly two characters, a greater-than angle bracket followed by an underscore on the same baseline, like a terminal prompt. Both characters in bold monospace style, crisp pixel-perfect edges, saturated clean green color, with a slight subtle glow. The pair occupies 40 percent of canvas width, perfectly centered horizontally and vertically. No other text, no numbers, no letters besides the bracket and underscore. No gradient on background. No shadow. No 3D. Clean vector pixel style. Square 1024x1024. Symbol strictly inside the central 70 percent safe zone for circle crop.",
    ),
    (
        "07-claudeswp.png",
        "Flat minimal logo icon. Solid pitch-black background, deepest jet black. Centered composition. Single visual element: a warm burnt orange eight-pointed asterisk star (sunburst style, four long main points vertical-horizontal and four shorter diagonal points between them), symmetrical, crisp clean geometric edges. The asterisk occupies 55 percent of the canvas and is perfectly centered. No text, no letters, no numbers. No gradient on background. No shadow. No 3D. Clean vector style. Square 1024x1024. Symbol strictly inside the central 70 percent safe zone for circle crop.",
    ),
    (
        "08-bitsocialwp.png",
        'Flat minimal logo icon. Solid vibrant pure grass green background, a saturated clean green color. Centered composition. Main visual element: a pure white broadcast antenna tower with three radiating signal wave arcs emanating from the top, clean geometric lines. The antenna occupies 50 percent of canvas height and is centered horizontally and slightly below vertical middle. In the top-right corner, a small bright hot pink rectangular badge containing the word "NEW" in bold white sans-serif letters. The pink badge uses a vibrant saturated hot magenta pink color. No other text besides "NEW". No gradient on background. No shadow. No 3D. Clean vector style. Square 1024x1024. Main symbol strictly inside the central 70 percent safe zone for circle crop.',
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
    print(f"Generating {len(AVATARS)} avatars -> {OUTPUT_DIR}")
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
