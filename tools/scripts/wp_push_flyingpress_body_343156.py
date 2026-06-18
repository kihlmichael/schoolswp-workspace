#!/usr/bin/env python3
"""
Push body translation FR->EN to post 343156 (/en/flyingpress-wp-rocket-comparison/).
Reads pairs from payload-pairs.json (59 pairs).
Uses WP REST (context=edit) to fetch raw content, applies 3-variant strtr, POSTs back.
Reports sha1 before/after + substitution counts. Never echoes credentials.
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
PAIRS = ROOT / "content" / "audits" / "flyingpress-wp-rocket-comparison-en" / "2026-05-12" / "payload-pairs-v2.json"
POST_ID = 343156
BASE = "https://schoolswp.com/wp-json/wp/v2/posts"


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


def build_replacements(pairs):
    """Each pair -> 3 variants for apostrophe robustness (curly, html entity, straight)."""
    repl = {}
    for fr, en in pairs:
        repl[fr] = en
        fr_html = fr.replace("’", "&rsquo;")
        if fr_html != fr:
            repl[fr_html] = en.replace("’", "&rsquo;")
        fr_straight = fr.replace("’", "'")
        if fr_straight != fr and fr_straight not in repl:
            repl[fr_straight] = en.replace("’", "'")
    return repl


def apply_strtr(content, replacements):
    """Python equivalent of PHP strtr() - longest keys first, non-overlapping single pass."""
    keys = sorted(replacements.keys(), key=len, reverse=True)
    matches_per_key = {k: content.count(k) for k in keys}
    out = []
    i = 0
    n = len(content)
    while i < n:
        matched = False
        for k in keys:
            if not k:
                continue
            if content.startswith(k, i):
                out.append(replacements[k])
                i += len(k)
                matched = True
                break
        if not matched:
            out.append(content[i])
            i += 1
    return "".join(out), matches_per_key


def main():
    user, pw = load_creds()
    pairs = json.loads(PAIRS.read_text(encoding="utf-8"))
    print(f"[info] Loaded {len(pairs)} FR->EN pairs")

    replacements = build_replacements(pairs)
    print(f"[info] Expanded to {len(replacements)} replacement keys (3 apostrophe variants)")

    print(f"[info] GET post {POST_ID} (context=edit)...")
    status, post = http("GET", f"{BASE}/{POST_ID}?context=edit", user, pw)
    if status != 200:
        print(f"[error] GET failed: HTTP {status}")
        print(str(post)[:800])
        sys.exit(1)

    raw = post.get("content", {}).get("raw")
    if not raw:
        print("[error] content.raw missing - check edit_posts capability")
        sys.exit(1)

    sha_before = hashlib.sha1(raw.encode("utf-8")).hexdigest()
    print(f"[info] content.raw len={len(raw)} sha1={sha_before}")

    new_raw, per_key = apply_strtr(raw, replacements)
    total_matches = sum(per_key.values())
    matched_keys = sum(1 for c in per_key.values() if c > 0)
    print(f"[info] strtr applied: {matched_keys}/{len(replacements)} keys matched, {total_matches} substitutions")

    if new_raw == raw:
        print("[error] no substitution happened - content unchanged, aborting POST")
        sys.exit(2)

    sha_after_local = hashlib.sha1(new_raw.encode("utf-8")).hexdigest()
    print(f"[info] new content len={len(new_raw)} sha1={sha_after_local} (local)")

    print(f"[info] POST post {POST_ID} (timeout 180s)...")
    status, resp = http("POST", f"{BASE}/{POST_ID}", user, pw, {"content": new_raw})
    if status != 200:
        print(f"[error] POST failed: HTTP {status}")
        print(str(resp)[:1500])
        sys.exit(3)

    server_modified = resp.get("modified")
    print("[ok] HTTP 200 - post updated")
    print(f"[ok] modified: {server_modified}")
    print(f"[ok] link: {resp.get('link')}")

    print(f"[info] GET post {POST_ID} (verify)...")
    status, post2 = http("GET", f"{BASE}/{POST_ID}?context=edit", user, pw)
    if status == 200:
        raw_after = post2.get("content", {}).get("raw", "")
        sha_server = hashlib.sha1(raw_after.encode("utf-8")).hexdigest()
        print(f"[ok] server content.raw len={len(raw_after)} sha1={sha_server}")
        if sha_server == sha_before:
            print("[warn] sha1 unchanged on server - rollback?")
            sys.exit(4)
        if sha_server == sha_after_local:
            print("[ok] sha1 matches local computation byte-perfect")
        else:
            print("[info] sha1 differs from local - WP normalized something (block markup, entities)")
    print(f"[done] post {POST_ID} body translation pushed")


if __name__ == "__main__":
    main()
