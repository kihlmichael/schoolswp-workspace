# Scripts video — Module 10 : TutorLMS + FluentCRM

**Formation** : Maitriser FluentCRM
**Module** : M10 — TutorLMS + FluentCRM (Premium)
**Lecons** : 7 videos + 1 exercice + 1 quiz
**Duree totale** : ~55 min
**Prerequis** : M6 (automations de base), M7 (automation avancee — goals, conditionals)
**Date** : 2026-03-23

---

### Lecon 10.1 — Active l'integration TutorLMS dans FluentCRM

**Duree** : 5 min
**Type** : Video HeyGen
**Ecran** : Face camera pour intro/conclusion, screencast FluentCRM et TutorLMS

---

**[INTRO — face camera]**

Tu as FluentCRM pour le marketing. Tu as TutorLMS pour tes formations. Mais sans integration entre les deux, ce sont deux mondes separes. Tes etudiants ne recoivent pas les bons emails. Tes automations ne savent pas qui est inscrit a quoi. Et tu fais tout manuellement. Cette lecon connecte les deux. Une activation, quelques reglages, et FluentCRM voit tout ce qui se passe dans TutorLMS — inscriptions, completions, quiz. C'est le duo que personne ne montre. On va corriger ca.

**[ECRAN — screencast FluentCRM > Settings > Integrations]**

[Navigation vers FluentCRM > Settings > Integrations]

Etape 1 : va dans FluentCRM, puis Settings, puis l'onglet Integrations. Tu vois la liste des plugins compatibles. Cherche TutorLMS. Si TutorLMS est installe et actif sur ton WordPress, tu verras un toggle pour activer l'integration.

[Montre le toggle TutorLMS dans la liste]

Etape 2 : active le toggle. FluentCRM va scanner tes cours TutorLMS et rendre disponibles les triggers, actions et filtres specifiques. Sans cette activation, les blocs TutorLMS n'apparaissent pas dans le builder d'automation.

**[ECRAN — screencast verification post-activation]**

[Va dans Automations > Nouveau trigger]

Etape 3 : verifie que l'integration fonctionne. Cree une nouvelle automation. Dans la liste des triggers, tu devrais maintenant voir une categorie "TutorLMS" avec plusieurs declencheurs : Student enrolled in a course, Course completed, Lesson completed, Quiz passed, Quiz failed. Si tu vois ces options, l'integration est active.

[Montre la liste des triggers TutorLMS]

Etape 4 : verifie aussi les actions. Dans le builder, ajoute une action. Tu devrais voir "Enroll student in a course" et "Remove from course" dans les options TutorLMS.

[Montre les actions TutorLMS dans le builder]

**[ECRAN — screencast FluentCRM > Settings > TutorLMS]**

[Montre les options de configuration specifiques]

Etape 5 : retourne dans Settings > Integrations > TutorLMS. Tu as quelques options supplementaires. La plus importante : la synchronisation automatique. Quand un etudiant s'inscrit a un cours via TutorLMS, FluentCRM peut automatiquement creer ou mettre a jour le contact correspondant. Active cette option. Sans elle, tu devras importer manuellement — ce qu'on voit dans la prochaine lecon.

**[TRANSITION — face camera]**

L'integration est active. FluentCRM voit maintenant tout ce qui se passe dans TutorLMS. Dans la prochaine lecon, on importe les etudiants qui existaient deja avant l'activation — pour que ta base soit complete des le depart.

---

**Points cles** :
- Activation dans FluentCRM > Settings > Integrations > TutorLMS
- TutorLMS doit etre installe et actif pour que le toggle apparaisse
- L'activation debloque les triggers (enrolled, completed, quiz) et les actions (enroll, remove)
- Activer la synchronisation automatique pour les nouvelles inscriptions
- Sans activation, les blocs TutorLMS sont invisibles dans le builder

**Mots cles SEO** : FluentCRM TutorLMS integration, connecter TutorLMS FluentCRM, automation LMS WordPress, FluentCRM settings integration

---

### Lecon 10.2 — Importe tes etudiants TutorLMS existants

**Duree** : 5 min
**Type** : Video HeyGen
**Ecran** : Face camera pour intro/conclusion, screencast FluentCRM import

---

**[INTRO — face camera]**

Tu viens d'activer l'integration. Les nouveaux etudiants seront synchronises automatiquement. Mais ceux qui etaient deja inscrits avant ? Ils existent dans TutorLMS mais pas forcement dans FluentCRM — ou ils y sont sans les bonnes infos. Dans cette lecon, on importe les etudiants existants et on les tag correctement pour que tes automations fonctionnent sur toute ta base.

**[ECRAN — screencast FluentCRM > Contacts > Import]**

[Navigation vers FluentCRM > Contacts > Import]

Etape 1 : va dans FluentCRM > Contacts > Import. Tu as plusieurs methodes d'import. Celle qui nous interesse : "Import from TutorLMS" ou, si cette option n'apparait pas, "Import from WordPress Users" avec un filtre par role.

