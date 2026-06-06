#!/usr/bin/env python3
"""Audit Polylang language alignment across all /en/ posts on schoolswp.com.

For each EN post:
- Fetch raw content via WP REST (context=edit)
- Check Title (post_title) language
- Score body language via FR markers vs EN markers
- Detect mixed-language pages (bug Polylang body translation incomplete)

Skips post 343156 (already fixed in Action #1).
Outputs JSON report sorted by FR-pollution score (most contaminated first).
"""

import base64
import json
import re
import sys
import urllib.error
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SETTINGS = ROOT / ".claude" / "settings.local.json"
OUT_DIR = ROOT / "content" / "audits" / "polylang-en-mass" / "2026-05-12"
OUT_DIR.mkdir(parents=True, exist_ok=True)
OUT_FILE = OUT_DIR / "audit-report.json"

POST_ID_DONE = 343156  # FlyingPress, already fixed in Action #1

# FR markers (case-sensitive on accents to avoid EN false positives)
FR_MARKERS = re.compile(
    r"\b(tu |Tu |ton |ta |tes |te |Te |toi |"
    r"vous |Vous |votre |Votre |"
    r"c'est |C'est |"
    r"très|Très|aujourd'hui|"
    r"dès |Dès |"
    r"Pour |pour |"
    r"avec |Avec |"
    r"sans |Sans |"
    r"déjà|Déjà|"
    r"plus de |moins de |"
    r"Choisis|Notre verdict|"
    r"Hébergeur|Compression|"
    r"Bonne nouvelle|Toujours indécis|"
    r"r[èeé]glage|am[ée]lior|"
    r"\s(et|ou|dans|sur|sans|de|du|la|le|les|un|une|en|ne|pas|au|aux|qui|que|car|mais|si|ainsi)\s)"
)

EN_MARKERS = re.compile(
    r"\b(you |your |both |with |and |the |is |are |to |of |this |that |these |those |for |from |here |there |when |where |why |how |what |which |will |has |have |had |were |was |been )",
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
        headers={
            "Authorization": auth_header(user, pw),
            "Accept": "application/json",
        },
    )
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            return resp.status, json.loads(resp.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        return e.code, e.read().decode("utf-8", errors="replace")
    except Exception as e:
        return 0, str(e)


def list_en_posts(user, pw, per_page=100):
    """List published posts where slug starts with /en/ or lang=en."""
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
            if "/en/" in link:
                posts.append(p)
        if len(data) < per_page:
            break
        page += 1
        if page > 20:  # safety
            break
    return posts


def strip_tags(s):
    return re.sub(r"<[^>]+>", " ", s)


def detect_language(text):
    """Return (lang_label, fr_count, en_count, fr_score)."""
    plain = strip_tags(text)
    fr = len(FR_MARKERS.findall(plain))
    en = len(EN_MARKERS.findall(plain))
    total = fr + en
    if total < 5:
        return ("EMPTY_OR_UNKNOWN", fr, en, 0.0)
    fr_ratio = fr / total
    if fr_ratio > 0.4:
        return ("FR_HEAVY", fr, en, fr_ratio)
    elif fr_ratio > 0.15:
        return ("MIXED", fr, en, fr_ratio)
    else:
        return ("EN", fr, en, fr_ratio)


def detect_title_lang(title):
    """Crude language detection on a short title."""
    if not title:
        return "EMPTY"
    fr_words = ["pour", "le", "la", "les", "et", "ou", "des", "du", "comparatif", "guide", "avis", "test", "comment", "pourquoi", "quel", "quelle", "tutoriel"]
    en_words = ["the", "for", "and", "or", "with", "review", "guide", "how", "why", "what", "best", "vs", "tutorial", "compare"]
    t_lower = title.lower()
    fr = sum(1 for w in fr_words if f" {w} " in f" {t_lower} ")
    en = sum(1 for w in en_words if f" {w} " in f" {t_lower} ")
    if fr > en:
        return "FR"
    if en > fr:
        return "EN"
    return "MIXED_OR_PROPER_NAMES"


def main():
    user, pw = load_creds()
    print("[info] Listing all EN posts via WP REST...")
    posts = list_en_posts(user, pw)
    print(f"[info] Found {len(posts)} posts with /en/ in link")

    report = []
    for p in posts:
        pid = p["id"]
        if pid == POST_ID_DONE:
            continue
        title_rendered = p.get("title", {}).get("rendered", "")
        title_raw = p.get("title", {}).get("raw") or title_rendered
        content_raw = p.get("content", {}).get("raw", "")
        link = p.get("link", "")

        title_lang = detect_title_lang(title_raw)
        body_lang, fr_count, en_count, fr_ratio = detect_language(content_raw)

        is_bugged = body_lang in ("FR_HEAVY", "MIXED") or title_lang == "FR"

        report.append({
            "post_id": pid,
            "link": link,
            "title_raw": title_raw,
            "title_lang_estimate": title_lang,
            "body_lang_estimate": body_lang,
            "fr_markers_count": fr_count,
            "en_markers_count": en_count,
            "fr_pollution_ratio": round(fr_ratio, 3),
            "content_length": len(content_raw),
            "modified": p.get("modified"),
            "is_bugged_candidate": is_bugged,
        })

    # Sort by fr_pollution_ratio descending (worst first)
    report.sort(key=lambda x: (x["is_bugged_candidate"], x["fr_pollution_ratio"]), reverse=True)

    bugged = [r for r in report if r["is_bugged_candidate"]]
    print(f"\n[stats] Total EN posts audited: {len(report)}")
    print(f"[stats] Candidates with FR bug: {len(bugged)}")
    print()

    print("=== Top bugged candidates (FR_HEAVY or MIXED body, or FR title) ===\n")
    for r in bugged[:15]:
        print(f"  [{r['body_lang_estimate']:15}] FR%={r['fr_pollution_ratio']*100:5.1f} | T={r['title_lang_estimate']:25} | {r['link']}")
        print(f"       title: {r['title_raw'][:100]}")
        print()

    OUT_FILE.write_text(json.dumps(report, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"[done] Report written to {OUT_FILE}")
    print(f"[done] {len(bugged)} bugged candidate(s) found")


if __name__ == "__main__":
    main()
