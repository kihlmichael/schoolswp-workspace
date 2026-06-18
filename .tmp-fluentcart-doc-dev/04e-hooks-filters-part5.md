# FluentCart Developer Docs - Hooks (Filters) (Part 5/6)

Tous les filtres WordPress exposés par FluentCart, groupés par domaine (cart & checkout, orders & payments, customers & subscriptions, products & pricing, settings & configuration, integrations & advanced).

---

## Products & Pricing | FluentCart Developer Docs

**URL** : https://dev.fluentcart.com/hooks/filters/products-and-pricing

[Skip to content](https://dev.fluentcart.com/hooks/filters/products-and-pricing#VPContent)

# Products & Pricing [​](https://dev.fluentcart.com/hooks/filters/products-and-pricing\#products-pricing)

All filters related to [Product](https://dev.fluentcart.com/database/models/product.html) display, catalog management, pricing, stock, URLs, and [Coupon](https://dev.fluentcart.com/database/models/coupon.html) s.

* * *

## Product Display & Layout [​](https://dev.fluentcart.com/hooks/filters/products-and-pricing\#product-display-layout)

### ` products_list` [​](https://dev.fluentcart.com/hooks/filters/products-and-pricing\#products-list)

`fluent_cart/products_list` - Filter the admin products list

**When it runs:** This filter is applied after fetching the paginated products collection in the admin products list view.

**Parameters:**

- `$products` (LengthAwarePaginator): The paginated products collection with appended `view_url` and `edit_url` attributes

**Returns:**

- `$products` (LengthAwarePaginator): The modified paginated collection

**Source:**`app/Http/Controllers/ProductController.php:52`

**Usage:**

php

```
add_filter('fluent_cart/products_list', function($products) {
    // Modify the products collection before it is returned to the admin
    $products->getCollection()->transform(function ($product) {
        $product->custom_badge = 'Featured';
        return $product;
    });
    return $products;
}, 10, 1);
```

### ` shop_query` [​](https://dev.fluentcart.com/hooks/filters/products-and-pricing\#shop-query)

`fluent_cart/shop_query` - Filter the shop product query builder

**When it runs:** This filter is applied when building the query for the public-facing shop product listing, before search, status, and sorting clauses are added.

**Parameters:**

- `$query` (Builder): The Eloquent query builder instance with `select` and `with` already applied
- `$params` (array): The query parameters array
php

```
$params = [\
      'select'               => '*',\
      'with'                 => [],\
      'admin_all_statuses'   => [],\
      'selected_status'      => '',\
      // ...additional request parameters\
];
```


**Returns:**

- `$query` (Builder): The modified query builder

**Source:**`api/Resource/ShopResource.php:100`

**Usage:**

php

```
add_filter('fluent_cart/shop_query', function($query, $params) {
    // Only show products from a specific category
    $query->whereHas('taxonomies', function ($q) {
        $q->where('taxonomy', 'product-category')
          ->where('term_id', 5);
    });
    return $query;
}, 10, 2);
```

### ` single_product/variation_view_type` [​](https://dev.fluentcart.com/hooks/filters/products-and-pricing\#single-product-variation-view-type)

`fluent_cart/single_product/variation_view_type` - Filter the variation display type on single product pages

**When it runs:** This filter is applied when initializing the product renderer to determine how variations are visually presented on the single product page.

**Parameters:**

- `$viewType` (string): The variation view type. Possible values: `'image'`, `'text'`, `'both'`
- `$data` (array): Context data
php

```
$data = [\
      'product'            => $product,       // Product model\
      'variants'           => $variants,       // Collection of variants\
      'defaultVariationId' => $defaultVariationId // Default selected variation ID\
];
```


**Returns:**

- `$viewType` (string): The modified view type

**Source:**`app/Services/Renderer/ProductRenderer.php:67`

**Usage:**

php

```
add_filter('fluent_cart/single_product/variation_view_type', function($viewType, $data) {
    // Always show both image and text for variations
    return 'both';
}, 10, 2);
```

### ` single_product/variation_column_type` [​](https://dev.fluentcart.com/hooks/filters/products-and-pricing\#single-product-variation-column-type)

`fluent_cart/single_product/variation_column_type` - Filter the variation column layout on single product pages

**When it runs:** This filter is applied when initializing the product renderer to determine the column layout for product variations.

**Parameters:**

- `$columnType` (string): The column layout type. Possible values: `'one'`, `'two'`, `'three'`, `'four'`, `'masonry'`
- `$data` (array): Context data
php

```
$data = [\
      'product'            => $product,       // Product model\
      'variants'           => $variants,       // Collection of variants\
      'defaultVariationId' => $defaultVariationId // Default selected variation ID\
];
```


**Returns:**

- `$columnType` (string): The modified column type

**Source:**`app/Services/Renderer/ProductRenderer.php:74`

**Usage:**

php

```
add_filter('fluent_cart/single_product/variation_column_type', function($columnType, $data) {
    $product = $data['product'];
    // Use two-column layout for products with many variations
    if (count($data['variants']) > 6) {
        return 'two';
    }
    return $columnType;
}, 10, 2);
```

### ` single_product/variation_price` [​](https://dev.fluentcart.com/hooks/filters/products-and-pricing\#single-product-variation-price)

`fluent_cart/single_product/variation_price` - Filter the variation price text displayed on single product pages

**When it runs:** This filter is applied when rendering the price text for each product variation. For one-time products the price is the formatted decimal amount; for subscriptions it includes the billing terms text.

**Parameters:**

- `$priceText` (string): The formatted price text (escaped HTML)
- `$data` (array): Context data
php

```
$data = [\
      'product' => $product,   // Product model\
      'variant' => $variant,   // ProductVariant model\
      'scope'   => 'product_variant_price'\
];
```


**Returns:**

- `$priceText` (string): The modified price text (HTML allowed via `wp_kses_post`)

**Source:**`app/Services/Renderer/ProductRenderer.php:827`

**Usage:**

php

```
add_filter('fluent_cart/single_product/variation_price', function($priceText, $data) {
    $variant = $data['variant'];
    // Append a "per month" label for subscription variants
    if ($variant->payment_type === 'subscription') {
        return $priceText . ' <small>/month</small>';
    }
    return $priceText;
}, 10, 2);
```

### ` shop_app_product_query_taxonomy_filters` [​](https://dev.fluentcart.com/hooks/filters/products-and-pricing\#shop-app-product-query-taxonomy-filters)

`fluent_cart/shop_app_product_query_taxonomy_filters` - Filter taxonomy filters for the Shop block product query

**When it runs:** This filter is applied in the Shop App Gutenberg block when merging URL-based taxonomy filters with default block filters, before the product query is executed.

**Parameters:**

- `$mergedTerms` (array): Merged taxonomy term IDs keyed by taxonomy name
php

```
$mergedTerms = [\
      'product-category' => [1, 5, 12],\
      'product-tag'      => [3, 7]\
];
```

- `$data` (array): Context data
php

```
$data = [\
      'default_terms'   => $defaultTerms,   // Terms from block settings\
      'url_terms'       => $urlTerms,        // Terms from URL query parameters\
      'url_filters'     => $urlFilters,      // Raw URL filter parameters\
      'default_filters' => $defaultFilters,  // Raw block default filters\
      'block'           => $block,           // Block instance\
      'is_main_query'   => true|false        // Whether this is the main query\
];
```


**Returns:**

- `$mergedTerms` (array): The modified taxonomy term IDs array

**Source:**`app/Hooks/Handlers/BlockEditors/ShopApp/InnerBlocks/InnerBlocks.php:1379`

**Usage:**

php

```
add_filter('fluent_cart/shop_app_product_query_taxonomy_filters', function($mergedTerms, $data) {
    // Always exclude a specific category from shop listings
    if (isset($mergedTerms['product-category'])) {
        $mergedTerms['product-category'] = array_diff($mergedTerms['product-category'], [99]);
    }
    return $mergedTerms;
}, 10, 2);
```

### ` products_views/preload_collection_{$provider}` [​](https://dev.fluentcart.com/hooks/filters/products-and-pricing\#products-views-preload-collection-provider)

`fluent_cart/products_views/preload_collection_{$provider}` - Preload product view collection for a template provider

**When it runs:** This dynamic filter is applied when the shop controller loads products via AJAX for a specific template provider (e.g., `bricks`). The `{$provider}` portion is replaced with the template provider name from the request.

**Parameters:**

- `$html` (string): Default empty string. Return rendered HTML to use the preloaded view instead of JSON
- `$data` (array): Context data
php

```
$data = [\
      'client_id'   => $clientId,    // Client identifier from the request\
      'products'    => $products,     // Array of product data\
      'total'       => $total,        // Total number of products\
      'requestData' => $requestData   // Full request parameters\
];
```


**Returns:**

- `$html` (string): Rendered HTML string, or empty string to fall back to default JSON response

**Source:**`app/Http/Controllers/ShopController.php:103`

**Usage:**

php

```
add_filter('fluent_cart/products_views/preload_collection_bricks', function($html, $data) {
    // Return custom rendered HTML for Bricks page builder
    ob_start();
    foreach ($data['products'] as $product) {
        echo '<div class="custom-product-card">' . esc_html($product['title']) . '</div>';
    }
    return ob_get_clean();
}, 10, 2);
```

* * *

## Product Buttons & Text [​](https://dev.fluentcart.com/hooks/filters/products-and-pricing\#product-buttons-text)

### ` product/buy_now_button_text` [​](https://dev.fluentcart.com/hooks/filters/products-and-pricing\#product-buy-now-button-text)

`fluent_cart/product/buy_now_button_text` - Filter the Buy Now button text

**When it runs:** This filter is applied when rendering the "Buy Now" button on single product pages. It runs in both the PHP product renderer and when localizing JavaScript variables for the frontend.

**Parameters:**

- `$text` (string): The button text. Default: `'Buy Now'` (translated)
- `$data` (array): Context data
php

```
$data = [\
      'product' => $product // Product model (when rendered server-side)\
];
```


**Returns:**

- `$text` (string): The modified button text

**Source:**`app/Services/Renderer/ProductRenderer.php:1081,1181`, `app/Modules/Templating/AssetLoader.php:87,261`

**Usage:**

php

```
add_filter('fluent_cart/product/buy_now_button_text', function($text, $data) {
    // Customize Buy Now text for specific products
    if (!empty($data['product']) && $data['product']->product_type === 'digital') {
        return 'Download Now';
    }
    return $text;
}, 10, 2);
```

### ` product/add_to_cart_text` [​](https://dev.fluentcart.com/hooks/filters/products-and-pricing\#product-add-to-cart-text)

`fluent_cart/product/add_to_cart_text` - Filter the Add to Cart button text

**When it runs:** This filter is applied when rendering the "Add to Cart" button text across multiple contexts: single product pages, shop blocks, product carousels, shortcodes, and localized JavaScript variables.

**Parameters:**

- `$text` (string): The button text. Default: `'Add To Cart'` (translated)
- `$data` (array): Context data
php

```
$data = [\
      'product' => $product // Product model (when rendered server-side)\
];
```


**Returns:**

- `$text` (string): The modified button text

**Source:**`app/Services/Renderer/ProductRenderer.php:1227,1314`, `app/Hooks/Handlers/ShortCodes/SingleProductShortCode.php:81`, `app/Hooks/Handlers/BlockEditors/ShopApp/InnerBlocks/InnerBlocks.php:1025,1104`, `app/Modules/Templating/AssetLoader.php:83,258`, `app/Hooks/Handlers/BlockEditors/ProductCarousel/InnerBlocks/InnerBlocks.php:493`

**Usage:**

php

```
add_filter('fluent_cart/product/add_to_cart_text', function($text, $data) {
    // Change to a different label
    return 'Add to Basket';
}, 10, 2);
```

### ` product/out_of_stock_text` [​](https://dev.fluentcart.com/hooks/filters/products-and-pricing\#product-out-of-stock-text)

`fluent_cart/product/out_of_stock_text` - Filter the out-of-stock button text

**When it runs:** This filter is applied when rendering the button text for products that are out of stock. It is used across shortcodes, shop blocks, product carousels, and localized JavaScript variables.

**Parameters:**

- `$text` (string): The out-of-stock text. Default: `'Not Available'` (translated)
- `$data` (array): Context data (empty array)

**Returns:**

- `$text` (string): The modified out-of-stock text

**Source:**`app/Hooks/Handlers/ShortCodes/SingleProductShortCode.php:83`, `app/Hooks/Handlers/BlockEditors/ShopApp/InnerBlocks/InnerBlocks.php:1027,1106`, `app/Modules/Templating/AssetLoader.php:85`, `app/Hooks/Handlers/BlockEditors/ProductCarousel/InnerBlocks/InnerBlocks.php:495`

**Usage:**

php

```
add_filter('fluent_cart/product/out_of_stock_text', function($text) {
    return 'Sold Out';
}, 10, 1);
```

### ` product/out_of_stock_button_text` [​](https://dev.fluentcart.com/hooks/filters/products-and-pricing\#product-out-of-stock-button-text)

`fluent_cart/product/out_of_stock_button_text` - Filter the out-of-stock button text (block editor variant)

**When it runs:** This filter is applied in the block editor asset loader when localizing the out-of-stock button text for JavaScript-rendered product pages. It serves the same purpose as `out_of_stock_text` but is used in a different rendering context.

**Parameters:**

- `$text` (string): The out-of-stock text. Default: `'Not Available'` (translated)
- `$data` (array): Context data (empty array)

**Returns:**

- `$text` (string): The modified out-of-stock button text

**Source:**`app/Modules/Templating/AssetLoader.php:260`

**Usage:**

php

```
add_filter('fluent_cart/product/out_of_stock_button_text', function($text) {
    return 'Currently Unavailable';
}, 10, 1);
```

### ` product/price_suffix_atts` [​](https://dev.fluentcart.com/hooks/filters/products-and-pricing\#product-price-suffix-atts)

`fluent_cart/product/price_suffix_atts` - Filter the price suffix for product variations

**When it runs:** This filter is applied when rendering each variation item in the variation selector. The Tax module hooks into this filter to append a price suffix (e.g., "incl. tax") configured in tax settings.

**Parameters:**

- `$suffix` (string): The price suffix text. Default: `''` (empty string)
- `$data` (array): Context data
php

```
$data = [\
      'product' => $product,   // Product model\
      'variant' => $variant,   // ProductVariant model\
      'scope'   => 'variant_item'\
];
```


**Returns:**

- `$suffix` (string): The modified price suffix text

**Source:**`app/Services/Renderer/ProductRenderer.php:1408`

**Usage:**

php

```
add_filter('fluent_cart/product/price_suffix_atts', function($suffix, $data) {
    // Add a custom price suffix
    return ' incl. VAT';
}, 10, 2);
```

### ` product_short_description` [​](https://dev.fluentcart.com/hooks/filters/products-and-pricing\#product-short-description)

`fluent_cart/product_short_description` - Filter the product short description

**When it runs:** This filter is applied when rendering the short description section on the single product page, using the post excerpt as the default value.

**Parameters:**

- `$shortDescription` (string): The product short description (from `$post->post_excerpt`)
- `$data` (array): Context data (empty array)

**Returns:**

- `$shortDescription` (string): The modified short description (output via `wp_kses_post`)

**Source:**`app/Hooks/Handlers/TemplateLoader.php:26`

**Usage:**

php

```
add_filter('fluent_cart/product_short_description', function($shortDescription) {
    // Append a disclaimer to all product short descriptions
    return $shortDescription . '<p class="disclaimer">Prices subject to change.</p>';
}, 10, 1);
```

* * *

## Stock & Availability [​](https://dev.fluentcart.com/hooks/filters/products-and-pricing\#stock-availability)

### ` product_stock_availability` [​](https://dev.fluentcart.com/hooks/filters/products-and-pricing\#product-stock-availability)

`fluent_cart/product_stock_availability` - Filter product stock availability information

**When it runs:** This filter is applied when retrieving the stock availability data for a product from the `ProductDetail` model. It runs after the default availability is determined based on stock management settings and current stock levels.

**Parameters:**

- `$availability` (array): The stock availability data
php

```
// When stock is not managed:
$availability = [\
      'manage_stock'       => false,\
      'availability'       => 'In Stock',\
      'class'              => 'in-stock',\
      'available_quantity' => null\
];

// When stock is managed and available:
$availability = [\
      'manage_stock'       => true,\
      'availability'       => 'In Stock',\
      'class'              => 'in-stock',\
      'available_quantity' => 25 // actual stock count\
];

// When stock is managed and depleted:
$availability = [\
      'manage_stock'       => true,\
      'availability'       => 'Out of Stock',\
      'class'              => 'out-of-stock',\
      'available_quantity' => 0\
];
```

- `$data` (array): Context data
php

```
$data = [\
      'detail'       => $productDetail, // ProductDetail model instance\
      'variation_id' => $variationId    // Variation ID or null\
];
```


**Returns:**

- `$availability` (array): The modified availability data

**Source:**`app/Models/ProductDetail.php:183`

**Usage:**

php

```
add_filter('fluent_cart/product_stock_availability', function($availability, $data) {
    // Show "Low Stock" warning when fewer than 5 items remain
    if ($availability['manage_stock'] && $availability['available_quantity'] > 0 && $availability['available_quantity'] < 5) {
        $availability['availability'] = 'Only ' . $availability['available_quantity'] . ' left in stock!';
        $availability['class'] = 'low-stock';
    }
    return $availability;
}, 10, 2);
```

* * *

## Product URLs & Templates [​](https://dev.fluentcart.com/hooks/filters/products-and-pricing\#product-urls-templates)

### ` price_class` [​](https://dev.fluentcart.com/hooks/filters/products-and-pricing\#price-class)

`fluent_cart/price_class` - Filter the price element CSS class

**When it runs:** This filter is applied when rendering the price paragraph element on the single product page template.

**Parameters:**

- `$class` (string): The CSS class for the price element. Default: `'price'`

**Returns:**

- `$class` (string): The modified CSS class string

**Source:**`app/Hooks/Handlers/TemplateLoader.php:40`

**Usage:**

php

```
add_filter('fluent_cart/price_class', function($class) {
    // Add additional CSS classes to the price element
    return 'price fct-custom-price';
}, 10, 1);
```

### ` front_url_slug` [​](https://dev.fluentcart.com/hooks/filters/products-and-pricing\#front-url-slug)

`fluent_cart/front_url_slug` - Filter the product URL slug

**When it runs:** This filter is applied when registering the `fluent-products` custom post type, allowing you to change the URL slug used for product permalinks.

**Parameters:**

- `$slug` (string): The product URL slug. Default comes from store settings, typically `'item'`
- `$data` (array): Context data (empty array)

**Returns:**

- `$slug` (string): The modified URL slug

**Source:**`app/CPT/FluentProducts.php:181`

**Note:** After changing the slug, you must flush rewrite rules (visit Settings > Permalinks in WP admin) for the change to take effect.

**Usage:**

php

```
add_filter('fluent_cart/front_url_slug', function($slug) {
    // Change product URLs from /item/product-name to /shop/product-name
    return 'shop';
}, 10, 1);
```

### ` product_url_with_front` [​](https://dev.fluentcart.com/hooks/filters/products-and-pricing\#product-url-with-front)

`fluent_cart/product_url_with_front` - Filter whether the product URL includes the front base

**When it runs:** This filter is applied when registering the `fluent-products` custom post type, immediately after `fluent_cart/front_url_slug` resolves the slug. The value is passed as the `with_front` argument to WordPress's `rewrite` option, controlling whether the site's permalink front base (e.g. `/blog/`) is prepended to product URLs.

**Parameters:**

- `$withFront` (bool): Whether to prepend the permalink front base. Default: `true`
- `$data` (array): Context data
php

```
$data = [\
      'slug' => $urlSlug // The resolved product URL slug\
];
```


**Returns:**

- `$withFront` (bool): The modified value

**Source:**`app/CPT/FluentProducts.php:183`

**Note:** After changing this value, flush rewrite rules by visiting Settings > Permalinks in the WordPress admin.

**Usage:**

php

```
add_filter('fluent_cart/product_url_with_front', function($withFront, $data) {
    // Remove the permalink front base from product URLs
    // e.g. /blog/products/my-item → /products/my-item
    return false;
}, 10, 2);
```

### ` show_standalone_product_menu` [​](https://dev.fluentcart.com/hooks/filters/products-and-pricing\#show-standalone-product-menu)

`fluent_cart/show_standalone_product_menu` - Filter whether to show a standalone Products menu in the WordPress admin

**When it runs:** This filter is applied during the `init` action when FluentCart registers the product custom post type. When enabled, a separate "Products" menu item appears in the WordPress admin sidebar.

**Parameters:**

- `$show` (bool): Whether to show the standalone menu. Default: `false`

**Returns:**

- `$show` (bool): The modified boolean value

**Source:**`app/CPT/FluentProducts.php:37`

**Usage:**

php

```
add_filter('fluent_cart/show_standalone_product_menu', function($show) {
    // Show the standalone Products menu in WP admin
    return true;
}, 10, 1);
```

### ` single_product_page/show_relevant_products` [​](https://dev.fluentcart.com/hooks/filters/products-and-pricing\#single-product-page-show-relevant-products)

`fluent_cart/single_product_page/show_relevant_products` - Filter whether to show related products on the single product page

**When it runs:** This filter is applied when rendering the single product page content, after checking the store setting `show_relevant_product_in_single_page`. When enabled, similar products are displayed below the main product content.

**Parameters:**

- `$show` (bool): Whether to show related products. Default comes from store settings
- `$postId` (int): The current product post ID

**Returns:**

- `$show` (bool): The modified boolean value

**Source:**`app/Modules/Templating/TemplateActions.php:240`

**Usage:**

php

```
add_filter('fluent_cart/single_product_page/show_relevant_products', function($show, $postId) {
    // Disable related products for specific product IDs
    $excludedIds = [100, 200, 300];
    if (in_array($postId, $excludedIds)) {
        return false;
    }
    return $show;
}, 10, 2);
```

### ` disable_auto_single_product_page` [​](https://dev.fluentcart.com/hooks/filters/products-and-pricing\#disable-auto-single-product-page)

`fluent_cart/disable_auto_single_product_page` - Disable automatic single product page rendering

**When it runs:** This filter is applied in two places: when filtering the post title and when filtering the post content for single product pages. When it returns `true`, FluentCart will not automatically inject product rendering into the default product page, allowing you to build the product page entirely with custom templates or page builders.

**Parameters:**

- `$disable` (bool): Whether to disable automatic rendering. Default: `false`

**Returns:**

- `$disable` (bool): The modified boolean value

**Source:**`app/Modules/Templating/TemplateActions.php:191,215`

**Usage:**

php

```
add_filter('fluent_cart/disable_auto_single_product_page', function($disable) {
    // Disable auto-rendering when using a custom page builder
    if (class_exists('Elementor\Plugin')) {
        return true;
    }
    return $disable;
}, 10, 1);
```

* * *

## Coupons [​](https://dev.fluentcart.com/hooks/filters/products-and-pricing\#coupons)

### ` coupon/validating_coupon` [​](https://dev.fluentcart.com/hooks/filters/products-and-pricing\#coupon-validating-coupon)

`fluent_cart/coupon/validating_coupon` - Filter the coupon code during validation

**When it runs:** This filter is applied at the very beginning of coupon validation, before the coupon is looked up in the database. You can modify the coupon code string or return a `WP_Error` to reject it early.

**Parameters:**

- `$couponCode` (string): The coupon code being validated
- `$data` (array): Context data
php

```
$data = [\
      'coupon_code'   => $couponCode,     // Original coupon code\
      'line_items'    => $lineItems,       // Cart line items\
      'couponService' => $couponService    // CouponService instance\
];
```


**Returns:**

- `$couponCode` (string\|WP\_Error): The modified coupon code, or a `WP_Error` to reject

**Source:**`app/Services/Coupon/Concerns/CanValidateCoupon.php:21`

**Usage:**

php

```
add_filter('fluent_cart/coupon/validating_coupon', function($couponCode, $data) {
    // Normalize coupon codes to uppercase
    $couponCode = strtoupper(trim($couponCode));

    // Block specific coupon codes
    $blockedCodes = ['EXPIRED2024', 'TESTONLY'];
    if (in_array($couponCode, $blockedCodes)) {
        return new \WP_Error('coupon_blocked', __('This coupon code is no longer valid.', 'fluent-cart'));
    }

    return $couponCode;
}, 10, 2);
```

### ` coupon/can_use_coupon` [​](https://dev.fluentcart.com/hooks/filters/products-and-pricing\#coupon-can-use-coupon)

`fluent_cart/coupon/can_use_coupon` - Filter whether a coupon can be used

**When it runs:** This filter is applied after the coupon has been validated and found in the database, but before the discount is calculated. It allows you to add custom eligibility checks.

**Parameters:**

- `$canUse` (bool): Whether the coupon can be used. Default: `true`
- `$data` (array): Context data
php

```
$data = [\
      'coupon'     => $coupon,     // Coupon model instance\
      'cart'       => $cart,        // Cart model instance\
      'cart_items' => $cartItems    // Array of cart item data\
];
```


**Returns:**

- `$canUse` (bool\|WP\_Error): `true` to allow, `false` or `WP_Error` to reject. When a `WP_Error` is returned, its message is shown to the customer

**Source:**`app/Services/Coupon/DiscountService.php:257`

**Usage:**

php

```
add_filter('fluent_cart/coupon/can_use_coupon', function($canUse, $data) {
    $coupon = $data['coupon'];
    $cart = $data['cart'];

    // Require a minimum cart subtotal of $50 (5000 cents)
    if ($cart->sub_total < 5000) {
        return new \WP_Error(
            'coupon_min_total',
            __('This coupon requires a minimum order of $50.', 'fluent-cart')
        );
    }

    return $canUse;
}, 10, 2);
```

### ` coupon/will_skip_item` [​](https://dev.fluentcart.com/hooks/filters/products-and-pricing\#coupon-will-skip-item)

`fluent_cart/coupon/will_skip_item` - Filter whether an item should be skipped from coupon discount

**When it runs:** This filter is applied for each cart item when filtering applicable items for a coupon discount. Returning `true` excludes the item from the coupon discount calculation.

**Parameters:**

- `$willSkip` (bool): Whether to skip this item. Default: `false`
- `$data` (array): Context data
php

```
$data = [\
      'item'   => $item,    // Cart item array data\
      'coupon' => $coupon,   // Coupon model instance\
      'cart'   => $cart      // Cart model instance\
];
```


**Returns:**

- `$willSkip` (bool): `true` to exclude the item from the coupon, `false` to include it

**Source:**`app/Services/Coupon/DiscountService.php:279`

**Usage:**

php

```
add_filter('fluent_cart/coupon/will_skip_item', function($willSkip, $data) {
    $item = $data['item'];

    // Never apply coupons to gift card items
    if (!empty($item['product_type']) && $item['product_type'] === 'gift_card') {
        return true;
    }

    return $willSkip;
}, 10, 2);
```

### ` coupon/per_customer_usage_query` [​](https://dev.fluentcart.com/hooks/filters/products-and-pricing\#coupon-per-customer-usage-query)

`fluent_cart/coupon/per_customer_usage_query` - Filter the per-customer coupon usage query

**When it runs:** This filter is applied when checking if a customer has exceeded the per-customer usage limit for a coupon. It allows you to modify the query that counts previous uses.

**Parameters:**

- `$usageQuery` (Builder): The Eloquent query builder for [`AppliedCoupon`](https://dev.fluentcart.com/database/models/applied-coupon.html) records, already filtered by coupon ID and customer ID
- `$data` (array): Context data
php

```
$data = [\
      'coupon'   => $coupon,    // Coupon model instance\
      'customer' => $customer,  // Customer model instance\
      'cart'     => $cart       // Cart model instance\
];
```


**Returns:**

- `$usageQuery` (Builder): The modified query builder

**Source:**`app/Services/Coupon/DiscountService.php:592`

**Usage:**

php

```
add_filter('fluent_cart/coupon/per_customer_usage_query', function($usageQuery, $data) {
    // Only count usage from the last 30 days (rolling usage limit)
    $usageQuery->where('created_at', '>=', gmdate('Y-m-d H:i:s', strtotime('-30 days')));
    return $usageQuery;
}, 10, 2);
```

### ` coupon_statuses` [​](https://dev.fluentcart.com/hooks/filters/products-and-pricing\#coupon-statuses)

`fluent-cart/coupon_statuses` - Filter the available coupon statuses

**When it runs:** This filter is applied when retrieving the list of available coupon statuses, used in the admin coupon management interface.

**Parameters:**

- `$statuses` (array): Array of coupon statuses (key => label)
php

```
$statuses = [\
      'active'   => 'Active',\
      'expired'  => 'Expired',\
      'disabled' => 'Disabled'\
];
```

- `$data` (array): Context data (empty array)

**Returns:**

- `$statuses` (array): The modified coupon statuses array

**Source:**`app/Helpers/Helper.php:823`

**Note:** This hook uses `fluent-cart/` (with a hyphen) instead of the usual `fluent_cart/` (with an underscore) prefix.

**Usage:**

php

```
add_filter('fluent-cart/coupon_statuses', function($statuses) {
    // Add a custom coupon status
    $statuses['scheduled'] = __('Scheduled', 'fluent-cart');
    return $statuses;
}, 10, 1);
```

* * *

Today

Hi! I’m your AI assistant. How can I assist you today?

Just now

Powered by **FluentBot**


---

---

