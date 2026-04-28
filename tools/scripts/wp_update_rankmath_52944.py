#!/usr/bin/env python3
"""
Update Rank Math SEO title + description for post 52944.
Uses the native Rank Math REST endpoint (core /wp/v2/posts meta silent-ignores RM fields).
Pattern validated on post 52819 (2026-04-21).
"""
import json
import sys
import urllib.request
import urllib.error
import base64
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SETTINGS = ROOT / ".claude" / "settings.local.json"
POST_ID = 52944

RANK_MATH_TITLE = "Créer une plateforme de formation WordPress avec plugins LMS"
RANK_MATH_DESC = (
    "Créez et vendez votre formation en ligne avec WordPress. Tutor LMS, "
    "LearnDash, Lifter LMS + WooCommerce : le guide complet pour monétiser vos cours."
)


def load_creds():
    data = json.loads(SETTINGS.read_text(encoding="utf-8"))
    env = data.get("env", {})
    return env["WP_API_USERNAME"], env["WP_API_PASSWORD"]


def auth_header(user, app_pw):
    token = base64.b64encode(f"{user}:{app_pw}".encode()).decode()
    return f"Basic {token}"


def update_rankmath(user, pw):
    url = "https://schoolswp.com/wp-json/rankmath/v1/updateMeta"
    payload = {
        "objectID": POST_ID,
        "objectType": "post",
        "meta": {
            "rank_math_title": RANK_MATH_TITLE,
            "rank_math_description": RANK_MATH_DESC,
        },
    }
    body = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(
        url, data=body, method="POST",
        headers={
            "Authorization": auth_header(user, pw),
            "Content-Type": "application/json",
            "Accept": "application/json",
        }
    )
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            return resp.status, resp.read().decode("utf-8", errors="replace")
    except urllib.error.HTTPError as e:
        return e.code, e.read().decode("utf-8", errors="replace")


def main():
    user, pw = load_creds()
    print(f"[info] Post {POST_ID}")
    print(f"[info] New title ({len(RANK_MATH_TITLE)} char): {RANK_MATH_TITLE}")
    print(f"[info] New desc  ({len(RANK_MATH_DESC)} char): {RANK_MATH_DESC}")
    status, resp = update_rankmath(user, pw)
    print(f"[result] HTTP {status}")
    print(resp[:2000])
    if status != 200:
        sys.exit(1)


if __name__ == "__main__":
    main()
