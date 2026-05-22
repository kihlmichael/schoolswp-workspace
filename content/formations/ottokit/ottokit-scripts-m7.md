# Scripts vidéo — Module 7 : Workflows multi-étapes et patterns avancés

**Formation** : Maîtriser OttoKit
**Module** : M7 — Workflows multi-étapes et patterns avancés
**Leçons** : 7 vidéos + 1 quiz
**Durée totale** : ~41 min de vidéo
**Date** : 2026-03-30

---

## Leçon 7.1 — Penser son workflow : la méthode avant de construire

**Durée** : 6 min
**Type** : Vidéo HeyGen
**Écran** : Face caméra pour intro/conclusion, slides méthode, screencast papier/tableau blanc

---

**[INTRO — face caméra]**

Tu as appris à construire des workflows avec des triggers, des actions, des filtres, des branches. Mais la plus grosse erreur que je vois, c'est de se lancer directement dans OttoKit sans avoir réfléchi avant. Un bon workflow, ça se dessine avant de se construire.

**[ÉCRAN — slide "Le problème : construire sans plan"]**

Quand tu construis directement dans OttoKit :

- Tu ajoutes des blocs, tu les supprimes, tu recommences
- Tu oublies un cas de figure (que se passe-t-il si le champ est vide ?)
- Tu finis avec un workflow qui marche "à peu près" mais qui plante dans certains cas
- Tu perds 2 heures au lieu de 30 minutes

Le problème n'est pas OttoKit. C'est l'absence de plan.

**[ÉCRAN — slide "La méthode en 4 étapes"]**

Avant d'ouvrir OttoKit, réponds à ces 4 questions :

1. **Quel est le déclencheur ?** — Qu'est-ce qui démarre le processus ? (ex: nouvelle inscription, nouvelle commande, formulaire soumis)

2. **Quelles sont les données ?** — De quoi as-tu besoin ? (ex: email, prénom, montant, pays). Liste les champs.

3. **Quelles sont les étapes ?** — Qu'est-ce qui doit se passer, dans quel ordre ? Note chaque action.

4. **Quelles sont les conditions ?** — Y a-t-il des cas où le chemin change ? (ex: VIP vs standard, France vs étranger, actif vs inactif)

**[ÉCRAN — screencast papier/tableau blanc]**

[Prend un papier ou ouvre un tableau blanc]
[Dessine un diagramme simple du workflow nurturing vu au M6]

Je vais te montrer avec notre workflow de nurturing.

[Écrit "Inscription" dans un rectangle en haut]
[Flèche vers "Email bienvenue"]
[Flèche vers "Attendre 3j"]
[Flèche vers "Email relance"]
[Flèche vers "Vérification : a commencé M1 ?"]
[Bifurcation : OUI → "Email bravo" | NON → "Email aide + tag"]
[Flèche vers "Attendre 11j"]
[Flèche vers "Email avis"]

Voilà. En 2 minutes sur papier, j'ai le workflow complet. Je vois les étapes, les conditions, les délais. Quand j'ouvre OttoKit, je sais exactement quoi construire.

**[ÉCRAN — slide "Checklist avant de construire"]**

Avant d'ouvrir OttoKit, vérifie :

- [ ] Le déclencheur est identifié
- [ ] Les données nécessaires sont listées
- [ ] Les étapes sont ordonnées
- [ ] Les conditions sont définies (et les cas "sinon")
- [ ] Les délais sont positionnés
- [ ] Le diagramme tient sur une feuille

Si tu ne peux pas dessiner ton workflow en 5 minutes, c'est qu'il est trop complexe. Découpe-le en plusieurs workflows.

**[TRANSITION — face caméra]**

Maintenant que tu as la méthode, on va voir les 3 patterns de base qui couvrent 90% des cas. Reconnaître le bon pattern, c'est gagner du temps.

---

