---
source_url: https://developer.surecart.com/documentation/actions-filters/purchases
source: surecart-developer-docs
scraped: true
---

[Skip to main content](https://developer.surecart.com/documentation/actions-filters/purchases#content-area)

> ## Documentation Index
>
> Fetch the complete documentation index at: [https://developer.surecart.com/llms.txt](https://developer.surecart.com/llms.txt)
>
> Use this file to discover all available pages before exploring further.

**Important: These are low-level filters for purchase events.**

If you are wanting to create a full purchase integration that handles refunds, upgrades, downgrades and more, please follow the [Purchase Integration Guide](https://developer.surecart.com/documentation/orders-and-purchases)

These actions are triggered throughout the purchase lifecycle, including:

- **Checkout** — When a customer completes a purchase
- **Refunds** — When a purchase is refunded and access is revoked
- **Upgrades/Downgrades** — When a customer switches to a different product
- **Quantity changes** — When a customer adjusts the quantity of their purchase
- **Subscription cancellations** — When a subscription ends and access is revoked
- **Subscription restorations** — When a canceled subscription is reactivated

## [​](https://developer.surecart.com/documentation/actions-filters/purchases#surecart/purchase_created) `surecart/purchase_created`

Fired when a new purchase is created after a successful checkout.

Parameters: `$purchase` (`\SureCart\Models\Purchase`) — contains product, customer, quantity, and other purchase details.

```
add_action( 'surecart/purchase_created', function( $purchase ) {
    $product = sc_get_product( $purchase->product );
    $user = $purchase->getWPUser();

    if ( empty($user) || empty($product->name) ) {
        return;
    }

    wp_mail(
        $user->user_email,
        'Welcome!',
        sprintf(
            "Hi %s, thank you for purchasing %s!",
            $user->display_name,
            $product->name
        )
    );
} );
```

## [​](https://developer.surecart.com/documentation/actions-filters/purchases#surecart/purchase_invoked) `surecart/purchase_invoked`

Fired when a purchase is invoked (access is granted). This happens when a subscription is restored, or when manually invoking access.

```
add_action( 'surecart/purchase_invoked', function( $purchase ) {
    $user = $purchase->getWPUser();
    if ( $user ) {
        wp_mail( $user->user_email, 'Access Restored', 'Your access has been restored.' );
    }
} );
```

## [​](https://developer.surecart.com/documentation/actions-filters/purchases#surecart/purchase_revoked) `surecart/purchase_revoked`

Fired when a purchase is revoked (access is removed). This happens when a subscription is canceled or when manually revoking access.

```
add_action( 'surecart/purchase_revoked', function( $purchase ) {
    $user = $purchase->getWPUser();
    if ( $user ) {
        wp_mail(
            $user->user_email,
            'Access Revoked',
            'Your subscription has been canceled and access has been removed.'
        );
    }
} );
```

## [​](https://developer.surecart.com/documentation/actions-filters/purchases#surecart/purchase_updated) `surecart/purchase_updated`

Fired when a purchase is updated, due to upgrade, downgrade, quantity change, or price change.

Parameters: `$purchase` (`\SureCart\Models\Purchase`), `$request` (object — webhook request with `data->object` and `data->previous_attributes`).

```
add_action( 'surecart/purchase_updated', function( $purchase, $request ) {
    $user = $purchase->getWPUser();
    if ( $user ) {
        wp_mail( $user->user_email, 'Purchase Updated', 'Your purchase has been successfully modified.' );
    }
}, 10, 2 );
```
