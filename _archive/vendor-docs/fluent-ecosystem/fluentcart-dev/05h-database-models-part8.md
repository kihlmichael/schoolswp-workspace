# FluentCart Developer Docs - Database Models (Part 8/8)

Tous les modèles Eloquent exposés par FluentCart : orders, customers, products, subscriptions, coupons, licenses, taxes, shipping, etc.

---

## Subscription Model | FluentCart Developer Docs

**URL** : https://dev.fluentcart.com/database/models/subscription

[Skip to content](https://dev.fluentcart.com/database/models/subscription#VPContent)

# Subscription Model [​](https://dev.fluentcart.com/database/models/subscription\#subscription-model)

| DB Table Name | {wp\_db\_prefix}\_fct\_subscriptions |
| --- | --- |
| Schema | [Check Schema](https://dev.fluentcart.com/database/schema.html#fct-subscriptions-table) |
| Source File | fluent-cart/app/Models/Subscription.php |
| Name Space | FluentCart\\App\\Models |
| Class | FluentCart\\App\\Models\\Subscription |

## Traits [​](https://dev.fluentcart.com/database/models/subscription\#traits)

| Trait | Provides |
| --- | --- |
| `HasActivity` | `activities()` morphMany relationship to `Activity` model |
| `CanUpdateBatch` | `scopeBatchUpdate` scope for bulk-updating rows in one query |

## Attributes [​](https://dev.fluentcart.com/database/models/subscription\#attributes)

| Attribute | Data Type | Comment |
| --- | --- | --- |
| id | Integer | Primary Key |
| uuid | String | Unique identifier (auto-generated on create via `md5(time() . wp_generate_uuid4())`) |
| customer\_id | Integer | Customer ID |
| parent\_order\_id | Integer | Parent order ID |
| product\_id | Integer | Product ID |
| item\_name | String | Item name |
| variation\_id | Integer | Product variation ID |
| billing\_interval | String | Billing interval (daily, weekly, monthly, quarterly, half\_yearly, yearly) |
| signup\_fee | Integer | Signup fee in cents |
| quantity | Integer | Quantity |
| recurring\_amount | Integer | Recurring amount in cents |
| recurring\_tax\_total | Integer | Recurring tax total in cents |
| recurring\_total | Integer | Recurring total in cents |
| bill\_times | Integer | Number of times to bill (0 = unlimited) |
| bill\_count | Integer | Number of times billed |
| expire\_at | Date Time | Expiration date |
| trial\_ends\_at | Date Time | Trial end date |
| canceled\_at | Date Time | Cancellation date |
| restored\_at | Date Time | Restoration date |
| collection\_method | String | Collection method |
| trial\_days | Integer | Trial days |
| vendor\_customer\_id | String | Vendor customer ID |
| vendor\_plan\_id | String | Vendor plan ID |
| vendor\_subscription\_id | String | Vendor subscription ID |
| next\_billing\_date | Date Time | Next billing date |
| status | String | Subscription status |
| original\_plan | JSON | Original plan data |
| vendor\_response | JSON | Vendor response data |
| current\_payment\_method | String | Current payment method |
| config | JSON | Subscription configuration (auto-encoded/decoded) |
| created\_at | Date Time | Creation timestamp |
| updated\_at | Date Time | Last update timestamp |

## Appended Attributes [​](https://dev.fluentcart.com/database/models/subscription\#appended-attributes)

These virtual attributes are automatically appended when the model is serialized to an array or JSON.

| Attribute | Type | Description |
| --- | --- | --- |
| url | String | Remote subscription URL from payment gateway (via `fluent_cart/subscription/url_{method}` filter) |
| payment\_info | String | Human-readable subscription billing summary (interval, amount, trial) |
| billingInfo | Array | Active payment method details from subscription meta |
| overridden\_status | String | Display-corrected status (handles simulated trial days and actual trial period detection) |
| currency | String | Uppercase currency code (from config or store settings fallback) |
| reactivate\_url | String | Frontend URL for reactivating a canceled/expired subscription |

## Usage [​](https://dev.fluentcart.com/database/models/subscription\#usage)

Please check [Model Basic](https://dev.fluentcart.com/database/models.html) for Common methods.

### Accessing Attributes [​](https://dev.fluentcart.com/database/models/subscription\#accessing-attributes)

php

```
$subscription = FluentCart\App\Models\Subscription::find(1);

$subscription->id; // returns subscription ID
$subscription->status; // returns subscription status
$subscription->recurring_total; // returns recurring total in cents
$subscription->billing_interval; // returns billing interval
$subscription->next_billing_date; // returns next billing date
$subscription->currency; // returns currency code (appended attribute)
$subscription->url; // returns remote subscription URL (appended attribute)
$subscription->overridden_status; // returns display-corrected status (appended attribute)
```

## Scopes [​](https://dev.fluentcart.com/database/models/subscription\#scopes)

### scopeBatchUpdate (via CanUpdateBatch trait) [​](https://dev.fluentcart.com/database/models/subscription\#scopebatchupdate-via-canupdatebatch-trait)

Perform a bulk update of multiple rows in a single query.

- Parameters: `$query` (Builder), `$values` (Array) - Array of row data to update, `$index` (String\|null) - Column to match on (defaults to primary key)

php

```
use FluentCart\App\Models\Subscription;

Subscription::batchUpdate([\
    ['id' => 1, 'status' => 'active'],\
    ['id' => 2, 'status' => 'canceled'],\
]);
```

## Methods [​](https://dev.fluentcart.com/database/models/subscription\#methods)

Along with Global Model methods, this model has the following helper methods.

### getConfigAttribute($value) [​](https://dev.fluentcart.com/database/models/subscription\#getconfigattribute-value)

Get subscription configuration. Automatically decodes JSON strings to arrays.

- Parameters: `$value` (String\|Array\|null) - Raw config value from database
- Returns `Array` \- Decoded configuration array

php

```
$subscription = FluentCart\App\Models\Subscription::find(1);
$config = $subscription->config; // returns configuration array
```

### setConfigAttribute($value) [​](https://dev.fluentcart.com/database/models/subscription\#setconfigattribute-value)

Set subscription configuration. Automatically encodes arrays to JSON.

- Parameters: `$value` (Array\|Mixed) - Configuration array (non-array values default to `[]`)

php

```
$subscription = FluentCart\App\Models\Subscription::find(1);
$subscription->config = ['custom_field' => 'value'];
```

### getUrlAttribute($value) [​](https://dev.fluentcart.com/database/models/subscription\#geturlattribute-value)

Get the remote subscription URL from the payment gateway.

- Parameters: `$value` (String) - URL value
- Returns `String` \- Subscription URL (filtered via `fluent_cart/subscription/url_{payment_method}`)

php

```
$subscription = FluentCart\App\Models\Subscription::find(1);
$url = $subscription->url; // returns subscription URL
```

### getOverriddenStatusAttribute($value) [​](https://dev.fluentcart.com/database/models/subscription\#getoverriddenstatusattribute-value)

Get the display-corrected subscription status. Handles two cases:

1. If trial days were simulated (e.g., via discount/proration) and status is `trialing`, returns `active` instead.
2. If trial days exist but status is `active` and the subscription is still within the trial period, returns `trialing` instead.

- Parameters: `$value` (String) - Status value
- Returns `String` \- Overridden status

php

```
$subscription = FluentCart\App\Models\Subscription::find(1);
$status = $subscription->overridden_status; // returns overridden status
```

### getBillingInfoAttribute($value) [​](https://dev.fluentcart.com/database/models/subscription\#getbillinginfoattribute-value)

Get billing information from the `active_payment_method` subscription meta entry.

- Parameters: `$value` (String) - Billing info value
- Returns `Array` \- Billing information (e.g., card brand, last 4 digits)

php

```
$subscription = FluentCart\App\Models\Subscription::find(1);
$billingInfo = $subscription->billingInfo; // returns billing info array
```

### getCurrencyAttribute() [​](https://dev.fluentcart.com/database/models/subscription\#getcurrencyattribute)

Get subscription currency. Reads from `config.currency` first, falls back to store currency settings.

- Returns `String` \- Uppercase currency code (e.g., `USD`, `EUR`)

php

```
$subscription = FluentCart\App\Models\Subscription::find(1);
$currency = $subscription->currency; // returns currency code
```

### getPaymentInfoAttribute() [​](https://dev.fluentcart.com/database/models/subscription\#getpaymentinfoattribute)

Get a human-readable subscription billing summary string (interval, recurring total, trial days).

- Returns `String` \- Payment information summary

php

```
$subscription = FluentCart\App\Models\Subscription::find(1);
$paymentInfo = $subscription->payment_info; // returns payment info string
```

### getReactivateUrlAttribute() [​](https://dev.fluentcart.com/database/models/subscription\#getreactivateurlattribute)

Get the frontend reactivation URL. Returns empty string if the subscription cannot be reactivated.

- Returns `String` \- Reactivation URL or empty string

php

```
$subscription = FluentCart\App\Models\Subscription::find(1);
$reactivateUrl = $subscription->reactivate_url; // returns reactivation URL
```

### getPaymentMethodText() [​](https://dev.fluentcart.com/database/models/subscription\#getpaymentmethodtext)

Get a formatted payment method display string (e.g., "Visa \*\*\*4242").

- Returns `String` \- Payment method text (brand + last 4 digits), or the method name if card details are unavailable

php

```
$subscription = FluentCart\App\Models\Subscription::find(1);
$paymentMethodText = $subscription->getPaymentMethodText();
```

### getMeta($metaKey, $default = null) [​](https://dev.fluentcart.com/database/models/subscription\#getmeta-metakey-default-null)

Get a subscription meta value by key from the `fct_subscription_meta` table.

- Parameters: `$metaKey` (String) - Meta key, `$default` (Mixed) - Default value if not found
- Returns `Mixed` \- Meta value or default

php

```
$subscription = FluentCart\App\Models\Subscription::find(1);
$metaValue = $subscription->getMeta('custom_field', 'default');
```

### updateMeta($metaKey, $metaValue) [​](https://dev.fluentcart.com/database/models/subscription\#updatemeta-metakey-metavalue)

Create or update a subscription meta entry. If the key already exists, it updates the value; otherwise, it creates a new row.

- Parameters: `$metaKey` (String) - Meta key, `$metaValue` (Mixed) - Meta value
- Returns `Boolean` \- Always returns true

php

```
$subscription = FluentCart\App\Models\Subscription::find(1);
$subscription->updateMeta('custom_field', 'new_value');
```

### addLog($title, $description = '', $type = 'info', $by = '') [​](https://dev.fluentcart.com/database/models/subscription\#addlog-title-description-type-info-by)

Add an activity log entry for this subscription.

- Parameters:
  - `$title` (String) - Log title
  - `$description` (String) - Log description (default: `''`)
  - `$type` (String) - Log type, e.g., `info`, `error` (default: `'info'`)
  - `$by` (String) - Created-by identifier (default: `''`)

php

```
$subscription = FluentCart\App\Models\Subscription::find(1);
$subscription->addLog('Status Changed', 'Subscription activated', 'info');
$subscription->addLog('Payment Failed', 'Card declined', 'error', 'system');
```

### getDownloads() [​](https://dev.fluentcart.com/database/models/subscription\#getdownloads)

Get downloadable files associated with this subscription's product. Only returns downloads when the subscription has a `variation_id` and status is `active`. Filters downloads by the subscription's variation ID.

- Returns `Collection|Array` \- Collection of `ProductDownload` models with product and variation titles, or empty array

php

```
$subscription = FluentCart\App\Models\Subscription::find(1);
$downloads = $subscription->getDownloads();
```

### getLatestTransaction() [​](https://dev.fluentcart.com/database/models/subscription\#getlatesttransaction)

Get the most recent charge transaction for this subscription.

- Returns `FluentCart\App\Models\OrderTransaction|null` \- Latest charge transaction or null

php

```
$subscription = FluentCart\App\Models\Subscription::find(1);
$transaction = $subscription->getLatestTransaction();
```

### canUpgrade() [​](https://dev.fluentcart.com/database/models/subscription\#canupgrade)

Check if the subscription can be upgraded. Requires a `variant_upgrade_path` meta entry for the current variation and the subscription must be `active` or `trialing`.

- Returns `Boolean` \- True if upgrade path exists and status allows it

php

```
$subscription = FluentCart\App\Models\Subscription::find(1);
$canUpgrade = $subscription->canUpgrade();
```

### canUpdatePaymentMethod() [​](https://dev.fluentcart.com/database/models/subscription\#canupdatepaymentmethod)

Check if the payment method can be updated (card update). The current payment gateway must support the `card_update` feature and the subscription must be in one of the allowed statuses: `active`, `trialing`, `paused`, `intended`, `past_due`, `failing`, or `expiring`.

- Returns `Boolean` \- True if payment method can be updated

php

```
$subscription = FluentCart\App\Models\Subscription::find(1);
$canUpdate = $subscription->canUpdatePaymentMethod();
```

### canSwitchPaymentMethod() [​](https://dev.fluentcart.com/database/models/subscription\#canswitchpaymentmethod)

Check if the payment method can be switched to a different gateway entirely. The current gateway must support the `switch_payment_method` feature, and the subscription must be `active`, `trialing`, or `paused`.

- Returns `Boolean` \- True if payment method can be switched

php

```
$subscription = FluentCart\App\Models\Subscription::find(1);
$canSwitch = $subscription->canSwitchPaymentMethod();
```

### switchablePaymentMethods() [​](https://dev.fluentcart.com/database/models/subscription\#switchablepaymentmethods)

Get the list of payment gateways that can be switched to from the current gateway.

- Returns `Array` \- Array of supported gateway identifiers, or empty array if switching is not supported

php

```
$subscription = FluentCart\App\Models\Subscription::find(1);
$methods = $subscription->switchablePaymentMethods();
// e.g., ['stripe', 'paypal']
```

### canReactive() [​](https://dev.fluentcart.com/database/models/subscription\#canreactive)

Check if the subscription can be reactivated. Returns empty string (falsy) if:

- FluentCart Pro is not active
- The subscription was upgraded to another subscription
- The recurring amount is zero or negative
- The cancellation reason is `refunded`

Otherwise checks if status is one of: `canceled`, `failing`, `expired`, `paused`, `expiring`, or `past_due`.

- Returns `Mixed` \- Filtered boolean/string value (empty string if cannot reactivate, truthy if can). Result is filtered via `fluent_cart/subscription/can_reactivate`.

php

```
$subscription = FluentCart\App\Models\Subscription::find(1);
if ($subscription->canReactive()) {
    // subscription can be reactivated
}
```

### getReactivateUrl() [​](https://dev.fluentcart.com/database/models/subscription\#getreactivateurl)

Get the frontend URL for reactivating a canceled or expired subscription. Returns empty string if the subscription cannot be reactivated.

- Returns `String` \- Reactivation URL with `fluent-cart=reactivate-subscription` query parameter, or empty string

php

```
$subscription = FluentCart\App\Models\Subscription::find(1);
$reactivateUrl = $subscription->getReactivateUrl();
```

### getViewUrl($type = 'customer') [​](https://dev.fluentcart.com/database/models/subscription\#getviewurl-type-customer)

Get the subscription view URL for the customer portal or admin dashboard.

- Parameters: `$type` (String) - View type: `'customer'` (default) for the customer portal, or `'admin'` for the admin dashboard
- Returns `String` \- View URL

php

```
$subscription = FluentCart\App\Models\Subscription::find(1);
$customerUrl = $subscription->getViewUrl(); // customer portal URL
$adminUrl = $subscription->getViewUrl('admin'); // admin dashboard URL
```

### hasAccessValidity() [​](https://dev.fluentcart.com/database/models/subscription\#hasaccessvalidity)

Check if the subscription currently grants access. Returns true for `active`, `trialing`, and `completed` statuses. Returns false for `expired`, `past_due`, `intended`, and `pending`. For other statuses (e.g., `canceled`, `failing`, `paused`, `expiring`), checks whether the next billing date (or guessed billing date) is still in the future.

- Returns `Boolean` \- True if the subscription has valid access

php

```
$subscription = FluentCart\App\Models\Subscription::find(1);
$hasAccess = $subscription->hasAccessValidity();
```

### reSyncFromRemote() [​](https://dev.fluentcart.com/database/models/subscription\#resyncfromremote)

Re-sync subscription data from the remote payment gateway. The gateway must support the `subscriptions` feature.

- Returns `Mixed` \- Sync result from the gateway, or `WP_Error` if the payment method does not support remote resync

php

```
$subscription = FluentCart\App\Models\Subscription::find(1);
$result = $subscription->reSyncFromRemote();
if (is_wp_error($result)) {
    // handle error
}
```

### cancelRemoteSubscription($args = \[\]) [​](https://dev.fluentcart.com/database/models/subscription\#cancelremotesubscription-args)

Cancel the subscription both remotely (at the payment gateway) and locally. Updates the status to `canceled`, sets `canceled_at`, stores the cancellation reason in config, and dispatches the `SubscriptionCanceled` event.

- Parameters: `$args` (Array) - Cancellation arguments:
  - `reason` (String) - Cancellation reason (stored in config, default: `''`)
  - `fire_hooks` (Boolean) - Whether to dispatch the `SubscriptionCanceled` event (default: `true`)
  - `note` (String) - Cancellation note (saved to order, default: `''`)
- Returns `Array|WP_Error` \- Array with `subscription` and `vendor_result` keys on success

php

```
$subscription = FluentCart\App\Models\Subscription::find(1);
$result = $subscription->cancelRemoteSubscription([\
    'reason'     => 'Customer request',\
    'fire_hooks' => true,\
    'note'       => 'Cancelled by customer'\
]);
```

### getCurrentRenewalAmount() [​](https://dev.fluentcart.com/database/models/subscription\#getcurrentrenewalamount)

Get the current renewal amount. Checks `config.current_renewal_amount` first (used when the renewal amount differs from the base recurring total, e.g., after a plan change), then falls back to `recurring_total`.

- Returns `Integer` \- Current renewal amount in cents

php

```
$subscription = FluentCart\App\Models\Subscription::find(1);
$amount = $subscription->getCurrentRenewalAmount();
```

### getRequiredBillTimes() [​](https://dev.fluentcart.com/database/models/subscription\#getrequiredbilltimes)

Get the number of remaining billing cycles. If `bill_times` is 0, returns 0 (unlimited). If the calculated remaining count is zero or negative, it re-verifies against actual successful transactions and early payment history, correcting `bill_count` if needed. Returns -1 if billing is truly complete after verification.

- Returns `Integer` \- Remaining bill times (0 = unlimited, -1 = completed)

php

```
$subscription = FluentCart\App\Models\Subscription::find(1);
$billTimes = $subscription->getRequiredBillTimes();
```

### getReactivationTrialDays() [​](https://dev.fluentcart.com/database/models/subscription\#getreactivationtrialdays)

Get the number of trial days to apply when reactivating this subscription. If the subscription still has valid access (i.e., the billing period has not fully elapsed), the remaining days are returned as trial days so the customer is not double-charged.

- Returns `Integer` \- Number of trial days for reactivation (0 if no remaining validity)

php

```
$subscription = FluentCart\App\Models\Subscription::find(1);
$trialDays = $subscription->getReactivationTrialDays();
```

### guessNextBillingDate($forced = false) [​](https://dev.fluentcart.com/database/models/subscription\#guessnextbillingdate-forced-false)

Calculate the next billing date when it is not already set (or when forced). Uses the last successful order's creation date plus the billing interval. For initial orders with trial days, adds trial days instead.

- Parameters: `$forced` (Boolean) - Force recalculation even if `next_billing_date` is already set (default: `false`)
- Returns `String` \- Next billing date in `Y-m-d H:i:s` GMT format

php

```
$subscription = FluentCart\App\Models\Subscription::find(1);
$nextBillingDate = $subscription->guessNextBillingDate();
$forcedDate = $subscription->guessNextBillingDate(true); // force recalculation
```

### checkAndExpireSubscriptions($batchSize = 100) (static) [​](https://dev.fluentcart.com/database/models/subscription\#checkandexpiresubscriptions-batchsize-100-static)

Check and expire subscriptions that have missed payments beyond their grace period. Called by the hourly scheduler. Processes `active`, `trialing`, and `canceled` subscriptions whose `next_billing_date` is past the grace period threshold. Grace periods vary by billing interval (e.g., 1 day for daily, 3 for weekly, 7 for monthly, 15 for quarterly/half\_yearly/yearly).

For active/trialing subscriptions, status is changed to `expired`. For canceled subscriptions, only `next_billing_date` is cleared (status remains canceled). Dispatches `SubscriptionValidityExpired` event for each affected subscription.

- Parameters: `$batchSize` (Integer) - Number of subscriptions to process per batch (default: `100`)
- Returns `Array` \- Statistics with keys: `checked`, `validity_expired`, `batches`

php

```
use FluentCart\App\Models\Subscription;

$stats = Subscription::checkAndExpireSubscriptions(50);
// $stats = ['checked' => 200, 'validity_expired' => 5, 'batches' => 4]
```

## Relations [​](https://dev.fluentcart.com/database/models/subscription\#relations)

This model has the following relationships that you can use.

### meta [​](https://dev.fluentcart.com/database/models/subscription\#meta)

Access the subscription metadata.

- Relation type: `HasMany`
- Returns `Collection` of `FluentCart\App\Models\SubscriptionMeta`

php

```
$subscription = FluentCart\App\Models\Subscription::find(1);
$meta = $subscription->meta;
```

### customer [​](https://dev.fluentcart.com/database/models/subscription\#customer)

Access the customer.

- Relation type: `BelongsTo`
- Foreign key: `customer_id`
- Returns `FluentCart\App\Models\Customer`

php

```
$subscription = FluentCart\App\Models\Subscription::find(1);
$customer = $subscription->customer;
```

### product [​](https://dev.fluentcart.com/database/models/subscription\#product)

Access the product.

- Relation type: `BelongsTo`
- Foreign key: `product_id` -\> `ID`
- Returns `FluentCart\App\Models\Product`

php

```
$subscription = FluentCart\App\Models\Subscription::find(1);
$product = $subscription->product;
```

### variation [​](https://dev.fluentcart.com/database/models/subscription\#variation)

Access the product variation.

- Relation type: `BelongsTo`
- Foreign key: `variation_id`
- Returns `FluentCart\App\Models\ProductVariation`

php

```
$subscription = FluentCart\App\Models\Subscription::find(1);
$variation = $subscription->variation;
```

### labels [​](https://dev.fluentcart.com/database/models/subscription\#labels)

Access the subscription labels.

- Relation type: `MorphMany`
- Returns `Collection` of `FluentCart\App\Models\LabelRelationship`

php

```
$subscription = FluentCart\App\Models\Subscription::find(1);
$labels = $subscription->labels;
```

### license [​](https://dev.fluentcart.com/database/models/subscription\#license)

Access the subscription license (single). Only available when FluentCart Pro with the Licensing module is active.

- Relation type: `HasOne` (nullable -- returns `null` if `License` class does not exist)
- Returns `FluentCartPro\App\Modules\Licensing\Models\License|null`

php

```
$subscription = FluentCart\App\Models\Subscription::find(1);
$license = $subscription->license;
```

### licenses [​](https://dev.fluentcart.com/database/models/subscription\#licenses)

Access all subscription licenses. Only available when FluentCart Pro with the Licensing module is active.

- Relation type: `HasMany` (nullable -- returns `null` if `License` class does not exist)
- Returns `Collection` of `FluentCartPro\App\Modules\Licensing\Models\License|null`

php

```
$subscription = FluentCart\App\Models\Subscription::find(1);
$licenses = $subscription->licenses;
```

### transactions [​](https://dev.fluentcart.com/database/models/subscription\#transactions)

Access the subscription transactions.

- Relation type: `HasMany`
- Returns `Collection` of `FluentCart\App\Models\OrderTransaction`

php

```
$subscription = FluentCart\App\Models\Subscription::find(1);
$transactions = $subscription->transactions;
```

### billing\_addresses [​](https://dev.fluentcart.com/database/models/subscription\#billing-addresses)

Access the billing addresses for the subscription's customer.

- Relation type: `HasMany` (scoped to `type = 'billing'`)
- Foreign key: `customer_id` -\> `customer_id`
- Returns `Collection` of `FluentCart\App\Models\CustomerAddresses`

php

```
$subscription = FluentCart\App\Models\Subscription::find(1);
$addresses = $subscription->billing_addresses;
```

### product\_detail [​](https://dev.fluentcart.com/database/models/subscription\#product-detail)

Access the product detail (variation details).

- Relation type: `BelongsTo`
- Foreign key: `variation_id` -\> `id`
- Returns `FluentCart\App\Models\ProductDetail`

php

```
$subscription = FluentCart\App\Models\Subscription::find(1);
$productDetail = $subscription->product_detail;
```

### order [​](https://dev.fluentcart.com/database/models/subscription\#order)

Access the parent order.

- Relation type: `BelongsTo`
- Foreign key: `parent_order_id` -\> `id`
- Returns `FluentCart\App\Models\Order`

php

```
$subscription = FluentCart\App\Models\Subscription::find(1);
$order = $subscription->order;
```

### activities (via HasActivity trait) [​](https://dev.fluentcart.com/database/models/subscription\#activities-via-hasactivity-trait)

Access the activity logs for this subscription.

- Relation type: `MorphMany` (ordered by `created_at DESC`, `id DESC`)
- Returns `Collection` of `FluentCart\App\Models\Activity`

php

```
$subscription = FluentCart\App\Models\Subscription::find(1);
$activities = $subscription->activities;
```

## Usage Examples [​](https://dev.fluentcart.com/database/models/subscription\#usage-examples)

### Creating a Subscription [​](https://dev.fluentcart.com/database/models/subscription\#creating-a-subscription)

php

```
use FluentCart\App\Models\Subscription;

$subscription = Subscription::create([\
    'customer_id' => 1,\
    'parent_order_id' => 1,\
    'product_id' => 1,\
    'variation_id' => 1,\
    'billing_interval' => 'monthly',\
    'recurring_total' => 2999, // $29.99 in cents\
    'status' => 'active'\
]);
// uuid is auto-generated on create
```

### Retrieving Subscriptions [​](https://dev.fluentcart.com/database/models/subscription\#retrieving-subscriptions)

php

```
// Get subscription by ID
$subscription = Subscription::find(1);

// Get subscription with customer and product
$subscription = Subscription::with(['customer', 'product'])->find(1);

// Get active subscriptions
$subscriptions = Subscription::where('status', 'active')->get();
```

### Updating a Subscription [​](https://dev.fluentcart.com/database/models/subscription\#updating-a-subscription)

php

```
$subscription = Subscription::find(1);
$subscription->status = 'cancelled';
$subscription->canceled_at = gmdate('Y-m-d H:i:s');
$subscription->save();
```

### Deleting a Subscription [​](https://dev.fluentcart.com/database/models/subscription\#deleting-a-subscription)

php

```
$subscription = Subscription::find(1);
$subscription->delete();
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

## Subscription Meta Model | FluentCart Developer Docs

**URL** : https://dev.fluentcart.com/database/models/subscription-meta

[Skip to content](https://dev.fluentcart.com/database/models/subscription-meta#VPContent)

# Subscription Meta Model [​](https://dev.fluentcart.com/database/models/subscription-meta\#subscription-meta-model)

| DB Table Name | {wp\_db\_prefix}\_fct\_subscription\_meta |
| --- | --- |
| Schema | [Check Schema](https://dev.fluentcart.com/database/schema.html#fct-subscription-meta-table) |
| Source File | fluent-cart/app/Models/SubscriptionMeta.php |
| Name Space | FluentCart\\App\\Models |
| Class | FluentCart\\App\\Models\\SubscriptionMeta |

## Attributes [​](https://dev.fluentcart.com/database/models/subscription-meta\#attributes)

| Attribute | Data Type | Comment |
| --- | --- | --- |
| id | Integer | Primary Key |
| subscription\_id | Integer | Reference to subscription |
| meta\_key | String | Meta key name |
| meta\_value | Text | Meta value (JSON encoded for arrays/objects, auto-encoded/decoded via mutator/accessor) |
| created\_at | Date Time | Creation timestamp |
| updated\_at | Date Time | Last update timestamp |

## Usage [​](https://dev.fluentcart.com/database/models/subscription-meta\#usage)

Please check [Model Basic](https://dev.fluentcart.com/database/models.html) for Common methods.

### Accessing Attributes [​](https://dev.fluentcart.com/database/models/subscription-meta\#accessing-attributes)

php

```
$subscriptionMeta = FluentCart\App\Models\SubscriptionMeta::find(1);

$subscriptionMeta->id; // returns id
$subscriptionMeta->subscription_id; // returns subscription ID
$subscriptionMeta->meta_key; // returns meta key
$subscriptionMeta->meta_value; // returns meta value (auto-decoded if JSON)
```

## Relations [​](https://dev.fluentcart.com/database/models/subscription-meta\#relations)

This model has the following relationships that you can use

### product\_detail [​](https://dev.fluentcart.com/database/models/subscription-meta\#product-detail)

Access the associated subscription (BelongsTo via `subscription_id` -\> `id`).

Note

Despite the name `product_detail`, this relationship returns a `Subscription` model, not a `Product` model. This is a legacy naming convention.

- return `FluentCart\App\Models\Subscription` Model (BelongsTo)

#### Example: [​](https://dev.fluentcart.com/database/models/subscription-meta\#example)

php

```
// Accessing Subscription
$subscription = $subscriptionMeta->product_detail;

// For Filtering by subscription relationship
$subscriptionMetas = FluentCart\App\Models\SubscriptionMeta::whereHas('product_detail', function($query) {
    $query->where('status', 'active');
})->get();
```

## Methods [​](https://dev.fluentcart.com/database/models/subscription-meta\#methods)

Along with Global Model methods, this model has few helper methods.

### setMetaValueAttribute($value) [​](https://dev.fluentcart.com/database/models/subscription-meta\#setmetavalueattribute-value)

Set meta value with automatic JSON encoding (mutator). Arrays and objects are encoded with `JSON_UNESCAPED_UNICODE | JSON_UNESCAPED_SLASHES` flags.

- Parameters
  - `$value` \- mixed (array, object, or string)
- Returns `void`

#### Usage [​](https://dev.fluentcart.com/database/models/subscription-meta\#usage-1)

php

```
$subscriptionMeta->meta_value = ['custom_data' => 'value', 'settings' => ['key' => 'value']];
// Automatically JSON encodes arrays and objects
```

### getMetaValueAttribute($value) [​](https://dev.fluentcart.com/database/models/subscription-meta\#getmetavalueattribute-value)

Get meta value with automatic JSON decoding (accessor). If the stored string is valid JSON, it returns the decoded array. Otherwise, returns the raw string value.

- Parameters
  - `$value` \- mixed
- Returns `mixed` (decoded array if valid JSON, otherwise original value)

#### Usage [​](https://dev.fluentcart.com/database/models/subscription-meta\#usage-2)

php

```
$metaValue = $subscriptionMeta->meta_value; // Returns decoded value (array, object, or string)
```

## Usage Examples [​](https://dev.fluentcart.com/database/models/subscription-meta\#usage-examples)

### Get Subscription Meta [​](https://dev.fluentcart.com/database/models/subscription-meta\#get-subscription-meta)

php

```
$subscription = FluentCart\App\Models\Subscription::find(123);
$meta = $subscription->subscription_meta;

foreach ($meta as $metaItem) {
    echo "Key: " . $metaItem->meta_key;
    echo "Value: " . print_r($metaItem->meta_value, true);
}
```

### Create Subscription Meta [​](https://dev.fluentcart.com/database/models/subscription-meta\#create-subscription-meta)

php

```
$subscriptionMeta = FluentCart\App\Models\SubscriptionMeta::create([\
    'subscription_id' => 123,\
    'meta_key' => 'custom_field',\
    'meta_value' => 'custom_value'\
]);
```

### Store Complex Subscription Data [​](https://dev.fluentcart.com/database/models/subscription-meta\#store-complex-subscription-data)

php

```
$subscriptionMeta = FluentCart\App\Models\SubscriptionMeta::create([\
    'subscription_id' => 123,\
    'meta_key' => 'subscription_settings',\
    'meta_value' => [\
        'auto_renew' => true,\
        'payment_reminder_days' => 7,\
        'grace_period_days' => 3,\
        'notifications' => ['email' => true, 'sms' => false]\
    ]\
]);
```

### Get Meta by Key [​](https://dev.fluentcart.com/database/models/subscription-meta\#get-meta-by-key)

php

```
$meta = FluentCart\App\Models\SubscriptionMeta::where('subscription_id', 123)
    ->where('meta_key', 'subscription_settings')
    ->first();

if ($meta) {
    echo "Settings: " . print_r($meta->meta_value, true);
}
```

### Update Meta Value [​](https://dev.fluentcart.com/database/models/subscription-meta\#update-meta-value)

php

```
$meta = FluentCart\App\Models\SubscriptionMeta::find(1);
$meta->meta_value = ['updated' => true, 'timestamp' => now()];
$meta->save();
```

### Get All Meta for Subscription [​](https://dev.fluentcart.com/database/models/subscription-meta\#get-all-meta-for-subscription)

php

```
$subscriptionMetas = FluentCart\App\Models\SubscriptionMeta::where('subscription_id', 123)->get();
```

### Get Subscription Settings [​](https://dev.fluentcart.com/database/models/subscription-meta\#get-subscription-settings)

php

```
$settings = FluentCart\App\Models\SubscriptionMeta::where('subscription_id', 123)
    ->where('meta_key', 'subscription_settings')
    ->first();

if ($settings) {
    $autoRenew = $settings->meta_value['auto_renew'] ?? false;
    $gracePeriod = $settings->meta_value['grace_period_days'] ?? 0;
}
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

## Tax Class Model | FluentCart Developer Docs

**URL** : https://dev.fluentcart.com/database/models/tax-class

[Skip to content](https://dev.fluentcart.com/database/models/tax-class#VPContent)

# Tax Class Model [​](https://dev.fluentcart.com/database/models/tax-class\#tax-class-model)

| DB Table Name | {wp\_db\_prefix}\_fct\_tax\_classes |
| --- | --- |
| Schema | [Check Schema](https://dev.fluentcart.com/database/schema.html#fct-tax-classes-table) |
| Source File | fluent-cart/app/Models/TaxClass.php |
| Name Space | FluentCart\\App\\Models |
| Class | FluentCart\\App\\Models\\TaxClass |

## Guarded & Fillable [​](https://dev.fluentcart.com/database/models/tax-class\#guarded-fillable)

This model uses both `$guarded` and `$fillable`:

- **Guarded:**`['id']`
- **Fillable:**`['title', 'description', 'meta', 'slug']`

## Lifecycle Hooks (booted) [​](https://dev.fluentcart.com/database/models/tax-class\#lifecycle-hooks-booted)

The model registers lifecycle hooks in the `booted()` method:

- **Creating:** Automatically generates a unique slug from `title` via `generateUniqueSlug()`.
- **Updating:** If `title` has changed (is dirty), the slug is regenerated to match the new title.

## Attributes [​](https://dev.fluentcart.com/database/models/tax-class\#attributes)

| Attribute | Data Type | Comment |
| --- | --- | --- |
| id | Integer | Primary Key (guarded) |
| title | String | Tax class title |
| description | Text | Tax class description |
| meta | JSON | Additional metadata (manual JSON mutator/accessor) |
| slug | String | URL-friendly slug (auto-generated from title) |
| created\_at | Date Time | Creation timestamp |
| updated\_at | Date Time | Last update timestamp |

## Usage [​](https://dev.fluentcart.com/database/models/tax-class\#usage)

Please check [Model Basic](https://dev.fluentcart.com/database/models.html) for Common methods.

### Accessing Attributes [​](https://dev.fluentcart.com/database/models/tax-class\#accessing-attributes)

php

```
$taxClass = FluentCart\App\Models\TaxClass::find(1);

$taxClass->id; // returns id
$taxClass->title; // returns title
$taxClass->description; // returns description
$taxClass->slug; // returns slug
$taxClass->meta; // returns array (accessor)
```

## Methods [​](https://dev.fluentcart.com/database/models/tax-class\#methods)

Along with Global Model methods, this model has few helper methods.

### setMetaAttribute($value) [​](https://dev.fluentcart.com/database/models/tax-class\#setmetaattribute-value)

Set meta with automatic JSON encoding (mutator). Encodes the value with `json_encode()`. Falls back to `'[]'` if encoding fails or value is falsy.

- Parameters
  - $value - mixed (array, object, or string)
- Returns `void`

#### Usage [​](https://dev.fluentcart.com/database/models/tax-class\#usage-1)

php

```
$taxClass->meta = ['tax_rate' => 8.5, 'exempt_products' => [1, 2, 3]];
// Automatically JSON encodes arrays and objects
```

### getMetaAttribute($value) [​](https://dev.fluentcart.com/database/models/tax-class\#getmetaattribute-value)

Get meta with automatic JSON decoding (accessor). Decodes the stored JSON string into an associative array.

- Parameters
  - $value - mixed
- Returns `array` \- Decoded array, or empty array if value is falsy

#### Usage [​](https://dev.fluentcart.com/database/models/tax-class\#usage-2)

php

```
$meta = $taxClass->meta; // Returns decoded array
```

### generateUniqueSlug($title, $ignoreId = null) [​](https://dev.fluentcart.com/database/models/tax-class\#generateuniqueslug-title-ignoreid-null)

Generate unique slug for tax class (protected static method). Uses `Str::slug()` to create a URL-friendly slug from the title, then appends a numeric suffix if the slug already exists. Falls back to `'tax-class'` as the base slug if `Str::slug()` returns empty.

This method is called automatically by the model's lifecycle hooks -- you typically do not need to call it directly.

- Parameters
  - $title - string
  - $ignoreId - integer\|null (default: null) - Exclude this ID when checking for uniqueness (used during updates)
- Returns `string`

Note

This method is `protected static`, so it is not callable from outside the model class. Slug generation happens automatically on create and on update (when the title changes).

## Usage Examples [​](https://dev.fluentcart.com/database/models/tax-class\#usage-examples)

### Get Tax Classes [​](https://dev.fluentcart.com/database/models/tax-class\#get-tax-classes)

php

```
$taxClass = FluentCart\App\Models\TaxClass::find(1);
echo "Title: " . $taxClass->title;
echo "Description: " . $taxClass->description;
echo "Slug: " . $taxClass->slug;
```

### Create Tax Class [​](https://dev.fluentcart.com/database/models/tax-class\#create-tax-class)

php

```
$taxClass = FluentCart\App\Models\TaxClass::create([\
    'title' => 'Standard Tax',\
    'description' => 'Standard tax rate for most products',\
    'meta' => [\
        'tax_rate' => 8.5,\
        'exempt_products' => [],\
        'applicable_regions' => ['US', 'CA']\
    ]\
]);
// Slug will be automatically generated as "standard-tax"
```

### Get All Tax Classes [​](https://dev.fluentcart.com/database/models/tax-class\#get-all-tax-classes)

php

```
$taxClasses = FluentCart\App\Models\TaxClass::all();

foreach ($taxClasses as $class) {
    echo "Class: " . $class->title . " (" . $class->slug . ")";
}
```

### Get Tax Class by Slug [​](https://dev.fluentcart.com/database/models/tax-class\#get-tax-class-by-slug)

php

```
$taxClass = FluentCart\App\Models\TaxClass::where('slug', 'standard-tax')->first();
```

### Update Tax Class [​](https://dev.fluentcart.com/database/models/tax-class\#update-tax-class)

php

```
$taxClass = FluentCart\App\Models\TaxClass::find(1);
$taxClass->update([\
    'title' => 'Updated Tax Class',\
    'description' => 'Updated description',\
    'meta' => ['tax_rate' => 9.0, 'updated' => true]\
]);
// Slug will be automatically updated if title changes
```

### Get Tax Classes with Meta [​](https://dev.fluentcart.com/database/models/tax-class\#get-tax-classes-with-meta)

php

```
$taxClasses = FluentCart\App\Models\TaxClass::all();

foreach ($taxClasses as $class) {
    $meta = $class->meta;
    if (isset($meta['tax_rate'])) {
        echo "Class: " . $class->title . " - Rate: " . $meta['tax_rate'] . "%";
    }
}
```

### Search Tax Classes [​](https://dev.fluentcart.com/database/models/tax-class\#search-tax-classes)

php

```
$searchResults = FluentCart\App\Models\TaxClass::where('title', 'like', '%Standard%')->get();
```

### Delete Tax Class [​](https://dev.fluentcart.com/database/models/tax-class\#delete-tax-class)

php

```
$taxClass = FluentCart\App\Models\TaxClass::find(1);
$taxClass->delete();
```

### Get Tax Classes Ordered by Title [​](https://dev.fluentcart.com/database/models/tax-class\#get-tax-classes-ordered-by-title)

php

```
$orderedClasses = FluentCart\App\Models\TaxClass::orderBy('title', 'asc')->get();
```

### Automatic Slug Generation [​](https://dev.fluentcart.com/database/models/tax-class\#automatic-slug-generation)

php

```
// Creating a class with a duplicate title auto-generates a unique slug
$taxClass1 = FluentCart\App\Models\TaxClass::create(['title' => 'Sales Tax']);
// slug: "sales-tax"

$taxClass2 = FluentCart\App\Models\TaxClass::create(['title' => 'Sales Tax']);
// slug: "sales-tax-2"
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

## Tax Rate Model | FluentCart Developer Docs

**URL** : https://dev.fluentcart.com/database/models/tax-rate

[Skip to content](https://dev.fluentcart.com/database/models/tax-rate#VPContent)

# Tax Rate Model [​](https://dev.fluentcart.com/database/models/tax-rate\#tax-rate-model)

| DB Table Name | {wp\_db\_prefix}\_fct\_tax\_rates |
| --- | --- |
| Schema | [Check Schema](https://dev.fluentcart.com/database/schema.html#fct-tax-rates-table) |
| Source File | fluent-cart/app/Models/TaxRate.php |
| Name Space | FluentCart\\App\\Models |
| Class | FluentCart\\App\\Models\\TaxRate |

## Guarded & Fillable [​](https://dev.fluentcart.com/database/models/tax-rate\#guarded-fillable)

This model uses both `$guarded` and `$fillable`:

- **Guarded:**`['id']`
- **Fillable:**`['class_id', 'country', 'state', 'postcode', 'city', 'rate', 'name', 'group', 'priority', 'is_compound', 'for_shipping', 'for_order']`

## Timestamps [​](https://dev.fluentcart.com/database/models/tax-rate\#timestamps)

This model has **timestamps disabled** (`$timestamps = false`). The `created_at` and `updated_at` columns are not automatically managed.

## Appended Attributes [​](https://dev.fluentcart.com/database/models/tax-rate\#appended-attributes)

The following computed attributes are automatically appended to the model's array/JSON output:

- `formatted_state` \- Human-readable state name

## Attributes [​](https://dev.fluentcart.com/database/models/tax-rate\#attributes)

| Attribute | Data Type | Comment |
| --- | --- | --- |
| id | Integer | Primary Key (guarded) |
| class\_id | Integer | Reference to tax class |
| country | String | Country code |
| state | String | State/Province code |
| postcode | String | Postal/ZIP code |
| city | String | City name |
| rate | Decimal | Tax rate percentage |
| name | String | Tax rate name |
| group | String | Tax group |
| priority | Integer | Priority order |
| is\_compound | Boolean | Whether tax is compound |
| for\_shipping | Boolean | Whether tax applies to shipping |
| for\_order | Boolean | Whether tax applies to order |

No Timestamps

This model does not use automatic timestamps. There are no `created_at` or `updated_at` columns managed by the ORM.

## Usage [​](https://dev.fluentcart.com/database/models/tax-rate\#usage)

Please check [Model Basic](https://dev.fluentcart.com/database/models.html) for Common methods.

### Accessing Attributes [​](https://dev.fluentcart.com/database/models/tax-rate\#accessing-attributes)

php

```
$taxRate = FluentCart\App\Models\TaxRate::find(1);

$taxRate->id; // returns id
$taxRate->class_id; // returns class ID
$taxRate->country; // returns country code
$taxRate->state; // returns state code
$taxRate->rate; // returns tax rate
$taxRate->formatted_state; // returns formatted state name (appended attribute)
```

## Relations [​](https://dev.fluentcart.com/database/models/tax-rate\#relations)

This model has the following relationships that you can use

### tax\_class [​](https://dev.fluentcart.com/database/models/tax-rate\#tax-class)

Access the associated tax class

- return `FluentCart\App\Models\TaxClass` Model

#### Example: [​](https://dev.fluentcart.com/database/models/tax-rate\#example)

php

```
// Accessing Tax Class
$taxClass = $taxRate->tax_class;

// For Filtering by tax class relationship
$taxRates = FluentCart\App\Models\TaxRate::whereHas('tax_class', function($query) {
    $query->where('title', 'Standard Tax');
})->get();
```

## Methods [​](https://dev.fluentcart.com/database/models/tax-rate\#methods)

Along with Global Model methods, this model has few helper methods.

### getFormattedStateAttribute() [​](https://dev.fluentcart.com/database/models/tax-rate\#getformattedstateattribute)

Get formatted state name (accessor). Resolves the state code to its human-readable name using `AddressHelper::getStateNameByCode()`, using the model's `country` attribute for context.

- Parameters
  - none
- Returns `string` \- Formatted state name, or empty string if state is empty

#### Usage [​](https://dev.fluentcart.com/database/models/tax-rate\#usage-1)

php

```
$formattedState = $taxRate->formatted_state; // e.g., "California"
```

## Usage Examples [​](https://dev.fluentcart.com/database/models/tax-rate\#usage-examples)

### Get Tax Rates [​](https://dev.fluentcart.com/database/models/tax-rate\#get-tax-rates)

php

```
$taxRate = FluentCart\App\Models\TaxRate::find(1);
echo "Name: " . $taxRate->name;
echo "Rate: " . $taxRate->rate . "%";
echo "Country: " . $taxRate->country;
echo "State: " . $taxRate->state;
echo "Formatted State: " . $taxRate->formatted_state;
```

### Create Tax Rate [​](https://dev.fluentcart.com/database/models/tax-rate\#create-tax-rate)

php

```
$taxRate = FluentCart\App\Models\TaxRate::create([\
    'class_id' => 1,\
    'country' => 'US',\
    'state' => 'CA',\
    'postcode' => '90210',\
    'city' => 'Beverly Hills',\
    'rate' => 8.75,\
    'name' => 'California Sales Tax',\
    'group' => 'sales_tax',\
    'priority' => 1,\
    'is_compound' => false,\
    'for_shipping' => true,\
    'for_order' => true\
]);
```

### Get Tax Rates by Country [​](https://dev.fluentcart.com/database/models/tax-rate\#get-tax-rates-by-country)

php

```
$usTaxRates = FluentCart\App\Models\TaxRate::where('country', 'US')->get();
$caTaxRates = FluentCart\App\Models\TaxRate::where('country', 'CA')->get();
```

### Get Tax Rates by State [​](https://dev.fluentcart.com/database/models/tax-rate\#get-tax-rates-by-state)

php

```
$caTaxRates = FluentCart\App\Models\TaxRate::where('country', 'US')
    ->where('state', 'CA')
    ->get();
```

### Get Tax Rates with Tax Class [​](https://dev.fluentcart.com/database/models/tax-rate\#get-tax-rates-with-tax-class)

php

```
$taxRates = FluentCart\App\Models\TaxRate::with('tax_class')->get();

foreach ($taxRates as $rate) {
    echo "Rate: " . $rate->name . " (" . $rate->rate . "%)";
    echo "Class: " . $rate->tax_class->title;
}
```

### Get Tax Rates by Priority [​](https://dev.fluentcart.com/database/models/tax-rate\#get-tax-rates-by-priority)

php

```
$orderedTaxRates = FluentCart\App\Models\TaxRate::orderBy('priority', 'asc')->get();
```

### Get Compound Tax Rates [​](https://dev.fluentcart.com/database/models/tax-rate\#get-compound-tax-rates)

php

```
$compoundTaxRates = FluentCart\App\Models\TaxRate::where('is_compound', true)->get();
$nonCompoundTaxRates = FluentCart\App\Models\TaxRate::where('is_compound', false)->get();
```

### Get Tax Rates for Shipping [​](https://dev.fluentcart.com/database/models/tax-rate\#get-tax-rates-for-shipping)

php

```
$shippingTaxRates = FluentCart\App\Models\TaxRate::where('for_shipping', true)->get();
```

### Get Tax Rates for Orders [​](https://dev.fluentcart.com/database/models/tax-rate\#get-tax-rates-for-orders)

php

```
$orderTaxRates = FluentCart\App\Models\TaxRate::where('for_order', true)->get();
```

### Update Tax Rate [​](https://dev.fluentcart.com/database/models/tax-rate\#update-tax-rate)

php

```
$taxRate = FluentCart\App\Models\TaxRate::find(1);
$taxRate->update([\
    'rate' => 9.25,\
    'name' => 'Updated California Sales Tax'\
]);
```

### Get Tax Rates by Postcode [​](https://dev.fluentcart.com/database/models/tax-rate\#get-tax-rates-by-postcode)

php

```
$postcodeTaxRates = FluentCart\App\Models\TaxRate::where('postcode', '90210')->get();
```

### Get Tax Rates by City [​](https://dev.fluentcart.com/database/models/tax-rate\#get-tax-rates-by-city)

php

```
$cityTaxRates = FluentCart\App\Models\TaxRate::where('city', 'Beverly Hills')->get();
```

### Delete Tax Rate [​](https://dev.fluentcart.com/database/models/tax-rate\#delete-tax-rate)

php

```
$taxRate = FluentCart\App\Models\TaxRate::find(1);
$taxRate->delete();
```

### Get Tax Rates by Group [​](https://dev.fluentcart.com/database/models/tax-rate\#get-tax-rates-by-group)

php

```
$salesTaxRates = FluentCart\App\Models\TaxRate::where('group', 'sales_tax')->get();
$vatTaxRates = FluentCart\App\Models\TaxRate::where('group', 'vat')->get();
```

* * *

Today

Hi! I’m your AI assistant. How can I assist you today?

Just now

Powered by **FluentBot**


---

---

## User Model | FluentCart Developer Docs

**URL** : https://dev.fluentcart.com/database/models/user

[Skip to content](https://dev.fluentcart.com/database/models/user#VPContent)

# User Model [​](https://dev.fluentcart.com/database/models/user\#user-model)

| DB Table Name | {wp\_db\_prefix}\_users |
| --- | --- |
| Schema | [Check Schema](https://dev.fluentcart.com/database/schema.html#users-table) |
| Source File | fluent-cart/app/Models/User.php |
| Name Space | FluentCart\\App\\Models |
| Class | FluentCart\\App\\Models\\User |

## Properties [​](https://dev.fluentcart.com/database/models/user\#properties)

- **Table**: `users`
- **Primary Key**: `ID`
- **Guarded**: `['password']`
- **Fillable**: Not explicitly defined (uses guarded approach)

## Attributes [​](https://dev.fluentcart.com/database/models/user\#attributes)

| Attribute | Data Type | Comment |
| --- | --- | --- |
| ID | Integer | Primary Key (WordPress user ID) |
| user\_login | String | User login name |
| user\_pass | String | User password (guarded) |
| user\_nicename | String | User nice name |
| user\_email | String | User email address |
| user\_url | String | User website URL |
| user\_registered | Date Time | User registration date |
| user\_activation\_key | String | User activation key |
| user\_status | Integer | User status |
| display\_name | String | User display name |

## Usage [​](https://dev.fluentcart.com/database/models/user\#usage)

Please check [Model Basic](https://dev.fluentcart.com/database/models.html) for Common methods.

### Accessing Attributes [​](https://dev.fluentcart.com/database/models/user\#accessing-attributes)

php

```
$user = FluentCart\App\Models\User::find(1);

$user->ID; // returns user ID
$user->user_login; // returns login name
$user->user_email; // returns email address
$user->display_name; // returns display name
```

## Relations [​](https://dev.fluentcart.com/database/models/user\#relations)

This model has the following relationships that you can use

### customer [​](https://dev.fluentcart.com/database/models/user\#customer)

Access the associated customer (HasOne)

- return `FluentCart\App\Models\Customer` Model

#### Example: [​](https://dev.fluentcart.com/database/models/user\#example)

php

```
// Accessing Customer
$customer = $user->customer;

// For Filtering by customer relationship
$users = FluentCart\App\Models\User::whereHas('customer', function($query) {
    $query->where('status', 'active');
})->get();
```

## Methods [​](https://dev.fluentcart.com/database/models/user\#methods)

Along with Global Model methods, this model has few helper methods.

### userCan($permission) [​](https://dev.fluentcart.com/database/models/user\#usercan-permission)

Check if the user has a specific permission. Delegates to `PermissionManager::hasPermission()`.

- Parameters
  - $permission - string\|array
- Returns `boolean`

#### Usage [​](https://dev.fluentcart.com/database/models/user\#usage-1)

php

```
$user = FluentCart\App\Models\User::find(1);
$canManageOrders = $user->userCan('manage_orders');
$canManageProducts = $user->userCan(['manage_products', 'edit_products']);
```

### userCanAny($permission) [​](https://dev.fluentcart.com/database/models/user\#usercanany-permission)

Check if the user has any of the specified permissions. Delegates to `PermissionManager::hasAnyPermission()`.

- Parameters
  - $permission - string\|array
- Returns `boolean`

#### Usage [​](https://dev.fluentcart.com/database/models/user\#usage-2)

php

```
$user = FluentCart\App\Models\User::find(1);
$canManage = $user->userCanAny(['manage_orders', 'manage_products']);
```

### setStoreRole($role) [​](https://dev.fluentcart.com/database/models/user\#setstorerole-role)

Set store role for the user. Stores the role in user meta key `_fluent_cart_admin_role`. Returns a `WP_Error` if the user already has the `manage_options` capability (WordPress Administrator).

- Parameters
  - $role - string
- Returns `int|bool|\WP_Error` \- Returns WP\_Error for administrators, otherwise the result of `update_user_meta()`

#### Usage [​](https://dev.fluentcart.com/database/models/user\#usage-3)

php

```
$user = FluentCart\App\Models\User::find(1);
$result = $user->setStoreRole('store_manager');

if (is_wp_error($result)) {
    echo "Error: " . $result->get_error_message();
} else {
    echo "Role set successfully";
}
```

## Usage Examples [​](https://dev.fluentcart.com/database/models/user\#usage-examples)

### Get User [​](https://dev.fluentcart.com/database/models/user\#get-user)

php

```
$user = FluentCart\App\Models\User::find(1);
echo "User: " . $user->display_name;
echo "Email: " . $user->user_email;
echo "Login: " . $user->user_login;
```

### Check User Permissions [​](https://dev.fluentcart.com/database/models/user\#check-user-permissions)

php

```
$user = FluentCart\App\Models\User::find(1);

// Check single permission
if ($user->userCan('manage_orders')) {
    echo "User can manage orders";
}

// Check multiple permissions (all required)
if ($user->userCan(['manage_products', 'edit_products'])) {
    echo "User can manage and edit products";
}

// Check multiple permissions (any required)
if ($user->userCanAny(['manage_orders', 'manage_products'])) {
    echo "User can manage orders or products";
}
```

### Get User with Customer Data [​](https://dev.fluentcart.com/database/models/user\#get-user-with-customer-data)

php

```
$user = FluentCart\App\Models\User::with('customer')->find(1);
$customer = $user->customer;

if ($customer) {
    echo "Customer ID: " . $customer->id;
    echo "Customer Status: " . $customer->status;
}
```

### Set Store Role [​](https://dev.fluentcart.com/database/models/user\#set-store-role)

php

```
$user = FluentCart\App\Models\User::find(1);
$result = $user->setStoreRole('store_manager');

if (is_wp_error($result)) {
    echo "Error: " . $result->get_error_message();
} else {
    echo "Store role set successfully";
}
```

### Get Users with Customer Relationship [​](https://dev.fluentcart.com/database/models/user\#get-users-with-customer-relationship)

php

```
$users = FluentCart\App\Models\User::whereHas('customer', function($query) {
    $query->where('status', 'active');
})->get();

foreach ($users as $user) {
    echo "User: " . $user->display_name;
    echo "Customer: " . $user->customer->email;
}
```

### Get Users by Role [​](https://dev.fluentcart.com/database/models/user\#get-users-by-role)

php

```
// Get users with specific store role
$storeManagers = get_users([\
    'meta_key' => '_fluent_cart_admin_role',\
    'meta_value' => 'store_manager'\
]);
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

## User Meta Model | FluentCart Developer Docs

**URL** : https://dev.fluentcart.com/database/models/user-meta

[Skip to content](https://dev.fluentcart.com/database/models/user-meta#VPContent)

# User Meta Model [​](https://dev.fluentcart.com/database/models/user-meta\#user-meta-model)

| DB Table Name | {wp\_db\_prefix}\_usermeta |
| --- | --- |
| Schema | [Check Schema](https://dev.fluentcart.com/database/schema.html#usermeta-table) |
| Source File | fluent-cart-pro/app/Models/UserMeta.php |
| Name Space | FluentCartPro\\App\\Models |
| Class | FluentCartPro\\App\\Models\\UserMeta |
| Plugin | FluentCart Pro |

## Properties [​](https://dev.fluentcart.com/database/models/user-meta\#properties)

- **Table**: `usermeta`
- **Primary Key**: `umeta_id`
- **Fillable**: `['user_id', 'meta_key', 'meta_value']`

## Attributes [​](https://dev.fluentcart.com/database/models/user-meta\#attributes)

| Attribute | Data Type | Comment |
| --- | --- | --- |
| umeta\_id | Integer | Primary Key |
| user\_id | Integer | Reference to user |
| meta\_key | String | Meta key name |
| meta\_value | Text | Meta value |

## Usage [​](https://dev.fluentcart.com/database/models/user-meta\#usage)

Please check [Model Basic](https://dev.fluentcart.com/database/models.html) for Common methods.

### Accessing Attributes [​](https://dev.fluentcart.com/database/models/user-meta\#accessing-attributes)

php

```
$userMeta = FluentCartPro\App\Models\UserMeta::find(1);

$userMeta->umeta_id; // returns meta ID
$userMeta->user_id; // returns user ID
$userMeta->meta_key; // returns meta key
$userMeta->meta_value; // returns meta value
```

## Relations [​](https://dev.fluentcart.com/database/models/user-meta\#relations)

This model has the following relationships that you can use

### user [​](https://dev.fluentcart.com/database/models/user-meta\#user)

Access the associated user (BelongsTo)

- return `FluentCartPro\App\Models\User` Model (via `belongsTo(User::class, 'user_id', 'ID')`)

#### Example: [​](https://dev.fluentcart.com/database/models/user-meta\#example)

php

```
// Accessing User
$user = $userMeta->user;

// For Filtering by user relationship
$userMetas = FluentCartPro\App\Models\UserMeta::whereHas('user', function($query) {
    $query->where('user_status', 0);
})->get();
```

## Usage Examples [​](https://dev.fluentcart.com/database/models/user-meta\#usage-examples)

### Get User Meta [​](https://dev.fluentcart.com/database/models/user-meta\#get-user-meta)

php

```
$userMeta = FluentCartPro\App\Models\UserMeta::find(1);
echo "User ID: " . $userMeta->user_id;
echo "Meta Key: " . $userMeta->meta_key;
echo "Meta Value: " . $userMeta->meta_value;
```

### Create User Meta [​](https://dev.fluentcart.com/database/models/user-meta\#create-user-meta)

php

```
$userMeta = FluentCartPro\App\Models\UserMeta::create([\
    'user_id' => 123,\
    'meta_key' => 'fluent_cart_admin_role',\
    'meta_value' => 'store_manager'\
]);
```

### Get All User Meta [​](https://dev.fluentcart.com/database/models/user-meta\#get-all-user-meta)

php

```
$userMetas = FluentCartPro\App\Models\UserMeta::all();

foreach ($userMetas as $meta) {
    echo "User: " . $meta->user_id;
    echo "Key: " . $meta->meta_key;
    echo "Value: " . $meta->meta_value;
}
```

### Get Meta by User [​](https://dev.fluentcart.com/database/models/user-meta\#get-meta-by-user)

php

```
$userMetas = FluentCartPro\App\Models\UserMeta::where('user_id', 123)->get();
```

### Get Meta by Key [​](https://dev.fluentcart.com/database/models/user-meta\#get-meta-by-key)

php

```
$adminRoleMetas = FluentCartPro\App\Models\UserMeta::where('meta_key', 'fluent_cart_admin_role')->get();
```

### Get Meta with User Information [​](https://dev.fluentcart.com/database/models/user-meta\#get-meta-with-user-information)

php

```
$userMetas = FluentCartPro\App\Models\UserMeta::with('user')->get();

foreach ($userMetas as $meta) {
    echo "User: " . $meta->user->display_name;
    echo "Key: " . $meta->meta_key;
    echo "Value: " . $meta->meta_value;
}
```

### Get Specific User Meta [​](https://dev.fluentcart.com/database/models/user-meta\#get-specific-user-meta)

php

```
$userMeta = FluentCartPro\App\Models\UserMeta::where('user_id', 123)
    ->where('meta_key', 'fluent_cart_admin_role')
    ->first();
```

### Update User Meta [​](https://dev.fluentcart.com/database/models/user-meta\#update-user-meta)

php

```
$userMeta = FluentCartPro\App\Models\UserMeta::find(1);
$userMeta->update([\
    'meta_value' => 'store_admin'\
]);
```

### Get Users with Specific Meta [​](https://dev.fluentcart.com/database/models/user-meta\#get-users-with-specific-meta)

php

```
$storeManagers = FluentCartPro\App\Models\UserMeta::where('meta_key', 'fluent_cart_admin_role')
    ->where('meta_value', 'store_manager')
    ->get();
```

### Delete User Meta [​](https://dev.fluentcart.com/database/models/user-meta\#delete-user-meta)

php

```
$userMeta = FluentCartPro\App\Models\UserMeta::find(1);
$userMeta->delete();
```

### Get Meta for Multiple Users [​](https://dev.fluentcart.com/database/models/user-meta\#get-meta-for-multiple-users)

php

```
$userMetas = FluentCartPro\App\Models\UserMeta::whereIn('user_id', [123, 124, 125])->get();
```

### Get Meta for Multiple Keys [​](https://dev.fluentcart.com/database/models/user-meta\#get-meta-for-multiple-keys)

php

```
$userMetas = FluentCartPro\App\Models\UserMeta::whereIn('meta_key', ['fluent_cart_admin_role', 'fluent_cart_permissions'])->get();
```

* * *

**Plugin**: FluentCart Pro

Today

Hi! I’m your AI assistant. How can I assist you today?

Just now

Powered by **FluentBot**


---

---

