#!/usr/bin/env python3
"""
Generateur de metadonnees SEO pour les medias WordPress schoolsWP.

Lit le JSON source (288 medias) et genere alt, caption, description
en se basant sur le filename, titre, article parent, langue et type MIME.

Usage:
    python generate-media-metadata.py
"""

import json
import os
import re

# --- Config ---
SOURCE_FILE = (
    r"C:\Users\micha\.claude\projects\d--VS-Code-CLAUDE-CODE-projects-schoolswp"
    r"\2c19ce5b-9047-404d-acb5-971ba2a59fa9\tool-results"
    r"\mcp-novamira-schoolswp-com-mcp-adapter-execute-ability-1774992401284.txt"
)
OUTPUT_FILE = os.path.join(os.path.dirname(__file__), "media-metadata-updates.json")


# --- Helpers ---


def clean_filename(filename: str) -> str:
    """Extrait les mots-cles d'un nom de fichier."""
    # Retirer extension
    name = os.path.splitext(filename)[0]
    # Retirer timestamps (10+ digits)
    name = re.sub(r"-?\d{10,}", "", name)
    # Retirer suffixes type -scaled, _01, -1, etc.
    name = re.sub(r"[-_](scaled|original|full|thumbnail)$", "", name, flags=re.IGNORECASE)
    name = re.sub(r"[-_]\d{1,2}$", "", name)
    # Remplacer separateurs par espaces
    name = re.sub(r"[-_]+", " ", name)
    # Nettoyer espaces multiples
    name = re.sub(r"\s+", " ", name).strip()
    return name


def extract_product_name(filename: str, title: str) -> str:
    """Extrait le nom du produit/plugin depuis le filename ou le titre."""
    # Patterns courants dans les filenames schoolsWP
    text = clean_filename(filename) or title

    # Chercher des noms de produits connus dans le texte
    known_products = [
        "FluentCRM",
        "FluentBooking",
        "FluentSMTP",
        "FluentCart",
        "Fluent Forms",
        "Fluent Support",
        "Fluent Boards",
        "FlyingPress",
        "Kadence",
        "TutorLMS",
        "Tutor LMS",
        "LearnDash",
        "LearnPress",
        "LifterLMS",
        "Academy LMS",
        "MasterStudy",
        "Sensei LMS",
        "SureCart",
        "EasyCommerce",
        "WooCommerce",
        "LatePoint",
        "Amelia",
        "AmeliaWP",
        "Booknetic",
        "OttoKit",
        "SureTriggers",
        "AutomatorWP",
        "Uncanny Automator",
        "Rapyd Cloud",
        "Starter Templates",
        "Jesuspended",
        "Divi",
        "Elementor",
        "Bricks Builder",
        "Breakdance",
        "Rank Math",
        "Link Whisper",
        "Missinglettr",
        "ClickWhale",
        "Easy Content Linker",
        "BuddyBoss",
        "BuddyPress",
        "Jesuspended",
        "Skoatch",
        "Jeunes Etoiles",
        "BeFreelancr",
        "thruuu",
        "Presto Player",
        "Ninja Tables",
        "WP Amelia",
        "SchoolsWP",
        "schoolsWP",
        "WordPress",
        "Gutenberg",
        "SureMembers",
        "Jeuspended",
        "FreshRank",
        "SecuPress",
        "CookieYes",
        "Polylang",
        "WPML",
        "Loco Translate",
    ]

    combined = f"{text} {title}"
    found = None
    for product in known_products:
        if product.lower() in combined.lower():
            found = product
            break

    return found or ""


def guess_image_type(filename: str, mime: str) -> str:
    """Determine le type d'image (logo, screenshot, banner, etc.)."""
    fn_lower = filename.lower()
    if mime == "image/svg+xml" or "logo" in fn_lower:
        return "logo"
    if "banner" in fn_lower or "pinterest" in fn_lower:
        return "banner"
    if any(
        k in fn_lower
        for k in [
            "dashboard",
            "tableau",
            "bordbrett",
            "settings",
            "einstellungen",
            "configuration",
            "interface",
            "screenshot",
            "screen",
            "overview",
            "berichte",
            "reports",
            "pricing",
            "plans",
            "tarif",
            "preis",
            "features",
            "funktionalitaten",
            "integrations",
            "add-ons",
            "editor",
            "builder",
            "template",
            "modele",
        ]
    ):
        return "screenshot"
    if "maxresdefault" in fn_lower or "thumbnail" in fn_lower:
        return "video_thumbnail"
    if mime == "image/png":
        return "illustration"
    return "visuel"


