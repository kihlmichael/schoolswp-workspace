# Scripts video — Module 7 : Automation avancee

**Formation** : Maitriser FluentCRM
**Module** : M7 — Automation avancee (Premium)
**Lecons** : 6 videos + 1 exercice + 1 quiz
**Duree totale** : ~50 min
**Prerequis** : M6 (automations de base)
**Date** : 2026-03-23

---

### Lecon 7.1 — Goals : definis des objectifs dans ton funnel

**Duree** : 7 min
**Type** : Video HeyGen
**Ecran** : Face camera pour intro/conclusion, screencast FluentCRM automation builder

---

**[INTRO — face camera]**

Tu as un funnel de vente avec 5 emails. Un contact achete apres le deuxieme email. Que se passe-t-il ? Sans goal, il recoit quand meme les 3 emails suivants — ceux qui lui demandent d'acheter un truc qu'il a deja achete. Pas ideal. Les Goals dans FluentCRM resolvent exactement ce probleme. Dans cette lecon, tu apprends a poser des objectifs dans tes automations pour que les contacts sortent du funnel au bon moment.

**[ECRAN — screencast FluentCRM > Automations]**

[Ouvre une automation existante dans le builder visuel]

Etape 1 : ouvre une automation existante ou cree-en une nouvelle. On va travailler sur un funnel de vente classique — une sequence d'emails qui pousse vers l'achat d'une formation premium.

[Montre la barre laterale avec les blocs disponibles]

Etape 2 : dans la barre laterale du builder, cherche le bloc "Goal". Tu le trouves dans la categorie "Internal Actions". Fais-le glisser dans ton automation, a l'endroit ou tu veux que l'objectif soit evalue.

[Place le bloc Goal apres une sequence de 3 emails]

Etape 3 : place le goal apres ta sequence d'emails de vente. L'idee : si le contact atteint cet objectif avant d'avoir recu tous les emails, il saute directement au goal et ignore les etapes intermediaires.

**[ECRAN — screencast configuration du Goal]**

[Clique sur le bloc Goal pour ouvrir sa configuration]

Etape 4 : configure le goal. Tu dois definir deux choses. D'abord, la condition : quel evenement declenche l'objectif ? Pour un funnel de vente, c'est generalement un tag. Par exemple : "a-achete-premium". Quand FluentCRM detecte ce tag sur le contact, l'objectif est atteint.

[Montre le champ de selection de la condition]

Tu peux choisir parmi plusieurs conditions : tag applique, liste rejointe, champ personnalise modifie. Pour un achat, le tag est le plus fiable — tu le poses via ton plugin e-commerce ou manuellement.

