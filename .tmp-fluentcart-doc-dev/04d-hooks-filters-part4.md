# FluentCart Developer Docs - Hooks (Filters) (Part 4/6)

Tous les filtres WordPress exposés par FluentCart, groupés par domaine (cart & checkout, orders & payments, customers & subscriptions, products & pricing, settings & configuration, integrations & advanced).

---

## Orders & Payments | FluentCart Developer Docs

**URL** : https://dev.fluentcart.com/hooks/filters/orders-and-payments

[Skip to content](https://dev.fluentcart.com/hooks/filters/orders-and-payments#VPContent)

# Orders & Payments [​](https://dev.fluentcart.com/hooks/filters/orders-and-payments\#orders-payments)

All filters related to [Order](https://dev.fluentcart.com/database/models/order.html) lifecycle, payment processing, gateway integrations, and taxes.

## Order Statuses [​](https://dev.fluentcart.com/hooks/filters/orders-and-payments\#order-statuses)

### ` order_statuses` [​](https://dev.fluentcart.com/hooks/filters/orders-and-payments\#order-statuses-1)

`fluent_cart/order_statuses` - Filter available order statuses

**When it runs:** Applied when retrieving the list of available order statuses throughout the admin and storefront.

**Parameters:**

- `$statuses` (array): Associative array of order statuses (key => translated label)
php

```
$statuses = [\
      'processing' => 'Processing',\
      'completed'  => 'Completed',\
      'on-hold'    => 'On Hold',\
      'canceled'   => 'Canceled',\
      'failed'     => 'Failed',\
];
```

- `$data` (array): Additional context data (empty array)

**Returns:**`array` - The modified order statuses array

**Source:**`app/Helpers/Status.php:159`

**Usage:**

php

```
add_filter('fluent_cart/order_statuses', function ($statuses, $data) {
    // Add a custom order status
    $statuses['awaiting_pickup'] = __('Awaiting Pickup', 'my-plugin');
    return $statuses;
}, 10, 2);
```

### ` order_statuses (legacy)` [​](https://dev.fluentcart.com/hooks/filters/orders-and-payments\#order-statuses-legacy)

`fluent-cart/order_statuses` - Filter order statuses (legacy hook name)

**When it runs:** Legacy location of the order statuses filter. Applied in the older Helper class. Prefer `fluent_cart/order_statuses` for new code.

**Parameters:**

- `$statuses` (array): Associative array of order statuses (key => translated label)
- `$data` (array): Additional context data (empty array)

**Returns:**`array` - The modified order statuses array

**Source:**`app/Helpers/Helper.php:140`

**Usage:**

php

```
add_filter('fluent-cart/order_statuses', function ($statuses, $data) {
    $statuses['custom'] = __('Custom Status', 'my-plugin');
    return $statuses;
}, 10, 2);
```

### ` editable_order_statuses` [​](https://dev.fluentcart.com/hooks/filters/orders-and-payments\#editable-order-statuses)

`fluent-cart/editable_order_statuses` - Filter manually settable order statuses

**When it runs:** Applied when building the list of order statuses an admin can manually set on an order. This controls the dropdown options in the order edit screen.

> **Note:** This hook uses a non-standard hyphenated prefix (`fluent-cart/`) rather than the standard `fluent_cart/` convention. This is a legacy naming that may be standardized in a future release.

**Parameters:**

- `$statuses` (array): Associative array of editable statuses (key => translated label)
php

```
$statuses = [\
      'on-hold'    => 'On Hold',\
      'processing' => 'Processing',\
      'completed'  => 'Completed',\
      'canceled'   => 'Canceled',\
];
```

- `$data` (array): Additional context data (empty array)

**Returns:**`array` - The modified editable order statuses array

**Source:**`app/Helpers/Helper.php:151`, `app/Helpers/Status.php:170,242`

**Usage:**

php

```
add_filter('fluent-cart/editable_order_statuses', function ($statuses, $data) {
    // Remove the ability to manually set "canceled"
    unset($statuses['canceled']);
    return $statuses;
}, 10, 2);
```

### ` payment_statuses` [​](https://dev.fluentcart.com/hooks/filters/orders-and-payments\#payment-statuses)

`fluent_cart/payment_statuses` - Filter payment statuses

**When it runs:** Applied when retrieving the list of available payment statuses used across the order and transaction system.

**Parameters:**

- `$statuses` (array): Associative array of payment statuses (key => translated label)
php

```
$statuses = [\
      'pending'            => 'Pending',\
      'paid'               => 'Paid',\
      'partially_paid'     => 'Partially Paid',\
      'failed'             => 'Failed',\
      'refunded'           => 'Refunded',\
      'partially_refunded' => 'Partially Refunded',\
      'authorized'         => 'Authorized',\
];
```

- `$data` (array): Additional context data (empty array)

**Returns:**`array` - The modified payment statuses array

**Source:**`app/Helpers/Status.php:183`

**Usage:**

php

```
add_filter('fluent_cart/payment_statuses', function ($statuses, $data) {
    $statuses['on_hold'] = __('On Hold', 'my-plugin');
    return $statuses;
}, 10, 2);
```

### ` transaction_statuses` [​](https://dev.fluentcart.com/hooks/filters/orders-and-payments\#transaction-statuses)

`fluent_cart/transaction_statuses` - Filter transaction statuses

**When it runs:** Applied when retrieving available transaction statuses for the primary transaction system.

**Parameters:**

- `$statuses` (array): Associative array of transaction statuses (key => translated label)
php

```
$statuses = [\
      'pending'    => 'Pending',\
      'succeeded'  => 'Succeeded',\
      'authorized' => 'Authorized',\
      'failed'     => 'Failed',\
      'refunded'   => 'Refunded',\
];
```

- `$data` (array): Additional context data (empty array)

**Returns:**`array` - The modified transaction statuses array

**Source:**`app/Helpers/Status.php:197`

**Usage:**

php

```
add_filter('fluent_cart/transaction_statuses', function ($statuses, $data) {
    $statuses['disputed'] = __('Disputed', 'my-plugin');
    return $statuses;
}, 10, 2);
```

### ` transaction_statuses (legacy)` [​](https://dev.fluentcart.com/hooks/filters/orders-and-payments\#transaction-statuses-legacy)

`fluent-cart/transaction_statuses` - Filter transaction statuses (legacy hook name)

**When it runs:** Legacy location of the transaction statuses filter. Applied in the older Helper class. Prefer `fluent_cart/transaction_statuses` for new code.

**Parameters:**

- `$statuses` (array): Associative array of transaction statuses (key => translated label)
- `$data` (array): Additional context data (empty array)

**Returns:**`array` - The modified transaction statuses array

**Source:**`app/Helpers/Helper.php:215`

**Usage:**

php

```
add_filter('fluent-cart/transaction_statuses', function ($statuses, $data) {
    return $statuses;
}, 10, 2);
```

### ` editable_transaction_statuses` [​](https://dev.fluentcart.com/hooks/filters/orders-and-payments\#editable-transaction-statuses)

`fluent-cart/editable_transaction_statuses` - Filter manually editable transaction statuses

**When it runs:** Applied when building the list of transaction statuses that an admin can manually set.

> **Note:** This hook uses a non-standard hyphenated prefix (`fluent-cart/`) rather than the standard `fluent_cart/` convention. This is a legacy naming that may be standardized in a future release.

**Parameters:**

- `$statuses` (array): Associative array of editable transaction statuses (key => translated label)
php

```
$statuses = [\
      'pending'    => 'Pending',\
      'succeeded'  => 'Succeeded',\
      'authorized' => 'Authorized',\
      'failed'     => 'Failed',\
      'refunded'   => 'Refunded',\
];
```

- `$data` (array): Additional context data (empty array)

**Returns:**`array` - The modified editable transaction statuses array

**Source:**`app/Helpers/Helper.php:233`, `app/Helpers/Status.php:214`

**Usage:**

php

```
add_filter('fluent-cart/editable_transaction_statuses', function ($statuses, $data) {
    unset($statuses['refunded']);
    return $statuses;
}, 10, 2);
```

### ` transaction_success_statuses` [​](https://dev.fluentcart.com/hooks/filters/orders-and-payments\#transaction-success-statuses)

`fluent_cart/transaction_success_statuses` - Filter which statuses count as successful transactions

**When it runs:** Applied when determining which transaction statuses should be considered "successful" for reporting and order completion logic.

**Parameters:**

- `$statuses` (array): Indexed array of status strings
php

```
$statuses = ['succeeded', 'authorized'];
```

- `$data` (array): Additional context data (empty array)

**Returns:**`array` - The modified success statuses array

**Source:**`app/Helpers/Status.php:331`

**Usage:**

php

```
add_filter('fluent_cart/transaction_success_statuses', function ($statuses, $data) {
    // Also count "captured" as a success status
    $statuses[] = 'captured';
    return $statuses;
}, 10, 2);
```

### ` shipping_statuses (legacy)` [​](https://dev.fluentcart.com/hooks/filters/orders-and-payments\#shipping-statuses-legacy)

`fluent-cart/shipping_statuses` - Filter shipping statuses (legacy hook name)

**When it runs:** Legacy location of the shipping statuses filter. Applied in the older Helper class. Prefer `fluent_cart/shipping_statuses` for new code.

**Parameters:**

- `$statuses` (array): Associative array of shipping statuses (key => translated label)
- `$data` (array): Additional context data (empty array)

**Returns:**`array` - The modified shipping statuses array

**Source:**`app/Helpers/Helper.php:170`

**Usage:**

php

```
add_filter('fluent-cart/shipping_statuses', function ($statuses, $data) {
    return $statuses;
}, 10, 2);
```

### ` shipping_statuses` [​](https://dev.fluentcart.com/hooks/filters/orders-and-payments\#shipping-statuses)

`fluent_cart/shipping_statuses` - Filter shipping statuses

**When it runs:** Applied when retrieving the list of available shipping statuses used for order fulfillment.

**Parameters:**

- `$statuses` (array): Associative array of shipping statuses (key => translated label)
php

```
$statuses = [\
      'unshipped'   => 'Unshipped',\
      'shipped'     => 'Shipped',\
      'delivered'   => 'Delivered',\
      'unshippable' => 'Unshippable',\
];
```

- `$data` (array): Additional context data (empty array)

**Returns:**`array` - The modified shipping statuses array

**Source:**`app/Helpers/Status.php:232`

**Usage:**

php

```
add_filter('fluent_cart/shipping_statuses', function ($statuses, $data) {
    $statuses['in_transit'] = __('In Transit', 'my-plugin');
    return $statuses;
}, 10, 2);
```

* * *

## Order Data & Lifecycle [​](https://dev.fluentcart.com/hooks/filters/orders-and-payments\#order-data-lifecycle)

### ` orders_list` [​](https://dev.fluentcart.com/hooks/filters/orders-and-payments\#orders-list)

`fluent_cart/orders_list` - Filter the admin orders list

**When it runs:** Applied after retrieving the paginated orders collection for the admin orders list view.

**Parameters:**

- `$orders` (LengthAwarePaginator): Paginated collection of orders

**Returns:**`LengthAwarePaginator` - The modified paginated orders collection

**Source:**`app/Http/Controllers/OrderController.php:58`

**Usage:**

php

```
add_filter('fluent_cart/orders_list', function ($orders) {
    // Add custom data to each order in the list
    foreach ($orders as $order) {
        $order->custom_badge = get_post_meta($order->id, '_custom_badge', true);
    }
    return $orders;
}, 10, 1);
```

### ` order/view` [​](https://dev.fluentcart.com/hooks/filters/orders-and-payments\#order-view)

`fluent_cart/order/view` - Filter single order view data

**When it runs:** Applied when preparing the data for a single order view in the admin panel.

**Parameters:**

- `$order` (array): The order data array containing all order details
- `$data` (array): Additional context data (empty array)

**Returns:**`array` - The modified order data

**Source:**`app/Http/Controllers/OrderController.php:580`

**Usage:**

php

```
add_filter('fluent_cart/order/view', function ($order, $data) {
    // Add custom data to the order view
    $order['custom_field'] = 'Custom Value';
    return $order;
}, 10, 2);
```

### ` widgets/single_order` [​](https://dev.fluentcart.com/hooks/filters/orders-and-payments\#widgets-single-order)

`fluent_cart/widgets/single_order` - Filter single order admin widgets

**When it runs:** Applied when loading the stats/widgets section on the single order admin view.

**Parameters:**

- `$widgets` (array): Array of widget data (default empty)
- `$order` ( [Order](https://dev.fluentcart.com/database/models/order.html)): The Order model instance

**Returns:**`array` - Array of widget definitions to display

**Source:**`app/Http/Controllers/OrderController.php:1009`

**Usage:**

php

```
add_filter('fluent_cart/widgets/single_order', function ($widgets, $order) {
    $widgets[] = [\
        'title' => __('Custom Widget', 'my-plugin'),\
        'value' => 'Some data for order #' . $order->id,\
    ];
    return $widgets;
}, 10, 2);
```

### ` order/is_subscription_allowed_in_manual_order` [​](https://dev.fluentcart.com/hooks/filters/orders-and-payments\#order-is-subscription-allowed-in-manual-order)

`fluent_cart/order/is_subscription_allowed_in_manual_order` - Allow subscriptions in manual orders

**When it runs:** Applied when creating a manual order that contains subscription items. By default, subscriptions in manual orders are not supported.

**Parameters:**

- `$allowed` (bool): Whether subscriptions are allowed (default `false`)
- `$context` (array): Context data
php

```
$context = [\
      'order_items' => [...] // Array of order item data\
];
```


**Returns:**`bool` - Whether to allow subscription items in manual orders

**Source:**`app/Http/Controllers/OrderController.php:78`

**Usage:**

php

```
add_filter('fluent_cart/order/is_subscription_allowed_in_manual_order', function ($allowed, $context) {
    // Enable subscriptions in manual orders
    return true;
}, 10, 2);
```

### ` order/type` [​](https://dev.fluentcart.com/hooks/filters/orders-and-payments\#order-type)

`fluent_cart/order/type` - Filter order type during manual creation

**When it runs:** Applied when determining the order type during manual order creation. The type is automatically set to `'subscription'` if subscription items are detected, otherwise `'payment'`.

**Parameters:**

- `$type` (string): The order type (`'payment'` or `'subscription'`)
- `$data` (array): Additional context data (empty array)

**Returns:**`string` - The order type string

**Source:**`app/Http/Controllers/OrderController.php:91`

**Usage:**

php

```
add_filter('fluent_cart/order/type', function ($type, $data) {
    return $type;
}, 10, 2);
```

### ` order/expected_license_count` [​](https://dev.fluentcart.com/hooks/filters/orders-and-payments\#order-expected-license-count)

`fluent_cart/order/expected_license_count` - Filter expected license count for an order

**When it runs:** Applied when checking how many licenses should exist for an order. Used to detect missing licenses that need to be regenerated.

**Parameters:**

- `$count` (int): Expected number of licenses (default `0`)
- `$context` (array): Context data
php

```
$context = [\
      'order_items' => [...] // Collection of order items\
];
```


**Returns:**`int` - The expected number of licenses

**Source:**`app/Http/Controllers/OrderController.php:215,585`

**Usage:**

php

```
add_filter('fluent_cart/order/expected_license_count', function ($count, $context) {
    foreach ($context['order_items'] as $item) {
        if ($item->requires_license) {
            $count += $item->quantity;
        }
    }
    return $count;
}, 10, 2);
```

### ` create_receipt_number_on_order_create` [​](https://dev.fluentcart.com/hooks/filters/orders-and-payments\#create-receipt-number-on-order-create)

`fluent_cart/create_receipt_number_on_order_create` - Force receipt number generation on order creation

**When it runs:** Applied during the order `creating` model event. By default, receipt numbers are only generated when the payment status is `'paid'`. Return `true` to always generate a receipt number.

**Parameters:**

- `$force` (bool): Whether to force receipt number creation (default `false`)

**Returns:**`bool` - Whether to generate a receipt number regardless of payment status

**Source:**`app/Models/Order.php:52`

**Usage:**

php

```
add_filter('fluent_cart/create_receipt_number_on_order_create', function ($force) {
    // Always create a receipt number when an order is created
    return true;
}, 10, 1);
```

### ` single_order_downloads` [​](https://dev.fluentcart.com/hooks/filters/orders-and-payments\#single-order-downloads)

`fluent_cart/single_order_downloads` - Filter order downloads data

**When it runs:** Applied when preparing the downloadable files for a specific order, allowing you to add, remove, or modify download data.

**Parameters:**

- `$downloadData` (array): Array of download groups
php

```
$downloadData = [\
      [\
          'title'           => 'Product Name - Variation Title',\
          'product_id'      => 123,\
          'variation_id'    => 456,\
          'additional_html' => '',\
          'downloads'       => [\
              ['id' => 1, 'name' => 'File Name', 'url' => '...']\
          ]\
      ]\
];
```

- `$context` (array): Context data
php

```
$context = [\
      'order' => Order,  // The Order model instance\
      'scope' => 'admin' // 'admin' or 'customer'\
];
```


**Returns:**`array` - The modified download data array

**Source:**`app/Models/Order.php:657`

**Usage:**

php

```
add_filter('fluent_cart/single_order_downloads', function ($downloadData, $context) {
    // Add a bonus download for completed orders
    if ($context['order']->status === 'completed') {
        $downloadData[] = [\
            'title'     => 'Bonus Content',\
            'downloads' => [\
                ['name' => 'Bonus File', 'url' => 'https://example.com/bonus.pdf']\
            ]\
        ];
    }
    return $downloadData;
}, 10, 2);
```

### ` order_can_be_deleted` [​](https://dev.fluentcart.com/hooks/filters/orders-and-payments\#order-can-be-deleted)

`fluent_cart/order_can_be_deleted` - Filter whether an order can be deleted

**When it runs:** Applied when checking if an order is eligible for deletion. By default, orders with active subscriptions cannot be deleted.

**Parameters:**

- `$canBeDeleted` (true\|WP\_Error): `true` if deletable, or a `WP_Error` with the reason
- `$context` (array): Context data
php

```
$context = [\
      'order' => Order // The Order model instance\
];
```


**Returns:**`true|WP_Error` - `true` to allow deletion, or `WP_Error` to block it

**Source:**`app/Models/Order.php:812`

**Usage:**

php

```
add_filter('fluent_cart/order_can_be_deleted', function ($canBeDeleted, $context) {
    $order = $context['order'];
    // Prevent deletion of orders less than 30 days old
    if (strtotime($order->created_at) > strtotime('-30 days')) {
        return new \WP_Error('too_recent', __('Orders less than 30 days old cannot be deleted.', 'my-plugin'));
    }
    return $canBeDeleted;
}, 10, 2);
```

### ` min_receipt_number` [​](https://dev.fluentcart.com/hooks/filters/orders-and-payments\#min-receipt-number)

`fluent_cart/min_receipt_number` - Filter the minimum receipt number

**When it runs:** Applied when calculating the next receipt number. If the computed next number is below this minimum, it will be bumped up.

**Parameters:**

- `$min` (int): The minimum receipt number from store settings (default `1`)

**Returns:**`int` - The minimum receipt number to enforce

**Source:**`app/Services/OrderService.php:572`

**Usage:**

php

```
add_filter('fluent_cart/min_receipt_number', function ($min) {
    // Start receipt numbers from 1000
    return 1000;
}, 10, 1);
```

### ` invoice_prefix` [​](https://dev.fluentcart.com/hooks/filters/orders-and-payments\#invoice-prefix)

`fluent_cart/invoice_prefix` - Filter the invoice number prefix

**When it runs:** Applied when generating the invoice number string for new orders. The invoice number is formed as `prefix + receipt_number`.

**Parameters:**

- `$prefix` (string): The invoice prefix from store settings (default `'INV-'`)

**Returns:**`string` - The modified invoice prefix

**Source:**`app/Services/OrderService.php:584`

**Usage:**

php

```
add_filter('fluent_cart/invoice_prefix', function ($prefix) {
    // Use a year-based prefix
    return 'INV-' . date('Y') . '-';
}, 10, 1);
```

### ` order_refund_manually` [​](https://dev.fluentcart.com/hooks/filters/orders-and-payments\#order-refund-manually)

`fluent_cart/order_refund_manually` - Intercept manual refund processing

**When it runs:** Applied during the refund process before the payment gateway refund method is called. Allows you to handle refunds through a custom mechanism instead of the gateway.

**Parameters:**

- `$manualRefund` (array): Manual refund status
php

```
$manualRefund = [\
      'status' => 'no',    // 'yes' to skip gateway refund\
      'source' => ''       // Identifier for the manual refund source\
];
```

- `$context` (array): Refund context data
php

```
$context = [\
      'refund_amount' => 5000,           // Amount in cents\
      'transaction'   => Transaction,     // OrderTransaction model\
      'order'         => Order,           // Order model\
      'args'          => ['reason' => ''] // Additional refund arguments\
];
```


**Returns:**`array` - Array with `'status'` key set to `'yes'` to skip the gateway refund

**Source:**`app/Services/Payments/Refund.php:65`

**Usage:**

php

```
add_filter('fluent_cart/order_refund_manually', function ($manualRefund, $context) {
    // Handle refund via a custom service
    $result = my_custom_refund($context['transaction'], $context['refund_amount']);
    if ($result) {
        return ['status' => 'yes', 'source' => 'my_custom_service'];
    }
    return $manualRefund;
}, 10, 2);
```

### ` order_status/auto_complete_digital_order` [​](https://dev.fluentcart.com/hooks/filters/orders-and-payments\#order-status-auto-complete-digital-order)

`fluent_cart/order_status/auto_complete_digital_order` - Control auto-completion of digital orders

**When it runs:** Applied during payment status reconciliation. When a digital (non-physical) order is paid, it is automatically marked as completed. Return `false` to prevent this behavior.

**Parameters:**

- `$autoComplete` (bool): Whether to auto-complete the order (default `true`)
- `$context` (array): Context data
php

```
$context = [\
      'order' => Order // The Order model instance\
];
```


**Returns:**`bool` - Whether to automatically complete the digital order

**Source:**`app/Helpers/StatusHelper.php:193`

**Usage:**

php

```
add_filter('fluent_cart/order_status/auto_complete_digital_order', function ($autoComplete, $context) {
    // Require manual review for high-value digital orders
    if ($context['order']->total > 50000) { // > $500
        return false;
    }
    return $autoComplete;
}, 10, 2);
```

### ` customer/order_data` [​](https://dev.fluentcart.com/hooks/filters/orders-and-payments\#customer-order-data)

`fluent_cart/customer/order_data` - Filter customer portal order data

**When it runs:** Applied when preparing order data for display in the customer-facing order details page.

**Parameters:**

- `$formattedOrderData` (array): The formatted order data array
- `$context` (array): Context data
php

```
$context = [\
      'order'    => Order,    // The Order model instance\
      'customer' => Customer  // The Customer model instance\
];
```


**Returns:**`array` - The modified formatted order data

**Source:**`app/Http/Controllers/FrontendControllers/CustomerOrderController.php:285`

**Usage:**

php

```
add_filter('fluent_cart/customer/order_data', function ($formattedOrderData, $context) {
    // Add custom data visible to customers
    $formattedOrderData['estimated_delivery'] = get_post_meta(
        $context['order']->id, '_estimated_delivery', true
    );
    return $formattedOrderData;
}, 10, 2);
```

### ` customer/order_details_section_parts` [​](https://dev.fluentcart.com/hooks/filters/orders-and-payments\#customer-order-details-section-parts)

`fluent_cart/customer/order_details_section_parts` - Filter customer order detail sections

**When it runs:** Applied when building the customer-facing order details page. Allows you to inject custom HTML content into predefined section slots.

**Parameters:**

- `$sections` (array): HTML content for each section slot
php

```
$sections = [\
      'before_summary'      => '',\
      'after_summary'       => '',\
      'after_licenses'      => '',\
      'after_subscriptions' => '',\
      'after_downloads'     => '',\
      'after_transactions'  => '',\
      'end_of_order'        => '',\
];
```

- `$context` (array): Context data
php

```
$context = [\
      'order'         => Order, // The Order model instance\
      'formattedData' => [...]  // The formatted order data array\
];
```


**Returns:**`array` - The modified sections array with HTML content

**Source:**`app/Http/Controllers/FrontendControllers/CustomerOrderController.php:292`

**Usage:**

php

```
add_filter('fluent_cart/customer/order_details_section_parts', function ($sections, $context) {
    $sections['after_summary'] = '<div class="custom-notice">Thank you for your order!</div>';
    return $sections;
}, 10, 2);
```

* * *

## Payment Processing [​](https://dev.fluentcart.com/hooks/filters/orders-and-payments\#payment-processing)

### ` ipn_url_{$slug}` [​](https://dev.fluentcart.com/hooks/filters/orders-and-payments\#ipn-url-slug)

`fluent_cart_ipn_url_{$slug}` - Filter IPN/webhook listener URL for a payment gateway

**When it runs:** Applied when generating the IPN (Instant Payment Notification) or webhook listener URL for a specific payment method. The `{$slug}` is the gateway slug (e.g., `stripe`, `paypal`).

**Parameters:**

- `$urlData` (array): Array containing the listener URL
php

```
$urlData = [\
      'listener_url' => 'https://yoursite.com/?fct_payment_listener=1&method=stripe'\
];
```


**Returns:**`array` - The modified URL data array

**Source:**`app/Services/Payments/PaymentHelper.php:24`

**Usage:**

php

```
add_filter('fluent_cart_ipn_url_stripe', function ($urlData) {
    // Use a custom endpoint for Stripe webhooks
    $urlData['listener_url'] = home_url('/custom-stripe-webhook/');
    return $urlData;
}, 10, 1);
```

### ` payment/success_url` [​](https://dev.fluentcart.com/hooks/filters/orders-and-payments\#payment-success-url)

`fluentcart/payment/success_url` - Filter the payment success redirect URL

**When it runs:** Applied when generating the URL the customer is redirected to after a successful payment.

> **Note:** This hook uses a non-standard prefix (`fluentcart/`) rather than the standard `fluent_cart/` convention. This is a legacy naming that may be standardized in a future release.

**Parameters:**

- `$url` (string): The success redirect URL (receipt page with query args)
- `$context` (array): Context data
php

```
$context = [\
      'transaction_hash' => 'abc123...',  // Transaction UUID\
      'args'             => [],           // Additional arguments\
      'payment_method'   => 'stripe'      // Gateway slug\
];
```


**Returns:**`string` - The modified success URL

**Source:**`app/Services/Payments/PaymentHelper.php:46`

**Usage:**

php

```
add_filter('fluentcart/payment/success_url', function ($url, $context) {
    // Redirect to a custom thank-you page
    return add_query_arg('trx_hash', $context['transaction_hash'], home_url('/thank-you/'));
}, 10, 2);
```

### ` default_payment_method_for_zero_payment` [​](https://dev.fluentcart.com/hooks/filters/orders-and-payments\#default-payment-method-for-zero-payment)

`fluent_cart/default_payment_method_for_zero_payment` - Filter the default payment method for zero-total orders

**When it runs:** Applied during checkout validation when the order total (including recurring) is zero. Determines which payment method handles the $0 transaction.

**Parameters:**

- `$method` (string): Payment method slug (default `'offline_payment'`)
- `$data` (array): Additional context data (empty array)

**Returns:**`string` - The payment method slug to use for zero-total orders

**Source:**`app/Services/Payments/PaymentHelper.php:70`

**Usage:**

php

```
add_filter('fluent_cart/default_payment_method_for_zero_payment', function ($method, $data) {
    // Use Stripe for free trials that have recurring charges
    return 'stripe';
}, 10, 2);
```

### ` get_payment_connect_info_{$method}` [​](https://dev.fluentcart.com/hooks/filters/orders-and-payments\#get-payment-connect-info-method)

`fluent_cart/get_payment_connect_info_{$method}` - Filter payment method connection info

**When it runs:** Applied when retrieving connection/setup information for a specific payment method. The `{$method}` is the sanitized gateway slug. Used by gateways that require an OAuth connection flow.

**Parameters:**

- `$info` (array): Connection info array (default empty)
- `$data` (array): Additional context data (empty array)

**Returns:**`array` - The payment method connection information

**Source:**`api/PaymentMethods.php:105`

**Usage:**

php

```
add_filter('fluent_cart/get_payment_connect_info_stripe', function ($info, $data) {
    $info['connected'] = true;
    $info['account_id'] = 'acct_xxx';
    return $info;
}, 10, 2);
```

### ` transaction/url_{$payment_method}` [​](https://dev.fluentcart.com/hooks/filters/orders-and-payments\#transaction-url-payment-method)

`fluent_cart/transaction/url_{$payment_method}` - Filter the vendor dashboard URL for a transaction

**When it runs:** Applied when generating the URL attribute of an [`OrderTransaction`](https://dev.fluentcart.com/database/models/order-transaction.html) model. The `{$payment_method}` is the gateway slug. This URL typically links to the transaction in the payment provider's dashboard.

**Parameters:**

- `$url` (string): The vendor URL (default empty string)
- `$context` (array): Context data
php

```
$context = [\
      'transaction'      => OrderTransaction, // The transaction model\
      'payment_mode'     => 'live',           // 'live' or 'test'\
      'vendor_charge_id' => 'ch_xxx',         // External charge ID\
      'transaction_type' => 'charge'          // Transaction type\
];
```


**Returns:**`string` - The URL to the transaction in the payment provider's dashboard

**Source:**`app/Models/OrderTransaction.php:111`

**Usage:**

php

```
add_filter('fluent_cart/transaction/url_stripe', function ($url, $context) {
    $chargeId = $context['vendor_charge_id'];
    $mode = $context['payment_mode'] === 'test' ? 'test/' : '';
    return "https://dashboard.stripe.com/{$mode}payments/{$chargeId}";
}, 10, 2);
```

### ` transaction/receipt_page_url` [​](https://dev.fluentcart.com/hooks/filters/orders-and-payments\#transaction-receipt-page-url)

`fluentcart/transaction/receipt_page_url` - Filter the transaction receipt page URL

**When it runs:** Applied when generating the public-facing receipt page URL for a transaction, typically used in email notifications and customer-facing links.

> **Note:** This hook uses a non-standard prefix (`fluentcart/`) rather than the standard `fluent_cart/` convention. This is a legacy naming that may be standardized in a future release.

**Parameters:**

- `$url` (string): The receipt page URL with `trx_hash` query parameter
- `$context` (array): Context data
php

```
$context = [\
      'transaction' => OrderTransaction, // The transaction model\
      'order'       => Order             // The parent order model\
];
```


**Returns:**`string` - The modified receipt page URL

**Source:**`app/Models/OrderTransaction.php:183`

**Usage:**

php

```
add_filter('fluentcart/transaction/receipt_page_url', function ($url, $context) {
    // Use a custom receipt page
    return add_query_arg('trx_hash', $context['transaction']->uuid, home_url('/my-receipt/'));
}, 10, 2);
```

* * *

## Stripe [​](https://dev.fluentcart.com/hooks/filters/orders-and-payments\#stripe)

### ` stripe_settings` [​](https://dev.fluentcart.com/hooks/filters/orders-and-payments\#stripe-settings)

`fluent_cart/stripe_settings` - Filter Stripe gateway settings

**When it runs:** Applied when loading Stripe gateway settings during initialization.

**Parameters:**

- `$settings` (array): The Stripe settings array including keys, modes, and configuration options

**Returns:**`array` - The modified Stripe settings

**Source:**`app/Modules/PaymentMethods/StripeGateway/StripeSettingsBase.php:38`

**Usage:**

php

```
add_filter('fluent_cart/stripe_settings', function ($settings) {
    // Force test mode in staging environments
    if (wp_get_environment_type() === 'staging') {
        $settings['payment_mode'] = 'test';
    }
    return $settings;
}, 10, 1);
```

### ` payments/stripe_metadata_subscription` [​](https://dev.fluentcart.com/hooks/filters/orders-and-payments\#payments-stripe-metadata-subscription)

`fluent_cart/payments/stripe_metadata_subscription` - Filter Stripe subscription metadata

**When it runs:** Applied when creating a Stripe subscription, allowing you to add or modify metadata sent to Stripe's subscription object.

**Parameters:**

- `$metadata` (array): The metadata array for the Stripe subscription
php

```
$metadata = [\
      'fct_ref_id'        => 'order-uuid',\
      'email'             => 'customer@example.com',\
      'name'              => 'Customer Name',\
      'subscription_item' => 'Product Name',\
      'order_reference'   => 'fct_order_id_123',\
];
```

- `$context` (array): Context data
php

```
$context = [\
      'order'        => Order,        // Order model\
      'transaction'  => Transaction,  // OrderTransaction model\
      'subscription' => Subscription  // Subscription model\
];
```


**Returns:**`array` - The modified metadata array (max 50 keys per Stripe limits)

**Source:**`app/Modules/PaymentMethods/StripeGateway/Processor.php:90`

**Usage:**

php

```
add_filter('fluent_cart/payments/stripe_metadata_subscription', function ($metadata, $context) {
    $metadata['affiliate_id'] = get_user_meta($context['order']->customer->user_id, 'affiliate_id', true);
    return $metadata;
}, 10, 2);
```

### ` payments/stripe_metadata_onetime` [​](https://dev.fluentcart.com/hooks/filters/orders-and-payments\#payments-stripe-metadata-onetime)

`fluent_cart/payments/stripe_metadata_onetime` - Filter Stripe one-time payment metadata

**When it runs:** Applied when creating a Stripe payment intent for a one-time (non-subscription) payment.

**Parameters:**

- `$metadata` (array): The metadata array for the Stripe payment intent
php

```
$metadata = [\
      'fct_ref_id'      => 'order-uuid',\
      'Name'            => 'Customer Name',\
      'Email'           => 'customer@example.com',\
      'order_reference' => 'fct_order_id_123',\
];
```

- `$context` (array): Context data
php

```
$context = [\
      'order'       => Order,       // Order model\
      'transaction' => Transaction  // OrderTransaction model\
];
```


**Returns:**`array` - The modified metadata array (max 50 keys per Stripe limits)

**Source:**`app/Modules/PaymentMethods/StripeGateway/Processor.php:221`

**Usage:**

php

```
add_filter('fluent_cart/payments/stripe_metadata_onetime', function ($metadata, $context) {
    $metadata['campaign'] = 'spring_sale_2025';
    if (isset($context['order'])) {
        $metadata['customer_id'] = $context['order']->customer_id;
    }
    return $metadata;
}, 10, 2);
```

### ` payments/stripe_onetime_intent_args` [​](https://dev.fluentcart.com/hooks/filters/orders-and-payments\#payments-stripe-onetime-intent-args)

`fluent_cart/payments/stripe_onetime_intent_args` - Filter Stripe payment intent arguments

**When it runs:** Applied after building the full payment intent data array, just before creating the intent via the Stripe API. This is the last chance to modify intent parameters.

**Parameters:**

- `$intentData` (array): The payment intent arguments
php

```
$intentData = [\
      'amount'                    => 5000,        // In smallest currency unit\
      'currency'                  => 'usd',\
      'automatic_payment_methods' => ['enabled' => 'true'],\
      'metadata'                  => [...],\
      'customer'                  => 'cus_xxx',\
];
```

- `$context` (array): Context data
php

```
$context = [\
      'order'       => Order,       // Order model\
      'transaction' => Transaction  // OrderTransaction model\
];
```


**Returns:**`array` - The modified payment intent arguments

**Source:**`app/Modules/PaymentMethods/StripeGateway/Processor.php:257`

**Usage:**

php

```
add_filter('fluent_cart/payments/stripe_onetime_intent_args', function ($intentData, $context) {
    // Add a statement descriptor
    $intentData['statement_descriptor_suffix'] = 'Order ' . $context['order']->id;
    return $intentData;
}, 10, 2);
```

### ` payments/stripe_checkout_session_args` [​](https://dev.fluentcart.com/hooks/filters/orders-and-payments\#payments-stripe-checkout-session-args)

`fluent_cart/payments/stripe_checkout_session_args` - Filter Stripe Checkout session arguments (one-time)

**When it runs:** Applied when creating a Stripe Checkout session for one-time (non-subscription) hosted payments.

**Parameters:**

- `$sessionData` (array): The Checkout session arguments
php

```
$sessionData = [\
      'customer'            => 'cus_xxx',\
      'client_reference_id' => 'order-uuid',\
      'line_items'          => [...],\
      'mode'                => 'payment',\
      'success_url'         => '...',\
      'cancel_url'          => '...',\
      'metadata'            => [...],\
];
```

- `$context` (array): Context data
php

```
$context = [\
      'order'       => Order,       // Order model\
      'transaction' => Transaction  // OrderTransaction model\
];
```


**Returns:**`array` - The modified Checkout session arguments

**Source:**`app/Modules/PaymentMethods/StripeGateway/Processor.php:356`

**Usage:**

php

```
add_filter('fluent_cart/payments/stripe_checkout_session_args', function ($sessionData, $context) {
    // Enable promotion codes on the Checkout page
    $sessionData['allow_promotion_codes'] = true;
    return $sessionData;
}, 10, 2);
```

### ` payments/stripe_subscription_checkout_session_args` [​](https://dev.fluentcart.com/hooks/filters/orders-and-payments\#payments-stripe-subscription-checkout-session-args)

`fluent_cart/payments/stripe_subscription_checkout_session_args` - Filter Stripe Checkout session arguments (subscription)

**When it runs:** Applied when creating a Stripe Checkout session for subscription-based hosted payments.

**Parameters:**

- `$sessionData` (array): The Checkout session arguments
php

```
$sessionData = [\
      'customer'            => 'cus_xxx',\
      'client_reference_id' => 'order-uuid',\
      'line_items'          => [...],\
      'mode'                => 'subscription',\
      'success_url'         => '...',\
      'cancel_url'          => '...',\
      'subscription_data'   => ['metadata' => [...]],\
      'metadata'            => [...],\
];
```

- `$context` (array): Context data
php

```
$context = [\
      'order'        => Order,        // Order model\
      'transaction'  => Transaction,  // OrderTransaction model\
      'subscription' => Subscription  // Subscription model\
];
```


**Returns:**`array` - The modified Checkout session arguments

**Source:**`app/Modules/PaymentMethods/StripeGateway/Processor.php:509`

**Usage:**

php

```
add_filter('fluent_cart/payments/stripe_subscription_checkout_session_args', function ($sessionData, $context) {
    // Add tax ID collection
    $sessionData['tax_id_collection'] = ['enabled' => true];
    return $sessionData;
}, 10, 2);
```

### ` stripe_idempotency_key` [​](https://dev.fluentcart.com/hooks/filters/orders-and-payments\#stripe-idempotency-key)

`fluent_cart_stripe_idempotency_key` - Filter the Stripe idempotency key

**When it runs:** Applied when sending charge requests to the Stripe API. The idempotency key prevents duplicate charges from being created.

**Parameters:**

- `$key` (string): The generated idempotency key
- `$context` (array): Context data
php

```
$context = [\
      'request' => [...] // The Stripe API request body\
];
```


**Returns:**`string` - The modified idempotency key

**Source:**`app/Modules/PaymentMethods/StripeGateway/API/ApiRequest.php:115`

**Usage:**

php

```
add_filter('fluent_cart_stripe_idempotency_key', function ($key, $context) {
    // Use a custom idempotency key format
    return 'fct_' . md5($key . time());
}, 10, 2);
```

### ` stripe_request_body` [​](https://dev.fluentcart.com/hooks/filters/orders-and-payments\#stripe-request-body)

`fluent_cart_stripe_request_body` - Filter the Stripe API request body

**When it runs:** Applied just before every request is sent to the Stripe API. This is a low-level filter that affects all Stripe API calls.

**Parameters:**

- `$request` (array): The request body data
- `$context` (array): Context data
php

```
$context = [\
      'api' => 'charges' // The Stripe API endpoint being called\
];
```


**Returns:**`array` - The modified request body

**Source:**`app/Modules/PaymentMethods/StripeGateway/API/ApiRequest.php:126`

**Usage:**

php

```
add_filter('fluent_cart_stripe_request_body', function ($request, $context) {
    // Log all Stripe API requests
    error_log('Stripe API call to: ' . $context['api']);
    return $request;
}, 10, 2);
```

### ` form_disable_stripe_connect` [​](https://dev.fluentcart.com/hooks/filters/orders-and-payments\#form-disable-stripe-connect)

`fluent_cart_form_disable_stripe_connect` - Disable Stripe Connect provider option

**When it runs:** Applied when rendering the Stripe settings form. Return `true` to force the use of manual API keys instead of Stripe Connect.

**Parameters:**

- `$disable` (bool): Whether to disable Stripe Connect (default `false`)
- `$data` (array): Additional context data (empty array)

**Returns:**`bool` - `true` to disable Stripe Connect and force API keys mode

**Source:**`app/Modules/PaymentMethods/StripeGateway/Stripe.php:288`

**Usage:**

php

```
add_filter('fluent_cart_form_disable_stripe_connect', function ($disable, $data) {
    // Force manual API keys
    return true;
}, 10, 2);
```

### ` stripe_appearance` [​](https://dev.fluentcart.com/hooks/filters/orders-and-payments\#stripe-appearance)

`fluent_cart_stripe_appearance` - Filter Stripe Elements appearance configuration

**When it runs:** Applied when initializing Stripe Elements on the checkout page. Controls the visual theme and styling of the embedded payment form.

**Parameters:**

- `$appearance` (array): Stripe Elements appearance configuration
php

```
$appearance = [\
      'theme' => 'stripe' // 'stripe', 'night', 'flat', or custom\
];
```


**Returns:**`array` - The modified appearance configuration (follows [Stripe Appearance API](https://docs.stripe.com/elements/appearance-api))

**Source:**`app/Modules/PaymentMethods/StripeGateway/Stripe.php:427`

**Usage:**

php

```
add_filter('fluent_cart_stripe_appearance', function ($appearance) {
    return [\
        'theme'     => 'night',\
        'variables' => [\
            'colorPrimary'    => '#0570de',\
            'borderRadius'    => '8px',\
            'fontFamily'      => 'Inter, system-ui, sans-serif',\
        ],\
    ];
}, 10, 1);
```

### ` stripe/setup_intent_rate_limit_customer_daily` [​](https://dev.fluentcart.com/hooks/filters/orders-and-payments\#stripe-setup-intent-rate-limit-customer-daily)

`fluent_cart/stripe/setup_intent_rate_limit_customer_daily` - Filter the daily SetupIntent rate limit per customer

**When it runs:** Applied when checking and enforcing the rate limit for Stripe SetupIntent creation (used for subscription card updates). Prevents card testing fraud.

**Parameters:**

- `$limit` (int): Maximum number of SetupIntent attempts per customer per day (default `3`)
- `$customerId` (string): The Stripe customer ID

**Returns:**`int` - The modified daily rate limit

**Source:**`app/Modules/PaymentMethods/StripeGateway/SubscriptionsManager.php:85,101`

**Usage:**

php

```
add_filter('fluent_cart/stripe/setup_intent_rate_limit_customer_daily', function ($limit, $customerId) {
    // Allow more attempts for trusted customers
    return 5;
}, 10, 2);
```

### ` stripe/fallback_order_transaction` [​](https://dev.fluentcart.com/hooks/filters/orders-and-payments\#stripe-fallback-order-transaction)

`fluent_cart/stripe/fallback_order_transaction` - Provide a fallback transaction for Stripe webhook events

**When it runs:** Applied during Stripe webhook processing (`charge.refunded` or `charge.succeeded`) when no matching [`OrderTransaction`](https://dev.fluentcart.com/database/models/order-transaction.html) can be found by `vendor_charge_id`. Allows you to resolve the transaction through custom logic.

**Parameters:**

- `$transaction` ( [OrderTransaction](https://dev.fluentcart.com/database/models/order-transaction.html) \|null): The fallback transaction (default `null`)
- `$vendorDataObject` (object): The Stripe event data object containing charge details

**Returns:** [OrderTransaction](https://dev.fluentcart.com/database/models/order-transaction.html) \|null - An `OrderTransaction` instance or `null` if not found

**Source:**`app/Modules/PaymentMethods/StripeGateway/Webhook/Webhook.php:121`

**Usage:**

php

```
add_filter('fluent_cart/stripe/fallback_order_transaction', function ($transaction, $vendorDataObject) {
    // Look up transaction by metadata
    if (isset($vendorDataObject->metadata->fct_ref_id)) {
        $order = \FluentCart\App\Models\Order::where('uuid', $vendorDataObject->metadata->fct_ref_id)->first();
        if ($order) {
            return \FluentCart\App\Models\OrderTransaction::where('order_id', $order->id)
                ->where('transaction_type', 'charge')
                ->first();
        }
    }
    return $transaction;
}, 10, 2);
```

* * *

## PayPal [​](https://dev.fluentcart.com/hooks/filters/orders-and-payments\#paypal)

### ` paypal_plan_id` [​](https://dev.fluentcart.com/hooks/filters/orders-and-payments\#paypal-plan-id)

`fluent_cart/paypal_plan_id` - Filter the PayPal plan ID for subscriptions

**When it runs:** Applied when generating or resolving the PayPal billing plan ID for a subscription product variation. The plan ID is a computed string based on currency, variation, billing interval, and other parameters.

**Parameters:**

- `$planId` (string): The generated plan ID string
- `$context` (array): Context data
php

```
$context = [\
      'plan_data' => [...],       // Plan configuration data\
      'variation' => Variation,   // Product variation model\
      'product'   => Product      // Product model\
];
```


**Returns:**`string` - The modified PayPal plan ID

**Source:**`app/Modules/PaymentMethods/PayPalGateway/PayPalHelper.php:54`

**Usage:**

php

```
add_filter('fluent_cart/paypal_plan_id', function ($planId, $context) {
    // Use a custom plan ID format
    return 'custom_plan_' . $context['variation']->id;
}, 10, 2);
```

### ` payments/paypal_sdk_src` [​](https://dev.fluentcart.com/hooks/filters/orders-and-payments\#payments-paypal-sdk-src)

`fluent_cart/payments/paypal_sdk_src` - Filter the PayPal SDK JavaScript source URL

**When it runs:** Applied when generating the PayPal JavaScript SDK script URL for the checkout page.

**Parameters:**

- `$sdkSrc` (string): The PayPal SDK URL with query parameters (client-id, currency, intent, vault, etc.)
- `$data` (array): Additional context data (empty array)

**Returns:**`string` - The modified PayPal SDK URL

**Source:**`app/Modules/PaymentMethods/PayPalGateway/PayPal.php:518`

**Usage:**

php

```
add_filter('fluent_cart/payments/paypal_sdk_src', function ($sdkSrc, $data) {
    // Add locale parameter
    return add_query_arg('locale', 'en_US', $sdkSrc);
}, 10, 2);
```

### ` payments/paypal/disable_webhook_verification` [​](https://dev.fluentcart.com/hooks/filters/orders-and-payments\#payments-paypal-disable-webhook-verification)

`fluent_cart/payments/paypal/disable_webhook_verification` - Disable PayPal webhook signature verification

**When it runs:** Applied at the start of PayPal webhook verification. Return `'yes'` to skip signature verification entirely. Only use this for debugging or in environments where verification cannot work.

**Parameters:**

- `$disable` (string): Whether to disable verification (default `'no'`)
- `$data` (array): Additional context data (empty array)

**Returns:**`string` - `'yes'` to skip verification, `'no'` to verify normally

**Source:**`app/Modules/PaymentMethods/PayPalGateway/IPN.php:179`

**Usage:**

php

```
add_filter('fluent_cart/payments/paypal/disable_webhook_verification', function ($disable, $data) {
    // Disable verification in local development
    if (wp_get_environment_type() === 'local') {
        return 'yes';
    }
    return $disable;
}, 10, 2);
```

### ` payments/paypal/verify_webhook` [​](https://dev.fluentcart.com/hooks/filters/orders-and-payments\#payments-paypal-verify-webhook)

`fluent_cart/payments/paypal/verify_webhook` - Control PayPal webhook verification

**When it runs:** Applied before the actual PayPal webhook signature verification step in the main webhook processing flow. Return `false` to skip verification for specific webhook types or modes.

**Parameters:**

- `$verify` (bool): Whether to verify the webhook (default `true`)
- `$context` (array): Context data
php

```
$context = [\
      'data' => [...],         // The webhook payload\
      'mode' => 'live',        // 'live' or 'test'\
      'type' => 'PAYMENT.SALE.COMPLETED' // Webhook event type\
];
```


**Returns:**`bool` - Whether to proceed with webhook verification

**Source:**`app/Modules/PaymentMethods/PayPalGateway/IPN.php:302`

**Usage:**

php

```
add_filter('fluent_cart/payments/paypal/verify_webhook', function ($verify, $context) {
    // Skip verification for test mode
    if ($context['mode'] === 'test') {
        return false;
    }
    return $verify;
}, 10, 2);
```

* * *

## Tax [​](https://dev.fluentcart.com/hooks/filters/orders-and-payments\#tax)

### ` tax/country_tax_titles` [​](https://dev.fluentcart.com/hooks/filters/orders-and-payments\#tax-country-tax-titles)

`fluent_cart/tax/country_tax_titles` - Filter tax title labels per country

**When it runs:** Applied when retrieving the mapping of country codes to their tax identification field labels (e.g., VAT, GST, ABN). Used in checkout forms and tax settings.

**Parameters:**

- `$taxTitles` (array): Associative array of country code => tax label
php

```
$taxTitles = [\
      'AU' => 'ABN',\
      'NZ' => 'GST',\
      'IN' => 'GST',\
      'CA' => 'GST / HST / PST / QST',\
      'GB' => 'VAT',\
      'EU' => 'VAT',\
      'US' => 'EIN / Sales Tax',\
      // ... 30+ countries\
];
```


**Returns:**`array` - The modified country tax titles array

**Source:**`app/Modules/Tax/TaxModule.php:821`

**Usage:**

php

```
add_filter('fluent_cart/tax/country_tax_titles', function ($taxTitles) {
    // Add or override tax labels
    $taxTitles['KR'] = __('BRN / VAT', 'my-plugin'); // South Korea
    $taxTitles['US'] = __('Tax ID', 'my-plugin');     // Simplify US label
    return $taxTitles;
}, 10, 1);
```

* * *

## Mollie (Pro) [​](https://dev.fluentcart.com/hooks/filters/orders-and-payments\#mollie-pro)

### ` mollie_settings` [​](https://dev.fluentcart.com/hooks/filters/orders-and-payments\#mollie-settings)

`fluent_cart/mollie_settings`Pro - Filter Mollie gateway settings

**When it runs:** Applied when loading Mollie gateway settings during initialization.

**Parameters:**

- `$settings` (array): The Mollie settings array including API keys and configuration

**Returns:**`array` - The modified Mollie settings

**Source:**`fluent-cart-pro/app/Modules/PaymentMethods/MollieGateway/MollieSettingsBase.php:26`

**Usage:**

php

```
add_filter('fluent_cart/mollie_settings', function ($settings) {
    // Override settings for staging
    if (wp_get_environment_type() === 'staging') {
        $settings['payment_mode'] = 'test';
    }
    return $settings;
}, 10, 1);
```

### ` payments/mollie_payment_args` [​](https://dev.fluentcart.com/hooks/filters/orders-and-payments\#payments-mollie-payment-args)

`fluent_cart/payments/mollie_payment_args`Pro - Filter Mollie payment data

**When it runs:** Applied when building the payment data array before sending to the Mollie API for payment creation.

**Parameters:**

- `$paymentData` (array): The payment data for the Mollie API
- `$context` (array): Context data
php

```
$context = [\
      'order'       => Order,       // Order model\
      'transaction' => Transaction  // OrderTransaction model\
];
```


**Returns:**`array` - The modified payment data

**Source:**`fluent-cart-pro/app/Modules/PaymentMethods/MollieGateway/MollieProcessor.php:142`

**Usage:**

php

```
add_filter('fluent_cart/payments/mollie_payment_args', function ($paymentData, $context) {
    // Add a custom description
    $paymentData['description'] = 'Order #' . $context['order']->id . ' - My Store';
    return $paymentData;
}, 10, 2);
```

### ` mollie/pass_line_items_details` [​](https://dev.fluentcart.com/hooks/filters/orders-and-payments\#mollie-pass-line-items-details)

`fluent_cart/mollie/pass_line_items_details`Pro - Control whether line item details are passed to Mollie

**When it runs:** Applied before building the Mollie payment request. Return `true` to include individual line items in the Mollie order (useful for Klarna, iDEAL, etc.).

**Parameters:**

- `$passLineItems` (bool): Whether to include line items (default `false`)
- `$context` (array): Array containing `[$order, $transaction]`

**Returns:**`bool` - Whether to pass line item details to Mollie

**Source:**`fluent-cart-pro/app/Modules/PaymentMethods/MollieGateway/MollieProcessor.php:128`

**Usage:**

php

```
add_filter('fluent_cart/mollie/pass_line_items_details', function ($passLineItems, $context) {
    // Enable line items for Klarna support
    return true;
}, 10, 2);
```

### ` mollie/webhook_url` [​](https://dev.fluentcart.com/hooks/filters/orders-and-payments\#mollie-webhook-url)

`fluent_cart/mollie/webhook_url`Pro - Filter the Mollie webhook URL

**When it runs:** Applied when generating the webhook notification URL sent to Mollie during payment creation.

**Parameters:**

- `$webhookUrl` (string): The IPN/webhook listener URL

**Returns:**`string` - The modified webhook URL

**Source:**`fluent-cart-pro/app/Modules/PaymentMethods/MollieGateway/MollieProcessor.php:301`

**Usage:**

php

```
add_filter('fluent_cart/mollie/webhook_url', function ($webhookUrl) {
    // Use a tunnel URL for local development
    if (wp_get_environment_type() === 'local') {
        return 'https://my-tunnel.ngrok.io/?fct_payment_listener=1&method=mollie';
    }
    return $webhookUrl;
}, 10, 1);
```

### ` mollie/subscription_description` [​](https://dev.fluentcart.com/hooks/filters/orders-and-payments\#mollie-subscription-description)

`fluent_cart/mollie/subscription_description`Pro - Filter the Mollie subscription description

**When it runs:** Applied when creating a Mollie subscription, allowing you to customize the description shown on the customer's payment statement.

**Parameters:**

- `$description` (string): The generated subscription description
- `$context` (array): Context data
php

```
$context = [\
      'subscription_model' => Subscription, // Subscription model\
      'currency'           => 'EUR'         // Currency code\
];
```


**Returns:**`string` - The modified subscription description

**Source:**`fluent-cart-pro/app/Modules/PaymentMethods/MollieGateway/MollieHelper.php:209`

**Usage:**

php

```
add_filter('fluent_cart/mollie/subscription_description', function ($description, $context) {
    return 'MyStore - ' . $context['subscription_model']->item_name;
}, 10, 2);
```

* * *

## Paddle (Pro) [​](https://dev.fluentcart.com/hooks/filters/orders-and-payments\#paddle-pro)

### ` paddle_product_tax_category` [​](https://dev.fluentcart.com/hooks/filters/orders-and-payments\#paddle-product-tax-category)

`fluent_cart/paddle_product_tax_category`Pro - Filter Paddle product tax category

**When it runs:** Applied when determining the tax category for a product in Paddle. Paddle uses tax categories to apply the correct tax rates.

**Parameters:**

- `$taxCategory` (string): The tax category (default `'standard'`)

**Returns:**`string` - The Paddle tax category (e.g., `'standard'`, `'digital-goods'`, `'saas'`)

**Source:**`fluent-cart-pro/app/Modules/PaymentMethods/PaddleGateway/`

**Usage:**

php

```
add_filter('fluent_cart/paddle_product_tax_category', function ($taxCategory) {
    return 'digital-goods';
}, 10, 1);
```

### ` paddle_onetime_price_id` [​](https://dev.fluentcart.com/hooks/filters/orders-and-payments\#paddle-onetime-price-id)

`fluent_cart/paddle_onetime_price_id`Pro - Filter Paddle one-time price ID

**When it runs:** Applied when resolving the Paddle price ID for a one-time payment product.

**Parameters:**

- `$priceId` (string): The Paddle price ID

**Returns:**`string` - The modified Paddle price ID

**Source:**`fluent-cart-pro/app/Modules/PaymentMethods/PaddleGateway/`

**Usage:**

php

```
add_filter('fluent_cart/paddle_onetime_price_id', function ($priceId) {
    return $priceId;
}, 10, 1);
```

### ` paddle_recurring_price_id` [​](https://dev.fluentcart.com/hooks/filters/orders-and-payments\#paddle-recurring-price-id)

`fluent_cart/paddle_recurring_price_id`Pro - Filter Paddle recurring price ID

**When it runs:** Applied when resolving the Paddle price ID for a recurring subscription product.

**Parameters:**

- `$priceId` (string): The Paddle recurring price ID

**Returns:**`string` - The modified Paddle recurring price ID

**Source:**`fluent-cart-pro/app/Modules/PaymentMethods/PaddleGateway/`

**Usage:**

php

```
add_filter('fluent_cart/paddle_recurring_price_id', function ($priceId) {
    return $priceId;
}, 10, 1);
```

### ` paddle_discount_id` [​](https://dev.fluentcart.com/hooks/filters/orders-and-payments\#paddle-discount-id)

`fluent_cart/paddle_discount_id`Pro - Filter Paddle discount ID

**When it runs:** Applied when resolving the Paddle discount ID to apply during checkout.

**Parameters:**

- `$discountId` (string): The Paddle discount ID

**Returns:**`string` - The modified Paddle discount ID

**Source:**`fluent-cart-pro/app/Modules/PaymentMethods/PaddleGateway/`

**Usage:**

php

```
add_filter('fluent_cart/paddle_discount_id', function ($discountId) {
    return $discountId;
}, 10, 1);
```

### ` paddle_subscription_product_type` [​](https://dev.fluentcart.com/hooks/filters/orders-and-payments\#paddle-subscription-product-type)

`fluent_cart/paddle_subscription_product_type`Pro - Filter Paddle subscription product type

**When it runs:** Applied when determining the Paddle product type for subscription items.

**Parameters:**

- `$productType` (string): The Paddle product type

**Returns:**`string` - The modified Paddle product type

**Source:**`fluent-cart-pro/app/Modules/PaymentMethods/PaddleGateway/`

**Usage:**

php

```
add_filter('fluent_cart/paddle_subscription_product_type', function ($productType) {
    return $productType;
}, 10, 1);
```

### ` paddle_subscription_price_type` [​](https://dev.fluentcart.com/hooks/filters/orders-and-payments\#paddle-subscription-price-type)

`fluent_cart/paddle_subscription_price_type`Pro - Filter Paddle subscription price type

**When it runs:** Applied when determining the Paddle price type for subscription items.

**Parameters:**

- `$priceType` (string): The Paddle price type

**Returns:**`string` - The modified Paddle price type

**Source:**`fluent-cart-pro/app/Modules/PaymentMethods/PaddleGateway/`

**Usage:**

php

```
add_filter('fluent_cart/paddle_subscription_price_type', function ($priceType) {
    return $priceType;
}, 10, 1);
```

### ` paddle_signup_fee_price_type` [​](https://dev.fluentcart.com/hooks/filters/orders-and-payments\#paddle-signup-fee-price-type)

`fluent_cart/paddle_signup_fee_price_type`Pro - Filter Paddle signup fee price type

**When it runs:** Applied when determining the Paddle price type for subscription signup fees.

**Parameters:**

- `$priceType` (string): The Paddle signup fee price type

**Returns:**`string` - The modified Paddle signup fee price type

**Source:**`fluent-cart-pro/app/Modules/PaymentMethods/PaddleGateway/`

**Usage:**

php

```
add_filter('fluent_cart/paddle_signup_fee_price_type', function ($priceType) {
    return $priceType;
}, 10, 1);
```

### ` paddle_product_id` [​](https://dev.fluentcart.com/hooks/filters/orders-and-payments\#paddle-product-id)

`fluent_cart/paddle_product_id`Pro - Filter Paddle one-time product ID

**When it runs:** Applied when resolving the Paddle product ID for one-time payment items.

**Parameters:**

- `$productId` (string): The Paddle product ID

**Returns:**`string` - The modified Paddle product ID

**Source:**`fluent-cart-pro/app/Modules/PaymentMethods/PaddleGateway/`

**Usage:**

php

```
add_filter('fluent_cart/paddle_product_id', function ($productId) {
    return $productId;
}, 10, 1);
```

### ` paddle_onetime_product_type` [​](https://dev.fluentcart.com/hooks/filters/orders-and-payments\#paddle-onetime-product-type)

`fluent_cart/paddle_onetime_product_type`Pro - Filter Paddle one-time product type

**When it runs:** Applied when determining the Paddle product type for one-time payment items.

**Parameters:**

- `$productType` (string): The Paddle product type

**Returns:**`string` - The modified Paddle product type

**Source:**`fluent-cart-pro/app/Modules/PaymentMethods/PaddleGateway/`

**Usage:**

php

```
add_filter('fluent_cart/paddle_onetime_product_type', function ($productType) {
    return $productType;
}, 10, 1);
```

### ` paddle_onetime_price_type` [​](https://dev.fluentcart.com/hooks/filters/orders-and-payments\#paddle-onetime-price-type)

`fluent_cart/paddle_onetime_price_type`Pro - Filter Paddle one-time price type

**When it runs:** Applied when determining the Paddle price type for one-time payment items.

**Parameters:**

- `$priceType` (string): The Paddle price type

**Returns:**`string` - The modified Paddle price type

**Source:**`fluent-cart-pro/app/Modules/PaymentMethods/PaddleGateway/`

**Usage:**

php

```
add_filter('fluent_cart/paddle_onetime_price_type', function ($priceType) {
    return $priceType;
}, 10, 1);
```

### ` paddle_addon_product_type` [​](https://dev.fluentcart.com/hooks/filters/orders-and-payments\#paddle-addon-product-type)

`fluent_cart/paddle_addon_product_type`Pro - Filter Paddle add-on product type

**When it runs:** Applied when determining the Paddle product type for add-on items.

**Parameters:**

- `$productType` (string): The Paddle add-on product type

**Returns:**`string` - The modified Paddle add-on product type

**Source:**`fluent-cart-pro/app/Modules/PaymentMethods/PaddleGateway/`

**Usage:**

php

```
add_filter('fluent_cart/paddle_addon_product_type', function ($productType) {
    return $productType;
}, 10, 1);
```

### ` paddle_discount_mode` [​](https://dev.fluentcart.com/hooks/filters/orders-and-payments\#paddle-discount-mode)

`fluent_cart/paddle_discount_mode`Pro - Filter Paddle discount mode

**When it runs:** Applied when determining how discounts are applied in Paddle transactions.

**Parameters:**

- `$discountMode` (string): The discount mode

**Returns:**`string` - The modified discount mode

**Source:**`fluent-cart-pro/app/Modules/PaymentMethods/PaddleGateway/`

**Usage:**

php

```
add_filter('fluent_cart/paddle_discount_mode', function ($discountMode) {
    return $discountMode;
}, 10, 1);
```

* * *

## Authorize.net (Pro) [​](https://dev.fluentcart.com/hooks/filters/orders-and-payments\#authorize-net-pro)

### ` authorize_dot_net_supported_currencies` [​](https://dev.fluentcart.com/hooks/filters/orders-and-payments\#authorize-dot-net-supported-currencies)

`fluent_cart/authorize_dot_net_supported_currencies`Pro - Filter Authorize.net supported currencies

**When it runs:** Applied when checking which currencies are supported by the Authorize.net gateway.

**Parameters:**

- `$currencies` (array): Array of supported currency codes
php

```
$currencies = ['USD', 'CAD', 'GBP', 'EUR', ...];
```


**Returns:**`array` - The modified array of supported currency codes

**Source:**`fluent-cart-pro/app/Modules/PaymentMethods/AuthorizeDotNetGateway/`

**Usage:**

php

```
add_filter('fluent_cart/authorize_dot_net_supported_currencies', function ($currencies) {
    // Add additional supported currencies
    $currencies[] = 'AUD';
    $currencies[] = 'NZD';
    return $currencies;
}, 10, 1);
```

### ` should_send_email_notification` [​](https://dev.fluentcart.com/hooks/filters/orders-and-payments\#should-send-email-notification)

`fluent_cart/should_send_email_notification` - Control whether an automatic email notification should be sent

**When it runs:** This filter is applied before each automatic email notification is sent for an order event. It allows you to selectively block or allow specific email notifications, for example when using a Merchant of Record payment gateway (like Paddle) that handles its own transactional emails.

**Parameters:**

- `$should` (bool): Whether the email should be sent (default: `true`)
- `$args` (array): Context data about the notification
php

```
$args = [\
      'event'     => 'order_paid',          // The event triggering the email\
      'mail_name' => 'order_paid_customer',  // The specific notification identifier\
      'order'     => $order,                 // Order model instance\
];
```


**Available `mail_name` values:**

- `order_paid_customer` - Purchase receipt to customer
- `order_paid_admin` - New order alert to admin
- `order_refunded_customer` - Refund confirmation to customer
- `order_refunded_admin` - Refund alert to admin
- `subscription_renewed_customer` - Renewal receipt to customer
- `subscription_renewed_admin` - Renewal alert to admin
- `subscription_canceled_customer` - Cancellation notice to customer
- `subscription_canceled_admin` - Cancellation alert to admin
- `order_placed_customer` - Order confirmation to customer (offline payment)
- `order_placed_admin` - Order placed alert to admin (offline payment)

**Returns:**

- `$should` (bool): Whether the email notification should be sent

**Usage:**

php

```
// Block all customer-facing emails for a specific payment gateway
add_filter('fluent_cart/should_send_email_notification', function($should, $args) {
    $order = $args['order'];

    if ($order->payment_method !== 'my_gateway') {
        return $should;
    }

    // Only allow order confirmation and admin notifications
    $allowedEmails = [\
        'order_paid_customer',\
        'order_paid_admin',\
    ];

    return in_array($args['mail_name'], $allowedEmails, true);
}, 10, 2);
```

**Note:** This filter only affects automatic event-driven emails. Manual actions like generating invoices or printing receipts from the admin panel are not affected.

### ` paddle_allowed_email_notifications` [​](https://dev.fluentcart.com/hooks/filters/orders-and-payments\#paddle-allowed-email-notifications)

`fluent_cart/paddle_allowed_email_notifications` - Control which email notifications are allowed for Paddle orders

**When it runs:** This filter is applied when determining whether to send an automatic email notification for a Paddle order. Since Paddle is a Merchant of Record and handles its own payment receipts, refund confirmations, and subscription billing emails, FluentCart blocks most automatic emails for Paddle orders by default. Use this filter to customize which emails are still sent by FluentCart.

**Parameters:**

- `$allowedEmails` (array): List of notification identifiers that FluentCart is allowed to send for Paddle orders
php

```
// Default allowed emails
$allowedEmails = [\
      'order_paid_customer',  // Order confirmation to customer\
      'order_paid_admin',     // New order alert to admin\
];
```


**Returns:**

- `$allowedEmails` (array): The modified list of allowed notification identifiers

**Usage:**

php

```
// Allow shipping notifications for Paddle orders
add_filter('fluent_cart/paddle_allowed_email_notifications', function($allowedEmails) {
    $allowedEmails[] = 'shipping_status_changed_to_shipped_customer';
    $allowedEmails[] = 'shipping_status_changed_to_delivered_customer';
    return $allowedEmails;
});
```

**Available notification identifiers:**

- `order_paid_customer` - Purchase receipt / order confirmation to customer (allowed by default)
- `order_paid_admin` - New order alert to admin (allowed by default)
- `order_refunded_customer` - Refund confirmation to customer
- `order_refunded_admin` - Refund alert to admin
- `subscription_renewed_customer` - Renewal receipt to customer
- `subscription_renewed_admin` - Renewal alert to admin
- `subscription_canceled_customer` - Cancellation notice to customer
- `subscription_canceled_admin` - Cancellation alert to admin

**Note:** This filter is specific to Paddle orders. For general email notification control across all payment gateways, use the `fluent_cart/should_send_email_notification` filter instead.

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

