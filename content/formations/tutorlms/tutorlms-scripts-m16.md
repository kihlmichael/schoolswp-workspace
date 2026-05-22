# Scripts vidéo — Module 16 : Développeur (avancé)

**Formation** : Maîtriser TutorLMS
**Module** : M16 — Développeur (avancé) (Premium)
**Leçons** : 7 vidéos + 1 quiz final (certification)
**Durée totale** : ~50 min
**Date** : 2026-03-23

---

### Leçon 16.1 — Override templates

**Durée** : 7 min
**Type** : Vidéo HeyGen
**Écran** : Face caméra pour intro/conclusion, screencast éditeur de code + site WordPress
**Source** : doc developers/override-templates

---

**[INTRO — face caméra]**

Tu veux modifier l'apparence d'un cours, d'une leçon ou du catalogue TutorLMS sans toucher au plugin ? C'est exactement à ça que servent les overrides de templates. Tu copies un fichier template du plugin dans ton child theme, tu le modifies, et TutorLMS utilise ta version à la place de l'originale. Tes modifications survivent aux mises à jour du plugin. C'est la méthode propre — et la seule que schoolsWP recommande.

**[ÉCRAN — screencast explorateur de fichiers]**

[Navigation vers wp-content/plugins/tutor/templates/]

Première chose à connaître : l'emplacement des templates originaux. Ouvre ton gestionnaire de fichiers ou ton éditeur de code, et va dans wp-content, plugins, tutor, puis templates. C'est là que TutorLMS stocke tous ses fichiers de templates — l'affichage des cours, les leçons, le catalogue, les pages de profil.

Tu y trouves plusieurs dossiers et fichiers PHP. Chaque fichier correspond à une partie de l'interface front-end.

**[ÉCRAN — screencast éditeur de code]**

[Montre la création du dossier tutor dans le child theme]

Pour overrider un template, la méthode est simple. Dans ton child theme — jamais dans le thème parent — crée un dossier nommé "tutor". Pas "templates", pas "tutor-lms" — juste "tutor".

Le chemin final : wp-content/themes/ton-child-theme/tutor/

**[ÉCRAN — screencast copie de fichier]**

