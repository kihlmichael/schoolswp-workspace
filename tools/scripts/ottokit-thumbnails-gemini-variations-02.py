#!/usr/bin/env python3
"""Generate 3 variations of concept #02 (Gratuit vs Zapier) via Gemini 2.5 Flash Image."""

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
MODEL = "gemini-2.5-flash-image"
API_URL = f"https://generativelanguage.googleapis.com/v1beta/models/{MODEL}:generateContent"
ASPECT_RATIO = "16:9"


def load_env() -> None:
    if not ENV_FILE.exists():
        sys.exit(f".env not found: {ENV_FILE}")
    for line in ENV_FILE.read_text(encoding="utf-8").splitlines():
        s = line.strip()
        if not s or s.startswith("#") or "=" not in s:
            continue
        k, v = s.split("=", 1)
        os.environ.setdefault(k.strip(), v.strip())


VARIATIONS: list[dict[str, str]] = [
    {
        "slug": "02-zapier-v1-typo-frontale",
        "angle": "Typo frontale, split diagonal",
        "prompt": (
            "YouTube thumbnail, 16:9 aspect ratio. Extreme typography focus. "
            "Full-frame split diagonally at -20 degrees angle. "
            "LEFT side (dark red gradient background): huge crossed-out price '30 euros / mois' "
            "in heavy white bold sans-serif font with thick red strikethrough line across it, "
            "small orange Zapier-style circular mark in the top corner. "
            "RIGHT side (bright yellow gradient background): single huge word 'GRATUIT' in "
            "massive black ultra-bold sans-serif font, with a bold black lightning-bolt icon "
            "next to it representing OttoKit. "
            "Between the two halves, a jagged neon-cyan tear/crack effect adds drama. "
            "Headline overlay at top center in white with thick black outline: 'ZAPIER vs OTTOKIT'. "
            "Extreme contrast, clickbait aesthetic, premium finish, no humans, no photos, text perfectly legible."
        ),
    },
    {
        "slug": "02-zapier-v2-metaphore-argent",
        "angle": "Métaphore billets qui s'envolent",
        "prompt": (
            "YouTube thumbnail, 16:9 aspect ratio. Dark teal gradient background with subtle grain. "
            "LEFT SIDE: exploding pile of green dollar bills and euro notes blowing away to the left "
            "with motion blur trails, a small orange Zapier-style circular logo mark fading and "
            "tumbling with the bills. Red subtitle below: 'ZAPIER - 30 euros / mois'. "
            "RIGHT SIDE: a floating clean gold coin with a black lightning-bolt OttoKit icon on top, "
            "glowing bright yellow halo around it, subtle floating sparkles. Yellow subtitle below "
            "in bold: 'OTTOKIT - GRATUIT'. "
            "Big overlay headline centered at top, white bold with thick black outline: 'GARDE TON ARGENT'. "
            "Financial magazine meets cinematic premium aesthetic, dramatic side-lighting, no humans, "
            "crisp typography perfectly legible."
        ),
    },
    {
        "slug": "02-zapier-v3-comparatif-cartes",
        "angle": "Comparatif produit 2 cartes",
        "prompt": (
            "YouTube thumbnail, 16:9 aspect ratio. Minimalist premium dark navy background with "
            "a very subtle grid pattern. Two product comparison cards side by side. "
            "LEFT CARD (greyed out, semi-transparent, tilted slightly backwards): orange Zapier-style "
            "circular logo at top, three line items below each with a red X mark - 'Payant', 'Limite', "
            "'Lent'. Red price banner at the bottom: '30 euros / mois'. "
            "RIGHT CARD (vibrant, glowing bright yellow thick border, slightly larger and forward): "
            "black lightning-bolt OttoKit logo at top, three line items below each with a bright "
            "green check mark - 'Gratuit', 'Illimite', 'Rapide'. Green price banner at the bottom: '0 euros'. "
            "Huge top headline in yellow bold sans-serif with black outline: 'ON COMPARE'. "
            "Modern SaaS landing-page aesthetic with cinematic rim lighting, no humans, crisp sharp "
            "typography, all text perfectly legible."
        ),
    },
]


