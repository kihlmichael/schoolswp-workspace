#!/usr/bin/env python3
"""
CLI — Professeur IA WordPress Business schoolsWP

Usage :
  python -m agents.wp_business_teacher.cli --topic "La vitesse de chargement"
  python -m agents.wp_business_teacher.cli --topic "..." --project "site vitrine freelance"
  python -m agents.wp_business_teacher.cli --topic "..." --question "..." --output lecons/vitesse.md
  python -m agents.wp_business_teacher.cli --list-topics
"""
import argparse
import asyncio
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from agents.base import safe_write_path
from agents.wp_business_teacher.agent import WpBusinessTeacherAgent

_SUGGESTED_TOPICS = [
    # Fondamentaux business
    "Pourquoi un site WordPress pro (et pas Wix ou Squarespace) ?",
    "Choisir son hébergeur : impact sur la crédibilité et la performance",
    "Nom de domaine : choisir, sécuriser, bien utiliser",
    # Design & confiance
    "Choisir un thème professionnel (sans usine à gaz)",
    "La page d'accueil parfaite pour un site professionnel",
    "La page À propos qui convertit",
    "La page Contact qui rassure",
    # Conversion
    "Les CTA (Call to Action) : comment inviter à agir sans forcer",
    "Structurer ses offres de services sur WordPress",
    "Créer une landing page simple et efficace",
    # Visibilité
    "SEO de base : être trouvé sur Google sans être expert",
    "Yoast SEO ou Rank Math : lequel choisir et comment l'utiliser",
    "Le blog comme outil de visibilité et de crédibilité",
    # Performance & sécurité
    "La vitesse de chargement : pourquoi ça coûte des clients",
    "SSL / HTTPS : sécurité et confiance en 5 minutes",
    "Les sauvegardes automatiques : protéger son travail",
    "Moins de plugins = plus de performance",
    # Autonomie
    "Maintenance WordPress : ce qu'il faut faire chaque mois",
    "Analyser son trafic avec Google Analytics / MonsterInsights",
    "Préparer son site pour le présenter à un client",
]

_PROJECT_TYPES = [
    "site vitrine freelance",
    "portfolio créatif",
    "site de consultant",
    "landing page offre unique",
    "site prestataire local",
    "blog pro / personal branding",
    "site PME / petite entreprise",
    "site e-commerce simple",
]


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="wp-business-teacher",
        description=(
            "Professeur IA WordPress Business schoolsWP — "
            "leçons orientées crédibilité, conversion et visibilité"
        ),
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=(
            "Exemples :\n"
            "  # Leçon simple\n"
            "  python -m agents.wp_business_teacher.cli \\\n"
            '    --topic "La vitesse de chargement"\n\n'
            "  # Leçon contextualisée avec type de projet\n"
            "  python -m agents.wp_business_teacher.cli \\\n"
            '    --topic "Choisir un thème professionnel" \\\n'
            '    --project "site vitrine freelance graphiste" \\\n'
            "    --output lecons/choisir-theme-pro.md\n\n"
            "  # Débloquer un blocage business spécifique\n"
            "  python -m agents.wp_business_teacher.cli \\\n"
            '    --topic "Page d\'accueil" \\\n'
            '    --question "Je ne sais pas quoi mettre sur ma page d\'accueil pour convaincre" \\\n'
            '    --project "consultant RH indépendant"\n\n'
            "  # Voir tous les sujets business disponibles\n"
            "  python -m agents.wp_business_teacher.cli --list-topics"
        ),
    )
    parser.add_argument(
        "--topic",
        metavar="SUJET",
        help="Notion à apprendre (ex: 'La vitesse de chargement', 'La page À propos')",
    )
    parser.add_argument(
        "--question",
        metavar="QUESTION",
        default=None,
        help="Question ou blocage précis (ex: 'je ne sais pas quoi mettre sur ma page d'accueil')",
    )
    parser.add_argument(
        "--project",
        metavar="PROJET",
        default=None,
        help=(
            "Type de projet business "
            "(ex: 'site vitrine freelance graphiste', 'landing page offre coaching')"
        ),
    )
    parser.add_argument(
        "--level",
        metavar="NIVEAU",
        default="débutant avec esprit business",
        help="Niveau déclaré (défaut : 'débutant avec esprit business')",
    )
    parser.add_argument(
        "--output",
        metavar="FICHIER",
        default=None,
        help="Chemin de sortie (.md). Si absent, affiche dans le terminal.",
    )
    parser.add_argument(
        "--model",
        default=None,
        metavar="MODEL",
        help="Modèle Claude (défaut : $MODEL_WRITER ou claude-sonnet-4-6)",
    )
    parser.add_argument(
        "--list-topics",
        action="store_true",
        default=False,
        help="Affiche tous les sujets business disponibles",
    )
    return parser


async def main() -> None:
    parser = build_parser()
    args = parser.parse_args()

    if args.list_topics:
        print("\n💼 Sujets WordPress Business disponibles :\n")
        categories = {
            "Fondamentaux business": _SUGGESTED_TOPICS[:3],
            "Design & confiance": _SUGGESTED_TOPICS[3:7],
            "Conversion": _SUGGESTED_TOPICS[7:10],
            "Visibilité SEO": _SUGGESTED_TOPICS[10:13],
            "Performance & sécurité": _SUGGESTED_TOPICS[13:17],
            "Autonomie & suivi": _SUGGESTED_TOPICS[17:],
        }
        for category, topics in categories.items():
            print(f"  {category} :")
            for topic in topics:
                print(f"    - {topic}")
            print()
        print("Types de projets :")
        for p in _PROJECT_TYPES:
            print(f"  - {p}")
        print(
            "\nUtilise : python -m agents.wp_business_teacher.cli "
            '--topic "<sujet>" --project "<projet>"\n'
        )
        return

    if not args.topic:
        parser.error(
            "L'argument --topic est requis. "
            "Utilise --list-topics pour voir les sujets disponibles."
        )

    agent = WpBusinessTeacherAgent(model=args.model)

    print("\n[wp-business-teacher] Préparation de la leçon...", flush=True)
    print(f"  Sujet   : {args.topic}", flush=True)
    if args.project:
        print(f"  Projet  : {args.project}", flush=True)
    print(f"  Niveau  : {args.level}", flush=True)
    if args.question:
        print(f"  Question: {args.question}", flush=True)
    print("", flush=True)

    lesson = await agent.run(
        topic=args.topic,
        question=args.question,
        project=args.project,
        level=args.level,
    )

    if args.output:
        try:
            output_path = safe_write_path(args.output)
        except ValueError as e:
            print(f"[wp-business-teacher] Erreur : {e}", file=sys.stderr)
            sys.exit(1)
        output_path.parent.mkdir(parents=True, exist_ok=True)
        output_path.write_text(lesson, encoding="utf-8")
        print(f"[wp-business-teacher] Leçon sauvegardée → {output_path}")
    else:
        print(lesson)


if __name__ == "__main__":
    asyncio.run(main())
