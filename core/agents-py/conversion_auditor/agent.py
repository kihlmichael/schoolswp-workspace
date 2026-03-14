"""
Module Score Conversion & CTA Layer — schoolsWP

Audit de conversion /100 sur 5 blocs stratégiques + injection CTA si score < seuil.

Un article SEO sans couche conversion est un article qui attire mais n'oriente pas.
Ce module mesure si le contenu fait passer le lecteur de l'intention à l'action.

5 blocs × 20 pts :
  1. Clarté du problème        — le lecteur se reconnaît, le besoin est explicite
  2. Logique décisionnelle     — critères clairs, l'utilisateur peut décider
  3. Orientation action        — next step naturel, évite l'indécision
  4. CTA stratégique           — cohérent, contextualisé, non agressif
  5. Cohérence business schoolsWP — sert autorité/email/affiliation/offre

Mode inject : si score < seuil, injecte ou améliore les CTA sans réécrire l'article.

Usage programmatique :
    agent = ConversionAuditorAgent()
    result = await agent.run(article, keyword="lms wordpress rentable")
    print(result.score_conversion, result.diagnostic)

    # Audit + injection CTA automatique
    result = await agent.audit_and_inject(article, keyword="...", threshold=85)
    if result.injected:
        print(result.article_with_cta)
"""
from __future__ import annotations

import re
from dataclasses import dataclass, field

from agents.base import BaseContentAgent

# ---------------------------------------------------------------------------
# Prompt d'audit conversion
# ---------------------------------------------------------------------------

_AUDIT_SYSTEM = """\
Tu es un stratège conversion spécialisé WordPress pour schoolsWP.

MISSION
Analyser le contenu fourni et attribuer un Score Conversion sur 100.
Ton analyse est stratégique, précise, orientée business réel.
schoolsWP s'adresse à des freelances, formateurs et solopreneurs WordPress.

━━━ 5 BLOCS D'AUDIT (20 pts chacun) ━━━

1️⃣ CLARTÉ DU PROBLÈME (20 pts)
Évaluer :
– Le lecteur cible se reconnaît-il immédiatement dans l'intro ?
– Le problème/besoin est-il formulé explicitement (pas supposé) ?
– Le contexte est-il posé avant d'entrer dans le contenu ?
– Le titre et l'intro sont-ils alignés sur la douleur réelle du lecteur ?
Pénalités : intro trop générique sans ancrage problème (−6), lecteur pas identifié (−5),
besoin implicite jamais formulé (−5), ouverture hors-sujet (−4)

2️⃣ LOGIQUE DÉCISIONNELLE (20 pts)
Évaluer :
– Les critères de choix sont-ils explicités (pour qui, dans quel cas) ?
– Le lecteur peut-il prendre une décision à la fin de la lecture ?
– Les alternatives et conditions sont-elles présentées honnêtement ?
– Y a-t-il un tableau comparatif, un arbre de décision ou un profil de recommandation ?
– Les limites sont-elles mentionnées (pas de solution "universelle") ?
Pénalités : recommandation binaire sans profil (−6), aucun critère de choix (−5),
alternatives ignorées (−4), conclusion sans orientation (−5)

3️⃣ ORIENTATION ACTION (20 pts)
Évaluer :
– Y a-t-il un next step naturel et logique après lecture ?
– Le contenu évite-t-il de laisser le lecteur dans l'indécision ?
– Les actions proposées sont-elles concrètes et réalisables immédiatement ?
– La progression lecture → action est-elle fluide (pas de rupture) ?
– Les actions sont-elles adaptées au niveau du lecteur (débutant / avancé) ?
Pénalités : fin d'article sans orientation (−7), next step flou ou générique (−5),
actions trop complexes sans accompagnement (−4), rupture logique lecture/action (−4)

4️⃣ CTA STRATÉGIQUE (20 pts)
Évaluer :
– Y a-t-il au moins un CTA dans l'article (implicite ou explicite) ?
– Le CTA est-il contextualisé et cohérent avec le sujet traité ?
– Le CTA est-il non agressif (pas de FOMO forcé, pas de jargon marketing) ?
– Le CTA est-il utile pour le lecteur (pas uniquement pour schoolsWP) ?
– Le lien affilié est-il disclosé si présent ?
– Le CTA sert-il au moins un des leviers : email / affiliation / formation / offre directe ?
Pénalités : CTA absent (−10), CTA générique sans contexte (−6),
CTA agressif ou FOMO (−5), affiliation non disclosée (−5)

5️⃣ COHÉRENCE BUSINESS schoolsWP (20 pts)
Évaluer :
– L'article renforce-t-il l'autorité de schoolsWP sur ce sujet ?
– Y a-t-il une opportunité email (lead magnet, checklist, guide) ? Est-elle exploitée ?
– Y a-t-il une opportunité d'affiliation contextuelle ? Est-elle intégrée proprement ?
– L'article prépare-t-il ou soutient-il une offre de formation ou de service ?
– L'ensemble sert-il un tunnel de conversion cohérent (même implicite) ?
Pénalités : aucun levier business exploité (−8), contenu SEO pur sans intention business (−6),
opportunité email manquée sans raison (−4), contenu qui travaille contre l'autorité (−5)

━━━ FORMAT DE SORTIE OBLIGATOIRE ━━━

Score Conversion : XX/100

Détail :
Clarté problème : X/20
Décision : X/20
Orientation action : X/20
CTA : X/20
Business alignment : X/20

Points forts :
– ...
– ...

Faiblesses :
– ...
– ...

Recommandations concrètes :
1. [action précise et réalisable]
2. [action précise et réalisable]
3. [action précise et réalisable]

Respecte strictement ce format — les scores sont parsés automatiquement.\
"""

