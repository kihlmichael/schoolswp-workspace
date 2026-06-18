"""
Module Auto-Audit SEO schoolsWP — Agent standalone /100

Score un article sur 5 dimensions (5 × 20 pts) :
  1. SEO Structure      — Hn, mot-clé, maillage, lisibilité
  2. Intention          — Intent respectée, angle différenciant, hors-sujet
  3. Pédagogie          — Clarté, jargon, paragraphes courts
  4. Valeur business    — Décision aidée, cas d'usage, recommandation
  5. Branding schoolsWP — Tutoiement, mots interdits, hype, nuance

Mode auto-fix : si score < seuil, réécrit uniquement les sections faibles.

Usage programmatique :
    agent = SeoAuditorAgent()
    result = await agent.run(article, keyword="lms wordpress rentable")
    print(result.score_global, result.diagnostic)

    # Audit + correction automatique
    result = await agent.audit_and_fix(article, keyword="...", threshold=90)
    if result.fixed:
        print(result.v2)
"""

from __future__ import annotations

import re
from dataclasses import dataclass, field

from agents.base import BaseContentAgent

# ---------------------------------------------------------------------------
# Prompt d'audit
# ---------------------------------------------------------------------------

_AUDIT_SYSTEM = """\
Tu es un auditeur SEO senior spécialisé WordPress pour schoolsWP.

MISSION
Auditer le contenu fourni et attribuer un score global sur 100.
Ton analyse doit être objective, précise, ni complaisante ni destructrice.

━━━ 5 BLOCS D'AUDIT (20 pts chacun) ━━━

1️⃣ SEO STRUCTURE (20 pts)
Évaluer :
– H1 unique, présent et optimisé pour le mot-clé principal
– H2 logiques, hiérarchisés, sans doublon de H1
– Mot-clé principal dans H1, intro, et au moins 2 H2
– Mots-clés secondaires couverts en titres ou corps
– Lisibilité : paragraphes ≤ 5 lignes, phrases courtes
– Maillage interne suggéré ou présent
Pénalités : H1 absent (−10), mot-clé absent de l'intro (−4), structure Hn chaotique (−6)

2️⃣ INTENTION DE RECHERCHE (20 pts)
Évaluer :
– Intent principale respectée (informationnelle / comparative / décisionnelle)
– Réponse directe et claire au problème posé
– Absence de hors-sujet ou de sections sans rapport
– Angle différenciant par rapport aux résultats SERP génériques
– Présence d'une "Réponse rapide" ou équivalent featured snippet
Pénalités : intent non respectée (−10), réponse vague (−5), pas d'angle unique (−4)

3️⃣ QUALITÉ PÉDAGOGIQUE (20 pts)
Évaluer :
– Clarté des explications (concept → exemple → application)
– Jargon technique expliqué ou défini
– Paragraphes courts, structure logique
– Pas de listes à 1 seul item, pas de titres sans corps
– Progression logique : problème → explication → solution
Pénalités : jargon non expliqué (−5), blocs trop longs (−4), structure désordonnée (−5)

4️⃣ VALEUR BUSINESS (20 pts)
Évaluer :
– Aide concrète à prendre une décision WordPress
– Contextualisation pour le public cible (freelances, formateurs, solopreneurs)
– Au moins un cas d'usage concret ou exemple chiffré
– Recommandation exploitable (pas de conseil générique sans profil cible)
– CTA ou orientation vers une ressource complémentaire
Pénalités : aucun chiffre (−5), recommandation générique (−5), pas de cas d'usage (−6)

5️⃣ COHÉRENCE BRANDING schoolsWP (20 pts)
Évaluer :
– Tutoiement systématique (jamais "vous" pour s'adresser au lecteur — critique)
– Ton direct, pédagogique, chaleureux, jamais condescendant
– Mots INTERDITS absents : disruptif, game changer, scalable, hack, révolutionnaire,
  incroyable, "en un clic", "sans effort", "il suffit de", "meilleur plugin universel"
– Zéro promesse non prouvée — toujours "dans mon cas" / "sur schoolsWP" si retour terrain
– Approche nuancée : jamais de décision binaire sans contexte
Pénalités : utilisation du "vous" (−8), mot interdit présent (−5/occurrence), promesse irréaliste (−6)

━━━ FORMAT DE SORTIE OBLIGATOIRE ━━━

Score global : XX/100

Détail par bloc :
SEO STRUCTURE : X/20
INTENTION : X/20
PÉDAGOGIE : X/20
BUSINESS : X/20
BRANDING : X/20

Points forts :
– ...
– ...

Points faibles :
– ...
– ...

Axes d'amélioration prioritaires :
1. [action concrète, pas de généralité]
2. [action concrète]
3. [action concrète]

Respecte strictement ce format — les scores sont parsés automatiquement.\
"""

