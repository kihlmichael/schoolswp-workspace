# Lecon A.6 — Recommandations in-cart : upsells dans le panier

## Metadata

- **Formation** : CartFlows Add-ons (premium — FRM-008)
- **Module** : A — Modern Cart
- **Duree cible** : 10 min (~1300 mots)
- **Type** : Video HeyGen + voix ElevenLabs
- **Objectif pedagogique** : Configurer les recommandations de produits dans le side cart (upsells et cross-sells) pour augmenter le nombre d'articles par commande.

---

## Script narration

**[INTRO — face camera]**

Le client a ouvert le side cart. Il voit ses produits. Et juste en dessous, il voit d'autres produits qui pourraient l'interesser. Pas une page de pub, pas un popup — des suggestions discretes, pertinentes, au bon moment.

C'est ce que font les recommandations in-cart de Modern Cart Pro. Et c'est un des moyens les plus naturels d'augmenter le panier moyen sans aucune pression commerciale.

---

**[SECTION 1 — Upsell vs cross-sell : la difference]**

**[ECRAN — slide definitions upsell / cross-sell]**

Avant de configurer, clarifions les termes.

**Upsell** : tu proposes un produit superieur a celui que le client a dans son panier. Il a choisi le t-shirt basique a 25 euros — tu lui suggeres le t-shirt premium a 39 euros. L'objectif : faire monter en gamme.

**Cross-sell** : tu proposes un produit complementaire. Le client a un t-shirt dans son panier — tu lui suggeres une casquette assortie ou une ceinture. L'objectif : ajouter des articles a la commande.

Dans le contexte du side cart, les cross-sells fonctionnent generalement mieux que les upsells. Pourquoi ? Parce que le client a deja choisi son produit et l'a mis dans le panier. Lui proposer de le remplacer par un autre est moins naturel que lui proposer un complement.

Modern Cart affiche les deux, mais en pratique, concentre-toi sur les cross-sells pour le side cart. Les upsells ont plus d'impact sur les pages produit ou dans les funnels CartFlows post-achat.

---

**[SECTION 2 — Comment WooCommerce gere les recommandations]**

**[ECRAN — edition produit WooCommerce, onglet Produits lies]**

Les recommandations dans Modern Cart s'appuient sur les produits lies que tu configures dans WooCommerce. C'est un point important : Modern Cart affiche ce que WooCommerce connait — il ne genere pas de recommandations automatiques par IA.

Va dans Produits → selectionne un produit → onglet Produits lies (ou "Linked Products" en anglais).

Tu as deux champs :

- **Upsells** : les produits superieurs que tu veux suggerer
- **Cross-sells** : les produits complementaires

Pour chaque produit de ta boutique, remplis au minimum les cross-sells. C'est un travail manuel, mais c'est un investissement qui paie. Chaque association bien pensee est une opportunite de vente supplementaire.

Exemple concret : tu vends des formations WordPress. Un client ajoute la formation "WooCommerce Debutant". En cross-sell, tu mets : la formation "WooCommerce SEO", le pack de templates WooCommerce, le guide PDF de lancement boutique. Trois suggestions pertinentes qui enrichissent l'achat principal.

---

**[SECTION 3 — Activer les recommandations dans Modern Cart Pro]**

**[ECRAN — Modern Cart Pro → Settings → Upsells / Recommendations]**

Dans Modern Cart, va dans Settings → Upsells (ou Recommendations selon la version).

**Enable In-Cart Upsells** : active.

**Type de recommandation** : cross-sells, upsells, ou les deux. Comme je l'ai dit, privilegie les cross-sells dans le side cart.

**Nombre de produits affiches** : entre 2 et 3. C'est le bon equilibre. Un seul produit donne peu de choix. Quatre ou cinq produits encombrent le side cart et diluent l'attention. Deux ou trois, c'est optimal.

**Position** : en dessous de la liste de produits, au-dessus du total. C'est l'emplacement naturel — le client a vu ce qu'il a, et avant de passer au total, il decouvre des suggestions.

**Titre de la section** : "Tu pourrais aussi aimer", "Completer ta commande", ou "Produits complementaires". Choisis une formulation naturelle, pas vendeuse.

---

**[SECTION 4 — Le design des recommandations]**

