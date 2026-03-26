# Scripts video — Module 16 : Developpeur (avance)

**Formation** : Maitriser TutorLMS
**Module** : M16 — Developpeur (avance) (Premium)
**Lecons** : 7 videos + 1 quiz final (certification)
**Duree totale** : ~50 min
**Date** : 2026-03-23

---

### Lecon 16.1 — Override templates

**Duree** : 7 min
**Type** : Video HeyGen
**Ecran** : Face camera pour intro/conclusion, screencast editeur de code + site WordPress
**Source** : doc developers/override-templates

---

**[INTRO — face camera]**

Tu veux modifier l'apparence d'un cours, d'une lecon ou du catalogue TutorLMS sans toucher au plugin ? C'est exactement a ca que servent les overrides de templates. Tu copies un fichier template du plugin dans ton child theme, tu le modifies, et TutorLMS utilise ta version a la place de l'originale. Tes modifications survivent aux mises a jour du plugin. C'est la methode propre — et la seule que schoolsWP recommande.

**[ECRAN — screencast explorateur de fichiers]**

[Navigation vers wp-content/plugins/tutor/templates/]

Premiere chose a connaitre : l'emplacement des templates originaux. Ouvre ton gestionnaire de fichiers ou ton editeur de code, et va dans wp-content, plugins, tutor, puis templates. C'est la que TutorLMS stocke tous ses fichiers de templates — l'affichage des cours, les lecons, le catalogue, les pages de profil.

Tu y trouves plusieurs dossiers et fichiers PHP. Chaque fichier correspond a une partie de l'interface front-end.

**[ECRAN — screencast editeur de code]**

[Montre la creation du dossier tutor dans le child theme]

Pour overrider un template, la methode est simple. Dans ton child theme — jamais dans le theme parent — cree un dossier nomme "tutor". Pas "templates", pas "tutor-lms" — juste "tutor".

Le chemin final : wp-content/themes/ton-child-theme/tutor/

**[ECRAN — screencast copie de fichier]**

