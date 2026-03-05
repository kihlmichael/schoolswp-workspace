#!/usr/bin/env python3
"""
schoolsWP Brain — Version API Compact

Single LLM call (~30s). Maximum intelligence, minimum tokens.
Compatible OpenAI API / Claude API / Gemini API / n8n.

Contrairement au ContentFactoryAgent (11-14 appels, 4-8 min),
la version compact produit tout en UN appel optimisé.

Usage programmatique :
    agent = CompactBrainAgent()
    result = await agent.run(
        keyword="tutor lms vs learndash",
        intent="comparative",
    )
    print(result.article)
    print(result.composite_score)   # moyenne SEO + Conversion + Autorité

Usage CLI :
    python -m agents.content_factory.brain_compact \\
      --keyword "tutor lms vs learndash" \\
      --intent comparative \\
      --pillar LMS \\
      --save-dir articles/lms-compact/

Utilisation n8n (HTTP Request → Claude API) :
    Voir docs/brain-api-compact.md pour le body JSON complet.
"""
from __future__ import annotations

import argparse
import asyncio
import io
import re
import sys
import time
from dataclasses import dataclass, field
from pathlib import Path

# Force UTF-8 sur Windows
if hasattr(sys.stdout, "buffer") and sys.stdout.encoding.lower() not in ("utf-8", "utf8"):
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
if hasattr(sys.stderr, "buffer") and sys.stderr.encoding.lower() not in ("utf-8", "utf8"):
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding="utf-8", errors="replace")

sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from agents.base import BaseContentAgent

# ---------------------------------------------------------------------------
# System Prompt — compact, API-ready
# ---------------------------------------------------------------------------
# Note : tutoiement systématique ajouté (règle branding schoolsWP)
# Note : mots interdits ajoutés dans les règles

COMPACT_SYSTEM_PROMPT = """\
Tu es schoolsWP Brain, expert WordPress, SEO long terme, automatisation et conversion.
Public : freelances, formateurs, solopreneurs utilisant WordPress.
Plateforme : schoolswp.com (Michael KIHL).

MISSION : Produire un contenu stratégique optimisé SEO + LLM + Conversion + Autorité.

━━━ ACTIVER SYSTÉMATIQUEMENT ━━━

1. Déterminer intention (informationnelle / comparative / décisionnelle).
2. Structurer H1–H2–H3 optimisés (mot-clé dans H1, ≥2 H2, hiérarchie logique).
3. Expliquer POURQUOI avant COMMENT (problème → explication → solution).
4. Ajouter obligatoirement :
   – Bloc "Réponse rapide" (≤60 mots, autonome, extractible par Google AI Overview)
   – Bloc "Points clés" (3–5 bullets factuels)
   – Bloc "En résumé" (synthèse finale ≤80 mots)
5. Intégrer recommandation contextualisée (pour qui, dans quel cas, à quelle condition).
6. Ajouter 1 CTA soft aligné business (email / affiliation / formation — non agressif).
7. Auto-évaluer :
   – Score SEO /100 (structure + intent + champ lexical + lisibilité)
   – Score Conversion /100 (clarté problème + décision + CTA + business alignment)
   – Score Autorité /100 (couverture + connexions + cohérence + positionnement + cluster)
8. Si score < 90 sur l'un des 3 critères : améliorer automatiquement avant de livrer.
9. Proposer 3 contenus liés (cluster sémantique schoolsWP).

━━━ RÈGLES ABSOLUES ━━━

Branding schoolsWP :
– Tutoiement systématique (JAMAIS "vous" pour s'adresser au lecteur)
– Ton direct, pédagogique, chaleureux — jamais condescendant
– JAMAIS : disruptif, game changer, scalable, hack, révolutionnaire, incroyable,
  "en un clic", "sans effort", "il suffit de", "meilleur plugin universel"
– Zéro promesse irréaliste — toujours "dans mon cas" / "sur schoolsWP" si retour terrain
– Recommandation contextualisée (pas de conseil générique sans profil cible)

Contenu :
– Phrases courtes (≤20 mots idéalement)
– Paragraphes ≤5 lignes
– Chiffres réels ou estimations sourcées — jamais inventées
– Affiliation disclosée si présente : "(lien affilié — soutient schoolsWP sans surcoût)"

━━━ FORMAT DE SORTIE OBLIGATOIRE ━━━

IMPORTANT : utilise EXACTEMENT ces marqueurs de section (pas de ## avant).

---article---

[Article complet H1/H2/H3 en markdown — 1200–2000 mots]

---llm---

**Réponse rapide**
[≤60 mots, autonome]

**Points clés**
– [point 1]
– [point 2]
– [point 3]

**En résumé**
[≤80 mots]

---cta---

[Bloc CTA soft contextuel — tutoiement, utile, non agressif]

---scores---

SEO : XX/100
Conversion : XX/100
Autorité : XX/100

---cluster---

– [Titre article satellite 1 | intention | lien logique]
– [Titre article satellite 2 | intention | lien logique]
– [Titre article satellite 3 | intention | lien logique]

---meta---

title: [titre SEO ≤60 caractères]
description: [meta description ≤155 caractères]

Respecte strictement ces marqueurs — les sections sont parsées automatiquement.\
"""

