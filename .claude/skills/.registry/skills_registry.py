"""
Skills Registry — scan + cache + sync Google Sheets via n8n webhook
Usage:
  python skills_registry.py          # scan + rapport + cache
  python skills_registry.py --sync   # scan + rapport + cache + POST webhook
"""

import argparse
import hashlib
import json
import os
import re
from datetime import datetime

try:
    import urllib.request

    HAS_URLLIB = True
except ImportError:
    HAS_URLLIB = False

WEBHOOK_URL = "https://schoolswp-n8n.wp1.host/webhook/skills-registry-sync"
SKILLS_DIRS = [
    r"D:\VS Code\CLAUDE CODE\projects\schoolswp\.claude\skills",  # source unique (consolidé 2026-04-17)
]
CACHE_DIR = os.path.join(SKILLS_DIRS[0], ".registry")
CACHE_PATH = os.path.join(CACHE_DIR, "registry_cache.json")

os.makedirs(CACHE_DIR, exist_ok=True)

# ── Parse args ──────────────────────────────────────────────────────────────
parser = argparse.ArgumentParser()
parser.add_argument("--sync", action="store_true", help="POST résultats au webhook n8n")
args = parser.parse_args()

# ── Load cache ───────────────────────────────────────────────────────────────
cache = {}
if os.path.exists(CACHE_PATH):
    with open(CACHE_PATH, encoding="utf-8") as f:
        cache = json.load(f).get("skills", {})

# ── Load archived descriptions (preserved across runs) ──────────────────────
ARCHIVED_DESC_PATH = os.path.join(CACHE_DIR, "archived_descriptions.json")
archived_desc = {}
if os.path.exists(ARCHIVED_DESC_PATH):
    with open(ARCHIVED_DESC_PATH, encoding="utf-8") as f:
        archived_desc = json.load(f)

# ── Load classification (family / subcategory / usage / impact) ─────────────
CLASSIF_PATH = os.path.join(CACHE_DIR, "skills_classification.json")
classification = {"directory_defaults": {}, "subcategory_rules": [], "skill_overrides": {}}
if os.path.exists(CLASSIF_PATH):
    with open(CLASSIF_PATH, encoding="utf-8") as f:
        classification = json.load(f)

TIER_MAP = {
    ("S", "Critique"): "T1",
    ("S", "Important"): "T1",
    ("A", "Critique"): "T1",
    ("S", "Support"): "T2",
    ("A", "Important"): "T2",
    ("B", "Critique"): "T2",
    ("A", "Support"): "T3",
    ("B", "Important"): "T3",
    ("B", "Support"): "T3",
    ("C", "Critique"): "T4",
    ("C", "Important"): "T4",
    ("C", "Support"): "T4",
}


def classify(name, rel_path):
    """Apply directory_defaults -> subcategory_rules -> skill_overrides. Compute tier."""
    top_dir = rel_path.split("/", 1)[0] if "/" in rel_path else ""
    defaults = classification.get("directory_defaults", {}).get(top_dir, {})
    family = defaults.get("family", "")
    subcategory = defaults.get("subcategory", "")
    usage = defaults.get("usage", "B")
    impact = defaults.get("impact", "Support")

    # Path-based subcategory rules (e.g. gws/recipes/, gws/personas/)
    for rule in classification.get("subcategory_rules", []):
        if rule.get("path_prefix") and not rel_path.startswith(rule["path_prefix"]):
            continue
        if rule.get("name_prefix") and not name.startswith(rule["name_prefix"]):
            continue
        subcategory = rule["subcategory"]

    # Per-skill overrides win
    override = classification.get("skill_overrides", {}).get(name, {})
    family = override.get("family", family)
    subcategory = override.get("subcategory", subcategory)
    usage = override.get("usage", usage)
    impact = override.get("impact", impact)

    tier = override.get("tier_override") or TIER_MAP.get((usage, impact), "T3")
    return family, subcategory, usage, impact, tier

