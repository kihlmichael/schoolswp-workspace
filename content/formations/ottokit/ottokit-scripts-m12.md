# Scripts vidéo - Module 12 : Monitoring, debugging et optimisation

**Formation** : Maîtriser OttoKit
**Module** : M12 - Monitoring, debugging et optimisation
**Leçons** : 7 vidéos + 1 quiz
**Durée totale** : ~45 min de vidéo
**Date** : 2026-03-30

---

## Leçon 12.1 - Workflow History : lire et comprendre les logs

**Durée** : 6 min
**Type** : Vidéo HeyGen
**Écran** : Face caméra pour intro/conclusion, screencast OttoKit History

---

**[INTRO - face caméra]**

Tes workflows tournent. Mais est-ce qu'ils tournent bien ? La seule façon de le savoir, c'est de lire les logs. OttoKit enregistre chaque exécution dans l'onglet History. C'est ta boîte noire. Aujourd'hui, on apprend à la lire.

**[ÉCRAN - screencast OttoKit dashboard]**

[Clique sur "History" dans la barre latérale gauche]

Voici l'écran History. C'est la liste de toutes les exécutions de tous tes workflows. Chaque ligne représente un "run" - une exécution complète.

[Pointe les colonnes du tableau : workflow name, status, date, duration]

Pour chaque run, tu vois :

- **Le nom du workflow** - lequel s'est déclenché
- **Le statut** - Success (vert), Failed (rouge), Running (bleu)
- **La date et l'heure** - quand exactement
- **La durée** - combien de temps l'exécution a pris

