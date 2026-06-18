---
source_url: https://developer.surecart.com/documentation/actions-filters/seo
source: surecart-developer-docs
scraped: true
---

[Skip to main content](https://developer.surecart.com/documentation/actions-filters/seo#content-area)

> ## Documentation Index
>
> Fetch the complete documentation index at: [https://developer.surecart.com/llms.txt](https://developer.surecart.com/llms.txt)
>
> Use this file to discover all available pages before exploring further.

These filters allow you to customize SEO-related behavior in SureCart, including meta tags, Open Graph data, and structured data (JSON-LD schema).

## [​](https://developer.surecart.com/documentation/actions-filters/seo#meta-tags) Meta Tags

### `surecart/noindex_query_vars`

Filter the query variables that trigger a `noindex` meta tag on product pages.

```
add_filter( 'surecart/noindex_query_vars', function( $vars ) {
    $vars[] = 'ref';
    $vars[] = 'affiliate_id';
    $vars[] = 'utm_source';
    $vars[] = 'utm_medium';
    return $vars;
} );
```

### `sc_display_product_seo_meta`

Control whether SureCart outputs its built-in SEO meta tags for product pages. Return `false` when using a dedicated SEO plugin.

Parameters: `$display` (bool), `$product` (`\SureCart\Models\Product`).

```
// Disable for Yoast SEO
add_filter( 'sc_display_product_seo_meta', function( $display, $product ) {
    if ( defined( 'WPSEO_VERSION' ) ) {
        return false;
    }
    return $display;
}, 10, 2 );

// Disable for Rank Math
add_filter( 'sc_display_product_seo_meta', function( $display, $product ) {
    if ( class_exists( 'RankMath' ) ) {
        return false;
    }
    return $display;
}, 10, 2 );

// Disable entirely
add_filter( 'sc_display_product_seo_meta', '__return_false' );
```

### `surecart/og:image/size`

Filter the WordPress image size used for Open Graph and Twitter Card tags. Default: `'full'`.

```
add_filter( 'surecart/og:image/size', function( $size ) {
    return 'large';
} );
```

## [​](https://developer.surecart.com/documentation/actions-filters/seo#product-schema) Product Schema

### `sc_display_product_json_ld_schema`

Control whether JSON-LD schema markup is output for products. Disable when using a third-party SEO plugin that generates product schema.

```
add_filter( 'sc_display_product_json_ld_schema', '__return_false' );
```

## [​](https://developer.surecart.com/documentation/actions-filters/seo#yoast-seo-integration) Yoast SEO Integration

### `sc_wpseo_frontend_presenters`

Filter the Yoast SEO presenters that SureCart uses on product pages.

```
add_filter( 'sc_wpseo_frontend_presenters', function( $title_presenters, $presenters ) {
    // Use all available Yoast presenters
    return $presenters;
}, 10, 2 );
```
