# Audit `masteriyo-lms-avis`

- **URL** : <https://schoolswp.com/masteriyo-lms-avis/>
- **Slug** : `masteriyo-lms-avis`
- **Pillar** : LMS
- **Statut** : refonte-pushed-2026-05-07 (post_id 2040881, content md5 `54fa2f457cd815653bc1c52558f41c6b`)
- **Décision retenue** : Option D - Refonte chirurgicale (voir `content/decisions/masteriyo-arbitrage-2026-05-06.md`)

## Historique des snapshots

| Date | Trigger | Statut résultant | Synthèse |
| --- | --- | --- | --- |
| [2026-05-07](2026-05-07/synthese.md) | Rank Math weekly 2026-05-03 (-51 positions, 76e) | refonte-decidee | [synthese.md](2026-05-07/synthese.md) |

## Actions décidées

| # | Action | Effort | Statut | Référence |
| --- | --- | --- | --- | --- |
| 1 | Backup HTML article actuel | 5 min | **fait** 2026-05-07 | `content/articles/lms/_backup/2026-05-07_masteriyo-lms-avis-original.html` (97 KB) |
| 2 | Vérifier programme affilié Themeum (Tutor LMS Pro) | 10 min | à faire (externe Michael) | - |
| 3 | Préparer snippet migration Masteriyo vers Tutor | 30 min | **fait** 2026-05-07 | `content/decisions/masteriyo-arbitrage-2026-05-06_migration-snippet-draft.md` |
| 4 | Refonte chirurgicale 11 sections + section 9-bis | ~4h | **PUSHED 2026-05-07 13:59 UTC** post_id 2040881 | MD : `content/articles/lms/masteriyo-lms-avis-refonte-v1.md` (4362 mots) + HTML Gutenberg : `..._gutenberg-ready.html` (45 KB) + Push via Novamira (md5 match 54fa2f...). Reste à faire manuellement par Michael : Rank Math title/meta/focus kw/schema Review (saisie sidebar Gutenberg, cf. mémoire `feedback_rank_math_via_plugin_only.md`) + insertion 3 CTAs Kadence (placeholders en commentaires HTML) |
| 5 | Investiguer Review schema | 30 min | **fait diagnostic** 2026-05-07 | `content/decisions/masteriyo-arbitrage-2026-05-06_schema-review-snippet.md` |
| 5-bis | Pousser le schema Review (Option A manuel ou B mu-plugin) | 15 min | à faire | snippet schema prêt à coller |
| 6 | Audit thruuu (SERP + audit article 2 variations kw) | externe | **fait** 2026-05-07 | 4 fichiers dans `2026-05-07/thruuu-raw/` + extraits MD + intégré dans `synthese.md` section 5 |
| 7 | Auditer schema Review sur autres articles d'avis schoolsWP | 1h | à planifier (mission `audit-schema-review-tous-articles-avis`) | bug probablement systémique |

## Métriques de suivi (post-refonte)

| Métrique | Baseline 2026-05-07 | Cible J+90 |
| --- | --- | --- |
| Position "masteriyo lms" | 4,5 | 1-3 |
| Position "masteriyo lms avis" | 76e (Rank Math) | top 10 |
| Position "masteriyo" | 7,4 | 3-5 |
| CTR moyen | 0 % | 3-8 % |
| Clicks 90j | 0 | 4-10 / mois |
| Impressions 90j | 124 | 200+ |
| Rich result Review | non détecté | détecté |
| Conversions affiliate Tutor LMS Pro | 0 | tracking ClickWhale |

## Prochain snapshot prévu

- **Quand** : J+30 post-refonte (après publication) puis J+60, J+90
- **Trigger** : automatique post-refonte + monitoring Rank Math weekly
- **Comparaison** : générer `_diff.md` vs `2026-05-07/`

## Décisions connexes

1. **Slug `/tutor-lms-avis/` à libérer** — l'article principal Tutor LMS est sur `/creer-sa-plateforme-de-formation-en-ligne-avec-tutor-lms/`. Migration future vers slug court.
2. **Article `/tutor-lms-vs-masteriyo/` dédié** — pillar comparatif Q3 2026.
3. **Audit cluster LMS perdants** — Tunnel de vente WordPress (-41), EasyCommerce Avis (-25), SEOKEY (-33). Mission `cluster-perdants-arbitrage` à planifier.