def generate(prompt: str) -> bytes:
    payload = {
        "contents": [{"parts": [{"text": prompt}]}],
        "generationConfig": {
            "responseModalities": ["IMAGE"],
            "imageConfig": {"aspectRatio": ASPECT_RATIO},
        },
    }
    req = request.Request(
        API_URL,
        data=json.dumps(payload).encode("utf-8"),
        headers={
            "x-goog-api-key": os.environ["GEMINI_API_KEY"],
            "Content-Type": "application/json",
        },
    )
    with request.urlopen(req, timeout=180) as resp:
        data = json.loads(resp.read())

    candidates = data.get("candidates") or []
    if not candidates:
        raise RuntimeError(f"no candidates returned: {json.dumps(data)[:500]}")
    parts = candidates[0].get("content", {}).get("parts") or []
    for p in parts:
        inline = p.get("inlineData") or p.get("inline_data")
        if inline and inline.get("data"):
            return base64.b64decode(inline["data"])
    raise RuntimeError(f"no inlineData in response: {json.dumps(data)[:500]}")


def build_index(manifest: list[dict[str, str]]) -> str:
    cards = []
    for e in manifest:
        cards.append(
            f'<figure><img src="{e["file"]}" alt="{e["slug"]}">'
            f'<figcaption><b>{e["slug"]}</b><br>'
            f'<i>{e.get("angle", "")}</i><br>'
            f'<small>{e["prompt"]}</small></figcaption></figure>'
        )
    return (
        '<!doctype html><html lang="fr"><head><meta charset="utf-8">'
        '<title>OttoKit concept 02 - 3 variations Nano Banana</title>'
        '<style>body{background:#0e0e11;color:#eee;font-family:system-ui,Segoe UI,sans-serif;'
        'padding:32px;max-width:1300px;margin:auto}'
        'h1{margin:0 0 8px;font-size:28px}p.lead{color:#aaa;margin:0 0 32px}'
        '.grid{display:grid;grid-template-columns:1fr;gap:32px}'
        'figure{margin:0;background:#1a1a1f;border-radius:12px;overflow:hidden;'
        'box-shadow:0 8px 24px rgba(0,0,0,.4)}'
        'img{width:100%;display:block;border-bottom:1px solid #2a2a30}'
        'figcaption{padding:20px;font-size:14px;line-height:1.5}'
        'figcaption b{color:#ffd400;font-size:16px}'
        'figcaption i{color:#9ac1ff;font-style:italic;display:block;margin:4px 0}'
        'figcaption small{color:#bbb;display:block;margin-top:8px}</style></head><body>'
        '<h1>OttoKit - concept #02 "Gratuit vs Zapier" - 3 variations</h1>'
        f'<p class="lead">Modele {MODEL}, 16:9 natif. Genere le {time.strftime("%Y-%m-%d %H:%M")}.</p>'
        f'<div class="grid">{"".join(cards)}</div></body></html>'
    )


def main() -> int:
    load_env()
    if not os.environ.get("GEMINI_API_KEY"):
        sys.exit("GEMINI_API_KEY missing from .env")
    OUT_DIR.mkdir(parents=True, exist_ok=True)

    manifest: list[dict[str, str]] = []
    for entry in VARIATIONS:
        out = OUT_DIR / f"{entry['slug']}.png"
        if out.exists() and out.stat().st_size > 0:
            print(f"-> {entry['slug']} (skipped, already exists)")
            manifest.append({**entry, "file": out.name})
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
        except Exception as e:  # noqa: BLE001
            print(f"   ! {type(e).__name__}: {e}")
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
        manifest.append({**entry, "file": out.name})
        print(f"   OK {out.name} ({len(img) // 1024} KB)")

    (OUT_DIR / "prompts-02-variations.json").write_text(
        json.dumps(manifest, indent=2, ensure_ascii=False), encoding="utf-8"
    )
    (OUT_DIR / "index-02-variations.html").write_text(
        build_index(manifest), encoding="utf-8"
    )

    print(f"\nDone. {len(manifest)}/{len(VARIATIONS)} variations generated.")
    print(f"Open: {OUT_DIR / 'index-02-variations.html'}")
    return 0 if manifest else 1


if __name__ == "__main__":
    sys.exit(main())
