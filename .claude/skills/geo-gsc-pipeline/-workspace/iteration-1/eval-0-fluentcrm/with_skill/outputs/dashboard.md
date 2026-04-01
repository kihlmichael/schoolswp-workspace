# Dashboard Editorial GEO — FluentCRM / CRM WordPress

**Propriete** : schoolswp.fr
**Periode** : 2026-02-01 a 2026-03-31 (60 jours)
**Pays** : FR | **Device** : ALL
**Source** : test-data.csv (export GSC)
**Qualite des donnees** : gsc_real
**Date de generation** : 2026-03-31

---

## Synthese du pipeline

| Phase | Resultat |
|-------|----------|
| **Phase 0** | 15 requetes extraites du CSV, 0 doublons, 0 lignes vides |
| **V1 — Filtrage** | 15/15 requetes retenues (0 eliminee — aucune brand-only ni trop vague) |
| **V2 — Clustering** | 11 clusters canoniques (5 P1, 4 P2, 2 P3) |
| **V3 — Specs AIO** | 5 specs completes (tous les P1) |

---

## Repartition des intentions

| Intention | Nombre de prompts | % |
|-----------|-------------------|---|
| COMM | 9 | 60% |
| INFO | 6 | 40% |

---

## Metriques cles du dataset

| Metrique | Valeur |
|----------|--------|
| Impressions totales | 9 750 |
| Clics totaux | 277 |
| CTR moyen | 2.84% |
| Position moyenne | 13.4 |
| Requete la plus visible | `crm wordpress gratuit` (1 500 imp.) |
| Requete la plus cliquee | `fluentcrm avis` (45 clics) |

---

## Backlog editorial priorise

### P1 — Production immediate (5 clusters)

| # | Cluster canonique | Decision | Impressions | Prompts |
|---|-------------------|----------|-------------|---------|
| 1 | [WP-CRM] / [Guide] / [COMM] / [CRM WordPress gratuit] | NEW | 1 500 | 1 |
| 2 | [WP-CRM] / [Avis] / [COMM] / [FluentCRM avis complet] | NEW | 1 200 | 1 |
| 3 | [WP-CRM] / [Comparatif] / [COMM] / [Meilleur plugin email marketing WordPress] | NEW | 1 100 | 1 |
| 4 | [WP-CRM] / [Comparatif] / [COMM] / [FluentCRM vs Mailchimp] | NEW | 980 | 1 |
| 5 | [WP-CRM] / [Pricing] / [COMM] / [FluentCRM tarifs et gratuite] | NEW | 2 150* | 3 |

*Impressions cumulees des 3 requetes rattachees (pricing + gratuit + lite vs pro).

### P2 — Production planifiee (4 clusters)

| # | Cluster canonique | Decision | Impressions | Prompts |
|---|-------------------|----------|-------------|---------|
| 6 | [WP-CRM] / [Comparatif] / [COMM] / [FluentCRM vs MailPoet] | NEW | 520 | 1 |
| 7 | [WP-CRM] / [Alternatives] / [COMM] / [Alternatives FluentCRM] | NEW | 410 | 1 |
| 8 | [WP-CRM] / [Tutoriel] / [INFO] / [Configurer FluentCRM WordPress] | NEW | 740* | 2 |
| 9 | [WP-CRM] / [Tutoriel] / [INFO] / [Automatisation email FluentCRM] | NEW | 630* | 2 |

*Impressions cumulees des requetes rattachees.

### P3 — Long terme (2 clusters)

| # | Cluster canonique | Decision | Impressions | Prompts |
|---|-------------------|----------|-------------|---------|
| 10 | [WP-CRM] / [Setup] / [INFO] / [FluentCRM WooCommerce integration] | NEW | 340 | 1 |
| 11 | [WP-CRM] / [Tutoriel] / [INFO] / [Segmentation contacts FluentCRM] | NEW | 180 | 1 |

---

## Overlaps detectes

| Cluster A | Cluster B | Action recommandee |
|-----------|-----------|--------------------|
| [WP-CRM] / [Comparatif] / [COMM] / [FluentCRM vs Mailchimp] | [WP-CRM] / [Comparatif] / [COMM] / [FluentCRM vs MailPoet] | Pages separees avec maillage interne reciproque |

---

## Prompts Thruuu — Resume

| Type | Nombre |
|------|--------|
| PRIMARY | 15 |
| SECONDARY (V3 P1 uniquement) | 106 |
| **TOTAL** | **121** |

---

## Actions suivantes recommandees

1. **Produire les 5 pages P1** dans cet ordre de priorite :
   - `crm-wordpress-gratuit` (1 500 imp., COMM generique)
   - `fluentcrm-avis` (1 200 imp., COMM directe)
   - `meilleur-plugin-email-marketing-wordpress` (1 100 imp., COMM generique)
   - `fluentcrm-vs-mailchimp` (980 imp., COMM comparative)
   - `fluentcrm-pricing-tarifs` (2 150 imp. cumulees, COMM decisive)

2. **Configurer le maillage interne** entre les 5 pages P1 (cocon CRM)

3. **Uploader les 121 prompts Thruuu** pour monitoring des citations AI

4. **Generer les specs V3 pour les P2** (FluentCRM vs MailPoet, Alternatives, Configurer, Automatisation)

5. **Verifier les pages existantes** sur schoolswp.fr pour basculer de NEW a UPDATE si applicable

---

## Decisions editoriales

- **Toutes les decisions sont NEW** : aucune page existante detectee dans les donnees GSC (colonne `page` absente du CSV)
- **Univers unique : WP-CRM** — le dataset est 100% centre sur FluentCRM et l'email marketing WordPress
- **Potentiel affiliation** : FluentCRM (programme affilies actif), Mailchimp, MailPoet, Brevo, ActiveCampaign, Amazon SES
- **Strategie de contenu** : les 5 pages P1 forment un cocon semantique complet autour de FluentCRM / CRM WordPress