**[ÉCRAN - screencast détail d'un run]**

[Clique sur un run avec statut "Success"]
[Montre le détail : chaque étape du workflow avec ses données d'entrée et de sortie]

Quand tu cliques sur un run, tu vois le détail étape par étape. Chaque nœud du workflow affiche :

1. Les **données reçues** (input) - ce qui est arrivé dans le nœud
2. Les **données produites** (output) - ce qui en est sorti
3. Le **temps d'exécution** de chaque étape

C'est fondamental. Si quelque chose ne fonctionne pas, c'est ici que tu trouveras pourquoi.

**[ÉCRAN - screencast filtre et recherche]**

[Montre les filtres : par workflow, par statut, par date]
[Filtre par statut "Failed"]
[Filtre par workflow spécifique]

Tu peux filtrer les logs par statut, par workflow, ou par date. Si tu cherches uniquement les échecs, filtre par "Failed". Si tu veux suivre un workflow spécifique, sélectionne-le dans la liste.

**[ÉCRAN - screencast workflow "Inscription → email → CRM"]**

[Ouvre le détail d'un run du workflow d'inscription]
[Montre le trigger "User Registered", puis l'action "Send Email", puis l'action "Add to CRM"]
[Pointe les données transmises entre chaque étape]

Prenons un exemple réel. Ce workflow se déclenche quand un utilisateur s'inscrit sur le site schoolsWP. Il envoie un email de bienvenue, puis ajoute le contact dans FluentCRM. Dans les logs, tu vois exactement quel email a été envoyé, à quelle adresse, et quel contact a été créé.

**[TRANSITION - face caméra]**

Tu sais maintenant lire les logs. Dans la prochaine leçon, on va voir les 5 erreurs les plus fréquentes - et comment les repérer dans ces mêmes logs.

---

**Points clés**
- L'onglet History enregistre chaque exécution de chaque workflow
- Trois statuts : Success (vert), Failed (rouge), Running (bleu)
- Le détail d'un run montre les données d'entrée et de sortie de chaque étape
- Les filtres permettent d'isoler rapidement les échecs ou un workflow spécifique

**Mots-clés SEO**
- OttoKit workflow history
- OttoKit logs automatisation
- monitorer workflow OttoKit
- debug OttoKit WordPress

---

## Leçon 12.2 - Identifier une erreur : les 5 causes les plus fréquentes

**Durée** : 6 min
**Type** : Vidéo HeyGen
**Écran** : Face caméra pour intro/conclusion, slides pour chaque type d'erreur, screencast OttoKit

---

**[INTRO - face caméra]**

Un workflow qui échoue, ça arrive. Ce n'est pas un problème - à condition que tu saches diagnostiquer la cause. En 3 ans d'automatisation WordPress, j'ai identifié 5 erreurs qui reviennent dans 90% des cas. On les passe en revue.

**[ÉCRAN - slide "Erreur 1 : Connexion expirée"]**

**Cause 1 : la connexion a expiré.**

C'est la plus courante. Tu as connecté Google Sheets ou Mailchimp il y a 3 mois. Depuis, le token d'authentification a expiré. OttoKit ne peut plus communiquer avec l'app.

Symptôme : le message d'erreur contient "401 Unauthorized" ou "Invalid credentials".

Solution : va dans Connections, déconnecte l'app concernée, et reconnecte-la.

**[ÉCRAN - slide "Erreur 2 : Champ manquant ou vide"]**

**Cause 2 : un champ obligatoire est vide.**

Tu as configuré une action "Envoyer un email" avec le champ `billing_email`. Mais cette fois, le trigger n'a pas retourné d'email - le champ est vide. L'action échoue.

Symptôme : "Required field is empty" ou "Missing value".

Solution : ajoute un filtre avant l'action pour vérifier que le champ existe. Ou configure une valeur par défaut.

**[ÉCRAN - slide "Erreur 3 : Limite API atteinte"]**

**Cause 3 : la limite de l'API est atteinte (rate limit).**

Chaque service a des limites. Si tu envoies 200 requêtes à Google Sheets en 1 minute, Google te bloque temporairement.

Symptôme : "429 Too Many Requests" ou "Rate limit exceeded".

Solution : ajoute un délai entre les actions, ou réduis le volume de données traitées par run.

**[ÉCRAN - slide "Erreur 4 : Format de données invalide"]**

**Cause 4 : le format de données est invalide.**

Tu envoies un texte là où l'API attend un nombre. Ou une date au format "30/03/2026" alors que l'app attend "2026-03-30".

Symptôme : "Invalid format", "Type mismatch" ou "Cannot parse".

Solution : vérifie le format attendu dans la documentation de l'app et utilise les fonctions de formatage d'OttoKit.

**[ÉCRAN - slide "Erreur 5 : Permission refusée"]**

**Cause 5 : permissions insuffisantes.**

L'app est connectée, mais avec un compte qui n'a pas les droits nécessaires. Par exemple, un compte Google qui n'a pas accès au spreadsheet visé.

Symptôme : "403 Forbidden" ou "Access denied".

Solution : vérifie que le compte utilisé a les permissions nécessaires sur la ressource cible.

**[ÉCRAN - screencast OttoKit History - run Failed]**

[Ouvre un run en échec]
[Montre le message d'erreur dans le détail]
[Pointe l'étape exacte qui a échoué (en rouge)]

Dans les logs, l'étape en échec est marquée en rouge. Clique dessus pour voir le message d'erreur. C'est là que tu identifies la cause. Compare le message avec les 5 cas qu'on vient de voir.

**[TRANSITION - face caméra]**

Tu connais les 5 erreurs. Maintenant, on va voir comment corriger et relancer un workflow sans repartir de zéro.

---

**Points clés**
- 5 causes couvrent 90% des erreurs : connexion expirée, champ manquant, rate limit, format invalide, permission
- Le message d'erreur dans les logs indique presque toujours la cause
- L'étape en échec est marquée en rouge dans le détail du run
- Chaque cause a une solution précise et rapide

**Mots-clés SEO**
- OttoKit erreur workflow
- debug automatisation WordPress
- OttoKit connexion expirée
- OttoKit 401 403 429 erreur

---

## Leçon 12.3 - Auto-replay et replay manuel : corriger et relancer

**Durée** : 6 min
**Type** : Vidéo HeyGen
**Écran** : Face caméra pour intro/conclusion, screencast OttoKit History et replay

---

**[INTRO - face caméra]**

Un workflow a échoué. Tu as identifié la cause. Maintenant, tu veux relancer cette exécution - sans attendre qu'un nouvel événement se produise. OttoKit propose deux mécanismes : l'auto-replay et le replay manuel.

**[ÉCRAN - slide "Auto-replay vs replay manuel"]**

| | Auto-replay | Replay manuel |
|---|---|---|
| Déclenchement | Automatique après échec | Toi, quand tu décides |
| Tentatives | Jusqu'à 6 tentatives | 1 tentative |
| Données | Identiques au run original | Modifiables avant relance |
| Cas d'usage | Erreur temporaire (timeout, rate limit) | Erreur de données (email invalide) |

L'auto-replay est utile pour les erreurs temporaires. L'API est surchargée ? OttoKit réessaie automatiquement. Mais si le problème vient des données - un email mal formaté par exemple - l'auto-replay va échouer 6 fois de suite avec la même erreur.

**[ÉCRAN - screencast OttoKit - configuration auto-replay]**

[Ouvre les paramètres d'un workflow]
[Montre l'option auto-replay : enable/disable]
[Montre le nombre de tentatives configurable]

L'auto-replay se configure dans les paramètres du workflow. Tu peux l'activer ou le désactiver. Quand c'est activé, OttoKit réessaie automatiquement avec un délai croissant entre chaque tentative.

**[ÉCRAN - screencast OttoKit - replay manuel]**

[Va dans History]
[Sélectionne un run en échec]
[Clique sur le bouton "Replay"]
[Montre l'écran de modification des données]

Le replay manuel, c'est différent. Tu ouvres un run en échec dans l'History. Tu cliques sur "Replay". Et là, OttoKit te montre les données du run original. Tu peux les modifier avant de relancer.

**[ÉCRAN - screencast correction et relance]**

[Montre les données du run : un champ email contient "jean@gmailcom" (manque le point)]
[Corrige le champ en "jean@gmail.com"]
[Clique sur "Replay"]
[Montre le nouveau run qui passe en "Success"]

Exemple concret. Ce run a échoué parce que l'email du client était mal saisi : "jean@gmailcom" au lieu de "jean@gmail.com". Avec le replay manuel, tu corriges le champ et tu relances. Le workflow s'exécute correctement.

**[ÉCRAN - slide "Quand utiliser quoi"]**

- **Erreur temporaire** (timeout, rate limit, serveur indisponible) → laisse l'auto-replay gérer
- **Erreur de données** (email invalide, champ manquant, format incorrect) → replay manuel avec correction
- **Erreur de configuration** (connexion expirée, mauvais mapping) → corrige d'abord le workflow, puis replay

**[TRANSITION - face caméra]**

Le replay, c'est ton filet de sécurité. Aucune exécution n'est perdue. Dans la prochaine leçon, on va aller plus loin : se faire alerter avant même d'ouvrir les logs.

---

**Points clés**
- Auto-replay : jusqu'à 6 tentatives automatiques, idéal pour les erreurs temporaires
- Replay manuel : permet de modifier les données avant de relancer
- Le replay évite de perdre des exécutions - chaque run peut être rejoué
- Toujours corriger la cause avant de rejouer (sinon le même échec se répète)

**Mots-clés SEO**
- OttoKit replay workflow
- OttoKit auto-replay
- relancer workflow échec OttoKit
- corriger erreur OttoKit automatisation

---

## Leçon 12.4 - Notifications : sois alerté avant que ça casse

**Durée** : 5 min
**Type** : Vidéo HeyGen
**Écran** : Face caméra pour intro/conclusion, screencast OttoKit notifications

---

**[INTRO - face caméra]**

Tu ne peux pas surveiller tes workflows en permanence. Tu as autre chose à faire. C'est pour ça qu'OttoKit peut t'envoyer des alertes quand quelque chose échoue. Tu configures une fois, et tu es prévenu automatiquement.

**[ÉCRAN - screencast OttoKit Settings → Notifications]**

[Ouvre Settings dans la barre latérale]
[Clique sur la section Notifications]
[Montre les options disponibles]

Dans les settings d'OttoKit, tu trouves la section Notifications. Ici, tu configures comment tu veux être alerté.

**[ÉCRAN - screencast configuration email]**

[Active les notifications par email]
[Montre le champ d'adresse email]
[Sélectionne les événements : "Workflow Failed"]

Première option : l'email. Tu entres ton adresse, tu sélectionnes les événements qui t'intéressent - en général, "Workflow Failed". À chaque échec, tu reçois un email avec le nom du workflow, l'erreur, et un lien direct vers le run.

**[ÉCRAN - screencast configuration avancée]**

[Montre les options supplémentaires : alerte par workflow, fréquence]

Tu peux aller plus loin. Certaines configurations permettent de :

- Recevoir des alertes uniquement pour certains workflows critiques
- Grouper les alertes pour éviter d'être noyé (un résumé toutes les heures plutôt qu'un email par échec)

**[ÉCRAN - slide "Stratégie d'alerte recommandée"]**

Voici ce que je recommande :

1. **Email immédiat** pour les workflows critiques (paiement, inscription, livraison)
2. **Résumé quotidien** pour les workflows moins urgents (synchronisation de données, nettoyage)
3. **Pas d'alerte** pour les workflows de test en cours de développement

L'objectif : être prévenu des vrais problèmes sans être submergé par le bruit.

**[ÉCRAN - screencast création d'un workflow d'alerte custom]**

[Montre un workflow OttoKit dont le trigger est "Workflow Failed"]
[L'action envoie un message WhatsApp ou Slack avec les détails de l'échec]

Astuce avancée : tu peux créer un workflow OttoKit dont le trigger est l'échec d'un autre workflow. Ce méta-workflow peut t'envoyer un message WhatsApp, poster dans Slack, ou même créer une tâche dans Notion. Tu contrôles entièrement le canal d'alerte.

**[TRANSITION - face caméra]**

Les alertes sont en place. Passons à un sujet qui touche directement ton portefeuille : optimiser ta consommation de tasks.

---

**Points clés**
- Les notifications évitent de découvrir un problème trop tard
- Email par défaut pour "Workflow Failed" - la configuration minimum
- Un méta-workflow peut alerter sur n'importe quel canal (Slack, WhatsApp, Notion)
- Différencier les workflows critiques des workflows secondaires

**Mots-clés SEO**
- OttoKit notification échec
- alerte workflow OttoKit
- monitoring automatisation WordPress
- OttoKit WhatsApp notification

---

## Leçon 12.5 - Optimiser sa consommation de tasks

**Durée** : 6 min
**Type** : Vidéo HeyGen
**Écran** : Face caméra pour intro/conclusion, slides compteur tasks, screencast OttoKit

---

**[INTRO - face caméra]**

Chaque action exécutée par OttoKit consomme un "task". Et ton forfait a une limite. Donc si tu veux automatiser beaucoup sans exploser le compteur, tu dois comprendre ce qui consomme et comment optimiser.

**[ÉCRAN - slide "Ce qui compte comme task"]**

Règle numéro un : **chaque action exécutée = 1 task**.

Ce qui consomme :
- Chaque action dans un workflow qui s'exécute = 1 task
- Si ton workflow a 5 actions et se déclenche 10 fois → 50 tasks

Ce qui ne consomme PAS :
- Le trigger (l'événement déclencheur) = 0 task
- Les filtres et conditions = 0 task
- Un workflow en pause = 0 task
- Un workflow actif qui ne se déclenche pas = 0 task

**[ÉCRAN - slide "Exemple de calcul"]**

Prenons un exemple. Tu as un workflow "Nouvelle commande WooCommerce" avec 4 actions :

1. Ajouter le client dans FluentCRM → 1 task
2. Envoyer un email de confirmation → 1 task
3. Ajouter une ligne dans Google Sheets → 1 task
4. Envoyer un message Slack → 1 task

Total par commande : 4 tasks. À 100 commandes par mois : 400 tasks.

**[ÉCRAN - screencast OttoKit dashboard usage]**

[Montre le compteur de tasks dans le dashboard]
[Pointe le forfait actuel et la consommation]

Dans ton dashboard, tu vois ta consommation en temps réel. Le compteur indique combien de tasks tu as utilisées sur le mois et combien il t'en reste.

**[ÉCRAN - slide "5 stratégies d'économie"]**

Voici 5 stratégies pour optimiser :

**1. Filtre avant d'agir.** Si tu as un workflow WooCommerce, ajoute un filtre pour ignorer les commandes de test. Les filtres ne consomment pas de task, mais ils évitent de déclencher des actions inutiles.

**2. Combine les actions.** Plutôt que d'envoyer 3 webhooks séparément, envoie un seul webhook avec toutes les données. 1 task au lieu de 3.

**3. Désactive les workflows en développement.** Un workflow actif avec un trigger planifié consomme des tasks à chaque vérification qui détecte quelque chose. Mets-le en pause tant que tu testes.

**4. Utilise les conditions intelligemment.** Avant l'action "Envoyer un SMS", vérifie que le numéro de téléphone existe. Si le champ est vide, l'action ne s'exécute pas → 0 task.

**5. Consolide les workflows redondants.** Si tu as 3 workflows qui font la même chose pour 3 formulaires différents, combine-les en un seul avec un routeur.

**[ÉCRAN - screencast workflow WooCommerce avec filtre]**

[Ouvre un workflow réel]
[Montre un nœud Filter après le trigger WooCommerce]
[Le filtre exclut les commandes avec status "test" ou montant = 0]
[Montre que les commandes de test ne déclenchent pas les actions en aval]

Exemple schoolsWP : ce workflow gère les inscriptions aux formations. On a ajouté un filtre qui exclut les commandes de test de WooCommerce - montant à zéro ou email contenant "test@". Résultat : on économise environ 20% de tasks chaque mois.

**[TRANSITION - face caméra]**

Tu sais maintenant compter et optimiser tes tasks. Prochaine étape : tester tes workflows sans risquer de casser ta production.

---

**Points clés**
- 1 action exécutée = 1 task ; triggers et filtres = 0 task
- Toujours filtrer les données de test avant les actions
- Combiner les actions et consolider les workflows redondants pour économiser
- Surveiller le compteur de tasks dans le dashboard chaque semaine

**Mots-clés SEO**
- OttoKit tasks consommation
- optimiser tasks OttoKit
- OttoKit pricing tasks
- économiser automatisation OttoKit

---

## Leçon 12.6 - Tester en staging : ne jamais casser la production

**Durée** : 5 min
**Type** : Vidéo HeyGen
**Écran** : Face caméra pour intro/conclusion, slides stratégie de test, screencast OttoKit

---

**[INTRO - face caméra]**

Tu viens de créer un workflow qui envoie un email à chaque nouveau client. Avant de l'activer pour de vrai, tu veux être sûr qu'il fonctionne correctement. Parce qu'un email de bienvenue avec des champs vides, ça donne une mauvaise première impression. Voyons comment tester sans risque.

**[ÉCRAN - slide "Les 3 niveaux de test"]**

Il y a 3 niveaux de test pour un workflow OttoKit :

**Niveau 1 - Fetch Data.** Quand tu configures un trigger ou une action, le bouton "Fetch Data" récupère des données réelles. Ça te permet de vérifier que les champs sont corrects. C'est le test le plus basique.

**Niveau 2 - Run manuel avec données de test.** Tu actives le workflow, tu déclenches manuellement l'événement (par exemple, tu crées une commande de test dans WooCommerce), et tu vérifies dans l'History que chaque étape s'exécute correctement.

**Niveau 3 - Environnement de staging.** Tu dupliques ton workflow, tu le connectes à un site de staging (une copie de ton site), et tu testes là-bas. Aucun impact sur la production.

**[ÉCRAN - screencast préparation d'un test]**

[Montre un workflow en brouillon]
[Montre le bouton "Fetch Data" sur le trigger]
[Clique et montre les données récupérées]

Le niveau 1, tu le connais déjà - c'est le Fetch Data. Ça confirme que la connexion fonctionne et que les données arrivent.

**[ÉCRAN - screencast test avec données réelles]**

[Active le workflow]
[Va dans WooCommerce et crée une commande de test - produit à 0 euros, email de test]
[Revient dans OttoKit History]
[Montre le run déclenché avec les données de test]
[Vérifie chaque étape]

Le niveau 2 : tu crées une vraie commande de test. Utilise un email de test (pas celui d'un vrai client), un produit à 0 euros, et un nom reconnaissable comme "Test Workflow". Ensuite, vérifie dans l'History que chaque étape s'est exécutée correctement.

**[ÉCRAN - slide "Bonnes pratiques de test"]**

Quelques règles de prudence :

- **Ne teste jamais avec de vraies données clients.** Utilise des emails de test.
- **Mets un filtre anti-test en production.** On l'a vu dans la leçon précédente - exclure les commandes à 0 euros ou les emails "test@".
- **Teste après chaque modification.** Tu changes un champ, tu retestes. Pas dans 3 jours.
- **Documente tes tests.** Note ce que tu as testé et le résultat. Quand un workflow casse 2 mois plus tard, tu sauras ce qui fonctionnait avant.

**[ÉCRAN - slide "Publication progressive"]**

Quand tu es satisfait du test :

1. Active le workflow
2. Surveille les 5 premiers runs dans l'History
3. Si tout est bon, passe à autre chose
4. Reviens vérifier le lendemain

Pas besoin de surveiller pendant des heures. Mais les premiers runs après l'activation méritent ton attention.

**[TRANSITION - face caméra]**

Tes tests sont en place. Pour finir ce module, on va récapituler les 10 bonnes pratiques qui séparent un workflow amateur d'un workflow professionnel.

---

**Points clés**
- 3 niveaux de test : Fetch Data, run manuel, environnement de staging
- Ne jamais tester avec de vraies données clients
- Filtrer les commandes de test en production
- Surveiller les 5 premiers runs après chaque activation

**Mots-clés SEO**
- tester workflow OttoKit
- OttoKit staging test
- workflow test automatisation WordPress
- vérifier workflow avant production

---

## Leçon 12.7 - Les 10 bonnes pratiques workflow

**Durée** : 6 min
**Type** : Vidéo HeyGen
**Écran** : Face caméra pour intro/conclusion, slides pour chaque bonne pratique

---

**[INTRO - face caméra]**

Tu sais créer des workflows, les tester, les debugger. Maintenant, parlons de qualité. Il y a une différence entre un workflow qui marche et un workflow bien construit. Les 10 bonnes pratiques qu'on va voir font cette différence.

**[ÉCRAN - slide "Pratique 1 : Nommage clair"]**

**1. Nomme tes workflows clairement.**

Mauvais : "Workflow 1", "Test", "New workflow (3)".
Bon : "WooCommerce → FluentCRM - Nouvelle commande", "Formulaire contact → Email + Sheets".

Le format recommandé : `[App source] → [App cible] - [Ce que ça fait]`. Tu vas me remercier quand tu en auras 30.

**[ÉCRAN - slide "Pratique 2 : Un workflow, un objectif"]**

**2. Un workflow fait une seule chose.**

Si ton workflow gère les inscriptions ET les désabonnements ET les relances, c'est trop. Découpe en 3 workflows distincts. Plus simple à tester, plus simple à debugger.

**[ÉCRAN - slide "Pratique 3 : Documente"]**

**3. Ajoute des notes dans tes workflows.**

OttoKit permet d'ajouter des notes sur le canvas. Utilise-les. Explique pourquoi tel filtre est là, pourquoi tel champ est mappé ainsi. Ton futur toi te remerciera dans 6 mois.

**[ÉCRAN - slide "Pratique 4 : Filtre tôt"]**

**4. Filtre le plus tôt possible dans le workflow.**

Place tes conditions et filtres juste après le trigger. Ça évite de consommer des tasks pour des exécutions qui seront finalement ignorées.

**[ÉCRAN - slide "Pratique 5 : Gère les erreurs"]**

**5. Prévois les cas d'erreur.**

Un champ peut être vide. Une API peut être indisponible. Un email peut être invalide. Ajoute des conditions pour gérer ces cas au lieu de laisser le workflow échouer.

**[ÉCRAN - slide "Pratique 6 : Versionne"]**

**6. Duplique avant de modifier.**

Tu veux changer un workflow qui fonctionne ? Duplique-le d'abord. Modifie la copie. Teste. Si ça marche, désactive l'original. Si ça casse, tu as toujours la version qui marche.

**[ÉCRAN - slide "Pratique 7 : Garde-le simple"]**

**7. Moins de 10 nœuds par workflow.**

Si ton workflow dépasse 10 nœuds, il est probablement trop complexe. Découpe-le en plusieurs workflows connectés par des webhooks. Chaque workflow reste lisible et testable.

**[ÉCRAN - slide "Pratique 8 : Nomme tes nœuds"]**

**8. Renomme les nœuds par défaut.**

"Action 1", "Action 2"... ça ne dit rien. Renomme en "Ajout contact FluentCRM", "Email confirmation", "Ligne Google Sheets". Le canvas devient lisible en un coup d'œil.

**[ÉCRAN - slide "Pratique 9 : Teste régulièrement"]**

**9. Reteste après chaque mise à jour de plugin.**

Tu mets à jour WooCommerce ou FluentCRM ? Vérifie que tes workflows fonctionnent toujours. Les mises à jour peuvent modifier les champs disponibles ou le comportement des hooks.

**[ÉCRAN - slide "Pratique 10 : Revue mensuelle"]**

**10. Fais une revue mensuelle.**

Une fois par mois, parcours tes workflows :
- Lesquels n'ont pas été déclenchés depuis 30 jours ? → Désactive-les ou supprime-les.
- Lesquels ont un taux d'échec élevé ? → Investigue.
- Lesquels consomment le plus de tasks ? → Optimise.

C'est 15 minutes par mois qui t'évitent des heures de debug.

**[TRANSITION - face caméra]**

Ces 10 pratiques, applique-les dès maintenant. Prends un workflow existant et passe-le en revue. C'est le meilleur exercice. On se retrouve dans le quiz pour valider ce module.

---

**Points clés**
- Nommer clairement : [Source] → [Cible] - [Objectif]
- Un workflow = un objectif, moins de 10 nœuds
- Filtrer tôt, gérer les erreurs, documenter avec des notes
- Revue mensuelle : désactiver, optimiser, nettoyer

**Mots-clés SEO**
- bonnes pratiques OttoKit
- organiser workflows OttoKit
- OttoKit conseils automatisation
- workflow propre WordPress

---

## Leçon 12.8 - Quiz M12

**Durée** : 5 min
**Type** : Quiz
**Note production** : Quiz interactif - pas de script vidéo. Questions générées dans le LMS.

---

# Notes de production - Module 12

**Angle schoolsWP** : Le fil rouge du module est le monitoring réel du workflow "inscription → email → CRM" sur le site schoolsWP. Les exemples de debug utilisent des erreurs réelles (email invalide, connexion expirée FluentCRM). L'optimisation des tasks illustre le filtrage des commandes de test WooCommerce avant exécution.

**Assets nécessaires** :
- Compte OttoKit avec historique de runs (success + failed)
- Workflow "inscription → email → FluentCRM" actif avec historique
- Un run en échec réel (email invalide) pour démo replay
- Tableau compteur de tasks du dashboard
- 10 slides bonnes pratiques (une par pratique)

**Enchaînement des leçons** :
- 12.1 → 12.2 : des logs à l'identification d'erreurs (progression naturelle)
- 12.2 → 12.3 : de l'identification à la correction (action)
- 12.3 → 12.4 : du réactif au proactif (alertes)
- 12.4 → 12.5 : des alertes à l'optimisation (coûts)
- 12.5 → 12.6 : de l'optimisation au test (prévention)
- 12.6 → 12.7 : du test aux bonnes pratiques (excellence)

**Workflows montrés dans le module** :
1. Workflow "Inscription formation → Email bienvenue → FluentCRM" (fil rouge)
2. Workflow "WooCommerce commande → Filtre test → Actions" (optimisation tasks)
3. Méta-workflow "Workflow Failed → Alerte WhatsApp" (notifications avancées)
