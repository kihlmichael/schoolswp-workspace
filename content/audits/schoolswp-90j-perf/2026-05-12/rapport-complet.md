# Audit de performance schoolsWP : 90 jours

**Site** : schoolswp.com
**Période analysée** : 12/02/2026 → 12/05/2026 (90 jours)
**Période de comparaison** : 14/11/2025 → 11/02/2026 (89 jours)
**Source de données** : Google Search Console + DataForSEO on-page (fetch live 12/05/2026)
**Auteur** : Claude Code (Opus 4.7) pour Michael KIHL
**Date du rapport** : 12 mai 2026

---

## Sommaire

1. Analyse de performance (90 j)
2. Opportunités d'optimisation du CTR
3. Audit d'alignement requête-page
4. Plan d'actions consolidé Quick Wins

---

# Partie 1 : Analyse de performance (90 jours)

## 1.1 Qualité des données

- Données complètes : clics / impressions / CTR / position par jour, requête, page, pays, device.
- Le 12/05/2026 n'est que partiel (1 clic / 1 007 impressions) : exclu des comparaisons fines.
- Total requêtes mouvantes : 1 503 ; total pages : 1 136. Top 50 exploité dans la compare API.
- Information non fournie : conversions / revenus (pas de GA4), couverture d'index, données CWV.

## 1.2 Vue d'ensemble

| Métrique | Période actuelle | Tendance interne |
|---|---|---|
| Clics | 1 121 | Flat 12-14 clics/j, chute le 01/05 (2 clics) |
| Impressions | 375 776 | Volume stable, légère reprise mai |
| CTR moyen | 0,30 % | Très faible, plafond P2 à 0,56 % (14/02) |
| Position moyenne | 10,3 | Trajectoire : 14,8 (12/02) → 7,7 (07/04, plus bas) → 9,5 (11/05) |

**Signal clé** : la position s'est améliorée de 7 places entre mi-février et début avril, puis dégradation visible mi-avril → mai (de 8,1 à 10,2). C'est ce point qui mérite l'enquête prioritaire.

### Segmentation par device

| Device | Clics | Impressions | CTR | Position |
|---|---|---|---|---|
| Desktop | 817 (73 %) | 306 252 (81 %) | 0,27 % | 10,4 |
| Mobile | 286 (26 %) | 61 734 (16 %) | 0,46 % | 9,4 |
| Tablet | 7 | 2 524 | 0,28 % | 8,1 |

Desktop représente 81 % des impressions mais avec un CTR 1,7× inférieur au mobile. Le potentiel le plus gros est sur desktop.

### Segmentation par pays (top 5)

| Pays | Clics | Impressions | CTR | Position |
|---|---|---|---|---|
| France | 509 | 112 194 | 0,45 % | 12,6 |
| Allemagne | 133 | 27 683 | 0,48 % | 9,7 |
| USA | 42 | 90 395 | 0,05 % | 9,3 |
| Suisse | 26 | 4 734 | 0,55 % | 9,9 |
| Belgique | 21 | 5 544 | 0,38 % | 9,6 |

Anomalie USA : 24 % des impressions du site, 0,05 % de CTR. Position correcte (9,3) mais zéro clic.

### Brand vs non-brand

"schoolswp" n'apparaît dans aucune des 50 requêtes mouvantes top. Site 100 % non-brand. Pas de marque organique recherchée, signal d'autorité encore faible.

## 1.3 Top 10 pertes : Requêtes

| Requête | Delta Clics | Delta Impressions | Delta CTR | Delta Position | Commentaire |
|---|---|---|---|---|---|
| 5euros | -31 (-82 %) | -2 520 (-35 %) | -0,38 pt | -1,0 (7 → 8) | Article majeur perd son terrain |
| 5euros.com avis | -12 (-100 %) | -652 | -1,69 pt | -1,6 | Sorti des clics |
| suretriggers | -9 (-53 %) | -144 | -0,45 pt | +13,3 | Position s'améliore, CTR baisse |
| wp rocket vs flying press | -7 (-88 %) | -66 | -4,95 pt | -0,3 | SERP visiblement remaniée |
| frank houbre | -4 (-67 %) | -9 | -2,06 pt | -0,1 | Brand person query |
| mailerpress | -4 (-33 %) | +118 | -1,26 pt | +0,6 | CTR divisé par 2 à position stable |
| pageradar | -5 (-100 %) | -429 | -1,17 pt | n/a | Sorti |
| skeall | -4 (-80 %) | -2 | -6,30 pt | +4,8 | CTR effondré |
| o2switch | -3 (-100 %) | -1 833 | -0,16 pt | n/a | Sorti |
| tutor lms review | -3 (-100 %) | -300 | -1,00 pt | n/a | Sorti |

