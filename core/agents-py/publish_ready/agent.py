"""
Super Agent — Publish Ready Dashboard — schoolsWP

Orchestrateur des 4 modules d'audit en parallèle.
Produit un dashboard unifié avec score composite et plan d'action priorisé.

Modules orchestrés (asyncio.gather — exécutés simultanément) :
  Module 1 — SeoAuditorAgent      : SEO structure /100 (5 × 20 pts)
  Module 2 — LlmSeoAgent          : Citabilité IA /100 (5 signaux)
  Module 3 — ConversionAuditorAgent: Score Conversion /100 (5 × 20 pts)
  Module 4 — TopicalAuthorityAgent : Autorité Thématique /100 (5 × 20 pts)

Score composite (Publish Score) :
  SEO structure    30 %  — fondation technique
  Citabilité IA    25 %  — future-proofing (Google AI + Perplexity)
  Conversion       25 %  — levier business
  Autorité thème   20 %  — écosystème long terme

Interprétation Publish Score :
  ≥ 90  → Publication immédiate
  80–89 → 1–2 optimisations ciblées
  70–79 → Travail requis sur blocs faibles
  < 70  → Révision substantielle avant publication

Usage programmatique :
    agent = PublishReadyAgent()
    result = await agent.run(article, keyword="lms wordpress rentable")
    print(result.publish_score)          # 84
    print(result.ready_to_publish)       # False
    print(result.action_plan[:3])        # top 3 actions

    # Avec auto-fix du bloc le plus faible
    result = await agent.run(
        article, keyword="...",
        fix_weakest=True,
        threshold=85,
    )
    if result.fixed_article:
        print(result.fixed_article)
"""

from __future__ import annotations

import asyncio
from dataclasses import dataclass, field

from agents.base import BaseContentAgent
from agents.conversion_auditor.agent import ConversionAuditorAgent, ConversionAuditResult
from agents.llm_seo.agent import CitationSignalResult, LlmSeoAgent
from agents.seo_auditor.agent import AuditResult, SeoAuditorAgent
from agents.topical_authority.agent import TopicalAuditResult, TopicalAuthorityAgent

# ---------------------------------------------------------------------------
# Weights — Publish Score formula
# ---------------------------------------------------------------------------

_WEIGHTS = {
    "seo": 0.30,
    "llm": 0.25,
    "conversion": 0.25,
    "authority": 0.20,
}

# ---------------------------------------------------------------------------
# Prompt de synthèse finale (plan d'action priorisé)
# ---------------------------------------------------------------------------

_SYNTHESIS_SYSTEM = """\
Tu es un éditeur stratégique senior pour schoolsWP.

CONTEXTE
Tu reçois les rapports complets de 4 audits réalisés sur un même article WordPress :
  – Module 1 : Audit SEO Structure
  – Module 2 : Audit Citabilité IA (LLM-SEO)
  – Module 3 : Score Conversion & CTA
  – Module 4 : Topical Authority

MISSION
Synthétiser ces 4 rapports en un plan d'action priorisé, sans répétition.

RÈGLES
– Maximum 8 actions, classées de la plus impactante à la moins impactante
– Chaque action doit être concrète, réalisable, liée à un bloc précis
– Indiquer le module source entre parenthèses : (SEO) | (IA) | (Conversion) | (Autorité)
– Pas de généralités — chaque action doit être applicable à cet article précis
– Tutoiement (jamais "vous")
– Pas d'introduction ni de conclusion éditoriales

FORMAT OBLIGATOIRE

## Plan d'action prioritaire

1. [Action la plus impactante] (Module)
2. [Action 2] (Module)
3. [Action 3] (Module)
4. [Action 4] (Module)
5. [Action 5] (Module)
[jusqu'à 8 max]

## Bloc prioritaire à corriger en premier
**[Nom du bloc]** — [justification 1 phrase]

## Potentiel après optimisations
Si les 3 premières actions sont appliquées : Publish Score estimé à XX/100.

Uniquement ce contenu — pas de résumé des rapports.\
"""


