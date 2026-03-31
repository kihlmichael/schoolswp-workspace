# Scripts video — Module 7 : Workflows multi-etapes et patterns avances

**Formation** : Maitriser OttoKit
**Module** : M7 — Workflows multi-etapes et patterns avances
**Lecons** : 7 videos + 1 quiz
**Duree totale** : ~41 min de video
**Date** : 2026-03-30

---

## Lecon 7.1 — Penser son workflow : la methode avant de construire

**Duree** : 6 min
**Type** : Video HeyGen
**Ecran** : Face camera pour intro/conclusion, slides methode, screencast papier/tableau blanc

---

**[INTRO — face camera]**

Tu as appris a construire des workflows avec des triggers, des actions, des filtres, des branches. Mais la plus grosse erreur que je vois, c'est de se lancer directement dans OttoKit sans avoir reflechi avant. Un bon workflow, ca se dessine avant de se construire.

**[ECRAN — slide "Le probleme : construire sans plan"]**

Quand tu construis directement dans OttoKit :

- Tu ajoutes des blocs, tu les supprimes, tu recommences
- Tu oublies un cas de figure (que se passe-t-il si le champ est vide ?)
- Tu finis avec un workflow qui marche "a peu pres" mais qui plante dans certains cas
- Tu perds 2 heures au lieu de 30 minutes

Le probleme n'est pas OttoKit. C'est l'absence de plan.

**[ECRAN — slide "La methode en 4 etapes"]**

Avant d'ouvrir OttoKit, reponds a ces 4 questions :

1. **Quel est le declencheur ?** — Qu'est-ce qui demarre le processus ? (ex: nouvelle inscription, nouvelle commande, formulaire soumis)

2. **Quelles sont les donnees ?** — De quoi as-tu besoin ? (ex: email, prenom, montant, pays). Liste les champs.

3. **Quelles sont les etapes ?** — Qu'est-ce qui doit se passer, dans quel ordre ? Note chaque action.

4. **Quelles sont les conditions ?** — Y a-t-il des cas ou le chemin change ? (ex: VIP vs standard, France vs etranger, actif vs inactif)

**[ECRAN — screencast papier/tableau blanc]**

[Prend un papier ou ouvre un tableau blanc]
[Dessine un diagramme simple du workflow nurturing vu au M6]

Je vais te montrer avec notre workflow de nurturing.

[Ecrit "Inscription" dans un rectangle en haut]
[Fleche vers "Email bienvenue"]
[Fleche vers "Attendre 3j"]
[Fleche vers "Email relance"]
[Fleche vers "Verification : a commence M1 ?"]
[Bifurcation : OUI → "Email bravo" | NON → "Email aide + tag"]
[Fleche vers "Attendre 11j"]
[Fleche vers "Email avis"]

Voila. En 2 minutes sur papier, j'ai le workflow complet. Je vois les etapes, les conditions, les delais. Quand j'ouvre OttoKit, je sais exactement quoi construire.

**[ECRAN — slide "Checklist avant de construire"]**

Avant d'ouvrir OttoKit, verifie :

- [ ] Le declencheur est identifie
- [ ] Les donnees necessaires sont listees
- [ ] Les etapes sont ordonnees
- [ ] Les conditions sont definies (et les cas "sinon")
- [ ] Les delais sont positionnes
- [ ] Le diagramme tient sur une feuille

Si tu ne peux pas dessiner ton workflow en 5 minutes, c'est qu'il est trop complexe. Decoupe-le en plusieurs workflows.

**[TRANSITION — face camera]**

Maintenant que tu as la methode, on va voir les 3 patterns de base qui couvrent 90% des cas. Reconnaitre le bon pattern, c'est gagner du temps.

---

**Points cles**
- Toujours dessiner le workflow avant d'ouvrir OttoKit
- 4 questions : declencheur, donnees, etapes, conditions
- Si le diagramme ne tient pas sur une feuille, decouper en plusieurs workflows
- 2 minutes de planification evitent 2 heures de corrections

