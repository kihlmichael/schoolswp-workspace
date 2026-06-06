# Lecon 5.2 - Creer un upsell one-click

## Metadata

- **Formation** : CartFlows Masterclass Vente (premium - FRM-007)
- **Module** : 5 - One-Click Upsells et Downsells
- **Duree cible** : 10 min (~1400 mots)
- **Type** : Video HeyGen + voix ElevenLabs
- **Objectif pedagogique** : Creer un step upsell dans CartFlows, le connecter a un produit WooCommerce, designer la page avec Gutenberg + Kadence, configurer les boutons Oui/Non, et tester le parcours complet.

---

## Script narration

**[INTRO - face camera]**

Tu as compris la theorie du upsell post-achat. Maintenant on construit. Dans cette lecon, tu vas creer ton premier upsell one-click dans CartFlows, de A a Z. A la fin, tu auras une page upsell fonctionnelle, integree dans ton funnel, avec un paiement en un clic via Stripe.

---

**[SECTION 1 - Ajouter un step Upsell dans ton flow]**

**[ECRAN - CartFlows → Flows → ton funnel]**

Ouvre ton funnel dans CartFlows. Tu as deja ta Landing Page et ton Checkout. On va inserer l'upsell juste apres le checkout, avant la Thank You Page.

Clique sur "Add New Step". Dans la liste des types, selectionne "Upsell (Offer)". CartFlows te propose des templates - tu peux en choisir un pour demarrer ou partir d'une page vierge. Je te recommande de partir d'un template pour avoir la structure de base, puis de le personnaliser.

**[ECRAN - selection du template upsell]**

Donne un nom clair a ton step : par exemple "Upsell - Coaching Premium". Valide. Le step apparait maintenant dans ton flow, entre le Checkout et la Thank You.