[Montre l'option "Benchmark"]

Etape 5 : le parametre "Benchmark". C'est le terme FluentCRM pour dire : ce goal sert aussi de point d'entree. Si tu coches cette option, un contact qui recoit le tag "a-achete-premium" peut entrer dans l'automation directement a ce point, meme s'il n'etait pas dans le funnel avant. On reviendra la-dessus dans la lecon suivante.

**[ECRAN — screencast test du comportement]**

[Montre un contact dans le funnel qui recoit le tag]

Etape 6 : voyons ce qui se passe concretement. Un contact entre dans ton funnel. Il recoit l'email 1, puis l'email 2. Entre l'email 2 et l'email 3, il achete la formation. Ton plugin e-commerce — WooCommerce, TutorLMS, peu importe — pose le tag "a-achete-premium".

[Montre le contact qui saute au Goal dans le builder]

FluentCRM detecte le tag. Le contact saute directement au goal. Les emails 3, 4 et 5 ne sont jamais envoyes. Le contact continue l'automation apres le goal — par exemple, vers un email de bienvenue ou un onboarding.

**[TRANSITION — face camera]**

Les goals sont le mecanisme central pour gerer les parcours non lineaires dans tes funnels. Sans eux, tes automations restent rigides — tout le monde recoit tout, dans l'ordre. Avec eux, chaque contact avance a son rythme. Dans la prochaine lecon, on voit la difference entre un goal optionnel et un goal essentiel — et pourquoi ca change completement le comportement de ton automation.

---

**Points cles** :
- Un Goal = un point de controle dans ton automation qui detecte si un objectif est atteint
- Conditions possibles : tag applique, liste rejointe, champ personnalise
- Le contact saute directement au goal quand la condition est remplie — les etapes intermediaires sont ignorees
- Benchmark = le goal peut servir de point d'entree dans l'automation
- Cas d'usage principal : sortir un acheteur d'un funnel de vente

**Mots cles SEO** : FluentCRM goal automation, funnel FluentCRM, objectif automation email, FluentCRM benchmark

---

### Lecon 7.2 — Goal optionnel vs essentiel : quand utiliser chaque type

**Duree** : 6 min
**Type** : Video HeyGen
**Ecran** : Face camera pour intro/conclusion, screencast FluentCRM automation builder

---

**[INTRO — face camera]**

Dans la lecon precedente, tu as pose un goal dans ton automation. Mais FluentCRM te propose deux modes pour chaque goal : "Can be achieved by contact at any time" et "Must be achieved to proceed". Ce n'est pas un detail — ca change completement le comportement de ton funnel. Dans cette lecon, on clarifie la difference et tu sauras exactement quand utiliser chaque mode.

**[ECRAN — screencast FluentCRM > Automation builder]**

[Ouvre un goal existant, montre les deux options]

Voici les deux modes d'un goal dans FluentCRM.

Mode 1 : "Can be achieved at any time" — le goal optionnel. Le contact avance dans l'automation normalement, etape par etape. Si a un moment il remplit la condition du goal, il saute directement au goal. Mais s'il ne la remplit jamais, il continue quand meme — il passe le goal sans s'arreter.

Mode 2 : "Must be achieved to proceed" — le goal essentiel. Le contact avance dans l'automation jusqu'au goal. S'il n'a pas rempli la condition, il s'arrete. Il reste bloque au goal tant que la condition n'est pas remplie. Aucune etape suivante ne sera executee.

**[ECRAN — slide "Comparaison visuelle"]**

[Montre deux schemas cote a cote]

Schema 1 — goal optionnel. Le contact entre. Email 1, email 2, email 3. A n'importe quel moment, s'il achete, il saute au goal. S'il n'achete jamais, il traverse le goal et continue. Par exemple, il recoit un email de conclusion ou un feedback.

Schema 2 — goal essentiel. Le contact entre. Email 1, email 2, email 3. Il arrive au goal. S'il n'a pas achete, il s'arrete la. Pas d'email de conclusion, pas de suite. Il attend indefiniment — jusqu'a ce que la condition soit remplie ou que tu le retires manuellement de l'automation.

**[ECRAN — screencast cas concret 1 : funnel de vente]**

[Montre un funnel de vente avec un goal optionnel]

Cas concret : funnel de vente post-formation. Tu as une sequence de 5 emails qui propose la formation premium. Le goal "a-achete-premium" est en mode optionnel.

Pourquoi optionnel ? Parce que meme si le contact n'achete pas, tu veux qu'il continue. Apres le goal, tu places un branchement conditionnel : s'il a achete, onboarding. S'il n'a pas achete, email de feedback pour comprendre pourquoi.

**[ECRAN — screencast cas concret 2 : prerequis obligatoire]**

[Montre une automation avec un goal essentiel]

Cas concret : onboarding avec prerequis. Tu formes tes utilisateurs a configurer FluentCRM. L'etape 3 de ton onboarding necessite que l'utilisateur ait connecte son domaine email. Le goal "domaine-configure" est en mode essentiel.

Pourquoi essentiel ? Parce que les etapes suivantes n'ont aucun sens sans le domaine. Envoyer un email "configure tes premiers templates" a quelqu'un qui n'a pas encore de domaine, c'est du bruit. Le goal essentiel bloque la progression tant que le prerequis n'est pas rempli.

**[ECRAN — slide "Regle de decision"]**

[Montre un arbre de decision simple]

La regle est simple. Pose-toi la question : est-ce que la suite de l'automation a du sens si le goal n'est pas atteint ?

Si oui — goal optionnel. Le contact continue quoi qu'il arrive.
Si non — goal essentiel. Le contact attend.

**[TRANSITION — face camera]**

Tu sais maintenant choisir entre les deux modes de goal. Retiens : optionnel pour les funnels de vente ou tu veux gerer les deux cas (acheteur et non-acheteur), essentiel pour les prerequis obligatoires. Dans la prochaine lecon, on passe aux split tests A/B directement dans tes automations.

---

**Points cles** :
- Goal optionnel ("Can be achieved at any time") : le contact continue meme si le goal n'est pas atteint
- Goal essentiel ("Must be achieved to proceed") : le contact est bloque tant que la condition n'est pas remplie
- Funnel de vente = goal optionnel (tu geres acheteurs et non-acheteurs)
- Prerequis obligatoire = goal essentiel (la suite n'a pas de sens sans)
- Regle : est-ce que la suite a du sens si le goal n'est pas atteint ?

**Mots cles SEO** : FluentCRM goal optionnel, goal essentiel FluentCRM, benchmark automation, funnel automation WordPress

---

### Lecon 7.3 — Split test A/B dans tes automations

**Duree** : 7 min
**Type** : Video HeyGen
**Ecran** : Face camera pour intro/conclusion, screencast FluentCRM automation builder

---

**[INTRO — face camera]**

Tu envoies une sequence de vente. Tu veux savoir si un email avec une video performe mieux qu'un email texte classique. Ou si une ligne d'objet directe convertit mieux qu'une ligne avec une question. Le split test A/B dans les automations FluentCRM te donne la reponse. Dans cette lecon, tu mets en place ton premier test directement dans le builder visuel.

**[ECRAN — screencast FluentCRM > Automation builder]**

[Ouvre une automation, montre la barre laterale]

Etape 1 : dans le builder d'automation, cherche le bloc "Split" ou "A/B Testing" dans les actions disponibles. Ce bloc divise ton flux en deux branches (ou plus) et repartit les contacts selon un pourcentage que tu definis.

[Ajoute le bloc Split dans l'automation]

Etape 2 : place le bloc a l'endroit ou tu veux tester. Typiquement, juste avant l'envoi d'un email. Le bloc va creer deux chemins : chemin A et chemin B.

**[ECRAN — screencast configuration du split test]**

[Montre la configuration du bloc]

Etape 3 : configure la repartition. Par defaut, c'est 50/50. La moitie des contacts prend le chemin A, l'autre moitie le chemin B. Tu peux ajuster — 70/30, 80/20 — mais pour un vrai test, 50/50 est la norme.

[Montre le chemin A avec un email texte]

Etape 4 : configure le chemin A. Place un bloc email avec ta version "texte classique". Objet, corps du mail, CTA — ta version de reference.

[Montre le chemin B avec un email contenant une video]

Etape 5 : configure le chemin B. Place un bloc email avec ta version "video". Meme objet ou objet different — ca depend de ce que tu testes. Si tu testes le format du contenu, garde le meme objet. Si tu testes l'objet, garde le meme contenu.

Important : ne teste qu'une variable a la fois. Si tu changes l'objet ET le contenu, tu ne sauras pas ce qui a fait la difference.

**[ECRAN — screencast convergence apres le test]**

[Montre les deux chemins qui convergent vers la suite du funnel]

Etape 6 : apres le split test, les deux chemins doivent converger. Les contacts des deux branches continuent dans le meme funnel. Le test porte sur un email, pas sur tout le parcours.

[Montre comment relier les deux branches au meme bloc suivant]

Connecte la fin du chemin A et la fin du chemin B au meme bloc. Par exemple, un delai de 24 heures puis le prochain email de la sequence.

**[ECRAN — screencast lecture des resultats]**

[Montre les statistiques de l'automation]

Etape 7 : lecture des resultats. Apres quelques jours — et suffisamment de contacts passes dans le test — compare les metriques. Taux d'ouverture si tu as teste l'objet. Taux de clic si tu as teste le contenu. Taux de conversion si tu as un goal apres le test.

[Montre les taux d'ouverture et de clic des deux variantes]

FluentCRM affiche les stats par email. Variante A : 38% d'ouverture, 12% de clic. Variante B : 42% d'ouverture, 18% de clic. La version video gagne sur les deux metriques.

**[ECRAN — slide "Bonnes pratiques split test"]**

[Montre une liste]

Quelques regles pour des tests fiables.

Un : attends au moins 200 contacts par branche avant de conclure. Avec 20 contacts, les resultats ne veulent rien dire.

Deux : ne teste qu'une variable. Objet OU contenu OU CTA. Pas tout en meme temps.

Trois : definis ton critere de succes avant le test. "Je cherche a maximiser le taux de clic" — pas "je verrai bien".

Quatre : une fois le gagnant identifie, supprime la variante perdante et garde la gagnante comme email definitif.

**[TRANSITION — face camera]**

Tu sais maintenant poser un split test A/B dans tes automations FluentCRM. Le test dans l'automation est plus puissant que le test classique sur une campagne unique — parce qu'il tourne en continu, avec chaque nouveau contact qui entre dans le funnel. Dans la prochaine lecon, on va au-dela du A/B avec les conditionals multi-chemins.

---

**Points cles** :
- Le bloc Split divise le flux en deux branches avec un pourcentage configurable
- 50/50 est la repartition standard pour un test fiable
- Ne tester qu'une variable a la fois (objet, contenu, ou CTA)
- Minimum 200 contacts par branche pour des resultats significatifs
- Le split test en automation tourne en continu — chaque nouveau contact est teste

**Mots cles SEO** : split test FluentCRM, A/B testing automation email, test email WordPress, FluentCRM automation split

---

### Lecon 7.4 — Multi-path conditionals : plus de 2 chemins

**Duree** : 6 min
**Type** : Video HeyGen
**Ecran** : Face camera pour intro/conclusion, screencast FluentCRM automation builder

---

**[INTRO — face camera]**

Un branchement conditionnel classique, c'est oui ou non. Le contact a le tag, ou il ne l'a pas. Mais dans un vrai funnel, tu as souvent plus de deux scenarios. Un contact peut etre client premium, client standard, ou prospect. Il peut etre inscrit depuis moins de 7 jours, entre 7 et 30 jours, ou plus de 30 jours. Les conditionals multi-chemins dans FluentCRM gerent ces cas. Dans cette lecon, tu construis un branchement a 3 chemins ou plus.

**[ECRAN — screencast FluentCRM > Automation builder]**

[Ouvre le builder, montre le bloc conditionnel]

Etape 1 : dans le builder, ajoute un bloc conditionnel. C'est le meme bloc que tu utilises pour un simple oui/non, mais on va l'etendre.

[Montre la configuration du premier chemin]

Etape 2 : configure la premiere condition. Par exemple : "a le tag client-premium". Les contacts qui remplissent cette condition prennent le chemin 1.

[Montre comment ajouter un deuxieme chemin conditionnel]

Etape 3 : ajoute un deuxieme bloc conditionnel dans la branche "non" du premier. Condition : "a le tag client-standard". Les contacts qui remplissent cette condition prennent le chemin 2.

[Montre la branche "non" du deuxieme conditionnel]

Etape 4 : la branche "non" du deuxieme conditionnel, c'est ton chemin 3 — les prospects. Ceux qui ne sont ni premium ni standard.

**[ECRAN — slide "Schema multi-path"]**

[Montre le schema en arbre]

Visuellement, ca donne un arbre. L'entree unique se divise en 3 branches.

Branche 1 : client premium — recoit un email d'upsell vers le coaching.
Branche 2 : client standard — recoit un email d'upgrade vers le premium.
Branche 3 : prospect — recoit un email de vente vers l'offre standard.

Chaque branche a son propre contenu, son propre ton, ses propres CTA. Un seul funnel gere les trois segments.

**[ECRAN — screencast construction du multi-path]**

[Construit les 3 branches en direct]

[Chemin 1 : place un email "Coaching individuel — places limitees"]

Voila le chemin premium. Email personnalise, ton exclusif, offre de coaching.

[Chemin 2 : place un email "Passe au premium — 30% ce mois"]

Chemin standard. Mise en avant des benefices du premium, avec une offre limitee.

[Chemin 3 : place un email "Decouvre la formation — essai gratuit"]

Chemin prospect. Approche pedagogique, lien vers un module gratuit ou une demo.

**[ECRAN — screencast convergence]**

[Montre les 3 branches qui convergent vers un delai commun]

Etape 5 : apres chaque branche, fais converger les chemins. Les 3 branches se reconnectent au meme point — par exemple, un delai de 48 heures avant le prochain email commun.

**[ECRAN — slide "Conseils pratiques"]**

[Montre une liste]

Premier conseil : limite-toi a 3 ou 4 chemins maximum. Au-dela, l'automation devient illisible et difficile a maintenir.

Deuxieme conseil : nomme tes blocs conditionnels clairement. "Est client premium ?", "Est client standard ?" — pas "Condition 1", "Condition 2".

Troisieme conseil : pense a l'ordre. Place la condition la plus restrictive en premier. Si tu testes "a le tag client" avant "a le tag client-premium", le premium sera capture par la premiere condition et n'atteindra jamais la deuxieme.

**[TRANSITION — face camera]**

Tu sais maintenant creer des parcours multi-chemins dans tes automations. L'idee centrale : un seul funnel, plusieurs segments, chacun avec son contenu adapte. Dans la prochaine lecon, on explore les triggers avances — anniversaire, changement de champ personnalise, suppression de tag.

---

**Points cles** :
- Les conditionals multi-chemins = enchainer des blocs conditionnels pour creer 3+ branches
- Chaque branche a son propre contenu et ses propres CTA
- Limiter a 3-4 chemins pour garder l'automation lisible
- Placer la condition la plus restrictive en premier
- Toujours nommer les blocs clairement

**Mots cles SEO** : FluentCRM conditional, multi-path automation, segmentation automation WordPress, branchement conditionnel email

---

### Lecon 7.5 — Triggers avances : birthday, company, custom field change

**Duree** : 6 min
**Type** : Video HeyGen
**Ecran** : Face camera pour intro/conclusion, screencast FluentCRM automation builder

---

**[INTRO — face camera]**

Jusqu'ici, tu as declenche tes automations avec des triggers classiques : ajout de tag, inscription a une liste, soumission de formulaire. FluentCRM propose des triggers plus specifiques qui ouvrent de nouveaux cas d'usage. Dans cette lecon, on couvre trois triggers avances : l'anniversaire, le changement de champ personnalise, et la suppression de tag.

**[ECRAN — screencast FluentCRM > Automations > Nouveau trigger]**

[Montre la liste des triggers disponibles]

Voici la liste complete des triggers dans FluentCRM. Tu connais deja les premiers : "Tag Applied", "List Applied", "Form Submitted". Descendons plus bas.

**[ECRAN — screencast trigger Birthday]**

[Selectionne le trigger "Contact Birthday"]

Trigger 1 : Contact Birthday. Ce trigger se declenche automatiquement a la date d'anniversaire du contact. Pour qu'il fonctionne, le champ "Date of Birth" doit etre renseigne dans la fiche du contact.

[Montre la configuration du trigger]

La configuration est simple. Tu choisis combien de jours avant l'anniversaire le trigger se declenche. Zero pour le jour meme. Un pour la veille. Sept pour une semaine avant.

[Montre un email d'anniversaire type]

Cas d'usage schoolsWP : tu formes des coachs en ligne. Chaque annee, a l'anniversaire de ton client, tu envoies un email personnalise avec un code promo de 20% sur ta prochaine formation. C'est un geste simple qui renforce la relation et genere des ventes recurrentes.

**[ECRAN — screencast trigger Custom Field Change]**

[Revient a la liste des triggers, selectionne "Custom Field Changed"]

Trigger 2 : Custom Field Changed. Ce trigger se declenche quand la valeur d'un champ personnalise est modifiee. C'est puissant parce que les champs personnalises sont le moyen le plus flexible de stocker des donnees sur tes contacts.

[Montre la configuration : choix du champ et de la valeur]

Tu selectionnes le champ a surveiller. Par exemple : "niveau_formation" avec les valeurs "debutant", "intermediaire", "avance". Quand un contact passe de "debutant" a "intermediaire", le trigger se declenche.

[Montre un cas d'usage]

Cas d'usage : quand un etudiant termine le module 5 de ta formation, ton LMS met a jour le champ "niveau_formation" a "intermediaire". FluentCRM detecte le changement et lance une automation de felicitations + proposition du niveau avance.

**[ECRAN — screencast trigger Tag Removed]**

[Revient a la liste des triggers, selectionne "Tag Removed"]

Trigger 3 : Tag Removed. Le pendant de "Tag Applied". Ce trigger se declenche quand un tag est retire d'un contact.

[Montre la configuration]

Tu selectionnes le tag a surveiller. Par exemple : "abonne-newsletter".

[Montre un cas d'usage]

Cas d'usage : un contact se desabonne de ta newsletter. Tu retires le tag "abonne-newsletter". Le trigger "Tag Removed" se declenche et lance une automation de reengagement — un email 7 jours plus tard pour demander pourquoi il est parti, avec une offre de contenu exclusif pour le faire revenir.

Autre cas : le tag "client-actif" est retire quand un abonnement expire. Le trigger lance un funnel de win-back avec une offre de renouvellement.

**[ECRAN — slide "Resume des 3 triggers"]**

[Tableau comparatif]

Birthday : se declenche a la date d'anniversaire. Necessite le champ Date of Birth. Usage : emails personnalises, promos anniversaire.

Custom Field Changed : se declenche quand un champ personnalise est modifie. Usage : progression de formation, changement de statut, mise a jour de profil.

Tag Removed : se declenche quand un tag est retire. Usage : desabonnement, expiration, desengagement.

**[TRANSITION — face camera]**

Ces trois triggers te permettent de reagir a des evenements que les triggers classiques ne couvrent pas. L'anniversaire pour la relation, le changement de champ pour la progression, la suppression de tag pour le win-back. Dans la prochaine lecon, on voit comment importer et exporter tes automations — pour les sauvegarder, les partager, ou les dupliquer entre sites.

---

**Points cles** :
- Birthday : declenche un email X jours avant/le jour de l'anniversaire du contact
- Custom Field Changed : reagit quand la valeur d'un champ personnalise est modifiee
- Tag Removed : reagit quand un tag est retire (desabonnement, expiration)
- Chaque trigger ouvre des cas d'usage que les triggers classiques ne couvrent pas
- Le champ Date of Birth doit etre renseigne pour que Birthday fonctionne

**Mots cles SEO** : FluentCRM trigger avance, birthday email automation, custom field trigger, tag removed FluentCRM

---

### Lecon 7.6 — Importe et exporte tes automations

**Duree** : 5 min
**Type** : Video HeyGen
**Ecran** : Face camera pour intro/conclusion, screencast FluentCRM

---

**[INTRO — face camera]**

Tu as construit une automation complexe — un funnel de vente avec des goals, des split tests, des conditionals. Tu veux la sauvegarder, la dupliquer sur un autre site, ou la partager avec un client. FluentCRM permet d'exporter et d'importer des automations en JSON. Dans cette lecon, tu apprends a le faire.

**[ECRAN — screencast FluentCRM > Automations]**

[Montre la liste des automations]

Etape 1 : va dans FluentCRM, section Automations. Tu vois la liste de toutes tes automations.

**[ECRAN — screencast export]**

[Selectionne une automation, montre le menu d'actions]

Etape 2 : ouvre l'automation que tu veux exporter. Dans le builder, cherche l'option d'export. Selon la version de FluentCRM, c'est soit un bouton "Export" dans la barre d'outils, soit dans le menu "More Options" ou les trois points.

[Montre le fichier JSON telecharge]

Etape 3 : FluentCRM genere un fichier JSON qui contient toute la structure de ton automation. Les blocs, les connexions, les conditions, les delais — tout est la. Les emails eux-memes sont inclus avec leur contenu.

[Ouvre le fichier JSON dans un editeur]

Voici a quoi ressemble le fichier. Tu vois les etapes, les conditions, les templates d'email. Tu n'as pas besoin de modifier ce fichier — c'est FluentCRM qui le lit. Mais savoir que c'est du JSON standard te permet de le versionner dans Git, de le stocker dans un Drive, ou de le partager par email.

**[ECRAN — screencast import]**

[Va dans Automations > Import]

Etape 4 : pour importer, va dans la liste des automations. Cherche le bouton "Import" ou "Import Automation".

[Montre le formulaire d'import]

Etape 5 : selectionne ton fichier JSON. FluentCRM le lit et recree toute l'automation avec ses blocs, ses connexions et ses emails.

[Montre l'automation importee dans le builder]

Etape 6 : verifie l'automation importee. Tous les blocs sont la, dans le bon ordre. Mais attention a trois choses.

**[ECRAN — slide "Points de vigilance apres import"]**

[Montre une liste]

Premier point : les tags. Si ton automation reference le tag "client-premium" et que ce tag n'existe pas sur le site de destination, FluentCRM ne le creera pas automatiquement. Tu devras creer les tags manquants et les reassigner dans les blocs concernes.

Deuxieme point : les listes. Meme logique. Si l'automation ajoute des contacts a la liste "Clients VIP", cette liste doit exister sur le site de destination.

Troisieme point : les liens dans les emails. Si tes emails contiennent des liens vers ton site, ils pointent toujours vers le site d'origine. Mets-les a jour manuellement.

Quatrieme point : les integrations. Si un bloc depend d'un plugin — WooCommerce, TutorLMS — ce plugin doit etre installe et configure sur le site de destination.

**[ECRAN — screencast bonnes pratiques]**

[Montre un dossier de fichiers JSON organise]

Bonne pratique : cree un dossier dedie pour tes exports. Nomme tes fichiers avec une convention claire. Par exemple : "funnel-vente-premium-v2-2026-03.json". Date, version, nom explicite.

Autre bonne pratique : exporte tes automations avant chaque modification majeure. C'est ton systeme de sauvegarde. Si une modification casse ton funnel, tu reimportes la version precedente.

**[TRANSITION — face camera]**

Tu sais maintenant exporter, sauvegarder et reimporter tes automations. C'est un reflexe a prendre : avant chaque modification importante, exporte. Ca te prend 10 secondes et ca peut te sauver des heures de reconstruction. Dans la prochaine lecon, on met tout ensemble : tu construis un funnel d'upsell complet avec split test et goal.

---

**Points cles** :
- Export = fichier JSON contenant toute la structure de l'automation + emails
- Import recree l'automation mais ne cree pas les tags, listes ou integrations manquantes
- Verifier apres import : tags, listes, liens, plugins dependants
- Convention de nommage : nom-version-date.json
- Exporter avant chaque modification majeure = sauvegarde

**Mots cles SEO** : exporter automation FluentCRM, importer automation WordPress, backup automation email, FluentCRM JSON export

---

### Lecon 7.7 — Exercice : Cree un funnel d'upsell avec split test et goal

**Duree** : 8 min
**Type** : Exercice guide (Video HeyGen)
**Ecran** : Face camera pour intro/conclusion, screencast FluentCRM automation builder

---

**[INTRO — face camera]**

C'est l'exercice du module. Tu vas construire un funnel d'upsell complet en combinant tout ce que tu as appris : split test A/B, goal avec benchmark, et conditional multi-chemins. Le scenario : un etudiant vient de terminer ta formation gratuite sur TutorLMS. Tu veux lui proposer la formation premium. On construit ce funnel ensemble, etape par etape.

**[ECRAN — slide "Le scenario"]**

[Montre le schema du funnel]

Voici le parcours complet.

Declencheur : le contact recoit le tag "formation-gratuite-terminee" (pose automatiquement par TutorLMS).

Etape 1 : delai de 24 heures. On ne vend pas dans la seconde ou quelqu'un finit une formation.

Etape 2 : split test A/B a 50/50.
- Chemin A : email texte avec temoignages d'etudiants premium.
- Chemin B : email avec video ou tu presentes les benefices du premium.

Etape 3 : delai de 3 jours.

Etape 4 : email de relance commun aux deux branches. Rappel de l'offre + code promo limite a 48 heures.

Etape 5 : goal "a-achete-premium" en mode optionnel.

Apres le goal : conditional multi-chemins.
- Si tag "a-achete-premium" : email de bienvenue premium + ajout liste "Etudiants Premium".
- Si pas le tag : email de feedback + code promo de derniere chance.

**[ECRAN — screencast construction etape par etape]**

[Cree une nouvelle automation]

Etape 1 : cree une nouvelle automation. Nom : "Upsell post-formation gratuite". Trigger : "Tag Applied" > "formation-gratuite-terminee".

[Ajoute le delai de 24 heures]

Etape 2 : ajoute un bloc delai. 24 heures. Le contact attend une journee avant de recevoir quoi que ce soit.

[Ajoute le bloc Split 50/50]

Etape 3 : ajoute le bloc split test. Repartition 50/50.

[Configure le chemin A]

Etape 4 : chemin A. Place un bloc email. Objet : "Les etudiants premium partagent leur experience". Corps : 3 temoignages courts, un CTA vers la page de vente.

[Configure le chemin B]

Etape 5 : chemin B. Place un bloc email. Objet : "Regarde ce que le premium t'apporte — en 2 minutes". Corps : lien vers une video de presentation, meme CTA vers la page de vente.

[Fait converger les deux chemins]

Etape 6 : les deux chemins convergent vers un delai de 3 jours.

[Ajoute l'email de relance]

Etape 7 : apres le delai, place un email de relance. Objet : "Derniere chance — 20% avec le code PREMIUM20". Corps : rappel des benefices, urgence (48h), CTA.

[Ajoute le goal]

Etape 8 : place le goal "a-achete-premium". Mode : "Can be achieved at any time" — optionnel. Condition : tag "a-achete-premium" present.

Pourquoi optionnel ? Parce que tu veux gerer les deux cas : ceux qui achetent et ceux qui n'achetent pas.

[Ajoute le conditional apres le goal]

Etape 9 : apres le goal, place un bloc conditionnel. Condition : "Has tag a-achete-premium".

[Configure le chemin "oui"]

Etape 10 : chemin oui — le contact a achete. Place un email de bienvenue premium. Ajoute un bloc "Add to List" : "Etudiants Premium". Ajoute un bloc "Remove Tag" : "formation-gratuite-terminee" pour nettoyer.

[Configure le chemin "non"]

Etape 11 : chemin non — le contact n'a pas achete. Place un email de feedback. Objet : "On aimerait comprendre". Corps : 3 raisons possibles (prix, timing, contenu), un lien vers un formulaire de feedback, et un dernier code promo valable 7 jours.

**[ECRAN — screencast verification finale]**

[Vue d'ensemble de l'automation complete]

Etape 12 : verifie l'ensemble. De haut en bas : trigger tag, delai 24h, split test A/B, convergence, delai 3 jours, email relance, goal, conditional, deux chemins de sortie. Tout est connecte.

[Active l'automation]

Etape 13 : active l'automation. Elle est prete a recevoir des contacts.

**[TRANSITION — face camera]**

Bravo. Tu viens de construire un funnel d'upsell complet avec les trois mecaniques avancees de FluentCRM : split test pour optimiser, goal pour detecter l'achat, conditional pour adapter la suite. C'est exactement ce type de funnel qui tourne en arriere-plan et genere des ventes sans que tu interviennes au quotidien. Derniere etape du module : le quiz pour valider tes acquis.

---

**Points cles** :
- Funnel complet : trigger tag > delai > split test > relance > goal > conditional > 2 sorties
- Split test A/B : email texte vs email video, 50/50
- Goal optionnel : detecte l'achat sans bloquer les non-acheteurs
- Conditional apres le goal : parcours personnalise acheteur vs non-acheteur
- Nettoyage : retirer les tags obsoletes, ajouter aux bonnes listes

**Mots cles SEO** : funnel upsell FluentCRM, automation upsell WordPress, split test email funnel, FluentCRM exercice pratique

---

### Lecon 7.8 — Quiz : Valide tes acquis M7

**Duree** : 5 min
**Type** : Quiz TutorLMS (8 QCM)
**Format** : Questions affichees dans TutorLMS, pas de video

---

**Question 1** : Quel est le role principal d'un Goal dans une automation FluentCRM ?

- A) Envoyer un email automatique a une date precise
- B) Detecter si un contact a atteint un objectif et adapter son parcours en consequence ✅
- C) Supprimer un contact de l'automation apres un certain delai
- D) Creer un segment automatique base sur l'engagement

**Explication** : Un Goal surveille une condition (tag, liste, champ). Quand elle est remplie, le contact saute directement au goal, ignorant les etapes intermediaires.

---

**Question 2** : Un goal en mode "Can be achieved at any time" (optionnel) — que se passe-t-il si le contact n'atteint jamais l'objectif ?

- A) Le contact est supprime de l'automation
- B) Le contact reste bloque indefiniment au niveau du goal
- C) Le contact traverse le goal et continue l'automation normalement ✅
- D) FluentCRM envoie une notification a l'administrateur

**Explication** : En mode optionnel, le contact continue meme sans atteindre l'objectif. En mode essentiel ("Must be achieved"), il serait bloque.

---

**Question 3** : Tu configures un split test A/B dans une automation. Quelle est la meilleure pratique ?

- A) Tester l'objet, le contenu et le CTA en meme temps pour gagner du temps
- B) Ne tester qu'une seule variable a la fois pour identifier ce qui fait la difference ✅
- C) Utiliser une repartition 90/10 pour limiter les risques
- D) Attendre 10 contacts par branche avant de conclure

**Explication** : Tester une seule variable a la fois garantit des resultats exploitables. Minimum recommande : 200 contacts par branche.

---

**Question 4** : Comment creer un branchement a 3 chemins dans FluentCRM ?

- A) Utiliser le bloc "Triple Split" disponible dans les actions avancees
- B) Enchainer des blocs conditionnels : le premier filtre un segment, la branche "non" contient un deuxieme conditionnel ✅
- C) Creer 3 automations separees avec des triggers differents
- D) Utiliser un goal avec 3 conditions simultanees

