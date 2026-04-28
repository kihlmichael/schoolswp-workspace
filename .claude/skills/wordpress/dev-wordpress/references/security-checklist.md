# Security Checklist — schoolsWP Dev Skills

Checklist de sécurité pour le développement WordPress.

## Principes fondamentaux

1. **Ne jamais faire confiance aux données** — Toute donnée externe est potentiellement malveillante
2. **Échapper en sortie** — Toujours échapper au dernier moment, selon le contexte
3. **Valider et nettoyer en entrée** — Sanitiser avant stockage
4. **Principe du moindre privilège** — N'accorder que les permissions nécessaires

## Échappement (output escaping)

### Fonctions d'échappement

| Contexte | Fonction | Exemple |
|----------|----------|---------|
| HTML | `esc_html()` | `<p><?php echo esc_html( $text ); ?></p>` |
| Attribut HTML | `esc_attr()` | `<input value="<?php echo esc_attr( $value ); ?>">` |
| URL | `esc_url()` | `<a href="<?php echo esc_url( $url ); ?>">` |
| JavaScript | `esc_js()` | `onclick="alert('<?php echo esc_js( $msg ); ?>');"` |
| Textarea | `esc_textarea()` | `<textarea><?php echo esc_textarea( $content ); ?></textarea>` |
| HTML avec balises | `wp_kses()` | Voir ci-dessous |
| Traductions | `esc_html__()` | `<?php echo esc_html__( 'Text', 'domain' ); ?>` |

### wp_kses pour HTML contrôlé

```php
$allowed_html = [
  'a' => [
    'href'   => [],
    'title'  => [],
    'target' => [],
  ],
  'br'     => [],
  'em'     => [],
  'strong' => [],
  'p'      => [
    'class' => [],
  ],
];

echo wp_kses( $user_html, $allowed_html );

// Ou utiliser les presets
echo wp_kses_post( $content );   // HTML autorisé dans les posts
echo wp_kses_data( $data );      // Très restrictif
```

### Échappement avec traduction

```php
// Correct
echo esc_html__( 'Hello World', 'textdomain' );
esc_html_e( 'Hello World', 'textdomain' );

// Avec placeholder
printf(
  /* translators: %s: username */
  esc_html__( 'Hello %s', 'textdomain' ),
  esc_html( $username )
);

// HTML dans traduction
printf(
  /* translators: %s: link to settings */
  wp_kses(
    __( 'Go to <a href="%s">settings</a>', 'textdomain' ),
    [ 'a' => [ 'href' => [] ] ]
  ),
  esc_url( admin_url( 'options-general.php' ) )
);
```

## Sanitisation (input sanitization)

### Fonctions de sanitisation

| Type | Fonction | Description |
|------|----------|-------------|
| Texte simple | `sanitize_text_field()` | Supprime tags, encode caractères |
| Textarea | `sanitize_textarea_field()` | Préserve les retours à la ligne |
| Email | `sanitize_email()` | Valide et nettoie email |
| Nom de fichier | `sanitize_file_name()` | Supprime caractères interdits |
| Slug | `sanitize_title()` | Pour URLs et identifiants |
| Clé | `sanitize_key()` | Lowercase, alphanumérique, tirets |
| HTML | `wp_kses()` | Filtre HTML selon whitelist |
| URL | `esc_url_raw()` | Pour stockage (pas affichage) |
| Entier | `absint()` ou `intval()` | Conversion en entier |

### Exemples d'utilisation

```php
// Formulaire POST
$title = isset( $_POST['title'] )
  ? sanitize_text_field( wp_unslash( $_POST['title'] ) )
  : '';

$content = isset( $_POST['content'] )
  ? sanitize_textarea_field( wp_unslash( $_POST['content'] ) )
  : '';

$email = isset( $_POST['email'] )
  ? sanitize_email( wp_unslash( $_POST['email'] ) )
  : '';

$count = isset( $_POST['count'] )
  ? absint( $_POST['count'] )
  : 0;

// Validation combinée
if ( ! is_email( $email ) ) {
  return new WP_Error( 'invalid_email', 'Email invalide.' );
}
```

## Nonces (CSRF protection)

### Formulaires

