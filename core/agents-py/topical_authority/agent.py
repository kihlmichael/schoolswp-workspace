"""
Module Topical Authority Engine — schoolsWP

Score d'autorité thématique /100 sur 5 dimensions.
Passe d'un article isolé à un signal d'expertise structuré.

Google et les LLM favorisent :
  – Cohérence sémantique
  – Couverture complète d'un sujet
  – Profondeur structurée
  – Interconnexion logique
  – Expertise démontrée

Un article fort isolé = faible autorité.
Un cluster cohérent = signal expert perçu.

5 blocs × 20 pts :
  1. Couverture du sujet      — profondeur, sous-thèmes couverts/manquants
  2. Connexions internes      — opportunités de maillage vers d'autres contenus
  3. Cohérence sémantique     — champ lexical, absence de dilution
  4. Positionnement expert    — différenciation, angle stratégique, valeur ajoutée
  5. Potentiel cluster        — pilier / satellite / exploitable en série

Mode expand : génère les titres, angles et H2 des articles satellites identifiés.

Usage programmatique :
    agent = TopicalAuthorityAgent()
    result = await agent.run(article, keyword="lms wordpress rentable")
    print(result.score_autorite, result.diagnostic)
    print(result.role)        # "Pilier" | "Satellite" | "À renforcer"
    print(result.satellites)  # liste des articles cluster recommandés

    # Audit + plan d'expansion cluster
    result = await agent.audit_and_expand(article, keyword="...", pillar="LMS")
"""

from __future__ import annotations

import re
from dataclasses import dataclass, field

from agents.base import BaseContentAgent

# ---------------------------------------------------------------------------
# Prompt d'audit autorité thématique
# ---------------------------------------------------------------------------

