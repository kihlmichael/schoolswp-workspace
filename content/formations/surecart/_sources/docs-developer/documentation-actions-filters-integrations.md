---
source_url: https://developer.surecart.com/documentation/actions-filters/integrations
source: surecart-developer-docs
scraped: true
---

[Skip to main content](https://developer.surecart.com/documentation/actions-filters/integrations#content-area)

> ## Documentation Index
>
> Fetch the complete documentation index at: [https://developer.surecart.com/llms.txt](https://developer.surecart.com/llms.txt)
>
> Use this file to discover all available pages before exploring further.

**These are low-level actions for integration configuration changes.**

If you are wanting to create a full purchase integration that handles granting access, refunds, upgrades, downgrades and more, please follow the [Purchase Integration Guide](https://developer.surecart.com/documentation/orders-and-purchases).

These actions fire when a merchant configures or removes product integrations in the SureCart admin. Product integrations are the automated actions that occur when a product is purchased—such as changing a user's WordPress role, enrolling them in a course, or adding them to a membership group.

## [​](https://developer.surecart.com/documentation/actions-filters/integrations#surecart/integrations/create) `surecart/integrations/create`

Fired when a merchant **adds** an integration to a product.

Parameters: `$params` (array) — The integration parameters including provider, model, and configuration.

```
add_action( 'surecart/integrations/create', function( $params ) {
    error_log( 'Integration created: ' . print_r( $params, true ) );

    if ( ! empty( $params['provider'] ) ) {
        wp_mail(
            get_option( 'admin_email' ),
            'New Product Integration Added',
            sprintf( 'A %s integration was added to a product.', $params['provider'] )
        );
    }
} );
```

## [​](https://developer.surecart.com/documentation/actions-filters/integrations#surecart/integrations/delete) `surecart/integrations/delete`

Fired when a merchant **removes** an integration from a product.

```
add_action( 'surecart/integrations/delete', function( $params ) {
    error_log( 'Integration deleted: ' . print_r( $params, true ) );
} );
```
