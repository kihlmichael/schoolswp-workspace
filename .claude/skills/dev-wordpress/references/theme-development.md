# Theme Development — schoolsWP Dev Skills

Guide pour le développement de thèmes WordPress blocs selon les standards modernes.

## Structure d'un thème bloc

```
schoolswp-theme/
├── style.css                 # Métadonnées uniquement
├── theme.json                # Configuration centrale
├── functions.php             # Minimal (optionnel)
├── templates/
│   ├── index.html            # Template par défaut (obligatoire)
│   ├── single.html           # Articles
│   ├── page.html             # Pages
│   ├── archive.html          # Archives
│   ├── search.html           # Recherche
│   ├── 404.html              # Erreur 404
│   └── home.html             # Page d'accueil blog
├── parts/
│   ├── header.html           # En-tête
│   ├── footer.html           # Pied de page
│   └── sidebar.html          # Barre latérale
├── patterns/
│   ├── hero.php              # Pattern Hero
│   └── cta.php               # Pattern CTA
└── assets/
    ├── fonts/                # Polices locales
    └── images/               # Images du thème
```

## style.css (métadonnées)

```css
/*
Theme Name: schoolsWP Theme
Theme URI: https://schoolswp.com/themes/schoolswp-theme
Author: schoolsWP
Author URI: https://schoolswp.com
Description: Thème bloc moderne pour schoolsWP.
Requires at least: 6.4
Tested up to: 6.9
Requires PHP: 8.0
Version: 1.0.0
License: GNU General Public License v2 or later
License URI: https://www.gnu.org/licenses/gpl-2.0.html
Text Domain: schoolswp-theme
Tags: block-patterns, block-styles, editor-style, full-site-editing, wide-blocks
*/

/* Les styles vont dans theme.json, pas ici */
```

## theme.json (configuration centrale)