[Copie d'un fichier template spécifique]

Ensuite, copie le fichier que tu veux modifier depuis le dossier templates du plugin vers ton dossier tutor dans le child theme. Respecte la même arborescence. Par exemple, si tu veux modifier le template d'un cours individuel qui se trouve dans single/course/, crée le sous-dossier single/course/ dans ton dossier tutor et copie le fichier dedans.

Le système de TutorLMS cherche d'abord dans ton child theme. S'il trouve le fichier, il l'utilise. Sinon, il prend l'original du plugin.

**[ÉCRAN — screencast modification d'un template]**

[Ouvre lead-info.php et modifie le texte "Course Level"]

Exemple concret. Disons que tu veux modifier le texte "Course Level" qui s'affiche sur la page d'un cours. Le fichier concerné est single/course/enrolled/lead-info.php.

Copie-le dans ton child theme : wp-content/themes/ton-child-theme/tutor/single/course/enrolled/lead-info.php

Ouvre-le, cherche la chaîne "Course Level", remplace-la par ce que tu veux — "Niveau du cours" par exemple. Enregistre. Rafraîchis la page du cours. Le changement est visible immédiatement.

**[ÉCRAN — screencast avant/après]**

[Montre la page du cours avant et après la modification]

Avant : "Course Level". Après : "Niveau du cours". Ta modification est en place, et elle ne sera pas écrasée quand tu mettras à jour TutorLMS.

**[TRANSITION — face caméra]**

Trois règles à retenir. Un : toujours utiliser un child theme — jamais le thème parent, jamais les fichiers du plugin directement. Deux : ne copie que les fichiers que tu modifies. Ne duplique pas tout le dossier templates — ça rendrait les futures mises à jour plus compliquées, parce que les nouveaux templates du plugin ne seraient pas pris en compte. Trois : attention au fichier course-archive.php — il est sensible et peut casser l'affichage du catalogue si tu le modifies sans précaution.

La recommandation schoolsWP : les overrides de templates, c'est la bonne approche pour les modifications visuelles. Pour les modifications de logique — ajouter des fonctionnalités, modifier des comportements — utilise les hooks. On voit ça dans les leçons 16.3 et 16.4.

---

**Points clés** :
- Templates originaux dans wp-content/plugins/tutor/templates/
- Override dans wp-content/themes/child-theme/tutor/ (même arborescence)
- Ne copier que les fichiers à modifier, pas tout le dossier
- Toujours utiliser un child theme — jamais le thème parent ni les fichiers du plugin
- Attention à course-archive.php (fichier sensible)
- Modifications visuelles → overrides / Modifications logiques → hooks

**Mots-clés SEO** : TutorLMS override templates, personnaliser templates TutorLMS, child theme TutorLMS, modifier affichage cours TutorLMS

---

### Leçon 16.2 — Modifier le dashboard

**Durée** : 7 min
**Type** : Vidéo HeyGen
**Écran** : Face caméra pour intro/conclusion, screencast éditeur de code + dashboard front-end
**Source** : doc developers/editing-dashboard

---

**[INTRO — face caméra]**

Le dashboard TutorLMS — c'est l'espace où tes élèves et tes instructeurs passent le plus de temps. Cours en cours, résultats, profil, certificats — tout est là. Par défaut, il fonctionne bien. Mais si tu veux ajouter des onglets, retirer des éléments de menu ou modifier la mise en page, il faut aller plus loin. Dans cette leçon, on modifie le dashboard avec les outils de développeur.

**[ÉCRAN — screencast front-end]**

[Montre le dashboard étudiant par défaut]

Avant de modifier quoi que ce soit, regarde ce que tu as. Le dashboard TutorLMS affiche une barre latérale avec plusieurs onglets : Dashboard (accueil), My Courses, Wishlist, Reviews, Order History, Settings, et Logout. Chaque onglet a son propre template.

**[ÉCRAN — screencast éditeur de code]**

[Navigation vers le dossier templates du plugin — section dashboard]

Les templates du dashboard se trouvent dans wp-content/plugins/tutor/templates/dashboard/. Tu y trouves les fichiers de chaque section — la page d'accueil du dashboard, la liste des cours, le profil, etc.

Pour modifier l'apparence d'une section, tu utilises la même technique que la leçon précédente : copie le fichier dans ton child theme, dans le dossier tutor/dashboard/, et modifie-le.

**[ÉCRAN — screencast éditeur de code]**

[Montre le filtre tutor_dashboard/nav_items dans functions.php]

Mais la partie la plus intéressante, c'est la personnalisation du menu de navigation. TutorLMS expose un filtre très utile : tutor_dashboard/nav_items. Ce filtre te donne accès au tableau complet des éléments de menu du dashboard.

Dans le fichier functions.php de ton child theme, ajoute un filtre :

```php
add_filter('tutor_dashboard/nav_items', function($nav_items) {
    // Tes modifications ici
    return $nav_items;
});
```

Le tableau $nav_items contient toutes les entrées du menu. Chaque entrée a un slug, un titre et une icône.

**[ÉCRAN — screencast éditeur de code]**

[Ajoute un onglet personnalisé au dashboard]

Pour ajouter un onglet personnalisé — par exemple "Ressources" — ajoute une entrée au tableau :

```php
add_filter('tutor_dashboard/nav_items', function($nav_items) {
    $nav_items['resources'] = array(
        'title' => 'Ressources',
        'icon'  => 'tutor-icon-document',
    );
    return $nav_items;
});
```

Le slug "resources" définit l'URL du dashboard : /dashboard/resources/. L'icône utilise les classes d'icônes de TutorLMS.

**[ÉCRAN — screencast éditeur de code]**

[Montre comment supprimer un onglet — ex: wishlist]

Pour retirer un onglet — disons que tu n'as pas besoin de la Wishlist :

```php
add_filter('tutor_dashboard/nav_items', function($nav_items) {
    unset($nav_items['wishlist']);
    return $nav_items;
});
```

Deux lignes. L'onglet disparaît du menu.

**[ÉCRAN — screencast éditeur de code]**

[Montre le filtre tutor_dashboard/permalinks]

Tu peux aussi modifier les URLs du dashboard avec le filtre tutor_dashboard/permalinks. Ça te permet de changer les slugs — par exemple remplacer "my-courses" par "mes-formations".

**[ÉCRAN — screencast front-end avant/après]**

[Montre le dashboard avec les modifications appliquées]

Résultat : le dashboard affiche ton nouvel onglet "Ressources", la Wishlist a disparu, et les URLs sont personnalisées. Tout ça sans toucher au plugin.

**[TRANSITION — face caméra]**

La recommandation schoolsWP : commence par le filtre tutor_dashboard/nav_items. C'est le levier le plus utile pour adapter le dashboard à ton projet. Si tu as besoin de modifier le contenu d'un onglet, combine le filtre avec un override de template. Et si tu as besoin d'un onglet avec du contenu complètement personnalisé, crée un template dans ton child theme qui correspond au slug que tu as ajouté.

---

**Points clés** :
- Templates du dashboard dans wp-content/plugins/tutor/templates/dashboard/
- Filtre tutor_dashboard/nav_items pour ajouter, retirer ou réordonner les onglets
- Filtre tutor_dashboard/permalinks pour modifier les URLs
- Ajouter un onglet : insérer une entrée dans le tableau nav_items
- Retirer un onglet : unset($nav_items['slug'])
- Combiner filtres + overrides de templates pour des modifications complètes

**Mots-clés SEO** : TutorLMS dashboard personnalisé, modifier tableau de bord TutorLMS, ajouter onglet dashboard TutorLMS, tutor_dashboard nav_items

---

### Leçon 16.3 — Action Hooks

**Durée** : 8 min
**Type** : Vidéo HeyGen
**Écran** : Face caméra pour intro/conclusion, screencast éditeur de code + site WordPress
**Source** : doc developer-documentation/action-hooks

---

**[INTRO — face caméra]**

Les action hooks, c'est le mécanisme qui te permet d'exécuter du code à des moments précis du fonctionnement de TutorLMS — sans modifier les fichiers du plugin. Quand un élève s'inscrit à un cours, quand un quiz est soumis, quand un instructeur crée une leçon — à chaque étape, TutorLMS déclenche des hooks. Toi, tu branches ton code dessus. C'est la base du développement WordPress propre.

**[ÉCRAN — screencast éditeur de code]**

[Montre le principe d'un action hook — schéma conceptuel]

Le principe : TutorLMS contient des appels do_action() à des endroits stratégiques de son code. Toi, dans le functions.php de ton child theme ou dans un plugin custom, tu utilises add_action() pour brancher ta propre fonction sur ce hook.

```php
add_action('nom_du_hook', 'ma_fonction', 10, 2);

function ma_fonction($param1, $param2) {
    // Ton code ici
}
```

Le troisième argument, c'est la priorité — 10 par défaut. Plus le chiffre est bas, plus ta fonction s'exécute tôt. Le quatrième, c'est le nombre de paramètres que ta fonction reçoit.

**[ÉCRAN — screencast éditeur de code]**

[Montre les hooks du Course Builder]

TutorLMS propose des hooks organisés par contexte. Commençons par le Course Builder — l'éditeur de cours. Voici les principaux :

tutor_course_builder_before_quiz_btn_action — se déclenche avant le bouton d'action du quiz, te passe l'ID du quiz.

tutor_course_builder_before_btn_group et tutor_course_builder_after_btn_group — avant et après le groupe de boutons d'un topic. Te passent l'ID du topic.

Cas d'usage concret : tu veux ajouter un bouton "Dupliquer" à côté des boutons existants d'un topic.

```php
add_action('tutor_course_builder_after_btn_group', function($topic_id) {
    echo '<button class="tutor-btn" data-topic="' . esc_attr($topic_id) . '">Dupliquer</button>';
});
```

**[ÉCRAN — screencast éditeur de code]**

[Montre les hooks des Settings]

Les hooks de Settings te permettent d'injecter du contenu dans les onglets de configuration :

tutor_course/settings_tab_content/before et after — avant et après le contenu de chaque onglet. Te passent la clé de l'onglet et les données du tab.

Il existe aussi des versions dynamiques : tutor_course/settings_tab_content/before/{$key} — où $key est le slug de l'onglet. Ça te permet de cibler un onglet spécifique.

**[ÉCRAN — screencast éditeur de code]**

[Montre les hooks de Lesson et Quiz editing]

Pour les modales d'édition de leçon et de quiz :

tutor_lesson_edit_modal_form_before et after — te passent l'objet $post de la leçon. Tu peux ajouter des champs personnalisés dans la modale.

tutor_quiz_edit_modal_info_tab_after et tutor_quiz_edit_modal_settings_tab_after — pour ajouter du contenu dans les onglets de la modale du quiz.

**[ÉCRAN — screencast éditeur de code]**

[Montre les hooks d'inscription instructeur]

Les hooks d'inscription instructeur :

tutor_add_new_instructor_form_fields_before et after — te permettent d'ajouter des champs supplémentaires dans le formulaire d'inscription instructeur. Par exemple, un champ "Spécialité" ou "Lien LinkedIn".

```php
add_action('tutor_add_new_instructor_form_fields_after', function() {
    echo '<div class="tutor-form-group">';
    echo '<label>Spécialité</label>';
    echo '<input type="text" name="instructor_specialty" />';
    echo '</div>';
});
```

**[ÉCRAN — screencast éditeur de code]**

[Montre les hooks Options et Tools]

Dernière catégorie : les hooks d'options et d'outils.

tutor_options_before_{$key} et tutor_options_after_{$key} — pour injecter du contenu avant ou après une section d'options dans les réglages TutorLMS.

tutor_tools_page_{$current_page}_before, tutor_tools_page_{$current_page}, et tutor_tools_page_{$current_page}_after — pour la page Outils.

**[TRANSITION — face caméra]**

La recommandation schoolsWP : mets toujours tes hooks dans un plugin custom dédié ou dans le functions.php de ton child theme. Ne modifie jamais les fichiers du plugin. Et pense à la priorité — si plusieurs fonctions sont branchées sur le même hook, la priorité détermine l'ordre d'exécution. Pour les cas avancés, la prochaine leçon couvre les filter hooks — ils fonctionnent pareil, mais au lieu d'exécuter du code, ils modifient des données.

---

**Points clés** :
- Action hooks = exécuter du code à un moment précis (do_action / add_action)
- Priorité : 10 par défaut, plus bas = exécuté plus tôt
- Hooks Course Builder : before/after_btn_group, before_quiz_btn_action
- Hooks Settings : before/after par onglet (générique ou dynamique avec {$key})
- Hooks Lesson/Quiz : injection dans les modales d'édition
- Hooks Instructor : champs supplémentaires dans le formulaire d'inscription
- Toujours coder dans un child theme ou un plugin custom

**Mots-clés SEO** : TutorLMS action hooks, hooks développeur TutorLMS, do_action TutorLMS, personnaliser TutorLMS PHP

---

### Leçon 16.4 — Filter Hooks

**Durée** : 8 min
**Type** : Vidéo HeyGen
**Écran** : Face caméra pour intro/conclusion, screencast éditeur de code + site WordPress
**Source** : doc developer-documentation/filters

---

**[INTRO — face caméra]**

Dans la leçon précédente, on a vu les action hooks — qui exécutent du code. Les filter hooks, c'est l'autre face de la médaille. Au lieu d'exécuter du code, ils modifient des données. TutorLMS te passe une valeur, tu la transformes, tu la retournes. Le prix d'un cours, les éléments du menu, l'URL de redirection après connexion — tout ça passe par des filtres. TutorLMS en expose plus de 48.

**[ÉCRAN — screencast éditeur de code]**

[Montre le principe d'un filter hook]

Le principe est similaire aux actions, avec une différence : ta fonction reçoit une valeur et doit en retourner une.

```php
add_filter('nom_du_filtre', 'ma_fonction', 10, 2);

function ma_fonction($valeur, $param_optionnel) {
    // Modifier $valeur
    return $valeur;  // Obligatoire !
}
```

Si tu oublies le return, le filtre retourne null — et ça casse la fonctionnalité. Toujours retourner quelque chose.

**[ÉCRAN — screencast éditeur de code]**

[Montre les filtres d'authentification]

Commençons par les filtres d'authentification et d'inscription. Ce sont les plus courants :

tutor_login_redirect_url — contrôle où l'utilisateur est redirigé après connexion. Par défaut, c'est le dashboard. Tu peux le changer :

```php
add_filter('tutor_login_redirect_url', function($url) {
    return home_url('/mes-cours/');
});
```

tutor_process_login_errors — pour personnaliser les messages d'erreur à la connexion.

tutor_instructor_registration_required_fields — définit les champs obligatoires du formulaire instructeur. Tu peux en ajouter ou en retirer.

**[ÉCRAN — screencast éditeur de code]**

[Montre les filtres de cours et contenu]

Les filtres de contenu — parmi les plus utiles :

tutor_courses_base_slug — change le slug de base des cours dans l'URL. Par défaut, c'est "courses". Tu peux le remplacer par "formations" :

```php
add_filter('tutor_courses_base_slug', function($slug) {
    return 'formations';
});
```

Après modification, n'oublie pas de régénérer les permalinks dans Réglages > Permaliens.

tutor_course_level — pour modifier les niveaux de difficulté disponibles. Tu peux ajouter des niveaux personnalisés ou renommer les existants.

should_remove_price_if_enrolled — contrôle si le prix est masqué pour les élèves déjà inscrits. Retourne true pour masquer, false pour afficher.

**[ÉCRAN — screencast éditeur de code]**

[Montre les filtres de monétisation]

Les filtres de monétisation :

tutor_monetization_options — pour ajouter tes propres options de paiement au système. C'est le point d'entrée pour les passerelles personnalisées (on voit ça en détail dans la leçon 16.6).

get_tutor_course_price — pour modifier le prix affiché d'un cours. Par exemple, ajouter un suffixe "HT" :

```php
add_filter('get_tutor_course_price', function($price) {
    return $price . ' HT';
});
```

is_course_paid — détermine si un cours est considéré comme payant. Tu peux forcer un cours gratuit en retournant false.

**[ÉCRAN — screencast éditeur de code]**

[Montre les filtres du dashboard]

Les filtres du dashboard — on les a déjà vus dans la leçon 16.2 :

tutor_dashboard/nav_items — personnaliser le menu.

tutor_dashboard/permalinks — modifier les URLs.

**[ÉCRAN — screencast éditeur de code]**

[Montre les filtres de templates et média]

Les filtres de templates et médias :

tutor_lms_should_template_override — retourne true ou false pour autoriser ou bloquer le remplacement de templates. Utile pour désactiver les overrides dans certaines conditions.

tutor_lesson_template — modifier le template utilisé pour une leçon.

tutor_course_thumbnail_size — changer la taille des images de cours. Par défaut, c'est "post-thumbnail". Tu peux la remplacer par une taille custom.

tutor_video_types — définit les formats vidéo acceptés. Par défaut : mp4, webm, ogg.

tutor_video_stream_is_public — contrôle si les vidéos sont accessibles publiquement ou réservées aux inscrits.

**[ÉCRAN — screencast éditeur de code]**

[Montre les filtres REST API]

Et enfin, les filtres REST API :

tutor/api/get_courses — modifie les résultats retournés par l'API.

tutor_rest_course_query_args — personnalise les paramètres de requête de l'API. Utile si tu développes un front-end découplé.

**[TRANSITION — face caméra]**

La recommandation schoolsWP : les filtres les plus utiles au quotidien sont tutor_courses_base_slug pour franciser les URLs, tutor_login_redirect_url pour contrôler la navigation, et tutor_dashboard/nav_items pour adapter l'interface. Commence par ceux-là. Et rappelle-toi : un filtre qui ne retourne rien, c'est un bug garanti. Toujours retourner une valeur.

---

**Points clés** :
- Filter hooks = modifier des données (apply_filters / add_filter)
- Toujours retourner une valeur — sinon la fonctionnalité casse
- 48+ filtres disponibles couvrant : auth, cours, monétisation, dashboard, templates, API
- tutor_courses_base_slug : changer "courses" en "formations" dans les URLs
- tutor_login_redirect_url : rediriger après connexion
- tutor_dashboard/nav_items : personnaliser le menu du dashboard
- get_tutor_course_price : modifier l'affichage du prix

**Mots-clés SEO** : TutorLMS filter hooks, filtres TutorLMS développeur, apply_filters TutorLMS, personnaliser prix cours TutorLMS

---

### Leçon 16.5 — REST API

**Durée** : 7 min
**Type** : Vidéo HeyGen
**Écran** : Face caméra pour intro/conclusion, screencast navigateur (requêtes API) + éditeur de code
**Source** : doc developer-documentation/rest-api

---

**[INTRO — face caméra]**

TutorLMS expose une REST API basée sur WordPress. Ça veut dire que tu peux interroger tes cours, leçons, quiz et utilisateurs via des requêtes HTTP standard — en JSON. C'est utile pour développer une application mobile, un dashboard externe, ou intégrer TutorLMS avec un outil tiers. Dans cette leçon, on explore les endpoints disponibles et on fait nos premières requêtes.

**[ÉCRAN — screencast navigateur]**

[Montre une requête GET dans le navigateur ou un outil comme Postman]

L'API TutorLMS est accessible à l'adresse : ton-site.com/wp-json/tutor/v1/

C'est le namespace. Tous les endpoints partent de là. Et comme c'est basé sur la REST API WordPress, l'authentification fonctionne de la même manière — cookies, application passwords, ou JWT si tu as un plugin dédié.

Point important : en version gratuite de TutorLMS, seules les requêtes en lecture (GET) sont disponibles. Les opérations d'écriture nécessitent TutorLMS Pro.

**[ÉCRAN — screencast Postman ou navigateur]**

[Requête GET /wp-json/tutor/v1/courses]

Premier endpoint : la liste des cours.

GET /wp-json/tutor/v1/courses

Ça retourne un tableau JSON avec tous les cours publiés. Tu peux filtrer avec des paramètres :

- order : asc ou desc
- orderby : date, title, etc.
- paged : pour la pagination
- tags : filtrer par tags
- categories : filtrer par catégories de cours

Exemple : /wp-json/tutor/v1/courses?orderby=title&order=asc&categories=lms

**[ÉCRAN — screencast Postman]**

[Requête GET /wp-json/tutor/v1/courses/123]

Pour un cours spécifique :

GET /wp-json/tutor/v1/courses/{course_id}

Remplace {course_id} par l'ID du cours. Tu obtiens toutes les métadonnées : titre, description, prix, instructeur, niveau, durée, nombre d'inscrits.

**[ÉCRAN — screencast Postman]**

[Requêtes sur les topics et leçons]

Pour récupérer la structure d'un cours — les topics et leurs leçons :

GET /wp-json/tutor/v1/topics?course_id=123

Ça retourne les topics (sections) du cours. Ensuite, pour les leçons d'un topic :

GET /wp-json/tutor/v1/lessons?topic_id=456

**[ÉCRAN — screencast Postman]**

[Montre les endpoints quiz, rating, annonces]

Les autres endpoints disponibles :

GET /wp-json/tutor/v1/quiz/{topic_id} — les quiz d'un topic.

GET /wp-json/tutor/v1/quiz-question-answer/{quiz_id} — les questions et réponses d'un quiz.

GET /wp-json/tutor/v1/course-annoucement/{course_id} — les annonces d'un cours. Note le "ou" dans "annoucement" — c'est une faute de frappe dans l'API, mais c'est le endpoint officiel.

GET /wp-json/tutor/v1/course-rating/{course_id} — les notes et avis.

GET /wp-json/tutor/v1/author-information/{author_id} — les infos de l'instructeur.

GET /wp-json/tutor/v1/course-contents/{course_id} — le contenu complet du cours (topics + leçons + quiz en une seule requête).

**[ÉCRAN — screencast éditeur de code]**

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

Et rappelle-toi les filtres de la leçon précédente : tutor/api/get_courses et tutor_rest_course_query_args te permettent de modifier les réponses de l'API côté serveur — ajouter des champs, filtrer les résultats, limiter l'accès.

**[TRANSITION — face caméra]**

La recommandation schoolsWP : l'endpoint le plus utile, c'est /course-contents/{course_id}. Il te donne toute la structure d'un cours en une seule requête — topics, leçons, quiz. C'est celui que tu utiliseras pour les intégrations externes. Et pense à sécuriser tes endpoints — n'expose pas les données sensibles sans authentification.

---

**Points clés** :
- API basé sur WordPress REST API, namespace /wp-json/tutor/v1/
- Version gratuite : lecture seule (GET). Écriture : TutorLMS Pro
- 10 endpoints : courses, topics, lessons, quiz, ratings, announcements, author, course-contents
- Authentification : cookies, Application Passwords, ou JWT
- Filtrable côté serveur avec tutor/api/get_courses et tutor_rest_course_query_args
- Endpoint le plus utile : /course-contents/{course_id} (structure complète)

**Mots clés SEO** : TutorLMS REST API, API cours TutorLMS, endpoints TutorLMS, wp-json tutor v1, intégration API LMS WordPress

---

### Leçon 16.6 — Custom Payment Gateways

**Durée** : 8 min
**Type** : Vidéo HeyGen
**Écran** : Face caméra pour intro/conclusion, screencast éditeur de code
**Source** : doc developer-documentation/custom-payment-gateways

---

**[INTRO — face caméra]**

TutorLMS supporte Stripe et PayPal nativement. Mais si ton marché utilise une autre passerelle — Mollie en Europe, Razorpay en Inde, ou un système bancaire local — tu peux créer ta propre passerelle de paiement. TutorLMS fournit un framework avec des classes à étendre et une structure de plugin prête à l'emploi. C'est du développement avancé, mais le processus est bien documenté.

**[ÉCRAN — screencast navigateur]**

[Montre la page de documentation et le lien de téléchargement du plugin démo]

Point de départ : la documentation officielle fournit un plugin de démonstration appelé "CustomPayment". C'est un squelette complet que tu dupliques et que tu adaptes à ta passerelle.

Télécharge-le, dézippe-le, et regarde la structure.

**[ÉCRAN — screencast éditeur de code]**

[Montre l'arborescence du plugin démo]

Le plugin contient 5 fichiers principaux :

1. CustomPaymentConfig.php — la configuration (clés API, environnement)
2. CustomPaymentGateway.php — la classe principale qui lie le tout
3. Init.php — l'initialisation du plugin
4. Custompayment.php — la logique de paiement
5. composer.json — les dépendances

Tu renommes tout avec le nom de ta passerelle. Par exemple, si tu intègres Mollie : MollieConfig.php, MollieGateway.php, etc.

**[ÉCRAN — screencast éditeur de code]**

[Ouvre CustomPaymentConfig.php]

Premier fichier à modifier : la configuration. La classe étend BaseConfig et implémente ConfigContract — deux classes fournies par TutorLMS.

```php
namespace CustomPayment;

use Ollyo\PaymentHub\Core\Payment\BaseConfig;
use Ollyo\PaymentHub\Contracts\Payment\ConfigContract;
```

Tu définis tes propriétés — les champs nécessaires pour ta passerelle :

```php
private $environment;
private $public_key;
private $secret_key;
private $client_id;
protected $name = 'custompayment';
```

Trois méthodes clés à implémenter :

get_custompayment_config_keys() — retourne un tableau qui mappe les clés de configuration.

is_configured() — vérifie que tous les champs obligatoires sont remplis. Si un champ manque, la passerelle ne s'active pas.

createConfig() — initialise la configuration avec les valeurs saisies par l'admin.

**[ÉCRAN — screencast éditeur de code]**

[Ouvre CustomPaymentGateway.php]

Deuxième fichier : la classe Gateway. Elle étend GatewayBase et définit trois propriétés :

$dir_name — le nom du dossier racine de ton plugin.
$config_class — la référence vers ta classe de config.
$payment_class — la référence vers ta classe de paiement.

Et quatre méthodes getter : get_root_dir_name(), get_payment_class(), get_config_class(), get_autoload_file().

C'est le chef d'orchestre — il connecte la config, le traitement du paiement, et l'autoloader.

**[ÉCRAN — screencast éditeur de code]**

[Ouvre Custompayment.php]

Troisième fichier : la logique de paiement. C'est ici que tu codes l'interaction avec l'API de ta passerelle. Tu dois implémenter :

- La création du paiement (envoyer la requête à l'API)
- La gestion du callback/webhook (recevoir la confirmation)
- La vérification de la transaction (s'assurer que le paiement est valide)

C'est spécifique à chaque passerelle. Stripe utilise des PaymentIntents, Mollie utilise des Payments — l'implémentation varie.

**[ÉCRAN — screencast éditeur de code]**

[Montre Init.php et composer.json]

Init.php : le point d'entrée du plugin. Il enregistre ta passerelle auprès de TutorLMS. Et composer.json gère les dépendances — le SDK de ta passerelle, par exemple.

**[ÉCRAN — screencast WordPress admin]**

[Montre la passerelle qui apparaît dans les réglages TutorLMS]

Une fois le plugin activé, ta passerelle apparaît dans les réglages de TutorLMS, à côté de Stripe et PayPal. L'admin remplit les champs que tu as définis dans la config — clés API, mode sandbox/production — et la passerelle est opérationnelle.

**[TRANSITION — face caméra]**

La recommandation schoolsWP : avant de coder ta propre passerelle, vérifie qu'il n'existe pas déjà un plugin tiers. Mollie, Razorpay et plusieurs autres ont des plugins WooCommerce — et si tu utilises WooCommerce comme moteur de paiement pour TutorLMS, tu n'as pas besoin de coder quoi que ce soit. La passerelle custom, c'est pour le eCommerce natif de TutorLMS quand aucune alternative n'existe.

---

**Points clés** :
- Plugin démo "CustomPayment" à télécharger et adapter
- 5 fichiers : Config, Gateway, Init, Payment, composer.json
- Config : étend BaseConfig, implémente ConfigContract, définit les clés API
- Gateway : étend GatewayBase, connecte config + payment + autoloader
- Payment : logique spécifique (création paiement, webhook, vérification)
- La passerelle apparaît automatiquement dans les réglages TutorLMS
- Alternative : utiliser WooCommerce + plugin de passerelle existant

**Mots clés SEO** : TutorLMS custom payment gateway, passerelle paiement TutorLMS, créer passerelle paiement LMS, TutorLMS PaymentHub, GatewayBase TutorLMS

---

### Leçon 16.7 — Custom Fields

**Durée** : 7 min
**Type** : Vidéo HeyGen
**Écran** : Face caméra pour intro/conclusion, screencast éditeur de code + Course Builder
**Source** : doc developer-documentation/register-custom-fields

---

**[INTRO — face caméra]**

TutorLMS couvre les champs essentiels d'un cours — titre, description, prix, niveau. Mais chaque projet a ses spécificités. Peut-être que tu as besoin d'un champ "Contenu SEO" pour tes formateurs, d'un champ "Prérequis techniques" sur les leçons, ou d'un champ "Difficulté estimée" sur les quiz. TutorLMS expose une fonction JavaScript — registerField — qui te permet d'injecter des champs personnalisés directement dans le Course Builder. Et côté PHP, tu sauvegardes et tu affiches les données.

**[ÉCRAN — screencast éditeur de code]**

[Montre la fonction registerField en JavaScript]

La fonction d'enregistrement est en JavaScript. Elle s'appelle Tutor.CourseBuilder.Basic.registerField. Tu l'appelles avec deux arguments : l'emplacement (slot) et la configuration du champ.

```javascript
Tutor.CourseBuilder.Basic.registerField("after_description", {
    name: "seo_content",
    type: "textarea",
    label: "Contenu SEO"
});
```

"after_description" — c'est le slot, l'endroit où le champ apparaît. "seo_content" — c'est l'identifiant unique du champ.

**[ÉCRAN — screencast éditeur de code]**

[Montre la liste des slots disponibles]

Les slots disponibles — où tu peux placer tes champs :

Pour les cours (Basics) :
- after_description — après la description du cours
- after_settings — après les réglages du cours

Pour les leçons (Lesson) :
- after_description — après la description de la leçon
- bottom_of_sidebar — en bas de la barre latérale

Pour les quiz (Quiz) :
- after_question_description — après la description d'une question
- bottom_of_question_sidebar — en bas de la barre latérale de la question

Pour les devoirs (Assignment) :
- after_description — après la description
- bottom_of_sidebar — en bas de la barre latérale

**[ÉCRAN — screencast éditeur de code]**

[Montre les types de champs disponibles]

Les types de champs disponibles : text, number, password, textarea, select, radio, checkbox, switch, date, time, image, video, uploader, WPEditor.

Exemple avec un select :

```javascript
Tutor.CourseBuilder.Basic.registerField("after_settings", {
    name: "course_difficulty",
    type: "select",
    label: "Difficulté estimée",
    options: [
        { value: "debutant", label: "Débutant" },
        { value: "intermediaire", label: "Intermédiaire" },
        { value: "avance", label: "Avancé" },
        { value: "expert", label: "Expert" }
    ]
});
```

Tu peux aussi ajouter une propriété "priority" pour contrôler l'ordre d'affichage, et "rules" pour la validation — ça utilise React Hook Form.

**[ÉCRAN — screencast éditeur de code]**

[Montre le code PHP de sauvegarde]

Côté JavaScript, le champ s'affiche. Mais il faut aussi sauvegarder la donnée. Ça se fait en PHP, avec un hook WordPress classique :

```php
add_action('save_post_courses', 'save_custom_course_meta');

function save_custom_course_meta($post_id) {
    if (isset($_POST['seo_content'])) {
        $seo_content = sanitize_textarea_field($_POST['seo_content']);
        update_post_meta($post_id, 'tlcf_seo_content', $seo_content);
    }
}
```

Deux règles : toujours sanitiser les données avant de les sauvegarder (sanitize_text_field, sanitize_textarea_field). Et utiliser un préfixe pour tes meta keys — ici "tlcf_" — pour éviter les conflits.

Les hooks de sauvegarde selon le type de contenu :
- save_post_courses — pour les cours
- save_post_lesson — pour les leçons
- save_post_tutor_assignments — pour les devoirs

**[ÉCRAN — screencast éditeur de code]**

[Montre l'affichage des données en front-end]

Pour afficher les données en front-end, utilise un filtre :

```php
add_filter('tutor_course_details_response', function($response) {
    $seo_content = get_post_meta($response->ID, 'tlcf_seo_content', true);
    $response->seo_content = $seo_content;
    return $response;
});
```

Ça ajoute ton champ personnalisé à la réponse du cours — que ce soit dans les templates ou via l'API REST.

Les filtres disponibles par type :
- tutor_course_details_response — cours
- tutor_lesson_details_response — leçons
- tutor_quiz_details_response — quiz

**[ÉCRAN — screencast Course Builder]**

[Montre le champ personnalisé dans le Course Builder]

Résultat dans le Course Builder : ton champ "Contenu SEO" apparaît sous la description du cours, avec un textarea éditable. Le formateur le remplit, il est sauvegardé, et il est accessible en front-end.

**[TRANSITION — face caméra]**

La recommandation schoolsWP : les custom fields sont particulièrement utiles pour les informations spécifiques à ton domaine — niveau de certification, durée estimée en heures, code de formation CPF. Mets le JavaScript dans un fichier séparé enqueué via wp_enqueue_script, pas en inline. Et côté PHP, sanitise toujours les données — c'est une règle de sécurité non-négociable.

---

**Points clés** :
- registerField() en JavaScript pour ajouter des champs dans le Course Builder
- Slots : after_description, after_settings (cours), bottom_of_sidebar (leçons/quiz)
- 14 types de champs : text, select, checkbox, date, WPEditor, etc.
- Sauvegarde PHP via save_post_courses + update_post_meta
- Affichage via filtres : tutor_course_details_response, tutor_lesson_details_response
- Toujours sanitiser les données et préfixer les meta keys
- JavaScript dans un fichier séparé, pas en inline

**Mots clés SEO** : TutorLMS custom fields, champs personnalisés TutorLMS, registerField TutorLMS, Course Builder custom fields, méta données cours TutorLMS

---

### Leçon 16.8 — Quiz final Module 16 + Certification

**Durée** : ~10 min (12 questions)
**Type** : Quiz TutorLMS
**Seuil de réussite** : 80%
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
Quel filtre permet de personnaliser les éléments du menu du dashboard TutorLMS ?

- A) tutor_dashboard_menu_items
- B) tutor_dashboard/nav_items ✓
- C) tutor_nav_menu_filter
- D) tutor_sidebar_items

**Explication** : Le filtre tutor_dashboard/nav_items donne accès au tableau complet des onglets du dashboard.

---

**Question 3**
Quelle est la différence fondamentale entre un action hook et un filter hook ?

- A) Les actions sont pour le front-end, les filtres pour le back-end
- B) Les actions exécutent du code, les filtres modifient et retournent des données ✓
- C) Les actions sont plus rapides que les filtres
- D) Les filtres ne peuvent pas recevoir de paramètres

**Explication** : Un action hook exécute du code à un moment précis (do_action). Un filter hook reçoit une valeur, la modifie et la retourne (apply_filters). Oublier le return dans un filtre casse la fonctionnalité.

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
Dans la création d'une passerelle de paiement custom, quelle classe la Config doit-elle étendre ?

- A) PaymentConfig
- B) BaseConfig ✓
- C) GatewayConfig
- D) TutorConfig

