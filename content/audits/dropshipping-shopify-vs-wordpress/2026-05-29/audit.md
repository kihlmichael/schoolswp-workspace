# Audit — Dropshipping : Shopify vs Wordpress

- **URL** : https://schoolswp.com/dropshipping-shopify-vs-wordpress/
- **Post ID** : 977 — publié 2020-10-28, modifié 2026-05-13, langue FR
- **Date audit** : 2026-05-29
- **Focus keyword Rank Math** : « dropshipping avec wordpress » (10 rech./mois — quasi nul)
- **Méthode** : audit expert manuel (le pipeline `publish_ready.cli` n'a pas pu tourner — `ANTHROPIC_API_KEY` du projet sans crédits, erreur 400). Grille identique : SEO×0.30 + LLM×0.25 + Conversion×0.25 + Autorité×0.20. Données réelles GSC + DataForSEO.

## Publish Score : 34 / 100 → réécriture (mais ROI faible, voir verdict)

| Axe                | Note | Pondération | Contribution |
| ------------------ | ---- | ----------- | ------------ |
| SEO                | 45   | 0.30        | 13.5         |
| LLM / GEO          | 35   | 0.25        | 8.75         |
| Conversion         | 25   | 0.25        | 6.25         |
| Autorité / E-E-A-T | 28   | 0.20        | 5.6          |
| **Total**          |      |             | **≈ 34**     |

## Données réelles

### Performance GSC (180 j, 2025-11-30 → 2026-05-29)

- **0 clic**, 433 impressions, CTR 0 %.
- Position 6 sur « dropshipping shopify vs wordpress » (118 impressions) → **0 clic** : titre/snippet ne convertit pas, ou requête micro-volume.
- Focus keyword « dropshipping avec wordpress » : position **34** (33 impressions).
- « shopify ou wordpress » : pos 31 (70 impr). « dropshipping wordpress » : pos 21 (14 impr).
- Beaucoup d'impressions sur des requêtes **anglaises** (signal de contenu traduit, faible pertinence FR).
- Indexée, PASS, crawl mobile, schema Breadcrumbs détecté. Liens internes entrants : `/creer-site-web-professionnel-wordpress`, `/ressources`.

### Volumes de recherche (DataForSEO, France/FR)

| Mot-clé                                        | Volume/mois | Tendance an | Note                                 |
| ---------------------------------------------- | ----------- | ----------- | ------------------------------------ |
| shopify dropshipping                           | 480         | -64 %       | Shopify-centré, hors angle schoolsWP |
| shopify vs woocommerce                         | 170         | -92 %       | **Meilleure cible réaliste** (KD 1)  |
| dropshipping wordpress / woocommerce           | 70-90       | -71 à -98 % | déclin fort                          |
| shopify ou woocommerce                         | 50          | -56 %       |                                      |
| shopify ou wordpress                           | 40          | -73 %       | intention navigationnelle            |
| **dropshipping avec wordpress** (focus actuel) | **10**      | —           | **mauvais choix de cible**           |

→ Cluster **petit et en déclin structurel**. Dropshipping = tangentiel au cœur schoolsWP (LMS/CRM/automation/formation), rattaché au pilier ecommerce.

## Findings par axe

### SEO (45)

- **Incohérence de ciblage majeure** : H1 « Shopify vs Wordpress » ≠ SEO title « Shopify ou WooCommerce ? » ≠ focus keyword « dropshipping avec wordpress ». Trois angles différents.
- Focus keyword mal choisi (10/mois). Cible réaliste : « shopify vs woocommerce » (170) ou « dropshipping woocommerce » (70).
- **Contenu mince** : ~1506 mots pour une SERP commerciale comparative.
- **0 CTR** malgré une position 6 → titre + meta à retravailler.
- **Pas de tableau comparatif** (Ninja Tables) alors que c'est un comparatif « vs » → manque featured snippet + aide à la décision.
- HTML invalide : lien Yoast avec **double attribut `title`**. Lien `/le-plug-in-alidropship-en-details` **sans slash final** (hygiène slug).
- Aucune image dans le corps (alt text absent).

### LLM / GEO (35)

- Contenu générique, **aucune donnée chiffrée fiable, aucune source/citation** → non extractible avec confiance par un moteur IA.
- **Erreurs factuelles** propagées (voir Autorité) → un LLM citant la page diffuse des erreurs.
- Pas de bloc réponse / TL;DR / verdict structuré par critère ; pas de FAQ alors que les requêtes sont des questions (« quelle plateforme… pour le dropshipping »).
- Verdict final hésitant (« les deux sont gagnants ») → mauvaise extraction.

### Conversion (25)

- **Aucun CTA schoolsWP** (newsletter, lead magnet, formation, bloc CTA Kadence). Fin générique « N'attendez plus ! ».
- **Monétisation incohérente** : pousse le lien affilié Shopify (`lien.michaelkihl.fr/shopify`) 4× mais **recommande WooCommerce** en conclusion — et WooCommerce pointe vers woocommerce.com sans monétisation.
- Aucun relais de conversion en milieu d'article. Pas de tableau d'aide à la décision.

### Autorité / E-E-A-T (28)

- **Vouvoiement** sur tout l'article → viole la règle de marque tutoiement.
- « nous voyons » → viole la voix « je » singulier (Michaël solo).
- **Ton « traduit de l'anglais »** (magasin, vlogs, tournures), confirmé par le ranking sur requêtes EN → faible originalité/expertise.
- **Erreurs factuelles** : « 75 000 plugins WooCommerce » (c'est le nb de plugins WordPress, pas des extensions WooCommerce) ; « hébergement WooCommerce 21 $/an » ; comptages d'apps/thèmes Shopify de 2020 ; **Yoast SEO** recommandé alors que le stack schoolsWP = **Rank Math**.
- Données 2020 non mises à jour, prix en $ (audience FR → €).
- « Wordpress » mal capitalisé (→ WordPress).

## Recommandations (par priorité)

### Quick wins (cheap, à faire même sans refonte — stoppe l'hémorragie E-E-A-T)

1. Corriger le ton : **tutoiement** intégral, supprimer « nous voyons » → « je ».
2. Corriger « Wordpress » → **WordPress** (H1 + corps).
3. Remplacer **Yoast** par **Rank Math** dans la section SEO + relier au bon article interne FR.
4. Corriger l'erreur « 75 000 plugins WooCommerce » + retirer/qualifier « hébergement 21 $/an ».
5. Réparer le **double `title`** du lien Yoast + ajouter le **slash final** au lien AliDropship.
6. Réaligner **H1 / SEO title / focus keyword** sur un seul angle (recommandé : « shopify vs woocommerce » ou « dropshipping woocommerce »).
7. Ajouter un **CTA schoolsWP** (bloc Kadence : newsletter ou formation ecommerce).

### Si refonte (à n'engager que si le pilier ecommerce/dropshipping est priorisé)

- Retarget « shopify vs woocommerce » (170) + intégrer « dropshipping woocommerce ».
- **Tableau comparatif Ninja Tables** (prix, SEO, scalabilité, support, paiement, dropshipping).
- Données 2026 à jour + sources ; prix en €.
- Bloc verdict « Pour qui Shopify reste pertinent » (respect concurrent, BRAND_RULES 31).
- Section FAQ (requêtes-questions GSC).

## Quick wins appliqués (2026-05-29)

Appliqués en production via Novamira (`wp_update_post` + meta Rank Math), vérifiés côté serveur. Source du nouveau contenu : [new-content.html](new-content.html).

- Tutoiement intégral (plus aucun « vous »), « nous voyons » → « je ».
- « Wordpress » → « WordPress » partout (H1 + corps).
- Yoast → Rank Math (2 occurrences) + lien interne conservé.
- Erreur « 75 000 plugins WooCommerce » corrigée ; hébergement et prix passés en € et actualisés (Shopify ~27-290 €, hébergement WP 5-15 €/mois) ; comptages Shopify (apps/thèmes) requalifiés.
- Lien AliDropship : slash final ajouté. Lien Yoast : double attribut `title` supprimé.
- Réalignement ciblage : H1 « Dropshipping : Shopify vs WordPress, lequel choisir ? » / SEO title « Dropshipping : Shopify vs WordPress ? Comparatif complet » / focus keyword « dropshipping shopify vs wordpress, shopify vs woocommerce, dropshipping woocommerce ».
- CTA Kadence (bouton brand palette9/1 + gradient) vers `/creer-site-web-professionnel-wordpress/`.
- Slug **inchangé** (indexé, position 6 sur la requête exacte). Date de modif rafraîchie.

**Non fait (refonte, hors quick win)** : tableau comparatif Ninja Tables, FAQ, section « Pour qui Shopify reste pertinent », mise à jour data sourcée 2026. Monétisation Shopify/WooCommerce incohérente laissée en l'état (décision marketing).

## Refonte appliquée (2026-06-01)

Refonte hybride poussée en production via Novamira (post 977). Draft validé par Michaël avant push. Source : [refonte/draft-v1.md](refonte/draft-v1.md) + [refonte/content-gutenberg.html](refonte/content-gutenberg.html).

- **Angle hybride** : comparatif Shopify vs WooCommerce complet (cible « shopify vs woocommerce », 170/mois, KD 1) AVEC section dropshipping (maintien position 5 sur « dropshipping shopify vs wordpress »).
- **H1 inchangé** + **slug inchangé** (protège l'acquis). SEO title : « Shopify vs WooCommerce : le comparatif complet (dropshipping inclus) ». Focus keyword : « shopify vs woocommerce, dropshipping shopify vs wordpress, dropshipping woocommerce ».
- **14 sections H2** : tableau récap, définitions, prix/frais, hébergement/domaine, thèmes/perso, facilité, fonctionnalités, paiement, SEO, support, migration, dropshipping, verdict + « À qui Shopify convient », FAQ (6 Q).
- **Ninja Table 2969337** créée (11 lignes × 3 colonnes, header vert brand `#00D400`) + intégrée en bloc `ninja-tables/guten-block`.
- **TOC** régénéré (14 entrées). **CTA Kadence** conservé. Affilié Shopify gardé, liens internes AliDropship + Rank Math.
- Termes gap couverts : frais de transaction, migration, thème/personnalisation, nom de domaine, moyens de paiement.
- ~2300 mots (vs 1688 avant). Brand vérifié : 0 vouvoiement, 0 em-dash, Rank Math (pas Yoast).

**Reste à faire (hors périmètre)** : article dédié « Comment faire du dropshipping avec WooCommerce » (cible « dropshipping woocommerce » 70/mois, intention how-to + fournisseurs).

## Verdict stratégique

Article **faible (34/100) ET à faible enjeu** : 0 clic en 6 mois, cluster micro-volume en déclin fort, sujet tangentiel au cœur schoolsWP.

**MAJ post-thruuu/DataForSEO (2026-05-29)** : KD = **1** sur « shopify vs woocommerce » (170/mois) et thruuu confirme qu'on est déjà **5e sur « dropshipping shopify vs wordpress »** (1688 mots = médiane). La cible est donc _winnable_ — le frein est la profondeur/fraîcheur, pas la difficulté. Détail : [thruuu/gap-analysis.md](thruuu/gap-analysis.md). « dropshipping woocommerce » (70/mois) est une **intention séparée** (how-to + fournisseurs) → article dédié, hors périmètre de cette page.

**Recommandation** : NE PAS engager une refonte lourde maintenant. Appliquer les **quick wins** (1 h de travail) pour aligner le ciblage, corriger les erreurs factuelles et les violations de marque pendant qu'elle est indexée — puis **décider explicitement** si le pilier ecommerce mérite un investissement de cluster. Sinon, candidate à la **consolidation** (fusion avec un futur hub ecommerce/WooCommerce) plutôt qu'à un article isolé maintenu.
