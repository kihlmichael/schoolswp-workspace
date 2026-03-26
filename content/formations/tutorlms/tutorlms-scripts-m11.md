# Scripts video — Module 11 : Inscription & Gestion utilisateurs

**Formation** : Maitriser TutorLMS
**Module** : M11 — Inscription & Gestion utilisateurs (Premium)
**Lecons** : 10 videos + 1 quiz
**Duree totale** : ~55 min
**Date** : 2026-03-23

---

### Lecon 11.1 — Inscription etudiant

**Duree** : 5 min
**Type** : Video HeyGen
**Ecran** : Face camera pour intro/conclusion, screencast du parcours d'inscription
**Source** : doc tutorials/student-signup

---

**[INTRO — face camera]**

Quand un visiteur arrive sur ton site de formation, la premiere chose qu'il doit pouvoir faire, c'est s'inscrire. TutorLMS propose un parcours d'inscription etudiant integre, avec un formulaire dedie et des options de personnalisation. Dans cette lecon, on configure ce parcours de A a Z.

**[ECRAN — screencast WordPress admin]**

[Navigation vers Tutor LMS > Settings > General]

Pour commencer, va dans Tutor LMS, puis Settings, puis l'onglet General. Cherche l'option "Student Registration". Active-la si ce n'est pas deja fait. C'est cette option qui autorise les visiteurs a creer un compte etudiant depuis le front-end.

**[ECRAN — screencast reglages inscription]**