[Montre les options d'import]

Etape 2 : si tu as l'option directe TutorLMS, utilise-la. FluentCRM va lister tous les utilisateurs WordPress qui ont au moins une inscription TutorLMS. Selectionne-les tous ou filtre par cours.

[Montre la liste des etudiants a importer]

**[ECRAN — screencast mapping et tags]**

[Montre l'ecran de configuration de l'import]

Etape 3 : configure le mapping. Le prenom, le nom et l'email sont mappes automatiquement. L'important, c'est ce que tu ajoutes. Assigne une liste — par exemple "etudiants-tutorlms" — et un tag de base — "student".

[Montre l'ajout de liste et tag]

Etape 4 : pour les tags par cours, tu as deux approches. L'approche manuelle : tu importes cours par cours et tu assignes un tag specifique a chaque import. Par exemple, tu importes les inscrits a "Maitriser FluentCRM" avec le tag "enrolled-fluentcrm". Puis les inscrits a "Creer son LMS" avec le tag "enrolled-lms".

[Montre un import filtre par cours avec tag specifique]

L'approche automatique : tu importes tout le monde avec le tag generique "student", puis tu crees une automation qui pose les tags specifiques selon les cours. On verra cette approche dans la lecon 10.3 avec les triggers.

**[ECRAN — screencast lancement de l'import]**

[Lance l'import et montre la progression]

Etape 5 : lance l'import. FluentCRM traite les contacts par lots. Les contacts existants sont mis a jour — ils ne sont pas dupliques. Les nouveaux contacts sont crees. A la fin, tu as un rapport : X contacts crees, Y contacts mis a jour, Z ignores.

[Montre le rapport d'import]

Etape 6 : verifie le resultat. Va dans Contacts, filtre par la liste "etudiants-tutorlms". Tous tes etudiants doivent apparaitre avec les bons tags.

**[TRANSITION — face camera]**

Ta base est complete. Etudiants existants importes et tagges, nouveaux etudiants synchronises automatiquement. Maintenant on passe aux triggers TutorLMS — les evenements qui vont declencher tes automations.

---

**Points cles** :
- Import via FluentCRM > Contacts > Import (option TutorLMS ou WordPress Users)
- Toujours assigner une liste et un tag de base a l'import
- Deux approches pour les tags par cours : import separe par cours ou automation post-import
- Les contacts existants sont mis a jour, pas dupliques
- Verifier le rapport d'import et filtrer pour confirmer

**Mots cles SEO** : importer etudiants TutorLMS FluentCRM, synchroniser contacts LMS, import FluentCRM WordPress users, migration TutorLMS

---

### Lecon 10.3 — Triggers TutorLMS : enrollment, completion, quiz passed

**Duree** : 7 min
**Type** : Video HeyGen
**Ecran** : Face camera pour intro/conclusion, screencast FluentCRM automation builder

---

**[INTRO — face camera]**

Un etudiant s'inscrit a un cours. Un autre termine une lecon. Un troisieme rate un quiz. Trois evenements, trois reactions differentes a automatiser. Les triggers TutorLMS dans FluentCRM detectent ces evenements et declenchent tes automations automatiquement. Dans cette lecon, on configure les cinq triggers principaux avec des cas concrets tires de la formation schoolsWP.

**[ECRAN — screencast FluentCRM > Automations > New]**

[Cree une nouvelle automation, montre la liste des triggers]

Etape 1 : cree une nouvelle automation. A l'etape de selection du trigger, cherche la categorie TutorLMS. Tu as cinq triggers disponibles.

[Montre les 5 triggers TutorLMS]

Trigger 1 : "Student Enrolled in a Course". Se declenche quand un etudiant s'inscrit a un cours — que ce soit une inscription gratuite, un achat, ou un enroll manuel. Tu choisis le cours concerne ou "Any Course" pour tous les cours.

**[ECRAN — screencast configuration trigger Enrolled]**

[Configure le trigger Enrolled avec un cours specifique]

Etape 2 : cas concret. Sur schoolsWP, quand un etudiant s'inscrit aux modules gratuits M1-M3, on veut poser le tag "free-student" et demarrer une sequence de nurturing. Selectionne le cours "Maitriser FluentCRM — Modules 1-3", et dans la suite de l'automation, ajoute l'action "Apply Tag > free-student".

[Montre la configuration complete : trigger enrolled + action apply tag]

**[ECRAN — screencast trigger Course Completed]**

[Selectionne le trigger Course Completed]

Trigger 2 : "Course Completed". Se declenche quand un etudiant termine toutes les lecons et tous les quiz d'un cours. C'est le trigger le plus strategique pour le marketing — l'etudiant a fini, il est pret pour la suite.

[Configure avec le cours gratuit M1-M3]

Etape 3 : cas concret. Quand un etudiant termine les modules gratuits, c'est le moment de proposer la formation premium. Le trigger "Course Completed" sur M1-M3 declenche une sequence de vente vers les modules M4-M16.

**[ECRAN — screencast trigger Lesson Completed]**

[Selectionne le trigger Lesson Completed]

Trigger 3 : "Lesson Completed". Plus granulaire — se declenche a chaque lecon terminee. Utile pour le suivi de progression, mais attention : si ton cours a 30 lecons, ce trigger se declenchera 30 fois par etudiant. Utilise-le avec des conditions pour eviter le bruit.

[Montre la selection d'une lecon specifique]

Etape 4 : cas concret. Tu veux envoyer un email de felicitation quand un etudiant termine la lecon 3.6 "Cree ta premiere automation" — un milestone important. Configure le trigger sur cette lecon specifique, pas sur "Any Lesson".

**[ECRAN — screencast triggers Quiz]**

[Montre les deux triggers quiz]

Trigger 4 : "Quiz Passed". Se declenche quand un etudiant reussit un quiz avec le score minimum requis.

Trigger 5 : "Quiz Failed". Se declenche quand un etudiant echoue. C'est celui que la plupart des gens oublient — et c'est pourtant le plus utile pour la retention.

[Configure le trigger Quiz Failed]

Etape 5 : cas concret. Un etudiant echoue au quiz du module 6. Tu declenches un email automatique : "Tu n'as pas obtenu le score minimum sur le quiz M6. Voici les lecons a revoir avant de retenter." Tu ajoutes les liens directs vers les lecons concernees. C'est de l'accompagnement automatise — pas du spam.

**[ECRAN — slide recapitulatif des 5 triggers]**

[Tableau : trigger, evenement, cas d'usage]

Recapitulatif rapide. Enrolled — inscription a un cours — tagging et welcome sequence. Course Completed — cours termine — upsell et certification. Lesson Completed — lecon terminee — suivi de progression et milestones. Quiz Passed — quiz reussi — felicitation et deblocage. Quiz Failed — quiz rate — relance et support.

**[TRANSITION — face camera]**

Tu connais les cinq triggers TutorLMS. Chacun detecte un moment precis du parcours etudiant. Dans la prochaine lecon, on passe de l'autre cote — les actions. Tu vas pouvoir inscrire et desinscrire des etudiants de cours directement depuis tes automations FluentCRM.

---

**Points cles** :
- 5 triggers TutorLMS : Enrolled, Course Completed, Lesson Completed, Quiz Passed, Quiz Failed
- Chaque trigger peut cibler un cours/lecon/quiz specifique ou "Any"
- Lesson Completed se declenche a chaque lecon — utiliser avec conditions pour eviter le bruit
- Quiz Failed = trigger sous-utilise mais strategique pour la retention
- Cas schoolsWP : inscription gratuite M1-M3 → tag "free-student" → nurturing → upsell M4-M16

**Mots cles SEO** : FluentCRM TutorLMS trigger, automation inscription cours, trigger quiz FluentCRM, automatiser LMS WordPress

---

### Lecon 10.4 — Actions TutorLMS : enroll in course, remove from course

**Duree** : 6 min
**Type** : Video HeyGen
**Ecran** : Face camera pour intro/conclusion, screencast FluentCRM automation builder

---

**[INTRO — face camera]**

Dans la lecon precedente, TutorLMS declenchait des automations dans FluentCRM. Maintenant on fait l'inverse : FluentCRM agit sur TutorLMS. Un contact achete ta formation premium ? FluentCRM l'inscrit automatiquement aux modules M4 a M16 sans que tu leves le petit doigt. Un remboursement ? FluentCRM retire l'acces. Deux actions, enormement de temps gagne.

**[ECRAN — screencast FluentCRM > Automation builder]**

[Ouvre une automation existante, montre les actions disponibles]

Etape 1 : dans le builder d'automation, ajoute une action. Dans la liste, tu trouves deux actions TutorLMS. "Enroll Student in a Course" — inscrit le contact a un cours. "Remove from Course" — retire l'acces.

[Montre les deux actions dans la liste]

**[ECRAN — screencast action Enroll]**

[Ajoute l'action Enroll et configure-la]

Etape 2 : configure l'action Enroll. Tu selectionnes le cours cible. Un cours par action. Si tu veux inscrire a plusieurs cours, tu enchaines plusieurs actions Enroll.

[Montre la selection du cours]

Etape 3 : cas concret — le funnel schoolsWP. L'automation demarre quand un contact recoit le tag "a-achete-premium" (pose par WooCommerce apres l'achat). L'action Enroll inscrit l'etudiant au cours "Maitriser FluentCRM — Modules 4-16".

[Montre l'automation complete : trigger tag applied > enroll course]

Mais on ne s'arrete pas la. Apres l'enroll, on ajoute trois actions supplementaires. Apply tag "premium-student". Remove tag "free-student" — il n'est plus en version gratuite. Et un email de bienvenue avec les liens d'acces directs.

[Montre la sequence complete : enroll > apply tag > remove tag > send email]

**[ECRAN — screencast action Remove from Course]**

[Ajoute l'action Remove et configure-la]

Etape 4 : l'action Remove from Course. Meme logique — tu selectionnes le cours concerne.

Etape 5 : cas concret. Un etudiant demande un remboursement. Ton plugin e-commerce pose le tag "refunded". L'automation detecte ce tag, retire l'acces au cours premium, et envoie un email de confirmation de remboursement.

[Montre l'automation : trigger tag "refunded" > remove from course > send email]

**[ECRAN — screencast enchainement multi-cours]**

[Montre une automation avec plusieurs Enroll]

Etape 6 : pour inscrire a plusieurs cours dans la meme automation, enchaine les actions. Attention a l'ordre — TutorLMS traite chaque inscription sequentiellement. Si tu as beaucoup de cours, ajoute un delai de quelques secondes entre chaque Enroll pour eviter de surcharger le serveur.

[Montre trois actions Enroll avec des delais de 5 secondes entre chaque]

**[TRANSITION — face camera]**

Tu controles maintenant l'acces aux cours depuis tes automations. Inscription automatique a l'achat, retrait a la desinscription. Dans la prochaine lecon, on combine triggers et actions avec les goals et les conditionals — pour creer des parcours etudiants vraiment intelligents.

---

**Points cles** :
- 2 actions TutorLMS : Enroll Student in a Course, Remove from Course
- Une action = un cours. Pour plusieurs cours, enchainer les actions
- Cas principal : achat → tag "a-achete-premium" → enroll automatique + tag "premium-student"
- Remboursement : tag "refunded" → remove from course + email confirmation
- Pour multi-enroll : ajouter quelques secondes de delai entre chaque action

**Mots cles SEO** : FluentCRM enroll course TutorLMS, inscrire etudiant automatiquement, automation achat formation, FluentCRM action TutorLMS

---

### Lecon 10.5 — Goals et conditionals specifiques TutorLMS

**Duree** : 7 min
**Type** : Video HeyGen
**Ecran** : Face camera pour intro/conclusion, screencast FluentCRM automation builder

---

**[INTRO — face camera]**

Tu as vu les goals dans le module 7. Maintenant on les utilise avec TutorLMS. Un goal "a termine le cours X" dans une sequence de nurturing. Un conditional "est inscrit au cours Y" pour personnaliser les emails. C'est la que l'integration devient vraiment puissante — tes automations reagissent en temps reel a la progression de chaque etudiant.

**[ECRAN — screencast FluentCRM > Automation builder]**

[Ouvre une automation de nurturing post-inscription gratuite]

Etape 1 : contexte. On reprend le funnel schoolsWP. Un etudiant s'inscrit aux modules gratuits M1-M3. Il entre dans une automation de nurturing qui envoie des emails de valeur et propose la formation premium. Le probleme : combien de temps dure ce nurturing ?

[Montre la sequence d'emails de nurturing]

Etape 2 : ajoute un goal "Course Completed" sur le cours M1-M3. Place-le dans l'automation. Ce goal detecte quand l'etudiant a termine les modules gratuits.

[Place le bloc Goal dans l'automation]

**[ECRAN — screencast configuration du Goal TutorLMS]**

[Configure le goal avec la condition Course Completed]

Etape 3 : configure le goal. Condition : le contact a termine le cours "Maitriser FluentCRM — Modules 1-3". Mode : goal optionnel — "Can be achieved at any time". Pourquoi optionnel ? Parce que si l'etudiant ne finit pas le cours, tu veux quand meme qu'il recoive les emails suivants.

[Montre les parametres du goal]

Etape 4 : place le goal juste avant ta sequence de vente. Voila ce qui se passe. L'etudiant recoit les emails de nurturing. A n'importe quel moment, s'il termine le cours M1-M3, il saute directement au goal. Apres le goal, tu places ta sequence de vente — "Tu as fini les bases, voici ce que la formation complete t'apporte." Le timing est parfait : l'email de vente arrive au moment ou l'etudiant est le plus engage.

**[ECRAN — screencast conditionals TutorLMS]**

[Ajoute un bloc conditionnel dans l'automation]

Etape 5 : les conditionals. Ajoute un bloc "Conditional" dans ton automation. Dans les conditions disponibles, tu trouves des filtres TutorLMS. "Is enrolled in course X" — verifie si le contact est inscrit a un cours. "Has completed course X" — verifie si le cours est termine.

[Montre les conditions TutorLMS dans le bloc conditionnel]

Etape 6 : cas concret. Apres le goal, tu veux personnaliser l'email de vente. Condition : "Has completed course M1-M3". Branche Oui : email de vente avec angle "Tu as deja vu la puissance de FluentCRM, imagine ce que tu feras avec les modules avances." Branche Non : email avec angle "Tu n'as pas encore explore tous les modules gratuits — termine-les d'abord, puis on en reparle."

[Montre les deux branches avec des emails differents]

**[ECRAN — screencast goal essentiel pour prerequis]**

[Cree une nouvelle automation avec un goal essentiel]

Etape 7 : deuxieme cas — le goal essentiel. Tu as un parcours ou l'etudiant doit terminer le module 6 (automations de base) avant d'acceder au module 7 (automation avancee). Le goal "Course Completed > Module 6" est en mode essentiel — "Must be achieved to proceed". L'etudiant ne recoit pas les emails du module 7 tant qu'il n'a pas termine le module 6.

[Montre la configuration en mode essentiel]

**[TRANSITION — face camera]**

Goals et conditionals transforment tes automations en parcours adaptatifs. Chaque etudiant avance a son rythme, recoit le bon message au bon moment. Dans la prochaine lecon, on va encore plus loin avec les filtres avances — segmentation par cours, progression et instructeur.

---

**Points cles** :
- Goal "Course Completed" = detecte la fin d'un cours dans l'automation
- Goal optionnel pour le nurturing (le contact continue meme sans finir le cours)
- Goal essentiel pour les prerequis (le contact est bloque tant que le cours n'est pas termine)
- Conditionals TutorLMS : "Is enrolled in course X", "Has completed course X"
- Personnalisation des emails selon la progression reelle de l'etudiant

**Mots cles SEO** : FluentCRM goal TutorLMS, conditional automation LMS, personnaliser email progression cours, funnel etudiant FluentCRM

---

### Lecon 10.6 — Filtre avance : segmente par cours, progression, instructeur

**Duree** : 6 min
**Type** : Video HeyGen
**Ecran** : Face camera pour intro/conclusion, screencast FluentCRM contacts et segments

---

**[INTRO — face camera]**

Tu as 500 contacts dans FluentCRM. Parmi eux, des etudiants inscrits a differents cours, a differents stades de progression. Tu veux envoyer un email uniquement aux etudiants inscrits au cours FluentCRM qui n'ont pas encore termine le module 3. Les filtres avances TutorLMS dans FluentCRM te permettent ce niveau de precision. Dans cette lecon, on construit des segments dynamiques bases sur les donnees TutorLMS.

**[ECRAN — screencast FluentCRM > Contacts > Filtres]**

[Ouvre la vue contacts et montre les filtres disponibles]

Etape 1 : va dans FluentCRM > Contacts. Clique sur "Filter". Dans les filtres disponibles, tu trouves une section TutorLMS avec plusieurs criteres.

[Montre les filtres TutorLMS]

Filtre 1 : "Enrolled in Course". Selectionne un cours et FluentCRM affiche uniquement les contacts inscrits a ce cours. Tu peux combiner avec "Is" ou "Is not" — pour cibler les inscrits ou les non-inscrits.

[Applique le filtre et montre les resultats]

**[ECRAN — screencast filtre par progression]**

[Ajoute un filtre de progression]

Etape 2 : filtre par progression. "Course Completed" — filtre les contacts qui ont termine ou pas un cours specifique. Combine les deux : "Enrolled in Course X" ET "Course not completed" — tu obtiens les etudiants en cours de formation, ceux qui ont commence mais pas fini.

[Montre la combinaison de filtres]

Etape 3 : cas concret. Tu veux relancer les etudiants qui se sont inscrits aux modules gratuits mais ne les ont pas termines. Filtre : "Enrolled in M1-M3" + "Course M1-M3 not completed". Resultat : ta liste de contacts a relancer.

[Montre le resultat filtre]

**[ECRAN — screencast filtre par instructeur]**

[Montre le filtre instructeur si disponible]

Etape 4 : filtre par instructeur. Si tu as plusieurs instructeurs sur ton LMS, tu peux filtrer les etudiants d'un instructeur specifique. Utile pour les ecoles avec plusieurs formateurs — chaque instructeur peut avoir ses propres sequences email.

**[ECRAN — screencast creation de segments dynamiques]**

[Sauvegarde un filtre comme segment]

Etape 5 : transforme ton filtre en segment dynamique. Une fois tes criteres definis, sauvegarde le filtre. Ce segment se met a jour automatiquement — chaque nouveau contact qui correspond aux criteres y entre, chaque contact qui ne correspond plus en sort.

[Montre la sauvegarde du segment]

Etape 6 : utilise ces segments dans tes campagnes. Quand tu crees un email ou une campagne, tu peux cibler un segment. "Etudiants M1-M3 non termines" — voila ton audience de relance.

[Montre la selection du segment dans la creation de campagne]

**[ECRAN — slide combinaisons utiles]**

[Tableau : combinaison de filtres, cas d'usage]

Quelques combinaisons utiles. "Enrolled + Not completed" — relance les inactifs. "Completed course A + Not enrolled course B" — upsell vers le cours suivant. "Quiz failed + Enrolled" — support personnalise pour les etudiants en difficulte. "Not enrolled in any course + Tag newsletter" — prospects pas encore convertis en etudiants.

**[TRANSITION — face camera]**

Tu sais maintenant segmenter ta base selon les donnees TutorLMS. Des segments precis, dynamiques, qui alimentent des campagnes ciblees. Dans la prochaine lecon, on automatise le cas d'usage le plus strategique : la relance des etudiants inactifs.

---

**Points cles** :
- Filtres TutorLMS dans FluentCRM : par cours, par completion, par instructeur
- Combinaison de filtres pour une segmentation fine (inscrit + pas termine = a relancer)
- Segments dynamiques : se mettent a jour automatiquement
- Utilisation directe dans les campagnes email
- 4 combinaisons cles : relance inactifs, upsell, support, conversion prospects

**Mots cles SEO** : FluentCRM segment TutorLMS, filtrer etudiants par cours, segmentation LMS email, segment dynamique FluentCRM

---

### Lecon 10.7 — Automatise la relance des etudiants inactifs

**Duree** : 8 min
**Type** : Video HeyGen
**Ecran** : Face camera pour intro/conclusion, screencast FluentCRM automation builder

---

**[INTRO — face camera]**

Un etudiant s'inscrit, suit deux lecons, puis disparait. Deux semaines sans connexion. C'est le scenario le plus courant dans les formations en ligne — et aussi la plus grosse perte de revenus. Parce qu'un etudiant inactif, c'est un etudiant qui ne terminera pas, qui ne recommandera pas, et qui n'achetera pas la suite. Dans cette lecon, on construit une automation de relance complete qui detecte l'inactivite et ramene l'etudiant dans sa formation avec un smart link de connexion automatique.

**[ECRAN — screencast FluentCRM > Automations > New]**

[Cree une nouvelle automation]

Etape 1 : la strategie. On va detecter les etudiants qui ne progressent plus depuis 14 jours. Pour ca, on combine un trigger d'inscription avec des delais et des conditions.

[Montre le schema de l'automation sur papier ou slide]

Le flux : inscription au cours → delai 14 jours → condition "a progresse ?" → si non → email de relance 1 → delai 7 jours → condition "a progresse ?" → si non → email de relance 2 → delai 7 jours → derniere tentative.

**[ECRAN — screencast construction de l'automation]**

[Commence a construire dans le builder]

Etape 2 : trigger — "Student Enrolled in a Course". Selectionne ton cours, ou "Any Course" pour couvrir toute ta base.

[Configure le trigger]

Etape 3 : ajoute un delai de 14 jours. C'est la periode de grace. On laisse l'etudiant avancer a son rythme pendant deux semaines avant de verifier.

[Ajoute le bloc Wait 14 days]

Etape 4 : ajoute un bloc conditionnel. Condition : "Has completed course X" — est-ce que l'etudiant a deja termine ? Si oui, branche Oui — on ne relance pas quelqu'un qui a fini. Remove from automation. Si non, on continue.

[Configure le conditionnel avec les deux branches]

**[ECRAN — screencast deuxieme condition et premier email]**

[Ajoute une condition plus fine]

Etape 5 : deuxieme condition sur la branche Non. On verifie la derniere activite. Si l'etudiant a complete une lecon dans les 14 derniers jours, il est encore actif — on attend. Si aucune activite, c'est un inactif confirme.

[Montre la configuration de la condition]

Note : selon ta version de FluentCRM et TutorLMS, cette condition peut etre basee sur un tag pose par une autre automation qui track la progression, ou sur un champ personnalise "last_lesson_date". L'important, c'est d'avoir un signal d'activite.

Etape 6 : premier email de relance. Ton objectif : ramener l'etudiant dans le cours sans pression. L'email doit etre court, personnel, et utile.

[Montre un email type dans l'editeur]

Objet : "Tu en etais ou dans [nom du cours] ?" Corps : rappel de ce qu'il a deja accompli, teaser de ce qui l'attend dans les prochaines lecons, et le lien de connexion direct.

**[ECRAN — screencast smart link auto-login]**

[Montre la creation du lien]

Etape 7 : le smart link. Au lieu d'envoyer un simple lien vers la page du cours, envoie un lien de connexion automatique. FluentCRM genere des liens personnalises par contact. Combine ca avec l'URL de la lecon ou l'etudiant s'est arrete — il clique, il est connecte, il reprend exactement ou il en etait. Zero friction.

[Montre l'insertion du lien dans l'email]

Format : `{{auto_login_url}}/courses/maitriser-fluentcrm/lecon-suivante/`. Le `{{auto_login_url}}` connecte l'etudiant automatiquement, et le chemin l'amene directement a la bonne lecon.

**[ECRAN — screencast sequence de relance complete]**

[Montre l'automation complete dans le builder]

Etape 8 : apres le premier email, ajoute un delai de 7 jours. Puis une condition : a-t-il progresse ? Si oui, fin de la relance. Si non, deuxieme email — cette fois avec un angle different. Par exemple : "3 etudiants sur 5 qui terminent ce module disent que c'est le declic. Tu es a [X]% de completion."

[Montre le deuxieme email avec donnees de progression]

Etape 9 : apres un nouveau delai de 7 jours, un troisieme et dernier email. Plus direct : "Ca fait un mois que tu n'as pas avance. Est-ce que tu es bloque ? Reponds a cet email et je t'aide." Apres ce troisieme email, l'automation s'arrete. Trois relances, pas plus — au-dela, c'est intrusif.

**[ECRAN — screencast ajout des tags de suivi]**

[Montre l'ajout de tags dans l'automation]

Etape 10 : ajoute des tags de suivi a chaque etape. Tag "relance-1-envoyee" apres le premier email. Tag "relance-2-envoyee" apres le deuxieme. Tag "inactif-confirme" si l'etudiant ne reagit a aucune relance. Ces tags alimentent tes rapports et tes futures segmentations.

**[TRANSITION — face camera]**

Tu as maintenant une automation de relance complete. Elle detecte l'inactivite, envoie trois emails progressifs avec des smart links, et tag les contacts pour le suivi. C'est ce type d'automation qui fait la difference entre un LMS qui perd 80% de ses etudiants et un LMS qui les accompagne jusqu'au bout. Dans la prochaine lecon, tu mets tout ca en pratique avec un exercice complet.

---

**Points cles** :
- Detecter l'inactivite apres 14 jours sans progression
- 3 emails de relance maximum, espaces de 7 jours
- Smart link auto-login pour zero friction au retour
- Tags de suivi a chaque etape (relance-1, relance-2, inactif-confirme)
- Chaque email = un angle different (rappel, social proof, aide directe)
- Toujours verifier si l'etudiant a termine avant de relancer

**Mots cles SEO** : relance etudiant inactif FluentCRM, automation retention LMS, smart link TutorLMS, email relance formation en ligne

---

### Lecon 10.8 — Exercice : Cree le funnel complet d'un parcours etudiant

**Duree** : 6 min
**Type** : Exercice
**Ecran** : Face camera pour intro et conclusion, slides pour les consignes

---

**[INTRO — face camera]**

Tu as tous les blocs. Triggers, actions, goals, conditionals, filtres, relance. Maintenant tu assembles tout dans un funnel complet — de l'inscription gratuite jusqu'a l'achat de la formation premium, en passant par le nurturing et la relance. C'est exactement le funnel qu'on utilise sur schoolsWP. A toi de le reproduire.

**[ECRAN — slide "Contexte de l'exercice"]**

Voici le scenario. Tu geres un site de formation WordPress. Tu proposes une formation gratuite en 3 modules (M1-M3) et une formation premium en 13 modules (M4-M16). Ton objectif : automatiser tout le parcours etudiant.

**[ECRAN — slide "Etape 1 — Inscription et tagging"]**

Etape 1 : cree une automation declenchee par l'inscription au cours gratuit M1-M3. A l'entree, pose le tag "free-student" et ajoute le contact a la liste "etudiants-actifs". Envoie un email de bienvenue avec le lien d'acces au premier module.

**[ECRAN — slide "Etape 2 — Nurturing pendant la formation"]**

Etape 2 : dans la meme automation ou dans une automation separee, envoie une sequence de 3 emails de valeur espaces de 5 jours. Email 1 — une astuce avancee liee au module 1. Email 2 — un temoignage d'un etudiant qui a termine. Email 3 — un apercu de ce que contient la formation premium.

**[ECRAN — slide "Etape 3 — Goal completion et upsell"]**

Etape 3 : ajoute un goal "Course Completed" sur M1-M3, en mode optionnel. Apres le goal, ajoute un conditionnel. Branche "A termine" : lance la sequence de vente premium (3 emails sur 10 jours). Branche "N'a pas termine" : email d'encouragement puis delai de 7 jours avant la sequence de vente.

**[ECRAN — slide "Etape 4 — Achat et enroll automatique"]**

Etape 4 : cree une deuxieme automation. Trigger : tag "a-achete-premium" applique. Actions : enroll dans le cours premium M4-M16, apply tag "premium-student", remove tag "free-student", envoyer l'email de bienvenue premium avec les liens d'acces.

**[ECRAN — slide "Etape 5 — Relance inactifs"]**

Etape 5 : cree une troisieme automation de relance. Trigger : inscription a n'importe quel cours. Delai 14 jours. Condition : a progresse ? Si non, sequence de 3 emails de relance avec smart links (voir lecon 10.7).

**[ECRAN — slide "Criteres de reussite"]**

[Checklist]

Ton funnel est complet si tu coches ces 6 criteres. Un : l'inscription gratuite pose le tag "free-student" et envoie un email de bienvenue. Deux : le nurturing envoie 3 emails de valeur pendant la formation. Trois : le goal "Course Completed" detecte la fin du cours gratuit. Quatre : la sequence de vente se declenche au bon moment. Cinq : l'achat enroll automatiquement dans le cours premium. Six : les inactifs sont relances apres 14 jours.

**[TRANSITION — face camera]**

Prends 30 a 45 minutes pour construire ce funnel dans ton FluentCRM. Si tu bloques, reviens sur les lecons 10.3 a 10.7 — chaque piece du puzzle y est detaillee. Une fois ton funnel en place, termine ce module avec le quiz pour valider tes acquis.

---

**Points cles** :
- Funnel complet en 3 automations : inscription/nurturing, achat/enroll, relance inactifs
- Tags cles : "free-student", "premium-student", "a-achete-premium"
- Goal optionnel pour detecter la completion sans bloquer le flux
- Conditionnel pour personnaliser l'upsell selon la progression
- 6 criteres de reussite a cocher

---

### Lecon 10.9 — Quiz : Valide tes acquis M10

**Duree** : 5 min
**Type** : Quiz (8 QCM)
**Ecran** : Face camera pour intro et conclusion, slides pour les questions

---

**[INTRO — face camera]**

Dernier checkpoint du module 10. 8 questions pour verifier que tu maitrises l'integration TutorLMS + FluentCRM. Triggers, actions, goals, segments, relance — tout y passe. Rappel : 75% minimum pour valider.

---

**Question 1** : Ou active-t-on l'integration TutorLMS dans FluentCRM ?

- A) FluentCRM > Automations > Settings
- B) FluentCRM > Settings > Integrations
- C) WordPress > Settings > Integrations
- D) TutorLMS > Settings > FluentCRM

**Reponse** : B — FluentCRM > Settings > Integrations. C'est la qu'on active le toggle TutorLMS.

---

**Question 2** : Quels triggers TutorLMS sont disponibles dans FluentCRM ? (Plusieurs reponses possibles)

- A) Student Enrolled in a Course
- B) Course Completed
- C) Student Logged In
- D) Quiz Passed
- E) Lesson Completed

**Reponse** : A, B, D, E — Les quatre triggers natifs. "Student Logged In" n'est pas un trigger TutorLMS dans FluentCRM.

---

**Question 3** : Tu veux inscrire automatiquement un etudiant a 3 cours apres son achat. Comment fais-tu ?

- A) Une seule action Enroll avec les 3 cours selectionnes
- B) Trois actions Enroll successives, une par cours
- C) Un webhook vers TutorLMS
- D) Un import CSV

**Reponse** : B — Une action Enroll = un cours. Pour plusieurs cours, on enchaine les actions.

---

**Question 4** : Un etudiant est dans ton funnel de nurturing. Il termine le cours gratuit apres le deuxieme email. Que se passe-t-il si tu as un goal optionnel "Course Completed" ?

- A) Il continue a recevoir les emails de nurturing normalement
- B) Il saute directement au goal et entre dans la sequence de vente
- C) Il est retire de l'automation
- D) Il recoit tous les emails restants puis le goal s'active

**Reponse** : B — Le goal optionnel detecte la completion et fait sauter le contact directement a ce point.

---

**Question 5** : Tu veux segmenter les etudiants inscrits au cours FluentCRM qui ne l'ont pas encore termine. Quelle combinaison de filtres utilises-tu ?

- A) Tag "student" + liste "actifs"
- B) Enrolled in Course "FluentCRM" + Course "FluentCRM" not completed
- C) Tag "enrolled-fluentcrm" uniquement
- D) Enrolled in any course + No tag

