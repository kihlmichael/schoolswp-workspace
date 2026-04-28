#!/usr/bin/env python3
"""Generate 5 YouTube thumbnail concepts for the OttoKit cocon via OpenAI gpt-image-1."""

from __future__ import annotations

import base64
import json
import os
import sys
import time
from pathlib import Path
from urllib import error, request

PROJECT_ROOT = Path(__file__).resolve().parents[2]
ENV_FILE = PROJECT_ROOT / ".env"
OUT_DIR = PROJECT_ROOT / "content" / "assets" / "youtube-thumbnails" / "ottokit"
API_URL = "https://api.openai.com/v1/images/generations"
MODEL = "gpt-image-1"
SIZE = "1536x1024"
QUALITY = "high"


def load_env() -> None:
    if not ENV_FILE.exists():
        sys.exit(f".env not found: {ENV_FILE}")
    for line in ENV_FILE.read_text(encoding="utf-8").splitlines():
        s = line.strip()
        if not s or s.startswith("#") or "=" not in s:
            continue
        k, v = s.split("=", 1)
        os.environ.setdefault(k.strip(), v.strip())


PROMPTS: list[dict[str, str]] = [
    {
        "slug": "01-140k-sites",
        "prompt": (
            "YouTube thumbnail, 16:9 aspect ratio, cinematic high-contrast style. "
            "Giant bold yellow number '140K' on the left side, extremely thick sans-serif font, "
            "glowing edge, slight 3D depth. Small subtitle underneath in white: 'SITES WORDPRESS'. "
            "On the right side, a stylized modern laptop floating in 3D space with a glowing "
            "workflow diagram on screen made of connected nodes in blue and purple gradients. "
            "Dark navy gradient background with subtle radial glow. Mood: confident, tech-premium, "
            "impressive. No humans. Sharp focus, professional lighting. Text must be perfectly legible."
        ),
    },
    {
        "slug": "02-gratuit-vs-zapier",
        "prompt": (
            "YouTube thumbnail, 16:9. Vertical split screen. LEFT HALF: red-tinted dark background, "
            "a large orange circular logo shape (Zapier-style) with a thick red X crossed over it, "
            "white subtitle 'ZAPIER' below. RIGHT HALF: bright yellow background, clean stylized black "
            "lightning-bolt logo inside a rounded square, bold black subtitle 'OTTOKIT' below. "
            "Big bold overlay headline centered across the divider, white text with thick black outline: "
            "'GRATUIT vs 30 euros/mois'. High contrast, dramatic, clickbait energy. "
            "No humans. Sharp saturated colors, professional finish."
        ),
    },
    {
        "slug": "03-suretriggers-mort",
        "prompt": (
            "YouTube thumbnail, 16:9. Dark purple gradient background with subtle smoke texture. "
            "LEFT SIDE: grayed-out faded word 'SureTriggers' with a large red diagonal strikethrough, "
            "cracked-glass effect, looking dead and broken. MIDDLE: giant bright yellow curved arrow "
            "pointing right, with motion blur and glowing edges. RIGHT SIDE: vibrant modern wordmark "
            "'OttoKit' in bold white with a purple underline, small sparkle icons around it, looking alive "
            "and new. Top banner overlay in bold white with red accent: 'SureTriggers est MORT'. "
            "Dramatic before/after transformation feel. No humans. Premium finish."
        ),
    },
    {
        "slug": "04-canvas-automatise",
        "prompt": (
            "YouTube thumbnail, 16:9. Close-up of a complex automation workflow canvas: multiple "
            "connected nodes (rectangular cards with small icons) linked by glowing curved lines, "
            "representing WordPress triggers wired to email, payment and AI actions. Color-coded nodes "
            "in purple, blue and green. One central node highlighted with a thick red circle outline "
            "and a large yellow arrow pointing at it. Dark background with subtle grid pattern. "
            "Bold white overlay text in bottom-left corner, slight tilt: 'J'AI TOUT AUTOMATISE'. "
            "Professional dashboard aesthetic, cinematic depth of field. No humans."
        ),
    },
    {
        "slug": "05-le-verdict",
        "prompt": (
            "YouTube thumbnail, 16:9. Three logo plates in a horizontal row on a dark courtroom-inspired "
            "background with subtle wood texture and a dramatic spotlight from above. "
            "LEFT plate: wordmark 'n8n' with a silver '7/10' badge. MIDDLE plate: wordmark "
            "'Uncanny Automator' with a bronze '6/10' badge. RIGHT plate: wordmark 'OttoKit' "
            "highlighted with a gold glow and a '9/10' gold medal badge above it, slightly larger "
            "than the others. Giant bold yellow overlay headline at the top: 'LE VERDICT'. "
            "Cinematic dramatic lighting, high contrast, premium feel. No humans."
        ),
    },
]


