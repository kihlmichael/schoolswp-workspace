#!/usr/bin/env python3
"""
CLI — Module Score Conversion & CTA Layer — schoolsWP

Audit stratégique /100 sur 5 blocs : clarté problème, décision, orientation action,
CTA stratégique, cohérence business. Mode --inject pour améliorer les CTA automatiquement.

Usage :
  # Audit seul
  python -m agents.conversion_auditor.cli \\
    --file content/articles/lms-pilier/v3.md \\
    --keyword "formation en ligne rentable wordpress" \\
    --intent décisionnelle

  # Audit + injection CTA si score < 85
  python -m agents.conversion_auditor.cli \\
    --file content/articles/lms-pilier/v3.md \\
    --keyword "formation en ligne rentable wordpress" \\
    --inject \\
    --save-dir content/articles/lms-pilier/

  # Avec objectif business prioritaire
  python -m agents.conversion_auditor.cli \\
    --file content/articles/lms-pilier/v4.md \\
    --keyword "lms wordpress" \\
    --objective formation \\
    --inject --save-dir content/articles/lms-pilier/

Interprétation des scores :
  95–100  ✅  Article business-ready
  85–94   🟡  Optimisations mineures
  70–84   🟠  Manque d'orientation action
  < 70    🔴  SEO sans levier business
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
from agents.conversion_auditor.agent import ConversionAuditorAgent, ConversionAuditResult

_INTENTS = ["informationnelle", "comparative", "décisionnelle", "transactionnelle"]
_OBJECTIVES = ["email", "affiliation", "formation", "offre"]

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


def _print_result(result: ConversionAuditResult, elapsed: float) -> None:
    emoji = result.diagnostic_emoji
    diag = result.diagnostic

    print("\n" + "━" * 62)
    print("  Score Conversion & CTA — schoolsWP")
    print("━" * 62)
    print(f"  Score global      {_score_bar(result.score_conversion)}  {emoji}")
    print(f"  Diagnostic        {diag}")
    print(f"  Bloc le plus faible : {result.weakest_bloc}")
    print("─" * 62)
    print("  DÉTAIL PAR BLOC")
    print(f"  Clarté problème    {_bloc_bar(result.clarte_probleme)}")
    print(f"  Décision           {_bloc_bar(result.decision)}")
    print(f"  Orientation action {_bloc_bar(result.orientation_action)}")
    print(f"  CTA stratégique    {_bloc_bar(result.cta)}")
    print(f"  Business alignment {_bloc_bar(result.business_alignment)}")
    print("─" * 62)

    if result.points_forts:
        print("  Points forts :")
        for p in result.points_forts:
            print(f"    + {p}")

    if result.faiblesses:
        print("  Faiblesses :")
        for f in result.faiblesses:
            print(f"    – {f}")

    if result.recommandations:
        print("  Recommandations concrètes :")
        for i, r in enumerate(result.recommandations, 1):
            print(f"    {i}. {r}")

    print("─" * 62)
    mode = "Audit + Injection CTA" if result.injected else "Audit seul"
    if result.injected:
        wc = len(result.article_with_cta.split())
        print(f"  {mode} terminé en {elapsed:.1f}s  (article : {wc} mots)")
    else:
        print(f"  {mode} terminé en {elapsed:.1f}s")
    print("━" * 62)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="conversion-auditor",
        description=(
            "Module Score Conversion & CTA Layer — schoolsWP. "
            "Audit /100 sur 5 blocs stratégiques. "
            "Mode --inject : améliore les CTA si score < seuil."
        ),
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=(
            "Exemples :\n\n"
            "  # Audit seul\n"
            "  python -m agents.conversion_auditor.cli \\\n"
            '    --file content/articles/lms-pilier/v3.md \\\n'
            '    --keyword "formation en ligne rentable wordpress"\n\n'
            "  # Audit + injection CTA\n"
            "  python -m agents.conversion_auditor.cli \\\n"
            '    --file content/articles/lms-pilier/v3.md \\\n'
            '    --keyword "formation en ligne rentable wordpress" \\\n'
            "    --inject --save-dir content/articles/lms-pilier/\n\n"
            "  # Avec objectif business\n"
            "  python -m agents.conversion_auditor.cli \\\n"
            '    --file content/articles/lms-pilier/v4.md \\\n'
            '    --keyword "lms wordpress" \\\n'
            "    --objective formation --inject --save-dir content/articles/lms-pilier/"
        ),
    )

    # --- Source de contenu ---
    source = parser.add_mutually_exclusive_group(required=True)
    source.add_argument(
        "--file",
        metavar="FICHIER",
        help="Fichier markdown (.md) à auditer",
    )
    source.add_argument(
        "--text",
        metavar="TEXTE",
        help="Contenu markdown passé directement en argument",
    )

    # --- Contexte ---
    parser.add_argument(
        "--keyword",
        required=True,
        metavar="MOT_CLÉ",
        help="Mot-clé SEO principal de l'article",
    )
    parser.add_argument(
        "--intent",
        default=None,
        choices=_INTENTS,
        metavar="INTENT",
        help=f"Intention de recherche : {' | '.join(_INTENTS)}",
    )
    parser.add_argument(
        "--objective",
        default=None,
        choices=_OBJECTIVES,
        metavar="OBJECTIF",
        help=(
            f"Objectif business prioritaire : {' | '.join(_OBJECTIVES)}. "
            "Oriente l'analyse du bloc Business alignment."
        ),
    )

    # --- Mode injection ---
    parser.add_argument(
        "--inject",
        action="store_true",
        help=(
            "Active l'injection/amélioration des CTA si score < --threshold. "
            "Ne réécrit pas l'article — améliore uniquement la couche CTA."
        ),
    )
    parser.add_argument(
        "--threshold",
        type=int,
        default=85,
        metavar="N",
        help="Score minimum pour éviter l'injection (défaut : 85)",
    )

    # --- Sorties ---
    parser.add_argument(
        "--save-dir",
        default=None,
        metavar="DOSSIER",
        help=(
            "Dossier de sauvegarde. "
            "Produit : conversion-audit.md + article-cta.md (si --inject)"
        ),
    )
    parser.add_argument(
        "--output",
        default=None,
        metavar="FICHIER",
        help="Fichier unique pour le rapport d'audit (.md)",
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

    # --- Chargement du contenu ---
    if args.file:
        try:
            p = safe_read_path(args.file)
        except (ValueError, FileNotFoundError) as e:
            print(f"[conversion-auditor] Erreur : {e}", file=sys.stderr)
            sys.exit(1)
        article = p.read_text(encoding="utf-8")
        word_count = len(article.split())
        print(f"\n[conversion-auditor] Fichier chargé : {p} ({word_count} mots)", flush=True)
    else:
        article = args.text
        word_count = len(article.split())
        print(f"\n[conversion-auditor] Texte reçu ({word_count} mots)", flush=True)

    print(f"  Mot-clé   : {args.keyword}", flush=True)
    if args.intent:
        print(f"  Intent    : {args.intent}", flush=True)
    if args.objective:
        print(f"  Objectif  : {args.objective}", flush=True)
    mode_label = f"Audit + Injection CTA (seuil {args.threshold})" if args.inject else "Audit seul"
    print(f"  Mode      : {mode_label}", flush=True)
    print("", flush=True)

    agent = ConversionAuditorAgent(model=args.model)
    t_start = time.monotonic()

    if args.inject:
        print("  → Audit en cours...", flush=True)
        result: ConversionAuditResult = await agent.audit_and_inject(
            article=article,
            keyword=args.keyword,
            intent=args.intent,
            objective=args.objective,
            threshold=args.threshold,
        )
        if result.injected:
            wc_cta = len(result.article_with_cta.split())
            print(
                f"  ✓ Score {result.score_conversion}/100  →  CTA injectés ({wc_cta} mots)",
                flush=True,
            )
        else:
            print(
                f"  ✓ Score {result.score_conversion}/100  →  Seuil {args.threshold} déjà atteint, pas d'injection",
                flush=True,
            )
    else:
        print("  → Audit en cours...", flush=True)
        result = await agent.run(
            article=article,
            keyword=args.keyword,
            intent=args.intent,
            objective=args.objective,
        )
        print(f"  ✓ Audit terminé : {result.score_conversion}/100", flush=True)

    elapsed = time.monotonic() - t_start

    # --- Affichage terminal ---
    _print_result(result, elapsed)

    # --- Sauvegarde ---
    if args.save_dir:
        save_path = safe_write_path(args.save_dir)
        save_path.mkdir(parents=True, exist_ok=True)

        report_file = save_path / "conversion-audit.md"
        report_file.write_text(result.report, encoding="utf-8")
        saved = ["conversion-audit.md"]

        if result.injected and result.article_with_cta:
            cta_file = save_path / "article-cta.md"
            cta_file.write_text(result.article_with_cta, encoding="utf-8")
            saved.append("article-cta.md")

        print(f"\n  Fichiers → {save_path}/")
        print(f"  {' | '.join(saved)}")

    elif args.output:
        out = safe_write_path(args.output)
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(result.report, encoding="utf-8")
        print(f"\n  Rapport sauvegardé → {out}")

    else:
        print("\n" + "=" * 60)
        print(result.report)
        if result.injected and result.article_with_cta:
            print("\n" + "=" * 60)
            print("# Article avec CTA améliorés\n")
            print(result.article_with_cta)


if __name__ == "__main__":
    asyncio.run(main())
