# FluentCart Developer Docs - Modules

Modules internes FluentCart : fee system, ghost product selling, licensing, payment methods.

---

## Fee System (Surcharges & Additional Charges) | FluentCart Developer Docs

**URL** : https://dev.fluentcart.com/modules/fee-system

[Skip to content](https://dev.fluentcart.com/modules/fee-system#VPContent)

# Fee System (Surcharges & Additional Charges) [​](https://dev.fluentcart.com/modules/fee-system\#fee-system-surcharges-additional-charges)

FluentCart provides a built-in fee system that allows developers to attach additional charges to a cart during checkout. This is useful for processing fees, handling fees, small-order surcharges, payment gateway surcharges, environmental levies, and more.

## Overview [​](https://dev.fluentcart.com/modules/fee-system\#overview)

Fees are stored as order items with `payment_type = 'fee'` and a cached `fee_total` column on the order for fast aggregation. The system provides two ways to register fees:

- **Dynamic fees** via the `fluent_cart/cart/fees` filter - recalculated on every checkout update
- **Persistent fees** via `$cart->addFee()` - stored directly on the cart and persisted to the database

Fees automatically integrate with:

- Checkout summary display
- Order totals calculation
- Email templates and PDF receipts
- Admin order view and customer portal
- Refund distribution (proportional)
- REST API responses

## Fee Data Structure [​](https://dev.fluentcart.com/modules/fee-system\#fee-data-structure)

Every fee follows this structure:

php

```
[\
    'key'     => 'processing_fee',        // Unique slug (required)\
    'label'   => 'Processing Fee',         // Customer-facing name (required)\
    'amount'  => 450,                      // Amount in cents, must be positive (required)\
    'taxable' => false,                    // Whether tax should be calculated (default: false)\
    'source'  => 'my-addon',              // Addon identifier (default: 'custom')\
    'meta'    => ['rule_id' => 42],        // Optional extra data stored in order item\
]
```

**Rules:**

- `amount` must be a positive integer (in cents). Negative values are rejected.
- `key` is sanitized with `sanitize_key()`. Combined with `source`, it forms a composite dedup key (`source:key`).
- Duplicate `source:key` entries are deduplicated - the last one wins.

* * *

## Method 1: Dynamic Fees via Filter [​](https://dev.fluentcart.com/modules/fee-system\#method-1-dynamic-fees-via-filter)

Use the `fluent_cart/cart/fees` filter to add fees that are recalculated on every checkout update (quantity change, coupon applied, payment method changed, etc.).

### Hook: `fluent_cart/cart/fees` [​](https://dev.fluentcart.com/modules/fee-system\#hook-fluent-cart-cart-fees)

**Parameters:**

- `$fees` (array): Current fees array (may contain fees from other addons or stored fees)
- `$context` (array): Cart context for condition evaluation

**Returns:** Modified fees array

**Context array contents:**

| Key | Type | Description |
| --- | --- | --- |
| `cart` | `Cart` | The Cart model instance |
| `cart_items` | `array` | Current cart item data |
| `cart_subtotal` | `int` | Cart subtotal in cents (before discounts) |
| `shipping_total` | `int` | Shipping total in cents |
| `customer_id` | `int` | Customer ID |
| `payment_method` | `string` | Selected payment method key |
| `checkout_data` | `array` | Full checkout data |

### Example: Small Order Surcharge [​](https://dev.fluentcart.com/modules/fee-system\#example-small-order-surcharge)

Add a $5 fee when the cart subtotal is under $25:

php

```
add_filter('fluent_cart/cart/fees', function (array $fees, array $context) {
    $subtotal = $context['cart_subtotal'];

    if ($subtotal > 0 && $subtotal < 2500) {
        $fees[] = [\
            'key'     => 'small_order_fee',\
            'label'   => __('Small Order Fee', 'my-addon'),\
            'amount'  => 500,\
            'taxable' => false,\
            'source'  => 'my-addon',\
            'meta'    => ['reason' => 'subtotal_below_threshold'],\
        ];
    }

    return $fees;
}, 10, 2);
```

### Example: Payment Method Processing Fee [​](https://dev.fluentcart.com/modules/fee-system\#example-payment-method-processing-fee)

Add a 2.9% processing fee for Stripe payments:

php

```
add_filter('fluent_cart/cart/fees', function (array $fees, array $context) {
    if ($context['payment_method'] !== 'stripe') {
        return $fees;
    }

    $subtotal = $context['cart_subtotal'];
    if ($subtotal <= 0) {
        return $fees;
    }

    $feeAmount = (int) round($subtotal * 0.029);

    $fees[] = [\
        'key'     => 'stripe_processing',\
        'label'   => __('Processing Fee (2.9%)', 'my-addon'),\
        'amount'  => $feeAmount,\
        'taxable' => true,\
        'source'  => 'my-addon',\
        'meta'    => ['rate' => '2.9%'],\
    ];

    return $fees;
}, 10, 2);
```

### Example: Location-Based Fee [​](https://dev.fluentcart.com/modules/fee-system\#example-location-based-fee)

Add a handling fee for orders shipping to remote areas:

php

```
add_filter('fluent_cart/cart/fees', function (array $fees, array $context) {
    $checkoutData = $context['checkout_data'];
    $country = $checkoutData['form_data']['shipping_country'] ?? '';
    $state = $checkoutData['form_data']['shipping_state'] ?? '';

    $remoteAreas = ['AK', 'HI', 'PR']; // Alaska, Hawaii, Puerto Rico

    if ($country === 'US' && in_array($state, $remoteAreas, true)) {
        $fees[] = [\
            'key'     => 'remote_handling',\
            'label'   => __('Remote Area Handling Fee', 'my-addon'),\
            'amount'  => 1500,\
            'taxable' => false,\
            'source'  => 'my-addon',\
        ];
    }

    return $fees;
}, 10, 2);
```

* * *

## Method 2: Persistent Fees via Cart Methods [​](https://dev.fluentcart.com/modules/fee-system\#method-2-persistent-fees-via-cart-methods)

Use these methods to programmatically add or remove fees that are stored on the cart. Persistent fees survive page reloads and are included alongside dynamic fees.

### `$cart->addFee(array $fee): bool` [​](https://dev.fluentcart.com/modules/fee-system\#cart-addfee-array-fee-bool)

Adds a fee to the cart and saves immediately. If a fee with the same `source:key` already exists, it will be updated.

php

```
$cart = \FluentCart\App\Models\Cart::find($cartId);

$cart->addFee([\
    'key'     => 'handling_fee',\
    'label'   => 'Handling Fee',\
    'amount'  => 200,\
    'source'  => 'my-addon',\
    'taxable' => false,\
    'meta'    => ['applied_by' => 'admin'],\
]);
```

### `$cart->removeFee(string $key, ?string $source = null): bool` [​](https://dev.fluentcart.com/modules/fee-system\#cart-removefee-string-key-string-source-null-bool)

Removes a fee by key. Optionally filter by source to avoid removing another addon's fee with the same key.

php

```
// Remove a specific fee by key and source
$cart->removeFee('handling_fee', 'my-addon');

// Remove all fees with this key (regardless of source)
$cart->removeFee('handling_fee');
```

### `$cart->removeFeesBySource(string $source): void` [​](https://dev.fluentcart.com/modules/fee-system\#cart-removefeesbysource-string-source-void)

Removes all fees from a specific source. Useful for clearing all your addon's fees before recalculating.

php

```
// Clear all fees from your addon
$cart->removeFeesBySource('my-addon');
```

### `$cart->getFees(): array` [​](https://dev.fluentcart.com/modules/fee-system\#cart-getfees-array)

Returns all validated fees (stored + dynamic from filter).

### `$cart->getFeeTotal(): int` [​](https://dev.fluentcart.com/modules/fee-system\#cart-getfeetotal-int)

Returns the total of all fees in cents.

php

```
$fees = $cart->getFees();
$total = $cart->getFeeTotal(); // e.g., 700 (= $7.00)
```

* * *

## How Fees Flow Through the System [​](https://dev.fluentcart.com/modules/fee-system\#how-fees-flow-through-the-system)

```
1. REGISTRATION
   Addon registers fees via filter or $cart->addFee()

2. CHECKOUT SUMMARY
   WebCheckoutHandler recalculates on every cart change
   CartSummaryRender::renderFees() displays fee lines
   Fee total included in estimated total

3. ORDER CREATION
   CheckoutProcessor reads fees from cart
   Each fee becomes an OrderItem (payment_type = 'fee')
   fee_total cached on the Order record
   total_amount formula includes fee_total

4. POST-ORDER
   Admin view: fee rows in payment table
   Customer portal: fee rows in totals
   Emails: fee rows in items table
   PDF receipts: fee rows in summary
   Refunds: fees participate in proportional distribution
```

### Total Amount Formula [​](https://dev.fluentcart.com/modules/fee-system\#total-amount-formula)

```
total_amount = subtotal
             - coupon_discount_total
             - manual_discount_total
             + fee_total
             + shipping_total
             + tax_total (if exclusive)
             + shipping_tax (if exclusive)
```

* * *

## Fee Display Order [​](https://dev.fluentcart.com/modules/fee-system\#fee-display-order)

Fees appear in the checkout summary and all post-order displays in this order:

```
1. Subtotal
2. Shipping
3. Fees          ← your fees appear here
4. Coupons / Discounts
5. Tax
6. Total
```

This ordering is intentional - fees are additions (like shipping), shown before subtractions (discounts).

* * *

## Reading Fees from Orders [​](https://dev.fluentcart.com/modules/fee-system\#reading-fees-from-orders)

After an order is placed, fees are stored as order items. Use these methods to access them:

### `$order->feeItems()` [​](https://dev.fluentcart.com/modules/fee-system\#order-feeitems)

Returns a HasMany relationship query for fee order items.

php

```
$order = \FluentCart\App\Models\Order::find($orderId);

$feeItems = $order->feeItems()->get();

foreach ($feeItems as $item) {
    echo $item->title;      // "Processing Fee"
    echo $item->subtotal;   // 450 (cents)
    echo $item->tax_amount; // 36 (cents, if taxable)
}
```

### `$order->getAppliedFees()` [​](https://dev.fluentcart.com/modules/fee-system\#order-getappliedfees)

Returns a simplified array of applied fees.

php

```
$fees = $order->getAppliedFees();
// [\
//     [\
//         'key'     => 'processing_fee',\
//         'label'   => 'Processing Fee',\
//         'amount'  => 450,\
//         'source'  => 'my-addon',\
//         'item_id' => 42,\
//     ],\
// ]
```

### `$order->getProductItems()` [​](https://dev.fluentcart.com/modules/fee-system\#order-getproductitems)

Returns order items excluding fees and signup fees. Use this whenever displaying product line items to avoid showing fee rows in the product list.

php

```
// Correct: excludes fee and signup_fee items
$products = $order->getProductItems();

// Also available on the order: the cached total
$feeTotal = $order->fee_total; // e.g., 650
```

* * *

## Fee Item Structure in Order Items [​](https://dev.fluentcart.com/modules/fee-system\#fee-item-structure-in-order-items)

When a fee becomes an order item, it has this structure in `fct_order_items`:

| Column | Value | Notes |
| --- | --- | --- |
| `post_id` | `0` | No product |
| `object_id` | `0` | No variation |
| `title` | `"Processing Fee"` | The fee label |
| `quantity` | `1` | Always 1 |
| `unit_price` | `450` | Amount in cents |
| `subtotal` | `450` | Same as unit\_price |
| `line_total` | `450` | Same as subtotal |
| `payment_type` | `'fee'` | Identifies as a fee |
| `other_info` | JSON | Contains `fee_key`, `source`, `taxable`, `meta` |

* * *

## Actions [​](https://dev.fluentcart.com/modules/fee-system\#actions)

### `fluent_cart/cart/fees_calculated` [​](https://dev.fluentcart.com/modules/fee-system\#fluent-cart-cart-fees-calculated)

Fired after fees are collected and stored on the cart during checkout summary recalculation.

php

```
add_action('fluent_cart/cart/fees_calculated', function (array $fees, $cart) {
    // Log or track fee activity
    if (!empty($fees)) {
        error_log('Fees applied: ' . count($fees) . ' for cart #' . $cart->id);
    }
}, 10, 2);
```

### `fluent_cart/order/fee_items_created` [​](https://dev.fluentcart.com/modules/fee-system\#fluent-cart-order-fee-items-created)

Fired after fee order items are created during order placement.

php

```
add_action('fluent_cart/order/fee_items_created', function (array $feeOrderItems, $order) {
    // Post-creation processing
}, 10, 2);
```

* * *

## Important Behavior Notes [​](https://dev.fluentcart.com/modules/fee-system\#important-behavior-notes)

1. **Fees are recalculated on every checkout update.** Dynamic fees (via filter) run whenever the checkout summary refreshes - item changes, coupon application, payment method change, address change, etc.

2. **Fees are not applied to subscription renewals.** The filter is skipped when `checkout_data.renew_data.is_renewal` is `yes`.

3. **Fees are not applied to locked carts.** Custom/manual checkout carts that are locked return only stored fees without running the filter.

4. **Deduplication uses `source:key`.** Two addons can both register a fee with `key = 'processing_fee'` as long as they use different `source` values.

5. **Fees are read-only after order creation.** Once an order is placed, fee items cannot be edited from the admin panel.

6. **Fees participate in proportional refunds.** When an order is refunded, fee items are included in the proportional distribution automatically.

7. **Per-request caching.**`getFees()` caches results within a single request. Call `$cart->clearFeeCache()` if you modify fees and need to re-read within the same request.

8. **Recursion guard.** If your filter callback calls `$cart->getFees()`, it returns only stored fees (not the filter result) to prevent infinite loops.


* * *

## Complete Example: Tiered Handling Fee Addon [​](https://dev.fluentcart.com/modules/fee-system\#complete-example-tiered-handling-fee-addon)

A full working example that applies tiered handling fees based on cart subtotal:

php

```
<?php
/**
 * Plugin Name: FluentCart Handling Fee
 * Description: Adds tiered handling fees based on cart subtotal.
 */

add_filter('fluent_cart/cart/fees', function (array $fees, array $context) {
    $subtotal = $context['cart_subtotal'];

    if ($subtotal <= 0) {
        return $fees;
    }

    // Tiered handling fee
    $feeAmount = match (true) {
        $subtotal < 2000  => 500,  // Under $20: $5.00 fee
        $subtotal < 5000  => 300,  // $20-$49.99: $3.00 fee
        $subtotal < 10000 => 100,  // $50-$99.99: $1.00 fee
        default           => 0,    // $100+: no fee
    };

    if ($feeAmount > 0) {
        $fees[] = [\
            'key'     => 'handling_fee',\
            'label'   => __('Handling Fee', 'my-handling-fee'),\
            'amount'  => $feeAmount,\
            'taxable' => false,\
            'source'  => 'handling-fee-addon',\
            'meta'    => [\
                'tier'     => $subtotal < 2000 ? 'small' : ($subtotal < 5000 ? 'medium' : 'large'),\
                'subtotal' => $subtotal,\
            ],\
        ];
    }

    return $fees;
}, 10, 2);
```

* * *

## Related Documentation [​](https://dev.fluentcart.com/modules/fee-system\#related-documentation)

- [Developer Hooks](https://dev.fluentcart.com/hooks/) \- Complete hooks and filters reference
- [Orders API](https://dev.fluentcart.com/restapi/operations/orders/) \- Order management API
- [Database Models](https://dev.fluentcart.com/database/models/) \- Data model documentation
- [Ghost Product Selling](https://dev.fluentcart.com/modules/ghost-product-selling.html) \- Custom product selling guide

* * *

**Next Steps:** Explore [Custom Payment Gateway Integration](https://dev.fluentcart.com/payment-methods-integration/) or return to [Getting Started](https://dev.fluentcart.com/getting-started.html)

Was this article helpful?

### Comments

Sign in to comment:

No comments yet. Be the first to share your thoughts!

Today

Hi! I’m your AI assistant. How can I assist you today?

Just now

Powered by **FluentBot**


---

## Ghost Product Selling Options | FluentCart Developer Docs

**URL** : https://dev.fluentcart.com/modules/ghost-product-selling

[Skip to content](https://dev.fluentcart.com/modules/ghost-product-selling#VPContent)

# Ghost Product Selling Options [​](https://dev.fluentcart.com/modules/ghost-product-selling\#ghost-product-selling-options)

FluentCart provides a powerful hook system that allows developers to sell ghost products that don't exist in the product catalog. This feature enables selling add-ons, gift wrapping, custom subscriptions, and any other custom items through your store.

## Overview [​](https://dev.fluentcart.com/modules/ghost-product-selling\#overview)

Custom product selling allows you to add items to the cart that are not stored as regular products in the database. This is useful for:

- **Add-on Products** \- Gift wrapping, insurance, custom options
- **Custom Subscriptions** \- Recurring billing for non-catalog items
- **Dynamic Products** \- Products created on-the-fly based on user selections
- **Service-Based Items** \- One-time or recurring service purchases

## Implementation Flow [​](https://dev.fluentcart.com/modules/ghost-product-selling\#implementation-flow)

The complete implementation follows this flow:

```
Add Button → Add Validation Hook → Handle Quantity Change Hook → Checkout Validation Hook
```

* * *

## Step 1: Add Button (Frontend) [​](https://dev.fluentcart.com/modules/ghost-product-selling\#step-1-add-button-frontend)

Add the appropriate button to your page based on the item type.

### One-Time Custom Item (Add to Cart) [​](https://dev.fluentcart.com/modules/ghost-product-selling\#one-time-custom-item-add-to-cart)

For one-time purchases that are added to the cart:

html

```
<button
    data-cart-id="1000"
    data-quantity="1"
    data-is-custom="true"
    data-fluent-cart-add-to-cart-button
>
  Add Gift Wrapping
</button>
```

### Subscription Custom Item (Instant Checkout) [​](https://dev.fluentcart.com/modules/ghost-product-selling\#subscription-custom-item-instant-checkout)

For subscription items that go directly to checkout:

html

```
<a href="https://yourstore.com/?fluent-cart=instant_checkout&item_id=3001&quantity=1&is_custom=true">
  Buy Now
</a>
```

**Note:** Replace `https://yourstore.com` with your actual site URL and `3001` with your custom item ID.

* * *

## Step 2: Add Validation Hook (Backend) [​](https://dev.fluentcart.com/modules/ghost-product-selling\#step-2-add-validation-hook-backend)

Use this filter to validate and return the custom product item when it's added to the cart.

### Hook: `fluent_cart/cart/validate_custom_item` [​](https://dev.fluentcart.com/modules/ghost-product-selling\#hook-fluent-cart-cart-validate-custom-item)

**Parameters:**

- `$variation` (object/array): The variation object to be modified
- `$item` (array): The item data from the request

**Returns:** The modified variation object

### Example: Validate New Custom Item [​](https://dev.fluentcart.com/modules/ghost-product-selling\#example-validate-new-custom-item)

php

```
add_filter('fluent_cart/cart/validate_custom_item',
function($variation, $item) {
    if ((bool)$item['is_custom']) {
        $variation = (object) [\
            'item_id'      => absint($item['item_id']),\
            'object_id'    => absint($item['item_id']),\
            'post_id'      => 5000,\
            'quantity'     => max(1, (int)$item['quantity']),\
            'price'        => floatval(5000),\
            'unit_price'   => floatval(5000),\
            'line_total'   => floatval(5000) * max(1, (int)$item['quantity']),\
            'post_title'   => sanitize_text_field('Weekly Protein Pack'),\
            'title'        => sanitize_text_field('Subscription Version 1'),\
            'is_custom'    => true,\
            'payment_type' => 'subscription',\
            "other_info"       => [\
                "payment_type"      => "subscription",\
                "repeat_interval"   => "monthly",\
                "installment"     => "no",\
                "manage_setup_fee" => "yes",\
                 "signup_fee"       => 500\
            ],\
\
        ];
    }
    return $variation;
}, 10, 2);
```

* * *

## Step 3: Handle Quantity Changes (Cart) [​](https://dev.fluentcart.com/modules/ghost-product-selling\#step-3-handle-quantity-changes-cart)

This step applies only to one-time items for quantity increment/decrement actions.

### Hook: `fluent_cart/cart/custom_item_quantity_changed` [​](https://dev.fluentcart.com/modules/ghost-product-selling\#hook-fluent-cart-cart-custom-item-quantity-changed)

**Parameters:**

- `$variation` (object/array): The variation object to be updated
- `$item` (array): Item data including quantity changes

**Returns:** The modified variation object with updated quantity and totals

### Example: Change Existing Item Quantity [​](https://dev.fluentcart.com/modules/ghost-product-selling\#example-change-existing-item-quantity)

php

```
add_filter('fluent_cart/cart/custom_item_quantity_changed', function ($variation, $item) {

    if (empty($item['is_custom'])) {
        return $variation;
    }

    // Ensure array
    $variation = (array) $variation;

    $newQty  = (int) ($item['new_quantity'] ?? 1);
    $oldQty  = (int) ($item['old_quantity'] ?? 1);
    $byInput = (bool) ($item['by_input'] ?? false);

    /**
     * If quantity changed via increment, decrement or delete buttons
     */
    if (!$byInput) {
        $newQty = $newQty == 0 ? 0 : ($oldQty+$newQty);
    }

    $price = (float) ($variation['price'] ?? 0);

    $variation['quantity']   = $newQty;
    $variation['line_total'] = $price * $newQty;

    return $variation;

}, 10, 2);
```

* * *

## Step 4: Checkout Validation [​](https://dev.fluentcart.com/modules/ghost-product-selling\#step-4-checkout-validation)

This hook runs before payment processing for both one-time and subscription items.

### Hook: `fluent_cart/payment/validate_custom_item` [​](https://dev.fluentcart.com/modules/ghost-product-selling\#hook-fluent-cart-payment-validate-custom-item)

**Parameters:**

- `$items` (array): Array containing product and variation objects
- `$data` (array): Additional checkout data

**Returns:** Modified items array

### Example: Payment Validate Item [​](https://dev.fluentcart.com/modules/ghost-product-selling\#example-payment-validate-item)

php

```
add_filter('fluent_cart/payment/validate_custom_item', function ($items, $data) {

    [$product, $variation] = $items;

    // Mark the item as custom visually
    $variation->title    .= ' (Custom Item)';
    $product->post_title .= ' [Custom]';

    return [$product, $variation];

}, 10, 2);
```

* * *

## Step 5: Admin Order Update Handling (Optional) [​](https://dev.fluentcart.com/modules/ghost-product-selling\#step-5-admin-order-update-handling-optional)

Handle custom item updates from the WordPress admin panel after an order is placed.

### Order Item Changed [​](https://dev.fluentcart.com/modules/ghost-product-selling\#order-item-changed)

**Action:**`fluent_cart/order/custom_item_changed`

**Parameters:**

- `$oldItem` (array): The original item data
- `$item` (array): The updated item data

**Returns:** The item to be saved

#### Example: Order Item Changed [​](https://dev.fluentcart.com/modules/ghost-product-selling\#example-order-item-changed)

php

```
add_filter('fluent_cart/order/custom_item_changed', function ($oldItem, $item) {

    $oldItem = (array) $oldItem;
    $item    = (array) $item;

    $isCustom = (bool) ($item['is_custom'] ?? false);
    $newQuantity  = (int) ($item['quantity'] ?? 1);
    $oldQuantity  = (int) ($oldItem['quantity'] ?? 1);

    /**
     * If item is a Custom Item → always save updated changes
     */
    if ($isCustom) {
        return $item;
    }

    /**
     * If quantity is unchanged → return old item (no update)
     */
    if ($oldQuantity === $newQuantity) {
        return $oldItem;
    }

    /**
     * If quantity changed → allow update
     */
    return $item;

}, 10, 2);
```

### Before Custom Items Are Deleted [​](https://dev.fluentcart.com/modules/ghost-product-selling\#before-custom-items-are-deleted)

**Action:**`fluent_cart/order/before_custom_items_deleted`

**Parameters:**

- `$customItems` (array): Array of custom items to be deleted
- `$order` (object): The order object

#### Example: Before Order Item Deleted [​](https://dev.fluentcart.com/modules/ghost-product-selling\#example-before-order-item-deleted)

php

```
add_action('fluent_cart/order/before_custom_items_deleted', function ($customItems, $order) {

    foreach ($customItems as $item) {
        error_log(
            sprintf(
                'Custom item about to be deleted. Order #%d | Item ID: %d | Qty: %d',
                $order->id,
                $item->id,
                $item->quantity
            )
        );

        // Restore external stock if needed
    }

}, 10, 2);
```

### After Custom Items Are Deleted [​](https://dev.fluentcart.com/modules/ghost-product-selling\#after-custom-items-are-deleted)

**Action:**`fluent_cart/order/after_custom_items_deleted`

**Parameters:**

- `$customItems` (array): Array of deleted custom items
- `$order` (object): The order object

#### Example: After Order Item Deleted [​](https://dev.fluentcart.com/modules/ghost-product-selling\#example-after-order-item-deleted)

php

```
add_action('fluent_cart/order/after_custom_items_deleted', function ($customItems, $order) {

    foreach ($customItems as $item) {
        error_log(
            sprintf(
                'Custom item deleted. Order #%d | Item ID: %d | Qty: %d',
                $order->id,
                $item->id,
                $item->quantity
            )
        );

        // Analytics or internal counters
        // Notify admin
        // wp_mail('admin@example.com', 'Custom Item Deleted', 'Item ID ' . $item->id . ' was deleted');
    }

}, 10, 2);
```

* * *

## Sample Datasets [​](https://dev.fluentcart.com/modules/ghost-product-selling\#sample-datasets)

### One-Time Item [​](https://dev.fluentcart.com/modules/ghost-product-selling\#one-time-item)

php

```
$item = [\
    "item_id"          => 1000,\
    "object_id"       => 1000,\
    "post_id"          => 10000,\
    "quantity"        => 1,\
    "is_custom"      => true,\
    "post_title"        => "Air Max 1 running shoe",\
    "title"                 => "Version 1",\
    "price"               => 2000,\
    "unit_price"      => 2000,\
    "line_total"        => 2000 * 1, // quantity is 1\
    "payment_type"     => "onetime",\
    "fulfillment_type" => "digital",\
    "featured_media"   => "http://wordpress.test/wp-content/uploads/2025/11/white-navy-athletic-shoe-4-1.jpeg",\
    "sold_individually"=> 0,\
    "other_info"       => [\
        "payment_type" => "onetime"\
    ],\
    "view_url"         => "https://www.abelandcole.co.uk/turkey-breast-joint-high-welfare-kellybronze?cid=9427"\
];
```

### Subscription Item [​](https://dev.fluentcart.com/modules/ghost-product-selling\#subscription-item)

php

```
$item = [\
    "item_id"          => 2000,\
    "object_id"       => 2000,\
    "post_id"          => 20000,\
    "quantity"        => 1, // always 1 for subscription\
    "is_custom"      => true,\
    "post_title"        => "Weekly Protein Pack",\
    "title"                 => "Subscription Version 1",\
    "price"               => 2500,\
    "unit_price"      => 2500,\
    "line_total"       => 2500 * 1,\
    "payment_type"     => "subscription",\
    "fulfillment_type" => "digital",\
    "featured_media"   => "http://wordpress.test/wp-content/uploads/2025/11/protein-pack-1.jpeg",\
    "sold_individually"=> 1, // enforce quantity = 1\
    "other_info"       => [\
        "payment_type"      => "subscription",\
        "repeat_interval"   => "monthly",\
        "installment"     => "no",\
        "manage_setup_fee" => "yes",\
         "signup_fee"       => 500\
    ],\
    "view_url"         => "https://www.abelandcole.co.uk/weekly-protein-pack?cid=9428"\
];
```

### Payment Gateway Validation During Checkout [​](https://dev.fluentcart.com/modules/ghost-product-selling\#payment-gateway-validation-during-checkout)

php

```
$variation = (object)[\
    "item_id"          => 1000,\
    "object_id"        => 1000,\
    "post_id"          => 10000,\
    "quantity"         => 1,\
    "is_custom"        => true,\
    "post_title"       => "Air Max 1 running shoe",\
    "title"            => "Version 1",\
    "price"            => 2000,\
    "unit_price"       => 2000,\
    "line_total"       => 2000 * 1,\
    "payment_type"     => "onetime",\
    "fulfillment_type" => "digital",\
    "featured_media"   => "http://wordpress.test/wp-content/uploads/2025/11/white-navy-athletic-shoe-4-1.jpeg",\
    "sold_individually"=> 0,\
    "other_info"       => [\
        "payment_type" => "onetime"\
    ],\
    "view_url"         => "https://www.example.com/product/air-max-1-running-shoe"\
];

$product = (object)[\
    "ID"           => 148,\
    "post_title"   => "Air Max 1 running shoe",\
    "post_status"  => "publish",\
];
```

* * *

## Key Properties Reference [​](https://dev.fluentcart.com/modules/ghost-product-selling\#key-properties-reference)

### Item Object Properties [​](https://dev.fluentcart.com/modules/ghost-product-selling\#item-object-properties)

| Property | Type | Description | Example |
| --- | --- | --- | --- |
| `item_id` | integer | Unique identifier for the custom item | `1000` |
| `object_id` | integer | Reference ID for the item | `1000` |
| `post_id` | integer | WordPress post ID reference | `5000` |
| `quantity` | integer | Item quantity | `1` |
| `is_custom` | boolean | Marks item as custom | `true` |
| `post_title` | string | Product title | `"Air Max 1 running shoe"` |
| `title` | string | Variation title | `"Version 1"` |
| `price` | float | Unit price | `2000` |
| `unit_price` | float | Unit price (same as price) | `2000` |
| `line_total` | float | Total price (price × quantity) | `2000` |
| `payment_type` | string | `onetime` or `subscription` | `"onetime"` |
| `fulfillment_type` | string | `digital` or `physical` | `"digital"` |
| `featured_media` | string | Media URL | `"http://..."` |
| `sold_individually` | integer | `0` for no, `1` for yes | `0` |
| `other_info` | array | Additional information | See below |

### other\_info Properties for Subscriptions [​](https://dev.fluentcart.com/modules/ghost-product-selling\#other-info-properties-for-subscriptions)

| Property | Type | Description | Example |
| --- | --- | --- | --- |
| `payment_type` | string | Type of payment | `"subscription"` |
| `repeat_interval` | string | Billing frequency | `"monthly"` |
| `installment` | string | Installment plan | `"no"` |
| `manage_setup_fee` | string | Enable setup fee | `"yes"` |
| `signup_fee` | float | Setup fee amount | `500` |

* * *

## Best Practices [​](https://dev.fluentcart.com/modules/ghost-product-selling\#best-practices)

1. **Always Validate Data**: Use the validation hook to ensure item data is correct before adding to cart
2. **Handle Quantity Changes**: Implement quantity change handlers for one-time items
3. **Mark Custom Items**: Use `is_custom` flag to distinguish custom items from regular products (required for all custom items)
4. **Set Correct Payment Type**: Ensure `payment_type` is set correctly (`onetime` or `subscription`)
5. **Calculate Totals**: Always calculate `line_total` as `price × quantity`
6. **Use Sanitization**: Apply `sanitize_text_field()` and `absint()` for security
7. **Handle Admin Actions**: Implement order update handlers if admins will modify orders

* * *

## Related Documentation [​](https://dev.fluentcart.com/modules/ghost-product-selling\#related-documentation)

- [Developer Hooks](https://dev.fluentcart.com/hooks/) \- Complete hooks and filters reference
- [Products API](https://dev.fluentcart.com/api/products/) \- Product management API
- [Orders API](https://dev.fluentcart.com/api/orders/) \- Order management API
- [Database Models](https://dev.fluentcart.com/database/models/) \- Data model documentation

* * *

**Next Steps:** Explore [Payment Methods Module](https://dev.fluentcart.com/modules/payment-methods.html) or return to [Modules Overview](https://dev.fluentcart.com/modules/)

Today

Hi! I’m your AI assistant. How can I assist you today?

Just now

Powered by **FluentBot**


---

## Payment Methods Module | FluentCart Developer Docs

**URL** : https://dev.fluentcart.com/modules/payment-methods

[Skip to content](https://dev.fluentcart.com/modules/payment-methods#VPContent)

# Payment Methods Module [​](https://dev.fluentcart.com/modules/payment-methods\#payment-methods-module)

The Payment Methods module is FluentCart's core payment processing system. It provides a flexible architecture for integrating various payment gateways while maintaining a consistent interface for order processing.

## Architecture Overview [​](https://dev.fluentcart.com/modules/payment-methods\#architecture-overview)

### Core Components [​](https://dev.fluentcart.com/modules/payment-methods\#core-components)

#### 1\. **GatewayManager** [​](https://dev.fluentcart.com/modules/payment-methods\#_1-gatewaymanager)

The central manager for all payment gateways using the Singleton pattern.

php

```
use FluentCart\App\Modules\PaymentMethods\Core\GatewayManager;

// Get manager instance
$manager = GatewayManager::getInstance();

// Get specific gateway
$stripe = GatewayManager::gateway('stripe');

// Check if gateway exists
$exists = GatewayManager::has('stripe');
```

#### 2\. **PaymentGatewayInterface** [​](https://dev.fluentcart.com/modules/payment-methods\#_2-paymentgatewayinterface)

The interface that all payment gateways must implement.

php

```
interface PaymentGatewayInterface
{
    public function has(string $feature): bool;
    public function meta(): array;
    public function makePaymentFromPaymentInstance(PaymentInstance $paymentInstance);
    public function handleIPN();
    public function getOrderInfo(array $data);
    public function fields();
}
```

#### 3\. **AbstractPaymentGateway** [​](https://dev.fluentcart.com/modules/payment-methods\#_3-abstractpaymentgateway)

Base class providing common functionality for all gateways.

php

```
abstract class AbstractPaymentGateway implements PaymentGatewayInterface
{
    public array $supportedFeatures = [];
    public StoreSettings $storeSettings;
    public ?AbstractSubscriptionModule $subscriptions;
    public BaseGatewaySettings $settings;
}
```

## Supported Payment Gateways [​](https://dev.fluentcart.com/modules/payment-methods\#supported-payment-gateways)

### Built-in Gateways [​](https://dev.fluentcart.com/modules/payment-methods\#built-in-gateways)

#### **Stripe** [​](https://dev.fluentcart.com/modules/payment-methods\#stripe)

- **Features**: Payment, Refund, Webhook, Custom Payment, Card Update, Dispute Handler
- **Supported**: Credit Cards, Debit Cards, Digital Wallets
- **Location**: `app/Modules/PaymentMethods/StripeGateway/`

#### **PayPal** [​](https://dev.fluentcart.com/modules/payment-methods\#paypal)

- **Features**: Payment, Refund, Webhook, Subscriptions
- **Supported**: PayPal, Credit Cards via PayPal
- **Location**: `app/Modules/PaymentMethods/PayPalGateway/`

#### **Mollie** [​](https://dev.fluentcart.com/modules/payment-methods\#mollie)

- **Features**: Payment, Refund, Webhook
- **Supported**: Credit Cards, SEPA, iDEAL, Bancontact
- **Location**: `app/Modules/PaymentMethods/MollieGateway/`

#### **Square** [​](https://dev.fluentcart.com/modules/payment-methods\#square)

- **Features**: Payment, Refund, Webhook
- **Supported**: Credit Cards, Digital Wallets
- **Location**: `app/Modules/PaymentMethods/SquareGateway/`

#### **Razorpay** [​](https://dev.fluentcart.com/modules/payment-methods\#razorpay)

- **Features**: Payment, Refund, Webhook
- **Supported**: Credit Cards, UPI, Net Banking, Wallets
- **Location**: `app/Modules/PaymentMethods/RazorpayGateway/`

#### **Paystack** [​](https://dev.fluentcart.com/modules/payment-methods\#paystack)

- **Features**: Payment, Refund, Webhook
- **Supported**: Credit Cards, Bank Transfer, Mobile Money
- **Location**: `app/Modules/PaymentMethods/PaystackGateway/`

#### **Authorize.Net** [​](https://dev.fluentcart.com/modules/payment-methods\#authorize-net)

- **Features**: Payment, Refund, Webhook
- **Supported**: Credit Cards, ACH
- **Location**: `app/Modules/PaymentMethods/AuthorizeNetGateway/`

#### **Airwallex** [​](https://dev.fluentcart.com/modules/payment-methods\#airwallex)

- **Features**: Payment, Refund, Webhook
- **Supported**: Credit Cards, Local Payment Methods
- **Location**: `app/Modules/PaymentMethods/AirwallexGateway/`

#### **Cash on Delivery (COD)** [​](https://dev.fluentcart.com/modules/payment-methods\#cash-on-delivery-cod)

- **Features**: Payment, Refund
- **Supported**: Cash on Delivery
- **Location**: `app/Modules/PaymentMethods/Cod/`

## Gateway Development [​](https://dev.fluentcart.com/modules/payment-methods\#gateway-development)

### Creating a Custom Payment Gateway [​](https://dev.fluentcart.com/modules/payment-methods\#creating-a-custom-payment-gateway)

#### 1\. **Create Gateway Directory Structure** [​](https://dev.fluentcart.com/modules/payment-methods\#_1-create-gateway-directory-structure)

```
app/Modules/PaymentMethods/YourGateway/
├── YourGateway.php              # Main gateway class
├── Settings/
│   └── YourGatewaySettings.php  # Gateway settings
├── API/
│   └── YourGatewayAPI.php       # API communication
├── Webhook/
│   └── WebhookHandler.php       # Webhook processing
├── Views/
│   └── payment-form.php         # Payment form template
└── Assets/
    ├── css/
    ├── js/
    └── images/
```

#### 2\. **Create Main Gateway Class** [​](https://dev.fluentcart.com/modules/payment-methods\#_2-create-main-gateway-class)

php

```
<?php
namespace FluentCart\App\Modules\PaymentMethods\YourGateway;

use FluentCart\App\Modules\PaymentMethods\Core\AbstractPaymentGateway;
use FluentCart\App\Services\Payments\PaymentInstance;
use FluentCart\App\Vite;

class YourGateway extends AbstractPaymentGateway
{
    public array $supportedFeatures = [\
        'payment',\
        'refund',\
        'webhook'\
    ];

    public function __construct()
    {
        parent::__construct(new YourGatewaySettings());
    }

    public function meta(): array
    {
        return [\
            'title' => __('Your Gateway', 'fluent-cart'),\
            'route' => 'your_gateway',\
            'slug' => 'your_gateway',\
            'description' => __('Accept payments with Your Gateway', 'fluent-cart'),\
            'logo' => Vite::getAssetUrl('images/payment-methods/your-gateway-logo.svg'),\
            'icon' => Vite::getAssetUrl('images/payment-methods/your-gateway-icon.svg'),\
            'brand_color' => '#your-brand-color',\
            'status' => $this->settings->get('is_active') === 'yes',\
            'upcoming' => false,\
            'supported_features' => $this->supportedFeatures\
        ];
    }

    public function boot()
    {
        // Initialize webhook handler
        add_action('wp_ajax_your_gateway_webhook', [$this, 'handleWebhook']);
        add_action('wp_ajax_nopriv_your_gateway_webhook', [$this, 'handleWebhook']);

        // Register settings filter
        add_filter('fluent_cart/payment_methods/your_gateway_settings', [$this, 'getSettings'], 10, 2);
    }

    public function makePaymentFromPaymentInstance(PaymentInstance $paymentInstance)
    {
        $order = $paymentInstance->order;
        $transaction = $paymentInstance->transaction;

        // Prepare payment data
        $paymentData = [\
            'amount' => $transaction->total,\
            'currency' => $transaction->currency,\
            'order_id' => $order->uuid,\
            'customer_email' => $order->email,\
            'return_url' => $this->getReturnUrl($transaction),\
            'cancel_url' => $this->getCancelUrl($transaction)\
        ];

        // Process payment with gateway API
        $result = $this->processPayment($paymentData);

        if ($result['success']) {
            return [\
                'success' => true,\
                'redirect_url' => $result['redirect_url'],\
                'payment_id' => $result['payment_id']\
            ];
        }

        return [\
            'success' => false,\
            'message' => $result['error_message']\
        ];
    }

    public function handleIPN()
    {
        $webhookData = $this->getWebhookData();

        if (!$this->verifyWebhookSignature($webhookData)) {
            http_response_code(400);
            exit('Invalid signature');
        }

        $this->processWebhook($webhookData);

        http_response_code(200);
        exit('OK');
    }

    public function getOrderInfo(array $data)
    {
        $orderId = $data['order_id'] ?? '';
        $order = Order::where('uuid', $orderId)->first();

        if (!$order) {
            return new \WP_Error('order_not_found', 'Order not found');
        }

        return [\
            'order' => $order,\
            'total' => $order->total,\
            'currency' => $order->currency,\
            'status' => $order->status\
        ];
    }

    public function fields()
    {
        return $this->settings->getFields();
    }

    private function processPayment($paymentData)
    {
        // Implement your gateway's payment processing logic
        $api = new YourGatewayAPI($this->settings);
        return $api->createPayment($paymentData);
    }

    private function processWebhook($webhookData)
    {
        $orderId = $webhookData['order_id'];
        $status = $webhookData['status'];

        $order = Order::where('uuid', $orderId)->first();

        if ($order) {
            $this->updateOrderStatus($order, $status);
        }
    }
}
```

#### 3\. **Create Gateway Settings** [​](https://dev.fluentcart.com/modules/payment-methods\#_3-create-gateway-settings)

php

```
<?php
namespace FluentCart\App\Modules\PaymentMethods\YourGateway\Settings;

use FluentCart\App\Modules\PaymentMethods\Core\BaseGatewaySettings;

class YourGatewaySettings extends BaseGatewaySettings
{
    public function getFields(): array
    {
        return [\
            'is_active' => [\
                'type' => 'yes_no',\
                'label' => __('Enable Your Gateway', 'fluent-cart'),\
                'default' => 'no',\
                'description' => __('Enable this payment method', 'fluent-cart')\
            ],\
            'api_key' => [\
                'type' => 'text',\
                'label' => __('API Key', 'fluent-cart'),\
                'required' => true,\
                'description' => __('Your gateway API key', 'fluent-cart')\
            ],\
            'secret_key' => [\
                'type' => 'password',\
                'label' => __('Secret Key', 'fluent-cart'),\
                'required' => true,\
                'description' => __('Your gateway secret key', 'fluent-cart')\
            ],\
            'webhook_secret' => [\
                'type' => 'password',\
                'label' => __('Webhook Secret', 'fluent-cart'),\
                'description' => __('Webhook secret for signature verification', 'fluent-cart')\
            ],\
            'test_mode' => [\
                'type' => 'yes_no',\
                'label' => __('Test Mode', 'fluent-cart'),\
                'default' => 'yes',\
                'description' => __('Enable test mode for development', 'fluent-cart')\
            ],\
            'debug_mode' => [\
                'type' => 'yes_no',\
                'label' => __('Debug Mode', 'fluent-cart'),\
                'default' => 'no',\
                'description' => __('Enable debug logging', 'fluent-cart')\
            ]\
        ];
    }

    public function getDefaultSettings(): array
    {
        return [\
            'is_active' => 'no',\
            'api_key' => '',\
            'secret_key' => '',\
            'webhook_secret' => '',\
            'test_mode' => 'yes',\
            'debug_mode' => 'no'\
        ];
    }
}
```

#### 4\. **Create API Communication Class** [​](https://dev.fluentcart.com/modules/payment-methods\#_4-create-api-communication-class)

php

```
<?php
namespace FluentCart\App\Modules\PaymentMethods\YourGateway\API;

use FluentCart\App\Modules\PaymentMethods\YourGateway\Settings\YourGatewaySettings;

class YourGatewayAPI
{
    private $settings;
    private $baseUrl;
    private $headers;

    public function __construct(YourGatewaySettings $settings)
    {
        $this->settings = $settings;
        $this->baseUrl = $settings->get('test_mode') === 'yes'
            ? 'https://api-test.yourgateway.com'
            : 'https://api.yourgateway.com';

        $this->headers = [\
            'Authorization' => 'Bearer ' . $settings->get('api_key'),\
            'Content-Type' => 'application/json',\
            'Accept' => 'application/json'\
        ];
    }

    public function createPayment($paymentData)
    {
        $response = wp_remote_post($this->baseUrl . '/payments', [\
            'headers' => $this->headers,\
            'body' => json_encode($paymentData),\
            'timeout' => 30\
        ]);

        if (is_wp_error($response)) {
            return [\
                'success' => false,\
                'error_message' => $response->get_error_message()\
            ];
        }

        $body = wp_remote_retrieve_body($response);
        $data = json_decode($body, true);

        if ($data['status'] === 'success') {
            return [\
                'success' => true,\
                'payment_id' => $data['payment_id'],\
                'redirect_url' => $data['redirect_url']\
            ];
        }

        return [\
            'success' => false,\
            'error_message' => $data['error_message']\
        ];
    }

    public function getPaymentStatus($paymentId)
    {
        $response = wp_remote_get($this->baseUrl . '/payments/' . $paymentId, [\
            'headers' => $this->headers,\
            'timeout' => 30\
        ]);

        if (is_wp_error($response)) {
            return false;
        }

        $body = wp_remote_retrieve_body($response);
        return json_decode($body, true);
    }

    public function refundPayment($paymentId, $amount, $reason = '')
    {
        $refundData = [\
            'amount' => $amount,\
            'reason' => $reason\
        ];

        $response = wp_remote_post($this->baseUrl . '/payments/' . $paymentId . '/refund', [\
            'headers' => $this->headers,\
            'body' => json_encode($refundData),\
            'timeout' => 30\
        ]);

        if (is_wp_error($response)) {
            return false;
        }

        $body = wp_remote_retrieve_body($response);
        return json_decode($body, true);
    }
}
```

#### 5\. **Create Webhook Handler** [​](https://dev.fluentcart.com/modules/payment-methods\#_5-create-webhook-handler)

php

```
<?php
namespace FluentCart\App\Modules\PaymentMethods\YourGateway\Webhook;

use FluentCart\App\Models\Order;
use FluentCart\App\Models\OrderTransaction;
use FluentCart\App\Services\PaymentHelper;

class WebhookHandler
{
    private $settings;

    public function __construct($settings)
    {
        $this->settings = $settings;
    }

    public function handleWebhook()
    {
        $webhookData = $this->getWebhookData();

        if (!$this->verifyWebhookSignature($webhookData)) {
            http_response_code(400);
            exit('Invalid signature');
        }

        $this->processWebhook($webhookData);

        http_response_code(200);
        exit('OK');
    }

    private function getWebhookData()
    {
        $input = file_get_contents('php://input');
        return json_decode($input, true);
    }

    private function verifyWebhookSignature($webhookData)
    {
        $signature = $_SERVER['HTTP_X_WEBHOOK_SIGNATURE'] ?? '';
        $secret = $this->settings->get('webhook_secret');

        $expectedSignature = hash_hmac('sha256', json_encode($webhookData), $secret);

        return hash_equals($expectedSignature, $signature);
    }

    private function processWebhook($webhookData)
    {
        $eventType = $webhookData['event_type'];
        $paymentId = $webhookData['payment_id'];
        $orderId = $webhookData['order_id'];

        $order = Order::where('uuid', $orderId)->first();

        if (!$order) {
            return;
        }

        switch ($eventType) {
            case 'payment.completed':
                $this->handlePaymentCompleted($order, $webhookData);
                break;

            case 'payment.failed':
                $this->handlePaymentFailed($order, $webhookData);
                break;

            case 'payment.refunded':
                $this->handlePaymentRefunded($order, $webhookData);
                break;
        }
    }

    private function handlePaymentCompleted($order, $webhookData)
    {
        $order->update([\
            'status' => 'completed',\
            'payment_status' => 'paid'\
        ]);

        // Create transaction record
        OrderTransaction::create([\
            'order_id' => $order->id,\
            'transaction_id' => $webhookData['payment_id'],\
            'type' => 'payment',\
            'status' => 'completed',\
            'amount' => $webhookData['amount'],\
            'currency' => $webhookData['currency'],\
            'gateway' => 'your_gateway',\
            'gateway_response' => json_encode($webhookData)\
        ]);

        // Trigger payment success action
        do_action('fluent_cart/payment_success', [\
            'order' => $order,\
            'gateway' => 'your_gateway',\
            'transaction_id' => $webhookData['payment_id']\
        ]);
    }

    private function handlePaymentFailed($order, $webhookData)
    {
        $order->update([\
            'status' => 'failed',\
            'payment_status' => 'failed'\
        ]);

        // Trigger payment failed action
        do_action('fluent_cart/payment_failed', [\
            'order' => $order,\
            'gateway' => 'your_gateway',\
            'error_message' => $webhookData['error_message']\
        ]);
    }

    private function handlePaymentRefunded($order, $webhookData)
    {
        // Create refund transaction record
        OrderTransaction::create([\
            'order_id' => $order->id,\
            'transaction_id' => $webhookData['refund_id'],\
            'type' => 'refund',\
            'status' => 'completed',\
            'amount' => $webhookData['refund_amount'],\
            'currency' => $webhookData['currency'],\
            'gateway' => 'your_gateway',\
            'gateway_response' => json_encode($webhookData)\
        ]);

        // Trigger refund action
        do_action('fluent_cart/payment_refunded', [\
            'order' => $order,\
            'gateway' => 'your_gateway',\
            'refund_id' => $webhookData['refund_id'],\
            'refund_amount' => $webhookData['refund_amount']\
        ]);
    }
}
```

### Gateway Registration [​](https://dev.fluentcart.com/modules/payment-methods\#gateway-registration)

#### Register Your Gateway [​](https://dev.fluentcart.com/modules/payment-methods\#register-your-gateway)

php

```
// In your plugin's main file or module initialization
add_action('fluentcart_loaded', function($app) {
    $gatewayManager = \FluentCart\App\Modules\PaymentMethods\Core\GatewayManager::getInstance();
    $gatewayManager->register('your_gateway', new \FluentCart\App\Modules\PaymentMethods\YourGateway\YourGateway());
});
```

#### Gateway Configuration [​](https://dev.fluentcart.com/modules/payment-methods\#gateway-configuration)

php

```
// Get gateway settings
$gateway = GatewayManager::gateway('your_gateway');
$settings = $gateway->settings;

// Check if gateway is enabled
$isEnabled = $gateway->settings->get('is_active') === 'yes';

// Get gateway meta information
$meta = $gateway->meta();
```

## Payment Processing Flow [​](https://dev.fluentcart.com/modules/payment-methods\#payment-processing-flow)

### 1\. **Payment Initiation** [​](https://dev.fluentcart.com/modules/payment-methods\#_1-payment-initiation)

php

```
// Create payment instance
$paymentInstance = new PaymentInstance([\
    'order' => $order,\
    'transaction' => $transaction,\
    'gateway' => 'your_gateway'\
]);

// Process payment
$gateway = GatewayManager::gateway('your_gateway');
$result = $gateway->makePaymentFromPaymentInstance($paymentInstance);
```

### 2\. **Payment Response Handling** [​](https://dev.fluentcart.com/modules/payment-methods\#_2-payment-response-handling)

php

```
if ($result['success']) {
    // Redirect to payment page
    wp_redirect($result['redirect_url']);
    exit;
} else {
    // Handle payment error
    wc_add_notice($result['message'], 'error');
}
```

### 3\. **Webhook Processing** [​](https://dev.fluentcart.com/modules/payment-methods\#_3-webhook-processing)

php

```
// Webhook endpoint: /wp-ajax/your_gateway_webhook
public function handleWebhook()
{
    $webhookHandler = new WebhookHandler($this->settings);
    $webhookHandler->handleWebhook();
}
```

## Gateway Features [​](https://dev.fluentcart.com/modules/payment-methods\#gateway-features)

### Supported Features [​](https://dev.fluentcart.com/modules/payment-methods\#supported-features)

#### **Payment Processing** [​](https://dev.fluentcart.com/modules/payment-methods\#payment-processing)

- One-time payments
- Recurring payments (subscriptions)
- Payment method storage
- Payment method updates

#### **Refund Management** [​](https://dev.fluentcart.com/modules/payment-methods\#refund-management)

- Full refunds
- Partial refunds
- Refund status tracking
- Refund notifications

#### **Webhook Handling** [​](https://dev.fluentcart.com/modules/payment-methods\#webhook-handling)

- Real-time payment notifications
- Signature verification
- Event processing
- Error handling

#### **Security Features** [​](https://dev.fluentcart.com/modules/payment-methods\#security-features)

- API key management
- Webhook signature verification
- Test mode support
- Debug logging

### Feature Implementation [​](https://dev.fluentcart.com/modules/payment-methods\#feature-implementation)

#### **Subscription Support** [​](https://dev.fluentcart.com/modules/payment-methods\#subscription-support)

php

```
class YourGateway extends AbstractPaymentGateway
{
    public function __construct()
    {
        parent::__construct(
            new YourGatewaySettings(),
            new YourGatewaySubscriptions() // Add subscription support
        );
    }

    public array $supportedFeatures = [\
        'payment',\
        'refund',\
        'webhook',\
        'subscriptions' // Enable subscription feature\
    ];
}
```

#### **Refund Support** [​](https://dev.fluentcart.com/modules/payment-methods\#refund-support)

php

```
public function processRefund($transaction, $amount, $args = [])
{
    $api = new YourGatewayAPI($this->settings);
    $result = $api->refundPayment($transaction->transaction_id, $amount);

    if ($result['success']) {
        return [\
            'success' => true,\
            'refund_id' => $result['refund_id']\
        ];
    }

    return new \WP_Error('refund_failed', $result['error_message']);
}
```

## Testing and Debugging [​](https://dev.fluentcart.com/modules/payment-methods\#testing-and-debugging)

### Test Mode Configuration [​](https://dev.fluentcart.com/modules/payment-methods\#test-mode-configuration)

php

```
// Enable test mode in settings
$settings = [\
    'test_mode' => 'yes',\
    'debug_mode' => 'yes'\
];
```

### Debug Logging [​](https://dev.fluentcart.com/modules/payment-methods\#debug-logging)

php

```
public function logDebug($message, $data = [])
{
    if ($this->settings->get('debug_mode') === 'yes') {
        error_log('YourGateway: ' . $message . ' - ' . json_encode($data));
    }
}
```

### Testing Webhooks [​](https://dev.fluentcart.com/modules/payment-methods\#testing-webhooks)

php

```
// Test webhook locally using ngrok or similar
$webhookUrl = 'https://your-ngrok-url.ngrok.io/wp-ajax/your_gateway_webhook';

// Send test webhook
$testData = [\
    'event_type' => 'payment.completed',\
    'payment_id' => 'test_payment_123',\
    'order_id' => 'test_order_456',\
    'amount' => 1000,\
    'currency' => 'USD'\
];

wp_remote_post($webhookUrl, [\
    'body' => json_encode($testData),\
    'headers' => [\
        'Content-Type' => 'application/json',\
        'X-Webhook-Signature' => $this->generateSignature($testData)\
    ]\
]);
```

* * *

**Next Steps:**

- [Shipping Module](https://dev.fluentcart.com/modules/shipping.html) \- Shipping method development
- [Storage Drivers](https://dev.fluentcart.com/modules/storage.html) \- File storage integration
- [Modules Overview](https://dev.fluentcart.com/modules/index.html) \- Back to modules overview

Today

Hi! I’m your AI assistant. How can I assist you today?

Just now

Powered by **FluentBot**


---
