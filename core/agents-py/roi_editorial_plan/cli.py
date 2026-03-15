#!/usr/bin/env python3
"""
CLI — Plan Éditorial Auto-Priorisé ROI schoolsWP

Usage :
  python -m agents.roi_editorial_plan.cli
  python -m agents.roi_editorial_plan.cli --pillar lms
  python -m agents.roi_editorial_plan.cli --pillar lms --context "1 article/semaine"
  python -m agents.roi_editorial_plan.cli \\
      --authority-file audit/piliers/summary.md \\
      --cocon-file cocons/lms.md \\
      --graph-file content/docs/knowledge-graph.md \\
      --output plans/plan-roi.md

Flux recommandé :
  1. agents.knowledge_graph.cli        → content/docs/knowledge-graph.md
  2. agents.pillar_authority.cli --all → audit/piliers/summary.md
  3. agents.cocon_builder.cli          → cocons/<pilier>.md
  4. agents.roi_editorial_plan.cli     → plans/plan-roi.md  ← tu es ici
"""
import argparse
import asyncio
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from agents.base import safe_read_path, safe_write_path
from agents.roi_editorial_plan.agent import RoiEditorialPlanAgent

# Piliers disponibles — aligné avec pillar_authority et cocon_builder
_PILLAR_CHOICES = [
    "seo", "lms", "crm", "automatisation", "performance", "ecommerce",
]
_PILLAR_LABELS = {
    "seo": "SEO WordPress",
    "lms": "LMS WordPress",
    "crm": "CRM WordPress",
    "automatisation": "Automatisation WordPress",
    "performance": "Performance WordPress",
    "ecommerce": "E-commerce WordPress",
}


def _parse_roi_stats(text: str) -> dict[str, int]:
    """Extrait les compteurs A/B/C et quick wins du plan."""
    stats: dict[str, int] = {"A": 0, "B": 0, "C": 0}
    for line in text.splitlines():
        if re.search(r"🔥\s*A\b", line):
            stats["A"] += 1
        elif re.search(r"🟡\s*B\b", line):
            stats["B"] += 1
        elif re.search(r"🔵\s*C\b", line):
            stats["C"] += 1
    # Dé-doublonner (chaque article peut apparaître en tableau + détail)
    # Heuristique : au moins une ligne de tableau (commence par | \d)
    a = b = c = 0
    for line in text.splitlines():
        if re.match(r"^\|\s*\d+\s*\|", line):
            if "🔥" in line or "A |" in line.split("|")[-2]:
                a += 1
            elif "🟡" in line or "B |" in line.split("|")[-2]:
                b += 1
            elif "🔵" in line or "C |" in line.split("|")[-2]:
                c += 1
    if a + b + c > 0:
        stats = {"A": a, "B": b, "C": c}
    return stats


