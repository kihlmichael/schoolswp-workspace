# Audit : learn-wordpress-one-day (EN, brouillon 2289537)

> Brouillon EN « Is it possible to learn WordPress in a day? » (post 2289537, slug `learn-wordpress-one-day`).
> ⚠️ **Doublon** de l'article EN publié 2274708 (`/en/learn-wordpress-in-a-day/`), déjà audité sous [`learn-wordpress-day/`](../learn-wordpress-day/README.md) le 2026-05-16. Voir le constat de cannibalisation dans la synthèse.

## Statut

`doublon-consolidé` — Option A exécutée le 2026-06-02 (fusion + archivage des doublons EN/DE).

## Décision exécutée (2026-06-02, Option A)

Michaël a tranché : **fusion**. Actions appliquées côté prod :

- Hero interrogatif **2969739** (« in a day? ») porté sur l'EN canonique **2274708** (matche le titre-question ; ancien thumb 2968995 conservé, pas supprimé). og:image non épinglé → suit l'image à la une. Cache FlyingPress purgé.
- Constat à l'inspection : **2274708 était déjà supérieur au brouillon** (2828 mots vs 2240, 3 images vs 0, sa propre table EN 2901083, focus keyword correct, 0 lien FR). Donc rien d'autre à porter ; la table EN 2969740 (créée pour le brouillon) était redondante.
- Doublons mis en **corbeille** : EN **2289537** + DE **2289536**. Table EN redondante **2969740** en corbeille.
- **Groupe Polylang réparé** : le trash avait scindé le groupe (EN isolé / FR+DE liés sans EN). Reconstruit proprement via `pll_save_post_translations` → en:2274708 / fr:2112488 / de:2274709.

## Historique des snapshots

| Date       | Trigger                                                      | Statut            | Décision                                                  | Synthèse                              |
| ---------- | ------------------------------------------------------------ | ----------------- | --------------------------------------------------------- | ------------------------------------- |
| 2026-06-02 | Demande Michaël (audit pré-publication brouillon EN refondu) | doublon-consolidé | Option A : fusion dans 2274708 + corbeille doublons EN/DE | [synthese.md](2026-06-02/synthese.md) |

## Données collectées (2026-06-02)

- On-page via Novamira (`article-current-snapshot.md`)
- DataForSEO US/EN : volumes, SERP, intent, suggestions (`dataforseo-*.json` + `dataforseo-google-sheet.csv`)
- GSC : URL inspect + 90j (`gsc-*.json`) — URL publiée « Discovered - not indexed », 0 traction
- Google Sheet Drive : `schoolsWP - Volumes SEO - learn wordpress in a day - 2026-06-02`
- thruuu : à fournir par Michaël (`thruuu-raw/`)

## Actions recommandées

1. Trancher l'option de consolidation (doc `content/decisions/`).
2. Si Option A : porter image (2969739) + table EN (2969740) + corrections on-page dans 2274708, puis corbeille 2289537. Idem DE (2289536 → 2274709).
3. Nettoyer focus keyword, activer FAQPage schema, ajouter images corps, corriger lien FR, densifier maillage.
4. Pousser indexation `/en/learn-wordpress-in-a-day/`.
