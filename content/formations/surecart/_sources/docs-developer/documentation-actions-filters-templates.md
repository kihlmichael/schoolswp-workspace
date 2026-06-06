---
source_url: https://developer.surecart.com/documentation/actions-filters/templates
source: surecart-developer-docs
scraped: true
---

[Skip to main content](https://developer.surecart.com/documentation/actions-filters/templates#content-area)

> ## Documentation Index
>
> Fetch the complete documentation index at: [https://developer.surecart.com/llms.txt](https://developer.surecart.com/llms.txt)
>
> Use this file to discover all available pages before exploring further.

## [​](https://developer.surecart.com/documentation/actions-filters/templates#modifying-block-and-front-end-html) Modifying Block and Front-End HTML

You can modify the HTML output of any SureCart block using WordPress's `render_block` filter combined with the HTML Tag Processor.

### Finding a Block's Name

SureCart blocks use the `surecart/` namespace (e.g., `surecart/product-title`). The wrapper element class follows the pattern `wp-block-{namespace}-{block-name}`. In the Code Editor, block names appear in HTML comments like `<!-- wp:surecart/product-title -->`.

Common SureCart blocks: `surecart/product-title`, `surecart/product-price`, `surecart/buy-button`, `surecart/product-image`, `surecart/product-description`, `surecart/product-collection`.

### Using `render_block`

```
add_filter( 'render_block', function( $block_content, $block ) {
    if ( 'surecart/product-title' !== $block['blockName'] ) {
        return $block_content;
    }
    return $block_content;
}, 10, 2 );
```

Block-specific shorthand (cleaner):

```
add_filter( 'render_block_surecart/product-title', function( $block_content, $block, $instance ) {
    return $block_content;
}, 10, 3 );
```

### Using the HTML Tag Processor

```
add_filter( 'render_block_surecart/product-title', function( $block_content, $block, $instance ) {
    $processor = new WP_HTML_Tag_Processor( $block_content );

    if ( $processor->next_tag( 'h2' ) ) {
        $processor->add_class( 'my-custom-title-class' );
        $processor->set_attribute( 'data-custom', 'value' );
    }

    return $processor->get_updated_html();
}, 10, 3 );
```

### Block Examples

#### Add Custom Data Attributes to Buy Buttons

```
add_filter( 'render_block_surecart/buy-button', function( $block_content, $block, $instance ) {
    $processor = new WP_HTML_Tag_Processor( $block_content );

    if ( $processor->next_tag( 'a' ) ) {
        $processor->set_attribute( 'data-track', 'buy-button-click' );
        $processor->set_attribute( 'data-product-id', $block['attrs']['id'] ?? '' );
    }

    return $processor->get_updated_html();
}, 10, 3 );
```

#### Wrap Product Prices with Custom Markup

```
add_filter( 'render_block_surecart/product-price', function( $block_content, $block, $instance ) {
    return '<div class="price-wrapper">' . $block_content . '</div>';
}, 10, 3 );
```

#### Add Low Stock Warning Badge

Uses SureCart's `.sc-tag` component classes (`--warning`, `--success`, `--danger`, `--info`, `--primary`; sizes `--small`, `--medium`, `--large`; `--pill` for rounded corners).

```
add_filter( 'render_block_surecart/product-title', function( $block_content, $block, $instance ) {
    $product = sc_get_product();

    if ( empty( $product->stock_enabled ) ) {
        return $block_content;
    }

    if ( $product->available_stock >= 5 ) {
        return $block_content;
    }

    $badge = sprintf(
        '<span class="sc-tag sc-tag--warning sc-tag--small sc-tag--pill">Only %d left!</span>',
        $product->available_stock
    );

    return $block_content . $badge;
}, 10, 3 );
```

## [​](https://developer.surecart.com/documentation/actions-filters/templates#review-filters) Review Filters

### `surecart/review_form/enabled`

```
add_filter( 'surecart/review_form/enabled', function( $enabled ) {
    return is_user_logged_in();
} );
```

### `sc_anonymous_reviewer_name`

```
add_filter( 'sc_anonymous_reviewer_name', function( $name ) {
    return 'Verified Buyer';
} );
```

## [​](https://developer.surecart.com/documentation/actions-filters/templates#template-actions) Template Actions

### `surecart_buy_page_body_open`

```
add_action( 'surecart_buy_page_body_open', function() {
    echo '<div class="announcement-bar">Special offer: 20% off!</div>';
} );
```

### `surecart_template_dashboard_body_open`

```
add_action( 'surecart_template_dashboard_body_open', function() {
    if ( is_user_logged_in() ) {
        $user = wp_get_current_user();
        echo '<div class="welcome-message">Welcome back, ' . esc_html( $user->display_name ) . '!</div>';
    }
} );
```
