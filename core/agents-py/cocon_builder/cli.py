#!/usr/bin/env python3
"""
CLI — Générateur de Cocon Sémantique schoolsWP

Usage :
  python -m agents.cocon_builder.cli --pillar lms
  python -m agents.cocon_builder.cli --pillar lms --context "12 articles, focus Tutor LMS"
  python -m agents.cocon_builder.cli --pillar seo --graph-file content/docs/knowledge-graph.md
  python -m agents.cocon_builder.cli --pillar lms \\
      --authority-file audit/piliers/lms.md \\
      --graph-file content/docs/knowledge-graph.md \\
      --output cocons/lms.md
"""
import argparse
import asyncio
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from agents.base import safe_read_path, safe_write_path
from agents.cocon_builder.agent import PILLARS, CoconBuilderAgent


def _count_satellites(text: str) -> int:
    """Compte le nombre de lignes dans le tableau satellites (heuristique)."""
    in_table = False
    count = 0
    for line in text.splitlines():
        if "Articles Satellites" in line:
            in_table = True
            continue
        if in_table:
            # Ligne de tableau : commence par | et contient un numéro
            if re.match(r"^\|\s*\d+\s*\|", line):
                count += 1
            # Fin du tableau
            elif line.startswith("---") and count > 0:
                break
    return count


def _count_priority(text: str, label: str) -> int:
    """Compte le nombre d'articles avec une priorité donnée (A, B ou C)."""
    pattern = rf"Priorité {re.escape(label)}\b"
    return len(re.findall(pattern, text))


def build_parser() -> argparse.ArgumentParser:
    pillar_choices = list(PILLARS.keys())

    parser = argparse.ArgumentParser(
        prog="cocon-builder",
        description=(
            "Générateur de Cocon Sémantique schoolsWP — "
            "architecture 3 niveaux + scoring + maillage + priorités A/B/C"
        ),
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=(
            "Piliers disponibles :\n"
            + "\n".join(f"  {k:18} → {v}" for k, v in PILLARS.items())
            + "\n\n"
            "Exemples :\n"
            "  # Cocon minimal\n"
            "  python -m agents.cocon_builder.cli --pillar lms\n\n"
            "  # Avec contexte éditorial\n"
            "  python -m agents.cocon_builder.cli \\\n"
            "    --pillar lms \\\n"
            '    --context "12 articles publiés, focus Tutor LMS, peu sur LearnDash,'
            " audience freelances, aucun guide tunnel LMS gratuit\"\n\n"
            "  # Pipeline complet (KG + Autorité → Cocon)\n"
            "  python -m agents.cocon_builder.cli \\\n"
            "    --pillar lms \\\n"
            "    --graph-file content/docs/knowledge-graph.md \\\n"
            "    --authority-file audit/piliers/lms.md \\\n"
            "    --output cocons/lms.md\n\n"
            "Flux recommandé :\n"
            "  1. agents.knowledge_graph.cli   → knowledge-graph.md\n"
            "  2. agents.pillar_authority.cli  → audit/piliers/lms.md\n"
            "  3. agents.cocon_builder.cli     → cocons/lms.md"
        ),
    )
    parser.add_argument(
        "--pillar",
        required=True,
        choices=pillar_choices,
        metavar="PILIER",
        help=f"Pilier à développer : {' | '.join(pillar_choices)}",
    )
    parser.add_argument(
        "--context",
        default=None,
        metavar="CONTEXTE",
        help=(
            "Contexte éditorial actuel du pilier : articles existants, angles couverts, "
            "lacunes connues, cible audience "
            "(ex: '12 articles LMS, focus Tutor LMS, aucun comparatif prix')"
        ),
    )
    parser.add_argument(
        "--graph-file",
        default=None,
        metavar="FICHIER",
        help=(
            "Fichier Knowledge Graph (.md) produit par agents.knowledge_graph.cli. "
            "Enrichit les entités et les relations du cocon."
        ),
    )
    parser.add_argument(
        "--authority-file",
        default=None,
        metavar="FICHIER",
        help=(
            "Fichier d'analyse d'autorité (.md) produit par agents.pillar_authority.cli "
            "pour ce pilier. Aligne les priorités sur les zones faibles identifiées."
        ),
    )
    parser.add_argument(
        "--output",
        default=None,
        metavar="FICHIER",
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

    pillar_label = PILLARS[args.pillar]

    # Charger les fichiers optionnels
    graph_content: str | None = None
    if args.graph_file:
        try:
            graph_path = safe_read_path(args.graph_file)
            graph_content = graph_path.read_text(encoding="utf-8")
            print(f"[cocon-builder] Knowledge Graph chargé : {graph_path}", flush=True)
        except ValueError as e:
            print(f"[cocon-builder] Erreur accès refusé : {e} — ignoré", flush=True)
        except FileNotFoundError:
            print(
                f"[cocon-builder] ⚠ Fichier graph introuvable : {args.graph_file} — ignoré",
                flush=True,
            )

    authority_content: str | None = None
    if args.authority_file:
        try:
            auth_path = safe_read_path(args.authority_file)
            authority_content = auth_path.read_text(encoding="utf-8")
            print(f"[cocon-builder] Score autorité chargé : {auth_path}", flush=True)
        except ValueError as e:
            print(f"[cocon-builder] Erreur accès refusé : {e} — ignoré", flush=True)
        except FileNotFoundError:
            print(
                f"[cocon-builder] ⚠ Fichier autorité introuvable : {args.authority_file} — ignoré",
                flush=True,
            )

    agent = CoconBuilderAgent(model=args.model)

    print(f"\n[cocon-builder] Génération du cocon : {pillar_label}", flush=True)
    if args.context:
        print(f"  Contexte   : {args.context}", flush=True)
    if graph_content:
        print("  KG         : chargé", flush=True)
    if authority_content:
        print("  Autorité   : chargé", flush=True)
    print("", flush=True)

    cocon = await agent.run(
        pillar=pillar_label,
        context=args.context,
        graph_content=graph_content,
        authority_content=authority_content,
    )

    # Résumé rapide
    satellites = _count_satellites(cocon)
    prio_a = _count_priority(cocon, "A")
    prio_b = _count_priority(cocon, "B")
    prio_c = _count_priority(cocon, "C")

    if satellites > 0:
        print(
            f"  ✓ {satellites} satellites générés "
            f"— 🔴 {prio_a}A  🟡 {prio_b}B  🟢 {prio_c}C",
            flush=True,
        )
    print("", flush=True)

    if args.output:
        try:
            output_path = safe_write_path(args.output)
        except ValueError as e:
            print(f"[cocon-builder] Erreur : {e}", file=sys.stderr)
            sys.exit(1)
        output_path.parent.mkdir(parents=True, exist_ok=True)
        output_path.write_text(cocon, encoding="utf-8")
        print(f"[cocon-builder] Cocon sauvegardé → {output_path}")
    else:
        print(cocon)


if __name__ == "__main__":
    asyncio.run(main())
