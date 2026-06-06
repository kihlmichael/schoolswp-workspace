# Lecon A.3 - Design du panier lateral : couleurs, position, animation

## Metadata

- **Formation** : CartFlows Add-ons (premium - FRM-008)
- **Module** : A - Modern Cart
- **Duree cible** : 8 min (~1100 mots)
- **Type** : Video HeyGen + voix ElevenLabs
- **Objectif pedagogique** : Maitriser les options de design de Modern Cart (couleurs, position, animation, largeur) et optimiser le rendu visuel sur desktop et mobile.

---

## Script narration

**[INTRO - face camera]**

Ton side cart est installe et fonctionnel. Maintenant, on va le rendre beau. Pas "beau" au sens decoratif - beau au sens professionnel. Un side cart qui inspire confiance, qui s'integre parfaitement a ton site, et qui donne envie de passer commande.

Dans cette lecon, on couvre toutes les options de design de Modern Cart : couleurs, position, animation d'ouverture, largeur, et rendu responsive.

---

**[SECTION 1 - Les options de couleurs en detail]**

**[ECRAN - Modern Cart → Settings → Design]**

Va dans Modern Cart, puis Settings, onglet Design ou Apparence selon ta version. Tu retrouves les reglages de couleurs qu'on a survoles dans le wizard, mais avec plus de granularite.

**Fond du panneau.** Blanc pur (#FFFFFF) ou un gris tres clair (#F9F9F9). Le fond doit rester neutre - c'est le contenu (produits, prix, boutons) qui doit ressortir. Evite les fonds colores sauf si ta charte graphique l'impose vraiment.

**Couleur des textes.** Noir (#000000) ou gris fonce (#333333) pour les noms de produits et les prix. Le contraste avec le fond doit etre maximal. C'est une question d'accessibilite autant que d'esthetique.

**Bouton principal (Checkout / Passer commande).** C'est l'element le plus important visuellement. Utilise ta couleur d'action - la meme que tes boutons "Ajouter au panier" sur les pages produit. Si c'est un bleu vif, un orange, un vert : reprends exactement la meme couleur. La coherence cree un reflexe chez le client.

**Bouton secondaire (Continuer les achats).** Moins visible que le bouton principal. Un simple lien texte ou un bouton avec bordure (outline) sans fond colore. Tu veux que l'oeil du client aille naturellement vers "Passer commande", pas vers "Continuer les achats".

**Separateurs et bordures.** Un gris leger pour les lignes entre chaque produit. Discret mais present - ca structure visuellement la liste.

**Header du side cart.** Le titre en haut du panneau ("Ton panier", "Mon panier", ou le texte de ton choix). Mets-le en gras, taille lisible. Certains themes ajoutent automatiquement un style - verifie que ca ne cree pas de doublon.

---

**[SECTION 2 - Position : droite vs gauche]**

**[ECRAN - comparaison side cart droite vs gauche]**

On en a parle dans le wizard : le side cart peut s'ouvrir a droite ou a gauche.

**Droite (recommande).** C'est le standard e-commerce. Amazon, Shopify, la majorite des boutiques premium utilisent un panneau a droite. Le regard occidental se deplace de gauche a droite - le panneau a droite est la destination naturelle apres avoir parcouru la page.

**Gauche.** A envisager uniquement si ton menu principal ou ton panier dans le header est positionne a gauche. Dans ce cas, l'ouverture a gauche cree une continuite visuelle. Sinon, reste a droite.

Pour changer : Modern Cart → Settings → Position → Right / Left. Un clic, c'est fait.

---

**[SECTION 3 - Animation d'ouverture]**

**[ECRAN - demonstration animation slide vs fade]**

L'animation, c'est le mouvement du panneau quand il s'ouvre.

**Slide (glissement).** Le panneau glisse depuis le bord de l'ecran. C'est l'option la plus naturelle et la plus utilisee. Le client comprend immediatement d'ou vient le panneau et comment le fermer.

**Fade (fondu).** Le panneau apparait en fondu. Plus discret, moins "physique". Ca fonctionne, mais l'effet slide donne une meilleure sensation de controle a l'utilisateur - il voit le panneau arriver et sait qu'il peut le repousser.

Mon conseil : slide. C'est le comportement attendu sur un side cart. Le fade peut parfois donner l'impression d'un popup, ce qui declenche un reflexe de fermeture chez certains utilisateurs.

---

**[SECTION 4 - Largeur du panneau]**

**[ECRAN - side cart largeur defaut vs custom]**

La largeur par defaut de Modern Cart est generalement autour de 350-400 pixels. C'est suffisant pour la majorite des cas.

Quand elargir ? Si tes noms de produits sont longs et qu'ils sont tronques. Si tu affiches les variantes (taille, couleur) et que ca prend de la place. Ou si tu actives les recommandations in-cart en version Pro - il faut de la place pour le carrousel.

Quand ne pas elargir ? Sur un ecran desktop standard, un panneau de 450+ pixels commence a couvrir une partie significative du contenu. Le client perd le contexte de la page derriere. Reste en dessous de 420 pixels sauf besoin specifique.

Pour modifier : Modern Cart → Settings → Width. Tu entres la valeur en pixels.

---

**[SECTION 5 - L'overlay (fond assombri)]**

**[ECRAN - side cart avec et sans overlay]**

Quand le side cart s'ouvre, le reste de la page est couvert par un overlay - un fond semi-transparent gris ou noir. C'est le meme principe que les popups.

L'overlay a deux roles : focaliser l'attention sur le side cart, et servir de zone de clic pour fermer le panneau (le client clique en dehors, le panneau se ferme).

Tu peux ajuster l'opacite de l'overlay. Trop opaque (noir a 80%), ca fait agressif. Trop transparent (10%), le client ne comprend pas que le side cart est au premier plan. Un bon compromis : entre 30% et 50% d'opacite.

---

**[SECTION 6 - Verification responsive mobile]**

**[ECRAN - side cart sur mobile, outil responsive navigateur]**

Le test mobile est non negociable. Plus de la moitie du trafic e-commerce passe par mobile.

Ouvre ton navigateur, appuie sur F12, active le mode responsive. Teste sur iPhone (375px de large) et sur tablette (768px).

Sur mobile, le side cart prend generalement 100% de la largeur de l'ecran. Verifie ces points :

- Les boutons + et - de quantite sont assez grands pour un doigt (44px minimum)
- Le bouton "Passer commande" est visible sans scroller
- Le X de fermeture est accessible et ne chevauche pas d'autres elements
- Les noms de produits ne sont pas tronques au point d'etre illisibles

Si quelque chose cloche, ajuste la largeur ou la taille des polices dans les settings Modern Cart. La plupart des ajustements responsive sont automatiques, mais verifie quand meme.

---

**[CONCLUSION - face camera]**

Ton side cart est maintenant design et coherent avec ta charte graphique. Position a droite, animation slide, couleurs alignees sur ton theme, responsive valide.

Dans la prochaine lecon, on va se concentrer sur l'icone flottante et le badge produit - les elements qui rappellent en permanence au client qu'il a quelque chose dans son panier.

---

## Notes de production

- **Visuels** : panneau settings Modern Cart, comparaison droite/gauche, demo animation slide vs fade, vue mobile
- **Conseil montage** : split-screen pour les comparaisons (droite vs gauche, slide vs fade, largeur defaut vs custom)
- **Prerequis** : LA.2 completee (Modern Cart installe et fonctionnel)
- **Transition** : enchaine sur LA.4 (icone flottante et badge)
