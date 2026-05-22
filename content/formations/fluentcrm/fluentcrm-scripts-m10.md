# Scripts vidéo — Module 10 : TutorLMS + FluentCRM

**Formation** : Maîtriser FluentCRM
**Module** : M10 — TutorLMS + FluentCRM (Premium)
**Leçons** : 7 vidéos + 1 exercice + 1 quiz
**Durée totale** : ~55 min
**Prérequis** : M6 (automations de base), M7 (automation avancée — goals, conditionals)
**Date** : 2026-03-23

---

### Leçon 10.1 — Active l'intégration TutorLMS dans FluentCRM

**Durée** : 5 min
**Type** : Vidéo HeyGen
**Écran** : Face caméra pour intro/conclusion, screencast FluentCRM et TutorLMS

---

**[INTRO — face caméra]**

Tu as FluentCRM pour le marketing. Tu as TutorLMS pour tes formations. Mais sans intégration entre les deux, ce sont deux mondes séparés. Tes étudiants ne reçoivent pas les bons emails. Tes automations ne savent pas qui est inscrit à quoi. Et tu fais tout manuellement. Cette leçon connecte les deux. Une activation, quelques réglages, et FluentCRM voit tout ce qui se passe dans TutorLMS — inscriptions, completions, quiz. C'est le duo que personne ne montre. On va corriger ça.

**[ÉCRAN — screencast FluentCRM > Settings > Integrations]**

[Navigation vers FluentCRM > Settings > Integrations]

Étape 1 : va dans FluentCRM, puis Settings, puis l'onglet Integrations. Tu vois la liste des plugins compatibles. Cherche TutorLMS. Si TutorLMS est installé et actif sur ton WordPress, tu verras un toggle pour activer l'intégration.

[Montre le toggle TutorLMS dans la liste]

Étape 2 : active le toggle. FluentCRM va scanner tes cours TutorLMS et rendre disponibles les triggers, actions et filtres spécifiques. Sans cette activation, les blocs TutorLMS n'apparaissent pas dans le builder d'automation.

**[ÉCRAN — screencast vérification post-activation]**

[Va dans Automations > Nouveau trigger]

Étape 3 : vérifie que l'intégration fonctionne. Crée une nouvelle automation. Dans la liste des triggers, tu devrais maintenant voir une catégorie "TutorLMS" avec plusieurs déclencheurs : Student enrolled in a course, Course completed, Lesson completed, Quiz passed, Quiz failed. Si tu vois ces options, l'intégration est active.

[Montre la liste des triggers TutorLMS]

Étape 4 : vérifie aussi les actions. Dans le builder, ajoute une action. Tu devrais voir "Enroll student in a course" et "Remove from course" dans les options TutorLMS.

[Montre les actions TutorLMS dans le builder]

**[ÉCRAN — screencast FluentCRM > Settings > TutorLMS]**

[Montre les options de configuration spécifiques]

Étape 5 : retourne dans Settings > Integrations > TutorLMS. Tu as quelques options supplémentaires. La plus importante : la synchronisation automatique. Quand un étudiant s'inscrit à un cours via TutorLMS, FluentCRM peut automatiquement créer ou mettre à jour le contact correspondant. Active cette option. Sans elle, tu devras importer manuellement — ce qu'on voit dans la prochaine leçon.

**[TRANSITION — face caméra]**

L'intégration est active. FluentCRM voit maintenant tout ce qui se passe dans TutorLMS. Dans la prochaine leçon, on importe les étudiants qui existaient déjà avant l'activation — pour que ta base soit complète dès le départ.

---

**Points clés** :
- Activation dans FluentCRM > Settings > Integrations > TutorLMS
- TutorLMS doit être installé et actif pour que le toggle apparaisse
- L'activation débloque les triggers (enrolled, completed, quiz) et les actions (enroll, remove)
- Activer la synchronisation automatique pour les nouvelles inscriptions
- Sans activation, les blocs TutorLMS sont invisibles dans le builder

**Mots clés SEO** : FluentCRM TutorLMS intégration, connecter TutorLMS FluentCRM, automation LMS WordPress, FluentCRM settings integration

---

### Leçon 10.2 — Importe tes étudiants TutorLMS existants

**Durée** : 5 min
**Type** : Vidéo HeyGen
**Écran** : Face caméra pour intro/conclusion, screencast FluentCRM import

---

**[INTRO — face caméra]**

Tu viens d'activer l'intégration. Les nouveaux étudiants seront synchronisés automatiquement. Mais ceux qui étaient déjà inscrits avant ? Ils existent dans TutorLMS mais pas forcément dans FluentCRM — ou ils y sont sans les bonnes infos. Dans cette leçon, on importe les étudiants existants et on les tag correctement pour que tes automations fonctionnent sur toute ta base.

**[ÉCRAN — screencast FluentCRM > Contacts > Import]**

[Navigation vers FluentCRM > Contacts > Import]

Étape 1 : va dans FluentCRM > Contacts > Import. Tu as plusieurs méthodes d'import. Celle qui nous intéresse : "Import from TutorLMS" ou, si cette option n'apparaît pas, "Import from WordPress Users" avec un filtre par rôle.

