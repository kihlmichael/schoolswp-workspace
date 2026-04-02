# Lecon A.8 — Modern Cart + CartFlows : le parcours complet

## Metadata

- **Formation** : CartFlows Add-ons (premium — FRM-008)
- **Module** : A — Modern Cart
- **Duree cible** : 8 min (~1100 mots)
- **Type** : Video HeyGen + voix ElevenLabs
- **Objectif pedagogique** : Comprendre comment Modern Cart et CartFlows se completent pour couvrir l'integralite du parcours d'achat, de la navigation au post-achat.

---

## Script narration

**[INTRO — face camera]**

Modern Cart optimise le panier. CartFlows optimise la conversion. Les deux plugins viennent de Brainstorm Force, et ils sont concus pour fonctionner ensemble. Dans cette lecon, on va connecter les deux et visualiser le parcours d'achat complet.

---

**[SECTION 1 — Les deux zones du parcours d'achat]**

**[ECRAN — schema du parcours complet en deux zones]**

Pour comprendre comment les deux plugins se completent, il faut voir le parcours d'achat comme deux zones distinctes.

**Zone 1 — L'exploration et l'accumulation.** Le client navigue sur ta boutique, decouvre des produits, les ajoute au panier, compare, hesite, ajoute encore. C'est la phase de "shopping". C'est le territoire de Modern Cart.

Pendant cette phase, Modern Cart fait trois choses :
- Il confirme chaque ajout au panier via le side cart (pas de redirection)
- Il montre des recommandations pour ajouter des produits complementaires
- Il utilise la barre de livraison gratuite pour inciter le client a remplir son panier
- Il permet d'appliquer un coupon avant meme d'arriver au checkout

**Zone 2 — La conversion et la maximisation.** Le client a decide d'acheter. Il clique sur "Passer commande". Il arrive sur le checkout. C'est la phase de "decision finale". C'est le territoire de CartFlows.

Pendant cette phase, CartFlows fait trois choses :
- Il presente un checkout optimise (moins de champs, elements de reassurance)
- Il propose un order bump (produit supplementaire en une case a cocher)
- Apres le paiement, il affiche un upsell one-click (offre complementaire sans re-saisir les infos bancaires)

Les deux zones se succedent naturellement. Modern Cart remplit le panier. CartFlows convertit le panier en commande et maximise la valeur.

---

**[SECTION 2 — Le flux complet etape par etape]**

**[ECRAN — animation du flux complet avec fleches]**

Deroulons le parcours complet d'un client.

**Etape 1 — Page produit.** Le client est sur la fiche d'un produit. Il clique sur "Ajouter au panier".

**Etape 2 — Side cart Modern Cart.** Le panneau lateral glisse. Le client voit son produit, le prix, les recommandations. La barre de livraison gratuite indique "Plus que 20 euros pour la livraison gratuite". Il ajoute un produit recommande. La barre passe au vert. Il entre un code promo. La remise s'applique.

**Etape 3 — Clic sur "Passer commande".** Le client clique sur le bouton du side cart. Il est redirige vers le checkout.

**Etape 4 — Checkout CartFlows.** Le client arrive sur ta page de checkout optimisee. Formulaire simplifie, elements de confiance (garantie, avis clients, logos de paiement). En bas du formulaire, un order bump : "Ajoute la garantie etendue pour 19 euros" avec une case a cocher.

**Etape 5 — Paiement.** Le client remplit ses infos et paie.

**Etape 6 — Upsell CartFlows.** Apres le paiement, une page s'affiche : "Offre exclusive : la formation avancee a -30%, uniquement maintenant." Un bouton "Oui, j'en profite" qui debite directement (one-click, pas besoin de re-saisir la carte). Ou un bouton "Non merci" pour passer.

**Etape 7 — Page de remerciement.** La commande est confirmee. Le client voit le recapitulatif.

Sept etapes. Modern Cart gere les etapes 1 a 3. CartFlows gere les etapes 4 a 7. Chaque plugin excelle dans sa zone.

---

**[SECTION 3 — Configurer le bouton "Commander" du side cart]**

**[ECRAN — Modern Cart → Settings → Checkout URL]**

Par defaut, le bouton "Passer commande" du side cart pointe vers la page checkout standard de WooCommerce. Si tu utilises CartFlows, tu veux qu'il pointe vers ton checkout CartFlows a la place.

Deux methodes.

**Methode 1 — CartFlows Checkout Takeover (Pro).** Si tu as active le "Store Checkout" dans CartFlows (le remplacement global du checkout WooCommerce), tu n'as rien a faire. Toutes les redirections vers le checkout passent automatiquement par CartFlows, y compris celle du side cart Modern Cart.

**Methode 2 — URL personnalisee.** Si tu n'utilises pas le Store Checkout de CartFlows, tu peux modifier l'URL du checkout dans Modern Cart → Settings → Checkout URL. Entre l'URL de ton checkout CartFlows (celle de ton Flow principal). Comme ca, le bouton du side cart envoie directement vers le bon funnel.

La methode 1 est la plus propre — un seul reglage dans CartFlows qui s'applique partout. Si tu as suivi la Masterclass CartFlows, c'est deja en place.

---

**[SECTION 4 — Ce que chaque plugin gere]**

**[ECRAN — tableau recapitulatif Modern Cart vs CartFlows]**

Pour clarifier les responsabilites :

| Moment | Plugin | Fonctionnalites |
|---|---|---|
| Navigation / ajout panier | Modern Cart | Side cart, icone flottante, badge |
| Dans le side cart | Modern Cart | Recommandations, barre livraison, coupon |
| Checkout | CartFlows | Formulaire optimise, custom fields |
| Pendant le paiement | CartFlows | Order bump |
| Apres le paiement | CartFlows | Upsell one-click, downsell |
| Confirmation | CartFlows | Page de remerciement personnalisee |

Il n'y a pas de chevauchement. Chaque plugin intervient a son moment. C'est pour ca que la combinaison fonctionne si bien — pas de conflit, pas de redondance.

---

**[SECTION 5 — Recap du Module A]**

**[ECRAN — slide recap 8 lecons]**

Faisons le bilan de ce module.

En 8 lecons, tu as couvert :
- Pourquoi le side cart reduit la friction et augmente les ventes (LA.1)
- L'installation et la configuration de base (LA.2)
- Le design complet : couleurs, position, animation (LA.3)
- L'icone flottante et le badge produit (LA.4)
- La barre de progression pour la livraison gratuite — Pro (LA.5)
- Les recommandations in-cart — Pro (LA.6)
- Le champ coupon integre — Pro (LA.7)
- L'integration avec CartFlows pour le parcours complet (LA.8)

Ton side cart est maintenant un outil de vente a part entiere. Il ne se contente pas d'afficher des produits — il incite a ajouter, rassure avec le coupon, motive avec la barre de livraison, et redirige vers un checkout optimise par CartFlows.

---

**[CONCLUSION — face camera]**

Modern Cart et CartFlows ensemble, c'est la couverture complete du parcours d'achat. L'un optimise le panier, l'autre optimise la conversion. Les deux plugins viennent du meme editeur, ils sont concus pour fonctionner en tandem, et les resultats sont la.

Dans le Module B, on va decouvrir un autre add-on CartFlows qui cible un moment critique : l'abandon de panier. On parlera de Cart Abandonment Recovery. A tout de suite.

---

## Notes de production

- **Visuels** : schema flux complet (7 etapes avec fleches), config URL checkout, tableau recapitulatif Modern Cart vs CartFlows
- **Animation** : parcours client complet en simulation (side cart → checkout CartFlows → bump → upsell → thank you)
- **Slide recap** : les 8 titres de lecons avec icones ou check marks
- **Prerequis** : Modern Cart Pro + CartFlows Pro actifs, Store Checkout active
- **Transition** : annonce Module B (Cart Abandonment Recovery)
