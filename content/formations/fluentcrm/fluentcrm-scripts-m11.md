# Scripts vidéo — Module 11 : Recurring campaigns et newsletters

**Formation** : Maîtriser FluentCRM
**Module** : M11 — Recurring campaigns et newsletters (Premium)
**Leçons** : 6 vidéos + 1 quiz
**Durée totale** : ~40 min
**Prérequis** : M10 (campagnes email classiques)
**Date** : 2026-03-23

---

### Leçon 11.1 — Comprends les recurring campaigns : newsletter en autopilote

**Durée** : 5 min
**Type** : Vidéo HeyGen
**Écran** : Face caméra pour intro/conclusion, screencast FluentCRM

---

**[INTRO — face caméra]**

Tu publies des articles chaque semaine sur ton site WordPress. Tes abonnés les découvrent par hasard — ou pas du tout. Tu pourrais créer une campagne email chaque vendredi, copier les liens, envoyer manuellement. Mais tu as mieux à faire. Les recurring campaigns de FluentCRM font exactement ça à ta place : elles envoient une newsletter automatique à la fréquence que tu choisis, avec tes derniers contenus, sans que tu touches à quoi que ce soit. Dans cette leçon, tu comprends le principe et tu vois quand les utiliser.

**[ÉCRAN — screencast FluentCRM > Email Campaigns]**

[Montre la liste des campagnes, puis le bouton "Create Campaign"]

Étape 1 : dans FluentCRM, va dans Email Campaigns. Tu connais déjà les campagnes classiques — tu en as créé dans les modules précédents. Ici, on s'intéresse à un type spécifique : la recurring campaign. Clique sur "Create Campaign" et observe les options disponibles.

