---
source_url: https://surecart.com/docs/all-shortcodes
source: surecart-kb
scraped: true
---

# SureCart List Of All Shortcodes

## What is a Shortcode?

A shortcode is a simple and abbreviated code enclosed in square brackets. Shortcodes allow you to add dynamic content to posts, pages, or widgets without writing complex code.

## How to Use Shortcodes

1. Copy the desired shortcode
2. Add any parameters you want (optional)
3. Paste it into your post, page, or widget content
4. Save and view the front end to see the result

**Important Note:** The ID parameter does not work in SureCart version 3 and above due to the WordPress Interactivity API requirement.

## Available Shortcodes

### Shop Page

**sc_product_list** — Display products in a grid format

Parameters: columns, limit, pagination_enabled, ajax_pagination, pagination_auto_scroll, type, search_enabled, sort_enabled, ids, collection_enabled

### Product Page Shortcodes

**sc_product_title** — Display product title (requires id parameter)

**sc_product_description** — Display product description (requires id parameter)

**sc_product_price** — Display currently selected price (supports id and sale_text parameters)

**sc_product_variant_choices** — Display variant options (requires id parameter)

**sc_product_price_choices** — Show pricing options (supports id, label, columns, show_price)

**sc_product_media** — Display product images/slideshow (supports id, auto_height, height, width, thumbnails_per_page)

**sc_product_quantity** — Show quantity selector (supports id, label)

**sc_product_cart_button** — Add to cart or buy now button (supports id, text, add_to_cart)

### Checkout Forms

**sc_form** — Display checkout form (requires id parameter). Example: id=123

### Cart Menu Icon

**sc_cart_menu_icon** — Display cart icon (supports cart_icon, cart_menu_always_shown)

### Customer Dashboard

**sc_customer_dashboard_button** — Add dashboard button (supports label parameter)

**sc_customer_dashboard_page** — Wrapper for all dashboard components

**sc_customer_orders** — Show orders section (supports title parameter)

**sc_customer_subscriptions** — Show subscriptions section (supports title parameter)

**sc_customer_downloads** — Show downloads section (supports title parameter)

**sc_customer_payment_methods** — Show payment methods section (supports title parameter)

**sc_customer_billing_details** — Show billing details section (supports title parameter)

**sc_customer_wordpress_account** — Show account details section (supports title parameter)

### Order Confirmation

**sc_order_confirmation** — Show order confirmation wrapper (no parameters)

**sc_order_confirmation_line_items** — Show order items (no parameters)

### Product Collections

**sc_product_collection** — Display product collection page. Parameters: collection_id (required), columns, sort_enabled, pagination_enabled, ajax_pagination, limit

### Buy Button

**sc_buy_button** — Display a Buy Now button. Parameters: price_id (required), quantity, ad_hoc_amount

### Currency Switcher

**sc_currency_switcher** — Integrate currency switching (no parameters)

## Finding Product IDs

Product IDs appear in the edit product URL. The ID is the value after `id=` at the end of the URL when editing a product in the WordPress dashboard.
