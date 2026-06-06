# Scripts vidéo - F1 Module 3 : La page de paiement qui convertit

**Formation** : Vendre sans WooCommerce (SureCart) - méthode CAISSE (parcours F1)
**Module** : M3 - La page de paiement qui convertit (payant)
**Leçons** : 9 vidéos + 1 quiz + 1 template de page de paiement réutilisable
**Durée totale** : ~40 min
**Type** : Vidéo HeyGen + voix ElevenLabs
**Date** : 2026-06-04
**Sources** : `_sources/docs-kb/` (add-checkout-form, edit-checkout-form, adding-terms-conditions-in-checkout, guest-checkout, instant-checkout-pages, creating-custom-buy-links, custom-thank-you-page, conditional-block, slide-out-cart, cart-toggle-icon) + `_sources/youtube-transcripts/` (02 créer formulaire, 04 champs personnalisés, 05 flux de connexion, 10 dupliquer, 11 page produit unique, 17 panier)

> Rôle de ce module : le plus dense de la formation. C'est ici qu'on construit la pièce maîtresse, la page de paiement. À la fin, l'élève a publié au moins une page de paiement soignée et fonctionnelle. Très orienté manipulation : screencast guidé en continu. On reste dans le périmètre F1 : un formulaire propre qui convertit, sans plonger dans le développement.

---

### Leçon 3.1 : Créer un formulaire de paiement

**Durée** : ~5 min (~750 mots)
**Objectif pédagogique** : Créer un formulaire de paiement, choisir un design de départ, y ajouter un ou plusieurs produits, et comprendre les blocs qui le composent.
**Écran** : Screencast Forms, Add New, choix du design, ajout produit, vue en liste.

---

**[INTRO - face caméra]**

On arrive au coeur du sujet : la page où ton client sort sa carte. C'est la pièce qui décide si une visite devient une vente. SureCart appelle ça un formulaire de paiement, un checkout. Dans cette leçon, on en crée un de zéro, et je te montre de quoi il est fait.

**[SECTION 1 - Créer le formulaire]**

**[ÉCRAN - screencast : SureCart, Forms, Add New]**

Dans WordPress, va dans SureCart, Forms, formulaires, puis Add New. On te demande un titre. Retiens bien : ce titre, c'est pour toi seul. Tes acheteurs ne le verront jamais. Nomme-le clairement, par exemple Checkout coaching, pour t'y retrouver quand tu en auras plusieurs.

**[ÉCRAN - screencast : choix du design de départ]**

SureCart te propose ensuite des designs de départ. Ce sont juste des assemblages de blocs prêts à l'emploi. Le design Default inclut un sélecteur de prix. Le Simple ne l'a pas, mais tu peux l'ajouter quand tu veux. Le design en sections présente le formulaire et le récapitulatif de commande sur deux colonnes. Choisis le Simple pour démarrer, c'est le plus clair, puis clique sur Next.

**[SECTION 2 - Ajouter ton produit]**

**[ÉCRAN - screencast : Add Product]**

On choisit maintenant ce que ce formulaire va vendre. Clique sur Add Product et sélectionne ton produit, par exemple celui que tu as créé au module 2.

**[ÉCRAN - slide "Plusieurs produits sur un formulaire"]**

Si tu ajoutes plusieurs produits, tu décides comment le client les voit. Première option : le client doit tout acheter, les produits sont groupés. Deuxième : il doit en choisir un seul, c'est un choix par boutons radio. Troisième : il peut en cocher plusieurs. Pour une offre simple, un seul produit suffit. Clique sur Create.

**[SECTION 3 - Comprendre les blocs du formulaire]**

**[ÉCRAN - screencast : éditeur de blocs, icône vue en liste]**

Ton formulaire s'ouvre dans l'éditeur de blocs WordPress, celui que tu connais. Mon conseil pour ne pas être perdu : clique sur l'icône de vue en liste, en haut. Tu déplies alors tous les composants du formulaire.

Tu vois en général : le paiement express, le champ email, les lignes de produits, le bouton de validation, et un champ pour les coupons. Chacun de ces blocs est modifiable, tu cliques dessus et ses réglages apparaissent à droite. On personnalise tout ça dans la prochaine leçon.

**[ÉCRAN - zoom : Persist Across Pages]**

Une option utile à connaître : la persistance du panier. Dans les réglages du panier du formulaire, tu peux activer Persist Across Pages. Le contenu du panier reste alors présent même si le client navigue ailleurs ou revient plus tard. Pratique pour ne pas perdre une vente en cours.

**[OUTRO - face caméra]**

Ton formulaire existe et tu sais de quoi il est fait. Maintenant, on le rend efficace : on personnalise les blocs, on réordonne, et on passe en deux colonnes pour une page qui inspire confiance. C'est la prochaine leçon.

---

**Points clés** :

