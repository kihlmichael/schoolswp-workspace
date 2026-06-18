#!/usr/bin/env python3
"""
Push EN translation to post 59051 (/en/learndash-review/).
Updates content + title + excerpt. Preserves Gutenberg block markup byte-for-byte
(only translatable text/alts/captions/2 internal hrefs changed).

Pre-push: snapshot current FR raw to _backup_59051_fr_<timestamp>.json for rollback.
"""

import base64
import hashlib
import json
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SETTINGS = ROOT / ".claude" / "settings.local.json"
SCRIPTS = ROOT / "tools" / "scripts"
EN_CONTENT = SCRIPTS / "_59051_en_content.html"
POST_ID = 59051
BASE = "https://schoolswp.com/wp-json/wp/v2/posts"

TITLE_EN = "LearnDash Review 2026: Is It Worth It for Your Courses?"
EXCERPT_EN = "Want to build effective online courses but feel lost among all the LMS solutions? We break down LearnDash, the WordPress plugin that turns your site into a real training platform. Discover its features, strengths, limits and whether it's the right choice for you."


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
        "User-Agent": "Mozilla/5.0 schoolsWP-push",
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


def main():
    user, pw = load_creds()

    # Step 1: Snapshot current state (FR raw) for rollback
    print(f"[info] GET post {POST_ID} (context=edit) for FR backup...")
    status, post = http("GET", f"{BASE}/{POST_ID}?context=edit", user, pw)
    if status != 200:
        print(f"[error] GET failed: HTTP {status}")
        sys.exit(1)

    fr_content = post["content"]["raw"]
    fr_title = post["title"]["raw"]
    fr_excerpt = post.get("excerpt", {}).get("raw", "")
    fr_sha = hashlib.sha1(fr_content.encode("utf-8")).hexdigest()

    ts = time.strftime("%Y-%m-%d_%H%M%S")
    backup_path = SCRIPTS / f"_backup_59051_fr_{ts}.json"
    backup_path.write_text(
        json.dumps(
            {
                "post_id": POST_ID,
                "timestamp": ts,
                "title": fr_title,
                "excerpt": fr_excerpt,
                "content": fr_content,
                "content_sha1": fr_sha,
                "modified": post.get("modified"),
            },
            indent=2,
            ensure_ascii=False,
        ),
        encoding="utf-8",
    )
    print(f"[ok ] FR backup saved: {backup_path}")
    print(f"     FR sha1={fr_sha} len={len(fr_content)}")
    print(f"     FR title: {fr_title}")

    # Step 2: Load EN translation
    en_content = EN_CONTENT.read_text(encoding="utf-8")
    # Strip trailing single newline if present (POST will get the same form server-side)
    if en_content.endswith("\n"):
        en_content_send = en_content[:-1]
    else:
        en_content_send = en_content
    en_sha = hashlib.sha1(en_content_send.encode("utf-8")).hexdigest()
    print(f"\n[info] EN content loaded: len={len(en_content_send)} sha1={en_sha}")
    print(f"     EN title  : {TITLE_EN}")
    print(f"     EN excerpt: {EXCERPT_EN[:80]}...")

    # Step 3: POST update
    payload = {
        "content": en_content_send,
        "title": TITLE_EN,
        "excerpt": EXCERPT_EN,
    }
    print(f"\n[info] POST post {POST_ID} with content + title + excerpt...")
    status, resp = http("POST", f"{BASE}/{POST_ID}", user, pw, payload)
    if status != 200:
        print(f"[error] POST failed: HTTP {status}")
        print(str(resp)[:1500])
        sys.exit(3)

    print(f"[ok ] HTTP 200, modified: {resp.get('modified')}")
    print(f"[ok ] link: {resp.get('link')}")

    # Step 4: Verify
    print(f"\n[info] GET post {POST_ID} for verification...")
    status, post2 = http("GET", f"{BASE}/{POST_ID}?context=edit", user, pw)
    if status == 200:
        srv_content = post2["content"]["raw"]
        srv_title = post2["title"]["raw"]
        srv_sha = hashlib.sha1(srv_content.encode("utf-8")).hexdigest()
        print(f"[ok ] server content sha1={srv_sha} len={len(srv_content)}")
        print(f"[ok ] server title    : {srv_title}")
        # check FR words leak
        for fr_word in ("formations", "découvre", "n'importe", "élèves", "créer"):
            if fr_word in srv_content.lower():
                print(f"[warn] FR word '{fr_word}' still present in server content!")
        if srv_sha == en_sha:
            print("[ok ] byte-perfect EN")
        else:
            print("[info] sha differs (WP normalized) - inspecting deltas...")
            # Show first 30 differing chars
            for i, (a, b) in enumerate(zip(srv_content, en_content_send)):
                if a != b:
                    print(f"  first diff @{i}: server={a!r} local={b!r}")
                    print(f"  context server: {srv_content[max(0,i-30):i+30]!r}")
                    print(f"  context local : {en_content_send[max(0,i-30):i+30]!r}")
                    break
    print("\n[done] EN translation pushed to /en/learndash-review/")
    print(f"[done] rollback available via: {backup_path}")


if __name__ == "__main__":
    main()
