# Script video - Module 5, Lecon 7 : Cas pratique - inscription formation → FluentCRM → TutorLMS

**Formation** : FluentForms Masterclass Formulaires
**Code** : FRM-012 (premium)
**Module** : 5 - FluentForms + FluentCRM
**Lecon** : 7/7 - Cas pratique : inscription formation → FluentCRM → TutorLMS
**Duree** : 10 min (~1300 mots)
**Type** : Video HeyGen + voix ElevenLabs
**Ecran** : Face camera intro/outro, screencast pipeline complet, slide schema ecosysteme
**Objectif** : Construire le pipeline formation schoolsWP : formulaire → CRM → LMS (gratuit) ou CRM → CartFlows (payant)

---

**[INTRO - face camera]**

Derniere lecon du module 5, et c'est la plus complete. On va connecter 4 outils de l'ecosysteme schoolsWP : FluentForms pour le formulaire, FluentCRM pour le CRM, TutorLMS pour la formation, et CartFlows pour le paiement.

Le scenario : un visiteur veut s'inscrire a une formation. Selon qu'elle est gratuite ou payante, le parcours est different. On construit les deux.

**[SECTION 1 - slide "Les deux parcours"]**

Parcours gratuit : formulaire d'inscription → FluentCRM (tag "inscrit-formation-X") → OttoKit ou automation cree le compte TutorLMS → email de bienvenue avec lien d'acces au cours.

Parcours payant : formulaire d'inscription → FluentCRM (tag "interest-formation-X") → redirection vers funnel CartFlows → paiement → FluentCRM (tag "bought-formation-X") → acces TutorLMS → email de bienvenue.

La difference : pour le gratuit, l'acces est donne immediatement. Pour le payant, il y a une etape de paiement via CartFlows avant de debloquer l'acces.

**[SECTION 2 - screencast "Formulaire d'inscription"]**

Cree un nouveau formulaire. "Inscription Formation WordPress".

Champs : Prenom, Email, et un Select "Quelle formation t'interesse ?". Options :
- "Les bases de WordPress (gratuit)"
- "Maitriser le SEO WordPress (premium)"
- "FluentCRM de A a Z (premium)"

Ce select va determiner le parcours du contact.

Configure le feed FluentCRM principal : mapping email + prenom, liste "leads-formation", tag "source-formulaire-inscription".

Ajoute des feeds conditionnels :
- Si formation = "Les bases de WordPress (gratuit)" → tag "inscrit-formation-bases-wp"
- Si formation = "Maitriser le SEO WordPress (premium)" → tag "interest-formation-seo"
- Si formation = "FluentCRM de A a Z (premium)" → tag "interest-formation-fluentcrm"

**[SECTION 3 - screencast "Parcours gratuit : acces immediat"]**

Pour la formation gratuite, le contact recoit le tag "inscrit-formation-bases-wp". Deux options pour lui donner acces a TutorLMS.

Option 1 - OttoKit. Si tu as OttoKit installe, cree une automation : quand le tag "inscrit-formation-bases-wp" est ajoute dans FluentCRM → OttoKit inscrit automatiquement l'utilisateur au cours TutorLMS "Les bases de WordPress". Si le compte WordPress n'existe pas, OttoKit le cree d'abord.

Option 2 - Manuellement via FluentCRM. Dans l'automation FluentCRM, apres l'ajout du tag, envoie un email avec le lien d'inscription au cours TutorLMS. Le visiteur cree son compte et accede au cours. Moins automatise mais plus simple a mettre en place.

Pour schoolsWP, on utilise l'option 1 - OttoKit gere la creation de compte et l'inscription au cours automatiquement.

**[SECTION 4 - screencast "Parcours payant : redirection CartFlows"]**

Pour les formations premium, le contact recoit un tag "interest-formation-X". Pas un tag "inscrit" - il n'a pas encore paye.

Configure la confirmation du formulaire en mode conditionnel.

Si formation = "Maitriser le SEO WordPress (premium)" → redirection vers la page CartFlows du funnel SEO. L'URL : ton-site.com/checkout-formation-seo/.