# ---------------------------------------------------------------------------
# Prompt de correction automatique (mode --fix)
# ---------------------------------------------------------------------------

_FIX_SYSTEM = """\
Tu es un éditeur senior WordPress pour schoolsWP.

CONTEXTE
Tu as reçu un article et le rapport d'audit SEO qui l'accompagne.
Le score est insuffisant (< seuil de publication).

MISSION
Réécrire UNIQUEMENT les sections qui font baisser le score.
Ne pas modifier ce qui fonctionne.
Faire passer le score au-dessus de 90/100.

RÈGLES D'ÉDITION

Structure :
– Corriger les Hn mal positionnés selon les axes d'amélioration
– Intégrer les mots-clés secondaires manquants dans les titres signalés
– Ajouter "Réponse rapide" en début d'article si absent

Contenu :
– Intégrer les cas d'usage concrets manquants (avec données chiffrées si possible)
– Développer les recommandations génériques en recommandations profilées
– Définir les termes techniques signalés comme jargon non expliqué

Branding schoolsWP (priorité absolue) :
– Convertir TOUT "vous" en "tu"
– Supprimer TOUS les mots interdits identifiés
– Remplacer les promesses irréalistes par des formulations nuancées

FORMAT DE SORTIE
L'article complet corrigé en markdown (H1/H2/H3), prêt à publier.
Pas de commentaires éditoriaux, pas de bilan des changements.
Uniquement l'article V2 amélioré.\
"""


# ---------------------------------------------------------------------------
# AuditResult — dataclass de résultat parsé
# ---------------------------------------------------------------------------


@dataclass
class AuditResult:
    """
    Résultat structuré d'un audit SEO schoolsWP.

    Produit par SeoAuditorAgent.run() — parsé depuis la sortie LLM.

    Champs principaux :
        score_global     : score /100 parsé
        seo_structure    : bloc 1 /20
        intention        : bloc 2 /20
        pedagogie        : bloc 3 /20
        business         : bloc 4 /20
        branding         : bloc 5 /20
        report           : rapport complet markdown
        v2               : article corrigé si mode audit_and_fix
        fixed            : True si auto-correction déclenchée
    """

    score_global: int = 0
    seo_structure: int = 0
    intention: int = 0
    pedagogie: int = 0
    business: int = 0
    branding: int = 0
    points_forts: list[str] = field(default_factory=list)
    points_faibles: list[str] = field(default_factory=list)
    axes_amelioration: list[str] = field(default_factory=list)
    report: str = ""
    v2: str = ""
    fixed: bool = False

    @property
    def diagnostic(self) -> str:
        """Interprétation schoolsWP du score."""
        if self.score_global >= 95:
            return "Publication immédiate"
        elif self.score_global >= 85:
            return "Ajustements mineurs"
        elif self.score_global >= 70:
            return "Optimisation nécessaire"
        else:
            return "Réécriture stratégique"

    @property
    def diagnostic_emoji(self) -> str:
        if self.score_global >= 95:
            return "✅"
        elif self.score_global >= 85:
            return "🟡"
        elif self.score_global >= 70:
            return "🟠"
        else:
            return "🔴"

    @classmethod
    def parse(cls, report: str) -> "AuditResult":
        """Parse le rapport markdown LLM en AuditResult structuré."""
        result = cls(report=report)

        # Score global
        m = re.search(r"Score global\s*:\s*(\d+)/100", report, re.IGNORECASE)
        if m:
            result.score_global = int(m.group(1))

        # Blocs /20
        bloc_patterns = {
            "seo_structure": r"SEO STRUCTURE\s*:\s*(\d+)/20",
            "intention": r"INTENTION\s*:\s*(\d+)/20",
            "pedagogie": r"P[ÉE]DAGOGIE\s*:\s*(\d+)/20",
            "business": r"BUSINESS\s*:\s*(\d+)/20",
            "branding": r"BRANDING\s*:\s*(\d+)/20",
        }
        for attr, pattern in bloc_patterns.items():
            m = re.search(pattern, report, re.IGNORECASE)
            if m:
                setattr(result, attr, int(m.group(1)))

        # Points forts (lignes commençant par –)
        m = re.search(
            r"Points forts\s*:\s*\n((?:[\–\-][^\n]+\n?)+)",
            report,
            re.IGNORECASE,
        )
        if m:
            result.points_forts = [
                re.sub(r"^[\–\-]\s*", "", line).strip() for line in m.group(1).strip().splitlines() if line.strip()
            ]

        # Points faibles
        m = re.search(
            r"Points faibles\s*:\s*\n((?:[\–\-][^\n]+\n?)+)",
            report,
            re.IGNORECASE,
        )
        if m:
            result.points_faibles = [
                re.sub(r"^[\–\-]\s*", "", line).strip() for line in m.group(1).strip().splitlines() if line.strip()
            ]

        # Axes d'amélioration (lignes numérotées)
        m = re.search(
            r"Axes d.amélioration[^\n]*:\s*\n((?:\d+\.[^\n]+\n?)+)",
            report,
            re.IGNORECASE,
        )
        if m:
            result.axes_amelioration = [
                re.sub(r"^\d+\.\s*", "", line).strip() for line in m.group(1).strip().splitlines() if line.strip()
            ]

        return result

    def summary(self) -> str:
        """Résumé compact du rapport pour affichage CLI."""
        lines = [
            f"  Score global   : {self.score_global}/100  {self.diagnostic_emoji}  {self.diagnostic}",
            f"  SEO Structure  : {self.seo_structure}/20",
            f"  Intention      : {self.intention}/20",
            f"  Pédagogie      : {self.pedagogie}/20",
            f"  Business       : {self.business}/20",
            f"  Branding       : {self.branding}/20",
        ]
        if self.points_faibles:
            lines.append("")
            lines.append("  Points faibles :")
            for p in self.points_faibles[:3]:
                lines.append(f"    – {p}")
        if self.axes_amelioration:
            lines.append("")
            lines.append("  Axes prioritaires :")
            for i, a in enumerate(self.axes_amelioration[:3], 1):
                lines.append(f"    {i}. {a}")
        return "\n".join(lines)