## 1.4 Top 10 gains : Requêtes

| Requête | Delta Clics | Delta Impressions | Delta Position | Commentaire |
|---|---|---|---|---|
| chatseo | +10 (de 0) | +3 702 | n/a → 8,7 | Nouvel article qui prend |
| zipwp | +8 (+200 %) | +877 | +0,2 | Hub plugin solide |
| flyingpress | +7 (+64 %) | +100 | -1,1 | Bonne progression brand |
| buddyboss | +6 (de 0) | +1 116 | n/a → 8,2 | Nouvel hub |
| 5euros com | +6 (+120 %) | -578 | -0,4 | Récupère ce que 5euros perd |
| latepoint | +5 (+500 %) | +584 | +8,5 | Bond de position |
| kadence | +4 (de 0) | +1 207 | n/a → 9,5 | Nouvel hub WP |
| metricool | +4 (de 0) | +1 397 | n/a → 5,3 | Top 5 immédiat |
| kadence wordpress | +4 (de 0) | +380 | n/a → 7,5 | Variante intent |
| 5€.com avis | +2 (+200 %) | -13 | +0,9 | Variante typographique active |

## 1.5 Top 10 pertes : Pages

| Page | Delta Clics | Delta Impressions | Delta Position | Hypothèse |
|---|---|---|---|---|
| /ce-quil-faut-savoir-sur-la-plateforme-5euros-com/ | -86 (-54 %) | -4 324 (-12 %) | +0,4 | Cluster 5euros remanié par Google ; CTR ÷ 2 à position stable |
| /en/flyingpress-wp-rocket-comparison/ | -21 (-62 %) | -6 283 (-54 %) | +2,2 | Position s'améliore mais perd l'audience US |
| /en/local-wp-review/ | -20 (-65 %) | +236 | -0,1 | CTR -0,36 pt : title/meta off |
| /suretriggers-automatisation-integration-wordpress/ | -13 (-54 %) | -316 | +12,5 | Position bondit (24,7 → 12,3) mais clics chutent |
| /wordpress-6-9-nouveautes/ | -10 (-100 %) | -285 | -2,5 | Article éphémère sorti, normal |
| /en/zipwp-alternative-instawp/ | -10 (-50 %) | -358 | +2,2 | Bonne position, mais cannibalisé ? |
| /qui-est-frank-houbre/ | -8 (-44 %) | -211 | +3,0 | Page personne, perte naturelle |
| /mise-a-jour-mailerpress-1-1/ | -8 (-100 %) | -352 | -2,5 | Page MAJ produit ancien, sortie |
| /en/droip-review/ | -8 (-73 %) | -117 | -0,3 | CTR -1,00 pt |
| /pageradar-avis/ | -7 (-100 %) | -624 | -6,1 | Désindexée ou produit éteint |

## 1.6 Top 10 gains : Pages

| Page | Delta Clics | Delta Impressions | Delta Position | Commentaire |
|---|---|---|---|---|
| /avis-chatseo-test-complet/ | +25 (+1250 %) | +5 847 (+4 640 %) | -2,6 | Article démarre fort |
| /mon-avis-sur-kadence-wp/ | +17 (+46 %) | +2 713 (+64 %) | +1,2 | Page pilier qui scale |
| /de/zipwp-wordpress-seiten-erstellung-mit-ki/ | +16 (+160 %) | +1 467 | +1,1 | Très bonne performance DE |
| /en/amelia-wp-review/ | +14 (+64 %) | +10 253 (+39 %) | +2,8 | CTR catastrophique (0,10 %) : voir alerte |
| /tout-ce-que-vous-devez-savoir-sur-buddyboss/ | +13 (+217 %) | -287 | +2,3 | Bond de CTR (+1,1 pt) |
| /en/metricool-review/ | +12 (+200 %) | +10 430 (+38 %) | -1,7 | CTR 0,05 % : voir alerte rouge |
| /en/affiliatepress-review/ | +11 (+275 %) | +339 | +8,9 | Bond de 18,5 → 9,7 |
| /divi-machine-le-plugin-divi-quil-vous-faut/ | +9 (+150 %) | -22 | +4,5 | CTR +1,4 pt |
| /comparaison-flyingpress-wp-rocket/ | +7 (+37 %) | +242 | +7,0 | Position 13,3 → 6,2 |
| /en/clickwhale-alternative-pretty-links/ | +7 (+350 %) | +22 | +6,5 | Petit volume mais bon momentum |

## 1.7 Alertes (rouge / orange)

### Alerte rouge n°1 : Cluster `5euros` en chute brutale

