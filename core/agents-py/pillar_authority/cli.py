#!/usr/bin/env python3
"""
CLI — Index d'Autorité par Pilier schoolsWP

Usage :
  python -m agents.pillar_authority.cli --pillar lms
  python -m agents.pillar_authority.cli --pillar seo --context "12 articles, focus Yoast"
  python -m agents.pillar_authority.cli --all
  python -m agents.pillar_authority.cli --all --graph-file content/docs/knowledge-graph.md --output audit/
"""
import argparse
import asyncio
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from agents.base import safe_read_path, safe_write_path
from agents.pillar_authority.agent import PILLARS, PillarAuthorityAgent

# Seuils de diagnostic
_DIAGNOSTIC_EMOJI = {
    "dominant": "💎",
    "solide": "🟢",
    "construction": "🟡",
    "faible": "🔴",
}


def _parse_score(text: str) -> int | None:
    """Extrait le score total /100 depuis l'output markdown."""
    match = re.search(r"\*\*Score total\*\*\s*\|\s*\*\*(\d+)/100\*\*", text)
    if match:
        return int(match.group(1))
    # Fallback : cherche "X/100" dans le texte
    match = re.search(r"\b(\d{1,3})/100\b", text)
    return int(match.group(1)) if match else None


def _parse_diagnostic(score: int | None) -> str:
    if score is None:
        return "?"
    if score > 85:
        return "💎 Dominant"
    if score >= 70:
        return "🟢 Solide"
    if score >= 50:
        return "🟡 En construction"
    return "🔴 Faible"


def build_parser() -> argparse.ArgumentParser:
    pillar_choices = list(PILLARS.keys())

    parser = argparse.ArgumentParser(
        prog="pillar-authority",
        description=(
            "Index d'Autorité par Pilier schoolsWP — "
            "score /100 + diagnostic + plan d'action"
        ),
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=(
            "Piliers disponibles :\n"
            + "\n".join(f"  {k:18} → {v}" for k, v in PILLARS.items())
            + "\n\n"
            "Exemples :\n"
            "  # Analyser un pilier\n"
            "  python -m agents.pillar_authority.cli --pillar lms\n\n"
            "  # Avec contexte\n"
            "  python -m agents.pillar_authority.cli \\\n"
            '    --pillar lms \\\n'
            '    --context "12 articles, focus Tutor LMS, peu sur LearnDash, aucun comparatif prix"\n\n'
            "  # Tous les piliers (dashboard complet)\n"
            "  python -m agents.pillar_authority.cli --all\n\n"
            "  # Tous les piliers avec Knowledge Graph + sortie répertoire\n"
            "  python -m agents.pillar_authority.cli \\\n"
            "    --all \\\n"
            "    --graph-file content/docs/knowledge-graph.md \\\n"
            "    --output audit/piliers/"
        ),
    )

    mode_group = parser.add_mutually_exclusive_group(required=True)
    mode_group.add_argument(
        "--pillar",
        choices=pillar_choices,
        metavar="PILIER",
        help=(
            f"Pilier à analyser : {' | '.join(pillar_choices)}. "
            "Incompatible avec --all."
        ),
    )
    mode_group.add_argument(
        "--all",
        action="store_true",
        help="Analyser tous les piliers en séquence et afficher un tableau récapitulatif.",
    )

    parser.add_argument(
        "--context",
        default=None,
        metavar="CONTEXTE",
        help=(
            "Contexte éditorial du pilier (ou global si --all) : "
            "articles existants, angles couverts, lacunes connues "
            "(ex: '12 articles LMS, focus Tutor LMS, aucun comparatif prix')"
        ),
    )
    parser.add_argument(
        "--graph-file",
        default=None,
        metavar="FICHIER",
        help=(
            "Fichier Knowledge Graph produit par agents.knowledge_graph.cli "
            "(.md). Enrichit l'analyse avec les données de couverture réelles."
        ),
    )
    parser.add_argument(
        "--output",
        default=None,
        metavar="SORTIE",
        help=(
            "Fichier de sortie (.md) pour --pillar, "
            "ou répertoire de sortie pour --all (un fichier par pilier + summary.md). "
            "Si absent, affiche dans le terminal."
        ),
    )
    parser.add_argument(
        "--model",
        default=None,
        metavar="MODEL",
        help="Modèle Claude (défaut : $MODEL_WRITER ou claude-sonnet-4-6)",
    )
    return parser


async def analyze_pillar(
    agent: PillarAuthorityAgent,
    pillar_key: str,
    context: str | None,
    graph_content: str | None,
) -> tuple[str, str, int | None]:
    """Analyse un pilier et retourne (pillar_key, output_text, score)."""
    pillar_label = PILLARS[pillar_key]
    print(f"  [{pillar_label}] Analyse en cours...", flush=True)

    result = await agent.run(
        pillar=pillar_label,
        context=context,
        graph_content=graph_content,
    )

    score = _parse_score(result)
    diagnostic = _parse_diagnostic(score)
    score_str = f"{score}/100" if score is not None else "?/100"
    print(f"  [{pillar_label}] {score_str} — {diagnostic}", flush=True)

    return pillar_key, result, score


