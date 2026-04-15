"""Machine d'etat du pipeline Pinterest schoolsWP.

Transitions strictes, logging de chaque changement.
Source de verite : systems/pinterest-pipeline/SOP.md
"""

import hashlib
import json
import logging
from datetime import datetime, timezone
from pathlib import Path

logger = logging.getLogger("agents.pinterest.state")

# Transitions autorisees (etat actuel → etats suivants possibles)
TRANSITIONS = {
    "idea": ["brief_generated"],
    "brief_generated": ["brief_approved"],
    "brief_approved": ["design_generated"],
    "design_generated": ["design_approved"],
    "design_approved": ["exported"],
    "exported": ["publish_approved"],
    "publish_approved": ["published"],
    "published": ["analytics_synced"],
    "analytics_synced": ["archived"],
}

PIPELINE_DIR = Path(__file__).resolve().parent.parent
QUEUE_PATH = PIPELINE_DIR / "data" / "pins_queue.json"
LOG_PATH = PIPELINE_DIR / "logs" / "state-transitions.log"


def load_queue() -> dict:
    """Charge la file de production."""
    with open(QUEUE_PATH, encoding="utf-8") as f:
        return json.load(f)


def save_queue(data: dict) -> None:
    """Sauvegarde la file de production."""
    with open(QUEUE_PATH, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)


def find_pin(queue: dict, pin_id: str) -> dict | None:
    """Trouve un pin par ID."""
    for pin in queue.get("pins", []):
        if pin["id"] == pin_id:
            return pin
    return None


def compute_content_hash(pin: dict) -> str:
    """Calcule le SHA-256 du brief (title + description + overlay_text + destination_url)."""
    content = f"{pin.get('title', '')}|{pin.get('description', '')}|{pin.get('overlay_text', '')}|{pin.get('destination_url', '')}"
    h = hashlib.sha256(content.encode("utf-8")).hexdigest()
    return f"sha256:{h}"


def log_transition(pin_id: str, from_status: str, to_status: str) -> None:
    """Logue une transition d'etat."""
    LOG_PATH.parent.mkdir(parents=True, exist_ok=True)
    timestamp = datetime.now(timezone.utc).isoformat()
    line = f"{timestamp} | {pin_id} | {from_status} → {to_status}\n"
    with open(LOG_PATH, "a", encoding="utf-8") as f:
        f.write(line)
    logger.info("Transition: %s %s → %s", pin_id, from_status, to_status)


def transition(pin_id: str, to_status: str, *, dry_run: bool = False) -> dict:
    """Effectue une transition d'etat pour un pin.

    Args:
        pin_id: ID du pin (ex: pin-001)
        to_status: Etat cible
        dry_run: Si True, ne modifie rien, retourne le pin tel qu'il serait

    Returns:
        Le pin mis a jour

    Raises:
        ValueError: Si la transition est invalide ou le pin introuvable
    """
    queue = load_queue()
    pin = find_pin(queue, pin_id)

    if pin is None:
        raise ValueError(f"Pin introuvable : {pin_id}")

    current = pin["status"]
    allowed = TRANSITIONS.get(current, [])

    if to_status not in allowed:
        raise ValueError(
            f"Transition invalide : {current} → {to_status}. Transitions autorisees depuis '{current}' : {allowed}"
        )

    # Verifications specifiques
    if to_status == "published" and not pin.get("publish_approved"):
        raise ValueError(f"Impossible de publier {pin_id} : publish_approved = false")

    if to_status == "published" and pin.get("published_pin_id"):
        raise ValueError(f"Doublon detecte : {pin_id} a deja un published_pin_id = {pin['published_pin_id']}")

    if dry_run:
        logger.info("[DRY-RUN] Transition: %s %s → %s", pin_id, current, to_status)
        return {**pin, "status": to_status}

    # Appliquer la transition
    pin["status"] = to_status
    pin["updated_at"] = datetime.now(timezone.utc).isoformat()
    pin["content_hash"] = compute_content_hash(pin)

    # Mettre a jour les flags d'approbation
    if to_status == "brief_approved":
        pin["brief_approved"] = True
    elif to_status == "design_approved":
        pin["design_approved"] = True
    elif to_status == "publish_approved":
        pin["publish_approved"] = True

    save_queue(queue)
    log_transition(pin_id, current, to_status)

    return pin


def add_pin(pin_data: dict) -> dict:
    """Ajoute un nouveau pin a la file.

    Args:
        pin_data: Donnees du pin (doit contenir au minimum id, source_url, title,
                  description, destination_url, board_key)

    Returns:
        Le pin cree avec les champs par defaut
    """
    queue = load_queue()

    # Verifier doublon
    if find_pin(queue, pin_data["id"]):
        raise ValueError(f"Pin deja existant : {pin_data['id']}")

    now = datetime.now(timezone.utc).isoformat()
    pin = {
        "id": pin_data["id"],
        "source_type": pin_data.get("source_type", "article"),
        "source_id": pin_data.get("source_id"),
        "source_url": pin_data["source_url"],
        "title": pin_data["title"],
        "description": pin_data["description"],
        "alt_text": pin_data.get("alt_text"),
        "overlay_text": pin_data.get("overlay_text"),
        "destination_url": pin_data["destination_url"],
        "board_key": pin_data["board_key"],
        "board_id": pin_data.get("board_id"),
        "template_key": pin_data.get("template_key"),
        "canva_mode": pin_data.get("canva_mode", "assisted"),
        "canva_template_id": pin_data.get("canva_template_id"),
        "canva_design_id": pin_data.get("canva_design_id"),
        "export_format": pin_data.get("export_format", "png"),
        "image_path": pin_data.get("image_path"),
        "status": "idea",
        "brief_approved": False,
        "design_approved": False,
        "publish_approved": False,
        "published_pin_id": None,
        "analytics_last_sync_at": None,
        "content_hash": None,
        "pillar": pin_data.get("pillar"),
        "keyword_primary": pin_data.get("keyword_primary"),
        "keywords_secondary": pin_data.get("keywords_secondary", []),
        "pin_id_editorial": pin_data.get("pin_id_editorial"),
        "angle": pin_data.get("angle"),
        "cta": pin_data.get("cta"),
        "created_at": now,
        "updated_at": now,
    }

    pin["content_hash"] = compute_content_hash(pin)
    queue["pins"].append(pin)
    save_queue(queue)
    log_transition(pin["id"], "(new)", "idea")

    return pin


def dashboard() -> dict:
    """Resume de la file de production."""
    queue = load_queue()
    pins = queue.get("pins", [])

    counts = {}
    for pin in pins:
        status = pin["status"]
        counts[status] = counts.get(status, 0) + 1

    pending_approvals = [p for p in pins if p["status"] in ("brief_generated", "design_generated", "exported")]

    return {
        "total": len(pins),
        "by_status": counts,
        "pending_approvals": [{"id": p["id"], "status": p["status"], "title": p["title"]} for p in pending_approvals],
    }