# ---------------------------------------------------------------------------
# CompactBrainResult — dataclass de résultat parsé
# ---------------------------------------------------------------------------


@dataclass
class CompactBrainResult:
    """
    Résultat d'un appel CompactBrainAgent.

    Parsé depuis la sortie LLM structurée avec marqueurs ---section---.

    Champs :
        article         : Article markdown complet
        llm_block       : Blocs Réponse rapide + Points clés + En résumé
        cta_block       : CTA soft contextuel
        seo_score       : Score SEO auto-évalué /100
        conversion_score: Score Conversion auto-évalué /100
        authority_score : Score Autorité auto-évalué /100
        cluster         : 3 articles satellites recommandés
        meta_title      : Titre SEO
        meta_description: Meta description
        raw             : Réponse LLM brute complète
    """

    article: str = ""
    llm_block: str = ""
    cta_block: str = ""
    seo_score: int = 0
    conversion_score: int = 0
    authority_score: int = 0
    cluster: list[str] = field(default_factory=list)
    meta_title: str = ""
    meta_description: str = ""
    raw: str = ""

    @property
    def composite_score(self) -> int:
        """Moyenne simple des 3 scores auto-évalués."""
        scores = [
            s for s in [self.seo_score, self.conversion_score, self.authority_score]
            if s > 0
        ]
        return round(sum(scores) / len(scores)) if scores else 0

    @property
    def composite_emoji(self) -> str:
        s = self.composite_score
        if s >= 90:
            return "✅"
        elif s >= 80:
            return "🟡"
        elif s >= 70:
            return "🟠"
        else:
            return "🔴"

    @property
    def word_count(self) -> int:
        return len(self.article.split()) if self.article else 0

    @classmethod
    def parse(cls, raw: str) -> "CompactBrainResult":
        """Parse la réponse LLM structurée en CompactBrainResult."""
        result = cls(raw=raw)

        # Découpe par marqueurs ---key--- (évite le conflit avec les ## H2 de l'article)
        sections: dict[str, str] = {}
        current_key = ""
        current_lines: list[str] = []

        for line in raw.splitlines():
            m = re.match(r"^---(\w+)---\s*$", line.strip())
            if m:
                if current_key:
                    sections[current_key] = "\n".join(current_lines).strip()
                current_key = m.group(1).lower()
                current_lines = []
            else:
                current_lines.append(line)

        if current_key:
            sections[current_key] = "\n".join(current_lines).strip()

        result.article = sections.get("article", "")
        result.llm_block = sections.get("llm", "")
        result.cta_block = sections.get("cta", "")
        result.meta_title, result.meta_description = cls._parse_meta(sections.get("meta", ""))
        result.cluster = cls._parse_cluster(sections.get("cluster", ""))

        # Scores
        scores_raw = sections.get("scores", "")
        result.seo_score = cls._parse_score(scores_raw, r"SEO\s*:\s*(\d+)/100")
        result.conversion_score = cls._parse_score(scores_raw, r"Conversion\s*:\s*(\d+)/100")
        result.authority_score = cls._parse_score(scores_raw, r"Autorit[eé]\s*:\s*(\d+)/100")

        return result

    @staticmethod
    def _parse_score(text: str, pattern: str) -> int:
        m = re.search(pattern, text, re.IGNORECASE)
        return int(m.group(1)) if m else 0

    @staticmethod
    def _parse_meta(text: str) -> tuple[str, str]:
        title = ""
        description = ""
        for line in text.splitlines():
            if line.lower().startswith("title:"):
                title = line.split(":", 1)[1].strip()
            elif line.lower().startswith("description:"):
                description = line.split(":", 1)[1].strip()
        return title, description

    @staticmethod
    def _parse_cluster(text: str) -> list[str]:
        items = []
        for line in text.splitlines():
            line = line.strip()
            if line.startswith(("–", "-", "•", "*")):
                item = re.sub(r"^[\–\-\•\*]\s*", "", line).strip()
                if item:
                    items.append(item)
        return items[:3]

    def export_api_ready(self) -> dict:
        """
        Export JSON API-ready pour stockage ou transmission n8n.

        Retourne un dict avec tous les champs parsés.
        Compatible avec une insertion en base de données, un webhook n8n,
        ou une réponse JSON d'API.
        """
        return {
            "article": self.article,
            "llm_block": self.llm_block,
            "cta": self.cta_block,
            "meta": {
                "title": self.meta_title,
                "description": self.meta_description,
            },
            "scores": {
                "seo": self.seo_score,
                "conversion": self.conversion_score,
                "authority": self.authority_score,
                "composite": self.composite_score,
            },
            "cluster": self.cluster,
            "word_count": self.word_count,
        }