def generate(prompt: str) -> bytes:
    payload = {
        "model": MODEL,
        "prompt": prompt,
        "size": SIZE,
        "quality": QUALITY,
        "n": 1,
    }
    req = request.Request(
        API_URL,
        data=json.dumps(payload).encode("utf-8"),
        headers={
            "Authorization": f"Bearer {os.environ['OPENAI_API_KEY']}",
            "Content-Type": "application/json",
        },
    )
    with request.urlopen(req, timeout=180) as resp:
        data = json.loads(resp.read())
    return base64.b64decode(data["data"][0]["b64_json"])


def build_index(manifest: list[dict[str, str]]) -> str:
    cards = []
    for e in manifest:
        cards.append(
            f'<figure><img src="{e["file"]}" alt="{e["slug"]}">'
            f'<figcaption><b>{e["slug"]}</b><br><small>{e["prompt"]}</small></figcaption></figure>'
        )
    return (
        "<!doctype html><html lang=\"fr\"><head><meta charset=\"utf-8\">"
        "<title>OttoKit - 5 miniatures YouTube</title>"
        "<style>body{background:#0e0e11;color:#eee;font-family:system-ui,Segoe UI,sans-serif;"
        "padding:32px;max-width:1200px;margin:auto}"
        "h1{margin:0 0 8px;font-size:28px}p.lead{color:#aaa;margin:0 0 32px}"
        ".grid{display:grid;gap:32px}"
        "figure{margin:0;background:#1a1a1f;border-radius:12px;overflow:hidden;"
        "box-shadow:0 8px 24px rgba(0,0,0,.4)}"
        "img{width:100%;display:block;border-bottom:1px solid #2a2a30}"
        "figcaption{padding:16px;font-size:14px;line-height:1.5}"
        "figcaption b{color:#ffd400;font-size:15px}"
        "figcaption small{color:#bbb;display:block;margin-top:6px}</style></head><body>"
        "<h1>OttoKit - 5 concepts miniature YouTube</h1>"
        f"<p class=\"lead\">Modele {MODEL}, taille {SIZE}, qualite {QUALITY}. "
        f"Genere le {time.strftime('%Y-%m-%d %H:%M')}.</p>"
        f"<div class=\"grid\">{''.join(cards)}</div></body></html>"
    )


def main() -> int:
    load_env()
    if not os.environ.get("OPENAI_API_KEY"):
        sys.exit("OPENAI_API_KEY missing from .env")
    OUT_DIR.mkdir(parents=True, exist_ok=True)

    manifest: list[dict[str, str]] = []
    for entry in PROMPTS:
        out = OUT_DIR / f"{entry['slug']}.png"
        if out.exists() and out.stat().st_size > 0:
            print(f"-> {entry['slug']} (skipped, already exists)")
            manifest.append({"slug": entry["slug"], "file": out.name, "prompt": entry["prompt"]})
            continue
        print(f"-> {entry['slug']}")
        try:
            img = generate(entry["prompt"])
        except error.HTTPError as e:
            body = e.read().decode(errors="replace")
            print(f"   ! HTTP {e.code}: {body[:500]}")
            continue
        except error.URLError as e:
            print(f"   ! URLError: {e}")
            continue
        for attempt in range(3):
            try:
                out.write_bytes(img)
                break
            except PermissionError as e:
                print(f"   ! write attempt {attempt + 1}/3 failed: {e}")
                time.sleep(1.5)
        else:
            print(f"   ! gave up writing {out}")
            continue
        manifest.append({"slug": entry["slug"], "file": out.name, "prompt": entry["prompt"]})
        print(f"   OK {out.name} ({len(img) // 1024} KB)")

    (OUT_DIR / "prompts.json").write_text(
        json.dumps(manifest, indent=2, ensure_ascii=False), encoding="utf-8"
    )
    (OUT_DIR / "index.html").write_text(build_index(manifest), encoding="utf-8")

    print(f"\nDone. {len(manifest)}/{len(PROMPTS)} images generated.")
    print(f"Open: {OUT_DIR / 'index.html'}")
    return 0 if manifest else 1


if __name__ == "__main__":
    sys.exit(main())
