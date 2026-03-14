#!/usr/bin/env python3
"""
CLI — Pipeline article schoolsWP (7 agents max)

Usage :
  python -m agents.article_pipeline.cli --topic "..." --keyword "..." --intent comparative --angle "..."
  python -m agents.article_pipeline.cli ... --save-dir content/articles/cache-wp/
  python -m agents.article_pipeline.cli ... --include-serp --skip-ner --output article.md

Fichiers produits si --save-dir :
  [save-dir]/v1.md        Article brut (Agent 1)
  [save-dir]/audit.md     Rapport d'audit (Agent 2)
  [save-dir]/serp-sim.md  Simulation SERP Top 5 (Agent 2b — si --include-serp)
  [save-dir]/serp-comp.md Comparaison V1 vs SERP (Agent 2c — si --include-serp)
  [save-dir]/v2.md        Article édité (Agent 3)
  [save-dir]/v3.md        Article LLM-optimisé (Agent 4 — sauf --skip-llm)
  [save-dir]/ner.json     Graphe sémantique NER (Agent 4b — sauf --skip-ner)
  [save-dir]/v4.md        Article enrichi NER (Agent 4c — sauf --skip-ner)
  [save-dir]/links.md     Plan maillage interne (Agent 4d — sauf --skip-links)
  [save-dir]/meta.md      Méta SEO + FAQ schema (Agent 5 — sauf --skip-meta)
"""
import argparse
import asyncio
import io
import sys
import time
from pathlib import Path

# Force UTF-8 stdout/stderr on Windows (CP1252 can't encode → ✓ etc.)
if sys.stdout.encoding and sys.stdout.encoding.lower() not in ("utf-8", "utf8"):
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
if sys.stderr.encoding and sys.stderr.encoding.lower() not in ("utf-8", "utf8"):
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding="utf-8", errors="replace")

sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from agents.article_pipeline.pipeline import ArticlePipeline

_INTENTS = ["informationnelle", "comparative", "décisionnelle"]


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="article-pipeline",
        description=(
            "Pipeline article schoolsWP — "
            "Writer → Auditor → [SERP] → Editor → LLM-SEO → Meta"
        ),
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=(
            "Exemples :\n"
            "  # Pipeline complet (5 agents), sortie terminale\n"
            "  python -m agents.article_pipeline.cli \\\n"
            '    --topic "Choisir un hébergeur WordPress" \\\n'
            '    --keyword "meilleur hébergeur WordPress" \\\n'
            "    --intent comparative \\\n"
            '    --angle "focus coût réel vs performance, sans jargon"\n\n'
            "  # Avec simulation SERP + sauvegarde des fichiers\n"
            "  python -m agents.article_pipeline.cli \\\n"
            '    --topic "Plugin de cache WordPress" \\\n'
            '    --keyword "plugin cache WordPress gratuit" \\\n'
            "    --intent comparative \\\n"
            '    --angle "comparatif pour hébergement mutualisé" \\\n'
            "    --include-serp --save-dir content/articles/cache-wp/\n\n"
            "  # Sans LLM-SEO ni Meta + sortie fichier unique\n"
            "  python -m agents.article_pipeline.cli \\\n"
            '    --topic "..." --keyword "..." --intent informationnelle \\\n'
            '    --angle "..." --skip-llm --skip-meta --output article.md'
        ),
    )
    parser.add_argument("--topic", required=True, metavar="SUJET")
    parser.add_argument("--keyword", required=True, metavar="MOT_CLÉ")
    parser.add_argument(
        "--intent",
        required=True,
        choices=_INTENTS,
        metavar="INTENT",
        help=f"{' | '.join(_INTENTS)}",
    )
    parser.add_argument(
        "--angle",
        required=True,
        metavar="ANGLE",
        help="Angle différenciant (ex: 'focus coût réel, sans jargon technique')",
    )
    parser.add_argument(
        "--save-dir",
        metavar="DOSSIER",
        default=None,
        help="Dossier où sauvegarder les fichiers intermédiaires et finaux",
    )
    parser.add_argument(
        "--output",
        metavar="FICHIER",
        default=None,
        help="Fichier de sortie pour l'article final uniquement (si pas --save-dir)",
    )
    parser.add_argument(
        "--include-serp",
        action="store_true",
        default=False,
        help="Activer le flux SERP étendu (Agent 2b simulation + Agent 2c comparaison)",
    )
    parser.add_argument(
        "--skip-llm",
        action="store_true",
        default=False,
        help="Ne pas exécuter Agent 4 LLM-SEO (optimisation citations IA → V3)",
    )
    parser.add_argument(
        "--skip-ner",
        action="store_true",
        default=False,
        help="Ne pas exécuter Agents 4b/4c NER (graphe sémantique → V4 enrichie)",
    )
    parser.add_argument(
        "--skip-links",
        action="store_true",
        default=False,
        help="Ne pas exécuter Agent 4d Link-Strategist (plan maillage interne)",
    )
    parser.add_argument(
        "--skip-meta",
        action="store_true",
        default=False,
        help="Ne pas exécuter Agent 5 (extraction méta SEO)",
    )
    parser.add_argument(
        "--model",
        default=None,
        metavar="MODEL",
        help="Modèle Claude (défaut : $MODEL_WRITER ou claude-sonnet-4-6)",
    )
    return parser


