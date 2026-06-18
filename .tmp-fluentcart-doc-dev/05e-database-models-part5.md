# FluentCart Developer Docs - Database Models (Part 5/8)

Tous les modèles Eloquent exposés par FluentCart : orders, customers, products, subscriptions, coupons, licenses, taxes, shipping, etc.

---

## Order Meta Model | FluentCart Developer Docs

**URL** : https://dev.fluentcart.com/database/models/order-meta

[Skip to content](https://dev.fluentcart.com/database/models/order-meta#VPContent)

# Order Meta Model [​](https://dev.fluentcart.com/database/models/order-meta\#order-meta-model)

| DB Table Name | {wp\_db\_prefix}\_fct\_order\_meta |
| --- | --- |
| Schema | [Check Schema](https://dev.fluentcart.com/database/schema.html#fct-order-meta-table) |
| Source File | fluent-cart/app/Models/OrderMeta.php |
| Name Space | FluentCart\\App\\Models |
| Class | FluentCart\\App\\Models\\OrderMeta |

## Traits [​](https://dev.fluentcart.com/database/models/order-meta\#traits)

- **CanSearch** \- Provides `search()`, `whereLike()`, `whereBeginsWith()`, `whereEndsWith()`, and `groupSearch()` scopes

## Attributes [​](https://dev.fluentcart.com/database/models/order-meta\#attributes)

| Attribute | Data Type | Comment |
| --- | --- | --- |
| id | Integer | Primary Key |
| order\_id | Integer | Reference to order |
| meta\_key | String | Meta key name |
| meta\_value | Text | Meta value (JSON or string) |
| created\_at | Date Time | Creation timestamp |
| updated\_at | Date Time | Last update timestamp |

## Usage [​](https://dev.fluentcart.com/database/models/order-meta\#usage)

Please check [Model Basic](https://dev.fluentcart.com/database/models.html) for Common methods.

### Accessing Attributes [​](https://dev.fluentcart.com/database/models/order-meta\#accessing-attributes)

php

```
$orderMeta = FluentCart\App\Models\OrderMeta::find(1);

$orderMeta->id; // returns id
$orderMeta->order_id; // returns order ID
$orderMeta->meta_key; // returns meta key
$orderMeta->meta_value; // returns meta value (auto-decoded if JSON)
```

## Scopes [​](https://dev.fluentcart.com/database/models/order-meta\#scopes)

This model has the following scopes via the `CanSearch` trait.

### search($params) [​](https://dev.fluentcart.com/database/models/order-meta\#search-params)

Perform a parameterized search with various operators (=, like\_all, between, in, not\_in, etc.).

- Parameters
  - $params - array of search parameters

#### Usage: [​](https://dev.fluentcart.com/database/models/order-meta\#usage-1)

php

```
$orderMeta = FluentCart\App\Models\OrderMeta::search([\
    'meta_key' => 'billing_address',\
])->get();
```

### whereLike($column, $value, $boolean = 'and') [​](https://dev.fluentcart.com/database/models/order-meta\#wherelike-column-value-boolean-and)

Filter with a WHERE LIKE %value% query.

- Parameters
  - $column - string
  - $value - string
  - $boolean - string (default: 'and')

#### Usage: [​](https://dev.fluentcart.com/database/models/order-meta\#usage-2)

php

```
$orderMeta = FluentCart\App\Models\OrderMeta::whereLike('meta_key', 'billing')->get();
```

### whereBeginsWith($column, $value, $boolean = 'and') [​](https://dev.fluentcart.com/database/models/order-meta\#wherebeginswith-column-value-boolean-and)

Filter with a WHERE LIKE value% query.

- Parameters
  - $column - string
  - $value - string
  - $boolean - string (default: 'and')

#### Usage: [​](https://dev.fluentcart.com/database/models/order-meta\#usage-3)

php

```
$orderMeta = FluentCart\App\Models\OrderMeta::whereBeginsWith('meta_key', 'shipping_')->get();
```

### whereEndsWith($column, $value, $boolean = 'and') [​](https://dev.fluentcart.com/database/models/order-meta\#whereendswith-column-value-boolean-and)

Filter with a WHERE LIKE %value query.

- Parameters
  - $column - string
  - $value - string
  - $boolean - string (default: 'and')

#### Usage: [​](https://dev.fluentcart.com/database/models/order-meta\#usage-4)

php

```
$orderMeta = FluentCart\App\Models\OrderMeta::whereEndsWith('meta_key', '_address')->get();
```

### groupSearch($groups) [​](https://dev.fluentcart.com/database/models/order-meta\#groupsearch-groups)

Perform grouped searches across the model and its relationships.

- Parameters
  - $groups - array of grouped search parameters

#### Usage: [​](https://dev.fluentcart.com/database/models/order-meta\#usage-5)

php

```
$orderMeta = FluentCart\App\Models\OrderMeta::groupSearch([\
    'OrderMeta.meta_key' => [\
        'column' => 'meta_key',\
        'operator' => '=',\
        'value' => 'billing_address'\
    ],\
])->get();
```

## Relations [​](https://dev.fluentcart.com/database/models/order-meta\#relations)

This model has the following relationships that you can use

### order [​](https://dev.fluentcart.com/database/models/order-meta\#order)

Access the associated order

- return `FluentCart\App\Models\Order` Model

#### Example: [​](https://dev.fluentcart.com/database/models/order-meta\#example)

php

```
// Accessing Order
$order = $orderMeta->order;

// For Filtering by order relationship
$orderMeta = FluentCart\App\Models\OrderMeta::whereHas('order', function($query) {
    $query->where('status', 'completed');
})->get();
```

## Methods [​](https://dev.fluentcart.com/database/models/order-meta\#methods)

Along with Global Model methods, this model has few helper methods.

### setMetaValueAttribute($value) [​](https://dev.fluentcart.com/database/models/order-meta\#setmetavalueattribute-value)

Set meta value with automatic JSON encoding for arrays and objects (mutator). Uses `JSON_UNESCAPED_UNICODE | JSON_UNESCAPED_SLASHES` flags.

- Parameters
  - $value - array\|object\|string
- Returns `void`

#### Usage [​](https://dev.fluentcart.com/database/models/order-meta\#usage-6)

php

```
// Set array value (will be JSON encoded)
$orderMeta->meta_value = ['address' => '123 Main St', 'city' => 'New York'];

// Set string value
$orderMeta->meta_value = 'simple string value';
```

### getMetaValueAttribute($value) [​](https://dev.fluentcart.com/database/models/order-meta\#getmetavalueattribute-value)

Get meta value with automatic JSON decoding (accessor). Returns the decoded array if the value is valid JSON, otherwise returns the original string.

- Parameters
  - $value - mixed
- Returns `mixed` \- array if valid JSON, original string otherwise

#### Usage [​](https://dev.fluentcart.com/database/models/order-meta\#usage-7)

php

```
$metaValue = $orderMeta->meta_value; // Returns array if JSON, string otherwise
```

### updateMeta($metaKey, $metaValue) [​](https://dev.fluentcart.com/database/models/order-meta\#updatemeta-metakey-metavalue)

Create or update a meta entry for the current order. If a record with the same `order_id` and `meta_key` exists, it updates the value; otherwise, it creates a new record.

- Parameters
  - $metaKey - string
  - $metaValue - mixed
- Returns `FluentCart\App\Models\OrderMeta`

#### Usage [​](https://dev.fluentcart.com/database/models/order-meta\#usage-8)

php

```
$orderMeta = FluentCart\App\Models\OrderMeta::find(1);
$result = $orderMeta->updateMeta('custom_field', ['key' => 'value']);
```

## Common Meta Keys [​](https://dev.fluentcart.com/database/models/order-meta\#common-meta-keys)

Here are some common meta keys used in FluentCart:

### Billing Information [​](https://dev.fluentcart.com/database/models/order-meta\#billing-information)

- `billing_address` \- Billing address data
- `billing_first_name` \- Billing first name
- `billing_last_name` \- Billing last name
- `billing_company` \- Billing company
- `billing_address_1` \- Billing address line 1
- `billing_address_2` \- Billing address line 2
- `billing_city` \- Billing city
- `billing_state` \- Billing state
- `billing_postcode` \- Billing postal code
- `billing_country` \- Billing country
- `billing_phone` \- Billing phone number
- `billing_email` \- Billing email

### Shipping Information [​](https://dev.fluentcart.com/database/models/order-meta\#shipping-information)

- `shipping_address` \- Shipping address data
- `shipping_first_name` \- Shipping first name
- `shipping_last_name` \- Shipping last name
- `shipping_company` \- Shipping company
- `shipping_address_1` \- Shipping address line 1
- `shipping_address_2` \- Shipping address line 2
- `shipping_city` \- Shipping city
- `shipping_state` \- Shipping state
- `shipping_postcode` \- Shipping postal code
- `shipping_country` \- Shipping country
- `shipping_phone` \- Shipping phone number

### Order Information [​](https://dev.fluentcart.com/database/models/order-meta\#order-information)

- `order_notes` \- Order notes
- `customer_notes` \- Customer notes
- `admin_notes` \- Admin notes
- `payment_method` \- Payment method used
- `payment_method_title` \- Payment method display name
- `transaction_id` \- Payment transaction ID
- `gateway_transaction_id` \- Gateway transaction ID
- `gateway_order_id` \- Gateway order ID

### Subscription Information [​](https://dev.fluentcart.com/database/models/order-meta\#subscription-information)

- `subscription_id` \- Associated subscription ID
- `subscription_status` \- Subscription status
- `next_payment_date` \- Next payment date
- `subscription_interval` \- Subscription interval

### Custom Fields [​](https://dev.fluentcart.com/database/models/order-meta\#custom-fields)

- `custom_field_*` \- Custom field values
- `_custom_*` \- Custom meta fields

## Usage Examples [​](https://dev.fluentcart.com/database/models/order-meta\#usage-examples)

### Get Order Billing Address [​](https://dev.fluentcart.com/database/models/order-meta\#get-order-billing-address)

php

```
$order = FluentCart\App\Models\Order::find(123);
$billingAddress = $order->meta()->where('meta_key', 'billing_address')->first();

if ($billingAddress) {
    $address = $billingAddress->meta_value; // Returns array
    echo $address['address_1'] . ', ' . $address['city'];
}
```

### Set Order Custom Meta [​](https://dev.fluentcart.com/database/models/order-meta\#set-order-custom-meta)

php

```
$order = FluentCart\App\Models\Order::find(123);

// Set custom meta
$order->meta()->updateOrCreate(
    ['meta_key' => 'custom_field'],
    ['meta_value' => ['value' => 'custom data', 'type' => 'text']]
);
```

### Update Meta via updateMeta() [​](https://dev.fluentcart.com/database/models/order-meta\#update-meta-via-updatemeta)

php

```
$orderMeta = FluentCart\App\Models\OrderMeta::where('order_id', 123)->first();
$orderMeta->updateMeta('shipping_notes', 'Leave at front door');
```

### Get All Order Meta as Key-Value Array [​](https://dev.fluentcart.com/database/models/order-meta\#get-all-order-meta-as-key-value-array)

php

```
$order = FluentCart\App\Models\Order::find(123);
$metaData = $order->meta()->pluck('meta_value', 'meta_key')->toArray();
```

* * *

Today

Hi! I’m your AI assistant. How can I assist you today?

Just now

Powered by **FluentBot**


---

---

## Order Operation Model | FluentCart Developer Docs

**URL** : https://dev.fluentcart.com/database/models/order-operation

[Skip to content](https://dev.fluentcart.com/database/models/order-operation#VPContent)

# Order Operation Model [​](https://dev.fluentcart.com/database/models/order-operation\#order-operation-model)

| DB Table Name | {wp\_db\_prefix}\_fct\_order\_operations |
| --- | --- |
| Schema | [Check Schema](https://dev.fluentcart.com/database/schema.html#fct-order-operations-table) |
| Source File | fluent-cart/app/Models/OrderOperation.php |
| Name Space | FluentCart\\App\\Models |
| Class | FluentCart\\App\\Models\\OrderOperation |

## Attributes [​](https://dev.fluentcart.com/database/models/order-operation\#attributes)

| Attribute | Data Type | Comment |
| --- | --- | --- |
| id | Integer | Primary Key (guarded) |
| order\_id | Integer | Reference to order |
| created\_via | String | How the order was created |
| has\_tax | Boolean | Whether order has tax |
| has\_discount | Boolean | Whether order has discount |
| coupons\_counted | Integer | Number of coupons applied |
| emails\_sent | Integer | Number of emails sent |
| sales\_recorded | Boolean | Whether sales were recorded |
| utm\_campaign | String | UTM campaign parameter |
| utm\_term | String | UTM term parameter |
| utm\_source | String | UTM source parameter |
| utm\_content | String | UTM content parameter |
| utm\_medium | String | UTM medium parameter |
| utm\_id | String | UTM ID parameter |
| cart\_hash | String | Cart hash identifier |
| refer\_url | String | Referral URL |
| meta | JSON | Additional operation data (has accessor/mutator but not in $fillable) |
| created\_at | Date Time | Creation timestamp |
| updated\_at | Date Time | Last update timestamp |

> **Note:** The `meta` column has accessor/mutator methods for JSON encoding/decoding but is not included in `$fillable`. It must be set directly on the model instance. The `id` column is both guarded and declared as `$primaryKey`.

## Usage [​](https://dev.fluentcart.com/database/models/order-operation\#usage)

Please check [Model Basic](https://dev.fluentcart.com/database/models.html) for Common methods.

### Accessing Attributes [​](https://dev.fluentcart.com/database/models/order-operation\#accessing-attributes)

php

```
$orderOperation = FluentCart\App\Models\OrderOperation::find(1);

$orderOperation->id; // returns id
$orderOperation->order_id; // returns order ID
$orderOperation->created_via; // returns creation method
$orderOperation->has_tax; // returns tax status
```

## Relations [​](https://dev.fluentcart.com/database/models/order-operation\#relations)

This model has the following relationships that you can use

### order [​](https://dev.fluentcart.com/database/models/order-operation\#order)

Access the associated order

- return `FluentCart\App\Models\Order` Model

#### Example: [​](https://dev.fluentcart.com/database/models/order-operation\#example)

php

```
// Accessing Order
$order = $orderOperation->order;

// For Filtering by order relationship
$orderOperations = FluentCart\App\Models\OrderOperation::whereHas('order', function($query) {
    $query->where('status', 'completed');
})->get();
```

## Methods [​](https://dev.fluentcart.com/database/models/order-operation\#methods)

Along with Global Model methods, this model has few helper methods.

### setMetaAttribute($value) [​](https://dev.fluentcart.com/database/models/order-operation\#setmetaattribute-value)

Set meta from array (mutator). Automatically JSON-encodes the value.

- Parameters
  - $value - array\|object
- Returns `void`

#### Usage [​](https://dev.fluentcart.com/database/models/order-operation\#usage-1)

php

```
$orderOperation->meta = ['analytics_data' => 'value', 'tracking_info' => 'data'];
```

### getMetaAttribute($value) [​](https://dev.fluentcart.com/database/models/order-operation\#getmetaattribute-value)

Get meta as array (accessor). Automatically JSON-decodes the stored value.

- Parameters
  - $value - mixed
- Returns `array`

#### Usage [​](https://dev.fluentcart.com/database/models/order-operation\#usage-2)

php

```
$meta = $orderOperation->meta; // Returns array
```

## Usage Examples [​](https://dev.fluentcart.com/database/models/order-operation\#usage-examples)

### Get Order Operations [​](https://dev.fluentcart.com/database/models/order-operation\#get-order-operations)

php

```
$order = FluentCart\App\Models\Order::find(123);
$operations = $order->order_operations;

foreach ($operations as $operation) {
    echo "Created via: " . $operation->created_via;
    echo "UTM Campaign: " . $operation->utm_campaign;
}
```

### Get Operations by UTM Source [​](https://dev.fluentcart.com/database/models/order-operation\#get-operations-by-utm-source)

php

```
$googleOperations = FluentCart\App\Models\OrderOperation::where('utm_source', 'google')->get();
$facebookOperations = FluentCart\App\Models\OrderOperation::where('utm_source', 'facebook')->get();
```

### Create Order Operation [​](https://dev.fluentcart.com/database/models/order-operation\#create-order-operation)

php

```
$orderOperation = FluentCart\App\Models\OrderOperation::create([\
    'order_id' => 123,\
    'created_via' => 'checkout',\
    'has_tax' => true,\
    'has_discount' => true,\
    'coupons_counted' => 2,\
    'emails_sent' => 3,\
    'sales_recorded' => true,\
    'utm_campaign' => 'summer_sale',\
    'utm_source' => 'google',\
    'utm_medium' => 'cpc',\
    'cart_hash' => 'abc123def456',\
    'refer_url' => 'https://example.com/products'\
]);
```

### Track UTM Parameters [​](https://dev.fluentcart.com/database/models/order-operation\#track-utm-parameters)

php

```
$orderOperation = FluentCart\App\Models\OrderOperation::create([\
    'order_id' => 123,\
    'utm_campaign' => 'black_friday',\
    'utm_source' => 'facebook',\
    'utm_medium' => 'social',\
    'utm_content' => 'banner_ad',\
    'utm_term' => 'discount',\
    'utm_id' => 'fb_123'\
]);
```

* * *

Today

Hi! I’m your AI assistant. How can I assist you today?

Just now

Powered by **FluentBot**


---

---

## Order Promotion Model | FluentCart Developer Docs

**URL** : https://dev.fluentcart.com/database/models/order-promotion

[Skip to content](https://dev.fluentcart.com/database/models/order-promotion#VPContent)

Pro

# Order Promotion Model [​](https://dev.fluentcart.com/database/models/order-promotion\#order-promotion-model)

| DB Table Name | {wp\_db\_prefix}\_fct\_order\_promotions |
| --- | --- |
| Schema | [Check Schema](https://dev.fluentcart.com/database/schema.html#fct-order-promotions-table) |
| Source File | fluent-cart-pro/app/Modules/Promotional/Models/OrderPromotion.php |
| Name Space | FluentCartPro\\App\\Modules\\Promotional\\Models |
| Class | FluentCartPro\\App\\Modules\\Promotional\\Models\\OrderPromotion |
| Plugin | FluentCart Pro |

## Properties [​](https://dev.fluentcart.com/database/models/order-promotion\#properties)

- **Table**: `fct_order_promotions`
- **Primary Key**: `id`
- **Guarded**: `['id']`
- **Fillable**: `['hash', 'parent_id', 'type', 'status', 'src_object_id', 'src_object_type', 'title', 'description', 'conditions', 'config', 'priority']`

## Boot Logic [​](https://dev.fluentcart.com/database/models/order-promotion\#boot-logic)

The model registers a `creating` event that auto-generates a `hash` (using `md5('fct_promotion_' . wp_generate_uuid4() . time())`) if one is not provided, and defaults empty `conditions` and `config` to empty JSON arrays.

## Attributes [​](https://dev.fluentcart.com/database/models/order-promotion\#attributes)

| Attribute | Data Type | Comment |
| --- | --- | --- |
| id | Integer | Primary Key |
| hash | String | Unique promotion hash (auto-generated on creation) |
| parent\_id | Integer | Parent promotion ID |
| type | String | Promotion type |
| status | String | Promotion status |
| src\_object\_id | Integer | Source object ID |
| src\_object\_type | String | Source object type |
| title | String | Promotion title |
| description | Text | Promotion description |
| conditions | JSON | Promotion conditions (auto JSON encode/decode via accessor/mutator) |
| config | JSON | Promotion configuration (auto JSON encode/decode via accessor/mutator) |
| priority | Integer | Promotion priority |
| created\_at | Date Time | Creation timestamp |
| updated\_at | Date Time | Last update timestamp |

## Usage [​](https://dev.fluentcart.com/database/models/order-promotion\#usage)

Please check [Model Basic](https://dev.fluentcart.com/database/models.html) for Common methods.

### Accessing Attributes [​](https://dev.fluentcart.com/database/models/order-promotion\#accessing-attributes)

php

```
$orderPromotion = FluentCartPro\App\Modules\Promotional\Models\OrderPromotion::find(1);

$orderPromotion->id; // returns id
$orderPromotion->hash; // returns hash
$orderPromotion->type; // returns type
$orderPromotion->status; // returns status
$orderPromotion->conditions; // returns decoded array
$orderPromotion->config; // returns decoded array
```

## Relations [​](https://dev.fluentcart.com/database/models/order-promotion\#relations)

This model has the following relationships that you can use

### product\_variant [​](https://dev.fluentcart.com/database/models/order-promotion\#product-variant)

Access the associated product variant (BelongsTo via `src_object_id`)

- return `FluentCart\App\Models\ProductVariation` Model

#### Example: [​](https://dev.fluentcart.com/database/models/order-promotion\#example)

php

```
// Accessing Product Variant
$productVariant = $orderPromotion->product_variant;

// For Filtering by product variant relationship
$orderPromotions = FluentCartPro\App\Modules\Promotional\Models\OrderPromotion::whereHas('product_variant', function($query) {
    $query->where('status', 'active');
})->get();
```

## Methods [​](https://dev.fluentcart.com/database/models/order-promotion\#methods)

Along with Global Model methods, this model has few helper methods.

### setConditionsAttribute($value) [​](https://dev.fluentcart.com/database/models/order-promotion\#setconditionsattribute-value)

Set conditions with automatic JSON encoding (mutator). Arrays and objects are JSON encoded before storage.

- Parameters
  - $value - mixed (array, object, or string)
- Returns `void`

#### Usage [​](https://dev.fluentcart.com/database/models/order-promotion\#usage-1)

php

```
$orderPromotion->conditions = ['min_amount' => 100, 'product_ids' => [1, 2, 3]];
// Automatically JSON encodes arrays and objects
```

### getConditionsAttribute($value) [​](https://dev.fluentcart.com/database/models/order-promotion\#getconditionsattribute-value)

Get conditions with automatic JSON decoding (accessor). If the stored value is a JSON string, it is decoded to an array.

- Parameters
  - $value - mixed
- Returns `mixed` \- array if JSON string, otherwise original value

#### Usage [​](https://dev.fluentcart.com/database/models/order-promotion\#usage-2)

php

```
$conditions = $orderPromotion->conditions; // Returns decoded array
```

### setConfigAttribute($value) [​](https://dev.fluentcart.com/database/models/order-promotion\#setconfigattribute-value)

Set config with automatic JSON encoding (mutator). Arrays and objects are JSON encoded before storage.

- Parameters
  - $value - mixed (array, object, or string)
- Returns `void`

#### Usage [​](https://dev.fluentcart.com/database/models/order-promotion\#usage-3)

php

```
$orderPromotion->config = ['discount_type' => 'percentage', 'discount_value' => 10];
// Automatically JSON encodes arrays and objects
```

### getConfigAttribute($value) [​](https://dev.fluentcart.com/database/models/order-promotion\#getconfigattribute-value)

Get config with automatic JSON decoding (accessor). If the stored value is a JSON string, it is decoded to an array.

- Parameters
  - $value - mixed
- Returns `mixed` \- array if JSON string, otherwise original value

#### Usage [​](https://dev.fluentcart.com/database/models/order-promotion\#usage-4)

php

```
$config = $orderPromotion->config; // Returns decoded array
```

## Usage Examples [​](https://dev.fluentcart.com/database/models/order-promotion\#usage-examples)

### Create Order Promotion [​](https://dev.fluentcart.com/database/models/order-promotion\#create-order-promotion)

php

```
$orderPromotion = FluentCartPro\App\Modules\Promotional\Models\OrderPromotion::create([\
    'type' => 'order_bump',\
    'status' => 'active',\
    'src_object_id' => 123,\
    'src_object_type' => 'product_variation',\
    'title' => 'Add-on Product',\
    'description' => 'Enhance your order with this add-on',\
    'conditions' => [\
        'min_amount' => 50,\
        'product_ids' => [1, 2, 3]\
    ],\
    'config' => [\
        'discount_type' => 'percentage',\
        'discount_value' => 15,\
        'display_position' => 'checkout'\
    ],\
    'priority' => 1\
]);
// Hash is automatically generated during creation
```

### Get Active Promotions [​](https://dev.fluentcart.com/database/models/order-promotion\#get-active-promotions)

php

```
$activePromotions = FluentCartPro\App\Modules\Promotional\Models\OrderPromotion::where('status', 'active')->get();
```

### Get Promotions by Type [​](https://dev.fluentcart.com/database/models/order-promotion\#get-promotions-by-type)

php

```
$orderBumps = FluentCartPro\App\Modules\Promotional\Models\OrderPromotion::where('type', 'order_bump')->get();
$upsells = FluentCartPro\App\Modules\Promotional\Models\OrderPromotion::where('type', 'upsell')->get();
```

### Get Promotions with Product Variants [​](https://dev.fluentcart.com/database/models/order-promotion\#get-promotions-with-product-variants)

php

```
$promotionsWithVariants = FluentCartPro\App\Modules\Promotional\Models\OrderPromotion::with('product_variant')->get();

foreach ($promotionsWithVariants as $promotion) {
    echo "Promotion: " . $promotion->title;
    if ($promotion->product_variant) {
        echo "Product: " . $promotion->product_variant->variation_title;
    }
}
```

### Get Promotions by Priority [​](https://dev.fluentcart.com/database/models/order-promotion\#get-promotions-by-priority)

php

```
$orderedPromotions = FluentCartPro\App\Modules\Promotional\Models\OrderPromotion::orderBy('priority', 'asc')->get();
```

### Update Order Promotion [​](https://dev.fluentcart.com/database/models/order-promotion\#update-order-promotion)

php

```
$orderPromotion = FluentCartPro\App\Modules\Promotional\Models\OrderPromotion::find(1);
$orderPromotion->update([\
    'status' => 'inactive',\
    'config' => ['discount_value' => 20, 'updated' => true]\
]);
```

### Get Promotions by Source Object [​](https://dev.fluentcart.com/database/models/order-promotion\#get-promotions-by-source-object)

php

```
$promotions = FluentCartPro\App\Modules\Promotional\Models\OrderPromotion::where('src_object_type', 'product_variation')
    ->where('src_object_id', 123)
    ->get();
```

### Get Promotions by Hash [​](https://dev.fluentcart.com/database/models/order-promotion\#get-promotions-by-hash)

php

```
$promotion = FluentCartPro\App\Modules\Promotional\Models\OrderPromotion::where('hash', 'abc123def456')->first();
```

### Delete Order Promotion [​](https://dev.fluentcart.com/database/models/order-promotion\#delete-order-promotion)

php

```
$orderPromotion = FluentCartPro\App\Modules\Promotional\Models\OrderPromotion::find(1);
$orderPromotion->delete();
```

### Get Promotions with Conditions [​](https://dev.fluentcart.com/database/models/order-promotion\#get-promotions-with-conditions)

php

```
$promotions = FluentCartPro\App\Modules\Promotional\Models\OrderPromotion::all();

foreach ($promotions as $promotion) {
    $conditions = $promotion->conditions;
    if (isset($conditions['min_amount'])) {
        echo "Min Amount: " . $conditions['min_amount'];
    }
}
```

* * *

**Plugin**: FluentCart Pro

Today

Hi! I’m your AI assistant. How can I assist you today?

Just now

Powered by **FluentBot**


---

---

## Order Promotion Stat Model | FluentCart Developer Docs

**URL** : https://dev.fluentcart.com/database/models/order-promotion-stat

[Skip to content](https://dev.fluentcart.com/database/models/order-promotion-stat#VPContent)

Pro

# Order Promotion Stat Model [​](https://dev.fluentcart.com/database/models/order-promotion-stat\#order-promotion-stat-model)

| DB Table Name | {wp\_db\_prefix}\_fct\_order\_promotion\_stats |
| --- | --- |
| Schema | [Check Schema](https://dev.fluentcart.com/database/schema.html#fct-order-promotion-stats-table) |
| Source File | fluent-cart-pro/app/Modules/Promotional/Models/OrderPromotionStat.php |
| Name Space | FluentCartPro\\App\\Modules\\Promotional\\Models |
| Class | FluentCartPro\\App\\Modules\\Promotional\\Models\\OrderPromotionStat |
| Plugin | FluentCart Pro |

## Properties [​](https://dev.fluentcart.com/database/models/order-promotion-stat\#properties)

- **Table**: `fct_order_promotion_stats`
- **Primary Key**: `id`
- **Guarded**: `['id']`
- **Fillable**: `['promotion_id', 'order_id', 'object_id', 'amount', 'status']`

## Attributes [​](https://dev.fluentcart.com/database/models/order-promotion-stat\#attributes)

| Attribute | Data Type | Comment |
| --- | --- | --- |
| id | Integer | Primary Key |
| promotion\_id | Integer | Reference to order promotion |
| order\_id | Integer | Reference to order |
| object\_id | Integer | Reference to object (product, variation, etc.) |
| amount | Decimal | Promotion amount |
| status | String | Promotion status |
| created\_at | Date Time | Creation timestamp |
| updated\_at | Date Time | Last update timestamp |

## Usage [​](https://dev.fluentcart.com/database/models/order-promotion-stat\#usage)

Please check [Model Basic](https://dev.fluentcart.com/database/models.html) for Common methods.

### Accessing Attributes [​](https://dev.fluentcart.com/database/models/order-promotion-stat\#accessing-attributes)

php

```
$orderPromotionStat = FluentCartPro\App\Modules\Promotional\Models\OrderPromotionStat::find(1);

$orderPromotionStat->id; // returns id
$orderPromotionStat->promotion_id; // returns promotion ID
$orderPromotionStat->order_id; // returns order ID
$orderPromotionStat->object_id; // returns object ID
$orderPromotionStat->amount; // returns amount
$orderPromotionStat->status; // returns status
```

## Relations [​](https://dev.fluentcart.com/database/models/order-promotion-stat\#relations)

This model has the following relationships that you can use

### order [​](https://dev.fluentcart.com/database/models/order-promotion-stat\#order)

Access the associated order (BelongsTo)

- return `FluentCart\App\Models\Order` Model

#### Example: [​](https://dev.fluentcart.com/database/models/order-promotion-stat\#example)

php

```
// Accessing Order
$order = $orderPromotionStat->order;

// For Filtering by order relationship
$orderPromotionStats = FluentCartPro\App\Modules\Promotional\Models\OrderPromotionStat::whereHas('order', function($query) {
    $query->where('status', 'completed');
})->get();
```

### promotion [​](https://dev.fluentcart.com/database/models/order-promotion-stat\#promotion)

Access the associated order promotion (BelongsTo)

- return `FluentCartPro\App\Modules\Promotional\Models\OrderPromotion` Model

#### Example: [​](https://dev.fluentcart.com/database/models/order-promotion-stat\#example-1)

php

```
// Accessing Promotion
$promotion = $orderPromotionStat->promotion;

// For Filtering by promotion relationship
$orderPromotionStats = FluentCartPro\App\Modules\Promotional\Models\OrderPromotionStat::whereHas('promotion', function($query) {
    $query->where('status', 'active');
})->get();
```

## Usage Examples [​](https://dev.fluentcart.com/database/models/order-promotion-stat\#usage-examples)

### Create Order Promotion Stat [​](https://dev.fluentcart.com/database/models/order-promotion-stat\#create-order-promotion-stat)

php

```
$orderPromotionStat = FluentCartPro\App\Modules\Promotional\Models\OrderPromotionStat::create([\
    'promotion_id' => 1,\
    'order_id' => 123,\
    'object_id' => 456,\
    'amount' => 15.99,\
    'status' => 'applied'\
]);
```

### Get Stats by Promotion [​](https://dev.fluentcart.com/database/models/order-promotion-stat\#get-stats-by-promotion)

php

```
$promotionStats = FluentCartPro\App\Modules\Promotional\Models\OrderPromotionStat::where('promotion_id', 1)->get();
```

### Get Stats by Order [​](https://dev.fluentcart.com/database/models/order-promotion-stat\#get-stats-by-order)

php

```
$orderStats = FluentCartPro\App\Modules\Promotional\Models\OrderPromotionStat::where('order_id', 123)->get();
```

### Get Stats by Status [​](https://dev.fluentcart.com/database/models/order-promotion-stat\#get-stats-by-status)

php

```
$appliedStats = FluentCartPro\App\Modules\Promotional\Models\OrderPromotionStat::where('status', 'applied')->get();
$declinedStats = FluentCartPro\App\Modules\Promotional\Models\OrderPromotionStat::where('status', 'declined')->get();
```

### Get Stats with Order and Promotion Information [​](https://dev.fluentcart.com/database/models/order-promotion-stat\#get-stats-with-order-and-promotion-information)

php

```
$statsWithDetails = FluentCartPro\App\Modules\Promotional\Models\OrderPromotionStat::with(['order', 'promotion'])->get();

foreach ($statsWithDetails as $stat) {
    echo "Order: " . $stat->order->id;
    echo "Promotion: " . $stat->promotion->title;
    echo "Amount: " . $stat->amount;
}
```

### Get Stats by Amount Range [​](https://dev.fluentcart.com/database/models/order-promotion-stat\#get-stats-by-amount-range)

php

```
$highValueStats = FluentCartPro\App\Modules\Promotional\Models\OrderPromotionStat::where('amount', '>', 50.00)->get();
$lowValueStats = FluentCartPro\App\Modules\Promotional\Models\OrderPromotionStat::where('amount', '<=', 10.00)->get();
```

### Update Order Promotion Stat [​](https://dev.fluentcart.com/database/models/order-promotion-stat\#update-order-promotion-stat)

php

```
$orderPromotionStat = FluentCartPro\App\Modules\Promotional\Models\OrderPromotionStat::find(1);
$orderPromotionStat->update([\
    'status' => 'completed',\
    'amount' => 20.00\
]);
```

### Get Stats by Object ID [​](https://dev.fluentcart.com/database/models/order-promotion-stat\#get-stats-by-object-id)

php

```
$objectStats = FluentCartPro\App\Modules\Promotional\Models\OrderPromotionStat::where('object_id', 456)->get();
```

### Get Stats for Date Range [​](https://dev.fluentcart.com/database/models/order-promotion-stat\#get-stats-for-date-range)

php

```
$stats = FluentCartPro\App\Modules\Promotional\Models\OrderPromotionStat::whereBetween('created_at', ['2024-01-01', '2024-01-31'])->get();
```

### Delete Order Promotion Stat [​](https://dev.fluentcart.com/database/models/order-promotion-stat\#delete-order-promotion-stat)

php

```
$orderPromotionStat = FluentCartPro\App\Modules\Promotional\Models\OrderPromotionStat::find(1);
$orderPromotionStat->delete();
```

* * *

**Plugin**: FluentCart Pro

Today

Hi! I’m your AI assistant. How can I assist you today?

Just now

Powered by **FluentBot**


---

---

## Order Tax Rate Model | FluentCart Developer Docs

**URL** : https://dev.fluentcart.com/database/models/order-tax-rate

[Skip to content](https://dev.fluentcart.com/database/models/order-tax-rate#VPContent)

# Order Tax Rate Model [​](https://dev.fluentcart.com/database/models/order-tax-rate\#order-tax-rate-model)

| DB Table Name | {wp\_db\_prefix}\_fct\_order\_tax\_rate |
| --- | --- |
| Schema | [Check Schema](https://dev.fluentcart.com/database/schema.html#fct-order-tax-rate-table) |
| Source File | fluent-cart/app/Models/OrderTaxRate.php |
| Name Space | FluentCart\\App\\Models |
| Class | FluentCart\\App\\Models\\OrderTaxRate |

## Attributes [​](https://dev.fluentcart.com/database/models/order-tax-rate\#attributes)

| Attribute | Data Type | Comment |
| --- | --- | --- |
| id | Integer | Primary Key (guarded) |
| order\_id | Integer | Reference to order |
| tax\_rate\_id | Integer | Reference to tax rate |
| shipping\_tax | Decimal | Shipping tax amount (in cents) |
| order\_tax | Decimal | Order tax amount (in cents) |
| total\_tax | Decimal | Total tax amount (in cents) |
| meta | JSON | Additional tax data |
| filed\_at | Date Time | Tax filing date |
| created\_at | Date Time | Creation timestamp |
| updated\_at | Date Time | Last update timestamp |

> **Note:** The `id` column is both guarded and declared as `$primaryKey`.

## Usage [​](https://dev.fluentcart.com/database/models/order-tax-rate\#usage)

Please check [Model Basic](https://dev.fluentcart.com/database/models.html) for Common methods.

### Accessing Attributes [​](https://dev.fluentcart.com/database/models/order-tax-rate\#accessing-attributes)

php

```
$orderTaxRate = FluentCart\App\Models\OrderTaxRate::find(1);

$orderTaxRate->id; // returns id
$orderTaxRate->order_id; // returns order ID
$orderTaxRate->tax_rate_id; // returns tax rate ID
$orderTaxRate->total_tax; // returns total tax amount
```

## Scopes [​](https://dev.fluentcart.com/database/models/order-tax-rate\#scopes)

This model has the following scopes that you can use

### validOrder() [​](https://dev.fluentcart.com/database/models/order-tax-rate\#validorder)

Filter tax rates to only include those belonging to completed orders. Uses a `whereHas` on the `order` relationship with `status = 'completed'`.

- Parameters
  - none

#### Usage: [​](https://dev.fluentcart.com/database/models/order-tax-rate\#usage-1)

php

```
// Get tax rates for completed orders only
$taxRates = FluentCart\App\Models\OrderTaxRate::validOrder()->get();
```

## Relations [​](https://dev.fluentcart.com/database/models/order-tax-rate\#relations)

This model has the following relationships that you can use

### order [​](https://dev.fluentcart.com/database/models/order-tax-rate\#order)

Access the associated order

- return `FluentCart\App\Models\Order` Model

#### Example: [​](https://dev.fluentcart.com/database/models/order-tax-rate\#example)

php

```
// Accessing Order
$order = $orderTaxRate->order;

// For Filtering by order relationship
$orderTaxRates = FluentCart\App\Models\OrderTaxRate::whereHas('order', function($query) {
    $query->where('status', 'completed');
})->get();
```

### tax\_rate [​](https://dev.fluentcart.com/database/models/order-tax-rate\#tax-rate)

Access the associated tax rate

- return `FluentCart\App\Models\TaxRate` Model

#### Example: [​](https://dev.fluentcart.com/database/models/order-tax-rate\#example-1)

php

```
// Accessing Tax Rate
$taxRate = $orderTaxRate->tax_rate;

// For Filtering by tax rate relationship
$orderTaxRates = FluentCart\App\Models\OrderTaxRate::whereHas('tax_rate', function($query) {
    $query->where('rate', '>', 0);
})->get();
```

## Methods [​](https://dev.fluentcart.com/database/models/order-tax-rate\#methods)

Along with Global Model methods, this model has few helper methods.

### setMetaAttribute($value) [​](https://dev.fluentcart.com/database/models/order-tax-rate\#setmetaattribute-value)

Set meta from array (mutator). Automatically JSON-encodes the value.

- Parameters
  - $value - array\|object
- Returns `void`

#### Usage [​](https://dev.fluentcart.com/database/models/order-tax-rate\#usage-2)

php

```
$orderTaxRate->meta = ['tax_details' => 'value', 'filing_info' => 'data'];
```

### getMetaAttribute($value) [​](https://dev.fluentcart.com/database/models/order-tax-rate\#getmetaattribute-value)

Get meta as array (accessor). Automatically JSON-decodes the stored value.

- Parameters
  - $value - mixed
- Returns `array`

#### Usage [​](https://dev.fluentcart.com/database/models/order-tax-rate\#usage-3)

php

```
$meta = $orderTaxRate->meta; // Returns array
```

## Usage Examples [​](https://dev.fluentcart.com/database/models/order-tax-rate\#usage-examples)

### Get Order Tax Rates [​](https://dev.fluentcart.com/database/models/order-tax-rate\#get-order-tax-rates)

php

```
$order = FluentCart\App\Models\Order::find(123);
$taxRates = $order->order_tax_rates;

foreach ($taxRates as $taxRate) {
    echo "Tax Rate: " . $taxRate->tax_rate->rate;
    echo "Total Tax: " . $taxRate->total_tax;
}
```

### Get Tax Rates for Completed Orders [​](https://dev.fluentcart.com/database/models/order-tax-rate\#get-tax-rates-for-completed-orders)

php

```
$completedOrderTaxRates = FluentCart\App\Models\OrderTaxRate::validOrder()->get();
```

### Create Order Tax Rate [​](https://dev.fluentcart.com/database/models/order-tax-rate\#create-order-tax-rate)

php

```
$orderTaxRate = FluentCart\App\Models\OrderTaxRate::create([\
    'order_id' => 123,\
    'tax_rate_id' => 5,\
    'shipping_tax' => 250,\
    'order_tax' => 1575,\
    'total_tax' => 1825,\
    'filed_at' => now()\
]);
```

### Get Tax Rate Details [​](https://dev.fluentcart.com/database/models/order-tax-rate\#get-tax-rate-details)

php

```
$orderTaxRate = FluentCart\App\Models\OrderTaxRate::with(['order', 'tax_rate'])->find(1);
$order = $orderTaxRate->order;
$taxRate = $orderTaxRate->tax_rate;
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

## Order Transaction Model | FluentCart Developer Docs

**URL** : https://dev.fluentcart.com/database/models/order-transaction

[Skip to content](https://dev.fluentcart.com/database/models/order-transaction#VPContent)

# Order Transaction Model [​](https://dev.fluentcart.com/database/models/order-transaction\#order-transaction-model)

| DB Table Name | {wp\_db\_prefix}\_fct\_order\_transactions |
| --- | --- |
| Schema | [Check Schema](https://dev.fluentcart.com/database/schema.html#fct-order-transactions-table) |
| Source File | fluent-cart/app/Models/OrderTransaction.php |
| Name Space | FluentCart\\App\\Models |
| Class | FluentCart\\App\\Models\\OrderTransaction |

## Traits [​](https://dev.fluentcart.com/database/models/order-transaction\#traits)

- **CanSearch** (`FluentCart\App\Models\Concerns\CanSearch`) \-\- Provides `search`, `groupSearch`, `whereLike`, `whereBeginsWith`, and `whereEndsWith` scopes for flexible querying.

## Appends [​](https://dev.fluentcart.com/database/models/order-transaction\#appends)

The model automatically appends the following computed attributes to its array/JSON output:

- `url` \-\- Transaction URL generated via the `getUrlAttribute` accessor

## Boot [​](https://dev.fluentcart.com/database/models/order-transaction\#boot)

On the `creating` event the model auto-generates a `uuid` when one is not already set:

php

```
$model->uuid = md5(time() . wp_generate_uuid4());
```

## Searchable Fields [​](https://dev.fluentcart.com/database/models/order-transaction\#searchable-fields)

The following columns are searchable via the `CanSearch` trait:

`id`, `total`, `status`, `payment_method`, `currency`, `created_at`, `updated_at`

## Attributes [​](https://dev.fluentcart.com/database/models/order-transaction\#attributes)

| Attribute | Data Type | Comment |
| --- | --- | --- |
| id | Integer | Primary Key |
| order\_id | Integer | Reference to order |
| order\_type | String | Order type (onetime, subscription, signup\_fee) |
| vendor\_charge\_id | String | Payment gateway transaction ID |
| payment\_method | String | Payment method key |
| payment\_mode | String | Payment mode (live, test) |
| payment\_method\_type | String | Payment method type (card, bank, etc.) |
| currency | String | Transaction currency |
| transaction\_type | String | Transaction type (charge, refund, partial\_refund, dispute) |
| subscription\_id | Integer | Reference to subscription (if applicable) |
| card\_last\_4 | String | Last 4 digits of card |
| card\_brand | String | Card brand (visa, mastercard, etc.) |
| status | String | Transaction status |
| total | Bigint | Transaction amount in cents |
| rate | Bigint | Exchange rate |
| meta | JSON | Additional transaction data (stored as JSON, accessed as array via accessor/mutator) |
| uuid | String | Unique transaction identifier (auto-generated on create) |
| created\_at | Date Time | Creation timestamp |
| updated\_at | Date Time | Last update timestamp |

## Usage [​](https://dev.fluentcart.com/database/models/order-transaction\#usage)

Please check [Model Basic](https://dev.fluentcart.com/database/models.html) for Common methods.

### Accessing Attributes [​](https://dev.fluentcart.com/database/models/order-transaction\#accessing-attributes)

php

```
$transaction = FluentCart\App\Models\OrderTransaction::find(1);

$transaction->id; // returns id
$transaction->order_id; // returns order ID
$transaction->total; // returns total amount in cents
$transaction->status; // returns status
$transaction->payment_method; // returns payment method
$transaction->meta; // returns array (auto-decoded from JSON)
$transaction->url; // returns computed transaction URL (appended attribute)
```

## Scopes [​](https://dev.fluentcart.com/database/models/order-transaction\#scopes)

This model has the following scopes that you can use

### ofStatus($status) [​](https://dev.fluentcart.com/database/models/order-transaction\#ofstatus-status)

Filter transactions by status

- Parameters
  - $status - string

#### Usage: [​](https://dev.fluentcart.com/database/models/order-transaction\#usage-1)

php

```
// Get all successful transactions
$transactions = FluentCart\App\Models\OrderTransaction::ofStatus('succeeded')->get();
```

### ofPaymentMethod($methodName) [​](https://dev.fluentcart.com/database/models/order-transaction\#ofpaymentmethod-methodname)

Filter transactions by payment method

- Parameters
  - $methodName - string

#### Usage: [​](https://dev.fluentcart.com/database/models/order-transaction\#usage-2)

php

```
// Get all Stripe transactions
$transactions = FluentCart\App\Models\OrderTransaction::ofPaymentMethod('stripe')->get();
```

### searchByPayerEmail($data) [​](https://dev.fluentcart.com/database/models/order-transaction\#searchbypayeremail-data)

Filter transactions by the payer email address stored in the `meta` JSON column at `$.payer.email_address`. Supports multiple operators.

- Parameters
  - $data - array with keys:
    - `value` (string) - The email or partial email to search for
    - `operator` (string, optional) - One of `contains` (default), `starts_with`, `ends_with`, `equals`, `not_like`

#### Usage: [​](https://dev.fluentcart.com/database/models/order-transaction\#usage-3)

php

```
// Find transactions where payer email contains "example.com"
$transactions = FluentCart\App\Models\OrderTransaction::searchByPayerEmail([\
    'value'    => 'example.com',\
    'operator' => 'contains',\
])->get();

// Find transactions where payer email starts with "john"
$transactions = FluentCart\App\Models\OrderTransaction::searchByPayerEmail([\
    'value'    => 'john',\
    'operator' => 'starts_with',\
])->get();

// Find transactions where payer email exactly matches
$transactions = FluentCart\App\Models\OrderTransaction::searchByPayerEmail([\
    'value'    => 'john@example.com',\
    'operator' => 'equals',\
])->get();
```

## Relations [​](https://dev.fluentcart.com/database/models/order-transaction\#relations)

This model has the following relationships that you can use

### order [​](https://dev.fluentcart.com/database/models/order-transaction\#order)

Access the associated order (belongsTo)

- return `FluentCart\App\Models\Order` Model

#### Example: [​](https://dev.fluentcart.com/database/models/order-transaction\#example)

php

```
// Accessing Order
$order = $transaction->order;

// For Filtering by order relationship
$transactions = FluentCart\App\Models\OrderTransaction::whereHas('order', function($query) {
    $query->where('status', 'completed');
})->get();
```

### orders [​](https://dev.fluentcart.com/database/models/order-transaction\#orders)

Access the associated order via hasOne (alternative to `order` relationship)

- return `FluentCart\App\Models\Order` Model (HasOne)

#### Example: [​](https://dev.fluentcart.com/database/models/order-transaction\#example-1)

php

```
// Accessing Order via hasOne
$order = $transaction->orders;
```

### subscription [​](https://dev.fluentcart.com/database/models/order-transaction\#subscription)

Access the associated subscription (hasOne)

- return `FluentCart\App\Models\Subscription` Model

#### Example: [​](https://dev.fluentcart.com/database/models/order-transaction\#example-2)

php

```
// Accessing Subscription
$subscription = $transaction->subscription;

// For Filtering by subscription relationship
$transactions = FluentCart\App\Models\OrderTransaction::whereHas('subscription', function($query) {
    $query->where('status', 'active');
})->get();
```

## Methods [​](https://dev.fluentcart.com/database/models/order-transaction\#methods)

Along with Global Model methods, this model has few helper methods.

### getMetaAttribute($value) [​](https://dev.fluentcart.com/database/models/order-transaction\#getmetaattribute-value)

Get meta as array (accessor). Automatically decodes the JSON string stored in the database into a PHP array.

- Parameters
  - $value - mixed (raw JSON string from database)
- Returns `array`

#### Usage [​](https://dev.fluentcart.com/database/models/order-transaction\#usage-4)

php

```
$meta = $transaction->meta; // Returns array
```

### setMetaAttribute($value) [​](https://dev.fluentcart.com/database/models/order-transaction\#setmetaattribute-value)

Set meta from array/object (mutator). Automatically encodes the value to a JSON string for storage.

- Parameters
  - $value - array\|object
- Returns `void`

#### Usage [​](https://dev.fluentcart.com/database/models/order-transaction\#usage-5)

php

```
$transaction->meta = ['gateway_response' => 'success', 'fee' => 2.9];
```

### getUrlAttribute($value) [​](https://dev.fluentcart.com/database/models/order-transaction\#geturlattribute-value)

Get transaction URL (accessor). Applies the `fluent_cart/transaction/url_{payment_method}` filter to generate a gateway-specific URL.

- Parameters
  - $value - mixed
- Returns `string`

#### Usage [​](https://dev.fluentcart.com/database/models/order-transaction\#usage-6)

php

```
$url = $transaction->url; // Returns filtered transaction URL
```

### updateStatus($newStatus, $otherData = \[\]) [​](https://dev.fluentcart.com/database/models/order-transaction\#updatestatus-newstatus-otherdata)

Update the transaction status. If the new status is the same as the current status, no update is performed. Optionally fills additional data before saving.

- Parameters
  - $newStatus - string - The new status to set
  - $otherData - array (optional) - Additional fillable attributes to update
- Returns `OrderTransaction` \- The current model instance

#### Usage [​](https://dev.fluentcart.com/database/models/order-transaction\#usage-7)

php

```
// Update status only
$transaction->updateStatus('succeeded');

// Update status with additional data
$transaction->updateStatus('succeeded', [\
    'vendor_charge_id' => 'ch_abc123',\
    'card_last_4'      => '4242',\
    'card_brand'       => 'visa',\
]);
```

### bulkDeleteByOrderIds($ids, $params = \[\]) [​](https://dev.fluentcart.com/database/models/order-transaction\#bulkdeletebyorderids-ids-params)

Delete all transactions associated with the given order IDs. This is a static method.

- Parameters
  - $ids - array - Array of order IDs
  - $params - array (optional) - Currently unused
- Returns `mixed` \- Result of the delete query

#### Usage [​](https://dev.fluentcart.com/database/models/order-transaction\#usage-8)

php

```
// Delete all transactions for specific orders
FluentCart\App\Models\OrderTransaction::bulkDeleteByOrderIds([123, 456, 789]);
```

### getMaxRefundableAmount() [​](https://dev.fluentcart.com/database/models/order-transaction\#getmaxrefundableamount)

Calculate the maximum refundable amount for this transaction. Returns 0 if the transaction status is not `succeeded`. Subtracts any already-refunded amount (from `meta.refunded_total`) from the transaction total.

- Parameters
  - none
- Returns `int` \- The maximum refundable amount in cents

#### Usage [​](https://dev.fluentcart.com/database/models/order-transaction\#usage-9)

php

```
$maxRefund = $transaction->getMaxRefundableAmount();
// If total is 5000 (cents) and 2000 has been refunded, returns 3000
```

### getPaymentMethodText() [​](https://dev.fluentcart.com/database/models/order-transaction\#getpaymentmethodtext)

Get a human-readable payment method description. If card brand and last 4 digits are available, returns a formatted string like "visa \*\*\*4242". Otherwise returns the raw payment method key.

- Parameters
  - none
- Returns `string`

#### Usage [​](https://dev.fluentcart.com/database/models/order-transaction\#usage-10)

php

```
$text = $transaction->getPaymentMethodText();
// Returns "visa ***4242" or "stripe" (fallback)
```

### getReceiptPageUrl($filtered = false) [​](https://dev.fluentcart.com/database/models/order-transaction\#getreceiptpageurl-filtered-false)

Generate the receipt page URL for this transaction. Appends the `trx_hash` query parameter (the transaction's uuid) to the store's configured receipt page URL.

- Parameters
  - $filtered - boolean (optional, default `false`) \- When `true`, applies the `fluentcart/transaction/receipt_page_url` filter
- Returns `string` \- The full receipt page URL

#### Usage [​](https://dev.fluentcart.com/database/models/order-transaction\#usage-11)

php

```
// Get basic receipt URL
$url = $transaction->getReceiptPageUrl();

// Get filtered receipt URL (allows plugins to modify)
$url = $transaction->getReceiptPageUrl(true);
```

### acceptDispute($args = \[\]) [​](https://dev.fluentcart.com/database/models/order-transaction\#acceptdispute-args)

Accept a payment dispute for this transaction. Only works on transactions where `transaction_type` is `dispute`. Calls the payment gateway's remote dispute handler, updates the transaction status to `dispute_lost`, adjusts the order's `total_paid` and `payment_status`, and logs the action.

- Parameters
  - $args - array (optional) - Accepts:
    - `dispute_note` (string) - Optional note about the dispute acceptance
- Returns `void|\WP_Error` \- Returns `WP_Error` if the transaction is not a dispute, the payment method does not support remote dispute management, or the remote handler fails

#### Usage [​](https://dev.fluentcart.com/database/models/order-transaction\#usage-12)

php

```
$result = $transaction->acceptDispute([\
    'dispute_note' => 'Customer claim accepted, refund approved.',\
]);

if (is_wp_error($result)) {
    // Handle error
    echo $result->get_error_message();
}
```

## Transaction Statuses [​](https://dev.fluentcart.com/database/models/order-transaction\#transaction-statuses)

Common transaction statuses in FluentCart:

- `pending` \- Transaction is pending
- `processing` \- Transaction is being processed
- `succeeded` \- Transaction succeeded
- `failed` \- Transaction failed
- `cancelled` \- Transaction was cancelled
- `refunded` \- Transaction was refunded
- `partially_refunded` \- Transaction was partially refunded
- `dispute_lost` \- Dispute accepted/lost

## Transaction Types [​](https://dev.fluentcart.com/database/models/order-transaction\#transaction-types)

Common transaction types in FluentCart:

- `charge` \- Initial charge/payment
- `refund` \- Full refund
- `partial_refund` \- Partial refund
- `dispute` \- Payment dispute

## Usage Examples [​](https://dev.fluentcart.com/database/models/order-transaction\#usage-examples)

### Get Order Transactions [​](https://dev.fluentcart.com/database/models/order-transaction\#get-order-transactions)

php

```
$order = FluentCart\App\Models\Order::find(123);
$transactions = $order->transactions()->orderBy('created_at', 'desc')->get();

foreach ($transactions as $transaction) {
    echo "Transaction #{$transaction->id}: {$transaction->total} cents - {$transaction->status}";
}
```

### Get Successful Transactions for Date Range [​](https://dev.fluentcart.com/database/models/order-transaction\#get-successful-transactions-for-date-range)

php

```
$transactions = FluentCart\App\Models\OrderTransaction::ofStatus('succeeded')
    ->whereBetween('created_at', ['2024-01-01', '2024-01-31'])
    ->get();
```

### Get Refund Transactions [​](https://dev.fluentcart.com/database/models/order-transaction\#get-refund-transactions)

php

```
$refunds = FluentCart\App\Models\OrderTransaction::whereIn('transaction_type', ['refund', 'partial_refund'])
    ->get();
```

### Get Subscription Transactions [​](https://dev.fluentcart.com/database/models/order-transaction\#get-subscription-transactions)

php

```
$subscriptionTransactions = FluentCart\App\Models\OrderTransaction::whereNotNull('subscription_id')
    ->get();
```

### Calculate Refundable Amount [​](https://dev.fluentcart.com/database/models/order-transaction\#calculate-refundable-amount)

php

```
$transaction = FluentCart\App\Models\OrderTransaction::find(1);
$maxRefund = $transaction->getMaxRefundableAmount();
echo "Max refundable: " . $maxRefund . " cents";
```

### Search by Payer Email [​](https://dev.fluentcart.com/database/models/order-transaction\#search-by-payer-email)

php

```
$transactions = FluentCart\App\Models\OrderTransaction::searchByPayerEmail([\
    'value'    => 'customer@example.com',\
    'operator' => 'equals',\
])->get();
```

* * *

Today

Hi! I’m your AI assistant. How can I assist you today?

Just now

Powered by **FluentBot**


---

---

