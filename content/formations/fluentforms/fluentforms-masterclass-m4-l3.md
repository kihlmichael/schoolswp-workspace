# Script video — Module 4, Lecon 3 : Paiements recurrents — abonnements

**Formation** : FluentForms Masterclass Formulaires
**Code** : FRM-012 (premium)
**Module** : 4 — Paiements
**Lecon** : 3/7 — Paiements recurrents : abonnements
**Duree** : 8 min (~1100 mots)
**Type** : Video HeyGen + voix ElevenLabs
**Ecran** : Face camera intro/outro, screencast builder + Stripe subscriptions, slide cas d'usage
**Objectif** : Configurer un formulaire d'abonnement recurrent avec Stripe

---

**[INTRO — face camera]**

Un paiement unique c'est bien. Un revenu recurrent c'est mieux. FluentForms Pro permet de creer des abonnements directement depuis un formulaire — mensuel, annuel, ou a la frequence que tu veux.

On va voir comment configurer ca, et surtout comment gerer les annulations proprement.

**[SECTION 1 — slide "Cas d'usage des abonnements"]**

Avant de configurer, voyons quand utiliser un abonnement plutot qu'un paiement unique.

Communaute privee. Acces mensuel a un groupe, un forum, des ressources exclusives. 19 euros par mois par exemple.

Coaching recurrent. Seance mensuelle avec suivi. 97 euros par mois.

SaaS ou outil en ligne. Acces a un service que tu developpes. Facturation mensuelle ou annuelle.

Maintenance WordPress. Mises a jour, sauvegardes, support technique. Forfait mensuel.

Le point commun : le client paie regulierement pour un acces ou un service continu.

**[SECTION 2 — screencast "Creer le formulaire d'abonnement"]**

Cree un nouveau formulaire. "Abonnement Communaute WordPress".

Ajoute les champs client : Name, Email.

Maintenant, dans Payment Fields, ajoute un champ Subscription Payment. C'est different du Payment Item qu'on a utilise dans la lecon precedente.

Configure-le. Label : "Abonnement Communaute". Prix : 19.00. Billing Interval : Monthly.

Tu as plusieurs options de frequence : Daily (rare), Weekly, Monthly, Yearly. Pour notre communaute, Monthly est le bon choix.

Si tu veux proposer un choix entre mensuel et annuel, utilise un champ Radio avant le Subscription et configure la logique conditionnelle pour afficher le bon prix. Mensuel 19 euros, annuel 190 euros — le client choisit.

**[SECTION 3 — screencast "Configuration Stripe pour les subscriptions"]**

Stripe gere les abonnements nativement. Quand un client souscrit via ton formulaire, FluentForms cree automatiquement un objet Subscription dans Stripe.

Dans ton dashboard Stripe, tu retrouves tout. Section Subscriptions : la liste de tes abonnes, la date du prochain prelevement, le statut (active, past_due, canceled).

Le prelevement se fait automatiquement. Le client entre sa carte une fois. Stripe preleve chaque mois sans que tu n'aies rien a faire.

Si le paiement echoue — carte expiree, fonds insuffisants — Stripe retente automatiquement selon sa politique de retry. Trois tentatives espacees de quelques jours. Si ca echoue trois fois, l'abonnement passe en statut "canceled".

**[SECTION 4 — screencast "Notifications et confirmation"]**

Pour les abonnements, configure deux notifications.

La premiere : email de bienvenue a la souscription. "Bienvenue dans la communaute WordPress. Ton abonnement mensuel de 19 euros est actif. Voici ton lien d'acces."

La deuxieme : tu la configures dans Stripe directement. Stripe peut envoyer un email automatique a chaque prelevement reussi. Dashboard Stripe, Settings, Emails, active "Successful payment". Le client recoit un recu chaque mois.

Pour la page de confirmation dans FluentForms, redirige vers ta page d'acces a la communaute. Le client souscrit et arrive directement sur le contenu.

**[SECTION 5 — slide "Gerer les annulations"]**

Les annulations, ca fait partie du jeu. Il faut les gerer proprement.

Option 1 : le client annule depuis son espace Stripe. Tu peux lui fournir un lien vers le portail client Stripe (Stripe Customer Portal). Il se connecte, il annule, c'est fait.

Option 2 : tu annules manuellement depuis ton dashboard Stripe. Tu trouves l'abonnement, tu cliques "Cancel subscription". Tu choisis : annulation immediate ou a la fin de la periode en cours.

Je te recommande l'annulation a la fin de la periode. Le client a paye pour le mois en cours, il garde son acces jusqu'a la fin. C'est plus propre et ca reduit les demandes de remboursement.

Connecte ca a FluentCRM si tu l'utilises : quand un abonnement est annule, retire le tag "membre-actif" et ajoute le tag "ancien-membre". Tu pourras relancer ces contacts plus tard avec une offre de retour.

**[OUTRO — face camera]**

Tu as maintenant un formulaire qui encaisse des abonnements recurrents. C'est la base d'un revenu previsible. Dans la prochaine lecon, on attaque la tarification conditionnelle — le prix qui s'adapte en temps reel selon les choix du client.

On se retrouve dans la lecon suivante.

---

**Points cles** :
- Champ Subscription Payment (Pro) : prix + frequence (Monthly, Yearly...)
- Stripe gere les prelevements automatiques et les retries
- Notifications : email bienvenue + recus automatiques via Stripe
- Annulations : portail client Stripe ou annulation manuelle
- Recommandation : annulation en fin de periode, pas immediate
- Connecter les annulations a FluentCRM pour le suivi

**Mots cles SEO** : FluentForms abonnement, paiement recurrent WordPress, Stripe subscription formulaire, vendre abonnement WordPress

---

**Notes de production** :
- Face camera : intro (pitch revenu recurrent) + outro (transition tarification)
- Screencast : creation formulaire + dashboard Stripe subscriptions (~5 min)
- Slides : 2 slides (cas d'usage + gestion annulations)
- Ton : concret, oriente business — montrer la valeur du recurrent