# ---------------------------------------------------------------------------
# Prompt d'injection CTA (mode --inject)
# ---------------------------------------------------------------------------

_INJECT_SYSTEM = """\
Tu es un éditeur conversion senior pour schoolsWP.

CONTEXTE
Tu as reçu un article WordPress et le rapport d'audit conversion qui l'accompagne.
Le score de conversion est insuffisant (< seuil de publication business).
Tu dois améliorer la couche CTA et business sans réécrire l'article.

MISSION
Injecter ou améliorer les CTA de l'article pour faire passer le score au-dessus de 85/100.
Modifier UNIQUEMENT ce qui est signalé dans les faiblesses et recommandations.
Ne pas toucher aux sections SEO, à la structure, ni aux parties qui fonctionnent.

━━━ LEVIERS À ACTIVER ━━━

Levier 1 — Bloc CTA Soft (toujours pertinent)
À placer en fin de section principale ou avant la FAQ :

> Si tu utilises déjà WordPress pour ton activité,
> le vrai enjeu n'est pas d'ajouter plus de plugins,
> mais de structurer un système cohérent.
>
> Commence par :
> – clarifier ton objectif principal
> – choisir un outil adapté à ton usage réel
> – automatiser intelligemment
>
> C'est exactement l'approche schoolsWP.

Levier 2 — Bloc CTA Lead Magnet (si opportunité email identifiée)
À placer en fin d'intro ou après une section clé :

> **Tu veux la checklist complète pour [sujet spécifique] ?**
>
> Télécharge le guide gratuit → [lien ou placeholder]

Adapter le sujet et le format au contenu de l'article.
Ne pas générer ce bloc s'il n'y a pas d'opportunité email réelle.

Levier 3 — Bloc CTA Affiliation (si outil recommandé dans l'article)
À placer directement après la mention de l'outil :

> Si [outil_recommandé] correspond à ton profil,
> tu peux le tester ici → [lien ou placeholder]
>
> *(Lien affilié transparent — cela soutient schoolsWP sans coût supplémentaire.)*

Adapter à l'outil réellement mentionné. Ne pas forcer si pas d'outil cité.

━━━ RÈGLES D'INJECTION ━━━

Branding (priorité absolue) :
– Tutoiement SYSTÉMATIQUE (jamais "vous")
– Ton utile, direct, jamais agressif
– Zéro FOMO forcé ("offre limitée", "ne ratez pas", "dernière chance")
– Zéro mots interdits : disruptif, game changer, scalable, hack, révolutionnaire, incroyable
– Affiliation toujours disclosée si présente

Intégration :
– Les CTA s'insèrent naturellement dans le flux de lecture
– Pas plus de 3 CTA dans un même article
– Ne pas doubler un CTA déjà présent et efficace
– Ne pas modifier la structure markdown (H1/H2/H3) sans nécessité absolue

FORMAT DE SORTIE
L'article complet avec les CTA injectés ou améliorés, en markdown.
Pas de commentaires éditoriaux, pas de résumé des changements.
Uniquement l'article amélioré.\
"""


# ---------------------------------------------------------------------------
# ConversionAuditResult — dataclass de résultat parsé
# ---------------------------------------------------------------------------


