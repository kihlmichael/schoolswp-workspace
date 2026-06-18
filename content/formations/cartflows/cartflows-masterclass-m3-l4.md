# Lecon 3.4 - Pre-remplir le checkout pour les clients existants

## Metadata

- **Formation** : CartFlows Masterclass Vente (premium - FRM-007)
- **Module** : 3 - Checkout optimise
- **Duree cible** : 6 min (~900 mots)
- **Type** : Video HeyGen + voix ElevenLabs
- **Objectif pedagogique** : Comprendre les deux methodes de pre-remplissage du checkout CartFlows (client connecte et URL parameters), savoir les mettre en place, et les combiner avec FluentCRM pour des campagnes de relance efficaces.

---

## Script narration

**[INTRO - face camera]**

Un client qui revient sur ton site pour acheter un deuxieme produit - c'est le meilleur scenario possible. Il te connait deja, il te fait confiance, il est pret a acheter. Et la, il arrive sur le checkout et il doit re-remplir son nom, son prenom, son email, son adresse. Tout. Depuis zero.

C'est une friction absurde. Ce client t'a deja donne toutes ces infos lors de son premier achat. Lui demander de les retaper, c'est lui mettre des batons dans les roues alors qu'il veut te donner son argent.

CartFlows permet de pre-remplir le checkout automatiquement. Deux methodes. Voyons les deux.

---

**[SECTION 1 - Pre-fill automatique pour les clients connectes]**

**[ECRAN - checkout avec champs deja remplis]**

Premiere methode : le pre-remplissage automatique. Quand un client est connecte a son compte WooCommerce et qu'il arrive sur un checkout CartFlows, ses informations sont automatiquement injectees dans les champs du formulaire.

Nom, prenom, email, adresse, telephone - tout est deja la. Le client n'a plus qu'a verifier, eventuellement modifier une adresse de livraison, et valider son paiement.

Ca fonctionne nativement. CartFlows recupere les donnees du profil WooCommerce du client connecte. Pas de configuration supplementaire - c'est actif par defaut.

La seule condition : le client doit etre connecte. S'il navigue en mode deconnecte, CartFlows ne peut pas savoir qui il est, et le checkout sera vide.

C'est pour ca que c'est important d'encourager la creation de compte lors du premier achat. Dans WooCommerce → Reglages → Comptes, active la creation automatique de compte a la commande. Le client recoit un email avec ses identifiants et, a son prochain achat, il est connecte et son checkout est pre-rempli.

---

**[SECTION 2 - Pre-fill via URL parameters]**

**[ECRAN - URL avec parametres visible dans la barre d'adresse]**

Deuxieme methode : le pre-remplissage via l'URL. Tu ajoutes les informations directement dans le lien qui mene au checkout.

Ca ressemble a ca :

**[ECRAN - URL formatee]**

`tonsite.com/checkout/?billing_first_name=Jean&billing_email=jean@email.com`

Quand le client clique sur ce lien, il arrive sur le checkout avec le prenom "Jean" et l'email "jean@email.com" deja remplis dans les champs correspondants.

Les parametres suivent la convention WooCommerce : `billing_first_name`, `billing_last_name`, `billing_email`, `billing_phone`, `billing_address_1`, `billing_city`, `billing_postcode`. Chaque champ du formulaire a son parametre URL.

L'avantage de cette methode : le client n'a pas besoin d'etre connecte. Tu lui envoies un lien personnalise, il clique, et le checkout est pre-rempli. Ca fonctionne dans un email, un SMS, un message direct.

---

**[SECTION 3 - Cas d'usage : liens personnalises dans FluentCRM]**

**[ECRAN - FluentCRM → editeur d'email avec lien dynamique]**

C'est la que ca devient vraiment puissant. Si tu utilises FluentCRM pour ta gestion de contacts et tes sequences email, tu peux generer des liens de checkout pre-remplis automatiquement.

Dans ton email FluentCRM, tu construis l'URL du checkout avec les merge tags du contact :

**[ECRAN - URL avec merge tags]**

`tonsite.com/checkout/?billing_first_name={{contact.first_name}}&billing_email={{contact.email}}`

FluentCRM remplace automatiquement `{{contact.first_name}}` par le prenom reel du contact et `{{contact.email}}` par son email. Chaque destinataire recoit un lien unique, personnalise avec ses propres infos.

Resultat : le client clique sur le lien dans ton email, arrive sur le checkout, et ses champs sont deja remplis. Il n'a plus qu'a entrer son mode de paiement et valider. Deux actions au lieu de dix.

C'est ideal pour les emails de relance, les offres speciales, les sequences de vente. Tu reduis la friction au minimum absolu.

---

**[SECTION 4 - Limites a connaitre]**

**[ECRAN - face camera]**

Deux limites a garder en tete.

Premiere limite : le pre-fill automatique ne fonctionne que pour les clients connectes. Si ton site ne pousse pas a la creation de compte, la majorite de tes clients reviendront en mode deconnecte et devront tout re-remplir.

Deuxieme limite : les URL parameters sont visibles dans la barre d'adresse. L'email du client est en clair dans l'URL. Ce n'est pas un probleme de securite critique - le client clique sur un lien dans son propre email - mais evite de transmettre des donnees sensibles par ce canal. Nom, prenom, email : OK. Numero de carte : jamais.

Et une precision technique : les URL parameters pre-remplissent les champs visuellement, mais le client peut les modifier. Ce n'est pas un verrouillage, c'est une facilite. Le client garde le controle.

---

**[SECTION 5 - La combinaison gagnante]**

**[ECRAN - schema : abandon de panier → email FluentCRM → lien pre-rempli → checkout]**

Le vrai levier, c'est la combinaison pre-fill plus relance panier abandonne. Voici le scenario.

Un client commence son checkout, remplit l'etape 1 (email + prenom), puis abandonne. CartFlows capture cet abandon. FluentCRM recoit les infos du contact. Une sequence automatique se declenche : un email part 30 minutes plus tard avec un lien vers le checkout, pre-rempli avec les infos que le client a deja saisies.

Le client recoit l'email, clique, arrive sur un checkout ou tout est deja rempli. Il n'a plus qu'a payer. La friction est a zero.

C'est exactement pour ca qu'on a configure le multi-step checkout dans la lecon precedente : l'etape 1 capture l'email, et meme en cas d'abandon, tu as ce qu'il faut pour relancer.

---

**[OUTRO - face camera]**

Pre-remplir le checkout, c'est supprimer la friction pour les clients qui sont deja convaincus. Combine le pre-fill automatique pour les clients connectes avec les URL parameters pour tes campagnes email, et tu transformes ton checkout en une experience ou il ne reste qu'une seule action : payer.

Le module 3 est termine. Tu as un checkout optimise - Takeover configure, multi-step en place, custom fields au minimum necessaire, et pre-fill actif. Dans le prochain module, on passe aux order bumps et aux upsells - comment augmenter la valeur de chaque commande.

---

## Notes de production

- **Captures d'ecran necessaires** : checkout pre-rempli (client connecte), URL avec parametres dans la barre d'adresse, FluentCRM editeur email avec merge tags, WooCommerce reglages comptes
- **Schema** : flow abandon panier → email FluentCRM → lien pre-rempli → checkout → conversion
- **Timing** : intro (1 min) → pre-fill automatique (1.5 min) → URL parameters (1.5 min) → FluentCRM (1 min) → limites (0.5 min) → combinaison (0.5 min) → outro (0.5 min)
- **Ton** : pratique, focus sur l'elimination de friction, pont explicite avec FluentCRM (stack schoolsWP)
