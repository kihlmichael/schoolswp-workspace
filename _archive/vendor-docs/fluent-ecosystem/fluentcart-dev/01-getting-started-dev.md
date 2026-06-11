# FluentCart Developer Docs - Getting Started & Guides

Setup, premiers pas et guides pratiques (frontend, abonnements).

---

## Getting Started | FluentCart Developer Docs

**URL** : https://dev.fluentcart.com/getting-started

[Skip to content](https://dev.fluentcart.com/getting-started#VPContent)

# FluentCart Developer Guide [​](https://dev.fluentcart.com/getting-started\#fluentcart-developer-guide)

FluentCart Core Complete Guide

Welcome to the complete developer guide for **FluentCart** \- the self-hosted e-commerce plugin for WordPress. This comprehensive guide will take you from understanding the basics to building sophisticated integrations and custom functionality.

## What is FluentCart? [​](https://dev.fluentcart.com/getting-started\#what-is-fluentcart)

FluentCart is a **Self-Hosted E-commerce Plugin** for WordPress that helps businesses manage their online stores, process payments, handle orders, and manage customers. Unlike cloud-based solutions, FluentCart runs entirely on your WordPress site, ensuring data privacy, unlimited products, and no monthly fees.

## Why Extend FluentCart? [​](https://dev.fluentcart.com/getting-started\#why-extend-fluentcart)

FluentCart is designed to be highly extensible, allowing developers to customize and extend its functionality far beyond what the plugin offers out-of-the-box. Whether you're a business owner looking to customize your store or a developer hired to create specific integrations, FluentCart provides the tools you need.

### 🔧 **Built for Customization** [​](https://dev.fluentcart.com/getting-started\#%F0%9F%94%A7-built-for-customization)

- **Extensive hook system** \- 315+ action and filter hooks for custom functionality
- **Modular architecture** \- Clean separation allows safe modifications and additions
- **RESTful API** \- Complete programmatic access to all e-commerce data and functions
- **WordPress-native** \- Follows WordPress coding standards and best practices

### 🏗️ **Flexible Extension Points** [​](https://dev.fluentcart.com/getting-started\#%F0%9F%8F%97%EF%B8%8F-flexible-extension-points)

- **Custom payment gateways** \- Integrate with any payment processor
- **Third-party integrations** \- Connect with external services and platforms
- **Custom modules** \- Add specialized functionality and features
- **API extensions** \- Build custom endpoints for mobile apps or external systems

### 💼 **Business Benefits** [​](https://dev.fluentcart.com/getting-started\#%F0%9F%92%BC-business-benefits)

- **No vendor lock-in** \- Your customizations stay with you, not dependent on external services
- **Unlimited scalability** \- Extend functionality as your business needs grow
- **Cost-effective** \- One-time development instead of ongoing SaaS fees
- **Complete control** \- Modify any aspect to match your specific business processes

## FluentCart Versions [​](https://dev.fluentcart.com/getting-started\#fluentcart-versions)

### FluentCart Core (Free) [​](https://dev.fluentcart.com/getting-started\#fluentcart-core-free)

The free version includes powerful core functionalities:

- ✅ **Product Management** \- Unlimited products and variations
- ✅ **Order Processing** \- Complete order management system
- ✅ **Customer Management** \- Customer accounts and profiles
- ✅ **Payment Processing** \- Multiple payment gateway support
- ✅ **Shipping Management** \- Flexible shipping options
- ✅ **Coupon System** \- Discount and promotional codes
- ✅ **Developer API** \- Full access to hooks and REST API

### FluentCart Pro (Premium) [​](https://dev.fluentcart.com/getting-started\#fluentcart-pro-premium)

The premium version adds advanced e-commerce features:

- 🚀 **Licensing System** \- Software license management
- 🚀 **Order Bumps** \- Advanced upselling and promotional tools
- 🚀 **Roles & Permissions** \- Advanced user role management
- 🚀 **Advanced Analytics** \- Detailed sales and performance analytics
- 🚀 **Subscription Management** \- Recurring billing and subscriptions
- 🚀 **Advanced Integrations** \- Deep third-party integrations
- 🚀 **Custom Modules** \- Extensible module system

## Core Development Concepts [​](https://dev.fluentcart.com/getting-started\#core-development-concepts)

### 📊 **Data Architecture** [​](https://dev.fluentcart.com/getting-started\#%F0%9F%93%8A-data-architecture)

FluentCart follows WordPress conventions with a clean, normalized database structure:

**Core Tables & Relationships:**

- **🛒 Orders** (`fct_orders`) \- Central hub for all order data
  - Stores order information, status, customer details
  - Links to all order items, transactions, and metadata
- **👥 Customers** (`fct_customers`) \- Customer management
  - Customer profiles, addresses, order history
  - Integration with WordPress users
- **📦 Products** (WordPress `posts` table) - Product catalog
  - Product information stored as WordPress custom post type
  - Additional details in `fct_product_details` and `fct_product_variations`
- **💳 Transactions** (`fct_order_transactions`) \- Payment processing
  - Payment records, refunds, transaction history
  - Integration with payment gateways
- **📋 Subscriptions** (`fct_subscriptions`) \- Recurring billing
  - Subscription management and renewals
  - Automated billing workflows

### 🔄 **E-commerce Workflow** [​](https://dev.fluentcart.com/getting-started\#%F0%9F%94%84-e-commerce-workflow)

The three-component e-commerce system:

1. **Products** \- Catalog management and inventory tracking
2. **Orders** \- Order processing and fulfillment
3. **Payments** \- Payment processing and transaction management

### 🔌 **Extension Points** [​](https://dev.fluentcart.com/getting-started\#%F0%9F%94%8C-extension-points)

Multiple ways to extend FluentCart:

- **WordPress Hooks** \- 315+ actions and filters for custom functionality
- **REST API** \- Complete programmatic access to all features
- **Module System** \- Add new payment gateways, shipping methods, and features
- **Custom Fields** \- Extend products, orders, and customers with custom data
- **Template System** \- Customize frontend templates and layouts

## Directory Structure [​](https://dev.fluentcart.com/getting-started\#directory-structure)

Understanding FluentCart's organized codebase:

```
fluent-cart/
├── app/                    # Core application logic
│   ├── Hooks/             # WordPress action/filter handlers
│   │   ├── Handlers/      # Hook handlers
│   │   ├── actions.php    # Action hooks
│   │   └── filters.php    # Filter hooks
│   ├── Http/              # Request handling and routing
│   │   ├── Controllers/   # API and admin controllers
│   │   ├── Middleware/    # Request middleware
│   │   └── Routes/        # API route definitions
│   ├── Models/            # Database models and relationships (45 files)
│   │   ├── Order.php      # Order model
│   │   ├── Customer.php   # Customer model
│   │   ├── Product.php    # Product model
│   │   └── ...           # Additional models
│   ├── Services/          # Business logic and services
│   │   ├── Payment/      # Payment processing services
│   │   ├── Shipping/     # Shipping calculation services
│   │   └── Helper.php    # Core helper utilities
│   ├── Views/            # PHP template files
│   ├── Events/           # Event system
│   ├── Listeners/        # Event listeners
│   └── Modules/          # Module system
│
├── api/                   # REST API endpoints and utilities
│   ├── Orders.php        # Order management API
│   ├── Customers.php     # Customer management API
│   ├── Products.php      # Product catalog API
│   ├── Resource/         # API resource classes
│   └── ...              # Additional API endpoints
│
├── resources/           # Frontend assets and templates
│   ├── admin/          # Admin interface (Vue.js) + Gutenberg blocks (React)
│   │   ├── Components/ # Vue components
│   │   ├── Modules/    # Feature modules
│   │   └── BlockEditor/# React Gutenberg blocks
│   ├── public/         # Public-facing components
│   │   ├── cart/       # Cart functionality
│   │   ├── checkout/   # Checkout process
│   │   └── customer-profile/ # Customer interface
│   ├── styles/         # SCSS stylesheets
│   └── images/         # Image resources
│
├── boot/                # Plugin initialization
├── config/              # Configuration files
├── database/            # Database migrations and schema
│   ├── Migrations/      # Database migration files (34 files)
│   ├── Seeder/         # Database seeders
│   └── DBMigrator.php  # Migration handler
│
├── dev/                 # Development tools and testing
│   ├── cli/            # CLI commands
│   ├── test/           # Test files
│   └── factories/      # Model factories
│
└── fluent-cart.php     # Plugin entry point
```

## Development Environment Setup [​](https://dev.fluentcart.com/getting-started\#development-environment-setup)

### Prerequisites [​](https://dev.fluentcart.com/getting-started\#prerequisites)

- **WordPress 5.0+** \- Modern WordPress installation
- **PHP 7.4+** \- Recent PHP version with required extensions
- **MySQL 5.6+** \- Database with InnoDB support
- **Basic WordPress Development** \- Understanding of hooks, plugins, and themes

### Development Tools [​](https://dev.fluentcart.com/getting-started\#development-tools)

- **Code Editor** \- VS Code, PhpStorm, or your preferred editor
- **Local Environment** \- Laravel Herd, XAMPP, WAMP, or Docker
- **Version Control** \- Git for tracking changes (optional but recommended)
- **API Testing** \- Postman or Insomnia for REST API development

### Getting Started Checklist [​](https://dev.fluentcart.com/getting-started\#getting-started-checklist)

1. **📖 Read the Fundamentals**

   - \[ \] Understand the database schema
   - \[ \] Review core models
   - \[ \] Explore global functions
2. **🔍 Explore the Hooks**

   - \[ \] Browse action hooks
   - \[ \] Study filter hooks
   - \[ \] Try event system
3. **🏗️ Build Your First Extension**

   - \[ \] Create a custom payment gateway
   - \[ \] Build a custom shipping method
   - \[ \] Add a custom module
4. **🌐 API Integration**

   - \[ \] Set up REST API access
   - \[ \] Test order management
   - \[ \] Explore webhook integration

## Quick Start Guide [​](https://dev.fluentcart.com/getting-started\#quick-start-guide)

### 1\. Database & Models [​](https://dev.fluentcart.com/getting-started\#_1-database-models)

Start by understanding FluentCart's data structure:

- [Database Schema](https://dev.fluentcart.com/database/schema.html) \- Complete table structure
- [Core Models](https://dev.fluentcart.com/database/models.html) \- Order, Customer, Product models
- [Model Relationships](https://dev.fluentcart.com/database/models/relationships.html) \- How data connects

### 2\. Developer Hooks [​](https://dev.fluentcart.com/getting-started\#_2-developer-hooks)

Learn how to extend FluentCart functionality:

- [Action Hooks](https://dev.fluentcart.com/hooks/actions.html) \- Trigger custom code on events
- [Filter Hooks](https://dev.fluentcart.com/hooks/filters.html) \- Modify data and behavior

## Community & Support [​](https://dev.fluentcart.com/getting-started\#community-support)

### 📚 **Learning Resources** [​](https://dev.fluentcart.com/getting-started\#%F0%9F%93%9A-learning-resources)

- **[Official Documentation](https://docs.fluentcart.com/)** \- Complete user and developer reference

### 💬 **Community** [​](https://dev.fluentcart.com/getting-started\#%F0%9F%92%AC-community)

- **[Official Support](https://fluentcart.com/account)** \- Technical support

Today

Hi! I’m your AI assistant. How can I assist you today?

Just now

Powered by **FluentBot**


---

## Subscription Customization | FluentCart Developer Docs

**URL** : https://dev.fluentcart.com/guides/subscriptions

[Skip to content](https://dev.fluentcart.com/guides/subscriptions#VPContent)

# Subscription Customization [​](https://dev.fluentcart.com/guides/subscriptions\#subscription-customization)

## Grace Periods [​](https://dev.fluentcart.com/guides/subscriptions\#grace-periods)

### What is a grace period? [​](https://dev.fluentcart.com/guides/subscriptions\#what-is-a-grace-period)

When a subscription renewal payment fails or is delayed, FluentCart does not immediately mark the subscription as expired. Instead it waits a configurable number of days - the **grace period** - before changing the status to `expired`.

This matters because some payment methods are asynchronous. The payment may have been initiated and will succeed, but confirmation arrives hours or days later. Expiring the subscription the moment a payment is not instantly confirmed would incorrectly cut off access for customers who have already paid.

Default grace periods by billing interval:

| Interval | Default grace (days) |
| --- | --- |
| Daily | 1 |
| Weekly | 3 |
| Monthly | 7 |
| Quarterly | 15 |
| Half-yearly | 15 |
| Yearly | 15 |

* * *

### When should you extend the grace period? [​](https://dev.fluentcart.com/guides/subscriptions\#when-should-you-extend-the-grace-period)

**The clearest case: SEPA Direct Debit.**

SEPA bank transfers can take 2–3 business days to confirm. For a monthly subscriber paying via SEPA, the default 7-day grace period is sufficient - but only if the payment was initiated on time. If your site processes renewals late (e.g. a missed cron run), or if a weekend is involved, a 7-day window can become tight. Extending it to 10–14 days eliminates false expiries for SEPA customers.

Other cases where you should extend:

- **ACH / bank transfers** - US bank transfers can take 3–5 business days.
- **Slow-processing gateways** - Some regional gateways in emerging markets batch-process overnight.
- **High-value subscriptions** - For yearly plans where incorrectly expiring a subscription has a large customer impact, a 21–30 day window is safer.

php

```
add_filter('fluent_cart/subscription/grace_period_days', function (array $gracePeriods): array {
    // Extend monthly grace period to 14 days to safely cover SEPA debit delays
    $gracePeriods['monthly'] = 14;

    // Give yearly subscribers a full month before expiry
    $gracePeriods['yearly'] = 30;

    return $gracePeriods;
});
```

* * *

### When should you reduce the grace period? [​](https://dev.fluentcart.com/guides/subscriptions\#when-should-you-reduce-the-grace-period)

If your product delivers time-sensitive value (live access, daily content, seat-based software), you may want stricter expiry - cut off access as soon as a payment has clearly failed, not 7–15 days later.

php

```
add_filter('fluent_cart/subscription/grace_period_days', function (array $gracePeriods): array {
    // Tight grace for daily content - expire after 1 missed day regardless of interval
    $gracePeriods['monthly']     = 1;
    $gracePeriods['quarterly']   = 1;
    $gracePeriods['half_yearly'] = 1;
    $gracePeriods['yearly']      = 3;

    return $gracePeriods;
});
```

WARNING

Reducing grace periods below 3 days for bank-based payment methods (SEPA, ACH) will cause valid customers to lose access before their payment has had time to settle. Only do this when your payment methods are card-only or instant-confirm.

* * *

### Targeting grace period by payment method [​](https://dev.fluentcart.com/guides/subscriptions\#targeting-grace-period-by-payment-method)

If you accept both instant (card) and delayed (SEPA/ACH) payment methods, you can apply different grace periods per customer:

php

```
add_filter('fluent_cart/subscription/grace_period_days', function (array $gracePeriods): array {
    // Default stays for card-based subscriptions.
    // Individual subscriptions using SEPA need more time - handled in grace_period_days_for_subscription.
    return $gracePeriods;
});
```

TIP

The `fluent_cart/subscription/grace_period_days` filter applies globally across all subscriptions of a given billing interval. If you need per-subscription overrides (e.g. by payment method), use the subscription's `current_payment_method` field to conditionally adjust values in your filter callback, by loading the specific subscription from context.

* * *

### Reference [​](https://dev.fluentcart.com/guides/subscriptions\#reference)

- **Filter:**`fluent_cart/subscription/grace_period_days`
- **Source:**`app/Services/Payments/SubscriptionHelper.php`
- **Full filter reference:** [Customers & Subscriptions filters](https://dev.fluentcart.com/hooks/filters/customers-and-subscriptions.html#subscription-grace_period_days)

* * *

## Custom Subscription Intervals [​](https://dev.fluentcart.com/guides/subscriptions\#custom-subscription-intervals)

FluentCart ships with `daily`, `weekly`, `monthly`, `quarterly`, `half_yearly`, and `yearly`. You can register additional intervals through filters.

The example below adds an **every 10th day** interval. Swap in your own values as needed.

### 1\. Register the interval option [​](https://dev.fluentcart.com/guides/subscriptions\#_1-register-the-interval-option)

Adds the interval to the product editor dropdown. All three fields are required.

php

```
add_filter('fluent_cart/available_subscription_interval_options', function ($options) {
    return array_merge($options, [\
        [\
            'label'     => __('Every 10th day', 'fluent-cart'), // shown in dropdown\
            'value'     => 'every_tenth_day',                   // stored in database\
            'map_value' => '10th Day',                          // readable format\
        ],\
    ]);
});
```

### 2\. Define the interval in days [​](https://dev.fluentcart.com/guides/subscriptions\#_2-define-the-interval-in-days)

Used internally for trial day calculations and renewal scheduling.

php

```
add_filter('fluent_cart/subscription_interval_in_days', function ($days, $args) {
    if ($args['interval'] === 'every_tenth_day') {
        return 10;
    }
    return $days;
}, 10, 2);
```

### 3\. Map to gateway billing period [​](https://dev.fluentcart.com/guides/subscriptions\#_3-map-to-gateway-billing-period)

Required for built-in gateways (Stripe, PayPal). If you own the gateway code, handle this directly in your processor instead.

php

```
add_filter('fluent_cart/subscription_billing_period', function ($billingPeriod, $args) {
    if ($args['subscription_interval'] !== 'every_tenth_day') {
        return $billingPeriod;
    }

    if ($args['payment_method'] === 'stripe') {
        $billingPeriod['interval_unit']      = 'day';
        $billingPeriod['interval_frequency'] = 10;
    }

    if ($args['payment_method'] === 'paypal') {
        $billingPeriod['interval_unit']      = 'day';
        $billingPeriod['interval_frequency'] = 10;
    }

    return $billingPeriod;
}, 10, 2);
```

### 4\. Set max trial days (optional) [​](https://dev.fluentcart.com/guides/subscriptions\#_4-set-max-trial-days-optional)

Caps how many trial days can be assigned to this interval.

php

```
add_filter('fluent_cart/max_trial_days_allowed', function ($days, $args) {
    if ($args['repeat_interval'] === 'every_tenth_day') {
        return min($args['existing_trial_days'] + $args['interval_in_days'], 10);
    }
    return $days;
}, 10, 2);
```

### 5\. License validity (Pro - licensed products only) [​](https://dev.fluentcart.com/guides/subscriptions\#_5-license-validity-pro-%E2%80%94-licensed-products-only)

If the product uses the licensing module, set the expiry period for the custom interval.

php

```
add_filter('fluent_cart/license/default_validity_by_variation', function ($validity, $args) {
    $interval = Arr::get($args['variation']->other_info, 'repeat_interval');
    if ($interval === 'every_tenth_day') {
        return ['unit' => 'day', 'value' => 10];
    }
    return $validity;
}, 10, 2);
```

Gateway compatibility

**Stripe** accepts any positive integer with `day`, `week`, `month`, or `year`.

**PayPal** supports the same units but has frequency limits - check PayPal's billing plan docs for your interval.

Full reference and additional snippets: [fluent-cart-snippets on GitHub](https://github.com/fluent-cart/fluent-cart-snippets/blob/main/Subscriptions/HOW_TO_ADD_CUSTOM_SUBSCRIPTION_INTERVAL.md)

Today

Hi! I’m your AI assistant. How can I assist you today?

Just now

Powered by **FluentBot**


---