[Copie d'un fichier template specifique]

Ensuite, copie le fichier que tu veux modifier depuis le dossier templates du plugin vers ton dossier tutor dans le child theme. Respecte la meme arborescence. Par exemple, si tu veux modifier le template d'un cours individuel qui se trouve dans single/course/, cree le sous-dossier single/course/ dans ton dossier tutor et copie le fichier dedans.

Le systeme de TutorLMS cherche d'abord dans ton child theme. S'il trouve le fichier, il l'utilise. Sinon, il prend l'original du plugin.

**[ECRAN — screencast modification d'un template]**

[Ouvre lead-info.php et modifie le texte "Course Level"]

Exemple concret. Disons que tu veux modifier le texte "Course Level" qui s'affiche sur la page d'un cours. Le fichier concerne est single/course/enrolled/lead-info.php.

Copie-le dans ton child theme : wp-content/themes/ton-child-theme/tutor/single/course/enrolled/lead-info.php

Ouvre-le, cherche la chaine "Course Level", remplace-la par ce que tu veux — "Niveau du cours" par exemple. Enregistre. Rafraichis la page du cours. Le changement est visible immediatement.

**[ECRAN — screencast avant/apres]**

[Montre la page du cours avant et apres la modification]

Avant : "Course Level". Apres : "Niveau du cours". Ta modification est en place, et elle ne sera pas ecrasee quand tu mettras a jour TutorLMS.

**[TRANSITION — face camera]**

Trois regles a retenir. Un : toujours utiliser un child theme — jamais le theme parent, jamais les fichiers du plugin directement. Deux : ne copie que les fichiers que tu modifies. Ne duplique pas tout le dossier templates — ca rendrait les futures mises a jour plus compliquees, parce que les nouveaux templates du plugin ne seraient pas pris en compte. Trois : attention au fichier course-archive.php — il est sensible et peut casser l'affichage du catalogue si tu le modifies sans precaution.

La recommandation schoolsWP : les overrides de templates, c'est la bonne approche pour les modifications visuelles. Pour les modifications de logique — ajouter des fonctionnalites, modifier des comportements — utilise les hooks. On voit ca dans les lecons 16.3 et 16.4.

---

**Points cles** :
- Templates originaux dans wp-content/plugins/tutor/templates/
- Override dans wp-content/themes/child-theme/tutor/ (meme arborescence)
- Ne copier que les fichiers a modifier, pas tout le dossier
- Toujours utiliser un child theme — jamais le theme parent ni les fichiers du plugin
- Attention a course-archive.php (fichier sensible)
- Modifications visuelles → overrides / Modifications logiques → hooks

**Mots cles SEO** : TutorLMS override templates, personnaliser templates TutorLMS, child theme TutorLMS, modifier affichage cours TutorLMS

---

### Lecon 16.2 — Modifier le dashboard

**Duree** : 7 min
**Type** : Video HeyGen
**Ecran** : Face camera pour intro/conclusion, screencast editeur de code + dashboard front-end
**Source** : doc developers/editing-dashboard

---

**[INTRO — face camera]**

Le dashboard TutorLMS — c'est l'espace ou tes eleves et tes instructeurs passent le plus de temps. Cours en cours, resultats, profil, certificats — tout est la. Par defaut, il fonctionne bien. Mais si tu veux ajouter des onglets, retirer des elements de menu ou modifier la mise en page, il faut aller plus loin. Dans cette lecon, on modifie le dashboard avec les outils de developpeur.

**[ECRAN — screencast front-end]**

[Montre le dashboard etudiant par defaut]

Avant de modifier quoi que ce soit, regarde ce que tu as. Le dashboard TutorLMS affiche une barre laterale avec plusieurs onglets : Dashboard (accueil), My Courses, Wishlist, Reviews, Order History, Settings, et Logout. Chaque onglet a son propre template.

**[ECRAN — screencast editeur de code]**

[Navigation vers le dossier templates du plugin — section dashboard]

Les templates du dashboard se trouvent dans wp-content/plugins/tutor/templates/dashboard/. Tu y trouves les fichiers de chaque section — la page d'accueil du dashboard, la liste des cours, le profil, etc.

Pour modifier l'apparence d'une section, tu utilises la meme technique que la lecon precedente : copie le fichier dans ton child theme, dans le dossier tutor/dashboard/, et modifie-le.

**[ECRAN — screencast editeur de code]**

[Montre le filtre tutor_dashboard/nav_items dans functions.php]

Mais la partie la plus interessante, c'est la personnalisation du menu de navigation. TutorLMS expose un filtre tres utile : tutor_dashboard/nav_items. Ce filtre te donne acces au tableau complet des elements de menu du dashboard.

Dans le fichier functions.php de ton child theme, ajoute un filtre :

```php
add_filter('tutor_dashboard/nav_items', function($nav_items) {
    // Tes modifications ici
    return $nav_items;
});
```

Le tableau $nav_items contient toutes les entrees du menu. Chaque entree a un slug, un titre et une icone.

**[ECRAN — screencast editeur de code]**

[Ajoute un onglet personnalise au dashboard]

Pour ajouter un onglet personnalise — par exemple "Ressources" — ajoute une entree au tableau :

```php
add_filter('tutor_dashboard/nav_items', function($nav_items) {
    $nav_items['resources'] = array(
        'title' => 'Ressources',
        'icon'  => 'tutor-icon-document',
    );
    return $nav_items;
});
```

Le slug "resources" definit l'URL du dashboard : /dashboard/resources/. L'icone utilise les classes d'icones de TutorLMS.

**[ECRAN — screencast editeur de code]**

[Montre comment supprimer un onglet — ex: wishlist]

Pour retirer un onglet — disons que tu n'as pas besoin de la Wishlist :

```php
add_filter('tutor_dashboard/nav_items', function($nav_items) {
    unset($nav_items['wishlist']);
    return $nav_items;
});
```

Deux lignes. L'onglet disparait du menu.

**[ECRAN — screencast editeur de code]**

[Montre le filtre tutor_dashboard/permalinks]

Tu peux aussi modifier les URLs du dashboard avec le filtre tutor_dashboard/permalinks. Ca te permet de changer les slugs — par exemple remplacer "my-courses" par "mes-formations".

**[ECRAN — screencast front-end avant/apres]**

[Montre le dashboard avec les modifications appliquees]

Resultat : le dashboard affiche ton nouvel onglet "Ressources", la Wishlist a disparu, et les URLs sont personnalisees. Tout ca sans toucher au plugin.

**[TRANSITION — face camera]**

La recommandation schoolsWP : commence par le filtre tutor_dashboard/nav_items. C'est le levier le plus utile pour adapter le dashboard a ton projet. Si tu as besoin de modifier le contenu d'un onglet, combine le filtre avec un override de template. Et si tu as besoin d'un onglet avec du contenu completement personnalise, cree un template dans ton child theme qui correspond au slug que tu as ajoute.

---

**Points cles** :
- Templates du dashboard dans wp-content/plugins/tutor/templates/dashboard/
- Filtre tutor_dashboard/nav_items pour ajouter, retirer ou reordonner les onglets
- Filtre tutor_dashboard/permalinks pour modifier les URLs
- Ajouter un onglet : inserer une entree dans le tableau nav_items
- Retirer un onglet : unset($nav_items['slug'])
- Combiner filtres + overrides de templates pour des modifications completes

**Mots cles SEO** : TutorLMS dashboard personnalise, modifier tableau de bord TutorLMS, ajouter onglet dashboard TutorLMS, tutor_dashboard nav_items

---

### Lecon 16.3 — Action Hooks

**Duree** : 8 min
**Type** : Video HeyGen
**Ecran** : Face camera pour intro/conclusion, screencast editeur de code + site WordPress
**Source** : doc developer-documentation/action-hooks

---

**[INTRO — face camera]**

Les action hooks, c'est le mecanisme qui te permet d'executer du code a des moments precis du fonctionnement de TutorLMS — sans modifier les fichiers du plugin. Quand un eleve s'inscrit a un cours, quand un quiz est soumis, quand un instructeur cree une lecon — a chaque etape, TutorLMS declenche des hooks. Toi, tu branches ton code dessus. C'est la base du developpement WordPress propre.

**[ECRAN — screencast editeur de code]**

[Montre le principe d'un action hook — schema conceptuel]

Le principe : TutorLMS contient des appels do_action() a des endroits strategiques de son code. Toi, dans le functions.php de ton child theme ou dans un plugin custom, tu utilises add_action() pour brancher ta propre fonction sur ce hook.

```php
add_action('nom_du_hook', 'ma_fonction', 10, 2);

function ma_fonction($param1, $param2) {
    // Ton code ici
}
```

Le troisieme argument, c'est la priorite — 10 par defaut. Plus le chiffre est bas, plus ta fonction s'execute tot. Le quatrieme, c'est le nombre de parametres que ta fonction recoit.

**[ECRAN — screencast editeur de code]**

[Montre les hooks du Course Builder]

TutorLMS propose des hooks organises par contexte. Commencons par le Course Builder — l'editeur de cours. Voici les principaux :

tutor_course_builder_before_quiz_btn_action — se declenche avant le bouton d'action du quiz, te passe l'ID du quiz.

tutor_course_builder_before_btn_group et tutor_course_builder_after_btn_group — avant et apres le groupe de boutons d'un topic. Te passent l'ID du topic.

Cas d'usage concret : tu veux ajouter un bouton "Dupliquer" a cote des boutons existants d'un topic.

```php
add_action('tutor_course_builder_after_btn_group', function($topic_id) {
    echo '<button class="tutor-btn" data-topic="' . esc_attr($topic_id) . '">Dupliquer</button>';
});
```

**[ECRAN — screencast editeur de code]**

[Montre les hooks des Settings]

Les hooks de Settings te permettent d'injecter du contenu dans les onglets de configuration :

tutor_course/settings_tab_content/before et after — avant et apres le contenu de chaque onglet. Te passent la cle de l'onglet et les donnees du tab.

Il existe aussi des versions dynamiques : tutor_course/settings_tab_content/before/{$key} — ou $key est le slug de l'onglet. Ca te permet de cibler un onglet specifique.

**[ECRAN — screencast editeur de code]**

[Montre les hooks de Lesson et Quiz editing]

Pour les modales d'edition de lecon et de quiz :

tutor_lesson_edit_modal_form_before et after — te passent l'objet $post de la lecon. Tu peux ajouter des champs personnalises dans la modale.

tutor_quiz_edit_modal_info_tab_after et tutor_quiz_edit_modal_settings_tab_after — pour ajouter du contenu dans les onglets de la modale du quiz.

**[ECRAN — screencast editeur de code]**

[Montre les hooks d'inscription instructeur]

Les hooks d'inscription instructeur :

tutor_add_new_instructor_form_fields_before et after — te permettent d'ajouter des champs supplementaires dans le formulaire d'inscription instructeur. Par exemple, un champ "Specialite" ou "Lien LinkedIn".

```php
add_action('tutor_add_new_instructor_form_fields_after', function() {
    echo '<div class="tutor-form-group">';
    echo '<label>Specialite</label>';
    echo '<input type="text" name="instructor_specialty" />';
    echo '</div>';
});
```

**[ECRAN — screencast editeur de code]**

[Montre les hooks Options et Tools]

Derniere categorie : les hooks d'options et d'outils.

tutor_options_before_{$key} et tutor_options_after_{$key} — pour injecter du contenu avant ou apres une section d'options dans les reglages TutorLMS.

tutor_tools_page_{$current_page}_before, tutor_tools_page_{$current_page}, et tutor_tools_page_{$current_page}_after — pour la page Outils.

**[TRANSITION — face camera]**

La recommandation schoolsWP : mets toujours tes hooks dans un plugin custom dedie ou dans le functions.php de ton child theme. Ne modifie jamais les fichiers du plugin. Et pense a la priorite — si plusieurs fonctions sont branchees sur le meme hook, la priorite determine l'ordre d'execution. Pour les cas avancees, la prochaine lecon couvre les filter hooks — ils fonctionnent pareil, mais au lieu d'executer du code, ils modifient des donnees.

---

**Points cles** :
- Action hooks = executer du code a un moment precis (do_action / add_action)
- Priorite : 10 par defaut, plus bas = execute plus tot
- Hooks Course Builder : before/after_btn_group, before_quiz_btn_action
- Hooks Settings : before/after par onglet (generique ou dynamique avec {$key})
- Hooks Lesson/Quiz : injection dans les modales d'edition
- Hooks Instructor : champs supplementaires dans le formulaire d'inscription
- Toujours coder dans un child theme ou un plugin custom

**Mots cles SEO** : TutorLMS action hooks, hooks developpeur TutorLMS, do_action TutorLMS, personnaliser TutorLMS PHP

---

### Lecon 16.4 — Filter Hooks

**Duree** : 8 min
**Type** : Video HeyGen
**Ecran** : Face camera pour intro/conclusion, screencast editeur de code + site WordPress
**Source** : doc developer-documentation/filters

---

**[INTRO — face camera]**

Dans la lecon precedente, on a vu les action hooks — qui executent du code. Les filter hooks, c'est l'autre face de la medaille. Au lieu d'executer du code, ils modifient des donnees. TutorLMS te passe une valeur, tu la transformes, tu la retournes. Le prix d'un cours, les elements du menu, l'URL de redirection apres connexion — tout ca passe par des filtres. TutorLMS en expose plus de 48.

**[ECRAN — screencast editeur de code]**

[Montre le principe d'un filter hook]

Le principe est similaire aux actions, avec une difference : ta fonction recoit une valeur et doit en retourner une.

```php
add_filter('nom_du_filtre', 'ma_fonction', 10, 2);

function ma_fonction($valeur, $param_optionnel) {
    // Modifier $valeur
    return $valeur;  // Obligatoire !
}
```

Si tu oublies le return, le filtre retourne null — et ca casse la fonctionnalite. Toujours retourner quelque chose.

**[ECRAN — screencast editeur de code]**

[Montre les filtres d'authentification]

Commencons par les filtres d'authentification et d'inscription. Ce sont les plus courants :

tutor_login_redirect_url — controle ou l'utilisateur est redirige apres connexion. Par defaut, c'est le dashboard. Tu peux le changer :

```php
add_filter('tutor_login_redirect_url', function($url) {
    return home_url('/mes-cours/');
});
```

tutor_process_login_errors — pour personnaliser les messages d'erreur a la connexion.

tutor_instructor_registration_required_fields — definit les champs obligatoires du formulaire instructeur. Tu peux en ajouter ou en retirer.

**[ECRAN — screencast editeur de code]**

[Montre les filtres de cours et contenu]

Les filtres de contenu — parmi les plus utiles :

tutor_courses_base_slug — change le slug de base des cours dans l'URL. Par defaut, c'est "courses". Tu peux le remplacer par "formations" :

```php
add_filter('tutor_courses_base_slug', function($slug) {
    return 'formations';
});
```

Apres modification, n'oublie pas de regenerer les permalinks dans Reglages > Permaliens.

tutor_course_level — pour modifier les niveaux de difficulte disponibles. Tu peux ajouter des niveaux personnalises ou renommer les existants.

should_remove_price_if_enrolled — controle si le prix est masque pour les eleves deja inscrits. Retourne true pour masquer, false pour afficher.

**[ECRAN — screencast editeur de code]**

[Montre les filtres de monetisation]

Les filtres de monetisation :

tutor_monetization_options — pour ajouter tes propres options de paiement au systeme. C'est le point d'entree pour les passerelles personnalisees (on voit ca en detail dans la lecon 16.6).

get_tutor_course_price — pour modifier le prix affiche d'un cours. Par exemple, ajouter un suffixe "HT" :

```php
add_filter('get_tutor_course_price', function($price) {
    return $price . ' HT';
});
```

is_course_paid — determine si un cours est considere comme payant. Tu peux forcer un cours gratuit en retournant false.

**[ECRAN — screencast editeur de code]**

[Montre les filtres du dashboard]

Les filtres du dashboard — on les a deja vus dans la lecon 16.2 :

tutor_dashboard/nav_items — personnaliser le menu.

tutor_dashboard/permalinks — modifier les URLs.

**[ECRAN — screencast editeur de code]**

[Montre les filtres de templates et media]

Les filtres de templates et medias :

tutor_lms_should_template_override — retourne true ou false pour autoriser ou bloquer le remplacement de templates. Utile pour desactiver les overrides dans certaines conditions.

tutor_lesson_template — modifier le template utilise pour une lecon.

tutor_course_thumbnail_size — changer la taille des images de cours. Par defaut, c'est "post-thumbnail". Tu peux la remplacer par une taille custom.

tutor_video_types — definit les formats video acceptes. Par defaut : mp4, webm, ogg.

tutor_video_stream_is_public — controle si les videos sont accessibles publiquement ou reservees aux inscrits.

**[ECRAN — screencast editeur de code]**

[Montre les filtres REST API]

Et enfin, les filtres REST API :

tutor/api/get_courses — modifie les resultats retournes par l'API.

tutor_rest_course_query_args — personnalise les parametres de requete de l'API. Utile si tu developpes un front-end decouple.

**[TRANSITION — face camera]**

La recommandation schoolsWP : les filtres les plus utiles au quotidien sont tutor_courses_base_slug pour franciser les URLs, tutor_login_redirect_url pour controler la navigation, et tutor_dashboard/nav_items pour adapter l'interface. Commence par ceux-la. Et rappelle-toi : un filtre qui ne retourne rien, c'est un bug garanti. Toujours retourner une valeur.

---

**Points cles** :
- Filter hooks = modifier des donnees (apply_filters / add_filter)
- Toujours retourner une valeur — sinon la fonctionnalite casse
- 48+ filtres disponibles couvrant : auth, cours, monetisation, dashboard, templates, API
- tutor_courses_base_slug : changer "courses" en "formations" dans les URLs
- tutor_login_redirect_url : rediriger apres connexion
- tutor_dashboard/nav_items : personnaliser le menu du dashboard
- get_tutor_course_price : modifier l'affichage du prix

**Mots cles SEO** : TutorLMS filter hooks, filtres TutorLMS developpeur, apply_filters TutorLMS, personnaliser prix cours TutorLMS

---

### Lecon 16.5 — REST API

**Duree** : 7 min
**Type** : Video HeyGen
**Ecran** : Face camera pour intro/conclusion, screencast navigateur (requetes API) + editeur de code
**Source** : doc developer-documentation/rest-api

---

**[INTRO — face camera]**

TutorLMS expose une REST API basee sur WordPress. Ca veut dire que tu peux interroger tes cours, lecons, quiz et utilisateurs via des requetes HTTP standard — en JSON. C'est utile pour developper une application mobile, un dashboard externe, ou integrer TutorLMS avec un outil tiers. Dans cette lecon, on explore les endpoints disponibles et on fait nos premieres requetes.

**[ECRAN — screencast navigateur]**

[Montre une requete GET dans le navigateur ou un outil comme Postman]

L'API TutorLMS est accessible a l'adresse : ton-site.com/wp-json/tutor/v1/

C'est le namespace. Tous les endpoints partent de la. Et comme c'est base sur la REST API WordPress, l'authentification fonctionne de la meme maniere — cookies, application passwords, ou JWT si tu as un plugin dedie.

Point important : en version gratuite de TutorLMS, seules les requetes en lecture (GET) sont disponibles. Les operations d'ecriture necessitent TutorLMS Pro.

**[ECRAN — screencast Postman ou navigateur]**

[Requete GET /wp-json/tutor/v1/courses]

Premier endpoint : la liste des cours.

GET /wp-json/tutor/v1/courses

Ca retourne un tableau JSON avec tous les cours publies. Tu peux filtrer avec des parametres :

- order : asc ou desc
- orderby : date, title, etc.
- paged : pour la pagination
- tags : filtrer par tags
- categories : filtrer par categories de cours

Exemple : /wp-json/tutor/v1/courses?orderby=title&order=asc&categories=lms

**[ECRAN — screencast Postman]**

[Requete GET /wp-json/tutor/v1/courses/123]

Pour un cours specifique :

GET /wp-json/tutor/v1/courses/{course_id}

Remplace {course_id} par l'ID du cours. Tu obtiens toutes les metadonnees : titre, description, prix, instructeur, niveau, duree, nombre d'inscrits.

**[ECRAN — screencast Postman]**

[Requetes sur les topics et lecons]

Pour recuperer la structure d'un cours — les topics et leurs lecons :

GET /wp-json/tutor/v1/topics?course_id=123

Ca retourne les topics (sections) du cours. Ensuite, pour les lecons d'un topic :

GET /wp-json/tutor/v1/lessons?topic_id=456

**[ECRAN — screencast Postman]**

[Montre les endpoints quiz, rating, annonces]

Les autres endpoints disponibles :

GET /wp-json/tutor/v1/quiz/{topic_id} — les quiz d'un topic.

GET /wp-json/tutor/v1/quiz-question-answer/{quiz_id} — les questions et reponses d'un quiz.

GET /wp-json/tutor/v1/course-annoucement/{course_id} — les annonces d'un cours. Note le "ou" dans "annoucement" — c'est une faute de frappe dans l'API, mais c'est le endpoint officiel.

GET /wp-json/tutor/v1/course-rating/{course_id} — les notes et avis.

GET /wp-json/tutor/v1/author-information/{author_id} — les infos de l'instructeur.

GET /wp-json/tutor/v1/course-contents/{course_id} — le contenu complet du cours (topics + lecons + quiz en une seule requete).

**[ECRAN — screencast editeur de code]**

[Montre un exemple d'appel API depuis JavaScript]

Exemple concret : afficher les cours sur une page externe avec JavaScript.

```javascript
fetch('https://ton-site.com/wp-json/tutor/v1/courses', {
    headers: {
        'Authorization': 'Basic ' + btoa('user:app_password')
    }
})
.then(response => response.json())
.then(courses => {
    courses.forEach(course => {
        console.log(course.post_title, course.course_price);
    });
});
```

L'authentification utilise ici un Application Password WordPress — genere dans le profil de l'utilisateur.

**[ECRAN — screencast editeur de code]**

[Montre les filtres API vus en 16.4]

Et rappelle-toi les filtres de la lecon precedente : tutor/api/get_courses et tutor_rest_course_query_args te permettent de modifier les reponses de l'API cote serveur — ajouter des champs, filtrer les resultats, limiter l'acces.

**[TRANSITION — face camera]**

La recommandation schoolsWP : l'endpoint le plus utile, c'est /course-contents/{course_id}. Il te donne toute la structure d'un cours en une seule requete — topics, lecons, quiz. C'est celui que tu utiliseras pour les integrations externes. Et pense a securiser tes endpoints — n'expose pas les donnees sensibles sans authentification.

---

**Points cles** :
- API base sur WordPress REST API, namespace /wp-json/tutor/v1/
- Version gratuite : lecture seule (GET). Ecriture : TutorLMS Pro
- 10 endpoints : courses, topics, lessons, quiz, ratings, announcements, author, course-contents
- Authentification : cookies, Application Passwords, ou JWT
- Filtrable cote serveur avec tutor/api/get_courses et tutor_rest_course_query_args
- Endpoint le plus utile : /course-contents/{course_id} (structure complete)

**Mots cles SEO** : TutorLMS REST API, API cours TutorLMS, endpoints TutorLMS, wp-json tutor v1, integration API LMS WordPress

---

### Lecon 16.6 — Custom Payment Gateways

**Duree** : 8 min
**Type** : Video HeyGen
**Ecran** : Face camera pour intro/conclusion, screencast editeur de code
**Source** : doc developer-documentation/custom-payment-gateways

---

**[INTRO — face camera]**

TutorLMS supporte Stripe et PayPal nativement. Mais si ton marche utilise une autre passerelle — Mollie en Europe, Razorpay en Inde, ou un systeme bancaire local — tu peux creer ta propre passerelle de paiement. TutorLMS fournit un framework avec des classes a etendre et une structure de plugin prete a l'emploi. C'est du developpement avance, mais le processus est bien documente.

**[ECRAN — screencast navigateur]**

[Montre la page de documentation et le lien de telechargement du plugin demo]

Point de depart : la documentation officielle fournit un plugin de demonstration appele "CustomPayment". C'est un squelette complet que tu dupliques et que tu adaptes a ta passerelle.

Telecharge-le, dezippe-le, et regarde la structure.

**[ECRAN — screencast editeur de code]**

[Montre l'arborescence du plugin demo]

Le plugin contient 5 fichiers principaux :

1. CustomPaymentConfig.php — la configuration (cles API, environnement)
2. CustomPaymentGateway.php — la classe principale qui lie le tout
3. Init.php — l'initialisation du plugin
4. Custompayment.php — la logique de paiement
5. composer.json — les dependances

Tu renommes tout avec le nom de ta passerelle. Par exemple, si tu integres Mollie : MollieConfig.php, MollieGateway.php, etc.

**[ECRAN — screencast editeur de code]**

[Ouvre CustomPaymentConfig.php]

Premier fichier a modifier : la configuration. La classe etend BaseConfig et implemente ConfigContract — deux classes fournies par TutorLMS.

```php
namespace CustomPayment;

use Ollyo\PaymentHub\Core\Payment\BaseConfig;
use Ollyo\PaymentHub\Contracts\Payment\ConfigContract;
```

Tu definis tes proprietes — les champs necessaires pour ta passerelle :

```php
private $environment;
private $public_key;
private $secret_key;
private $client_id;
protected $name = 'custompayment';
```

Trois methodes cles a implementer :

get_custompayment_config_keys() — retourne un tableau qui mappe les cles de configuration.

is_configured() — verifie que tous les champs obligatoires sont remplis. Si un champ manque, la passerelle ne s'active pas.

createConfig() — initialise la configuration avec les valeurs saisies par l'admin.

**[ECRAN — screencast editeur de code]**

[Ouvre CustomPaymentGateway.php]

Deuxieme fichier : la classe Gateway. Elle etend GatewayBase et definit trois proprietes :

$dir_name — le nom du dossier racine de ton plugin.
$config_class — la reference vers ta classe de config.
$payment_class — la reference vers ta classe de paiement.

Et quatre methodes getter : get_root_dir_name(), get_payment_class(), get_config_class(), get_autoload_file().

C'est le chef d'orchestre — il connecte la config, le traitement du paiement, et l'autoloader.

**[ECRAN — screencast editeur de code]**

[Ouvre Custompayment.php]

Troisieme fichier : la logique de paiement. C'est ici que tu codes l'interaction avec l'API de ta passerelle. Tu dois implementer :

- La creation du paiement (envoyer la requete a l'API)
- La gestion du callback/webhook (recevoir la confirmation)
- La verification de la transaction (s'assurer que le paiement est valide)

C'est specifique a chaque passerelle. Stripe utilise des PaymentIntents, Mollie utilise des Payments — l'implementation varie.

**[ECRAN — screencast editeur de code]**

[Montre Init.php et composer.json]

Init.php : le point d'entree du plugin. Il enregistre ta passerelle aupres de TutorLMS. Et composer.json gere les dependances — le SDK de ta passerelle, par exemple.

**[ECRAN — screencast WordPress admin]**

[Montre la passerelle qui apparait dans les reglages TutorLMS]

Une fois le plugin active, ta passerelle apparait dans les reglages de TutorLMS, a cote de Stripe et PayPal. L'admin remplit les champs que tu as definis dans la config — cles API, mode sandbox/production — et la passerelle est operationnelle.

**[TRANSITION — face camera]**

La recommandation schoolsWP : avant de coder ta propre passerelle, verifie qu'il n'existe pas deja un plugin tiers. Mollie, Razorpay et plusieurs autres ont des plugins WooCommerce — et si tu utilises WooCommerce comme moteur de paiement pour TutorLMS, tu n'as pas besoin de coder quoi que ce soit. La passerelle custom, c'est pour le eCommerce natif de TutorLMS quand aucune alternative n'existe.

---

**Points cles** :
- Plugin demo "CustomPayment" a telecharger et adapter
- 5 fichiers : Config, Gateway, Init, Payment, composer.json
- Config : etend BaseConfig, implemente ConfigContract, definit les cles API
- Gateway : etend GatewayBase, connecte config + payment + autoloader
- Payment : logique specifique (creation paiement, webhook, verification)
- La passerelle apparait automatiquement dans les reglages TutorLMS
- Alternative : utiliser WooCommerce + plugin de passerelle existant

**Mots cles SEO** : TutorLMS custom payment gateway, passerelle paiement TutorLMS, creer passerelle paiement LMS, TutorLMS PaymentHub, GatewayBase TutorLMS

---

### Lecon 16.7 — Custom Fields

**Duree** : 7 min
**Type** : Video HeyGen
**Ecran** : Face camera pour intro/conclusion, screencast editeur de code + Course Builder
**Source** : doc developer-documentation/register-custom-fields

---

**[INTRO — face camera]**

TutorLMS couvre les champs essentiels d'un cours — titre, description, prix, niveau. Mais chaque projet a ses specificites. Peut-etre que tu as besoin d'un champ "Contenu SEO" pour tes formateurs, d'un champ "Prerequis techniques" sur les lecons, ou d'un champ "Difficulte estimee" sur les quiz. TutorLMS expose une fonction JavaScript — registerField — qui te permet d'injecter des champs personnalises directement dans le Course Builder. Et cote PHP, tu sauvegardes et tu affiches les donnees.

**[ECRAN — screencast editeur de code]**

[Montre la fonction registerField en JavaScript]

La fonction d'enregistrement est en JavaScript. Elle s'appelle Tutor.CourseBuilder.Basic.registerField. Tu l'appelles avec deux arguments : l'emplacement (slot) et la configuration du champ.

```javascript
Tutor.CourseBuilder.Basic.registerField("after_description", {
    name: "seo_content",
    type: "textarea",
    label: "Contenu SEO"
});
```

"after_description" — c'est le slot, l'endroit ou le champ apparait. "seo_content" — c'est l'identifiant unique du champ.

**[ECRAN — screencast editeur de code]**

[Montre la liste des slots disponibles]

Les slots disponibles — ou tu peux placer tes champs :

Pour les cours (Basics) :
- after_description — apres la description du cours
- after_settings — apres les reglages du cours

Pour les lecons (Lesson) :
- after_description — apres la description de la lecon
- bottom_of_sidebar — en bas de la barre laterale

Pour les quiz (Quiz) :
- after_question_description — apres la description d'une question
- bottom_of_question_sidebar — en bas de la barre laterale de la question

Pour les devoirs (Assignment) :
- after_description — apres la description
- bottom_of_sidebar — en bas de la barre laterale

**[ECRAN — screencast editeur de code]**

[Montre les types de champs disponibles]

Les types de champs disponibles : text, number, password, textarea, select, radio, checkbox, switch, date, time, image, video, uploader, WPEditor.

Exemple avec un select :

```javascript
Tutor.CourseBuilder.Basic.registerField("after_settings", {
    name: "course_difficulty",
    type: "select",
    label: "Difficulte estimee",
    options: [
        { value: "debutant", label: "Debutant" },
        { value: "intermediaire", label: "Intermediaire" },
        { value: "avance", label: "Avance" },
        { value: "expert", label: "Expert" }
    ]
});
```

Tu peux aussi ajouter une propriete "priority" pour controler l'ordre d'affichage, et "rules" pour la validation — ca utilise React Hook Form.

**[ECRAN — screencast editeur de code]**

[Montre le code PHP de sauvegarde]

Cote JavaScript, le champ s'affiche. Mais il faut aussi sauvegarder la donnee. Ca se fait en PHP, avec un hook WordPress classique :

```php
add_action('save_post_courses', 'save_custom_course_meta');

function save_custom_course_meta($post_id) {
    if (isset($_POST['seo_content'])) {
        $seo_content = sanitize_textarea_field($_POST['seo_content']);
        update_post_meta($post_id, 'tlcf_seo_content', $seo_content);
    }
}
```

Deux regles : toujours sanitiser les donnees avant de les sauvegarder (sanitize_text_field, sanitize_textarea_field). Et utiliser un prefixe pour tes meta keys — ici "tlcf_" — pour eviter les conflits.

Les hooks de sauvegarde selon le type de contenu :
- save_post_courses — pour les cours
- save_post_lesson — pour les lecons
- save_post_tutor_assignments — pour les devoirs

**[ECRAN — screencast editeur de code]**

[Montre l'affichage des donnees en front-end]

Pour afficher les donnees en front-end, utilise un filtre :

```php
add_filter('tutor_course_details_response', function($response) {
    $seo_content = get_post_meta($response->ID, 'tlcf_seo_content', true);
    $response->seo_content = $seo_content;
    return $response;
});
```

Ca ajoute ton champ personnalise a la reponse du cours — que ce soit dans les templates ou via l'API REST.

Les filtres disponibles par type :
- tutor_course_details_response — cours
- tutor_lesson_details_response — lecons
- tutor_quiz_details_response — quiz

**[ECRAN — screencast Course Builder]**

[Montre le champ personnalise dans le Course Builder]

Resultat dans le Course Builder : ton champ "Contenu SEO" apparait sous la description du cours, avec un textarea editable. Le formateur le remplit, il est sauvegarde, et il est accessible en front-end.

**[TRANSITION — face camera]**

La recommandation schoolsWP : les custom fields sont particulierement utiles pour les informations specifiques a ton domaine — niveau de certification, duree estimee en heures, code de formation CPF. Mets le JavaScript dans un fichier separe enqueue via wp_enqueue_script, pas en inline. Et cote PHP, sanitise toujours les donnees — c'est une regle de securite non-negociable.

---

**Points cles** :
- registerField() en JavaScript pour ajouter des champs dans le Course Builder
- Slots : after_description, after_settings (cours), bottom_of_sidebar (lecons/quiz)
- 14 types de champs : text, select, checkbox, date, WPEditor, etc.
- Sauvegarde PHP via save_post_courses + update_post_meta
- Affichage via filtres : tutor_course_details_response, tutor_lesson_details_response
- Toujours sanitiser les donnees et prefixer les meta keys
- JavaScript dans un fichier separe, pas en inline

**Mots cles SEO** : TutorLMS custom fields, champs personnalises TutorLMS, registerField TutorLMS, Course Builder custom fields, meta donnees cours TutorLMS

---

### Lecon 16.8 — Quiz final Module 16 + Certification

**Duree** : ~10 min (12 questions)
**Type** : Quiz TutorLMS
**Seuil de reussite** : 80%
**Note** : Quiz final de la formation — couvre M1-M16

---

**Question 1**
Pour overrider un template TutorLMS, dans quel dossier du child theme dois-tu placer tes fichiers ?

- A) wp-content/themes/child-theme/templates/
- B) wp-content/themes/child-theme/tutor-lms/
- C) wp-content/themes/child-theme/tutor/ ✓
- D) wp-content/themes/child-theme/tutorlms-templates/

**Explication** : Le dossier doit s'appeler "tutor" dans le child theme. TutorLMS cherche automatiquement dans ce dossier avant d'utiliser ses propres templates.

---

**Question 2**
Quel filtre permet de personnaliser les elements du menu du dashboard TutorLMS ?

- A) tutor_dashboard_menu_items
- B) tutor_dashboard/nav_items ✓
- C) tutor_nav_menu_filter
- D) tutor_sidebar_items

**Explication** : Le filtre tutor_dashboard/nav_items donne acces au tableau complet des onglets du dashboard.

---

**Question 3**
Quelle est la difference fondamentale entre un action hook et un filter hook ?

- A) Les actions sont pour le front-end, les filtres pour le back-end
- B) Les actions executent du code, les filtres modifient et retournent des donnees ✓
- C) Les actions sont plus rapides que les filtres
- D) Les filtres ne peuvent pas recevoir de parametres

