#!/usr/bin/env python3
"""
Brain Lite — schoolsWP Content Machine simplifiée.

Workflow 5 étapes :
  1. Stratégie  (Brain : angle + sujet auto-générés)
  2. Rédaction  (Writer V1 — 1500-2500 mots)
  3. Audit      (Auditor — score /10, amélioration si < 7)
  4. Optimisation LLM (AIO-ready : réponse rapide + définitions + en résumé)
  5. Maillage   (5-12 liens internes stratégiques)

Usage :
  python -m agents.article_pipeline.brain_lite_cli \\
    --keyword "lms wordpress rentable" \\
    --intent décisionnelle

  python -m agents.article_pipeline.brain_lite_cli \\
    --keyword "fluentcrm vs activecampaign" \\
    --intent comparative \\
    --pilier crm \\
    --save-dir content/articles/crm/
"""
import argparse
import asyncio
import io
import json
import logging
import re
import sys
import time
from pathlib import Path

# Force UTF-8 stdout/stderr on Windows (CP1252 cannot encode → ✓ etc.)
if sys.stdout.encoding and sys.stdout.encoding.lower() not in ("utf-8", "utf8"):
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
if sys.stderr.encoding and sys.stderr.encoding.lower() not in ("utf-8", "utf8"):
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding="utf-8", errors="replace")

sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from agents.article_pipeline.pipeline import ArticlePipeline  # noqa: E402
from agents.base import BaseContentAgent  # noqa: E402

# ---------------------------------------------------------------------------
# Brain Lite Agent — Step 0 : stratégie éditoriale
# ---------------------------------------------------------------------------

_BRAIN_LITE_SYSTEM = """Tu es schoolsWP Brain Lite, agent de priorisation éditoriale de schoolsWP (schoolswp.com).

Ton rôle : analyser un mot-clé et produire une stratégie éditoriale JSON en 5 secondes.

Réponds UNIQUEMENT en JSON valide, sans backticks, sans commentaire.

Format :
{
  "topic": "Titre H1 optimisé SEO (question ou affirmation forte)",
  "angle": "Angle différenciant — ce que schoolsWP fait mieux ou autrement vs concurrence (1 phrase)",
  "audience": "Profil précis (ex: freelance WordPress intermédiaire qui veut monétiser)",
  "roi_ok": true,
  "roi_reasons": ["raison 1", "raison 2"]
}

Règle roi_ok = true si au moins 2 questions sur 3 = oui :
  1. Le sujet aide une décision WordPress concrète ?
  2. Il est lié à un outil stratégique (FluentCRM, Tutor LMS, WooCommerce, n8n, Yoast, Rank Math...) ?
  3. Il renforce un pilier prioritaire (SEO / LMS / CRM / Performance / Automatisation) ?

Règles schoolsWP :
- Tutoiement systématique dans les recommandations
- Voix directe, pédagogique, sans jargon
- Jamais : disruptif, game changer, scalable, révolutionnaire"""


class BrainLiteAgent(BaseContentAgent):
    name = "brain-lite"
    system_prompt = _BRAIN_LITE_SYSTEM

    async def run(  # type: ignore[override]
        self,
        keyword: str,
        intent: str,
        pilier: str = "",
    ) -> dict:
        """Retourne la stratégie éditoriale sous forme de dict."""
        user_msg = (
            f"Mot-clé : {keyword}\n"
            f"Intent SEO : {intent}\n"
            f"Pilier schoolsWP : {pilier or 'à détecter automatiquement'}"
        )
        response = await self._client.messages.create(
            model=self.model,
            max_tokens=600,
            system=self.system_prompt,
            messages=[{"role": "user", "content": user_msg}],
        )
        raw = response.content[0].text.strip()
        raw = re.sub(r"```json\s*|\s*```", "", raw).strip()
        try:
            return json.loads(raw)
        except Exception as e:
            logging.warning("[brain-lite] JSON parse error: %s — retour aux valeurs par défaut", e)
            return {
                "topic": keyword.title(),
                "angle": "Vision système et rentabilité — concret, actionnable",
                "audience": "freelance WordPress intermédiaire",
                "roi_ok": True,
                "roi_reasons": ["sujet WordPress stratégique"],
            }


# ---------------------------------------------------------------------------
# Helpers CLI
# ---------------------------------------------------------------------------

_LINE = "━" * 48


