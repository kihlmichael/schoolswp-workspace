# FluentCart Developer Docs - Hooks (Actions) (Part 3/5)

Toutes les actions WordPress exposées par FluentCart, groupées par domaine (orders, subscriptions, cart & checkout, customers & users, products & coupons, licenses, admin & templates, payments & integrations).

---

## Licenses | FluentCart Developer Docs

**URL** : https://dev.fluentcart.com/hooks/actions/licenses

[Skip to content](https://dev.fluentcart.com/hooks/actions/licenses#VPContent)

Pro

# Licenses [​](https://dev.fluentcart.com/hooks/actions/licenses\#licenses)

Action hooks for software licensing lifecycle management including [License](https://dev.fluentcart.com/database/models/license.html) status changes, [LicenseActivation](https://dev.fluentcart.com/database/models/license-activation.html) management, [LicenseSite](https://dev.fluentcart.com/database/models/license-site.html) activations/deactivations, and bulk operations. All hooks in this section require the FluentCart Pro plugin.

* * *

## License Status [​](https://dev.fluentcart.com/hooks/actions/licenses\#license-status)

### ` license_status_updated` [​](https://dev.fluentcart.com/hooks/actions/licenses\#license-status-updated)

`fluent_cart_sl/license_status_updated`Pro - Fires on any license status change

**When it runs:** This action fires whenever a [License](https://dev.fluentcart.com/database/models/license.html)'s status transitions from one value to another (e.g., `active` to `expired`, `active` to `disabled`, etc.).

**Parameters:**

- `$data`(array): License status change data
  - `license` ( [`\FluentCart\App\Models\License`](https://dev.fluentcart.com/database/models/license.html)) - The license model after the status change
  - `old_status` (string) - The previous status value
  - `new_status` (string) - The new status value

**Source:**`fluent-cart-pro/app/Modules/Licensing/Models/License.php:206`

**Usage:**

php

```
add_action('fluent_cart_sl/license_status_updated', function ($data) {
    $license   = $data['license'];
    $oldStatus = $data['old_status'];
    $newStatus = $data['new_status'];

    fluent_cart_add_log(
        'License Status Changed',
        sprintf('License #%d changed from %s to %s', $license->id, $oldStatus, $newStatus),
        'info'
    );
}, 10, 1);
```

### ` license_status_updated_to_{$newStatus}` [​](https://dev.fluentcart.com/hooks/actions/licenses\#license-status-updated-to-newstatus)

`fluent_cart_sl/license_status_updated_to_{$newStatus}`Pro - Fires when a license transitions to a specific status

**When it runs:** This is a dynamic hook that fires for a specific target status. For example, `fluent_cart_sl/license_status_updated_to_expired` fires only when a [License](https://dev.fluentcart.com/database/models/license.html) becomes `expired`.

**Parameters:**

- `$data`(array): License status change data
  - `license` ( [`\FluentCart\App\Models\License`](https://dev.fluentcart.com/database/models/license.html)) - The license model after the status change
  - `old_status` (string) - The previous status value
  - `new_status` (string) - The new status value

**Source:**`fluent-cart-pro/app/Modules/Licensing/Models/License.php:211`

**Usage:**

php

```
add_action('fluent_cart_sl/license_status_updated_to_expired', function ($data) {
    $license   = $data['license'];
    $oldStatus = $data['old_status'];
    $newStatus = $data['new_status'];

    // Handle license expiration
    wp_mail(get_option('admin_email'), 'License Expired', sprintf('License #%d has expired.', $license->id));
}, 10, 1);
```

* * *

## License Activation Status [​](https://dev.fluentcart.com/hooks/actions/licenses\#license-activation-status)

### ` license_activation_status_updated` [​](https://dev.fluentcart.com/hooks/actions/licenses\#license-activation-status-updated)

`fluent_cart_sl/license_activation_status_updated`Pro - Fires on any license activation status change

**When it runs:** This action fires whenever a [LicenseActivation](https://dev.fluentcart.com/database/models/license-activation.html)'s status transitions from one value to another.

**Parameters:**

- `$data`(array): License activation status change data
  - `license` ( [`\FluentCart\App\Models\LicenseActivation`](https://dev.fluentcart.com/database/models/license-activation.html)) - The license activation model (note: key is `license` but value is a LicenseActivation instance)
  - `old_status` (string) - The previous activation status
  - `new_status` (string) - The new activation status

**Source:**`fluent-cart-pro/app/Modules/Licensing/Models/LicenseActivation.php:52`

**Usage:**

php

```
add_action('fluent_cart_sl/license_activation_status_updated', function ($data) {
    $activation = $data['license']; // Note: key is 'license' but value is a LicenseActivation instance
    $oldStatus  = $data['old_status'];
    $newStatus  = $data['new_status'];

    fluent_cart_add_log(
        'License Activation Status Changed',
        sprintf('Activation #%d status changed from %s to %s', $activation->id, $oldStatus, $newStatus),
        'info'
    );
}, 10, 1);
```

### ` license_activation_status_updated_to_{$newStatus}` [​](https://dev.fluentcart.com/hooks/actions/licenses\#license-activation-status-updated-to-newstatus)

`fluent_cart_sl/license_activation_status_updated_to_{$newStatus}`Pro - Fires when a license activation transitions to a specific status

**When it runs:** This is a dynamic hook that fires for a specific target [LicenseActivation](https://dev.fluentcart.com/database/models/license-activation.html) status.

**Parameters:**

- `$data`(array): License activation status change data
  - `license` ( [`\FluentCart\App\Models\LicenseActivation`](https://dev.fluentcart.com/database/models/license-activation.html)) - The license activation model (note: key is `license` but value is a LicenseActivation instance)
  - `old_status` (string) - The previous activation status
  - `new_status` (string) - The new activation status

**Source:**`fluent-cart-pro/app/Modules/Licensing/Models/LicenseActivation.php:57`

**Usage:**

php

```
add_action('fluent_cart_sl/license_activation_status_updated_to_active', function ($data) {
    $activation = $data['license']; // Note: key is 'license' but value is a LicenseActivation instance
    $oldStatus  = $data['old_status'];
    $newStatus  = $data['new_status'];

    // Handle activation becoming active
}, 10, 1);
```

* * *

## License Limits [​](https://dev.fluentcart.com/hooks/actions/licenses\#license-limits)

### ` license_limit_increased (activation count)` [​](https://dev.fluentcart.com/hooks/actions/licenses\#license-limit-increased-activation-count)

`fluent_cart_sl/license_limit_increased`Pro - Fires when the license activation count is increased

**When it runs:** This action fires when a [License](https://dev.fluentcart.com/database/models/license.html)'s activation count is increased.

**Parameters:**

- `$data`(array): License limit change data
  - `license` ( [`\FluentCart\App\Models\License`](https://dev.fluentcart.com/database/models/license.html)) - The license model
  - `old_count` (int) - The previous activation count

**Source:**`fluent-cart-pro/app/Modules/Licensing/Models/License.php:224`

**Usage:**

php

```
add_action('fluent_cart_sl/license_limit_increased', function ($data) {
    $license  = $data['license'];
    $oldCount = $data['old_count'];

    fluent_cart_add_log(
        'License Activation Count Increased',
        sprintf('License #%d activation count increased from %d', $license->id, $oldCount),
        'info'
    );
}, 10, 1);
```

### ` license_limit_decreased` [​](https://dev.fluentcart.com/hooks/actions/licenses\#license-limit-decreased)

`fluent_cart_sl/license_limit_decreased`Pro - Fires when the license activation count is decreased

**When it runs:** This action fires when a [License](https://dev.fluentcart.com/database/models/license.html)'s activation count is decreased.

**Parameters:**

- `$data`(array): License limit change data
  - `license` ( [`\FluentCart\App\Models\License`](https://dev.fluentcart.com/database/models/license.html)) - The license model
  - `old_count` (int) - The previous activation count

**Source:**`fluent-cart-pro/app/Modules/Licensing/Models/License.php:239`

**Usage:**

php

```
add_action('fluent_cart_sl/license_limit_decreased', function ($data) {
    $license  = $data['license'];
    $oldCount = $data['old_count'];

    fluent_cart_add_log(
        'License Activation Count Decreased',
        sprintf('License #%d activation count decreased from %d', $license->id, $oldCount),
        'info'
    );
}, 10, 1);
```

### ` license_limit_increased (limit slots)` [​](https://dev.fluentcart.com/hooks/actions/licenses\#license-limit-increased-limit-slots)

`fluent_cart_sl/license_limit_increased`Pro - Fires when the license activation limit (slots) is increased

**When it runs:** This action fires when a [License](https://dev.fluentcart.com/database/models/license.html)'s activation limit (maximum allowed activations) is increased.

**Parameters:**

- `$data`(array): License limit change data
  - `license` ( [`\FluentCart\App\Models\License`](https://dev.fluentcart.com/database/models/license.html)) - The license model
  - `old_count` (int) - The previous activation limit

**Source:**`fluent-cart-pro/app/Modules/Licensing/Models/License.php:259`

**Usage:**

php

```
add_action('fluent_cart_sl/license_limit_increased', function ($data) {
    $license  = $data['license'];
    $oldCount = $data['old_count'];

    fluent_cart_add_log(
        'License Limit Increased',
        sprintf('License #%d activation limit increased from %d', $license->id, $oldCount),
        'info'
    );
}, 10, 1);
```

* * *

## License Key & Validity [​](https://dev.fluentcart.com/hooks/actions/licenses\#license-key-validity)

### ` license_key_regenerated` [​](https://dev.fluentcart.com/hooks/actions/licenses\#license-key-regenerated)

`fluent_cart_sl/license_key_regenerated`Pro - Fires when a license key is regenerated

**When it runs:** This action fires when a license key is regenerated, replacing the old key with a new one.

**Parameters:**

- `$data`(array): License key change data
  - `license` ( [`\FluentCart\App\Models\License`](https://dev.fluentcart.com/database/models/license.html)) - The license model with the new key
  - `old_key` (string) - The previous license key

**Source:**`fluent-cart-pro/app/Modules/Licensing/Models/License.php:318`

**Usage:**

php

```
add_action('fluent_cart_sl/license_key_regenerated', function ($data) {
    $license = $data['license'];
    $oldKey  = $data['old_key'];

    fluent_cart_add_log(
        'License Key Regenerated',
        sprintf('License #%d key was regenerated', $license->id),
        'info'
    );
}, 10, 1);
```

### ` license_validity_extended` [​](https://dev.fluentcart.com/hooks/actions/licenses\#license-validity-extended)

`fluent_cart_sl/license_validity_extended`Pro - Fires when a license expiration date is changed

**When it runs:** This action fires when a license's expiration date is modified to a new date.

**Parameters:**

- `$data`(array): License validity change data
  - `license` ( [`\FluentCart\App\Models\License`](https://dev.fluentcart.com/database/models/license.html)) - The license model
  - `old_date` (string) - The previous expiration date
  - `new_date` (string) - The new expiration date

**Source:**`fluent-cart-pro/app/Modules/Licensing/Models/License.php:348`

**Usage:**

php

```
add_action('fluent_cart_sl/license_validity_extended', function ($data) {
    $license = $data['license'];
    $oldDate = $data['old_date'];
    $newDate = $data['new_date'];

    fluent_cart_add_log(
        'License Validity Extended',
        sprintf('License #%d expiration changed from %s to %s', $license->id, $oldDate, $newDate),
        'info'
    );
}, 10, 1);
```

* * *

## License Lifecycle [​](https://dev.fluentcart.com/hooks/actions/licenses\#license-lifecycle)

### ` license_issued (order)` [​](https://dev.fluentcart.com/hooks/actions/licenses\#license-issued-order)

`fluent_cart/licensing/license_issued`Pro - Fires when a new license is created for an order

**When it runs:** This action fires when a new license is generated as part of an order fulfillment process.

**Parameters:**

- `$data`(array): License issuance data
  - `license` ( [`\FluentCart\App\Models\License`](https://dev.fluentcart.com/database/models/license.html)) - The newly created license
  - `data` (array) - License creation data
  - `order` ( [`\FluentCart\App\Models\Order`](https://dev.fluentcart.com/database/models/order.html)) - The associated order
  - `subscription` ( [`\FluentCart\App\Models\Subscription`](https://dev.fluentcart.com/database/models/subscription.html) \|null) - The associated subscription, if any

**Source:**`fluent-cart-pro/app/Modules/Licensing/Hooks/Handlers/LicenseGenerationHandler.php:532`

**Usage:**

php

```
add_action('fluent_cart/licensing/license_issued', function ($data) {
    $license      = $data['license'];
    $order        = $data['order'];
    $subscription = $data['subscription'];

    // Notify customer about their new license
    wp_mail(
        $order->customer->email,
        'Your License Key',
        sprintf('Your license key for order #%d is: %s', $order->id, $license->license_key)
    );
}, 10, 1);
```

### ` license_issued (manager)` [​](https://dev.fluentcart.com/hooks/actions/licenses\#license-issued-manager)

`fluent_cart_sl/license_issued`Pro - Fires when a license is issued via the license manager

**When it runs:** This action fires when a license is created through the admin license management interface.

**Parameters:**

- `$data`(array): License issuance data
  - `license` ( [`\FluentCart\App\Models\License`](https://dev.fluentcart.com/database/models/license.html)) - The newly created license
  - `data` (array) - License creation data

**Source:**`fluent-cart-pro/app/Modules/Licensing/Services/LicenseManager.php:261`

**Usage:**

php

```
add_action('fluent_cart_sl/license_issued', function ($data) {
    $license    = $data['license'];
    $createData = $data['data'];

    fluent_cart_add_log(
        'License Issued via Manager',
        sprintf('License #%d issued manually', $license->id),
        'info'
    );
}, 10, 1);
```

### ` license_renewed` [​](https://dev.fluentcart.com/hooks/actions/licenses\#license-renewed)

`fluent_cart/licensing/license_renewed`Pro - Fires when a license expiration is extended on subscription renewal

**When it runs:** This action fires when a license's expiration date is extended because the associated subscription has been successfully renewed.

**Parameters:**

- `$data`(array): License renewal data
  - `license` ( [`\FluentCart\App\Models\License`](https://dev.fluentcart.com/database/models/license.html)) - The renewed license
  - `subscription` ( [`\FluentCart\App\Models\Subscription`](https://dev.fluentcart.com/database/models/subscription.html)) - The associated subscription
  - `prev_status` (string) - The previous license status

**Source:**`fluent-cart-pro/app/Modules/Licensing/Hooks/Handlers/LicenseGenerationHandler.php:231`

**Usage:**

php

```
add_action('fluent_cart/licensing/license_renewed', function ($data) {
    $license      = $data['license'];
    $subscription = $data['subscription'];
    $prevStatus   = $data['prev_status'];

    fluent_cart_add_log(
        'License Renewed',
        sprintf('License #%d renewed via subscription #%d', $license->id, $subscription->id),
        'info'
    );
}, 10, 1);
```

### ` license_expired` [​](https://dev.fluentcart.com/hooks/actions/licenses\#license-expired)

`fluent_cart/licensing/license_expired`Pro - Fires when a license expires due to subscription cancellation or scheduler

**When it runs:** This action fires when a license is marked as expired, either because the associated subscription was cancelled or because the license scheduler determined it has passed its expiration date.

**Parameters:**

- `$data`(array): License expiration data
  - `license` ( [`\FluentCart\App\Models\License`](https://dev.fluentcart.com/database/models/license.html)) - The expired license
  - `subscription` ( [`\FluentCart\App\Models\Subscription`](https://dev.fluentcart.com/database/models/subscription.html)) - The associated subscription
  - `prev_status` (string) - The previous license status

**Source:**`fluent-cart-pro/app/Modules/Licensing/Hooks/Handlers/LicenseGenerationHandler.php:267`, `fluent-cart-pro/app/Modules/Licensing/Hooks/Handlers/LicenseSchedulerHandler.php:46`

**Usage:**

php

```
add_action('fluent_cart/licensing/license_expired', function ($data) {
    $license      = $data['license'];
    $subscription = $data['subscription'];
    $prevStatus   = $data['prev_status'];

    // Notify customer about license expiration
    wp_mail(
        $license->customer->email,
        'License Expired',
        sprintf('Your license #%d has expired.', $license->id)
    );
}, 10, 1);
```

### ` license_disabled` [​](https://dev.fluentcart.com/hooks/actions/licenses\#license-disabled)

`fluent_cart/licensing/license_disabled`Pro - Fires when a license is disabled due to payment failure or refund

**When it runs:** This action fires when a license is disabled, typically because the associated order's payment failed or a refund was processed.

**Parameters:**

- `$data`(array): License disabled data
  - `license` ( [`\FluentCart\App\Models\License`](https://dev.fluentcart.com/database/models/license.html)) - The disabled license
  - `order` ( [`\FluentCart\App\Models\Order`](https://dev.fluentcart.com/database/models/order.html)) - The associated order
  - `reason` (string\|undefined) - The reason for disabling (only present on payment failure; absent on refund)

**Source:**`fluent-cart-pro/app/Modules/Licensing/Hooks/Handlers/LicenseGenerationHandler.php:158`, `fluent-cart-pro/app/Modules/Licensing/Hooks/Handlers/LicenseGenerationHandler.php:196`

**Usage:**

php

```
add_action('fluent_cart/licensing/license_disabled', function ($data) {
    $license = $data['license'];
    $order   = $data['order'];
    $reason  = $data['reason'] ?? '';

    fluent_cart_add_log(
        'License Disabled',
        sprintf('License #%d disabled for order #%d. Reason: %s', $license->id, $order->id, $reason ?: 'refund'),
        'warning'
    );
}, 10, 1);
```

### ` extended_to_lifetime` [​](https://dev.fluentcart.com/hooks/actions/licenses\#extended-to-lifetime)

`fluent_cart/licensing/extended_to_lifetime`Pro - Fires when a license is extended to lifetime on subscription end-of-term

**When it runs:** This action fires when a license is converted to a lifetime license because its associated subscription has completed all billing cycles (end-of-term).

**Parameters:**

- `$data`(array): License lifetime extension data
  - `license` ( [`\FluentCart\App\Models\License`](https://dev.fluentcart.com/database/models/license.html)) - The license extended to lifetime
  - `subscription` ( [`\FluentCart\App\Models\Subscription`](https://dev.fluentcart.com/database/models/subscription.html)) - The associated subscription
  - `prev_status` (string) - The previous license status

**Source:**`fluent-cart-pro/app/Modules/Licensing/Hooks/Handlers/LicenseGenerationHandler.php:302`

**Usage:**

php

```
add_action('fluent_cart/licensing/extended_to_lifetime', function ($data) {
    $license      = $data['license'];
    $subscription = $data['subscription'];
    $prevStatus   = $data['prev_status'];

    wp_mail(
        $license->customer->email,
        'License Extended to Lifetime',
        sprintf('Your license #%d has been extended to lifetime access!', $license->id)
    );
}, 10, 1);
```

### ` license_upgraded` [​](https://dev.fluentcart.com/hooks/actions/licenses\#license-upgraded)

`fluent_cart/licensing/license_upgraded`Pro - Fires when a license is upgraded to a new plan

**When it runs:** This action fires when a license is upgraded to a different plan, typically through a plan change or upgrade flow.

**Parameters:**

- `$data`(array): License upgrade data
  - `license` ( [`\FluentCart\App\Models\License`](https://dev.fluentcart.com/database/models/license.html)) - The upgraded license
  - `order` ( [`\FluentCart\App\Models\Order`](https://dev.fluentcart.com/database/models/order.html)) - The associated order
  - `subscription` ( [`\FluentCart\App\Models\Subscription`](https://dev.fluentcart.com/database/models/subscription.html)) - The associated subscription
  - `updates` (array) - The update data applied to the license

**Source:**`fluent-cart-pro/app/Modules/Licensing/Hooks/Handlers/LicenseGenerationHandler.php:375`

**Usage:**

php

```
add_action('fluent_cart/licensing/license_upgraded', function ($data) {
    $license      = $data['license'];
    $order        = $data['order'];
    $subscription = $data['subscription'];
    $updates      = $data['updates'];

    fluent_cart_add_log(
        'License Upgraded',
        sprintf('License #%d upgraded for order #%d', $license->id, $order->id),
        'info'
    );
}, 10, 1);
```

### ` license_deleted (admin)` [​](https://dev.fluentcart.com/hooks/actions/licenses\#license-deleted-admin)

`fluent_cart_sl/license_deleted`Pro - Fires when a license is deleted from the admin interface

**When it runs:** This action fires when an admin deletes a license through the license management UI.

**Parameters:**

- `$data`(array): License deletion data
  - `license` ( [`\FluentCart\App\Models\License`](https://dev.fluentcart.com/database/models/license.html)) - The license being deleted

**Source:**`fluent-cart-pro/app/Modules/Licensing/Http/Controllers/LicenseController.php:255`

**Usage:**

php

```
add_action('fluent_cart_sl/license_deleted', function ($data) {
    $license = $data['license'];

    fluent_cart_add_log(
        'License Deleted',
        sprintf('License #%d was deleted by admin', $license->id),
        'warning'
    );
}, 10, 1);
```

### ` license_deleted (order deleted)` [​](https://dev.fluentcart.com/hooks/actions/licenses\#license-deleted-order-deleted)

`fluent_cart/licensing/license_deleted`Pro - Fires when a license is deleted because its parent order was deleted

**When it runs:** This action fires when a license is automatically deleted as a result of its parent order being deleted.

**Parameters:**

- `$data`(array): License deletion data
  - `license` ( [`\FluentCart\App\Models\License`](https://dev.fluentcart.com/database/models/license.html)) - The license being deleted
  - `order` ( [`\FluentCart\App\Models\Order`](https://dev.fluentcart.com/database/models/order.html)) - The parent order being deleted

**Source:**`fluent-cart-pro/app/Modules/Licensing/Hooks/license-actions.php:141`

**Usage:**

php

```
add_action('fluent_cart/licensing/license_deleted', function ($data) {
    $license = $data['license'];
    $order   = $data['order'];

    fluent_cart_add_log(
        'License Deleted with Order',
        sprintf('License #%d deleted because order #%d was deleted', $license->id, $order->id),
        'warning'
    );
}, 10, 1);
```

* * *

## License Site Activation [​](https://dev.fluentcart.com/hooks/actions/licenses\#license-site-activation)

### ` site_activated (API)` [​](https://dev.fluentcart.com/hooks/actions/licenses\#site-activated-api)

`fluent_cart/license/site_activated`Pro - Fires when a site is activated for a license via the public API

**When it runs:** This action fires when a site is successfully activated for a license through the external licensing API.

**Parameters:**

- `$site` ( [`\FluentCart\App\Models\LicenseSite`](https://dev.fluentcart.com/database/models/license-site.html)) - The activated site
- `$activation` ( [`\FluentCart\App\Models\LicenseActivation`](https://dev.fluentcart.com/database/models/license-activation.html)) - The license activation record
- `$license` ( [`\FluentCart\App\Models\License`](https://dev.fluentcart.com/database/models/license.html)) - The associated license
- `$data` (array) - The activation request data

**Source:**`fluent-cart-pro/app/Modules/Licensing/Hooks/Handlers/LicenseApiHandler.php:255`

**Usage:**

php

```
add_action('fluent_cart/license/site_activated', function ($site, $activation, $license, $data) {
    fluent_cart_add_log(
        'Site Activated via API',
        sprintf('Site %s activated for license #%d', $site->site_url, $license->id),
        'info'
    );
}, 10, 4);
```

### ` site_deactivated (API)` [​](https://dev.fluentcart.com/hooks/actions/licenses\#site-deactivated-api)

`fluent_cart/license/site_deactivated`Pro - Fires when a site is deactivated via the public API

**When it runs:** This action fires when a site is successfully deactivated for a license through the external licensing API.

**Parameters:**

- `$site` ( [`\FluentCart\App\Models\LicenseSite`](https://dev.fluentcart.com/database/models/license-site.html)) - The deactivated site
- `$activation` ( [`\FluentCart\App\Models\LicenseActivation`](https://dev.fluentcart.com/database/models/license-activation.html)) - The license activation record
- `$license` ( [`\FluentCart\App\Models\License`](https://dev.fluentcart.com/database/models/license.html)) - The associated license
- `$data` (array) - The deactivation request data

**Source:**`fluent-cart-pro/app/Modules/Licensing/Hooks/Handlers/LicenseApiHandler.php:340`

**Usage:**

php

```
add_action('fluent_cart/license/site_deactivated', function ($site, $activation, $license, $data) {
    fluent_cart_add_log(
        'Site Deactivated via API',
        sprintf('Site %s deactivated for license #%d', $site->site_url, $license->id),
        'info'
    );
}, 10, 4);
```

### ` site_deactivated_failed` [​](https://dev.fluentcart.com/hooks/actions/licenses\#site-deactivated-failed)

`fluent_cart/license/site_deactivated_failed`Pro - Fires when a site deactivation attempt fails

**When it runs:** This action fires when a site deactivation request fails. This can happen for multiple reasons such as an invalid license key, site not found, or activation mismatch.

**Parameters:**

- `$formattedData` (array) - Error information including the reason for failure

**Source:**`fluent-cart-pro/app/Modules/Licensing/Hooks/Handlers/LicenseApiHandler.php:295,309,321`

**Usage:**

php

```
add_action('fluent_cart/license/site_deactivated_failed', function ($formattedData) {
    fluent_cart_add_log(
        'Site Deactivation Failed',
        wp_json_encode($formattedData),
        'error'
    );
}, 10, 1);
```

### ` site_activated (local)` [​](https://dev.fluentcart.com/hooks/actions/licenses\#site-activated-local)

`fluent_cart_sl/site_activated`Pro - Fires when a site is activated via the local API method

**When it runs:** This action fires when a site is activated through the internal (local) license site management method.

**Parameters:**

- `$data`(array): Site activation data
  - `site` ( [`\FluentCart\App\Models\LicenseSite`](https://dev.fluentcart.com/database/models/license-site.html)) - The activated site
  - `license` ( [`\FluentCart\App\Models\License`](https://dev.fluentcart.com/database/models/license.html)) - The associated license
  - `activation` ( [`\FluentCart\App\Models\LicenseActivation`](https://dev.fluentcart.com/database/models/license-activation.html)) - The license activation record

**Source:**`fluent-cart-pro/app/Modules/Licensing/Concerns/CanManageLicenseSites.php:84`

**Usage:**

php

```
add_action('fluent_cart_sl/site_activated', function ($data) {
    $site       = $data['site'];
    $license    = $data['license'];
    $activation = $data['activation'];

    fluent_cart_add_log(
        'Site Activated Locally',
        sprintf('Site %s activated for license #%d', $site->site_url, $license->id),
        'info'
    );
}, 10, 1);
```

### ` site_license_deactivated` [​](https://dev.fluentcart.com/hooks/actions/licenses\#site-license-deactivated)

`fluent_cart_sl/site_license_deactivated`Pro - Fires when a license is deactivated from a site (admin or customer)

**When it runs:** This action fires when a license is deactivated from a specific site, either by an admin through the management interface or by the customer through their profile.

**Parameters:**

- `$data`(array): Site deactivation data
  - `site` ( [`\FluentCart\App\Models\LicenseSite`](https://dev.fluentcart.com/database/models/license-site.html)) - The site being deactivated
  - `license` ( [`\FluentCart\App\Models\License`](https://dev.fluentcart.com/database/models/license.html)) - The associated license

**Source:**`fluent-cart-pro/app/Modules/Licensing/Concerns/CanManageLicenseSites.php:141,177`, `fluent-cart-pro/app/Modules/Licensing/Http/Controllers/CustomerProfileController.php:192`

**Usage:**

php

```
add_action('fluent_cart_sl/site_license_deactivated', function ($data) {
    $site    = $data['site'];
    $license = $data['license'];

    fluent_cart_add_log(
        'Site License Deactivated',
        sprintf('License #%d deactivated from site %s', $license->id, $site->site_url),
        'info'
    );
}, 10, 1);
```

* * *

## Bulk License Operations [​](https://dev.fluentcart.com/hooks/actions/licenses\#bulk-license-operations)

### ` before_deleting_licenses` [​](https://dev.fluentcart.com/hooks/actions/licenses\#before-deleting-licenses)

`fluent_cart_sl/before_deleting_licenses`Pro - Fires before licenses are bulk deleted by order

**When it runs:** This action fires immediately before a collection of licenses is deleted as part of a bulk operation (e.g., when an order is deleted).

**Parameters:**

- `$data`(array): Bulk deletion data
  - `licenses` (`\Illuminate\Support\Collection`) - Collection of [License](https://dev.fluentcart.com/database/models/license.html) models about to be deleted

**Source:**`fluent-cart-pro/app/Modules/Licensing/Services/LicenseManager.php:232`

**Usage:**

php

```
add_action('fluent_cart_sl/before_deleting_licenses', function ($data) {
    $licenses = $data['licenses'];

    foreach ($licenses as $license) {
        fluent_cart_add_log('License Bulk Delete', sprintf('About to delete license #%d', $license->id), 'warning');
    }
}, 10, 1);
```

### ` after_deleting_licenses` [​](https://dev.fluentcart.com/hooks/actions/licenses\#after-deleting-licenses)

`fluent_cart_sl/after_deleting_licenses`Pro - Fires after licenses are bulk deleted

**When it runs:** This action fires immediately after a collection of licenses has been deleted.

**Parameters:**

- `$data`(array): Bulk deletion data
  - `licenses` (`\Illuminate\Support\Collection`) - Collection of [License](https://dev.fluentcart.com/database/models/license.html) models that were deleted

**Source:**`fluent-cart-pro/app/Modules/Licensing/Services/LicenseManager.php:237`

**Usage:**

php

```
add_action('fluent_cart_sl/after_deleting_licenses', function ($data) {
    $licenses = $data['licenses'];

    fluent_cart_add_log('Licenses Bulk Deleted', sprintf('%d licenses were deleted', $licenses->count()), 'warning');
}, 10, 1);
```

### ` before_updating_licenses_status` [​](https://dev.fluentcart.com/hooks/actions/licenses\#before-updating-licenses-status)

`fluent_cart_sl/before_updating_licenses_status`Pro - Fires before a bulk license status update

**When it runs:** This action fires immediately before a collection of licenses has their status updated in bulk.

**Parameters:**

- `$data`(array): Bulk status update data
  - `licenses` (`\Illuminate\Support\Collection`) - Collection of [License](https://dev.fluentcart.com/database/models/license.html) models about to be updated

**Source:**`fluent-cart-pro/app/Modules/Licensing/Services/LicenseManager.php:285`

**Usage:**

php

```
add_action('fluent_cart_sl/before_updating_licenses_status', function ($data) {
    $licenses = $data['licenses'];

    // Log or validate before bulk status change
}, 10, 1);
```

### ` before_updating_licenses_status_to_disabled` [​](https://dev.fluentcart.com/hooks/actions/licenses\#before-updating-licenses-status-to-disabled)

`fluent_cart_sl/before_updating_licenses_status_to_disabled`Pro - Fires before licenses are bulk disabled

**When it runs:** This action fires immediately before a collection of licenses is bulk-disabled.

**Parameters:**

- `$data`(array): Bulk disable data
  - `licenses` (`\Illuminate\Support\Collection`) - Collection of [License](https://dev.fluentcart.com/database/models/license.html) models about to be disabled

**Source:**`fluent-cart-pro/app/Modules/Licensing/Services/LicenseManager.php:286`

**Usage:**

php

```
add_action('fluent_cart_sl/before_updating_licenses_status_to_disabled', function ($data) {
    $licenses = $data['licenses'];

    // Perform pre-disable checks
}, 10, 1);
```

### ` after_updating_licenses_status` [​](https://dev.fluentcart.com/hooks/actions/licenses\#after-updating-licenses-status)

`fluent_cart_sl/after_updating_licenses_status`Pro - Fires after a bulk license status update

**When it runs:** This action fires immediately after a collection of licenses has had their status updated in bulk.

**Parameters:**

- `$data`(array): Bulk status update data
  - `licenses` (`\Illuminate\Support\Collection`) - Collection of [License](https://dev.fluentcart.com/database/models/license.html) models that were updated

**Source:**`fluent-cart-pro/app/Modules/Licensing/Services/LicenseManager.php:290`

**Usage:**

php

```
add_action('fluent_cart_sl/after_updating_licenses_status', function ($data) {
    $licenses = $data['licenses'];

    fluent_cart_add_log('Licenses Status Updated', sprintf('%d licenses updated', $licenses->count()), 'info');
}, 10, 1);
```

### ` after_updating_licenses_status_to_disabled` [​](https://dev.fluentcart.com/hooks/actions/licenses\#after-updating-licenses-status-to-disabled)

`fluent_cart_sl/after_updating_licenses_status_to_disabled`Pro - Fires after licenses are bulk disabled

**When it runs:** This action fires immediately after a collection of licenses has been bulk-disabled.

**Parameters:**

- `$data`(array): Bulk disable data
  - `licenses` (`\Illuminate\Support\Collection`) - Collection of [License](https://dev.fluentcart.com/database/models/license.html) models that were disabled

**Source:**`fluent-cart-pro/app/Modules/Licensing/Services/LicenseManager.php:291`

**Usage:**

php

```
add_action('fluent_cart_sl/after_updating_licenses_status_to_disabled', function ($data) {
    $licenses = $data['licenses'];

    fluent_cart_add_log('Licenses Bulk Disabled', sprintf('%d licenses disabled', $licenses->count()), 'warning');
}, 10, 1);
```

* * *

Today

Hi! I’m your AI assistant. How can I assist you today?

Just now

Powered by **FluentBot**


---

---

## Orders | FluentCart Developer Docs

**URL** : https://dev.fluentcart.com/hooks/actions/orders

[Skip to content](https://dev.fluentcart.com/hooks/actions/orders#VPContent)

# Orders [​](https://dev.fluentcart.com/hooks/actions/orders\#orders)

All hooks related to order lifecycle, status transitions, payments, shipping, refunds, and order items. These action hooks allow you to respond to key order events in FluentCart.

Each hook passes an associative array as its single parameter. The `order` value is always an [`\FluentCart\App\Models\Order`](https://dev.fluentcart.com/database/models/order.html) model instance with the [`customer`](https://dev.fluentcart.com/database/models/customer.html), `shipping_address`, and `billing_address` relationships eager-loaded (unless noted otherwise).

> **Amounts are in cents.** All monetary values (`total`, `refunded_amount`, etc.) are stored as integers in the smallest currency unit. Use `Helper::toDecimal($amount)` to convert for display.

* * *

## Order Status Changes [​](https://dev.fluentcart.com/hooks/actions/orders\#order-status-changes)

Fired when the **order status** field changes (e.g. `processing` → `completed`). Both a dynamic, status-specific hook and a generic hook fire on every change.

### ` order_status_changed_to_{status}` [​](https://dev.fluentcart.com/hooks/actions/orders\#order-status-changed-to-status)

`fluent_cart/order_status_changed_to_{$newStatus}` - Fires when the order status changes to a specific status

**When it runs:** Fires inside `OrderStatusUpdated::afterDispatch()` whenever the order status type transitions to a new value. The `{$newStatus}` portion is replaced dynamically with the target status, so you can listen for a single status you care about.

**Available dynamic variants:**`completed`, `canceled`, `processing`, `on-hold`, `failed`

**Parameters:**

- `$data` (array): Order status change data
php

```
$data = [\
      'order'       => $order,       // \FluentCart\App\Models\Order (with customer, addresses loaded)\
      'old_status'  => 'processing', // Previous order status string\
      'new_status'  => 'completed',  // New order status string (matches the dynamic suffix)\
      'manageStock' => true,         // Whether stock management should be applied\
      'activity'    => [             // Optional activity log context\
          'title'   => '',\
          'content' => '',\
      ],\
];
```


**Source:**`app/Events/Order/OrderStatusUpdated.php` (line 91)

**Usage:**

php

```
add_action('fluent_cart/order_status_changed_to_completed', function ($data) {
    $order = $data['order'];
    // Grant digital access when order completes
    grant_digital_access($order->customer_id, $order->id);
}, 10, 1);
```

### ` order_status_changed` [​](https://dev.fluentcart.com/hooks/actions/orders\#order-status-changed)

`fluent_cart/order_status_changed` - Fires on any order status change

**When it runs:** Fires immediately after the dynamic `order_status_changed_to_{$newStatus}` hook, on every order status transition regardless of the target status. Use this when you need to react to all status changes in a single callback.

**Parameters:**

- `$data` (array): Order status change data
php

```
$data = [\
      'order'       => $order,       // \FluentCart\App\Models\Order\
      'old_status'  => 'processing', // Previous order status\
      'new_status'  => 'completed',  // New order status\
      'manageStock' => true,         // Whether stock management applies\
      'activity'    => [\
          'title'   => '',\
          'content' => '',\
      ],\
];
```


**Source:**`app/Events/Order/OrderStatusUpdated.php` (line 92)

**Usage:**

php

```
add_action('fluent_cart/order_status_changed', function ($data) {
    $order = $data['order'];
    // Log every status transition
    fluent_cart_add_log(
        'Order status changed',
        sprintf('Order #%d: %s -> %s', $order->id, $data['old_status'], $data['new_status']),
        'info'
    );
}, 10, 1);
```

* * *

## Payment Status Changes [​](https://dev.fluentcart.com/hooks/actions/orders\#payment-status-changes)

Fired when the **payment status** field changes (e.g. `pending` → `paid`). Both a dynamic, status-specific hook and a generic hook fire on every change.

### ` payment_status_changed_to_{status}` [​](https://dev.fluentcart.com/hooks/actions/orders\#payment-status-changed-to-status)

`fluent_cart/payment_status_changed_to_{$newStatus}` - Fires when payment status changes to a specific status

**When it runs:** Fires inside `OrderStatusUpdated::afterDispatch()` when the status change type is `payment_status`. The `{$newStatus}` suffix is replaced dynamically so you can target a single payment state.

**Available dynamic variants:**`pending`, `paid`, `partially_paid`, `failed`, `refunded`, `partially_refunded`, `authorized`

**Parameters:**

- `$data` (array): Payment status change data
php

```
$data = [\
      'order'       => $order,     // \FluentCart\App\Models\Order\
      'old_status'  => 'pending',  // Previous payment status\
      'new_status'  => 'paid',     // New payment status (matches the dynamic suffix)\
      'manageStock' => true,       // Whether stock management applies\
      'activity'    => [\
          'title'   => '',\
          'content' => '',\
      ],\
];
```


**Source:**`app/Events/Order/OrderStatusUpdated.php` (line 81)

**Usage:**

php

```
add_action('fluent_cart/payment_status_changed_to_paid', function ($data) {
    $order = $data['order'];
    // Trigger fulfillment workflow when payment is confirmed
    do_action('my_custom_fulfillment_start', $order->id);
}, 10, 1);
```

### ` payment_status_changed` [​](https://dev.fluentcart.com/hooks/actions/orders\#payment-status-changed)

`fluent_cart/payment_status_changed` - Fires on any payment status change

**When it runs:** Fires immediately after the dynamic `payment_status_changed_to_{$newStatus}` hook, on every payment status transition. Use this when you need a single callback for all payment status changes.

**Parameters:**

- `$data` (array): Payment status change data
php

```
$data = [\
      'order'       => $order,     // \FluentCart\App\Models\Order\
      'old_status'  => 'pending',  // Previous payment status\
      'new_status'  => 'paid',     // New payment status\
      'manageStock' => true,       // Whether stock management applies\
      'activity'    => [\
          'title'   => '',\
          'content' => '',\
      ],\
];
```


**Source:**`app/Events/Order/OrderStatusUpdated.php` (line 82)

**Usage:**

php

```
add_action('fluent_cart/payment_status_changed', function ($data) {
    $order = $data['order'];
    // Send payment status update notification
    if ($data['new_status'] === 'paid') {
        wp_mail($order->customer->email, 'Payment Confirmed', 'Your payment has been received.');
    }
}, 10, 1);
```

* * *

## Shipping Status Changes [​](https://dev.fluentcart.com/hooks/actions/orders\#shipping-status-changes)

Fired when the **shipping status** field changes (e.g. `unshipped` → `shipped`). Both a dynamic, status-specific hook and a generic hook fire on every change.

### ` shipping_status_changed_to_{status}` [​](https://dev.fluentcart.com/hooks/actions/orders\#shipping-status-changed-to-status)

`fluent_cart/shipping_status_changed_to_{$newStatus}` - Fires when shipping status changes to a specific status

**When it runs:** Fires inside `OrderStatusUpdated::afterDispatch()` when the status change type is `shipping_status`. The `{$newStatus}` suffix is replaced dynamically so you can target a single shipping state.

**Available dynamic variants:**`unshipped`, `shipped`, `delivered`, `unshippable`

**Parameters:**

- `$data` (array): Shipping status change data
php

```
$data = [\
      'order'       => $order,      // \FluentCart\App\Models\Order\
      'old_status'  => 'unshipped', // Previous shipping status\
      'new_status'  => 'shipped',   // New shipping status (matches the dynamic suffix)\
      'manageStock' => true,        // Whether stock management applies\
      'activity'    => [\
          'title'   => '',\
          'content' => '',\
      ],\
];
```


**Source:**`app/Events/Order/OrderStatusUpdated.php` (line 86)

**Usage:**

php

```
add_action('fluent_cart/shipping_status_changed_to_shipped', function ($data) {
    $order = $data['order'];
    // Notify customer that their order has shipped
    wp_mail(
        $order->customer->email,
        'Your Order Has Shipped!',
        sprintf('Order #%d has been shipped.', $order->id)
    );
}, 10, 1);
```

### ` shipping_status_changed` [​](https://dev.fluentcart.com/hooks/actions/orders\#shipping-status-changed)

`fluent_cart/shipping_status_changed` - Fires on any shipping status change

**When it runs:** Fires immediately after the dynamic `shipping_status_changed_to_{$newStatus}` hook, on every shipping status transition. Use this when you need a single callback for all shipping status changes.

**Parameters:**

- `$data` (array): Shipping status change data
php

```
$data = [\
      'order'       => $order,      // \FluentCart\App\Models\Order\
      'old_status'  => 'unshipped', // Previous shipping status\
      'new_status'  => 'shipped',   // New shipping status\
      'manageStock' => true,        // Whether stock management applies\
      'activity'    => [\
          'title'   => '',\
          'content' => '',\
      ],\
];
```


**Source:**`app/Events/Order/OrderStatusUpdated.php` (line 87)

**Usage:**

php

```
add_action('fluent_cart/shipping_status_changed', function ($data) {
    $order = $data['order'];
    // Log all shipping status transitions
    fluent_cart_add_log(
        'Shipping status changed',
        sprintf('Order #%d: %s -> %s', $order->id, $data['old_status'], $data['new_status']),
        'info'
    );
}, 10, 1);
```

* * *

## Refunds [​](https://dev.fluentcart.com/hooks/actions/orders\#refunds)

Fired during the refund flow after transaction records have been created. The generic `order_refunded` hook fires on every refund, followed by either `order_fully_refunded` or `order_partially_refunded` depending on the refund type. Refund data includes the [Order](https://dev.fluentcart.com/database/models/order.html), [OrderItem](https://dev.fluentcart.com/database/models/order-item.html), [OrderTransaction](https://dev.fluentcart.com/database/models/order-transaction.html), and [Customer](https://dev.fluentcart.com/database/models/customer.html) models.

### ` order_refunded` [​](https://dev.fluentcart.com/hooks/actions/orders\#order-refunded)

`fluent_cart/order_refunded` - Fires after any refund (full or partial)

**When it runs:** Fires inside `OrderRefund::afterDispatch()` after a refund transaction is recorded and the refund amount is calculated. This hook fires for both full and partial refunds. It fires before the type-specific hooks below.

**Parameters:**

- `$data` (array): Refund data
php

```
$data = [\
      'order'              => $order,          // \FluentCart\App\Models\Order\
      'refunded_items'     => [],              // Array of OrderItem models (looked up from refundedItemIds)\
      'new_refunded_items' => [],              // Raw refunded items array with restore_quantity info\
      'refunded_amount'    => 5000,            // Newly refunded amount in cents\
      'manage_stock'       => true,            // Whether stock should be restored\
      'transaction'        => $transaction,    // \FluentCart\App\Models\OrderTransaction (the refund transaction)\
      'customer'           => $customer,       // \FluentCart\App\Models\Customer\
      'type'               => 'full',          // 'full' or 'partial'\
];
```


**Source:**`app/Events/Order/OrderRefund.php` (line 141)

**Usage:**

php

```
add_action('fluent_cart/order_refunded', function ($data) {
    $order = $data['order'];
    $amount = \FluentCart\App\Helpers\Helper::toDecimal($data['refunded_amount']);
    // Notify admin of any refund
    wp_mail(
        get_option('admin_email'),
        sprintf('Refund on Order #%d', $order->id),
        sprintf('A %s refund of %s has been processed.', $data['type'], $amount)
    );
}, 10, 1);
```

### ` order_fully_refunded` [​](https://dev.fluentcart.com/hooks/actions/orders\#order-fully-refunded)

`fluent_cart/order_fully_refunded` - Fires only when an order is fully refunded

**When it runs:** Fires inside `OrderRefund::afterDispatch()` immediately after the generic `order_refunded` hook, but only when the total refunded amount meets or exceeds the order's total paid amount (i.e. full refund).

**Parameters:**

- `$data` (array): Full refund data (identical structure to `order_refunded`)
php

```
$data = [\
      'order'              => $order,          // \FluentCart\App\Models\Order\
      'refunded_items'     => [],              // Array of OrderItem models\
      'new_refunded_items' => [],              // Raw refunded items with restore_quantity\
      'refunded_amount'    => 10000,           // Refunded amount in cents\
      'manage_stock'       => true,            // Whether stock should be restored\
      'transaction'        => $transaction,    // \FluentCart\App\Models\OrderTransaction\
      'customer'           => $customer,       // \FluentCart\App\Models\Customer\
      'type'               => 'full',          // Always 'full' for this hook\
];
```


**Source:**`app/Events/Order/OrderRefund.php` (line 144)

**Usage:**

php

```
add_action('fluent_cart/order_fully_refunded', function ($data) {
    $order = $data['order'];
    // Revoke digital access on full refund
    update_user_meta($order->customer_id, 'membership_active', false);
}, 10, 1);
```

### ` order_partially_refunded` [​](https://dev.fluentcart.com/hooks/actions/orders\#order-partially-refunded)

`fluent_cart/order_partially_refunded` - Fires only when an order is partially refunded

**When it runs:** Fires inside `OrderRefund::afterDispatch()` immediately after the generic `order_refunded` hook, but only when the total refunded amount is less than the order's total paid amount (i.e. partial refund).

**Parameters:**

- `$data` (array): Partial refund data (identical structure to `order_refunded`)
php

```
$data = [\
      'order'              => $order,          // \FluentCart\App\Models\Order\
      'refunded_items'     => [],              // Array of OrderItem models\
      'new_refunded_items' => [],              // Raw refunded items with restore_quantity\
      'refunded_amount'    => 3000,            // Refunded amount in cents\
      'manage_stock'       => true,            // Whether stock should be restored\
      'transaction'        => $transaction,    // \FluentCart\App\Models\OrderTransaction\
      'customer'           => $customer,       // \FluentCart\App\Models\Customer\
      'type'               => 'partial',       // Always 'partial' for this hook\
];
```


**Source:**`app/Events/Order/OrderRefund.php` (line 146)

**Usage:**

php

```
add_action('fluent_cart/order_partially_refunded', function ($data) {
    $order = $data['order'];
    $customer = $data['customer'];
    // Notify customer of partial refund
    wp_mail(
        $customer->email,
        'Partial Refund Processed',
        sprintf('A partial refund has been issued for Order #%d.', $order->id)
    );
}, 10, 1);
```

* * *

## Order Items [​](https://dev.fluentcart.com/hooks/actions/orders\#order-items)

Hooks that fire when custom line items on an order are being deleted. These are useful for cleanup or audit logging on custom [OrderItem](https://dev.fluentcart.com/database/models/order-item.html) records.

### ` order/before_custom_items_deleted` [​](https://dev.fluentcart.com/hooks/actions/orders\#order-before-custom-items-deleted)

`fluent_cart/order/before_custom_items_deleted` - Fires before custom line items are deleted

**When it runs:** Fires inside `OrderResource::updateOrderItems()` just before custom order items (flagged as `is_custom`) are permanently deleted from the database. Only fires if the filtered collection of custom items is not empty.

**Parameters:**

- `$customItems` (\\Illuminate\\Support\\Collection): Collection of [`\FluentCart\App\Models\OrderItem`](https://dev.fluentcart.com/database/models/order-item.html) models about to be deleted (only items where `is_custom` is true)
- `$order` ( [`\FluentCart\App\Models\Order`](https://dev.fluentcart.com/database/models/order.html)): The parent order model

**Source:**`api/Resource/OrderResource.php` (line 535)

**Usage:**

php

```
add_action('fluent_cart/order/before_custom_items_deleted', function ($customItems, $order) {
    // Archive custom items before they are removed
    foreach ($customItems as $item) {
        fluent_cart_add_log(
            'Custom item removed',
            sprintf('Item "%s" removed from Order #%d', $item->title, $order->id),
            'info'
        );
    }
}, 10, 2);
```

### ` order/after_custom_items_deleted` [​](https://dev.fluentcart.com/hooks/actions/orders\#order-after-custom-items-deleted)

`fluent_cart/order/after_custom_items_deleted` - Fires after custom line items are deleted

**When it runs:** Fires inside `OrderResource::updateOrderItems()` immediately after custom order items have been permanently deleted from the database. The collection still holds the model instances (now removed from DB). Only fires if the collection is not empty.

**Parameters:**

- `$customItems` (\\Illuminate\\Support\\Collection): Collection of [`\FluentCart\App\Models\OrderItem`](https://dev.fluentcart.com/database/models/order-item.html) models that were just deleted
- `$order` ( [`\FluentCart\App\Models\Order`](https://dev.fluentcart.com/database/models/order.html)): The parent order model

**Source:**`api/Resource/OrderResource.php` (line 541)

**Usage:**

php

```
add_action('fluent_cart/order/after_custom_items_deleted', function ($customItems, $order) {
    // Recalculate order totals after custom items removed
    $order->recalculateTotals();
}, 10, 2);
```

* * *

## Order Lifecycle [​](https://dev.fluentcart.com/hooks/actions/orders\#order-lifecycle)

General lifecycle hooks that fire at key moments during an [Order](https://dev.fluentcart.com/database/models/order.html)'s existence: invoice generation, [Customer](https://dev.fluentcart.com/database/models/customer.html) changes, payment completion, license generation, and receipt viewing.

### ` order/invoice_number_added` [​](https://dev.fluentcart.com/hooks/actions/orders\#order-invoice-number-added)

`fluent_cart/order/invoice_number_added` - Fires after an invoice/receipt number is assigned to an order

**When it runs:** Fires in two places:

1. Inside the `Order::booted()``created` callback, immediately after a new order is persisted to the database with an invoice number already set (when payment status is `paid` at creation time).
2. Inside `Order::generateReceiptNumber()`, when a receipt number is generated for an existing order that did not previously have one.

**Parameters:**

- `$data` (array): Order data
php

```
$data = [\
      'order' => $order, // \FluentCart\App\Models\Order\
];
```


**Source:**`app/Models/Order.php` (lines 60 and 734)

**Usage:**

php

```
add_action('fluent_cart/order/invoice_number_added', function ($data) {
    $order = $data['order'];
    // Sync invoice number to external accounting system
    sync_to_accounting($order->id, $order->invoice_no, $order->receipt_number);
}, 10, 1);
```

### ` order_customer_changed` [​](https://dev.fluentcart.com/hooks/actions/orders\#order-customer-changed)

`fluent_cart/order_customer_changed` - Fires when the customer assigned to an order changes

**When it runs:** Fires inside `OrderController::changeCustomer()` after the order (and any child orders and [subscriptions](https://dev.fluentcart.com/database/models/subscription.html)) have been reassigned to a new customer, and both the old and new customer stats have been recounted.

**Parameters:**

- `$data` (array): Customer change data
php

```
$data = [\
      'order'               => $order,        // \FluentCart\App\Models\Order\
      'old_customer'        => $oldCustomer,  // \FluentCart\App\Models\Customer|null\
      'new_customer'        => $newCustomer,  // \FluentCart\App\Models\Customer\
      'connected_order_ids' => [123, 124],    // Array of all order IDs updated (parent + children)\
];
```


**Source:**`app/Http/Controllers/OrderController.php` (line 427)

**Usage:**

php

```
add_action('fluent_cart/order_customer_changed', function ($data) {
    $order = $data['order'];
    $oldCustomer = $data['old_customer'];
    $newCustomer = $data['new_customer'];
    // Notify the new customer about the transfer
    wp_mail(
        $newCustomer->email,
        'Order Transferred to Your Account',
        sprintf('Order #%d has been assigned to your account.', $order->id)
    );
}, 10, 1);
```

### ` order/generateMissingLicenses` [​](https://dev.fluentcart.com/hooks/actions/orders\#order-generatemissinglicenses)

`fluent_cart/order/generateMissingLicenses` - Fires when an admin triggers license generation for an order

**When it runs:** Fires inside `OrderController::generateLicense()` when an admin requests license generation for an order that has fewer licenses than expected. This allows license modules to hook in and create the missing license keys.

**Parameters:**

- `$data` (array): Order data
php

```
$data = [\
      'order' => $order, // \FluentCart\App\Models\Order (with order_items and licenses loaded)\
];
```


**Source:**`app/Http/Controllers/OrderController.php` (line 225)

**Usage:**

php

```
add_action('fluent_cart/order/generateMissingLicenses', function ($data) {
    $order = $data['order'];
    // Generate licenses for each eligible order item
    foreach ($order->order_items as $item) {
        generate_license_key($order->id, $item->product_id);
    }
}, 10, 1);
```

### ` order_placed_offline` [​](https://dev.fluentcart.com/hooks/actions/orders\#order-placed-offline)

`fluent_cart/order_placed_offline` - Fires when an order is placed via Cash on Delivery or other offline payment

**When it runs:** Fires inside `CodHandler::processPayment()` after the order and its [transaction](https://dev.fluentcart.com/database/models/order-transaction.html) have been created for an offline/COD payment. The [Order](https://dev.fluentcart.com/database/models/order.html), [Customer](https://dev.fluentcart.com/database/models/customer.html), and transaction data are all available at this point. The order has its `customer`, `shipping_address`, and `billing_address` relationships loaded.

**Parameters:**

- `$data` (array): Offline order data
php

```
$data = [\
      'order'       => $order,                  // \FluentCart\App\Models\Order\
      'customer'    => $order->customer ?? [],   // \FluentCart\App\Models\Customer or empty array\
      'transaction' => $transaction ?? [],        // \FluentCart\App\Models\OrderTransaction or empty array\
];
```


**Source:**`app/Modules/PaymentMethods/Cod/CodHandler.php` (line 55)

**Usage:**

php

```
add_action('fluent_cart/order_placed_offline', function ($data) {
    $order = $data['order'];
    // Notify warehouse of new COD order
    wp_mail(
        'warehouse@example.com',
        sprintf('New COD Order #%d', $order->id),
        'A new Cash on Delivery order needs to be prepared for shipment.'
    );
}, 10, 1);
```

### ` order_paid_done` [​](https://dev.fluentcart.com/hooks/actions/orders\#order-paid-done)

`fluent_cart/order_paid_done` - Main lifecycle hook when order payment completes (recommended for integrations)

**When it runs:** Fires asynchronously via Action Scheduler after an order's payment is confirmed as `paid`. The `OrderPaid` event enqueues a `fluent_cart/order_paid_ansyc_private_handle` async action, which validates the order is still paid, then dispatches this hook. This is the **recommended hook for third-party integrations** because it runs outside the payment gateway request cycle, avoiding race conditions and timeouts. For subscription or renewal orders, the associated [Subscription](https://dev.fluentcart.com/database/models/subscription.html) model is included in the data.

**Parameters:**

- `$data` (array): Order payment completion data

php

```
$data = [\
      'order'        => $order,        // \FluentCart\App\Models\Order\
      'transaction'  => $transaction,  // \FluentCart\App\Models\OrderTransaction (latest successful transaction)\
      'customer'     => $customer,     // \FluentCart\App\Models\Customer\
      'subscription' => $subscription, // \FluentCart\App\Models\Subscription (only for subscription/renewal orders)\
];
```




> **Note:** The `subscription` key is only present when the order type is `subscription` or `renewal`.


**Source:**`app/Hooks/actions.php` (line 159)

**Usage:**

php

```
add_action('fluent_cart/order_paid_done', function ($data) {
    $order = $data['order'];
    $customer = $data['customer'];

    // Grant membership access after payment
    update_user_meta($customer->user_id, 'membership_active', true);

    // Handle subscription orders differently
    if (!empty($data['subscription'])) {
        $subscription = $data['subscription'];
        update_user_meta($customer->user_id, 'subscription_id', $subscription->id);
    }
}, 10, 1);
```

### ` order_paid_ansyc_private_handle` [​](https://dev.fluentcart.com/hooks/actions/orders\#order-paid-ansyc-private-handle)

`fluent_cart/order_paid_ansyc_private_handle` - Internal async handler that processes post-payment integrations

**When it runs:** Enqueued by `OrderPaid::afterDispatch()` as an Action Scheduler async action. The handler in `app/Hooks/actions.php` validates the order, clears the scheduler meta, and then dispatches `fluent_cart/order_paid_done`. It is also dispatched manually in `IntegrationEventListener` for retry scenarios. **You should generally hook into `order_paid_done` instead of this hook.**

**Parameters:**

- `$data` (array): Order identifier
php

```
$data = [\
      'order_id' => 123, // int: The order ID to process\
];
```


**Source:**`app/Listeners/IntegrationEventListener.php` (line 360), `app/Hooks/actions.php` (line 126)

**Usage:**

php

```
// Not recommended for third-party use. Use fluent_cart/order_paid_done instead.
add_action('fluent_cart/order_paid_ansyc_private_handle', function ($data) {
    $orderId = $data['order_id'];
    // Internal processing only
}, 10, 1);
```

### ` order/receipt_viewed` [​](https://dev.fluentcart.com/hooks/actions/orders\#order-receipt-viewed)

`fluent_cart/order/receipt_viewed` - Fires the first time a customer views their order receipt

**When it runs:** Fires at the end of receipt rendering (both the `ReceiptRenderer` class and the `receipt_slip.php` view template) when the `$is_first_time` flag is true. This means it only fires once per order, the very first time the receipt page is loaded. Subsequent views do not trigger this hook. The data includes both the [Order](https://dev.fluentcart.com/database/models/order.html) and [OrderOperation](https://dev.fluentcart.com/database/models/order-operation.html) models.

**Parameters:**

- `$data` (array): Receipt view data
php

```
$data = [\
      'order'           => $order,           // \FluentCart\App\Models\Order\
      'order_operation' => $order_operation,  // \FluentCart\App\Models\OrderOperation\
];
```


**Source:**`app/Services/Renderer/Receipt/ReceiptRenderer.php` (line 151), `app/Views/invoice/receipt_slip.php` (line 482)

**Usage:**

php

```
add_action('fluent_cart/order/receipt_viewed', function ($data) {
    $order = $data['order'];
    // Track receipt view for analytics
    fluent_cart_add_log(
        'Receipt viewed',
        sprintf('Customer viewed receipt for Order #%d', $order->id),
        'info',
        ['module_name' => 'order', 'module_id' => $order->id]
    );
}, 10, 1);
```

* * *

Was this article helpful?

### Comments

Sign in to comment:

No comments yet. Be the first to share your thoughts!

Today

Hi! I’m your AI assistant. How can I assist you today?

Just now

Powered by **FluentBot**


---

---

