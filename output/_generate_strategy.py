"""Generate thruuu-strategist output: strategy.md + strategy.xlsx + archive input."""
import json
import shutil
from pathlib import Path
from datetime import date

import openpyxl
from openpyxl.styles import Font, PatternFill, Alignment
from openpyxl.utils import get_column_letter

ROOT = Path(__file__).resolve().parent.parent
INPUT_FILE = ROOT / "input" / "thruuu_cluster_report_schoolsWP - 17_04_2026.xlsx"
OUTPUT_DIR = ROOT / "output"
PROCESSED_DIR = ROOT / "input" / "processed"
PROJECT_NAME = "schoolsWP_17_04_2026"
DOMAIN = "schoolswp.com"
DOMAIN_PR = 28
PLAN_SIZE = 20
WEEKLY_CAP = 3

# ======= MANUAL CLASSIFICATION (from Claude reasoning) =======
# Schema per entry: topic_key -> {action, format, priority, reasoning, notes}
# Topics normalized lowercase for matching.
CLASS: dict[str, dict] = {
    # === TOP 20 (P1 + P2) ===
    "lms": {"action": "Create", "format": "Article + Video", "priority": "P1",
            "reasoning": "Pilier core schoolsWP (Academy Tutor LMS). Aucune page, Moderate comp (PR 30), gros volume 12 100. Video 100 % impose duo article + YouTube.",
            "rank": 1},
    "o2switch": {"action": "Create", "format": "Article + Video", "priority": "P1",
            "reasoning": "Ton hébergeur actuel = expérience réelle à valoriser. Affiliate disponible. Volume 33 100, Moderate comp. Core pilier hébergement.",
            "rank": 2},
    "tutor lms": {"action": "Optimize", "format": "Article + Video", "priority": "P1",
            "reasoning": "Page existante pos 12, zone d'optimisation. URL matche l'intention commerciale. Product-market fit maximum (Academy tourne dessus). Quick win top 10.",
            "rank": 3},
    "seo wordpress": {"action": "Create", "format": "Article + Video", "priority": "P1",
            "reasoning": "Pillar SEO, cannibalisation probable avec Référencement WordPress — fusionner en UN seul pilier FR. Moderate comp (PR 39), hub-level topic.",
            "rank": 4, "notes": "Fusionner avec cluster Référencement Wordpress (880 vol) — même intention SEO FR."},
    "membership": {"action": "Create", "format": "Article + Video", "priority": "P1",
            "reasoning": "Pilier /espaces-membres-wordpress/ (7 articles déjà). Volume 3 600 info intent = pilier hub. Moderate comp (PR 38).",
            "rank": 5},
    "monétisation": {"action": "Create", "format": "Article + Video", "priority": "P1",
            "reasoning": "Pilier monétisation/affiliation = revenue core schoolsWP (8 articles cat). High comp (PR 48) mais enjeu stratégique maximum. Hub-level.",
            "rank": 6},
    "droip": {"action": "Create", "format": "Article", "priority": "P1",
            "reasoning": "Gros volume 40 500, PR 35 Moderate. No-code builder concurrent Elementor/Divi. Affiliate opportunity. Video 0 % → article seul.",
            "rank": 7},
    "elementor": {"action": "Create", "format": "Article + Video", "priority": "P1",
            "reasoning": "Volume 9 900, competitor direct Kadence. Angle comparatif ou review Elementor pour audience schoolsWP qui compare. Moderate comp (PR 37).",
            "rank": 8},
    "divi": {"action": "Create", "format": "Article + Video", "priority": "P2",
            "reasoning": "PR 24 Low (sous ta PR 28). Volume 4 400. Competitor à Kadence, nombreux Divi-adjacent déjà couverts (Pixel, Machine, Toolbox).",
            "rank": 9},
    "linkuma": {"action": "Create", "format": "Article", "priority": "P2",
            "reasoning": "PR 24 Low. Volume 3 600 commercial. Plugin FR affiliation. Video 0 %. Affiliate opportunity.",
            "rank": 10},
    "systeme.io": {"action": "Create", "format": "Article + Video", "priority": "P2",
            "reasoning": "Angle comparatif Systeme.io vs WordPress — clé pour audience qui compare no-code all-in-one vs stack WP. Gros volume 33 100, PR 42 High.",
            "rank": 11, "notes": "Angle obligatoire : comparatif, pas review directe (concurrent de WP)."},
    "wp rocket": {"action": "Create", "format": "Article + Video", "priority": "P2",
            "reasoning": "Volume 2 900, PR 40 High. Comparatif FlyingPress vs WP Rocket existe déjà. Cet article = review directe pour compléter. Affiliate.",
            "rank": 12},
    "wp umbrella": {"action": "Create", "format": "Article + Video", "priority": "P2",
            "reasoning": "Tu l'utilises (monitoring schoolswp.com). Expérience réelle + affiliate. Volume 880, Moderate comp (PR 32).",
            "rank": 13},
    "befreelancr": {"action": "Create", "format": "Article + Video", "priority": "P2",
            "reasoning": "Audience freelances WP = cœur de cible. Transactional intent (signup). Volume 480, PR 31 Moderate. Marketplace FR.",
            "rank": 14},
    "seokey": {"action": "Create", "format": "Article", "priority": "P2",
            "reasoning": "Plugin SEO FR, pilier SEO. PR 34 Moderate. Video 0 % → Article. Volume 480 modeste mais audience ciblée.",
            "rank": 15},
    "thruuu": {"action": "Create", "format": "Article + Video", "priority": "P2",
            "reasoning": "Tu l'utilises pour ton SEO ops. Expérience réelle + affiliate. Info intent = review/explain. Volume 260, PR 39 Moderate.",
            "rank": 16},
    "performance wordpress": {"action": "Create", "format": "Article + Video", "priority": "P2",
            "reasoning": "PR 28 = ta PR = Low comp. Pilier /performance-wordpress/. Volume 70 bas mais hub-level. Video 100 %.",
            "rank": 17, "notes": "Opportunité low-comp rare à ne pas manquer."},
    "traduction wordpress": {"action": "Create", "format": "Article", "priority": "P2",
            "reasoning": "Pilier multilingue. Polylang + Traduire Sans Migraine = expérience réelle. PR 42 High mais pilier stratégique. Video 0 % → Article.",
            "rank": 18},
    "copilhost": {"action": "Optimize", "format": "Article + Video", "priority": "P2",
            "reasoning": "Page existante pos 12, zone optimisation. PR 28 = Low comp. Optimiser pour passer top 10. Hébergement niche FR.",
            "rank": 19},
    "5euros": {"action": "Optimize", "format": "Article + Video", "priority": "P2",
            "reasoning": "Page pos 10, borderline optimization. Volume 2 400. Light refresh suffit pour passer top 5. Faible effort.",
            "rank": 20},

    # === BACKLOG IMMEDIAT (ranks 21-34) ===
    "amelia": {"action": "Create", "format": "Article + Video", "priority": "P3",
            "reasoning": "Angle comparatif Amelia vs FluentBooking (ton stack). Volume 9 900, High comp (PR 44). Backlog.",
            "rank": 21},
    "localwp": {"action": "Optimize", "format": "Article + Video", "priority": "P3",
            "reasoning": "Page pos 10, PR 26 Low. Quick-win easy. Volume 1 600 modeste.",
            "rank": 22},
    "pretty links": {"action": "Create", "format": "Article + Video", "priority": "P3",
            "reasoning": "Comparatif ClickWhale vs Pretty Links déjà en place. Article review direct = bonus.",
            "rank": 23},
    "cartflows": {"action": "Create", "format": "Article + Video", "priority": "P3",
            "reasoning": "Comparatif Launchflows vs Cartflows existe. Review Cartflows = complément.",
            "rank": 24},
    "perfmatters": {"action": "Optimize", "format": "Article + Video", "priority": "P3",
            "reasoning": "Pos 12, PR 36 Moderate. Niche performance.",
            "rank": 25},
    "plugin de réservation wordpress": {"action": "Create", "format": "Article + Video", "priority": "P3",
            "reasoning": "Pilier réservations. Low vol 110. Angle : tour d'horizon + FluentBooking.",
            "rank": 26},
    "elementskit": {"action": "Create", "format": "Article + Video", "priority": "P3",
            "reasoning": "Addon Elementor, pas ton stack. PR 36 Moderate. Niche.",
            "rank": 27},
    "fluentsmtp": {"action": "Create", "format": "Article", "priority": "P3",
            "reasoning": "Tu l'utilises. Expérience réelle + affiliate Fluent. PR 58 High. Volume 50 très bas.",
            "rank": 28},
    "aawp": {"action": "Create", "format": "Article + Video", "priority": "P3",
            "reasoning": "PR 27 Low (opportunité). Amazon affiliate angle. Volume 70. Tangent par rapport à ton stack principal.",
            "rank": 29},
    "wordpress e-learning": {"action": "Create", "format": "Article + Video", "priority": "P3",
            "reasoning": "Variant sémantique LMS. Low vol 20. Complément pilier LMS, risque cannibalisation avec cluster LMS.",
            "rank": 30},
    "metricool": {"action": "Create", "format": "Article", "priority": "P3",
            "reasoning": "Volume 36 200 mais off-core (social media). Ton stack social = Blotato. Angle review/comparatif borderline.",
            "rank": 31, "notes": "Garder en veille, réévaluer si tu lances un cocon social media management."},
    "rapyd cloud": {"action": "Create", "format": "Article + Video", "priority": "P3",
            "reasoning": "Hosting WP managed. Volume 0 (trop bas). Pilier hébergement.",
            "rank": 32},
    "slug seo wordpress": {"action": "Optimize", "format": "Article + Video", "priority": "P3",
            "reasoning": "Page pos 12. Volume 10. Micro-opti SEO.",
            "rank": 33},
    "lms wordpress": {"action": "Optimize", "format": "—", "priority": "P3",
            "reasoning": "URL est une page catégorie hub. Pos 8. Optimiser le contenu de la catégorie elle-même.",
            "rank": 34},

    # === MONITOR (existing URL in top 10) ===
    "kadence": {"action": "No action", "format": "—", "priority": "Monitor",
            "reasoning": "Page pos 7 sur topic core (thème Discover enfant Kadence). Performe.",
            "rank": None},
    "zipwp": {"action": "No action", "format": "—", "priority": "Monitor",
            "reasoning": "Pos 5, PR 31. Performe.",
            "rank": None},
    "chatseo": {"action": "No action", "format": "—", "priority": "Monitor", "reasoning": "Pos 6, PR 22 Low. Performe.", "rank": None},
    "thot seo": {"action": "No action", "format": "—", "priority": "Monitor", "reasoning": "Pos 10 borderline, PR 29. Monitor.", "rank": None},
    "crocoblock": {"action": "No action", "format": "—", "priority": "Monitor", "reasoning": "Pos 9, PR 31. Performe.", "rank": None},
    "flyingpress": {"action": "No action", "format": "—", "priority": "Monitor", "reasoning": "Pos 2 excellent.", "rank": None},
    "learndash": {"action": "No action", "format": "—", "priority": "Monitor", "reasoning": "Pos 6, PR 31.", "rank": None},
    "divi pixel": {"action": "No action", "format": "—", "priority": "Monitor", "reasoning": "Pos 2, PR 28.", "rank": None},
    "link whisper": {"action": "No action", "format": "—", "priority": "Monitor", "reasoning": "Pos 6.", "rank": None},
    "fluent forms": {"action": "No action", "format": "—", "priority": "Monitor", "reasoning": "Pos 7, performe.", "rank": None},
    "surecart": {"action": "No action", "format": "—", "priority": "Monitor", "reasoning": "Pos 9, PR 46 High mais performe.", "rank": None},
    "skoatch": {"action": "No action", "format": "—", "priority": "Monitor", "reasoning": "Pos 6, PR 22.", "rank": None},
    "fluentcrm": {"action": "No action", "format": "—", "priority": "Monitor", "reasoning": "Pos 8, core affiliate. Surveiller si passe top 5.", "rank": None},
    "wishlist member": {"action": "No action", "format": "—", "priority": "Monitor", "reasoning": "Pos 2.", "rank": None},
    "latepoint": {"action": "No action", "format": "—", "priority": "Monitor", "reasoning": "Pos 4.", "rank": None},
    "wp social ninja": {"action": "No action", "format": "—", "priority": "Monitor", "reasoning": "Pos 4, stack schoolsWP.", "rank": None},
    "suremembers": {"action": "No action", "format": "—", "priority": "Monitor", "reasoning": "Pos 5.", "rank": None},
    "divi machine": {"action": "No action", "format": "—", "priority": "Monitor", "reasoning": "Pos 4.", "rank": None},
    "funnelkit": {"action": "No action", "format": "—", "priority": "Monitor", "reasoning": "Pos 6.", "rank": None},
    "tastewp": {"action": "No action", "format": "—", "priority": "Monitor", "reasoning": "Pos 5.", "rank": None},
    "skeall": {"action": "No action", "format": "—", "priority": "Monitor", "reasoning": "Pos 3.", "rank": None},
    "restrict content pro": {"action": "No action", "format": "—", "priority": "Monitor", "reasoning": "Pos 10 borderline, PR 26.", "rank": None},
    "armember": {"action": "No action", "format": "—", "priority": "Monitor", "reasoning": "Pos 5.", "rank": None},
    "academy lms": {"action": "No action", "format": "—", "priority": "Monitor", "reasoning": "Pos 3.", "rank": None},
    "divi toolbox": {"action": "No action", "format": "—", "priority": "Monitor", "reasoning": "Pos 3.", "rank": None},
    "aioseo / all in one seo": {"action": "No action", "format": "—", "priority": "Monitor", "reasoning": "Pos 8.", "rank": None},
    "launchflows": {"action": "No action", "format": "—", "priority": "Monitor", "reasoning": "Pos 3.", "rank": None},
    "affiliatepress": {"action": "No action", "format": "—", "priority": "Monitor", "reasoning": "Pos 3.", "rank": None},
    "plateforme de formation avec wordpress": {"action": "No action", "format": "—", "priority": "Monitor", "reasoning": "Pos 2.", "rank": None},
    "solid affiliate": {"action": "No action", "format": "—", "priority": "Monitor", "reasoning": "Pos 3.", "rank": None},
    "bodycommerce": {"action": "No action", "format": "—", "priority": "Monitor", "reasoning": "Pos 2.", "rank": None},
    "clickwhale": {"action": "No action", "format": "—", "priority": "Monitor", "reasoning": "Pos 3.", "rank": None},
    "fluentcommunity": {"action": "No action", "format": "—", "priority": "Monitor", "reasoning": "Pos 7.", "rank": None},
    "fluent support": {"action": "No action", "format": "—", "priority": "Monitor", "reasoning": "Pos 3.", "rank": None},
    "fluentbooking": {"action": "No action", "format": "—", "priority": "Monitor", "reasoning": "Pos 2.", "rank": None},
    "fluentcart": {"action": "No action", "format": "—", "priority": "Monitor", "reasoning": "Pos 6.", "rank": None},
    "fluentboards": {"action": "No action", "format": "—", "priority": "Monitor", "reasoning": "Pos 3.", "rank": None},

    # === SKIP ===
    "fiverr": {"action": "Skip", "format": "—", "priority": "—",
            "reasoning": "Off-brand confirmé par le client. Volume 135 000 trompeur, PR 44 High, intention de recherche hors positionnement WordPress.",
            "rank": None},
    "comparatifs entre plugins": {"action": "Skip", "format": "—", "priority": "—",
            "reasoning": "Volume 0, requête générique sans intention claire.", "rank": None},
    "lms / membership": {"action": "Skip", "format": "—", "priority": "—",
            "reasoning": "Redondance avec clusters LMS et Membership traités individuellement. Volume 10.", "rank": None},
    "création de plateforme": {"action": "Skip", "format": "—", "priority": "—",
            "reasoning": "Redondance avec Plateforme De Formation Avec WordPress (existant pos 2). Volume 10.", "rank": None},
    "référencement wordpress": {"action": "Create", "format": "Article + Video", "priority": "P1",
            "reasoning": "Fusionné avec cluster SEO WordPress (rank 4) — même intention SEO FR. Ne pas créer deux articles séparés.",
            "rank": None, "notes": "Intégré au pillar SEO WordPress (rank 4)."},
}

