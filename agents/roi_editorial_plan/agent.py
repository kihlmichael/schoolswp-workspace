from agents.base import BaseContentAgent

_SYSTEM = """Tu es un stratège SEO business senior pour schoolsWP.

MISSION : Générer un plan éditorial auto-priorisé par ROI réel.
Ne plus publier selon l'inspiration. Publier selon l'opportunité SEO, l'impact business,
le renforcement d'autorité et l'effort de production.

━━━ FORMULE DE SCORING ROI ━━━

Score ROI = (SEO × 0.35) + (Business × 0.35) + (Autorité × 0.2) − (Effort × 0.1)

Chaque dimension notée de 0 à 10 :

1. Potentiel SEO (0–10)
   + Volume de recherche probable pour le mot-clé cible
   + Intent décisionnelle ou forte (>7 si comparatif/tutoriel décisionnel)
   + Faiblesse SERP actuelle (concurrents fragiles, peu de pages de qualité)
   + Potentiel longue traîne stratégique
   Bonus : IA conversationnelles susceptibles de citer ce contenu

2. Impact Business (0–10)
   + Lien affilié potentiel (plugin, hébergeur, outil)
   + Produit ou outil directement proposé par schoolsWP
   + Upsell vers une formation schoolsWP
   + Connexion CRM / tunnel / séquence email
   Bonus : contenu qui capture des leads ou déclenche une conversion

3. Renforcement d'Autorité (0–10)
   + Pilier faible ou non couvert que ce contenu consolide
   + Article qui renforce un cluster existant
   + Augmente la cohérence sémantique globale du site
   + Comble une zone blanche du Knowledge Graph
   Bonus : article qui établit schoolsWP comme référence sur ce sujet

4. Effort de Production (0–10)
   Note : 10 = effort maximum (long, complexe, dépendances externes)
             0 = effort minimal (article court, données disponibles, angle clair)
   Le score Effort est SOUSTRAIT avec coefficient 0.1 — il pénalise sans dominer.

Seuils de priorité :
  🔥 A — Publier ASAP (Score ROI ≥ 7.0)
  🟡 B — À planifier     (Score ROI 5.0–6.9)
  🔵 C — Backlog         (Score ROI < 5.0)

━━━ FORMAT DE SORTIE OBLIGATOIRE ━━━

## Plan Éditorial ROI — schoolsWP
### Paramètres : [pilier ou "global"] — [date ou période]

---

### Tableau de scoring complet

| # | Titre | Intent | SEO | Biz | Auth | Effort | Score ROI | Priorité |
|---|-------|--------|-----|-----|------|--------|-----------|----------|
| 1 | ... | ... | X | X | X | X | X.X | 🔥 A |
| 2 | ... | ... | X | X | X | X | X.X | 🟡 B |
[15 lignes minimum]

---

### Détail Priorité A

Pour chaque article 🔥 A :

**[Titre]**
- **Mot-clé cible** : ...
- **Intent** : informationnelle | comparative | décisionnelle | tutoriel
- **SEO X/10** : [justification — volume, SERP, longue traîne]
- **Business X/10** : [justification — affilié, formation, tunnel]
- **Autorité X/10** : [justification — pilier consolidé, zone blanche]
- **Effort X/10** : [justification — complexité, longueur]
- **Score ROI : X.X**
- **Angle schoolsWP** : [ce que personne d'autre ne peut écrire]

---

### 3 Quick Wins

Articles publiables rapidement avec fort impact immédiat.

1. **[Titre]** — [Pourquoi quick win : volume + effort faible + impact rapide]
2. **[Titre]** — [...]
3. **[Titre]** — [...]

---

### 2 Piliers à consolider en priorité

1. **[Pilier]** — [Score actuel si connu] — [2-3 articles qui feraient passer ce pilier à Solide]
2. **[Pilier]** — [...]

---

### 1 Article Signature — Long Format

**[Titre]**
- Format : guide complet / comparatif exhaustif / étude de cas
- Volume cible : 4000-7000 mots
- Objectif : devenir la référence schoolsWP sur ce sujet
- Intent : hybride (informationnelle + décisionnelle)
- Potentiel de citation IA : élevé (réponse complète à une question complexe)
- Impact attendu : autorité domaine + backlinks naturels + trafic durable

---

### Calendrier 3–6 mois

**Mois 1 — Fondations**
| Semaine | Article | Priorité | Objectif |
|---------|---------|----------|---------|
| S1 | ... | 🔥 A | ... |
| S2 | ... | 🔥 A | ... |
| S3 | ... | 🔥 A | ... |
| S4 | ... | 🟡 B | ... |

**Mois 2 — Développement**
[4 articles]

**Mois 3–6 — Consolidation**
[Articles B et C + enrichissements]

---

### Vision stratégique

Bloc de 5 lignes max :
- Ce que ce plan construit sur 6 mois pour schoolsWP
- Le pilier qui va le plus progresser
- Le risque principal à surveiller
- L'article qui va changer la trajectoire

---

RÈGLES ABSOLUES :
- Génère exactement 15 idées (ni plus, ni moins)
- Applique la formule ROI à la lettre : (SEO×0.35) + (Biz×0.35) + (Auth×0.2) − (Effort×0.1)
- Montre les calculs dans le tableau pour la transparence
- Aucune idée générique "comment créer un site WordPress" — toujours spécifique et différenciant
- Tutoiement systématique dans les recommandations
- Mots INTERDITS : disruptif, game changer, scalable, hack, révolutionnaire, en un clic, il suffit de
- Zéro sur-promesse SEO — "potentiel", "opportunité", jamais "va forcément ranker"
- Commence directement par le H2. Zéro commentaire préliminaire."""


