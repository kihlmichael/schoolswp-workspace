# FluentCart Developer Docs - Database Models (Part 2/8)

Tous les modèles Eloquent exposés par FluentCart : orders, customers, products, subscriptions, coupons, licenses, taxes, shipping, etc.

---

## Cart Model | FluentCart Developer Docs

**URL** : https://dev.fluentcart.com/database/models/cart

[Skip to content](https://dev.fluentcart.com/database/models/cart#VPContent)

# Cart Model [​](https://dev.fluentcart.com/database/models/cart\#cart-model)

| DB Table Name | {wp\_db\_prefix}\_fct\_carts |
| --- | --- |
| Schema | [Check Schema](https://dev.fluentcart.com/database/schema.html#fct-carts-table) |
| Source File | fluent-cart/app/Models/Cart.php |
| Name Space | FluentCart\\App\\Models |
| Class | FluentCart\\App\\Models\\Cart |

## Primary Key [​](https://dev.fluentcart.com/database/models/cart\#primary-key)

The Cart model uses `cart_hash` (a string) as its primary key instead of the usual auto-incrementing `id`. The model sets `$incrementing = false` to reflect this. When creating a new Cart without providing a `cart_hash`, the `boot()` method auto-generates one using `md5('fct_global_cart_' . wp_generate_uuid4() . time())`.

## Traits [​](https://dev.fluentcart.com/database/models/cart\#traits)

- **CanSearch** \- Adds search scope capabilities to the model.

## Hidden Attributes [​](https://dev.fluentcart.com/database/models/cart\#hidden-attributes)

The following attributes are hidden from array/JSON serialization: `order_id`, `customer_id`, `user_id`.

## Attributes [​](https://dev.fluentcart.com/database/models/cart\#attributes)

| Attribute | Data Type | Comment |
| --- | --- | --- |
| cart\_hash | String | Primary Key (non-incrementing) - Unique cart hash, auto-generated on creation |
| customer\_id | Integer | Customer ID (nullable, hidden) |
| user\_id | Integer | WordPress user ID (nullable, hidden) |
| order\_id | Integer | Associated order ID (nullable, hidden) |
| checkout\_data | JSON | Checkout data (auto JSON encoded/decoded via accessor/mutator) |
| cart\_data | JSON | Cart items data (auto JSON encoded/decoded via accessor/mutator, loads bundle children on read) |
| utm\_data | JSON | UTM tracking data (auto JSON encoded/decoded via accessor/mutator) |
| coupons | JSON | Applied coupon codes (auto JSON encoded/decoded via accessor/mutator) |
| first\_name | String | Customer first name |
| last\_name | String | Customer last name |
| email | String | Customer email |
| stage | String | Cart stage (e.g. `completed`) |
| cart\_group | String | Cart group identifier |
| user\_agent | Text | User agent string |
| ip\_address | String | Customer IP address |
| completed\_at | Date Time | Completion timestamp |
| deleted\_at | Date Time | Soft delete timestamp |
| created\_at | Date Time | Creation timestamp |
| updated\_at | Date Time | Last update timestamp |

## Usage [​](https://dev.fluentcart.com/database/models/cart\#usage)

Please check [Model Basic](https://dev.fluentcart.com/database/models.html) for Common methods.

### Accessing Attributes [​](https://dev.fluentcart.com/database/models/cart\#accessing-attributes)

php

```
$cart = FluentCart\App\Models\Cart::find('cart_hash_123');

$cart->cart_hash; // returns cart hash (primary key)
$cart->customer_id; // returns customer ID
$cart->cart_data; // returns decoded cart items array (with bundle children loaded)
$cart->checkout_data; // returns decoded checkout data array
$cart->coupons; // returns decoded coupon codes array
$cart->utm_data; // returns decoded UTM data array
```

## Methods [​](https://dev.fluentcart.com/database/models/cart\#methods)

Along with Global Model methods, this model has the following helper methods.

### Attribute Accessors / Mutators [​](https://dev.fluentcart.com/database/models/cart\#attribute-accessors-mutators)

#### setCheckoutDataAttribute($settings) [​](https://dev.fluentcart.com/database/models/cart\#setcheckoutdataattribute-settings)

Set checkout data with JSON encoding.

- Parameters: `$settings` (Array) - Checkout settings

php

```
$cart = FluentCart\App\Models\Cart::find('cart_hash_123');
$cart->checkout_data = ['shipping_method' => 'standard'];
```

#### getCheckoutDataAttribute($settings) [​](https://dev.fluentcart.com/database/models/cart\#getcheckoutdataattribute-settings)

Get checkout data with JSON decoding. Returns an empty array if value is falsy or not valid JSON.

- Parameters: `$settings` (String) - Raw JSON settings from database
- Returns `Array` \- Decoded checkout data

php

```
$cart = FluentCart\App\Models\Cart::find('cart_hash_123');
$checkoutData = $cart->checkout_data; // returns array
```

#### setCouponsAttribute($coupons) [​](https://dev.fluentcart.com/database/models/cart\#setcouponsattribute-coupons)

Set coupons with JSON encoding. Non-array values are reset to an empty array.

- Parameters: `$coupons` (Array) - Coupon codes

php

```
$cart = FluentCart\App\Models\Cart::find('cart_hash_123');
$cart->coupons = ['SAVE10', 'WELCOME20'];
```

#### getCouponsAttribute($coupons) [​](https://dev.fluentcart.com/database/models/cart\#getcouponsattribute-coupons)

Get coupons with JSON decoding. Returns an empty array if value is falsy or not valid JSON.

- Parameters: `$coupons` (String) - Raw JSON coupons from database
- Returns `Array` \- Decoded coupon codes

php

```
$cart = FluentCart\App\Models\Cart::find('cart_hash_123');
$coupons = $cart->coupons; // returns array
```

#### setCartDataAttribute($settings) [​](https://dev.fluentcart.com/database/models/cart\#setcartdataattribute-settings)

Set cart data with JSON encoding. Also invalidates the internal static cache for this cart.

- Parameters: `$settings` (Array) - Cart item data

php

```
$cart = FluentCart\App\Models\Cart::find('cart_hash_123');
$cart->cart_data = [['product_id' => 1, 'quantity' => 2]];
```

#### getCartDataAttribute($data) [​](https://dev.fluentcart.com/database/models/cart\#getcartdataattribute-data)

Get cart data with JSON decoding. Uses an internal static cache keyed by `cart_hash` for performance. Automatically loads bundle child items via `Helper::loadBundleChild()`.

- Parameters: `$data` (String) - Raw JSON data from database
- Returns `Array` \- Decoded cart data with bundle children resolved

php

```
$cart = FluentCart\App\Models\Cart::find('cart_hash_123');
$cartData = $cart->cart_data; // returns array with bundle children loaded
```

#### setUtmDataAttribute($utmData) [​](https://dev.fluentcart.com/database/models/cart\#setutmdataattribute-utmdata)

Set UTM data with JSON encoding.

- Parameters: `$utmData` (Array) - UTM data

php

```
$cart = FluentCart\App\Models\Cart::find('cart_hash_123');
$cart->utm_data = ['utm_source' => 'google', 'utm_campaign' => 'summer'];
```

#### getUtmDataAttribute($utmData) [​](https://dev.fluentcart.com/database/models/cart\#getutmdataattribute-utmdata)

Get UTM data with JSON decoding. Returns an empty array if value is falsy.

- Parameters: `$utmData` (String) - Raw JSON UTM data from database
- Returns `Array` \- Decoded UTM data

php

```
$cart = FluentCart\App\Models\Cart::find('cart_hash_123');
$utmData = $cart->utm_data; // returns array
```

### Cart State Methods [​](https://dev.fluentcart.com/database/models/cart\#cart-state-methods)

#### isLocked() [​](https://dev.fluentcart.com/database/models/cart\#islocked)

Check if cart is locked. A cart is locked when `checkout_data.is_locked` is `'yes'` AND the cart has an associated `order_id`.

- Returns `Boolean` \- True if cart is locked

php

```
$cart = FluentCart\App\Models\Cart::find('cart_hash_123');
$isLocked = $cart->isLocked();
```

#### isZeroPayment() [​](https://dev.fluentcart.com/database/models/cart\#iszeropayment)

Check if the cart has a zero payment amount and does not contain subscription items. Useful for determining if payment processing can be skipped.

- Returns `Boolean` \- True if estimated total is zero and no subscription items exist

php

```
$cart = FluentCart\App\Models\Cart::find('cart_hash_123');
if ($cart->isZeroPayment()) {
    // No payment processing needed
}
```

#### isShipToDifferent() [​](https://dev.fluentcart.com/database/models/cart\#isshiptodifferent)

Check if the customer has opted to ship to a different address than the billing address.

- Returns `Boolean` \- True if `checkout_data.form_data.ship_to_different` is `'yes'`

php

```
$cart = FluentCart\App\Models\Cart::find('cart_hash_123');
if ($cart->isShipToDifferent()) {
    // Use separate shipping address
}
```

#### hasSubscription() [​](https://dev.fluentcart.com/database/models/cart\#hassubscription)

Check if cart contains any subscription items by inspecting `other_info.payment_type` in each cart data item.

- Returns `Boolean` \- True if any item has a `subscription` payment type

php

```
$cart = FluentCart\App\Models\Cart::find('cart_hash_123');
$hasSubscription = $cart->hasSubscription();
```

#### requireShipping() [​](https://dev.fluentcart.com/database/models/cart\#requireshipping)

Check if cart requires shipping by inspecting `fulfillment_type` in each cart data item.

- Returns `Boolean` \- True if any item has a `physical` fulfillment type

php

```
$cart = FluentCart\App\Models\Cart::find('cart_hash_123');
$requiresShipping = $cart->requireShipping();
```

### Cart Item Methods [​](https://dev.fluentcart.com/database/models/cart\#cart-item-methods)

#### addItem($item = \[\], $replacingIndex = null) [​](https://dev.fluentcart.com/database/models/cart\#additem-item-replacingindex-null)

Add an item to the cart. If the cart is locked, returns a `WP_Error`. If `$replacingIndex` is provided and exists, replaces that item; otherwise appends the item. Saves the cart, re-validates coupons, and fires `fluent_cart/cart/item_added` and `fluent_cart/cart/cart_data_items_updated` actions.

- Parameters:
  - `$item` (Array) - Cart item data
  - `$replacingIndex` (Integer\|null) - Index of existing item to replace
- Returns `FluentCart\App\Models\Cart|WP_Error` \- Cart instance or error if locked

php

```
$cart = FluentCart\App\Models\Cart::find('cart_hash_123');
$cart->addItem(['product_id' => 1, 'quantity' => 2]);
```

#### removeItem($variationId, $extraArgs = \[\], $triggerEvent = true) [​](https://dev.fluentcart.com/database/models/cart\#removeitem-variationid-extraargs-triggerevent-true)

Remove an item from the cart by variation ID. Uses `findExistingItemAndIndex()` to locate the item. If the cart is locked, returns a `WP_Error`. When `$triggerEvent` is true, re-validates coupons and fires `fluent_cart/cart/item_removed`; otherwise fires `fluent_cart/checkout/cart_amount_updated`. Always fires `fluent_cart/cart/cart_data_items_updated`.

- Parameters:
  - `$variationId` (Integer) - Variation/object ID to remove
  - `$extraArgs` (Array) - Additional matching arguments for identifying the item
  - `$triggerEvent` (Boolean) - Whether to trigger item\_removed event (default: true)
- Returns `FluentCart\App\Models\Cart|WP_Error` \- Cart instance or error if locked

php

```
$cart = FluentCart\App\Models\Cart::find('cart_hash_123');
$cart->removeItem(1, [], true);
```

#### addByVariation(ProductVariation $variation, $config = \[\]) [​](https://dev.fluentcart.com/database/models/cart\#addbyvariation-productvariation-variation-config)

Add a product variation to the cart with full business logic. Handles quantity adjustments, existing item replacement, promotional price locking, stock validation, and purchase eligibility checks via `canPurchase()`. Uses `CartHelper::generateCartItemFromVariation()` to build the cart item. If quantity is 0, removes the item instead.

- Parameters:
  - `$variation` (ProductVariation) - Product variation model instance
  - `$config`(Array) - Configuration options:
    - `quantity` (int) - Desired quantity (default: 1; 0 removes the item)
    - `by_input` (bool) - If true, sets quantity directly instead of incrementing
    - `will_validate` (bool) - If true, runs stock/purchase validation
    - `replace` (bool) - If true, removes existing item before adding
    - `remove_args` (array) - Extra args for matching when removing
    - `matched_args` (array) - Extra args for matching existing items
    - `other_info` (array) - Additional info merged into item's `other_info`
- Returns `FluentCart\App\Models\Cart|WP_Error` \- Cart instance or error

php

```
$cart = FluentCart\App\Models\Cart::find('cart_hash_123');
$variation = FluentCart\App\Models\ProductVariation::find(1);
$cart->addByVariation($variation, ['quantity' => 2, 'will_validate' => true]);
```

#### addByCustom(array $variation, array $config = \[\]) [​](https://dev.fluentcart.com/database/models/cart\#addbycustom-array-variation-array-config)

Add a custom (non-standard) item to the cart. Normalizes the item via `CartHelper::normalizeCustomFields()`, validates required fields (`id`, `object_id`, `post_id`, `post_title`, `price`, `unit_price`, `payment_type`), and rejects subscription items (which must use direct checkout). Uses `CartHelper::generateCartItemCustomItem()` to build the cart item.

- Parameters:
  - `$variation` (Array) - Custom item data with required fields
  - `$config`(Array) - Configuration options:
    - `quantity` (int) - Desired quantity (default: 1; 0 removes the item)
    - `remove_args` (array) - Extra args for matching when removing
    - `matched_args` (array) - Extra args for matching existing items
- Returns `FluentCart\App\Models\Cart|WP_Error` \- Cart instance or error

php

```
$cart = FluentCart\App\Models\Cart::find('cart_hash_123');
$cart->addByCustom([\
    'id' => 100,\
    'object_id' => 100,\
    'post_id' => 50,\
    'post_title' => 'Custom Item',\
    'price' => 1500,\
    'unit_price' => 1500,\
    'payment_type' => 'one_time',\
], ['quantity' => 1]);
```

#### findExistingItemAndIndex($objectId, $extraArgs = \[\]) [​](https://dev.fluentcart.com/database/models/cart\#findexistingitemandindex-objectid-extraargs)

Find an existing cart item and its index by `object_id`. Optionally matches additional arguments against the item using dot-notation keys.

- Parameters:
  - `$objectId` (Integer) - The object ID to search for
  - `$extraArgs` (Array) - Additional key-value pairs to match against the item
- Returns `Array|null` \- `[$index, $item]` tuple if found, or null

php

```
$cart = FluentCart\App\Models\Cart::find('cart_hash_123');
$result = $cart->findExistingItemAndIndex(100, ['other_info.color' => 'red']);
if ($result) {
    [$index, $item] = $result;
}
```

### Coupon Methods [​](https://dev.fluentcart.com/database/models/cart\#coupon-methods)

#### applyCoupon($codes = \[\]) [​](https://dev.fluentcart.com/database/models/cart\#applycoupon-codes)

Apply coupon codes to the cart. If the cart is locked, returns a `WP_Error`. Creates a `DiscountService` instance to calculate discounts, updates `cart_data`, `coupons`, and `checkout_data.__per_coupon_discounts`, then saves. Fires `fluent_cart/checkout/cart_amount_updated` and `fluent_cart/cart/cart_data_items_updated` actions.

- Parameters: `$codes` (Array) - Coupon codes to apply
- Returns `Mixed` \- Discount service result or `WP_Error` if locked/invalid

php

```
$cart = FluentCart\App\Models\Cart::find('cart_hash_123');
$result = $cart->applyCoupon(['SAVE10', 'WELCOME20']);
```

#### removeCoupon($removeCodes = \[\]) [​](https://dev.fluentcart.com/database/models/cart\#removecoupon-removecodes)

Remove specific coupon codes from the cart. Accepts a single code string or an array. Re-validates remaining coupons via `DiscountService` and updates `cart_data`, `coupons`, and `checkout_data.__per_coupon_discounts`. If the cart is locked, returns a `WP_Error`.

- Parameters: `$removeCodes` (Array\|String) - Coupon code(s) to remove
- Returns `FluentCart\App\Models\Cart|WP_Error` \- Cart instance or error if locked

php

```
$cart = FluentCart\App\Models\Cart::find('cart_hash_123');
$cart->removeCoupon(['SAVE10']);
```

#### reValidateCoupons() [​](https://dev.fluentcart.com/database/models/cart\#revalidatecoupons)

Re-validate all currently applied coupons against the current cart state. Recalculates discounts via `DiscountService`, updates `cart_data`, `coupons`, and `checkout_data.__per_coupon_discounts`. Fires `fluent_cart/checkout/cart_amount_updated` and conditionally fires `fluent_cart/cart/cart_data_items_updated` if discount totals changed.

- Returns `FluentCart\App\Models\Cart|WP_Error` \- Cart instance or error if locked

php

```
$cart = FluentCart\App\Models\Cart::find('cart_hash_123');
$cart->reValidateCoupons();
```

#### getDiscountLines($revalidate = false) [​](https://dev.fluentcart.com/database/models/cart\#getdiscountlines-revalidate-false)

Get formatted discount line items for all applied coupons. Each line includes coupon ID, code, type, discount amount, formatted price HTML, and formatted title. When only one coupon is applied, sums `coupon_discount` from each cart item. When multiple coupons are applied, reads per-coupon breakdowns from `checkout_data.__per_coupon_discounts`.

- Parameters: `$revalidate` (Boolean) - If true, re-applies coupons before calculating (default: false)
- Returns `Array` \- Associative array keyed by coupon code, each containing `id`, `code`, `type`, `discount`, `formatted_discount`, `actual_formatted_discount`, `formatted_title`

php

```
$cart = FluentCart\App\Models\Cart::find('cart_hash_123');
$discountLines = $cart->getDiscountLines();
// Example output:
// ['SAVE10' => ['id' => 1, 'code' => 'SAVE10', 'discount' => 500, ...]]
```

### Totals & Calculation Methods [​](https://dev.fluentcart.com/database/models/cart\#totals-calculation-methods)

#### getShippingTotal() [​](https://dev.fluentcart.com/database/models/cart\#getshippingtotal)

Get the shipping total for the cart. Returns 0 if the cart does not require shipping.

- Returns `Integer` \- Shipping total in cents

php

```
$cart = FluentCart\App\Models\Cart::find('cart_hash_123');
$shippingTotal = $cart->getShippingTotal();
```

#### getItemsSubtotal() [​](https://dev.fluentcart.com/database/models/cart\#getitemssubtotal)

Get the items subtotal (before discounts) by combining one-time and subscription items via `CheckoutService` and `OrderService::getItemsAmountWithoutDiscount()`.

- Returns `Integer` \- Items subtotal in cents

php

```
$cart = FluentCart\App\Models\Cart::find('cart_hash_123');
$subtotal = $cart->getItemsSubtotal();
```

#### getEstimatedTotal($extraAmount = 0) [​](https://dev.fluentcart.com/database/models/cart\#getestimatedtotal-extraamount-0)

Get the estimated cart total including item totals, shipping, and custom checkout adjustments. Combines one-time and subscription items via `CheckoutService`, calculates item totals via `OrderService::getItemsAmountTotal()`, adds shipping charges, handles custom checkout shipping amounts, and ensures the total is never negative. Applies the `fluent_cart/cart/estimated_total` filter.

- Parameters: `$extraAmount` (Integer) - Extra amount in cents to include (default: 0)
- Returns `Integer` \- Estimated total in cents (minimum 0)

php

```
$cart = FluentCart\App\Models\Cart::find('cart_hash_123');
$total = $cart->getEstimatedTotal(1000); // $10.00 extra
```

#### getEstimatedRecurringTotal() [​](https://dev.fluentcart.com/database/models/cart\#getestimatedrecurringtotal)

Get the estimated recurring total for subscription items only. Sums each subscription item's `subtotal` minus its `recurring_discounts.amount`.

- Returns `Integer` \- Estimated recurring total in cents

php

```
$cart = FluentCart\App\Models\Cart::find('cart_hash_123');
$recurringTotal = $cart->getEstimatedRecurringTotal();
```

### Address Methods [​](https://dev.fluentcart.com/database/models/cart\#address-methods)

#### getBillingAddress() [​](https://dev.fluentcart.com/database/models/cart\#getbillingaddress)

Get the billing address from checkout form data.

- Returns `Array` \- Associative array with keys: `full_name`, `company`, `address_1`, `address_2`, `city`, `state`, `postcode`, `country`

php

```
$cart = FluentCart\App\Models\Cart::find('cart_hash_123');
$billing = $cart->getBillingAddress();
// ['full_name' => 'John Doe', 'company' => '', 'address_1' => '123 Main St', ...]
```

#### getShippingAddress() [​](https://dev.fluentcart.com/database/models/cart\#getshippingaddress)

Get the shipping address. If the customer opted to ship to a different address (`isShipToDifferent()`), returns the separate shipping address fields from form data. Otherwise, falls back to `getBillingAddress()`.

- Returns `Array` \- Associative array with keys: `full_name`, `company`, `address_1`, `address_2`, `city`, `state`, `postcode`, `country`

php

```
$cart = FluentCart\App\Models\Cart::find('cart_hash_123');
$shipping = $cart->getShippingAddress();
```

### Customer Methods [​](https://dev.fluentcart.com/database/models/cart\#customer-methods)

#### guessCustomer() [​](https://dev.fluentcart.com/database/models/cart\#guesscustomer)

Attempt to find the associated customer by checking (in order): `customer_id`, `user_id`, then `email`. Returns the first matching `Customer` model found, or null if none match.

- Returns `FluentCart\App\Models\Customer|null` \- Customer instance or null

php

```
$cart = FluentCart\App\Models\Cart::find('cart_hash_123');
$customer = $cart->guessCustomer();
```

### Action Hook Helper Methods [​](https://dev.fluentcart.com/database/models/cart\#action-hook-helper-methods)

#### addDraftCreatedActions($hooks) [​](https://dev.fluentcart.com/database/models/cart\#adddraftcreatedactions-hooks)

Build a response array for actions to execute after a draft order is created. Deduplicates the hooks array.

- Parameters: `$hooks` (Array) - Hook identifiers
- Returns `Array` \- `['__after_draft_created_actions__' => [...]]`

#### addSuccessActions($hooks) [​](https://dev.fluentcart.com/database/models/cart\#addsuccessactions-hooks)

Build a response array for actions to execute on successful checkout. Deduplicates the hooks array.

- Parameters: `$hooks` (Array) - Hook identifiers
- Returns `Array` \- `['__on_success_actions__' => [...]]`

#### addCartNotices($notices) [​](https://dev.fluentcart.com/database/models/cart\#addcartnotices-notices)

Build a response array for cart notices to display. Deduplicates by notice `id`.

- Parameters: `$notices` (Array) - Array of notice arrays, each with an `id` key
- Returns `Array` \- `['__cart_notices' => [...]]`

php

```
$cart = FluentCart\App\Models\Cart::find('cart_hash_123');
$actions = $cart->addSuccessActions(['redirect_to_thank_you', 'clear_cart']);
$notices = $cart->addCartNotices([\
    ['id' => 'stock_warning', 'message' => 'Limited stock remaining']\
]);
```

## Relations [​](https://dev.fluentcart.com/database/models/cart\#relations)

This model has the following relationships that you can use.

### customer [​](https://dev.fluentcart.com/database/models/cart\#customer)

Access the associated customer (BelongsTo).

- Returns `FluentCart\App\Models\Customer`
- Foreign Key: `customer_id`

php

```
$cart = FluentCart\App\Models\Cart::find('cart_hash_123');
$customer = $cart->customer;
```

### order [​](https://dev.fluentcart.com/database/models/cart\#order)

Access the associated order (BelongsTo).

- Returns `FluentCart\App\Models\Order`
- Foreign Key: `order_id`

php

```
$cart = FluentCart\App\Models\Cart::find('cart_hash_123');
$order = $cart->order;
```

## Scopes [​](https://dev.fluentcart.com/database/models/cart\#scopes)

This model has the following scopes that you can use.

### stageNotCompleted() [​](https://dev.fluentcart.com/database/models/cart\#stagenotcompleted)

Get carts where the `stage` column is not `completed`.

php

```
$carts = FluentCart\App\Models\Cart::stageNotCompleted()->get();
```

## Usage Examples [​](https://dev.fluentcart.com/database/models/cart\#usage-examples)

### Creating a Cart [​](https://dev.fluentcart.com/database/models/cart\#creating-a-cart)

The `cart_hash` is auto-generated if not provided:

php

```
use FluentCart\App\Models\Cart;

// Auto-generated cart_hash
$cart = Cart::create([\
    'customer_id' => 1,\
    'email' => 'customer@example.com',\
]);

// Or with explicit cart_hash
$cart = Cart::create([\
    'cart_hash' => 'unique_cart_hash_123',\
    'customer_id' => 1,\
    'email' => 'customer@example.com',\
]);
```

### Retrieving Carts [​](https://dev.fluentcart.com/database/models/cart\#retrieving-carts)

php

```
// Get cart by hash (primary key)
$cart = Cart::find('cart_hash_123');

// Get carts that are not completed
$carts = Cart::stageNotCompleted()->get();

// Get cart with customer eager-loaded
$cart = Cart::with('customer')->find('cart_hash_123');
```

### Working with Cart Items [​](https://dev.fluentcart.com/database/models/cart\#working-with-cart-items)

php

```
$cart = Cart::find('cart_hash_123');

// Add by variation with validation
$variation = \FluentCart\App\Models\ProductVariation::find(1);
$cart->addByVariation($variation, [\
    'quantity' => 2,\
    'will_validate' => true,\
]);

// Remove an item
$cart->removeItem($variation->id);

// Check totals
$subtotal = $cart->getItemsSubtotal();
$total = $cart->getEstimatedTotal();
$recurringTotal = $cart->getEstimatedRecurringTotal();
```

### Working with Coupons [​](https://dev.fluentcart.com/database/models/cart\#working-with-coupons)

php

```
$cart = Cart::find('cart_hash_123');

// Apply coupons
$result = $cart->applyCoupon(['SAVE10']);

// Get discount lines for display
$discountLines = $cart->getDiscountLines();

// Remove a coupon
$cart->removeCoupon(['SAVE10']);
```

### Updating a Cart [​](https://dev.fluentcart.com/database/models/cart\#updating-a-cart)

php

```
$cart = Cart::find('cart_hash_123');
$cart->email = 'newemail@example.com';
$cart->save();
```

### Deleting a Cart [​](https://dev.fluentcart.com/database/models/cart\#deleting-a-cart)

php

```
$cart = Cart::find('cart_hash_123');
$cart->delete(); // Soft delete
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

## Coupon Model | FluentCart Developer Docs

**URL** : https://dev.fluentcart.com/database/models/coupon

[Skip to content](https://dev.fluentcart.com/database/models/coupon#VPContent)

# Coupon Model [​](https://dev.fluentcart.com/database/models/coupon\#coupon-model)

| DB Table Name | {wp\_db\_prefix}\_fct\_coupons |
| --- | --- |
| Schema | [Check Schema](https://dev.fluentcart.com/database/schema.html#fct-coupons-table) |
| Source File | fluent-cart/app/Models/Coupon.php |
| Name Space | FluentCart\\App\\Models |
| Class | FluentCart\\App\\Models\\Coupon |

## Traits [​](https://dev.fluentcart.com/database/models/coupon\#traits)

| Trait | Description |
| --- | --- |
| CanSearch | Provides `search()`, `whereLike()`, `whereBeginsWith()`, `whereEndsWith()`, and `groupSearch()` query scopes |
| HasActivity | Provides the `activities()` polymorphic relationship to the Activity model |

## Attributes [​](https://dev.fluentcart.com/database/models/coupon\#attributes)

| Attribute | Data Type | Comment |
| --- | --- | --- |
| id | Integer (BIGINT UNSIGNED) | Primary Key, auto-increment |
| parent | Integer | Parent coupon ID |
| title | String (VARCHAR 200) | Coupon title |
| code | String (VARCHAR 50) | Coupon code (unique) |
| status | String (VARCHAR 20) | Coupon status (active, inactive, expired) |
| type | String (VARCHAR 20) | Coupon type (percentage, fixed) |
| conditions | JSON | Coupon conditions (auto-encoded/decoded via mutator) |
| amount | Double | Coupon amount (in cents for fixed, raw value for percentage) |
| stackable | String (VARCHAR 3) | Whether coupon is stackable ('yes' or 'no', default 'no') |
| priority | Integer | Coupon priority |
| use\_count | Integer | Number of times used (default 0) |
| notes | Text (LONGTEXT) | Coupon notes |
| show\_on\_checkout | String (VARCHAR 3) | Show on checkout page ('yes' or 'no', default 'yes') |
| settings | JSON | Coupon settings (auto-encoded/decoded via mutator) |
| other\_info | JSON | Additional info like buy/get products (auto-encoded/decoded via mutator) |
| categories | JSON | Category IDs for coupon applicability (auto-encoded/decoded via mutator) |
| products | JSON | Product IDs for coupon applicability (auto-encoded/decoded via mutator, values cast to integer) |
| start\_date | Timestamp | Start date |
| end\_date | Timestamp | End date |
| created\_at | DateTime | Creation timestamp |
| updated\_at | DateTime | Last update timestamp |

### Fillable Attributes [​](https://dev.fluentcart.com/database/models/coupon\#fillable-attributes)

php

```
protected $fillable = [\
    'parent', 'title', 'code', 'status', 'type', 'conditions',\
    'amount', 'stackable', 'priority', 'use_count', 'notes',\
    'show_on_checkout', 'start_date', 'end_date',\
];
```

### Casts [​](https://dev.fluentcart.com/database/models/coupon\#casts)

| Attribute | Cast Type |
| --- | --- |
| max\_uses | integer |

## Usage [​](https://dev.fluentcart.com/database/models/coupon\#usage)

Please check [Model Basic](https://dev.fluentcart.com/database/models.html) for Common methods.

### Accessing Attributes [​](https://dev.fluentcart.com/database/models/coupon\#accessing-attributes)

php

```
$coupon = FluentCart\App\Models\Coupon::find(1);

$coupon->id; // returns coupon ID
$coupon->code; // returns coupon code
$coupon->type; // returns coupon type
$coupon->amount; // returns coupon amount in cents
$coupon->status; // returns coupon status
$coupon->conditions; // returns decoded conditions array (via JSON mutator)
$coupon->settings; // returns decoded settings array (via JSON mutator)
$coupon->other_info; // returns decoded other info array (via JSON mutator)
$coupon->categories; // returns decoded categories array (via JSON mutator)
$coupon->products; // returns decoded products array of integers (via JSON mutator)
```

## Relations [​](https://dev.fluentcart.com/database/models/coupon\#relations)

This model has the following relationships that you can use.

### appliedCoupons [​](https://dev.fluentcart.com/database/models/coupon\#appliedcoupons)

Access the applied coupons (hasMany).

- **Type:**`hasMany`
- **Related Model:**`FluentCart\App\Models\AppliedCoupon`
- **Foreign Key:**`coupon_id`
- **Local Key:**`id`
- Returns `FluentCart\Framework\Database\Orm\Collection` of `FluentCart\App\Models\AppliedCoupon`

php

```
$coupon = FluentCart\App\Models\Coupon::find(1);
$appliedCoupons = $coupon->appliedCoupons;
```

### orders [​](https://dev.fluentcart.com/database/models/coupon\#orders)

Access the orders that used this coupon (belongsToMany through pivot table).

- **Type:**`belongsToMany`
- **Related Model:**`FluentCart\App\Models\Order`
- **Pivot Table:**`fct_applied_coupons`
- **Foreign Pivot Key:**`coupon_id`
- **Related Pivot Key:**`order_id`
- Returns `FluentCart\Framework\Database\Orm\Collection` of `FluentCart\App\Models\Order`

php

```
$coupon = FluentCart\App\Models\Coupon::find(1);
$orders = $coupon->orders;
```

### activities [​](https://dev.fluentcart.com/database/models/coupon\#activities)

Access the activity log entries for this coupon (polymorphic, from `HasActivity` trait).

- **Type:**`morphMany`
- **Related Model:**`FluentCart\App\Models\Activity`
- **Morph Name:**`module`
- **Default Order:**`created_at DESC`, `id DESC`
- Returns `FluentCart\Framework\Database\Orm\Collection` of `FluentCart\App\Models\Activity`

php

```
$coupon = FluentCart\App\Models\Coupon::find(1);
$activities = $coupon->activities;
```

## Scopes [​](https://dev.fluentcart.com/database/models/coupon\#scopes)

This model has the following scopes that you can use.

### active() [​](https://dev.fluentcart.com/database/models/coupon\#active)

Get only active coupons that have not expired.

php

```
$coupons = FluentCart\App\Models\Coupon::active()->get();
```

This scope filters coupons that are:

- Status is `'active'`
- End date is null, or `'0000-00-00 00:00:00'`, or in the future (compared to `DateTime::gmtNow()`)

### Scopes from CanSearch Trait [​](https://dev.fluentcart.com/database/models/coupon\#scopes-from-cansearch-trait)

#### search($params) [​](https://dev.fluentcart.com/database/models/coupon\#search-params)

Search coupons using an array of filter parameters.

php

```
$coupons = FluentCart\App\Models\Coupon::search([\
    'status' => 'active',\
    'type'   => 'percentage',\
])->get();
```

#### whereLike($column, $value) [​](https://dev.fluentcart.com/database/models/coupon\#wherelike-column-value)

WHERE column LIKE %value% query.

php

```
$coupons = FluentCart\App\Models\Coupon::whereLike('code', 'SAVE')->get();
```

#### whereBeginsWith($column, $value) [​](https://dev.fluentcart.com/database/models/coupon\#wherebeginswith-column-value)

WHERE column LIKE value% query.

php

```
$coupons = FluentCart\App\Models\Coupon::whereBeginsWith('code', 'SAVE')->get();
```

#### whereEndsWith($column, $value) [​](https://dev.fluentcart.com/database/models/coupon\#whereendswith-column-value)

WHERE column LIKE %value query.

php

```
$coupons = FluentCart\App\Models\Coupon::whereEndsWith('code', '10')->get();
```

## Methods [​](https://dev.fluentcart.com/database/models/coupon\#methods)

Along with Global Model methods, this model has few helper methods.

### JSON Mutators (Accessors & Mutators) [​](https://dev.fluentcart.com/database/models/coupon\#json-mutators-accessors-mutators)

The Coupon model uses accessor/mutator pairs to automatically handle JSON encoding and decoding for several attributes. When you set these attributes with an array or object, they are automatically JSON-encoded before storage. When you read them, they are automatically JSON-decoded into arrays.

#### conditions (setConditionsAttribute / getConditionsAttribute) [​](https://dev.fluentcart.com/database/models/coupon\#conditions-setconditionsattribute-getconditionsattribute)

Set and get coupon conditions with automatic JSON encoding/decoding.

- **Setter:** Accepts an array or object, JSON-encodes it. Falls back to `'[]'` if value is empty or encoding fails.
- **Getter:** Returns a decoded array, or `[]` if value is empty.

php

```
$coupon = FluentCart\App\Models\Coupon::find(1);

// Setting conditions
$coupon->conditions = [\
    'min_purchase_amount' => 5000,\
    'max_per_customer'    => 3,\
    'max_uses'            => 100,\
    'is_recurring'        => 'yes',\
];

// Getting conditions
$conditions = $coupon->conditions; // returns array
```

#### settings (setSettingsAttribute / getSettingsAttribute) [​](https://dev.fluentcart.com/database/models/coupon\#settings-setsettingsattribute-getsettingsattribute)

Set and get coupon settings with automatic JSON encoding/decoding.

- **Setter:** If value is an array or object, JSON-encodes with `JSON_UNESCAPED_UNICODE | JSON_UNESCAPED_SLASHES` flags.
- **Getter:** If value is a string, JSON-decodes it. Returns the decoded array on success, or the original value if decoding fails.

php

```
$coupon = FluentCart\App\Models\Coupon::find(1);

// Setting
$coupon->settings = ['custom_field' => 'value'];

// Getting
$settings = $coupon->settings; // returns array
```

#### other\_info (setOtherInfoAttribute / getOtherInfoAttribute) [​](https://dev.fluentcart.com/database/models/coupon\#other-info-setotherinfoattribute-getotherinfoattribute)

Set and get additional info with automatic JSON encoding/decoding. The setter has special handling: if `buy_products` or `get_products` keys are present and are arrays, their values are cast to integers via `array_map('intval', ...)`.

- **Setter:** Accepts a string (JSON-decodes it first), array, or object. Casts `buy_products` and `get_products` values to integers. Falls back to `'[]'` for non-array/non-object values.
- **Getter:** Returns a decoded array, or `[]` if value is empty.

php

```
$coupon = FluentCart\App\Models\Coupon::find(1);

// Setting (buy_products and get_products values auto-cast to integers)
$coupon->other_info = [\
    'buy_products' => [1, 2, 3],\
    'get_products' => [4, 5],\
];

// Getting
$otherInfo = $coupon->other_info; // returns array
```

#### categories (setCategoriesAttribute / getCategoriesAttribute) [​](https://dev.fluentcart.com/database/models/coupon\#categories-setcategoriesattribute-getcategoriesattribute)

Set and get categories with automatic JSON encoding/decoding.

- **Setter:** If value is an array or object, JSON-encodes it. Falls back to `'[]'` otherwise.
- **Getter:** Returns a decoded array, or `[]` if value is empty.

php

```
$coupon = FluentCart\App\Models\Coupon::find(1);

// Setting
$coupon->categories = [1, 2, 3];

// Getting
$categories = $coupon->categories; // returns array
```

#### products (setProductsAttribute / getProductsAttribute) [​](https://dev.fluentcart.com/database/models/coupon\#products-setproductsattribute-getproductsattribute)

Set and get products with automatic JSON encoding/decoding. The setter casts each product ID to an integer via `array_map('intval', ...)`.

- **Setter:** If value is an array or object, casts each item to integer, then JSON-encodes. Falls back to `'[]'` otherwise.
- **Getter:** Returns a decoded array, or `[]` if value is empty.

php

```
$coupon = FluentCart\App\Models\Coupon::find(1);

// Setting (values are auto-cast to integers)
$coupon->products = [1, 2, 3];

// Getting
$products = $coupon->products; // returns array of integers
```

### getEndDate() [​](https://dev.fluentcart.com/database/models/coupon\#getenddate)

Get the coupon's end date.

- Returns `String|null` \- End date value

php

```
$coupon = FluentCart\App\Models\Coupon::find(1);
$endDate = $coupon->getEndDate();
```

### getStatus() [​](https://dev.fluentcart.com/database/models/coupon\#getstatus)

Get the coupon's current status.

- Returns `String` \- Status value

php

```
$coupon = FluentCart\App\Models\Coupon::find(1);
$status = $coupon->getStatus();
```

### setStatus($value) [​](https://dev.fluentcart.com/database/models/coupon\#setstatus-value)

Set the coupon's status.

- Parameters: `$value` (String) - Status value (e.g., 'active', 'inactive', 'expired')

php

```
$coupon = FluentCart\App\Models\Coupon::find(1);
$coupon->setStatus('active');
```

### getMeta($metaKey, $default = null) [​](https://dev.fluentcart.com/database/models/coupon\#getmeta-metakey-default-null)

Get a coupon meta value from the `fct_meta` table where `object_type` is `'coupon'`.

- Parameters: `$metaKey` (String) - Meta key, `$default` (Mixed) - Default value if meta not found
- Returns `Mixed` \- Meta value or default

php

```
$coupon = FluentCart\App\Models\Coupon::find(1);
$metaValue = $coupon->getMeta('custom_field', 'default');
```

### updateMeta($metaKey, $metaValue) [​](https://dev.fluentcart.com/database/models/coupon\#updatemeta-metakey-metavalue)

Create or update a coupon meta value in the `fct_meta` table where `object_type` is `'coupon'`. If the meta key already exists for this coupon, it updates the value. Otherwise, it creates a new meta record.

- Parameters: `$metaKey` (String) - Meta key, `$metaValue` (Mixed) - Meta value
- Returns `FluentCart\App\Models\Meta` \- The created or updated Meta instance

php

```
$coupon = FluentCart\App\Models\Coupon::find(1);
$meta = $coupon->updateMeta('custom_field', 'new_value');
```

### isRecurringDiscount() [​](https://dev.fluentcart.com/database/models/coupon\#isrecurringdiscount)

Check if this coupon is configured as a recurring discount. Looks at the `is_recurring` key inside the `conditions` JSON attribute.

- Returns `Boolean` \- `true` if `conditions.is_recurring` equals `'yes'`, `false` otherwise

php

```
$coupon = FluentCart\App\Models\Coupon::find(1);

if ($coupon->isRecurringDiscount()) {
    // This coupon applies to recurring subscription payments
}
```

## Usage Examples [​](https://dev.fluentcart.com/database/models/coupon\#usage-examples)

### Creating a Coupon [​](https://dev.fluentcart.com/database/models/coupon\#creating-a-coupon)

php

```
use FluentCart\App\Models\Coupon;

$coupon = Coupon::create([\
    'code'       => 'SAVE10',\
    'title'      => 'Save 10%',\
    'type'       => 'percentage',\
    'amount'     => 10, // 10%\
    'status'     => 'active',\
    'stackable'  => 'no',\
    'conditions' => [\
        'min_purchase_amount' => 5000,\
        'max_uses'            => 100,\
        'max_per_customer'    => 3,\
        'is_recurring'        => 'yes',\
    ],\
    'start_date' => now(),\
    'end_date'   => now()->addDays(30),\
]);
```

### Retrieving Coupons [​](https://dev.fluentcart.com/database/models/coupon\#retrieving-coupons)

php

```
// Get coupon by code
$coupon = Coupon::where('code', 'SAVE10')->first();

// Get all active coupons
$coupons = Coupon::active()->get();

// Get coupon by ID
$coupon = Coupon::find(1);

// Search coupons by code pattern
$coupons = Coupon::whereLike('code', 'SAVE')->get();

// Get coupon with activities
$coupon = Coupon::with(['activities.user'])->find(1);

// Get coupon with applied coupons count
$coupon = Coupon::withCount('appliedCoupons')->find(1);
```

### Updating a Coupon [​](https://dev.fluentcart.com/database/models/coupon\#updating-a-coupon)

php

```
$coupon = Coupon::find(1);
$coupon->use_count = $coupon->use_count + 1;
$coupon->save();
```

### Checking Recurring Discount [​](https://dev.fluentcart.com/database/models/coupon\#checking-recurring-discount)

php

```
$coupon = Coupon::find(1);
if ($coupon->isRecurringDiscount()) {
    // Handle recurring discount logic
}
```

### Working with Meta [​](https://dev.fluentcart.com/database/models/coupon\#working-with-meta)

php

```
$coupon = Coupon::find(1);

// Set meta
$coupon->updateMeta('custom_setting', 'value');

// Get meta with default
$value = $coupon->getMeta('custom_setting', 'fallback');
```

### Deleting a Coupon [​](https://dev.fluentcart.com/database/models/coupon\#deleting-a-coupon)

php

```
$coupon = Coupon::find(1);
$coupon->delete();
```

* * *

Today

Hi! I’m your AI assistant. How can I assist you today?

Just now

Powered by **FluentBot**


---

---

## Customer Model | FluentCart Developer Docs

**URL** : https://dev.fluentcart.com/database/models/customer

[Skip to content](https://dev.fluentcart.com/database/models/customer#VPContent)

# Customer Model [​](https://dev.fluentcart.com/database/models/customer\#customer-model)

| DB Table Name | {wp\_db\_prefix}\_fct\_customers |
| --- | --- |
| Schema | [Check Schema](https://dev.fluentcart.com/database/schema.html#fct-customers-table) |
| Source File | fluent-cart/app/Models/Customer.php |
| Name Space | FluentCart\\App\\Models |
| Class | FluentCart\\App\\Models\\Customer |

## Traits [​](https://dev.fluentcart.com/database/models/customer\#traits)

| Trait | Description |
| --- | --- |
| CanSearch | Provides `search()`, `whereLike()`, `whereBeginsWith()`, `whereEndsWith()`, `groupSearch()` scopes for flexible query filtering |
| CanUpdateBatch | Provides `batchUpdate()` scope for batch updating multiple records |

## Attributes [​](https://dev.fluentcart.com/database/models/customer\#attributes)

| Attribute | Data Type | Comment |
| --- | --- | --- |
| id | Integer (BIGINT UNSIGNED) | Primary Key, Auto Increment |
| user\_id | Integer (BIGINT UNSIGNED) | WordPress user ID (nullable) |
| contact\_id | Integer (BIGINT UNSIGNED) | Contact ID (default 0) |
| email | String (VARCHAR 192) | Customer email address |
| first\_name | String (VARCHAR 192) | Customer first name |
| last\_name | String (VARCHAR 192) | Customer last name |
| status | String (VARCHAR 45) | Customer status (default: 'active') |
| purchase\_value | JSON | Purchase value data (stored/retrieved as JSON) |
| purchase\_count | Integer (BIGINT UNSIGNED) | Number of purchases (default 0) |
| ltv | Integer (BIGINT) | Lifetime value in cents (default 0) |
| first\_purchase\_date | Date Time | First purchase date (nullable) |
| last\_purchase\_date | Date Time | Last purchase date (nullable) |
| aov | Decimal (18,2) | Average order value (nullable) |
| notes | Text (LONGTEXT) | Customer notes |
| uuid | String (VARCHAR 100) | Unique identifier (auto-generated on creation) |
| country | String (VARCHAR 45) | Customer country code (nullable) |
| city | String (VARCHAR 45) | Customer city (nullable) |
| state | String (VARCHAR 45) | Customer state (nullable) |
| postcode | String (VARCHAR 45) | Customer postcode (nullable) |
| created\_at | Date Time | Creation timestamp |
| updated\_at | Date Time | Last update timestamp |

### Appended Attributes [​](https://dev.fluentcart.com/database/models/customer\#appended-attributes)

These virtual attributes are appended to every serialized Customer instance via the `$appends` property:

| Attribute | Accessor Method | Return Type | Description |
| --- | --- | --- | --- |
| full\_name | `getFullNameAttribute()` | String | Concatenation of first\_name and last\_name |
| photo | `getPhotoAttribute()` | String | Custom photo URL from user meta, or Gravatar fallback |
| country\_name | `getCountryNameAttribute()` | String | Human-readable country name from country code |
| formatted\_address | `getFormattedAddressAttribute()` | Array | Formatted address data array |
| user\_link | `getUserLinkAttribute()` | String | WordPress admin user-edit URL (empty if no user\_id) |

### Searchable Fields [​](https://dev.fluentcart.com/database/models/customer\#searchable-fields)

The `$searchable` property defines which fields are used by the `searchBy` scope:

- `first_name`
- `last_name`
- `email`

### Mutators [​](https://dev.fluentcart.com/database/models/customer\#mutators)

| Mutator | Direction | Description |
| --- | --- | --- |
| `setPurchaseValueAttribute` | Set | Accepts array/object (JSON-encodes) or scalar value |
| `getPurchaseValueAttribute` | Get | Returns decoded JSON as array, or null if empty |

### Boot Behavior [​](https://dev.fluentcart.com/database/models/customer\#boot-behavior)

On `creating`, the model auto-generates the `uuid` attribute using `md5($model->email . '_' . wp_generate_uuid4())`.

## Usage [​](https://dev.fluentcart.com/database/models/customer\#usage)

Please check [Model Basic](https://dev.fluentcart.com/database/models.html) for Common methods.

### Accessing Attributes [​](https://dev.fluentcart.com/database/models/customer\#accessing-attributes)

php

```
$customer = FluentCart\App\Models\Customer::find(1);

$customer->id; // returns customer ID
$customer->email; // returns email address
$customer->first_name; // returns first name
$customer->last_name; // returns last name
$customer->status; // returns customer status
$customer->full_name; // returns "John Doe" (appended)
$customer->photo; // returns photo URL (appended)
$customer->country_name; // returns country name (appended)
$customer->formatted_address; // returns address array (appended)
$customer->user_link; // returns WP user edit URL (appended)
```

## Methods [​](https://dev.fluentcart.com/database/models/customer\#methods)

Along with Global Model methods, this model has few helper methods.

### getFullNameAttribute() [​](https://dev.fluentcart.com/database/models/customer\#getfullnameattribute)

Get customer full name by concatenating first\_name and last\_name.

- Returns `String` \- Full name (first\_name + last\_name), trimmed

php

```
$customer = FluentCart\App\Models\Customer::find(1);
$fullName = $customer->full_name; // returns "John Doe"
```

### getPhotoAttribute() [​](https://dev.fluentcart.com/database/models/customer\#getphotoattribute)

Get customer photo URL. First checks for a custom photo URL stored in user meta (`fc_customer_photo_url`). Falls back to Gravatar (100x100) if no custom photo is set.

- Returns `String` \- Photo URL (custom or Gravatar)

php

```
$customer = FluentCart\App\Models\Customer::find(1);
$photo = $customer->photo; // returns photo URL
```

### getCountryNameAttribute() [​](https://dev.fluentcart.com/database/models/customer\#getcountrynameattribute)

Get country name from country code using `Helper::getCountryName()`.

- Returns `String` \- Country name

php

```
$customer = FluentCart\App\Models\Customer::find(1);
$countryName = $customer->country_name; // returns country name
```

### getFormattedAddressAttribute() [​](https://dev.fluentcart.com/database/models/customer\#getformattedaddressattribute)

Get formatted address as an associative array with resolved country and state names.

- Returns `Array` \- Formatted address data with keys: `country`, `state`, `city`, `postcode`, `first_name`, `last_name`, `full_name`

php

```
$customer = FluentCart\App\Models\Customer::find(1);
$address = $customer->formatted_address;
// [\
//     'country'    => 'United States',\
//     'state'      => 'California',\
//     'city'       => 'San Francisco',\
//     'postcode'   => '94102',\
//     'first_name' => 'John',\
//     'last_name'  => 'Doe',\
//     'full_name'  => 'John Doe'\
// ]
```

### getUserLinkAttribute() [​](https://dev.fluentcart.com/database/models/customer\#getuserlinkattribute)

Get WordPress user edit link. Returns empty string if the customer has no associated `user_id`.

- Returns `String` \- User edit URL (e.g., `/wp-admin/user-edit.php?user_id=5`) or empty string

php

```
$customer = FluentCart\App\Models\Customer::find(1);
$userLink = $customer->user_link; // returns user edit URL
```

### recountStats() [​](https://dev.fluentcart.com/database/models/customer\#recountstats)

Recount customer order statistics. Sets `total_order_count` (count of all orders) and `total_order_value` (sum of `total_amount` across all orders) and saves the model.

- Returns `FluentCart\App\Models\Customer` \- Updated customer instance

php

```
$customer = FluentCart\App\Models\Customer::find(1);
$customer->recountStats();
```

### recountStat() [​](https://dev.fluentcart.com/database/models/customer\#recountstat)

Recount detailed customer purchase statistics from successful payment orders only. Updates `purchase_count`, `first_purchase_date`, `last_purchase_date`, `ltv` (lifetime value as net paid minus refunds), and `aov` (average order value = ltv / purchase\_count). Saves the model.

- Returns `FluentCart\App\Models\Customer` \- Updated customer instance

php

```
$customer = FluentCart\App\Models\Customer::find(1);
$customer->recountStat();
```

### updateCustomerStatus($newStatus) [​](https://dev.fluentcart.com/database/models/customer\#updatecustomerstatus-newstatus)

Update customer status and fire action hooks. If the new status is the same as the current status, returns early without saving or firing hooks.

Fires the following WordPress action hooks:

- `fluent_cart/customer_status_to_{$newStatus}` \- Status-specific hook
- `fluent_cart/customer_status_updated` \- General status change hook

Both hooks receive an array with keys: `customer`, `old_status`, `new_status`.

- Parameters: `$newStatus` (String) - New status value
- Returns `FluentCart\App\Models\Customer` \- Updated customer instance

php

```
$customer = FluentCart\App\Models\Customer::find(1);
$customer->updateCustomerStatus('active');
```

### getWpUserId($recheck = false) [​](https://dev.fluentcart.com/database/models/customer\#getwpuserid-recheck-false)

Get WordPress user ID. When `$recheck` is true, looks up the WordPress user by the customer's email and updates the stored `user_id` if it has changed.

- Parameters: `$recheck` (Boolean) - Whether to recheck by looking up the WP user by email (default: false)
- Returns `Integer|null` \- WordPress user ID

php

```
$customer = FluentCart\App\Models\Customer::find(1);
$wpUserId = $customer->getWpUserId();
$wpUserId = $customer->getWpUserId(true); // recheck and sync user_id
```

### getWpUser() [​](https://dev.fluentcart.com/database/models/customer\#getwpuser)

Get WordPress user object. First tries to find by `user_id`, then falls back to email lookup. If found by email and the `user_id` differs, updates the stored `user_id` and saves.

- Returns `WP_User|false` \- WordPress user object or false if not found

php

```
$customer = FluentCart\App\Models\Customer::find(1);
$wpUser = $customer->getWpUser();
```

### getMeta($metaKey, $default = null) [​](https://dev.fluentcart.com/database/models/customer\#getmeta-metakey-default-null)

Get customer meta value from the `fct_customer_meta` table.

- Parameters: `$metaKey` (String) - Meta key, `$default` (Mixed) - Default value if not found (default: null)
- Returns `Mixed` \- Meta value or default

php

```
$customer = FluentCart\App\Models\Customer::find(1);
$metaValue = $customer->getMeta('custom_field', 'default');
```

### updateMeta($metaKey, $metaValue) [​](https://dev.fluentcart.com/database/models/customer\#updatemeta-metakey-metavalue)

Create or update customer meta value in the `fct_customer_meta` table.

- Parameters: `$metaKey` (String) - Meta key, `$metaValue` (Mixed) - Meta value
- Returns `FluentCart\App\Models\CustomerMeta` \- Meta instance (created or updated)

php

```
$customer = FluentCart\App\Models\Customer::find(1);
$meta = $customer->updateMeta('custom_field', 'new_value');
```

## Relations [​](https://dev.fluentcart.com/database/models/customer\#relations)

This model has the following relationships that you can use

### orders [​](https://dev.fluentcart.com/database/models/customer\#orders)

Access the customer orders.

- Relation type: `HasMany`
- Returns collection of `FluentCart\App\Models\Order`
- Foreign key: `customer_id`

php

```
$customer = FluentCart\App\Models\Customer::find(1);
$orders = $customer->orders;
```

### success\_order\_items [​](https://dev.fluentcart.com/database/models/customer\#success-order-items)

Access the successful order items (items from orders with successful payment statuses).

- Relation type: `HasManyThrough` (through `FluentCart\App\Models\Order`)
- Returns collection of `FluentCart\App\Models\OrderItem`
- Filters orders by successful payment statuses via `Status::getOrderPaymentSuccessStatuses()`

php

```
$customer = FluentCart\App\Models\Customer::find(1);
$orderItems = $customer->success_order_items;
```

### subscriptions [​](https://dev.fluentcart.com/database/models/customer\#subscriptions)

Access the customer subscriptions.

- Relation type: `HasMany`
- Returns collection of `FluentCart\App\Models\Subscription`
- Foreign key: `customer_id`

php

```
$customer = FluentCart\App\Models\Customer::find(1);
$subscriptions = $customer->subscriptions;
```

### shipping\_address [​](https://dev.fluentcart.com/database/models/customer\#shipping-address)

Access the shipping addresses (filtered by type = 'shipping').

- Relation type: `HasMany`
- Returns collection of `FluentCart\App\Models\CustomerAddresses`
- Foreign key: `customer_id`

php

```
$customer = FluentCart\App\Models\Customer::find(1);
$addresses = $customer->shipping_address;
```

### billing\_address [​](https://dev.fluentcart.com/database/models/customer\#billing-address)

Access the billing addresses (filtered by type = 'billing').

- Relation type: `HasMany`
- Returns collection of `FluentCart\App\Models\CustomerAddresses`
- Foreign key: `customer_id`

php

```
$customer = FluentCart\App\Models\Customer::find(1);
$addresses = $customer->billing_address;
```

### primary\_shipping\_address [​](https://dev.fluentcart.com/database/models/customer\#primary-shipping-address)

Access the primary shipping address (filtered by type = 'shipping' and is\_primary = 1).

- Relation type: `HasOne`
- Returns `FluentCart\App\Models\CustomerAddresses|null`

php

```
$customer = FluentCart\App\Models\Customer::find(1);
$address = $customer->primary_shipping_address;
```

### primary\_billing\_address [​](https://dev.fluentcart.com/database/models/customer\#primary-billing-address)

Access the primary billing address (filtered by type = 'billing' and is\_primary = 1).

- Relation type: `HasOne`
- Returns `FluentCart\App\Models\CustomerAddresses|null`

php

```
$customer = FluentCart\App\Models\Customer::find(1);
$address = $customer->primary_billing_address;
```

### labels [​](https://dev.fluentcart.com/database/models/customer\#labels)

Access the customer labels (polymorphic relationship).

- Relation type: `MorphMany`
- Returns collection of `FluentCart\App\Models\LabelRelationship`

php

```
$customer = FluentCart\App\Models\Customer::find(1);
$labels = $customer->labels;
```

### wpUser [​](https://dev.fluentcart.com/database/models/customer\#wpuser)

Access the associated WordPress user.

- Relation type: `BelongsTo`
- Returns `FluentCart\App\Models\User|null`
- Foreign key: `user_id`

php

```
$customer = FluentCart\App\Models\Customer::find(1);
$user = $customer->wpUser;
```

## Scopes [​](https://dev.fluentcart.com/database/models/customer\#scopes)

This model has the following scopes that you can use

### ofActive() [​](https://dev.fluentcart.com/database/models/customer\#ofactive)

Get only active customers (where status = 'active').

php

```
$customers = FluentCart\App\Models\Customer::ofActive()->get();
```

### ofArchived() [​](https://dev.fluentcart.com/database/models/customer\#ofarchived)

Get only archived customers (where status = 'archived').

php

```
$customers = FluentCart\App\Models\Customer::ofArchived()->get();
```

### searchBy($search) [​](https://dev.fluentcart.com/database/models/customer\#searchby-search)

Search customers by query string. Supports multiple search modes:

- **Operator-based search**: `column_name > value`, `column_name = value`, etc. (supports `=`, `!=`, `>`, `<`)
- **Column-specific LIKE search**: `column_name:value` (searches with LIKE %value%)
- **Column-specific exact search**: `column_name=value`
- **General search**: Searches across `$searchable` fields (`first_name`, `last_name`, `email`) with LIKE matching. Also handles multi-word queries by splitting into first\_name/last\_name search.

- Parameters: `$search` (String) - Search query

php

```
// General search across searchable fields
$customers = FluentCart\App\Models\Customer::searchBy('john')->get();

// Operator-based search
$customers = FluentCart\App\Models\Customer::searchBy('purchase_count > 5')->get();

// Column-specific LIKE search
$customers = FluentCart\App\Models\Customer::searchBy('email:example.com')->get();

// Full name search (splits "John Doe" into first_name + last_name)
$customers = FluentCart\App\Models\Customer::searchBy('John Doe')->get();
```

### applyCustomFilters($filters) [​](https://dev.fluentcart.com/database/models/customer\#applycustomfilters-filters)

Apply custom filters using an associative array. Each filter key must be a fillable attribute. Supports operators: `includes` (LIKE), `not_includes` (NOT LIKE), `gt` (>), `lt` (<), and standard SQL operators.

- Parameters: `$filters` (Array) - Associative array of filter key => `['value' => ..., 'operator' => ...]`

php

```
$customers = FluentCart\App\Models\Customer::applyCustomFilters([\
    'status' => ['value' => 'active', 'operator' => '='],\
    'email'  => ['value' => 'example.com', 'operator' => 'includes'],\
    'ltv'    => ['value' => '1000', 'operator' => 'gt']\
])->get();
```

### searchByFullName($data) [​](https://dev.fluentcart.com/database/models/customer\#searchbyfullname-data)

Search by concatenated full name (CONCAT(first\_name, ' ', last\_name)). Supports multiple matching operators.

- Parameters: `$data` (Array) - Search data with keys:
  - `value` (String) - The search term
  - `operator` (String) - One of `starts_with`, `ends_with`, `not_like`, or default (contains/like\_all)

php

```
$customers = FluentCart\App\Models\Customer::searchByFullName([\
    'value' => 'John',\
    'operator' => 'starts_with'\
])->get();

$customers = FluentCart\App\Models\Customer::searchByFullName([\
    'value' => 'Doe',\
    'operator' => 'ends_with'\
])->get();

$customers = FluentCart\App\Models\Customer::searchByFullName([\
    'value' => 'Test User',\
    'operator' => 'not_like'\
])->get();
```

### Inherited Scopes from CanSearch Trait [​](https://dev.fluentcart.com/database/models/customer\#inherited-scopes-from-cansearch-trait)

These scopes are available via the `CanSearch` trait:

#### search($params) [​](https://dev.fluentcart.com/database/models/customer\#search-params)

Flexible search with multiple operators per column.

php

```
$customers = FluentCart\App\Models\Customer::search([\
    'email' => ['column' => 'email', 'operator' => 'like_all', 'value' => 'example.com'],\
    'status' => ['column' => 'status', 'operator' => '=', 'value' => 'active']\
])->get();
```

#### whereLike($column, $value) [​](https://dev.fluentcart.com/database/models/customer\#wherelike-column-value)

WHERE column LIKE %value% query.

php

```
$customers = FluentCart\App\Models\Customer::whereLike('email', 'example.com')->get();
```

#### whereBeginsWith($column, $value) [​](https://dev.fluentcart.com/database/models/customer\#wherebeginswith-column-value)

WHERE column LIKE value% query.

php

```
$customers = FluentCart\App\Models\Customer::whereBeginsWith('first_name', 'Jo')->get();
```

#### whereEndsWith($column, $value) [​](https://dev.fluentcart.com/database/models/customer\#whereendswith-column-value)

WHERE column LIKE %value query.

php

```
$customers = FluentCart\App\Models\Customer::whereEndsWith('email', '.com')->get();
```

#### groupSearch($groups) [​](https://dev.fluentcart.com/database/models/customer\#groupsearch-groups)

Search across related models using dot notation.

php

```
$customers = FluentCart\App\Models\Customer::groupSearch([\
    'fct_customers.email' => ['column' => 'email', 'operator' => 'like_all', 'value' => 'test'],\
])->get();
```

### Inherited Scope from CanUpdateBatch Trait [​](https://dev.fluentcart.com/database/models/customer\#inherited-scope-from-canupdatebatch-trait)

#### batchUpdate($values, $index = null) [​](https://dev.fluentcart.com/database/models/customer\#batchupdate-values-index-null)

Batch update multiple records at once.

php

```
FluentCart\App\Models\Customer::batchUpdate([\
    ['id' => 1, 'status' => 'active'],\
    ['id' => 2, 'status' => 'archived'],\
]);
```

## Usage Examples [​](https://dev.fluentcart.com/database/models/customer\#usage-examples)

### Creating a Customer [​](https://dev.fluentcart.com/database/models/customer\#creating-a-customer)

php

```
use FluentCart\App\Models\Customer;

// uuid is auto-generated on creation
$customer = Customer::create([\
    'email' => 'customer@example.com',\
    'first_name' => 'John',\
    'last_name' => 'Doe',\
    'status' => 'active'\
]);
```

### Retrieving Customers [​](https://dev.fluentcart.com/database/models/customer\#retrieving-customers)

php

```
// Get all active customers
$customers = Customer::ofActive()->get();

// Get customer by email
$customer = Customer::where('email', 'customer@example.com')->first();

// Get customer with orders
$customer = Customer::with('orders')->find(1);

// Search customers
$customers = Customer::searchBy('john doe')->get();

// Get customers with custom filters
$customers = Customer::applyCustomFilters([\
    'country' => ['value' => 'US', 'operator' => '=']\
])->get();
```

### Updating a Customer [​](https://dev.fluentcart.com/database/models/customer\#updating-a-customer)

php

```
$customer = Customer::find(1);
$customer->first_name = 'Jane';
$customer->save();

// Update status with hooks
$customer->updateCustomerStatus('archived');

// Recount purchase statistics
$customer->recountStat();
```

### Working with Meta [​](https://dev.fluentcart.com/database/models/customer\#working-with-meta)

php

```
$customer = Customer::find(1);

// Get meta
$value = $customer->getMeta('preferred_language', 'en');

// Set/update meta
$customer->updateMeta('preferred_language', 'fr');
```

### Deleting a Customer [​](https://dev.fluentcart.com/database/models/customer\#deleting-a-customer)

php

```
$customer = Customer::find(1);
$customer->delete();
```

* * *

Today

Hi! I’m your AI assistant. How can I assist you today?

Just now

Powered by **FluentBot**


---

---

