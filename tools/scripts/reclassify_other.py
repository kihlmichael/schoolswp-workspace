"""Reclassify articles from other/andere into correct category folders."""

import json
import os
import subprocess
import sys
import time

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

GWS = os.path.expandvars(r"%APPDATA%\npm\gws.cmd")

EN_DST = "1YsbmU5Dg8R1kEsRPe4McL8BRsyOsB4bn"
DE_DST = "1ZvvmtgKZgb4QJ5ydKJ7Q3_lFCXRP_D1G"

EN_RULES = {
    "wordpress-guides": ["what is", "how to", "guide", "slug", "gutenberg", "create a", "multisite", "playground", "boost your blog", "wordpress plugin and"],
    "design-page-builders": ["elementor", "divi", "beaver", "kadence", "crocoblock", "microthemer", "ninja tables", "presto player", "fse", "full site editing", "droip", "page builder"],
    "ecommerce-wordpress": ["woocommerce", "wpboutik", "surecart", "funnelkit", "cartflows", "launchflows", "storebuilder", "funnel", "bodycommerce", "shopify", "clickfunnels", "alidropship", "barn2", "wpmarmite pay", "virfice"],
    "affiliation-monetization": ["affiliate", "monetiz", "aawp", "clickwhale", "pretty links", "affiliation", "solid affiliate"],
    "forms-crm": ["fluentcrm", "fluent forms", "groundhogg", "getresponse", "sureforms", "mailerpress", "fluentsmtp"],
    "seo-wordpress": ["seo", "linkuma", "seokey", "thot seo", "semrush", "aioseo", "rank math", "link finder", "link whisper", "netlinking", "thruuu", "referencement", "pageradar", "linksclub", "linksgarden"],
    "wordpress-hosting": ["hosting", "copilhost", "easyhoster", "instawp", "tastewp", "zipwp vs", "local wp", "flywheel", "rapyd", "wordpress.com vs", "o2switch", "lws"],
    "member-areas": ["suremember", "wishlist member", "buddyboss", "fluentcommunity", "armember", "membership", "restrict content"],
    "wordpress-performance": ["wp rocket", "flyingpress", "perfmatters", "cache", "speed", "amp de google"],
    "booking-systems": ["booking", "reservation", "amelia", "fluentbooking", "latepoint"],
    "ai-wordpress": ["bertha ai", "skoatch", "zipwp rev", "chatseo", "getgenie"],
    "maintenance-security": ["umbrella", "fluent support", "maintenance", "security", "clean wordpress database", "wpmissioncontrol"],
    "elearning-lms": ["lms", "learndash", "tutor lms", "masteriyo", "academy lms", "formation en ligne", "e-learning"],
    "wordpress-automation": ["suretriggers", "ottokit", "zapier", "automation", "bit flows"],
}

DE_RULES = {
    "wordpress-leitfaden": ["was ist", "wie verwende", "leitfaden", "slug in wordpress", "gutenberg", "erstellen", "multisite", "playground", "grundlagen", "wordpress-plugin ist"],
    "design-wordpress": ["elementor", "divi", "beaver", "kadence", "crocoblock", "microthemer", "ninja tables", "presto player", "fse", "full site editing", "droip"],
    "ecommerce-wordpress": ["woocommerce", "wpboutik", "surecart", "funnelkit", "cartflows", "launchflows", "storebuilder", "funnel", "bodycommerce", "shopify", "clickfunnels", "alidropship", "barn2", "wpmarmite pay", "e-commerce", "online-handel", "virfice", "easycommerce", "fluentcart"],
    "monetarisierung": ["affiliate", "monetar", "aawp", "clickwhale", "pretty links"],
    "formulare-crm": ["fluentcrm", "fluent forms", "groundhogg", "getresponse", "sureforms", "mailerpress", "formular", "fluentsmtp"],
    "seo-wordpress": ["seo", "linkuma", "seokey", "thot", "semrush", "aioseo", "rank math", "link finder", "link whisper", "netlinking", "thruuu", "pageradar", "linksclub", "linksgarden"],
    "hosting-wordpress": ["hosting", "copilhost", "easyhoster", "instawp", "tastewp", "zipwp vs", "local wp", "flywheel", "rapyd", "wordpress.org vs", "o2switch", "lws"],
    "mitgliederbereiche": ["suremember", "wishlist member", "buddyboss", "fluentcommunity", "armember", "mitglied", "restrict content"],
    "geschwindigkeit-leistung": ["wp rocket", "flyingpress", "perfmatters", "cache", "geschwindigkeit", "leistung", "amp"],
    "reservierungen-wordpress": ["booking", "buchung", "amelia", "fluentbooking", "latepoint", "reservier", "termin"],
    "ki-wordpress": ["ki-gespeist", "bertha", "skoatch", "zipwp rev", "chatseo", "getgenie"],
    "wartung-sicherheit": ["umbrella", "fluent support", "wartung", "sicherheit", "datenbank", "wpmissioncontrol"],
    "lernplattformen-lms": ["lms", "learndash", "tutor lms", "masteriyo", "academy lms", "lernplattform"],
    "automatisierungen": ["suretriggers", "ottokit", "zapier", "automatisierung", "bit flows"],
}


def gws(service, resource, action, params=None, json_body=None):
    cmd = [GWS, service, resource, action]
    if params:
        cmd += ["--params", json.dumps(params)]
    if json_body:
        cmd += ["--json", json.dumps(json_body)]
    r = subprocess.run(cmd, capture_output=True, timeout=90, encoding="utf-8", errors="replace")
    stdout = r.stdout or ""
    try:
        j = stdout.find("{")
        if j >= 0:
            return json.loads(stdout[j:])
    except Exception:
        pass
    return None


def classify(file_name, rules):
    name = file_name.lower()
    for folder, keywords in rules.items():
        for kw in keywords:
            if kw in name:
                return folder
    return None


def reclassify(lang, dst_folder, other_slug, rules):
    r = gws(
        "drive", "files", "list",
        params={
            "q": f"'{dst_folder}' in parents and mimeType = 'application/vnd.google-apps.folder' and trashed = false",
            "fields": "files(id,name)",
            "pageSize": 50,
        },
    )
    folders = {f["name"]: f["id"] for f in r.get("files", [])}
    other_id = folders.get(other_slug)
    if not other_id:
        print(f"  ERROR: {other_slug} folder not found")
        return

    r2 = gws(
        "drive", "files", "list",
        params={
            "q": f"'{other_id}' in parents and trashed = false",
            "fields": "files(id,name)",
            "pageSize": 200,
        },
    )
    files = r2.get("files", []) if r2 else []
    print(f"  {len(files)} files in {other_slug}/")

    moved = stayed = 0
    remaining = []
    for f in files:
        target = classify(f["name"], rules)
        if target and target != other_slug and target in folders:
            gws(
                "drive", "files", "update",
                params={"fileId": f["id"], "addParents": folders[target], "removeParents": other_id},
                json_body={},
            )
            moved += 1
            print(f"  {other_slug} -> {target}: {f['name'][:55]}...")
            time.sleep(0.5)
        else:
            stayed += 1
            remaining.append(f["name"])
    print(f"  Result: {moved} moved, {stayed} stayed")
    if remaining:
        print(f"  Remaining in {other_slug}:")
        for n in remaining:
            print(f"    - {n[:70]}")


if __name__ == "__main__":
    print("=== EN: Reclassify other/ ===")
    reclassify("EN", EN_DST, "other", EN_RULES)
    print("\n=== DE: Reclassify andere/ ===")
    reclassify("DE", DE_DST, "andere", DE_RULES)
    print("\nDONE")
