# Lecon B.3 - Configurer la sequence de relance (15 min, 1 jour, 3 jours)

## Metadata

- **Formation** : CartFlows Add-ons (premium - FRM-008)
- **Module** : B - Cart Abandonment Recovery
- **Duree cible** : 10 min (~1 300 mots)
- **Type** : Video HeyGen + voix ElevenLabs
- **Objectif pedagogique** : Configurer les 3 emails de la sequence de relance par defaut (delais, objets, contenus, variables dynamiques) et comprendre la logique de chaque etape.

---

## Script narration

**[INTRO - face camera]**

Le plugin est installe. Il capture les emails. Maintenant, la vraie question : qu'est-ce qu'on envoie, et quand ?

Cart Abandonment Recovery fonctionne avec une sequence de 3 emails automatiques. Chaque email a un role precis, un timing precis, et un objectif precis. On va configurer les trois ensemble.

---

**[SECTION 1 - La logique de la sequence en 3 temps]**

**[ECRAN - schema timeline 15 min → 24h → 3 jours]**

La sequence par defaut suit une escalade progressive.

Email 1 : 15 minutes apres l'abandon. C'est le rappel immediat. Le client vient de quitter ta page, il a peut-etre ete distrait, son telephone a sonne, sa connexion a coupe. L'email est un simple rappel : "Hey, tu as laisse quelque chose dans ton panier."

Email 2 : 24 heures apres l'abandon. Le client a eu le temps d'oublier. Cet email rappelle le produit mais ajoute des arguments : les benefices, un temoignage, un element de rarete. L'objectif est de raviver l'interet.

Email 3 : 3 jours apres l'abandon. Si les deux premiers emails n'ont pas converti, on sort l'offre speciale. Un coupon de reduction, une livraison gratuite, quelque chose de concret pour declencher l'achat.

Cette escalade est testee et eprouvee. Le premier email convertit le plus (les gens qui avaient juste besoin d'un rappel). Le deuxieme recupere les hesitants. Le troisieme convertit ceux qui ont besoin d'un incentive supplementaire.

---

**[SECTION 2 - Configurer l'email 1 (15 minutes)]**

**[ECRAN - Cart Abandonment → Follow-Up Emails → Email 1]**

Va dans WooCommerce → Cart Abandonment → Follow-Up Emails. Tu vois la liste des 3 emails preconfigures.

Clique sur le premier email. Voici les champs a configurer.

**Delai d'envoi** : 15 minutes. C'est la valeur par defaut et c'est le bon timing. Pas avant - le client est peut-etre encore en train de chercher sa carte bancaire. Pas apres - la memoire du panier est encore fraiche a 15 minutes.

**Objet de l'email** : l'objet par defaut est generique. Remplace-le par quelque chose de direct et personnel. Exemple : "Tu as oublie quelque chose dans ton panier". Pas de point d'exclamation, pas de majuscules, pas de spam words.

**Contenu de l'email** : le corps doit etre court. Trois a quatre phrases maximum. Rappelle le produit, donne le lien pour revenir au panier, c'est tout. Pas de discours de vente a ce stade.

Assure-toi que l'email est en statut "Active".

---

**[SECTION 3 - Configurer l'email 2 (24 heures)]**

**[ECRAN - Cart Abandonment → Follow-Up Emails → Email 2]**

Clique sur le deuxieme email.

**Delai d'envoi** : 24 heures. Le client a dormi dessus. Il a probablement oublie ton produit. Cet email doit lui rappeler pourquoi il s'etait interesse.

**Objet** : "Ton panier t'attend toujours" ou "Ne passe pas a cote de [produit]". L'objet doit creer un leger sentiment d'urgence sans etre agressif.

**Contenu** : cette fois, on argumente. Rappelle le nom du produit, ajoute deux ou trois benefices concrets, inclus un temoignage si tu en as un. Termine par le lien vers le panier.

L'email 2 est plus long que le 1, mais reste concis. Cinq a sept phrases, pas un roman.

---

**[SECTION 4 - Configurer l'email 3 (3 jours)]**

**[ECRAN - Cart Abandonment → Follow-Up Emails → Email 3]**

Le troisieme email, c'est la derniere chance.

**Delai d'envoi** : 3 jours (72 heures). Si le client n'a pas reagi aux deux premiers emails, il a besoin d'un incentive supplementaire pour passer a l'action.

**Objet** : "Derniere chance : -10% sur ta commande" ou "On a un cadeau pour toi". L'objet annonce clairement l'offre.

**Contenu** : cet email presente le coupon de reduction. Le code est genere automatiquement par le plugin (on le configure dans la lecon 5). Le corps de l'email rappelle le produit, presente le coupon, et donne une deadline d'expiration. L'urgence ici est reelle : le coupon expire, l'offre ne sera pas repetee.

---

**[SECTION 5 - Les variables dynamiques]**

**[ECRAN - liste des variables dans l'editeur d'email]**

Cart Abandonment Recovery propose des variables dynamiques que tu peux inserer dans tes emails. C'est ce qui rend chaque email personnalise automatiquement.

Les variables essentielles :

- `{{customer.firstname}}` - le prenom du client. Indispensable pour personnaliser l'accroche.
- `{{cart.product.name}}` - le nom du produit abandonne. Le client voit exactement ce qu'il a laisse.
- `{{cart.total}}` - le montant total du panier. Rappelle l'engagement financier.
- `{{cart.checkout_url}}` - le lien magique. Ce lien ramene le client directement a son panier pre-rempli avec tous les produits deja selectionnes. Il n'a qu'a entrer ses infos de paiement.

Le `{{cart.checkout_url}}` est la variable la plus importante. Sans elle, le client devrait retourner sur ta boutique, retrouver le produit, l'ajouter au panier, et recommencer le checkout. Avec elle, un clic et il est de retour exactement ou il en etait. Zero friction.

Utilise ces variables dans chaque email. Un email qui dit "Hey Jean, tu as laisse le Pack Formation WordPress (89€) dans ton panier" convertit beaucoup mieux qu'un email generique.

---

**[SECTION 6 - Activer et desactiver individuellement]**

**[ECRAN - toggle active/inactive sur chaque email]**

Chaque email de la sequence peut etre active ou desactive independamment. Tu peux par exemple :

- Activer les 3 emails (recommande au debut pour tester la sequence complete)
- Desactiver l'email 3 si tu ne veux pas offrir de coupon
- Desactiver l'email 2 et garder uniquement le rappel immediat et l'offre finale

Mon conseil : commence avec les 3 actifs. Teste pendant 30 jours. Analyse les resultats (on voit ca dans la lecon 6). Ensuite, ajuste en fonction des donnees.

---

**[CONCLUSION - face camera]**

Ta sequence de relance est configuree. Trois emails, trois moments, trois approches. Le rappel immediat, l'argumentation, et l'offre speciale.

Mais configurer c'est une chose - bien rediger ces emails, c'en est une autre. Dans la prochaine lecon, on va ecrire le contenu exact de chaque email pour maximiser les conversions.

---

## Notes de production

- **Visuels** : schema timeline 15 min → 24h → 3 jours, captures ecran editeur d'email, liste des variables dynamiques
- **Donnees** : timing optimal 15 min/24h/72h (standard industrie), variables dynamiques du plugin
- **Transition** : enchaine sur LB.4 (rediger des emails de relance qui convertissent)
