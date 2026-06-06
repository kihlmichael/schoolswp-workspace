# Scripts vidéo - Module 9 : Communication & Emails

**Formation** : Maîtriser TutorLMS
**Module** : M9 - Communication & Emails (Premium)
**Leçons** : 6 vidéos + 1 quiz
**Durée totale** : ~35 min
**Date** : 2026-03-23

---

### Leçon 9.1 : Email template builder

**Durée** : 6 min
**Type** : Vidéo HeyGen
**Écran** : Face caméra pour intro/conclusion, screencast du panneau Email
**Source** : Vidéo #27 + doc email-notifications

---

**[INTRO - face caméra]**

TutorLMS envoie des emails à chaque étape clé : inscription à un cours, complétion, résultat de quiz, nouveau commentaire Q&A. Le problème, c'est que les emails par défaut sont génériques et impersonnels. Dans cette leçon, on va les personnaliser avec le template builder intégré.

**[ÉCRAN - screencast WordPress admin]**

[Navigation vers Tutor LMS > Settings > Email]

Va dans Tutor LMS, Settings, puis Email. Tu arrives sur le panneau de configuration des emails. Première chose : vérifie que le toggle "Enable Email Notification" est activé. Sans ça, TutorLMS n'envoie rien.

**[ÉCRAN - screencast panneau Email]**

[Vue des options globales : Notification From, Sender Address, Footer Text]

En haut, tu as trois réglages globaux :

1. Notification From - le nom d'expéditeur. Mets le nom de ta plateforme, pas "WordPress" ou "admin".
2. Sender Email Address - l'adresse d'envoi. Utilise une adresse sur ton domaine, pas une adresse Gmail.
3. Footer Text - le pied de page commun à tous les emails.

La recommandation schoolsWP : utilise un expéditeur du type "Formation schoolsWP" avec une adresse noreply@tondomaine.com. Ça fait professionnel et ça évite les filtres anti-spam.

**[ÉCRAN - screencast liste des templates]**

[Défilement de la liste des événements email]

En dessous, tu as la liste de tous les événements qui déclenchent un email. Chaque événement a un toggle pour l'activer ou le désactiver. Les principaux :

Pour les étudiants :
- Enrollment - quand un élève s'inscrit à un cours
- Course Completed - quand il termine le cours
- Quiz Completed - après chaque quiz
- Assignment Submitted - confirmation de soumission d'un devoir

Pour les instructeurs :
- New Student Enrolled - notification quand un nouvel élève rejoint le cours
- New Q&A Message - quand un élève pose une question
- Assignment Submitted - quand un devoir est soumis

Pour les administrateurs :
- New Instructor Registration - quand un instructeur demande son compte
- New Course Published - quand un cours est soumis pour relecture

