# Registry des audits articles schoolsWP

> Index global de tous les articles ayant fait l'objet d'un audit dans `content/audits/`. Mise à jour à chaque nouveau snapshot.
> Conventions : voir [CONVENTIONS.md](CONVENTIONS.md).

## Articles audités

| Slug                                                                                       | URL                                                                                                                                         | Premier audit | Dernier audit | Snapshots        | Statut                                           | Trigger initial                                                                     |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------- | ------------- | ------------- | ---------------- | ------------------------------------------------ | ----------------------------------------------------------------------------------- |
| [masteriyo-lms-avis](masteriyo-lms-avis/README.md)                                         | `/masteriyo-lms-avis/`                                                                                                                      | 2026-05-07    | 2026-05-07    | 1                | refonte-decidee                                  | Rank Math weekly 2026-05-03 (-51 pos)                                               |
| [tablepress-wp-table-builder-comparatif](tablepress-wp-table-builder-comparatif/README.md) | `?p=2881499` (brouillon)                                                                                                                    | 2026-05-14    | 2026-05-14    | 1                | refonte-decidee                                  | Demande Michael (audit pré-publication)                                             |
| [learn-wordpress-day](learn-wordpress-day/README.md)                                       | `/en/?p=2274708` (brouillon, EN)                                                                                                            | 2026-05-16    | 2026-05-16    | 1                | refonte-effectuee                                | Demande Michael (audit pré-publication)                                             |
| [ottokit-free-vs-pro](ottokit-free-vs-pro/README.md)                                       | `/ottokit-gratuit-vs-pro/` (publié, FR) + `/de/?p=2898734` (programmé, DE) + `/en/?p=2865102` (brouillon, EN)                               | 2026-05-19    | 2026-05-20    | 3 (DE + EN + FR) | bloc-3-applique (DE + EN) + bloc-4-applique (FR) | Demande Michael (audit multilingue)                                                 |
| [avis-rank-math](avis-rank-math/README.md)                                                 | `/avis-rank-math/` (publié, ID 2289943)                                                                                                     | 2026-05-20    | 2026-05-31    | 1                | publie                                           | Demande Michael (publié, FR)                                                        |
| [tablepress-3-3-wordpress-update](tablepress-3-3-wordpress-update/README.md)               | `/tablepress-3-3-mise-a-jour-wordpress/` (publié, FR) + `/de/?p=2898584` (programmé, DE) + `/en/?p=2898585` (programmé, EN)                 | 2026-05-20    | 2026-05-21    | 3 (DE + EN + FR) | refonte-effectuee (DE + EN) + publie (FR)        | Demande Michael (audit multilingue)                                                 |
| [copilhost-avis](copilhost-avis/README.md)                                                 | `/copilhost-hebergement-rapide-securise-pour-wordpress/` (publié, FR)                                                                       | 2026-05-28    | 2026-05-28    | 1                | publie                                           | Demande Michael (DataForSEO + Thruuu)                                               |
| [fluentcrm-vs-groundhogg](fluentcrm-vs-groundhogg/README.md)                               | post 2966750 (corbeille) → canonique `/comparatif-groundhogg-vs-fluentcrm/` (publié, 2511708)                                               | 2026-05-29    | 2026-05-29    | 1                | doublon-consolidé                                | Article auto-généré publié par erreur ; doublon du 2511708 → corbeille              |
| [code-promo-tutor-lms](code-promo-tutor-lms/README.md)                                     | `/creer-sa-plateforme-de-formation-en-ligne-avec-tutor-lms/` (publié, post 5843)                                                            | 2026-05-29    | 2026-05-29    | 1                | refonte-effectuee                                | Demande Michael (audit pré-publication série code-promo, pilote Tutor LMS)          |
| [thot-seo-avis](thot-seo-avis/README.md)                                                   | `/thot-seo-avis/` (publié, ID 57156)                                                                                                        | 2026-05-31    | 2026-05-31    | 1                | publie                                           | Choix Michael (Quick Win en Striking Distance)                                      |
| [fluent-forms](fluent-forms-meilleur-plugin-formulaires-wordpress/README.md)               | `/fluent-forms-meilleur-plugin-formulaires-wordpress/` (publié, ID 5063)                                                                    | 2026-05-31    | 2026-05-31    | 1                | publie                                           | Choix Michael (Quick Win en Striking Distance)                                      |
| [learn-wordpress-one-day](learn-wordpress-one-day/README.md)                               | doublons EN 2289537 + DE 2289536 → corbeille ; canoniques `/en/learn-wordpress-in-a-day/` (2274708) + `/de/wordpress-lernen-tag/` (2274709) | 2026-06-02    | 2026-06-02    | 1                | doublon-consolidé                                | Demande Michaël (audit pré-publication) - cannibalisation EN/DE → fusion (Option A) |
| [avis-booknetic-wordpress](avis-booknetic-wordpress/README.md)                             | `?p=2969996` (brouillon, FR)                                                                                                                | 2026-06-03    | 2026-06-03    | 1                | refonte-decidee                                  | Demande Michaël (audit pré-publication) - 5 bloquants, marché faible/déclinant      |
| [optimiser-wp-grid-builder-performance](optimiser-wp-grid-builder-performance/README.md)   | `?p=2969994` (brouillon, FR)                                                                                                                | 2026-06-04    | 2026-06-04    | 1                | refonte-decidee                                  | Demande Michaël (audit pré-publication, décision Option B : asset GEO standalone)   |
| [can-clickfunnels-be-useful-for-your-business](can-clickfunnels-be-useful-for-your-business/README.md) | `?p=1794972` (brouillon, EN)                                                                                                              | 2026-06-06    | 2026-06-06    | 1                | refonte-decidee                                  | Demande Michaël (Audit SEO + Thruuu)                                                |

## Statuts possibles

| Statut              | Sens                                                             |
| ------------------- | ---------------------------------------------------------------- |
| `audit-en-cours`    | Collecte de données pas terminée                                 |
| `a-arbitrer`        | Audit terminé, décision (ex: consolidation doublon) en attente   |
| `refonte-decidee`   | Décision prise, plan d'action en attente d'exécution             |
| `refonte-en-cours`  | Rédaction / réécriture en cours                                  |
| `refonte-effectuee` | Corrections appliquées côté serveur, attente publication humaine |
| `publie`            | Refonte poussée en prod, monitoring activé                       |
| `en-monitoring`     | Pas de refonte décidée, on surveille les positions               |
| `pause`             | Audit fait mais aucune action planifiée                          |
| `archive`           | Plus pertinent (article supprimé, fusionné, 301)                 |

## Triggers fréquents

- **Rank Math weekly** : rapport hebdo positions, baisse > 20 places
- **GSC alerte** : chute clics / impressions / CTR
- **Demande Michael** : audit explicite
- **Pre-publication** : audit avant publication d'un nouvel article concurrent (cluster check)
- **Routine pillar** : audit régulier des articles piliers (trimestriel)
- **Refonte stack** : changement de positionnement (ex: stack Tutor LMS → revue de tous les avis LMS)

## Fréquence de re-audit recommandée

| Type article           | Fréquence                                            |
| ---------------------- | ---------------------------------------------------- |
| Article pilier         | trimestriel                                          |
| Avis plugin affilié    | trimestriel + sur trigger Rank Math                  |
| Comparatif             | trimestriel + sur sortie nouvelle version concurrent |
| Article informationnel | annuel                                               |
| Article perdant (>50e) | mensuel jusqu'à décision                             |