**[ECRAN - flow avec le step upsell visible dans l'ordre]**

Verifie l'ordre : Landing → Checkout → Upsell → Thank You. Si l'ordre n'est pas bon, glisse-depose le step a la bonne position.

---

**[SECTION 2 - Connecter un produit WooCommerce]**

**[ECRAN - parametres du step upsell → onglet Products]**

Clique sur le step Upsell pour ouvrir ses parametres. Va dans l'onglet "Products". C'est ici que tu lies un produit WooCommerce a ton upsell.

Tape le nom du produit dans le champ de recherche. Par exemple "Coaching Premium 1h". Selectionne-le. CartFlows va automatiquement recuperer le prix et les details du produit.

Tu peux aussi definir un prix special pour l'upsell - un prix reduit par rapport au prix catalogue. C'est une pratique courante : le coaching vaut 197 euros en temps normal, mais tu le proposes a 147 euros en offre exclusive post-achat. Cette remise contextuelle augmente significativement le taux d'acceptation.

**[ECRAN - champ "Offer Price" renseigne]**

Important : le produit doit deja exister dans WooCommerce. CartFlows ne cree pas de produit - il s'appuie sur ton catalogue existant.

---

**[SECTION 3 - Designer la page upsell avec Gutenberg + Kadence]**

**[ECRAN - editeur Gutenberg de la page upsell]**

Clique sur "Edit" pour ouvrir la page upsell dans l'editeur Gutenberg. C'est ici que tu construis la page que le client verra juste apres son paiement.

La structure d'une bonne page upsell est simple. Tu as besoin de cinq elements :

**1. Un titre accrocheur.** Pas "Offre speciale" - ca ne dit rien. Plutot "Accelere tes resultats avec un coaching personnalise". Le titre doit nommer le benefice, pas le produit.

**[ECRAN - bloc Kadence Advanced Heading]**

Utilise un bloc Kadence Advanced Heading. Taille H2, centre, couleur qui contraste avec le fond.

**2. Les benefices.** Pas les caracteristiques. Pas "1 heure de coaching". Plutot "Tu repars avec un plan d'action personnalise pour ton site". Utilise un bloc Kadence Icon List - trois a cinq benefices maximum.

**[ECRAN - bloc Kadence Icon List avec benefices]**

**3. Le prix.** Affiche le prix barre et le prix upsell. CartFlows fournit des shortcodes pour ca : `[cartflows_offer_product_price]` affiche le prix de l'offre. Pour le prix barre, utilise un bloc texte avec le prix catalogue raye.

**4. Les deux boutons.** C'est le coeur de la page. On les configure dans la section suivante.

**5. Un element de reassurance.** En bas de page, ajoute une ligne de texte : "Garantie 30 jours - satisfait ou rembourse" ou "Paiement securise via Stripe". Un bloc Kadence Advanced Text suffit.

---

**[SECTION 4 - Configurer les boutons Oui / Non]**

**[ECRAN - deux boutons sur la page upsell]**

Ta page upsell a deux boutons. Le premier accepte l'offre. Le second la refuse.

Pour le bouton "Oui" : utilise le shortcode CartFlows `[cartflows_offer_yes]Oui, j'en profite ![/cartflows_offer_yes]`. Ce shortcode genere un bouton qui, au clic, ajoute le produit upsell a la commande du client sans aucune re-saisie de paiement. Un clic, c'est fait.

Pour le bouton "Non" : utilise `[cartflows_offer_no]Non merci, passer cette offre[/cartflows_offer_no]`. Ce bouton fait avancer le client vers l'etape suivante du funnel - soit le downsell, soit la Thank You Page.

**[ECRAN - apercu des deux boutons stylises]**

Stylise ces boutons avec Kadence. Le bouton "Oui" doit etre le plus visible - grande taille, couleur vive (vert ou couleur principale de ta marque). Le bouton "Non" doit etre discret - texte simple, pas de fond colore, taille reduite. Tu ne caches pas le refus, mais tu guides visuellement vers l'acceptation.

Conseil de copywriting : evite les formulations negatives sur le bouton "Non". "Non merci, passer cette offre" est neutre. "Non, je ne veux pas accelerer mes resultats" est manipulateur - ne fais pas ca.

---

**[SECTION 5 - Le paiement one-click via Stripe]**

**[ECRAN - parametres Stripe dans CartFlows]**

Le paiement one-click fonctionne nativement avec Stripe. Quand le client a paye au checkout avec sa carte via Stripe, CartFlows stocke de maniere securisee les informations necessaires pour effectuer un debit supplementaire sans re-saisie.

Pour que ca fonctionne, tu dois utiliser Stripe comme passerelle de paiement sur ton checkout. Si c'est le cas, rien de plus a configurer cote upsell - CartFlows gere automatiquement la transaction.

Le client clique sur "Oui, j'en profite", Stripe debite le montant de l'upsell, et le produit est ajoute a sa commande existante. Pas de nouvelle commande - un ajout sur la meme commande. Propre.

---

**[SECTION 6 - Tester le parcours complet]**

**[ECRAN - CartFlows → Flow → bouton "Test Mode"]**

Avant de mettre en production, teste. Active le mode test de CartFlows (Settings → General → Enable Test Mode). Ce mode te permet de passer les commandes sans paiement reel.

Parcours le funnel en entier : Landing → Checkout → Upsell → Thank You. Verifie que :

- La page upsell s'affiche bien apres le paiement checkout
- Le bouton "Oui" ajoute le produit a la commande
- Le bouton "Non" redirige correctement vers l'etape suivante
- La commande dans WooCommerce contient bien le produit principal + le produit upsell (si accepte)

**[ECRAN - commande WooCommerce avec les deux produits]**

Desactive le mode test une fois que tout fonctionne.

---

**[OUTRO - face camera]**

Ton premier upsell one-click est en place. Le client paye, voit ton offre complementaire, et peut l'accepter en un clic. Pas de formulaire supplementaire, pas de friction.

Dans la prochaine lecon, on ajoute le filet de securite : le downsell - l'offre de repli pour ceux qui refusent l'upsell.

---

## Notes de production

- **Visuels** : captures CartFlows (ajout step, products, boutons), editeur Gutenberg avec blocs Kadence, commande WooCommerce
- **Shortcodes a afficher** : `[cartflows_offer_yes]`, `[cartflows_offer_no]`, `[cartflows_offer_product_price]`
- **Ton** : tutoriel pas-a-pas, rythme soutenu
- **Duree estimee** : ~10 min a debit normal
- **Transition** : enchaine sur L5.3 (downsell)
