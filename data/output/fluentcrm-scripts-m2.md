# Scripts video — Module 2 : Premiers contacts et segmentation

**Formation** : Maitriser FluentCRM
**Module** : M2 — Premiers contacts et segmentation (Gratuit)
**Lecons** : 8 videos + 1 quiz
**Duree totale** : ~45 min de video
**Date** : 2026-03-21

---

### Lecon 2.1 — Decouvre le dashboard Contacts

**Duree** : 5 min
**Type** : Video HeyGen
**Ecran** : Dashboard FluentCRM > Contacts > All Contacts

---

**[INTRO — face camera]**

Tu viens d'installer FluentCRM. Avant d'ajouter le moindre contact, prends deux minutes pour comprendre ton tableau de bord Contacts. C'est ta base de commande.

**[ECRAN — screencast FluentCRM > Contacts]**

Voici le dashboard Contacts. C'est la premiere chose que tu vois quand tu cliques sur Contacts dans le menu FluentCRM.

En haut a gauche, tu as trois filtres rapides.

[Clic sur le filtre Lists]

Le premier, c'est le filtre par listes. Une liste, c'est un grand groupe de contacts. Par exemple : "Prospects blog" ou "Clients formation".

[Clic sur le filtre Tags]

Le deuxieme, c'est le filtre par tags. Les tags sont plus precis. On en reparlera en detail dans la lecon 2.5.

[Clic sur le filtre Status]

Le troisieme, c'est le filtre par statut. Subscribed, Pending, Unsubscribed... Six statuts au total. On les detaille dans la lecon 2.6.

**[ECRAN — zone haute droite du dashboard]**

En haut a droite, tu retrouves quatre boutons essentiels.

[Pointer le bouton + Add Contact]

"Add Contact" pour ajouter un contact manuellement. C'est la prochaine lecon.

[Pointer le bouton Import]

"Import" pour charger un fichier CSV ou migrer depuis un autre outil.

[Pointer le bouton Export]

"Export" pour telecharger ta liste au format CSV.

[Pointer le bouton Advanced Filter]

Et "Advanced Filter" pour des recherches avancees. Tres puissant.

**[ECRAN — barre de recherche + colonnes]**

Tu as aussi une barre de recherche. Tape un nom ou un email, le resultat s'affiche instantanement.

