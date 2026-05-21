# Audits articles schoolsWP — Conventions

> Source de vérité pour le système d'audit/snapshots d'articles schoolsWP. Permet la comparaison entre dates et la traçabilité des décisions éditoriales.

## Principes

- **1 dossier par article** : nommé par le slug WordPress (ex: `masteriyo-lms-avis/`).
- **1 sous-dossier par snapshot daté** : format `YYYY-MM-DD/`. Un snapshot = un audit complet à un instant T.
- **Versionné git** : chaque snapshot reste figé une fois écrit. La comparaison entre dates passe par `git diff` ou un fichier `_diff.md` dédié.
- **Données brutes à côté de la synthèse** : on peut toujours rejouer l'analyse plus tard.

## Structure type

```text
content/audits/
├── CONVENTIONS.md                           # ce fichier
├── _registry.md                             # index global tous articles audités
└── <slug-article>/                          # ex: masteriyo-lms-avis
    ├── README.md                            # index article : statut + historique snapshots + actions
    ├── 2026-05-07/                          # snapshot daté
    │   ├── synthese.md                      # synthèse Claude exploitable (LE doc à lire)
    │   ├── article-current-snapshot.md      # contenu article au moment T (via defuddle)
    │   ├── gsc-90d.json                     # dump GSC 90 jours (queries + positions + impressions + clicks)
    │   ├── gsc-url-inspect.json             # inspection URL Google (indexation + rich results)
    │   ├── dataforseo-volume.json           # volumes mensuels FR
    │   ├── dataforseo-serp-fr.json          # SERP organique top 20 FR + PAA
    │   ├── dataforseo-keyword-suggestions.json  # suggestions seed
    │   ├── dataforseo-search-intent.json    # classification intent
    │   ├── dataforseo-google-sheet.csv      # source du Google Sheet des volumes (cf. section dédiée)
    │   └── thruuu-raw/                      # exports thruuu bruts (XLSX, PDF, HTML)
    │       ├── audit-article.<ext>
    │       └── serp-analysis.<ext>
    └── 2026-XX-XX/                          # snapshot suivant
        ├── synthese.md
        ├── _diff.md                         # delta vs snapshot précédent (positions, queries gagnées/perdues, structure article)
        └── ...
```

## Convention de nommage

