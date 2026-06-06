"""Patch the excerpt field of a single post via WP REST (WP-native, not Rank Math)."""

import argparse
import base64
import json
import sys
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


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--id", type=int, required=True)
    parser.add_argument("--excerpt", required=True)
    args = parser.parse_args()

    user, pwd = load_credentials()
    auth = auth_header(user, pwd)

    body = json.dumps({"excerpt": args.excerpt}).encode("utf-8")
    req = urllib.request.Request(
        f"{SITE_URL}/wp-json/wp/v2/posts/{args.id}",
        data=body,
        method="POST",
        headers={
            "Authorization": auth,
            "Content-Type": "application/json",
            "User-Agent": "Mozilla/5.0 schoolswp-tooling",
        },
    )
    with urllib.request.urlopen(req, timeout=60) as resp:
        out = json.loads(resp.read().decode("utf-8"))
    raw = out["excerpt"]["raw"] if isinstance(out["excerpt"], dict) else out["excerpt"]
    print(f"Post {args.id} excerpt updated (modified={out.get('modified')})")
    print(f"New raw: {raw}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
