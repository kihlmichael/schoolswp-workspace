# Script video - Module 3, Lecon 3 : Calculs dynamiques

**Formation** : FluentForms Masterclass Formulaires
**Code** : FRM-012 (premium)
**Module** : 3 - Formulaires avances
**Lecon** : 3/8 - Calculs dynamiques
**Duree** : 10 min (~1300 mots)
**Type** : Video HeyGen + voix ElevenLabs
**Ecran** : Face camera intro/outro, screencast construction de calculateurs
**Objectif** : Creer des champs calcules pour afficher des prix, estimations et scores en temps reel

---

**[INTRO - face camera]**

Un formulaire qui calcule un prix en temps reel, c'est un outil de vente. Le visiteur ajuste ses options, et le total se met a jour instantanement. Pas besoin d'attendre un devis par email, pas besoin de calculer de tete.

FluentForms Pro permet de creer des champs calcules. On va en construire trois types : un calculateur de devis, un simulateur de pret, et un estimateur de cout.

**[ECRAN - screencast "Le champ Numeric avec Custom Calculation"]**

Le champ calcule, c'est un champ Numeric standard avec l'option "Custom Calculation" activee.

Ajoutons-en un dans un formulaire. J'ajoute un champ Number, j'ouvre ses settings. Dans la section "Advanced Options", tu trouves "Enable Calculation". Active-le.

Un editeur de formule apparait. C'est la que tu ecris l'equation.

La syntaxe est simple : {inputs.nom_du_champ} pour referencer un autre champ. Les operateurs standards : + - * / pour les operations arithmetiques. Les parentheses pour l'ordre des operations.

**[ECRAN - screencast "Cas pratique 1 : calculateur de devis"]**

Premier exemple : un calculateur de devis pour un photographe.

Champs du formulaire :

Select "Type de prestation" : Portrait (150 euros), Mariage (800 euros), Evenement (500 euros), Corporate (400 euros).

Number "Nombre de photos retouchees" - min 10, max 200, defaut 30.

Checkbox "Options supplementaires" : Album photo (+120 euros), Tirage grand format (+60 euros), Reportage video (+350 euros).

Le champ calcule "Total estime" doit additionner le prix de la prestation, le cout des retouches, et les options cochees.

Pour le select, on utilise une astuce : chaque option a une valeur numerique associee. Dans les settings du Select, au lieu de mettre "Portrait" comme valeur, je mets "150". L'affichage reste "Portrait (150 euros)", mais la valeur interne est 150.

Meme chose pour les checkboxes : "Album photo" a pour valeur 120, "Tirage grand format" = 60, "Reportage video" = 350.

La formule du champ calcule :

{inputs.type_prestation} + ({inputs.nombre_retouches} * 2) + {inputs.options}

Le select envoie 150, 800, 500 ou 400. Le nombre de retouches est multiplie par 2 euros. Les checkboxes cochees additionnent leurs valeurs.

En preview : je selectionne "Mariage" (800), 50 retouches (100), j'ajoute "Album photo" (120) et "Tirage grand format" (60). Total affiche : 1080 euros. Instantane.

**[ECRAN - screencast "Cas pratique 2 : simulateur de pret"]**

Deuxieme exemple : un simulateur de mensualite de pret.

Champs : Number "Montant emprunte" (min 1000, max 500000). Number "Duree en mois" (min 12, max 360). Number "Taux annuel en pourcentage" (min 0.5, max 15, pas 0.1).

Le calcul de mensualite suit une formule standard : M = C * t / (1 - (1 + t)^(-n)) ou C est le capital, t le taux mensuel, n le nombre de mois.

FluentForms supporte les formules basiques mais pas les puissances complexes. Pour un simulateur de pret precis, tu aurais besoin d'un snippet JavaScript. Mais pour une estimation simplifiee, on peut utiliser :

{inputs.montant} * ({inputs.taux} / 1200) / (1 - 1 / (1 + {inputs.taux} / 1200))

Ou alors, approche simplifiee : {inputs.montant} / {inputs.duree} + ({inputs.montant} * {inputs.taux} / 2400).

