# Script video - Module 7, Lecon 6 : FluentForms + Google Sheets

**Formation** : FluentForms Masterclass Formulaires
**Code** : FRM-012 (premium)
**Module** : 7 - Ecosysteme et integrations
**Lecon** : 6/9 - FluentForms + Google Sheets
**Duree** : 6 min (~900 mots)
**Type** : Video HeyGen + voix ElevenLabs
**Ecran** : Face camera intro/outro, screencast config Google Sheets feed, slide cas d'usage
**Objectif** : Envoyer chaque soumission de formulaire dans un Google Sheet automatiquement

---

**[INTRO - face camera]**

Ton equipe commerciale travaille dans Google Sheets. Ton associe n'a pas acces a WordPress. Tu veux un suivi des leads en temps reel dans un tableur partage. FluentForms envoie chaque soumission dans Google Sheets automatiquement.

**[SECTION 1 - screencast "Connecter Google Sheets"]**

Direction FluentForms, Settings (global), Integrations. Cherche Google Sheets.

FluentForms utilise l'authentification Google OAuth. Clique sur "Connect Google Sheets". Tu vas etre redirige vers Google pour autoriser l'acces. Connecte-toi avec le compte Google qui possede les Sheets.

Autorise FluentForms a acceder a Google Sheets et Google Drive. Les permissions demandees sont : lire et ecrire dans tes spreadsheets. C'est tout.

Une fois autorise, tu reviens dans FluentForms. Le statut passe a "Connected".

**[SECTION 2 - screencast "Creer le Sheet"]**

Avant de configurer le feed, prepare ton Google Sheet.

Va dans Google Sheets, cree un nouveau spreadsheet. Nomme-le "Leads FluentForms - Janvier 2026" (ou un nom qui te convient).

Sur la premiere ligne, definis les headers - les noms de colonnes : Prenom, Email, Telephone, Message, Date, Source.

Ces headers doivent correspondre aux champs que tu veux envoyer depuis FluentForms. L'ordre n'a pas d'importance - c'est le mapping dans le feed qui fait la connexion.

**[SECTION 3 - screencast "Configurer le feed"]**

Retour dans FluentForms. Ouvre ton formulaire. Settings, Integrations, Google Sheets. Ajoute un feed.

Selectionne le spreadsheet que tu viens de creer. Selectionne l'onglet (sheet tab) - par defaut c'est "Sheet1".

Maintenant, le mapping. Pour chaque colonne du Sheet, selectionne le champ FluentForms correspondant.

Colonne "Prenom" → champ First Name du formulaire.
Colonne "Email" → champ Email.
Colonne "Telephone" → champ Phone.
Colonne "Message" → champ Textarea.
Colonne "Date" → tu peux utiliser le shortcode {date.date} pour inserer la date de soumission automatiquement.
Colonne "Source" → texte fixe "Formulaire Contact" (ou le nom du formulaire).

Sauvegarde. A chaque soumission, une nouvelle ligne est ajoutee dans le Google Sheet avec les donnees mappees.

**[SECTION 4 - screencast "Tester"]**

Soumets le formulaire en mode test. Va dans Google Sheets. Une nouvelle ligne devrait apparaitre avec les donnees que tu viens d'entrer.

Si la ligne n'apparait pas : verifie que la connexion Google est toujours active (les tokens expirent parfois). Verifie que le bon spreadsheet et le bon onglet sont selectionnes. Verifie que les headers dans le Sheet correspondent au mapping.

Si les donnees sont dans les mauvaises colonnes : verifie le mapping dans le feed. Chaque champ doit pointer vers la bonne colonne.

**[SECTION 5 - slide "Cas d'usage"]**

Centraliser les leads pour l'equipe commerciale. Le commercial ouvre le Sheet chaque matin et traite les nouveaux leads. Il ajoute ses notes dans des colonnes supplementaires (statut, date de relance, commentaire).

Reporting automatique. Avec Google Sheets, tu peux creer des graphiques, des tableaux croises, des formules. Nombre de leads par semaine, par source, par type. Le tout mis a jour en temps reel.

Collaboration. Le Sheet est partage avec qui tu veux - associe, freelance, equipe. Chacun voit les donnees sans avoir besoin d'un acces WordPress.

Backup des donnees. Les soumissions sont dans FluentForms ET dans Google Sheets. Double sauvegarde. Si tu perds ton WordPress, les donnees sont toujours dans le Sheet.

Export vers d'autres outils. Google Sheets se connecte a Data Studio, Notion, Airtable, et des dizaines d'autres outils. Le Sheet devient un hub de donnees.

**[SECTION 6 - screencast "Astuces avancees"]**

Quelques astuces pour tirer le maximum de l'integration.

Un Sheet par formulaire. Ne melange pas les leads du formulaire de contact et du formulaire de devis dans le meme Sheet. Chaque formulaire a son propre spreadsheet ou son propre onglet.

Formules de suivi. Ajoute une colonne "Statut" dans le Sheet (manuellement). Valeurs : "Nouveau", "Contacte", "En cours", "Gagne", "Perdu". L'equipe met a jour au fur et a mesure.

Mise en forme conditionnelle. Colore les lignes en rouge quand le statut est "Nouveau" depuis plus de 48h. Ca force l'equipe a reagir vite.

Notifications Sheet. Dans Google Sheets, tu peux activer les notifications quand le spreadsheet est modifie. Comme ca, le commercial recoit une alerte quand un nouveau lead arrive.

**[OUTRO - face camera]**

FluentForms et Google Sheets sont connectes. Tes donnees sont centralisees et partagees. Dans la prochaine lecon, on passe aux webhooks et a Zapier - pour connecter FluentForms a des milliers d'applications.

On se retrouve dans la lecon suivante.

---

**Points cles** :
- Connexion via Google OAuth : FluentForms Settings → Integrations → Google Sheets
- Creer le Sheet avec des headers avant de configurer le feed
- Mapping : chaque colonne du Sheet = un champ du formulaire
- Un Sheet par formulaire pour garder les donnees propres
- Cas d'usage : centralisation leads, reporting, collaboration, backup
- Astuces : formules de suivi, mise en forme conditionnelle, notifications

**Mots cles SEO** : FluentForms Google Sheets, formulaire WordPress Google Sheets, envoyer formulaire tableur, FluentForms spreadsheet

---

**Notes de production** :
- Face camera : intro (le besoin de centralisation) + outro (transition webhooks)
- Screencast : connexion + config feed + test (~4 min)
- Slide : 1 slide cas d'usage
- Ton : pratique, rapide - lecon courte et directe
