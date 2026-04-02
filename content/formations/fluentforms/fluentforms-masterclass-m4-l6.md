# Script video — Module 4, Lecon 6 : Coupons de reduction

**Formation** : FluentForms Masterclass Formulaires
**Code** : FRM-012 (premium)
**Module** : 4 — Paiements
**Lecon** : 6/7 — Coupons de reduction
**Duree** : 6 min (~900 mots)
**Type** : Video HeyGen + voix ElevenLabs
**Ecran** : Face camera intro/outro, screencast creation coupons + formulaire, slide strategie
**Objectif** : Creer et configurer des codes promo avec limites d'utilisation et dates d'expiration

---

**[INTRO — face camera]**

Les codes promo, ca marche. Un visiteur hesite, tu lui envoies un code de reduction par email, il revient et il achete. Simple, efficace. FluentForms Pro integre un systeme de coupons directement dans les formulaires de paiement.

On va creer des coupons, les configurer, et les connecter a FluentCRM pour les distribuer automatiquement.

**[SECTION 1 — screencast "Creer un coupon"]**

Direction FluentForms, Settings, Payment Settings, onglet Coupons.

Clique sur "Add Coupon". Tu as plusieurs parametres a configurer.

Coupon Code : c'est le code que le client va taper. Choisis quelque chose de memorable. "WELCOME20" pour 20% de reduction. "EARLYBIRD" pour les premiers inscrits.

Discount Type : deux options. Percentage — un pourcentage de reduction. Ou Fixed Amount — un montant fixe en euros.

Pour "WELCOME20", choisis Percentage et entre 20.

Discount Amount : 20 (pour 20%).

**[SECTION 2 — screencast "Limites et expiration"]**

Maintenant les garde-fous. Sans limites, un coupon peut devenir un probleme.

Usage Limit : le nombre total d'utilisations. Si tu veux que le coupon fonctionne pour les 100 premiers clients, entre 100. Apres 100 utilisations, le code ne marche plus.

Start Date et Expiry Date : la periode de validite. Tu peux creer un coupon valable uniquement pendant le Black Friday, ou pendant une semaine de lancement.

Minimum Purchase Amount : le montant minimum de commande pour que le coupon s'applique. Utile si tu ne veux pas qu'un coupon de 10 euros s'applique sur un produit a 15 euros.

Stackable : est-ce que le client peut utiliser plusieurs coupons sur la meme commande ? En general, non. Desactive cette option.

**[SECTION 3 — screencast "Ajouter le champ coupon au formulaire"]**

Retour dans ton formulaire de paiement. Dans Payment Fields, ajoute un champ Coupon.

C'est un champ texte avec un bouton "Apply". Le client tape son code, clique sur Apply, et la reduction s'applique en temps reel. Le Payment Summary se met a jour avec le prix reduit.

Si le code est invalide ou expire, un message d'erreur s'affiche. "Ce coupon n'est pas valide" ou "Ce coupon a expire".

Place le champ Coupon juste avant le Payment Summary. L'ordre logique : options de paiement, coupon, recapitulatif, carte bancaire, bouton.

**[SECTION 4 — slide "Strategie coupons + FluentCRM"]**

Voici comment combiner coupons et FluentCRM pour automatiser la distribution.

Scenario 1 : email de bienvenue. Un nouveau contact s'inscrit a ta newsletter. FluentCRM envoie un email automatique avec le code "WELCOME20". Le contact revient sur ton formulaire de vente, tape le code, et obtient 20% de reduction.

Scenario 2 : relance panier abandonne. Un visiteur a commence un formulaire de paiement mais ne l'a pas termine (partial entries — on verra ca au module 6). Tu envoies un email via FluentCRM avec un code "COMEBACK10" valable 48h.

Scenario 3 : offre de fidelite. Un client a deja achete. FluentCRM lui envoie un code anniversaire ou un code de reduction pour un deuxieme achat.

A chaque fois, le meme principe : FluentCRM distribue le code par email, FluentForms le valide au moment du paiement.

**[SECTION 5 — screencast "Tester le coupon"]**

On teste. Ouvre ton formulaire de paiement en preview. Selectionne un produit. Tape "WELCOME20" dans le champ coupon. Clique Apply.

Le Payment Summary doit afficher : prix original, reduction, et prix final. Si le produit coute 100 euros, tu vois 100 euros, -20 euros, total 80 euros.

Teste aussi un code invalide. Tape "NIMPORTEQUOI". Le message d'erreur doit apparaitre.

Teste un code expire. Cree un coupon avec une date d'expiration dans le passe et essaie de l'utiliser.

**[OUTRO — face camera]**

Les coupons sont en place. Tu as un levier de conversion supplementaire. Dans la prochaine lecon — la derniere du module — on assemble tout dans un cas pratique complet : un formulaire de reservation avec paiement, options, coupon et confirmation.

On se retrouve dans la lecon suivante.

---

**Points cles** :
- Coupons : pourcentage ou montant fixe
- Limites : nombre d'utilisations, dates de validite, montant minimum
- Champ Coupon dans le formulaire : le client tape le code, la reduction s'applique en temps reel
- FluentCRM pour distribuer les codes automatiquement (bienvenue, relance, fidelite)
- Toujours tester les coupons valides, invalides et expires

**Mots cles SEO** : FluentForms coupon, code promo formulaire WordPress, reduction FluentForms, coupon Stripe WordPress

---

**Notes de production** :
- Face camera : intro (pitch codes promo) + outro (transition cas pratique)
- Screencast : creation coupon + ajout champ + test (~4 min)
- Slide : 1 slide strategie coupons + FluentCRM
- Ton : oriente conversion — montrer l'impact business des coupons
