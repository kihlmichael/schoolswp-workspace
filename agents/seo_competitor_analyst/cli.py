#!/usr/bin/env python3
"""
CLI — Consultant SEO Analyse Concurrentielle schoolsWP

Usage :
  # Via fichiers CSV
  python -m agents.seo_competitor_analyst.cli \
    --my-file data/schoolswp-keywords.csv \
    --competitor-file data/wpmarmite-keywords.csv

  # Via données inline (test rapide)
  python -m agents.seo_competitor_analyst.cli \
    --my-data "mot-clé,position,url\nautomatisation wordpress,7,/auto\n..." \
    --competitor-data "mot-clé,position\nautomatisation wordpress,2\n..."

  # Avec focus thématique et sortie fichier
  python -m agents.seo_competitor_analyst.cli \
    --my-file schoolswp.csv --competitor-file wpmarmite.csv \
    --focus "LMS et formations" \
    --output reports/seo-gap-analysis.md

Formats acceptés pour les fichiers :
  CSV : colonnes attendues (dans n'importe quel ordre) :
        mot-clé / keyword, position / pos, url, trafic / traffic (optionnel)
  JSON : [{"keyword": "...", "position": 7, "url": "...", "traffic": 120}, ...]
  TSV  : même structure que CSV mais séparateur tabulation
  TXT  : texte structuré libre (l'agent s'adapte)
"""
import argparse
import asyncio
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from agents.seo_competitor_analyst.agent import SeoCompetitorAnalystAgent


def _read_data(file_path: str | None, inline_data: str | None, label: str) -> str:
    """Lit les données depuis un fichier ou retourne les données inline."""
    if file_path:
        path = Path(file_path)
        if not path.exists():
            print(f"[seo-analyst] ERREUR : fichier '{file_path}' introuvable.", file=sys.stderr)
            sys.exit(1)
        content = path.read_text(encoding="utf-8")
        print(f"  {label}: {path.name} ({len(content.splitlines())} lignes)", flush=True)
        return content
    if inline_data:
        print(f"  {label}: données inline ({len(inline_data.splitlines())} lignes)", flush=True)
        return inline_data
    return ""


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="seo-competitor-analyst",
        description=(
            "Consultant SEO Analyse Concurrentielle schoolsWP — "
            "gaps, quick wins, clusters, plan d'action expert"
        ),
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=(
            "Exemples :\n"
            "  # Analyse complète via fichiers CSV\n"
            "  python -m agents.seo_competitor_analyst.cli \\\n"
            "    --my-file data/schoolswp-keywords.csv \\\n"
            "    --competitor-file data/wpmarmite-keywords.csv \\\n"
            "    --output reports/seo-gap-analysis.md\n\n"
            "  # Avec focus thématique\n"
            "  python -m agents.seo_competitor_analyst.cli \\\n"
            "    --my-file data/schoolswp.csv \\\n"
            "    --competitor-file data/wpmarmite.csv \\\n"
            '    --focus "automatisation WordPress et IA" \\\n'
            "    --output reports/gap-automation.md\n\n"
            "  # Test rapide avec données inline\n"
            "  python -m agents.seo_competitor_analyst.cli \\\n"
            "    --my-data $'mot-clé,position\\nautomatisation wordpress,7\\nplugin cache,12' \\\n"
            "    --competitor-data $'mot-clé,position\\nautomatisation wordpress,2\\nplugin cache,1'\n\n"
            "  # Concurrent différent (ex: WPChef)\n"
            "  python -m agents.seo_competitor_analyst.cli \\\n"
            "    --my-file schoolswp.csv --competitor-file wpchef.csv \\\n"
            "    --competitor-name WPChef"
        ),
    )

    # Source données schoolsWP
    my_group = parser.add_mutually_exclusive_group(required=True)
    my_group.add_argument(
        "--my-file",
        metavar="FICHIER",
        help="Fichier de mots-clés schoolsWP (CSV, JSON, TSV, TXT)",
    )
    my_group.add_argument(
        "--my-data",
        metavar="DATA",
        help="Données inline mots-clés schoolsWP (CSV, JSON ou texte libre)",
    )

    # Source données concurrent
    comp_group = parser.add_mutually_exclusive_group(required=True)
    comp_group.add_argument(
        "--competitor-file",
        metavar="FICHIER",
        help="Fichier de mots-clés du concurrent (CSV, JSON, TSV, TXT)",
    )
    comp_group.add_argument(
        "--competitor-data",
        metavar="DATA",
        help="Données inline mots-clés du concurrent",
    )

    parser.add_argument(
        "--competitor-name",
        metavar="NOM",
        default="WPMarmite",
        help="Nom du concurrent (défaut : WPMarmite)",
    )
    parser.add_argument(
        "--focus",
        metavar="FOCUS",
        default=None,
        help=(
            "Thématique prioritaire pour l'analyse "
            "(ex: 'LMS et formations', 'IA WordPress', 'automatisation')"
        ),
    )
    parser.add_argument(
        "--output",
        metavar="FICHIER",
        default=None,
        help="Fichier de sortie (.md). Si absent, affiche dans le terminal.",
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

    print(f"\n[seo-competitor-analyst] Analyse en cours...", flush=True)
    print(f"  Concurrent   : {args.competitor_name}", flush=True)
    if args.focus:
        print(f"  Focus        : {args.focus}", flush=True)

    my_keywords = _read_data(args.my_file, args.my_data, "schoolsWP")
    competitor_keywords = _read_data(args.competitor_file, args.competitor_data, args.competitor_name)
    print("", flush=True)

    agent = SeoCompetitorAnalystAgent(model=args.model)

    analysis = await agent.run(
        my_keywords=my_keywords,
        competitor_keywords=competitor_keywords,
        competitor_name=args.competitor_name,
        focus=args.focus,
    )

    if args.output:
        output_path = Path(args.output)
        output_path.parent.mkdir(parents=True, exist_ok=True)
        output_path.write_text(analysis, encoding="utf-8")
        print(f"[seo-competitor-analyst] Analyse sauvegardée → {output_path}")
    else:
        print(analysis)


if __name__ == "__main__":
    asyncio.run(main())
