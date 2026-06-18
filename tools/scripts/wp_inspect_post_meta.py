"""Inspect title, excerpt and Rank Math meta for a single post."""

import argparse
import base64
import json
import sys
import urllib.parse
import urllib.request
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
SETTINGS_PATH = REPO_ROOT / ".claude" / "settings.local.json"
SITE_URL = "https://schoolswp.com"


def load_credentials() -> tuple[str, str]:
    data = json.loads(SETTINGS_PATH.read_text(encoding="utf-8"))
    env = data.get("env", {}) or {}
    return env["WP_API_USERNAME"], env["WP_API_PASSWORD"]


def auth_header(user: str, pwd: str) -> str:
    raw = f"{user}:{pwd}".encode("utf-8")
    return "Basic " + base64.b64encode(raw).decode("ascii")


def get_post(auth: str, post_id: int) -> dict:
    url = f"{SITE_URL}/wp-json/wp/v2/posts/{post_id}?context=edit"
    req = urllib.request.Request(
        url,
        headers={"Authorization": auth, "User-Agent": "Mozilla/5.0 schoolswp-tooling"},
    )
    with urllib.request.urlopen(req, timeout=60) as resp:
        return json.loads(resp.read().decode("utf-8"))


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--id", type=int, required=True)
    args = parser.parse_args()

    user, pwd = load_credentials()
    auth = auth_header(user, pwd)
    post = get_post(auth, args.id)

    title = post["title"]["raw"] if isinstance(post["title"], dict) else post["title"]
    excerpt = post["excerpt"]["raw"] if isinstance(post["excerpt"], dict) else post["excerpt"]
    slug = post.get("slug")
    lang = post.get("lang")
    print(f"ID: {post['id']}")
    print(f"slug: {slug}")
    print(f"lang: {lang}")
    print(f"--- title ---\n{title}\n")
    print(f"--- excerpt ---\n{excerpt}\n")
    meta = post.get("meta", {}) or {}
    rm_keys = [
        "rank_math_title",
        "rank_math_description",
        "rank_math_focus_keyword",
        "rank_math_facebook_title",
        "rank_math_facebook_description",
        "rank_math_twitter_title",
        "rank_math_twitter_description",
    ]
    print("--- Rank Math meta ---")
    for k in rm_keys:
        v = meta.get(k)
        if v:
            print(f"{k}: {v}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
