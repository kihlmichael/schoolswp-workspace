# Lecon 5.4 - Site avec funnels : ZipWP + CartFlows

## Metadata

- **Formation** : ZipWP Masterclass Business (FRM-010)
- **Module** : 5 - Sites business avec ZipWP
- **Lecon** : 4/8
- **Duree cible** : 12 min
- **Objectif pedagogique** : Creer un funnel de vente complet avec CartFlows sur un site ZipWP - de la landing page au thank you, en passant par le checkout, l'order bump et l'upsell.
- **Production** : HeyGen (avatar) + voix ElevenLabs (FR)

---

## Script narration

[INTRO]

Un site, c'est une vitrine. Un funnel, c'est une machine a vendre. Et avec CartFlows sur ton site ZipWP, tu combines les deux : un site professionnel qui attire les visiteurs, et un entonnoir de conversion qui transforme ces visiteurs en acheteurs.

CartFlows, c'est le funnel builder de reference pour WordPress. Et comme c'est un produit partenaire de l'ecosysteme Brainstorm Force, il s'integre parfaitement avec Astra et Spectra. On installe, on configure, et on construit un funnel complet aujourd'hui.

---

[SECTION 1 - Installer CartFlows sur le site ZipWP]

Premiere etape : genere ton site avec ZipWP. Un site e-commerce ou un site de formation - le type de site ou tu vends quelque chose. CartFlows a besoin de WooCommerce pour fonctionner, donc assure-toi que WooCommerce est installe et configure (on l'a vu dans la lecon precedente).

Installe CartFlows : Extensions → Ajouter → "CartFlows" → Installer → Activer. Si tu as la licence Pro, uploade le fichier zip de CartFlows Pro ensuite.

La version gratuite permet de creer des funnels basiques - landing page, checkout, thank you. La version Pro ajoute les fonctionnalites qui font la difference : order bumps, upsells, downsells, A/B testing, et les templates premium.

Apres activation, CartFlows ajoute un menu dans ton dashboard WordPress. Va dans CartFlows → Settings pour configurer les bases : active le "Modern Checkout" - c'est le checkout optimise CartFlows qui remplace le checkout WooCommerce par defaut. La difference est visible immediatement : le checkout devient plus propre, plus rapide, et convertit mieux.

---

[SECTION 2 - La structure d'un funnel de vente]

Un funnel CartFlows a 5 etapes. Chacune a un objectif precis.

Etape 1 - Landing Page : c'est le point d'entree. Le visiteur arrive ici depuis une pub, un email, ou un lien sur ton site. La landing page presente l'offre, les benefices, et un seul CTA : "Acheter maintenant" ou "S'inscrire". Pas de menu, pas de footer, pas de distraction.

Etape 2 - Checkout : le formulaire de commande. Le visiteur entre ses informations et son moyen de paiement. CartFlows optimise cette page avec un design epure et des champs pre-remplis si possible.

Etape 3 - Order Bump : juste avant de payer, le visiteur voit une offre complementaire. Une case a cocher avec un texte du type "Ajoute le pack de templates bonus pour seulement 17 euros". L'order bump est la fonctionnalite la plus rentable de CartFlows - le taux d'acceptation moyen est entre 15 et 30%.

Etape 4 - Upsell : apres le paiement, avant la page de confirmation, le visiteur voit une offre premium. "Tu viens d'acheter la formation de base. Ajoute l'accompagnement premium pour 97 euros - paiement en un clic, pas besoin de re-saisir tes informations." Si le visiteur refuse, tu peux proposer un downsell - la meme offre a un prix reduit.

Etape 5 - Thank You : la page de remerciement. Confirmation de commande, recap de l'achat, et prochaines etapes. C'est aussi l'endroit ideal pour inviter l'acheteur a rejoindre ta communaute, suivre tes reseaux, ou partager son achat.

---

[SECTION 3 - Creer le funnel pas a pas]

Dans le dashboard CartFlows, clique sur "Flows" → "Add New". CartFlows propose des templates - choisis-en un adapte a ton offre ou pars de zero.

Cree la Landing Page : ajoute une etape "Landing", ouvre-la dans l'editeur. Utilise les blocs Spectra pour construire ta page. Hero section avec le titre de l'offre et un visuel. Section probleme - le pain point de ton audience. Section solution - comment ton produit resout ce probleme. Benefices - 3 a 5 avantages cles. Temoignages. CTA - le bouton qui envoie vers le checkout.

Cree le Checkout : ajoute une etape "Checkout". CartFlows genere automatiquement un formulaire de commande lie a un produit WooCommerce. Selectionne le produit. Personnalise le design - titre, description, logo de confiance (badges de paiement securise).

Configure l'Order Bump : dans les parametres du checkout, active "Order Bump". Choisis le produit complementaire, ecris le texte d'accroche, definis le prix. Conseil : le prix de l'order bump doit etre entre 10 et 30% du prix du produit principal. Un produit a 47 euros → un order bump entre 7 et 15 euros.

Cree l'Upsell : ajoute une etape "Upsell". Selectionne le produit premium. Ecris un texte court et percutant - le visiteur vient de sortir sa carte, il est en mode achat. Sois direct. Si tu proposes un downsell, ajoute une etape "Downsell" juste apres.

Cree le Thank You : ajoute une etape "Thank You". Personnalise avec un message de remerciement, le recap de la commande, et un CTA secondaire (rejoindre la communaute, telecharger un bonus).

---

[SECTION 4 - Connecter CartFlows au site ZipWP]

Ton funnel est cree, mais comment les visiteurs de ton site ZipWP y accedent ?

Le flux est le suivant : le visiteur navigue sur ton site ZipWP - il decouvre tes pages, ton contenu, ton positionnement. A un moment, il clique sur un bouton "Acheter", "S'inscrire", ou "Decouvrir l'offre". Ce bouton pointe vers la landing page de ton funnel CartFlows.

Concretement : copie l'URL de ta landing page CartFlows. Dans ton site ZipWP, edite le bouton CTA de ta page d'accueil, ta page services, ou ta page de vente Spectra. Colle l'URL du funnel comme lien du bouton.

Tu peux aussi integrer le checkout CartFlows directement dans une page existante avec un shortcode. Mais le plus propre, c'est de garder le funnel sur ses propres pages - sans menu ni footer - pour maximiser la conversion.

Le flux complet devient : Visiteur arrive sur le site ZipWP → Decouvre ton offre → Clique sur "Acheter" → Entre dans le funnel CartFlows → Landing → Checkout + Order Bump → Upsell → Thank You → Conversion optimisee.

Le conseil schoolsWP : ZipWP genere le site. CartFlows genere le revenu.

---

[OUTRO]

Ton funnel est en place. Landing page, checkout optimise, order bump pour augmenter le panier moyen, upsell pour maximiser la valeur par client, et thank you page pour fideler.

C'est cette combinaison site + funnel qui fait la difference entre un site qui "existe" et un site qui genere du chiffre d'affaires.

Dans la prochaine lecon, on ajoute la couche CRM. ZipWP + FluentCRM pour capturer les emails et ne plus jamais perdre un visiteur.

---

## Notes de production

### Captures d'ecran suggerees

1. **CartFlows Dashboard** - Vue des flows avec les etapes du funnel
2. **Modern Checkout** - Comparaison avant/apres (checkout WooCommerce vs CartFlows)
3. **Order Bump** - Case a cocher avec l'offre complementaire sur le checkout
4. **Upsell Page** - Page d'upsell avec offre premium et bouton one-click
5. **Schema funnel** - Diagramme Landing → Checkout → Order Bump → Upsell → Thank You
6. **Bouton CTA** - Lien du bouton site ZipWP pointant vers le funnel CartFlows

### Transitions

- Intro → Section 1 : installation CartFlows depuis le dashboard WP
- Section 1 → Section 2 : schema visuel des 5 etapes du funnel
- Section 2 → Section 3 : retour a l'editeur, creation etape par etape
- Section 3 → Section 4 : vue du site ZipWP, connexion au funnel
- Section 4 → Outro : animation du flux complet visiteur → conversion

### Notes HeyGen / ElevenLabs

- Ton business et direct - on parle argent et conversion
- Section 2 (structure) : rythme pose, bien expliquer chaque etape du funnel
- Section 3 (creation) : rythme tutoriel, montrer les manipulations
- Insister sur "ZipWP genere le site, CartFlows genere le revenu" - punchline de la lecon
