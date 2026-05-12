---
name: chatseo-relations-extractor
description: |
  Extrait les entités nommées (NER) et leurs relations sémantiques depuis un titre + corps de page web, avec sortie JSON pure pour graphe de connaissances. Catégorise chaque entité (personne, organisation, marque, lieu, produit, concept) et identifie les prédicats sujet → objet avec extrait justificatif.
  Utilise ce skill quand l'utilisateur dit : "extrais les entités de cette page", "analyse NER de cet article", "construis un knowledge graph de ce contenu", ou fournit un titre + contenu ensemble pour un rapport JSON entités/relations (SEO sémantique, structuration NLP, schéma RDF-like).
  NE PAS utiliser pour : un brief sémantique FR multi-catégories à partir d'un mot-clé (utiliser `seo-semantique-fr`), audit SEO d'une page complète (utiliser `seo-page-audit`), ou clustering de mots-clés en cocons (utiliser `cocon-map-schoolswp` ou `cluster-cocon-automatique`).
---

# ChatSEO — Extracteur de relations vers JSON

Tu transformes un titre de page web et son contenu textuel en un rapport JSON structuré contenant deux ensembles : les entités nommées et les relations qui les lient.

L'objectif final : produire un graphe de connaissances exploitable (SEO sémantique, NLP, structuration de contenu).

## Entrées attendues

- `{TITRE_PAGE}` — le titre de la page web
- `{CONTENU_PAGE}` — le contenu textuel de la page web

Si l'une des deux entrées manque, demande-la avant d'analyser. N'invente jamais de contenu manquant.

## Pipeline d'analyse

Procède exactement dans cet ordre :

1. Identifier les entités nommées présentes dans le texte.
2. Catégoriser chaque entité.
3. Extraire les relations entre ces entités.
4. Classer chaque relation selon son type (prédicat).
5. Identifier la direction (sujet → objet) de chaque relation.
6. Pour chaque relation, isoler un extrait textuel justificatif issu directement du contenu fourni.
7. Générer le rapport JSON final.

## Types d'entités autorisés

Utilise uniquement ces types (au singulier, en minuscules) :

- `personne`
- `organisation`
- `entreprise`
- `lieu`
- `marque`
- `produit`
- `événement`
- `institution`
- `concept`
- `autre`

Si une entité ne rentre dans aucune des neuf premières catégories, classe-la en `autre`. N'invente pas de nouveaux types.

## Structure de sortie

La sortie est un objet JSON unique avec exactement deux clés racines : `entites` et `relations`.

```json
{
  "entites": [
    {
      "id": "E1",
      "nom": "Nom de l'entité",
      "type": "Type de l'entité"
    }
  ],
  "relations": [
    {
      "sujet": "E1",
      "predicat": "Type de relation",
      "objet": "E2",
      "contexte": "Extrait du texte qui justifie la relation"
    }
  ]
}
```

## Règles pour les entités

- Identifiants uniques au format `E1`, `E2`, `E3`, etc. — incrément continu, sans saut.
- Conserve uniquement les entités les plus importantes du texte.
- Plafond strict : 20 entités maximum.
- N'invente jamais d'entité absente du contenu fourni.
- Catégorise chaque entité de façon claire et univoque.
- Une même entité réelle = un seul ID. Si elle apparaît sous plusieurs formes (« Apple », « Apple Inc. »), regroupe-les sous une seule entrée et choisis la forme la plus complète comme `nom`.

## Règles pour les relations

Chaque relation contient quatre champs obligatoires : `sujet`, `predicat`, `objet`, `contexte`.

- Le `sujet` et l'`objet` doivent obligatoirement référencer un identifiant déjà présent dans `entites` (ex. `E1`, `E2`).
- La relation doit être clairement exprimée ou très fortement implicite dans le texte.
- N'inclus jamais de relation ambiguë, spéculative ou déduite par culture générale.
- Pas de doublons : une même triple (sujet, predicat, objet) n'apparaît qu'une fois.
- Plafond strict : 30 relations maximum.
- Priorise les relations les plus structurantes pour le sujet principal du texte.

### Choisir un bon prédicat

Le `predicat` doit être un verbe ou syntagme court qui décrit la nature de la relation. Privilégie des prédicats réutilisables.

Préférence générale : snake_case en français, sans déterminant, sans ponctuation.

### Typologie de relations canoniques (indicatif)

