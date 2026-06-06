# Lecon 8.4 - CartFlows + WooCommerce Subscriptions

## Metadata

- **Formation** : CartFlows Masterclass Vente (premium - FRM-007)
- **Module** : 8 - Ecosysteme et automatisation
- **Duree cible** : 10 min (~1300 mots)
- **Type** : Video HeyGen + voix ElevenLabs
- **Objectif pedagogique** : Vendre des abonnements via un funnel CartFlows. Configurer un produit WooCommerce Subscription, afficher le prix recurrent dans le checkout, ajouter bump et upsell sur un abonnement, et gerer renouvellements et annulations.

---

## Script narration

**[INTRO - face camera]**

Jusqu'ici, on a vendu des produits a paiement unique - une formation, un coaching, un service. Mais le vrai levier de croissance pour un business en ligne, c'est le revenu recurrent. Un abonnement mensuel ou annuel qui genere du chiffre d'affaires previsible, mois apres mois.

WooCommerce Subscriptions est le plugin de reference pour ca. Et il fonctionne parfaitement avec CartFlows. Tu peux vendre un abonnement via un funnel optimise, avec bump, upsell, et toute la mecanique qu'on a vue dans les modules precedents.

---

**[SECTION 1 - Configurer un produit WooCommerce Subscription]**

**[ECRAN - WooCommerce > Produit > Type : Simple Subscription]**

La premiere etape, c'est de creer ton produit abonnement dans WooCommerce. Va dans Produits, Ajouter, et dans le type de produit, choisis "Simple Subscription" (ou "Variable Subscription" si tu veux proposer plusieurs formules).

Les champs specifiques a configurer :

- Prix de l'abonnement : par exemple 29 euros par mois
- Periode de facturation : mensuelle, trimestrielle, annuelle
- Periode d'essai : optionnel - 7 jours gratuits pour reduire la barriere d'entree
- Frais d'inscription : un paiement unique a l'inscription, en plus du premier mois (utile pour couvrir les couts de setup)

Pour une communaute ou un acces premium, je recommande de commencer avec un abonnement mensuel a 19-39 euros sans periode d'essai. L'essai gratuit peut attirer des curieux qui annulent immediatement. Mieux vaut un prix d'entree accessible et un contenu qui justifie le renouvellement.

---

**[SECTION 2 - Afficher le prix recurrent dans le checkout CartFlows]**

**[ECRAN - checkout CartFlows avec produit subscription]**

Quand tu ajoutes un produit Subscription au checkout CartFlows, le prix affiche automatiquement la mention recurrente : "29 euros/mois". C'est WooCommerce Subscriptions qui gere cet affichage - CartFlows n'a rien de special a configurer.

Un point important : la transparence. Le client doit comprendre immediatement qu'il s'engage sur un paiement recurrent. Assure-toi que la mention "/mois" ou "/an" est bien visible dans le recapitulatif de commande. Si tu utilises un prix d'essai ou des frais d'inscription, affiche-les clairement : "Premier mois : 1 euro, puis 29 euros/mois."

Dans les options du checkout CartFlows, tu peux personnaliser le texte du bouton de commande. Pour un abonnement, change "Passer commande" en quelque chose de plus explicite : "Demarrer mon abonnement" ou "M'inscrire pour 29 euros/mois". La clarte reduit les demandes de remboursement.

---

**[SECTION 3 - Order bump sur un abonnement]**

**[ECRAN - checkout avec bump sur abonnement]**

Le bump sur un abonnement demande une reflexion differente. Tu ne veux pas ajouter un deuxieme abonnement en bump - ca complique la gestion et ca fait peur au client. Le meilleur bump sur un abonnement, c'est un produit a paiement unique qui enrichit l'experience.

Exemples de bumps qui marchent :