**Mots-cles SEO**
- planifier workflow OttoKit
- methode workflow automatisation
- diagramme workflow WordPress
- concevoir automatisation OttoKit

---

## Lecon 7.2 — Patterns courants : lineaire, conditionnel, parallele

**Duree** : 6 min
**Type** : Video HeyGen
**Ecran** : Face camera pour intro/conclusion, slides schemas, screencast OttoKit

---

**[INTRO — face camera]**

Tous les workflows du monde — pas seulement dans OttoKit — reposent sur 3 patterns de base. Quand tu les connais, tu sais immediatement comment structurer ton automatisation.

**[ECRAN — slide "Pattern 1 : Lineaire"]**

```
A → B → C → D
```

Le plus simple. Chaque etape s'execute apres la precedente, dans l'ordre. Pas de condition, pas de bifurcation.

**Exemples :**
- Formulaire soumis → envoyer email de confirmation → ajouter dans Google Sheets → notifier sur Slack
- Commande creee → envoyer facture → mettre a jour le stock

**Quand l'utiliser :** quand chaque donnee suit le meme chemin, sans exception.

**[ECRAN — slide "Pattern 2 : Conditionnel"]**

```
A → si X alors B, sinon C
```

Le workflow prend un chemin ou un autre selon une condition. C'est ce qu'on a vu avec le Filter, le Condition et le Branch.

**Exemples :**
- Commande > 200 EUR → email VIP, sinon → email standard
- Pays = FR → message en francais, sinon → message en anglais
- Categorie = bug → equipe technique, sinon → equipe commerciale

**Quand l'utiliser :** quand le traitement change selon les donnees.

**[ECRAN — slide "Pattern 3 : Parallele"]**

```
    ┌→ B
A → ├→ C
    └→ D
```

Plusieurs actions se declenchent en meme temps a partir d'un meme point. Pas de condition — toutes les branches s'executent.

**Exemples :**
- Nouvelle inscription → envoyer email + notifier Slack + ajouter dans CRM (les 3 en parallele)
- Commande completee → envoyer facture + mettre a jour le tableau de bord + generer le rapport

**Quand l'utiliser :** quand tu veux faire plusieurs choses a la fois, sans dependre l'une de l'autre.

**[ECRAN — screencast OttoKit — identification des patterns]**

[Ouvre 3 workflows existants dans OttoKit]

[Workflow 1 : formulaire → email → Google Sheets → Slack]
Ce workflow est lineaire. A → B → C → D. Pas de condition.

[Workflow 2 : commande → Branch (VIP / Standard) → actions differentes]
Ce workflow est conditionnel. Le chemin change selon le montant.

[Workflow 3 : inscription → email + Slack + CRM en parallele]
Ce workflow est parallele. Trois actions partent du meme point.

**[ECRAN — slide "Combiner les patterns"]**

En pratique, la plupart des workflows combinent plusieurs patterns.

```
A → B → si X alors C, sinon D → E
         (lineaire) (conditionnel) (lineaire)
```

Le workflow de nurturing du M6 combine les trois : lineaire (email → delay → email), conditionnel (branch actif/inactif), et potentiellement parallele (email + tag en meme temps).

L'important, c'est de reconnaitre quel pattern utiliser a chaque etape.

**[ECRAN — slide "Choisir le bon pattern"]**

| Tu veux... | Pattern |
|---|---|
| Executer des etapes dans l'ordre | Lineaire |
| Adapter selon une donnee | Conditionnel |
| Faire plusieurs choses en meme temps | Parallele |
| Combiner tout ca | Compose (plusieurs patterns enchaines) |

**[TRANSITION — face camera]**

Tu connais les 3 patterns. Dans la prochaine lecon, on voit comment gagner du temps en dupliquant et en reutilisant des etapes entre workflows.

