# Lecon 3.5 — Checkout pour produits physiques vs digitaux vs formations

## Metadata

- **Formation** : CartFlows Masterclass Vente (premium — FRM-007)
- **Module** : 3 — Checkout optimise
- **Duree cible** : 10 min (~1400 mots)
- **Type** : Video HeyGen + voix ElevenLabs
- **Objectif pedagogique** : Savoir configurer un checkout CartFlows adapte au type de produit vendu — physique, digital ou formation. Comprendre quels champs activer ou desactiver, et configurer la bonne redirection apres achat.

---

## Script narration

**[INTRO — face camera]**

Un checkout, ca ne se configure pas de la meme maniere selon ce que tu vends. Si tu vends un t-shirt, tu as besoin de l'adresse de livraison. Si tu vends un ebook, cette adresse ne sert strictement a rien — elle alourdit ton formulaire et fait baisser ta conversion.

CartFlows te permet de personnaliser chaque step de ton funnel. Et c'est exactement ce qu'on va faire dans cette lecon : configurer trois checkouts differents pour trois types de produits — physique, digital, et formation en ligne avec TutorLMS.

---

**[SECTION 1 — Chaque type de produit a ses propres besoins]**

**[ECRAN — tableau comparatif : 3 colonnes (physique / digital / formation) avec les champs requis]**

Avant de toucher a CartFlows, il faut poser les bases. Les besoins checkout changent completement selon la nature du produit.

Pour un produit physique — un livre imprime, du materiel, un accessoire — tu as besoin du nom complet, de l'adresse de livraison, du choix du transporteur, et eventuellement d'un numero de telephone. Le client s'attend a ces champs. Si tu les retires, il va se demander comment il va recevoir sa commande.

Pour un produit digital — un ebook, un template Kadence, un plugin premium — tu n'as besoin que de l'email et du prenom. C'est tout. Pas d'adresse, pas de telephone, pas de champ societe. Le client paie, et il recoit son acces immediatement par email ou sur une page de telechargement.

Pour une formation en ligne via TutorLMS, c'est encore different. Tu as besoin de l'email et du prenom pour creer le compte utilisateur WordPress. Le reste est gere automatiquement : le compte est cree au moment du paiement, et le client est redirige vers son espace membre.

Trois types, trois configurations. Et trois flows CartFlows differents.

---

**[SECTION 2 — Checkout produit physique : tous les champs actifs]**

**[ECRAN — CartFlows checkout step → onglet "Checkout Fields"]**

On commence par le cas le plus complet : le produit physique.

Dans CartFlows, ouvre ton checkout step et va dans l'onglet "Checkout Fields". Par defaut, WooCommerce affiche tous les champs billing et shipping. Pour un produit physique, c'est exactement ce qu'on veut.

Verifie que ces champs sont actifs et marques comme obligatoires : prenom, nom, email, adresse ligne 1, ville, code postal, pays. Ajoute le champ telephone si ton transporteur en a besoin pour la livraison.

Pour les frais de livraison, c'est WooCommerce qui gere. Configure tes zones de livraison dans WooCommerce → Reglages → Expedition. CartFlows affichera automatiquement les options de livraison dans le checkout — colissimo, chronopost, retrait en point relais, ce que tu as configure.

L'estimation du delai de livraison, tu l'ajoutes en texte juste en dessous du choix de transporteur. Un simple bloc texte dans ton checkout step : "Livraison estimee sous 3-5 jours ouvrables." Ca rassure le client au moment critique de la decision.

---

**[SECTION 3 — Checkout produit digital : le minimum absolu]**

**[ECRAN — CartFlows checkout step avec champs desactives un par un]**

Maintenant, le produit digital. Et la, tu vas faire l'inverse : retirer tout ce qui est inutile.

Dans CartFlows → Checkout Fields, desactive les champs suivants : nom de famille (optionnel au mieux), adresse, ville, code postal, pays, telephone, et surtout toute la section shipping. Un produit digital n'a pas d'adresse de livraison — desactiver cette section est la premiere chose a faire.

Ce que tu gardes : prenom et email. C'est tout. Deux champs. Ton checkout tient sur un ecran sans scroller. Le client voit le recapitulatif du produit, entre son prenom, son email, entre ses informations de paiement, et c'est termine.

L'impact sur la conversion est direct. Chaque champ supplementaire dans un formulaire fait baisser le taux de conversion de 5 a 10%. En passant de 8 champs a 2, tu peux doubler ta conversion sur un produit digital.