# ---------------------------------------------------------------------------
# PublishReadyResult — dataclass de résultat agrégé
# ---------------------------------------------------------------------------


@dataclass
class PublishReadyResult:
    """
    Résultat agrégé du Publish Ready Dashboard.

    Contient les 4 résultats d'audit + le score composite + le plan d'action.

    Champs principaux :
        seo_result        : AuditResult (Module 1)
        llm_result        : CitationSignalResult (Module 2)
        conversion_result : ConversionAuditResult (Module 3)
        authority_result  : TopicalAuditResult (Module 4)
        publish_score     : score composite /100 (pondéré)
        action_plan       : plan d'action priorisé (markdown)
        ready_to_publish  : True si publish_score >= threshold
        fixed_article     : article amélioré si fix_weakest=True
        weakest_module    : nom du module avec le score le plus faible
        dashboard         : rapport markdown unifié complet
    """

    seo_result: AuditResult = field(default_factory=AuditResult)
    llm_result: CitationSignalResult = field(default_factory=CitationSignalResult)
    conversion_result: ConversionAuditResult = field(default_factory=ConversionAuditResult)
    authority_result: TopicalAuditResult = field(default_factory=TopicalAuditResult)
    publish_score: int = 0
    action_plan: str = ""
    ready_to_publish: bool = False
    fixed_article: str = ""
    weakest_module: str = ""
    dashboard: str = ""

    @property
    def publish_diagnostic(self) -> str:
        if self.publish_score >= 90:
            return "Publication immédiate"
        elif self.publish_score >= 80:
            return "1–2 optimisations ciblées"
        elif self.publish_score >= 70:
            return "Travail requis sur blocs faibles"
        else:
            return "Révision substantielle"

    @property
    def publish_emoji(self) -> str:
        if self.publish_score >= 90:
            return "✅"
        elif self.publish_score >= 80:
            return "🟡"
        elif self.publish_score >= 70:
            return "🟠"
        else:
            return "🔴"

    def scores_summary(self) -> dict[str, int]:
        return {
            "SEO Structure": self.seo_result.score_global,
            "Citabilité IA": self.llm_result.citation_score,
            "Conversion": self.conversion_result.score_conversion,
            "Autorité thème": self.authority_result.score_autorite,
        }


def _compute_publish_score(seo: int, llm: int, conversion: int, authority: int) -> int:
    """Calcule le Publish Score composite pondéré."""
    raw = (
        seo * _WEIGHTS["seo"]
        + llm * _WEIGHTS["llm"]
        + conversion * _WEIGHTS["conversion"]
        + authority * _WEIGHTS["authority"]
    )
    return round(raw)


def _find_weakest(seo: int, llm: int, conversion: int, authority: int) -> str:
    scores = {
        "SEO Structure": seo,
        "Citabilité IA": llm,
        "Conversion & CTA": conversion,
        "Autorité Thématique": authority,
    }
    return min(scores, key=lambda k: scores[k])


def _build_dashboard(result: PublishReadyResult, keyword: str) -> str:
    """Construit le rapport markdown unifié."""
    scores = result.scores_summary()

    def bar(s):
        return "█" * round(s / 10) + "░" * (10 - round(s / 10))

    lines = [
        f"# Publish Ready Dashboard — {keyword}",
        "",
        "---",
        "",
        f"## Publish Score : {result.publish_score}/100  {result.publish_emoji}",
        f"**{result.publish_diagnostic}**",
        "",
        "| Module | Score | Barre |",
        "|--------|-------|-------|",
    ]
    for name, score in scores.items():
        lines.append(f"| {name} | {score}/100 | {bar(score)} |")

    lines += [
        "",
        f"**Bloc le plus faible** : {result.weakest_module}",
        "",
        "---",
        "",
        result.action_plan,
        "",
        "---",
        "",
        "## Rapports détaillés",
        "",
        "### Module 1 — SEO Structure",
        result.seo_result.report,
        "",
        "### Module 2 — Citabilité IA",
        result.llm_result.report,
        "",
        "### Module 3 — Conversion & CTA",
        result.conversion_result.report,
        "",
        "### Module 4 — Autorité Thématique",
        result.authority_result.report,
    ]
    return "\n".join(lines)


