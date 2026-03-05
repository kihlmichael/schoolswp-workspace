#!/usr/bin/env python3
"""
CLI — Niche Scout schoolsWP
Détection de niches atteignables vs WPMarmite

Usage :
  python -m agents.niche_scout.cli --thematique "LMS WordPress"
  python -m agents.niche_scout.cli --thematique "CRM WordPress" --focus "automatisation"
  python -m agents.niche_scout.cli --thematique "Plugin cache" --context "déjà 2 articles WP Rocket" --output niches/cache.md
"""
import argparse
import asyncio
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from agents.niche_scout.agent import NicheScoutAgent


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="niche-scout",
        description="Niche Scout schoolsWP — détection de niches atteignables vs WPMarmite",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=(
            "Exemples :\n"
            "  python -m agents.niche_scout.cli \\\n"
            '    --thematique "LMS WordPress"\n\n'
            "  python -m agents.niche_scout.cli \\\n"
            '    --thematique "CRM WordPress" \\\n'
            '    --focus "automatisation"\n\n'
            "  python -m agents.niche_scout.cli \\\n"
            '    --thematique "Plugin de sécurité WordPress" \\\n'
            '    --context "schoolsWP a déjà un article sur Wordfence" \\\n'
            '    --focus "e-commerce" \\\n'
            "    --output niches/securite.md"
        ),
    )
    parser.add_argument(
        "--thematique",
        required=True,
        metavar="SUJET",
        help="Thématique principale à analyser (ex: 'LMS WordPress', 'CRM WordPress')",
    )
    parser.add_argument(
        "--context",
        default=None,
        metavar="CONTEXTE",
        help=(
            "Contexte additionnel : contenu existant, contraintes budgétaires, cible "
            "(ex: 'schoolsWP a déjà 3 articles sur Tutor LMS')"
        ),
    )
    parser.add_argument(
        "--focus",
        default=None,
        metavar="ANGLE",
        help=(
            "Angle prioritaire à approfondir "
            "(ex: 'automatisation', 'freelances', 'e-commerce')"
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

    agent = NicheScoutAgent(model=args.model)

    print("\n[niche-scout] Analyse en cours...", flush=True)
    print(f"  Thématique : {args.thematique}", flush=True)
    if args.focus:
        print(f"  Focus      : {args.focus}", flush=True)
    if args.context:
        print(f"  Contexte   : {args.context}", flush=True)
    print("", flush=True)

    result = await agent.run(
        thematique=args.thematique,
        context=args.context,
        focus=args.focus,
    )

    if args.output:
        output_path = Path(args.output)
        output_path.parent.mkdir(parents=True, exist_ok=True)
        output_path.write_text(result, encoding="utf-8")
        print(f"[niche-scout] Analyse sauvegardée → {output_path}")
    else:
        print(result)


if __name__ == "__main__":
    asyncio.run(main())
