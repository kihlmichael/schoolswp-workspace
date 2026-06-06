# Lecon 8.8 - Cas pratique : funnel e-commerce produit physique FR

## Metadata

- **Formation** : CartFlows Masterclass Vente (premium - FRM-007)
- **Module** : 8 - Ecosysteme et automatisation
- **Duree cible** : 12 min (~1500 mots)
- **Type** : Video HeyGen + voix ElevenLabs
- **Objectif pedagogique** : Construire un funnel CartFlows complet pour une boutique e-commerce francaise avec produit physique. Integrer bump, upsell, downsell, tracking (Pixel + GA4) et relance panier abandonne. Calculer l'impact sur l'AOV.

---

## Script narration

**[INTRO - face camera]**

On change completement de contexte. Jusqu'ici, on a parle de formations, de contenu numerique, de prestations. Mais CartFlows fonctionne aussi parfaitement pour l'e-commerce physique. Et c'est la que l'impact sur le chiffre d'affaires est souvent le plus spectaculaire.

Dans cette lecon, on construit un funnel complet pour une boutique WooCommerce francaise. Le produit : un coffret degustation cafe a 39 euros. On va ajouter un bump, un upsell, un downsell, le tracking, et la relance panier abandonne. Et on va calculer les chiffres.

---

**[SECTION 1 - Le produit et la strategie de funnel]**

**[ECRAN - fiche produit WooCommerce du coffret cafe]**

Le produit principal : un coffret degustation cafe d'origine unique. Prix : 39 euros TTC, livraison incluse en France metropolitaine. C'est un produit d'impulsion - le prix est assez bas pour un achat sans trop de reflexion, mais assez eleve pour generer de la marge.

La strategie : utiliser le funnel CartFlows pour augmenter la valeur de chaque commande. Le coffret a 39 euros, c'est le produit d'appel. Le vrai chiffre d'affaires vient du bump, du upsell et du downsell.

Structure du flow CartFlows :
1. Landing page produit
2. Checkout + order bump
3. Upsell (abonnement)
4. Downsell (option de repli)
5. Thank You

---

**[SECTION 2 - Landing page et checkout]**

**[ECRAN - landing page coffret cafe]**

La landing page est une page produit enrichie : photo lifestyle du coffret, description sensorielle, origine des cafes, note de torrefaction, avis clients, et un gros bouton "Commander mon coffret - 39 euros."

Le checkout est simplifie avec CartFlows. Deux colonnes : formulaire de livraison a gauche (nom, adresse, telephone), recapitulatif de commande a droite. Le paiement se fait par carte (Stripe) ou PayPal.

Et au-dessus du bouton de paiement, l'order bump.

Le bump : "Ajoute un sachet de cafe single origin Ethiopie Yirgacheffe - 12 euros." C'est un produit complementaire, en rapport direct avec le coffret. Le texte du bump : "Nos clients adorent ce single origin - parfait pour prolonger l'experience apres la degustation." Case a cocher. Un clic.

Avec un taux d'acceptation de 30% sur le bump (ce qui est realiste pour un produit a 12 euros), la valeur moyenne passe deja de 39 a 42,60 euros.

---