**Explication** : FluentCRM n'a pas de bloc "triple split" natif. On enchaine des conditionnels : la branche "non" du premier contient le deuxieme test, et ainsi de suite.

---

**Question 5** : Le trigger "Contact Birthday" necessite que :

- A) Le contact ait un tag "birthday" applique manuellement
- B) Le champ "Date of Birth" soit renseigne dans la fiche du contact ✅
- C) L'administrateur active le module "Calendar" dans les reglages FluentCRM
- D) Le contact soit inscrit dans une liste specifique "Anniversaires"

**Explication** : Le trigger Birthday lit le champ Date of Birth. Sans cette donnee, le trigger ne se declenche jamais.

---

**Question 6** : Tu exportes une automation FluentCRM et tu l'importes sur un autre site. Qu'est-ce que FluentCRM NE recree PAS automatiquement ?

- A) Les blocs de l'automation et leurs connexions
- B) Le contenu des emails inclus dans l'automation
- C) Les tags et listes references dans l'automation ✅
- D) Les delais configures entre les etapes

**Explication** : L'import recree la structure et les emails, mais pas les tags, listes, ou integrations. Tu dois les creer manuellement sur le site de destination.

---

**Question 7** : Dans un funnel d'upsell, tu places un goal "a-achete-premium" en mode optionnel. Pourquoi optionnel plutot qu'essentiel ?

