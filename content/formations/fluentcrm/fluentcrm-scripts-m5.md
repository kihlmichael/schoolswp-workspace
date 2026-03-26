# Scripts video -- Module 5 : Email sequences et nurturing

**Formation** : Maitriser FluentCRM
**Module** : M5 -- Email sequences et nurturing (Premium)
**Lecons** : 6 videos + 1 exercice + 1 quiz
**Duree totale** : ~50 min de video
**Date** : 2026-03-23

---

## Lecon 5.1 -- Comprends les sequences : quand les utiliser vs une campagne

**Duree** : 5 min
**Type** : Video HeyGen
**Ecran** : FluentCRM > Email Sequences

---

**[INTRO -- face camera]**

Tu sais envoyer des campagnes. Mais une campagne, c'est un envoi ponctuel. Tu l'envoies, c'est fini. Une sequence, c'est different : c'est une serie d'emails envoyes automatiquement dans un ordre precis, avec des delais entre chaque envoi. Et c'est la que ton email marketing devient vraiment efficace.

**[ECRAN -- slide "Campagne vs Sequence vs Automation"]**

Posons les bases clairement. Il y a trois outils d'envoi dans FluentCRM, et chacun a un role precis.

La campagne : un email envoye a une audience a un moment donne. Une newsletter, une promo, une annonce. C'est du one-shot.

La sequence : une serie d'emails envoyes automatiquement, dans l'ordre, avec des delais configures. Chaque contact qui entre dans la sequence recoit le meme parcours, mais a son propre rythme.

L'automation : un workflow visuel avec des conditions, des branches, des declencheurs. C'est plus puissant, mais plus complexe. On le verra dans le Module 6.

**[ECRAN -- slide "Quand utiliser quoi ?"]**

Utilise une campagne quand tu envoies un message ponctuel a un groupe de contacts. Un lancement, une newsletter mensuelle, une annonce.

Utilise une sequence quand tu veux qu'un contact recoive une serie d'emails predetermines dans un ordre fixe. L'onboarding d'un nouvel inscrit, le nurturing d'un prospect, la relance d'un contact inactif.

Utilise une automation quand tu as besoin de logique conditionnelle. Si le contact ouvre l'email, il va dans la branche A. S'il ne l'ouvre pas, branche B. On n'en est pas encore la.

**[ECRAN -- screencast FluentCRM > Email Sequences]**

Dans FluentCRM, va dans Email Sequences dans le menu lateral.

[Clic sur Email Sequences]

Tu arrives sur la liste de tes sequences. Si tu n'en as pas encore, c'est vide. Et c'est normal.

Clique sur "Create New Sequence".

[Clic sur Create New Sequence]

Tu vois l'interface de creation. Un titre, et ensuite tu ajoutes tes emails un par un. Chaque email a un delai, un sujet, un contenu. Le premier email part immediatement quand le contact entre dans la sequence. Les suivants partent apres le delai que tu as configure.

**[ECRAN -- slide "Cas d'usage concrets schoolsWP"]**

Voici les sequences les plus utiles quand tu vends des formations en ligne :

Sequence d'onboarding : un nouvel inscrit recoit 4-5 emails sur 7 jours. Bienvenue, contenu gratuit, temoignage, offre.

Sequence de nurturing : un prospect qui a telecharge un lead magnet recoit une serie d'emails qui le fait passer de "curieux" a "pret a acheter".

Sequence de re-engagement : un etudiant qui n'a pas termine son cours depuis 14 jours recoit une serie d'emails pour le remotiver.

Sequence post-achat : un client qui vient d'acheter recoit des emails pour maximiser sa satisfaction et reduire les demandes de remboursement.

**[FACE CAMERA]**

Retiens ca : une campagne parle a un groupe a un instant T. Une sequence accompagne chaque individu dans un parcours. C'est la difference entre crier dans un megaphone et avoir une conversation personnalisee.

**[TRANSITION]**

Tu comprends maintenant quand utiliser quoi. Dans la prochaine lecon, on cree ta premiere sequence d'onboarding, email par email.

---

**Points cles** :
- Campagne = envoi ponctuel. Sequence = serie automatique. Automation = workflow conditionnel.
- Utiliser une sequence quand chaque contact doit recevoir le meme parcours a son propre rythme
- Cas d'usage cles : onboarding, nurturing, re-engagement, post-achat
- Le premier email d'une sequence part immediatement, les suivants selon les delais configures

**Mots cles SEO** : sequence email FluentCRM, campagne vs sequence, email automation WordPress, nurturing email marketing

---

## Lecon 5.2 -- Cree ta premiere sequence d'onboarding

**Duree** : 7 min
**Type** : Video HeyGen
**Ecran** : FluentCRM > Email Sequences > Create

---

**[INTRO -- face camera]**

