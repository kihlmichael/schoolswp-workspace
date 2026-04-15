/**
 * Templates for CLAUDE.md generation.
 * Each theme/plugin has specific rules and warnings.
 */

const THEME_TEMPLATES = {
  astra: {
    name: 'Astra',
    rules: [
      'Astra utilise des hooks custom (`astra_header_before`, `astra_content_after`, etc.) — les utiliser plutot que modifier les templates directement.',
      'Les options du theme sont stockees via `astra_get_option()` — ne pas lire directement dans `wp_options`.',
      'Le customizer Astra a sa propre API — ne pas injecter de sections custom sans passer par `Astra_Customizer`.',
    ],
    warnings: [
      'Ne jamais modifier les fichiers du theme parent Astra — toujours passer par un theme enfant.',
      'Les Astra Pro modules ajoutent des hooks supplementaires — verifier lesquels sont actifs avant intervention.',
    ],
    structure: 'Structure Astra : `astra/inc/` (core), `astra/template-parts/` (templates partiels), `astra/assets/` (CSS/JS compiles).',
  },

  generatepress: {
    name: 'GeneratePress',
    rules: [
      'GeneratePress utilise un systeme de hooks (`generate_before_header`, `generate_after_entry_content`, etc.).',
      'Le theme est volontairement leger — ne pas surcharger avec du CSS inline. Utiliser les Elements GP pour injecter du contenu.',
      'GP Premium ajoute des modules (Typography, Colors, Sections) — verifier leur activation avant de coder manuellement ce qu\'ils gerent.',
    ],
    warnings: [
      'Ne jamais modifier le theme parent GeneratePress.',
      'Les Elements GP (hooks, layouts, headers) sont stockes en base — ne pas les reproduire en code si ils existent deja.',
    ],
    structure: 'Structure GP : theme tres minimaliste. `inc/` (core), `templates/` (templates de page).',
  },

  divi: {
    name: 'Divi',
    rules: [
      'Divi stocke tout le contenu dans les shortcodes du Divi Builder — ne pas modifier le contenu des posts directement en base.',
      'Les modules custom Divi doivent etendre `ET_Builder_Module` — ne pas creer de blocks Gutenberg en parallele sauf si necessaire.',
      'Le CSS custom Divi se place dans les options du theme > Custom CSS, ou dans un theme enfant.',
    ],
    warnings: [
      'Le Divi Builder encode le layout en shortcodes — toute modification directe du `post_content` peut casser le design.',
      'Divi a son propre systeme de cache — le vider apres chaque modification de template.',
      'Ne jamais mettre a jour Divi sans backup — les mises a jour peuvent casser les layouts.',
    ],
    structure: 'Structure Divi : `includes/builder/` (Builder core), `includes/builder/module/` (modules). Theme enfant minimal recommande.',
  },

  kadence: {
    name: 'Kadence',
    rules: [
      'Kadence utilise un systeme de hooks similaire a Astra (`kadence_before_header`, `kadence_after_content`, etc.).',
      'Les options sont gerees via `kadence()->option()` — ne pas lire directement les options WP.',
      'Kadence Blocks est un plugin separe — les blocks custom Kadence sont distincts du theme.',
    ],
    warnings: [
      'Ne pas modifier le theme parent Kadence.',
      'Kadence Pro ajoute des fonctionnalites (header/footer builder, hooked elements) — verifier avant de coder manuellement.',
    ],
    structure: 'Structure Kadence : `inc/` (core), `template-parts/` (templates), `assets/` (CSS/JS).',
  },

  oceanwp: {
    name: 'OceanWP',
    rules: [
      'OceanWP a un systeme d\'extensions (Ocean Extra, Ocean Hooks, etc.) — verifier lesquelles sont actives.',
      'Le theme utilise ses propres hooks (`ocean_before_header`, `ocean_after_content`, etc.).',
      'Les metaboxes OceanWP permettent de controler le layout par page — ne pas forcer via le code ce qui peut etre gere par metabox.',
    ],
    warnings: [
      'Ne pas modifier le theme parent OceanWP.',
      'Ocean Extra est quasi obligatoire — verifier sa presence avant de supposer que certaines fonctionnalites existent.',
    ],
    structure: 'Structure OceanWP : `inc/` (core), `partials/` (templates partiels), `assets/` (CSS/JS).',
  },

  custom: {
    name: 'Theme custom',
    rules: [
      'Theme custom detecte — analyser `style.css` et `functions.php` pour comprendre la structure.',
      'Verifier si le theme suit les WordPress Coding Standards.',
      'Identifier les hooks custom declares dans `functions.php` avant d\'en creer de nouveaux.',
    ],
    warnings: [
      'Un theme custom peut avoir des conventions non standard — lire le code avant de modifier.',
      'Verifier s\'il y a un fichier README ou une documentation interne.',
    ],
    structure: 'Analyser la structure manuellement : `functions.php`, `template-parts/`, `inc/`, `assets/`.',
  },
};