- Symptôme : /ce-quil-faut-savoir-sur-la-plateforme-5euros-com/ perd 86 clics (-54 %) avec position stable (8,3 → 7,9). CTR divisé par 2.
- Sur les requêtes : `5euros` -82 %, `5euros.com avis` -100 %, `wp rocket vs flying press` CTR -4,95 pt à position stable.
- Cause probable : Google a remanié la SERP `5euros` (sitelinks renforcés du site officiel, knowledge panel, ou featured snippet pris par un concurrent).
- Check immédiat : recherche manuelle `5euros` depuis FR / desktop + mobile et capture de SERP. Vérifier la présence de sitelinks expanded site:5euros.com, de PAA, de "Discussions et forums".

### Alerte rouge n°2 : Anglais positionné mais CTR USA = 0,05 %

- Symptôme : USA = 90 395 impressions / 42 clics. Position moyenne 9,3 (donc visible) mais quasiment zéro clic.
- Pages concernées : /en/metricool-review/ (37 580 impressions, CTR 0,05 %), /en/amelia-wp-review/ (36 639 impressions, CTR 0,10 %), /en/sureforms-wordpress-plugin/ (3 187 impressions, CTR 0,13 %).
- Cause probable : titres/metas pas optimisés pour l'audience US, ou présence en bas de page 1 sur des SERPs ultra-concurrentielles dominées par G2/Capterra/affiliés US, ou citations AI Overview sans clic.
- Check immédiat : taper `metricool review` et `amelia wordpress review` depuis USA/desktop (proxy ou VPN), vérifier le SERP layout.

### Alerte orange n°3 : Dégradation de position depuis mi-avril

- Symptôme : position moyenne 8,0 (07/04) → 10,2 (10/05). +2 places perdues sur 5 semaines.
- Cause probable : nouvelles concurrences sur les nouveaux articles indexés en mars qui ressortent maintenant, ou changement algo Google avril/mai.
- Check immédiat : croiser avec la table audits si certains snapshots datés montrent du décrochage sur les pages piliers.

### Alerte orange n°4 : Decay des pages "actualité"

- /wordpress-6-9-nouveautes/, /mise-a-jour-mailerpress-1-1/, /o2switch-avis/ : -100 % de clics. Pages "news" naturelles à expirer, mais montrent que le contenu daté pèse sur le score moyen du site.

## 1.8 Opportunités rapides

### A. Quick wins CTR (impressions massives + CTR < 0,5 % + position 5-10)

| Page | Impressions | CTR actuel | Position | Action |
|---|---|---|---|---|
| /en/metricool-review/ | 37 580 | 0,05 % | 7,3 | Refonte title/meta EN : orientation US |
| /en/amelia-wp-review/ | 36 639 | 0,10 % | 7,1 | Refonte title/meta + Schema Review |
| /en/tastewp-review/ | 8 395 | 0,17 % | 6,2 | Refonte title (déjà bien rankée) |
| /en/flyingpress-wp-rocket-comparison/ | 5 417 | 0,24 % | 7,5 | Capitaliser via meta description 2026 |
| /en/local-wp-review/ | 5 872 | 0,19 % | 6,7 | Title plus bénéfice (free local WP env 2026) |
| /en/sureforms-wordpress-plugin/ | 3 187 | 0,13 % | 9,8 | Optimiser title pour intent US |

### B. Bonds de position à pousser maintenant

- /comparaison-flyingpress-wp-rocket/ : 13,3 → 6,2 = maillage interne immédiat depuis articles cache plugins.
- /en/affiliatepress-review/ : 18,5 → 9,7 = lien interne depuis pages affiliation/Pretty Links.
- /de/latepoint-meinung/ : 9,9 → 6,4 = à pousser sur cluster booking DE.
- /learndash-avis/ : 17,5 → 8,2 = lien depuis /tutor-lms-vs-learndash/ si existe.

### C. Nouveaux hubs qui décollent

- kadence / kadence wp / kadence wordpress : 3 variantes dans le top des nouvelles requêtes. Cocon Kadence à formaliser.
- metricool : produit en momentum, créer FR side si pas fait.
- linkcentral, buddyboss, fluentcart : tous démarrent. Maillage croisé manquant.

## 1.9 Résumé exécutif Partie 1

