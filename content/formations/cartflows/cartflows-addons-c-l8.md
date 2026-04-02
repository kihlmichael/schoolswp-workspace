# Lecon C.8 — Remises par quantite : paliers degressifs

## Metadata

- **Formation** : CartFlows Add-ons (premium — FRM-008)
- **Module** : C — Power Coupons
- **Duree cible** : 8 min (~1100 mots)
- **Type** : Video HeyGen + voix ElevenLabs
- **Objectif pedagogique** : Configurer des paliers de prix degressifs avec Power Coupons, afficher le tableau des paliers sur la page produit, et comprendre pourquoi cette strategie augmente le volume par commande.

---

## Script narration

**[INTRO — face camera]**

Plus le client achete, moins il paye par unite. C'est le principe des paliers degressifs, et c'est un mecanisme que tu retrouves partout — du grossiste au supermarche.

En e-commerce, les paliers degressifs ont un effet direct : le client achete plus en une seule commande. Au lieu de prendre 2 sachets de cafe, il en prend 6 parce que le prix unitaire passe de 12€ a 8€. Tu augmentes le volume et le montant de la commande en meme temps.

Power Coupons te permet de creer ces paliers directement dans WooCommerce. On va configurer ca ensemble.

---

**[SECTION 1 — Le concept des paliers degressifs]**

**[ECRAN — slide tableau de paliers]**

Le principe est simple. Tu definis des seuils de quantite avec un prix unitaire different pour chaque seuil.

Prenons l'exemple du cafe. Un sachet a 12€. Le client qui en prend un paye 12€. Rien de special.

A partir de 3 sachets : 10€ l'unite au lieu de 12€. Le client qui en prend 3 paye 30€ au lieu de 36€. Il economise 6€.

A partir de 6 sachets : 8€ l'unite au lieu de 12€. Le client qui en prend 6 paye 48€ au lieu de 72€. Il economise 24€.

Le client voit l'economie augmenter a chaque palier. La question n'est plus "est-ce que j'achete ?", c'est "combien j'achete ?". Tu deplaces la decision d'achat vers une decision de volume.

---

**[SECTION 2 — Configurer les paliers dans Power Coupons]**

**[ECRAN — WordPress admin → Power Coupons → Quantity Discount]**

Dans Power Coupons, va dans la section "Quantity Discount" ou "Remises par quantite".

Selectionne le produit ou la categorie de produits concernes. Pour notre exemple, on selectionne le produit "Cafe Colombie 250g".

Ajoute les paliers.

Palier 1 : quantite 1 a 2. Remise : 0%. Prix normal.

Palier 2 : quantite 3 a 5. Remise : -17% (equivalent de 10€ au lieu de 12€).

Palier 3 : quantite 6 et plus. Remise : -33% (equivalent de 8€ au lieu de 12€).

Tu peux definir la remise en pourcentage ou en montant fixe par unite. Le pourcentage est plus flexible — si tu changes le prix de base, les paliers s'ajustent automatiquement.

Active l'option "Auto Apply" pour que la remise s'applique automatiquement quand le client atteint le palier. Pas de code a taper.

---

**[SECTION 3 — Afficher le tableau des paliers]**

**[ECRAN — page produit front-end avec tableau de paliers]**

Le point crucial : le client doit voir les paliers avant d'ajouter au panier. S'il ne sait pas que le prix baisse a partir de 3 unites, il ne va pas en commander 3.

Power Coupons affiche un tableau des paliers directement sur la page produit. Le tableau montre la quantite, le prix unitaire, et l'economie realisee.

| Quantite | Prix unitaire | Economie |
|----------|--------------|----------|
| 1-2 | 12€ | — |
| 3-5 | 10€ | -17% |
| 6+ | 8€ | -33% |

Ce tableau est genere automatiquement par Power Coupons. Tu peux personnaliser son emplacement sur la page produit — au-dessus du bouton "Ajouter au panier", c'est le meilleur endroit.

