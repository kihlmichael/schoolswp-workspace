# FluentCart Developer Docs - Database Models (Part 4/8)

Tous les modèles Eloquent exposés par FluentCart : orders, customers, products, subscriptions, coupons, licenses, taxes, shipping, etc.

---

## License Site Model | FluentCart Developer Docs

**URL** : https://dev.fluentcart.com/database/models/license-site

[Skip to content](https://dev.fluentcart.com/database/models/license-site#VPContent)

Pro

# License Site Model [​](https://dev.fluentcart.com/database/models/license-site\#license-site-model)

| DB Table Name | {wp\_db\_prefix}\_fct\_license\_sites |
| --- | --- |
| Schema | [Check Schema](https://dev.fluentcart.com/database/schema.html#fct-license-sites-table) |
| Source File | fluent-cart-pro/app/Modules/Licensing/Models/LicenseSite.php |
| Name Space | FluentCartPro\\App\\Modules\\Licensing\\Models |
| Class | FluentCartPro\\App\\Modules\\Licensing\\Models\\LicenseSite |
| Plugin | FluentCart Pro |

## Properties [​](https://dev.fluentcart.com/database/models/license-site\#properties)

- **Table**: `fct_license_sites`
- **Primary Key**: `id`
- **Guarded**: `['id']`
- **Fillable**: `['site_url', 'server_version', 'platform_version', 'other']`

## Attributes [​](https://dev.fluentcart.com/database/models/license-site\#attributes)

| Attribute | Data Type | Comment |
| --- | --- | --- |
| id | Integer | Primary Key |
| site\_url | String | Site URL |
| server\_version | String | Server version |
| platform\_version | String | Platform version |
| other | JSON | Additional site information (auto JSON encode/decode via accessor/mutator) |
| created\_at | Date Time | Creation timestamp |
| updated\_at | Date Time | Last update timestamp |

## Usage [​](https://dev.fluentcart.com/database/models/license-site\#usage)

Please check [Model Basic](https://dev.fluentcart.com/database/models.html) for Common methods.

### Accessing Attributes [​](https://dev.fluentcart.com/database/models/license-site\#accessing-attributes)

php

```
$licenseSite = FluentCartPro\App\Modules\Licensing\Models\LicenseSite::find(1);

$licenseSite->id; // returns id
$licenseSite->site_url; // returns site URL
$licenseSite->server_version; // returns server version
$licenseSite->platform_version; // returns platform version
$licenseSite->other; // returns decoded array
```

## Relations [​](https://dev.fluentcart.com/database/models/license-site\#relations)

This model has the following relationships that you can use

### activations [​](https://dev.fluentcart.com/database/models/license-site\#activations)

Access all license activations for this site (HasMany)

- return `FluentCartPro\App\Modules\Licensing\Models\LicenseActivation` Model Collection

#### Example: [​](https://dev.fluentcart.com/database/models/license-site\#example)

php

```
// Accessing Activations
$activations = $licenseSite->activations;

// For Filtering by activations relationship
$licenseSites = FluentCartPro\App\Modules\Licensing\Models\LicenseSite::whereHas('activations', function($query) {
    $query->where('status', 'active');
})->get();
```

## Methods [​](https://dev.fluentcart.com/database/models/license-site\#methods)

Along with Global Model methods, this model has few helper methods.

### setOtherAttribute($value) [​](https://dev.fluentcart.com/database/models/license-site\#setotherattribute-value)

Set other information with automatic JSON encoding (mutator). Arrays and objects are JSON encoded before storage.

- Parameters
  - $value - mixed (array, object, or string)
- Returns `void`

#### Usage [​](https://dev.fluentcart.com/database/models/license-site\#usage-1)

php

```
$licenseSite->other = ['domain' => 'example.com', 'ssl' => true];
// Automatically JSON encodes arrays and objects
```

### getOtherAttribute($value) [​](https://dev.fluentcart.com/database/models/license-site\#getotherattribute-value)

Get other information with automatic JSON decoding (accessor). Returns the decoded array if valid JSON, otherwise returns an empty array.

- Parameters
  - $value - mixed
- Returns `array`

#### Usage [​](https://dev.fluentcart.com/database/models/license-site\#usage-2)

php

```
$other = $licenseSite->other; // Returns decoded array, or empty array if invalid
```

### isLocalSite() [​](https://dev.fluentcart.com/database/models/license-site\#islocalsite)

Check if the site is a local development site. Checks the `url` property against local domain extensions (`.lab`, `.local`, `.test`, `.localhost`) and development subdomains (`staging`, `dev`, `development`, `test`, `testing`). Result is filterable via the `fluent_cart_sl/is_local_site` filter hook.

- Parameters
  - none
- Returns `boolean`

#### Usage [​](https://dev.fluentcart.com/database/models/license-site\#usage-3)

php

```
$isLocal = $licenseSite->isLocalSite();
// Returns true if site is local (lab, local, test, localhost, staging, dev, etc.)
```

## Usage Examples [​](https://dev.fluentcart.com/database/models/license-site\#usage-examples)

### Get License Sites [​](https://dev.fluentcart.com/database/models/license-site\#get-license-sites)

php

```
$licenseSite = FluentCartPro\App\Modules\Licensing\Models\LicenseSite::find(1);
echo "Site URL: " . $licenseSite->site_url;
echo "Server Version: " . $licenseSite->server_version;
echo "Platform Version: " . $licenseSite->platform_version;
```

### Create License Site [​](https://dev.fluentcart.com/database/models/license-site\#create-license-site)

php

```
$licenseSite = FluentCartPro\App\Modules\Licensing\Models\LicenseSite::create([\
    'site_url' => 'https://example.com',\
    'server_version' => 'PHP 8.1',\
    'platform_version' => 'WordPress 6.0',\
    'other' => [\
        'domain' => 'example.com',\
        'ssl' => true,\
        'theme' => 'custom-theme'\
    ]\
]);
```

### Get License Sites with Activations [​](https://dev.fluentcart.com/database/models/license-site\#get-license-sites-with-activations)

php

```
$licenseSites = FluentCartPro\App\Modules\Licensing\Models\LicenseSite::with('activations')->get();

foreach ($licenseSites as $site) {
    echo "Site: " . $site->site_url;
    echo "Activations: " . $site->activations->count();
}
```

### Get Local Sites [​](https://dev.fluentcart.com/database/models/license-site\#get-local-sites)

php

```
$licenseSites = FluentCartPro\App\Modules\Licensing\Models\LicenseSite::all();

foreach ($licenseSites as $site) {
    if ($site->isLocalSite()) {
        echo "Local Site: " . $site->site_url;
    }
}
```

### Get Sites by URL [​](https://dev.fluentcart.com/database/models/license-site\#get-sites-by-url)

php

```
$site = FluentCartPro\App\Modules\Licensing\Models\LicenseSite::where('site_url', 'https://example.com')->first();
```

### Update License Site [​](https://dev.fluentcart.com/database/models/license-site\#update-license-site)

php

```
$licenseSite = FluentCartPro\App\Modules\Licensing\Models\LicenseSite::find(1);
$licenseSite->update([\
    'server_version' => 'PHP 8.2',\
    'platform_version' => 'WordPress 6.1',\
    'other' => ['updated' => true]\
]);
```

### Get Sites with Other Information [​](https://dev.fluentcart.com/database/models/license-site\#get-sites-with-other-information)

php

```
$licenseSites = FluentCartPro\App\Modules\Licensing\Models\LicenseSite::all();

foreach ($licenseSites as $site) {
    $other = $site->other;
    if (isset($other['ssl']) && $other['ssl']) {
        echo "SSL Site: " . $site->site_url;
    }
}
```

### Delete License Site [​](https://dev.fluentcart.com/database/models/license-site\#delete-license-site)

php

```
$licenseSite = FluentCartPro\App\Modules\Licensing\Models\LicenseSite::find(1);
$licenseSite->delete();
```

* * *

**Plugin**: FluentCart Pro

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

## Meta Model | FluentCart Developer Docs

**URL** : https://dev.fluentcart.com/database/models/meta

[Skip to content](https://dev.fluentcart.com/database/models/meta#VPContent)

# Meta Model [​](https://dev.fluentcart.com/database/models/meta\#meta-model)

| DB Table Name | {wp\_db\_prefix}\_fct\_meta |
| --- | --- |
| Schema | [Check Schema](https://dev.fluentcart.com/database/schema.html#fct-meta-table) |
| Source File | fluent-cart/app/Models/Meta.php |
| Name Space | FluentCart\\App\\Models |
| Class | FluentCart\\App\\Models\\Meta |

## Attributes [​](https://dev.fluentcart.com/database/models/meta\#attributes)

| Attribute | Data Type | Comment |
| --- | --- | --- |
| id | Integer | Primary Key |
| object\_type | String | Type of object (User, ProductVariation, etc.) |
| object\_id | Integer | ID of the associated object |
| meta\_key | String | Meta key name |
| meta\_value | Text | Meta value (JSON encoded for arrays/objects) |
| created\_at | Date Time | Creation timestamp |
| updated\_at | Date Time | Last update timestamp |

## Guarded Attributes [​](https://dev.fluentcart.com/database/models/meta\#guarded-attributes)

The `id` field is explicitly guarded via `$guarded = ['id']`.

## Usage [​](https://dev.fluentcart.com/database/models/meta\#usage)

Please check [Model Basic](https://dev.fluentcart.com/database/models.html) for Common methods.

### Accessing Attributes [​](https://dev.fluentcart.com/database/models/meta\#accessing-attributes)

php

```
$meta = FluentCart\App\Models\Meta::find(1);

$meta->id; // returns id
$meta->object_type; // returns object type
$meta->object_id; // returns object ID
$meta->meta_key; // returns meta key
$meta->meta_value; // returns meta value (auto-decoded from JSON)
```

## Scopes [​](https://dev.fluentcart.com/database/models/meta\#scopes)

This model has the following scopes that you can use

### userTheme() [​](https://dev.fluentcart.com/database/models/meta\#usertheme)

Filter meta for current user's theme setting. Filters by `object_type = User::class`, `object_id = current user ID`, and `meta_key = 'theme'`.

- Parameters
  - none

#### Usage: [​](https://dev.fluentcart.com/database/models/meta\#usage-1)

php

```
// Get current user's theme meta
$userTheme = FluentCart\App\Models\Meta::userTheme()->first();
```

### upgradeablePath($productId) [​](https://dev.fluentcart.com/database/models/meta\#upgradeablepath-productid)

Filter meta for upgradeable paths by product ID. Uses a `whereHas` on the `upgradeableVariants` relationship and filters by `PlanUpgradeService::$metaType` and `PlanUpgradeService::$metaKey`.

- Parameters
  - $productId - integer

#### Usage: [​](https://dev.fluentcart.com/database/models/meta\#usage-2)

php

```
// Get upgradeable paths for a product
$upgradePaths = FluentCart\App\Models\Meta::upgradeablePath(123)->get();
```

## Relations [​](https://dev.fluentcart.com/database/models/meta\#relations)

This model has the following relationships that you can use

### upgradeableVariants [​](https://dev.fluentcart.com/database/models/meta\#upgradeablevariants)

Access all upgradeable variants (`hasMany`). Links via `object_id` to `ProductVariation.id`.

- return `FluentCart\App\Models\ProductVariation` Model Collection

#### Example: [​](https://dev.fluentcart.com/database/models/meta\#example)

php

```
// Accessing Upgradeable Variants
$variants = $meta->upgradeableVariants;

// For Filtering by upgradeable variants relationship
$metas = FluentCart\App\Models\Meta::whereHas('upgradeableVariants', function($query) {
    $query->where('status', 'active');
})->get();
```

## Methods [​](https://dev.fluentcart.com/database/models/meta\#methods)

Along with Global Model methods, this model has few helper methods.

### setMetaValueAttribute($meta\_value) [​](https://dev.fluentcart.com/database/models/meta\#setmetavalueattribute-meta-value)

Set meta value with automatic JSON encoding (mutator). If the value is an array or object, it is JSON-encoded with `JSON_UNESCAPED_UNICODE | JSON_UNESCAPED_SLASHES` flags.

- Parameters
  - $meta\_value - mixed (array, object, or string)
- Returns `void`

#### Usage [​](https://dev.fluentcart.com/database/models/meta\#usage-3)

php

```
$meta->meta_value = ['custom_data' => 'value', 'settings' => ['key' => 'value']];
// Automatically JSON encodes arrays and objects
```

### getMetaValueAttribute($value) [​](https://dev.fluentcart.com/database/models/meta\#getmetavalueattribute-value)

Get meta value with automatic JSON decoding (accessor). If the stored value is a string, it attempts to JSON-decode it. Returns the decoded value if successful, or the original string if decoding returns `null`.

- Parameters
  - $value - mixed
- Returns `mixed`

#### Usage [​](https://dev.fluentcart.com/database/models/meta\#usage-4)

php

```
$metaValue = $meta->meta_value; // Returns decoded value (array or string)
```

## Usage Examples [​](https://dev.fluentcart.com/database/models/meta\#usage-examples)

### Get Meta [​](https://dev.fluentcart.com/database/models/meta\#get-meta)

php

```
$meta = FluentCart\App\Models\Meta::where('object_type', 'User')
    ->where('object_id', 123)
    ->get();

foreach ($meta as $metaItem) {
    echo "Key: " . $metaItem->meta_key;
    echo "Value: " . print_r($metaItem->meta_value, true);
}
```

### Create Meta [​](https://dev.fluentcart.com/database/models/meta\#create-meta)

php

```
$meta = FluentCart\App\Models\Meta::create([\
    'object_type' => 'User',\
    'object_id' => 123,\
    'meta_key' => 'preferences',\
    'meta_value' => 'dark_mode'\
]);
```

### Store Complex Meta Data [​](https://dev.fluentcart.com/database/models/meta\#store-complex-meta-data)

php

```
$meta = FluentCart\App\Models\Meta::create([\
    'object_type' => 'ProductVariation',\
    'object_id' => 456,\
    'meta_key' => 'upgrade_paths',\
    'meta_value' => [\
        'upgrade_to' => [789, 101],\
        'discount_percentage' => 20,\
        'conditions' => ['active_subscription' => true]\
    ]\
]);
```

### Get User Theme [​](https://dev.fluentcart.com/database/models/meta\#get-user-theme)

php

```
$userTheme = FluentCart\App\Models\Meta::userTheme()->first();
if ($userTheme) {
    echo "User Theme: " . $userTheme->meta_value;
}
```

### Get Upgradeable Paths [​](https://dev.fluentcart.com/database/models/meta\#get-upgradeable-paths)

php

```
$upgradePaths = FluentCart\App\Models\Meta::upgradeablePath(123)->get();
foreach ($upgradePaths as $path) {
    echo "Upgrade Path: " . print_r($path->meta_value, true);
}
```

### Get Meta by Key [​](https://dev.fluentcart.com/database/models/meta\#get-meta-by-key)

php

```
$meta = FluentCart\App\Models\Meta::where('object_type', 'User')
    ->where('object_id', 123)
    ->where('meta_key', 'preferences')
    ->first();

if ($meta) {
    echo "Preferences: " . $meta->meta_value;
}
```

### Update Meta Value [​](https://dev.fluentcart.com/database/models/meta\#update-meta-value)

php

```
$meta = FluentCart\App\Models\Meta::find(1);
$meta->meta_value = ['updated' => true, 'timestamp' => now()];
$meta->save();
```

### Get All Meta for Object [​](https://dev.fluentcart.com/database/models/meta\#get-all-meta-for-object)

php

```
$objectMetas = FluentCart\App\Models\Meta::where('object_type', 'ProductVariation')
    ->where('object_id', 456)
    ->get();
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

## Order Model | FluentCart Developer Docs

**URL** : https://dev.fluentcart.com/database/models/order

[Skip to content](https://dev.fluentcart.com/database/models/order#VPContent)

# Order Model [​](https://dev.fluentcart.com/database/models/order\#order-model)

| DB Table Name | {wp\_db\_prefix}\_fct\_orders |
| --- | --- |
| Schema | [Check Schema](https://dev.fluentcart.com/database/schema.html#fct-orders-table) |
| Source File | fluent-cart/app/Models/Order.php |
| Name Space | FluentCart\\App\\Models |
| Class | FluentCart\\App\\Models\\Order |

## Attributes [​](https://dev.fluentcart.com/database/models/order\#attributes)

| Attribute | Data Type | Comment |
| --- | --- | --- |
| id | Integer | Primary Key |
| status | String | Order status (draft, pending, processing, completed, etc.) |
| parent\_id | Integer | Parent order ID (for renewals/child orders) |
| receipt\_number | Integer | Receipt number |
| invoice\_no | String | Invoice number |
| fulfillment\_type | String | Fulfillment type (physical, digital) |
| type | String | Order type (subscription, renewal, etc.) |
| mode | String | Order mode (live, test) |
| shipping\_status | String | Shipping status |
| customer\_id | Integer | Customer ID (cast to integer) |
| payment\_method | String | Payment method |
| payment\_status | String | Payment status |
| payment\_method\_title | String | Payment method title |
| currency | String | Currency code |
| subtotal | Integer | Subtotal in cents (cast to double) |
| discount\_tax | Integer | Discount tax in cents (cast to double) |
| manual\_discount\_total | Integer | Manual discount total in cents (cast to double) |
| coupon\_discount\_total | Integer | Coupon discount total in cents (cast to double) |
| shipping\_tax | Integer | Shipping tax in cents (cast to double) |
| shipping\_total | Integer | Shipping total in cents (cast to double) |
| tax\_total | Integer | Tax total in cents (cast to double) |
| total\_amount | Integer | Total amount in cents (cast to double) |
| total\_paid | Integer | Total paid in cents |
| total\_refund | Integer | Total refund in cents |
| rate | Decimal | Exchange rate |
| tax\_behavior | Integer | Tax behavior (0=no\_tax, 1=exclusive, 2=inclusive) |
| note | Text | Order notes |
| ip\_address | Text | Customer IP address |
| completed\_at | Date Time | Completion timestamp |
| refunded\_at | Date Time | Refund timestamp |
| uuid | String | Unique identifier |
| config | JSON | Order configuration (auto-encoded/decoded via accessor/mutator) |
| created\_at | Date Time | Creation timestamp |
| updated\_at | Date Time | Last update timestamp |

## Usage [​](https://dev.fluentcart.com/database/models/order\#usage)

Please check [Model Basic](https://dev.fluentcart.com/database/models.html) for Common methods.

### Accessing Attributes [​](https://dev.fluentcart.com/database/models/order\#accessing-attributes)

php

```
$order = FluentCart\App\Models\Order::find(1);

$order->id; // returns order ID
$order->status; // returns order status
$order->total_amount; // returns total amount in cents
$order->currency; // returns currency code
$order->customer_id; // returns customer ID
```

## Methods [​](https://dev.fluentcart.com/database/models/order\#methods)

Along with Global Model methods, this model has few helper methods.

### updateStatus($key, $newStatus) [​](https://dev.fluentcart.com/database/models/order\#updatestatus-key-newstatus)

Update order status

- Parameters: `$key` (String) - Status key, `$newStatus` (String) - New status
- Returns `FluentCart\App\Models\Order` \- Updated order instance

php

```
$order = FluentCart\App\Models\Order::find(1);
$order->updateStatus('status', 'completed');
```

### updatePaymentStatus($newStatus) [​](https://dev.fluentcart.com/database/models/order\#updatepaymentstatus-newstatus)

Update payment status

- Parameters: `$newStatus` (String) - New payment status
- Returns `FluentCart\App\Models\Order` \- Updated order instance

php

```
$order = FluentCart\App\Models\Order::find(1);
$order->updatePaymentStatus('paid');
```

### getMeta($metaKey, $defaultValue = false) [​](https://dev.fluentcart.com/database/models/order\#getmeta-metakey-defaultvalue-false)

Get order meta value

- Parameters: `$metaKey` (String) - Meta key, `$defaultValue` (Mixed) - Default value
- Returns `Mixed` \- Meta value or default

php

```
$order = FluentCart\App\Models\Order::find(1);
$metaValue = $order->getMeta('custom_field', 'default');
```

### updateMeta($metaKey, $value) [​](https://dev.fluentcart.com/database/models/order\#updatemeta-metakey-value)

Update order meta value

- Parameters: `$metaKey` (String) - Meta key, `$value` (Mixed) - Meta value
- Returns `FluentCart\App\Models\OrderMeta` \- Meta instance

php

```
$order = FluentCart\App\Models\Order::find(1);
$meta = $order->updateMeta('custom_field', 'new_value');
```

### deleteMeta($metaKey) [​](https://dev.fluentcart.com/database/models/order\#deletemeta-metakey)

Delete order meta

- Parameters: `$metaKey` (String) - Meta key
- Returns `Boolean` \- True if deleted

php

```
$order = FluentCart\App\Models\Order::find(1);
$deleted = $order->deleteMeta('custom_field');
```

### getTotalPaidAmount() [​](https://dev.fluentcart.com/database/models/order\#gettotalpaidamount)

Get total paid amount from succeeded transactions

- Returns `Integer` \- Total paid amount in cents

php

```
$order = FluentCart\App\Models\Order::find(1);
$totalPaid = $order->getTotalPaidAmount();
```

### getTotalRefundAmount() [​](https://dev.fluentcart.com/database/models/order\#gettotalrefundamount)

Get total refund amount from refunded transactions

- Returns `Integer` \- Total refund amount in cents

php

```
$order = FluentCart\App\Models\Order::find(1);
$totalRefund = $order->getTotalRefundAmount();
```

### recountTotalPaidAndRefund() [​](https://dev.fluentcart.com/database/models/order\#recounttotalpaidandrefund)

Recount total paid and refund amounts. Updates `total_refund` and sets `payment_status` to refunded or partially refunded as appropriate.

- Returns `FluentCart\App\Models\Order` \- Updated order instance

php

```
$order = FluentCart\App\Models\Order::find(1);
$order->recountTotalPaidAndRefund();
```

### syncOrderAfterRefund($type, $refundedAmount) [​](https://dev.fluentcart.com/database/models/order\#syncorderafterrefund-type-refundedamount)

Sync order after refund

- Parameters: `$type` (String) - Refund type ('full' or 'partial'), `$refundedAmount` (Integer) - Refund amount
- Returns `FluentCart\App\Models\Order` \- Updated order instance

php

```
$order = FluentCart\App\Models\Order::find(1);
$order->syncOrderAfterRefund('full', 1000);
```

### updateRefundedItems($refundedItemIds, $refundedAmount) [​](https://dev.fluentcart.com/database/models/order\#updaterefundeditems-refundeditemids-refundedamount)

Update refunded items. Distributes refund amount proportionally across the specified order items.

- Parameters: `$refundedItemIds` (Array) - Order item IDs, `$refundedAmount` (Integer) - Refund amount

php

```
$order = FluentCart\App\Models\Order::find(1);
$order->updateRefundedItems([1, 2, 3], 1000);
```

### recountTotalPaid() [​](https://dev.fluentcart.com/database/models/order\#recounttotalpaid)

Recount total paid amount (paid minus refunded)

- Returns `FluentCart\App\Models\Order` \- Updated order instance

php

```
$order = FluentCart\App\Models\Order::find(1);
$order->recountTotalPaid();
```

### getLatestTransactionAttribute() [​](https://dev.fluentcart.com/database/models/order\#getlatesttransactionattribute)

Get latest non-refund transaction (accessor, accessed as `latest_transaction` attribute)

- Returns `FluentCart\App\Models\OrderTransaction|null` \- Latest transaction

php

```
$order = FluentCart\App\Models\Order::find(1);
$transaction = $order->latest_transaction;
```

### isSubscription() [​](https://dev.fluentcart.com/database/models/order\#issubscription)

Check if order is subscription

- Returns `Boolean` \- True if order has subscription items

php

```
$order = FluentCart\App\Models\Order::find(1);
$isSubscription = $order->isSubscription();
```

### getViewUrl($type = 'customer') [​](https://dev.fluentcart.com/database/models/order\#getviewurl-type-customer)

Get order view URL

- Parameters: `$type` (String) - View type ('customer' or 'admin')
- Returns `String` \- View URL

php

```
$order = FluentCart\App\Models\Order::find(1);
$viewUrl = $order->getViewUrl('admin');
```

### getLatestTransaction() [​](https://dev.fluentcart.com/database/models/order\#getlatesttransaction)

Get latest non-refund transaction (method call, unlike the accessor attribute)

- Returns `FluentCart\App\Models\OrderTransaction|null` \- Latest transaction

php

```
$order = FluentCart\App\Models\Order::find(1);
$transaction = $order->getLatestTransaction();
```

### currentSubscription() [​](https://dev.fluentcart.com/database/models/order\#currentsubscription)

Get current active subscription for this order

- Returns `FluentCart\App\Models\Subscription|null` \- Current active subscription

php

```
$order = FluentCart\App\Models\Order::find(1);
$subscription = $order->currentSubscription();
```

### getDownloads($scope = 'email') [​](https://dev.fluentcart.com/database/models/order\#getdownloads-scope-email)

Get order downloads. Returns downloadable files associated with the order items, filtered by product variation authorization.

- Parameters: `$scope` (String) - Download scope
- Returns `Array` \- Download data

php

```
$order = FluentCart\App\Models\Order::find(1);
$downloads = $order->getDownloads('email');
```

### getLicenses($with = \['product', 'productVariant'\]) [​](https://dev.fluentcart.com/database/models/order\#getlicenses-with-product-productvariant)

Get order licenses (requires Pro and active license module)

- Parameters: `$with` (Array) - Relationships to eager load (default: `['product', 'productVariant']`)
- Returns `Illuminate\Database\Eloquent\Collection|null` \- Licenses collection or null if module inactive

php

```
$order = FluentCart\App\Models\Order::find(1);
$licenses = $order->getLicenses(['product', 'productVariant']);
```

### getDownloadsById($orderId) [​](https://dev.fluentcart.com/database/models/order\#getdownloadsbyid-orderid)

Get downloads for a specific order by ID

- Parameters: `$orderId` (Integer) - Order ID
- Returns `Array` \- Download data

php

```
$order = FluentCart\App\Models\Order::find(1);
$downloads = $order->getDownloadsById(42);
```

### getReceiptUrl() [​](https://dev.fluentcart.com/database/models/order\#getreceipturl)

Get receipt URL

- Returns `String` \- Receipt URL

php

```
$order = FluentCart\App\Models\Order::find(1);
$receiptUrl = $order->getReceiptUrl();
```

### addLog($title, $description = '', $type = 'info', $by = '') [​](https://dev.fluentcart.com/database/models/order\#addlog-title-description-type-info-by)

Add order log

- Parameters: `$title` (String) - Log title, `$description` (String) - Description, `$type` (String) - Log type, `$by` (String) - Created by

php

```
$order = FluentCart\App\Models\Order::find(1);
$order->addLog('Status Updated', 'Order status changed to completed', 'info', 'admin');
```

### canBeRefunded() [​](https://dev.fluentcart.com/database/models/order\#canberefunded)

Check if order can be refunded. Returns false if the order has been upgraded to another order.

- Returns `Boolean` \- True if order can be refunded

php

```
$order = FluentCart\App\Models\Order::find(1);
$canBeRefunded = $order->canBeRefunded();
```

### generateReceiptNumber() [​](https://dev.fluentcart.com/database/models/order\#generatereceiptnumber)

Generate receipt number and invoice number if not already set

- Returns `FluentCart\App\Models\Order` \- Updated order instance

php

```
$order = FluentCart\App\Models\Order::find(1);
$order->generateReceiptNumber();
```

### canBeDeleted() [​](https://dev.fluentcart.com/database/models/order\#canbedeleted)

Check if order can be deleted. Validates order status, payment status, mode, and subscription state. Test mode orders can always be deleted. Live orders must be canceled or on-hold, and must not have an active subscription.

- Returns `Boolean|WP_Error` \- True if order can be deleted, or WP\_Error with reason

php

```
$order = FluentCart\App\Models\Order::find(1);
$canBeDeleted = $order->canBeDeleted();
if (is_wp_error($canBeDeleted)) {
    echo $canBeDeleted->get_error_message();
}
```

## Relations [​](https://dev.fluentcart.com/database/models/order\#relations)

This model has the following relationships that you can use

### parentOrder [​](https://dev.fluentcart.com/database/models/order\#parentorder)

Access the parent order.

- Returns `FluentCart\App\Models\Order`

php

```
$order = FluentCart\App\Models\Order::find(1);
$parentOrder = $order->parentOrder;
```

### children [​](https://dev.fluentcart.com/database/models/order\#children)

Access the child orders.

- Returns `Illuminate\Database\Eloquent\Collection` of `FluentCart\App\Models\Order`

php

```
$order = FluentCart\App\Models\Order::find(1);
$children = $order->children;
```

### transactions [​](https://dev.fluentcart.com/database/models/order\#transactions)

Access the order transactions.

- Returns `Illuminate\Database\Eloquent\Collection` of `FluentCart\App\Models\OrderTransaction`

php

```
$order = FluentCart\App\Models\Order::find(1);
$transactions = $order->transactions;
```

### subscriptions [​](https://dev.fluentcart.com/database/models/order\#subscriptions)

Access the order subscriptions.

- Returns `Illuminate\Database\Eloquent\Collection` of `FluentCart\App\Models\Subscription`

php

```
$order = FluentCart\App\Models\Order::find(1);
$subscriptions = $order->subscriptions;
```

### order\_items [​](https://dev.fluentcart.com/database/models/order\#order-items)

Access the order items.

- Returns `Illuminate\Database\Eloquent\Collection` of `FluentCart\App\Models\OrderItem`

php

```
$order = FluentCart\App\Models\Order::find(1);
$items = $order->order_items;
```

### filteredOrderItems [​](https://dev.fluentcart.com/database/models/order\#filteredorderitems)

Access the filtered order items based on priority rules for payment\_type (onetime > subscription > adjustment).

- Returns `Illuminate\Database\Eloquent\Collection` of `FluentCart\App\Models\OrderItem`

php

```
$order = FluentCart\App\Models\Order::find(1);
$filteredItems = $order->filteredOrderItems;
```

### customer [​](https://dev.fluentcart.com/database/models/order\#customer)

Access the customer.

- Returns `FluentCart\App\Models\Customer`

php

```
$order = FluentCart\App\Models\Order::find(1);
$customer = $order->customer;
```

### orderMeta [​](https://dev.fluentcart.com/database/models/order\#ordermeta)

Access the order metadata.

- Returns `Illuminate\Database\Eloquent\Collection` of `FluentCart\App\Models\OrderMeta`

php

```
$order = FluentCart\App\Models\Order::find(1);
$meta = $order->orderMeta;
```

### orderTaxRates [​](https://dev.fluentcart.com/database/models/order\#ordertaxrates)

Access the order tax rates.

- Returns `Illuminate\Database\Eloquent\Collection` of `FluentCart\App\Models\OrderTaxRate`

php

```
$order = FluentCart\App\Models\Order::find(1);
$taxRates = $order->orderTaxRates;
```

### appliedCoupons [​](https://dev.fluentcart.com/database/models/order\#appliedcoupons)

Access the applied coupons.

- Returns `Illuminate\Database\Eloquent\Collection` of `FluentCart\App\Models\AppliedCoupon`

php

```
$order = FluentCart\App\Models\Order::find(1);
$appliedCoupons = $order->appliedCoupons;
```

### usedCoupons [​](https://dev.fluentcart.com/database/models/order\#usedcoupons)

Access the used coupons (through the applied coupons intermediate table).

- Returns `Illuminate\Database\Eloquent\Collection` of `FluentCart\App\Models\Coupon`

php

```
$order = FluentCart\App\Models\Order::find(1);
$usedCoupons = $order->usedCoupons;
```

### shipping\_address [​](https://dev.fluentcart.com/database/models/order\#shipping-address)

Access the shipping address.

- Returns `FluentCart\App\Models\OrderAddress`

php

```
$order = FluentCart\App\Models\Order::find(1);
$address = $order->shipping_address;
```

### billing\_address [​](https://dev.fluentcart.com/database/models/order\#billing-address)

Access the billing address.

- Returns `FluentCart\App\Models\OrderAddress`

php

```
$order = FluentCart\App\Models\Order::find(1);
$address = $order->billing_address;
```

### order\_addresses [​](https://dev.fluentcart.com/database/models/order\#order-addresses)

Access the order addresses.

- Returns `Illuminate\Database\Eloquent\Collection` of `FluentCart\App\Models\OrderAddress`

php

```
$order = FluentCart\App\Models\Order::find(1);
$addresses = $order->order_addresses;
```

### licenses [​](https://dev.fluentcart.com/database/models/order\#licenses)

Access the order licenses.

- Returns `Illuminate\Database\Eloquent\Collection` of `FluentCartPro\App\Modules\Licensing\Models\License`

php

```
$order = FluentCart\App\Models\Order::find(1);
$licenses = $order->licenses;
```

### labels [​](https://dev.fluentcart.com/database/models/order\#labels)

Access the order labels (morph many relationship).

- Returns `Illuminate\Database\Eloquent\Collection` of `FluentCart\App\Models\LabelRelationship`

php

```
$order = FluentCart\App\Models\Order::find(1);
$labels = $order->labels;
```

### renewals [​](https://dev.fluentcart.com/database/models/order\#renewals)

Access the order renewals (child orders of type 'renewal', excluding canceled, failed, and on-hold).

- Returns `Illuminate\Database\Eloquent\Collection` of `FluentCart\App\Models\Order`

php

```
$order = FluentCart\App\Models\Order::find(1);
$renewals = $order->renewals;
```

### orderOperation [​](https://dev.fluentcart.com/database/models/order\#orderoperation)

Access the order operation record.

- Returns `FluentCart\App\Models\OrderOperation`

php

```
$order = FluentCart\App\Models\Order::find(1);
$operation = $order->orderOperation;
```

## Scopes [​](https://dev.fluentcart.com/database/models/order\#scopes)

This model has the following scopes that you can use

### searchBy($search) [​](https://dev.fluentcart.com/database/models/order\#searchby-search)

Search orders by query. Searches across order ID, status, total amount, payment status, payment method, invoice number, order item titles, and customer name/email.

- Parameters: `$search` (String) - Search query

php

```
$orders = FluentCart\App\Models\Order::searchBy('john')->get();
```

### ofPaymentStatus($status) [​](https://dev.fluentcart.com/database/models/order\#ofpaymentstatus-status)

Get orders by payment status

- Parameters: `$status` (String) - Payment status

php

```
$orders = FluentCart\App\Models\Order::ofPaymentStatus('paid')->get();
```

### ofOrderStatus($status) [​](https://dev.fluentcart.com/database/models/order\#oforderstatus-status)

Get orders by order status

- Parameters: `$status` (String) - Order status

php

```
$orders = FluentCart\App\Models\Order::ofOrderStatus('completed')->get();
```

### ofShippingStatus($status) [​](https://dev.fluentcart.com/database/models/order\#ofshippingstatus-status)

Get orders by shipping status

- Parameters: `$status` (String) - Shipping status

php

```
$orders = FluentCart\App\Models\Order::ofShippingStatus('shipped')->get();
```

### ofOrderType($type) [​](https://dev.fluentcart.com/database/models/order\#ofordertype-type)

Get orders by order type

- Parameters: `$type` (String) - Order type

php

```
$orders = FluentCart\App\Models\Order::ofOrderType('payment')->get();
```

### ofPaymentMethod($methodName) [​](https://dev.fluentcart.com/database/models/order\#ofpaymentmethod-methodname)

Get orders by payment method

- Parameters: `$methodName` (String) - Payment method name

php

```
$orders = FluentCart\App\Models\Order::ofPaymentMethod('stripe')->get();
```

### applyCustomFilters($filters) [​](https://dev.fluentcart.com/database/models/order\#applycustomfilters-filters)

Apply custom filters

- Parameters: `$filters` (Array) - Filter array

php

```
$orders = FluentCart\App\Models\Order::applyCustomFilters([\
    'status' => ['value' => ['completed', 'processing']]\
])->get();
```

## Usage Examples [​](https://dev.fluentcart.com/database/models/order\#usage-examples)

### Creating an Order [​](https://dev.fluentcart.com/database/models/order\#creating-an-order)

php

```
use FluentCart\App\Models\Order;

$order = Order::create([\
    'customer_id' => 1,\
    'status' => 'pending',\
    'payment_method' => 'stripe',\
    'currency' => 'USD',\
    'total_amount' => 9999 // $99.99 in cents\
]);
```

### Retrieving Orders [​](https://dev.fluentcart.com/database/models/order\#retrieving-orders)

php

```
// Get orders by payment status
$orders = Order::ofPaymentStatus('paid')->get();

// Get order by ID
$order = Order::find(1);

// Get order with items and customer
$order = Order::with(['order_items', 'customer'])->find(1);
```

### Updating an Order [​](https://dev.fluentcart.com/database/models/order\#updating-an-order)

php

```
$order = Order::find(1);
$order->status = 'completed';
$order->completed_at = now();
$order->save();
```

### Deleting an Order [​](https://dev.fluentcart.com/database/models/order\#deleting-an-order)

php

```
$order = Order::find(1);
$order->delete();
```

* * *

Today

Hi! I’m your AI assistant. How can I assist you today?

Just now

Powered by **FluentBot**


---

---

## Order Address Model | FluentCart Developer Docs

**URL** : https://dev.fluentcart.com/database/models/order-address

[Skip to content](https://dev.fluentcart.com/database/models/order-address#VPContent)

# Order Address Model [​](https://dev.fluentcart.com/database/models/order-address\#order-address-model)

| DB Table Name | {wp\_db\_prefix}\_fct\_order\_addresses |
| --- | --- |
| Schema | [Check Schema](https://dev.fluentcart.com/database/schema.html#fct-order-addresses-table) |
| Source File | fluent-cart/app/Models/OrderAddress.php |
| Name Space | FluentCart\\App\\Models |
| Class | FluentCart\\App\\Models\\OrderAddress |

## Attributes [​](https://dev.fluentcart.com/database/models/order-address\#attributes)

| Attribute | Data Type | Comment |
| --- | --- | --- |
| id | Integer | Primary Key |
| order\_id | Integer | Reference to order |
| type | String | Address type (billing, shipping) |
| name | String | Full name |
| address\_1 | String | Primary address line |
| address\_2 | String | Secondary address line |
| city | String | City |
| state | String | State/Province |
| postcode | String | Postal/ZIP code |
| country | String | Country code |
| meta | JSON NULL | Additional address data (stores phone, company\_name, label in `other_data`) |
| created\_at | Date Time | Creation timestamp |
| updated\_at | Date Time | Last update timestamp |

## Appended Attributes [​](https://dev.fluentcart.com/database/models/order-address\#appended-attributes)

The following virtual attributes are appended to every serialized response via `$appends`:

| Attribute | Data Type | Description |
| --- | --- | --- |
| email | String/Null | Email from associated order's customer |
| first\_name | String/Null | First part of name (split by space) |
| last\_name | String/Null | Last part of name (split by space) |
| full\_name | String/Null | Same as `name` attribute |
| formatted\_address | Array | Full formatted address array with resolved country/state names |
| company\_name | String | Company name stored in `meta.other_data.company_name` |
| phone | String | Phone number stored in `meta.other_data.phone` |
| label | String | Address label stored in `meta.other_data.label` |

## Usage [​](https://dev.fluentcart.com/database/models/order-address\#usage)

Please check [Model Basic](https://dev.fluentcart.com/database/models.html) for Common methods.

### Accessing Attributes [​](https://dev.fluentcart.com/database/models/order-address\#accessing-attributes)

php

```
$orderAddress = FluentCart\App\Models\OrderAddress::find(1);

$orderAddress->id; // returns id
$orderAddress->order_id; // returns order ID
$orderAddress->type; // returns address type
$orderAddress->name; // returns full name
$orderAddress->email; // returns email from order's customer
$orderAddress->first_name; // returns first name
$orderAddress->last_name; // returns last name
$orderAddress->full_name; // returns full name (alias for name)
$orderAddress->company_name; // returns company name from meta
$orderAddress->phone; // returns phone from meta
$orderAddress->label; // returns label from meta
$orderAddress->formatted_address; // returns formatted address array
```

## Relations [​](https://dev.fluentcart.com/database/models/order-address\#relations)

This model has the following relationships that you can use

### order [​](https://dev.fluentcart.com/database/models/order-address\#order)

Access the associated order

- return `FluentCart\App\Models\Order` Model

#### Example: [​](https://dev.fluentcart.com/database/models/order-address\#example)

php

```
// Accessing Order
$order = $orderAddress->order;

// For Filtering by order relationship
$orderAddresses = FluentCart\App\Models\OrderAddress::whereHas('order', function($query) {
    $query->where('status', 'completed');
})->get();
```

## Methods [​](https://dev.fluentcart.com/database/models/order-address\#methods)

Along with Global Model methods, this model has few helper methods.

### setMetaAttribute($value) [​](https://dev.fluentcart.com/database/models/order-address\#setmetaattribute-value)

Set meta from array/object (mutator). Automatically JSON-encodes the value.

- Parameters
  - $value - array\|object\|null
- Returns `void`

#### Usage [​](https://dev.fluentcart.com/database/models/order-address\#usage-1)

php

```
$orderAddress->meta = ['other_data' => ['phone' => '555-1234', 'company_name' => 'Acme Inc']];
```

### getMetaAttribute($value) [​](https://dev.fluentcart.com/database/models/order-address\#getmetaattribute-value)

Get meta as array (accessor). Automatically JSON-decodes the stored value.

- Parameters
  - $value - mixed
- Returns `array`

#### Usage [​](https://dev.fluentcart.com/database/models/order-address\#usage-2)

php

```
$meta = $orderAddress->meta; // Returns array
```

### getFullNameAttribute() [​](https://dev.fluentcart.com/database/models/order-address\#getfullnameattribute)

Get full name (accessor). Returns the `name` attribute directly.

- Parameters
  - none
- Returns `string|null`

#### Usage [​](https://dev.fluentcart.com/database/models/order-address\#usage-3)

php

```
$fullName = $orderAddress->full_name; // Returns full name
```

### getFirstNameAttribute() [​](https://dev.fluentcart.com/database/models/order-address\#getfirstnameattribute)

Get first name (accessor). Splits `name` by space and returns the first part.

- Parameters
  - none
- Returns `string|null`

#### Usage [​](https://dev.fluentcart.com/database/models/order-address\#usage-4)

php

```
$firstName = $orderAddress->first_name; // Returns first name
```

### getLastNameAttribute() [​](https://dev.fluentcart.com/database/models/order-address\#getlastnameattribute)

Get last name (accessor). Splits `name` by space and returns the last part.

- Parameters
  - none
- Returns `string|null`

#### Usage [​](https://dev.fluentcart.com/database/models/order-address\#usage-5)

php

```
$lastName = $orderAddress->last_name; // Returns last name
```

### getEmailAttribute() [​](https://dev.fluentcart.com/database/models/order-address\#getemailattribute)

Get email address from associated order's customer (accessor).

- Parameters
  - none
- Returns `string|null`

#### Usage [​](https://dev.fluentcart.com/database/models/order-address\#usage-6)

php

```
$email = $orderAddress->email; // Returns email from order's customer
```

### getCompanyNameAttribute() [​](https://dev.fluentcart.com/database/models/order-address\#getcompanynameattribute)

Get company name from meta `other_data.company_name` (accessor).

- Parameters
  - none
- Returns `string`

#### Usage [​](https://dev.fluentcart.com/database/models/order-address\#usage-7)

php

```
$companyName = $orderAddress->company_name; // Returns company name or empty string
```

### setCompanyNameAttribute($value) [​](https://dev.fluentcart.com/database/models/order-address\#setcompanynameattribute-value)

Set company name in meta `other_data.company_name` (mutator). Skips if value is falsy.

- Parameters
  - $value - string\|null
- Returns `void`

#### Usage [​](https://dev.fluentcart.com/database/models/order-address\#usage-8)

php

```
$orderAddress->company_name = 'Acme Inc';
```

### getPhoneAttribute() [​](https://dev.fluentcart.com/database/models/order-address\#getphoneattribute)

Get phone number from meta `other_data.phone` (accessor).

- Parameters
  - none
- Returns `string`

#### Usage [​](https://dev.fluentcart.com/database/models/order-address\#usage-9)

php

```
$phone = $orderAddress->phone; // Returns phone number or empty string
```

### setPhoneAttribute($value) [​](https://dev.fluentcart.com/database/models/order-address\#setphoneattribute-value)

Set phone number in meta `other_data.phone` (mutator). Skips if value is falsy.

- Parameters
  - $value - string\|null
- Returns `void`

#### Usage [​](https://dev.fluentcart.com/database/models/order-address\#usage-10)

php

```
$orderAddress->phone = '555-1234';
```

### getLabelAttribute() [​](https://dev.fluentcart.com/database/models/order-address\#getlabelattribute)

Get address label from meta `other_data.label` (accessor).

- Parameters
  - none
- Returns `string`

#### Usage [​](https://dev.fluentcart.com/database/models/order-address\#usage-11)

php

```
$label = $orderAddress->label; // Returns label or empty string
```

### setLabelAttribute($value) [​](https://dev.fluentcart.com/database/models/order-address\#setlabelattribute-value)

Set address label in meta `other_data.label` (mutator). Skips if value is falsy.

- Parameters
  - $value - string\|null
- Returns `void`

#### Usage [​](https://dev.fluentcart.com/database/models/order-address\#usage-12)

php

```
$orderAddress->label = 'Home';
```

### getFormattedAddressAttribute() [​](https://dev.fluentcart.com/database/models/order-address\#getformattedaddressattribute)

Get formatted address as array (accessor). Delegates to `getFormattedAddress()`.

- Parameters
  - none
- Returns `array`

#### Usage [​](https://dev.fluentcart.com/database/models/order-address\#usage-13)

php

```
$formattedAddress = $orderAddress->formatted_address; // Returns formatted address array
```

### getFormattedAddress($filtered = false) [​](https://dev.fluentcart.com/database/models/order-address\#getformattedaddress-filtered-false)

Get formatted address with optional filtering. Returns an array including resolved country/state names, full address string, and all name/email/company fields.

- Parameters
  - $filtered - boolean (default: false) - When true, removes empty values from the address array
- Returns `array` \- Keys: `country`, `state`, `city`, `postcode`, `address_1`, `address_2`, `type`, `name`, `first_name`, `last_name`, `full_name`, `email`, `company_name`, `label`, `full_address`

#### Usage [​](https://dev.fluentcart.com/database/models/order-address\#usage-14)

php

```
$formattedAddress = $orderAddress->getFormattedAddress(true); // Returns filtered formatted address
```

### getAddressAsText($isHtml = false, $includeName = true, $separator = ', ') [​](https://dev.fluentcart.com/database/models/order-address\#getaddressastext-ishtml-false-includename-true-separator)

Get address as formatted text string.

- Parameters
  - $isHtml - boolean (default: false)
  - $includeName - boolean (default: true)
  - $separator - string (default: ', ')
- Returns `string`

#### Usage [​](https://dev.fluentcart.com/database/models/order-address\#usage-15)

php

```
$addressText = $orderAddress->getAddressAsText(false, true, ', '); // Returns: "John Doe, 123 Main St, New York, NY, 10001, US"
```

### getFormattedDataForCheckout($prefix = 'billing\_') [​](https://dev.fluentcart.com/database/models/order-address\#getformatteddataforcheckout-prefix-billing)

Get address data formatted for checkout forms. Returns an associative array with prefixed keys suitable for pre-filling checkout fields. When prefix is `billing_`, the `billing_full_name` key is excluded.

- Parameters
  - $prefix - string (default: 'billing\_')
- Returns `array` \- Keys like `{prefix}address_id`, `{prefix}full_name`, `{prefix}address_1`, `{prefix}address_2`, `{prefix}city`, `{prefix}state`, `{prefix}phone`, `{prefix}postcode`, `{prefix}country`, `{prefix}company_name`

#### Usage [​](https://dev.fluentcart.com/database/models/order-address\#usage-16)

php

```
$checkoutData = $orderAddress->getFormattedDataForCheckout('billing_');
// Returns: ['billing_address_id' => 1, 'billing_address_1' => '123 Main St', ...]

$shippingData = $orderAddress->getFormattedDataForCheckout('shipping_');
// Returns: ['shipping_address_id' => 1, 'shipping_full_name' => 'John Doe', ...]
```

## Address Types [​](https://dev.fluentcart.com/database/models/order-address\#address-types)

Common address types in FluentCart:

- `billing` \- Billing address for payment processing
- `shipping` \- Shipping address for order fulfillment

## Usage Examples [​](https://dev.fluentcart.com/database/models/order-address\#usage-examples)

### Get Order Addresses [​](https://dev.fluentcart.com/database/models/order-address\#get-order-addresses)

php

```
$order = FluentCart\App\Models\Order::find(123);
$addresses = $order->order_addresses;

foreach ($addresses as $address) {
    echo "Address Type: " . $address->type;
    echo "Name: " . $address->name;
    echo "Address: " . $address->getAddressAsText();
}
```

### Get Billing Address [​](https://dev.fluentcart.com/database/models/order-address\#get-billing-address)

php

```
$billingAddress = FluentCart\App\Models\OrderAddress::where('order_id', 123)
    ->where('type', 'billing')
    ->first();
```

### Get Shipping Address [​](https://dev.fluentcart.com/database/models/order-address\#get-shipping-address)

php

```
$shippingAddress = FluentCart\App\Models\OrderAddress::where('order_id', 123)
    ->where('type', 'shipping')
    ->first();
```

### Create Order Address [​](https://dev.fluentcart.com/database/models/order-address\#create-order-address)

php

```
$orderAddress = FluentCart\App\Models\OrderAddress::create([\
    'order_id' => 123,\
    'type' => 'billing',\
    'name' => 'John Doe',\
    'address_1' => '123 Main Street',\
    'city' => 'New York',\
    'state' => 'NY',\
    'postcode' => '10001',\
    'country' => 'US'\
]);
```

### Get Formatted Address [​](https://dev.fluentcart.com/database/models/order-address\#get-formatted-address)

php

```
$address = FluentCart\App\Models\OrderAddress::find(1);
$formattedText = $address->getAddressAsText();
// Returns: "John Doe, 123 Main Street, New York, NY, 10001, US"
```

### Get Checkout-Ready Data [​](https://dev.fluentcart.com/database/models/order-address\#get-checkout-ready-data)

php

```
$address = FluentCart\App\Models\OrderAddress::find(1);
$billingData = $address->getFormattedDataForCheckout('billing_');
$shippingData = $address->getFormattedDataForCheckout('shipping_');
```

* * *

Today

Hi! I’m your AI assistant. How can I assist you today?

Just now

Powered by **FluentBot**


---

---

## Order Download Permission Model | FluentCart Developer Docs

**URL** : https://dev.fluentcart.com/database/models/order-download-permission

[Skip to content](https://dev.fluentcart.com/database/models/order-download-permission#VPContent)

# Order Download Permission Model [​](https://dev.fluentcart.com/database/models/order-download-permission\#order-download-permission-model)

| DB Table Name | {wp\_db\_prefix}\_fct\_order\_download\_permissions |
| --- | --- |
| Schema | [Check Schema](https://dev.fluentcart.com/database/schema.html#fct-order-download-permissions-table) |
| Source File | fluent-cart/app/Models/OrderDownloadPermission.php |
| Name Space | FluentCart\\App\\Models |
| Class | FluentCart\\App\\Models\\OrderDownloadPermission |

## Attributes [​](https://dev.fluentcart.com/database/models/order-download-permission\#attributes)

| Attribute | Data Type | Comment |
| --- | --- | --- |
| id | Integer | Primary Key (guarded) |
| order\_id | Integer | Reference to order |
| variation\_id | Integer | Reference to product variation |
| customer\_id | Integer | Reference to customer |
| download\_id | Integer | Reference to download |
| download\_count | Integer | Number of downloads used |
| download\_limit | Integer | Maximum number of downloads allowed |
| access\_expires | Date Time | When download access expires |
| created\_at | Date Time | Creation timestamp |
| updated\_at | Date Time | Last update timestamp |

> **Note:** The `id` column is both guarded and declared as `$primaryKey`.

## Usage [​](https://dev.fluentcart.com/database/models/order-download-permission\#usage)

Please check [Model Basic](https://dev.fluentcart.com/database/models.html) for Common methods.

### Accessing Attributes [​](https://dev.fluentcart.com/database/models/order-download-permission\#accessing-attributes)

php

```
$orderDownloadPermission = FluentCart\App\Models\OrderDownloadPermission::find(1);

$orderDownloadPermission->id; // returns id
$orderDownloadPermission->order_id; // returns order ID
$orderDownloadPermission->customer_id; // returns customer ID
$orderDownloadPermission->download_count; // returns download count
$orderDownloadPermission->download_limit; // returns download limit
$orderDownloadPermission->access_expires; // returns access expiry date
```

## Relations [​](https://dev.fluentcart.com/database/models/order-download-permission\#relations)

This model has the following relationships that you can use

### order [​](https://dev.fluentcart.com/database/models/order-download-permission\#order)

Access the associated order

- return `FluentCart\App\Models\Order` Model

#### Example: [​](https://dev.fluentcart.com/database/models/order-download-permission\#example)

php

```
// Accessing Order
$order = $orderDownloadPermission->order;

// For Filtering by order relationship
$orderDownloadPermissions = FluentCart\App\Models\OrderDownloadPermission::whereHas('order', function($query) {
    $query->where('status', 'completed');
})->get();
```

### customer [​](https://dev.fluentcart.com/database/models/order-download-permission\#customer)

Access the associated customer

- return `FluentCart\App\Models\Customer` Model

#### Example: [​](https://dev.fluentcart.com/database/models/order-download-permission\#example-1)

php

```
// Accessing Customer
$customer = $orderDownloadPermission->customer;

// For Filtering by customer relationship
$orderDownloadPermissions = FluentCart\App\Models\OrderDownloadPermission::whereHas('customer', function($query) {
    $query->where('email', 'customer@example.com');
})->get();
```

## Usage Examples [​](https://dev.fluentcart.com/database/models/order-download-permission\#usage-examples)

### Get Order Download Permissions [​](https://dev.fluentcart.com/database/models/order-download-permission\#get-order-download-permissions)

php

```
$order = FluentCart\App\Models\Order::find(123);
$downloadPermissions = $order->download_permissions;

foreach ($downloadPermissions as $permission) {
    echo "Download ID: " . $permission->download_id;
    echo "Downloads Used: " . $permission->download_count . "/" . $permission->download_limit;
}
```

### Get Customer Download Permissions [​](https://dev.fluentcart.com/database/models/order-download-permission\#get-customer-download-permissions)

php

```
$customer = FluentCart\App\Models\Customer::find(456);
$downloadPermissions = $customer->download_permissions;

foreach ($downloadPermissions as $permission) {
    echo "Order ID: " . $permission->order_id;
    echo "Access Expires: " . $permission->access_expires;
}
```

### Create Download Permission [​](https://dev.fluentcart.com/database/models/order-download-permission\#create-download-permission)

php

```
$orderDownloadPermission = FluentCart\App\Models\OrderDownloadPermission::create([\
    'order_id' => 123,\
    'variation_id' => 789,\
    'customer_id' => 456,\
    'download_id' => 101,\
    'download_count' => 0,\
    'download_limit' => 5,\
    'access_expires' => now()->addDays(30)\
]);
```

### Check Download Access [​](https://dev.fluentcart.com/database/models/order-download-permission\#check-download-access)

php

```
$permission = FluentCart\App\Models\OrderDownloadPermission::find(1);

// Check if downloads are available
$canDownload = $permission->download_count < $permission->download_limit;

// Check if access is still valid
$isValid = $permission->access_expires > now();
```

### Get Active Download Permissions [​](https://dev.fluentcart.com/database/models/order-download-permission\#get-active-download-permissions)

php

```
$activePermissions = FluentCart\App\Models\OrderDownloadPermission::where('access_expires', '>', now())
    ->whereColumn('download_count', '<', 'download_limit')
    ->get();
```

* * *

Today

Hi! I’m your AI assistant. How can I assist you today?

Just now

Powered by **FluentBot**


---

---

## Order Item Model | FluentCart Developer Docs

**URL** : https://dev.fluentcart.com/database/models/order-item

[Skip to content](https://dev.fluentcart.com/database/models/order-item#VPContent)

# Order Item Model [​](https://dev.fluentcart.com/database/models/order-item\#order-item-model)

| DB Table Name | {wp\_db\_prefix}\_fct\_order\_items |
| --- | --- |
| Schema | [Check Schema](https://dev.fluentcart.com/database/schema.html#fct-order-items-table) |
| Source File | fluent-cart/app/Models/OrderItem.php |
| Name Space | FluentCart\\App\\Models |
| Class | FluentCart\\App\\Models\\OrderItem |

## Traits [​](https://dev.fluentcart.com/database/models/order-item\#traits)

| Trait | Description |
| --- | --- |
| CanSearch | Provides `search()`, `whereLike()`, `whereBeginsWith()`, `whereEndsWith()`, `groupSearch()` scopes |
| CanUpdateBatch | Provides `batchUpdate()` scope for bulk updates |

## Attributes [​](https://dev.fluentcart.com/database/models/order-item\#attributes)

| Attribute | Data Type | Comment |
| --- | --- | --- |
| id | Integer | Primary Key |
| order\_id | Integer | Reference to order |
| post\_id | Integer | WordPress post ID (product) |
| fulfillment\_type | String | Fulfillment type (physical, digital, service) |
| fulfilled\_quantity | Integer | Quantity fulfilled |
| post\_title | Text | Product title |
| title | Text | Item title (variation) |
| object\_id | Integer | Variation ID |
| cart\_index | Integer | Position in cart |
| quantity | Integer | Item quantity |
| unit\_price | Bigint | Price per unit in cents |
| cost | Bigint | Cost in cents |
| subtotal | Bigint | Line subtotal |
| tax\_amount | Bigint | Tax amount for this line |
| shipping\_charge | Bigint | Shipping charge (not in fillable) |
| discount\_total | Bigint | Discount amount |
| line\_total | Bigint | Total line amount |
| refund\_total | Bigint | Refunded amount |
| rate | Bigint | Exchange rate |
| other\_info | JSON | Additional item data (auto-encoded/decoded) |
| line\_meta | JSON | Line-specific metadata (auto-encoded/decoded) |
| referrer | Text | Referral information |
| object\_type | String | Object type |
| payment\_type | String | Payment type (onetime, subscription, signup\_fee) |
| created\_at | Date Time | Creation timestamp |
| updated\_at | Date Time | Last update timestamp |

## Casts [​](https://dev.fluentcart.com/database/models/order-item\#casts)

The following attributes are automatically cast to `double` when accessed:

| Attribute | Cast Type |
| --- | --- |
| unit\_price | double |
| cost | double |
| subtotal | double |
| tax\_amount | double |
| shipping\_charge | double |
| discount\_total | double |
| line\_total | double |
| refund\_total | double |

## Appends [​](https://dev.fluentcart.com/database/models/order-item\#appends)

The following virtual attributes are appended to the model:

| Append | Type | Description |
| --- | --- | --- |
| payment\_info | string | Subscription payment info (empty string if not a subscription) |
| setup\_info | string | Subscription setup fee info (empty string if not a subscription) |
| is\_custom | boolean | Whether the item is a custom item (from `other_info['is_custom']`) |
| formatted\_total | float | Decimal-formatted subtotal (appended via `booted()` on retrieval) |

## Usage [​](https://dev.fluentcart.com/database/models/order-item\#usage)

Please check [Model Basic](https://dev.fluentcart.com/database/models.html) for Common methods.

### Accessing Attributes [​](https://dev.fluentcart.com/database/models/order-item\#accessing-attributes)

php

```
$orderItem = FluentCart\App\Models\OrderItem::find(1);

$orderItem->id; // returns id
$orderItem->order_id; // returns order ID
$orderItem->quantity; // returns quantity
$orderItem->unit_price; // returns unit price (cast to double)
$orderItem->line_total; // returns line total (cast to double)
$orderItem->payment_info; // returns subscription payment info string
$orderItem->setup_info; // returns subscription setup info string
$orderItem->is_custom; // returns boolean
$orderItem->formatted_total; // returns decimal-formatted subtotal
$orderItem->full_name; // returns title + post_title combined
$orderItem->view_url; // returns view URL for custom items
```

## Relations [​](https://dev.fluentcart.com/database/models/order-item\#relations)

This model has the following relationships that you can use

### order [​](https://dev.fluentcart.com/database/models/order-item\#order)

Access the associated order

- Relation type: `belongsTo`
- return `FluentCart\App\Models\Order` Model
- Foreign key: `order_id`

#### Example: [​](https://dev.fluentcart.com/database/models/order-item\#example)

php

```
// Accessing Order
$order = $orderItem->order;

// For Filtering by order relationship
$orderItems = FluentCart\App\Models\OrderItem::whereHas('order', function($query) {
    $query->where('status', 'completed');
})->get();
```

### product [​](https://dev.fluentcart.com/database/models/order-item\#product)

Access the associated product

- Relation type: `belongsTo`
- return `FluentCart\App\Models\Product` Model
- Foreign key: `post_id` -\> `ID`

#### Example: [​](https://dev.fluentcart.com/database/models/order-item\#example-1)

php

```
// Accessing Product
$product = $orderItem->product;

// For Filtering by product relationship
$orderItems = FluentCart\App\Models\OrderItem::whereHas('product', function($query) {
    $query->where('post_status', 'publish');
})->get();
```

### variants [​](https://dev.fluentcart.com/database/models/order-item\#variants)

Access the associated product variation

- Relation type: `belongsTo`
- return `FluentCart\App\Models\ProductVariation` Model
- Foreign key: `object_id` -\> `id`

#### Example: [​](https://dev.fluentcart.com/database/models/order-item\#example-2)

php

```
// Accessing Product Variation
$variation = $orderItem->variants;
```

### product\_downloads [​](https://dev.fluentcart.com/database/models/order-item\#product-downloads)

Access the associated product downloads

- Relation type: `belongsTo`
- return `FluentCart\App\Models\ProductDownload` Model
- Foreign key: `post_id` -\> `post_id`

#### Example: [​](https://dev.fluentcart.com/database/models/order-item\#example-3)

php

```
// Accessing Product Downloads
$downloads = $orderItem->product_downloads;
```

### productImage [​](https://dev.fluentcart.com/database/models/order-item\#productimage)

Access the product gallery image via WordPress post meta

- Relation type: `hasOne`
- return `FluentCart\App\Models\WpModels\PostMeta` Model
- Foreign key: `post_id` -\> `post_id`
- Condition: `postmeta.meta_key = 'fluent-products-gallery-image'`

#### Example: [​](https://dev.fluentcart.com/database/models/order-item\#example-4)

php

```
// Accessing Product Image
$image = $orderItem->productImage;
```

### variantImages [​](https://dev.fluentcart.com/database/models/order-item\#variantimages)

Access the variant thumbnail image via product meta

- Relation type: `hasOne`
- return `FluentCart\App\Models\ProductMeta` Model
- Foreign key: `object_id` -\> `object_id`
- Conditions: `object_type = 'product_variant_info'` and `meta_key = 'product_thumbnail'`

#### Example: [​](https://dev.fluentcart.com/database/models/order-item\#example-5)

php

```
// Accessing Variant Image
$variantImage = $orderItem->variantImages;
```

## Methods [​](https://dev.fluentcart.com/database/models/order-item\#methods)

Along with Global Model methods, this model has few helper methods.

### getFormattedTotalAttribute() [​](https://dev.fluentcart.com/database/models/order-item\#getformattedtotalattribute)

Get formatted line total as a decimal value (accessor). This attribute is appended automatically when the model is retrieved from the database via the `booted()` method.

- Parameters
  - none
- Returns `float`

#### Usage [​](https://dev.fluentcart.com/database/models/order-item\#usage-1)

php

```
$formattedTotal = $orderItem->formatted_total; // Returns: 99.99
```

### getPaymentInfoAttribute() [​](https://dev.fluentcart.com/database/models/order-item\#getpaymentinfoattribute)

Get subscription payment info string. Returns an empty string if the item's `payment_type` is not `subscription`. For subscription items, delegates to `Helper::generateSubscriptionInfo()` using `other_info` and `unit_price`.

- Parameters
  - none
- Returns `string`

#### Usage [​](https://dev.fluentcart.com/database/models/order-item\#usage-2)

php

```
$paymentInfo = $orderItem->payment_info; // e.g. "$9.99 / month"
```

### getSetupInfoAttribute() [​](https://dev.fluentcart.com/database/models/order-item\#getsetupinfoattribute)

Get subscription setup fee info string. Returns an empty string if the item's `payment_type` is not `subscription`. For subscription items, delegates to `Helper::generateSetupFeeInfo()` using `other_info`.

- Parameters
  - none
- Returns `string`

#### Usage [​](https://dev.fluentcart.com/database/models/order-item\#usage-3)

php

```
$setupInfo = $orderItem->setup_info; // e.g. "$19.99 setup fee"
```

### getIsCustomAttribute() [​](https://dev.fluentcart.com/database/models/order-item\#getiscustomattribute)

Check if this is a custom item (accessor). Reads the `is_custom` key from the `other_info` JSON field.

- Parameters
  - none
- Returns `boolean`

#### Usage [​](https://dev.fluentcart.com/database/models/order-item\#usage-4)

php

```
$isCustom = $orderItem->is_custom; // Returns: true or false
```

### getViewUrlAttribute() [​](https://dev.fluentcart.com/database/models/order-item\#getviewurlattribute)

Get the view URL for custom items (accessor). Returns an empty string for non-custom items.

- Parameters
  - none
- Returns `string`

#### Usage [​](https://dev.fluentcart.com/database/models/order-item\#usage-5)

php

```
$viewUrl = $orderItem->view_url; // Returns URL string or empty string
```

### getFullNameAttribute() [​](https://dev.fluentcart.com/database/models/order-item\#getfullnameattribute)

Get the full name by combining the item title and product title.

- Parameters
  - none
- Returns `string`

#### Usage [​](https://dev.fluentcart.com/database/models/order-item\#usage-6)

php

```
$fullName = $orderItem->full_name; // Returns: "Variation Name Product Title"
```

### getOtherInfoAttribute($value) [​](https://dev.fluentcart.com/database/models/order-item\#getotherinfoattribute-value)

Get other info as array (accessor). Automatically decodes the JSON string stored in the database.

- Parameters
  - $value - mixed (raw database value)
- Returns `array`

#### Usage [​](https://dev.fluentcart.com/database/models/order-item\#usage-7)

php

```
$otherInfo = $orderItem->other_info; // Returns array
```

### setOtherInfoAttribute($value) [​](https://dev.fluentcart.com/database/models/order-item\#setotherinfoattribute-value)

Set other info from array (mutator). Automatically encodes arrays/objects to JSON for storage.

- Parameters
  - $value - array\|object\|string
- Returns `void`

#### Usage [​](https://dev.fluentcart.com/database/models/order-item\#usage-8)

php

```
$orderItem->other_info = ['custom_field' => 'value'];
```

### getLineMetaAttribute($value) [​](https://dev.fluentcart.com/database/models/order-item\#getlinemetaattribute-value)

Get line meta as array (accessor). Automatically decodes the JSON string stored in the database.

- Parameters
  - $value - mixed (raw database value)
- Returns `array`

#### Usage [​](https://dev.fluentcart.com/database/models/order-item\#usage-9)

php

```
$lineMeta = $orderItem->line_meta; // Returns array
```

### setLineMetaAttribute($value) [​](https://dev.fluentcart.com/database/models/order-item\#setlinemetaattribute-value)

Set line meta from array (mutator). Automatically encodes arrays/objects to JSON for storage.

- Parameters
  - $value - array\|object
- Returns `void`

#### Usage [​](https://dev.fluentcart.com/database/models/order-item\#usage-10)

php

```
$orderItem->line_meta = ['custom_meta' => 'value'];
```

### processCustom($product, $orderId) [​](https://dev.fluentcart.com/database/models/order-item\#processcustom-product-orderid)

Process a custom item for an order. Delegates to `OrderItemHelper::processCustom()`.

- Parameters
  - $product - mixed (product data)
  - $orderId - integer (order ID)
- Returns `mixed`

#### Usage [​](https://dev.fluentcart.com/database/models/order-item\#usage-11)

php

```
$orderItem = new FluentCart\App\Models\OrderItem();
$result = $orderItem->processCustom($productData, 123);
```

### createItem($orderItems) [​](https://dev.fluentcart.com/database/models/order-item\#createitem-orderitems)

Create an item (note: the method body returns a `belongsTo` relation to `ProductVariation` via `variation_id`).

- Parameters
  - $orderItems - mixed
- Returns `BelongsTo` relation to `FluentCart\App\Models\ProductVariation`

* * *

Today

Hi! I’m your AI assistant. How can I assist you today?

Just now

Powered by **FluentBot**


---

---