[Montre l'option "Recurring Campaign" dans le sélecteur de type]

Étape 2 : FluentCRM propose plusieurs types de campagnes. La recurring campaign est celle qui nous intéresse. Contrairement à une campagne classique que tu envoies une fois, la recurring campaign se relance automatiquement selon un calendrier que tu définis.

**[ÉCRAN — slide "Campagne classique vs Recurring"]**

[Montre un tableau comparatif]

Voici la différence fondamentale.

Campagne classique : tu la crées, tu la configures, tu l'envoies. Terminée. Pour envoyer une nouvelle newsletter, tu recommences de zéro.

Recurring campaign : tu la crées, tu la configures une fois. Elle s'envoie automatiquement — chaque semaine, chaque mois, ou à la fréquence que tu veux. Le contenu se met à jour tout seul grâce aux blocs dynamiques.

**[ÉCRAN — screencast FluentCRM]**

[Montre les blocs dynamiques disponibles dans l'éditeur]

Étape 3 : la magie des recurring campaigns repose sur deux blocs dynamiques. Le bloc "Latest Post" — il tire automatiquement tes derniers articles WordPress. Et le bloc "RSS" — il tire du contenu depuis n'importe quel flux RSS, même externe. On les verra en détail dans les prochaines leçons.

**[ÉCRAN — slide "3 cas d'usage schoolsWP"]**

[Montre 3 scénarios]

Quand utiliser une recurring campaign ? Trois scénarios concrets.

Scénario 1 : newsletter hebdo automatique. Chaque vendredi, tes abonnés reçoivent les 3 derniers articles schoolsWP. Tu ne fais rien — la campagne tire les articles publiés dans la semaine.

Scénario 2 : newsletter mensuelle étudiants premium. Chaque premier du mois, les étudiants premium reçoivent un récap des nouveaux modules de formation ajoutés.

Scénario 3 : newsletter segmentée par pilier. Les abonnés intéressés par le CRM reçoivent uniquement les articles CRM. Ceux intéressés par le SEO reçoivent les articles SEO. Même campagne, contenu différent selon la catégorie.

**[TRANSITION — face caméra]**

La recurring campaign est la pièce qui manque entre ton blog et ta liste email. Tu publies du contenu, FluentCRM le distribue. Pas de manipulation manuelle, pas d'oubli le vendredi soir. Dans la prochaine leçon, tu crées ta première recurring campaign de A à Z.

---

**Points clés** :
- Recurring campaign = campagne qui se relance automatiquement selon un calendrier
- Différence avec campagne classique : configuration unique, envois répétés
- Deux blocs dynamiques : Latest Post (articles WP) et RSS (flux externes)
- Cas d'usage : newsletter hebdo, récap mensuel, contenu segmenté par catégorie
- Zéro intervention manuelle après la configuration initiale

**Mots clés SEO** : FluentCRM recurring campaign, newsletter automatique WordPress, campagne récurrente FluentCRM, newsletter autopilote

---

### Leçon 11.2 — Crée ta première recurring campaign

**Durée** : 6 min
**Type** : Vidéo HeyGen
**Écran** : Face caméra pour intro/conclusion, screencast FluentCRM

---

**[INTRO — face caméra]**

Tu sais ce qu'est une recurring campaign. Maintenant tu en crées une. L'objectif : une newsletter hebdomadaire qui part chaque vendredi à 9h à toute ta liste, avec tes derniers articles. Six étapes, et c'est en place.

**[ÉCRAN — screencast FluentCRM > Email Campaigns > Create Campaign]**

[Clique sur "Create Campaign", sélectionne "Recurring Campaign"]

Étape 1 : va dans Email Campaigns, clique sur "Create Campaign". Sélectionne le type "Recurring Campaign". Donne-lui un nom interne clair — par exemple "Newsletter Hebdo schoolsWP". Ce nom n'est pas visible par tes abonnés, il sert à t'y retrouver dans ta liste de campagnes.

[Montre le champ "Subject" et "Preview Text"]

Étape 2 : configure l'objet et le preview text. Pour une newsletter récurrente, tu peux utiliser des merge tags dynamiques. Par exemple : "Les nouveautés schoolsWP de cette semaine" ou "3 articles frais pour toi, {{contact.first_name}}". Le preview text apparaît après l'objet dans la boîte de réception — utilise-le pour donner envie d'ouvrir.

**[ÉCRAN — screencast sélection des destinataires]**

[Montre la sélection des listes et segments]

Étape 3 : choisis tes destinataires. Sélectionne la liste ou le segment qui doit recevoir cette newsletter. Pour une newsletter générale, c'est ta liste principale — par exemple "Abonnés Blog". Pour une newsletter segmentée, tu cibles un segment spécifique.

[Montre les options d'exclusion]

Tu peux aussi exclure des segments. Par exemple, exclure les contacts qui ont le tag "desabonne-newsletter" ou ceux qui sont dans une automation de vente active — pour ne pas les bombarder.

**[ÉCRAN — screencast éditeur de contenu]**

[Ouvre l'éditeur visuel de la campagne]

Étape 4 : construis le template. C'est la structure de ta newsletter — elle sera réutilisée à chaque envoi. En haut, un header avec ton logo schoolsWP. En dessous, une intro courte — un ou deux paragraphes personnalisés. Puis le bloc dynamique qui tire tes articles — on le configure en détail dans la leçon suivante. En bas, un footer avec le lien de désabonnement.

[Montre l'ajout d'un bloc texte pour l'intro]

L'intro peut être statique — le même texte chaque semaine — ou tu peux la personnaliser avec des merge tags. Pour commencer, un texte simple suffit : "Voici les derniers articles publiés sur schoolsWP cette semaine."

**[ÉCRAN — screencast ajout du bloc Latest Post]**

[Montre l'insertion du bloc Latest Post]

Étape 5 : insère le bloc "Latest Post". C'est lui qui rend ta newsletter dynamique. À chaque envoi, il tire automatiquement les articles les plus récents. On verra tous ses paramètres dans la leçon 11.3. Pour l'instant, insère-le avec les réglages par défaut.

**[ÉCRAN — screencast planification]**

[Montre les options de planification]

Étape 6 : planifie l'envoi. Sélectionne la fréquence — "Weekly". Choisis le jour — "Friday". Choisis l'heure — "09:00". Choisis le fuseau horaire — celui de ton audience principale. FluentCRM enverra automatiquement chaque vendredi à 9h.

[Active la campagne]

Valide et active la campagne. Elle est maintenant programmée. Chaque vendredi, FluentCRM va générer un nouvel email avec tes derniers articles et l'envoyer à ta liste.

**[TRANSITION — face caméra]**

Ta première recurring campaign est en place. Elle va tourner chaque semaine sans intervention. Mais le bloc Latest Post a beaucoup de paramètres qui changent tout — nombre d'articles, catégorie, affichage. C'est ce qu'on voit dans la prochaine leçon.

---

**Points clés** :
- Créer une recurring campaign : type "Recurring" > sujet > destinataires > template > planification
- Nom interne clair pour s'y retrouver dans la liste des campagnes
- Merge tags dynamiques dans l'objet : {{contact.first_name}}
- Template réutilisé à chaque envoi — structure fixe, contenu dynamique
- Possibilité d'exclure des segments pour éviter la sur-sollicitation

**Mots clés SEO** : créer recurring campaign FluentCRM, newsletter hebdomadaire WordPress, campagne récurrente email, FluentCRM newsletter setup

---

### Leçon 11.3 — Le bloc Latest Post : insère tes derniers articles automatiquement

**Durée** : 6 min
**Type** : Vidéo HeyGen
**Écran** : Face caméra pour intro/conclusion, screencast FluentCRM éditeur email

---

**[INTRO — face caméra]**

Le bloc Latest Post est le moteur de ta newsletter automatique. C'est lui qui décide quels articles apparaissent, combien, et comment ils sont affichés. Bien configuré, il transforme chaque envoi en une newsletter pertinente et à jour. Mal configuré, il envoie du contenu en vrac sans logique. Dans cette leçon, tu maîtrises chaque paramètre.

**[ÉCRAN — screencast FluentCRM > éditeur recurring campaign]**

[Ouvre la recurring campaign créée en 11.2, positionne sur le bloc Latest Post]

Étape 1 : ouvre ta recurring campaign et clique sur le bloc Latest Post pour accéder à ses paramètres. Tu vas voir plusieurs options de configuration.

**[ÉCRAN — screencast paramètres du bloc]**

[Montre le paramètre "Number of posts"]

Étape 2 : nombre d'articles. C'est le premier paramètre — combien d'articles afficher dans chaque newsletter. Pour une newsletter hebdomadaire, 3 est un bon chiffre. Assez pour offrir du choix, pas trop pour ne pas noyer le lecteur. Pour une newsletter mensuelle, tu peux monter à 5 ou 6.

[Montre le paramètre "Post Type"]

Étape 3 : type de publication. Par défaut, le bloc tire les articles (post type "post"). Mais tu peux aussi tirer d'autres types de contenu — des pages, des produits WooCommerce, des cours TutorLMS. Pour une newsletter de contenu classique, reste sur "post".

[Montre le filtre par catégorie]

Étape 4 : filtre par catégorie. C'est le paramètre le plus puissant. Tu peux limiter les articles à une ou plusieurs catégories WordPress. Par exemple : uniquement les articles de la catégorie "LMS". Ou uniquement "CRM" et "Automatisation".

Cas concret schoolsWP : tu as une recurring campaign pour chaque pilier thématique. La newsletter "LMS" tire uniquement les articles LMS. La newsletter "CRM" tire uniquement les articles CRM. Même template, même fréquence, contenu différent.

[Montre le filtre par tag WordPress]

Étape 5 : filtre par tag. En plus des catégories, tu peux filtrer par tag WordPress. Par exemple, uniquement les articles taggés "tutoriel" ou "comparatif". Ça te permet de créer des newsletters thématiques très ciblées.

**[ÉCRAN — screencast options d'affichage]**

[Montre les options d'affichage du bloc]

Étape 6 : options d'affichage. Tu contrôles ce qui apparaît pour chaque article dans la newsletter. Image mise en avant — oui ou non. Extrait — le résumé automatique ou les premiers mots de l'article. Auteur, date de publication. Bouton "Lire la suite" avec le lien vers l'article.

[Active l'image mise en avant et l'extrait]

Pour une newsletter visuellement engageante, active l'image mise en avant et l'extrait. Désactive la date et l'auteur — sauf si tu as plusieurs auteurs et que ça a du sens pour ton audience.

[Montre le rendu dans le preview]

Étape 7 : prévisualise le résultat. FluentCRM affiche un aperçu avec tes vrais articles. Vérifie que le rendu correspond à ce que tu veux : les bonnes images, les bons titres, les extraits lisibles.

**[ÉCRAN — screencast cas spécifique : aucun article nouveau]**

[Montre le comportement quand il n'y a pas de nouvel article]

Étape 8 : que se passe-t-il si tu n'as pas publié d'article cette semaine ? Le bloc Latest Post tire les articles les plus récents disponibles — même si ce sont les mêmes que la semaine précédente. Pour éviter de renvoyer du contenu déjà envoyé, tu peux cocher l'option "Only posts published since last campaign" si elle est disponible dans ta version de FluentCRM. Sinon, maintiens un rythme de publication régulier.

**[TRANSITION — face caméra]**

Le bloc Latest Post est ton meilleur allié pour une newsletter zéro maintenance. Filtre par catégorie pour segmenter, ajuste le nombre d'articles pour doser, et vérifie le rendu dans le preview. Dans la prochaine leçon, on voit le bloc RSS — pour tirer du contenu depuis n'importe quel flux, y compris externe.

---

**Points clés** :
- Nombre d'articles : 3 pour une hebdo, 5-6 pour une mensuelle
- Filtre par catégorie : une recurring campaign par pilier thématique
- Filtre par tag WordPress : newsletters thématiques ciblées
- Options d'affichage : image, extrait, lien "Lire la suite"
- Preview obligatoire avant activation pour vérifier le rendu réel

**Mots clés SEO** : FluentCRM Latest Post bloc, newsletter articles automatique, recurring campaign WordPress contenu, FluentCRM filtre catégorie

---

### Leçon 11.4 — Le bloc RSS : tire du contenu depuis n'importe quel flux

**Durée** : 5 min
**Type** : Vidéo HeyGen
**Écran** : Face caméra pour intro/conclusion, screencast FluentCRM éditeur email

---

**[INTRO — face caméra]**

Le bloc Latest Post tire tes propres articles WordPress. Mais parfois, tu veux inclure du contenu externe dans ta newsletter — un article d'un partenaire, les dernières actualités d'un outil que tu recommandes, ou ton propre contenu depuis un autre site. Le bloc RSS de FluentCRM fait exactement ça. Tu lui donnes un flux RSS, il tire les derniers éléments et les affiche dans ta newsletter.

**[ÉCRAN — screencast FluentCRM > éditeur recurring campaign]**

[Ouvre l'éditeur, montre la barre de blocs]

Étape 1 : dans l'éditeur de ta recurring campaign, cherche le bloc "RSS Content" ou "RSS Feed" dans les blocs disponibles. Insère-le à l'endroit où tu veux afficher le contenu externe.

[Montre le champ URL du flux RSS]

Étape 2 : entre l'URL du flux RSS. Chaque site avec un blog a un flux RSS — généralement accessible à l'adresse `site.com/feed/`. Par exemple, pour inclure les dernières actualités de WordPress.org : `https://wordpress.org/news/feed/`.

**[ÉCRAN — screencast configuration du bloc RSS]**

[Montre les paramètres du bloc]

Étape 3 : configure le nombre d'éléments à afficher. Comme pour le bloc Latest Post, 3 à 5 éléments est un bon point de départ. Le bloc tire les éléments les plus récents du flux.

[Montre les options d'affichage]

Étape 4 : configure l'affichage. Tu retrouves des options similaires au bloc Latest Post — titre, description, image si disponible dans le flux, lien vers l'article original. Le rendu dépend de la qualité du flux RSS source. Certains flux incluent des images et des descriptions riches, d'autres uniquement le titre.

**[ÉCRAN — screencast cas d'usage concrets]**

[Montre une newsletter avec deux blocs : Latest Post + RSS]

Étape 5 : combine les blocs. Voici un cas concret schoolsWP. Ta newsletter hebdomadaire contient deux sections. Section 1 : "Nos derniers articles" — bloc Latest Post avec tes 3 derniers articles. Section 2 : "Veille WordPress" — bloc RSS avec les 2 dernières actualités de WordPress.org ou d'un blog de référence dans ta niche.

[Montre un deuxième exemple : flux RSS de ton propre podcast ou chaîne YouTube]

Étape 6 : tu peux aussi utiliser le bloc RSS pour tirer ton propre contenu depuis une autre plateforme. Ton podcast a un flux RSS. Ta chaîne YouTube a un flux RSS. Intègre-les dans ta newsletter pour que tes abonnés découvrent tous tes contenus, pas seulement tes articles.

**[ÉCRAN — screencast vérification du flux]**

[Teste un flux RSS dans le navigateur]

Étape 7 : avant d'utiliser un flux RSS, vérifie qu'il fonctionne. Colle l'URL dans ton navigateur — tu dois voir du contenu XML structuré. Si la page affiche une erreur ou est vide, le flux ne fonctionne pas et le bloc RSS n'affichera rien dans ta newsletter.

**[TRANSITION — face caméra]**

Le bloc RSS élargit les possibilités de ta newsletter au-delà de ton propre blog. Contenu partenaire, veille sectorielle, tes autres plateformes — tout peut être intégré automatiquement. Dans la prochaine leçon, on parle planification : comment choisir la bonne fréquence et le bon timing pour tes recurring campaigns.

---

**Points clés** :
- Bloc RSS : tire du contenu depuis n'importe quel flux RSS valide
- URL type : site.com/feed/ pour les sites WordPress
- Combiner Latest Post + RSS dans une même newsletter pour varier le contenu
- Vérifier le flux dans le navigateur avant de l'intégrer
- Cas d'usage : veille sectorielle, contenu partenaire, podcast, YouTube

**Mots clés SEO** : FluentCRM bloc RSS, newsletter flux RSS WordPress, recurring campaign contenu externe, RSS feed email marketing

---

### Leçon 11.5 — Planifie : hebdo, bimensuel, mensuel — choisis ta fréquence

**Durée** : 5 min
**Type** : Vidéo HeyGen
**Écran** : Face caméra pour intro/conclusion, screencast FluentCRM

---

**[INTRO — face caméra]**

Ta recurring campaign est configurée, le contenu est dynamique. Reste la question qui change tout : à quelle fréquence envoyer ? Trop souvent, tu fatigues ta liste. Pas assez, on t'oublie. Et le jour et l'heure comptent autant que la fréquence. Dans cette leçon, tu configures la planification optimale pour ta newsletter.

**[ÉCRAN — screencast FluentCRM > recurring campaign > onglet Schedule]**

[Ouvre les paramètres de planification d'une recurring campaign]

Étape 1 : accède aux paramètres de planification de ta recurring campaign. C'est ici que tu définis quand et à quelle fréquence FluentCRM envoie ta newsletter.

[Montre les options de fréquence]

Étape 2 : choisis ta fréquence. FluentCRM propose plusieurs options.

Hebdomadaire — une fois par semaine. C'est le rythme le plus courant pour un blog actif. Tu publies au moins 2-3 articles par semaine, tes abonnés reçoivent un récap chaque semaine.

Bimensuel — toutes les deux semaines. Bon compromis si tu publies moins souvent. Un article par semaine suffit pour alimenter une newsletter bimensuelle.

Mensuel — une fois par mois. Adapté aux récaps, aux newsletters premium, ou aux audiences qui ne veulent pas être sollicitées souvent.

**[ÉCRAN — slide "Quelle fréquence pour quel cas"]**

[Montre un tableau de décision]

Voici comment choisir.

Tu publies 2+ articles par semaine ? Newsletter hebdo. Tu as assez de contenu frais pour chaque envoi.

Tu publies 1 article par semaine ? Newsletter bimensuelle. Ça te donne 2-3 articles par envoi.

Tu publies 2-3 articles par mois ? Newsletter mensuelle. Un récap complet chaque mois.

Cas schoolsWP : la newsletter générale est hebdomadaire — 3 derniers articles chaque vendredi. La newsletter étudiants premium est mensuelle — récap des nouveaux modules le premier du mois.

**[ÉCRAN — screencast configuration du jour et de l'heure]**

[Montre la sélection du jour de la semaine]

Étape 3 : choisis le jour d'envoi. Pour une newsletter hebdo, le mardi et le jeudi ont historiquement les meilleurs taux d'ouverture en B2B. Le vendredi fonctionne bien pour du contenu "à lire ce week-end". Évite le lundi — les boîtes de réception sont surchargées.

[Montre la sélection de l'heure]

Étape 4 : choisis l'heure d'envoi. Deux créneaux fonctionnent bien : 9h-10h le matin (début de journée, les gens checkent leurs emails) et 14h (retour de pause déjeuner). Teste les deux sur plusieurs semaines et compare les taux d'ouverture.

[Montre la sélection du fuseau horaire]

Étape 5 : choisis le fuseau horaire. C'est un détail qui change les résultats. Si ton audience est francophone en France, sélectionne Europe/Paris. Si tu as une audience internationale, choisis le fuseau de la majorité de tes abonnés. FluentCRM envoie selon ce fuseau — pas celui de ton serveur.

**[ÉCRAN — screencast modification d'une campagne active]**

[Montre comment modifier la planification d'une campagne déjà active]

Étape 6 : tu peux modifier la planification d'une recurring campaign active à tout moment. Change le jour, l'heure ou la fréquence — les prochains envois suivront la nouvelle planification. Les envois passés ne sont pas affectés.

**[TRANSITION — face caméra]**

La fréquence idéale dépend de ton rythme de publication et de ton audience. Commence par une fréquence, observe les métriques pendant un mois, ajuste si nécessaire. Le taux de désabonnement est ton indicateur clé — s'il monte, tu envoies trop souvent. Dans la prochaine leçon, on organise tes campagnes avec les labels pour garder le contrôle quand tu en as plusieurs.

---

**Points clés** :
- Hebdomadaire : 2+ articles par semaine — adapté aux blogs actifs
- Bimensuel : 1 article par semaine — bon compromis
- Mensuel : 2-3 articles par mois — récaps et audiences sélectionnées
- Jour d'envoi : mardi, jeudi ou vendredi selon le contexte
- Heure : 9h-10h ou 14h — tester et comparer
- Fuseau horaire : celui de la majorité de ton audience, pas celui du serveur

**Mots clés SEO** : fréquence newsletter FluentCRM, planification recurring campaign, meilleur jour envoi newsletter, FluentCRM schedule email

---

### Leçon 11.6 — Organise tes campagnes avec les labels

**Durée** : 5 min
**Type** : Vidéo HeyGen
**Écran** : Face caméra pour intro/conclusion, screencast FluentCRM

---

**[INTRO — face caméra]**

Tu as ta newsletter hebdo générale, ta newsletter mensuelle premium, ta campagne de veille sectorielle. Plus une campagne de bienvenue, une de réengagement, et trois campagnes de promotion. En quelques mois, ta liste de campagnes devient un mur de texte. Les campaign labels de FluentCRM résolvent ce problème — ils te permettent de classer, filtrer et retrouver tes campagnes en quelques secondes.

**[ÉCRAN — screencast FluentCRM > Email Campaigns]**

[Montre une liste de campagnes sans labels — désordonnée]

Étape 1 : voici une liste de campagnes sans organisation. Newsletters, promotions, séquences de bienvenue — tout est mélangé. Pour retrouver ta recurring campaign mensuelle, tu scrolles, tu lis les noms un par un. Pas efficace.

[Montre le menu des labels]

Étape 2 : dans la page des campagnes, repère la section labels. FluentCRM te permet de créer des labels pour catégoriser tes campagnes. Clique sur "Add Label" ou "Manage Labels".

**[ÉCRAN — screencast création des labels]**

[Crée un premier label]

Étape 3 : crée tes labels. Voici une structure qui fonctionne pour schoolsWP.

Label "Newsletter" — pour toutes les recurring campaigns de type newsletter.
Label "Promotion" — pour les campagnes de vente et offres spéciales.
Label "Onboarding" — pour les séquences de bienvenue.
Label "Reengagement" — pour les campagnes de win-back.

[Crée les 4 labels avec des couleurs distinctes]

Donne à chaque label une couleur distincte. Les couleurs rendent le tri visuel immédiat — tu vois d'un coup d'œil quelles campagnes sont des newsletters, des promotions ou de l'onboarding.

**[ÉCRAN — screencast application des labels]**

[Sélectionne une recurring campaign et lui assigne un label]

Étape 4 : assigne les labels à tes campagnes. Ouvre une campagne, ou sélectionne-la dans la liste, et attribue-lui le label correspondant. Ta "Newsletter Hebdo schoolsWP" reçoit le label "Newsletter". Ta "Promo Black Friday" reçoit le label "Promotion".

[Montre l'assignation de label sur plusieurs campagnes]

Tu peux assigner un label à plusieurs campagnes en une fois si FluentCRM le permet dans ta version. Sinon, fais-le campagne par campagne — ça prend 30 secondes chacune.

**[ÉCRAN — screencast filtrage par label]**

[Montre le filtre par label dans la liste des campagnes]

Étape 5 : filtre par label. C'est là où les labels prennent tout leur sens. Clique sur le label "Newsletter" — tu ne vois que tes recurring campaigns. Clique sur "Promotion" — uniquement les campagnes de vente. Tu passes d'un mur de 30 campagnes à une liste filtrée de 5.

[Montre le filtre en action avec différents labels]

Quand tu gères 10, 20, 50 campagnes, ce filtrage devient indispensable. Tu retrouves n'importe quelle campagne en deux clics.

**[ÉCRAN — slide "Convention de nommage"]**

[Montre un tableau avec la convention]

Étape 6 : combine les labels avec une convention de nommage claire. Voici la méthode schoolsWP.

Format : [Type] Nom descriptif — Fréquence
Exemples :
- "[NL] Articles Hebdo schoolsWP — Weekly"
- "[NL] Recap Premium — Monthly"
- "[PROMO] Black Friday 2026 — One-shot"
- "[OB] Bienvenue Nouveaux Abonnés — Triggered"

Labels + nommage cohérent = tu retrouves n'importe quelle campagne en moins de 5 secondes, même avec des dizaines de campagnes.

**[TRANSITION — face caméra]**

Les labels sont un petit investissement de temps qui rapporte gros quand ta liste de campagnes grandit. Crée tes labels dès maintenant, assigne-les à tes campagnes existantes, et adopte une convention de nommage. Tu gagneras du temps chaque semaine. Dernier arrêt de ce module : le quiz pour valider tes acquis.

---

**Points clés** :
- Campaign labels : classement visuel par couleur et catégorie
- Structure recommandée : Newsletter, Promotion, Onboarding, Reengagement
- Filtrage par label : retrouver une campagne en 2 clics parmi des dizaines
- Convention de nommage : [Type] Nom — Fréquence
- Combiner labels + nommage pour une organisation zéro friction

**Mots clés SEO** : FluentCRM campaign labels, organiser campagnes email, labels email marketing, FluentCRM organisation campagnes

---

### Leçon 11.7 — Quiz : Valide tes acquis M11

**Durée** : 8 min
**Type** : Quiz TutorLMS (8 QCM)
**Format** : Questions affichées dans TutorLMS, pas de vidéo

---

**Question 1** : Quelle est la différence fondamentale entre une campagne classique et une recurring campaign dans FluentCRM ?

- A) La campagne classique est gratuite, la recurring campaign est payante
- B) La campagne classique s'envoie une fois, la recurring campaign se relance automatiquement selon un calendrier ✅
- C) La recurring campaign ne peut envoyer que des articles de blog
- D) La campagne classique ne peut pas utiliser de merge tags

**Explication** : Une campagne classique est un envoi unique. Une recurring campaign se relance automatiquement à la fréquence définie (hebdo, bimensuel, mensuel) avec du contenu mis à jour dynamiquement.

---

**Question 2** : Tu veux créer une newsletter qui envoie automatiquement tes 3 derniers articles WordPress chaque semaine. Quel bloc utilises-tu ?

- A) Le bloc "Dynamic Content"
- B) Le bloc "RSS Feed"
- C) Le bloc "Latest Post" ✅
- D) Le bloc "Post Notification"

**Explication** : Le bloc Latest Post tire automatiquement les derniers articles publiés sur ton site WordPress. Le bloc RSS sert pour le contenu externe ou les flux d'autres plateformes.

---

**Question 3** : Quel est l'avantage principal du filtre par catégorie dans le bloc Latest Post ?

- A) Il accélère le temps de chargement de l'email
- B) Il permet de créer des newsletters segmentées par thématique sans dupliquer le template ✅
- C) Il empêche les articles en brouillon d'apparaître
- D) Il trie les articles par nombre de commentaires

**Explication** : Le filtre par catégorie te permet d'avoir une recurring campaign par pilier thématique (LMS, CRM, SEO) avec le même template mais du contenu différent selon la catégorie filtrée.

---

**Question 4** : Tu veux inclure les dernières actualités de WordPress.org dans ta newsletter. Quel bloc utilises-tu et quelle URL entres-tu ?

- A) Bloc Latest Post avec l'URL wordpress.org
- B) Bloc RSS avec l'URL https://wordpress.org/news/feed/ ✅
- C) Bloc HTML avec un iframe vers wordpress.org
- D) Bloc Latest Post avec le filtre "External Sources"

**Explication** : Le bloc RSS tire du contenu depuis n'importe quel flux RSS valide. L'URL du flux WordPress.org est https://wordpress.org/news/feed/. Le bloc Latest Post ne fonctionne qu'avec le contenu de ton propre site.

---

**Question 5** : Tu publies 1 article par semaine sur ton blog. Quelle fréquence de recurring campaign est la plus adaptée ?

- A) Quotidienne — pour maximiser la visibilité
- B) Hebdomadaire — un article par envoi suffit
- C) Bimensuelle — ça te donne 2-3 articles par envoi ✅
- D) La fréquence n'a aucun impact sur les résultats