Si formation = "FluentCRM de A a Z (premium)" → redirection vers la page CartFlows du funnel FluentCRM.

Le contact arrive sur le checkout CartFlows. Il paie. CartFlows declenche l'acces WooCommerce. WooCommerce + TutorLMS debloquent le cours.

Cote FluentCRM, CartFlows ou WooCommerce ajoute le tag "bought-formation-seo" apres le paiement. L'automation FluentCRM detecte ce tag et envoie l'email de bienvenue formation.

**[SECTION 5 - screencast "Email de bienvenue formation"]**

Cree une automation FluentCRM declenchee par le tag "inscrit-formation-bases-wp" (gratuit) ou "bought-formation-seo" (payant).

Email de bienvenue. Objet : "Bienvenue dans la formation - ton acces est pret".

Corps :
- Lien direct vers le cours dans TutorLMS
- Rappel de ce que la formation contient (modules, objectifs)
- Conseil pour demarrer : "Commence par le module 1, ca prend 15 minutes"
- Lien vers le groupe communaute si tu en as un
- Contact support si probleme d'acces

Cet email est critique. C'est le premier contact apres l'inscription. Il doit etre clair, accueillant et donner envie de commencer immediatement.

**[SECTION 6 - slide "Schema ecosysteme complet"]**

Recapitulatif visuel.

FluentForms : point d'entree. Collecte le prenom, l'email, le choix de formation.

FluentCRM : cerveau. Stocke le contact, assigne tags et listes, declenche les automations, envoie les emails.

CartFlows : encaissement. Funnels de vente pour les formations payantes. Checkout optimise.

TutorLMS : livraison. Heberge les cours, gere les inscriptions, suit la progression.

OttoKit : colle. Connecte FluentCRM a TutorLMS pour les inscriptions automatiques.

Chaque outil fait ce qu'il fait le mieux. Pas de duplication. Pas de bricolage. C'est l'ecosysteme WordPress natif.

**[SECTION 7 - screencast "Tester le parcours complet"]**

Teste les deux parcours.

Parcours gratuit : remplis le formulaire avec "Les bases de WordPress". Verifie dans FluentCRM : contact cree, tags corrects. Verifie dans TutorLMS : inscription au cours. Verifie l'email de bienvenue.

Parcours payant : remplis le formulaire avec "Maitriser le SEO WordPress". Verifie la redirection vers CartFlows. Simule un paiement test. Verifie le tag "bought-formation-seo" dans FluentCRM. Verifie l'acces TutorLMS. Verifie l'email de bienvenue.

Si une etape ne fonctionne pas, verifie les connexions entre les outils dans l'ordre : formulaire → feed CRM → automation → action.

**[OUTRO - face camera]**

Tu as le pipeline formation complet. Formulaire, CRM, paiement, LMS - tout connecte, tout automatise.

Le module 5 est termine. Tu maitrises l'integration FluentForms et FluentCRM. Dans le prochain module, on explore les quiz, les surveys et les analytics - des outils pour collecter de l'intelligence, pas juste des donnees.

On se retrouve au module 6.

---

**Points cles** :
- Deux parcours : gratuit (acces immediat via OttoKit) et payant (CartFlows → paiement → acces)
- Tags : "inscrit-formation-X" (gratuit) vs "interest-formation-X" puis "bought-formation-X" (payant)
- Confirmation conditionnelle : redirection vers le bon funnel CartFlows
- Email de bienvenue : lien d'acces, contenu de la formation, conseil pour demarrer
- Ecosysteme : FluentForms + FluentCRM + CartFlows + TutorLMS + OttoKit
- Tester les deux parcours de bout en bout

**Mots cles SEO** : FluentForms TutorLMS integration, pipeline formation WordPress, FluentCRM formation, inscription cours WordPress automatique

---

**Notes de production** :
- Face camera : intro (ecosysteme complet) + outro (transition module 6)
- Screencast : formulaire + automations + test (~7 min)
- Slides : 2 slides (deux parcours + schema ecosysteme)
- Ton : oriente systeme - montrer que les outils communiquent entre eux nativement
