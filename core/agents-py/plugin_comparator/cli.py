#!/usr/bin/env python3
"""
CLI — Comparateur de plugins WordPress schoolsWP

Usage :
  python -m agents.plugin_comparator.cli --plugins "WP Rocket" "W3 Total Cache"
  python -m agents.plugin_comparator.cli --plugins "Elementor" "Divi" "Bricks" --output comparatif.md
  python -m agents.plugin_comparator.cli --plugins "Yoast" "Rank Math" --context "blog freelance, trafic < 5k/mois"
"""

import argparse
import asyncio
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from agents.base import safe_write_path
from agents.plugin_comparator.agent import PluginComparatorAgent


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="plugin-comparator",
        description="Comparateur de plugins WordPress schoolsWP — analyse objective, verdict par profil",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=(
            "Exemples :\n"
            "  python -m agents.plugin_comparator.cli \\\n"
            '    --plugins "WP Rocket" "W3 Total Cache"\n\n'
            "  python -m agents.plugin_comparator.cli \\\n"
            '    --plugins "Elementor" "Divi" "Bricks" \\\n'
            '    --context "site portfolio freelance, budget limité" \\\n'
            "    --output content/articles/comparatif-page-builders.md\n\n"
            "  python -m agents.plugin_comparator.cli \\\n"
            '    --plugins "Yoast SEO" "Rank Math" "SEOPress" \\\n'
            "    --intent comparative"
        ),
    )
    parser.add_argument(
        "--plugins",
        required=True,
        nargs="+",
        metavar="PLUGIN",
        help="2 à 4 noms de plugins à comparer (entre guillemets si espace)",
    )
    parser.add_argument(
        "--context",
        metavar="CONTEXTE",
        default=None,
        help=(
            "Contexte optionnel : type de site, contraintes budget, niveau technique "
            "(ex: 'blog WordPress, trafic 10k/mois, hébergeur mutualisé')"
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

    plugins: list[str] = args.plugins

    if len(plugins) < 2:
        parser.error("Il faut au minimum 2 plugins pour une comparaison.")
    if len(plugins) > 4:
        parser.error("Maximum 4 plugins par comparaison.")

    agent = PluginComparatorAgent(model=args.model)

    plugins_display = " vs ".join(plugins)
    print("\n[plugin-comparator] Comparaison en cours...", flush=True)
    print(f"  Plugins : {plugins_display}", flush=True)
    if args.context:
        print(f"  Contexte : {args.context}", flush=True)
    print("", flush=True)

    article = await agent.run(plugins=plugins, context=args.context)

    if args.output:
        try:
            output_path = safe_write_path(args.output)
        except ValueError as e:
            print(f"[plugin-comparator] Erreur : {e}", file=sys.stderr)
            sys.exit(1)
        output_path.parent.mkdir(parents=True, exist_ok=True)
        output_path.write_text(article, encoding="utf-8")
        print(f"[plugin-comparator] Comparatif sauvegardé → {output_path}")
    else:
        print(article)


if __name__ == "__main__":
    asyncio.run(main())