def _parse_top_roi(text: str) -> str | None:
    """Extrait la ligne avec le Score ROI le plus élevé."""
    best_score = -1.0
    best_title = None
    for line in text.splitlines():
        if re.match(r"^\|\s*\d+\s*\|", line):
            match = re.search(r"\|\s*(\d+\.\d+)\s*\|", line)
            if match:
                score = float(match.group(1))
                if score > best_score:
                    best_score = score
                    # Extraire le titre (2e colonne)
                    parts = [p.strip() for p in line.split("|")]
                    if len(parts) >= 3:
                        best_title = parts[2]
    return f"{best_title} ({best_score})" if best_title else None


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="roi-editorial-plan",
        description=(
            "Plan Éditorial Auto-Priorisé ROI schoolsWP — "
            "Score ROI = (SEO×0.35) + (Biz×0.35) + (Auth×0.2) − (Effort×0.1)"
        ),
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=(
            "Exemples :\n"
            "  # Plan global tous piliers\n"
            "  python -m agents.roi_editorial_plan.cli\n\n"
            "  # Focus sur le pilier LMS\n"
            "  python -m agents.roi_editorial_plan.cli --pillar lms\n\n"
            "  # Plan complet avec toutes les données\n"
            "  python -m agents.roi_editorial_plan.cli \\\n"
            "    --pillar lms \\\n"
            '    --context "1 article/semaine, priorité rentabilité LMS" \\\n'
            "    --graph-file content/docs/knowledge-graph.md \\\n"
            "    --authority-file audit/piliers/summary.md \\\n"
            "    --cocon-file cocons/lms.md \\\n"
            "    --output plans/plan-roi-lms.md\n\n"
            "Flux recommandé :\n"
            "  knowledge_graph.cli → pillar_authority.cli --all → cocon_builder.cli → roi_editorial_plan.cli"
        ),
    )
    parser.add_argument(
        "--pillar",
        default=None,
        choices=_PILLAR_CHOICES,
        metavar="PILIER",
        help=(
            f"Pilier de focus : {' | '.join(_PILLAR_CHOICES)}. "
            "Si absent, plan global tous piliers."
        ),
    )
    parser.add_argument(
        "--context",
        default=None,
        metavar="CONTEXTE",
        help=(
            "Contexte éditorial : cadence, objectifs, audience, contraintes de prod "
            "(ex: '1 article/semaine, audience freelances WP, priorité LMS + SEO')"
        ),
    )
    parser.add_argument(
        "--graph-file",
        default=None,
        metavar="FICHIER",
        help="Fichier Knowledge Graph (.md) — produit par agents.knowledge_graph.cli",
    )
    parser.add_argument(
        "--authority-file",
        default=None,
        metavar="FICHIER",
        help=(
            "Fichier scores d'autorité (.md) — produit par agents.pillar_authority.cli. "
            "summary.md (--all) recommandé pour vision globale."
        ),
    )
    parser.add_argument(
        "--cocon-file",
        default=None,
        metavar="FICHIER",
        help="Fichier cocon sémantique (.md) — produit par agents.cocon_builder.cli",
    )
    parser.add_argument(
        "--articles",
        nargs="+",
        default=None,
        metavar="TITRE",
        help=(
            "Titres d'articles déjà publiés (évite les doublons). "
            "Exemples : --articles 'Tutor LMS vs LearnDash' 'FluentCRM guide complet'"
        ),
    )
    parser.add_argument(
        "--count",
        type=int,
        default=15,
        metavar="N",
        help="Nombre d'idées à générer (défaut : 15, min : 10, max : 30)",
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

    # Validation count
    count = max(10, min(30, args.count))
    if count != args.count:
        print(
            f"[roi-editorial-plan] ⚠ --count ajusté à {count} (plage : 10–30)",
            flush=True,
        )

    # Charger les fichiers optionnels
    def _load_file(path_str: str | None, label: str) -> str | None:
        if not path_str:
            return None
        try:
            p = safe_read_path(path_str)
        except ValueError as e:
            print(f"[roi-editorial-plan] Erreur accès refusé : {e} — ignoré", flush=True)
            return None
        except FileNotFoundError:
            print(
                f"[roi-editorial-plan] ⚠ {label} introuvable : {path_str} — ignoré",
                flush=True,
            )
            return None
        content = p.read_text(encoding="utf-8")
        print(f"[roi-editorial-plan] {label} chargé : {p}", flush=True)
        return content

    graph_content = _load_file(args.graph_file, "Knowledge Graph")
    authority_content = _load_file(args.authority_file, "Scores autorité")
    cocon_content = _load_file(args.cocon_file, "Cocon sémantique")

    # Résumé des inputs
    pillar_label = _PILLAR_LABELS.get(args.pillar, "Tous piliers") if args.pillar else "Tous piliers"
    data_loaded = sum(
        1 for x in [graph_content, authority_content, cocon_content] if x
    )

    print("\n[roi-editorial-plan] Génération du plan éditorial ROI", flush=True)
    print(f"  Focus       : {pillar_label}", flush=True)
    print(f"  Idées       : {count}", flush=True)
    print(f"  Données     : {data_loaded}/3 fichier(s) chargé(s)", flush=True)
    if args.context:
        print(f"  Contexte    : {args.context}", flush=True)
    if args.articles:
        print(f"  Articles ex : {len(args.articles)} fourni(s)", flush=True)
    print("", flush=True)

    agent = RoiEditorialPlanAgent(model=args.model)

    plan = await agent.run(
        pillar=_PILLAR_LABELS.get(args.pillar) if args.pillar else None,
        context=args.context,
        graph_content=graph_content,
        authority_content=authority_content,
        cocon_content=cocon_content,
        existing_articles=args.articles,
        count=count,
    )

    # Résumé rapide
    stats = _parse_roi_stats(plan)
    top = _parse_top_roi(plan)

    total = stats["A"] + stats["B"] + stats["C"]
    if total > 0:
        print(
            f"  ✓ {total} articles — "
            f"🔥 {stats['A']}A  🟡 {stats['B']}B  🔵 {stats['C']}C",
            flush=True,
        )
    if top:
        print(f"  ✓ Top ROI   : {top}", flush=True)
    print("", flush=True)

    if args.output:
        try:
            output_path = safe_write_path(args.output)
        except ValueError as e:
            print(f"[roi-editorial-plan] Erreur : {e}", file=sys.stderr)
            sys.exit(1)
        output_path.parent.mkdir(parents=True, exist_ok=True)
        output_path.write_text(plan, encoding="utf-8")
        print(f"[roi-editorial-plan] Plan sauvegardé → {output_path}")
    else:
        print(plan)


if __name__ == "__main__":
    asyncio.run(main())
