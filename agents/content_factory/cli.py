#!/usr/bin/env python3
"""
schoolsWP Brain — Content Factory CLI

Un seul agent. Une seule commande. Un actif stratégique complet.

Deux modes :

  MODE GÉNÉRATION (depuis mot-clé) :
    Brain → Article → Audit 4 modules → Cluster plan
    ~4-8 min selon options

  MODE AUDIT (article existant) :
    Audit 4 modules en parallèle → Cluster plan
    ~90-120s

Usage :
  # Génération complète depuis mot-clé
  python -m agents.content_factory.cli \\
    --keyword "formation en ligne rentable wordpress" \\
    --intent décisionnelle \\
    --pillar LMS \\
    --save-dir articles/lms-factory/

  # Audit d'un article existant
  python -m agents.content_factory.cli \\
    --file articles/lms-pilier/v3.md \\
    --keyword "formation en ligne rentable wordpress" \\
    --intent décisionnelle \\
    --pillar LMS \\
    --save-dir articles/lms-pilier/

  # Génération + NER + SERP (pipeline complet)
  python -m agents.content_factory.cli \\
    --keyword "fluentcrm vs activecampaign" \\
    --intent comparative \\
    --pillar CRM \\
    --include-serp --include-ner \\
    --save-dir articles/crm-factory/

Publish Score (score composite /100) :
  ≥ 90  ✅  Publication immédiate
  80–89 🟡  1–2 optimisations ciblées
  70–79 🟠  Travail requis sur blocs faibles
  < 70  🔴  Révision substantielle
"""
import argparse
import asyncio
import io
import json
import re
import sys
import time
from pathlib import Path

# Force UTF-8 sur Windows
if hasattr(sys.stdout, "buffer") and sys.stdout.encoding.lower() not in ("utf-8", "utf8"):
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
if hasattr(sys.stderr, "buffer") and sys.stderr.encoding.lower() not in ("utf-8", "utf8"):
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding="utf-8", errors="replace")

sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from agents.content_factory.agent import ContentFactoryAgent, ContentFactoryResult

_INTENTS = ["informationnelle", "comparative", "décisionnelle", "transactionnelle"]
_PILLARS = ["SEO", "LMS", "CRM", "Performance", "Automatisation"]
_OBJECTIVES = ["email", "affiliation", "formation", "offre"]

_LINE = "━" * 62
_SEP = "─" * 62
_STEP_LABELS: dict[str, str] = {
    "Brain":   "Étape 1 — Brain (stratégie + ROI check)",
    "Writer":  "Étape 2 — Writer (article V1)",
    "Auditor": "Étape 3 — Auditor (score /10)",
    "Editor":  "Étape 3 — Editor (amélioration ciblée)",
    "LLM-SEO": "Étape 4 — LLM-SEO (AIO-ready V3)",
    "NER":     "Étape 4b — NER Analyzer (entités JSON)",
    "NER-Enrich": "Étape 4c — Enrichisseur sémantique (V4)",
    "Links":   "Étape 5 — Maillage interne",
    "Meta":    "Étape 5 — Méta SEO",
    "Audit":   "Étape 6 — Audit 4 modules en parallèle",
    "Cluster": "Étape 7 — Plan cluster sémantique",
}
_prev_step: dict[str, str] = {"name": "", "t": 0.0}


def _on_step(step_name: str, content: str = "") -> None:
    prev = _prev_step["name"]
    now = time.monotonic()
    if prev:
        elapsed = now - _prev_step["t"]
        wc = len(content.split()) if content and len(content) > 50 else 0
        detail = f"{wc} mots, {elapsed:.0f}s" if wc else f"{elapsed:.0f}s"
        label = _STEP_LABELS.get(prev, prev)
        print(f"  ✓ {label}  ({detail})", flush=True)
    label = _STEP_LABELS.get(step_name, step_name)
    print(f"  → {label}...", flush=True)
    _prev_step["name"] = step_name
    _prev_step["t"] = now


def _close_last_step() -> None:
    if _prev_step["name"]:
        elapsed = time.monotonic() - _prev_step["t"]
        label = _STEP_LABELS.get(_prev_step["name"], _prev_step["name"])
        print(f"  ✓ {label}  ({elapsed:.0f}s)", flush=True)
        _prev_step["name"] = ""


