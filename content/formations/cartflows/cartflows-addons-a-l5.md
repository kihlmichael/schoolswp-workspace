# Lecon A.5 - Modern Cart Pro : barre de progression livraison gratuite

## Metadata

- **Formation** : CartFlows Add-ons (premium - FRM-008)
- **Module** : A - Modern Cart
- **Duree cible** : 8 min (~1100 mots)
- **Type** : Video HeyGen + voix ElevenLabs
- **Objectif pedagogique** : Configurer la barre de progression "livraison gratuite" dans Modern Cart Pro pour inciter les clients a augmenter leur panier moyen.

---

## Script narration

**[INTRO - face camera]**

"Plus que 12 euros pour la livraison gratuite." Cette phrase, tu l'as deja vue sur les sites e-commerce. Et si tu l'as vue, c'est parce que ca fonctionne. C'est un des leviers les plus puissants pour augmenter le panier moyen - et Modern Cart Pro l'integre directement dans le side cart.

A partir de cette lecon, on entre dans les fonctionnalites Pro. Si tu as la version gratuite, c'est le bon moment pour evaluer si la mise a niveau vaut le coup pour ta boutique.

---

**[SECTION 1 - Le principe psychologique]**

**[ECRAN - slide "psychologie de la barre de progression"]**

La barre de progression pour la livraison gratuite exploite deux biais cognitifs.

**L'aversion a la perte.** Le client a deja des produits dans son panier. Il va payer des frais de livraison - mais il pourrait les eviter. Payer la livraison quand il aurait pu l'avoir gratuitement, ca ressemble a une perte. Et les humains detestent les pertes plus qu'ils n'aiment les gains.

**L'effet de progression.** Une barre qui se remplit cree une envie de la completer. Le client est a 60% du seuil - il veut atteindre les 100%. C'est le meme mecanisme que les barres de progression de profil sur LinkedIn ou les jauges de fidelite.

Les chiffres le confirment : les boutiques qui implementent une barre de progression pour la livraison gratuite constatent une augmentation du panier moyen de 10 a 20%. Le client ajoute un produit supplementaire pour franchir le seuil, plutot que de payer 5 ou 6 euros de livraison.

---

**[SECTION 2 - Prerequis : configurer la livraison gratuite dans WooCommerce]**

**[ECRAN - WooCommerce → Reglages → Livraison]**

Avant de configurer la barre dans Modern Cart, il faut que la livraison gratuite soit active dans WooCommerce avec un montant minimum. Si c'est deja fait, passe a la section suivante.

Va dans WooCommerce → Reglages → Livraison. Selectionne ta zone de livraison (France metropolitaine, par exemple). Clique sur Ajouter une methode de livraison → Livraison gratuite.

Dans les options de la methode, choisis "Un montant minimum de commande" comme condition. Entre ton seuil - par exemple 49 euros. Ca signifie : en dessous de 49 euros, le client paie les frais de port. A partir de 49 euros, la livraison est gratuite.

Comment choisir le seuil ? Regarde ton panier moyen actuel dans WooCommerce → Rapports. Si ton panier moyen est de 35 euros, un seuil a 49 euros est ideal - le client doit ajouter un petit produit pour y arriver. Si ton panier moyen est de 20 euros, un seuil a 80 euros est trop ambitieux. Vise entre 30 et 50% au-dessus de ton panier moyen actuel.

Sauvegarde. La livraison gratuite conditionnelle est active.

---

**[SECTION 3 - Activer la barre dans Modern Cart Pro]**

**[ECRAN - Modern Cart Pro → Settings → Free Shipping Bar]**

Maintenant, dans Modern Cart, va dans Settings → Free Shipping Bar (ou Progress Bar selon la version).

**Enable Free Shipping Bar** : active. La barre va s'afficher en haut du side cart, au-dessus de la liste de produits.

**Threshold (seuil)** : Modern Cart detecte automatiquement le seuil de livraison gratuite configure dans WooCommerce. Verifie que le montant affiche correspond. Si tu as plusieurs zones de livraison avec des seuils differents, Modern Cart utilise generalement le seuil de la zone par defaut.

**Texte de progression.** C'est le message affiche au-dessus de la barre. Modern Cart propose des textes dynamiques avec des variables :

- "Plus que {remaining} pour la livraison gratuite !" - le montant restant se calcule automatiquement
- "Tu as atteint la livraison gratuite !" - le message quand le seuil est depasse

Personnalise le texte pour qu'il sonne naturel dans ta boutique. Tutoiement, ton direct, pas de formulation corporate.

---

**[SECTION 4 - Personnaliser les couleurs de la barre]**

**[ECRAN - options couleurs barre de progression]**

La barre de progression a deux etats visuels.

**En progression.** La partie remplie de la barre. Utilise une couleur qui avance - un bleu, un orange, un vert. Evite le rouge (associe a l'erreur ou au danger).

**Objectif atteint.** Quand le client depasse le seuil, la barre se remplit a 100% et change de couleur. Un vert franc signale le succes. Le texte passe au message de felicitation.

**Le fond de la barre** (partie non remplie) : un gris clair. Ca cree le contraste avec la partie remplie et rend la progression visible.

Tu peux aussi ajuster l'epaisseur de la barre. Fine (4-6px) pour un look discret. Epaisse (10-12px) pour un impact visuel fort. Je recommande une epaisseur moyenne - suffisamment visible sans dominer le side cart.

---

**[SECTION 5 - La barre en action]**

**[ECRAN - demonstration complete : ajout produits, barre qui progresse]**

Voyons la barre en situation reelle.

Le client ajoute un produit a 29 euros. Le side cart s'ouvre. En haut : "Plus que 20 euros pour la livraison gratuite !" La barre est remplie a environ 60%.

Il ajoute un deuxieme produit a 15 euros. Le side cart se met a jour. Total : 44 euros. "Plus que 5 euros pour la livraison gratuite !" La barre est presque pleine.

Il ajoute un accessoire a 9 euros. Total : 53 euros. La barre passe a 100%, vert. "Livraison gratuite debloquee !" Le client est satisfait - il a "gagne" la livraison gratuite.

Ce qui s'est passe en realite : le client a depense 24 euros de plus que son achat initial pour economiser 5 euros de frais de port. C'est la que la barre de progression est puissante.

---

**[CONCLUSION - face camera]**

La barre de progression pour la livraison gratuite est probablement la fonctionnalite Pro de Modern Cart qui a le meilleur retour sur investissement. A 69 dollars par an, si elle augmente ton panier moyen ne serait-ce que de 10%, le plugin est rentabilise en quelques commandes.

Dans la prochaine lecon, on attaque les recommandations in-cart - des produits suggeres directement dans le side cart.

---

## Notes de production

- **Visuels** : config WooCommerce livraison gratuite, settings Modern Cart Pro, barre en action (3 etapes d'ajout progressif)
- **Animation** : montrer la barre qui se remplit progressivement a chaque ajout de produit
- **Chiffres** : augmentation AOV 10-20% (donnees secteur e-commerce, pas specifiques Modern Cart)
- **Prerequis** : Modern Cart Pro actif, livraison gratuite configuree dans WooCommerce
- **Transition** : enchaine sur LA.6 (recommandations in-cart)
