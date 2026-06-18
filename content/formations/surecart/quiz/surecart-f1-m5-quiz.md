# Quiz - Module 5 : Vendre en récurrent, abonnements simples

Quiz de validation de fin de module (5 questions). Source à recopier dans TutorLMS.

## Réglages TutorLMS recommandés

- **Placement** : fin du Module 5, avec verrouillage de la progression (l'élève doit réussir le quiz pour débloquer le Module 6).
- **Note de passage** : 80 % (4 bonnes réponses sur 5).
- **Tentatives** : illimitées (ou 3), pour que l'élève réessaie sans blocage.
- **Affichage des réponses** : révéler la bonne réponse et l'explication après chaque tentative.
- **Points** : 1 point par question.

La bonne réponse est marquée `[x]`. Le champ "Answer Explanation" de TutorLMS reprend la ligne **Explication**.

---

## Question 1

**Type** : Choix unique (Single Choice)

Dans SureCart, pour créer un abonnement mensuel à 15 euros, tu pars d'un produit, tu cliques sur Add a Price et tu choisis le type de paiement Subscription. Quel est le bon réglage pour l'intervalle ?

- [ ] Tu laisses l'intervalle vide, SureCart utilise le mois par défaut
- [ ] Tu choisis "année" puis tu divises le montant par 12 pour afficher 15 euros
- [x] Tu choisis "mois" comme intervalle, et tu saisis 15 comme montant
- [ ] L'intervalle n'est pas modifiable après la création du prix

**Explication** : L'abonnement est un type de paiement avec un intervalle de répétition que tu fixes librement : jour, semaine, mois ou année. Pour un mensuel à 15 euros, tu choisis mois et tu saisis 15. L'intervalle est modifiable tant que personne n'est encore abonné sur ce prix.

---

## Question 2

**Type** : Choix unique (Single Choice)

Un client souscrit à ton abonnement mensuel avec un essai gratuit de 7 jours. Il saisit ses coordonnées bancaires au checkout un lundi. Quand est-il débité pour la première fois ?

- [ ] Immédiatement, le lundi de la souscription
- [ ] Le mercredi suivant, soit 48 heures après
- [x] Le lundi suivant, soit 7 jours après la souscription, au terme de l'essai
- [ ] Il choisit lui-même sa date de premier débit

**Explication** : Avec un essai gratuit, le client saisit ses coordonnées bancaires mais n'est pas débité immédiatement. Le premier débit intervient à la fin de l'essai - ici 7 jours plus tard. SureCart envoie un rappel 3 jours avant la fin de l'essai. C'est ensuite que l'abonnement mensuel démarre et que le cycle se répète.

---

## Question 3

**Type** : Choix multiple (Multiple Choice)

Tu veux proposer un "essai à 1 euro" sur ton abonnement mensuel. Quelles actions sont nécessaires dans SureCart ? (plusieurs bonnes réponses)

- [x] Activer le toggle Free Trial et indiquer une durée (ex : 7 jours)
- [x] Activer le toggle Setup Fee, nommer les frais (ex : Essai première semaine) et saisir 1 comme montant
- [x] Activer l'option Charge setup fee during free trial
- [ ] Créer un deuxième produit dédié à l'essai payant
- [ ] Passer par les réglages Stripe pour paramétrer le montant de l'essai

**Explication** : Un essai payant se configure entièrement dans SureCart, sur le prix abonnement : Free Trial pour la durée, Setup Fee pour le montant et le nom, et Charge setup fee during free trial pour que ce montant soit débité immédiatement au lieu d'attendre la fin de l'essai. Pas besoin d'un deuxième produit ni d'aller dans Stripe.

---

## Question 4

**Type** : Vrai / Faux (True/False)

Un client te demande de mettre son abonnement en pause. Tu cliques sur Actions, Pause Subscription. La pause prend effet immédiatement, dès la confirmation.

- [ ] Vrai
- [x] Faux

**Explication** : La pause ne prend pas effet immédiatement. Elle démarre à la fin de la période déjà payée. Si le client a payé jusqu'au 1er juin, la pause commencera le 1er juin - et non le jour où tu cliques. Pendant la pause, aucun prélèvement et les accès liés sont suspendus, puis rendus automatiquement à la date de reprise que tu as choisie.

---

## Question 5

**Type** : Choix unique (Single Choice)

Tu as un abonnement annuel à 300 euros. Dans le tableau de bord SureCart, combien cet abonnement contribue-t-il à ton MRR ?

- [ ] 300 euros, soit le montant annuel encaissé
- [ ] 0 euro, les abonnements annuels ne sont pas comptés dans le MRR
- [x] 25 euros, soit 300 divisé par 12
- [ ] 150 euros, soit la moitié de l'année

**Explication** : Le MRR (Monthly Recurring Revenue) ramène tous tes abonnements à une base mensuelle pour les comparer entre eux. Un abonnement annuel à 300 euros est divisé par 12, soit 25 euros de MRR. Un mensuel à 25 euros pèse le même MRR - c'est exactement ce qui permet de les comparer. Les paiements échelonnés, eux, ne sont pas comptés dans le MRR : ils ont une fin, ce n'est pas du vrai récurrent.