# ---------------------------------------------------------------------------
# Agent de synthèse (privé)
# ---------------------------------------------------------------------------


class _SynthesisAgent(BaseContentAgent):
    """Synthétise les 4 rapports en un plan d'action priorisé."""

    name = "publish-ready-synthesis"
    system_prompt = _SYNTHESIS_SYSTEM

    async def run(  # type: ignore[override]
        self,
        seo_report: str,
        llm_report: str,
        conversion_report: str,
        authority_report: str,
        keyword: str,
        publish_score: int,
    ) -> str:
        user_message = (
            f"Mot-clé principal : {keyword}\n"
            f"Publish Score composite : {publish_score}/100\n\n"
            "--- MODULE 1 : AUDIT SEO STRUCTURE ---\n\n"
            f"{seo_report}\n\n"
            "--- MODULE 2 : AUDIT CITABILITÉ IA ---\n\n"
            f"{llm_report}\n\n"
            "--- MODULE 3 : SCORE CONVERSION & CTA ---\n\n"
            f"{conversion_report}\n\n"
            "--- MODULE 4 : TOPICAL AUTHORITY ---\n\n"
            f"{authority_report}"
        )
        return await self.call_llm(user_message, max_tokens=1500)


# ---------------------------------------------------------------------------
# PublishReadyAgent — orchestrateur principal
# ---------------------------------------------------------------------------


