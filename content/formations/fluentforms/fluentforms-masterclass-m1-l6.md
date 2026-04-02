# Script video — Module 1, Lecon 6 : Migration depuis CF7, WPForms, Gravity Forms

**Formation** : FluentForms Masterclass Formulaires
**Code** : FRM-012 (premium)
**Module** : 1 — Fondations
**Lecon** : 6/6 — Migration depuis CF7, WPForms, Gravity Forms
**Duree** : 8 min (~1100 mots)
**Type** : Video HeyGen + voix ElevenLabs
**Ecran** : Face camera intro/outro, screencast migration pas a pas
**Objectif** : Migrer ses formulaires existants sans perdre de donnees

---

**[INTRO — face camera]**

Tu as deja des formulaires sur ton site. Probablement Contact Form 7 — c'est le plugin le plus installe en France. Peut-etre WPForms ou Gravity Forms.

La bonne nouvelle : FluentForms a un outil de migration integre. Tu peux importer tes formulaires existants sans repartir de zero. La migration est rapide, mais il y a des pieges a connaitre. On voit ca ensemble.

**[ECRAN — screencast "Migrer depuis Contact Form 7"]**

Contact Form 7 est le cas le plus courant. Plus de 5 millions de sites l'utilisent.

Dans ton dashboard WordPress, va dans Fluent Forms → Tools → Import. Tu vas voir une section "Migrate from other plugins" avec les logos des plugins supportes.

Clique sur "Contact Form 7". FluentForms detecte automatiquement tous les formulaires CF7 sur ton site. Tu vois la liste complete avec le nom de chaque formulaire.

Tu peux migrer un formulaire specifique ou tous les formulaires d'un coup. Pour commencer, je te recommande d'en migrer un seul — pour verifier que tout est correct avant de tout basculer.

Clique sur "Import" a cote du formulaire. En quelques secondes, FluentForms cree un nouveau formulaire avec les memes champs. Le mapping est automatique : les champs texte de CF7 deviennent des champs texte FluentForms, les selects restent des selects, les checkboxes restent des checkboxes.

**[ECRAN — screencast "Ce qui est migre"]**

Voyons ce qui est effectivement transfere.

Les champs du formulaire : noms, types, labels, options — tout est repris.

Les notifications email : les adresses de destination, le sujet, le body — migres automatiquement. Les merge tags CF7 sont convertis en merge tags FluentForms.

Les soumissions existantes : si tu utilises un plugin comme Flamingo pour stocker les soumissions CF7, FluentForms peut les importer aussi.

Le resultat : un formulaire FluentForms fonctionnel, avec le meme comportement que l'original.

**[ECRAN — screencast "Migrer depuis WPForms"]**

Meme processus pour WPForms.

Fluent Forms → Tools → Import → WPForms.

Les formulaires WPForms sont detectes automatiquement. Les champs, les notifications, les confirmations — tout est migre.

WPForms et FluentForms partagent une structure similaire (builder drag-and-drop, memes types de champs), donc la migration est propre. Les champs avances de WPForms Pro sont convertis en equivalents FluentForms quand ils existent.

**[ECRAN — screencast "Migrer depuis Gravity Forms"]**

Pour Gravity Forms, c'est le meme principe.

Fluent Forms → Tools → Import → Gravity Forms.

Gravity Forms est le plus complexe des trois — il a des champs avances, des notifications conditionnelles, des post feeds. FluentForms gere la majorite des cas. Les champs standard sont migres sans probleme. Les champs specifiques a Gravity (comme certains champs pricing avances) peuvent necessiter un ajustement manuel.

Apres la migration, ouvre chaque formulaire importe et verifie que les champs sont corrects et que la logique conditionnelle fonctionne.

**[ECRAN — slide "Ce qui n'est PAS migre"]**

Attention : la migration n'est pas complete a 100%. Il y a des elements a gerer manuellement.

Premierement : les shortcodes. Si tu as insere ton formulaire CF7 avec le shortcode [contact-form-7 id="123"], ce shortcode ne fonctionnera plus une fois CF7 desactive. Tu dois remplacer chaque shortcode par le shortcode FluentForms correspondant.

FluentForms genere un shortcode pour chaque formulaire importe : [fluentform id="456"]. Tu dois faire le remplacement dans chaque page ou article qui contenait un formulaire.

Conseil : avant de migrer, fais une liste de toutes les pages ou tes formulaires sont inseres. Un simple Ctrl+F dans l'editeur WordPress sur "contact-form" ou "wpforms" te donnera les emplacements.

Deuxiemement : les integrations externes. Si ton formulaire CF7 etait connecte a Mailchimp via un plugin tiers, cette connexion ne sera pas migree. Tu devras la reconfigurer dans FluentForms.

Troisiemement : le CSS personnalise. Si tu avais ajoute du CSS pour styliser tes formulaires CF7, ce CSS ne s'appliquera pas aux formulaires FluentForms. La bonne nouvelle : FluentForms a un bien meilleur systeme de styling, donc tu n'auras probablement plus besoin de CSS custom.

**[ECRAN — screencast "La methode de migration sans risque"]**

Voici la methode que je recommande. Quatre etapes, zero stress.

Etape 1 : migre tes formulaires dans FluentForms. Les deux plugins coexistent — CF7 continue de fonctionner pendant que tu prepares FluentForms.

Etape 2 : verifie chaque formulaire importe. Ouvre-le dans le builder, controle les champs, les notifications, la logique. Soumets un test.

Etape 3 : remplace les shortcodes page par page. Prends le temps de tester chaque page apres remplacement.

Etape 4 : desactive l'ancien plugin. Pas avant d'avoir verifie que tous les formulaires FluentForms fonctionnent correctement sur toutes les pages.

Ne supprime jamais l'ancien plugin immediatement. Desactive-le d'abord. Garde-le desactive pendant une a deux semaines. Si tout fonctionne, alors tu peux le supprimer.

**[OUTRO — face camera]**

Migrer tes formulaires, ca prend entre 10 minutes et une heure selon le nombre de formulaires et de pages. Le plus long, c'est le remplacement des shortcodes — pas la migration elle-meme.

Et voila, le Module 1 est termine. Tu connais les differences Free vs Pro, l'interface du builder, les types de champs, les notifications, l'anti-spam, et la migration.

Dans le Module 2, on attaque la logique conditionnelle — le vrai moteur de FluentForms. C'est la que tes formulaires deviennent intelligents. On se retrouve dans la premiere lecon.

---

**Points cles** :
- Migration integree : CF7, WPForms, Gravity Forms — un clic
- Migre : champs, notifications, soumissions
- Non migre : shortcodes (a remplacer manuellement), integrations externes, CSS custom
- Methode : migrer → verifier → remplacer shortcodes → desactiver ancien plugin
- Ne jamais supprimer l'ancien plugin sans periode de test

**Mots cles SEO** : migration Contact Form 7 FluentForms, migrer WPForms vers FluentForms, FluentForms import formulaires, remplacer CF7 WordPress

---

**Notes de production** :
- Face camera : intro (15 sec) + outro (20 sec, transition vers Module 2)
- Screencast : migration complete CF7 → FluentForms (etape par etape)
- Montrer le remplacement de shortcode dans l'editeur WordPress
- Ton : rassurant, methodique — la migration fait peur, il faut dedramatiser