**Explication** : Avec 1 article par semaine, une newsletter bimensuelle te donne 2-3 articles par envoi — assez pour offrir de la valeur à chaque email. Une hebdo avec un seul article peut paraître légère.

---

**Question 6** : Quel indicateur te signale que tu envoies tes newsletters trop fréquemment ?

- A) Le taux d'ouverture augmente
- B) Le taux de désabonnement augmente ✅
- C) Le taux de clic reste stable
- D) Le nombre de nouveaux abonnés diminue

**Explication** : Un taux de désabonnement en hausse est le signal le plus direct que ta fréquence est trop élevée. Si tes abonnés partent, réduis la cadence.

---

**Question 7** : Quelle convention de nommage est recommandée pour organiser tes campagnes FluentCRM ?

- A) Utiliser uniquement des numéros : "Campaign 001", "Campaign 002"
- B) [Type] Nom descriptif — Fréquence, avec des labels couleur par catégorie ✅
- C) Le nom de l'auteur suivi de la date : "Michael_2026-03-23"
- D) Pas de convention — FluentCRM trie automatiquement par pertinence

**Explication** : La convention [Type] Nom — Fréquence combinée aux labels couleur permet de retrouver n'importe quelle campagne en quelques secondes, même avec des dizaines de campagnes.

---

**Question 8** : Tu as une recurring campaign active et tu veux changer le jour d'envoi du vendredi au mardi. Que se passe-t-il ?

- A) Tu dois désactiver la campagne, en créer une nouvelle, et supprimer l'ancienne
- B) Les prochains envois suivront la nouvelle planification, les envois passés ne sont pas affectés ✅
- C) FluentCRM envoie un email supplémentaire le mardi suivant pour compenser
- D) La modification est impossible sur une campagne active

**Explication** : Tu peux modifier la planification d'une recurring campaign active à tout moment. Les prochains envois suivront la nouvelle planification. Aucun impact sur les emails déjà envoyés.

---

**Seuil de réussite** : 6/8 (75%)

**Message de réussite** : Module 11 validé. Tu maîtrises les recurring campaigns FluentCRM : configuration, blocs dynamiques (Latest Post et RSS), planification et organisation par labels. Le module 12 t'attend pour passer aux intégrations FluentCRM avec les autres outils de ton stack WordPress.

**Message d'échec** : Tu n'as pas atteint le seuil de 75%. Revois les leçons 11.1 à 11.6, en particulier les différences entre les blocs Latest Post et RSS, et les critères de choix de fréquence. Tu peux retenter le quiz autant de fois que nécessaire.
