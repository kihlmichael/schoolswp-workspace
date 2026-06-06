---
title: SureCart - Vendre en récurrent, abonnements simples (Module 5)
version: 1.0
last_updated: 2026-06-05
---

# Fiche - Vendre en récurrent avec SureCart

Garde cette fiche à côté de toi pendant le Module 5. Elle couvre les quatre leçons : créer un abonnement, ajouter un essai et des frais de mise en place, gérer les situations courantes, et lire tes indicateurs. À la fin du module, tu as un revenu récurrent solide et tu sais le piloter.

## Matrice : quelle offre récurrente pour ton activité ?

Choisis le modèle selon ce que tu vends, pas par mode.

| Modèle                              | Cas d'usage type                                                |
| ----------------------------------- | --------------------------------------------------------------- |
| Abonnement pur                      | Accès continu - communauté, outil SaaS, contenu premium         |
| Abonnement + essai gratuit          | Tu veux lever les freins à l'engagement avant le premier débit  |
| Abonnement + essai payant (1 euro)  | Tu veux filtrer les vrais acheteurs et réduire les abus d'essai |
| Abonnement + frais de mise en place | Prestation ou service : le démarrage demande du travail initial |
| Paiement échelonné                  | Étaler le prix d'une offre ponctuelle sans vrai récurrent       |

## Créer un abonnement _(Leçons 5.1 - 5.2)_

- [ ] **Partir d'un produit** : nouveau ou existant, dans le menu SureCart Produits.
- [ ] **Ajouter un prix abonnement** : Pricing, Add a Price (ou Add Another Price), nommer le prix (ex : Mensuel).
- [ ] **Choisir le type Subscription** : montant + intervalle (jour, semaine, mois, année). Cliquer sur Create Price.
- [ ] **Options à connaître** : Pay What You Want (prix libre) et Compare at Price (prix barré) disponibles au même endroit.
- [ ] **Plusieurs formules sur un même produit** : ajouter un deuxième prix (ex : accès à vie en unique + formule mensuelle en abonnement). Le client choisit dans le sélecteur de prix sur la page de paiement. _(Leçon 5.1)_
- [ ] **Récupérer le lien d'achat** : bouton Copy Links sur le prix, comme pour tout prix SureCart.

## Ajouter un essai et des frais de mise en place _(Leçon 5.2)_

### Mécanique de l'essai

Le client saisit ses informations bancaires au checkout mais n'est pas débité immédiatement. Il profite du produit pendant la durée de l'essai. Le premier débit a lieu à la fin de l'essai, ce qui marque le début de l'abonnement. SureCart envoie un rappel 3 jours avant la fin de l'essai.

### Ajouter un essai gratuit

- [ ] Éditer le produit, déplie le prix abonnement, activer le toggle **Free Trial**.
- [ ] Indiquer la durée (ex : 7 jours). Enregistrer.
- [ ] Vérifier sur la page de paiement que la mention "commence dans X jours" s'affiche.

### Ajouter des frais de mise en place

- [ ] Déplie le prix, activer le toggle **Setup Fee**.
- [ ] Renseigner un nom (affiché dans le récapitulatif, ex : Frais de mise en place) et un montant.
- [ ] Les frais de mise en place sont possibles seuls, sans essai.

### Transformer en essai payant

- [ ] Activer **Charge setup fee during free trial** : les frais sont débités immédiatement, l'abonnement normal démarre à la fin de l'essai.
- [ ] Nommer les frais "Essai première semaine" avec un petit montant (ex : 1 euro) pour créer un essai à 1 euro.

> Pourquoi un essai payant ? Un euro sépare les curieux des vrais acheteurs. Quelqu'un qui accepte de payer pour essayer est bien plus susceptible de rester. C'est un filtre simple, surtout pour un outil ou un accès.

### Anti-abus d'essai

- [ ] SureCart, **Settings**, **Subscriptions**, section Purchase Behavior, activer **Prevent Duplicate Trials**.

> Règle d'or : avec Prevent Duplicate Trials activé, un client qui a déjà bénéficié d'un essai sur ce produit est facturé au prix plein dès la prochaine tentative. Active cette option avant d'ouvrir l'essai au public.

### Exercice du module

Créer un abonnement mensuel avec essai gratuit de 7 jours. Vérifier l'affichage sur la page de paiement.

## Mémo technique

### Ajouter un essai gratuit étape par étape

```
Produit → Pricing → déplie le prix abonnement
→ Free Trial : ON → Durée : 7 → Enregistrer
→ Ouvrir la page de paiement → vérifier "commence dans 7 jours"
```

