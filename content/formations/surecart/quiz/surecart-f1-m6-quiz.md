# Quiz - Module 6 : Augmenter le panier, revenue boosters

Quiz de validation de fin de module (5 questions). Source à recopier dans TutorLMS.

## Réglages TutorLMS recommandés

- **Placement** : fin de Module 6, avec verrouillage de la progression (l'élève doit réussir le quiz pour débloquer le Module 7).
- **Note de passage** : 80 % (4 bonnes réponses sur 5).
- **Tentatives** : illimitées (ou 3), pour que l'élève réessaie sans blocage.
- **Affichage des réponses** : révéler la bonne réponse et l'explication après chaque tentative.
- **Points** : 1 point par question.

La bonne réponse est marquée `[x]`. Le champ "Answer Explanation" de TutorLMS reprend la ligne **Explication**.

---

## Question 1

**Type** : Choix unique (Single Choice)

Quelle est la différence principale entre un order bump et un upsell dans SureCart ?

- [x] L'order bump se déclenche pendant le paiement, l'upsell se déclenche après l'achat
- [ ] L'order bump se déclenche après l'achat, l'upsell se déclenche pendant le paiement
- [ ] Les deux se déclenchent pendant le paiement, mais à des étapes différentes
- [ ] L'order bump est gratuit, l'upsell est payant

**Explication** : L'order bump apparaît au checkout, juste avant que le client valide son paiement : il coche une case et le produit s'ajoute sans changer de page. L'upsell, lui, se déclenche après l'achat : le client a déjà payé, ses données bancaires sont enregistrées, et il peut accepter l'offre sans ressaisir sa carte. Ce sont deux moments distincts, deux logiques différentes.

---

## Question 2

**Type** : Choix unique (Single Choice)

Tu veux afficher un order bump uniquement quand ta formation "LMS WordPress" est dans le panier. Que fais-tu dans SureCart ?

- [ ] Tu réglages la priorité de l'order bump à 1
- [ ] Tu actives l'application automatique de la remise
- [x] Tu cliques sur "Add A Condition" et tu choisis le produit ou le prix comme déclencheur
- [ ] Tu places le bloc Order Bumps en haut du formulaire

**Explication** : Les conditions d'affichage sont ce qui rend les order bumps ciblés. Via "Add A Condition", tu choisis un déclencheur par produit ou par prix - par exemple "ce produit est au panier". Tu peux empiler plusieurs conditions et régler la logique (l'un, tous, ou aucun). La priorité et la position dans le formulaire sont des réglages distincts qui ne conditionnent pas l'affichage.

---

## Question 3

**Type** : Choix unique (Single Choice)

Dans un tunnel d'upsell, tu veux faire passer un client d'un abonnement mensuel à un abonnement annuel. Quel comportement dois-tu choisir pour l'étape d'upsell ?

- [ ] Ajouter à la commande
- [x] Remplacer toute la commande
- [ ] Ignorer si déjà acheté
- [ ] Désactiver le minuteur

**Explication** : "Remplacer toute la commande" échange la commande d'origine par la nouvelle offre - parfait pour une vraie montée en gamme comme passer du mensuel à l'annuel, ou d'une formule Starter à une formule Pro. "Ajouter à la commande" empile l'offre par-dessus l'existant, ce qui est adapté pour un produit supplémentaire ou un bonus, pas pour un changement de formule.

---

## Question 4

**Type** : Vrai / Faux (True/False)

Activer la récupération des paniers abandonnés dans SureCart est conforme au RGPD dès la configuration, sans ajout d'un plugin tiers.

- [x] Vrai
- [ ] Faux

**Explication** : SureCart gère nativement la conformité RGPD pour la récupération de paniers abandonnés. La fonction envoie les emails de relance uniquement aux personnes qui ont laissé leur adresse email pendant le processus de paiement. Des garde-fous intégrés - arrêt automatique si la commande est finalisée, délai de grâce, mode test - complètent le dispositif. Tu actives depuis Settings, Abandoned Checkout, sans plugin supplémentaire.

---

## Question 5

**Type** : Choix multiple (Multiple Choice)

Dans quels cas le Quick Add est-il vraiment pertinent pour ta boutique ? (plusieurs bonnes réponses)

- [x] Tu as un catalogue de plusieurs produits que les clients parcourent et peuvent combiner
- [ ] Tu vends une seule formation bien identifiée avec un Instant Checkout
- [x] Tu veux réduire le nombre d'étapes entre la page boutique et le panier
- [ ] Tu n'as que deux offres et tes clients savent exactement ce qu'ils viennent chercher
- [x] Tes clients ont tendance à ajouter plusieurs articles lors d'une même session

**Explication** : Le Quick Add brille sur un vrai catalogue, quand les clients parcourent plusieurs produits et en prennent plusieurs à la fois. Pour une ou deux offres bien identifiées, l'Instant Checkout ou un lien direct restent plus adaptés et plus simples. Activer le Quick Add uniquement parce que la fonction existe - sans catalogue qui le justifie - complique l'interface sans apporter de valeur.
