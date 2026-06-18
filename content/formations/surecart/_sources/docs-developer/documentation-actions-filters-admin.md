---
source_url: https://developer.surecart.com/documentation/actions-filters/admin
source: surecart-developer-docs
scraped: true
---

[Skip to main content](https://developer.surecart.com/documentation/actions-filters/admin#content-area)

> ## Documentation Index
>
> Fetch the complete documentation index at: [https://developer.surecart.com/llms.txt](https://developer.surecart.com/llms.txt)
>
> Use this file to discover all available pages before exploring further.

These filters allow you to customize the WordPress admin experience for SureCart.

## [​](https://developer.surecart.com/documentation/actions-filters/admin#menu-filters) Menu Filters

### [​](https://developer.surecart.com/documentation/actions-filters/admin#surecart_menu_priority) `surecart_menu_priority`

Filter the admin menu position. Lower numbers appear higher in the menu.

```
add_filter( 'surecart_menu_priority', function( $priority ) {
    return 5; // Move menu higher (closer to Dashboard)
} );

// Or move it lower
add_filter( 'surecart_menu_priority', function( $priority ) {
    return 80; // Move below Settings
} );
```

## [​](https://developer.surecart.com/documentation/actions-filters/admin#admin-bar-filters) Admin Bar Filters

### [​](https://developer.surecart.com/documentation/actions-filters/admin#surecart_show_admin_bar_visit_store) `surecart_show_admin_bar_visit_store`

Control whether "Visit Store" appears in the admin bar.

```
add_filter( 'surecart_show_admin_bar_visit_store', '__return_false' );

// Or show only for specific roles
add_filter( 'surecart_show_admin_bar_visit_store', function( $show ) {
    return current_user_can( 'manage_options' );
} );
```

### [​](https://developer.surecart.com/documentation/actions-filters/admin#surecart_show_admin_bar_new_content) `surecart_show_admin_bar_new_content`

Control whether "New" content menu appears in admin bar.

```
add_filter( 'surecart_show_admin_bar_new_content', '__return_false' );
```

### [​](https://developer.surecart.com/documentation/actions-filters/admin#surecart/help_widget/show) `surecart/help_widget/show`

Control when the help widget is shown.

```
add_filter( 'surecart/help_widget/show', function( $show ) {
    // Hide for non-admins
    return current_user_can( 'manage_options' );
} );

// Or always hide
add_filter( 'surecart/help_widget/show', '__return_false' );
```

### [​](https://developer.surecart.com/documentation/actions-filters/admin#surecart/help_widget/loaded) `surecart/help_widget/loaded`

Fired when the help widget is loaded in the admin. Use this to inject custom scripts or modify widget behavior.

```
add_action( 'surecart/help_widget/loaded', function() {
    // Add custom help resources or modify widget behavior
    ?>
    <script>
        // Customize help widget
    </script>
    <?php
} );
```

## [​](https://developer.surecart.com/documentation/actions-filters/admin#sync-filters) Sync Filters

### [​](https://developer.surecart.com/documentation/actions-filters/admin#surecart_get_post_type_post) `surecart_get_{post_type}_post`

Filter the synced post lookup result. Replace `{post_type}` with the actual post type (e.g., `sc_product`).

```
add_filter( 'surecart_get_sc_product_post', function( $post, $model_id, $service ) {
    // Custom post lookup logic
    return $post;
}, 10, 3 );
```

### [​](https://developer.surecart.com/documentation/actions-filters/admin#surecart_excluded_post_meta_keys) `surecart_excluded_post_meta_keys`

Filter meta keys excluded from sync.

```
add_filter( 'surecart_excluded_post_meta_keys', function( $keys ) {
    $keys[] = 'my_excluded_key';
    $keys[] = '_custom_meta';
    return $keys;
} );
```

## [​](https://developer.surecart.com/documentation/actions-filters/admin#use-cases) Use Cases

### [​](https://developer.surecart.com/documentation/actions-filters/admin#hide-admin-features-for-shop-managers) Hide Admin Features for Shop Managers

```
// Hide help widget for non-admins
add_filter( 'surecart/help_widget/show', function( $show ) {
    return current_user_can( 'manage_options' );
} );

// Hide admin bar links for shop managers
add_filter( 'surecart_show_admin_bar_new_content', function( $show ) {
    return current_user_can( 'manage_options' );
} );
```

### [​](https://developer.surecart.com/documentation/actions-filters/admin#simplify-admin-interface) Simplify Admin Interface

```
// Hide all dropdowns for a cleaner interface
add_filter( 'surecart/disable_product_collection_dropdown', '__return_true' );
add_filter( 'surecart/disable_fulfillment_dropdown', '__return_true' );
add_filter( 'surecart/disable_shipment_dropdown', '__return_true' );
```

### [​](https://developer.surecart.com/documentation/actions-filters/admin#customize-menu-position) Customize Menu Position

```
// Move SureCart menu right after Dashboard
add_filter( 'surecart_menu_priority', function( $priority ) {
    return 3;
} );
```

## [​](https://developer.surecart.com/documentation/actions-filters/admin#related) Related

## Templates

Hook into admin and template actions.

## Requests

Modify API requests and responses.