**Reponse** : B — La combinaison de deux filtres TutorLMS donne le segment precis des etudiants en cours.

---

**Question 6** : Apres combien de jours d'inactivite lance-t-on la premiere relance dans l'automation de la lecon 10.7 ?

- A) 7 jours
- B) 14 jours
- C) 21 jours
- D) 30 jours

**Reponse** : B — 14 jours. C'est la periode de grace avant la premiere verification.

---

**Question 7** : Quel est l'avantage du smart link auto-login dans les emails de relance ?

- A) Il permet de tracker les ouvertures d'email
- B) Il connecte l'etudiant automatiquement et l'amene a sa lecon en cours
- C) Il cree un nouveau compte pour l'etudiant
- D) Il desactive le mot de passe de l'etudiant

**Reponse** : B — Zero friction : un clic, l'etudiant est connecte et reprend exactement ou il en etait.

---

**Question 8** : Dans le funnel complet schoolsWP, que se passe-t-il quand un contact recoit le tag "a-achete-premium" ?

- A) Il est ajoute a une liste d'attente
- B) Il recoit un email de vente supplementaire
- C) FluentCRM l'inscrit au cours premium, pose le tag "premium-student" et retire le tag "free-student"
- D) Il est retire de toutes les automations

**Reponse** : C — L'automation d'achat enchaine enroll + tag "premium-student" + remove tag "free-student" + email de bienvenue.

---

**[TRANSITION — face camera]**

Module 10 termine. Tu sais maintenant connecter TutorLMS et FluentCRM, automatiser les inscriptions, segmenter par progression, et relancer les inactifs. C'est la combinaison qui transforme un simple LMS en machine de retention. Dans le module suivant, on passe a un autre sujet. Mais ce que tu as construit ici — le funnel etudiant complet — c'est une base que tu peux dupliquer pour chaque nouvelle formation que tu lances.

---

**Points cles du quiz** :
- 8 questions couvrant les lecons 10.1 a 10.7
- Seuil de validation : 75% (6/8)
- Questions sur : activation integration, triggers, actions, goals, filtres, relance, smart links, funnel complet
