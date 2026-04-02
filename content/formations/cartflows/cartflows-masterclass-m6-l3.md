# Lecon 6.3 — Tester les order bumps et upsells

## Metadata

- **Formation** : CartFlows Masterclass Vente (premium — FRM-007)
- **Module** : 6 — A/B Testing et Analytics
- **Duree cible** : 8 min (~1100 mots)
- **Type** : Video HeyGen + voix ElevenLabs
- **Objectif pedagogique** : Savoir appliquer l'A/B testing aux order bumps et aux upsells. Comprendre comment isoler les variables quand on teste plusieurs etapes du funnel.

---

## Script narration

**[INTRO — face camera]**

Tu sais tester ta page checkout. Maintenant, on s'attaque aux deux autres leviers de ton funnel : les order bumps et les upsells. Ce sont les etapes qui augmentent ta valeur par commande. Et elles se testent aussi.

La methode est la meme : une variable a la fois, volume suffisant, et patience. Mais il y a des subtilites specifiques aux bumps et aux upsells qu'on va voir ensemble.

---

**[SECTION 1 — A/B tester un order bump]**

**[ECRAN — CartFlows > Checkout > Order Bump settings]**

L'order bump, c'est cette petite case a cocher sur la page de paiement — l'offre complementaire que le client ajoute en un clic avant de valider sa commande.

Pour le tester, tu vas creer deux variantes de ton checkout. Variante A avec le bump actuel, variante B avec un bump different. Meme methode que la lecon precedente : CartFlows > step Checkout > A/B Test > ajouter une variante.

Exemple concret. Tu vends une formation WordPress a 97 euros. Ton bump actuel est un pack de templates a 17 euros. Tu veux tester si un accompagnement coaching 30 minutes a 27 euros fonctionnerait mieux.

Variante A : bump "Pack 12 templates Kadence" a 17 euros. Variante B : bump "Session coaching 30 min" a 27 euros.

Ce que tu mesures : le taux d'acceptation du bump et le revenu genere par le bump. Un bump a 27 euros avec 10% d'acceptation rapporte plus qu'un bump a 17 euros avec 12% d'acceptation. C'est le revenu total qui compte, pas uniquement le taux d'acceptation.

---

**[SECTION 2 — A/B tester un upsell]**

**[ECRAN — CartFlows > Flow > step Upsell > A/B Test]**

L'upsell post-achat se teste de la meme maniere. Tu accedes au step Upsell dans ton flow, tu actives l'A/B Test, et tu crees une variante.

Ici, le levier principal a tester est le prix. Exemple : ton upsell actuel est un coaching premium a 97 euros. Tu veux savoir si le meme coaching a 67 euros genererait plus de revenu total grace a un meilleur taux d'acceptation.

Variante A : upsell coaching a 97 euros. Variante B : upsell coaching a 67 euros.

Scenario possible : la variante A a 97 euros est acceptee par 8% des acheteurs. La variante B a 67 euros est acceptee par 14%. Calcul rapide : 97 x 0.08 = 7.76 euros de revenu moyen par acheteur. 67 x 0.14 = 9.38 euros. La variante B gagne — meme si le prix unitaire est plus bas.

C'est pour ca qu'on teste. L'intuition aurait dit "le prix plus haut rapporte plus". Les donnees disent le contraire.

---

**[SECTION 3 — Isoler les variables : la regle sequentielle]**

**[ECRAN — schema "ordre de test" : checkout > bump > upsell]**

Voici la question que tu te poses surement : est-ce que je peux tester le checkout, le bump et l'upsell en meme temps ?

La reponse est non. Pas simultanement.

Si tu testes le titre du checkout et le prix du bump en meme temps, tu ne sais pas si le changement de conversion vient du titre ou du bump. Les deux elements interagissent : un meilleur titre peut augmenter la confiance du client, ce qui augmente aussi l'acceptation du bump.

La bonne approche est sequentielle :

Etape 1 : teste le checkout d'abord. C'est la page la plus importante — si le client ne passe pas le checkout, il ne verra jamais le bump ni l'upsell. Optimise d'abord l'entree du funnel.

Etape 2 : une fois le checkout optimise, teste l'order bump. Le volume de trafic sur le bump depend directement du taux de conversion du checkout. Un checkout optimise te donne plus de donnees pour le test du bump.

Etape 3 : enfin, teste l'upsell. Le volume de trafic sur l'upsell depend du checkout et du bump. C'est la derniere etape a tester parce que c'est celle qui recoit le moins de visiteurs.

Cette sequence respecte la logique du funnel : du haut vers le bas, du plus large au plus etroit.

---

**[SECTION 4 — Cas pratique : quand le bump et l'upsell interagissent]**

**[ECRAN — tableau d'interaction bump/upsell]**

Il y a un cas specifique a connaitre. Le prix du bump peut influencer l'acceptation de l'upsell. Si le client vient d'ajouter un bump a 27 euros, sa commande totale est plus elevee. Il peut etre moins enclin a accepter un upsell a 97 euros ensuite.

C'est ce qu'on appelle la fatigue d'achat. Plus le total monte, plus la resistance augmente.

Consequence pratique : quand tu as termine tes tests sequentiels et que tu as optimise chaque etape individuellement, fais un dernier test global. Mesure le revenu par visiteur du funnel complet. C'est le seul chiffre qui integre toutes les interactions entre les etapes.

Si tu optimises le bump de maniere isolee mais que ca fait chuter l'upsell, le gain net peut etre negatif. Le revenu par visiteur te protege de ce piege.

---

**[OUTRO — face camera]**

La regle est claire : teste dans l'ordre du funnel — checkout d'abord, bump ensuite, upsell en dernier. Ne teste jamais deux etapes simultanement. Et une fois que chaque etape est optimisee, verifie le revenu par visiteur global pour confirmer que les pieces fonctionnent ensemble.

Dans la prochaine lecon, on va apprendre a lire les resultats correctement. Parce que la signification statistique, c'est le gardien qui t'empeche de prendre des decisions sur du bruit.

---

## Notes de production

- **Visuels** : captures CartFlows (bump settings, upsell A/B Test), schema ordre de test, tableau interaction bump/upsell
- **Captures d'ecran** : CartFlows Pro — Order Bump config, Upsell step A/B Test (4 captures minimum)
- **Ton** : pratique et methodique, avec exemples chiffres
- **Duree estimee** : ~8 min a debit normal
- **Transition** : enchaine directement sur L6.4 (signification statistique)
