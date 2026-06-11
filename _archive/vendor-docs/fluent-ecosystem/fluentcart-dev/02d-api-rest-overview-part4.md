# FluentCart Developer Docs - REST API Overview (Part 4/4)

Overview de l'API REST FluentCart : authentification, orders, products, customers, subscriptions, licensing, order-bump, roles & permissions.

---

## REST API Overview | FluentCart Developer Docs

**URL** : https://dev.fluentcart.com/restapi/

[Skip to content](https://dev.fluentcart.com/restapi/#VPContent)

# FluentCart REST API [​](https://dev.fluentcart.com/restapi/\#fluentcart-rest-api)

Complete REST API reference for FluentCart and FluentCart Pro. This documentation covers **367+ endpoints** organized by module, with full parameter details, response examples, and authentication guides.

## Getting Started [​](https://dev.fluentcart.com/restapi/\#getting-started)

**Base URL:**`https://your-site.com/wp-json/fluent-cart/v2`

All admin endpoints require authentication. Public and customer portal endpoints have different authentication requirements as noted in each module.

### Authentication [​](https://dev.fluentcart.com/restapi/\#authentication)

**Admin API** - Use WordPress Application Passwords (HTTP Basic Auth):

1. Go to **WordPress Dashboard** → **Users** → **Your Profile**
2. Scroll to **Application Passwords** section
3. Create a new application password
4. Use the credentials with every request:

bash

```
curl -X GET "https://your-site.com/wp-json/fluent-cart/v2/orders" \
  -u "username:application_password"
```

**Customer Portal API** - Uses WordPress cookie-based authentication with nonce verification:

bash

```
curl -X GET "https://your-site.com/wp-json/fluent-cart/v2/customer-profile/" \
  -H "X-WP-Nonce: <nonce>" \
  --cookie "wordpress_logged_in_xxx=..."
```

**Public API** - No authentication required.

### Conventions [​](https://dev.fluentcart.com/restapi/\#conventions)

- All monetary values are in **cents** (e.g., `$10.00` = `1000`). Use integer arithmetic.
- All timestamps are in **UTC/GMT**.
- Pagination uses `page` and `per_page` parameters (default: `per_page=10`).
- Responses use standard HTTP status codes (`200`, `400`, `403`, `404`, `422`).
- The REST namespace is `fluent-cart/v2`.

* * *

## API Modules [​](https://dev.fluentcart.com/restapi/\#api-modules)

### Core Resources [​](https://dev.fluentcart.com/restapi/\#core-resources)

| Module | Endpoints | Description |
| --- | --- | --- |
| [Orders](https://dev.fluentcart.com/restapi/orders.html) | 22 | Order CRUD, payments, refunds, shipping, fulfillment, notes, transactions |
| [Products](https://dev.fluentcart.com/restapi/products.html) | 59 | Product CRUD, variations, attributes, downloadables, pricing, bundles |
| [Customers](https://dev.fluentcart.com/restapi/customers.html) | 18 | Customer CRUD, addresses, WordPress user association, notes |
| [Coupons](https://dev.fluentcart.com/restapi/coupons.html) | 12 | Coupon CRUD, validation, usage tracking |
| [Subscriptions](https://dev.fluentcart.com/restapi/subscriptions.html) | 17 | Subscription lifecycle, billing, cancellations, payment method management |

### Configuration [​](https://dev.fluentcart.com/restapi/\#configuration)

| Module | Endpoints | Description |
| --- | --- | --- |
| [Tax](https://dev.fluentcart.com/restapi/tax.html) | 26 | Tax classes, rates, EU VAT, configuration |
| [Shipping](https://dev.fluentcart.com/restapi/shipping.html) | 15 | Shipping zones, methods, classes |
| [Settings](https://dev.fluentcart.com/restapi/settings.html) | 30 | Store settings, payment methods, modules, storage, permissions, checkout fields |
| [Email Notifications](https://dev.fluentcart.com/restapi/email-notifications.html) | 11 | Email template management, previews, test sending |

### Analytics & Content [​](https://dev.fluentcart.com/restapi/\#analytics-content)

| Module | Endpoints | Description |
| --- | --- | --- |
| [Reports](https://dev.fluentcart.com/restapi/reports.html) | 45 | Revenue, orders, sales, refunds, subscriptions, dashboards, retention |
| [Integrations](https://dev.fluentcart.com/restapi/integrations.html) | 17 | Add-ons, global feeds, product integration feeds |
| [Files](https://dev.fluentcart.com/restapi/files.html) | 5 | File uploads, storage management, editor uploads |
| [Labels & Attributes](https://dev.fluentcart.com/restapi/labels-and-attributes.html) | 13 | Product labels, attribute groups, attribute terms |
| [Dashboard](https://dev.fluentcart.com/restapi/dashboard.html) | 20 | Dashboard stats, onboarding, activity log, print templates, widgets |

### Storefront & Checkout [​](https://dev.fluentcart.com/restapi/\#storefront-checkout)

| Module | Endpoints | Description |
| --- | --- | --- |
| [Public Shop](https://dev.fluentcart.com/restapi/public-shop.html) | 3 | Public product listing, search, server-rendered views |
| [Checkout](https://dev.fluentcart.com/restapi/checkout.html) | 7 | Order placement, payment processing, shipping methods, country info |
| [Customer Profile](https://dev.fluentcart.com/restapi/customer-profile.html) | 21 | Customer portal - orders, downloads, addresses, profile management |

### Pro Features [​](https://dev.fluentcart.com/restapi/\#pro-features)

| Module | Endpoints | Description |
| --- | --- | --- |
| [Licensing](https://dev.fluentcart.com/restapi/licensing.html) | 24 | License management, activations, public license API, WordPress update API |
| [Roles & Permissions](https://dev.fluentcart.com/restapi/roles.html) | 7 | FluentCart role assignment and management |
| [Order Bumps](https://dev.fluentcart.com/restapi/order-bumps.html) | 5 | Order bump CRUD with display conditions |

* * *

## Permission System [​](https://dev.fluentcart.com/restapi/\#permission-system)

FluentCart uses a policy-based authorization system with 32 granular permissions across 4 built-in roles:

| Role | Description |
| --- | --- |
| `super_admin` | Full access to all features |
| `manager` | Manage orders, customers, products, and settings |
| `worker` | Day-to-day operations - orders, customers, products |
| `accountant` | Read-only access to orders, customers, and reports |

Each endpoint documents its required permission (e.g., `orders/view`, `products/edit`, `store/sensitive`).

## Error Handling [​](https://dev.fluentcart.com/restapi/\#error-handling)

All error responses follow a consistent format:

json

```
{
  "message": "Error description",
  "errors": {
    "field_name": ["Validation error message"]
  }
}
```

| Status Code | Meaning |
| --- | --- |
| `200` | Success |
| `400` | Bad Request - validation failed or invalid parameters |
| `403` | Forbidden - insufficient permissions |
| `404` | Not Found - resource does not exist |
| `422` | Unprocessable Entity - business logic error |
| `429` | Too Many Requests - rate limited |

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