[Clic sur l'icone Columns]

Et le selecteur de colonnes. Par defaut, tu vois le nom, l'email, les listes, les tags et le statut. Tu peux ajouter le telephone, le pays, la date de creation, la derniere activite.

Si tu utilises WooCommerce, des colonnes supplementaires apparaissent : valeur totale, nombre d'achats, dernier achat.

**[ECRAN — pagination en bas]**

En bas, la pagination. Tu peux afficher 10, 20, 50, 100 ou meme 600 contacts par page.

**[FACE CAMERA]**

Petit conseil : quand tu debutes, garde les colonnes par defaut. Ajoute le pays et la source. Ca te donne une vue claire sans surcharger l'ecran.

Les trois filtres du haut fonctionnent en mode AND. Si tu selectionnes la liste "Prospects" ET le tag "Webinaire", tu ne verras que les contacts qui sont dans les deux.

**[TRANSITION]**

Maintenant que tu connais ton tableau de bord, on va ajouter ton premier contact a la main.

---

**Points cles** :
- Le dashboard Contacts est la vue centrale de FluentCRM
- Trois filtres rapides : listes, tags, statuts (fonctionnent en AND)
- Quatre actions : ajouter, importer, exporter, filtre avance
- Les colonnes sont personnalisables selon tes besoins

**Mots cles SEO** : FluentCRM contacts, dashboard FluentCRM, tableau de bord contacts, gestion contacts WordPress

---

### Lecon 2.2 — Ajoute ton premier contact manuellement

**Duree** : 4 min
**Type** : Video HeyGen
**Ecran** : FluentCRM > Contacts > Add Contact

---

**[INTRO — face camera]**

Tu as un prospect au telephone. Tu veux l'ajouter tout de suite dans ton CRM. Voyons comment faire en moins d'une minute.

**[ECRAN — screencast FluentCRM > Contacts]**

Depuis le dashboard Contacts, clique sur le bouton "+ Add Contact" en haut a droite.

[Clic sur + Add Contact — le panneau lateral s'ouvre]

Un panneau s'ouvre sur la droite. Il contient quatre sections.

**[ECRAN — section Basic Info]**

Premiere section : les informations de base. Prefixe, prenom, nom, email, telephone, date de naissance et entreprise.

L'email est le seul champ obligatoire. Tout le reste est optionnel.

[Remplir les champs prenom, nom, email]

Je remplis : prenom, nom, email. C'est le minimum pour un contact utile.

**[ECRAN — section Address Info]**

Deuxieme section : l'adresse. Ligne 1, ligne 2, ville, departement, code postal, pays.

Si tu vends des formations en ligne, le pays peut suffire. Pour du service local, remplis l'adresse complete.

**[ECRAN — section Custom Data]**

Troisieme section : les donnees personnalisees. Ce sont les champs que tu as crees toi-meme dans FluentCRM.

Par exemple, si tu as ajoute un champ "Niveau WordPress", il apparait ici.

**[ECRAN — section Identifiers]**

Quatrieme section : les identifiants. C'est la plus importante pour l'organisation.

[Selectionner une liste]

Tu choisis une liste. Par exemple : "Prospects blog".

[Selectionner un tag]

Tu ajoutes un ou plusieurs tags. Par exemple : "Source : telephone".

[Selectionner un statut]

Et tu definis le statut. Subscribed si tu as le consentement. Pending si tu veux envoyer un email de confirmation.

**[ECRAN — boutons de validation]**

Deux boutons en bas. "Create Contact" pour creer et fermer. "Create & Add Another" pour enchainer.

[Clic sur Create Contact]

Et voila. Ton contact est cree. Il apparait dans la liste.

**[FACE CAMERA]**

Une bonne pratique : assigne toujours au moins une liste et un tag a chaque contact. Un contact sans liste ni tag, c'est un contact perdu dans la masse.

Et si tu n'as pas encore le consentement explicite pour tes emails marketing, mets le statut sur Pending. FluentCRM enverra automatiquement un email de confirmation si le double opt-in est active.

**[TRANSITION]**

Ajouter un contact a la main, c'est bien pour un ou deux. Mais si tu as une base existante, il te faut l'import CSV. C'est le sujet de la prochaine lecon.

---

**Points cles** :
- L'email est le seul champ obligatoire
- Toujours assigner une liste et un tag
- Choisir le bon statut : Subscribed (consentement) ou Pending (a confirmer)
- "Create & Add Another" pour enchainer les ajouts

**Mots cles SEO** : ajouter contact FluentCRM, creer contact manuellement, FluentCRM contact

---

### Lecon 2.3 — Importe tes contacts depuis un CSV

**Duree** : 6 min
**Type** : Video HeyGen
**Ecran** : FluentCRM > Contacts > Import > CSV

---

**[INTRO — face camera]**

Tu as une liste de contacts dans un tableur. Peut-etre un export MailChimp, un fichier Excel, ou une liste de clients. Voyons comment tout importer dans FluentCRM proprement.

**[ECRAN — screencast FluentCRM > Contacts]**

Depuis le dashboard Contacts, clique sur "Import" en haut a droite.

[Clic sur Import — la fenetre modale s'ouvre]

Une fenetre s'ouvre. Plusieurs sources sont proposees. Choisis "CSV File".

[Clic sur CSV File puis Next]

**[ECRAN — etape 1 : upload]**

Avant d'uploader, verifions ton fichier.

[Afficher un exemple de CSV dans un tableur]

Ton fichier CSV doit avoir des en-tetes en premiere ligne. Au minimum : email. Idealement : first_name, last_name, email.

FluentCRM propose un fichier exemple. Clique sur "Download Sample File" pour voir le format attendu.

Le delimiteur par defaut est la virgule. Si ton fichier utilise le point-virgule, comme beaucoup de fichiers Excel en francais, change le delimiteur ici.

[Selectionner "Semicolon separated" si besoin]

Maintenant, glisse ton fichier ou clique pour le selectionner.

[Upload du fichier CSV]

**[ECRAN — etape 2 : mapping des champs]**

C'est l'etape cle. FluentCRM te montre tes colonnes a gauche et les champs CRM a droite.

[Pointer les colonnes]

A gauche, les en-tetes de ton CSV. A droite, les champs FluentCRM correspondants.

Verifie que chaque colonne est bien associee. Prenom avec First Name. Nom avec Last Name. Email avec Email.

Si ton CSV a des colonnes supplementaires, comme "Entreprise" ou "Telephone", associe-les aussi.

[Mapper les champs un par un]

**[ECRAN — etape 3 : liste, tags, statut]**

Sous le mapping, tu definis trois choses.

[Selectionner une liste]

La liste d'affectation. Tous tes contacts importes iront dans cette liste.

[Selectionner un tag]

Les tags a appliquer. Par exemple : "Import mars 2026".

[Selectionner le statut]

Le statut des nouveaux contacts. Deux cas :

Si tu as le consentement de ces contacts pour recevoir tes emails, choisis "Subscribed".

Si tu n'es pas sur, choisis "Pending". FluentCRM leur enverra un email de double opt-in.

**[ECRAN — option "Update existing"]**

L'option "Update existing subscribers". Si un contact existe deja avec le meme email, est-ce que tu veux mettre a jour ses donnees ?

Choisis "Yes" si ton CSV contient des infos plus recentes. "No" pour ne pas ecraser les donnees existantes.

**[ECRAN — clic sur Confirm Import]**

Tout est pret. Clique sur "Confirm Import".

[Barre de progression puis message de succes]

FluentCRM importe tes contacts. Ca prend quelques secondes pour 100 contacts. Quelques minutes pour des milliers.

**[FACE CAMERA]**

Trois conseils pour un import propre.

Un : nettoie ton fichier avant. Supprime les doublons, les emails invalides, les lignes vides.

Deux : ajoute toujours un tag d'import avec la date. Ca te permet de retrouver facilement ce lot. Par exemple : "import-csv-2026-03".

Trois : fais un test avec 5 contacts d'abord. Verifie que le mapping est correct. Puis importe le reste.

**[TRANSITION]**

Et si tu viens de MailChimp, ConvertKit ou ActiveCampaign ? FluentCRM sait migrer directement via API. C'est la prochaine lecon.

---

**Points cles** :
- Le CSV doit avoir des en-tetes, avec au minimum la colonne email
- Attention au delimiteur : virgule ou point-virgule selon ta source
- Toujours verifier le mapping des champs avant d'importer
- Ajouter un tag d'import avec la date pour tracer le lot
- Tester avec 5 contacts avant un import massif

**Mots cles SEO** : import CSV FluentCRM, importer contacts FluentCRM, migration email WordPress

---

### Lecon 2.4 — Importe depuis MailChimp, ConvertKit ou ActiveCampaign

**Duree** : 6 min
**Type** : Video HeyGen
**Ecran** : FluentCRM > Contacts > Import > Other Platforms

---

**[INTRO — face camera]**

Tu quittes MailChimp, ConvertKit ou ActiveCampaign pour FluentCRM. Bonne decision. La migration se fait en quelques minutes, directement via l'API.

**[ECRAN — screencast FluentCRM > Contacts > Import]**

Depuis le dashboard Contacts, clique sur Import. Cette fois, choisis "Import from Other Platforms".

[Clic sur Import from Other Platforms]

Tu vois la liste des plateformes supportees. MailChimp, ConvertKit, Mailer Lite, Drip, ActiveCampaign.

**[SLIDE — Les 3 etapes de migration]**

La procedure est la meme pour toutes les plateformes. Trois etapes.

Etape 1 : connecter l'API. Etape 2 : mapper les donnees. Etape 3 : lancer l'import.

Voyons ca avec MailChimp. Puis je te montre les differences pour ConvertKit et ActiveCampaign.

**[ECRAN — migration MailChimp]**

[Selectionner MailChimp puis Next]

FluentCRM te demande ta cle API MailChimp.

Pour la trouver : dans ton compte MailChimp, va dans Account, Extras, API Keys.

[Afficher un screenshot de MailChimp > API Keys]

Copie ta cle. Colle-la ici. Clique sur "Continue".

[Coller la cle et cliquer Continue]

FluentCRM se connecte a ton compte MailChimp. Il recupere tes listes et tes audiences.

Tu vois un apercu de tes donnees. Les champs MailChimp sont mappes vers les champs FluentCRM.

[Pointer le mapping]

Verifie que tout correspond. Prenom, nom, email, tags.

Choisis la liste et les tags FluentCRM pour les contacts importes.

Definis le statut. Si tes contacts MailChimp etaient deja inscrits, tu peux les passer en "Subscribed".

Et lance l'import.

[Clic sur Import]

**[FACE CAMERA]**

Pour ConvertKit, c'est le meme principe. Tu trouves ta cle API dans Account Settings, puis API Key.

Pour ActiveCampaign, tu as besoin de deux choses : l'URL de ton compte et la cle API. Tu les trouves dans Settings, Developer.

**[ECRAN — screencast rapide ConvertKit]**

[Selectionner ConvertKit, coller la cle, montrer le mapping]

Le mapping est identique. Champs source a gauche, champs FluentCRM a droite.

**[ECRAN — screencast rapide ActiveCampaign]**

[Selectionner ActiveCampaign, coller URL + cle]

Pour ActiveCampaign, colle l'URL de ton compte et ta cle API. Le reste est pareil.

**[FACE CAMERA]**

Quelques points importants pour une migration reussie.

Un : exporte d'abord une sauvegarde de ton ancienne plateforme en CSV. Meme si l'import API fonctionne bien, tu auras un filet de securite.

Deux : verifie les tags. MailChimp utilise des "groups" et des "tags". ConvertKit utilise des "tags" et des "sequences". ActiveCampaign utilise des "tags", des "listes" et des "deals". Pas tout ne sera importe automatiquement.

Trois : apres l'import, fais un tour dans tes contacts. Verifie que les listes et tags sont corrects. Compare le nombre de contacts importes avec ta source.

Quatre : ne supprime pas ton ancien compte tout de suite. Garde-le actif pendant 30 jours, le temps de verifier que tout fonctionne.

**[ECRAN — import depuis WooCommerce et TutorLMS]**

FluentCRM peut aussi importer depuis des plugins WordPress installes sur ton site. WooCommerce, TutorLMS, LearnDash, LifterLMS, MemberPress, et d'autres.

Pour ca, le plugin doit etre installe et actif. Tu verras alors l'option dans la fenetre d'import.

Par exemple, pour WooCommerce, tu peux importer par produit achete. Pour TutorLMS, par cours suivi.

On ne detaille pas ca aujourd'hui, mais sache que c'est disponible.

**[TRANSITION]**

Tes contacts sont importes. Maintenant, il faut les organiser. Dans la prochaine lecon, on met en place ta strategie de listes et de tags.

---

**Points cles** :
- Migration directe via API pour MailChimp, ConvertKit, ActiveCampaign, Drip, Mailer Lite
- Toujours exporter un CSV de sauvegarde avant la migration
- Verifier le mapping des champs et des tags apres import
- Garder l'ancien compte actif 30 jours apres migration
- Import aussi possible depuis WooCommerce, TutorLMS, LearnDash, etc.

**Mots cles SEO** : migration MailChimp FluentCRM, import ConvertKit FluentCRM, quitter ActiveCampaign WordPress

---

### Lecon 2.5 — Organise avec les listes et les tags — ta strategie de nommage

**Duree** : 6 min
**Type** : Video HeyGen
**Ecran** : FluentCRM > Contacts > Lists / Tags

---

**[INTRO — face camera]**

Listes et tags, c'est le coeur de ton organisation dans FluentCRM. Mal utilises, tu te retrouves avec un bazar inutilisable. Bien utilises, tu peux cibler n'importe quel segment en deux clics.

**[SLIDE — Liste vs Tag : la difference]**

Premiere regle a comprendre.

Une liste, c'est un grand groupe stable. Un contact appartient a une ou deux listes. Rarement plus.

Un tag, c'est une etiquette precise et dynamique. Un contact peut avoir 5, 10, 20 tags. Les tags evoluent dans le temps.

Pense a ca : la liste, c'est le classeur. Le tag, c'est le post-it.

**[ECRAN — FluentCRM > Contacts > Lists]**

Voyons les listes. Clique sur "Lists" dans le menu Contacts.

[Afficher la page Lists]

Pour creer une liste, clique sur "Create List". Donne-lui un nom et une description interne optionnelle.

[Creer une liste "Prospects Blog"]

**[SLIDE — Convention de nommage des listes]**

Voici la convention que je te recommande si tu crees des formations en ligne.

Trois a cinq listes maximum. Pas plus.

Liste 1 : "Prospects Blog". Tous les visiteurs qui s'inscrivent via ton site.

Liste 2 : "Eleves Formation". Ceux qui ont achete une formation.

Liste 3 : "Clients Services". Ceux qui ont achete un service ou un accompagnement.

Liste 4 : "Partenaires". Affilies, collaborateurs, prescripteurs.

Si tu vends sur WooCommerce, ajoute une liste "Acheteurs Boutique".

C'est tout. Si tu as besoin de plus de precision, utilise les tags.

**[ECRAN — FluentCRM > Contacts > Tags]**

Passons aux tags. Clique sur "Tags" dans le menu Contacts.

[Afficher la page Tags]

Meme principe pour en creer un. Clique sur "Create Tag", donne un nom.

[Creer quelques tags]

**[SLIDE — Convention de nommage des tags]**

Pour les tags, je te propose un systeme a prefixes. C'est ce qui fait la difference entre un CRM propre et un CRM chaotique.

Categorie 1 : la source. D'ou vient le contact ?

Exemples : "src:blog", "src:webinaire", "src:linkedin", "src:import-csv-2026-03".

Categorie 2 : l'action. Qu'a fait le contact ?

Exemples : "act:telecharge-guide", "act:vu-webinaire", "act:achat-formation-lms".

Categorie 3 : l'interet ou le pilier thematique.

Exemples : "int:lms", "int:crm", "int:seo", "int:automatisation".

Categorie 4 : le niveau.

Exemples : "niv:debutant", "niv:intermediaire", "niv:avance".

Categorie 5 : le statut commercial.

Exemples : "com:prospect-chaud", "com:client-actif", "com:churne".

**[FACE CAMERA]**

Pourquoi des prefixes ? Parce que dans FluentCRM, quand tu tapes "src:" dans un champ de tag, tu vois immediatement toutes les sources. Pareil pour "act:", "int:", "niv:", "com:".

Ca evite les tags en vrac du type "webinaire", "formation", "chaud", "2024"... qui ne veulent plus rien dire au bout de trois mois.

**[ECRAN — exemple concret]**

Prenons un exemple. Marie s'inscrit via ton blog pour telecharger un guide sur les LMS WordPress.

[Montrer la fiche contact avec les tags]

Marie est dans la liste "Prospects Blog". Elle a les tags : "src:blog", "act:telecharge-guide", "int:lms".

Deux mois plus tard, elle achete ta formation. Tu la passes dans la liste "Eleves Formation". Tu ajoutes le tag "act:achat-formation-lms".

Tu gardes l'historique complet de son parcours.

**[SLIDE — Les erreurs a eviter]**

Trois erreurs classiques.

Erreur 1 : creer une liste par produit. Non. Utilise un tag "act:achat-nom-du-produit". Les listes restent larges.

Erreur 2 : des tags sans convention. "chaud", "Webinaire 2024", "a relancer"... Illisible au bout de 50 tags.

Erreur 3 : ne pas documenter. Note ta convention quelque part. Un simple Google Doc suffit. Ton futur toi te remerciera.

**[TRANSITION]**

Tes listes et tags sont en place. Mais il y a un concept que beaucoup ignorent : les six statuts de contact. C'est la prochaine lecon, et c'est essentiel.

---

**Points cles** :
- Listes = grands groupes stables (3 a 5 max)
- Tags = etiquettes precises et dynamiques (prefixes : src:, act:, int:, niv:, com:)
- Toujours utiliser une convention de nommage avec prefixes
- Documenter sa convention de tags dans un document partage
- Ne pas creer une liste par produit — utiliser un tag a la place

**Mots cles SEO** : listes tags FluentCRM, organiser contacts CRM, convention nommage tags, segmentation email WordPress

---

### Lecon 2.6 — Comprends les 6 statuts de contact (dont Transactional)

**Duree** : 5 min
**Type** : Video HeyGen
**Ecran** : FluentCRM > Contacts (filtrage par statut)

---

**[INTRO — face camera]**

Dans FluentCRM, chaque contact a un statut. Ce statut determine ce que tu peux lui envoyer. Six statuts au total. Et le dernier, Transactional, est mal compris par la majorite des utilisateurs.

**[SLIDE — Les 6 statuts]**

Les voici :

1. Subscribed
2. Pending
3. Unsubscribed
4. Bounced
5. Complained
6. Transactional

Detaillons chacun.

**[SLIDE — Statut 1 : Subscribed]**

Subscribed. Ce sont tes contacts actifs. Ils ont donne leur consentement. Tu peux leur envoyer des emails marketing, des campagnes, des sequences. Les automations fonctionnent pour eux.

C'est ton audience principale. Celle que tu veux faire grandir.

**[SLIDE — Statut 2 : Pending]**

Pending. Le contact attend de confirmer son inscription. En general, il a rempli un formulaire mais n'a pas encore clique sur le lien de confirmation du double opt-in.

Tu ne peux pas lui envoyer de campagne. Les automations tournent pour lui, mais les emails de l'automation ne partent pas.

L'objectif : le faire passer en Subscribed. On verra le double opt-in en detail dans la lecon 2.8.

**[SLIDE — Statut 3 : Unsubscribed]**

Unsubscribed. Le contact s'est desinscrit. Soit en cliquant le lien de desinscription dans un email, soit manuellement par un admin.

Regle absolue : ne lui envoie plus rien. C'est une obligation legale et une question de reputation.

**[SLIDE — Statut 4 : Bounced]**

Bounced. L'email n'a pas ete delivre. L'adresse est invalide ou le serveur a rejete le message.

FluentCRM marque automatiquement ces contacts si tu as configure un gestionnaire de rebonds avec ton service d'envoi.

Aucun email ne sera envoye a un contact Bounced. Nettoie regulierement ces contacts.

**[SLIDE — Statut 5 : Complained]**

Complained. Le contact a marque ton email comme spam.

C'est un signal fort. Arrete toute communication avec ces contacts. Trop de plaintes, et ta delivrabilite plonge pour tout le monde.

**[SLIDE — Statut 6 : Transactional]**

Et maintenant, Transactional. C'est le statut que peu de gens comprennent.

Un contact Transactional ne recevra pas tes campagnes marketing. Pas de newsletters, pas de promotions.

Mais — et c'est la difference cle — il recevra les emails envoyes via les automations.

**[FACE CAMERA]**

Concretement, a quoi ca sert ?

Exemple 1 : un client WooCommerce qui achete mais ne veut pas de marketing. Tu le mets en Transactional. Il recoit ses confirmations de commande via automation, mais pas tes newsletters.

D'ailleurs, c'est le statut par defaut du module Panier Abandonne de FluentCRM.

Exemple 2 : un utilisateur de ta plateforme de formation. Il a besoin de recevoir des rappels automatiques sur ses cours. Mais il ne veut pas tes offres commerciales. Transactional.

Exemple 3 : un partenaire. Tu veux l'inclure dans une automation de suivi, mais pas dans tes campagnes de masse.

**[SLIDE — Tableau recapitulatif]**

Voici le resume :

| Statut | Campagnes | Automations (emails) | Automations (actions) |
|--------|-----------|---------------------|-----------------------|
| Subscribed | Oui | Oui | Oui |
| Pending | Non | Non | Oui (si active) |
| Unsubscribed | Non | Non | Oui (si active) |
| Bounced | Non | Non | Non |
| Complained | Non | Non | Non |
| Transactional | Non | Oui | Oui |

Retiens ce tableau. C'est la logique de FluentCRM.

**[FACE CAMERA]**

Mon conseil : verifie le statut de tes contacts regulierement. Filtre par "Bounced" et nettoie. Filtre par "Complained" et supprime. Filtre par "Pending" et relance les confirmations si besoin.

Un CRM propre, c'est un CRM ou chaque contact a le bon statut.

**[TRANSITION]**

Tu connais les statuts. Maintenant, passons aux segments dynamiques. C'est une fonctionnalite Pro qui change la donne.

---

**Points cles** :
- 6 statuts : Subscribed, Pending, Unsubscribed, Bounced, Complained, Transactional
- Seuls les Subscribed recoivent les campagnes marketing
- Transactional recoit les emails d'automation mais pas les campagnes
- Transactional est le statut par defaut du module Panier Abandonne
- Nettoyer regulierement les Bounced et Complained

**Mots cles SEO** : statuts contact FluentCRM, transactional FluentCRM, gestion statuts email, contact bounced WordPress

---

### Lecon 2.7 — Cree des segments dynamiques (Pro)

**Duree** : 6 min
**Type** : Video HeyGen
**Ecran** : FluentCRM > Contacts > Segments

---

**[INTRO — face camera]**

Les listes et les tags, c'est bien. Mais ils sont statiques. Tu les assignes manuellement ou via automation. Les segments dynamiques, eux, se mettent a jour tout seuls en temps reel. C'est une fonctionnalite Pro.

**[ECRAN — FluentCRM > Contacts > Segments]**

Pour acceder aux segments, survole "Contacts" dans le menu FluentCRM et clique sur "Segments".

[Clic sur Segments]

Tu arrives sur la liste de tes segments. Pour en creer un, clique sur "Create Custom Segment".

[Clic sur Create Custom Segment]

**[ECRAN — creation d'un segment]**

Premiere chose : donne un nom a ton segment.

[Taper "Clients Premium WooCommerce"]

Maintenant, on definit les conditions.

[Clic sur le selecteur de filtre]

Tu as acces a des dizaines de criteres. Segments de contact, activites email, donnees WooCommerce, cours LMS, champs personnalises.

**[ECRAN — exemple 1 : clients WooCommerce premium]**

Creons un segment de clients premium. Les conditions :

[Ajouter filtre "WooCommerce Total Value" > Greater than > 500]

Premiere condition : la valeur totale WooCommerce est superieure a 500 euros.

[Cliquer + pour ajouter une condition]

Deuxieme condition : le nombre de commandes est superieur a 2.

[Ajouter filtre "WooCommerce Total Order" > Greater than > 2]

FluentCRM combine ces conditions en AND. Le segment n'affiche que les contacts qui remplissent toutes les conditions.

[Clic sur Save — le segment se cree avec le nombre de contacts]

Le segment est cree. Le nombre de contacts correspondants s'affiche automatiquement.

Et demain, si un nouveau client depasse 500 euros et 2 commandes, il entre dans le segment sans que tu fasses quoi que ce soit.

**[ECRAN — exemple 2 : contacts inactifs]**

Deuxieme exemple. On veut identifier les contacts qui n'ont pas ouvert d'email depuis 90 jours.

[Creer un nouveau segment "Inactifs 90 jours"]

[Ajouter filtre "Last Email Open" > Before > (date il y a 90 jours)]

Un segment utile pour lancer une campagne de reengagement.

**[ECRAN — exemple 3 : prospects formation LMS]**

Troisieme exemple. Adapte a un createur de formation.

[Creer un segment "Prospects Formation LMS"]

Conditions : le contact a le tag "int:lms". ET le contact n'a PAS le tag "act:achat-formation-lms".

[Ajouter les filtres avec tag includes / tag not includes]

Ce segment te donne tous les contacts interesses par le LMS qui n'ont pas encore achete. Ideal pour une campagne ciblee.

**[FACE CAMERA]**

Tu peux creer autant de segments que tu veux. Voici ceux que je te recommande pour demarrer :

Segment 1 : "Clients actifs" — au moins un achat dans les 6 derniers mois.

Segment 2 : "Inactifs 90 jours" — aucune ouverture depuis 90 jours.

Segment 3 : "Prospects chauds" — inscrits depuis moins de 7 jours, au moins un email ouvert.

Segment 4 : "Interesses par [ton produit]" — tag d'interet mais pas de tag d'achat.

**[ECRAN — utilisation dans une campagne]**

Et ensuite, tu utilises ces segments directement dans tes campagnes email. Quand tu crees une campagne, a l'etape des destinataires, tu peux choisir "Dynamic Segments" au lieu de "Lists & Tags".

[Montrer l'onglet Dynamic Segments dans l'editeur de campagne]

C'est ca la puissance. Un segment qui se met a jour en temps reel, directement utilisable dans tes envois.

**[TRANSITION]**

On a couvert listes, tags, statuts et segments dynamiques. Il reste un sujet crucial : le double opt-in. Quand l'activer, quand le desactiver, et l'impact sur tes conversions.

---

**Points cles** :
- Les segments dynamiques se mettent a jour automatiquement en temps reel
- Fonctionnalite disponible dans FluentCRM Pro uniquement
- Combiner plusieurs conditions avec AND pour un ciblage precis
- 4 segments recommandes : clients actifs, inactifs, prospects chauds, interesses
- Les segments sont utilisables directement dans les campagnes email

**Mots cles SEO** : segments dynamiques FluentCRM, segmentation avancee, FluentCRM Pro segments, ciblage email WordPress

---

### Lecon 2.8 — Double opt-in : quand l'activer et impact sur tes conversions

**Duree** : 7 min
**Type** : Video HeyGen
**Ecran** : FluentCRM > Settings > Double Opt-in

---

**[INTRO — face camera]**

Le double opt-in, c'est l'email de confirmation que recoit un contact apres son inscription. "Confirme ton abonnement." Simple en apparence. Mais ca a un impact direct sur ta delivrabilite et tes conversions.

**[SLIDE — Comment ca marche]**

Le mecanisme en trois etapes.

Etape 1 : le visiteur remplit un formulaire sur ton site.

Etape 2 : FluentCRM lui envoie un email avec un bouton "Confirme ton inscription".

Etape 3 : le visiteur clique. Son statut passe de Pending a Subscribed.

S'il ne clique pas, il reste en Pending. Il ne recoit aucune campagne.

**[FACE CAMERA]**

La question que tout le monde se pose : est-ce que je dois l'activer ?

Ca depend de ta situation. Voici mon arbre de decision.

**[SLIDE — Arbre de decision double opt-in]**

**Cas 1 — Blog francais, audience RGPD : ACTIVE le double opt-in.**

Si tu as un blog en francais et que ton audience est en France ou en Europe, le RGPD impose un consentement explicite. Le double opt-in est la methode la plus sure pour le prouver.

Active-le. Pas de discussion.

**Cas 2 — Import d'une liste existante : CA DEPEND.**

Si tes contacts ont deja donne leur consentement sur une autre plateforme, tu peux les importer en Subscribed sans double opt-in.

Si tu n'es pas sur du consentement, importe-les en Pending. FluentCRM leur enverra un email de confirmation.

**Cas 3 — Acheteurs WooCommerce : DESACTIVE le double opt-in.**

Un client qui achete un produit t'a donne son consentement transactionnel. Pas besoin de lui demander de confirmer une deuxieme fois. Ca cree de la friction inutile.

Dans les parametres WooCommerce de FluentCRM, mets le statut par defaut a Subscribed.

**Cas 4 — Formulaire lead magnet (guide gratuit, checklist) : ACTIVE.**

L'utilisateur n'a pas encore de relation commerciale avec toi. Le double opt-in filtre les faux emails et confirme l'interet.

**Cas 5 — Webinaire ou evenement : ACTIVE.**

Meme logique. Le double opt-in garantit que l'email est valide avant d'envoyer le lien de connexion.

**[SLIDE — Resume arbre de decision]**

| Situation | Double opt-in |
|-----------|---------------|
| Blog francais / audience RGPD | Oui |
| Import liste consentie | Non (importer en Subscribed) |
| Import liste douteuse | Oui (importer en Pending) |
| Acheteurs WooCommerce | Non |
| Lead magnet / guide gratuit | Oui |
| Webinaire / evenement | Oui |
| Panier abandonne | Non (statut Transactional) |

**[ECRAN — FluentCRM > Settings > Double Opt-in Settings]**

Voyons comment le configurer.

Dans FluentCRM, va dans Settings, puis "Double Opt-in Settings" dans la barre laterale.

[Naviguer vers Settings > Double Opt-in]

**[ECRAN — Email Subject & Body]**

Premiere section : l'objet et le corps de l'email.

[Pointer le champ Subject]

L'objet par defaut fonctionne. Mais tu peux le personnaliser. Quelque chose comme : "Confirme ton inscription a schoolsWP".

[Pointer le corps de l'email]

Le corps de l'email contient un bouton de confirmation. C'est le smart code "activate_button" qui genere le lien.

Ne supprime jamais ce smart code. Sans lui, le contact ne peut pas confirmer.

Tu peux personnaliser le texte autour. Reste bref. Une phrase d'accueil, le bouton, c'est tout.

**[ECRAN — Design Template]**

Tu choisis le design. Quatre options : Simple Boxed, Plain Centered, Plain Left, Classic Editor.

[Selectionner Plain Centered]

Plain Centered est le plus lisible sur mobile. C'est celui que je recommande.

**[ECRAN — After Confirmation Actions]**

Apres la confirmation, deux options.

[Pointer "Show Message"]

Option 1 : afficher un message. Le contact voit une page de confirmation. Tu peux personnaliser le texte.

[Pointer "Redirect to URL"]

Option 2 : rediriger vers une URL. Plus interessant. Tu peux envoyer le contact vers une page de remerciement avec une offre, un bonus, ou un lien vers ta formation gratuite.

**[FACE CAMERA]**

L'impact sur les conversions. Soyons honnetes.

Le double opt-in reduit ton nombre d'inscrits. En moyenne, 20 a 30 pourcent des contacts ne confirment pas. C'est normal.

Mais ceux qui confirment sont des contacts de qualite. Ils ouvrent plus, cliquent plus, achetent plus. Ta delivrabilite s'ameliore parce que tu envoies a des gens qui veulent vraiment recevoir tes emails.

C'est un compromis. Moins de volume, plus de qualite.

Et un point important si tu utilises Fluent Forms avec FluentCRM : les deux ont chacun leur propre double opt-in. N'active pas les deux en meme temps, sinon ton contact recoit deux emails de confirmation. Active celui de FluentCRM et desactive celui de Fluent Forms.

[Pointer la note dans les settings]

**[ECRAN — sauvegarde]**

Quand tes parametres sont bons, clique sur "Save Settings".

[Clic sur Save Settings]

**[FACE CAMERA]**

Pour resumer : active le double opt-in par defaut. Desactive-le uniquement pour les acheteurs et les imports de listes deja consenties.

Et si tu hais les faibles taux de confirmation, optimise ton email. Un objet accrocheur, un texte court, un bouton visible. Ca fait la difference.

**[TRANSITION]**

C'est la fin du Module 2. Tu sais importer tes contacts, les organiser avec des listes et des tags, comprendre les statuts, creer des segments dynamiques et configurer le double opt-in. Dans le quiz qui suit, on verifie que tout est bien ancre.

---

**Points cles** :
- Le double opt-in envoie un email de confirmation avant de passer le contact en Subscribed
- Obligatoire pour un blog francais sous RGPD
- Desactive pour les acheteurs WooCommerce (consentement transactionnel)
- Reduit le volume de 20-30 % mais ameliore la qualite et la delivrabilite
- Ne pas activer le double opt-in Fluent Forms ET FluentCRM en meme temps
- Personnaliser l'email et la page de confirmation pour maximiser les confirmations

**Mots cles SEO** : double opt-in FluentCRM, RGPD email WordPress, confirmation inscription email, delivrabilite FluentCRM