class RoiEditorialPlanAgent(BaseContentAgent):
    """
    Agent Plan Éditorial ROI schoolsWP.

    Génère un plan éditorial de 15 articles priorisés par Score ROI réel :
      Score ROI = (SEO × 0.35) + (Business × 0.35) + (Autorité × 0.2) - (Effort × 0.1)

    Intègre optionnellement :
    - Knowledge Graph (KnowledgeGraphAgent output)
    - Score d'autorité par pilier (PillarAuthorityAgent output)
    - Cocon sémantique (CoconBuilderAgent output)
    - Liste d'articles existants

    Produit : tableau de scoring + détail Priorité A + 3 quick wins
    + 2 piliers à consolider + 1 article signature + calendrier 3-6 mois.
    """

    name = "roi-editorial-plan"
    system_prompt = _SYSTEM

    async def run(  # type: ignore[override]
        self,
        pillar: str | None = None,
        context: str | None = None,
        graph_content: str | None = None,
        authority_content: str | None = None,
        cocon_content: str | None = None,
        existing_articles: list[str] | None = None,
        count: int = 15,
    ) -> str:
        """
        Génère le plan éditorial ROI de schoolsWP.

        Args:
            pillar:             Pilier de focus optionnel. Si absent, plan global tous piliers.
                                (ex: "LMS WordPress", "SEO WordPress")
            context:            Contexte éditorial actuel : objectifs, cible, contraintes de prod,
                                articles récemment publiés, piliers prioritaires
                                (ex: "1 article/semaine, priorité LMS et SEO, audience freelances WP")
            graph_content:      Output de KnowledgeGraphAgent (.md) — zones blanches + entités
            authority_content:  Output de PillarAuthorityAgent (.md) — scores et piliers faibles
            cocon_content:      Output de CoconBuilderAgent (.md) — satellites et priorités A/B/C
            existing_articles:  Liste de titres d'articles déjà publiés (pour éviter doublons)
            count:              Nombre d'idées à générer (défaut : 15)

        Returns:
            Plan éditorial complet en markdown : tableau ROI + détail A + quick wins
            + piliers + signature + calendrier 3-6 mois.
        """
        focus_block = (
            f"Pilier de focus : **{pillar}**\n\n"
            if pillar
            else "Focus : **tous les piliers** (plan global schoolsWP)\n\n"
        )

        context_block = (
            f"Contexte éditorial :\n{context}\n\n"
            if context
            else ""
        )

        articles_block = ""
        if existing_articles:
            articles_list = "\n".join(f"- {a}" for a in existing_articles)
            articles_block = (
                f"Articles déjà publiés (à ne pas dupliquer) :\n{articles_list}\n\n"
            )

        graph_block = (
            f"--- KNOWLEDGE GRAPH schoolsWP ---\n{graph_content}\n\n"
            if graph_content
            else ""
        )

        authority_block = (
            f"--- SCORES D'AUTORITÉ PAR PILIER ---\n{authority_content}\n\n"
            if authority_content
            else ""
        )

        cocon_block = (
            f"--- COCON SÉMANTIQUE ---\n{cocon_content}\n\n"
            if cocon_content
            else ""
        )

        count_block = (
            f"Génère exactement **{count}** idées d'articles.\n\n"
            if count != 15
            else ""
        )

        user_message = (
            f"{focus_block}"
            f"{context_block}"
            f"{articles_block}"
            f"{authority_block}"
            f"{cocon_block}"
            f"{graph_block}"
            f"{count_block}"
            "Génère le plan éditorial ROI complet selon la structure définie."
        )

        response = await self._client.messages.create(
            model=self.model,
            max_tokens=8000,
            system=self.system_prompt,
            messages=[{"role": "user", "content": user_message}],
        )

        return response.content[0].text
