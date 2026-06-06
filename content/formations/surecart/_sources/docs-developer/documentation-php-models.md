---
source_url: https://developer.surecart.com/documentation/php-models
source: surecart-developer-docs
scraped: true
---

[Skip to main content](https://developer.surecart.com/documentation/php-models#content-area)

> ## Documentation Index
>
> Fetch the complete documentation index at: [https://developer.surecart.com/llms.txt](https://developer.surecart.com/llms.txt)
>
> Use this file to discover all available pages before exploring further.

**PHP Models = API Interface** — The PHP models provide a fluent, Laravel-like interface to the SureCart REST API. Each model corresponds directly to an API resource.

**Blocking HTTP requests** — Each model query makes a synchronous HTTP request to the SureCart API. Use in: AJAX/REST handlers, admin dashboard pages, WP-CLI commands, cron jobs. Avoid in front-end page rendering.

# [​](https://developer.surecart.com/documentation/php-models#retrieving) Retrieving

### Find by ID

```
use SureCart\Models\Product;
$product = Product::find('8ba8d60f-5277-4e6b-807c-dee8166446d5');
```

### Get multiple

```
$products = Product::get();
foreach ($products as $product) {
    echo $product->name;
}
```

### Where (query by parameters — match API endpoint query params)

```
$archived_products = Product::where(['archived' => false])->get();
```

### Paginate

```
$products = Product::where(['archived' => false])->paginate(['per_page' => 20, 'page' => 2]);
```

Returns: `['object', 'pagination' => ['count', 'limit', 'page'], 'data' => [...]]`

### First

```
$product = Product::where(['archived' => false])->first();
```

### Refresh

```
$freshProduct = $product->fresh(); // re-fetch, doesn't affect existing instance
$product->refresh();               // re-hydrate existing instance
```

# [​](https://developer.surecart.com/documentation/php-models#expanding-relations) Expanding Relations

### Single relation

```
$prices = \SureCart\Models\Price::with(['product'])->paginate(['page' => 1]);
```

### List relations

```
$products = \SureCart\Models\Product::with(['prices'])->paginate(['page' => 1]);
```

### Recursive / nested expansion

```
$orders = \SureCart\Models\Order::with([
   'checkout',
   'checkout.line_items',
   'line_item.price',
   'price.product'
])->paginate(['page' => 1]);
```

Max depth: 2 levels, max 10 objects per request. Works on `get`, `paginate`, `create`, and `update`.

# [​](https://developer.surecart.com/documentation/php-models#inserting-updating-and-deleting) Inserting, Updating, and Deleting

```
// Create
$product = Product::create(['name' => 'iPhone', 'description' => '...']);

// Update (static)
Product::update(['id' => $product_id, 'name' => 'iPhone Pro']);

// Update (instance)
$product = Product::find($product_id);
$product->name = 'iPhone Pro';
$product->save();

// Delete
$product->delete();
// or
Product::delete($product_id);
```

# [​](https://developer.surecart.com/documentation/php-models#error-handling) Error Handling

```
$product = Product::find('invalid-id');
if (is_wp_error($product)) {
    $error_message = $product->get_error_message();
    return;
}
echo $product->name;
```

# [​](https://developer.surecart.com/documentation/php-models#utility-methods) Utility Methods

```
$product->toArray();       // Convert to array
$product->toObject();      // Convert to stdClass
$product['name'];          // Array access (equivalent to $product->name)
$product->isDirty();       // true if unsaved changes
$product->getDirty();      // ['name' => 'New Name']
```

# [​](https://developer.surecart.com/documentation/php-models#available-models) Available Models (namespace: `SureCart\Models`)

**Products:** `Product`, `Price`, `ProductCollection`, `ProductGroup`, `ProductMedia`, `Variant`, `VariantOption`, `Bump`, `Upsell`, `UpsellFunnel`, `Swap`, `Download`, `Coupon`, `Promotion`

**Customers:** `Customer`, `BalanceTransaction`

**Orders & Payments:** `Order`, `Checkout`, `AbandonedCheckout`, `LineItem`, `Purchase`, `Charge`, `Invoice`, `Refund`, `PaymentIntent`, `PaymentMethod`, `ManualPaymentMethod`, `Processor`, `Fee`, `Dispute`

**Subscriptions:** `Subscription`, `Period`, `CancellationAct`, `CancellationReason`

**Shipping & Fulfillment:** `Fulfillment`, `FulfillmentItem`, `ShippingMethod`, `ShippingProfile`, `ShippingRate`, `ShippingZone`, `ReturnRequest`, `ReturnItem`

**Tax:** `TaxRegistration`, `TaxZone`

**Licensing:** `License`, `Activation`

**Affiliates:** `Affiliation`, `AffiliationRequest`, `AffiliationProduct`, `Referral`, `ReferralItem`, `Payout`, `PayoutGroup`, `Click`

**Media:** `Media`

**Account & Settings:** `Account`, `Brand`, `Webhook`

**Reviews:** `Review`

**Other:** `Event`, `Export`
