---
title: SureCart - Fiche de la page de paiement (Module 3)
version: 1.0
last_updated: 2026-06-05
---

# Fiche : La page de paiement qui convertit

Garde cette fiche à côté de toi pendant le Module 3. Elle couvre les 9 leçons : de la création d'un formulaire jusqu'au panier coulissant. Coche chaque ligne quand elle est faite.

---

## Créer et personnaliser un formulaire de paiement

### Créer un formulaire _(Leçons 3.1 et 3.2)_

- [ ] Aller dans SureCart, Forms, Add New. Donner un titre clair (pour toi seul, invisible pour l'acheteur). _(Leçon 3.1)_
- [ ] Choisir un design de départ : Simple (sans sélecteur de prix), Default (avec sélecteur de prix), Sections (deux colonnes dès le départ). _(Leçon 3.1)_
- [ ] Cliquer sur Add Product et sélectionner le ou les produits. Si plusieurs produits : choisir le mode (tout acheter / choisir un / en cocher plusieurs). _(Leçon 3.1)_
- [ ] Après création, ouvrir la vue en liste pour repérer tous les blocs : paiement express, email, lignes de produits, bouton, coupon. _(Leçon 3.1)_
- [ ] Option Persist Across Pages : activer dans les réglages du panier si tu veux conserver le panier entre les pages. _(Leçon 3.1)_
- [ ] Modifier un bloc : Forms, Edit, clic sur le bloc, réglages à droite, Update pour enregistrer. _(Leçon 3.2)_
- [ ] Soigner le bouton : changer le texte (ex. : "Régler ma commande"), activer l'affichage du montant total dans le bouton. _(Leçon 3.2)_
- [ ] Réordonner les blocs via glisser-déposer dans la vue en liste (ordre logique : produits, nom, email, bouton). _(Leçon 3.2)_
- [ ] Passer en deux colonnes : cliquer sur le bloc parent, option Two Column, puis faire glisser les éléments entre colonnes. _(Leçon 3.2)_

### Ajouter des champs personnalisés _(Leçon 3.3)_

- [ ] Champ texte libre : dans le formulaire, clic sur le plus, Text Field. Renseigner le label (question affichée), le name (clé stockée dans la commande), le placeholder. Activer le champ requis si nécessaire.
- [ ] Champ à options : Radio Select Box. Label, valeur par option (texte affiché et valeur stockée séparément), option par défaut possible.
- [ ] Vérifier que les données remontent bien dans SureCart, Orders, métadonnées de la commande. Tester en mode test avant ouverture au public.

### Ajouter les conditions générales _(Leçon 3.4)_

- [ ] Insérer un bloc Checkbox juste avant le bouton de validation.
- [ ] Activer l'option Required : pas de validation possible sans la case cochée.
- [ ] Éditer le texte (ex. : "J'accepte les conditions générales de vente") et le lier à la page CGV via l'icône de lien ou Ctrl + K.
- [ ] Le texte et la valeur de la case sont enregistrés avec la commande : tu gardes une trace de l'accord.

> Règle clé : en France, il est préférable de laisser la case décochée par défaut. Un accord explicite (le client coche lui-même) est plus solide qu'une case pré-cochée. Pour toute question sur la valeur juridique de ce consentement, consulte un comptable ou un conseiller juridique.

---

## Gérer le compte client et les options de vente rapide

### Flux de connexion au checkout _(Leçon 3.5)_

- [ ] Comprendre que SureCart ne propose pas d'achat invité : un compte est créé automatiquement à partir de l'email du client.
- [ ] **Approche 1 - compte au checkout** : ajouter le champ Set Password (renommé "Créer un mot de passe"), le rendre obligatoire, le placer dans l'ordre nom - email - mot de passe - carte - bouton. Activer la création auto dans Settings, Customer Accounts, et choisir le rôle Abonné.
- [ ] **Approche 2 - compte après l'achat** : retirer le champ mot de passe. Sur app.surecart.com, vérifier que l'email post-achat est activé et qu'il contient bien le lien de création de compte.
- [ ] Arbitrage : l'approche 1 donne un accès immédiat (idéal pour un cours), l'approche 2 offre un checkout plus léger. Choisir selon ton offre.

### Instant Checkout et liens d'achat directs _(Leçon 3.6)_

- [ ] Ouvrir un produit dans SureCart, Products, et cliquer sur le bouton Instant Checkout.
- [ ] Activer Published pour rendre la page accessible. Activer Test Mode pour tester, puis le désactiver avant le live.
- [ ] Choisir les infos affichées sur la page (image du produit, description, coupon, conditions générales).
- [ ] Enregistrer avec Save Product, puis copier le lien ou cliquer sur View.
- [ ] Pour un lien d'achat simple : utiliser le bouton Copy Links à côté du prix (voie suffisante dans la plupart des cas).
- [ ] Option avancée : construire un lien avec le Price ID pour pré-remplir le panier (quantité, plusieurs produits). Consulter la doc SureCart pour la syntaxe exacte.

---

## Construire une page qui convertit et soigner l'après-achat

### Page produit unique qui convertit _(Leçon 3.7)_

- [ ] Partir du layout deux colonnes : inverser les colonnes pour mettre le formulaire à droite.
- [ ] Déplacer le récapitulatif de commande (totaux) juste au-dessus du bouton de validation.
- [ ] Élargir la colonne de gauche et y ajouter : sélecteur de prix, image du produit, description courte, avis client, garantie.
- [ ] Styliser avec la palette du thème. Le client lit d'abord pourquoi acheter, puis paie à droite.

### Dupliquer un formulaire _(Leçon 3.7)_

- [ ] Ouvrir le formulaire à copier, cliquer sur les trois points en haut à droite, puis sur Éditeur de code.
- [ ] Sélectionner tout le code et le copier.
- [ ] Créer un nouveau formulaire (Add New), ouvrir son éditeur de code, coller, sortir de l'éditeur. Le formulaire est dupliqué.
- [ ] Cette méthode fonctionne aussi pour copier un formulaire vers un autre site.

### Page de remerciement personnalisée _(Leçon 3.7)_

- [ ] Créer une nouvelle page WordPress avec les blocs SureCart. Ajouter le bloc Order Confirmation. Publier.
- [ ] Dans SureCart, Custom Forms, sélectionner le formulaire, cliquer sur l'en-tête du formulaire.
- [ ] Activer l'option Thank You Page et choisir la page créée. Cliquer sur Update.

---

## Fonctions avancées du checkout

### Le bloc conditionnel _(Leçon 3.8)_

- [ ] Ajouter un bloc conditionnel (Conditional) dans le formulaire via le plus.
- [ ] Définir la condition : produit, pays de livraison, montant, coupon appliqué, ou moyen de paiement. Cliquer sur Set Rules.
- [ ] Insérer les blocs à afficher à l'intérieur du bloc conditionnel.
- [ ] **Cas TVA par pays** : condition Shipping Country, pays sélectionnés, puis champ Tax ID à l'intérieur. Le champ n'apparaît que pour ces pays.
- [ ] **Cas message lié à un produit** : condition Product, produit sélectionné, puis un bloc paragraphe à l'intérieur.
- [ ] Plusieurs blocs conditionnels peuvent coexister, évalués en temps réel pendant le paiement.

### Le panier coulissant _(Leçon 3.9)_

- [ ] Activer dans SureCart, Settings, Design & Branding, section Cart. Choisir le type d'icône (flottante, dans le menu, ou les deux) et la position (droite recommandée).
- [ ] Choisir si le panier affiche l'image et la description des produits, et s'il apparaît même quand vide.
- [ ] Ajouter l'icône au menu : thème classique via Apparence, Menus, entrée SureCart ; thème FSE via l'éditeur, bloc panier dans la navigation (bloc Cart Toggle Icon). Utiliser le shortcode en repli si le bloc ne fonctionne pas.
- [ ] Personnaliser les textes (bouton de validation, message de panier vide) dans les réglages.

> Panier ou lien direct ? Le panier est utile quand tu as plusieurs produits que le client parcourt et combine. Pour une ou deux offres bien identifiées, le formulaire dédié ou l'Instant Checkout reste souvent plus direct et plus efficace.

---

## Mémo technique

### Les 3 designs de départ

| Design   | Caractéristique principale                                        |
| -------- | ----------------------------------------------------------------- |
| Simple   | Pas de sélecteur de prix par défaut - le plus clair pour démarrer |
| Default  | Inclut un sélecteur de prix                                       |
| Sections | Formulaire et récapitulatif en deux colonnes dès le départ        |

### Dupliquer via l'éditeur de code (méthode rapide)

```
Formulaire source :
1. Trois points en haut à droite > Éditeur de code
2. Sélectionner tout (Ctrl+A) > Copier (Ctrl+C)

Nouveau formulaire :
3. SureCart, Forms, Add New > nommer > Create
4. Trois points > Éditeur de code > Coller (Ctrl+V)
5. Sortir de l'éditeur de code > Update
```

### Bloc conditionnel : conditions disponibles

- Produits sélectionnés dans le panier
- Pays de livraison
- Montant de la commande
- Coupon appliqué
- Moyen de paiement

### Flux de connexion : critères de choix

| Critère              | Approche 1 (mot de passe au checkout) | Approche 2 (email post-achat) |
| -------------------- | ------------------------------------- | ----------------------------- |
| Accès au produit     | Immédiat                              | Après confirmation email      |
| Longueur du checkout | Un champ de plus                      | Plus léger                    |
| Idéal pour           | Cours, accès immédiat attendu         | Offres sans accès direct      |