_AUDIT_SYSTEM = """\
Tu es un analyste SEO senior spécialisé Topical Authority pour schoolsWP.

CONTEXTE schoolsWP
schoolsWP est une plateforme WordPress créée par Michael KIHL.
Public cible : freelances WordPress, formateurs en ligne, solopreneurs.
5 piliers thématiques : SEO WordPress | LMS & Formation | CRM & Email | Performance | Automatisation.
Concurrent de référence : WPMarmite (généraliste, fort DR).
Différenciation schoolsWP : approche terrain, systèmes cohérents, pas de tutos isolés.

MISSION
Analyser le contenu fourni et évaluer son intégration dans une stratégie
d'autorité thématique WordPress.

Attribuer un score sur 100 selon 5 dimensions.

━━━ 5 BLOCS D'AUDIT (20 pts chacun) ━━━

1️⃣ COUVERTURE DU SUJET (20 pts)
Évaluer :
– Le sujet principal est-il traité en profondeur (pas survol) ?
– Les sous-thèmes essentiels sont-ils présents ?
– Y a-t-il des angles obligatoires non couverts (gaps critiques) ?
– La couverture est-elle suffisante pour signaler l'expertise sur ce domaine ?
– La profondeur dépasse-t-elle ce que retourne une recherche SERP générique ?
Pénalités : sujet effleuré sans profondeur (−8), angle principal absent (−6),
gaps évidents non signalés (−5), couverture inférieure aux concurrents SERP (−6)

2️⃣ CONNEXIONS INTERNES (20 pts)
Évaluer :
– Combien d'opportunités de maillage interne sont identifiables ?
– Y a-t-il des liens logiques vers d'autres sujets WordPress couverts ou à couvrir ?
– L'article peut-il recevoir des liens entrants d'autres articles du cluster ?
– Les connexions sont-elles thématiquement pertinentes (pas artificielles) ?
– Le contenu fait-il référence à des ressources complémentaires (même implicitement) ?
Pénalités : aucune connexion possible (−8), article en silo complet (−7),
liens existants hors-sujet (−4), opportunités évidentes non exploitées (−5)

3️⃣ COHÉRENCE SÉMANTIQUE (20 pts)
Évaluer :
– Le champ lexical est-il cohérent et dense sur le sujet central ?
– Y a-t-il dilution sémantique (sujets parasites sans lien fort) ?
– Les entités nommées (outils, plugins, concepts) sont-elles cohérentes avec le sujet ?
– Le vocabulaire est-il celui de l'expert ou du généraliste ?
– Les termes SEO (entités) sont-ils suffisamment variés pour couvrir l'intention ?
Pénalités : champ lexical pauvre (−6), dilution sémantique marquée (−7),
entités hors-sujet (−4), vocabulaire généraliste non expert (−5)

4️⃣ POSITIONNEMENT EXPERT (20 pts)
Évaluer :
– Y a-t-il un angle différenciant qui n'existe pas dans les résultats SERP génériques ?
– La perspective schoolsWP (terrain, système, solopreneurs) est-elle visible ?
– Y a-t-il des données propriétaires, retours terrain ou exemples exclusifs ?
– L'article exprime-t-il un point de vue ou reste-t-il dans la synthèse générique ?
– La valeur ajoutée est-elle immédiatement perceptible par le lecteur cible ?
Pénalités : contenu purement générique sans angle (−8), aucune perspective terrain (−6),
pas de valeur ajoutée perceptible (−5), fusion avec ce que retourne le SERP (−6)

5️⃣ POTENTIEL CLUSTER (20 pts)
Évaluer :
– L'article peut-il devenir la page pilier d'un cluster de 5-10 contenus ?
– Ou s'intègre-t-il naturellement comme satellite d'un pilier existant ?
– Peut-il soutenir d'autres articles (liens entrants, contexte, concepts socles) ?
– Est-il exploitable en série (newsletter, LinkedIn, FAQ, YouTube) ?
– Sa position dans l'écosystème schoolsWP est-elle claire ?
Pénalités : aucun potentiel d'extension identifiable (−8), trop spécifique pour être pilier
sans être suffisamment satellite (−5), exploitabilité en série impossible (−4),
position floue dans l'écosystème (−5)

━━━ FORMAT DE SORTIE OBLIGATOIRE ━━━

Score Autorité : XX/100

Détail :
Couverture : X/20
Connexions : X/20
Cohérence : X/20
Positionnement : X/20
Potentiel cluster : X/20

Manques identifiés :
– [manque 1 — critique ou secondaire]
– [manque 2]
– [manque 3]

Opportunités de cluster :
– Article satellite 1 : [titre exact proposé | angle | lien logique avec le pilier]
– Article satellite 2 : [titre exact proposé | angle | lien logique]
– Article satellite 3 : [titre exact proposé | angle | lien logique]

Recommandation stratégique : [Pilier | Satellite fort | À renforcer | Contenu isolé]
Justification : [1-2 phrases de justification]

Respecte strictement ce format — les scores et recommandations sont parsés automatiquement.\
"""

# ---------------------------------------------------------------------------
# Prompt d'expansion cluster (mode --expand)
# ---------------------------------------------------------------------------

_EXPAND_SYSTEM = """\
Tu es un architecte de contenu senior pour schoolsWP.

CONTEXTE
Tu as reçu un article et le rapport d'audit Topical Authority qui l'accompagne.
Ta mission : produire le plan complet du cluster sémantique autour de cet article.

RÈGLES schoolsWP
– Tutoiement systématique dans tous les titres et descriptions
– Pas de titres génériques copiables sur n'importe quel blog
– Chaque satellite doit avoir un angle exclusif schoolsWP (terrain, système, solopreneur)
– Mots interdits : disruptif, game changer, scalable, hack, révolutionnaire

━━━ FORMAT DE SORTIE ━━━

# Plan Cluster — [Sujet]

## Pilier
**Titre** : [titre exact H1]
**Slug** : [slug-kebab-case]
**Angle** : [angle différenciant en 1 phrase]
**H2 principaux** : [liste des H2 du pilier]

## Satellites recommandés (5-8 articles)

### Satellite 1
**Titre** : [titre exact]
**Intent** : informationnelle | comparative | décisionnelle
**Angle schoolsWP** : [ce qui le différencie]
**Lien vers pilier** : [comment il renvoie au pilier]
**H2 suggérés** : [3-4 H2]

[Répéter pour chaque satellite]

## Maillage interne
Tableau : Article → Renvoie vers → Ancre suggérée

## Ordre de production
1. [article 1 — pourquoi en premier]
2. [article 2 — pourquoi en deuxième]
[...]

Uniquement le plan, sans introduction ni conclusion éditoriaux.\
"""