Dans le checkout et dans le panier, le client voit le prix ajuste. S'il a 4 sachets dans le panier, le prix unitaire affiche est 10€, avec une mention de l'economie realisee.

Affiche toujours le tableau des paliers sur la page produit. Le client doit voir l'economie avant d'ajouter au panier. C'est ce qui le pousse a augmenter la quantite.

---

**[SECTION 4 — Cas pratique et strategie]**

**[ECRAN — slide strategie paliers]**

Le cas du cafe est un classique. Mais les paliers degressifs fonctionnent pour beaucoup de types de produits.

Consommables : cafe, cosmetiques, supplements. Le client sait qu'il va en avoir besoin regulierement. Un prix degressif l'incite a stocker.

Produits a offrir : t-shirts, mugs, accessoires. Le client qui achete un cadeau pour une personne peut en acheter trois pour trois personnes si le prix unitaire baisse.

Produits numeriques : licences, templates, formations. Le cout marginal est quasi nul. Tu peux etre tres genereux sur les paliers sans impacter ta marge.

La cle : choisis le bon ecart entre les paliers. Si le palier 1 est a 12€ et le palier 2 a 11.50€, la difference est trop faible pour motiver un changement de comportement. Si le palier 2 est a 8€, la difference est visible et incitative. Vise une remise de 15-20% par palier pour que l'effet soit perceptible.

---

**[SECTION 5 — Power Coupons vs les plugins de volume discount]**

**[ECRAN — slide comparaison]**

Il existe des plugins dedies aux remises par quantite sur WordPress.org. Pourquoi utiliser Power Coupons plutot qu'un plugin separe ?

L'integration native. Power Coupons est dans le meme ecosysteme que CartFlows et Modern Cart. Les paliers fonctionnent avec l'auto-application, avec les conditions avancees, avec le side cart. Un plugin separe ne communique pas avec le reste de ta stack promotionnelle.

La centralisation. Tous tes coupons — auto-apply, BOGO, fidelite, quantite — sont geres au meme endroit. Un seul plugin, une seule interface, un seul systeme de conditions.

Moins de plugins. Chaque plugin supplementaire ajoute du poids, des risques de conflit, et de la maintenance. Si tu peux tout faire dans Power Coupons, tu evites un plugin de plus.

---

**[CONCLUSION — face camera et recap Module C]**

Tu as configure des paliers degressifs qui poussent le client a acheter en volume. Le tableau des paliers sur la page produit, combine a l'auto-application, fait tout le travail.

Et avec ca, on termine le Module C — Power Coupons. On a couvert les six grandes fonctionnalites : auto-application, conditions avancees, BOGO, livraison gratuite conditionnelle, programme de fidelite, et remises par quantite.

On fait aussi le bilan de la formation complete CartFlows Add-ons. En trois modules, tu as installe et configure Modern Cart pour le side cart et l'experience panier, Cart Abandonment Recovery pour recuperer les ventes perdues, et Power Coupons pour des promotions intelligentes qui augmentent le panier moyen et la fidelisation.

Ces trois plugins, c'est un systeme complet. Modern Cart reduit la friction. Cart Abandonment Recovery recupere les abandons. Power Coupons augmente l'AOV et la retention. Ensemble, ils couvrent tout le parcours d'achat — de la navigation au rachat.

Merci d'avoir suivi cette formation. Mets en place ce que tu as appris, mesure les resultats, et ajuste. Les outils sont la — c'est l'execution qui fait la difference.

---

## Notes de production

- **Visuels** : tableau de paliers (cafe), captures configuration Quantity Discount dans Power Coupons, page produit front-end avec tableau des paliers, slide comparaison plugins, slide recap Module C et formation complete
- **Donnees** : impact paliers degressifs sur volume commande, ecart optimal entre paliers (15-20%)
- **Transition** : fin du Module C et de la formation CartFlows Add-ons (FRM-008)
