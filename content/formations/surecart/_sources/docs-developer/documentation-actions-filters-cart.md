---
source_url: https://developer.surecart.com/documentation/actions-filters/cart
source: surecart-developer-docs
scraped: true
---

[Skip to main content](https://developer.surecart.com/documentation/actions-filters/cart#content-area)

> ## Documentation Index
>
> Fetch the complete documentation index at: [https://developer.surecart.com/llms.txt](https://developer.surecart.com/llms.txt)
>
> Use this file to discover all available pages before exploring further.

These filters allow you to customize the cart experience.

## [​](https://developer.surecart.com/documentation/actions-filters/cart#sc_cart_menu_icon) `sc_cart_menu_icon`

Filter the cart menu icon.

Parameters: `$icon` (string) — The icon name/identifier. `$type` (string) — The icon type or position context.

```
add_filter( 'sc_cart_menu_icon', function( $icon, $type ) {
    return 'shopping-bag'; // Use a different icon
}, 10, 2 );
```

## [​](https://developer.surecart.com/documentation/actions-filters/cart#sc_cart_disabled) `sc_cart_disabled`

Disable the cart functionality entirely on specific pages or conditions.

```
add_filter( 'sc_cart_disabled', function( $disabled ) {
    // Disable cart on specific pages
    if ( is_page( 'landing-page' ) ) {
        return true;
    }
    return $disabled;
} );

// Or disable during maintenance
add_filter( 'sc_cart_disabled', function( $disabled ) {
    if ( get_option( 'maintenance_mode' ) ) {
        return true;
    }
    return $disabled;
} );
```

## [​](https://developer.surecart.com/documentation/actions-filters/cart#use-cases) Use Cases

### [​](https://developer.surecart.com/documentation/actions-filters/cart#hide-cart-on-landing-pages) Hide Cart on Landing Pages

```
add_filter( 'sc_cart_disabled', function( $disabled ) {
    // Hide cart on specific landing pages
    $landing_pages = [ 'promo', 'special-offer', 'webinar' ];

    foreach ( $landing_pages as $slug ) {
        if ( is_page( $slug ) ) {
            return true;
        }
    }

    return $disabled;
} );
```

### [​](https://developer.surecart.com/documentation/actions-filters/cart#disable-cart-for-logged-out-users) Disable Cart for Logged-Out Users

```
add_filter( 'sc_cart_disabled', function( $disabled ) {
    // Only show cart to logged-in users
    return ! is_user_logged_in();
} );
```
