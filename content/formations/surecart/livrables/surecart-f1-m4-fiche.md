---
title: SureCart - Checklist conformité paiement (Module 4)
version: 1.0
last_updated: 2026-06-05
---

# Checklist conformité paiement SureCart

Garde cette fiche à portée de main pendant le Module 4 et pour chaque nouvelle offre que tu mets en ligne. Elle couvre les réglages du quotidien (commandes, factures, remboursements, coupons, taxes) et le passage du mode test au mode live. Coche chaque point dans l'ordre.

---

## 1. Suivi des commandes et reçus

- [ ] **Numérotation séquentielle activée** : SureCart, Settings, Orders & Receipts, passer de Aléatoire à Séquentiel, ajouter un préfixe et définir le numéro de départ. _(Leçon 4.1)_
- [ ] **Filtres de statut vérifiés** : tu sais distinguer Payée, En traitement, Échouée, Annulée dans la liste des commandes. _(Leçon 4.1)_
- [ ] **Reçu téléchargé au moins une fois** : depuis le détail d'une commande, section du paiement, Download Receipt ou Invoice. _(Leçon 4.1)_

> Règle d'or : une numérotation continue et ordonnée est ce que ton comptable et l'administration attendent. Ne laisse pas le réglage en mode Aléatoire.

---

## 2. Facturation (si tu fais de la prestation)

- [ ] **Accès Invoices confirmé** : SureCart, Orders, Invoices - présent et accessible selon ton plan. _(Leçon 4.2)_
- [ ] **Mentions obligatoires dans le Footer** : les mentions légales FR placées dans le champ Footer avant toute publication. Valide leur contenu avec ton comptable - SureCart ne garantit pas la conformité par défaut. _(Leçon 4.2)_
- [ ] **Date d'émission et date d'échéance renseignées** sur chaque facture. _(Leçon 4.2)_
- [ ] **Lien de paiement testé** : la facture publiée s'ouvre, affiche le récapitulatif et permet de payer en ligne. _(Leçon 4.2)_

> Piège : tant que tu n'as pas cliqué sur Create Invoice, la facture reste un brouillon. C'est ce clic qui la publie, et l'email au client comme le numéro de facture ne sont générés qu'à ce moment-là.

---

## 3. Remboursements

- [ ] **Chemin mémorisé** : Orders, commande, section Charge, menu à trois points, Refund. _(Leçon 4.3)_
- [ ] **Revoke Purchase coché si accès à retirer** : pour un cours en ligne, un fichier ou un abonnement, tu coches Revoke Purchase en même temps que tu rembourses - sinon le client est remboursé et garde l'accès. _(Leçon 4.3)_
- [ ] **Délai communiqué au client** : informer le client que le remboursement prend 5 à 10 jours à apparaître sur son relevé. _(Leçon 4.3)_

> Point à retenir : les frais prélevés par le processeur de paiement ne te sont en général pas rendus lors d'un remboursement. C'est le coût réel de la transaction initiale.

---

## 4. Coupons et codes promo

- [ ] **Nom interne distinct du code promo** : le nom est pour toi, le code est saisi par le client au checkout. _(Leçon 4.4)_
- [ ] **Type de réduction choisi** : pourcentage (offre globale) ou montant fixe (réduction précise). _(Leçon 4.4)_
- [ ] **Limites d'usage définies** : total d'utilisations, maximum par client, montant minimum de commande, date de fin. _(Leçon 4.4)_
- [ ] **Date de fin en UTC vérifiée** : tenir compte du décalage horaire entre UTC et l'heure française avant de fixer l'expiration. _(Leçon 4.4)_
- [ ] **Exercice du module complété** : coupon -20 % créé (nom : Lancement, code : LANCEMENT20, limite et date de fin configurées). _(Leçon 4.4)_

---

## 5. Taxes et TVA

> Important : cette section décrit comment configurer l'outil SureCart. Elle ne constitue pas un conseil fiscal. Tes obligations dépendent de ton statut, de tes activités et de ton pays. Consulte ton comptable avant d'activer ou de modifier les réglages de taxes.

