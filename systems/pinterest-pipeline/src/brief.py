"""Generation de briefs Pinterest via Claude pour schoolsWP.

Genere des briefs structures (title, description, alt_text, overlay_text, keywords)
a partir d'un article source.
"""

import argparse
import json
import logging
from datetime import datetime, timezone
from pathlib import Path

logger = logging.getLogger("agents.pinterest.brief")

PIPELINE_DIR = Path(__file__).resolve().parent.parent
BRIEFS_DIR = PIPELINE_DIR / "briefs"

# Prompt systeme pour la generation de briefs
SYSTEM_PROMPT = """Tu es l'assistant Pinterest de schoolsWP. Tu generes des briefs de pins Pinterest
structures et optimises SEO.

Regles strictes :
- Tutoiement systematique
- Titre : 40-100 caracteres, mot-cle principal en debut
- Description : 150-300 caracteres, mot-cle en premiere phrase, CTA en fin
- Alt text : description factuelle de l'image pour accessibilite
- Overlay text : 3-7 mots impactants, chiffres si possible
- Mots interdits : disruptif, game changer, scalable, hack, revolutionnaire, incroyable, en un clic, sans effort
- CTA : "Decouvre le guide complet sur schoolsWP.com" ou equivalent utile
- Angle : tutoriel / comparatif / listicle / erreurs a eviter / behind the scenes

Output : JSON strict, pas de texte autour.
"""

BRIEF_TEMPLATE = {
    "title": "",
    "description": "",
    "alt_text": "",
    "overlay_text": "",
    "keyword_primary": "",
    "keywords_secondary": [],
    "board_key": "",
    "template_key": "",
    "pillar": "",
    "angle": "",
    "cta": "",
}


def build_user_prompt(source_url: str, board_key: str, article_content: str | None = None) -> str:
    """Construit le prompt utilisateur pour generer un brief."""
    prompt = f"""Genere un brief Pinterest pour cet article schoolsWP.

URL source : {source_url}
Board cible : {board_key}
"""
    if article_content:
        # Tronquer a 2000 caracteres pour rester raisonnable
        truncated = article_content[:2000]
        prompt += f"\nContenu de l'article (extrait) :\n{truncated}\n"

    prompt += """
Retourne un JSON avec exactement ces champs :
{
  "title": "Titre SEO 40-100 car.",
  "description": "Description 150-300 car., mot-cle en 1ere phrase, CTA en fin",
  "alt_text": "Description factuelle de l'image",
  "overlay_text": "3-7 mots impactants",
  "keyword_primary": "mot-cle principal",
  "keywords_secondary": ["mot-cle 2", "mot-cle 3"],
  "board_key": "board-key",
  "template_key": "pin-tutoriel|pin-comparatif|pin-listicle",
  "pillar": "SEO|LMS|CRM|WordPress|Automatisation|Plugins|Ecommerce|Freelance|Formation|Coulisses",
  "angle": "tutoriel|comparatif|listicle|erreurs|behind-the-scenes",
  "cta": "CTA schoolsWP"
}

JSON uniquement, pas de texte autour.
"""
    return prompt


def save_brief(pin_id: str, brief_data: dict) -> Path:
    """Sauvegarde un brief dans le dossier briefs/."""
    BRIEFS_DIR.mkdir(parents=True, exist_ok=True)
    date_str = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    filename = f"{date_str}-{pin_id}.json"
    path = BRIEFS_DIR / filename

    with open(path, "w", encoding="utf-8") as f:
        json.dump(brief_data, f, indent=2, ensure_ascii=False)

    logger.info("Brief sauvegarde : %s", path)
    return path


def main():
    """CLI pour generer un brief (sans appel LLM — structure seulement)."""
    parser = argparse.ArgumentParser(description="Generer un brief Pinterest schoolsWP")
    parser.add_argument("--source-url", required=True, help="URL de l'article source")
    parser.add_argument("--board-key", required=True, help="Board cible (ex: seo-wordpress)")
    parser.add_argument("--pin-id", required=True, help="ID du pin (ex: pin-001)")
    parser.add_argument("--dry-run", action="store_true", help="Affiche le prompt sans appeler le LLM")
    args = parser.parse_args()

    prompt = build_user_prompt(args.source_url, args.board_key)

    if args.dry_run:
        print("=== SYSTEM PROMPT ===")
        print(SYSTEM_PROMPT)
        print("\n=== USER PROMPT ===")
        print(prompt)
        print("\n[DRY-RUN] Aucun appel LLM effectue.")
        return

    # En mode reel, l'appel LLM serait fait via BaseContentAgent
    # Pour l'instant, on affiche le prompt et on attend l'integration
    print("=== SYSTEM PROMPT ===")
    print(SYSTEM_PROMPT)
    print("\n=== USER PROMPT ===")
    print(prompt)
    print(
        "\n[INFO] Appel LLM non implemente dans ce script standalone."
        "\nUtilise Claude Code avec le skill /pinterest-pipeline pour generer le brief."
    )


if __name__ == "__main__":
    main()
