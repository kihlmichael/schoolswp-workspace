"""Generate a single 16:9 featured image via Gemini (Nano Banana).

Output: assets/featured-images/post-<id>/v<N>.png (auto-incremented).
Reads GEMINI_API_KEY from .env. No upload; user reviews then approves.

Usage:
    python tools/scripts/generate_post_featured.py --post-id 343156 --prompt-file <path>
    python tools/scripts/generate_post_featured.py --post-id 343156 --prompt "..."
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

ROOT = Path(__file__).resolve().parents[2]
ENV_FILE = ROOT / ".env"
ASSETS_DIR = ROOT / "assets" / "featured-images"

GEMINI_MODEL = "gemini-2.5-flash-image"
GEMINI_ENDPOINT = f"https://generativelanguage.googleapis.com/v1beta/models/{GEMINI_MODEL}:generateContent"


def load_env_key(name: str) -> str:
    if ENV_FILE.exists():
        for line in ENV_FILE.read_text(encoding="utf-8").splitlines():
            if line.startswith(f"{name}="):
                return line.split("=", 1)[1].strip()
    if key := os.environ.get(name):
        return key
    raise RuntimeError(f"{name} not found in .env or env")


def generate(prompt: str, api_key: str, aspect: str = "16:9", max_retries: int = 3) -> bytes:
    body = json.dumps(
        {
            "contents": [{"parts": [{"text": prompt}]}],
            "generationConfig": {
                "responseModalities": ["IMAGE"],
                "imageConfig": {"aspectRatio": aspect},
            },
        }
    ).encode("utf-8")

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
            break
        except urllib.error.HTTPError as exc:
            err = exc.read().decode("utf-8", errors="replace")
            if attempt < max_retries and ("API_KEY_INVALID" in err or exc.code == 429 or exc.code >= 500):
                backoff = 30
                print(f"  rate-limited, cooling down {backoff}s (attempt {attempt}/{max_retries})")
                time.sleep(backoff)
                continue
            raise SystemExit(f"HTTP {exc.code}: {err[:400]}")

    try:
        parts = payload["candidates"][0]["content"]["parts"]
        img_b64 = next(p["inlineData"]["data"] for p in parts if "inlineData" in p)
    except (KeyError, IndexError, StopIteration):
        raise SystemExit(f"No image in response: {json.dumps(payload)[:400]}")
    return base64.b64decode(img_b64)


def next_output_path(post_id: int) -> Path:
    out_dir = ASSETS_DIR / f"post-{post_id}"
    out_dir.mkdir(parents=True, exist_ok=True)
    n = 1
    while (out_dir / f"v{n}.png").exists():
        n += 1
    return out_dir / f"v{n}.png"


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--post-id", type=int, required=True)
    parser.add_argument("--prompt")
    parser.add_argument("--prompt-file")
    parser.add_argument("--aspect", default="16:9", choices=["1:1", "4:3", "3:4", "16:9", "9:16"])
    args = parser.parse_args()

    if not args.prompt and not args.prompt_file:
        parser.error("--prompt or --prompt-file required")

    prompt = args.prompt or Path(args.prompt_file).read_text(encoding="utf-8").strip()
    api_key = load_env_key("GEMINI_API_KEY")
    print(f"Generating {args.aspect} image for post {args.post_id}...")
    img_bytes = generate(prompt, api_key, aspect=args.aspect)
    out = next_output_path(args.post_id)
    out.write_bytes(img_bytes)
    print(f"OK → {out.relative_to(ROOT)} ({out.stat().st_size // 1024} KB)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
