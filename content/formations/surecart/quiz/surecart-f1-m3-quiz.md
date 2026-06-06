# Quiz - Module 3 : La page de paiement qui convertit

Quiz de validation de fin de module (5 questions). Source à recopier dans TutorLMS.

## Réglages TutorLMS recommandés

- **Placement** : fin de Module 3, avec verrouillage de la progression (l'élève doit réussir le quiz pour débloquer le Module 4).
- **Note de passage** : 80 % (4 bonnes réponses sur 5).
- **Tentatives** : illimitées (ou 3), pour que l'élève réessaie sans blocage.
- **Affichage des réponses** : révéler la bonne réponse et l'explication après chaque tentative.
- **Points** : 1 point par question.

La bonne réponse est marquée `[x]`. Le champ "Answer Explanation" de TutorLMS reprend la ligne **Explication**.

---

## Question 1

**Type** : Choix unique (Single Choice)

Dans l'éditeur de blocs d'un formulaire SureCart, tu actives la vue en liste. Quels blocs trouves-tu en général dans un formulaire Simple par défaut ?

- [ ] L'avatar vendeur, le titre du produit, le bouton d'achat et le chat en direct
- [x] Le paiement express, le champ email, les lignes de produits, le bouton de validation et le champ coupon
- [ ] Le formulaire de contact, le champ téléphone, la liste de souhaits et le bouton d'abonnement
- [ ] La galerie d'images, le sélecteur de couleurs, le champ adresse et le récapitulatif fiscal

**Explication** : Un formulaire SureCart Simple contient par défaut : le paiement express (Apple Pay, Google Pay), le champ email, les lignes de produits, le bouton de validation et le champ coupon. La vue en liste (icône en haut de l'éditeur) les affiche tous et permet de les réordonner par glisser-déposer.

---

## Question 2

**Type** : Vrai / Faux (True/False)

Dans SureCart, un client peut finaliser son achat sans qu'aucun compte ne soit créé (achat en mode invité pur, sans enregistrement de l'email).

- [ ] Vrai
- [x] Faux

**Explication** : SureCart ne propose pas d'achat invité au sens strict. À chaque achat, un compte est automatiquement créé à partir de l'email du client. Ce choix permet de maintenir un espace client, un suivi des commandes et des actions de fidélisation. La vraie question n'est donc pas "compte ou pas compte" mais "à quel moment le client crée son accès" : au checkout (champ mot de passe) ou après (email post-achat).

---

## Question 3

**Type** : Choix unique (Single Choice)

Tu veux ajouter une case d'acceptation des conditions générales de vente à ton formulaire. Quelle combinaison d'actions est correcte ?

- [ ] Ajouter un champ Text Field, le renommer "CGV", activer l'option Published
- [ ] Ajouter un bloc Checkbox, l'insérer n'importe où dans le formulaire, laisser l'option Required désactivée pour ne pas bloquer l'achat
- [x] Ajouter un bloc Checkbox juste avant le bouton, activer l'option Required, éditer le texte et le lier à la page CGV
- [ ] Ajouter un bloc Radio Select Box avec deux options (J'accepte / Je refuse) et rendre le champ obligatoire

**Explication** : Le bon bloc est Checkbox (pas Radio, pas Text Field). Il faut l'activer en Required pour que la validation soit bloquée sans la case. On place la case juste avant le bouton, on rédige le texte (ex. : "J'accepte les conditions générales de vente") et on le lie à la page CGV. Le texte et la valeur de la case sont ensuite enregistrés avec la commande, ce qui trace l'accord.

---

## Question 4

**Type** : Choix unique (Single Choice)

Tu veux partager un lien de paiement pour un produit unique depuis un email, sans construire de page complète. Quelle est la marche à suivre dans SureCart ?

- [ ] Aller dans Forms, Add New, choisir le design Simple, ajouter le produit, publier la page et copier son URL
- [ ] Aller dans Settings, Payment Processors, activer le mode "Vente directe" et copier le lien généré
- [x] Ouvrir le produit dans SureCart, Products, cliquer sur Instant Checkout, activer Published, configurer les options souhaitées, enregistrer avec Save Product, puis copier le lien
- [ ] Installer une extension tierce de "buy now link" et la connecter à SureCart via l'API

**Explication** : L'Instant Checkout est disponible directement dans la fiche produit. Il suffit d'activer Published, de choisir ce qui s'affiche sur la page (image, description, coupon, CGV), d'enregistrer, puis de copier le lien. Ce lien mène directement au paiement sans passer par une page de ton site. Pour 90 % des cas simples, le bouton Copy Links à côté du prix suffit également.

---

## Question 5

**Type** : Choix multiple (Multiple Choice)

Dans un formulaire SureCart, le bloc conditionnel te permet d'afficher du contenu selon certaines conditions. Lesquelles sont disponibles nativement ? (plusieurs bonnes réponses)

- [x] Le pays de livraison du client
- [x] Les produits sélectionnés dans le panier
- [ ] La langue du navigateur du client
- [x] Le montant total de la commande
- [x] Le coupon appliqué par le client
- [ ] L'heure et le jour de l'achat

**Explication** : Le bloc conditionnel évalue en temps réel : les produits sélectionnés, le pays de livraison, le montant de la commande, le coupon appliqué et le moyen de paiement. La langue du navigateur et l'heure d'achat ne font pas partie des conditions disponibles. Exemple d'usage concret : afficher un champ de numéro TVA uniquement pour certains pays, ou afficher un message de précommande pour un produit précis.