- [ ] **Décision prise avec ton comptable** : dois-tu collecter de la TVA ? Si oui, à quel taux et pour quelles régions ? _(Leçon 4.5)_
- [ ] **Tax Collection activé si applicable** : SureCart, Settings, Taxes. Taux de repli (fallback) et adresse d'entreprise renseignés. _(Leçon 4.5)_
- [ ] **Région configurée** : Union européenne (ou autre région pertinente), mode de calcul automatique (TaxJar + numéro d'enregistrement) ou manuel (pourcentage fixe). _(Leçon 4.5)_
- [ ] **Taxe activée produit par produit** : sur chaque produit concerné, onglet Taxes, Charge tax on this product. _(Leçon 4.5)_
- [ ] **Collecte du numéro de TVA configurée si B2B** : champ VAT or Tax ID Input ajouté au formulaire ; options Require VAT Number et Local Reverse Charge réglées selon les recommandations de ton comptable. _(Leçon 4.5)_

---

## 6. Passage du mode test au mode live

- [ ] **Test Mode Restricted activé pendant les tests** : Settings, Advanced, Spam Protection & Security - réserve les commandes de test aux administrateurs. _(Leçon 4.6)_
- [ ] **Paiement test de bout en bout réussi** : modal Thank you, reçu reçu, commande visible dans les commandes. _(Leçon 4.6)_
- [ ] **Données de test nettoyées** : Settings, Advanced, Clear Test Data, taper CONFIRM. Action irréversible - vérifie bien que tu n'effaces que des données de test, jamais de vraies commandes. _(Leçon 4.6)_
- [ ] **Mode test désactivé partout** : sur chaque produit (Instant Checkout), sur chaque formulaire (Custom Forms). Un produit ou formulaire encore en test ne peut pas encaisser de vrai paiement. _(Leçon 4.6)_

---

## Checklist finale avant ouverture publique

Passe ces 8 points avant de partager ton premier lien public. Si tout est coché, tu peux ouvrir.

- [ ] Processeur de paiement connecté en mode live (pastille verte dans Settings, Payment Processors)
- [ ] Devise correcte (ne pas changer une fois des ventes enregistrées)
- [ ] Conditions générales de vente en place sur le checkout
- [ ] Taxes configurées si tu y es soumis - après échange avec ton comptable
- [ ] Numérotation des commandes en Séquentiel
- [ ] Paiement test de bout en bout réussi
- [ ] Données de test nettoyées (Clear Test Data)
- [ ] Mode test désactivé sur tous les produits et formulaires

---

## Mémo technique

### Actions sur une commande : Cancel Order vs Revoke

| Action       | Où                                              | Effet                                                                   |
| ------------ | ----------------------------------------------- | ----------------------------------------------------------------------- |
| Cancel Order | Bouton Actions, en haut à droite de la commande | Coupe l'accès à tous les produits, téléchargements et abonnements liés  |
| Revoke       | Section des achats, sur un article précis       | Retire l'accès à ce produit spécifique, ses abonnements et ses fichiers |

### Facture payable : ce qui se déclenche à la publication

Dès que tu cliques sur Create Invoice :

1. Un email part vers le client.
2. La facture reçoit son numéro officiel.
3. Les adresses de facturation sont récupérées.
4. Un lien partageable est généré.
5. Le client peut payer directement en ligne via ce lien.

### Régions de taxe prédéfinies dans SureCart

- Union européenne (France incluse)
- Australie
- Canada
- Royaume-Uni
- États-Unis
- Reste du monde

Pour chaque région : calcul automatique via TaxJar (avec numéro d'enregistrement) ou calcul manuel (pourcentage que tu fixes toi-même).

### Coupons : comportement des restrictions produits

Si tu restreins un coupon à certains produits, il suffit qu'un de ces produits soit dans le panier pour que la réduction s'applique - même si le panier contient d'autres produits non concernés.

> Règle d'or : pour tout ce qui touche à la TVA et à la facturation, l'outil SureCart montre comment configurer les réglages. Ce que tu dois collecter et déclarer, c'est ton comptable qui te le dit, pas moi.