Pour l'acces au produit apres paiement, tu as deux options. Soit tu rediriges vers une page de telechargement — une thank you page CartFlows avec le lien de download. Soit tu envoies un email automatique avec le lien — WooCommerce le fait nativement pour les produits "telechargeable".

---

**[SECTION 4 — Checkout formation TutorLMS : creation de compte automatique]**

**[ECRAN — CartFlows checkout step + WooCommerce → TutorLMS integration settings]**

Le checkout formation avec TutorLMS a une particularite : il doit creer un compte utilisateur WordPress au moment de l'achat. Sans compte, pas d'acces a l'espace membre.

Dans CartFlows, les champs que tu gardes : prenom, email. L'email sert a la fois de login et de contact. Le mot de passe est genere automatiquement par WordPress et envoye par email au client — pas besoin d'un champ mot de passe dans le checkout.

Pour que ca fonctionne, verifie deux reglages. Dans WooCommerce → Reglages → Comptes et confidentialite, active "Autoriser la creation de compte pendant le paiement" et "Generer automatiquement un mot de passe pour le compte". Ces deux options doivent etre cochees.

Cote TutorLMS, l'integration avec WooCommerce fait le reste. Quand le client achete le produit lie au cours TutorLMS, l'inscription au cours est automatique. Le client paie, le compte est cree, et l'acces au cours est attribue — tout ca en une seule transaction.

La redirection apres achat, c'est le dashboard TutorLMS. Dans ton flow CartFlows, configure la thank you page pour rediriger vers l'URL de l'espace membre — generalement `/dashboard/` ou `/tableau-de-bord/` selon ta configuration. Le client paie et se retrouve directement dans son espace de formation.

---

**[SECTION 5 — Configuration dans CartFlows : un flow par type]**

**[ECRAN — CartFlows → Flows avec 3 flows distincts nommes]**

Dans CartFlows, chaque type de produit devrait avoir son propre flow. Ne melange pas un checkout physique et un checkout digital dans le meme funnel.

Cree trois flows : "Vente produit physique", "Vente produit digital", "Vente formation". Chacun avec son propre checkout step configure comme on vient de le voir.

Pour activer ou desactiver les champs, tu vas dans chaque checkout step → onglet "Checkout Fields". Tu vois la liste de tous les champs billing et shipping. Chaque champ a un toggle on/off et un reglage "required" ou "optional".

Pour le checkout digital : billing_first_name (on, required), billing_email (on, required), tout le reste off. Pour le checkout physique : tout on. Pour la formation : prenom et email on, le reste off, avec la creation de compte activee cote WooCommerce.

---

**[SECTION 6 — Redirections apres achat selon le type]**

**[ECRAN — CartFlows thank you step → redirection settings]**

La page qui s'affiche apres le paiement est aussi importante que le checkout lui-meme. C'est le moment ou tu confirmes au client que tout s'est bien passe et ou tu le guides vers l'etape suivante.

Pour un produit physique : thank you page classique avec le recapitulatif de commande, le numero de suivi (quand disponible), et un message "Ta commande est en cours de preparation."

Pour un produit digital : page de telechargement avec le lien direct. Pas besoin d'attendre un email — le client clique et telecharge immediatement. Ajoute un message "Tu as aussi recu le lien par email, au cas ou."

Pour une formation : redirection automatique vers le dashboard TutorLMS. Le client se retrouve dans son espace, voit le cours, et peut commencer immediatement. C'est la meilleure experience possible — zero friction entre le paiement et la premiere lecon.

---

**[CONCLUSION — face camera]**

Retiens cette regle : cree un flow different par type de produit. Ne melange pas un checkout physique et digital dans le meme funnel. Le checkout physique a besoin de tous les champs. Le checkout digital ne demande que l'email et le prenom. Le checkout formation cree un compte automatiquement.

Moins de champs, plus de conversions. C'est aussi simple que ca.

Dans la prochaine lecon, on voit comment gerer les variations produit directement dans le checkout CartFlows — tailles, plans, options.

---

## Notes de production

- **Visuels requis** : tableau comparatif 3 colonnes (physique/digital/formation), captures CartFlows Checkout Fields avec toggles on/off, capture WooCommerce reglages comptes, schema redirection par type
- **Captures d'ecran** : CartFlows checkout step editor, WooCommerce → Reglages → Comptes et confidentialite, CartFlows thank you step settings, TutorLMS dashboard
- **Points d'insistance voix** : "Deux champs. C'est tout." (section 3), "Cree un flow different par type de produit" (conclusion)
- **Transitions** : enchainer les 3 types comme une progression logique — du plus complexe (physique) au plus simple (digital), puis le cas special (formation)
