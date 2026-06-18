# Lecon C.6 - Livraison gratuite conditionnelle

## Metadata

- **Formation** : CartFlows Add-ons (premium - FRM-008)
- **Module** : C - Power Coupons
- **Duree cible** : 6 min (~900 mots)
- **Type** : Video HeyGen + voix ElevenLabs
- **Objectif pedagogique** : Configurer la livraison gratuite conditionnelle avec Power Coupons et exploiter la synergie avec la barre de progression Modern Cart pour augmenter l'AOV.

---

## Script narration

**[INTRO - face camera]**

Les frais de livraison sont le frein numero un a la conversion en e-commerce. Le client voit un produit a 45€, il l'ajoute au panier, il arrive au checkout et decouvre 7€ de frais de port. Le prix percu vient de passer de 45€ a 52€. Et c'est souvent la que la commande est abandonnee.

La livraison gratuite conditionnelle resout ce probleme tout en protegeant ta marge. Le client obtient la livraison gratuite, mais seulement s'il atteint un seuil. Et ce seuil, c'est ton levier pour augmenter le panier moyen.

---

**[SECTION 1 - WooCommerce natif vs Power Coupons]**

**[ECRAN - slide comparaison]**

WooCommerce propose nativement la livraison gratuite. Tu peux la configurer dans les zones de livraison avec un montant minimum de commande. C'est basique et ca fonctionne.

Mais tu ne peux pas conditionner la livraison gratuite sur autre chose que le montant du panier. Tu ne peux pas dire "livraison gratuite pour la categorie Vetements uniquement" ou "livraison gratuite pour les clients fideles" ou "livraison gratuite le weekend".

Power Coupons reprend toutes les conditions avancees qu'on a vues dans la lecon precedente et les applique a la livraison gratuite. Tu combines montant du panier, categorie de produit, historique client, role, temporalite - tout est disponible.

---

**[SECTION 2 - Configurer la livraison gratuite conditionnelle]**

**[ECRAN - WordPress admin → Coupons → Ajouter]**

On va creer un exemple. L'objectif : livraison gratuite automatique des 60€ d'achat.

Cree un nouveau coupon. Nom interne : "free-shipping-60eur".

Type de remise : "Livraison gratuite". Coche la case.

Onglet Power Coupons → Enable Auto Apply.

Conditions : "Cart Total greater than or equal to 60€".

Publie. C'est fait.

Le client qui a 60€ ou plus dans son panier voit la livraison passer a 0€ automatiquement. Celui qui a 55€ voit les frais de port normaux - et c'est la que la barre de progression entre en jeu.

---

**[SECTION 3 - La synergie avec Modern Cart]**

**[ECRAN - front-end, side cart avec barre de progression]**

Si tu as installe Modern Cart - qu'on a couvert dans le Module A - tu peux activer la barre de progression dans le side cart.

Cette barre affiche un message dynamique : "Plus que 5€ pour la livraison gratuite !" Le client voit exactement combien il lui manque pour debloquer l'offre.

C'est la combinaison la plus puissante de la formation : Power Coupons gere la regle (livraison gratuite des 60€), Modern Cart gere l'affichage (la barre de progression).

Le resultat : le client avec 55€ dans son panier voit "Plus que 5€ pour la livraison gratuite". Il ajoute un petit produit a 8€ pour passer le seuil. Son panier passe de 55€ a 63€. Tu as augmente l'AOV de 15% sur cette commande.

Sans la barre de progression, le client ne sait pas qu'il est a 5€ du seuil. Il paye les frais de port et tu perds l'opportunite.

---

**[SECTION 4 - Conditions avancees pour la livraison]**

**[ECRAN - exemples de conditions]**

Quelques exemples de conditions avancees specifiques a la livraison.

Par categorie : livraison gratuite uniquement sur les produits de la categorie "Accessoires". Les produits volumineux restent avec frais de port. Ca protege ta marge sur les envois couteux.

Premiere commande : livraison gratuite pour le premier achat, sans condition de montant. Tu elimines le frein numero un pour convertir un visiteur en client. Le cout de la livraison offerte, c'est ton cout d'acquisition client.

Client fidele : livraison gratuite permanente pour les clients qui ont depense plus de 300€ au total. C'est un avantage VIP qui recompense la fidelite.

Weekend : livraison gratuite le samedi et le dimanche. Tu concentres tes ventes sur le weekend - le moment ou les clients naviguent le plus.

---

**[SECTION 5 - Conseil strategique]**

**[ECRAN - slide conseil]**

La livraison gratuite conditionnelle est le levier numero un pour augmenter l'AOV. Le client ajoute un produit pour eviter les frais de port. C'est un comportement previsible et mesurable.

Pour choisir le bon seuil, regarde ton AOV actuel. Si ton panier moyen est a 45€, fixe le seuil de livraison gratuite a 60€. Le client a 45€ va ajouter 15€ de produits pour franchir le seuil. Si tu fixes le seuil a 120€, il ne fera pas l'effort - c'est trop loin. Le seuil ideal est entre 20% et 40% au-dessus de ton AOV.

---

**[CONCLUSION - face camera]**

La livraison gratuite conditionnelle avec Power Coupons, combinee a la barre de progression de Modern Cart - c'est le duo le plus rentable de cette formation. La regle est invisible pour le client, l'incitation est visible.

Dans la prochaine lecon, on passe au programme de fidelite. Points, credits, conversion - on construit un systeme qui fait revenir les clients.

---

## Notes de production

- **Visuels** : comparaison WooCommerce natif vs Power Coupons pour la livraison, capture configuration coupon, demo barre de progression Modern Cart avec compteur, slide exemples conditions avancees
- **Donnees** : impact frais de port sur abandon (source Baymard), formule seuil optimal = AOV + 20-40%
- **Transition** : enchaine sur LC.7 (programme de fidelite)
