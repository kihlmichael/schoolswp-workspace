#!/usr/bin/env python3
"""
Three pre-enrichment checks for post 2871653:
1. Verify existence of internal mailing candidates on schoolswp.com
2. Read content of Ninja Tables table 2873004 (REST: /ninja-tables/v1.0/items/{id})
3. Extract Kadence accordion (FAQ) panes Q/A summary
"""

import base64
import json
import re
import sys
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")

ROOT = Path(__file__).resolve().parents[2]
SETTINGS = ROOT / ".claude" / "settings.local.json"
SRC = ROOT / "content" / "articles" / "_workspace" / "post-2871653-current.json"
SITE = "https://schoolswp.com"


def load_creds():
    env = json.loads(SETTINGS.read_text(encoding="utf-8")).get("env", {})
    return env["WP_API_USERNAME"], env["WP_API_PASSWORD"]


def auth():
    u, p = load_creds()
    return "Basic " + base64.b64encode(f"{u}:{p}".encode()).decode()


def http_get(url):
    req = urllib.request.Request(url, headers={
        "Authorization": auth(),
        "Accept": "application/json",
        "User-Agent": "schoolswp-fetcher/1.0",
    })
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            return r.status, r.read().decode("utf-8")
    except urllib.error.HTTPError as e:
        return e.code, e.read().decode("utf-8", errors="replace")[:600]


# ----- 1. Internal mailing candidates -----
print("=" * 80)
print("INTERNAL MAILING CANDIDATES (via WP REST search)")
print("=" * 80)
candidates = [
    "fluentcart",
    "tutorlms",
    "tutor-lms",
    "tutor lms",
    "ottokit",
    "surecart",
    "memberpress",
    "buddyboss",
    "fluentboards",
    "fluent boards",
    "fluentsmtp",
    "fluent smtp",
    "amazon ses",
    "polylang",
    "double opt-in",
]
for q in candidates:
    enc = urllib.parse.quote(q)
    code, body = http_get(f"{SITE}/wp-json/wp/v2/search?search={enc}&per_page=3&type=post&subtype=post")
    if code != 200:
        print(f"  [{q}] HTTP {code}")
        continue
    items = json.loads(body) if body.startswith("[") else []
    if not items:
        print(f"  [{q}] NO RESULT")
        continue
    print(f"  [{q}]")
    for it in items[:3]:
        url_path = it.get("url", "").replace(SITE, "")
        print(f"     - {url_path}  ::  {it.get('title','')[:80]}")

# ----- 2. Ninja Tables 2873004 -----
print()
print("=" * 80)
print("NINJA TABLES 2873004 content")
print("=" * 80)
# Try a few common endpoints
for url in [
    f"{SITE}/wp-json/ninja-tables/v1.0/items/2873004",
    f"{SITE}/wp-json/ninja-tables/public/tables/2873004",
    f"{SITE}/wp-json/wp/v2/ninja-tables/2873004",
]:
    code, body = http_get(url)
    print(f"  {url}")
    print(f"  -> HTTP {code}")
    if code == 200:
        try:
            d = json.loads(body)
            print("  KEYS:", list(d.keys())[:20] if isinstance(d, dict) else f"list[{len(d)}]")
            print("  PREVIEW:")
            print("  " + json.dumps(d, ensure_ascii=False)[:2000])
        except Exception:
            print("  RAW (first 600c):", body[:600])
        break
    else:
        print(f"  ERROR (first 200c): {body[:200]}")
    print()

# ----- 3. Kadence accordion (FAQ) -----
print()
print("=" * 80)
print("KADENCE ACCORDION FAQ (Q/A pairs)")
print("=" * 80)
c = json.loads(SRC.read_text(encoding="utf-8"))["content"]["raw"]
# kadence/accordion contains kadence/pane (the actual Q/A items)
# Find FAQ H2 first
faq_m = re.search(r"<h2[^>]*>\s*Questions fréquentes[^<]*</h2>", c, re.IGNORECASE)
faq_start = faq_m.start() if faq_m else 0
faq_section = c[faq_start:]

panes = re.findall(
    r'<!--\s*wp:kadence/pane[^-]*"title":"([^"]+)"[^-]*-->(.*?)<!--\s*/wp:kadence/pane\s*-->',
    faq_section, re.DOTALL,
)
print(f"Found {len(panes)} accordion panes inside FAQ block.")
for i, (title, body) in enumerate(panes, 1):
    plain = re.sub(r"<[^>]+>", " ", body)
    plain = re.sub(r"\s+", " ", plain).strip()
    print(f"  Q{i}: {title}")
    print(f"      A: {plain[:240]}{'...' if len(plain) > 240 else ''}")
    print()
