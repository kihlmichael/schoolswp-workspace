#!/usr/bin/env python3
"""
CLI — Cluster & Cocon Automatique schoolsWP

Usage :
  python -m agents.cluster_architect.cli --thematique "CRM WordPress" --objectif "vente formation"
  python -m agents.cluster_architect.cli --thematique "Plugin cache" --objectif "affiliation" --competition élevé
  python -m agents.cluster_architect.cli --thematique "LMS WordPress" --objectif "leads" --keyword "lms wordpress gratuit" --output clusters/lms.md
"""

import argparse
import asyncio
import sys
from pathlib import Path

# Permet d'exécuter depuis la racine du workspace sans installation
sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from agents.base import safe_write_path
from agents.cluster_architect.agent import ClusterArchitectAgent

_COMPETITION_LEVELS = ["faible", "moyen", "élevé"]


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="cluster-architect",
        description="Cluster & Cocon Automatique schoolsWP — architecture sémantique complète",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=(
            "Exemples :\n"
            "  python -m agents.cluster_architect.cli \\\n"
            '    --thematique "CRM WordPress" \\\n'
            '    --objectif "vente formation FluentCRM" \\\n'
            "    --competition moyen\n\n"
            "  python -m agents.cluster_architect.cli \\\n"
            '    --thematique "Plugin de cache WordPress" \\\n'
            '    --objectif "affiliation hébergeurs" \\\n'
            "    --competition élevé \\\n"
            '    --keyword "meilleur plugin cache wordpress" \\\n'
            "    --output clusters/cache-wp.md\n\n"
            "  python -m agents.cluster_architect.cli \\\n"
            '    --thematique "Automatisation WordPress" \\\n'
            '    --objectif "autorité thématique + leads" \\\n'
            "    --competition faible \\\n"
            '    --context "schoolsWP a déjà 3 articles sur n8n" \\\n'
            "    --output clusters/automatisation.md"
        ),
    )
    parser.add_argument(
        "--thematique",
        required=True,
        metavar="SUJET",
        help="Sujet principal du cluster (ex: 'CRM WordPress', 'LMS WordPress')",
    )
    parser.add_argument(
        "--objectif",
        required=True,
        metavar="OBJECTIF",
        help=("Objectif business visé (ex: 'vente formation LMS', 'affiliation hébergeurs', 'leads freelances')"),
    )
    parser.add_argument(
        "--competition",
        default="moyen",
        choices=_COMPETITION_LEVELS,
        metavar="NIVEAU",
        help=f"Niveau de compétition estimé : {' | '.join(_COMPETITION_LEVELS)} (défaut: moyen)",
    )
    parser.add_argument(
        "--keyword",
        default=None,
        metavar="MOT_CLÉ",
        help="Mot-clé principal si déjà identifié (ex: 'crm wordpress gratuit')",
    )
    parser.add_argument(
        "--context",
        default=None,
        metavar="CONTEXTE",
        help=(
            "Contexte additionnel : cible, contraintes, contenu existant "
            "(ex: 'schoolsWP a déjà 2 articles sur FluentCRM')"
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

    agent = ClusterArchitectAgent(model=args.model)

    print("\n[cluster-architect] Génération en cours...", flush=True)
    print(f"  Thématique  : {args.thematique}", flush=True)
    print(f"  Objectif    : {args.objectif}", flush=True)
    print(f"  Compétition : {args.competition}", flush=True)
    if args.keyword:
        print(f"  Mot-clé     : {args.keyword}", flush=True)
    if args.context:
        print(f"  Contexte    : {args.context}", flush=True)
    print("", flush=True)

    cluster = await agent.run(
        thematique=args.thematique,
        objectif=args.objectif,
        competition=args.competition,
        keyword=args.keyword,
        context=args.context,
    )

    if args.output:
        try:
            output_path = safe_write_path(args.output)
        except ValueError as e:
            print(f"[cluster-architect] Erreur : {e}", file=sys.stderr)
            sys.exit(1)
        output_path.parent.mkdir(parents=True, exist_ok=True)
        output_path.write_text(cluster, encoding="utf-8")
        print(f"[cluster-architect] Cluster sauvegardé → {output_path}")
    else:
        print(cluster)


if __name__ == "__main__":
    asyncio.run(main())
