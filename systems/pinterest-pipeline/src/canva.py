"""Interactions Canva pour le pipeline Pinterest schoolsWP.

Chemin A : Enterprise Autofill (si disponible)
Chemin B : Assiste via MCP (generate-design + export-design)

Ce module fournit les fonctions utilitaires. L'orchestration reelle
passe par Claude Code + MCP Canva.
"""

import json
import logging
from pathlib import Path

logger = logging.getLogger("agents.pinterest.canva")

PIPELINE_DIR = Path(__file__).resolve().parent.parent
TEMPLATES_PATH = PIPELINE_DIR / "data" / "templates.json"
EXPORTS_DIR = PIPELINE_DIR / "exports"


def load_templates() -> list[dict]:
    """Charge les templates Canva."""
    with open(TEMPLATES_PATH, encoding="utf-8") as f:
        data = json.load(f)
    return data.get("templates", [])


def get_template(template_key: str) -> dict | None:
    """Recupere un template par cle."""
    templates = load_templates()
    for t in templates:
        if t["template_key"] == template_key:
            return t
    return None


def build_design_prompt(pin: dict) -> str:
    """Construit le prompt pour Canva MCP generate-design-structured.

    Le prompt inclut les specs design schoolsWP pour que Canva
    genere un visuel conforme.
    """
    return f"""Cree un pin Pinterest pour schoolsWP.

Format : 1000x1500 pixels (ratio 2:3)
Marge : 50px sur tous les cotes

Texte principal (tiers superieur) :
"{pin.get("overlay_text", pin.get("title", ""))}"

Style :
- Fond sombre (#12111F) ou fond clair (#FAFBFD)
- Accent vert #00D400 pour les barres, soulignements et CTA uniquement
- Typo titre : Montserrat Bold, minimum 30pt
- Typo corps : Open Sans
- Logo schoolsWP en bas a droite (petit, discret)

Sujet : {pin.get("pillar", "WordPress")} — {pin.get("angle", "tutoriel")}
CTA en bas : "{pin.get("cta", "Decouvre le guide complet sur schoolsWP.com")}"

Le visuel doit etre lisible sur mobile. Pas de texte en dessous de 30pt.
"""


def get_export_path(pin_id: str, fmt: str = "png") -> Path:
    """Retourne le chemin d'export pour un pin."""
    EXPORTS_DIR.mkdir(parents=True, exist_ok=True)
    return EXPORTS_DIR / f"{pin_id}.{fmt}"


def export_exists(pin_id: str, fmt: str = "png") -> bool:
    """Verifie si un export existe deja."""
    return get_export_path(pin_id, fmt).exists()
