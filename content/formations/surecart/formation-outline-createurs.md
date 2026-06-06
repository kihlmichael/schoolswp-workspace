# Plan de formation : Créateurs, numérique, abos, paywall (SureCart)

- **Parcours** : F2 (voir [\_architecture-parcours.md](_architecture-parcours.md))
- **Méthode (proposition)** : PREMIUM
- **Version** : v1.0 (plan)
- **Date** : 2026-06-04
- **Plateforme** : WordPress + SureCart, livrée sur TutorLMS
- **Niveau** : intermédiaire
- **Durée visée** : 4 à 5 h de vidéo, 9 sections (Module 0 + 8 modules + Bonus), ~50 leçons de 4 à 8 min
- **Prix (proposition)** : 197 € (offre de lancement 47-57 €), garantie 7 jours
- **Sources** : transcripts + docs dans [\_sources/](_sources/)

> Prix et nom de méthode = propositions, à valider.

## 1. Promesse et transformation

**Avant** : tu crées du contenu, tu as une audience ou une expertise, mais tu peines à la monétiser proprement (numérique, abonnements, accès premium) sans empiler les outils.

**Après** : tu vends tes produits numériques, tu encaisses des abonnements récurrents, tu protèges ton contenu premium derrière un paiement, et tu maximises chaque client (rétention, montée en gamme), le tout sur ton site.

**Livrable final** : un système de monétisation de contenu opérationnel (au moins 1 produit numérique ou abonnement live + 1 accès premium protégé) + un plan de rétention.

**KPI de l'élève** :

- 1 produit numérique ou abonnement créé et vendu
- 1 contenu premium protégé par l'achat
- 1 levier de rétention activé (Subscription Saver, upgrade, ou relance)
- 1 séquence email post-achat en place

## 2. Persona et positionnement

**Cible** : créateur de contenu, formateur, coach, expert, indépendant qui veut vivre de son contenu et de son expertise.

**Problèmes** : outils de membership coûteux et rigides, abonnements compliqués à gérer, contenu premium mal protégé, churn non maîtrisé.

**Objections** :

- « Il me faut un plugin de membership lourd » : on montre comment SureCart gère l'accès au produit et se branche au gating de cours.
- « Gérer des abonnements, c'est risqué » : on couvre essais, pause, annulation, relance d'échec de paiement.
- « Je vais perdre mes abonnés » : on installe les leviers de rétention natifs.

**Différenciation** : abonnements, essais, accès premium et rétention gérés nativement, sans empiler 4 extensions.

**Frontières** : ce parcours suppose les bases (installer, connecter, 1 page de paiement) vues vite en Module 1 ; la maîtrise complète de la caisse est dans le parcours « Vendre sans WooCommerce » (F1). La logistique physique relève du parcours Boutique (F3).

## 3. Vue d'ensemble des modules

| Module | Titre                               | Durée    | Objectif                                      |
| ------ | ----------------------------------- | -------- | --------------------------------------------- |
| M0     | Monétiser ton contenu sur WordPress | ~20 min  | Choisir le bon modèle (numérique, abo, accès) |
| M1     | Fondations express                  | ~25 min  | Installer et encaisser, l'essentiel           |
| M2     | Vendre des produits numériques      | ~35 min  | Téléchargements, accès, licences              |
| M3     | Abonnements et accès récurrents     | ~40 min  | Abos, essais, frais, paiement échelonné       |
| M4     | Paywall, espace membre et gating    | ~40 min  | Protéger et livrer le contenu premium         |
| M5     | Rétention et revenu récurrent       | ~40 min  | Subscription Saver, upgrades, relances        |
| M6     | Dons et modèles alternatifs         | ~20 min  | Donations, prix libre                         |
| M7     | International et preuve sociale     | ~30 min  | Multi-devise, avis, coupons de lancement      |
| M8     | Lancer                              | ~20 min  | Passer en live et planifier                   |
| Bonus  | Cas pratiques et la suite           | variable | Pratique + passerelles F1/F3                  |

## 4. Détail des modules

Chaque module finit par un quiz de 5 questions.

