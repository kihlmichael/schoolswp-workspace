#!/usr/bin/env python3
"""Audit Polylang language alignment across all /de/ posts on schoolswp.com.

For each DE post:
- Fetch raw content via WP REST (context=edit)
- Score language: DE vs FR vs EN markers
- Flag pages with significant FR or EN pollution (paragraph-level OR attr-level)

Companion to wp_audit_en_polylang_lang.py.
"""

import base64
import json
import re
import urllib.error
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SETTINGS = ROOT / ".claude" / "settings.local.json"
OUT_DIR = ROOT / "content" / "audits" / "polylang-de-mass" / "2026-05-13"
OUT_DIR.mkdir(parents=True, exist_ok=True)
OUT_FILE = OUT_DIR / "audit-report.json"

# DE markers (function words, case-sensitive on umlauts)
DE_MARKERS = re.compile(
    r"\b(und|der|die|das|den|dem|des|"
    r"mit|ohne|für|auf|von|zu|bei|nach|über|unter|durch|"
    r"ich|du|Sie|wir|ihr|"
    r"ist|sind|war|waren|habe|haben|hat|hast|"
    r"wenn|weil|aber|auch|nicht|noch|schon|sehr|"
    r"kann|muss|soll|wird|werden|sollte|könnte|"
    r"Ihre|Ihrer|Ihren|deine|dein|"
    r"ein|eine|einen|einer|einem|"
    r"sich|man|alle|kein|jede)\b"
)

# FR markers (paragraph + attr level)
FR_MARKERS = re.compile(
    r"\b(tu |Tu |ton |ta |tes |te |Te |toi |"
    r"vous |Vous |votre |Votre |vos |"
    r"c'est |C'est |"
    r"très|Très|aujourd'hui|"
    r"avec|sans|dans|pour|sur|"
    r"plug-?in|"
    r"\s(et|ou|dans|pour|avec|sur|sans|de|du|la|le|les|un|une|en|ne|pas|au|aux|qui|que|car|mais|si|ainsi)\s)"
)

# EN markers (typical function words)
EN_MARKERS = re.compile(
    r"\b(you|your|both|with|and|the|is|are|to|of|from|when|where|how|what|which|will|been|that|this|these|those|for|here|there|why)\b",
    re.IGNORECASE,
)


def load_creds():
    data = json.loads(SETTINGS.read_text(encoding="utf-8"))
    env = data.get("env", {})
    return env["WP_API_USERNAME"], env["WP_API_PASSWORD"]


def auth_header(user, pw):
    return "Basic " + base64.b64encode(f"{user}:{pw}".encode()).decode()


