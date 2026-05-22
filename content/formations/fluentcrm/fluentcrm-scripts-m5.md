# Scripts vidéo -- Module 5 : Email séquences et nurturing

**Formation** : Maîtriser FluentCRM
**Module** : M5 -- Email séquences et nurturing (Premium)
**Leçons** : 6 vidéos + 1 exercice + 1 quiz
**Durée totale** : ~50 min de vidéo
**Date** : 2026-03-23

---

## Leçon 5.1 -- Comprends les séquences : quand les utiliser vs une campagne

**Durée** : 5 min
**Type** : Vidéo HeyGen
**Écran** : FluentCRM > Email Sequences

---

**[INTRO -- face caméra]**

Tu sais envoyer des campagnes. Mais une campagne, c'est un envoi ponctuel. Tu l'envoies, c'est fini. Une séquence, c'est différent : c'est une série d'emails envoyés automatiquement dans un ordre précis, avec des délais entre chaque envoi. Et c'est là que ton email marketing devient vraiment efficace.

**[ÉCRAN -- slide "Campagne vs Séquence vs Automation"]**

Posons les bases clairement. Il y a trois outils d'envoi dans FluentCRM, et chacun a un rôle précis.

La campagne : un email envoyé à une audience à un moment donné. Une newsletter, une promo, une annonce. C'est du one-shot.

La séquence : une série d'emails envoyés automatiquement, dans l'ordre, avec des délais configurés. Chaque contact qui entre dans la séquence reçoit le même parcours, mais à son propre rythme.

L'automation : un workflow visuel avec des conditions, des branches, des déclencheurs. C'est plus puissant, mais plus complexe. On le verra dans le Module 6.

**[ÉCRAN -- slide "Quand utiliser quoi ?"]**

Utilise une campagne quand tu envoies un message ponctuel à un groupe de contacts. Un lancement, une newsletter mensuelle, une annonce.

Utilise une séquence quand tu veux qu'un contact reçoive une série d'emails prédéterminés dans un ordre fixe. L'onboarding d'un nouvel inscrit, le nurturing d'un prospect, la relance d'un contact inactif.

Utilise une automation quand tu as besoin de logique conditionnelle. Si le contact ouvre l'email, il va dans la branche A. S'il ne l'ouvre pas, branche B. On n'en est pas encore là.

**[ÉCRAN -- screencast FluentCRM > Email Sequences]**

Dans FluentCRM, va dans Email Sequences dans le menu latéral.

[Clic sur Email Sequences]

Tu arrives sur la liste de tes séquences. Si tu n'en as pas encore, c'est vide. Et c'est normal.

Clique sur "Create New Sequence".

[Clic sur Create New Sequence]

Tu vois l'interface de création. Un titre, et ensuite tu ajoutes tes emails un par un. Chaque email a un délai, un sujet, un contenu. Le premier email part immédiatement quand le contact entre dans la séquence. Les suivants partent après le délai que tu as configuré.

**[ÉCRAN -- slide "Cas d'usage concrets schoolsWP"]**

Voici les séquences les plus utiles quand tu vends des formations en ligne :

Séquence d'onboarding : un nouvel inscrit reçoit 4-5 emails sur 7 jours. Bienvenue, contenu gratuit, témoignage, offre.

Séquence de nurturing : un prospect qui a téléchargé un lead magnet reçoit une série d'emails qui le fait passer de "curieux" à "prêt à acheter".

Séquence de re-engagement : un étudiant qui n'a pas terminé son cours depuis 14 jours reçoit une série d'emails pour le remotiver.

Séquence post-achat : un client qui vient d'acheter reçoit des emails pour maximiser sa satisfaction et réduire les demandes de remboursement.

**[FACE CAMÉRA]**

Retiens ça : une campagne parle à un groupe à un instant T. Une séquence accompagne chaque individu dans un parcours. C'est la différence entre crier dans un mégaphone et avoir une conversation personnalisée.

**[TRANSITION]**

Tu comprends maintenant quand utiliser quoi. Dans la prochaine leçon, on crée ta première séquence d'onboarding, email par email.

---

**Points clés** :
- Campagne = envoi ponctuel. Séquence = série automatique. Automation = workflow conditionnel.
- Utiliser une séquence quand chaque contact doit recevoir le même parcours à son propre rythme
- Cas d'usage clés : onboarding, nurturing, re-engagement, post-achat
- Le premier email d'une séquence part immédiatement, les suivants selon les délais configurés

**Mots clés SEO** : séquence email FluentCRM, campagne vs séquence, email automation WordPress, nurturing email marketing

---

## Leçon 5.2 -- Crée ta première séquence d'onboarding

**Durée** : 7 min
**Type** : Vidéo HeyGen
**Écran** : FluentCRM > Email Sequences > Create

---

**[INTRO -- face caméra]**

