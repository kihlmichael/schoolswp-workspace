#!/usr/bin/env python3
"""Verify the 8 candidate pillar slugs exist on schoolswp.com.
Outputs the canonical URLs to be used in pillars.yaml.
"""
import json, urllib.request, urllib.parse, base64, sys, io
from pathlib import Path

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")

ROOT = Path(__file__).resolve().parents[3]
SETTINGS = ROOT / ".claude" / "settings.local.json"

env = json.loads(SETTINGS.read_text(encoding="utf-8")).get("env", {})
auth = "Basic " + base64.b64encode(f"{env['WP_API_USERNAME']}:{env['WP_API_PASSWORD']}".encode()).decode()

CANDIDATES = [
    ("LMS — pilier", "creer-plateforme-formation-wordpress"),
    ("CRM — pilier", "fluentcrm-automatisations-indispensables"),
    ("Perf — FlyingPress vs WP Rocket", "comparaison-flyingpress-wp-rocket"),
    ("Perf — CWV", "core-web-vitals-wordpress"),
    ("Hébergement", "hebergement-wordpress"),
    ("Automatisation — OttoKit vs Zapier", "ottokit-vs-zapier"),
    ("LMS — Tutor LMS plateforme", "creer-sa-plateforme-de-formation-en-ligne-avec-tutor-lms"),
    ("Stack — Kadence", "mon-avis-sur-kadence-wp"),
]

def search_by_slug(slug):
    url = f"https://schoolswp.com/wp-json/wp/v2/posts?slug={urllib.parse.quote(slug)}&_fields=id,title,slug,link,status"
    req = urllib.request.Request(url, headers={"Authorization": auth, "Accept": "application/json"})
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            data = json.loads(r.read().decode("utf-8"))
        if isinstance(data, list) and data:
            return data[0]
    except Exception as e:
        return {"error": str(e)}
    return None

print(f"{'Label':<45} | {'Status':<8} | {'ID':<7} | URL")
print("-" * 130)
confirmed = []
missing = []
for label, slug in CANDIDATES:
    result = search_by_slug(slug)
    if result and "id" in result:
        confirmed.append((label, result["link"], result["id"]))
        print(f"{label:<45} | {result['status']:<8} | {result['id']:<7} | {result['link']}")
    else:
        missing.append((label, slug))
        print(f"{label:<45} | NOT FOUND | -       | {slug}")

print()
print(f"Confirmed: {len(confirmed)} / {len(CANDIDATES)}")
if missing:
    print(f"Missing: {[m[1] for m in missing]}")

# Write the config snapshot
config = {
    "pillars": [
        {"label": label, "url": link, "post_id": pid}
        for label, link, pid in confirmed
    ],
    "notes": "Ajouter manuellement les 2 piliers manquants (SEO + Ecommerce/FluentCart) dans cette liste",
}
out = Path(__file__).parent / "pillars.json"
out.write_text(json.dumps(config, indent=2, ensure_ascii=False), encoding="utf-8")
print(f"\nWritten {out}")
