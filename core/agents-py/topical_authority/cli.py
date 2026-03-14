#!/usr/bin/env python3
"""
CLI — Module Topical Authority Engine — schoolsWP

Score d'autorité thématique /100 sur 5 dimensions.
Mode --expand : génère le plan cluster complet (pilier + satellites + maillage).

Usage :
  # Audit autorité seul
  python -m agents.topical_authority.cli \\
    --file content/articles/lms-pilier/v4.md \\
    --keyword "formation en ligne rentable wordpress" \\
    --pillar LMS

  # Audit + plan cluster complet
  python -m agents.topical_authority.cli \\
    --file content/articles/lms-pilier/v4.md \\
    --keyword "formation en ligne rentable wordpress" \\
    --pillar LMS \\
    --expand \\
    --save-dir content/articles/lms-pilier/

Interprétation des scores :
  95–100  ✅  Article pilier
  85–94   🟢  Satellite fort
  70–84   🟡  Renforcement cluster nécessaire
  < 70    🔴  Contenu isolé
"""
import argparse
import asyncio
import io
import sys
import time
from pathlib import Path

# Force UTF-8 sur Windows
if hasattr(sys.stdout, "buffer") and sys.stdout.encoding.lower() not in ("utf-8", "utf8"):
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
if hasattr(sys.stderr, "buffer") and sys.stderr.encoding.lower() not in ("utf-8", "utf8"):
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding="utf-8", errors="replace")

sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from agents.topical_authority.agent import TopicalAuditResult, TopicalAuthorityAgent

_INTENTS = ["informationnelle", "comparative", "décisionnelle", "transactionnelle"]
_PILLARS = ["SEO", "LMS", "CRM", "Performance", "Automatisation"]

_BAR_WIDTH = 20
_BLOC_BAR_WIDTH = 10


def _score_bar(score: int, max_score: int = 100) -> str:
    filled = round(score / max_score * _BAR_WIDTH)
    bar = "█" * filled + "░" * (_BAR_WIDTH - filled)
    return f"[{bar}] {score}/{max_score}"


def _bloc_bar(score: int, max_score: int = 20) -> str:
    filled = round(score / max_score * _BLOC_BAR_WIDTH)
    bar = "█" * filled + "░" * (_BLOC_BAR_WIDTH - filled)
    return f"[{bar}] {score}/{max_score}"


def _print_result(result: TopicalAuditResult, elapsed: float) -> None:
    emoji = result.diagnostic_emoji
    diag = result.diagnostic

    print("\n" + "━" * 62)
    print("  Topical Authority Engine — schoolsWP")
    print("━" * 62)
    print(f"  Score Autorité    {_score_bar(result.score_autorite)}  {emoji}")
    print(f"  Diagnostic        {diag}")
    print(f"  Rôle recommandé   {result.role}")
    print("─" * 62)
    print("  DÉTAIL PAR DIMENSION")
    print(f"  Couverture sujet     {_bloc_bar(result.couverture)}")
    print(f"  Connexions internes  {_bloc_bar(result.connexions)}")
    print(f"  Cohérence sémantique {_bloc_bar(result.coherence)}")
    print(f"  Positionnement       {_bloc_bar(result.positionnement)}")
    print(f"  Potentiel cluster    {_bloc_bar(result.potentiel_cluster)}")
    print("─" * 62)

    if result.manques:
        print("  Manques identifiés :")
        for m in result.manques:
            print(f"    – {m}")

    if result.satellites:
        print("  Satellites recommandés :")
        for s in result.satellites:
            print(f"    → {s}")

    if result.justification:
        print(f"  Justification : {result.justification}")

    print("─" * 62)
    mode = "Audit + Expansion cluster" if result.expanded else "Audit seul"
    print(f"  {mode} terminé en {elapsed:.1f}s")
    print("━" * 62)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="topical-authority",
        description=(
            "Module Topical Authority Engine — schoolsWP. "
            "Score /100 sur 5 dimensions. "
            "Mode --expand : plan cluster complet (pilier + satellites + maillage)."
        ),
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=(
            "Exemples :\n\n"
            "  # Audit autorité\n"
            "  python -m agents.topical_authority.cli \\\n"
            '    --file content/articles/lms-pilier/v4.md \\\n'
            '    --keyword "formation en ligne rentable wordpress" --pillar LMS\n\n'
            "  # Audit + plan cluster\n"
            "  python -m agents.topical_authority.cli \\\n"
            '    --file content/articles/lms-pilier/v4.md \\\n'
            '    --keyword "formation en ligne rentable wordpress" \\\n'
            "    --pillar LMS --expand --save-dir content/articles/lms-pilier/"
        ),
    )

    source = parser.add_mutually_exclusive_group(required=True)
    source.add_argument("--file", metavar="FICHIER", help="Fichier markdown à auditer")
    source.add_argument("--text", metavar="TEXTE", help="Contenu markdown direct")

    parser.add_argument("--keyword", required=True, metavar="MOT_CLÉ",
                        help="Mot-clé SEO principal")
    parser.add_argument("--intent", default=None, choices=_INTENTS, metavar="INTENT",
                        help=f"Intention de recherche : {' | '.join(_INTENTS)}")
    parser.add_argument("--pillar", default=None, metavar="PILIER",
                        help=f"Pilier thématique schoolsWP : {' | '.join(_PILLARS)}")

    parser.add_argument("--expand", action="store_true",
                        help="Génère le plan cluster complet (pilier + satellites + maillage + ordre production)")

    parser.add_argument("--save-dir", default=None, metavar="DOSSIER",
                        help="Dossier de sauvegarde. Produit : topical-audit.md [+ cluster-plan.md]")
    parser.add_argument("--output", default=None, metavar="FICHIER",
                        help="Fichier unique pour le rapport d'audit")
    parser.add_argument("--model", default=None, metavar="MODEL",
                        help="Modèle Claude (défaut : claude-sonnet-4-6)")

    return parser