**Explication** : Un action hook execute du code a un moment precis (do_action). Un filter hook recoit une valeur, la modifie et la retourne (apply_filters). Oublier le return dans un filtre casse la fonctionnalite.

---

**Question 4**
Quel est le namespace de base de la REST API TutorLMS ?

- A) /wp-json/tutor-lms/v2/
- B) /wp-json/lms/v1/
- C) /wp-json/tutor/v1/ ✓
- D) /wp-json/themeum/tutor/v1/

**Explication** : Tous les endpoints de l'API TutorLMS partent du namespace /wp-json/tutor/v1/.

---

**Question 5**
Dans la creation d'une passerelle de paiement custom, quelle classe la Config doit-elle etendre ?

- A) PaymentConfig
- B) BaseConfig ✓
- C) GatewayConfig
- D) TutorConfig

**Explication** : La classe de configuration etend BaseConfig et implemente ConfigContract, deux classes fournies par le PaymentHub de TutorLMS.

---

**Question 6**
Pour enregistrer un champ personnalise dans le Course Builder, quelle fonction JavaScript utilises-tu ?

- A) Tutor.addField()
- B) Tutor.CourseBuilder.Basic.registerField() ✓
- C) wp.hooks.addFilter('tutor_custom_field')
- D) TutorLMS.registerCustomMeta()

