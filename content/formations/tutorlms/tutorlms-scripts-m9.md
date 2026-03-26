# Scripts video — Module 9 : Communication & Emails

**Formation** : Maitriser TutorLMS
**Module** : M9 — Communication & Emails (Premium)
**Lecons** : 6 videos + 1 quiz
**Duree totale** : ~35 min
**Date** : 2026-03-23

---

### Lecon 9.1 — Email template builder

**Duree** : 6 min
**Type** : Video HeyGen
**Ecran** : Face camera pour intro/conclusion, screencast du panneau Email
**Source** : Video #27 + doc email-notifications

---

**[INTRO — face camera]**

TutorLMS envoie des emails a chaque etape cle : inscription a un cours, completion, resultat de quiz, nouveau commentaire Q&A. Le probleme, c'est que les emails par defaut sont generiques et impersonnels. Dans cette lecon, on va les personnaliser avec le template builder integre.

**[ECRAN — screencast WordPress admin]**

[Navigation vers Tutor LMS > Settings > Email]

Va dans Tutor LMS, Settings, puis Email. Tu arrives sur le panneau de configuration des emails. Premiere chose : verifie que le toggle "Enable Email Notification" est active. Sans ca, TutorLMS n'envoie rien.

**[ECRAN — screencast panneau Email]**

[Vue des options globales : Notification From, Sender Address, Footer Text]

En haut, tu as trois reglages globaux :

1. Notification From — le nom d'expediteur. Mets le nom de ta plateforme, pas "WordPress" ou "admin".
2. Sender Email Address — l'adresse d'envoi. Utilise une adresse sur ton domaine, pas une adresse Gmail.
3. Footer Text — le pied de page commun a tous les emails.

La recommandation schoolsWP : utilise un expediteur du type "Formation schoolsWP" avec une adresse noreply@tondomaine.com. Ca fait professionnel et ca evite les filtres anti-spam.

**[ECRAN — screencast liste des templates]**

[Defilement de la liste des evenements email]

En dessous, tu as la liste de tous les evenements qui declenchent un email. Chaque evenement a un toggle pour l'activer ou le desactiver. Les principaux :

Pour les etudiants :
- Enrollment — quand un eleve s'inscrit a un cours
- Course Completed — quand il termine le cours
- Quiz Completed — apres chaque quiz
- Assignment Submitted — confirmation de soumission d'un devoir

Pour les instructeurs :
- New Student Enrolled — notification quand un nouvel eleve rejoint le cours
- New Q&A Message — quand un eleve pose une question
- Assignment Submitted — quand un devoir est soumis

Pour les administrateurs :
- New Instructor Registration — quand un instructeur demande son compte
- New Course Published — quand un cours est soumis pour relecture

