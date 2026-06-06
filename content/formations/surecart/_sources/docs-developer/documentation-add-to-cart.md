---
source_url: https://developer.surecart.com/documentation/add-to-cart
source: surecart-developer-docs
scraped: true
---

[Skip to main content](https://developer.surecart.com/documentation/add-to-cart#content-area)

> ## Documentation Index
>
> Fetch the complete documentation index at: [https://developer.surecart.com/llms.txt](https://developer.surecart.com/llms.txt)
>
> Use this file to discover all available pages before exploring further.

SureCart provides multiple ways to add items to the cart programmatically:

1. **URL Parameters** - Redirect users to checkout with pre-filled line items
2. **Shortcodes** - Use built-in shortcodes for add-to-cart buttons
3. **Checkout Form Customization** - Add custom fields, checkboxes, or content

## [​](https://developer.surecart.com/documentation/add-to-cart#url-parameters) URL Parameters

### Basic Example

```
<?php
$checkout_url = add_query_arg(
    [
        'line_items' => [
            [
                'price_id' => 'price_xxxxxxxxxxxxx',
                'quantity' => 1,
            ],
        ],
    ],
    \SureCart::pages()->url( 'checkout' )
);
?>

<a href="<?php echo esc_url( $checkout_url ); ?>">Add to Cart</a>
```

### With Coupon Code

```
<?php
$checkout_url = add_query_arg(
    [
        'line_items' => [
            [ 'price_id' => 'price_xxxxxxxxxxxxx', 'quantity' => 1 ],
        ],
        'coupon' => 'SAVE10',
    ],
    \SureCart::pages()->url( 'checkout' )
);
?>
```

### With Product Variant

```
<?php
$checkout_url = add_query_arg(
    [
        'line_items' => [
            [
                'price_id'   => 'price_xxxxxxxxxxxxx',
                'quantity'   => 1,
                'variant_id' => 'variant_xxxxxxxxxxxxx',
            ],
        ],
    ],
    \SureCart::pages()->url( 'checkout' )
);
?>
```

## [​](https://developer.surecart.com/documentation/add-to-cart#shortcodes) Shortcodes

### Add to Cart Button

```
[sc_product_cart_button id="prod_xxxxxxxxxxxxx" text="Add To Cart"]
```

Parameters: `id` (required — product ID), `text` (button text, default "Add To Cart"), `width` (pixels), `add_to_cart` (boolean — add to cart vs. go directly to checkout).

### Buy Button with Line Items

```
[sc_buy_button]
    [sc_line_item price_id="price_xxxxxxxxxxxxx" quantity="1"]
[/sc_buy_button]
```

### Using Shortcodes in PHP

```
<?php echo do_shortcode( '[sc_product_cart_button id="prod_xxxxxxxxxxxxx" text="Buy Now"]' ); ?>
```

## [​](https://developer.surecart.com/documentation/add-to-cart#checkout-form-customization) Checkout Form Customization

### Add Custom Content Before Submit Button

```
add_filter( 'render_block', function( $block_content, $block ) {
    if ( 'surecart/submit' !== $block['blockName'] ) {
        return $block_content;
    }

    $checkbox = '<div class="my-terms-checkbox" style="margin-bottom: 1em;">
        <label style="display: flex; align-items: start; gap: 0.5em; cursor: pointer;">
            <input type="checkbox" name="accept_terms" value="yes" required />
            <span>I agree to the <a href="/terms" target="_blank">terms and conditions</a></span>
        </label>
    </div>';

    return $checkbox . $block_content;
}, 10, 2 );
```

### Server-Side Validation

```
add_filter( 'surecart/checkout/validate', function( $errors, $args, $request ) {
    $accept_terms = isset( $_POST['accept_terms'] ) ? sanitize_text_field( wp_unslash( $_POST['accept_terms'] ) ) : '';

    if ( 'yes' !== $accept_terms ) {
        $errors->add( 'terms_required', 'You must accept the terms and conditions.' );
    }

    return $errors;
}, 10, 3 );
```

### Checkout Block Names

| Block Name            | Description              |
| --------------------- | ------------------------ |
| `surecart/submit`     | Submit/Pay button        |
| `surecart/email`      | Email field              |
| `surecart/name`       | Full name field          |
| `surecart/first-name` | First name field         |
| `surecart/last-name`  | Last name field          |
| `surecart/phone`      | Phone number field       |
| `surecart/address`    | Address fields           |
| `surecart/payment`    | Payment method selection |
| `surecart/coupon`     | Coupon code field        |
| `surecart/line-items` | Order line items         |
| `surecart/totals`     | Order totals summary     |
