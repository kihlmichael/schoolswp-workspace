# Plan de formation : Vendre sans WooCommerce (SureCart)

- **Parcours** : F1 (voir [\_architecture-parcours.md](_architecture-parcours.md))
- **Méthode (proposition)** : CAISSE
- **Version** : v1.0 (plan)
- **Date** : 2026-06-04
- **Plateforme** : WordPress + SureCart, livrée sur TutorLMS
- **Niveau** : débutant à intermédiaire
- **Durée visée** : 4 à 5 h de vidéo, 9 sections (Module 0 + 8 modules + Bonus), ~51 leçons de 4 à 8 min
- **Prix (proposition)** : 197 € (offre de lancement 47-57 €), garantie 7 jours
- **Sources** : transcripts + docs dans [\_sources/](_sources/)

> Les prix et le nom de méthode sont des propositions, à valider.

## 1. Promesse et transformation

**Avant** : tu as un site WordPress, tu veux vendre (un service, un produit numérique, un abonnement, une offre simple), mais WooCommerce te semble lourd, lent et plein d'extensions à maintenir.

**Après** : tu encaisses des paiements ponctuels et récurrents sur ton site, avec une caisse légère, une page de paiement qui convertit, des factures propres et des leviers pour augmenter le panier, le tout sans usine à gaz.

**Livrable final** : une boutique SureCart opérationnelle (au moins 1 offre payante + 1 page de paiement en mode live) + un plan de lancement 7 jours.

**KPI de l'élève** :

- 1 produit payant et 1 produit gratuit créés
- 1 page de paiement publiée et testée
- 1 paiement réel encaissé (ou paiement test validé puis passage en live)
- 1 levier de panier activé (order bump, upsell ou panier abandonné)

## 2. Persona et positionnement

**Cible** : créateur, freelance, formateur, solopreneur, petite entreprise qui veut vendre sur WordPress sans devenir développeur ni administrer WooCommerce.

**Problèmes** : WooCommerce paraît surdimensionné pour vendre 1 à 10 offres simples ; trop d'extensions, de réglages, de poids ; peur des frais cachés et de la technique.

**Objections** :

- « SureCart, c'est encore un abonnement de plus » : on explique le modèle et les frais réels (pas de commission SureCart, seuls les frais Stripe s'appliquent).
- « Je vais être enfermé dans une plateforme » : on montre l'export des données et la portabilité.
- « WooCommerce est le standard » : on cadre les cas où SureCart est plus adapté, et ceux où WooCommerce reste pertinent (respect du concurrent).

**Différenciation vs WooCommerce** : légèreté, rapidité de mise en place, page de paiement moderne, abonnements et revenue boosters natifs, moins de maintenance.

**Frontières** (voir architecture) : cette formation ne couvre PAS en profondeur le contenu premium / paywall / membership (parcours Créateurs) ni la logistique physique avancée (parcours Boutique). Ces sujets sont effleurés puis renvoyés.

## 3. Vue d'ensemble des modules

| Module | Titre                                | Durée    | Objectif                                         |
| ------ | ------------------------------------ | -------- | ------------------------------------------------ |
| M0     | Comprendre : vendre sans WooCommerce | ~20 min  | Décider en connaissance de cause et se projeter  |
| M1     | Installer et connecter SureCart      | ~30 min  | Avoir une base technique propre                  |
| M2     | Créer tes offres                     | ~35 min  | Mettre en vente service, numérique, gratuit      |
| M3     | La page de paiement qui convertit    | ~40 min  | Publier un checkout efficace                     |
| M4     | Encaisser proprement                 | ~35 min  | Commandes, factures, coupons, taxes de base      |
| M5     | Vendre en récurrent                  | ~35 min  | Abonnements simples et essais                    |
| M6     | Augmenter le panier                  | ~30 min  | Order bumps, upsells, paniers abandonnés         |
| M7     | Après la vente                       | ~35 min  | Espace client, emails, intégrations, affiliation |
| M8     | Lancer                               | ~20 min  | Passer en live et planifier le lancement         |
| Bonus  | Cas pratiques et la suite            | variable | Mise en pratique + passerelles F2/F3             |