**[ÉCRAN - screencast édition d'un template]**

[Clique sur un événement, par exemple "Enrollment"]

Clique sur un événement pour le personnaliser. Tu arrives dans l'éditeur de template. Tu as :

- Subject - l'objet de l'email
- Heading - le titre principal dans le corps de l'email
- Message - le contenu avec un éditeur visuel

L'éditeur supporte le HTML basique et surtout les placeholders - des variables dynamiques qu'on remplacera automatiquement. Par exemple, {student_name} sera remplacé par le prénom de l'élève, {course_name} par le nom du cours. On verra la liste complète des placeholders dans la leçon 9.6.

**[ÉCRAN - screencast preview email]**

[Montre le bouton Preview et le rendu]

Avant d'enregistrer, utilise le bouton Preview pour voir le rendu final. Ça t'évite les mauvaises surprises - un placeholder mal fermé, un titre trop long, un lien cassé.

**[TRANSITION - face caméra]**

Personnalise au minimum les emails d'inscription et de complétion de cours. Ce sont les deux que tes élèves voient le plus. Mets ton nom de marque, un message d'accueil clair, et un lien vers le cours. Dans la prochaine leçon, on passe aux notifications on-site - celles qui apparaissent directement dans l'interface.

---

**Points clés** :
- Activation : Settings > Email > Enable Email Notification
- 3 réglages globaux : Notification From, Sender Email, Footer Text
- Chaque événement a un toggle + template personnalisable (subject, heading, message)
- Placeholders dynamiques pour personnaliser ({student_name}, {course_name}, etc.)
- Toujours vérifier avec Preview avant d'enregistrer
- Priorité : personnaliser Enrollment + Course Completed en premier

**Mots clés SEO** : TutorLMS email template, personnaliser emails TutorLMS, notifications email LMS WordPress, TutorLMS email builder

---

### Leçon 9.2 : Notifications on-site & push

**Durée** : 5 min
**Type** : Vidéo HeyGen
**Écran** : Face caméra pour intro/conclusion, screencast panneau Notifications
**Source** : Vidéo #11 + doc notifications

---

**[INTRO - face caméra]**

Les emails c'est bien, mais tes élèves ne les lisent pas toujours. Les notifications on-site, elles, apparaissent directement dans l'interface TutorLMS - comme sur Facebook ou YouTube. L'élève voit une cloche avec un badge, il clique, il voit ce qui s'est passé. C'est immédiat et ça ne dépend pas de la boîte mail.

**[ÉCRAN - screencast WordPress admin]**

[Navigation vers Tutor LMS > Settings > Notifications]

Va dans Tutor LMS, Settings, puis cherche la section Notifications. Tu as deux blocs : les notifications on-site (dans le navigateur) et les notifications push (optionnelles).

**[ÉCRAN - screencast panneau Notifications]**

[Vue du toggle principal et de la liste des événements]

Active le toggle principal "Enable On-Site Notification". En dessous, tu retrouves une liste d'événements similaire aux emails - mais cette fois, la notification s'affiche dans l'interface du site.

Les événements les plus utiles :

Pour les étudiants :
- Course Enrollment - confirmation d'inscription
- Quiz Graded - résultat de quiz disponible
- Announcement Posted - l'instructeur a publié une annonce (on verra ça en leçon 9.3)
- Q&A Reply - réponse à sa question

Pour les instructeurs :
- New Q&A Question - un élève a posé une question
- Assignment to Review - un devoir est en attente de correction
- New Enrollment - un élève rejoint le cours

**[ÉCRAN - screencast front-end cloche notification]**

[Montre la cloche de notification dans le header du site, côté élève]

Côté front-end, l'élève voit une icône cloche dans le header. Le badge affiche le nombre de notifications non lues. Un clic ouvre le panneau avec la liste. Chaque notification contient un lien direct vers le contenu concerné - le cours, le quiz, la discussion Q&A.

**[ÉCRAN - screencast paramètres push]**

[Montre les options push si disponibles]

TutorLMS propose aussi les notifications push via le navigateur. C'est la notification qui apparaît même quand l'élève n'est pas sur ton site - comme une notification de téléphone, mais sur desktop. Pour l'activer, il faut que ton site soit en HTTPS (obligatoire) et que l'élève accepte les notifications dans son navigateur.

Mon avis : les notifications on-site sont indispensables, les push sont un bonus. Active les on-site en priorité.

**[TRANSITION - face caméra]**

Les notifications on-site et les emails sont complémentaires. L'email confirme, la notification on-site rappelle. Active les deux pour les événements importants - inscription, complétion, Q&A. Dans la prochaine leçon, on découvre les annonces - un outil pour communiquer directement avec les élèves d'un cours spécifique.

---

**Points clés** :
- Activation : Settings > Notifications > Enable On-Site Notification
- Notifications apparaissent dans la cloche du header front-end
- Événements principaux : enrollment, quiz graded, announcement, Q&A reply
- Push notifications disponibles (HTTPS requis + autorisation navigateur)
- Recommandation : activer on-site en priorité, push en complément
- Complémentaire aux emails - pas un remplacement

**Mots clés SEO** : TutorLMS notifications, notifications on-site LMS, push notifications TutorLMS, alertes élèves WordPress

---

### Leçon 9.3 : Annonces

**Durée** : 5 min
**Type** : Vidéo HeyGen
**Écran** : Face caméra pour intro/conclusion, screencast Course Builder + front-end
**Source** : doc menus/announcement

---

**[INTRO - face caméra]**

Tu dois prévenir tes élèves d'une mise à jour de contenu, d'un live prévu la semaine prochaine, ou d'un changement de planning ? Les annonces TutorLMS sont faites pour ça. C'est un système de communication ciblé - tu publies une annonce dans un cours, et seuls les élèves inscrits à ce cours la voient.

**[ÉCRAN - screencast WordPress admin]**

[Navigation vers Tutor LMS > un cours > onglet Announcements]

Ouvre n'importe quel cours dans TutorLMS. Dans le menu du cours, tu trouves l'onglet Announcements. C'est ici que tu gères toutes les annonces liées à ce cours.

**[ÉCRAN - screencast création d'une annonce]**

[Clique sur "Add New Announcement"]

Clique sur "Add New Announcement". Tu as deux champs :

1. Titre - l'objet de l'annonce. Sois concis : "Nouveau module disponible", "Live Q&A vendredi 14h", "Mise à jour de la leçon 5".
2. Contenu - le corps du message. L'éditeur supporte le texte riche, les liens, les images. Tu peux détailler autant que nécessaire.

Publie. L'annonce est immédiatement visible pour tous les élèves inscrits au cours.

**[ÉCRAN - screencast front-end annonce]**

[Montre l'onglet Announcements sur la page du cours côté élève]

Côté élève, les annonces apparaissent dans l'onglet "Announcements" sur la page du cours. L'annonce la plus récente est en haut. L'élève voit le titre, la date, et peut cliquer pour lire le contenu complet.

Si les notifications on-site sont activées (leçon précédente), l'élève reçoit aussi une notification dans sa cloche. Et si l'événement email correspondant est activé, il reçoit un email. Trois canaux pour une seule action - c'est la force du système.

**[ÉCRAN - screencast liste des annonces]**

[Montre la liste des annonces existantes avec options modifier/supprimer]

Tu retrouves toutes tes annonces dans la liste. Tu peux les modifier ou les supprimer à tout moment. Les annonces sont spécifiques à chaque cours - une annonce publiée dans le cours A n'apparaît pas dans le cours B.

**[ÉCRAN - screencast cas d'usage]**

[Montre un exemple concret d'annonce bien rédigée]

Quelques bonnes pratiques :

- Un titre clair et actionnable - pas "Information" mais "Nouveau quiz disponible - teste tes connaissances"
- Un contenu court - l'annonce n'est pas un article de blog, c'est un message ciblé
- Un lien si nécessaire - vers la leçon concernée, un formulaire, un replay
- Une fréquence raisonnable - une annonce par semaine maximum, sinon tes élèves décrochent

**[TRANSITION - face caméra]**

Les annonces sont parfaites pour maintenir l'engagement dans un cours. Utilise-les pour les mises à jour importantes, pas pour du remplissage. Prochaine leçon : le système de Q&A, qui permet à tes élèves de poser des questions directement dans les leçons.

---

**Points clés** :
- Accès : page du cours > onglet Announcements > Add New Announcement
- Deux champs : titre + contenu (texte riche)
- Visibles uniquement par les élèves inscrits au cours
- Déclenchent notification on-site + email si actives
- Spécifiques à chaque cours - pas de diffusion globale
- Bonne pratique : une annonce par semaine max, titre actionnable, contenu court

**Mots clés SEO** : TutorLMS annonces, announcements TutorLMS, communiquer élèves LMS WordPress, annonces cours en ligne

---

### Leçon 9.4 : Q&A étudiants/instructeurs

**Durée** : 6 min
**Type** : Vidéo HeyGen
**Écran** : Face caméra pour intro/conclusion, screencast Q&A front-end + admin
**Source** : doc tutorials/qa

---

**[INTRO - face caméra]**

Quand un élève bloque sur une leçon, il doit pouvoir poser sa question sans quitter la page. C'est exactement ce que fait le Q&A intégré de TutorLMS. Chaque leçon a son propre fil de discussion. L'élève pose sa question, l'instructeur répond, et toute la classe en bénéficie. C'est comme un mini-forum contextuel.

**[ÉCRAN - screencast WordPress admin]**

[Navigation vers Tutor LMS > Settings > recherche Q&A]

D'abord, vérifie que le Q&A est activé. Va dans Tutor LMS, Settings, et cherche l'option "Q&A" ou "Enable Q&A for course". Active le toggle. Sans ça, les élèves ne voient pas l'onglet Q&A dans les leçons.

**[ÉCRAN - screencast front-end leçon]**

[Montre l'onglet Q&A sous le contenu d'une leçon]

Côté élève, quand le Q&A est activé, un onglet "Q&A" apparaît sous le contenu de chaque leçon. L'élève clique dessus et voit les questions existantes. Il peut poser une nouvelle question ou répondre à une question existante.

**[ÉCRAN - screencast création d'une question]**

[Montre le formulaire de soumission Q&A]

Pour poser une question, l'élève clique sur "Ask a new question". Il a deux champs :
- Le titre - la question en une phrase
- Le contenu - les détails, le contexte, ce qu'il a déjà essayé

Il peut aussi cocher une option pour rendre la question privée - visible uniquement par l'instructeur. Utile si la question est personnelle ou spécifique.

**[ÉCRAN - screencast réponse instructeur]**

[Montre la vue instructeur du Q&A dans le dashboard]

Côté instructeur, tu retrouves toutes les questions dans ton dashboard, section Q&A. Tu vois :
- Les questions en attente de réponse (marquées comme non lues)
- Le cours et la leçon concernés
- La date et l'auteur

Clique sur une question pour répondre. Ta réponse est publiée immédiatement. L'élève reçoit une notification (on-site + email si actives).

**[ÉCRAN - screencast modération Q&A]**

[Montre les options de modération]

En tant qu'instructeur ou admin, tu as des options de modération :
- Marquer une question comme résolue - ça la signale visuellement dans la liste
- Supprimer une question inappropriée
- Répondre publiquement ou en privé

Le Q&A fonctionne aussi pour les quiz et les devoirs - pas uniquement les leçons vidéo ou texte.

**[ÉCRAN - screencast vue globale Q&A admin]**

[Montre la page Q&A dans le menu admin Tutor LMS]

En tant qu'admin, tu as aussi une vue globale de toutes les questions Q&A de la plateforme. Ça te permet de surveiller les questions sans réponse, identifier les leçons qui posent problème, et intervenir si un instructeur ne répond pas.

**[TRANSITION - face caméra]**

Le Q&A est un outil d'engagement puissant. Un élève qui pose une question est un élève impliqué. Un instructeur qui répond rapidement est un instructeur qui fidélise. Surveille les questions sans réponse - c'est un indicateur de santé de ta formation. Prochaine leçon : le feedback instructeur, un autre canal de communication direct.

---

**Points clés** :
- Activation : Settings > Q&A > Enable
- Onglet Q&A sous chaque leçon, quiz et devoir
- Questions publiques ou privées (choix de l'élève)
- Instructeur répond depuis son dashboard > Q&A
- Options : marquer comme résolu, supprimer, répondre en privé
- Vue admin globale pour surveiller les questions sans réponse
- Déclenchent notifications on-site + email

**Mots clés SEO** : TutorLMS Q&A, questions réponses LMS WordPress, forum discussion TutorLMS, interaction élèves instructeurs TutorLMS

---

### Leçon 9.5 : Feedback instructeur

**Durée** : 5 min
**Type** : Vidéo HeyGen
**Écran** : Face caméra pour intro/conclusion, screencast feedback dans le Course Builder
**Source** : doc tutorials/give-feedback

---

**[INTRO - face caméra]**

Le Q&A est public - tout le monde voit les questions et les réponses. Mais parfois, tu as besoin d'un retour individuel et privé. C'est le rôle du feedback instructeur dans TutorLMS. Tu corriges un devoir, tu évalues un quiz à réponse ouverte, tu veux guider un élève personnellement - le feedback est ton outil.

**[ÉCRAN - screencast WordPress admin]**

[Navigation vers le dashboard instructeur > Assignments]

Le feedback s'utilise principalement dans deux contextes : les devoirs (assignments) et les quiz à correction manuelle. Commençons par les devoirs.

Va dans ton dashboard instructeur, section Assignments. Tu vois la liste des devoirs soumis par tes élèves, avec le statut : en attente, validé, ou rejeté.

**[ÉCRAN - screencast correction d'un devoir]**

[Clique sur un devoir soumis pour le corriger]

Clique sur un devoir pour le corriger. Tu vois :
- Le fichier ou le texte soumis par l'élève
- Les consignes du devoir pour référence
- La date de soumission

En bas, tu as la zone de feedback. C'est un éditeur texte où tu écris ton retour. Sois précis : ce qui est bien, ce qui doit être amélioré, et comment l'améliorer. Un "bien" tout seul ne sert à rien. Un "ta structure est claire, mais la partie 3 manque d'exemples concrets - ajoute un cas pratique" est utile.

**[ÉCRAN - screencast notation + feedback]**

[Montre le champ de note et le bouton de validation]

Tu attribues une note (sur le barème que tu as défini dans le devoir) et tu choisis :
- Approve - le devoir est validé
- Reject - le devoir est refusé, l'élève doit recommencer

Dans les deux cas, ton feedback est envoyé à l'élève. S'il est refusé, l'élève peut resoumettre - il verra ton feedback pour s'améliorer.

**[ÉCRAN - screencast feedback sur quiz]**

[Montre un quiz à correction manuelle dans le dashboard]

Pour les quiz, le feedback fonctionne avec les questions à réponse ouverte - celles qui ne peuvent pas être corrigées automatiquement. Tu retrouves les quiz en attente de correction dans ton dashboard, section Quiz Attempts.

Clique sur une tentative. Tu vois les réponses de l'élève question par question. Pour chaque réponse ouverte, tu attribues les points et tu peux ajouter un commentaire.

**[ÉCRAN - screencast vue élève du feedback]**

[Montre ce que l'élève voit après correction]

Côté élève, le feedback apparaît directement sur la page du devoir ou du quiz. L'élève reçoit une notification quand le feedback est disponible. Il voit ta note, ton commentaire, et si c'est un devoir refusé, le bouton pour resoumettre.

**[TRANSITION - face caméra]**

Le feedback est ce qui fait la différence entre une plateforme de cours et une vraie formation. Un retour précis et constructif transforme un cours passif en expérience d'apprentissage. Prends le temps de rédiger des feedbacks utiles - tes élèves s'en souviendront. Dernière leçon du module : les placeholders email, pour automatiser la personnalisation de tes communications.

---

**Points clés** :
- Feedback disponible sur les devoirs (assignments) et les quiz à correction manuelle
- Devoirs : Approve ou Reject avec commentaire détaillé
- Quiz : points + commentaire par question ouverte
- L'élève voit le feedback sur la page du devoir/quiz + notification
- Devoir refusé = l'élève peut resoumettre
- Bonne pratique : feedback précis et actionnable, jamais un simple "bien" ou "insuffisant"

**Mots clés SEO** : TutorLMS feedback instructeur, corriger devoirs TutorLMS, notation quiz TutorLMS, retour personnalisé LMS WordPress

---

### Leçon 9.6 : Placeholders email

**Durée** : 6 min
**Type** : Vidéo HeyGen
**Écran** : Face caméra pour intro/conclusion, screencast Email templates + placeholders
**Source** : doc tutorials/email-placeholders

---

**[INTRO - face caméra]**

En leçon 9.1, on a vu comment personnaliser les templates email. Mais pour aller plus loin, tu dois maîtriser les placeholders - ces variables dynamiques qui insèrent automatiquement le nom de l'élève, le titre du cours, la note d'un quiz. C'est ce qui transforme un email générique en message personnalisé, sans effort manuel.

**[ÉCRAN - screencast WordPress admin]**

[Navigation vers Tutor LMS > Settings > Email > un template]

Retourne dans Settings, Email, et ouvre n'importe quel template. Dans l'éditeur, tu vois un bouton ou un lien "Available Placeholders" - clique dessus pour afficher la liste des variables utilisables dans ce template.

**[ÉCRAN - screencast liste des placeholders]**

[Montre la liste des placeholders disponibles pour un template d'inscription]

Chaque template a ses propres placeholders. Voici les plus courants :

Placeholders globaux (disponibles partout) :
- {site_name} - le nom de ton site WordPress
- {site_url} - l'URL de ton site
- {logo} - le logo de ton site (si défini)

Placeholders élève :
- {student_name} - prénom et nom de l'élève
- {student_email} - adresse email
- {student_username} - nom d'utilisateur

Placeholders cours :
- {course_name} - titre du cours
- {course_url} - lien direct vers le cours
- {course_duration} - durée estimée du cours

Placeholders quiz :
- {quiz_name} - titre du quiz
- {quiz_score} - note obtenue
- {quiz_passing_grade} - note minimale pour réussir

**[ÉCRAN - screencast exemple concret]**

[Montre un template d'email de complétion avec placeholders]

Prenons un exemple concret. Pour l'email de complétion de cours, tu pourrais écrire :

Sujet : Bravo {student_name} - tu as terminé {course_name} !

Corps :
"Félicitations {student_name},

Tu as terminé le cours {course_name}. C'est une belle étape.

Pour continuer ta progression, voici tes prochaines options :
- Reviens sur le cours : {course_url}
- Découvre nos autres formations : {site_url}/cours

À bientôt,
L'équipe {site_name}"

C'est personnalisé, professionnel, et ça prend 30 secondes à configurer.

**[ÉCRAN - screencast placeholders avancés]**

[Montre des placeholders spécifiques aux devoirs et instructeurs]

Pour les templates liés aux devoirs :
- {assignment_name} - titre du devoir
- {assignment_comment} - le feedback que tu as rédigé (leçon 9.5)
- {assignment_score} - la note attribuée

Pour les templates instructeurs :
- {instructor_name} - nom de l'instructeur
- {instructor_email} - email de l'instructeur

**[ÉCRAN - screencast erreurs courantes]**

[Montre un placeholder mal écrit et le résultat]

Attention aux erreurs courantes :
- Un placeholder mal orthographié - {studen_name} au lieu de {student_name} - s'affiche tel quel dans l'email. L'élève voit la variable brute.
- Un placeholder utilisé dans le mauvais template - {quiz_score} dans un email d'inscription ne donnera rien, parce qu'il n'y a pas de quiz à ce stade.
- Les accolades manquantes - student_name sans les {} n'est pas interprété.

Toujours utiliser le bouton Preview (leçon 9.1) pour vérifier le rendu avant d'enregistrer.

**[TRANSITION - face caméra]**

Les placeholders sont le lien entre tes templates email et les données de ta plateforme. Maîtrise-les, et chaque email que TutorLMS envoie ressemblera à un message rédigé à la main. C'est la fin du Module 9 - tu sais maintenant gérer les emails, les notifications, les annonces, le Q&A, le feedback et les placeholders. Prochaine étape : le quiz du module pour valider tes acquis.

---

**Points clés** :
- Chaque template a ses propres placeholders - consulter "Available Placeholders"
- Placeholders globaux : {site_name}, {site_url}, {logo}
- Placeholders élève : {student_name}, {student_email}
- Placeholders cours : {course_name}, {course_url}
- Placeholders quiz : {quiz_name}, {quiz_score}, {quiz_passing_grade}
- Erreurs courantes : faute d'orthographe, mauvais template, accolades manquantes
- Toujours prévisualiser avec Preview

**Mots clés SEO** : TutorLMS placeholders email, variables email LMS WordPress, personnaliser notifications TutorLMS, email dynamique TutorLMS

---

### Leçon 9.7 : Quiz Module 9

**Type** : Quiz TutorLMS
**Questions** : 8 QCM
**Note de passage** : 70% (6/8)
**Tentatives** : illimitées

---

**Question 1**

Où active-t-on les notifications email dans TutorLMS ?

- A) Tutor LMS > Settings > General
- B) Tutor LMS > Settings > Email > Enable Email Notification ✅
- C) WordPress > Settings > Email
- D) Tutor LMS > Tools > Notifications

**Explication** : Le toggle "Enable Email Notification" se trouve dans Settings > Email. Sans cette activation, aucun email n'est envoyé par TutorLMS.

---

**Question 2**

Quel placeholder insère automatiquement le nom de l'élève dans un email ?

- A) {user_name}
- B) {student_name} ✅
- C) {eleve_nom}
- D) {name}

**Explication** : {student_name} est le placeholder standard TutorLMS pour le nom de l'élève. Les autres syntaxes ne sont pas reconnues.

---

**Question 3**

Les annonces de cours sont visibles par :

- A) Tous les visiteurs du site
- B) Tous les utilisateurs connectés
- C) Uniquement les élèves inscrits au cours concerné ✅
- D) Uniquement les administrateurs

