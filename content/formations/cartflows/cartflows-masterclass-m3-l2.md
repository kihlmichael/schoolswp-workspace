# Lecon 3.2 - Multi-step checkout : pourquoi et comment

## Metadata

- **Formation** : CartFlows Masterclass Vente (premium - FRM-007)
- **Module** : 3 - Checkout optimise
- **Duree cible** : 10 min (~1400 mots)
- **Type** : Video HeyGen + voix ElevenLabs
- **Objectif pedagogique** : Comprendre le principe du multi-step checkout (engagement progressif), savoir configurer un checkout en 2 ou 3 etapes dans CartFlows, choisir le bon format selon le type de produit.

---

## Script narration

**[INTRO - face camera]**

Un formulaire de checkout long, c'est intimidant. Le visiteur arrive, voit 12 champs a remplir d'un coup - nom, prenom, adresse, code postal, ville, pays, telephone, email, numero de carte, date d'expiration, CVV, conditions generales. Il n'a meme pas commence qu'il a deja envie de partir.

Le multi-step checkout resout ce probleme. Au lieu d'afficher tout d'un bloc, tu decoupes le formulaire en 2 ou 3 etapes. Le client remplit ses coordonnees, clique sur "Suivant", puis ses infos de livraison, puis son paiement. Meme nombre de champs - mais une experience completement differente.

Et ca change les taux de conversion. Voyons pourquoi, et comment le mettre en place dans CartFlows.

---

**[SECTION 1 - Pourquoi le multi-step convertit mieux]**

**[ECRAN - schema : formulaire unique vs formulaire en etapes]**

Le principe derriere le multi-step, c'est l'engagement progressif. En psychologie comportementale, on appelle ca la "technique du pied dans la porte". Une fois que quelqu'un a fait un premier petit pas, il est beaucoup plus enclin a continuer.

Quand ton visiteur remplit son email et son prenom a l'etape 1 et clique "Suivant", il a deja investi du temps et de l'effort. Il a commence le processus. Abandonner maintenant, ce serait "perdre" ce qu'il a deja fait. Alors il continue.

Trois raisons concretes pour lesquelles ca fonctionne.

Premiere raison : c'est moins intimidant. Trois champs a l'ecran, c'est simple. Douze champs d'un coup, c'est un mur.

Deuxieme raison : les micro-engagements. Chaque clic sur "Suivant" est un petit "oui" que le client se dit a lui-meme. Ces micro-engagements s'accumulent et rendent l'abandon de plus en plus couteux psychologiquement.

Troisieme raison : tu recuperes des donnees meme en cas d'abandon. Si le client remplit l'etape 1 (email + prenom) puis abandonne a l'etape 2, tu as quand meme son email. Tu peux le relancer. Avec un checkout en une seule page, un abandon te laisse avec rien.

---

**[SECTION 2 - Configurer le multi-step dans CartFlows]**

**[ECRAN - editeur CartFlows, step Checkout]**

La mise en place est simple. Ouvre ton flow CartFlows, clique sur l'etape Checkout, puis va dans les settings du checkout.

**[ECRAN - Layout → options Two Step / Two Column / One Column]**

Dans la section Layout, tu vas trouver les options de disposition. CartFlows propose plusieurs formats : One Column, Two Column, et Two Step.

Selectionne "Two Step". L'apercu change immediatement - tu vois maintenant deux onglets en haut du formulaire avec une barre de progression.

**[ECRAN - apercu du checkout two step]**

L'etape 1 regroupe les informations personnelles : nom, prenom, email, telephone. L'etape 2 affiche le paiement et le recapitulatif de commande. Le client clique "Suivant" pour passer d'une etape a l'autre.

Pour un checkout en trois etapes, CartFlows ne propose pas nativement un "Three Step" en un clic. Mais tu peux obtenir le meme resultat en combinant le two-step avec des custom fields regroupes (on verra les custom fields dans la lecon suivante). L'approche classique en trois etapes : contact, livraison, paiement.

---

**[SECTION 3 - Configurer les champs de chaque etape]**

**[ECRAN - CartFlows Checkout settings → Form Fields]**

Maintenant, il faut decider quels champs vont dans chaque etape. Le principe : le minimum vital a chaque etape, dans un ordre logique.

**Etape 1 - Contact** : prenom, nom, email. C'est tout. Trois champs. Le visiteur entre ses infos de base, c'est rapide, c'est facile. Et tu as deja son email en cas d'abandon.

**Etape 2 (produit physique) - Livraison** : adresse, code postal, ville, pays, telephone. Les champs specifiques a l'expedition. Pour un produit digital, cette etape n'existe pas - tu passes directement au paiement.