- Forms, Add New, titre (pour toi seul, invisible pour l'acheteur), choisir un design (Default avec sélecteur de prix, Simple sans, Sections en deux colonnes), Next.
- Add Product : un ou plusieurs produits. Si plusieurs : tout acheter / en choisir un (radio) / en cocher plusieurs.
- Le formulaire s'ouvre dans l'éditeur de blocs. La vue en liste affiche tous les composants (paiement express, email, lignes produits, bouton, coupon).
- Option Persist Across Pages : garde le panier en mémoire entre les pages.

**Mots clés SEO** : formulaire de paiement SureCart, checkout SureCart, créer checkout WordPress, page de paiement SureCart, checkout form SureCart

---

### Leçon 3.2 : Éditer et personnaliser les blocs du formulaire

**Durée** : ~5 min (~750 mots)
**Objectif pédagogique** : Modifier les blocs, réordonner les champs, personnaliser le bouton, et passer en mise en page deux colonnes.
**Écran** : Screencast édition de blocs, bouton, layout deux colonnes, drag and drop.

---

**[INTRO - face caméra]**

Un formulaire par défaut, ça marche. Mais un formulaire pensé, ça convertit mieux. Dans cette leçon, je te montre comment ajuster chaque bloc, remettre les choses dans le bon ordre, et passer en deux colonnes pour un rendu plus pro. Tout est en glisser-déposer, tu n'écris pas une ligne de code.

**[SECTION 1 - Modifier un bloc]**

**[ÉCRAN - screencast : Forms, Edit, clic sur un bloc]**

Pour éditer un formulaire existant, va dans Forms et clique sur Edit sous le formulaire concerné. Clique ensuite sur le bloc que tu veux modifier : ses réglages s'ouvrent à droite. Tu fais tes changements, et tu enregistres avec le bouton Update. Simple et direct.

**[SECTION 2 - Soigner le bouton de validation]**

**[ÉCRAN - screencast : bloc bouton, options à droite]**

Le bouton mérite une attention particulière, c'est le dernier geste avant l'achat. Clique dessus. Tu peux changer son texte, par exemple Régler ma commande plutôt qu'un simple Acheter. Et active l'option qui affiche le montant total à payer dans le texte du bouton. Le client voit alors exactement la somme qu'il va payer au moment de cliquer. C'est rassurant, et ça lève un frein.

**[SECTION 3 - Ajouter et réordonner les champs]**

**[ÉCRAN - screencast : bouton plus, ajout du champ Nom, déplacement]**

Pour ajouter un composant, clique sur le plus. Tu as une liste de blocs propres à SureCart. Ajoute par exemple le champ Nom. Ensuite, réordonne. Dans la vue en liste, attrape un bloc et déplace-le. Un bon ordre logique : les lignes de produits en haut, puis le nom, l'email, et le bouton en bas. Le client suit alors un parcours naturel, du produit au paiement.

**[SECTION 4 - Passer en deux colonnes]**

**[ÉCRAN - screencast : sélection du bloc formulaire parent, option Two Column]**

Voici ce qui change vraiment l'allure. Dans la vue en liste, clique sur le bloc parent du formulaire, le conteneur. À droite, choisis l'option Two Column, deux colonnes, puis l'endroit où couper. Ton formulaire passe en deux colonnes d'un coup.

**[ÉCRAN - screencast : drag and drop entre colonnes]**

Et tu gardes la main sur tout. En cliquant dans chaque colonne, tu vois ses éléments, et tu peux les faire glisser d'une colonne à l'autre. Tu veux le coupon dans la colonne de droite ? Tu le glisses, tu valides, c'est fait. Une fois content, clique sur Update et va voir le rendu côté visiteur.

**[OUTRO - face caméra]**

Ton formulaire est propre, ordonné, et bien présenté. Mais parfois, tu as besoin de poser une question à ton client au moment de l'achat. Pour ça, il y a les champs personnalisés. C'est la prochaine leçon.

---

**Points clés** :

- Forms, Edit, clic sur un bloc, réglages à droite, Update pour enregistrer.
- Bouton : changer le texte, activer l'affichage du montant total dans le bouton (rassure le client).
- Ajouter des blocs via le plus, réordonner en glisser-déposer (produits en haut, puis nom, email, bouton).
- Deux colonnes : sélectionner le bloc parent, option Two Column, glisser les éléments entre colonnes. Tout en visuel, sans code.

**Mots clés SEO** : personnaliser checkout SureCart, éditer formulaire SureCart, checkout deux colonnes SureCart, bouton paiement SureCart, blocs checkout SureCart

---

### Leçon 3.3 : Ajouter des champs personnalisés

**Durée** : ~4 min (~650 mots)
**Objectif pédagogique** : Collecter une information précise au checkout via un champ texte ou un choix radio, et retrouver la donnée dans la commande.
**Écran** : Screencast ajout champ texte et radio, réglages label/valeur/requis, donnée dans la commande.

---

**[INTRO - face caméra]**

Parfois, tu veux poser une question à ton client au moment de l'achat. Son entreprise, un besoin précis, une préférence. SureCart te laisse ajouter tes propres champs au formulaire, sans coder, et tu retrouves la réponse dans la commande. Je te montre.

**[SECTION 1 - Ajouter un champ texte]**

**[ÉCRAN - screencast : formulaire, plus, Text Field]**

Dans ton formulaire, clique sur un champ existant puis sur le plus pour ouvrir la liste. Cherche Text Field, champ texte, et clique dessus : il s'ajoute. À droite, tu configures trois choses. Le label, la question affichée, par exemple Quel est ton site web ? Le name, le nom interne sous lequel la réponse sera stockée dans la commande, par exemple site-web. Et un texte d'exemple, le placeholder, pour guider la saisie. Tu peux rendre le champ obligatoire avec un simple bouton.

**[SECTION 2 - Ajouter un choix à options : le bloc radio]**

**[ÉCRAN - screencast : Radio Select Box, ajout d'options]**

Quand tu veux contrôler les réponses possibles, utilise le bloc radio, le choix à boutons. Ajoute-le, donne-lui un label, par exemple Qu'est-ce qui te décrit le mieux ? Rends-le obligatoire si tu veux forcer un choix.

**[ÉCRAN - zoom : label vs value d'une option]**

Pour chaque option, deux éléments. Le texte affiché au client. Et la valeur, ce qui sera réellement enregistré dans la commande. Par exemple, l'option affichée Créateur de contenu peut enregistrer la valeur createur. Tu cliques sur le plus pour ajouter d'autres options, et tu peux en pré-sélectionner une par défaut.

**[SECTION 3 - Retrouver la donnée dans la commande]**

**[ÉCRAN - screencast : SureCart, Orders, métadonnées de la commande]**

À quoi bon collecter si tu ne retrouves pas l'info ? Après une vente, va dans SureCart, Orders, commandes, et ouvre une commande. Dans la section des métadonnées, tu vois exactement les réponses : ton champ site-web avec l'adresse saisie, ton champ radio avec la valeur choisie. La donnée est là, propre, attachée à la commande.

Comme toujours, teste en mode test avant d'ouvrir au public, pour vérifier que tes champs se comportent comme prévu.

**[OUTRO - face caméra]**

Tu sais maintenant poser les bonnes questions au bon moment. Il y a un champ particulier que beaucoup oublient, et qui est important, surtout en France : l'acceptation des conditions générales. On le voit tout de suite.

---

**Points clés** :

- Ajouter un champ : dans le formulaire, plus, Text Field (champ libre) ou Radio Select Box (choix à options).
- Champ texte : label (question), name (clé stockée dans la commande), placeholder, requis.
- Radio : chaque option a un texte affiché et une valeur stockée ; option par défaut possible.
- Les réponses se retrouvent dans SureCart, Orders, métadonnées de la commande. Tester en mode test.

**Mots clés SEO** : champs personnalisés SureCart, custom fields checkout SureCart, collecter information checkout, champ formulaire SureCart, métadonnées commande SureCart

---

### Leçon 3.4 : Ajouter les conditions générales au checkout

**Durée** : ~3 min (~500 mots)
**Objectif pédagogique** : Ajouter une case d'acceptation des conditions générales, obligatoire, liée à la page CGV, et comprendre que l'accord est enregistré avec la commande.
**Écran** : Screencast ajout case à cocher, lien vers page CGV, option requis.

---

**[INTRO - face caméra]**

En France, faire accepter tes conditions générales de vente au moment du paiement, ce n'est pas un détail, c'est une bonne pratique. SureCart te permet d'ajouter une case à cocher obligatoire, liée à ta page CGV, en deux minutes. Je te montre.

**[SECTION 1 - Ajouter la case à cocher]**

**[ÉCRAN - screencast : formulaire, insérer un bloc Checkbox]**

Ouvre ton formulaire de paiement. À l'endroit où tu veux la case, en général juste avant le bouton, insère un bloc Checkbox, case à cocher. Sélectionne-le, et dans les réglages à droite, active l'option Required, obligatoire. À partir de là, le client ne pourra pas valider sa commande sans cocher la case.

**[SECTION 2 - Rédiger et lier le texte]**

**[ÉCRAN - screencast : édition du label, icône lien]**

Double-clique sur le texte de la case pour le modifier. Écris quelque chose comme J'accepte les conditions générales de vente. Ensuite, sélectionne le texte, clique sur l'icône de lien, ou fais Contrôle plus K, et colle l'adresse de ta page de conditions générales. Le client peut ainsi la consulter avant d'accepter.

**[SECTION 3 - L'accord est tracé]**

**[ÉCRAN - slide "L'accord est enregistré avec la commande"]**

Point important : le texte de la case et sa valeur sont sauvegardés avec la commande. Tu gardes donc une trace de l'accord du client, ce qui est exactement ce que tu veux pour tes CGV. Tu peux aussi pré-cocher la case par défaut, mais en France, mieux vaut souvent laisser le client cocher lui-même, c'est un accord plus explicite.

**[OUTRO - face caméra]**

Ta page de paiement est maintenant carrée sur le plan des conditions. Passons à une question que tout le monde se pose : faut-il forcer la création de compte, ou laisser acheter en invité ? La réponse de SureCart est intéressante. Prochaine leçon.

---

**Points clés** :

- Insérer un bloc Checkbox avant le bouton, activer Required : pas de validation sans la case cochée.
- Éditer le texte (J'accepte les conditions générales de vente), le lier à la page CGV via l'icône de lien ou Contrôle plus K.
- Le texte et la valeur de la case sont enregistrés avec la commande : trace de l'accord.
- Pré-cocher est possible, mais un accord explicite (case décochée) est souvent préférable.

**Mots clés SEO** : conditions générales checkout SureCart, CGV SureCart, case à cocher checkout, acceptation CGV WordPress, terms and conditions SureCart

---

### Leçon 3.5 : Login, compte client ou achat invité

**Durée** : ~5 min (~750 mots)
**Objectif pédagogique** : Comprendre que SureCart crée toujours un compte à l'achat, et choisir entre deux flux : créer le compte au paiement ou après.
**Écran** : Screencast champ Set Password, réglages Customer Accounts, email post-achat.

---

**[INTRO - face caméra]**

Question classique : dois-tu obliger ton client à créer un compte, ou le laisser acheter en invité ? La réponse de SureCart va surprendre certains. On va clarifier ça, puis je te montre les deux façons de gérer l'accès après l'achat.

**[SECTION 1 - Le vrai fonctionnement : pas d'achat invité]**

**[ÉCRAN - slide "SureCart crée toujours un compte"]**

Soyons clairs tout de suite. SureCart ne propose pas de véritable achat invité. À chaque achat, un compte est automatiquement créé à partir de l'email du client. Pourquoi ce choix ? Parce qu'un compte, c'est un espace client où l'acheteur retrouve ses commandes et ses factures, et c'est pour toi la base pour le suivi, la relance et la fidélisation. L'achat invité semble pratique, mais il te coupe de presque tout : pas de relance, pas de newsletter, pas de suivi. SureCart fait donc le choix du compte.

La question n'est donc pas compte ou pas compte, mais : à quel moment le client crée son accès ?

**[SECTION 2 - Approche 1 : le compte se crée au paiement]**

**[ÉCRAN - screencast : ajout du champ Set Password, label "Créer un mot de passe"]**

Première approche : le client crée son compte pendant l'achat. Dans ton formulaire, ajoute le champ Set Password, définir un mot de passe. Renomme-le en Créer un mot de passe, rends-le obligatoire, et place-le dans l'ordre nom, email, mot de passe, carte, bouton.

**[ÉCRAN - screencast : Settings, Customer Accounts, rôle WordPress]**

Pour que ça fonctionne, va dans SureCart, Settings, Customer Accounts, comptes clients. Active la création automatique de comptes, et choisis le rôle WordPress attribué à l'acheteur. Le rôle Abonné, le plus bas niveau, convient parfaitement ici. À l'achat, le client devient utilisateur WordPress et accède immédiatement à ce qu'il a acheté. Si ton produit donne accès à un cours, par exemple via une intégration LearnDash ou TutorLMS, l'accès est ouvert dans la foulée.

**[SECTION 3 - Approche 2 : le compte se crée après l'achat]**

**[ÉCRAN - screencast : retrait du champ mot de passe, email post-achat]**

Deuxième approche : pas de mot de passe au checkout. Tu retires ce champ du formulaire. Le client achète, et reçoit ensuite un email de SureCart l'invitant à créer son compte et à accéder à son produit. Pour que ça marche, va sur la plateforme app point surecart point com et vérifie que l'email de nouvel achat est activé et qu'il contient bien le lien de création de compte.

**[ÉCRAN - slide "Quelle approche choisir"]**

Le choix t'appartient. L'approche 1 donne un accès immédiat, mais ajoute un champ au checkout, ce qui peut faire baisser un peu la conversion. L'approche 2 offre un checkout plus léger, mais introduit un petit délai avant l'accès. Pour un produit où l'accès immédiat compte, comme un cours, l'approche 1 est souvent préférable. À toi de juger selon ton offre.

**[OUTRO - face caméra]**

Tu maîtrises maintenant le parcours de connexion. On va voir une façon encore plus rapide de vendre un seul produit, sans même passer par une page classique : l'Instant Checkout et les liens d'achat directs. Prochaine leçon.

---

**Points clés** :

- SureCart n'a pas d'achat invité : un compte est créé automatiquement à partir de l'email, par choix (espace client, suivi, relance).
- Approche 1 : champ Créer un mot de passe au checkout + Settings, Customer Accounts, création auto + rôle Abonné. Accès immédiat (idéal avec une intégration cours).
- Approche 2 : pas de mot de passe ; le client crée son compte via l'email post-achat (vérifier que l'email est activé avec le lien).
- Arbitrage : accès immédiat (approche 1) vs checkout plus léger (approche 2).

**Mots clés SEO** : achat invité SureCart, compte client SureCart, login SureCart, créer compte au checkout, rôle WordPress SureCart

---

### Leçon 3.6 : Instant Checkout et liens d'achat directs

**Durée** : ~5 min (~750 mots)
**Objectif pédagogique** : Activer une page Instant Checkout pour un produit unique, et comprendre les liens d'achat directs pré-remplis.
**Écran** : Screencast Instant Checkout (toggle Published, options), Copy Links, exemple de lien.

---

**[INTRO - face caméra]**

Tu veux vendre un seul produit, vite, depuis un email ou un réseau social, sans construire de page ? SureCart a ce qu'il te faut : l'Instant Checkout. Une page de paiement dédiée à un produit, accessible par un simple lien. Je te montre comment l'activer, puis comment aller plus loin avec les liens d'achat directs.

**[SECTION 1 - Activer l'Instant Checkout]**

**[ÉCRAN - screencast : Products, produit, bouton Instant Checkout]**

Va dans SureCart, Products, et ouvre un produit. À droite, repère le bouton Instant Checkout et clique dessus. Un menu déroulant s'ouvre.

Active d'abord Published, publié, pour rendre la page accessible. Juste en dessous, tu as Test Mode : active-le si tu veux faire un achat de test avant l'ouverture, puis désactive-le pour le live. Ensuite, tu choisis ce qui s'affiche sur la page : l'image du produit, la description, le champ coupon, les conditions générales. Tu actives ce qui sert ta vente.

**[ÉCRAN - screencast : Save Product, Copy link, View]**

Clique sur Save Product pour appliquer, puis copie le lien, ou clique sur View pour le voir dans un nouvel onglet. Tu as maintenant un lien que tu peux coller dans un email, un message, une bio de réseau social. Le client clique et arrive direct sur le paiement, sans parcourir ton site. Moins d'étapes, souvent plus de ventes.

**[SECTION 2 - Les liens d'achat directs]**

**[ÉCRAN - screencast : Copy Links sur le prix]**

Rappel du module 2 : à côté de chaque prix, le bouton Copy Links te donne un lien d'achat direct prêt à l'emploi. C'est la voie la plus simple, et pour 90 % des cas, elle suffit.

**[ÉCRAN - slide "Aller plus loin : pré-remplir le panier"]**

Pour aller plus loin, tu peux construire tes propres liens qui pré-remplissent le panier. Le principe : tu pars de l'adresse de ta page de paiement, et tu ajoutes un paramètre qui désigne le prix à charger, grâce à son identifiant, le Price ID que tu copies dans Copy Links. Tu peux même préciser une quantité, ou empiler plusieurs produits dans le même lien. Le client arrive alors sur un checkout déjà rempli. La syntaxe exacte est dans la doc SureCart ; pour ce parcours, retiens surtout que c'est possible, et que le lien direct de Copy Links couvre déjà l'essentiel.

**[OUTRO - face caméra]**

Tu as plusieurs façons de vendre un produit en un lien. Maintenant, on monte en gamme côté présentation : une vraie page produit unique qui convertit, comment dupliquer un formulaire réussi, et soigner la page de remerciement. Prochaine leçon.

---

**Points clés** :

- Instant Checkout : Products, produit, bouton Instant Checkout, activer Published, option Test Mode, choisir les infos affichées (image, description, coupon, CGV), Save Product, copier le lien.
- Page dédiée à un produit, partageable par email ou réseaux, qui mène droit au paiement.
- Liens d'achat directs : Copy Links donne un lien prêt (voie simple, suffisante en général).
- Avancé : construire un lien avec le Price ID pour pré-remplir le panier (quantité, plusieurs produits). Syntaxe dans la doc SureCart.

**Mots clés SEO** : instant checkout SureCart, lien d'achat direct SureCart, page produit unique SureCart, buy link SureCart, vendre en un lien WordPress

---

### Leçon 3.7 : Page produit unique, dupliquer un formulaire, page de remerciement

**Durée** : ~5 min (~800 mots)
**Objectif pédagogique** : Construire une page de paiement produit unique qui convertit, réutiliser un formulaire en le dupliquant, et créer une page de remerciement personnalisée.
**Écran** : Screencast layout deux colonnes orienté vente, duplication via éditeur de code, assignation page de remerciement.

---

**[INTRO - face caméra]**

Dans cette leçon, trois techniques qui font la différence entre un checkout fonctionnel et un checkout qui vend. Une vraie page produit unique pensée pour convertir, la duplication d'un formulaire réussi, et la page de remerciement, ce moment qu'on néglige trop souvent.

**[SECTION 1 - Une page produit unique qui convertit]**

**[ÉCRAN - screencast : formulaire, vue en liste, swap columns]**

On part du layout deux colonnes vu en leçon 3.2, et on l'oriente vente. Dans le formulaire, sélectionne le bloc parent et inverse les colonnes : le formulaire passe à droite, et la colonne de gauche accueille les informations qui rassurent.

**[ÉCRAN - screencast : déplacer les totaux, élargir la colonne gauche]**

Déplace le récapitulatif de commande, le bloc des totaux, juste au-dessus du bouton de validation : le client voit ce qu'il paie au bon moment. Élargis la colonne de gauche pour lui donner de la place.

**[ÉCRAN - screencast : ajout sélecteur de prix, image, garantie]**

Dans cette colonne de gauche, ajoute le sélecteur de prix, pour que le client choisisse son option avant de payer, puis une image du produit, une description courte, et des éléments de confiance : un avis client, une garantie. Le client lit d'abord pourquoi acheter, puis il paie à droite. Tu styles le tout avec la palette de ton thème. Ce parcours convertit nettement mieux qu'un formulaire brut sur une colonne, et tu le montes en quelques minutes.

**[SECTION 2 - Dupliquer un formulaire réussi]**

**[ÉCRAN - screencast : trois points, Code Editor, sélectionner, copier]**

Tu as construit un formulaire parfait et tu veux le réutiliser ? SureCart n'a pas de bouton dupliquer, mais WordPress, si. Ouvre ton formulaire, clique sur les trois points en haut à droite, puis sur l'éditeur de code. Sélectionne tout le code et copie-le.

**[ÉCRAN - screencast : Add New, coller dans l'éditeur de code]**

Crée ensuite un nouveau formulaire avec Add New, nomme-le, ouvre son éditeur de code par les trois points, et colle. Sors de l'éditeur de code, et ton formulaire est dupliqué à l'identique. Tu peux même t'en servir pour copier un formulaire vers un autre site. Pratique pour décliner une base qui marche.

**[SECTION 3 - La page de remerciement]**

**[ÉCRAN - screencast : Pages, Add New, bloc Order Confirmation]**

Par défaut, après l'achat, SureCart affiche une petite fenêtre de confirmation. Tu peux faire bien mieux. Crée une page dédiée : Pages, Add New, construis-la avec les blocs SureCart, et ajoute le bloc Order Confirmation pour afficher le détail de la commande. Publie.

**[ÉCRAN - screencast : Custom Forms, en-tête du formulaire, Thank You Page]**

Pour l'assigner, va dans SureCart, Custom Forms, sélectionne ton formulaire, clique sur l'en-tête du formulaire pour ouvrir ses réglages, active l'option Thank You Page et choisis ta page. Update. Désormais, tes clients arrivent sur ta page personnalisée plutôt que sur la fenêtre par défaut. C'est le premier moment après l'achat : remercie, rassure, et indique la prochaine étape.

**[OUTRO - face caméra]**

Tu as une page qui vend, un formulaire réutilisable, et un après-achat soigné. Il reste une fonction puissante pour des checkouts intelligents : afficher des champs ou des messages selon des conditions. C'est le bloc conditionnel, dans la prochaine leçon.

---

**Points clés** :

- Page produit unique : inverser les colonnes (formulaire à droite), totaux au-dessus du bouton, colonne gauche élargie avec sélecteur de prix, image, description, avis, garantie. Style à la palette du thème.
- Dupliquer un formulaire : trois points, Éditeur de code, copier tout le code ; nouveau formulaire, coller dans son éditeur de code. Marche aussi entre sites.
- Page de remerciement : créer une page avec le bloc Order Confirmation, puis Custom Forms, en-tête du formulaire, activer Thank You Page, choisir la page, Update.

**Mots clés SEO** : page produit unique SureCart, dupliquer formulaire SureCart, page de remerciement SureCart, thank you page SureCart, checkout qui convertit

---

### Leçon 3.8 : La puissance du bloc conditionnel

**Durée** : ~4 min (~650 mots)
**Objectif pédagogique** : Utiliser le bloc conditionnel pour afficher un champ ou un message selon des règles (pays, produit, montant, coupon, paiement).
**Écran** : Screencast bloc conditionnel, conditions, cas TVA par pays et message produit.

---

**[INTRO - face caméra]**

Voici une fonction qui rend ton checkout intelligent. Le bloc conditionnel affiche ou masque du contenu selon des règles que tu définis. Un champ qui n'apparaît que pour certains pays, un message lié à un produit précis. Je te montre deux cas concrets.

**[SECTION 1 - Ce qu'il sait faire]**

**[ÉCRAN - slide "Conditions disponibles"]**

Le bloc conditionnel montre les blocs qu'il contient seulement quand tes règles sont remplies. Les conditions peuvent reposer sur les produits sélectionnés, le pays de livraison, le montant de la commande, un coupon appliqué, ou le moyen de paiement. C'est ce qui te permet d'adapter le checkout au contexte du client.

**[SECTION 2 - Cas 1 : un champ TVA selon le pays]**

**[ÉCRAN - screencast : ajout bloc conditionnel, condition Shipping Country]**

Imaginons que tu veuilles afficher un champ numéro de TVA seulement pour certains pays. Dans ton formulaire, clique sur le plus, cherche Conditional et ajoute le bloc conditionnel. Sélectionne-le, clique sur Add Conditions, et dans le menu, choisis Shipping Country, pays de livraison. Sélectionne les pays concernés, puis clique sur Set Rules.

**[ÉCRAN - screencast : ajout du champ Tax ID dans le bloc]**

Ensuite, clique sur le plus à l'intérieur du bloc conditionnel, cherche Tax et insère le champ Tax ID ou TVA. Ajuste le label si besoin. Update. Le champ TVA n'apparaîtra que pour les clients des pays que tu as choisis. Propre et automatique.

**[SECTION 3 - Cas 2 : un message lié à un produit]**

**[ÉCRAN - screencast : condition Product, bloc paragraphe]**

Autre cas : afficher un message pour un produit précis, par exemple un délai de livraison ou une précommande. Ajoute un bloc conditionnel, donne-lui une condition basée sur le produit, sélectionne le produit déclencheur, Set Rules. À l'intérieur, insère un bloc paragraphe et écris ton message. Update. Quand ce produit est dans le panier, le message s'affiche au checkout.

Tu peux empiler plusieurs blocs conditionnels, chacun avec ses règles. Les conditions sont évaluées en temps réel pendant le paiement.

**[OUTRO - face caméra]**

Ton checkout sait maintenant s'adapter au client. Pour finir ce module, on parle du panier : le panier coulissant, et comment ajouter l'icône à ton menu pour vendre plusieurs produits à la fois. Dernière leçon du module.

---

**Points clés** :

- Le bloc conditionnel affiche ou masque son contenu selon des règles : produits, pays de livraison, montant, coupon, moyen de paiement.
- Cas TVA : bloc conditionnel, Add Conditions, Shipping Country, pays, Set Rules, puis insérer le champ Tax ID dedans.
- Cas message produit : condition sur le produit, Set Rules, insérer un paragraphe dans le bloc.
- Plusieurs blocs conditionnels possibles, évalués en temps réel.

**Mots clés SEO** : bloc conditionnel SureCart, conditional block SureCart, champ TVA checkout, checkout conditionnel SureCart, afficher champ selon pays

---

### Leçon 3.9 : Le panier, ajout au panier et panier coulissant

**Durée** : ~4 min (~650 mots)
**Objectif pédagogique** : Activer le panier coulissant, ajouter l'icône au menu (thème classique ou FSE), et savoir quand le panier est pertinent.
**Écran** : Screencast réglages panier, ajout de l'icône menu, panier coulissant en action.

---

**[INTRO - face caméra]**

Jusqu'ici, on a vendu produit par produit. Mais si tu as plusieurs produits que les gens parcourent et combinent, tu as besoin d'un panier. SureCart propose un panier coulissant, celui qui glisse sur le côté quand on ajoute un article. Je te montre comment l'activer et l'ajouter à ton menu.

**[SECTION 1 - Activer le panier coulissant]**

**[ÉCRAN - screencast : Settings, Design & Branding, section Cart]**

Sur un thème classique, va dans SureCart, Settings, Design & Branding, et descends jusqu'à la section Cart, panier. Active le panier. Tu choisis ensuite comment l'icône s'affiche : une icône flottante seule, une icône dans le menu seule, ou les deux. Tu décides aussi si le panier s'ouvre à droite ou à gauche. À droite, c'est ce que les gens attendent. Tu peux afficher l'image et la description des produits dans le panier, et choisir d'afficher l'icône même quand le panier est vide. Enregistre.

Côté style, le panier reprend la couleur de marque que tu as définie au module 1, par exemple pour le bouton de validation. Ton panier est donc déjà à tes couleurs.

**[SECTION 2 - Ajouter l'icône à ton menu]**

**[ÉCRAN - screencast : thème classique, Apparence, Menus]**

La façon d'ajouter l'icône dépend de ton thème. Sur un thème classique, va dans Apparence, Menus. Dans les éléments à ajouter, repère l'entrée SureCart et ajoute le panier au menu, puis enregistre. L'icône apparaît dans ta navigation.

**[ÉCRAN - screencast : thème FSE, éditeur, bloc Cart]**

Sur un thème en édition complète du site, un thème FSE, va dans l'éditeur de site, ouvre ta navigation, clique sur le plus et cherche le bloc panier de SureCart, parfois nommé Cart Toggle Icon. Ajoute-le. Tu peux régler son apparence et choisir s'il s'affiche toujours ou seulement quand le panier contient des articles. Si le bloc ne fonctionne pas sur ton thème, SureCart fournit aussi un shortcode en solution de repli.

**[SECTION 3 - Quand le panier est vraiment utile]**

**[ÉCRAN - slide "Panier ou lien direct ?"]**

Un mot de cadrage honnête. Le panier brille quand tu as plusieurs produits que le client parcourt et combine, comme une vraie boutique. Si tu vends une ou deux offres bien identifiées, le formulaire dédié ou l'Instant Checkout des leçons précédentes suffit souvent, et reste plus direct. Choisis selon ton catalogue, pas par réflexe. Et pense à personnaliser les textes du panier, comme le bouton de validation ou le message de panier vide, dans les réglages.

**[OUTRO - face caméra]**

Tu as maintenant tout pour une page de paiement qui convertit : un formulaire propre, des champs utiles, les conditions générales, le bon flux de connexion, l'Instant Checkout, une page produit soignée, le bloc conditionnel et le panier. Récupère le template de page de paiement que je t'ai préparé. Dans le module 4, on s'occupe d'encaisser proprement : commandes, factures, coupons et taxes. On se retrouve là-bas.

---

**Points clés** :

- Panier coulissant : Settings, Design & Branding, section Cart, activer. Choisir le type d'icône (flottante, menu, les deux), la position, l'affichage des infos produit. Reprend la couleur de marque.
- Ajouter l'icône : thème classique via Apparence, Menus (entrée SureCart) ; thème FSE via l'éditeur, bloc panier dans la navigation (shortcode en repli).
- Le panier est utile pour plusieurs produits parcourus ensemble. Pour une ou deux offres, le formulaire dédié ou l'Instant Checkout reste plus direct.
- Personnaliser les textes du panier dans les réglages.

**Mots clés SEO** : panier SureCart, panier coulissant SureCart, ajouter panier au menu WordPress, slide-out cart SureCart, icône panier FSE SureCart

---

## Notes de production (module)

### Captures et écrans à préparer

- Screencast Forms, Add New, choix de design, ajout produit, vue en liste (3.1)
- Slide "plusieurs produits sur un formulaire" + zoom Persist Across Pages (3.1)
- Screencast édition de blocs, options du bouton, drag and drop, passage deux colonnes (3.2)
- Screencast ajout Text Field et Radio, réglages label/name/valeur, métadonnées dans Orders (3.3)
- Screencast insertion Checkbox, lien vers page CGV, option Required (3.4)
- Slide "SureCart crée toujours un compte" + screencast Set Password + Settings Customer Accounts + email post-achat (3.5)
- Screencast Instant Checkout (toggle Published, options) + Copy Links + slide pré-remplissage du panier (3.6)
- Screencast layout vente (swap columns, totaux, sélecteur de prix, garantie) + duplication via éditeur de code + assignation Thank You Page (3.7)
- Screencast bloc conditionnel : condition pays + champ TVA, condition produit + message (3.8)
- Screencast réglages panier + ajout icône menu (classique et FSE) + panier coulissant en action (3.9)

### Ton et transitions

- Intro/outro face caméra, fond neutre schoolsWP.
- Module très pratique : screencast guidé quasi permanent, slides Kadence pour les concepts (conditions, arbitrages).
- Leçon 3.4 (CGV) : adaptation France assumée, parler de conditions générales de vente et d'accord explicite.
- Leçon 3.5 (login) : bien clarifier qu'il n'y a pas d'achat invité, puis présenter les deux flux sans imposer.
- Leçon 3.9 : finir le module en rappelant que le panier n'est pas obligatoire selon le catalogue.

### Livrables du module

- Template de page de paiement réutilisable (layout deux colonnes orienté vente : formulaire à droite, sélecteur de prix, image, avis, garantie et totaux à gauche). Fourni en formulaire à dupliquer via l'éditeur de code (méthode 3.7).
- Quiz 5 questions (composants d'un formulaire, champ requis CGV, absence d'achat invité, activation Instant Checkout, rôle du bloc conditionnel).

### Garde-fous voix schoolsWP

- Tutoiement, singulier solo, jamais d'em-dash ni d'en-dash.
- Aucune promesse absolue ("convertit mieux" oui, "garantit des ventes" non).
- Honnêteté sur les arbitrages : champ mot de passe vs conversion (3.5), panier vs lien direct (3.9).
- Les liens d'achat avancés (paramètres d'URL) sont présentés comme option, sans transformer la leçon en cours technique : renvoi à la doc pour la syntaxe exacte.

### Cohérence avec le plan et les modules précédents

- Reprend les produits et prix créés au M2 (le formulaire vend ces produits, le sélecteur de prix affiche leurs prix).
- Le champ mot de passe et la création de compte (3.5) préparent l'espace client et les intégrations détaillés au module 7.
- Les coupons apparaissent ici comme champ du formulaire ; leur création est traitée au module 4.
- Les taxes via le bloc conditionnel (3.8) sont effleurées ; la configuration des taxes est au module 4.
- L'abonnement n'est pas abordé dans le checkout ici : il a son module dédié (M5).