**Explication** : La classe de configuration étend BaseConfig et implémente ConfigContract, deux classes fournies par le PaymentHub de TutorLMS.

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
Dans TutorLMS, quel est l'ordre hiérarchique du contenu d'un cours ?

- A) Cours → Leçons → Topics → Quiz
- B) Cours → Topics → Leçons/Quiz ✓
- C) Cours → Chapitres → Sections → Leçons
- D) Cours → Modules → Leçons → Exercices

**Explication** : La hiérarchie TutorLMS est : Cours (Course) → Topics (sections) → Leçons et Quiz (contenus). Un topic regroupe plusieurs leçons et/ou quiz.

---

**Question 8** *(question transversale M6-M8)*
Quel format de certificat TutorLMS offre le plus de liberté de design ?

- A) Certificat PDF standard
- B) Certificat HTML basique
- C) Certificat drag & drop builder ✓
- D) Certificat généré par code PHP

**Explication** : Le certificat drag & drop builder (disponible avec TutorLMS Pro) permet de placer librement les éléments — texte, images, QR code, logo — sur un canvas visuel.

---

**Question 9** *(question transversale M9-M11)*
Quelle est la recommandation schoolsWP pour la vérification email à l'inscription étudiant ?

- A) La désactiver pour simplifier l'inscription
- B) L'activer uniquement pour les cours payants
- C) Toujours l'activer pour filtrer les faux comptes ✓
- D) Utiliser un CAPTCHA à la place

