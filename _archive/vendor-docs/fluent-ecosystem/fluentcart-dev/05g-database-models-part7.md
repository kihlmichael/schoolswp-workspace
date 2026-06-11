# FluentCart Developer Docs - Database Models (Part 7/8)

Tous les modèles Eloquent exposés par FluentCart : orders, customers, products, subscriptions, coupons, licenses, taxes, shipping, etc.

---

## Product Variation Model | FluentCart Developer Docs

**URL** : https://dev.fluentcart.com/database/models/product-variation

[Skip to content](https://dev.fluentcart.com/database/models/product-variation#VPContent)

# Product Variation Model [​](https://dev.fluentcart.com/database/models/product-variation\#product-variation-model)

| DB Table Name | {wp\_db\_prefix}\_fct\_product\_variations |
| --- | --- |
| Schema | [Check Schema](https://dev.fluentcart.com/database/schema.html#fct-product-variations-table) |
| Source File | fluent-cart/app/Models/ProductVariation.php |
| Name Space | FluentCart\\App\\Models |
| Class | FluentCart\\App\\Models\\ProductVariation |

## Traits [​](https://dev.fluentcart.com/database/models/product-variation\#traits)

| Trait | Description |
| --- | --- |
| `CanSearch` | Adds search scope capabilities |
| `CanUpdateBatch` | Adds batch update capabilities |

## Attributes [​](https://dev.fluentcart.com/database/models/product-variation\#attributes)

| Attribute | Data Type | Comment |
| --- | --- | --- |
| id | Integer | Primary Key |
| post\_id | Integer | Reference to WordPress post (product) |
| media\_id | Integer | Reference to media |
| serial\_index | Integer | Serial index for ordering |
| sold\_individually | Integer | Whether sold individually (0 or 1) |
| variation\_title | String | Variation title |
| variation\_identifier | String | Variation identifier |
| sku | String | Stock keeping unit |
| manage\_stock | String | Whether to manage stock |
| payment\_type | String | Payment type (`onetime`, `subscription`) |
| stock\_status | String | Stock status |
| backorders | Integer | Backorder quantity |
| total\_stock | Integer | Total stock quantity |
| available | Integer | Available quantity |
| committed | Integer | Committed quantity |
| on\_hold | Integer | On hold quantity |
| fulfillment\_type | String | Fulfillment type (`physical`, `digital`) |
| item\_status | String | Item status (`active`, `inactive`) |
| manage\_cost | String | Whether to manage cost |
| item\_price | Decimal | Item price (stored in cents, cast to double) |
| item\_cost | Decimal | Item cost (stored in cents, cast to double) |
| compare\_price | Decimal | Compare price (stored in cents, cast to double) |
| other\_info | Array | Additional variation information (JSON, cast to array) |
| downloadable | String | Whether downloadable |
| shipping\_class | String | Shipping class ID |
| created\_at | Date Time | Creation timestamp |
| updated\_at | Date Time | Last update timestamp |

## Casts [​](https://dev.fluentcart.com/database/models/product-variation\#casts)

The following attributes are automatically cast when accessed:

| Attribute | Cast Type |
| --- | --- |
| post\_id | integer |
| media\_id | integer |
| item\_cost | double |
| item\_price | double |
| compare\_price | double |
| backorders | integer |
| total\_stock | integer |
| available | integer |
| committed | integer |
| on\_hold | integer |
| sold\_individually | integer |
| serial\_index | integer |
| other\_info | array |

## Appends [​](https://dev.fluentcart.com/database/models/product-variation\#appends)

The following computed attributes are appended to every model instance:

| Appended Attribute | Description |
| --- | --- |
| `thumbnail` | Always appended via `$appends`. Returns the first thumbnail URL from the `media` relation, or `null`. |
| `formatted_total` | Appended at runtime inside `booted()` on every `retrieved` event. Returns `Helper::toDecimal($this->item_price)`. |

## Custom `other_info` Accessor [​](https://dev.fluentcart.com/database/models/product-variation\#custom-other-info-accessor)

The `getOtherInfoAttribute` accessor decodes the JSON value and, when `payment_type` is `subscription`, injects sensible defaults for subscription fields that may not yet be stored:

| Injected Key | Default Value |
| --- | --- |
| `payment_type` | `'subscription'` |
| `installment` | `'yes'` only if value is `'yes'` AND Pro is active; otherwise `'no'` |
| `repeat_interval` | `'yearly'` |
| `times` | `0` |
| `trial_days` | `0` |
| `manage_setup_fee` | `'no'` |

This means reading `$variation->other_info` on a subscription variation always returns these keys even if they were not explicitly saved.

## Cascade Deletes [​](https://dev.fluentcart.com/database/models/product-variation\#cascade-deletes)

When a `ProductVariation` is deleted, the `boot()` method fires the following cleanup:

1. **Media** \-\- calls `\FluentCart\Api\Meta::deleteVariationMedia($model->id)` to remove associated media metadata.
2. **Attribute Map** \-\- calls `$model->attrMap()->delete()` to remove all related `AttributeRelation` records.

## Usage [​](https://dev.fluentcart.com/database/models/product-variation\#usage)

Please check [Model Basic](https://dev.fluentcart.com/database/models.html) for Common methods.

### Accessing Attributes [​](https://dev.fluentcart.com/database/models/product-variation\#accessing-attributes)

php

```
$productVariation = FluentCart\App\Models\ProductVariation::find(1);

$productVariation->id; // returns id
$productVariation->post_id; // returns post ID
$productVariation->item_price; // returns item price (cast to double)
$productVariation->stock_status; // returns stock status
$productVariation->sku; // returns SKU
$productVariation->thumbnail; // returns thumbnail URL or null (appended attribute)
$productVariation->formatted_total; // returns formatted price string (appended on retrieval)
```

## Scopes [​](https://dev.fluentcart.com/database/models/product-variation\#scopes)

This model has the following scopes that you can use

### getWithShippingClass() [​](https://dev.fluentcart.com/database/models/product-variation\#getwithshippingclass)

Get variations with their shipping class information. This scope executes the query, then looks up `ShippingMethod` records whose IDs match the `other_info.shipping_class` value on each variation, and attaches the matching method as a `shipping_method` dynamic attribute.

- Parameters
  - none
- Returns the query result (executes `$query->get()` internally)

#### Usage: [​](https://dev.fluentcart.com/database/models/product-variation\#usage-1)

php

```
// Get variations with shipping class data
$variations = FluentCart\App\Models\ProductVariation::getWithShippingClass();

foreach ($variations as $variation) {
    if (isset($variation->shipping_method)) {
        echo $variation->shipping_method->title;
    }
}
```

## Relations [​](https://dev.fluentcart.com/database/models/product-variation\#relations)

This model has the following relationships that you can use

### product [​](https://dev.fluentcart.com/database/models/product-variation\#product)

Access the associated product (WordPress post). BelongsTo via `post_id` -\> `Product.ID`.

- return `FluentCart\App\Models\Product` Model

#### Example: [​](https://dev.fluentcart.com/database/models/product-variation\#example)

php

```
// Accessing Product
$product = $productVariation->product;

// For Filtering by product relationship
$productVariations = FluentCart\App\Models\ProductVariation::whereHas('product', function($query) {
    $query->where('post_status', 'publish');
})->get();
```

### shippingClass [​](https://dev.fluentcart.com/database/models/product-variation\#shippingclass)

Access the associated shipping class. BelongsTo via `shipping_class` -\> `ShippingClass.id`.

- return `FluentCart\App\Models\ShippingClass` Model

#### Example: [​](https://dev.fluentcart.com/database/models/product-variation\#example-1)

php

```
// Accessing Shipping Class
$shippingClass = $productVariation->shippingClass;
```

### product\_detail [​](https://dev.fluentcart.com/database/models/product-variation\#product-detail)

Access the associated product detail. BelongsTo via `post_id` -\> `ProductDetail.post_id`.

- return `FluentCart\App\Models\ProductDetail` Model

#### Example: [​](https://dev.fluentcart.com/database/models/product-variation\#example-2)

php

```
// Accessing Product Detail
$productDetail = $productVariation->product_detail;
```

### media [​](https://dev.fluentcart.com/database/models/product-variation\#media)

Access the associated product thumbnail media. HasOne to `ProductMeta` via `object_id` -\> `id`, filtered to `meta_key = 'product_thumbnail'`. Only selects `id`, `object_id`, `meta_value`.

- return `FluentCart\App\Models\ProductMeta` Model (single record)

#### Example: [​](https://dev.fluentcart.com/database/models/product-variation\#example-3)

php

```
// Accessing Media
$media = $productVariation->media;

// The thumbnail appended attribute reads from this relation:
$url = $productVariation->thumbnail; // shortcut
```

### product\_downloads [​](https://dev.fluentcart.com/database/models/product-variation\#product-downloads)

Access all product downloads associated with this variation's product. HasMany to `ProductDownload` via `post_id` -\> `post_id`, filtered to rows where `product_variation_id` contains this variation's ID, or is `NULL`, or is `'[]'`.

- return `FluentCart\App\Models\ProductDownload` Model Collection

#### Example: [​](https://dev.fluentcart.com/database/models/product-variation\#example-4)

php

```
// Accessing Product Downloads
$downloads = $productVariation->product_downloads;
```

### order\_items [​](https://dev.fluentcart.com/database/models/product-variation\#order-items)

Access all order items for this variation. HasMany to `OrderItem` via `object_id` -\> `id`.

- return `FluentCart\App\Models\OrderItem` Model Collection

#### Example: [​](https://dev.fluentcart.com/database/models/product-variation\#example-5)

php

```
// Accessing Order Items
$orderItems = $productVariation->order_items;
```

### downloadable\_files [​](https://dev.fluentcart.com/database/models/product-variation\#downloadable-files)

Access all downloadable files directly linked to this variation. HasMany to `ProductDownload` via `product_variation_id` -\> `id`.

- return `FluentCart\App\Models\ProductDownload` Model Collection

#### Example: [​](https://dev.fluentcart.com/database/models/product-variation\#example-6)

php

```
// Accessing Downloadable Files
$downloadableFiles = $productVariation->downloadable_files;
```

### upgrade\_paths [​](https://dev.fluentcart.com/database/models/product-variation\#upgrade-paths)

Access all upgrade path meta entries for this variation. HasMany to `Meta` via `object_id` -\> `id`, filtered by `object_type = PlanUpgradeService::$metaType` and `meta_key = PlanUpgradeService::$metaKey`.

- return `FluentCart\App\Models\Meta` Model Collection

#### Example: [​](https://dev.fluentcart.com/database/models/product-variation\#example-7)

php

```
// Accessing Upgrade Paths
$upgradePaths = $productVariation->upgrade_paths;
```

### attrMap [​](https://dev.fluentcart.com/database/models/product-variation\#attrmap)

Access all attribute relation mappings for this variation. HasMany to `AttributeRelation` via `object_id` -\> `id`.

**Note:** These records are cascade-deleted when the variation is deleted.

- return `FluentCart\App\Models\AttributeRelation` Model Collection

#### Example: [​](https://dev.fluentcart.com/database/models/product-variation\#example-8)

php

```
// Accessing Attribute Relations
$attrMap = $productVariation->attrMap;
```

### bundleChildren [​](https://dev.fluentcart.com/database/models/product-variation\#bundlechildren)

Access the child variations of a bundle product. Uses a custom `BundleChildrenRelation` that reads child IDs from the `other_info` JSON column (key `bundle_child_ids`) and loads the corresponding `ProductVariation` records. Supports eager loading.

- return `FluentCart\App\Models\ProductVariation` Model Collection (via `BundleChildrenRelation`)

#### Example: [​](https://dev.fluentcart.com/database/models/product-variation\#example-9)

php

```
// Accessing Bundle Children
$children = $productVariation->bundleChildren;

// Eager loading bundle children
$variations = FluentCart\App\Models\ProductVariation::with('bundleChildren')->where('post_id', $postId)->get();

foreach ($variations as $variation) {
    foreach ($variation->bundleChildren as $child) {
        echo $child->variation_title;
    }
}
```

## Methods [​](https://dev.fluentcart.com/database/models/product-variation\#methods)

Along with Global Model methods, this model has few helper methods.

### getFormattedTotalAttribute() [​](https://dev.fluentcart.com/database/models/product-variation\#getformattedtotalattribute)

Get formatted total price (accessor). Automatically appended on every `retrieved` event via the `booted()` method.

- Parameters
  - none
- Returns `string` \-\- the decimal-formatted item price

#### Usage [​](https://dev.fluentcart.com/database/models/product-variation\#usage-2)

php

```
$formattedTotal = $productVariation->formatted_total; // Returns formatted price string
```

### getThumbnailAttribute() [​](https://dev.fluentcart.com/database/models/product-variation\#getthumbnailattribute)

Get thumbnail URL (accessor). Reads from the `media` relation. Returns the `url` key of the first element in `media->meta_value`, or `null` if no media is set.

- Parameters
  - none
- Returns `string|null`

#### Usage [​](https://dev.fluentcart.com/database/models/product-variation\#usage-3)

php

```
$thumbnail = $productVariation->thumbnail; // Returns thumbnail URL or null
```

### canPurchase($quantity = 1) [​](https://dev.fluentcart.com/database/models/product-variation\#canpurchase-quantity-1)

Check if the variation can be purchased. Validates:

1. `item_status` must be `active` and parent product must be `publish` or `private`.
2. Subscription variations cannot have `$quantity > 1`.
3. A related `product_detail` must exist.
4. If stock management module is active and both `productDetail->manage_stock` and `$this->manage_stock` are truthy, `$quantity` must not exceed `$this->available`.
5. Bundle products require Pro to be active.
6. Applies the `fluent_cart/variation/can_purchase_bundle` filter for additional bundle checks.

- Parameters
  - `$quantity` \- integer (default: 1)
- Returns `true` on success, or `\WP_Error` with an error code on failure

**Error codes:**`unpublished`, `invalid_subscription_quantity`, `insufficient_stock`, `invalid_bundle_product`

#### Usage [​](https://dev.fluentcart.com/database/models/product-variation\#usage-4)

php

```
$canPurchase = $productVariation->canPurchase(2);
if (is_wp_error($canPurchase)) {
    echo "Error: " . $canPurchase->get_error_message();
} else {
    echo "Available for purchase";
}
```

### getSubscriptionTermsText($withComparePrice = false) [​](https://dev.fluentcart.com/database/models/product-variation\#getsubscriptiontermstext-withcompareprice-false)

Get human-readable subscription terms text. Returns an empty string for non-subscription variations. Reads `trial_days`, `repeat_interval`, `times`, `signup_fee`, `signup_fee_name` from `other_info` and delegates to `Helper::getSubscriptionTermText()`.

- Parameters
  - `$withComparePrice` \- boolean (default: false). When `true` and `compare_price > item_price`, the compare price is included in the formatted output.
- Returns `string`

#### Usage [​](https://dev.fluentcart.com/database/models/product-variation\#usage-5)

php

```
$termsText = $productVariation->getSubscriptionTermsText(true);
echo "Subscription Terms: " . $termsText;
```

### getPurchaseUrl() [​](https://dev.fluentcart.com/database/models/product-variation\#getpurchaseurl)

Get the instant checkout purchase URL for this variation.

- Parameters
  - none
- Returns `string` \-\- URL in the format `site_url('?fluent-cart=instant_checkout&item_id={id}&quantity=1')`

#### Usage [​](https://dev.fluentcart.com/database/models/product-variation\#usage-6)

php

```
$purchaseUrl = $productVariation->getPurchaseUrl();
echo "Purchase URL: " . $purchaseUrl;
```

### soldIndividually() [​](https://dev.fluentcart.com/database/models/product-variation\#soldindividually)

Check whether this variation's parent product is sold individually. Delegates to `$this->product->soldIndividually()`.

- Parameters
  - none
- Returns `bool` \-\- `false` if no product is loaded

#### Usage [​](https://dev.fluentcart.com/database/models/product-variation\#usage-7)

php

```
if ($productVariation->soldIndividually()) {
    echo "This product can only be purchased one at a time.";
}
```

### isStock() [​](https://dev.fluentcart.com/database/models/product-variation\#isstock)

Check whether this variation is currently in stock. The logic handles both regular and bundle products:

1. Returns `false` if `item_status` is not `active`.
2. If `manage_stock` is disabled:
   - For bundle products, delegates to `isBundleChildrenInStock()`.
   - For regular products, returns `true` when `stock_status` equals `Helper::IN_STOCK`.
3. If `manage_stock` is enabled, checks `available > 0` AND `stock_status === Helper::IN_STOCK`.
4. For bundle products with stock management enabled, the parent must be in stock AND all children must pass `isBundleChildrenInStock()`.

- Parameters
  - none
- Returns `bool`

#### Usage [​](https://dev.fluentcart.com/database/models/product-variation\#usage-8)

php

```
$variation = FluentCart\App\Models\ProductVariation::find(1);
if ($variation->isStock()) {
    echo "In stock";
} else {
    echo "Out of stock";
}
```

### isBundleChildrenInStock() (protected) [​](https://dev.fluentcart.com/database/models/product-variation\#isbundlechildreninstock-protected)

Check if all bundle children are in stock. Reads `bundle_child_ids` from `other_info`, loads those variations, and verifies each child is `active` and (if `manage_stock` is enabled) has `available > 0` with `stock_status === Helper::IN_STOCK`. Returns `true` if there are no bundle children.

- Visibility: `protected`
- Parameters
  - none
- Returns `bool`

## Hooks / Filters [​](https://dev.fluentcart.com/database/models/product-variation\#hooks-filters)

| Hook | Type | Location | Description |
| --- | --- | --- | --- |
| `fluent_cart/variation/can_purchase_bundle` | Filter | `canPurchase()` | Allows external code to block or allow bundle purchases. Receives `null` and an array with `variation` and `quantity`. Return `\WP_Error` to block, `false` for out-of-stock, or `null`/`true` to allow. |

## Usage Examples [​](https://dev.fluentcart.com/database/models/product-variation\#usage-examples)

### Get Product Variations [​](https://dev.fluentcart.com/database/models/product-variation\#get-product-variations)

php

```
$productVariation = FluentCart\App\Models\ProductVariation::find(1);
echo "Price: " . $productVariation->formatted_total;
echo "Stock: " . $productVariation->available;
echo "Status: " . $productVariation->item_status;
echo "SKU: " . $productVariation->sku;
```

### Get Variations with Shipping Class [​](https://dev.fluentcart.com/database/models/product-variation\#get-variations-with-shipping-class)

php

```
$variations = FluentCart\App\Models\ProductVariation::getWithShippingClass();
foreach ($variations as $variation) {
    echo "Variation: " . $variation->variation_title;
    if (isset($variation->shipping_method)) {
        echo "Shipping Method: " . $variation->shipping_method->title;
    }
}
```

### Check Purchase Availability [​](https://dev.fluentcart.com/database/models/product-variation\#check-purchase-availability)

php

```
$variation = FluentCart\App\Models\ProductVariation::find(1);
$canPurchase = $variation->canPurchase(1);

if (is_wp_error($canPurchase)) {
    echo "Cannot purchase: " . $canPurchase->get_error_message();
} else {
    echo "Available for purchase";
}
```

### Check Stock Status (Including Bundles) [​](https://dev.fluentcart.com/database/models/product-variation\#check-stock-status-including-bundles)

php

```
$variation = FluentCart\App\Models\ProductVariation::find(1);
if ($variation->isStock()) {
    echo "Variation is in stock";
} else {
    echo "Variation is out of stock";
}
```

### Get Subscription Terms [​](https://dev.fluentcart.com/database/models/product-variation\#get-subscription-terms)

php

```
$variation = FluentCart\App\Models\ProductVariation::find(1);
if ($variation->payment_type === 'subscription') {
    $terms = $variation->getSubscriptionTermsText(true);
    echo "Subscription: " . $terms;
}
```

### Get Downloadable Files [​](https://dev.fluentcart.com/database/models/product-variation\#get-downloadable-files)

php

```
$variation = FluentCart\App\Models\ProductVariation::find(1);
$downloads = $variation->downloadable_files;

foreach ($downloads as $download) {
    echo "Download: " . $download->title;
}
```

### Work with Bundle Children [​](https://dev.fluentcart.com/database/models/product-variation\#work-with-bundle-children)

php

```
$variation = FluentCart\App\Models\ProductVariation::find(1);
$children = $variation->bundleChildren;

foreach ($children as $child) {
    echo "Child: " . $child->variation_title . " - Price: " . $child->formatted_total;
}
```

* * *

Today

Hi! I’m your AI assistant. How can I assist you today?

Just now

Powered by **FluentBot**


---

---

## Model Relationships | FluentCart Developer Docs

**URL** : https://dev.fluentcart.com/database/models/relationships

[Skip to content](https://dev.fluentcart.com/database/models/relationships#VPContent)

# Model Relationships [​](https://dev.fluentcart.com/database/models/relationships\#model-relationships)

FluentCart uses Eloquent ORM relationships to establish connections between different models. Understanding these relationships is crucial for efficient data querying and manipulation.

## Relationship Types [​](https://dev.fluentcart.com/database/models/relationships\#relationship-types)

FluentCart models use the following relationship types:

- **One-to-One** \- Each model has one related model
- **One-to-Many** \- One model has many related models
- **Many-to-Many** \- Models can have multiple related models
- **Polymorphic** \- Models can relate to multiple different model types

## Core Model Relationships [​](https://dev.fluentcart.com/database/models/relationships\#core-model-relationships)

### Order Relationships [​](https://dev.fluentcart.com/database/models/relationships\#order-relationships)

The Order model is central to FluentCart and has multiple relationships:

php

```
// Order belongs to one Customer
$order = Order::find(1);
$customer = $order->customer;

// Order has many Order Items
$orderItems = $order->items;

// Order has many Transactions
$transactions = $order->transactions;

// Order has many Meta entries
$meta = $order->meta;

// Order belongs to one Subscription (optional)
$subscription = $order->subscription;
```

#### Order Model Relationships [​](https://dev.fluentcart.com/database/models/relationships\#order-model-relationships)

| Relationship | Type | Related Model | Foreign Key | Local Key |
| --- | --- | --- | --- | --- |
| customer | belongsTo | Customer | customer\_id | id |
| items | hasMany | OrderItem | order\_id | id |
| transactions | hasMany | OrderTransaction | order\_id | id |
| meta | hasMany | OrderMeta | order\_id | id |
| subscription | belongsTo | Subscription | subscription\_id | id |

### Customer Relationships [​](https://dev.fluentcart.com/database/models/relationships\#customer-relationships)

Customers are connected to multiple entities:

php

```
// Customer has many Orders
$customer = Customer::find(1);
$orders = $customer->orders;

// Customer has many Subscriptions
$subscriptions = $customer->subscriptions;

// Customer has many Activities
$activities = $customer->activities;

// Customer has many Carts
$carts = $customer->carts;

// Customer has many Licenses (Pro)
$licenses = $customer->licenses;
```

#### Customer Model Relationships [​](https://dev.fluentcart.com/database/models/relationships\#customer-model-relationships)

| Relationship | Type | Related Model | Foreign Key | Local Key |
| --- | --- | --- | --- | --- |
| orders | hasMany | Order | customer\_id | id |
| subscriptions | hasMany | Subscription | customer\_id | id |
| activities | hasMany | Activity | customer\_id | id |
| carts | hasMany | Cart | customer\_id | id |
| licenses | hasMany | License | customer\_id | id |

### Product Relationships [​](https://dev.fluentcart.com/database/models/relationships\#product-relationships)

Products have complex relationships for variations and metadata:

php

```
// Product has many Variations
$product = Product::find(1);
$variations = $product->variations;

// Product has many Order Items
$orderItems = $product->orderItems;

// Product has many Licenses (Pro)
$licenses = $product->licenses;

// Product belongs to many Categories (WordPress)
$categories = $product->categories;
```

#### Product Model Relationships [​](https://dev.fluentcart.com/database/models/relationships\#product-model-relationships)

| Relationship | Type | Related Model | Foreign Key | Local Key |
| --- | --- | --- | --- | --- |
| variations | hasMany | ProductVariation | product\_id | ID |
| orderItems | hasMany | OrderItem | post\_id | ID |
| licenses | hasMany | License | product\_id | ID |
| categories | belongsToMany | Category | post\_id | term\_id |

### Subscription Relationships [​](https://dev.fluentcart.com/database/models/relationships\#subscription-relationships)

Subscriptions connect customers to recurring orders:

php

```
// Subscription belongs to one Customer
$subscription = Subscription::find(1);
$customer = $subscription->customer;

// Subscription has many Orders
$orders = $subscription->orders;

// Subscription has many Transactions
$transactions = $subscription->transactions;

// Subscription has many Licenses (Pro)
$licenses = $subscription->licenses;
```

#### Subscription Model Relationships [​](https://dev.fluentcart.com/database/models/relationships\#subscription-model-relationships)

| Relationship | Type | Related Model | Foreign Key | Local Key |
| --- | --- | --- | --- | --- |
| customer | belongsTo | Customer | customer\_id | id |
| orders | hasMany | Order | subscription\_id | id |
| transactions | hasMany | OrderTransaction | subscription\_id | id |
| licenses | hasMany | License | subscription\_id | id |

## Pro Plugin Relationships [​](https://dev.fluentcart.com/database/models/relationships\#pro-plugin-relationships)

### License Relationships (Pro) [​](https://dev.fluentcart.com/database/models/relationships\#license-relationships-pro)

Licenses have relationships with multiple entities:

php

```
// License belongs to one Customer
$license = License::find(1);
$customer = $license->customer;

// License belongs to one Product
$product = $license->product;

// License belongs to one Order
$order = $license->order;

// License belongs to one Subscription (optional)
$subscription = $license->subscription;

// License has many Activations
$activations = $license->activations;

// License has many Meta entries
$meta = $license->meta;

// License has many Transactions
$transactions = $license->transactions;
```

#### License Model Relationships [​](https://dev.fluentcart.com/database/models/relationships\#license-model-relationships)

| Relationship | Type | Related Model | Foreign Key | Local Key |
| --- | --- | --- | --- | --- |
| customer | belongsTo | Customer | customer\_id | id |
| product | belongsTo | Product | product\_id | ID |
| order | belongsTo | Order | order\_id | id |
| subscription | belongsTo | Subscription | subscription\_id | id |
| activations | hasMany | LicenseActivation | license\_id | id |
| meta | hasMany | LicenseMeta | license\_id | id |
| transactions | hasMany | LicenseTransaction | license\_id | id |

## Relationship Usage Examples [​](https://dev.fluentcart.com/database/models/relationships\#relationship-usage-examples)

### Eager Loading [​](https://dev.fluentcart.com/database/models/relationships\#eager-loading)

Prevent N+1 queries by eager loading relationships:

php

```
// Load orders with their customers and items
$orders = Order::with(['customer', 'items', 'transactions'])->get();

// Load customers with their orders and subscriptions
$customers = Customer::with(['orders', 'subscriptions'])->get();

// Load products with their variations
$products = Product::with(['variations'])->get();
```

### Querying with Relationships [​](https://dev.fluentcart.com/database/models/relationships\#querying-with-relationships)

Use relationships in queries:

php

```
// Get orders for customers with specific email
$orders = Order::whereHas('customer', function($query) {
    $query->where('email', 'customer@example.com');
})->get();

// Get customers who have active subscriptions
$customers = Customer::whereHas('subscriptions', function($query) {
    $query->where('status', 'active');
})->get();

// Get products that have been ordered
$products = Product::whereHas('orderItems')->get();
```

### Filtering by Relationship Data [​](https://dev.fluentcart.com/database/models/relationships\#filtering-by-relationship-data)

php

```
// Get orders with total greater than $100
$orders = Order::whereHas('items', function($query) {
    $query->where('line_total', '>', 10000);
})->get();

// Get customers with orders in specific date range
$customers = Customer::whereHas('orders', function($query) {
    $query->whereBetween('created_at', ['2024-01-01', '2024-01-31']);
})->get();
```

### Counting Relationships [​](https://dev.fluentcart.com/database/models/relationships\#counting-relationships)

php

```
// Get customers with order count
$customers = Customer::withCount('orders')->get();

// Get products with order item count
$products = Product::withCount('orderItems')->get();

// Get orders with item count
$orders = Order::withCount('items')->get();
```

### Complex Relationship Queries [​](https://dev.fluentcart.com/database/models/relationships\#complex-relationship-queries)

php

```
// Get customers with their latest order
$customers = Customer::with(['orders' => function($query) {\
    $query->latest()->limit(1);\
}])->get();

// Get orders with their customer's subscription status
$orders = Order::with(['customer.subscriptions' => function($query) {\
    $query->where('status', 'active');\
}])->get();

// Get products with their most recent order
$products = Product::with(['orderItems.order' => function($query) {\
    $query->latest()->limit(1);\
}])->get();
```

## Relationship Best Practices [​](https://dev.fluentcart.com/database/models/relationships\#relationship-best-practices)

### 1\. Use Eager Loading [​](https://dev.fluentcart.com/database/models/relationships\#_1-use-eager-loading)

Always eager load relationships to prevent N+1 queries:

php

```
// Bad - N+1 queries
$orders = Order::all();
foreach ($orders as $order) {
    echo $order->customer->name; // N+1 query
}

// Good - Eager loading
$orders = Order::with('customer')->get();
foreach ($orders as $order) {
    echo $order->customer->name; // No additional queries
}
```

### 2\. Use Specific Columns [​](https://dev.fluentcart.com/database/models/relationships\#_2-use-specific-columns)

Only load the columns you need:

php

```
// Load only specific columns
$orders = Order::with(['customer:id,name,email'])->get();
```

### 3\. Use Constraints [​](https://dev.fluentcart.com/database/models/relationships\#_3-use-constraints)

Apply constraints to relationships:

php

```
// Load only active subscriptions
$customers = Customer::with(['subscriptions' => function($query) {\
    $query->where('status', 'active');\
}])->get();
```

### 4\. Use Lazy Loading Wisely [​](https://dev.fluentcart.com/database/models/relationships\#_4-use-lazy-loading-wisely)

Lazy load when you don't always need the relationship:

php

```
$order = Order::find(1);

// Only load when needed
if ($needCustomer) {
    $customer = $order->customer;
}
```

### 5\. Use Relationship Methods [​](https://dev.fluentcart.com/database/models/relationships\#_5-use-relationship-methods)

Use relationship methods for complex queries:

php

```
// Get orders for specific customer
$customer = Customer::find(1);
$orders = $customer->orders()->where('status', 'completed')->get();

// Get active subscriptions for customer
$activeSubscriptions = $customer->subscriptions()->active()->get();
```

## Common Relationship Patterns [​](https://dev.fluentcart.com/database/models/relationships\#common-relationship-patterns)

### 1\. Parent-Child Relationships [​](https://dev.fluentcart.com/database/models/relationships\#_1-parent-child-relationships)

php

```
// Order -> Order Items
$order = Order::find(1);
$items = $order->items;

// Customer -> Orders
$customer = Customer::find(1);
$orders = $customer->orders;
```

### 2\. Many-to-Many Relationships [​](https://dev.fluentcart.com/database/models/relationships\#_2-many-to-many-relationships)

php

```
// Product -> Categories
$product = Product::find(1);
$categories = $product->categories;

// Customer -> Products (through orders)
$customer = Customer::find(1);
$products = $customer->orders()->with('items.product')->get();
```

### 3\. Polymorphic Relationships [​](https://dev.fluentcart.com/database/models/relationships\#_3-polymorphic-relationships)

php

```
// Activities can belong to different models
$activities = Activity::where('object_type', 'order')
    ->where('object_id', 1)
    ->get();
```

## Performance Considerations [​](https://dev.fluentcart.com/database/models/relationships\#performance-considerations)

### 1\. Index Foreign Keys [​](https://dev.fluentcart.com/database/models/relationships\#_1-index-foreign-keys)

Ensure foreign key columns are indexed:

sql

```
-- Add indexes for better performance
ALTER TABLE fct_orders ADD INDEX idx_customer_id (customer_id);
ALTER TABLE fct_order_items ADD INDEX idx_order_id (order_id);
ALTER TABLE fct_subscriptions ADD INDEX idx_customer_id (customer_id);
```

### 2\. Use Query Scopes [​](https://dev.fluentcart.com/database/models/relationships\#_2-use-query-scopes)

Create scopes for common relationship queries:

php

```
// In Order model
public function scopeWithCustomer($query) {
    return $query->with('customer');
}

public function scopeWithItems($query) {
    return $query->with('items');
}

// Usage
$orders = Order::withCustomer()->withItems()->get();
```

### 3\. Cache Relationship Data [​](https://dev.fluentcart.com/database/models/relationships\#_3-cache-relationship-data)

Cache frequently accessed relationship data:

php

```
// Cache customer orders
$customer = Customer::find(1);
$orders = Cache::remember("customer_{$customer->id}_orders", 3600, function() use ($customer) {
    return $customer->orders()->with('items')->get();
});
```

* * *

Today

Hi! I’m your AI assistant. How can I assist you today?

Just now

Powered by **FluentBot**


---

---

## Scheduled Action Model | FluentCart Developer Docs

**URL** : https://dev.fluentcart.com/database/models/scheduled-action

[Skip to content](https://dev.fluentcart.com/database/models/scheduled-action#VPContent)

# Scheduled Action Model [​](https://dev.fluentcart.com/database/models/scheduled-action\#scheduled-action-model)

| DB Table Name | {wp\_db\_prefix}\_fct\_scheduled\_actions |
| --- | --- |
| Schema | [Check Schema](https://dev.fluentcart.com/database/schema.html#fct-scheduled-actions-table) |
| Source File | fluent-cart/app/Models/ScheduledAction.php |
| Name Space | FluentCart\\App\\Models |
| Class | FluentCart\\App\\Models\\ScheduledAction |

## Guarded & Fillable [​](https://dev.fluentcart.com/database/models/scheduled-action\#guarded-fillable)

This model uses both `$guarded` and `$fillable`:

- **Guarded:**`['id']`
- **Fillable:**`['scheduled_at', 'action', 'status', 'group', 'object_id', 'object_type', 'completed_at', 'retry_count', 'data', 'response_note']`

## Attributes [​](https://dev.fluentcart.com/database/models/scheduled-action\#attributes)

| Attribute | Data Type | Comment |
| --- | --- | --- |
| id | Integer | Primary Key (guarded) |
| scheduled\_at | Date Time | When the action is scheduled to run |
| action | String | Action to be performed |
| status | String | Action status (pending, completed, failed) |
| group | String | Action group |
| object\_id | Integer | ID of the associated object |
| object\_type | String | Type of the associated object |
| completed\_at | Date Time | When the action was completed |
| retry\_count | Integer | Number of retry attempts |
| data | JSON | Action data and parameters (manual JSON mutator/accessor) |
| response\_note | String | Response or error note |
| created\_at | Date Time | Creation timestamp |
| updated\_at | Date Time | Last update timestamp |

## Usage [​](https://dev.fluentcart.com/database/models/scheduled-action\#usage)

Please check [Model Basic](https://dev.fluentcart.com/database/models.html) for Common methods.

### Accessing Attributes [​](https://dev.fluentcart.com/database/models/scheduled-action\#accessing-attributes)

php

```
$scheduledAction = FluentCart\App\Models\ScheduledAction::find(1);

$scheduledAction->id; // returns id
$scheduledAction->scheduled_at; // returns scheduled time
$scheduledAction->action; // returns action name
$scheduledAction->status; // returns status
$scheduledAction->data; // returns array (accessor)
$scheduledAction->response_note; // returns response note
```

## Methods [​](https://dev.fluentcart.com/database/models/scheduled-action\#methods)

Along with Global Model methods, this model has few helper methods.

### setDataAttribute($value) [​](https://dev.fluentcart.com/database/models/scheduled-action\#setdataattribute-value)

Set data with automatic JSON encoding (mutator). If the value is an array or object, it is encoded with `json_encode()`. Otherwise the raw value is stored as-is.

- Parameters
  - $value - mixed (array, object, or string)
- Returns `void`

#### Usage [​](https://dev.fluentcart.com/database/models/scheduled-action\#usage-1)

php

```
$scheduledAction->data = ['param1' => 'value1', 'param2' => 'value2'];
// Automatically JSON encodes arrays and objects
```

### getDataAttribute($value) [​](https://dev.fluentcart.com/database/models/scheduled-action\#getdataattribute-value)

Get data with automatic JSON decoding (accessor). Decodes the stored JSON string into an associative array.

- Parameters
  - $value - mixed
- Returns `array` \- Decoded array, or empty array if decoding fails or value is not a valid JSON array

#### Usage [​](https://dev.fluentcart.com/database/models/scheduled-action\#usage-2)

php

```
$data = $scheduledAction->data; // Returns decoded array
```

## Usage Examples [​](https://dev.fluentcart.com/database/models/scheduled-action\#usage-examples)

### Get Scheduled Actions [​](https://dev.fluentcart.com/database/models/scheduled-action\#get-scheduled-actions)

php

```
$scheduledAction = FluentCart\App\Models\ScheduledAction::find(1);
echo "Action: " . $scheduledAction->action;
echo "Status: " . $scheduledAction->status;
echo "Scheduled At: " . $scheduledAction->scheduled_at;
```

### Get Pending Actions [​](https://dev.fluentcart.com/database/models/scheduled-action\#get-pending-actions)

php

```
$pendingActions = FluentCart\App\Models\ScheduledAction::where('status', 'pending')
    ->where('scheduled_at', '<=', now())
    ->get();

foreach ($pendingActions as $action) {
    echo "Action: " . $action->action;
    echo "Data: " . print_r($action->data, true);
}
```

### Create Scheduled Action [​](https://dev.fluentcart.com/database/models/scheduled-action\#create-scheduled-action)

php

```
$scheduledAction = FluentCart\App\Models\ScheduledAction::create([\
    'scheduled_at' => now()->addHours(1),\
    'action' => 'send_email',\
    'status' => 'pending',\
    'group' => 'notifications',\
    'object_id' => 123,\
    'object_type' => 'order',\
    'data' => [\
        'email' => 'customer@example.com',\
        'template' => 'order_confirmation',\
        'order_id' => 123\
    ]\
]);
```

### Get Actions by Group [​](https://dev.fluentcart.com/database/models/scheduled-action\#get-actions-by-group)

php

```
$emailActions = FluentCart\App\Models\ScheduledAction::where('group', 'notifications')->get();
$webhookActions = FluentCart\App\Models\ScheduledAction::where('group', 'webhooks')->get();
```

### Get Failed Actions [​](https://dev.fluentcart.com/database/models/scheduled-action\#get-failed-actions)

php

```
$failedActions = FluentCart\App\Models\ScheduledAction::where('status', 'failed')
    ->where('retry_count', '<', 3)
    ->get();
```

### Mark Action as Completed [​](https://dev.fluentcart.com/database/models/scheduled-action\#mark-action-as-completed)

php

```
$action = FluentCart\App\Models\ScheduledAction::find(1);
$action->status = 'completed';
$action->completed_at = now();
$action->response_note = 'Successfully processed';
$action->save();
```

### Get Actions for Object [​](https://dev.fluentcart.com/database/models/scheduled-action\#get-actions-for-object)

php

```
$orderActions = FluentCart\App\Models\ScheduledAction::where('object_type', 'order')
    ->where('object_id', 123)
    ->get();
```

### Retry Failed Action [​](https://dev.fluentcart.com/database/models/scheduled-action\#retry-failed-action)

php

```
$failedAction = FluentCart\App\Models\ScheduledAction::where('status', 'failed')
    ->where('retry_count', '<', 3)
    ->first();

if ($failedAction) {
    $failedAction->status = 'pending';
    $failedAction->retry_count = $failedAction->retry_count + 1;
    $failedAction->scheduled_at = now()->addMinutes(5);
    $failedAction->save();
}
```

* * *

Today

Hi! I’m your AI assistant. How can I assist you today?

Just now

Powered by **FluentBot**


---

---

## Shipping Class Model | FluentCart Developer Docs

**URL** : https://dev.fluentcart.com/database/models/shipping-class

[Skip to content](https://dev.fluentcart.com/database/models/shipping-class#VPContent)

# Shipping Class Model [​](https://dev.fluentcart.com/database/models/shipping-class\#shipping-class-model)

| DB Table Name | {wp\_db\_prefix}\_fct\_shipping\_classes |
| --- | --- |
| Schema | [Check Schema](https://dev.fluentcart.com/database/schema.html#fct-shipping-classes-table) |
| Source File | fluent-cart/app/Models/ShippingClass.php |
| Name Space | FluentCart\\App\\Models |
| Class | FluentCart\\App\\Models\\ShippingClass |

## Traits [​](https://dev.fluentcart.com/database/models/shipping-class\#traits)

- `FluentCart\App\Models\Concerns\CanSearch` \- Provides `search()`, `groupSearch()`, `whereLike()`, `whereBeginsWith()`, `whereEndsWith()` scopes

## Casts [​](https://dev.fluentcart.com/database/models/shipping-class\#casts)

| Attribute | Cast Type |
| --- | --- |
| cost | float |

## Attributes [​](https://dev.fluentcart.com/database/models/shipping-class\#attributes)

| Attribute | Data Type | Comment |
| --- | --- | --- |
| id | Integer | Primary Key |
| name | String | Shipping class name |
| cost | Float | Shipping cost (cast to float) |
| type | String | Shipping class type |
| per\_item | Boolean | Whether cost is per item |
| created\_at | Date Time | Creation timestamp |
| updated\_at | Date Time | Last update timestamp |

## Usage [​](https://dev.fluentcart.com/database/models/shipping-class\#usage)

Please check [Model Basic](https://dev.fluentcart.com/database/models.html) for Common methods.

### Accessing Attributes [​](https://dev.fluentcart.com/database/models/shipping-class\#accessing-attributes)

php

```
$shippingClass = FluentCart\App\Models\ShippingClass::find(1);

$shippingClass->id; // returns id
$shippingClass->name; // returns name
$shippingClass->cost; // returns cost (cast to float)
$shippingClass->type; // returns type
$shippingClass->per_item; // returns per_item flag
```

## Relations [​](https://dev.fluentcart.com/database/models/shipping-class\#relations)

This model does not currently define any relationships.

Note

A `products` relationship (`hasMany` to `Product`) is planned but not yet implemented in the source code.

## Usage Examples [​](https://dev.fluentcart.com/database/models/shipping-class\#usage-examples)

### Get Shipping Classes [​](https://dev.fluentcart.com/database/models/shipping-class\#get-shipping-classes)

php

```
$shippingClass = FluentCart\App\Models\ShippingClass::find(1);
echo "Name: " . $shippingClass->name;
echo "Cost: " . $shippingClass->cost;
echo "Type: " . $shippingClass->type;
echo "Per Item: " . ($shippingClass->per_item ? 'Yes' : 'No');
```

### Create Shipping Class [​](https://dev.fluentcart.com/database/models/shipping-class\#create-shipping-class)

php

```
$shippingClass = FluentCart\App\Models\ShippingClass::create([\
    'name' => 'Standard Shipping',\
    'cost' => 5.99,\
    'type' => 'standard',\
    'per_item' => false\
]);
```

### Get All Shipping Classes [​](https://dev.fluentcart.com/database/models/shipping-class\#get-all-shipping-classes)

php

```
$shippingClasses = FluentCart\App\Models\ShippingClass::all();

foreach ($shippingClasses as $class) {
    echo "Class: " . $class->name . " - Cost: $" . $class->cost;
}
```

### Get Shipping Classes by Type [​](https://dev.fluentcart.com/database/models/shipping-class\#get-shipping-classes-by-type)

php

```
$standardClasses = FluentCart\App\Models\ShippingClass::where('type', 'standard')->get();
$expressClasses = FluentCart\App\Models\ShippingClass::where('type', 'express')->get();
```

### Get Per-Item Shipping Classes [​](https://dev.fluentcart.com/database/models/shipping-class\#get-per-item-shipping-classes)

php

```
$perItemClasses = FluentCart\App\Models\ShippingClass::where('per_item', true)->get();
$flatRateClasses = FluentCart\App\Models\ShippingClass::where('per_item', false)->get();
```

### Update Shipping Class [​](https://dev.fluentcart.com/database/models/shipping-class\#update-shipping-class)

php

```
$shippingClass = FluentCart\App\Models\ShippingClass::find(1);
$shippingClass->update([\
    'cost' => 7.99,\
    'per_item' => true\
]);
```

### Get Shipping Classes by Cost Range [​](https://dev.fluentcart.com/database/models/shipping-class\#get-shipping-classes-by-cost-range)

php

```
$lowCostClasses = FluentCart\App\Models\ShippingClass::where('cost', '<', 10.00)->get();
$highCostClasses = FluentCart\App\Models\ShippingClass::where('cost', '>=', 10.00)->get();
```

### Delete Shipping Class [​](https://dev.fluentcart.com/database/models/shipping-class\#delete-shipping-class)

php

```
$shippingClass = FluentCart\App\Models\ShippingClass::find(1);
$shippingClass->delete();
```

### Get Shipping Classes Ordered by Cost [​](https://dev.fluentcart.com/database/models/shipping-class\#get-shipping-classes-ordered-by-cost)

php

```
$orderedClasses = FluentCart\App\Models\ShippingClass::orderBy('cost', 'asc')->get();
```

### Search Shipping Classes [​](https://dev.fluentcart.com/database/models/shipping-class\#search-shipping-classes)

php

```
$searchResults = FluentCart\App\Models\ShippingClass::whereLike('name', 'Standard')->get();
```

* * *

Today

Hi! I’m your AI assistant. How can I assist you today?

Just now

Powered by **FluentBot**


---

---

## Shipping Method Model | FluentCart Developer Docs

**URL** : https://dev.fluentcart.com/database/models/shipping-method

[Skip to content](https://dev.fluentcart.com/database/models/shipping-method#VPContent)

# Shipping Method Model [​](https://dev.fluentcart.com/database/models/shipping-method\#shipping-method-model)

| DB Table Name | {wp\_db\_prefix}\_fct\_shipping\_methods |
| --- | --- |
| Schema | [Check Schema](https://dev.fluentcart.com/database/schema.html#fct-shipping-methods-table) |
| Source File | fluent-cart/app/Models/ShippingMethod.php |
| Name Space | FluentCart\\App\\Models |
| Class | FluentCart\\App\\Models\\ShippingMethod |

## Traits [​](https://dev.fluentcart.com/database/models/shipping-method\#traits)

- `FluentCart\App\Models\Concerns\CanSearch` \- Provides `search()`, `groupSearch()`, `whereLike()`, `whereBeginsWith()`, `whereEndsWith()` scopes

## Appended Attributes [​](https://dev.fluentcart.com/database/models/shipping-method\#appended-attributes)

The following computed attributes are automatically appended to the model's array/JSON output:

- `formatted_states` \- Array of human-readable state names

## Casts [​](https://dev.fluentcart.com/database/models/shipping-method\#casts)

| Attribute | Cast Type |
| --- | --- |
| settings | array |
| states | array |
| is\_enabled | boolean |

## Default Attribute Values [​](https://dev.fluentcart.com/database/models/shipping-method\#default-attribute-values)

| Attribute | Default |
| --- | --- |
| states | `'[]'` |

## Attributes [​](https://dev.fluentcart.com/database/models/shipping-method\#attributes)

| Attribute | Data Type | Comment |
| --- | --- | --- |
| id | Integer | Primary Key |
| zone\_id | Integer | Reference to shipping zone |
| title | String | Shipping method title |
| type | String | Shipping method type |
| settings | Array | Shipping method settings (cast to array) |
| amount | Decimal | Shipping amount |
| is\_enabled | Boolean | Whether method is enabled (cast to boolean) |
| order | Integer | Display order |
| states | Array | Applicable states (cast to array, defaults to empty array) |
| meta | JSON | Additional metadata (manual JSON mutator/accessor) |
| created\_at | Date Time | Creation timestamp |
| updated\_at | Date Time | Last update timestamp |

## Usage [​](https://dev.fluentcart.com/database/models/shipping-method\#usage)

Please check [Model Basic](https://dev.fluentcart.com/database/models.html) for Common methods.

### Accessing Attributes [​](https://dev.fluentcart.com/database/models/shipping-method\#accessing-attributes)

php

```
$shippingMethod = FluentCart\App\Models\ShippingMethod::find(1);

$shippingMethod->id; // returns id
$shippingMethod->zone_id; // returns zone ID
$shippingMethod->title; // returns title
$shippingMethod->amount; // returns amount
$shippingMethod->is_enabled; // returns boolean
$shippingMethod->settings; // returns array (cast)
$shippingMethod->states; // returns array (cast)
$shippingMethod->meta; // returns array (accessor)
$shippingMethod->formatted_states; // returns array of formatted state names (appended attribute)
```

## Scopes [​](https://dev.fluentcart.com/database/models/shipping-method\#scopes)

This model has the following scopes that you can use

### applicableToCountry($country, $state) [​](https://dev.fluentcart.com/database/models/shipping-method\#applicabletocountry-country-state)

Filter methods applicable to a specific country and state. This scope:

1. Filters by zone region matching the country or `'all'`
2. Filters by states -- includes methods with empty states array, or methods whose states contain the given state
3. Orders results by `amount` descending
4. Only returns enabled methods (`is_enabled = 1`)

Supports both MySQL (using JSON functions) and SQLite (using string search) for state filtering.

- Parameters
  - $country - string (country code)
  - $state - string\|null (state code)

#### Usage: [​](https://dev.fluentcart.com/database/models/shipping-method\#usage-1)

php

```
// Get methods applicable to US, California
$methods = FluentCart\App\Models\ShippingMethod::applicableToCountry('US', 'CA')->get();

// Get methods applicable to US, any state
$methods = FluentCart\App\Models\ShippingMethod::applicableToCountry('US', null)->get();
```

## Relations [​](https://dev.fluentcart.com/database/models/shipping-method\#relations)

This model has the following relationships that you can use

### zone [​](https://dev.fluentcart.com/database/models/shipping-method\#zone)

Access the associated shipping zone

- return `FluentCart\App\Models\ShippingZone` Model

#### Example: [​](https://dev.fluentcart.com/database/models/shipping-method\#example)

php

```
// Accessing Zone
$zone = $shippingMethod->zone;

// For Filtering by zone relationship
$shippingMethods = FluentCart\App\Models\ShippingMethod::whereHas('zone', function($query) {
    $query->where('region', 'US');
})->get();
```

## Methods [​](https://dev.fluentcart.com/database/models/shipping-method\#methods)

Along with Global Model methods, this model has few helper methods.

### getFormattedStatesAttribute() [​](https://dev.fluentcart.com/database/models/shipping-method\#getformattedstatesattribute)

Get formatted states array (accessor). Maps each state code to its human-readable name using `AddressHelper::getStateNameByCode()`, resolving against the zone's region.

- Parameters
  - none
- Returns `array` \- Array of formatted state name strings, or empty array if states is not an array

#### Usage [​](https://dev.fluentcart.com/database/models/shipping-method\#usage-2)

php

```
$formattedStates = $shippingMethod->formatted_states; // Returns array of formatted state names
```

### setMetaAttribute($value) [​](https://dev.fluentcart.com/database/models/shipping-method\#setmetaattribute-value)

Set meta with automatic JSON encoding (mutator). Encodes the value with `json_encode()`. Falls back to `'[]'` if encoding fails or value is falsy.

- Parameters
  - $value - mixed (array, object, or string)
- Returns `void`

#### Usage [​](https://dev.fluentcart.com/database/models/shipping-method\#usage-3)

php

```
$shippingMethod->meta = ['custom_data' => 'value', 'settings' => ['key' => 'value']];
// Automatically JSON encodes arrays and objects
```

### getMetaAttribute($value) [​](https://dev.fluentcart.com/database/models/shipping-method\#getmetaattribute-value)

Get meta with automatic JSON decoding (accessor). Decodes the stored JSON string into an associative array.

- Parameters
  - $value - mixed
- Returns `array` \- Decoded array, or empty array if value is falsy

#### Usage [​](https://dev.fluentcart.com/database/models/shipping-method\#usage-4)

php

```
$meta = $shippingMethod->meta; // Returns decoded array
```

## Usage Examples [​](https://dev.fluentcart.com/database/models/shipping-method\#usage-examples)

### Get Shipping Methods [​](https://dev.fluentcart.com/database/models/shipping-method\#get-shipping-methods)

php

```
$shippingMethod = FluentCart\App\Models\ShippingMethod::find(1);
echo "Title: " . $shippingMethod->title;
echo "Amount: " . $shippingMethod->amount;
echo "Enabled: " . ($shippingMethod->is_enabled ? 'Yes' : 'No');
```

### Create Shipping Method [​](https://dev.fluentcart.com/database/models/shipping-method\#create-shipping-method)

php

```
$shippingMethod = FluentCart\App\Models\ShippingMethod::create([\
    'zone_id' => 1,\
    'title' => 'Standard Shipping',\
    'type' => 'flat_rate',\
    'settings' => ['cost' => 5.99, 'free_shipping_threshold' => 50],\
    'amount' => 5.99,\
    'is_enabled' => true,\
    'order' => 1,\
    'states' => ['CA', 'NY', 'TX']\
]);
```

### Get Methods by Zone [​](https://dev.fluentcart.com/database/models/shipping-method\#get-methods-by-zone)

php

```
$zoneMethods = FluentCart\App\Models\ShippingMethod::where('zone_id', 1)->get();
```

### Get Enabled Methods [​](https://dev.fluentcart.com/database/models/shipping-method\#get-enabled-methods)

php

```
$enabledMethods = FluentCart\App\Models\ShippingMethod::where('is_enabled', true)->get();
```

### Get Methods Applicable to Country [​](https://dev.fluentcart.com/database/models/shipping-method\#get-methods-applicable-to-country)

php

```
// Get methods for US, California
$usMethods = FluentCart\App\Models\ShippingMethod::applicableToCountry('US', 'CA')->get();

// Get methods for US, any state
$usAllMethods = FluentCart\App\Models\ShippingMethod::applicableToCountry('US', null)->get();
```

### Get Methods with Zone Information [​](https://dev.fluentcart.com/database/models/shipping-method\#get-methods-with-zone-information)

php

```
$methodsWithZones = FluentCart\App\Models\ShippingMethod::with('zone')->get();

foreach ($methodsWithZones as $method) {
    echo "Method: " . $method->title;
    echo "Zone: " . $method->zone->name;
}
```

### Get Methods by Type [​](https://dev.fluentcart.com/database/models/shipping-method\#get-methods-by-type)

php

```
$flatRateMethods = FluentCart\App\Models\ShippingMethod::where('type', 'flat_rate')->get();
$freeShippingMethods = FluentCart\App\Models\ShippingMethod::where('type', 'free_shipping')->get();
```

### Update Shipping Method [​](https://dev.fluentcart.com/database/models/shipping-method\#update-shipping-method)

php

```
$shippingMethod = FluentCart\App\Models\ShippingMethod::find(1);
$shippingMethod->update([\
    'amount' => 7.99,\
    'is_enabled' => false,\
    'meta' => ['updated' => true, 'timestamp' => now()]\
]);
```

### Get Methods Ordered by Display Order [​](https://dev.fluentcart.com/database/models/shipping-method\#get-methods-ordered-by-display-order)

php

```
$orderedMethods = FluentCart\App\Models\ShippingMethod::orderBy('order', 'asc')->get();
```

### Get Methods with Formatted States [​](https://dev.fluentcart.com/database/models/shipping-method\#get-methods-with-formatted-states)

php

```
$methods = FluentCart\App\Models\ShippingMethod::where('zone_id', 1)->get();

foreach ($methods as $method) {
    echo "Method: " . $method->title;
    echo "States: " . implode(', ', $method->formatted_states);
}
```

* * *

Today

Hi! I’m your AI assistant. How can I assist you today?

Just now

Powered by **FluentBot**


---

---

## Shipping Zone Model | FluentCart Developer Docs

**URL** : https://dev.fluentcart.com/database/models/shipping-zone

[Skip to content](https://dev.fluentcart.com/database/models/shipping-zone#VPContent)

# Shipping Zone Model [​](https://dev.fluentcart.com/database/models/shipping-zone\#shipping-zone-model)

| DB Table Name | {wp\_db\_prefix}\_fct\_shipping\_zones |
| --- | --- |
| Schema | [Check Schema](https://dev.fluentcart.com/database/schema.html#fct-shipping-zones-table) |
| Source File | fluent-cart/app/Models/ShippingZone.php |
| Name Space | FluentCart\\App\\Models |
| Class | FluentCart\\App\\Models\\ShippingZone |

## Traits [​](https://dev.fluentcart.com/database/models/shipping-zone\#traits)

- `FluentCart\App\Models\Concerns\CanSearch` \- Provides `search()`, `groupSearch()`, `whereLike()`, `whereBeginsWith()`, `whereEndsWith()` scopes

## Appended Attributes [​](https://dev.fluentcart.com/database/models/shipping-zone\#appended-attributes)

The following computed attributes are automatically appended to the model's array/JSON output:

- `formatted_region` \- Human-readable region name

## Attributes [​](https://dev.fluentcart.com/database/models/shipping-zone\#attributes)

| Attribute | Data Type | Comment |
| --- | --- | --- |
| id | Integer | Primary Key |
| name | String | Shipping zone name |
| region | String | Region/country code (or `'all'` for whole world) |
| order | Integer | Display order |
| created\_at | Date Time | Creation timestamp |
| updated\_at | Date Time | Last update timestamp |

## Usage [​](https://dev.fluentcart.com/database/models/shipping-zone\#usage)

Please check [Model Basic](https://dev.fluentcart.com/database/models.html) for Common methods.

### Accessing Attributes [​](https://dev.fluentcart.com/database/models/shipping-zone\#accessing-attributes)

php

```
$shippingZone = FluentCart\App\Models\ShippingZone::find(1);

$shippingZone->id; // returns id
$shippingZone->name; // returns zone name
$shippingZone->region; // returns region code
$shippingZone->order; // returns display order
$shippingZone->formatted_region; // returns formatted region name (appended attribute)
```

## Relations [​](https://dev.fluentcart.com/database/models/shipping-zone\#relations)

This model has the following relationships that you can use

### methods [​](https://dev.fluentcart.com/database/models/shipping-zone\#methods)

Access all shipping methods in this zone. Results are ordered by `id` descending.

- return `FluentCart\App\Models\ShippingMethod` Model Collection

#### Example: [​](https://dev.fluentcart.com/database/models/shipping-zone\#example)

php

```
// Accessing Methods
$methods = $shippingZone->methods;

// For Filtering by methods relationship
$shippingZones = FluentCart\App\Models\ShippingZone::whereHas('methods', function($query) {
    $query->where('is_enabled', 1);
})->get();
```

## Methods [​](https://dev.fluentcart.com/database/models/shipping-zone\#methods-1)

Along with Global Model methods, this model has few helper methods.

### getFormattedRegionAttribute() [​](https://dev.fluentcart.com/database/models/shipping-zone\#getformattedregionattribute)

Get formatted region name (accessor). Returns `'Whole World'` if region is `'all'`, otherwise resolves the country code to its full name via `AddressHelper::getCountryNameByCode()`.

- Parameters
  - none
- Returns `string`

#### Usage [​](https://dev.fluentcart.com/database/models/shipping-zone\#usage-1)

php

```
$formattedRegion = $shippingZone->formatted_region; // e.g., "United States" or "Whole World"
```

## Usage Examples [​](https://dev.fluentcart.com/database/models/shipping-zone\#usage-examples)

### Get Shipping Zones [​](https://dev.fluentcart.com/database/models/shipping-zone\#get-shipping-zones)

php

```
$shippingZone = FluentCart\App\Models\ShippingZone::find(1);
echo "Zone Name: " . $shippingZone->name;
echo "Region: " . $shippingZone->region;
echo "Formatted Region: " . $shippingZone->formatted_region;
```

### Create Shipping Zone [​](https://dev.fluentcart.com/database/models/shipping-zone\#create-shipping-zone)

php

```
$shippingZone = FluentCart\App\Models\ShippingZone::create([\
    'name' => 'United States',\
    'region' => 'US',\
    'order' => 1\
]);
```

### Get Shipping Zones with Methods [​](https://dev.fluentcart.com/database/models/shipping-zone\#get-shipping-zones-with-methods)

php

```
$shippingZones = FluentCart\App\Models\ShippingZone::with('methods')->get();

foreach ($shippingZones as $zone) {
    echo "Zone: " . $zone->name;
    foreach ($zone->methods as $method) {
        echo "  - Method: " . $method->title;
    }
}
```

### Get Zones by Region [​](https://dev.fluentcart.com/database/models/shipping-zone\#get-zones-by-region)

php

```
$usZones = FluentCart\App\Models\ShippingZone::where('region', 'US')->get();
$allWorldZones = FluentCart\App\Models\ShippingZone::where('region', 'all')->get();
```

### Get Zones Ordered by Display Order [​](https://dev.fluentcart.com/database/models/shipping-zone\#get-zones-ordered-by-display-order)

php

```
$orderedZones = FluentCart\App\Models\ShippingZone::orderBy('order', 'asc')->get();
```

### Get Zones with Enabled Methods [​](https://dev.fluentcart.com/database/models/shipping-zone\#get-zones-with-enabled-methods)

php

```
$zonesWithEnabledMethods = FluentCart\App\Models\ShippingZone::whereHas('methods', function($query) {
    $query->where('is_enabled', 1);
})->get();
```

### Update Shipping Zone [​](https://dev.fluentcart.com/database/models/shipping-zone\#update-shipping-zone)

php

```
$shippingZone = FluentCart\App\Models\ShippingZone::find(1);
$shippingZone->update([\
    'name' => 'United States & Canada',\
    'order' => 2\
]);
```

### Get Zone by Name [​](https://dev.fluentcart.com/database/models/shipping-zone\#get-zone-by-name)

php

```
$zone = FluentCart\App\Models\ShippingZone::where('name', 'United States')->first();
```

### Get Zones with Method Count [​](https://dev.fluentcart.com/database/models/shipping-zone\#get-zones-with-method-count)

php

```
$zonesWithCounts = FluentCart\App\Models\ShippingZone::withCount('methods')->get();

foreach ($zonesWithCounts as $zone) {
    echo "Zone: " . $zone->name . " (" . $zone->methods_count . " methods)";
}
```

### Delete Shipping Zone [​](https://dev.fluentcart.com/database/models/shipping-zone\#delete-shipping-zone)

php

```
$shippingZone = FluentCart\App\Models\ShippingZone::find(1);
$shippingZone->delete();
```

* * *

Today

Hi! I’m your AI assistant. How can I assist you today?

Just now

Powered by **FluentBot**


---

---

