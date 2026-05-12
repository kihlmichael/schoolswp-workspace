"""Inspect a WP page's template + Kadence layout meta."""

from __future__ import annotations

import json
import sys
from pathlib import Path

import requests

SETTINGS = Path("d:/VS Code/CLAUDE CODE/projects/schoolswp/.claude/settings.local.json")


def load_wp():
    raw = json.loads(SETTINGS.read_text(encoding="utf-8"))
    env = raw["env"]
    url = env["WP_API_URL"].rstrip("/")
    if url.endswith("/wp-json"):
        base = url
    elif "/wp-json" in url:
        base = url.split("/wp-json")[0] + "/wp-json"
    else:
        base = f"{url}/wp-json"
    return base, (env["WP_API_USERNAME"], env["WP_API_PASSWORD"])


def main(page_id: int) -> int:
    base, auth = load_wp()
    headers = {"User-Agent": "Mozilla/5.0"}

    # 1) Page details with meta context=edit
    r = requests.get(f"{base}/wp/v2/pages/{page_id}", params={"context": "edit"}, auth=auth, headers=headers, timeout=30)
    r.raise_for_status()
    page = r.json()
    summary = {
        "id": page["id"],
        "title": page["title"]["raw"],
        "slug": page["slug"],
        "status": page["status"],
        "template": page.get("template"),
        "featured_media": page.get("featured_media"),
        "meta_keys": sorted((page.get("meta") or {}).keys()),
        "kadence_meta_present": "_kad_post_meta" in (page.get("meta") or {}),
        "kadence_meta_value": (page.get("meta") or {}).get("_kad_post_meta"),
    }
    print(json.dumps(summary, indent=2, ensure_ascii=False))

    # 2) List available page templates
    r2 = requests.get(f"{base}/wp/v2/types/page", auth=auth, headers=headers, timeout=30)
    if r2.ok:
        types = r2.json()
        # In WP REST, available templates appear on /wp/v2/templates or via theme
        # but a quick proxy is the "supports" + try OPTIONS on page
    r3 = requests.options(f"{base}/wp/v2/pages", auth=auth, headers=headers, timeout=30)
    if r3.ok:
        schema = r3.json()
        # the schema's 'template' field enum lists available templates
        template_enum = (
            schema.get("schema", {}).get("properties", {}).get("template", {}).get("enum")
        )
        print("\navailable templates:", json.dumps(template_enum, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main(int(sys.argv[1])))
