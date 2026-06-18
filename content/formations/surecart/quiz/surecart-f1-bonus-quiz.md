# Quiz - Bonus : Cas pratiques et dépannage SureCart

Quiz de validation du module Bonus (5 questions). Source à recopier dans TutorLMS.

## Réglages TutorLMS recommandés

- **Placement** : fin du module Bonus, après la leçon B.5.
- **Note de passage** : 80 % (4 bonnes réponses sur 5).
- **Tentatives** : illimitées (ou 3), pour que l'élève réessaie sans blocage.
- **Affichage des réponses** : révéler la bonne réponse et l'explication après chaque tentative.
- **Points** : 1 point par question.

La bonne réponse est marquée `[x]`. Le champ "Answer Explanation" de TutorLMS reprend la ligne **Explication**.

---

## Question 1

**Type** : Choix unique (Single Choice)

Tu vends un accompagnement à 300 euros. Tu veux récupérer l'URL du site du client dès la commande. Quelle fonction SureCart utilises-tu pour ça ?

- [ ] Un champ dans l'email de confirmation
- [ ] Un produit à zéro euro en lead magnet
- [x] Un champ personnalisé ajouté au formulaire ou à l'Instant Checkout
- [ ] Une note dans la description du produit

**Explication** : Le champ personnalisé (vu au module 3) s'ajoute directement sur la page de paiement. Il est enregistré dans les données de la commande, pas seulement dans un email. C'est la seule façon de le retrouver proprement côté admin.

---

## Question 2

**Type** : Choix unique (Single Choice)

Pour un ebook à 19 euros vendu sur les réseaux sociaux, quelle option de page de paiement est la plus adaptée ?

- [ ] Un formulaire deux colonnes avec témoignages
- [x] L'Instant Checkout, qui génère un lien direct partageable
- [ ] Une facture payable
- [ ] Une page de remerciement personnalisée

**Explication** : L'Instant Checkout (module 3) génère un lien direct que tu copies-colles dans tes posts et emails. Pour un produit à petit prix vendu en masse via les réseaux, c'est la solution la plus rapide et la plus frictionless. Le formulaire deux colonnes est plus adapté à une prestation ou à un produit nécessitant une mise en contexte plus longue.

---

## Question 3

**Type** : Vrai / Faux (True/False)

La boutique affiche "déconnectée". Le réflexe le plus fiable à long terme est de recoller le jeton dans l'interface Settings, Connection.

- [ ] Vrai
- [x] Faux

**Explication** : Recoller le jeton dans l'interface fonctionne dans l'immédiat, mais ne résout pas la cause : certains plugins de sécurité régénèrent les salts WordPress, ce qui invalide le jeton stocké en base. La méthode robuste (vue au module 1 et rappelée en B.3) est de définir le jeton directement dans wp-config.php avec `define( 'SURECART_API_TOKEN', '...' )`. Là, il survit aux régénérations.

---

## Question 4

**Type** : Choix unique (Single Choice)

Tu suis la méthode de dépannage de B.3. Tu as vidé les 3 caches et testé sur un autre navigateur, mais le problème persiste. Quelle est la prochaine étape logique ?

- [ ] Contacter le support SureCart immédiatement
- [ ] Réinstaller SureCart
- [x] Désactiver tes autres plugins un par un, en vérifiant après chaque désactivation
- [ ] Changer de processeur de paiement

**Explication** : La méthode de dépannage suit un ordre précis : on commence par le simple (mises à jour, caches, autre navigateur), puis on cherche un conflit. On désactive les plugins un par un - quand le problème disparaît, on a trouvé le coupable. Faire plusieurs changements en même temps rend impossible d'identifier la cause.

---

## Question 5

**Type** : Choix multiple (Multiple Choice)

Dans le parcours F1, lesquels de ces éléments sont couverts ? (plusieurs bonnes réponses)

- [x] Vendre une prestation de service avec paiement unique
- [x] Vendre un ebook avec livraison automatique du fichier
- [ ] Gérer un catalogue de produits physiques avec variations et zones d'expédition
- [x] Mettre en place un order bump sur un petit prix (plan Pro)
- [ ] Créer un espace membre avec contenu protégé et accès restreint

**Explication** : Le parcours F1 couvre le socle : encaisser proprement, produits numériques, prestations, abonnements simples, leviers de panier basiques. La gestion de catalogue physique avec stock et expédition relève du parcours Boutique (F3). Les espaces membres et le contenu protégé relèvent du parcours Créateurs (F2). Tu choisis la suite selon ce que tu vends réellement.