# ---------------------------------------------------------------------------
# TopicalAuditResult — dataclass de résultat parsé
# ---------------------------------------------------------------------------


@dataclass
class TopicalAuditResult:
    """
    Résultat structuré d'un audit Topical Authority schoolsWP.

    Produit par TopicalAuthorityAgent.run() — parsé depuis la sortie LLM.

    Champs principaux :
        score_autorite     : score global /100
        couverture         : bloc 1 /20
        connexions         : bloc 2 /20
        coherence          : bloc 3 /20
        positionnement     : bloc 4 /20
        potentiel_cluster  : bloc 5 /20
        manques            : sous-thèmes/angles absents
        satellites         : articles cluster recommandés
        recommandation     : "Pilier" | "Satellite fort" | "À renforcer" | "Contenu isolé"
        justification      : explication de la recommandation
        report             : rapport complet markdown
        cluster_plan       : plan d'expansion cluster (mode audit_and_expand)
        expanded           : True si expansion cluster déclenchée
    """

    score_autorite: int = 0
    couverture: int = 0
    connexions: int = 0
    coherence: int = 0
    positionnement: int = 0
    potentiel_cluster: int = 0
    manques: list[str] = field(default_factory=list)
    satellites: list[str] = field(default_factory=list)
    recommandation: str = ""
    justification: str = ""
    report: str = ""
    cluster_plan: str = ""
    expanded: bool = False

    @property
    def diagnostic(self) -> str:
        """Interprétation schoolsWP du score autorité."""
        if self.score_autorite >= 95:
            return "Article pilier"
        elif self.score_autorite >= 85:
            return "Satellite fort"
        elif self.score_autorite >= 70:
            return "Renforcement cluster nécessaire"
        else:
            return "Contenu isolé"

    @property
    def diagnostic_emoji(self) -> str:
        if self.score_autorite >= 95:
            return "✅"
        elif self.score_autorite >= 85:
            return "🟢"
        elif self.score_autorite >= 70:
            return "🟡"
        else:
            return "🔴"

    @property
    def role(self) -> str:
        """Rôle dans l'écosystème schoolsWP."""
        r = self.recommandation.lower()
        if "pilier" in r and "satellite" not in r:
            return "Pilier"
        elif "satellite" in r:
            return "Satellite"
        elif "renforcer" in r or "renforcement" in r:
            return "À renforcer"
        else:
            return "Contenu isolé"

    @classmethod
    def parse(cls, report: str) -> "TopicalAuditResult":
        """Parse le rapport markdown LLM en TopicalAuditResult structuré."""
        result = cls(report=report)

        # Score global
        m = re.search(r"Score Autorit[eé]\s*:\s*(\d+)/100", report, re.IGNORECASE)
        if m:
            result.score_autorite = int(m.group(1))

        # Blocs /20 — gère bold markdown
        bloc_patterns = {
            "couverture": r"\*{0,2}Couverture\s*:\s*(\d+)/20\*{0,2}",
            "connexions": r"\*{0,2}Connexions\s*:\s*(\d+)/20\*{0,2}",
            "coherence": r"\*{0,2}Coh[eé]rence\s*:\s*(\d+)/20\*{0,2}",
            "positionnement": r"\*{0,2}Positionnement\s*:\s*(\d+)/20\*{0,2}",
            "potentiel_cluster": r"\*{0,2}Potentiel cluster\s*:\s*(\d+)/20\*{0,2}",
        }
        for attr, pattern in bloc_patterns.items():
            m = re.search(pattern, report, re.IGNORECASE | re.MULTILINE)
            if m:
                setattr(result, attr, int(m.group(1)))

        # Manques identifiés
        m = re.search(
            r"Manques identifi[eé]s\s*:\s*\n((?:[\–\-•][^\n]+\n?)+)",
            report,
            re.IGNORECASE,
        )
        if m:
            result.manques = [
                re.sub(r"^[\–\-•]\s*", "", line).strip() for line in m.group(1).strip().splitlines() if line.strip()
            ]

        # Opportunités de cluster — lignes "– Article satellite N : ..."
        m = re.search(
            r"Opportunit[eé]s de cluster\s*:\s*\n((?:[\–\-•][^\n]+\n?)+)",
            report,
            re.IGNORECASE,
        )
        if m:
            result.satellites = [
                re.sub(r"^[\–\-•]\s*Article satellite\s*\d+\s*:\s*", "", line).strip()
                for line in m.group(1).strip().splitlines()
                if line.strip()
            ]

        # Recommandation stratégique
        m = re.search(
            r"Recommandation strat[eé]gique\s*:\s*([^\n]+)",
            report,
            re.IGNORECASE,
        )
        if m:
            result.recommandation = m.group(1).strip()

        # Justification (ligne après recommandation)
        m = re.search(
            r"Justification\s*:\s*([^\n]+(?:\n(?![\–\-#])[^\n]+)*)",
            report,
            re.IGNORECASE,
        )
        if m:
            result.justification = m.group(1).strip()

        return result

    def summary(self) -> str:
        """Résumé compact pour affichage CLI."""
        lines = [
            f"  Score Autorité      : {self.score_autorite}/100  {self.diagnostic_emoji}  {self.diagnostic}",
            f"  Rôle recommandé     : {self.role}",
            f"  Couverture sujet    : {self.couverture}/20",
            f"  Connexions internes : {self.connexions}/20",
            f"  Cohérence sémantique: {self.coherence}/20",
            f"  Positionnement      : {self.positionnement}/20",
            f"  Potentiel cluster   : {self.potentiel_cluster}/20",
        ]
        if self.manques:
            lines.append("")
            lines.append("  Manques identifiés :")
            for m in self.manques[:3]:
                lines.append(f"    – {m}")
        if self.satellites:
            lines.append("")
            lines.append("  Satellites recommandés :")
            for s in self.satellites[:3]:
                lines.append(f"    → {s}")
        if self.justification:
            lines.append("")
            lines.append(f"  Justification : {self.justification}")
        return "\n".join(lines)


