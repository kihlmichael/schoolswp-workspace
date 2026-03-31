# Scripts video — Module 12 : Monitoring, debugging et optimisation

**Formation** : Maitriser OttoKit
**Module** : M12 — Monitoring, debugging et optimisation
**Lecons** : 7 videos + 1 quiz
**Duree totale** : ~45 min de video
**Date** : 2026-03-30

---

## Lecon 12.1 — Workflow History : lire et comprendre les logs

**Duree** : 6 min
**Type** : Video HeyGen
**Ecran** : Face camera pour intro/conclusion, screencast OttoKit History

---

**[INTRO — face camera]**

Tes workflows tournent. Mais est-ce qu'ils tournent bien ? La seule facon de le savoir, c'est de lire les logs. OttoKit enregistre chaque execution dans l'onglet History. C'est ta boite noire. Aujourd'hui, on apprend a la lire.

**[ECRAN — screencast OttoKit dashboard]**

[Clique sur "History" dans la barre laterale gauche]

Voici l'ecran History. C'est la liste de toutes les executions de tous tes workflows. Chaque ligne represente un "run" — une execution complete.

[Pointe les colonnes du tableau : workflow name, status, date, duration]

Pour chaque run, tu vois :

- **Le nom du workflow** — lequel s'est declenche
- **Le statut** — Success (vert), Failed (rouge), Running (bleu)
- **La date et l'heure** — quand exactement
- **La duree** — combien de temps l'execution a pris

