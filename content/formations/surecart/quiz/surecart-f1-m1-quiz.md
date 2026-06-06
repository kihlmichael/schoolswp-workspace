# Quiz - Module 1 : Installer et connecter SureCart

Quiz de validation de fin de module (5 questions). Source à recopier dans TutorLMS.

## Réglages TutorLMS recommandés

- **Placement** : fin de Module 1, avec verrouillage de la progression (l'élève doit réussir le quiz pour débloquer le Module 2).
- **Note de passage** : 80 % (4 bonnes réponses sur 5).
- **Tentatives** : illimitées (ou 3), pour que l'élève réessaie sans blocage.
- **Affichage des réponses** : révéler la bonne réponse et l'explication après chaque tentative.
- **Points** : 1 point par question.

La bonne réponse est marquée `[x]`. Le champ "Answer Explanation" de TutorLMS reprend la ligne **Explication**.

---

## Question 1

**Type** : Choix unique (Single Choice)

Juste après l'assistant de configuration, un bandeau vert affiche un bouton **Complete Setup**. Pourquoi est-il essentiel de cliquer dessus tout de suite ?

- [ ] Pour activer le mode test de la boutique
- [x] Pour rattacher la boutique à ton compte SureCart : une boutique non rattachée est considérée comme abandonnée et peut être supprimée
- [ ] Pour connecter Stripe automatiquement
- [ ] Pour traduire l'interface en français

**Explication** : Complete Setup revendique ta boutique et la relie officiellement à ton compte. Tant que ce n'est pas fait, elle peut être supprimée. Valider l'email débloque ensuite toutes les fonctions de ton compte.

---

## Question 2

**Type** : Choix unique (Single Choice)

Où récupères-tu le jeton API (Secret Token) qui relie ton plugin à la plateforme SureCart ?

- [ ] Dans WordPress, SureCart, Settings, Connection
- [x] Sur app.surecart.com, menu API, onglet Secret Token
- [ ] Dans ton tableau de bord Stripe
- [ ] Dans le fichier wp-config.php

**Explication** : Le jeton se génère et se copie sur app.surecart.com (menu API, onglet Secret Token, il commence par st\_). Tu le colles ensuite côté WordPress dans Settings, Connection. Traite-le comme un mot de passe : ne le partage jamais en clair.

---

## Question 3

**Type** : Choix unique (Single Choice)

Au moment d'ajouter ton domaine dans Stripe pour activer Apple Pay, quelle règle respecter pour qu'Apple Pay s'affiche bien ?

- [ ] Entrer le domaine en minuscules sans son extension
- [x] Entrer le domaine exactement comme il apparaît dans la barre d'adresse de tes visiteurs (avec le www s'il est utilisé)
- [ ] Entrer l'adresse IP du serveur
- [ ] Peu importe la forme, Stripe corrige automatiquement

**Explication** : Tu dois saisir le domaine exact (avec ou sans www, selon ce que voient tes visiteurs), puis le valider via le fichier déposé dans le dossier .well-known. Un domaine mal saisi et Apple Pay ne s'affiche pas. Rappel : le test se fait uniquement sous Safari, avec une vraie carte, dans un pays compatible.

---

## Question 4

**Type** : Vrai / Faux (True/False)

Tu as déjà des commandes et des abonnements actifs sur ta boutique en live. Changer la devise maintenant est sans risque.

- [ ] Vrai
- [x] Faux

**Explication** : Sur une boutique en live, changer de devise ne convertit pas les prix (tu dois tous les ressaisir, et entre-temps tes produits peuvent devenir non achetables), fait disparaître tes anciens rapports et peut faire échouer le renouvellement des abonnements actifs. On choisit donc bien sa devise sur une boutique neuve ou de test, pendant que c'est sans conséquence.

---

## Question 5

**Type** : Choix multiple (Multiple Choice)

Pour éviter que le cache casse ton tunnel de paiement, quelles règles appliques-tu ? (plusieurs bonnes réponses)

- [x] Exclure du cache les pages connexion, inscription, paiement et espace client
- [x] Exclure les requêtes de l'API REST
- [ ] Activer la combinaison des scripts JavaScript pour accélérer le checkout
- [x] Désactiver la combinaison des scripts JavaScript
- [x] Tester le tunnel en navigation privée après chaque réglage

**Explication** : Le cache mal réglé est la cause numéro un des bugs de boutique. On exclut les pages dynamiques et l'API REST, on ne diffère pas les scripts de base, on désactive la combinaison JavaScript, et on teste toujours en navigation privée. Activer la combinaison JS (réponse barrée) n'apporte rien aujourd'hui et peut justement casser le paiement.
