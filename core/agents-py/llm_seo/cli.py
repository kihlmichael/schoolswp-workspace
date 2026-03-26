#!/usr/bin/env python3
"""
CLI — Module LLM-SEO schoolsWP

Audit de citabilité IA + optimisation AI Overviews.
Score /100 sur 5 signaux + probabilités de citation par plateforme.

Usage :
  # Audit uniquement (score + signaux + probabilités)
  python -m agents.llm_seo.cli \\
    --file content/articles/lms-pilier/v3.md \\
    --keyword "formation en ligne rentable wordpress" \\
    --intent décisionnelle

  # Audit + injection des signaux manquants
  python -m agents.llm_seo.cli \\
    --file content/articles/lms-pilier/v3.md \\
    --keyword "formation en ligne rentable wordpress" \\
    --optimize \\
    --save-dir content/articles/lms-pilier/

  # Texte direct (sans fichier)
  python -m agents.llm_seo.cli \\
    --text "# Mon article..." \\
    --keyword "lms wordpress" \\
    --optimize

Interprétation des scores :
  85–100  ✅  Hautement citable
  70–84   🟡  Citable — optimisations mineures
  50–69   🟠  Partiellement citable
  < 50    🔴  Non optimisé pour les IA
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
from agents.llm_seo.agent import CitationSignalResult, LlmSeoAgent

_INTENTS = ["informationnelle", "comparative", "décisionnelle", "transactionnelle"]

_BAR_WIDTH = 20
_SIGNAL_BAR_WIDTH = 10


def _score_bar(score: int, max_score: int = 100) -> str:
    """Barre de progression ASCII pour le score global."""
    filled = round(score / max_score * _BAR_WIDTH)
    bar = "█" * filled + "░" * (_BAR_WIDTH - filled)
    return f"[{bar}] {score}/{max_score}"


def _signal_bar(score: int, max_score: int) -> str:
    """Barre courte pour les signaux individuels."""
    filled = round(score / max_score * _SIGNAL_BAR_WIDTH)
    bar = "█" * filled + "░" * (_SIGNAL_BAR_WIDTH - filled)
    return f"[{bar}] {score}/{max_score}"


def _pct_bar(pct: int) -> str:
    """Barre de probabilité (0-100 %)."""
    filled = round(pct / 100 * _SIGNAL_BAR_WIDTH)
    bar = "█" * filled + "░" * (_SIGNAL_BAR_WIDTH - filled)
    return f"[{bar}] {pct} %"


def _print_result(result: CitationSignalResult, elapsed: float) -> None:
    """Affiche le rapport formaté dans le terminal."""
    emoji = result.diagnostic_emoji
    diag = result.diagnostic

    print("\n" + "━" * 62)
    print("  LLM-SEO schoolsWP — Audit Citabilité IA")
    print("━" * 62)
    print(f"  Score citation  {_score_bar(result.citation_score)}  {emoji}")
    print(f"  Diagnostic      {diag}")
    print(f"  Meilleure plateforme : {result.best_platform}")
    print("─" * 62)
    print("  SIGNAUX DÉTECTÉS")
    s = result
    print(f"  Réponse rapide      {_signal_bar(s.signal_reponse_rapide, 25)}  {s.status_reponse_rapide}")
    print(f"  Blocs extractibles  {_signal_bar(s.signal_blocs_extractibles, 25)}  {s.status_blocs}")
    print(f"  Définitions         {_signal_bar(s.signal_definitions, 20)}  {s.status_definitions}")
    print(f"  Structure snippet   {_signal_bar(s.signal_structure_snippet, 15)}  {s.status_snippet}")
    print(f"  Cohérence           {_signal_bar(s.signal_coherence, 15)}  {s.status_coherence}")
    print("─" * 62)
    print("  PROBABILITÉS DE CITATION")
    print(f"  Google AI Overview  {_pct_bar(s.google_ai_overview_pct)}")
    print(f"  Perplexity          {_pct_bar(s.perplexity_pct)}")
    print(f"  ChatGPT Browse      {_pct_bar(s.chatgpt_pct)}")
    print(f"  Bing Copilot        {_pct_bar(s.bing_pct)}")
    print("─" * 62)

    if result.points_forts:
        print("  Points forts :")
        for p in result.points_forts:
            print(f"    + {p}")

    if result.signaux_manquants:
        print("  Signaux manquants :")
        for p in result.signaux_manquants:
            print(f"    – {p}")

    if result.recommandations:
        print("  Recommandations d'optimisation :")
        for i, r in enumerate(result.recommandations, 1):
            print(f"    {i}. {r}")

    print("─" * 62)
    mode = "Audit + Optimisation" if result.optimized else "Audit seul"
    if result.optimized:
        wc = len(result.article_optimized.split())
        print(f"  {mode} terminé en {elapsed:.1f}s  (article optimisé : {wc} mots)")
    else:
        print(f"  {mode} terminé en {elapsed:.1f}s")
    print("━" * 62)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="llm-seo",
        description=(
            "Module LLM-SEO schoolsWP — Audit citabilité IA /100 sur 5 signaux. "
            "Mode --optimize : injection des signaux manquants."
        ),
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=(
            "Exemples :\n\n"
            "  # Audit citabilité IA\n"
            "  python -m agents.llm_seo.cli \\\n"
            "    --file content/articles/lms-pilier/v3.md \\\n"
            '    --keyword "formation en ligne rentable wordpress" \\\n'
            "    --intent décisionnelle\n\n"
            "  # Audit + injection des signaux manquants\n"
            "  python -m agents.llm_seo.cli \\\n"
            "    --file content/articles/lms-pilier/v3.md \\\n"
            '    --keyword "formation en ligne rentable wordpress" \\\n'
            "    --optimize --save-dir content/articles/lms-pilier/\n\n"
            "  # Texte direct + optimisation\n"
            "  python -m agents.llm_seo.cli \\\n"
            '    --text "# Mon article..." \\\n'
            '    --keyword "lms wordpress" --optimize'
        ),
    )

    # --- Source de contenu (l'un ou l'autre) ---
    source = parser.add_mutually_exclusive_group(required=True)
    source.add_argument(
        "--file",
        metavar="FICHIER",
        help="Fichier markdown (.md) à analyser",
    )
    source.add_argument(
        "--text",
        metavar="TEXTE",
        help="Contenu markdown passé directement en argument (guillemets requis)",
    )

    # --- Contexte SEO ---
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
        help=f"Intention de recherche : {' | '.join(_INTENTS)} (optionnel)",
    )

    # --- Mode optimisation ---
    parser.add_argument(
        "--optimize",
        action="store_true",
        help=(
            "Active l'injection des signaux manquants après l'audit. "
            "Produit un article optimisé sans réécrire ce qui fonctionne."
        ),
    )

    # --- Sorties ---
    parser.add_argument(
        "--save-dir",
        default=None,
        metavar="DOSSIER",
        help=("Dossier de sauvegarde. Produit : citation-audit.md (rapport) + article-optimized.md (si --optimize)"),
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
            print(f"[llm-seo] Erreur : {e}", file=sys.stderr)
            sys.exit(1)
        article = p.read_text(encoding="utf-8")
        word_count = len(article.split())
        print(f"\n[llm-seo] Fichier chargé : {p} ({word_count} mots)", flush=True)
    else:
        article = args.text
        word_count = len(article.split())
        print(f"\n[llm-seo] Texte reçu ({word_count} mots)", flush=True)

    print(f"  Mot-clé : {args.keyword}", flush=True)
    if args.intent:
        print(f"  Intent  : {args.intent}", flush=True)
    mode_label = "Audit + Optimisation" if args.optimize else "Audit seul"
    print(f"  Mode    : {mode_label}", flush=True)
    print("", flush=True)

    agent = LlmSeoAgent(model=args.model)
    t_start = time.monotonic()

    # --- Exécution ---
    if args.optimize:
        print("  → Audit en cours...", flush=True)
        result: CitationSignalResult = await agent.optimize(
            article=article,
            keyword=args.keyword,
            intent=args.intent,
        )
        wc_opt = len(result.article_optimized.split())
        print(
            f"  ✓ Audit {result.citation_score}/100  →  Article optimisé ({wc_opt} mots)",
            flush=True,
        )
    else:
        print("  → Audit en cours...", flush=True)
        result = await agent.audit(
            article=article,
            keyword=args.keyword,
            intent=args.intent,
        )
        print(f"  ✓ Audit terminé : {result.citation_score}/100", flush=True)

    elapsed = time.monotonic() - t_start

    # --- Affichage terminal ---
    _print_result(result, elapsed)

    # --- Sauvegarde ---
    if args.save_dir:
        try:
            save_path = safe_write_path(args.save_dir)
        except ValueError as e:
            print(f"[llm-seo] Erreur : {e}", file=sys.stderr)
            sys.exit(1)
        save_path.mkdir(parents=True, exist_ok=True)

        report_file = save_path / "citation-audit.md"
        report_file.write_text(result.report, encoding="utf-8")
        saved = ["citation-audit.md"]

        if result.optimized and result.article_optimized:
            opt_file = save_path / "article-optimized.md"
            opt_file.write_text(result.article_optimized, encoding="utf-8")
            saved.append("article-optimized.md")

        print(f"\n  Fichiers → {save_path}/")
        print(f"  {' | '.join(saved)}")

    elif args.output:
        try:
            out = safe_write_path(args.output)
        except ValueError as e:
            print(f"[llm-seo] Erreur : {e}", file=sys.stderr)
            sys.exit(1)
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(result.report, encoding="utf-8")
        print(f"\n  Rapport sauvegardé → {out}")

    else:
        # Affichage du rapport complet si pas de save-dir
        print("\n" + "=" * 60)
        print(result.report)
        if result.optimized and result.article_optimized:
            print("\n" + "=" * 60)
            print("# Article optimisé\n")
            print(result.article_optimized)


if __name__ == "__main__":
    asyncio.run(main())