**[ECRAN — screencast edition d'un template]**

[Clique sur un evenement, par exemple "Enrollment"]

Clique sur un evenement pour le personnaliser. Tu arrives dans l'editeur de template. Tu as :

- Subject — l'objet de l'email
- Heading — le titre principal dans le corps de l'email
- Message — le contenu avec un editeur visuel

L'editeur supporte le HTML basique et surtout les placeholders — des variables dynamiques qu'on remplacera automatiquement. Par exemple, {student_name} sera remplace par le prenom de l'eleve, {course_name} par le nom du cours. On verra la liste complete des placeholders dans la lecon 9.6.

**[ECRAN — screencast preview email]**

[Montre le bouton Preview et le rendu]

Avant d'enregistrer, utilise le bouton Preview pour voir le rendu final. Ca t'evite les mauvaises surprises — un placeholder mal ferme, un titre trop long, un lien casse.

**[TRANSITION — face camera]**

Personnalise au minimum les emails d'inscription et de completion de cours. Ce sont les deux que tes eleves voient le plus. Met ton nom de marque, un message d'accueil clair, et un lien vers le cours. Dans la prochaine lecon, on passe aux notifications on-site — celles qui apparaissent directement dans l'interface.

---

**Points cles** :
- Activation : Settings > Email > Enable Email Notification
- 3 reglages globaux : Notification From, Sender Email, Footer Text
- Chaque evenement a un toggle + template personnalisable (subject, heading, message)
- Placeholders dynamiques pour personnaliser ({student_name}, {course_name}, etc.)
- Toujours verifier avec Preview avant d'enregistrer
- Priorite : personnaliser Enrollment + Course Completed en premier

**Mots cles SEO** : TutorLMS email template, personnaliser emails TutorLMS, notifications email LMS WordPress, TutorLMS email builder

---

### Lecon 9.2 — Notifications on-site & push

**Duree** : 5 min
**Type** : Video HeyGen
**Ecran** : Face camera pour intro/conclusion, screencast panneau Notifications
**Source** : Video #11 + doc notifications

---

**[INTRO — face camera]**

Les emails c'est bien, mais tes eleves ne les lisent pas toujours. Les notifications on-site, elles, apparaissent directement dans l'interface TutorLMS — comme sur Facebook ou YouTube. L'eleve voit une cloche avec un badge, il clique, il voit ce qui s'est passe. C'est immediat et ca ne depend pas de la boite mail.

**[ECRAN — screencast WordPress admin]**

[Navigation vers Tutor LMS > Settings > Notifications]

Va dans Tutor LMS, Settings, puis cherche la section Notifications. Tu as deux blocs : les notifications on-site (dans le navigateur) et les notifications push (optionnelles).

**[ECRAN — screencast panneau Notifications]**

[Vue du toggle principal et de la liste des evenements]

Active le toggle principal "Enable On-Site Notification". En dessous, tu retrouves une liste d'evenements similaire aux emails — mais cette fois, la notification s'affiche dans l'interface du site.

Les evenements les plus utiles :

Pour les etudiants :
- Course Enrollment — confirmation d'inscription
- Quiz Graded — resultat de quiz disponible
- Announcement Posted — l'instructeur a publie une annonce (on verra ca en lecon 9.3)
- Q&A Reply — reponse a sa question

Pour les instructeurs :
- New Q&A Question — un eleve a pose une question
- Assignment to Review — un devoir est en attente de correction
- New Enrollment — un eleve rejoint le cours

**[ECRAN — screencast front-end cloche notification]**

[Montre la cloche de notification dans le header du site, cote eleve]

Cote front-end, l'eleve voit une icone cloche dans le header. Le badge affiche le nombre de notifications non lues. Un clic ouvre le panneau avec la liste. Chaque notification contient un lien direct vers le contenu concerne — le cours, le quiz, la discussion Q&A.

**[ECRAN — screencast parametres push]**

[Montre les options push si disponibles]

TutorLMS propose aussi les notifications push via le navigateur. C'est la notification qui apparait meme quand l'eleve n'est pas sur ton site — comme une notification de telephone, mais sur desktop. Pour l'activer, il faut que ton site soit en HTTPS (obligatoire) et que l'eleve accepte les notifications dans son navigateur.

Mon avis : les notifications on-site sont indispensables, les push sont un bonus. Active les on-site en priorite.

**[TRANSITION — face camera]**

Les notifications on-site et les emails sont complementaires. L'email confirme, la notification on-site rappelle. Active les deux pour les evenements importants — inscription, completion, Q&A. Dans la prochaine lecon, on decouvre les annonces — un outil pour communiquer directement avec les eleves d'un cours specifique.

---

**Points cles** :
- Activation : Settings > Notifications > Enable On-Site Notification
- Notifications apparaissent dans la cloche du header front-end
- Evenements principaux : enrollment, quiz graded, announcement, Q&A reply
- Push notifications disponibles (HTTPS requis + autorisation navigateur)
- Recommandation : activer on-site en priorite, push en complement
- Complementaire aux emails — pas un remplacement

**Mots cles SEO** : TutorLMS notifications, notifications on-site LMS, push notifications TutorLMS, alertes eleves WordPress

---

### Lecon 9.3 — Annonces

**Duree** : 5 min
**Type** : Video HeyGen
**Ecran** : Face camera pour intro/conclusion, screencast Course Builder + front-end
**Source** : doc menus/announcement

---

**[INTRO — face camera]**

Tu dois prevenir tes eleves d'une mise a jour de contenu, d'un live prevu la semaine prochaine, ou d'un changement de planning ? Les annonces TutorLMS sont faites pour ca. C'est un systeme de communication cible — tu publies une annonce dans un cours, et seuls les eleves inscrits a ce cours la voient.

**[ECRAN — screencast WordPress admin]**

[Navigation vers Tutor LMS > un cours > onglet Announcements]

Ouvre n'importe quel cours dans TutorLMS. Dans le menu du cours, tu trouves l'onglet Announcements. C'est ici que tu geres toutes les annonces liees a ce cours.

**[ECRAN — screencast creation d'une annonce]**

[Clique sur "Add New Announcement"]

Clique sur "Add New Announcement". Tu as deux champs :

1. Titre — l'objet de l'annonce. Sois concis : "Nouveau module disponible", "Live Q&A vendredi 14h", "Mise a jour de la lecon 5".
2. Contenu — le corps du message. L'editeur supporte le texte riche, les liens, les images. Tu peux detailler autant que necessaire.

Publie. L'annonce est immediatement visible pour tous les eleves inscrits au cours.

**[ECRAN — screencast front-end annonce]**

[Montre l'onglet Announcements sur la page du cours cote eleve]

Cote eleve, les annonces apparaissent dans l'onglet "Announcements" sur la page du cours. L'annonce la plus recente est en haut. L'eleve voit le titre, la date, et peut cliquer pour lire le contenu complet.

Si les notifications on-site sont activees (lecon precedente), l'eleve recoit aussi une notification dans sa cloche. Et si l'evenement email correspondant est active, il recoit un email. Trois canaux pour une seule action — c'est la force du systeme.

**[ECRAN — screencast liste des annonces]**

[Montre la liste des annonces existantes avec options modifier/supprimer]

Tu retrouves toutes tes annonces dans la liste. Tu peux les modifier ou les supprimer a tout moment. Les annonces sont specifiques a chaque cours — une annonce publiee dans le cours A n'apparait pas dans le cours B.

**[ECRAN — screencast cas d'usage]**

[Montre un exemple concret d'annonce bien redigee]

Quelques bonnes pratiques :

- Un titre clair et actionnable — pas "Information" mais "Nouveau quiz disponible — teste tes connaissances"
- Un contenu court — l'annonce n'est pas un article de blog, c'est un message cible
- Un lien si necessaire — vers la lecon concernee, un formulaire, un replay
- Une frequence raisonnable — une annonce par semaine maximum, sinon tes eleves decrochent

**[TRANSITION — face camera]**

Les annonces sont parfaites pour maintenir l'engagement dans un cours. Utilise-les pour les mises a jour importantes, pas pour du remplissage. Prochaine lecon : le systeme de Q&A, qui permet a tes eleves de poser des questions directement dans les lecons.

---

**Points cles** :
- Acces : page du cours > onglet Announcements > Add New Announcement
- Deux champs : titre + contenu (texte riche)
- Visibles uniquement par les eleves inscrits au cours
- Declenchent notification on-site + email si actives
- Specifiques a chaque cours — pas de diffusion globale
- Bonne pratique : une annonce par semaine max, titre actionnable, contenu court

**Mots cles SEO** : TutorLMS annonces, announcements TutorLMS, communiquer eleves LMS WordPress, annonces cours en ligne

---

### Lecon 9.4 — Q&A etudiants/instructeurs

**Duree** : 6 min
**Type** : Video HeyGen
**Ecran** : Face camera pour intro/conclusion, screencast Q&A front-end + admin
**Source** : doc tutorials/qa

---

**[INTRO — face camera]**

Quand un eleve bloque sur une lecon, il doit pouvoir poser sa question sans quitter la page. C'est exactement ce que fait le Q&A integre de TutorLMS. Chaque lecon a son propre fil de discussion. L'eleve pose sa question, l'instructeur repond, et toute la classe en beneficie. C'est comme un mini-forum contextuel.

**[ECRAN — screencast WordPress admin]**

[Navigation vers Tutor LMS > Settings > recherche Q&A]

D'abord, verifie que le Q&A est active. Va dans Tutor LMS, Settings, et cherche l'option "Q&A" ou "Enable Q&A for course". Active le toggle. Sans ca, les eleves ne voient pas l'onglet Q&A dans les lecons.

**[ECRAN — screencast front-end lecon]**

[Montre l'onglet Q&A sous le contenu d'une lecon]

Cote eleve, quand le Q&A est active, un onglet "Q&A" apparait sous le contenu de chaque lecon. L'eleve clique dessus et voit les questions existantes. Il peut poser une nouvelle question ou repondre a une question existante.

**[ECRAN — screencast creation d'une question]**

[Montre le formulaire de soumission Q&A]

Pour poser une question, l'eleve clique sur "Ask a new question". Il a deux champs :
- Le titre — la question en une phrase
- Le contenu — les details, le contexte, ce qu'il a deja essaye

Il peut aussi cocher une option pour rendre la question privee — visible uniquement par l'instructeur. Utile si la question est personnelle ou specifique.

**[ECRAN — screencast reponse instructeur]**

[Montre la vue instructeur du Q&A dans le dashboard]

Cote instructeur, tu retrouves toutes les questions dans ton dashboard, section Q&A. Tu vois :
- Les questions en attente de reponse (marquees comme non lues)
- Le cours et la lecon concernes
- La date et l'auteur

Clique sur une question pour repondre. Ta reponse est publiee immediatement. L'eleve recoit une notification (on-site + email si actives).

**[ECRAN — screencast moderation Q&A]**

[Montre les options de moderation]

En tant qu'instructeur ou admin, tu as des options de moderation :
- Marquer une question comme resolue — ca la signale visuellement dans la liste
- Supprimer une question inappropriee
- Repondre publiquement ou en prive

Le Q&A fonctionne aussi pour les quiz et les devoirs — pas uniquement les lecons video ou texte.

**[ECRAN — screencast vue globale Q&A admin]**

[Montre la page Q&A dans le menu admin Tutor LMS]

En tant qu'admin, tu as aussi une vue globale de toutes les questions Q&A de la plateforme. Ca te permet de surveiller les questions sans reponse, identifier les lecons qui posent probleme, et intervenir si un instructeur ne repond pas.

**[TRANSITION — face camera]**

Le Q&A est un outil d'engagement puissant. Un eleve qui pose une question est un eleve implique. Un instructeur qui repond rapidement est un instructeur qui fidélise. Surveille les questions sans reponse — c'est un indicateur de sante de ta formation. Prochaine lecon : le feedback instructeur, un autre canal de communication direct.

---

**Points cles** :
- Activation : Settings > Q&A > Enable
- Onglet Q&A sous chaque lecon, quiz et devoir
- Questions publiques ou privees (choix de l'eleve)
- Instructeur repond depuis son dashboard > Q&A
- Options : marquer comme resolu, supprimer, repondre en prive
- Vue admin globale pour surveiller les questions sans reponse
- Declenchent notifications on-site + email

**Mots cles SEO** : TutorLMS Q&A, questions reponses LMS WordPress, forum discussion TutorLMS, interaction eleves instructeurs TutorLMS

---

### Lecon 9.5 — Feedback instructeur

**Duree** : 5 min
**Type** : Video HeyGen
**Ecran** : Face camera pour intro/conclusion, screencast feedback dans le Course Builder
**Source** : doc tutorials/give-feedback

---

**[INTRO — face camera]**

Le Q&A est public — tout le monde voit les questions et les reponses. Mais parfois, tu as besoin d'un retour individuel et prive. C'est le role du feedback instructeur dans TutorLMS. Tu corriges un devoir, tu evalues un quiz a reponse ouverte, tu veux guider un eleve personnellement — le feedback est ton outil.

**[ECRAN — screencast WordPress admin]**

[Navigation vers le dashboard instructeur > Assignments]

Le feedback s'utilise principalement dans deux contextes : les devoirs (assignments) et les quiz a correction manuelle. Commencons par les devoirs.

Va dans ton dashboard instructeur, section Assignments. Tu vois la liste des devoirs soumis par tes eleves, avec le statut : en attente, valide, ou rejete.

**[ECRAN — screencast correction d'un devoir]**

[Clique sur un devoir soumis pour le corriger]

Clique sur un devoir pour le corriger. Tu vois :
- Le fichier ou le texte soumis par l'eleve
- Les consignes du devoir pour reference
- La date de soumission

En bas, tu as la zone de feedback. C'est un editeur texte ou tu ecris ton retour. Sois precis : ce qui est bien, ce qui doit etre ameliore, et comment l'ameliorer. Un "bien" tout seul ne sert a rien. Un "ta structure est claire, mais la partie 3 manque d'exemples concrets — ajoute un cas pratique" est utile.

**[ECRAN — screencast notation + feedback]**

[Montre le champ de note et le bouton de validation]

Tu attribues une note (sur le bareme que tu as defini dans le devoir) et tu choisis :
- Approve — le devoir est valide
- Reject — le devoir est refuse, l'eleve doit recommencer

Dans les deux cas, ton feedback est envoye a l'eleve. S'il est refuse, l'eleve peut resoumettre — il verra ton feedback pour s'ameliorer.

**[ECRAN — screencast feedback sur quiz]**

[Montre un quiz a correction manuelle dans le dashboard]

Pour les quiz, le feedback fonctionne avec les questions a reponse ouverte — celles qui ne peuvent pas etre corrigees automatiquement. Tu retrouves les quiz en attente de correction dans ton dashboard, section Quiz Attempts.

Clique sur une tentative. Tu vois les reponses de l'eleve question par question. Pour chaque reponse ouverte, tu attribues les points et tu peux ajouter un commentaire.

**[ECRAN — screencast vue eleve du feedback]**

[Montre ce que l'eleve voit apres correction]

Cote eleve, le feedback apparait directement sur la page du devoir ou du quiz. L'eleve recoit une notification quand le feedback est disponible. Il voit ta note, ton commentaire, et si c'est un devoir refuse, le bouton pour resoumettre.

**[TRANSITION — face camera]**

Le feedback est ce qui fait la difference entre une plateforme de cours et une vraie formation. Un retour precis et constructif transforme un cours passif en experience d'apprentissage. Prends le temps de rediger des feedbacks utiles — tes eleves s'en souviendront. Derniere lecon du module : les placeholders email, pour automatiser la personnalisation de tes communications.

---

**Points cles** :
- Feedback disponible sur les devoirs (assignments) et les quiz a correction manuelle
- Devoirs : Approve ou Reject avec commentaire detaille
- Quiz : points + commentaire par question ouverte
- L'eleve voit le feedback sur la page du devoir/quiz + notification
- Devoir refuse = l'eleve peut resoumettre
- Bonne pratique : feedback precis et actionnable, jamais un simple "bien" ou "insuffisant"

**Mots cles SEO** : TutorLMS feedback instructeur, corriger devoirs TutorLMS, notation quiz TutorLMS, retour personnalise LMS WordPress

---

### Lecon 9.6 — Placeholders email

**Duree** : 6 min
**Type** : Video HeyGen
**Ecran** : Face camera pour intro/conclusion, screencast Email templates + placeholders
**Source** : doc tutorials/email-placeholders

---

**[INTRO — face camera]**

En lecon 9.1, on a vu comment personnaliser les templates email. Mais pour aller plus loin, tu dois maitriser les placeholders — ces variables dynamiques qui inserent automatiquement le nom de l'eleve, le titre du cours, la note d'un quiz. C'est ce qui transforme un email generique en message personnalise, sans effort manuel.

**[ECRAN — screencast WordPress admin]**

[Navigation vers Tutor LMS > Settings > Email > un template]

Retourne dans Settings, Email, et ouvre n'importe quel template. Dans l'editeur, tu vois un bouton ou un lien "Available Placeholders" — clique dessus pour afficher la liste des variables utilisables dans ce template.

**[ECRAN — screencast liste des placeholders]**

[Montre la liste des placeholders disponibles pour un template d'inscription]

Chaque template a ses propres placeholders. Voici les plus courants :

Placeholders globaux (disponibles partout) :
- {site_name} — le nom de ton site WordPress
- {site_url} — l'URL de ton site
- {logo} — le logo de ton site (si defini)

Placeholders eleve :
- {student_name} — prenom et nom de l'eleve
- {student_email} — adresse email
- {student_username} — nom d'utilisateur

Placeholders cours :
- {course_name} — titre du cours
- {course_url} — lien direct vers le cours
- {course_duration} — duree estimee du cours

Placeholders quiz :
- {quiz_name} — titre du quiz
- {quiz_score} — note obtenue
- {quiz_passing_grade} — note minimale pour reussir

**[ECRAN — screencast exemple concret]**

[Montre un template d'email de completion avec placeholders]

Prenons un exemple concret. Pour l'email de completion de cours, tu pourrais ecrire :

Sujet : Bravo {student_name} — tu as termine {course_name} !

Corps :
"Felicitations {student_name},

Tu as termine le cours {course_name}. C'est une belle etape.

Pour continuer ta progression, voici tes prochaines options :
- Reviens sur le cours : {course_url}
- Decouvre nos autres formations : {site_url}/cours

A bientot,
L'equipe {site_name}"

C'est personnalise, professionnel, et ca prend 30 secondes a configurer.

**[ECRAN — screencast placeholders avances]**

[Montre des placeholders specifiques aux devoirs et instructeurs]

Pour les templates lies aux devoirs :
- {assignment_name} — titre du devoir
- {assignment_comment} — le feedback que tu as redige (lecon 9.5)
- {assignment_score} — la note attribuee

Pour les templates instructeurs :
- {instructor_name} — nom de l'instructeur
- {instructor_email} — email de l'instructeur

**[ECRAN — screencast erreurs courantes]**

[Montre un placeholder mal ecrit et le resultat]

Attention aux erreurs courantes :
- Un placeholder mal orthographie — {studen_name} au lieu de {student_name} — s'affiche tel quel dans l'email. L'eleve voit la variable brute.
- Un placeholder utilise dans le mauvais template — {quiz_score} dans un email d'inscription ne donnera rien, parce qu'il n'y a pas de quiz a ce stade.
- Les accolades manquantes — student_name sans les {} n'est pas interprete.

Toujours utiliser le bouton Preview (lecon 9.1) pour verifier le rendu avant d'enregistrer.

**[TRANSITION — face camera]**

Les placeholders sont le lien entre tes templates email et les donnees de ta plateforme. Maitrise-les, et chaque email que TutorLMS envoie ressemblera a un message redige a la main. C'est la fin du Module 9 — tu sais maintenant gerer les emails, les notifications, les annonces, le Q&A, le feedback et les placeholders. Prochaine etape : le quiz du module pour valider tes acquis.

---

**Points cles** :
- Chaque template a ses propres placeholders — consulter "Available Placeholders"
- Placeholders globaux : {site_name}, {site_url}, {logo}
- Placeholders eleve : {student_name}, {student_email}
- Placeholders cours : {course_name}, {course_url}
- Placeholders quiz : {quiz_name}, {quiz_score}, {quiz_passing_grade}
- Erreurs courantes : faute d'orthographe, mauvais template, accolades manquantes
- Toujours previsualiser avec Preview

**Mots cles SEO** : TutorLMS placeholders email, variables email LMS WordPress, personnaliser notifications TutorLMS, email dynamique TutorLMS

---

### Lecon 9.7 — Quiz Module 9

**Type** : Quiz TutorLMS
**Questions** : 8 QCM
**Note de passage** : 70% (6/8)
**Tentatives** : illimitees

---

**Question 1**

Ou active-t-on les notifications email dans TutorLMS ?

- A) Tutor LMS > Settings > General
- B) Tutor LMS > Settings > Email > Enable Email Notification ✅
- C) WordPress > Settings > Email
- D) Tutor LMS > Tools > Notifications

**Explication** : Le toggle "Enable Email Notification" se trouve dans Settings > Email. Sans cette activation, aucun email n'est envoye par TutorLMS.

---

**Question 2**

Quel placeholder insere automatiquement le nom de l'eleve dans un email ?

- A) {user_name}
- B) {student_name} ✅
- C) {eleve_nom}
- D) {name}

**Explication** : {student_name} est le placeholder standard TutorLMS pour le nom de l'eleve. Les autres syntaxes ne sont pas reconnues.

---

**Question 3**

Les annonces de cours sont visibles par :

- A) Tous les visiteurs du site
- B) Tous les utilisateurs connectes
- C) Uniquement les eleves inscrits au cours concerne ✅
- D) Uniquement les administrateurs

