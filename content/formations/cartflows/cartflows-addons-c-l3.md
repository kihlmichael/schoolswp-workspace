# Lecon C.3 - Auto-application : offres sans code coupon

## Metadata

- **Formation** : CartFlows Add-ons (premium - FRM-008)
- **Module** : C - Power Coupons
- **Duree cible** : 8 min (~1100 mots)
- **Type** : Video HeyGen + voix ElevenLabs
- **Objectif pedagogique** : Configurer un coupon auto-applique avec Power Coupons, comprendre pourquoi l'auto-application elimine la friction et augmente les conversions.

---

## Script narration

**[INTRO - face camera]**

Le plus gros frein des coupons classiques, c'est le code. Le client doit le connaitre, s'en souvenir, et le taper. S'il oublie, il paye plein tarif. S'il ne l'a jamais vu, ta promo n'existe pas pour lui.

L'auto-application supprime ce probleme. Le coupon s'active tout seul quand les conditions sont remplies. Zero friction, zero code a taper. C'est la fonctionnalite numero un de Power Coupons.

---

**[SECTION 1 - Pourquoi l'auto-application change tout]**

**[ECRAN - slide comparaison coupon classique vs auto-apply]**

Avec un coupon classique, le parcours ressemble a ca. Le client arrive sur ta boutique. Il ajoute des produits au panier. Il arrive au checkout. Il voit le champ "Code promo". Deux scenarios possibles.

Scenario 1 : il a un code. Il le tape, ca marche, il est content.

Scenario 2 : il n'a pas de code. Il voit le champ vide et se dit "il doit y avoir une promo quelque part". Il quitte le checkout, ouvre un nouvel onglet, tape "code promo + ton site" sur Google. S'il trouve un code perime, il est frustre. S'il ne trouve rien, il revient au checkout avec un sentiment negatif.

Le simple fait d'afficher un champ "Code promo" cree de la friction, meme quand le client n'a pas de code.

Avec l'auto-application, le client n'a rien a faire. Il ajoute pour 80€ au panier, la remise de -10% apparait automatiquement. Il voit la ligne de reduction, il comprend qu'il beneficie d'une offre. Pas de champ a remplir, pas de recherche, pas de frustration.

---

**[SECTION 2 - Configurer un coupon auto-applique]**

**[ECRAN - WordPress admin → WooCommerce → Coupons → Ajouter]**

On va creer ensemble un coupon auto-applique. L'objectif : -10% automatique des que le panier depasse 80€.

Va dans WooCommerce → Marketing → Coupons → Ajouter un coupon.

Donne un nom interne au coupon - par exemple "auto-10pct-80eur". Ce nom n'est pas visible par le client, c'est juste pour toi.

Dans "Type de remise", selectionne "Remise en pourcentage". Indique 10 dans le montant.

Maintenant, clique sur l'onglet "Power Coupons". C'est la que tout se passe.

Active l'option "Enable Auto Apply". C'est la case qui transforme un coupon classique en coupon automatique.

---

**[SECTION 3 - Definir les conditions]**

**[ECRAN - onglet Power Coupons, section conditions]**

En dessous de l'auto-application, tu as la section "Conditions". C'est la que tu definis quand le coupon se declenche.

Pour notre exemple, on va ajouter une condition : "Cart Total" → "Greater than or equal to" → "80".

Ca veut dire : des que le total du panier atteint ou depasse 80€, le coupon de 10% s'applique automatiquement.

Tu peux ajouter d'autres conditions si tu veux. Par exemple :

- Produit specifique : le coupon ne s'active que si le produit X est dans le panier.
- Categorie : le coupon ne s'active que si un produit de la categorie "Accessoires" est present.
- Role utilisateur : le coupon ne s'active que pour les clients avec le role "Subscriber" ou "Wholesale".
- Premiere commande : le coupon ne s'active que pour un client qui n'a jamais commande.

Chaque condition se configure en quelques clics. On va les detailler dans la lecon suivante.

Pour l'instant, on reste simple : montant minimum 80€.

Publie le coupon.

---

**[SECTION 4 - Tester l'auto-application]**

**[ECRAN - boutique front-end, ajout produits au panier]**

On va tester. Ouvre ta boutique en mode visiteur - ou utilise une fenetre de navigation privee.

Ajoute des produits au panier pour un total inferieur a 80€. Ouvre le panier ou le side cart. Pas de remise. Normal.

Maintenant, ajoute un produit supplementaire pour depasser 80€. Regarde le panier. La remise de 10% apparait automatiquement. Le client voit une ligne "Coupon : auto-10pct-80eur - -X€".

Note : tu peux personnaliser le libelle affiche dans les reglages Power Coupons pour que le client voie "Remise automatique -10%" au lieu du nom technique du coupon.

---

**[SECTION 5 - Cas pratique et conseil]**

**[ECRAN - slide recapitulatif]**

Le cas pratique qu'on vient de configurer - "-10% automatique des 80€ d'achat" - c'est un classique du e-commerce. Il incite le client a atteindre le seuil. Un client avec 65€ dans son panier va chercher un produit a 15€ pour debloquer la promo. Tu augmentes l'AOV sans effort supplementaire.

L'auto-application est la feature numero un de Power Coupons. Elle elimine le plus gros frein des coupons : devoir connaitre le code. Un client qui beneficie d'une remise automatique a une meilleure experience d'achat. Et un client satisfait revient.

Combine l'auto-application avec la barre de progression de Modern Cart - "Plus que 15€ pour -10% sur ta commande" - et tu as un systeme qui pousse naturellement le panier vers le haut.

---

**[CONCLUSION - face camera]**

Tu as ton premier coupon auto-applique. Le client n'a rien a taper, la remise apparait toute seule. C'est propre, c'est efficace, ca convertit.

Dans la prochaine lecon, on va approfondir les conditions avancees. Historique client, roles, jours de la semaine - Power Coupons permet des regles tres precises.

---

## Notes de production

- **Visuels** : comparaison parcours coupon classique vs auto-apply, captures configuration coupon WooCommerce + onglet Power Coupons, demo front-end panier avec remise automatique
- **Donnees** : impact champ "code promo" sur les abandons checkout (etudes UX)
- **Transition** : enchaine sur LC.4 (conditions avancees)
