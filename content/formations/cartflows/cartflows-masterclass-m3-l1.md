# Lecon 3.1 — Checkout Takeover : remplacer le checkout WooCommerce

## Metadata

- **Formation** : CartFlows Masterclass Vente (premium — FRM-007)
- **Module** : 3 — Checkout optimise
- **Duree cible** : 8 min (~1100 mots)
- **Type** : Video HeyGen + voix ElevenLabs
- **Objectif pedagogique** : Comprendre le Checkout Takeover de CartFlows — ce qu'il remplace, quand l'activer, quand le laisser desactive. Savoir faire le bon choix selon sa configuration WooCommerce.

---

## Script narration

**[INTRO — face camera]**

Le checkout WooCommerce par defaut, c'est une page generique. Memes champs, meme design, meme structure pour tout le monde. Que tu vendes une formation en ligne ou du materiel scolaire, tu obtiens le meme formulaire sans ame.

Le probleme : ce checkout n'est pas concu pour convertir. Il est concu pour fonctionner. C'est une difference enorme. Un checkout qui fonctionne affiche des champs et prend un paiement. Un checkout qui convertit reduit les frictions, rassure le client et le guide vers la validation.

CartFlows propose une solution radicale : le Checkout Takeover. Et c'est ce qu'on va configurer ensemble dans cette lecon.

---

**[SECTION 1 — Le probleme du checkout WooCommerce standard]**

**[ECRAN — capture du checkout WooCommerce natif]**

Regarde le checkout WooCommerce de base. Tu as un formulaire long, des champs que personne ne remplit (le champ "Entreprise" pour un particulier, par exemple), un design qui depend entierement de ton theme, et zero element de reassurance.

Pas de temoignages. Pas de recapitulatif visuel du produit. Pas de garantie visible. Le client arrive sur cette page et il voit un formulaire administratif. C'est l'exact oppose de ce qu'il faut pour conclure une vente.

Avec Kadence comme theme, le rendu est correct. Mais "correct" ne suffit pas. Un checkout doit etre optimise — pas juste propre.

---

**[SECTION 2 — Qu'est-ce que le Checkout Takeover]**

**[ECRAN — schema avant/apres : checkout WooCommerce vs checkout CartFlows]**

Le Checkout Takeover, c'est un interrupteur global. Quand tu l'actives, CartFlows remplace tous les checkouts de ton site. Pas seulement ceux de tes funnels — tous.

Concretement, chaque fois qu'un visiteur arrive sur `/checkout/` — que ce soit via un funnel CartFlows, un bouton "Ajouter au panier" classique, ou un lien direct — il voit le design CartFlows au lieu du checkout WooCommerce natif.

C'est un remplacement total. CartFlows prend le controle de la page checkout globale de WooCommerce et y applique son propre template, ses propres styles, ses propres options d'optimisation.

---

**[SECTION 3 — Activer le Checkout Takeover]**

**[ECRAN — CartFlows → Settings → Checkout]**

L'activation se fait en trois clics. Va dans CartFlows, puis Settings, puis l'onglet Checkout.

Tu vas voir l'option "Enable Checkout Takeover" — un simple toggle. Active-le.

**[ECRAN — toggle active]**

Une fois active, CartFlows te demande de selectionner un flow par defaut. C'est le funnel dont le design checkout sera utilise comme template global. Choisis celui que tu as concu pour etre ton checkout principal.

Sauvegarde. C'est fait. A partir de maintenant, toute URL `/checkout/` sur ton site utilise le design CartFlows.

---

**[SECTION 4 — Ce qui change concretement]**

**[ECRAN — navigation sur le site : ajout panier classique → arrivee sur checkout CartFlows]**

Voyons ce que ca donne en pratique. Je vais sur la boutique, j'ajoute un produit au panier de facon classique — pas via un funnel. Je clique sur "Commander". Et la, au lieu du checkout WooCommerce brut, j'arrive sur le checkout CartFlows.

Le design est propre. Les champs sont organises. Le recapitulatif du produit est visible. Les elements de reassurance que tu as configures dans ton flow sont la — temoignages, garantie, logos de paiement.

Toute la personnalisation que tu as faite dans l'editeur CartFlows s'applique maintenant a l'ensemble de ton site. Un seul design, partout.

---

**[SECTION 5 — Quand utiliser le Checkout Takeover]**

**[ECRAN — face camera]**

Le Checkout Takeover est ideal dans deux cas.

Premier cas : tu as un seul produit ou une offre principale. Tu vends une formation, un service, un abonnement. Un seul checkout, un seul design, une seule experience. Le Takeover simplifie tout.

Deuxieme cas : tu veux une experience coherente sur tout ton site. Meme si tu as plusieurs produits, tu veux que chaque achat passe par le meme checkout optimise. Le branding est uniforme, les clients ne sont jamais desorientes.

---

**[SECTION 6 — Quand NE PAS utiliser le Checkout Takeover]**

**[ECRAN — schema : plusieurs funnels avec des checkouts differents]**

Le Takeover n'est pas toujours la bonne option.

Si tu as plusieurs funnels avec des checkouts specifiques — par exemple un funnel pour ta formation avec un checkout en deux etapes, un autre pour ton ebook avec un checkout simplifie, et un troisieme pour du coaching avec un formulaire personnalise — le Takeover va ecraser tout ca avec un seul design.

Les funnels CartFlows gardent leur propre checkout quand le client passe par le funnel. Mais si quelqu'un arrive directement sur `/checkout/`, il verra le checkout du Takeover, pas celui du funnel specifique.

Donc si tu comptes sur des designs de checkout differents selon les produits, laisse le Takeover desactive. Chaque funnel gerera son propre checkout independamment.

---

**[SECTION 7 — Conseil pratique]**

**[ECRAN — face camera]**

Mon conseil : active le Checkout Takeover si tu as un seul produit ou une offre principale. Ca te garantit un checkout optimise partout, sans risque qu'un visiteur tombe sur le formulaire WooCommerce generique.

Desactive-le si tu as plusieurs funnels avec des designs differents. Dans ce cas, laisse chaque funnel gerer son propre checkout et assure-toi que les visiteurs passent toujours par le funnel — jamais par le checkout direct.

Et dans tous les cas, teste. Ajoute un produit au panier manuellement, va sur `/checkout/`, et verifie que le rendu correspond a ce que tu attends. C'est un controle qui prend 30 secondes et qui t'evite de mauvaises surprises.

---

**[OUTRO — face camera]**

Le Checkout Takeover, c'est un outil puissant mais a utiliser en connaissance de cause. Active ou desactive, l'important c'est que tu choisisses en fonction de ta strategie de vente, pas par defaut.

Dans la prochaine lecon, on passe au multi-step checkout — comment decouper ton formulaire en plusieurs etapes pour reduire l'abandon.

---

## Notes de production

- **Captures d'ecran necessaires** : checkout WooCommerce natif, page CartFlows Settings → Checkout, toggle Checkout Takeover, flow par defaut, demo navigation boutique → checkout
- **Schema** : avant/apres checkout WooCommerce vs CartFlows, schema multi-funnels avec checkouts differents
- **Timing** : intro (1 min) → probleme checkout standard (1 min) → explication Takeover (1 min) → activation (1.5 min) → demo concrete (1 min) → quand utiliser (1 min) → quand ne pas utiliser (1 min) → outro (0.5 min)
- **Ton** : direct, pas de survente — le Takeover n'est pas toujours la bonne option, et on le dit clairement
