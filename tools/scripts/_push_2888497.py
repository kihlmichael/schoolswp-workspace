#!/usr/bin/env python3
"""Push patched content + slug to post 2888497 via WP REST.

Per reference_wp_rest_block_preservation.md : timeout 180s, /wp/v2/posts.
Per feedback_wp_update_post_unslash_kadence.md : verify Kadence escapes survive.
Per reference_novamira_large_content_push.md : 43KB is small enough for a single POST.
"""

import base64
import json
import sys
import urllib.error
import urllib.request
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")

ROOT = Path(__file__).resolve().parents[2]
SETTINGS = ROOT / ".claude" / "settings.local.json"
PATCHED = ROOT / "content" / "articles" / "_workspace" / "post-2888497-patched.html"
SITE = "https://schoolswp.com"
POST_ID = 2888497
NEW_SLUG = "ninja-tables-datatables-grosse-datensaetze"

# Backup first
BACKUP = ROOT / "content" / "articles" / "_workspace" / "post-2888497-backup-pre-patch.json"


def load_creds():
    data = json.loads(SETTINGS.read_text(encoding="utf-8"))
    env = data.get("env", {})
    return env["WP_API_USERNAME"], env["WP_API_PASSWORD"]


def auth_header(user, pw):
    return "Basic " + base64.b64encode(f"{user}:{pw}".encode()).decode()


def main():
    user, pw = load_creds()
    auth = auth_header(user, pw)

    # 1) Backup current state from disk (was already fetched)
    src = ROOT / "content" / "articles" / "_workspace" / "post-2888497-current.json"
    BACKUP.write_text(src.read_text(encoding="utf-8"), encoding="utf-8")
    print(f"[backup] {BACKUP}")

    # 2) Read patched content
    content = PATCHED.read_text(encoding="utf-8")
    print(f"[push] content length: {len(content)} chars")

    # 3) Build payload
    payload = {
        "content": content,
        "slug": NEW_SLUG,
    }
    body = json.dumps(payload).encode("utf-8")

    url = f"{SITE}/wp-json/wp/v2/posts/{POST_ID}"
    req = urllib.request.Request(url, data=body, method="POST", headers={
        "Authorization": auth,
        "Accept": "application/json",
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0 schoolswp-patcher/1.0",
    })

    try:
        with urllib.request.urlopen(req, timeout=180) as r:
            resp = json.loads(r.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        body = e.read().decode("utf-8", errors="replace")
        print(f"[push] HTTP {e.code}: {body[:800]}", file=sys.stderr)
        sys.exit(1)
    except urllib.error.URLError as e:
        print(f"[push] URLError: {e}", file=sys.stderr)
        sys.exit(1)

    print(f"[push] OK")
    print(f"  id        : {resp.get('id')}")
    print(f"  status    : {resp.get('status')}")
    print(f"  slug      : {resp.get('slug')}")
    print(f"  modified  : {resp.get('modified')}")
    print(f"  link      : {resp.get('link')}")
    print(f"  content   : {len(resp.get('content',{}).get('rendered',''))} chars (rendered)")

    # 4) Save server-side state for verification
    after = ROOT / "content" / "articles" / "_workspace" / "post-2888497-after.json"
    # Re-fetch raw to verify byte-for-byte
    req2 = urllib.request.Request(
        f"{SITE}/wp-json/wp/v2/posts/{POST_ID}?context=edit",
        headers={
            "Authorization": auth,
            "Accept": "application/json",
            "User-Agent": "Mozilla/5.0 schoolswp-patcher/1.0",
        },
    )
    with urllib.request.urlopen(req2, timeout=60) as r:
        after_data = json.loads(r.read().decode("utf-8"))
    after.write_text(json.dumps(after_data, indent=2, ensure_ascii=False), encoding="utf-8")

    after_content = after_data.get("content", {}).get("raw", "")
    print(f"  re-fetch  : {len(after_content)} chars (raw)")
    if after_content == content:
        print("  byte-perfect: YES ✓")
    else:
        # Find first diff
        n = min(len(after_content), len(content))
        for i in range(n):
            if after_content[i] != content[i]:
                print(f"  byte-perfect: NO  (first diff at offset {i})")
                print(f"    expected: ...{content[max(0,i-40):i+40]!r}...")
                print(f"    got     : ...{after_content[max(0,i-40):i+40]!r}...")
                break
        if len(after_content) != len(content):
            print(f"  length diff: expected={len(content)} got={len(after_content)}")


if __name__ == "__main__":
    main()