---

**Points cles**
- 3 patterns de base : lineaire, conditionnel, parallele
- Lineaire = chaque etape suit la precedente
- Conditionnel = le chemin change selon les donnees
- Parallele = plusieurs actions en meme temps
- La plupart des workflows combinent plusieurs patterns

**Mots-cles SEO**
- patterns workflow OttoKit
- architecture workflow automatisation
- workflow lineaire conditionnel parallele
- structurer automatisation WordPress

---

## Lecon 7.3 — Dupliquer et reutiliser des etapes

**Duree** : 5 min
**Type** : Video HeyGen
**Ecran** : Face camera pour intro/conclusion, screencast OttoKit canvas

---

**[INTRO — face camera]**

Tu as construit un workflow qui marche bien. Maintenant, tu veux en creer un deuxieme avec des etapes similaires. Pas besoin de tout refaire. OttoKit te permet de dupliquer des blocs et de reutiliser tes workflows existants.

**[ECRAN — screencast OttoKit — duplication d'un bloc]**

[Ouvre un workflow existant avec plusieurs actions]
[Fait un clic droit sur un bloc d'action (ex: "Send Email")]
[Montre l'option "Duplicate" ou "Copy"]

Pour dupliquer un bloc dans le meme workflow, fais un clic droit et choisis "Duplicate". Le bloc est copie avec toute sa configuration : app, champs, valeurs.

[Montre le bloc duplique qui apparait dans le canvas]

Tu peux ensuite le deplacer et l'ajuster. Les valeurs dynamiques (les champs du trigger) sont conservees.

**[ECRAN — screencast OttoKit — copier entre workflows]**

[Ouvre un second workflow dans un autre onglet]

Pour copier un bloc d'un workflow a un autre, la methode depend de la version d'OttoKit. Deux cas :

1. **Si OttoKit supporte le copier-coller entre workflows** : tu copies le bloc dans le premier, tu le colles dans le second.

2. **Si ce n'est pas supporte** : tu recrees le bloc manuellement, mais tu gardes le premier workflow ouvert comme reference. Astuce : ouvre les deux workflows cote a cote dans deux onglets.

[Montre les deux onglets ouverts, le workflow source et le workflow cible]

Dans les deux cas, verifie toujours les champs dynamiques. Les donnees du trigger peuvent etre differentes d'un workflow a l'autre.

**[ECRAN — screencast OttoKit — dupliquer un workflow entier]**

[Retourne sur le dashboard OttoKit]
[Montre la liste des workflows]
[Clique sur les trois points (menu) a cote d'un workflow]
[Selectionne "Duplicate" ou "Clone"]

Tu peux dupliquer un workflow entier. Ca cree une copie exacte : trigger, actions, conditions, delais. Tout est copie.

[Montre le workflow duplique dans la liste — nom avec "(copy)" ou "(2)"]

C'est parfait pour creer des variantes. Par exemple, tu as un workflow de nurturing pour ta formation LMS. Tu le dupliques et tu l'adaptes pour ta formation SEO. La structure reste, seuls les contenus changent.

**[ECRAN — slide "Bonnes pratiques"]**

- Donne des noms clairs a tes workflows ("Nurturing — Formation LMS", "Nurturing — Formation SEO")
- Apres duplication, verifie tous les champs dynamiques — les donnees du trigger peuvent changer
- Garde un workflow "modele" que tu ne modifies jamais — c'est ton template
- Desactive les workflows dupliques tant qu'ils ne sont pas testes

**[TRANSITION — face camera]**

Dupliquer, c'est bien. Mais parfois, tu as besoin de repeter une action pour chaque element d'une liste. C'est le role du Loop, qu'on voit maintenant.

---

**Points cles**
- Dupliquer un bloc : clic droit → Duplicate (conserve la configuration)
- Dupliquer un workflow entier : menu → Duplicate (copie tout)
- Toujours verifier les champs dynamiques apres duplication
- Garder un workflow "modele" comme template reutilisable

**Mots-cles SEO**
- OttoKit dupliquer workflow
- copier etapes OttoKit
- template workflow OttoKit
- reutiliser automatisation WordPress

---

## Lecon 7.4 — Loop : repeter une action pour chaque element d'une liste

**Duree** : 7 min
**Type** : Video HeyGen
**Ecran** : Face camera pour intro/conclusion, screencast OttoKit canvas

---

**[INTRO — face camera]**

Tu as une liste de 50 participants a un evenement. Tu veux envoyer un email personnalise a chacun. Pas un email de masse — un email avec le prenom, le cours, la date. Le Loop fait exactement ca : il prend une liste et execute une action pour chaque element.

**[ECRAN — slide "Le concept du Loop"]**

Un Loop, c'est une boucle. Tu lui donnes une liste (un tableau de donnees), et pour chaque element du tableau, il execute les actions que tu as definies.

```
Liste : [Alice, Bob, Claire]
    │
    ├── Iteration 1 : email a Alice
    ├── Iteration 2 : email a Bob
    └── Iteration 3 : email a Claire
```

Chaque iteration a acces aux donnees de l'element en cours. Pour Alice, le champ {name} contient "Alice". Pour Bob, il contient "Bob".

**[ECRAN — screencast OttoKit — scenario email participants evenement]**

[Ouvre OttoKit]
[Cree un nouveau workflow : "Email participants evenement"]
[Ajoute un trigger — "Button" (declenchement manuel) ou Schedule]

Notre scenario : tu as un Google Sheets avec une liste de participants (colonnes : Nom, Email, Cours). Tu veux envoyer un email personnalise a chacun.

**[ECRAN — screencast OttoKit — recuperer la liste]**

[Ajoute une action "Google Sheets — Get Rows"]
[Configure : selectionne le spreadsheet, selectionne la feuille "Participants"]
[Fait un Fetch Data]

L'action Google Sheets "Get Rows" renvoie un tableau. Chaque ligne est un element du tableau.

[Montre les donnees retournees : un tableau avec 3 lignes]

On a 3 participants. Maintenant, on boucle dessus.

**[ECRAN — screencast OttoKit — ajout du Loop]**

[Clique sur "+" apres l'action Google Sheets]
[Cherche "Loop" ou "Iterator" dans la liste des apps]
[Selectionne l'app correspondante]

[Configure le Loop : selectionne le tableau retourne par Google Sheets]

Le Loop prend le tableau en entree. Pour chaque element, il va executer les actions que tu places a l'interieur.

**[ECRAN — screencast OttoKit — action dans le Loop]**

[A l'interieur du Loop, ajoute une action "Send Email"]
[Destinataire : {current_item.email}]
[Objet : "{current_item.nom}, rappel pour ton cours"]
[Corps : "Bonjour {current_item.nom}, ton cours {current_item.cours} commence bientot..."]

A l'interieur du Loop, tu accedes aux champs de l'element en cours. Le selecteur de donnees dynamiques montre les champs de la ligne actuelle : nom, email, cours.

**[ECRAN — screencast OttoKit — test du Loop]**

[Lance le workflow en mode test]
[Montre l'historique : 3 executions successives]
[Ouvre le detail de chaque iteration — chaque email a un destinataire different]

Le Loop a execute l'action 3 fois : une fois pour Alice, une fois pour Bob, une fois pour Claire. Chaque email est personnalise.

**[ECRAN — slide "Limites et precautions"]**

Quelques points importants :

- **Nombre d'elements** — chaque iteration consomme une task OttoKit. 50 participants = 50 tasks pour l'action email.
- **Temps d'execution** — un Loop de 100 elements prend plus de temps qu'un envoi simple. Prevois le temps.
- **Pas de Loop infini** — OttoKit a une limite par defaut. Tu ne risques pas de boucle sans fin.
- **Erreur sur un element** — si une iteration echoue (email invalide), les autres continuent. Verifie l'historique.

**[ECRAN — slide "Cas d'usage courants du Loop"]**

| Scenario | Source | Action par element |
|---|---|---|
| Email a chaque participant | Google Sheets | Send Email |
| Tag CRM a chaque contact d'un segment | FluentCRM | Add Tag |
| Notification pour chaque produit en rupture | WooCommerce | Slack Message |
| Mise a jour de chaque ligne d'un tableur | Google Sheets | Update Row |

**[TRANSITION — face camera]**

Le Loop est un outil indispensable des que tu travailles avec des listes. Dans la prochaine lecon, on decouvre un autre outil avance : l'Email Parser, qui transforme un email en donnees exploitables.

---

**Points cles**
- Le Loop execute une action pour chaque element d'une liste (tableau)
- Chaque iteration accede aux donnees de l'element en cours
- Chaque iteration consomme une task OttoKit — a prendre en compte
- Si une iteration echoue, les autres continuent

**Mots-cles SEO**
- OttoKit Loop
- boucle workflow OttoKit
- iteration automatisation WordPress
- envoyer email liste OttoKit

---

## Lecon 7.5 — Email Parser : transforme un email en donnees exploitables

**Duree** : 7 min
**Type** : Video HeyGen
**Ecran** : Face camera pour intro/conclusion, screencast OttoKit canvas

---

**[INTRO — face camera]**

Tu recois des emails de commande, de notification, de contact. Ces emails contiennent des donnees utiles : un nom, un montant, une reference. Mais c'est du texte brut. L'Email Parser d'OttoKit transforme ce texte en donnees structurees que tes workflows peuvent exploiter.

**[ECRAN — slide "Le probleme : les emails sont du texte"]**

Voici un email type de commande :

```
Sujet : Nouvelle commande #1234
De : boutique@monsite.com

Bonjour,
Une nouvelle commande a ete passee.

Client : Marie Dupont
Email : marie@example.com
Montant : 89,00 EUR
Produit : Formation WordPress Avancee
```

Cet email contient 4 informations utiles. Mais pour OttoKit, c'est juste un bloc de texte. L'Email Parser va extraire chaque information dans un champ separe.

**[ECRAN — screencast OttoKit — configuration du trigger email]**

[Ouvre OttoKit]
[Cree un nouveau workflow : "Parse email commande"]
[Ajoute un trigger email — "Email Received" ou equivalent]

Le point de depart, c'est un trigger qui detecte un nouvel email. OttoKit peut se connecter a ton email via Gmail, Outlook, ou un email de transfert dedie.

[Configure le trigger avec la boite email source]
[Fait un Fetch Data — montre un email brut recupere]

**[ECRAN — screencast OttoKit — ajout de l'Email Parser]**

[Clique sur "+" apres le trigger]
[Cherche "Email Parser" ou "Text Parser" dans la liste]
[Selectionne l'app]

L'Email Parser te permet de definir des regles d'extraction. Pour chaque donnee que tu veux recuperer, tu crees une regle.

[Configure la regle 1 : "Client"]
[Methode : chercher le texte apres "Client : " jusqu'a la fin de la ligne]

[Configure la regle 2 : "Montant"]
[Methode : chercher le texte apres "Montant : " jusqu'a la fin de la ligne]

[Configure la regle 3 : "Produit"]
[Methode : chercher le texte apres "Produit : " jusqu'a la fin de la ligne]

Chaque regle extrait un champ precis. Le parser utilise des marqueurs textuels pour reperer ou se trouve l'information.

**[ECRAN — screencast OttoKit — utilisation des donnees parsees]**

[Ajoute une action "Google Sheets — Add Row" apres le parser]
[Mappe les champs : Colonne A = {parsed_client}, Colonne B = {parsed_montant}, Colonne C = {parsed_produit}]

Maintenant, les donnees extraites sont utilisables comme n'importe quel champ dynamique. Tu peux les envoyer dans Google Sheets, dans ton CRM, dans un email de confirmation.

**[ECRAN — screencast OttoKit — test]**

[Lance un test avec l'email d'exemple]
[Montre les donnees parsees : Client = "Marie Dupont", Montant = "89,00 EUR", Produit = "Formation WordPress Avancee"]
[Montre la ligne ajoutee dans Google Sheets avec les 3 valeurs]

Le parsing fonctionne. L'email brut est devenu 3 champs exploitables.

**[ECRAN — slide "Cas d'usage courants"]**

| Email recu | Donnees extraites | Action suivante |
|---|---|---|
| Notification de commande | Client, montant, produit | Ajouter dans CRM + Google Sheets |
| Email de contact (formulaire) | Nom, email, message | Creer un ticket support |
| Alerte monitoring | Serveur, erreur, heure | Notification Slack urgente |
| Email de facture fournisseur | Montant, date, reference | Ajouter dans le suivi comptable |

**[ECRAN — slide "Limites et alternatives"]**

- Le parsing fonctionne bien quand le format de l'email est constant. Si le format change, les regles cassent.
- Pour des emails tres variables, envisage d'utiliser un webhook ou un formulaire a la place.
- Certains services (Stripe, WooCommerce) envoient des webhooks structures — plus fiables que le parsing email.

**[TRANSITION — face camera]**

L'Email Parser est un pont entre le monde des emails et le monde des donnees structurees. Dans la prochaine lecon, on voit comment sauvegarder et transferer tes workflows avec l'export et l'import.

---

**Points cles**
- L'Email Parser transforme du texte brut en champs exploitables
- Chaque regle d'extraction cible une donnee precise
- Les donnees parsees s'utilisent comme n'importe quel champ dynamique
- Le parsing fonctionne mieux avec des emails au format constant

**Mots-cles SEO**
- OttoKit Email Parser
- parser email automatisation
- extraire donnees email OttoKit
- email vers donnees workflow WordPress

---

## Lecon 7.6 — Export et import de workflows

**Duree** : 5 min
**Type** : Video HeyGen
**Ecran** : Face camera pour intro/conclusion, screencast OttoKit

---

**[INTRO — face camera]**

Tu as construit un workflow parfait. Maintenant tu veux le deployer sur un autre site. Ou tu veux le sauvegarder avant de le modifier. L'export et l'import sont la pour ca.

**[ECRAN — screencast OttoKit — export d'un workflow]**

[Ouvre le dashboard OttoKit]
[Selectionne un workflow existant (ex: "Nurturing inscription")]
[Clique sur les trois points (menu) du workflow]
[Selectionne "Export" ou "Download"]

L'export genere un fichier JSON. Ce fichier contient tout : le trigger, les actions, les conditions, les delais, le mapping des champs.

[Montre le fichier JSON telecharge]
[Ouvre brievement le fichier dans un editeur — montre la structure]

Tu n'as pas besoin de comprendre le JSON. C'est un fichier de sauvegarde que tu peux reimporter.

**[ECRAN — slide "Que contient le fichier JSON ?"]**

Le fichier d'export contient :

- La structure du workflow (ordre des blocs)
- La configuration de chaque bloc (app, evenement, champs)
- Les conditions, filtres, branches
- Les delais

Ce qu'il ne contient PAS :

- Les identifiants de connexion (tokens, mots de passe)
- Les donnees reelles (emails, noms)
- L'historique d'execution

C'est normal et c'est securise. Apres l'import, tu devras reconnecter tes apps.

**[ECRAN — screencast OttoKit — import d'un workflow]**

[Retourne sur le dashboard]
[Clique sur "Import Workflow" ou "Upload"]
[Selectionne le fichier JSON exporte]

[Montre le workflow importe qui apparait dans la liste]

Le workflow est importe avec toute sa structure. Mais il est en mode inactif — il ne se declenche pas.

[Ouvre le workflow importe]
[Montre les blocs avec des icones d'alerte sur les connexions]

Tu vois des alertes sur certains blocs. C'est parce que les connexions ne sont pas encore configurees. Il faut associer chaque app a une connexion existante sur ce compte.

**[ECRAN — screencast OttoKit — reconfiguration des connexions]**

[Clique sur le bloc trigger]
[Selectionne la connexion WordPress locale dans le dropdown]
[Clique sur le bloc action Google Sheets]
[Selectionne la connexion Google existante]

Tu reconfigures chaque connexion une par une. Ca prend 2-3 minutes. Ensuite, fais un Fetch Data sur le trigger pour verifier que tout est en ordre.

[Fait un Fetch Data sur le trigger — donnees chargees]

C'est bon. Le workflow est pret a etre teste et active.

**[ECRAN — slide "Cas d'usage de l'export/import"]**

| Situation | Action |
|---|---|
| Deployer un workflow sur le site d'un client | Export → envoyer le JSON → import chez le client |
| Sauvegarder avant modification | Export → garder le fichier comme backup |
| Partager un template avec ta communaute | Export → mettre le fichier en telechargement |
| Migrer d'un compte OttoKit a un autre | Export tous les workflows → import sur le nouveau compte |

**[TRANSITION — face camera]**

L'export/import fonctionne avec des fichiers. Mais OttoKit propose aussi une methode plus directe : le partage par URL. On voit ca tout de suite.

---

**Points cles**
- L'export genere un fichier JSON contenant toute la structure du workflow
- Les identifiants et donnees reelles ne sont pas exportes (securite)
- Apres import, reconnecter les apps et faire un Fetch Data
- Le workflow importe est inactif par defaut — tester avant d'activer

**Mots-cles SEO**
- OttoKit export workflow
- importer workflow OttoKit
- JSON export OttoKit
- transferer workflow automatisation WordPress

---

## Lecon 7.7 — Partager un workflow par URL

**Duree** : 5 min
**Type** : Video HeyGen
**Ecran** : Face camera pour intro/conclusion, screencast OttoKit

---

**[INTRO — face camera]**

Tu veux partager un workflow avec un collegue, un client, ou ta communaute. Plutot que d'envoyer un fichier JSON, OttoKit te permet de generer un lien de partage. La personne clique, et le workflow est importe dans son compte.

**[ECRAN — screencast OttoKit — generation du lien de partage]**

[Ouvre un workflow existant]
[Clique sur les trois points (menu) ou le bouton de partage]
[Selectionne "Share" ou "Share Link"]

OttoKit genere une URL unique pour ce workflow.

[Montre l'URL generee]
[Copie l'URL]

Cette URL est publique. N'importe qui avec le lien peut importer ce workflow dans son propre compte OttoKit. Attention : les connexions ne sont pas partagees. Le destinataire devra configurer ses propres apps.

**[ECRAN — screencast OttoKit — vue du destinataire]**

[Ouvre le lien dans un navigateur en mode prive (simuler un autre utilisateur)]
[Montre la page d'import : apercu du workflow, bouton "Import"]
[Clique sur "Import"]
[Montre le workflow importe dans le compte]

Le destinataire voit un apercu du workflow : les etapes, les apps utilisees. Il clique sur "Import" et le workflow est copie dans son compte. Comme avec l'import JSON, il devra reconnecter ses apps.

**[ECRAN — slide "URL de partage vs export JSON"]**

| | URL de partage | Export JSON |
|---|---|---|
| Envoi | Lien a copier-coller | Fichier a telecharger et envoyer |
| Acces | N'importe qui avec le lien | Seulement qui a le fichier |
| Mise a jour | Le lien pointe vers la version au moment du partage | Le fichier est fige |
| Ideal pour | Communaute, formations, collegues | Backup, migration, deploiement client |

**[ECRAN — slide "Cas d'usage pour schoolsWP"]**

Chez schoolsWP, on utilise le partage par URL pour :

- Partager des workflows "modeles" avec les apprenants de la formation
- Donner un workflow pre-configure a un client freelance
- Publier un workflow dans un article de blog comme ressource gratuite

Par exemple, a la fin de cette formation, tu trouveras des liens vers des workflows OttoKit prets a importer. Tu cliques, tu importes, tu configures tes apps, et ca tourne.

**[ECRAN — slide "Precautions"]**

- L'URL est publique — ne partage pas un workflow contenant des infos sensibles dans sa configuration
- Le workflow partage est une copie — les modifications sur l'original ne se propagent pas
- Desactive le lien si tu ne veux plus que d'autres personnes importent le workflow
- Verifie toujours les permissions des apps apres import

**[TRANSITION — face camera]**

Tu sais maintenant construire des workflows structures, les dupliquer, les boucler, les parser, les exporter et les partager. Le Module 7 est termine. Place au quiz pour valider tout ca.

---

**Points cles**
- OttoKit permet de partager un workflow via une URL publique
- Le destinataire importe le workflow dans son compte en un clic
- Les connexions ne sont pas partagees — chacun configure ses propres apps
- URL pour le partage rapide, JSON pour le backup et la migration

**Mots-cles SEO**
- OttoKit partager workflow
- lien partage workflow OttoKit
- template workflow OttoKit communaute
- partager automatisation WordPress

---

## Notes de production — Module 7

### Captures a preparer
- Feuille papier / tableau blanc avec diagramme workflow nurturing (lecon 7.1)
- Slide 3 patterns : lineaire (A→B→C), conditionnel (A→si X alors B sinon C), parallele (A→B+C+D)
- Canvas OttoKit : clic droit sur un bloc → menu "Duplicate"
- Canvas OttoKit : deux workflows ouverts cote a cote (onglets navigateur)
- Dashboard OttoKit : menu workflow → "Duplicate"
- Canvas OttoKit : Loop avec Google Sheets "Get Rows" → bloc Loop → action "Send Email"
- Historique Loop : 3 iterations successives avec details
- Email brut (notification commande) dans un client email
- Canvas OttoKit : Email Parser avec regles d'extraction configurees
- Donnees parsees dans le panneau de resultats
- Dashboard OttoKit : menu workflow → "Export" → fichier JSON telecharge
- Fichier JSON ouvert dans un editeur (structure visible)
- Dashboard OttoKit : bouton "Import Workflow" → selection du fichier
- Workflow importe avec alertes sur les connexions
- OttoKit : bouton "Share" → URL generee
- Vue destinataire : page d'apercu du workflow avec bouton "Import"

### Environnement de demo
- Compte OttoKit (plan premium recommande pour les loops et multi-etapes)
- Site WordPress schoolsWP avec WooCommerce et TutorLMS
- Google Sheets avec une feuille "Participants" (colonnes : Nom, Email, Cours, 3 lignes de donnees)
- Boite email avec des emails de notification (commande WooCommerce ou equivalent)
- Un second compte OttoKit ou un navigateur en mode prive (pour simuler le destinataire du partage)
- Papier et stylo ou tableau blanc (pour la lecon 7.1)
- 3 workflows existants representant les 3 patterns (lecon 7.2)

### Duree estimee par lecon (hors quiz)
| Lecon | Duree video |
|-------|-------------|
| 7.1 | 6 min |
| 7.2 | 6 min |
| 7.3 | 5 min |
| 7.4 | 7 min |
| 7.5 | 7 min |
| 7.6 | 5 min |
| 7.7 | 5 min |
| **Total M7** | **41 min** |
