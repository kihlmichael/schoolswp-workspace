# Plan de formation : Boutique produits physiques (SureCart)

- **Parcours** : F3 (voir [\_architecture-parcours.md](_architecture-parcours.md))
- **Méthode (proposition)** : BOUTIQUE
- **Version** : v1.0 (plan)
- **Date** : 2026-06-04
- **Plateforme** : WordPress + SureCart, livrée sur TutorLMS
- **Niveau** : intermédiaire
- **Durée visée** : 4 à 5 h de vidéo, 9 sections (Module 0 + 8 modules + Bonus), ~50 leçons de 4 à 8 min
- **Prix (proposition)** : 197 € (offre de lancement 47-57 €), garantie 7 jours
- **Sources** : transcripts + docs dans [\_sources/](_sources/)

> Prix et nom de méthode = propositions, à valider.

## 1. Promesse et transformation

**Avant** : tu veux ouvrir ou tenir une boutique de produits physiques sur WordPress, mais tu redoutes la complexité (catalogue, variations, stock, expédition, taxes) et la lourdeur de WooCommerce.

**Après** : tu as une boutique complète : catalogue avec variations et stock, une vitrine soignée, l'expédition configurée, le traitement des commandes et le suivi de colis, et les taxes en règle, sur une base légère.

**Livrable final** : une boutique physique opérationnelle (catalogue + vitrine + expédition + 1 commande traitée de A à Z en live).

**KPI de l'élève** :

- 1 catalogue avec au moins 1 produit à variations et stock suivi
- 1 vitrine (page boutique) publiée
- 1 profil et zone d'expédition configurés
- 1 commande traitée : paiement, fulfillment, suivi de colis

## 2. Persona et positionnement

**Cible** : e-commerçant, artisan, marque, petite boutique qui vend des produits physiques et veut un e-commerce WordPress sans usine à gaz.

**Problèmes** : gérer stock, variations, zones d'expédition et taxes est intimidant ; WooCommerce et ses extensions sont lourds à maintenir.

**Objections** :

- « SureCart ne fait que du numérique » : on montre catalogue, stock, expédition et fulfillment.
- « Migrer depuis WooCommerce va tout casser » : on couvre l'import produits et la migration.
- « Les taxes physiques sont un casse-tête » : on traite zones, TVA et overrides.

**Différenciation** : un e-commerce physique complet mais léger, vitrine moderne et builders (Bricks, Elementor, Divi) pris en charge.

**Frontières** : ce parcours suppose les bases (installer, connecter, 1 page de paiement) vues vite en Module 1 ; la maîtrise complète de la caisse est dans le parcours F1. La monétisation de contenu (numérique, abos, paywall) relève du parcours Créateurs (F2).

## 3. Vue d'ensemble des modules

| Module | Titre                            | Durée    | Objectif                                      |
| ------ | -------------------------------- | -------- | --------------------------------------------- |
| M0     | Vendre du physique sur WordPress | ~20 min  | Cadrer le projet, migration WooCommerce       |
| M1     | Fondations express               | ~25 min  | Installer et encaisser, l'essentiel           |
| M2     | Construire ton catalogue         | ~40 min  | Produits, collections, variations, stock      |
| M3     | Ta vitrine                       | ~40 min  | Page boutique, fiches, panier, builders       |
| M4     | Expédition                       | ~35 min  | Profils, zones, méthodes et tarifs            |
| M5     | Commandes et fulfillment         | ~35 min  | Traiter, expédier, suivre les colis           |
| M6     | Taxes et conformité              | ~30 min  | TVA, taxes incluses, overrides, pays          |
| M7     | Acquisition et conversion        | ~30 min  | Order bumps, avis, coupons, SEO, multi-devise |
| M8     | Lancer                           | ~20 min  | Passer en live et planifier                   |
| Bonus  | Cas pratiques et la suite        | variable | Pratique + passerelles F1/F2                  |

