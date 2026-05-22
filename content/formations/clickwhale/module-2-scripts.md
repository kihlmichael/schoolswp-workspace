# Module 2 — Créer et gérer tes liens

> **Formation** : ClickWhale — schoolsWP
> **Prérequis** : Module 1 terminé
> **Objectif** : Tu sais créer des liens raccourcis, choisir le bon type de redirection, organiser par catégories, et importer des liens en masse via CSV.

---

## 2.1 — Crée ton premier lien raccourci

**Durée cible : 5 min**

[TALKING HEAD]

Ton premier lien affilié en 2 minutes chrono. C'est ce qu'on va faire dans cette leçon. Tu vas voir, la logique est simple : tu donnes un nom, tu choisis un slug, tu colles ton URL de destination, et c'est réglé.

[SCREENCAST: Dashboard WordPress > ClickWhale > Links]

**Étape 1 — Accède à l'interface de création**

Rends-toi dans ton dashboard WordPress. Dans le menu latéral gauche, clique sur **ClickWhale**, puis sur **Links**. Tu arrives sur la liste de tous tes liens. Pour l'instant, elle est vide. Clique sur **Add New** en haut de la page.

**Étape 2 — Remplis les champs essentiels**

[SCREENCAST: Formulaire de création de lien ClickWhale]

Tu as trois champs à remplir :

- **Title** : c'est le nom interne de ton lien. Personne ne le voit à part toi. Mets quelque chose de clair. Par exemple : "Lien affilié TutorLMS".
- **Slug** : c'est la partie qui apparaît dans l'URL. Si tu tapes "tutorlms", ton lien sera `tonsite.com/go/tutorlms`. Le préfixe `/go/` dépend de ce que tu as configuré dans le Module 1. Choisis un slug court et lisible.
- **Target URL** : colle ici l'URL de destination. C'est le vrai lien affilié, celui que tu as récupéré sur la plateforme d'affiliation.

**Étape 3 — Sauvegarde et teste**

[SCREENCAST: Bouton Save + test du lien dans un nouvel onglet]

Clique sur **Save**. Ton lien est créé. Maintenant, ouvre un nouvel onglet dans ton navigateur et tape l'adresse : `tonsite.com/go/tutorlms`. Tu dois être redirigé vers la page de destination. Si ça fonctionne, c'est bon, ton premier lien est actif.

[TALKING HEAD]

**TRANSITION** : Ton lien fonctionne, mais on a survolé les champs. Dans la leçon suivante, on va détailler chaque champ — slug, titre, description, catégorie — pour que tu comprennes exactement quoi mettre et pourquoi.

---

## 2.2 — Slug, titre, description : les champs à remplir

**Durée cible : 5 min**

[TALKING HEAD]

Quand tu crées un lien dans ClickWhale, tu as plusieurs champs devant toi. Certains sont obligatoires, d'autres optionnels. L'objectif de cette leçon : que tu saches exactement quoi mettre dans chaque champ, sans hésiter.

[SCREENCAST: Formulaire de création de lien ClickWhale, champs visibles]

**Champ 1 — Title**

Le titre, c'est ton repère interne. Tes visiteurs ne le voient jamais. Il sert uniquement à toi pour retrouver tes liens dans la liste.

Sois explicite. "Lien 1" ne t'aidera pas quand tu auras 50 liens. Préfère quelque chose comme "Affilié TutorLMS — page pricing" ou "Affilié Elementor — lien footer".

**Champ 2 — Slug**

Le slug, c'est la partie visible dans l'URL. Si ton préfixe est `/go/` et que ton slug est `tutorlms`, l'URL sera `tonsite.com/go/tutorlms`.

