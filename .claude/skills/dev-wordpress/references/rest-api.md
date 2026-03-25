# REST API — schoolsWP Dev Skills

Guide pour créer des endpoints REST API WordPress personnalisés.

## Structure des routes

```php
<?php

declare( strict_types=1 );

namespace SchoolsWP\Plugin\REST;

use WP_REST_Controller;
use WP_REST_Request;
use WP_REST_Response;
use WP_REST_Server;
use WP_Error;

class ItemsController extends WP_REST_Controller {
  protected $namespace = 'schoolswp/v1';
  protected $rest_base = 'items';

  public function register_routes(): void {
    // GET /wp-json/schoolswp/v1/items
    register_rest_route(
      $this->namespace,
      '/' . $this->rest_base,
      [
        [
          'methods'             => WP_REST_Server::READABLE,
          'callback'            => [ $this, 'get_items' ],
          'permission_callback' => [ $this, 'get_items_permissions_check' ],
          'args'                => $this->get_collection_params(),
        ],
        [
          'methods'             => WP_REST_Server::CREATABLE,
          'callback'            => [ $this, 'create_item' ],
          'permission_callback' => [ $this, 'create_item_permissions_check' ],
          'args'                => $this->get_endpoint_args_for_item_schema( WP_REST_Server::CREATABLE ),
        ],
        'schema' => [ $this, 'get_public_item_schema' ],
      ]
    );

    // GET/PUT/DELETE /wp-json/schoolswp/v1/items/{id}
    register_rest_route(
      $this->namespace,
      '/' . $this->rest_base . '/(?P<id>[\d]+)',
      [
        [
          'methods'             => WP_REST_Server::READABLE,
          'callback'            => [ $this, 'get_item' ],
          'permission_callback' => [ $this, 'get_item_permissions_check' ],
          'args'                => [
            'id' => [
              'description' => __( 'Unique identifier for the item.', 'schoolswp' ),
              'type'        => 'integer',
              'required'    => true,
            ],
          ],
        ],
        [
          'methods'             => WP_REST_Server::EDITABLE,
          'callback'            => [ $this, 'update_item' ],
          'permission_callback' => [ $this, 'update_item_permissions_check' ],
          'args'                => $this->get_endpoint_args_for_item_schema( WP_REST_Server::EDITABLE ),
        ],
        [
          'methods'             => WP_REST_Server::DELETABLE,
          'callback'            => [ $this, 'delete_item' ],
          'permission_callback' => [ $this, 'delete_item_permissions_check' ],
        ],
        'schema' => [ $this, 'get_public_item_schema' ],
      ]
    );
  }
}
```

## Permission callbacks

```php
/**
 * Permissions pour GET collection.
 */
public function get_items_permissions_check( WP_REST_Request $request ): bool|WP_Error {
  // Public = toujours true
  return true;

  // Authentifié uniquement
  return is_user_logged_in();

  // Capability spécifique
  return current_user_can( 'read' );
}

/**
 * Permissions pour POST.
 */
public function create_item_permissions_check( WP_REST_Request $request ): bool|WP_Error {
  if ( ! current_user_can( 'publish_posts' ) ) {
    return new WP_Error(
      'rest_forbidden',
      __( 'Vous n\'avez pas les permissions pour créer des items.', 'schoolswp' ),
      [ 'status' => rest_authorization_required_code() ]
    );
  }
  return true;
}

/**
 * Permissions pour PUT/PATCH.
 */
public function update_item_permissions_check( WP_REST_Request $request ): bool|WP_Error {
  $item = $this->get_item_from_db( $request->get_param( 'id' ) );

  if ( is_wp_error( $item ) ) {
    return $item;
  }

  // Vérifier propriété ou admin
  if ( (int) $item->user_id !== get_current_user_id() && ! current_user_can( 'manage_options' ) ) {
    return new WP_Error(
      'rest_forbidden',
      __( 'Vous ne pouvez modifier que vos propres items.', 'schoolswp' ),
      [ 'status' => 403 ]
    );
  }

  return true;
}

/**
 * Permissions pour DELETE.
 */
public function delete_item_permissions_check( WP_REST_Request $request ): bool|WP_Error {
  return $this->update_item_permissions_check( $request );
}
```

## Callbacks CRUD

