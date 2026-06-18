#!/usr/bin/env python3
"""Diagnose HTTP 500 on 6 stubborn posts."""
import base64, json, urllib.request, urllib.error
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
data = json.loads((ROOT / ".claude" / "settings.local.json").read_text(encoding="utf-8"))
env = data["env"]
auth = "Basic " + base64.b64encode(f"{env['WP_API_USERNAME']}:{env['WP_API_PASSWORD']}".encode()).decode()

for pid in (927, 933, 2453, 2475, 3157, 3161):
    req = urllib.request.Request(
        f"https://schoolswp.com/wp-json/wp/v2/posts/{pid}?context=edit&_fields=id,slug,modified",
        headers={"Authorization": auth, "User-Agent": "Mozilla/5.0"},
    )
    try:
        with urllib.request.urlopen(req, timeout=60) as r:
            d = json.loads(r.read())
            print(f"{pid:>5}: {r.status} | slug={d.get('slug')} modified={d.get('modified')}")
    except urllib.error.HTTPError as e:
        body = e.read().decode("utf-8", errors="replace")
        print(f"{pid:>5}: HTTP {e.code} | body[:300]={body[:300]!r}")
    except Exception as e:
        print(f"{pid:>5}: EXC {type(e).__name__}: {e}")

# Also try context=view (lighter, no raw content)
print()
print("=== context=view (no edit auth, lighter) ===")
for pid in (927, 933, 2453, 2475, 3157, 3161):
    req = urllib.request.Request(
        f"https://schoolswp.com/wp-json/wp/v2/posts/{pid}?context=view&_fields=id,slug,modified,link",
        headers={"User-Agent": "Mozilla/5.0"},
    )
    try:
        with urllib.request.urlopen(req, timeout=60) as r:
            d = json.loads(r.read())
            print(f"{pid:>5}: {r.status} | slug={d.get('slug'):40.40} | link={d.get('link')}")
    except urllib.error.HTTPError as e:
        print(f"{pid:>5}: HTTP {e.code} (view)")
    except Exception as e:
        print(f"{pid:>5}: EXC {type(e).__name__}: {e}")
