"""Generate a brand-aligned hero image for a schoolsWP article.

Pipeline (hybride) :
  1. Fetch post (WP REST) -> title, excerpt, category, lang
  2. Derive variables (eyebrow, title HTML, subtitle, accent word)
  3. Generate central illustration via Nano Banana (Gemini 2.5 Flash Image, line-art)
  4. Inject in HTML template -> Playwright render 1920x1080

Outputs :
  content/articles/<slug>/captures-brand/hero-illustration.png  (1024x1024 Nano Banana)
  content/articles/<slug>/captures-brand/slide-00-hero.html     (HTML wrapper)
  content/articles/<slug>/captures-brand/slide-00-hero.png      (1920x1080 final hero)

Usage :
  python tools/article_hero/generate.py <slug_or_id> \
      [--concept "..."] [--accent-word "..."] [--eyebrow "..."] [--subtitle "..."] \
      [--title "..."] [--no-confirm] [--regen-illustration]
"""

from __future__ import annotations

import argparse
import base64
import json
import os
import re
import subprocess
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path

import requests
from dotenv import load_dotenv

ROOT = Path(__file__).resolve().parents[2]
load_dotenv(ROOT / ".env")

TEMPLATE_REF = ROOT / "content" / "articles" / "fluentcrm-automatisations-indispensables" / "captures-brand" / "_hero-template.html"
CAPTURE_MJS = ROOT / "tools" / "html-to-png" / "capture.mjs"

GEMINI_MODEL = "gemini-2.5-flash-image"
GEMINI_ENDPOINT = f"https://generativelanguage.googleapis.com/v1beta/models/{GEMINI_MODEL}:generateContent"

AUTH_PAIRS = [
    ("WP_API_USERNAME", "WP_API_PASSWORD"),
    ("WORDPRESS_USERNAME", "WORDPRESS_APP_PASSWORD"),
    ("WP_USER", "WP_APP_PASSWORD"),
    ("NOVAMIRA_USER", "NOVAMIRA_APP_PASSWORD"),
]


# -----------------------------------------------------------------------------
# Nano Banana prompt template
# -----------------------------------------------------------------------------

ILLUSTRATION_STYLE_GUIDE = """Square 1024x1024 minimalist editorial illustration.

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

Concept to illustrate: {concept}
"""


# -----------------------------------------------------------------------------
# WP REST helpers
# -----------------------------------------------------------------------------

def wp_auth() -> tuple[str, str]:
    for u_key, p_key in AUTH_PAIRS:
        u, p = os.environ.get(u_key), os.environ.get(p_key)
        if u and p:
            return (u, p)
    raise RuntimeError("No WP credentials in env (expected WP_API_USERNAME/PASSWORD)")


def wp_base() -> str:
    url = os.environ.get("WP_API_URL", "").rstrip("/")
    if not url:
        return "https://schoolswp.com/wp-json"
    if url.endswith("/wp-json"):
        return url
    if "/wp-json" in url:
        return url.split("/wp-json")[0] + "/wp-json"
    return url + "/wp-json"


def fetch_post(slug_or_id: str) -> dict:
    auth = wp_auth()
    base = wp_base()

    try:
        post_id = int(slug_or_id)
    except ValueError:
        slug = slug_or_id.strip("/").split("/")[-1]
        r = requests.get(f"{base}/wp/v2/posts?slug={slug}&context=edit", auth=auth, timeout=30)
        if r.status_code != 200 or not r.json():
            r = requests.get(f"{base}/wp/v2/pages?slug={slug}&context=edit", auth=auth, timeout=30)
            if r.status_code != 200 or not r.json():
                raise RuntimeError(f"Slug '{slug}' not found")
        post_id = r.json()[0]["id"]

    r = requests.get(f"{base}/wp/v2/posts/{post_id}?context=edit&_embed=1", auth=auth, timeout=30)
    if r.status_code == 404:
        r = requests.get(f"{base}/wp/v2/pages/{post_id}?context=edit&_embed=1", auth=auth, timeout=30)
    r.raise_for_status()
    return r.json()


def fetch_category_name(cat_id: int) -> str:
    auth = wp_auth()
    base = wp_base()
    r = requests.get(f"{base}/wp/v2/categories/{cat_id}", auth=auth, timeout=15)
    if r.status_code != 200:
        return ""
    return r.json().get("name", "")


# -----------------------------------------------------------------------------
# Variables derivation
# -----------------------------------------------------------------------------

def strip_html(html: str) -> str:
    text = re.sub(r"<[^>]+>", "", html)
    text = re.sub(r"&[a-z]+;", " ", text)
    return text.strip()


