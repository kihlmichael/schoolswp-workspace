#!/usr/bin/env python3
"""
CLI — Professeur IA WordPress schoolsWP

Usage :
  python -m agents.wp_teacher.cli --topic "Les thèmes WordPress"
  python -m agents.wp_teacher.cli --topic "Créer une page" --goal "un blog personnel"
  python -m agents.wp_teacher.cli --topic "Plugins" --question "Je ne comprends pas la différence entre plugin et thème"
  python -m agents.wp_teacher.cli --topic "..." --output lecons/themes.md
"""

import argparse
import asyncio
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from agents.base import safe_write_path
from agents.wp_teacher.agent import WpTeacherAgent

# Sujets suggérés pour guider l'utilisateur
_SUGGESTED_TOPICS = [
    "Qu'est-ce que WordPress ?",
    "La différence entre WordPress.com et WordPress.org",
    "Les thèmes WordPress",
    "Les plugins WordPress",
    "Créer une page",
    "Créer un article",
    "Les menus de navigation",
    "Les widgets",
    "L'hébergeur et le nom de domaine",
    "Le tableau de bord WordPress",
    "Gutenberg : l'éditeur de blocs",
    "Les catégories et les étiquettes",
    "Les images et la médiathèque",
    "La différence entre page et article",
    "La sécurité WordPress pour débutant",
]


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="wp-teacher",
        description="Professeur IA WordPress schoolsWP — leçons pédagogiques pour débutants",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=(
            "Exemples :\n"
            "  # Leçon basique\n"
            "  python -m agents.wp_teacher.cli \\\n"
            '    --topic "Les thèmes WordPress"\n\n'
            "  # Leçon contextualisée avec objectif\n"
            "  python -m agents.wp_teacher.cli \\\n"
            '    --topic "Créer une page" \\\n'
            '    --goal "créer un site vitrine pour mon activité freelance" \\\n'
            "    --output lecons/creer-une-page.md\n\n"
            "  # Débloquer une confusion spécifique\n"
            "  python -m agents.wp_teacher.cli \\\n"
            '    --topic "Plugins vs Thèmes" \\\n'
            '    --question "Je ne comprends pas pourquoi j\'ai besoin des deux" \\\n'
            "    --level \"j'ai installé WordPress mais je n'ai encore rien fait\"\n\n"
            "  # Afficher les sujets suggérés\n"
            "  python -m agents.wp_teacher.cli --list-topics"
        ),
    )
    parser.add_argument(
        "--topic",
        metavar="SUJET",
        help="Notion à apprendre (ex: 'Les thèmes WordPress', 'Créer une page')",
    )
    parser.add_argument(
        "--question",
        metavar="QUESTION",
        default=None,
        help="Question précise ou point de blocage (ex: 'je ne comprends pas la différence entre...')",
    )
    parser.add_argument(
        "--level",
        metavar="NIVEAU",
        default="débutant",
        help=("Niveau déclaré ou contexte (défaut : 'débutant') (ex: 'j\\'ai installé WordPress mais jamais publié')"),
    )
    parser.add_argument(
        "--goal",
        metavar="OBJECTIF",
        default=None,
        help="Ce que l'apprenant veut créer (ex: 'un blog personnel', 'un site vitrine freelance')",
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
        help="Affiche les sujets suggérés pour débutants",
    )
    return parser


async def main() -> None:
    parser = build_parser()
    args = parser.parse_args()

    if args.list_topics:
        print("\n📚 Sujets suggérés pour débutants WordPress :\n")
        for i, topic in enumerate(_SUGGESTED_TOPICS, 1):
            print(f"  {i:2}. {topic}")
        print('\nUtilise : python -m agents.wp_teacher.cli --topic "<sujet>"\n')
        return

    if not args.topic:
        parser.error("L'argument --topic est requis. Utilise --list-topics pour voir les sujets disponibles.")

    agent = WpTeacherAgent(model=args.model)

    print("\n[wp-teacher] Préparation de la leçon...", flush=True)
    print(f"  Sujet   : {args.topic}", flush=True)
    print(f"  Niveau  : {args.level}", flush=True)
    if args.goal:
        print(f"  Objectif: {args.goal}", flush=True)
    if args.question:
        print(f"  Question: {args.question}", flush=True)
    print("", flush=True)

    lesson = await agent.run(
        topic=args.topic,
        question=args.question,
        level=args.level,
        goal=args.goal,
    )

    if args.output:
        try:
            output_path = safe_write_path(args.output)
        except ValueError as e:
            print(f"[wp-teacher] Erreur : {e}", file=sys.stderr)
            sys.exit(1)
        output_path.parent.mkdir(parents=True, exist_ok=True)
        output_path.write_text(lesson, encoding="utf-8")
        print(f"[wp-teacher] Leçon sauvegardée → {output_path}")
    else:
        print(lesson)


if __name__ == "__main__":
    asyncio.run(main())
