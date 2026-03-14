#!/usr/bin/env python3
"""
CLI — Niche Scorer schoolsWP
Scoring automatique basé sur overlap SEO (formule schoolsWP /10)

Usage :
  python -m agents.niche_scout.scorer_cli --niches "Tutor LMS + CRM" "CRM WordPress avancé"
  python -m agents.niche_scout.scorer_cli --niches-file niches.txt --topics "LMS, FluentCRM, n8n"
  python -m agents.niche_scout.scorer_cli --niches "LMS freelance" "LMS débutant" --output scores/lms.md
"""
import argparse
import asyncio
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from agents.niche_scout.scorer import NicheScorerAgent


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="niche-scorer",
        description=(
            "Niche Scorer schoolsWP — scoring SEO /10 basé sur la formule overlap\n"
            "Formula: (Volume_norm + Low_Competition + Overlap + Authority + Longtail) / 5 × 10"
        ),
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=(
            "Exemples :\n"
            "  # Scorer 3 niches directement\n"
            "  python -m agents.niche_scout.scorer_cli \\\n"
            '    --niches "Tutor LMS + FluentCRM" "CRM WordPress avancé" "LMS pour débutants"\n\n'
            "  # Avec thèmes existants schoolsWP pour overlap précis\n"
            "  python -m agents.niche_scout.scorer_cli \\\n"
            '    --niches "Automatisation n8n WordPress" "LMS freelance rentable" \\\n'
            '    --topics "n8n, FluentCRM, Tutor LMS, SEO sémantique, IA WordPress"\n\n'
            "  # Depuis un fichier (1 niche par ligne)\n"
            "  python -m agents.niche_scout.scorer_cli \\\n"
            "    --niches-file niches/lms-candidates.txt \\\n"
            '    --context "DA schoolsWP estimé 25, focus freelances" \\\n'
            "    --output scores/lms-scored.md"
        ),
    )

    input_group = parser.add_mutually_exclusive_group(required=True)
    input_group.add_argument(
        "--niches",
        nargs="+",
        metavar="NICHE",
        help=(
            "Liste des niches à scorer (une ou plusieurs, séparées par des espaces). "
            "Mettre entre guillemets si la niche contient des espaces."
        ),
    )
    input_group.add_argument(
        "--niches-file",
        metavar="FICHIER",
        help="Fichier texte avec une niche par ligne (encoding UTF-8).",
    )

    parser.add_argument(
        "--topics",
        default=None,
        metavar="THÈMES",
        help=(
            "Thèmes existants de schoolsWP pour calculer l'overlap sémantique. "
            "Format : liste séparée par des virgules. "
            "(ex: 'FluentCRM, Tutor LMS, n8n, SEO WordPress, IA')"
        ),
    )
    parser.add_argument(
        "--context",
        default=None,
        metavar="CONTEXTE",
        help=(
            "Contexte additionnel : DA estimé, contraintes, focus spécifique "
            "(ex: 'DA schoolsWP estimé à 25, focus e-commerce')"
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

    # Lecture des niches depuis le fichier ou les args
    if args.niches_file:
        niches_path = Path(args.niches_file)
        if not niches_path.exists():
            print(f"[niche-scorer] Erreur : fichier introuvable → {niches_path}", file=sys.stderr)
            sys.exit(1)
        niches = [
            line.strip()
            for line in niches_path.read_text(encoding="utf-8").splitlines()
            if line.strip() and not line.startswith("#")
        ]
    else:
        niches = args.niches

    if not niches:
        print("[niche-scorer] Erreur : aucune niche à scorer.", file=sys.stderr)
        sys.exit(1)

    agent = NicheScorerAgent(model=args.model)

    print("\n[niche-scorer] Scoring en cours...", flush=True)
    print(f"  Niches ({len(niches)}) :", flush=True)
    for n in niches:
        print(f"    • {n}", flush=True)
    if args.topics:
        print(f"  Thèmes schoolsWP : {args.topics}", flush=True)
    if args.context:
        print(f"  Contexte         : {args.context}", flush=True)
    print("", flush=True)

    result = await agent.run(
        niches=niches,
        schoolswp_topics=args.topics,
        context=args.context,
    )

    if args.output:
        output_path = Path(args.output)
        output_path.parent.mkdir(parents=True, exist_ok=True)
        output_path.write_text(result, encoding="utf-8")
        print(f"[niche-scorer] Scores sauvegardés → {output_path}")
    else:
        print(result)


if __name__ == "__main__":
    asyncio.run(main())
