# Lecon B.6 — Analyser le tableau de bord : taux de recuperation

## Metadata

- **Formation** : CartFlows Add-ons (premium — FRM-008)
- **Module** : B — Cart Abandonment Recovery
- **Duree cible** : 8 min (~1 100 mots)
- **Type** : Video HeyGen + voix ElevenLabs
- **Objectif pedagogique** : Lire et interpreter le tableau de bord Cart Abandonment Recovery (metriques cles, taux objectifs) et identifier quel email de la sequence performe le mieux.

---

## Script narration

**[INTRO — face camera]**

Ta sequence de relance tourne. Les emails partent automatiquement. Mais est-ce que ca fonctionne ? Combien de paniers tu recuperes ? Quel email convertit le plus ? Le tableau de bord de Cart Abandonment Recovery te donne toutes les reponses.

---

**[SECTION 1 — Acceder au tableau de bord]**

**[ECRAN — WooCommerce → Cart Abandonment → Reports]**

Va dans WooCommerce → Cart Abandonment → Reports. C'est le centre de controle de ta recuperation de paniers.

Le dashboard affiche quatre blocs principaux en haut de page :

- **Paniers abandonnes** : le nombre total de paniers detectes comme abandonnes sur la periode.
- **Emails envoyes** : le nombre total d'emails de relance envoyes (tous emails confondus).
- **Paniers recuperes** : le nombre de paniers qui ont ete finalises apres reception d'un email de relance.
- **Revenu recupere** : le montant total en euros des commandes recuperees.

C'est le revenu recupere qui te donne la reponse a la question la plus importante : combien d'argent le plugin te rapporte chaque mois.

---

**[SECTION 2 — Le taux de recuperation : objectif 20-30%]**

**[ECRAN — slide taux de recuperation]**

Le taux de recuperation, c'est le ratio paniers recuperes / paniers abandonnes. C'est ta metrique numero un.

Pour le calculer : si tu as 100 paniers abandonnes et 25 recuperes, ton taux de recuperation est de 25%.

Les objectifs realistes :

- **Moins de 10%** : la sequence a un probleme. Les emails ne sont peut-etre pas pertinents, les delais sont mauvais, ou les emails arrivent en spam.
- **10-20%** : correct, mais ameliorable. Retravaille le copywriting des emails et teste des objets differents.
- **20-30%** : excellent. C'est la cible. Ta sequence fonctionne bien.
- **Plus de 30%** : exceptionnel. Tu as probablement un bon produit avec un public engage.

Ne te compare pas aux benchmarks des grandes plateformes (Amazon, Zalando). Elles ont des equipes entieres dediees a l'optimisation. 20-30% pour une boutique WooCommerce independante, c'est un tres bon resultat.

---

**[SECTION 3 — Taux d'ouverture et taux de clic]**

**[ECRAN — metriques email par email]**

En dessous du dashboard global, tu as les metriques par email.

**Taux d'ouverture** : le pourcentage de destinataires qui ouvrent l'email. Objectif : plus de 40%.

Les emails de relance ont des taux d'ouverture naturellement eleves parce qu'ils sont pertinents — le client reconnait le contexte. C'est pas une newsletter aleatoire, c'est un rappel de quelque chose qu'il a fait il y a quelques heures.

Si ton taux d'ouverture est en dessous de 30%, le probleme est dans l'objet de l'email. Teste des variantes. Remplace "Ton panier t'attend" par "Tu as oublie {{cart.product.name}}". L'objet avec le nom du produit performe souvent mieux.

**Taux de clic** : le pourcentage de destinataires qui cliquent sur le lien dans l'email. Objectif : plus de 10%.

Si le taux d'ouverture est bon mais le taux de clic est faible, le probleme est dans le contenu de l'email. Le CTA n'est pas assez visible, le lien est perdu dans le texte, ou le message n'est pas assez convaincant.

Un bon reflexe : place le lien `{{cart.checkout_url}}` en haut de l'email ET en bas. Le client qui scanne rapidement doit voir le lien immediatement.

---

**[SECTION 4 — Analyser par email : quel email convertit le plus]**

**[ECRAN — tableau comparatif email 1 vs 2 vs 3]**

Le tableau de bord te permet de voir les performances de chaque email individuellement. C'est crucial pour optimiser ta sequence.

Pattern typique :

- **Email 1 (15 min)** : le plus gros volume de recuperation. 50-60% des paniers recuperes viennent de cet email. Normal — c'est le plus proche de l'abandon, et beaucoup d'abandons sont des accidents.
- **Email 2 (24h)** : recuperation moderee. 20-30% des recuperations. Les clients qui avaient besoin de reflechir.
- **Email 3 (3 jours)** : le coupon fait la difference. 10-20% des recuperations, mais le montant moyen est souvent plus eleve (les clients qui attendent le coupon ont souvent des paniers plus gros).

Si l'email 1 ne convertit pas du tout, verifie que le delai de 15 minutes est respecte et que les emails ne tombent pas en spam. Si l'email 3 ne convertit pas, augmente le montant du coupon ou teste la livraison gratuite a la place.

---

**[SECTION 5 — Frequence d'analyse]**

**[ECRAN — calendrier de suivi]**

Ne regarde pas le tableau de bord tous les jours. Les donnees sur 24 heures ne sont pas significatives.

Mon conseil : analyse une fois par semaine pendant le premier mois, puis une fois par mois quand la sequence est stabilisee.

A chaque analyse, pose-toi trois questions :
1. Mon taux de recuperation global est-il au-dessus de 20% ?
2. Quel email de la sequence recupere le plus ?
3. Mes taux d'ouverture sont-ils au-dessus de 40% ?

Si la reponse est oui aux trois, ta sequence fonctionne. Tu peux passer a l'optimisation fine. Si la reponse est non a l'une d'entre elles, c'est la priorite a traiter.

---

**[CONCLUSION — face camera]**

Le tableau de bord te dit exactement ce qui fonctionne et ce qui ne fonctionne pas. Paniers recuperes, revenu genere, performance par email. Pas de devinettes, des donnees.

Dans la prochaine lecon, on va aller plus loin en segmentant les abandons pour adapter ta strategie selon le type de client et le montant du panier.

---

## Notes de production

- **Visuels** : capture dashboard Reports, slide objectifs par metrique, tableau comparatif email 1/2/3
- **Donnees** : objectifs 20-30% recuperation, >40% ouverture, >10% clic (benchmarks industrie)
- **Transition** : enchaine sur LB.7 (segmenter les abandons)
