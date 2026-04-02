# Script video — Module 2, Lecon 5 : Advanced Conditional Groups (Pro)

**Formation** : FluentForms Masterclass Formulaires
**Code** : FRM-012 (premium)
**Module** : 2 — Logique conditionnelle
**Lecon** : 5/7 — Advanced Conditional Groups (Pro)
**Duree** : 10 min (~1300 mots)
**Type** : Video HeyGen + voix ElevenLabs
**Ecran** : Face camera intro/outro, screencast configuration groupes avances
**Objectif** : Maitriser les groupes de conditions imbriques pour des logiques complexes

---

**[INTRO — face camera]**

Jusqu'ici, on a travaille avec des conditions simples : si un champ vaut telle valeur, on fait ceci. Avec le mode ALL ou ANY pour combiner plusieurs conditions.

Mais que faire quand ta logique est plus elaboree ? Quand tu as besoin de dire : "affiche ce champ si le type est e-commerce ET le budget depasse 3000, OU si le type est formation ET le nombre d'apprenants depasse 50" ?

C'est la que les groupes de conditions avances de FluentForms Pro entrent en jeu.

**[ECRAN — slide "Logique basique vs groupes avances"]**

Recap rapide de la logique basique.

En basique, tu as des conditions en liste, reliees par ALL ou ANY. C'est un seul niveau. Soit toutes les conditions doivent etre vraies (ALL), soit au moins une (ANY).

Le probleme : tu ne peux pas melanger AND et OR dans la meme logique. Si tu veux "A ET B OU C ET D", la logique basique ne peut pas l'exprimer.

Les groupes avances resolvent ca. Tu crees des groupes de conditions, et tu relies les groupes entre eux par AND ou OR. A l'interieur de chaque groupe, les conditions sont reliees par AND ou OR independamment.

C'est de la logique imbriquee. Et c'est exclusif a la version Pro.

**[ECRAN — screencast "Acceder aux groupes avances"]**

Dans le builder, ouvre les settings d'un champ. Active la logique conditionnelle.

En version Pro, tu vois un bouton "Add Condition Group" en plus du bouton "Add Condition" habituel.

"Add Condition" ajoute une condition dans le groupe actuel.

"Add Condition Group" cree un nouveau groupe, relie au precedent par AND ou OR.

C'est ce deuxieme bouton qui fait toute la difference.

**[ECRAN — screencast "Cas pratique 1 : formulaire de devis"]**

Construisons le cas que j'ai mentionne en intro.

On a un formulaire avec les champs suivants : Select "Type de projet" (E-commerce, Formation, Blog), Number "Budget", Number "Nombre d'apprenants".

On veut afficher un champ "Accompagnement premium" seulement dans deux cas :
- Le type est "E-commerce" ET le budget depasse 3000 euros
- OU le type est "Formation" ET le nombre d'apprenants depasse 50

Configuration :

Groupe 1 :
- Condition 1 : "Type de projet" Equal "E-commerce"
- Condition 2 : "Budget" Greater Than "3000"
- Liaison interne : ALL (les deux doivent etre vraies)

Clique sur "Add Condition Group".

Groupe 2 :
- Condition 1 : "Type de projet" Equal "Formation"
- Condition 2 : "Nombre d'apprenants" Greater Than "50"
- Liaison interne : ALL

Liaison entre les groupes : OR (un seul groupe suffit).

La logique complete : (E-commerce ET budget > 3000) OU (Formation ET apprenants > 50).

**[ECRAN — screencast "Test du cas pratique 1"]**

Testons en preview.

Test 1 : type = E-commerce, budget = 2000. Le champ "Accompagnement premium" n'apparait pas. Normal — budget insuffisant.

Test 2 : type = E-commerce, budget = 5000. Le champ apparait. Groupe 1 satisfait.

Test 3 : type = Formation, apprenants = 30. Le champ n'apparait pas. Nombre insuffisant.

Test 4 : type = Formation, apprenants = 80. Le champ apparait. Groupe 2 satisfait.

Test 5 : type = Blog. Le champ n'apparait pas. Aucun groupe satisfait.

