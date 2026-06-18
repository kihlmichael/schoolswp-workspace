---
title: SureCart - Gabarit Structurer une offre (Module 2)
version: 1.0
last_updated: 2026-06-05
---

# Gabarit : Structurer une offre SureCart

Garde cette fiche à côté de toi pendant le Module 2. Utilise-la pour cadrer chaque offre avant de la créer dans SureCart : remplis une fiche par produit. En bas, la checklist de création te guide étape par étape.

---

## Gabarit "Structurer une offre" (à remplir par produit)

| Champ                                                       | Ta réponse |
| ----------------------------------------------------------- | ---------- |
| **Nom du produit**                                          |            |
| **Nature** (numérique, téléchargement, service, gratuit...) |            |
| **Type de paiement** (unique, échelonné, abonnement)        |            |
| **Prix** (ou 0 si gratuit)                                  |            |
| **Ce que le client reçoit concrètement**                    |            |
| **À qui ça s'adresse**                                      |            |
| **Ce qui se passe après l'achat** (livraison, accès, délai) |            |
| **Fichier ou accès à attacher** (oui / non - lequel ?)      |            |
| **Intégration éventuelle** (tag CRM, liste, accès...)       |            |

> Règle d'or : si tu ne peux pas remplir "Ce que le client reçoit concrètement" en une phrase précise, ta description n'est pas encore prête. Remplis cette case avant d'ouvrir SureCart.

---

## Checklist de création : produit payant (paiement unique)

- [ ] **Nom et description clairs** : nom du produit saisi, description qui dit ce qui est inclus, la durée ou le format, et ce que le client repart avec. _(Leçon 2.2)_
- [ ] **Au moins une image** : une fiche sans visuel inspire moins confiance. _(Leçon 2.2)_
- [ ] **Prix créé** : section Pricing, Add a Price, type One Time, montant saisi, Create Price. _(Leçon 2.2)_
- [ ] **Options de prix décidées** : compare price (prix barré) activé ou non, Pay What You Want activé ou non, taxe incluse cochée ou non selon ta situation fiscale. _(Leçon 2.2)_
- [ ] **Produit sauvegardé** : bouton Save Product cliqué en haut. _(Leçon 2.2)_
- [ ] **Lien de vente copié** : bouton Copy Links à côté du prix - le lien d'achat direct est prêt à être collé dans un email ou un bouton. _(Leçon 2.2)_

## Checklist complémentaire : service (prestation, coaching, forfait)

- [ ] **Sections expédition et stock ignorées** : un service n'a rien à expédier ni à stocker. _(Leçon 2.3)_
- [ ] **Purchase Limits réglée si besoin** : limite d'achat à 1 pour une offre découverte réservée aux nouveaux clients. _(Leçon 2.3)_
- [ ] **Expire Access activé si besoin** : nombre de jours saisi si l'accès doit s'arrêter automatiquement (ex : accompagnement 30 jours). _(Leçon 2.3)_

## Checklist complémentaire : produit numérique ou téléchargement

- [ ] **Fichier attaché** : section Downloads, Add Downloads, choix entre Secure Storage (hébergé chez SureCart, accès protégé) ou External Link (Google Drive, Dropbox, toute URL). _(Leçon 2.4)_
- [ ] **Livraison vérifiée** : après un achat test, le fichier est bien accessible dans l'espace client et le lien est reçu par email. _(Leçon 2.4)_
- [ ] **Contrôle d'accès connu** : si un remboursement intervient, SureCart, Customers, fiche client, Revoke permet de retirer l'accès. Unrevoke restaure. _(Leçon 2.4)_

## Checklist : produit gratuit (capture de lead / lead magnet)

- [ ] **Prix à zéro** : aucun champ de paiement ne s'affiche - SureCart transforme le formulaire en formulaire d'inscription. _(Leçon 2.5)_
- [ ] **Fichier PDF attaché si besoin** : le lead magnet (ex : guide, fiche) est attaché dans la section Downloads. _(Leçon 2.5)_
- [ ] **Formulaire créé et nettoyé** : Forms, Add New, produit gratuit ajouté, paiement express et totaux retirés, bouton renommé (Rejoindre / Je télécharge / Accéder maintenant), cadenas masqué. _(Leçon 2.5)_
- [ ] **Champ Nom ajouté et obligatoire** : pour personnaliser les messages ensuite. _(Leçon 2.5)_
- [ ] **Formulaire publié sur une page** : bloc Checkout Form inséré sur une page dédiée, page de remerciement personnalisée activée. _(Leçon 2.5)_
- [ ] **Test en navigation privée réussi** : inscription complète, accès reçu, contact visible là où il doit remonter. _(Leçon 2.5)_

## Checklist : soigner la fiche produit

- [ ] **Description vs Contenu distincts** : description courte pour le résumé qui voyage avec le produit, contenu (Content Designer) pour la mise en page riche. _(Leçon 2.6)_
- [ ] **Template réglé sur Theme Layout** (pas SureCart Layout) si le contenu ne s'affiche pas. _(Leçon 2.6)_
- [ ] **Images soignées** : galerie ou diaporama, au moins une image nette et bien cadrée. _(Leçon 2.6)_
- [ ] **Permalien lisible** : adresse courte et personnalisée depuis les réglages de permaliens WordPress. _(Leçon 2.6)_

---

## Mémo technique

### Les 3 types de paiement SureCart

| Type                   | Description                            | Cas d'usage                                |
| ---------------------- | -------------------------------------- | ------------------------------------------ |
| **Paiement unique**    | Le client paie en une fois             | Service, ebook, accès ponctuel - ce module |
| **Paiement échelonné** | Plusieurs mensualités (ex : 6 x 100 €) | Offre au prix élevé                        |
| **Abonnement**         | Paiement régulier, mensuel ou annuel   | Revenus récurrents - Module 5              |

Un même produit peut avoir plusieurs prix (ex : unique + échelonné côte à côte). Tu n'as pas besoin de dupliquer le produit.

### Secure Storage vs External Link

**Secure Storage** : ton fichier est hébergé chez SureCart, l'accès est contrôlé. Recommandé pour un ebook payant ou tout fichier que tu veux protéger.

**External Link** : tu pointes vers un fichier hébergé ailleurs (Google Drive, Dropbox, toute URL). Pratique si le fichier est déjà hébergé proprement chez toi.

Les deux sont combinables. Tu peux attacher autant de fichiers que tu veux sur un même produit.

### Revoke / Unrevoke : contrôle d'accès après l'achat

```
SureCart > Customers > clic sur le client
> section Purchases > Revoke (retirer l'accès)
> Unrevoke (restaurer l'accès si tu t'es trompé)
```

### Bouton Copy Links : les 4 éléments

À côté de chaque prix créé :

1. **Lien d'achat direct** : le plus simple pour démarrer - à coller dans un email ou un bouton.
2. **Shortcode bouton Ajouter au panier**
3. **Shortcode bouton Acheter**
4. **Identifiant du prix** : pour les usages techniques

### Périmètre de ce module et de ce parcours

- **Abonnement** (type de paiement récurrent) : Module 5.
- **Numérique avancé** (paywall, espace membre, licences logicielles) : parcours Créateurs.
- **Physique avancé** : parcours Boutique.
- **Branchement CRM du produit gratuit** (tags, séquence de bienvenue) : Module 7.

> Pour toute question sur la TVA ou ta situation fiscale, consulte un comptable. Les réglages de taxe dans SureCart (taxe incluse, taux) ne remplacent pas un conseil fiscal.
