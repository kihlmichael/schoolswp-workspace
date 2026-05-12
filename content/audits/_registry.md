# Registry des audits articles schoolsWP

> Index global de tous les articles ayant fait l'objet d'un audit dans `content/audits/`. Mise à jour à chaque nouveau snapshot.
> Conventions : voir [CONVENTIONS.md](CONVENTIONS.md).

## Articles audités

| Slug | URL | Premier audit | Dernier audit | Snapshots | Statut | Trigger initial |
| --- | --- | --- | --- | --- | --- | --- |
| [masteriyo-lms-avis](masteriyo-lms-avis/README.md) | `/masteriyo-lms-avis/` | 2026-05-07 | 2026-05-07 | 1 | refonte-decidee | Rank Math weekly 2026-05-03 (-51 pos) |

## Statuts possibles

| Statut | Sens |
| --- | --- |
| `audit-en-cours` | Collecte de données pas terminée |
| `refonte-decidee` | Décision prise, plan d'action en attente d'exécution |
| `refonte-en-cours` | Rédaction / réécriture en cours |
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