def get_context_from_articles(item: dict) -> str:
    """Extrait le contexte editorial depuis parent_title ou used_in."""
    if item.get("parent_title"):
        return item["parent_title"]
    if item.get("used_in") and len(item["used_in"]) > 0:
        return item["used_in"][0]
    return ""


def _extract_screen_descriptor(filename: str, lang: str) -> str:
    """Traduit les termes du filename en descripteur lisible pour l'alt text."""
    fn = clean_filename(filename).lower()

    # Mapping de termes techniques -> descripteurs par langue
    descriptors = {
        "dashboard": {"fr": "tableau de bord", "de": "Dashboard", "en": "dashboard"},
        "bordbrett": {"fr": "tableau de bord", "de": "Dashboard", "en": "dashboard"},
        "tableau": {"fr": "tableau de bord", "de": "Dashboard", "en": "dashboard"},
        "settings": {"fr": "parametres", "de": "Einstellungen", "en": "settings"},
        "einstellungen": {"fr": "parametres", "de": "Einstellungen", "en": "settings"},
        "configuration": {"fr": "configuration", "de": "Konfiguration", "en": "configuration"},
        "reports": {"fr": "rapports", "de": "Berichte", "en": "reports"},
        "berichte": {"fr": "rapports", "de": "Berichte", "en": "reports"},
        "pricing": {"fr": "tarifs", "de": "Preise", "en": "pricing"},
        "plans": {"fr": "tarifs et plans", "de": "Preise und Plane", "en": "pricing plans"},
        "preis": {"fr": "tarifs", "de": "Preise", "en": "pricing"},
        "tarif": {"fr": "tarifs", "de": "Preise", "en": "pricing"},
        "features": {"fr": "fonctionnalites", "de": "Funktionen", "en": "features"},
        "funktionalitaten": {"fr": "fonctionnalites", "de": "Funktionen", "en": "features"},
        "integrations": {"fr": "integrations", "de": "Integrationen", "en": "integrations"},
        "add-ons": {"fr": "extensions", "de": "Erweiterungen", "en": "add-ons"},
        "editor": {"fr": "editeur", "de": "Editor", "en": "editor"},
        "builder": {"fr": "constructeur", "de": "Builder", "en": "builder"},
        "template": {"fr": "modeles", "de": "Vorlagen", "en": "templates"},
        "overview": {"fr": "vue d'ensemble", "de": "Ubersicht", "en": "overview"},
        "interface": {"fr": "interface", "de": "Oberflache", "en": "interface"},
        "vorschritte": {"fr": "rapports d'avancement", "de": "Fortschrittsberichte", "en": "progress reports"},
    }

    found = []
    for term, translations in descriptors.items():
        if term in fn:
            found.append(translations.get(lang, translations["en"]))

    if found:
        return ", ".join(found[:2])  # Max 2 descripteurs
    return ""