**Explication** : Les annonces sont spécifiques à chaque cours et visibles uniquement par les élèves inscrits à ce cours.

---

**Question 4**

Que se passe-t-il quand un instructeur rejette un devoir avec feedback ?

- A) Le devoir est supprimé définitivement
- B) L'élève reçoit le feedback et peut resoumettre ✅
- C) L'élève doit contacter l'admin pour débloquer
- D) Le devoir est automatiquement noté à zéro

**Explication** : Un devoir rejeté permet à l'élève de voir le feedback de l'instructeur et de resoumettre une version améliorée.

---

**Question 5**

Quelle condition est obligatoire pour les notifications push navigateur ?

- A) Un plugin supplémentaire
- B) Le site doit être en HTTPS ✅
- C) Un compte Google Analytics
- D) WordPress Multisite

**Explication** : Les notifications push navigateur nécessitent un site en HTTPS. C'est une exigence technique des navigateurs, pas de TutorLMS.

---

**Question 6**

Un élève veut poser une question visible uniquement par l'instructeur. Quelle option utilise-t-il ?

- A) Envoyer un email à l'instructeur
- B) Cocher l'option "question privée" dans le Q&A ✅
- C) Poster dans les annonces du cours
- D) Les questions sont toujours publiques

**Explication** : Le Q&A de TutorLMS offre une option pour rendre une question privée - visible uniquement par l'instructeur.

