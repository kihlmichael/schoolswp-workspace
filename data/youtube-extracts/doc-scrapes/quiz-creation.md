# Quiz Creation
> Source : https://docs.themeum.com/tutor-lms/quizzes/quiz-creation/

Le Quiz Builder de Tutor LMS permet de creer des quiz interactifs avec 8 types de questions pour evaluer la comprehension des etudiants.

## Acces au Quiz Builder

Dans la section **Curriculum**, cliquer sur **+Quiz**. Le Quiz Builder s'ouvre : saisir un titre et une description avant d'ajouter des questions.

---

## Types de questions

### 1. True/False

Presente une affirmation a laquelle l'etudiant repond Vrai ou Faux. Ideal pour tester les connaissances factuelles.

**Creation :**
- Selectionner le type True/False
- Ajouter la question et une description optionnelle
- Indiquer si la reponse correcte est True ou False
- Renseigner la section Answer Explanation pour le feedback post-quiz

**Options :**
- Answer Required : rendre la question obligatoire
- Randomize Choice : ordre aleatoire des options True/False
- Point For This Question : valeur en points (defaut : 1)
- Display Points : afficher ou masquer les points

### 2. Multiple Choice

Presente une question avec plusieurs options de reponse.

**Creation :**
- Selectionner Multiple Choice
- Saisir la question
- Cliquer **+ Add Option** pour ajouter des choix
- Ajouter des images optionnelles (resolution recommandee : 700x430 px)
- Cocher la ou les bonnes reponses

**Configuration :**
- Activer "Multiple Correct Answer" pour autoriser plusieurs reponses correctes
- Quand active, selectionner les bonnes reponses dans la sidebar gauche

### 3. Open Ended / Essay

Questions subjectives demandant des reponses ecrites detaillees.

**Creation :**
- Selectionner Open-Ended/Essay
- Saisir le titre et la description
- Definir une limite de caracteres optionnelle dans les Quiz Settings

**Usage :** evaluer la comprehension approfondie et la pensee critique.

### 4. Fill in the Blanks

L'etudiant complete des phrases en remplissant les mots manquants.

**Creation :**
- Selectionner Fill in the Blanks
- Ajouter titre et description
- Utiliser la variable **{dash}** pour indiquer les espaces vides
- Saisir les reponses correctes dans "Correct Answer(s)"

**Format des reponses :**
- Un seul blanc : saisir la reponse directement
- Plusieurs blancs : lister les reponses dans l'ordre, separees par **|**

*Exemple :* Question : "Water is made up of {dash} and {dash}."
Reponses : "Hydrogen | Oxygen"

### 5. Short Answer

Teste les connaissances via des reponses textuelles courtes.

**Creation :**
- Selectionner Short Answer
- Saisir titre et description
- Definir une limite de caracteres optionnelle dans les Quiz Settings

### 6. Matching

L'etudiant associe des elements de deux listes en glissant les options.

**Creation :**
- Saisir titre et description
- Cliquer **+ Add Option** pour ajouter des paires
- Saisir le terme et sa reponse correspondante
- Cliquer **Save**

**Option supplementaire :**
- Activer **Image Matching** pour inclure des images dans les options
- Supporte les evaluations visuelles par paires

### 7. Image Answering

Questions interactives ou l'etudiant selectionne des reponses associees a des images.

**Creation :**
- Saisir le titre dans le champ Question
- Ajouter une description optionnelle
- Cliquer **Add Image** pour uploader (recommande : 700x430 px)
- Utiliser "Write option" pour le label/description de l'image
- Cliquer **+ Add Option** pour des choix supplementaires
- Renseigner l'explication dans "Write answer explanation"
- Cliquer **Ok** puis **Save**

### 8. Ordering

L'etudiant reordonne des elements (texte, images ou les deux) dans le bon ordre.

**Creation :**
- Selectionner le type Ordering
- Ajouter les elements a reordonner
- Etablir la sequence correcte
- Configurer les points et options d'affichage

**Usage :** tester les connaissances procedurales et la comprehension sequentielle.

---

## Options communes a tous les types

- **Answer Required** : rendre la question obligatoire
- **Point For This Question** : assigner une valeur en points
- **Display Points** : afficher/masquer la valeur en points
- **Answer Explanation** : feedback accessible apres soumission du quiz

> Les explications sont accessibles sur la page Quiz Details uniquement apres avoir complete le quiz. Si Quiz Details est desactive, les Answer Explanations ne sont pas visibles.