## 4. Détail des modules

Nomenclature : `M.L` (Module.Leçon). Chaque module finit par un quiz de 5 questions (validation pour débloquer la suite).

### Module 0 : Comprendre, vendre sur WordPress sans WooCommerce (lead magnet)

Objectif : aider l'élève à décider et à se projeter. Ce module est le candidat lead magnet (gratuit).

- 0.1 Le vrai coût de WooCommerce : extensions, poids, maintenance _(positionnement ; understanding-ecommerce-fees)_
- 0.2 SureCart en 5 minutes : plateforme + plugin, comment ça marche _(intro developer ; getting-started ; surecart-glossary)_
- 0.3 Les frais réels : frais processeur (Stripe/PayPal), commission 1,9 % du plan gratuit Launch (supprimée en Pro), et l'Application Fee Stripe _(stripe-application-fee ; understanding-ecommerce-fees)_
- 0.4 Pour qui SureCart est le bon choix, et quand WooCommerce reste pertinent _(positionnement ; surecart-product-types)_
- 0.5 Ce que tu vas savoir faire : tour rapide du tableau de bord _(getting-started)_

Livrable : fiche d'1 page « SureCart ou WooCommerce, comment choisir ». Exercice : décrire ton offre principale en 1 phrase. Quiz : modèle SureCart, frais, cas d'usage.

### Module 1 : Installer et connecter SureCart

Objectif : poser une base technique propre, prête à encaisser.

- 1.1 Installer le plugin et créer ton compte SureCart _(installing-surecart ; getting-started)_
- 1.2 Connecter le plugin à la plateforme avec la clé API _(add-surecart-api ; api-token-wp-config)_
- 1.3 Connecter Stripe (carte bancaire, Apple Pay) _(connect-stripe ; configuring-apple-pay)_
- 1.4 Connecter PayPal et les autres processeurs _(connect-paypal ; connect-mollie ; connect-razorpay ; connect-paystack)_
- 1.5 Réglages de base : devise, branding, logo clair et sombre _(switching-store-currency ; set-up-your-branding ; light-and-dark-logo)_
- 1.6 Traduire SureCart en français : interface et emails _(translating-surecart ; notification-language)_
- 1.7 SureCart et ton thème : apparence, dark mode, performance et cache _(set-dark-mode ; add-custom-css ; caching ; lsp-config ; plugin-performance)_
- 1.8 Le mode test et ton premier paiement de test _(how-to-make-test-payments ; clear-test-data)_

Livrable : checklist d'installation en 10 points. Exercice : réussir un paiement test. Quiz.

### Module 2 : Créer tes offres (produits et prix)

Objectif : mettre en vente une offre de service, un produit numérique et un produit gratuit.

- 2.1 Types de produits et types de paiement _(surecart-product-types ; payment-types-in-surecart)_
- 2.2 Créer ton premier produit et son prix (paiement unique) _(create-product ; setup-one-time-payment-type)_
- 2.3 Vendre un service (offre sans livraison) _(create-product appliqué)_
- 2.4 Vendre un produit numérique ou un téléchargement _(attach-files-to-products ; product-access-actions)_ — base, l'avancé est dans le parcours Créateurs
- 2.5 Offrir un produit gratuit (freebie, capture de lead) _(vidéo 06)_
- 2.6 Soigner la fiche produit : description et médias _(product-content-description ; product-pages-guide)_ — l'essentiel

Livrable : gabarit « structurer une offre ». Exercice : créer 1 produit payant + 1 produit gratuit. Quiz.

### Module 3 : La page de paiement qui convertit (checkout)

Objectif : publier un formulaire de paiement efficace et personnalisé.

