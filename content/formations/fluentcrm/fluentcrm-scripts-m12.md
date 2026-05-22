# Scripts vidéo — Module 12 : Conditional sections et personnalisation

**Formation** : Maîtriser FluentCRM
**Module** : M12 — Conditional sections et personnalisation (Premium)
**Leçons** : 6 vidéos + 1 exercice + 1 quiz
**Durée totale** : ~45 min
**Prérequis** : M11 (recurring campaigns et newsletters)
**Date** : 2026-03-23

---

### Leçon 12.1 — Comprends les conditional sections : un email, plusieurs versions

**Durée** : 5 min
**Type** : Vidéo HeyGen
**Écran** : Face caméra pour intro/conclusion, screencast FluentCRM

---

**[INTRO — face caméra]**

Tu envoies le même email à toute ta liste. Même contenu, même CTA, même offre — que le contact soit débutant ou expert, gratuit ou premium. Résultat : ton message parle à tout le monde en général, et à personne en particulier. Les conditional sections de FluentCRM changent ça. Un seul email, mais des blocs qui s'affichent ou se masquent selon le profil du contact. Dans cette leçon, tu comprends le principe et tu vois pourquoi c'est un levier de conversion concret.

**[ÉCRAN — slide "Un email, plusieurs versions"]**

[Montre un schéma : 1 email à gauche, 3 versions à droite selon le profil]

Étape 1 : le concept est simple. Tu rédiges un seul email dans FluentCRM. À l'intérieur, tu places des blocs conditionnels. Chaque bloc a une règle : "affiche ce contenu SI le contact remplit telle condition". Le contact débutant voit un CTA vers la formation gratuite. Le contact avancé voit un CTA vers la formation premium. Le contact qui a déjà acheté voit un message de fidélité. Un seul email à maintenir, trois expériences différentes.

**[ÉCRAN — screencast FluentCRM > éditeur email]**

