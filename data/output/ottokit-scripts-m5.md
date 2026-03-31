# Scripts video — Module 5 : Data mapping et formatters : manipuler tes donnees

**Formation** : Maitriser OttoKit
**Module** : M5 — Data mapping et formatters : manipuler tes donnees
**Lecons** : 7 videos + 1 quiz
**Duree totale** : ~39 min de video
**Date** : 2026-03-30

---

## Lecon 5.1 — Data mapping : passer des donnees d'une etape a l'autre

**Duree** : 6 min
**Type** : Video HeyGen
**Ecran** : Face camera pour intro/conclusion, screencast OttoKit canvas

---

**[INTRO — face camera]**

Tu sais configurer des triggers et des actions. Mais la vraie puissance d'OttoKit, c'est ce qui se passe entre les deux : le data mapping. C'est la capacite a prendre une donnee d'une etape et a l'utiliser dans une autre.

**[ECRAN — slide "Qu'est-ce que le data mapping ?"]**

Le data mapping, c'est le transfert de donnees d'une etape a une autre dans un workflow.

Exemple concret :
- Le trigger detecte une nouvelle commande WooCommerce
- L'action Gmail utilise le champ `billing_email` du trigger comme destinataire
- L'action Google Sheets utilise le champ `total` du trigger comme montant

Ce transfert ne se fait pas tout seul. C'est toi qui decides quel champ va ou. C'est ca, le mapping.

**[ECRAN — screencast OttoKit canvas]**