**Explication** : La fonction registerField() prend deux arguments : le slot (emplacement) et la configuration du champ (name, type, label).

---

**Question 7** *(question transversale M1-M5)*
Dans TutorLMS, quel est l'ordre hierarchique du contenu d'un cours ?

- A) Cours → Lecons → Topics → Quiz
- B) Cours → Topics → Lecons/Quiz ✓
- C) Cours → Chapitres → Sections → Lecons
- D) Cours → Modules → Lecons → Exercices

**Explication** : La hierarchie TutorLMS est : Cours (Course) → Topics (sections) → Lecons et Quiz (contenus). Un topic regroupe plusieurs lecons et/ou quiz.

---

**Question 8** *(question transversale M6-M8)*
Quel format de certificat TutorLMS offre le plus de liberte de design ?

- A) Certificat PDF standard
- B) Certificat HTML basique
- C) Certificat drag & drop builder ✓
- D) Certificat genere par code PHP

**Explication** : Le certificat drag & drop builder (disponible avec TutorLMS Pro) permet de placer librement les elements — texte, images, QR code, logo — sur un canvas visuel.

---

**Question 9** *(question transversale M9-M11)*
Quelle est la recommandation schoolsWP pour la verification email a l'inscription etudiant ?

- A) La desactiver pour simplifier l'inscription
- B) L'activer uniquement pour les cours payants
- C) Toujours l'activer pour filtrer les faux comptes ✓
- D) Utiliser un CAPTCHA a la place