async def main() -> None:
    parser = build_parser()
    args = parser.parse_args()

    if args.file:
        p = Path(args.file)
        if not p.exists():
            print(f"[topical-authority] Fichier introuvable : {p}", file=sys.stderr)
            sys.exit(1)
        article = p.read_text(encoding="utf-8")
        word_count = len(article.split())
        print(f"\n[topical-authority] Fichier chargé : {p} ({word_count} mots)", flush=True)
    else:
        article = args.text
        word_count = len(article.split())
        print(f"\n[topical-authority] Texte reçu ({word_count} mots)", flush=True)

    print(f"  Mot-clé : {args.keyword}", flush=True)
    if args.intent:
        print(f"  Intent  : {args.intent}", flush=True)
    if args.pillar:
        print(f"  Pilier  : {args.pillar}", flush=True)
    mode_label = "Audit + Expansion cluster" if args.expand else "Audit seul"
    print(f"  Mode    : {mode_label}", flush=True)
    print("", flush=True)

    agent = TopicalAuthorityAgent(model=args.model)
    t_start = time.monotonic()

    if args.expand:
        print("  → Audit en cours...", flush=True)
        result: TopicalAuditResult = await agent.audit_and_expand(
            article=article,
            keyword=args.keyword,
            intent=args.intent,
            pillar=args.pillar,
        )
        wc_plan = len(result.cluster_plan.split())
        print(
            f"  ✓ Score {result.score_autorite}/100  →  Plan cluster ({wc_plan} mots)",
            flush=True,
        )
    else:
        print("  → Audit en cours...", flush=True)
        result = await agent.run(
            article=article,
            keyword=args.keyword,
            intent=args.intent,
            pillar=args.pillar,
        )
        print(f"  ✓ Audit terminé : {result.score_autorite}/100", flush=True)

    elapsed = time.monotonic() - t_start
    _print_result(result, elapsed)

    if args.save_dir:
        save_path = Path(args.save_dir)
        save_path.mkdir(parents=True, exist_ok=True)

        audit_file = save_path / "topical-audit.md"
        audit_file.write_text(result.report, encoding="utf-8")
        saved = ["topical-audit.md"]

        if result.expanded and result.cluster_plan:
            plan_file = save_path / "cluster-plan.md"
            plan_file.write_text(result.cluster_plan, encoding="utf-8")
            saved.append("cluster-plan.md")

        print(f"\n  Fichiers → {save_path}/")
        print(f"  {' | '.join(saved)}")

    elif args.output:
        out = Path(args.output)
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(result.report, encoding="utf-8")
        print(f"\n  Rapport sauvegardé → {out}")

    else:
        print("\n" + "=" * 60)
        print(result.report)
        if result.expanded and result.cluster_plan:
            print("\n" + "=" * 60)
            print("# Plan Cluster\n")
            print(result.cluster_plan)


if __name__ == "__main__":
    asyncio.run(main())