On passe à la pratique. On va créer ensemble une séquence d'onboarding pour accueillir les nouveaux inscrits à ta formation gratuite. Cinq emails, sept jours. À la fin de cette leçon, ta séquence sera prête.

**[ÉCRAN -- screencast FluentCRM]**

Va dans Email Sequences et clique sur "Create New Sequence".

[Clic sur Create New Sequence]

Donne un nom à ta séquence. Par exemple : "Onboarding -- Nouveau membre". Ce nom est interne, tes contacts ne le verront pas.

[Saisie du titre]

Tu arrives sur l'interface de la séquence. C'est une liste verticale où chaque ligne est un email. Pour l'instant, c'est vide.

**[ÉCRAN -- slide "Structure de la séquence onboarding"]**

Avant de plonger dans FluentCRM, voici la structure qu'on va suivre. C'est un modèle éprouvé pour les créateurs de formation.

Email 1 -- Jour 0 : Bienvenue. Présente-toi, donne accès au contenu gratuit, fixe les attentes.

Email 2 -- Jour 1 : Valeur gratuite. Partage un conseil actionnable ou une ressource complémentaire. Tu montres ton expertise.

Email 3 -- Jour 3 : Témoignage. Partage le retour d'expérience d'un utilisateur. La preuve sociale fait le travail à ta place.

Email 4 -- Jour 5 : Contenu avancé. Un aperçu de ce que contient la formation payante. Tu donnes un avant-goût sans tout dévoiler.

Email 5 -- Jour 7 : Offre. Présente ta formation premium avec un appel à l'action clair.

**[ÉCRAN -- screencast : création du premier email]**

Clique sur "Add Email" ou le bouton "+" pour ajouter ton premier email.

[Clic sur Add Email]

Remplis le sujet. Pour le premier email : "Bienvenue {{contact.first_name}} -- ton accès est prêt".

[Saisie du sujet]

Le délai d'attente : mets 0. Le premier email part immédiatement quand le contact entre dans la séquence.

[Configuration du délai à 0]

Maintenant, rédige le contenu. Sois direct. Présente-toi en une phrase, donne le lien d'accès au contenu gratuit, et dis au contact ce qu'il va recevoir dans les prochains jours.

[Rédaction du contenu -- screencast]

Exemple de structure :

"Salut {{contact.first_name}},

Je suis [Prénom], créateur de [Nom formation].

Ton accès est prêt : [lien].

Dans les prochains jours, je vais te partager des ressources pour aller plus loin. Reste à l'affût."

Pas besoin d'en faire trop. Court, clair, utile.

**[ÉCRAN -- screencast : ajout des emails suivants]**

Clique de nouveau sur "Add Email" pour l'email 2.

[Clic sur Add Email]

Le délai cette fois : 1 jour. Ça signifie que cet email partira 24 heures après le précédent.

[Configuration du délai à 1 jour]

Sujet : "Un conseil que j'aurais aimé avoir plus tôt". Rédige un contenu court avec une astuce concrète liée à ta thématique.

[Saisie du sujet et rédaction rapide]

On continue. Email 3 : délai 2 jours après l'email 2 (donc J+3 au total). Sujet : "Comment [Prénom du témoignage] a obtenu [résultat]". Tu partages un témoignage ou une étude de cas.