@dataclass
class ConversionAuditResult:
    """
    Résultat structuré d'un audit conversion schoolsWP.

    Produit par ConversionAuditorAgent.run() — parsé depuis la sortie LLM.

    Champs principaux :
        score_conversion   : score global /100
        clarte_probleme    : bloc 1 /20
        decision           : bloc 2 /20
        orientation_action : bloc 3 /20
        cta                : bloc 4 /20
        business_alignment : bloc 5 /20
        report             : rapport complet markdown
        article_with_cta   : article avec CTA injectés (mode audit_and_inject)
        injected           : True si injection CTA déclenchée
    """

    score_conversion: int = 0
    clarte_probleme: int = 0
    decision: int = 0
    orientation_action: int = 0
    cta: int = 0
    business_alignment: int = 0
    points_forts: list[str] = field(default_factory=list)
    faiblesses: list[str] = field(default_factory=list)
    recommandations: list[str] = field(default_factory=list)
    report: str = ""
    article_with_cta: str = ""
    injected: bool = False

    @property
    def diagnostic(self) -> str:
        """Interprétation schoolsWP du score conversion."""
        if self.score_conversion >= 95:
            return "Article business-ready"
        elif self.score_conversion >= 85:
            return "Optimisations mineures"
        elif self.score_conversion >= 70:
            return "Manque d'orientation action"
        else:
            return "SEO sans levier business"

    @property
    def diagnostic_emoji(self) -> str:
        if self.score_conversion >= 95:
            return "✅"
        elif self.score_conversion >= 85:
            return "🟡"
        elif self.score_conversion >= 70:
            return "🟠"
        else:
            return "🔴"

    @property
    def weakest_bloc(self) -> str:
        """Identifie le bloc le plus faible pour guider la correction."""
        scores = {
            "Clarté problème": (self.clarte_probleme, 20),
            "Logique décision": (self.decision, 20),
            "Orientation action": (self.orientation_action, 20),
            "CTA stratégique": (self.cta, 20),
            "Business alignment": (self.business_alignment, 20),
        }
        # Ratio score/max pour comparer à poids égal
        return min(scores, key=lambda k: scores[k][0] / scores[k][1])

    @classmethod
    def parse(cls, report: str) -> "ConversionAuditResult":
        """Parse le rapport markdown LLM en ConversionAuditResult structuré."""
        result = cls(report=report)

        # Score global
        m = re.search(r"Score Conversion\s*:\s*(\d+)/100", report, re.IGNORECASE)
        if m:
            result.score_conversion = int(m.group(1))

        # Blocs /20 — gère bold markdown `**NOM : X/20**`
        bloc_patterns = {
            "clarte_probleme":    r"\*{0,2}Clart[eé] probl[eè]me\s*:\s*(\d+)/20\*{0,2}",
            "decision":           r"\*{0,2}D[eé]cision\s*:\s*(\d+)/20\*{0,2}",
            "orientation_action": r"\*{0,2}Orientation action\s*:\s*(\d+)/20\*{0,2}",
            "cta":                r"\*{0,2}CTA\s*:\s*(\d+)/20\*{0,2}",
            "business_alignment": r"\*{0,2}Business alignment\s*:\s*(\d+)/20\*{0,2}",
        }
        for attr, pattern in bloc_patterns.items():
            m = re.search(pattern, report, re.IGNORECASE | re.MULTILINE)
            if m:
                setattr(result, attr, int(m.group(1)))

        # Points forts
        m = re.search(
            r"Points forts\s*:\s*\n((?:[\–\-•][^\n]+\n?)+)",
            report,
            re.IGNORECASE,
        )
        if m:
            result.points_forts = [
                re.sub(r"^[\–\-•]\s*", "", line).strip()
                for line in m.group(1).strip().splitlines()
                if line.strip()
            ]

        # Faiblesses
        m = re.search(
            r"Faiblesses\s*:\s*\n((?:[\–\-•][^\n]+\n?)+)",
            report,
            re.IGNORECASE,
        )
        if m:
            result.faiblesses = [
                re.sub(r"^[\–\-•]\s*", "", line).strip()
                for line in m.group(1).strip().splitlines()
                if line.strip()
            ]

        # Recommandations concrètes (numérotées)
        m = re.search(
            r"Recommandations\s+concrètes\s*:\s*\n((?:\d+\.[^\n]+\n?)+)",
            report,
            re.IGNORECASE,
        )
        if m:
            result.recommandations = [
                re.sub(r"^\d+\.\s*", "", line).strip()
                for line in m.group(1).strip().splitlines()
                if line.strip()
            ]

        return result

    def summary(self) -> str:
        """Résumé compact pour affichage CLI."""
        lines = [
            f"  Score Conversion   : {self.score_conversion}/100  "
            f"{self.diagnostic_emoji}  {self.diagnostic}",
            f"  Clarté problème    : {self.clarte_probleme}/20",
            f"  Décision           : {self.decision}/20",
            f"  Orientation action : {self.orientation_action}/20",
            f"  CTA stratégique    : {self.cta}/20",
            f"  Business alignment : {self.business_alignment}/20",
        ]
        if self.faiblesses:
            lines.append("")
            lines.append("  Faiblesses :")
            for f in self.faiblesses[:3]:
                lines.append(f"    – {f}")
        if self.recommandations:
            lines.append("")
            lines.append("  Recommandations :")
            for i, r in enumerate(self.recommandations[:3], 1):
                lines.append(f"    {i}. {r}")
        return "\n".join(lines)


