# Script video - Module 5, Lecon 2 : Configurer l'integration FluentForms vers FluentCRM

**Formation** : FluentForms Masterclass Formulaires
**Code** : FRM-012 (premium)
**Module** : 5 - FluentForms + FluentCRM
**Lecon** : 2/7 - Configurer l'integration FluentForms → FluentCRM
**Duree** : 8 min (~1100 mots)
**Type** : Video HeyGen + voix ElevenLabs
**Ecran** : Face camera intro/outro, screencast complet config integration
**Objectif** : Connecter un formulaire a FluentCRM avec mapping des champs, liste et tags

---

**[INTRO - face camera]**

On passe a la pratique. Tu as FluentForms et FluentCRM installes sur ton site. On va les connecter pour qu'a chaque soumission de formulaire, un contact soit cree automatiquement dans FluentCRM. Avec la bonne liste, les bons tags, et les bons champs.

**[SECTION 1 - screencast "Prerequis"]**

Avant de commencer, verifie que FluentCRM est installe et actif. Dashboard WordPress, Plugins, FluentCRM doit etre dans la liste.

Si ce n'est pas le cas, installe-le. FluentCRM a une version gratuite qui fait deja beaucoup - contacts, listes, tags, sequences email basiques. La version Pro ajoute les automations avancees, le scoring, et les rapports.

Pour cette lecon, la version gratuite de FluentCRM suffit.

Verifie aussi que FluentCRM est configure avec au moins un expediteur email. Si tu n'as pas encore configure FluentSMTP, fais-le avant - sinon tes emails risquent d'atterrir en spam. On verra ca en detail au module 7.

**[SECTION 2 - screencast "Acceder a l'integration"]**

Ouvre ton formulaire dans FluentForms. On va utiliser un formulaire simple - un formulaire de capture d'email avec Prenom et Email.

Va dans Settings du formulaire, puis Marketing & CRM Integrations. Tu vois la liste des integrations disponibles. Clique sur FluentCRM.

Clique sur "Add New FluentCRM Feed". Un feed, c'est une connexion entre ton formulaire et FluentCRM. Tu peux en avoir plusieurs par formulaire - on verra pourquoi plus tard.

**[SECTION 3 - screencast "Mapper les champs"]**

Premier ecran : le mapping des champs. C'est la que tu dis a FluentForms quel champ du formulaire correspond a quel champ dans FluentCRM.

Email : selectionne le champ Email de ton formulaire. C'est le seul champ obligatoire - FluentCRM utilise l'email comme identifiant unique.

First Name : selectionne le champ Prenom.

Last Name : si tu as un champ Nom de famille, mappe-le. Sinon, laisse vide.

Tu peux mapper d'autres champs si tu les as : telephone, adresse, entreprise, site web. FluentCRM a des champs standard pour tout ca. Et si tu as des champs custom dans FluentCRM, ils apparaissent aussi dans la liste.

**[SECTION 4 - screencast "Choisir la liste"]**

Deuxieme section : Lists. Selectionne la liste dans laquelle le contact sera ajoute.

Si tu n'as pas encore cree de listes dans FluentCRM, va dans FluentCRM, Contacts, Lists, et cree-en. Par exemple : "Newsletter", "Leads SEO", "Prospects Atelier".

Chaque formulaire devrait avoir sa propre liste. Ca te permet de savoir exactement d'ou vient chaque contact.

Selectionne la liste appropriee pour ce formulaire. Tu peux en selectionner plusieurs si le contact doit etre dans plusieurs listes.

**[SECTION 5 - screencast "Choisir les tags"]**

Troisieme section : Tags. Les tags qualifient le contact - son interet, sa source, son comportement.

Cree des tags parlants dans FluentCRM. Exemples : "source-formulaire-contact", "interest-seo", "lead-magnet-checklist".

Selectionne les tags a appliquer automatiquement quand ce formulaire est soumis.

La difference entre listes et tags : une liste est un groupement large (tous les contacts de la newsletter). Un tag est une qualification precise (interesse par le SEO, a telecharge le guide, prospect chaud).

Un contact peut etre dans une seule liste mais avoir 10 tags differents. Les tags sont le vrai outil de segmentation.

**[SECTION 6 - screencast "Double opt-in"]**

Derniere option importante : le double opt-in.

Si tu l'actives, le contact recoit un email de confirmation apres avoir soumis le formulaire. Il doit cliquer sur un lien pour confirmer son inscription. Tant qu'il n'a pas confirme, il reste en statut "pending" dans FluentCRM.

Avantage : tu es certain que l'email est valide et que la personne veut vraiment recevoir tes emails. Meilleure delivrabilite.

Inconvenient : tu perds entre 10 et 30% des contacts - ceux qui ne cliquent pas sur le lien de confirmation.

Ma recommandation : active le double opt-in pour les formulaires de newsletter et de lead magnet. Desactive-le pour les formulaires de contact, de devis ou de paiement - ces personnes t'ont deja fait confiance en te contactant ou en payant.

**[SECTION 7 - screencast "Tester l'integration"]**

Sauvegarde le feed. Ouvre le formulaire en preview. Remplis-le avec une adresse email de test.

Va dans FluentCRM, Contacts. Ton contact de test doit apparaitre. Verifie : le prenom est correct, l'email est correct, la liste est la bonne, les tags sont appliques.

Si le double opt-in est actif, verifie que l'email de confirmation arrive et que le statut passe de "pending" a "subscribed" apres le clic.

Si tout est bon, l'integration est operationnelle.

**[OUTRO - face camera]**

FluentForms et FluentCRM sont connectes. Chaque soumission cree un contact propre dans ton CRM. Dans la prochaine lecon, on approfondit les listes et les tags - comment les organiser pour une segmentation efficace.

On se retrouve dans la lecon suivante.

---

**Points cles** :
- Marketing & CRM Integrations → FluentCRM → Add New Feed
- Mapping : email (obligatoire) + prenom + nom + champs custom
- Liste : une par source/formulaire
- Tags : qualification precise du contact (interet, source, comportement)
- Double opt-in : activer pour newsletter/lead magnet, desactiver pour contact/paiement
- Tester : soumettre le formulaire et verifier dans FluentCRM

**Mots cles SEO** : FluentForms FluentCRM configuration, connecter formulaire CRM WordPress, FluentCRM integration, FluentForms tags automatiques

---

**Notes de production** :
- Face camera : intro + outro
- Screencast : config complete de l'integration (~6 min)
- Slides : aucune - tout en screencast
- Ton : pas a pas, methodique - le viewer doit pouvoir reproduire en temps reel
