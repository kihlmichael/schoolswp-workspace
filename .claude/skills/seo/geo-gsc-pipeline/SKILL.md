---
name: geo-gsc-pipeline
description: |
  Pipeline data-driven GSC-to-GEO : transforme des données réelles (export GSC CSV/XLSX, fichiers SERP Thruuu/SEOKey, ou accès API GSC) en système éditorial GEO complet V1+V2+V3 avec sortie JSON strict. Chaque décision est fondée sur des métriques observables (impressions, position, CTR), pas sur l'intuition.
  Utilise ce skill quand l'utilisateur dit : "analyse mes requêtes GSC", "j'ai un CSV GSC, fais-en un plan GEO", "priorise mes requêtes pour l'AIO", "transforme cet export en clusters GEO", "backlog éditorial depuis GSC", ou fournit un export GSC / fichier SERP avec demande de clustering data-driven.
  NE PAS utiliser pour : pipeline GEO sans données réelles depuis un seul mot-clé (utiliser `geo-architect`, sortie markdown), cartographie macro tous cocons (utiliser `cocon-map-schoolswp`), ou audit GSC de pilotage opérationnel sans construction GEO (utiliser le runbook `schoolswp-gsc-radar`).
---

# GEO GSC Pipeline — Donnees GSC vers Systeme Editorial GEO

## Pourquoi ce skill existe

Les exports GSC contiennent des centaines de requetes brutes, mais sans methode structuree, on finit par produire du contenu au feeling au lieu de capitaliser sur les signaux reels. Ce skill impose un pipeline reproductible en 3 phases (V1 filtrage, V2 clustering, V3 production) qui transforme des donnees mesurees en pages WordPress concues pour etre citees par les IA.

La difference avec `geo-architect` : ici, chaque decision est fondee sur des metriques observables (impressions, position, CTR), pas sur de l'intuition.

---

## Entrees attendues

L'utilisateur fournit un ou plusieurs de ces elements :

| Type | Format | Exemple |
|------|--------|---------|
| Export GSC brut | `.csv`, `.xlsx` | Export Performance > Requetes |
| Fichier SERP (Thruuu, SEOKey) | `.xlsx`, `.csv`, `.json` | `95_-_seokey_wordpress.xlsx` |
| Liste de mots-cles avec metriques | texte, CSV | `keyword, impressions, clicks, position` |
| Acces API GSC | MCP ou credentials | Propriete `sc-domain:schoolswp.fr` |

**Minimum requis** : au moins une source de donnees avec des requetes et idealement des metriques (impressions, clicks, position). Sans metriques, le pipeline fonctionne mais la priorisation sera moins fiable.

**Parametres a collecter** (demander si non fournis, puis continuer avec les valeurs par defaut) :

| Parametre | Defaut | Exemple |
|-----------|--------|---------|
| Propriete / domaine | — (obligatoire) | `schoolswp.fr` |
| Periode | 90 derniers jours | `60 derniers jours` |
| Pays | `ALL` | `FR` |
| Device | `ALL` | `desktop` |
| Nombre max de requetes | 1000 | `500` |

---

## Sorties produites

| Livrable | Format | Contenu |
|----------|--------|---------|
| Systeme GEO complet | JSON strict | V1 + V2 + V3 dans une seule structure |
| Dashboard editorial | Markdown | Vue d'ensemble, backlog priorise, actions suivantes |
| Pages AIO-ready | Markdown (1 par cluster P1/P2) | Specs de pages WordPress citation-ready |
| Liste Thruuu | CSV | Prompts PRIMARY + SECONDARY pour monitoring |

Le JSON est le livrable principal. Lire `references/output-schema.md` pour le schema exact.

---

## Pipeline en 4 phases

### Phase 0 — Extraction et preparation

**But** : charger les donnees brutes et les normaliser.

1. **Identifier la source** : fichier CSV/XLSX fourni, ou API GSC via MCP
2. **Extraire les colonnes utiles** : `query`, `clicks`, `impressions`, `ctr`, `position`, `page` (si dispo)
3. **Nettoyer** : supprimer doublons, requetes vides, lignes sans impression
4. **Trier** : par impressions decroissantes, puis par clics decroissants
5. **Limiter** : top N requetes (defaut 1000)

