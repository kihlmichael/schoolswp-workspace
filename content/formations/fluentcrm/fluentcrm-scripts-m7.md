# Scripts vidéo — Module 7 : Automation avancée

**Formation** : Maîtriser FluentCRM
**Module** : M7 — Automation avancée (Premium)
**Leçons** : 6 vidéos + 1 exercice + 1 quiz
**Durée totale** : ~50 min
**Prérequis** : M6 (automations de base)
**Date** : 2026-03-23

---

### Leçon 7.1 — Goals : définis des objectifs dans ton funnel

**Durée** : 7 min
**Type** : Vidéo HeyGen
**Écran** : Face caméra pour intro/conclusion, screencast FluentCRM automation builder

---

**[INTRO — face caméra]**

Tu as un funnel de vente avec 5 emails. Un contact achète après le deuxième email. Que se passe-t-il ? Sans goal, il reçoit quand même les 3 emails suivants — ceux qui lui demandent d'acheter un truc qu'il a déjà acheté. Pas idéal. Les Goals dans FluentCRM résolvent exactement ce problème. Dans cette leçon, tu apprends à poser des objectifs dans tes automations pour que les contacts sortent du funnel au bon moment.

**[ÉCRAN — screencast FluentCRM > Automations]**

[Ouvre une automation existante dans le builder visuel]

Étape 1 : ouvre une automation existante ou crée-en une nouvelle. On va travailler sur un funnel de vente classique — une séquence d'emails qui pousse vers l'achat d'une formation premium.

[Montre la barre latérale avec les blocs disponibles]

Étape 2 : dans la barre latérale du builder, cherche le bloc "Goal". Tu le trouves dans la catégorie "Internal Actions". Fais-le glisser dans ton automation, à l'endroit où tu veux que l'objectif soit évalué.

[Place le bloc Goal après une séquence de 3 emails]

Étape 3 : place le goal après ta séquence d'emails de vente. L'idée : si le contact atteint cet objectif avant d'avoir reçu tous les emails, il saute directement au goal et ignore les étapes intermédiaires.

**[ÉCRAN — screencast configuration du Goal]**

[Clique sur le bloc Goal pour ouvrir sa configuration]

Étape 4 : configure le goal. Tu dois définir deux choses. D'abord, la condition : quel événement déclenche l'objectif ? Pour un funnel de vente, c'est généralement un tag. Par exemple : "a-achete-premium". Quand FluentCRM détecte ce tag sur le contact, l'objectif est atteint.

[Montre le champ de sélection de la condition]

Tu peux choisir parmi plusieurs conditions : tag appliqué, liste rejointe, champ personnalisé modifié. Pour un achat, le tag est le plus fiable — tu le poses via ton plugin e-commerce ou manuellement.

