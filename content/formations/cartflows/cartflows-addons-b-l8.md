# Lecon B.8 — Cart Abandonment + FluentCRM : relance CRM avancee

## Metadata

- **Formation** : CartFlows Add-ons (premium — FRM-008)
- **Module** : B — Cart Abandonment Recovery
- **Duree cible** : 10 min (~1 300 mots)
- **Type** : Video HeyGen + voix ElevenLabs
- **Objectif pedagogique** : Connecter Cart Abandonment Recovery a FluentCRM pour combiner la relance court terme (emails automatiques) et la strategie long terme (sequences CRM, nurturing, re-engagement).

---

## Script narration

**[INTRO — face camera]**

Cart Abandonment Recovery envoie 3 emails en 3 jours. C'est efficace pour le court terme — le rappel immediat, l'argumentation, le coupon. Mais que se passe-t-il apres 3 jours si le client n'a toujours pas converti ?

Avec Cart Abandonment Recovery seul : rien. Le client disparait.

Avec FluentCRM en plus : tu continues la relation. Et c'est la que la combinaison des deux outils devient redoutable.

---

**[SECTION 1 — Pourquoi connecter les deux]**

**[ECRAN — schema Cart Abandonment Recovery + FluentCRM]**

Cart Abandonment Recovery est specialise : il detecte les abandons, envoie des emails de relance, genere des coupons. Il fait ca tres bien, mais il s'arrete apres la sequence de 3 emails.

FluentCRM est un CRM complet. Il gere des contacts, des tags, des listes, des sequences email avancees, de l'automatisation conditionnelle. Il ne detecte pas les abandons de panier nativement, mais il sait tout faire une fois qu'il a un contact.

La combinaison : Cart Abandonment Recovery detecte et relance a court terme. FluentCRM prend le relais a long terme.

L'idee n'est pas de remplacer l'un par l'autre. C'est d'utiliser chacun pour ce qu'il fait le mieux.

---

**[SECTION 2 — Le pont : tag "panier-abandonne" dans FluentCRM]**

**[ECRAN — FluentCRM → Automatisations]**

Pour connecter les deux, il faut creer un pont. Voici comment.

**Etape 1 : creer le tag dans FluentCRM.** Va dans FluentCRM → Tags → Ajouter un tag. Nomme-le "panier-abandonne". Ce tag identifiera tous les contacts qui ont abandonne un panier.

**Etape 2 : configurer l'automatisation.** Cart Abandonment Recovery enregistre les adresses email des paniers abandonnes. FluentCRM peut detecter quand un nouveau contact WooCommerce est cree ou mis a jour.

Cree une automatisation FluentCRM avec comme declencheur "New Order — WooCommerce" en statut "failed" ou "cancelled". Quand le declencheur se declenche, l'action est : appliquer le tag "panier-abandonne" au contact.

Alternative plus simple : utilise le webhook Cart Abandonment Recovery (disponible en version Pro) pour envoyer directement les donnees a FluentCRM via une automatisation n8n. On a vu dans les modules precedents comment connecter les outils entre eux.

**Etape 3 : verifier.** Fais un test d'abandon. Verifie que le contact apparait dans FluentCRM avec le tag "panier-abandonne".

---

**[SECTION 3 — Sequences FluentCRM avancees]**

**[ECRAN — FluentCRM → editeur de sequence]**

Une fois le pont en place, tu peux creer des sequences FluentCRM dediees aux paniers abandonnes. Voici trois scenarios.

**Scenario 1 : Nurturing post-abandon (J+7 a J+14)**

La sequence Cart Abandonment Recovery s'arrete a J+3. FluentCRM prend le relais a J+7 :

- J+7 : email de valeur — un article de blog, un guide, une video liee au produit abandonne. Pas de vente, juste du contenu utile.
- J+10 : email temoignage — une etude de cas ou un retour client detaille sur le produit.
- J+14 : email offre speciale — une promotion differente du coupon initial (bundle, upgrade, acces anticipe).

Cette sequence ne met pas de pression. Elle maintient la relation et rappelle regulierement la valeur du produit.

**Scenario 2 : Re-engagement a 30 jours**

Si le client n'a toujours pas converti apres 14 jours, il entre dans une sequence de re-engagement :

- J+30 : email "On pense a toi" — nouveau produit, nouvelle offre, ou simple rappel que la boutique existe.
- J+45 : email enquete — "Qu'est-ce qui t'a freine ?" avec un lien vers un formulaire court. Les reponses sont de l'or pour ameliorer ta boutique.

**Scenario 3 : Relance multi-produit**

Si le client a abandonne un produit A, FluentCRM peut lui proposer un produit B dans la meme categorie. Parfois, le probleme n'est pas la boutique — c'est le produit specifique qui ne correspondait pas.

---

**[SECTION 4 — Le cas concret : timeline complete]**

**[ECRAN — timeline complete J+0 a J+45]**

Voici la timeline complete d'un abandon de panier avec les deux outils :

| Moment | Outil | Action |
|---|---|---|
| J+0 (15 min) | Cart Abandonment Recovery | Email 1 — rappel simple |
| J+1 (24h) | Cart Abandonment Recovery | Email 2 — rappel + arguments |
| J+3 (72h) | Cart Abandonment Recovery | Email 3 — coupon unique |
| J+3 | FluentCRM | Tag "panier-abandonne" applique |
| J+7 | FluentCRM | Email nurturing — contenu de valeur |
| J+10 | FluentCRM | Email temoignage client |
| J+14 | FluentCRM | Offre speciale differente |
| J+30 | FluentCRM | Email re-engagement |
| J+45 | FluentCRM | Enquete satisfaction |

Si le client convertit a n'importe quelle etape, les deux outils detectent la commande et arretent la sequence. Pas de double envoi, pas de spam.

Cette combinaison couvre le court terme (reflexe d'achat, 0-3 jours), le moyen terme (nurturing, 7-14 jours), et le long terme (re-engagement, 30-45 jours). Tu maximises la fenetre de recuperation.

---

**[SECTION 5 — Conseil strategique]**

**[ECRAN — slide recapitulatif]**

Cart Abandonment Recovery pour le court terme. FluentCRM pour le long terme. Les deux ensemble pour un maximum de recuperation.

Quelques regles a respecter :

- Ne commence pas FluentCRM avant J+7. Laisse Cart Abandonment Recovery faire son travail sans interference.
- Change le ton entre les deux outils. Cart Abandonment Recovery est transactionnel (rappel, coupon). FluentCRM est relationnel (contenu, temoignage, enquete).
- Surveille le taux de desabonnement. Si les clients se desabonnent apres J+14, raccourcis la sequence FluentCRM.

Le resultat : au lieu de perdre definitivement un client apres 3 jours, tu maintiens le contact pendant 45 jours. Et chaque point de contact supplementaire est une chance de recuperation.

---

**[CONCLUSION — face camera]**

La combinaison Cart Abandonment Recovery + FluentCRM transforme un outil de relance basique en un systeme de recuperation complet. Le court terme automatise, le long terme personnalise.

Dans la derniere lecon de ce module, on fait le bilan : combien de paniers tu peux realistement recuperer et quel est le ROI concret de tout ce qu'on a mis en place.

---

## Notes de production

- **Visuels** : schema connexion CAR + FluentCRM, timeline complete J+0 a J+45, editeur sequence FluentCRM
- **Donnees** : timeline basee sur les best practices CRM e-commerce, 3 scenarios de sequences
- **Transition** : enchaine sur LB.9 (objectif : recuperer 20-30% des paniers)