**Points clés**
- Toujours dessiner le workflow avant d'ouvrir OttoKit
- 4 questions : déclencheur, données, étapes, conditions
- Si le diagramme ne tient pas sur une feuille, découper en plusieurs workflows
- 2 minutes de planification évitent 2 heures de corrections

**Mots-clés SEO**
- planifier workflow OttoKit
- méthode workflow automatisation
- diagramme workflow WordPress
- concevoir automatisation OttoKit

---

## Leçon 7.2 — Patterns courants : linéaire, conditionnel, parallèle

**Durée** : 6 min
**Type** : Vidéo HeyGen
**Écran** : Face caméra pour intro/conclusion, slides schémas, screencast OttoKit

---

**[INTRO — face caméra]**

Tous les workflows du monde — pas seulement dans OttoKit — reposent sur 3 patterns de base. Quand tu les connais, tu sais immédiatement comment structurer ton automatisation.

**[ÉCRAN — slide "Pattern 1 : Linéaire"]**

```
A → B → C → D
```

Le plus simple. Chaque étape s'exécute après la précédente, dans l'ordre. Pas de condition, pas de bifurcation.

**Exemples :**
- Formulaire soumis → envoyer email de confirmation → ajouter dans Google Sheets → notifier sur Slack
- Commande créée → envoyer facture → mettre à jour le stock

**Quand l'utiliser :** quand chaque donnée suit le même chemin, sans exception.

**[ÉCRAN — slide "Pattern 2 : Conditionnel"]**

```
A → si X alors B, sinon C
```

Le workflow prend un chemin ou un autre selon une condition. C'est ce qu'on a vu avec le Filter, le Condition et le Branch.

**Exemples :**
- Commande > 200 EUR → email VIP, sinon → email standard
- Pays = FR → message en français, sinon → message en anglais
- Catégorie = bug → équipe technique, sinon → équipe commerciale

**Quand l'utiliser :** quand le traitement change selon les données.

**[ÉCRAN — slide "Pattern 3 : Parallèle"]**

```
    ┌→ B
A → ├→ C
    └→ D
```

Plusieurs actions se déclenchent en même temps à partir d'un même point. Pas de condition — toutes les branches s'exécutent.

**Exemples :**
- Nouvelle inscription → envoyer email + notifier Slack + ajouter dans CRM (les 3 en parallèle)
- Commande complétée → envoyer facture + mettre à jour le tableau de bord + générer le rapport

**Quand l'utiliser :** quand tu veux faire plusieurs choses à la fois, sans dépendre l'une de l'autre.

**[ÉCRAN — screencast OttoKit — identification des patterns]**

[Ouvre 3 workflows existants dans OttoKit]

[Workflow 1 : formulaire → email → Google Sheets → Slack]
Ce workflow est linéaire. A → B → C → D. Pas de condition.

[Workflow 2 : commande → Branch (VIP / Standard) → actions différentes]
Ce workflow est conditionnel. Le chemin change selon le montant.

[Workflow 3 : inscription → email + Slack + CRM en parallèle]
Ce workflow est parallèle. Trois actions partent du même point.

**[ÉCRAN — slide "Combiner les patterns"]**

En pratique, la plupart des workflows combinent plusieurs patterns.

```
A → B → si X alors C, sinon D → E
         (linéaire) (conditionnel) (linéaire)
```

Le workflow de nurturing du M6 combine les trois : linéaire (email → delay → email), conditionnel (branch actif/inactif), et potentiellement parallèle (email + tag en même temps).

L'important, c'est de reconnaître quel pattern utiliser à chaque étape.

**[ÉCRAN — slide "Choisir le bon pattern"]**

| Tu veux... | Pattern |
|---|---|
| Exécuter des étapes dans l'ordre | Linéaire |
| Adapter selon une donnée | Conditionnel |
| Faire plusieurs choses en même temps | Parallèle |
| Combiner tout ça | Composé (plusieurs patterns enchaînés) |

**[TRANSITION — face caméra]**