[Montre l'option "Benchmark"]

Étape 5 : le paramètre "Benchmark". C'est le terme FluentCRM pour dire : ce goal sert aussi de point d'entrée. Si tu coches cette option, un contact qui reçoit le tag "a-achete-premium" peut entrer dans l'automation directement à ce point, même s'il n'était pas dans le funnel avant. On reviendra là-dessus dans la leçon suivante.

**[ÉCRAN — screencast test du comportement]**

[Montre un contact dans le funnel qui reçoit le tag]

Étape 6 : voyons ce qui se passe concrètement. Un contact entre dans ton funnel. Il reçoit l'email 1, puis l'email 2. Entre l'email 2 et l'email 3, il achète la formation. Ton plugin e-commerce — WooCommerce, TutorLMS, peu importe — pose le tag "a-achete-premium".

[Montre le contact qui saute au Goal dans le builder]

FluentCRM détecte le tag. Le contact saute directement au goal. Les emails 3, 4 et 5 ne sont jamais envoyés. Le contact continue l'automation après le goal — par exemple, vers un email de bienvenue ou un onboarding.

**[TRANSITION — face caméra]**

Les goals sont le mécanisme central pour gérer les parcours non linéaires dans tes funnels. Sans eux, tes automations restent rigides — tout le monde reçoit tout, dans l'ordre. Avec eux, chaque contact avance à son rythme. Dans la prochaine leçon, on voit la différence entre un goal optionnel et un goal essentiel — et pourquoi ça change complètement le comportement de ton automation.

---

**Points clés** :
- Un Goal = un point de contrôle dans ton automation qui détecte si un objectif est atteint
- Conditions possibles : tag appliqué, liste rejointe, champ personnalisé
- Le contact saute directement au goal quand la condition est remplie — les étapes intermédiaires sont ignorées
- Benchmark = le goal peut servir de point d'entrée dans l'automation
- Cas d'usage principal : sortir un acheteur d'un funnel de vente

**Mots clés SEO** : FluentCRM goal automation, funnel FluentCRM, objectif automation email, FluentCRM benchmark

---

### Leçon 7.2 — Goal optionnel vs essentiel : quand utiliser chaque type

**Durée** : 6 min
**Type** : Vidéo HeyGen
**Écran** : Face caméra pour intro/conclusion, screencast FluentCRM automation builder

---

**[INTRO — face caméra]**

Dans la leçon précédente, tu as posé un goal dans ton automation. Mais FluentCRM te propose deux modes pour chaque goal : "Can be achieved by contact at any time" et "Must be achieved to proceed". Ce n'est pas un détail — ça change complètement le comportement de ton funnel. Dans cette leçon, on clarifie la différence et tu sauras exactement quand utiliser chaque mode.

**[ÉCRAN — screencast FluentCRM > Automation builder]**

[Ouvre un goal existant, montre les deux options]

Voici les deux modes d'un goal dans FluentCRM.

Mode 1 : "Can be achieved at any time" — le goal optionnel. Le contact avance dans l'automation normalement, étape par étape. Si à un moment il remplit la condition du goal, il saute directement au goal. Mais s'il ne la remplit jamais, il continue quand même — il passe le goal sans s'arrêter.

Mode 2 : "Must be achieved to proceed" — le goal essentiel. Le contact avance dans l'automation jusqu'au goal. S'il n'a pas rempli la condition, il s'arrête. Il reste bloqué au goal tant que la condition n'est pas remplie. Aucune étape suivante ne sera exécutée.

**[ÉCRAN — slide "Comparaison visuelle"]**

[Montre deux schémas côte à côte]

Schéma 1 — goal optionnel. Le contact entre. Email 1, email 2, email 3. À n'importe quel moment, s'il achète, il saute au goal. S'il n'achète jamais, il traverse le goal et continue. Par exemple, il reçoit un email de conclusion ou un feedback.

Schéma 2 — goal essentiel. Le contact entre. Email 1, email 2, email 3. Il arrive au goal. S'il n'a pas acheté, il s'arrête là. Pas d'email de conclusion, pas de suite. Il attend indéfiniment — jusqu'à ce que la condition soit remplie ou que tu le retires manuellement de l'automation.

**[ÉCRAN — screencast cas concret 1 : funnel de vente]**

[Montre un funnel de vente avec un goal optionnel]

Cas concret : funnel de vente post-formation. Tu as une séquence de 5 emails qui propose la formation premium. Le goal "a-achete-premium" est en mode optionnel.

Pourquoi optionnel ? Parce que même si le contact n'achète pas, tu veux qu'il continue. Après le goal, tu places un branchement conditionnel : s'il a acheté, onboarding. S'il n'a pas acheté, email de feedback pour comprendre pourquoi.

**[ÉCRAN — screencast cas concret 2 : prérequis obligatoire]**

[Montre une automation avec un goal essentiel]

Cas concret : onboarding avec prérequis. Tu formes tes utilisateurs à configurer FluentCRM. L'étape 3 de ton onboarding nécessite que l'utilisateur ait connecté son domaine email. Le goal "domaine-configure" est en mode essentiel.

Pourquoi essentiel ? Parce que les étapes suivantes n'ont aucun sens sans le domaine. Envoyer un email "configure tes premiers templates" à quelqu'un qui n'a pas encore de domaine, c'est du bruit. Le goal essentiel bloque la progression tant que le prérequis n'est pas rempli.

**[ÉCRAN — slide "Règle de décision"]**

[Montre un arbre de décision simple]

La règle est simple. Pose-toi la question : est-ce que la suite de l'automation a du sens si le goal n'est pas atteint ?

Si oui — goal optionnel. Le contact continue quoi qu'il arrive.
Si non — goal essentiel. Le contact attend.

**[TRANSITION — face caméra]**

Tu sais maintenant choisir entre les deux modes de goal. Retiens : optionnel pour les funnels de vente où tu veux gérer les deux cas (acheteur et non-acheteur), essentiel pour les prérequis obligatoires. Dans la prochaine leçon, on passe aux split tests A/B directement dans tes automations.

---

**Points clés** :
- Goal optionnel ("Can be achieved at any time") : le contact continue même si le goal n'est pas atteint
- Goal essentiel ("Must be achieved to proceed") : le contact est bloqué tant que la condition n'est pas remplie
- Funnel de vente = goal optionnel (tu gères acheteurs et non-acheteurs)
- Prérequis obligatoire = goal essentiel (la suite n'a pas de sens sans)
- Règle : est-ce que la suite a du sens si le goal n'est pas atteint ?

**Mots clés SEO** : FluentCRM goal optionnel, goal essentiel FluentCRM, benchmark automation, funnel automation WordPress

---

### Leçon 7.3 — Split test A/B dans tes automations

**Durée** : 7 min
**Type** : Vidéo HeyGen
**Écran** : Face caméra pour intro/conclusion, screencast FluentCRM automation builder

---

**[INTRO — face caméra]**

Tu envoies une séquence de vente. Tu veux savoir si un email avec une vidéo performe mieux qu'un email texte classique. Ou si une ligne d'objet directe convertit mieux qu'une ligne avec une question. Le split test A/B dans les automations FluentCRM te donne la réponse. Dans cette leçon, tu mets en place ton premier test directement dans le builder visuel.

**[ÉCRAN — screencast FluentCRM > Automation builder]**

[Ouvre une automation, montre la barre latérale]

Étape 1 : dans le builder d'automation, cherche le bloc "Split" ou "A/B Testing" dans les actions disponibles. Ce bloc divise ton flux en deux branches (ou plus) et répartit les contacts selon un pourcentage que tu définis.

[Ajoute le bloc Split dans l'automation]

Étape 2 : place le bloc à l'endroit où tu veux tester. Typiquement, juste avant l'envoi d'un email. Le bloc va créer deux chemins : chemin A et chemin B.

**[ÉCRAN — screencast configuration du split test]**

[Montre la configuration du bloc]

Étape 3 : configure la répartition. Par défaut, c'est 50/50. La moitié des contacts prend le chemin A, l'autre moitié le chemin B. Tu peux ajuster — 70/30, 80/20 — mais pour un vrai test, 50/50 est la norme.

[Montre le chemin A avec un email texte]

Étape 4 : configure le chemin A. Place un bloc email avec ta version "texte classique". Objet, corps du mail, CTA — ta version de référence.

[Montre le chemin B avec un email contenant une vidéo]

Étape 5 : configure le chemin B. Place un bloc email avec ta version "vidéo". Même objet ou objet différent — ça dépend de ce que tu testes. Si tu testes le format du contenu, garde le même objet. Si tu testes l'objet, garde le même contenu.

Important : ne teste qu'une variable à la fois. Si tu changes l'objet ET le contenu, tu ne sauras pas ce qui a fait la différence.

**[ÉCRAN — screencast convergence après le test]**

[Montre les deux chemins qui convergent vers la suite du funnel]

Étape 6 : après le split test, les deux chemins doivent converger. Les contacts des deux branches continuent dans le même funnel. Le test porte sur un email, pas sur tout le parcours.

[Montre comment relier les deux branches au même bloc suivant]

Connecte la fin du chemin A et la fin du chemin B au même bloc. Par exemple, un délai de 24 heures puis le prochain email de la séquence.

**[ÉCRAN — screencast lecture des résultats]**

[Montre les statistiques de l'automation]

Étape 7 : lecture des résultats. Après quelques jours — et suffisamment de contacts passés dans le test — compare les métriques. Taux d'ouverture si tu as testé l'objet. Taux de clic si tu as testé le contenu. Taux de conversion si tu as un goal après le test.

[Montre les taux d'ouverture et de clic des deux variantes]

FluentCRM affiche les stats par email. Variante A : 38% d'ouverture, 12% de clic. Variante B : 42% d'ouverture, 18% de clic. La version vidéo gagne sur les deux métriques.

**[ÉCRAN — slide "Bonnes pratiques split test"]**

[Montre une liste]

Quelques règles pour des tests fiables.

Un : attends au moins 200 contacts par branche avant de conclure. Avec 20 contacts, les résultats ne veulent rien dire.

Deux : ne teste qu'une variable. Objet OU contenu OU CTA. Pas tout en même temps.

Trois : définis ton critère de succès avant le test. "Je cherche à maximiser le taux de clic" — pas "je verrai bien".

Quatre : une fois le gagnant identifié, supprime la variante perdante et garde la gagnante comme email définitif.

**[TRANSITION — face caméra]**

Tu sais maintenant poser un split test A/B dans tes automations FluentCRM. Le test dans l'automation est plus puissant que le test classique sur une campagne unique — parce qu'il tourne en continu, avec chaque nouveau contact qui entre dans le funnel. Dans la prochaine leçon, on va au-delà du A/B avec les conditionals multi-chemins.

---

**Points clés** :
- Le bloc Split divise le flux en deux branches avec un pourcentage configurable
- 50/50 est la répartition standard pour un test fiable
- Ne tester qu'une variable à la fois (objet, contenu, ou CTA)
- Minimum 200 contacts par branche pour des résultats significatifs
- Le split test en automation tourne en continu — chaque nouveau contact est testé

**Mots clés SEO** : split test FluentCRM, A/B testing automation email, test email WordPress, FluentCRM automation split

---

### Leçon 7.4 — Multi-path conditionals : plus de 2 chemins

**Durée** : 6 min
**Type** : Vidéo HeyGen
**Écran** : Face caméra pour intro/conclusion, screencast FluentCRM automation builder

---

**[INTRO — face caméra]**

Un branchement conditionnel classique, c'est oui ou non. Le contact a le tag, ou il ne l'a pas. Mais dans un vrai funnel, tu as souvent plus de deux scénarios. Un contact peut être client premium, client standard, ou prospect. Il peut être inscrit depuis moins de 7 jours, entre 7 et 30 jours, ou plus de 30 jours. Les conditionals multi-chemins dans FluentCRM gèrent ces cas. Dans cette leçon, tu construis un branchement à 3 chemins ou plus.

**[ÉCRAN — screencast FluentCRM > Automation builder]**

[Ouvre le builder, montre le bloc conditionnel]

Étape 1 : dans le builder, ajoute un bloc conditionnel. C'est le même bloc que tu utilises pour un simple oui/non, mais on va l'étendre.

[Montre la configuration du premier chemin]

Étape 2 : configure la première condition. Par exemple : "a le tag client-premium". Les contacts qui remplissent cette condition prennent le chemin 1.

[Montre comment ajouter un deuxième chemin conditionnel]

Étape 3 : ajoute un deuxième bloc conditionnel dans la branche "non" du premier. Condition : "a le tag client-standard". Les contacts qui remplissent cette condition prennent le chemin 2.

[Montre la branche "non" du deuxième conditionnel]

Étape 4 : la branche "non" du deuxième conditionnel, c'est ton chemin 3 — les prospects. Ceux qui ne sont ni premium ni standard.

**[ÉCRAN — slide "Schéma multi-path"]**

[Montre le schéma en arbre]

Visuellement, ça donne un arbre. L'entrée unique se divise en 3 branches.

Branche 1 : client premium — reçoit un email d'upsell vers le coaching.
Branche 2 : client standard — reçoit un email d'upgrade vers le premium.
Branche 3 : prospect — reçoit un email de vente vers l'offre standard.

Chaque branche a son propre contenu, son propre ton, ses propres CTA. Un seul funnel gère les trois segments.

**[ÉCRAN — screencast construction du multi-path]**

[Construit les 3 branches en direct]

[Chemin 1 : place un email "Coaching individuel — places limitées"]

Voilà le chemin premium. Email personnalisé, ton exclusif, offre de coaching.

[Chemin 2 : place un email "Passe au premium — 30% ce mois"]

Chemin standard. Mise en avant des bénéfices du premium, avec une offre limitée.

[Chemin 3 : place un email "Découvre la formation — essai gratuit"]

Chemin prospect. Approche pédagogique, lien vers un module gratuit ou une démo.

**[ÉCRAN — screencast convergence]**

[Montre les 3 branches qui convergent vers un délai commun]

Étape 5 : après chaque branche, fais converger les chemins. Les 3 branches se reconnectent au même point — par exemple, un délai de 48 heures avant le prochain email commun.

**[ÉCRAN — slide "Conseils pratiques"]**

[Montre une liste]

Premier conseil : limite-toi à 3 ou 4 chemins maximum. Au-delà, l'automation devient illisible et difficile à maintenir.

Deuxième conseil : nomme tes blocs conditionnels clairement. "Est client premium ?", "Est client standard ?" — pas "Condition 1", "Condition 2".

Troisième conseil : pense à l'ordre. Place la condition la plus restrictive en premier. Si tu testes "a le tag client" avant "a le tag client-premium", le premium sera capturé par la première condition et n'atteindra jamais la deuxième.

**[TRANSITION — face caméra]**

Tu sais maintenant créer des parcours multi-chemins dans tes automations. L'idée centrale : un seul funnel, plusieurs segments, chacun avec son contenu adapté. Dans la prochaine leçon, on explore les triggers avancés — anniversaire, changement de champ personnalisé, suppression de tag.

---

**Points clés** :
- Les conditionals multi-chemins = enchaîner des blocs conditionnels pour créer 3+ branches
- Chaque branche a son propre contenu et ses propres CTA
- Limiter à 3-4 chemins pour garder l'automation lisible
- Placer la condition la plus restrictive en premier
- Toujours nommer les blocs clairement

**Mots clés SEO** : FluentCRM conditional, multi-path automation, segmentation automation WordPress, branchement conditionnel email

---

### Leçon 7.5 — Triggers avancés : birthday, company, custom field change

**Durée** : 6 min
**Type** : Vidéo HeyGen
**Écran** : Face caméra pour intro/conclusion, screencast FluentCRM automation builder

---

**[INTRO — face caméra]**

Jusqu'ici, tu as déclenché tes automations avec des triggers classiques : ajout de tag, inscription à une liste, soumission de formulaire. FluentCRM propose des triggers plus spécifiques qui ouvrent de nouveaux cas d'usage. Dans cette leçon, on couvre trois triggers avancés : l'anniversaire, le changement de champ personnalisé, et la suppression de tag.

**[ÉCRAN — screencast FluentCRM > Automations > Nouveau trigger]**

[Montre la liste des triggers disponibles]

Voici la liste complète des triggers dans FluentCRM. Tu connais déjà les premiers : "Tag Applied", "List Applied", "Form Submitted". Descendons plus bas.

**[ÉCRAN — screencast trigger Birthday]**

[Sélectionne le trigger "Contact Birthday"]

Trigger 1 : Contact Birthday. Ce trigger se déclenche automatiquement à la date d'anniversaire du contact. Pour qu'il fonctionne, le champ "Date of Birth" doit être renseigné dans la fiche du contact.

[Montre la configuration du trigger]

La configuration est simple. Tu choisis combien de jours avant l'anniversaire le trigger se déclenche. Zéro pour le jour même. Un pour la veille. Sept pour une semaine avant.

[Montre un email d'anniversaire type]

Cas d'usage schoolsWP : tu formes des coachs en ligne. Chaque année, à l'anniversaire de ton client, tu envoies un email personnalisé avec un code promo de 20% sur ta prochaine formation. C'est un geste simple qui renforce la relation et génère des ventes récurrentes.

**[ÉCRAN — screencast trigger Custom Field Change]**

[Revient à la liste des triggers, sélectionne "Custom Field Changed"]

Trigger 2 : Custom Field Changed. Ce trigger se déclenche quand la valeur d'un champ personnalisé est modifiée. C'est puissant parce que les champs personnalisés sont le moyen le plus flexible de stocker des données sur tes contacts.

[Montre la configuration : choix du champ et de la valeur]

Tu sélectionnes le champ à surveiller. Par exemple : "niveau_formation" avec les valeurs "débutant", "intermédiaire", "avancé". Quand un contact passe de "débutant" à "intermédiaire", le trigger se déclenche.

[Montre un cas d'usage]

Cas d'usage : quand un étudiant termine le module 5 de ta formation, ton LMS met à jour le champ "niveau_formation" à "intermédiaire". FluentCRM détecte le changement et lance une automation de félicitations + proposition du niveau avancé.

**[ÉCRAN — screencast trigger Tag Removed]**

[Revient à la liste des triggers, sélectionne "Tag Removed"]

Trigger 3 : Tag Removed. Le pendant de "Tag Applied". Ce trigger se déclenche quand un tag est retiré d'un contact.

[Montre la configuration]

Tu sélectionnes le tag à surveiller. Par exemple : "abonne-newsletter".

[Montre un cas d'usage]

Cas d'usage : un contact se désabonne de ta newsletter. Tu retires le tag "abonne-newsletter". Le trigger "Tag Removed" se déclenche et lance une automation de réengagement — un email 7 jours plus tard pour demander pourquoi il est parti, avec une offre de contenu exclusif pour le faire revenir.

Autre cas : le tag "client-actif" est retiré quand un abonnement expire. Le trigger lance un funnel de win-back avec une offre de renouvellement.

**[ÉCRAN — slide "Résumé des 3 triggers"]**

[Tableau comparatif]

Birthday : se déclenche à la date d'anniversaire. Nécessite le champ Date of Birth. Usage : emails personnalisés, promos anniversaire.

Custom Field Changed : se déclenche quand un champ personnalisé est modifié. Usage : progression de formation, changement de statut, mise à jour de profil.

Tag Removed : se déclenche quand un tag est retiré. Usage : désabonnement, expiration, désengagement.

**[TRANSITION — face caméra]**

Ces trois triggers te permettent de réagir à des événements que les triggers classiques ne couvrent pas. L'anniversaire pour la relation, le changement de champ pour la progression, la suppression de tag pour le win-back. Dans la prochaine leçon, on voit comment importer et exporter tes automations — pour les sauvegarder, les partager, ou les dupliquer entre sites.

---

**Points clés** :
- Birthday : déclenche un email X jours avant/le jour de l'anniversaire du contact
- Custom Field Changed : réagit quand la valeur d'un champ personnalisé est modifiée
- Tag Removed : réagit quand un tag est retiré (désabonnement, expiration)
- Chaque trigger ouvre des cas d'usage que les triggers classiques ne couvrent pas
- Le champ Date of Birth doit être renseigné pour que Birthday fonctionne

**Mots clés SEO** : FluentCRM trigger avancé, birthday email automation, custom field trigger, tag removed FluentCRM

---

### Leçon 7.6 — Importe et exporte tes automations

**Durée** : 5 min
**Type** : Vidéo HeyGen
**Écran** : Face caméra pour intro/conclusion, screencast FluentCRM

---

**[INTRO — face caméra]**

Tu as construit une automation complexe — un funnel de vente avec des goals, des split tests, des conditionals. Tu veux la sauvegarder, la dupliquer sur un autre site, ou la partager avec un client. FluentCRM permet d'exporter et d'importer des automations en JSON. Dans cette leçon, tu apprends à le faire.

**[ÉCRAN — screencast FluentCRM > Automations]**

[Montre la liste des automations]

Étape 1 : va dans FluentCRM, section Automations. Tu vois la liste de toutes tes automations.

**[ÉCRAN — screencast export]**

[Sélectionne une automation, montre le menu d'actions]

Étape 2 : ouvre l'automation que tu veux exporter. Dans le builder, cherche l'option d'export. Selon la version de FluentCRM, c'est soit un bouton "Export" dans la barre d'outils, soit dans le menu "More Options" ou les trois points.

[Montre le fichier JSON téléchargé]

Étape 3 : FluentCRM génère un fichier JSON qui contient toute la structure de ton automation. Les blocs, les connexions, les conditions, les délais — tout est là. Les emails eux-mêmes sont inclus avec leur contenu.

[Ouvre le fichier JSON dans un éditeur]

Voici à quoi ressemble le fichier. Tu vois les étapes, les conditions, les templates d'email. Tu n'as pas besoin de modifier ce fichier — c'est FluentCRM qui le lit. Mais savoir que c'est du JSON standard te permet de le versionner dans Git, de le stocker dans un Drive, ou de le partager par email.

**[ÉCRAN — screencast import]**

[Va dans Automations > Import]

Étape 4 : pour importer, va dans la liste des automations. Cherche le bouton "Import" ou "Import Automation".

[Montre le formulaire d'import]

Étape 5 : sélectionne ton fichier JSON. FluentCRM le lit et recrée toute l'automation avec ses blocs, ses connexions et ses emails.

[Montre l'automation importée dans le builder]

Étape 6 : vérifie l'automation importée. Tous les blocs sont là, dans le bon ordre. Mais attention à trois choses.

**[ÉCRAN — slide "Points de vigilance après import"]**

[Montre une liste]

Premier point : les tags. Si ton automation référence le tag "client-premium" et que ce tag n'existe pas sur le site de destination, FluentCRM ne le créera pas automatiquement. Tu devras créer les tags manquants et les réassigner dans les blocs concernés.

Deuxième point : les listes. Même logique. Si l'automation ajoute des contacts à la liste "Clients VIP", cette liste doit exister sur le site de destination.

Troisième point : les liens dans les emails. Si tes emails contiennent des liens vers ton site, ils pointent toujours vers le site d'origine. Mets-les à jour manuellement.

Quatrième point : les intégrations. Si un bloc dépend d'un plugin — WooCommerce, TutorLMS — ce plugin doit être installé et configuré sur le site de destination.

**[ÉCRAN — screencast bonnes pratiques]**

[Montre un dossier de fichiers JSON organisé]

Bonne pratique : crée un dossier dédié pour tes exports. Nomme tes fichiers avec une convention claire. Par exemple : "funnel-vente-premium-v2-2026-03.json". Date, version, nom explicite.

Autre bonne pratique : exporte tes automations avant chaque modification majeure. C'est ton système de sauvegarde. Si une modification casse ton funnel, tu réimportes la version précédente.

**[TRANSITION — face caméra]**

Tu sais maintenant exporter, sauvegarder et réimporter tes automations. C'est un réflexe à prendre : avant chaque modification importante, exporte. Ça te prend 10 secondes et ça peut te sauver des heures de reconstruction. Dans la prochaine leçon, on met tout ensemble : tu construis un funnel d'upsell complet avec split test et goal.

---

**Points clés** :
- Export = fichier JSON contenant toute la structure de l'automation + emails
- Import recrée l'automation mais ne crée pas les tags, listes ou intégrations manquantes
- Vérifier après import : tags, listes, liens, plugins dépendants
- Convention de nommage : nom-version-date.json
- Exporter avant chaque modification majeure = sauvegarde

**Mots clés SEO** : exporter automation FluentCRM, importer automation WordPress, backup automation email, FluentCRM JSON export

---

### Leçon 7.7 — Exercice : Crée un funnel d'upsell avec split test et goal

**Durée** : 8 min
**Type** : Exercice guidé (Vidéo HeyGen)
**Écran** : Face caméra pour intro/conclusion, screencast FluentCRM automation builder

---

**[INTRO — face caméra]**

C'est l'exercice du module. Tu vas construire un funnel d'upsell complet en combinant tout ce que tu as appris : split test A/B, goal avec benchmark, et conditional multi-chemins. Le scénario : un étudiant vient de terminer ta formation gratuite sur TutorLMS. Tu veux lui proposer la formation premium. On construit ce funnel ensemble, étape par étape.

**[ÉCRAN — slide "Le scénario"]**

[Montre le schéma du funnel]

Voici le parcours complet.

Déclencheur : le contact reçoit le tag "formation-gratuite-terminee" (posé automatiquement par TutorLMS).

Étape 1 : délai de 24 heures. On ne vend pas dans la seconde où quelqu'un finit une formation.

Étape 2 : split test A/B à 50/50.
- Chemin A : email texte avec témoignages d'étudiants premium.
- Chemin B : email avec vidéo où tu présentes les bénéfices du premium.

Étape 3 : délai de 3 jours.

Étape 4 : email de relance commun aux deux branches. Rappel de l'offre + code promo limité à 48 heures.

Étape 5 : goal "a-achete-premium" en mode optionnel.

Après le goal : conditional multi-chemins.
- Si tag "a-achete-premium" : email de bienvenue premium + ajout liste "Étudiants Premium".
- Si pas le tag : email de feedback + code promo de dernière chance.

**[ÉCRAN — screencast construction étape par étape]**

[Crée une nouvelle automation]

Étape 1 : crée une nouvelle automation. Nom : "Upsell post-formation gratuite". Trigger : "Tag Applied" > "formation-gratuite-terminee".

[Ajoute le délai de 24 heures]

Étape 2 : ajoute un bloc délai. 24 heures. Le contact attend une journée avant de recevoir quoi que ce soit.

[Ajoute le bloc Split 50/50]

Étape 3 : ajoute le bloc split test. Répartition 50/50.

[Configure le chemin A]

Étape 4 : chemin A. Place un bloc email. Objet : "Les étudiants premium partagent leur expérience". Corps : 3 témoignages courts, un CTA vers la page de vente.

[Configure le chemin B]

Étape 5 : chemin B. Place un bloc email. Objet : "Regarde ce que le premium t'apporte — en 2 minutes". Corps : lien vers une vidéo de présentation, même CTA vers la page de vente.

[Fait converger les deux chemins]

Étape 6 : les deux chemins convergent vers un délai de 3 jours.

[Ajoute l'email de relance]

Étape 7 : après le délai, place un email de relance. Objet : "Dernière chance — 20% avec le code PREMIUM20". Corps : rappel des bénéfices, urgence (48h), CTA.

[Ajoute le goal]

Étape 8 : place le goal "a-achete-premium". Mode : "Can be achieved at any time" — optionnel. Condition : tag "a-achete-premium" présent.

Pourquoi optionnel ? Parce que tu veux gérer les deux cas : ceux qui achètent et ceux qui n'achètent pas.

[Ajoute le conditional après le goal]

Étape 9 : après le goal, place un bloc conditionnel. Condition : "Has tag a-achete-premium".

[Configure le chemin "oui"]

Étape 10 : chemin oui — le contact a acheté. Place un email de bienvenue premium. Ajoute un bloc "Add to List" : "Étudiants Premium". Ajoute un bloc "Remove Tag" : "formation-gratuite-terminee" pour nettoyer.

[Configure le chemin "non"]

Étape 11 : chemin non — le contact n'a pas acheté. Place un email de feedback. Objet : "On aimerait comprendre". Corps : 3 raisons possibles (prix, timing, contenu), un lien vers un formulaire de feedback, et un dernier code promo valable 7 jours.

**[ÉCRAN — screencast vérification finale]**

[Vue d'ensemble de l'automation complète]

Étape 12 : vérifie l'ensemble. De haut en bas : trigger tag, délai 24h, split test A/B, convergence, délai 3 jours, email relance, goal, conditional, deux chemins de sortie. Tout est connecté.

[Active l'automation]

Étape 13 : active l'automation. Elle est prête à recevoir des contacts.

**[TRANSITION — face caméra]**

Bravo. Tu viens de construire un funnel d'upsell complet avec les trois mécaniques avancées de FluentCRM : split test pour optimiser, goal pour détecter l'achat, conditional pour adapter la suite. C'est exactement ce type de funnel qui tourne en arrière-plan et génère des ventes sans que tu interviennes au quotidien. Dernière étape du module : le quiz pour valider tes acquis.

---

**Points clés** :
- Funnel complet : trigger tag > délai > split test > relance > goal > conditional > 2 sorties
- Split test A/B : email texte vs email vidéo, 50/50
- Goal optionnel : détecte l'achat sans bloquer les non-acheteurs
- Conditional après le goal : parcours personnalisé acheteur vs non-acheteur
- Nettoyage : retirer les tags obsolètes, ajouter aux bonnes listes

**Mots clés SEO** : funnel upsell FluentCRM, automation upsell WordPress, split test email funnel, FluentCRM exercice pratique

---

### Leçon 7.8 — Quiz : Valide tes acquis M7

**Durée** : 5 min
**Type** : Quiz TutorLMS (8 QCM)
**Format** : Questions affichées dans TutorLMS, pas de vidéo

---

**Question 1** : Quel est le rôle principal d'un Goal dans une automation FluentCRM ?

- A) Envoyer un email automatique à une date précise
- B) Détecter si un contact a atteint un objectif et adapter son parcours en conséquence ✅
- C) Supprimer un contact de l'automation après un certain délai
- D) Créer un segment automatique basé sur l'engagement

**Explication** : Un Goal surveille une condition (tag, liste, champ). Quand elle est remplie, le contact saute directement au goal, ignorant les étapes intermédiaires.

---

**Question 2** : Un goal en mode "Can be achieved at any time" (optionnel) — que se passe-t-il si le contact n'atteint jamais l'objectif ?

- A) Le contact est supprimé de l'automation
- B) Le contact reste bloqué indéfiniment au niveau du goal
- C) Le contact traverse le goal et continue l'automation normalement ✅
- D) FluentCRM envoie une notification à l'administrateur

**Explication** : En mode optionnel, le contact continue même sans atteindre l'objectif. En mode essentiel ("Must be achieved"), il serait bloqué.

---

**Question 3** : Tu configures un split test A/B dans une automation. Quelle est la meilleure pratique ?

- A) Tester l'objet, le contenu et le CTA en même temps pour gagner du temps
- B) Ne tester qu'une seule variable à la fois pour identifier ce qui fait la différence ✅
- C) Utiliser une répartition 90/10 pour limiter les risques
- D) Attendre 10 contacts par branche avant de conclure

**Explication** : Tester une seule variable à la fois garantit des résultats exploitables. Minimum recommandé : 200 contacts par branche.

---

**Question 4** : Comment créer un branchement à 3 chemins dans FluentCRM ?

- A) Utiliser le bloc "Triple Split" disponible dans les actions avancées
- B) Enchaîner des blocs conditionnels : le premier filtre un segment, la branche "non" contient un deuxième conditionnel ✅
- C) Créer 3 automations séparées avec des triggers différents
- D) Utiliser un goal avec 3 conditions simultanées