[Ouvre un email existant dans l'éditeur visuel]

Étape 2 : dans l'éditeur email de FluentCRM, tu vas trouver l'option "Conditional Section" ou "Conditional Block". C'est un bloc spécial qui enveloppe du contenu et lui applique une condition d'affichage. Si la condition est vraie, le contenu s'affiche. Si elle est fausse, le bloc disparaît complètement — le contact ne voit rien, pas de trou, pas d'espace vide.

**[ÉCRAN — slide "Conditions disponibles"]**

[Montre une liste des conditions possibles]

Étape 3 : quelles conditions peux-tu utiliser ? FluentCRM te donne accès à tout ce qu'il sait sur le contact.

Par tags : le contact a le tag "premium" ou "débutant".
Par listes : le contact est dans la liste "Étudiants LMS" ou "Prospects CRM".
Par champs personnalisés : le contact a un champ "niveau" égal à "avancé".
Par statut : le contact est abonné, désabonné, en attente.

Tu peux combiner ces conditions — par exemple : tag "premium" ET liste "Étudiants LMS".

**[ÉCRAN — slide "Exemple concret schoolsWP"]**

[Montre un email avec 3 blocs conditionnels annotés]

Étape 4 : exemple concret. Tu envoies ta newsletter hebdomadaire. Le corps de l'email est identique pour tout le monde — tes derniers articles. Mais le CTA en bas change selon le profil.

Bloc conditionnel 1 — si tag "débutant" : "Découvre la formation gratuite pour bien démarrer avec WordPress."
Bloc conditionnel 2 — si tag "avancé" : "Passe au niveau supérieur avec la formation premium TutorLMS."
Bloc conditionnel 3 — si tag "client" : "Merci pour ta confiance. Voici les nouveautés réservées aux membres."

Trois expériences, un seul email à gérer.

**[TRANSITION — face caméra]**

Les conditional sections te permettent de personnaliser sans multiplier les campagnes. Un email, plusieurs versions selon le profil. Dans la prochaine leçon, tu crées tes premières sections conditionnelles dans l'éditeur email de FluentCRM.

---

**Points clés** :
- Conditional section = bloc qui s'affiche ou se masque selon une condition
- Conditions basées sur : tags, listes, champs personnalisés, statut
- Le contact ne voit jamais les blocs masqués — pas d'espace vide
- Cas d'usage principal : CTA différent selon le niveau ou le statut client
- Un seul email à maintenir au lieu de plusieurs campagnes

**Mots clés SEO** : FluentCRM conditional sections, personnalisation email WordPress, contenu conditionnel FluentCRM, email dynamique FluentCRM

---

### Leçon 12.2 — Crée des sections conditionnelles dans tes emails

**Durée** : 7 min
**Type** : Vidéo HeyGen
**Écran** : Face caméra pour intro/conclusion, screencast FluentCRM éditeur email

---

**[INTRO — face caméra]**

Tu connais le principe des conditional sections. Maintenant tu les crées. L'objectif : un email avec un bloc visible uniquement pour les contacts tagués "premium" et un autre bloc pour les contacts sans ce tag. Sept étapes, et ton premier email personnalisé est prêt.

**[ÉCRAN — screencast FluentCRM > Email Campaigns > Create Campaign]**

[Crée une nouvelle campagne classique]

Étape 1 : crée une nouvelle campagne email. Donne-lui un nom interne — par exemple "Newsletter Perso M12". Configure l'objet : "Tes ressources de la semaine, {{contact.first_name}}". On travaille sur une campagne classique pour tester — tu pourras appliquer la même technique dans une recurring campaign ensuite.

**[ÉCRAN — screencast éditeur visuel]**

[Ouvre l'éditeur et ajoute un bloc texte classique]

Étape 2 : commence par le contenu commun. Ajoute un bloc texte en haut avec ton introduction — identique pour tout le monde. Par exemple : "Bonjour {{contact.first_name}}, voici ce que j'ai préparé pour toi cette semaine." Ce bloc n'a aucune condition — tout le monde le voit.

[Montre l'ajout d'un deuxième bloc texte avec du contenu article]

Étape 3 : ajoute le corps de ta newsletter — tes derniers articles, un récap, ce que tu veux. Ce contenu commun constitue la base de ton email.

**[ÉCRAN — screencast ajout du bloc conditionnel]**

[Montre comment insérer une conditional section]

Étape 4 : maintenant, ajoute ta première section conditionnelle. Dans l'éditeur, cherche l'option "Conditional Block" ou le bouton pour ajouter une condition à un bloc. Sélectionne-le et place-le sous ton contenu commun.

[Montre le panneau de configuration de la condition]

Étape 5 : configure la condition. Sélectionne "Contact Tags" dans le type de condition. Puis choisis "Has Tag" et sélectionne le tag "premium". Ce bloc ne s'affichera que pour les contacts qui portent ce tag. À l'intérieur, rédige ton CTA premium : "Tu as accès à la formation avancée TutorLMS — découvre les nouveaux modules cette semaine." Ajoute un bouton qui pointe vers ta page de formation.

**[ÉCRAN — screencast ajout du deuxième bloc conditionnel]**

[Ajoute un second bloc conditionnel]

Étape 6 : ajoute un deuxième bloc conditionnel juste en dessous. Cette fois, la condition est "Does NOT have Tag" > "premium". À l'intérieur, rédige un CTA pour les contacts gratuits : "Prêt à aller plus loin ? Découvre la formation premium pour maîtriser WordPress de A à Z." Bouton vers ta page de vente.

[Montre les deux blocs conditionnels côte à côte dans l'éditeur]

Tu vois maintenant les deux blocs dans l'éditeur. Toi tu vois tout. Mais chaque contact ne verra qu'un seul des deux blocs — celui dont la condition correspond à son profil.

**[ÉCRAN — screencast prévisualisation]**

[Montre la prévisualisation avec un contact premium, puis un contact gratuit]

Étape 7 : prévisualise ton email. FluentCRM te permet de voir le rendu pour différents contacts. Sélectionne un contact avec le tag "premium" — tu vois le CTA premium. Sélectionne un contact sans ce tag — tu vois le CTA gratuit. Vérifie que le rendu est propre dans les deux cas — pas d'espace vide, pas de décalage.

**[TRANSITION — face caméra]**

Ton premier email avec des blocs conditionnels est prêt. Un seul email, deux expériences. Tu peux ajouter autant de blocs conditionnels que nécessaire — par tag, par liste, par champ personnalisé. Dans la prochaine leçon, on applique le même principe aux pages WordPress.

---

**Points clés** :
- Contenu commun en haut (intro, articles) — visible par tout le monde
- Blocs conditionnels en bas — chacun avec sa propre règle
- Condition "Has Tag" / "Does NOT have Tag" pour cibler par profil
- Toujours prévisualiser avec plusieurs profils de contacts
- Technique applicable aux campagnes classiques et recurring

**Mots clés SEO** : créer conditional section FluentCRM, email conditionnel WordPress, bloc dynamique FluentCRM, personnalisation CTA email

---

### Leçon 12.3 — Crée des sections conditionnelles sur tes pages WordPress

**Durée** : 6 min
**Type** : Vidéo HeyGen
**Écran** : Face caméra pour intro/conclusion, screencast WordPress + FluentCRM

---

**[INTRO — face caméra]**

Les conditional sections ne sont pas limitées aux emails. FluentCRM te permet aussi de personnaliser tes pages WordPress selon le profil du visiteur. Un contact connecté avec le tag "premium" voit un contenu différent d'un visiteur anonyme. Ta page d'accueil, ta page de formation, ta page de vente — chacune peut s'adapter au visiteur. Dans cette leçon, tu mets ça en place.

**[ÉCRAN — screencast WordPress > page d'accueil en édition]**

[Ouvre l'éditeur de page WordPress]

Étape 1 : ouvre la page que tu veux personnaliser dans l'éditeur WordPress. On va travailler sur la page d'accueil pour l'exemple. FluentCRM ajoute des shortcodes conditionnels que tu peux utiliser directement dans tes pages.

**[ÉCRAN — slide "Shortcodes conditionnels FluentCRM"]**

[Montre la syntaxe des shortcodes]

Étape 2 : FluentCRM fournit des shortcodes pour afficher du contenu selon le profil du contact connecté. La syntaxe de base :

`[fluentcrm_conditional]` — ouvre la section conditionnelle.
Attributs : `tag`, `list`, `status`, `contact_type`.

Par exemple : `[fluentcrm_conditional tag="premium"]Contenu réservé aux premium[/fluentcrm_conditional]`. Seuls les contacts connectés qui portent le tag "premium" verront ce contenu.

**[ÉCRAN — screencast WordPress éditeur]**

[Ajoute un bloc HTML ou shortcode dans la page]

Étape 3 : dans ta page d'accueil, ajoute un bloc "Shortcode" ou "HTML personnalisé". Insère le shortcode conditionnel. Par exemple, un message de bienvenue personnalisé :

Pour les contacts premium : `[fluentcrm_conditional tag="premium"]Bienvenue, {{contact.first_name}}. Tes cours premium t'attendent.[/fluentcrm_conditional]`

Pour les contacts sans tag premium : `[fluentcrm_conditional not_tag="premium"]Découvre nos formations pour maîtriser WordPress.[/fluentcrm_conditional]`

Pour les visiteurs anonymes (non identifiés) : le contenu par défaut de la page, sans shortcode.

[Montre les trois blocs dans l'éditeur]

Étape 4 : place ces blocs dans ta page. L'ordre compte. Le shortcode vérifie la condition et affiche ou masque le contenu. Si le visiteur n'est pas un contact FluentCRM identifié, aucun shortcode conditionnel ne s'affiche — seul le contenu standard de la page reste visible.

**[ÉCRAN — screencast test en front-end]**

[Montre la page avec un compte premium, puis un compte gratuit, puis en anonyme]

Étape 5 : teste ta page. Connecte-toi avec un compte qui a le tag "premium" — tu vois le message premium. Déconnecte-toi et connecte-toi avec un compte sans le tag — tu vois le message standard. Visite la page en anonyme — tu vois uniquement le contenu de base.

**[ÉCRAN — slide "Cas d'usage concrets"]**

[Montre 3 scénarios]

Étape 6 : trois cas d'usage concrets pour tes pages WordPress.

Page d'accueil personnalisée : message de bienvenue différent selon le niveau.
Page de formation : afficher les modules premium uniquement aux contacts qui ont acheté.
Page de vente : masquer le bouton d'achat pour les clients existants et afficher un message "Tu as déjà accès".

**[TRANSITION — face caméra]**

Tes pages WordPress s'adaptent maintenant au profil du visiteur. Combine ça avec les emails conditionnels et tu obtiens une expérience cohérente du premier email à la navigation sur ton site. Prochaine leçon : les merge codes avancés pour aller encore plus loin dans la personnalisation.

---

**Points clés** :
- Shortcodes FluentCRM pour personnaliser les pages WordPress
- Syntaxe : `[fluentcrm_conditional tag="xxx"]contenu[/fluentcrm_conditional]`
- Attributs disponibles : tag, not_tag, list, status, contact_type
- Visiteurs anonymes ne voient que le contenu standard (sans shortcode)
- Cas d'usage : page d'accueil, page formation, page de vente

**Mots clés SEO** : FluentCRM shortcode conditionnel, personnalisation page WordPress FluentCRM, contenu dynamique WordPress, page personnalisée CRM

---

### Leçon 12.4 — Merge codes avancés : data transformers et formatage

**Durée** : 7 min
**Type** : Vidéo HeyGen
**Écran** : Face caméra pour intro/conclusion, screencast FluentCRM éditeur email

---

**[INTRO — face caméra]**

Tu utilises déjà `{{contact.first_name}}` dans tes emails. C'est un merge code basique — il insère le prénom du contact. Mais FluentCRM va plus loin. Les data transformers te permettent de formater ces données : mettre une majuscule, formater une date, transformer du texte. Dans cette leçon, tu découvres les merge codes avancés et les transformers qui rendent tes emails plus propres et plus professionnels.

**[ÉCRAN — slide "Merge codes — rappel"]**

[Montre les merge codes de base]

Étape 1 : rappel rapide. Un merge code est un placeholder qui est remplacé par la donnée du contact au moment de l'envoi. Les plus courants :

`{{contact.first_name}}` — prénom
`{{contact.last_name}}` — nom
`{{contact.email}}` — adresse email
`{{contact.id}}` — identifiant unique
`{{contact.status}}` — statut (subscribed, unsubscribed…)

Tu les connais déjà. Maintenant on passe au niveau suivant.

**[ÉCRAN — screencast FluentCRM > éditeur email]**

[Ouvre un email et montre le bouton d'insertion de merge codes]

Étape 2 : dans l'éditeur email, clique sur le bouton d'insertion de merge codes — souvent représenté par des accolades `{}`. FluentCRM affiche la liste complète des champs disponibles. Tu y trouves les champs standard, les champs personnalisés que tu as créés, et les champs système.

[Montre la liste déroulante des merge codes disponibles]

Étape 3 : au-delà des champs contact, tu as accès à d'autres données. Les informations de ton site : `{{wp.site_url}}`, `{{wp.site_name}}`. Les dates : `{{current.date}}`, `{{current.year}}`. Ces merge codes sont utiles dans les footers, les mentions légales, ou les emails automatisés.

**[ÉCRAN — slide "Data transformers"]**

[Montre un tableau des transformers disponibles]

Étape 4 : les data transformers. C'est là où ça devient puissant. Un transformer modifie la donnée avant de l'afficher. La syntaxe : `{{contact.first_name | transformer}}`.

Les transformers les plus utiles :

`ucfirst` — première lettre en majuscule. `{{contact.first_name | ucfirst}}` transforme "michael" en "Michael".
`upper` — tout en majuscules. `{{contact.last_name | upper}}` transforme "kihl" en "KIHL".
`lower` — tout en minuscules. Utile pour normaliser les emails dans le contenu visible.
`date_format:"d/m/Y"` — formate une date. `{{contact.date_of_birth | date_format:"d/m/Y"}}` transforme "1990-05-15" en "15/05/1990".

**[ÉCRAN — screencast application dans un email]**

[Montre un email avec des merge codes transformer]

Étape 5 : application concrète. Tu rédiges un email de bienvenue. Au lieu de `Bonjour {{contact.first_name}}`, tu écris `Bonjour {{contact.first_name | ucfirst}}`. Si le contact a saisi son prénom en minuscules dans le formulaire, l'email affichera quand même une majuscule.

[Montre un deuxième exemple avec une date]

Autre exemple : tu envoies un récap annuel. Tu veux afficher la date d'inscription du contact. `Tu es avec nous depuis le {{contact.created_at | date_format:"d F Y"}}.` Au lieu d'afficher "2024-01-15", l'email affiche "15 January 2024".

**[ÉCRAN — slide "Combiner transformers"]**

[Montre un exemple de chaîne de transformers]

Étape 6 : tu peux chaîner les transformers. `{{contact.first_name | lower | ucfirst}}` — d'abord tout en minuscules, puis première lettre en majuscule. Ça normalise les prénoms saisis n'importe comment : "MICHAEL" devient "Michael", "mIcHaEl" devient "Michael".

**[ÉCRAN — screencast test d'envoi]**

[Montre un email de test envoyé avec les merge codes résolus]

Étape 7 : teste toujours tes merge codes avant l'envoi. Envoie un email de test à toi-même et vérifie que les transformers fonctionnent correctement. Vérifie aussi le rendu quand un champ est vide — on verra comment gérer ça dans la prochaine leçon avec les fallback values.

**[TRANSITION — face caméra]**

Les data transformers rendent tes emails plus propres sans effort de saisie supplémentaire de la part du contact. Majuscules, dates formatées, texte normalisé — tout ça se gère au niveau du merge code. Prochaine étape : que se passe-t-il quand la donnée est vide ? C'est le sujet des fallback values.

---

**Points clés** :
- Merge codes = placeholders remplacés par les données du contact à l'envoi
- Data transformers : ucfirst, upper, lower, date_format
- Syntaxe : `{{contact.field | transformer}}`
- Chaîner les transformers : `{{contact.first_name | lower | ucfirst}}`
- Toujours tester les merge codes avant envoi réel

**Mots clés SEO** : FluentCRM merge codes, data transformers FluentCRM, formatage email dynamique, merge tags WordPress email

---

### Leçon 12.5 — Fallback values : que montrer quand la donnée est vide

**Durée** : 5 min
**Type** : Vidéo HeyGen
**Écran** : Face caméra pour intro/conclusion, screencast FluentCRM éditeur email

---

**[INTRO — face caméra]**

Tu écris "Bonjour {{contact.first_name}}" dans ton email. Le contact n'a pas renseigné son prénom. Résultat : "Bonjour " suivi de rien. Un espace vide, un email qui fait amateur. Les fallback values règlent ce problème. Tu définis une valeur de remplacement qui s'affiche quand la donnée est absente. Dans cette leçon, tu apprends à les configurer correctement.

**[ÉCRAN — slide "Le problème des champs vides"]**

[Montre un email avec un prénom vide — "Bonjour ," — puis un avec fallback — "Bonjour ami,"]

Étape 1 : le problème est fréquent. Tous tes contacts n'ont pas rempli tous les champs. Certains se sont inscrits avec juste une adresse email — pas de prénom, pas de nom, pas de date de naissance. Si tu utilises un merge code qui pointe vers un champ vide, FluentCRM affiche une chaîne vide. L'email a un trou.

**[ÉCRAN — screencast FluentCRM > éditeur email]**

[Montre la syntaxe du fallback dans le merge code]

Étape 2 : la syntaxe du fallback. Tu ajoutes `| default:"valeur"` après le nom du champ.

`{{contact.first_name | default:"ami"}}` — si le prénom est vide, affiche "ami".

Résultat : "Bonjour ami," au lieu de "Bonjour ,". Propre, naturel, sans trou.

[Montre d'autres exemples de fallback]

Étape 3 : tu peux appliquer un fallback à n'importe quel merge code.

`{{contact.company | default:"ton entreprise"}}` — si pas de nom d'entreprise.
`{{contact.phone | default:"non renseigné"}}` — si pas de téléphone (utile dans les récaps de profil).
`{{contact.city | default:"ta ville"}}` — si pas de ville.

Le fallback n'écrase jamais la donnée existante. Si le champ est rempli, c'est la vraie valeur qui s'affiche.

**[ÉCRAN — slide "Combiner fallback et transformer"]**

[Montre la syntaxe combinée]

Étape 4 : tu peux combiner fallback et data transformers. L'ordre compte.

`{{contact.first_name | default:"ami" | ucfirst}}` — si le prénom est vide, affiche "Ami" (avec majuscule). Si le prénom est "michael", affiche "Michael".

La règle : le default s'applique d'abord, puis le transformer formate le résultat — que ce soit la vraie donnée ou le fallback.

**[ÉCRAN — screencast test avec contact sans prénom]**

[Crée un contact test sans prénom, envoie un email de test]

Étape 5 : teste avec un contact qui n'a pas de prénom. Crée un contact de test dans FluentCRM avec uniquement une adresse email — aucun autre champ rempli. Envoie-lui un email de test avec tes merge codes et fallbacks. Vérifie que chaque fallback s'affiche correctement.

[Montre l'email reçu avec les fallbacks en place]

Voilà le résultat. "Bonjour ami" au lieu de "Bonjour ". "Pour ton entreprise" au lieu de "Pour ". Chaque trou est comblé par une valeur naturelle.

**[TRANSITION — face caméra]**

Les fallback values sont un détail qui fait la différence entre un email amateur et un email professionnel. Prends l'habitude d'en mettre un sur chaque merge code qui pourrait être vide — en particulier le prénom. Prochaine leçon : les custom contact fields pour stocker tes propres données sur chaque contact.

---

**Points clés** :
- Fallback = valeur affichée quand le champ du contact est vide
- Syntaxe : `{{contact.field | default:"valeur"}}`
- Choisir des fallbacks naturels qui s'intègrent dans la phrase ("ami", "ton entreprise")
- Combinable avec les transformers : `{{contact.first_name | default:"ami" | ucfirst}}`
- Toujours tester avec un contact dont les champs sont vides

**Mots clés SEO** : FluentCRM fallback value, valeur par défaut merge code, personnalisation email champ vide, FluentCRM default value

---

### Leçon 12.6 — Custom contact fields : ajoute tes propres champs

**Durée** : 6 min
**Type** : Vidéo HeyGen
**Écran** : Face caméra pour intro/conclusion, screencast FluentCRM settings

---

**[INTRO — face caméra]**

FluentCRM stocke des données standard sur chaque contact : prénom, nom, email, adresse. Mais ton activité a des besoins spécifiques. Tu veux savoir quel CMS utilise ton contact. Son niveau en WordPress. S'il a déjà un LMS installé. Les custom contact fields te permettent de créer tes propres champs et de les utiliser dans tes emails, tes automations et tes conditions. Dans cette leçon, tu en crées plusieurs et tu les exploites.

**[ÉCRAN — screencast FluentCRM > Settings > Custom Contact Fields]**

[Navigue vers les paramètres des champs personnalisés]

Étape 1 : va dans FluentCRM > Settings > Custom Contact Fields. C'est ici que tu crées et gères tes champs personnalisés. Par défaut, la liste est vide — tu pars de zéro.

[Montre le bouton "Add Field"]

Étape 2 : clique sur "Add Field". FluentCRM te propose plusieurs types de champs.

Texte libre — pour une réponse courte (nom du site, URL).
Textarea — pour une réponse longue (description du projet).
Select dropdown — pour un choix unique dans une liste (niveau : débutant, intermédiaire, avancé).
Radio buttons — même principe, affichage différent.
Checkbox — pour des choix multiples (intérêts : LMS, CRM, SEO, Automatisation).
Date — pour une date (date de début de projet).
Number — pour un chiffre (nombre de sites WordPress gérés).

**[ÉCRAN — screencast création des champs]**

[Crée un premier champ "Niveau WordPress"]

Étape 3 : crée ton premier champ. Nom : "Niveau WordPress". Type : Select dropdown. Options : "Débutant", "Intermédiaire", "Avancé". Slug : "niveau_wordpress" — généré automatiquement, c'est ce que tu utiliseras dans les merge codes.

[Crée un deuxième champ "CMS actuel"]

Étape 4 : crée un deuxième champ. Nom : "CMS actuel". Type : Select dropdown. Options : "WordPress", "Wix", "Shopify", "Autre", "Aucun". Slug : "cms_actuel".

[Crée un troisième champ "Intérêts"]

Étape 5 : crée un champ à choix multiples. Nom : "Intérêts". Type : Checkbox. Options : "LMS", "CRM", "SEO", "Automatisation", "Ecommerce". Slug : "interets". Ce champ permettra de segmenter tes contacts selon leurs centres d'intérêt.

**[ÉCRAN — screencast utilisation dans un email]**

[Ouvre un email et insère un merge code de champ personnalisé]

Étape 6 : utilise tes champs personnalisés dans un email. Le merge code suit le format : `{{contact.custom.niveau_wordpress}}`. Tu peux y appliquer un fallback : `{{contact.custom.niveau_wordpress | default:"non renseigné"}}`.

Exemple concret dans un email : "Tu es actuellement au niveau {{contact.custom.niveau_wordpress | default:"non renseigné"}} sur WordPress. Voici les ressources adaptées à ton profil."

**[ÉCRAN — screencast utilisation dans une condition]**

[Montre un bloc conditionnel basé sur un champ personnalisé]

Étape 7 : combine avec les conditional sections. Crée un bloc conditionnel avec la condition : "Custom Field > niveau_wordpress > equals > Avancé". Dans ce bloc, affiche du contenu réservé aux utilisateurs avancés. Un autre bloc avec "niveau_wordpress > equals > Débutant" pour le contenu débutant.

C'est là que tout se connecte. Tes champs personnalisés alimentent tes conditions qui personnalisent tes emails.

**[TRANSITION — face caméra]**

Les custom contact fields sont la fondation de la personnalisation avancée. Plus tu collectes de données pertinentes sur tes contacts, plus tu peux cibler tes messages. Mais attention — ne crée que les champs que tu vas vraiment utiliser. Chaque champ doit servir à une segmentation ou une personnalisation concrète. Dans la prochaine leçon, tu mets tout ça en pratique avec un exercice complet.

---

**Points clés** :
- Custom fields : texte, textarea, select, radio, checkbox, date, number
- Slug généré automatiquement — utilisé dans les merge codes
- Merge code : `{{contact.custom.slug_du_champ}}`
- Utilisable dans les emails, conditions, automations
- Ne créer que les champs utiles à une segmentation ou personnalisation réelle

**Mots clés SEO** : FluentCRM custom contact fields, champs personnalisés FluentCRM, merge code custom field, segmentation FluentCRM champs

---

### Leçon 12.7 — Exercice : Crée un email avec 3 blocs conditionnels par niveau

**Durée** : 5 min
**Type** : Exercice guidé
**Écran** : Face caméra pour consignes, screencast pour démo du résultat attendu

---

**[INTRO — face caméra]**

C'est le moment de pratiquer. Tu vas créer un email complet avec trois blocs conditionnels basés sur le champ personnalisé "Niveau WordPress" que tu as créé dans la leçon précédente. Un bloc pour les débutants, un pour les intermédiaires, un pour les avancés. Même email, trois expériences.

**[ÉCRAN — slide "Consignes de l'exercice"]**

[Affiche les consignes]

Voici ce que tu dois faire.

Objectif : créer un email de newsletter avec un contenu commun et trois CTA différents selon le niveau WordPress du contact.

Étape 1 — Crée une campagne email. Nom : "Newsletter Perso Niveaux". Objet : "{{contact.first_name | default:"Ami" | ucfirst}}, tes ressources WordPress de la semaine".

Étape 2 — Ajoute le contenu commun. Un bloc d'introduction avec un salut personnalisé utilisant le merge code avec fallback. Un ou deux paragraphes présentant les articles de la semaine.

Étape 3 — Crée le bloc conditionnel "Débutant". Condition : custom field "niveau_wordpress" égal à "Débutant". Contenu : "Tu débutes avec WordPress ? Voici 3 tutoriels pour bien démarrer." Bouton : "Voir les tutoriels débutant" pointant vers ta catégorie débutant.

Étape 4 — Crée le bloc conditionnel "Intermédiaire". Condition : custom field "niveau_wordpress" égal à "Intermédiaire". Contenu : "Tu maîtrises les bases ? Passe à la vitesse supérieure avec ces guides pratiques." Bouton : "Voir les guides intermédiaires".

Étape 5 — Crée le bloc conditionnel "Avancé". Condition : custom field "niveau_wordpress" égal à "Avancé". Contenu : "Tu es au niveau avancé ? Découvre les techniques de pro pour optimiser ton site." Bouton : "Voir les techniques avancées".

Étape 6 — Ajoute un bloc sans condition en bas. Un footer commun avec le lien de désabonnement et un rappel : "Tu reçois cet email parce que tu fais partie de la communauté schoolsWP."

Étape 7 — Teste. Prévisualise avec un contact de chaque niveau. Vérifie que chaque bloc s'affiche correctement et que les blocs non pertinents sont masqués.

**[ÉCRAN — screencast du résultat attendu]**

[Montre l'email fini dans l'éditeur avec les 3 blocs conditionnels annotés]

Voici le résultat attendu. Dans l'éditeur, tu vois tous les blocs. Chaque bloc conditionnel est clairement identifié avec sa condition. Le contact débutant verra l'intro + le CTA débutant + le footer. Le contact avancé verra l'intro + le CTA avancé + le footer.

[Montre la prévisualisation pour chaque niveau]

Et voici le rendu pour chaque profil. Propre, personnalisé, sans trou.

**[TRANSITION — face caméra]**

Si tu as réussi cet exercice, tu maîtrises les conditional sections, les merge codes avec fallback, et les champs personnalisés. C'est la combinaison de ces trois outils qui rend FluentCRM vraiment puissant pour la personnalisation. Dernière étape du module : le quiz pour valider tes acquis.

---

**Points clés** :
- Exercice : 1 email, 3 blocs conditionnels par niveau WordPress
- Utiliser merge codes avec fallback dans l'objet et le corps
- Chaque bloc conditionnel basé sur un custom field
- Footer commun sans condition
- Tester avec des contacts de profils différents

---

### Leçon 12.8 — Quiz : Valide tes acquis M12

**Durée** : 4 min
**Type** : Quiz (8 QCM)
**Plateforme** : TutorLMS quiz intégré

---

**[INTRO — face caméra]**

Dernier exercice du Module 12. Huit questions pour vérifier que tu maîtrises les conditional sections, les merge codes avancés et la personnalisation dans FluentCRM. Réponds sans revenir sur les leçons — c'est un test de ce que tu as retenu.

---

**Question 1** : Que se passe-t-il quand un contact ne remplit pas la condition d'une section conditionnelle ?

A) Un message d'erreur s'affiche
B) Le bloc s'affiche vide avec un espace blanc
C) Le bloc disparaît complètement — le contact ne le voit pas ✅
D) FluentCRM envoie un email différent

**Question 2** : Quelle syntaxe permet d'afficher "ami" si le prénom du contact est vide ?

A) `{{contact.first_name || "ami"}}`
B) `{{contact.first_name | default:"ami"}}` ✅
C) `{{contact.first_name ? "ami"}}`
D) `{{contact.first_name | fallback:"ami"}}`

**Question 3** : Quel data transformer met la première lettre en majuscule ?

A) `capitalize`
B) `upper`
C) `ucfirst` ✅
D) `title`

