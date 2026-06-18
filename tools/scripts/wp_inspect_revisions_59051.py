#!/usr/bin/env python3
"""List revisions of post 59051 to find pre-push EN content (if any existed)."""
import base64, json, urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SETTINGS = ROOT / ".claude" / "settings.local.json"
data = json.loads(SETTINGS.read_text(encoding="utf-8"))
env = data.get("env", {})
auth = "Basic " + base64.b64encode(f"{env['WP_API_USERNAME']}:{env['WP_API_PASSWORD']}".encode()).decode()


def get(url):
    req = urllib.request.Request(url, headers={"Authorization": auth, "Accept": "application/json"})
    with urllib.request.urlopen(req, timeout=60) as r:
        return r.status, json.loads(r.read().decode("utf-8"))


_, revs = get("https://schoolswp.com/wp-json/wp/v2/posts/59051/revisions?per_page=30&_fields=id,date,modified,title,excerpt")
print(f"Total revisions: {len(revs)}")
for r in revs:
    title = r.get("title", {}).get("rendered", "")
    print(f"  rev {r['id']:>7} | {r.get('date','?')[:19]} | {title[:75]}")

# Now inspect the oldest few revisions to see if any was in English
print()
print("=== Inspecting first 200 chars of content of each revision (oldest -> newest) ===")
revs_sorted = sorted(revs, key=lambda r: r.get("date", ""))
for r in revs_sorted[:10]:
    _, rev_full = get(f"https://schoolswp.com/wp-json/wp/v2/posts/59051/revisions/{r['id']}?context=edit&_fields=id,date,title,content")
    title = rev_full.get("title", {}).get("rendered", "")
    raw = rev_full.get("content", {}).get("raw", "")
    # Detect language naively: look for stop words
    sample = raw[:1500].lower()
    fr_score = sum(1 for w in [" tu ", " vous ", " un ", "des ", " et ", "à l", "c'est", "très", "votre"] if w in sample)
    en_score = sum(1 for w in [" you ", " your ", " the ", " is ", " a ", "this ", "with ", "for ", " of "] if w in sample)
    lang_guess = "EN" if en_score > fr_score else "FR"
    print(f"  rev {r['id']:>7} | {r.get('date','?')[:19]} | lang≈{lang_guess} (en={en_score}/fr={fr_score})")
    print(f"      title: {title[:80]}")
    print(f"      first 200: {raw[:200].replace(chr(10),' / ')}")
