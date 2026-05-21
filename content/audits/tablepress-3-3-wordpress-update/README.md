# Audit - tablepress-3-3-wordpress-update

Index article. Conventions : voir [../CONVENTIONS.md](../CONVENTIONS.md).

- **Requête cible** : TablePress 3.3 (cluster : tablepress, tablepress wordpress, wordpress table plugin)
- **Trio Polylang** : FR 2678035 (publié) / DE 2898584 (programmé) / EN 2898585 (programmé)
- **Statut DE** : refonte-effectuee (corrections appliquées côté serveur, attente publication)
- **Statut EN** : refonte-effectuee (toutes les corrections appliquées le 2026-05-21, tableau Ninja Tables EN inclus)
- **Statut FR** : publie (audit formel + corrections appliquées le 2026-05-21 ; article classé #3 sur google.fr)

## Historique des snapshots

| Date | Langue | Synthèse | Trigger | Décision |
| --- | --- | --- | --- | --- |
| 2026-05-20 | DE | [2026-05-20/synthese.md](2026-05-20/synthese.md) | Demande Michael (audit pré-publication, article DE) | FIX THEN GO - 2 bloquants + corrections appliqués le 2026-05-20 |
| 2026-05-21 | EN | [2026-05-21/synthese.md](2026-05-21/synthese.md) | Demande Michael (audit pré-publication, article EN) | FIX THEN GO - 3 bloquants + 4 importants, corrections appliquées le 2026-05-21 |
| 2026-05-21-fr | FR | [2026-05-21-fr/synthese.md](2026-05-21-fr/synthese.md) | Demande Michael (audit formel de l'article FR publié) | OPTIMISATION CONTINUE - 6 corrections appliquées le 2026-05-21 (pas de refonte, article #3) |

## Actions - DE (post 2898584)

- [x] **Bloquant 1** - corps converti au tutoiement allemand (Duzen). 41 corrections, « Sie/Ihre/Ihnen » -> « du/dein », « wir » -> « ich ». Seul « Sie bleibt » conservé (pronom de la barre d'outils, pas du vouvoiement) - **FAIT le 2026-05-20**.
- [x] **Bloquant 2** - lien interne cassé remplacé par `/de/ninja-tables-datatables-grosse-datensaetze/` (DE, publié) - **FAIT le 2026-05-20**.
- [x] **Important** - lien vers la source officielle `de.wordpress.org/plugins/tablepress/` ajouté (1re mention, `_blank` `rel=noopener`) - **FAIT le 2026-05-20**.
- [x] **Moyen** - mention « WordPress 7.0 » clarifiée (préparation au futur WP 7.0 + prérequis WordPress 6.7) dans le corps et la FAQ - **FAIT le 2026-05-20**.
- [x] **Faible** - mention TablePress 3.3.1 ajoutée ; `id` d'ancrage des 5 H2 traduits en allemand - **FAIT le 2026-05-20**.
- [x] Métadonnées : titre SEO Rank Math et extrait convertis au tutoiement - **FAIT le 2026-05-20**.
- [x] Tableau Ninja Tables dupliqué en DE (table 2920728) ; image à la une (hero éditorial DE, attachment 2920710) ; logo officiel TablePress en tête (attachment 2920791) - **FAIT le 2026-05-21**.
- [x] **Transverse E/D** - dernière mention « WordPress 7.0 » surfaite (« vollständige Kompatibilität », para après H2#1) requalifiée + H3 vide « Warum dieses Update deinen Alltag verändert » supprimé - **FAIT le 2026-05-21**. (Défaut H : DE déjà au bon format « für geübte Nutzer um fast 30 % », aucune action.)
- [ ] **Captures d'écran** - 2-3 captures réelles de l'écran d'édition TablePress 3.3 à fournir par Michael.
- [ ] **Recalcul Rank Math** - ouvrir le post dans Gutenberg et cliquer Update pour rafraîchir le score.
- [ ] **Publication** - en attente du feu vert de Michael, puis vérifier les liens Polylang FR/DE/EN.

Sauvegarde `post_content` pré-corrections : postmeta `_audit_backup_content_20260520` sur le post 2898584
(md5 original `7b3176417950569f92d64508fb48360b`).

## Actions - EN (post 2898585)

Décision FIX THEN GO du 2026-05-21. Plan détaillé : [2026-05-21/synthese.md](2026-05-21/synthese.md) §8.
Corrections appliquées le 2026-05-21 via WP REST (push canonique `POST /wp/v2/posts`, blocs vérifiés intacts).

- [x] **Bloquant A** - titre du bloc table des matières `"Sommaire de l'article"` -> `"In this article"` - **FAIT le 2026-05-21**.
- [x] **Bloquant B** - lien interne cassé `ninja-tables-vs-tablepress-comparatif` (404) -> `/en/ninja-tables-datatables-large-datasets/` (post 2865114), ancre EN - **FAIT le 2026-05-21**.
- [x] **Bloquant C** - tableau Ninja Tables EN créé (table **2922940**, colonnes Version / Script size / Load time / CPU load, 3 lignes traduites) via Novamira ; `tableId` du bloc + shortcode `[ninja_tables]` mis à jour (2858338 -> 2922940) - **FAIT le 2026-05-21**.
- [x] **Important D** - H3 vide *« Why this update changes your daily routine »* supprimé - **FAIT le 2026-05-21**.
- [x] **Important E** - 6 mentions prose « WordPress 7.0 » clarifiées (préparation au futur WP 7.0 + prérequis WP 6.7) dans chapô, intro, corps et FAQ ; extrait + meta description Rank Math corrigés - **FAIT le 2026-05-21**.
- [x] **Important F** - lien vers la source officielle `wordpress.org/plugins/tablepress/` ajouté (1re mention, `_blank` `rel=noopener`) - **FAIT le 2026-05-21**.
- [x] **Moyen G** - lien interne cassé réparé (1 lien EN solide). Maillage EN supplémentaire (*Elementor*, *FastPixel*) volontairement non forcé, faute d'ancre naturelle - cohérent avec la version DE.
- [x] **Moyen H** - statistique « 30 % » requalifiée en « almost 30% for experienced users » (chapô aligné sur l'encadré Tip) - **FAIT le 2026-05-21**.
- [x] **Moyen I** - image à la une : hero éditorial EN dédié (attachment **2922768**, texte anglais) - **FAIT le 2026-05-21**.
- [x] **Moyen J** - logo officiel TablePress en tête d'article (attachment **2922770**, alt anglais, copyright TablePress / Tobias Bäthge) - **FAIT le 2026-05-21**.
- [x] **Moyen K** - FAQ *« We strongly recommend »* -> *« I strongly recommend »* - **FAIT le 2026-05-21**.
- [x] **Faible M/N** - mention TablePress 3.3.1 ajoutée ; `id` d'ancrage des 5 H2 traduits en anglais - **FAIT le 2026-05-21**.
- [ ] **Faible L/O** - captures d'écran (à fournir par Michael) ; resserrage des phrases de remplissage (non bloquant, non traité).
- [ ] **Recalcul Rank Math** - ouvrir le post dans Gutenberg et cliquer Update (le push REST ne relance pas l'analyse JS).
- [ ] **Publication** - en attente du feu vert de Michael, puis vérifier les liens Polylang FR/DE/EN.

Sauvegarde `post_content` pré-corrections : [2026-05-21/article-raw-blocks.html](2026-05-21/article-raw-blocks.html)
(snapshot original versionné). Contenu post-corrections : `2026-05-21/_en-corrected-content.html`.

> **Défauts transverses traités le 2026-05-21** sur le **FR publié** (2678035) et le **DE** (2898584) :
> mention « WordPress 7.0 » requalifiée (E), statistique « 30 % » requalifiée en « près de 30 % pour
> les utilisateurs expérimentés » (H, FR uniquement - le DE l'était déjà), H3 vide supprimé (D).
> **Conversion vouvoiement vers tutoiement de tout l'article FR** appliquée dans la foulée (30 occurrences :
> pronoms, possessifs, impératifs, conjugaisons + extrait + meta description Rank Math). Le trio FR/DE/EN
> est désormais aligné sur E, H, D et le registre de marque (tutoiement).

## Actions - FR (post 2678035)

Audit formel du 2026-05-21 : [2026-05-21-fr/synthese.md](2026-05-21-fr/synthese.md). Décision
**OPTIMISATION CONTINUE** (article classé #3 sur google.fr, pas de refonte). Corrections via WP REST
(push canonique) + Novamira pour la lecture serveur.

- [x] **Pré-audit (2026-05-21)** - défauts transverses E (« WordPress 7.0 »), H (stat « 30 % »),
  D (H3 vide) corrigés + **conversion complète au tutoiement** (30 occurrences) + extrait et meta
  description Rank Math.
- [x] **Bloquant B** - lien interne cassé `ninja-tables-vs-tablepress-comparatif` (404) -> `/ninja-tables-datatables-seo-guide/` (post 2592793) - **FAIT le 2026-05-21**.
- [x] **Important C** - lien vers la source officielle `fr.wordpress.org/plugins/tablepress/` ajouté (1re mention, `_blank` `rel=noopener`) - **FAIT le 2026-05-21**.
- [x] **Moyen G** - maillage interne : ajout du lien vers le guide `/wordpress-7-nouveautes-guide-complet/` (ancre naturelle dans la section WordPress 7.0) - **FAIT le 2026-05-21**.
- [x] **Moyen I** - image à la une : hero éditorial FR dédié (attachment **2923375**, texte français) en remplacement de l'ancienne image générique 2858314 - **FAIT le 2026-05-21**.
- [x] **Moyen J** - logo officiel TablePress en tête d'article (attachment **2923388**, alt français, copyright TablePress / Tobias Bäthge) - **FAIT le 2026-05-21**.
- [x] **Faible M** - mention TablePress 3.3.1 ajoutée - **FAIT le 2026-05-21**.
- [ ] **Faible F** - captures d'écran (à fournir par Michael).
- [ ] **Recalcul Rank Math** - ouvrir le post dans Gutenberg, recharger, cliquer Update (le push REST ne relance pas l'analyse JS).

Contenu pré-corrections du jour : `2026-05-21/_fr-live-content.html` (avant E/H/D) puis
`2026-05-21/_fr-tutoiement-content.html` (avant audit). Contenu post-audit : `2026-05-21-fr/_fr-audit-corrected-content.html`.

> **Défauts transverses traités le 2026-05-21** sur le **FR publié** (2678035) et le **DE** (2898584) :
> mention « WordPress 7.0 » requalifiée (E), statistique « 30 % » requalifiée (H, FR uniquement -
> le DE l'était déjà), H3 vide supprimé (D), + conversion vouvoiement vers tutoiement du FR.
> Le trio FR/DE/EN est aligné sur E, H, D, le registre de marque et les défauts B/C/I/J/M.

## Livrables data

### Snapshot DE - 2026-05-20

- `2026-05-20/synthese.md`, `article-current-snapshot.md`, dumps DataForSEO (volume, serp-de, suggestions, intent), `dataforseo-google-sheet.csv`, `thruuu-raw/serp-analysis.xlsx`.
- Google Sheet : [schoolsWP - Volumes SEO - TablePress 3.3 (DE) - 2026-05-20](https://docs.google.com/spreadsheets/d/1khBfFmtTGlmDtzDHzPFqtBeHb7jUZZulaI0to5gWtAs/edit).

### Snapshot EN - 2026-05-21

- `2026-05-21/synthese.md` - synthèse, décision, plan d'action (16 actions).
- `2026-05-21/article-current-snapshot.md` - rendu lisible du brouillon EN ; `article-raw-blocks.html` - blocs source.
- `2026-05-21/dataforseo-volume.json` - volumes keyword_overview (US/English).
- `2026-05-21/dataforseo-serp-us.json` - SERP google.com (US) « TablePress 3.3 » (live).
- `2026-05-21/dataforseo-keyword-suggestions.json` - champ sémantique « tablepress » (60 suggestions).
- `2026-05-21/dataforseo-search-intent.json` - classification d'intention.
- `2026-05-21/dataforseo-google-sheet.csv` - source du Google Sheet des volumes.
- `2026-05-21/thruuu-raw/serp-analysis.xlsx` - export thruuu brut (google.com US).
- Google Sheet : [schoolsWP - Volumes SEO - TablePress 3.3 (EN) - 2026-05-21](https://docs.google.com/spreadsheets/d/1cIdlcFoXfHkIqtTHlHnogT9-qPY52CXgRjM_LFLYNug/edit).

### Snapshot FR - 2026-05-21-fr

- `2026-05-21-fr/synthese.md` - synthèse, décision OPTIMISATION CONTINUE, plan d'action (8 actions).
- `2026-05-21-fr/article-current-snapshot.md` - rendu lisible de l'article FR ; `article-raw-blocks.html` - blocs source.
- `2026-05-21-fr/dataforseo-volume.json` - volumes keyword_overview (France/français).
- `2026-05-21-fr/dataforseo-serp-fr.json` - SERP google.fr « TablePress 3.3 » (live, article #3).
- `2026-05-21-fr/dataforseo-keyword-suggestions.json` - champ sémantique « tablepress » (60 suggestions).
- `2026-05-21-fr/dataforseo-search-intent.json` - classification d'intention.
- `2026-05-21-fr/gsc-28d.json` - GSC search analytics 28 j de l'URL (publiée le 2026-05-13).
- `2026-05-21-fr/gsc-url-inspect.json` - inspection URL Google (indexée, PASS).
- `2026-05-21-fr/dataforseo-google-sheet.csv` - source du Google Sheet des volumes.
- `2026-05-21-fr/thruuu-raw/serp-analysis.xlsx` - export thruuu SERP google.fr (Location France, Language fr ; scrape 2026-05-20 ; fourni le 2026-05-21). Confirme la SERP DataForSEO et révèle la double présence schoolsWP en page 1 (article #3 + page catégorie #7).
- Google Sheet : [schoolsWP - Volumes SEO - TablePress 3.3 (FR) - 2026-05-21](https://docs.google.com/spreadsheets/d/16POHMHhQQmFQILo4tskLjFIyU-5ZQMVQf4_V_okVFx4/edit).
