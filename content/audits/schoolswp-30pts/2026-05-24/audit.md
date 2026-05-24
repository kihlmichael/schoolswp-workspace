# Audit WordPress — schoolswp.com

**Date** : 2026-05-24 | **Source données** : WP Umbrella (ID 51911), GSC, DataForSEO Lighthouse + on-page | **Skill** : `wp-site-audit-30pts`

## SCORE TOTAL : 22 / 30

| Catégorie | Note |
|---|---|
| Sécurité | 5/6 |
| Performance | 5/6 |
| SEO | 4/6 |
| Contenu | 4/6 |
| Technique | 4/6 |

## 1. Sécurité — 5/6

| Check | Verdict | Détail |
|---|---|---|
| WordPress/plugins à jour | PARTIEL | 6 plugins en retard : `fluent-crm`, `fluent-boards-pro`, `fluentcampaign-pro`, `fluent-support` + Pro, `novamira-pro` |
| 0 vulnérabilité CVE | OK | Scan WP Umbrella vide |
| 2FA / login masqué | OK | SecuPress Pro 2.6.1 actif |
| HTTPS | OK | Forcé |
| XML-RPC | OK | SecuPress |

## 2. Performance — 5/6

| Métrique | Valeur | Verdict |
|---|---|---|
| Lighthouse Desktop | 98/100 | Excellent |
| Lighthouse Mobile | 88/100 | Bon |
| LCP | 773 ms | Excellent |
| CLS | 0 | Parfait |
| Server response (TTFB) | 982 ms | À améliorer |
| Latest ping WP Umbrella | 4586 ms | Anormalement lent |
| Total weight | 1.27 MB | Correct |
| Scripts | 41 | Lourd |
| Unused JS/CSS | ~50% chacun | À nettoyer |
| Compression | Brotli | OK |

## 3. SEO — 4/6

| Check | Verdict | Détail |
|---|---|---|
| Title/H1/Meta | OK | Title 55c, desc 139c, H1 unique |
| Maillage interne | OK | 53 internal links sur home, Link Whisper + Easy Content Linker |
| Sitemaps | À FIXER | 10 soumis, sitemap_index OK mais `post-sitemap.xml` legacy = 628 warnings |
| Indexation home | PASS | Crawled MOBILE, indexing_allowed |
| Canonical | OK | Self-canonical confirmé |
| Schema rich results | INSUFFISANT | `rich_results: null` sur home |

**GSC 28 jours** : 358 clics / 128 835 impressions / CTR **0,28 %** / position moy. 9,5. Gisement = +940% si CTR atteint 3%.

## 4. Contenu — 4/6

| Check | Verdict | Détail |
|---|---|---|
| Fraîcheur | OK | Home modifiée 2026-05-05 |
| E-E-A-T | OK | Michael KIHL nommé, photo, twitter:creator |
| Duplication | À VÉRIFIER | Polylang FR/EN/DE, hreflang à auditer |
| TL;DR / FAQ | PARTIEL | H2 "Foire Aux Questions" sur home + buttons IA sur 357 articles |
| Qualité rédactionnelle | OK | Consistency 0.86-0.88 |
| Médias optimisés | OK | og:image + alt, WebP via FlyingPress |
| **Liens cassés** | **920 broken** | 10 pages WP Umbrella × 100. Pareto : 24× FluentCart item_id=2 mort, 23× /x, 20× /linkedin, 3× /o2switch, 1× /feed-youtube + ~15 articles renommés |

## 5. Technique — 4/6

| Check | Verdict | Détail |
|---|---|---|
| Version PHP | Présumé 8.1+ | À confirmer site details |
| **173 PHP issues loggées** | PRÉOCCUPANT | Probables résidus Fluent stack en retard |
| BDD optimisée | Disponible | WP Umbrella DB Optimization |
| SSL/HTTPS | OK | Cert valide |
| Sauvegardes auto | OK | WP Umbrella |
| Monitoring uptime | OK | Dernier downtime 2026-02-18 (3 mois) |
| .htaccess | OK | SecuPress, post-incident 2026-04-21 |
| TTFB | À AMÉLIORER | 982 ms / latest ping 4586 ms |

---

## TOP 3 ACTIONS PRIORITAIRES

### 1. Réparer les redirections d'affiliation et purger les broken links (EN COURS)
**Impact estimé** : UX cumulée sur ~70 vraies cassures (cloaks manquants + produit mort), purge crawl budget.

**Décisions prises** :
- Cloaks /linkedin, /x, /feed-youtube ajoutés au mu-plugin v1.1.0
- /o2switch : en attente URL d'affiliation réelle
- Produit FluentCart Buy-me-a-coffee (item_id=2) : à recréer en Tip fixe 5 €

### 2. Doubler le CTR organique via Schema enrichi
**Impact estimé** : +940% trafic organique potentiel (CTR 0,28% → 3%).

### 3. Investiguer 173 PHP issues + alléger home
**Impact estimé** : -300 ms TTFB minimum, Lighthouse mobile 88 → 95+.

---

## Snapshots de référence

- WP Umbrella snapshot project : ID 51911, 2026-05-24
- GSC perf 28j : 2026-04-26 → 2026-05-24
- Lighthouse Desktop : Lighthouse 13.1.0, 2026-05-24 16:12 UTC
- DataForSEO on-page : 2026-05-24 16:12 UTC
- WP Umbrella broken-links : 10 pages × 100, 2026-05-24
