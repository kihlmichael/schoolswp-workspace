# Méthode : construire un site WordPress avec Claude (Darrel Wilson, 2026)

> **Source** : vidéo YouTube "(REALLY) Build a WordPress Website with Claude in 2026" - chaîne Darrel Wilson (509 k abonnés)
> **URL** : https://www.youtube.com/watch?v=El484PgSHEk
> **Durée** : 34:49 - **Publiée** : 1 juin 2026 - **Vues** : 36 k (au 05/06/2026)
> **Transcript** : récupéré via DataForSEO (sous-titres EN auto-générés)
> **Intérêt schoolsWP** : la vidéo entière repose sur **NovaMira** (plugin Michaël) comme connecteur MCP WordPress <-> Claude. Voir l'analyse produit associée : [2026-06-05_analyse-novamira-video-darrel-wilson.md](2026-06-05_analyse-novamira-video-darrel-wilson.md)

---

## Le principe directeur

L'erreur que presque tout le monde fait : générer un site avec l'IA puis enchaîner les prompts à l'infini ("agrandis le bouton, déplace la section, corrige l'espacement...") jusqu'à ce qu'après 45 prompts le site soit **pire** qu'au départ.

La bonne approche tient en **3 étapes** :

1. **Claude crée le design** (en HTML)
2. **Tu installes WordPress** (hébergement Hostinger)
3. **Tu importes le design dans WordPress** (Elementor + NovaMira) pour le customiser proprement avec un page builder, au lieu de re-prompter.

---

## ÉTAPE 1 - Créer le design avec Claude

### 1.1 Installer Claude Desktop