def generate_alt(item: dict, product: str, image_type: str, keywords: str, context: str) -> str:
    """Genere un alt text SEO (max 125 car.)."""
    lang = item["lang"]
    item["mime"]

    if image_type == "logo":
        if lang == "fr":
            alt = f"Logo officiel {product}" if product else f"Logo {keywords}"
            if "wordpress" not in alt.lower() and product:
                alt += ", plugin WordPress"
        elif lang == "de":
            alt = f"Offizielles Logo {product}" if product else f"Logo {keywords}"
            if "wordpress" not in alt.lower() and product:
                alt += ", WordPress-Plugin"
        else:
            alt = f"Official {product} logo" if product else f"{keywords} logo"
            if "wordpress" not in alt.lower() and product:
                alt += ", WordPress plugin"

    elif image_type == "screenshot":
        # Extraire un descripteur court depuis le filename
        detail = _extract_screen_descriptor(item["filename"], lang)
        if lang == "fr":
            if product:
                alt = (
                    f"Capture d'ecran {product} — {detail}"
                    if detail
                    else f"Capture d'ecran de {product} dans WordPress"
                )
            else:
                alt = f"Capture d'ecran {detail or keywords}"
        elif lang == "de":
            if product:
                alt = f"Screenshot {product} — {detail}" if detail else f"Screenshot von {product} in WordPress"
            else:
                alt = f"Screenshot {detail or keywords}"
        else:
            if product:
                alt = f"{product} screenshot — {detail}" if detail else f"{product} screenshot in WordPress"
            else:
                alt = f"Screenshot of {detail or keywords}"

    elif image_type == "video_thumbnail":
        if lang == "fr":
            alt = f"Miniature video {product or keywords}"
        elif lang == "de":
            alt = f"Video-Thumbnail {product or keywords}"
        else:
            alt = f"Video thumbnail {product or keywords}"

    elif image_type == "banner":
        if lang == "fr":
            alt = f"Banniere {product or keywords}"
        elif lang == "de":
            alt = f"Banner {product or keywords}"
        else:
            alt = f"Banner {product or keywords}"

    else:
        # Visuel generique / illustration
        if lang == "fr":
            alt = f"{product or keywords} sur WordPress" if product else keywords
        elif lang == "de":
            alt = f"{product or keywords} auf WordPress" if product else keywords
        else:
            alt = f"{product or keywords} on WordPress" if product else keywords

    # Nettoyer et tronquer
    alt = re.sub(r"\s+", " ", alt).strip()
    alt = alt.rstrip(".,;: ")
    if len(alt) > 125:
        alt = alt[:122].rsplit(" ", 1)[0] + "..."
    return alt


def generate_caption(item: dict, product: str, image_type: str, keywords: str, context: str) -> str:
    """Genere une legende contextuelle."""
    lang = item["lang"]

    # Construire la base du caption
    article_ref = ""
    if context:
        # Extraire un titre court de l'article
        article_ref = context.replace("&amp;", "&")

    if image_type == "logo":
        if lang == "fr":
            caption = f"Logo {product or keywords} — plugin WordPress presente sur schoolsWP."
        elif lang == "de":
            caption = f"Logo von {product or keywords} — WordPress-Plugin vorgestellt auf schoolsWP."
        else:
            caption = f"{product or keywords} logo — WordPress plugin featured on schoolsWP."

    elif image_type == "screenshot":
        if lang == "fr":
            caption = f"Interface {product or keywords} dans WordPress"
            if article_ref:
                caption += ", extrait de l'article schoolsWP."
            else:
                caption += " — guide schoolsWP."
        elif lang == "de":
            caption = f"{product or keywords}-Oberflache in WordPress"
            if article_ref:
                caption += ", aus dem schoolsWP-Artikel."
            else:
                caption += " — schoolsWP-Anleitung."
        else:
            caption = f"{product or keywords} interface in WordPress"
            if article_ref:
                caption += ", from the schoolsWP article."
            else:
                caption += " — schoolsWP guide."

    elif image_type == "video_thumbnail":
        if lang == "fr":
            caption = f"Apercu de la video {product or keywords} sur schoolsWP."
        elif lang == "de":
            caption = f"Vorschau des {product or keywords}-Videos auf schoolsWP."
        else:
            caption = f"{product or keywords} video preview on schoolsWP."

    elif image_type == "banner":
        if lang == "fr":
            caption = f"Banniere promotionnelle {product or keywords} pour l'article schoolsWP."
        elif lang == "de":
            caption = f"Werbebanner {product or keywords} fur den schoolsWP-Artikel."
        else:
            caption = f"{product or keywords} promotional banner for the schoolsWP article."

    else:
        if lang == "fr":
            caption = f"{product or keywords} — illustration de l'article schoolsWP."
        elif lang == "de":
            caption = f"{product or keywords} — Illustration des schoolsWP-Artikels."
        else:
            caption = f"{product or keywords} — illustration from the schoolsWP article."

    return caption.strip()