def derive_eyebrow(post: dict, primary_keyword: str | None = None) -> str:
    cats = post.get("categories", []) or []
    cat_name = ""
    for cid in cats:
        if cid <= 1:
            continue
        name = fetch_category_name(cid)
        if name and name.lower() not in {"non classe", "non classé", "uncategorized"}:
            cat_name = name
            break
    label = primary_keyword or "Guide"
    if cat_name:
        return f"{cat_name} · {label}"
    return f"Guide · {label}"


def derive_subtitle(post: dict) -> str:
    excerpt = (post.get("excerpt") or {}).get("rendered", "")
    if excerpt:
        s = strip_html(excerpt)
        if len(s) > 180:
            s = s[:177].rsplit(" ", 1)[0] + "..."
        return s
    yoast = post.get("yoast_head_json") or {}
    if isinstance(yoast, dict) and yoast.get("description"):
        return yoast["description"][:180]
    return ""


def derive_title_with_accent(title: str, accent_word: str | None = None) -> tuple[str, str]:
    """Returns (title_html_with_strong, chosen_accent_word)."""
    plain = strip_html(title)
    if accent_word:
        target = accent_word
    else:
        # Heuristic: prefer last capitalized non-stopword (often the topic), else longest noun-like word
        tokens = plain.split()
        candidates = [t for t in tokens if len(t) > 3 and t[0].isupper()]
        target = candidates[-1] if candidates else max(tokens, key=len)

    # Replace first occurrence of target (case-insensitive, preserve case)
    pattern = re.compile(re.escape(target), re.IGNORECASE)
    html = pattern.sub(f"<strong>{target}</strong>", plain, count=1)
    return html, target


# -----------------------------------------------------------------------------
# Nano Banana illustration
# -----------------------------------------------------------------------------

def gemini_api_key() -> str:
    k = os.environ.get("GEMINI_API_KEY")
    if k:
        return k
    raise RuntimeError("GEMINI_API_KEY missing in env")


def generate_illustration(prompt: str, out_path: Path, max_retries: int = 3) -> None:
    key = gemini_api_key()
    body = json.dumps({
        "contents": [{"parts": [{"text": prompt}]}],
        "generationConfig": {"responseModalities": ["IMAGE"]},
    }).encode("utf-8")

    last_err = ""
    for attempt in range(1, max_retries + 1):
        req = urllib.request.Request(
            GEMINI_ENDPOINT,
            data=body,
            headers={"x-goog-api-key": key, "Content-Type": "application/json"},
            method="POST",
        )
        try:
            with urllib.request.urlopen(req, timeout=180) as resp:
                payload = json.loads(resp.read().decode("utf-8"))
            parts = payload["candidates"][0]["content"]["parts"]
            b64 = next(p["inlineData"]["data"] for p in parts if "inlineData" in p)
            out_path.parent.mkdir(parents=True, exist_ok=True)
            out_path.write_bytes(base64.b64decode(b64))
            return
        except urllib.error.HTTPError as exc:
            err_body = exc.read().decode("utf-8", errors="replace")
            last_err = f"HTTP {exc.code}: {err_body[:300]}"
            if attempt < max_retries and (exc.code == 429 or exc.code >= 500):
                print(f"  rate-limited (attempt {attempt}/{max_retries}), backing off 45s...")
                time.sleep(45)
                continue
            raise RuntimeError(last_err)
        except (KeyError, IndexError, StopIteration) as exc:
            raise RuntimeError(f"No image in Gemini response: {exc}")


# -----------------------------------------------------------------------------
# HTML hero rendering
# -----------------------------------------------------------------------------

