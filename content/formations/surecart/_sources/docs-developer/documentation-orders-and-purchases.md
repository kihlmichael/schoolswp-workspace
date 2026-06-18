---
source_url: https://developer.surecart.com/documentation/orders-and-purchases
source: surecart-developer-docs
scraped: true
---

[Skip to main content](https://developer.surecart.com/documentation/orders-and-purchases#content-area)

> ## Documentation Index
>
> Fetch the complete documentation index at: [https://developer.surecart.com/llms.txt](https://developer.surecart.com/llms.txt)
>
> Use this file to discover all available pages before exploring further.

Integrating with sophisticated pricing structures can be complex. SureCart abstracts away many of the complexities by extending an integration PHP class. You implement what you want to do when a purchase is created, invoked, or revoked.

## [​](https://developer.surecart.com/documentation/orders-and-purchases#purchases) Purchases

A purchase is the state of what a customer currently should have "access" to. It is tied 1:1 to a product, price, and optionally a variant.

# [​](https://developer.surecart.com/documentation/orders-and-purchases#purchase-lifecycle) Purchase Lifecycle

### Purchase Created

Created the first time a customer completes an order, or when upgrading/downgrading a subscription. Typically, this is when an integration provides "access" to something.

### Purchase Revoked

Can be revoked manually by the Merchant or automatically (subscription canceled/expired, or plan change). When a new purchase is created for an upgrade/downgrade, the old purchase is revoked.

### Purchase Invoked

A purchase is 'invoked' when a previously revoked purchase is un-revoked. Great for restoration scenarios — e.g., you only want to send a welcome email on first purchase, not on reinstatement.

## [​](https://developer.surecart.com/documentation/orders-and-purchases#example-creating-a-user-role-switcher) Example: Creating A User Role Switcher

### Step 1 — Extend IntegrationService

```
<?php

namespace MyPlugin\Integrations;

use SureCart\Integrations\Contracts\IntegrationInterface;
use SureCart\Integrations\Contracts\PurchaseSyncInterface;
use SureCart\Integrations\IntegrationService;

class UserRoleChangeIntegration extends IntegrationService implements IntegrationInterface, PurchaseSyncInterface {
}
```

### Step 2 — Set the integration details

```
public function getName() { return 'my-plugin/user-role-change'; }
public function getModel() { return 'product'; }
public function getLogo() { return esc_url_raw( trailingslashit( plugin_dir_url( __FILE__ ) ) . 'icon.svg' ); }
public function getLabel() { return __( 'Change WordPress User Role', 'surecart' ); }
public function getItemLabel() { return __( 'Change User Role', 'surecart' ); }
public function getItemHelp() { return __( 'Change the user role of the user who purchased the product.', 'surecart' ); }
```

### Step 3 — Populate the integration item chooser

`getItems()` must return arrays with `id` and `label`. `getItem($id)` returns a single item.

```
public function getItems( $items = [], $search = '' ) {
    $roles          = [];
    $editable_roles = wp_roles()->roles;
    foreach ( $editable_roles as $role => $details ) {
        $sub['id']      = esc_attr( $role );
        $sub['label']   = translate_user_role( $details['name'] );
        $roles[ $role ] = $sub;
    }
    return $roles;
}

public function getItem( $id ) {
    return [ 'id' => $id, 'label' => wp_roles()->get_names()[ $id ] ];
}
```

### Step 4 — Handle purchase lifecycle events

`$integration->integration_id` is the saved `id` from `getItem`/`getItems`.

```
public function onPurchaseCreated( $integration, $wp_user ) {
    $this->toggleRole( $integration->integration_id, $wp_user, true );
}

public function onPurchaseInvoked( $integration, $wp_user ) {
    $this->onPurchaseCreated( $integration, $wp_user );
}

public function onPurchaseRevoked( $integration, $wp_user ) {
    $this->toggleRole( $integration->integration_id, $wp_user, false );
}

public function toggleRole( $role, $wp_user, $add = true ) {
    $role_object = get_role( $role );
    if ( ! $role_object ) { return; }
    return $add ? $wp_user->add_role( $role ) : $wp_user->remove_role( $role );
}
```

Optional methods: `onPurchaseQuantityUpdated()`, `onPurchaseProductAdded()`, `onPurchaseProductRemoved()`. If not defined, `onPurchaseCreated`/`onPurchaseRevoked` are called as fallback.

### Step 5 — Bootstrap the integration

```
(new \MyPlugin\Integrations\UserRoleChangeIntegration())->bootstrap();
```