**[SECTION 3 - Upsell : l'abonnement mensuel]**

**[ECRAN - page upsell abonnement cafe]**

Apres le paiement, le client arrive sur la page upsell. Et la, on propose le vrai produit a forte valeur : l'abonnement mensuel.

"Tu viens de commander ton coffret degustation. Chaque mois, recois un cafe d'exception selection par notre torrefacteur - 29 euros/mois. Premier mois offert."

Le premier mois offert elimine la barriere d'entree. Le client ne paie rien de plus aujourd'hui - le premier prelevement commence dans 30 jours. CartFlows + WooCommerce Subscriptions gerent ca automatiquement.

Un bouton : "Oui, j'essaie gratuitement pendant 1 mois." Un lien texte en-dessous : "Non merci, je passe."

Si le client accepte, tu viens de transformer un acheteur ponctuel en abonne recurrent. Sur 12 mois, ce client qui a depense 39 euros va generer 39 + 29 x 11 = 358 euros. C'est un facteur 9 sur la valeur client.

Taux d'acceptation estime pour un upsell abonnement avec mois offert : 8 a 15%.

---

**[SECTION 4 - Downsell : le produit de repli]**

**[ECRAN - page downsell sachet decouverte]**

Le client refuse l'abonnement. Pas de probleme - on ne le laisse pas partir sans une derniere proposition.

Le downsell : "Pas pret pour l'abonnement ? Essaie notre sachet decouverte 250g - 15 euros." C'est un produit a paiement unique, moins engageant qu'un abonnement, mais qui augmente quand meme la valeur de la commande.

Le downsell doit toujours etre une proposition plus simple, moins chere, et moins engageante que le upsell. Le client a dit non a l'abonnement - tu ne vas pas lui proposer un produit plus cher. Tu descends d'un cran.

Taux d'acceptation estime : 15 a 25% (parmi ceux qui ont refuse le upsell).

---

**[SECTION 5 - Tracking : Facebook Pixel + GA4]**

**[ECRAN - parametres tracking CartFlows]**

Pour un e-commerce, le tracking est indispensable. CartFlows integre nativement Facebook Pixel et Google Analytics 4.

Facebook Pixel : dans CartFlows > Parametres > Facebook Pixel, entre ton Pixel ID. CartFlows envoie automatiquement les evenements : ViewContent (landing page), InitiateCheckout (checkout), AddToCart (bump accepte), Purchase (paiement confirme). Ces donnees alimentent tes audiences publicitaires et optimisent tes campagnes.

Google Analytics 4 : active le tracking GA4 dans les parametres CartFlows. Les evenements e-commerce standard sont envoyes : begin_checkout, add_payment_info, purchase. Tu retrouves les donnees dans GA4 > Monetisation > Parcours d'achat.

Si tu fais de la publicite, ces donnees sont essentielles. Facebook utilise l'evenement Purchase pour trouver des audiences similaires. GA4 te montre ou les clients abandonnent le funnel. Sans tracking, tu voles a l'aveugle.

---

**[SECTION 6 - Relance panier abandonne]**

**[ECRAN - CartFlows > Parametres > Cart Abandonment]**

CartFlows Pro inclut un module de relance de panier abandonne. Quand un client commence a remplir le checkout mais ne finalise pas le paiement, son email est capture (s'il l'a deja saisi).

Tu configures une sequence de 3 emails :

Email 1 - 30 minutes apres l'abandon : "Tu as oublie quelque chose ? Ton coffret degustation t'attend." Objet simple, rappel du produit, lien direct vers le checkout pre-rempli.

Email 2 - 24 heures apres : "Derniere chance pour ton coffret cafe." Ajoute un temoignage client ou une photo appetissante. Cree un sentiment d'urgence leger.

Email 3 - 48 heures apres : "On t'offre la livraison express." Ajoute une incitation - livraison gratuite, petit cadeau bonus, ou coupon de 5 euros. C'est le dernier effort.

Taux de recuperation moyen des paniers abandonnes : 5 a 15%. Sur 100 abandons, tu recuperes 5 a 15 ventes. C'est du chiffre d'affaires que tu aurais completement perdu sans relance.

---

**[SECTION 7 - Les chiffres : l'impact sur l'AOV]**

**[ECRAN - tableau recapitulatif AOV]**

Calculons l'impact du funnel sur 100 commandes :

Sans funnel CartFlows : 100 commandes x 39 euros = 3 900 euros.

Avec funnel CartFlows :
- 100 commandes a 39 euros = 3 900 euros
- Bump (30% acceptent) : 30 x 12 euros = 360 euros
- Upsell abonnement (10% acceptent) : 10 x 29 euros/mois x 6 mois moyen = 1 740 euros
- Downsell (20% des 90 refus) : 18 x 15 euros = 270 euros
- Relance panier (10 recuperes) : 10 x 39 euros = 390 euros

Total avec funnel : 6 660 euros (hors recurrence long terme de l'abonnement).

AOV sans funnel : 39 euros. AOV avec funnel (hors abonnement) : 49,20 euros. Augmentation : +26%.

Et si on compte la valeur a 12 mois de l'abonnement, le gain total est bien superieur. Le funnel ne coute rien de plus en acquisition - il maximise chaque visiteur.

---

**[OUTRO - face camera]**

Ce funnel e-commerce n'a rien de complexe a mettre en place. Un produit d'appel, un bump, un upsell abonnement, un downsell, du tracking, et de la relance. Chaque element ajoute une couche de revenus supplementaires.

Dans la prochaine lecon, on adapte le modele pour un freelance qui vend des prestations de service.

---

## Notes de production

- **Visuels** : schema flow 5 etapes, landing produit, checkout avec bump, page upsell abonnement, tableau AOV comparatif
- **Captures d'ecran** : fiche produit WooCommerce, checkout CartFlows avec bump cafe, page upsell, parametres tracking, emails relance panier
- **Ton** : concret et chiffre, focus sur le ROI du funnel
- **Duree estimee** : ~12 min a debit normal
- **Transition** : enchaine sur L8.9 (Cas pratique funnel freelance)