```json
{
  "$schema": "https://schemas.wp.org/trunk/theme.json",
  "version": 3,
  "settings": {
    "appearanceTools": true,
    "useRootPaddingAwareAlignments": true,
    "layout": {
      "contentSize": "720px",
      "wideSize": "1200px"
    },
    "color": {
      "palette": [
        {
          "slug": "primary",
          "color": "#0073aa",
          "name": "Primary"
        },
        {
          "slug": "secondary",
          "color": "#23282d",
          "name": "Secondary"
        },
        {
          "slug": "accent",
          "color": "#00a0d2",
          "name": "Accent"
        },
        {
          "slug": "background",
          "color": "#ffffff",
          "name": "Background"
        },
        {
          "slug": "foreground",
          "color": "#1e1e1e",
          "name": "Foreground"
        }
      ],
      "gradients": [
        {
          "slug": "primary-to-secondary",
          "gradient": "linear-gradient(135deg, var(--wp--preset--color--primary) 0%, var(--wp--preset--color--secondary) 100%)",
          "name": "Primary to Secondary"
        }
      ]
    },
    "typography": {
      "fluid": true,
      "fontFamilies": [
        {
          "fontFamily": "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen-Sans, Ubuntu, Cantarell, 'Helvetica Neue', sans-serif",
          "slug": "system",
          "name": "System"
        },
        {
          "fontFamily": "'Inter', sans-serif",
          "slug": "inter",
          "name": "Inter",
          "fontFace": [
            {
              "fontFamily": "Inter",
              "fontWeight": "400",
              "fontStyle": "normal",
              "fontStretch": "normal",
              "src": ["file:./assets/fonts/inter-regular.woff2"]
            },
            {
              "fontFamily": "Inter",
              "fontWeight": "700",
              "fontStyle": "normal",
              "fontStretch": "normal",
              "src": ["file:./assets/fonts/inter-bold.woff2"]
            }
          ]
        }
      ],
      "fontSizes": [
        {
          "slug": "small",
          "size": "0.875rem",
          "name": "Small",
          "fluid": {
            "min": "0.875rem",
            "max": "1rem"
          }
        },
        {
          "slug": "medium",
          "size": "1rem",
          "name": "Medium",
          "fluid": {
            "min": "1rem",
            "max": "1.125rem"
          }
        },
        {
          "slug": "large",
          "size": "1.5rem",
          "name": "Large",
          "fluid": {
            "min": "1.25rem",
            "max": "1.5rem"
          }
        },
        {
          "slug": "x-large",
          "size": "2.25rem",
          "name": "Extra Large",
          "fluid": {
            "min": "1.75rem",
            "max": "2.25rem"
          }
        }
      ]
    },
    "spacing": {
      "units": ["px", "rem", "em", "%", "vw", "vh"],
      "spacingSizes": [
        { "slug": "10", "size": "0.625rem", "name": "1" },
        { "slug": "20", "size": "1rem", "name": "2" },
        { "slug": "30", "size": "1.5rem", "name": "3" },
        { "slug": "40", "size": "2rem", "name": "4" },
        { "slug": "50", "size": "3rem", "name": "5" },
        { "slug": "60", "size": "4rem", "name": "6" }
      ]
    },
    "border": {
      "radius": true,
      "color": true,
      "style": true,
      "width": true
    },
    "shadow": {
      "presets": [
        {
          "slug": "small",
          "shadow": "0 1px 3px rgba(0,0,0,0.12)",
          "name": "Small"
        },
        {
          "slug": "medium",
          "shadow": "0 4px 6px rgba(0,0,0,0.1)",
          "name": "Medium"
        }
      ]
    }
  },
  "styles": {
    "color": {
      "background": "var(--wp--preset--color--background)",
      "text": "var(--wp--preset--color--foreground)"
    },
    "typography": {
      "fontFamily": "var(--wp--preset--font-family--system)",
      "fontSize": "var(--wp--preset--font-size--medium)",
      "lineHeight": "1.6"
    },
    "spacing": {
      "padding": {
        "top": "0",
        "right": "var(--wp--preset--spacing--30)",
        "bottom": "0",
        "left": "var(--wp--preset--spacing--30)"
      }
    },
    "elements": {
      "link": {
        "color": {
          "text": "var(--wp--preset--color--primary)"
        },
        ":hover": {
          "color": {
            "text": "var(--wp--preset--color--accent)"
          }
        }
      },
      "button": {
        "color": {
          "background": "var(--wp--preset--color--primary)",
          "text": "var(--wp--preset--color--background)"
        },
        "border": {
          "radius": "4px"
        },
        ":hover": {
          "color": {
            "background": "var(--wp--preset--color--secondary)"
          }
        }
      },
      "heading": {
        "typography": {
          "fontWeight": "700",
          "lineHeight": "1.2"
        },
        "color": {
          "text": "var(--wp--preset--color--foreground)"
        }
      }
    },
    "blocks": {
      "core/navigation": {
        "typography": {
          "fontSize": "var(--wp--preset--font-size--small)"
        }
      },
      "core/post-title": {
        "typography": {
          "fontSize": "var(--wp--preset--font-size--x-large)"
        }
      }
    }
  },
  "templateParts": [
    {
      "name": "header",
      "title": "Header",
      "area": "header"
    },
    {
      "name": "footer",
      "title": "Footer",
      "area": "footer"
    }
  ],
  "customTemplates": [
    {
      "name": "blank",
      "title": "Blank",
      "postTypes": ["page"]
    },
    {
      "name": "landing",
      "title": "Landing Page",
      "postTypes": ["page"]
    }
  ]
}
```

## Templates HTML

### templates/index.html

```html
<!-- wp:template-part {"slug":"header","area":"header"} /-->

<!-- wp:group {"tagName":"main","layout":{"type":"constrained"}} -->
<main class="wp-block-group">
  <!-- wp:query {"queryId":1,"query":{"perPage":10,"pages":0,"offset":0,"postType":"post","order":"desc","orderBy":"date","inherit":true}} -->
  <div class="wp-block-query">
    <!-- wp:post-template -->
    <!-- wp:post-title {"isLink":true} /-->
    <!-- wp:post-excerpt /-->
    <!-- wp:post-date /-->
    <!-- /wp:post-template -->

    <!-- wp:query-pagination -->
    <!-- wp:query-pagination-previous /-->
    <!-- wp:query-pagination-numbers /-->
    <!-- wp:query-pagination-next /-->
    <!-- /wp:query-pagination -->
  </div>
  <!-- /wp:query -->
</main>
<!-- /wp:group -->

<!-- wp:template-part {"slug":"footer","area":"footer"} /-->
```

### parts/header.html

```html
<!-- wp:group {"tagName":"header","style":{"spacing":{"padding":{"top":"var:preset|spacing|30","bottom":"var:preset|spacing|30"}}},"layout":{"type":"constrained"}} -->
<header class="wp-block-group">
  <!-- wp:group {"layout":{"type":"flex","justifyContent":"space-between","flexWrap":"wrap"}} -->
  <div class="wp-block-group">
    <!-- wp:site-title {"level":0} /-->
    <!-- wp:navigation {"layout":{"type":"flex","justifyContent":"right"}} /-->
  </div>
  <!-- /wp:group -->
</header>
<!-- /wp:group -->
```

