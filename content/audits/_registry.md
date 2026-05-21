# Registry des audits articles schoolsWP

> Index global de tous les articles ayant fait l'objet d'un audit dans `content/audits/`. Mise à jour à chaque nouveau snapshot.
> Conventions : voir [CONVENTIONS.md](CONVENTIONS.md).

## Articles audités

| Slug | URL | Premier audit | Dernier audit | Snapshots | Statut | Trigger initial |
| --- | --- | --- | --- | --- | --- | --- |
| [masteriyo-lms-avis](masteriyo-lms-avis/README.md) | `/masteriyo-lms-avis/` | 2026-05-07 | 2026-05-07 | 1 | refonte-decidee | Rank Math weekly 2026-05-03 (-51 pos) |
| [tablepress-wp-table-builder-comparatif](tablepress-wp-table-builder-comparatif/README.md) | `?p=2881499` (brouillon) | 2026-05-14 | 2026-05-14 | 1 | refonte-decidee | Demande Michael (audit pré-publication) |
| [learn-wordpress-day](learn-wordpress-day/README.md) | `/en/?p=2274708` (brouillon, EN) | 2026-05-16 | 2026-05-16 | 1 | refonte-effectuee | Demande Michael (audit pré-publication) |
| [ottokit-free-vs-pro](ottokit-free-vs-pro/README.md) | `/ottokit-gratuit-vs-pro/` (publié, FR) + `/de/?p=2898734` (programmé, DE) + `/en/?p=2865102` (brouillon, EN) | 2026-05-19 | 2026-05-20 | 3 (DE + EN + FR) | bloc-3-applique (DE + EN) + bloc-4-applique (FR) | Demande Michael (audit multilingue) |
| [avis-rank-math](avis-rank-math/README.md) | `?p=2289943` (brouillon, FR) | 2026-05-20 | 2026-05-20 | 1 | refonte-decidee | Demande Michael (audit pré-publication) |
| [tablepress-3-3-wordpress-update](tablepress-3-3-wordpress-update/README.md) | `/tablepress-3-3-mise-a-jour-wordpress/` (publié, FR) + `/de/?p=2898584` (programmé, DE) + `/en/?p=2898585` (programmé, EN) | 2026-05-20 | 2026-05-21 | 3 (DE + EN + FR) | refonte-effectuee (DE + EN) + publie (FR) | Demande Michael (audit multilingue) |

## Statuts possibles

| Statut | Sens |
| --- | --- |
| `audit-en-cours` | Collecte de données pas terminée |
| `refonte-decidee` | Décision prise, plan d'action en attente d'exécution |
| `refonte-en-cours` | Rédaction / réécriture en cours |
| `refonte-effectuee` | Corrections appliquées côté serveur, attente publication humaine |
| `publie` | Refonte poussée en prod, monitoring activé |
| `en-monitoring` | Pas de refonte décidée, on surveille les positions |
| `pause` | Audit fait mais aucune action planifiée |
| `archive` | Plus pertinent (article supprimé, fusionné, 301) |

## Triggers fréquents

- **Rank Math weekly** : rapport hebdo positions, baisse > 20 places
- **GSC alerte** : chute clics / impressions / CTR
- **Demande Michael** : audit explicite
- **Pre-publication** : audit avant publication d'un nouvel article concurrent (cluster check)
- **Routine pillar** : audit régulier des articles piliers (trimestriel)
- **Refonte stack** : changement de positionnement (ex: stack Tutor LMS → revue de tous les avis LMS)

## Fréquence de re-audit recommandée

| Type article | Fréquence |
| --- | --- |
| Article pilier | trimestriel |
| Avis plugin affilié | trimestriel + sur trigger Rank Math |
| Comparatif | trimestriel + sur sortie nouvelle version concurrent |
| Article informationnel | annuel |
| Article perdant (>50e) | mensuel jusqu'à décision |