def _print_result(result: ContentFactoryResult, elapsed: float, mode: str) -> None:
    print("\n" + _LINE)
    print("  schoolsWP Brain — Résultat")
    print(_LINE)

    if result.topic:
        print(f"  Sujet    : {result.topic[:70]}")
    if result.angle:
        print(f"  Angle    : {result.angle[:70]}")
    print(f"  Article  : {result.word_count} mots ({result.article_version_label})")
    print(_SEP)

    if result.publish:
        pub = result.publish
        scores = pub.scores_summary()
        bar = lambda s: "█" * round(s / 10) + "░" * (10 - round(s / 10))
        print(f"  Publish Score    {bar(pub.publish_score)} {pub.publish_score}/100  {pub.publish_emoji}")
        print(f"  Diagnostic       {pub.publish_diagnostic}")
        print(f"  Bloc le + faible : {pub.weakest_module}")
        print(_SEP)
        print("  MODULES")
        for name, score in scores.items():
            print(f"  {name:<22} {bar(score)} {score}/100")
        print(_SEP)

        # Premières actions du plan
        if pub.action_plan:
            action_lines = [
                l.strip() for l in pub.action_plan.splitlines()
                if l.strip() and l.strip()[0].isdigit()
            ]
            if action_lines:
                print("  PLAN D'ACTION")
                for l in action_lines[:5]:
                    print(f"    {l}")
        print(_SEP)

    if result.cluster_plan:
        cluster_lines = [
            l for l in result.cluster_plan.splitlines()
            if l.strip() and (l.startswith("#") or l.startswith("**") or "Satellite" in l)
        ]
        if cluster_lines:
            print("  CLUSTER")
            for l in cluster_lines[:6]:
                print(f"    {l.strip()}")
        print(_SEP)

    mins, secs = divmod(int(elapsed), 60)
    print(f"  Mode : {mode} | Durée : {mins}m {secs}s")
    print(_LINE)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="brain",
        description=(
            "schoolsWP Brain — Content Factory.\n"
            "Mode génération : keyword → article → audit → cluster.\n"
            "Mode audit : article existant → audit → cluster."
        ),
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=(
            "Exemples :\n\n"
            "  # Génération complète\n"
            "  python -m agents.content_factory.cli \\\n"
            '    --keyword "lms wordpress rentable" --intent décisionnelle \\\n'
            "    --pillar LMS --save-dir articles/lms-factory/\n\n"
            "  # Audit article existant\n"
            "  python -m agents.content_factory.cli \\\n"
            '    --file articles/lms-pilier/v3.md \\\n'
            '    --keyword "lms wordpress rentable" --intent décisionnelle \\\n'
            "    --pillar LMS --save-dir articles/lms-pilier/\n\n"
            "  # Génération + NER + SERP (pipeline complet)\n"
            "  python -m agents.content_factory.cli \\\n"
            '    --keyword "fluentcrm vs activecampaign" --intent comparative \\\n'
            "    --pillar CRM --include-serp --include-ner --save-dir articles/crm/"
        ),
    )

    # --- Source : génération depuis keyword OU audit d'un fichier ---
    source = parser.add_mutually_exclusive_group()
    source.add_argument("--keyword", metavar="MOT_CLÉ",
                        help="Mot-clé principal → mode génération")
    source.add_argument("--file", metavar="FICHIER",
                        help="Fichier markdown existant → mode audit seul")

    # Keyword + intent (mode génération OU audit avec fichier)
    parser.add_argument("--intent", default=None, choices=_INTENTS, metavar="INTENT",
                        help=f"Intention : {' | '.join(_INTENTS)}")
    # --keyword-for-audit : permet de fournir keyword en mode fichier
    parser.add_argument("--kw", "--keyword-audit", dest="kw_audit", metavar="MOT_CLÉ",
                        help="Mot-clé (obligatoire en mode --file)")

    parser.add_argument("--pillar", default=None, metavar="PILIER",
                        help=f"Pilier schoolsWP : {' | '.join(_PILLARS)}")
    parser.add_argument("--objective", default=None, choices=_OBJECTIVES, metavar="OBJECTIF",
                        help=f"Objectif business : {' | '.join(_OBJECTIVES)}")

    # Options pipeline (mode génération uniquement)
    parser.add_argument("--include-serp", action="store_true",
                        help="Simulation SERP Top 5 (mode génération, +~2 min)")
    parser.add_argument("--include-ner", action="store_true",
                        help="Enrichissement NER sémantique V4 (mode génération, +~1-2 min)")
    parser.add_argument("--no-links", action="store_true",
                        help="Désactive le maillage interne (mode génération)")
    parser.add_argument("--no-cluster", action="store_true",
                        help="Désactive le plan cluster")
    parser.add_argument("--force", action="store_true",
                        help="Forcer la génération même si ROI faible")

    parser.add_argument("--save-dir", default=None, metavar="DOSSIER",
                        help="Dossier de sauvegarde (auto-généré si absent)")
    parser.add_argument("--model", default=None, metavar="MODEL",
                        help="Modèle Claude (défaut : claude-sonnet-4-6)")

    return parser


def _auto_save_dir(keyword: str, pillar: str | None) -> Path:
    slug_base = pillar.lower() if pillar else keyword.lower()
    slug = re.sub(r"[^a-z0-9-]", "-", slug_base)[:40].strip("-")
    return Path("articles") / slug


