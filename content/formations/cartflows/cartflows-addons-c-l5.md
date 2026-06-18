# Lecon C.5 - BOGO : Buy One Get One

## Metadata

- **Formation** : CartFlows Add-ons (premium - FRM-008)
- **Module** : C - Power Coupons
- **Duree cible** : 8 min (~1100 mots)
- **Type** : Video HeyGen + voix ElevenLabs
- **Objectif pedagogique** : Configurer une promotion BOGO avec Power Coupons, comprendre les variantes (Buy X Get X, Buy X Get Y) et pourquoi le BOGO augmente le volume sans degrader le prix unitaire percu.

---

## Script narration

**[INTRO - face camera]**

Le BOGO - Buy One Get One - c'est la promotion la plus puissante en e-commerce. Le client achete un produit et en recoit un deuxieme gratuit ou a prix reduit.

Pourquoi c'est si efficace ? Parce que le client percoit un cadeau, pas une remise. "-50%" et "le 2eme offert" ont le meme impact economique, mais l'effet psychologique est completement different. Le cadeau genere une emotion positive. La remise est juste un calcul.

Power Coupons te permet de configurer des BOGO automatiques. On va voir comment.

---

**[SECTION 1 - Les variantes du BOGO]**

**[ECRAN - slide 3 variantes BOGO]**

Le BOGO n'est pas un seul mecanisme. Il en existe plusieurs variantes.

Buy X Get X. Le client achete le produit A et recoit un deuxieme exemplaire du meme produit gratuitement. Exemple : achete 1 t-shirt, recois le meme t-shirt en cadeau. C'est le BOGO classique.

Buy X Get Y. Le client achete le produit A et recoit le produit B gratuitement. Exemple : achete un shampoing, recois un apres-shampoing offert. Tu vides un stock ou tu fais decouvrir un produit complementaire.

Buy X Get X at discount. Le client achete le produit A et recoit un deuxieme exemplaire a prix reduit - pas gratuit. Exemple : achete 1 sachet de cafe, le 2eme a -50%. Tu limites le cout de la promo tout en gardant l'effet incitatif.

Tu peux aussi faire "Buy 2 Get 1" : achete 2 unites, la 3eme est offerte. Ou "Buy 3 Get 1 at -50%". Les combinaisons sont flexibles.

---

**[SECTION 2 - Configurer un BOGO dans Power Coupons]**

**[ECRAN - WordPress admin → Coupons → Ajouter → onglet Power Coupons → BOGO]**

On va creer un BOGO concret. L'objectif : "Achete 2 t-shirts, le 3eme est offert."

Cree un nouveau coupon. Donne-lui un nom interne : "bogo-3eme-tshirt-offert".

Dans "Type de remise", laisse "Remise en pourcentage" - Power Coupons va gerer la logique BOGO separement.

Va dans l'onglet Power Coupons. Active "Enable Auto Apply" - le BOGO doit etre automatique sinon ca perd tout son interet.

Ensuite, dans la section BOGO Rules, clique sur "Add BOGO Rule".

Produit declencheur : selectionne la categorie "T-shirts" ou les produits specifiques. Quantite declencheur : 2. C'est le seuil d'achat.

Produit offert : meme categorie "T-shirts" (Buy X Get X) ou un produit different si tu fais un Buy X Get Y. Quantite offerte : 1.

Type de remise sur le produit offert : "100%" (gratuit) ou "50%" (a moitie prix) ou un montant fixe.

Publie le coupon.

---

**[SECTION 3 - Comportement cote client]**

**[ECRAN - front-end boutique, ajout au panier]**

Teste l'experience. Ouvre ta boutique en navigation privee.

Le client ajoute 2 t-shirts au panier. Quand il ajoute le deuxieme, Power Coupons detecte que le seuil est atteint. Le produit offert - le 3eme t-shirt - s'ajoute automatiquement au panier avec un prix barre et la mention "Offert" ou "BOGO".

Le client n'a rien fait. Il n'a pas tape de code. Il n'a pas cherche de promo. Le cadeau est apparu tout seul dans son panier.

C'est la que l'auto-application et le BOGO se combinent. Sans auto-application, le client devrait taper un code pour activer le BOGO. Avec, tout est fluide.

Si le client retire un des deux t-shirts declencheurs, le produit offert disparait automatiquement du panier. La logique est coherente.

---

**[SECTION 4 - Strategies BOGO qui fonctionnent]**

**[ECRAN - slide 3 strategies]**

Strategie 1 : ecoulement de stock. Tu as un produit qui ne se vend pas bien ? Fais-en le produit offert d'un BOGO. Le client achete un best-seller et recoit le produit a ecouler en cadeau. Tu vides le stock sans faire de soldes.

Strategie 2 : decouverte produit. Tu lances un nouveau produit ? Offre-le en BOGO avec un produit populaire. Le client decouvre le nouveau produit sans risque. S'il l'apprecie, il l'achetera seul la prochaine fois.

Strategie 3 : augmentation du volume. "Achete 2, le 3eme offert" pousse le client a acheter une unite de plus que prevu. Il etait venu pour un t-shirt. Il en achete trois. Ton volume de vente augmente, et le prix unitaire percu ne baisse pas - le client a l'impression d'avoir recu un cadeau, pas d'avoir achete du discount.

Le BOGO est la promo la plus puissante en e-commerce. Elle augmente le volume sans baisser le prix unitaire percu. Le client pense "j'ai eu un cadeau", pas "j'ai achete du pas cher".

---

**[SECTION 5 - Points d'attention]**

**[ECRAN - slide conseils]**

Attention a la marge. Un BOGO "le 3eme offert" sur un produit a faible marge peut te couter cher. Calcule toujours le cout reel de la promo avant de la lancer.

Attention a l'abus. Mets une limite d'utilisation par client si necessaire. Un client qui passe 10 commandes pour profiter du BOGO a repetition, ca n'est pas l'objectif.

Attention a la clarte. Le client doit comprendre l'offre immediatement. "Achete 2, le 3eme offert" est clair. "Buy 1.5X Get 0.7Y at -33.5%" est incomprehensible. Reste simple.

---

**[CONCLUSION - face camera]**

Tu as ton premier BOGO automatique. Le produit offert s'ajoute tout seul au panier, sans code, sans friction. C'est la promo qui genere le plus de satisfaction client.

Dans la prochaine lecon, on va configurer la livraison gratuite conditionnelle - et voir comment elle se combine avec la barre de progression de Modern Cart.

---

## Notes de production

- **Visuels** : slide 3 variantes BOGO, captures configuration BOGO Rules dans Power Coupons, demo front-end ajout produit offert automatique, slide 3 strategies
- **Donnees** : psychologie du cadeau vs remise (perception client), impact BOGO sur volume de vente
- **Transition** : enchaine sur LC.6 (livraison gratuite conditionnelle)
