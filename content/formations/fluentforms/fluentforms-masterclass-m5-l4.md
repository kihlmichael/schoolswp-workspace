# Script video - Module 5, Lecon 4 : Tags dynamiques selon les reponses

**Formation** : FluentForms Masterclass Formulaires
**Code** : FRM-012 (premium)
**Module** : 5 - FluentForms + FluentCRM
**Lecon** : 4/7 - Tags dynamiques selon les reponses
**Duree** : 10 min (~1300 mots)
**Type** : Video HeyGen + voix ElevenLabs
**Ecran** : Face camera intro/outro, screencast config conditional tags, slide schema
**Objectif** : Assigner des tags differents selon les reponses du visiteur dans le formulaire

---

**[INTRO - face camera]**

Jusqu'ici, chaque formulaire assigne les memes tags a tous les contacts. Que le visiteur soit un freelance avec un budget de 500 euros ou un directeur marketing avec 50 000 euros, il recoit les memes tags.

Ca, c'est insuffisant. Les tags dynamiques resolvent ce probleme. Le tag change selon ce que le visiteur a repondu. Et ca change tout pour la qualification commerciale.

**[SECTION 1 - slide "Le principe"]**

Le principe est simple.

Tu as un champ select, radio ou checkbox dans ton formulaire. Selon la valeur selectionnee, FluentForms assigne un tag different dans FluentCRM.

Exemple concret. Ton formulaire de devis a un champ "Budget". Trois options : moins de 1000 euros, entre 1000 et 5000 euros, plus de 5000 euros.

Si le visiteur choisit "moins de 1000 euros" → tag "budget-small".
Si "entre 1000 et 5000 euros" → tag "budget-medium".
Si "plus de 5000 euros" → tag "budget-enterprise".

Le commercial qui recoit la notification sait immediatement la valeur du lead sans avoir a lire les details du formulaire.

**[SECTION 2 - screencast "Configurer le conditional tag"]**

Ouvre ton formulaire dans FluentForms. On va prendre un formulaire de devis avec un champ Select "Budget" et un champ Select "Type de projet".

Va dans Settings, Marketing & CRM, FluentCRM. Ouvre le feed existant ou cree-en un nouveau.

Dans la section Tags, au lieu de selectionner des tags fixes, clique sur "Enable Conditional Tag Assignment" ou utilise le mode conditionnel.

La methode la plus flexible : creer plusieurs feeds FluentCRM pour le meme formulaire, chacun avec une condition differente.

**[SECTION 3 - screencast "Methode multi-feeds"]**

Voici comment ca marche. Au lieu d'un seul feed, tu en crees trois.

Feed 1 : condition "Budget IS Less than 1000 euros". Tags : "budget-small", "status-prospect". Liste : "prospects".

Feed 2 : condition "Budget IS 1000-5000 euros". Tags : "budget-medium", "status-prospect". Liste : "prospects".

Feed 3 : condition "Budget IS More than 5000 euros". Tags : "budget-enterprise", "status-prospect-premium". Liste : "prospects".

Chaque feed a une condition. Seul le feed dont la condition est remplie s'execute. Si le visiteur choisit "plus de 5000 euros", seul le feed 3 s'active. Le contact recoit les tags "budget-enterprise" et "status-prospect-premium".

**[SECTION 4 - screencast "Cas pratique : qualifier un lead"]**

On va construire un cas complet. Formulaire de demande de devis pour un site WordPress.

Champs :
- Name, Email, Phone
- Select "Type de projet" : Site vitrine, Site e-commerce, Application web
- Select "Budget" : Moins de 1000 euros, 1000-5000 euros, Plus de 5000 euros
- Select "Delai" : Urgent (moins d'1 mois), Normal (1-3 mois), Flexible
- Textarea "Description du projet"

Maintenant, les feeds FluentCRM :

Feed principal : s'execute toujours. Mapping email + nom + telephone. Liste : "prospects". Tags : "source-formulaire-devis".

Feed "budget-small" : condition Budget = Moins de 1000 euros. Tag additionnel : "budget-small".

Feed "budget-medium" : condition Budget = 1000-5000 euros. Tag additionnel : "budget-medium".

Feed "budget-enterprise" : condition Budget = Plus de 5000 euros. Tags additionnels : "budget-enterprise", "priority-high".

Feed "urgent" : condition Delai = Urgent. Tag additionnel : "delai-urgent".

Feed "ecommerce" : condition Type de projet = Site e-commerce. Tag additionnel : "interest-ecommerce".

Au total, 6 feeds. Le feed principal s'execute toujours. Les autres s'activent selon les reponses. Un contact qui demande un site e-commerce a plus de 5000 euros en urgence recoit les tags : "source-formulaire-devis", "budget-enterprise", "priority-high", "delai-urgent", "interest-ecommerce".

C'est un lead premium. Tu le vois immediatement dans FluentCRM.

**[SECTION 5 - slide "Impact commercial"]**

Voici ce que ca change pour ton business.

Priorisation automatique. Les leads "budget-enterprise" + "delai-urgent" recoivent une reponse dans l'heure. Les leads "budget-small" + "flexible" recoivent un email automatique avec tes tarifs standards.

Sequence email personnalisee. Un lead "interest-ecommerce" recoit une sequence avec des temoignages de sites e-commerce. Un lead "interest-site-vitrine" recoit des exemples de sites vitrines.

Scoring. Dans FluentCRM Pro, tu peux attribuer des points selon les tags. "budget-enterprise" = +50 points. "delai-urgent" = +30 points. Les leads avec le score le plus eleve remontent en haut de ta liste.

Les tags dynamiques sont le pont entre les donnees brutes du formulaire et l'intelligence commerciale de ton CRM.

**[SECTION 6 - screencast "Tester"]**

Teste le formulaire avec differentes combinaisons.

Soumission 1 : budget small, site vitrine, flexible. Verifie dans FluentCRM : tags "source-formulaire-devis" + "budget-small".

Soumission 2 : budget enterprise, e-commerce, urgent. Verifie : tags "source-formulaire-devis" + "budget-enterprise" + "priority-high" + "delai-urgent" + "interest-ecommerce".

Si les tags ne s'appliquent pas, verifie les conditions de chaque feed. L'erreur la plus courante : la valeur dans la condition ne correspond pas exactement a la valeur de l'option du champ. Attention aux espaces, aux accents et a la casse.

**[OUTRO - face camera]**

Tes formulaires qualifient maintenant chaque lead automatiquement. Dans la prochaine lecon, on utilise ces tags pour declencher des automations FluentCRM - des sequences email qui partent toutes seules.

On se retrouve dans la lecon suivante.

---

**Points cles** :
- Tags dynamiques : le tag change selon la reponse du visiteur
- Methode : plusieurs feeds FluentCRM avec conditions differentes
- Feed principal (toujours actif) + feeds conditionnels (par reponse)
- Impact : priorisation commerciale, sequences personnalisees, scoring
- Tester chaque combinaison et verifier les tags dans FluentCRM
- Attention aux valeurs exactes dans les conditions (espaces, accents, casse)

**Mots cles SEO** : FluentForms tags conditionnels, FluentCRM tag dynamique, qualifier leads WordPress, segmentation avancee FluentCRM

---

**Notes de production** :
- Face camera : intro (probleme des tags fixes) + outro (transition automations)
- Screencast : creation des feeds conditionnels + test (~7 min)
- Slides : 2 slides (principe + impact commercial)
- Ton : oriente business - montrer la valeur commerciale des tags dynamiques
