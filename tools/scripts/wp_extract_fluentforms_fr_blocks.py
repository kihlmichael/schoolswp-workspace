#!/usr/bin/env python3
"""Extract literal FR paragraphs/list-items still in post 54709 (fluent-forms /en/).

Same approach as wp_extract_flyingpress_fr_blocks.py but for the fluent-forms post.
Writes a JSON list of FR-leaning blocks to live-fr-blocks.json for hand-translation.
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
OUT = OUT_DIR / "live-fr-blocks.json"
POST_ID = 54709

FR_MARKERS = re.compile(
    r"\b(tu |Tu |ton |ta |tes |te |Te |toi |"
    r"vous |Vous |votre |Votre |vos |"
    r"c'est |C'est |"
    r"très|Très|aujourd'hui|"
    r"avec |sans |dans |pour |"
    r"plug-?in|"
    r"\s(et|ou|dans|pour|avec|sur|sans|de|du|la|le|les|un|une|en|ne|pas|au|aux|qui|que|car|mais|si|ainsi)\s)"
)

EN_MARKERS = re.compile(
    r"\b(you|your|both|with|and|the |is |are |to |of |from|when|where|how|what|which|will|been)",
    re.IGNORECASE,
)


def strip_tags(s):
    return re.sub(r"<[^>]+>", "", s)


def is_likely_fr(plain):
    fr = len(FR_MARKERS.findall(plain))
    en = len(EN_MARKERS.findall(plain))
    return fr >= 2 and fr > en


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
    for kind in ("p", "li", "h2", "h3", "h4", "td"):
        for m in re.finditer(rf"<{kind}\b[^>]*>(.*?)</{kind}>", raw, flags=re.DOTALL):
            inner = m.group(1)
            plain = strip_tags(inner).strip()
            if not plain:
                continue
            if is_likely_fr(plain):
                blocks.append({"kind": kind, "raw_inner": inner, "plain": plain[:250]})

    print(f"[info] {len(blocks)} FR-leaning blocks found\n")
    for i, b in enumerate(blocks, 1):
        print(f"#{i:02d} <{b['kind']}> [{len(b['raw_inner'])} chars]")
        print(f"      plain: {b['plain'][:200]}")
        print()

    OUT.write_text(json.dumps(blocks, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"[done] wrote {OUT.name} ({len(blocks)} blocks)")


if __name__ == "__main__":
    main()
