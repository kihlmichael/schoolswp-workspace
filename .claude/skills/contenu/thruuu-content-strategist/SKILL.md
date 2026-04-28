---
name: thruuu-content-strategist
description: |
  Strategie de contenu SEO automatisee a partir des exports de clustering thruuu (XLSX).
  Analyse les clusters de mots-cles, determine les actions (creer/optimiser/ignorer), les formats
  (article, video, forum, outil), la priorite (P1-P3) et genere un rapport strategie + fichier Excel.
  Declenche ce skill pour : analyser un export thruuu, creer une strategie de contenu SEO,
  prioriser des clusters de mots-cles, generer un calendrier editorial SEO, ou produire
  un plan de contenu base sur des donnees SERP.
allowed-tools:
  - Read
  - Write
  - Edit
  - Bash
  - Glob
  - Grep
  - WebSearch
  - WebFetch
  - Agent
---

# thruuu Content Strategist

Transforme un export de clustering thruuu en strategie de contenu SEO priorisee et actionnable.

## Repertoire de travail

```
D:\VS Code\CLAUDE CODE\thruuu-claude-content-strategist\
├── input/                  <- deposer les exports thruuu (.xlsx)
│   └── processed/          <- fichiers traites (deplaces automatiquement)
├── output/                 <- rapports strategie (.md) et tableurs (.xlsx)
├── domains/                <- profils business sauvegardes (un .md par domaine)
└── CLAUDE.md               <- workflow complet (source de verite)
```

## Utilisation rapide

1. Deposer un export thruuu (.xlsx) dans `thruuu-claude-content-strategist/input/`
2. Lancer ce skill
3. Claude pose les questions de contexte business (1ere fois) puis analyse chaque cluster

## Workflow en 4 phases

### Phase 0 — Contexte business

1. Lire le fichier `.xlsx` dans `input/` (onglet Info : domaine, langue, localisation)
2. Verifier si un profil existe dans `domains/{domaine}.md`
   - Si oui : charger et confirmer avec l'utilisateur
   - Si non : interview rapide (activite, produits, audience, objectifs, concurrents)
3. Recherche `site:{domaine}` pour cartographier le contenu existant
4. Demander la capacite : nombre de pieces souhaitees (20/50/100) et rythme hebdo
5. Sauvegarder le profil dans `domains/`

### Phase 1 — Parsing et fondation

1. Lire l'onglet Topic Clusters : categories, topics, keywords, volumes, positions, URLs, PR, intent, features SERP (AIO%, Video%, Forum%, etc.)
2. Lire l'onglet Competitors : top 20 par visibilite clusters
3. Detecter les URLs dupliquees (meme URL pour plusieurs clusters)
4. Calculer les stats globales et presenter un resume avant analyse

### Phase 2 — Analyse strategique

Pour chaque cluster, determiner :

**Action** (raisonnement, pas formule) :

- Pas de Best URL → Create (sauf hors-sujet → Skip)
- Position <= 10 → No action (sauf mismatch d'intent)
- Position 10-20 → Optimize (verifier coherence URL/topic)
- Position > 20 → Optimize si meme sujet, Create si mismatch
- URL partagee entre clusters → identifier lesquels meritent leur propre page

**Format** (base sur les donnees SERP) :

- Video Feature % > 50% → Video (primaire ou complementaire)
- Forum Feature % eleve → Forum engagement (Reddit, Quora)
- Intent commercial/transactionnel → Article (+ video si signal fort)
- Sujet interactif → Free tool
- Combiner les formats quand les donnees le justifient

**Priorite** (ponderee par contexte business) :

- P1 : forte adequation produit + competition accessible + volume significatif
- P2 : bon fit mais competition plus dure, ou fit decent + volume modere
- P3 : backlog, valeur strategique limitee
- Monitor : couverture adequate ou effort non justifie

### Phase 3 — Livrables

**Rapport Markdown** → `output/{projet}_strategy.md` :

- Resume executif (insight cle en premier, stats ensuite, 2-3 alertes prioritaires)
- Tableau du plan de contenu (Topic, Action, Format, Priorite, Intent, Best URL, Position, Volume, Competition, Raisonnement)
- Calendrier editorial semaine par semaine
- Opportunites AIO (keywords a monitorer dans thruuu)
- Pages multi-clusters (ranking well vs. needs dedicated content)
- Clusters ignores + raisonnement

**Fichier Excel** → `output/{projet}_strategy.xlsx` :

- Tab 1 : Content Plan (colonnes detaillees)
- Tab 2 : Content Calendar (semaine, topic, action, format, priorite)
- Tab 3 : AIO Monitoring (un keyword par ligne pour copier-coller)
- Tab 4 : All Clusters Annotated (dataset complet + annotations Claude)

**Post-traitement** :

- Deplacer l'input vers `input/processed/`
- Resume des prochaines etapes

## Principes de contenu

- **Information Gain (80/20)** : 80% intent standard, 20% angle unique (experience, donnees originales)
- **Brand Anchoring** : importance de l'ancrage de marque pour la citation IA
- **E-E-A-T Human-First** : perspective personnelle et preuve sociale > compilation generique

## Regles strictes

- Ne PAS generer de nouveaux sujets — strictement base sur l'export
- Ne PAS suggerer de titres ou angles — recommander action/format/priorite uniquement
- Ne PAS presumer du statut de citation AIO — toujours dire "verifier avec thruuu"
- Ne PAS faire d'analyse concurrentielle par cluster — onglet Competitors = niveau agrege
- Verifier activement les % Video et Forum pour chaque cluster
- Les deux livrables (.md et .xlsx) sont obligatoires
- CTA systematique : "analyser dans thruuu + creer un brief"

## Lecture complete du workflow

Pour le workflow detaille avec tous les cas de figure, lire :
`D:\VS Code\CLAUDE CODE\thruuu-claude-content-strategist\CLAUDE.md`
