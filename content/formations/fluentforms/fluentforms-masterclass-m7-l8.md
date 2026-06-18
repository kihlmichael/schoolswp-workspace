# Script video - Module 7, Lecon 8 : Formulaires RGPD conformes

**Formation** : FluentForms Masterclass Formulaires
**Code** : FRM-012 (premium)
**Module** : 7 - Ecosysteme et integrations
**Lecon** : 8/9 - Formulaires RGPD conformes
**Duree** : 10 min (~1300 mots)
**Type** : Video HeyGen + voix ElevenLabs
**Ecran** : Face camera intro/outro, screencast settings RGPD, slides obligations legales
**Objectif** : Rendre ses formulaires conformes au RGPD avec consentement, retention et droits utilisateur

---

**[INTRO - face camera]**

Le RGPD n'est pas optionnel en France. Un formulaire qui collecte des donnees personnelles sans consentement explicite, c'est un risque legal. Et les amendes ne sont pas symboliques - on parle de 2 a 4% du chiffre d'affaires annuel.

On va configurer FluentForms pour etre en conformite. Pas le minimum syndical - la conformite complete.

**[SECTION 1 - slide "Les 4 obligations RGPD pour les formulaires"]**

Obligation 1 - Consentement explicite. Le visiteur doit cocher une case pour accepter le traitement de ses donnees. Pas de case pre-cochee. Pas de consentement implicite. Une action deliberee.

Obligation 2 - Information transparente. Le visiteur doit savoir pourquoi tu collectes ses donnees, comment tu les utilises, combien de temps tu les conserves, et a qui tu les transmets. Lien vers ta politique de confidentialite obligatoire.

Obligation 3 - Droit d'acces et de suppression. Le visiteur peut demander a voir ses donnees et a les faire supprimer. Tu dois pouvoir repondre a cette demande dans un delai raisonnable (30 jours maximum).

Obligation 4 - Minimisation des donnees. Tu ne collectes que les donnees necessaires a la finalite declaree. Un formulaire de newsletter qui demande l'adresse postale, le numero de telephone et la date de naissance - c'est disproportionne.

**[SECTION 2 - screencast "Activer les settings RGPD de FluentForms"]**

FluentForms a des reglages RGPD integres. Direction FluentForms, Settings, Global Settings. Cherche la section GDPR.

Active "Enable GDPR Compliance". Ca active plusieurs fonctionnalites :
- La possibilite d'ajouter des champs RGPD aux formulaires
- La retention automatique des donnees (suppression apres X jours)
- L'export et la suppression des donnees utilisateur

**[SECTION 3 - screencast "Checkbox de consentement"]**

Dans chaque formulaire qui collecte des donnees personnelles, ajoute un champ GDPR Agreement ou une Checkbox Terms & Conditions.

Le texte doit etre clair et specifique. Pas "J'accepte les conditions generales" - c'est trop vague.

Bon exemple : "J'accepte que mes donnees (nom, email) soient utilisees pour repondre a ma demande et m'envoyer des communications liees a schoolsWP. Politique de confidentialite."

Le lien "Politique de confidentialite" pointe vers ta page dediee.

Rends ce champ obligatoire. Sans la case cochee, le formulaire ne peut pas etre soumis.

Pour les formulaires de newsletter, sois encore plus specifique : "J'accepte de recevoir la newsletter schoolsWP par email. Je peux me desinscrire a tout moment via le lien en bas de chaque email."

**[SECTION 4 - screencast "Data retention"]**

La retention des donnees, c'est la duree pendant laquelle tu conserves les soumissions.

FluentForms permet de configurer une suppression automatique. Settings, GDPR, Data Retention. Definis un nombre de jours.

Pour un formulaire de contact : 365 jours. Apres un an, si le contact n'est pas devenu client, la soumission est supprimee automatiquement.

Pour un formulaire de paiement : conserve plus longtemps - les obligations comptables imposent souvent 6 a 10 ans pour les factures.

Pour un formulaire de newsletter : tant que le contact est inscrit. Les donnees sont supprimees quand il se desinscrit.

La retention automatique te protege. Tu ne conserves pas des donnees inutiles pendant des annees. Et en cas de controle CNIL, tu peux montrer que tu as un processus de suppression en place.

**[SECTION 5 - screencast "Export et suppression des donnees"]**

Un visiteur te demande : "Quelles donnees avez-vous sur moi ?" ou "Supprimez toutes mes donnees."

FluentForms te permet de repondre.

Export : FluentForms, Entries. Recherche par email. Tu trouves toutes les soumissions de cette personne. Exporte-les en CSV et envoie-les au demandeur.

Suppression : meme recherche. Selectionne les entrees et supprime-les. Les donnees sont retirees de la base WordPress.

Si le contact est aussi dans FluentCRM, fais la meme chose : recherche par email, exporte ou supprime.

Si le contact est dans Brevo ou Google Sheets, fais la meme chose dans chaque service. C'est la qu'on comprend l'avantage d'avoir tout dans WordPress - une seule base a gerer.

Documente chaque demande de suppression : qui a demande, quand, quelles donnees supprimees. C'est ta preuve de conformite.

**[SECTION 6 - screencast "Politique de confidentialite"]**

Tu as besoin d'une page de politique de confidentialite sur ton site. WordPress a un generateur integre : Settings, Privacy.

Cette page doit contenir :
- Qui est le responsable du traitement (toi, ton entreprise)
- Quelles donnees tu collectes et pourquoi
- Comment tu les utilises
- A qui tu les transmets (Brevo, Stripe, etc.)
- Combien de temps tu les conserves
- Les droits du visiteur (acces, rectification, suppression, opposition)
- Comment exercer ces droits (email de contact)

Ajoute le lien vers cette page dans chaque formulaire - dans le champ de consentement et/ou dans le footer du formulaire.

**[SECTION 7 - slide "Checklist RGPD formulaire"]**

Pour chaque formulaire, verifie ces 6 points.

Checkbox de consentement : present, obligatoire, texte clair et specifique.
Lien politique de confidentialite : present et fonctionnel.
Minimisation : tu ne demandes que les donnees necessaires.
Retention : duree definie et suppression automatique configuree.
Export/suppression : tu sais repondre a une demande en moins de 30 jours.
Sous-traitants : tu sais lister les services tiers qui recoivent les donnees (Stripe, Brevo, Google...).

Si les 6 cases sont cochees, ton formulaire est conforme.

**[OUTRO - face camera]**

Tes formulaires sont RGPD conformes. C'est une obligation legale, mais c'est aussi un signal de confiance pour tes visiteurs. Dans la derniere lecon du module - et de la formation - on termine avec un comparatif FluentForms vs WPForms vs Gravity Forms. Pour que tu saches exactement pourquoi on a fait ce choix.

On se retrouve dans la lecon suivante.

---

**Points cles** :
- 4 obligations : consentement explicite, information, droits d'acces/suppression, minimisation
- Checkbox RGPD obligatoire avec texte specifique + lien politique de confidentialite
- Data retention : suppression automatique selon la duree configuree
- Export/suppression : repondre aux demandes sous 30 jours
- Page politique de confidentialite obligatoire
- Checklist 6 points pour chaque formulaire

**Mots cles SEO** : FluentForms RGPD, formulaire WordPress RGPD, conformite GDPR formulaire, FluentForms donnees personnelles

---

**Notes de production** :
- Face camera : intro (le risque legal) + outro (transition comparatif)
- Screencast : config RGPD + checkbox + retention + export (~7 min)
- Slides : 2 slides (4 obligations + checklist)
- Ton : serieux mais pas alarmiste - montrer que la conformite est accessible
