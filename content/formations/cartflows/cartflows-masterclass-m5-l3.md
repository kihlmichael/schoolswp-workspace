# Lecon 5.3 — Creer un downsell (offre de repli)

## Metadata

- **Formation** : CartFlows Masterclass Vente (premium — FRM-007)
- **Module** : 5 — One-Click Upsells et Downsells
- **Duree cible** : 8 min (~1100 mots)
- **Type** : Video HeyGen + voix ElevenLabs
- **Objectif pedagogique** : Comprendre le concept de downsell, creer un step downsell dans CartFlows, le positionner correctement dans le flow, et designer une offre de repli coherente.

---

## Script narration

**[INTRO — face camera]**

Le client a refuse ton upsell. Il a clique sur "Non merci". C'est fini ? Non. Tu as encore une carte a jouer : le downsell. Une offre de repli, a prix reduit, qui te donne une seconde chance de maximiser la valeur de cette commande.

---

**[SECTION 1 — Qu'est-ce qu'un downsell]**

**[ECRAN — schema du parcours : Checkout → Upsell (Non) → Downsell]**

Le downsell est une offre alternative proposee uniquement quand le client refuse l'upsell. Si le client accepte l'upsell, il ne voit jamais le downsell — il passe directement a la Thank You Page.

La logique est simple : le client a dit non a ton offre premium. Peut-etre que le prix etait trop eleve. Peut-etre que l'offre ne correspondait pas exactement a son besoin. Le downsell repond a cette objection en proposant une version plus accessible.

C'est un filet de securite pour ton chiffre d'affaires. Au lieu de passer de 0 a 0 apres un refus, tu recuperes une partie de la valeur avec une offre plus legere.

---

**[SECTION 2 — La regle : version allegee, pas produit different]**

**[ECRAN — exemples bon downsell vs mauvais downsell]**

Regle fondamentale : ton downsell doit etre une version allegee de ton upsell. Pas un produit completement different. Le client a montre un interet pour le type de produit propose (meme s'il a refuse le prix) — reste dans la meme thematique.

Exemples concrets :

- Upsell refuse : coaching 1h a 97 euros → Downsell : mini-coaching 30 min a 47 euros
- Upsell refuse : formation video complete a 197 euros → Downsell : acces aux 3 premiers modules a 67 euros
- Upsell refuse : licence multi-sites a 149 euros → Downsell : licence 3 sites a 79 euros
- Upsell refuse : pack templates premium a 47 euros → Downsell : 1 template au choix a 17 euros

Le point commun : c'est le meme type de produit, en version reduite. Moins de contenu, moins de temps, moins de sites — mais le meme type de valeur.

---

**[SECTION 3 — Ajouter un step Downsell dans CartFlows]**

**[ECRAN — CartFlows → Flow → Add New Step]**

Ouvre ton funnel. Tu as maintenant : Landing → Checkout → Upsell → Thank You. On va inserer le downsell entre l'upsell et la Thank You.

Clique sur "Add New Step". Selectionne "Downsell (Offer)". Choisis un template ou pars d'une page vierge. Nomme le step clairement : "Downsell — Mini-Coaching 30min".

**[ECRAN — flow mis a jour avec le downsell]**

Ton flow ressemble maintenant a ca : Landing → Checkout → Upsell → Downsell → Thank You. CartFlows gere automatiquement le routage : si le client accepte l'upsell, il saute le downsell et va directement a la Thank You. S'il refuse, il voit le downsell.

C'est la magie du systeme : tu ne configures pas de regles conditionnelles complexes. CartFlows sait que le downsell n'apparait que sur refus de l'upsell.

---

**[SECTION 4 — Configurer le produit et designer la page]**

**[ECRAN — parametres du step downsell → onglet Products]**

Comme pour l'upsell, connecte un produit WooCommerce au downsell. Va dans les parametres du step, onglet "Products", et selectionne ton produit de repli.

Definis le prix d'offre si necessaire. Rappel : le downsell doit etre nettement moins cher que l'upsell. L'ecart de prix doit etre evident au premier coup d'oeil.

**[ECRAN — editeur Gutenberg de la page downsell]**

Pour le design de la page, reprends la meme structure que l'upsell mais adapte le message :

- **Titre** : reconnaissez le refus et repositionne l'offre. "Pas pret pour le coaching complet ? Voici une alternative."
- **Benefices** : les memes que l'upsell, en version condensee
- **Prix** : mets en avant l'ecart. "Au lieu de 97 euros, decouvre le mini-coaching a seulement 47 euros."
- **Boutons** : memes shortcodes. `[cartflows_offer_yes]Oui, 47 euros ca me va ![/cartflows_offer_yes]` et `[cartflows_offer_no]Non merci, finaliser ma commande[/cartflows_offer_no]`

Stylise avec Kadence comme pour l'upsell. Le bouton "Oui" visible et colore, le "Non" discret.

---

**[SECTION 5 — Le flux complet]**

**[ECRAN — schema du flux avec les 3 chemins]**

Recapitulons les chemins possibles a ce stade :

1. Checkout → Upsell OUI → Thank You (le client a tout accepte)
2. Checkout → Upsell NON → Downsell OUI → Thank You (le client a pris l'offre de repli)
3. Checkout → Upsell NON → Downsell NON → Thank You (le client n'a rien pris en plus)

Dans les trois cas, le client arrive sur la Thank You Page. La difference, c'est le montant total de sa commande. Et toi, tu as maximise tes chances sur chaque scenario.

---

**[OUTRO — face camera]**

Le downsell est ton filet de securite. Il transforme un "non" en une seconde opportunite. Et comme pour l'upsell, tout se fait en un clic cote client — zero friction.

Dans la prochaine lecon, on va chainer tout ca proprement : upsell, downsell, et Thank You Page dans un parcours fluide avec le Canvas Mode de CartFlows.

---

## Notes de production

- **Visuels** : schema parcours avec branchement upsell/downsell, captures CartFlows (ajout step, products), editeur Gutenberg
- **Shortcodes a afficher** : `[cartflows_offer_yes]`, `[cartflows_offer_no]`
- **Ton** : pratique et methodique
- **Duree estimee** : ~8 min a debit normal
- **Transition** : enchaine sur L5.4 (chainage upsell → downsell → thank you)
