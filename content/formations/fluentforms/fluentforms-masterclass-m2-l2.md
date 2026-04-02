# Script video — Module 2, Lecon 2 : Afficher/masquer des champs

**Formation** : FluentForms Masterclass Formulaires
**Code** : FRM-012 (premium)
**Module** : 2 — Logique conditionnelle
**Lecon** : 2/7 — Afficher/masquer des champs
**Duree** : 8 min (~1100 mots)
**Type** : Video HeyGen + voix ElevenLabs
**Ecran** : Face camera intro/outro, screencast configuration step-by-step
**Objectif** : Configurer des conditions simples et multiples pour afficher/masquer des champs

---

**[INTRO — face camera]**

On entre dans le concret. Dans cette lecon, tu vas configurer ta premiere condition dans FluentForms. Afficher un champ quand une condition est remplie, le masquer sinon.

C'est la brique de base de tout ce qu'on va construire dans ce module. Une fois que tu maitrises ca, tout le reste suit.

**[ECRAN — screencast "Acceder a la logique conditionnelle"]**

Ouvrons un formulaire dans le builder.

J'ai un formulaire avec trois champs : un Select "Type de projet" (Site vitrine, E-commerce, Blog), un champ Number "Nombre de produits", et un Textarea "Description du projet".

Le champ "Nombre de produits" n'a de sens que si le visiteur choisit "E-commerce". On va le masquer par defaut et l'afficher uniquement dans ce cas.

Clique sur le champ "Nombre de produits" pour ouvrir ses settings dans le panneau de droite.

Descends jusqu'a la section "Advanced Options". Tu vas voir un toggle "Conditional Logic". Active-le.

**[ECRAN — screencast "Configurer une condition simple"]**

Une fois active, tu vois apparaitre un panneau de configuration.

Premiere option : "Show this field if" ou "Hide this field if". On choisit "Show" — le champ sera masque par defaut et s'affichera quand la condition est remplie.

Ensuite, tu configures la condition.

Champ : selectionne "Type de projet" dans le menu deroulant.

Operateur : selectionne "Equal".

Valeur : tape "E-commerce".

C'est fait. La condition dit : affiche "Nombre de produits" si "Type de projet" est egal a "E-commerce".

Sauvegarde et teste en preview.

**[ECRAN — screencast "Test en preview"]**

En preview, le formulaire affiche "Type de projet" et "Description du projet". Le champ "Nombre de produits" est invisible.

Je selectionne "Site vitrine" — rien ne change. Je selectionne "E-commerce" — le champ "Nombre de produits" apparait avec une transition fluide. Je reviens a "Site vitrine" — il disparait.

C'est instantane. Pas de rechargement de page, pas de delai. Le visiteur ne sait meme pas que d'autres champs existent.

**[ECRAN — screencast "Conditions multiples — AND"]**

Maintenant, ajoutons une deuxieme condition.

Imaginons que tu veux afficher un champ "Plateforme e-commerce preferee" (WooCommerce, Shopify, PrestaShop) seulement si le type est "E-commerce" ET que le nombre de produits est superieur a 50.

Ouvre les settings du champ "Plateforme e-commerce". Active la logique conditionnelle. Clique sur "Add Condition" pour ajouter une deuxieme ligne.

Condition 1 : "Type de projet" Equal "E-commerce".

Condition 2 : "Nombre de produits" Greater Than "50".

En haut, tu vois un selecteur : "ALL" ou "ANY". Choisis "ALL".

"ALL" signifie que TOUTES les conditions doivent etre remplies pour que le champ s'affiche. C'est le AND logique. Les deux conditions doivent etre vraies simultanement.

Test : je choisis "E-commerce" et je mets 30 produits — le champ plateforme n'apparait pas. Je monte a 60 produits — il apparait. Les deux conditions sont remplies.

**[ECRAN — screencast "Conditions multiples — OR"]**

Maintenant, changeons la logique. Au lieu de "ALL", selectionne "ANY".

"ANY" signifie qu'AU MOINS UNE condition suffit. C'est le OR logique.

Exemple : afficher un champ "Budget supplementaire" si le type est "E-commerce" OU si le type est "Application web". Les deux types de projets coutent cher, donc on veut poser la question du budget dans les deux cas.

Condition 1 : "Type de projet" Equal "E-commerce".

Condition 2 : "Type de projet" Equal "Application web".

Mode : "ANY".

Test : je choisis "Site vitrine" — pas de champ budget. Je choisis "E-commerce" — le champ apparait. Je choisis "Application web" — le champ apparait aussi. Je choisis "Blog" — il disparait.

**[ECRAN — screencast "Les operateurs disponibles"]**

Parlons des operateurs. FluentForms en propose plusieurs.

Equal : la valeur doit correspondre exactement.

Not Equal : la valeur ne doit PAS correspondre. Utile pour "afficher si le champ n'est PAS vide" ou "afficher si le type n'est PAS blog".

Greater Than / Less Than : pour les champs numeriques. "Afficher si le budget est superieur a 5000".

Contains : la valeur doit contenir un texte specifique. Utile pour les champs texte libres.

Starts With / Ends With : la valeur doit commencer ou finir par un texte specifique.

Is Empty / Is Not Empty : le champ est vide ou non. "Afficher le champ suivant seulement si le precedent a ete rempli" — ca cree un formulaire progressif.

**[ECRAN — slide "Bonnes pratiques"]**

Quelques bonnes pratiques avant de te lancer.

Commence simple. Une condition par champ. Quand ca marche, ajoute de la complexite.

Teste chaque condition immediatement. N'attends pas d'avoir configure 10 conditions pour tester. Configure, teste, passe a la suivante.

Nomme tes champs clairement. Si ton champ s'appelle "champ_7", tu ne sauras plus quelle condition tu as configuree dans une semaine. Utilise des noms explicites : "type_projet", "nombre_produits", "budget".

Documente les conditions complexes. Si tu as un formulaire avec 8 conditions imbriquees, note la logique quelque part. Le toi du futur te remerciera.

**[OUTRO — face camera]**

Tu viens de maitriser la base de la logique conditionnelle : afficher et masquer des champs selon les reponses. C'est simple a configurer, mais ca change completement l'experience de tes visiteurs.

Dans la prochaine lecon, on applique la meme logique aux notifications email. Le bon message, a la bonne personne, automatiquement. A tout de suite.

---

**Points cles** :
- Acceder : champ → Advanced Options → Conditional Logic
- Show/Hide selon un champ, un operateur, une valeur
- ALL (AND) : toutes les conditions doivent etre vraies
- ANY (OR) : au moins une condition suffit
- Operateurs : Equal, Not Equal, Greater/Less Than, Contains, Is Empty
- Tester chaque condition immediatement en preview

**Mots cles SEO** : FluentForms afficher masquer champs, FluentForms conditional logic configuration, formulaire conditionnel WordPress, FluentForms conditions AND OR

---

**Notes de production** :
- Face camera : intro (15 sec) + outro (15 sec)
- Screencast dominant — chaque clic montre en temps reel
- Zoomer sur le panneau de conditions et le selecteur ALL/ANY
- Rythme : pause apres chaque test pour que le viewer assimile