# ── Scan ─────────────────────────────────────────────────────────────────────
results = []
seen_names = set()
for skills_dir in SKILLS_DIRS:
    if not os.path.isdir(skills_dir):
        continue
    for root, dirs, files in os.walk(skills_dir):
        dirs[:] = [d for d in dirs if d not in (".registry", ".archived-workspace-variants", "_to-delete", "node_modules")]
        if "SKILL.md" not in files:
            continue
        path = os.path.join(root, "SKILL.md")
        folder = os.path.basename(root)
        if folder in seen_names:
            continue
        seen_names.add(folder)
        try:
            with open(path, encoding="utf-8") as f:
                content = f.read()
        except Exception:
            continue

        # Strip UTF-8 BOM if present so frontmatter regex anchors correctly
        if content.startswith("﻿"):
            content = content.lstrip("﻿")

        fm_match = re.match(r"^---\s*\n(.*?)\n---", content, re.DOTALL)
        name, desc = folder, ""
        if fm_match:
            fm = fm_match.group(1)
            nm = re.search(r"^name:\s*(.+)", fm, re.MULTILINE)
            dm = re.search(r"^description:\s*[|>]?[+-]?\s*([\s\S]+?)(?=\n\w|\Z)", fm, re.MULTILINE)
            if nm:
                name = nm.group(1).strip().strip('"').strip("'")
            if dm:
                desc = re.sub(r"\s+", " ", dm.group(1).strip())
                # Strip outer YAML quotes (single-line description: "..." or '...')
                if (desc.startswith('"') and desc.endswith('"')) or (desc.startswith("'") and desc.endswith("'")):
                    desc = desc[1:-1].strip()

        desc_short = (desc[:130] + "...") if len(desc) > 130 else desc
        h = hashlib.md5(content.encode()).hexdigest()[:8]
        mtime = datetime.fromtimestamp(os.path.getmtime(path)).strftime("%Y-%m-%d")
        rel_path = path.replace(skills_dir + os.sep, "").replace(os.sep, "/")

        if name not in cache:
            status = "new"
        elif cache[name]["hash"] != h:
            status = "modified"
        else:
            status = "unchanged"

        family, subcategory, usage, impact, tier = classify(name, rel_path)
        results.append(
            {
                "name": name,
                "family": family,
                "subcategory": subcategory,
                "usage": usage,
                "impact": impact,
                "tier": tier,
                "description": desc_short,
                "path": rel_path,
                "last_modified": mtime,
                "status": status,
                "hash": h,
                "detected_at": datetime.now().strftime("%Y-%m-%d"),
            }
        )

# Archived — re-inject last known description from cache or archived_desc store
current_names = {r["name"] for r in results}
for cname in cache:
    if cname not in current_names:
        last_desc = cache.get(cname, {}).get("description", "") or archived_desc.get(cname, "")
        family, subcategory, usage, impact, _ = classify(cname, "")
        results.append(
            {
                "name": cname,
                "family": family,
                "subcategory": subcategory,
                "usage": usage,
                "impact": impact,
                "tier": "Archive",
                "description": last_desc,
                "path": "",
                "last_modified": "",
                "status": "archived",
                "hash": "",
                "detected_at": datetime.now().strftime("%Y-%m-%d"),
            }
        )

# Persist archived descriptions for skills first detected as archived this run
for r in results:
    if r["status"] != "archived" and r["description"]:
        archived_desc[r["name"]] = r["description"]
with open(ARCHIVED_DESC_PATH, "w", encoding="utf-8") as f:
    json.dump(archived_desc, f, ensure_ascii=False, indent=2)