Quand le texte exprime un de ces patterns, réutilise le prédicat canonique pour garantir la cohérence du graphe entre plusieurs analyses. Cette liste n'est pas exhaustive — si le texte exprime une relation hors typologie, crée un prédicat ad hoc dans le même style.

| Sujet → Objet | Prédicat canonique | Exemple textuel |
|---|---|---|
| personne → organisation/entreprise | `travaille_pour` | « X est ingénieur chez Y » |
| personne → organisation/entreprise | `dirige` | « Y, PDG de X » |
| personne → organisation/entreprise | `fondé_par` (inverser : organisation → personne) | « X a été fondée par Y » |
| organisation/entreprise → lieu | `situé_à` | « Le siège de X est à Paris » |
| organisation/entreprise → produit | `développe` / `commercialise` | « X commercialise Y » |
| produit → organisation/entreprise | `conçu_par` | « Y, conçu par X » |
| entreprise → entreprise | `acquis_par` / `partenaire_de` / `concurrence` | « X a racheté Y » |
| personne → événement | `participe_à` / `organise` | « X intervient lors de Y » |
| produit → produit | `équipé_de` / `compatible_avec` | « X embarque Y » |
| organisation → concept | `utilise` / `développe` | « X mise sur le machine learning » |
| entité → date/période | `créé_en` | « Fondée en 2010 » |

Direction : respecte toujours le sens du texte. Si la phrase dit « Apple a racheté Beats », c'est `Beats acquis_par Apple` — donc `sujet=E_beats`, `objet=E_apple`. Ne force pas une direction qui contredit la formulation.

## Règles pour le contexte

- Le `contexte` est une **citation directe** issue du contenu fourni — pas une reformulation.
- Le plus court extrait possible qui justifie clairement la relation.
- Si plusieurs extraits conviennent, garde le plus explicite.
- Si aucun extrait textuel ne justifie la relation, ne crée pas la relation.

## Contraintes de sortie (impératives)

- Produis **uniquement** du JSON valide.
- **Aucun** texte avant le JSON.
- **Aucun** texte après le JSON.
- **Aucune** balise Markdown (` ``` `, `#`, etc.) autour du JSON.
- La réponse commence directement par `{` et se termine directement par `}`.
- Aucune information inventée. Base-toi exclusivement sur le contenu fourni.
- Si le contenu est trop court ou inexploitable, retourne quand même un JSON valide avec les tableaux vides : `{"entites": [], "relations": []}`.

## Exemple de référence

**Entrée :**

```
TITRE_PAGE : Apple présente le nouveau MacBook Pro à Cupertino
CONTENU_PAGE : Tim Cook, PDG d'Apple, a dévoilé le nouveau MacBook Pro lors d'un événement à Cupertino. Le produit est équipé de la puce M4, conçue par Apple. Le MacBook Pro sera commercialisé à partir de novembre.
```

**Sortie attendue (exactement ce format, rien autour) :**

```json
{
  "entites": [
    {"id": "E1", "nom": "Apple", "type": "entreprise"},
    {"id": "E2", "nom": "Tim Cook", "type": "personne"},
    {"id": "E3", "nom": "MacBook Pro", "type": "produit"},
    {"id": "E4", "nom": "Cupertino", "type": "lieu"},
    {"id": "E5", "nom": "puce M4", "type": "produit"}
  ],
  "relations": [
    {
      "sujet": "E2",
      "predicat": "dirige",
      "objet": "E1",
      "contexte": "Tim Cook, PDG d'Apple"
    },
    {
      "sujet": "E1",
      "predicat": "présente",
      "objet": "E3",
      "contexte": "Apple présente le nouveau MacBook Pro"
    },
    {
      "sujet": "E3",
      "predicat": "présenté_à",
      "objet": "E4",
      "contexte": "lors d'un événement à Cupertino"
    },
    {
      "sujet": "E3",
      "predicat": "équipé_de",
      "objet": "E5",
      "contexte": "Le produit est équipé de la puce M4"
    },
    {
      "sujet": "E5",
      "predicat": "conçu_par",
      "objet": "E1",
      "contexte": "la puce M4, conçue par Apple"
    }
  ]
}
```

## Cas d'usage typiques

- SEO sémantique et optimisation de cocon
- Extraction d'entités nommées (NER) sur page web
- Analyse NLP de contenu éditorial
- Structuration d'un corpus en triples sujet-prédicat-objet
- Construction de graphes de connaissances
- Cartographie des relations entre personnes, organisations, lieux, produits ou concepts d'un article
