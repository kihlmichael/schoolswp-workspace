#!/usr/bin/env python3
"""Read current Rank Math postmeta for post 52944 to debug why front-end still
shows old title/meta after /updateMeta returned 200."""
import json, sys, urllib.request, urllib.error, base64
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SETTINGS = ROOT / ".claude" / "settings.local.json"
POST_ID = 52944

def creds():
    env = json.loads(SETTINGS.read_text(encoding="utf-8")).get("env", {})
    return env["WP_API_USERNAME"], env["WP_API_PASSWORD"]

def auth(u, p):
    return "Basic " + base64.b64encode(f"{u}:{p}".encode()).decode()

def fetch(url, u, p):
    req = urllib.request.Request(url, headers={
        "Authorization": auth(u, p),
        "Accept": "application/json",
    })
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            return r.status, r.read().decode("utf-8", errors="replace")
    except urllib.error.HTTPError as e:
        return e.code, e.read().decode("utf-8", errors="replace")

u, p = creds()
# Get the post with ALL meta exposed (context=edit shows raw meta)
status, body = fetch(f"https://schoolswp.com/wp-json/wp/v2/posts/{POST_ID}?context=edit", u, p)
data = json.loads(body)
meta = data.get("meta", {})
# Print only rank_math_* keys
rm_keys = {k: v for k, v in meta.items() if "rank_math" in k.lower()}
print(f"[meta] rank_math keys: {len(rm_keys)}")
for k in sorted(rm_keys.keys()):
    v = rm_keys[k]
    s = str(v)
    if len(s) > 200:
        s = s[:200] + "…"
    print(f"  {k} = {s}")

# Also print non-standard keys that may drive the output
interesting = ["_yoast_wpseo_title", "_yoast_wpseo_metadesc", "_aioseo_title", "_aioseo_description"]
for k in interesting:
    if k in meta:
        print(f"  {k} = {meta[k]}")
