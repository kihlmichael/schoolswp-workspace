#!/usr/bin/env python3
"""Inspect Polylang state for posts 58175 (FR) + 59051 (EN slot)."""
import base64, json, urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SETTINGS = ROOT / ".claude" / "settings.local.json"
data = json.loads(SETTINGS.read_text(encoding="utf-8"))
env = data.get("env", {})
user, pw = env["WP_API_USERNAME"], env["WP_API_PASSWORD"]
auth = "Basic " + base64.b64encode(f"{user}:{pw}".encode()).decode()


def get(url):
    req = urllib.request.Request(url, headers={"Authorization": auth, "Accept": "application/json"})
    with urllib.request.urlopen(req, timeout=60) as r:
        return r.status, json.loads(r.read().decode("utf-8"))


for pid in (58175, 59051):
    print(f"=== POST {pid} ===")
    status, p = get(f"https://schoolswp.com/wp-json/wp/v2/posts/{pid}?context=edit")
    keys_of_interest = ["id", "slug", "link", "lang", "translations", "polylang_translations", "polylang", "meta", "categories", "type", "status", "date", "modified"]
    for k in keys_of_interest:
        if k in p:
            v = p[k]
            if isinstance(v, (dict, list)) and len(str(v)) > 400:
                print(f"  {k}: {str(v)[:400]} ... [truncated]")
            else:
                print(f"  {k}: {v}")
    title = p.get("title", {}).get("rendered", "")
    print(f"  title: {title}")
    # Show raw_excerpt of meta keys to spot polylang
    if "meta" in p and isinstance(p["meta"], dict):
        poly_keys = [k for k in p["meta"] if "poly" in k.lower() or "lang" in k.lower() or "trans" in k.lower()]
        if poly_keys:
            print(f"  polylang-ish meta keys: {poly_keys}")
    print()

# Polylang exposes a dedicated REST endpoint
print("=== Polylang languages registered ===")
try:
    status, langs = get("https://schoolswp.com/wp-json/pll/v1/languages")
    print(json.dumps(langs, indent=2, ensure_ascii=False)[:1500])
except Exception as e:
    print(f"  /pll/v1/languages -> {e}")

print()
print("=== Polylang translations for 58175 ===")
try:
    status, t = get("https://schoolswp.com/wp-json/pll/v1/post/58175/translations")
    print(json.dumps(t, indent=2, ensure_ascii=False)[:800])
except Exception as e:
    print(f"  -> {e}")

print()
print("=== Polylang translations for 59051 ===")
try:
    status, t = get("https://schoolswp.com/wp-json/pll/v1/post/59051/translations")
    print(json.dumps(t, indent=2, ensure_ascii=False)[:800])
except Exception as e:
    print(f"  -> {e}")
