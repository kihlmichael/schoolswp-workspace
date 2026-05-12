"""Generate Telegram bot avatars via switchable image engine.

Two engines supported:
- nano_banana (default): Gemini 2.5 Flash Image, free tier, weak on FR text rendering
- openai: gpt-image-1 (model name read from env OPENAI_IMAGE_MODEL), paid, strong on text

Engine selection priority:
1. CLI flag --engine (forces choice for the whole run)
2. Optional 3rd field of an AVATARS tuple (per-image engine)
3. Default "nano_banana"

Note: gpt-image-2 requires OpenAI organization verification (KYC). Without it, the
fallback gpt-image-1 still beats Nano Banana on French text rendering (cf. test
report at tools/test-gpt-image-2-vs-nano-banana/REPORT.md).

Reads GEMINI_API_KEY and OPENAI_API_KEY from projects/schoolswp/.env.
Writes PNG files to projects/schoolswp/assets/telegram-avatars/.

Usage:
  .venv/Scripts/python tools/generate_telegram_avatars.py
  .venv/Scripts/python tools/generate_telegram_avatars.py --engine openai
  .venv/Scripts/python tools/generate_telegram_avatars.py --engine nano_banana
"""

from __future__ import annotations

import argparse
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

GEMINI_MODEL = "gemini-2.5-flash-image"
GEMINI_ENDPOINT = f"https://generativelanguage.googleapis.com/v1beta/models/{GEMINI_MODEL}:generateContent"

OPENAI_MODEL = os.environ.get("OPENAI_IMAGE_MODEL", "gpt-image-1")
OPENAI_ENDPOINT = "https://api.openai.com/v1/images/generations"

# Tuple shape: (filename, prompt) or (filename, prompt, engine)
# engine in {"nano_banana", "openai"} pins that avatar to a specific engine
AVATARS: list[tuple] = [
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


def load_env_key(name: str) -> str:
    if ENV_FILE.exists():
        for line in ENV_FILE.read_text(encoding="utf-8").splitlines():
            if line.startswith(f"{name}="):
                return line.split("=", 1)[1].strip()
    if key := os.environ.get(name):
        return key
    raise RuntimeError(f"{name} not found in .env or env")


def generate_via_gemini(filename: str, prompt: str, api_key: str, max_retries: int = 2) -> str:
    body = json.dumps(
        {
            "contents": [{"parts": [{"text": prompt}]}],
            "generationConfig": {"responseModalities": ["IMAGE"]},
        }
    ).encode("utf-8")

    payload = None
    for attempt in range(1, max_retries + 1):
        req = urllib.request.Request(
            GEMINI_ENDPOINT,
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

    if payload is None:
        return "no payload after retries"

    try:
        parts = payload["candidates"][0]["content"]["parts"]
        img_b64 = next(p["inlineData"]["data"] for p in parts if "inlineData" in p)
    except (KeyError, IndexError, StopIteration):
        return f"no image in response: {json.dumps(payload)[:300]}"

    out = OUTPUT_DIR / filename
    out.write_bytes(base64.b64decode(img_b64))
    return f"OK ({out.stat().st_size // 1024} KB)"


def generate_via_openai(filename: str, prompt: str, api_key: str) -> str:
    body = json.dumps(
        {
            "model": OPENAI_MODEL,
            "prompt": prompt,
            "size": "1024x1024",
            "quality": "medium",
            "n": 1,
        }
    ).encode("utf-8")

    req = urllib.request.Request(
        OPENAI_ENDPOINT,
        data=body,
        headers={"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"},
        method="POST",
    )
    try:
        with urllib.request.urlopen(req, timeout=180) as resp:
            payload = json.loads(resp.read().decode("utf-8"))
    except urllib.error.HTTPError as exc:
        return f"HTTP {exc.code}: {exc.read().decode('utf-8', errors='replace')[:200]}"

    try:
        img_b64 = payload["data"][0]["b64_json"]
    except (KeyError, IndexError):
        return f"no image in response: {json.dumps(payload)[:300]}"

    out = OUTPUT_DIR / filename
    out.write_bytes(base64.b64decode(img_b64))
    return f"OK ({out.stat().st_size // 1024} KB)"


ENGINES: dict[str, tuple[str, callable]] = {
    "nano_banana": ("GEMINI_API_KEY", generate_via_gemini),
    "openai": ("OPENAI_API_KEY", generate_via_openai),
}

THROTTLE_S = {"nano_banana": 15, "openai": 3}


def resolve_engine(item: tuple, cli_choice: str | None) -> str:
    if cli_choice:
        return cli_choice
    if len(item) >= 3 and item[2]:
        return item[2]
    return "nano_banana"


def main() -> int:
    parser = argparse.ArgumentParser(description="Generate Telegram bot avatars (nano_banana | openai).")
    parser.add_argument(
        "--engine",
        choices=list(ENGINES.keys()),
        default=None,
        help="Force engine for the whole run. If absent, uses per-avatar engine field or 'nano_banana'.",
    )
    args = parser.parse_args()

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    keys: dict[str, str] = {}

    print(f"Generating {len(AVATARS)} avatars -> {OUTPUT_DIR}")
    if args.engine:
        print(f"Engine forced via CLI: {args.engine}")

    errors = 0
    for i, item in enumerate(AVATARS, 1):
        fn = item[0]
        pr = item[1]
        engine = resolve_engine(item, args.engine)
        env_var, generate_fn = ENGINES[engine]

        if env_var not in keys:
            keys[env_var] = load_env_key(env_var)

        print(f"[{i}/{len(AVATARS)}] {fn} via {engine} ...", flush=True)
        status = generate_fn(fn, pr, keys[env_var])
        marker = "OK" if status.startswith("OK") else "FAIL"
        print(f"    [{marker}] {status}")
        if not status.startswith("OK"):
            errors += 1
        if i < len(AVATARS):
            time.sleep(THROTTLE_S[engine])
    return errors


if __name__ == "__main__":
    sys.exit(main())
