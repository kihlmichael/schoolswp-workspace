# FluentCart Developer Docs - Payment Gateway Integration (Part 1/2)

Guide complet pour intégrer une nouvelle passerelle de paiement à FluentCart (overview, quick implementation, payment setting fields, exemple Paddle).

---

## Payment Gateway Integration | FluentCart Developer Docs

**URL** : https://dev.fluentcart.com/payment-methods-integration/

[Skip to content](https://dev.fluentcart.com/payment-methods-integration/#VPContent)

# Payment Gateway Integration [​](https://dev.fluentcart.com/payment-methods-integration/\#payment-gateway-integration)

Build and integrate custom payment gateways with FluentCart to extend payment processing capabilities beyond the built-in options. This guide provides everything third-party developers need to create robust payment integrations.

## Overview [​](https://dev.fluentcart.com/payment-methods-integration/\#overview)

FluentCart's payment gateway system is designed for extensibility, allowing developers to integrate any payment processor while maintaining consistent user experience and following WordPress best practices.

## Live example [​](https://dev.fluentcart.com/payment-methods-integration/\#live-example)

You can test our live PayStack integration ( [https://github.com/WPManageNinja/paystack-for-fluent-cart](https://github.com/WPManageNinja/paystack-for-fluent-cart)). available with full source code and detailed documentation on how to integrate any custom payment gateway.

### What You'll Learn [​](https://dev.fluentcart.com/payment-methods-integration/\#what-you-ll-learn)

- **Gateway Architecture** \- Understanding FluentCart's payment system structure
- **Implementation Steps** \- Step-by-step guide to building a payment gateway
- **Integration Methods** \- How to register and hook into FluentCart
- **Custom Event System** \- How to use FluentCart's custom events for payment method integration
- **Real-world Example** \- Based on the Paddle Gateway implementation
- **Best Practices** \- Security, error handling, and WordPress standards

### Prerequisites [​](https://dev.fluentcart.com/payment-methods-integration/\#prerequisites)

- PHP 7.4+ and WordPress development experience
- Understanding of payment gateway APIs and webhooks
- Basic knowledge of FluentCart structure
- Access to your payment processor's API documentation

## Quick Start [​](https://dev.fluentcart.com/payment-methods-integration/\#quick-start)

Here's a minimal example to get you started:

php

```
<?php
namespace YourPlugin\PaymentMethods\YourGateway;

use FluentCart\App\Modules\PaymentMethods\Core\AbstractPaymentGateway;
use FluentCart\App\Services\Payments\PaymentInstance;

class YourGateway extends AbstractPaymentGateway
{
    public array $supportedFeatures = ['payment', 'refund', 'webhook'];

    public function __construct()
    {
        parent::__construct(new YourGatewaySettings());
    }

    public function meta(): array
    {
        return [\
            'title' => __('Your Gateway', 'your-plugin'),\
            'route' => 'your_gateway',\
            'slug' => 'your_gateway',\
            'description' => __('Accept payments with Your Gateway', 'your-plugin'),\
            'status' => $this->settings->get('is_active') === 'yes',\
        ];
    }

    public function makePaymentFromPaymentInstance(PaymentInstance $paymentInstance)
    {
        // Your payment processing logic here
        return [\
            'success' => true,\
            'redirect_url' => 'https://your-gateway.com/checkout/...'\
        ];
    }
}

// Register the gateway
add_action('fluent_cart/register_payment_methods', function() {
    fluent_cart_api()->registerCustomPaymentMethod('your_gateway', new YourGateway());
});
```

## Core Concepts [​](https://dev.fluentcart.com/payment-methods-integration/\#core-concepts)

### Gateway Manager [​](https://dev.fluentcart.com/payment-methods-integration/\#gateway-manager)

FluentCart uses a centralized `GatewayManager` to handle all payment gateways:

php

```
// Get a specific gateway
$gateway = App::gateway('your_gateway');

// Check if gateway exists
if (GatewayManager::has('your_gateway')) {
    // Gateway is registered
}

// Get all gateways
$allGateways = GatewayManager::getInstance()->all();
```

### Frontend Integration with Custom Events [​](https://dev.fluentcart.com/payment-methods-integration/\#frontend-integration-with-custom-events)

FluentCart uses a custom event system to load payment methods in the checkout page. When a customer selects a payment method, FluentCart triggers a custom event in the format:

```
fluent_cart_load_payments_[payment_method_slug]
```

Your JavaScript file should listen for this event and handle the payment process. Here's a simple example:

javascript

```
// Example for a simple payment method (like Cash on Delivery)
window.addEventListener("fluent_cart_load_payments_your_gateway", function (e) {
    const submitButton = window.fluentcart_checkout_vars?.submit_button;
    const gatewayContainer = document.querySelector('.fluent-cart-checkout_embed_payment_container_your_gateway');

    // Simple implementation
    if (gatewayContainer) {
        gatewayContainer.innerHTML = '<p>Your payment instructions here.</p>';
    }

    // Enable the checkout button
    e.detail.paymentLoader.enableCheckoutButton(submitButton.text);
});
```

The event object provides these important properties:

- `e.detail.form` \- The checkout form element
- `e.detail.paymentLoader` \- Helper object to manage checkout button state
- `e.detail.paymentInfoUrl` \- URL to fetch payment information
- `e.detail.nonce` \- WordPress nonce for secure API calls

### Payment Flow [​](https://dev.fluentcart.com/payment-methods-integration/\#payment-flow)

1. **Registration** \- Gateway registers with FluentCart
2. **Configuration** \- Admin configures gateway settings
3. **Payment Processing** \- Customer initiates payment
4. **Webhook Handling** \- Gateway processes payment confirmations
5. **Order Completion** \- FluentCart updates order status

## Next Steps [​](https://dev.fluentcart.com/payment-methods-integration/\#next-steps)

- **[Complete Integration](https://dev.fluentcart.com/payment-methods-integration/quick-implementation.html)** \- Step by step guide to integrate custom payment methods with fluent-cart
- **[Payment Gateway Settings Fields](https://dev.fluentcart.com/payment-methods-integration/payment_setting_fields.html)** \- Detailed guide to build settings fields for your custom payment gateway

## Examples [​](https://dev.fluentcart.com/payment-methods-integration/\#examples)

- **[Paddle Gateway Case Study](https://dev.fluentcart.com/payment-methods-integration/paddle-example.html)** \- Real implementation analysis

* * *

**Need Help?** Check out the [FluentCart Core Payment Methods](https://dev.fluentcart.com/modules/payment-methods.html) documentation for deeper technical details.

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

## Implementation Guide | FluentCart Developer Docs

**URL** : https://dev.fluentcart.com/payment-methods-integration/quick-implementation

[Skip to content](https://dev.fluentcart.com/payment-methods-integration/quick-implementation#VPContent)

# Payment Gateway Integration Guide [​](https://dev.fluentcart.com/payment-methods-integration/quick-implementation\#payment-gateway-integration-guide)

This guide provides a step-by-step approach to integrate your payment gateway with FluentCart. Follow these steps to create a fully functional payment gateway with support for one-time payments, subscriptions, and web hooks.

## Implementation Steps [​](https://dev.fluentcart.com/payment-methods-integration/quick-implementation\#implementation-steps)

### Step 1: Register Your Gateway [​](https://dev.fluentcart.com/payment-methods-integration/quick-implementation\#step-1-register-your-gateway)

In your plugin's main file, register your gateway with FluentCart using the hook approach (recommended):

php

```
// In your-plugin.php
add_action('fluent_cart/register_payment_methods', function() {
    if (!function_exists('fluent_cart_api')) {
        return; // FluentCart not active
    }

    // Register your custom gateway
    fluent_cart_api()->registerCustomPaymentMethod(
        'your_gateway',
        new \YourPlugin\PaymentMethods\YourGateway\YourGateway()
    );
});
```

Alternatively, you can register on the `init` hook (not recommended):

php

```
add_action('init', function() {
    if (!function_exists('fluent_cart_api')) {
        return;
    }
    fluent_cart_api()->registerCustomPaymentMethod('your_gateway', new \YourPlugin\PaymentMethods\YourGateway\YourGateway());
});
```

### Step 2: Create the Settings Class [​](https://dev.fluentcart.com/payment-methods-integration/quick-implementation\#step-2-create-the-settings-class)

Create a settings class that extends `BaseGatewaySettings`:

php

```
<?php
namespace YourPlugin\PaymentMethods\YourGateway;

use FluentCart\App\Modules\PaymentMethods\Core\BaseGatewaySettings;
use FluentCart\App\Helpers\Helper;

class YourGatewaySettings extends BaseGatewaySettings
{
    public $methodHandler = 'fluent_cart_payment_settings_your_gateway';

    public static function getDefaults()
    {
        return [\
            'is_active' => 'no',\
            'payment_mode' => 'test', // test or live\
            'test_api_key' => '',\
            'test_secret_key' => '',\
            'live_api_key' => '',\
            'live_secret_key' => '',\
        ];
    }

    public function getApiKey()
    {
        $mode = $this->get('payment_mode');
        return $this->get($mode . '_api_key');
    }

    public function getSecretKey()
    {
        $mode = $this->get('payment_mode');
        return Helper::decryptKey($this->get($mode . '_secret_key'));
    }

    public function isTestMode()
    {
        return $this->get('payment_mode') === 'test';
    }
}
```

### Step 3: Create your Gateway Class [​](https://dev.fluentcart.com/payment-methods-integration/quick-implementation\#step-3-create-your-gateway-class)

Create base class that implements all required methods:

php

```
<?php
namespace YourPlugin\PaymentMethods\YourGateway;

use FluentCart\App\Modules\PaymentMethods\Core\AbstractPaymentGateway;
use FluentCart\App\Services\Payments\PaymentInstance;
use FluentCart\Framework\Support\Arr;

class YourGateway extends AbstractPaymentGateway
{
    // Define supported features
    public array $supportedFeatures = [\
        'payment',\
        'webhook',\
        'refund',\
        'subscriptions'\
    ];


    public function __construct()
    {
        // Initialize settings
        parent::__construct(new YourGatewaySettings());

    }

    public function boot()
    {
        // initialize any hanldere, webhook/ payment confirmation class if needed
    }

    #equired: Return gateway metadata
    public function meta(): array
    {
        return [\
            'title' => __('Your Gateway', 'your-plugin'),\
            'route' => 'your_gateway',\
            'slug' => 'your_gateway',\
            'description' => __('Accept payments with Your Gateway', 'your-plugin'),\
            'logo' => plugin_dir_url(__FILE__) .\
                'assets/images/logo.svg',\
            'icon' => plugin_dir_url(__FILE__) .\
                'assets/images/icon.svg',\
            'status' => $this->settings->get('is_active') === 'yes',\
            'supported_features' => $this->supportedFeatures\
        ];
    }

    #equired: Check if gateway supports a feature
    public function has(string $feature): bool
    {
        return in_array($feature, $this->supportedFeatures);
    }

    // Required: Process payment
    public function makePaymentFromPaymentInstance(PaymentInstance $paymentInstance)
    {
        // Your payment processing logic here

    }

    // Required: Handle IPNs/Webhooks
    public function handleIPN()
    {
        // Process the webhook

    }


    #required: Return settings fields configuration
    public function fields(): array
    {
        // For a comprehensive guide on building gateway settings fields,
        // see the detailed [Payment Gateway Settings Fields] documentation link given below
        return [\
            ....\
        ];
    }

    // For a comprehensive guide on building gateway settings fields,
    // see the detailed documentation: [Payment Gateway Settings Fields](./payment_setting_fields.md)

    #required: Get order information for frontend
    public function getOrderInfo(array $data)
    {
        // Prepare frontend data for checkout
        $paymentArgs = [];

        // Return data for frontend
        wp_send_json([\
            'status' => 'success',\
            'payment_args' => $paymentArgs,\
            'message' => __('Order info retrieved', 'your-plugin')\
        ], 200);
    }

    #required: Register scripts (automatically called by base gateway)
    public function getEnqueueScriptSrc($hasSubscription = 'no'): array
    {
        // External gateway library, custom checkout scripts (if needed), otherwise return empty array
        $gatewayLibUrl = 'https://js.yourgateway.com/v1/checkout.js';

        return [\
            [\
                'handle' => 'your-gateway-external-lib',\
                'src' => $gatewayLibUrl,\
            ],\
            [\
                'handle' => 'fluent-cart-your-gateway-checkout',\
                'src' => plugin_dir_url(__FILE__) . 'assets/js/your-gateway-checkout.js',\
                'deps' => ['your-gateway-external-lib'],\
                'version' => FLUENTCART_PLUGIN_VERSION\
            ]\
        ];
    }
}
```

#### fields() method setup [​](https://dev.fluentcart.com/payment-methods-integration/quick-implementation\#fields-method-setup)

For a comprehensive guide on building gateway settings fields, see the detailed documentation: [Payment Gateway Settings Fields](https://dev.fluentcart.com/payment-methods-integration/payment_setting_fields.html)

Now your gateway registration is done, you will see your gateway in the payment methods list in FluentCart admin dashboard. And if you follow the [Fields](https://dev.fluentcart.com/payment-methods-integration/payment_setting_fields.html) guide and Configure your gateway settings and save with **Payment activation** on, you will see the gateway in the payment methods list in FluentCart checkout page.

### Step 4: Create JavaScript File for Frontend Checkout [​](https://dev.fluentcart.com/payment-methods-integration/quick-implementation\#step-4-create-javascript-file-for-frontend-checkout)

FluentCart uses a custom event system to load payment methods in the checkout page. When a customer selects your payment method, FluentCart triggers a custom event in the format: `fluent_cart_load_payments_[payment_method_slug]`.

Your JavaScript file should listen for this event and handle the payment process accordingly. Here's a simple example:

javascript

```
window.addEventListener("fluent_cart_load_payments_your_gateway", function (e) {
    const submitButton = window.fluentcart_checkout_vars?.submit_button;
    const gatewayContainer = document.querySelector('.fluent-cart-checkout_embed_payment_container_your_gateway');
    const translations = window.fct_your_gateway_data?.translations || {};

    function $t(string) {
        return translations[string] || string;
    }

    // Simple implementation (like COD/offline payments)
    if (gatewayContainer) {
        gatewayContainer.innerHTML = `<p>${$t('Your payment instructions here.')}</p>`;
    }

    // Enable the checkout button
    e.detail.paymentLoader.enableCheckoutButton(submitButton.text);

    // OR if you need to integrate with a third-party SDK:
    // loadYourGatewaySDK(e.detail.paymentInfoUrl, e.detail.nonce, e.detail.form, e.detail.paymentLoader);
});

// Example function for loading a more complex gateway SDK
function loadYourGatewaySDK(paymentInfoUrl, nonce, form, paymentLoader) {
    // Fetch payment information from server
    fetch(paymentInfoUrl, {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
            "X-WP-Nonce": nonce,
        },
        credentials: 'include'
    }).then(response => response.json())
    .then(data => {
        // Initialize your gateway SDK with the data
        // When ready, enable the checkout button:
        paymentLoader.enableCheckoutButton('Pay Now');
    });
}
```

#### Payment methods list in FluentCart admin dashboard [​](https://dev.fluentcart.com/payment-methods-integration/quick-implementation\#payment-methods-list-in-fluentcart-admin-dashboard)

![Payment methods list in FluentCart admin dashboard](https://dev.fluentcart.com/assets/payment-mthods-list.DK5L5gfy.png)

#### Payment method settings configuration page [​](https://dev.fluentcart.com/payment-methods-integration/quick-implementation\#payment-method-settings-configuration-page)

![Payment method settings configuration page](https://dev.fluentcart.com/assets/payment-settings.BT9_ZdOD.png)

#### Active payment methods displayed in checkout page [​](https://dev.fluentcart.com/payment-methods-integration/quick-implementation\#active-payment-methods-displayed-in-checkout-page)

![Active payment gateway displayed in checkout page](https://dev.fluentcart.com/assets/active-payment-methods-in-checkout.DZztE06D.png)

## Start taking payments with your gateway [​](https://dev.fluentcart.com/payment-methods-integration/quick-implementation\#start-taking-payments-with-your-gateway)

## Step 4: Create an API Handler [​](https://dev.fluentcart.com/payment-methods-integration/quick-implementation\#step-4-create-an-api-handler)

Create a class for API communications with your payment provider:

php

```
<?php
namespace YourPlugin\PaymentMethods\YourGateway;

class API
{
    private $settings;
    private $baseUrl;

    public function __construct(YourGatewaySettings $settings)
    {
        $this->settings = $settings;
        $this->baseUrl = $settings->isTestMode()
            ? 'https://api-test.yourgateway.com/v1'
            : 'https://api.yourgateway.com/v1';
    }

    public function makeRequest($method, $endpoint, $data = [])
    {
        $args = [\
            'method' => $method,\
            'headers' => [\
                'Authorization' => 'Bearer ' . $this->settings->getApiKey(),\
                'Content-Type' => 'application/json',\
            ],\
            'timeout' => 30\
        ];

        if (!empty($data) && in_array($method, ['POST', 'PUT'])) {
            $args['body'] = json_encode($data);
        }

        $response = wp_remote_request($this->baseUrl . $endpoint, $args);

        if (is_wp_error($response)) {
            return [\
                'success' => false,\
                'message' => $response->get_error_message()\
            ];
        }

        $body = wp_remote_retrieve_body($response);
        $data = json_decode($body, true);
        $code = wp_remote_retrieve_response_code($response);

        if ($code >= 400) {
            return [\
                'success' => false,\
                'message' => $data['error'] ?? 'API request failed'\
            ];
        }

        return [\
            'success' => true,\
            'data' => $data\
        ];
    }

    public function createPayment($paymentData)
    {
        return $this->makeRequest('POST', '/payments', $paymentData);
    }

    public function createSubscription($subscriptionData)
    {
        return $this->makeRequest('POST', '/subscriptions', $subscriptionData);
    }

    public function refundPayment($paymentId, $amount, $reason = '')
    {
        return $this->makeRequest('POST', "/payments/{$paymentId}/refund", [\
            'amount' => $amount,\
            'reason' => $reason\
        ]);
    }
}
```

## Step 5: Payment processing [​](https://dev.fluentcart.com/payment-methods-integration/quick-implementation\#step-5-payment-processing)

php

```
<?php

 #YourGateway.php

public function makePaymentFromPaymentInstance(PaymentInstance $paymentInstance)
{
    $order = $paymentInstance->order;

    if ($paymentInstance->subscription) {
        return (new Processor())->handleSubscriptionPayment($paymentInstance);
    }

    // check if this is a subscription payment
    if ($paymentInstance->subscription) {
        return $this->handleSubscriptionPayment($paymentInstance);
    }

    // This is a regular one-time payment
    return $this->handleOneTimePayment($paymentInstance);
}

// Example of one-time payment processing

// option 1: make payment with hosted(redirect) checkout
private function handleOneTimePayment(PaymentInstance $paymentInstance)
{
    $order = $paymentInstance->order;
    $transaction = $paymentInstance->transaction;

    $api = new API($this->settings);

    // Prepare payment data for the API
    $paymentData = [\
       ....\
    ];

    // Create payment in your gateway
    $result = $api->createPayment($paymentData);

    if ($result['success']) {
        // Store payment ID for later reference
        $transaction->update([\
            ...\
        ]);

        // Return redirect URL (for redirect-based gateways)
        return [\
            'redirect_to' => $result['data']['checkout_url'],\
            'status'      => 'success',\
            'message'     => __('Order has been placed successfully', 'fluent-cart'),\
        ];
    }
}

// option 2: make payment onsite
private function handleOneTimePayment(PaymentInstance $paymentInstance)
{
    $order = $paymentInstance->order;
    $transaction = $paymentInstance->transaction;

    $api = new API($this->settings);

    // Prepare payment data for the API
    $paymentData = [\
       ....\
    ];

    // Create payment in your gateway
    $result = $api->createPayment($paymentData);

    if ($result['success']) {
        // Store payment ID for later reference
        $transaction->update([\
            ...\
        ]);

        // Return success response with custom action to redirect to your own your-gateway-checkout.js
        return [\
            'nextAction'         => 'your_gateway',\
            'actionName'         => 'custom',\
            'status'             => 'success',\
            'message' => __('Order has been placed successfully', 'fluent-cart'),\
            'response' => $result,\
        ];
    }
}

// ... subscription is similar to one-time payment
```

## Step 6: Confirm Payment [​](https://dev.fluentcart.com/payment-methods-integration/quick-implementation\#step-6-confirm-payment)

Payment confirmation can be done in two ways:

#### Ajax call From you your-gateway-checkout.js (onsite payment) [​](https://dev.fluentcart.com/payment-methods-integration/quick-implementation\#ajax-call-from-you-your-gateway-checkout-js-onsite-payment)

php

```
<?php

#YourGateway.php

// init ajax handler in boot/constructor
public function boot()
{
    ....
    add_action('wp_ajax_fluent_cart_confirm_your_gateway_payment', [$this, 'confirmPayment']);
    add_action('wp_ajax_nopriv_fluent_cart_confirm_your_gateway_payment', [$this, 'confirmPayment']);
}

// Example
public function confirmPayment()
{

    // Get data from request
    $transactionId = sanitize_text_field($_REQUEST['transaction_id'] ?? '');
    $paymentId = sanitize_text_field($_REQUEST['payment_id'] ??

    // Find the transaction by UUID (ref_id)
    $transaction = OrderTransaction::query()->where('uuid', $transactionId)->first();

    if (!$transaction) {
        wp_send_json([\
            'message' => 'Transaction ID is required to confirm the payment.',\
            'status' => 'failed'\
        ], 400);
    }

    // Check if already processed
    if ($transaction->status === Status::TRANSACTION_SUCCEEDED) {
        wp_send_json([\
            'redirect_url' => $transaction->getReceiptPageUrl(),\
            'order' => [\
                'uuid' => $transaction->order->uuid,\
            ],\
            'message' => __('Payment already confirmed.', 'fluent-cart'),\
            'status' => 'success'\
        ], 200);
    }

    // Verify payment with gateway API
    // $paymentStatus = YourGatewayAPI::verifyPayment($paymentId);

    // Update transaction and order status
    $transaction->fill([\
        'status' => Status::TRANSACTION_SUCCEEDED,\
        'vendor_charge_id' => $paymentId,\
        // Add other fields as needed\
    ]);
    $transaction->save();


    // Update order status
    $order = Order::query()->find($transaction->order_id);
    (new StatusHelper($order))->syncOrderStatuses($transaction);

    // Send success response
    wp_send_json([\
        'redirect_url' => $transaction->getReceiptPageUrl(),\
        'order' => [\
            'uuid' => $transaction->order->uuid,\
        ],\
        'message' => __('Payment confirmed successfully.', 'fluent-cart'),\
        'status' => 'success'\
    ],

}
```

#### With IPN/Webhooks (Hosted payment) [​](https://dev.fluentcart.com/payment-methods-integration/quick-implementation\#with-ipn-webhooks-hosted-payment)

php

```
<?php

// YourGateway.php

// init ipn handler in boot/constructor
public function boot()
{
    ....
    add_action('fluent_cart/payments/your_gateway/webhook_payment_completed', [$this, 'handlePaymentCompleted']);
    ....
}

public function handleIPN(): void
{
    // Process the webhook
    $this->processWebhookEvent($data);
}

// Example of webhook processing
public function processWebhookEvent($data)
{
    $eventType = $data['event'] ?? '';
    $eventTypeFormatted = str_replace('.', '_', $eventType);

    // Fire specific event handler
    if (has_action('fluent_cart/payments/your_gateway/webhook_' . $eventTypeFormatted)) {
        do_action('fluent_cart/payments/your_gateway/webhook_' . $eventTypeFormatted, [\
            'data' => $data,\
            'raw' => $rawPayload,\
            'order' => $order\
        ]);
    }
}

// Example of payment confirmation
public function handlePaymentCompleted($data)
{
    $paymentId = $data['payment']['id'] ?? '';

    // Find the transaction
    $transaction = OrderTransaction::query()->where('uuid', $transactionId)->first();

    if (!$transaction) {
        return;
    }

    // Check if already processed
    if ($transaction->status === Status::TRANSACTION_SUCCEEDED) {
        return;
    }

    // Get transaction details from YourGateway
    $yourGatewayTransaction = API::getYourGatewayObject("transactions/{$paymentId}", [], $transaction->payment_mode);

    if (is_wp_error($yourGatewayTransaction)) {
        return;
    }

    $data = Arr::get($yourGatewayTransaction, 'data');
    $transactionStatus = Arr::get($data, 'status');

    // Check if payment is completed
    if ($transactionStatus !== 'paid' && $transactionStatus !== 'completed') {
        return;
    }

    // Update transaction and order status
    $transaction->fill([\
        'status' => Status::TRANSACTION_SUCCEEDED,\
        'vendor_charge_id' => $paymentId,\
        // Add other fields as needed\
    ]);
    $transaction->save();

    // Update order status
    $order = Order::query()->find($transaction->order_id);
    (new StatusHelper($order))->syncOrderStatuses($transaction);
}
```

### Step 7: (optional) Create your-gateway-checkout.js [​](https://dev.fluentcart.com/payment-methods-integration/quick-implementation\#step-7-optional-create-your-gateway-checkout-js)

Create custom JavaScript file to handle (onsite) payment checkout, step #3 above is enough for (hosted) payment checkout.

#### Example of onsite payment checkout with custom checkout button [​](https://dev.fluentcart.com/payment-methods-integration/quick-implementation\#example-of-onsite-payment-checkout-with-custom-checkout-button)

javascript

```
// File: assets/js/your-gateway-checkout.js
class YourGatewayCheckout {
    constructor(form, orderHandler, response, paymentLoader) {
        this.form = form;
        this.orderHandler = orderHandler;
        this.response = response;
        this.paymentLoader = paymentLoader;
        this.paymentArgs = response?.payment_args || {};
    }

    init() {
        // Find the payment container
        const paymentContainer = document.querySelector('.fluent-cart-checkout_embed_payment_container_your_gateway');
        if (!paymentContainer) {
            console.error('Payment container not found');
            return;
        }

        // Create payment button
        this.createPaymentButton(paymentContainer);

        // Initialize gateway SDK (if applicable)
        this.initGatewaySDK();
    }

    createPaymentButton(container) {
        // Clear container
        container.innerHTML = '';

        // Create button
        const button = document.createElement('button');
        button.type = 'button';
        button.className = 'your-gateway-checkout-button';
        button.textContent = 'Pay with Your Gateway';
        button.style.cssText = `
            width: 100%;
            padding: 12px;
            background: #007bff;
            color: #fff;
            border: none;
            border-radius: 4px;
            font-size: 16px;
            cursor: pointer;
        `;

        // Add click event
        button.addEventListener('click', () => {
            this.handlePaymentButtonClick();
        });

        // Add to container
        container.appendChild(button);
    }

    initGatewaySDK() {
        // Initialize your gateway's SDK if required
        if (window.YourGatewaySDK) {
            window.YourGatewaySDK.initialize({
                publicKey: this.paymentArgs.public_key,
                environment: this.paymentArgs.mode
            });
        }
    }

    async handlePaymentButtonClick() {
        try {
            this.paymentLoader?.changeLoaderStatus('processing');

            // Create order in FluentCart first
            const orderResponse = await this.orderHandler.createOrder();

            if (!orderResponse?.success) {
                throw new Error('Failed to create order');
            }

            // For redirect-based gateways
            if (orderResponse.redirect_url) {
                window.location.href = orderResponse.redirect_url;
                return;
            }

            // For JS-based gateways, open checkout modal
            if (window.YourGatewaySDK) {
                const result = await window.YourGatewaySDK.openCheckout({
                    amount: this.response.amount,
                    currency: this.response.currency,
                    orderId: orderResponse.order_id,
                    onSuccess: (data) => {
                        // Confirm payment on your server
                        this.confirmPayment(data, orderResponse);
                    },
                    onCancel: () => {
                        this.paymentLoader?.hideLoader();
                    }
                });
            }
        } catch (error) {
            this.paymentLoader?.changeLoaderStatus('Error: ' + error.message);
            this.paymentLoader?.hideLoader();
        }
    }

    async confirmPayment(gatewayData, orderData) {
        try {
            // Confirm payment on your server
            const confirmResponse = await fetch(fluentCartData.ajax_url, {
                method: 'POST',
                headers: {"Content-Type": "application/json"},
                credentials: 'same-origin',
                body: JSON.stringify({
                    action: 'fluent_cart_confirm_your_gateway_payment',
                    transaction_id: orderData.transaction_id,
                    payment_id: gatewayData.paymentId
                })
            });

            const confirmation = await confirmResponse.json();

            if (confirmation.success && confirmation.redirect_url) {
                window.location.href = confirmation.redirect_url;
            } else {
                throw new Error(confirmation.message || 'Payment confirmation failed');
            }
        } catch (error) {
            this.paymentLoader?.changeLoaderStatus('Error: ' + error.message);
            this.paymentLoader?.hideLoader();
        }
    }
}

// Initialize when FluentCart triggers the event
window.addEventListener("fluent_cart_load_payments_your_gateway", function (e) {
    fetch(e.detail.paymentInfoUrl, {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        credentials: 'include'
    })
    .then(response => response.json())
    .then(data => {
        new YourGatewayCheckout(
            e.detail.form,
            e.detail.orderHandler,
            data,
            e.detail.paymentLoader
        ).init();
    })
    .catch(error => {
        console.error('Error initializing gateway:', error);
    });
});
```

## Key FluentCart Services to Use [​](https://dev.fluentcart.com/payment-methods-integration/quick-implementation\#key-fluentcart-services-to-use)

FluentCart provides these services to make gateway development easier:

### StatusHelper for Order Updates [​](https://dev.fluentcart.com/payment-methods-integration/quick-implementation\#statushelper-for-order-updates)

php

```
// Update order status and fire all necessary hooks
(new \FluentCart\App\Helpers\StatusHelper($order))->syncOrderStatuses($transaction);

// This automatically fires:
// - fluent_cart/order_paid (for successful payments)
// - fluent_cart/order_failed (for failed payments)
// - fluent_cart/order_status_updated
$data[\
    'order'       => $this->order,\
    'customer'    => $this->customer ?? null,\
    'transaction' => $this->transaction ?? null\
];
```

### Refund Service for Handling Refunds [​](https://dev.fluentcart.com/payment-methods-integration/quick-implementation\#refund-service-for-handling-refunds)

php

```
// Use Refund service for all refund operations
\FluentCart\App\Services\Payments\Refund::createOrRecordRefund([\
    'vendor_charge_id' => $refundId,\
    'payment_method' => 'your_gateway',\
    'status' => 'refunded',\
    'total' => $refundAmount,\
], $parentTransaction);

// This automatically handles:
// - Creating refund transaction
// - Updating order status
// - Firing all refund-related hooks
```

### Subscription Handling [​](https://dev.fluentcart.com/payment-methods-integration/quick-implementation\#subscription-handling)

For subscription renewals, use the SubscriptionRenewal service:

php

```
\FluentCart\App\Services\Subscription\SubscriptionRenewal::recordRenewalPayment(
    $subscription,
    [\
        'amount' => $amount,\
        'transaction_id' => $paymentId,\
        'payment_method' => 'your_gateway',\
        'status' => 'completed'\
    ]
);
```

## Important Hooks [​](https://dev.fluentcart.com/payment-methods-integration/quick-implementation\#important-hooks)

Key hooks to be aware of:

1. **Payment Hooks** (Handled by StatusHelper):


   - `fluent_cart/order_paid`
   - `fluent_cart/order_failed`
   - `fluent_cart/order_status_updated`

php

```
$data = array(
   'order'       => $this->order,
   'customer'    => $this->customer ?? null,
   'transaction' => $this->transaction ?? null
);
```

2. **Subscription Hooks**:


   - `fluent_cart/subscription_created`
   - `fluent_cart/subscription_activated`
   - `fluent_cart/subscription_renewed`
   - `fluent_cart/subscription_cancelled`

php

```
$data = array(
    'subscription' => $this->subscription,
    'order' => $this->order,
    'customer' => $this->customer ?? [],
);
```

Learn more about hooks in [FluentCart Hooks](https://dev.fluentcart.com/hooks/) documentation.

## Testing Your Gateway [​](https://dev.fluentcart.com/payment-methods-integration/quick-implementation\#testing-your-gateway)

1. **Install & Activate**: Activate your plugin in WordPress
2. **Configure**: Go to FluentCart → Settings → Payment Methods
3. **Test Payment**: Test a one-time payment on the checkout page
4. **Test Subscription**: Test a subscription product if supported
5. **Test Web Hook**: Test web hook processing using a tool like RequestBin

## Additional Resources [​](https://dev.fluentcart.com/payment-methods-integration/quick-implementation\#additional-resources)

For more detailed examples, you can refer to:

- Built-in payment methods in FluentCart (Stripe, PayPal)
- [Paddle Gateway Implementation](https://dev.fluentcart.com/payment-methods-integration/paddle-example.html) for a complete, real-world example

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

## Payment Gateway Settings Fields | FluentCart Developer Docs

**URL** : https://dev.fluentcart.com/payment-methods-integration/payment_setting_fields

[Skip to content](https://dev.fluentcart.com/payment-methods-integration/payment_setting_fields#VPContent)

# Payment Gateway Settings Fields [​](https://dev.fluentcart.com/payment-methods-integration/payment_setting_fields\#payment-gateway-settings-fields)

This guide explains how to build settings fields for your custom payment gateway in FluentCart. The `fields()` method in your main gateway class (ex: YourGateway.php) returns a schema that FluentCart uses to render settings fields in the admin interface.

## Basic Structure [​](https://dev.fluentcart.com/payment-methods-integration/payment_setting_fields\#basic-structure)

The `fields()` method returns an associative array where each key is a field ID and each value is an array defining the field properties:

php

```
public function fields(): array
{
    return [\
        'field_id' => [\
            'type'  => 'text',          // Field type (required)\
            'label' => 'Field Label',   // Display label\
            'value' => 'default_value', // Default value\
            // ... other properties\
        ],\
        // ... more fields\
    ];
}
```

## Common Field Properties [​](https://dev.fluentcart.com/payment-methods-integration/payment_setting_fields\#common-field-properties)

All field types support these common properties:

| Property | Description |
| --- | --- |
| `type` | Required. Defines the field type (see available types below) |
| `label` | The field label displayed to the user |
| `value` | Default value for the field |
| `placeholder` | Placeholder text for input fields |
| `tooltip` | Brief tooltip displayed on hover |
| `description` | Brief description displayed below the field |
| `max_length` | Maximum length of the text/input/password field |
| `disabled` | Whether the field is disabled (boolean) |

## Available Field Types [​](https://dev.fluentcart.com/payment-methods-integration/payment_setting_fields\#available-field-types)

### Text Fields [​](https://dev.fluentcart.com/payment-methods-integration/payment_setting_fields\#text-fields)

#### `text`, `input`, `password`, `email`, `number` [​](https://dev.fluentcart.com/payment-methods-integration/payment_setting_fields\#text-input-password-email-number)

Basic input fields for text, passwords, number(with min, max), and emails.

php

```
'api_key' => [\
    'type'        => 'text',\
    'label'       => __('API Key', 'your-plugin'),\
    'placeholder' => __('Enter your API key', 'your-plugin'),\
    'help_text'   => __('Find this in your gateway dashboard', 'your-plugin'),\
],
'secret_key' => [\
    'type'        => 'password',\
    'label'       => __('Secret Key', 'your-plugin'),\
    'placeholder' => __('Enter your secret key', 'your-plugin'),\
],
```

### Toggle Fields [​](https://dev.fluentcart.com/payment-methods-integration/payment_setting_fields\#toggle-fields)

#### `enable` (Toggle Switch) [​](https://dev.fluentcart.com/payment-methods-integration/payment_setting_fields\#enable-toggle-switch)

Creates a toggle switch for enabling/disabling features.

php

```
'is_active' => [\
    'type'    => 'enable',\
    'label'   => __('Enable Gateway', 'your-plugin'),\
    'value'   => 'yes', // or 'no'\
],
```

#### `checkbox` [​](https://dev.fluentcart.com/payment-methods-integration/payment_setting_fields\#checkbox)

Creates a single checkbox.

php

```
'save_card' => [\
    'type'    => 'checkbox',\
    'label'   => __('Save Customer Cards', 'your-plugin'),\
    'value'   => 'no',\
    'tooltip' => __('Allow customers to save payment methods', 'your-plugin'),\
],
```

### Selection Fields [​](https://dev.fluentcart.com/payment-methods-integration/payment_setting_fields\#selection-fields)

#### `select` [​](https://dev.fluentcart.com/payment-methods-integration/payment_setting_fields\#select)

Creates a dropdown select menu.

php

```
'checkout_mode' => [\
    'type'    => 'select',\
    'label'   => __('Checkout Mode', 'your-plugin'),\
    'options' => [\
        ['value' => 'hosted', 'label' => __('Hosted Checkout', 'your-plugin')],\
        ['value' => 'embedded', 'label' => __('Embedded Checkout', 'your-plugin')],\
    ],\
],
```

#### `radio` [​](https://dev.fluentcart.com/payment-methods-integration/payment_setting_fields\#radio)

Creates a group of radio buttons.

php

```
'transaction_type' => [\
    'type'    => 'radio',\
    'label'   => __('Transaction Type', 'your-plugin'),\
    'options' => [\
        'sale'      => __('Direct Sale', 'your-plugin'),\
        'authorize' => __('Authorize Only', 'your-plugin'),\
    ],\
    'value' => 'sale',\
],
```

#### `checkbox_group` [​](https://dev.fluentcart.com/payment-methods-integration/payment_setting_fields\#checkbox-group)

Creates a group of checkboxes.

php

```
'accepted_cards' => [\
    'type'    => 'checkbox_group',\
    'title'   => __('Accepted Cards', 'your-plugin'),\
    'desc'    => __('Select the card types to accept', 'your-plugin'),\
    'options' => [\
        'visa'       => __('Visa', 'your-plugin'),\
        'mastercard' => __('Mastercard', 'your-plugin'),\
        'amex'       => __('American Express', 'your-plugin'),\
    ],\
],
```

### Display Fields [​](https://dev.fluentcart.com/payment-methods-integration/payment_setting_fields\#display-fields)

#### `notice` [​](https://dev.fluentcart.com/payment-methods-integration/payment_setting_fields\#notice)

Displays an informational notice without input.

php

```
'setup_notice' => [\
    'type'  => 'notice',\
    'value' => '<p>Configure your gateway settings below.</p>',\
],
```

#### `html_attr` [​](https://dev.fluentcart.com/payment-methods-integration/payment_setting_fields\#html-attr)

Displays custom HTML content.

php

```
'webhook_info' => [\
    'type'  => 'html_attr',\
    'value' => '<div class="fc-gateway-webhook-info">Webhook URL: ' . $this->getWebhookUrl() . '</div>',\
],
```

### Color Selector [​](https://dev.fluentcart.com/payment-methods-integration/payment_setting_fields\#color-selector)

#### `color` [​](https://dev.fluentcart.com/payment-methods-integration/payment_setting_fields\#color)

Creates a color picker.

php

```
'button_color' => [\
    'type'  => 'color',\
    'label' => __('Button Color', 'your-plugin'),\
    'value' => '#3498db',\
],
```

### Advanced Field Groups [​](https://dev.fluentcart.com/payment-methods-integration/payment_setting_fields\#advanced-field-groups)

#### `tabs` [​](https://dev.fluentcart.com/payment-methods-integration/payment_setting_fields\#tabs)

Creates a tabbed interface, useful for separating test and live credentials.

php

```
'payment_mode' => [\
    'type'   => 'tabs',\
    'schema' => [\
        [\
            'type'   => 'tab',\
            'label'  => __('Live credentials', 'your-plugin'),\
            'value'  => 'live',\
            'schema' => [\
                'live_api_key' => [\
                    'type'  => 'text',\
                    'label' => __('Live API Key', 'your-plugin'),\
                ],\
                'live_secret_key' => [\
                    'type'  => 'password',\
                    'label' => __('Live Secret Key', 'your-plugin'),\
                ],\
            ]\
        ],\
        [\
            'type'   => 'tab',\
            'label'  => __('Test credentials', 'your-plugin'),\
            'value'  => 'test',\
            'schema' => [\
                'test_api_key' => [\
                    'type'  => 'text',\
                    'label' => __('Test API Key', 'your-plugin'),\
                ],\
                'test_secret_key' => [\
                    'type'  => 'password',\
                    'label' => __('Test Secret Key', 'your-plugin'),\
                ],\
            ]\
        ]\
    ]\
],
```

## Complete Example [​](https://dev.fluentcart.com/payment-methods-integration/payment_setting_fields\#complete-example)

Here's a complete example of a `fields()` method in a gateway class:

php

```
public function fields(): array
{
    // Get webhook URL
    $webhookUrl = $this->getWebhookUrl();

    // Test mode credentials
    $testSchema = [\
        'test_api_key' => [\
            'type'        => 'text',\
            'label'       => __('Test API Key', 'your-plugin'),\
            'placeholder' => __('Enter your test API key', 'your-plugin'),\
        ],\
        'test_secret_key' => [\
            'type'        => 'password',\
            'label'       => __('Test Secret Key', 'your-plugin'),\
            'placeholder' => __('Enter your test secret key', 'your-plugin'),\
        ],\
    ];

    // Live mode credentials
    $liveSchema = [\
        'live_api_key' => [\
            'type'        => 'text',\
            'label'       => __('Live API Key', 'your-plugin'),\
            'placeholder' => __('Enter your live API key', 'your-plugin'),\
        ],\
        'live_secret_key' => [\
            'type'        => 'password',\
            'label'       => __('Live Secret Key', 'your-plugin'),\
            'placeholder' => __('Enter your live secret key', 'your-plugin'),\
        ],\
    ];

    return [\
        'setup_notice' => [\
            'type'  => 'notice',\
            'value' => '<p>' . __('Configure your gateway settings below.', 'your-plugin') . '</p>',\
        ],\
        'payment_mode' => [\
            'type'   => 'tabs',\
            'schema' => [\
                [\
                    'type'   => 'tab',\
                    'label'  => __('Live credentials', 'your-plugin'),\
                    'value'  => 'live',\
                    'schema' => $liveSchema\
                ],\
                [\
                    'type'   => 'tab',\
                    'label'  => __('Test credentials', 'your-plugin'),\
                    'value'  => 'test',\
                    'schema' => $testSchema\
                ]\
            ]\
        ],\
        'checkout_title' => [\
            'type'        => 'text',\
            'label'       => __('Checkout Title', 'your-plugin'),\
            'value'       => __('Credit Card Payment', 'your-plugin'),\
            'placeholder' => __('Appears on the checkout page', 'your-plugin'),\
        ],\
        'checkout_description' => [\
            'type'        => 'textarea',\
            'label'       => __('Checkout Description', 'your-plugin'),\
            'value'       => __('Pay securely using your credit card.', 'your-plugin'),\
            'placeholder' => __('Appears on the checkout page', 'your-plugin'),\
        ],\
        'webhook_info' => [\
            'type'  => 'html_attr',\
            'value' => '<div class="fc-webhook-info">' .\
                       '<strong>' . __('Webhook URL:', 'your-plugin') . '</strong><br>' .\
                       '<code>' . $webhookUrl . '</code><br>' .\
                       __('Configure this URL in your gateway dashboard to receive payment notifications.', 'your-plugin') .\
                       '</div>',\
        ],\
        'debug_mode' => [\
            'type'    => 'checkbox',\
            'label'   => __('Debug Mode', 'your-plugin'),\
            'value'   => 'no',\
            'tooltip' => __('Enable logging for debugging purposes', 'your-plugin'),\
        ],\
    ];
}
```

## Accessing Settings Values [​](https://dev.fluentcart.com/payment-methods-integration/payment_setting_fields\#accessing-settings-values)

Once settings are saved, you can access them in your gateway class using the `$this->settings->get()` method:

php

```
// Get a setting value
$apiKey = $this->settings->get('api_key');

// Get a nested setting value based on payment mode
$mode = $this->settings->get('payment_mode');
$apiKey = $this->settings->get($mode . '_api_key');
```

## Best Practices [​](https://dev.fluentcart.com/payment-methods-integration/payment_setting_fields\#best-practices)

1. **Group Related Settings**: Use tabs to separate test and live credentials
2. **Provide Clear Labels**: Use descriptive labels and help text
3. **Include Validation**: Use appropriate field types for data validation
4. **Secure Sensitive Data**: Use password fields for API secrets
5. **Add Webhook Instructions**: Show webhook URLs and instructions when applicable

## Available Field Types Reference [​](https://dev.fluentcart.com/payment-methods-integration/payment_setting_fields\#available-field-types-reference)

| Field Type | Description |
| --- | --- |
| `text`, `input` | Standard text input |
| `password` | Password input (masked text) |
| `email` | Email input with validation |
| `textarea` | Multi-line text input |
| `select` | Dropdown selection |
| `radio` | Radio button group |
| `checkbox` | Single checkbox toggle |
| `checkbox_group` | Multiple checkbox group |
| `enable` | Toggle switch |
| `color` | Color picker |
| `notice` | Information display |
| `html_attr` | Raw HTML content |
| `tabs` | Tabbed interface |

For more complete payment method integration examples, refer to the [Complete Payment Gateway Integration Guide](https://dev.fluentcart.com/payment-methods-integration/quick-implementation.html).

Today

Hi! I’m your AI assistant. How can I assist you today?

Just now

Powered by **FluentBot**


---

---