## 4. Détail des modules

Chaque module finit par un quiz de 5 questions.

### Module 0 : Vendre du physique sur WordPress (lead magnet)

- 0.1 SureCart pour une vraie boutique : ce qu'il sait faire _(vidéo 07 ; surecart-product-types)_
- 0.2 SureCart ou WooCommerce pour le physique : comment choisir _(positionnement ; understanding-ecommerce-fees)_
- 0.3 Migrer depuis WooCommerce sans tout casser _(import-from-woocommerce ; migrate-to-surecart)_
- 0.4 Ce que tu vas construire dans cette formation _(getting-started)_

Livrable : fiche de décision boutique. Exercice : lister tes 3 premiers produits. Quiz.

### Module 1 : Fondations express

Objectif : poser le minimum technique (la maîtrise complète est dans F1).

- 1.1 Installer SureCart et connecter ton compte _(installing-surecart ; getting-started ; add-surecart-api)_
- 1.2 Connecter Stripe et PayPal _(connect-stripe ; connect-paypal)_
- 1.3 Une première page de paiement _(add-checkout-form ; vidéo 02)_
- 1.4 Mode test et passage en live _(how-to-make-test-payments ; clear-test-data)_

Livrable : checklist fondations. Exercice : réussir un paiement test. Quiz.

### Module 2 : Construire ton catalogue

- 2.1 Créer un produit physique _(create-product)_
- 2.2 Organiser en collections et catégories _(product-collections ; individual-collections)_
- 2.3 Créer des variations (taille, couleur) _(creating-and-managing-variants ; vidéo 22)_
- 2.4 Lier des images aux variations _(variant-images ; vidéo 29)_
- 2.5 Gérer le stock et l'inventaire _(inventory-management ; vidéo 22 ; change-product-availability)_
- 2.6 Importer tes produits en masse _(import-products-in-bulk)_

Livrable : structure de catalogue. Exercice : créer 1 produit à variations avec stock. Quiz.

### Module 3 : Ta vitrine (page boutique et fiches)

- 3.1 Créer ta page boutique _(vidéo 26 ; product-list-guide-shop-page)_
- 3.2 Personnaliser les listes de produits _(vidéo 18 ; filter-and-display-featured-products)_
- 3.3 Soigner la fiche produit _(vidéo 14 ; product-pages-guide ; product-content-description)_
- 3.4 Produits liés et vue rapide _(related-products ; quick-view-bricks)_
- 3.5 Le panier : panier coulissant et icône _(vidéo 17 ; slide-out-cart ; cart-toggle-icon ; cart-menu-icon-shortcode)_
- 3.6 Builders : Bricks, Elementor, Divi _(collection-template-bricks ; product-content-bricks ; product-card ; product-page-in-elementor ; product-content-elementor)_

Livrable : maquette de vitrine. Exercice : publier ta page boutique. Quiz.

### Module 4 : Expédition

- 4.1 Créer un profil d'expédition _(how-to-create-shipping-profiles)_
- 4.2 Zones, méthodes et tarifs d'expédition _(shipping-zone-methods-rates ; adding-shipping-methods-and-rates ; vidéo 20)_
- 4.3 Restreindre la vente à certains pays _(restrict-purchases-to-specific-countries)_

Livrable : grille d'expédition. Exercice : configurer 1 zone + 1 tarif. Quiz.

### Module 5 : Commandes et fulfillment

- 5.1 Traiter une commande de A à Z _(manage-customer-orders ; orders-receipts)_
- 5.2 Fulfillment et expédition _(order-fulfillment-and-shipping ; vidéo 19)_
- 5.3 Ajouter un numéro de suivi _(add-tracking-number)_
- 5.4 Factures et reçus _(create-invoices ; download-invoices)_
- 5.5 Rembourser une commande _(refund-an-order)_