def _step_log(step: str, content: str) -> None:
    word_count = len(content.split())
    labels = {
        "writer": f"Agent 1 (Writer)        → V1 produite          ({word_count} mots)",
        "auditor": f"Agent 2 (Auditor)       → Audit prêt           ({word_count} mots)",
        "serp_simulator": f"Agent 2b (SERP-Sim)     → Simulation SERP      ({word_count} mots)",
        "serp_comparator": f"Agent 2c (SERP-Comp)    → Comparaison prête    ({word_count} mots)",
        "editor": f"Agent 3 (Editor)        → V2 finale produite   ({word_count} mots)",
        "llm_optimizer": f"Agent 4  (LLM-SEO)      → V3 LLM-ready         ({word_count} mots)",
        "ner_analyzer": f"Agent 4b (NER)          → Graphe sémantique    ({word_count} tokens JSON)",
        "semantic_enricher": f"Agent 4c (Sem-Enrich)   → V4 enrichie          ({word_count} mots)",
        "internal_link_strategist": f"Agent 4d (Links)        → Plan maillage prêt   ({word_count} mots)",
        "meta_extractor": f"Agent 5  (Meta)         → Méta extraite        ({word_count} mots)",
    }
    print(f"  ✓ {labels.get(step, step)}", flush=True)


async def main() -> None:
    parser = build_parser()
    args = parser.parse_args()

    include_serp = args.include_serp
    include_llm = not args.skip_llm
    include_ner = not args.skip_ner
    include_links = not args.skip_links
    include_meta = not args.skip_meta

    # Construire la liste des étapes pour l'affichage
    steps_display = ["Writer", "Auditor"]
    if include_serp:
        steps_display += ["SERP-Sim", "SERP-Comp"]
    steps_display.append("Editor")
    if include_llm:
        steps_display.append("LLM-SEO")
    if include_ner:
        steps_display += ["NER", "Sem-Enrich"]
    if include_links:
        steps_display.append("Links")
    if include_meta:
        steps_display.append("Meta")

    pipeline = ArticlePipeline(model=args.model)

    print("\n[article-pipeline] Démarrage...", flush=True)
    print(f"  Sujet   : {args.topic}", flush=True)
    print(f"  Mot-clé : {args.keyword}", flush=True)
    print(f"  Intent  : {args.intent}", flush=True)
    print(f"  Angle   : {args.angle}", flush=True)
    print(f"  Étapes  : {' → '.join(steps_display)}\n", flush=True)

    t_start = time.monotonic()

    result = await pipeline.run(
        topic=args.topic,
        keyword=args.keyword,
        intent=args.intent,
        angle=args.angle,
        include_meta=include_meta,
        include_serp=include_serp,
        include_llm=include_llm,
        include_ner=include_ner,
        include_links=include_links,
        on_step=_step_log,
    )

    elapsed = time.monotonic() - t_start
    print(f"\n  Terminé en {elapsed:.1f}s", flush=True)

    # Résumé des scores
    if result.score_global:
        print(
            f"  Audit    → Score: {result.score_global} | {result.diagnostic or '?'}",
            flush=True,
        )
    if result.score_serp_global:
        print(f"  SERP     → Score: {result.score_serp_global}", flush=True)
    if result.score_llm_global:
        print(f"  LLM-SEO  → Score: {result.score_llm_global}", flush=True)
    if result.score_ner_coherence:
        print(f"  NER      → Cohérence sémantique: {result.score_ner_coherence}", flush=True)

    final_article = result.v4 if result.v4 else (result.v3 if result.v3 else result.v2)

    # Sauvegarde
    if args.save_dir:
        save_path = Path(args.save_dir)
        save_path.mkdir(parents=True, exist_ok=True)
        (save_path / "v1.md").write_text(result.v1, encoding="utf-8")
        (save_path / "audit.md").write_text(result.audit, encoding="utf-8")
        if result.serp_simulation:
            (save_path / "serp-sim.md").write_text(result.serp_simulation, encoding="utf-8")
        if result.serp_comparison:
            (save_path / "serp-comp.md").write_text(result.serp_comparison, encoding="utf-8")
        (save_path / "v2.md").write_text(result.v2, encoding="utf-8")
        if result.v3:
            (save_path / "v3.md").write_text(result.v3, encoding="utf-8")
        if result.ner_json:
            (save_path / "ner.json").write_text(result.ner_json, encoding="utf-8")
        if result.v4:
            (save_path / "v4.md").write_text(result.v4, encoding="utf-8")
        if result.internal_links:
            (save_path / "links.md").write_text(result.internal_links, encoding="utf-8")
        if result.meta:
            (save_path / "meta.md").write_text(result.meta, encoding="utf-8")

        saved_files = ["v1.md", "audit.md"]
        if result.serp_simulation:
            saved_files += ["serp-sim.md", "serp-comp.md"]
        saved_files.append("v2.md")
        if result.v3:
            saved_files.append("v3.md")
        if result.ner_json:
            saved_files += ["ner.json", "v4.md"]
        if result.internal_links:
            saved_files.append("links.md")
        if result.meta:
            saved_files.append("meta.md")

        print(f"\n[article-pipeline] Fichiers sauvegardés → {save_path}/")
        print(f"  {' | '.join(saved_files)}")
    elif args.output:
        output_path = Path(args.output)
        output_path.parent.mkdir(parents=True, exist_ok=True)
        content = final_article
        if result.meta:
            content += f"\n\n---\n\n{result.meta}"
        output_path.write_text(content, encoding="utf-8")
        print(f"\n[article-pipeline] Article sauvegardé → {output_path}")
    else:
        # Sortie terminale : article final + méta
        print("\n" + "=" * 70)
        print(final_article)
        if result.meta:
            print("\n" + "=" * 70)
            print(result.meta)


if __name__ == "__main__":
    asyncio.run(main())
