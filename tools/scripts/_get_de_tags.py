#!/usr/bin/env python3
"""Find/create DE tags for post 2888497 via Polylang-aware REST."""

import base64
import json
import sys
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")

ROOT = Path(__file__).resolve().parents[2]
SETTINGS = ROOT / ".claude" / "settings.local.json"
SITE = "https://schoolswp.com"

TARGET_TAGS_DE = [
    "Ninja Tables",
    "DataTables",
    "WordPress-Tabellen",
    "AJAX",
]


def load_creds():
    data = json.loads(SETTINGS.read_text(encoding="utf-8"))
    env = data.get("env", {})
    return env["WP_API_USERNAME"], env["WP_API_PASSWORD"]


def auth_header(user, pw):
    return "Basic " + base64.b64encode(f"{user}:{pw}".encode()).decode()


def request(url, auth, method="GET", body=None):
    data = json.dumps(body).encode("utf-8") if body else None
    req = urllib.request.Request(url, data=data, method=method, headers={
        "Authorization": auth,
        "Accept": "application/json",
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0 schoolswp/1.0",
    })
    try:
        with urllib.request.urlopen(req, timeout=60) as r:
            return r.status, json.loads(r.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        body = e.read().decode("utf-8", errors="replace")
        try:
            return e.code, json.loads(body)
        except Exception:
            return e.code, {"_raw": body[:500]}


def main():
    user, pw = load_creds()
    auth = auth_header(user, pw)

    print(f"Searching DE tags among: {TARGET_TAGS_DE}\n")
    results = {}
    for name in TARGET_TAGS_DE:
        q = urllib.parse.quote(name)
        # Search by exact name
        st, data = request(
            f"{SITE}/wp-json/wp/v2/tags?search={q}&per_page=20&_fields=id,name,slug,count,lang",
            auth,
        )
        if st != 200:
            print(f"  [{name}] HTTP {st}: {data}")
            continue
        # filter for exact name (case-insensitive) and DE lang
        matches = [t for t in data if t.get("name", "").lower() == name.lower()]
        # Some envs return lang via "lang" key, others via taxonomies. Show all.
        print(f"  [{name}] -> {len(matches)} exact match(es):")
        for m in matches:
            print(f"      id={m['id']} slug={m.get('slug')} count={m.get('count')} lang={m.get('lang','?')}")
        results[name] = matches

    Path(ROOT / "content/articles/_workspace/post-2888497-tags-search.json").write_text(
        json.dumps(results, indent=2, ensure_ascii=False), encoding="utf-8"
    )


if __name__ == "__main__":
    main()
