# Lecon 3.3 — Custom fields : collecter les bonnes informations

## Metadata

- **Formation** : CartFlows Masterclass Vente (premium — FRM-007)
- **Module** : 3 — Checkout optimise
- **Duree cible** : 8 min (~1100 mots)
- **Type** : Video HeyGen + voix ElevenLabs
- **Objectif pedagogique** : Savoir ajouter des champs personnalises au checkout CartFlows, choisir le bon type de champ selon le besoin, retrouver les donnees collectees dans WooCommerce, et appliquer des regles conditionnelles.

---

## Script narration

**[INTRO — face camera]**

Le checkout standard collecte les infos de base : nom, adresse, email, paiement. C'est suffisant pour traiter une commande. Mais parfois, tu as besoin de plus.

Tu vends des t-shirts personnalises ? Il te faut la taille. Tu proposes un coffret cadeau ? Il te faut le message de dedication. Tu livres des produits frais ? Il te faut la date de livraison souhaitee.

Les custom fields de CartFlows te permettent d'ajouter exactement les champs dont tu as besoin, a l'endroit ou tu veux dans le checkout. Sans toucher au code. Mais attention — chaque champ supplementaire a un cout sur ta conversion. Voyons comment trouver le bon equilibre.

---

**[SECTION 1 — Pourquoi ajouter des champs personnalises]**

**[ECRAN — face camera]**

Trois raisons legitimes d'ajouter un custom field.

Premiere raison : la personnalisation produit. Le client a besoin de te transmettre une information pour que tu puisses preparer sa commande — taille, couleur, gravure, message personnalise.

Deuxieme raison : les contraintes logistiques. Tu as besoin d'une info de livraison specifique — code d'acces a l'immeuble, creneau horaire prefere, date souhaitee.

Troisieme raison : la segmentation. Tu veux collecter une info marketing qui t'aidera a mieux servir le client ensuite — comment il t'a connu, son niveau d'experience, son secteur d'activite.

Si ton champ ne rentre dans aucune de ces trois categories, pose-toi la question : est-ce que j'en ai vraiment besoin ? La reponse est probablement non.

---

**[SECTION 2 — Ajouter un champ dans CartFlows]**

**[ECRAN — CartFlows → Step Checkout → Custom Fields]**

Ouvre ton flow, clique sur l'etape Checkout, et va dans la section "Custom Fields" ou "Checkout Fields" selon ta version de CartFlows.

