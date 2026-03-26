# Scripts video — Module 12 : Conditional sections et personnalisation

**Formation** : Maitriser FluentCRM
**Module** : M12 — Conditional sections et personnalisation (Premium)
**Lecons** : 6 videos + 1 exercice + 1 quiz
**Duree totale** : ~45 min
**Prerequis** : M11 (recurring campaigns et newsletters)
**Date** : 2026-03-23

---

### Lecon 12.1 — Comprends les conditional sections : un email, plusieurs versions

**Duree** : 5 min
**Type** : Video HeyGen
**Ecran** : Face camera pour intro/conclusion, screencast FluentCRM

---

**[INTRO — face camera]**

Tu envoies le meme email a toute ta liste. Meme contenu, meme CTA, meme offre — que le contact soit debutant ou expert, gratuit ou premium. Resultat : ton message parle a tout le monde en general, et a personne en particulier. Les conditional sections de FluentCRM changent ca. Un seul email, mais des blocs qui s'affichent ou se masquent selon le profil du contact. Dans cette lecon, tu comprends le principe et tu vois pourquoi c'est un levier de conversion concret.

**[ECRAN — slide "Un email, plusieurs versions"]**

[Montre un schema : 1 email a gauche, 3 versions a droite selon le profil]

Etape 1 : le concept est simple. Tu rediges un seul email dans FluentCRM. A l'interieur, tu places des blocs conditionnels. Chaque bloc a une regle : "affiche ce contenu SI le contact remplit telle condition". Le contact debutant voit un CTA vers la formation gratuite. Le contact avance voit un CTA vers la formation premium. Le contact qui a deja achete voit un message de fidelite. Un seul email a maintenir, trois experiences differentes.

**[ECRAN — screencast FluentCRM > editeur email]**