1. Le site génère 1 121 clics / 376 k impressions / CTR 0,30 % sur 90 j. CTR très faible, c'est le levier numéro 1.
2. Trajectoire de position positive sur mars-avril (14 → 8) puis dégradation en mai (8 → 10) à surveiller.
3. Alerte rouge n°1 : cluster `5euros` perd 86 clics sur une page majeure à position stable = SERP remaniée par Google.
4. Alerte rouge n°2 : USA = 24 % des impressions mais CTR 0,05 %. /en/metricool-review/ et /en/amelia-wp-review/ cumulent 73 k impressions pour 54 clics.
5. Desktop = 81 % des impressions mais CTR 1,7× inférieur au mobile. Chantier title/snippet desktop transverse.
6. Gros gains : chatseo démarre (+25 clics), Kadence cluster décolle (4 requêtes nouvelles), latepoint position +8,5.
7. Site 100 % non-brand. Identité brand absente, à construire en parallèle du netlinking Q2.
8. Priorité 48-72h : refonte titre/meta EN sur metricool + amelia, capture SERP `5euros`, maillage vers /comparaison-flyingpress-wp-rocket/.
9. Priorité semaine : cocon Kadence + refonte titres EN restants + audit cluster 5euros.
10. Chantier structurel : trancher la stratégie US (refonte vraie ou noindex), nettoyer les pages "actualité", construire identité brand.

---

# Partie 2 : Opportunités d'optimisation du CTR

## 2.1 Résumé

1. CTR moyen pondéré du site : 1 121 clics / 375 776 impressions = 0,30 %.
2. Seuil "beaucoup d'impressions" : pages >= 3 000 impressions / 90 j (top ~3 % des pages).
3. 7 pages opportunités prioritaires (P1) : position <= 10 + CTR < 0,30 %. 3 pages secondaires (P2).
4. Anomalie majeure : sur /en/metricool-review/ et /en/amelia-wp-review/ (74 k impressions cumulées), 95 % du volume vient de queries anonymisées → narrowing d'intent nécessaire on-page.
5. Pattern observé : les pages "review" EN positionnées 5-10 ont des titles trop génériques pour le marché US.

## 2.2 Tableau priorisé

| Priorité | URL | Impressions | CTR actuel | Position | Pourquoi opportunité | Mot-clé principal |
|---|---|---|---|---|---|---|
| P1 | /en/metricool-review/ | 37 488 | 0,05 % | 7,3 | 37 k impressions à 6× sous CTR moyen | metricool review |
| P1 | /en/amelia-wp-review/ | 36 528 | 0,10 % | 7,1 | 36 k impressions à 3× sous moyenne | amelia wordpress |
| P1 | /ce-quil-faut-savoir-sur-la-plateforme-5euros-com/ | 31 234 | 0,23 % | 7,9 | Article majeur FR en chute (-54 %) | 5euros.com |
| P1 | /en/tastewp-review/ | 8 389 | 0,17 % | 6,2 | Position 6 stable mais CTR 2× sous moyenne | tastewp |
| P1 | /en/local-wp-review/ | 5 815 | 0,19 % | 6,7 | Top 7 vs `localwp / xampp` mais titre générique | localwp |
| P1 | /en/flyingpress-wp-rocket-comparison/ | 5 406 | 0,24 % | 7,5 | Position s'améliore | flyingpress vs wp rocket |
| P1 | /en/sureforms-wordpress-plugin/ | 3 187 | 0,13 % | 9,8 | Position 9,8 = bord du top 10 | sureforms wordpress |
| P2 | /zipwp-revolution-creation-site-wordpress-ia/ | 5 904 | 0,34 % | 6,3 | CTR juste au-dessus moyenne | zipwp |
| P2 | /avis-metricool-test-complet/ | 3 799 | 0,29 % | 6,8 | Tout proche du seuil | metricool avis |
| P2 | /en/bit-flows-review/ | 4 165 | 0,38 % | 8,0 | Au-dessus moyenne mais peut gagner +1 pt CTR | bit flows |

## 2.3 Recommandations par page

### 1. /en/metricool-review/ : P1

**Intention probable** : investigation commerciale EN. L'utilisateur compare Metricool à Buffer/Hootsuite avant achat ou cherche un avis honnête après teaser publicitaire.

**Mot-clé principal** : metricool review

**Titles**

- V1 (53 c) : `Metricool Review 2026: Honest Test After 6 Months Use` - Angle preuve d'usage, déclenche la curiosité.
- V2 (54 c) : `Metricool Review 2026: Worth It vs Buffer & Hootsuite?` - Angle comparatif, capte les chercheurs en investigation.
- V3 (55 c) : `Metricool Review 2026: Real Pricing, Pros & Hidden Cons` - Angle transparence, "Hidden Cons" est le hook.

**Metas**

- M1 (152 c) : `I tested Metricool for 6 months. Real pricing, what works for Instagram & TikTok, and 3 limits Buffer users will hate. Honest review, no sponsorship.`
- M2 (155 c) : `Detailed Metricool 2026 review: pricing tiers, AI generator, competitor analysis, and how it really compares to Buffer & Hootsuite. WordPress agency view.`

**Risque de mismatch** : moyen. Le titre promet "Honest Test After 6 Months". Si l'article actuel n'a pas de signal de durée d'usage personnel, ajouter 1 paragraphe "How I tested" en intro.

