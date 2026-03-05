#!/usr/bin/env python3
"""
CLI — schoolsWP Brain Stratégique (Orchestrateur Central)

Ce n'est pas un outil de production de contenu.
C'est le cerveau décisionnel : il analyse, décide, et fournit des commandes CLI prêtes à exécuter.

Usage :
  # Analyse minimale (raisonne sur l'écosystème WP connu)
  python -m agents.strategic_brain.cli

  # Avec contexte seul
  python -m agents.strategic_brain.cli \\
    --context "trafic LMS stagne, SEO en croissance, objectif 50k/mois"

  # Analyse complète avec toutes les données
  python -m agents.strategic_brain.cli \\
    --context "..." \\
    --graph-file docs/knowledge-graph.md \\
    --authority-file audit/piliers/summary.md \\
    --cocon-file cocons/lms.md \\
    --roi-file plans/plan-roi.md \\
    --output decisions/brain-report.md

Flux recommandé (pipeline complet) :
  1. agents.knowledge_graph.cli        → docs/knowledge-graph.md
  2. agents.pillar_authority.cli --all → audit/piliers/summary.md
  3. agents.cocon_builder.cli          → cocons/<pilier>.md
  4. agents.roi_editorial_plan.cli     → plans/plan-roi.md
  5. agents.strategic_brain.cli  ← tu es ici (couche méta)
"""
import argparse
import asyncio
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from agents.strategic_brain.agent import StrategicBrainAgent


def _count_decisions(text: str) -> int:
    """Compte le nombre de décisions dans le Decision Board."""
    return len(re.findall(r"#### Décision \d+", text))


def _count_alerts(text: str) -> int:
    """Compte les alertes stratégiques."""
    return len(re.findall(r"^- ⚠", text, re.MULTILINE))


def _extract_top_opportunity(text: str) -> str | None:
    """Extrait la première opportunité ROI du rapport."""
    match = re.search(r"\*\*\[?1\]?\s+(.+?)\*\*", text)
    return match.group(1).strip() if match else None


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="strategic-brain",
        description=(
            "schoolsWP Brain — Orchestrateur stratégique central. "
            "Analyse l'écosystème, détecte les faiblesses, "
            "et produit un Decision Board avec commandes CLI prêtes à exécuter."
        ),
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=(
            "Exemples :\n"
            "  # Analyse rapide sans données\n"
            "  python -m agents.strategic_brain.cli \\\n"
            '    --context "20 articles publiés, pilier LMS dominant, SEO en construction"\n\n'
            "  # Analyse complète avec toutes les données du pipeline\n"
            "  python -m agents.strategic_brain.cli \\\n"
            '    --context "objectif : 50k visites/mois en 6 mois, cadence 1 article/semaine" \\\n'
            "    --graph-file docs/knowledge-graph.md \\\n"
            "    --authority-file audit/piliers/summary.md \\\n"
            "    --cocon-file cocons/lms.md \\\n"
            "    --roi-file plans/plan-roi-lms.md \\\n"
            "    --output decisions/brain-report.md\n\n"
            "Pipeline complet recommandé :\n"
            "  1. knowledge_graph.cli        → docs/knowledge-graph.md\n"
            "  2. pillar_authority.cli --all → audit/piliers/summary.md\n"
            "  3. cocon_builder.cli          → cocons/<pilier>.md\n"
            "  4. roi_editorial_plan.cli     → plans/plan-roi.md\n"
            "  5. strategic_brain.cli        → decisions/brain-report.md"
        ),
    )
    parser.add_argument(
        "--context",
        default=None,
        metavar="CONTEXTE",
        help=(
            "Situation actuelle de schoolsWP : objectifs, signaux détectés, "
            "contraintes, événements récents "
            "(ex: 'trafic LMS stagne depuis 2 mois, SEO en forte croissance, "
            "objectif 50k visites/mois en 6 mois')"
        ),
    )
    parser.add_argument(
        "--graph-file",
        default=None,
        metavar="FICHIER",
        help="Knowledge Graph (.md) — produit par agents.knowledge_graph.cli",
    )
    parser.add_argument(
        "--authority-file",
        default=None,
        metavar="FICHIER",
        help=(
            "Index d'autorité (.md) — produit par agents.pillar_authority.cli. "
            "summary.md (mode --all) recommandé pour la vision globale."
        ),
    )
    parser.add_argument(
        "--cocon-file",
        default=None,
        metavar="FICHIER",
        help=(
            "Cocon sémantique (.md) — produit par agents.cocon_builder.cli. "
            "Peut contenir plusieurs cocons concaténés."
        ),
    )
    parser.add_argument(
        "--roi-file",
        default=None,
        metavar="FICHIER",
        help="Plan ROI éditorial (.md) — produit par agents.roi_editorial_plan.cli",
    )
    parser.add_argument(
        "--articles",
        nargs="+",
        default=None,
        metavar="TITRE",
        help=(
            "Titres des articles déjà publiés. "
            "Exemples : --articles 'Tutor LMS vs LearnDash' 'FluentCRM guide'"
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

    # Chargement des fichiers
    def _load(path_str: str | None, label: str) -> str | None:
        if not path_str:
            return None
        p = Path(path_str)
        if not p.exists():
            print(
                f"[strategic-brain] ⚠ {label} introuvable : {p} — ignoré",
                flush=True,
            )
            return None
        content = p.read_text(encoding="utf-8")
        print(f"[strategic-brain] {label} chargé ({len(content):,} chars) : {p}", flush=True)
        return content

    graph_content = _load(args.graph_file, "Knowledge Graph")
    authority_content = _load(args.authority_file, "Index autorité")
    cocon_content = _load(args.cocon_file, "Cocon sémantique")
    roi_plan_content = _load(args.roi_file, "Plan ROI")

    # Bilan données disponibles
    data_count = sum(
        1 for x in [graph_content, authority_content, cocon_content, roi_plan_content]
        if x
    )

    print(f"\n[strategic-brain] Analyse en cours — {data_count}/4 sources de données", flush=True)
    if args.context:
        print(f"  Contexte : {args.context[:80]}{'...' if len(args.context or '') > 80 else ''}", flush=True)
    if data_count == 0:
        print(
            "  ⚠ Aucune donnée fournie — le Brain va raisonner sur l'écosystème WordPress connu.",
            flush=True,
        )
        print(
            "  💡 Pour une analyse précise, génère d'abord les données avec le pipeline 6→9.",
            flush=True,
        )
    print("", flush=True)

    agent = StrategicBrainAgent(model=args.model)

    report = await agent.run(
        context=args.context,
        graph_content=graph_content,
        authority_content=authority_content,
        cocon_content=cocon_content,
        roi_plan_content=roi_plan_content,
        existing_articles=args.articles,
    )

    # Résumé du Decision Board
    decisions = _count_decisions(report)
    alerts = _count_alerts(report)
    top_opp = _extract_top_opportunity(report)

    if decisions > 0:
        print(f"  ✓ {decisions} décision(s) stratégique(s) générée(s)", flush=True)
    if alerts > 0:
        print(f"  ⚠ {alerts} alerte(s) stratégique(s)", flush=True)
    if top_opp:
        print(f"  ★ Top opportunité : {top_opp}", flush=True)
    print("", flush=True)

    if args.output:
        output_path = Path(args.output)
        output_path.parent.mkdir(parents=True, exist_ok=True)
        output_path.write_text(report, encoding="utf-8")
        print(f"[strategic-brain] Decision Board sauvegardé → {output_path}")
    else:
        print(report)


if __name__ == "__main__":
    asyncio.run(main())