- Télécharger sur **claude.com/download** la **version Desktop**.
- Piège : la **version navigateur ne fonctionne pas** pour la suite (c'est elle qui permettra de brancher le MCP sur WordPress).

### 1.2 Le prompt de génération (verbatim)

> _"Design a complete five-page website for my business using HTML. Make it look modern, clean, and professional, and give it a unique design, and make sure the design beats my competitors."_

Y ajouter :

- **Nom de l'entreprise**, activité, clients ciblés, objectif du site (leads, prise de RDV...).
- **Emphase de design** optionnelle ("award-style websites", "a split-screen effect", "a checkered effect on the homepage").
- Pages par défaut générées : **home, about, services, listing, contact** (ajoutable : "my team", "portfolio").

### 1.3 Mots-clés SEO (à ne pas zapper)

Insérer les **SEO keywords dès ce premier prompt**, sinon "it's just going to give you a bunch of generic crap". Exemple : "real estate services in Las Vegas, Las Vegas realtor". Dosage conseillé : jusqu'à ~10 mots-clés, pas plus.

### 1.4 Couleurs / polices

Par défaut, laisser l'IA décider. Sinon imposer ("a blue and brown and white website with Poppins bold fonts and Lato"). Le prompt impose aussi : tous les liens/boutons fonctionnels, images ajoutées, "SEO ready".

### 1.5 Choisir le modèle

- **Gratuit** : Sonnet ou Haiku suffisent ("you can do all this in the free version").
- Lui utilise **Opus + adaptive thinking** (compte payant).

### 1.6 Générer + premier aperçu

- Génération en ~3 à 5 min.
- Les images ne s'affichent pas dans l'aperçu Claude Desktop : **ouvrir le rendu dans Google Chrome** pour voir le vrai résultat.

### 1.7 Prompt de polish/debug (verbatim)

> _"Polish up the website, go throughout the website and look for any design inconsistencies and fix them. Make sure all links are working and debug the website for any issues."_

Ne **pas** corriger les textes par re-prompt ici : ce sera plus rapide dans le page builder.

---

## ÉTAPE 2 - Installer WordPress (Hostinger)

### 2.1 Plan & promo

- Hébergeur recommandé : **Hostinger**, garantie 30 jours.
- Plan **Business** (jusqu'à 50 sites, stockage NVMe rapide). Le plan Premium est limité à 3 sites/SSD.
- Durée : **48 mois** = remise max. Budget serré -> **12 mois** (qualifie pour le **domaine gratuit**).
- Code promo **darrell10** -> -10 % supplémentaires. Apply -> Continue.

### 2.2 Compte + paiement

Email + mot de passe -> Register. Adresse de facturation. Paiement CB / PayPal / Google Pay -> Submit payment.

### 2.3 Setup initial

- "Who is this website for?" -> **myself or for my business** -> Next.
- **Create a website** -> Next.
- Créer les **identifiants WordPress** (à noter précieusement) -> Next.

### 2.4 Domaine gratuit

Saisir le nom de domaine, vérifier la dispo, sélectionner -> renseigner les **owner details** (indispensable pour transférer/revendre plus tard) -> Register. Indiquer le pays cible -> Next. WordPress s'installe (quelques minutes) -> **Go to WordPress**.

### 2.5 Vérifier domaine & email (critique)

Dans la boîte mail Hostinger, **2 emails** à valider (compte + domaine) -> "Verify email" sur les deux.
ATTENTION : sans vérification sous **30 jours** : remboursement automatique + fermeture du compte.

### 2.6 Se connecter

- Direct : `tondomaine.com/wp-admin` -> identifiants WordPress.
- Ou via Hostinger : compte -> Websites -> All websites -> bouton **wp-admin** (connexion sans mot de passe via hPanel).

---

## ÉTAPE 2 bis - Thème + 4 plugins

### Thème : **Astra**

Appearance > Themes -> Install -> Activate.

### Les 4 plugins (Plugins > Add plugin)

1. **Elementor** (page builder gratuit). Si un wizard s'ouvre : skip, skip, skip.
2. **WPForms** (formulaire de contact).
3. **Xpro Theme Builder for Elementor - Free** (+ module XPro Add-ons).
   - _Pourquoi_ : il permet de construire **header/footer custom gratuitement**. Les thèmes (5 testés) gèrent mal le customizer à l'import -> on fait fabriquer header/footer par Elementor pour limiter les erreurs.
4. **NovaMira** (plugin Michaël - **pas dans le répertoire WP**). Télécharger le zip sur le site dédié -> Plugins > Add plugin > Upload plugin > Choose file -> Install now -> Activate.
   - _Rôle_ : il fait le **pont WordPress <-> Claude (MCP)** et apprend à l'IA à utiliser les éléments Elementor.

### Réglages Elementor critiques (Elementor > Settings)

- **Désactiver l'Atomic editor** (sauf si tu es développeur). Deactivate -> cocher "I've read and understood".
- Onglet **Features** -> option **Container** -> **Active** -> Save.
  - _Pourquoi_ : force Claude à utiliser le **flexbox moderne** au lieu des sections dépréciées.

### Installer **Node.js**

Fiabilise l'export (Claude génère parfois du **React** au lieu de HTML -> échec d'export sinon). Télécharger sur nodejs.org -> Get Node.js -> installer (Continue, Agree, Install).

---

## ÉTAPE 2 ter - Connecter WordPress à Claude (MCP)

1. Menu **NovaMira > Configuration** -> cocher **"turn on AI abilities for this site"** -> Save.
2. **Generate application password**.
3. Cliquer le lien de config client -> choisir **Claude Desktop** -> **Copy** le code de config affiché.
4. Dans Claude : **profil > Settings > Developer > Edit config** -> ouvre `claude_desktop_config.json`.
5. Double-cliquer le fichier, **tout supprimer**, **coller** le code (Ctrl+V).
6. **File > Save** (jamais "Save as" : ça crée un doublon et recharge l'ancien script).
7. **Quitter complètement Claude** (Quit) puis le rouvrir -> Settings > Developer doit afficher le **MCP running** = connecté.

---

## ÉTAPE 3 - Convertir le design en Elementor

### Prompt d'import (le plus important - verbatim)

> _"...take this design and convert it for the Elementor page builder for WordPress. Make sure to use the native Elementor elements and not HTML widgets. We have installed the Nova Mira plugin to help you understand how to use the Elementor elements better."_ (+ "create a new menu for the pages", "set the homepage")

- _Pourquoi_ : sans l'instruction "native Elementor elements", Claude crache des blocs HTML aléatoires.

### Header/footer (verbatim)

> _"Next, use X Pro to create the header and footer. This plugin allows you to build a custom header and footer with Elementor. Make sure to save the header and footer template in the X Pro library so I can customize them later."_

### Contact + URL (verbatim)

> _"use WP Forms as the contact form for the contact page."_

ATTENTION : mettre l'**URL du domaine en https**, jamais `www.com` (sinon mauvais répertoire / pas de SSL).

### Exécution

- À la 1re demande de permission -> **"always allow"**.
- Bug ~1 fois sur 10 (Claude hésite) : reprompter en ajoutant _"Have the Nova Mira plugin help you."_
- Conversion complète ~ **12 minutes**.

---

## ÉTAPE 3 bis - Corrections finales

### Header/footer manquants (très fréquent)

Souvent en **draft** dans Xpro -> crayon -> ouvrir avec Elementor -> **Publish** (header) / **Display on > Entire website** + Update (footer). Si toujours absent, demander à Claude (verbatim) :

> _"The header and footer are not displaying on the website with the XPro plugin. Can you debug the footer and header and make sure they display? And also make sure the templates are available in the library."_

### Problème de wrap (flexbox)

Claude gère mal le wrap. Symptôme : sections décalées. Fix : sélectionner le **flexbox** de la section -> **No wrap** (et **center** pour recentrer un footer trop bas).

### Images & widgets HTML résiduels

Les images viennent d'une **URL**, pas de la médiathèque -> les ré-uploader (ex. depuis Unsplash) en image de fond de container, position **cover**. Supprimer les **widgets HTML** que Claude a créés faute de mieux et les remplacer par les vrais éléments Elementor.

---

## Récap stack & pièges

**Stack** : Claude Desktop (Opus/Sonnet/Haiku) - Hostinger Business - thème Astra - Elementor + WPForms + Xpro + **NovaMira** - Node.js - Unsplash pour les images.

**Pièges à éviter** :

- Claude Desktop obligatoire (pas le navigateur)
- SEO keywords dès le 1er prompt
- Vérifier l'email Hostinger sous 30 jours
- Container = Active + Atomic editor désactivé dans Elementor
- Node.js installé (cas React)
- `claude_desktop_config.json` : **Save**, jamais "Save as"
- URL en **https**, jamais `www.com`
- Forcer "native Elementor elements, not HTML widgets"

---

## Tous les prompts (verbatim, à copier-coller)

1. **Génération** : _"Design a complete five-page website for my business using HTML. Make it look modern, clean, and professional, and give it a unique design, and make sure the design beats my competitors."_
2. **Polish/debug** : _"Polish up the website, go throughout the website and look for any design inconsistencies and fix them. Make sure all links are working and debug the website for any issues."_
3. **Import Elementor** : _"...take this design and convert it for the Elementor page builder for WordPress. Make sure to use the native Elementor elements and not HTML widgets. We have installed the Nova Mira plugin to help you understand how to use the Elementor elements better."_
4. **Header/footer** : _"Next, use X Pro to create the header and footer. This plugin allows you to build a custom header and footer with Elementor. Make sure to save the header and footer template in the X Pro library so I can customize them later."_
5. **Contact** : _"use WP Forms as the contact form for the contact page."_
6. **Fix header/footer** : _"The header and footer are not displaying on the website with the XPro plugin. Can you debug the footer and header and make sure they display? And also make sure the templates are available in the library."_