**Explication** : La vérification email filtre les inscriptions fantômes et améliore la qualité de la liste d'élèves. schoolsWP recommande de toujours l'activer.

---

**Question 10** *(question transversale M12-M15)*
À partir de combien de vidéos schoolsWP recommande-t-il de passer à BunnyNet pour l'hébergement ?

- A) 10 vidéos
- B) 25 vidéos
- C) 50 vidéos ✓
- D) 100 vidéos

**Explication** : schoolsWP recommande BunnyNet dès 50 vidéos. En dessous, YouTube non-listé ou Vimeo gratuit peuvent suffire. BunnyNet coûte 5 à 15 dollars par mois pour 50 à 100 vidéos.

---

**Question 11**
Quel hook TutorLMS te permet d'ajouter des champs dans le formulaire d'inscription instructeur ?

- A) tutor_instructor_form_fields
- B) tutor_add_new_instructor_form_fields_after ✓
- C) tutor_registration_extra_fields
- D) tutor_instructor_signup_hook

**Explication** : Les hooks tutor_add_new_instructor_form_fields_before et after permettent d'injecter des champs HTML supplémentaires dans le formulaire d'inscription instructeur.

---

**Question 12**
Pourquoi schoolsWP recommande-t-il de ne jamais modifier les fichiers du plugin TutorLMS directement ?