**Explication** : Les annonces sont specifiques a chaque cours et visibles uniquement par les eleves inscrits a ce cours.

---

**Question 4**

Que se passe-t-il quand un instructeur rejette un devoir avec feedback ?

- A) Le devoir est supprime definitivement
- B) L'eleve recoit le feedback et peut resoumettre ✅
- C) L'eleve doit contacter l'admin pour debloquer
- D) Le devoir est automatiquement note a zero

**Explication** : Un devoir rejete permet a l'eleve de voir le feedback de l'instructeur et de resoumettre une version amelioree.

---

**Question 5**

Quelle condition est obligatoire pour les notifications push navigateur ?

- A) Un plugin supplementaire
- B) Le site doit etre en HTTPS ✅
- C) Un compte Google Analytics
- D) WordPress Multisite

**Explication** : Les notifications push navigateur necessitent un site en HTTPS. C'est une exigence technique des navigateurs, pas de TutorLMS.

---

**Question 6**

Un eleve veut poser une question visible uniquement par l'instructeur. Quelle option utilise-t-il ?

- A) Envoyer un email a l'instructeur
- B) Cocher l'option "question privee" dans le Q&A ✅
- C) Poster dans les annonces du cours
- D) Les questions sont toujours publiques

**Explication** : Le Q&A de TutorLMS offre une option pour rendre une question privee — visible uniquement par l'instructeur.