Si la source est un fichier SERP (Thruuu/SEOKey) plutot qu'un export GSC pur :
- Extraire les "Frequent Questions" (balises H2 SERP)
- Extraire les "Related Searches"
- Extraire les "People Also Ask"
- Estimer les metriques proportionnellement si les valeurs exactes ne sont pas disponibles (documenter l'estimation dans `meta.data_quality`)

### Phase V1 — Filtrage et normalisation

**But** : constituer la liste de primary prompts GEO qualifies.

**Filtres a appliquer** (dans l'ordre) :

| Filtre | Regle | Raison |
|--------|-------|--------|
| Intention exploitable | Garder INFO et COMM uniquement | Les requetes navigationnelles pures n'ont pas de potentiel GEO |
| Formulation question | Garder les requetes formulees comme questions OU facilement convertibles | Les IA citent des reponses a des questions |
| Long-tail | Privilegier ≥ 5 mots (sauf intention tres claire) | Plus specifique = plus citable |
| Brand-only | Eliminer les requetes brand pures sans intention | "wordpress.org" seul n'est pas exploitable |
| Trop vague | Eliminer les requetes sans sujet actionnable | "aide", "probleme" seuls ne guident rien |

**Regle de fidelite** : conserver le wording original de la requete GSC. Ne pas reformuler. Le `primary_prompt_geo` est une normalisation en langage naturel (ajout de "?", formulation complete) mais le sens et les mots doivent rester fideles.

**Pour chaque requete retenue, produire** :

```json
{
  "query_raw": "texte exact GSC",
  "primary_prompt_geo": "question en langage naturel fidele au wording",
  "intent": "INFO | COMM",
  "gsc_metrics": {
    "clicks": 0,
    "impressions": 0,
    "ctr": 0.0,
    "position": 0.0
  },
  "top_pages": [{"url": "...", "impressions": 0, "clicks": 0}]
}
```

### Phase V2 — Clustering canonique et priorisation

**But** : transformer la liste V1 en backlog editorial pilotable.

**Format de cluster strict** :

```
[Univers] / [Type] / [Intention] / [Objet]
```

**Univers** (choisir 1) :
`WP-Core` . `WP-Plugins` . `WP-SEO` . `WP-Performance` . `WP-Security` . `WP-Hosting` . `WP-Ecommerce` . `WP-LMS` . `WP-CRM` . `WP-Automation` . `WP-Builders` . `WP-Analytics` . `WP-Content` . `WP-Forms` . `WP-Translate` . `WP-Theme`

**Type** (choisir 1) :
`Guide` . `Comparatif` . `Checklist` . `Tutoriel` . `Avis` . `Pricing` . `Setup` . `Depannage` . `Alternatives` . `Template`

**Intention** : `INFO` ou `COMM`

**Objet** : court, explicite, sans jargon

**Regles de clustering** :
- 1 cluster canonique = 1 page pilier (anti-cannibalisation)
- Regrouper les prompts qui repondent a la meme intention editoriale
- Si 2 clusters se chevauchent : documenter dans `detected_overlap` et proposer MERGE

**Decision editoriale par cluster** :

| Decision | Quand | Signal |
|----------|-------|--------|
| `UPDATE` | Une page existante couvre deja le sujet | URL detectee dans `top_pages` GSC |
| `NEW` | Aucune page pertinente n'existe | Pas de page dans les donnees |
| `MERGE` | Plusieurs pages/clusters se chevauchent | Overlap detecte, risque cannibalisation |

**Priorisation** :

| Priorite | Critere principal | Critere secondaire |
|----------|-------------------|--------------------|
| `P1` | COMM + impressions elevees OU position 4-20 (opportunite) | Business fort (affiliation, conversion) |
| `P2` | INFO + fort volume OU COMM + volume moyen | Faisabilite elevee |
| `P3` | Niche, faible volume, ou faible urgence | Long terme |

**Regle absolue** : tout sujet COMM a fort potentiel = P1, sans exception.

### Phase V3 — Production AIO-ready (clusters P1, puis P2 si demande)

**But** : generer une spec de page WordPress concue pour etre citee par les IA.

**Structure obligatoire de chaque spec** :

1. **H1** — match le cluster canonique
2. **Reponse courte** (60-70 mots) — auto-contenue, citable, factuelle. C'est le bloc le plus cite en AIO.
3. **Sections H2/H3** (adapter selon le type de cluster) :
   - Definition / contexte
   - Solutions / methode (etapes numerotees)
   - Checklist
   - Erreurs frequentes / risques
   - Tableau comparatif (obligatoire si COMM ou choix entre options)
   - Recommandation assumee schoolsWP + justification
4. **FAQ GEO** — 8-12 questions tirees des prompts secondaires, avec reponses courtes
5. **Secondary prompts GEO** — 20-30 prompts classes par categorie :
   - `decisionnel` : choix, "lequel choisir", "faut-il"
   - `risque` : "que se passe-t-il si", "risques de"
   - `comparatif` : "X vs Y", "difference entre"
   - `solution` : "comment faire", "comment configurer"
   - `checklist` : "checklist pour", "etapes pour"
6. **Liste Thruuu** — prompts PRIMARY + SECONDARY prets pour upload monitoring

---

## Regles non negociables

| Regle | Raison |
|-------|--------|
| Fidelite GEO | Conserver le wording des requetes GSC — ne pas reinventer |
| 1 requete = 1 prompt | Pas de fusion, pas de paraphrase |
| Priorite COMM > INFO | Le business avant l'information pure |
| 1 cluster = 1 page pilier | Anti-cannibalisation stricte |
| JSON strict en sortie | Le systeme doit etre parsable par d'autres outils |
| Toujours schoolsWP | Marque, tutoiement, zero fluff |

---

## Format de sortie

La sortie finale est un objet JSON unique contenant 5 cles. Le schema exact est dans `references/output-schema.md` — le lire avant de produire la sortie.

Cles de premier niveau :
- `meta` — propriete, periode, filtres, qualite des donnees
- `v1_primary_prompts` — tableau de prompts GEO qualifies
- `v2_clusters` — tableau de clusters canoniques priorises
- `v3_pages_spec_p1` — tableau de specs AIO-ready (P1, puis P2 si demande)
- `questions_for_user` — questions pour l'iteration suivante

**En plus du JSON**, produire :
- 1 fichier Markdown "Dashboard editorial" (vue d'ensemble, backlog, actions)
- 1 fichier Markdown par page V3 (spec WordPress integrable)
- 1 fichier CSV "prompts Thruuu" (upload-ready)

---

## Exemple rapide

**Entree** : `95_-_seokey_wordpress.xlsx` (SERP analysis Thruuu)

**Phase 0** : 33 requetes extraites (Frequent Questions + Related Searches)
**V1** : 33 primary prompts qualifies (3 COMM, 30 INFO)
**V2** : 9 clusters canoniques (1 P1, 4 P2, 4 P3)
**V3** : 5 specs AIO-ready (P1 + P2)
**Thruuu** : 104 prompts (29 PRIMARY, 75 SECONDARY)

---

## Checklist qualite

### Avant de livrer V1
- [ ] Chaque `query_raw` est le texte exact de la source
- [ ] Chaque `primary_prompt_geo` est en langage naturel, fidele au wording
- [ ] Intention correctement taguee (INFO vs COMM)
- [ ] Requetes brand-only / trop vagues eliminees

### Avant de livrer V2
- [ ] Format cluster strict `[Univers] / [Type] / [Intention] / [Objet]`
- [ ] Tous les prompts V1 sont rattaches a un cluster
- [ ] Overlaps detectes et documentes
- [ ] Decisions UPDATE/NEW/MERGE coherentes
- [ ] P1 = tous les COMM a fort potentiel

### Avant de livrer V3
- [ ] Reponse courte 60-70 mots, auto-contenue, citable
- [ ] Tableau comparatif present si COMM
- [ ] FAQ 8-12 questions avec reponses courtes
- [ ] 20-30 secondary prompts classes par categorie
- [ ] Liste Thruuu complete (primary + secondary)

---

## Interaction avec les autres skills

| Skill | Quand l'utiliser en complement |
|-------|-------------------------------|
| `geo-architect` | Pour la phase creative (generation de variantes, ideation) quand les donnees GSC ne suffisent pas |
| `seo-audit` | Pour valider une page existante avant decision UPDATE |
| `schoolswp-article-workflow` | Pour produire l'article complet a partir de la spec V3 |
| `thruuu-writer` | Pour transformer un brief thruuu en article AIO-ready |
| `branding` | Pour verifier la conformite brand des specs V3 |
| `cluster-cocon-automatique` | Pour etendre un cluster en cocon semantique complet |

---

## Ressources bundled

| Fichier | Role | Quand le lire |
|---------|------|---------------|
| `references/output-schema.md` | Schema JSON complet avec descriptions de chaque champ | Avant de produire la sortie JSON |