[Montre les options d'import]

Étape 2 : si tu as l'option directe TutorLMS, utilise-la. FluentCRM va lister tous les utilisateurs WordPress qui ont au moins une inscription TutorLMS. Sélectionne-les tous ou filtre par cours.

[Montre la liste des étudiants à importer]

**[ÉCRAN — screencast mapping et tags]**

[Montre l'écran de configuration de l'import]

Étape 3 : configure le mapping. Le prénom, le nom et l'email sont mappés automatiquement. L'important, c'est ce que tu ajoutes. Assigne une liste — par exemple "etudiants-tutorlms" — et un tag de base — "student".

[Montre l'ajout de liste et tag]

Étape 4 : pour les tags par cours, tu as deux approches. L'approche manuelle : tu importes cours par cours et tu assignes un tag spécifique à chaque import. Par exemple, tu importes les inscrits à "Maîtriser FluentCRM" avec le tag "enrolled-fluentcrm". Puis les inscrits à "Créer son LMS" avec le tag "enrolled-lms".

[Montre un import filtré par cours avec tag spécifique]

L'approche automatique : tu importes tout le monde avec le tag générique "student", puis tu crées une automation qui pose les tags spécifiques selon les cours. On verra cette approche dans la leçon 10.3 avec les triggers.

**[ÉCRAN — screencast lancement de l'import]**

[Lance l'import et montre la progression]

Étape 5 : lance l'import. FluentCRM traite les contacts par lots. Les contacts existants sont mis à jour — ils ne sont pas dupliqués. Les nouveaux contacts sont créés. À la fin, tu as un rapport : X contacts créés, Y contacts mis à jour, Z ignorés.

[Montre le rapport d'import]

Étape 6 : vérifie le résultat. Va dans Contacts, filtre par la liste "etudiants-tutorlms". Tous tes étudiants doivent apparaître avec les bons tags.

**[TRANSITION — face caméra]**

Ta base est complète. Étudiants existants importés et taggés, nouveaux étudiants synchronisés automatiquement. Maintenant on passe aux triggers TutorLMS — les événements qui vont déclencher tes automations.

---

**Points clés** :
- Import via FluentCRM > Contacts > Import (option TutorLMS ou WordPress Users)
- Toujours assigner une liste et un tag de base à l'import
- Deux approches pour les tags par cours : import séparé par cours ou automation post-import
- Les contacts existants sont mis à jour, pas dupliqués
- Vérifier le rapport d'import et filtrer pour confirmer

**Mots clés SEO** : importer étudiants TutorLMS FluentCRM, synchroniser contacts LMS, import FluentCRM WordPress users, migration TutorLMS

---

### Leçon 10.3 — Triggers TutorLMS : enrollment, completion, quiz passed

**Durée** : 7 min
**Type** : Vidéo HeyGen
**Écran** : Face caméra pour intro/conclusion, screencast FluentCRM automation builder

---

**[INTRO — face caméra]**

Un étudiant s'inscrit à un cours. Un autre termine une leçon. Un troisième rate un quiz. Trois événements, trois réactions différentes à automatiser. Les triggers TutorLMS dans FluentCRM détectent ces événements et déclenchent tes automations automatiquement. Dans cette leçon, on configure les cinq triggers principaux avec des cas concrets tirés de la formation schoolsWP.

**[ÉCRAN — screencast FluentCRM > Automations > New]**

[Crée une nouvelle automation, montre la liste des triggers]

Étape 1 : crée une nouvelle automation. À l'étape de sélection du trigger, cherche la catégorie TutorLMS. Tu as cinq triggers disponibles.

[Montre les 5 triggers TutorLMS]

Trigger 1 : "Student Enrolled in a Course". Se déclenche quand un étudiant s'inscrit à un cours — que ce soit une inscription gratuite, un achat, ou un enroll manuel. Tu choisis le cours concerné ou "Any Course" pour tous les cours.

**[ÉCRAN — screencast configuration trigger Enrolled]**

[Configure le trigger Enrolled avec un cours spécifique]

Étape 2 : cas concret. Sur schoolsWP, quand un étudiant s'inscrit aux modules gratuits M1-M3, on veut poser le tag "free-student" et démarrer une séquence de nurturing. Sélectionne le cours "Maîtriser FluentCRM — Modules 1-3", et dans la suite de l'automation, ajoute l'action "Apply Tag > free-student".

[Montre la configuration complète : trigger enrolled + action apply tag]

**[ÉCRAN — screencast trigger Course Completed]**

[Sélectionne le trigger Course Completed]

Trigger 2 : "Course Completed". Se déclenche quand un étudiant termine toutes les leçons et tous les quiz d'un cours. C'est le trigger le plus stratégique pour le marketing — l'étudiant a fini, il est prêt pour la suite.

[Configure avec le cours gratuit M1-M3]

Étape 3 : cas concret. Quand un étudiant termine les modules gratuits, c'est le moment de proposer la formation premium. Le trigger "Course Completed" sur M1-M3 déclenche une séquence de vente vers les modules M4-M16.

**[ÉCRAN — screencast trigger Lesson Completed]**

[Sélectionne le trigger Lesson Completed]

Trigger 3 : "Lesson Completed". Plus granulaire — se déclenche à chaque leçon terminée. Utile pour le suivi de progression, mais attention : si ton cours a 30 leçons, ce trigger se déclenchera 30 fois par étudiant. Utilise-le avec des conditions pour éviter le bruit.

[Montre la sélection d'une leçon spécifique]

Étape 4 : cas concret. Tu veux envoyer un email de félicitation quand un étudiant termine la leçon 3.6 "Crée ta première automation" — un milestone important. Configure le trigger sur cette leçon spécifique, pas sur "Any Lesson".

**[ÉCRAN — screencast triggers Quiz]**

[Montre les deux triggers quiz]

Trigger 4 : "Quiz Passed". Se déclenche quand un étudiant réussit un quiz avec le score minimum requis.

Trigger 5 : "Quiz Failed". Se déclenche quand un étudiant échoue. C'est celui que la plupart des gens oublient — et c'est pourtant le plus utile pour la rétention.

[Configure le trigger Quiz Failed]

Étape 5 : cas concret. Un étudiant échoue au quiz du module 6. Tu déclenches un email automatique : "Tu n'as pas obtenu le score minimum sur le quiz M6. Voici les leçons à revoir avant de retenter." Tu ajoutes les liens directs vers les leçons concernées. C'est de l'accompagnement automatisé — pas du spam.

**[ÉCRAN — slide récapitulatif des 5 triggers]**

[Tableau : trigger, événement, cas d'usage]

Récapitulatif rapide. Enrolled — inscription à un cours — tagging et welcome sequence. Course Completed — cours terminé — upsell et certification. Lesson Completed — leçon terminée — suivi de progression et milestones. Quiz Passed — quiz réussi — félicitation et déblocage. Quiz Failed — quiz raté — relance et support.

**[TRANSITION — face caméra]**

Tu connais les cinq triggers TutorLMS. Chacun détecte un moment précis du parcours étudiant. Dans la prochaine leçon, on passe de l'autre côté — les actions. Tu vas pouvoir inscrire et désinscrire des étudiants de cours directement depuis tes automations FluentCRM.

---

**Points clés** :
- 5 triggers TutorLMS : Enrolled, Course Completed, Lesson Completed, Quiz Passed, Quiz Failed
- Chaque trigger peut cibler un cours/leçon/quiz spécifique ou "Any"
- Lesson Completed se déclenche à chaque leçon — utiliser avec conditions pour éviter le bruit
- Quiz Failed = trigger sous-utilisé mais stratégique pour la rétention
- Cas schoolsWP : inscription gratuite M1-M3 → tag "free-student" → nurturing → upsell M4-M16

**Mots clés SEO** : FluentCRM TutorLMS trigger, automation inscription cours, trigger quiz FluentCRM, automatiser LMS WordPress

---

### Leçon 10.4 — Actions TutorLMS : enroll in course, remove from course

**Durée** : 6 min
**Type** : Vidéo HeyGen
**Écran** : Face caméra pour intro/conclusion, screencast FluentCRM automation builder

---

**[INTRO — face caméra]**

Dans la leçon précédente, TutorLMS déclenchait des automations dans FluentCRM. Maintenant on fait l'inverse : FluentCRM agit sur TutorLMS. Un contact achète ta formation premium ? FluentCRM l'inscrit automatiquement aux modules M4 à M16 sans que tu lèves le petit doigt. Un remboursement ? FluentCRM retire l'accès. Deux actions, énormément de temps gagné.

**[ÉCRAN — screencast FluentCRM > Automation builder]**

[Ouvre une automation existante, montre les actions disponibles]

Étape 1 : dans le builder d'automation, ajoute une action. Dans la liste, tu trouves deux actions TutorLMS. "Enroll Student in a Course" — inscrit le contact à un cours. "Remove from Course" — retire l'accès.

[Montre les deux actions dans la liste]

**[ÉCRAN — screencast action Enroll]**

[Ajoute l'action Enroll et configure-la]

Étape 2 : configure l'action Enroll. Tu sélectionnes le cours cible. Un cours par action. Si tu veux inscrire à plusieurs cours, tu enchaînes plusieurs actions Enroll.

[Montre la sélection du cours]

Étape 3 : cas concret — le funnel schoolsWP. L'automation démarre quand un contact reçoit le tag "a-achete-premium" (posé par WooCommerce après l'achat). L'action Enroll inscrit l'étudiant au cours "Maîtriser FluentCRM — Modules 4-16".

[Montre l'automation complète : trigger tag applied > enroll course]

Mais on ne s'arrête pas là. Après l'enroll, on ajoute trois actions supplémentaires. Apply tag "premium-student". Remove tag "free-student" — il n'est plus en version gratuite. Et un email de bienvenue avec les liens d'accès directs.

[Montre la séquence complète : enroll > apply tag > remove tag > send email]

**[ÉCRAN — screencast action Remove from Course]**

[Ajoute l'action Remove et configure-la]

Étape 4 : l'action Remove from Course. Même logique — tu sélectionnes le cours concerné.

Étape 5 : cas concret. Un étudiant demande un remboursement. Ton plugin e-commerce pose le tag "refunded". L'automation détecte ce tag, retire l'accès au cours premium, et envoie un email de confirmation de remboursement.

[Montre l'automation : trigger tag "refunded" > remove from course > send email]

**[ÉCRAN — screencast enchaînement multi-cours]**

[Montre une automation avec plusieurs Enroll]

Étape 6 : pour inscrire à plusieurs cours dans la même automation, enchaîne les actions. Attention à l'ordre — TutorLMS traite chaque inscription séquentiellement. Si tu as beaucoup de cours, ajoute un délai de quelques secondes entre chaque Enroll pour éviter de surcharger le serveur.

[Montre trois actions Enroll avec des délais de 5 secondes entre chaque]

**[TRANSITION — face caméra]**

Tu contrôles maintenant l'accès aux cours depuis tes automations. Inscription automatique à l'achat, retrait à la désinscription. Dans la prochaine leçon, on combine triggers et actions avec les goals et les conditionals — pour créer des parcours étudiants vraiment intelligents.

---

**Points clés** :
- 2 actions TutorLMS : Enroll Student in a Course, Remove from Course
- Une action = un cours. Pour plusieurs cours, enchaîner les actions
- Cas principal : achat → tag "a-achete-premium" → enroll automatique + tag "premium-student"
- Remboursement : tag "refunded" → remove from course + email confirmation
- Pour multi-enroll : ajouter quelques secondes de délai entre chaque action

**Mots clés SEO** : FluentCRM enroll course TutorLMS, inscrire étudiant automatiquement, automation achat formation, FluentCRM action TutorLMS

---

### Leçon 10.5 — Goals et conditionals spécifiques TutorLMS

**Durée** : 7 min
**Type** : Vidéo HeyGen
**Écran** : Face caméra pour intro/conclusion, screencast FluentCRM automation builder

---

**[INTRO — face caméra]**

Tu as vu les goals dans le module 7. Maintenant on les utilise avec TutorLMS. Un goal "a terminé le cours X" dans une séquence de nurturing. Un conditional "est inscrit au cours Y" pour personnaliser les emails. C'est là que l'intégration devient vraiment puissante — tes automations réagissent en temps réel à la progression de chaque étudiant.

**[ÉCRAN — screencast FluentCRM > Automation builder]**

[Ouvre une automation de nurturing post-inscription gratuite]

Étape 1 : contexte. On reprend le funnel schoolsWP. Un étudiant s'inscrit aux modules gratuits M1-M3. Il entre dans une automation de nurturing qui envoie des emails de valeur et propose la formation premium. Le problème : combien de temps dure ce nurturing ?

[Montre la séquence d'emails de nurturing]

Étape 2 : ajoute un goal "Course Completed" sur le cours M1-M3. Place-le dans l'automation. Ce goal détecte quand l'étudiant a terminé les modules gratuits.

[Place le bloc Goal dans l'automation]

**[ÉCRAN — screencast configuration du Goal TutorLMS]**

[Configure le goal avec la condition Course Completed]

Étape 3 : configure le goal. Condition : le contact a terminé le cours "Maîtriser FluentCRM — Modules 1-3". Mode : goal optionnel — "Can be achieved at any time". Pourquoi optionnel ? Parce que si l'étudiant ne finit pas le cours, tu veux quand même qu'il reçoive les emails suivants.

[Montre les paramètres du goal]

Étape 4 : place le goal juste avant ta séquence de vente. Voilà ce qui se passe. L'étudiant reçoit les emails de nurturing. À n'importe quel moment, s'il termine le cours M1-M3, il saute directement au goal. Après le goal, tu places ta séquence de vente — "Tu as fini les bases, voici ce que la formation complète t'apporte." Le timing est parfait : l'email de vente arrive au moment où l'étudiant est le plus engagé.

**[ÉCRAN — screencast conditionals TutorLMS]**

[Ajoute un bloc conditionnel dans l'automation]

Étape 5 : les conditionals. Ajoute un bloc "Conditional" dans ton automation. Dans les conditions disponibles, tu trouves des filtres TutorLMS. "Is enrolled in course X" — vérifie si le contact est inscrit à un cours. "Has completed course X" — vérifie si le cours est terminé.

[Montre les conditions TutorLMS dans le bloc conditionnel]

Étape 6 : cas concret. Après le goal, tu veux personnaliser l'email de vente. Condition : "Has completed course M1-M3". Branche Oui : email de vente avec angle "Tu as déjà vu la puissance de FluentCRM, imagine ce que tu feras avec les modules avancés." Branche Non : email avec angle "Tu n'as pas encore exploré tous les modules gratuits — termine-les d'abord, puis on en reparle."

[Montre les deux branches avec des emails différents]

**[ÉCRAN — screencast goal essentiel pour prérequis]**

[Crée une nouvelle automation avec un goal essentiel]

Étape 7 : deuxième cas — le goal essentiel. Tu as un parcours où l'étudiant doit terminer le module 6 (automations de base) avant d'accéder au module 7 (automation avancée). Le goal "Course Completed > Module 6" est en mode essentiel — "Must be achieved to proceed". L'étudiant ne reçoit pas les emails du module 7 tant qu'il n'a pas terminé le module 6.

[Montre la configuration en mode essentiel]

**[TRANSITION — face caméra]**

Goals et conditionals transforment tes automations en parcours adaptatifs. Chaque étudiant avance à son rythme, reçoit le bon message au bon moment. Dans la prochaine leçon, on va encore plus loin avec les filtres avancés — segmentation par cours, progression et instructeur.

---

**Points clés** :
- Goal "Course Completed" = détecte la fin d'un cours dans l'automation
- Goal optionnel pour le nurturing (le contact continue même sans finir le cours)
- Goal essentiel pour les prérequis (le contact est bloqué tant que le cours n'est pas terminé)
- Conditionals TutorLMS : "Is enrolled in course X", "Has completed course X"
- Personnalisation des emails selon la progression réelle de l'étudiant

**Mots clés SEO** : FluentCRM goal TutorLMS, conditional automation LMS, personnaliser email progression cours, funnel étudiant FluentCRM

---

### Leçon 10.6 — Filtre avancé : segmente par cours, progression, instructeur

**Durée** : 6 min
**Type** : Vidéo HeyGen
**Écran** : Face caméra pour intro/conclusion, screencast FluentCRM contacts et segments

---

**[INTRO — face caméra]**

Tu as 500 contacts dans FluentCRM. Parmi eux, des étudiants inscrits à différents cours, à différents stades de progression. Tu veux envoyer un email uniquement aux étudiants inscrits au cours FluentCRM qui n'ont pas encore terminé le module 3. Les filtres avancés TutorLMS dans FluentCRM te permettent ce niveau de précision. Dans cette leçon, on construit des segments dynamiques basés sur les données TutorLMS.

**[ÉCRAN — screencast FluentCRM > Contacts > Filtres]**

[Ouvre la vue contacts et montre les filtres disponibles]

Étape 1 : va dans FluentCRM > Contacts. Clique sur "Filter". Dans les filtres disponibles, tu trouves une section TutorLMS avec plusieurs critères.

[Montre les filtres TutorLMS]

Filtre 1 : "Enrolled in Course". Sélectionne un cours et FluentCRM affiche uniquement les contacts inscrits à ce cours. Tu peux combiner avec "Is" ou "Is not" — pour cibler les inscrits ou les non-inscrits.

[Applique le filtre et montre les résultats]

**[ÉCRAN — screencast filtre par progression]**

[Ajoute un filtre de progression]

Étape 2 : filtre par progression. "Course Completed" — filtre les contacts qui ont terminé ou pas un cours spécifique. Combine les deux : "Enrolled in Course X" ET "Course not completed" — tu obtiens les étudiants en cours de formation, ceux qui ont commencé mais pas fini.

[Montre la combinaison de filtres]

Étape 3 : cas concret. Tu veux relancer les étudiants qui se sont inscrits aux modules gratuits mais ne les ont pas terminés. Filtre : "Enrolled in M1-M3" + "Course M1-M3 not completed". Résultat : ta liste de contacts à relancer.

[Montre le résultat filtré]

**[ÉCRAN — screencast filtre par instructeur]**

[Montre le filtre instructeur si disponible]

Étape 4 : filtre par instructeur. Si tu as plusieurs instructeurs sur ton LMS, tu peux filtrer les étudiants d'un instructeur spécifique. Utile pour les écoles avec plusieurs formateurs — chaque instructeur peut avoir ses propres séquences email.

**[ÉCRAN — screencast création de segments dynamiques]**

[Sauvegarde un filtre comme segment]

Étape 5 : transforme ton filtre en segment dynamique. Une fois tes critères définis, sauvegarde le filtre. Ce segment se met à jour automatiquement — chaque nouveau contact qui correspond aux critères y entre, chaque contact qui ne correspond plus en sort.

[Montre la sauvegarde du segment]

Étape 6 : utilise ces segments dans tes campagnes. Quand tu crées un email ou une campagne, tu peux cibler un segment. "Étudiants M1-M3 non terminés" — voilà ton audience de relance.

[Montre la sélection du segment dans la création de campagne]

**[ÉCRAN — slide combinaisons utiles]**

[Tableau : combinaison de filtres, cas d'usage]

Quelques combinaisons utiles. "Enrolled + Not completed" — relance les inactifs. "Completed course A + Not enrolled course B" — upsell vers le cours suivant. "Quiz failed + Enrolled" — support personnalisé pour les étudiants en difficulté. "Not enrolled in any course + Tag newsletter" — prospects pas encore convertis en étudiants.

**[TRANSITION — face caméra]**

Tu sais maintenant segmenter ta base selon les données TutorLMS. Des segments précis, dynamiques, qui alimentent des campagnes ciblées. Dans la prochaine leçon, on automatise le cas d'usage le plus stratégique : la relance des étudiants inactifs.

---

**Points clés** :
- Filtres TutorLMS dans FluentCRM : par cours, par complétion, par instructeur
- Combinaison de filtres pour une segmentation fine (inscrit + pas terminé = à relancer)
- Segments dynamiques : se mettent à jour automatiquement
- Utilisation directe dans les campagnes email
- 4 combinaisons clés : relance inactifs, upsell, support, conversion prospects

**Mots clés SEO** : FluentCRM segment TutorLMS, filtrer étudiants par cours, segmentation LMS email, segment dynamique FluentCRM

---

### Leçon 10.7 — Automatise la relance des étudiants inactifs

**Durée** : 8 min
**Type** : Vidéo HeyGen
**Écran** : Face caméra pour intro/conclusion, screencast FluentCRM automation builder

---

**[INTRO — face caméra]**

Un étudiant s'inscrit, suit deux leçons, puis disparaît. Deux semaines sans connexion. C'est le scénario le plus courant dans les formations en ligne — et aussi la plus grosse perte de revenus. Parce qu'un étudiant inactif, c'est un étudiant qui ne terminera pas, qui ne recommandera pas, et qui n'achètera pas la suite. Dans cette leçon, on construit une automation de relance complète qui détecte l'inactivité et ramène l'étudiant dans sa formation avec un smart link de connexion automatique.

**[ÉCRAN — screencast FluentCRM > Automations > New]**

[Crée une nouvelle automation]

Étape 1 : la stratégie. On va détecter les étudiants qui ne progressent plus depuis 14 jours. Pour ça, on combine un trigger d'inscription avec des délais et des conditions.

[Montre le schéma de l'automation sur papier ou slide]

Le flux : inscription au cours → délai 14 jours → condition "a progressé ?" → si non → email de relance 1 → délai 7 jours → condition "a progressé ?" → si non → email de relance 2 → délai 7 jours → dernière tentative.

**[ÉCRAN — screencast construction de l'automation]**

[Commence à construire dans le builder]

Étape 2 : trigger — "Student Enrolled in a Course". Sélectionne ton cours, ou "Any Course" pour couvrir toute ta base.

[Configure le trigger]

Étape 3 : ajoute un délai de 14 jours. C'est la période de grâce. On laisse l'étudiant avancer à son rythme pendant deux semaines avant de vérifier.

[Ajoute le bloc Wait 14 days]

Étape 4 : ajoute un bloc conditionnel. Condition : "Has completed course X" — est-ce que l'étudiant a déjà terminé ? Si oui, branche Oui — on ne relance pas quelqu'un qui a fini. Remove from automation. Si non, on continue.

[Configure le conditionnel avec les deux branches]

**[ÉCRAN — screencast deuxième condition et premier email]**

[Ajoute une condition plus fine]

Étape 5 : deuxième condition sur la branche Non. On vérifie la dernière activité. Si l'étudiant a complété une leçon dans les 14 derniers jours, il est encore actif — on attend. Si aucune activité, c'est un inactif confirmé.

[Montre la configuration de la condition]

Note : selon ta version de FluentCRM et TutorLMS, cette condition peut être basée sur un tag posé par une autre automation qui track la progression, ou sur un champ personnalisé "last_lesson_date". L'important, c'est d'avoir un signal d'activité.

Étape 6 : premier email de relance. Ton objectif : ramener l'étudiant dans le cours sans pression. L'email doit être court, personnel, et utile.

[Montre un email type dans l'éditeur]

Objet : "Tu en étais où dans [nom du cours] ?" Corps : rappel de ce qu'il a déjà accompli, teaser de ce qui l'attend dans les prochaines leçons, et le lien de connexion direct.

**[ÉCRAN — screencast smart link auto-login]**

[Montre la création du lien]

Étape 7 : le smart link. Au lieu d'envoyer un simple lien vers la page du cours, envoie un lien de connexion automatique. FluentCRM génère des liens personnalisés par contact. Combine ça avec l'URL de la leçon où l'étudiant s'est arrêté — il clique, il est connecté, il reprend exactement où il en était. Zéro friction.

[Montre l'insertion du lien dans l'email]

Format : `{{auto_login_url}}/courses/maitriser-fluentcrm/lecon-suivante/`. Le `{{auto_login_url}}` connecte l'étudiant automatiquement, et le chemin l'amène directement à la bonne leçon.

**[ÉCRAN — screencast séquence de relance complète]**

[Montre l'automation complète dans le builder]

Étape 8 : après le premier email, ajoute un délai de 7 jours. Puis une condition : a-t-il progressé ? Si oui, fin de la relance. Si non, deuxième email — cette fois avec un angle différent. Par exemple : "3 étudiants sur 5 qui terminent ce module disent que c'est le déclic. Tu es à [X]% de complétion."

[Montre le deuxième email avec données de progression]

Étape 9 : après un nouveau délai de 7 jours, un troisième et dernier email. Plus direct : "Ça fait un mois que tu n'as pas avancé. Est-ce que tu es bloqué ? Réponds à cet email et je t'aide." Après ce troisième email, l'automation s'arrête. Trois relances, pas plus — au-delà, c'est intrusif.

**[ÉCRAN — screencast ajout des tags de suivi]**

[Montre l'ajout de tags dans l'automation]

Étape 10 : ajoute des tags de suivi à chaque étape. Tag "relance-1-envoyee" après le premier email. Tag "relance-2-envoyee" après le deuxième. Tag "inactif-confirme" si l'étudiant ne réagit à aucune relance. Ces tags alimentent tes rapports et tes futures segmentations.

**[TRANSITION — face caméra]**

Tu as maintenant une automation de relance complète. Elle détecte l'inactivité, envoie trois emails progressifs avec des smart links, et tag les contacts pour le suivi. C'est ce type d'automation qui fait la différence entre un LMS qui perd 80% de ses étudiants et un LMS qui les accompagne jusqu'au bout. Dans la prochaine leçon, tu mets tout ça en pratique avec un exercice complet.

---

**Points clés** :
- Détecter l'inactivité après 14 jours sans progression
- 3 emails de relance maximum, espacés de 7 jours
- Smart link auto-login pour zéro friction au retour
- Tags de suivi à chaque étape (relance-1, relance-2, inactif-confirme)
- Chaque email = un angle différent (rappel, social proof, aide directe)
- Toujours vérifier si l'étudiant a terminé avant de relancer

**Mots clés SEO** : relance étudiant inactif FluentCRM, automation rétention LMS, smart link TutorLMS, email relance formation en ligne

---

### Leçon 10.8 — Exercice : Crée le funnel complet d'un parcours étudiant

**Durée** : 6 min
**Type** : Exercice
**Écran** : Face caméra pour intro et conclusion, slides pour les consignes

---

**[INTRO — face caméra]**

Tu as tous les blocs. Triggers, actions, goals, conditionals, filtres, relance. Maintenant tu assembles tout dans un funnel complet — de l'inscription gratuite jusqu'à l'achat de la formation premium, en passant par le nurturing et la relance. C'est exactement le funnel qu'on utilise sur schoolsWP. À toi de le reproduire.

**[ÉCRAN — slide "Contexte de l'exercice"]**

Voici le scénario. Tu gères un site de formation WordPress. Tu proposes une formation gratuite en 3 modules (M1-M3) et une formation premium en 13 modules (M4-M16). Ton objectif : automatiser tout le parcours étudiant.

**[ÉCRAN — slide "Étape 1 — Inscription et tagging"]**

Étape 1 : crée une automation déclenchée par l'inscription au cours gratuit M1-M3. À l'entrée, pose le tag "free-student" et ajoute le contact à la liste "etudiants-actifs". Envoie un email de bienvenue avec le lien d'accès au premier module.

**[ÉCRAN — slide "Étape 2 — Nurturing pendant la formation"]**

Étape 2 : dans la même automation ou dans une automation séparée, envoie une séquence de 3 emails de valeur espacés de 5 jours. Email 1 — une astuce avancée liée au module 1. Email 2 — un témoignage d'un étudiant qui a terminé. Email 3 — un aperçu de ce que contient la formation premium.

**[ÉCRAN — slide "Étape 3 — Goal complétion et upsell"]**

Étape 3 : ajoute un goal "Course Completed" sur M1-M3, en mode optionnel. Après le goal, ajoute un conditionnel. Branche "A terminé" : lance la séquence de vente premium (3 emails sur 10 jours). Branche "N'a pas terminé" : email d'encouragement puis délai de 7 jours avant la séquence de vente.

**[ÉCRAN — slide "Étape 4 — Achat et enroll automatique"]**

Étape 4 : crée une deuxième automation. Trigger : tag "a-achete-premium" appliqué. Actions : enroll dans le cours premium M4-M16, apply tag "premium-student", remove tag "free-student", envoyer l'email de bienvenue premium avec les liens d'accès.

**[ÉCRAN — slide "Étape 5 — Relance inactifs"]**

Étape 5 : crée une troisième automation de relance. Trigger : inscription à n'importe quel cours. Délai 14 jours. Condition : a progressé ? Si non, séquence de 3 emails de relance avec smart links (voir leçon 10.7).

**[ÉCRAN — slide "Critères de réussite"]**

[Checklist]

Ton funnel est complet si tu coches ces 6 critères. Un : l'inscription gratuite pose le tag "free-student" et envoie un email de bienvenue. Deux : le nurturing envoie 3 emails de valeur pendant la formation. Trois : le goal "Course Completed" détecte la fin du cours gratuit. Quatre : la séquence de vente se déclenche au bon moment. Cinq : l'achat enroll automatiquement dans le cours premium. Six : les inactifs sont relancés après 14 jours.

**[TRANSITION — face caméra]**

Prends 30 à 45 minutes pour construire ce funnel dans ton FluentCRM. Si tu bloques, reviens sur les leçons 10.3 à 10.7 — chaque pièce du puzzle y est détaillée. Une fois ton funnel en place, termine ce module avec le quiz pour valider tes acquis.

---

**Points clés** :
- Funnel complet en 3 automations : inscription/nurturing, achat/enroll, relance inactifs
- Tags clés : "free-student", "premium-student", "a-achete-premium"
- Goal optionnel pour détecter la complétion sans bloquer le flux
- Conditionnel pour personnaliser l'upsell selon la progression
- 6 critères de réussite à cocher

---

### Leçon 10.9 — Quiz : Valide tes acquis M10

**Durée** : 5 min
**Type** : Quiz (8 QCM)
**Écran** : Face caméra pour intro et conclusion, slides pour les questions

---

**[INTRO — face caméra]**

Dernier checkpoint du module 10. 8 questions pour vérifier que tu maîtrises l'intégration TutorLMS + FluentCRM. Triggers, actions, goals, segments, relance — tout y passe. Rappel : 75% minimum pour valider.

---

**Question 1** : Où active-t-on l'intégration TutorLMS dans FluentCRM ?

- A) FluentCRM > Automations > Settings
- B) FluentCRM > Settings > Integrations
- C) WordPress > Settings > Integrations
- D) TutorLMS > Settings > FluentCRM

**Réponse** : B — FluentCRM > Settings > Integrations. C'est là qu'on active le toggle TutorLMS.

---

**Question 2** : Quels triggers TutorLMS sont disponibles dans FluentCRM ? (Plusieurs réponses possibles)

- A) Student Enrolled in a Course
- B) Course Completed
- C) Student Logged In
- D) Quiz Passed
- E) Lesson Completed

**Réponse** : A, B, D, E — Les quatre triggers natifs. "Student Logged In" n'est pas un trigger TutorLMS dans FluentCRM.

---

**Question 3** : Tu veux inscrire automatiquement un étudiant à 3 cours après son achat. Comment fais-tu ?

- A) Une seule action Enroll avec les 3 cours sélectionnés
- B) Trois actions Enroll successives, une par cours
- C) Un webhook vers TutorLMS
- D) Un import CSV

**Réponse** : B — Une action Enroll = un cours. Pour plusieurs cours, on enchaîne les actions.

---

**Question 4** : Un étudiant est dans ton funnel de nurturing. Il termine le cours gratuit après le deuxième email. Que se passe-t-il si tu as un goal optionnel "Course Completed" ?

- A) Il continue à recevoir les emails de nurturing normalement
- B) Il saute directement au goal et entre dans la séquence de vente
- C) Il est retiré de l'automation
- D) Il reçoit tous les emails restants puis le goal s'active

**Réponse** : B — Le goal optionnel détecte la complétion et fait sauter le contact directement à ce point.

---

**Question 5** : Tu veux segmenter les étudiants inscrits au cours FluentCRM qui ne l'ont pas encore terminé. Quelle combinaison de filtres utilises-tu ?

- A) Tag "student" + liste "actifs"
- B) Enrolled in Course "FluentCRM" + Course "FluentCRM" not completed
- C) Tag "enrolled-fluentcrm" uniquement
- D) Enrolled in any course + No tag

