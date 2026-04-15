"""Sync analytics Pinterest pour le pipeline schoolsWP.

Recupere les metriques par pin et genere des snapshots quotidiens.
"""

import json
import logging
from datetime import datetime, timezone
from pathlib import Path

logger = logging.getLogger("agents.pinterest.analytics")

PIPELINE_DIR = Path(__file__).resolve().parent.parent
ANALYTICS_DIR = PIPELINE_DIR / "analytics"


def get_snapshot_path(date: str | None = None) -> Path:
    """Retourne le chemin du snapshot pour une date donnee."""
    ANALYTICS_DIR.mkdir(parents=True, exist_ok=True)
    if date is None:
        date = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    return ANALYTICS_DIR / f"{date}.json"


def save_snapshot(data: dict, date: str | None = None) -> Path:
    """Sauvegarde un snapshot analytics."""
    path = get_snapshot_path(date)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    logger.info("Snapshot analytics sauvegarde : %s", path)
    return path


def build_empty_snapshot() -> dict:
    """Structure d'un snapshot analytics vide."""
    return {
        "date": datetime.now(timezone.utc).strftime("%Y-%m-%d"),
        "account": {
            "impressions": 0,
            "engagements": 0,
            "saves": 0,
            "pin_clicks": 0,
            "outbound_clicks": 0,
            "followers": 0,
        },
        "pins": [],
        "top_pins": [],
    }


def build_pin_analytics_entry(pin_id: str, pinterest_pin_id: str, metrics: dict) -> dict:
    """Structure d'une entree analytics par pin."""
    return {
        "pin_id": pin_id,
        "pinterest_pin_id": pinterest_pin_id,
        "impressions": metrics.get("impressions", 0),
        "saves": metrics.get("saves", 0),
        "pin_clicks": metrics.get("pin_clicks", 0),
        "outbound_clicks": metrics.get("outbound_clicks", 0),
        "engagement_rate": 0.0,
    }


def main():
    """CLI pour sync analytics."""
    import argparse

    parser = argparse.ArgumentParser(description="Pinterest Analytics — schoolsWP")
    parser.add_argument("--sync", action="store_true", help="Synchroniser les analytics")
    parser.add_argument("--dry-run", action="store_true", help="Simule sans appel API")
    args = parser.parse_args()

    if args.sync:
        if args.dry_run:
            snapshot = build_empty_snapshot()
            print("[DRY-RUN] Snapshot vide genere :")
            print(json.dumps(snapshot, indent=2, ensure_ascii=False))
            return

        print(
            "[INFO] Sync analytics non implemente dans ce script standalone."
            "\nUtilise Claude Code pour orchestrer la sync via Pinterest API."
        )


if __name__ == "__main__":
    main()