Livrable : SOP de traitement de commande. Exercice : traiter 1 commande test jusqu'au suivi. Quiz.

### Module 6 : Taxes et conformité

- 6.1 Configurer les taxes et la TVA _(configure-tax-settings-in-surecart ; collect-tax-or-vat)_
- 6.2 TVA européenne et ventes transfrontalières _(sales-tax-eu-vat)_
- 6.3 Prix taxes incluses _(products-with-tax-included)_
- 6.4 Overrides de taxes produit et expédition _(override-product-and-shipping-taxes)_
- 6.5 Afficher la TVA entreprise sur la facture _(display-company-customer-tax-on-invoice)_

Livrable : checklist conformité fiscale. Exercice : paramétrer la TVA de ton pays. Quiz.

### Module 7 : Acquisition et conversion boutique

- 7.1 Order bumps et upsells _(order-bumps ; vidéo 08 ; enable-upsell-funnels ; vidéo 24)_
- 7.2 Récupérer les paniers abandonnés _(abandoned-checkout ; vidéos 09 et 27)_
- 7.3 Avis produits et preuve sociale _(product-reviews ; product-reviews-shortcodes)_
- 7.4 Coupons et promotions _(create-coupons ; create-discount-coupons)_
- 7.5 SEO de tes fiches produit _(product-seo)_
- 7.6 Vendre en plusieurs devises _(multi-currency)_

Livrable : plan d'acquisition boutique. Exercice : activer 1 order bump + les avis. Quiz.

### Module 8 : Lancer (passage à l'action)

- 8.1 Checklist finale test vers live
- 8.2 Ton plan de lancement boutique en 7 jours
- 8.3 Les 5 réflexes d'une boutique qui tourne

Livrable : plan de lancement 7 jours. Exercice : fixer ta date de lancement. Quiz final + certificat.

### Bonus : cas pratiques et la suite

- B.1 Cas pratique : lancer une boutique d'artisan de A à Z
- B.2 Cas pratique : migrer une petite boutique WooCommerce vers SureCart
- B.3 Dropshipping et print on demand : ce qui est possible avec SureCart, et ses limites _(create-product ; order-fulfillment-and-shipping)_
- B.4 Questions et réponses
- B.5 Et après : pour la caisse complète, parcours F1 ; pour vendre du numérique et des abos, parcours F2

## 5. Drip (7 jours)

- J1 : M0 + M1
- J2 : M2
- J3 : M3
- J4 : M4
- J5 : M5
- J6 : M6 + M7
- J7 : M8 + Bonus

## 6. Tunnel de vente

- **Lead magnet** : Module 0 (vidéo + fiche de décision boutique) contre email.
- **Séquence welcome** : 5 emails sur 5 jours, push achat à J5.
- **Offre de fond** : formation complète (197 €, lancement 47-57 €).
- **Upsell post-achat** : pack templates de fiches produit, ou audit 30 min.
- **Upsells de parcours** : F1 (caisse complète) et F2 (numérique et abos). Bundle des 3 (voir architecture).

Tags FluentCRM : `abonne_lead_magnet_boutique`, `acheteur_formation_surecart_boutique`, `lang_fr`.

## 7. Notes de production

- Voix : tutoiement, singulier solo, pas d'em-dash, brand schoolsWP.
- Le fichier source `guides-variant-swatches` (swatches de variantes, utile pour M2.4) a son code retiré (voir [\_README.md](_README.md)) : récupérer le code via son `source_url`.
- Prévoir des captures réelles pour expédition et taxes (réglages denses).
- Quiz : 5 questions par module, à rédiger en production.

## 8. Hors périmètre (renvoyé vers F1 et F2)

- **F1 (Vendre sans WooCommerce)** : maîtrise complète de l'installation, des processeurs de paiement, du checkout, des commandes et factures, des taxes de base.
- **F2 (Créateurs)** : produits numériques avancés, abonnements, paywall, espace membre, rétention, licences.