const PLUGIN_TEMPLATES = {
  woocommerce: {
    name: 'WooCommerce',
    category: 'E-commerce',
    rules: [
      'WooCommerce a son propre systeme de templates dans `woocommerce/templates/` — les surcharger dans le theme via `yourtheme/woocommerce/`.',
      'Utiliser les hooks WooCommerce (`woocommerce_before_shop_loop`, `woocommerce_single_product_summary`, etc.) plutot que modifier les templates.',
      'Les donnees produit passent par `WC_Product` — ne pas lire directement les post_meta sans raison.',
      'Les commandes utilisent `WC_Order` — toujours passer par l\'API objet.',
    ],
    warnings: [
      'Ne jamais modifier les fichiers dans `wp-content/plugins/woocommerce/` directement.',
      'Les templates WooCommerce surcharges dans le theme doivent etre maintenus a chaque mise a jour de WooCommerce.',
      'WooCommerce utilise ses propres tables (`wp_wc_*`) depuis les versions recentes — ne pas supposer que tout est dans `wp_posts`.',
    ],
  },

  acf: {
    name: 'ACF (Advanced Custom Fields)',
    category: 'Custom Fields',
    rules: [
      'Les champs ACF se lisent avec `get_field()` et `the_field()` — ne pas utiliser `get_post_meta()` directement.',
      'Les groupes de champs peuvent etre exportes en PHP (`acf-json/` ou `acf_add_local_field_group()`) — verifier la methode utilisee.',
      'Si le dossier `acf-json/` existe dans le theme, les configurations sont synchronisees via JSON — ne pas les modifier en base.',
    ],
    warnings: [
      'Les champs ACF en base et en JSON peuvent entrer en conflit — ne pas melanger les deux methodes.',
      'ACF Pro ajoute des types de champs supplementaires (repeater, flexible content, gallery) — verifier la licence.',
    ],
  },

  yoast: {
    name: 'Yoast SEO',
    category: 'SEO',
    rules: [
      'Yoast gere les meta title/description — ne pas les generer manuellement dans le `<head>`.',
      'Les breadcrumbs Yoast s\'activent via `yoast_breadcrumb()` — ne pas creer un systeme parallele.',
      'Le sitemap est genere automatiquement — ne pas creer de sitemap custom sauf besoin specifique.',
    ],
    warnings: [
      'Les filtres Yoast (`wpseo_title`, `wpseo_metadesc`, etc.) peuvent entrer en conflit avec d\'autres plugins SEO.',
      'Ne pas installer Yoast et Rank Math en meme temps.',
    ],
  },

  elementor: {
    name: 'Elementor',
    category: 'Page Builder',
    rules: [
      'Elementor stocke le contenu dans les post_meta (`_elementor_data`) en JSON — ne pas modifier directement.',
      'Les widgets custom doivent etendre `\\Elementor\\Widget_Base`.',
      'Le CSS genere par Elementor est stocke dans `wp-content/uploads/elementor/css/` — ne pas modifier ces fichiers.',
    ],
    warnings: [
      'Elementor et Gutenberg peuvent coexister mais cela complexifie la maintenance — choisir un editeur principal.',
      'Les templates Elementor (header, footer, single) sont stockes comme des CPT `elementor_library` — ne pas les confondre avec les templates du theme.',
      'Elementor Pro est requis pour le Theme Builder — ne pas supposer sa presence.',
    ],
  },

  cf7: {
    name: 'Contact Form 7',
    category: 'Formulaires',
    rules: [
      'Les formulaires CF7 sont des CPT `wpcf7_contact_form` — les modifier via l\'admin ou via `wpcf7_before_send_mail` hook.',
      'Le markup HTML est dans le champ de contenu du formulaire — ne pas generer les formulaires en PHP.',
      'Les extensions CF7 (Flamingo, Conditional Fields, etc.) ajoutent des tags et des hooks specifiques.',
    ],
    warnings: [
      'CF7 ne stocke pas les soumissions par defaut — verifier si Flamingo ou un equivalent est installe.',
      'Le CSS de CF7 est minimal — les styles sont generalement dans le theme.',
    ],
  },
};