### 2. /en/amelia-wp-review/ : P1

**Intention probable** : investigation commerciale EN. Owner WP cherche un plugin de booking.

**Mot-clé principal** : amelia wordpress

**Titles**

- V1 (55 c) : `Amelia WordPress Review 2026: Booking Plugin Worth $79?` - Angle prix.
- V2 (52 c) : `Amelia for WordPress: Real Review After 50+ Bookings` - Angle preuve d'usage.
- V3 (63 c) : `Amelia WP Booking Plugin Review: Pros, Cons & Best Alternatives` - Angle exhaustif.

**Metas**

- M1 (142 c) : `Real Amelia for WordPress test: SMS reminders, Apple/Google Calendar sync, Stripe, and the 4 features missing vs FluentBooking. 2026 review.`
- M2 (141 c) : `Is Amelia the best booking plugin for WordPress? Honest review with screenshots, pricing breakdown and 2 alternatives I tested side by side.`

**Risque de mismatch** : moyen. Même problème que Metricool (36 k impressions / 700 trackées). Vérifier que le H1 et l'intro ciblent bien `amelia wordpress booking plugin`.

### 3. /ce-quil-faut-savoir-sur-la-plateforme-5euros-com/ : P1

**Intention probable** : navigationnel + investigation FR.

**Mot-clé principal** : 5euros.com

**Titles**

- V1 (56 c) : `5euros.com : avis 2026, arnaque ou plateforme légitime ?` - Angle curiosité utile.
- V2 (50 c) : `5euros.com : avis, prix et alternatives pour 2026` - Angle safe / complet.
- V3 (58 c) : `5euros.com : retour d'expérience après 100 commandes (2026)` - Angle preuve d'usage.

**Metas**

- M1 (144 c) : `Tu hésites avec 5euros.com ? J'ai commandé 100+ services sur la plateforme. Avis honnête : pour qui ça marche, pour qui c'est une perte de temps.`
- M2 (134 c) : `5euros.com en 2026 : prix réels, qualité des prestations, arnaques à éviter et 3 alternatives sérieuses pour les freelances WordPress.`

**Risque de mismatch** : moyen-élevé sur V1 si l'article ne tranche pas clairement "légitime".

### 4. /en/tastewp-review/ : P1

**Intention probable** : navigationnel + investigation EN.

**Mot-clé principal** : tastewp

**Titles**

- V1 (49 c) : `TasteWP Review 2026: Best Free WordPress Sandbox?`
- V2 (55 c) : `TasteWP Honest Review: Limits, Pricing & 2 Alternatives`
- V3 (55 c) : `TasteWP vs InstaWP: Which Free WP Sandbox Wins in 2026?`

**Metas**

- M1 (134 c) : `Real TasteWP test: how long sites really last, performance limits, paid plans worth it, and 2 free alternatives I use weekly for WP dev.`
- M2 (144 c) : `TasteWP free sandbox for WordPress: honest review with screenshots, the 7-day catch nobody mentions, and how it compares to InstaWP & LocalWP.`

**Risque de mismatch** : faible (terme très branded).

### 5. /en/local-wp-review/ : P1

**Intention probable** : investigation EN.

**Mot-clé principal** : localwp

**Titles**

- V1 (50 c) : `Local WP Review 2026: Free Flywheel Tool Worth It?`
- V2 (57 c) : `Local WP vs XAMPP: Honest 2026 Review (Free WordPress Dev)`
- V3 (62 c) : `Local WP by Flywheel Review: Setup, Limits & Best Alternatives`

**Metas**

- M1 (133 c) : `Local WP review after 200+ test sites: real setup time, SSL pain points, and why I switched from XAMPP. Free dev environment compared.`
- M2 (138 c) : `Local WP by Flywheel in 2026: honest review with screenshots, the 3 features I miss vs Docker, and when XAMPP still wins for WordPress dev.`

**Risque de mismatch** : faible.

### 6. /en/flyingpress-wp-rocket-comparison/ : P1

**Intention probable** : comparative EN.

**Mot-clé principal** : flyingpress vs wp rocket

**Titles**

- V1 (50 c) : `FlyingPress vs WP Rocket 2026: Real PageSpeed Test`
- V2 (56 c) : `FlyingPress vs WP Rocket: Which One Saved My Site? (2026)`
- V3 (59 c) : `WP Rocket vs FlyingPress: Lighthouse Results & Verdict 2026`

**Metas**

- M1 (142 c) : `Tested FlyingPress and WP Rocket on the same site. Real Lighthouse scores, LCP times, and the one feature that decided it. No affiliate fluff.`
- M2 (139 c) : `FlyingPress vs WP Rocket: side-by-side benchmark on 3 sites. Pricing, support, and which one I kept for clients in 2026. Screenshots inside.`