**Question 4** : Tu veux personnaliser ta page WordPress selon le profil FluentCRM du visiteur. Quel outil utilises-tu ?

A) Un plugin de page builder
B) Les shortcodes conditionnels FluentCRM ✅
C) Le customizer WordPress
D) Un fichier functions.php modifié

**Question 5** : Quelle est la syntaxe correcte pour un merge code de champ personnalisé ?

A) `{{contact.niveau_wordpress}}`
B) `{{custom.niveau_wordpress}}`
C) `{{contact.custom.niveau_wordpress}}` ✅
D) `{{field.niveau_wordpress}}`

**Question 6** : Tu chaînes `| default:"ami" | ucfirst` sur un merge code. Le prénom du contact est vide. Que s'affiche-t-il ?

A) ami
B) Ami ✅
C) AMI
D) Rien — le fallback ne fonctionne pas avec ucfirst

**Question 7** : Quel type de custom field utilises-tu pour permettre à un contact de choisir plusieurs centres d'intérêt ?

A) Select dropdown
B) Radio buttons
C) Checkbox ✅
D) Texte libre

**Question 8** : Tu as un email avec un CTA conditionnel pour les contacts tagués "premium" et un autre pour ceux sans ce tag. Un contact a les tags "premium" et "débutant". Que voit-il ?