- Module bonus a debloquer immediatement : "Ajoute le module avance 'Automatisation e-commerce' - 17 euros (paiement unique)." Le client commence son abonnement avec un bonus exclusif.
- Acces a un canal prive : "Rejoins le groupe Slack VIP des membres premium - 9 euros (une fois)." Donne un sentiment d'exclusivite des le depart.
- Ressource telechargeable : "Pack de 10 templates prets a l'emploi - 12 euros." Un complement tangible qui accelere les premiers resultats.

Le bump a paiement unique sur un abonnement fonctionne mieux qu'un bump recurrent parce que le client n'a pas l'impression de s'engager sur deux fronts a la fois.

---

**[SECTION 4 - Upsell : upgrade mensuel vers annuel]**

**[ECRAN - page upsell upgrade annuel]**

Voici le upsell le plus puissant pour les abonnements : proposer l'upgrade vers le plan annuel juste apres l'achat du plan mensuel.

Le client vient de souscrire a 29 euros par mois. Sur la page upsell, tu lui proposes : "Passe au plan annuel a 249 euros (au lieu de 348 euros - soit 2 mois offerts)." Le one-click upsell de CartFlows permet au client d'upgrader sans ressaisir ses informations de paiement.

Pourquoi ca marche : le client vient de dire oui. Il est dans une dynamique positive. Et l'offre annuelle est mathematiquement avantageuse pour lui. Il economise de l'argent, et toi tu securises 12 mois de revenu d'un coup.

Techniquement, CartFlows remplace le produit mensuel par le produit annuel dans la commande. WooCommerce Subscriptions gere le changement de plan automatiquement.

Si le client refuse l'annuel, le downsell peut etre : "OK, reste sur le mensuel. Mais voici un bonus exclusif pour les 3 premiers mois : acces au coaching de groupe - offert." Tu renforces l'engagement sans demander plus d'argent.

---

**[SECTION 5 - Gestion des renouvellements et annulations]**

**[ECRAN - WooCommerce > Abonnements > tableau de bord]**

Une fois l'abonnement actif, WooCommerce Subscriptions gere automatiquement les renouvellements. A chaque echeance, le paiement est preleve via la passerelle (Stripe, PayPal). Si le paiement echoue, WooCommerce tente une relance automatique selon les regles que tu configures.

Pour les annulations : dans WooCommerce > Parametres > Subscriptions, tu peux autoriser ou non le client a annuler lui-meme depuis son espace "Mon Compte". Mon conseil : autorise l'annulation. Un client qui veut partir mais ne peut pas est un client qui va contester le paiement aupres de sa banque - et ca, c'est pire.

En revanche, ce que tu peux faire : ajouter une enquete de depart. Quand le client clique "Annuler", affiche un formulaire : "Qu'est-ce qui t'a pousse a annuler ?" Les reponses sont precieuses pour ameliorer ton offre.

Et combine avec FluentCRM : quand un abonnement est annule, applique le tag "ex-abonne" et demarre une sequence de reconquete. Email a J+3 : "Tu nous manques - voici ce que tu rates ce mois-ci." Email a J+7 : "Reviens avec 30% de reduction pendant 3 mois."

---

**[OUTRO - face camera]**

Les abonnements via CartFlows + WooCommerce Subscriptions, c'est le pilier du revenu recurrent. Avec un funnel optimise, un bump pertinent et un upsell annuel, tu maximises la valeur de chaque nouvel abonne des son premier passage en caisse.

Dans la prochaine lecon, quelque chose de plus rapide mais tres utile : comment exporter et importer des funnels entre sites.

---

## Notes de production

- **Visuels** : formulaire produit subscription WooCommerce, checkout avec prix recurrent, page upsell annuel vs mensuel
- **Captures d'ecran** : creation produit subscription, checkout CartFlows avec mention /mois, dashboard abonnements WooCommerce
- **Ton** : technique et strategique, focus sur le business model recurrent
- **Duree estimee** : ~10 min a debit normal
- **Transition** : enchaine sur L8.5 (Import/Export de funnels)