def generate_description(item: dict, product: str, image_type: str, keywords: str, context: str) -> str:
    """Genere une description editoriale (1-2 phrases)."""
    lang = item["lang"]
    article_ref = context.replace("&amp;", "&") if context else ""

    type_labels = {
        "logo": {"fr": "le logo officiel", "de": "das offizielle Logo", "en": "the official logo"},
        "screenshot": {"fr": "une capture d'ecran", "de": "einen Screenshot", "en": "a screenshot"},
        "video_thumbnail": {"fr": "la miniature de la video", "de": "das Video-Thumbnail", "en": "the video thumbnail"},
        "banner": {"fr": "une banniere visuelle", "de": "ein visuelles Banner", "en": "a visual banner"},
        "illustration": {"fr": "une illustration", "de": "eine Illustration", "en": "an illustration"},
        "visuel": {"fr": "un visuel", "de": "ein Bild", "en": "a visual"},
    }

    type_label = type_labels.get(image_type, type_labels["visuel"])

    subject = product or keywords

    if lang == "fr":
        desc = f"Cette image montre {type_label['fr']} de {subject}."
        if article_ref:
            desc += f' Elle illustre l\'article schoolsWP "{article_ref}".'
        else:
            desc += " Publiee sur schoolsWP dans le cadre d'un guide WordPress."

    elif lang == "de":
        desc = f"Dieses Bild zeigt {type_label['de']} von {subject}."
        if article_ref:
            desc += f' Es illustriert den schoolsWP-Artikel "{article_ref}".'
        else:
            desc += " Veroffentlicht auf schoolsWP im Rahmen eines WordPress-Leitfadens."

    else:
        desc = f"This image shows {type_label['en']} of {subject}."
        if article_ref:
            desc += f' It illustrates the schoolsWP article "{article_ref}".'
        else:
            desc += " Published on schoolsWP as part of a WordPress guide."

    return desc.strip()


def process_item(item: dict) -> dict | None:
    """Traite un item et retourne les champs manquants a completer."""
    missing = item.get("missing", [])
    if not missing:
        return None

    filename = item.get("filename", "")
    title = item.get("title", "")
    keywords = clean_filename(filename) or clean_filename(title) or title
    product = extract_product_name(filename, title)
    image_type = guess_image_type(filename, item.get("mime", ""))
    context = get_context_from_articles(item)

    # Si pas de product et pas de keywords utiles, essayer depuis le contexte
    if not product and context:
        product = extract_product_name(context, context)

    # Capitaliser les keywords si tout en minuscule
    if keywords and keywords == keywords.lower():
        keywords = keywords.title()

    result = {"id": item["id"]}

    if "alt" in missing:
        result["alt"] = generate_alt(item, product, image_type, keywords, context)

    if "caption" in missing:
        result["caption"] = generate_caption(item, product, image_type, keywords, context)

    if "desc" in missing:
        result["description"] = generate_description(item, product, image_type, keywords, context)

    return result


def main():
    # Lire le JSON source
    print("Lecture du fichier source...")
    with open(SOURCE_FILE, "r", encoding="utf-8") as f:
        data = json.load(f)

    items = data["data"]["return_value"]["items"]
    print(f"  {len(items)} medias trouves")

    # Traiter chaque item
    results = []
    stats = {"alt": 0, "caption": 0, "description": 0}

    for item in items:
        result = process_item(item)
        if result:
            results.append(result)
            if "alt" in result:
                stats["alt"] += 1
            if "caption" in result:
                stats["caption"] += 1
            if "description" in result:
                stats["description"] += 1

    # Ecrire le fichier de sortie
    print(f"\nEcriture de {len(results)} items dans {OUTPUT_FILE}")
    os.makedirs(os.path.dirname(OUTPUT_FILE), exist_ok=True)
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        json.dump(results, f, ensure_ascii=False, indent=2)

    print("\nStatistiques:")
    print(f"  Items traites: {len(results)}")
    print(f"  Alt generes: {stats['alt']}")
    print(f"  Captions generees: {stats['caption']}")
    print(f"  Descriptions generees: {stats['description']}")
    print(f"\nFichier: {OUTPUT_FILE}")

    # Apercu des 5 premiers resultats
    print("\nApercu (5 premiers):")
    for r in results[:5]:
        print(f"  ID {r['id']}:")
        for k in ["alt", "caption", "description"]:
            if k in r:
                print(f"    {k}: {r[k][:80]}...")


if __name__ == "__main__":
    main()
