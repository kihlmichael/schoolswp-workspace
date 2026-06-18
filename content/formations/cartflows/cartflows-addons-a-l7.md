# Lecon A.7 - Champ coupon integre au side cart

## Metadata

- **Formation** : CartFlows Add-ons (premium - FRM-008)
- **Module** : A - Modern Cart
- **Duree cible** : 6 min (~900 mots)
- **Type** : Video HeyGen + voix ElevenLabs
- **Objectif pedagogique** : Activer et configurer le champ coupon dans le side cart pour permettre aux clients d'appliquer leurs codes promo sans quitter la page.

---

## Script narration

**[INTRO - face camera]**

Tu connais le scenario : un client a un code promo. Il a des produits dans son panier. Il cherche ou entrer son code. Il ne trouve pas. Il va au checkout, il ne voit pas le champ coupon tout de suite. Il se dit "tant pis" et quitte le site. Ou pire : il ouvre un nouvel onglet, cherche "code promo [ta boutique]" sur Google, tombe sur un concurrent, et tu perds la vente.

Le champ coupon dans le side cart elimine ce probleme. Le client tape son code directement dans le panneau lateral, la remise s'applique instantanement, et il passe commande.

---

**[SECTION 1 - Activer le champ coupon]**

**[ECRAN - Modern Cart Pro → Settings → Coupon]**

L'activation prend 10 secondes. Va dans Modern Cart → Settings → Coupon Field (ou Enable Coupon selon la version).

**Enable Coupon Field** : active.

Le champ apparait dans le side cart, generalement entre la liste de produits et le total. C'est un champ texte simple avec un bouton "Appliquer".

Pas besoin de configuration supplementaire pour le champ lui-meme. Les coupons qu'il accepte sont ceux que tu as crees dans WooCommerce → Marketing → Coupons. Modern Cart utilise la meme logique de validation - il ne cree pas un systeme de coupons parallele.

---

**[SECTION 2 - L'experience client]**

**[ECRAN - demonstration : saisie coupon dans le side cart]**

Voyons ce que le client voit.

Il a des produits dans son side cart. En dessous de la liste, il voit un champ "Code promo" avec un bouton "Appliquer". Il tape son code - par exemple "BIENVENUE10" - et clique sur Appliquer.

Deux cas possibles.

**Code valide.** La remise s'applique immediatement. Le side cart se met a jour :
- Le prix original est barre
- Le nouveau prix apres remise s'affiche
- Le montant de la remise est visible (par exemple "-10%" ou "-5,00 euros")
- Le total en bas du side cart se recalcule

Tout ca sans quitter la page, sans aller au checkout, sans recharger quoi que ce soit. Le client voit instantanement l'impact de son coupon.

**Code invalide.** Un message d'erreur s'affiche dans le side cart - "Code promo invalide" ou "Ce coupon a expire". Le client comprend immediatement et peut reessayer avec un autre code ou continuer sans remise.

---

**[SECTION 3 - Pourquoi ca reduit les abandons]**

**[ECRAN - slide "parcours client avec vs sans champ coupon"]**

Comparons les deux parcours.

**Sans champ coupon dans le side cart.** Le client a un code promo. Il ajoute ses produits. Il ouvre le side cart - pas de champ coupon. Il doit aller au checkout pour l'appliquer. Il clique sur "Passer commande", arrive sur le checkout CartFlows, cherche le champ coupon. Si le champ est replie ou peu visible, il galere. Chaque seconde de recherche augmente le risque d'abandon.

**Avec champ coupon dans le side cart.** Le client ajoute ses produits. Il ouvre le side cart. Il voit le champ coupon. Il entre son code. La remise s'affiche. Il clique sur "Passer commande" avec confiance - il sait deja que son code fonctionne et combien il va payer.

La difference, c'est la friction et l'incertitude. Le client qui ne sait pas si son coupon va fonctionner est un client qui hesite. Celui qui voit sa remise appliquee est un client confiant.

---

**[SECTION 4 - Conseils de configuration]**

**[ECRAN - slide bonnes pratiques coupons]**

Quelques points importants pour tirer le maximum du champ coupon.

**Texte du placeholder.** Le texte affiche dans le champ vide ("Entrer un code promo", "Code de reduction"). Rends-le explicite. Si tes clients francais ne connaissent pas le terme "coupon", utilise "Code promo" ou "Code de reduction".

**Position dans le side cart.** Par defaut, le champ est entre les produits et le total. C'est l'emplacement logique : le client voit ses produits, entre son code, et le total se met a jour. Ne deplace pas le champ au-dessus des produits - le client veut d'abord voir ce qu'il achete avant de penser au coupon.

**Ne masque pas le champ.** Certains marchands hesitent a afficher un champ coupon visible - ils ont peur que les clients sans code promo se sentent leses ou aillent chercher un code en ligne. C'est un faux probleme. Un client qui a un code et ne peut pas l'utiliser facilement, c'est une vente perdue certaine. Un client sans code qui voit le champ, il l'ignore et passe commande.

**Coupons WooCommerce a configurer.** Assure-toi que tes coupons WooCommerce sont correctement parametres : date d'expiration, montant minimum de commande, nombre d'utilisations maximum. Modern Cart applique les memes regles de validation que le checkout.

---

**[SECTION 5 - Combinaison avec la barre de livraison gratuite]**

**[ECRAN - side cart avec barre + coupon + total]**

Un detail strategique : si le client applique un coupon qui reduit le total en dessous du seuil de livraison gratuite, la barre de progression se met a jour. Par exemple, le client est a 52 euros (livraison gratuite a 49 euros). Il applique un coupon de -10%. Son total passe a 46,80 euros. La barre repasse sous les 100% : "Plus que 2,20 euros pour la livraison gratuite !"

C'est un mecanisme puissant. Le client qui applique un coupon et perd la livraison gratuite va souvent ajouter un petit produit pour repasser au-dessus du seuil. Le coupon l'a fait economiser, mais la barre le pousse a depenser un peu plus. Les deux fonctionnalites se renforcent mutuellement.

---

**[CONCLUSION - face camera]**

Le champ coupon dans le side cart, c'est une fonctionnalite simple qui enleve un point de friction majeur. Le client entre son code, voit sa remise, et passe commande en confiance.

Prochaine et derniere lecon du module : comment Modern Cart et CartFlows fonctionnent ensemble pour creer le parcours d'achat complet.

---

## Notes de production

- **Visuels** : activation du champ coupon dans les settings, demo saisie code valide (prix barre + remise), demo code invalide (message erreur), interaction barre livraison + coupon
- **Animation** : montrer le recalcul instantane du total apres application du coupon
- **Prerequis** : Modern Cart Pro actif, au moins un coupon WooCommerce cree pour la demo
- **Transition** : enchaine sur LA.8 (Modern Cart + CartFlows ensemble)