const HOSTING_TEMPLATES = {
  o2switch: {
    name: 'o2switch',
    notes: [
      'o2switch utilise cPanel — acces SSH disponible.',
      'WP-CLI generalement disponible.',
      'Pas de restrictions specifiques sur les crons WordPress.',
    ],
  },
  ovh: {
    name: 'OVH',
    notes: [
      'OVH peut avoir des restrictions sur les crons et les ressources.',
      'Verifier la version PHP disponible dans le panel.',
      'SSH pas toujours disponible selon l\'offre.',
    ],
  },
  kinsta: {
    name: 'Kinsta',
    notes: [
      'Kinsta utilise un environnement manage — pas d\'acces aux fichiers serveur hors `wp-content/`.',
      'WP-CLI disponible via SSH.',
      'Les plugins de cache sont interdits — Kinsta gere le cache au niveau serveur.',
      'Staging disponible en un clic.',
    ],
  },
  wpengine: {
    name: 'WP Engine',
    notes: [
      'WP Engine interdit certains plugins (liste sur leur site).',
      'Le cache est gere au niveau serveur — ne pas installer de plugin de cache.',
      'Git push disponible pour le deploiement.',
    ],
  },
  cloudways: {
    name: 'Cloudways',
    notes: [
      'Cloudways donne un acces SSH complet.',
      'Le serveur (DigitalOcean, Vultr, AWS, etc.) est configurable.',
      'WP-CLI disponible.',
    ],
  },
  local: {
    name: 'Local',
    notes: [
      'Environnement local detecte — les commandes serveur dependent de l\'outil utilise (DDEV, Local WP, Lando, MAMP, etc.).',
      'Verifier la methode de synchronisation avec la production (WP Migrate, duplicator, scripts custom, etc.).',
    ],
  },
};

const PAGE_BUILDER_RULES = {
  'Gutenberg (natif)': 'L\'editeur natif Gutenberg est utilise — privilegier les blocks natifs et les patterns.',
  'Elementor': 'Elementor est le page builder principal — tout le contenu visuel passe par lui.',
  'Divi Builder': 'Le Divi Builder est utilise — le contenu est stocke en shortcodes.',
  'Beaver Builder': 'Beaver Builder est utilise — les modules custom doivent etendre `FLBuilderModule`.',
  'Bricks': 'Bricks Builder est utilise — moteur de rendu custom, ne pas melanger avec Gutenberg.',
  'Oxygen': 'Oxygen Builder est utilise — il remplace completement le systeme de templates WordPress.',
  'Aucun': 'Pas de page builder — le contenu est gere via l\'editeur classique ou Gutenberg natif.',
};
