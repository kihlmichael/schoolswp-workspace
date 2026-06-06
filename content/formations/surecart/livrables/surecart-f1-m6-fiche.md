---
title: SureCart - Plan d'optimisation du panier (Module 6)
version: 1.0
last_updated: 2026-06-05
---

# Plan d'optimisation du panier - 3 leviers à activer

Garde cette fiche à côté de toi pour le Module 6. Elle te sert à choisir les trois leviers les plus pertinents pour ton offre, puis à les activer dans le bon ordre. Tous les points renvoient à la leçon qui les couvre en détail.

---

## Les 4 leviers disponibles

### Levier 1 - Order bump (offre au moment du paiement)

- [ ] **Créé et activé** : SureCart, Order Bumps, Add New. Produit et prix choisis, conditions d'affichage posées. _(Leçon 6.1)_
- [ ] **Conditions d'affichage réglées** : au moins une condition par produit ou par prix (l'un / tous / aucun). _(Leçon 6.1)_
- [ ] **Remise définie** : pourcentage ou montant fixe, assez significative pour ne pas demander de réflexion. _(Leçon 6.1)_
- [ ] **Présentation complète** : nom, description, texte d'appel à l'action renseignés (surtout si le produit n'a pas d'image). _(Leçon 6.1)_
- [ ] **Priorité réglée (1 à 5)** : si plusieurs bumps peuvent s'afficher sur le même formulaire. _(Leçon 6.1)_
- [ ] **Bloc Order Bumps placé dans le formulaire** : drag and drop à l'endroit voulu, libellé personnalisé. _(Leçon 6.1)_

> Rappel important : les order bumps font partie des plans **Pro et Business** de SureCart. Sur le plan gratuit, cette section ne sera pas disponible.

---

### Levier 2 - Tunnel d'upsell (offre après l'achat)

- [ ] **Tunnel créé** : SureCart, Funnels, Add New. Nom interne, déclencheur (produit acheté), étape d'upsell (produit + remise). _(Leçon 6.2)_
- [ ] **Comportement choisi** : ajouter à la commande (pour cumuler) ou remplacer toute la commande (pour la montée en gamme). _(Leçon 6.2)_
- [ ] **Enchaînement pensé** : upsell 1, upsell 2 si accepté, downsell si refusé - ou une seule étape si plus simple. _(Leçon 6.2)_
- [ ] **"Ignorer si déjà acheté" activé** : évite de proposer au client ce qu'il possède déjà. _(Leçon 6.2)_
- [ ] **Page d'upsell créée** : une page WordPress avec le bloc Upsell de SureCart, reliée au tunnel. _(Leçon 6.2)_
- [ ] **Minuteur réglé si besoin** : par défaut 30 min. Si tu veux l'ajuster : SureCart, Settings, Orders & Invoices, section Upsells. _(Leçon 6.2)_
- [ ] **Moyens de paiement vérifiés** : si tu utilises iDEAL ou Bancontact via Mollie, ne pas activer d'upsell sur ces produits - uniquement carte et SEPA. _(Leçon 6.2)_

---

### Levier 3 - Récupération des paniers abandonnés

- [ ] **Fonction activée** : SureCart, Settings, Abandoned Checkout, Enable. _(Leçon 6.3)_
- [ ] **Calendrier des 3 emails réglé** : premier email (par défaut 1h), deuxième (ex. 3h), dernier ou désactivé selon ton choix. _(Leçon 6.3)_
- [ ] **Remise de récupération configurée (optionnel)** : montant fixe ou pourcentage, code unique auto, dans l'email choisi, expiration possible. _(Leçon 6.3)_
- [ ] **Mode test validé** : teste avant d'ouvrir en live. _(Leçon 6.3)_
- [ ] **Statistiques consultées** : Orders, Abandoned - paniers récupérables, récupérés, taux. _(Leçon 6.3)_

> Règle d'or : la récupération de paniers est conforme au RGPD nativement. Elle ne demande qu'une activation et quelques minutes de réglage. C'est le levier avec le meilleur rapport effort / résultat.

---

### Levier 4 - Quick Add (achat rapide depuis la boutique)

- [ ] **Bloc Quick Add ajouté** : éditeur de la page boutique, vue en liste, dans la carte produit - ou remplacé par un design prêt à l'emploi incluant déjà le bouton. _(Leçon 6.4)_
- [ ] **Bouton personnalisé** : affichage (icône / texte / les deux), texte libre, ajout direct si pas d'options, styles adaptés à ta marque. _(Leçon 6.4)_
- [ ] **Fenêtre personnalisée si besoin** : Apparence, Design, Patterns, modèle Product Quick Add. _(Leçon 6.4)_

> Ce levier est pertinent seulement si tu as un vrai catalogue, plusieurs produits que le client parcourt et combine. Pour une ou deux offres identifiées, l'Instant Checkout reste plus adapté.

---

## Mémo technique

### Order bump : logique des conditions d'affichage

Tu peux empiler plusieurs conditions. La logique disponible par condition :

- **L'un de ces produits/prix est au panier** : le bump s'affiche dès qu'un des éléments listés est présent.
- **Tous ces produits/prix sont au panier** : le bump ne s'affiche que si tous les éléments sont présents.
- **Aucun de ces produits/prix n'est au panier** : le bump s'affiche uniquement si aucun n'est présent.

```
Exemple :
Produit déclencheur : Formation LMS WordPress
Produit bump : Modèle de cours prêt à l'emploi (- 40 %)
Condition : "Formation LMS WordPress est au panier"
Résultat : le bump ne s'affiche qu'aux acheteurs de la formation.
```

### Upsell : ajouter vs remplacer

| Comportement                | Cas d'usage                                                            |
| --------------------------- | ---------------------------------------------------------------------- |
| Ajouter à la commande       | Produit supplémentaire (ex. extension, modèle, bonus)                  |
| Remplacer toute la commande | Montée en gamme réelle (ex. mensuel -> annuel, formule Starter -> Pro) |

### Récupération de paniers : les garde-fous natifs

SureCart intègre plusieurs protections automatiques :

- Les emails s'arrêtent dès que la commande est finalisée - pas de message gênant après achat.
- Option "ignorer si le produit est déjà acheté" disponible.
- Délai de grâce configurable avant le premier rappel.
- Mode test pour valider sans déclencher de vrais emails.

### Ordre de grandeur honnête

La récupération de paniers ramène souvent de l'ordre de 10 à 20 % de revenu en plus, sans publicité ni effort supplémentaire. Ce chiffre dépend de ton offre et de ton trafic : c'est un ordre de grandeur, pas une garantie. Mais c'est du revenu que tu laisses sur la table si tu n'actives pas la fonction.

---

## Ton plan d'optimisation

Coche ici les trois leviers que tu actives en priorité, en fonction de ton offre et de ton plan SureCart :

- [ ] **Order bump** - pertinent si tu as un complément logique à proposer au checkout (plan Pro/Business requis)
- [ ] **Tunnel d'upsell** - pertinent si tu peux proposer une montée en gamme ou un produit additionnel après l'achat
- [ ] **Récupération des paniers abandonnés** - pertinent pour tous, quel que soit ton plan
- [ ] **Quick Add** - pertinent si tu as plusieurs produits sur une page boutique

> Commence par la récupération des paniers abandonnés si tu hésites : c'est le levier le plus universel, le plus rapide à activer, et le seul disponible sur tous les plans.