[SCREENCAST: Exemple de slug dans la barre d'adresse du navigateur]

La convention schoolsWP : `/go/nom-outil`. Tout en minuscules, pas d'espaces, pas de caractères spéciaux. Des exemples concrets :
- `tutorlms` pour TutorLMS
- `fluentcrm` pour FluentCRM
- `rankmath` pour RankMath

Si tu as plusieurs liens pour le même outil — par exemple un lien vers la page pricing et un vers la page features — ajoute un suffixe : `tutorlms-pricing`, `tutorlms-features`.

**Champ 3 — Target URL**

C'est l'URL de destination. Le vrai lien affilié brut, celui que tu récupères sur la plateforme d'affiliation. Tu le colles ici, point.

Vérifie toujours que l'URL fonctionne avant de la coller. Un lien cassé dès le départ, c'est du trafic perdu.

**Champ 4 — Description**

[SCREENCAST: Champ description dans le formulaire]

Optionnel, mais utile. C'est une note interne. Tu peux y mettre le taux de commission, la date d'expiration du programme, ou un rappel du type "commission 30% récurrente".

Personne ne voit ce champ à part toi dans le dashboard.

**Champ 5 — Category**

On détaillera les catégories dans la leçon 2.5, mais sache que tu peux assigner une catégorie dès la création. Ça t'évitera de devoir y revenir plus tard.

[TALKING HEAD]

**TRANSITION** : Tu sais remplir chaque champ. Mais il y a un réglage qu'on n'a pas encore abordé et qui change tout : le type de redirection. 301, 302, 307... dans la leçon suivante, on décortique les 5 types et je te dis lequel utiliser pour tes liens affiliés.

---

## 2.3 — Les 5 types de redirection : lequel choisir et pourquoi

**Durée cible : 7 min**

[TALKING HEAD]

Quand quelqu'un clique sur ton lien `tonsite.com/go/tutorlms`, le serveur doit répondre quelque chose au navigateur. Ce "quelque chose", c'est un code de redirection. Et tous les codes ne se valent pas. Certains sont bons pour le SEO, d'autres pour le tracking. Dans cette leçon, on passe en revue les 5 types disponibles dans ClickWhale, et je te donne la recommandation schoolsWP.

[SCREENCAST: Formulaire de lien ClickWhale > menu déroulant "Redirect Type"]

**Type 1 — 301 Moved Permanently**

Le 301 dit au navigateur : "cette page a déménagé pour de bon, ne reviens plus ici." Le navigateur met le résultat en cache. Google aussi. C'est le bon choix quand tu changes définitivement l'URL d'une page de ton site.

Pour l'affiliation ? Mauvaise idée. Le navigateur met en cache la destination, ce qui veut dire que les clics suivants ne passent plus par ClickWhale. Ton tracking devient faux.

**Type 2 — 302 Found (Temporarily Moved)**

Le 302 dit : "cette page est temporairement ailleurs." Le navigateur ne met pas systématiquement en cache, mais certains le font quand même. Utilisé classiquement pour des pages de maintenance ou des redirections de test.

Pour l'affiliation, c'est mieux que le 301, mais pas optimal.

**Type 3 — 303 See Other**

Le 303 est spécifique : il dit "va voir cette autre page avec une requête GET." On l'utilise principalement après la soumission d'un formulaire, pour rediriger vers une page de confirmation.

Pour les liens affiliés, tu n'en as pas besoin. Passe.

**Type 4 — 307 Temporarily Redirect**

[SCREENCAST: Sélection du 307 dans le menu déroulant]

Le 307, c'est la version stricte du 302. Il garantit que la méthode HTTP est préservée et — point clé — le navigateur ne met jamais le résultat en cache. Chaque clic repasse par ClickWhale. Chaque clic est compté.

C'est le choix recommandé pour tes liens affiliés.

**Type 5 — 308 Permanent Redirect**

Le 308 est la version stricte du 301 pour les requêtes POST. C'est un cas technique très rare. Tu n'en auras probablement jamais besoin pour de l'affiliation.

[TALKING HEAD]

**Récapitulatif rapide :**

| Type | Usage | Pour l'affiliation ? |
|------|-------|---------------------|
| 301 | Déménagement permanent | Non — cache = tracking cassé |
| 302 | Redirection temporaire | Bof — cache possible |
| 303 | Post-formulaire | Non — pas le bon usage |
| **307** | **Redirection temporaire stricte** | **Oui — recommandé** |
| 308 | Permanent strict (POST) | Non — cas rare |

**La recommandation schoolsWP : utilise le 307 pour tous tes liens affiliés.** Pas de cache navigateur, tracking précis, chaque clic est comptabilisé.

**TRANSITION** : Le type de redirection, c'est fait. Mais il y a deux attributs SEO à cocher systématiquement sur tes liens affiliés. Nofollow et Sponsored — on voit ça tout de suite.

---

## 2.4 — Nofollow et Sponsored : les attributs SEO essentiels

**Durée cible : 5 min**

[TALKING HEAD]

Quand tu crées un lien affilié, Google attend de toi que tu le signales. Si tu ne le fais pas, tu risques une pénalité manuelle. Deux attributs existent pour ça : nofollow et sponsored. Dans ClickWhale, c'est deux cases à cocher. Mais encore faut-il comprendre ce qu'elles font.

**Attribut 1 — Nofollow**

[SCREENCAST: Formulaire de lien > case "Nofollow"]

Quand tu ajoutes `rel="nofollow"` à un lien, tu dis à Google : "ne suis pas ce lien, ne transmets pas de jus SEO vers cette page." En clair, tu ne transfères pas ton autorité de domaine vers le site affilié.

Pour les liens affiliés, c'est obligatoire. Tu ne veux pas que ton site distribue du PageRank vers des pages commerciales externes.

**Attribut 2 — Sponsored**

[SCREENCAST: Formulaire de lien > case "Sponsored"]

L'attribut `rel="sponsored"` va plus loin. Il dit explicitement à Google : "ce lien est un lien commercial." C'est la recommandation officielle de Google depuis 2019 pour les liens d'affiliation et les liens payants.

**Pourquoi mettre les deux ?**

Nofollow est compris par tous les moteurs de recherche depuis des années. Sponsored est plus récent et plus précis. En cumulant les deux, tu couvres tous les cas. C'est la pratique recommandée.

[SCREENCAST: Création d'un lien avec les deux cases cochées]

**Dans ClickWhale, c'est simple** : à chaque création de lien affilié, coche les deux cases — **Nofollow** et **Sponsored**. Pas de réflexion à avoir, c'est systématique.

**Ce qui se passe si tu oublies :**

Google peut considérer que tu manipules ton classement en transmettant du jus SEO via des liens commerciaux non déclarés. Résultat possible : une action manuelle dans la Google Search Console. Ça veut dire une pénalité sur ton référencement, que tu devras ensuite corriger et soumettre pour réexamen. Autant faire les choses proprement dès le départ.

[TALKING HEAD]

**Règle schoolsWP à retenir** : lien affilié = nofollow + sponsored. Toujours.

**TRANSITION** : Tes liens sont bien configurés techniquement. Maintenant, il faut les organiser. Parce qu'à 10 liens, ça va. À 50, sans catégories, c'est le chaos. On voit ça dans la leçon suivante.

---

## 2.5 — Organise tes liens par catégories

**Durée cible : 5 min**

[TALKING HEAD]

10 liens, tu gères de tête. 30 liens, tu commences à chercher. 50 liens, sans organisation, tu perds du temps à chaque modification. Les catégories, c'est ce qui te permet de garder le contrôle quand ta liste grossit.

[SCREENCAST: ClickWhale > Links > Categories]

**Étape 1 — Créer tes catégories**

Dans le menu ClickWhale, va dans **Links**, puis clique sur **Categories**. Tu arrives sur l'interface de gestion des catégories. C'est le même principe que les catégories WordPress classiques : un nom, un slug, et c'est tout.

**Étape 2 — Choisir ta convention de nommage**

La convention schoolsWP suit les piliers thématiques du site :

- **LMS** — tous les liens liés à la formation en ligne (TutorLMS, LearnDash, etc.)
- **CRM** — les outils de relation client (FluentCRM, FluentSupport, etc.)
- **SEO** — les outils de référencement (RankMath, etc.)
- **Automatisation** — les outils d'automatisation (n8n, FluentCRM Automations, etc.)
- **Hébergement** — les hébergeurs WordPress

[SCREENCAST: Création de 3-4 catégories dans l'interface]

Crée tes catégories en fonction de tes thématiques à toi. L'important, c'est d'avoir une logique cohérente que tu pourras tenir dans la durée.

**Étape 3 — Assigner une catégorie à la création**

[SCREENCAST: Formulaire de création de lien > champ Category]

Quand tu crées un nouveau lien, le champ **Category** est disponible directement dans le formulaire. Prends l'habitude de l'assigner immédiatement. Revenir catégoriser 50 liens après coup, c'est une corvée que tu veux éviter.

**Étape 4 — Filtrer par catégorie**

[SCREENCAST: Liste des liens > filtre par catégorie]

De retour dans la liste des liens, tu peux filtrer par catégorie. En un coup d'œil, tu vois tous tes liens LMS, tous tes liens CRM, etc. C'est aussi utile pour vérifier que chaque catégorie est à jour : liens actifs, URLs correctes, rien de cassé.

[TALKING HEAD]

**TRANSITION** : Tes liens sont créés et organisés. Mais si tu as déjà un tableur avec 20 ou 30 liens affiliés, les créer un par un, c'est long. Dans la leçon suivante, on voit comment tout importer d'un coup via un fichier CSV.

---

## 2.6 — Importe tes liens en masse via CSV

**Durée cible : 6 min**

[TALKING HEAD]

Si tu pars de zéro, tu peux créer tes liens un par un. Mais si tu as déjà un tableur avec tes liens affiliés — ou si tu migres depuis un autre plugin — l'import CSV va te faire gagner un temps considérable.

[SCREENCAST: Google Sheets ou Excel avec un tableau de liens]

**Étape 1 — Prépare ton fichier CSV**

Ouvre ton tableur et crée les colonnes suivantes :

| Title | Slug | Target URL | Nofollow | Sponsored | Category |
|-------|------|------------|----------|-----------|----------|
| Affilié TutorLMS | tutorlms | https://www.tutorlms.com/?ref=xxx | 1 | 1 | LMS |
| Affilié FluentCRM | fluentcrm | https://fluentcrm.com/?ref=xxx | 1 | 1 | CRM |
| Affilié RankMath | rankmath | https://rankmath.com/?ref=xxx | 1 | 1 | SEO |

Quelques règles :
- **Nofollow et Sponsored** : mets `1` pour activer, `0` pour désactiver. Pour les liens affiliés, c'est toujours `1` et `1`.
- **Slug** : minuscules, pas d'espaces, pas de caractères spéciaux.
- **Category** : utilise le nom exact de la catégorie telle que tu l'as créée dans ClickWhale.

Exporte en format CSV (séparateur virgule, encodage UTF-8).

**Étape 2 — Lance l'import dans ClickWhale**

[SCREENCAST: ClickWhale > Tools > Import]

Va dans **ClickWhale > Tools > Import**. Clique sur **Choose File** et sélectionne ton fichier CSV.

**Étape 3 — Fais le mapping des colonnes**

[SCREENCAST: Interface de mapping des colonnes]

ClickWhale te demande de faire correspondre les colonnes de ton CSV avec les champs du plugin. C'est du glisser-déposer ou un menu déroulant selon la version :

- Colonne "Title" → champ **Title**
- Colonne "Slug" → champ **Slug**
- Colonne "Target URL" → champ **Target URL**
- Et ainsi de suite pour Nofollow, Sponsored, Category.

**Étape 4 — Vérifie les champs et lance l'import**

[SCREENCAST: Bouton "Run Importer" + résultat]

Avant de lancer, vérifie l'aperçu. ClickWhale te montre les premières lignes telles qu'elles seront importées. Si tout est bon, clique sur **Run Importer**.

**Étape 5 — Vérifie le résultat**

[SCREENCAST: Liste des liens après import]

Retourne dans **ClickWhale > Links**. Tes liens importés doivent apparaître dans la liste. Vérifie quelques points :
- Les slugs sont corrects
- Les catégories sont bien assignées
- Les attributs nofollow et sponsored sont activés

Teste 2 ou 3 liens au hasard en les ouvrant dans un nouvel onglet pour confirmer que les redirections fonctionnent.

[TALKING HEAD]

**TRANSITION** : Tu maîtrises maintenant la création unitaire et l'import en masse. Il est temps de mettre tout ça en pratique. Dans la leçon suivante, un exercice concret : tu vas créer 5 liens affiliés pour tes outils WordPress préférés.

---

## 2.7 — Exercice — Crée 5 liens affiliés pour tes outils WordPress préférés

**Format : Exercice pratique (pas de script vidéo)**

---

### Objectif

Mettre en pratique tout ce que tu as appris dans le Module 2 en créant 5 liens affiliés complets dans ClickWhale.

### Étapes à suivre

1. **Choisis 5 outils ou services WordPress** pour lesquels tu as (ou peux obtenir) un lien affilié. Si tu n'as pas encore de programme d'affiliation, utilise les URLs classiques des outils — tu remplaceras par les vrais liens affiliés plus tard.

2. **Crée une catégorie** pour chaque thématique si ce n'est pas déjà fait (ex : LMS, CRM, SEO, Hébergement).

3. **Pour chaque lien, remplis tous les champs** :
   - Title : nom explicite (ex : "Affilié TutorLMS — page pricing")
   - Slug : convention `/go/nom-outil` (ex : `tutorlms`)
   - Target URL : l'URL de destination
   - Redirection : **307**
   - Nofollow : **coché**
   - Sponsored : **coché**
   - Category : la catégorie correspondante
   - Description (optionnel) : taux de commission, notes utiles

4. **Teste chaque lien** en l'ouvrant dans un nouvel onglet. Vérifie que la redirection fonctionne.

5. **Vérifie dans la liste** que tes 5 liens sont bien organisés par catégorie.

### Critères de validation

- [ ] 5 liens créés dans ClickWhale
- [ ] Chaque lien a un titre explicite et un slug en minuscules
- [ ] Redirection en 307 sur les 5 liens
- [ ] Nofollow ET Sponsored cochés sur les 5 liens
- [ ] Au moins 2 catégories différentes utilisées
- [ ] Les 5 liens redirigent correctement vers la destination
- [ ] Chaque lien a une description avec au moins le taux de commission (ou "À compléter")

### Exemple de résultat attendu

| Title | Slug | Target URL | Redirect | Nofollow | Sponsored | Category |
|-------|------|-----------|----------|----------|-----------|----------|
| Affilié TutorLMS | tutorlms | https://www.tutorlms.com/?ref=xxx | 307 | Oui | Oui | LMS |
| Affilié FluentCRM | fluentcrm | https://fluentcrm.com/?ref=xxx | 307 | Oui | Oui | CRM |
| Affilié RankMath Pro | rankmath | https://rankmath.com/?ref=xxx | 307 | Oui | Oui | SEO |
| Affilié Cloudways | cloudways | https://cloudways.com/?ref=xxx | 307 | Oui | Oui | Hébergement |
| Affilié FluentSupport | fluentsupport | https://fluentsupport.com/?ref=xxx | 307 | Oui | Oui | CRM |

---

## 2.8 — Quiz — Valide tes acquis M2

**Format : QCM 8 questions (pas de script vidéo)**

---

### Question 1 — Création de lien

Quels sont les 3 champs obligatoires pour créer un lien dans ClickWhale ?

- A) Title, Slug, Description
- B) Title, Slug, Target URL
- C) Slug, Target URL, Category
- D) Title, Target URL, Nofollow