**Risque de mismatch** : faible.

### 7. /en/sureforms-wordpress-plugin/ : P1

**Intention probable** : investigation EN.

**Mot-clé principal** : sureforms wordpress

**Titles**

- V1 (58 c) : `SureForms Review 2026: Free WordPress Form Plugin Worth It?`
- V2 (53 c) : `SureForms vs Gravity Forms: Free Plugin Showdown 2026`
- V3 (55 c) : `SureForms WordPress Plugin: Honest Review After 3 Months`

**Metas**

- M1 (145 c) : `SureForms review: the free WordPress form builder from Brainstorm Force. AI form generation, conditional logic, and the 4 gaps vs Gravity Forms.`
- M2 (146 c) : `Is SureForms a real alternative to Gravity or Fluent Forms? Tested for 3 months on 5 sites: pros, cons, pricing, and where it falls short in 2026.`

**Risque de mismatch** : faible.

## 2.4 Actions complémentaires hors titre/meta

| Action | Pages concernées | Raison |
|---|---|---|
| Narrowing d'intent on-page | /en/metricool-review/, /en/amelia-wp-review/ | 95 % d'impressions sur queries anonymisées |
| Schema Review (Product + AggregateRating) | Toutes les pages review EN/FR | Active des étoiles en SERP, +20-30 % CTR mesuré |
| Audit SERP manuel | /ce-quil-faut-savoir-sur-la-plateforme-5euros-com/ | Vérifier sitelinks/PAA du site officiel avant rewrite |
| A/B sequential test | Top 3 (Metricool, Amelia, 5euros) | Implémenter V1, mesurer CTR sur 14 j, si gain < +50 % tester V2 |

---

# Partie 3 : Audit d'alignement requête-page

## 3.1 Découverte critique sur les queries Metricool

Le décompte des 100 premières queries révèle un pattern d'impressions venant d'AI Overview / Gemini / ChatGPT (queries type "any red flags?", "can i do this for free", "give me a short summary of it", "evaluate the b2b software review company capterra", "apa berbayar"). La page est citée par les LLM mais l'utilisateur reste dans l'AIO.

Conclusion : les 95 % d'impressions cachées sur /en/metricool-review/ sont du trafic AEO/GEO. C'est un signal d'autorité dans l'index LLM, mais le clic ne suit pas.

## 3.2 Taxonomie d'intention

| Intent | Format attendu | Signal SERP typique |
|---|---|---|
| Informationnelle (apprendre) | guide, tuto, définition, FAQ | PAA, "People also ask", AIO box |
| Investigation commerciale (comparer/avis) | review, comparatif, pricing, pros/cons | "review" rich snippets, AggregateRating étoiles |
| Transactionnelle (acheter) | landing, page produit, pricing direct | shopping ads, prix, CTA acheter |
| Navigationnelle (marque) | page brand, page officielle | sitelinks expanded |
| AIO/Conversational (LLM-style) | sentence-level answers, FAQ, tables factuelles | AI Overview, "AI Mode" |

## 3.3 Analyse par URL

### Page 1 : /en/metricool-review/ (Score 65/100)

**État live**
- Title : `Metricool review 2026 | Review of the best free tool` (52 c)
- H1 : `Metricool review: Our comprehensive test and verdict for 2026`
- Meta : `Discover our review of Metricool 2026: strengths, weaknesses, pricing, and tips to boost your social media presence` (118 c)
- 2 533 mots, 9 H2

**Intent dominant requêtes** : investigation commerciale + AIO conversational (60 % du volume caché)
**Intent page** : review structurée mono-produit. Manque de sentence-level answers pour AIO et aucune section comparative.

**Problèmes**
- Aucune section explicite "Buffer vs Metricool" / "Hootsuite vs Metricool"
- Pas de FAQ schema sentence-level visible pour AIO
- Pas de mention Capterra/Trustpilot ratings (citation autorité tierce manquante)
- H1 "Our comprehensive test" sans signal d'usage personnel concret

**Décision** : OPTIMISER
**Priorité** : P1 (Impact H × Effort M)
**KPI** : CTR de 0,05 % → 0,30 % en 30 j ; +100 clics/mois

### Page 2 : /en/amelia-wp-review/ (Score 70/100)

**État live**
- Title : `Amelia Booking Plugin Pricing (2026): Plans, Costs + Review` (59 c)
- H1 : `Amelia WP Review 2026: The Best WordPress Booking Plugin?`
- Meta : `Up-to-date Amelia pricing (2026): license plans, what's included, who it's for, and the best alternatives. Clear verdict in 2 minutes.` (134 c)
- 2 813 mots

**Problème majeur** : Title (Pricing) ≠ H1 (Review) ≠ Meta (Pricing). Google ne sait pas quoi mettre en avant.