**[ECRAN — side cart avec carrousel de recommandations]**

Les recommandations s'affichent generalement en carrousel horizontal dans le side cart. Chaque produit montre :

- L'image du produit (miniature)
- Le nom du produit
- Le prix
- Un bouton "Ajouter"

Le design doit rester coherent avec le reste du side cart. Memes couleurs de bouton, meme style. Le client ne doit pas avoir l'impression de passer d'une zone a une autre — tout doit etre fluide.

Un point sur les images : assure-toi que tes miniatures de produits sont propres et lisibles a petite taille. Dans un side cart de 380 pixels de large, les images de recommandation sont petites. Une image floue ou mal cadree donne une impression de mauvaise qualite.

Si tu as plus de 3 recommandations configurees pour un produit, le carrousel permet de scroller horizontalement. Mais ne compte pas sur le scroll — la plupart des clients ne scrolleront pas dans un carrousel a l'interieur d'un side cart. Les 2-3 premiers produits visibles sont ceux qui comptent.

---

**[SECTION 5 — Cas pratique : t-shirt + accessoires]**

**[ECRAN — demonstration complete ajout produit + recommandations]**

On va simuler un parcours complet.

Le client est sur la page d'un t-shirt a 29 euros. Il clique sur "Ajouter au panier". Le side cart s'ouvre.

En haut : la barre de livraison gratuite. "Plus que 20 euros pour la livraison gratuite !"

Au milieu : le t-shirt ajoute, avec quantite et prix.

En dessous : section "Complete ta commande" avec trois suggestions :
- Casquette assortie — 15 euros → bouton "Ajouter"
- Ceinture en cuir — 22 euros → bouton "Ajouter"
- Pack de 3 paires de chaussettes — 12 euros → bouton "Ajouter"

Le client clique sur "Ajouter" pour la casquette. La casquette apparait dans la liste du panier. Le total passe a 44 euros. La barre de livraison gratuite se met a jour : "Plus que 5 euros !"

Il voit les chaussettes a 12 euros. Il les ajoute. Total : 56 euros. Barre verte : "Livraison gratuite debloquee !"

Resultat : le client est venu pour un t-shirt a 29 euros. Il repart avec 56 euros de produits. La livraison gratuite et les recommandations ont fait le travail ensemble.

---

**[SECTION 6 — Bonnes pratiques]**

**[ECRAN — slide "regles d'or recommandations in-cart"]**

Quelques regles pour que les recommandations fonctionnent.

**Pertinence absolue.** Ne recommande jamais un produit sans rapport. Un client qui achete une formation WordPress ne veut pas voir une coque de telephone. Les recommandations non pertinentes degradent la confiance.

**Prix coherent.** Les cross-sells dans le side cart doivent etre moins chers que le produit principal. Le client a pris un produit a 29 euros — propose des complements a 10-20 euros, pas un accessoire a 89 euros.

**Pas de doublons.** Si le client a deja un produit dans le panier, ne le montre pas en recommandation. Modern Cart gere ca automatiquement dans la plupart des cas, mais verifie.

**Mets a jour regulierement.** Quand tu ajoutes de nouveaux produits a ta boutique, pense a mettre a jour les cross-sells de tes produits existants. Une boutique avec des recommandations a jour, c'est une boutique qui convertit mieux.

---

**[CONCLUSION — face camera]**

Les recommandations in-cart transforment le side cart en outil de vente. Le client decouvre des produits complementaires au moment exact ou il est en mode achat — sans popup, sans redirection, sans friction.

Prochaine lecon : le champ coupon integre au side cart. Encore une fonctionnalite Pro qui reduit les abandons.

---

## Notes de production

- **Visuels** : config produits lies WooCommerce, settings Modern Cart Pro, demo complete t-shirt + accessoires, carrousel recommandations
- **Animation** : montrer le side cart qui s'enrichit a chaque ajout (barre + recommandations + total qui evoluent)
- **Cas pratique** : utiliser des produits visuels (vetements) pour la demo, mais mentionner les formations comme exemple alternatif
- **Prerequis** : Modern Cart Pro actif, cross-sells configures sur au moins 3 produits WooCommerce
- **Transition** : enchaine sur LA.7 (champ coupon integre)