Cinq tests, cinq resultats corrects. La logique fonctionne.

**[ECRAN — screencast "Cas pratique 2 : formulaire d'inscription"]**

Deuxieme cas pratique. Formulaire d'inscription a une conference.

Champs : Select "Statut" (Etudiant, Professionnel, Intervenant), Select "Format" (Presentiel, En ligne), Checkbox "Options" (Dejeuner networking, Atelier pratique, Visite guidee).

On veut afficher le champ "Code reduction etudiant" si :
- Statut = Etudiant ET Format = Presentiel
- OU Statut = Etudiant ET Format = En ligne

Attends — ca revient simplement a : Statut = Etudiant. Pas besoin de groupes avances ici. Une seule condition suffit.

Mais si on veut afficher "Informations restauration" seulement si :
- Format = Presentiel ET l'option "Dejeuner networking" est cochee
- OU Statut = Intervenant (les intervenants ont toujours acces au dejeuner)

La, on a besoin de deux groupes.

Groupe 1 :
- "Format" Equal "Presentiel"
- "Options" Contains "Dejeuner networking"
- Liaison : ALL

Groupe 2 :
- "Statut" Equal "Intervenant"
- Liaison : (une seule condition, pas besoin de ALL/ANY)

Liaison entre groupes : OR.

**[ECRAN — slide "Visualiser la logique"]**

Quand les conditions deviennent complexes, il faut les visualiser. Voici comment je fais.

J'ecris la logique en pseudo-code avant de la configurer :

```
AFFICHER "Accompagnement premium" SI :
  (Type = E-commerce ET Budget > 3000)
  OU
  (Type = Formation ET Apprenants > 50)
```

Ca prend 10 secondes a ecrire. Et ca t'evite de te perdre dans l'interface quand tu as 3 ou 4 groupes.

Note la logique dans un document ou dans un commentaire HTML du formulaire (via le champ Custom HTML). Le toi de dans 6 mois te remerciera.

**[ECRAN — slide "Limites et bonnes pratiques"]**

Quelques limites a connaitre.

FluentForms supporte plusieurs niveaux de groupes, mais au-dela de 3 groupes, la lisibilite baisse. Si ta logique necessite 5 groupes imbriques, c'est probablement le signe que tu as besoin de deux formulaires distincts.

Les groupes avances sont disponibles sur les champs, les notifications et les confirmations. La meme mecanique partout.

Performance : la logique conditionnelle s'execute en JavaScript cote client. Meme avec des groupes complexes, c'est instantane. Pas de requete serveur, pas de latence.

Bonne pratique : teste CHAQUE combinaison possible. Si tu as 3 groupes avec 2 conditions chacun, tu as potentiellement 8 combinaisons a verifier. Prends le temps de tout tester.

**[OUTRO — face camera]**

Les groupes de conditions avances, c'est l'arme secrete de FluentForms Pro. Avec ca, tu peux creer des formulaires qui reagissent a des scenarios complexes sans une seule ligne de code.

Dans les deux prochaines lecons, on met tout ca en pratique. D'abord un formulaire de devis automatique pour un freelance, puis un formulaire d'inscription evenement avec options. Du concret, de A a Z. On se retrouve tout de suite.

---

**Points cles** :
- Logique basique : conditions en liste (ALL ou ANY, pas les deux)
- Groupes avances (Pro) : groupes de conditions relies par AND/OR entre groupes
- Ecrire la logique en pseudo-code avant de configurer
- Disponible sur champs, notifications et confirmations
- Tester chaque combinaison possible
- Au-dela de 3 groupes : envisager deux formulaires distincts

**Mots cles SEO** : FluentForms groupes conditionnels, FluentForms advanced conditional logic, conditions imbriquees formulaire WordPress, FluentForms Pro logique avancee

---

**Notes de production** :
- Face camera : intro (20 sec) + outro (15 sec)
- Screencast : configuration complete des deux cas pratiques
- Montrer le bouton "Add Condition Group" vs "Add Condition"
- Slide pseudo-code : afficher la logique avant la configuration
- Rythme : plus lent que les lecons precedentes — le sujet est dense