# ── Save cache ────────────────────────────────────────────────────────────────
new_cache = {
    "last_run": datetime.now().isoformat(),
    "skills": {
        r["name"]: {
            "hash": r["hash"],
            "last_modified": r["last_modified"],
            "description": r["description"],
        }
        for r in results
        if r["status"] != "archived"
    },
}
with open(CACHE_PATH, "w", encoding="utf-8") as f:
    json.dump(new_cache, f, ensure_ascii=False, indent=2)

# ── CSV ───────────────────────────────────────────────────────────────────────
csv_path = os.path.join(CACHE_DIR, "skills_registry.csv")
with open(csv_path, "w", encoding="utf-8-sig") as f:
    f.write("name\tfamily\tsubcategory\tusage\timpact\ttier\tdescription\tpath\tlast_modified\tstatus\tdetected_at\thash\n")
    for r in sorted(results, key=lambda x: (x["tier"], x["family"], x["subcategory"], x["name"])):
        dc = r["description"].replace("\t", " ").replace("\n", " ")
        f.write(
            f"{r['name']}\t{r['family']}\t{r['subcategory']}\t{r['usage']}\t{r['impact']}\t{r['tier']}\t{dc}\t{r['path']}\t{r['last_modified']}\t{r['status']}\t{r['detected_at']}\t{r['hash']}\n"
        )

# ── Rapport ───────────────────────────────────────────────────────────────────
counts = {"new": 0, "modified": 0, "unchanged": 0, "archived": 0}
for r in results:
    counts[r["status"]] += 1

now = datetime.now().strftime("%Y-%m-%d %H:%M")
print(f"\nSKILLS REGISTRY -- {now}")
print("-" * 50)
print(f"Total     : {len(results)} skills")
print(f"Nouveaux  : {counts['new']}")
print(f"Modifies  : {counts['modified']}")
print(f"Inchanges : {counts['unchanged']}")
print(f"Archives  : {counts['archived']}")

# Tier breakdown
tier_counts = {"T1": 0, "T2": 0, "T3": 0, "T4": 0, "Archive": 0}
for r in results:
    tier_counts[r["tier"]] = tier_counts.get(r["tier"], 0) + 1
print("\nRepartition par tier :")
for t in ["T1", "T2", "T3", "T4", "Archive"]:
    print(f"  {t:8s} : {tier_counts.get(t, 0)}")

# Family breakdown
family_counts = {}
for r in results:
    family_counts[r["family"]] = family_counts.get(r["family"], 0) + 1
print("\nRepartition par famille :")
for fam in sorted(family_counts.keys()):
    label = fam if fam else "(non classe)"
    print(f"  {label:35s} : {family_counts[fam]}")

for status_label, status_key in [("NOUVEAUX", "new"), ("MODIFIES", "modified"), ("ARCHIVES", "archived")]:
    group = sorted([r for r in results if r["status"] == status_key], key=lambda x: x["name"])
    if group:
        print(f"\n{status_label} :")
        for r in group:
            print(
                f"  {'+' if status_key == 'new' else '~' if status_key == 'modified' else 'x'} {r['name']}  [{r['last_modified']}]"
            )

print(f"\nCache : {CACHE_PATH}")
print(f"CSV   : {csv_path}")

# ── Sync webhook ──────────────────────────────────────────────────────────────
if args.sync:
    payload = {"execution_date": datetime.now().isoformat(), "skills": results, "summary": counts}
    payload_bytes = json.dumps(payload, ensure_ascii=False).encode("utf-8")
    req = urllib.request.Request(
        WEBHOOK_URL,
        data=payload_bytes,
        headers={"Content-Type": "application/json", "User-Agent": "Mozilla/5.0"},
        method="POST",
    )
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            print(f"\nWebhook OK -- {resp.status} {resp.reason}")
            print(f"URL : {WEBHOOK_URL}")
    except Exception as e:
        print(f"\nWebhook ERREUR : {e}")
else:
    print("\nSync desactivee. Relancer avec --sync pour pousser vers Google Sheets.")
    print(f"URL webhook : {WEBHOOK_URL}")