[Ouvre un workflow avec un trigger WooCommerce et une action Gmail]
[Clique sur l'action Gmail]
[Clique dans le champ "To"]

Quand tu cliques dans un champ d'action, tu as deux options : taper un texte fixe ou inserer une donnee dynamique.

**[ECRAN — screencast selecteur de donnees dynamiques]**

[Montre le selecteur de donnees — icone ou bouton a cote du champ]
[Clique dessus]
[Montre la liste des champs disponibles, organises par etape : "Trigger — WooCommerce Order Created" avec tous les champs]

Le selecteur affiche tous les champs disponibles. Ils sont organises par etape. Ici, tu vois les champs du trigger : `billing_email`, `billing_first_name`, `total`, `order_id`...

[Selectionne "billing_email"]
[Le token s'insere dans le champ "To"]

Tu cliques sur le champ, et le token s'insere. Ce token sera remplace par la valeur reelle a chaque execution.

**[ECRAN — screencast mapping avec plusieurs etapes]**

[Montre un workflow avec un trigger + action 1 (FluentCRM) + action 2 (Gmail)]
[Clique sur l'action 2 — Gmail]
[Montre le selecteur de donnees dynamiques]
[Montre que les champs disponibles viennent du trigger ET de l'action 1]

Quand tu as plusieurs etapes, le selecteur affiche les donnees de toutes les etapes precedentes. L'action 2 peut utiliser les donnees du trigger et de l'action 1. L'action 3 peut utiliser les donnees du trigger, de l'action 1 et de l'action 2.

[Selectionne un champ de l'action 1 — par exemple "contact_id" de FluentCRM]

Ici, on insere le `contact_id` genere par FluentCRM dans l'etape precedente. C'est une donnee qui n'existait pas avant l'action 1.

**[ECRAN — slide "La chaine de donnees"]**

```
Trigger (fournit les donnees initiales)
    ↓
Action 1 (utilise les donnees du trigger, produit de nouvelles donnees)
    ↓
Action 2 (utilise les donnees du trigger + action 1, produit de nouvelles donnees)
    ↓
Action 3 (utilise les donnees du trigger + action 1 + action 2)
```

Chaque etape enrichit le flux de donnees. C'est une chaine. Plus ton workflow avance, plus tu as de donnees disponibles.

**[ECRAN — slide "Regle d'or du mapping"]**

Toujours faire un Fetch Data avant de mapper. Si le trigger n'a pas de donnees chargees, le selecteur sera vide. Et tu ne sauras pas quels champs sont disponibles.

Si tu ajoutes une action et que le selecteur n'affiche rien :
1. Retourne au trigger
2. Fais un Fetch Data
3. Reviens a l'action — les champs apparaissent

**[TRANSITION — face camera]**

Le data mapping est le coeur d'OttoKit. Dans la prochaine lecon, on approfondit la difference entre donnees statiques et dynamiques, et comment les combiner.

---

**Points cles**
- Le data mapping transfere les donnees d'une etape a une autre
- Le selecteur de donnees dynamiques affiche les champs de toutes les etapes precedentes
- Chaque action enrichit le flux de donnees pour les actions suivantes
- Toujours faire un Fetch Data avant de configurer le mapping

**Mots-cles SEO**
- OttoKit data mapping
- donnees dynamiques OttoKit
- mapper champs OttoKit workflow
- transfert donnees entre etapes OttoKit

---

## Lecon 5.2 — Donnees statiques vs dynamiques

**Duree** : 5 min
**Type** : Video HeyGen
**Ecran** : Face camera pour intro/conclusion, screencast OttoKit canvas

---

**[INTRO — face camera]**

Dans chaque champ d'une action OttoKit, tu peux mettre deux types de contenu : du texte fixe que tu tapes toi-meme, ou des tokens qui s'adaptent a chaque execution. Savoir quand utiliser l'un ou l'autre, c'est ce qui rend tes workflows intelligents.

**[ECRAN — slide "Statique vs Dynamique"]**

| | Donnee statique | Donnee dynamique |
|---|---|---|
| Defini par | Toi, au moment de la configuration | Le trigger ou les actions precedentes |
| Change a chaque execution | Non | Oui |
| Exemple | "Bienvenue sur schoolsWP" | "{billing_first_name}" |
| Utilisation | Texte fixe, valeurs constantes | Donnees personnalisees par execution |

**[ECRAN — screencast OttoKit — action Gmail]**

[Ouvre un workflow avec une action "Send Email"]
[Clique dans le champ "Subject"]

Prenons le sujet d'un email. Tu veux ecrire : "Merci pour ta commande #12345, Jean".

[Tape "Merci pour ta commande #"]

"Merci pour ta commande #" — c'est du texte statique. Identique a chaque execution.

[Clique sur le selecteur dynamique et selectionne "order_id"]

Le numero de commande — c'est dynamique. Il change a chaque commande.

[Tape ", "]

La virgule et l'espace — statique.

[Selectionne "billing_first_name"]

Le prenom — dynamique.

[Le champ affiche maintenant : "Merci pour ta commande #{order_id}, {billing_first_name}"]

Le resultat combine les deux. A l'execution, OttoKit remplacera les tokens par les valeurs reelles : "Merci pour ta commande #12345, Jean".

**[ECRAN — screencast OttoKit — corps de l'email]**

[Clique dans le champ "Body"]
[Montre un email qui combine texte statique et dynamique :]

```
Bonjour {first_name},

Ta commande #{order_id} d'un montant de {total} EUR a ete confirmee.

Recapitulatif :
- Produit : {product_name}
- Montant : {total} EUR
- Livraison estimee : sous 48h

Merci de ta confiance,
L'equipe schoolsWP
```

[Pointe les parties statiques (texte fixe) et dynamiques (tokens entre accolades)]

Dans le corps du message, le melange est encore plus visible. Le texte structurel est statique : "Bonjour", "Ta commande", "Merci de ta confiance". Les donnees personnalisees sont dynamiques : prenom, numero de commande, montant, produit.

**[ECRAN — slide "Quand utiliser quoi ?"]**

**Utilise du statique quand :**
- Le contenu ne change jamais (nom de ta marque, URL de ton site, signature)
- Tu veux un texte de remplissage ("Non specifie", "A completer")
- Tu definis une valeur fixe (statut "Draft", categorie "Blog")

**Utilise du dynamique quand :**
- Le contenu depend de l'evenement (prenom, email, montant, date)
- Le contenu vient du trigger ou d'une action precedente
- Tu veux personnaliser chaque execution

**[ECRAN — slide "Piege courant"]**

Attention : si un token dynamique est vide (le champ n'existe pas ou n'a pas de valeur), OttoKit insere une chaine vide. Tu peux te retrouver avec "Bonjour , ta commande..." au lieu de "Bonjour Jean, ta commande...".

La solution ? Gerer les donnees manquantes. On verra comment dans la lecon 5.7 sur les valeurs par defaut.

**[TRANSITION — face camera]**

Tu maitrises maintenant la difference entre statique et dynamique. Dans les prochaines lecons, on passe aux formatters : des outils pour transformer les donnees avant de les utiliser.

---

**Points cles**
- Statique = texte fixe, identique a chaque execution
- Dynamique = token remplace par une valeur reelle a chaque execution
- On peut combiner les deux dans un meme champ
- Un token vide genere une chaine vide — prevoir un fallback

**Mots-cles SEO**
- OttoKit donnees statiques dynamiques
- tokens dynamiques OttoKit
- personnaliser workflow OttoKit
- champs dynamiques automatisation WordPress

---

## Lecon 5.3 — Formatter date et heure : affiche les dates en francais

**Duree** : 6 min
**Type** : Video HeyGen
**Ecran** : Face camera pour intro/conclusion, screencast OttoKit canvas

---

**[INTRO — face camera]**

Ton trigger envoie "March 30, 2026" et tu veux afficher "30/03/2026" dans ton email. C'est le travail du formatter date. Il transforme les dates dans le format que tu veux, sans toucher aux donnees source.

**[ECRAN — slide "Le probleme"]**

Les apps envoient les dates dans leur propre format :

- WooCommerce : `2026-03-30T14:30:00`
- Google Sheets : `3/30/2026`
- WordPress : `March 30, 2026`

Tes clients francais s'attendent a lire : `30/03/2026` ou `30 mars 2026`.

Le formatter date fait la conversion automatiquement.

**[ECRAN — screencast OttoKit canvas]**

[Ouvre un workflow existant]
[Clique sur "+" pour ajouter une etape]
[Tape "Formatter" dans la barre de recherche des apps]
[Selectionne "Formatter" ou "Data Formatter"]

Le formatter est une app interne a OttoKit. Tu l'ajoutes comme une etape dans ton workflow, entre le trigger et l'action.

**[ECRAN — screencast selection du type de formatter]**

[Selectionne le type "Date / Time" ou "Format Date"]

On choisit le type "Date / Time". C'est celui qui gere les dates et les heures.

**[ECRAN — screencast configuration]**

[Dans le champ "Input Date", selectionne un champ date du trigger — par exemple "order_date" de WooCommerce]

Le champ d'entree, c'est la date brute qui vient du trigger. Ici, la date de commande WooCommerce.

[Dans le champ "Input Format" ou "From Format", selectionne ou tape le format d'entree : "YYYY-MM-DDTHH:mm:ss"]

Le format d'entree — comment la date arrive. OttoKit a souvent besoin de le savoir pour parser correctement.

[Dans le champ "Output Format" ou "To Format", tape ou selectionne : "DD/MM/YYYY"]

Le format de sortie — comment tu veux que la date soit affichee. `DD/MM/YYYY` pour le format francais classique.

**[ECRAN — screencast fuseau horaire]**

[Montre le champ "Timezone" ou "Output Timezone"]
[Selectionne "Europe/Paris"]

Le fuseau horaire. OttoKit recoit souvent les dates en UTC. Si tu ne changes pas, 14h UTC sera affiche comme 14h au lieu de 15h (heure de Paris en ete) ou 16h (heure d'ete). Selectionne "Europe/Paris" pour que l'heure corresponde a la France.

**[ECRAN — screencast test du formatter]**

[Clique sur "Test Step"]
[Montre l'entree : "2026-03-30T14:30:00"]
[Montre la sortie : "30/03/2026"]

Le test confirme la conversion. L'entree brute `2026-03-30T14:30:00` devient `30/03/2026`. C'est cette valeur que tu utiliseras dans tes actions.

**[ECRAN — slide "Formats courants"]**

| Format | Resultat | Usage |
|---|---|---|
| `DD/MM/YYYY` | 30/03/2026 | Date francaise classique |
| `DD MMMM YYYY` | 30 mars 2026 | Date en toutes lettres |
| `DD/MM/YYYY HH:mm` | 30/03/2026 15:30 | Date + heure |
| `dddd DD MMMM` | lundi 30 mars | Jour de la semaine + date |
| `YYYY-MM-DD` | 2026-03-30 | Format technique (tri, export) |

**[ECRAN — screencast utilisation dans une action]**

[Ajoute une action Gmail apres le formatter]
[Dans le corps de l'email, selectionne la sortie du formatter au lieu de la date brute du trigger]

Dans ton action email, tu n'utilises plus la date brute du trigger. Tu utilises la sortie du formatter. Ton email affichera "30/03/2026" au lieu de "2026-03-30T14:30:00".

[Clique sur "Save"]

**[TRANSITION — face camera]**

Les dates sont gerees. Dans la prochaine lecon, on passe aux formatters nombre pour arrondir, calculer et formater des prix.

---

**Points cles**
- Le formatter date convertit les dates d'un format a un autre
- Toujours definir le fuseau horaire (defaut = UTC)
- Le formatter est une etape du workflow, placee entre le trigger et l'action
- Utiliser la sortie du formatter dans les actions, pas la date brute du trigger

**Mots-cles SEO**
- OttoKit formatter date
- formater date francais OttoKit
- convertir date automatisation WordPress
- fuseau horaire OttoKit UTC

---

## Lecon 5.4 — Formatter nombre : arrondir, calculer, formater des prix

**Duree** : 6 min
**Type** : Video HeyGen
**Ecran** : Face camera pour intro/conclusion, screencast OttoKit canvas

---

**[INTRO — face camera]**

Tu recois un montant "49.99" depuis WooCommerce et tu veux calculer le prix TTC avec la TVA a 20%. Ou tu veux afficher "50 EUR" au lieu de "49.990000". Le formatter nombre gere tout ca.

**[ECRAN — slide "Cas d'usage concrets"]**

- Arrondir un prix : `49.9876` → `49.99`
- Calculer la TVA : `prix HT × 1.20` → prix TTC
- Formater un prix : `49.99` → `49,99 EUR`
- Appliquer une remise : `prix × 0.80` → prix avec 20% de reduction
- Convertir : `100` centimes → `1.00` euro

**[ECRAN — screencast OttoKit canvas]**

[Ouvre un workflow avec un trigger WooCommerce]
[Ajoute une etape "Formatter"]
[Selectionne le type "Number" ou "Format Number"]

On ajoute un formatter nombre. Le type est "Number" ou "Math" selon l'operation.

**[ECRAN — screencast operation mathematique — calcul TTC]**

[Selectionne l'operation "Math" ou "Perform Math Operation"]
[Dans le premier champ, selectionne "total" du trigger WooCommerce — valeur exemple : 83.33]
[Selectionne l'operateur "Multiply" ou "×"]
[Dans le second champ, tape "1.20"]

On va calculer le prix TTC. Le montant HT vient du trigger : 83,33 EUR. On multiplie par 1,20 pour ajouter la TVA a 20%.

[Clique sur "Test Step"]
[Montre le resultat : 99.996]

Le resultat brut est 99,996. Pas tres propre pour un prix. On va ajouter un arrondi.

**[ECRAN — screencast arrondi]**

[Ajoute une autre etape formatter ou modifie la configuration pour inclure un arrondi]
[Selectionne l'operation "Round" ou "Round Number"]
[Selectionne le nombre de decimales : 2]
[Teste : 99.996 → 99.99 ou 100.00 selon la methode d'arrondi]

L'arrondi a 2 decimales transforme 99,996 en 100,00. Parfait pour un prix.

**[ECRAN — screencast formatage avec devise]**

[Si disponible, montre l'option de formatage avec symbole monetaire]
[Configure : 2 decimales, separateur virgule, symbole "EUR" ou " EUR"]
[Teste : 100 → "100,00 EUR"]

Certaines versions du formatter permettent d'ajouter un symbole monetaire. Sinon, tu combines le resultat du formatter avec du texte statique dans ton action : `{montant_formate} EUR`.

**[ECRAN — slide "Calculer une remise — cas schoolsWP"]**

Scenario : tu vends une formation a 197 EUR et tu offres 30% de reduction aux abonnes newsletter.

```
Prix de base : 197 EUR (statique)
Coefficient reduction : 0.70 (statique — 100% - 30%)
Prix reduit : 197 × 0.70 = 137.90 EUR
```

[Montre la configuration dans OttoKit : premier champ = 197, operateur = multiply, second champ = 0.70]
[Teste : 137.90]

Le prix reduit est calcule automatiquement. Tu peux l'inserer dans un email promotionnel ou un coupon WooCommerce.

**[ECRAN — slide "Operations disponibles"]**

| Operation | Symbole | Exemple |
|---|---|---|
| Addition | + | prix + frais de port |
| Soustraction | - | prix - remise |
| Multiplication | × | prix HT × 1.20 (TVA) |
| Division | ÷ | montant total ÷ nombre d'articles |
| Arrondi | round | 49.996 → 50.00 |
| Valeur absolue | abs | -15 → 15 |

**[TRANSITION — face camera]**

Les nombres sont maitrises. Prochaine etape : le formatter texte pour extraire, transformer et nettoyer des chaines de caracteres.

---

**Points cles**
- Le formatter nombre gere les calculs, arrondis et formatages
- Multiplier par 1.20 pour ajouter 20% de TVA
- Toujours arrondir a 2 decimales pour les prix
- Combiner la sortie du formatter avec du texte statique pour le symbole monetaire

**Mots-cles SEO**
- OttoKit formatter nombre
- calculer prix automatiquement OttoKit
- TVA automatique WordPress
- OttoKit math operation

---

## Lecon 5.5 — Formatter texte : extraire, concatener, transformer

**Duree** : 6 min
**Type** : Video HeyGen
**Ecran** : Face camera pour intro/conclusion, screencast OttoKit canvas

---

**[INTRO — face camera]**

Tu recois "Jean DUPONT" dans un seul champ, mais tu veux seulement le prenom pour personnaliser un email. Ou tu recois "   jean.dupont@gmail.com   " avec des espaces en trop. Le formatter texte resout ces problemes.

**[ECRAN — slide "Operations texte courantes"]**

- **Extraire** : prendre une partie d'un texte ("Jean DUPONT" → "Jean")
- **Concatener** : assembler plusieurs textes ("Jean" + " " + "DUPONT" → "Jean DUPONT")
- **Majuscule/Minuscule** : transformer la casse ("jean dupont" → "Jean Dupont")
- **Trim** : supprimer les espaces en trop ("  texte  " → "texte")
- **Remplacer** : changer un mot ou un caractere ("lms wordpress" → "LMS WordPress")

**[ECRAN — screencast OttoKit canvas]**

[Ouvre un workflow]
[Ajoute une etape "Formatter"]
[Selectionne le type "Text" ou "Format Text"]

On ajoute un formatter texte. Premiere operation : extraire le prenom d'un champ "Nom complet".

**[ECRAN — screencast extraction du prenom]**

[Selectionne l'operation "Split Text" ou "Extract"]
[Dans le champ d'entree, selectionne "display_name" ou "billing_full_name" du trigger — valeur : "Jean DUPONT"]
[Configure le separateur : espace " "]
[Selectionne "First segment" ou index 0]
[Teste : "Jean DUPONT" → "Jean"]

On decoupe le texte au niveau de l'espace. Le premier segment, c'est le prenom. "Jean DUPONT" devient "Jean".

**[ECRAN — screencast transformation de casse]**

[Ajoute un autre formatter ou modifie l'operation]
[Selectionne "Capitalize" ou "Title Case"]
[Champ d'entree : "jean dupont"]
[Teste : "jean dupont" → "Jean Dupont"]

La transformation "Title Case" met la premiere lettre de chaque mot en majuscule. Utile quand les donnees arrivent en minuscules.

[Montre aussi "Uppercase" : "jean" → "JEAN"]
[Et "Lowercase" : "JEAN" → "jean"]

**[ECRAN — screencast trim — supprimer les espaces]**

[Selectionne l'operation "Trim"]
[Champ d'entree : "   jean@email.com   " — valeur avec espaces avant et apres]
[Teste : "jean@email.com" — espaces supprimes]

Le trim supprime les espaces au debut et a la fin d'un texte. C'est important pour les adresses email : un espace invisible peut faire echouer un envoi.

**[ECRAN — screencast concatenation]**

[Selectionne l'operation "Concatenate" ou "Combine Text"]
[Premier champ : "Bonjour " (texte statique)]
[Deuxieme champ : selecteur dynamique → "first_name"]
[Troisieme champ : ", bienvenue sur schoolsWP !" (texte statique)]
[Teste : "Bonjour Jean, bienvenue sur schoolsWP !"]

La concatenation assemble plusieurs morceaux de texte en un seul. Ici, on construit une phrase de bienvenue complete.

**[ECRAN — screencast remplacement]**

[Selectionne l'operation "Replace" ou "Find and Replace"]
[Champ d'entree : "Commande en cours de traitement"]
[Chercher : "en cours de traitement"]
[Remplacer par : "confirmee"]
[Teste : "Commande confirmee"]

Le remplacement cherche un texte et le remplace par un autre. Utile pour adapter des messages generiques a ton contexte.

**[ECRAN — slide "Recapitulatif des operations"]**

| Operation | Entree | Sortie |
|---|---|---|
| Split + index 0 | "Jean DUPONT" | "Jean" |
| Title Case | "jean dupont" | "Jean Dupont" |
| Trim | "  email@test.com  " | "email@test.com" |
| Concatenate | "Bonjour " + "Jean" | "Bonjour Jean" |
| Replace | "en cours" → "confirme" | "Commande confirmee" |
| Lowercase | "URGENT" | "urgent" |

**[TRANSITION — face camera]**

Tu maitrises maintenant les trois formatters principaux : date, nombre et texte. Dans la prochaine lecon, on decouvre un formatter un peu special : le generateur de nombres aleatoires.

---

**Points cles**
- Split extrait une partie d'un texte en le decoupant avec un separateur
- Title Case, Uppercase, Lowercase transforment la casse
- Trim supprime les espaces invisibles (important pour les emails)
- Concatenate assemble plusieurs textes en un seul
- Replace cherche et remplace un mot ou une expression

**Mots-cles SEO**
- OttoKit formatter texte
- extraire prenom OttoKit
- transformer texte automatisation WordPress
- OttoKit text operations

---

## Lecon 5.6 — Generer un nombre aleatoire

**Duree** : 4 min
**Type** : Video HeyGen
**Ecran** : Face camera pour intro/conclusion, screencast OttoKit canvas

---

**[INTRO — face camera]**

Parfois tu as besoin d'un nombre unique : un code promo, un identifiant temporaire, un numero de ticket. Le formatter "Random Number" genere un nombre aleatoire a chaque execution.

**[ECRAN — slide "Cas d'usage"]**

- **Code promo unique** : generer "PROMO-8347" pour chaque client
- **Identifiant de ticket** : "TICKET-29481" pour un systeme de support
- **Code de verification** : un code a 6 chiffres pour valider une action
- **Variation A/B** : un nombre entre 1 et 2 pour diriger vers la version A ou B

**[ECRAN — screencast OttoKit canvas]**

[Ouvre un workflow]
[Ajoute une etape "Formatter"]
[Selectionne le type "Number" ou "Random Number"]
[Selectionne l'operation "Generate Random Number"]

On ajoute un formatter de type nombre aleatoire.

**[ECRAN — screencast configuration]**

[Configure la plage : minimum = 1000, maximum = 9999]
[Teste : resultat = 7283 (exemple)]

On definit la plage. Ici, entre 1000 et 9999. A chaque execution, OttoKit genere un nombre different dans cette plage.

[Teste a nouveau : resultat = 4156 (exemple different)]

Chaque test donne un resultat different. C'est bien aleatoire.

**[ECRAN — screencast construction d'un code promo]**

[Ajoute une action apres le formatter]
[Dans un champ texte, tape "SCHOOL-" (texte statique)]
[Insere le resultat du formatter (nombre aleatoire)]
[Le champ affiche : "SCHOOL-{random_number}"]

Pour construire un code promo, on combine du texte statique avec le nombre aleatoire. "SCHOOL-" + 7283 = "SCHOOL-7283". Chaque client recoit un code unique.

**[ECRAN — slide "Limites a connaitre"]**

Deux limites :

1. **Pas garanti unique** — sur une grande plage (1000-9999), la probabilite de doublon est faible mais non nulle. Pour un vrai systeme d'identifiants uniques, utilise un champ auto-incremente dans ta base de donnees.

2. **Entiers uniquement** — le resultat est un nombre entier. Pas de decimales.

Pour reduire les doublons, augmente la plage : 100000 a 999999 donne 900 000 possibilites.

**[TRANSITION — face camera]**

Les nombres aleatoires sont un outil pratique pour les codes et identifiants. Derniere lecon avant le quiz : comment gerer les cas ou une donnee est manquante ou vide.

---

**Points cles**
- Le formatter genere un nombre aleatoire dans une plage definie
- Combiner avec du texte statique pour creer des codes ("PROMO-8347")
- Le resultat n'est pas garanti unique — augmenter la plage pour reduire les doublons
- Utilisation principale : codes promo, identifiants, numeros de ticket

**Mots-cles SEO**
- OttoKit nombre aleatoire
- generer code promo OttoKit
- random number automatisation WordPress
- identifiant unique OttoKit

---

## Lecon 5.7 — Gerer les donnees manquantes : valeurs par defaut et fallback

**Duree** : 6 min
**Type** : Video HeyGen
**Ecran** : Face camera pour intro/conclusion, screencast OttoKit canvas

---

**[INTRO — face camera]**

Un client passe commande sans renseigner son telephone. Un formulaire est soumis avec le champ "societe" vide. Un trigger envoie un prenom vide parce que le compte n'a pas ete rempli. Que se passe-t-il dans ton workflow ? Si tu n'as rien prevu, tu te retrouves avec des emails qui commencent par "Bonjour ," ou des lignes vides dans ton Google Sheet.

**[ECRAN — slide "Le probleme des champs vides"]**

Quand un champ dynamique est vide, OttoKit insere une chaine vide. Pas d'erreur, pas d'alerte. Le workflow continue normalement, mais avec des donnees incompletes.

Exemples :
- Email : "Bonjour , ta commande..." (prenom vide)
- Google Sheets : une colonne vide au milieu d'une ligne
- WordPress : un article cree avec un titre vide

**[ECRAN — screencast OttoKit canvas — methode 1 : texte par defaut dans le champ]**

[Ouvre un workflow avec une action Gmail]
[Clique dans le champ "Subject"]

La methode la plus simple : combiner un token dynamique avec un texte de remplacement directement dans le champ.

[Montre le champ sujet avec uniquement le token dynamique "first_name"]

Si `first_name` est vide, le sujet affichera juste "Bonjour ,". Pas ideal.

**[ECRAN — screencast OttoKit — ajout d'un formatter condition]**

[Ajoute une etape Formatter avant l'action email]
[Selectionne le type "Text" ou "Conditional"]
[Configure une condition : "Si {first_name} est vide, utiliser 'Ami(e) de schoolsWP'"]

La meilleure methode : utiliser un formatter ou un bloc conditionnel pour definir une valeur de remplacement.

Si le prenom existe → on l'utilise.
Si le prenom est vide → on affiche "Ami(e) de schoolsWP".

[Teste avec un prenom vide : resultat = "Ami(e) de schoolsWP"]
[Teste avec un prenom "Jean" : resultat = "Jean"]

**[ECRAN — screencast OttoKit — methode 2 : Filter App]**

[Montre une alternative : ajouter un Filter avant l'action]
[Configure le filtre : "first_name is not empty"]
[Si vrai → le workflow continue]
[Si faux → le workflow s'arrete]

Deuxieme approche : le Filter App. Au lieu de remplacer la valeur, tu bloques le workflow si la donnee manquante est critique. Par exemple, si l'email du client est vide, mieux vaut ne pas envoyer un email du tout.

**[ECRAN — slide "Quand utiliser quelle methode ?"]**

| Situation | Methode | Exemple |
|---|---|---|
| Champ optionnel (prenom, telephone) | Valeur par defaut | "Ami(e)" au lieu de vide |
| Champ critique (email) | Filter → stop | Ne pas envoyer sans adresse |
| Champ calculable (nom complet) | Formatter concatenation | Combiner prenom + nom avec un fallback |

**[ECRAN — screencast OttoKit — cas complet]**

[Montre un workflow complet :]
[Trigger → Formatter (fallback prenom) → Filter (email non vide) → Gmail → Sheets]

Voici un workflow robuste. Le formatter gere le fallback du prenom. Le filtre bloque si l'email est vide. L'email et le Sheet recoivent des donnees propres.

[Montre le canvas avec toutes les etapes visibles]

**[ECRAN — slide "Checklist anti-donnees manquantes"]**

Avant de publier un workflow :

1. Liste tous les champs dynamiques utilises
2. Pour chaque champ, demande-toi : "est-ce qu'il peut etre vide ?"
3. Si oui et optionnel → definis une valeur par defaut
4. Si oui et critique → ajoute un filtre qui bloque le workflow
5. Teste avec des donnees volontairement incompletes

**[TRANSITION — face camera]**

Tu sais maintenant gerer les donnees manquantes. Le Module 5 est termine. Passe au quiz pour valider tes acquis avant d'attaquer le Module 6 sur la logique conditionnelle.

---

**Points cles**
- Un champ vide ne provoque pas d'erreur — OttoKit insere une chaine vide
- Methode 1 : valeur par defaut via un formatter conditionnel
- Methode 2 : Filter App pour bloquer le workflow si une donnee critique manque
- Toujours tester avec des donnees volontairement incompletes avant de publier

**Mots-cles SEO**
- OttoKit donnees manquantes
- valeur par defaut OttoKit
- fallback workflow OttoKit
- gerer champs vides automatisation WordPress

---

## Notes de production — Module 5

### Captures a preparer
- Selecteur de donnees dynamiques dans un champ d'action — vue detaillee
- Selecteur montrant les champs de plusieurs etapes (trigger + action 1)
- Champ email avec melange texte statique et tokens dynamiques
- Formatter date : configuration input/output format + timezone
- Formatter nombre : operation multiplication (calcul TVA)
- Formatter texte : split, title case, trim, concatenate, replace
- Formatter nombre aleatoire : configuration plage min/max
- Construction d'un code promo "SCHOOL-{random}"
- Formatter conditionnel : configuration fallback prenom
- Filter App : condition "email is not empty"
- Workflow complet avec formatter + filter avant l'action email

### Environnement de demo
- Compte OttoKit (plan gratuit ou premium)
- Site WordPress schoolsWP avec :
  - WooCommerce installe (au moins 1 commande avec tous les champs remplis + 1 commande avec des champs vides)
  - Au moins 2 utilisateurs de test (un avec prenom, un sans)
- Google Sheet avec colonnes : Date, Client, Email, Montant
- Compte Gmail connecte a OttoKit
- Donnees de test avec des valeurs vides pour tester les fallbacks

### Duree estimee par lecon (hors quiz)
| Lecon | Duree video |
|-------|-------------|
| 5.1 | 6 min |
| 5.2 | 5 min |
| 5.3 | 6 min |
| 5.4 | 6 min |
| 5.5 | 6 min |
| 5.6 | 4 min |
| 5.7 | 6 min |
| **Total M5** | **39 min** |
