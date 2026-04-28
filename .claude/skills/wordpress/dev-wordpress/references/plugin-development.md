# Plugin Development — schoolsWP Dev Skills

Guide pour le développement de plugins WordPress selon les standards modernes.

## Structure recommandée

```
schoolswp-plugin/
├── schoolswp-plugin.php      # Point d'entrée unique
├── composer.json             # Dépendances et autoloading
├── package.json              # Build assets (optionnel)
├── uninstall.php             # Nettoyage à la désinstallation
├── readme.txt                # Documentation WordPress.org
├── src/
│   ├── Plugin.php            # Classe principale
│   ├── Admin/                # Fonctionnalités admin
│   ├── Frontend/             # Fonctionnalités frontend
│   ├── REST/                 # Endpoints REST API
│   └── Blocks/               # Blocs Gutenberg
├── assets/
│   ├── css/
│   ├── js/
│   └── images/
├── languages/                # Traductions
├── templates/                # Templates PHP
└── tests/                    # Tests PHPUnit
```

## Point d'entrée

```php
<?php
/**
 * Plugin Name:       schoolsWP Plugin
 * Plugin URI:        https://schoolswp.com/plugins/plugin-name
 * Description:       Description du plugin.
 * Version:           1.0.0
 * Requires at least: 6.4
 * Requires PHP:      8.0
 * Author:            schoolsWP
 * Author URI:        https://schoolswp.com
 * License:           GPL v2 or later
 * License URI:       https://www.gnu.org/licenses/gpl-2.0.html
 * Text Domain:       schoolswp-plugin
 * Domain Path:       /languages
 */

declare( strict_types=1 );

namespace SchoolsWP\Plugin;

// Protection accès direct
if ( ! defined( 'ABSPATH' ) ) {
  exit;
}

// Constantes
define( 'SCHOOLSWP_PLUGIN_VERSION', '1.0.0' );
define( 'SCHOOLSWP_PLUGIN_FILE', __FILE__ );
define( 'SCHOOLSWP_PLUGIN_DIR', plugin_dir_path( __FILE__ ) );
define( 'SCHOOLSWP_PLUGIN_URL', plugin_dir_url( __FILE__ ) );

// Autoloading
require_once SCHOOLSWP_PLUGIN_DIR . 'vendor/autoload.php';

// Initialisation
add_action( 'plugins_loaded', [ Plugin::class, 'init' ] );

// Activation / Désactivation
register_activation_hook( __FILE__, [ Activator::class, 'activate' ] );
register_deactivation_hook( __FILE__, [ Deactivator::class, 'deactivate' ] );
```

## Classe principale

```php
<?php

declare( strict_types=1 );

namespace SchoolsWP\Plugin;

class Plugin {
  private static ?self $instance = null;

  public static function init(): self {
    if ( null === self::$instance ) {
      self::$instance = new self();
    }
    return self::$instance;
  }

  private function __construct() {
    $this->load_textdomain();
    $this->register_hooks();
  }

  private function load_textdomain(): void {
    load_plugin_textdomain(
      'schoolswp-plugin',
      false,
      dirname( plugin_basename( SCHOOLSWP_PLUGIN_FILE ) ) . '/languages'
    );
  }

  private function register_hooks(): void {
    // Admin uniquement
    if ( is_admin() ) {
      add_action( 'admin_menu', [ Admin\Settings::class, 'register_menu' ] );
      add_action( 'admin_init', [ Admin\Settings::class, 'register_settings' ] );
    }

    // Frontend uniquement
    if ( ! is_admin() ) {
      add_action( 'wp_enqueue_scripts', [ Frontend\Assets::class, 'enqueue' ] );
    }

    // Toujours
    add_action( 'init', [ $this, 'register_post_types' ] );
    add_action( 'rest_api_init', [ REST\Routes::class, 'register' ] );
  }

  public function register_post_types(): void {
    // Enregistrement des CPT
  }
}
```

## Activation / Désactivation

