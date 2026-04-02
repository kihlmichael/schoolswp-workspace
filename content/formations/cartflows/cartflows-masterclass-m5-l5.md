# Lecon 5.5 — Dynamic Offers : offres conditionnelles selon le panier

## Metadata

- **Formation** : CartFlows Masterclass Vente (premium — FRM-007)
- **Module** : 5 — One-Click Upsells et Downsells
- **Duree cible** : 10 min (~1400 mots)
- **Type** : Video HeyGen + voix ElevenLabs
- **Objectif pedagogique** : Comprendre et configurer les Dynamic Offers de CartFlows Pro. Creer des regles conditionnelles qui adaptent l'upsell/downsell selon le produit achete, le montant du panier ou la quantite.

---

## Script narration

**[INTRO — face camera]**

Jusqu'ici, ton upsell est le meme pour tout le monde. Que le client achete ta formation debutant ou ton pack complet, il voit la meme offre. Ca fonctionne, mais c'est loin d'etre optimal.

Avec les Dynamic Offers de CartFlows Pro, tu peux adapter l'upsell en fonction de ce que le client vient d'acheter. Chaque client voit l'offre la plus pertinente pour sa situation. Et la pertinence, c'est ce qui fait passer un taux d'acceptation de 10% a 25%.

---

**[SECTION 1 — Le probleme de l'offre unique]**

**[ECRAN — schema : 2 clients differents, meme upsell]**

Prenons un exemple. Tu vends deux formations : "WordPress Debutant" a 47 euros et "WordPress Avance" a 197 euros. Ton upsell propose un coaching a 97 euros.

Le client qui achete la formation debutant voit le coaching : ca peut l'interesser, il debute, il a besoin d'accompagnement. Taux d'acceptation : correct.

Le client qui achete la formation avancee voit le meme coaching : il est deja avance, un coaching debutant ne l'interesse pas. Taux d'acceptation : faible.

Si tu pouvais proposer au client avance un audit de site personnalise a 147 euros au lieu du coaching, le taux d'acceptation remonterait. C'est exactement ce que font les Dynamic Offers.

---

**[SECTION 2 — Qu'est-ce que les Dynamic Offers]**

**[ECRAN — schema logique : SI produit = X ALORS upsell = Y]**

Les Dynamic Offers sont un systeme de regles conditionnelles integre a CartFlows Pro. Pour chaque step upsell ou downsell, tu peux definir plusieurs offres avec des conditions d'affichage.

Le principe : SI le client a achete le produit X, ALORS montre l'upsell Y. SINON, montre l'upsell Z.

Les conditions disponibles :

- **Produit principal** : quel produit le client a achete au checkout
- **Montant total** : le total de la commande au checkout (par exemple : si total > 100 euros)
- **Quantite** : le nombre d'articles commandes
- **Categorie de produit** : la categorie WooCommerce du produit achete

Tu peux combiner ces conditions avec des ET / OU pour creer des regles fines.

---

**[SECTION 3 — Configurer une Dynamic Offer]**

**[ECRAN — CartFlows → Flow → Step Upsell → Dynamic Offers]**

Ouvre les parametres de ton step Upsell. Tu vas trouver un onglet ou une section "Dynamic Offers" (disponible uniquement avec CartFlows Pro).

Clique sur "Add Offer". Tu vois apparaitre un formulaire avec :
- **Product** : le produit WooCommerce a proposer en upsell pour cette regle
- **Offer Price** : le prix special de l'offre (optionnel)
- **Conditions** : les regles qui declenchent cette offre

**[ECRAN — ajout de la premiere regle]**

Premiere regle : si le client a achete "Formation WordPress Debutant", propose le "Coaching Personnalise 1h" a 97 euros.

Configure la condition : Product in Cart → contient → "Formation WordPress Debutant". Associe le produit "Coaching Personnalise 1h" et definis le prix d'offre a 97 euros.

**[ECRAN — ajout de la deuxieme regle]**

Deuxieme regle : si le client a achete "Formation WordPress Avance", propose l'"Audit de Site Personnalise" a 147 euros.

Configure la condition : Product in Cart → contient → "Formation WordPress Avance". Associe le produit "Audit de Site" avec le prix d'offre.

**[ECRAN — vue des deux regles configurees]**

CartFlows evaline les regles dans l'ordre. La premiere regle qui matche est celle qui s'affiche. Si aucune regle ne matche, le comportement par defaut s'applique (tu peux definir une offre par defaut).

---

**[SECTION 4 — Regles basees sur le montant]**

**[ECRAN — condition basee sur le montant total]**

Les regles par montant sont puissantes pour segmenter tes offres. Exemple :

- Si le total du checkout est inferieur a 100 euros → upsell a petit prix (27 euros)
- Si le total est entre 100 et 200 euros → upsell moyen (67 euros)
- Si le total depasse 200 euros → upsell premium (147 euros)

La logique : un client qui vient de depenser 200 euros a deja montre une forte intention d'investissement. Il est plus receptif a un upsell a 147 euros qu'un client qui a depense 47 euros.

**[ECRAN — configuration de la condition "Cart Total > 200"]**

Pour configurer ca : Add Offer → Condition → Cart Total → Greater Than → 200. Associe le produit premium.

---

**[SECTION 5 — Exemple complet avec 3 chemins dynamiques]**

**[ECRAN — schema des 3 chemins dynamiques]**

Construisons un exemple concret. Tu as un funnel avec 3 produits possibles au checkout :

1. **Ebook WordPress** (27 euros) → Upsell : Formation Video (67 euros)
2. **Formation Basique** (97 euros) → Upsell : Formation Premium (197 euros)
3. **Pack Complet** (297 euros) → Upsell : Coaching Individuel (247 euros)

Chaque client voit l'offre adaptee a son niveau d'engagement et a son investissement initial. L'ebook buyer voit une montee en gamme accessible. Le pack complet buyer voit une offre premium qui correspond a son profil.

**[ECRAN — les 3 regles configurees dans CartFlows]**

Tu peux faire la meme chose pour les downsells. Si l'upsell "Formation Premium" est refuse, le downsell propose "Acces 3 modules" a 47 euros. Si l'upsell "Coaching" est refuse, le downsell propose "Audit ecrit" a 97 euros.

---

**[SECTION 6 — Pourquoi c'est un avantage decisif]**

**[ECRAN — comparaison taux de conversion upsell statique vs dynamique]**

Un upsell statique (meme offre pour tout le monde) convertit typiquement entre 5 et 15%. Un upsell dynamique bien configure monte a 15-30%. La difference vient de la pertinence : chaque client voit une offre qui correspond a ce qu'il vient d'acheter.

C'est le meme principe que la personnalisation e-commerce d'Amazon ou de Netflix. Plus l'offre est pertinente, plus le taux d'acceptation est eleve.

Et tu n'as pas besoin de 50 regles pour demarrer. Deux ou trois regles bien pensees suffisent pour doubler l'efficacite de tes upsells.

---

**[OUTRO — face camera]**

Les Dynamic Offers transforment un upsell generique en une offre personnalisee. Chaque client voit l'offre la plus pertinente pour lui, et tes taux de conversion s'en ressentent directement.

Dans la prochaine lecon, on va aller encore plus loin avec les Segments : cibler tes offres en fonction de l'historique d'achat du client, pas seulement de sa commande actuelle.

---

## Notes de production

- **Visuels** : schemas conditionnels (SI/ALORS), captures CartFlows Pro (Dynamic Offers UI), tableau des 3 chemins, graphique comparaison taux de conversion
- **Captures d'ecran** : interface Dynamic Offers, configuration conditions, regles multiples
- **Prerequis technique** : CartFlows Pro obligatoire pour les Dynamic Offers
- **Ton** : strategique et technique, exemples chiffres
- **Duree estimee** : ~10 min a debit normal
- **Transition** : enchaine sur L5.6 (Segments)