async def main() -> None:
    parser = build_parser()
    args = parser.parse_args()

    # --- Validation des arguments ---
    if args.file and not (args.intent or args.kw_audit):
        # Mode fichier : keyword requis (via --kw ou dans le fichier)
        # On autorise sans intent (optionnel)
        pass
    if not args.file and not args.keyword:
        parser.error("Spécifie --keyword (génération) ou --file (audit)")

    # --- Résolution du keyword et de l'intent en mode fichier ---
    if args.file:
        keyword = args.kw_audit or args.keyword or ""
        if not keyword:
            parser.error("En mode --file, spécifie le mot-clé via --kw 'mot-clé'")
        intent = args.intent
        article_content = Path(args.file).read_text(encoding="utf-8")
        wc = len(article_content.split())
        mode_label = "Audit seul"
        print(f"\n[brain] Fichier chargé : {args.file} ({wc} mots)", flush=True)
    else:
        keyword = args.keyword
        intent = args.intent or "décisionnelle"
        article_content = None
        mode_label = "Génération + Audit"
        print(f"\n[brain] schoolsWP Content Factory", flush=True)
        print(f"  Mot-clé : {keyword}", flush=True)
        print(f"  Intent  : {intent}", flush=True)

    if args.pillar:
        print(f"  Pilier  : {args.pillar}", flush=True)
    if args.objective:
        print(f"  Objectif: {args.objective}", flush=True)
    cluster_label = "Non" if args.no_cluster else "Oui"
    print(f"  Cluster : {cluster_label}", flush=True)
    print("", flush=True)

    agent = ContentFactoryAgent(model=args.model)
    t_start = time.monotonic()

    if article_content is not None:
        # ── Mode Audit ──────────────────────────────────────────────
        # Les steps sont gérés par le callback dans agent.audit_only()
        result: ContentFactoryResult = await agent.audit_only(
            article=article_content,
            keyword=keyword,
            intent=intent,
            pillar=args.pillar,
            objective=args.objective,
            expand_cluster=not args.no_cluster,
            on_step=_on_step,
        )
        _close_last_step()

    else:
        # ── Mode Génération ─────────────────────────────────────────
        result = await agent.generate_and_audit(
            keyword=keyword,
            intent=intent,
            pillar=args.pillar,
            objective=args.objective,
            include_serp=args.include_serp,
            include_ner=args.include_ner,
            include_links=not args.no_links,
            expand_cluster=not args.no_cluster,
            force=args.force,
            on_step=_on_step,
        )
        _close_last_step()

        if not result.roi_ok and not args.force:
            print("\n  ⚠  ROI faible — le Brain recommande de reporter ce sujet.")
            print("  → Utilise --force pour produire quand même.")
            print()
            sys.exit(0)

    elapsed = time.monotonic() - t_start
    _print_result(result, elapsed, mode_label)

    # ── Sauvegarde ──────────────────────────────────────────────────
    if args.save_dir:
        save_path = Path(args.save_dir)
    else:
        save_path = _auto_save_dir(keyword, args.pillar)

    save_path.mkdir(parents=True, exist_ok=True)
    saved: list[str] = []

    def _save(name: str, content: str) -> None:
        if content:
            f = save_path / name
            f.write_text(content, encoding="utf-8")
            saved.append(name)

    # Rapport maître
    _save("brain-report.md", result.factory_report)

    # Pipeline (mode génération)
    if result.pipeline:
        p = result.pipeline
        _save("v1.md", p.v1)
        _save("v2.md", p.v2)
        if p.v3:
            _save("v3.md", p.v3)
        if p.v4:
            _save("v4.md", p.v4)
        if p.internal_links:
            _save("links.md", p.internal_links)
        if p.meta:
            _save("meta.md", p.meta)
        if p.audit:
            _save("pipeline-audit.md", p.audit)
        # Stratégie JSON
        if result.strategy_raw:
            (save_path / "strategy.json").write_text(
                json.dumps(result.strategy_raw, ensure_ascii=False, indent=2),
                encoding="utf-8",
            )
            saved.append("strategy.json")

    # Audits 4 modules
    if result.publish:
        pub = result.publish
        _save("publish-dashboard.md", pub.dashboard)
        _save("seo-audit.md", pub.seo_result.report)
        _save("citation-audit.md", pub.llm_result.report)
        _save("conversion-audit.md", pub.conversion_result.report)
        _save("topical-audit.md", pub.authority_result.report)

    # Cluster
    _save("cluster-plan.md", result.cluster_plan)

    print(f"\n  Fichiers → {save_path}/")
    for f in saved:
        wc = len((save_path / f).read_text(encoding="utf-8").split()) if f.endswith(".md") else "—"
        print(f"  • {f:<30} {str(wc) + ' mots' if isinstance(wc, int) else ''}")

    print()


if __name__ == "__main__":
    asyncio.run(main())
