# Lecon 8.1 - CartFlows + FluentCRM : segmenter les acheteurs

## Metadata

- **Formation** : CartFlows Masterclass Vente (premium - FRM-007)
- **Module** : 8 - Ecosysteme et automatisation
- **Duree cible** : 12 min (~1500 mots)
- **Type** : Video HeyGen + voix ElevenLabs
- **Objectif pedagogique** : Connecter CartFlows a FluentCRM pour segmenter automatiquement les acheteurs. Creer des tags, des sequences email post-achat et une segmentation exploitable pour le marketing.

---

## Script narration

**[INTRO - face camera]**

Tu viens de construire des funnels. Tes clients passent par tes checkouts, tes bumps, tes upsells. Les commandes tombent. Mais est-ce que tu sais qui sont ces clients ? Est-ce que tu peux les recontacter avec le bon message au bon moment ?

Si tu n'as pas de CRM connecte a CartFlows, la reponse est non. Tu encaisses, mais tu ne capitalises pas. Et c'est la que FluentCRM entre en jeu.

---

**[SECTION 1 - FluentCRM : le CRM WordPress natif]**

**[ECRAN - dashboard FluentCRM]**

FluentCRM, c'est un CRM qui tourne directement dans ton WordPress. Pas de SaaS externe, pas d'abonnement mensuel qui explose avec le nombre de contacts. C'est developpe par WPManageNinja, la meme equipe que FluentForms et Fluent Support.

En version gratuite, tu as deja la gestion des contacts, les tags, les listes et les sequences email basiques. La version Pro ajoute les automatisations avancees, les rapports et les integrations e-commerce.

Le point cle : FluentCRM s'integre nativement avec WooCommerce. Et comme CartFlows genere des commandes WooCommerce, chaque achat dans ton funnel remonte automatiquement dans FluentCRM. Pas besoin de Zapier. Pas besoin de webhook custom. Ca marche out of the box.

---

**[SECTION 2 - Connecter CartFlows a FluentCRM via WooCommerce]**

**[ECRAN - FluentCRM > Parametres > Integrations WooCommerce]**

La connexion se fait en quelques etapes. Dans FluentCRM, va dans Parametres, puis Integrations. Active l'integration WooCommerce. C'est un toggle - on/off.

Une fois active, FluentCRM cree ou met a jour un contact a chaque commande WooCommerce completee. Le contact recupere automatiquement le nom, l'email et l'historique d'achats.

Mais le vrai pouvoir, c'est les tags automatiques. Dans FluentCRM, va dans Automatisations, et cree un nouveau workflow. Le declencheur : "WooCommerce - New Order (Completed)". Puis ajoute une action : "Appliquer un tag."

Tu peux conditionner le tag en fonction du produit achete. Si le client achete ta formation SEO a 97 euros, il recoit le tag "acheteur-formation-seo". S'il achete ta formation complete a 297 euros, il recoit "client-premium".

---

**[SECTION 3 - Strategie de tags pour CartFlows]**

**[ECRAN - tableau de tags recommandes]**

Voici la strategie de tags que je recommande pour un funnel CartFlows :

Premiere categorie - les tags produit :
- "acheteur-formation-seo" - a achete la formation SEO
- "acheteur-coaching" - a achete le coaching
- "client-premium" - a achete l'offre la plus chere

Deuxieme categorie - les tags comportementaux lies au funnel :
- "a-accepte-bump" - a pris l'order bump au checkout
- "a-accepte-upsell" - a accepte le upsell post-achat
- "a-refuse-upsell" - a decline le upsell (candidat pour un email de relance)
- "a-accepte-downsell" - a pris l'offre alternative

Troisieme categorie - les tags de valeur :
- "panier-moyen-eleve" - AOV superieure a 100 euros
- "multi-acheteur" - a achete plus d'une fois
- "client-recurrent" - abonnement actif

Ces tags ne sont pas decoratifs. Chaque tag declenche des sequences email specifiques. Un client qui a refuse le upsell ne recoit pas le meme email qu'un client qui a tout accepte.

---

**[SECTION 4 - Sequences email post-achat]**

**[ECRAN - FluentCRM > Sequences > creation]**