- A) Parce que le mode essentiel n'est pas compatible avec les split tests
- B) Parce que tu veux que les non-acheteurs continuent dans l'automation pour recevoir un email de feedback ✅
- C) Parce que le mode optionnel est plus rapide a configurer
- D) Parce que le mode essentiel supprime les contacts qui n'atteignent pas le goal

**Explication** : En mode optionnel, les non-acheteurs traversent le goal et continuent — tu peux leur envoyer un email de feedback ou une derniere offre. En mode essentiel, ils seraient bloques.

---

**Question 8** : Le trigger "Tag Removed" est particulierement utile pour :

- A) Ajouter automatiquement un nouveau tag en remplacement
- B) Lancer un funnel de win-back quand un abonnement expire ou qu'un contact se desabonne ✅
- C) Nettoyer la base de contacts en supprimant les inactifs
- D) Synchroniser les tags entre FluentCRM et WooCommerce

**Explication** : "Tag Removed" detecte la perte d'un statut (desabonnement, expiration). C'est le declencheur ideal pour les sequences de reengagement et de win-back.

---

**Seuil de reussite** : 6/8 (75%)

**Message de reussite** : Module 7 valide. Tu maitrises les mecaniques avancees d'automation FluentCRM : goals, split tests, conditionals multi-chemins et triggers avances. Le module 8 t'attend pour passer a la delivrabilite et au monitoring.

**Message d'echec** : Score insuffisant. Revisionne les lecons 7.1 a 7.6 avant de retenter le quiz. Concentre-toi sur la difference entre goal optionnel et essentiel (7.2) et les bonnes pratiques du split test (7.3).