---

**Question 7**

Si tu écris {studen_name} (avec une faute) dans un template email, que voit l'élève ?

- A) Son vrai nom quand même
- B) Un champ vide
- C) Le texte brut {studen_name} ✅
- D) Un message d'erreur

**Explication** : Un placeholder mal orthographié n'est pas interprété par TutorLMS. Il s'affiche tel quel dans l'email envoyé.

---

**Question 8**

Quelle est la recommandation schoolsWP pour l'adresse d'expéditeur des emails TutorLMS ?

- A) Une adresse Gmail personnelle
- B) admin@wordpress.org
- C) Une adresse sur ton propre domaine (ex: noreply@tondomaine.com) ✅
- D) Ne pas mettre d'adresse - TutorLMS gère automatiquement

**Explication** : Utiliser une adresse sur ton propre domaine fait professionnel et améliore la délivrabilité - ça évite les filtres anti-spam.

---

**Récapitulatif Module 9** :
- Leçon 9.1 : Email template builder - personnalisation des emails automatiques
- Leçon 9.2 : Notifications on-site - cloche + push navigateur
- Leçon 9.3 : Annonces - communication ciblée par cours
- Leçon 9.4 : Q&A - forum contextuel par leçon
- Leçon 9.5 : Feedback instructeur - retour privé sur devoirs et quiz
- Leçon 9.6 : Placeholders email - variables dynamiques pour personnalisation