class PublishReadyAgent(BaseContentAgent):
    """
    Super Agent Publish Ready — schoolsWP.

    Orchestre les 4 modules d'audit en parallèle et produit :
    – Un Publish Score composite pondéré /100
    – Un dashboard unifié avec les 4 scores
    – Un plan d'action priorisé (synthèse LLM cross-modules)
    – Optionnellement : correction automatique du bloc le plus faible

    Formule Publish Score :
        SEO (30%) + LLM/IA (25%) + Conversion (25%) + Autorité (20%)

    Usage :
        agent = PublishReadyAgent()
        result = await agent.run(
            article=article,
            keyword="lms wordpress rentable",
            intent="décisionnelle",
            pillar="LMS",
        )
        print(result.publish_score)
        print(result.action_plan)

        # Avec auto-fix du module le plus faible
        result = await agent.run(
            article=article,
            keyword="lms wordpress",
            fix_weakest=True,
            threshold=85,
        )
    """

    name = "publish-ready"
    system_prompt = _SYNTHESIS_SYSTEM  # utilisé par la sous-classe

    async def run(  # type: ignore[override]
        self,
        article: str,
        keyword: str,
        intent: str | None = None,
        pillar: str | None = None,
        objective: str | None = None,
        fix_weakest: bool = False,
        threshold: int = 85,
    ) -> PublishReadyResult:
        """
        Lance les 4 audits en parallèle, calcule le Publish Score, synthétise.

        Args:
            article     : Article markdown à auditer
            keyword     : Mot-clé SEO principal
            intent      : Intention de recherche (optionnel)
            pillar      : Pilier thématique schoolsWP (optionnel)
            objective   : Objectif business prioritaire pour Conversion (optionnel)
            fix_weakest : Si True et publish_score < threshold,
                          corrige automatiquement le module le plus faible
            threshold   : Seuil de publication (défaut : 85)

        Returns:
            PublishReadyResult avec les 4 résultats, publish_score, action_plan,
            dashboard markdown et (optionnellement) fixed_article.
        """
        # 4 audits en parallèle
        seo_agent = SeoAuditorAgent(model=self.raw_model)
        llm_agent = LlmSeoAgent(model=self.raw_model)
        conv_agent = ConversionAuditorAgent(model=self.raw_model)
        auth_agent = TopicalAuthorityAgent(model=self.raw_model)

        seo_res, llm_res, conv_res, auth_res = await asyncio.gather(
            seo_agent.run(article=article, keyword=keyword, intent=intent),
            llm_agent.audit(article=article, keyword=keyword, intent=intent),
            conv_agent.run(
                article=article,
                keyword=keyword,
                intent=intent,
                objective=objective,
            ),
            auth_agent.run(
                article=article,
                keyword=keyword,
                intent=intent,
                pillar=pillar,
            ),
        )

        publish_score = _compute_publish_score(
            seo=seo_res.score_global,
            llm=llm_res.citation_score,
            conversion=conv_res.score_conversion,
            authority=auth_res.score_autorite,
        )

        weakest = _find_weakest(
            seo=seo_res.score_global,
            llm=llm_res.citation_score,
            conversion=conv_res.score_conversion,
            authority=auth_res.score_autorite,
        )

        result = PublishReadyResult(
            seo_result=seo_res,
            llm_result=llm_res,
            conversion_result=conv_res,
            authority_result=auth_res,
            publish_score=publish_score,
            ready_to_publish=(publish_score >= threshold),
            weakest_module=weakest,
        )

        # Synthèse plan d'action cross-modules
        synth = _SynthesisAgent(model=self.raw_model)
        result.action_plan = await synth.run(
            seo_report=seo_res.report,
            llm_report=llm_res.report,
            conversion_report=conv_res.report,
            authority_report=auth_res.report,
            keyword=keyword,
            publish_score=publish_score,
        )

        # Auto-fix du module le plus faible (optionnel)
        if fix_weakest and not result.ready_to_publish:
            result.fixed_article = await self._fix_weakest(
                article=article,
                keyword=keyword,
                intent=intent,
                objective=objective,
                result=result,
            )

        # Dashboard unifié
        result.dashboard = _build_dashboard(result, keyword)

        return result

    async def _fix_weakest(
        self,
        article: str,
        keyword: str,
        intent: str | None,
        objective: str | None,
        result: PublishReadyResult,
    ) -> str:
        """
        Corrige automatiquement le module ayant le score le plus faible.
        Retourne l'article amélioré ou une chaîne vide si aucune correction.
        """
        scores = result.scores_summary()
        weakest_name = result.weakest_module
        weakest_score = scores.get(weakest_name, 100)

        # SEO est le plus faible → SeoAuditorAgent.audit_and_fix
        if weakest_name == "SEO Structure":
            from agents.seo_auditor.agent import SeoAuditorAgent as _SA

            agent = _SA(model=self.raw_model)
            fix_result = await agent.audit_and_fix(article=article, keyword=keyword, intent=intent, threshold=90)
            return fix_result.v2 if fix_result.fixed else ""

        # Conversion est le plus faible → ConversionAuditorAgent.audit_and_inject
        if weakest_name == "Conversion & CTA":
            from agents.conversion_auditor.agent import ConversionAuditorAgent as _CA

            agent = _CA(model=self.raw_model)
            inject_result = await agent.audit_and_inject(
                article=article, keyword=keyword, intent=intent, objective=objective
            )
            return inject_result.article_with_cta if inject_result.injected else ""

        # LLM-SEO est le plus faible → LlmSeoAgent.optimize
        if weakest_name == "Citabilité IA":
            from agents.llm_seo.agent import LlmSeoAgent as _LA

            agent = _LA(model=self.raw_model)
            opt_result = await agent.optimize(article=article, keyword=keyword, intent=intent)
            return opt_result.article_optimized if opt_result.optimized else ""

        # Autorité est le plus faible → pas de fix automatique (besoin de nouveaux articles)
        # On retourne une note explicative
        return (
            f"[Note] Le bloc Autorité Thématique ({weakest_score}/100) ne peut pas être "
            "corrigé dans cet article seul — il nécessite la création d'articles satellites. "
            f"Consulter le rapport topical-audit.md pour les recommandations cluster."
        )