- 3.1 Créer un formulaire de checkout _(add-checkout-form ; vidéo 02)_
- 3.2 Éditer et personnaliser les blocs du formulaire _(edit-checkout-form)_
- 3.3 Ajouter des champs personnalisés _(vidéo 04 ; product-page-custom-fields)_
- 3.4 Ajouter les conditions générales au checkout _(vidéo 03 ; adding-terms-conditions-in-checkout)_
- 3.5 Login, compte client ou achat invité _(vidéo 05 ; guest-checkout)_
- 3.6 Instant Checkout et liens d'achat directs _(vidéo 12 ; instant-checkout-pages ; creating-custom-buy-links)_
- 3.7 Page de paiement produit unique, dupliquer un formulaire, page de remerciement _(vidéo 11 ; vidéo 10 ; custom-thank-you-page)_
- 3.8 La puissance du bloc conditionnel : afficher champs ou messages selon des conditions _(conditional-block)_
- 3.9 Le panier : ajout au panier et panier coulissant _(vidéo 17 ; slide-out-cart ; cart-toggle-icon)_

Livrable : template de page de paiement réutilisable. Exercice : publier 1 page de paiement. Quiz.

### Module 4 : Encaisser proprement (commandes, factures, taxes de base)

Objectif : gérer ses ventes au quotidien et rester en règle.

- 4.1 Comprendre commandes et reçus _(orders-receipts ; manage-customer-orders)_
- 4.2 Générer et envoyer des factures _(create-invoices ; download-invoices ; vidéo 25)_
- 4.3 Rembourser une commande _(refund-an-order)_
- 4.4 Créer des coupons et codes promo _(create-coupons ; create-discount-coupons)_
- 4.5 Taxes et TVA, la base _(configure-tax-settings-in-surecart ; collect-tax-or-vat ; sales-tax-eu-vat)_ — les cas avancés sont dans le parcours Boutique
- 4.6 Passer du mode test au mode live en sécurité _(how-to-make-test-payments ; clear-test-data)_

Livrable : checklist conformité paiement (test vers live + TVA). Exercice : créer 1 coupon -20 %. Quiz.

### Module 5 : Vendre en récurrent (abonnements simples)

Objectif : mettre en place une offre récurrente sans complexité.

- 5.1 Créer un abonnement _(setup-subscription-payment-type ; managing-subscriptions)_
- 5.2 Essais gratuits, essais payants, frais de mise en place _(vidéo 13 ; vidéo 01 ; trial-subscription ; set-up-fee-on-trials)_
- 5.3 Gérer un abonnement : pause, annulation, date de renouvellement _(vidéo 16 ; pause-subscription ; how-to-cancel-the-subscriptions-in-surecart ; change-subscription-date)_
- 5.4 Lire tes indicateurs d'abonnement _(subscription-insights)_

Note : la rétention avancée (Subscription Saver, Upgrade Groups, Price Boost) est traitée dans le parcours Créateurs.

Livrable : matrice « quelle offre récurrente pour ton activité ». Exercice : créer 1 abonnement mensuel avec essai 7 jours. Quiz.

### Module 6 : Augmenter le panier (revenue boosters)

Objectif : activer les leviers natifs de SureCart pour vendre plus, sans extension.

- 6.1 Order bumps : l'upsell en 1 clic au checkout _(vidéo 08 ; order-bumps ; order-bump-placement)_
- 6.2 Tunnels d'upsell après l'achat _(vidéo 24 ; enable-upsell-funnels ; update-upsell-countdown-timer)_
- 6.3 Récupérer les paniers abandonnés _(vidéos 09 et 27 ; abandoned-checkout ; see-abandoned-orders)_
- 6.4 Quick Add et achat rapide _(vidéo 28)_

Livrable : plan d'optimisation du panier (3 leviers à activer). Exercice : activer 1 order bump. Quiz.

### Module 7 : Après la vente (espace client, emails, intégrations, affiliation)

Objectif : fidéliser, automatiser et amorcer la croissance.

