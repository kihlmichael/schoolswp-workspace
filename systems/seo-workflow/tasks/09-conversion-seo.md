# T9 — Conversion SEO

## Objectif

Transformer le trafic SEO existant en leads, affiliations et ventes via des CTA ciblés et des parcours de conversion optimisés.

## Outils clés

- Skill : `money-pages-framework` (existant dans `.claude/skills/`)
- Skill : `affiliation-optimizer` (existant dans `.claude/skills/`)
- Agent Python : `agents.conversion_auditor.cli`
- Google Sheets (onglet `09_Conversion`)

## Entrées exactes

- Top pages trafic (issues de `03_GSC`)
- Pages business à promouvoir (issues de `01_Inventory` : role_business = "affilie" ou "vente")
- `cluster_map.xlsx` (T5) : pour associer article → page business du même cluster
- `06_Linking` (T6) : pour aligner maillage interne et CTA

## Étapes

1. Cartographier : pour chaque cluster, lister 3 pages info à fort trafic + 2 pages business associées
2. Vérifier les CTA actuels sur les pages à fort trafic :
   - Newsletter générique sans lien avec le contenu → CTA générique = faible conversion
   - Absence de lien vers la page comparatif ou affiliée du même cluster
   - CTA trop tardif (uniquement en fin d'article)
3. Proposer des CTA ciblés par cluster (ex : "Téléchargez le guide WordPress performant" sur un article cache)
4. Définir 3 parcours de conversion principaux :
   - Parcours A : Article informatif → Comparatif affilié → Clic affilié
   - Parcours B : Article informatif → Newsletter → Séquence email → Offre
   - Parcours C : Guide pilier → Page contact/prestation → Lead
5. Prioriser par volume trafic × valeur business
6. Remplir `09_Conversion` + rédiger Doc `09_Conversion`

## Sorties attendues

**Fichier :** `conversion_map.xlsx`
**Destination :** Onglet `09_Conversion`

**Schéma CSV :**

```
url_source, intention_visiteur, objectif_business, cta_actuel, probleme_cta, cta_recommande, page_cible, parcours, priority
```

**Valeurs intention_visiteur :** informationnelle | comparative | transactionnelle | navigationnelle
**Valeurs objectif_business :** affiliation | lead | newsletter | vente | support
**Valeurs parcours :** A-affiliation | B-newsletter | C-lead

**Doc :** `09_Conversion.gdoc` — 3 parcours illustrés avec diagrammes simples

## Observables

- CTA visibles sur les pages à fort trafic (newsletter, boutons sociaux, liens affiliés)
- Présence ou absence de liens vers comparatifs affiliés dans les articles
- Position des CTA dans la structure de l'article (observable via lecture)

## Hypothèses à valider

- Taux de conversion actuel par CTA (À VALIDER via analytics ou FluentCRM)
- Taux d'inscription newsletter actuel (À VALIDER via FluentCRM ou Fluent Forms)
- CTR vers pages affiliées depuis articles (À VALIDER via analytics UTM)

## Dépendances

- **T3 obligatoire** : pages à fort trafic
- **T5 obligatoire** : association article → page business par cluster
- **T6 recommandé** : aligner maillage et CTA dans la même intervention

## KPIs

| KPI                                  | Baseline  | Objectif    |
| ------------------------------------ | --------- | ----------- |
| Pages P1 avec CTA ciblé              | À mesurer | 100%        |
| Taux inscription newsletter pages P1 | À VALIDER | +3-5 points |
| CTR vers pages affiliées             | À VALIDER | +2-4 points |

## Effort / Priorité

- Effort : M
- Priorité : **P2**

## Risques / Blocages

- Modification du template WordPress nécessaire → combiner avec T6 (maillage) dans une seule intervention sur les templates
- Pas de données analytics disponibles → travailler sur observables uniquement, noter toutes les conversions comme "À VALIDER"

## Intégration n8n

```
n8n (new post published trigger)
  → Function Node (vérifier présence CTA dans le contenu)
  → Notification Slack si CTA manquant
```

## Prompt agent IA

```
RÔLE : Tu es un consultant SEO/CRO spécialisé WordPress et affiliation pour schoolsWP.com.

OBJECTIF : Optimiser la monétisation du trafic SEO existant.

INPUTS :
- Pages à fort trafic (03_GSC)
- Pages business (01_Inventory role_business = affilie | vente | newsletter)
- cluster_map.xlsx (association article → page business)

ACTIONS (dans l'ordre) :
1. Pour chaque cluster : liste 3 pages info à fort trafic + 2 pages business associées
2. Vérifie les CTA actuels : présents, type, position, pertinence thématique
3. Identifie les CTA génériques à remplacer (newsletter sans lien avec le contenu)
4. Propose 1 CTA ciblé par article en cohérence avec l'intention et le cluster
5. Définit 3 parcours de conversion : A (affiliation), B (newsletter→email), C (lead)
6. Priorise par trafic × valeur business

RÈGLES DE PREUVE :
- Observable : CTA visibles sur les pages
- À VALIDER : taux de conversion, données analytics
- Ne jamais estimer une conversion sans données

FORMAT DE SORTIE :
- CSV : url_source, intention_visiteur, objectif_business, cta_actuel, probleme_cta, cta_recommande, page_cible, parcours, priority
- Doc 1-page : 3 parcours de conversion avec flux simplifié

CONDITIONS D'ARRÊT :
- Toutes les pages P1 (trafic >500 impressions) ont un CTA recommandé
- 3 parcours de conversion définis avec entrée et sortie claires
```