[Ouvre un email existant dans l'editeur visuel]

Etape 2 : dans l'editeur email de FluentCRM, tu vas trouver l'option "Conditional Section" ou "Conditional Block". C'est un bloc special qui enveloppe du contenu et lui applique une condition d'affichage. Si la condition est vraie, le contenu s'affiche. Si elle est fausse, le bloc disparait completement — le contact ne voit rien, pas de trou, pas d'espace vide.

**[ECRAN — slide "Conditions disponibles"]**

[Montre une liste des conditions possibles]

Etape 3 : quelles conditions peux-tu utiliser ? FluentCRM te donne acces a tout ce qu'il sait sur le contact.

Par tags : le contact a le tag "premium" ou "debutant".
Par listes : le contact est dans la liste "Etudiants LMS" ou "Prospects CRM".
Par champs personnalises : le contact a un champ "niveau" egal a "avance".
Par statut : le contact est abonne, desabonne, en attente.

Tu peux combiner ces conditions — par exemple : tag "premium" ET liste "Etudiants LMS".

**[ECRAN — slide "Exemple concret schoolsWP"]**

[Montre un email avec 3 blocs conditionnels annotes]

Etape 4 : exemple concret. Tu envoies ta newsletter hebdomadaire. Le corps de l'email est identique pour tout le monde — tes derniers articles. Mais le CTA en bas change selon le profil.

Bloc conditionnel 1 — si tag "debutant" : "Decouvre la formation gratuite pour bien demarrer avec WordPress."
Bloc conditionnel 2 — si tag "avance" : "Passe au niveau superieur avec la formation premium TutorLMS."
Bloc conditionnel 3 — si tag "client" : "Merci pour ta confiance. Voici les nouveautes reservees aux membres."

Trois experiences, un seul email a gerer.

**[TRANSITION — face camera]**

Les conditional sections te permettent de personnaliser sans multiplier les campagnes. Un email, plusieurs versions selon le profil. Dans la prochaine lecon, tu crees tes premieres sections conditionnelles dans l'editeur email de FluentCRM.

---

**Points cles** :
- Conditional section = bloc qui s'affiche ou se masque selon une condition
- Conditions basees sur : tags, listes, champs personnalises, statut
- Le contact ne voit jamais les blocs masques — pas d'espace vide
- Cas d'usage principal : CTA different selon le niveau ou le statut client
- Un seul email a maintenir au lieu de plusieurs campagnes

**Mots cles SEO** : FluentCRM conditional sections, personnalisation email WordPress, contenu conditionnel FluentCRM, email dynamique FluentCRM

---

### Lecon 12.2 — Cree des sections conditionnelles dans tes emails

**Duree** : 7 min
**Type** : Video HeyGen
**Ecran** : Face camera pour intro/conclusion, screencast FluentCRM editeur email

---

**[INTRO — face camera]**

Tu connais le principe des conditional sections. Maintenant tu les crees. L'objectif : un email avec un bloc visible uniquement pour les contacts tagges "premium" et un autre bloc pour les contacts sans ce tag. Sept etapes, et ton premier email personnalise est pret.

**[ECRAN — screencast FluentCRM > Email Campaigns > Create Campaign]**

[Cree une nouvelle campagne classique]

Etape 1 : cree une nouvelle campagne email. Donne-lui un nom interne — par exemple "Newsletter Perso M12". Configure l'objet : "Tes ressources de la semaine, {{contact.first_name}}". On travaille sur une campagne classique pour tester — tu pourras appliquer la meme technique dans une recurring campaign ensuite.

**[ECRAN — screencast editeur visuel]**

[Ouvre l'editeur et ajoute un bloc texte classique]

Etape 2 : commence par le contenu commun. Ajoute un bloc texte en haut avec ton introduction — identique pour tout le monde. Par exemple : "Bonjour {{contact.first_name}}, voici ce que j'ai prepare pour toi cette semaine." Ce bloc n'a aucune condition — tout le monde le voit.

[Montre l'ajout d'un deuxieme bloc texte avec du contenu article]

Etape 3 : ajoute le corps de ta newsletter — tes derniers articles, un recap, ce que tu veux. Ce contenu commun constitue la base de ton email.

**[ECRAN — screencast ajout du bloc conditionnel]**

[Montre comment inserer une conditional section]

Etape 4 : maintenant, ajoute ta premiere section conditionnelle. Dans l'editeur, cherche l'option "Conditional Block" ou le bouton pour ajouter une condition a un bloc. Selectionne-le et place-le sous ton contenu commun.

[Montre le panneau de configuration de la condition]

Etape 5 : configure la condition. Selectionne "Contact Tags" dans le type de condition. Puis choisis "Has Tag" et selectionne le tag "premium". Ce bloc ne s'affichera que pour les contacts qui portent ce tag. A l'interieur, redige ton CTA premium : "Tu as acces a la formation avancee TutorLMS — decouvre les nouveaux modules cette semaine." Ajoute un bouton qui pointe vers ta page de formation.

**[ECRAN — screencast ajout du deuxieme bloc conditionnel]**

[Ajoute un second bloc conditionnel]

Etape 6 : ajoute un deuxieme bloc conditionnel juste en dessous. Cette fois, la condition est "Does NOT have Tag" > "premium". A l'interieur, redige un CTA pour les contacts gratuits : "Pret a aller plus loin ? Decouvre la formation premium pour maitriser WordPress de A a Z." Bouton vers ta page de vente.

[Montre les deux blocs conditionnels cote a cote dans l'editeur]

Tu vois maintenant les deux blocs dans l'editeur. Toi tu vois tout. Mais chaque contact ne verra qu'un seul des deux blocs — celui dont la condition correspond a son profil.

**[ECRAN — screencast previsualisation]**

[Montre la previsualisation avec un contact premium, puis un contact gratuit]

Etape 7 : previsualise ton email. FluentCRM te permet de voir le rendu pour differents contacts. Selectionne un contact avec le tag "premium" — tu vois le CTA premium. Selectionne un contact sans ce tag — tu vois le CTA gratuit. Verifie que le rendu est propre dans les deux cas — pas d'espace vide, pas de decalage.

**[TRANSITION — face camera]**

Ton premier email avec des blocs conditionnels est pret. Un seul email, deux experiences. Tu peux ajouter autant de blocs conditionnels que necessaire — par tag, par liste, par champ personnalise. Dans la prochaine lecon, on applique le meme principe aux pages WordPress.

---

**Points cles** :
- Contenu commun en haut (intro, articles) — visible par tout le monde
- Blocs conditionnels en bas — chacun avec sa propre regle
- Condition "Has Tag" / "Does NOT have Tag" pour cibler par profil
- Toujours previsualiser avec plusieurs profils de contacts
- Technique applicable aux campagnes classiques et recurring

**Mots cles SEO** : creer conditional section FluentCRM, email conditionnel WordPress, bloc dynamique FluentCRM, personnalisation CTA email

---

### Lecon 12.3 — Cree des sections conditionnelles sur tes pages WordPress

**Duree** : 6 min
**Type** : Video HeyGen
**Ecran** : Face camera pour intro/conclusion, screencast WordPress + FluentCRM

---

**[INTRO — face camera]**

Les conditional sections ne sont pas limitees aux emails. FluentCRM te permet aussi de personnaliser tes pages WordPress selon le profil du visiteur. Un contact connecte avec le tag "premium" voit un contenu different d'un visiteur anonyme. Ta page d'accueil, ta page de formation, ta page de vente — chacune peut s'adapter au visiteur. Dans cette lecon, tu mets ca en place.

**[ECRAN — screencast WordPress > page d'accueil en edition]**

[Ouvre l'editeur de page WordPress]

Etape 1 : ouvre la page que tu veux personnaliser dans l'editeur WordPress. On va travailler sur la page d'accueil pour l'exemple. FluentCRM ajoute des shortcodes conditionnels que tu peux utiliser directement dans tes pages.

**[ECRAN — slide "Shortcodes conditionnels FluentCRM"]**

[Montre la syntaxe des shortcodes]

Etape 2 : FluentCRM fournit des shortcodes pour afficher du contenu selon le profil du contact connecte. La syntaxe de base :

`[fluentcrm_conditional]` — ouvre la section conditionnelle.
Attributs : `tag`, `list`, `status`, `contact_type`.

Par exemple : `[fluentcrm_conditional tag="premium"]Contenu reserve aux premium[/fluentcrm_conditional]`. Seuls les contacts connectes qui portent le tag "premium" verront ce contenu.

**[ECRAN — screencast WordPress editeur]**

[Ajoute un bloc HTML ou shortcode dans la page]

Etape 3 : dans ta page d'accueil, ajoute un bloc "Shortcode" ou "HTML personnalise". Insere le shortcode conditionnel. Par exemple, un message de bienvenue personnalise :

Pour les contacts premium : `[fluentcrm_conditional tag="premium"]Bienvenue, {{contact.first_name}}. Tes cours premium t'attendent.[/fluentcrm_conditional]`

Pour les contacts sans tag premium : `[fluentcrm_conditional not_tag="premium"]Decouvre nos formations pour maitriser WordPress.[/fluentcrm_conditional]`

Pour les visiteurs anonymes (non identifies) : le contenu par defaut de la page, sans shortcode.

[Montre les trois blocs dans l'editeur]

Etape 4 : place ces blocs dans ta page. L'ordre compte. Le shortcode verifie la condition et affiche ou masque le contenu. Si le visiteur n'est pas un contact FluentCRM identifie, aucun shortcode conditionnel ne s'affiche — seul le contenu standard de la page reste visible.

**[ECRAN — screencast test en front-end]**

[Montre la page avec un compte premium, puis un compte gratuit, puis en anonyme]

Etape 5 : teste ta page. Connecte-toi avec un compte qui a le tag "premium" — tu vois le message premium. Deconnecte-toi et connecte-toi avec un compte sans le tag — tu vois le message standard. Visite la page en anonyme — tu vois uniquement le contenu de base.

**[ECRAN — slide "Cas d'usage concrets"]**

[Montre 3 scenarios]

Etape 6 : trois cas d'usage concrets pour tes pages WordPress.

Page d'accueil personnalisee : message de bienvenue different selon le niveau.
Page de formation : afficher les modules premium uniquement aux contacts qui ont achete.
Page de vente : masquer le bouton d'achat pour les clients existants et afficher un message "Tu as deja acces".

**[TRANSITION — face camera]**

Tes pages WordPress s'adaptent maintenant au profil du visiteur. Combine ca avec les emails conditionnels et tu obtiens une experience coherente du premier email a la navigation sur ton site. Prochaine lecon : les merge codes avances pour aller encore plus loin dans la personnalisation.

---

**Points cles** :
- Shortcodes FluentCRM pour personnaliser les pages WordPress
- Syntaxe : `[fluentcrm_conditional tag="xxx"]contenu[/fluentcrm_conditional]`
- Attributs disponibles : tag, not_tag, list, status, contact_type
- Visiteurs anonymes ne voient que le contenu standard (sans shortcode)
- Cas d'usage : page d'accueil, page formation, page de vente

**Mots cles SEO** : FluentCRM shortcode conditionnel, personnalisation page WordPress FluentCRM, contenu dynamique WordPress, page personnalisee CRM

---

### Lecon 12.4 — Merge codes avances : data transformers et formatage

**Duree** : 7 min
**Type** : Video HeyGen
**Ecran** : Face camera pour intro/conclusion, screencast FluentCRM editeur email

---

**[INTRO — face camera]**

Tu utilises deja `{{contact.first_name}}` dans tes emails. C'est un merge code basique — il insere le prenom du contact. Mais FluentCRM va plus loin. Les data transformers te permettent de formater ces donnees : mettre une majuscule, formater une date, transformer du texte. Dans cette lecon, tu decouvres les merge codes avances et les transformers qui rendent tes emails plus propres et plus professionnels.

**[ECRAN — slide "Merge codes — rappel"]**

[Montre les merge codes de base]

Etape 1 : rappel rapide. Un merge code est un placeholder qui est remplace par la donnee du contact au moment de l'envoi. Les plus courants :

`{{contact.first_name}}` — prenom
`{{contact.last_name}}` — nom
`{{contact.email}}` — adresse email
`{{contact.id}}` — identifiant unique
`{{contact.status}}` — statut (subscribed, unsubscribed…)

Tu les connais deja. Maintenant on passe au niveau suivant.

**[ECRAN — screencast FluentCRM > editeur email]**

[Ouvre un email et montre le bouton d'insertion de merge codes]

Etape 2 : dans l'editeur email, clique sur le bouton d'insertion de merge codes — souvent represente par des accolades `{}`. FluentCRM affiche la liste complete des champs disponibles. Tu y trouves les champs standard, les champs personnalises que tu as crees, et les champs systeme.

[Montre la liste deroulante des merge codes disponibles]

Etape 3 : au-dela des champs contact, tu as acces a d'autres donnees. Les informations de ton site : `{{wp.site_url}}`, `{{wp.site_name}}`. Les dates : `{{current.date}}`, `{{current.year}}`. Ces merge codes sont utiles dans les footers, les mentions legales, ou les emails automatises.

**[ECRAN — slide "Data transformers"]**

[Montre un tableau des transformers disponibles]

Etape 4 : les data transformers. C'est la ou ca devient puissant. Un transformer modifie la donnee avant de l'afficher. La syntaxe : `{{contact.first_name | transformer}}`.

Les transformers les plus utiles :

`ucfirst` — premiere lettre en majuscule. `{{contact.first_name | ucfirst}}` transforme "michael" en "Michael".
`upper` — tout en majuscules. `{{contact.last_name | upper}}` transforme "kihl" en "KIHL".
`lower` — tout en minuscules. Utile pour normaliser les emails dans le contenu visible.
`date_format:"d/m/Y"` — formate une date. `{{contact.date_of_birth | date_format:"d/m/Y"}}` transforme "1990-05-15" en "15/05/1990".

**[ECRAN — screencast application dans un email]**

[Montre un email avec des merge codes transformer]

Etape 5 : application concrete. Tu rediges un email de bienvenue. Au lieu de `Bonjour {{contact.first_name}}`, tu ecris `Bonjour {{contact.first_name | ucfirst}}`. Si le contact a saisi son prenom en minuscules dans le formulaire, l'email affichera quand meme une majuscule.

[Montre un deuxieme exemple avec une date]

Autre exemple : tu envoies un recap annuel. Tu veux afficher la date d'inscription du contact. `Tu es avec nous depuis le {{contact.created_at | date_format:"d F Y"}}.` Au lieu d'afficher "2024-01-15", l'email affiche "15 January 2024".

**[ECRAN — slide "Combiner transformers"]**

[Montre un exemple de chaine de transformers]

Etape 6 : tu peux chainer les transformers. `{{contact.first_name | lower | ucfirst}}` — d'abord tout en minuscules, puis premiere lettre en majuscule. Ca normalise les prenoms saisis n'importe comment : "MICHAEL" devient "Michael", "mIcHaEl" devient "Michael".

**[ECRAN — screencast test d'envoi]**

[Montre un email de test envoye avec les merge codes resolus]

Etape 7 : teste toujours tes merge codes avant l'envoi. Envoie un email de test a toi-meme et verifie que les transformers fonctionnent correctement. Verifie aussi le rendu quand un champ est vide — on verra comment gerer ca dans la prochaine lecon avec les fallback values.

**[TRANSITION — face camera]**

Les data transformers rendent tes emails plus propres sans effort de saisie supplementaire de la part du contact. Majuscules, dates formatees, texte normalise — tout ca se gere au niveau du merge code. Prochaine etape : que se passe-t-il quand la donnee est vide ? C'est le sujet des fallback values.

---

**Points cles** :
- Merge codes = placeholders remplaces par les donnees du contact a l'envoi
- Data transformers : ucfirst, upper, lower, date_format
- Syntaxe : `{{contact.field | transformer}}`
- Chainer les transformers : `{{contact.first_name | lower | ucfirst}}`
- Toujours tester les merge codes avant envoi reel

**Mots cles SEO** : FluentCRM merge codes, data transformers FluentCRM, formatage email dynamique, merge tags WordPress email

---

### Lecon 12.5 — Fallback values : que montrer quand la donnee est vide

**Duree** : 5 min
**Type** : Video HeyGen
**Ecran** : Face camera pour intro/conclusion, screencast FluentCRM editeur email

---

**[INTRO — face camera]**

Tu ecris "Bonjour {{contact.first_name}}" dans ton email. Le contact n'a pas renseigne son prenom. Resultat : "Bonjour " suivi de rien. Un espace vide, un email qui fait amateur. Les fallback values reglent ce probleme. Tu definis une valeur de remplacement qui s'affiche quand la donnee est absente. Dans cette lecon, tu apprends a les configurer correctement.

**[ECRAN — slide "Le probleme des champs vides"]**

[Montre un email avec un prenom vide — "Bonjour ," — puis un avec fallback — "Bonjour ami,"]

Etape 1 : le probleme est frequent. Tous tes contacts n'ont pas rempli tous les champs. Certains se sont inscrits avec juste une adresse email — pas de prenom, pas de nom, pas de date de naissance. Si tu utilises un merge code qui pointe vers un champ vide, FluentCRM affiche une chaine vide. L'email a un trou.

**[ECRAN — screencast FluentCRM > editeur email]**

[Montre la syntaxe du fallback dans le merge code]

Etape 2 : la syntaxe du fallback. Tu ajoutes `| default:"valeur"` apres le nom du champ.

`{{contact.first_name | default:"ami"}}` — si le prenom est vide, affiche "ami".

Resultat : "Bonjour ami," au lieu de "Bonjour ,". Propre, naturel, sans trou.

[Montre d'autres exemples de fallback]

Etape 3 : tu peux appliquer un fallback a n'importe quel merge code.

`{{contact.company | default:"ton entreprise"}}` — si pas de nom d'entreprise.
`{{contact.phone | default:"non renseigne"}}` — si pas de telephone (utile dans les recaps de profil).
`{{contact.city | default:"ta ville"}}` — si pas de ville.

Le fallback n'ecrase jamais la donnee existante. Si le champ est rempli, c'est la vraie valeur qui s'affiche.

**[ECRAN — slide "Combiner fallback et transformer"]**

[Montre la syntaxe combinee]

Etape 4 : tu peux combiner fallback et data transformers. L'ordre compte.

`{{contact.first_name | default:"ami" | ucfirst}}` — si le prenom est vide, affiche "Ami" (avec majuscule). Si le prenom est "michael", affiche "Michael".

La regle : le default s'applique d'abord, puis le transformer formate le resultat — que ce soit la vraie donnee ou le fallback.

**[ECRAN — screencast test avec contact sans prenom]**

[Cree un contact test sans prenom, envoie un email de test]

Etape 5 : teste avec un contact qui n'a pas de prenom. Cree un contact de test dans FluentCRM avec uniquement une adresse email — aucun autre champ rempli. Envoie-lui un email de test avec tes merge codes et fallbacks. Verifie que chaque fallback s'affiche correctement.

[Montre l'email recu avec les fallbacks en place]

Voila le resultat. "Bonjour ami" au lieu de "Bonjour ". "Pour ton entreprise" au lieu de "Pour ". Chaque trou est comble par une valeur naturelle.

**[TRANSITION — face camera]**

Les fallback values sont un detail qui fait la difference entre un email amateur et un email professionnel. Prends l'habitude d'en mettre un sur chaque merge code qui pourrait etre vide — en particulier le prenom. Prochaine lecon : les custom contact fields pour stocker tes propres donnees sur chaque contact.

---

**Points cles** :
- Fallback = valeur affichee quand le champ du contact est vide
- Syntaxe : `{{contact.field | default:"valeur"}}`
- Choisir des fallbacks naturels qui s'integrent dans la phrase ("ami", "ton entreprise")
- Combinable avec les transformers : `{{contact.first_name | default:"ami" | ucfirst}}`
- Toujours tester avec un contact dont les champs sont vides

**Mots cles SEO** : FluentCRM fallback value, valeur par defaut merge code, personnalisation email champ vide, FluentCRM default value

---

### Lecon 12.6 — Custom contact fields : ajoute tes propres champs

**Duree** : 6 min
**Type** : Video HeyGen
**Ecran** : Face camera pour intro/conclusion, screencast FluentCRM settings

---

**[INTRO — face camera]**

FluentCRM stocke des donnees standard sur chaque contact : prenom, nom, email, adresse. Mais ton activite a des besoins specifiques. Tu veux savoir quel CMS utilise ton contact. Son niveau en WordPress. S'il a deja un LMS installe. Les custom contact fields te permettent de creer tes propres champs et de les utiliser dans tes emails, tes automations et tes conditions. Dans cette lecon, tu en crees plusieurs et tu les exploites.

**[ECRAN — screencast FluentCRM > Settings > Custom Contact Fields]**

[Navigue vers les parametres des champs personnalises]

Etape 1 : va dans FluentCRM > Settings > Custom Contact Fields. C'est ici que tu crees et geres tes champs personnalises. Par defaut, la liste est vide — tu pars de zero.

[Montre le bouton "Add Field"]

Etape 2 : clique sur "Add Field". FluentCRM te propose plusieurs types de champs.

Texte libre — pour une reponse courte (nom du site, URL).
Textarea — pour une reponse longue (description du projet).
Select dropdown — pour un choix unique dans une liste (niveau : debutant, intermediaire, avance).
Radio buttons — meme principe, affichage different.
Checkbox — pour des choix multiples (interets : LMS, CRM, SEO, Automatisation).
Date — pour une date (date de debut de projet).
Number — pour un chiffre (nombre de sites WordPress geres).

**[ECRAN — screencast creation des champs]**

[Cree un premier champ "Niveau WordPress"]

Etape 3 : cree ton premier champ. Nom : "Niveau WordPress". Type : Select dropdown. Options : "Debutant", "Intermediaire", "Avance". Slug : "niveau_wordpress" — genere automatiquement, c'est ce que tu utiliseras dans les merge codes.

[Cree un deuxieme champ "CMS actuel"]

Etape 4 : cree un deuxieme champ. Nom : "CMS actuel". Type : Select dropdown. Options : "WordPress", "Wix", "Shopify", "Autre", "Aucun". Slug : "cms_actuel".

[Cree un troisieme champ "Interets"]

Etape 5 : cree un champ a choix multiples. Nom : "Interets". Type : Checkbox. Options : "LMS", "CRM", "SEO", "Automatisation", "Ecommerce". Slug : "interets". Ce champ permettra de segmenter tes contacts selon leurs centres d'interet.

**[ECRAN — screencast utilisation dans un email]**

[Ouvre un email et insere un merge code de champ personnalise]

Etape 6 : utilise tes champs personnalises dans un email. Le merge code suit le format : `{{contact.custom.niveau_wordpress}}`. Tu peux y appliquer un fallback : `{{contact.custom.niveau_wordpress | default:"non renseigne"}}`.

Exemple concret dans un email : "Tu es actuellement au niveau {{contact.custom.niveau_wordpress | default:"non renseigne"}} sur WordPress. Voici les ressources adaptees a ton profil."

**[ECRAN — screencast utilisation dans une condition]**

[Montre un bloc conditionnel base sur un champ personnalise]

Etape 7 : combine avec les conditional sections. Cree un bloc conditionnel avec la condition : "Custom Field > niveau_wordpress > equals > Avance". Dans ce bloc, affiche du contenu reserve aux utilisateurs avances. Un autre bloc avec "niveau_wordpress > equals > Debutant" pour le contenu debutant.

C'est la que tout se connecte. Tes champs personnalises alimentent tes conditions qui personnalisent tes emails.

**[TRANSITION — face camera]**

Les custom contact fields sont la fondation de la personnalisation avancee. Plus tu collectes de donnees pertinentes sur tes contacts, plus tu peux cibler tes messages. Mais attention — ne cree que les champs que tu vas vraiment utiliser. Chaque champ doit servir a une segmentation ou une personnalisation concrete. Dans la prochaine lecon, tu mets tout ca en pratique avec un exercice complet.

---

**Points cles** :
- Custom fields : texte, textarea, select, radio, checkbox, date, number
- Slug genere automatiquement — utilise dans les merge codes
- Merge code : `{{contact.custom.slug_du_champ}}`
- Utilisable dans les emails, conditions, automations
- Ne creer que les champs utiles a une segmentation ou personnalisation reelle

**Mots cles SEO** : FluentCRM custom contact fields, champs personnalises FluentCRM, merge code custom field, segmentation FluentCRM champs

---

### Lecon 12.7 — Exercice : Cree un email avec 3 blocs conditionnels par niveau

**Duree** : 5 min
**Type** : Exercice guide
**Ecran** : Face camera pour consignes, screencast pour demo du resultat attendu

---

**[INTRO — face camera]**

C'est le moment de pratiquer. Tu vas creer un email complet avec trois blocs conditionnels bases sur le champ personnalise "Niveau WordPress" que tu as cree dans la lecon precedente. Un bloc pour les debutants, un pour les intermediaires, un pour les avances. Meme email, trois experiences.

**[ECRAN — slide "Consignes de l'exercice"]**

[Affiche les consignes]

Voici ce que tu dois faire.

Objectif : creer un email de newsletter avec un contenu commun et trois CTA differents selon le niveau WordPress du contact.

Etape 1 — Cree une campagne email. Nom : "Newsletter Perso Niveaux". Objet : "{{contact.first_name | default:"Ami" | ucfirst}}, tes ressources WordPress de la semaine".

Etape 2 — Ajoute le contenu commun. Un bloc d'introduction avec un salut personnalise utilisant le merge code avec fallback. Un ou deux paragraphes presentant les articles de la semaine.

Etape 3 — Cree le bloc conditionnel "Debutant". Condition : custom field "niveau_wordpress" egal a "Debutant". Contenu : "Tu debutes avec WordPress ? Voici 3 tutoriels pour bien demarrer." Bouton : "Voir les tutoriels debutant" pointant vers ta categorie debutant.

Etape 4 — Cree le bloc conditionnel "Intermediaire". Condition : custom field "niveau_wordpress" egal a "Intermediaire". Contenu : "Tu maitrises les bases ? Passe a la vitesse superieure avec ces guides pratiques." Bouton : "Voir les guides intermediaires".

Etape 5 — Cree le bloc conditionnel "Avance". Condition : custom field "niveau_wordpress" egal a "Avance". Contenu : "Tu es au niveau avance ? Decouvre les techniques de pro pour optimiser ton site." Bouton : "Voir les techniques avancees".

Etape 6 — Ajoute un bloc sans condition en bas. Un footer commun avec le lien de desabonnement et un rappel : "Tu recois cet email parce que tu fais partie de la communaute schoolsWP."

Etape 7 — Teste. Previsualise avec un contact de chaque niveau. Verifie que chaque bloc s'affiche correctement et que les blocs non pertinents sont masques.

**[ECRAN — screencast du resultat attendu]**

[Montre l'email fini dans l'editeur avec les 3 blocs conditionnels annotes]

Voici le resultat attendu. Dans l'editeur, tu vois tous les blocs. Chaque bloc conditionnel est clairement identifie avec sa condition. Le contact debutant verra l'intro + le CTA debutant + le footer. Le contact avance verra l'intro + le CTA avance + le footer.

[Montre la previsualisation pour chaque niveau]

Et voici le rendu pour chaque profil. Propre, personnalise, sans trou.

**[TRANSITION — face camera]**

Si tu as reussi cet exercice, tu maitrises les conditional sections, les merge codes avec fallback, et les champs personnalises. C'est la combinaison de ces trois outils qui rend FluentCRM vraiment puissant pour la personnalisation. Derniere etape du module : le quiz pour valider tes acquis.

---

**Points cles** :
- Exercice : 1 email, 3 blocs conditionnels par niveau WordPress
- Utiliser merge codes avec fallback dans l'objet et le corps
- Chaque bloc conditionnel base sur un custom field
- Footer commun sans condition
- Tester avec des contacts de profils differents

---

### Lecon 12.8 — Quiz : Valide tes acquis M12

**Duree** : 4 min
**Type** : Quiz (8 QCM)
**Plateforme** : TutorLMS quiz intégré

---

**[INTRO — face camera]**

Dernier exercice du Module 12. Huit questions pour verifier que tu maitrises les conditional sections, les merge codes avances et la personnalisation dans FluentCRM. Reponds sans revenir sur les lecons — c'est un test de ce que tu as retenu.

---

**Question 1** : Que se passe-t-il quand un contact ne remplit pas la condition d'une section conditionnelle ?

A) Un message d'erreur s'affiche
B) Le bloc s'affiche vide avec un espace blanc
C) Le bloc disparait completement — le contact ne le voit pas ✅
D) FluentCRM envoie un email different

**Question 2** : Quelle syntaxe permet d'afficher "ami" si le prenom du contact est vide ?

A) `{{contact.first_name || "ami"}}`
B) `{{contact.first_name | default:"ami"}}` ✅
C) `{{contact.first_name ? "ami"}}`
D) `{{contact.first_name | fallback:"ami"}}`

**Question 3** : Quel data transformer met la premiere lettre en majuscule ?

A) `capitalize`
B) `upper`
C) `ucfirst` ✅
D) `title`

