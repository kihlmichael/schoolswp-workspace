---
source_url: https://developer.surecart.com/documentation/actions-filters/products
source: surecart-developer-docs
scraped: true
---

[Skip to main content](https://developer.surecart.com/documentation/actions-filters/products#content-area)

> ## Documentation Index
>
> Fetch the complete documentation index at: [https://developer.surecart.com/llms.txt](https://developer.surecart.com/llms.txt)
>
> Use this file to discover all available pages before exploring further.

These hooks allow you to respond to product events and customize how products are displayed.

## [​](https://developer.surecart.com/documentation/actions-filters/products#actions) Actions

### `surecart/product_created`

```
add_action( 'surecart/product_created', function( $product, $data ) {
    wp_remote_post( SLACK_WEBHOOK_URL, [
        'body' => json_encode([ 'text' => sprintf( '🆕 New product created: %s', $product->name ) ]),
    ]);
}, 10, 2 );
```

### `surecart/product_updated`

```
add_action( 'surecart/product_updated', function( $product, $data ) {
    // Sync updated product info to external system
}, 10, 2 );
```

### `surecart/product_deleted`

```
add_action( 'surecart/product_deleted', function( $product, $data ) {
    wp_remote_request( 'https://api.crm.example.com/products/' . $product->id, [
        'method'  => 'DELETE',
        'headers' => [ 'Authorization' => 'Bearer ' . CRM_API_KEY ],
    ]);
}, 10, 2 );
```

### `surecart/product_stock_adjusted`

Fires when a product's stock level changes.

| Property          | Description                                         |
| ----------------- | --------------------------------------------------- |
| `stock`           | Total on-hand inventory count                       |
| `held_stock`      | Units purchased but not yet fulfilled/shipped       |
| `available_stock` | Units available for purchase (`stock - held_stock`) |

```
add_action( 'surecart/product_stock_adjusted', function( $product, $data ) {
    if ( $product->available_stock <= 5 && $product->available_stock > 0 ) {
        wp_remote_post( SLACK_WEBHOOK_URL, [
            'body' => json_encode([
                'text' => sprintf(
                    '⚠️ Low stock: %s has %d available (%d on hand, %d held)',
                    $product->name, $product->available_stock, $product->stock, $product->held_stock
                )
            ]),
        ]);
    }
}, 10, 2 );
```

## [​](https://developer.surecart.com/documentation/actions-filters/products#filters) Filters

### `surecart/product/replace_content_with_product_info_part`

```
add_filter( 'surecart/product/replace_content_with_product_info_part', '__return_false' );
```

### `sc_product_post_type_link_sc_collection`

Control which collection slug appears in product URLs when the permalink includes `%sc_collection%`.

```
add_filter( 'sc_product_post_type_link_sc_collection', function( $term, $terms, $post ) {
    // Use the first collection assigned to the product
    return $terms[0] ?? $term;
}, 10, 3 );
```

### `surecart/product-line-item-image/fallback_src`

```
add_filter( 'surecart/product-line-item-image/fallback_src', function( $src, $product ) {
    return get_template_directory_uri() . '/images/placeholder.png';
}, 10, 2 );
```

### `surecart_product_page_query_args`

```
add_filter( 'surecart_product_page_query_args', function( $args ) {
    if ( current_user_can( 'manage_options' ) ) {
        $args['post_status'] = [ 'publish', 'draft', 'private' ];
    }
    return $args;
} );
```