# ---------------------------------------------------------------------------
# CompactBrainAgent — single LLM call
# ---------------------------------------------------------------------------


class CompactBrainAgent(BaseContentAgent):
    """
    schoolsWP Brain — Version compact, single call.

    1 appel LLM (~30s) → article + LLM blocks + CTA + scores auto-évalués + cluster.

    Contrairement au ContentFactoryAgent (~4-8 min, 11-14 appels),
    la version compact sacrifie la profondeur multi-agent pour la vitesse.

    Cas d'usage :
        – Idéation rapide avant pipeline complet
        – Intégrations n8n / API
        – Tests de positionnement
        – Brouillon rapide à enrichir manuellement

    Usage :
        agent = CompactBrainAgent()
        result = await agent.run(
            keyword="tutor lms vs learndash",
            intent="comparative",
            audience="formateurs WordPress débutants",
            pillar="LMS",
        )
    """

    name = "brain-compact"
    system_prompt = COMPACT_SYSTEM_PROMPT

    async def run(  # type: ignore[override]
        self,
        keyword: str,
        intent: str = "décisionnelle",
        topic: str | None = None,
        audience: str | None = None,
        pillar: str | None = None,
        objective: str | None = None,
        angle: str | None = None,
    ) -> CompactBrainResult:
        """
        Génère un contenu complet en un seul appel LLM.

        Args:
            keyword   : Mot-clé SEO principal (obligatoire)
            intent    : informationnelle | comparative | décisionnelle (défaut : décisionnelle)
            topic     : Sujet/titre H1 si déjà défini (sinon auto-généré par le LLM)
            audience  : Profil lecteur précis (optionnel — améliore la pertinence)
            pillar    : Pilier schoolsWP (SEO|LMS|CRM|Performance|Automatisation)
            objective : Objectif business prioritaire (email|affiliation|formation|offre)
            angle     : Angle différenciant (optionnel — sinon le LLM choisit)

        Returns:
            CompactBrainResult avec article, blocs LLM, CTA, scores et cluster.
        """
        lines = [f"SUJET: {topic or keyword.title()}"]
        lines.append(f"MOT-CLÉ: {keyword}")
        lines.append(f"INTENTION: {intent}")
        if audience:
            lines.append(f"PUBLIC: {audience}")
        if pillar:
            lines.append(f"PILIER SCHOOLSWP: {pillar}")
        if objective:
            lines.append(f"OBJECTIF BUSINESS: {objective}")
        if angle:
            lines.append(f"ANGLE: {angle}")

        user_message = "\n".join(lines)

        response = await self._client.messages.create(
            model=self.model,
            max_tokens=5000,
            system=self.system_prompt,
            messages=[{"role": "user", "content": user_message}],
        )
        raw = response.content[0].text
        return CompactBrainResult.parse(raw)


# ---------------------------------------------------------------------------
# CLI intégré
# ---------------------------------------------------------------------------

_INTENTS = ["informationnelle", "comparative", "décisionnelle", "transactionnelle"]
_PILLARS = ["SEO", "LMS", "CRM", "Performance", "Automatisation"]
_OBJECTIVES = ["email", "affiliation", "formation", "offre"]


def _bar(score: int, width: int = 10) -> str:
    filled = round(score / 100 * width)
    return "█" * filled + "░" * (width - filled)


def _print_result(result: CompactBrainResult, elapsed: float) -> None:
    print("\n" + "━" * 62)
    print("  schoolsWP Brain Compact — Résultat")
    print("━" * 62)
    print(f"  Article   : {result.word_count} mots")
    print(f"  Composite : [{_bar(result.composite_score)}] {result.composite_score}/100  {result.composite_emoji}")
    print("─" * 62)
    print("  SCORES AUTO-ÉVALUÉS")
    print(f"  SEO         [{_bar(result.seo_score)}] {result.seo_score}/100")
    print(f"  Conversion  [{_bar(result.conversion_score)}] {result.conversion_score}/100")
    print(f"  Autorité    [{_bar(result.authority_score)}] {result.authority_score}/100")
    print("─" * 62)
    if result.cluster:
        print("  CLUSTER RECOMMANDÉ")
        for i, s in enumerate(result.cluster, 1):
            print(f"    {i}. {s}")
    if result.meta_title:
        print("─" * 62)
        print(f"  Meta title : {result.meta_title}")
    print("─" * 62)
    print(f"  Terminé en {elapsed:.1f}s  (1 appel LLM)")
    print("━" * 62)


