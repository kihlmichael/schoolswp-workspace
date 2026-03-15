#!/usr/bin/env python3
"""
CLI — Rédacteur SEO schoolsWP

Usage :
  python -m agents.seo_writer.cli --topic "..." --keyword "..." --intent informationnelle
  python -m agents.seo_writer.cli --topic "..." --keyword "..." --intent comparative --output article.md
"""
import argparse
import asyncio
import sys
from pathlib import Path

# Permet d'exécuter depuis la racine du workspace sans installation
sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from agents.base import safe_write_path
from agents.seo_writer.agent import SeoWriterAgent

_INTENTS = ["informationnelle", "comparative", "décisionnelle"]


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="seo-writer",
        description="Rédacteur SEO schoolsWP — génère un article WordPress optimisé",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=(
            "Exemples :\n"
            "  python -m agents.seo_writer.cli \\\n"
            '    --topic "Choisir un hébergeur WordPress" \\\n'
            '    --keyword "meilleur hébergeur WordPress" \\\n'
            "    --intent comparative\n\n"
            "  python -m agents.seo_writer.cli \\\n"
            '    --topic "Plugin de cache WordPress" \\\n'
            '    --keyword "plugin cache WordPress gratuit" \\\n'
            "    --intent comparative --output content/articles/cache-wp.md"
        ),
    )
    parser.add_argument(
        "--topic",
        required=True,
        metavar="SUJET",
        help="Sujet de l'article (ex: 'Choisir un hébergeur WordPress')",
    )
    parser.add_argument(
        "--keyword",
        required=True,
        metavar="MOT_CLÉ",
        help="Mot-clé principal (ex: 'meilleur hébergeur WordPress')",
    )
    parser.add_argument(
        "--intent",
        required=True,
        choices=_INTENTS,
        metavar="INTENT",
        help=f"Intention de recherche : {' | '.join(_INTENTS)}",
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

    agent = SeoWriterAgent(model=args.model)

    print("\n[seo-writer] Génération en cours...", flush=True)
    print(f"  Sujet   : {args.topic}", flush=True)
    print(f"  Mot-clé : {args.keyword}", flush=True)
    print(f"  Intent  : {args.intent}\n", flush=True)

    article = await agent.run(
        topic=args.topic,
        keyword=args.keyword,
        intent=args.intent,
    )

    if args.output:
        try:
            output_path = safe_write_path(args.output)
        except ValueError as e:
            print(f"[seo-writer] Erreur : {e}", file=sys.stderr)
            sys.exit(1)
        output_path.parent.mkdir(parents=True, exist_ok=True)
        output_path.write_text(article, encoding="utf-8")
        print(f"[seo-writer] Article sauvegardé → {output_path}")
    else:
        print(article)


if __name__ == "__main__":
    asyncio.run(main())