[Montre les options liees a l'inscription]

Tu as plusieurs options a configurer :

1. Registration Page — la page qui contient le formulaire d'inscription. TutorLMS en cree une automatiquement, mais tu peux en choisir une autre.
2. Email Verification — si tu actives cette option, l'etudiant doit confirmer son adresse email avant d'acceder aux cours. Recommande pour eviter les faux comptes.
3. Manual Instructor Approval — on verra ca dans la lecon suivante, c'est pour les instructeurs.

**[ECRAN — screencast front-end]**

[Montre la page d'inscription vue par un visiteur]

Cote visiteur, le formulaire d'inscription affiche les champs standards : nom, prenom, email, mot de passe. L'etudiant remplit le formulaire, recoit un email de confirmation si tu l'as active, puis accede a son tableau de bord.

**[ECRAN — screencast WordPress admin]**

[Navigation vers Users dans le back-office]

Dans le back-office WordPress, chaque etudiant inscrit apparait dans la liste des utilisateurs avec le role "Subscriber" par defaut. TutorLMS lui attribue automatiquement les capacites necessaires pour suivre des cours.

**[ECRAN — screencast TutorLMS Dashboard etudiant]**

[Montre le tableau de bord etudiant front-end]

Une fois connecte, l'etudiant accede a son dashboard TutorLMS : ses cours en cours, ses certificats, son profil. C'est son espace personnel.

**[TRANSITION — face camera]**

La recommandation schoolsWP : active toujours la verification email. Ca filtre les inscriptions fantomes et ameliore la qualite de ta liste. Dans la prochaine lecon, on voit le parcours d'inscription pour les instructeurs — c'est un peu different.

---

**Points cles** :
- Activation dans Settings > General > Student Registration
- Email Verification recommandee pour filtrer les faux comptes
- Role WordPress : Subscriber avec capacites TutorLMS
- Dashboard etudiant front-end accessible des la connexion

**Mots cles SEO** : inscription etudiant TutorLMS, formulaire inscription LMS WordPress, student signup TutorLMS, creer compte eleve TutorLMS

---

### Lecon 11.2 — Inscription instructeur

**Duree** : 5 min
**Type** : Video HeyGen
**Ecran** : Face camera pour intro/conclusion, screencast du parcours instructeur
**Source** : doc tutorials/instructor-signup

---

**[INTRO — face camera]**

Si tu prevois d'avoir plusieurs formateurs sur ton site, tu dois configurer l'inscription instructeur. TutorLMS permet a n'importe qui de candidater comme instructeur, avec un systeme de validation manuelle ou automatique. Voyons comment ca fonctionne.

**[ECRAN — screencast WordPress admin]**

[Navigation vers Tutor LMS > Settings > General]

Va dans Tutor LMS, Settings, onglet General. Cherche la section "Instructor Registration". Active l'option "Enable Instructor Registration". Ca ajoute un formulaire d'inscription specifique pour les instructeurs sur le front-end.

**[ECRAN — screencast reglages instructeur]**

[Montre les options d'approbation]

Juste en dessous, tu trouves l'option "Manual Approval for Instructor". Deux choix :

1. Active — chaque candidature instructeur passe par toi. Tu recois une notification, tu examines le profil, tu acceptes ou tu refuses.
2. Desactive — l'inscription est automatique. Toute personne qui s'inscrit comme instructeur obtient immediatement les droits de creation de cours.

Pour un site professionnel, je recommande l'approbation manuelle. Ca te permet de controler qui publie du contenu sur ta plateforme.

**[ECRAN — screencast front-end]**

[Montre le formulaire d'inscription instructeur]

Le formulaire instructeur est similaire a celui de l'etudiant, avec un champ supplementaire : la bio. L'instructeur decrit son expertise et son experience. C'est ce que tu liras pour decider si tu approuves sa candidature.

**[ECRAN — screencast WordPress admin]**

[Navigation vers Tutor LMS > Instructors > liste en attente]

Quand un instructeur s'inscrit avec l'approbation manuelle, il apparait dans la section Instructors avec le statut "Pending". Tu cliques sur son profil, tu verifies sa bio, et tu valides ou tu refuses.

**[ECRAN — screencast notification email]**

[Montre l'email de notification]

TutorLMS envoie un email a l'instructeur pour lui confirmer l'approbation. A partir de la, il peut creer des cours depuis le front-end.

**[TRANSITION — face camera]**

Conseil schoolsWP : meme si tu es le seul formateur pour l'instant, active l'inscription instructeur avec approbation manuelle. Ca te laisse la porte ouverte pour accueillir des contributeurs plus tard, sans risque. Prochaine lecon : on simplifie l'inscription avec le Social Login Google.

---

**Points cles** :
- Activation dans Settings > General > Instructor Registration
- Approbation manuelle recommandee pour controler la qualite
- Les instructeurs en attente apparaissent dans Tutor LMS > Instructors
- Email de confirmation automatique a l'approbation

**Mots cles SEO** : inscription instructeur TutorLMS, ajouter formateur LMS WordPress, instructor signup TutorLMS, multi-instructeur TutorLMS

---

### Lecon 11.3 — Social Login (Google)

**Duree** : 6 min
**Type** : Video HeyGen
**Ecran** : Face camera pour intro/conclusion, screencast Google Cloud Console + TutorLMS
**Source** : Video #19, #28 + doc social-login

---

**[INTRO — face camera]**

Plus un formulaire d'inscription est simple, plus tu as d'inscrits. Le Social Login permet a tes visiteurs de s'inscrire avec leur compte Google — pas de mot de passe a creer, pas de formulaire a remplir. Dans cette lecon, on configure la connexion Google dans TutorLMS.

**[ECRAN — screencast WordPress admin]**

[Navigation vers Tutor LMS > Settings > Design & Content > Login]

Pour activer le Social Login, va dans Tutor LMS, Settings, puis Design & Content, onglet Login. Tu y trouves la section Social Login avec les options Google et Facebook. Active le toggle "Google Login".

TutorLMS te demande deux informations : un Client ID et un Client Secret. On va les creer dans Google Cloud Console.

**[ECRAN — screencast Google Cloud Console]**

[Navigation vers console.cloud.google.com > APIs & Services > Credentials]

Connecte-toi a Google Cloud Console. Si tu n'as pas de projet, cree-en un — donne-lui le nom de ton site. Ensuite, va dans APIs & Services, puis Credentials.

Clique sur "Create Credentials", puis "OAuth client ID".

**[ECRAN — screencast configuration OAuth]**

[Montre les champs de configuration]

Etape par etape :

1. Application type — selectionne "Web application"
2. Name — donne un nom descriptif, par exemple "TutorLMS Social Login"
3. Authorized JavaScript origins — entre l'URL de ton site, par exemple https://ton-site.com
4. Authorized redirect URIs — entre l'URL de callback que TutorLMS t'affiche dans ses reglages

Valide. Google genere un Client ID et un Client Secret.

**[ECRAN — screencast ecran de consentement OAuth]**

[Navigation vers OAuth consent screen]

Avant que ca fonctionne, tu dois aussi configurer l'ecran de consentement OAuth. Va dans OAuth consent screen. Choisis "External" si ton site est public. Remplis le nom de l'application, l'email de support et les domaines autorises.

Pas besoin de scopes supplementaires — les scopes par defaut (email, profile) suffisent.

**[ECRAN — screencast retour TutorLMS]**

[Colle le Client ID et Client Secret dans les champs]

Retourne dans TutorLMS. Colle le Client ID et le Client Secret dans les champs correspondants. Enregistre.

**[ECRAN — screencast front-end]**

[Montre le bouton "Sign in with Google" sur la page de connexion]

Sur ta page de connexion, un bouton "Sign in with Google" apparait. Le visiteur clique, autorise l'acces, et son compte est cree automatiquement avec les bonnes informations.

**[TRANSITION — face camera]**

Le Social Login Google couvre la majorite de tes visiteurs. Mais certains preferent Facebook — c'est ce qu'on configure dans la prochaine lecon.

---

**Points cles** :
- Social Login active dans Settings > Design & Content > Login
- Client ID et Client Secret crees dans Google Cloud Console > Credentials
- OAuth consent screen configure en mode External
- Redirect URI fournie par TutorLMS a coller dans Google Cloud

**Mots cles SEO** : Social Login TutorLMS Google, connexion Google LMS WordPress, OAuth TutorLMS, inscription Google TutorLMS

---

### Lecon 11.4 — Social Login (Facebook)

**Duree** : 5 min
**Type** : Video HeyGen
**Ecran** : Face camera pour intro/conclusion, screencast Meta for Developers + TutorLMS
**Source** : Video #21 + doc get-facebook-app-id

---

**[INTRO — face camera]**

Apres Google, Facebook. Certains de tes eleves preferent se connecter avec leur compte Facebook. La configuration est un peu differente — ca passe par Meta for Developers. On fait ca ensemble.

**[ECRAN — screencast WordPress admin]**

[Navigation vers Tutor LMS > Settings > Design & Content > Login]

Dans TutorLMS, meme endroit que pour Google : Settings, Design & Content, Login. Active le toggle "Facebook Login". Tu as besoin d'un App ID et d'un App Secret.

**[ECRAN — screencast Meta for Developers]**

[Navigation vers developers.facebook.com > My Apps]

Va sur developers.facebook.com. Connecte-toi avec ton compte Facebook. Clique sur "Create App".

**[ECRAN — screencast creation de l'app]**

[Montre les etapes de creation]

1. Use case — selectionne "Authenticate and request data from users with Facebook Login"
2. App name — donne un nom clair, par exemple "TutorLMS Login"
3. App contact email — ton email professionnel

Valide. Facebook cree l'application.

**[ECRAN — screencast configuration Facebook Login]**

[Navigation vers Facebook Login > Settings dans l'app]

Dans le menu de l'app, va dans Facebook Login, puis Settings. Dans le champ "Valid OAuth Redirect URIs", colle l'URL de callback que TutorLMS t'affiche. C'est la meme logique que pour Google.

**[ECRAN — screencast App ID et App Secret]**

[Navigation vers Settings > Basic]

Pour recuperer tes cles, va dans Settings, puis Basic. Tu y trouves l'App ID (affiche directement) et l'App Secret (clique sur "Show" pour le reveler).

**[ECRAN — screencast retour TutorLMS]**

[Colle l'App ID et l'App Secret]

Retourne dans TutorLMS. Colle l'App ID et l'App Secret. Enregistre.

**[ECRAN — screencast front-end]**

[Montre les deux boutons Social Login sur la page de connexion]

Ta page de connexion affiche maintenant deux boutons : "Sign in with Google" et "Sign in with Facebook". L'eleve choisit celui qu'il prefere.

**[TRANSITION — face camera]**

Avec Google et Facebook configures, tu couvres la grande majorite des comptes sociaux. Mais le Social Login ne protege pas contre les bots. Prochaine lecon : on ajoute reCAPTCHA pour securiser les formulaires.

---

**Points cles** :
- App creee sur developers.facebook.com avec le use case "Facebook Login"
- App ID et App Secret dans Settings > Basic de l'app
- Redirect URI TutorLMS a coller dans Facebook Login > Settings
- Les deux boutons Google + Facebook apparaissent sur la page de connexion

**Mots cles SEO** : Social Login Facebook TutorLMS, connexion Facebook LMS WordPress, Meta App ID TutorLMS, Facebook Login WordPress

---

### Lecon 11.5 — reCAPTCHA anti-fraude

**Duree** : 5 min
**Type** : Video HeyGen
**Ecran** : Face camera pour intro/conclusion, screencast Google reCAPTCHA + TutorLMS
**Source** : Video #23 + doc create-recaptcha-keys

---

**[INTRO — face camera]**

Les bots adorent les formulaires d'inscription. Faux comptes, spam, tentatives de brute force — c'est un probleme reel des que ton site a un peu de trafic. reCAPTCHA bloque ces bots avant qu'ils ne posent probleme. TutorLMS l'integre nativement — on le configure maintenant.

**[ECRAN — screencast WordPress admin]**

[Navigation vers Tutor LMS > Settings > Design & Content > Login]

Dans TutorLMS, va dans Settings, Design & Content, onglet Login. Cherche la section "reCAPTCHA". Active le toggle. TutorLMS te demande une Site Key et une Secret Key.

**[ECRAN — screencast Google reCAPTCHA admin]**

[Navigation vers google.com/recaptcha/admin]

Va sur google.com/recaptcha/admin. Connecte-toi avec ton compte Google. Clique sur le "+" pour creer un nouveau site.

**[ECRAN — screencast formulaire de creation]**

[Montre les champs a remplir]

Remplis les champs :

1. Label — le nom de ton site, pour t'y retrouver
2. reCAPTCHA type — selectionne "reCAPTCHA v2" avec l'option "I'm not a robot" checkbox. TutorLMS ne supporte pas encore v3 nativement.
3. Domains — entre ton nom de domaine, sans https, par exemple "ton-site.com"
4. Accept the terms of service

Valide.

**[ECRAN — screencast cles generees]**

[Montre la Site Key et la Secret Key]

Google genere deux cles :
- Site Key — la cle publique, visible dans le code HTML de ta page
- Secret Key — la cle privee, qui reste sur ton serveur

Copie les deux.

**[ECRAN — screencast retour TutorLMS]**

[Colle les cles dans les champs correspondants]

Retourne dans TutorLMS. Colle la Site Key et la Secret Key dans les champs. Enregistre.

**[ECRAN — screencast front-end]**

[Montre le formulaire d'inscription avec le reCAPTCHA visible]

Sur ta page d'inscription, la checkbox "I'm not a robot" apparait en bas du formulaire. Les visiteurs reels cochent la case, les bots sont bloques.

**[TRANSITION — face camera]**

Le reCAPTCHA est une protection de base, mais efficace. Combine-le avec la verification email de la lecon 11.1, et tu as un double filtre contre les faux comptes. Prochaine lecon : on passe aux regles business avec l'enrollment scheduling.

---

**Points cles** :
- reCAPTCHA active dans Settings > Design & Content > Login
- Cles creees sur google.com/recaptcha/admin (v2 checkbox)
- Site Key (publique) + Secret Key (privee) a coller dans TutorLMS
- Combine avec la verification email pour une double protection

**Mots cles SEO** : reCAPTCHA TutorLMS, securiser inscription LMS WordPress, anti-spam TutorLMS, proteger formulaire TutorLMS

---

### Lecon 11.6 — Enrollment & scheduling

**Duree** : 6 min
**Type** : Video HeyGen
**Ecran** : Face camera pour intro/conclusion, screencast Addon Enrollment + Course Builder
**Source** : Video #36 + doc addons/enrollment

---

**[INTRO — face camera]**

Par defaut, un eleve peut s'inscrire a un cours a n'importe quel moment. Mais dans certains cas, tu veux controler quand l'inscription est ouverte — par exemple pour un cours en cohorte, une session qui demarre a date fixe, ou une offre limitee dans le temps. L'addon Enrollment de TutorLMS gere tout ca.

**[ECRAN — screencast WordPress admin]**

[Navigation vers Tutor LMS > Addons]

Pour activer l'addon, va dans Tutor LMS, puis Addons. Cherche "Enrollment". Active-le. C'est un addon Pro — il faut la licence TutorLMS Pro active.

**[ECRAN — screencast Course Builder]**

[Navigation vers la section Enrollment d'un cours]

Une fois l'addon actif, ouvre un cours dans le Course Builder. Tu trouves une nouvelle section "Enrollment". Trois options principales :

1. Open — inscription ouverte en permanence. C'est le comportement par defaut.
2. Closed — inscription fermee. Personne ne peut s'inscrire. Utile quand tu prepares un cours et que tu ne veux pas d'inscriptions anticipees.
3. By Date — tu definis une fenetre d'inscription avec une date de debut et une date de fin.

**[ECRAN — screencast configuration By Date]**

[Montre les champs date de debut et date de fin]

Avec l'option "By Date", tu configures :
- Enrollment Start Date — la date et l'heure d'ouverture des inscriptions
- Enrollment End Date — la date et l'heure de fermeture

En dehors de cette fenetre, le bouton d'inscription est remplace par un message indiquant que l'inscription est fermee ou qu'elle ouvrira a telle date.

**[ECRAN — screencast front-end avant/pendant/apres]**

[Montre les trois etats du bouton d'inscription]

Trois situations cote visiteur :
- Avant la date de debut — message "Enrollment opens on [date]"
- Pendant la fenetre — bouton d'inscription actif
- Apres la date de fin — message "Enrollment is closed"

C'est automatique, pas besoin de revenir modifier manuellement.

**[ECRAN — screencast cas d'usage]**

[Montre un cours configure en cohorte]

Cas d'usage concret : tu lances une formation en cohorte qui demarre le 1er du mois. Tu ouvres les inscriptions du 15 au 28 du mois precedent. Ceux qui s'inscrivent commencent ensemble. Ceux qui arrivent trop tard attendront la prochaine session.

**[TRANSITION — face camera]**

L'enrollment scheduling est un outil puissant pour creer de l'urgence et structurer tes lancements. Mais que se passe-t-il quand un eleve est deja inscrit et que tu veux limiter la duree de son acces ? C'est le sujet de la prochaine lecon : l'expiration d'inscription.

---

**Points cles** :
- Addon Enrollment active dans Tutor LMS > Addons (Pro requis)
- Trois modes : Open, Closed, By Date
- By Date = fenetre d'inscription avec debut et fin
- Le bouton d'inscription s'adapte automatiquement selon les dates
- Ideal pour les cours en cohorte et les lancements

**Mots cles SEO** : enrollment scheduling TutorLMS, inscription programmee LMS WordPress, cours cohorte TutorLMS, fenetre inscription TutorLMS

---

### Lecon 11.7 — Expiration d'inscription

**Duree** : 5 min
**Type** : Video HeyGen
**Ecran** : Face camera pour intro/conclusion, screencast Course Builder section expiration
**Source** : doc tutorials/enrollment-expiration

---

**[INTRO — face camera]**

Tu veux que l'acces a un cours expire apres un certain temps ? Par exemple, 12 mois apres l'achat, ou 90 jours pour un essai gratuit. TutorLMS permet de definir une duree d'acces limitee pour chaque cours. Une fois le delai depasse, l'eleve perd l'acces automatiquement.

**[ECRAN — screencast Course Builder]**

[Navigation vers un cours > section Settings ou Enrollment]

Ouvre un cours dans le Course Builder. Va dans les reglages du cours. Cherche la section "Enrollment Expiry" ou "Content Access Expiry" selon ta version.

**[ECRAN — screencast configuration expiration]**

[Montre les champs de configuration]

Tu as deux elements a configurer :

1. Enable Enrollment Expiry — active le toggle pour ce cours
2. Expire After — definis la duree en jours. Par exemple, 365 pour un an, 90 pour un trimestre, 30 pour un mois

La duree commence a partir de la date d'inscription de l'eleve, pas de la date de creation du cours. Chaque eleve a donc son propre compte a rebours.

**[ECRAN — screencast front-end eleve]**

[Montre le dashboard eleve avec la date d'expiration visible]

Cote eleve, la date d'expiration est visible dans son tableau de bord. Il sait exactement quand son acces se termine. Pas de surprise.

**[ECRAN — screencast apres expiration]**

[Montre ce qui se passe quand l'acces expire]

Une fois le delai depasse :
- L'eleve ne peut plus acceder au contenu du cours
- Le cours apparait toujours dans son historique, mais marque comme expire
- Si tu le souhaites, l'eleve peut se reinscrire — en rachetant le cours ou via une action manuelle de ta part

**[ECRAN — screencast cas d'usage]**

[Montre deux exemples de configuration]

Deux cas d'usage courants :

1. Formation premium a acces limite — 12 mois d'acces apres l'achat. Ca pousse l'eleve a suivre la formation dans un temps raisonnable et te permet de vendre un renouvellement.
2. Essai gratuit — 14 ou 30 jours d'acces a un cours gratuit. Apres, l'eleve doit acheter pour continuer.

**[TRANSITION — face camera]**

L'expiration d'inscription est un levier business important. Elle cree une urgence naturelle et te permet de monetiser les renouvellements. Prochaine lecon : on voit comment vendre a des visiteurs qui n'ont pas encore de compte — l'achat invite.

---

**Points cles** :
- Enrollment Expiry active par cours dans les reglages du Course Builder
- Duree configurable en jours (commence a l'inscription de l'eleve)
- L'eleve voit la date d'expiration dans son dashboard
- Apres expiration : acces bloque, possibilite de renouvellement
- Cas d'usage : acces limite 12 mois, essai gratuit 14-30 jours

**Mots cles SEO** : expiration inscription TutorLMS, acces limite cours WordPress, enrollment expiry TutorLMS, duree acces formation LMS

---

### Lecon 11.8 — Achat invite (Guest Purchase)

**Duree** : 4 min
**Type** : Video HeyGen
**Ecran** : Face camera pour intro/conclusion, screencast reglages Guest Purchase
**Source** : doc tutorials/guest-purchase

---

**[INTRO — face camera]**

Par defaut, un visiteur doit creer un compte avant de pouvoir acheter un cours. Ca ajoute une etape, et chaque etape supplementaire fait perdre des acheteurs. Le Guest Purchase permet a un visiteur d'acheter un cours sans creer de compte au prealable. TutorLMS cree le compte automatiquement apres le paiement.

**[ECRAN — screencast WordPress admin]**

[Navigation vers Tutor LMS > Settings > Monetization > Checkout]

Pour activer le Guest Purchase, va dans Tutor LMS, Settings, Monetization, puis Checkout. Cherche l'option "Guest Checkout" ou "Allow guest users to purchase courses". Active le toggle.

**[ECRAN — screencast configuration]**

[Montre les options liees au Guest Purchase]

Quand le Guest Purchase est actif, le processus d'achat change :

1. Le visiteur ajoute un cours au panier sans etre connecte
2. Sur la page de paiement, il entre son email et ses informations de paiement
3. Apres le paiement, TutorLMS cree automatiquement un compte avec cet email
4. L'eleve recoit un email avec ses identifiants de connexion

Pas de formulaire d'inscription, pas de mot de passe a choisir avant l'achat. Le frein est supprime.

**[ECRAN — screencast front-end parcours achat]**

[Montre le parcours complet d'un achat invite]

Voici le parcours complet d'un achat invite : le visiteur clique sur "Buy Now", entre son email et sa carte, valide le paiement, et recoit immediatement acces au cours. Son compte est cree en arriere-plan.

**[ECRAN — screencast back-office verification]**

[Montre le nouvel utilisateur cree automatiquement]

Cote admin, tu vois le nouvel utilisateur dans la liste WordPress, avec le cours achete lie a son compte. Tout est automatique.

**[TRANSITION — face camera]**

Le Guest Purchase est un quick win pour ameliorer ton taux de conversion. Moins d'etapes, plus de ventes. Prochaine lecon : on voit comment limiter l'inscription a un seul cours par utilisateur — utile pour les offres exclusives.

---

**Points cles** :
- Guest Checkout active dans Settings > Monetization > Checkout
- Le visiteur achete sans creer de compte au prealable
- TutorLMS cree le compte automatiquement apres le paiement
- Email avec identifiants envoye automatiquement
- Reduit le frein a l'achat et ameliore la conversion

**Mots cles SEO** : guest purchase TutorLMS, achat sans compte LMS WordPress, guest checkout TutorLMS, achat invite formation WordPress

---

### Lecon 11.9 — Limiter un cours par utilisateur

**Duree** : 4 min
**Type** : Video HeyGen
**Ecran** : Face camera pour intro/conclusion, screencast reglages limitation
**Source** : doc tutorials/limit-one-course

---

**[INTRO — face camera]**

Dans certains cas, tu veux qu'un utilisateur ne puisse s'inscrire qu'a un seul cours. Par exemple, pour une offre d'essai ou chaque nouvel inscrit a droit a un cours gratuit. Ou pour eviter qu'un eleve s'inscrive a tous tes cours gratuits sans jamais passer a l'achat. TutorLMS permet de poser cette limite.

**[ECRAN — screencast WordPress admin]**

[Navigation vers Tutor LMS > Settings]

Va dans Tutor LMS, puis Settings. Cherche l'option "Limit Enrollment per Student" ou "Enrollment Restriction". Selon ta version de TutorLMS, cette option peut etre dans l'onglet General ou dans les reglages avances.

**[ECRAN — screencast configuration]**

[Montre les options de limitation]

L'option te permet de definir le nombre maximum de cours auxquels un etudiant peut s'inscrire. Par defaut, c'est illimite. Tu peux le passer a 1 pour une offre d'essai, a 3 pour un plan basique, ou a n'importe quel nombre qui correspond a ton modele.

**[ECRAN — screencast front-end tentative d'inscription]**

[Montre ce qui se passe quand un eleve depasse la limite]

Quand un eleve atteint sa limite et essaye de s'inscrire a un cours supplementaire, TutorLMS affiche un message d'erreur. L'inscription est bloquee. L'eleve doit upgrader son plan ou se desinscrire d'un cours existant.

**[ECRAN — screencast cas d'usage]**

[Montre un scenario concret]

Scenario concret : tu proposes un plan gratuit avec acces a 1 cours, un plan Standard avec 3 cours, et un plan Premium avec acces illimite. Tu configures la limite en fonction du plan de chaque utilisateur. C'est un levier de monetisation efficace.

**[TRANSITION — face camera]**

La limitation par utilisateur fonctionne bien avec les memberships qu'on a vues dans le module eCommerce. Combine les deux pour creer des offres a paliers. Prochaine lecon — la derniere du module : on configure le profil instructeur visible par les eleves.

---

**Points cles** :
- Limite configurable dans Settings (nombre max de cours par etudiant)
- Par defaut : illimite. Modifiable a 1, 3, ou tout nombre
- Message d'erreur affiche quand la limite est atteinte
- Combine avec les memberships pour creer des offres a paliers

**Mots cles SEO** : limiter cours par utilisateur TutorLMS, restriction inscription LMS WordPress, enrollment limit TutorLMS, limite cours eleve TutorLMS

---

### Lecon 11.10 — Profil instructeur (frontend)

**Duree** : 5 min
**Type** : Video HeyGen
**Ecran** : Face camera pour intro/conclusion, screencast profil instructeur front-end
**Source** : doc tutorials/editing-instructor-profile

---

**[INTRO — face camera]**

Le profil instructeur, c'est la page publique qui presente un formateur a tes eleves. Photo, bio, liste de cours, evaluation — tout est visible. Un bon profil inspire confiance et aide a convertir. Dans cette lecon, on voit comment un instructeur configure son profil depuis le front-end, sans passer par le back-office.

**[ECRAN — screencast front-end instructeur]**

[Connexion en tant qu'instructeur > Dashboard]

Connecte-toi avec un compte instructeur. Depuis le dashboard TutorLMS, clique sur "Profile" ou sur le lien d'edition du profil.

**[ECRAN — screencast edition du profil]**

[Montre le formulaire d'edition du profil]

Le formulaire de profil instructeur contient plusieurs sections :

1. Photo de profil — l'avatar visible sur les pages de cours et la page profil
2. Nom d'affichage — le nom que les eleves voient
3. Designation — le titre professionnel, par exemple "Expert WordPress" ou "Formateur SEO"
4. Bio — le texte de presentation. C'est l'element le plus important. Ecris quelques phrases qui resument ton expertise et ce que l'eleve va apprendre avec toi.

**[ECRAN — screencast champs supplementaires]**

[Montre les reseaux sociaux et autres champs]

En dessous, tu trouves les champs optionnels :
- Site web personnel
- Liens reseaux sociaux — Twitter, Facebook, LinkedIn, YouTube, GitHub
- Competences / tags

Ces informations apparaissent sur la page publique du profil.

**[ECRAN — screencast page publique du profil]**

[Montre la page profil vue par un visiteur]

Voici ce que les eleves voient : la photo, le nom, la designation, la bio, les liens sociaux, et la liste des cours publies par cet instructeur. La note moyenne et le nombre d'eleves s'affichent aussi si les avis sont actives.

**[ECRAN — screencast bonnes pratiques]**

[Montre un profil bien rempli vs un profil vide]

Comparaison rapide : un profil complet avec photo professionnelle, bio detaillee et liens sociaux inspire confiance. Un profil vide avec juste un nom — ca fait amateur. Prends le temps de bien remplir chaque champ.

**[TRANSITION — face camera]**

Le profil instructeur est souvent neglige, mais c'est un facteur de confiance direct pour tes eleves. Assure-toi que chaque formateur sur ton site a un profil complet et professionnel. Ca conclut le module 11 — on termine avec le quiz pour valider tes acquis.

---

**Points cles** :
- Edition du profil accessible depuis le dashboard front-end
- Champs cles : photo, nom, designation, bio, reseaux sociaux
- La page publique affiche aussi les cours, la note moyenne et le nombre d'eleves
- Un profil complet inspire confiance et ameliore la conversion

**Mots cles SEO** : profil instructeur TutorLMS, page formateur LMS WordPress, personnaliser profil TutorLMS, instructor profile TutorLMS frontend

---

### Lecon 11.11 — Quiz Module 11

**Duree** : ~5 min (10 questions)
**Type** : Quiz TutorLMS
**Seuil de reussite** : 70%

---

**Question 1**
Ou active-t-on l'inscription etudiant dans TutorLMS ?

- A) Tutor LMS > Addons > Student Registration
- B) Settings > General > Student Registration ✓
- C) Settings > Monetization > Users
- D) WordPress > Settings > General

**Explication** : L'inscription etudiant s'active dans Tutor LMS > Settings > General > Student Registration.

---

**Question 2**
Pourquoi recommande-t-on l'approbation manuelle pour les instructeurs ?

- A) Pour accelerer le processus d'inscription
- B) Pour eviter que des formateurs non qualifies publient du contenu ✓
- C) Pour limiter le nombre d'instructeurs a un seul
- D) Pour empecher les instructeurs de modifier leurs cours

**Explication** : L'approbation manuelle permet de controler la qualite en verifiant chaque candidature avant de donner les droits de creation de cours.

---

**Question 3**
Quelles informations faut-il pour configurer le Social Login Google ?

- A) Un API Key et un Secret Token
- B) Un Client ID et un Client Secret crees dans Google Cloud Console ✓
- C) Un App ID et un App Secret crees dans Google Ads
- D) Un username et un mot de passe Google

**Explication** : Le Social Login Google necessite un Client ID et un Client Secret, crees dans Google Cloud Console > APIs & Services > Credentials.

---

**Question 4**
Ou cree-t-on l'App ID Facebook pour le Social Login ?

- A) Dans les parametres Facebook personnels
- B) Sur developers.facebook.com en creant une nouvelle application ✓
- C) Dans Google Cloud Console
- D) Dans les reglages WordPress

**Explication** : L'App ID Facebook se cree sur developers.facebook.com via "Create App" avec le use case "Facebook Login".

---

**Question 5**
Quelle version de reCAPTCHA est supportee nativement par TutorLMS ?

- A) reCAPTCHA v3 invisible
- B) reCAPTCHA v2 "I'm not a robot" checkbox ✓
- C) reCAPTCHA Enterprise
- D) hCaptcha

