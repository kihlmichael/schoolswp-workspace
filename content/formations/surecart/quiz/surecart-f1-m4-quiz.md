# Quiz - Module 4 : Encaisser proprement

Quiz de validation de fin de module (5 questions). Source à recopier dans TutorLMS.

## Réglages TutorLMS recommandés

- **Placement** : fin de Module 4, avec verrouillage de la progression (l'élève doit réussir le quiz pour débloquer le Module 5).
- **Note de passage** : 80 % (4 bonnes réponses sur 5).
- **Tentatives** : illimitées (ou 3), pour que l'élève réessaie sans blocage.
- **Affichage des réponses** : révéler la bonne réponse et l'explication après chaque tentative.
- **Points** : 1 point par question.

La bonne réponse est marquée `[x]`. Le champ "Answer Explanation" de TutorLMS reprend la ligne **Explication**.

---

## Question 1

**Type** : Choix unique (Single Choice)

Dans SureCart, Settings, Orders & Receipts, tu as le choix entre deux types de numérotation des commandes. Pourquoi choisir la numérotation séquentielle plutôt qu'aléatoire ?

- [ ] Parce que la numérotation aléatoire ralentit le chargement des commandes
- [ ] Parce que SureCart facture un supplément pour la numérotation aléatoire
- [x] Parce qu'une numérotation continue et ordonnée est ce que ton comptable et l'administration attendent
- [ ] Parce que la numérotation aléatoire ne fonctionne qu'en mode test

**Explication** : La numérotation séquentielle te permet d'ajouter un préfixe et de définir le numéro de départ. Elle produit une suite ordonnée, ce qui est la norme attendue en comptabilité. La numérotation aléatoire fonctionne techniquement, mais elle complique le suivi et peut poser des problèmes lors d'un contrôle.

---

## Question 2

**Type** : Choix unique (Single Choice)

Quand tu publies une facture dans SureCart (Create Invoice), plusieurs événements se déclenchent automatiquement. Lequel de ces événements ne fait PAS partie de ce qui se passe à la publication ?

- [ ] Un email est envoyé au client
- [ ] La facture reçoit son numéro officiel
- [x] Le paiement est débité automatiquement sur la carte du client
- [ ] Un lien partageable est généré

**Explication** : À la publication, SureCart envoie l'email, attribue le numéro de facture, récupère les adresses et génère un lien partageable. Mais la facture est payable - pas débitée automatiquement. C'est le client qui choisit de payer en cliquant sur le lien. C'est toute la force du système : une facture que le client règle en ligne à son rythme.

---

## Question 3

**Type** : Choix multiple (Multiple Choice)

Tu rembourses un client qui a acheté un cours en ligne. Dans le panneau de remboursement SureCart, quelles options dois-tu cocher pour que le remboursement soit complet ? (plusieurs bonnes réponses)

- [ ] Restock (remettre le cours en stock)
- [x] Revoke Purchase (révoquer l'achat et retirer l'accès au cours)
- [x] Choisir une raison de remboursement dans le menu
- [ ] Envoyer manuellement un email au client depuis WordPress
- [x] Vérifier et ajuster le montant à rembourser avant de confirmer

**Explication** : Pour un cours en ligne, Restock ne s'applique pas (pas de stock physique). Revoke Purchase est essentiel : sans lui, le client est remboursé mais garde l'accès au cours. La raison de remboursement est utile pour ton suivi côté processeur. SureCart envoie automatiquement un email au client - pas besoin d'en envoyer un manuellement. Enfin, vérifier le montant permet de faire un remboursement partiel si c'est un geste commercial.

---

## Question 4

**Type** : Vrai / Faux (True/False)

Si tu fixes une date de fin sur un coupon SureCart et que tu veux qu'il expire le 20 juin à minuit, heure de Paris, tu peux entrer le 20 juin à 00:00 dans le champ de date de fin sans autre précaution.

- [ ] Vrai
- [x] Faux

**Explication** : La date de fin dans SureCart est exprimée en heure universelle UTC. En été, la France est à UTC+2 : minuit à Paris correspond à 22:00 UTC la veille. Si tu entres le 20 juin à 00:00 sans ajuster, ton coupon expirera deux heures plus tôt que prévu pour tes clients. Pense toujours au décalage entre UTC et l'heure locale avant de fixer une date d'expiration.

---

## Question 5

**Type** : Choix unique (Single Choice)

Pour activer la collecte de TVA dans SureCart et permettre à tes clients professionnels (B2B) de renseigner leur numéro de TVA au checkout, dans quel ordre dois-tu procéder ?

- [ ] Ajouter le champ VAT or Tax ID Input au formulaire, puis activer Tax Collection dans Settings, Taxes
- [ ] Activer Tax Collection dans Settings, Taxes uniquement - le champ TVA s'ajoute automatiquement au formulaire
- [x] Activer Tax Collection dans Settings, Taxes, puis ajouter le champ VAT or Tax ID Input dans SureCart, Forms, sur ton formulaire de paiement
- [ ] Configurer les régions de taxe produit par produit, puis activer Tax Collection

**Explication** : Tax Collection doit être activé en premier dans Settings, Taxes - tant qu'il est éteint, les réglages TVA restent cachés. Ensuite, le champ VAT or Tax ID Input s'ajoute manuellement dans SureCart, Forms, sur le formulaire concerné. Ce champ ne s'ajoute pas seul (sauf si tu actives l'option Require VAT Number qui le force). Rappel : la configuration de l'outil ne remplace pas l'avis de ton comptable sur ce que tu dois collecter et déclarer.