**Etape 3 - Paiement** : mode de paiement (carte, PayPal, virement), recap de commande, case conditions generales, bouton "Commander".

Dans CartFlows, tu peux reordonner les champs par drag-and-drop dans la section "Checkout Fields". Tu peux aussi masquer les champs inutiles - le fameux champ "Entreprise" que personne ne remplit, par exemple. Desactive-le. Chaque champ en moins, c'est une friction en moins.

---

**[SECTION 4 - Les indicateurs de progression]**

**[ECRAN - breadcrumbs en haut du checkout multi-step]**

Les breadcrumbs - les indicateurs de progression en haut du checkout - jouent un role important. Le client voit ou il en est et combien d'etapes il reste. Ca reduit l'anxiete du "combien de temps ca va encore durer ?".

CartFlows affiche automatiquement ces indicateurs quand tu actives le two-step. Tu peux personnaliser les labels de chaque etape. Par defaut, c'est "Your Details" et "Order Review". Change-les en francais : "Tes coordonnees" et "Paiement" - ou "Etape 1" et "Etape 2" si tu preferes quelque chose de neutre.

**[ECRAN - personnalisation des labels dans CartFlows]**

Le style des breadcrumbs depend de ton theme. Avec Kadence, le rendu est propre par defaut. Si tu veux aller plus loin, tu peux ajuster les couleurs et les polices dans les options CartFlows du checkout - section "Design", onglet typography et colors.

---

**[SECTION 5 - Cas pratique : digital vs physique]**

**[ECRAN - face camera]**

Maintenant, la question pratique : combien d'etapes pour ton produit ?

**Produit digital** - formation en ligne, ebook, template, plugin : deux etapes suffisent. Etape 1 : contact (prenom, email). Etape 2 : paiement. Pas besoin d'adresse de livraison, pas besoin de telephone. Tu reduis le checkout au strict minimum.

Avec deux etapes, tu as un checkout qui se remplit en moins d'une minute. Et si le client abandonne apres l'etape 1, tu as son email pour le relancer.

**Produit physique** - materiel, livres, accessoires : trois etapes. Etape 1 : contact. Etape 2 : livraison (adresse complete). Etape 3 : paiement. L'adresse de livraison est obligatoire, tu ne peux pas la supprimer - mais en la mettant dans une etape separee, tu evites l'effet "mur de champs".

**[ECRAN - tableau comparatif : digital 2 etapes vs physique 3 etapes]**

La regle simple : deux etapes pour le digital, trois etapes pour le physique. Pas plus. Quatre etapes ou plus, c'est contre-productif - le client a l'impression que ca n'en finit jamais.

---

**[SECTION 6 - Mesurer l'impact]**

**[ECRAN - face camera]**

Une fois ton multi-step en place, tu vas vouloir mesurer si ca ameliore reellement tes conversions. Deux methodes.

Methode simple : compare ton taux de conversion avant et apres le changement. Regarde tes stats WooCommerce sur les 30 derniers jours, active le multi-step, attends 30 jours, et compare. Ce n'est pas scientifiquement rigoureux, mais ca donne une tendance.

Methode rigoureuse : l'A/B test. CartFlows Pro permet de creer des variantes de tes etapes. Tu peux tester un checkout en une page contre un checkout en deux etapes, et CartFlows repartit le trafic automatiquement. On verra ca en detail dans un module futur dedie a l'optimisation.

Dans tous les cas, ne change pas plusieurs choses en meme temps. Si tu passes au multi-step et que tu modifies aussi le design, les couleurs et les textes, tu ne sauras pas ce qui a fait la difference.

---

**[OUTRO - face camera]**

Le multi-step checkout, c'est une des optimisations les plus simples a mettre en place et les plus efficaces sur le taux de conversion. Deux etapes pour le digital, trois pour le physique. Des breadcrumbs clairs. Le minimum de champs a chaque etape.

Dans la prochaine lecon, on va voir comment ajouter des champs personnalises a ton checkout - pour collecter exactement les informations dont tu as besoin sans casser ta conversion.

---

## Notes de production

- **Captures d'ecran necessaires** : checkout one-column vs two-step, settings Layout dans CartFlows, Form Fields editor, breadcrumbs personnalises, design settings
- **Schemas** : formulaire unique vs multi-step (visuel), tableau digital 2 etapes vs physique 3 etapes
- **Timing** : intro (1 min) → pourquoi ca convertit (2 min) → configuration CartFlows (2 min) → champs par etape (1.5 min) → breadcrumbs (1 min) → cas pratique digital/physique (1.5 min) → mesurer (1 min) → outro (0.5 min)
- **Ton** : pedagogique, appuye sur la psychologie (engagement progressif), concret avec les exemples digital vs physique