C'est une estimation, pas un calcul bancaire exact. Mais ca donne une idee au visiteur et ca engage la conversation.

En preview : montant 200 000, duree 240 mois, taux 3.5%. Mensualite estimee affichee en temps reel.

**[ECRAN - screencast "Cas pratique 3 : estimateur de cout projet"]**

Troisieme exemple : estimateur de cout pour un projet WordPress.

Champs :

Radio "Type de site" : Vitrine (valeur 1000), Blog (valeur 500), E-commerce (valeur 2500), LMS (valeur 3000).

Range Slider "Nombre de pages" - min 1, max 50, defaut 5. Affichage en temps reel de la valeur.

Checkbox "Fonctionnalites" : SEO avance (valeur 300), Multilingue (valeur 500), Espace membre (valeur 400), Newsletter (valeur 200), Paiement en ligne (valeur 350).

Champ calcule "Estimation" : {inputs.type_site} + ({inputs.nombre_pages} * 100) + {inputs.fonctionnalites}.

En preview : E-commerce (2500) + 20 pages (2000) + SEO avance (300) + Paiement en ligne (350) = 5150 euros.

Le visiteur ajuste le slider, coche une option - le prix bouge. C'est interactif et transparent.

**[ECRAN - screencast "Affichage et formatage"]**

Quelques options d'affichage pour le champ calcule.

Le champ peut etre en lecture seule - le visiteur voit le resultat mais ne peut pas le modifier. Active "Read Only" dans les settings.

Tu peux ajouter un prefixe ou un suffixe : "euros" apres le nombre, ou le symbole euro avant.

Tu peux aussi masquer le champ calcule et l'utiliser uniquement dans les notifications. Le visiteur ne voit pas le total sur le formulaire, mais l'email de confirmation inclut l'estimation.

Conseil : affiche toujours le resultat en temps reel. Un calcul que le visiteur ne voit pas, c'est un calcul inutile cote UX.

**[ECRAN - slide "Limites et astuces"]**

Quelques limites a connaitre.

Les formules sont evaluees cote client en JavaScript. Pas de requete serveur, donc c'est instantane. Mais ca signifie aussi que les formules complexes (puissances, logarithmes, fonctions trigonometriques) ne sont pas supportees nativement.

Les divisions par zero ne sont pas gerees automatiquement. Si un champ diviseur peut etre a zero, ajoute une condition pour masquer le resultat dans ce cas.

Les valeurs des checkboxes sont additionnees automatiquement quand plusieurs sont cochees. C'est le comportement par defaut - pas besoin de gerer les additions manuellement.

Astuce : tu peux enchainer les champs calcules. Le champ "Sous-total" calcule une partie, le champ "TVA" calcule 20% du sous-total, le champ "Total TTC" additionne les deux. Chaque champ reference le precedent.

**[OUTRO - face camera]**

Les calculs dynamiques transforment un formulaire passif en outil interactif. Le visiteur joue avec les options, voit le prix bouger, et prend sa decision en temps reel.

Prochaine lecon : l'upload de fichiers et images. Comment gerer les CV, les photos, les documents - proprement et en securite. A tout de suite.

---

**Points cles** :
- Champ Numeric + "Enable Calculation" = champ calcule
- Syntaxe : {inputs.nom_du_champ} avec operateurs + - * /
- Valeurs numeriques sur les Select, Radio, Checkbox pour les calculs
- Calculs enchaines possibles (sous-total → TVA → total TTC)
- Execution cote client = instantane, mais formules complexes non supportees
- Toujours afficher le resultat en temps reel

**Mots cles SEO** : FluentForms calcul dynamique, formulaire calcul prix WordPress, FluentForms calculateur, formulaire devis automatique WordPress

---

**Notes de production** :
- Face camera : intro (15 sec) + outro (15 sec)
- Screencast : 3 cas pratiques complets avec test en preview
- Zoomer sur l'editeur de formule et les merge tags
- Montrer le resultat qui bouge en temps reel quand le visiteur modifie un champ
- Rythme : modere - les formules demandent de la concentration