# ---------------------------------------------------------------------------
# Agent d'expansion cluster (privé)
# ---------------------------------------------------------------------------


class _ClusterExpanderAgent(BaseContentAgent):
    """Génère le plan complet du cluster sémantique autour de l'article."""

    name = "topical-cluster-expander"
    system_prompt = _EXPAND_SYSTEM

    async def run(  # type: ignore[override]
        self,
        article: str,
        audit_report: str,
        keyword: str,
        pillar: str | None,
    ) -> str:
        context_lines = [f"Mot-clé principal : {keyword}"]
        if pillar:
            context_lines.append(f"Pilier thématique schoolsWP : {pillar}")

        user_message = (
            "\n".join(context_lines)
            + "\n\n--- RAPPORT D'AUDIT TOPICAL AUTHORITY ---\n\n"
            + audit_report
            + "\n\n--- ARTICLE ---\n\n"
            + article
        )
        return await self.call_llm(user_message, max_tokens=4000)


# ---------------------------------------------------------------------------
# TopicalAuthorityAgent — agent principal
# ---------------------------------------------------------------------------


class TopicalAuthorityAgent(BaseContentAgent):
    """
    Module Topical Authority Engine — schoolsWP.

    Score d'autorité thématique /100 sur 5 dimensions.

    Deux modes :

    Mode audit seul :
        result = await agent.run(article, keyword="lms wordpress")
        print(result.score_autorite)   # 82
        print(result.diagnostic)       # "Renforcement cluster nécessaire"
        print(result.role)             # "Satellite"
        for s in result.satellites:
            print(s)

    Mode audit + expansion cluster :
        result = await agent.audit_and_expand(
            article, keyword="lms wordpress", pillar="LMS & Formation"
        )
        if result.expanded:
            print(result.cluster_plan)  # plan complet pilier + satellites
    """

    name = "topical-authority"
    system_prompt = _AUDIT_SYSTEM

    async def run(  # type: ignore[override]
        self,
        article: str,
        keyword: str,
        intent: str | None = None,
        pillar: str | None = None,
    ) -> TopicalAuditResult:
        """
        Audite l'autorité thématique d'un article.

        Args:
            article : Contenu markdown à auditer
            keyword : Mot-clé SEO principal
            intent  : Intention de recherche (optionnel)
            pillar  : Pilier thématique schoolsWP (SEO|LMS|CRM|Performance|Automatisation)
                      Permet de contextualiser l'analyse des connexions internes.

        Returns:
            TopicalAuditResult avec score /100, 5 blocs /20, manques, satellites
            et recommandation Pilier/Satellite/À renforcer/Contenu isolé.
        """
        context_lines = [f"Mot-clé principal : {keyword}"]
        if intent:
            context_lines.append(f"Intention de recherche : {intent}")
        if pillar:
            context_lines.append(f"Pilier thématique schoolsWP : {pillar}")

        user_message = "\n".join(context_lines) + "\n\n--- ARTICLE À AUDITER ---\n\n" + article
        raw = await self.call_llm(user_message, max_tokens=2500)
        return TopicalAuditResult.parse(raw)

    async def expand_cluster(
        self,
        article: str,
        existing_result: TopicalAuditResult,
        keyword: str,
        pillar: str | None = None,
    ) -> str:
        """
        Génère le plan cluster à partir d'un audit DÉJÀ effectué.

        Évite un LLM call redondant quand l'audit topical a déjà été exécuté
        (typiquement par PublishReadyAgent). Réutilise le rapport existant.

        Args:
            article         : Article source
            existing_result : TopicalAuditResult déjà calculé
            keyword         : Mot-clé principal
            pillar          : Pilier thématique schoolsWP (optionnel)

        Returns:
            Plan cluster markdown (pilier + satellites + maillage + ordre de production).
        """
        expander = _ClusterExpanderAgent(model=self.model)
        return await expander.run(
            article=article,
            audit_report=existing_result.report,
            keyword=keyword,
            pillar=pillar,
        )

    async def audit_and_expand(
        self,
        article: str,
        keyword: str,
        intent: str | None = None,
        pillar: str | None = None,
    ) -> TopicalAuditResult:
        """
        Audit autorité + plan d'expansion cluster.

        Le plan cluster est toujours généré (pas de condition sur le score),
        car même un article fort a besoin de son plan cluster documenté.

        Args:
            article : Article à auditer
            keyword : Mot-clé principal
            intent  : Intention de recherche (optionnel)
            pillar  : Pilier thématique schoolsWP (optionnel)

        Returns:
            TopicalAuditResult. result.expanded=True et result.cluster_plan
            contient le plan complet (pilier + satellites + maillage + ordre de production).
        """
        result = await self.run(
            article=article,
            keyword=keyword,
            intent=intent,
            pillar=pillar,
        )

        expander = _ClusterExpanderAgent(model=self.model)
        result.cluster_plan = await expander.run(
            article=article,
            audit_report=result.report,
            keyword=keyword,
            pillar=pillar,
        )
        result.expanded = True

        return result