async def main() -> None:
    parser = argparse.ArgumentParser(
        prog="brain-compact",
        description=(
            "schoolsWP Brain Compact — 1 LLM call (~30s). "
            "Article + LLM blocks + CTA + scores + cluster."
        ),
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=(
            "Exemples :\n\n"
            "  python -m agents.content_factory.brain_compact \\\n"
            '    --keyword "tutor lms vs learndash" --intent comparative --pillar LMS\n\n'
            "  python -m agents.content_factory.brain_compact \\\n"
            '    --keyword "fluentcrm wordpress" --intent décisionnelle \\\n'
            "    --pillar CRM --objective formation --save-dir articles/crm-compact/"
        ),
    )

    parser.add_argument("--keyword", required=True, metavar="MOT_CLÉ")
    parser.add_argument("--intent", default="décisionnelle", choices=_INTENTS)
    parser.add_argument("--topic", default=None, metavar="TITRE_H1",
                        help="Titre H1 si déjà défini (sinon auto-généré)")
    parser.add_argument("--audience", default=None, metavar="PUBLIC")
    parser.add_argument("--pillar", default=None, choices=_PILLARS, metavar="PILIER")
    parser.add_argument("--objective", default=None, choices=_OBJECTIVES, metavar="OBJECTIF")
    parser.add_argument("--angle", default=None, metavar="ANGLE",
                        help="Angle différenciant schoolsWP (optionnel)")
    parser.add_argument("--save-dir", default=None, metavar="DOSSIER",
                        help="Dossier de sauvegarde (article.md + llm.md + cta.md + meta.json)")
    parser.add_argument("--output", default=None, metavar="FICHIER",
                        help="Fichier unique pour l'article")
    parser.add_argument("--json", action="store_true",
                        help="Afficher le résultat en JSON (compatible API)")
    parser.add_argument("--model", default=None, metavar="MODEL")

    args = parser.parse_args()

    print(f"\n[brain-compact] schoolsWP Brain Compact", flush=True)
    print(f"  Mot-clé : {args.keyword}", flush=True)
    print(f"  Intent  : {args.intent}", flush=True)
    if args.pillar:
        print(f"  Pilier  : {args.pillar}", flush=True)
    print("  → 1 appel LLM en cours...", flush=True)

    agent = CompactBrainAgent(model=args.model)
    t_start = time.monotonic()

    result = await agent.run(
        keyword=args.keyword,
        intent=args.intent,
        topic=args.topic,
        audience=args.audience,
        pillar=args.pillar,
        objective=args.objective,
        angle=args.angle,
    )

    elapsed = time.monotonic() - t_start
    print(f"  ✓ Terminé en {elapsed:.1f}s  ({result.word_count} mots)", flush=True)

    if args.json:
        import json
        print(json.dumps(result.export_api_ready(), ensure_ascii=False, indent=2))
        return

    _print_result(result, elapsed)

    if args.save_dir:
        save_path = Path(args.save_dir)
        save_path.mkdir(parents=True, exist_ok=True)
        saved = []

        def _save(name: str, content: str) -> None:
            if content:
                (save_path / name).write_text(content, encoding="utf-8")
                saved.append(name)

        _save("article.md", result.article)
        _save("llm.md", result.llm_block)
        _save("cta.md", result.cta_block)

        if result.meta_title or result.meta_description:
            import json
            (save_path / "meta.json").write_text(
                json.dumps({
                    "title": result.meta_title,
                    "description": result.meta_description,
                }, ensure_ascii=False, indent=2),
                encoding="utf-8",
            )
            saved.append("meta.json")

        print(f"\n  Fichiers → {save_path}/")
        print(f"  {' | '.join(saved)}")

    elif args.output:
        out = Path(args.output)
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(result.article, encoding="utf-8")
        print(f"\n  Article → {out}")

    else:
        print("\n" + "=" * 60)
        print(result.article)
        if result.llm_block:
            print("\n" + "─" * 40)
            print(result.llm_block)
        if result.cta_block:
            print("\n" + "─" * 40)
            print(result.cta_block)


if __name__ == "__main__":
    asyncio.run(main())