def render_hero(slug: str, eyebrow: str, title_html: str, subtitle: str,
                illustration_path: Path, out_dir: Path) -> Path:
    template = TEMPLATE_REF.read_text(encoding="utf-8")

    # The reference template hardcodes the FluentCRM content. We surgically replace
    # the three editable zones rather than re-engineer the template.
    html = template
    html = html.replace(
        '<span class="badge"><span class="badge-dot"></span> Guide complet · FluentCRM</span>',
        f'<span class="badge"><span class="badge-dot"></span> {eyebrow}</span>',
    )
    html = html.replace(
        '<h1 class="title">10 <strong>automatisations</strong> FluentCRM indispensables</h1>',
        f'<h1 class="title">{title_html}</h1>',
    )
    html = html.replace(
        '<p class="subtitle">Le guide complet des workflows que je fais tourner sur schoolsWP pour transformer WordPress en moteur marketing autonome.</p>',
        f'<p class="subtitle">{subtitle}</p>',
    )

    # Illustration path -> file:// URL
    illu_url = "file:///" + str(illustration_path).replace("\\", "/")
    html = html.replace("__IMAGE_PATH__", illu_url)
    html = html.replace('src="hero-fluentcrm-automatisation.png"', f'src="{illu_url}"')
    # Some templates use __TITLE__ placeholder
    html = html.replace("__TITLE__", strip_html(title_html))

    out_dir.mkdir(parents=True, exist_ok=True)
    slide_html = out_dir / "slide-00-hero.html"
    slide_html.write_text(html, encoding="utf-8")

    # Render via capture.mjs
    cmd = [
        "node",
        str(CAPTURE_MJS),
        str(out_dir),
        "--width=1920",
        "--height=1080",
        "--scale=1",
        "--pattern=slide-00-hero",
    ]
    print(f"Running: {' '.join(cmd)}")
    res = subprocess.run(cmd, capture_output=True, text=True)
    if res.returncode != 0:
        print(res.stdout)
        print(res.stderr, file=sys.stderr)
        raise RuntimeError(f"capture.mjs failed with code {res.returncode}")
    print(res.stdout)

    final = out_dir / "slide-00-hero.png"
    if not final.exists():
        raise RuntimeError(f"Expected output not found: {final}")
    return final


# -----------------------------------------------------------------------------
# CLI
# -----------------------------------------------------------------------------

def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("slug_or_id")
    ap.add_argument("--title", help="Override title text (default: post title)")
    ap.add_argument("--accent-word", help="Word to render in brand green inside the title")
    ap.add_argument("--eyebrow", help="Override eyebrow badge text")
    ap.add_argument("--subtitle", help="Override subtitle")
    ap.add_argument("--concept", help="Illustration concept for Nano Banana (1-2 sentences). REQUIRED unless --regen-illustration is skipped.")
    ap.add_argument("--no-confirm", action="store_true", help="Skip pre-generation confirmation")
    ap.add_argument("--skip-illustration", action="store_true", help="Skip Nano Banana, reuse existing hero-illustration.png if present")
    args = ap.parse_args()

    post = fetch_post(args.slug_or_id)
    slug = post.get("slug", args.slug_or_id)
    raw_title = strip_html((post.get("title") or {}).get("rendered", ""))
    print(f"\n[POST] id={post.get('id')}  status={post.get('status')}  slug={slug}")
    print(f"[POST] title: {raw_title}")

    final_title = args.title or raw_title
    title_html, accent_used = derive_title_with_accent(final_title, args.accent_word)
    eyebrow = args.eyebrow or derive_eyebrow(post, primary_keyword=accent_used)
    subtitle = args.subtitle if args.subtitle is not None else derive_subtitle(post)

    print("\n[VARIABLES]")
    print(f"  eyebrow:    {eyebrow}")
    print(f"  title HTML: {title_html}")
    print(f"  accent:     {accent_used}")
    print(f"  subtitle:   {subtitle}")

    if not subtitle:
        print("\n[WARN] subtitle is empty. Provide one via --subtitle for a proper hero.", file=sys.stderr)

    art_dir = ROOT / "content" / "articles" / slug / "captures-brand"
    illu_path = art_dir / "hero-illustration.png"

    if not args.skip_illustration:
        if not args.concept:
            print("\n[ERR] --concept required (unless --skip-illustration). Example:", file=sys.stderr)
            print('  --concept "central node connected to 5 user avatars by clean curved lines, one avatar with a green online dot"', file=sys.stderr)
            return 2

        full_prompt = ILLUSTRATION_STYLE_GUIDE.format(concept=args.concept)
        print("\n[NANO BANANA] prompt:")
        print("-" * 60)
        print(full_prompt)
        print("-" * 60)

        if not args.no_confirm:
            ans = input("\nProceed with generation ? [y/N] ").strip().lower()
            if ans != "y":
                print("Aborted.")
                return 0

        print(f"\n[NANO BANANA] generating illustration -> {illu_path}")
        generate_illustration(full_prompt, illu_path)
        size_kb = illu_path.stat().st_size // 1024
        print(f"[NANO BANANA] OK ({size_kb} KB)")
    else:
        if not illu_path.exists():
            print(f"[ERR] --skip-illustration set but {illu_path} not found", file=sys.stderr)
            return 3

    print(f"\n[RENDER] composing HTML hero -> {art_dir}")
    final_png = render_hero(slug, eyebrow, title_html, subtitle, illu_path, art_dir)
    print(f"\n[OK] Hero ready: {final_png}")
    print(f"[OK] Size: {final_png.stat().st_size // 1024} KB")
    return 0


if __name__ == "__main__":
    sys.exit(main())