def _header(keyword: str, intent: str, pilier: str) -> None:
    print()
    print(_LINE)
    print("[brain-lite] schoolsWP Content Machine")
    print(f"  Mot-clé : {keyword}")
    print(f"  Intent  : {intent}")
    if pilier:
        print(f"  Pilier  : {pilier}")
    print("  Étapes  : Brain → Writer → Audit → LLM → Maillage")
    print(_LINE)
    print()


def _step_log(label: str, detail: str = "", done: bool = False) -> None:
    marker = "✓" if done else "→"
    suffix = f"  ({detail})" if detail else ""
    print(f"  {marker} {label}{suffix}")


# ---------------------------------------------------------------------------
# Parser
# ---------------------------------------------------------------------------

_PILIERS = ["seo", "lms", "crm", "performance", "automatisation", "ecommerce"]
_INTENTS = ["informationnelle", "comparative", "décisionnelle"]


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        prog="brain-lite",
        description="Brain Lite schoolsWP — 5 étapes, 1 article prêt à publier",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""Exemples :
  python -m agents.article_pipeline.brain_lite_cli \\
    --keyword "lms wordpress rentable" --intent décisionnelle

  python -m agents.article_pipeline.brain_lite_cli \\
    --keyword "fluentcrm avis" --intent informationnelle \\
    --pilier crm --save-dir content/articles/crm/fluent/

  python -m agents.article_pipeline.brain_lite_cli \\
    --keyword "tutor lms vs learndash" --intent comparative \\
    --pilier lms --output content/articles/comparatif-lms.md""",
    )
    p.add_argument(
        "--keyword",
        required=True,
        help="Mot-clé principal cible (ex: 'lms wordpress rentable')",
    )
    p.add_argument(
        "--intent",
        required=True,
        choices=_INTENTS,
        help="Intent SEO : informationnelle | comparative | décisionnelle",
    )
    p.add_argument(
        "--pilier",
        choices=_PILIERS,
        default="",
        help="Pilier schoolsWP (optionnel — auto-détecté si absent)",
    )
    p.add_argument(
        "--save-dir",
        default="",
        help=(
            "Dossier de sauvegarde des fichiers produits "
            "(auto : content/articles/{pilier-ou-keyword-slug}/)"
        ),
    )
    p.add_argument(
        "--output",
        default="",
        help="Fichier de sortie principal (article V3 ou V2)",
    )
    p.add_argument(
        "--model",
        default="",
        help="Modèle Claude à utiliser (défaut : env MODEL_WRITER ou claude-sonnet-4-6)",
    )
    p.add_argument(
        "--force",
        action="store_true",
        help="Forcer la production même si roi_ok=false",
    )
    return p


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

async def main() -> None:
    parser = build_parser()
    args = parser.parse_args()

    keyword = args.keyword.strip()
    intent = args.intent.strip()
    pilier = args.pilier.strip()
    model = args.model.strip() or None

    _header(keyword, intent, pilier)
    t_start = time.time()

    # ------------------------------------------------------------------
    # ÉTAPE 1 / 5 — Brain Lite : stratégie éditoriale
    # ------------------------------------------------------------------
    _step_log("Étape 1/5 — Brain (angle + sujet + ROI check)")

    brain = BrainLiteAgent(model=model)
    strategy = await brain.run(keyword=keyword, intent=intent, pilier=pilier)

    topic: str = strategy.get("topic") or keyword.title()
    angle: str = (
        strategy.get("angle")
        or "Vision système et rentabilité — concret, actionnable, sans jargon"
    )
    audience: str = strategy.get("audience") or "freelance WordPress intermédiaire"
    roi_ok: bool = bool(strategy.get("roi_ok", True))
    roi_reasons: list = strategy.get("roi_reasons") or []

    roi_label = "OK ✓" if roi_ok else "FAIBLE ⚠"
    _step_log("Étape 1/5 — Brain", f"ROI={roi_label} | topic={topic[:50]}", done=True)

    if not roi_ok and not args.force:
        print()
        print("  ⚠  ROI faible — le Brain recommande de reporter ce sujet.")
        if roi_reasons:
            print("     Raisons :")
            for r in roi_reasons:
                print(f"       - {r}")
        print()
        print("  → Utilise --force pour produire quand même.")
        print("  → Ou choisis un sujet avec plus d'impact ROI.")
        print()
        sys.exit(0)

    # ------------------------------------------------------------------
    # ÉTAPES 2-5 — Pipeline (Writer → Auditor → Editor → LLM → Links → Meta)
    # ------------------------------------------------------------------
    pipeline = ArticlePipeline(model=model)

    _STEP_LABELS: dict[str, str] = {
        "Writer":  "Étape 2/5 — Writer (V1 article)",
        "Auditor": "Étape 3/5 — Auditor (score /10)",
        "Editor":  "Étape 3/5 — Editor (amélioration si score < 7)",
        "LLM-SEO": "Étape 4/5 — LLM Optimizer (AIO-ready)",
        "Links":   "Étape 5/5 — Maillage interne",
        "Meta":    "Étape 5/5 — Méta SEO",
    }
    _prev_step: dict[str, str] = {"name": ""}

    def on_step(step_name: str, content: str) -> None:
        prev = _prev_step["name"]
        if prev:
            wc = len(content.split()) if content else 0
            detail = f"{wc} mots" if wc > 50 else ""
            _step_log(_STEP_LABELS.get(prev, prev), detail, done=True)
        label = _STEP_LABELS.get(step_name, step_name)
        _step_log(label)
        _prev_step["name"] = step_name

    result = await pipeline.run(
        topic=topic,
        keyword=keyword,
        intent=intent,
        angle=angle,
        include_serp=False,   # Brain Lite : pas de simulation SERP
        include_llm=True,     # LLM Optimizer = indispensable pour 2026
        include_ner=False,    # NER désactivé pour rester rapide
        include_links=True,   # Maillage = toujours
        include_meta=True,    # Meta SEO = toujours
        on_step=on_step,
    )

    # Ferme le dernier step
    if _prev_step["name"]:
        _step_log(_STEP_LABELS.get(_prev_step["name"], _prev_step["name"]), done=True)

    # ------------------------------------------------------------------
    # RÉSUMÉ
    # ------------------------------------------------------------------
    elapsed = round(time.time() - t_start)
    mins, secs = divmod(elapsed, 60)

    article_version = result.v3 or result.v2 or result.v1
    version_label = "V3 (LLM)" if result.v3 else "V2 (édité)" if result.v2 else "V1 (brut)"
    word_count = len(article_version.split())

    link_count = max(0, (result.internal_links or "").count("| ") - 2)

    print()
    print(_LINE)
    print(f"  Terminé en {mins}m {secs}s")
    print(f"  Score audit   : {result.score_global or '—'}/10 | {result.diagnostic or '—'}")
    if result.score_llm_global:
        print(f"  Score LLM-SEO : {result.score_llm_global}/10")
    if link_count > 0:
        print(f"  Liens internes: {link_count} liens recommandés")
    print(f"  Article       : {word_count} mots ({version_label})")
    print(_LINE)

    # ------------------------------------------------------------------
    # SAUVEGARDE
    # ------------------------------------------------------------------
    if args.save_dir:
        save_dir = Path(args.save_dir)
    else:
        slug = (pilier or re.sub(r"[^a-z0-9-]", "-", keyword.lower()))[:40].strip("-")
        save_dir = Path("articles") / slug

    save_dir.mkdir(parents=True, exist_ok=True)
    saved: list[str] = []

    def _save(name: str, content: str) -> None:
        if content:
            fp = save_dir / name
            fp.write_text(content, encoding="utf-8")
            saved.append(str(fp))

    _save("v1.md", result.v1)
    _save("audit.md", result.audit)
    _save("v2.md", result.v2)
    if result.v3:
        _save("v3.md", result.v3)
    if result.internal_links:
        _save("links.md", result.internal_links)
    if result.meta:
        _save("meta.md", result.meta)

    # Fichier de sortie principal
    if args.output:
        out = Path(args.output)
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(article_version, encoding="utf-8")
        main_file = out
    else:
        main_file = save_dir / ("v3.md" if result.v3 else "v2.md")

    print()
    print(f"  Article principal : {main_file}")
    print(f"  Fichiers produits : {len(saved)} fichiers dans {save_dir}/")
    print()

    # ------------------------------------------------------------------
    # RÉCAP STRATÉGIQUE
    # ------------------------------------------------------------------
    print("  ─── Stratégie Brain Lite ─────────────────")
    print(f"  Sujet    : {topic}")
    print(f"  Angle    : {angle[:80]}")
    print(f"  Audience : {audience}")
    print()


if __name__ == "__main__":
    asyncio.run(main())