- 7.1 L'espace client : tableau de bord et self-service _(vidéo 15 ; overview-customer-dashboard ; customers-access-dashboard)_
- 7.2 Personnaliser emails et notifications _(vidéo 21 ; customize-email-templates ; customer-email-notifications ; notification-language)_
- 7.3 Connecter FluentCRM et tes automatisations _(sync-users-with-surecart)_ — l'essentiel
- 7.4 Suivre tes ventes : Google Analytics et Pixel _(track-events-with-ga ; track-events-with-fbpixels)_ — l'essentiel
- 7.5 Affiliation (intégré léger) : à quoi ça sert et quand l'utiliser _(vidéo 23 ; surecart-affiliate-platform ; affiliate-program)_
- 7.6 Affiliation : activer une base simple et des coupons d'apporteurs d'affaires _(create-affiliate-coupon-codes ; managing-the-affiliates)_
- 7.7 Connecter SureCart à (presque) tout : automatisations, webhooks et l'IA avec Abilities _(surecart-abilities ; webhooks ; sync-users-with-surecart ; integrating-analytics)_

Livrable : checklist « outils connectés + 1er affilié ». Exercice : paramétrer l'email de confirmation de commande. Quiz.

### Module 8 : Lancer (passage à l'action)

Objectif : passer en live et planifier le lancement.

- 8.1 Checklist finale : passage test vers live _(récapitulatif)_
- 8.2 Ton plan de lancement en 7 jours
- 8.3 Les 5 réflexes pour vendre proprement dans la durée

Livrable : plan de lancement 7 jours (template). Exercice : fixer ta date de lancement. Quiz final + certificat.

### Bonus : cas pratiques et la suite

- B.1 Cas pratique complet : vendre une prestation de service de A à Z
- B.2 Cas pratique complet : vendre un ebook ou un template numérique
- B.3 Éviter et résoudre les soucis courants : cache, conflits, store déconnecté _(initial-troubleshooting ; fix-surecart-store-disconnected ; caching)_
- B.4 Questions et réponses (alimenté par les vraies questions des élèves)
- B.5 Et après : si tu vends du contenu premium, direction le parcours Créateurs ; si tu vends du physique, direction le parcours Boutique

## 5. Drip (déblocage progressif sur 7 jours)

- J1 : Module 0 (comprendre) + Module 1 (installer)
- J2 : Module 2 (créer tes offres)
- J3 : Module 3 (page de paiement)
- J4 : Module 4 (encaisser)
- J5 : Module 5 (abonnements)
- J6 : Module 6 (panier) + Module 7 (après la vente)
- J7 : Module 8 (lancer) + Bonus

## 6. Tunnel de vente

- **Lead magnet** : Module 0 (vidéo + fiche « SureCart ou WooCommerce ») contre email.
- **Séquence welcome** : 5 emails sur 5 jours, push achat à J5.
- **Offre de fond** : la formation complète (197 €, lancement 47-57 €).
- **Upsell post-achat** : audit 30 min ou pack templates de pages de paiement.
- **Cross-sell / upsells de parcours** : parcours Créateurs et parcours Boutique (voir Option B dans l'architecture). Bundle des 3 quand ils existent (Option A).
- **Dogfooding** : vendre cette formation via SureCart lui-même (order bump = bundle, upsells = autres parcours).

Tags FluentCRM (à créer) : `abonne_lead_magnet_surecart`, `acheteur_formation_surecart_caisse`, `lang_fr`.

## 7. Notes de production

- Voix : tutoiement, singulier solo, pas d'em-dash, brand schoolsWP.
- Chaque leçon référence ses sources (transcripts numérotés et slugs de docs dans [\_sources/](_sources/)).
- 6 fichiers sources ont leurs blocs de code retirés (voir [\_README.md](_README.md)) : récupérer le code via leur `source_url` pour les leçons techniques (Instant Checkout, shortcodes, dashboard permalinks).
- Quiz : 5 questions par module, à rédiger en phase de production (un thème par leçon clé).

## 8. Hors périmètre (renvoyé vers F2 et F3)

- **Parcours Créateurs (F2)** : paywall, espace membre, accès premium, licences, gating LearnDash/TutorLMS, Subscription Saver, Upgrade Groups, Price Boost, dunning, multi-currency digital.
- **Parcours Boutique (F3)** : catalogue et variations avancées, stock, zones et tarifs d'expédition, fulfillment, entrepôts, suivi de colis, taxes avancées et overrides.
