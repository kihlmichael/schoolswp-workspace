"""Edit an existing featured image via Gemini (Nano Banana) — image-to-image.

Pass an input image + an English edit instruction; Gemini returns the edited
image preserving the original layout. Use case: translate the text of a
brand-aligned hero from FR to EN without losing the exact composition.

Output: assets/featured-images/post-<id>/v<N>.png (auto-incremented, same dir
as generate_post_featured.py).

Usage:
    python tools/scripts/edit_post_featured.py \\
        --post-id 2865114 \\
        --input assets/featured-images/post-2865114/_reference-fr.jpg \\
        --prompt-file tools/scripts/_prompts/2865114-en.txt
"""

from __future__ import annotations

import argparse
import base64
import json
import mimetypes
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


def edit_image(prompt: str, input_path: Path, api_key: str, max_retries: int = 3) -> bytes:
    mime = mimetypes.guess_type(str(input_path))[0] or "image/jpeg"
    img_b64 = base64.b64encode(input_path.read_bytes()).decode("ascii")

    body = json.dumps(
        {
            "contents": [
                {
                    "parts": [
                        {"inlineData": {"mimeType": mime, "data": img_b64}},
                        {"text": prompt},
                    ]
                }
            ],
            "generationConfig": {"responseModalities": ["IMAGE"]},
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
        out_b64 = next(p["inlineData"]["data"] for p in parts if "inlineData" in p)
    except (KeyError, IndexError, StopIteration):
        raise SystemExit(f"No image in response: {json.dumps(payload)[:400]}")
    return base64.b64decode(out_b64)


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
    parser.add_argument("--input", required=True, help="path to source image")
    parser.add_argument("--prompt")
    parser.add_argument("--prompt-file")
    args = parser.parse_args()

    if not args.prompt and not args.prompt_file:
        parser.error("--prompt or --prompt-file required")

    prompt = args.prompt or Path(args.prompt_file).read_text(encoding="utf-8").strip()
    input_path = Path(args.input).resolve()
    if not input_path.exists():
        raise SystemExit(f"input not found: {input_path}")

    api_key = load_env_key("GEMINI_API_KEY")
    print(f"Editing image for post {args.post_id} from {input_path.name}...")
    img_bytes = edit_image(prompt, input_path, api_key)
    out = next_output_path(args.post_id)
    out.write_bytes(img_bytes)
    print(f"OK -> {out.relative_to(ROOT)} ({out.stat().st_size // 1024} KB)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
