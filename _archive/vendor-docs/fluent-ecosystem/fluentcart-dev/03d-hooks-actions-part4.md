# FluentCart Developer Docs - Hooks (Actions) (Part 4/5)

Toutes les actions WordPress exposées par FluentCart, groupées par domaine (orders, subscriptions, cart & checkout, customers & users, products & coupons, licenses, admin & templates, payments & integrations).

---

## Payments & Integrations | FluentCart Developer Docs

**URL** : https://dev.fluentcart.com/hooks/actions/payments-and-integrations

[Skip to content](https://dev.fluentcart.com/hooks/actions/payments-and-integrations#VPContent)

# Payments & Integrations [​](https://dev.fluentcart.com/hooks/actions/payments-and-integrations\#payments-integrations)

All hooks related to payment processing, payment gateway webhooks, third-party integrations, file storage drivers, and development logging. Many of these hooks provide [Order](https://dev.fluentcart.com/database/models/order.html), [Customer](https://dev.fluentcart.com/database/models/customer.html), and [OrderTransaction](https://dev.fluentcart.com/database/models/order-transaction.html) model instances.

## Payment Events [​](https://dev.fluentcart.com/hooks/actions/payments-and-integrations\#payment-events)

### ` payment_{$paymentStatus}` [​](https://dev.fluentcart.com/hooks/actions/payments-and-integrations\#payment-paymentstatus)

`fluent_cart/payment_{$paymentStatus}` - Fires after order creation when a transaction succeeds

**When it runs:** This dynamic action fires during [Order](https://dev.fluentcart.com/database/models/order.html) finalization, after the transaction has been recorded and the payment status is determined. It only fires when the transaction status is one of the recognized success statuses (e.g. `paid`, `pending`). The `{$paymentStatus}` portion is replaced with the order's actual payment status.

**Parameters:**

- `$data` (array): [Order](https://dev.fluentcart.com/database/models/order.html), [Customer](https://dev.fluentcart.com/database/models/customer.html), and [OrderTransaction](https://dev.fluentcart.com/database/models/order-transaction.html) data
php

```
$data = [\
      'order'       => $order,       // Order model instance\
      'customer'    => $customer,    // Customer model (via $order->customer)\
      'transaction' => $transaction, // Transaction model (via $order->latest_transaction)\
];
```


**Source:**`api/Resource/OrderResource.php`

**Dynamic variants:**

- `fluent_cart/payment_paid` \-\- payment completed successfully
- `fluent_cart/payment_pending` \-\- payment is pending confirmation

**Usage:**

php

```
add_action('fluent_cart/payment_paid', function ($data) {
    $order = $data['order'];
    $customer = $data['customer'];

    // Grant access after successful payment
    update_user_meta($customer->user_id, 'has_premium_access', true);

    fluent_cart_add_log(
        'Payment Received',
        'Order #' . $order->id . ' paid successfully.',
        'success'
    );
}, 10, 1);
```

### ` payment_{$transactionType}_{$paymentStatus}` [​](https://dev.fluentcart.com/hooks/actions/payments-and-integrations\#payment-transactiontype-paymentstatus)

`fluent_cart/payment_{$transactionType}_{$paymentStatus}` - Fires after order creation with both transaction type and payment status

**When it runs:** This dynamic action fires immediately after `fluent_cart/payment_{$paymentStatus}` during [Order](https://dev.fluentcart.com/database/models/order.html) finalization. It provides more granular filtering by combining the transaction type (e.g. `one_time`, `subscription`) with the payment status (e.g. `paid`, `pending`).

**Parameters:**

- `$data` (array): Order, customer, and transaction data
php

```
$data = [\
      'order'       => $order,       // Order model instance\
      'customer'    => $customer,    // Customer model (via $order->customer)\
      'transaction' => $transaction, // Transaction model (via $order->latest_transaction)\
];
```


**Source:**`api/Resource/OrderResource.php`

**Dynamic variants:**

- `fluent_cart/payment_one_time_paid` \-\- one-time purchase paid
- `fluent_cart/payment_subscription_paid` \-\- subscription payment paid
- `fluent_cart/payment_one_time_pending` \-\- one-time purchase pending
- `fluent_cart/payment_subscription_pending` \-\- subscription payment pending

**Usage:**

php

```
add_action('fluent_cart/payment_subscription_paid', function ($data) {
    $order = $data['order'];
    $transaction = $data['transaction'];

    // Handle subscription-specific logic after payment
    fluent_cart_add_log(
        'Subscription Payment',
        'Subscription payment received for Order #' . $order->id,
        'success'
    );
}, 10, 1);
```

### ` after_payment_{$paymentStatus}` [​](https://dev.fluentcart.com/hooks/actions/payments-and-integrations\#after-payment-paymentstatus)

`fluent_cart/payments/after_payment_{$paymentStatus}` - Fires in abstract gateway after payment processing completes

**When it runs:** This dynamic action fires inside the abstract payment gateway base class after a payment has been processed, the [OrderTransaction](https://dev.fluentcart.com/database/models/order-transaction.html) recorded, and the [Order](https://dev.fluentcart.com/database/models/order.html) status updated. It runs after `changeOrderStatus()` and any automatic digital-product completion logic. The `{$paymentStatus}` is the resulting payment status (e.g. `paid`, `failed`).

**Parameters:**

- `$data` (array): The order that was just processed
php

```
$data = [\
      'order' => $order, // Order model instance with updated status\
];
```


**Source:**`app/Modules/PaymentMethods/Core/AbstractPaymentGateway.php`

**Usage:**

php

```
add_action('fluent_cart/payments/after_payment_paid', function ($data) {
    $order = $data['order'];

    // Trigger external fulfillment after any gateway marks payment as paid
    wp_remote_post('https://fulfillment.example.com/api/orders', [\
        'body' => wp_json_encode([\
            'order_id' => $order->id,\
            'total'    => $order->total_amount,\
        ]),\
    ]);
}, 10, 1);
```

### ` payment_success` [​](https://dev.fluentcart.com/hooks/actions/payments-and-integrations\#payment-success)

`fluent_cart/payment_success` - Fires when an Airwallex or Square payment succeeds

**When it runs:** This action fires inside the Airwallex and Square gateway handlers when a payment intent or payment object is confirmed as successful. The order status is updated to `processing` and payment status to `paid` before this hook runs.

**Parameters:**

- `$data` (array): The order and payment intent/payment data
php

```
$data = [\
      'order'          => $order,         // Order model with updated status\
      'payment_intent' => $paymentIntent, // Gateway-specific payment intent or payment object (array)\
];
```


**Source:**`app/Modules/PaymentMethods/AirwallexGateway/Airwallex.php`, `app/Modules/PaymentMethods/SquareGateway/Square.php`

**Usage:**

php

```
add_action('fluent_cart/payment_success', function ($data) {
    $order = $data['order'];
    $paymentIntent = $data['payment_intent'];

    // Log the gateway-specific payment reference
    fluent_cart_add_log(
        'Gateway Payment Success',
        'Payment intent ' . $paymentIntent['id'] . ' for Order #' . $order->id,
        'success'
    );
}, 10, 1);
```

### ` payment_failed` [​](https://dev.fluentcart.com/hooks/actions/payments-and-integrations\#payment-failed)

`fluent_cart/payment_failed` - Fires when an Airwallex payment fails

**When it runs:** This action fires inside the Airwallex gateway handler when a payment intent is determined to have failed. The order status and payment status are both set to `failed` before this hook runs.

**Parameters:**

- `$data` (array): The order and failed payment intent data
php

```
$data = [\
      'order'          => $order,         // Order model with failed status\
      'payment_intent' => $paymentIntent, // Airwallex payment intent object (array)\
];
```


**Source:**`app/Modules/PaymentMethods/AirwallexGateway/Airwallex.php`

**Usage:**

php

```
add_action('fluent_cart/payment_failed', function ($data) {
    $order = $data['order'];
    $paymentIntent = $data['payment_intent'];

    // Notify admin about failed payment
    wp_mail(
        get_option('admin_email'),
        'Payment Failed - Order #' . $order->id,
        'Airwallex payment intent ' . $paymentIntent['id'] . ' failed.'
    );
}, 10, 1);
```

* * *

## Payment Gateway Registration [​](https://dev.fluentcart.com/hooks/actions/payments-and-integrations\#payment-gateway-registration)

### ` register_payment_methods` [​](https://dev.fluentcart.com/hooks/actions/payments-and-integrations\#register-payment-methods)

`fluent_cart/register_payment_methods` - Register custom payment gateways

**When it runs:** This action fires during initialization after all built-in payment gateways (Stripe, PayPal, Razorpay, Paystack, COD, Square, Airwallex) have been registered. Use this hook to register your own custom payment gateway with the gateway manager.

**Parameters:**

- `$data` (array): Contains the gateway manager instance
php

```
$data = [\
      'gatewayManager' => $gateway, // GatewayManager instance for registering gateways\
];
```


**Source:**`app/Hooks/Handlers/GlobalPaymentHandler.php`

**Usage:**

php

```
add_action('fluent_cart/register_payment_methods', function ($data) {
    $gatewayManager = $data['gatewayManager'];

    // Register a custom payment gateway
    $gatewayManager->register('my_gateway', new MyCustomPaymentGateway());
}, 10, 1);
```

### ` after_render_payment_method_{$route}` [​](https://dev.fluentcart.com/hooks/actions/payments-and-integrations\#after-render-payment-method-route)

`fluent-cart/after_render_payment_method_{$route}` - Fires after a payment method UI renders on the checkout page

**When it runs:** This action fires after a payment method's frontend UI (logo or radio button) has been rendered on the checkout form. The `{$route}` is the gateway's route identifier. Note that this hook uses a **hyphenated** prefix (`fluent-cart/`) rather than the usual underscored prefix.

**Parameters:**

None.

**Source:**`app/Modules/PaymentMethods/Core/AbstractPaymentGateway.php`

**Dynamic variants:**

- `fluent-cart/after_render_payment_method_stripe`
- `fluent-cart/after_render_payment_method_paypal`
- `fluent-cart/after_render_payment_method_square`
- `fluent-cart/after_render_payment_method_airwallex`
- `fluent-cart/after_render_payment_method_offline_payment`
- `fluent-cart/after_render_payment_method_razorpay`
- `fluent-cart/after_render_payment_method_paystack`

**Usage:**

php

```
add_action('fluent-cart/after_render_payment_method_stripe', function () {
    // Add custom messaging below the Stripe payment option
    echo '<p class="payment-note">Secure payments powered by Stripe.</p>';
}, 10, 0);
```

* * *

## Stripe Webhooks [​](https://dev.fluentcart.com/hooks/actions/payments-and-integrations\#stripe-webhooks)

### ` stripe/webhook_{$eventType}` [​](https://dev.fluentcart.com/hooks/actions/payments-and-integrations\#stripe-webhook-eventtype)

`fluent_cart/payments/stripe/webhook_{$eventType}` - Fires for each Stripe webhook event

**When it runs:** This dynamic action fires during Stripe webhook (IPN) processing after the event has been verified and the associated [Order](https://dev.fluentcart.com/database/models/order.html) has been found. The `{$eventType}` is the Stripe event type with dots replaced by underscores (e.g. `invoice.payment_succeeded` becomes `invoice_payment_succeeded`). The webhook handler checks if any listener is registered via `has_action()` before dispatching.

**Parameters:**

- `$data` (array): The Stripe event object and associated order
php

```
$data = [\
      'event' => $event, // Stripe Event object (contains type, data, etc.)\
      'order' => $order, // Order model instance (may be WP_Error if not found)\
];
```


**Source:**`app/Modules/PaymentMethods/StripeGateway/Webhook/IPN.php`

**Dynamic variants (common Stripe events):**

- `fluent_cart/payments/stripe/webhook_invoice_payment_succeeded`
- `fluent_cart/payments/stripe/webhook_invoice_payment_failed`
- `fluent_cart/payments/stripe/webhook_charge_refunded`
- `fluent_cart/payments/stripe/webhook_customer_subscription_deleted`
- `fluent_cart/payments/stripe/webhook_customer_subscription_updated`
- `fluent_cart/payments/stripe/webhook_payment_intent_succeeded`
- `fluent_cart/payments/stripe/webhook_payment_intent_payment_failed`

**Usage:**

php

```
add_action('fluent_cart/payments/stripe/webhook_charge_refunded', function ($data) {
    $event = $data['event'];
    $order = $data['order'];

    if (is_wp_error($order)) {
        return;
    }

    $charge = $event->data->object;

    // Custom refund handling
    fluent_cart_add_log(
        'Stripe Refund Webhook',
        'Charge ' . $charge->id . ' refunded for Order #' . $order->id,
        'info'
    );
}, 10, 1);
```

* * *

## PayPal Webhooks [​](https://dev.fluentcart.com/hooks/actions/payments-and-integrations\#paypal-webhooks)

### ` paypal_webhook_received` [​](https://dev.fluentcart.com/hooks/actions/payments-and-integrations\#paypal-webhook-received)

`fluent_cart/paypal_webhook_received` - Fires when raw PayPal webhook data is received before processing

**When it runs:** This action fires early in PayPal webhook processing, after the webhook type has been validated against the list of supported events but before any event-specific handling occurs. Use this to log or inspect all incoming PayPal webhook payloads.

**Parameters:**

- `$data` (array): The parsed and raw webhook data
php

```
$data = [\
      'data' => $data,      // Parsed webhook payload (array)\
      'raw'  => $post_data, // Raw POST body string\
];
```


**Source:**`app/Modules/PaymentMethods/PayPalGateway/IPN.php`

**Usage:**

php

```
add_action('fluent_cart/paypal_webhook_received', function ($data) {
    // Log all incoming PayPal webhooks for debugging
    error_log('PayPal webhook received: ' . wp_json_encode($data['data']));
}, 10, 1);
```

### ` paypal/webhook_subscription_payment_received` [​](https://dev.fluentcart.com/hooks/actions/payments-and-integrations\#paypal-webhook-subscription-payment-received)

`fluent_cart/payments/paypal/webhook_subscription_payment_received` - Fires when a PayPal recurring subscription payment is received

**When it runs:** This action fires when a PayPal `PAYMENT.SALE.COMPLETED` webhook is received and the resource contains a `billing_agreement_id`, indicating it is a recurring subscription payment rather than a one-time purchase.

**Parameters:**

- `$data` (array): The charge resource and billing agreement ID
php

```
$data = [\
      'charge'                 => $resource,           // PayPal sale resource object (array)\
      'vendor_subscription_id' => $billingAgreementId, // PayPal billing agreement ID (string)\
];
```


**Source:**`app/Modules/PaymentMethods/PayPalGateway/IPN.php`

**Usage:**

php

```
add_action('fluent_cart/payments/paypal/webhook_subscription_payment_received', function ($data) {
    $charge = $data['charge'];
    $billingAgreementId = $data['vendor_subscription_id'];

    // Track recurring payment
    fluent_cart_add_log(
        'PayPal Recurring Payment',
        'Billing agreement ' . $billingAgreementId . ' payment received.',
        'success'
    );
}, 10, 1);
```

### ` paypal/webhook_payment_capture_completed` [​](https://dev.fluentcart.com/hooks/actions/payments-and-integrations\#paypal-webhook-payment-capture-completed)

`fluent_cart/payments/paypal/webhook_payment_capture_completed` - Fires when a PayPal one-time payment capture completes

**When it runs:** This action fires when a PayPal `PAYMENT.SALE.COMPLETED` webhook arrives without a billing agreement ID (one-time payment), or when a `PAYMENT.CAPTURE.COMPLETED` event is received. Both indicate a successful one-time payment capture.

**Parameters:**

- `$data` (array): The charge resource from PayPal
php

```
$data = [\
      'charge' => $resource, // PayPal capture/sale resource object (array)\
];
```


**Source:**`app/Modules/PaymentMethods/PayPalGateway/IPN.php`

**Usage:**

php

```
add_action('fluent_cart/payments/paypal/webhook_payment_capture_completed', function ($data) {
    $charge = $data['charge'];

    // Handle one-time payment capture confirmation
    fluent_cart_add_log(
        'PayPal Capture Completed',
        'Capture completed for resource: ' . wp_json_encode($charge),
        'success'
    );
}, 10, 1);
```

### ` paypal/webhook_payment_sale_refunded` [​](https://dev.fluentcart.com/hooks/actions/payments-and-integrations\#paypal-webhook-payment-sale-refunded)

`fluent_cart/payments/paypal/webhook_payment_sale_refunded` - Fires when a PayPal recurring sale is refunded

**When it runs:** This action fires when a PayPal `PAYMENT.SALE.REFUNDED` webhook is received, indicating that a refund has been issued for a recurring/subscription payment sale.

**Parameters:**

- `$data` (array): The refund resource from PayPal
php

```
$data = [\
      'refund' => $resource, // PayPal refund resource object (array)\
];
```


**Source:**`app/Modules/PaymentMethods/PayPalGateway/IPN.php`

**Usage:**

php

```
add_action('fluent_cart/payments/paypal/webhook_payment_sale_refunded', function ($data) {
    $refund = $data['refund'];

    // Handle recurring payment refund
    fluent_cart_add_log(
        'PayPal Sale Refund',
        'Recurring payment sale refunded: ' . wp_json_encode($refund),
        'info'
    );
}, 10, 1);
```

### ` paypal/webhook_payment_capture_refunded` [​](https://dev.fluentcart.com/hooks/actions/payments-and-integrations\#paypal-webhook-payment-capture-refunded)

`fluent_cart/payments/paypal/webhook_payment_capture_refunded` - Fires when a PayPal one-time payment capture is refunded

**When it runs:** This action fires when a PayPal `PAYMENT.CAPTURE.REFUNDED` webhook is received, indicating that a refund has been issued for a one-time payment capture.

**Parameters:**

- `$data` (array): The refund resource from PayPal
php

```
$data = [\
      'refund' => $resource, // PayPal refund resource object (array)\
];
```


**Source:**`app/Modules/PaymentMethods/PayPalGateway/IPN.php`

**Usage:**

php

```
add_action('fluent_cart/payments/paypal/webhook_payment_capture_refunded', function ($data) {
    $refund = $data['refund'];

    // Handle one-time payment refund
    fluent_cart_add_log(
        'PayPal Capture Refund',
        'One-time payment capture refunded: ' . wp_json_encode($refund),
        'info'
    );
}, 10, 1);
```

### ` paypal/webhook_{$eventType} (disputes)` [​](https://dev.fluentcart.com/hooks/actions/payments-and-integrations\#paypal-webhook-eventtype-disputes)

`fluent_cart/payments/paypal/webhook_{$eventType}` - Fires for PayPal customer dispute events

**When it runs:** This dynamic action fires when a PayPal dispute-related webhook is received. The `{$eventType}` is the PayPal event type converted to lowercase with dots replaced by underscores.

**Parameters:**

- `$data` (array): The dispute resource from PayPal
php

```
$data = [\
      'dispute' => $resource, // PayPal dispute resource object (array)\
];
```


**Source:**`app/Modules/PaymentMethods/PayPalGateway/IPN.php`

**Dynamic variants:**

- `fluent_cart/payments/paypal/webhook_customer_dispute_created`
- `fluent_cart/payments/paypal/webhook_customer_dispute_updated`
- `fluent_cart/payments/paypal/webhook_customer_dispute_resolved`

**Usage:**

php

```
add_action('fluent_cart/payments/paypal/webhook_customer_dispute_created', function ($data) {
    $dispute = $data['dispute'];

    // Alert admin about a new PayPal dispute
    wp_mail(
        get_option('admin_email'),
        'PayPal Dispute Created',
        'A customer has opened a dispute. Details: ' . wp_json_encode($dispute)
    );
}, 10, 1);
```

### ` paypal/webhook_{$eventType} (subscriptions)` [​](https://dev.fluentcart.com/hooks/actions/payments-and-integrations\#paypal-webhook-eventtype-subscriptions)

`fluent_cart/payments/paypal/webhook_{$eventType}` - Fires for PayPal billing subscription lifecycle events

**When it runs:** This dynamic action fires as a catch-all for PayPal webhook events that are not payments, refunds, or disputes. These are primarily billing subscription lifecycle events. The `{$eventType}` is the PayPal event type converted to lowercase with dots replaced by underscores.

**Parameters:**

- `$data` (array): The PayPal subscription resource
php

```
$data = [\
      'paypal_subscription' => $resource, // PayPal subscription resource object (array)\
];
```


**Source:**`app/Modules/PaymentMethods/PayPalGateway/IPN.php`

**Dynamic variants:**

- `fluent_cart/payments/paypal/webhook_billing_subscription_activated`
- `fluent_cart/payments/paypal/webhook_billing_subscription_created`
- `fluent_cart/payments/paypal/webhook_billing_subscription_cancelled`
- `fluent_cart/payments/paypal/webhook_billing_subscription_expired`
- `fluent_cart/payments/paypal/webhook_billing_subscription_suspended`
- `fluent_cart/payments/paypal/webhook_billing_subscription_re-activated`

**Usage:**

php

```
add_action('fluent_cart/payments/paypal/webhook_billing_subscription_cancelled', function ($data) {
    $subscription = $data['paypal_subscription'];

    // Handle PayPal subscription cancellation
    fluent_cart_add_log(
        'PayPal Subscription Cancelled',
        'PayPal subscription cancelled: ' . wp_json_encode($subscription),
        'warning'
    );
}, 10, 1);
```

* * *

## Mollie Webhooks Pro [​](https://dev.fluentcart.com/hooks/actions/payments-and-integrations\#mollie-webhooks)

### ` mollie/webhook_subscription_payment_{$status}` [​](https://dev.fluentcart.com/hooks/actions/payments-and-integrations\#mollie-webhook-subscription-payment-status)

`fluent_cart/payments/mollie/webhook_subscription_payment_{$status}`Pro - Fires for each Mollie subscription payment status change

**When it runs:** This dynamic action fires during Mollie webhook (IPN) processing when a subscription payment status is determined. The `{$status}` is replaced with the Mollie payment status (e.g. `paid`, `failed`, `expired`, `canceled`). Use this hook to react to specific subscription payment outcomes from Mollie.

**Parameters:**

- `$molliePayment` (object): The Mollie Payment object from the API
- `$order` ( [Order](https://dev.fluentcart.com/database/models/order.html)): The Order model instance associated with this payment

**Source:**`fluent-cart-pro/app/Modules/PaymentMethods/MollieGateway/Webhook/MollieIPN.php`

**Dynamic variants:**

- `fluent_cart/payments/mollie/webhook_subscription_payment_paid` \-\- subscription payment succeeded
- `fluent_cart/payments/mollie/webhook_subscription_payment_failed` \-\- subscription payment failed
- `fluent_cart/payments/mollie/webhook_subscription_payment_expired` \-\- subscription payment expired
- `fluent_cart/payments/mollie/webhook_subscription_payment_canceled` \-\- subscription payment canceled

**Usage:**

php

```
add_action('fluent_cart/payments/mollie/webhook_subscription_payment_paid', function ($molliePayment, $order) {
    // Handle successful Mollie subscription payment
    fluent_cart_add_log(
        'Mollie Subscription Payment',
        'Subscription payment received for Order #' . $order->id . ' (Mollie ID: ' . $molliePayment->id . ')',
        'success'
    );
}, 10, 2);
```

### ` mollie/webhook_payment_{$status}` [​](https://dev.fluentcart.com/hooks/actions/payments-and-integrations\#mollie-webhook-payment-status)

`fluent_cart/payments/mollie/webhook_payment_{$status}`Pro - Fires for each Mollie one-time payment status change

**When it runs:** This dynamic action fires during Mollie webhook processing when a one-time (non-subscription) payment status is determined. The `{$status}` is replaced with the Mollie payment status. Use this hook to react to specific one-time payment outcomes from Mollie.

**Parameters:**

- `$molliePayment` (object): The Mollie Payment object from the API
- `$order` ( [Order](https://dev.fluentcart.com/database/models/order.html)): The Order model instance associated with this payment

**Source:**`fluent-cart-pro/app/Modules/PaymentMethods/MollieGateway/Webhook/MollieIPN.php`

**Dynamic variants:**

- `fluent_cart/payments/mollie/webhook_payment_paid` \-\- one-time payment succeeded
- `fluent_cart/payments/mollie/webhook_payment_failed` \-\- one-time payment failed
- `fluent_cart/payments/mollie/webhook_payment_expired` \-\- one-time payment expired
- `fluent_cart/payments/mollie/webhook_payment_canceled` \-\- one-time payment canceled

**Usage:**

php

```
add_action('fluent_cart/payments/mollie/webhook_payment_paid', function ($molliePayment, $order) {
    // Handle successful Mollie one-time payment
    wp_remote_post('https://fulfillment.example.com/api/orders', [\
        'body' => wp_json_encode([\
            'order_id'   => $order->id,\
            'mollie_id'  => $molliePayment->id,\
            'amount'     => $molliePayment->amount->value,\
            'currency'   => $molliePayment->amount->currency,\
        ]),\
    ]);
}, 10, 2);
```

### ` payment_failed (Mollie)` [​](https://dev.fluentcart.com/hooks/actions/payments-and-integrations\#payment-failed-mollie)

`fluent_cart/payment_failed`Pro - Fires when a Mollie payment fails, is canceled, or expires

**When it runs:** This action fires inside the Mollie IPN handler when a payment is determined to have failed, been canceled, or expired. The order status and payment status are updated before this hook runs. Note that this is the same `fluent_cart/payment_failed` hook used by the base plugin for Airwallex; the Pro plugin adds Mollie as an additional source that fires it.

**Parameters:**

- `$data` (array): Payment failure data
php

```
$data = [\
      'order'              => $order,              // \FluentCart\App\Models\Order - with updated failed status\
      'transaction'        => $transactionModel,   // \FluentCart\App\Models\OrderTransaction\
      'old_payment_status' => $oldStatus,          // string - previous payment status\
      'new_payment_status' => Status::PAYMENT_FAILED, // string - new payment status\
      'reason'             => $reason,             // string - 'failed', 'canceled', or 'expired'\
];
```


**Source:**`fluent-cart-pro/app/Modules/PaymentMethods/MollieGateway/Webhook/MollieIPN.php`

**Usage:**

php

```
add_action('fluent_cart/payment_failed', function ($data) {
    $order       = $data['order'];
    $transaction = $data['transaction'];
    $oldStatus   = $data['old_payment_status'];
    $newStatus   = $data['new_payment_status'];
    $reason      = $data['reason'];

    // Notify admin about failed Mollie payment
    if ($order->payment_method !== 'mollie') {
        return; // Only handle Mollie failures in this callback
    }

    wp_mail(
        get_option('admin_email'),
        'Mollie Payment Failed - Order #' . $order->id,
        sprintf(
            "Payment for Order #%d has %s.\nPrevious status: %s\nNew status: %s\nTransaction ID: %s",
            $order->id,
            $reason,
            $oldStatus,
            $newStatus,
            $transaction->id
        )
    );
}, 10, 1);
```

* * *

## Paddle Webhooks Pro [​](https://dev.fluentcart.com/hooks/actions/payments-and-integrations\#paddle-webhooks)

### ` paddle_webhook_received` [​](https://dev.fluentcart.com/hooks/actions/payments-and-integrations\#paddle-webhook-received)

`fluent_cart/paddle_webhook_received`Pro - Fires when raw Paddle webhook data is received before processing

**When it runs:** This action fires early in Paddle webhook processing, after the event type has been extracted from the payload but before any event-specific handling occurs. Use this to log or inspect all incoming Paddle webhook payloads for debugging purposes.

**Parameters:**

- `$eventType` (string): The Paddle event type (e.g. `transaction.paid`, `subscription.created`)
- `$data` (array): The parsed webhook payload
- `$raw` (string): The raw POST body string
- `$order` ( [Order](https://dev.fluentcart.com/database/models/order.html) \|null): The associated Order model instance, or null if not yet resolved

**Source:**`fluent-cart-pro/app/Modules/PaymentMethods/PaddleGateway/Webhook/IPN.php`

**Usage:**

php

```
add_action('fluent_cart/paddle_webhook_received', function ($eventType, $data, $raw, $order) {
    // Log all incoming Paddle webhooks for debugging
    fluent_cart_add_log(
        'Paddle Webhook Received',
        sprintf(
            'Event: %s | Order: %s | Payload size: %d bytes',
            $eventType,
            $order ? '#' . $order->id : 'N/A',
            strlen($raw)
        ),
        'info'
    );
}, 10, 4);
```

### ` paddle/webhook_{$eventType}` [​](https://dev.fluentcart.com/hooks/actions/payments-and-integrations\#paddle-webhook-eventtype)

`fluent_cart/payments/paddle/webhook_{$eventType}`Pro - Fires for each Paddle webhook event

**When it runs:** This dynamic action fires during Paddle webhook (IPN) processing after the event has been received and the associated order has been resolved (if applicable). The `{$eventType}` is the Paddle event type with dots replaced by underscores (e.g. `transaction.paid` becomes `transaction_paid`). The webhook handler validates incoming events against a list of accepted event types before dispatching.

**Parameters:**

- `$eventType` (string): The Paddle event type with dots replaced by underscores
- `$data` (array): The parsed webhook payload
- `$raw` (string): The raw POST body string
- `$order` ( [Order](https://dev.fluentcart.com/database/models/order.html) \|null): The associated Order model instance, or null if not resolved

**Source:**`fluent-cart-pro/app/Modules/PaymentMethods/PaddleGateway/Webhook/IPN.php`

**Accepted events (dynamic variants):**

- `fluent_cart/payments/paddle/webhook_transaction_paid` \-\- transaction payment succeeded
- `fluent_cart/payments/paddle/webhook_transaction_completed` \-\- transaction fully completed
- `fluent_cart/payments/paddle/webhook_transaction_payment_failed` \-\- transaction payment failed
- `fluent_cart/payments/paddle/webhook_transaction_refunded` \-\- transaction refunded
- `fluent_cart/payments/paddle/webhook_adjustment_created` \-\- adjustment (refund/credit) created
- `fluent_cart/payments/paddle/webhook_adjustment_updated` \-\- adjustment updated
- `fluent_cart/payments/paddle/webhook_subscription_created` \-\- subscription created
- `fluent_cart/payments/paddle/webhook_subscription_activated` \-\- subscription activated
- `fluent_cart/payments/paddle/webhook_subscription_updated` \-\- subscription updated
- `fluent_cart/payments/paddle/webhook_subscription_canceled` \-\- subscription canceled
- `fluent_cart/payments/paddle/webhook_subscription_paused` \-\- subscription paused
- `fluent_cart/payments/paddle/webhook_subscription_resumed` \-\- subscription resumed
- `fluent_cart/payments/paddle/webhook_subscription_past_due` \-\- subscription past due

**Usage:**

php

```
add_action('fluent_cart/payments/paddle/webhook_transaction_paid', function ($eventType, $data, $raw, $order) {
    if (!$order) {
        return;
    }

    // Handle successful Paddle transaction payment
    fluent_cart_add_log(
        'Paddle Transaction Paid',
        'Paddle payment completed for Order #' . $order->id,
        'success'
    );
}, 10, 4);

add_action('fluent_cart/payments/paddle/webhook_subscription_canceled', function ($eventType, $data, $raw, $order) {
    if (!$order) {
        return;
    }

    // Handle Paddle subscription cancellation
    wp_mail(
        get_option('admin_email'),
        'Paddle Subscription Canceled - Order #' . $order->id,
        'A Paddle subscription has been canceled. Event data: ' . wp_json_encode($data)
    );
}, 10, 4);

add_action('fluent_cart/payments/paddle/webhook_transaction_refunded', function ($eventType, $data, $raw, $order) {
    if (!$order) {
        return;
    }

    // Track Paddle refund
    fluent_cart_add_log(
        'Paddle Refund',
        'Paddle transaction refunded for Order #' . $order->id,
        'warning'
    );
}, 10, 4);
```

* * *

## Integrations [​](https://dev.fluentcart.com/hooks/actions/payments-and-integrations\#integrations)

### ` register_integration_action` [​](https://dev.fluentcart.com/hooks/actions/payments-and-integrations\#register-integration-action)

`fluent_cart/register_integration_action` - Register custom integration actions during initialization

**When it runs:** This action fires during WordPress `init` to allow registration of custom integration actions. Use this hook to register your integration provider so it appears in the FluentCart integration action settings.

**Parameters:**

None.

**Source:**`app/Modules/IntegrationActions/GlobalIntegrationActionHandler.php`

**Usage:**

php

```
add_action('fluent_cart/register_integration_action', function () {
    // Register a custom integration action provider
    add_filter('fluent_cart/integration/get_global_integration_actions', function ($actions) {
        $actions['my_crm'] = [\
            'title'    => 'My CRM',\
            'logo'     => plugin_dir_url(__FILE__) . 'logo.png',\
            'handler'  => 'MyCrmIntegrationHandler',\
        ];
        return $actions;
    });
}, 10, 0);
```

### ` authenticate_global_credentials_{$settingsKey}` [​](https://dev.fluentcart.com/hooks/actions/payments-and-integrations\#authenticate-global-credentials-settingskey)

`fluent_cart/integration/authenticate_global_credentials_{$settingsKey}` - Verify integration credentials for a specific provider

**When it runs:** This dynamic action fires when a user clicks the "Verify" or "Authenticate" button for an integration's global credentials in the FluentCart admin settings. The `{$settingsKey}` is the integration provider's settings key (e.g. `mailchimp`, `activecampaign`). The handler is expected to validate the credentials and send a JSON response.

**Parameters:**

- `$data` (array): The settings key and integration configuration
php

```
$data = [\
      'settings_key' => $settingsKey, // Integration provider key (string)\
      'integration'  => $integration, // Integration settings data (array, unslashed)\
];
```


**Source:**`app/Modules/Integrations/GlobalIntegrationSettings.php`

**Usage:**

php

```
add_action('fluent_cart/integration/authenticate_global_credentials_my_crm', function ($data) {
    $apiKey = $data['integration']['api_key'] ?? '';

    // Verify the API key with the external service
    $response = wp_remote_get('https://api.mycrm.com/verify', [\
        'headers' => ['Authorization' => 'Bearer ' . $apiKey],\
    ]);

    if (is_wp_error($response) || wp_remote_retrieve_response_code($response) !== 200) {
        wp_send_json_error(['message' => 'Invalid API credentials.'], 400);
    }

    wp_send_json_success(['message' => 'Credentials verified successfully.']);
}, 10, 1);
```

### ` save_global_integration_settings_{$settingsKey}` [​](https://dev.fluentcart.com/hooks/actions/payments-and-integrations\#save-global-integration-settings-settingskey)

`fluent_cart/integration/save_global_integration_settings_{$settingsKey}` - Save integration settings for a specific provider

**When it runs:** This dynamic action fires when a user saves the global integration settings for a specific provider. The `{$settingsKey}` is the integration provider's settings key. The handler is expected to persist the settings and send a JSON response. If no handler catches this action, a fallback error message is returned.

**Parameters:**

- `$data` (array): The settings key and integration configuration
php

```
$data = [\
      'settings_key' => $settingsKey, // Integration provider key (string)\
      'integration'  => $integration, // Integration settings data (array, unslashed)\
];
```


**Source:**`app/Modules/Integrations/GlobalIntegrationSettings.php`

**Usage:**

php

```
add_action('fluent_cart/integration/save_global_integration_settings_my_crm', function ($data) {
    $settings = $data['integration'];

    // Persist integration settings
    fluent_cart_update_option('my_crm_settings', $settings);

    wp_send_json_success([\
        'message' => 'Settings saved successfully.',\
    ]);
}, 10, 1);
```

### ` integration/chained_{$route}` [​](https://dev.fluentcart.com/hooks/actions/payments-and-integrations\#integration-chained-route)

`fluent_cart/integration/chained_{$route}` - Fires for chained data requests in cascading dropdowns

**When it runs:** This dynamic action fires when the integration settings UI requests chained/dependent data for cascading dropdown fields. For example, after selecting a mailing list, this hook loads the available tags or groups for that list. The `{$route}` is the integration's route identifier.

**Parameters:**

- `$data` (array): The request data for the chained lookup
php

```
$data = [\
      'data' => $requestData, // Request data array (contains route, selected values, etc.)\
];
```


**Source:**`app/Modules/Integrations/GlobalIntegrationSettings.php`

**Usage:**

php

```
add_action('fluent_cart/integration/chained_my_crm', function ($data) {
    $requestData = $data['data'];
    $listId = $requestData['list_id'] ?? '';

    // Fetch tags for the selected list
    $tags = my_crm_get_tags($listId);

    wp_send_json_success([\
        'tags' => $tags,\
    ]);
}, 10, 1);
```

### ` integration/run/{$provider}` [​](https://dev.fluentcart.com/hooks/actions/payments-and-integrations\#integration-run-provider)

`fluent_cart/integration/run/{$provider}` - Execute a specific integration feed for a provider

**When it runs:** This dynamic action fires when an integration feed needs to be executed for a specific provider, both in real-time (synchronous) and async (via scheduled actions) processing. The `{$provider}` is the integration provider's slug (e.g. `mailchimp`, `activecampaign`). It runs within a try/catch block, and errors are logged to the [Order](https://dev.fluentcart.com/database/models/order.html)'s activity log.

**Parameters:**

- `$integrationArray` (array): The full integration feed configuration and context
php

```
$integrationArray = [\
      'provider'   => 'mailchimp',  // Integration provider slug\
      'order'      => $order,       // Order model instance\
      'event_data' => $data,        // Event trigger data (may include subscription)\
      'feed'       => [],           // Feed configuration array\
      // ... additional feed configuration fields\
];
```


**Source:**`app/Listeners/IntegrationEventListener.php`

**Usage:**

php

```
add_action('fluent_cart/integration/run/my_crm', function ($integrationArray) {
    $order = $integrationArray['order'];
    $feed = $integrationArray['feed'] ?? [];
    $customer = $order->customer;

    // Push customer data to your CRM
    wp_remote_post('https://api.mycrm.com/contacts', [\
        'headers' => [\
            'Authorization' => 'Bearer ' . fluent_cart_get_option('my_crm_api_key'),\
            'Content-Type'  => 'application/json',\
        ],\
        'body' => wp_json_encode([\
            'email' => $customer->email,\
            'name'  => $customer->full_name,\
            'tags'  => $feed['tags'] ?? [],\
        ]),\
    ]);
}, 10, 1);
```

### ` global_notify_completed` [​](https://dev.fluentcart.com/hooks/actions/payments-and-integrations\#global-notify-completed)

`fluent_cart/integrations/global_notify_completed` - Fires after all synchronous global notification feeds have completed

**When it runs:** This action fires after all sync (non-async) global notification integration feeds have been processed for an order. It does not fire if there are async feeds still pending.

**Parameters:**

- `$order` ( [Order](https://dev.fluentcart.com/database/models/order.html)): The Order model instance
- `$feeds` (array): Array of feed configurations that were processed

**Source:**`app/Modules/Integrations/GlobalNotificationHandler.php`

**Usage:**

php

```
add_action('fluent_cart/integrations/global_notify_completed', function ($order, $feeds) {
    // All sync integrations are done for this order
    fluent_cart_add_log(
        'Integrations Complete',
        count($feeds) . ' integration feeds processed for Order #' . $order->id,
        'info'
    );
}, 10, 2);
```

### ` reindex_integration_feeds` [​](https://dev.fluentcart.com/hooks/actions/payments-and-integrations\#reindex-integration-feeds)

`fluent_cart/reindex_integration_feeds` - Fires when integration feeds need to be re-indexed

**When it runs:** This action fires after integration feed configurations are saved or updated, both at the global level (via `IntegrationController`) and at the product level (via `ProductIntegrationsController`). It signals that the cached integration feed index should be rebuilt.

**Parameters:**

- `$data` (array): Empty array
php

```
$data = []; // No data passed
```


**Source:**`app/Http/Controllers/IntegrationController.php`, `app/Http/Controllers/ProductIntegrationsController.php`

**Usage:**

php

```
add_action('fluent_cart/reindex_integration_feeds', function ($data) {
    // Clear any cached integration feed data
    delete_transient('my_plugin_integration_cache');
}, 10, 1);
```

* * *

## Storage Drivers [​](https://dev.fluentcart.com/hooks/actions/payments-and-integrations\#storage-drivers)

### ` register_storage_drivers` [​](https://dev.fluentcart.com/hooks/actions/payments-and-integrations\#register-storage-drivers)

`fluent_cart/register_storage_drivers` - Register custom file storage drivers

**When it runs:** This action fires during WordPress `init` at priority 9, after the built-in Local and S3 storage drivers have been initialized. Use this hook to register a custom file storage driver (e.g. Google Cloud Storage, Azure Blob Storage) for digital product file delivery.

**Parameters:**

None.

**Source:**`app/Hooks/Handlers/GlobalStorageHandler.php`

**Usage:**

php

```
add_action('fluent_cart/register_storage_drivers', function () {
    // Register a custom storage driver
    add_filter('fluent_cart/storage_drivers', function ($drivers) {
        $drivers['gcs'] = [\
            'title'   => 'Google Cloud Storage',\
            'handler' => new MyGcsStorageDriver(),\
        ];
        return $drivers;
    });
}, 10, 0);
```

* * *

## Development Logging [​](https://dev.fluentcart.com/hooks/actions/payments-and-integrations\#development-logging)

### ` dev_log` [​](https://dev.fluentcart.com/hooks/actions/payments-and-integrations\#dev-log)

`fluent_cart/dev_log` - Fires for development and debug logging (requires FLUENT\_CART\_DEV\_MODE)

**When it runs:** This action fires at various points during payment gateway webhook processing (primarily in the PayPal IPN handler) when the `FLUENT_CART_DEV_MODE` constant is defined. It provides detailed diagnostic data for debugging webhook failures, signature verification issues, and missing transaction references. There are 8+ call sites in the PayPal IPN handler alone.

**Parameters:**

- `$data` (array): Logging context with raw data and metadata
php

```
$data = [\
      'raw_data'    => $rawData,     // Raw webhook payload or resource data (mixed)\
      'status'      => 'failed',     // Log status: 'failed', 'received', etc.\
      'title'       => 'Log title',  // Human-readable log title (string)\
      'log_type'    => 'webhook',    // Type of log entry (string)\
      'module_type' => 'paypal_ipn', // Module identifier (string)\
      'module_name' => 'PayPal',     // Display name of the module (string)\
];
```


**Source:**`app/Modules/PaymentMethods/PayPalGateway/IPN.php` (multiple call sites)

**Usage:**

php

```
// First, define the constant in wp-config.php:
// define('FLUENT_CART_DEV_MODE', true);

add_action('fluent_cart/dev_log', function ($data) {
    // Write detailed logs to a custom file
    $logEntry = sprintf(
        "[%s] [%s] %s - %s\n%s\n\n",
        gmdate('Y-m-d H:i:s'),
        $data['status'] ?? 'unknown',
        $data['module_name'] ?? 'General',
        $data['title'] ?? 'No title',
        wp_json_encode($data['raw_data'] ?? [], JSON_PRETTY_PRINT)
    );

    error_log($logEntry, 3, WP_CONTENT_DIR . '/fluent-cart-debug.log');
}, 10, 1);
```

* * *

Today

Hi! I’m your AI assistant. How can I assist you today?

Just now

Powered by **FluentBot**


---

---

## Products & Coupons | FluentCart Developer Docs

**URL** : https://dev.fluentcart.com/hooks/actions/products-and-coupons

[Skip to content](https://dev.fluentcart.com/hooks/actions/products-and-coupons#VPContent)

# Products & Coupons [​](https://dev.fluentcart.com/hooks/actions/products-and-coupons\#products-coupons)

All hooks related to catalog management including [Product](https://dev.fluentcart.com/database/models/product.html) lifecycle, single product page rendering, product card rendering, and [Coupon](https://dev.fluentcart.com/database/models/coupon.html) management.

## Product Lifecycle [​](https://dev.fluentcart.com/hooks/actions/products-and-coupons\#product-lifecycle)

Hooks that fire during product create/update/duplicate operations in the admin.

### ` product_duplicated` [​](https://dev.fluentcart.com/hooks/actions/products-and-coupons\#product-duplicated)

`fluent_cart/product_duplicated` - Fired after a product is duplicated

**When it runs:** This action fires after a [Product](https://dev.fluentcart.com/database/models/product.html) has been fully duplicated, including all variants, taxonomy terms, and post meta. The database transaction has already been committed when this hook runs.

**Parameters:**

- `$data` (array): Duplication result data
php

```
$data = [\
      'original_product_id' => 123,        // (int) The source product's post ID\
      'new_product_id'      => 456,        // (int) The newly created product's post ID\
      'options'             => [\
          'import_stock_management'   => true,  // (bool) Whether stock settings were copied\
          'import_license_settings'   => true,  // (bool) Whether license settings were copied\
          'import_downloadable_files' => false,  // (bool) Whether downloadable files were copied\
      ],\
];
```


**Source:**`app/Models/Product.php`

**Usage:**

php

```
add_action('fluent_cart/product_duplicated', function($data) {
    $originalId = $data['original_product_id'];
    $newId      = $data['new_product_id'];

    // Copy custom meta that the core duplication doesn't handle
    $custom = get_post_meta($originalId, '_my_custom_field', true);
    if ($custom) {
        update_post_meta($newId, '_my_custom_field', $custom);
    }
}, 10, 1);
```

### ` product_updated` [​](https://dev.fluentcart.com/hooks/actions/products-and-coupons\#product-updated)

`fluent_cart/product_updated` - Fired when a product is updated via the admin API

**When it runs:** This action fires after a product has been successfully updated through the admin REST API (ProductController). It runs after `ProductResource::update()` has persisted all changes, including variants and product details.

**Parameters:**

- `$data` (array): Contains the raw request data and the updated [Product](https://dev.fluentcart.com/database/models/product.html) model
php

```
$data = [\
      'data'    => [              // (array) Sanitized request payload\
          'title'   => 'Product Name',\
          'detail'  => [\
              'variation_type' => 'simple',\
              // ... other product detail fields\
          ],\
          'variants' => [\
              // ... variant data\
          ],\
      ],\
      'product' => $product,      // (Product model) The updated Product instance\
];
```


**Source:**`app/Http/Controllers/ProductController.php`

**Usage:**

php

```
add_action('fluent_cart/product_updated', function($data) {
    $product = $data['product'];

    // Sync product to an external inventory system
    do_action('my_plugin/sync_inventory', [\
        'product_id' => $product->ID,\
        'title'      => $product->post_title,\
    ]);

    // Clear any cached product data
    wp_cache_delete('fct_product_' . $product->ID, 'fluent_cart');
}, 10, 1);
```

* * *

## Single Product Page Rendering [​](https://dev.fluentcart.com/hooks/actions/products-and-coupons\#single-product-page-rendering)

Hooks that fire during the server-side rendering of a single product page. All rendering hooks use **output buffering** \-\- your callback should `echo` HTML directly rather than return a value.

### ` render_product_header` [​](https://dev.fluentcart.com/hooks/actions/products-and-coupons\#render-product-header)

`fluent_cart/product/render_product_header` - Before the single product page content

**When it runs:** This action fires at the very top of a single product page, before the main post content is rendered. Output is captured via `ob_start()` / `ob_get_clean()` and prepended to the product content.

**Parameters:**

- `$postId` (int): The product's WordPress post ID

**Source:**`app/Modules/Templating/TemplateActions.php`

**Usage:**

php

```
add_action('fluent_cart/product/render_product_header', function($postId) {
    // Display a promotional banner above the product
    echo '<div class="my-promo-banner">Free shipping on this item!</div>';
}, 10, 1);
```

### ` after_product_content` [​](https://dev.fluentcart.com/hooks/actions/products-and-coupons\#after-product-content)

`fluent_cart/product/after_product_content` - After the single product page content

**When it runs:** This action fires immediately after the main product content on a single product page. Output is captured via `ob_start()` / `ob_get_clean()` and appended to the product content.

**Parameters:**

- `$postId` (int): The product's WordPress post ID

**Source:**`app/Modules/Templating/TemplateActions.php`

**Usage:**

php

```
add_action('fluent_cart/product/after_product_content', function($postId) {
    // Add a trust badge section below the product
    echo '<div class="trust-badges">';
    echo '<span>30-day money back guarantee</span>';
    echo '</div>';
}, 10, 1);
```

### ` product_archive` [​](https://dev.fluentcart.com/hooks/actions/products-and-coupons\#product-archive)

`fluent_cart/template/product_archive` - Render the product archive/taxonomy page

**When it runs:** This action fires when a product taxonomy archive page (category, tag, etc.) is being rendered. It is triggered inside `renderMainContent()` when the current page is a taxonomy page for `fluent-products`.

**Parameters:**

None.

**Source:**`app/Modules/Templating/TemplateActions.php`

**Usage:**

php

```
add_action('fluent_cart/template/product_archive', function() {
    // Render a custom product archive layout
    echo '<div class="my-custom-archive">';
    // ... your custom archive rendering
    echo '</div>';
}, 10, 0);
```

### ` before_price_block` [​](https://dev.fluentcart.com/hooks/actions/products-and-coupons\#before-price-block)

`fluent_cart/product/single/before_price_block` - Before the price block on a single product page

**When it runs:** This action fires immediately before the price wrapper `<div>` is rendered on a single product page. It fires in two contexts: once for simple products showing a single price, and once for multi-variant products showing the selected variant's price.

**Parameters:**

- `$data` (array): Price block context
php

```
$data = [\
      'product'       => $product,      // (Product model) The current product\
      'current_price' => 5000,          // (int) Price in cents\
      'scope'         => 'price_range', // (string) 'price_range' for simple products,\
                                        //          'product_variant_price' for variant pricing\
];
```


**Source:**`app/Services/Renderer/ProductRenderer.php`

**Usage:**

php

```
add_action('fluent_cart/product/single/before_price_block', function($data) {
    if ($data['scope'] === 'price_range') {
        echo '<div class="price-label">Our Price:</div>';
    }
}, 10, 1);
```

### ` after_price (single & card)` [​](https://dev.fluentcart.com/hooks/actions/products-and-coupons\#after-price-single-card)

`fluent_cart/product/after_price` - Inline after the price is rendered

**When it runs:** This action fires inline immediately after a price value is echoed, while still inside the price `<span>` or `<div>`. It fires in multiple contexts: simple product prices, price ranges, individual variant prices, and product cards. Use the `scope` key to distinguish between contexts.

**Parameters:**

- `$data` (array): Price context
php

```
$data = [\
      'product'       => $product,              // (Product model) The current product\
      'current_price' => 5000,                  // (int) Price in cents\
      'scope'         => 'price_range',         // (string) One of:\
                                                //   'price_range'          - simple product or min/max range\
                                                //   'product_variant_price' - individual variant price\
                                                //   'product_card'         - product card on archive/group pages\
];
```


**Source:**`app/Services/Renderer/ProductRenderer.php`, `app/Services/Renderer/ProductCardRender.php`

**Usage:**

php

```
add_action('fluent_cart/product/after_price', function($data) {
    // Show a "per unit" label next to the price
    if ($data['scope'] === 'product_variant_price') {
        echo '<span class="per-unit"> / unit</span>';
    }

    // Show a sale badge on product cards
    if ($data['scope'] === 'product_card') {
        echo '<span class="sale-badge">Sale</span>';
    }
}, 10, 1);
```

### ` after_price_block` [​](https://dev.fluentcart.com/hooks/actions/products-and-coupons\#after-price-block)

`fluent_cart/product/single/after_price_block` - After the price block wrapper closes on a single product page

**When it runs:** This action fires immediately after the closing `</div>` of the price block on a single product page. Like `before_price_block`, it fires in two contexts: simple product pricing and variant pricing.

**Parameters:**

- `$data` (array): Price block context
php

```
$data = [\
      'product'       => $product,      // (Product model) The current product\
      'current_price' => 5000,          // (int) Price in cents\
      'scope'         => 'price_range', // (string) 'price_range' for simple products,\
                                        //          'product_variant_price' for variant pricing\
];
```


**Source:**`app/Services/Renderer/ProductRenderer.php`

**Usage:**

php

```
add_action('fluent_cart/product/single/after_price_block', function($data) {
    // Add installment info below the price
    $monthly = \FluentCart\App\Helpers\Helper::toDecimal(intval($data['current_price'] / 3));
    echo '<p class="installment-info">Or 3 payments of ' . esc_html($monthly) . '</p>';
}, 10, 1);
```

### ` before_price_range_block` [​](https://dev.fluentcart.com/hooks/actions/products-and-coupons\#before-price-range-block)

`fluent_cart/product/single/before_price_range_block` - Before the price range block for multi-variant products

**When it runs:** This action fires before the min-max price range `<div>` is rendered on multi-variant products (products with more than one variant that show a "from X - Y" price range). It does **not** fire for simple products.

**Parameters:**

- `$data` (array): Price range context
php

```
$data = [\
      'product'       => $product,      // (Product model) The current product\
      'current_price' => 2000,          // (int) Minimum price in cents\
      'scope'         => 'price_range',\
];
```


**Source:**`app/Services/Renderer/ProductRenderer.php`

**Usage:**

php

```
add_action('fluent_cart/product/single/before_price_range_block', function($data) {
    echo '<div class="pricing-note">Choose a plan below:</div>';
}, 10, 1);
```

### ` after_price_range_block` [​](https://dev.fluentcart.com/hooks/actions/products-and-coupons\#after-price-range-block)

`fluent_cart/product/single/after_price_range_block` - After the price range block for multi-variant products

**When it runs:** This action fires after the closing `</div>` of the min-max price range block on multi-variant products. It does **not** fire for simple products.

**Parameters:**

- `$data` (array): Price range context
php

```
$data = [\
      'product'       => $product,      // (Product model) The current product\
      'current_price' => 2000,          // (int) Minimum price in cents\
      'scope'         => 'price_range',\
];
```


**Source:**`app/Services/Renderer/ProductRenderer.php`

**Usage:**

php

```
add_action('fluent_cart/product/single/after_price_range_block', function($data) {
    echo '<p class="bulk-discount">Bulk discounts available for 10+ licenses.</p>';
}, 10, 1);
```

### ` before_variant_item` [​](https://dev.fluentcart.com/hooks/actions/products-and-coupons\#before-variant-item)

`fluent_cart/product/single/before_variant_item` - Before each variant item in the variant list

**When it runs:** This action fires before each individual [ProductVariation](https://dev.fluentcart.com/database/models/product-variation.html) option is rendered in the variant selection list. It fires once per variant, inside the `foreach` loop that iterates over sorted variants. It fires in both the standard variant list and the tabbed (subscription/onetime) variant layout.

**Parameters:**

- `$data` (array): Variant item context
php

```
$data = [\
      'product' => $product,               // (Product model) The current product\
      'variant' => $variant,               // (ProductVariant model) The current variant being rendered\
      'scope'   => 'product_variant_item',\
];
```


**Source:**`app/Services/Renderer/ProductRenderer.php`

**Usage:**

php

```
add_action('fluent_cart/product/single/before_variant_item', function($data) {
    $variant = $data['variant'];

    // Add a "Most Popular" badge before a specific variant
    if ($variant->id === 42) {
        echo '<div class="popular-badge">Most Popular</div>';
    }
}, 10, 1);
```

### ` after_variant_item` [​](https://dev.fluentcart.com/hooks/actions/products-and-coupons\#after-variant-item)

`fluent_cart/product/single/after_variant_item` - After each variant item in the variant list

**When it runs:** This action fires after each individual variant option is rendered in the variant selection list. It fires once per variant, immediately after `renderVariationItem()` completes. It fires in both the standard variant list and the tabbed variant layout.

**Parameters:**

- `$data` (array): Variant item context
php

```
$data = [\
      'product' => $product,               // (Product model) The current product\
      'variant' => $variant,               // (ProductVariant model) The current variant being rendered\
      'scope'   => 'product_variant_item',\
];
```


**Source:**`app/Services/Renderer/ProductRenderer.php`

**Usage:**

php

```
add_action('fluent_cart/product/single/after_variant_item', function($data) {
    $variant = $data['variant'];

    // Show remaining stock below each variant
    if ($variant->stock_quantity > 0 && $variant->stock_quantity < 10) {
        echo '<span class="low-stock">Only ' . esc_html($variant->stock_quantity) . ' left!</span>';
    }
}, 10, 1);
```

### ` before_quantity_block` [​](https://dev.fluentcart.com/hooks/actions/products-and-coupons\#before-quantity-block)

`fluent_cart/product/single/before_quantity_block` - Before the quantity selector on a single product page

**When it runs:** This action fires immediately before the quantity input container is rendered on a single product page. It only fires if the product allows quantity selection (not hidden by sold-individually or other conditions).

**Parameters:**

- `$data` (array): Quantity block context
php

```
$data = [\
      'product' => $product,                   // (Product model) The current product\
      'scope'   => 'product_quantity_block',\
];
```


**Source:**`app/Services/Renderer/ProductRenderer.php`

**Usage:**

php

```
add_action('fluent_cart/product/single/before_quantity_block', function($data) {
    echo '<p class="quantity-hint">Select your desired quantity:</p>';
}, 10, 1);
```

### ` after_quantity_block` [​](https://dev.fluentcart.com/hooks/actions/products-and-coupons\#after-quantity-block)

`fluent_cart/product/single/after_quantity_block` - After the quantity selector on a single product page

**When it runs:** This action fires immediately after the quantity input container is rendered on a single product page, after the closing `</div>` of the quantity wrapper.

**Parameters:**

- `$data` (array): Quantity block context
php

```
$data = [\
      'product' => $product,                   // (Product model) The current product\
      'scope'   => 'product_quantity_block',\
];
```


**Source:**`app/Services/Renderer/ProductRenderer.php`

**Usage:**

php

```
add_action('fluent_cart/product/single/after_quantity_block', function($data) {
    // Show bulk pricing table after the quantity selector
    echo '<div class="bulk-pricing">';
    echo '<small>Buy 5+ and save 10% &bull; Buy 10+ and save 20%</small>';
    echo '</div>';
}, 10, 1);
```

* * *

## Product Card Rendering (Archive / Group Pages) [​](https://dev.fluentcart.com/hooks/actions/products-and-coupons\#product-card-rendering-archive-group-pages)

Hooks that fire during server-side rendering of product cards on archive pages, product group blocks, and shop listings. All rendering hooks use **output buffering** \-\- your callback should `echo` HTML directly.

### ` group/before_image_block` [​](https://dev.fluentcart.com/hooks/actions/products-and-coupons\#group-before-image-block)

`fluent_cart/product/group/before_image_block` - Before the product card image

**When it runs:** This action fires before the product card image link and `<img>` tag are rendered inside a product card on archive or group pages.

**Parameters:**

- `$data` (array): Product card context
php

```
$data = [\
      'product' => $product,        // (Product model) The current product\
      'scope'   => 'product_card',\
];
```


**Source:**`app/Services/Renderer/ProductCardRender.php`

**Usage:**

php

```
add_action('fluent_cart/product/group/before_image_block', function($data) {
    // Add a "New" ribbon over the product card image
    $product = $data['product'];
    $created = strtotime($product->post_date);
    if ($created > strtotime('-30 days')) {
        echo '<span class="new-ribbon">New</span>';
    }
}, 10, 1);
```

### ` group/after_image_block` [​](https://dev.fluentcart.com/hooks/actions/products-and-coupons\#group-after-image-block)

`fluent_cart/product/group/after_image_block` - After the product card image

**When it runs:** This action fires immediately after the product card image link closes, before the rest of the card content (title, price, button) is rendered.

**Parameters:**

- `$data` (array): Product card context
php

```
$data = [\
      'product' => $product,        // (Product model) The current product\
      'scope'   => 'product_card',\
];
```


**Source:**`app/Services/Renderer/ProductCardRender.php`

**Usage:**

php

```
add_action('fluent_cart/product/group/after_image_block', function($data) {
    // Add a quick-view button overlay after the image
    echo '<button class="quick-view-btn" data-product="' . esc_attr($data['product']->ID) . '">Quick View</button>';
}, 10, 1);
```

### ` group/before_price_block` [​](https://dev.fluentcart.com/hooks/actions/products-and-coupons\#group-before-price-block)

`fluent_cart/product/group/before_price_block` - Before the price section in product cards

**When it runs:** This action fires before the price wrapper `<div class="fct-product-card-prices">` is rendered inside a product card on archive or group pages.

**Parameters:**

- `$data` (array): Product card price context
php

```
$data = [\
      'product'       => $product,       // (Product model) The current product\
      'current_price' => 2000,           // (int) Minimum price in cents\
      'scope'         => 'product_card',\
];
```


**Source:**`app/Services/Renderer/ProductCardRender.php`

**Usage:**

php

```
add_action('fluent_cart/product/group/before_price_block', function($data) {
    // Show a "Starting at" label before the price
    echo '<span class="price-prefix">Starting at</span>';
}, 10, 1);
```

### ` group/after_price_block` [​](https://dev.fluentcart.com/hooks/actions/products-and-coupons\#group-after-price-block)

`fluent_cart/product/group/after_price_block` - After the price section in product cards

**When it runs:** This action fires immediately after the closing `</div>` of the product card price wrapper, after prices and the inline `fluent_cart/product/after_price` hook have been rendered.

**Parameters:**

- `$data` (array): Product card price context
php

```
$data = [\
      'product'       => $product,       // (Product model) The current product\
      'current_price' => 2000,           // (int) Minimum price in cents\
      'scope'         => 'product_card',\
];
```


**Source:**`app/Services/Renderer/ProductCardRender.php`

**Usage:**

php

```
add_action('fluent_cart/product/group/after_price_block', function($data) {
    // Show a short feature list below the price on product cards
    $features = get_post_meta($data['product']->ID, '_card_features', true);
    if ($features) {
        echo '<ul class="card-features">';
        foreach ((array) $features as $feature) {
            echo '<li>' . esc_html($feature) . '</li>';
        }
        echo '</ul>';
    }
}, 10, 1);
```

* * *

## Coupons [​](https://dev.fluentcart.com/hooks/actions/products-and-coupons\#coupons)

Hooks that fire during [Coupon](https://dev.fluentcart.com/database/models/coupon.html) create and update operations in the admin.

### ` coupon_created` [​](https://dev.fluentcart.com/hooks/actions/products-and-coupons\#coupon-created)

`fluent_cart/coupon_created` - Fired after a new coupon is created via the admin

**When it runs:** This action fires after a [Coupon](https://dev.fluentcart.com/database/models/coupon.html) has been successfully created through the admin REST API. It runs after `CouponResource::create()` has persisted the coupon and after the activity log entry has been recorded.

**Parameters:**

- `$data` (array): [Coupon](https://dev.fluentcart.com/database/models/coupon.html) creation data
php

```
$data = [\
      'data'   => [                // (array) Sanitized request payload\
          'title'      => 'SAVE20',\
          'type'       => 'percentage',   // 'percentage' or 'fixed'\
          'amount'     => 2000,           // (int) Discount amount in cents (or percentage value)\
          'start_date' => '2026-01-01 00:00:00',  // (string|null) GMT start date\
          'end_date'   => '2026-12-31 23:59:59',  // (string|null) GMT end date\
          'conditions' => [\
              'is_recurring' => 'no',\
              // ... other condition fields\
          ],\
      ],\
      'coupon' => $coupon,          // (Coupon model) The newly created Coupon instance\
];
```


**Source:**`app/Http/Controllers/CouponsController.php`

**Usage:**

php

```
add_action('fluent_cart/coupon_created', function($data) {
    $coupon = $data['coupon'];

    // Notify marketing team about the new coupon
    wp_mail(
        'marketing@example.com',
        'New Coupon Created: ' . $coupon->title,
        'A new coupon has been created with code: ' . $coupon->title
    );
}, 10, 1);
```

### ` coupon_updated` [​](https://dev.fluentcart.com/hooks/actions/products-and-coupons\#coupon-updated)

`fluent_cart/coupon_updated` - Fired after a coupon is updated via the admin

**When it runs:** This action fires after a [Coupon](https://dev.fluentcart.com/database/models/coupon.html) has been successfully updated through the admin REST API. It runs after `CouponResource::update()` has persisted the changes, but before the activity log entry is recorded.

**Parameters:**

- `$data` (array): Coupon update data
php

```
$data = [\
      'data'   => [                // (array) Sanitized request payload\
          'title'      => 'SAVE20',\
          'type'       => 'percentage',\
          'amount'     => 2500,\
          'start_date' => '2026-01-01 00:00:00',\
          'end_date'   => '2026-12-31 23:59:59',\
          'conditions' => [\
              'is_recurring' => 'no',\
              // ... other condition fields\
          ],\
      ],\
      'coupon' => $coupon,          // (Coupon model) The updated Coupon instance\
];
```


**Source:**`app/Http/Controllers/CouponsController.php`

**Usage:**

php

```
add_action('fluent_cart/coupon_updated', function($data) {
    $coupon = $data['coupon'];

    // Clear coupon validation cache when a coupon is modified
    wp_cache_delete('fct_coupon_' . $coupon->id, 'fluent_cart');

    // Sync updated coupon to external promotion platform
    do_action('my_plugin/sync_coupon', $coupon);
}, 10, 1);
```

Today

Hi! I’m your AI assistant. How can I assist you today?

Just now

Powered by **FluentBot**


---

---

