# FluentCart Developer Docs - Hooks (Filters) (Part 2/6)

Tous les filtres WordPress exposés par FluentCart, groupés par domaine (cart & checkout, orders & payments, customers & subscriptions, products & pricing, settings & configuration, integrations & advanced).

---

## Customers & Subscriptions | FluentCart Developer Docs

**URL** : https://dev.fluentcart.com/hooks/filters/customers-and-subscriptions

[Skip to content](https://dev.fluentcart.com/hooks/filters/customers-and-subscriptions#VPContent)

# Customers & Subscriptions [​](https://dev.fluentcart.com/hooks/filters/customers-and-subscriptions\#customers-subscriptions)

All filters related to [Customer](https://dev.fluentcart.com/database/models/customer.html) management, the customer portal, [Subscription](https://dev.fluentcart.com/database/models/subscription.html) lifecycle, billing configuration, and automated reminders.

* * *

## Customer Data & Portal [​](https://dev.fluentcart.com/hooks/filters/customers-and-subscriptions\#customer-data-portal)

### ` customer/view` [​](https://dev.fluentcart.com/hooks/filters/customers-and-subscriptions\#customer-view)

`fluent_cart/customer/view` - Filter admin single customer view data

**When it runs:** This filter is applied when preparing a single customer's data for display in the admin panel.

**Parameters:**

- `$customer` ( [Customer](https://dev.fluentcart.com/database/models/customer.html)): The Customer model instance with loaded relations
php

```
$customer = [\
      'id' => 456,\
      'email' => 'customer@example.com',\
      'first_name' => 'John',\
      'last_name' => 'Doe',\
      'total_orders' => 5,\
      'total_spent' => 50000,\
      'selected_labels' => [...]\
];
```

- `$requestData` (array): The full request data from `$request->all()`

**Returns:**

- `$customer` ( [Customer](https://dev.fluentcart.com/database/models/customer.html)): The modified customer data

**Source:**`app/Http/Controllers/CustomerController.php:74`

**Usage:**

php

```
add_filter('fluent_cart/customer/view', function($customer, $requestData) {
    // Add loyalty points to customer view
    $customer['loyalty_points'] = get_user_meta($customer['user_id'], 'loyalty_points', true);
    return $customer;
}, 10, 2);
```

### ` widgets/single_customer` [​](https://dev.fluentcart.com/hooks/filters/customers-and-subscriptions\#widgets-single-customer)

`fluent_cart/widgets/single_customer` - Filter single customer admin widgets

**When it runs:** This filter is applied when loading widget data for a single customer's admin view, allowing you to inject custom widget sections.

**Parameters:**

- `$widgets` (array): Array of widget definitions (default: `[]`)
- `$customer` ( [Customer](https://dev.fluentcart.com/database/models/customer.html)): The Customer model instance

**Returns:**

- `$widgets` (array): The modified widgets array

**Source:**`app/Http/Controllers/CustomerController.php:177`

**Usage:**

php

```
add_filter('fluent_cart/widgets/single_customer', function($widgets, $customer) {
    // Add a custom CRM widget
    $widgets[] = [\
        'title' => 'CRM Notes',\
        'content' => get_user_meta($customer->user_id, 'crm_notes', true)\
    ];
    return $widgets;
}, 10, 2);
```

### ` customer_dashboard_data` [​](https://dev.fluentcart.com/hooks/filters/customers-and-subscriptions\#customer-dashboard-data)

`fluent_cart/customer_dashboard_data` - Filter customer dashboard data

**When it runs:** This filter is applied when preparing the customer portal dashboard data, including the recent orders list and section parts. Runs both when a customer exists and when no customer is found.

**Parameters:**

- `$data` (array): The dashboard response data
php

```
$data = [\
      'message' => 'Success',\
      'dashboard_data' => [\
          'orders' => [...] // Recent orders collection\
      ],\
      'sections_parts' => [\
          'before_orders_table' => '',\
          'after_orders_table' => ''\
      ]\
];
```

- `$context` (array): Context data containing the customer
php

```
$context = [\
      'customer' => $customer // Customer model or null\
];
```


**Returns:**

- `$data` (array): The modified dashboard data

**Source:**`app/Http/Controllers/FrontendControllers/CustomerProfileController.php:58,114`

**Usage:**

php

```
add_filter('fluent_cart/customer_dashboard_data', function($data, $context) {
    $customer = $context['customer'];
    if ($customer) {
        // Add a welcome banner above the orders table
        $data['sections_parts']['before_orders_table'] = '<div class="welcome-banner">Welcome back!</div>';
    }
    return $data;
}, 10, 2);
```

### ` global_customer_menu_items` [​](https://dev.fluentcart.com/hooks/filters/customers-and-subscriptions\#global-customer-menu-items)

`fluent_cart/global_customer_menu_items` - Filter customer portal menu items

**When it runs:** This filter is applied when building the customer portal sidebar navigation menu, after built-in items have been conditionally removed (e.g., subscriptions, licenses).

**Parameters:**

- `$menuItems` (array): Associative array of menu items keyed by slug
php

```
$menuItems = [\
      'orders' => [\
          'label' => 'Orders',\
          'css_class' => 'fct_route',\
          'link' => '/customer-portal/#/orders',\
          'icon_svg' => '<svg>...</svg>'\
      ],\
      'subscriptions' => [...],\
      'licenses' => [...],\
      'downloads' => [...],\
      'profile' => [...]\
];
```

- `$context` (array): Context data
php

```
$context = [\
      'base_url' => '/customer-portal/#/'\
];
```


**Returns:**

- `$menuItems` (array): The modified menu items array

**Source:**`app/Hooks/Handlers/ShortCodes/CustomerProfileHandler.php:266`

**Usage:**

php

```
add_filter('fluent_cart/global_customer_menu_items', function($menuItems, $context) {
    // Add a custom "Support" tab before "profile"
    $baseUrl = $context['base_url'];
    $menuItems['support'] = [\
        'label' => 'Support',\
        'css_class' => 'fct_route',\
        'link' => $baseUrl . 'support',\
        'icon_svg' => '<svg>...</svg>'\
    ];
    return $menuItems;
}, 10, 2);
```

### ` customer_portal/active_tab` [​](https://dev.fluentcart.com/hooks/filters/customers-and-subscriptions\#customer-portal-active-tab)

`fluent_cart/customer_portal/active_tab` - Filter the active tab in customer portal

**When it runs:** This filter is applied when rendering the customer portal to determine which tab should be visually active by default.

**Parameters:**

- `$activeTab` (string): The active tab identifier (default: `''`)

**Returns:**

- `$activeTab` (string): The modified active tab slug

**Source:**`app/Hooks/Handlers/ShortCodes/CustomerProfileHandler.php:117`

**Usage:**

php

```
add_filter('fluent_cart/customer_portal/active_tab', function($activeTab) {
    // Default to subscriptions tab
    return 'subscriptions';
}, 10, 1);
```

### ` customer_portal/custom_endpoints` [​](https://dev.fluentcart.com/hooks/filters/customers-and-subscriptions\#customer-portal-custom-endpoints)

`fluent_cart/customer_portal/custom_endpoints` - Filter custom portal endpoints

**When it runs:** This filter is applied when routing customer portal requests to check for registered custom endpoint paths. Use this to add entirely new pages to the customer portal.

**Parameters:**

- `$endpoints` (array): Associative array of custom endpoints (default: `[]`)
php

```
$endpoints = [\
      'my-page' => [\
          'render_callback' => callable,\
          // or 'page_id' => 123\
      ]\
];
```


**Returns:**

- `$endpoints` (array): The modified endpoints array

**Source:**`app/Hooks/Handlers/ShortCodes/CustomerProfileHandler.php:141`

**Usage:**

php

```
add_filter('fluent_cart/customer_portal/custom_endpoints', function($endpoints) {
    $endpoints['warranty'] = [\
        'render_callback' => function() {\
            echo '<div class="warranty-page">Warranty info here</div>';\
        }\
    ];
    return $endpoints;
}, 10, 1);
```

TIP

Consider using the `FluentCartGeneralApi::addCustomerPortalEndpoint()` helper method instead, which registers both the menu item and the endpoint in one call.

### ` customer_portal/subscription_data` [​](https://dev.fluentcart.com/hooks/filters/customers-and-subscriptions\#customer-portal-subscription-data)

`fluent_cart/customer_portal/subscription_data` - Filter customer portal subscription data

**When it runs:** This filter is applied when preparing a single subscription's data for display in the customer portal, after transactions have been loaded.

**Parameters:**

- `$formattedData` (array): The formatted subscription data including transactions
- `$context` (array): Context data
php

```
$context = [\
      'subscription' => $subscription, // Subscription model\
      'customer' => $customer           // Customer model\
];
```


**Returns:**

- `$formattedData` (array): The modified subscription data

**Source:**`app/Http/Controllers/FrontendControllers/CustomerSubscriptionController.php:157`

**Usage:**

php

```
add_filter('fluent_cart/customer_portal/subscription_data', function($formattedData, $context) {
    // Add next invoice preview
    $subscription = $context['subscription'];
    $formattedData['next_invoice_preview'] = [\
        'amount' => $subscription->recurring_amount,\
        'date' => $subscription->expiration_at\
    ];
    return $formattedData;
}, 10, 2);
```

### ` payment_methods/stripe_pub_key` [​](https://dev.fluentcart.com/hooks/filters/customers-and-subscriptions\#payment-methods-stripe-pub-key)

`fluent_cart/payment_methods/stripe_pub_key` - Filter Stripe public key for customer portal

**When it runs:** This filter is applied when localizing JavaScript data for the customer portal, providing the Stripe publishable key for client-side payment operations.

**Parameters:**

- `$pubKey` (string): The Stripe publishable key (default: `''`)

**Returns:**

- `$pubKey` (string): The modified Stripe public key

**Source:**`app/Hooks/Handlers/ShortCodes/CustomerProfileHandler.php:356`

**Usage:**

php

```
add_filter('fluent_cart/payment_methods/stripe_pub_key', function($pubKey) {
    // Override Stripe key for specific conditions
    if (defined('STRIPE_TEST_MODE') && STRIPE_TEST_MODE) {
        return 'pk_test_xxxxxxxxxxxx';
    }
    return $pubKey;
}, 10, 1);
```

### ` payment_methods/paypal_client_id` [​](https://dev.fluentcart.com/hooks/filters/customers-and-subscriptions\#payment-methods-paypal-client-id)

`fluent_cart/payment_methods/paypal_client_id` - Filter PayPal client ID for customer portal

**When it runs:** This filter is applied when localizing JavaScript data for the customer portal, providing the PayPal client ID for client-side payment operations.

**Parameters:**

- `$clientId` (string): The PayPal client ID (default: `''`)
- `$context` (array): Additional context data (default: `[]`)

**Returns:**

- `$clientId` (string): The modified PayPal client ID

**Source:**`app/Hooks/Handlers/ShortCodes/CustomerProfileHandler.php:357`

**Usage:**

php

```
add_filter('fluent_cart/payment_methods/paypal_client_id', function($clientId, $context) {
    // Provide the PayPal sandbox client ID for testing
    return 'AYourPayPalClientId';
}, 10, 2);
```

* * *

## Customer Statuses & Auth [​](https://dev.fluentcart.com/hooks/filters/customers-and-subscriptions\#customer-statuses-auth)

### ` editable_customer_statuses` [​](https://dev.fluentcart.com/hooks/filters/customers-and-subscriptions\#editable-customer-statuses)

`fluent-cart/editable_customer_statuses` - Filter editable customer statuses

**When it runs:** This filter is applied when retrieving the list of customer statuses that can be set in the admin panel.

**Parameters:**

- `$statuses` (array): Associative array of status key => label
php

```
$statuses = [\
      'active' => 'Active',\
      'inactive' => 'Inactive'\
];
```

- `$context` (array): Additional context data (default: `[]`)

**Returns:**

- `$statuses` (array): The modified statuses array

**Source:**`app/Helpers/Helper.php:162`, `app/Helpers/Status.php:350`

**Usage:**

php

```
add_filter('fluent-cart/editable_customer_statuses', function($statuses, $context) {
    // Add a "suspended" customer status
    $statuses['suspended'] = __('Suspended', 'my-plugin');
    return $statuses;
}, 10, 2);
```

Note

This hook uses a hyphen separator (`fluent-cart/`) instead of the usual underscore separator (`fluent_cart/`).

### ` user/after_register/skip_hooks` [​](https://dev.fluentcart.com/hooks/filters/customers-and-subscriptions\#user-after-register-skip-hooks)

`fluent_cart/user/after_register/skip_hooks` - Skip post-registration hooks

**When it runs:** This filter is applied after a new WordPress user has been created during checkout registration. When it returns `true`, standard WordPress post-registration hooks like `register_new_user` are skipped.

**Parameters:**

- `$skip` (bool): Whether to skip the hooks (default: `false`)
- `$user_id` (int): The newly created WordPress user ID

**Returns:**

- `$skip` (bool): Whether to skip the post-registration hooks

**Source:**`app/Services/AuthService.php:122`

**Usage:**

php

```
add_filter('fluent_cart/user/after_register/skip_hooks', function($skip, $userId) {
    // Skip default WP registration hooks to prevent welcome emails
    // when creating users during checkout
    return true;
}, 10, 2);
```

* * *

## Subscription Statuses & Configuration [​](https://dev.fluentcart.com/hooks/filters/customers-and-subscriptions\#subscription-statuses-configuration)

### ` subscription_statuses` [​](https://dev.fluentcart.com/hooks/filters/customers-and-subscriptions\#subscription-statuses)

`fluent_cart/subscription_statuses` - Filter subscription statuses

**When it runs:** This filter is applied when retrieving the list of all available subscription statuses used throughout the system.

**Parameters:**

- `$statuses` (array): Associative array of status key => label
php

```
$statuses = [\
      'pending' => 'Pending',\
      'active' => 'Active',\
      'failing' => 'Failing',\
      'paused' => 'Paused',\
      'expired' => 'Expired',\
      'expiring' => 'Expiring',\
      'canceled' => 'Canceled',\
      'trialing' => 'Trialing',\
      'intended' => 'Intended',\
      'past_due' => 'Past Due',\
      'completed' => 'Completed'\
];
```

- `$context` (array): Additional context data (default: `[]`)

**Returns:**

- `$statuses` (array): The modified subscription statuses array

**Source:**`app/Helpers/Status.php:253`

**Usage:**

php

```
add_filter('fluent_cart/subscription_statuses', function($statuses, $context) {
    // Add a custom "on_hold" status
    $statuses['on_hold'] = __('On Hold', 'my-plugin');
    return $statuses;
}, 10, 2);
```

### ` validable_subscription_statuses` [​](https://dev.fluentcart.com/hooks/filters/customers-and-subscriptions\#validable-subscription-statuses)

`fluent_cart/validable_subscription_statuses` - Filter valid (active) subscription statuses

**When it runs:** This filter is applied when determining which subscription statuses should be considered "valid" (i.e., the subscription grants access to the product/service). Used for license validation, download access, etc.

**Parameters:**

- `$statuses` (array): Array of status keys considered valid
php

```
$statuses = ['active', 'trialing'];
```

- `$context` (array): Additional context data (default: `[]`)

**Returns:**

- `$statuses` (array): The modified list of valid statuses

**Source:**`app/Helpers/Status.php:271`

**Usage:**

php

```
add_filter('fluent_cart/validable_subscription_statuses', function($statuses, $context) {
    // Also treat "expiring" subscriptions as valid until they actually expire
    $statuses[] = 'expiring';
    return $statuses;
}, 10, 2);
```

### ` subscription/view` [​](https://dev.fluentcart.com/hooks/filters/customers-and-subscriptions\#subscription-view)

`fluent_cart/subscription/view` - Filter admin subscription view data

**When it runs:** This filter is applied when preparing a single subscription's data for display in the admin panel.

**Parameters:**

- `$subscription` ( [Subscription](https://dev.fluentcart.com/database/models/subscription.html)): The Subscription model with loaded relations
- `$context` (array): Additional context data (default: `[]`)

**Returns:**

- `$subscription` (array): The modified subscription data

**Source:**`app/Modules/Subscriptions/Http/Controllers/SubscriptionController.php:63`

**Usage:**

php

```
add_filter('fluent_cart/subscription/view', function($subscription, $context) {
    // Add external gateway link
    $subscription['external_url'] = 'https://dashboard.stripe.com/subscriptions/' . $subscription['vendor_subscription_id'];
    return $subscription;
}, 10, 2);
```

### ` subscription/url_{$payment_method}` [​](https://dev.fluentcart.com/hooks/filters/customers-and-subscriptions\#subscription-url-payment-method)

`fluent_cart/subscription/url_{$payment_method}` - Filter vendor dashboard URL for a subscription (dynamic)

**When it runs:** This filter is applied when generating the external vendor dashboard URL for a subscription. The hook name is dynamic, with `{$payment_method}` replaced by the subscription's current payment method (e.g., `stripe`, `paypal`).

**Parameters:**

- `$url` (string): The vendor dashboard URL (default: `''`)
- `$context` (array): Context data
php

```
$context = [\
      'vendor_subscription_id' => 'sub_1234567890',\
      'payment_mode' => 'live', // or 'test'\
      'subscription' => $subscription // Subscription model\
];
```


**Returns:**

- `$url` (string): The modified vendor dashboard URL

**Source:**`app/Models/Subscription.php:158`

**Usage:**

php

```
// Provide the Stripe dashboard URL for subscriptions
add_filter('fluent_cart/subscription/url_stripe', function($url, $context) {
    $subId = $context['vendor_subscription_id'];
    $mode = $context['payment_mode'];
    $base = ($mode === 'test')
        ? 'https://dashboard.stripe.com/test'
        : 'https://dashboard.stripe.com';
    return $base . '/subscriptions/' . $subId;
}, 10, 2);
```

### ` subscription/can_reactivate` [​](https://dev.fluentcart.com/hooks/filters/customers-and-subscriptions\#subscription-can-reactivate)

`fluent_cart/subscription/can_reactivate` - Filter whether a subscription can be reactivated

**When it runs:** This filter is applied when checking if a canceled, failing, expired, paused, expiring, or past-due subscription is eligible for reactivation.

**Parameters:**

- `$canReactivate` (bool): Whether the subscription can be reactivated (based on its current status)
- `$context` (array): Context data
php

```
$context = [\
      'subscription' => $subscription // Subscription model\
];
```


**Returns:**

- `$canReactivate` (bool): The modified reactivation eligibility

**Source:**`app/Models/Subscription.php:427`

**Usage:**

php

```
add_filter('fluent_cart/subscription/can_reactivate', function($canReactivate, $context) {
    $subscription = $context['subscription'];

    // Prevent reactivation if canceled more than 90 days ago
    if ($subscription->status === 'canceled') {
        $canceledAt = strtotime($subscription->updated_at);
        if ((time() - $canceledAt) > (90 * DAY_IN_SECONDS)) {
            return false;
        }
    }
    return $canReactivate;
}, 10, 2);
```

### ` available_subscription_interval_options` [​](https://dev.fluentcart.com/hooks/filters/customers-and-subscriptions\#available-subscription-interval-options)

`fluent_cart/available_subscription_interval_options` - Filter subscription interval options

**When it runs:** This filter is applied when retrieving the list of available subscription billing interval options for product configuration.

**Parameters:**

- `$intervals` (array): Array of interval option objects
php

```
$intervals = [\
      ['label' => 'Yearly', 'value' => 'yearly', 'map_value' => 'year'],\
      ['label' => 'Half Yearly', 'value' => 'half_yearly', 'map_value' => 'half_year'],\
      ['label' => 'Quarterly', 'value' => 'quarterly', 'map_value' => 'quarter'],\
      ['label' => 'Monthly', 'value' => 'monthly', 'map_value' => 'month'],\
      ['label' => 'Weekly', 'value' => 'weekly', 'map_value' => 'week'],\
      ['label' => 'Daily', 'value' => 'daily', 'map_value' => 'day']\
];
```


**Returns:**

- `$intervals` (array): The modified intervals array

**Source:**`app/Helpers/Helper.php:1531`

**Usage:**

php

```
add_filter('fluent_cart/available_subscription_interval_options', function($intervals) {
    // Add a custom "Every 10 days" interval
    $intervals[] = [\
        'label' => __('Every 10th Day', 'my-plugin'),\
        'value' => 'every_tenth_day',\
        'map_value' => '10th Day'\
    ];
    return $intervals;
});
```

TIP

When adding custom intervals, you must also implement the `fluent_cart/subscription_interval_in_days` and `fluent_cart/subscription_billing_period` filters so the system knows how to calculate dates and communicate with payment gateways.

### ` subscription_interval_in_days` [​](https://dev.fluentcart.com/hooks/filters/customers-and-subscriptions\#subscription-interval-in-days)

`fluent_cart/subscription_interval_in_days` - Filter the number of days for a custom subscription interval

**When it runs:** This filter is applied when converting a subscription interval to its day count. For built-in intervals (yearly, half\_yearly, quarterly, monthly, weekly, daily), the value is calculated automatically. This filter fires for custom/unknown intervals with a default of `0`.

**Parameters:**

- `$days` (int): Number of days for the interval (default: `0` for custom intervals)
- `$context` (array): Context data
php

```
$context = [\
      'interval' => 'every_tenth_day' // The interval key\
];
```


**Returns:**

- `$days` (int): The number of days in this interval

**Source:**`app/Helpers/Helper.php:1592`, `app/Services/Payments/PaymentHelper.php:236`

**Usage:**

php

```
add_filter('fluent_cart/subscription_interval_in_days', function($days, $args) {
    $interval = $args['interval'];

    if ($interval === 'every_tenth_day') {
        return 10;
    }

    if ($interval === 'biweekly') {
        return 14;
    }

    return $days;
}, 10, 2);
```

### ` max_trial_days_allowed` [​](https://dev.fluentcart.com/hooks/filters/customers-and-subscriptions\#max-trial-days-allowed)

`fluent_cart/max_trial_days_allowed` - Filter maximum trial days allowed

**When it runs:** This filter is applied when calculating adjusted trial days for a subscription interval. The system ensures the trial period does not exceed this maximum.

**Parameters:**

- `$maxDays` (int): Maximum trial days allowed (default: `365`)
- `$context` (array): Context data
php

```
$context = [\
      'existing_trial_days' => 14,\
      'repeat_interval' => 'monthly',\
      'interval_in_days' => 30\
];
```


**Returns:**

- `$maxDays` (int): The modified maximum trial days

**Source:**`app/Helpers/Helper.php:1566`

**Usage:**

php

```
add_filter('fluent_cart/max_trial_days_allowed', function($maxDays, $args) {
    // Cap trials at 30 days for monthly subscriptions
    if ($args['repeat_interval'] === 'monthly') {
        return 30;
    }
    return $maxDays;
}, 10, 2);
```

### ` trial_info` [​](https://dev.fluentcart.com/hooks/filters/customers-and-subscriptions\#trial-info)

`fluent_cart/trial_info` - Filter trial info display text

**When it runs:** This filter is applied when generating the human-readable trial information text shown to customers (e.g., "Free Trial: 14 days").

**Parameters:**

- `$trialInfo` (string): The generated trial info text (e.g., `'Free Trial: 14 days'` or `''` if no trial)
- `$otherInfo` (array): The product/variant pricing metadata
php

```
$otherInfo = [\
      'trial_days' => 14,\
      'is_trial_days_simulated' => 'no',\
      'signup_fee' => 0,\
      'manage_setup_fee' => 'no',\
      // ... other pricing info\
];
```


**Returns:**

- `$trialInfo` (string): The modified trial info text

**Source:**`app/Helpers/Helper.php:1133`

**Usage:**

php

```
add_filter('fluent_cart/trial_info', function($trialInfo, $otherInfo) {
    $days = $otherInfo['trial_days'] ?? 0;
    if ($days > 0) {
        return sprintf('Try free for %d days - no credit card required!', $days);
    }
    return $trialInfo;
}, 10, 2);
```

* * *

## Subscription Billing [​](https://dev.fluentcart.com/hooks/filters/customers-and-subscriptions\#subscription-billing)

### ` subscription_billing_period` [​](https://dev.fluentcart.com/hooks/filters/customers-and-subscriptions\#subscription-billing-period)

`fluent_cart/subscription_billing_period` - Filter billing period for payment gateways

**When it runs:** This filter is applied when translating a FluentCart subscription interval into the payment gateway's billing period format (used by Stripe Plans and PayPal billing cycles).

**Parameters:**

- `$billingPeriod` (array): The billing period for the gateway
php

```
$billingPeriod = [\
      'interval_unit' => 'month',      // day, week, month, year\
      'interval_frequency' => 1         // e.g., 3 for quarterly\
];
```

- `$context` (array): Context data
php

```
$context = [\
      'subscription_interval' => 'quarterly', // Original FluentCart interval\
      'payment_method' => 'stripe'             // or 'paypal'\
];
```


**Returns:**

- `$billingPeriod` (array): The modified billing period

**Source:**`app/Modules/PaymentMethods/StripeGateway/Plan.php:58`, `app/Modules/PaymentMethods/PayPalGateway/PayPalHelper.php:243`

**Usage:**

php

```
add_filter('fluent_cart/subscription_billing_period', function($billingPeriod, $args) {
    $interval = $args['subscription_interval'];
    $method = $args['payment_method'];

    if ($interval === 'every_tenth_day') {
        if ($method === 'stripe') {
            return [\
                'interval_unit' => 'day',\
                'interval_frequency' => 10\
            ];
        }
        if ($method === 'paypal') {
            return [\
                'interval_unit' => 'DAY',\
                'interval_frequency' => 10\
            ];
        }
    }

    return $billingPeriod;
}, 10, 2);
```

### ` subscription/grace_period_days` [​](https://dev.fluentcart.com/hooks/filters/customers-and-subscriptions\#subscription-grace-period-days)

`fluent_cart/subscription/grace_period_days` - Filter grace period days per billing interval

**When it runs:** This filter is applied when retrieving the grace period (number of extra days after a payment fails before the subscription is marked as expired) for each billing interval.

**Parameters:**

- `$gracePeriods` (array): Associative array of interval => days
php

```
$gracePeriods = [\
      'daily' => 1,\
      'weekly' => 3,\
      'monthly' => 7,\
      'quarterly' => 15,\
      'half_yearly' => 15,\
      'yearly' => 15\
];
```


**Returns:**

- `$gracePeriods` (array): The modified grace period days

**Source:**`app/Services/Payments/SubscriptionHelper.php:159`

**Usage:**

php

```
add_filter('fluent_cart/subscription/grace_period_days', function($gracePeriods) {
    // Give yearly subscribers more time
    $gracePeriods['yearly'] = 30;

    // Add grace period for custom interval
    $gracePeriods['every_tenth_day'] = 5;

    return $gracePeriods;
});
```

* * *

## Reminders [​](https://dev.fluentcart.com/hooks/filters/customers-and-subscriptions\#reminders)

### ` reminders/scan_batch_size` [​](https://dev.fluentcart.com/hooks/filters/customers-and-subscriptions\#reminders-scan-batch-size)

`fluent_cart/reminders/scan_batch_size` - Filter reminder scan batch size

**When it runs:** This filter is applied when the automated reminder system scans for subscriptions or invoices that need reminders. Controls how many records are processed per batch.

**Parameters:**

- `$batchSize` (int): Number of records per scan batch (default: `100`, min: `10`, max: `500`)

**Returns:**

- `$batchSize` (int): The modified batch size

**Source:**`app/Services/Reminders/ReminderService.php:75`

**Usage:**

php

```
add_filter('fluent_cart/reminders/scan_batch_size', function($batchSize) {
    // Process more records per batch on high-traffic sites
    return 250;
});
```

### ` reminders/invoice_due_days` [​](https://dev.fluentcart.com/hooks/filters/customers-and-subscriptions\#reminders-invoice-due-days)

`fluent_cart/reminders/invoice_due_days` - Filter invoice due reminder days

**When it runs:** This filter is applied when determining how many days before an invoice is due to send a reminder. The value comes from store settings but can be overridden.

**Parameters:**

- `$days` (int): Number of days before due date to send reminder (from store settings, min: `0`)

**Returns:**

- `$days` (int): The modified number of days

**Source:**`app/Services/Reminders/InvoiceReminderService.php:288`

**Usage:**

php

```
add_filter('fluent_cart/reminders/invoice_due_days', function($days) {
    // Always remind 3 days before invoice is due
    return 3;
});
```

### ` reminders/invoice_overdue_days` [​](https://dev.fluentcart.com/hooks/filters/customers-and-subscriptions\#reminders-invoice-overdue-days)

`fluent_cart/reminders/invoice_overdue_days` - Filter overdue invoice reminder intervals

**When it runs:** This filter is applied when determining at which day intervals after an invoice becomes overdue to send follow-up reminders.

**Parameters:**

- `$days` (array): Array of day intervals for overdue reminders (default from settings: `[1, 3, 7]`)

**Returns:**

- `$days` (array): The modified array of overdue reminder day intervals

**Source:**`app/Services/Reminders/InvoiceReminderService.php:299`

**Usage:**

php

```
add_filter('fluent_cart/reminders/invoice_overdue_days', function($days) {
    // Send overdue reminders at 1, 3, 7, and 14 days past due
    return [1, 3, 7, 14];
});
```

### ` reminders/billing_cycle` [​](https://dev.fluentcart.com/hooks/filters/customers-and-subscriptions\#reminders-billing-cycle)

`fluent_cart/reminders/billing_cycle` - Filter billing cycle name for reminder processing

**When it runs:** This filter is applied when mapping a subscription's billing interval to a billing cycle identifier used by the reminder system. Returns `'unsupported'` for unknown intervals by default.

**Parameters:**

- `$cycle` (string): The billing cycle name (e.g., `'monthly'`, `'yearly'`, `'unsupported'`)
- `$subscription` ( [Subscription](https://dev.fluentcart.com/database/models/subscription.html)): The Subscription model instance

**Returns:**

- `$cycle` (string): The modified billing cycle name

**Source:**`app/Services/Reminders/SubscriptionReminderService.php:502`

**Usage:**

php

```
add_filter('fluent_cart/reminders/billing_cycle', function($cycle, $subscription) {
    // Map custom intervals to supported reminder cycles
    if ($subscription->billing_interval === 'every_tenth_day') {
        return 'daily'; // Use daily reminder logic
    }
    return $cycle;
}, 10, 2);
```

### ` reminders/yearly_before_days` [​](https://dev.fluentcart.com/hooks/filters/customers-and-subscriptions\#reminders-yearly-before-days)

`fluent_cart/reminders/yearly_before_days` - Filter days before yearly renewal reminder

**When it runs:** This filter is applied when determining at which day intervals before a yearly subscription renewal to send reminders.

**Parameters:**

- `$days` (array): Array of day intervals before renewal (default from settings: `[30]`, range: 7-90)

**Returns:**

- `$days` (array): The modified array of reminder day intervals

**Source:**`app/Services/Reminders/SubscriptionReminderService.php:534`

**Usage:**

php

```
add_filter('fluent_cart/reminders/yearly_before_days', function($days) {
    // Remind at 60, 30, and 7 days before yearly renewal
    return [60, 30, 7];
});
```

### ` reminders/monthly_before_days` [​](https://dev.fluentcart.com/hooks/filters/customers-and-subscriptions\#reminders-monthly-before-days)

`fluent_cart/reminders/monthly_before_days` - Filter days before monthly renewal reminder

**When it runs:** This filter is applied when determining at which day intervals before a monthly subscription renewal to send reminders.

**Parameters:**

- `$days` (array): Array of day intervals before renewal (default from settings: `[7]`, range: 3-28)

**Returns:**

- `$days` (array): The modified array of reminder day intervals

**Source:**`app/Services/Reminders/SubscriptionReminderService.php:546`

**Usage:**

php

```
add_filter('fluent_cart/reminders/monthly_before_days', function($days) {
    // Remind at 7 and 3 days before monthly renewal
    return [7, 3];
});
```

### ` reminders/quarterly_before_days` [​](https://dev.fluentcart.com/hooks/filters/customers-and-subscriptions\#reminders-quarterly-before-days)

`fluent_cart/reminders/quarterly_before_days` - Filter days before quarterly renewal reminder

**When it runs:** This filter is applied when determining at which day intervals before a quarterly subscription renewal to send reminders.

**Parameters:**

- `$days` (array): Array of day intervals before renewal (default from settings: `[14]`, range: 7-60)

**Returns:**

- `$days` (array): The modified array of reminder day intervals

**Source:**`app/Services/Reminders/SubscriptionReminderService.php:558`

**Usage:**

php

```
add_filter('fluent_cart/reminders/quarterly_before_days', function($days) {
    // Remind at 21 and 7 days before quarterly renewal
    return [21, 7];
});
```

### ` reminders/half_yearly_before_days` [​](https://dev.fluentcart.com/hooks/filters/customers-and-subscriptions\#reminders-half-yearly-before-days)

`fluent_cart/reminders/half_yearly_before_days` - Filter days before half-yearly renewal reminder

**When it runs:** This filter is applied when determining at which day intervals before a half-yearly subscription renewal to send reminders.

**Parameters:**

- `$days` (array): Array of day intervals before renewal (default from settings: `[21]`, range: 7-60)

**Returns:**

- `$days` (array): The modified array of reminder day intervals

**Source:**`app/Services/Reminders/SubscriptionReminderService.php:570`

**Usage:**

php

```
add_filter('fluent_cart/reminders/half_yearly_before_days', function($days) {
    // Remind at 30 and 7 days before half-yearly renewal
    return [30, 7];
});
```

### ` reminders/trial_end_days` [​](https://dev.fluentcart.com/hooks/filters/customers-and-subscriptions\#reminders-trial-end-days)

`fluent_cart/reminders/trial_end_days` - Filter days before trial end reminder

**When it runs:** This filter is applied when determining at which day intervals before a trial period ends to send reminders to the customer.

**Parameters:**

- `$days` (array): Array of day intervals before trial ends (default from settings: `[3]`, range: 1-14)

**Returns:**

- `$days` (array): The modified array of reminder day intervals

**Source:**`app/Services/Reminders/SubscriptionReminderService.php:582`

**Usage:**

php

```
add_filter('fluent_cart/reminders/trial_end_days', function($days) {
    // Remind at 7, 3, and 1 day before trial ends
    return [7, 3, 1];
});
```

* * *

## Pro: Early Payments & Reactivation [​](https://dev.fluentcart.com/hooks/filters/customers-and-subscriptions\#pro-early-payments-reactivation)

### ` subscription/early_payment_enabled` [​](https://dev.fluentcart.com/hooks/filters/customers-and-subscriptions\#subscription-early-payment-enabled)

`fluent_cart/subscription/early_payment_enabled`Pro - Filter whether early installment payments are enabled

**When it runs:** This filter is applied when checking if the early payment feature for installment subscriptions is globally enabled. Requires FluentCart Pro to be active.

**Parameters:**

- `$isEnabled` (bool): Whether early payments are enabled (from store settings `enable_early_payment_for_installment`)

**Returns:**

- `$isEnabled` (bool): The modified enabled state

**Source:**`app/Modules/Subscriptions/Services/EarlyPaymentFeature.php:14`

**Usage:**

php

```
add_filter('fluent_cart/subscription/early_payment_enabled', function($isEnabled) {
    // Disable early payments during a specific promotion period
    if (current_time('Y-m') === '2026-12') {
        return false;
    }
    return $isEnabled;
});
```

### ` subscription/can_early_pay` [​](https://dev.fluentcart.com/hooks/filters/customers-and-subscriptions\#subscription-can-early-pay)

`fluent_cart/subscription/can_early_pay`Pro - Filter whether a specific subscription can make an early payment

**When it runs:** This filter is applied when checking if a specific installment subscription is eligible for early payment. The default check requires that early payments are globally enabled, the subscription has a finite bill count, there are remaining installments, and the subscription status is `active` or `trialing`.

**Parameters:**

- `$canPay` (bool): Whether the subscription can make an early payment
- `$context` (array): Context data
php

```
$context = [\
      'subscription' => $subscription // Subscription model\
];
```


**Returns:**

- `$canPay` (bool): The modified eligibility

**Source:**`app/Modules/Subscriptions/Services/EarlyPaymentFeature.php:26`

**Usage:**

php

```
add_filter('fluent_cart/subscription/can_early_pay', function($canPay, $context) {
    $subscription = $context['subscription'];

    // Only allow early payments for subscriptions with more than 2 remaining installments
    $remaining = $subscription->bill_times - $subscription->bill_count;
    if ($remaining <= 2) {
        return false;
    }

    return $canPay;
}, 10, 2);
```

### ` subscription/reactivation_same_price_days_limit` [​](https://dev.fluentcart.com/hooks/filters/customers-and-subscriptions\#subscription-reactivation-same-price-days-limit)

`fluent_cart/subscription/reactivation_same_price_days_limit`Pro - Filter days limit for same-price reactivation

**When it runs:** This filter is applied when a customer reactivates a canceled or expired subscription. If the subscription was canceled within this many days, the customer can reactivate at the original price without going through a new checkout.

**Parameters:**

- `$daysLimit` (int): Number of days within which same-price reactivation is allowed (default: `60`)
- `$context` (array): Context data
php

```
$context = [\
      'subscription' => $subscription // Subscription model\
];
```


**Returns:**

- `$daysLimit` (int): The modified days limit

**Source:**`fluent-cart-pro/.../SubscriptionRenewalHandler.php:234`

**Usage:**

php

```
add_filter('fluent_cart/subscription/reactivation_same_price_days_limit', function($daysLimit, $context) {
    $subscription = $context['subscription'];

    // Give yearly subscribers a longer reactivation window
    if ($subscription->billing_interval === 'yearly') {
        return 180; // 6 months
    }

    return $daysLimit;
}, 10, 2);
```

* * *

## Pro: License Customer Portal [​](https://dev.fluentcart.com/hooks/filters/customers-and-subscriptions\#pro-license-customer-portal)

### ` customer/license_details_section_parts` [​](https://dev.fluentcart.com/hooks/filters/customers-and-subscriptions\#customer-license-details-section-parts)

`fluent_cart/customer/license_details_section_parts`Pro - Filter license details section parts in customer portal

**When it runs:** This filter is applied when rendering a license details page in the customer portal, allowing you to inject custom HTML into specific sections of the license view.

**Parameters:**

- `$sectionParts` (array): Associative array of injectable HTML sections
php

```
$sectionParts = [\
      'before_summary' => '',\
      'after_summary' => '',\
      'end_of_details' => '',\
      'additional_actions' => ''\
];
```

- `$context` (array): Context data
php

```
$context = [\
      'license' => $license,          // License model\
      'formattedData' => $formattedData // Formatted license data for display\
];
```


**Returns:**

- `$sectionParts` (array): The modified section parts

**Source:**`fluent-cart-pro/.../CustomerProfileController.php:97`

**Usage:**

php

```
add_filter('fluent_cart/customer/license_details_section_parts', function($parts, $context) {
    $license = $context['license'];

    // Add activation instructions after the summary
    $parts['after_summary'] = '<div class="activation-guide">'
        . '<h4>How to Activate</h4>'
        . '<p>Copy your license key and paste it in your plugin settings.</p>'
        . '</div>';

    // Add a custom action button
    $parts['additional_actions'] = '<button class="btn-regenerate" onclick="regenerateLicense(\'' . $license->id . '\')">Regenerate Key</button>';

    return $parts;
}, 10, 2);
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