Maintenant qu'on a les tags, on construit les sequences. Voici les trois sequences essentielles pour tout funnel CartFlows :

Sequence 1 - Bienvenue et onboarding. Declencheur : tag "acheteur-formation-seo" applique. Email 1 (immediat) : confirmation d'achat + acces au contenu. Email 2 (J+1) : "Par ou commencer" - guide de demarrage rapide. Email 3 (J+3) : "Tu as des questions ?" - ouvrir le dialogue.

Sequence 2 - Upsell par email. Declencheur : tag "a-refuse-upsell" applique. Email 1 (J+3) : rappel de valeur du produit achete + teaser du produit premium. Email 2 (J+5) : temoignage client qui a pris l'offre complete. Email 3 (J+7) : offre limitee - "Je te propose le coaching a -20% cette semaine."

Sequence 3 - Demande d'avis et reactivation. Declencheur : tag produit + 14 jours apres l'achat. Email 1 (J+14) : demande d'avis ou de temoignage. Email 2 (J+21) : contenu bonus gratuit (pour maintenir l'engagement). Email 3 (J+30) : presentation de la prochaine offre.

---

**[SECTION 5 - Segmentation avancee : exploiter les donnees]**

**[ECRAN - FluentCRM > Segments dynamiques]**

Avec les tags en place et les sequences qui tournent, tu peux creer des segments dynamiques dans FluentCRM. Un segment dynamique, c'est un groupe de contacts qui se met a jour automatiquement selon des criteres.

Exemple de segments utiles :

- Acheteurs vs prospects : tous les contacts avec au moins un tag "acheteur-*" vs ceux sans tag d'achat
- Clients a forte valeur : tag "panier-moyen-eleve" OU "multi-acheteur"
- Candidats a l'upsell : tag "a-refuse-upsell" ET pas de tag "client-premium"
- Clients inactifs : dernier achat > 90 jours ET pas d'ouverture d'email > 30 jours

Ces segments alimentent tes campagnes email. Tu n'envoies plus le meme message a tout le monde. Tu parles a chaque client en fonction de son comportement reel dans ton funnel.

---

**[SECTION 6 - Cas concret : le parcours complet]**

**[ECRAN - schema du parcours client complet]**

Voici un cas concret, etape par etape. Marie arrive sur ta landing page CartFlows. Elle clique et arrive au checkout. Elle achete ta formation "Les bases du SEO WordPress" a 47 euros. Elle ne prend pas l'order bump. Elle refuse le upsell coaching a 197 euros. Elle atterrit sur la page Thank You.

Dans FluentCRM, voici ce qui se passe en coulisses : un contact est cree avec son email. Les tags appliques : "acheteur-formation-seo", "client-basique", "a-refuse-upsell". La sequence "Bienvenue onboarding" demarre immediatement. Trois jours plus tard, la sequence "Upsell par email" demarre.

A J+7, Marie recoit l'email avec l'offre coaching a -20%. Cette fois, elle clique et achete. Nouveaux tags : "acheteur-coaching", "client-premium". Le tag "a-refuse-upsell" est retire. La sequence upsell s'arrete automatiquement. Une nouvelle sequence premium demarre.

Resultat : un client a 47 euros est devenu un client a 204 euros - sans publicite supplementaire. Juste avec un CRM bien configure et des sequences pertinentes.

---

**[OUTRO - face camera]**

CartFlows genere les ventes. FluentCRM capitalise sur ces ventes. Les deux ensemble, c'est un systeme ou chaque achat declenche une chaine d'actions automatiques qui augmentent la valeur client dans le temps.

Dans la prochaine lecon, on ajoute OttoKit pour automatiser encore plus d'actions post-achat - au-dela de l'email.

---

## Notes de production

- **Visuels** : dashboard FluentCRM, tableau de tags recommandes, schema sequences email, schema parcours client complet
- **Captures d'ecran** : FluentCRM integrations WooCommerce, creation d'automatisation, editeur de sequence
- **Ton** : technique et strategique, avec un cas concret detaille
- **Duree estimee** : ~12 min a debit normal
- **Transition** : enchaine sur L8.2 (CartFlows + OttoKit)
