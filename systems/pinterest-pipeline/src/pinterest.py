"""Client Pinterest API v5 pour le pipeline schoolsWP.

Gere : upload media, creation de pin, analytics.
Necessite PINTEREST_ACCESS_TOKEN dans .env.
"""

import argparse
import json
import logging
import os
import sys
from datetime import datetime, timezone
from pathlib import Path

logger = logging.getLogger("agents.pinterest.api")

PIPELINE_DIR = Path(__file__).resolve().parent.parent
BOARDS_PATH = PIPELINE_DIR / "data" / "boards.json"
PUBLISH_LOG = PIPELINE_DIR / "logs" / "publish.log"

# Pinterest API base
API_BASE = "https://api.pinterest.com/v5"


def get_access_token() -> str:
    """Recupere le token Pinterest depuis l'environnement."""
    token = os.getenv("PINTEREST_ACCESS_TOKEN")
    if not token:
        raise RuntimeError("PINTEREST_ACCESS_TOKEN non defini. Ajouter dans .env.")
    return token


def load_boards() -> dict[str, str]:
    """Charge le mapping board_key → board_id."""
    with open(BOARDS_PATH, encoding="utf-8") as f:
        data = json.load(f)
    return {b["board_key"]: b["board_id"] for b in data.get("boards", []) if b.get("board_id")}


def resolve_board_id(board_key: str) -> str:
    """Resout un board_key en board_id Pinterest."""
    boards = load_boards()
    board_id = boards.get(board_key)
    if not board_id:
        raise ValueError(f"board_id non trouve pour '{board_key}'. Remplir data/boards.json avec les IDs Pinterest.")
    return board_id


def build_pin_payload(pin: dict) -> dict:
    """Construit le payload pour POST /pins.

    Args:
        pin: Donnees du pin depuis pins_queue.json

    Returns:
        Payload conforme a l'API Pinterest v5
    """
    board_id = pin.get("board_id") or resolve_board_id(pin["board_key"])

    payload = {
        "board_id": board_id,
        "title": pin["title"],
        "description": pin["description"],
        "alt_text": pin.get("alt_text", ""),
        "link": pin["destination_url"],
    }

    # media_source depend du mode d'upload (image_id ou url)
    if pin.get("image_path"):
        # L'upload media doit etre fait avant — ici on reference le media_id
        # qui serait stocke apres register_media_upload + upload
        payload["media_source"] = {
            "source_type": "image_id",
            "media_id": pin.get("media_id", "TO_BE_SET_AFTER_UPLOAD"),
        }

    return payload


def log_publish(pin_id: str, pinterest_pin_id: str, board_key: str) -> None:
    """Logue une publication dans publish.log."""
    PUBLISH_LOG.parent.mkdir(parents=True, exist_ok=True)
    timestamp = datetime.now(timezone.utc).isoformat()
    line = f"{timestamp} | PUBLISHED | {pin_id} | pinterest_id={pinterest_pin_id} | board={board_key}\n"
    with open(PUBLISH_LOG, "a", encoding="utf-8") as f:
        f.write(line)
    logger.info("Published: %s → %s", pin_id, pinterest_pin_id)


def main():
    """CLI pour les operations Pinterest."""
    parser = argparse.ArgumentParser(description="Pinterest API CLI — schoolsWP")
    parser.add_argument("--pin-id", required=True, help="ID du pin (ex: pin-001)")
    parser.add_argument("--publish", action="store_true", help="Publier le pin")
    parser.add_argument("--dry-run", action="store_true", help="Simule sans publier")
    args = parser.parse_args()

    # Charger le pin depuis la queue
    from state import find_pin, load_queue

    queue = load_queue()
    pin = find_pin(queue, args.pin_id)

    if not pin:
        print(f"[ERREUR] Pin introuvable : {args.pin_id}")
        sys.exit(1)

    if args.publish:
        if not pin.get("publish_approved"):
            print(f"[ERREUR] {args.pin_id} n'est pas approuve (publish_approved = false)")
            sys.exit(1)

        if pin.get("published_pin_id"):
            print(f"[ERREUR] Doublon : {args.pin_id} deja publie (id: {pin['published_pin_id']})")
            sys.exit(1)

        payload = build_pin_payload(pin)

        if args.dry_run:
            print("[DRY-RUN] Payload Pinterest :")
            print(json.dumps(payload, indent=2, ensure_ascii=False))
            print(f"\n[DRY-RUN] Board : {pin['board_key']}")
            print("[DRY-RUN] Aucune publication effectuee.")
            return

        # En mode reel, l'appel API serait fait ici via requests/httpx
        print("[INFO] Payload genere :")
        print(json.dumps(payload, indent=2, ensure_ascii=False))
        print(
            "\n[INFO] Appel API Pinterest non implemente dans ce script standalone."
            "\nUtilise Claude Code pour orchestrer la publication."
        )


if __name__ == "__main__":
    main()