**Question 4** : Tu veux personnaliser ta page WordPress selon le profil FluentCRM du visiteur. Quel outil utilises-tu ?

A) Un plugin de page builder
B) Les shortcodes conditionnels FluentCRM ✅
C) Le customizer WordPress
D) Un fichier functions.php modifie

**Question 5** : Quelle est la syntaxe correcte pour un merge code de champ personnalise ?

A) `{{contact.niveau_wordpress}}`
B) `{{custom.niveau_wordpress}}`
C) `{{contact.custom.niveau_wordpress}}` ✅
D) `{{field.niveau_wordpress}}`

**Question 6** : Tu chaines `| default:"ami" | ucfirst` sur un merge code. Le prenom du contact est vide. Que s'affiche-t-il ?

A) ami
B) Ami ✅
C) AMI
D) Rien — le fallback ne fonctionne pas avec ucfirst

**Question 7** : Quel type de custom field utilises-tu pour permettre a un contact de choisir plusieurs centres d'interet ?

A) Select dropdown
B) Radio buttons
C) Checkbox ✅
D) Texte libre

**Question 8** : Tu as un email avec un CTA conditionnel pour les contacts tagges "premium" et un autre pour ceux sans ce tag. Un contact a les tags "premium" et "debutant". Que voit-il ?