```php
// Création du formulaire
<form method="post" action="">
  <?php wp_nonce_field( 'schoolswp_save_action', 'schoolswp_nonce' ); ?>
  <input type="text" name="data" />
  <button type="submit">Enregistrer</button>
</form>

// Vérification
function process_form(): void {
  if ( ! isset( $_POST['schoolswp_nonce'] ) ) {
    return;
  }

  if ( ! wp_verify_nonce( $_POST['schoolswp_nonce'], 'schoolswp_save_action' ) ) {
    wp_die( 'Nonce verification failed' );
  }

  // Traitement sécurisé...
}
```

### URLs d'action

```php
// Création de l'URL
$delete_url = wp_nonce_url(
  admin_url( 'admin-post.php?action=schoolswp_delete&id=' . $item_id ),
  'schoolswp_delete_' . $item_id
);

// Vérification
add_action( 'admin_post_schoolswp_delete', function(): void {
  $id = isset( $_GET['id'] ) ? absint( $_GET['id'] ) : 0;

  if ( ! wp_verify_nonce( $_GET['_wpnonce'] ?? '', 'schoolswp_delete_' . $id ) ) {
    wp_die( 'Nonce verification failed' );
  }

  // Suppression sécurisée...
} );
```

### AJAX

```php
// JavaScript
jQuery.post( ajaxurl, {
  action: 'schoolswp_ajax_action',
  nonce: schoolswpData.nonce, // wp_create_nonce( 'schoolswp_ajax' )
  data: myData
} );

// PHP handler
add_action( 'wp_ajax_schoolswp_ajax_action', function(): void {
  check_ajax_referer( 'schoolswp_ajax', 'nonce' );

  // Traitement...

  wp_send_json_success( $data );
} );
```

## Capabilities (autorisations)

### Vérification basique

```php
// Avant toute action admin
if ( ! current_user_can( 'manage_options' ) ) {
  wp_die( __( 'Accès non autorisé.', 'schoolswp' ) );
}

// Pour un post spécifique
if ( ! current_user_can( 'edit_post', $post_id ) ) {
  return new WP_Error( 'forbidden', 'Vous ne pouvez pas modifier ce post.' );
}
```

### Capabilities communes

| Capability | Description |
|------------|-------------|
| `read` | Accès au tableau de bord |
| `edit_posts` | Modifier ses propres posts |
| `publish_posts` | Publier des posts |
| `edit_others_posts` | Modifier posts d'autres auteurs |
| `manage_options` | Accès aux réglages (admin) |
| `upload_files` | Uploader des médias |
| `manage_categories` | Gérer les catégories |

### Custom capabilities

```php
// Enregistrer avec un CPT
register_post_type( 'schoolswp_item', [
  // ...
  'capability_type' => 'schoolswp_item',
  'map_meta_cap'    => true,
  'capabilities'    => [
    'edit_post'          => 'edit_schoolswp_item',
    'read_post'          => 'read_schoolswp_item',
    'delete_post'        => 'delete_schoolswp_item',
    'edit_posts'         => 'edit_schoolswp_items',
    'edit_others_posts'  => 'edit_others_schoolswp_items',
    'publish_posts'      => 'publish_schoolswp_items',
    'read_private_posts' => 'read_private_schoolswp_items',
  ],
] );

// Assigner à un rôle (activation du plugin)
$admin = get_role( 'administrator' );
$admin->add_cap( 'edit_schoolswp_items' );
$admin->add_cap( 'edit_others_schoolswp_items' );
// etc.
```

## Base de données (SQL injection)

### Prepared statements (OBLIGATOIRE)

```php
global $wpdb;

// ❌ JAMAIS
$wpdb->query( "SELECT * FROM {$wpdb->posts} WHERE post_title = '$title'" );

// ✅ TOUJOURS
$results = $wpdb->get_results(
  $wpdb->prepare(
    "SELECT * FROM {$wpdb->posts} WHERE post_title = %s AND post_status = %s",
    $title,
    'publish'
  )
);

// Placeholders
// %s = string
// %d = integer
// %f = float

// IN clause
$ids = [ 1, 2, 3 ];
$placeholders = implode( ', ', array_fill( 0, count( $ids ), '%d' ) );
$query = $wpdb->prepare(
  "SELECT * FROM {$wpdb->posts} WHERE ID IN ($placeholders)",
  ...$ids
);

// LIKE
$search = 'test';
$results = $wpdb->get_results(
  $wpdb->prepare(
    "SELECT * FROM {$wpdb->posts} WHERE post_title LIKE %s",
    '%' . $wpdb->esc_like( $search ) . '%'
  )
);
```