# ---------------------------------------------------------------------------
# Agent d'injection CTA (privé)
# ---------------------------------------------------------------------------


class _CtaInjectorAgent(BaseContentAgent):
    """Injecte ou améliore les CTA pour atteindre >85/100 en conversion."""

    name = "conversion-cta-injector"
    system_prompt = _INJECT_SYSTEM

    async def run(  # type: ignore[override]
        self,
        article: str,
        audit_report: str,
        keyword: str,
        score: int,
    ) -> str:
        user_message = (
            f"Mot-clé principal : {keyword}\n"
            f"Score conversion actuel : {score}/100 — objectif : ≥ 85/100\n\n"
            "--- RAPPORT D'AUDIT CONVERSION ---\n\n"
            f"{audit_report}\n\n"
            "--- ARTICLE À AMÉLIORER ---\n\n"
            f"{article}"
        )
        response = await self._client.messages.create(
            model=self.model,
            max_tokens=6000,
            system=self.system_prompt,
            messages=[{"role": "user", "content": user_message}],
        )
        return response.content[0].text


# ---------------------------------------------------------------------------
# ConversionAuditorAgent — agent principal
# ---------------------------------------------------------------------------


class ConversionAuditorAgent(BaseContentAgent):
    """
    Module Score Conversion & CTA Layer — schoolsWP.

    Audite la couche business d'un article sur 5 blocs (5 × 20 pts = 100).

    Deux modes :

    Mode audit seul :
        result = await agent.run(article, keyword="lms wordpress rentable")
        print(result.score_conversion)   # 72
        print(result.diagnostic)         # "Manque d'orientation action"
        print(result.weakest_bloc)       # "CTA stratégique"

    Mode audit + injection CTA :
        result = await agent.audit_and_inject(article, keyword="...", threshold=85)
        if result.injected:
            # result.article_with_cta contient l'article avec CTA améliorés
            print(result.article_with_cta)
    """

    name = "conversion-auditor"
    system_prompt = _AUDIT_SYSTEM

    async def run(  # type: ignore[override]
        self,
        article: str,
        keyword: str,
        intent: str | None = None,
        objective: str | None = None,
    ) -> ConversionAuditResult:
        """
        Audite la couche conversion d'un article.

        Args:
            article   : Contenu markdown à auditer
            keyword   : Mot-clé SEO principal
            intent    : Intention de recherche (informationnelle/comparative/décisionnelle)
            objective : Objectif business prioritaire (email|affiliation|formation|offre)
                        Permet de pondérer l'analyse Business alignment.

        Returns:
            ConversionAuditResult avec score /100, 5 blocs /20, points forts/faiblesses,
            recommandations et propriétés diagnostic/weakest_bloc calculées automatiquement.
        """
        context_lines = [f"Mot-clé principal : {keyword}"]
        if intent:
            context_lines.append(f"Intention de recherche : {intent}")
        if objective:
            context_lines.append(f"Objectif business prioritaire : {objective}")

        user_message = (
            "\n".join(context_lines)
            + "\n\n--- ARTICLE À AUDITER ---\n\n"
            + article
        )
        response = await self._client.messages.create(
            model=self.model,
            max_tokens=2500,
            system=self.system_prompt,
            messages=[{"role": "user", "content": user_message}],
        )
        raw = response.content[0].text
        return ConversionAuditResult.parse(raw)

    async def audit_and_inject(
        self,
        article: str,
        keyword: str,
        intent: str | None = None,
        objective: str | None = None,
        threshold: int = 85,
    ) -> ConversionAuditResult:
        """
        Audit conversion + injection CTA automatique si score < threshold.

        Args:
            article   : Article à auditer
            keyword   : Mot-clé principal
            intent    : Intention de recherche (optionnel)
            objective : Objectif business prioritaire (optionnel)
            threshold : Score minimum pour éviter l'injection (défaut : 85)

        Returns:
            ConversionAuditResult. Si score < threshold : result.injected=True et
            result.article_with_cta contient l'article avec CTA améliorés.
            Sinon result.injected=False et result.article_with_cta="".
        """
        result = await self.run(
            article=article,
            keyword=keyword,
            intent=intent,
            objective=objective,
        )

        if result.score_conversion < threshold:
            injector = _CtaInjectorAgent(model=self.model)
            result.article_with_cta = await injector.run(
                article=article,
                audit_report=result.report,
                keyword=keyword,
                score=result.score_conversion,
            )
            result.injected = True

        return result