[Ajout de l'email 3 avec délai et sujet]

Email 4 : délai 2 jours. Sujet : "Ce que 90% des gens font mal avec [sujet]". Tu donnes un aperçu du contenu premium.

[Ajout de l'email 4]

Email 5 : délai 2 jours. Sujet : "Prêt à passer au niveau suivant ?". C'est ton email de vente. Présente l'offre, les bénéfices, un bouton clair.

[Ajout de l'email 5]

**[ÉCRAN -- screencast : vue d'ensemble de la séquence]**

Ta séquence est complète. Cinq emails, répartis sur 7 jours.

[Vue de la liste des 5 emails avec leurs délais]

Vérifie l'ordre, les délais, les sujets. Si tu veux réorganiser, tu peux glisser-déposer les emails.

**[ÉCRAN -- screencast : paramètres de la séquence]**

Avant de publier, clique sur les paramètres de la séquence en haut.

[Clic sur Settings]

Tu peux configurer les jours et heures d'envoi. On verra ça en détail dans la leçon suivante. Pour l'instant, laisse les paramètres par défaut.

Clique sur "Publish" ou active la séquence.

[Clic sur Publish]

**[FACE CAMÉRA]**

Ta séquence d'onboarding est prête. Mais elle ne fera rien tant que tu n'y inscris pas de contacts. Pour ça, tu as deux options : inscrire manuellement des contacts depuis leur fiche, ou automatiser l'inscription via une automation. L'automation, c'est le Module 6.

En attendant, tu peux inscrire un contact test pour vérifier que tout fonctionne.

**[TRANSITION]**

Ta séquence existe. Mais le timing, c'est ce qui fait la différence entre un email lu et un email ignoré. Dans la prochaine leçon, on configure les délais, les jours et les heures d'envoi.

---

**Points clés** :
- Structure onboarding : Bienvenue (J0) > Valeur gratuite (J1) > Témoignage (J3) > Contenu avancé (J5) > Offre (J7)
- Le premier email a un délai de 0 (envoi immédiat)
- Les délais sont relatifs à l'email précédent, pas au premier email
- Inscrire un contact test pour vérifier le parcours avant de lancer
- L'inscription automatique se fait via une automation (Module 6)

**Mots clés SEO** : séquence onboarding FluentCRM, créer séquence email, email bienvenue automatique, funnel email WordPress

---

## Leçon 5.3 -- Configure le timing : délais, jours spécifiques, heures d'envoi

**Durée** : 6 min
**Type** : Vidéo HeyGen
**Écran** : FluentCRM > Email Sequences > Settings

---

**[INTRO -- face caméra]**

Tu as ta séquence. Mais si tes emails partent à 3h du matin un dimanche, personne ne les lira. Le timing, c'est ce qui transforme un bon email en email ouvert. FluentCRM te donne un contrôle précis là-dessus.

**[ÉCRAN -- screencast FluentCRM > Sequence > Settings]**

Ouvre ta séquence et clique sur les paramètres en haut.

[Clic sur Settings de la séquence]

Tu vois trois réglages principaux : les jours d'envoi, les heures d'envoi et le fuseau horaire.

**[ÉCRAN -- screencast : jours d'envoi]**

Premier réglage : les jours d'envoi. Par défaut, FluentCRM envoie tous les jours, du lundi au dimanche.

[Affichage des cases à cocher des jours]

Pour une séquence professionnelle, désactive le samedi et le dimanche. La plupart des formations en ligne ciblent des professionnels ou des indépendants. Leurs boîtes de réception sont actives en semaine.

[Décochage samedi et dimanche]

Si un email est programmé un samedi, FluentCRM le décale automatiquement au lundi suivant. Pas besoin de recalculer tes délais.

**[ÉCRAN -- screencast : heures d'envoi]**

Deuxième réglage : la fenêtre horaire. Tu définis une heure de début et une heure de fin.

[Configuration de la fenêtre horaire]

Règle recommandée : entre 8h et 10h du matin. C'est le moment où la plupart des gens consultent leurs emails. Autre créneau efficace : 14h-15h, juste après la pause déjeuner.

Évite les envois après 18h. L'email sera noyé dans les newsletters du soir.

**[ÉCRAN -- screencast : fuseau horaire]**

Troisième réglage : le fuseau horaire. FluentCRM utilise le fuseau horaire de ton site WordPress.

[Affichage du réglage timezone]

Vérifie dans WordPress > Réglages > General que ton fuseau est correct. Si ton audience est en France, assure-toi que c'est bien Europe/Paris.

Si tu as une audience internationale, choisis le fuseau de la majorité de tes contacts. FluentCRM ne gère pas les envois par fuseau horaire individuel -- c'est une limitation à connaître.

**[ÉCRAN -- slide "Timing optimal par type de séquence"]**

Le bon timing dépend du type de séquence.

Onboarding : J+0, J+1, J+3, J+5, J+7. Rythme soutenu les premiers jours, puis on espace. Le contact est "chaud", il veut du contenu.

Nurturing : J+0, J+3, J+7, J+14, J+21. Plus espacé. Tu construis la relation dans la durée sans être envahissant.

Re-engagement : J+0, J+3, J+7. Trois emails maximum. Si le contact ne réagit pas après trois tentatives, arrête. Insister ne sert à rien.

**[ÉCRAN -- screencast : délai par email]**

Reviens dans la liste des emails de ta séquence. Chaque email a son propre délai.

[Affichage de la liste des emails avec délais]

Clique sur le délai d'un email pour le modifier. Tu peux le définir en jours ou en heures.

[Modification du délai d'un email]

Astuce : pour le deuxième email, mets 1 jour plutôt que 24 heures. "1 jour" respecte la fenêtre horaire que tu as configurée. "24 heures" envoie exactement 24 heures après, même si ça tombe en dehors de ta fenêtre.

**[FACE CAMÉRA]**

Ne change pas le timing toutes les semaines. Configure une fois, lance, et analyse les résultats après au moins 50 contacts passés dans la séquence. Avant ça, tu n'as pas assez de données pour optimiser.

**[TRANSITION]**

Le timing est calé. Dans la prochaine leçon, on construit une séquence plus ambitieuse : le nurturing. L'objectif : transformer un prospect en acheteur.

---

**Points clés** :
- Désactiver les envois le week-end pour une audience professionnelle
- Fenêtre d'envoi recommandée : 8h-10h ou 14h-15h
- Vérifier le fuseau horaire dans WordPress > Réglages > General
- Utiliser "jours" plutôt que "heures" pour respecter la fenêtre d'envoi
- Timing onboarding : J+0, J+1, J+3, J+5, J+7. Nurturing : plus espacé. Re-engagement : 3 emails max.

**Mots clés SEO** : timing email FluentCRM, heure envoi email, délai séquence email, optimiser envoi email WordPress

---

## Leçon 5.4 -- Construis une séquence de nurturing (lead vers acheteur)

**Durée** : 8 min
**Type** : Vidéo HeyGen
**Écran** : FluentCRM > Email Sequences

---

**[INTRO -- face caméra]**

L'onboarding accueille. Le nurturing convertit. Un contact qui télécharge ton lead magnet n'est pas prêt à acheter. Pas encore. La séquence de nurturing, c'est le pont entre "je te découvre" et "je te fais confiance, je passe à l'action".

**[ÉCRAN -- slide "Anatomie d'une séquence de nurturing"]**

Une bonne séquence de nurturing suit une progression psychologique. Pas une suite d'emails au hasard.

Phase 1 -- Crédibilité (emails 1-2) : tu montres que tu comprends le problème du contact. Tu donnes de la valeur sans rien demander.

Phase 2 -- Preuve (emails 3-4) : tu partages des résultats concrets. Témoignages, études de cas, chiffres. Le contact commence à se dire "ça marche vraiment".

Phase 3 -- Projection (email 5) : tu aides le contact à se projeter. À quoi ressemble sa situation après avoir utilisé ta solution ?

Phase 4 -- Offre (emails 6-7) : tu présentes ton offre avec un appel à l'action clair. Tu lèves les dernières objections.

**[ÉCRAN -- screencast FluentCRM]**

Crée une nouvelle séquence. Nom : "Nurturing -- Lead Magnet LMS".

[Création de la séquence]

**[ÉCRAN -- screencast : email 1 -- le problème]**

Email 1 -- Délai : 0 (immédiat). Sujet : "Le piège dans lequel tombent 80% des créateurs de formation".

[Ajout de l'email 1]

Le contenu identifie le problème principal de ton audience. Pas de solution encore. Tu montres que tu comprends leur situation. Tu finis par une question ouverte : "Tu te reconnais là-dedans ?"

Ça crée de l'engagement. Les contacts qui se reconnaissent sont plus susceptibles d'ouvrir les emails suivants.

**[ÉCRAN -- screencast : email 2 -- la valeur]**

Email 2 -- Délai : 3 jours. Sujet : "La méthode que j'utilise pour [résultat concret]".

[Ajout de l'email 2]

Ici, tu partages une méthode ou un framework. Du contenu concret et actionnable. Le contact applique ton conseil et obtient un premier résultat. Ça renforce ta crédibilité.

**[ÉCRAN -- screencast : email 3 -- le témoignage]**

Email 3 -- Délai : 4 jours. Sujet : "Comment [Prénom] est passé de [situation A] à [situation B]".

[Ajout de l'email 3]

Un témoignage détaillé. Pas juste "c'est génial". Le parcours complet : la situation de départ, ce que la personne a fait, le résultat obtenu. Les chiffres rendent le témoignage crédible.

**[ÉCRAN -- screencast : email 4 -- l'erreur courante]**

Email 4 -- Délai : 4 jours. Sujet : "L'erreur qui m'a coûté [X] mois (et comment l'éviter)".

[Ajout de l'email 4]

Tu partages une erreur personnelle ou une erreur fréquente chez tes clients. Être vulnérable renforce la confiance. Et la solution à cette erreur, c'est justement ce que ta formation enseigne.

**[ÉCRAN -- screencast : email 5 -- la projection]**

Email 5 -- Délai : 7 jours. Sujet : "Imagine si [situation idéale du contact]".

[Ajout de l'email 5]

Tu peins le tableau de la situation idéale. Pas de vente ici. Juste de la projection. Le contact visualise ce que serait sa vie après avoir résolu son problème. C'est l'email le plus émotionnel de la séquence.

**[ÉCRAN -- screencast : email 6 -- l'offre]**

Email 6 -- Délai : 3 jours. Sujet : "J'ai créé quelque chose pour toi".

[Ajout de l'email 6]

Première présentation de l'offre. Tu expliques ce que contient ta formation, pour qui c'est fait, et ce que le contact va obtenir concrètement. Un seul lien vers la page de vente. Pas de pression.

**[ÉCRAN -- screencast : email 7 -- la dernière chance]**

Email 7 -- Délai : 2 jours. Sujet : "Dernière chose avant qu'on passe à autre chose".

[Ajout de l'email 7]

Tu rappelles l'offre. Tu lèves les objections courantes : "Est-ce que c'est fait pour moi ?", "Est-ce que j'ai le temps ?", "Et si ça ne marche pas ?". Et tu ajoutes un élément d'urgence si tu en as un : places limitées, bonus temporaire, fermeture des inscriptions.

**[ÉCRAN -- screencast : vue d'ensemble de la séquence]**

Sept emails sur environ un mois. Voici la vue complète.

[Affichage de la séquence avec tous les délais]

**[ÉCRAN -- slide "Métriques à surveiller"]**

Les métriques clés de ta séquence de nurturing :

Taux de complétion : quel pourcentage de contacts reçoit le dernier email ? Si moins de 50% arrivent à l'email 7, tu as un problème de drop-off. Regarde quel email fait décrocher les gens.

Taux d'ouverture par email : il doit rester au-dessus de 25% tout au long de la séquence. Si un email tombe en dessous, retravaille le sujet.

Taux de clic sur l'email d'offre : c'est ton indicateur de conversion. Vise au moins 5%.

**[FACE CAMÉRA]**

Le nurturing, c'est un investissement. Tu écris 7 emails une seule fois, et ils travaillent pour toi pendant des mois. Chaque nouveau contact qui entre dans la séquence reçoit le même parcours optimisé. C'est ton meilleur commercial, et il ne dort jamais.

**[TRANSITION]**

Tu sais convertir des prospects. Mais que fais-tu des contacts qui décrochent ? Dans la prochaine leçon, on construit une séquence de re-engagement.

---

**Points clés** :
- 4 phases : Crédibilité > Preuve > Projection > Offre
- 7 emails sur environ 1 mois (J+0, J+3, J+7, J+11, J+18, J+21, J+23)
- Le premier email identifie le problème, pas la solution
- Témoignages détaillés avec chiffres pour la crédibilité
- Métriques : taux de complétion > 50%, ouverture > 25%, clic offre > 5%

**Mots clés SEO** : séquence nurturing FluentCRM, convertir prospect email, funnel email formation, lead nurturing WordPress

---

## Leçon 5.5 -- Construis une séquence de re-engagement

**Durée** : 7 min
**Type** : Vidéo HeyGen
**Écran** : FluentCRM > Email Sequences

---

**[INTRO -- face caméra]**

Tu as des contacts qui n'ouvrent plus tes emails. Des étudiants qui ont commencé un cours et qui ne l'ont jamais terminé. Ça arrive à tout le monde. La question, c'est : est-ce que tu les laisses partir ou est-ce que tu essaies de les récupérer ? On va construire une séquence de re-engagement.

**[ÉCRAN -- slide "Quand déclencher le re-engagement ?"]**

Première question : quand considérer qu'un contact est "inactif" ?

Pour un abonné email : aucune ouverture depuis 60 jours. C'est le seuil le plus courant.

Pour un étudiant de formation : cours non terminé depuis 14 jours. Si un étudiant ne se connecte pas pendant deux semaines, la probabilité qu'il revienne de lui-même chute à moins de 15%.

Le déclenchement de cette séquence se fait via une automation (Module 6). Pour l'instant, on construit les emails. L'automation viendra connecter le tout.

**[ÉCRAN -- screencast FluentCRM]**

Crée une nouvelle séquence. Nom : "Re-engagement -- Étudiants inactifs".

[Création de la séquence]

**[ÉCRAN -- slide "Structure du re-engagement"]**

Règle fondamentale : trois emails maximum. Le re-engagement, c'est une tentative, pas du harcèlement. Si le contact ne réagit pas après trois emails, tu le laisses tranquille.

Email 1 -- Jour 0 : Le rappel bienveillant. Tu rappelles ce que le contact a commencé sans accuser ni culpabiliser.

Email 2 -- Jour 3 : L'incitation. Tu donnes une raison concrète de revenir. Un nouveau contenu, un conseil exclusif, un raccourci.

Email 3 -- Jour 7 : Le dernier email. Tu annonces que c'est le dernier message. Le contact sait que c'est sa dernière chance d'agir.

**[ÉCRAN -- screencast : email 1 -- le rappel]**

Email 1 -- Délai : 0. Sujet : "Tu en étais où avec [nom du cours] ?".

[Ajout de l'email 1]

Le ton est décontracté. Pas de culpabilisation. Le contenu dit : "J'ai remarqué que tu n'as pas terminé [cours]. C'est normal, ça arrive. Voici le lien direct pour reprendre là où tu t'es arrêté."

Ajoute un lien direct vers la leçon en cours. Pas vers la page d'accueil du cours. Vers la leçon exacte. Moins il y a de friction, plus le contact revient.

**[ÉCRAN -- screencast : email 2 -- l'incitation]**

Email 2 -- Délai : 3 jours. Sujet : "Un raccourci pour [bénéfice concret]".

[Ajout de l'email 2]

Ici, tu donnes une raison nouvelle de revenir. Quelques approches qui fonctionnent :

"J'ai ajouté une ressource bonus dans le Module 3" -- la curiosité pousse à revenir.

"Voici un résumé des 3 points clés du cours en 2 minutes" -- tu réduis l'effort perçu.

"Les membres qui ont terminé ce module ont obtenu [résultat]" -- la preuve sociale motive.

Choisis l'approche qui correspond le mieux à ta formation.

**[ÉCRAN -- screencast : email 3 -- le dernier message]**

Email 3 -- Délai : 4 jours. Sujet : "Je ne vais pas insister".

[Ajout de l'email 3]

C'est l'email le plus important. Tu annonces clairement que c'est ton dernier message sur le sujet. Deux choses à inclure :

Un rappel de ce que le contact perd en ne terminant pas. Pas du chantage, du factuel. "Le Module 4 couvre [compétence clé] -- c'est souvent ce qui fait la différence."

Un dernier lien d'accès direct.

Et c'est tout. Si le contact ne réagit pas, tu respectes son choix.

**[ÉCRAN -- slide "Après la séquence : que faire des contacts inactifs ?"]**

Après les trois emails, deux scénarios.

Le contact a réagi (ouverture ou clic) : l'automation retire le tag "inactif" et le remet dans le parcours normal.

Le contact n'a pas réagi : tu lui ajoutes le tag "inactif-confirmé". Tu ne le supprimes pas de ta base, mais tu arrêtes de lui envoyer des séquences. Il recevra encore tes campagnes ponctuelles, mais c'est tout.

Tous les 6 mois, tu peux faire un nettoyage : envoyer un dernier email "Es-tu toujours intéressé ?" aux contacts "inactif-confirmé". Ceux qui ne réagissent pas, tu les désabonnes. Ça améliore ta délivrabilité.

**[FACE CAMÉRA]**

Le re-engagement, c'est une question de respect. Trois emails, pas plus. Tu donnes au contact l'opportunité de revenir, mais tu ne forces rien. Un contact qui ne veut plus recevoir tes emails et qui n'ose pas se désabonner va te signaler en spam. Et ça, c'est bien pire qu'un désabonnement.

**[TRANSITION]**

Tu as trois séquences opérationnelles : onboarding, nurturing, re-engagement. Mais comment savoir si tes sujets d'emails sont les meilleurs ? Dans la prochaine leçon, on met en place l'A/B testing.

---

**Points clés** :
- Re-engagement étudiant : déclencher après 14 jours d'inactivité
- Re-engagement abonné email : déclencher après 60 jours sans ouverture
- 3 emails maximum : rappel (J0), incitation (J3), dernier message (J7)
- Toujours inclure un lien direct vers le contenu (pas la page d'accueil)
- Après la séquence : tagger "inactif-confirmé" si aucune réaction

**Mots clés SEO** : séquence re-engagement FluentCRM, email relance inactif, récupérer étudiants inactifs, re-engagement email WordPress

---

## Leçon 5.6 -- A/B testing dans tes séquences : teste tes sujets

**Durée** : 5 min
**Type** : Vidéo HeyGen
**Écran** : FluentCRM > Email Sequences

---

**[INTRO -- face caméra]**

Tu as écrit tes emails. Les sujets te semblent bons. Mais est-ce qu'ils sont vraiment les meilleurs ? La seule façon de le savoir, c'est de tester. L'A/B testing, c'est comparer deux versions du même email pour voir laquelle performe le mieux.

**[ÉCRAN -- slide "A/B testing dans les séquences : ce qui est possible"]**

Soyons clairs sur ce que FluentCRM permet et ne permet pas dans les séquences.

Dans les campagnes, l'A/B testing est natif. Tu crées deux sujets, FluentCRM envoie chaque version à une partie de ton audience et garde le gagnant.

Dans les séquences, il n'y a pas de bouton A/B testing intégré. Mais tu peux le faire manuellement. Et c'est même plus fiable, parce que tu contrôles la durée du test.

**[ÉCRAN -- slide "Méthode manuelle d'A/B testing"]**

Voici la méthode en quatre étapes.

Étape 1 : identifie l'email à tester. Commence par celui qui a le taux d'ouverture le plus faible. C'est là qu'il y a le plus de potentiel d'amélioration.

Étape 2 : écris deux sujets. Un seul élément de différence entre les deux. Ne change pas le contenu, juste le sujet. Exemples :

Version A : "La méthode que j'utilise pour [résultat]"
Version B : "3 étapes pour [résultat] (sans [obstacle])"

Étape 3 : alterne les sujets. Pendant deux semaines, utilise le sujet A. Pendant les deux semaines suivantes, utilise le sujet B. Ça te donne environ le même volume de contacts pour chaque version.

Étape 4 : compare les résultats. Après 4 semaines, regarde les taux d'ouverture de chaque version. Le sujet avec le meilleur taux d'ouverture gagne.

**[ÉCRAN -- screencast FluentCRM]**

Ouvre ta séquence et clique sur l'email que tu veux tester.

[Clic sur un email de la séquence]

Change le sujet. Note quelque part (un tableur, une note) la date du changement et le sujet utilisé. FluentCRM ne garde pas l'historique des modifications.

[Modification du sujet]

**[ÉCRAN -- screencast : lecture des stats]**

Pour voir les résultats, clique sur le rapport de ta séquence.

[Clic sur le rapport de la séquence]

Tu vois le taux d'ouverture et le taux de clic pour chaque email. Compare les périodes où chaque sujet était actif.

[Affichage des stats par email]

Attention : il te faut au moins 50 envois par version pour que le test soit significatif. Avec moins, la différence peut être due au hasard.

**[ÉCRAN -- slide "Que tester en priorité ?"]**

Teste d'abord les sujets. C'est le facteur numéro un du taux d'ouverture.

Ensuite, si tu veux aller plus loin :

Le pré-header : c'est le texte qui s'affiche après le sujet sur mobile. Il influence l'ouverture.

L'heure d'envoi : teste 8h vs 14h pendant deux périodes distinctes.

Le premier paragraphe : les 2-3 premières lignes déterminent si le contact lit la suite.

Ne teste jamais plusieurs éléments en même temps. Un seul changement à la fois, sinon tu ne sauras pas ce qui a fait la différence.

**[FACE CAMÉRA]**

L'A/B testing, ce n'est pas un projet ponctuel. C'est une habitude. Chaque mois, teste un sujet. Sur un an, tu auras optimisé les 12 emails les plus importants de tes séquences. Ton taux d'ouverture global augmentera de 5 à 15 points. Ça fait une vraie différence sur tes conversions.

**[TRANSITION]**

Tu sais créer, timer et tester tes séquences. Dans la prochaine leçon, c'est à toi de jouer : tu vas construire ta propre séquence d'onboarding de A à Z.

---

**Points clés** :
- FluentCRM n'a pas d'A/B testing natif dans les séquences -- méthode manuelle en 4 étapes
- Tester un seul élément à la fois (commencer par le sujet)
- Minimum 50 envois par version pour un résultat fiable
- Alterner les sujets sur des périodes de 2 semaines chacune
- Priorité de test : sujet > pré-header > heure d'envoi > premier paragraphe

**Mots clés SEO** : A/B testing email FluentCRM, tester sujet email, optimiser taux ouverture, split test séquence email

---

## Leçon 5.7 -- Exercice : Crée ta séquence d'onboarding en 5 emails

**Durée** : 7 min
**Type** : Exercice guidé
**Écran** : FluentCRM > Email Sequences

---

**[INTRO -- face caméra]**

C'est ton tour. Tu vas créer ta propre séquence d'onboarding de A à Z. Pas un copier-coller de ce qu'on a vu. Ta séquence, adaptée à ta formation, à ton audience, à ton ton. Je te guide étape par étape.

**[ÉCRAN -- slide "Consignes de l'exercice"]**

Voici ce que tu vas produire :

Une séquence de 5 emails répartis sur 7 jours. Chaque email a un objectif précis. Tu dois écrire les sujets et le contenu toi-même.

**[ÉCRAN -- slide "Étape 1 : Définis le contexte"]**

Avant d'ouvrir FluentCRM, réponds à ces trois questions :

1. Qui entre dans cette séquence ? Un nouvel inscrit à ta newsletter, un membre gratuit, un participant à un webinaire ?

2. Quel est l'objectif final ? Vendre ta formation premium, obtenir un rendez-vous, générer un premier achat ?

3. Quelle est la principale objection de ton audience ? "C'est trop cher", "Je n'ai pas le temps", "Je ne sais pas si ça marche" ?

Note tes réponses. Elles vont guider chaque email.

**[ÉCRAN -- slide "Étape 2 : Écris tes 5 sujets"]**

Maintenant, écris les sujets de tes 5 emails en suivant cette structure :

Email 1 (J0) -- Bienvenue : accueille et donne accès au contenu promis. Sujet direct, pas de mystère.

Email 2 (J1) -- Valeur : partage un conseil actionnable. Le sujet doit promettre un bénéfice concret.

Email 3 (J3) -- Preuve sociale : témoignage ou étude de cas. Le sujet doit mentionner un résultat chiffré.

Email 4 (J5) -- Contenu avancé : un aperçu de ton offre premium. Le sujet doit susciter la curiosité.

Email 5 (J7) -- Offre : appel à l'action. Le sujet doit être clair et direct.

Écris tes 5 sujets avant de passer à la suite.

**[ÉCRAN -- slide "Étape 3 : Rédige tes emails"]**

Pour chaque email, respecte ces règles :

Longueur : 150-250 mots maximum. Un email de séquence n'est pas un article de blog.

Structure : une phrase d'accroche, un contenu principal, un appel à l'action. Trois blocs, pas plus.

Personnalisation : utilise au minimum {{contact.first_name}} dans le premier email.

Un seul appel à l'action par email. Pas deux liens, pas trois boutons. Un seul.

**[ÉCRAN -- slide "Étape 4 : Configure dans FluentCRM"]**

Ouvre FluentCRM. Crée ta séquence.

Checklist de configuration :

- [ ] Nom de la séquence (interne, descriptif)
- [ ] 5 emails ajoutés dans l'ordre
- [ ] Délais : 0, 1, 2, 2, 2 jours
- [ ] Jours d'envoi : lundi à vendredi
- [ ] Fenêtre horaire : 8h-10h
- [ ] Fuseau horaire correct

**[ÉCRAN -- slide "Étape 5 : Teste"]**

Avant de publier :

1. Inscris-toi dans la séquence avec ton adresse email de test
2. Vérifie que le premier email arrive dans ta boîte
3. Relis chaque email sur mobile (pas seulement sur desktop)
4. Vérifie que les liens fonctionnent
5. Vérifie que les smart codes s'affichent correctement

**[ÉCRAN -- slide "Grille d'auto-évaluation"]**

Note chaque email sur ces critères :

| Critère | Oui/Non |
| --- | --- |
| Le sujet donne envie d'ouvrir | |
| Le contenu tient en 250 mots | |
| Il y a un seul appel à l'action | |
| Le ton est personnel et direct | |
| L'email apporte de la valeur (pas juste de la vente) | |

Si tu as 4/5 ou plus sur chaque email, ta séquence est prête.

**[FACE CAMÉRA]**

Prends le temps de bien faire cet exercice. Une bonne séquence d'onboarding travaille pour toi pendant des mois. Chaque nouvel inscrit reçoit le même parcours optimisé. C'est du temps investi une seule fois pour un retour continu.

---

**Points clés** :
- Définir le contexte avant d'écrire : audience, objectif, objection principale
- 5 emails : Bienvenue > Valeur > Preuve > Aperçu > Offre
- 150-250 mots par email, un seul appel à l'action
- Toujours tester sur mobile avant de publier
- Grille d'auto-évaluation : 5 critères par email

**Mots clés SEO** : exercice séquence email, créer onboarding email, template séquence FluentCRM, emails automatiques formation

---

## Quiz M5 -- Email séquences et nurturing

**Type** : Quiz TutorLMS (8 questions)
**Seuil de réussite** : 80%

**Question 1** : Quelle est la différence principale entre une campagne et une séquence dans FluentCRM ?
- A) La campagne est gratuite, la séquence est payante
- B) La campagne est un envoi ponctuel, la séquence est une série automatique dans un ordre fixe *(bonne réponse)*
- C) La séquence ne peut contenir que 3 emails
- D) La campagne utilise des templates, la séquence non

**Question 2** : Quel délai recommande-t-on pour le premier email d'une séquence d'onboarding ?
- A) 24 heures
- B) 1 jour
- C) 0 -- envoi immédiat *(bonne réponse)*
- D) 2 heures

**Question 3** : Dans la structure de séquence d'onboarding schoolsWP, quel est l'objectif de l'email 3 (J+3) ?
- A) Présenter l'offre payante
- B) Partager un témoignage ou une preuve sociale *(bonne réponse)*
- C) Envoyer un code promo
- D) Demander un feedback

**Question 4** : Pourquoi est-il recommandé d'utiliser "1 jour" plutôt que "24 heures" comme délai entre deux emails ?
- A) Ça coûte moins cher en ressources serveur
- B) "1 jour" respecte la fenêtre horaire configurée, "24 heures" envoie exactement 24h après *(bonne réponse)*
- C) FluentCRM ne supporte pas les heures
- D) Ça évite les doublons

**Question 5** : Combien d'emails maximum doit contenir une séquence de re-engagement ?
- A) 1
- B) 3 *(bonne réponse)*
- C) 5
- D) 7

**Question 6** : Après combien de jours d'inactivité doit-on déclencher une séquence de re-engagement pour un étudiant de formation ?
- A) 3 jours
- B) 7 jours
- C) 14 jours *(bonne réponse)*
- D) 30 jours

**Question 7** : Quel est le minimum d'envois par version nécessaire pour un A/B test fiable sur un sujet d'email ?
- A) 10
- B) 25
- C) 50 *(bonne réponse)*
- D) 100

**Question 8** : Quelle est la fenêtre horaire d'envoi recommandée pour une séquence professionnelle ?
- A) 6h-7h
- B) 8h-10h *(bonne réponse)*
- C) 12h-14h
- D) 18h-20h
