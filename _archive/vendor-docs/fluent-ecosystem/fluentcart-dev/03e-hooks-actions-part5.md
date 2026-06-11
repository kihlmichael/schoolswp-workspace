# FluentCart Developer Docs - Hooks (Actions) (Part 5/5)

Toutes les actions WordPress exposées par FluentCart, groupées par domaine (orders, subscriptions, cart & checkout, customers & users, products & coupons, licenses, admin & templates, payments & integrations).

---

## Subscriptions | FluentCart Developer Docs

**URL** : https://dev.fluentcart.com/hooks/actions/subscriptions

[Skip to content](https://dev.fluentcart.com/hooks/actions/subscriptions#VPContent)

# Subscriptions [​](https://dev.fluentcart.com/hooks/actions/subscriptions\#subscriptions)

Action hooks for [Subscription](https://dev.fluentcart.com/database/models/subscription.html) lifecycle management, status transitions, and scheduled reminder notifications. These hooks let you react to subscription state changes, send custom notifications, and integrate with external systems. Most hooks pass the related [Order](https://dev.fluentcart.com/database/models/order.html) and [Customer](https://dev.fluentcart.com/database/models/customer.html) models as well.

* * *

## Subscription Status Changes [​](https://dev.fluentcart.com/hooks/actions/subscriptions\#subscription-status-changes)

### ` subscription_status_changed` [​](https://dev.fluentcart.com/hooks/actions/subscriptions\#subscription-status-changed)

`fluent_cart/payments/subscription_status_changed` - Fires on any subscription status transition

**When it runs:** This action fires whenever a [Subscription](https://dev.fluentcart.com/database/models/subscription.html)'s status changes from one value to another (e.g., `pending` to `active`, `active` to `cancelled`, etc.). It does **not** fire when other subscription data changes without a status transition. This is the generic handler -- for status-specific hooks, see `fluent_cart/payments/subscription_{$status}` below.

**Parameters:**

- `$data` (array): Subscription status change data
php

```
$data = [\
      'subscription' => $subscriptionModel, // \FluentCart\App\Models\Subscription\
      'order'        => $subscriptionModel->order, // \FluentCart\App\Models\Order\
      'customer'     => $subscriptionModel->customer, // \FluentCart\App\Models\Customer\
      'old_status'   => 'pending', // string - previous status\
      'new_status'   => 'active', // string - current status after update\
];
```


**Source:**`app/Modules/Subscriptions/Services/SubscriptionService.php`

**Usage:**

php

```
add_action('fluent_cart/payments/subscription_status_changed', function ($data) {
    $subscription = $data['subscription'];
    $oldStatus    = $data['old_status'];
    $newStatus    = $data['new_status'];

    // Log every status transition
    fluent_cart_add_log(
        'Subscription Status Changed',
        sprintf('Subscription #%d changed from %s to %s', $subscription->id, $oldStatus, $newStatus),
        'info'
    );
}, 10, 1);
```

### ` subscription_active` [​](https://dev.fluentcart.com/hooks/actions/subscriptions\#subscription-active)

`fluent_cart/payments/subscription_active` - Fires when a subscription becomes active

**When it runs:** This action fires when a subscription's status transitions to `active`. This may occur after initial payment, after reactivation, or when moving from `trialing` to `active`.

**Parameters:**

- `$data` (array): Subscription data
php

```
$data = [\
      'subscription' => $subscriptionModel, // \FluentCart\App\Models\Subscription\
      'order'        => $subscriptionModel->order, // \FluentCart\App\Models\Order\
      'customer'     => $subscriptionModel->customer, // \FluentCart\App\Models\Customer\
      'old_status'   => 'pending', // string - previous status\
      'new_status'   => 'active', // string - always 'active'\
];
```


**Source:**`app/Modules/Subscriptions/Services/SubscriptionService.php`

**Usage:**

php

```
add_action('fluent_cart/payments/subscription_active', function ($data) {
    $customer = $data['customer'];

    // Grant premium access when subscription activates
    update_user_meta($customer->user_id, 'premium_member', true);
}, 10, 1);
```

### ` subscription_canceled` [​](https://dev.fluentcart.com/hooks/actions/subscriptions\#subscription-canceled)

`fluent_cart/payments/subscription_canceled` - Fires when a subscription is cancelled

**When it runs:** This action fires when a subscription's status transitions to `canceled`. The `canceled_at` timestamp is automatically set if not already provided.

**Parameters:**

- `$data` (array): Subscription data
php

```
$data = [\
      'subscription' => $subscriptionModel, // \FluentCart\App\Models\Subscription\
      'order'        => $subscriptionModel->order, // \FluentCart\App\Models\Order\
      'customer'     => $subscriptionModel->customer, // \FluentCart\App\Models\Customer\
      'old_status'   => 'active', // string - previous status\
      'new_status'   => 'canceled', // string - always 'canceled'\
];
```


**Source:**`app/Modules/Subscriptions/Services/SubscriptionService.php`

**Usage:**

php

```
add_action('fluent_cart/payments/subscription_canceled', function ($data) {
    $subscription = $data['subscription'];
    $customer     = $data['customer'];

    // Revoke premium access on cancellation
    update_user_meta($customer->user_id, 'premium_member', false);

    // Notify admin
    wp_mail(
        get_option('admin_email'),
        'Subscription Cancelled',
        sprintf('Subscription #%d for %s has been cancelled.', $subscription->id, $customer->email)
    );
}, 10, 1);
```

### ` subscription_paused` [​](https://dev.fluentcart.com/hooks/actions/subscriptions\#subscription-paused)

`fluent_cart/payments/subscription_paused` - Fires when a subscription is paused

**When it runs:** This action fires when a subscription's status transitions to `paused`. The subscription remains in the system but billing is temporarily halted.

**Parameters:**

- `$data` (array): Subscription data
php

```
$data = [\
      'subscription' => $subscriptionModel, // \FluentCart\App\Models\Subscription\
      'order'        => $subscriptionModel->order, // \FluentCart\App\Models\Order\
      'customer'     => $subscriptionModel->customer, // \FluentCart\App\Models\Customer\
      'old_status'   => 'active', // string - previous status\
      'new_status'   => 'paused', // string - always 'paused'\
];
```


**Source:**`app/Modules/Subscriptions/Services/SubscriptionService.php`

**Usage:**

php

```
add_action('fluent_cart/payments/subscription_paused', function ($data) {
    $subscription = $data['subscription'];

    // Temporarily suspend feature access
    update_user_meta($data['customer']->user_id, 'subscription_paused', true);
}, 10, 1);
```

### ` subscription_expired` [​](https://dev.fluentcart.com/hooks/actions/subscriptions\#subscription-expired)

`fluent_cart/payments/subscription_expired` - Fires when a subscription expires

**When it runs:** This action fires when a subscription's status transitions to `expired`. After this hook fires, the system also stores a `validity_expired_at` meta value and dispatches the `SubscriptionValidityExpired` event.

**Parameters:**

- `$data` (array): Subscription data
php

```
$data = [\
      'subscription' => $subscriptionModel, // \FluentCart\App\Models\Subscription\
      'order'        => $subscriptionModel->order, // \FluentCart\App\Models\Order\
      'customer'     => $subscriptionModel->customer, // \FluentCart\App\Models\Customer\
      'old_status'   => 'active', // string - previous status\
      'new_status'   => 'expired', // string - always 'expired'\
];
```


**Source:**`app/Modules/Subscriptions/Services/SubscriptionService.php`

**Usage:**

php

```
add_action('fluent_cart/payments/subscription_expired', function ($data) {
    $customer = $data['customer'];

    // Remove premium access
    update_user_meta($customer->user_id, 'premium_member', false);

    // Notify the customer
    wp_mail(
        $customer->email,
        'Your Subscription Has Expired',
        'Your subscription has expired. Please renew to continue using premium features.'
    );
}, 10, 1);
```

### ` subscription_failing` [​](https://dev.fluentcart.com/hooks/actions/subscriptions\#subscription-failing)

`fluent_cart/payments/subscription_failing` - Fires when a subscription payment is failing

**When it runs:** This action fires when a subscription's status transitions to `failing`, indicating that a renewal payment attempt has failed. The subscription is still technically active but requires payment attention.

**Parameters:**

- `$data` (array): Subscription data
php

```
$data = [\
      'subscription' => $subscriptionModel, // \FluentCart\App\Models\Subscription\
      'order'        => $subscriptionModel->order, // \FluentCart\App\Models\Order\
      'customer'     => $subscriptionModel->customer, // \FluentCart\App\Models\Customer\
      'old_status'   => 'active', // string - previous status\
      'new_status'   => 'failing', // string - always 'failing'\
];
```


**Source:**`app/Modules/Subscriptions/Services/SubscriptionService.php`

**Usage:**

php

```
add_action('fluent_cart/payments/subscription_failing', function ($data) {
    $subscription = $data['subscription'];
    $customer     = $data['customer'];

    // Alert the customer about the payment failure
    wp_mail(
        $customer->email,
        'Payment Failed for Your Subscription',
        sprintf('We were unable to process payment for subscription #%d. Please update your payment method.', $subscription->id)
    );
}, 10, 1);
```

### ` subscription_expiring` [​](https://dev.fluentcart.com/hooks/actions/subscriptions\#subscription-expiring)

`fluent_cart/payments/subscription_expiring` - Fires when a subscription is marked as expiring soon

**When it runs:** This action fires when a subscription's status transitions to `expiring`, indicating that the subscription is approaching its end-of-term and will not be renewed.

**Parameters:**

- `$data` (array): Subscription data
php

```
$data = [\
      'subscription' => $subscriptionModel, // \FluentCart\App\Models\Subscription\
      'order'        => $subscriptionModel->order, // \FluentCart\App\Models\Order\
      'customer'     => $subscriptionModel->customer, // \FluentCart\App\Models\Customer\
      'old_status'   => 'active', // string - previous status\
      'new_status'   => 'expiring', // string - always 'expiring'\
];
```


**Source:**`app/Modules/Subscriptions/Services/SubscriptionService.php`

**Usage:**

php

```
add_action('fluent_cart/payments/subscription_expiring', function ($data) {
    $subscription = $data['subscription'];
    $customer     = $data['customer'];

    // Send a win-back offer before the subscription fully expires
    wp_mail(
        $customer->email,
        'Your Subscription is About to Expire',
        'Renew now and get 10% off your next billing cycle!'
    );
}, 10, 1);
```

### ` subscription_completed` [​](https://dev.fluentcart.com/hooks/actions/subscriptions\#subscription-completed)

`fluent_cart/payments/subscription_completed` - Fires when a subscription completes all billing cycles

**When it runs:** This action fires when a subscription's status transitions to `completed`. This occurs when the subscription has reached its end-of-term (EOT) -- i.e., the `bill_count` has met or exceeded `bill_times`. The `next_billing_date` is set to `NULL` and `canceled_at` is cleared.

**Parameters:**

- `$data` (array): Subscription data
php

```
$data = [\
      'subscription' => $subscriptionModel, // \FluentCart\App\Models\Subscription\
      'order'        => $subscriptionModel->order, // \FluentCart\App\Models\Order\
      'customer'     => $subscriptionModel->customer, // \FluentCart\App\Models\Customer\
      'old_status'   => 'active', // string - previous status\
      'new_status'   => 'completed', // string - always 'completed'\
];
```


**Source:**`app/Modules/Subscriptions/Services/SubscriptionService.php`

**Usage:**

php

```
add_action('fluent_cart/payments/subscription_completed', function ($data) {
    $subscription = $data['subscription'];
    $customer     = $data['customer'];

    // Thank the customer for completing their subscription term
    wp_mail(
        $customer->email,
        'Subscription Complete',
        sprintf('Your subscription #%d has completed all %d billing cycles. Thank you!', $subscription->id, $subscription->bill_times)
    );
}, 10, 1);
```

### ` subscription_trialing` [​](https://dev.fluentcart.com/hooks/actions/subscriptions\#subscription-trialing)

`fluent_cart/payments/subscription_trialing` - Fires when a subscription enters trial status

**When it runs:** This action fires when a subscription's status transitions to `trialing`. The subscription is in a free trial period and will transition to `active` (with billing) when the trial ends.

**Parameters:**

- `$data` (array): Subscription data
php

```
$data = [\
      'subscription' => $subscriptionModel, // \FluentCart\App\Models\Subscription\
      'order'        => $subscriptionModel->order, // \FluentCart\App\Models\Order\
      'customer'     => $subscriptionModel->customer, // \FluentCart\App\Models\Customer\
      'old_status'   => 'pending', // string - previous status\
      'new_status'   => 'trialing', // string - always 'trialing'\
];
```


**Source:**`app/Modules/Subscriptions/Services/SubscriptionService.php`

**Usage:**

php

```
add_action('fluent_cart/payments/subscription_trialing', function ($data) {
    $subscription = $data['subscription'];
    $customer     = $data['customer'];

    // Grant trial access
    update_user_meta($customer->user_id, 'trial_active', true);

    // Schedule a welcome email
    wp_mail(
        $customer->email,
        'Your Free Trial Has Started',
        sprintf('Enjoy your trial! Your first payment will be on %s.', $subscription->next_billing_date)
    );
}, 10, 1);
```

* * *

## Subscription Data Updates [​](https://dev.fluentcart.com/hooks/actions/subscriptions\#subscription-data-updates)

### ` subscription_data_updated` [​](https://dev.fluentcart.com/hooks/actions/subscriptions\#subscription-data-updated)

`fluent_cart/subscription/data_updated` - Fires when subscription data changes without a status transition

**When it runs:** This action fires when [Subscription](https://dev.fluentcart.com/database/models/subscription.html) attributes are modified but the status remains the same. Examples include billing amount changes, next payment date adjustments, or metadata updates. It only fires when there are actual dirty (changed) fields on the model.

**Parameters:**

- `$data` (array): Subscription update data
php

```
$data = [\
      'subscription' => $subscriptionModel, // \FluentCart\App\Models\Subscription (already saved)\
      'updated_data' => [\
          // Only the fields that actually changed (dirty attributes), e.g.:\
          'recurring_total'   => 2999, // int - new amount in cents\
          'next_billing_date' => '2025-03-15 00:00:00', // string - updated billing date\
      ],\
];
```


**Source:**`app/Modules/Subscriptions/Services/SubscriptionService.php`

**Usage:**

php

```
add_action('fluent_cart/subscription/data_updated', function ($data) {
    $subscription = $data['subscription'];
    $updatedData  = $data['updated_data'];

    // Log billing amount changes
    if (isset($updatedData['recurring_total'])) {
        fluent_cart_add_log(
            'Subscription Amount Changed',
            sprintf(
                'Subscription #%d recurring total changed to %s',
                $subscription->id,
                number_format($updatedData['recurring_total'] / 100, 2)
            ),
            'info'
        );
    }

    // Sync next billing date with external calendar
    if (isset($updatedData['next_billing_date'])) {
        do_action('my_plugin/sync_billing_date', $subscription->id, $updatedData['next_billing_date']);
    }
}, 10, 1);
```

* * *

## Reminders & Notifications [​](https://dev.fluentcart.com/hooks/actions/subscriptions\#reminders-notifications)

### ` subscription_renewal_reminder` [​](https://dev.fluentcart.com/hooks/actions/subscriptions\#subscription-renewal-reminder)

`fluent_cart/subscription_renewal_reminder` - Fires when a subscription renewal reminder is due

**When it runs:** This action fires on a scheduled basis (via Action Scheduler) when a subscription's next billing date is approaching. The reminder system supports multiple billing cycles (yearly, monthly, quarterly, half-yearly) and configurable "days before" thresholds. Only fires for subscriptions with `active` or `trialing` status. The stage name indicates how many days before renewal (e.g., `before_30`, `before_7`).

**Parameters:**

- `$data` (array): Renewal reminder data
php

```
$data = [\
      'subscription' => $subscription, // \FluentCart\App\Models\Subscription\
      'order'        => $subscription->order, // \FluentCart\App\Models\Order\
      'customer'     => $subscription->customer, // \FluentCart\App\Models\Customer\
      'reminder'     => [\
          'stage'         => 'before_30', // string - e.g., 'before_30', 'before_7'\
          'billing_cycle' => 'yearly', // string - 'yearly', 'monthly', 'quarterly', 'half_yearly'\
          'billing_date'  => '2025-03-15 00:00:00', // string - GMT formatted next billing date\
      ],\
];
```


**Source:**`app/Services/Reminders/SubscriptionReminderService.php`

**Usage:**

php

```
add_action('fluent_cart/subscription_renewal_reminder', function ($data) {
    $subscription = $data['subscription'];
    $customer     = $data['customer'];
    $reminder     = $data['reminder'];

    // Send a custom renewal reminder email
    wp_mail(
        $customer->email,
        'Subscription Renewal Coming Up',
        sprintf(
            'Your %s subscription #%d will renew on %s.',
            $reminder['billing_cycle'],
            $subscription->id,
            date('F j, Y', strtotime($reminder['billing_date']))
        )
    );
}, 10, 1);
```

### ` subscription_trial_end_reminder` [​](https://dev.fluentcart.com/hooks/actions/subscriptions\#subscription-trial-end-reminder)

`fluent_cart/subscription_trial_end_reminder` - Fires when a trial ending reminder is due

**When it runs:** This action fires on a scheduled basis when a trialing subscription's trial period is about to end. Only fires for subscriptions with `trialing` status (excluding simulated trials). The stage name indicates how many days before the trial ends (e.g., `trial_end_3`, `trial_end_1`). Configurable via the `trial_end_reminder_days` store setting.

**Parameters:**

- `$data` (array): Trial end reminder data
php

```
$data = [\
      'subscription' => $subscription, // \FluentCart\App\Models\Subscription\
      'order'        => $subscription->order, // \FluentCart\App\Models\Order\
      'customer'     => $subscription->customer, // \FluentCart\App\Models\Customer\
      'reminder'     => [\
          'stage'          => 'trial_end_3', // string - e.g., 'trial_end_3', 'trial_end_1'\
          'trial_end_date' => '2025-02-01 00:00:00', // string - GMT formatted trial end date\
      ],\
];
```


**Source:**`app/Services/Reminders/SubscriptionReminderService.php`

**Usage:**

php

```
add_action('fluent_cart/subscription_trial_end_reminder', function ($data) {
    $subscription = $data['subscription'];
    $customer     = $data['customer'];
    $reminder     = $data['reminder'];

    // Notify customer that their trial is ending soon
    wp_mail(
        $customer->email,
        'Your Free Trial is Ending Soon',
        sprintf(
            'Your trial for subscription #%d ends on %s. After that, you will be billed %s.',
            $subscription->id,
            date('F j, Y', strtotime($reminder['trial_end_date'])),
            number_format($subscription->recurring_total / 100, 2)
        )
    );
}, 10, 1);
```

### ` invoice_reminder_overdue` [​](https://dev.fluentcart.com/hooks/actions/subscriptions\#invoice-reminder-overdue)

`fluent_cart/invoice_reminder_overdue` - Fires when an overdue invoice reminder is triggered

**When it runs:** This action fires on a scheduled basis when an [Order](https://dev.fluentcart.com/database/models/order.html) with an outstanding balance has passed its due date by a configured number of days. The stage name indicates how many days overdue (e.g., `overdue_1`, `overdue_3`, `overdue_7`). Only fires for orders with `pending`, `partially_paid`, `failed`, or `authorized` payment statuses. The overdue days are configurable via the `invoice_reminder_overdue_days` store setting (defaults to `1,3,7`).

**Parameters:**

- `$data` (array): Invoice overdue reminder data
php

```
$data = [\
      'order'    => $order, // \FluentCart\App\Models\Order\
      'customer' => $order->customer, // \FluentCart\App\Models\Customer\
      'reminder' => [\
          'stage'        => 'overdue_3', // string - e.g., 'overdue_1', 'overdue_3', 'overdue_7'\
          'order_id'     => 123, // int - order ID\
          'order_ref'    => 'INV-00123', // string - invoice number or '#123' fallback\
          'due_at'       => '2025-01-15 00:00:00', // string - GMT formatted due date\
          'due_amount'   => 5000, // int - outstanding amount in cents\
          'payment_link' => 'https://example.com/checkout/pay/uuid', // string - customer payment URL\
      ],\
];
```


**Source:**`app/Services/Reminders/InvoiceReminderService.php`

**Usage:**

php

```
add_action('fluent_cart/invoice_reminder_overdue', function ($data) {
    $order    = $data['order'];
    $customer = $data['customer'];
    $reminder = $data['reminder'];

    // Send a payment reminder with a direct payment link
    wp_mail(
        $customer->email,
        sprintf('Payment Overdue for %s', $reminder['order_ref']),
        sprintf(
            "Your payment of %s for order %s is overdue.\n\nPay now: %s",
            number_format($reminder['due_amount'] / 100, 2),
            $reminder['order_ref'],
            $reminder['payment_link']
        )
    );
}, 10, 1);
```

### ` invoice_reminder_due` [​](https://dev.fluentcart.com/hooks/actions/subscriptions\#invoice-reminder-due)

`fluent_cart/invoice_reminder_due` - Fires when an invoice due-date reminder is triggered

**When it runs:** This action fires on a scheduled basis when an order with an outstanding balance has reached its due date (stage `before_0`). This is the on-due-date notification, as opposed to the overdue reminders that fire after the due date has passed. Shares the same parameter structure as the overdue reminder.

> **Note:** This hook is currently defined in the codebase but the queueing logic for the `before_0` stage is commented out pending the full invoice feature deployment. It is documented here for forward compatibility.

**Parameters:**

- `$data` (array): Invoice due reminder data
php

```
$data = [\
      'order'    => $order, // \FluentCart\App\Models\Order\
      'customer' => $order->customer, // \FluentCart\App\Models\Customer\
      'reminder' => [\
          'stage'        => 'before_0', // string - always 'before_0' for due-date reminders\
          'order_id'     => 123, // int - order ID\
          'order_ref'    => 'INV-00123', // string - invoice number or '#123' fallback\
          'due_at'       => '2025-01-15 00:00:00', // string - GMT formatted due date\
          'due_amount'   => 5000, // int - outstanding amount in cents\
          'payment_link' => 'https://example.com/checkout/pay/uuid', // string - customer payment URL\
      ],\
];
```


**Source:**`app/Services/Reminders/InvoiceReminderService.php`

**Usage:**

php

```
add_action('fluent_cart/invoice_reminder_due', function ($data) {
    $order    = $data['order'];
    $customer = $data['customer'];
    $reminder = $data['reminder'];

    // Notify customer that their invoice is due today
    wp_mail(
        $customer->email,
        sprintf('Payment Due Today for %s', $reminder['order_ref']),
        sprintf(
            "Your payment of %s for order %s is due today.\n\nPay now: %s",
            number_format($reminder['due_amount'] / 100, 2),
            $reminder['order_ref'],
            $reminder['payment_link']
        )
    );
}, 10, 1);
```

* * *

## Subscription Upgrades & Early Payments Pro [​](https://dev.fluentcart.com/hooks/actions/subscriptions\#subscription-upgrades-early-payments)

### ` early_payment_completed` [​](https://dev.fluentcart.com/hooks/actions/subscriptions\#early-payment-completed)

`fluent_cart/subscription/early_payment_completed`Pro - Fires when an early installment payment is completed

**When it runs:** This action fires when a customer makes an early installment payment on their subscription, paying for one or more future billing cycles ahead of schedule.

**Parameters:**

- `$data` (array): Early payment completion data
php

```
$data = [\
      'subscription'      => $subscription,      // \FluentCart\App\Models\Subscription\
      'order'             => $order,              // \FluentCart\App\Models\Order\
      'installment_count' => $installmentCount,   // int - number of installments paid early\
];
```


**Source:**`fluent-cart-pro/app/Hooks/Handlers/EarlyInstallmentPaymentHandler.php:279`

**Usage:**

php

```
add_action('fluent_cart/subscription/early_payment_completed', function ($data) {
    $subscription     = $data['subscription'];
    $order            = $data['order'];
    $installmentCount = $data['installment_count'];

    fluent_cart_add_log(
        'Early Payment Completed',
        sprintf('Subscription #%d received %d early installment(s) via order #%d', $subscription->id, $installmentCount, $order->id),
        'info'
    );
}, 10, 1);
```

### ` order_upgraded` [​](https://dev.fluentcart.com/hooks/actions/subscriptions\#order-upgraded)

`fluent_cart/order/upgraded`Pro - Fires when a plan upgrade is completed

**When it runs:** This action fires when a customer completes a plan upgrade, transitioning from one product variant to another. The upgrade creates a new order and transaction record.

**Parameters:**

- `$data` (array): Upgrade completion data
php

```
$data = [\
      'order'           => $newOrder,          // \FluentCart\App\Models\Order - the new upgrade order\
      'from_order'      => $upgradeFromOrder,  // \FluentCart\App\Models\Order - the original order\
      'cart'            => $cartModel,         // \FluentCart\App\Models\Cart - the cart used for the upgrade\
      'from_variant_id' => $fromVariantId,     // int - ID of the original product variant\
      'transaction'     => $transaction,       // \FluentCart\App\Models\OrderTransaction - the upgrade payment transaction\
];
```


**Source:**`fluent-cart-pro/app/Hooks/Handlers/UpgradeHandler.php:242`

**Usage:**

php

```
add_action('fluent_cart/order/upgraded', function ($data) {
    $order          = $data['order'];
    $fromOrder      = $data['from_order'];
    $fromVariantId  = $data['from_variant_id'];
    $transaction    = $data['transaction'];

    fluent_cart_add_log(
        'Plan Upgraded',
        sprintf(
            'Order #%d upgraded from order #%d (variant %d). Transaction: %s',
            $order->id,
            $fromOrder->id,
            $fromVariantId,
            $transaction->charge_id
        ),
        'info'
    );
}, 10, 1);
```

* * *

Today

Hi! I’m your AI assistant. How can I assist you today?

Just now

Powered by **FluentBot**


---

---