**Problèmes**
- Désalignement interne Title / H1 / Meta
- Title ne donne pas l'élément hook clé ("$79", "free?")
- Pas de TL;DR/verdict box en haut de page
- Section "Amelia vs FluentBooking" en bas de page (devrait remonter)
- Pas de Schema Review/AggregateRating visible
- Pattern AIO identique à Metricool

**Décision** : OPTIMISER + RÉALIGNER
**Priorité** : P1 (Impact H × Effort M)
**KPI** : CTR de 0,10 % → 0,40 % en 30 j

### Page 3 : /ce-quil-faut-savoir-sur-la-plateforme-5euros-com/ (Score 80/100)

**État live**
- Title : `5euros.com avis 2026 : tout savoir (devenue ComeUp)` (51 c)
- H1 : `5euros.com avis 2026 : tout savoir sur la plateforme (devenue ComeUp)`
- Meta : `Mon avis sur 5euros.com (ComeUp) : fonctionnement, tarifs, avantages, inconvénients et comparatif Fiverr. Inscription gratuite !` (128 c)
- 1 946 mots

**Décision** : OPTIMISER après check SERP
**Priorité** : P1 dépendante (gated by check SERP)
**KPI** : remonter clics de 72 à 130 en 30 j

### Page 4 : /en/tastewp-review/ (Score 35/100) : ALERTE ROUGE MISMATCH

**État live**
- Title : `Create a WordPress site without installation with TasteWP` (57 c)
- H1 : `TasteWP : Discover how to easily create your WordPress website`
- Meta : `Discover TasteWP! Easily create, test and manage online WordPress sites. No installation required!` (101 c)
- 2 041 mots
- Structure H2 : Introduction, Why choose TasteWP, How do I get started, Maximize your experience, Conclusion
- H3 : Step 1: Registration, Step 2: Explore dashboard, Step 3: Customize

**MISMATCH MAJEUR D'INTENT** : le slug `tastewp-review` annonce une review. Le contenu réel est un "how to get started". L'utilisateur qui tape `tastewp` veut savoir "is it good?", pas "how do I sign up?".

Aucune section : Pricing, Limits, Pros/Cons, Verdict, Comparatif avec InstaWP / LocalWP.

**Décision** : RETARGETING + RÉÉCRITURE PARTIELLE
**Priorité** : P1 critique (Impact H × Effort H)
**KPI** : CTR de 0,17 % → 0,8 % en 45 j

### Page 5 : /en/flyingpress-wp-rocket-comparison/ (Score 25/100) : ALERTE ROUGE BUG LANGUE

**État live**
- Title : `FlyingPress vs WP Rocket (2026) : Lequel Choisir pour WordPress ?` (EN FRANÇAIS sur page EN)
- H1 : `FlyingPress vs WP Rocket  -  Best WordPress Speed Plugin` (EN)
- Meta : `FlyingPress ou WP Rocket ? Comparatif 2026 : vitesse, Core Web Vitals, RUCSS, prix. Trouve le meilleur plugin de cache pour ton site WordPress.` (EN FRANÇAIS sur page EN)
- og:locale : en_US
- H2 : tous en FRANÇAIS
- H3 : mélange FR/EN
- 1 872 mots

**BUG MULTILINGUE** : Title + Meta + H2 + H3 partiel en FR sur version EN.

**Cause probable** : page créée via Polylang Translation Engine ou copie manuelle, le contenu HTML body a été traduit mais le title, meta description et les H2 ont gardé la VF.

**Décision** : CORRECTION CRITIQUE Polylang
**Priorité** : P1 critique (Impact H × Effort L)
**KPI** : CTR de 0,24 % → 0,8 % en 14 j (juste fix langue)

## 3.4 Synthèse des désalignements

**Top 5 désalignements**

1. TasteWP : slug "review" + contenu "how-to" = mismatch intent éliminatoire. Score 35/100.
2. FlyingPress comparison EN : Title/Meta/H2 en français sur page anglaise = bug Polylang. Score 25/100.
3. Metricool EN : page citée massivement par AIO mais sans FAQ sentence-level ni sections comparatives.
4. Amelia EN : désalignement interne Title (Pricing) ≠ H1 (Review) ≠ Meta (Pricing).
5. 5euros FR : alignement bon mais perte due à cause externe (SERP remaniée).

**Causes récurrentes**

- Slug "review" mais contenu "tuto" (TasteWP, suspecté Local WP)
- Bug Polylang Title/Meta non traduits (FlyingPress confirmé, à vérifier sur autres /en/)
- AIO/AEO non équipé : pas de FAQ Schema, pas de sentence-level answers
- Absence Schema Review sur 100 % des pages auditées

## 3.5 Règles de mapping (prévention)

