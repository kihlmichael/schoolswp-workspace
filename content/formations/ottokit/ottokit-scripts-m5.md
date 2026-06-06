# Scripts vidéo - Module 5 : Data mapping et formatters : manipuler tes données

**Formation** : Maîtriser OttoKit
**Module** : M5 - Data mapping et formatters : manipuler tes données
**Leçons** : 7 vidéos + 1 quiz
**Durée totale** : ~39 min de vidéo
**Date** : 2026-03-30

---

## Leçon 5.1 - Data mapping : passer des données d'une étape à l'autre

**Durée** : 6 min
**Type** : Vidéo HeyGen
**Écran** : Face caméra pour intro/conclusion, screencast OttoKit canvas

---

**[INTRO - face caméra]**

Tu sais configurer des triggers et des actions. Mais la vraie puissance d'OttoKit, c'est ce qui se passe entre les deux : le data mapping. C'est la capacité à prendre une donnée d'une étape et à l'utiliser dans une autre.

**[ÉCRAN - slide "Qu'est-ce que le data mapping ?"]**

Le data mapping, c'est le transfert de données d'une étape à une autre dans un workflow.

Exemple concret :
- Le trigger détecte une nouvelle commande WooCommerce
- L'action Gmail utilise le champ `billing_email` du trigger comme destinataire
- L'action Google Sheets utilise le champ `total` du trigger comme montant

Ce transfert ne se fait pas tout seul. C'est toi qui décides quel champ va où. C'est ça, le mapping.

**[ÉCRAN - screencast OttoKit canvas]**

