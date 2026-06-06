# Lecon C.4 - Conditions avancees : valeur panier, produit, historique

## Metadata

- **Formation** : CartFlows Add-ons (premium - FRM-008)
- **Module** : C - Power Coupons
- **Duree cible** : 10 min (~1400 mots)
- **Type** : Video HeyGen + voix ElevenLabs
- **Objectif pedagogique** : Maitriser les conditions avancees de Power Coupons pour creer des regles promotionnelles precises basees sur le panier, les produits, l'historique client et le contexte temporel.

---

## Script narration

**[INTRO - face camera]**

Dans la lecon precedente, on a configure un coupon auto-applique avec une condition simple : montant minimum du panier. C'est un bon debut. Mais Power Coupons va beaucoup plus loin.

Tu peux cibler un client selon ce qu'il a dans son panier, son historique d'achats, son role, sa premiere commande, ou meme le jour de la semaine. Et tu peux combiner tout ca.

On va passer en revue chaque type de condition et creer un exemple concret.

---

**[SECTION 1 - Conditions sur la valeur du panier]**

**[ECRAN - Power Coupons, section conditions → Cart]**

La condition de base, tu la connais : montant minimum du panier. Mais tu peux aussi definir un montant maximum ou une fourchette.

Montant minimum : "Cart Total greater than 50€". Le coupon ne s'active que si le panier depasse 50€.

Montant maximum : "Cart Total less than 200€". Utile si tu veux limiter une promo aux petits paniers - pour les gros paniers, tu as une autre offre.

Fourchette : combine les deux. "Cart Total between 50€ and 150€". Le coupon ne s'active que dans cette tranche. En dessous de 50€, le client est incite a ajouter des produits. Au-dessus de 150€, il passe sur une offre premium differente.

Tu peux aussi conditionner sur le nombre d'articles : "Cart Items Count greater than 3". Le coupon ne s'active que si le client a au moins 4 produits dans son panier.

---

**[SECTION 2 - Conditions sur les produits et categories]**

**[ECRAN - conditions → Products]**

Tu peux cibler des produits specifiques ou des categories entieres.

Produit specifique : "Cart contains Product X". Le coupon ne s'active que si le produit X est dans le panier. Exemple : tu vends un logiciel et tu veux offrir -20% sur l'extension quand le client achete la licence de base. Tu crees un coupon conditionne sur la presence de la licence dans le panier.

Categorie de produits : "Cart contains product from Category Y". Le coupon s'active des qu'un produit de la categorie "Formations" est dans le panier. Plus large, plus flexible.

Exclusion : tu peux aussi exclure des produits ou des categories. "Cart does not contain Product Z". Le coupon s'active seulement si le produit Z n'est pas dans le panier. Utile pour exclure les produits deja en promo.

---

**[SECTION 3 - Conditions sur l'historique client]**

**[ECRAN - conditions → Customer History]**

C'est la ou Power Coupons se demarque vraiment des coupons WooCommerce natifs.

Nombre de commandes passees : "Customer order count greater than 3". Le coupon ne s'active que pour les clients qui ont deja passe au moins 4 commandes. Tu recompenses la fidelite.

Montant total depense : "Customer total spent greater than 200€". Le coupon s'active pour les clients qui ont depense plus de 200€ au cumul. C'est un seuil VIP.

Premiere commande : "Customer order count equals 0". Le coupon ne s'active que pour un nouveau client qui n'a jamais commande. Parfait pour un coupon de bienvenue.

Derniere commande : "Last order date more than 30 days ago". Le coupon cible les clients inactifs depuis plus d'un mois. Tu les reactives avec une offre de retour.

---

**[SECTION 4 - Conditions sur le role et le contexte]**

**[ECRAN - conditions → User Role + Date/Time]**

Role utilisateur : "User role is Wholesale". Le coupon ne s'active que pour les clients avec un role specifique. Si tu as des clients B2B avec un role "Wholesale" et des clients B2C avec le role "Customer", tu crees des promos differenciees.

Statut de connexion : "User is logged in". Le coupon ne s'active que pour les clients connectes. Ca incite la creation de compte.

Jour de la semaine : "Day is Saturday OR Day is Sunday". Le coupon ne s'active que le weekend. Promo weekend automatique.

Plage horaire : "Time between 12:00 and 14:00". Happy hour. Le coupon ne s'active qu'entre midi et 14h. C'est un mecanisme d'urgence qui fonctionne bien pour les promos flash.

---

**[SECTION 5 - Combiner les conditions : ET / OU]**

**[ECRAN - interface conditions avec groupes ET/OU]**

La vraie puissance, c'est la combinaison. Power Coupons utilise une logique ET / OU.

ET : toutes les conditions du groupe doivent etre remplies. "Panier > 60€ ET premiere commande". Les deux conditions doivent etre vraies.

OU : au moins une condition du groupe doit etre remplie. "Categorie Formations OU Categorie Coaching". Le coupon s'active si le client a un produit dans l'une ou l'autre categorie.

Tu peux creer plusieurs groupes de conditions. Chaque groupe est lie par un ET, et les conditions a l'interieur d'un groupe peuvent etre liees par ET ou OU.

---

**[SECTION 6 - Cas pratique : livraison gratuite premier achat]**

**[ECRAN - configuration complete du coupon]**

On va creer un exemple concret. L'objectif : livraison gratuite si le panier depasse 60€ et que c'est la premiere commande du client.

Cree un nouveau coupon. Type : "Livraison gratuite". Nom interne : "free-shipping-first-order".

Onglet Power Coupons → Enable Auto Apply.

Conditions :
- Condition 1 : "Cart Total greater than or equal to 60€"
- Condition 2 : "Customer order count equals 0"
- Logique : ET (les deux doivent etre remplies)

Publie. Teste en navigation privee. Ajoute pour 60€+ au panier. Au checkout, la livraison gratuite s'applique automatiquement. Le client voit "Livraison gratuite - premiere commande".

Ce type de promo a un double effet. Elle convertit le premier achat en eliminant les frais de port - le frein numero un. Et elle fixe un seuil de panier minimum qui protege ta marge.

---

**[CONCLUSION - face camera]**

Tu as maintenant acces a des conditions que WooCommerce natif ne propose pas. Historique, roles, temporalite, combinaisons logiques. Ca te permet de creer des promos chirurgicales : la bonne offre, au bon client, au bon moment.

Dans la prochaine lecon, on passe au BOGO - Buy One Get One. La promotion la plus puissante du e-commerce.

---

## Notes de production

- **Visuels** : captures onglet Power Coupons pour chaque type de condition (Cart, Products, Customer History, User Role, Date/Time), demo configuration coupon livraison gratuite premier achat
- **Donnees** : impact conditions avancees sur la precision du ciblage promotionnel
- **Transition** : enchaine sur LC.5 (BOGO)
