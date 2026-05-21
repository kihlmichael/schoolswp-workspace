# Brief : 3 captures inline pour l'article "Learn WordPress in a day"

> 3 captures à insérer dans l'article post 2274708 pour combler le gap section 2.5 de l'audit (médiane SERP top 10 EN : 13-22 images, l'article schoolsWP à 0).

## Pourquoi 3 captures et pas plus

- Médiane SERP top 10 EN : 13-22 images, mais le contenu de l'article est compact (2 728 mots).
- 3 captures suffisent pour couvrir les 3 moments clés du 8-hour plan sans surcharger visuellement.
- 1 capture par macro-phase : démarrage (heures 1 à 3), thème (heure 4), plugins (heure 7).

## Outils de génération IA indisponibles cette session

| Outil | Statut | Action requise |
| --- | --- | --- |
| nano-banana MCP | API key Gemini signalée "expired" sur le seul appel testé. Vu la mémoire interne sur le rate limit Gemini, ce peut être un faux signal sur le free tier OU une vraie expiration de clé. | Renouveler la clé Gemini côté env vars puis relancer. |
| aidesigner MCP | 0 crédits restants (5 sur 5 monthly free déjà utilisés, pas de Pro actif). | Upgrade Pro (25 USD par mois, 100 crédits) ou attendre le reset monthly. |
| tools/html-to-png | Disponible et brand-aware schoolsWP. | Non optimal pour mimer un dashboard WP réaliste (HTML mockup demande environ 1 h de design custom). |
| Captures réelles de ton WP | Le plus authentique. | 5 à 10 min de ton côté, donne le meilleur E-E-A-T (BRAND_RULES 16 à 18). |

## Recommandation : Route A (captures perso, E-E-A-T fort)

Tu installes WP via WordPress Playground (playground.wordpress.net) en 30 secondes, ou tu utilises un WP existant. Tu prends 3 screenshots.

### Capture 1 : Dashboard WordPress vide premier login

- Vue ciblée : /wp-admin/index.php (Dashboard home)
- État souhaité : compte fraîchement créé, 0 posts, message "Welcome to WordPress" visible
- Zoom 100 %, fenêtre 1440 px de large pour rendu retina
- Format 16:9 ou 3:2, PNG
- À montrer : sidebar gauche avec menus (Posts, Pages, Comments, Appearance, Plugins, etc.) plus zone centrale avec widgets Welcome et At a Glance
- À cropper si nécessaire : le top admin bar (pour anonymiser ton profil)
- Caption proposée : "The WordPress dashboard right after install: the home base for everything you'll do today."
- ALT proposé : "WordPress dashboard home view after first install, sidebar with main menus visible"
- Nom fichier suggéré : wordpress-dashboard-first-login.png
- Position d'insertion dans l'article : juste après le H3 "Minimum Viable Knowledge", avant la liste à puces "Here's what you'll learn to do"

### Capture 2 : Theme installer avec Kadence visible

- Vue ciblée : /wp-admin/theme-install.php avec barre de recherche taper "Kadence"
- État souhaité : grille de résultats avec la tuile Kadence en premier (avec son screenshot officiel)
- Zoom 100 %, fenêtre 1440 px
- Format 16:9 ou 3:2, PNG
- À montrer : la grille de thèmes (3 à 4 thèmes visibles, Kadence centré), avec bouton "Install" ou "Activate"
- Caption proposée : "Installing a theme is one click away. Kadence is my recommendation for beginners: lightweight, block-native, free tier generous."
- ALT proposé : "WordPress theme installer showing Kadence in the search results, with install button visible"
- Nom fichier suggéré : wordpress-theme-installer-kadence.png
- Position d'insertion : juste après le paragraphe "Hour 4 : choose a lightweight theme..." dans la section 8-hour breakdown

### Capture 3 : Plugins installer (2-3 plugins essentiels visibles)

- Vue ciblée : /wp-admin/plugin-install.php
- État souhaité : grille de plugins populaires (Featured tab par défaut) OU recherche "contact form" pour montrer Fluent Forms ou Contact Form 7
- Zoom 100 %, fenêtre 1440 px
- Format 16:9 ou 3:2, PNG
- À montrer : 3 à 4 plugin cards avec icônes, descriptions courtes, bouton "Install Now"
- Caption proposée : "Essential plugins: a contact form, a security plugin, a cache plugin. Three installs. That's enough for day one."
- ALT proposé : "WordPress plugin installer showing essential plugins like contact forms and security"
- Nom fichier suggéré : wordpress-plugin-installer-essentials.png
- Position d'insertion : juste après "Hour 7 : install 2 or 3 essential plugins..."

## Métadonnées SEO à appliquer après upload

À pousser via le pipeline schoolsWP tools/wp-media-upload qui bake les XMP et EXIF puis remplit les 4 champs WordPress (Alt text, Titre, Légende, Description). Voir aussi mémoire sur reference_wp_media_upload_tool et reference_exiftool_path (ExifTool hors PATH, à exporter avant lancement).

| Fichier | Alt text WP | Title WP | Caption WP | Description WP |
| --- | --- | --- | --- | --- |
| wordpress-dashboard-first-login.png | WordPress dashboard home view after first install, sidebar with main menus visible | WordPress dashboard first login | The WordPress dashboard right after install: the home base for everything you'll do today. | Screenshot of the WordPress dashboard immediately after a fresh installation, showing the standard sidebar navigation (Posts, Pages, Comments, Appearance, Plugins, Users, Tools, Settings) and the Welcome widget. Used in the schoolsWP article "Is it possible to learn WordPress in a day?" to illustrate the starting point of the 8-hour learning plan. |
| wordpress-theme-installer-kadence.png | WordPress theme installer showing Kadence in the search results, with install button visible | Install Kadence theme on WordPress | Installing a theme is one click away. Kadence is my recommendation for beginners. | Screenshot of the WordPress theme installer page with Kadence visible in the search results grid, install button highlighted. Used in the schoolsWP article on learning WordPress in a day to illustrate the theme selection step of the 8-hour plan. |
| wordpress-plugin-installer-essentials.png | WordPress plugin installer showing essential plugins like contact forms and security | Install essential WordPress plugins | Essential plugins: a contact form, a security plugin, a cache plugin. Three installs, that's enough for day one. | Screenshot of the WordPress plugin installer page showing essential plugins (contact forms, security, cache) with install buttons visible. Used in the schoolsWP article on learning WordPress in a day to illustrate the plugin selection step of the 8-hour plan. |

XPKeywords proposés (séparés par point-virgule) : learn wordpress in a day; wordpress for beginners; wordpress dashboard; wordpress 8 hours; kadence theme; essential wordpress plugins; schoolsWP

XPAuthor : Michaël KIHL (schoolsWP)

Copyright : © schoolsWP - schoolswp.com

## Route B fallback : prompts IA prêts à l'emploi

Si tu décides plus tard de générer en IA (après renouvellement Gemini ou upgrade aidesigner), utilise ces 3 prompts. Régler aspect_ratio "16:9" et quality "high".

### Prompt 1 - Dashboard scene

Flat editorial illustration, landscape 16:9, for a WordPress learning article. Over-the-shoulder view of a young creator at a clean modern desk. Their laptop screen shows a simplified WordPress admin dashboard: a thin gray sidebar on the left with menu items represented as horizontal lines and small icons, and a main content area on the right with white cards labeled with placeholder rectangles. On the desk: an open notebook with hour numbers from one to eight written by hand, a ceramic coffee cup, a small potted plant. Background: a softly lit beige wall with one small framed poster. Color palette: dominant white and warm cream, accent fresh green like a young leaf for dashboard highlights and notebook checkmarks, dark slate blue for outlines and small text. No purple, no neon, no pink. Style: clean flat vector illustration, minimal shadows, warm natural side lighting. No text labels readable except placeholder rectangles. No watermark. Professional, magazine cover quality.

### Prompt 2 - Theme selection scene

Flat editorial illustration, landscape 16:9, for a WordPress beginners article. Top-down view of three website thumbnails floating side by side on a clean cream desk, like physical cards. The center thumbnail is highlighted with a fresh green accent border and a small selected tick mark. Around the thumbnails: a smartphone showing a small live preview, a stylus, a notebook page with the word "theme" written at the top. Color palette: white, cream, fresh leaf green for accents, dark slate blue for outlines. No purple, no pink, no neon. Style: flat vector, minimal shadows, soft top lighting. No readable text inside the thumbnails, just abstract layout placeholders (header, hero image, three columns). No watermark.

### Prompt 3 - Plugin selection scene

Flat editorial illustration, landscape 16:9, for a WordPress beginners article. A clean cream desk top-down view showing three card-like plugin icons arranged in a row: one shaped like a small letter envelope with a checkmark, one shaped like a small shield, one shaped like a small lightning bolt. Each card has a tiny placeholder name strip and a small install button represented as a green pill. A laptop edge is visible at the top of the frame. A notebook page nearby has the word "plugins" written at the top with a checkbox list of three items, two ticked. Color palette: white, cream, fresh leaf green for action buttons and checkmarks, dark slate blue for outlines. No purple, no pink, no neon. Style: flat vector, minimal shadows, soft top lighting. No readable text inside the icons. No watermark.

## Recommandation finale

Route A (vraies captures perso) si tu as 5 à 10 min. C'est plus authentique, plus crédible pour E-E-A-T, et plus aligné avec les BRAND_RULES 16 à 18 (proof points testés personnellement).

Route B (IA stylisée) si tu veux scaler la production sans toucher à WP. Cohérent visuellement avec un article-blog éducatif, mais moins crédible pour démontrer une expertise réelle.

Tu choisis. Une fois les fichiers prêts, push via le pipeline tools/wp-media-upload (avec ExifTool dans le PATH).