| Élément | Format | Exemple |
| --- | --- | --- |
| Slug article | slug WordPress strict (sans année, sans "schoolswp") | `masteriyo-lms-avis` |
| Date snapshot | `YYYY-MM-DD` (jour de l'audit, pas date Rank Math) | `2026-05-07` |
| Synthèse | `synthese.md` (toujours ce nom) | - |
| Snapshot article | `article-current-snapshot.md` | - |
| Dumps APIs | `<source>-<scope>.json` | `gsc-90d.json`, `dataforseo-serp-fr.json` |
| Raw thruuu | sous-dossier `thruuu-raw/` | - |
| Diff inter-snapshots | `_diff.md` (préfixe underscore = méta-fichier) | - |

## Contenu attendu de `synthese.md`

Frontmatter minimal :

```yaml
---
slug: masteriyo-lms-avis
url: https://schoolswp.com/masteriyo-lms-avis/
date_snapshot: 2026-05-07
trigger: Rank Math weekly 2026-05-03 (-51 positions)
status: refonte-decidee | en-monitoring | publie | archive
---
```

Sections types (adapter selon contexte) :

1. **Contexte & déclencheur** : pourquoi cet audit maintenant
2. **Données collectées** : sources (GSC, DataForSEO, thruuu, lecture article) + dates
3. **État de l'article** : structure actuelle, longueur, sections, schema
4. **SEO actuel** : positions GSC, queries gagnantes/perdantes, CTR, schema effectif
5. **SERP analysée** : top 10 concurrents, intent dominant, format majoritaire
6. **Insights critiques** : 3-5 points actionnables
7. **Décision** : action retenue (refonte / 301 / désindex / statu quo / monitoring)
8. **Plan d'action** : étapes concrètes + effort estimé
9. **Métriques de suivi** : ce qu'on regarde au prochain snapshot

## Cycle d'un audit

1. **Trigger** : Rank Math weekly, GSC alerte, demande Michael, etc.
2. **Création snapshot** : `mkdir content/audits/<slug>/<date>/`
3. **Collecte données** :
   - GSC 90j queries + URL inspect
   - DataForSEO volume + SERP FR + suggestions + intent
   - thruuu SERP + audit article (export raw → `thruuu-raw/`). ⚠️ thruuu ne sait PAS scraper un article en **brouillon** : il récupère la page 404 du site (titre « 404 », ~30 mots). Pour un audit pré-publication, seul l'export **SERP** est exploitable ; l'audit page thruuu est à ignorer.
   - defuddle parse de l'URL → `article-current-snapshot.md` (ou `post_content` via Novamira si brouillon)
4. **Rédaction `synthese.md`** : analyse + décision + plan
5. **Mise à jour** :
   - `<slug>/README.md` (historique snapshots + statut)
   - `_registry.md` (index global)
   - **Google Sheet des volumes** : créer le Sheet DataForSEO sur le Drive Michael (cf. section dédiée)
6. **Si snapshot N+1** : créer `_diff.md` qui compare avec le snapshot précédent

## Comparaison entre snapshots

Trois niveaux de comparaison possibles :

1. **Diff git brutal** : `git diff content/audits/<slug>/2026-05-07/synthese.md content/audits/<slug>/2026-08-15/synthese.md`
2. **Diff structuré** : fichier `_diff.md` rédigé manuellement à la création du snapshot N+1, qui répond à 5 questions :
   - Quelles positions ont bougé ? (via comparaison `gsc-90d.json`)
   - Quelles queries gagnées / perdues ?
   - La SERP top 10 a-t-elle bougé ? (via `dataforseo-serp-fr.json`)
   - L'article a-t-il été modifié entre temps ? (via `article-current-snapshot.md`)
   - Les actions décidées au snapshot précédent ont-elles été exécutées ?
3. **Tableau de bord transverse** : regroupe les `_diff.md` de plusieurs articles dans `_registry.md` (vue macro).

## Tableau Google Sheets des volumes (livrable systématique)

À **chaque audit d'article**, créer un Google Sheet sur le Drive de Michael avec les données DataForSEO du champ sémantique : volumes FR, concurrence, CPC, difficulté SEO (KD), intention, tendance annuelle + historique mensuel 12 mois. Le CSV source est colocalisé dans le snapshot (`dataforseo-google-sheet.csv`).

- **Création** : via le connecteur Google Drive de claude.ai (`text/csv` → conversion auto en Sheet). La CLI `gws` est une alternative quand son auth fonctionne.
- **Nommage** : `schoolsWP - Volumes SEO - <sujet> - <YYYY-MM-DD>`.
- **Objectif final** : centraliser les données de tous les articles audités dans un **tableau commun de surveillance SEO** (une ligne ou un onglet par article). Pour l'instant : un Sheet par audit ; la consolidation viendra ensuite.

## Règle git

- Tout snapshot = commit dédié. Message convention : `audit(<slug>): snapshot <date> + decision <action>`
  - Exemple : `audit(masteriyo-lms-avis): snapshot 2026-05-07 + decision refonte`
- Les raw thruuu sont commités par défaut (XLSX/PDF, pas des secrets).
- Si raw > 10 MB par snapshot → bascule Git LFS ou stockage Drive avec lien dans `synthese.md`.

## Ce qu'on NE met PAS dans `content/audits/`

- Plans de refonte / briefs d'écriture → restent dans `content/decisions/`
- Articles publiés → restent dans `content/articles/<pillar>/`
- Sandbox / scratch / tests → `sandbox-workspace/` (gitignored)
- Secrets ou credentials → jamais

Le système d'audit est en lecture seule pour la stratégie : il observe, il ne pilote pas. Le pilotage reste dans `content/decisions/` et `core/tasks/`.