### Module 0 : Monétiser ton contenu sur WordPress (lead magnet)

- 0.1 Les 4 façons de monétiser : numérique, abonnement, accès premium, donation _(positionnement ; surecart-product-types ; payment-types-in-surecart)_
- 0.2 SureCart pour les créateurs : ce qu'il fait nativement _(intro developer ; getting-started)_
- 0.3 Choisir ton modèle selon ton audience et ton contenu _(positionnement)_
- 0.4 Ce que tu vas construire dans cette formation _(getting-started)_

Livrable : fiche « quel modèle de monétisation pour toi ». Exercice : choisir ton modèle principal. Quiz.

### Module 1 : Fondations express

Objectif : poser le minimum technique pour encaisser (la maîtrise complète est dans F1).

- 1.1 Installer SureCart et connecter ton compte _(installing-surecart ; getting-started ; add-surecart-api)_
- 1.2 Connecter Stripe et PayPal _(connect-stripe ; connect-paypal)_
- 1.3 Une première page de paiement en 5 minutes _(add-checkout-form ; vidéo 02)_
- 1.4 Mode test et passage en live _(how-to-make-test-payments ; clear-test-data)_

Livrable : checklist fondations. Exercice : réussir un paiement test. Quiz.

### Module 2 : Vendre des produits numériques

- 2.1 Créer un produit numérique et attacher les fichiers _(create-product ; attach-files-to-products)_
- 2.2 Gérer l'accès au produit : accorder, révoquer, expirer _(product-access-actions)_
- 2.3 Vendre une licence (logiciel, thème, plugin, ressource) _(licensing-setup-and-functionality ; enable-manage-license-addon)_
- 2.4 Décliner ton offre en formules (variantes de prix) _(creating-and-managing-variants)_
- 2.5 Une fiche produit numérique qui vend : images, vidéos _(vidéo 29 ; vidéo 14 ; product-content-description)_

Livrable : gabarit d'offre numérique. Exercice : mettre en vente 1 produit numérique avec fichier. Quiz.

### Module 3 : Abonnements et accès récurrents

- 3.1 Créer un abonnement _(setup-subscription-payment-type ; managing-subscriptions ; vidéo 16)_
- 3.2 Essais gratuits, essais payants, frais de mise en place _(vidéo 13 ; vidéo 01 ; trial-subscription ; set-up-fee-on-trials ; product-with-free-trials)_
- 3.3 Réductions de première fois pour booster les inscriptions _(add-first-time-subscription-discounts)_
- 3.4 Paiement échelonné (installments) _(setup-installment-payment-type ; pay-off-remaining-balance-on-installment-plan)_
- 3.5 Transition annuel vers mensuel automatique _(automatically-change-subscription)_
- 3.6 Lire tes indicateurs d'abonnement _(subscription-insights)_

Livrable : matrice d'offres récurrentes. Exercice : créer 1 abo avec essai + 1 paiement échelonné. Quiz.

### Module 4 : Paywall, espace membre et gating de contenu

- 4.1 Le principe : l'achat débloque l'accès _(product-access-actions ; purchases developer)_
- 4.2 Protéger des cours : intégration LearnDash _(learndash-courses-and-groups)_
- 4.3 Brancher TutorLMS via automatisation (FluentCRM / OttoKit) _(sync-users-with-surecart)_ — schéma d'intégration
- 4.4 L'espace membre : tableau de bord, abonnements, factures côté client _(overview-customer-dashboard ; subcription-in-customer-dashboard ; customers-access-dashboard)_
- 4.5 Laisser le client gérer son compte et son paiement _(customers-update-payment ; customers-update-account ; customers-change-password)_
- 4.6 Rôles, permissions et synchronisation des utilisateurs _(user-roles-and-permissions ; sync-users-with-surecart)_

Livrable : schéma « achat vers accès » de ton offre. Exercice : protéger 1 contenu premium. Quiz.

### Module 5 : Rétention et maximisation du revenu récurrent

