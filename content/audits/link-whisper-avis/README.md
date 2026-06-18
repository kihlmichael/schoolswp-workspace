# Audit `link-whisper-avis`

- **URL** : <https://schoolswp.com/link-whisper-avis/>
- **Slug** : `link-whisper-avis`
- **Post ID** : 58166
- **Pillar** : SEO (maillage interne)
- **Type** : avis plugin affilié (code partenaire `schoolsWP10`)
- **Statut** : refonte-decidee (refresh léger recommandé, arbitrage final Michaël)

## Historique des snapshots

| Date | Trigger | Statut résultant | Synthèse |
| --- | --- | --- | --- |
| [2026-05-22](2026-05-22/synthese.md) | Demande Michaël - audit complet vraie data GSC/DataForSEO/thruuu (suite sprint refresh) | refonte-decidee | [synthese.md](2026-05-22/synthese.md) |

## Constat central de l'audit

Le sprint refresh `core/tasks/plans/linkwhisper-refresh-sprint.md` visait `linkwhisper avis`. La data GSC prouve que ce mot-clé est un **fantôme** : 0 impression mesurable sur 90 jours, 0 volume DataForSEO. La page y est déjà #2 pour rien.

Vraie cible : `link whisper` (390/mois, informationnel, position GSC actuelle 8,6) et `linkwhisper` (480/mois, navigationnel, position 20,6). Le contenu est compétitif (thruuu quasi tout vert, #2 SERP, 2567 mots). Le déficit est sur les **signaux** : 2 liens internes seulement, aucun rich result hors fil d'Ariane, crawl ancien.

**Recommandation : refresh léger ciblé (technique + signal, 3-4 h), pas la réécriture complète du brief.**

## Actions décidées

| # | Action | Effort | Statut | Référence |
| --- | --- | --- | --- | --- |
| 1 | Audit complet 4 sources (GSC + DataForSEO + thruuu + WP REST) | 2h | **fait** 2026-05-22 | `2026-05-22/` (18 fichiers) |
| 2 | Google Sheet volumes DataForSEO | 5 min | **fait** 2026-05-22 | [Sheet](https://docs.google.com/spreadsheets/d/1WfZf_tIQ_2UjmkWaBEVIcmbcsZ_a97edTEz0lI4Wug8/) |
| 3 | Arbitrage périmètre : refresh léger vs réécriture complète du brief | - | **à valider (Michaël)** | `core/tasks/plans/linkwhisper-rewrite-brief.md` à revoir |
| 4 | Maillage interne : ~6 -> ~14 liens internes contextuels (8-9 ajouts) | ~1h30 | **plan prêt** 2026-05-22 | `core/tasks/plans/linkwhisper-internal-linking-plan.md` |
| 5 | Titre SEO : retirer emoji + année figée, recibler `link whisper` | 15 min | à planifier | via Gutenberg/Rank Math |
| 6 | Schema Review/AggregateRating + FAQPage | ~1h | à planifier | URL inspection ne valide que Breadcrumbs |
| 7 | Enrichissement chirurgical : H2 « c'est quoi », H2 fonctionnalités, FAQ, encarts Kadence Option B (chiffres d'expérience réels) | ~1h30 | à planifier | réutiliser les chiffres validés du sprint |
| 8 | Signal fraîcheur : date MAJ + demande indexation GSC + IndexNow | 15 min | à planifier | post-publication |

## Métriques de suivi

| Métrique | Baseline 2026-05-22 | Cible prochain snapshot |
| --- | --- | --- |
| Position `link whisper` | 8,6 | top 5 |
| Position `linkwhisper` | 20,6 | top 10 |
| Clics page 90j | 3 | > 20 |
| Impressions page 90j | 1343 | maintien ou + |
| CTR page | 0,22 % | > 1,5 % |
| Rich results | Breadcrumbs seul | Breadcrumbs + Review + FAQ |
| Liens internes entrants | ~6 (GSC n'en listait que 2, échantillon partiel) | ~14 |

## Prochain snapshot prévu

- **Quand** : 4 à 6 semaines après le refresh (vers 2026-07-01)
- **Trigger** : post-refresh + monitoring Rank Math weekly
- **Comparaison** : générer `_diff.md` vs `2026-05-22/`

## Décisions connexes

1. **Sprint refresh à réorienter** - le brief `linkwhisper-rewrite-brief.md` (validé en session Cowork, Option B) repose sur la cible `linkwhisper avis` invalidée par cet audit. Les chiffres d'expérience réels et les encarts Kadence Option B restent réutilisables dans le refresh léger.
2. **Cluster maillage interne** - `/link-whisper-avis/` gagnerait à être relié au futur hub maillage interne / SEO (cf. articles `/slug-wordpress/`, `/seo-wordpress/` déjà liés).
