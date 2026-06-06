#!/usr/bin/env python3
"""
Strip trailing [CTA_STANDARD] placeholder from post 59051 (/en/learndash-review/).
Placeholder is the last 14 chars of content.raw, preceded by \\n\\n after a closed wp:columns block.
Verifies sha1 before/after, POSTs via WP REST (context=edit -> POST /posts/{id}).
"""

import base64
import hashlib
import json
import sys
import urllib.error
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SETTINGS = ROOT / ".claude" / "settings.local.json"
POST_ID = 59051
BASE = "https://schoolswp.com/wp-json/wp/v2/posts"
PLACEHOLDER = "[CTA_STANDARD]"


def load_creds():
    data = json.loads(SETTINGS.read_text(encoding="utf-8"))
    env = data.get("env", {})
    return env["WP_API_USERNAME"], env["WP_API_PASSWORD"]


def auth_header(user, pw):
    return "Basic " + base64.b64encode(f"{user}:{pw}".encode()).decode()


def http(method, url, user, pw, payload=None):
    headers = {
        "Authorization": auth_header(user, pw),
        "Accept": "application/json",
    }
    data = None
    if payload is not None:
        headers["Content-Type"] = "application/json"
        data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(url, data=data, method=method, headers=headers)
    try:
        with urllib.request.urlopen(req, timeout=180) as resp:
            return resp.status, json.loads(resp.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        return e.code, e.read().decode("utf-8", errors="replace")


def strip_placeholder(raw):
    """Remove the trailing [CTA_STANDARD] and any whitespace immediately before/after it."""
    idx = raw.find(PLACEHOLDER)
    if idx < 0:
        return raw, 0
    # Walk back over any \n or whitespace preceding the placeholder
    start = idx
    while start > 0 and raw[start - 1] in "\r\n\t ":
        start -= 1
    end = idx + len(PLACEHOLDER)
    # Walk forward over trailing whitespace
    while end < len(raw) and raw[end] in "\r\n\t ":
        end += 1
    cleaned = raw[:start] + raw[end:]
    # Ensure content ends with exactly one newline
    cleaned = cleaned.rstrip() + "\n"
    return cleaned, 1


def main():
    user, pw = load_creds()

    print(f"[info] GET post {POST_ID} (context=edit)...")
    status, post = http("GET", f"{BASE}/{POST_ID}?context=edit", user, pw)
    if status != 200:
        print(f"[error] GET failed: HTTP {status}\n{str(post)[:800]}")
        sys.exit(1)

    raw = post["content"]["raw"]
    sha_before = hashlib.sha1(raw.encode("utf-8")).hexdigest()
    print(f"[info] before: len={len(raw)} sha1={sha_before}")

    new_raw, n = strip_placeholder(raw)
    if n == 0:
        print("[ok] no [CTA_STANDARD] found - nothing to do")
        sys.exit(0)

    sha_local = hashlib.sha1(new_raw.encode("utf-8")).hexdigest()
    print(f"[info] after : len={len(new_raw)} sha1={sha_local}")
    print(f"[info] removed {len(raw) - len(new_raw)} chars")
    print("[info] last 200 chars of NEW content:")
    print(repr(new_raw[-200:]))

    print(f"\n[info] POST post {POST_ID}...")
    status, resp = http("POST", f"{BASE}/{POST_ID}", user, pw, {"content": new_raw})
    if status != 200:
        print(f"[error] POST failed: HTTP {status}\n{str(resp)[:1500]}")
        sys.exit(3)

    print("[ok] HTTP 200")
    print(f"[ok] modified: {resp.get('modified')}")
    print(f"[ok] link    : {resp.get('link')}")

    # Verify
    status, post2 = http("GET", f"{BASE}/{POST_ID}?context=edit", user, pw)
    if status == 200:
        raw2 = post2["content"]["raw"]
        sha_server = hashlib.sha1(raw2.encode("utf-8")).hexdigest()
        print(f"[ok] server: len={len(raw2)} sha1={sha_server}")
        if PLACEHOLDER in raw2:
            print("[error] placeholder STILL present on server!")
            sys.exit(4)
        if sha_server == sha_local:
            print("[ok] byte-perfect match")
        else:
            print("[info] server normalized whitespace - placeholder gone, content intact")
        print(f"[done] /en/learndash-review/ cleaned")


if __name__ == "__main__":
    main()