**[ECRAN — interface d'ajout de champ]**

Tu vas voir la liste des champs existants — ceux de WooCommerce par defaut. En bas, tu as un bouton "Add New Custom Field". Clique dessus.

CartFlows te demande plusieurs informations. Le label — c'est le texte que le client verra. Le placeholder — le texte grise dans le champ vide. Le type de champ. Et si le champ est obligatoire ou optionnel.

Pour la position, tu choisis ou le champ apparait dans le formulaire — apres l'email, apres l'adresse, avant le bouton de paiement. Tu peux le placer exactement ou ca a du sens dans le parcours.

---

**[SECTION 3 — Les types de champs disponibles]**

**[ECRAN — liste des types avec exemples visuels]**

CartFlows propose plusieurs types de champs. Chacun correspond a un usage precis.

**Texte** : une ligne de saisie libre. Ideal pour un prenom, un code promo specifique, un numero de reference. Exemple : "Message a graver sur le bijou".

**Textarea** : une zone de texte multiligne. Pour les messages longs — un mot de dedication, des instructions de livraison detaillees, une demande speciale.

**Select** : un menu deroulant avec des options predefinies. Parfait pour les choix limites — taille de t-shirt (S, M, L, XL), creneau de livraison (matin, apres-midi), formule choisie (standard, premium).

**Checkbox** : une case a cocher. Utile pour les options binaires — "Ajouter un emballage cadeau", "J'accepte les conditions de vente specifiques", "Je souhaite recevoir la newsletter".

**Date** : un selecteur de date. Pour les livraisons planifiees, les reservations, les rendez-vous. Le client choisit une date dans un calendrier visuel.

Le choix du type est important. Ne mets pas un champ texte libre la ou un select suffit. Un menu deroulant avec 4 options, c'est un clic. Un champ texte ou le client doit taper "taille L", c'est une source d'erreurs et de friction.

---

**[SECTION 4 — Exemples concrets]**

**[ECRAN — trois exemples de checkouts avec custom fields]**

Voyons trois configurations reelles.

**Exemple 1 — Boutique de t-shirts personnalises.** Deux champs ajoutes : un select "Taille" (S, M, L, XL, XXL) place juste apres le recapitulatif produit, et un texte "Texte a imprimer" place en dessous. Le premier est obligatoire, le second optionnel.

**Exemple 2 — Coffret cadeau.** Un textarea "Message de dedication" place avant le paiement. Optionnel. Et une checkbox "Emballage cadeau (+5 euros)" qui ajoute un frais supplementaire a la commande.

**Exemple 3 — Livraison de produits frais.** Un select "Creneau de livraison" (matin 8h-12h, apres-midi 14h-18h) obligatoire. Et un date picker "Date de livraison souhaitee" avec un minimum de J+2 pour laisser le temps de preparation.

---

**[SECTION 5 — Retrouver les donnees]**

**[ECRAN — WooCommerce → Commandes → detail d'une commande]**

Les donnees des custom fields ne disparaissent pas dans un trou noir. Tu les retrouves a deux endroits.

Premier endroit : dans le detail de la commande WooCommerce. Va dans WooCommerce, Commandes, ouvre une commande. Les custom fields apparaissent dans la section "Custom Fields" ou "Order Meta" — selon ta configuration.

Deuxieme endroit : dans l'email de confirmation. WooCommerce inclut automatiquement les custom fields dans l'email envoye au client et dans ta notification admin. Le client voit "Taille : L" et "Message : Joyeux anniversaire" dans son recapitulatif. Toi aussi.

Si tu utilises un CRM comme FluentCRM, tu peux aussi mapper ces champs pour segmenter tes contacts automatiquement.

---

**[SECTION 6 — Regles conditionnelles]**

**[ECRAN — CartFlows → regles conditionnelles sur un champ]**

CartFlows Pro permet d'afficher un champ seulement sous certaines conditions. Par exemple : afficher le champ "Taille" uniquement si le produit dans le panier est un t-shirt. Ou afficher le champ "Message de dedication" uniquement si la checkbox "Emballage cadeau" est cochee.

Ca evite d'afficher des champs inutiles qui n'ont rien a voir avec la commande en cours. Moins de champs visibles, moins de friction, meilleure conversion.

La configuration se fait dans les settings du custom field — section "Conditional Logic". Tu choisis la condition (produit dans le panier, valeur d'un autre champ, montant du panier) et l'action (afficher ou masquer le champ).

---

**[SECTION 7 — Le conseil qui compte]**

**[ECRAN — face camera]**

Chaque champ que tu ajoutes a ton checkout reduit ta conversion. C'est mesure, c'est documente, c'est une realite. Chaque champ supplementaire ajoute une friction, un effort, une raison de plus pour le client de se dire "je ferai ca plus tard" — et "plus tard" ne vient jamais.

Alors avant d'ajouter un champ, pose-toi la question : est-ce que cette information est strictement necessaire pour traiter cette commande ? Si la reponse est non, ne l'ajoute pas. Tu pourras toujours la collecter apres l'achat — par email, par un formulaire de suivi, dans l'espace client.

N'ajoute que ce qui est indispensable. Tout le reste peut attendre.

---

**[OUTRO — face camera]**

Les custom fields sont un outil precis. Utilise-les quand tu en as reellement besoin, avec le bon type de champ, au bon endroit dans le checkout. Et surtout, n'en abuse pas.

Dans la prochaine lecon, on va voir comment pre-remplir le checkout pour les clients qui reviennent — pour supprimer completement la friction du formulaire.

---

## Notes de production

- **Captures d'ecran necessaires** : interface Custom Fields CartFlows, ajout d'un champ, types de champs (texte, select, checkbox, date), detail commande WooCommerce avec custom fields, email de confirmation, regles conditionnelles
- **Schemas** : trois exemples de checkout (t-shirts, coffret cadeau, livraison frais)
- **Timing** : intro (1 min) → pourquoi (1 min) → ajout champ (1.5 min) → types de champs (1.5 min) → exemples (1 min) → donnees (0.5 min) → conditionnel (1 min) → conseil + outro (0.5 min)
- **Ton** : pragmatique, insistance sur le cout conversion de chaque champ ajoute — message cle : le moins possible