```php
/**
 * GET collection.
 */
public function get_items( WP_REST_Request $request ): WP_REST_Response|WP_Error {
  $per_page = $request->get_param( 'per_page' );
  $page     = $request->get_param( 'page' );
  $search   = $request->get_param( 'search' );

  global $wpdb;

  $where = '1=1';
  $args  = [];

  if ( $search ) {
    $where .= ' AND title LIKE %s';
    $args[] = '%' . $wpdb->esc_like( $search ) . '%';
  }

  $total = (int) $wpdb->get_var(
    $wpdb->prepare(
      "SELECT COUNT(*) FROM {$wpdb->prefix}schoolswp_items WHERE $where",
      ...$args
    )
  );

  $items = $wpdb->get_results(
    $wpdb->prepare(
      "SELECT * FROM {$wpdb->prefix}schoolswp_items
       WHERE $where
       ORDER BY created_at DESC
       LIMIT %d OFFSET %d",
      array_merge( $args, [ $per_page, ( $page - 1 ) * $per_page ] )
    )
  );

  $data = [];
  foreach ( $items as $item ) {
    $data[] = $this->prepare_item_for_response( $item, $request )->get_data();
  }

  $response = rest_ensure_response( $data );

  // Headers de pagination
  $response->header( 'X-WP-Total', $total );
  $response->header( 'X-WP-TotalPages', (int) ceil( $total / $per_page ) );

  return $response;
}

/**
 * GET single item.
 */
public function get_item( WP_REST_Request $request ): WP_REST_Response|WP_Error {
  $item = $this->get_item_from_db( $request->get_param( 'id' ) );

  if ( is_wp_error( $item ) ) {
    return $item;
  }

  return $this->prepare_item_for_response( $item, $request );
}

/**
 * POST create item.
 */
public function create_item( WP_REST_Request $request ): WP_REST_Response|WP_Error {
  global $wpdb;

  $prepared = $this->prepare_item_for_database( $request );

  if ( is_wp_error( $prepared ) ) {
    return $prepared;
  }

  $result = $wpdb->insert(
    $wpdb->prefix . 'schoolswp_items',
    $prepared,
    [ '%s', '%d', '%s' ]
  );

  if ( false === $result ) {
    return new WP_Error(
      'rest_cannot_create',
      __( 'Impossible de créer l\'item.', 'schoolswp' ),
      [ 'status' => 500 ]
    );
  }

  $item = $this->get_item_from_db( $wpdb->insert_id );

  $response = $this->prepare_item_for_response( $item, $request );
  $response->set_status( 201 );
  $response->header(
    'Location',
    rest_url( sprintf( '%s/%s/%d', $this->namespace, $this->rest_base, $item->id ) )
  );

  return $response;
}

/**
 * PUT/PATCH update item.
 */
public function update_item( WP_REST_Request $request ): WP_REST_Response|WP_Error {
  global $wpdb;

  $id   = $request->get_param( 'id' );
  $item = $this->get_item_from_db( $id );

  if ( is_wp_error( $item ) ) {
    return $item;
  }

  $prepared = $this->prepare_item_for_database( $request );

  if ( is_wp_error( $prepared ) ) {
    return $prepared;
  }

  $wpdb->update(
    $wpdb->prefix . 'schoolswp_items',
    $prepared,
    [ 'id' => $id ],
    [ '%s' ],
    [ '%d' ]
  );

  $item = $this->get_item_from_db( $id );

  return $this->prepare_item_for_response( $item, $request );
}

/**
 * DELETE item.
 */
public function delete_item( WP_REST_Request $request ): WP_REST_Response|WP_Error {
  global $wpdb;

  $id   = $request->get_param( 'id' );
  $item = $this->get_item_from_db( $id );

  if ( is_wp_error( $item ) ) {
    return $item;
  }

  $response = $this->prepare_item_for_response( $item, $request );

  $wpdb->delete(
    $wpdb->prefix . 'schoolswp_items',
    [ 'id' => $id ],
    [ '%d' ]
  );

  return $response;
}
```

## Préparation des données

```php
/**
 * Préparer un item pour la réponse.
 */
public function prepare_item_for_response( $item, WP_REST_Request $request ): WP_REST_Response {
  $data = [
    'id'         => (int) $item->id,
    'title'      => $item->title,
    'user_id'    => (int) $item->user_id,
    'created_at' => mysql_to_rfc3339( $item->created_at ),
    '_links'     => [
      'self' => [
        [
          'href' => rest_url( sprintf( '%s/%s/%d', $this->namespace, $this->rest_base, $item->id ) ),
        ],
      ],
      'collection' => [
        [
          'href' => rest_url( sprintf( '%s/%s', $this->namespace, $this->rest_base ) ),
        ],
      ],
      'author' => [
        [
          'href'       => rest_url( 'wp/v2/users/' . $item->user_id ),
          'embeddable' => true,
        ],
      ],
    ],
  ];

  $response = rest_ensure_response( $data );

  return $response;
}

/**
 * Préparer un item pour la base de données.
 */
protected function prepare_item_for_database( WP_REST_Request $request ): array|WP_Error {
  $prepared = [];

  if ( $request->has_param( 'title' ) ) {
    $prepared['title'] = sanitize_text_field( $request->get_param( 'title' ) );
  }

  $prepared['user_id'] = get_current_user_id();

  return $prepared;
}
```