def normalize(topic: str) -> str:
    return (topic or "").strip().lower()


def classify(cluster: dict) -> dict:
    key = normalize(cluster.get("Topic/Cluster", ""))
    c = CLASS.get(key)
    if not c:
        return {"action": "No action", "format": "—", "priority": "Monitor",
                "reasoning": "Non classifié (fallback monitor).", "rank": None, "notes": ""}
    return {**c, "notes": c.get("notes", "")}


def competition_tier(pr: int | None) -> str:
    if not pr:
        return "Unknown"
    if pr < DOMAIN_PR:
        return "Low"
    if pr <= DOMAIN_PR + 10:
        return "Moderate"
    return "High"


def clean_url(url: str | None) -> str:
    if not url:
        return "(none)"
    if "?srsltid=" in url:
        url = url.split("?srsltid=")[0]
    return url.replace("https://schoolswp.com", "")


def main():
    # Load clusters
    wb_in = openpyxl.load_workbook(INPUT_FILE, data_only=True)
    ws = wb_in["Topic Clusters"]
    rows = list(ws.iter_rows(values_only=True))
    headers = list(rows[0])
    clusters = [dict(zip(headers, r)) for r in rows[1:]]

    ws_comp = wb_in["Competitors"]
    comp_rows = list(ws_comp.iter_rows(values_only=True))
    comp_headers = list(comp_rows[0])
    competitors = [dict(zip(comp_headers, r)) for r in comp_rows[1:]]

    # Classify
    for c in clusters:
        c["_cls"] = classify(c)
        c["_comp"] = competition_tier(c.get("Avg PR"))
        c["_clean_url"] = clean_url(c.get("Best URL"))

    # Sort by rank (top 20), then backlog, then monitor/skip
    top20 = sorted([c for c in clusters if c["_cls"]["rank"] and c["_cls"]["rank"] <= 20],
                   key=lambda c: c["_cls"]["rank"])
    backlog = sorted([c for c in clusters if c["_cls"]["rank"] and c["_cls"]["rank"] > 20],
                     key=lambda c: c["_cls"]["rank"])
    monitors = [c for c in clusters if c["_cls"]["priority"] == "Monitor"]
    skips = [c for c in clusters if c["_cls"]["action"] == "Skip"]

    # Stats
    total = len(clusters)
    with_url = sum(1 for c in clusters if c.get("Best URL"))
    without_url = total - with_url

    # === XLSX OUTPUT ===
    OUTPUT_DIR.mkdir(exist_ok=True)
    wb_out = openpyxl.Workbook()
    wb_out.remove(wb_out.active)

    # --- Tab 1: Content Plan ---
    ws1 = wb_out.create_sheet("Content Plan")
    ws1_headers = ["#", "Topic", "Keywords", "Action", "Format", "Priority", "Intent",
                   "Competition", "Reasoning", "Notes", "Best URL", "Avg Position", "Aggregated Volume"]
    ws1.append(ws1_headers)
    for i, c in enumerate(top20, 1):
        cls = c["_cls"]
        ws1.append([
            i,
            c.get("Topic/Cluster"),
            c.get("Keywords"),
            cls["action"],
            cls["format"],
            cls["priority"],
            c.get("Intent"),
            f"{c['_comp']} ({c.get('Avg PR')})",
            cls["reasoning"],
            cls.get("notes", ""),
            c["_clean_url"],
            c.get("Avg Position") or "—",
            c.get("Aggregated Volume"),
        ])

    # --- Tab 2: Content Calendar ---
    ws2 = wb_out.create_sheet("Content Calendar")
    ws2.append(["Week", "Topic", "Action", "Format", "Priority"])
    for i, c in enumerate(top20):
        week = (i // WEEKLY_CAP) + 1
        cls = c["_cls"]
        ws2.append([
            week,
            c.get("Topic/Cluster"),
            cls["action"],
            cls["format"],
            cls["priority"],
        ])

    # --- Tab 3: AIO Monitoring ---
    ws3 = wb_out.create_sheet("AIO Monitoring")
    ws3.append(["Topic", "Keyword", "AIO Feature %", "Intent", "Rationale"])
    ws3.append(["—", "—", "—", "—",
                "ANOMALIE : colonne AIO Feature vide dans l'export thruuu. Données non disponibles. Activer AIO Monitoring directement dans thruuu.com pour le domaine schoolswp.com."])

    # --- Tab 4: All Clusters Annotated ---
    ws4 = wb_out.create_sheet("All Clusters Annotated")
    all_headers = headers + ["Action", "Format", "Priority", "Rank", "Notes"]
    ws4.append(all_headers)
    for c in sorted(clusters, key=lambda c: c["_cls"]["rank"] or 999):
        row = [c.get(h) for h in headers]
        cls = c["_cls"]
        row.extend([cls["action"], cls["format"], cls["priority"], cls["rank"] or "—", cls.get("notes", "")])
        ws4.append(row)

    # Styling: header row bold for all sheets
    for sheet in wb_out.worksheets:
        for cell in sheet[1]:
            cell.font = Font(bold=True)
            cell.fill = PatternFill(start_color="D9E1F2", end_color="D9E1F2", fill_type="solid")
        # Auto-adjust column widths (approximation)
        for col_idx, col in enumerate(sheet.columns, 1):
            max_len = max(len(str(cell.value or "")) for cell in col)
            sheet.column_dimensions[get_column_letter(col_idx)].width = min(max_len + 2, 60)

    xlsx_out = OUTPUT_DIR / f"{PROJECT_NAME}_strategy.xlsx"
    wb_out.save(xlsx_out)

    # === MD OUTPUT ===
    # Stats derived
    p1_count = sum(1 for c in top20 if c["_cls"]["priority"] == "P1")
    p2_count = sum(1 for c in top20 if c["_cls"]["priority"] == "P2")
    creates = sum(1 for c in top20 if c["_cls"]["action"] == "Create")
    optimizes = sum(1 for c in top20 if c["_cls"]["action"] == "Optimize")
    weeks = (PLAN_SIZE + WEEKLY_CAP - 1) // WEEKLY_CAP

    top_competitors = sorted(competitors, key=lambda c: c.get("Clusters Visibility", 0) or 0, reverse=True)[:5]

    md_lines = [
        f"# Content Strategy: {PROJECT_NAME}",
        "",
        "## Executive Summary",
        "",
        f"schoolswp.com est **déjà #1 en visibilité clusters** sur ce dataset (58 vs wordpress.org 47), "
        f"malgré une PR 28 inférieure à 4 des 5 premiers concurrents. L'avantage est l'affinité sujet — "
        f"pas la puissance domaine. Le plan consolide cet avantage sur les **hubs non encore couverts "
        f"(LMS, SEO, Monétisation, Membership)** tout en optimisant les pages frontière top 10-15 où un "
        f"simple refresh débloque des gains immédiats. À éviter : Fiverr (135k vol) et autres requêtes "
        f"off-brand, où le volume trompe sur le vrai match d'intention.",
        "",
        f"Le plan contient **{p1_count} items P1 + {p2_count} items P2** ({creates} Create + {optimizes} Optimize), "
        f"schedulé sur **{weeks} semaines à {WEEKLY_CAP} pièces/semaine**.",
        "",
        "### Stats",
        "",
        f"- **Domain** : {DOMAIN}",
        f"- **Domain strength** : PR {DOMAIN_PR}, classé **#1** sur la visibilité clusters parmi {len(competitors)} concurrents",
        f"- **Top competitors** :",
    ]
    for comp in top_competitors:
        md_lines.append(f"  - {comp.get('Website')} — PR {comp.get('Page Rank')}, "
                        f"Clusters Visibility {comp.get('Clusters Visibility')}, "
                        f"Top 10 KW {comp.get('Top 10 KW Visibility')}")
    md_lines.extend([
        f"- **Clusters analyzed** : {total}",
        f"- **With existing coverage** : {with_url} ({with_url * 100 // total} %)",
        f"- **Without coverage** : {without_url} ({without_url * 100 // total} %)",
        f"- **Content pieces recommended** : {PLAN_SIZE} (+ {len(backlog)} en backlog immédiat)",
        f"- **Estimated timeline** : {weeks} semaines à {WEEKLY_CAP}/semaine",
        "",
        "### À regarder en priorité",
        "",
        "- **LMS (rank 1)** — le plus gros cluster on-brand sans page existante. Volume 12 100, Moderate comp. À lancer en Semaine 1.",
        "- **Tutor LMS (rank 3)** — Optimize à faible effort (pos 12 → top 10). Quick win sur un topic cœur produit.",
        "- **Signal Video omniprésent** — 89 % des clusters ont ≥50 % Video Feature. Le duo Article + Vidéo YouTube devient le format par défaut, pas l'exception.",
        "- **AIO non trackable sur cet export** — colonne vide. Activer AIO Monitoring directement dans thruuu.com pour combler ce trou.",
        "",
        "## Content Plan",
        "",
        "| # | Topic | Action | Format | Priority | Intent | Best URL | Avg Pos | Vol | Competition | Reasoning |",
        "| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |",
    ])
    for i, c in enumerate(top20, 1):
        cls = c["_cls"]
        md_lines.append(
            f"| {i} | {c.get('Topic/Cluster')} | {cls['action']} | {cls['format']} | {cls['priority']} "
            f"| {c.get('Intent') or '—'} | `{c['_clean_url']}` | {c.get('Avg Position') or '—'} "
            f"| {c.get('Aggregated Volume'):,} | {c['_comp']} ({c.get('Avg PR')}) | {cls['reasoning']} |"
        )
    md_lines.extend([
        "",
        "> **Next step pour chaque topic** : ouvrir le cluster dans thruuu.com, analyser le contenu concurrent, cliquer Download Brief, puis invoquer `thruuu-writer` sur le `.docx` récupéré.",
        "",
        "## Content Calendar",
        "",
    ])
    for w in range(1, weeks + 1):
        md_lines.append(f"### Semaine {w}")
        md_lines.append("")
        for i, c in enumerate(top20):
            if (i // WEEKLY_CAP) + 1 == w:
                cls = c["_cls"]
                md_lines.append(f"- **{c.get('Topic/Cluster')}** — {cls['action']} — {cls['format']} — {cls['priority']}")
        md_lines.append("")

    md_lines.extend([
        "## AIO Visibility Opportunities",
        "",
        "> **ANOMALIE détectée** : la colonne `AIO Feature (%)` de l'export est vide (0 % sur les 76 clusters). "
        "Soit thruuu n'a pas activé le tracking AIO pour cet export, soit — plus probable en FR — l'AIO ne "
        "déclenche pas encore sur ces requêtes. **Aucune recommandation AIO Monitoring fiable ne peut être "
        "produite depuis cet export.**",
        "",
        "**Action recommandée** : dans thruuu.com, pour le projet schoolsWP, activer AIO Monitoring manuellement "
        "sur les clusters P1+P2 de ce plan et re-exporter d'ici 4 semaines.",
        "",
        "## Pages Ranking for Multiple Topics",
        "",
        "Aucune page de schoolswp.com ne rank actuellement sur plusieurs clusters dans ce dataset (0 Best URL "
        "dupliquée détectée). Cela signifie que chaque article cible une intention distincte — bon signe de propreté éditoriale.",
        "",
        "## Skipped Clusters",
        "",
        "| Topic | Reason |",
        "| --- | --- |",
    ])
    for c in skips:
        md_lines.append(f"| {c.get('Topic/Cluster')} | {c['_cls']['reasoning']} |")

    md_lines.extend([
        "",
        "## Backlog immédiat (rangs 21-34)",
        "",
        "Topics à reprendre après exécution du plan de 20 ou si capacité supplémentaire apparaît.",
        "",
        "| # | Topic | Action | Format | Priority | Vol | Competition | Reasoning |",
        "| --- | --- | --- | --- | --- | --- | --- | --- |",
    ])
    for c in backlog:
        cls = c["_cls"]
        md_lines.append(
            f"| {cls['rank']} | {c.get('Topic/Cluster')} | {cls['action']} | {cls['format']} | {cls['priority']} "
            f"| {c.get('Aggregated Volume'):,} | {c['_comp']} ({c.get('Avg PR')}) | {cls['reasoning']} |"
        )

    md_lines.extend([
        "",
        "## Clusters en Monitor (existing top 10)",
        "",
        f"{len(monitors)} clusters avec page existante en top 10. Surveiller la stabilité positionnelle — aucune production requise.",
        "",
        "<details><summary>Liste complète ({} clusters)</summary>".format(len(monitors)),
        "",
        "| Topic | Pos | PR | URL |",
        "| --- | --- | --- | --- |",
    ])
    for c in sorted(monitors, key=lambda c: c.get("Avg Position") or 99):
        md_lines.append(f"| {c.get('Topic/Cluster')} | {c.get('Avg Position') or '—'} | {c.get('Avg PR')} | `{c['_clean_url']}` |")
    md_lines.extend([
        "",
        "</details>",
        "",
        "## Key Reasoning Notes",
        "",
        "- **Fiverr (rank off)** : off-brand confirmé. Volume 135k trompeur — intention de recherche pointe vers Fiverr lui-même et comparateurs généralistes, pas vers un média WP.",
        "- **SEO WordPress + Référencement Wordpress** : fusionnés en UN seul pilier (rank 4). Sinon cannibalisation sémantique garantie.",
        "- **Performance WordPress (rank 17)** : volume faible (70) mais PR 28 = ta PR = Low comp. Opportunité low-comp rare, élevée en P2.",
        "- **Divi / Linkuma (ranks 9, 10)** : PR 24 (Low), sous ta PR 28. Attaque dès que possible.",
        "- **Systeme.io (rank 11)** : angle obligatoire **comparatif** WordPress vs Systeme.io — jamais review directe (concurrent du stack cœur).",
        "- **Self-experience cluster** : O2switch, WP Umbrella, thruuu, FluentSMTP, Polylang/Traduction — angle à forte E-E-A-T, prioriser dans la rédaction.",
        "- **Format par défaut = Article + Video** pour 89 % des clusters (SERP video ≥50 %). Article seul uniquement si Video 0 %.",
        "- **Backlog immédiat** : 14 items ranks 21-34 documentés. Ranks 21-35 demandés : arrêté à 34 faute de candidats crédibles supplémentaires (les 38 Monitor + 4 Skip couvrent les 76 - 20 - 14 = 42 restants).",
        "",
        "## Next steps concret",
        "",
        "1. Ouvrir [thruuu.com](https://thruuu.com) → projet `schoolsWP - 17/04/2026`",
        "2. Pour chaque cluster P1 de Semaine 1 (LMS, O2switch, Tutor LMS), cliquer **Download Brief** pour générer le `.docx`",
        f"3. Déposer les briefs dans `{ROOT}/briefs/`",
        "4. Invoquer le skill **`thruuu-writer`** sur chaque brief → articles `.md` dans `drafts/`",
        "5. Relecture humaine + publication WordPress",
    ])

    md_out = OUTPUT_DIR / f"{PROJECT_NAME}_strategy.md"
    md_out.write_text("\n".join(md_lines), encoding="utf-8")

    # === Move input to processed/ ===
    PROCESSED_DIR.mkdir(exist_ok=True)
    processed_path = PROCESSED_DIR / INPUT_FILE.name
    shutil.move(str(INPUT_FILE), str(processed_path))

    # === Cleanup raw json ===
    raw_json = OUTPUT_DIR / "_clusters_raw.json"
    if raw_json.exists():
        raw_json.unlink()

    # === Summary ===
    print(f"✓ Strategy MD:   {md_out}")
    print(f"✓ Strategy XLSX: {xlsx_out}")
    print(f"✓ Input moved:   {processed_path}")
    print()
    print(f"Top 20: {len(top20)} ({p1_count} P1 + {p2_count} P2)")
    print(f"Backlog: {len(backlog)} (ranks 21-34)")
    print(f"Monitor: {len(monitors)}")
    print(f"Skip: {len(skips)}")
    print(f"Total classified: {len(top20) + len(backlog) + len(monitors) + len(skips)} / {total}")


if __name__ == "__main__":
    main()