# ---------------------------------------------------------------------------
# Agent de correction automatique (privé)
# ---------------------------------------------------------------------------


class _FixerAgent(BaseContentAgent):
    """Réécrit les sections faibles pour atteindre >90/100."""

    name = "seo-auditor-fixer"
    system_prompt = _FIX_SYSTEM

    async def run(  # type: ignore[override]
        self,
        article: str,
        audit_report: str,
        keyword: str,
        score: int,
    ) -> str:
        user_message = (
            f"Mot-clé principal : {keyword}\n"
            f"Score actuel : {score}/100 — objectif : ≥ 90/100\n\n"
            "--- RAPPORT D'AUDIT ---\n\n"
            f"{audit_report}\n\n"
            "--- ARTICLE À CORRIGER ---\n\n"
            f"{article}"
        )
        return await self.call_llm(user_message, max_tokens=6000)


# ---------------------------------------------------------------------------
# SeoAuditorAgent — agent principal
# ---------------------------------------------------------------------------


class SeoAuditorAgent(BaseContentAgent):
    """
    Module Auto-Audit SEO schoolsWP — score /100 sur 5 dimensions.

    Deux modes d'utilisation :

    Mode audit simple :
        result = await agent.run(article, keyword="lms wordpress rentable")
        print(result.score_global)   # 78
        print(result.diagnostic)     # "Optimisation nécessaire"

    Mode audit + correction automatique :
        result = await agent.audit_and_fix(article, keyword="...", threshold=90)
        if result.fixed:
            # result.v2 contient l'article corrigé
            print(result.v2)
    """

    name = "seo-auditor"
    system_prompt = _AUDIT_SYSTEM

    async def run(  # type: ignore[override]
        self,
        article: str,
        keyword: str,
        intent: str | None = None,
    ) -> AuditResult:
        """
        Audite un article et retourne un AuditResult parsé.

        Args:
            article : Contenu markdown à auditer
            keyword : Mot-clé SEO principal de l'article
            intent  : Intention de recherche (pour contextualiser le bloc 2)

        Returns:
            AuditResult avec score_global, 5 blocs /20, points forts/faibles,
            axes d'amélioration et propriété diagnostic calculée automatiquement.
        """
        intent_block = f"\nIntention de recherche : {intent}" if intent else ""
        user_message = f"Mot-clé principal : {keyword}{intent_block}\n\n--- ARTICLE À AUDITER ---\n\n{article}"
        raw = await self.call_llm(user_message, max_tokens=2500)
        return AuditResult.parse(raw)

    async def audit_and_fix(
        self,
        article: str,
        keyword: str,
        intent: str | None = None,
        threshold: int = 90,
    ) -> AuditResult:
        """
        Audit + correction automatique si score < threshold.

        Args:
            article   : Article à auditer
            keyword   : Mot-clé principal
            intent    : Intention de recherche (optionnel)
            threshold : Score minimum pour éviter la correction (défaut : 90)

        Returns:
            AuditResult. Si score < threshold : result.fixed=True et result.v2
            contient l'article corrigé. Sinon result.fixed=False et result.v2="".
        """
        result = await self.run(article=article, keyword=keyword, intent=intent)

        if result.score_global < threshold:
            fixer = _FixerAgent(model=self.raw_model)
            result.v2 = await fixer.run(
                article=article,
                audit_report=result.report,
                keyword=keyword,
                score=result.score_global,
            )
            result.fixed = True

        return result