def http_get(url, user, pw, timeout=120):
    req = urllib.request.Request(
        url,
        headers={"Authorization": auth_header(user, pw), "Accept": "application/json"},
    )
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            return resp.status, json.loads(resp.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        return e.code, e.read().decode("utf-8", errors="replace")
    except Exception as e:
        return 0, str(e)


def list_de_posts(user, pw, per_page=100):
    posts = []
    page = 1
    while True:
        url = (
            f"https://schoolswp.com/wp-json/wp/v2/posts"
            f"?per_page={per_page}&page={page}&context=edit&_fields=id,slug,title,link,modified,content,status"
        )
        status, data = http_get(url, user, pw, timeout=180)
        if status != 200:
            print(f"[error] page {page}: HTTP {status} - {str(data)[:200]}")
            break
        if not data or len(data) == 0:
            break
        for p in data:
            link = p.get("link", "")
            if "/de/" in link:
                posts.append(p)
        if len(data) < per_page:
            break
        page += 1
        if page > 30:
            break
    return posts


def strip_tags(s):
    return re.sub(r"<[^>]+>", " ", s)


def score_languages(text):
    plain = strip_tags(text)
    de = len(DE_MARKERS.findall(plain))
    fr = len(FR_MARKERS.findall(plain))
    en = len(EN_MARKERS.findall(plain))
    total = de + fr + en
    if total < 5:
        return ("EMPTY_OR_UNKNOWN", de, fr, en, 0.0, 0.0)
    fr_ratio = fr / total
    en_ratio = en / total
    de_ratio = de / total
    if de_ratio > 0.5:
        label = "DE"
    elif fr_ratio > 0.3:
        label = "FR_HEAVY"
    elif en_ratio > 0.3:
        label = "EN_HEAVY"
    elif fr_ratio > 0.1 or en_ratio > 0.15:
        label = "MIXED"
    else:
        label = "UNCLEAR"
    return (label, de, fr, en, fr_ratio, en_ratio)


def detect_title_lang(title):
    if not title:
        return "EMPTY"
    fr_words = ["pour", "le", "la", "les", "et", "ou", "des", "du", "comparatif", "guide", "avis", "test", "comment", "pourquoi", "quel", "tutoriel"]
    en_words = ["the", "for", "and", "or", "with", "review", "how", "why", "what", "best", "vs", "tutorial"]
    de_words = ["der", "die", "das", "und", "für", "mit", "ohne", "ist", "sind", "wie", "warum", "was", "welche", "test", "vergleich", "rezension", "anleitung", "der beste", "die besten"]
    t_lower = title.lower()
    fr = sum(1 for w in fr_words if f" {w} " in f" {t_lower} ")
    en = sum(1 for w in en_words if f" {w} " in f" {t_lower} ")
    de = sum(1 for w in de_words if f" {w} " in f" {t_lower} ")
    scores = [("FR", fr), ("EN", en), ("DE", de)]
    scores.sort(key=lambda x: -x[1])
    if scores[0][1] == 0:
        return "PROPER_NAMES_OR_UNKNOWN"
    if scores[0][1] > scores[1][1]:
        return scores[0][0]
    return "MIXED"


def main():
    user, pw = load_creds()
    print("[info] Listing all DE posts via WP REST...")
    posts = list_de_posts(user, pw)
    print(f"[info] Found {len(posts)} posts with /de/ in link")

    report = []
    for p in posts:
        pid = p["id"]
        title_raw = p.get("title", {}).get("raw") or p.get("title", {}).get("rendered", "")
        content_raw = p.get("content", {}).get("raw", "")
        link = p.get("link", "")

        title_lang = detect_title_lang(title_raw)
        body_lang, de_c, fr_c, en_c, fr_ratio, en_ratio = score_languages(content_raw)

        is_bugged = (
            body_lang in ("FR_HEAVY", "EN_HEAVY", "MIXED")
            or title_lang in ("FR", "EN")
        )

        report.append({
            "post_id": pid,
            "link": link,
            "title_raw": title_raw,
            "title_lang_estimate": title_lang,
            "body_lang_estimate": body_lang,
            "de_markers_count": de_c,
            "fr_markers_count": fr_c,
            "en_markers_count": en_c,
            "fr_pollution_ratio": round(fr_ratio, 3),
            "en_pollution_ratio": round(en_ratio, 3),
            "content_length": len(content_raw),
            "modified": p.get("modified"),
            "is_bugged_candidate": is_bugged,
        })

    # Sort: bugged first, then by max(fr_ratio, en_ratio) descending
    report.sort(
        key=lambda x: (x["is_bugged_candidate"], max(x["fr_pollution_ratio"], x["en_pollution_ratio"])),
        reverse=True,
    )

    bugged = [r for r in report if r["is_bugged_candidate"]]
    print(f"\n[stats] Total DE posts audited: {len(report)}")
    print(f"[stats] Candidates with FR or EN pollution: {len(bugged)}")
    print()

    print("=== Top bugged candidates ===\n")
    for r in bugged[:20]:
        pollution = max(r["fr_pollution_ratio"], r["en_pollution_ratio"]) * 100
        print(f"  [{r['body_lang_estimate']:15}] FR%={r['fr_pollution_ratio']*100:5.1f} EN%={r['en_pollution_ratio']*100:5.1f} | T={r['title_lang_estimate']:10} | {r['link']}")
        print(f"       title: {r['title_raw'][:100]}")
        print()

    OUT_FILE.write_text(json.dumps(report, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"[done] Report written to {OUT_FILE}")
    print(f"[done] {len(bugged)} bugged candidate(s) found")


if __name__ == "__main__":
    main()