- A) Le code est chiffré et ne peut pas être modifié
- B) Les modifications sont écrasées à chaque mise à jour du plugin ✓
- C) Ça viole la licence du plugin
- D) Le plugin détecte les modifications et se désactive

**Explication** : Toute modification directe des fichiers du plugin est écrasée quand TutorLMS est mis à jour. Les overrides dans un child theme et les hooks dans un plugin custom sont les seules méthodes pérennes.

---

**Fin du Module 16 — Développeur (avancé)**

**Fin de la formation "Maîtriser TutorLMS"**

Résumé du module :
- Override templates : copier dans child-theme/tutor/, modifier, les mises à jour ne cassent rien
- Dashboard : filtre tutor_dashboard/nav_items pour personnaliser le menu
- Action hooks : exécuter du code aux moments clés (inscription, création de cours, quiz)
- Filter hooks : modifier les données (prix, URLs, menu, templates) — toujours retourner une valeur
- REST API : 10 endpoints en lecture, namespace /wp-json/tutor/v1/
- Custom Payment Gateways : framework BaseConfig + GatewayBase pour intégrer toute passerelle
- Custom Fields : registerField() en JS + save_post hooks en PHP

Recommandation finale schoolsWP : utilise toujours un child theme pour les overrides de templates, et un plugin custom pour les hooks et champs personnalisés. Ne touche jamais aux fichiers du plugin. C'est la règle numéro un du développement WordPress propre.

Durée totale estimée du module : ~52 minutes (7 leçons + quiz)
