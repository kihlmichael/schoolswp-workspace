#!/usr/bin/env python3
"""
CLI — Formateur WordPress/LMS schoolsWP

Usage :
  python -m agents.lms_trainer.cli --subject "Créer une formation avec Tutor LMS"
  python -m agents.lms_trainer.cli --subject "..." --plugins "Tutor LMS" "FluentCRM" --output tuto.md
  python -m agents.lms_trainer.cli --subject "..." --context "formation payante, 3 modules, upsell prévu"
"""
import argparse
import asyncio
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from agents.base import safe_write_path
from agents.lms_trainer.agent import LmsTrainerAgent


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="lms-trainer",
        description="Formateur WordPress/LMS schoolsWP — tutoriels pas à pas, orientés rentabilité",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=(
            "Exemples :\n"
            "  python -m agents.lms_trainer.cli \\\n"
            '    --subject "Créer une formation avec Tutor LMS et FluentCRM"\n\n'
            "  python -m agents.lms_trainer.cli \\\n"
            '    --subject "Mettre en place un upsell après achat de formation" \\\n'
            '    --plugins "Tutor LMS" "FluentCRM" "Fluent Forms" \\\n'
            '    --context "formation payante 97€, audience freelances WordPress" \\\n'
            "    --output content/articles/tutor-lms-upsell.md\n\n"
            "  python -m agents.lms_trainer.cli \\\n"
            '    --subject "Configurer les certificats automatiques Tutor LMS Pro" \\\n'
            '    --plugins "Tutor LMS Pro"'
        ),
    )
    parser.add_argument(
        "--subject",
        required=True,
        metavar="SUJET",
        help="Ce qu'on veut mettre en place (ex: 'Créer une formation avec certificat')",
    )
    parser.add_argument(
        "--plugins",
        nargs="+",
        metavar="PLUGIN",
        default=None,
        help="Plugins LMS impliqués (ex: 'Tutor LMS' 'FluentCRM')",
    )
    parser.add_argument(
        "--context",
        metavar="CONTEXTE",
        default=None,
        help=(
            "Contexte optionnel : type de formation, audience, objectif business "
            "(ex: 'formation payante 97€, 3 modules, séquence email de 5 jours')"
        ),
    )
    parser.add_argument(
        "--output",
        metavar="FICHIER",
        help="Chemin de sortie (.md). Si absent, affiche dans le terminal.",
    )
    parser.add_argument(
        "--model",
        default=None,
        metavar="MODEL",
        help="Modèle Claude (défaut : $MODEL_WRITER ou claude-sonnet-4-6)",
    )
    return parser


async def main() -> None:
    parser = build_parser()
    args = parser.parse_args()

    agent = LmsTrainerAgent(model=args.model)

    print("\n[lms-trainer] Génération en cours...", flush=True)
    print(f"  Sujet   : {args.subject}", flush=True)
    if args.plugins:
        print(f"  Plugins : {', '.join(args.plugins)}", flush=True)
    if args.context:
        print(f"  Contexte: {args.context}", flush=True)
    print("", flush=True)

    article = await agent.run(
        subject=args.subject,
        plugins=args.plugins,
        context=args.context,
    )

    if args.output:
        try:
            output_path = safe_write_path(args.output)
        except ValueError as e:
            print(f"[lms-trainer] Erreur : {e}", file=sys.stderr)
            sys.exit(1)
        output_path.parent.mkdir(parents=True, exist_ok=True)
        output_path.write_text(article, encoding="utf-8")
        print(f"[lms-trainer] Tutoriel sauvegardé → {output_path}")
    else:
        print(article)


if __name__ == "__main__":
    asyncio.run(main())
