#!/usr/bin/env python3
"""Extract literal FR paragraphs/list-items still in post 343156 raw content.

Scans <p>...</p> and <li>...</li> blocks, returns those whose
plaintext (markup-stripped) contains FR-only markers (te /tu /vraiment / etc.).
Writes a JSON list [{kind, raw, plain}] to live-fr-blocks.json for hand-translation.
"""

import base64
import json
import re
import sys
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SETTINGS = ROOT / ".claude" / "settings.local.json"
OUT = ROOT / "content" / "audits" / "flyingpress-wp-rocket-comparison-en" / "2026-05-12" / "live-fr-blocks.json"
POST_ID = 343156

# Markers that strongly indicate French (case-sensitive on diacritics)
FR_MARKERS = re.compile(
    r"\b(tu |Tu |ton |ta |tes |te |Te |toi |"
    r"c'est |C'est |C'est-à-dire |Ce |des |"
    r"très|Très|aujourd'hui|"
    r"H[ée]bergeur|Compression|Lazy Loading|"
    r"Pr[ée]visualisation|"
    r"LiteSpeed Cache|W3 Total Cache|Perfmatters|NitroPack|"
    r"Notre verdict|Pour 1 site|Pour plusieurs sites|"
    r"Choisis|R[ée]sum[ée]|"
    r"plug-?in|"
    r"Toujours ind[ée]cis|"
    r"r[èeé]glage|am[ée]lior|"
    r"\s(et|ou|dans|pour|avec|sur|sans|de|du|la|le|les|un|une|en)\s)"
)

# Definitive EN-only words (if present, paragraph is likely EN)
EN_MARKERS = re.compile(
    r"\b(you|your|both|with|and|the |is |are |to |of )", re.IGNORECASE
)


def strip_tags(s):
    return re.sub(r"<[^>]+>", "", s)


def is_likely_fr(plain):
    """A paragraph is FR if FR markers found AND (no EN markers OR much more FR than EN)."""
    fr_count = len(FR_MARKERS.findall(plain))
    en_count = len(EN_MARKERS.findall(plain))
    return fr_count >= 2 and fr_count > en_count


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

    blocks = []
    # Capture each <p>...</p>, <li>...</li>, <h2>...</h2>, <h3>...</h3>
    for kind in ("p", "li", "h2", "h3", "td"):
        for m in re.finditer(rf"<{kind}\b[^>]*>(.*?)</{kind}>", raw, flags=re.DOTALL):
            inner = m.group(1)
            plain = strip_tags(inner).strip()
            if not plain:
                continue
            if is_likely_fr(plain):
                blocks.append({"kind": kind, "raw_inner": inner, "plain": plain[:200]})

    print(f"[info] {len(blocks)} FR-leaning blocks found\n")
    for i, b in enumerate(blocks, 1):
        print(f"#{i:02d} <{b['kind']}> [{len(b['raw_inner'])} chars]")
        print(f"      plain: {b['plain'][:150]}")
        print()

    OUT.write_text(json.dumps(blocks, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"[done] wrote {OUT.name} ({len(blocks)} blocks)")


if __name__ == "__main__":
    main()