**[ECRAN — screencast detail d'un run]**

[Clique sur un run avec statut "Success"]
[Montre le detail : chaque etape du workflow avec ses donnees d'entree et de sortie]

Quand tu cliques sur un run, tu vois le detail etape par etape. Chaque noeud du workflow affiche :

1. Les **donnees recues** (input) — ce qui est arrive dans le noeud
2. Les **donnees produites** (output) — ce qui en est sorti
3. Le **temps d'execution** de chaque etape

C'est fondamental. Si quelque chose ne fonctionne pas, c'est ici que tu trouveras pourquoi.

**[ECRAN — screencast filtre et recherche]**

[Montre les filtres : par workflow, par statut, par date]
[Filtre par statut "Failed"]
[Filtre par workflow specifique]

Tu peux filtrer les logs par statut, par workflow, ou par date. Si tu cherches uniquement les echecs, filtre par "Failed". Si tu veux suivre un workflow specifique, selectionne-le dans la liste.

**[ECRAN — screencast workflow "Inscription → email → CRM"]**

[Ouvre le detail d'un run du workflow d'inscription]
[Montre le trigger "User Registered", puis l'action "Send Email", puis l'action "Add to CRM"]
[Pointe les donnees transmises entre chaque etape]

Prenons un exemple reel. Ce workflow se declenche quand un utilisateur s'inscrit sur le site schoolsWP. Il envoie un email de bienvenue, puis ajoute le contact dans FluentCRM. Dans les logs, tu vois exactement quel email a ete envoie, a quelle adresse, et quel contact a ete cree.

**[TRANSITION — face camera]**

Tu sais maintenant lire les logs. Dans la prochaine lecon, on va voir les 5 erreurs les plus frequentes — et comment les reperer dans ces memes logs.

---

**Points cles**
- L'onglet History enregistre chaque execution de chaque workflow
- Trois statuts : Success (vert), Failed (rouge), Running (bleu)
- Le detail d'un run montre les donnees d'entree et de sortie de chaque etape
- Les filtres permettent d'isoler rapidement les echecs ou un workflow specifique

**Mots-cles SEO**
- OttoKit workflow history
- OttoKit logs automatisation
- monitorer workflow OttoKit
- debug OttoKit WordPress

---

## Lecon 12.2 — Identifier une erreur : les 5 causes les plus frequentes

**Duree** : 6 min
**Type** : Video HeyGen
**Ecran** : Face camera pour intro/conclusion, slides pour chaque type d'erreur, screencast OttoKit

---

**[INTRO — face camera]**

Un workflow qui echoue, ca arrive. Ce n'est pas un probleme — a condition que tu saches diagnostiquer la cause. En 3 ans d'automatisation WordPress, j'ai identifie 5 erreurs qui reviennent dans 90% des cas. On les passe en revue.

**[ECRAN — slide "Erreur 1 : Connexion expiree"]**

**Cause 1 : la connexion a expire.**

C'est la plus courante. Tu as connecte Google Sheets ou Mailchimp il y a 3 mois. Depuis, le token d'authentification a expire. OttoKit ne peut plus communiquer avec l'app.

Symptome : le message d'erreur contient "401 Unauthorized" ou "Invalid credentials".

Solution : va dans Connections, deconnecte l'app concernee, et reconnecte-la.

**[ECRAN — slide "Erreur 2 : Champ manquant ou vide"]**

**Cause 2 : un champ obligatoire est vide.**

Tu as configure une action "Envoyer un email" avec le champ `billing_email`. Mais cette fois, le trigger n'a pas retourne d'email — le champ est vide. L'action echoue.

Symptome : "Required field is empty" ou "Missing value".

Solution : ajoute un filtre avant l'action pour verifier que le champ existe. Ou configure une valeur par defaut.

**[ECRAN — slide "Erreur 3 : Limite API atteinte"]**

**Cause 3 : la limite de l'API est atteinte (rate limit).**

Chaque service a des limites. Si tu envoies 200 requetes a Google Sheets en 1 minute, Google te bloque temporairement.

Symptome : "429 Too Many Requests" ou "Rate limit exceeded".

Solution : ajoute un delai entre les actions, ou reduis le volume de donnees traitees par run.

**[ECRAN — slide "Erreur 4 : Format de donnees invalide"]**

**Cause 4 : le format de donnees est invalide.**

Tu envoies un texte la ou l'API attend un nombre. Ou une date au format "30/03/2026" alors que l'app attend "2026-03-30".

Symptome : "Invalid format", "Type mismatch" ou "Cannot parse".

Solution : verifie le format attendu dans la documentation de l'app et utilise les fonctions de formatage d'OttoKit.

**[ECRAN — slide "Erreur 5 : Permission refusee"]**

**Cause 5 : permissions insuffisantes.**

L'app est connectee, mais avec un compte qui n'a pas les droits necessaires. Par exemple, un compte Google qui n'a pas acces au spreadsheet vise.

Symptome : "403 Forbidden" ou "Access denied".

Solution : verifie que le compte utilise a les permissions necessaires sur la ressource cible.

**[ECRAN — screencast OttoKit History — run Failed]**

[Ouvre un run en echec]
[Montre le message d'erreur dans le detail]
[Pointe l'etape exacte qui a echoue (en rouge)]

Dans les logs, l'etape en echec est marquee en rouge. Clique dessus pour voir le message d'erreur. C'est la que tu identifies la cause. Compare le message avec les 5 cas qu'on vient de voir.

**[TRANSITION — face camera]**

Tu connais les 5 erreurs. Maintenant, on va voir comment corriger et relancer un workflow sans repartir de zero.

---

**Points cles**
- 5 causes couvrent 90% des erreurs : connexion expiree, champ manquant, rate limit, format invalide, permission
- Le message d'erreur dans les logs indique presque toujours la cause
- L'etape en echec est marquee en rouge dans le detail du run
- Chaque cause a une solution precise et rapide

**Mots-cles SEO**
- OttoKit erreur workflow
- debug automatisation WordPress
- OttoKit connexion expiree
- OttoKit 401 403 429 erreur

---

## Lecon 12.3 — Auto-replay et replay manuel : corriger et relancer

**Duree** : 6 min
**Type** : Video HeyGen
**Ecran** : Face camera pour intro/conclusion, screencast OttoKit History et replay

---

**[INTRO — face camera]**

Un workflow a echoue. Tu as identifie la cause. Maintenant, tu veux relancer cette execution — sans attendre qu'un nouvel evenement se produise. OttoKit propose deux mecanismes : l'auto-replay et le replay manuel.

**[ECRAN — slide "Auto-replay vs replay manuel"]**

| | Auto-replay | Replay manuel |
|---|---|---|
| Declenchement | Automatique apres echec | Toi, quand tu decides |
| Tentatives | Jusqu'a 6 tentatives | 1 tentative |
| Donnees | Identiques au run original | Modifiables avant relance |
| Cas d'usage | Erreur temporaire (timeout, rate limit) | Erreur de donnees (email invalide) |

L'auto-replay est utile pour les erreurs temporaires. L'API est surchargee ? OttoKit reessaie automatiquement. Mais si le probleme vient des donnees — un email mal formate par exemple — l'auto-replay va echouer 6 fois de suite avec la meme erreur.

**[ECRAN — screencast OttoKit — configuration auto-replay]**

[Ouvre les parametres d'un workflow]
[Montre l'option auto-replay : enable/disable]
[Montre le nombre de tentatives configurable]

L'auto-replay se configure dans les parametres du workflow. Tu peux l'activer ou le desactiver. Quand c'est active, OttoKit reessaie automatiquement avec un delai croissant entre chaque tentative.

**[ECRAN — screencast OttoKit — replay manuel]**

[Va dans History]
[Selectionne un run en echec]
[Clique sur le bouton "Replay"]
[Montre l'ecran de modification des donnees]

Le replay manuel, c'est different. Tu ouvres un run en echec dans l'History. Tu cliques sur "Replay". Et la, OttoKit te montre les donnees du run original. Tu peux les modifier avant de relancer.

**[ECRAN — screencast correction et relance]**

[Montre les donnees du run : un champ email contient "jean@gmailcom" (manque le point)]
[Corrige le champ en "jean@gmail.com"]
[Clique sur "Replay"]
[Montre le nouveau run qui passe en "Success"]

Exemple concret. Ce run a echoue parce que l'email du client etait mal saisi : "jean@gmailcom" au lieu de "jean@gmail.com". Avec le replay manuel, tu corriges le champ et tu relances. Le workflow s'execute correctement.

**[ECRAN — slide "Quand utiliser quoi"]**

- **Erreur temporaire** (timeout, rate limit, serveur indisponible) → laisse l'auto-replay gerer
- **Erreur de donnees** (email invalide, champ manquant, format incorrect) → replay manuel avec correction
- **Erreur de configuration** (connexion expiree, mauvais mapping) → corrige d'abord le workflow, puis replay

**[TRANSITION — face camera]**

Le replay, c'est ton filet de securite. Aucune execution n'est perdue. Dans la prochaine lecon, on va aller plus loin : se faire alerter avant meme d'ouvrir les logs.

---

**Points cles**
- Auto-replay : jusqu'a 6 tentatives automatiques, ideal pour les erreurs temporaires
- Replay manuel : permet de modifier les donnees avant de relancer
- Le replay evite de perdre des executions — chaque run peut etre rejoue
- Toujours corriger la cause avant de rejouer (sinon le meme echec se repete)

**Mots-cles SEO**
- OttoKit replay workflow
- OttoKit auto-replay
- relancer workflow echec OttoKit
- corriger erreur OttoKit automatisation

---

## Lecon 12.4 — Notifications : sois alerte avant que ca casse

**Duree** : 5 min
**Type** : Video HeyGen
**Ecran** : Face camera pour intro/conclusion, screencast OttoKit notifications

---

**[INTRO — face camera]**

Tu ne peux pas surveiller tes workflows en permanence. Tu as autre chose a faire. C'est pour ca qu'OttoKit peut t'envoyer des alertes quand quelque chose echoue. Tu configures une fois, et tu es prevenu automatiquement.

**[ECRAN — screencast OttoKit Settings → Notifications]**

[Ouvre Settings dans la barre laterale]
[Clique sur la section Notifications]
[Montre les options disponibles]

Dans les settings d'OttoKit, tu trouves la section Notifications. Ici, tu configures comment tu veux etre alerte.

**[ECRAN — screencast configuration email]**

[Active les notifications par email]
[Montre le champ d'adresse email]
[Selectionne les evenements : "Workflow Failed"]

Premiere option : l'email. Tu entres ton adresse, tu selectionnes les evenements qui t'interessent — en general, "Workflow Failed". A chaque echec, tu recois un email avec le nom du workflow, l'erreur, et un lien direct vers le run.

**[ECRAN — screencast configuration avancee]**

[Montre les options supplementaires : alerte par workflow, frequence]

Tu peux aller plus loin. Certaines configurations permettent de :

- Recevoir des alertes uniquement pour certains workflows critiques
- Grouper les alertes pour eviter d'etre noye (un resume toutes les heures plutot qu'un email par echec)

**[ECRAN — slide "Strategie d'alerte recommandee"]**

Voici ce que je recommande :

1. **Email immediat** pour les workflows critiques (paiement, inscription, livraison)
2. **Resume quotidien** pour les workflows moins urgents (synchronisation de donnees, nettoyage)
3. **Pas d'alerte** pour les workflows de test en cours de developpement

L'objectif : etre prevenu des vrais problemes sans etre submerge par le bruit.

**[ECRAN — screencast creation d'un workflow d'alerte custom]**

[Montre un workflow OttoKit dont le trigger est "Workflow Failed"]
[L'action envoie un message WhatsApp ou Slack avec les details de l'echec]

Astuce avancee : tu peux creer un workflow OttoKit dont le trigger est l'echec d'un autre workflow. Ce meta-workflow peut t'envoyer un message WhatsApp, poster dans Slack, ou meme creer une tache dans Notion. Tu controles entierement le canal d'alerte.

**[TRANSITION — face camera]**

Les alertes sont en place. Passons a un sujet qui touche directement ton portefeuille : optimiser ta consommation de tasks.

---

**Points cles**
- Les notifications evitent de decouvrir un probleme trop tard
- Email par defaut pour "Workflow Failed" — la configuration minimum
- Un meta-workflow peut alerter sur n'importe quel canal (Slack, WhatsApp, Notion)
- Differencier les workflows critiques des workflows secondaires

**Mots-cles SEO**
- OttoKit notification echec
- alerte workflow OttoKit
- monitoring automatisation WordPress
- OttoKit WhatsApp notification

---

## Lecon 12.5 — Optimiser sa consommation de tasks

**Duree** : 6 min
**Type** : Video HeyGen
**Ecran** : Face camera pour intro/conclusion, slides compteur tasks, screencast OttoKit

---

**[INTRO — face camera]**

Chaque action executee par OttoKit consomme un "task". Et ton forfait a une limite. Donc si tu veux automatiser beaucoup sans exploser le compteur, tu dois comprendre ce qui consomme et comment optimiser.

**[ECRAN — slide "Ce qui compte comme task"]**

Regle numero un : **chaque action executee = 1 task**.

Ce qui consomme :
- Chaque action dans un workflow qui s'execute = 1 task
- Si ton workflow a 5 actions et se declenche 10 fois → 50 tasks

Ce qui ne consomme PAS :
- Le trigger (l'evenement declencheur) = 0 task
- Les filtres et conditions = 0 task
- Un workflow en pause = 0 task
- Un workflow actif qui ne se declenche pas = 0 task

**[ECRAN — slide "Exemple de calcul"]**

Prenons un exemple. Tu as un workflow "Nouvelle commande WooCommerce" avec 4 actions :

1. Ajouter le client dans FluentCRM → 1 task
2. Envoyer un email de confirmation → 1 task
3. Ajouter une ligne dans Google Sheets → 1 task
4. Envoyer un message Slack → 1 task

Total par commande : 4 tasks. A 100 commandes par mois : 400 tasks.

**[ECRAN — screencast OttoKit dashboard usage]**

[Montre le compteur de tasks dans le dashboard]
[Pointe le forfait actuel et la consommation]

Dans ton dashboard, tu vois ta consommation en temps reel. Le compteur indique combien de tasks tu as utilisees sur le mois et combien il t'en reste.

**[ECRAN — slide "5 strategies d'economie"]**

Voici 5 strategies pour optimiser :

**1. Filtre avant d'agir.** Si tu as un workflow WooCommerce, ajoute un filtre pour ignorer les commandes de test. Les filtres ne consomment pas de task, mais ils evitent de declencher des actions inutiles.

**2. Combine les actions.** Plutot que d'envoyer 3 webhooks separement, envoie un seul webhook avec toutes les donnees. 1 task au lieu de 3.

**3. Desactive les workflows en developpement.** Un workflow actif avec un trigger planifie consomme des tasks a chaque verification qui detecte quelque chose. Mets-le en pause tant que tu testes.

**4. Utilise les conditions intelligemment.** Avant l'action "Envoyer un SMS", verifie que le numero de telephone existe. Si le champ est vide, l'action ne s'execute pas → 0 task.

**5. Consolide les workflows redondants.** Si tu as 3 workflows qui font la meme chose pour 3 formulaires differents, combine-les en un seul avec un routeur.

**[ECRAN — screencast workflow WooCommerce avec filtre]**

[Ouvre un workflow reel]
[Montre un noeud Filter apres le trigger WooCommerce]
[Le filtre exclut les commandes avec status "test" ou montant = 0]
[Montre que les commandes de test ne declenchent pas les actions en aval]

Exemple schoolsWP : ce workflow gere les inscriptions aux formations. On a ajoute un filtre qui exclut les commandes de test de WooCommerce — montant a zero ou email contenant "test@". Resultat : on economise environ 20% de tasks chaque mois.

**[TRANSITION — face camera]**

Tu sais maintenant compter et optimiser tes tasks. Prochaine etape : tester tes workflows sans risquer de casser ta production.

---

**Points cles**
- 1 action executee = 1 task ; triggers et filtres = 0 task
- Toujours filtrer les donnees de test avant les actions
- Combiner les actions et consolider les workflows redondants pour economiser
- Surveiller le compteur de tasks dans le dashboard chaque semaine

**Mots-cles SEO**
- OttoKit tasks consommation
- optimiser tasks OttoKit
- OttoKit pricing tasks
- economiser automatisation OttoKit

---

## Lecon 12.6 — Tester en staging : ne jamais casser la production

**Duree** : 5 min
**Type** : Video HeyGen
**Ecran** : Face camera pour intro/conclusion, slides strategie de test, screencast OttoKit

---

**[INTRO — face camera]**

Tu viens de creer un workflow qui envoie un email a chaque nouveau client. Avant de l'activer pour de vrai, tu veux etre sur qu'il fonctionne correctement. Parce qu'un email de bienvenue avec des champs vides, ca donne une mauvaise premiere impression. Voyons comment tester sans risque.

**[ECRAN — slide "Les 3 niveaux de test"]**

Il y a 3 niveaux de test pour un workflow OttoKit :

**Niveau 1 — Fetch Data.** Quand tu configures un trigger ou une action, le bouton "Fetch Data" recupere des donnees reelles. Ca te permet de verifier que les champs sont corrects. C'est le test le plus basique.

**Niveau 2 — Run manuel avec donnees de test.** Tu actives le workflow, tu declenches manuellement l'evenement (par exemple, tu crees une commande de test dans WooCommerce), et tu verifies dans l'History que chaque etape s'execute correctement.

**Niveau 3 — Environnement de staging.** Tu dupliques ton workflow, tu le connectes a un site de staging (une copie de ton site), et tu testes la-bas. Aucun impact sur la production.

**[ECRAN — screencast preparation d'un test]**

[Montre un workflow en brouillon]
[Montre le bouton "Fetch Data" sur le trigger]
[Clique et montre les donnees recuperees]

Le niveau 1, tu le connais deja — c'est le Fetch Data. Ca confirme que la connexion fonctionne et que les donnees arrivent.

**[ECRAN — screencast test avec donnees reelles]**

[Active le workflow]
[Va dans WooCommerce et cree une commande de test — produit a 0 euros, email de test]
[Revient dans OttoKit History]
[Montre le run declenche avec les donnees de test]
[Verifie chaque etape]

Le niveau 2 : tu crees une vraie commande de test. Utilise un email de test (pas celui d'un vrai client), un produit a 0 euros, et un nom reconnaissable comme "Test Workflow". Ensuite, verifie dans l'History que chaque etape s'est executee correctement.

**[ECRAN — slide "Bonnes pratiques de test"]**

Quelques regles de prudence :

- **Ne teste jamais avec de vraies donnees clients.** Utilise des emails de test.
- **Mets un filtre anti-test en production.** On l'a vu dans la lecon precedente — exclure les commandes a 0 euros ou les emails "test@".
- **Teste apres chaque modification.** Tu changes un champ, tu retestes. Pas dans 3 jours.
- **Documente tes tests.** Note ce que tu as teste et le resultat. Quand un workflow casse 2 mois plus tard, tu sauras ce qui fonctionnait avant.

**[ECRAN — slide "Publication progressive"]**

Quand tu es satisfait du test :

1. Active le workflow
2. Surveille les 5 premiers runs dans l'History
3. Si tout est bon, passe a autre chose
4. Reviens verifier le lendemain

Pas besoin de surveiller pendant des heures. Mais les premiers runs apres l'activation meritent ton attention.

**[TRANSITION — face camera]**

Tes tests sont en place. Pour finir ce module, on va recapituler les 10 bonnes pratiques qui separent un workflow amateur d'un workflow professionnel.

---

**Points cles**
- 3 niveaux de test : Fetch Data, run manuel, environnement de staging
- Ne jamais tester avec de vraies donnees clients
- Filtrer les commandes de test en production
- Surveiller les 5 premiers runs apres chaque activation

**Mots-cles SEO**
- tester workflow OttoKit
- OttoKit staging test
- workflow test automatisation WordPress
- verifier workflow avant production

---

## Lecon 12.7 — Les 10 bonnes pratiques workflow

**Duree** : 6 min
**Type** : Video HeyGen
**Ecran** : Face camera pour intro/conclusion, slides pour chaque bonne pratique

---

**[INTRO — face camera]**

Tu sais creer des workflows, les tester, les debugger. Maintenant, parlons de qualite. Il y a une difference entre un workflow qui marche et un workflow bien construit. Les 10 bonnes pratiques qu'on va voir font cette difference.

**[ECRAN — slide "Pratique 1 : Nommage clair"]**

**1. Nomme tes workflows clairement.**

Mauvais : "Workflow 1", "Test", "New workflow (3)".
Bon : "WooCommerce → FluentCRM — Nouvelle commande", "Formulaire contact → Email + Sheets".

Le format recommande : `[App source] → [App cible] — [Ce que ca fait]`. Tu vas me remercier quand tu en auras 30.

**[ECRAN — slide "Pratique 2 : Un workflow, un objectif"]**

**2. Un workflow fait une seule chose.**

Si ton workflow gere les inscriptions ET les desabonnements ET les relances, c'est trop. Decoupe en 3 workflows distincts. Plus simple a tester, plus simple a debugger.

**[ECRAN — slide "Pratique 3 : Documente"]**

**3. Ajoute des notes dans tes workflows.**

OttoKit permet d'ajouter des notes sur le canvas. Utilise-les. Explique pourquoi tel filtre est la, pourquoi tel champ est mappe ainsi. Ton futur toi te remerciera dans 6 mois.

**[ECRAN — slide "Pratique 4 : Filtre tot"]**

**4. Filtre le plus tot possible dans le workflow.**

Place tes conditions et filtres juste apres le trigger. Ca evite de consommer des tasks pour des executions qui seront finalement ignorees.

**[ECRAN — slide "Pratique 5 : Gere les erreurs"]**

**5. Prevois les cas d'erreur.**

Un champ peut etre vide. Une API peut etre indisponible. Un email peut etre invalide. Ajoute des conditions pour gerer ces cas au lieu de laisser le workflow echouer.

**[ECRAN — slide "Pratique 6 : Versionne"]**

**6. Duplique avant de modifier.**

Tu veux changer un workflow qui fonctionne ? Duplique-le d'abord. Modifie la copie. Teste. Si ca marche, desactive l'original. Si ca casse, tu as toujours la version qui marche.

**[ECRAN — slide "Pratique 7 : Garde-le simple"]**

**7. Moins de 10 noeuds par workflow.**

Si ton workflow depasse 10 noeuds, il est probablement trop complexe. Decoupe-le en plusieurs workflows connectes par des webhooks. Chaque workflow reste lisible et testable.

**[ECRAN — slide "Pratique 8 : Nomme tes noeuds"]**

**8. Renomme les noeuds par defaut.**

"Action 1", "Action 2"... ca ne dit rien. Renomme en "Ajout contact FluentCRM", "Email confirmation", "Ligne Google Sheets". Le canvas devient lisible en un coup d'oeil.

**[ECRAN — slide "Pratique 9 : Teste regulierement"]**

**9. Reteste apres chaque mise a jour de plugin.**

Tu mets a jour WooCommerce ou FluentCRM ? Verifie que tes workflows fonctionnent toujours. Les mises a jour peuvent modifier les champs disponibles ou le comportement des hooks.

**[ECRAN — slide "Pratique 10 : Revue mensuelle"]**

**10. Fais une revue mensuelle.**

Une fois par mois, parcours tes workflows :
- Lesquels n'ont pas ete declenches depuis 30 jours ? → Desactive-les ou supprime-les.
- Lesquels ont un taux d'echec eleve ? → Investigue.
- Lesquels consomment le plus de tasks ? → Optimise.

C'est 15 minutes par mois qui t'evitent des heures de debug.

**[TRANSITION — face camera]**

Ces 10 pratiques, applique-les des maintenant. Prends un workflow existant et passe-le en revue. C'est le meilleur exercice. On se retrouve dans le quiz pour valider ce module.

---

**Points cles**
- Nommer clairement : [Source] → [Cible] — [Objectif]
- Un workflow = un objectif, moins de 10 noeuds
- Filtrer tot, gerer les erreurs, documenter avec des notes
- Revue mensuelle : desactiver, optimiser, nettoyer

**Mots-cles SEO**
- bonnes pratiques OttoKit
- organiser workflows OttoKit
- OttoKit conseils automatisation
- workflow propre WordPress

---

## Lecon 12.8 — Quiz M12

**Duree** : 5 min
**Type** : Quiz
**Note production** : Quiz interactif — pas de script video. Questions generees dans le LMS.

---

# Notes de production — Module 12

**Angle schoolsWP** : Le fil rouge du module est le monitoring reel du workflow "inscription → email → CRM" sur le site schoolsWP. Les exemples de debug utilisent des erreurs reelles (email invalide, connexion expiree FluentCRM). L'optimisation des tasks illustre le filtrage des commandes de test WooCommerce avant execution.

**Assets necessaires** :
- Compte OttoKit avec historique de runs (success + failed)
- Workflow "inscription → email → FluentCRM" actif avec historique
- Un run en echec reel (email invalide) pour demo replay
- Tableau compteur de tasks du dashboard
- 10 slides bonnes pratiques (une par pratique)

**Enchainement des lecons** :
- 12.1 → 12.2 : des logs a l'identification d'erreurs (progression naturelle)
- 12.2 → 12.3 : de l'identification a la correction (action)
- 12.3 → 12.4 : du reactif au proactif (alertes)
- 12.4 → 12.5 : des alertes a l'optimisation (couts)
- 12.5 → 12.6 : de l'optimisation au test (prevention)
- 12.6 → 12.7 : du test aux bonnes pratiques (excellence)

**Workflows montres dans le module** :
1. Workflow "Inscription formation → Email bienvenue → FluentCRM" (fil rouge)
2. Workflow "WooCommerce commande → Filtre test → Actions" (optimisation tasks)
3. Meta-workflow "Workflow Failed → Alerte WhatsApp" (notifications avancees)
