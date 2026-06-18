# FluentCart Developer Docs - REST API Overview (Part 1/4)

Overview de l'API REST FluentCart : authentification, orders, products, customers, subscriptions, licensing, order-bump, roles & permissions.

---

## REST API | FluentCart Developer Docs

**URL** : https://dev.fluentcart.com/api/

[Skip to content](https://dev.fluentcart.com/api/#VPContent)

# FluentCart REST API [​](https://dev.fluentcart.com/api/\#fluentcart-rest-api)

FluentCart provides a comprehensive REST API that allows developers to interact with all e-commerce functionality programmatically. The API is built on WordPress's REST API foundation with FluentCart-specific endpoints and authentication.

## API Overview [​](https://dev.fluentcart.com/api/\#api-overview)

The FluentCart REST API provides programmatic access to:

- **Order Management** \- Create, read, update, and manage orders
- **Customer Management** \- Handle customer data and relationships
- **Product Management** \- Manage products, variations, and pricing
- **Payment Processing** \- Handle payments and transactions
- **Subscription Management** \- Manage recurring subscriptions
- **Coupon System** \- Apply and manage discount coupons
- **File Management** \- Handle file uploads and downloads
- **Settings Management** \- Configure store and module settings

## Base URL [​](https://dev.fluentcart.com/api/\#base-url)

All API endpoints are prefixed with the WordPress REST API base URL:

```
https://yoursite.com/wp-json/fluent-cart/v2/
```

## Authentication [​](https://dev.fluentcart.com/api/\#authentication)

FluentCart uses WordPress's built-in authentication system with additional policy-based authorization:

### 1\. WordPress Authentication [​](https://dev.fluentcart.com/api/\#_1-wordpress-authentication)

- **Cookie Authentication** \- For logged-in users
- **Application Passwords** \- For external applications
- **OAuth** \- For third-party integrations

### 2\. Policy-Based Authorization [​](https://dev.fluentcart.com/api/\#_2-policy-based-authorization)

FluentCart implements a policy system for fine-grained access control:

- **AdminPolicy** \- Super admin access
- **OrderPolicy** \- Order management permissions
- **CustomerPolicy** \- Customer management permissions
- **ProductPolicy** \- Product management permissions
- **CouponPolicy** \- Coupon management permissions

### Authentication Example [​](https://dev.fluentcart.com/api/\#authentication-example)

php

```
// Using WordPress Application Passwords
$headers = [\
    'Authorization' => 'Basic ' . base64_encode('username:application_password'),\
    'Content-Type' => 'application/json'\
];

$response = wp_remote_get('https://yoursite.com/wp-json/fluent-cart/v1/orders', [\
    'headers' => $headers\
]);
```

## Response Format [​](https://dev.fluentcart.com/api/\#response-format)

All API responses follow a consistent JSON format:

### Success Response [​](https://dev.fluentcart.com/api/\#success-response)

json

```
{
    "success": true,
    "data": {
        // Response data
    },
    "message": "Operation completed successfully"
}
```

### Error Response [​](https://dev.fluentcart.com/api/\#error-response)

json

```
{
    "success": false,
    "error": {
        "code": "error_code",
        "message": "Error description"
    }
}
```

## Pagination [​](https://dev.fluentcart.com/api/\#pagination)

List endpoints support pagination using WordPress's standard pagination parameters:

- `page` \- Page number (default: 1)
- `per_page` \- Items per page (default: 10, max: 100)

### Pagination Response [​](https://dev.fluentcart.com/api/\#pagination-response)

json

```
{
    "data": [...],
    "pagination": {
        "current_page": 1,
        "per_page": 10,
        "total": 100,
        "total_pages": 10
    }
}
```

## Core Endpoints [​](https://dev.fluentcart.com/api/\#core-endpoints)

### Orders API [​](https://dev.fluentcart.com/api/\#orders-api)

- `GET /orders` \- List orders
- `POST /orders` \- Create order
- `GET /orders/{id}` \- Get order details
- `PUT /orders/{id}` \- Update order
- `DELETE /orders/{id}` \- Delete order
- `POST /orders/{id}/mark-as-paid` \- Mark order as paid
- `POST /orders/{id}/refund` \- Refund order
- `PUT /orders/{id}/statuses` \- Update order statuses

[View Orders API Documentation →](https://dev.fluentcart.com/api/orders.html)

### Customers API [​](https://dev.fluentcart.com/api/\#customers-api)

- `GET /customers` \- List customers
- `POST /customers` \- Create customer
- `GET /customers/{id}` \- Get customer details
- `PUT /customers/{id}` \- Update customer
- `GET /customers/{id}/orders` \- Get customer orders
- `GET /customers/{id}/address` \- Get customer addresses
- `PUT /customers/{id}/address` \- Update customer address

[View Customers API Documentation →](https://dev.fluentcart.com/api/customers.html)

### Products API [​](https://dev.fluentcart.com/api/\#products-api)

- `GET /products` \- List products
- `POST /products` \- Create product
- `GET /products/{id}` \- Get product details
- `PUT /products/{id}` \- Update product
- `DELETE /products/{id}` \- Delete product
- `GET /products/variants` \- List product variations
- `POST /products/variants` \- Create product variation
- `PUT /products/variants/{id}` \- Update product variation

[View Products API Documentation →](https://dev.fluentcart.com/api/products.html)

### Subscriptions API [​](https://dev.fluentcart.com/api/\#subscriptions-api)

- `GET /subscriptions` \- List subscriptions
- `GET /subscriptions/{id}` \- Get subscription details
- `PUT /subscriptions/{id}` \- Update subscription
- `POST /subscriptions/{id}/cancel` \- Cancel subscription
- `POST /subscriptions/{id}/reactivate` \- Reactivate subscription

[View Subscriptions API Documentation →](https://dev.fluentcart.com/api/subscriptions.html)

### Coupons API [​](https://dev.fluentcart.com/api/\#coupons-api)

- `GET /coupons` \- List coupons
- `POST /coupons` \- Create coupon
- `GET /coupons/{id}` \- Get coupon details
- `PUT /coupons/{id}` \- Update coupon
- `DELETE /coupons/{id}` \- Delete coupon
- `POST /coupons/apply` \- Apply coupon
- `POST /coupons/cancel` \- Cancel coupon

### Settings API [​](https://dev.fluentcart.com/api/\#settings-api)

- `GET /settings/store` \- Get store settings
- `POST /settings/store` \- Update store settings
- `GET /settings/payment-methods` \- Get payment method settings
- `POST /settings/payment-methods` \- Update payment method settings
- `GET /settings/storage-drivers` \- Get storage driver settings
- `POST /settings/storage-drivers` \- Update storage driver settings

### File Management API [​](https://dev.fluentcart.com/api/\#file-management-api)

- `GET /files` \- List files
- `POST /files/upload` \- Upload file
- `DELETE /files/delete` \- Delete file
- `GET /files/bucket-list` \- Get file bucket list

### Integration API [​](https://dev.fluentcart.com/api/\#integration-api)

- `GET /integration/global-settings` \- Get global integration settings
- `POST /integration/global-settings` \- Update global integration settings
- `GET /integration/global-feeds` \- Get integration feeds
- `POST /integration/global-feeds/settings` \- Save integration feed settings

### Reports API [​](https://dev.fluentcart.com/api/\#reports-api)

- `GET /reports/overview` \- Get overview report
- `GET /reports/orders` \- Get order report
- `GET /reports/customers` \- Get customer report
- `GET /reports/products` \- Get product report
- `GET /reports/revenue` \- Get revenue report

## Pro Endpoints ⭐ **PRO ONLY** [​](https://dev.fluentcart.com/api/\#pro-endpoints-%E2%AD%90-pro-only)

### Licensing API (Pro) [​](https://dev.fluentcart.com/api/\#licensing-api-pro)

- `GET /licenses` \- List licenses
- `POST /licenses` \- Create license
- `GET /licenses/{id}` \- Get license details
- `PUT /licenses/{id}` \- Update license
- `POST /licenses/{id}/activate` \- Activate license

[View Licensing API Documentation →](https://dev.fluentcart.com/api/licensing.html)

### Roles & Permissions API (Pro) [​](https://dev.fluentcart.com/api/\#roles-permissions-api-pro)

- `GET /settings/permissions` \- Get permissions
- `POST /settings/permissions` \- Update permissions
- `GET /users/{id}/capabilities` \- Get user capabilities
- `POST /users/{id}/capabilities` \- Update user capabilities

[View Roles & Permissions API Documentation →](https://dev.fluentcart.com/api/roles-permissions.html)

### Order Bump API (Pro) [​](https://dev.fluentcart.com/api/\#order-bump-api-pro)

- `GET /order-bumps` \- List order bumps
- `POST /order-bumps` \- Create order bump
- `GET /order-bumps/{id}` \- Get order bump details
- `PUT /order-bumps/{id}` \- Update order bump
- `DELETE /order-bumps/{id}` \- Delete order bump

[View Order Bump API Documentation →](https://dev.fluentcart.com/api/order-bump.html)

## Frontend Endpoints [​](https://dev.fluentcart.com/api/\#frontend-endpoints)

### Cart API [​](https://dev.fluentcart.com/api/\#cart-api)

- `GET /cart` \- Get cart contents
- `POST /cart/add` \- Add item to cart
- `PUT /cart/update` \- Update cart item
- `DELETE /cart/remove` \- Remove item from cart
- `POST /cart/apply-coupon` \- Apply coupon to cart

### Checkout API [​](https://dev.fluentcart.com/api/\#checkout-api)

- `POST /checkout/process` \- Process checkout
- `GET /checkout/shipping-methods` \- Get shipping methods
- `POST /checkout/calculate-shipping` \- Calculate shipping

### Public API [​](https://dev.fluentcart.com/api/\#public-api)

- `GET /public/products` \- Get public product catalog
- `GET /public/products/{id}` \- Get public product details
- `GET /public/categories` \- Get product categories

## Error Handling [​](https://dev.fluentcart.com/api/\#error-handling)

The API uses standard HTTP status codes:

- `200` \- Success
- `201` \- Created
- `400` \- Bad Request
- `401` \- Unauthorized
- `403` \- Forbidden
- `404` \- Not Found
- `422` \- Validation Error
- `500` \- Internal Server Error

### Error Response Example [​](https://dev.fluentcart.com/api/\#error-response-example)

json

```
{
    "success": false,
    "error": {
        "code": "validation_error",
        "message": "The given data was invalid.",
        "details": {
            "email": ["The email field is required."],
            "name": ["The name field must be at least 3 characters."]
        }
    }
}
```

## Rate Limiting [​](https://dev.fluentcart.com/api/\#rate-limiting)

API requests are subject to rate limiting to prevent abuse:

- **Authenticated requests**: 1000 requests per hour
- **Unauthenticated requests**: 100 requests per hour
- **Bulk operations**: 10 requests per hour

Rate limit headers are included in responses:

```
X-RateLimit-Limit: 1000
X-RateLimit-Remaining: 999
X-RateLimit-Reset: 1640995200
```

## Webhooks [​](https://dev.fluentcart.com/api/\#webhooks)

FluentCart supports webhooks for real-time notifications:

- `POST /webhook/feed` \- Create webhook
- `GET /webhook/feed` \- List webhooks
- `GET /webhook/feed/{id}` \- Get webhook details
- `PUT /webhook/feed/{id}` \- Update webhook
- `DELETE /webhook/feed/{id}` \- Delete webhook

### Webhook Events [​](https://dev.fluentcart.com/api/\#webhook-events)

- `order.created` \- Order created
- `order.updated` \- Order updated
- `order.paid` \- Order paid
- `subscription.created` \- Subscription created
- `subscription.cancelled` \- Subscription cancelled
- `payment.success` \- Payment successful
- `payment.failed` \- Payment failed

## SDK and Libraries [​](https://dev.fluentcart.com/api/\#sdk-and-libraries)

### JavaScript SDK [​](https://dev.fluentcart.com/api/\#javascript-sdk)

javascript

```
import FluentCartAPI from 'fluent-cart-sdk';

const api = new FluentCartAPI({
    baseURL: 'https://yoursite.com/wp-json/fluent-cart/v1',
    apiKey: 'your-api-key'
});

// Get orders
const orders = await api.orders.list();

// Create order
const order = await api.orders.create({
    customer_id: 123,
    items: [\
        { product_id: 456, quantity: 2 }\
    ]
});
```

### PHP SDK [​](https://dev.fluentcart.com/api/\#php-sdk)

php

```
use FluentCart\API\Client;

$client = new Client([\
    'base_url' => 'https://yoursite.com/wp-json/fluent-cart/v1',\
    'api_key' => 'your-api-key'\
]);

// Get orders
$orders = $client->orders()->list();

// Create order
$order = $client->orders()->create([\
    'customer_id' => 123,\
    'items' => [\
        ['product_id' => 456, 'quantity' => 2]\
    ]\
]);
```

## Testing [​](https://dev.fluentcart.com/api/\#testing)

### Postman Collection [​](https://dev.fluentcart.com/api/\#postman-collection)

Download the FluentCart API Postman collection for easy testing: [Download Postman Collection](https://github.com/fluentcart/api-postman-collection)

### API Testing Tools [​](https://dev.fluentcart.com/api/\#api-testing-tools)

- **Postman** \- GUI-based API testing
- **Insomnia** \- Alternative API testing tool
- **curl** \- Command-line testing
- **HTTPie** \- User-friendly command-line tool

### Example curl Commands [​](https://dev.fluentcart.com/api/\#example-curl-commands)

bash

```
# Get orders
curl -X GET "https://yoursite.com/wp-json/fluent-cart/v1/orders" \
  -H "Authorization: Basic dXNlcm5hbWU6YXBwbGljYXRpb25fcGFzc3dvcmQ="

# Create order
curl -X POST "https://yoursite.com/wp-json/fluent-cart/v1/orders" \
  -H "Authorization: Basic dXNlcm5hbWU6YXBwbGljYXRpb25fcGFzc3dvcmQ=" \
  -H "Content-Type: application/json" \
  -d '{
    "customer_id": 123,
    "items": [\
      {"product_id": 456, "quantity": 2}\
    ]
  }'
```

## Support and Resources [​](https://dev.fluentcart.com/api/\#support-and-resources)

### Community Support [​](https://dev.fluentcart.com/api/\#community-support)

- [GitHub Issues](https://github.com/fluentcart/issues) \- Bug reports and feature requests
- [Developer Community](https://community.fluentcart.com/) \- Community discussions
- [Documentation Issues](https://github.com/fluentcart/docs/issues) \- Documentation improvements

### Professional Support [​](https://dev.fluentcart.com/api/\#professional-support)

- [API Support](https://fluentcart.com/support) \- Priority support for API issues
- [Custom Development](https://fluentcart.com/services) \- Custom API integrations
- [Training](https://fluentcart.com/training) \- API development training

## Related Documentation [​](https://dev.fluentcart.com/api/\#related-documentation)

- [Database Models](https://dev.fluentcart.com/database/models.html) \- Data models used by API endpoints
- [Developer Hooks](https://dev.fluentcart.com/hooks/) \- Hooks triggered by API operations
- [Module System](https://dev.fluentcart.com/modules/) \- Modules that extend API functionality
- [Frontend Development](https://dev.fluentcart.com/guides/frontend.html) \- Frontend API integration
- [Integration Guide](https://dev.fluentcart.com/guides/integrations.html) \- Third-party API integrations

## Next Steps [​](https://dev.fluentcart.com/api/\#next-steps)

Continue with API development:

1. **[Authentication Guide](https://dev.fluentcart.com/api/authentication.html)** \- Learn about API authentication
2. **[Orders API](https://dev.fluentcart.com/api/orders.html)** \- Start with order management endpoints
3. **[Customers API](https://dev.fluentcart.com/api/customers.html)** \- Customer management endpoints
4. **[Products API](https://dev.fluentcart.com/api/products.html)** \- Product catalog endpoints

## Previous/Next Navigation [​](https://dev.fluentcart.com/api/\#previous-next-navigation)

- **Previous**: [Developer Hooks](https://dev.fluentcart.com/hooks/) \- Extending FluentCart functionality
- **Next**: [Module System](https://dev.fluentcart.com/modules/) \- Building custom modules

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

## Authentication | FluentCart Developer Docs

**URL** : https://dev.fluentcart.com/api/authentication

[Skip to content](https://dev.fluentcart.com/api/authentication#VPContent)

# API Authentication [​](https://dev.fluentcart.com/api/authentication\#api-authentication)

FluentCart uses WordPress's built-in authentication system with additional policy-based authorization for fine-grained access control. This guide covers all authentication methods and authorization policies.

## Authentication Methods [​](https://dev.fluentcart.com/api/authentication\#authentication-methods)

### 1\. WordPress Application Passwords [​](https://dev.fluentcart.com/api/authentication\#_1-wordpress-application-passwords)

Application passwords provide secure API access without exposing user credentials.

#### Creating Application Passwords [​](https://dev.fluentcart.com/api/authentication\#creating-application-passwords)

1. **WordPress Admin**: Go to Users → Profile
2. **Application Passwords**: Scroll to "Application Passwords" section
3. **Create New**: Enter application name and click "Add New Application Password"
4. **Copy Password**: Save the generated password securely

#### Using Application Passwords [​](https://dev.fluentcart.com/api/authentication\#using-application-passwords)

bash

```
curl -X GET "https://yoursite.com/wp-json/fluent-cart/v2/orders" \
  -H "Authorization: Basic dXNlcm5hbWU6YXBwbGljYXRpb25fcGFzc3dvcmQ="
```

php

```
$headers = [\
    'Authorization' => 'Basic ' . base64_encode('username:application_password'),\
    'Content-Type' => 'application/json'\
];

$response = wp_remote_get('https://yoursite.com/wp-json/fluent-cart/v2/orders', [\
    'headers' => $headers\
]);
```

javascript

```
const response = await fetch('https://yoursite.com/wp-json/fluent-cart/v2/orders', {
    headers: {
        'Authorization': 'Basic ' + btoa('username:application_password'),
        'Content-Type': 'application/json'
    }
});
```

### 2\. Cookie Authentication [​](https://dev.fluentcart.com/api/authentication\#_2-cookie-authentication)

For logged-in WordPress users, cookies can be used for authentication.

#### Using Cookie Authentication [​](https://dev.fluentcart.com/api/authentication\#using-cookie-authentication)

bash

```
curl -X GET "https://yoursite.com/wp-json/fluent-cart/v2/orders" \
  -H "Cookie: wordpress_logged_in_abc123=user_hash"
```

javascript

```
// In browser environment with logged-in user
const response = await fetch('https://yoursite.com/wp-json/fluent-cart/v2/orders', {
    credentials: 'include'
});
```

### 3\. OAuth (Third-party Integrations) [​](https://dev.fluentcart.com/api/authentication\#_3-oauth-third-party-integrations)

For third-party applications, OAuth can be implemented using WordPress OAuth plugins.

#### OAuth Flow [​](https://dev.fluentcart.com/api/authentication\#oauth-flow)

1. **Authorization Request**: Redirect user to authorization endpoint
2. **User Consent**: User grants permission to your application
3. **Authorization Code**: Receive authorization code
4. **Access Token**: Exchange code for access token
5. **API Requests**: Use access token for API calls

bash

```
curl -X GET "https://yoursite.com/wp-json/fluent-cart/v2/orders" \
  -H "Authorization: Bearer oauth_access_token"
```

## Authorization Policies [​](https://dev.fluentcart.com/api/authentication\#authorization-policies)

FluentCart implements a policy-based authorization system for fine-grained access control.

### Policy System Overview [​](https://dev.fluentcart.com/api/authentication\#policy-system-overview)

Policies are classes that determine whether a user can perform specific actions. Each API endpoint is protected by one or more policies.

### Core Policies [​](https://dev.fluentcart.com/api/authentication\#core-policies)

#### 1\. AdminPolicy [​](https://dev.fluentcart.com/api/authentication\#_1-adminpolicy)

**Purpose**: Super admin access to all FluentCart functionality

**Usage**: System administration, global settings, module management

php

```
// Policy check example
if ($user->can('super_admin')) {
    // Allow access to admin functions
}
```

**Endpoints Protected**:

- Dashboard settings
- Module management
- Global configuration
- System administration

#### 2\. OrderPolicy [​](https://dev.fluentcart.com/api/authentication\#_2-orderpolicy)

**Purpose**: Order management permissions

**Usage**: Order creation, updates, refunds, status changes

**Permissions**:

- `orders/view` \- View orders
- `orders/create` \- Create orders
- `orders/manage` \- Update orders
- `orders/delete` \- Delete orders
- `orders/manage_statuses` \- Change order statuses
- `orders/can_refund` \- Process refunds

**Endpoints Protected**:

- `GET /orders` \- List orders
- `POST /orders` \- Create order
- `PUT /orders/{id}` \- Update order
- `DELETE /orders/{id}` \- Delete order
- `POST /orders/{id}/refund` \- Refund order

#### 3\. CustomerPolicy [​](https://dev.fluentcart.com/api/authentication\#_3-customerpolicy)

**Purpose**: Customer management permissions

**Usage**: Customer data access, address management, user attachment

**Permissions**:

- `customers/view` \- View customers
- `customers/manage` \- Update customers
- `customers/delete` \- Delete customers

**Endpoints Protected**:

- `GET /customers` \- List customers
- `POST /customers` \- Create customer
- `PUT /customers/{id}` \- Update customer
- `GET /customers/{id}/address` \- Get addresses

#### 4\. ProductPolicy [​](https://dev.fluentcart.com/api/authentication\#_4-productpolicy)

**Purpose**: Product management permissions

**Usage**: Product catalog, variations, attributes, pricing

**Permissions**:

- `products/view` \- View products
- `products/create` \- Create products
- `products/edit` \- Update products
- `products/delete` \- Delete products
- `products/manage` \- Full product management

**Endpoints Protected**:

- `GET /products` \- List products
- `POST /products` \- Create product
- `PUT /products/{id}` \- Update product
- `DELETE /products/{id}` \- Delete product

#### 5\. CouponPolicy [​](https://dev.fluentcart.com/api/authentication\#_5-couponpolicy)

**Purpose**: Coupon management permissions

**Usage**: Discount codes, promotional offers

**Permissions**:

- `coupons/view` \- View coupons
- `coupons/manage` \- Create/update coupons
- `coupons/delete` \- Delete coupons

**Endpoints Protected**:

- `GET /coupons` \- List coupons
- `POST /coupons` \- Create coupon
- `PUT /coupons/{id}` \- Update coupon

#### 6\. StoreSettingsPolicy [​](https://dev.fluentcart.com/api/authentication\#_6-storesettingspolicy)

**Purpose**: Store configuration permissions

**Usage**: Store settings, payment methods, storage drivers

**Permissions**:

- `store/settings` \- Manage store settings
- `is_super_admin` \- Super admin access

**Endpoints Protected**:

- `GET /settings/store` \- Get store settings
- `POST /settings/store` \- Update store settings
- `GET /settings/payment-methods` \- Payment method settings

#### 7\. PublicPolicy [​](https://dev.fluentcart.com/api/authentication\#_7-publicpolicy)

**Purpose**: Public access permissions

**Usage**: Public product catalog, cart operations, checkout

**Endpoints Protected**:

- `GET /public/products` \- Public product catalog
- `GET /cart/add_item` \- Add to cart
- `POST /checkout/place-order` \- Place order

#### 8\. CustomerFrontendPolicy [​](https://dev.fluentcart.com/api/authentication\#_8-customerfrontendpolicy)

**Purpose**: Customer frontend access

**Usage**: Customer profile, orders, subscriptions

**Endpoints Protected**:

- `GET /customer-profile/` \- Customer profile
- `GET /customer-profile/orders` \- Customer orders
- `GET /customer-profile/subscriptions` \- Customer subscriptions

### Permission System [​](https://dev.fluentcart.com/api/authentication\#permission-system)

#### Permission Structure [​](https://dev.fluentcart.com/api/authentication\#permission-structure)

Permissions follow a hierarchical structure:

```
{resource}/{action}
```

**Examples**:

- `orders/view` \- View orders
- `orders/create` \- Create orders
- `orders/manage` \- Manage orders
- `products/edit` \- Edit products
- `customers/delete` \- Delete customers

#### Special Permissions [​](https://dev.fluentcart.com/api/authentication\#special-permissions)

- `super_admin` \- Full system access
- `is_super_admin` \- Super admin check
- `is_supper_admin` \- Alternative super admin check (typo in codebase)

### Policy Implementation [​](https://dev.fluentcart.com/api/authentication\#policy-implementation)

#### Policy Class Structure [​](https://dev.fluentcart.com/api/authentication\#policy-class-structure)

php

```
<?php

namespace FluentCart\App\Http\Policies;

use FluentCart\Framework\Http\Policy;

class OrderPolicy extends Policy
{
    public function canView($user)
    {
        return $user->hasPermission('orders/view');
    }

    public function canCreate($user)
    {
        return $user->hasPermission('orders/create');
    }

    public function canManage($user)
    {
        return $user->hasPermission('orders/manage');
    }
}
```

#### Route Protection [​](https://dev.fluentcart.com/api/authentication\#route-protection)

php

```
// Single policy
$router->get('/orders', [OrderController::class, 'index'])
    ->withPolicy('OrderPolicy');

// Multiple policies
$router->get('/orders', [OrderController::class, 'index'])
    ->withPolicy(['OrderPolicy', 'AdminPolicy']);

// Policy with specific permissions
$router->get('/orders', [OrderController::class, 'index'])
    ->withPolicy('OrderPolicy')
    ->meta(['permissions' => 'orders/view']);
```

## Frontend Authentication [​](https://dev.fluentcart.com/api/authentication\#frontend-authentication)

### User Login [​](https://dev.fluentcart.com/api/authentication\#user-login)

**POST**`/user/login`

Authenticate a user for frontend access.

#### Request Body [​](https://dev.fluentcart.com/api/authentication\#request-body)

json

```
{
  "username": "user@example.com",
  "password": "user_password"
}
```

#### Response [​](https://dev.fluentcart.com/api/authentication\#response)

json

```
{
  "success": true,
  "data": {
    "user": {
      "id": 1,
      "email": "user@example.com",
      "display_name": "John Doe"
    },
    "auth_cookie": "wordpress_logged_in_abc123"
  }
}
```

#### Example Request [​](https://dev.fluentcart.com/api/authentication\#example-request)

bash

```
curl -X POST "https://yoursite.com/wp-json/fluent-cart/v2/user/login" \
  -H "Content-Type: application/json" \
  -d '{
    "username": "user@example.com",
    "password": "user_password"
  }'
```

## Error Handling [​](https://dev.fluentcart.com/api/authentication\#error-handling)

### Authentication Errors [​](https://dev.fluentcart.com/api/authentication\#authentication-errors)

| Code | Description |
| --- | --- |
| `authentication_required` | No authentication provided |
| `authentication_failed` | Invalid credentials |
| `authentication_expired` | Token/session expired |
| `insufficient_permissions` | User lacks required permissions |
| `policy_violation` | Policy check failed |

### Error Response Examples [​](https://dev.fluentcart.com/api/authentication\#error-response-examples)

#### Authentication Required [​](https://dev.fluentcart.com/api/authentication\#authentication-required)

json

```
{
  "success": false,
  "error": {
    "code": "authentication_required",
    "message": "Authentication is required to access this endpoint"
  }
}
```

#### Insufficient Permissions [​](https://dev.fluentcart.com/api/authentication\#insufficient-permissions)

json

```
{
  "success": false,
  "error": {
    "code": "insufficient_permissions",
    "message": "You do not have permission to perform this action"
  }
}
```

## Security Best Practices [​](https://dev.fluentcart.com/api/authentication\#security-best-practices)

### 1\. Use Application Passwords [​](https://dev.fluentcart.com/api/authentication\#_1-use-application-passwords)

- **Never** use WordPress admin passwords in API calls
- Create dedicated application passwords for each integration
- Rotate application passwords regularly

### 2\. HTTPS Only [​](https://dev.fluentcart.com/api/authentication\#_2-https-only)

- Always use HTTPS for API calls
- Never send credentials over unencrypted connections

### 3\. Permission Principle [​](https://dev.fluentcart.com/api/authentication\#_3-permission-principle)

- Grant minimum required permissions
- Use specific permissions rather than broad access
- Regularly audit user permissions

### 4\. Rate Limiting [​](https://dev.fluentcart.com/api/authentication\#_4-rate-limiting)

- Implement rate limiting on your API calls
- Respect FluentCart's rate limits
- Use exponential backoff for retries

### 5\. Error Handling [​](https://dev.fluentcart.com/api/authentication\#_5-error-handling)

- Handle authentication errors gracefully
- Don't expose sensitive information in error messages
- Log authentication failures for monitoring

## Testing Authentication [​](https://dev.fluentcart.com/api/authentication\#testing-authentication)

### Test Credentials [​](https://dev.fluentcart.com/api/authentication\#test-credentials)

bash

```
# Test with valid credentials
curl -X GET "https://yoursite.com/wp-json/fluent-cart/v2/orders" \
  -H "Authorization: Basic dXNlcm5hbWU6YXBwbGljYXRpb25fcGFzc3dvcmQ="

# Test with invalid credentials
curl -X GET "https://yoursite.com/wp-json/fluent-cart/v2/orders" \
  -H "Authorization: Basic aW52YWxpZDppbnZhbGlk"
```

### Permission Testing [​](https://dev.fluentcart.com/api/authentication\#permission-testing)

bash

```
# Test with insufficient permissions
curl -X DELETE "https://yoursite.com/wp-json/fluent-cart/v2/orders/1" \
  -H "Authorization: Basic dXNlcm5hbWU6YXBwbGljYXRpb25fcGFzc3dvcmQ="
```

## Related Documentation [​](https://dev.fluentcart.com/api/authentication\#related-documentation)

- [Orders API](https://dev.fluentcart.com/api/orders.html) \- Order management endpoints
- [Customers API](https://dev.fluentcart.com/api/customers.html) \- Customer management endpoints
- [Products API](https://dev.fluentcart.com/api/products.html) \- Product management endpoints
- [Subscriptions API](https://dev.fluentcart.com/api/subscriptions.html) \- Subscription management endpoints
- [Database Models](https://dev.fluentcart.com/database/models.html) \- User and permission data models

## Next Steps [​](https://dev.fluentcart.com/api/authentication\#next-steps)

Continue with API development:

1. **[Orders API](https://dev.fluentcart.com/api/orders.html)** \- Start with order management
2. **[Customers API](https://dev.fluentcart.com/api/customers.html)** \- Customer management
3. **[Products API](https://dev.fluentcart.com/api/products.html)** \- Product catalog
4. **[Subscriptions API](https://dev.fluentcart.com/api/subscriptions.html)** \- Subscription management

## Previous/Next Navigation [​](https://dev.fluentcart.com/api/authentication\#previous-next-navigation)

- **Previous**: [Subscriptions API](https://dev.fluentcart.com/api/subscriptions.html) \- Subscription management endpoints
- **Next**: [Orders API](https://dev.fluentcart.com/api/orders.html) \- Order management endpoints

* * *

Today

Hi! I’m your AI assistant. How can I assist you today?

Just now

Powered by **FluentBot**


---

---

## Customers API | FluentCart Developer Docs

**URL** : https://dev.fluentcart.com/api/customers

[Skip to content](https://dev.fluentcart.com/api/customers#VPContent)

# Customers API [​](https://dev.fluentcart.com/api/customers\#customers-api)

The Customers API provides comprehensive endpoints for managing customers in FluentCart. This includes creating, reading, updating, and deleting customers, as well as managing customer addresses, orders, and user attachments.

## Base URL [​](https://dev.fluentcart.com/api/customers\#base-url)

```
https://yoursite.com/wp-json/fluent-cart/v2/customers
```

## Authentication [​](https://dev.fluentcart.com/api/customers\#authentication)

All endpoints require authentication and appropriate permissions:

- **Authentication**: WordPress Application Password or Cookie
- **Policy**: `CustomerPolicy`
- **Permissions**: Various customer-related permissions

## Endpoints [​](https://dev.fluentcart.com/api/customers\#endpoints)

### List Customers [​](https://dev.fluentcart.com/api/customers\#list-customers)

**GET**`/customers`

Retrieve a paginated list of customers with optional filtering and searching.

#### Parameters [​](https://dev.fluentcart.com/api/customers\#parameters)

| Parameter | Type | Description | Default |
| --- | --- | --- | --- |
| `page` | integer | Page number | 1 |
| `per_page` | integer | Items per page (max 100) | 10 |
| `search` | string | Search query | - |
| `filters` | object | Filter options | - |
| `order_by` | string | Sort field | id |
| `order_type` | string | Sort direction (ASC/DESC) | DESC |

#### Filter Options [​](https://dev.fluentcart.com/api/customers\#filter-options)

json

```
{
  "status": "active",
  "date_from": "2024-01-01",
  "date_to": "2024-12-31",
  "total_spent_min": 1000,
  "total_spent_max": 5000
}
```

#### Response [​](https://dev.fluentcart.com/api/customers\#response)

json

```
{
  "success": true,
  "data": {
    "customers": [\
      {\
        "id": 1,\
        "email": "customer@example.com",\
        "first_name": "John",\
        "last_name": "Doe",\
        "status": "active",\
        "total_spent": 5000,\
        "order_count": 3,\
        "created_at": "2024-01-01T10:00:00Z",\
        "updated_at": "2024-01-15T14:30:00Z"\
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

#### Example Request [​](https://dev.fluentcart.com/api/customers\#example-request)

bash

```
curl -X GET "https://yoursite.com/wp-json/fluent-cart/v1/customers?page=1&per_page=20&search=john" \
  -H "Authorization: Basic dXNlcm5hbWU6YXBwbGljYXRpb25fcGFzc3dvcmQ="
```

### Create Customer [​](https://dev.fluentcart.com/api/customers\#create-customer)

**POST**`/customers`

Create a new customer.

#### Request Body [​](https://dev.fluentcart.com/api/customers\#request-body)

json

```
{
  "email": "newcustomer@example.com",
  "first_name": "Jane",
  "last_name": "Smith",
  "phone": "+1234567890",
  "status": "active",
  "additional_info": {
    "company": "Example Corp",
    "notes": "VIP customer"
  }
}
```

#### Response [​](https://dev.fluentcart.com/api/customers\#response-1)

json

```
{
  "success": true,
  "data": {
    "customer": {
      "id": 1,
      "email": "newcustomer@example.com",
      "first_name": "Jane",
      "last_name": "Smith",
      "phone": "+1234567890",
      "status": "active",
      "created_at": "2024-01-01T10:00:00Z"
    }
  }
}
```

#### Example Request [​](https://dev.fluentcart.com/api/customers\#example-request-1)

bash

```
curl -X POST "https://yoursite.com/wp-json/fluent-cart/v1/customers" \
  -H "Authorization: Basic dXNlcm5hbWU6YXBwbGljYXRpb25fcGFzc3dvcmQ=" \
  -H "Content-Type: application/json" \
  -d '{
    "email": "newcustomer@example.com",
    "first_name": "Jane",
    "last_name": "Smith"
  }'
```

### Get Customer Details [​](https://dev.fluentcart.com/api/customers\#get-customer-details)

**GET**`/customers/{customerId}`

Retrieve detailed information about a specific customer.

#### Parameters [​](https://dev.fluentcart.com/api/customers\#parameters-1)

| Parameter | Type | Description |
| --- | --- | --- |
| `customerId` | integer | Customer ID |

#### Response [​](https://dev.fluentcart.com/api/customers\#response-2)

json

```
{
  "success": true,
  "data": {
    "customer": {
      "id": 1,
      "email": "customer@example.com",
      "first_name": "John",
      "last_name": "Doe",
      "phone": "+1234567890",
      "status": "active",
      "total_spent": 5000,
      "order_count": 3,
      "created_at": "2024-01-01T10:00:00Z",
      "updated_at": "2024-01-15T14:30:00Z",
      "addresses": [\
        {\
          "id": 1,\
          "type": "billing",\
          "first_name": "John",\
          "last_name": "Doe",\
          "address_1": "123 Main St",\
          "city": "New York",\
          "state": "NY",\
          "postcode": "10001",\
          "country": "US",\
          "is_primary": true\
        }\
      ]
    }
  }
}
```

#### Example Request [​](https://dev.fluentcart.com/api/customers\#example-request-2)

bash

```
curl -X GET "https://yoursite.com/wp-json/fluent-cart/v1/customers/1" \
  -H "Authorization: Basic dXNlcm5hbWU6YXBwbGljYXRpb25fcGFzc3dvcmQ="
```

### Update Customer [​](https://dev.fluentcart.com/api/customers\#update-customer)

**PUT**`/customers/{customerId}`

Update an existing customer's information.

#### Parameters [​](https://dev.fluentcart.com/api/customers\#parameters-2)

| Parameter | Type | Description |
| --- | --- | --- |
| `customerId` | integer | Customer ID |

#### Request Body [​](https://dev.fluentcart.com/api/customers\#request-body-1)

json

```
{
  "first_name": "John",
  "last_name": "Doe",
  "phone": "+1234567890",
  "status": "active"
}
```

#### Response [​](https://dev.fluentcart.com/api/customers\#response-3)

json

```
{
  "success": true,
  "data": {
    "customer": {
      "id": 1,
      "first_name": "John",
      "last_name": "Doe",
      "phone": "+1234567890",
      "status": "active",
      "updated_at": "2024-01-01T11:00:00Z"
    }
  }
}
```

#### Example Request [​](https://dev.fluentcart.com/api/customers\#example-request-3)

bash

```
curl -X PUT "https://yoursite.com/wp-json/fluent-cart/v1/customers/1" \
  -H "Authorization: Basic dXNlcm5hbWU6YXBwbGljYXRpb25fcGFzc3dvcmQ=" \
  -H "Content-Type: application/json" \
  -d '{
    "first_name": "John",
    "last_name": "Doe",
    "phone": "+1234567890"
  }'
```

### Update Customer Additional Info [​](https://dev.fluentcart.com/api/customers\#update-customer-additional-info)

**PUT**`/customers/{customerId}/additional-info`

Update customer's additional information.

#### Parameters [​](https://dev.fluentcart.com/api/customers\#parameters-3)

| Parameter | Type | Description |
| --- | --- | --- |
| `customerId` | integer | Customer ID |

#### Request Body [​](https://dev.fluentcart.com/api/customers\#request-body-2)

json

```
{
  "company": "Updated Corp",
  "notes": "Updated VIP customer",
  "custom_field_1": "Custom value"
}
```

#### Response [​](https://dev.fluentcart.com/api/customers\#response-4)

json

```
{
  "success": true,
  "data": {
    "customer": {
      "id": 1,
      "additional_info": {
        "company": "Updated Corp",
        "notes": "Updated VIP customer",
        "custom_field_1": "Custom value"
      },
      "updated_at": "2024-01-01T11:00:00Z"
    }
  }
}
```

#### Example Request [​](https://dev.fluentcart.com/api/customers\#example-request-4)

bash

```
curl -X PUT "https://yoursite.com/wp-json/fluent-cart/v1/customers/1/additional-info" \
  -H "Authorization: Basic dXNlcm5hbWU6YXBwbGljYXRpb25fcGFzc3dvcmQ=" \
  -H "Content-Type: application/json" \
  -d '{
    "company": "Updated Corp",
    "notes": "Updated VIP customer"
  }'
```

### Get Customer Stats [​](https://dev.fluentcart.com/api/customers\#get-customer-stats)

**GET**`/customers/get-stats/{customer}`

Get statistics for a specific customer.

#### Parameters [​](https://dev.fluentcart.com/api/customers\#parameters-4)

| Parameter | Type | Description |
| --- | --- | --- |
| `customer` | integer | Customer ID |

#### Response [​](https://dev.fluentcart.com/api/customers\#response-5)

json

```
{
  "success": true,
  "data": {
    "stats": {
      "total_spent": 5000,
      "order_count": 3,
      "average_order_value": 1667,
      "last_order_date": "2024-01-15T14:30:00Z",
      "first_order_date": "2024-01-01T10:00:00Z"
    }
  }
}
```

#### Example Request [​](https://dev.fluentcart.com/api/customers\#example-request-5)

bash

```
curl -X GET "https://yoursite.com/wp-json/fluent-cart/v1/customers/get-stats/1" \
  -H "Authorization: Basic dXNlcm5hbWU6YXBwbGljYXRpb25fcGFzc3dvcmQ="
```

### Get Customer Orders [​](https://dev.fluentcart.com/api/customers\#get-customer-orders)

**GET**`/customers/{customerId}/orders`

Get all orders for a specific customer.

#### Parameters [​](https://dev.fluentcart.com/api/customers\#parameters-5)

| Parameter | Type | Description |
| --- | --- | --- |
| `customerId` | integer | Customer ID |

#### Response [​](https://dev.fluentcart.com/api/customers\#response-6)

json

```
{
  "success": true,
  "data": {
    "orders": [\
      {\
        "id": 1,\
        "status": "completed",\
        "payment_status": "paid",\
        "total_amount": 2500,\
        "currency": "USD",\
        "created_at": "2024-01-01T10:00:00Z"\
      },\
      {\
        "id": 2,\
        "status": "processing",\
        "payment_status": "paid",\
        "total_amount": 2500,\
        "currency": "USD",\
        "created_at": "2024-01-15T14:30:00Z"\
      }\
    ]
  }
}
```

#### Example Request [​](https://dev.fluentcart.com/api/customers\#example-request-6)

bash

```
curl -X GET "https://yoursite.com/wp-json/fluent-cart/v1/customers/1/orders" \
  -H "Authorization: Basic dXNlcm5hbWU6YXBwbGljYXRpb25fcGFzc3dvcmQ="
```

### Get Customer Addresses [​](https://dev.fluentcart.com/api/customers\#get-customer-addresses)

**GET**`/customers/{customerId}/address`

Get all addresses for a specific customer.

#### Parameters [​](https://dev.fluentcart.com/api/customers\#parameters-6)

| Parameter | Type | Description |
| --- | --- | --- |
| `customerId` | integer | Customer ID |

#### Response [​](https://dev.fluentcart.com/api/customers\#response-7)

json

```
{
  "success": true,
  "data": {
    "addresses": [\
      {\
        "id": 1,\
        "type": "billing",\
        "first_name": "John",\
        "last_name": "Doe",\
        "address_1": "123 Main St",\
        "city": "New York",\
        "state": "NY",\
        "postcode": "10001",\
        "country": "US",\
        "is_primary": true\
      },\
      {\
        "id": 2,\
        "type": "shipping",\
        "first_name": "John",\
        "last_name": "Doe",\
        "address_1": "456 Oak Ave",\
        "city": "Brooklyn",\
        "state": "NY",\
        "postcode": "11201",\
        "country": "US",\
        "is_primary": false\
      }\
    ]
  }
}
```

#### Example Request [​](https://dev.fluentcart.com/api/customers\#example-request-7)

bash

```
curl -X GET "https://yoursite.com/wp-json/fluent-cart/v1/customers/1/address" \
  -H "Authorization: Basic dXNlcm5hbWU6YXBwbGljYXRpb25fcGFzc3dvcmQ="
```

### Update Customer Address [​](https://dev.fluentcart.com/api/customers\#update-customer-address)

**PUT**`/customers/{customerId}/address`

Update customer's address information.

#### Parameters [​](https://dev.fluentcart.com/api/customers\#parameters-7)

| Parameter | Type | Description |
| --- | --- | --- |
| `customerId` | integer | Customer ID |

#### Request Body [​](https://dev.fluentcart.com/api/customers\#request-body-3)

json

```
{
  "address_id": 1,
  "first_name": "John",
  "last_name": "Doe",
  "address_1": "123 Updated St",
  "city": "New York",
  "state": "NY",
  "postcode": "10001",
  "country": "US"
}
```

#### Response [​](https://dev.fluentcart.com/api/customers\#response-8)

json

```
{
  "success": true,
  "data": {
    "address": {
      "id": 1,
      "first_name": "John",
      "last_name": "Doe",
      "address_1": "123 Updated St",
      "city": "New York",
      "state": "NY",
      "postcode": "10001",
      "country": "US",
      "updated_at": "2024-01-01T11:00:00Z"
    }
  }
}
```

#### Example Request [​](https://dev.fluentcart.com/api/customers\#example-request-8)

bash

```
curl -X PUT "https://yoursite.com/wp-json/fluent-cart/v1/customers/1/address" \
  -H "Authorization: Basic dXNlcm5hbWU6YXBwbGljYXRpb25fcGFzc3dvcmQ=" \
  -H "Content-Type: application/json" \
  -d '{
    "address_id": 1,
    "address_1": "123 Updated St",
    "city": "New York"
  }'
```

### Create Customer Address [​](https://dev.fluentcart.com/api/customers\#create-customer-address)

**POST**`/customers/{customerId}/address`

Create a new address for a customer.

#### Parameters [​](https://dev.fluentcart.com/api/customers\#parameters-8)

| Parameter | Type | Description |
| --- | --- | --- |
| `customerId` | integer | Customer ID |

#### Request Body [​](https://dev.fluentcart.com/api/customers\#request-body-4)

json

```
{
  "type": "shipping",
  "first_name": "John",
  "last_name": "Doe",
  "address_1": "789 New St",
  "city": "Queens",
  "state": "NY",
  "postcode": "11301",
  "country": "US"
}
```

#### Response [​](https://dev.fluentcart.com/api/customers\#response-9)

json

```
{
  "success": true,
  "data": {
    "address": {
      "id": 3,
      "type": "shipping",
      "first_name": "John",
      "last_name": "Doe",
      "address_1": "789 New St",
      "city": "Queens",
      "state": "NY",
      "postcode": "11301",
      "country": "US",
      "created_at": "2024-01-01T11:00:00Z"
    }
  }
}
```

#### Example Request [​](https://dev.fluentcart.com/api/customers\#example-request-9)

bash

```
curl -X POST "https://yoursite.com/wp-json/fluent-cart/v1/customers/1/address" \
  -H "Authorization: Basic dXNlcm5hbWU6YXBwbGljYXRpb25fcGFzc3dvcmQ=" \
  -H "Content-Type: application/json" \
  -d '{
    "type": "shipping",
    "first_name": "John",
    "last_name": "Doe",
    "address_1": "789 New St",
    "city": "Queens",
    "state": "NY",
    "postcode": "11301",
    "country": "US"
  }'
```

### Delete Customer Address [​](https://dev.fluentcart.com/api/customers\#delete-customer-address)

**DELETE**`/customers/{customerId}/address`

Delete a customer's address.

#### Parameters [​](https://dev.fluentcart.com/api/customers\#parameters-9)

| Parameter | Type | Description |
| --- | --- | --- |
| `customerId` | integer | Customer ID |

#### Request Body [​](https://dev.fluentcart.com/api/customers\#request-body-5)

json

```
{
  "address_id": 2
}
```

#### Response [​](https://dev.fluentcart.com/api/customers\#response-10)

json

```
{
  "success": true,
  "message": "Address deleted successfully"
}
```

#### Example Request [​](https://dev.fluentcart.com/api/customers\#example-request-10)

bash

```
curl -X DELETE "https://yoursite.com/wp-json/fluent-cart/v1/customers/1/address" \
  -H "Authorization: Basic dXNlcm5hbWU6YXBwbGljYXRpb25fcGFzc3dvcmQ=" \
  -H "Content-Type: application/json" \
  -d '{
    "address_id": 2
  }'
```

### Set Primary Address [​](https://dev.fluentcart.com/api/customers\#set-primary-address)

**POST**`/customers/{customerId}/address/make-primary`

Set an address as the primary address for a customer.

#### Parameters [​](https://dev.fluentcart.com/api/customers\#parameters-10)

| Parameter | Type | Description |
| --- | --- | --- |
| `customerId` | integer | Customer ID |

#### Request Body [​](https://dev.fluentcart.com/api/customers\#request-body-6)

json

```
{
  "address_id": 2
}
```

#### Response [​](https://dev.fluentcart.com/api/customers\#response-11)

json

```
{
  "success": true,
  "data": {
    "address": {
      "id": 2,
      "is_primary": true,
      "updated_at": "2024-01-01T11:00:00Z"
    }
  }
}
```

#### Example Request [​](https://dev.fluentcart.com/api/customers\#example-request-11)

bash

```
curl -X POST "https://yoursite.com/wp-json/fluent-cart/v1/customers/1/address/make-primary" \
  -H "Authorization: Basic dXNlcm5hbWU6YXBwbGljYXRpb25fcGFzc3dvcmQ=" \
  -H "Content-Type: application/json" \
  -d '{
    "address_id": 2
  }'
```

### Get Attachable Users [​](https://dev.fluentcart.com/api/customers\#get-attachable-users)

**GET**`/customers/attachable-user`

Get WordPress users that can be attached to customers.

#### Response [​](https://dev.fluentcart.com/api/customers\#response-12)

json

```
{
  "success": true,
  "data": {
    "users": [\
      {\
        "id": 1,\
        "display_name": "John Doe",\
        "user_email": "john@example.com",\
        "user_login": "johndoe"\
      },\
      {\
        "id": 2,\
        "display_name": "Jane Smith",\
        "user_email": "jane@example.com",\
        "user_login": "janesmith"\
      }\
    ]
  }
}
```

#### Example Request [​](https://dev.fluentcart.com/api/customers\#example-request-12)

bash

```
curl -X GET "https://yoursite.com/wp-json/fluent-cart/v1/customers/attachable-user" \
  -H "Authorization: Basic dXNlcm5hbWU6YXBwbGljYXRpb25fcGFzc3dvcmQ="
```

### Attach User to Customer [​](https://dev.fluentcart.com/api/customers\#attach-user-to-customer)

**POST**`/customers/{customerId}/attachable-user`

Attach a WordPress user to a customer.

#### Parameters [​](https://dev.fluentcart.com/api/customers\#parameters-11)

| Parameter | Type | Description |
| --- | --- | --- |
| `customerId` | integer | Customer ID |

#### Request Body [​](https://dev.fluentcart.com/api/customers\#request-body-7)

json

```
{
  "user_id": 1
}
```

#### Response [​](https://dev.fluentcart.com/api/customers\#response-13)

json

```
{
  "success": true,
  "data": {
    "customer": {
      "id": 1,
      "user_id": 1,
      "updated_at": "2024-01-01T11:00:00Z"
    }
  }
}
```

#### Example Request [​](https://dev.fluentcart.com/api/customers\#example-request-13)

bash

```
curl -X POST "https://yoursite.com/wp-json/fluent-cart/v1/customers/1/attachable-user" \
  -H "Authorization: Basic dXNlcm5hbWU6YXBwbGljYXRpb25fcGFzc3dvcmQ=" \
  -H "Content-Type: application/json" \
  -d '{
    "user_id": 1
  }'
```

### Detach User from Customer [​](https://dev.fluentcart.com/api/customers\#detach-user-from-customer)

**POST**`/customers/{customerId}/detach-user`

Detach a WordPress user from a customer.

#### Parameters [​](https://dev.fluentcart.com/api/customers\#parameters-12)

| Parameter | Type | Description |
| --- | --- | --- |
| `customerId` | integer | Customer ID |

#### Response [​](https://dev.fluentcart.com/api/customers\#response-14)

json

```
{
  "success": true,
  "data": {
    "customer": {
      "id": 1,
      "user_id": null,
      "updated_at": "2024-01-01T11:00:00Z"
    }
  }
}
```

#### Example Request [​](https://dev.fluentcart.com/api/customers\#example-request-14)

bash

```
curl -X POST "https://yoursite.com/wp-json/fluent-cart/v1/customers/1/detach-user" \
  -H "Authorization: Basic dXNlcm5hbWU6YXBwbGljYXRpb25fcGFzc3dvcmQ="
```

### Bulk Actions [​](https://dev.fluentcart.com/api/customers\#bulk-actions)

**POST**`/customers/do-bulk-action`

Perform bulk actions on multiple customers.

#### Request Body [​](https://dev.fluentcart.com/api/customers\#request-body-8)

json

```
{
  "action": "update_status",
  "customer_ids": [1, 2, 3],
  "data": {
    "status": "inactive"
  }
}
```

#### Available Actions [​](https://dev.fluentcart.com/api/customers\#available-actions)

- `update_status` \- Update status of multiple customers
- `delete` \- Delete multiple customers
- `export` \- Export multiple customers

#### Response [​](https://dev.fluentcart.com/api/customers\#response-15)

json

```
{
  "success": true,
  "data": {
    "processed": 3,
    "failed": 0,
    "results": [\
      {\
        "customer_id": 1,\
        "success": true\
      },\
      {\
        "customer_id": 2,\
        "success": true\
      },\
      {\
        "customer_id": 3,\
        "success": true\
      }\
    ]
  }
}
```

#### Example Request [​](https://dev.fluentcart.com/api/customers\#example-request-15)

bash

```
curl -X POST "https://yoursite.com/wp-json/fluent-cart/v1/customers/do-bulk-action" \
  -H "Authorization: Basic dXNlcm5hbWU6YXBwbGljYXRpb25fcGFzc3dvcmQ=" \
  -H "Content-Type: application/json" \
  -d '{
    "action": "update_status",
    "customer_ids": [1, 2, 3],
    "data": {
      "status": "inactive"
    }
  }'
```

## Error Handling [​](https://dev.fluentcart.com/api/customers\#error-handling)

### Common Error Codes [​](https://dev.fluentcart.com/api/customers\#common-error-codes)

| Code | Description |
| --- | --- |
| `customer_not_found` | Customer with specified ID not found |
| `invalid_email` | Email address is invalid or already exists |
| `invalid_user` | WordPress user ID is invalid |
| `insufficient_permissions` | User lacks required permissions |
| `validation_error` | Request data validation failed |
| `address_not_found` | Address with specified ID not found |

### Error Response Example [​](https://dev.fluentcart.com/api/customers\#error-response-example)

json

```
{
  "success": false,
  "error": {
    "code": "customer_not_found",
    "message": "Customer with ID 999 not found"
  }
}
```

## Rate Limiting [​](https://dev.fluentcart.com/api/customers\#rate-limiting)

- **List operations**: 100 requests per hour
- **Create operations**: 50 requests per hour
- **Update operations**: 200 requests per hour
- **Delete operations**: 20 requests per hour

## Related Documentation [​](https://dev.fluentcart.com/api/customers\#related-documentation)

- [Orders API](https://dev.fluentcart.com/api/orders.html) \- Order management endpoints
- [Products API](https://dev.fluentcart.com/api/products.html) \- Product management endpoints
- [Database Models](https://dev.fluentcart.com/database/models.html) \- Customer data models
- [Developer Hooks](https://dev.fluentcart.com/hooks/) \- Customer-related hooks

## Next Steps [​](https://dev.fluentcart.com/api/customers\#next-steps)

Continue with customer management:

1. **[Orders API](https://dev.fluentcart.com/api/orders.html)** \- Manage customer orders
2. **[Products API](https://dev.fluentcart.com/api/products.html)** \- Manage product catalog
3. **[Database Models](https://dev.fluentcart.com/database/models.html)** \- Understand customer data structure
4. **[Developer Hooks](https://dev.fluentcart.com/hooks/)** \- Customer-related hooks

## Previous/Next Navigation [​](https://dev.fluentcart.com/api/customers\#previous-next-navigation)

- **Previous**: [Orders API](https://dev.fluentcart.com/api/orders.html) \- Order management endpoints
- **Next**: [Products API](https://dev.fluentcart.com/api/products.html) \- Product management endpoints

* * *

Today

Hi! I’m your AI assistant. How can I assist you today?

Just now

Powered by **FluentBot**


---

---

