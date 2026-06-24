# flyingpress-wp-rocket-comparison-de - index audits

- **URL** : <https://schoolswp.com/de/vergleich-flyingpress-wp-rocket/> (publié, DE)
- **post_id** : 343161
- **Mot-clé cible** : `flyingpress vs wp rocket` (de_DE, 10 recherches/mois, ultra-niche)
- **Pilier** : performance / plugins de cache (comparatif affilié)
- **Statut courant** : `publie` (en-monitoring) - **#1 organique de_DE atteint au J+30**
- **Polylang** : `de=343161 | fr=52819 | en=343156` (siblings : [comparison-fr](../flyingpress-wp-rocket-comparison-fr/), [comparison-en](../flyingpress-wp-rocket-comparison-en/))

## Historique des snapshots

| Date                                   | Trigger                                            | Position de_DE (live)       | Décision / livrable                                                                      | Synthèse                                                                                |
| -------------------------------------- | -------------------------------------------------- | --------------------------- | ---------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- |
| [2026-06-25](2026-06-25/audit.md)      | Re-audit J+30 (Calendar event)                     | **🏆 #1**                   | P1 (image evergreen) + P2 (mu-plugin cloaks Polylang) appliqués live ; boucle KPI fermée | [audit.md](2026-06-25/audit.md) + [state-after-v2.json](2026-06-25/state-after-v2.json) |
| [2026-06-01](2026-06-01/j7-monitor.md) | Monitoring J+7                                     | Absent top 30 (indexé PASS) | Comportement normal à J+7, attendre J+30                                                 | [j7-monitor.md](2026-06-01/j7-monitor.md)                                               |
| [2026-05-26](2026-05-26/audit.md)      | Audit + refonte (article publié DE mais rédigé FR) | Absent top 12               | Refonte body DE natif poussée (SHA `e1dc5666...`) + metas + image + CTA + maillage       | [audit.md](2026-05-26/audit.md)                                                         |

## Résumé du dernier audit (2026-06-25, J+30)

Le post 343161 était à l'origine un article publié en `lang=de` mais dont le corps était du **français pur** (dupliqué via Polylang sans traduction). La refonte du 2026-05-26 a réécrit le body en allemand natif (13 H2 + 12 H3 traduits, section "Optimale Einstellungen", 2 CTA Kadence, maillage interne recâblé, brand-strict 0 dash), avec recrawl Googlebot le jour même.

**Résultat J+30 : succès net.** Sur la SERP live de_DE de `flyingpress vs wp rocket`, schoolswp.com est passé de **absent du top 30 (J+7) à #1 organique**, devant la page officielle de wp-rocket.me et tous les concurrents EN. L'objectif initial ("émerger sur >= 1 keyword DE rank <= 30") est dépassé.

Vérification on-page live : body byte-identique au push (SHA `e1dc5666...`, zéro dérive), DE pur, indexé, RM title raccourci à 50 caractères (corrige le défaut title-too-long de thruuu), triade Polylang intacte.

Deux correctifs appliqués live ce jour : **P1** (retrait de la dernière occurrence "2025" dans la description de l'attachment 350864, backup postmeta `_schoolswp_bak_att_desc_20260624`) ; **P2** (mu-plugin `schoolswp-affiliate-cloaks.php` v1.1.1 -> v1.2.0 : les variantes localisées `/de|en|fr/flyingpress/` et `/wp-rocket/`, auparavant en 301 cassé vers une review FR/EN, sont désormais normalisées vers le slug canonique pour que ClickWhale gère le redirect avec tracking + nofollow/sponsored ; backup wp_option `schoolswp_bak_mu_affiliate_cloaks_20260624`).

**Note méthodo** : l'API DataForSEO Labs `ranked_keywords` renvoie toujours 0 pour l'URL (lag de leur base d'index sur ce mot-clé ultra-niche), alors que le SERP live montre #1. Pour les keywords ultra-niches, le SERP live est l'instrument fiable, pas la base Labs agrégée.

## Actions réalisées / en attente

- [x] Refonte body DE natif + metas + image + CTA + maillage (2026-05-26)
- [x] Monitoring indexation J+7 (2026-06-01)
- [x] Re-audit J+30 : SERP live + vérification on-page + state-after-v2 (2026-06-25)
- [x] P1 : résiduel evergreen "2025" featured image (2026-06-25)
- [x] P2 : routing Polylang-aware des cloaks affiliés localisés (2026-06-25)
- [ ] Re-audit J+60 (~2026-07-25) : tenue du #1 + rattrapage base Labs + GSC réel + AI Overview de_DE
