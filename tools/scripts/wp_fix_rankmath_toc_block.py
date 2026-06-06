"""
Fix Rank Math TOC block crash on a post (Gutenberg editor error).

Usage:
    python wp_fix_rankmath_toc_block.py --slug flyingpress-wp-rocket-comparison --lang en
    python wp_fix_rankmath_toc_block.py --id 343200 --dry-run

See: reference_rank_math_toc_block_bug memory.
"""

import argparse
import base64
import json
import re
import sys
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
SETTINGS_PATH = REPO_ROOT / ".claude" / "settings.local.json"
SITE_URL = "https://schoolswp.com"
TOC_BLOCK_PATTERN = re.compile(
    r"<!--\s*wp:rank-math/toc-block[^>]*-->.*?<!--\s*/wp:rank-math/toc-block\s*-->\s*\n?",
    re.DOTALL,
)


def load_credentials() -> tuple[str, str]:
    data = json.loads(SETTINGS_PATH.read_text(encoding="utf-8"))
    env = data.get("env", {}) or {}
    user = env.get("WP_API_USERNAME")
    pwd = env.get("WP_API_PASSWORD")
    if not user or not pwd:
        raise SystemExit("Missing WP_API_USERNAME / WP_API_PASSWORD in settings.local.json")
    return user, pwd


def auth_header(user: str, pwd: str) -> str:
    raw = f"{user}:{pwd}".encode("utf-8")
    return "Basic " + base64.b64encode(raw).decode("ascii")


def wp_request(
    method: str,
    path: str,
    auth: str,
    body: dict | None = None,
    query: dict | None = None,
) -> dict | list:
    url = f"{SITE_URL}/wp-json{path}"
    if query:
        url += "?" + urllib.parse.urlencode(query)
    data = None
    headers = {
        "Authorization": auth,
        "Accept": "application/json",
        "User-Agent": "Mozilla/5.0 schoolswp-tooling",
    }
    if body is not None:
        data = json.dumps(body).encode("utf-8")
        headers["Content-Type"] = "application/json"
    req = urllib.request.Request(url, data=data, method=method, headers=headers)
    try:
        with urllib.request.urlopen(req, timeout=180) as resp:
            return json.loads(resp.read().decode("utf-8"))
    except urllib.error.HTTPError as exc:
        sys.stderr.write(f"HTTP {exc.code} {exc.reason} on {method} {path}\n")
        sys.stderr.write(exc.read().decode("utf-8", errors="replace") + "\n")
        raise


def find_post(auth: str, slug: str, lang: str | None) -> dict:
    query = {"slug": slug, "context": "edit", "per_page": 5}
    if lang:
        query["lang"] = lang
    posts = wp_request("GET", "/wp/v2/posts", auth, query=query)
    if not posts:
        # Try pages
        posts = wp_request("GET", "/wp/v2/pages", auth, query=query)
    if not posts:
        raise SystemExit(f"No post/page found for slug={slug} lang={lang}")
    if len(posts) > 1:
        ids = [p["id"] for p in posts]
        sys.stderr.write(f"Multiple matches {ids}, using first.\n")
    return posts[0]


def get_post(auth: str, post_id: int) -> dict:
    return wp_request("GET", f"/wp/v2/posts/{post_id}", auth, query={"context": "edit"})


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--slug")
    parser.add_argument("--lang")
    parser.add_argument("--id", type=int)
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    if not args.id and not args.slug:
        parser.error("--id or --slug required")

    user, pwd = load_credentials()
    auth = auth_header(user, pwd)

    if args.id:
        post = get_post(auth, args.id)
    else:
        post = find_post(auth, args.slug, args.lang)
        post = get_post(auth, post["id"])

    post_id = post["id"]
    raw = post["content"]["raw"]
    title = post["title"]["raw"] if isinstance(post["title"], dict) else post["title"]
    print(f"Post {post_id} | {title}")
    print(f"Original raw length: {len(raw)}")

    matches = TOC_BLOCK_PATTERN.findall(raw)
    print(f"TOC blocks found: {len(matches)}")

    if not matches:
        print("Nothing to do — no wp:rank-math/toc-block in content.")
        return 0

    # Backup
    backup_dir = REPO_ROOT / "content" / "audits" / "_backups" / "rankmath-toc-fix"
    backup_dir.mkdir(parents=True, exist_ok=True)
    backup_path = backup_dir / f"post-{post_id}.before.html"
    backup_path.write_text(raw, encoding="utf-8")
    print(f"Backup saved: {backup_path}")

    new_raw, n = TOC_BLOCK_PATTERN.subn("", raw)
    delta = len(raw) - len(new_raw)
    print(f"Removed {n} block(s), delta={delta} chars")

    if delta > 5000:
        raise SystemExit(f"Delta too large ({delta}), aborting safety check.")

    after_path = backup_dir / f"post-{post_id}.after.html"
    after_path.write_text(new_raw, encoding="utf-8")
    print(f"After-content saved: {after_path}")

    if args.dry_run:
        print("Dry-run: no POST sent.")
        return 0

    res = wp_request("POST", f"/wp/v2/posts/{post_id}", auth, body={"content": new_raw})
    print(f"PATCH OK — new modified={res.get('modified')}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
