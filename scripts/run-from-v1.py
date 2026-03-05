#!/usr/bin/env python3
"""
Runner pipeline schoolsWP — à partir d'un V1 existant.

Lance les agents 2 → 5 sur un article V1 déjà rédigé :
  Agent 2  (Auditor)       → Audit + score /10
  Agent 3  (Editor)        → V2 (si score < 7)
  Agent 4  (LLM-SEO)       → V3 AIO-ready
  Agent 4d (Links)         → Maillage interne
  Agent 5  (Meta)          → Méta SEO

Usage :
  python scripts/run-from-v1.py \\
    --v1 articles/lms-architecture-signature/v1.md \\
    --keyword "lms wordpress rentable" \\
    --intent décisionnelle \\
    --save-dir articles/lms-architecture-signature/
"""
import argparse
import asyncio
import io
import sys
import time
from pathlib import Path

# Force UTF-8 on Windows
if sys.stdout.encoding and sys.stdout.encoding.lower() not in ("utf-8", "utf8"):
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
if sys.stderr.encoding and sys.stderr.encoding.lower() not in ("utf-8", "utf8"):
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding="utf-8", errors="replace")

sys.path.insert(0, str(Path(__file__).parent.parent))

from agents.article_pipeline.auditor import PipelineAuditorAgent
from agents.article_pipeline.editor import PipelineEditorAgent
from agents.article_pipeline.llm_optimizer import LlmOptimizerAgent
from agents.article_pipeline.internal_link_strategist import InternalLinkStrategistAgent
from agents.article_pipeline.meta_extractor import PipelineMetaExtractorAgent
from agents.article_pipeline.pipeline import PipelineResult

_LINE = "━" * 50


def _step(label: str, detail: str = "", done: bool = False) -> None:
    marker = "✓" if done else "→"
    suffix = f"  ({detail})" if detail else ""
    print(f"  {marker} {label}{suffix}")


def _parse_score(audit_text: str) -> str:
    """Extrait le score global (MOYENNE GLOBALE) depuis le rapport d'audit."""
    import re
    # Priorité : MOYENNE GLOBALE (score agrégé), pas le premier critère individuel
    patterns = [
        r"\*\*MOYENNE GLOBALE\s*[:\|]\s*(\d+(?:\.\d+)?)/10\*\*",
        r"MOYENNE GLOBALE\s*[:\|]\s*(\d+(?:\.\d+)?)/10",
        r"\*\*Score global\*\*\s*[:\|]\s*(\d+(?:\.\d+)?)/10",
        r"Score global\s*[:\|]\s*(\d+(?:\.\d+)?)/10",
        r"\|\s*Score global\s*\|\s*\*?\*?(\d+(?:\.\d+)?)/10",
        r"(\d+(?:\.\d+)?)/10",  # fallback : première occurrence
    ]
    for p in patterns:
        m = re.search(p, audit_text, re.IGNORECASE)
        if m:
            return m.group(1)
    return "?"


def _parse_diagnostic(audit_text: str) -> str:
    """Extrait le diagnostic depuis le rapport d'audit."""
    import re
    for label in ["RÉÉCRITURE MAJEURE", "AMÉLIORATION STRATÉGIQUE", "VALIDÉ"]:
        if label in audit_text.upper():
            return label
    m = re.search(r"(réécriture|amélioration|validé)", audit_text, re.IGNORECASE)
    return m.group(1).upper() if m else "—"


