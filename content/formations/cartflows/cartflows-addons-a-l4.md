# Lecon A.4 - Icone flottante et badge produit

## Metadata

- **Formation** : CartFlows Add-ons (premium - FRM-008)
- **Module** : A - Modern Cart
- **Duree cible** : 6 min (~900 mots)
- **Type** : Video HeyGen + voix ElevenLabs
- **Objectif pedagogique** : Configurer l'icone flottante sticky et le badge produit pour maintenir la visibilite du panier en permanence pendant la navigation.

---

## Script narration

**[INTRO - face camera]**

L'icone flottante, c'est le petit bouton de panier qui reste colle a l'ecran meme quand le client scrolle. C'est un rappel visuel permanent : "Tu as quelque chose dans ton panier." Et ce rappel, il fait la difference entre un client qui oublie son panier et un client qui finalise sa commande.

---

**[SECTION 1 - L'icone flottante : toujours visible]**

**[ECRAN - page boutique avec icone flottante visible en scrollant]**

Par defaut, le panier de ton site est dans le header. Le probleme : des que le client scrolle vers le bas, le header disparait (sauf si tu as un header sticky). L'icone de panier disparait avec.

L'icone flottante de Modern Cart resout ce probleme. C'est un bouton fixe positionne dans un coin de l'ecran - en bas a droite le plus souvent. Quand le client scrolle, l'icone reste en place. Il peut cliquer dessus a tout moment pour ouvrir le side cart.

Pour l'activer : Modern Cart → Settings → Floating Cart Icon → Enable. Si tu as suivi le wizard dans la lecon precedente, c'est deja fait.

**Position.** Tu peux placer l'icone en bas a droite (le plus courant), en bas a gauche, ou dans d'autres positions selon les options disponibles. Bas a droite est le standard - c'est la que les utilisateurs s'attendent a trouver un bouton d'action flottant (meme logique que les boutons de chat).

---

**[SECTION 2 - Le badge : nombre de produits]**

**[ECRAN - icone flottante avec badge rouge "3"]**

Le badge, c'est le petit cercle colore qui s'affiche au coin de l'icone avec le nombre de produits dans le panier. Quand le panier est vide : pas de badge. Quand le client ajoute un produit : le badge apparait avec "1". Deux produits : "2". Et ainsi de suite.

C'est un signal visuel puissant. Le client voit en permanence qu'il a des articles en attente. Ca cree un sentiment d'engagement - il a deja commence le processus d'achat.

Le badge est rouge par defaut dans la plupart des configurations. Le rouge attire l'oeil sans etre agressif quand il s'agit d'un petit cercle. Tu peux changer la couleur dans Modern Cart → Settings → Badge Color si le rouge jure avec ta charte graphique. Un orange vif ou la couleur d'accent de ton site fonctionne aussi.

---

**[SECTION 3 - Personnaliser l'icone]**

**[ECRAN - options d'icone Modern Cart]**

Modern Cart propose plusieurs styles d'icone.

**Panier (cart).** L'icone classique du chariot de supermarche. Universellement reconnu. C'est le choix le plus sur.

**Sac (bag).** Un sac de shopping. Plus moderne, plus "lifestyle". Adapte si ta boutique vend de la mode, des accessoires, des produits premium.

**Custom.** Selon la version, tu peux uploader ta propre icone. A utiliser uniquement si tu as un pictogramme de marque specifique. Sinon, reste sur les icones standard - tes clients les reconnaissent instantanement.

La taille de l'icone est aussi ajustable. Ni trop petite (invisible), ni trop grande (intrusive). La taille par defaut est generalement bien calibree. Ajuste si tu trouves que l'icone se perd sur ta page ou au contraire qu'elle ecrase le contenu.

---

**[SECTION 4 - Masquer l'icone sur certaines pages]**

**[ECRAN - settings Modern Cart, exclusion de pages]**

L'icone flottante a sa place partout ou le client peut acheter : pages produit, page boutique, pages de contenu, page d'accueil.

Mais il y a des pages ou elle n'a aucun sens :

- **Page checkout CartFlows** : le client est deja en train de payer. L'icone flottante est inutile voire distrayante.
- **Page de remerciement (thank you)** : la commande est passee. Le panier est vide. Pas besoin d'icone.
- **Pages legales** (mentions legales, CGV, politique de confidentialite) : on est hors contexte d'achat.

Pour masquer l'icone sur ces pages : Modern Cart → Settings → Hide on Pages. Tu entres les IDs ou les slugs des pages a exclure. Sur certaines versions, c'est une liste deroulante.

Ne masque jamais l'icone sur les pages produit, la page boutique, ou les pages de categories. C'est la que le client achete - il doit toujours avoir acces a son panier.

---

**[SECTION 5 - L'effet psychologique du rappel permanent]**

**[ECRAN - slide "L'icone flottante = rappel permanent"]**

L'icone flottante n'est pas juste un bouton. C'est un mecanisme psychologique.

Quand un client ajoute un produit a son panier et continue a naviguer, deux choses peuvent se passer. Soit il oublie qu'il a un article en attente et quitte le site. Soit il voit en permanence le badge "1" sur l'icone flottante, et ca maintient son intention d'achat active.

Le badge qui s'incremente (1, 2, 3 produits) cree aussi un effet d'accumulation. Le client voit sa "collection" grandir. Ca rend l'abandon psychologiquement plus couteux - il a deja investi du temps a choisir ces produits.

C'est pour ca que l'icone flottante ne doit jamais etre masquee sur les pages de navigation. C'est le fil rouge entre l'exploration et l'achat.

---

**[CONCLUSION - face camera]**

L'icone flottante et le badge, c'est un duo simple mais efficace. L'icone garantit l'acces permanent au panier, le badge rappelle que le processus d'achat est en cours.

Dans la prochaine lecon, on passe en version Pro avec la fonctionnalite qui a le plus d'impact sur le panier moyen : la barre de progression pour la livraison gratuite.

---

## Notes de production

- **Visuels** : icone flottante en action pendant le scroll, badge qui s'incremente, comparaison icone panier vs sac, settings exclusion de pages
- **Animation** : montrer le badge qui passe de 0 a 1 puis 2 quand le client ajoute des produits
- **Prerequis** : LA.2 et LA.3 completees
- **Transition** : enchaine sur LA.5 (barre de progression livraison gratuite - Pro)