A) Les deux CTA
B) Uniquement le CTA premium ✅
C) Uniquement le CTA debutant
D) Aucun CTA

---

**Seuil de reussite** : 6/8 (75%)

**[OUTRO — face camera]**

Module 12 termine. Tu sais maintenant personnaliser tes emails et tes pages WordPress selon le profil de chaque contact. Conditional sections, merge codes avances, fallback values, champs personnalises — ces outils combines te permettent de creer une experience unique pour chaque segment de ta liste. Un seul email a maintenir, plusieurs versions qui parlent a chaque profil. C'est ca, la vraie puissance d'un CRM bien configure.

---

**Recapitulatif Module 12** :

| Lecon | Concept cle |
|-------|-------------|
| 12.1 | Conditional sections = un email, plusieurs versions |
| 12.2 | Creer des blocs conditionnels dans les emails (tag, liste, champ) |
| 12.3 | Shortcodes conditionnels sur les pages WordPress |
| 12.4 | Merge codes avances + data transformers (ucfirst, date_format) |
| 12.5 | Fallback values pour gerer les champs vides |
| 12.6 | Custom contact fields pour stocker tes propres donnees |
| 12.7 | Exercice pratique — email avec 3 blocs par niveau |
| 12.8 | Quiz de validation (8 QCM) |