[Ouvre un workflow avec un trigger WooCommerce et une action Gmail]
[Clique sur l'action Gmail]
[Clique dans le champ "To"]

Quand tu cliques dans un champ d'action, tu as deux options : taper un texte fixe ou insérer une donnée dynamique.

**[ÉCRAN - screencast sélecteur de données dynamiques]**

[Montre le sélecteur de données - icône ou bouton à côté du champ]
[Clique dessus]
[Montre la liste des champs disponibles, organisés par étape : "Trigger - WooCommerce Order Created" avec tous les champs]

Le sélecteur affiche tous les champs disponibles. Ils sont organisés par étape. Ici, tu vois les champs du trigger : `billing_email`, `billing_first_name`, `total`, `order_id`...

[Sélectionne "billing_email"]
[Le token s'insère dans le champ "To"]

Tu cliques sur le champ, et le token s'insère. Ce token sera remplacé par la valeur réelle à chaque exécution.

**[ÉCRAN - screencast mapping avec plusieurs étapes]**

[Montre un workflow avec un trigger + action 1 (FluentCRM) + action 2 (Gmail)]
[Clique sur l'action 2 - Gmail]
[Montre le sélecteur de données dynamiques]
[Montre que les champs disponibles viennent du trigger ET de l'action 1]

Quand tu as plusieurs étapes, le sélecteur affiche les données de toutes les étapes précédentes. L'action 2 peut utiliser les données du trigger et de l'action 1. L'action 3 peut utiliser les données du trigger, de l'action 1 et de l'action 2.

[Sélectionne un champ de l'action 1 - par exemple "contact_id" de FluentCRM]

Ici, on insère le `contact_id` généré par FluentCRM dans l'étape précédente. C'est une donnée qui n'existait pas avant l'action 1.

**[ÉCRAN - slide "La chaîne de données"]**

```
Trigger (fournit les données initiales)
    ↓
Action 1 (utilise les données du trigger, produit de nouvelles données)
    ↓
Action 2 (utilise les données du trigger + action 1, produit de nouvelles données)
    ↓
Action 3 (utilise les données du trigger + action 1 + action 2)
```

Chaque étape enrichit le flux de données. C'est une chaîne. Plus ton workflow avance, plus tu as de données disponibles.

**[ÉCRAN - slide "Règle d'or du mapping"]**

Toujours faire un Fetch Data avant de mapper. Si le trigger n'a pas de données chargées, le sélecteur sera vide. Et tu ne sauras pas quels champs sont disponibles.

Si tu ajoutes une action et que le sélecteur n'affiche rien :
1. Retourne au trigger
2. Fais un Fetch Data
3. Reviens à l'action - les champs apparaissent

**[TRANSITION - face caméra]**

Le data mapping est le cœur d'OttoKit. Dans la prochaine leçon, on approfondit la différence entre données statiques et dynamiques, et comment les combiner.

---

**Points clés**
- Le data mapping transfère les données d'une étape à une autre
- Le sélecteur de données dynamiques affiche les champs de toutes les étapes précédentes
- Chaque action enrichit le flux de données pour les actions suivantes
- Toujours faire un Fetch Data avant de configurer le mapping

**Mots-clés SEO**
- OttoKit data mapping
- données dynamiques OttoKit
- mapper champs OttoKit workflow
- transfert données entre étapes OttoKit

---

## Leçon 5.2 - Données statiques vs dynamiques

**Durée** : 5 min
**Type** : Vidéo HeyGen
**Écran** : Face caméra pour intro/conclusion, screencast OttoKit canvas

---

**[INTRO - face caméra]**

Dans chaque champ d'une action OttoKit, tu peux mettre deux types de contenu : du texte fixe que tu tapes toi-même, ou des tokens qui s'adaptent à chaque exécution. Savoir quand utiliser l'un ou l'autre, c'est ce qui rend tes workflows intelligents.

**[ÉCRAN - slide "Statique vs Dynamique"]**

| | Donnée statique | Donnée dynamique |
|---|---|---|
| Défini par | Toi, au moment de la configuration | Le trigger ou les actions précédentes |
| Change à chaque exécution | Non | Oui |
| Exemple | "Bienvenue sur schoolsWP" | "{billing_first_name}" |
| Utilisation | Texte fixe, valeurs constantes | Données personnalisées par exécution |

**[ÉCRAN - screencast OttoKit - action Gmail]**

[Ouvre un workflow avec une action "Send Email"]
[Clique dans le champ "Subject"]

Prenons le sujet d'un email. Tu veux écrire : "Merci pour ta commande #12345, Jean".

[Tape "Merci pour ta commande #"]

"Merci pour ta commande #" - c'est du texte statique. Identique à chaque exécution.

[Clique sur le sélecteur dynamique et sélectionne "order_id"]

Le numéro de commande - c'est dynamique. Il change à chaque commande.

[Tape ", "]

La virgule et l'espace - statique.

[Sélectionne "billing_first_name"]

Le prénom - dynamique.

[Le champ affiche maintenant : "Merci pour ta commande #{order_id}, {billing_first_name}"]

Le résultat combine les deux. À l'exécution, OttoKit remplacera les tokens par les valeurs réelles : "Merci pour ta commande #12345, Jean".

**[ÉCRAN - screencast OttoKit - corps de l'email]**

[Clique dans le champ "Body"]
[Montre un email qui combine texte statique et dynamique :]

```
Bonjour {first_name},

Ta commande #{order_id} d'un montant de {total} EUR a été confirmée.

Récapitulatif :
- Produit : {product_name}
- Montant : {total} EUR
- Livraison estimée : sous 48h

Merci de ta confiance,
L'équipe schoolsWP
```

[Pointe les parties statiques (texte fixe) et dynamiques (tokens entre accolades)]

Dans le corps du message, le mélange est encore plus visible. Le texte structurel est statique : "Bonjour", "Ta commande", "Merci de ta confiance". Les données personnalisées sont dynamiques : prénom, numéro de commande, montant, produit.

**[ÉCRAN - slide "Quand utiliser quoi ?"]**

**Utilise du statique quand :**
- Le contenu ne change jamais (nom de ta marque, URL de ton site, signature)
- Tu veux un texte de remplissage ("Non spécifié", "À compléter")
- Tu définis une valeur fixe (statut "Draft", catégorie "Blog")

**Utilise du dynamique quand :**
- Le contenu dépend de l'événement (prénom, email, montant, date)
- Le contenu vient du trigger ou d'une action précédente
- Tu veux personnaliser chaque exécution

**[ÉCRAN - slide "Piège courant"]**

Attention : si un token dynamique est vide (le champ n'existe pas ou n'a pas de valeur), OttoKit insère une chaîne vide. Tu peux te retrouver avec "Bonjour , ta commande..." au lieu de "Bonjour Jean, ta commande...".

La solution ? Gérer les données manquantes. On verra comment dans la leçon 5.7 sur les valeurs par défaut.

**[TRANSITION - face caméra]**

Tu maîtrises maintenant la différence entre statique et dynamique. Dans les prochaines leçons, on passe aux formatters : des outils pour transformer les données avant de les utiliser.

---

**Points clés**
- Statique = texte fixe, identique à chaque exécution
- Dynamique = token remplacé par une valeur réelle à chaque exécution
- On peut combiner les deux dans un même champ
- Un token vide génère une chaîne vide - prévoir un fallback

**Mots-clés SEO**
- OttoKit données statiques dynamiques
- tokens dynamiques OttoKit
- personnaliser workflow OttoKit
- champs dynamiques automatisation WordPress

---

## Leçon 5.3 - Formatter date et heure : affiche les dates en français

**Durée** : 6 min
**Type** : Vidéo HeyGen
**Écran** : Face caméra pour intro/conclusion, screencast OttoKit canvas

---

**[INTRO - face caméra]**

Ton trigger envoie "March 30, 2026" et tu veux afficher "30/03/2026" dans ton email. C'est le travail du formatter date. Il transforme les dates dans le format que tu veux, sans toucher aux données source.

**[ÉCRAN - slide "Le problème"]**

Les apps envoient les dates dans leur propre format :

- WooCommerce : `2026-03-30T14:30:00`
- Google Sheets : `3/30/2026`
- WordPress : `March 30, 2026`

Tes clients français s'attendent à lire : `30/03/2026` ou `30 mars 2026`.

Le formatter date fait la conversion automatiquement.

**[ÉCRAN - screencast OttoKit canvas]**

[Ouvre un workflow existant]
[Clique sur "+" pour ajouter une étape]
[Tape "Formatter" dans la barre de recherche des apps]
[Sélectionne "Formatter" ou "Data Formatter"]

Le formatter est une app interne à OttoKit. Tu l'ajoutes comme une étape dans ton workflow, entre le trigger et l'action.

**[ÉCRAN - screencast sélection du type de formatter]**

[Sélectionne le type "Date / Time" ou "Format Date"]

On choisit le type "Date / Time". C'est celui qui gère les dates et les heures.

**[ÉCRAN - screencast configuration]**

[Dans le champ "Input Date", sélectionne un champ date du trigger - par exemple "order_date" de WooCommerce]

Le champ d'entrée, c'est la date brute qui vient du trigger. Ici, la date de commande WooCommerce.

[Dans le champ "Input Format" ou "From Format", sélectionne ou tape le format d'entrée : "YYYY-MM-DDTHH:mm:ss"]

Le format d'entrée - comment la date arrive. OttoKit a souvent besoin de le savoir pour parser correctement.

[Dans le champ "Output Format" ou "To Format", tape ou sélectionne : "DD/MM/YYYY"]

Le format de sortie - comment tu veux que la date soit affichée. `DD/MM/YYYY` pour le format français classique.

**[ÉCRAN - screencast fuseau horaire]**

[Montre le champ "Timezone" ou "Output Timezone"]
[Sélectionne "Europe/Paris"]

Le fuseau horaire. OttoKit reçoit souvent les dates en UTC. Si tu ne changes pas, 14h UTC sera affiché comme 14h au lieu de 15h (heure de Paris en été) ou 16h (heure d'été). Sélectionne "Europe/Paris" pour que l'heure corresponde à la France.

**[ÉCRAN - screencast test du formatter]**

[Clique sur "Test Step"]
[Montre l'entrée : "2026-03-30T14:30:00"]
[Montre la sortie : "30/03/2026"]

Le test confirme la conversion. L'entrée brute `2026-03-30T14:30:00` devient `30/03/2026`. C'est cette valeur que tu utiliseras dans tes actions.

**[ÉCRAN - slide "Formats courants"]**

| Format | Résultat | Usage |
|---|---|---|
| `DD/MM/YYYY` | 30/03/2026 | Date française classique |
| `DD MMMM YYYY` | 30 mars 2026 | Date en toutes lettres |
| `DD/MM/YYYY HH:mm` | 30/03/2026 15:30 | Date + heure |
| `dddd DD MMMM` | lundi 30 mars | Jour de la semaine + date |
| `YYYY-MM-DD` | 2026-03-30 | Format technique (tri, export) |

**[ÉCRAN - screencast utilisation dans une action]**

[Ajoute une action Gmail après le formatter]
[Dans le corps de l'email, sélectionne la sortie du formatter au lieu de la date brute du trigger]

Dans ton action email, tu n'utilises plus la date brute du trigger. Tu utilises la sortie du formatter. Ton email affichera "30/03/2026" au lieu de "2026-03-30T14:30:00".

[Clique sur "Save"]

**[TRANSITION - face caméra]**

Les dates sont gérées. Dans la prochaine leçon, on passe aux formatters nombre pour arrondir, calculer et formater des prix.

---

**Points clés**
- Le formatter date convertit les dates d'un format à un autre
- Toujours définir le fuseau horaire (défaut = UTC)
- Le formatter est une étape du workflow, placée entre le trigger et l'action
- Utiliser la sortie du formatter dans les actions, pas la date brute du trigger

**Mots-clés SEO**
- OttoKit formatter date
- formater date français OttoKit
- convertir date automatisation WordPress
- fuseau horaire OttoKit UTC

---

## Leçon 5.4 - Formatter nombre : arrondir, calculer, formater des prix

**Durée** : 6 min
**Type** : Vidéo HeyGen
**Écran** : Face caméra pour intro/conclusion, screencast OttoKit canvas

---

**[INTRO - face caméra]**

Tu reçois un montant "49.99" depuis WooCommerce et tu veux calculer le prix TTC avec la TVA à 20%. Ou tu veux afficher "50 EUR" au lieu de "49.990000". Le formatter nombre gère tout ça.

**[ÉCRAN - slide "Cas d'usage concrets"]**

- Arrondir un prix : `49.9876` → `49.99`
- Calculer la TVA : `prix HT × 1.20` → prix TTC
- Formater un prix : `49.99` → `49,99 EUR`
- Appliquer une remise : `prix × 0.80` → prix avec 20% de réduction
- Convertir : `100` centimes → `1.00` euro

**[ÉCRAN - screencast OttoKit canvas]**

[Ouvre un workflow avec un trigger WooCommerce]
[Ajoute une étape "Formatter"]
[Sélectionne le type "Number" ou "Format Number"]

On ajoute un formatter nombre. Le type est "Number" ou "Math" selon l'opération.

**[ÉCRAN - screencast opération mathématique - calcul TTC]**

[Sélectionne l'opération "Math" ou "Perform Math Operation"]
[Dans le premier champ, sélectionne "total" du trigger WooCommerce - valeur exemple : 83.33]
[Sélectionne l'opérateur "Multiply" ou "×"]
[Dans le second champ, tape "1.20"]

On va calculer le prix TTC. Le montant HT vient du trigger : 83,33 EUR. On multiplie par 1,20 pour ajouter la TVA à 20%.

[Clique sur "Test Step"]
[Montre le résultat : 99.996]

Le résultat brut est 99,996. Pas très propre pour un prix. On va ajouter un arrondi.

**[ÉCRAN - screencast arrondi]**

[Ajoute une autre étape formatter ou modifie la configuration pour inclure un arrondi]
[Sélectionne l'opération "Round" ou "Round Number"]
[Sélectionne le nombre de décimales : 2]
[Teste : 99.996 → 99.99 ou 100.00 selon la méthode d'arrondi]

L'arrondi à 2 décimales transforme 99,996 en 100,00. Parfait pour un prix.

**[ÉCRAN - screencast formatage avec devise]**

[Si disponible, montre l'option de formatage avec symbole monétaire]
[Configure : 2 décimales, séparateur virgule, symbole "EUR" ou " EUR"]
[Teste : 100 → "100,00 EUR"]

Certaines versions du formatter permettent d'ajouter un symbole monétaire. Sinon, tu combines le résultat du formatter avec du texte statique dans ton action : `{montant_formate} EUR`.

**[ÉCRAN - slide "Calculer une remise - cas schoolsWP"]**

Scénario : tu vends une formation à 197 EUR et tu offres 30% de réduction aux abonnés newsletter.

```
Prix de base : 197 EUR (statique)
Coefficient réduction : 0.70 (statique - 100% - 30%)
Prix réduit : 197 × 0.70 = 137.90 EUR
```

[Montre la configuration dans OttoKit : premier champ = 197, opérateur = multiply, second champ = 0.70]
[Teste : 137.90]

Le prix réduit est calculé automatiquement. Tu peux l'insérer dans un email promotionnel ou un coupon WooCommerce.

**[ÉCRAN - slide "Opérations disponibles"]**

| Opération | Symbole | Exemple |
|---|---|---|
| Addition | + | prix + frais de port |
| Soustraction | - | prix - remise |
| Multiplication | × | prix HT × 1.20 (TVA) |
| Division | ÷ | montant total ÷ nombre d'articles |
| Arrondi | round | 49.996 → 50.00 |
| Valeur absolue | abs | -15 → 15 |

**[TRANSITION - face caméra]**

Les nombres sont maîtrisés. Prochaine étape : le formatter texte pour extraire, transformer et nettoyer des chaînes de caractères.

---

**Points clés**
- Le formatter nombre gère les calculs, arrondis et formatages
- Multiplier par 1.20 pour ajouter 20% de TVA
- Toujours arrondir à 2 décimales pour les prix
- Combiner la sortie du formatter avec du texte statique pour le symbole monétaire

**Mots-clés SEO**
- OttoKit formatter nombre
- calculer prix automatiquement OttoKit
- TVA automatique WordPress
- OttoKit math operation

---

## Leçon 5.5 - Formatter texte : extraire, concaténer, transformer

**Durée** : 6 min
**Type** : Vidéo HeyGen
**Écran** : Face caméra pour intro/conclusion, screencast OttoKit canvas

---

**[INTRO - face caméra]**

Tu reçois "Jean DUPONT" dans un seul champ, mais tu veux seulement le prénom pour personnaliser un email. Ou tu reçois "   jean.dupont@gmail.com   " avec des espaces en trop. Le formatter texte résout ces problèmes.

**[ÉCRAN - slide "Opérations texte courantes"]**

- **Extraire** : prendre une partie d'un texte ("Jean DUPONT" → "Jean")
- **Concaténer** : assembler plusieurs textes ("Jean" + " " + "DUPONT" → "Jean DUPONT")
- **Majuscule/Minuscule** : transformer la casse ("jean dupont" → "Jean Dupont")
- **Trim** : supprimer les espaces en trop ("  texte  " → "texte")
- **Remplacer** : changer un mot ou un caractère ("lms wordpress" → "LMS WordPress")

**[ÉCRAN - screencast OttoKit canvas]**

[Ouvre un workflow]
[Ajoute une étape "Formatter"]
[Sélectionne le type "Text" ou "Format Text"]

On ajoute un formatter texte. Première opération : extraire le prénom d'un champ "Nom complet".

**[ÉCRAN - screencast extraction du prénom]**

[Sélectionne l'opération "Split Text" ou "Extract"]
[Dans le champ d'entrée, sélectionne "display_name" ou "billing_full_name" du trigger - valeur : "Jean DUPONT"]
[Configure le séparateur : espace " "]
[Sélectionne "First segment" ou index 0]
[Teste : "Jean DUPONT" → "Jean"]

On découpe le texte au niveau de l'espace. Le premier segment, c'est le prénom. "Jean DUPONT" devient "Jean".

**[ÉCRAN - screencast transformation de casse]**

[Ajoute un autre formatter ou modifie l'opération]
[Sélectionne "Capitalize" ou "Title Case"]
[Champ d'entrée : "jean dupont"]
[Teste : "jean dupont" → "Jean Dupont"]

La transformation "Title Case" met la première lettre de chaque mot en majuscule. Utile quand les données arrivent en minuscules.

[Montre aussi "Uppercase" : "jean" → "JEAN"]
[Et "Lowercase" : "JEAN" → "jean"]

**[ÉCRAN - screencast trim - supprimer les espaces]**

[Sélectionne l'opération "Trim"]
[Champ d'entrée : "   jean@email.com   " - valeur avec espaces avant et après]
[Teste : "jean@email.com" - espaces supprimés]

Le trim supprime les espaces au début et à la fin d'un texte. C'est important pour les adresses email : un espace invisible peut faire échouer un envoi.

**[ÉCRAN - screencast concaténation]**

[Sélectionne l'opération "Concatenate" ou "Combine Text"]
[Premier champ : "Bonjour " (texte statique)]
[Deuxième champ : sélecteur dynamique → "first_name"]
[Troisième champ : ", bienvenue sur schoolsWP !" (texte statique)]
[Teste : "Bonjour Jean, bienvenue sur schoolsWP !"]

La concaténation assemble plusieurs morceaux de texte en un seul. Ici, on construit une phrase de bienvenue complète.

**[ÉCRAN - screencast remplacement]**

[Sélectionne l'opération "Replace" ou "Find and Replace"]
[Champ d'entrée : "Commande en cours de traitement"]
[Chercher : "en cours de traitement"]
[Remplacer par : "confirmée"]
[Teste : "Commande confirmée"]

Le remplacement cherche un texte et le remplace par un autre. Utile pour adapter des messages génériques à ton contexte.

**[ÉCRAN - slide "Récapitulatif des opérations"]**

| Opération | Entrée | Sortie |
|---|---|---|
| Split + index 0 | "Jean DUPONT" | "Jean" |
| Title Case | "jean dupont" | "Jean Dupont" |
| Trim | "  email@test.com  " | "email@test.com" |
| Concatenate | "Bonjour " + "Jean" | "Bonjour Jean" |
| Replace | "en cours" → "confirmé" | "Commande confirmée" |
| Lowercase | "URGENT" | "urgent" |

**[TRANSITION - face caméra]**

Tu maîtrises maintenant les trois formatters principaux : date, nombre et texte. Dans la prochaine leçon, on découvre un formatter un peu spécial : le générateur de nombres aléatoires.

---

**Points clés**
- Split extrait une partie d'un texte en le découpant avec un séparateur
- Title Case, Uppercase, Lowercase transforment la casse
- Trim supprime les espaces invisibles (important pour les emails)
- Concatenate assemble plusieurs textes en un seul
- Replace cherche et remplace un mot ou une expression

**Mots-clés SEO**
- OttoKit formatter texte
- extraire prénom OttoKit
- transformer texte automatisation WordPress
- OttoKit text operations

---

## Leçon 5.6 - Générer un nombre aléatoire

**Durée** : 4 min
**Type** : Vidéo HeyGen
**Écran** : Face caméra pour intro/conclusion, screencast OttoKit canvas

---

**[INTRO - face caméra]**

Parfois tu as besoin d'un nombre unique : un code promo, un identifiant temporaire, un numéro de ticket. Le formatter "Random Number" génère un nombre aléatoire à chaque exécution.

**[ÉCRAN - slide "Cas d'usage"]**

- **Code promo unique** : générer "PROMO-8347" pour chaque client
- **Identifiant de ticket** : "TICKET-29481" pour un système de support
- **Code de vérification** : un code à 6 chiffres pour valider une action
- **Variation A/B** : un nombre entre 1 et 2 pour diriger vers la version A ou B

**[ÉCRAN - screencast OttoKit canvas]**

[Ouvre un workflow]
[Ajoute une étape "Formatter"]
[Sélectionne le type "Number" ou "Random Number"]
[Sélectionne l'opération "Generate Random Number"]

On ajoute un formatter de type nombre aléatoire.

**[ÉCRAN - screencast configuration]**

[Configure la plage : minimum = 1000, maximum = 9999]
[Teste : résultat = 7283 (exemple)]

On définit la plage. Ici, entre 1000 et 9999. À chaque exécution, OttoKit génère un nombre différent dans cette plage.

[Teste à nouveau : résultat = 4156 (exemple différent)]

Chaque test donne un résultat différent. C'est bien aléatoire.

**[ÉCRAN - screencast construction d'un code promo]**

[Ajoute une action après le formatter]
[Dans un champ texte, tape "SCHOOL-" (texte statique)]
[Insère le résultat du formatter (nombre aléatoire)]
[Le champ affiche : "SCHOOL-{random_number}"]

Pour construire un code promo, on combine du texte statique avec le nombre aléatoire. "SCHOOL-" + 7283 = "SCHOOL-7283". Chaque client reçoit un code unique.

**[ÉCRAN - slide "Limites à connaître"]**

Deux limites :

1. **Pas garanti unique** - sur une grande plage (1000-9999), la probabilité de doublon est faible mais non nulle. Pour un vrai système d'identifiants uniques, utilise un champ auto-incrémenté dans ta base de données.

2. **Entiers uniquement** - le résultat est un nombre entier. Pas de décimales.

Pour réduire les doublons, augmente la plage : 100000 à 999999 donne 900 000 possibilités.

**[TRANSITION - face caméra]**

Les nombres aléatoires sont un outil pratique pour les codes et identifiants. Dernière leçon avant le quiz : comment gérer les cas où une donnée est manquante ou vide.

---

**Points clés**
- Le formatter génère un nombre aléatoire dans une plage définie
- Combiner avec du texte statique pour créer des codes ("PROMO-8347")
- Le résultat n'est pas garanti unique - augmenter la plage pour réduire les doublons
- Utilisation principale : codes promo, identifiants, numéros de ticket

**Mots-clés SEO**
- OttoKit nombre aléatoire
- générer code promo OttoKit
- random number automatisation WordPress
- identifiant unique OttoKit

---

## Leçon 5.7 - Gérer les données manquantes : valeurs par défaut et fallback

**Durée** : 6 min
**Type** : Vidéo HeyGen
**Écran** : Face caméra pour intro/conclusion, screencast OttoKit canvas

---

**[INTRO - face caméra]**

Un client passe commande sans renseigner son téléphone. Un formulaire est soumis avec le champ "société" vide. Un trigger envoie un prénom vide parce que le compte n'a pas été rempli. Que se passe-t-il dans ton workflow ? Si tu n'as rien prévu, tu te retrouves avec des emails qui commencent par "Bonjour ," ou des lignes vides dans ton Google Sheet.

**[ÉCRAN - slide "Le problème des champs vides"]**

Quand un champ dynamique est vide, OttoKit insère une chaîne vide. Pas d'erreur, pas d'alerte. Le workflow continue normalement, mais avec des données incomplètes.

Exemples :
- Email : "Bonjour , ta commande..." (prénom vide)
- Google Sheets : une colonne vide au milieu d'une ligne
- WordPress : un article créé avec un titre vide

**[ÉCRAN - screencast OttoKit canvas - méthode 1 : texte par défaut dans le champ]**

[Ouvre un workflow avec une action Gmail]
[Clique dans le champ "Subject"]

La méthode la plus simple : combiner un token dynamique avec un texte de remplacement directement dans le champ.

[Montre le champ sujet avec uniquement le token dynamique "first_name"]

Si `first_name` est vide, le sujet affichera juste "Bonjour ,". Pas idéal.

**[ÉCRAN - screencast OttoKit - ajout d'un formatter condition]**

[Ajoute une étape Formatter avant l'action email]
[Sélectionne le type "Text" ou "Conditional"]
[Configure une condition : "Si {first_name} est vide, utiliser 'Ami(e) de schoolsWP'"]

La meilleure méthode : utiliser un formatter ou un bloc conditionnel pour définir une valeur de remplacement.

Si le prénom existe → on l'utilise.
Si le prénom est vide → on affiche "Ami(e) de schoolsWP".

[Teste avec un prénom vide : résultat = "Ami(e) de schoolsWP"]
[Teste avec un prénom "Jean" : résultat = "Jean"]

**[ÉCRAN - screencast OttoKit - méthode 2 : Filter App]**

[Montre une alternative : ajouter un Filter avant l'action]
[Configure le filtre : "first_name is not empty"]
[Si vrai → le workflow continue]
[Si faux → le workflow s'arrête]

Deuxième approche : le Filter App. Au lieu de remplacer la valeur, tu bloques le workflow si la donnée manquante est critique. Par exemple, si l'email du client est vide, mieux vaut ne pas envoyer un email du tout.

**[ÉCRAN - slide "Quand utiliser quelle méthode ?"]**

| Situation | Méthode | Exemple |
|---|---|---|
| Champ optionnel (prénom, téléphone) | Valeur par défaut | "Ami(e)" au lieu de vide |
| Champ critique (email) | Filter → stop | Ne pas envoyer sans adresse |
| Champ calculable (nom complet) | Formatter concaténation | Combiner prénom + nom avec un fallback |

**[ÉCRAN - screencast OttoKit - cas complet]**

[Montre un workflow complet :]
[Trigger → Formatter (fallback prénom) → Filter (email non vide) → Gmail → Sheets]

Voici un workflow robuste. Le formatter gère le fallback du prénom. Le filtre bloque si l'email est vide. L'email et le Sheet reçoivent des données propres.

[Montre le canvas avec toutes les étapes visibles]

**[ÉCRAN - slide "Checklist anti-données manquantes"]**

Avant de publier un workflow :

1. Liste tous les champs dynamiques utilisés
2. Pour chaque champ, demande-toi : "est-ce qu'il peut être vide ?"
3. Si oui et optionnel → définis une valeur par défaut
4. Si oui et critique → ajoute un filtre qui bloque le workflow
5. Teste avec des données volontairement incomplètes

**[TRANSITION - face caméra]**

Tu sais maintenant gérer les données manquantes. Le Module 5 est terminé. Passe au quiz pour valider tes acquis avant d'attaquer le Module 6 sur la logique conditionnelle.

---

**Points clés**
- Un champ vide ne provoque pas d'erreur - OttoKit insère une chaîne vide
- Méthode 1 : valeur par défaut via un formatter conditionnel
- Méthode 2 : Filter App pour bloquer le workflow si une donnée critique manque
- Toujours tester avec des données volontairement incomplètes avant de publier

**Mots-clés SEO**
- OttoKit données manquantes
- valeur par défaut OttoKit
- fallback workflow OttoKit
- gérer champs vides automatisation WordPress

---

## Notes de production - Module 5

### Captures à préparer
- Sélecteur de données dynamiques dans un champ d'action - vue détaillée
- Sélecteur montrant les champs de plusieurs étapes (trigger + action 1)
- Champ email avec mélange texte statique et tokens dynamiques
- Formatter date : configuration input/output format + timezone
- Formatter nombre : opération multiplication (calcul TVA)
- Formatter texte : split, title case, trim, concatenate, replace
- Formatter nombre aléatoire : configuration plage min/max
- Construction d'un code promo "SCHOOL-{random}"
- Formatter conditionnel : configuration fallback prénom
- Filter App : condition "email is not empty"
- Workflow complet avec formatter + filter avant l'action email

### Environnement de démo
- Compte OttoKit (plan gratuit ou premium)
- Site WordPress schoolsWP avec :
  - WooCommerce installé (au moins 1 commande avec tous les champs remplis + 1 commande avec des champs vides)
  - Au moins 2 utilisateurs de test (un avec prénom, un sans)
- Google Sheet avec colonnes : Date, Client, Email, Montant
- Compte Gmail connecté à OttoKit
- Données de test avec des valeurs vides pour tester les fallbacks

### Durée estimée par leçon (hors quiz)
| Leçon | Durée vidéo |
|-------|-------------|
| 5.1 | 6 min |
| 5.2 | 5 min |
| 5.3 | 6 min |
| 5.4 | 6 min |
| 5.5 | 6 min |
| 5.6 | 4 min |
| 5.7 | 6 min |
| **Total M5** | **39 min** |