**Bonne réponse : B**

---

### Question 2 — Convention de slug

Selon la convention schoolsWP, quel slug est correct pour un lien affilié TutorLMS ?

- A) TutorLMS
- B) tutor-lms-affiliate-link
- C) tutorlms
- D) go-tutorlms

**Bonne réponse : C**

---

### Question 3 — Type de redirection

Quel type de redirection est recommandé pour les liens affiliés et pourquoi ?

- A) 301 — car il est permanent et bon pour le SEO
- B) 302 — car il est le plus courant
- C) 307 — car le navigateur ne met pas en cache, donc chaque clic est compté
- D) 308 — car il préserve la méthode HTTP

**Bonne réponse : C**

---

### Question 4 — Problème du 301

Pourquoi le 301 est-il déconseillé pour les liens affiliés ?

- A) Il est trop lent
- B) Il n'est pas compatible avec ClickWhale
- C) Le navigateur met en cache la destination, ce qui fausse le tracking
- D) Google refuse les redirections 301 sur les liens commerciaux

**Bonne réponse : C**

---

### Question 5 — Attributs SEO

Quels attributs SEO doivent être cochés sur un lien affilié ?

- A) Nofollow uniquement
- B) Sponsored uniquement
- C) Nofollow et Sponsored
- D) Aucun, ClickWhale gère automatiquement

**Bonne réponse : C**

---

### Question 6 — Rôle de Sponsored

Que signifie l'attribut `rel="sponsored"` pour Google ?

- A) Le lien est sponsorisé par Google Ads
- B) Le lien est un lien commercial ou affilié
- C) Le lien est protégé contre le spam
- D) Le lien transmet du jus SEO

**Bonne réponse : B**

---

### Question 7 — Import CSV

Dans quel ordre se déroule l'import CSV dans ClickWhale ?

- A) Upload > Run Importer > Column Mapping
- B) Column Mapping > Upload > Run Importer
- C) Upload > Column Mapping > Run Importer
- D) Run Importer > Upload > Column Mapping

**Bonne réponse : C**

---

### Question 8 — Organisation

À partir de combien de liens environ l'organisation par catégories devient-elle vraiment nécessaire ?

- A) Dès le premier lien
- B) À partir de 10 liens
- C) À partir de 50 liens, sans catégories tu es perdu
- D) Les catégories ne sont jamais nécessaires

**Bonne réponse : C**

---

*Module 2 terminé. Module suivant : le tracking et les statistiques de clics.*