---

**Question 7**

Si tu ecris {studen_name} (avec une faute) dans un template email, que voit l'eleve ?

- A) Son vrai nom quand meme
- B) Un champ vide
- C) Le texte brut {studen_name} ✅
- D) Un message d'erreur

**Explication** : Un placeholder mal orthographie n'est pas interprete par TutorLMS. Il s'affiche tel quel dans l'email envoye.

---

**Question 8**

Quelle est la recommandation schoolsWP pour l'adresse d'expediteur des emails TutorLMS ?

- A) Une adresse Gmail personnelle
- B) admin@wordpress.org
- C) Une adresse sur ton propre domaine (ex: noreply@tondomaine.com) ✅
- D) Ne pas mettre d'adresse — TutorLMS gere automatiquement

**Explication** : Utiliser une adresse sur ton propre domaine fait professionnel et ameliore la delivrabilite — ca evite les filtres anti-spam.

---

**Recapitulatif Module 9** :
- Lecon 9.1 : Email template builder — personnalisation des emails automatiques
- Lecon 9.2 : Notifications on-site — cloche + push navigateur
- Lecon 9.3 : Annonces — communication ciblee par cours
- Lecon 9.4 : Q&A — forum contextuel par lecon
- Lecon 9.5 : Feedback instructeur — retour prive sur devoirs et quiz
- Lecon 9.6 : Placeholders email — variables dynamiques pour personnalisation