**Explication** : FluentCRM n'a pas de bloc "triple split" natif. On enchaîne des conditionnels : la branche "non" du premier contient le deuxième test, et ainsi de suite.

---

**Question 5** : Le trigger "Contact Birthday" nécessite que :

- A) Le contact ait un tag "birthday" appliqué manuellement
- B) Le champ "Date of Birth" soit renseigné dans la fiche du contact ✅
- C) L'administrateur active le module "Calendar" dans les réglages FluentCRM
- D) Le contact soit inscrit dans une liste spécifique "Anniversaires"

**Explication** : Le trigger Birthday lit le champ Date of Birth. Sans cette donnée, le trigger ne se déclenche jamais.

---

**Question 6** : Tu exportes une automation FluentCRM et tu l'importes sur un autre site. Qu'est-ce que FluentCRM NE recrée PAS automatiquement ?

- A) Les blocs de l'automation et leurs connexions
- B) Le contenu des emails inclus dans l'automation
- C) Les tags et listes référencés dans l'automation ✅
- D) Les délais configurés entre les étapes

**Explication** : L'import recrée la structure et les emails, mais pas les tags, listes, ou intégrations. Tu dois les créer manuellement sur le site de destination.

---

**Question 7** : Dans un funnel d'upsell, tu places un goal "a-achete-premium" en mode optionnel. Pourquoi optionnel plutôt qu'essentiel ?