**Explication** : TutorLMS supporte nativement reCAPTCHA v2 avec la checkbox "I'm not a robot".

---

**Question 6**
Quels sont les trois modes d'inscription de l'addon Enrollment ?

- A) Free, Paid, Premium
- B) Open, Closed, By Date ✓
- C) Manual, Automatic, Scheduled
- D) Instant, Delayed, Recurring

**Explication** : L'addon Enrollment propose trois modes : Open (permanent), Closed (ferme), et By Date (fenetre avec date de debut et fin).

---

**Question 7**
A partir de quand commence le decompte de l'expiration d'inscription ?

- A) A la date de creation du cours
- B) A la date d'inscription de l'eleve ✓
- C) A la date de premiere connexion de l'eleve
- D) A la date de fin de la fenetre d'inscription

**Explication** : La duree d'expiration se calcule a partir de la date d'inscription de chaque eleve, pas de la date de creation du cours.

---

**Question 8**
Que se passe-t-il apres un Guest Purchase ?

- A) Le visiteur doit creer un compte manuellement apres l'achat
- B) TutorLMS cree automatiquement un compte et envoie les identifiants par email ✓
- C) L'acces au cours est temporaire sans compte
- D) L'admin doit valider l'achat et creer le compte

**Explication** : Avec le Guest Purchase, TutorLMS cree automatiquement un compte avec l'email saisi et envoie les identifiants de connexion par email.

---

**Question 9**
Quel est l'interet de limiter le nombre de cours par utilisateur ?

- A) Reduire la charge serveur
- B) Creer des offres a paliers et encourager l'upgrade vers un plan superieur ✓
- C) Empecher les eleves de tricher aux quiz
- D) Faciliter la gestion des certificats

**Explication** : Limiter les cours par utilisateur permet de creer des plans (gratuit = 1 cours, standard = 3, premium = illimite) et incite les eleves a upgrader.

---

**Question 10**
Quel element du profil instructeur a le plus d'impact sur la confiance des eleves ?

- A) Le nombre de reseaux sociaux renseignes
- B) Le nom d'affichage
- C) La bio detaillant l'expertise et les benefices pour l'eleve ✓
- D) L'URL du site personnel

**Explication** : La bio est l'element le plus important du profil instructeur. Elle resume l'expertise du formateur et ce que l'eleve va apprendre — c'est le facteur de confiance principal.

---

**Fin du Module 11.**
