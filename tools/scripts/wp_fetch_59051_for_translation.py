#!/usr/bin/env python3
"""Fetch latest raw content of post 59051 + identify internal links to remap to EN equivalents."""
import base64, json, re, urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SETTINGS = ROOT / ".claude" / "settings.local.json"
data = json.loads(SETTINGS.read_text(encoding="utf-8"))
env = data.get("env", {})
auth = "Basic " + base64.b64encode(f"{env['WP_API_USERNAME']}:{env['WP_API_PASSWORD']}".encode()).decode()


def http_get(url):
    req = urllib.request.Request(url, headers={"Authorization": auth, "Accept": "application/json"})
    with urllib.request.urlopen(req, timeout=60) as r:
        return r.status, json.loads(r.read().decode("utf-8"))


_, post = http_get("https://schoolswp.com/wp-json/wp/v2/posts/59051?context=edit&_fields=id,title,excerpt,content,slug,link")
raw_content = post["content"]["raw"]
raw_title = post["title"]["raw"]
raw_excerpt = post.get("excerpt", {}).get("raw", "")

print(f"slug   : {post['slug']}")
print(f"link   : {post['link']}")
print(f"title  : {raw_title}")
print(f"excerpt: {raw_excerpt!r}")
print(f"content len: {len(raw_content)}")

out_dir = ROOT / "tools" / "scripts"
(out_dir / "_59051_fr_content.html").write_text(raw_content, encoding="utf-8")
(out_dir / "_59051_fr_title.txt").write_text(raw_title, encoding="utf-8")
(out_dir / "_59051_fr_excerpt.txt").write_text(raw_excerpt, encoding="utf-8")
print(f"\nFR snapshot saved to:")
print(f"  {out_dir / '_59051_fr_content.html'}")
print(f"  {out_dir / '_59051_fr_title.txt'}")
print(f"  {out_dir / '_59051_fr_excerpt.txt'}")

# Inventory of internal links to remap
print("\n=== Internal schoolswp.com links in content ===")
links = re.findall(r'href="(https://schoolswp\.com[^"]+)"', raw_content)
for link in sorted(set(links)):
    print(f"  {link}")

# Inventory of image src + alt
print("\n=== Image sources (to keep) + alts (to translate) ===")
for m in re.finditer(r'<img[^>]+src="([^"]+)"[^>]*?(?:alt="([^"]*)")?[^>]*>', raw_content):
    src = m.group(1)
    alt = m.group(2) or ""
    print(f"  src: {src}")
    print(f"  alt: {alt!r}")

# Inventory of embeds (Pinterest, YouTube)
print("\n=== Embeds (keep URLs) ===")
for m in re.finditer(r'(https://(?:fr\.)?pinterest\.com/pin/\d+/|https://www\.youtube\.com/embed/[^\"]+)', raw_content):
    print(f"  {m.group(0)}")
