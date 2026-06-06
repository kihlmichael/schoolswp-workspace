# Quiz - Module 2 : Créer tes offres (produits et prix)

Quiz de validation de fin de module (5 questions). Source à recopier dans TutorLMS.

## Réglages TutorLMS recommandés

- **Placement** : fin de Module 2, avec verrouillage de la progression (l'élève doit réussir le quiz pour débloquer le Module 3).
- **Note de passage** : 80 % (4 bonnes réponses sur 5).
- **Tentatives** : illimitées (ou 3), pour que l'élève réessaie sans blocage.
- **Affichage des réponses** : révéler la bonne réponse et l'explication après chaque tentative.
- **Points** : 1 point par question.

La bonne réponse est marquée `[x]`. Le champ "Answer Explanation" de TutorLMS reprend la ligne **Explication**.

---

## Question 1

**Type** : Choix unique (Single Choice)

Dans SureCart, quelle est la différence entre la **nature d'un produit** et son **type de paiement** ?

- [ ] C'est la même chose : le type de paiement définit ce que tu vends
- [x] La nature désigne ce que tu vends (service, numérique, téléchargement...), le type de paiement désigne comment c'est facturé (unique, échelonné, abonnement) : ce sont deux questions distinctes
- [ ] La nature du produit est choisie dans la section Pricing, le type de paiement dans la fiche produit
- [ ] Seul le type de paiement est configurable dans SureCart : la nature est détectée automatiquement

**Explication** : Ce sont deux questions séparées. La nature du produit (numérique, téléchargement, service, licence...) décrit ce que tu vends. Le type de paiement (unique, échelonné, abonnement) décrit comment le client paie. Un même produit peut porter plusieurs prix avec des types de paiement différents - par exemple unique et échelonné côte à côte.

---

## Question 2

**Type** : Choix unique (Single Choice)

Tu viens de créer un produit et tu veux ajouter un prix en paiement unique. Dans quel ordre effectues-tu les étapes ?

- [ ] Fiche produit, puis Settings, puis Add a Price, puis choisir One Time, puis Save Product
- [ ] Products, Add New, nommer, Create, puis dans la section Pricing cliquer Add a Price, choisir One Time, saisir le montant, Create Price, puis Save Product
- [x] Products, Add New, nommer le produit, Create - puis section Pricing, Add a Price, choisir le type One Time, saisir le montant, Create Price - puis Save Product en haut
- [ ] Add New, section Pricing, Add a Price, nommer le produit, Create Price, Save Product

**Explication** : L'ordre compte. Tu crées d'abord le produit (Add New, nom, Create), tu arrives sur la page d'édition, tu descends jusqu'à la section Pricing, tu cliques Add a Price, tu choisis One Time, tu saisis le montant, tu cliques Create Price. Tu termines toujours par Save Product en haut - sinon rien n'est enregistré. Une fois le prix créé, le bouton Copy Links te donne le lien d'achat direct.

---

## Question 3

**Type** : Choix unique (Single Choice)

Pour attacher un fichier téléchargeable à un produit, SureCart propose deux options. Laquelle choisir pour protéger un ebook payant ?

- [ ] External Link : c'est le plus fiable car le fichier est hébergé chez un tiers
- [ ] Les deux options offrent la même protection : peu importe le choix
- [x] Secure Storage : le fichier est hébergé chez SureCart et l'accès est contrôlé - recommandé pour tout fichier que tu veux protéger
- [ ] Il faut toujours les deux en même temps, sinon la livraison ne se fait pas

**Explication** : Secure Storage héberge ton fichier dans ton compte SureCart et en contrôle l'accès - si tu révoques un accès client, le fichier n'est plus accessible. External Link pointe vers un fichier hébergé ailleurs (Google Drive, Dropbox, toute URL) : pratique si le fichier est déjà hébergé proprement, mais le contrôle d'accès dépend de ta configuration externe. Pour un ebook payant, Secure Storage est la voie recommandée. Les deux options sont combinables et tu peux attacher plusieurs fichiers sur un même produit.

---

## Question 4

**Type** : Vrai / Faux (True/False)

Quand un produit SureCart est à prix zéro, les champs de carte bancaire s'affichent quand même pour rassurer le visiteur.

- [ ] Vrai
- [x] Faux

**Explication** : C'est tout l'intérêt du produit gratuit dans SureCart : quand le prix est à zéro, SureCart masque automatiquement tous les champs de paiement (carte, PayPal, Apple Pay). Le formulaire de paiement se transforme en un simple formulaire d'inscription où la personne donne son nom et son email. C'est ainsi qu'un produit à 0 € devient un outil de capture de lead - un lead magnet sans friction.

---

## Question 5

**Type** : Choix multiple (Multiple Choice)

Sur la fiche produit SureCart, quelles affirmations sur la **description** et le **contenu** sont correctes ? (plusieurs bonnes réponses)

- [x] La description est un texte court avec mise en forme basique (gras, italique, listes) - elle est stockée chez SureCart et suit le produit partout
- [ ] Le contenu (Content Designer) est stocké chez SureCart comme la description
- [x] Le contenu, ou long description, s'ouvre via le bouton Open Content Designer et utilise les blocs WordPress - il est stocké dans ta base WordPress
- [x] Si le contenu ne s'affiche pas sur la fiche, il faut vérifier que le template est réglé sur Theme Layout et non SureCart Layout
- [ ] La description et le contenu sont interchangeables : l'un ou l'autre suffit, peu importe lequel tu utilises

**Explication** : Description et contenu sont deux zones distinctes avec des usages différents. La description (courte, basique) voyage avec le produit et s'affiche partout. Le contenu (long description, blocs WordPress, Content Designer) permet une mise en page riche pour une vraie page de vente - mais il est stocké dans WordPress. Le piège classique : le contenu existe mais ne s'affiche pas parce que le template est resté sur SureCart Layout au lieu de Theme Layout.
