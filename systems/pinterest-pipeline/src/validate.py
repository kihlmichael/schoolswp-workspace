"""Validation JSON et regles metier pour le pipeline Pinterest schoolsWP."""

import json
import logging
from pathlib import Path

logger = logging.getLogger("agents.pinterest.validate")

PIPELINE_DIR = Path(__file__).resolve().parent.parent
SCHEMA_PATH = PIPELINE_DIR / "schemas" / "pin.schema.json"
BOARDS_PATH = PIPELINE_DIR / "data" / "boards.json"

# Board keys valides
VALID_BOARD_KEYS = {
    "wordpress-guides",
    "seo-wordpress",
    "lms-wordpress",
    "crm-email",
    "automatisation",
    "plugins",
    "ecommerce",
    "freelance",
    "strategie-contenu",
    "coulisses",
}

# Mots interdits schoolsWP (branding)
FORBIDDEN_WORDS = [
    "disruptif",
    "game changer",
    "scalable",
    "hack",
    "growth hack",
    "révolutionnaire",
    "revolutionnaire",
    "incroyable",
    "le meilleur du marché",
    "en un clic",
    "sans effort",
    "il suffit de",
]

# Statuts valides
VALID_STATUSES = {
    "idea",
    "brief_generated",
    "brief_approved",
    "design_generated",
    "design_approved",
    "exported",
    "publish_approved",
    "published",
    "analytics_synced",
    "archived",
}


def validate_pin(pin: dict) -> list[str]:
    """Valide un pin selon les regles metier.

    Returns:
        Liste d'erreurs. Vide si le pin est valide.
    """
    errors = []

    # Champs requis
    required = ["id", "source_url", "title", "description", "destination_url", "board_key", "status"]
    for field in required:
        if not pin.get(field):
            errors.append(f"Champ requis manquant : {field}")

    # ID format
    pin_id = pin.get("id", "")
    if pin_id and not pin_id.startswith("pin-"):
        errors.append(f"ID invalide : {pin_id} (doit commencer par 'pin-')")

    # Title length
    title = pin.get("title", "")
    if title and (len(title) < 10 or len(title) > 100):
        errors.append(f"Titre hors limites : {len(title)} car. (attendu 10-100)")

    # Description length
    desc = pin.get("description", "")
    if desc and (len(desc) < 50 or len(desc) > 500):
        errors.append(f"Description hors limites : {len(desc)} car. (attendu 50-500)")

    # Board key
    board_key = pin.get("board_key", "")
    if board_key and board_key not in VALID_BOARD_KEYS:
        errors.append(f"Board key invalide : {board_key}")

    # Status
    status = pin.get("status", "")
    if status and status not in VALID_STATUSES:
        errors.append(f"Statut invalide : {status}")

    # Overlay text (3-7 mots)
    overlay = pin.get("overlay_text", "")
    if overlay:
        word_count = len(overlay.split())
        if word_count < 3 or word_count > 7:
            errors.append(f"Overlay text : {word_count} mots (attendu 3-7)")

    # URLs
    for url_field in ["source_url", "destination_url"]:
        url = pin.get(url_field, "")
        if url and not url.startswith("https://"):
            errors.append(f"{url_field} doit commencer par https://")

    # Mots interdits dans title + description
    text_to_check = f"{title} {desc}".lower()
    for word in FORBIDDEN_WORDS:
        if word.lower() in text_to_check:
            errors.append(f"Mot interdit detecte : '{word}'")

    # Anti-doublon : publish_approved sans published_pin_id
    if pin.get("status") == "published" and not pin.get("published_pin_id"):
        errors.append("Pin marque 'published' sans published_pin_id")

    # Content hash
    if pin.get("status") not in ("idea",) and not pin.get("content_hash"):
        errors.append("content_hash manquant pour un pin hors status 'idea'")

    return errors


def validate_queue(queue_path: Path | None = None) -> dict:
    """Valide toute la file de production.

    Returns:
        {valid: bool, total: int, errors: {pin_id: [erreurs]}}
    """
    path = queue_path or (PIPELINE_DIR / "data" / "pins_queue.json")
    with open(path, encoding="utf-8") as f:
        data = json.load(f)

    results = {"valid": True, "total": 0, "errors": {}}

    for pin in data.get("pins", []):
        results["total"] += 1
        errors = validate_pin(pin)
        if errors:
            results["valid"] = False
            results["errors"][pin.get("id", "unknown")] = errors

    return results


def check_duplicate(queue: dict, source_url: str, template_key: str | None, content_hash: str | None) -> bool:
    """Verifie si un doublon existe dans la file.

    Returns:
        True si un doublon est detecte.
    """
    for pin in queue.get("pins", []):
        if (
            pin.get("source_url") == source_url
            and pin.get("template_key") == template_key
            and content_hash
            and pin.get("content_hash") == content_hash
        ):
            logger.warning(
                "Doublon detecte : source_url=%s, template_key=%s, hash=%s",
                source_url,
                template_key,
                content_hash,
            )
            return True
    return False