### Essai payant (1 euro)

```
Produit → Pricing → déplie le prix abonnement
→ Free Trial : ON → Durée : 7
→ Setup Fee : ON → Nom : "Essai première semaine" → Montant : 1
→ Charge setup fee during free trial : ON
→ Enregistrer
```

### Anti-abus

```
SureCart → Settings → Subscriptions → Purchase Behavior
→ Prevent Duplicate Trials : ON
```

## Gérer les abonnements _(Leçon 5.3)_

Tout part de **SureCart, Subscriptions** - ouvrir un abonnement - bouton **Actions**.

- [ ] **Changer la date de renouvellement** : Actions, Change Renewal Date, choisir la date, Update Subscription. Ce changement est global : toutes les échéances suivantes s'alignent sur cette date. Utile pour décaler une échéance à la demande d'un client, ou pour aligner tous les abonnés sur le 1er du mois.
- [ ] **Mettre en pause** : Actions, Pause Subscription. La pause démarre à la fin de la période déjà payée (pas immédiatement). Choisir la date de reprise. Pendant la pause, aucun prélèvement et les accès sont suspendus, puis rendus à la reprise. Reprise anticipée : Actions, Don't Pause, puis Resume Subscription.
- [ ] **Annuler** : Actions, Cancel Subscription. Deux options :
  - Annulation immédiate : accès coupé sur-le-champ.
  - Annulation en fin de période : le client garde l'accès jusqu'au terme, pas de nouveau débit. C'est en général la plus correcte vis-à-vis du client.
- [ ] **Restaurer un abonnement annulé** : Actions, Restore Now.

> Piège - Restaurer un abonnement totalement annulé déclenche immédiatement le prélèvement de la période suivante. SureCart t'en informe avec un message d'avertissement. Préviens ton client avant de confirmer, c'est plus honnête.

- [ ] **Mettre à jour les détails** : quantités, essai, moyen de paiement, activation du prorata (facturation au juste prix en cas de changement de formule en cours de période).
- [ ] **Accéder à la fiche client** : bouton View Customer - nom, email, téléphone, transactions, préférences email.

## Lire tes indicateurs d'abonnement _(Leçon 5.4)_

### Les 6 chiffres à connaître

| Indicateur            | Ce qu'il mesure                                      |
| --------------------- | ---------------------------------------------------- |
| Abonnements actifs    | Tous tes abonnés en cours (nouveaux + anciens)       |
| Nouveaux abonnements  | Nouvelles souscriptions sur la période               |
| Nouveaux essais       | Essais démarrés sur la période                       |
| MRR                   | Revenu récurrent mensuel - la santé de ton récurrent |
| MRR perdu             | Revenu parti (annulations, attrition)                |
| Échéances échelonnées | Somme des paiements échelonnés non encore réglés     |

Le MRR est le chiffre central. C'est lui qui résume où tu en es.

### Comment le MRR est calculé

- Abonnement mensuel : compte pour son montant mensuel exact.
- Abonnement annuel : divisé par 12 (ex : 300 euros/an = 25 euros de MRR).
- Abonnements quotidiens et hebdomadaires : ramenés au mois avec les bons coefficients.
- Paiements échelonnés : ne comptent PAS dans le MRR, ils sont suivis séparément dans les échéances en attente.

### Réglages pratiques

- [ ] Basculer entre **Live** et **Test** pour ne regarder que tes vraies données.
- [ ] Utiliser les **filtres de période** (semaine, mois) pour suivre une tendance.

### La table des abonnements

Filtres de statut disponibles : Tous, Actifs, En essai, En retard de paiement, Annulés.

> Le statut "en retard de paiement" mérite ton attention : ce sont des abonnés dont le prélèvement a échoué, souvent une carte expirée. Un email rapide peut récupérer ce revenu avant qu'il ne devienne une perte.

### Signaux à surveiller

- Ton MRR monte-t-il mois après mois ? C'est le signe que ton récurrent grandit.
- Trois alertes à surveiller : taux d'annulation élevé, MRR qui stagne, variations brutales inattendues.
- Le MRR perdu n'est pas qu'un chiffre déprimant : c'est ta meilleure boussole pour comprendre pourquoi tes clients partent, et donc quoi améliorer.

> Pour aller plus loin : réduire activement l'attrition et utiliser des outils comme le Subscription Saver est traité dans le parcours Créateurs. Ce module te donne l'abonnement simple et solide - c'est la bonne fondation.