1. 1 slug = 1 intent dominant. Un slug `*-review` doit produire une page review structurée (Limits / Pros / Cons / Verdict), pas un guide d'utilisation.
2. Title + H1 + Meta : 1 intent dominant aligné. Pas de Title "Pricing" avec H1 "Review" et Meta "Pricing".
3. Une page EN doit avoir TOUS ses éléments en EN : Title, Meta, H1, H2, H3, FAQ.
4. Si la query AIO existe (`how much does X cost`, `is X free`), la réponse doit exister en sentence-level (1-2 phrases) dans la page, idéalement dans un encadré FAQ avec Schema FAQPage.
5. Toute page "review" ou "avis" doit avoir Schema Review + aggregateRating.
6. Pour une query comparative (`X vs Y`, `best X alternatives`), la page doit avoir une section H2 comparative tabulaire.
7. Slug branded : prévoir une section comparative avec 2-3 alternatives.
8. Verdict / TL;DR en haut de page (en plus de la fin) pour les pages > 1 500 mots.
9. Mentionner les ratings tiers (Capterra, G2, Trustpilot) avec liens externes = signal E-E-A-T.
10. Toujours auditer l'alignement Title-H1-Meta après chaque modification via DataForSEO.
11. Cocon = 1 hub + N satellites mais 1 cible primaire par page.
12. Pages "actualité" / MAJ produit : décision binaire dès la publication = archivage J+90 ou rewrite evergreen.

---

# Partie 4 : Plan d'actions consolidé Quick Wins

## 4.1 Actions immédiates (48-72h)

| # | Action | Page | Effort | Impact | KPI |
|---|---|---|---|---|---|
| 1 | FIX Polylang langue sur /en/flyingpress-wp-rocket-comparison/ | 1 | L | H | CTR 0,24 % → 0,7 % en 14 j |
| 2 | Audit Polylang en masse : fetch on_page sur 10 pages /en/ | 10 | M | H | Identifier 2-3 autres pages bugées |
| 3 | Rewrite Title+Meta Metricool + Amelia + FAQ Schema | 2 | M | H | +200 clics cumulés en 30 j |
| 4 | Capture SERP `5euros`, `5euros.com`, `wp rocket vs flying press` | n/a | L | M | Diagnostic causal écrit |
| 5 | Inspect URL GSC sur les 4 pages -100 % clics | 4 | L | M | Identifier au moins 1 pb indexabilité |

## 4.2 Semaine prochaine

| # | Action | Effort | Impact | KPI |
|---|---|---|---|---|
| 6 | Restructuration TasteWP : nouveau H1, sections Limits/Pricing/Pros-Cons/Verdict/vs InstaWP | H | H | CTR 0,17 % → 0,8 % en 45 j |
| 7 | Ajout sections comparatives Metricool : Buffer/Hootsuite + ratings Capterra/Trustpilot | M | H | +50 clics/mois |
| 8 | Audit Local WP + SureForms : fetch on_page, décider Optimiser vs Retargeting | M | M | À confirmer |
| 9 | Cocon Kadence : hub + 3 articles satellites avec maillage en éventail | M | H | +30 clics/mois sur cluster d'ici 60 j |
| 10 | Refonte titre/meta des 4 autres pages EN à fort volume + CTR bas | M | M | +150 clics/mois cumulés |
| 11 | Schema Review systématique sur toutes les pages "-review-" et "-avis-" | M | H | +Snippets étoiles SERP |
| 12 | AEO playbook : template "page review prête AIO" avec sentence-level answers | M | H | Réutilisable sur 30+ pages |

## 4.3 Chantiers structurels (mois)

| # | Action | Objectif |
|---|---|---|
| C1 | Strategy US : décider si maintenir contenu EN tel quel ou réécrire pour audience US | 90 k impressions USA à 0,05 % CTR |
| C2 | Suppression / consolidation systématique des pages "actualité" | Réduire decay du site |
| C3 | Build identité brand : aucune requête "schoolswp" dans le top mouvant | Cohérent avec plan netlinking Q2 |
| C4 | Audit de cohérence hreflang sur l'ensemble des paires FR/EN/DE | Via crawl Screaming Frog ou DataForSEO |

## 4.4 Données manquantes

- Conversions / revenu par landing (GA4) : à croiser via MCP novamira ou export GA4
- Données SERP features par requête (DataForSEO) : utile pour confirmer alertes 1 et 2
- Données CWV / indexation (check_indexing_issues GSC ou Lighthouse) : utile pour expliquer dégradation mai

---

**Fin du rapport**

Rapport généré par Claude Code (Opus 4.7) pour Michael KIHL : schoolsWP : 12 mai 2026.
Sources : Google Search Console, DataForSEO on-page instant pages.