## File uploads

```php
function handle_upload(): int|WP_Error {
  if ( ! function_exists( 'wp_handle_upload' ) ) {
    require_once ABSPATH . 'wp-admin/includes/file.php';
  }

  // Vérifier le nonce
  check_admin_referer( 'schoolswp_upload' );

  // Vérifier les capabilities
  if ( ! current_user_can( 'upload_files' ) ) {
    return new WP_Error( 'forbidden', 'Upload non autorisé.' );
  }

  // Vérifier le fichier
  if ( empty( $_FILES['my_file'] ) ) {
    return new WP_Error( 'no_file', 'Aucun fichier.' );
  }

  // Types MIME autorisés
  $allowed_types = [
    'image/jpeg',
    'image/png',
    'image/gif',
    'application/pdf',
  ];

  $file_type = wp_check_filetype( $_FILES['my_file']['name'] );

  if ( ! in_array( $file_type['type'], $allowed_types, true ) ) {
    return new WP_Error( 'invalid_type', 'Type de fichier non autorisé.' );
  }

  // Taille max (5 Mo)
  if ( $_FILES['my_file']['size'] > 5 * MB_IN_BYTES ) {
    return new WP_Error( 'too_large', 'Fichier trop volumineux.' );
  }

  // Upload via WordPress
  $upload = wp_handle_upload(
    $_FILES['my_file'],
    [ 'test_form' => false ]
  );

  if ( isset( $upload['error'] ) ) {
    return new WP_Error( 'upload_error', $upload['error'] );
  }

  // Créer l'attachment
  $attachment_id = wp_insert_attachment(
    [
      'post_mime_type' => $upload['type'],
      'post_title'     => sanitize_file_name( $_FILES['my_file']['name'] ),
      'post_status'    => 'inherit',
    ],
    $upload['file']
  );

  // Générer les métadonnées
  require_once ABSPATH . 'wp-admin/includes/image.php';
  wp_update_attachment_metadata(
    $attachment_id,
    wp_generate_attachment_metadata( $attachment_id, $upload['file'] )
  );

  return $attachment_id;
}
```

## Headers de sécurité

```php
// Dans functions.php ou plugin
add_action( 'send_headers', function(): void {
  if ( ! is_admin() ) {
    header( 'X-Content-Type-Options: nosniff' );
    header( 'X-Frame-Options: SAMEORIGIN' );
    header( 'X-XSS-Protection: 1; mode=block' );
    header( 'Referrer-Policy: strict-origin-when-cross-origin' );
  }
} );
```

## Checklist finale

### Input

- [ ] Tous les `$_GET`, `$_POST`, `$_REQUEST` sanitisés
- [ ] `wp_unslash()` appliqué avant sanitisation
- [ ] Types validés (email, URL, entier, etc.)
- [ ] Nonces vérifiés pour toute action

### Output

- [ ] `esc_html()` pour texte dans HTML
- [ ] `esc_attr()` pour attributs
- [ ] `esc_url()` pour URLs
- [ ] `wp_kses()` pour HTML utilisateur

### Database

- [ ] 100% des requêtes utilisent `$wpdb->prepare()`
- [ ] `$wpdb->esc_like()` pour les LIKE
- [ ] Pas de concaténation directe de variables

### Authorization

- [ ] `current_user_can()` avant toute action
- [ ] Vérification de propriété pour les ressources
- [ ] Capabilities appropriées (pas toujours admin)

### Files

- [ ] Types MIME whitelist
- [ ] Taille limitée
- [ ] Upload via `wp_handle_upload()`
- [ ] Capabilities vérifiées

## Ressources

- [Plugin Security](https://developer.wordpress.org/plugins/security/)
- [Data Validation](https://developer.wordpress.org/plugins/security/data-validation/)
- [Nonces](https://developer.wordpress.org/plugins/security/nonces/)
- [OWASP WordPress Security](https://owasp.org/www-project-web-security-testing-guide/)
