# Section Customization & Themes

Source : docs.fluentcart.com
Date scrape : 2026-05-19

---

## Advanced Customization with CSS Variables - FluentCart Documentation
URL : https://docs.fluentcart.com/guide/customization-and-themes/advanced-customization-using-css

[Skip to content](https://docs.fluentcart.com/guide/customization-and-themes/advanced-customization-using-css#VPContent)

# Advanced Customization with CSS Variables [​](https://docs.fluentcart.com/guide/customization-and-themes/advanced-customization-using-css\#advanced-customization-with-css-variables)

FluentCart provides a powerful set of CSS variables that let you customize the appearance of your store without writing complex CSS or modifying theme files. Whether you want to change button colors, adjust text styles, or completely transform the look of your checkout, CSS variables make it easy to match your brand.

## Quick Start [​](https://docs.fluentcart.com/guide/customization-and-themes/advanced-customization-using-css\#quick-start)

The fastest way to customize your store is by using the WordPress Customizer:

1. Go to **Appearance → Customize → Additional CSS**
2. Add your custom CSS variables
3. Click **Publish**

For example, to change all primary buttons to blue:

css

```
:root {
  --fct-btn-bg-color: #0066cc;
}
```

That's it! All buttons across your store will now use this color.

## How CSS Variables Work [​](https://docs.fluentcart.com/guide/customization-and-themes/advanced-customization-using-css\#how-css-variables-work)

CSS variables (also called custom properties) are values you can define once and reuse throughout your site. FluentCart uses variables for colors, spacing, borders, and more. By overriding these variables, you can customize your store's appearance without touching the original code.

### Where to Add CSS Variables [​](https://docs.fluentcart.com/guide/customization-and-themes/advanced-customization-using-css\#where-to-add-css-variables)

You can add CSS variables in three ways:

1. **WordPress Customizer** (Recommended): Appearance → Customize → Additional CSS
2. **Theme CSS File**: Add to your theme's `style.css`
3. **Page Builders**: Use the Custom CSS section in Elementor, Bricks, or other builders

## Global Color Variables [​](https://docs.fluentcart.com/guide/customization-and-themes/advanced-customization-using-css\#global-color-variables)

These variables affect multiple pages at once, making them perfect for store-wide changes.

### Button Colors [​](https://docs.fluentcart.com/guide/customization-and-themes/advanced-customization-using-css\#button-colors)

| Variable | Default Value | Description |
| --- | --- | --- |
| `--fct-btn-bg-color` | `#253241` | Primary button background |
| `--fct-btn-text-color` | `#ffffff` | Primary button text |
| `--fct-btn-border-color` | `#253241` | Primary button border |

### Text Colors [​](https://docs.fluentcart.com/guide/customization-and-themes/advanced-customization-using-css\#text-colors)

| Variable | Default Value | Description |
| --- | --- | --- |
| `--fct-primary-text-color` | `#2F3448` | Headings and important text |
| `--fct-secondary-text-color` | `#565865` | Descriptions and body text |

### Background Colors [​](https://docs.fluentcart.com/guide/customization-and-themes/advanced-customization-using-css\#background-colors)

| Variable | Default Value | Description |
| --- | --- | --- |
| `--fct-border-color` | `#d6dae1` | Input borders and dividers |
| `--fct-primary-bg-color` | `#4f46e5` | Primary backgrounds |
| `--fct-secondary-bg-color` | `#f9fafb` | Secondary backgrounds |

### Input Colors [​](https://docs.fluentcart.com/guide/customization-and-themes/advanced-customization-using-css\#input-colors)

| Variable | Default Value | Description |
| --- | --- | --- |
| `--fct-input-bg-color` | `#ffffff` | Input background |
| `--fct-input-text-color` | `#2F3448` | Input text |
| `--fct-input-border-color` | `#d6dae1` | Input border |

**Example: Making all buttons blue**

css

```
:root {
  --fct-btn-bg-color: #0066cc;
  --fct-btn-border-color: #0066cc;
}
```

## Checkout Page Customization [​](https://docs.fluentcart.com/guide/customization-and-themes/advanced-customization-using-css\#checkout-page-customization)

The checkout page has its own set of variables for fine-tuned control.

### Checkout Buttons [​](https://docs.fluentcart.com/guide/customization-and-themes/advanced-customization-using-css\#checkout-buttons)

| Variable | Default Value | Description |
| --- | --- | --- |
| `--fct-checkout-btn-bg-color` | `--fct-checkout-primary-bg-color` | Place Order button |
| `--fct-checkout-btn-text-color` | `#ffffff` | Button text |

### Checkout Form Elements [​](https://docs.fluentcart.com/guide/customization-and-themes/advanced-customization-using-css\#checkout-form-elements)

| Variable | Default Value | Description |
| --- | --- | --- |
| `--fct-checkout-input-bg-color` | `#ffffff` | Input background |
| `--fct-checkout-input-text-color` | `theme('colors.system.dark')` | Input text |
| `--fct-checkout-input-border-color` | `--fct-checkout-border-color` | Input border |

### Checkout Sections [​](https://docs.fluentcart.com/guide/customization-and-themes/advanced-customization-using-css\#checkout-sections)

| Variable | Default Value | Description |
| --- | --- | --- |
| `--fct-checkout-summary-bg-color` | `#ffffff` | Order summary background |
| `--fct-checkout-payment-method-bg-color` | `#ffffff` | Payment methods background |
| `--fct-checkout-shipping-methods-bg` | `#ffffff` | Shipping methods background |

**Example: Green checkout buttons**

css

```
.fct-checkout {
  --fct-checkout-btn-bg-color: #28a745;
}
```

## Product Card Customization [​](https://docs.fluentcart.com/guide/customization-and-themes/advanced-customization-using-css\#product-card-customization)

Product cards are used in the shop page, related products, and product grids.

### Card Styling [​](https://docs.fluentcart.com/guide/customization-and-themes/advanced-customization-using-css\#card-styling)

| Variable | Default Value | Description |
| --- | --- | --- |
| `--fct-card-bg` | `#ffffff` | Card background |
| `--fct-card-border-color` | `#d6dae1` | Card border |

### Card Text [​](https://docs.fluentcart.com/guide/customization-and-themes/advanced-customization-using-css\#card-text)

| Variable | Default Value | Description |
| --- | --- | --- |
| `--fct-card-primary-text-color` | `#2F3448` | Product title |
| `--fct-card-text-color` | `#565865` | Product description |
| `--fct-heading-color` | `#2F3448` | Card headings |

### Card Buttons [​](https://docs.fluentcart.com/guide/customization-and-themes/advanced-customization-using-css\#card-buttons)

| Variable | Default Value | Description |
| --- | --- | --- |
| `--fct-card-btn-bg-color` | `#253241` | View Options button |
| `--fct-card-btn-text-color` | `#ffffff` | Button text |

**Example: Custom product card style**

css

```
.fct-product-card {
  --fct-card-bg: #f9f9f9;
  --fct-card-border-color: #e0e0e0;
  --fct-card-btn-bg-color: #0066cc;
}
```

## Product Buttons [​](https://docs.fluentcart.com/guide/customization-and-themes/advanced-customization-using-css\#product-buttons)

FluentCart uses different button styles for "Add to Cart" and "Buy Now" actions.

### Add to Cart Button [​](https://docs.fluentcart.com/guide/customization-and-themes/advanced-customization-using-css\#add-to-cart-button)

| Variable | Default Value | Description |
| --- | --- | --- |
| `--fct-add-to-cart-btn-bg-color` | `#ffffff` | Button background |
| `--fct-add-to-cart-btn-text-color` | `#2f3448` | Button text |
| `--fct-add-to-cart-btn-hover-bg-color` | `#f5f6f7` | Hover background |
| `--fct-add-to-cart-btn-border-color` | `#d6dae1` | Button border |

### Buy Now Button [​](https://docs.fluentcart.com/guide/customization-and-themes/advanced-customization-using-css\#buy-now-button)

| Variable | Default Value | Description |
| --- | --- | --- |
| `--fct-direct-btn-bg-color` | `#253241` | Button background |
| `--fct-direct-btn-text-color` | `#ffffff` | Button text |

**Example: Custom button colors**

css

```
:root {
  --fct-add-to-cart-btn-bg-color: #f0f0f0;
  --fct-add-to-cart-btn-text-color: #333;
  --fct-direct-btn-bg-color: #0066cc;
}
```

## Cart Drawer Customization [​](https://docs.fluentcart.com/guide/customization-and-themes/advanced-customization-using-css\#cart-drawer-customization)

The cart drawer (slide-out cart) can be customized independently.

### Drawer Colors [​](https://docs.fluentcart.com/guide/customization-and-themes/advanced-customization-using-css\#drawer-colors)

| Variable | Default Value | Description |
| --- | --- | --- |
| `--fct-cart-drawer-bg` | `#ffffff` | Drawer background |
| `--fct-cart-drawer-border-color` | `#d6dae1` | Drawer border |
| `--fct-cart-drawer-primary-text-color` | `#2F3448` | Primary text |
| `--fct-cart-drawer-secondary-text-color` | `#565865` | Secondary text |

### Drawer Buttons [​](https://docs.fluentcart.com/guide/customization-and-themes/advanced-customization-using-css\#drawer-buttons)

| Variable | Default Value | Description |
| --- | --- | --- |
| `--fct-cart-drawer-btn-bg-color` | `#253241` | Action button |
| `--fct-cart-drawer-btn-text-color` | `#ffffff` | Button text |
| `--fct-cart-drawer-open-btn-bg-color` | `#253241` | Cart icon button |
| `--fct-view-cart-btn-bg-color` | `#253241` | View Cart button |

### Cart Badge [​](https://docs.fluentcart.com/guide/customization-and-themes/advanced-customization-using-css\#cart-badge)

| Variable | Default Value | Description |
| --- | --- | --- |
| `--fct-cart-drawer-badge-bg-color` | `#ef4444` | Badge background |
| `--fct-cart-drawer-badge-text-color` | `#ffffff` | Badge text |

**Example: Blue cart drawer**

css

```
.fct-cart-drawer {
  --fct-cart-drawer-btn-bg-color: #0066cc;
  --fct-cart-drawer-badge-bg-color: #ff6b6b;
}
```

## Customer Dashboard Customization [​](https://docs.fluentcart.com/guide/customization-and-themes/advanced-customization-using-css\#customer-dashboard-customization)

The customer dashboard (account page) has its own color scheme.

### Dashboard Text [​](https://docs.fluentcart.com/guide/customization-and-themes/advanced-customization-using-css\#dashboard-text)

| Variable | Default Value | Description |
| --- | --- | --- |
| `--fct-customer-dashboard-primary-text-color` | `#2F3448` | Primary text |
| `--fct-customer-dashboard-secondary-text-color` | `#565865` | Secondary text |
| `--fct-customer-dashboard-title-color` | `#1f2937` | Page title |
| `--fct-customer-dashboard-sub-title-color` | `#6b7280` | Section title |

### Dashboard Navigation [​](https://docs.fluentcart.com/guide/customization-and-themes/advanced-customization-using-css\#dashboard-navigation)

| Variable | Default Value | Description |
| --- | --- | --- |
| `--fct-customer-dashboard-nav-text-color` | `#4b5563` | Nav item text |
| `--fct-customer-dashboard-nav-active-text-color` | `#4f46e5` | Active nav text |
| `--fct-customer-dashboard-nav-active-bg-color` | `#eef2ff` | Active nav background |
| `--fct-customer-dashboard-nav-active-bar-color` | `#4f46e5` | Active nav indicator |

### Dashboard Buttons [​](https://docs.fluentcart.com/guide/customization-and-themes/advanced-customization-using-css\#dashboard-buttons)

| Variable | Default Value | Description |
| --- | --- | --- |
| `--fct-customer-dashboard-btn-bg-color` | `#4f46e5` | Action button |
| `--fct-customer-dashboard-btn-text-color` | `#ffffff` | Button text |
| `--fct-customer-dashboard-logout-btn-bg-color` | `#ef4444` | Logout button |

**Example: Blue dashboard theme**

css

```
.fct-customer-dashboard {
  --fct-customer-dashboard-nav-active-bg-color: #0066cc;
  --fct-customer-dashboard-btn-bg-color: #0066cc;
}
```

## Shop Page Customization [​](https://docs.fluentcart.com/guide/customization-and-themes/advanced-customization-using-css\#shop-page-customization)

Customize the main shop page appearance.

### Shop Text Colors [​](https://docs.fluentcart.com/guide/customization-and-themes/advanced-customization-using-css\#shop-text-colors)

| Variable | Default Value | Description |
| --- | --- | --- |
| `--fct-shop-primary-text-color` | `#2F3448` | Primary text |
| `--fct-shop-secondary-text-color` | `#565865` | Secondary text |

### Shop Backgrounds [​](https://docs.fluentcart.com/guide/customization-and-themes/advanced-customization-using-css\#shop-backgrounds)

| Variable | Default Value | Description |
| --- | --- | --- |
| `--fct-shop-primary-bg-color` | `#ffffff` | Primary background |
| `--fct-shop-secondary-bg-color` | `#f9fafb` | Secondary background |

### Shop Buttons [​](https://docs.fluentcart.com/guide/customization-and-themes/advanced-customization-using-css\#shop-buttons)

| Variable | Default Value | Description |
| --- | --- | --- |
| `--fct-shop-btn-bg-color` | `#253241` | Filter/Sort buttons |
| `--fct-shop-btn-text-color` | `#ffffff` | Button text |

### Shop Pagination [​](https://docs.fluentcart.com/guide/customization-and-themes/advanced-customization-using-css\#shop-pagination)

| Variable | Default Value | Description |
| --- | --- | --- |
| `--fct-shop-paginator-bg` | `#ffffff` | Pagination background |
| `--fct-shop-paginator-items-color` | `#4b5563` | Page number color |
| `--fct-shop-paginator-items-active-bg` | `#4f46e5` | Active page background |
| `--fct-shop-paginator-items-active-color` | `#ffffff` | Active page text |
| `--fct-shop-paginator-items-hover-bg` | `#f3f4f6` | Hover background |

**Example: Custom shop theme**

css

```
.fct-shop-app {
  --fct-shop-btn-bg-color: #0066cc;
  --fct-shop-paginator-items-active-bg: #0066cc;
}
```

## Single Product Page Customization [​](https://docs.fluentcart.com/guide/customization-and-themes/advanced-customization-using-css\#single-product-page-customization)

Customize individual product pages.

### Product Page Text [​](https://docs.fluentcart.com/guide/customization-and-themes/advanced-customization-using-css\#product-page-text)

| Variable | Default Value | Description |
| --- | --- | --- |
| `--fct-single-product-primary-text-color` | `theme('colors.system.dark')` | Primary text |
| `--fct-single-product-secondary-text-color` | `theme('colors.system.mid')` | Secondary text |

### Product Page Borders [​](https://docs.fluentcart.com/guide/customization-and-themes/advanced-customization-using-css\#product-page-borders)

| Variable | Default Value | Description |
| --- | --- | --- |
| `--fct-single-product-border-color` | `theme('colors.gray.outline')` | Element borders |
| `--fct-single-product-active-border-color` | `theme('colors.primary.500')` | Active borders |

### Quantity Selector [​](https://docs.fluentcart.com/guide/customization-and-themes/advanced-customization-using-css\#quantity-selector)

| Variable | Default Value | Description |
| --- | --- | --- |
| `--fct-single-product-qty-bg` | `#eaecf0` | Quantity input background |
| `--fct-single-product-qty-text-color` | `#2F3448` | Quantity text |

**Example: Custom product page**

css

```
.fct-single-product-page {
  --fct-single-product-qty-bg: #f0f0f0;
  --fct-single-product-border-color: #e0e0e0;
}
```

## Common Customization Examples [​](https://docs.fluentcart.com/guide/customization-and-themes/advanced-customization-using-css\#common-customization-examples)

Here are some frequently requested customizations:

### Change All Buttons to Blue [​](https://docs.fluentcart.com/guide/customization-and-themes/advanced-customization-using-css\#change-all-buttons-to-blue)

css

```
:root {
  --fct-btn-bg-color: #0066cc;
  --fct-btn-border-color: #0066cc;
}
```

### Update Product Card Style [​](https://docs.fluentcart.com/guide/customization-and-themes/advanced-customization-using-css\#update-product-card-style)

css

```
.fct-product-card {
  --fct-card-bg: #fafafa;
  --fct-card-border-color: #e0e0e0;
  --fct-card-btn-bg-color: #0066cc;
}
```

### Style the Checkout Page [​](https://docs.fluentcart.com/guide/customization-and-themes/advanced-customization-using-css\#style-the-checkout-page)

css

```
.fct-checkout {
  --fct-checkout-btn-bg-color: #28a745;
  --fct-checkout-primary-bg-color: #28a745;
}
```

### Customize the Cart Drawer [​](https://docs.fluentcart.com/guide/customization-and-themes/advanced-customization-using-css\#customize-the-cart-drawer)

css

```
.fct-cart-drawer {
  --fct-cart-drawer-btn-bg-color: #0066cc;
  --fct-cart-drawer-badge-bg-color: #ff6b6b;
}
```

### Update the Customer Dashboard [​](https://docs.fluentcart.com/guide/customization-and-themes/advanced-customization-using-css\#update-the-customer-dashboard)

css

```
.fct-customer-dashboard {
  --fct-customer-dashboard-nav-active-bg-color: #0066cc;
  --fct-customer-dashboard-nav-active-text-color: #ffffff;
}
```

## Tips for Best Results [​](https://docs.fluentcart.com/guide/customization-and-themes/advanced-customization-using-css\#tips-for-best-results)

1. **Start Global**: Use `:root` for store-wide changes before targeting specific pages
2. **Be Specific**: Target specific pages (like `.fct-checkout`) when you need granular control
3. **Test Thoroughly**: Check multiple pages after making changes to ensure consistency
4. **Use Browser DevTools**: Inspect elements to discover which variables affect specific elements
5. **Keep It Simple**: Only override the variables you need-most have sensible defaults

## Important Notes [​](https://docs.fluentcart.com/guide/customization-and-themes/advanced-customization-using-css\#important-notes)

- All CSS variables have fallback values built-in, so your store will still work if a variable is missing
- Variables can inherit from parent variables automatically
- Third-party library variables (like Swiper or Toastify) are not included in this guide
- For the most up-to-date list of variables, check the `/resources/public/` directory in FluentCart

## Getting Help [​](https://docs.fluentcart.com/guide/customization-and-themes/advanced-customization-using-css\#getting-help)

If you need help with CSS variables or encounter issues:

1. Check the [Troubleshooting & Support](https://docs.fluentcart.com/guide/troubleshooting-support/common-issues-faqs) section
2. Use browser DevTools to inspect elements and identify variables
3. Visit our [support forums](https://fluentcart.com/support) for community help
4. Contact our support team for advanced customization assistance

> **Note**: CSS customizations are theme-independent and will persist even if you switch themes, as long as FluentCart remains active.

Today

Hi! I’m your AI assistant. How can I assist you today?

Just now

Powered by **FluentBot**

---

## Code Snippets - FluentCart Documentation
URL : https://docs.fluentcart.com/guide/customization-and-themes/code-snippets

[Skip to content](https://docs.fluentcart.com/guide/customization-and-themes/code-snippets#VPContent)

# Code Snippets [​](https://docs.fluentcart.com/guide/customization-and-themes/code-snippets\#code-snippets)

Here you'll find ready-to-use code snippets for FluentCart. These snippets help you customize and extend your store's functionality. Simply copy the code and add it to your theme's `functions.php` file or use a code snippets plugin.

## Checkout [​](https://docs.fluentcart.com/guide/customization-and-themes/code-snippets\#checkout)

### Hide Unnecessary Decimals [​](https://docs.fluentcart.com/guide/customization-and-themes/code-snippets\#hide-unnecessary-decimals)

By default, FluentCart displays prices with decimal places (e.g., $10.00). If you prefer cleaner pricing without unnecessary decimals (e.g., $10 instead of $10.00), use this snippet.

```
<?php

add_filter('fluent_cart/hide_unnecessary_decimals', '__return_true');
```

[View on GitHub Gist ↗](https://gist.github.com/377042dacea4f547fe606210cadc971e)

This filter removes trailing zeros from prices, so `$10.00` becomes `$10` while `$10.50` stays as `$10.50`.

### Display Custom Line Item Metadata on Checkout [​](https://docs.fluentcart.com/guide/customization-and-themes/code-snippets\#display-custom-line-item-metadata-on-checkout)

Use the `fluent_cart/cart/line_item/line_meta` action to print custom metadata under each cart item in the checkout order summary. This hook runs after the product title, variant title, and child variant details are rendered, but before the line item price.

php

```
add_action('fluent_cart/cart/line_item/line_meta', function ($data) {
    $item = $data['item'] ?? [];

    if (empty($item['line_meta']) || !is_array($item['line_meta'])) {
        return;
    }

    $giftMessage = $item['line_meta']['gift_message'] ?? '';

    if (!$giftMessage) {
        return;
    }

    echo '<div class="fct-custom-line-meta">';
    echo '<small>' . esc_html__('Gift message:', 'your-textdomain') . ' ' . esc_html($giftMessage) . '</small>';
    echo '</div>';
}, 10, 1);
```

The callback receives one `$data` array with the current line item rendering context:

php

```
$data = [\
    'item'    => $item,     // Cart item data. This is the main value to use.\
    'cart'    => $cart,     // Current cart model when available, otherwise null.\
    'product' => $product,  // Reserved for product data; currently may be null.\
    'variant' => $variant,  // Reserved for variation data; currently may be null.\
];
```

The `item` value is the reliable source for line item details. Use `$data['item']['line_meta']` when you need to show per-item details such as gift messages, engraving text, license information, booking dates, or other custom options stored with the line item.

## Customer Profile [​](https://docs.fluentcart.com/guide/customization-and-themes/code-snippets\#customer-profile)

### Add a Custom Menu Item to the Customer Profile [​](https://docs.fluentcart.com/guide/customization-and-themes/code-snippets\#add-a-custom-menu-item-to-the-customer-profile)

Use the `addCustomerDashboardEndpoint()` method to add a custom menu item to the FluentCart customer profile dashboard.

```
<?

add_action('init', function () {
    \FluentCart\Api\FluentCartGeneralApi::getInstance()->addCustomerDashboardEndpoint(
        'support', [\
            'title' => __('Customer Support', 'fluent-cart-pro'),\
            // 'render_callback' => function () {\
            //     echo 'Put your text';\
            // },\
            'icon_svg' => '<svg style="padding: 2px;" xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><path d="M21 11.25v8.25a1.5 1.5 0 0 1-1.5 1.5H4.5a1.5 1.5 0 0 1-1.5-1.5v-8.25M12 4.875A2.625 2.625 0 1 0 9.375 7.5H12m0-2.625V7.5m0-2.625A2.625 2.625 0 1 1 14.625 7.5H12m0 0V21m-8.625-9.75h18c.621 0 1.125-.504 1.125-1.125v-1.5c0-.621-.504-1.125-1.125-1.125h-18c-.621 0-1.125.504-1.125 1.125v1.5c0 .621.504 1.125 1.125 1.125Z"></path></svg>',\
            'page_id' => 178,\
        ]
    );
});

//Note: If you use render callback then the content from call back will be displayed. If you would like to add a specific wordpress page, skip render_callback method
```

[View on GitHub Gist ↗](https://gist.github.com/a92363c5a73e59163f52c35cbcc7bf28)

If you use `render_callback`, FluentCart will display the callback output for the menu item. If you want to show a specific WordPress page instead, skip the `render_callback` method and provide the `page_id`.

Today

Hi! I’m your AI assistant. How can I assist you today?

Just now

Powered by **FluentBot**

---

## Customize Store with Bricks - FluentCart Documentation
URL : https://docs.fluentcart.com/guide/customization-and-themes/customize-store-with-bricks

[Skip to content](https://docs.fluentcart.com/guide/customization-and-themes/customize-store-with-bricks#VPContent)

# Customize Store with Bricks [​](https://docs.fluentcart.com/guide/customization-and-themes/customize-store-with-bricks\#customize-store-with-bricks)

FluentCart works with the powerful **Bricks** theme & page builder, giving you complete creative control over your store's design. Instead of being limited to standard layouts, this integration adds a full set of FluentCart elements directly into the Bricks editor, allowing you to build everything from custom shop pages to unique single product layouts with a simple drag-and-drop interface.

This guide will show you how to use FluentCart's dedicated elements within Bricks.

## Getting Started [​](https://docs.fluentcart.com/guide/customization-and-themes/customize-store-with-bricks\#getting-started)

The integration is automatic. As long as you have both **FluentCart** and the **Bricks theme** installed and active on your site, you will find the FluentCart elements ready to use inside the Bricks editor.

### Building Your Main Shop Page [​](https://docs.fluentcart.com/guide/customization-and-themes/customize-store-with-bricks\#building-your-main-shop-page)

The easiest way to display your products is by using the main **Products** element.

1. Open any page with the Bricks editor.
2. Click the plus icon ( **+**) to add a new element.
3. In the elements panel, scroll down to the **FluentCart** category and click the **Products** element.

![FluentCart Elements in Brick](https://docs.fluentcart.com/assets/bricks-1.B2pCGDOm.webp)

This will instantly add a beautiful, fully functional grid of your products to the page.

#### Customizing the Products Element [​](https://docs.fluentcart.com/guide/customization-and-themes/customize-store-with-bricks\#customizing-the-products-element)

The real power comes from the customization options. After adding the **Products** element click on the element name in the right-hand panel, you can use the settings in the left-hand panel to control exactly how it looks and what it displays.

- **Content Settings**
  - **Display:** Choose between **Grid** and **List** view, toggle the frontend **View Switcher**, and pick a **Pagination Type** ( **Numbers** or **Scroll**). Set the number of **Columns**, the **Gap** between products, and how many **Products per page** are shown.
  - **Query:** This is a powerful feature that lets you choose which products to display. You can filter by **Product Type**, **Product Categories**, **Include** or **Exclude** specific products by name, restrict to **On sale Products only**, and choose whether to **Allow Out Of Stock** items. Perfect for creating custom pages that feature "New Arrivals" or "Best Sellers."
  - **Filter:** Add a customer-facing filter sidebar so shoppers can narrow the collection themselves. See [Customer-Facing Product Filters](https://docs.fluentcart.com/guide/customization-and-themes/customize-store-with-bricks#customer-facing-product-filters) below for the full list of filter controls.
  - **Fields:** This allows you to reorder the different parts of the product card. You can drag and drop the fields to change the order of the product image, title, price, and button.
- **Style Settings** Under the **Style** tab, you have full control over the visual design. You can customize the Layout, Typography, Borders, and more to perfectly match the look and feel of your brand.

![Elements options in Brick](https://docs.fluentcart.com/assets/bricks-3.Dje4akbU.webp)

### Grid vs. List View [​](https://docs.fluentcart.com/guide/customization-and-themes/customize-store-with-bricks\#grid-vs-list-view)

The **Products** element supports two layouts that customers can switch between on the frontend:

- **Grid (default):** Products appear in a multi-column card layout - ideal for shop pages where the product image is the main attention-grabber.
- **List:** Products appear in a single-column row layout - better for catalogs where the title, description, and price need more room to breathe.

Two settings control this:

- **View Mode:** Sets the default layout when the page first loads. Pick **Grid** or **List**.
- **Show View Switcher:** Enabled by default. When on, customers see toggle buttons on the frontend that let them flip between Grid and List without reloading the page. Turn this off if you want to lock the layout to a single mode.

### Pagination Type [​](https://docs.fluentcart.com/guide/customization-and-themes/customize-store-with-bricks\#pagination-type)

Choose how customers move through long product lists:

- **Numbers (default):** Classic numbered pagination at the bottom of the list. Best for SEO and predictable navigation.
- **Scroll:** Products load automatically as the customer scrolls. Best for long, browse-heavy collections.

### Customer-Facing Product Filters [​](https://docs.fluentcart.com/guide/customization-and-themes/customize-store-with-bricks\#customer-facing-product-filters)

The **Filter** group adds a filter sidebar to the frontend so shoppers can refine the collection on their own - without you needing to build separate landing pages for every category, brand, or price band.

- **Enable Filter:** The master switch. Turn this on to expose the filter sidebar; the rest of the filter controls below are hidden until this is enabled.
- **Enable Sort By:** On by default. Adds a sort dropdown so customers can reorder products by price, name, or date.
- **Live Filter:** When on, results update instantly as the customer changes a filter - no "Apply" button required.
- **Wildcard Filter:** When on, free-text searches match partial words (e.g. typing `shoe` matches `shoes`, `shoebox`, etc.).
- **Product Categories:** Add a category filter section to the sidebar. With **Display Name** you can rename the section (e.g. show "Shop by Category" instead of the default "Product Categories").
- **Product Brands:** Add a brand filter section. The **Display Name** field works the same way.
- **Price Range:** Add a price-range slider. The **Display Name** field lets you label it however suits your store (e.g. "Filter by Price").

Use these together to build a filtered shop experience that matches your customers' expectations - the filters work without a page reload when **Live Filter** is on, and they integrate with the **Sort By** dropdown for combined refinement.

Today

Hi! I’m your AI assistant. How can I assist you today?

Just now

Powered by **FluentBot**

---

## FluentCart Widgets for Elementor - FluentCart Documentation
URL : https://docs.fluentcart.com/guide/customization-and-themes/elementor-fluentcart-widgets

[Skip to content](https://docs.fluentcart.com/guide/customization-and-themes/elementor-fluentcart-widgets#VPContent)

# FluentCart Widgets for Elementor [​](https://docs.fluentcart.com/guide/customization-and-themes/elementor-fluentcart-widgets\#fluentcart-widgets-for-elementor)

The **FluentCart** category in the Elementor editor groups 12 store-wide widgets you can drop on any page - your home page, shop page, header, footer, or a custom landing page. They cover product display, cart, checkout, navigation, branding, and the all-in-one Product Info summary.

INFO

Before you can use these widgets, make sure the Elementor Blocks addon is turned on. See [Using Elementor Widgets](https://docs.fluentcart.com/guide/customization-and-themes/using-elementor-widgets) for the activation steps.

## 1\. Add to Cart [​](https://docs.fluentcart.com/guide/customization-and-themes/elementor-fluentcart-widgets\#_1-add-to-cart)

Adds a single **Add to Cart** button that customers can click to drop a specific product (or variation) into their cart without leaving the page.

- **Content Tab:**Pick what the button sells and how it reads.
  - **Select Product Variation:** Search for and select the product or variation this button should add.
  - **Button Text:** Customize the button label (default is _Add to Cart_).
- **Style Tab:** Customize the button's typography, background color, text color, border, hover state, and padding.
- **Advanced Tab:** Standard Elementor controls for margin, padding, and responsive visibility.

![Screenshot of the Add to Cart widget edit panel in Elementor](https://docs.fluentcart.com/images/customization-and-themes/fluentcart-elementor-widgets/widget-for-fluentcart/fluentcart-elementor-2.webp)

## 2\. Buy Now Button [​](https://docs.fluentcart.com/guide/customization-and-themes/elementor-fluentcart-widgets\#_2-buy-now-button)

A focused shortcut that sends customers straight to checkout without stopping at the cart. Perfect for landing pages built around a single offer.

- **Content Tab:**Set up what the button sells and how it behaves.
  - **Select Product Variation:** Choose the product or variation this button represents.
  - **Button Text:** Set the custom button label (default is _Buy Now_).
  - **Enable Modal Checkout:** Turn this **On** to open the checkout in a popup over the same page. Leave it **Off** to redirect customers to your normal checkout page.
- **Style Tab:** Style the background color, text color, typography, borders, and hover effects.
- **Advanced Tab:** Standard Elementor positioning and responsive controls.

![Screenshot of the Buy Now Button widget edit panel in Elementor](https://docs.fluentcart.com/images/customization-and-themes/fluentcart-elementor-widgets/widget-for-fluentcart/fluentcart-elementor-3.webp)

## 3\. Mini Cart [​](https://docs.fluentcart.com/guide/customization-and-themes/elementor-fluentcart-widgets\#_3-mini-cart)

A compact cart icon that usually sits in your site header. It lets customers see their cart count and total without leaving the current page.

- **Style Tab:** Almost all customization lives in **Cart Icon Style**.
  - **States:** Style **Normal** and **Hover** states separately.
  - **Typography & Colors:** Adjust the typography, text color, and icon color.
  - **Container Style:** Pick a **Background Type** (Classic or Gradient), choose a **Border Type**, set the **Border Radius** for rounded corners, and add a **Box Shadow**.
- **Advanced Tab:** Fine-tune padding and margin so the cart icon aligns perfectly with the rest of your header.

![Screenshot of the Mini Cart widget edit panel in Elementor showing Style controls](https://docs.fluentcart.com/images/customization-and-themes/fluentcart-elementor-widgets/widget-for-fluentcart/fluentcart-elementor-4.webp)

## 4\. Products [​](https://docs.fluentcart.com/guide/customization-and-themes/elementor-fluentcart-widgets\#_4-products)

The main widget for building shop pages. It renders your product catalog as a clean grid or list and supports filters, sorting, and pagination.

- **Content Tab:**Control which products show up and how they're arranged.
  - **General Settings:** Set **Products Per Page**, switch the **View Mode** between Grid and List, choose **Grid Columns**, and pick a **Pagination Type** (Infinite Scroll, Load More, or numbered pages). Choose the **Price Format**, sort with **Order By** and **Order**, and toggle **Use Default Style** for FluentCart's built-in styling.
  - **Shop Layout:** Adjust the spacing and layout of the product grid.
  - **Product Card Layout:** Choose which elements (image, title, price, button) appear inside each product card.
  - **Filter Settings:** Turn on a sidebar filter so customers can narrow the list by category, price, or attributes.
- **Style Tab:** Customize typography, card colors, button colors, and grid spacing.
- **Advanced Tab:** Standard Elementor margin, padding, and responsive controls.

![Screenshot of the Products widget edit panel in Elementor](https://docs.fluentcart.com/images/customization-and-themes/fluentcart-elementor-widgets/widget-for-fluentcart/fluentcart-elementor-5.webp)

## 5\. Product Card [​](https://docs.fluentcart.com/guide/customization-and-themes/elementor-fluentcart-widgets\#_5-product-card)

Renders a single product as a card - the same card layout used in the Products grid, but for a product you pick yourself. Great for highlighting a featured product anywhere on the page.

- **Content Tab:**Pick the product and shape the card.
  - **Select Product:** Choose the product this card represents.
  - **Price Format:** Pick how the price reads (for example, _Starts From_ for variable products).
  - **Card Layout:** Choose which elements appear on the card (image, title, price, button, etc.).
- **Style Tab:** Customize typography, colors, spacing, and the card's background and border.
- **Advanced Tab:** Standard Elementor controls.

![Screenshot of the Product Card widget edit panel in Elementor](https://docs.fluentcart.com/images/customization-and-themes/fluentcart-elementor-widgets/widget-for-fluentcart/fluentcart-elementor-6.webp)

## 6\. Product Carousel [​](https://docs.fluentcart.com/guide/customization-and-themes/elementor-fluentcart-widgets\#_6-product-carousel)

Use this on home pages or landing pages to show off a sliding row of products - perfect for "Best Sellers," "New Arrivals," or seasonal lineups.

- **Content Tab:**Configure which products show and how the slider behaves.
  - **Select Products:** Pick the products you want in the carousel.
  - **Carousel Settings:** Set how many slides show at once, turn on **Autoplay**, set the slide speed, enable **Infinite Loop**, and toggle navigation arrows or pagination dots.
  - **Card Layout:** Customize the look of each product card inside the carousel.
- **Style Tab:** Change the size and color of the arrows and pagination dots to match your theme.
- **Advanced Tab:** Add entrance animations or hide the carousel on specific devices.

![Screenshot of the Product Carousel widget edit panel in Elementor](https://docs.fluentcart.com/images/customization-and-themes/fluentcart-elementor-widgets/widget-for-fluentcart/fluentcart-elementor-7.webp)

## 7\. Product Categories List [​](https://docs.fluentcart.com/guide/customization-and-themes/elementor-fluentcart-widgets\#_7-product-categories-list)

Helps customers navigate your store by listing all of your product categories. Use it in sidebars, mega menus, or category landing pages.

- **Content Tab:**Set up the display.
  - **Display Style:** Choose between a vertical **List** or a space-saving **Dropdown**.
  - **Show Product Count:** Turn this on to display the number of products in each category.
  - **Show Hierarchy:** Turn this on to nest child categories under their parents.
  - **Show Empty Categories:** Turn this on to keep categories visible even when they have no products.
- **Style Tab:** Adjust spacing, link colors, hover states, and typography.
- **Advanced Tab:** Standard Elementor positioning controls.

![Screenshot of the Product Categories List widget edit panel in Elementor](https://docs.fluentcart.com/images/customization-and-themes/fluentcart-elementor-widgets/widget-for-fluentcart/fluentcart-elementor-8.webp)

## 8\. Checkout [​](https://docs.fluentcart.com/guide/customization-and-themes/elementor-fluentcart-widgets\#_8-checkout)

Place the FluentCart checkout form on any page. This gives you full control over the layout of your sales funnel - useful for one-page checkouts, dedicated landing pages, and custom upsell flows.

- **Content Tab:**Structure the form.
  - **General Settings:** Pick a **One Column** or **Two Column** layout, adjust **Form Column Width** and **Summary Column Width**, set the **Column Gap**, and toggle **Use Default FluentCart Styles** to apply the built-in look.
  - **Form Fields:** Customize each input section of the checkout - including the **EU VAT** section, which shows a VAT-ID input for B2B customers in EU countries.
  - **Order Summary:** Configure how the order totals, line items, and applied coupons appear.
  - **Layout Options:** Fine-tune the spacing and structure of the checkout container.
- **Style Tab:** Available when **Use Default FluentCart Styles** is set to **No**. Customize field colors, label typography, button styles, and the order summary box.
- **Advanced Tab:** Adjust width, spacing, and responsive behavior.

![Screenshot of the Checkout widget edit panel in Elementor](https://docs.fluentcart.com/images/customization-and-themes/fluentcart-elementor-widgets/widget-for-fluentcart/fluentcart-elementor-9.webp)

## 9\. Customer Dashboard Button [​](https://docs.fluentcart.com/guide/customization-and-themes/elementor-fluentcart-widgets\#_9-customer-dashboard-button)

A button that links to your customer's account dashboard. Drop it into your header, account area, or post-purchase pages so signed-in customers can jump to their orders in one click.

- **Content Tab:**Configure the button.
  - **Display Type:** Render as a **Button** or a plain **Link**.
  - **Label:** Set the visible text (for example, _My Account_).
  - **Show Icon:** Turn this on to display an icon next to the label.
  - **Open In:** Choose **Same Tab** or **New Tab** for the dashboard link target.
- **Style Tab:** Customize colors, typography, borders, and hover states.
- **Advanced Tab:** Standard Elementor positioning and responsive controls.

The dashboard page itself is configured under **FluentCart Pro → Settings → Pages Setup**.

![Screenshot of the Customer Dashboard Button widget edit panel in Elementor](https://docs.fluentcart.com/images/customization-and-themes/fluentcart-elementor-widgets/widget-for-fluentcart/fluentcart-elementor-10.webp)

## 10\. Product Search Bar [​](https://docs.fluentcart.com/guide/customization-and-themes/elementor-fluentcart-widgets\#_10-product-search-bar)

A search input that lets customers find products from anywhere on your site. Use it in headers, hero sections, or a dedicated search page.

- **Content Tab:**Set up the search behavior.
  - **Show Category Filter:** Turn this on to add an inline category dropdown next to the search input.
  - **Link Target:** Choose whether results open in the **Same Tab** or a **New Tab**.
  - **Link With Shop App:** Connect the bar to your configured Shop App page so results display in your store's layout.
- **Style Tab:** Style the input field, the category dropdown, the submit button, and the placeholder text.
- **Advanced Tab:** Standard Elementor controls.

![Screenshot of the Product Search Bar widget edit panel in Elementor](https://docs.fluentcart.com/images/customization-and-themes/fluentcart-elementor-widgets/widget-for-fluentcart/fluentcart-elementor-11.webp)

## 11\. Store Logo [​](https://docs.fluentcart.com/guide/customization-and-themes/elementor-fluentcart-widgets\#_11-store-logo)

Renders the store logo you configured in your FluentCart store settings. Drop it into headers, footers, or invoice templates so the logo updates everywhere when you change it.

- **Content Tab:**Configure the link.
  - **Link:** Choose where clicking the logo takes the visitor (Home Page or a custom URL).
  - **Open in New Tab:** Toggle on to open the link in a new browser tab.
- **Style Tab:** Adjust the logo size, max width, alignment, and border radius.
- **Advanced Tab:** Standard Elementor positioning controls.

To set or change the logo image itself, open your FluentCart store settings.

![Screenshot of the Store Logo widget edit panel in Elementor](https://docs.fluentcart.com/images/customization-and-themes/fluentcart-elementor-widgets/widget-for-fluentcart/fluentcart-elementor-12.webp)

## 12\. Product Info [​](https://docs.fluentcart.com/guide/customization-and-themes/elementor-fluentcart-widgets\#_12-product-info)

An all-in-one product summary widget. Instead of stacking a dozen smaller widgets, Product Info lets you compose the entire product summary block - title, price, stock, SKU, excerpt, package details, and buy section - inside a single widget with drag-and-drop reordering.

### Content Tab - Display [​](https://docs.fluentcart.com/guide/customization-and-themes/elementor-fluentcart-widgets\#content-tab-%E2%80%94-display)

- **Source:** Pull data from the **Current Product** (the product whose template you are editing) or a **Custom** product.

![Screenshot of the Product Info widget Content tab in Elementor](https://docs.fluentcart.com/images/customization-and-themes/fluentcart-elementor-widgets/widget-for-fluentcart/fluentcart-elementor-13.webp)

### Content Tab - Sections [​](https://docs.fluentcart.com/guide/customization-and-themes/elementor-fluentcart-widgets\#content-tab-%E2%80%94-sections)

Product Info groups its output into four section panels you can show or reorder independently:

- **Gallery:** Toggle **Show** to display the product gallery above the summary block.

- **Summary Sections:** A drag-and-drop repeater that controls the middle block. Reorder, show, or hide any of these rows:


  - **Title**
  - **Stock**
  - **SKU**
  - **Excerpt**
  - **Price**
  - **Package Description**
  - **Buy Section**

Drag the handle on each row to change its position. Click **Add Item** to insert a new row. The order in the editor matches the order on the rendered template.

- **Description:** Toggle **Show** to display the product's long-form description below the summary block.

- **Related Products:** Toggle **Show** to display a related-products row at the bottom.


![Screenshot of the Product Info widget Sections panel showing the drag-and-drop Summary Sections repeater](https://docs.fluentcart.com/images/customization-and-themes/fluentcart-elementor-widgets/widget-for-fluentcart/fluentcart-elementor-14.webp)

### Style Tab [​](https://docs.fluentcart.com/guide/customization-and-themes/elementor-fluentcart-widgets\#style-tab)

Each section has its own style panel - Title, Price, SKU, Excerpt, Description, Buy Section, and Gallery - so you can fine-tune typography, color, and spacing per row without touching the others.

### Advanced Tab [​](https://docs.fluentcart.com/guide/customization-and-themes/elementor-fluentcart-widgets\#advanced-tab)

Standard Elementor controls for margin, padding, and responsive visibility.

* * *

## What's Next [​](https://docs.fluentcart.com/guide/customization-and-themes/elementor-fluentcart-widgets\#what-s-next)

Looking for the single-product Theme Builder widgets? Head to [FluentCart Product Widgets for Elementor](https://docs.fluentcart.com/guide/customization-and-themes/elementor-product-widgets) for the 10 widgets that power your single-product templates.

Today

Hi! I’m your AI assistant. How can I assist you today?

Just now

Powered by **FluentBot**

---

## FluentCart Product Widgets for Elementor - FluentCart Documentation
URL : https://docs.fluentcart.com/guide/customization-and-themes/elementor-product-widgets

[Skip to content](https://docs.fluentcart.com/guide/customization-and-themes/elementor-product-widgets#VPContent)

# FluentCart Product Widgets for Elementor [​](https://docs.fluentcart.com/guide/customization-and-themes/elementor-product-widgets\#fluentcart-product-widgets-for-elementor)

The **FluentCart Product** category in the Elementor editor groups 10 focused widgets built for **Elementor Pro Theme Builder**. Use them inside single-product templates, archive templates, or theme parts - they automatically read the current product's data, so the same template works across your entire catalog.

INFO

Theme Builder widgets work best when **Source** is set to **Current Product** inside a Theme Builder template. Setting **Source** to **Custom** lets you preview a specific product while editing the template.

Before you can use these widgets, make sure the Elementor Blocks addon is turned on. See [Using Elementor Widgets](https://docs.fluentcart.com/guide/customization-and-themes/using-elementor-widgets) for the activation steps.

## 1\. Product Title [​](https://docs.fluentcart.com/guide/customization-and-themes/elementor-product-widgets\#_1-product-title)

Renders the title of the current product. Use it as the H1 on your single-product template.

- **Content Tab:**Configure the source and tag.
  - **Source:** Pull from the **Current Product** or a **Custom** product.
  - **HTML Tag:** Pick the tag - typically **H1** for single-product pages, or **H2** / **H3** when used inside cards or summary blocks.
  - **Alignment:** Align the title left, center, right, or justified.
- **Style Tab:** Customize typography, color, and text shadow.
- **Advanced Tab:** Standard Elementor controls.

![Screenshot of the Product Title widget edit panel in Elementor](https://docs.fluentcart.com/images/customization-and-themes/fluentcart-elementor-widgets/product-widgets/fluentcart-elementor-2.webp)

## 2\. Product Gallery [​](https://docs.fluentcart.com/guide/customization-and-themes/elementor-product-widgets\#_2-product-gallery)

Renders the product's image gallery with the main image plus thumbnails. Use it on single-product templates to put the gallery exactly where you want it.

- **Content Tab:**Configure the gallery layout.
  - **Source:** Pull from the **Current Product** or a **Custom** product.
  - **Thumbnail Position:** Place the thumbnail strip at the **Bottom**, **Top**, **Left**, or **Right** of the main image.
  - **Thumbnail Mode:** Show **All** thumbnails or limit them with **Max Thumbnails**.
  - **Scrollable Thumbnails:** Turn this on to enable scrolling when the thumbnails exceed the gallery's dimensions.
  - **Max Thumbnails:** Cap the visible thumbnails - extra images become accessible behind a **See More** button.
- **Advanced Tab:** Standard Elementor controls.

![Screenshot of the Product Gallery widget edit panel in Elementor](https://docs.fluentcart.com/images/customization-and-themes/fluentcart-elementor-widgets/product-widgets/fluentcart-elementor-3.webp)

## 3\. Product Price [​](https://docs.fluentcart.com/guide/customization-and-themes/elementor-product-widgets\#_3-product-price)

Displays the current product's price. For variable products, it shows the price range - and updates automatically when a customer picks a variation.

- **Content Tab:**Configure the price source.
  - **Source:** Pull from the **Current Product** or a **Custom** product.
  - **Select Product:** When **Source** is **Custom**, pick the product whose price you want to display.
  - **Alignment:** Align the price left, center, or right.
- **Style Tab:** Customize typography, regular-price color, sale-price color, and spacing.
- **Advanced Tab:** Standard Elementor controls.

![Screenshot of the Product Price widget edit panel in Elementor](https://docs.fluentcart.com/images/customization-and-themes/fluentcart-elementor-widgets/product-widgets/fluentcart-elementor-4.webp)

## 4\. Product Stock [​](https://docs.fluentcart.com/guide/customization-and-themes/elementor-product-widgets\#_4-product-stock)

Shows the current product's stock status - **In Stock**, **Out of Stock**, or a custom availability label.

- **Content Tab:**Configure the source.
  - **Source:** Pull from the **Current Product** or a **Custom** product.
  - **Select Product:** When **Source** is **Custom**, pick the product to display.
- **Style Tab:** Customize the label typography and the color used for each stock state.
- **Advanced Tab:** Standard Elementor controls.

![Screenshot of the Product Stock widget edit panel in Elementor](https://docs.fluentcart.com/images/customization-and-themes/fluentcart-elementor-widgets/product-widgets/fluentcart-elementor-5.webp)

## 5\. Product SKU [​](https://docs.fluentcart.com/guide/customization-and-themes/elementor-product-widgets\#_5-product-sku)

Displays the SKU (Stock Keeping Unit) of the current product. For variable products, the SKU updates when a customer selects a variation.

- **Content Tab:**Configure the label and source.
  - **Source:** Pull from the **Current Product** or a **Custom** product.
  - **Show Label:** Turn this on to prepend a label before the SKU value.
  - **Custom Label:** Set the literal label string (default is `SKU:`).
- **Style Tab:** Customize label typography, value typography, and color - independently.
- **Advanced Tab:** Standard Elementor controls.

![Screenshot of the Product SKU widget edit panel in Elementor](https://docs.fluentcart.com/images/customization-and-themes/fluentcart-elementor-widgets/product-widgets/fluentcart-elementor-6.webp)

## 6\. Product Package Description [​](https://docs.fluentcart.com/guide/customization-and-themes/elementor-product-widgets\#_6-product-package-description)

Surfaces the product's package metadata - package name, dimensions, product weight, and shipping weight - in a clean table on the template.

- **Content Tab:**Choose which rows to show.
  - **Source:** Pull from the **Current Product** or a **Custom** product.
  - **Show Package Name:** Toggle the package-label row.
  - **Show Dimensions:** Toggle the `L × W × H` row.
  - **Show Product Weight:** Toggle the product's own weight row.
  - **Show Shipping Weight:** Toggle the combined product + package weight row.
- **Style Tab:** Customize row spacing, label typography, value typography, and divider colors.
- **Advanced Tab:** Standard Elementor controls.

The data comes from the package assigned in the product's [Pricing & Shipping settings](https://docs.fluentcart.com/guide/product-types-creation/configuring-product-pricing).

![Screenshot of the Product Package Description widget edit panel in Elementor](https://docs.fluentcart.com/images/customization-and-themes/fluentcart-elementor-widgets/product-widgets/fluentcart-elementor-7.webp)

## 7\. Product Excerpt [​](https://docs.fluentcart.com/guide/customization-and-themes/elementor-product-widgets\#_7-product-excerpt)

Renders the product's short description (excerpt). Use it on single-product templates above the buy section, or on archive templates as a quick teaser.

- **Content Tab:**Configure the source.
  - **Source:** Pull from the **Current Product** or a **Custom** product.
  - **Alignment:** Align the excerpt left, center, right, or justified.
- **Style Tab:** Customize typography, color, and spacing.
- **Advanced Tab:** Standard Elementor controls.

![Screenshot of the Product Excerpt widget edit panel in Elementor](https://docs.fluentcart.com/images/customization-and-themes/fluentcart-elementor-widgets/product-widgets/fluentcart-elementor-8.webp)

## 8\. Product Buy Section [​](https://docs.fluentcart.com/guide/customization-and-themes/elementor-product-widgets\#_8-product-buy-section)

The full purchase block - variation selector, price, quantity field, **Buy Now** button, and **Add to Cart** button - rendered as a single widget. Drop it onto your single-product template to give customers everything they need to check out.

- **Content Tab:**Configure the source.
  - **Source:** Pull from the **Current Product** or a **Custom** product.
  - **Select Product:** When **Source** is **Custom**, pick the product to preview.
- **Style Tab:** Customize the variation chips, price display, quantity input, and both action buttons - each has its own typography, color, and spacing controls.
- **Advanced Tab:** Standard Elementor controls.

![Screenshot of the Product Buy Section widget edit panel in Elementor](https://docs.fluentcart.com/images/customization-and-themes/fluentcart-elementor-widgets/product-widgets/fluentcart-elementor-9.webp)

## 9\. Product Content [​](https://docs.fluentcart.com/guide/customization-and-themes/elementor-product-widgets\#_9-product-content)

Renders the long-form product content - the rich-text body of the product. Use it on single-product templates to place the full description anywhere you want, instead of relying on the theme's default placement.

- **Content Tab:**Configure the source.
  - **Source:** Pull from the **Current Product** or a **Custom** product.
  - **Select Product:** When **Source** is **Custom**, pick the product to preview.
  - **Alignment:** Align the content block left, center, right, or justified.
- **Style Tab:** Customize typography, link colors, and spacing.
- **Advanced Tab:** Standard Elementor controls.

![Screenshot of the Product Content widget edit panel in Elementor](https://docs.fluentcart.com/images/customization-and-themes/fluentcart-elementor-widgets/product-widgets/fluentcart-elementor-10.webp)

## 10\. Related Products [​](https://docs.fluentcart.com/guide/customization-and-themes/elementor-product-widgets\#_10-related-products)

Renders a row of products related to the current product. FluentCart picks the related items based on shared categories and tags, plus any manual relations you set in the product editor.

- **Content Tab:**Configure the query.
  - **Source:** Pull from the **Current Product** or a **Custom** product.
  - **Select Product:** When **Source** is **Custom**, pick the product whose related items you want to preview.
- **Style Tab:** Customize the card spacing, typography, button styles, and image aspect ratio.
- **Advanced Tab:** Standard Elementor controls.

![Screenshot of the Related Products widget edit panel in Elementor](https://docs.fluentcart.com/images/customization-and-themes/fluentcart-elementor-widgets/product-widgets/fluentcart-elementor-11.webp)

* * *

## What's Next [​](https://docs.fluentcart.com/guide/customization-and-themes/elementor-product-widgets\#what-s-next)

Looking for the store-wide widgets (cart, checkout, search bar, store logo, etc.)? Head to [FluentCart Widgets for Elementor](https://docs.fluentcart.com/guide/customization-and-themes/elementor-fluentcart-widgets).

---

## FluentCart Shortcodes - FluentCart Documentation
URL : https://docs.fluentcart.com/guide/customization-and-themes/fluentcart-shortcode

[Skip to content](https://docs.fluentcart.com/guide/customization-and-themes/fluentcart-shortcode#VPContent)

# FluentCart Shortcodes [​](https://docs.fluentcart.com/guide/customization-and-themes/fluentcart-shortcode\#fluentcart-shortcodes)

Shortcodes are like "magic codes" that allow you to display your store's products, buttons, and pages anywhere on your WordPress site. Whether you are using a blog post, a custom landing page, or a sidebar, FluentCart shortcodes give you the flexibility to build your shop exactly how you want it.

### 1\. The Product Catalog Shortcode (`[fluent_cart_products]`) [​](https://docs.fluentcart.com/guide/customization-and-themes/fluentcart-shortcode\#_1-the-product-catalog-shortcode-fluent-cart-products)

The `[fluent_cart_products]` shortcode is the easiest way to show a grid of products. It's perfect for your main shop page, a "Featured Products" section on your homepage, or a specific category gallery.

#### Basic Usage [​](https://docs.fluentcart.com/guide/customization-and-themes/fluentcart-shortcode\#basic-usage)

To show your standard product list with default settings, simply use:

text

```
[fluent_cart_products]
```

#### Filtering by Product IDs [​](https://docs.fluentcart.com/guide/customization-and-themes/fluentcart-shortcode\#filtering-by-product-ids)

You can show specific products by passing one or more product IDs. This is useful when you want to highlight a handpicked selection of items on a landing page or a promotional section.

text

```
// Show a single product
[fluent_cart_products ids="433"]

// Show multiple products
[fluent_cart_products ids="344,346,347"]
```

To hide certain products from the list, use the `exclude_ids` parameter:

text

```
// Exclude a single product
[fluent_cart_products exclude_ids="344"]

// Exclude multiple products
[fluent_cart_products exclude_ids="3595,3493"]
```

> **Note:** If you pass an ID that does not exist (e.g., `ids="999999"`), no products will be displayed.

#### Filtering by Category [​](https://docs.fluentcart.com/guide/customization-and-themes/fluentcart-shortcode\#filtering-by-category)

You can narrow the product list down to one or more categories. Categories can be referenced by their **slug** or their **term ID** - whichever is more convenient.

text

```
// Filter by a single category slug
[fluent_cart_products category="cloths"]

// Filter by multiple category slugs
[fluent_cart_products category="cloths,shoes"]

// Filter by a single category term ID
[fluent_cart_products category_id="9"]

// Filter by multiple category term IDs
[fluent_cart_products category_id="9,12"]

// Combine a slug and an ID together
[fluent_cart_products category="hoodies" category_id="8"]
```

Category filters also work seamlessly with pagination. For example, the following shortcode shows two products per page with numbered pagination, and the category filter persists when your visitors navigate between pages:

text

```
[fluent_cart_products category="hoodies" per_page="2" paginator="numbers"]
```

> **Note:** If you pass a category slug that does not exist (e.g., `category="nonexistent-category-xyz"`), the filter is ignored and all products are shown.

#### Filtering by Product Type & Sale Status [​](https://docs.fluentcart.com/guide/customization-and-themes/fluentcart-shortcode\#filtering-by-product-type-sale-status)

Use the `product_type` parameter to display only a specific type of product, or use `on_sale` to showcase discounted items.

text

```
// Simple products only
[fluent_cart_products product_type="simple"]

// Variation products only
[fluent_cart_products product_type="simple_variations"]

// Physical products only
[fluent_cart_products product_type="physical"]

// Digital products only
[fluent_cart_products product_type="digital"]

// Subscription products only
[fluent_cart_products product_type="subscription"]

// Only products currently on sale
[fluent_cart_products on_sale="yes"]
```

> **Tip:** Empty parameter values (e.g., `ids=""`, `category=""`, `product_type=""`) are safely ignored, so you don't have to worry about accidental blank values breaking your page.

#### Sorting Products [​](https://docs.fluentcart.com/guide/customization-and-themes/fluentcart-shortcode\#sorting-products)

Control the order in which products appear using the `sort_by` parameter for common presets, or the `orderby` and `order` parameters for more granular control.

text

```
// Sort by price, ascending (using orderby + order)
[fluent_cart_products orderby="price" order="ASC"]

// Price low to high
[fluent_cart_products sort_by="price-low"]

// Price high to low
[fluent_cart_products sort_by="price-high"]

// Alphabetical A–Z
[fluent_cart_products sort_by="name-asc"]

// Newest first
[fluent_cart_products sort_by="date-newest"]

// Oldest first
[fluent_cart_products sort_by="date-oldest"]
```

#### Layout & Display [​](https://docs.fluentcart.com/guide/customization-and-themes/fluentcart-shortcode\#layout-display)

Adjust the number of columns and the view mode to match the look and feel of your page.

text

```
// Show products in a 3-column grid
[fluent_cart_products columns="3"]

// Limit to 6 products in a 3-column grid
[fluent_cart_products limit="6" columns="3"]

// 2-column grid view
[fluent_cart_products columns="2" view_mode="grid"]

// List view with 4 products per page and numbered pagination
[fluent_cart_products per_page="4" view_mode="list" paginator="numbers"]
```

#### Combining Parameters [​](https://docs.fluentcart.com/guide/customization-and-themes/fluentcart-shortcode\#combining-parameters)

The real power of the shortcode comes from mixing and matching parameters. Here are a few practical combinations:

text

```
// Paginate through specific products, one per page
[fluent_cart_products ids="433,434" per_page="1" paginator="numbers"]

// Specific products in a custom 3-column layout
[fluent_cart_products ids="433,434,435" columns="3" per_page="3"]

// Category products, exclude one, newest first
[fluent_cart_products category="hoodies" exclude_ids="433" sort_by="date-newest"]

// Digital products in 3 columns, sorted by price, 6 per page
[fluent_cart_products product_type="digital" columns="3" sort_by="price-low" per_page="6"]
```

#### Advanced Usage (Filters & Sidebar) [​](https://docs.fluentcart.com/guide/customization-and-themes/fluentcart-shortcode\#advanced-usage-filters-sidebar)

You can also enable a sidebar filter and configure it with JSON-based settings. Here is a version that shows 4 products with a sidebar filter:

text

```
[fluent_cart_products\
    per_page=4\
    live_filter='false'\
    enable_filter='true'\
    paginator='numbers'\
    custom_filters='{"enabled":true,"live_filter":true,"taxonomies":"product-categories,product-brands","price_range":"price_range"}'\
    filters='{"enabled":true,"sort_by":"name-desc"}'\
]
```

#### Parameter Reference [​](https://docs.fluentcart.com/guide/customization-and-themes/fluentcart-shortcode\#parameter-reference)

| Parameter | Description | Default | Options |
| --- | --- | --- | --- |
| **ids** | Show only the products matching these IDs. Accepts a single ID or a comma-separated list. | - | Any valid product ID(s) (e.g., `433` or `344,346,347`) |
| **exclude\_ids** | Hide specific products from the list. Accepts a single ID or a comma-separated list. | - | Any valid product ID(s) (e.g., `344` or `3595,3493`) |
| **category** | Filter products by one or more category slugs. | - | Comma-separated slugs (e.g., `cloths` or `cloths,shoes`) |
| **category\_id** | Filter products by one or more category term IDs. | - | Comma-separated IDs (e.g., `9` or `9,12`) |
| **product\_type** | Show only products of a specific type. | - | `simple`, `simple_variations`, `physical`, `digital`, `subscription` |
| **on\_sale** | Show only products that are currently discounted. | - | `yes` |
| **sort\_by** | A quick preset for sorting products. | - | `price-low`, `price-high`, `name-asc`, `date-newest`, `date-oldest` |
| **orderby** | The field to sort products by (use with `order`). | - | `price`, `name`, `date` |
| **order** | Sort direction (use with `orderby`). | - | `ASC`, `DESC` |
| **columns** | Number of columns in the product grid. | - | Any number (e.g., `2`, `3`, `4`) |
| **limit** | Maximum number of products to display. | - | Any number (e.g., `6`, `10`) |
| **view\_mode** | Choose between a grid layout or a list layout. | `grid` | `grid`, `list` |
| **per\_page** | How many products to show on one page. | 12 | Any number (e.g., 4, 8, 20) |
| **paginator** | The style of the page navigation at the bottom. | `numbers` | `numbers`, `load_more`, `scroll`, `none` |
| **enable\_filter** | Show or hide the filter sidebar on the left/right. | `true` | `true`, `false` |
| **live\_filter** | If "true," products update instantly as you click filters. | `true` | `true`, `false` |
| **custom\_filters** | A list of settings to control category and price filters. | - | See JSON guide below |
| **filters** | Settings for how products are sorted (Name, Price, etc.). | - | See JSON guide below |

#### A Quick Look at Filter Settings (JSON) [​](https://docs.fluentcart.com/guide/customization-and-themes/fluentcart-shortcode\#a-quick-look-at-filter-settings-json)

**`custom_filters` object:**

- **enabled:** Set to `true` to show your custom category/brand filters.
- **live\_filter:** Set to `true` for instant, "no-reload" updates.
- **taxonomies:** Tell the plugin what to show (e.g., `"product-categories,product-brands"`).
- **price\_range:** Include a price slider by adding `"price_range"`.

**`filters` object:**

- **sort\_by:** Choose how products appear first. Options include: `name-asc`, `name-desc`, `price-asc`, `price-desc`, or `date-desc`.

* * *

### 2\. Checkout Button Shortcode (`[fluent_cart_checkout_button]`) [​](https://docs.fluentcart.com/guide/customization-and-themes/fluentcart-shortcode\#_2-checkout-button-shortcode-fluent-cart-checkout-button)

This shortcode creates a button that sends customers straight to the checkout page or opens a quick "Buy Now" popup. It is perfect for landing pages and promotions where you want to make buying as fast as possible.

#### Basic Usage [​](https://docs.fluentcart.com/guide/customization-and-themes/fluentcart-shortcode\#basic-usage-1)

text

```
[fluent_cart_checkout_button variation_id="113" instant_checkout="yes"]
```

#### Supported Attributes [​](https://docs.fluentcart.com/guide/customization-and-themes/fluentcart-shortcode\#supported-attributes)

| Attribute | Description |
| --- | --- |
| **button\_text** | Changes what the button says. Example: `button_text="Get it Now"`. (If left empty, it usually says "Checkout".) |
| **variation\_id** | **(Very Important)** The ID of the specific item or size/color you want to sell. You must use the specific variation ID found in your product settings. |
| **target** | Decides where the link opens. Use `_self` for the same tab or `_blank` to open the checkout in a new window. |
| **instant\_checkout** | If set to `yes`, the checkout will open in a popup modal. If set to `no`, it works like a normal link to the checkout page. |

#### Example Variations [​](https://docs.fluentcart.com/guide/customization-and-themes/fluentcart-shortcode\#example-variations)

- **Standard Link to Checkout:**`[fluent_cart_checkout_button button_text="Go to Checkout" target="_self"]`
- **One-Click "Instant" Purchase:**`[fluent_cart_checkout_button variation_id="113" instant_checkout="yes" button_text="Buy Now"]`

* * *

### 3\. Add to Cart Button Shortcode (`[fluent_cart_add_to_cart_button]`) [​](https://docs.fluentcart.com/guide/customization-and-themes/fluentcart-shortcode\#_3-add-to-cart-button-shortcode-fluent-cart-add-to-cart-button)

This shortcode puts a simple "Add to Cart" button anywhere you want. Use this if you want customers to stay on the page and keep shopping after they click.

#### Basic Usage [​](https://docs.fluentcart.com/guide/customization-and-themes/fluentcart-shortcode\#basic-usage-2)

text

```
[fluent_cart_add_to_cart_button button_text="Add to Cart" variation_id="113"]
```

#### Supported Attributes [​](https://docs.fluentcart.com/guide/customization-and-themes/fluentcart-shortcode\#supported-attributes-1)

| Attribute | Description |
| --- | --- |
| **button\_text** | The text displayed on the button (e.g., "Add to Bag", "Grab One"). |
| **variation\_id** | The ID of the product or specific option you want added to the cart. |

* * *

### 4\. Mini Cart Shortcode (`[fluent_cart_mini_cart]`) [​](https://docs.fluentcart.com/guide/customization-and-themes/fluentcart-shortcode\#_4-mini-cart-shortcode-fluent-cart-mini-cart)

The Mini Cart shortcode allows you to display a small, convenient cart summary. It is perfect for headers or sidebars, letting customers see how many items they have and the total price at a glance.

#### Basic Usage [​](https://docs.fluentcart.com/guide/customization-and-themes/fluentcart-shortcode\#basic-usage-3)

text

```
[fluent_cart_mini_cart cart_icon="bag" show_total_price="true"]
```

#### Supported Attributes [​](https://docs.fluentcart.com/guide/customization-and-themes/fluentcart-shortcode\#supported-attributes-2)

| Attribute | Description |
| --- | --- |
| **cart\_icon** | Choose the style of your icon. Options: `cart`, `bag`, `bag-alt`. You can also use a custom SVG URL: `cart_icon="https://example.com/icon.svg"`. |
| **show\_total\_price** | Set to `true` to show the current total amount next to the icon. |
| **show\_item\_count** | Decides when to show the number of items: `always` (shows even if 0), `has_items` (only when cart has items), `never` (hides count). |
| **icon\_color** / **price\_color** / **product\_count\_color** | Use hex codes to match your site's branding (e.g., `icon_color="#cf2e2e"`). |
| **button\_class** | Add a custom CSS class if you want to apply your own specific styling to the cart button. |

* * *

### 5\. Product Categories Shortcode (`[fluent_cart_product_categories]`) [​](https://docs.fluentcart.com/guide/customization-and-themes/fluentcart-shortcode\#_5-product-categories-shortcode-fluent-cart-product-categories)

This shortcode helps your customers browse your store by showing a list or a dropdown of your product categories.

#### Basic Usage [​](https://docs.fluentcart.com/guide/customization-and-themes/fluentcart-shortcode\#basic-usage-4)

text

```
[fluent_cart_product_categories display_style="list" show_hierarchy="true"]
```

#### Supported Attributes [​](https://docs.fluentcart.com/guide/customization-and-themes/fluentcart-shortcode\#supported-attributes-3)

| Attribute | Description |
| --- | --- |
| **display\_style** | Choose how the categories are presented: `list` (standard bulleted list) or `dropdown` (space-saving dropdown menu). |
| **show\_hierarchy** | Set to `true` to show "parent" and "child" categories (indented). |
| **show\_empty** | Set to `true` if you want to show categories even if they don't have any products yet. |
| **show\_product\_count** | Set to `true` to show the number of products next to each category name. |

### 6\. Store Logo Shortcode (`[fluent_cart_store_logo]`) [​](https://docs.fluentcart.com/guide/customization-and-themes/fluentcart-shortcode\#_6-store-logo-shortcode-fluent-cart-store-logo)

Use this shortcode to display your store's branding logo anywhere on your site. It allows you to set a custom link and control the size of the image easily.

#### Basic Usage [​](https://docs.fluentcart.com/guide/customization-and-themes/fluentcart-shortcode\#basic-usage-5)

text

```
[fluent_cart_store_logo is_link="true" logo_url="https://yoursite.com/logo.png" max_width="200"]
```

#### Supported Attributes [​](https://docs.fluentcart.com/guide/customization-and-themes/fluentcart-shortcode\#supported-attributes-4)

| Attribute | Description |
| --- | --- |
| **logo\_url** | (Required) The direct URL link to your logo image file. |
| **is\_link** | Set to `true` to make the logo clickable (usually linking to your homepage). Set to `false` for a static image. |
| **link\_target** | Choose `_self` to open in the same tab, or `_blank` to open the link in a new tab. |
| **max\_width** | Sets the maximum width of the logo in pixels (e.g., `"300"`). |
| **max\_height** | Sets the maximum height of the logo in pixels (e.g., `"200"`). |

* * *

### 7\. Customer Dashboard Button (`[fluent_cart_customer_dashboard_button]`) [​](https://docs.fluentcart.com/guide/customization-and-themes/fluentcart-shortcode\#_7-customer-dashboard-button-fluent-cart-customer-dashboard-button)

This shortcode adds a button or link that allows logged-in customers to access their "My Profile" or "My Orders" area. It is perfect for your site's header or footer menu.

#### Basic Usage [​](https://docs.fluentcart.com/guide/customization-and-themes/fluentcart-shortcode\#basic-usage-6)

text

```
[fluent_cart_customer_dashboard_button button_text="My Profile" display_type="link"]
```

#### Supported Attributes [​](https://docs.fluentcart.com/guide/customization-and-themes/fluentcart-shortcode\#supported-attributes-5)

| Attribute | Description |
| --- | --- |
| **button\_text** | The text displayed on the link or button (e.g., "My Account", "Profile"). |
| **display\_type** | Choose how it looks: `link` (simple text link) or `button` (styled button). |
| **show\_icon** | Set to `true` to display a small user icon next to the text, or `false` to hide it. |
| **link\_target** | Choose `_self` (same tab) or `_blank` (new tab). |

* * *

### 8\. Product Title Shortcode (`[fluent_cart_product_title]`) [​](https://docs.fluentcart.com/guide/customization-and-themes/fluentcart-shortcode\#_8-product-title-shortcode-fluent-cart-product-title)

This shortcode allows you to display the name of a specific product anywhere on your page. This is extremely useful when building custom landing pages where you want to place the product name separately from the image or description.

#### Basic Usage [​](https://docs.fluentcart.com/guide/customization-and-themes/fluentcart-shortcode\#basic-usage-7)

text

```
[fluent_cart_product_title product_id="123" is_link="true"]
```

#### Supported Attributes [​](https://docs.fluentcart.com/guide/customization-and-themes/fluentcart-shortcode\#supported-attributes-6)

| Attribute | Description |
| --- | --- |
| **product\_id** | (Required) The ID of the specific product you want to display the title for. |
| **is\_link** | Set to `true` to make the title clickable (links to the product page). |
| **link\_target** | Choose `_self` (same tab) or `_blank` (new tab). |
| **is\_default** | Set to `true` to use default styling, or `false` to inherit the surrounding text style. |

* * *

### 9\. Product Image Shortcode (`[fluent_cart_product_image]`) [​](https://docs.fluentcart.com/guide/customization-and-themes/fluentcart-shortcode\#_9-product-image-shortcode-fluent-cart-product-image)

Similar to the Product Title shortcode, this lets you display the featured image of a specific product. You can use this to create custom layouts by placing the image in one column and the details in another.

#### Basic Usage [​](https://docs.fluentcart.com/guide/customization-and-themes/fluentcart-shortcode\#basic-usage-8)

text

```
[fluent_cart_product_image product_id="123"]
```

#### Supported Attributes [​](https://docs.fluentcart.com/guide/customization-and-themes/fluentcart-shortcode\#supported-attributes-7)

| Attribute | Description |
| --- | --- |
| **product\_id** | (Required) The ID of the specific product you want to display the image for. |
| **is\_default** | Set to `false` to allow for custom sizing or styling via CSS, or `true` for standard output. |

* * *

### How to Implement [​](https://docs.fluentcart.com/guide/customization-and-themes/fluentcart-shortcode\#how-to-implement)

1. **Copy the code:** Select the shortcode configuration that fits your needs.
2. **Paste into WordPress:** Open any Page or Post in the Block Editor.
3. **Use a Shortcode Block:** Add a **Shortcode** block and paste the code.
4. **Publish:** Update your page to see your custom product grid in action.

> **Tip:** Use the `per_page` attribute to create small "Featured Products" sections on your homepage by setting it to a low number like 3 or 4.

Today

Hi! I’m your AI assistant. How can I assist you today?

Just now

Powered by **FluentBot**

---

## Layout and Template Customization (Block Editor) - FluentCart Documentation
URL : https://docs.fluentcart.com/guide/customization-and-themes/layout-template-customization

[Skip to content](https://docs.fluentcart.com/guide/customization-and-themes/layout-template-customization#VPContent)

# Layout and Template Customization (Block Editor) [​](https://docs.fluentcart.com/guide/customization-and-themes/layout-template-customization\#layout-and-template-customization-block-editor)

FluentCart allows for deep customization of your store's design. Whether you are using the native WordPress Block Editor, a Block Theme, or a third-party page builder, you have flexible tools to control exactly how your products appear.

## Advanced Layout Control: A Practical Example [​](https://docs.fluentcart.com/guide/customization-and-themes/layout-template-customization\#advanced-layout-control-a-practical-example)

The Products block is not just a static grid-it's a flexible container with smaller, nested blocks inside it. This allows you to completely change the layout of your product listings without any code.

### Example: Moving the Price Above the Image [​](https://docs.fluentcart.com/guide/customization-and-themes/layout-template-customization\#example-moving-the-price-above-the-image)

Let's say you want to create a unique look for your shop by displaying the price before the product image.

1. Add the Products block to your page.
2. Select the block, and in the toolbar at the top of the editor, click the **List View** icon.
3. In the **List View** panel, expand the Products block to see its nested structure. You will find blocks like **Product Image**, **Product Title**, and **Product Price**.
4. Simply click and drag the **Product Price** block and move it above the **Product Image** block.

Just like that, you have changed the layout for every product in the grid. You can reorder, remove, or customize any of the inner blocks to create the perfect design for your store.

![Screenshot of List View](https://docs.fluentcart.com/images/customization-and-themes/using-fluentcart-blocks/list-view.webp)

## Customizing Core Layouts with Templates (for Block Themes) [​](https://docs.fluentcart.com/guide/customization-and-themes/layout-template-customization\#customizing-core-layouts-with-templates-for-block-themes)

If you are using a modern, block-based WordPress theme, you can edit FluentCart's core templates directly. This gives you control over the fundamental design of your product and archive pages.

### Accessing FluentCart Templates [​](https://docs.fluentcart.com/guide/customization-and-themes/layout-template-customization\#accessing-fluentcart-templates)

1. From your WordPress dashboard, go to **Appearance** \> **Editor**.
2. In the Site Editor, select **Templates**.
3. Look for the FluentCart templates.

- **Single Product:** This template controls the design of your individual product pages. Edit this to change the layout of the product title, image, description, and price for all products at once.
- **Products by Category:** This template controls the design of your category pages (the pages that list all products in a category).

![Screenshot of FluentCart Templates](https://docs.fluentcart.com/images/customization-and-themes/using-fluentcart-blocks/fluentcart-templates.webp)

## Integrating with Page Builders Bricks [​](https://docs.fluentcart.com/guide/customization-and-themes/layout-template-customization\#integrating-with-page-builders-bricks)

FluentCart's blocks are also fully compatible with popular page builder Bricks. This allows you to seamlessly integrate FluentCart's e-commerce power with the advanced design capabilities of Bricks. You can use the FluentCart templates directly within the Bricks editor just as you would in the standard WordPress editor, giving you the best of both worlds.

For other builders that may not have direct block support, FluentCart also provides shortcodes as a flexible way to add product grids and buttons to any design.

TIP

You can always return later to make changes. The Block Editor is flexible, so feel free to experiment without worrying about messing up your layout.

### Save Your Changes [​](https://docs.fluentcart.com/guide/customization-and-themes/layout-template-customization\#save-your-changes)

When you’re done making changes, click the **Save** button at the top right. Your customized template will now be live on your site.

Today

Hi! I’m your AI assistant. How can I assist you today?

Just now

Powered by **FluentBot**

---

## Theme & Page Builder Compatibility - FluentCart Documentation
URL : https://docs.fluentcart.com/guide/customization-and-themes/theme-compatibility

[Skip to content](https://docs.fluentcart.com/guide/customization-and-themes/theme-compatibility#VPContent)

# Theme & Page Builder Compatibility [​](https://docs.fluentcart.com/guide/customization-and-themes/theme-compatibility\#theme-page-builder-compatibility)

FluentCart is designed to be lightweight, flexible, and compatible with the vast majority of modern, well-coded WordPress themes and page builders. Our goal is to give you the freedom to choose the design and tools that you love, without being locked into a specific look.

Because FluentCart leverages native WordPress features like blocks and shortcodes, it integrates seamlessly into most environments.

## Officially Compatible Themes & Page Builders [​](https://docs.fluentcart.com/guide/customization-and-themes/theme-compatibility\#officially-compatible-themes-page-builders)

While FluentCart should work well with almost any standard theme, we have officially tested and confirmed full compatibility with the following popular themes and page builders:

#### Popular Page Builders & Frameworks: [​](https://docs.fluentcart.com/guide/customization-and-themes/theme-compatibility\#popular-page-builders-frameworks)

- Bricks
- Gutenberg

#### Popular Modern & Block-Based Themes: [​](https://docs.fluentcart.com/guide/customization-and-themes/theme-compatibility\#popular-modern-block-based-themes)

- Divi
- Kadence
- Astra
- GeneratePress
- Blocksy
- Twenty Twenty-Five (and other default WordPress themes)
- Storefront
- OceanWP
- Hello Elementor
- FSE Block Theme

### What If My Theme Isn't on the List? [​](https://docs.fluentcart.com/guide/customization-and-themes/theme-compatibility\#what-if-my-theme-isn-t-on-the-list)

If your theme is not on this list, it is still very likely to be compatible with FluentCart, especially if it follows standard WordPress development practices.

FluentCart is built to be as theme-agnostic as possible. For any theme, you can use our powerful [**FluentCart Blocks**](https://docs.fluentcart.com/guide/customization-and-themes/using-gutenberg-blocks) in the WordPress editor or place our [**shortcodes**](https://docs.fluentcart.com/guide/settings-configuration/pages-setup) to display products, checkout forms, and customer dashboards. This ensures that you can build a fully functional and beautiful storefront, no matter which theme you choose.

Today

Hi! I’m your AI assistant. How can I assist you today?

Just now

Powered by **FluentBot**

---

## Translating FluentCart - FluentCart Documentation
URL : https://docs.fluentcart.com/guide/customization-and-themes/translating-fluentcart

[Skip to content](https://docs.fluentcart.com/guide/customization-and-themes/translating-fluentcart#VPContent)

# Translating FluentCart [​](https://docs.fluentcart.com/guide/customization-and-themes/translating-fluentcart\#translating-fluentcart)

Making your store available in different languages helps you connect with a wider, global audience and provide a better shopping experience for your customers.

FluentCart is fully translatable, so you can change the button, label, and message to fit your needs. In this guide, we'll use the popular Loco Translate plugin to get this done.

### Step 1. Install the Loco Translate Plugin [​](https://docs.fluentcart.com/guide/customization-and-themes/translating-fluentcart\#step-1-install-the-loco-translate-plugin)

First, you'll need to install the tool that will help you translate the plugin text.

1. Go to **Plugins → Add New** from your WordPress dashboard.
2. In the search bar, type "Loco Translate".
3. Find the plugin in the search results and click **Install Now**.
4. Once it's installed, click the **Activate** button.

![Activating the Loco Translate plugin from the WordPress plugins page.](https://docs.fluentcart.com/assets/loco-translate-activate.mKKBs23g.webp)

### Step 2. Translate FluentCart and FluentCart Pro [​](https://docs.fluentcart.com/guide/customization-and-themes/translating-fluentcart\#step-2-translate-fluentcart-and-fluentcart-pro)

Now you are ready to start translating. It's important to translate both the free **FluentCart** plugin and the **FluentCart Pro** add-on for a complete translation.

1. Navigate to the new **Loco Translate** menu in your dashboard sidebar and click on **Plugins**.

2. You will see a list of all your installed plugins. Click on **FluentCart** to begin. (You will repeat these steps for **FluentCart Pro** later.)

![The Loco Translate plugins list](https://docs.fluentcart.com/assets/loco-translate-fluentcart.DgQcjJvu.webp)

3. Click the **\+ New language** link to add your translation file.

![Clicking the 'New language' link in Loco Translate.](https://docs.fluentcart.com/assets/new-language.DZkZoE1X.webp)

4. On the next screen, you will need to configure your new language file.

   - **Choose a language:** Choose the language that matches your WordPress General Settings language.
   - **Choose a location:** Next, you need to decide where to save your translation files. You will see a few options.

INFO

We highly recommend choosing the " **Custom**" location. Files saved here are protected from being overwritten when you update the FluentCart plugin. If you choose the "Author" location, your custom translations could be lost during an update.

5. Click the **Start translating** button.

![Select Language Location](https://docs.fluentcart.com/assets/select-language-location.Ddf2QsRi.webp)

6. You will now be on the editor screen. Here you'll see a list of all the English text ("Source text") from the plugin.

   - Click on any English string from the list.
   - In the box below (e.g., "Spanish translation"), type your translation.
   - Click the **Save** button in the top left.
   - Repeat this process for all the text you wish to translate.
7. Once you have finished translating the free version, go back to **Loco Translate → Plugins** and repeat the same steps for **FluentCart Pro** to ensure all features are translated.

![Clicking the Save button](https://docs.fluentcart.com/assets/save-button.BCGkDylx.webp)


### Step 3. Set Your WordPress Site Language [​](https://docs.fluentcart.com/guide/customization-and-themes/translating-fluentcart\#step-3-set-your-wordpress-site-language)

For your translations to appear, you must tell WordPress which language your website should use.

1. From your WordPress dashboard, navigate to **Settings → General**.
2. Find the **Site Language** dropdown menu.
3. Select your desired language from the list.
4. Scroll to the bottom of the page and click the **Save Changes** button.

![Setting the Site Language in WordPress General Settings](https://docs.fluentcart.com/assets/general-settings.Cvt0rrtN.webp)

### Previewing Your Translations [​](https://docs.fluentcart.com/guide/customization-and-themes/translating-fluentcart\#previewing-your-translations)

After you save a translation, you can instantly see the changes on your site. There’s no need to log out or refresh anything except the page you’re viewing.

For example, let’s say you translated the helper text for the **Store Name** field as shown below.

Now, go to **FluentCart Pro → Settings → Store Setup**. You’ll notice that the text under the Store Name field now appears in your translated language. You can use this same method to preview any string you translate.

![Viewing the successfully translated helper text in the FluentCart Store Setup settings.](https://docs.fluentcart.com/assets/previewing-translation.B348Tg47.webp)

### Keeping Your Translations Up-to-Date [​](https://docs.fluentcart.com/guide/customization-and-themes/translating-fluentcart\#keeping-your-translations-up-to-date)

When FluentCart is updated, new text strings might be added. To find and translate these new strings, simply open your language file in Loco Translate and click the **Sync** button. This will automatically add any new text to your list so you can translate it.

### Troubleshooting Common Issues [​](https://docs.fluentcart.com/guide/customization-and-themes/translating-fluentcart\#troubleshooting-common-issues)

If your translations aren't behaving as expected, here are a few common issues and their solutions.

- **My translations are not showing up.**

  - **Check Site Language:** Make sure the language you are translating into in Loco Translate is the _exact same_ language you have set as the **Site Language** under **WordPress → Settings → General**.
  - **Check File Location:** Ensure you saved your translation file in the **Custom** location (`languages/loco/plugins/`). If you saved it in the "Author" or "System" location, it may be overwritten or not loaded properly.
  - **Clear Your Cache:** Your browser or a caching plugin might be showing an older, untranslated version of your site. Clear all caches and reload the page.
- **Some text is still in English (e.g., on the Checkout page).** This often happens with text that is saved to the database, like the names of payment methods or shipping options. If you set these up when your site was in English, they won't automatically change when you switch the site's language. To fix this, you must translate these items manually in the FluentCart settings where you created them.

- **Untranslatable Characters and Placeholders** You may see strings that contain special characters or codes like `%s`, `&`, or numbers. These are often dynamic placeholders that the system replaces with a value, like a name, a number, or a date. **Do not translate these placeholders.** Instead, include them in your translated sentence. For example, a source text of `Auto renews on %s` should be translated around the placeholder, like `Se renueva automáticamente el %s`.


Today

Hi! I’m your AI assistant. How can I assist you today?

Just now

Powered by **FluentBot**

---

## Using Elementor Widgets - FluentCart Documentation
URL : https://docs.fluentcart.com/guide/customization-and-themes/using-elementor-widgets

[Skip to content](https://docs.fluentcart.com/guide/customization-and-themes/using-elementor-widgets#VPContent)

# Using Elementor Widgets [​](https://docs.fluentcart.com/guide/customization-and-themes/using-elementor-widgets\#using-elementor-widgets)

Making a successful online store needs two things: a great look and the right tools. If you use Elementor to build your website, FluentCart gives you a set of built-in widgets that fit perfectly with your designs.

With these widgets, you can drag and drop product lists, checkout forms, single-product layouts, search bars, and more anywhere on your site - without writing any code.

## Turn on the Elementor Widgets [​](https://docs.fluentcart.com/guide/customization-and-themes/using-elementor-widgets\#turn-on-the-elementor-widgets)

FluentCart starts with only the basics to keep your site fast. To use the Elementor widgets, you need to turn them on first.

1. **Go to Settings:** In your WordPress dashboard, go to **FluentCart → Settings**.
2. **Open Features & Addons:** Click the **Features & addon** tab on the left.
3. **Find Plugin Addons:** Scroll to the bottom of the page to find the **Plugin Addons** section.
4. **Turn it On:** Find the **Elementor Blocks** card and click **Install & Activate**.

![Screenshot of the FluentCart widget category panel in the Elementor editor](https://docs.fluentcart.com/images/customization-and-themes/fluentcart-elementor-widgets/elementor-widget-1.webp)

Once activated, two new categories appear inside the Elementor editor: **FluentCart** for store-wide widgets and **FluentCart Product** for single-product Theme Builder widgets.

## How to Find Your Widgets in the Editor [​](https://docs.fluentcart.com/guide/customization-and-themes/using-elementor-widgets\#how-to-find-your-widgets-in-the-editor)

When you open any page or template in Elementor:

1. Open the **Elements panel** (click the grid icon in the top-left corner).
2. Type **FluentCart** in the search bar, or scroll the panel until you find the FluentCart categories.

![Screenshot of the FluentCart widget category panel in the Elementor editor](https://docs.fluentcart.com/images/customization-and-themes/fluentcart-elementor-widgets/widget-for-fluentcart/fluentcart-elementor-1.webp)

FluentCart groups its Elementor widgets into two categories so you always know where to look:

- **FluentCart** - store-wide widgets you can drop on any page: product grids, carousels, mini cart, checkout, search bar, store logo, and the all-in-one Product Info block.
- **FluentCart Product** - focused widgets for single-product templates inside Elementor Pro's Theme Builder: title, gallery, price, stock, SKU, package description, excerpt, content, buy section, and related products.

## Pick the Widget Group You Need [​](https://docs.fluentcart.com/guide/customization-and-themes/using-elementor-widgets\#pick-the-widget-group-you-need)

Jump straight to the group you want to learn about:

- [FluentCart Widgets for Elementor](https://docs.fluentcart.com/guide/customization-and-themes/elementor-fluentcart-widgets) - the 12 store-wide widgets you can use on any page.
- [FluentCart Product Widgets for Elementor](https://docs.fluentcart.com/guide/customization-and-themes/elementor-product-widgets) - the 10 Theme Builder widgets for single-product templates.

Today

Hi! I’m your AI assistant. How can I assist you today?

Just now

Powered by **FluentBot**

---

## Using Gutenberg Blocks - FluentCart Documentation
URL : https://docs.fluentcart.com/guide/customization-and-themes/using-gutenberg-blocks

[Skip to content](https://docs.fluentcart.com/guide/customization-and-themes/using-gutenberg-blocks#VPContent)

# Using Gutenberg Blocks [​](https://docs.fluentcart.com/guide/customization-and-themes/using-gutenberg-blocks\#using-gutenberg-blocks)

FluentCart provides a powerful set of dedicated blocks for the WordPress block editor (Gutenberg), allowing you to build and customize your e-commerce pages with ease. Instead of being limited to predefined layouts, you can use these blocks to create a fully custom shop page, display specific products, and add e-commerce functionalities anywhere on your site.

This guide will walk you through the different methods you can use to design your shop, product, and checkout pages.

## Building with FluentCart Blocks [​](https://docs.fluentcart.com/guide/customization-and-themes/using-gutenberg-blocks\#building-with-fluentcart-blocks)

The easiest and most flexible way to build your store is with FluentCart's dedicated blocks. These act like building bricks, allowing you to add e-commerce features to any page or post in the WordPress editor.

### Accessing FluentCart Blocks [​](https://docs.fluentcart.com/guide/customization-and-themes/using-gutenberg-blocks\#accessing-fluentcart-blocks)

1. From your WordPress dashboard, open any **page** or **post**.
2. Click the **plus icon (+)** to open the block inserter.
3. Scroll down to find the **FluentCart** and **FluentCart Buttons** categories, or simply search for the block you need.

You will see all the blocks listed below. Here is a fast look at all the FluentCart tools you can use in Gutenberg:

- Products
- Product Title
- Product Description
- Product Search
- Product Carousel
- Customer Dashboard
- Product Card
- Product Image
- Sale Badge
- Product Info
- Price Range
- Mini Cart
- Buy Now Button
- Add to Cart Button
- Buy Section
- Checkout
- Product Categories List
- Excerpt
- Product Package Description

### 1\. Products [​](https://docs.fluentcart.com/guide/customization-and-themes/using-gutenberg-blocks\#_1-products)

This is the main tool for building your shop pages using the WordPress block editor. It displays your inventory in a professional grid layout.

- **Paginator:** Choose your pagination style, such as Scroll (for infinite loading) or Numbers (for standard pages). You can also use the slider to set how many products show up per page.
- **Product Grid Options:** Set the View Mode to Grid and pick a Price Format, such as "Starts From" for products with multiple prices. You can also adjust the Product Per Row to decide how many items sit side-by-side.
- **Filter Option:** You can toggle Enable Filter to let customers sort products easily. You can also turn on Default Filter to manage the starting order of your items.
- **Additional CSS Class(es):** Enter custom code here if you want to add unique styling to the product block.

![Screenshot of FluentCart Blocks](https://docs.fluentcart.com/images/customization-and-themes/using-fluentcart-blocks/accessing-fluentcart-blocks.webp)

### 2\. Product Title [​](https://docs.fluentcart.com/guide/customization-and-themes/using-gutenberg-blocks\#_2-product-title)

This block displays the name of your product, pulling data automatically to keep your page accurate. It is a standalone tool, allowing you to place and style the title independently in your custom designs. Here you control how your product name behaves in the editor.

- **Settings:** Toggle Make title a link if you want customers to be able to click the product name to visit its specific page. You can also enable Open in new tab so customers don't lose the page they are currently browsing.
- **Typography & Alignment:** Use the block toolbar or sidebar to change the text alignment, adjust the font size, and pick a color that matches your brand.
- **Additional CSS Class(es):** Enter custom code here if you want to add unique styling or specific font effects to the product title.

### 3\. Product Description [​](https://docs.fluentcart.com/guide/customization-and-themes/using-gutenberg-blocks\#_3-product-description)

This block is used to display the full, detailed description of your product, providing customers with all the information they need to make a purchase. It pulls data directly from your product settings to ensure your site stays up to date automatically.

**Product Settings:** Use the settings tab (gear icon) to choose which product's details to show.

- **Select Product:** Click this button to search your inventory and pick the specific item whose full description you want to feature on the page.

**Style Tab:** Click the style tab (half-moon icon) to customize the visual look of your text.

- **Color:** You have granular control to set individual colors for the Text, the Background of the description area, and any Links included in the content.
- **Typography:** Adjust the Font Size (from Small to Extra Large) and Line Height to make sure your product details are easy for customers to read.
- **Dimensions:** Use the Padding and Margin sliders to perfectly space the description within your page layout.
- **Border & Shadow:** Add specialized borders or shadow effects to the description container to make the information pop.

**Additional CSS Class(es):** Enter custom code here if you want to add unique styling or specialized formatting to the product description block.

![Screenshot of FluentCart Blocks](https://docs.fluentcart.com/images/customization-and-themes/using-fluentcart-blocks/product-description.webp)

### 4\. Product Search [​](https://docs.fluentcart.com/guide/customization-and-themes/using-gutenberg-blocks\#_4-product-search)

The Product Search block helps customers quickly find specific items in your store. Instead of browsing through many products, users can simply type what they’re looking for and get instant results.

You can add this block from the editor by selecting the magnifying glass icon under the FluentCart section.

**Block Settings:** When you click on the search bar in your editor, the right-hand sidebar gives you several options to control how the search behaves:

- **Searchbar Behavior:** Choose whether search results open in a New Tab or the Current Tab.

- **Category Filtering:** Enable this option to allow customers to filter their search by product categories.

- **Link With Shop App:** Turn this on to connect the search bar with your Shop App settings for a more integrated experience.

- **Advanced Settings:** Standard block options for layout and design customization.

- **Additional CSS Class(es):** Add custom CSS classes if you want to modify the search bar’s style, such as colors, borders, or width.

![Screenshot of FluentCart Blocks](https://docs.fluentcart.com/images/customization-and-themes/using-fluentcart-blocks/product-search.webp)


### 5\. Product Carousel [​](https://docs.fluentcart.com/guide/customization-and-themes/using-gutenberg-blocks\#_5-product-carousel)

The Product Carousel block is a dynamic tool for highlighting your best-selling or newest items in an interactive, sliding row. It is perfect for homepages or landing pages where you want to showcase multiple products in a limited space without overwhelming your shoppers.

- **Product Selection:** Click the Select Product button to search for and pick the specific items you want to feature. You can easily manage your choices under the Selected products list.

- **Layout:** Use the Slides per view slider to decide exactly how many products sit side-by-side on the screen at one time (for example, setting it to 4).

- **Behavior:** This section gives you full control over the movement. You can toggle Autoplay for automatic sliding, enable an Infinite loop for continuous scrolling, and choose to Show arrows or Show Pagination (using styles like Fraction or Dots) to help customers navigate through your items.

- **Additional CSS Class(es):** Enter custom code here if you want to add unique styling, like specialized borders or shadow effects, to the carousel container.


> **Tip:** Use the Product Carousel block at the top of your homepage to highlight your best-selling items with high-quality imagery to grab attention immediately.

![Screenshot of FluentCart Blocks](https://docs.fluentcart.com/images/customization-and-themes/using-fluentcart-blocks/product-carousel.webp)

### 6\. Customer Dashboard [​](https://docs.fluentcart.com/guide/customization-and-themes/using-gutenberg-blocks\#_6-customer-dashboard)

This block is the "home base" for your customers. It acts as a personalized portal where they can manage every part of their relationship with your store, from viewing past orders to updating their own addresses.

**Settings:** Here you can place the dashboard on any page to give your users instant access to their account.

**Layout:** In the editor, you will see the dashboard organized with a clean sidebar menu that helps customers navigate between different sections like their Purchase History, Licenses, and Downloads.

> **Setup Tip:** For this block to work correctly, you must ensure you have assigned the Customer Dashboard page under **FluentCart Pro > Settings > Pages Setup**.

**Key Sections Your Customers Will See:**

- **Purchase History:** A complete list of all past orders including unique identifiers like #INV-6, the date of purchase, and the current status (such as "Completed" or "Processing").

- **Subscription Plans:** A dedicated area where customers can view their active or canceled recurring plans and check upcoming renewal dates.

- **Managing Licenses:** Perfect for digital products, this section lets users see their license keys and how many sites they are currently using them on.

- **Downloads:** A central place for customers to find every digital file they have bought, such as e-books or software updates.

- **Profile & Address Settings:** This allows shoppers to keep their contact information and shipping addresses up-to-date without needing to contact your support team.

- **Additional CSS Class(es):** Use this section to add custom code if you want to change the colors or spacing of the dashboard to match your theme perfectly.


![Screenshot of FluentCart Blocks](https://docs.fluentcart.com/images/customization-and-themes/using-fluentcart-blocks/customer-dashboard.webp)

### 7\. Product Card [​](https://docs.fluentcart.com/guide/customization-and-themes/using-gutenberg-blocks\#_7-product-card)

If you want to highlight one specific item on a special page-like a "Deal of the Day"-the Product Card block is the perfect tool. It puts a single product into a beautiful, standalone card that includes the featured image, price, and an "Add to Cart" button all in one neat package.

You can find this block in the FluentCart section of your editor, represented by a small card icon.

**Block Settings:** Here you can control exactly which product shows up and how the card is sized.

- **Product Selection:** Use the Product dropdown to search for and pick the specific item you want to feature.

- **Query type:** This determines how the block pulls information; leaving it on Default is usually best for a single card.

- **Price Format:** You can set the price to show as "Starts From," which is very helpful if the product has different versions with different prices.

- **Card Sizing:** You can fully control the size by choosing Custom Width and using the slider to make the card wider or narrower to fit your layout (e.g., setting it to 216 pixels).

- **Additional CSS Class(es):** Enter custom code here if you want to add unique styling, like special shadows or borders, to your product card.


![Screenshot of FluentCart Blocks](https://docs.fluentcart.com/images/customization-and-themes/using-fluentcart-blocks/product-card.webp)

### 8\. Product Image [​](https://docs.fluentcart.com/guide/customization-and-themes/using-gutenberg-blocks\#_8-product-image)

This block allows you to showcase the visual identity of your products anywhere on your site. It renders the featured image of a specific product, making it an essential tool for building custom landing pages or highlighted product sections.

**Settings:** Here you can control which product visual appears in the block.

- **Query type:** Choose how the block identifies which image to display, such as using a Custom selection to pick a specific item.

- **Select Product:** Click this button to open a search and select the exact product whose image you want to feature.

- **Product Title:** This area displays the name of the product you have currently selected (e.g., "Perfume") so you can easily verify you've picked the right one.

- **Additional CSS Class(es):** Enter custom code here if you want to add unique styling, like custom borders, shadows, or hover effects to your product image.


![Screenshot of FluentCart Blocks](https://docs.fluentcart.com/images/customization-and-themes/using-fluentcart-blocks/product-image.webp)

### 9\. Sale Badge [​](https://docs.fluentcart.com/guide/customization-and-themes/using-gutenberg-blocks\#_9-sale-badge)

The Sale Badge block is a must-have for any store looking to boost conversions by highlighting special deals. It automatically displays a label or a discount percentage over your items whenever they are on sale, making it easy for customers to spot a bargain at a glance.

**Badge Settings:** Use the settings tab (gear icon) to control how your promotional labels behave.

- **Badge Text:** Type in your own custom message like "Sale!", "Hot Deal", or "Clearance" to display when you aren't using percentages.
- **Show Discount Percentage:** Toggle this on to let the block do the math for you, showing customers exactly how much they save (e.g., -20%).
- **Percentage Format:** If you use percentages, you can customize their appearance using the {percent} placeholder.
- **Price Source:** Define which price the block should check to determine if a sale is active, such as the Default Variant.
- **Position & Style:** Choose your preferred Badge Style and set the Position to place the badge exactly where you want it on the product image, such as the Top Left.

**Style Settings:** Switch to the style tab (half-moon icon) to make your badges pop.

- **Color:** Manually set the Text and Background colors to match your theme or use a bright color like red to grab attention.

- **Typography:** Adjust the Font Size (ranging from Small to Extra Large) and Line Height for perfect readability.

- **Dimensions:** Use the Padding and Margin sliders to adjust the badge's size and its distance from the product card's edge.

- **Border & Shadow:** Add specialized borders or shadow effects to give your badges a professional, 3D look.

- **Additional CSS Class(es):** Enter custom code here if you want to add unique styling, like custom shapes or pulsing animations, to your sale badges.

![Screenshot of FluentCart Blocks](https://docs.fluentcart.com/images/customization-and-themes/using-fluentcart-blocks/sale-badge.webp)


### 10\. Sold Out Badge [​](https://docs.fluentcart.com/guide/customization-and-themes/using-gutenberg-blocks\#_10-sold-out-badge)

This block displays a clear visual alert on products that are currently out of stock, helping you manage customer expectations at a glance. It automatically triggers based on your real-time inventory levels, ensuring shoppers always know which items are unavailable before they try to purchase.

**Settings:** Here you control the primary behavior and placement of the badge.

- **Badge Text:** Customize the message displayed when an item is unavailable, such as "Sold Out" or "Out of Stock".
- **Position & Style:** Adjust the placement of the badge on your product image (e.g., Top Left) and choose a visual style that stands out clearly against your product photos.

**Additional CSS Class(es):** Enter custom code here if you want to apply unique styling, such as custom colors or specialized font effects, to the sold-out label.

![Screenshot of FluentCart Blocks](https://docs.fluentcart.com/images/customization-and-themes/using-fluentcart-blocks/sold-out-badge.webp)

### 11\. Product Info [​](https://docs.fluentcart.com/guide/customization-and-themes/using-gutenberg-blocks\#_11-product-info)

This block is used to display essential details about your product-such as the title, description, and price-in a clean and organized way. It acts as a central hub for pulling product data directly into your custom layouts or landing pages.

Here you control which product's information the block displays.

- **Query type:** This setting allows you to choose how the block identifies the product. Setting it to **Default** will automatically pull data from the product page it is placed on, while choosing **Custom** allows you to manually search for and select a specific item from your catalog.

- **Select Product:** If you choose a custom query, you can use the selection button in the editor to pick the exact product you want to showcase.

- **Additional CSS Class(es):** Enter custom code here if you want to add unique styling, such as custom borders or specific text colors, to the product information container.


![Screenshot of FluentCart Blocks](https://docs.fluentcart.com/images/customization-and-themes/using-fluentcart-blocks/product-info.webp)

### 12\. Price Range [​](https://docs.fluentcart.com/guide/customization-and-themes/using-gutenberg-blocks\#_12-price-range)

This block is designed to showcase the cost of your products with automatic currency formatting. It is especially useful for variable products, as it can dynamically display the full price range (e.g., $5.00 - $8.00) to give customers a clear idea of the cost options.

- **Query type:** This setting determines which product's price is displayed. Using the **Default** setting will automatically pull the price from the product page it is placed on, while choosing **Custom** allows you to manually select a specific product from your inventory.

- **Additional CSS Class(es):** Enter custom code here if you want to add unique styling, such as specific font weights, colors, or spacing, to the price display.


### 13\. Mini Cart [​](https://docs.fluentcart.com/guide/customization-and-themes/using-gutenberg-blocks\#_13-mini-cart)

This block is a compact cart widget designed to let shoppers quickly view their cart items. It allows customers to see their item count and total price at a glance without needing to leave the page they are currently browsing.

**Block Settings:** Here you control the icon style and what information is displayed to the user.

- **Cart Icon:** Choose from three default shopping icons or provide a Custom Icon URL (SVG) to match your store’s unique branding.
- **Display Options:** Toggle the Display total price switch to show or hide the current value of the cart next to the icon.
- **Show Cart Item Count:** Define when the item counter bubble appears. You can set it to display Always, Only if cart has items, or Never.
- **Style Settings:**Switch to the style tab (half-moon icon) to customize the visual look.
  - **Color:** You have granular control to set individual colors for the Icon, the Price, and the Product Count.
  - **Typography:** Adjust the Font Size (Small to Extra Large) and Line Height to ensure the text fits perfectly with your header's design.
  - **Dimensions:** Use the Padding and Margin sliders to adjust the spacing around the mini cart for perfect alignment.

**Advanced:** Standard block settings to help with your custom page design.

- **Additional CSS Class(es):** Enter custom code here if you want to add unique styling, such as specialized hover animations or custom border effects.

![Screenshot of FluentCart Blocks](https://docs.fluentcart.com/images/customization-and-themes/using-fluentcart-blocks/minicart-8.webp)

### 14\. Buy Now Button [​](https://docs.fluentcart.com/guide/customization-and-themes/using-gutenberg-blocks\#_14-buy-now-button)

The Buy Now button is a powerful shortcut designed for landing pages to trigger an immediate purchase action. Instead of sending customers through the standard cart process, this block can be configured to take them directly to checkout or open a payment window on the same page.

**Product Settings:** Here you control the behavior and target of the button.

- **Enable Instant Modal Checkout:** Toggle this on to open the checkout form in a popup modal instead of navigating the customer to a different page.

- **Product Selection:** You can search for and select a specific product variation (e.g., "Teal Green") that this button will automatically assign to the customer's order.

- **Style Settings:** Switch to the style tab (half-moon icon) to customize the button's appearance.

  - **Color:** You have full control over the Text and Background colors of the button.
  - **Typography:** Adjust the Font Size (from Small to Extra Large) and Line Height to ensure your call-to-action is clear and readable.
  - **Dimensions:** Use the Padding and Margin sliders to adjust the size of the button and its spacing within your layout.
- **Additional CSS Class(es):** Enter custom code here if you want to add unique styling, such as custom hover animations or specialized border effects.


![Screenshot of FluentCart Blocks](https://docs.fluentcart.com/images/customization-and-themes/using-fluentcart-blocks/buy-now-8.webp)

### 15\. Add to Cart Button [​](https://docs.fluentcart.com/guide/customization-and-themes/using-gutenberg-blocks\#_15-add-to-cart-button)

The Add to Cart button is a standalone tool that allows customers to add a specific product or variation to their cart while remaining on the same page. This is ideal for custom landing pages where you want to encourage multi-item shopping.

**Settings:** Use the settings tab (gear icon) to define which item the button targets.

- **Product Selection:** Click the Select Product button to search for and assign a specific product variation to this button.

- **Style Settings:** Switch to the style tab (half-moon icon) to customize the button's appearance.

  - **Color:** You can manually set the Text and Background colors to match your brand's palette.
  - **Typography:** Control the Font Size (ranging from Small to Extra Large) and Line Height to ensure your call-to-action is prominent.
  - **Dimensions:** Use the Padding and Margin sliders to adjust the button's internal spacing and its external position within your design.
  - **Border & Shadow:** Add depth to your button by configuring border styles or shadow effects.
- **Additional CSS Class(es):** Enter custom code here if you want to apply unique CSS styling, such as custom hover states or specialized animations.


![Screenshot of FluentCart Blocks](https://docs.fluentcart.com/images/customization-and-themes/using-fluentcart-blocks/add-to-cart-9.webp)

### 16\. Buy Section [​](https://docs.fluentcart.com/guide/customization-and-themes/using-gutenberg-blocks\#_16-buy-section)

This block acts as the functional hub of your product page. It brings together all the essential purchase elements-like price, quantity, and action buttons-into one convenient area for your customers.

**Settings:** You can control how the block identifies which product to display.

- **Query type:** Set this to **Default** to automatically pull details from the current product page, or choose **Custom** to manually select a specific item from your inventory.

- **Included Elements:** The block automatically renders the product price, a Quantity selector (with plus and minus buttons), and both Buy Now and Add To Cart buttons to provide a complete shopping experience.

- **Additional CSS Class(es):** Enter custom code here if you want to apply unique styling or specialized layout adjustments to the entire buy section container.


![Screenshot of FluentCart Blocks](https://docs.fluentcart.com/images/customization-and-themes/using-fluentcart-blocks/buy-section-10.webp)

### 17\. Checkout Page [​](https://docs.fluentcart.com/guide/customization-and-themes/using-gutenberg-blocks\#_17-checkout-page)

This is the essential block that renders the secure checkout form for completing purchases. It provides a comprehensive, professional layout where customers enter their details and review their items before finalizing their order.

- **Customer Information:** Includes standard fields for Name and Email, plus a toggle for customers to **Create an Account?** while they check out.

- **Address Sections:** Provides organized areas for Billing Address and Shipping Address, complete with fields for street names, apartment details, and phone numbers.

- **Order Summary Sidebar:** Displays a clear breakdown of the purchase, including product variations, subtotals, shipping costs, and tax estimates.

- **Coupons & Terms:** Features a **Have a Coupon?** section for applying manual discounts and a checkbox at the bottom for customers to agree to your terms and conditions.

- **Additional CSS Class(es):** Enter custom code here if you want to apply unique styling to the checkout form, such as custom borders or specific background colors for the form fields.


![Screenshot of FluentCart Blocks](https://docs.fluentcart.com/images/customization-and-themes/using-fluentcart-blocks/checkout-page-11.webp)

### 18\. Product Categories List [​](https://docs.fluentcart.com/guide/customization-and-themes/using-gutenberg-blocks\#_18-product-categories-list)

The Product Categories List block helps your customers navigate your store by displaying an organized directory of your different product departments. This is a great way to improve your site's browsing experience and help shoppers find related items quickly.

**Block Settings:** Use the settings tab (gear icon) to configure how the list is structured.

- **Display Style:** Choose between a standard **List** format or a space-saving **Dropdown** menu.

- **Show product count:** Toggle this on to display the number of available products next to each category name (e.g., "Menswear (10)").

- **Show hierarchy:** When enabled, this will display child categories nested underneath their respective parent categories for better organization.

- **Show empty categories:** You can choose whether to hide or display categories that do not currently contain any products.

- **Style Settings:** Switch to the style tab (half-moon icon) to customize the visual appearance of the list.

  - **Color:** You have separate controls to set the color for the Text and the clickable Links.
  - **Typography:** Adjust the Font Size (ranging from Small to Extra Large) and the Line Height to ensure the list matches your website's design.
- **Additional CSS Class(es):** Enter custom code here if you want to add unique styling, such as custom bullet points or specialized hover effects for the category links.


![Screenshot of FluentCart Blocks](https://docs.fluentcart.com/images/customization-and-themes/using-fluentcart-blocks/product-category-list-12.webp)

### 19\. Excerpt [​](https://docs.fluentcart.com/guide/customization-and-themes/using-gutenberg-blocks\#_19-excerpt)

The Excerpt block is designed to display a brief summary or snippet of your product's description. It is an ideal tool for building custom shop layouts or landing pages where you want to provide a quick preview of an item without including the full description text.

Here, you can easily control the data source for the snippet.

- **Product Selection:** Use the Product dropdown in the settings panel to search for and pick the specific item whose summary you want to feature.

- **Style Tab:** Here you change the visual look to match your website's design.

  - **Color:** You have granular control to set individual colors for both the Text and the Background.
  - **Typography:** Adjust the Font Size (ranging from Small to Extra Large) and the Line Height to ensure the text snippet is clear and readable.
  - **Dimensions:** Use the Margin slider to adjust the external spacing around the excerpt for perfect placement within your layout.
- **Additional CSS Class(es):** Enter custom code here if you want to apply unique styling, such as specific font weights or text effects, to the product excerpt.


![Screenshot of FluentCart Blocks](https://docs.fluentcart.com/images/customization-and-themes/using-fluentcart-blocks/excerpt.webp)

### 20\. Product Package Description [​](https://docs.fluentcart.com/guide/customization-and-themes/using-gutenberg-blocks\#_20-product-package-description)

The **Product Package Description** block surfaces the physical details of a product - package name, dimensions, product weight, and total shipping weight - directly on the product page in a clean, theme-aware table. It reads from the package you assigned in the product's [Pricing & Shipping settings](https://docs.fluentcart.com/guide/product-types-creation/configuring-product-pricing#adding-a-new-package), so there is no duplicate data to maintain.

For stores selling furniture, books, appliances, food, or anything where size and weight meaningfully influence a buying decision, this block turns hidden shipping metadata into information customers can see _before_ they check out.

![Screenshot of the Product Package Description block on a single product page showing Package, Dimensions, Weight, and Shipping Weight rows next to variant selectors](https://docs.fluentcart.com/images/customization-and-themes/using-fluentcart-blocks/product-package-description.webp)

**Inspector Settings:** Use the settings tab (gear icon) to control what the table displays.

- **Show Package Name:** Toggle the package label row (e.g., "Gift box"). Turn off if customers only care about dimensions and weight.
- **Show Dimensions:** Toggle the `L × W × H` row. Hides automatically if the selected package has no dimensions configured.
- **Show Product Weight:** Toggle the product's own weight (excluding the package).
- **Show Shipping Weight (Total):** Toggle the combined product + package weight. This value mirrors what FluentCart uses for shipping rate calculation, so the number on the product page matches the number used at checkout.

**Variant-Aware Switching**

When the product has variations (different sizes, colors, or configurations) and each variant ships in a different package, the block rebuilds its table instantly the moment a shopper selects a different variant - no page reload, no flicker. Each variant's package, dimensions, and weight render from data embedded in the variant buttons, so the information shoppers see is always tied to the exact version they are about to buy.

**Block Theme (FSE) Support**

The block ships inside FluentCart's default single-product template, so any block theme (Twenty Twenty-Four, Twenty Twenty-Five, or custom FSE themes) picks it up automatically on product pages. You can still remove it from the template via **Appearance > Editor** if you prefer not to expose package information for a particular store.

**Styling**

The table uses CSS variables (border, text, and background) inherited from your theme, so it adapts to light and dark modes without additional CSS. For custom tweaks, add an **Additional CSS Class** and target the `[data-fluent-cart-package-description]` wrapper.

**Where Else Package Information Appears**

Once you configure the package data, the same information flows through the customer's journey without further configuration:

- **Checkout order summary** - package name and shipping weight appear under each cart line, so shoppers confirm shipping details before they pay.

![Screenshot of the checkout order summary showing Gift box and shipping weight under an order line](https://docs.fluentcart.com/images/customization-and-themes/using-fluentcart-blocks/package-description-checkout.webp)

- **Order confirmation emails** - the default email body and customized templates can both display package details. See [Configuring Email Notifications](https://docs.fluentcart.com/guide/settings-configuration/email-configuration/configuring-email-notification) for the merge tags.


> **Note:** Each FluentCart block comes with its own customization settings. After adding a block, check the settings panel on the right to adjust design, alignment, behavior, and visibility.

---
