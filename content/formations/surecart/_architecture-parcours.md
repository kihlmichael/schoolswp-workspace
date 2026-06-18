# SureCart - Architecture des parcours

> Vision d'ensemble décidée le 2026-06-04.
> 3 parcours SureCart distincts, chacun vendable seul, en bundle, ou comme point d'entrée d'un tunnel d'upsells.
> Sources brutes communes : voir [\_README.md](_README.md).

## Les 3 parcours

| #   | Parcours                             | Méthode (proposition)  | Promesse                                                                        | Cible                                                                                                                                     | Statut                                                                           |
| --- | ------------------------------------ | ---------------------- | ------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| F1  | Vendre sans WooCommerce              | CAISSE                 | Encaisser des paiements sur WordPress, simplement, sans la lourdeur WooCommerce | Créateurs, freelances, formateurs, solopreneurs, TPE qui vendent services, produits numériques, formations, abonnements ou offres simples | **En cours** : plan détaillé dans [formation-outline.md](formation-outline.md)   |
| F2  | Créateurs : numérique, abos, paywall | PREMIUM (proposition)  | Monétiser ton contenu : numérique, abonnements, accès premium, espace membre    | Créateurs de contenu, formateurs, coachs, experts, indépendants                                                                           | **Plan prêt** : [formation-outline-createurs.md](formation-outline-createurs.md) |
| F3  | Boutique produits physiques          | BOUTIQUE (proposition) | Vendre des produits physiques sur WordPress : catalogue, stock, expédition      | E-commerçants, artisans, marques, petites boutiques                                                                                       | **Plan prêt** : [formation-outline-physique.md](formation-outline-physique.md)   |

## Frontières entre parcours (anti-recouvrement)

F1 est le socle généraliste. Il reste centré sur « vendre vite et proprement » et n'effleure que volontairement ce qui appartient aux deux parcours spécialisés.

- **F1 garde** : installation, connexion Stripe/PayPal, produits simples (service, numérique simple, gratuit), page de paiement, encaissement, factures, coupons, taxes de base, abonnements simples, revenue boosters de base (order bumps, upsells, paniers abandonnés), espace client, emails, affiliation en intégré léger.
- **F2 absorbe** (le numérique avancé) : paywall, espace membre, accès premium, licences, gating LearnDash / TutorLMS, rétention avancée (Subscription Saver, Upgrade Groups, Price Boost), dunning, multi-currency pour le digital.
- **F3 absorbe** (le physique avancé) : catalogue et variations avancées, gestion de stock, zones et tarifs d'expédition, fulfillment, entrepôts, suivi de colis, taxes avancées (VAT/EU, overrides).

Règle : si une notion relève clairement de F2 ou F3, F1 la mentionne en 1 phrase et renvoie vers le parcours dédié (voir module Bonus de F1).

## Logique commerciale

### Option A : bundle

Les 3 parcours sont vendus séparément, puis un bundle complet (les 3 réunis) est proposé. Le bundle peut être mis en avant directement à la caisse (order bump ou upsell post-achat), idéalement via SureCart lui-même (effet de démonstration : la formation SureCart est vendue avec SureCart).

### Option B : tunnel d'upsells

Chaque parcours devient un point d'entrée. Les deux autres deviennent upsell 1 et upsell 2.

| Point d'entrée                       | Upsell 1                             | Upsell 2                    |
| ------------------------------------ | ------------------------------------ | --------------------------- |
| Vendre sans WooCommerce              | Créateurs : numérique, abos, paywall | Boutique produits physiques |
| Créateurs : numérique, abos, paywall | Vendre sans WooCommerce              | Boutique produits physiques |
| Boutique produits physiques          | Créateurs : numérique, abos, paywall | Vendre sans WooCommerce     |

## Recommandation de déploiement

1. Lancer **F1** en premier (angle le plus large, le plus simple à comprendre).
2. Construire **F2** puis **F3** ensuite.
3. Activer le **tunnel d'upsells** dès que 2 parcours existent.
4. Activer le **bundle** quand les 3 existent.

## Stack de livraison (commune aux 3 parcours)

- **LMS** : TutorLMS (cours, leçons, drip, quiz, certificat)
- **Caisse** : SureCart (dogfooding recommandé) ou FluentCart
- **CRM / email** : FluentCRM (séquence welcome, segmentation par tags)
- Référence méthode : template formation schoolsWP (Module 0 mindset, modules cœur, module action, bonus ; leçons de 4 à 8 min ; drip 5 à 7 jours).
