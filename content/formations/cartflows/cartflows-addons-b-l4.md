# Lecon B.4 - Rediger des emails de relance qui convertissent

## Metadata

- **Formation** : CartFlows Add-ons (premium - FRM-008)
- **Module** : B - Cart Abandonment Recovery
- **Duree cible** : 12 min (~1 500 mots)
- **Type** : Video HeyGen + voix ElevenLabs
- **Objectif pedagogique** : Rediger le contenu exact des 3 emails de relance (objet + corps) en appliquant les regles de copywriting qui maximisent le taux de conversion.

---

## Script narration

**[INTRO - face camera]**

La sequence est configuree, les delais sont en place. Maintenant, on ecrit les emails. Et c'est la que la plupart des gens se plantent.

Un email de relance, ce n'est pas un email marketing classique. C'est un message personnel, court, direct, avec un seul objectif : ramener le client a son panier. Pas de newsletter, pas de branding elabore, pas de pavés. Un message, un lien, c'est tout.

---

**[SECTION 1 - Email 1 (15 minutes) : le rappel neutre]**

**[ECRAN - editeur email avec contenu]**

Le premier email part 15 minutes apres l'abandon. Le client vient de quitter ta page. Il sait ce qu'il faisait. Il n'a pas besoin qu'on lui explique.

**Objet** : "Tu as oublie quelque chose dans ton panier"

Simple, factuel, zero pression. Pas de point d'exclamation, pas de majuscules, pas d'urgence artificielle. Le client ouvre l'email par curiosite ou par reflexe.

**Corps** :

"Hey {{customer.firstname}},

Tu as laisse {{cart.product.name}} dans ton panier.

Si tu veux finaliser ta commande, tout est encore la :

[Reprendre ma commande]({{cart.checkout_url}})

A bientot."

C'est tout. Quatre lignes. Le prenom pour la personnalisation, le nom du produit pour le rappel concret, le lien pre-rempli pour zero friction.

Pas de benefices, pas d'arguments, pas de temoignages. A ce stade, le client sait deja pourquoi il voulait acheter. Il a juste besoin d'un coup de pouce pour revenir.

Cet email est le plus performant de la sequence. Il convertit a lui seul 40 a 50% des recuperations totales. La raison : beaucoup d'abandons sont des accidents (distraction, probleme technique, heure tardive). Le rappel rapide suffit.

---

**[SECTION 2 - Email 2 (24 heures) : la valeur]**

**[ECRAN - editeur email avec contenu]**

24 heures plus tard. Le client n'a pas reagi au premier email. Il a eu le temps d'oublier, de comparer, de se poser des questions. L'email 2 doit raviver l'interet en rappelant pourquoi le produit vaut le coup.

**Objet** : "Ton panier t'attend toujours"

Leger sentiment de continuite. Le panier "attend" - c'est personnel, pas commercial.

**Corps** :

"Hey {{customer.firstname}},

Ton {{cart.product.name}} est toujours dans ton panier.

Voici pourquoi nos clients l'adorent :

- [Benefice 1 : ce que le produit resout concretement]
- [Benefice 2 : le gain de temps ou d'argent]
- [Benefice 3 : ce qui le differencie]

'[Temoignage court d'un client satisfait]' - Prenom, client

[Finaliser ma commande - {{cart.total}}]({{cart.checkout_url}})

Si tu as une question, reponds directement a cet email."

L'email 2 est plus long mais reste structure. Trois benefices en liste a puces (pas des paragraphes), un temoignage court, et le lien avec le montant total affiche.

La derniere ligne est importante : "reponds directement a cet email". Ca humanise l'echange. Le client sait qu'il peut poser une question, et parfois c'est exactement ce dont il a besoin pour se decider.

Adapte les benefices au produit. Si tu vends une formation, parle du gain de competence. Si tu vends un plugin, parle du temps economise. Sois concret, pas generique.

---

**[SECTION 3 - Email 3 (3 jours) : l'offre irresistible]**

**[ECRAN - editeur email avec contenu et coupon]**

Trois jours. Le client n'a toujours pas finalise. Les deux premiers emails n'ont pas suffi. Il est temps de proposer quelque chose de concret.

**Objet** : "Derniere chance : -10% sur ta commande"

L'objet annonce l'offre directement. Pas de mystere, pas de teasing. Le client voit "-10%" et il sait immediatement ce qu'il gagne en ouvrant l'email.

**Corps** :

"Hey {{customer.firstname}},

Ca fait quelques jours que {{cart.product.name}} t'attend.

Pour t'aider a te decider, voici un code de reduction exclusif :

**{{coupon.code}}** - 10% de reduction sur ta commande

Ce code expire dans 48 heures.

[Utiliser mon code et finaliser ma commande]({{cart.checkout_url}})

C'est la derniere fois qu'on t'envoie un email pour ce panier. Apres ca, ton panier sera supprime."

Deux leviers d'urgence dans cet email. Le coupon qui expire dans 48 heures - c'est reel, pas une fausse urgence. Et l'annonce que c'est le dernier email - le client sait que l'offre ne se repetera pas.

Le `{{coupon.code}}` est genere automatiquement par le plugin. Chaque client recoit un code unique. On configure ca en detail dans la lecon 5.

---

**[SECTION 4 - Les regles de copywriting pour les emails de relance]**

**[ECRAN - slide 5 regles]**

Cinq regles qui s'appliquent aux trois emails.

**Regle 1 : court.** Chaque email doit etre lisible en 15 secondes maximum. Si le client doit scroller sur mobile, c'est trop long.

**Regle 2 : direct.** Pas de "Nous esperons que tu vas bien". Pas de "Dans le monde du e-commerce aujourd'hui". Le client a abandonne un panier, va droit au sujet.

**Regle 3 : un seul CTA par email.** Un bouton, un lien, une action. Pas deux offres, pas trois liens differents. Le client doit savoir exactement quoi faire.

**Regle 4 : texte avant HTML.** Les emails de relance les plus performants sont souvent en texte brut ou en HTML tres simple. Un email qui ressemble a un message personnel convertit mieux qu'une newsletter graphiquement elaboree. Le client doit avoir l'impression de recevoir un message, pas une publicite.

**Regle 5 : le lien pre-rempli est non negociable.** Chaque email doit contenir `{{cart.checkout_url}}`. Sans ce lien, le client doit retourner sur ta boutique, retrouver le produit, l'ajouter au panier. Chaque etape supplementaire tue la conversion.

---

**[CONCLUSION - face camera]**

Trois emails, trois tons, trois objectifs. Le rappel neutre, la creation de valeur, l'offre irresistible. Chaque email est court, direct, avec un seul lien d'action.

Copie ces templates, adapte-les a tes produits, et active la sequence. Dans la prochaine lecon, on configure les coupons uniques qui rendent l'email 3 encore plus puissant.

---

## Notes de production

- **Visuels** : captures editeur email avec contenu redige, slide 5 regles copywriting
- **Donnees** : email 1 = 40-50% des recuperations, taux ouverture emails relance > 40% (moyenne industrie)
- **Transition** : enchaine sur LB.5 (generer des coupons uniques automatiquement)