- 5.1 Subscription Saver : récupérer les abonnés qui partent _(subscription-saver)_
- 5.2 Upgrade Groups : faire monter en gamme _(upgrade-groups ; customers-upgrade-downgrade-subscription)_
- 5.3 Price Boost : encourager l'annuel _(price-boost)_
- 5.4 Tarification dynamique _(dynamic-pricing)_
- 5.5 Gérer pause, annulation, changement de date _(pause-subscription ; how-to-cancel-the-subscriptions-in-surecart ; change-subscription-date ; upgrading-downgrading-cancellation-of-subscriptions)_
- 5.6 Relancer les paiements échoués (dunning) _(manually-retry-failed-payments ; failed-payments-purchase-behavior ; reactivate-subscriptions-using-customer-dashboard)_

Livrable : plan de rétention (3 leviers). Exercice : activer Subscription Saver + 1 upgrade group. Quiz.

### Module 6 : Dons et modèles alternatifs

- 6.1 Mettre en place les donations _(setup-donations-with-surecart)_
- 6.2 Créer un formulaire de don _(create-donation-form)_
- 6.3 Prix libre et « paie ce que tu veux » _(dynamic-pricing)_

Livrable : page de don ou prix libre. Exercice : publier 1 offre à prix libre. Quiz.

### Module 7 : International et preuve sociale

- 7.1 Vendre en plusieurs devises _(multi-currency)_
- 7.2 Activer et afficher les avis produits _(product-reviews ; product-reviews-shortcodes)_
- 7.3 Importer tes avis existants _(how-to-import-reviews-in-surecart)_
- 7.4 Coupons et codes de lancement _(create-coupons ; create-discount-coupons)_
- 7.5 Emails et notifications côté client _(customize-email-templates ; customer-email-notifications)_

Livrable : checklist « confiance et international ». Exercice : activer les avis + 1 coupon de lancement. Quiz.

### Module 8 : Lancer (passage à l'action)

- 8.1 Checklist finale test vers live
- 8.2 Ton plan de lancement créateur en 7 jours
- 8.3 Les 5 réflexes pour des revenus récurrents durables

Livrable : plan de lancement 7 jours. Exercice : fixer ta date de lancement. Quiz final + certificat.

### Bonus : cas pratiques et la suite

- B.1 Cas pratique : vendre un abonnement à une bibliothèque de ressources
- B.2 Cas pratique : protéger une formation derrière un paiement
- B.3 Questions et réponses
- B.4 Et après : pour la caisse complète, parcours F1 ; pour vendre du physique, parcours F3

## 5. Drip (7 jours)

- J1 : M0 + M1
- J2 : M2
- J3 : M3
- J4 : M4
- J5 : M5
- J6 : M6 + M7
- J7 : M8 + Bonus

## 6. Tunnel de vente

- **Lead magnet** : Module 0 (vidéo + fiche « quel modèle de monétisation ») contre email.
- **Séquence welcome** : 5 emails sur 5 jours, push achat à J5.
- **Offre de fond** : formation complète (197 €, lancement 47-57 €).
- **Upsell post-achat** : pack templates d'emails de rétention, ou audit 30 min.
- **Upsells de parcours** : F1 (caisse complète) et F3 (physique). Bundle des 3 (voir architecture).

Tags FluentCRM : `abonne_lead_magnet_createurs`, `acheteur_formation_surecart_premium`, `lang_fr`.

## 7. Notes de production

- Voix : tutoiement, singulier solo, pas d'em-dash, brand schoolsWP.
- Le gating TutorLMS via SureCart n'est pas natif : prévoir une leçon « schéma d'automatisation » (FluentCRM ou OttoKit) plutôt qu'une intégration clé en main.
- `licensing-setup-and-functionality` est un fichier source au code retiré (voir [\_README.md](_README.md)) : récupérer le code via son `source_url`.
- Quiz : 5 questions par module, à rédiger en production.

## 8. Hors périmètre (renvoyé vers F1 et F3)

- **F1 (Vendre sans WooCommerce)** : maîtrise complète de l'installation, des processeurs de paiement, du checkout, des commandes, des factures et des taxes de base.
- **F3 (Boutique physique)** : catalogue, variations produit physiques, stock, expédition, fulfillment, suivi de colis, taxes avancées.
