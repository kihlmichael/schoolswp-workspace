#!/usr/bin/env python3
"""
CLI — Knowledge Graph Global schoolsWP

Usage :
  python -m agents.knowledge_graph.cli
  python -m agents.knowledge_graph.cli --context "40 articles, focus LMS et SEO"
  python -m agents.knowledge_graph.cli --ner-files content/articles/cache-wp/ner.json content/articles/lms/ner.json
  python -m agents.knowledge_graph.cli --context "..." --ner-files ner1.json ner2.json --output graph.md
"""

import argparse
import asyncio
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from agents.base import safe_read_path, safe_write_path
from agents.knowledge_graph.agent import KnowledgeGraphAgent


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="knowledge-graph",
        description=(
            "Knowledge Graph Global schoolsWP — cartographie sémantique de l'écosystème + Score Autorité Graph"
        ),
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=(
            "Exemples :\n"
            "  # Graphe global sans données existantes\n"
            "  python -m agents.knowledge_graph.cli\n\n"
            "  # Avec contexte éditorial\n"
            "  python -m agents.knowledge_graph.cli \\\n"
            '    --context "schoolsWP a 40 articles publiés, forte couverture LMS'
            " (Tutor LMS, LearnDash) et SEO (Yoast, Rank Math),"
            ' peu de contenu sur Performance et Automatisation"\n\n'
            "  # Enrichi par des NER d'articles existants\n"
            "  python -m agents.knowledge_graph.cli \\\n"
            "    --ner-files content/articles/cache-wp/ner.json content/articles/lms-comparatif/ner.json \\\n"
            "    --output knowledge-graph.md\n\n"
            "  # Combiné : contexte + NER + sortie fichier\n"
            "  python -m agents.knowledge_graph.cli \\\n"
            '    --context "..." \\\n'
            "    --ner-files ner1.json ner2.json ner3.json \\\n"
            "    --output content/docs/knowledge-graph.md"
        ),
    )
    parser.add_argument(
        "--context",
        default=None,
        metavar="CONTEXTE",
        help=(
            "Description du contexte éditorial actuel de schoolsWP : "
            "articles existants, piliers forts/faibles, objectifs, contraintes "
            "(ex: 'schoolsWP a 40 articles, focus LMS et SEO, peu sur Performance')"
        ),
    )
    parser.add_argument(
        "--ner-files",
        nargs="+",
        default=None,
        metavar="FICHIER_NER",
        help=(
            "Fichiers NER JSON issus d'articles existants (produits par article_pipeline). "
            "Enrichissent la cartographie avec des données réelles. "
            "Accepte plusieurs fichiers : --ner-files ner1.json ner2.json"
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

    # Charger les fichiers NER si fournis
    ner_data: list[str] | None = None
    if args.ner_files:
        ner_data = []
        for ner_path_str in args.ner_files:
            try:
                ner_path = safe_read_path(ner_path_str)
            except ValueError as e:
                print(
                    f"[knowledge-graph] Erreur accès refusé : {e} — ignoré",
                    flush=True,
                )
                continue
            except FileNotFoundError:
                print(
                    f"[knowledge-graph] ⚠ Fichier NER introuvable : {ner_path_str} — ignoré",
                    flush=True,
                )
                continue
            try:
                ner_data.append(ner_path.read_text(encoding="utf-8"))
                print(f"  ✓ NER chargé : {ner_path}", flush=True)
            except OSError as exc:
                print(
                    f"[knowledge-graph] ⚠ Erreur lecture {ner_path} : {exc} — ignoré",
                    flush=True,
                )
        if not ner_data:
            ner_data = None

    agent = KnowledgeGraphAgent(model=args.model)

    print("\n[knowledge-graph] Construction du graphe en cours...", flush=True)
    if args.context:
        print(f"  Contexte  : {args.context}", flush=True)
    if ner_data:
        print(f"  NER       : {len(ner_data)} fichier(s) chargé(s)", flush=True)
    print("", flush=True)

    graph = await agent.run(
        context=args.context,
        ner_data=ner_data,
    )

    # Extraire le score global pour l'afficher en résumé
    score_line = ""
    for line in graph.splitlines():
        if "Score global" in line and "/10" in line:
            import re

            match = re.search(r"(\d+(?:\.\d+)?)/10", line)
            if match:
                score_line = match.group(0)
            break

    if score_line:
        print(f"  ✓ Score Autorité Graph : {score_line}", flush=True)
    print("", flush=True)

    if args.output:
        try:
            output_path = safe_write_path(args.output)
        except ValueError as e:
            print(f"[knowledge-graph] Erreur : {e}", file=sys.stderr)
            sys.exit(1)
        output_path.parent.mkdir(parents=True, exist_ok=True)
        output_path.write_text(graph, encoding="utf-8")
        print(f"[knowledge-graph] Knowledge Graph sauvegardé → {output_path}")
    else:
        print(graph)


if __name__ == "__main__":
    asyncio.run(main())