**Réponse** : B — La combinaison de deux filtres TutorLMS donne le segment précis des étudiants en cours.

---

**Question 6** : Après combien de jours d'inactivité lance-t-on la première relance dans l'automation de la leçon 10.7 ?

- A) 7 jours
- B) 14 jours
- C) 21 jours
- D) 30 jours

**Réponse** : B — 14 jours. C'est la période de grâce avant la première vérification.

---

**Question 7** : Quel est l'avantage du smart link auto-login dans les emails de relance ?

- A) Il permet de tracker les ouvertures d'email
- B) Il connecte l'étudiant automatiquement et l'amène à sa leçon en cours
- C) Il crée un nouveau compte pour l'étudiant
- D) Il désactive le mot de passe de l'étudiant

**Réponse** : B — Zéro friction : un clic, l'étudiant est connecté et reprend exactement où il en était.

---

**Question 8** : Dans le funnel complet schoolsWP, que se passe-t-il quand un contact reçoit le tag "a-achete-premium" ?

- A) Il est ajouté à une liste d'attente
- B) Il reçoit un email de vente supplémentaire
- C) FluentCRM l'inscrit au cours premium, pose le tag "premium-student" et retire le tag "free-student"
- D) Il est retiré de toutes les automations

**Réponse** : C — L'automation d'achat enchaîne enroll + tag "premium-student" + remove tag "free-student" + email de bienvenue.

---

**[TRANSITION — face caméra]**

Module 10 terminé. Tu sais maintenant connecter TutorLMS et FluentCRM, automatiser les inscriptions, segmenter par progression, et relancer les inactifs. C'est la combinaison qui transforme un simple LMS en machine de rétention. Dans le module suivant, on passe à un autre sujet. Mais ce que tu as construit ici — le funnel étudiant complet — c'est une base que tu peux dupliquer pour chaque nouvelle formation que tu lances.

---

**Points clés du quiz** :
- 8 questions couvrant les leçons 10.1 à 10.7
- Seuil de validation : 75% (6/8)
- Questions sur : activation intégration, triggers, actions, goals, filtres, relance, smart links, funnel complet
