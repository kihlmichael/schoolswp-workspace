# Script video — Module 5, Lecon 5 : Declencher une automation FluentCRM

**Formation** : FluentForms Masterclass Formulaires
**Code** : FRM-012 (premium)
**Module** : 5 — FluentForms + FluentCRM
**Lecon** : 5/7 — Declencher une automation FluentCRM
**Duree** : 10 min (~1300 mots)
**Type** : Video HeyGen + voix ElevenLabs
**Ecran** : Face camera intro/outro, screencast FluentCRM automations, slide schema sequence
**Objectif** : Creer une automation FluentCRM declenchee par une soumission FluentForms

---

**[INTRO — face camera]**

Le contact est dans FluentCRM avec les bons tags. Maintenant, on automatise ce qui se passe apres. Une soumission de formulaire declenche une sequence email complete — bienvenue, contenu, offre — sans que tu n'aies a toucher quoi que ce soit.

**[SECTION 1 — slide "Les triggers disponibles"]**

FluentCRM propose trois triggers lies a FluentForms.

Trigger 1 : "Fluent Forms Submission". L'automation se declenche quand un formulaire specifique est soumis. Tu choisis le formulaire concerne.

Trigger 2 : "Tag Applied". L'automation se declenche quand un tag specifique est ajoute a un contact. Comme les tags sont assignes automatiquement par les feeds FluentForms, ca revient au meme — mais avec plus de flexibilite.

Trigger 3 : "List Applied". L'automation se declenche quand un contact est ajoute a une liste specifique.

Pour les cas simples, utilise le trigger "Fluent Forms Submission". Pour les cas avances ou un meme tag peut venir de plusieurs sources (formulaire, import, action manuelle), utilise "Tag Applied".

**[SECTION 2 — screencast "Creer l'automation"]**

Direction FluentCRM, Automations, Create Automation.

Donne un nom a ton automation : "Sequence bienvenue — Lead Magnet SEO".

Choisis le trigger : "Fluent Forms Submission". Selectionne le formulaire concerne — "Guide SEO gratuit".

L'automation se declenchera chaque fois que quelqu'un soumet ce formulaire.

**[SECTION 3 — screencast "Construire la sequence"]**

On va construire une sequence en 5 etapes.

Etape 1 — Email immediat. Action : Send Email. Objet : "Ton guide SEO WordPress est pret". Corps : remerciement + lien de telechargement du guide. Cet email part immediatement apres la soumission.

Etape 2 — Delai. Action : Wait. Duree : 1 heure. Pourquoi pas immediatement le deuxieme email ? Parce que le contact vient de recevoir le guide. Laisse-le lire.

Etape 3 — Email de bienvenue. Action : Send Email. Objet : "Une question rapide". Corps : qui tu es, ce que fait schoolsWP, et une question ouverte — "Quel est ton plus gros defi SEO en ce moment ?" Ca cree de l'engagement. Les reponses a cet email arrivent dans ta boite mail.

Etape 4 — Delai. Action : Wait. Duree : 3 jours.

Etape 5 — Email de valeur. Action : Send Email. Objet : "3 erreurs SEO que je vois sur 80% des sites WordPress". Corps : contenu educatif pur. Pas de pitch, pas de vente. Tu apportes de la valeur pour construire la confiance.

Etape 6 — Delai. Action : Wait. Duree : 4 jours.

Etape 7 — Email offre. Action : Send Email. Objet : "Si le SEO WordPress t'interesse...". Corps : presentation de ta formation SEO ou de ton offre de service. Lien vers la page de vente. Coupon de reduction optionnel.

**[SECTION 4 — screencast "Les actions complementaires"]**

Au-dela des emails, tu peux ajouter d'autres actions dans la sequence.

Apply Tag : a l'etape 7, ajoute le tag "sequence-completed-seo" pour savoir qui a recu toute la sequence.

Remove Tag : retire le tag "new-lead" et ajoute "nurtured-lead" apres la sequence.

Goal : si le contact achete avant la fin de la sequence (tag "bought-formation-seo" ajoute), l'automation s'arrete automatiquement. Pas besoin de lui envoyer l'email d'offre s'il a deja achete.

Wait for a specific date : utile pour les lancements. "Attends le 15 mars, puis envoie l'email d'ouverture des ventes."

**[SECTION 5 — slide "Schema de la sequence"]**

Visualise le flux complet.

Jour 0 : soumission formulaire → email livraison guide (immediat) → email bienvenue (H+1).
Jour 3 : email contenu de valeur.
Jour 7 : email offre.

Si achat entre-temps → automation stoppee par le goal.
Si pas d'achat → tag "sequence-completed-seo" ajoute → contact disponible pour d'autres campagnes.

C'est une sequence simple mais efficace. 4 emails sur 7 jours. Chaque email a un objectif precis : livrer, engager, eduquer, convertir.

**[SECTION 6 — screencast "Activer et monitorer"]**

Quand ta sequence est construite, clique sur "Publish" ou "Activate". L'automation est en marche.

Pour monitorer : FluentCRM, Automations, clique sur ton automation. Tu vois le nombre de contacts qui sont entres, combien sont a chaque etape, combien ont termine.

Regarde aussi les statistiques de chaque email : taux d'ouverture, taux de clic, desabonnements. Si un email a un taux d'ouverture de 10% alors que les autres sont a 40%, c'est l'objet qui pose probleme. Teste un nouvel objet.

Un bon taux d'ouverture pour une sequence de bienvenue : 40-60% pour le premier email, 30-45% pour les suivants. En dessous, il faut optimiser.

**[OUTRO — face camera]**

Tu as une automation complete qui se declenche a chaque soumission de formulaire. Le contact est accueilli, nourri et dirige vers ton offre automatiquement.

Dans la prochaine lecon, on construit un cas pratique complet : lead magnet, sequence de nurturing et upsell. Le pipeline schoolsWP de A a Z.

On se retrouve dans la lecon suivante.

---

**Points cles** :
- 3 triggers : Fluent Forms Submission, Tag Applied, List Applied
- Sequence type : livraison (J0) → bienvenue (H+1) → valeur (J+3) → offre (J+7)
- Actions complementaires : Apply/Remove Tag, Goal (arret si achat)
- Monitorer : taux d'ouverture, taux de clic, progression dans la sequence
- Bons taux d'ouverture : 40-60% premier email, 30-45% suivants
- Publier l'automation pour l'activer

**Mots cles SEO** : FluentCRM automation, sequence email WordPress, email automatique FluentForms, nurturing CRM WordPress

---

**Notes de production** :
- Face camera : intro + outro
- Screencast : creation complete de l'automation dans FluentCRM (~7 min)
- Slides : 2 slides (triggers disponibles + schema sequence)
- Ton : methodique, rythme pose — beaucoup d'etapes a configurer