## Schema

```php
/**
 * Schema de l'item.
 */
public function get_item_schema(): array {
  if ( $this->schema ) {
    return $this->schema;
  }

  $this->schema = [
    '$schema'    => 'http://json-schema.org/draft-04/schema#',
    'title'      => 'schoolswp_item',
    'type'       => 'object',
    'properties' => [
      'id' => [
        'description' => __( 'Identifiant unique de l\'item.', 'schoolswp' ),
        'type'        => 'integer',
        'context'     => [ 'view', 'edit' ],
        'readonly'    => true,
      ],
      'title' => [
        'description' => __( 'Titre de l\'item.', 'schoolswp' ),
        'type'        => 'string',
        'context'     => [ 'view', 'edit' ],
        'required'    => true,
        'minLength'   => 1,
        'maxLength'   => 255,
      ],
      'user_id' => [
        'description' => __( 'ID de l\'auteur.', 'schoolswp' ),
        'type'        => 'integer',
        'context'     => [ 'view', 'edit' ],
        'readonly'    => true,
      ],
      'created_at' => [
        'description' => __( 'Date de création (RFC3339).', 'schoolswp' ),
        'type'        => 'string',
        'format'      => 'date-time',
        'context'     => [ 'view' ],
        'readonly'    => true,
      ],
    ],
  ];

  return $this->schema;
}

/**
 * Paramètres de collection.
 */
public function get_collection_params(): array {
  return [
    'page' => [
      'description'       => __( 'Page courante de la collection.', 'schoolswp' ),
      'type'              => 'integer',
      'default'           => 1,
      'minimum'           => 1,
      'sanitize_callback' => 'absint',
    ],
    'per_page' => [
      'description'       => __( 'Nombre d\'items par page.', 'schoolswp' ),
      'type'              => 'integer',
      'default'           => 10,
      'minimum'           => 1,
      'maximum'           => 100,
      'sanitize_callback' => 'absint',
    ],
    'search' => [
      'description'       => __( 'Recherche textuelle.', 'schoolswp' ),
      'type'              => 'string',
      'sanitize_callback' => 'sanitize_text_field',
    ],
  ];
}
```

## Enregistrement

```php
// Dans le plugin principal
add_action( 'rest_api_init', function(): void {
  $controller = new REST\ItemsController();
  $controller->register_routes();
} );
```

## Authentification

### Application Passwords (recommandé)

```bash
# Créer un mot de passe application dans Profil > Mots de passe d'application
curl -u "username:xxxx xxxx xxxx xxxx" \
  https://example.com/wp-json/schoolswp/v1/items
```

### Cookie (pour le frontend)

```php
// Nonce automatiquement inclus par wp_localize_script
wp_localize_script( 'my-script', 'myData', [
  'nonce'   => wp_create_nonce( 'wp_rest' ),
  'restUrl' => rest_url( 'schoolswp/v1/' ),
] );
```

```javascript
// JavaScript
fetch(myData.restUrl + 'items', {
  headers: {
    'X-WP-Nonce': myData.nonce,
    'Content-Type': 'application/json',
  },
  method: 'POST',
  body: JSON.stringify({ title: 'New Item' }),
});
```

## Checklist de vérification

- [ ] Namespace versionné (`schoolswp/v1`)
- [ ] `permission_callback` sur CHAQUE route (jamais `__return_true` en production)
- [ ] Schema défini avec types et validation
- [ ] Inputs sanitisés (`sanitize_text_field`, `absint`, etc.)
- [ ] Prepared statements pour requêtes SQL
- [ ] Headers de pagination (X-WP-Total, X-WP-TotalPages)
- [ ] Codes HTTP corrects (201 pour création, 404 pour non trouvé)
- [ ] Réponses WP_REST_Response ou WP_Error

## Ressources

- [REST API Handbook](https://developer.wordpress.org/rest-api/)
- [Extending the REST API](https://developer.wordpress.org/rest-api/extending-the-rest-api/)
- [Adding Custom Endpoints](https://developer.wordpress.org/rest-api/extending-the-rest-api/adding-custom-endpoints/)