## Patterns

### patterns/hero.php

```php
<?php
/**
 * Title: Hero Section
 * Slug: schoolswp-theme/hero
 * Categories: featured
 * Keywords: hero, banner, header
 * Block Types: core/group
 */
?>
<!-- wp:cover {"overlayColor":"primary","minHeight":500,"align":"full","layout":{"type":"constrained"}} -->
<div class="wp-block-cover alignfull" style="min-height:500px">
  <span aria-hidden="true" class="wp-block-cover__background has-primary-background-color has-background-dim-100 has-background-dim"></span>
  <div class="wp-block-cover__inner-container">
    <!-- wp:heading {"textAlign":"center","level":1,"textColor":"background"} -->
    <h1 class="wp-block-heading has-text-align-center has-background-color has-text-color">
      <?php esc_html_e( 'Bienvenue sur schoolsWP', 'schoolswp-theme' ); ?>
    </h1>
    <!-- /wp:heading -->

    <!-- wp:paragraph {"align":"center","textColor":"background"} -->
    <p class="has-text-align-center has-background-color has-text-color">
      <?php esc_html_e( 'WordPress rendu simple, structuré et efficace.', 'schoolswp-theme' ); ?>
    </p>
    <!-- /wp:paragraph -->

    <!-- wp:buttons {"layout":{"type":"flex","justifyContent":"center"}} -->
    <div class="wp-block-buttons">
      <!-- wp:button {"backgroundColor":"background","textColor":"primary"} -->
      <div class="wp-block-button">
        <a class="wp-block-button__link has-primary-color has-background-background-color has-text-color has-background wp-element-button">
          <?php esc_html_e( 'Commencer', 'schoolswp-theme' ); ?>
        </a>
      </div>
      <!-- /wp:button -->
    </div>
    <!-- /wp:buttons -->
  </div>
</div>
<!-- /wp:cover -->
```

## functions.php (minimal)

```php
<?php
/**
 * schoolsWP Theme functions.
 *
 * @package schoolswp-theme
 */

declare( strict_types=1 );

if ( ! defined( 'ABSPATH' ) ) {
  exit;
}

/**
 * Enqueue block styles.
 */
add_action( 'wp_enqueue_scripts', function(): void {
  // Les styles du thème sont gérés par theme.json
  // Utiliser uniquement pour des cas spécifiques
} );

/**
 * Register block patterns category.
 */
add_action( 'init', function(): void {
  register_block_pattern_category(
    'schoolswp',
    [
      'label' => __( 'schoolsWP', 'schoolswp-theme' ),
    ]
  );
} );

/**
 * Register block styles.
 */
add_action( 'init', function(): void {
  register_block_style(
    'core/button',
    [
      'name'  => 'outline',
      'label' => __( 'Outline', 'schoolswp-theme' ),
    ]
  );
} );
```

## Style variations

Créer un fichier dans `styles/dark.json` :

```json
{
  "$schema": "https://schemas.wp.org/trunk/theme.json",
  "version": 3,
  "title": "Dark",
  "settings": {
    "color": {
      "palette": [
        {
          "slug": "background",
          "color": "#1e1e1e",
          "name": "Background"
        },
        {
          "slug": "foreground",
          "color": "#ffffff",
          "name": "Foreground"
        }
      ]
    }
  },
  "styles": {
    "color": {
      "background": "var(--wp--preset--color--background)",
      "text": "var(--wp--preset--color--foreground)"
    }
  }
}
```

## Checklist de vérification

- [ ] `style.css` avec header complet (tags: `full-site-editing`, `block-patterns`)
- [ ] `theme.json` version 3 avec `$schema`
- [ ] `templates/index.html` présent (obligatoire)
- [ ] Template parts dans `/parts` avec `area` déclarée
- [ ] Patterns dans `/patterns` avec header PHP
- [ ] Typographie fluide configurée
- [ ] Palette de couleurs cohérente avec brand
- [ ] `useRootPaddingAwareAlignments: true` pour les alignements
- [ ] Polices locales (pas de Google Fonts externes pour RGPD)
- [ ] Textes internationalisés dans les patterns

## Ressources

- [Block Theme Handbook](https://developer.wordpress.org/themes/block-themes/)
- [theme.json Reference](https://developer.wordpress.org/themes/global-settings-and-styles/)
- [Create Block Theme Plugin](https://wordpress.org/plugins/create-block-theme/)