Tu connais les 3 patterns. Dans la prochaine leçon, on voit comment gagner du temps en dupliquant et en réutilisant des étapes entre workflows.

---

**Points clés**
- 3 patterns de base : linéaire, conditionnel, parallèle
- Linéaire = chaque étape suit la précédente
- Conditionnel = le chemin change selon les données
- Parallèle = plusieurs actions en même temps
- La plupart des workflows combinent plusieurs patterns

**Mots-clés SEO**
- patterns workflow OttoKit
- architecture workflow automatisation
- workflow linéaire conditionnel parallèle
- structurer automatisation WordPress

---

## Leçon 7.3 — Dupliquer et réutiliser des étapes

**Durée** : 5 min
**Type** : Vidéo HeyGen
**Écran** : Face caméra pour intro/conclusion, screencast OttoKit canvas

---

**[INTRO — face caméra]**

Tu as construit un workflow qui marche bien. Maintenant, tu veux en créer un deuxième avec des étapes similaires. Pas besoin de tout refaire. OttoKit te permet de dupliquer des blocs et de réutiliser tes workflows existants.

**[ÉCRAN — screencast OttoKit — duplication d'un bloc]**

[Ouvre un workflow existant avec plusieurs actions]
[Fait un clic droit sur un bloc d'action (ex: "Send Email")]
[Montre l'option "Duplicate" ou "Copy"]

Pour dupliquer un bloc dans le même workflow, fais un clic droit et choisis "Duplicate". Le bloc est copié avec toute sa configuration : app, champs, valeurs.

[Montre le bloc dupliqué qui apparaît dans le canvas]

Tu peux ensuite le déplacer et l'ajuster. Les valeurs dynamiques (les champs du trigger) sont conservées.

**[ÉCRAN — screencast OttoKit — copier entre workflows]**

[Ouvre un second workflow dans un autre onglet]

Pour copier un bloc d'un workflow à un autre, la méthode dépend de la version d'OttoKit. Deux cas :

1. **Si OttoKit supporte le copier-coller entre workflows** : tu copies le bloc dans le premier, tu le colles dans le second.

2. **Si ce n'est pas supporté** : tu recrées le bloc manuellement, mais tu gardes le premier workflow ouvert comme référence. Astuce : ouvre les deux workflows côte à côté dans deux onglets.

[Montre les deux onglets ouverts, le workflow source et le workflow cible]

Dans les deux cas, vérifie toujours les champs dynamiques. Les données du trigger peuvent être différentes d'un workflow à l'autre.

**[ÉCRAN — screencast OttoKit — dupliquer un workflow entier]**

[Retourne sur le dashboard OttoKit]
[Montre la liste des workflows]
[Clique sur les trois points (menu) à côté d'un workflow]
[Sélectionne "Duplicate" ou "Clone"]

Tu peux dupliquer un workflow entier. Ça crée une copie exacte : trigger, actions, conditions, délais. Tout est copié.

[Montre le workflow dupliqué dans la liste — nom avec "(copy)" ou "(2)"]

C'est parfait pour créer des variantes. Par exemple, tu as un workflow de nurturing pour ta formation LMS. Tu le dupliques et tu l'adaptes pour ta formation SEO. La structure reste, seuls les contenus changent.

**[ÉCRAN — slide "Bonnes pratiques"]**

- Donne des noms clairs à tes workflows ("Nurturing — Formation LMS", "Nurturing — Formation SEO")
- Après duplication, vérifie tous les champs dynamiques — les données du trigger peuvent changer
- Garde un workflow "modèle" que tu ne modifies jamais — c'est ton template
- Désactive les workflows dupliqués tant qu'ils ne sont pas testés

**[TRANSITION — face caméra]**

Dupliquer, c'est bien. Mais parfois, tu as besoin de répéter une action pour chaque élément d'une liste. C'est le rôle du Loop, qu'on voit maintenant.

---

**Points clés**
- Dupliquer un bloc : clic droit → Duplicate (conserve la configuration)
- Dupliquer un workflow entier : menu → Duplicate (copie tout)
- Toujours vérifier les champs dynamiques après duplication
- Garder un workflow "modèle" comme template réutilisable

**Mots-clés SEO**
- OttoKit dupliquer workflow
- copier étapes OttoKit
- template workflow OttoKit
- réutiliser automatisation WordPress

---

## Leçon 7.4 — Loop : répéter une action pour chaque élément d'une liste

**Durée** : 7 min
**Type** : Vidéo HeyGen
**Écran** : Face caméra pour intro/conclusion, screencast OttoKit canvas

---

**[INTRO — face caméra]**

Tu as une liste de 50 participants à un événement. Tu veux envoyer un email personnalisé à chacun. Pas un email de masse — un email avec le prénom, le cours, la date. Le Loop fait exactement ça : il prend une liste et exécute une action pour chaque élément.

**[ÉCRAN — slide "Le concept du Loop"]**

Un Loop, c'est une boucle. Tu lui donnes une liste (un tableau de données), et pour chaque élément du tableau, il exécute les actions que tu as définies.

```
Liste : [Alice, Bob, Claire]
    │
    ├── Itération 1 : email à Alice
    ├── Itération 2 : email à Bob
    └── Itération 3 : email à Claire
```

Chaque itération a accès aux données de l'élément en cours. Pour Alice, le champ {name} contient "Alice". Pour Bob, il contient "Bob".

**[ÉCRAN — screencast OttoKit — scénario email participants événement]**

[Ouvre OttoKit]
[Crée un nouveau workflow : "Email participants événement"]
[Ajoute un trigger — "Button" (déclenchement manuel) ou Schedule]

Notre scénario : tu as un Google Sheets avec une liste de participants (colonnes : Nom, Email, Cours). Tu veux envoyer un email personnalisé à chacun.

**[ÉCRAN — screencast OttoKit — récupérer la liste]**

[Ajoute une action "Google Sheets — Get Rows"]
[Configure : sélectionne le spreadsheet, sélectionne la feuille "Participants"]
[Fait un Fetch Data]

L'action Google Sheets "Get Rows" renvoie un tableau. Chaque ligne est un élément du tableau.

[Montre les données retournées : un tableau avec 3 lignes]

On a 3 participants. Maintenant, on boucle dessus.

**[ÉCRAN — screencast OttoKit — ajout du Loop]**

[Clique sur "+" après l'action Google Sheets]
[Cherche "Loop" ou "Iterator" dans la liste des apps]
[Sélectionne l'app correspondante]

[Configure le Loop : sélectionne le tableau retourné par Google Sheets]

Le Loop prend le tableau en entrée. Pour chaque élément, il va exécuter les actions que tu places à l'intérieur.

**[ÉCRAN — screencast OttoKit — action dans le Loop]**

[À l'intérieur du Loop, ajoute une action "Send Email"]
[Destinataire : {current_item.email}]
[Objet : "{current_item.nom}, rappel pour ton cours"]
[Corps : "Bonjour {current_item.nom}, ton cours {current_item.cours} commence bientôt..."]

À l'intérieur du Loop, tu accèdes aux champs de l'élément en cours. Le sélecteur de données dynamiques montre les champs de la ligne actuelle : nom, email, cours.

**[ÉCRAN — screencast OttoKit — test du Loop]**

[Lance le workflow en mode test]
[Montre l'historique : 3 exécutions successives]
[Ouvre le détail de chaque itération — chaque email a un destinataire différent]

Le Loop a exécuté l'action 3 fois : une fois pour Alice, une fois pour Bob, une fois pour Claire. Chaque email est personnalisé.

**[ÉCRAN — slide "Limites et précautions"]**

Quelques points importants :

- **Nombre d'éléments** — chaque itération consomme une task OttoKit. 50 participants = 50 tasks pour l'action email.
- **Temps d'exécution** — un Loop de 100 éléments prend plus de temps qu'un envoi simple. Prévois le temps.
- **Pas de Loop infini** — OttoKit a une limite par défaut. Tu ne risques pas de boucle sans fin.
- **Erreur sur un élément** — si une itération échoue (email invalide), les autres continuent. Vérifie l'historique.

**[ÉCRAN — slide "Cas d'usage courants du Loop"]**

| Scénario | Source | Action par élément |
|---|---|---|
| Email à chaque participant | Google Sheets | Send Email |
| Tag CRM à chaque contact d'un segment | FluentCRM | Add Tag |
| Notification pour chaque produit en rupture | WooCommerce | Slack Message |
| Mise à jour de chaque ligne d'un tableur | Google Sheets | Update Row |

**[TRANSITION — face caméra]**

Le Loop est un outil indispensable dès que tu travailles avec des listes. Dans la prochaine leçon, on découvre un autre outil avancé : l'Email Parser, qui transforme un email en données exploitables.

---

**Points clés**
- Le Loop exécute une action pour chaque élément d'une liste (tableau)
- Chaque itération accède aux données de l'élément en cours
- Chaque itération consomme une task OttoKit — à prendre en compte
- Si une itération échoue, les autres continuent

**Mots-clés SEO**
- OttoKit Loop
- boucle workflow OttoKit
- itération automatisation WordPress
- envoyer email liste OttoKit

---

## Leçon 7.5 — Email Parser : transforme un email en données exploitables

**Durée** : 7 min
**Type** : Vidéo HeyGen
**Écran** : Face caméra pour intro/conclusion, screencast OttoKit canvas

---

**[INTRO — face caméra]**

Tu reçois des emails de commande, de notification, de contact. Ces emails contiennent des données utiles : un nom, un montant, une référence. Mais c'est du texte brut. L'Email Parser d'OttoKit transforme ce texte en données structurées que tes workflows peuvent exploiter.

**[ÉCRAN — slide "Le problème : les emails sont du texte"]**

Voici un email type de commande :

```
Sujet : Nouvelle commande #1234
De : boutique@monsite.com

Bonjour,
Une nouvelle commande a été passée.

Client : Marie Dupont
Email : marie@example.com
Montant : 89,00 EUR
Produit : Formation WordPress Avancée
```

Cet email contient 4 informations utiles. Mais pour OttoKit, c'est juste un bloc de texte. L'Email Parser va extraire chaque information dans un champ séparé.

**[ÉCRAN — screencast OttoKit — configuration du trigger email]**

[Ouvre OttoKit]
[Crée un nouveau workflow : "Parse email commande"]
[Ajoute un trigger email — "Email Received" ou équivalent]

Le point de départ, c'est un trigger qui détecte un nouvel email. OttoKit peut se connecter à ton email via Gmail, Outlook, ou un email de transfert dédié.

[Configure le trigger avec la boîte email source]
[Fait un Fetch Data — montre un email brut récupéré]

**[ÉCRAN — screencast OttoKit — ajout de l'Email Parser]**

[Clique sur "+" après le trigger]
[Cherche "Email Parser" ou "Text Parser" dans la liste]
[Sélectionne l'app]

L'Email Parser te permet de définir des règles d'extraction. Pour chaque donnée que tu veux récupérer, tu crées une règle.

[Configure la règle 1 : "Client"]
[Méthode : chercher le texte après "Client : " jusqu'à la fin de la ligne]

[Configure la règle 2 : "Montant"]
[Méthode : chercher le texte après "Montant : " jusqu'à la fin de la ligne]

[Configure la règle 3 : "Produit"]
[Méthode : chercher le texte après "Produit : " jusqu'à la fin de la ligne]

Chaque règle extrait un champ précis. Le parser utilise des marqueurs textuels pour repérer où se trouve l'information.

**[ÉCRAN — screencast OttoKit — utilisation des données parsées]**

[Ajoute une action "Google Sheets — Add Row" après le parser]
[Mappe les champs : Colonne A = {parsed_client}, Colonne B = {parsed_montant}, Colonne C = {parsed_produit}]

Maintenant, les données extraites sont utilisables comme n'importe quel champ dynamique. Tu peux les envoyer dans Google Sheets, dans ton CRM, dans un email de confirmation.

**[ÉCRAN — screencast OttoKit — test]**

[Lance un test avec l'email d'exemple]
[Montre les données parsées : Client = "Marie Dupont", Montant = "89,00 EUR", Produit = "Formation WordPress Avancée"]
[Montre la ligne ajoutée dans Google Sheets avec les 3 valeurs]

Le parsing fonctionne. L'email brut est devenu 3 champs exploitables.

**[ÉCRAN — slide "Cas d'usage courants"]**

| Email reçu | Données extraites | Action suivante |
|---|---|---|
| Notification de commande | Client, montant, produit | Ajouter dans CRM + Google Sheets |
| Email de contact (formulaire) | Nom, email, message | Créer un ticket support |
| Alerte monitoring | Serveur, erreur, heure | Notification Slack urgente |
| Email de facture fournisseur | Montant, date, référence | Ajouter dans le suivi comptable |

**[ÉCRAN — slide "Limites et alternatives"]**

- Le parsing fonctionne bien quand le format de l'email est constant. Si le format change, les règles cassent.
- Pour des emails très variables, envisage d'utiliser un webhook ou un formulaire à la place.
- Certains services (Stripe, WooCommerce) envoient des webhooks structurés — plus fiables que le parsing email.

**[TRANSITION — face caméra]**

L'Email Parser est un pont entre le monde des emails et le monde des données structurées. Dans la prochaine leçon, on voit comment sauvegarder et transférer tes workflows avec l'export et l'import.

---

**Points clés**
- L'Email Parser transforme du texte brut en champs exploitables
- Chaque règle d'extraction cible une donnée précise
- Les données parsées s'utilisent comme n'importe quel champ dynamique
- Le parsing fonctionne mieux avec des emails au format constant

**Mots-clés SEO**
- OttoKit Email Parser
- parser email automatisation
- extraire données email OttoKit
- email vers données workflow WordPress

---

## Leçon 7.6 — Export et import de workflows

**Durée** : 5 min
**Type** : Vidéo HeyGen
**Écran** : Face caméra pour intro/conclusion, screencast OttoKit

---

**[INTRO — face caméra]**

Tu as construit un workflow parfait. Maintenant tu veux le déployer sur un autre site. Ou tu veux le sauvegarder avant de le modifier. L'export et l'import sont là pour ça.

**[ÉCRAN — screencast OttoKit — export d'un workflow]**

[Ouvre le dashboard OttoKit]
[Sélectionne un workflow existant (ex: "Nurturing inscription")]
[Clique sur les trois points (menu) du workflow]
[Sélectionne "Export" ou "Download"]

L'export génère un fichier JSON. Ce fichier contient tout : le trigger, les actions, les conditions, les délais, le mapping des champs.

[Montre le fichier JSON téléchargé]
[Ouvre brièvement le fichier dans un éditeur — montre la structure]

Tu n'as pas besoin de comprendre le JSON. C'est un fichier de sauvegarde que tu peux réimporter.

**[ÉCRAN — slide "Que contient le fichier JSON ?"]**

Le fichier d'export contient :

- La structure du workflow (ordre des blocs)
- La configuration de chaque bloc (app, événement, champs)
- Les conditions, filtres, branches
- Les délais

Ce qu'il ne contient PAS :

- Les identifiants de connexion (tokens, mots de passe)
- Les données réelles (emails, noms)
- L'historique d'exécution

C'est normal et c'est sécurisé. Après l'import, tu devras reconnecter tes apps.

**[ÉCRAN — screencast OttoKit — import d'un workflow]**

[Retourne sur le dashboard]
[Clique sur "Import Workflow" ou "Upload"]
[Sélectionne le fichier JSON exporté]

[Montre le workflow importé qui apparaît dans la liste]

Le workflow est importé avec toute sa structure. Mais il est en mode inactif — il ne se déclenche pas.

[Ouvre le workflow importé]
[Montre les blocs avec des icônes d'alerte sur les connexions]

Tu vois des alertes sur certains blocs. C'est parce que les connexions ne sont pas encore configurées. Il faut associer chaque app à une connexion existante sur ce compte.

**[ÉCRAN — screencast OttoKit — reconfiguration des connexions]**

[Clique sur le bloc trigger]
[Sélectionne la connexion WordPress locale dans le dropdown]
[Clique sur le bloc action Google Sheets]
[Sélectionne la connexion Google existante]

Tu reconfigures chaque connexion une par une. Ça prend 2-3 minutes. Ensuite, fais un Fetch Data sur le trigger pour vérifier que tout est en ordre.

[Fait un Fetch Data sur le trigger — données chargées]

C'est bon. Le workflow est prêt à être testé et activé.

**[ÉCRAN — slide "Cas d'usage de l'export/import"]**

| Situation | Action |
|---|---|
| Déployer un workflow sur le site d'un client | Export → envoyer le JSON → import chez le client |
| Sauvegarder avant modification | Export → garder le fichier comme backup |
| Partager un template avec ta communauté | Export → mettre le fichier en téléchargement |
| Migrer d'un compte OttoKit à un autre | Export tous les workflows → import sur le nouveau compte |

**[TRANSITION — face caméra]**

L'export/import fonctionne avec des fichiers. Mais OttoKit propose aussi une méthode plus directe : le partage par URL. On voit ça tout de suite.

---

**Points clés**
- L'export génère un fichier JSON contenant toute la structure du workflow
- Les identifiants et données réelles ne sont pas exportés (sécurité)
- Après import, reconnecter les apps et faire un Fetch Data
- Le workflow importé est inactif par défaut — tester avant d'activer

**Mots-clés SEO**
- OttoKit export workflow
- importer workflow OttoKit
- JSON export OttoKit
- transférer workflow automatisation WordPress

---

## Leçon 7.7 — Partager un workflow par URL

**Durée** : 5 min
**Type** : Vidéo HeyGen
**Écran** : Face caméra pour intro/conclusion, screencast OttoKit

---

**[INTRO — face caméra]**

Tu veux partager un workflow avec un collègue, un client, ou ta communauté. Plutôt que d'envoyer un fichier JSON, OttoKit te permet de générer un lien de partage. La personne clique, et le workflow est importé dans son compte.

**[ÉCRAN — screencast OttoKit — génération du lien de partage]**

[Ouvre un workflow existant]
[Clique sur les trois points (menu) ou le bouton de partage]
[Sélectionne "Share" ou "Share Link"]

OttoKit génère une URL unique pour ce workflow.

[Montre l'URL générée]
[Copie l'URL]

Cette URL est publique. N'importe qui avec le lien peut importer ce workflow dans son propre compte OttoKit. Attention : les connexions ne sont pas partagées. Le destinataire devra configurer ses propres apps.

**[ÉCRAN — screencast OttoKit — vue du destinataire]**

[Ouvre le lien dans un navigateur en mode privé (simuler un autre utilisateur)]
[Montre la page d'import : aperçu du workflow, bouton "Import"]
[Clique sur "Import"]
[Montre le workflow importé dans le compte]

Le destinataire voit un aperçu du workflow : les étapes, les apps utilisées. Il clique sur "Import" et le workflow est copié dans son compte. Comme avec l'import JSON, il devra reconnecter ses apps.

**[ÉCRAN — slide "URL de partage vs export JSON"]**

| | URL de partage | Export JSON |
|---|---|---|
| Envoi | Lien à copier-coller | Fichier à télécharger et envoyer |
| Accès | N'importe qui avec le lien | Seulement qui a le fichier |
| Mise à jour | Le lien pointe vers la version au moment du partage | Le fichier est figé |
| Idéal pour | Communauté, formations, collègues | Backup, migration, déploiement client |

**[ÉCRAN — slide "Cas d'usage pour schoolsWP"]**

Chez schoolsWP, on utilise le partage par URL pour :

- Partager des workflows "modèles" avec les apprenants de la formation
- Donner un workflow pré-configuré à un client freelance
- Publier un workflow dans un article de blog comme ressource gratuite

Par exemple, à la fin de cette formation, tu trouveras des liens vers des workflows OttoKit prêts à importer. Tu cliques, tu importes, tu configures tes apps, et ça tourne.

**[ÉCRAN — slide "Précautions"]**

- L'URL est publique — ne partage pas un workflow contenant des infos sensibles dans sa configuration
- Le workflow partagé est une copie — les modifications sur l'original ne se propagent pas
- Désactive le lien si tu ne veux plus que d'autres personnes importent le workflow
- Vérifie toujours les permissions des apps après import

**[TRANSITION — face caméra]**

Tu sais maintenant construire des workflows structurés, les dupliquer, les boucler, les parser, les exporter et les partager. Le Module 7 est terminé. Place au quiz pour valider tout ça.

---

**Points clés**
- OttoKit permet de partager un workflow via une URL publique
- Le destinataire importe le workflow dans son compte en un clic
- Les connexions ne sont pas partagées — chacun configure ses propres apps
- URL pour le partage rapide, JSON pour le backup et la migration

**Mots-clés SEO**
- OttoKit partager workflow
- lien partage workflow OttoKit
- template workflow OttoKit communauté
- partager automatisation WordPress

---

## Notes de production — Module 7

### Captures à préparer
- Feuille papier / tableau blanc avec diagramme workflow nurturing (leçon 7.1)
- Slide 3 patterns : linéaire (A→B→C), conditionnel (A→si X alors B sinon C), parallèle (A→B+C+D)
- Canvas OttoKit : clic droit sur un bloc → menu "Duplicate"
- Canvas OttoKit : deux workflows ouverts côte à côté (onglets navigateur)
- Dashboard OttoKit : menu workflow → "Duplicate"
- Canvas OttoKit : Loop avec Google Sheets "Get Rows" → bloc Loop → action "Send Email"
- Historique Loop : 3 itérations successives avec détails
- Email brut (notification commande) dans un client email
- Canvas OttoKit : Email Parser avec règles d'extraction configurées
- Données parsées dans le panneau de résultats
- Dashboard OttoKit : menu workflow → "Export" → fichier JSON téléchargé
- Fichier JSON ouvert dans un éditeur (structure visible)
- Dashboard OttoKit : bouton "Import Workflow" → sélection du fichier
- Workflow importé avec alertes sur les connexions
- OttoKit : bouton "Share" → URL générée
- Vue destinataire : page d'aperçu du workflow avec bouton "Import"

### Environnement de démo
- Compte OttoKit (plan premium recommandé pour les loops et multi-étapes)
- Site WordPress schoolsWP avec WooCommerce et TutorLMS
- Google Sheets avec une feuille "Participants" (colonnes : Nom, Email, Cours, 3 lignes de données)
- Boîte email avec des emails de notification (commande WooCommerce ou équivalent)
- Un second compte OttoKit ou un navigateur en mode privé (pour simuler le destinataire du partage)
- Papier et stylo ou tableau blanc (pour la leçon 7.1)
- 3 workflows existants représentant les 3 patterns (leçon 7.2)

### Durée estimée par leçon (hors quiz)
| Leçon | Durée vidéo |
|-------|-------------|
| 7.1 | 6 min |
| 7.2 | 6 min |
| 7.3 | 5 min |
| 7.4 | 7 min |
| 7.5 | 7 min |
| 7.6 | 5 min |
| 7.7 | 5 min |
| **Total M7** | **41 min** |