```php
<?php

declare( strict_types=1 );

namespace SchoolsWP\Plugin;

class Activator {
  public static function activate(): void {
    // Vérifier les prérequis
    if ( version_compare( PHP_VERSION, '8.0', '<' ) ) {
      deactivate_plugins( plugin_basename( SCHOOLSWP_PLUGIN_FILE ) );
      wp_die( 'Ce plugin requiert PHP 8.0 ou supérieur.' );
    }

    // Créer les tables personnalisées
    self::create_tables();

    // Options par défaut
    add_option( 'schoolswp_plugin_version', SCHOOLSWP_PLUGIN_VERSION );

    // Flush rewrite rules (si CPT)
    flush_rewrite_rules();
  }

  private static function create_tables(): void {
    global $wpdb;

    $charset_collate = $wpdb->get_charset_collate();
    $table_name = $wpdb->prefix . 'schoolswp_data';

    $sql = "CREATE TABLE $table_name (
      id bigint(20) unsigned NOT NULL AUTO_INCREMENT,
      user_id bigint(20) unsigned NOT NULL,
      data longtext NOT NULL,
      created_at datetime DEFAULT CURRENT_TIMESTAMP,
      PRIMARY KEY (id),
      KEY user_id (user_id)
    ) $charset_collate;";

    require_once ABSPATH . 'wp-admin/includes/upgrade.php';
    dbDelta( $sql );
  }
}

class Deactivator {
  public static function deactivate(): void {
    // Nettoyer les tâches cron
    wp_clear_scheduled_hook( 'schoolswp_daily_task' );

    // Flush rewrite rules
    flush_rewrite_rules();
  }
}
```

## Désinstallation (uninstall.php)

```php
<?php
/**
 * Nettoyage à la désinstallation.
 */

// Protection
if ( ! defined( 'WP_UNINSTALL_PLUGIN' ) ) {
  exit;
}

global $wpdb;

// Supprimer les options
delete_option( 'schoolswp_plugin_version' );
delete_option( 'schoolswp_plugin_settings' );

// Supprimer les options utilisateur (multisite-aware)
$wpdb->query( "DELETE FROM {$wpdb->usermeta} WHERE meta_key LIKE 'schoolswp_plugin_%'" );

// Supprimer les tables personnalisées
$wpdb->query( "DROP TABLE IF EXISTS {$wpdb->prefix}schoolswp_data" );

// Supprimer les fichiers uploadés (optionnel)
// wp_delete_file( ... );

// Nettoyer le cache
wp_cache_flush();
```

## Settings API