**Explication** : La verification email filtre les inscriptions fantomes et ameliore la qualite de la liste d'eleves. schoolsWP recommande de toujours l'activer.

---

**Question 10** *(question transversale M12-M15)*
A partir de combien de videos schoolsWP recommande-t-il de passer a BunnyNet pour l'hebergement ?

- A) 10 videos
- B) 25 videos
- C) 50 videos ✓
- D) 100 videos

**Explication** : schoolsWP recommande BunnyNet des 50 videos. En dessous, YouTube non-liste ou Vimeo gratuit peuvent suffire. BunnyNet coute 5 a 15 dollars par mois pour 50 a 100 videos.

---

**Question 11**
Quel hook TutorLMS te permet d'ajouter des champs dans le formulaire d'inscription instructeur ?

- A) tutor_instructor_form_fields
- B) tutor_add_new_instructor_form_fields_after ✓
- C) tutor_registration_extra_fields
- D) tutor_instructor_signup_hook

**Explication** : Les hooks tutor_add_new_instructor_form_fields_before et after permettent d'injecter des champs HTML supplementaires dans le formulaire d'inscription instructeur.

---

**Question 12**
Pourquoi schoolsWP recommande-t-il de ne jamais modifier les fichiers du plugin TutorLMS directement ?

- A) Le code est chiffre et ne peut pas etre modifie
- B) Les modifications sont ecrasees a chaque mise a jour du plugin ✓
- C) Ca viole la licence du plugin
- D) Le plugin detecte les modifications et se desactive

**Explication** : Toute modification directe des fichiers du plugin est ecrasee quand TutorLMS est mis a jour. Les overrides dans un child theme et les hooks dans un plugin custom sont les seules methodes perennes.

---

**Fin du Module 16 — Developpeur (avance)**

**Fin de la formation "Maitriser TutorLMS"**

Resume du module :
- Override templates : copier dans child-theme/tutor/, modifier, les mises a jour ne cassent rien
- Dashboard : filtre tutor_dashboard/nav_items pour personnaliser le menu
- Action hooks : executer du code aux moments cles (inscription, creation de cours, quiz)
- Filter hooks : modifier les donnees (prix, URLs, menu, templates) — toujours retourner une valeur
- REST API : 10 endpoints en lecture, namespace /wp-json/tutor/v1/
- Custom Payment Gateways : framework BaseConfig + GatewayBase pour integrer toute passerelle
- Custom Fields : registerField() en JS + save_post hooks en PHP

Recommandation finale schoolsWP : utilise toujours un child theme pour les overrides de templates, et un plugin custom pour les hooks et champs personnalises. Ne touche jamais aux fichiers du plugin. C'est la regle numero un du developpement WordPress propre.

Duree totale estimee du module : ~52 minutes (7 lecons + quiz)
