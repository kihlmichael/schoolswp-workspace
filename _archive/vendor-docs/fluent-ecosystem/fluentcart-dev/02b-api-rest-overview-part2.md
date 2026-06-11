# FluentCart Developer Docs - REST API Overview (Part 2/4)

Overview de l'API REST FluentCart : authentification, orders, products, customers, subscriptions, licensing, order-bump, roles & permissions.

---

## Licensing API (Pro) | FluentCart Developer Docs

**URL** : https://dev.fluentcart.com/api/licensing

[Skip to content](https://dev.fluentcart.com/api/licensing#VPContent)

# Licensing API (Pro) [​](https://dev.fluentcart.com/api/licensing\#licensing-api-pro)

The Licensing API provides comprehensive software license management capabilities for FluentCart Pro. This API allows you to manage software licenses, track activations, and integrate with external license management systems.

## Base URL [​](https://dev.fluentcart.com/api/licensing\#base-url)

All Licensing API endpoints are prefixed with the same base URL as the core API:

```
/wp-json/fluent-cart/v2/
```

## Authentication [​](https://dev.fluentcart.com/api/licensing\#authentication)

All Licensing API endpoints require authentication with the `manage_fluent_cart_settings` capability.

## License Management [​](https://dev.fluentcart.com/api/licensing\#license-management)

### 1\. Get License Details [​](https://dev.fluentcart.com/api/licensing\#_1-get-license-details)

Retrieve details for the current FluentCart Pro license.

- **Endpoint:**`GET /wp-json/fluent-cart/v2/settings/license`
- **Authentication:** Requires `manage_fluent_cart_settings` capability.
- **Parameters:** None

**Example Request:**

bash

```
curl -X GET "http://localhost/wp-json/fluent-cart/v2/settings/license" \
-H "Authorization: Basic [YOUR_BASE64_ENCODED_CREDENTIALS]"
```

### 2\. Activate License [​](https://dev.fluentcart.com/api/licensing\#_2-activate-license)

Activate a FluentCart Pro license.

- **Endpoint:**`POST /wp-json/fluent-cart/v2/settings/license`
- **Authentication:** Requires `manage_fluent_cart_settings` capability.
- **Parameters:**
  - `license_key` (string, required): The license key to activate

**Example Request:**

bash

```
curl -X POST "http://localhost/wp-json/fluent-cart/v2/settings/license" \
-H "Authorization: Basic [YOUR_BASE64_ENCODED_CREDENTIALS]" \
-H "Content-Type: application/json" \
-d '{"license_key": "your-license-key-here"}'
```

### 3\. Deactivate License [​](https://dev.fluentcart.com/api/licensing\#_3-deactivate-license)

Deactivate the current FluentCart Pro license.

- **Endpoint:**`DELETE /wp-json/fluent-cart/v2/settings/license`
- **Authentication:** Requires `manage_fluent_cart_settings` capability.
- **Parameters:** None

**Example Request:**

bash

```
curl -X DELETE "http://localhost/wp-json/fluent-cart/v2/settings/license" \
-H "Authorization: Basic [YOUR_BASE64_ENCODED_CREDENTIALS]"
```

## Product License Management [​](https://dev.fluentcart.com/api/licensing\#product-license-management)

### 1\. Get All Licenses [​](https://dev.fluentcart.com/api/licensing\#_1-get-all-licenses)

Retrieve all product licenses.

- **Endpoint:**`GET /wp-json/fluent-cart/v2/licensing/licenses`
- **Authentication:** Requires `licenses/view` permission.
- **Parameters:** None

### 2\. Get Customer Licenses [​](https://dev.fluentcart.com/api/licensing\#_2-get-customer-licenses)

Retrieve all licenses for a specific customer.

- **Endpoint:**`GET /wp-json/fluent-cart/v2/licensing/licenses/customer/{id}`
- **Authentication:** Requires `licenses/view` permission.
- **Parameters:**
  - `id` (int, required): Customer ID

### 3\. Get License Details [​](https://dev.fluentcart.com/api/licensing\#_3-get-license-details)

Retrieve details for a specific license.

- **Endpoint:**`GET /wp-json/fluent-cart/v2/licensing/licenses/{id}`
- **Authentication:** Requires `licenses/view` permission.
- **Parameters:**
  - `id` (int, required): License ID

### 4\. Regenerate License Key [​](https://dev.fluentcart.com/api/licensing\#_4-regenerate-license-key)

Regenerate the license key for a specific license.

- **Endpoint:**`POST /wp-json/fluent-cart/v2/licensing/licenses/{id}/regenerate-key`
- **Authentication:** Requires `licenses/manage` permission.
- **Parameters:**
  - `id` (int, required): License ID

### 5\. Extend License Validity [​](https://dev.fluentcart.com/api/licensing\#_5-extend-license-validity)

Extend the validity period of a license.

- **Endpoint:**`POST /wp-json/fluent-cart/v2/licensing/licenses/{id}/extend-validity`
- **Authentication:** Requires `licenses/manage` permission.
- **Parameters:**
  - `id` (int, required): License ID
  - `days` (int, required): Number of days to extend

### 6\. Update License Status [​](https://dev.fluentcart.com/api/licensing\#_6-update-license-status)

Update the status of a license.

- **Endpoint:**`POST /wp-json/fluent-cart/v2/licensing/licenses/{id}/update_status`
- **Authentication:** Requires `licenses/manage` permission.
- **Parameters:**
  - `id` (int, required): License ID
  - `status` (string, required): New status (active, inactive, expired, etc.)

### 7\. Update License Limit [​](https://dev.fluentcart.com/api/licensing\#_7-update-license-limit)

Update the activation limit for a license.

- **Endpoint:**`POST /wp-json/fluent-cart/v2/licensing/licenses/{id}/update_limit`
- **Authentication:** Requires `licenses/manage` permission.
- **Parameters:**
  - `id` (int, required): License ID
  - `limit` (int, required): New activation limit

### 8\. Deactivate Site [​](https://dev.fluentcart.com/api/licensing\#_8-deactivate-site)

Deactivate a specific site from a license.

- **Endpoint:**`POST /wp-json/fluent-cart/v2/licensing/licenses/{id}/deactivate_site`
- **Authentication:** Requires `licenses/manage` permission.
- **Parameters:**
  - `id` (int, required): License ID
  - `site_id` (int, required): Site ID to deactivate

### 9\. Activate Site [​](https://dev.fluentcart.com/api/licensing\#_9-activate-site)

Activate a site for a license.

- **Endpoint:**`POST /wp-json/fluent-cart/v2/licensing/licenses/{id}/activate_site`
- **Authentication:** Requires `licenses/manage` permission.
- **Parameters:**
  - `id` (int, required): License ID
  - `site_url` (string, required): Site URL to activate

### 10\. Delete License [​](https://dev.fluentcart.com/api/licensing\#_10-delete-license)

Delete a license permanently.

- **Endpoint:**`DELETE /wp-json/fluent-cart/v2/licensing/licenses/{id}/delete`
- **Authentication:** Requires `licenses/delete` permission.
- **Parameters:**
  - `id` (int, required): License ID

## Product License Settings [​](https://dev.fluentcart.com/api/licensing\#product-license-settings)

### 1\. Get Product License Settings [​](https://dev.fluentcart.com/api/licensing\#_1-get-product-license-settings)

Retrieve license settings for a specific product.

- **Endpoint:**`GET /wp-json/fluent-cart/v2/licensing/products/{id}/settings`
- **Authentication:** Requires `licenses/view` permission.
- **Parameters:**
  - `id` (int, required): Product ID

### 2\. Save Product License Settings [​](https://dev.fluentcart.com/api/licensing\#_2-save-product-license-settings)

Save license settings for a specific product.

- **Endpoint:**`POST /wp-json/fluent-cart/v2/licensing/products/{id}/settings`
- **Authentication:** Requires `licenses/manage` permission.
- **Parameters:**
  - `id` (int, required): Product ID
  - `settings` (object, required): License settings object

## Customer License Management [​](https://dev.fluentcart.com/api/licensing\#customer-license-management)

### 1\. Get Customer Licenses [​](https://dev.fluentcart.com/api/licensing\#_1-get-customer-licenses)

Retrieve all licenses for the current customer.

- **Endpoint:**`GET /wp-json/fluent-cart/v2/customer-profile/licenses`
- **Authentication:** Requires customer authentication.
- **Parameters:** None

### 2\. Get License Details [​](https://dev.fluentcart.com/api/licensing\#_2-get-license-details)

Retrieve details for a specific license by license key.

- **Endpoint:**`GET /wp-json/fluent-cart/v2/customer-profile/licenses/{license_key}`
- **Authentication:** Requires customer authentication.
- **Parameters:**
  - `license_key` (string, required): License key

### 3\. Get License Activations [​](https://dev.fluentcart.com/api/licensing\#_3-get-license-activations)

Retrieve all activations for a specific license.

- **Endpoint:**`GET /wp-json/fluent-cart/v2/customer-profile/licenses/{license_key}/activations`
- **Authentication:** Requires customer authentication.
- **Parameters:**
  - `license_key` (string, required): License key

### 4\. Deactivate Site [​](https://dev.fluentcart.com/api/licensing\#_4-deactivate-site)

Deactivate a site from a customer's license.

- **Endpoint:**`POST /wp-json/fluent-cart/v2/customer-profile/licenses/{license_key}/deactivate_site`
- **Authentication:** Requires customer authentication.
- **Parameters:**
  - `license_key` (string, required): License key
  - `site_id` (int, required): Site ID to deactivate

**Example Response (Success):**

json

```
{
  "message": "License found",
  "license": {
    "id": 123,
    "customer_id": 456,
    "product_id": 789,
    "license_key": "YOUR_LICENSE_KEY_HERE",
    "status": "active",
    "expires_at": "2024-12-31 23:59:59",
    "domain_limit": 5,
    "active_domains": [\
      {"id": 1, "domain": "site1.com"},\
      {"id": 2, "domain": "site2.com"}\
    ],
    "created_at": "2023-01-01 10:00:00",
    "updated_at": "2023-06-15 11:30:00"
  }
}
```

**Example Response (Error - License Not Found):**

json

```
{
  "message": "License not found",
  "errors": [\
    {\
      "code": 404,\
      "message": "License not found"\
    }\
  ]
}
```

### 2\. Activate License [​](https://dev.fluentcart.com/api/licensing\#_2-activate-license-1)

Activate a license for a specific domain.

- **Endpoint:**`POST /wp-json/fluent-cart/v2/settings/license`
- **Authentication:** Requires `manage_fluent_cart_settings` capability.
- **Parameters:**
  - `license_key` (string, required): The license key to activate.
  - `domain` (string, required): The domain where the license is being activated.

**Example Request:**

bash

```
curl -X POST "http://localhost/wp-json/fluent-cart/v2/settings/license" \
-H "Content-Type: application/json" \
-H "Authorization: Basic [YOUR_BASE64_ENCODED_CREDENTIALS]" \
-d '{
  "license_key": "YOUR_LICENSE_KEY_HERE",
  "domain": "newsite.com"
}'
```

**Example Response (Success):**

json

```
{
  "message": "License activated successfully",
  "license": {
    "id": 123,
    "customer_id": 456,
    "product_id": 789,
    "license_key": "YOUR_LICENSE_KEY_HERE",
    "status": "active",
    "expires_at": "2024-12-31 23:59:59",
    "domain_limit": 5,
    "active_domains": [\
      {"id": 1, "domain": "site1.com"},\
      {"id": 2, "domain": "site2.com"},\
      {"id": 3, "domain": "newsite.com"}\
    ],
    "created_at": "2023-01-01 10:00:00",
    "updated_at": "2023-06-15 11:30:00"
  }
}
```

**Example Response (Error - Invalid License Key):**

json

```
{
  "message": "Invalid license key",
  "errors": [\
    {\
      "code": 400,\
      "message": "Invalid license key"\
    }\
  ]
}
```

**Example Response (Error - Domain Limit Reached):**

json

```
{
  "message": "License domain limit reached",
  "errors": [\
    {\
      "code": 403,\
      "message": "License domain limit reached"\
    }\
  ]
}
```

### 3\. Deactivate License [​](https://dev.fluentcart.com/api/licensing\#_3-deactivate-license-1)

Deactivate a license for a specific domain.

- **Endpoint:**`DELETE /wp-json/fluent-cart/v2/settings/license`
- **Authentication:** Requires `manage_fluent_cart_settings` capability.
- **Parameters:**
  - `license_key` (string, required): The license key to deactivate.
  - `domain` (string, required): The domain from which the license is being deactivated.

**Example Request:**

bash

```
curl -X DELETE "http://localhost/wp-json/fluent-cart/v2/settings/license" \
-H "Content-Type: application/json" \
-H "Authorization: Basic [YOUR_BASE64_ENCODED_CREDENTIALS]" \
-d '{
  "license_key": "YOUR_LICENSE_KEY_HERE",
  "domain": "old-site.com"
}'
```

**Example Response (Success):**

json

```
{
  "message": "License deactivated successfully",
  "license": {
    "id": 123,
    "customer_id": 456,
    "product_id": 789,
    "license_key": "YOUR_LICENSE_KEY_HERE",
    "status": "active",
    "expires_at": "2024-12-31 23:59:59",
    "domain_limit": 5,
    "active_domains": [\
      {"id": 1, "domain": "site1.com"},\
      {"id": 2, "domain": "site2.com"}\
    ],
    "created_at": "2023-01-01 10:00:00",
    "updated_at": "2023-06-15 11:30:00"
  }
}
```

**Example Response (Error - Domain Not Found):**

json

```
{
  "message": "Domain not found for this license",
  "errors": [\
    {\
      "code": 404,\
      "message": "Domain not found for this license"\
    }\
  ]
}
```

## License Model [​](https://dev.fluentcart.com/api/licensing\#license-model)

### License Attributes [​](https://dev.fluentcart.com/api/licensing\#license-attributes)

php

```
use FluentCartPro\App\Modules\Licensing\Models\License;

class License extends Model
{
    protected $table = 'fct_licenses';

    protected $fillable = [\
        'customer_id',\
        'product_id',\
        'variation_id',\
        'order_id',\
        'subscription_id',\
        'license_key',\
        'status',\
        'expiration_date',\
        'limit',\
        'activation_count',\
        'domain_limit',\
        'created_at',\
        'updated_at'\
    ];

    protected $casts = [\
        'expiration_date' => 'datetime',\
        'limit' => 'integer',\
        'activation_count' => 'integer',\
        'domain_limit' => 'integer'\
    ];
}
```

### License Status Management [​](https://dev.fluentcart.com/api/licensing\#license-status-management)

php

```
// Activate a license
$license->activate();

// Deactivate a license
$license->deactivate();

// Expire a license
$license->expire();

// Check if license is expired
if ($license->isExpired()) {
    echo "License has expired";
}

// Check activation limit
$remainingActivations = $license->getActivationLimit();
if ($remainingActivations === 'unlimited') {
    echo "Unlimited activations";
} else {
    echo "Remaining activations: " . $remainingActivations;
}
```

## Automatic License Generation [​](https://dev.fluentcart.com/api/licensing\#automatic-license-generation)

The Licensing module automatically generates licenses when orders are completed:

php

```
use FluentCartPro\App\Modules\Licensing\Hooks\Handlers\LicenseGenerationHandler;

class LicenseGenerationHandler
{
    public function register()
    {
        // Generate licenses when order is paid
        add_action('fluent_cart/order_paid', [$this, 'maybeGenerateLicensesOnPurchaseSuccess'], 10, 1);

        // Revoke licenses on full refund
        add_action('fluent_cart/order_fully_refunded', [$this, 'maybeRevokeLicensesOnFullRefund'], 10, 1);

        // Extend licenses on subscription renewal
        add_action('fluent_cart/subscription_renewed', [$this, 'maybeExtendOnRenewal'], 10, 1);

        // Expire licenses when subscription expires
        add_action('fluent_cart/payments/subscription_expired', [$this, 'maybeExpireLicenseOnSubscriptionExpired'], 10, 1);
    }

    public function maybeGenerateLicensesOnPurchaseSuccess($order)
    {
        // Check if products require licenses
        foreach ($order->order_items as $item) {
            if ($this->productRequiresLicense($item->product_id)) {
                $this->generateLicenseForItem($order, $item);
            }
        }
    }
}
```

## License Hooks and Filters [​](https://dev.fluentcart.com/api/licensing\#license-hooks-and-filters)

### License Generation Hooks [​](https://dev.fluentcart.com/api/licensing\#license-generation-hooks)

php

```
// Before license generation
add_action('fluent_cart/license/before_generate', function($order, $product) {
    // Custom validation before generating license
    if ($product->requires_manual_approval) {
        // Queue for manual approval
        return false;
    }
}, 10, 2);

// After license generation
add_action('fluent_cart/license/generated', function($license) {
    // Send license email to customer
    wp_mail(
        $license->customer->email,
        'Your License Key',
        "Your license key: {$license->license_key}"
    );

    // Log license generation
    error_log("License generated: {$license->license_key}");
}, 10, 1);

// License activation
add_action('fluent_cart/license/activated', function($license, $domain) {
    // Track activation
    $license->incrementActivationCount();

    // Send activation confirmation
    wp_mail(
        $license->customer->email,
        'License Activated',
        "Your license has been activated on {$domain}"
    );
}, 10, 2);
```

### License Filters [​](https://dev.fluentcart.com/api/licensing\#license-filters)

php

```
// Modify license data in customer view
add_filter('fluent_cart/customer/view', function($customer, $args) {
    $licenses = License::where('customer_id', $customer->id)->get();

    if (!$licenses->isEmpty()) {
        $customer->licenses = $licenses->map(function($license) {
            return [\
                'id' => $license->id,\
                'product_name' => $license->product->post_title,\
                'license_key' => $license->license_key,\
                'status' => $license->status,\
                'expires_at' => $license->expiration_date\
            ];
        });
    }

    return $customer;
}, 10, 2);

// Modify license data in order view
add_filter('fluent_cart/order/view', function($order, $args) {
    $licenses = License::where('order_id', $order->id)->get();

    if (!$licenses->isEmpty()) {
        $order['licenses'] = $licenses;
    }

    return $order;
}, 10, 2);
```

## License Validation [​](https://dev.fluentcart.com/api/licensing\#license-validation)

php

```
use FluentCartPro\App\Modules\Licensing\Services\LicenseHelper;

// Validate license key
$isValid = LicenseHelper::validateLicenseKey($licenseKey, $domain);

if ($isValid) {
    echo "License is valid";
} else {
    echo "Invalid license";
}

// Check license status
$status = LicenseHelper::getLicenseStatus($licenseKey);
// Returns: 'active', 'inactive', 'expired', 'suspended'
```

## Error Handling [​](https://dev.fluentcart.com/api/licensing\#error-handling)

### Common Error Responses [​](https://dev.fluentcart.com/api/licensing\#common-error-responses)

#### Invalid License Key [​](https://dev.fluentcart.com/api/licensing\#invalid-license-key)

json

```
{
  "message": "Invalid license key",
  "errors": [\
    {\
      "code": 400,\
      "message": "Invalid license key"\
    }\
  ]
}
```

#### License Not Found [​](https://dev.fluentcart.com/api/licensing\#license-not-found)

json

```
{
  "message": "License not found",
  "errors": [\
    {\
      "code": 404,\
      "message": "License not found"\
    }\
  ]
}
```

#### Domain Limit Reached [​](https://dev.fluentcart.com/api/licensing\#domain-limit-reached)

json

```
{
  "message": "License domain limit reached",
  "errors": [\
    {\
      "code": 403,\
      "message": "License domain limit reached"\
    }\
  ]
}
```

#### License Already Active [​](https://dev.fluentcart.com/api/licensing\#license-already-active)

json

```
{
  "message": "License already active",
  "errors": [\
    {\
      "code": 409,\
      "message": "License already active"\
    }\
  ]
}
```

* * *

**Related Documentation:**

- [Roles & Permissions API](https://dev.fluentcart.com/api/roles-permissions.html) \- User role management
- [Order Bump API](https://dev.fluentcart.com/api/order-bump.html) \- Promotional features
- [REST API Overview](https://dev.fluentcart.com/api/) \- General API information

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

## Order Bump API (Pro) | FluentCart Developer Docs

**URL** : https://dev.fluentcart.com/api/order-bump

[Skip to content](https://dev.fluentcart.com/api/order-bump#VPContent)

# Order Bump API (Pro) [​](https://dev.fluentcart.com/api/order-bump\#order-bump-api-pro)

The Order Bump system provides advanced promotional tools for increasing average order value through strategic product offers during the checkout process. Order bumps are implemented through hooks and filters rather than REST API endpoints.

## Implementation [​](https://dev.fluentcart.com/api/order-bump\#implementation)

Order bumps are handled through the `FluentCartPro\App\Modules\Promotional\OrderBump\OrderBumpBoot` class and use the `OrderPromotion` model with `type = 'order_bump'`.

## Order Bump Hooks and Filters [​](https://dev.fluentcart.com/api/order-bump\#order-bump-hooks-and-filters)

### 1\. Display Order Bumps [​](https://dev.fluentcart.com/api/order-bump\#_1-display-order-bumps)

Order bumps are displayed during checkout using this action hook:

- **Action Hook:**`fluent_cart/after_order_notes`
- **Description:** Displays available order bumps during the checkout process
- **Parameters:**
  - `$data` (array): Contains the cart object and other checkout data
- **Implementation:** Handled by `OrderBumpBoot::maybeShowBumps()`

### 2\. Apply/Remove Order Bump [​](https://dev.fluentcart.com/api/order-bump\#_2-apply-remove-order-bump)

This filter is used internally by FluentCart to apply or remove an order bump from the cart based on user interaction during checkout.

- **Filter Hook:**`fluent_cart/apply_order_bump`
- **Description:** Handles the logic for adding or removing an order bump product to/from the cart.
- **Parameters:**
  - `$message` (string): A default success or error message.
  - `$data`(array): An array containing:
    - `cart` (object): The current cart object.
    - `bump_id` (int): The ID of the order bump.
    - `request_data` (array): Request data, typically including `is_upgraded` ('yes' or 'no') to indicate if the bump should be added or removed.
- **Return:** A success message (string) or a `WP_Error` object if the operation fails.
- **Use Case:** Custom validation for applying bumps, adding custom tracking, or sending notifications when a bump is added/removed.

**Example Usage (within a custom plugin):**

php

```
add_filter('fluent_cart/apply_order_bump', function($message, $data) {
    $cart = $data['cart'];
    $bumpId = $data['bump_id'] ?? 0;
    $willAdd = ($data['request_data']['is_upgraded'] ?? '') === 'yes';

    // Custom validation logic: Prevent adding bump if cart total is too high
    if ($willAdd && $cart->total > 500) {
        return new WP_Error('bump_limit_exceeded', 'This order bump cannot be added to orders over $500.');
    }

    // Custom tracking or logging
    if ($willAdd) {
        error_log("Order Bump #{$bumpId} added to cart for customer {$cart->customer_id}");
    } else {
        error_log("Order Bump #{$bumpId} removed from cart for customer {$cart->customer_id}");
    }

    return $message; // Return the original message or a custom one
}, 10, 2);
```

## Order Bump Model [​](https://dev.fluentcart.com/api/order-bump\#order-bump-model)

### OrderPromotion Model [​](https://dev.fluentcart.com/api/order-bump\#orderpromotion-model)

php

```
use FluentCartPro\App\Modules\Promotional\Models\OrderPromotion;

class OrderPromotion extends Model
{
    protected $table = 'fct_order_promotions';

    protected $fillable = [\
        'title',\
        'description',\
        'product_id',\
        'variation_id',\
        'discount_type',\
        'discount_value',\
        'is_active',\
        'conditions',\
        'settings'\
    ];

    protected $casts = [\
        'conditions' => 'array',\
        'settings' => 'array',\
        'is_active' => 'boolean'\
    ];
}
```

### Creating Order Bumps [​](https://dev.fluentcart.com/api/order-bump\#creating-order-bumps)

php

```
// Create an order bump
$orderBump = OrderPromotion::create([\
    'title' => 'Premium Support Add-on',\
    'description' => 'Get 1 year of premium support with your purchase',\
    'product_id' => 123,\
    'variation_id' => 456,\
    'discount_type' => 'percentage',\
    'discount_value' => 20, // 20% off\
    'is_active' => true,\
    'conditions' => [\
        'minimum_cart_total' => 5000, // $50 minimum\
        'product_categories' => ['software', 'plugins'],\
        'customer_segments' => ['new_customers']\
    ],\
    'settings' => [\
        'display_position' => 'after_order_notes',\
        'auto_select' => false,\
        'show_urgency' => true\
    ]\
]);
```

## Order Bump Display [​](https://dev.fluentcart.com/api/order-bump\#order-bump-display)

### Order Bump Boot Class [​](https://dev.fluentcart.com/api/order-bump\#order-bump-boot-class)

php

```
use FluentCartPro\App\Modules\Promotional\OrderBump\OrderBumpBoot;

class OrderBumpBoot
{
    public function register()
    {
        // Display order bumps in checkout
        add_action('fluent_cart/after_order_notes', [$this, 'maybeShowBumps']);

        // Handle order bump application
        add_filter('fluent_cart/apply_order_bump', [$this, 'applyOrderBump'], 10, 2);
    }

    public function maybeShowBumps($data)
    {
        $cart = $data['cart'];
        $availableBumps = $this->getAvailableBumps($cart);

        if (!empty($availableBumps)) {
            $this->renderOrderBumps($availableBumps, $cart);
        }
    }

    private function getAvailableBumps($cart)
    {
        return OrderPromotion::where('is_active', true)
            ->where(function($query) use ($cart) {
                $query->whereNull('conditions->minimum_cart_total')
                      ->orWhere('conditions->minimum_cart_total', '<=', $cart->total);
            })
            ->get();
    }
}
```

### Order Bump Application [​](https://dev.fluentcart.com/api/order-bump\#order-bump-application)

php

```
// Apply order bump to cart
add_filter('fluent_cart/apply_order_bump', function($message, $data) {
    $cart = $data['cart'];
    $bumpId = $data['bump_id'] ?? 0;
    $willAdd = $data['request_data']['is_upgraded'] ?? false;

    if ($willAdd) {
        $bump = OrderPromotion::find($bumpId);

        if ($bump && $this->isBumpAvailable($bump, $cart)) {
            // Add bump product to cart
            $cart->addItem([\
                'product_id' => $bump->product_id,\
                'variation_id' => $bump->variation_id,\
                'quantity' => 1,\
                'is_bump' => true,\
                'bump_id' => $bumpId\
            ]);

            return "Order bump added successfully";
        }
    } else {
        // Remove bump from cart
        $cart->removeBumpItems($bumpId);
        return "Order bump removed";
    }

    return $message;
}, 10, 2);
```

## Order Bump Conditions [​](https://dev.fluentcart.com/api/order-bump\#order-bump-conditions)

### Condition Types [​](https://dev.fluentcart.com/api/order-bump\#condition-types)

#### Minimum Cart Total [​](https://dev.fluentcart.com/api/order-bump\#minimum-cart-total)

php

```
'conditions' => [\
    'minimum_cart_total' => 5000, // $50 minimum\
]
```

#### Product Categories [​](https://dev.fluentcart.com/api/order-bump\#product-categories)

php

```
'conditions' => [\
    'product_categories' => ['software', 'plugins', 'themes']\
]
```

#### Customer Segments [​](https://dev.fluentcart.com/api/order-bump\#customer-segments)

php

```
'conditions' => [\
    'customer_segments' => ['new_customers', 'returning_customers']\
]
```

#### Excluded Products [​](https://dev.fluentcart.com/api/order-bump\#excluded-products)

php

```
'conditions' => [\
    'excluded_products' => [123, 456, 789]\
]
```

#### Date Range [​](https://dev.fluentcart.com/api/order-bump\#date-range)

php

```
'conditions' => [\
    'start_date' => '2024-01-01',\
    'end_date' => '2024-12-31'\
]
```

### Custom Conditions [​](https://dev.fluentcart.com/api/order-bump\#custom-conditions)

php

```
// Custom condition validation
add_filter('fluent_cart/order_bump/conditions', function($conditions, $bump, $cart) {
    // Add custom conditions
    $conditions['custom_condition'] = $this->checkCustomCondition($cart);

    return $conditions;
}, 10, 3);

private function checkCustomCondition($cart)
{
    // Custom logic here
    return $cart->customer->total_orders > 5;
}
```

## Order Bump Hooks and Filters [​](https://dev.fluentcart.com/api/order-bump\#order-bump-hooks-and-filters-1)

### Order Bump Hooks [​](https://dev.fluentcart.com/api/order-bump\#order-bump-hooks)

php

```
// Before order bump is displayed
add_action('fluent_cart/order_bump/before_display', function($bump, $cart) {
    // Custom logic before displaying bump
    if ($cart->hasCoupon('NO_BUMPS')) {
        return false; // Don't show bumps
    }
}, 10, 2);

// After order bump is applied
add_action('fluent_cart/order_bump/applied', function($bump, $cart) {
    // Track bump application
    error_log("Order bump applied: {$bump->title} to cart {$cart->id}");

    // Send notification
    wp_mail(
        get_option('admin_email'),
        'Order Bump Applied',
        "Order bump '{$bump->title}' was applied to a cart"
    );
}, 10, 2);

// Order bump conditions
add_action('fluent_cart/order_bump/conditions', function($conditions, $bump, $cart) {
    // Add custom conditions
    $conditions['custom_condition'] = $this->checkCustomCondition($cart);

    return $conditions;
}, 10, 3);
```

### Order Bump Filters [​](https://dev.fluentcart.com/api/order-bump\#order-bump-filters)

php

```
// Modify order bump display
add_filter('fluent_cart/order_bump/display_data', function($data, $bump, $cart) {
    // Add custom data to bump display
    $data['custom_message'] = "Limited time offer!";
    $data['urgency_text'] = "Only 3 left in stock!";

    return $data;
}, 10, 3);

// Modify promotional settings
add_filter('fluent_cart/promotional/settings', function($settings) {
    // Add custom promotional settings
    $settings['custom_promotion'] = [\
        'title' => 'Custom Promotion',\
        'type' => 'checkbox',\
        'default' => false\
    ];

    return $settings;
});
```

## Order Bump Settings [​](https://dev.fluentcart.com/api/order-bump\#order-bump-settings)

### Display Settings [​](https://dev.fluentcart.com/api/order-bump\#display-settings)

php

```
'settings' => [\
    'display_position' => 'after_order_notes', // Where to show the bump\
    'auto_select' => false, // Auto-select the bump\
    'show_urgency' => true, // Show urgency messaging\
    'urgency_text' => 'Limited time offer!',\
    'discount_display' => 'percentage', // How to show discount\
    'button_text' => 'Add to Order',\
    'decline_text' => 'No Thanks'\
]
```

### Styling Settings [​](https://dev.fluentcart.com/api/order-bump\#styling-settings)

php

```
'settings' => [\
    'background_color' => '#f8f9fa',\
    'border_color' => '#dee2e6',\
    'text_color' => '#212529',\
    'button_color' => '#007cba',\
    'button_text_color' => '#ffffff'\
]
```

## Order Bump Analytics [​](https://dev.fluentcart.com/api/order-bump\#order-bump-analytics)

### Tracking Bump Performance [​](https://dev.fluentcart.com/api/order-bump\#tracking-bump-performance)

php

```
// Track bump views
add_action('fluent_cart/order_bump/viewed', function($bump, $cart) {
    // Log bump view
    error_log("Order bump viewed: {$bump->title} by customer {$cart->customer_id}");

    // Store analytics data
    $this->storeBumpAnalytics($bump->id, 'viewed', $cart->customer_id);
}, 10, 2);

// Track bump conversions
add_action('fluent_cart/order_bump/converted', function($bump, $cart, $order) {
    // Log bump conversion
    error_log("Order bump converted: {$bump->title} in order {$order->id}");

    // Store conversion data
    $this->storeBumpAnalytics($bump->id, 'converted', $cart->customer_id, $order->id);
}, 10, 3);

private function storeBumpAnalytics($bumpId, $action, $customerId, $orderId = null)
{
    // Store analytics data in database or external service
    $analytics = [\
        'bump_id' => $bumpId,\
        'action' => $action,\
        'customer_id' => $customerId,\
        'order_id' => $orderId,\
        'timestamp' => current_time('mysql')\
    ];

    // Store in custom analytics table or external service
    $this->analyticsService->store($analytics);
}
```

* * *

**Related Documentation:**

- [Licensing API](https://dev.fluentcart.com/api/licensing.html) \- Software license management
- [Roles & Permissions API](https://dev.fluentcart.com/api/roles-permissions.html) \- User role management
- [REST API Overview](https://dev.fluentcart.com/api/) \- General API information

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

## Orders API | FluentCart Developer Docs

**URL** : https://dev.fluentcart.com/api/orders

[Skip to content](https://dev.fluentcart.com/api/orders#VPContent)

# Orders API [​](https://dev.fluentcart.com/api/orders\#orders-api)

The Orders API provides comprehensive endpoints for managing orders in FluentCart. This includes creating, reading, updating, and deleting orders, as well as managing order statuses, payments, and related operations.

## Base URL [​](https://dev.fluentcart.com/api/orders\#base-url)

```
https://yoursite.com/wp-json/fluent-cart/v2/orders
```

## Authentication [​](https://dev.fluentcart.com/api/orders\#authentication)

All endpoints require authentication and appropriate permissions:

- **Authentication**: WordPress Application Password or Cookie
- **Policy**: `OrderPolicy`
- **Permissions**: Various order-related permissions

## Endpoints [​](https://dev.fluentcart.com/api/orders\#endpoints)

### List Orders [​](https://dev.fluentcart.com/api/orders\#list-orders)

**GET**`/orders`

Retrieve a paginated list of orders with optional filtering and searching.

#### Parameters [​](https://dev.fluentcart.com/api/orders\#parameters)

| Parameter | Type | Description | Default |
| --- | --- | --- | --- |
| `page` | integer | Page number | 1 |
| `per_page` | integer | Items per page (max 100) | 10 |
| `search` | string | Search query | - |
| `filters` | object | Filter options | - |
| `order_by` | string | Sort field | id |
| `order_type` | string | Sort direction (ASC/DESC) | DESC |

#### Filter Options [​](https://dev.fluentcart.com/api/orders\#filter-options)

json

```
{
  "status": "completed",
  "payment_status": "paid",
  "customer_id": 123,
  "date_from": "2024-01-01",
  "date_to": "2024-12-31"
}
```

#### Response [​](https://dev.fluentcart.com/api/orders\#response)

json

```
{
  "success": true,
  "data": {
    "orders": [\
      {\
        "id": 1,\
        "uuid": "abc123",\
        "status": "completed",\
        "payment_status": "paid",\
        "customer_id": 123,\
        "total_amount": 5000,\
        "currency": "USD",\
        "created_at": "2024-01-01T10:00:00Z",\
        "customer": {\
          "id": 123,\
          "email": "customer@example.com",\
          "first_name": "John",\
          "last_name": "Doe"\
        },\
        "order_items": [\
          {\
            "id": 1,\
            "product_id": 456,\
            "variation_id": 789,\
            "quantity": 2,\
            "price": 2500\
          }\
        ]\
      }\
    ],
    "pagination": {
      "current_page": 1,
      "per_page": 10,
      "total": 100,
      "total_pages": 10
    }
  }
}
```

#### Example Request [​](https://dev.fluentcart.com/api/orders\#example-request)

bash

```
curl -X GET "https://yoursite.com/wp-json/fluent-cart/v1/orders?page=1&per_page=20&search=john" \
  -H "Authorization: Basic dXNlcm5hbWU6YXBwbGljYXRpb25fcGFzc3dvcmQ="
```

### Create Order [​](https://dev.fluentcart.com/api/orders\#create-order)

**POST**`/orders`

Create a new order with items and customer information.

#### Request Body [​](https://dev.fluentcart.com/api/orders\#request-body)

json

```
{
  "customer_id": 123,
  "items": [\
    {\
      "product_id": 456,\
      "variation_id": 789,\
      "quantity": 2\
    }\
  ],
  "billing_address": {
    "first_name": "John",
    "last_name": "Doe",
    "email": "john@example.com",
    "address_1": "123 Main St",
    "city": "New York",
    "state": "NY",
    "postcode": "10001",
    "country": "US"
  },
  "shipping_address": {
    "first_name": "John",
    "last_name": "Doe",
    "address_1": "123 Main St",
    "city": "New York",
    "state": "NY",
    "postcode": "10001",
    "country": "US"
  },
  "payment_method": "stripe",
  "note": "Special delivery instructions"
}
```

#### Response [​](https://dev.fluentcart.com/api/orders\#response-1)

json

```
{
  "success": true,
  "data": {
    "order": {
      "id": 1,
      "uuid": "abc123",
      "status": "pending",
      "payment_status": "pending",
      "total_amount": 5000,
      "currency": "USD",
      "created_at": "2024-01-01T10:00:00Z"
    }
  }
}
```

#### Example Request [​](https://dev.fluentcart.com/api/orders\#example-request-1)

bash

```
curl -X POST "https://yoursite.com/wp-json/fluent-cart/v1/orders" \
  -H "Authorization: Basic dXNlcm5hbWU6YXBwbGljYXRpb25fcGFzc3dvcmQ=" \
  -H "Content-Type: application/json" \
  -d '{
    "customer_id": 123,
    "items": [\
      {\
        "product_id": 456,\
        "variation_id": 789,\
        "quantity": 2\
      }\
    ],
    "payment_method": "stripe"
  }'
```

### Get Order Details [​](https://dev.fluentcart.com/api/orders\#get-order-details)

**GET**`/orders/{id}`

Retrieve detailed information about a specific order.

#### Parameters [​](https://dev.fluentcart.com/api/orders\#parameters-1)

| Parameter | Type | Description |
| --- | --- | --- |
| `id` | integer | Order ID |

#### Response [​](https://dev.fluentcart.com/api/orders\#response-2)

json

```
{
  "success": true,
  "data": {
    "order": {
      "id": 1,
      "uuid": "abc123",
      "status": "completed",
      "payment_status": "paid",
      "customer_id": 123,
      "total_amount": 5000,
      "currency": "USD",
      "created_at": "2024-01-01T10:00:00Z",
      "customer": {
        "id": 123,
        "email": "customer@example.com",
        "first_name": "John",
        "last_name": "Doe"
      },
      "order_items": [\
        {\
          "id": 1,\
          "product_id": 456,\
          "variation_id": 789,\
          "quantity": 2,\
          "price": 2500,\
          "product": {\
            "id": 456,\
            "title": "Sample Product",\
            "sku": "SP-001"\
          }\
        }\
      ],
      "transactions": [\
        {\
          "id": 1,\
          "payment_method": "stripe",\
          "status": "succeeded",\
          "amount": 5000,\
          "transaction_id": "txn_123456"\
        }\
      ]
    }
  }
}
```

#### Example Request [​](https://dev.fluentcart.com/api/orders\#example-request-2)

bash

```
curl -X GET "https://yoursite.com/wp-json/fluent-cart/v1/orders/1" \
  -H "Authorization: Basic dXNlcm5hbWU6YXBwbGljYXRpb25fcGFzc3dvcmQ="
```

### Update Order [​](https://dev.fluentcart.com/api/orders\#update-order)

**PUT**`/orders/{id}`

Update an existing order's information.

#### Parameters [​](https://dev.fluentcart.com/api/orders\#parameters-2)

| Parameter | Type | Description |
| --- | --- | --- |
| `id` | integer | Order ID |

#### Request Body [​](https://dev.fluentcart.com/api/orders\#request-body-1)

json

```
{
  "status": "processing",
  "note": "Updated order note",
  "billing_address": {
    "first_name": "John",
    "last_name": "Doe",
    "email": "john@example.com"
  }
}
```

#### Response [​](https://dev.fluentcart.com/api/orders\#response-3)

json

```
{
  "success": true,
  "data": {
    "order": {
      "id": 1,
      "status": "processing",
      "note": "Updated order note",
      "updated_at": "2024-01-01T11:00:00Z"
    }
  }
}
```

#### Example Request [​](https://dev.fluentcart.com/api/orders\#example-request-3)

bash

```
curl -X PUT "https://yoursite.com/wp-json/fluent-cart/v1/orders/1" \
  -H "Authorization: Basic dXNlcm5hbWU6YXBwbGljYXRpb25fcGFzc3dvcmQ=" \
  -H "Content-Type: application/json" \
  -d '{
    "status": "processing",
    "note": "Updated order note"
  }'
```

### Delete Order [​](https://dev.fluentcart.com/api/orders\#delete-order)

**DELETE**`/orders/{id}`

Delete an order (soft delete).

#### Parameters [​](https://dev.fluentcart.com/api/orders\#parameters-3)

| Parameter | Type | Description |
| --- | --- | --- |
| `id` | integer | Order ID |

#### Response [​](https://dev.fluentcart.com/api/orders\#response-4)

json

```
{
  "success": true,
  "message": "Order deleted successfully"
}
```

#### Example Request [​](https://dev.fluentcart.com/api/orders\#example-request-4)

bash

```
curl -X DELETE "https://yoursite.com/wp-json/fluent-cart/v1/orders/1" \
  -H "Authorization: Basic dXNlcm5hbWU6YXBwbGljYXRpb25fcGFzc3dvcmQ="
```

### Mark Order as Paid [​](https://dev.fluentcart.com/api/orders\#mark-order-as-paid)

**POST**`/orders/{id}/mark-as-paid`

Mark an order as paid manually.

#### Parameters [​](https://dev.fluentcart.com/api/orders\#parameters-4)

| Parameter | Type | Description |
| --- | --- | --- |
| `id` | integer | Order ID |

#### Request Body [​](https://dev.fluentcart.com/api/orders\#request-body-2)

json

```
{
  "payment_method": "manual",
  "transaction_id": "manual_123",
  "note": "Manual payment confirmation"
}
```

#### Response [​](https://dev.fluentcart.com/api/orders\#response-5)

json

```
{
  "success": true,
  "data": {
    "order": {
      "id": 1,
      "payment_status": "paid",
      "updated_at": "2024-01-01T11:00:00Z"
    }
  }
}
```

#### Example Request [​](https://dev.fluentcart.com/api/orders\#example-request-5)

bash

```
curl -X POST "https://yoursite.com/wp-json/fluent-cart/v1/orders/1/mark-as-paid" \
  -H "Authorization: Basic dXNlcm5hbWU6YXBwbGljYXRpb25fcGFzc3dvcmQ=" \
  -H "Content-Type: application/json" \
  -d '{
    "payment_method": "manual",
    "transaction_id": "manual_123"
  }'
```

### Refund Order [​](https://dev.fluentcart.com/api/orders\#refund-order)

**POST**`/orders/{id}/refund`

Process a refund for an order.

#### Parameters [​](https://dev.fluentcart.com/api/orders\#parameters-5)

| Parameter | Type | Description |
| --- | --- | --- |
| `id` | integer | Order ID |

#### Request Body [​](https://dev.fluentcart.com/api/orders\#request-body-3)

json

```
{
  "amount": 2500,
  "reason": "Customer requested refund",
  "refund_method": "original_payment_method"
}
```

#### Response [​](https://dev.fluentcart.com/api/orders\#response-6)

json

```
{
  "success": true,
  "data": {
    "refund": {
      "id": 1,
      "order_id": 1,
      "amount": 2500,
      "status": "completed",
      "refund_id": "ref_123456",
      "created_at": "2024-01-01T11:00:00Z"
    }
  }
}
```

#### Example Request [​](https://dev.fluentcart.com/api/orders\#example-request-6)

bash

```
curl -X POST "https://yoursite.com/wp-json/fluent-cart/v1/orders/1/refund" \
  -H "Authorization: Basic dXNlcm5hbWU6YXBwbGljYXRpb25fcGFzc3dvcmQ=" \
  -H "Content-Type: application/json" \
  -d '{
    "amount": 2500,
    "reason": "Customer requested refund"
  }'
```

### Update Order Statuses [​](https://dev.fluentcart.com/api/orders\#update-order-statuses)

**PUT**`/orders/{id}/statuses`

Update order statuses (payment status, shipping status, order status).

#### Parameters [​](https://dev.fluentcart.com/api/orders\#parameters-6)

| Parameter | Type | Description |
| --- | --- | --- |
| `id` | integer | Order ID |

#### Request Body [​](https://dev.fluentcart.com/api/orders\#request-body-4)

json

```
{
  "payment_status": "paid",
  "shipping_status": "shipped",
  "order_status": "processing"
}
```

#### Response [​](https://dev.fluentcart.com/api/orders\#response-7)

json

```
{
  "success": true,
  "data": {
    "order": {
      "id": 1,
      "payment_status": "paid",
      "shipping_status": "shipped",
      "order_status": "processing",
      "updated_at": "2024-01-01T11:00:00Z"
    }
  }
}
```

#### Example Request [​](https://dev.fluentcart.com/api/orders\#example-request-7)

bash

```
curl -X PUT "https://yoursite.com/wp-json/fluent-cart/v1/orders/1/statuses" \
  -H "Authorization: Basic dXNlcm5hbWU6YXBwbGljYXRpb25fcGFzc3dvcmQ=" \
  -H "Content-Type: application/json" \
  -d '{
    "payment_status": "paid",
    "shipping_status": "shipped"
  }'
```

### Change Order Customer [​](https://dev.fluentcart.com/api/orders\#change-order-customer)

**POST**`/orders/{id}/change-customer`

Change the customer associated with an order.

#### Parameters [​](https://dev.fluentcart.com/api/orders\#parameters-7)

| Parameter | Type | Description |
| --- | --- | --- |
| `id` | integer | Order ID |

#### Request Body [​](https://dev.fluentcart.com/api/orders\#request-body-5)

json

```
{
  "customer_id": 456
}
```

#### Response [​](https://dev.fluentcart.com/api/orders\#response-8)

json

```
{
  "success": true,
  "data": {
    "order": {
      "id": 1,
      "customer_id": 456,
      "updated_at": "2024-01-01T11:00:00Z"
    }
  }
}
```

#### Example Request [​](https://dev.fluentcart.com/api/orders\#example-request-8)

bash

```
curl -X POST "https://yoursite.com/wp-json/fluent-cart/v1/orders/1/change-customer" \
  -H "Authorization: Basic dXNlcm5hbWU6YXBwbGljYXRpb25fcGFzc3dvcmQ=" \
  -H "Content-Type: application/json" \
  -d '{
    "customer_id": 456
  }'
```

### Create and Change Customer [​](https://dev.fluentcart.com/api/orders\#create-and-change-customer)

**POST**`/orders/{id}/create-and-change-customer`

Create a new customer and associate them with the order.

#### Parameters [​](https://dev.fluentcart.com/api/orders\#parameters-8)

| Parameter | Type | Description |
| --- | --- | --- |
| `id` | integer | Order ID |

#### Request Body [​](https://dev.fluentcart.com/api/orders\#request-body-6)

json

```
{
  "email": "newcustomer@example.com",
  "first_name": "Jane",
  "last_name": "Smith"
}
```

#### Response [​](https://dev.fluentcart.com/api/orders\#response-9)

json

```
{
  "success": true,
  "data": {
    "order": {
      "id": 1,
      "customer_id": 789,
      "updated_at": "2024-01-01T11:00:00Z"
    },
    "customer": {
      "id": 789,
      "email": "newcustomer@example.com",
      "first_name": "Jane",
      "last_name": "Smith"
    }
  }
}
```

#### Example Request [​](https://dev.fluentcart.com/api/orders\#example-request-9)

bash

```
curl -X POST "https://yoursite.com/wp-json/fluent-cart/v1/orders/1/create-and-change-customer" \
  -H "Authorization: Basic dXNlcm5hbWU6YXBwbGljYXRpb25fcGFzc3dvcmQ=" \
  -H "Content-Type: application/json" \
  -d '{
    "email": "newcustomer@example.com",
    "first_name": "Jane",
    "last_name": "Smith"
  }'
```

### Bulk Actions [​](https://dev.fluentcart.com/api/orders\#bulk-actions)

**POST**`/orders/do-bulk-action`

Perform bulk actions on multiple orders.

#### Request Body [​](https://dev.fluentcart.com/api/orders\#request-body-7)

json

```
{
  "action": "update_status",
  "order_ids": [1, 2, 3],
  "data": {
    "status": "completed"
  }
}
```

#### Available Actions [​](https://dev.fluentcart.com/api/orders\#available-actions)

- `update_status` \- Update status of multiple orders
- `delete` \- Delete multiple orders
- `export` \- Export multiple orders

#### Response [​](https://dev.fluentcart.com/api/orders\#response-10)

json

```
{
  "success": true,
  "data": {
    "processed": 3,
    "failed": 0,
    "results": [\
      {\
        "order_id": 1,\
        "success": true\
      },\
      {\
        "order_id": 2,\
        "success": true\
      },\
      {\
        "order_id": 3,\
        "success": true\
      }\
    ]
  }
}
```

#### Example Request [​](https://dev.fluentcart.com/api/orders\#example-request-10)

bash

```
curl -X POST "https://yoursite.com/wp-json/fluent-cart/v1/orders/do-bulk-action" \
  -H "Authorization: Basic dXNlcm5hbWU6YXBwbGljYXRpb25fcGFzc3dvcmQ=" \
  -H "Content-Type: application/json" \
  -d '{
    "action": "update_status",
    "order_ids": [1, 2, 3],
    "data": {
      "status": "completed"
    }
  }'
```

### Calculate Shipping [​](https://dev.fluentcart.com/api/orders\#calculate-shipping)

**POST**`/orders/calculate-shipping`

Calculate shipping costs for an order.

#### Request Body [​](https://dev.fluentcart.com/api/orders\#request-body-8)

json

```
{
  "items": [\
    {\
      "product_id": 456,\
      "variation_id": 789,\
      "quantity": 2\
    }\
  ],
  "shipping_address": {
    "country": "US",
    "state": "NY",
    "postcode": "10001"
  }
}
```

#### Response [​](https://dev.fluentcart.com/api/orders\#response-11)

json

```
{
  "success": true,
  "data": {
    "shipping_methods": [\
      {\
        "id": "standard",\
        "name": "Standard Shipping",\
        "cost": 500,\
        "estimated_days": "3-5"\
      },\
      {\
        "id": "express",\
        "name": "Express Shipping",\
        "cost": 1000,\
        "estimated_days": "1-2"\
      }\
    ]
  }
}
```

#### Example Request [​](https://dev.fluentcart.com/api/orders\#example-request-11)

bash

```
curl -X POST "https://yoursite.com/wp-json/fluent-cart/v1/orders/calculate-shipping" \
  -H "Authorization: Basic dXNlcm5hbWU6YXBwbGljYXRpb25fcGFzc3dvcmQ=" \
  -H "Content-Type: application/json" \
  -d '{
    "items": [\
      {\
        "product_id": 456,\
        "variation_id": 789,\
        "quantity": 2\
      }\
    ],
    "shipping_address": {
      "country": "US",
      "state": "NY",
      "postcode": "10001"
    }
  }'
```

### Get Shipping Methods [​](https://dev.fluentcart.com/api/orders\#get-shipping-methods)

**GET**`/orders/shipping_methods`

Get available shipping methods.

#### Response [​](https://dev.fluentcart.com/api/orders\#response-12)

json

```
{
  "success": true,
  "data": {
    "shipping_methods": [\
      {\
        "id": "standard",\
        "name": "Standard Shipping",\
        "description": "Standard ground shipping",\
        "cost": 500,\
        "estimated_days": "3-5"\
      },\
      {\
        "id": "express",\
        "name": "Express Shipping",\
        "description": "Express shipping",\
        "cost": 1000,\
        "estimated_days": "1-2"\
      }\
    ]
  }
}
```

#### Example Request [​](https://dev.fluentcart.com/api/orders\#example-request-12)

bash

```
curl -X GET "https://yoursite.com/wp-json/fluent-cart/v1/orders/shipping_methods" \
  -H "Authorization: Basic dXNlcm5hbWU6YXBwbGljYXRpb25fcGFzc3dvcmQ="
```

## Error Handling [​](https://dev.fluentcart.com/api/orders\#error-handling)

### Common Error Codes [​](https://dev.fluentcart.com/api/orders\#common-error-codes)

| Code | Description |
| --- | --- |
| `order_not_found` | Order with specified ID not found |
| `invalid_customer` | Customer ID is invalid |
| `invalid_product` | Product ID is invalid |
| `insufficient_permissions` | User lacks required permissions |
| `validation_error` | Request data validation failed |
| `payment_failed` | Payment processing failed |
| `refund_failed` | Refund processing failed |

### Error Response Example [​](https://dev.fluentcart.com/api/orders\#error-response-example)

json

```
{
  "success": false,
  "error": {
    "code": "order_not_found",
    "message": "Order with ID 999 not found"
  }
}
```

## Rate Limiting [​](https://dev.fluentcart.com/api/orders\#rate-limiting)

- **List operations**: 100 requests per hour
- **Create operations**: 50 requests per hour
- **Update operations**: 200 requests per hour
- **Delete operations**: 20 requests per hour

## Related Documentation [​](https://dev.fluentcart.com/api/orders\#related-documentation)

- [Customers API](https://dev.fluentcart.com/api/customers.html) \- Customer management endpoints
- [Products API](https://dev.fluentcart.com/api/products.html) \- Product management endpoints
- [Subscriptions API](https://dev.fluentcart.com/api/subscriptions.html) \- Subscription management endpoints
- [Database Models](https://dev.fluentcart.com/database/models.html) \- Order data models
- [Developer Hooks](https://dev.fluentcart.com/hooks/) \- Order-related hooks

## Next Steps [​](https://dev.fluentcart.com/api/orders\#next-steps)

Continue with order management:

1. **[Customers API](https://dev.fluentcart.com/api/customers.html)** \- Manage customer data
2. **[Products API](https://dev.fluentcart.com/api/products.html)** \- Manage product catalog
3. **[Subscriptions API](https://dev.fluentcart.com/api/subscriptions.html)** \- Manage recurring orders
4. **[Authentication Guide](https://dev.fluentcart.com/api/authentication.html)** \- API authentication

## Previous/Next Navigation [​](https://dev.fluentcart.com/api/orders\#previous-next-navigation)

- **Previous**: [API Overview](https://dev.fluentcart.com/api/) \- FluentCart REST API
- **Next**: [Customers API](https://dev.fluentcart.com/api/customers.html) \- Customer management endpoints

* * *

Today

Hi! I’m your AI assistant. How can I assist you today?

Just now

Powered by **FluentBot**


---

---

