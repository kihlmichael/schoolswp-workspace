# Audit Topical Authority — schoolsWP

---

## Score Autorité : 79/100

---

## Détail :

**Couverture : 16/20**
**Connexions : 15/20**
**Cohérence : 17/20**
**Positionnement : 17/20**
**Potentiel cluster : 14/20**

---

## Analyse par bloc

### 1️⃣ Couverture du sujet — 16/20

L'article couvre solidement les angles décisionnels attendus : positionnement produit, comparatif, cas d'usage, mise en place, FAQ. La structure répond bien à une intention d'achat/évaluation.

**Points forts :** Les données terrain (3 200 contacts, taux d'ouverture 38 % vs 22 %, coût SES) donnent une profondeur que le SERP générique n'a pas. Le tableau comparatif est bien construit. La distinction listes/tags est correctement expliquée.

**Gaps identifiés :**

- **Délivrabilité email absente** : aucun développement sur SPF/DKIM/DMARC, réputation de domaine, warm-up — pourtant critique pour quelqu'un qui migre depuis Mailchimp. C'est un angle obligatoire pour une décision éclairée.
- **Reporting et analytics FluentCRM** : le reporting est mentionné comme fonctionnalité Pro sans être illustré. Quel tableau de bord ? Quels KPIs visibles ? Pour un décideur, c'est un critère.
- **Groundhogg** cité dans le résumé final mais absent du comparatif principal — incohérence qui fragilise la couverture concurrentielle.
- **Limites réelles du plan gratuit** : survolées, pas détaillées (combien de contacts, quelles automatisations bloquées).

Pénalité appliquée : −4 (gaps sur délivrabilité et reporting, Groundhogg absent du comparatif)

---

### 2️⃣ Connexions internes — 15/20

**Points forts :** Deux liens internes explicites vers `/fluentsmtp-amazon-ses-wordpress` (mentionné deux fois, ce qui est pertinent). Un lien vers une checklist lead magnet. La logique de maillage vers un article SMTP complémentaire est bien pensée.

**Gaps identifiés :**

- **Aucun lien vers un article LMS** (LearnDash, LifterLMS) alors que l'article cite ces intégrations comme argument central. Si ces articles existent dans le cluster, c'est une opportunité manquée évidente.
- **Aucun lien vers WooCommerce** comme déclencheur d'automatisation — pourtant mentionné plusieurs fois.
- **Pas de lien vers un article "automatisations WordPress"** ou "segmentation email" qui serait naturellement satellite de ce pilier.
- **L'article ne peut recevoir de liens entrants** que si d'autres articles du cluster existent — la structure cluster n'est pas encore établie autour de ce pilier, ce qui limite mécaniquement le maillage entrant aujourd'hui.

Pénalité appliquée : −5 (opportunités de maillage vers LMS/WooCommerce/automatisations non exploitées)

---

### 3️⃣ Cohérence sémantique — 17/20

**Points forts :** Le champ lexical est dense et cohérent : CRM natif, automatisation visuelle, déclencheur, séquence conditionnelle, tag, liste, segmentation, SMTP, délivrabilité, intégration native, propriété des données. Le vocabulaire est celui d'un praticien, pas d'un généraliste qui paraphrase la page produit.

**Entités nommées bien utilisées :** WPManageNinja, Amazon SES, Brevo, Mailgun, FluentSMTP, LearnDash, LifterLMS, MemberPress, WooCommerce, Kinsta, WP Engine, o2switch — cohérence forte avec l'écosystème WordPress terrain.

**Légères dilutions :**

- La section "syndrome de l'outil dispersé" est valide mais générique — elle aurait pu être renforcée avec des termes plus spécifiques FluentCRM (smart codes, custom fields, deal module).
- "HubSpot", "Salesforce" apparaissent comme références externes sans développement — signal sémantique qui sort du territoire WordPress sans apporter de valeur.

Pénalité appliquée : −3 (HubSpot/Salesforce hors-territoire, quelques termes produit FluentCRM manquants)

---

### 4️⃣ Positionnement expert — 17/20

**Points forts :** C'est le bloc le plus solide de l'article. Les données terrain sont réelles et précises (6 mois, 3 200 contacts, chiffres mesurés, bug de déduplication résolu en SQL). L'angle "schoolsWP comme site de test réel" est différenciant — aucun article SERP générique sur FluentCRM ne fait ça. Le ton est celui d'un praticien qui a choisi cet outil pour lui-même avant de le recommander. La phrase sur le bug SQL résolu en 20 minutes grâce aux données locales est un exemple précis d'avantage terrain que personne d'autre ne peut reproduire.

**Ce qui manque pour atteindre 20/20 :**

- **Pas d'écran ou visuel** : l'article décrit l'éditeur d'automatisation comme "visuel" sans montrer à quoi ça ressemble. Pour une intention décisionnelle, un screenshot annoté vaut 500 mots.
- **Pas de regret ou de limite assumée** : l'honnêteté terrain serait renforcée par une limite concrète rencontrée (ex : "le reporting est trop basique pour moi sur X, voici comment je contourne").
- Le lien affilié est bien signalé — bonne pratique maintenue.

Pénalité appliquée : −3 (absence de visuels, absence de limite terrain assumée)

---

### 5️⃣ Potentiel cluster — 14/20

**Points forts :** L'article a clairement vocation de pilier du cluster CRM de schoolsWP. Il couvre le sujet de référence (FluentCRM), cite des satellites naturels (FluentSMTP, LMS, WooCommerce, segmentation), et pose les bases conceptuelles (listes vs tags, déclencheurs, automatisations).

**Limites identifiées :**

- **La position de pilier n'est pas encore architecturée** : l'article ne pointe pas vers ses futurs satellites, il mentionne seulement l'article SMTP. Un vrai pilier doit signaler l'étendue du cluster.
- **Pas de section "À aller plus loin"** qui liste les prochains articles du cluster — pourtant standard pour un pilier.
- **Exploitabilité en série** : forte sur LinkedIn (6 posts possibles : données terrain, comparatif, setup SMTP, structure tags, migration Mailchimp, FAQ). Newsletter : 2-3 épisodes. Mais cela n'est pas anticipé dans la structure de l'article.
- **Le cluster CRM n'est pas délimité dans l'article** : quelle est la suite logique pour le lecteur après ce pilier ? Il clique sur le lien affilié ou sur la checklist, mais il n'a pas de vision de ce que schoolsWP couvre sur ce territoire.

Pénalité appliquée : −6 (architecture cluster non visible dans l'article, pas de signal vers les satellites)

---

## Manques identifiés :

– **[CRITIQUE] Délivrabilité email absente** : SPF/DKIM/DMARC, warm-up de domaine, réputation IP — angle obligatoire pour un article décisionnel sur un CRM qui nécessite un SMTP externe. C'est la première question d'un acheteur qui migre depuis Mailchimp.

– **[CRITIQUE] Architecture cluster non visible** : l'article se comporte comme un article autonome, pas comme un pilier. Aucune section "Dans ce cluster" ou "Articles liés" ne signale les satellites. Un lecteur qui finit l'article n'a pas de chemin suivant dans l'écosystème schoolsWP (hors checklist et lien SMTP).

– **[SECONDAIRE] Reporting et analytics FluentCRM non développés** : fonctionnalité Pro citée sans illustration — taux d'ouverture par séquence, suivi des clics, logs d'activité contact. Pour une décision à 90 $/an, le lecteur veut savoir ce qu'il verra dans son tableau de bord.

– **[SECONDAIRE] Groundhogg absent du comparatif principal** : cité dans le récapitulatif final comme "alternative directe" mais absent du tableau et de la section comparatif. Incohérence qui fragilise la crédibilité de l'analyse concurrentielle.

– **[SECONDAIRE] Pas de limite terrain assumée** : l'honnêteté est un signal d'expertise. Citer une vraie limite rencontrée (ex : module deal trop limité, pas de scoring natif, reporting basique) renforcerait le positionnement différenciant plutôt que de l'affaiblir.

---

## Opportunités de cluster :

– **Article satellite 1 : "FluentCRM : comment structurer ses listes et tags pour un site formation WordPress" | Angle opérationnel/tutorial | Lien logique : l'article pilier pose la distinction listes/tags comme étape stratégique critique (étape 3) mais ne la développe pas — ce satellite transforme ce passage en guide complet, avec exemples de