- A) Parce que le mode essentiel n'est pas compatible avec les split tests
- B) Parce que tu veux que les non-acheteurs continuent dans l'automation pour recevoir un email de feedback ✅
- C) Parce que le mode optionnel est plus rapide à configurer
- D) Parce que le mode essentiel supprime les contacts qui n'atteignent pas le goal

**Explication** : En mode optionnel, les non-acheteurs traversent le goal et continuent — tu peux leur envoyer un email de feedback ou une dernière offre. En mode essentiel, ils seraient bloqués.

---

**Question 8** : Le trigger "Tag Removed" est particulièrement utile pour :

- A) Ajouter automatiquement un nouveau tag en remplacement
- B) Lancer un funnel de win-back quand un abonnement expire ou qu'un contact se désabonne ✅
- C) Nettoyer la base de contacts en supprimant les inactifs
- D) Synchroniser les tags entre FluentCRM et WooCommerce

**Explication** : "Tag Removed" détecte la perte d'un statut (désabonnement, expiration). C'est le déclencheur idéal pour les séquences de réengagement et de win-back.

---

**Seuil de réussite** : 6/8 (75%)

**Message de réussite** : Module 7 validé. Tu maîtrises les mécaniques avancées d'automation FluentCRM : goals, split tests, conditionals multi-chemins et triggers avancés. Le module 8 t'attend pour passer à la délivrabilité et au monitoring.

**Message d'échec** : Score insuffisant. Revisionne les leçons 7.1 à 7.6 avant de retenter le quiz. Concentre-toi sur la différence entre goal optionnel et essentiel (7.2) et les bonnes pratiques du split test (7.3).
