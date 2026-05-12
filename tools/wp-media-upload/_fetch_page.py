"""One-shot helper: fetch a single WP page (preview-friendly) via REST."""

from __future__ import annotations

import json
import os
import sys
from pathlib import Path

import requests

SETTINGS = Path("d:/VS Code/CLAUDE CODE/projects/schoolswp/.claude/settings.local.json")


def _load_env() -> tuple[str, str, str]:
    raw = json.loads(SETTINGS.read_text(encoding="utf-8"))
    env = raw.get("env", {})
    url = env["WP_API_URL"].rstrip("/")
    user = env["WP_API_USERNAME"]
    pwd = env["WP_API_PASSWORD"]
    if url.endswith("/wp-json"):
        base = url
    elif "/wp-json" in url:
        base = url.split("/wp-json")[0] + "/wp-json"
    else:
        base = f"{url}/wp-json"
    return base, user, pwd


def main(page_id: int) -> None:
    base, user, pwd = _load_env()
    auth = (user, pwd)
    headers = {"User-Agent": "Mozilla/5.0 (schoolsWP wp-media-upload)"}
    # Try page first, fall back to post
    for endpoint in (f"{base}/wp/v2/pages/{page_id}", f"{base}/wp/v2/posts/{page_id}"):
        params = {"context": "edit"}
        r = requests.get(endpoint, auth=auth, headers=headers, params=params, timeout=30)
        if r.status_code == 200:
            data = r.json()
            print(json.dumps({
                "endpoint": endpoint,
                "id": data.get("id"),
                "title": data.get("title", {}).get("raw") or data.get("title", {}).get("rendered"),
                "slug": data.get("slug"),
                "status": data.get("status"),
                "link": data.get("link"),
                "featured_media": data.get("featured_media"),
                "content_excerpt": (data.get("content", {}).get("raw") or "")[:2000],
                "excerpt": (data.get("excerpt", {}).get("raw") or ""),
            }, indent=2, ensure_ascii=False))
            return
        else:
            print(f"# {endpoint} -> {r.status_code}", file=sys.stderr)
    print("Page not found via REST", file=sys.stderr)
    sys.exit(2)


if __name__ == "__main__":
    main(int(sys.argv[1]))
