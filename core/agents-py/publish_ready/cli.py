#!/usr/bin/env python3
"""
CLI — Super Agent Publish Ready Dashboard — schoolsWP

Orchestre les 4 modules d'audit en parallèle.
Produit un Publish Score composite /100 + plan d'action priorisé.

Modules exécutés simultanément :
  Module 1 — SEO Structure      (30 %)
  Module 2 — Citabilité IA      (25 %)
  Module 3 — Conversion & CTA   (25 %)
  Module 4 — Autorité Thématique (20 %)

Usage :
  # Audit complet (4 modules en parallèle)
  python -m agents.publish_ready.cli \\
    --file content/articles/lms-pilier/v4.md \\
    --keyword "formation en ligne rentable wordpress" \\
    --intent décisionnelle \\
    --pillar LMS \\
    --save-dir content/articles/lms-pilier/

  # Audit + correction automatique du module le plus faible
  python -m agents.publish_ready.cli \\
    --file content/articles/lms-pilier/v4.md \\
    --keyword "formation en ligne rentable wordpress" \\
    --fix-weakest \\
    --threshold 85 \\
    --save-dir content/articles/lms-pilier/

Interprétation Publish Score :
  ≥ 90  ✅  Publication immédiate
  80–89 🟡  1–2 optimisations ciblées
  70–79 🟠  Travail requis sur blocs faibles
  < 70  🔴  Révision substantielle
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

from agents.base import safe_read_path, safe_write_path
from agents.publish_ready.agent import PublishReadyAgent, PublishReadyResult

_INTENTS = ["informationnelle", "comparative", "décisionnelle", "transactionnelle"]
_PILLARS = ["SEO", "LMS", "CRM", "Performance", "Automatisation"]
_OBJECTIVES = ["email", "affiliation", "formation", "offre"]

_DASH = "━" * 62
_SEP = "─" * 62
_BAR = 20
_MINI = 10


def _pbar(score: int, width: int = _BAR) -> str:
    filled = round(score / 100 * width)
    return "█" * filled + "░" * (width - filled)


def _print_result(result: PublishReadyResult, elapsed: float) -> None:
    scores = result.scores_summary()
    print("\n" + _DASH)
    print("  Publish Ready Dashboard — schoolsWP")
    print(_DASH)
    print(f"  Publish Score  [{_pbar(result.publish_score)}] {result.publish_score}/100  {result.publish_emoji}")
    print(f"  Diagnostic     {result.publish_diagnostic}")
    print(f"  Bloc le plus faible : {result.weakest_module}")
    print(_SEP)
    print("  SCORES PAR MODULE")
    weights = {"SEO Structure": "30%", "Citabilité IA": "25%", "Conversion": "25%", "Autorité thème": "20%"}
    for name, score in scores.items():
        w = weights.get(name, "")
        bar = _pbar(score, _MINI)
        print(f"  {name:<20} [{bar}] {score:>3}/100  {w}")
    print(_SEP)

    # Plan d'action (extrait du plan priorisé)
    if result.action_plan:
        # Affiche uniquement les lignes numérotées (1. 2. 3.)
        action_lines = [
            line.strip()
            for line in result.action_plan.splitlines()
            if line.strip() and (line.strip()[0].isdigit() or line.strip().startswith("**"))
        ]
        if action_lines:
            print("  PLAN D'ACTION PRIORITAIRE")
            for line in action_lines[:8]:
                print(f"    {line}")
        print(_SEP)

    mode = "Audit complet"
    if result.fixed_article:
        wc = len(result.fixed_article.split())
        mode = f"Audit + Auto-fix ({wc} mots)"
    print(f"  {mode} terminé en {elapsed:.1f}s  ({4} modules en parallèle)")
    print(_DASH)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="publish-ready",
        description=(
            "Super Agent Publish Ready Dashboard — schoolsWP. "
            "4 modules d'audit en parallèle. "
            "Publish Score composite /100 + plan d'action priorisé."
        ),
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=(
            "Exemples :\n\n"
            "  # Audit complet\n"
            "  python -m agents.publish_ready.cli \\\n"
            "    --file content/articles/lms-pilier/v4.md \\\n"
            '    --keyword "formation en ligne rentable wordpress" \\\n'
            "    --intent décisionnelle --pillar LMS --save-dir content/articles/lms-pilier/\n\n"
            "  # Audit + auto-fix module le plus faible\n"
            "  python -m agents.publish_ready.cli \\\n"
            "    --file content/articles/lms-pilier/v4.md \\\n"
            '    --keyword "lms wordpress" \\\n'
            "    --fix-weakest --threshold 85 --save-dir content/articles/lms-pilier/"
        ),
    )

    source = parser.add_mutually_exclusive_group(required=True)
    source.add_argument("--file", metavar="FICHIER", help="Fichier markdown à auditer")
    source.add_argument("--text", metavar="TEXTE", help="Contenu markdown direct")

    parser.add_argument("--keyword", required=True, metavar="MOT_CLÉ")
    parser.add_argument("--intent", default=None, choices=_INTENTS, metavar="INTENT", help=f"{' | '.join(_INTENTS)}")
    parser.add_argument("--pillar", default=None, metavar="PILIER", help=f"Pilier schoolsWP : {' | '.join(_PILLARS)}")
    parser.add_argument(
        "--objective",
        default=None,
        choices=_OBJECTIVES,
        metavar="OBJECTIF",
        help=f"Objectif business : {' | '.join(_OBJECTIVES)}",
    )

    parser.add_argument(
        "--fix-weakest",
        action="store_true",
        help=(
            "Corrige automatiquement le module le plus faible si "
            "publish_score < --threshold. "
            "SEO→v2-fixed.md | Conversion→article-cta.md | LLM→article-optimized.md"
        ),
    )
    parser.add_argument("--threshold", type=int, default=85, metavar="N", help="Seuil de publication (défaut : 85)")

    parser.add_argument(
        "--save-dir",
        default=None,
        metavar="DOSSIER",
        help=(
            "Dossier de sauvegarde. Produit : "
            "publish-dashboard.md | seo-audit.md | citation-audit.md | "
            "conversion-audit.md | topical-audit.md [+ article corrigé]"
        ),
    )
    parser.add_argument("--output", default=None, metavar="FICHIER", help="Fichier unique pour le dashboard unifié")
    parser.add_argument("--model", default=None, metavar="MODEL", help="Modèle Claude (défaut : claude-sonnet-4-6)")

    return parser


async def main() -> None:
    parser = build_parser()
    args = parser.parse_args()

    if args.file:
        try:
            p = safe_read_path(args.file)
        except (ValueError, FileNotFoundError) as e:
            print(f"[publish-ready] Erreur : {e}", file=sys.stderr)
            sys.exit(1)
        article = p.read_text(encoding="utf-8")
        wc = len(article.split())
        print(f"\n[publish-ready] Fichier chargé : {p} ({wc} mots)", flush=True)
    else:
        article = args.text
        wc = len(article.split())
        print(f"\n[publish-ready] Texte reçu ({wc} mots)", flush=True)

    print(f"  Mot-clé   : {args.keyword}", flush=True)
    if args.intent:
        print(f"  Intent    : {args.intent}", flush=True)
    if args.pillar:
        print(f"  Pilier    : {args.pillar}", flush=True)
    if args.objective:
        print(f"  Objectif  : {args.objective}", flush=True)
    fix_label = f"Oui (seuil {args.threshold})" if args.fix_weakest else "Non"
    print(f"  Auto-fix  : {fix_label}", flush=True)
    print("\n  → Lancement des 4 modules en parallèle...", flush=True)

    agent = PublishReadyAgent(model=args.model)
    t_start = time.monotonic()

    result: PublishReadyResult = await agent.run(
        article=article,
        keyword=args.keyword,
        intent=args.intent,
        pillar=args.pillar,
        objective=args.objective,
        fix_weakest=args.fix_weakest,
        threshold=args.threshold,
    )

    elapsed = time.monotonic() - t_start

    scores = result.scores_summary()
    print(
        f"  ✓ SEO {scores['SEO Structure']}/100  "
        f"IA {scores['Citabilité IA']}/100  "
        f"Conv {scores['Conversion']}/100  "
        f"Auth {scores['Autorité thème']}/100  "
        f"→ Publish Score {result.publish_score}/100",
        flush=True,
    )

    _print_result(result, elapsed)

    if args.save_dir:
        try:
            save_path = safe_write_path(args.save_dir)
        except ValueError as e:
            print(f"[publish-ready] Erreur : {e}", file=sys.stderr)
            sys.exit(1)
        save_path.mkdir(parents=True, exist_ok=True)
        saved = []

        # Dashboard unifié
        (save_path / "publish-dashboard.md").write_text(result.dashboard, encoding="utf-8")
        saved.append("publish-dashboard.md")

        # Rapports individuels
        (save_path / "seo-audit.md").write_text(result.seo_result.report, encoding="utf-8")
        saved.append("seo-audit.md")

        (save_path / "citation-audit.md").write_text(result.llm_result.report, encoding="utf-8")
        saved.append("citation-audit.md")

        (save_path / "conversion-audit.md").write_text(result.conversion_result.report, encoding="utf-8")
        saved.append("conversion-audit.md")

        (save_path / "topical-audit.md").write_text(result.authority_result.report, encoding="utf-8")
        saved.append("topical-audit.md")

        # Article corrigé (si fix-weakest déclenché)
        if result.fixed_article and not result.fixed_article.startswith("[Note]"):
            weakest = result.weakest_module
            if "SEO" in weakest:
                fname = "v2-fixed.md"
            elif "Conversion" in weakest:
                fname = "article-cta.md"
            elif "IA" in weakest or "Citabilité" in weakest:
                fname = "article-optimized.md"
            else:
                fname = "article-fixed.md"
            (save_path / fname).write_text(result.fixed_article, encoding="utf-8")
            saved.append(fname)
        elif result.fixed_article.startswith("[Note]"):
            note_file = save_path / "authority-note.txt"
            note_file.write_text(result.fixed_article, encoding="utf-8")
            saved.append("authority-note.txt")

        print(f"\n  Fichiers → {save_path}/")
        for f in saved:
            print(f"  • {f}")

    elif args.output:
        try:
            out = safe_write_path(args.output)
        except ValueError as e:
            print(f"[publish-ready] Erreur : {e}", file=sys.stderr)
            sys.exit(1)
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(result.dashboard, encoding="utf-8")
        print(f"\n  Dashboard sauvegardé → {out}")

    else:
        print("\n" + "=" * 60)
        print(result.dashboard)
        if result.action_plan:
            print("\n" + "=" * 60)
            print(result.action_plan)


if __name__ == "__main__":
    asyncio.run(main())