A) Les deux CTA
B) Uniquement le CTA premium ✅
C) Uniquement le CTA débutant
D) Aucun CTA

---

**Seuil de réussite** : 6/8 (75%)

**[OUTRO — face caméra]**

Module 12 terminé. Tu sais maintenant personnaliser tes emails et tes pages WordPress selon le profil de chaque contact. Conditional sections, merge codes avancés, fallback values, champs personnalisés — ces outils combinés te permettent de créer une expérience unique pour chaque segment de ta liste. Un seul email à maintenir, plusieurs versions qui parlent à chaque profil. C'est ça, la vraie puissance d'un CRM bien configuré.

---

**Récapitulatif Module 12** :

| Leçon | Concept clé |
|-------|-------------|
| 12.1 | Conditional sections = un email, plusieurs versions |
| 12.2 | Créer des blocs conditionnels dans les emails (tag, liste, champ) |
| 12.3 | Shortcodes conditionnels sur les pages WordPress |
| 12.4 | Merge codes avancés + data transformers (ucfirst, date_format) |
| 12.5 | Fallback values pour gérer les champs vides |
| 12.6 | Custom contact fields pour stocker tes propres données |
| 12.7 | Exercice pratique — email avec 3 blocs par niveau |
| 12.8 | Quiz de validation (8 QCM) |