async def run(
    v1_text: str,
    keyword: str,
    intent: str,
    topic: str,
    angle: str,
    save_dir: Path,
    model: str | None = None,
) -> PipelineResult:
    result = PipelineResult(
        topic=topic,
        keyword=keyword,
        intent=intent,
        angle=angle,
        v1=v1_text,
    )

    # --- Agent 2 : Auditor ---
    _step("Agent 2 — Auditor (score /10)")
    auditor = PipelineAuditorAgent(model=model)
    result.audit = await auditor.run(
        article_v1=v1_text,
        keyword=keyword,
        intent=intent,
    )
    score_raw = _parse_score(result.audit)
    diagnostic = _parse_diagnostic(result.audit)
    result.score_global = score_raw
    result.diagnostic = diagnostic
    wc_audit = len(result.audit.split())
    _step("Agent 2 — Auditor", f"score={score_raw}/10 | {diagnostic} | {wc_audit} mots", done=True)

    # Sauvegarde intermédiaire
    (save_dir / "audit.md").write_text(result.audit, encoding="utf-8")

    # --- Agent 3 : Editor (conditionnel) ---
    try:
        score_val = float(score_raw)
    except ValueError:
        score_val = 7.0

    if score_val < 7.0:
        _step(f"Agent 3 — Editor (amélioration — score {score_raw} < 7)")
        editor = PipelineEditorAgent(model=model)
        result.v2 = await editor.run(
            article_v1=v1_text,
            audit_report=result.audit,
            keyword=keyword,
            diagnostic=diagnostic,
        )
        wc_v2 = len(result.v2.split())
        _step("Agent 3 — Editor", f"V2 = {wc_v2} mots", done=True)
        (save_dir / "v2.md").write_text(result.v2, encoding="utf-8")
        working_version = result.v2
    else:
        _step(f"Agent 3 — Editor", f"score {score_raw} ≥ 7 → V1 conservé", done=True)
        result.v2 = v1_text
        working_version = v1_text

    # --- Agent 4 : LLM Optimizer ---
    _step("Agent 4 — LLM Optimizer (AIO-ready)")
    llm_optimizer = LlmOptimizerAgent(model=model)
    result.v3 = await llm_optimizer.run(
        article_v2=working_version,
        keyword=keyword,
    )
    wc_v3 = len(result.v3.split())
    _step("Agent 4 — LLM Optimizer", f"V3 = {wc_v3} mots", done=True)
    (save_dir / "v3.md").write_text(result.v3, encoding="utf-8")

    # --- Agent 4d : Internal Links ---
    _step("Agent 4d — Internal Links (maillage stratégique)")
    link_strat = InternalLinkStrategistAgent(model=model)
    result.internal_links = await link_strat.run(
        article=result.v3,
        keyword=keyword,
    )
    link_count = max(0, result.internal_links.count("| ") - 2)
    _step("Agent 4d — Internal Links", f"{link_count} liens recommandés", done=True)
    (save_dir / "links.md").write_text(result.internal_links, encoding="utf-8")

    # --- Agent 5 : Meta ---
    _step("Agent 5 — Meta SEO")
    meta = PipelineMetaExtractorAgent(model=model)
    result.meta = await meta.run(
        article_v2=result.v3,
        keyword=keyword,
    )
    _step("Agent 5 — Meta SEO", "title + description + FAQ schema", done=True)
    (save_dir / "meta.md").write_text(result.meta, encoding="utf-8")

    result.steps_completed = ["V1 (manuel)", "Auditor", "Editor", "LLM-SEO", "Links", "Meta"]
    return result


async def main() -> None:
    p = argparse.ArgumentParser(
        prog="run-from-v1",
        description="Pipeline agents 2→5 sur un V1 existant",
    )
    p.add_argument("--v1", required=True, help="Chemin vers le fichier V1.md")
    p.add_argument("--keyword", default="lms wordpress rentable", help="Mot-clé principal")
    p.add_argument("--intent", default="décisionnelle", help="Intent SEO")
    p.add_argument("--topic", default="Architecture complète d'un LMS WordPress rentable")
    p.add_argument("--angle", default="Vision système : Tutor LMS + WooCommerce + FluentCRM — architecture rentabilité")
    p.add_argument("--save-dir", default="", help="Dossier de sauvegarde (défaut : même dossier que --v1)")
    p.add_argument("--model", default="", help="Modèle Claude")
    args = p.parse_args()

    v1_path = Path(args.v1)
    if not v1_path.exists():
        print(f"  ERREUR : fichier V1 introuvable : {v1_path}")
        sys.exit(1)

    v1_text = v1_path.read_text(encoding="utf-8")
    save_dir = Path(args.save_dir) if args.save_dir else v1_path.parent
    save_dir.mkdir(parents=True, exist_ok=True)

    print()
    print(_LINE)
    print("[run-from-v1] Pipeline agents 2 → 5")
    print(f"  V1       : {v1_path}  ({len(v1_text.split())} mots)")
    print(f"  Mot-clé  : {args.keyword}")
    print(f"  Intent   : {args.intent}")
    print(f"  Save-dir : {save_dir}/")
    print(f"  Étapes   : Auditor → Editor → LLM → Links → Meta")
    print(_LINE)
    print()

    t_start = time.time()

    result = await run(
        v1_text=v1_text,
        keyword=args.keyword,
        intent=args.intent,
        topic=args.topic,
        angle=args.angle,
        save_dir=save_dir,
        model=args.model or None,
    )

    elapsed = round(time.time() - t_start)
    mins, secs = divmod(elapsed, 60)

    article = result.v3 or result.v2
    wc = len(article.split())

    print()
    print(_LINE)
    print(f"  Terminé en {mins}m {secs}s")
    print(f"  Score audit  : {result.score_global}/10 | {result.diagnostic}")
    lc = max(0, (result.internal_links or "").count("| ") - 2)
    print(f"  Liens        : {lc} liens recommandés")
    print(f"  Article      : {wc} mots (V{'3' if result.v3 else '2'})")
    print(_LINE)
    print()
    print(f"  Fichiers dans {save_dir}/")
    for f in ["v1.md", "audit.md", "v2.md", "v3.md", "links.md", "meta.md"]:
        fp = save_dir / f
        if fp.exists():
            print(f"    ✓ {f}  ({len(fp.read_text(encoding='utf-8').split())} mots)")
    print()


if __name__ == "__main__":
    asyncio.run(main())