async def main() -> None:
    parser = build_parser()
    args = parser.parse_args()

    # Charger le Knowledge Graph si fourni
    graph_content: str | None = None
    if args.graph_file:
        try:
            graph_path = safe_read_path(args.graph_file)
            graph_content = graph_path.read_text(encoding="utf-8")
            print(f"[pillar-authority] Knowledge Graph chargé : {graph_path}", flush=True)
        except ValueError as e:
            print(f"[pillar-authority] Erreur accès refusé : {e} — ignoré", flush=True)
        except FileNotFoundError:
            print(
                f"[pillar-authority] ⚠ Fichier graph introuvable : {args.graph_file} — ignoré",
                flush=True,
            )

    agent = PillarAuthorityAgent(model=args.model)

    # ──────────────────────────────────────────────
    # Mode : un seul pilier
    # ──────────────────────────────────────────────
    if args.pillar:
        pillar_label = PILLARS[args.pillar]
        print(f"\n[pillar-authority] Analyse du pilier : {pillar_label}", flush=True)
        if args.context:
            print(f"  Contexte : {args.context}", flush=True)
        print("", flush=True)

        result = await agent.run(
            pillar=pillar_label,
            context=args.context,
            graph_content=graph_content,
        )

        score = _parse_score(result)
        if score is not None:
            print(
                f"  ✓ Score : {score}/100 — {_parse_diagnostic(score)}\n",
                flush=True,
            )

        if args.output:
            try:
                output_path = safe_write_path(args.output)
            except ValueError as e:
                print(f"[pillar-authority] Erreur : {e}", file=sys.stderr)
                sys.exit(1)
            output_path.parent.mkdir(parents=True, exist_ok=True)
            output_path.write_text(result, encoding="utf-8")
            print(f"[pillar-authority] Sauvegardé → {output_path}")
        else:
            print(result)

    # ──────────────────────────────────────────────
    # Mode : tous les piliers (--all)
    # ──────────────────────────────────────────────
    else:
        print(
            f"\n[pillar-authority] Analyse complète — {len(PILLARS)} piliers",
            flush=True,
        )
        if args.context:
            print(f"  Contexte global : {args.context}", flush=True)
        if graph_content:
            print("  Knowledge Graph : chargé", flush=True)
        print("", flush=True)

        results: list[tuple[str, str, int | None]] = []
        for pillar_key in PILLARS:
            key, text, score = await analyze_pillar(
                agent, pillar_key, args.context, graph_content
            )
            results.append((key, text, score))

        # Tableau récapitulatif
        print("\n", flush=True)
        print("━" * 60, flush=True)
        print("  RÉCAPITULATIF — Index d'Autorité schoolsWP", flush=True)
        print("━" * 60, flush=True)

        summary_rows: list[str] = []
        summary_rows.append(
            "# Index d'Autorité par Pilier — schoolsWP\n\n"
            "| Pilier | Score | Diagnostic |\n"
            "|--------|-------|------------|\n"
        )

        for pillar_key, _, score in results:
            label = PILLARS[pillar_key]
            score_str = f"{score}/100" if score is not None else "?/100"
            diagnostic = _parse_diagnostic(score)
            print(f"  {label:<28} {score_str:<10} {diagnostic}", flush=True)
            summary_rows.append(f"| {label} | {score_str} | {diagnostic} |\n")

        print("━" * 60, flush=True)
        print("", flush=True)

        summary_content = "".join(summary_rows)

        # Sauvegarde
        if args.output:
            try:
                output_dir = safe_write_path(args.output)
            except ValueError as e:
                print(f"[pillar-authority] Erreur : {e}", file=sys.stderr)
                sys.exit(1)
            output_dir.mkdir(parents=True, exist_ok=True)

            # Un fichier par pilier
            for pillar_key, text, _ in results:
                pillar_file = output_dir / f"{pillar_key}.md"
                pillar_file.write_text(text, encoding="utf-8")
                print(f"[pillar-authority] → {pillar_file}")

            # Fichier récapitulatif
            summary_path = output_dir / "summary.md"
            # Ajouter les analyses complètes dans le summary
            full_summary = summary_content + "\n---\n\n"
            for pillar_key, text, _ in results:
                full_summary += text + "\n\n---\n\n"
            summary_path.write_text(full_summary, encoding="utf-8")
            print(f"[pillar-authority] Récapitulatif → {summary_path}")
        else:
            # Afficher chaque analyse
            for _, text, _ in results:
                print(text)
                print("\n---\n")


if __name__ == "__main__":
    asyncio.run(main())