```php
<?php

declare( strict_types=1 );

namespace SchoolsWP\Plugin\Admin;

class Settings {
  public const OPTION_NAME = 'schoolswp_plugin_settings';
  public const PAGE_SLUG = 'schoolswp-plugin';

  public static function register_menu(): void {
    add_options_page(
      __( 'schoolsWP Plugin', 'schoolswp-plugin' ),
      __( 'schoolsWP Plugin', 'schoolswp-plugin' ),
      'manage_options',
      self::PAGE_SLUG,
      [ self::class, 'render_page' ]
    );
  }

  public static function register_settings(): void {
    register_setting(
      self::PAGE_SLUG,
      self::OPTION_NAME,
      [
        'type'              => 'array',
        'sanitize_callback' => [ self::class, 'sanitize' ],
        'default'           => self::defaults(),
      ]
    );

    add_settings_section(
      'general',
      __( 'Paramètres généraux', 'schoolswp-plugin' ),
      '__return_null',
      self::PAGE_SLUG
    );

    add_settings_field(
      'api_key',
      __( 'Clé API', 'schoolswp-plugin' ),
      [ self::class, 'render_text_field' ],
      self::PAGE_SLUG,
      'general',
      [
        'label_for' => 'api_key',
        'type'      => 'password',
      ]
    );

    add_settings_field(
      'enable_feature',
      __( 'Activer la fonctionnalité', 'schoolswp-plugin' ),
      [ self::class, 'render_checkbox' ],
      self::PAGE_SLUG,
      'general',
      [
        'label_for' => 'enable_feature',
      ]
    );
  }

  public static function defaults(): array {
    return [
      'api_key'        => '',
      'enable_feature' => false,
    ];
  }

  public static function sanitize( array $input ): array {
    $output = self::defaults();

    if ( isset( $input['api_key'] ) ) {
      $output['api_key'] = sanitize_text_field( $input['api_key'] );
    }

    $output['enable_feature'] = ! empty( $input['enable_feature'] );

    return $output;
  }

  public static function get( string $key = '' ): mixed {
    $options = get_option( self::OPTION_NAME, self::defaults() );
    $options = wp_parse_args( $options, self::defaults() );

    if ( $key ) {
      return $options[ $key ] ?? null;
    }

    return $options;
  }

  public static function render_page(): void {
    if ( ! current_user_can( 'manage_options' ) ) {
      return;
    }
    ?>
    <div class="wrap">
      <h1><?php echo esc_html( get_admin_page_title() ); ?></h1>
      <form action="options.php" method="post">
        <?php
        settings_fields( self::PAGE_SLUG );
        do_settings_sections( self::PAGE_SLUG );
        submit_button();
        ?>
      </form>
    </div>
    <?php
  }

  public static function render_text_field( array $args ): void {
    $options = self::get();
    $value = $options[ $args['label_for'] ] ?? '';
    $type = $args['type'] ?? 'text';
    ?>
    <input
      type="<?php echo esc_attr( $type ); ?>"
      id="<?php echo esc_attr( $args['label_for'] ); ?>"
      name="<?php echo esc_attr( self::OPTION_NAME . '[' . $args['label_for'] . ']' ); ?>"
      value="<?php echo esc_attr( $value ); ?>"
      class="regular-text"
    />
    <?php
  }

  public static function render_checkbox( array $args ): void {
    $options = self::get();
    $checked = ! empty( $options[ $args['label_for'] ] );
    ?>
    <input
      type="checkbox"
      id="<?php echo esc_attr( $args['label_for'] ); ?>"
      name="<?php echo esc_attr( self::OPTION_NAME . '[' . $args['label_for'] . ']' ); ?>"
      value="1"
      <?php checked( $checked ); ?>
    />
    <?php
  }
}
```

## Hooks (actions et filtres)

```php
// Ajouter une action personnalisée
do_action( 'schoolswp_after_save', $data, $user_id );

// Ajouter un filtre personnalisé
$content = apply_filters( 'schoolswp_content', $content, $context );

// Documenter les hooks dans le code
/**
 * Fires after data is saved.
 *
 * @since 1.0.0
 *
 * @param array $data    The saved data.
 * @param int   $user_id The user ID.
 */
do_action( 'schoolswp_after_save', $data, $user_id );
```

## Cron / Tâches planifiées

```php
// Enregistrer l'intervalle personnalisé
add_filter( 'cron_schedules', function( array $schedules ): array {
  $schedules['schoolswp_hourly'] = [
    'interval' => HOUR_IN_SECONDS,
    'display'  => __( 'Toutes les heures', 'schoolswp-plugin' ),
  ];
  return $schedules;
} );

// Planifier la tâche (à l'activation)
if ( ! wp_next_scheduled( 'schoolswp_hourly_task' ) ) {
  wp_schedule_event( time(), 'schoolswp_hourly', 'schoolswp_hourly_task' );
}

// Handler
add_action( 'schoolswp_hourly_task', function(): void {
  // Exécuter la tâche
} );

// Nettoyer à la désactivation
wp_clear_scheduled_hook( 'schoolswp_hourly_task' );
```

## Checklist de vérification

- [ ] Header plugin complet et valide
- [ ] Namespace PSR-4 avec autoloading
- [ ] Protection accès direct (`if ( ! defined( 'ABSPATH' ) ) exit;`)
- [ ] Activation/désactivation/désinstallation propres
- [ ] Options avec valeurs par défaut et sanitization
- [ ] Capabilities vérifiées avant actions sensibles
- [ ] Textes internationalisés
- [ ] Coding standards WPCS respectés
- [ ] Pas de code dans le namespace global
- [ ] Préfixe unique pour éviter les collisions

## Ressources

- [Plugin Handbook](https://developer.wordpress.org/plugins/)
- [Plugin Security](https://developer.wordpress.org/plugins/security/)
- [Settings API](https://developer.wordpress.org/plugins/settings/settings-api/)