On passe a la pratique. On va creer ensemble une sequence d'onboarding pour accueillir les nouveaux inscrits a ta formation gratuite. Cinq emails, sept jours. A la fin de cette lecon, ta sequence sera prete.

**[ECRAN -- screencast FluentCRM]**

Va dans Email Sequences et clique sur "Create New Sequence".

[Clic sur Create New Sequence]

Donne un nom a ta sequence. Par exemple : "Onboarding -- Nouveau membre". Ce nom est interne, tes contacts ne le verront pas.

[Saisie du titre]

Tu arrives sur l'interface de la sequence. C'est une liste verticale ou chaque ligne est un email. Pour l'instant, c'est vide.

**[ECRAN -- slide "Structure de la sequence onboarding"]**

Avant de plonger dans FluentCRM, voici la structure qu'on va suivre. C'est un modele eprouve pour les createurs de formation.

Email 1 -- Jour 0 : Bienvenue. Presente-toi, donne acces au contenu gratuit, fixe les attentes.

Email 2 -- Jour 1 : Valeur gratuite. Partage un conseil actionnable ou une ressource complementaire. Tu montres ton expertise.

Email 3 -- Jour 3 : Temoignage. Partage le retour d'experience d'un utilisateur. La preuve sociale fait le travail a ta place.

Email 4 -- Jour 5 : Contenu avance. Un apercu de ce que contient la formation payante. Tu donnes un avant-gout sans tout devoiler.

Email 5 -- Jour 7 : Offre. Presente ta formation premium avec un appel a l'action clair.

**[ECRAN -- screencast : creation du premier email]**

Clique sur "Add Email" ou le bouton "+" pour ajouter ton premier email.

[Clic sur Add Email]

Remplis le sujet. Pour le premier email : "Bienvenue {{contact.first_name}} -- ton acces est pret".

[Saisie du sujet]

Le delai d'attente : mets 0. Le premier email part immediatement quand le contact entre dans la sequence.

[Configuration du delai a 0]

Maintenant, redige le contenu. Sois direct. Presente-toi en une phrase, donne le lien d'acces au contenu gratuit, et dis au contact ce qu'il va recevoir dans les prochains jours.

[Redaction du contenu -- screencast]

Exemple de structure :

"Salut {{contact.first_name}},

Je suis [Prenom], createur de [Nom formation].

Ton acces est pret : [lien].

Dans les prochains jours, je vais te partager des ressources pour aller plus loin. Reste a l'affut."

Pas besoin d'en faire trop. Court, clair, utile.

**[ECRAN -- screencast : ajout des emails suivants]**

Clique de nouveau sur "Add Email" pour l'email 2.

[Clic sur Add Email]

Le delai cette fois : 1 jour. Ca signifie que cet email partira 24 heures apres le precedent.

[Configuration du delai a 1 jour]

Sujet : "Un conseil que j'aurais aime avoir plus tot". Redige un contenu court avec une astuce concrere liee a ta thematique.

[Saisie du sujet et redaction rapide]

On continue. Email 3 : delai 2 jours apres l'email 2 (donc J+3 au total). Sujet : "Comment [Prenom du temoignage] a obtenu [resultat]". Tu partages un temoignage ou une etude de cas.

