#!/usr/bin/env python3
"""Generate 3 brand-aligned variations of concept #02 (Gratuit vs Zapier) via Gemini 2.5 Flash Image.

Applies schoolsWP brand rules (dark #12111F, primary green #00D400, accent pink #E668D4,
Nunito Sans bold vibes, clean editorial aesthetic — no clickbait chaos).
"""

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


BRAND_BLOCK = (
    "schoolsWP brand palette strictly applied: background color #12111F (very dark navy, almost black), "
    "primary highlight color #00D400 (vivid bright green), accent color #E668D4 (pink magenta), "
    "white text #FAFBFD. Typography style: Nunito Sans ultra-bold 700, thick clean geometric sans-serif, "
    "generous letter spacing. Overall aesthetic: editorial, clean, minimalist, professional but warm, "
    "generous negative space, no cheap clickbait chaos, no random glow explosions, no jagged tears, "
    "no torn paper effects. Premium YouTube thumbnail quality. Text must be perfectly legible with "
    "correct French typography and accents. No humans, no photos."
)


VARIATIONS: list[dict[str, str]] = [
    {
        "slug": "02-zapier-v4-typo-brand",
        "angle": "Typo frontale split, palette schoolsWP",
        "prompt": (
            "YouTube thumbnail, 16:9 aspect ratio. Vertical clean split in the middle (no jagged edge, "
            "just a subtle 2px pink magenta line). "
            "LEFT half (background #12111F, dark navy): word 'Zapier' in medium white font at top, "
            "below it the price '30 euros / mois' in large white bold font with a thin horizontal pink "
            "magenta (#E668D4) strikethrough line through the price. "
            "RIGHT half (background slightly lighter navy #1a1930 gradient): word 'OttoKit' in medium white "
            "font at top, below it the word 'GRATUIT' in huge vivid green (#00D400) ultra-bold sans-serif, "
            "with a subtle green glow behind it. "
            "Top center, small pill badge in pink magenta with white text: 'schoolsWP'. "
            + BRAND_BLOCK
        ),
    },
    {
        "slug": "02-zapier-v5-argent-brand",
        "angle": "Métaphore argent éditoriale, palette schoolsWP",
        "prompt": (
            "YouTube thumbnail, 16:9 aspect ratio. Dark navy background (#12111F) with very subtle "
            "radial gradient. "
            "LEFT SIDE: a small stack of euro banknotes tumbling and floating away to the left with "
            "soft motion blur, tinted slightly pink magenta (#E668D4) in the shadows. Below in small "
            "white caps: 'ZAPIER - 30 euros / mois'. "
            "RIGHT SIDE: a single clean modern coin standing upright, vivid green (#00D400) with a "
            "white lightning-bolt icon embossed on it, soft green glow halo around it. Below in small "
            "white caps: 'OTTOKIT - GRATUIT'. "
            "Centered top headline in white Nunito Sans ultra-bold: 'Garde ton argent.' — simple, clean, "
            "with a green underline accent. "
            "Small pink magenta 'schoolsWP' pill badge in the top-right corner. "
            + BRAND_BLOCK
        ),
    },
    {
        "slug": "02-zapier-v6-cartes-brand",
        "angle": "Comparatif 2 cartes éditorial, palette schoolsWP",
        "prompt": (
            "YouTube thumbnail, 16:9 aspect ratio. Dark navy background (#12111F) with a very subtle "
            "grid pattern. "
            "Two clean rectangular product cards side by side with rounded corners and generous padding. "
            "LEFT CARD (desaturated, thin pink magenta #E668D4 border, slightly smaller): "
            "white label 'Zapier' at top, three compact lines below each with a small pink magenta X "
            "followed by white text: 'Payant', 'Limite', 'Lent'. At bottom a small pink magenta price "
            "tag: '30 euros / mois'. "
            "RIGHT CARD (glowing vivid green #00D400 thick border, slightly larger and forward): "
            "white label 'OttoKit' at top, three compact lines below each with a small green check mark "
            "followed by white text: 'Gratuit', 'Illimite', 'Rapide'. At bottom a small green price "
            "tag: '0 euros'. "
            "Top center headline in white Nunito Sans ultra-bold: 'On compare.' — simple, clean, "
            "underlined in green. "
            "Small pink magenta 'schoolsWP' pill badge in the top-right corner. "
            + BRAND_BLOCK
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
            f'<i>{e.get("angle", "")}</i></figcaption></figure>'
        )
    return (
        '<!doctype html><html lang="fr"><head><meta charset="utf-8">'
        '<title>OttoKit #02 - 3 variations schoolsWP brand</title>'
        '<style>body{background:#12111F;color:#FAFBFD;'
        "font-family:'Nunito Sans',system-ui,Segoe UI,sans-serif;"
        'padding:32px;max-width:1300px;margin:auto}'
        'h1{margin:0 0 8px;font-size:28px;font-weight:800}'
        'p.lead{color:#9aa;margin:0 0 32px}'
        '.grid{display:grid;grid-template-columns:1fr;gap:32px}'
        'figure{margin:0;background:#1a1a2a;border-radius:12px;overflow:hidden;'
        'border:1px solid #2a2a40}'
        'img{width:100%;display:block;border-bottom:1px solid #2a2a40}'
        'figcaption{padding:20px;font-size:14px;line-height:1.5}'
        'figcaption b{color:#00D400;font-size:16px;font-weight:800}'
        'figcaption i{color:#E668D4;font-style:italic;display:block;margin:4px 0}</style></head><body>'
        '<h1>OttoKit - concept #02 "Gratuit vs Zapier" - branding schoolsWP (v4-v6)</h1>'
        f'<p class="lead">Palette #12111F + #00D400 + #E668D4. Modele {MODEL}. '
        f'Genere le {time.strftime("%Y-%m-%d %H:%M")}.</p>'
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

    (OUT_DIR / "prompts-02-variations-brand.json").write_text(
        json.dumps(manifest, indent=2, ensure_ascii=False), encoding="utf-8"
    )
    (OUT_DIR / "index-02-variations-brand.html").write_text(
        build_index(manifest), encoding="utf-8"
    )

    print(f"\nDone. {len(manifest)}/{len(VARIATIONS)} brand variations generated.")
    print(f"Open: {OUT_DIR / 'index-02-variations-brand.html'}")
    return 0 if manifest else 1


if __name__ == "__main__":
    sys.exit(main())
