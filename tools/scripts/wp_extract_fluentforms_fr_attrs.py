#!/usr/bin/env python3
"""Extract FR-residual content from post 54709 fluent-forms /en/.

Targets 3 categories where Polylang did NOT translate:
1. <figcaption>...</figcaption> inner content
2. alt="..." attributes on <img>
3. title="..." attributes on <a>

For each, detects FR marker presence and outputs a structured JSON.
"""

import base64
import json
import re
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SETTINGS = ROOT / ".claude" / "settings.local.json"
OUT_DIR = ROOT / "content" / "audits" / "fluent-forms-en" / "2026-05-12"
OUT_DIR.mkdir(parents=True, exist_ok=True)
OUT = OUT_DIR / "fr-attrs-and-captions.json"
POST_ID = 54709

FR_WORDS = re.compile(
    r"\b(formulaire|cr[ée]ation|capture|cran|interface|tableau|exemple|gestion|"
    r"optimisez|votre|vos|notre|avec|sans|pour|dans|sur|"
    r"performant|conversationnel|sondage|enqu[êe]te|satisfaction|plainte|"
    r"activation|s[ée]lection|d['']|du|de la|des|une|un |le |la |les |"
    r"choix|outils|liste|diffusion|champs|saisie|boutons|radio|texte|"
    r"meilleur|plug-in|sites?|bri[èe]vement|action|objectif|connexion|"
    r"personnalis[ée]s?|marketing|mod[èe]les|envoy[ée]|graphique)",
    re.IGNORECASE,
)


def has_fr(text):
    return len(FR_WORDS.findall(text)) >= 1


def load_creds():
    data = json.loads(SETTINGS.read_text(encoding="utf-8"))
    env = data.get("env", {})
    return env["WP_API_USERNAME"], env["WP_API_PASSWORD"]


def fetch_raw(user, pw):
    url = f"https://schoolswp.com/wp-json/wp/v2/posts/{POST_ID}?context=edit"
    req = urllib.request.Request(
        url,
        headers={
            "Authorization": "Basic " + base64.b64encode(f"{user}:{pw}".encode()).decode(),
            "Accept": "application/json",
        },
    )
    with urllib.request.urlopen(req, timeout=120) as resp:
        return json.loads(resp.read().decode("utf-8"))["content"]["raw"]


def main():
    user, pw = load_creds()
    raw = fetch_raw(user, pw)
    print(f"[info] raw len={len(raw)}")

    figcaptions = []
    for m in re.finditer(r"<figcaption[^>]*>(.*?)</figcaption>", raw, flags=re.DOTALL):
        inner = m.group(1)
        if has_fr(inner):
            figcaptions.append(inner)

    alts = []
    for m in re.finditer(r'alt="([^"]+)"', raw):
        val = m.group(1)
        if has_fr(val):
            alts.append(val)

    titles = []
    for m in re.finditer(r'title="([^"]+)"', raw):
        val = m.group(1)
        if has_fr(val):
            titles.append(val)

    print(f"\n[stats] figcaptions FR: {len(figcaptions)}")
    print(f"[stats] alt attrs FR: {len(alts)}")
    print(f"[stats] title attrs FR: {len(titles)}\n")

    print("=== FIGCAPTIONS ===")
    for i, f in enumerate(figcaptions, 1):
        print(f"#{i}: {f[:200]}")
        print()

    print("=== ALT ATTRIBUTES ===")
    for i, a in enumerate(alts, 1):
        print(f"#{i}: {a}")
    print()

    print("=== TITLE ATTRIBUTES ===")
    for i, t in enumerate(titles, 1):
        print(f"#{i}: {t}")

    payload = {
        "post_id": POST_ID,
        "figcaptions": figcaptions,
        "alt_attrs": list(set(alts)),
        "title_attrs": list(set(titles)),
        "total_units": len(figcaptions) + len(set(alts)) + len(set(titles)),
    }
    OUT.write_text(json.dumps(payload, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"\n[done] wrote {OUT.name} (total {payload['total_units']} unique units)")


if __name__ == "__main__":
    main()