[Ajout de l'email 3 avec delai et sujet]

Email 4 : delai 2 jours. Sujet : "Ce que 90% des gens font mal avec [sujet]". Tu donnes un apercu du contenu premium.

[Ajout de l'email 4]

Email 5 : delai 2 jours. Sujet : "Pret a passer au niveau suivant ?". C'est ton email de vente. Presente l'offre, les benefices, un bouton clair.

[Ajout de l'email 5]

**[ECRAN -- screencast : vue d'ensemble de la sequence]**

Ta sequence est complete. Cinq emails, repartis sur 7 jours.

[Vue de la liste des 5 emails avec leurs delais]

Verifie l'ordre, les delais, les sujets. Si tu veux reorganiser, tu peux glisser-deposer les emails.

**[ECRAN -- screencast : parametres de la sequence]**

Avant de publier, clique sur les parametres de la sequence en haut.

[Clic sur Settings]

Tu peux configurer les jours et heures d'envoi. On verra ca en detail dans la lecon suivante. Pour l'instant, laisse les parametres par defaut.

Clique sur "Publish" ou active la sequence.

[Clic sur Publish]

**[FACE CAMERA]**

Ta sequence d'onboarding est prete. Mais elle ne fera rien tant que tu n'y inscris pas de contacts. Pour ca, tu as deux options : inscrire manuellement des contacts depuis leur fiche, ou automatiser l'inscription via une automation. L'automation, c'est le Module 6.

En attendant, tu peux inscrire un contact test pour verifier que tout fonctionne.

**[TRANSITION]**

Ta sequence existe. Mais le timing, c'est ce qui fait la difference entre un email lu et un email ignore. Dans la prochaine lecon, on configure les delais, les jours et les heures d'envoi.

---

**Points cles** :
- Structure onboarding : Bienvenue (J0) > Valeur gratuite (J1) > Temoignage (J3) > Contenu avance (J5) > Offre (J7)
- Le premier email a un delai de 0 (envoi immediat)
- Les delais sont relatifs a l'email precedent, pas au premier email
- Inscrire un contact test pour verifier le parcours avant de lancer
- L'inscription automatique se fait via une automation (Module 6)

**Mots cles SEO** : sequence onboarding FluentCRM, creer sequence email, email bienvenue automatique, funnel email WordPress

---

## Lecon 5.3 -- Configure le timing : delais, jours specifiques, heures d'envoi

**Duree** : 6 min
**Type** : Video HeyGen
**Ecran** : FluentCRM > Email Sequences > Settings

---

**[INTRO -- face camera]**

Tu as ta sequence. Mais si tes emails partent a 3h du matin un dimanche, personne ne les lira. Le timing, c'est ce qui transforme un bon email en email ouvert. FluentCRM te donne un controle precis la-dessus.

**[ECRAN -- screencast FluentCRM > Sequence > Settings]**

Ouvre ta sequence et clique sur les parametres en haut.

[Clic sur Settings de la sequence]

Tu vois trois reglages principaux : les jours d'envoi, les heures d'envoi et le fuseau horaire.

**[ECRAN -- screencast : jours d'envoi]**

Premier reglage : les jours d'envoi. Par defaut, FluentCRM envoie tous les jours, du lundi au dimanche.

[Affichage des cases a cocher des jours]

Pour une sequence professionnelle, desactive le samedi et le dimanche. La plupart des formations en ligne ciblent des professionnels ou des independants. Leurs boites de reception sont actives en semaine.

[Decochage samedi et dimanche]

Si un email est programme un samedi, FluentCRM le decale automatiquement au lundi suivant. Pas besoin de recalculer tes delais.

**[ECRAN -- screencast : heures d'envoi]**

Deuxieme reglage : la fenetre horaire. Tu definis une heure de debut et une heure de fin.

[Configuration de la fenetre horaire]

Regle recommandee : entre 8h et 10h du matin. C'est le moment ou la plupart des gens consultent leurs emails. Autre creneau efficace : 14h-15h, juste apres la pause dejeuner.

Evite les envois apres 18h. L'email sera noye dans les newsletters du soir.

**[ECRAN -- screencast : fuseau horaire]**

Troisieme reglage : le fuseau horaire. FluentCRM utilise le fuseau horaire de ton site WordPress.

[Affichage du reglage timezone]

Verifie dans WordPress > Reglages > General que ton fuseau est correct. Si ton audience est en France, assure-toi que c'est bien Europe/Paris.

Si tu as une audience internationale, choisis le fuseau de la majorite de tes contacts. FluentCRM ne gere pas les envois par fuseau horaire individuel -- c'est une limitation a connaitre.

**[ECRAN -- slide "Timing optimal par type de sequence"]**

Le bon timing depend du type de sequence.

Onboarding : J+0, J+1, J+3, J+5, J+7. Rythme soutenu les premiers jours, puis on espace. Le contact est "chaud", il veut du contenu.

Nurturing : J+0, J+3, J+7, J+14, J+21. Plus espace. Tu construis la relation dans la duree sans etre envahissant.

Re-engagement : J+0, J+3, J+7. Trois emails maximum. Si le contact ne reagit pas apres trois tentatives, arrete. Insister ne sert a rien.

**[ECRAN -- screencast : delai par email]**

Reviens dans la liste des emails de ta sequence. Chaque email a son propre delai.

[Affichage de la liste des emails avec delais]

Clique sur le delai d'un email pour le modifier. Tu peux le definir en jours ou en heures.

[Modification du delai d'un email]

Astuce : pour le deuxieme email, mets 1 jour plutot que 24 heures. "1 jour" respecte la fenetre horaire que tu as configuree. "24 heures" envoie exactement 24 heures apres, meme si ca tombe en dehors de ta fenetre.

**[FACE CAMERA]**

Ne change pas le timing toutes les semaines. Configure une fois, lance, et analyse les resultats apres au moins 50 contacts passes dans la sequence. Avant ca, tu n'as pas assez de donnees pour optimiser.

**[TRANSITION]**

Le timing est cale. Dans la prochaine lecon, on construit une sequence plus ambitieuse : le nurturing. L'objectif : transformer un prospect en acheteur.

---

**Points cles** :
- Desactiver les envois le week-end pour une audience professionnelle
- Fenetre d'envoi recommandee : 8h-10h ou 14h-15h
- Verifier le fuseau horaire dans WordPress > Reglages > General
- Utiliser "jours" plutot que "heures" pour respecter la fenetre d'envoi
- Timing onboarding : J+0, J+1, J+3, J+5, J+7. Nurturing : plus espace. Re-engagement : 3 emails max.

**Mots cles SEO** : timing email FluentCRM, heure envoi email, delai sequence email, optimiser envoi email WordPress

---

## Lecon 5.4 -- Construis une sequence de nurturing (lead vers acheteur)

**Duree** : 8 min
**Type** : Video HeyGen
**Ecran** : FluentCRM > Email Sequences

---

**[INTRO -- face camera]**

L'onboarding accueille. Le nurturing convertit. Un contact qui telecharge ton lead magnet n'est pas pret a acheter. Pas encore. La sequence de nurturing, c'est le pont entre "je te decouvre" et "je te fais confiance, je passe a l'action".

**[ECRAN -- slide "Anatomie d'une sequence de nurturing"]**

Une bonne sequence de nurturing suit une progression psychologique. Pas une suite d'emails au hasard.

Phase 1 -- Credibilite (emails 1-2) : tu montres que tu comprends le probleme du contact. Tu donnes de la valeur sans rien demander.

Phase 2 -- Preuve (emails 3-4) : tu partages des resultats concrets. Temoignages, etudes de cas, chiffres. Le contact commence a se dire "ca marche vraiment".

Phase 3 -- Projection (email 5) : tu aides le contact a se projeter. A quoi ressemble sa situation apres avoir utilise ta solution ?

Phase 4 -- Offre (emails 6-7) : tu presentes ton offre avec un appel a l'action clair. Tu leves les dernieres objections.

**[ECRAN -- screencast FluentCRM]**

Cree une nouvelle sequence. Nom : "Nurturing -- Lead Magnet LMS".

[Creation de la sequence]

**[ECRAN -- screencast : email 1 -- le probleme]**

Email 1 -- Delai : 0 (immediat). Sujet : "Le piege dans lequel tombent 80% des createurs de formation".

[Ajout de l'email 1]

Le contenu identifie le probleme principal de ton audience. Pas de solution encore. Tu montres que tu comprends leur situation. Tu finis par une question ouverte : "Tu te reconnais la-dedans ?"

Ca cree de l'engagement. Les contacts qui se reconnaissent sont plus susceptibles d'ouvrir les emails suivants.

**[ECRAN -- screencast : email 2 -- la valeur]**

Email 2 -- Delai : 3 jours. Sujet : "La methode que j'utilise pour [resultat concret]".

[Ajout de l'email 2]

Ici, tu partages une methode ou un framework. Du contenu concret et actionnable. Le contact applique ton conseil et obtient un premier resultat. Ca renforce ta credibilite.

**[ECRAN -- screencast : email 3 -- le temoignage]**

Email 3 -- Delai : 4 jours. Sujet : "Comment [Prenom] est passe de [situation A] a [situation B]".

[Ajout de l'email 3]

Un temoignage detaille. Pas juste "c'est genial". Le parcours complet : la situation de depart, ce que la personne a fait, le resultat obtenu. Les chiffres rendent le temoignage credible.

**[ECRAN -- screencast : email 4 -- l'erreur courante]**

Email 4 -- Delai : 4 jours. Sujet : "L'erreur qui m'a coute [X] mois (et comment l'eviter)".

[Ajout de l'email 4]

Tu partages une erreur personnelle ou une erreur frequente chez tes clients. Etre vulnerable renforce la confiance. Et la solution a cette erreur, c'est justement ce que ta formation enseigne.

**[ECRAN -- screencast : email 5 -- la projection]**

Email 5 -- Delai : 7 jours. Sujet : "Imagine si [situation ideale du contact]".

[Ajout de l'email 5]

Tu peins le tableau de la situation ideale. Pas de vente ici. Juste de la projection. Le contact visualise ce que serait sa vie apres avoir resolu son probleme. C'est l'email le plus emotionnel de la sequence.

**[ECRAN -- screencast : email 6 -- l'offre]**

Email 6 -- Delai : 3 jours. Sujet : "J'ai cree quelque chose pour toi".

[Ajout de l'email 6]

Premiere presentation de l'offre. Tu expliques ce que contient ta formation, pour qui c'est fait, et ce que le contact va obtenir concretement. Un seul lien vers la page de vente. Pas de pression.

**[ECRAN -- screencast : email 7 -- la derniere chance]**

Email 7 -- Delai : 2 jours. Sujet : "Derniere chose avant qu'on passe a autre chose".

[Ajout de l'email 7]

Tu rappelles l'offre. Tu leves les objections courantes : "Est-ce que c'est fait pour moi ?", "Est-ce que j'ai le temps ?", "Et si ca ne marche pas ?". Et tu ajoutes un element d'urgence si tu en as un : places limitees, bonus temporaire, fermeture des inscriptions.

**[ECRAN -- screencast : vue d'ensemble de la sequence]**

Sept emails sur environ un mois. Voici la vue complete.

[Affichage de la sequence avec tous les delais]

**[ECRAN -- slide "Metrics a surveiller"]**

Les metriques cles de ta sequence de nurturing :

Taux de completion : quel pourcentage de contacts recoit le dernier email ? Si moins de 50% arrivent a l'email 7, tu as un probleme de drop-off. Regarde quel email fait decrocher les gens.

Taux d'ouverture par email : il doit rester au-dessus de 25% tout au long de la sequence. Si un email tombe en dessous, retravaille le sujet.

Taux de clic sur l'email d'offre : c'est ton indicateur de conversion. Vise au moins 5%.

**[FACE CAMERA]**

Le nurturing, c'est un investissement. Tu ecris 7 emails une seule fois, et ils travaillent pour toi pendant des mois. Chaque nouveau contact qui entre dans la sequence recoit le meme parcours optimise. C'est ton meilleur commercial, et il ne dort jamais.

**[TRANSITION]**

Tu sais convertir des prospects. Mais que fais-tu des contacts qui decrochent ? Dans la prochaine lecon, on construit une sequence de re-engagement.

---

**Points cles** :
- 4 phases : Credibilite > Preuve > Projection > Offre
- 7 emails sur environ 1 mois (J+0, J+3, J+7, J+11, J+18, J+21, J+23)
- Le premier email identifie le probleme, pas la solution
- Temoignages detailles avec chiffres pour la credibilite
- Metriques : taux de completion > 50%, ouverture > 25%, clic offre > 5%

**Mots cles SEO** : sequence nurturing FluentCRM, convertir prospect email, funnel email formation, lead nurturing WordPress

---

## Lecon 5.5 -- Construis une sequence de re-engagement

**Duree** : 7 min
**Type** : Video HeyGen
**Ecran** : FluentCRM > Email Sequences

---

**[INTRO -- face camera]**

Tu as des contacts qui n'ouvrent plus tes emails. Des etudiants qui ont commence un cours et qui ne l'ont jamais termine. Ca arrive a tout le monde. La question, c'est : est-ce que tu les laisses partir ou est-ce que tu essaies de les recuperer ? On va construire une sequence de re-engagement.

**[ECRAN -- slide "Quand declencher le re-engagement ?"]**

Premiere question : quand considerer qu'un contact est "inactif" ?

Pour un abonne email : aucune ouverture depuis 60 jours. C'est le seuil le plus courant.

Pour un etudiant de formation : cours non termine depuis 14 jours. Si un etudiant ne se connecte pas pendant deux semaines, la probabilite qu'il revienne de lui-meme chute a moins de 15%.

Le declenchement de cette sequence se fait via une automation (Module 6). Pour l'instant, on construit les emails. L'automation viendra connecter le tout.

**[ECRAN -- screencast FluentCRM]**

Cree une nouvelle sequence. Nom : "Re-engagement -- Etudiants inactifs".

[Creation de la sequence]

**[ECRAN -- slide "Structure du re-engagement"]**

Regle fondamentale : trois emails maximum. Le re-engagement, c'est une tentative, pas du harcelement. Si le contact ne reagit pas apres trois emails, tu le laisses tranquille.

Email 1 -- Jour 0 : Le rappel bienveillant. Tu rappelles ce que le contact a commence sans accuser ni culpabiliser.

Email 2 -- Jour 3 : L'incitation. Tu donnes une raison concrere de revenir. Un nouveau contenu, un conseil exclusif, un raccourci.

Email 3 -- Jour 7 : Le dernier email. Tu annonces que c'est le dernier message. Le contact sait que c'est sa derniere chance d'agir.

**[ECRAN -- screencast : email 1 -- le rappel]**

Email 1 -- Delai : 0. Sujet : "Tu en etais ou avec [nom du cours] ?".

[Ajout de l'email 1]

Le ton est decontracte. Pas de culpabilisation. Le contenu dit : "J'ai remarque que tu n'as pas termine [cours]. C'est normal, ca arrive. Voici le lien direct pour reprendre la ou tu t'es arrete."

Ajoute un lien direct vers la lecon en cours. Pas vers la page d'accueil du cours. Vers la lecon exacte. Moins il y a de friction, plus le contact revient.

**[ECRAN -- screencast : email 2 -- l'incitation]**

Email 2 -- Delai : 3 jours. Sujet : "Un raccourci pour [benefice concret]".

[Ajout de l'email 2]

Ici, tu donnes une raison nouvelle de revenir. Quelques approches qui fonctionnent :

"J'ai ajoute une ressource bonus dans le Module 3" -- la curiosite pousse a revenir.

"Voici un resume des 3 points cles du cours en 2 minutes" -- tu reduis l'effort percu.

"Les membres qui ont termine ce module ont obtenu [resultat]" -- la preuve sociale motive.

Choisis l'approche qui correspond le mieux a ta formation.

**[ECRAN -- screencast : email 3 -- le dernier message]**

Email 3 -- Delai : 4 jours. Sujet : "Je ne vais pas insister".

[Ajout de l'email 3]

C'est l'email le plus important. Tu annonces clairement que c'est ton dernier message sur le sujet. Deux choses a inclure :

Un rappel de ce que le contact perd en ne terminant pas. Pas du chantage, du factuel. "Le Module 4 couvre [competence cle] -- c'est souvent ce qui fait la difference."

Un dernier lien d'acces direct.

Et c'est tout. Si le contact ne reagit pas, tu respectes son choix.

**[ECRAN -- slide "Apres la sequence : que faire des contacts inactifs ?"]**

Apres les trois emails, deux scenarios.

Le contact a reagi (ouverture ou clic) : l'automation retire le tag "inactif" et le remet dans le parcours normal.

Le contact n'a pas reagi : tu lui ajoutes le tag "inactif-confirme". Tu ne le supprimes pas de ta base, mais tu arretes de lui envoyer des sequences. Il recevra encore tes campagnes ponctuelles, mais c'est tout.

Tous les 6 mois, tu peux faire un nettoyage : envoyer un dernier email "Es-tu toujours interesse ?" aux contacts "inactif-confirme". Ceux qui ne reagissent pas, tu les desabonnes. Ca ameliore ta delivrabilite.

**[FACE CAMERA]**

Le re-engagement, c'est une question de respect. Trois emails, pas plus. Tu donnes au contact l'opportunite de revenir, mais tu ne forces rien. Un contact qui ne veut plus recevoir tes emails et qui n'ose pas se desabonner va te signaler en spam. Et ca, c'est bien pire qu'un desabonnement.

**[TRANSITION]**

Tu as trois sequences operationnelles : onboarding, nurturing, re-engagement. Mais comment savoir si tes sujets d'emails sont les meilleurs ? Dans la prochaine lecon, on met en place l'A/B testing.

---

**Points cles** :
- Re-engagement etudiant : declencher apres 14 jours d'inactivite
- Re-engagement abonne email : declencher apres 60 jours sans ouverture
- 3 emails maximum : rappel (J0), incitation (J3), dernier message (J7)
- Toujours inclure un lien direct vers le contenu (pas la page d'accueil)
- Apres la sequence : tagger "inactif-confirme" si aucune reaction

**Mots cles SEO** : sequence re-engagement FluentCRM, email relance inactif, recuperer etudiants inactifs, re-engagement email WordPress

---

## Lecon 5.6 -- A/B testing dans tes sequences : teste tes sujets

**Duree** : 5 min
**Type** : Video HeyGen
**Ecran** : FluentCRM > Email Sequences

---

**[INTRO -- face camera]**

Tu as ecrit tes emails. Les sujets te semblent bons. Mais est-ce qu'ils sont vraiment les meilleurs ? La seule facon de le savoir, c'est de tester. L'A/B testing, c'est comparer deux versions du meme email pour voir laquelle performe le mieux.

**[ECRAN -- slide "A/B testing dans les sequences : ce qui est possible"]**

Soyons clairs sur ce que FluentCRM permet et ne permet pas dans les sequences.

Dans les campagnes, l'A/B testing est natif. Tu crees deux sujets, FluentCRM envoie chaque version a une partie de ton audience et garde le gagnant.

Dans les sequences, il n'y a pas de bouton A/B testing integre. Mais tu peux le faire manuellement. Et c'est meme plus fiable, parce que tu controles la duree du test.

**[ECRAN -- slide "Methode manuelle d'A/B testing"]**

Voici la methode en quatre etapes.

Etape 1 : identifie l'email a tester. Commence par celui qui a le taux d'ouverture le plus faible. C'est la qu'il y a le plus de potentiel d'amelioration.

Etape 2 : ecris deux sujets. Un seul element de difference entre les deux. Ne change pas le contenu, juste le sujet. Exemples :

Version A : "La methode que j'utilise pour [resultat]"
Version B : "3 etapes pour [resultat] (sans [obstacle])"

Etape 3 : alterne les sujets. Pendant deux semaines, utilise le sujet A. Pendant les deux semaines suivantes, utilise le sujet B. Ca te donne environ le meme volume de contacts pour chaque version.

Etape 4 : compare les resultats. Apres 4 semaines, regarde les taux d'ouverture de chaque version. Le sujet avec le meilleur taux d'ouverture gagne.

**[ECRAN -- screencast FluentCRM]**

Ouvre ta sequence et clique sur l'email que tu veux tester.

[Clic sur un email de la sequence]

Change le sujet. Note quelque part (un tableur, une note) la date du changement et le sujet utilise. FluentCRM ne garde pas l'historique des modifications.

[Modification du sujet]

**[ECRAN -- screencast : lecture des stats]**

Pour voir les resultats, clique sur le rapport de ta sequence.

[Clic sur le rapport de la sequence]

Tu vois le taux d'ouverture et le taux de clic pour chaque email. Compare les periodes ou chaque sujet etait actif.

[Affichage des stats par email]

Attention : il te faut au moins 50 envois par version pour que le test soit significatif. Avec moins, la difference peut etre due au hasard.

**[ECRAN -- slide "Que tester en priorite ?"]**

Teste d'abord les sujets. C'est le facteur numero un du taux d'ouverture.

Ensuite, si tu veux aller plus loin :

Le pre-header : c'est le texte qui s'affiche apres le sujet sur mobile. Il influence l'ouverture.

L'heure d'envoi : teste 8h vs 14h pendant deux periodes distinctes.

Le premier paragraphe : les 2-3 premieres lignes determinent si le contact lit la suite.

Ne teste jamais plusieurs elements en meme temps. Un seul changement a la fois, sinon tu ne sauras pas ce qui a fait la difference.

**[FACE CAMERA]**

L'A/B testing, ce n'est pas un projet ponctuel. C'est une habitude. Chaque mois, teste un sujet. Sur un an, tu auras optimise les 12 emails les plus importants de tes sequences. Ton taux d'ouverture global augmentera de 5 a 15 points. Ca fait une vraie difference sur tes conversions.

**[TRANSITION]**

Tu sais creer, timer et tester tes sequences. Dans la prochaine lecon, c'est a toi de jouer : tu vas construire ta propre sequence d'onboarding de A a Z.

---

**Points cles** :
- FluentCRM n'a pas d'A/B testing natif dans les sequences -- methode manuelle en 4 etapes
- Tester un seul element a la fois (commencer par le sujet)
- Minimum 50 envois par version pour un resultat fiable
- Alterner les sujets sur des periodes de 2 semaines chacune
- Priorite de test : sujet > pre-header > heure d'envoi > premier paragraphe

**Mots cles SEO** : A/B testing email FluentCRM, tester sujet email, optimiser taux ouverture, split test sequence email

---

## Lecon 5.7 -- Exercice : Cree ta sequence d'onboarding en 5 emails

**Duree** : 7 min
**Type** : Exercice guide
**Ecran** : FluentCRM > Email Sequences

---

**[INTRO -- face camera]**

C'est ton tour. Tu vas creer ta propre sequence d'onboarding de A a Z. Pas un copier-coller de ce qu'on a vu. Ta sequence, adaptee a ta formation, a ton audience, a ton ton. Je te guide etape par etape.

**[ECRAN -- slide "Consignes de l'exercice"]**

Voici ce que tu vas produire :

Une sequence de 5 emails repartis sur 7 jours. Chaque email a un objectif precis. Tu dois ecrire les sujets et le contenu toi-meme.

**[ECRAN -- slide "Etape 1 : Definis le contexte"]**

Avant d'ouvrir FluentCRM, reponds a ces trois questions :

1. Qui entre dans cette sequence ? Un nouvel inscrit a ta newsletter, un membre gratuit, un participant a un webinaire ?

2. Quel est l'objectif final ? Vendre ta formation premium, obtenir un rendez-vous, generer un premier achat ?

3. Quelle est la principale objection de ton audience ? "C'est trop cher", "Je n'ai pas le temps", "Je ne sais pas si ca marche" ?

Note tes reponses. Elles vont guider chaque email.

**[ECRAN -- slide "Etape 2 : Ecris tes 5 sujets"]**

Maintenant, ecris les sujets de tes 5 emails en suivant cette structure :

Email 1 (J0) -- Bienvenue : accueille et donne acces au contenu promis. Sujet direct, pas de mystere.

Email 2 (J1) -- Valeur : partage un conseil actionnable. Le sujet doit promettre un benefice concret.

Email 3 (J3) -- Preuve sociale : temoignage ou etude de cas. Le sujet doit mentionner un resultat chiffre.

Email 4 (J5) -- Contenu avance : un apercu de ton offre premium. Le sujet doit susciter la curiosite.

Email 5 (J7) -- Offre : appel a l'action. Le sujet doit etre clair et direct.

Ecris tes 5 sujets avant de passer a la suite.

**[ECRAN -- slide "Etape 3 : Redige tes emails"]**

Pour chaque email, respecte ces regles :

Longueur : 150-250 mots maximum. Un email de sequence n'est pas un article de blog.

Structure : une phrase d'accroche, un contenu principal, un appel a l'action. Trois blocs, pas plus.

Personnalisation : utilise au minimum {{contact.first_name}} dans le premier email.

Un seul appel a l'action par email. Pas deux liens, pas trois boutons. Un seul.

**[ECRAN -- slide "Etape 4 : Configure dans FluentCRM"]**

Ouvre FluentCRM. Cree ta sequence.

Checklist de configuration :

- [ ] Nom de la sequence (interne, descriptif)
- [ ] 5 emails ajoutes dans l'ordre
- [ ] Delais : 0, 1, 2, 2, 2 jours
- [ ] Jours d'envoi : lundi a vendredi
- [ ] Fenetre horaire : 8h-10h
- [ ] Fuseau horaire correct

**[ECRAN -- slide "Etape 5 : Teste"]**

Avant de publier :

1. Inscris-toi dans la sequence avec ton adresse email de test
2. Verifie que le premier email arrive dans ta boite
3. Relis chaque email sur mobile (pas seulement sur desktop)
4. Verifie que les liens fonctionnent
5. Verifie que les smart codes s'affichent correctement

**[ECRAN -- slide "Grille d'auto-evaluation"]**

Note chaque email sur ces criteres :

| Critere | Oui/Non |
| --- | --- |
| Le sujet donne envie d'ouvrir | |
| Le contenu tient en 250 mots | |
| Il y a un seul appel a l'action | |
| Le ton est personnel et direct | |
| L'email apporte de la valeur (pas juste de la vente) | |

Si tu as 4/5 ou plus sur chaque email, ta sequence est prete.

**[FACE CAMERA]**

Prends le temps de bien faire cet exercice. Une bonne sequence d'onboarding travaille pour toi pendant des mois. Chaque nouvel inscrit recoit le meme parcours optimise. C'est du temps investi une seule fois pour un retour continu.

---

**Points cles** :
- Definir le contexte avant d'ecrire : audience, objectif, objection principale
- 5 emails : Bienvenue > Valeur > Preuve > Apercu > Offre
- 150-250 mots par email, un seul appel a l'action
- Toujours tester sur mobile avant de publier
- Grille d'auto-evaluation : 5 criteres par email

**Mots cles SEO** : exercice sequence email, creer onboarding email, template sequence FluentCRM, emails automatiques formation

---

## Quiz M5 -- Email sequences et nurturing

**Type** : Quiz TutorLMS (8 questions)
**Seuil de reussite** : 80%

**Question 1** : Quelle est la difference principale entre une campagne et une sequence dans FluentCRM ?
- A) La campagne est gratuite, la sequence est payante
- B) La campagne est un envoi ponctuel, la sequence est une serie automatique dans un ordre fixe *(bonne reponse)*
- C) La sequence ne peut contenir que 3 emails
- D) La campagne utilise des templates, la sequence non

**Question 2** : Quel delai recommande-t-on pour le premier email d'une sequence d'onboarding ?
- A) 24 heures
- B) 1 jour
- C) 0 -- envoi immediat *(bonne reponse)*
- D) 2 heures

**Question 3** : Dans la structure de sequence d'onboarding schoolsWP, quel est l'objectif de l'email 3 (J+3) ?
- A) Presenter l'offre payante
- B) Partager un temoignage ou une preuve sociale *(bonne reponse)*
- C) Envoyer un code promo
- D) Demander un feedback

**Question 4** : Pourquoi est-il recommande d'utiliser "1 jour" plutot que "24 heures" comme delai entre deux emails ?
- A) Ca coute moins cher en ressources serveur
- B) "1 jour" respecte la fenetre horaire configuree, "24 heures" envoie exactement 24h apres *(bonne reponse)*
- C) FluentCRM ne supporte pas les heures
- D) Ca evite les doublons

**Question 5** : Combien d'emails maximum doit contenir une sequence de re-engagement ?
- A) 1
- B) 3 *(bonne reponse)*
- C) 5
- D) 7

**Question 6** : Apres combien de jours d'inactivite doit-on declencher une sequence de re-engagement pour un etudiant de formation ?
- A) 3 jours
- B) 7 jours
- C) 14 jours *(bonne reponse)*
- D) 30 jours

**Question 7** : Quel est le minimum d'envois par version necessaire pour un A/B test fiable sur un sujet d'email ?
- A) 10
- B) 25
- C) 50 *(bonne reponse)*
- D) 100

**Question 8** : Quelle est la fenetre horaire d'envoi recommandee pour une sequence professionnelle ?
- A) 6h-7h
- B) 8h-10h *(bonne reponse)*
- C) 12h-14h
- D) 18h-20h
