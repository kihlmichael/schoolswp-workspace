---
source_url: https://developer.surecart.com/documentation/actions-filters/errors
source: surecart-developer-docs
scraped: true
---

[Skip to main content](https://developer.surecart.com/documentation/actions-filters/errors#content-area)

> ## Documentation Index
>
> Fetch the complete documentation index at: [https://developer.surecart.com/llms.txt](https://developer.surecart.com/llms.txt)
>
> Use this file to discover all available pages before exploring further.

These filters allow you to customize how error messages are displayed to customers throughout SureCart.

## [​](https://developer.surecart.com/documentation/actions-filters/errors#error-message-filters) Error Message Filters

### [​](https://developer.surecart.com/documentation/actions-filters/errors#surecart/translated_error) `surecart/translated_error`

Filter individual translated error messages. The `$response` object contains the error details including `code`, `attribute`, `type`, and `options`.

```
add_filter( 'surecart/translated_error', function( $translated, $response ) {
    if ( ( $response['code'] ?? '' ) === 'checkout.discount.promotion_code.invalid_code' ) {
        return 'Sorry, that promo code is not valid. Please check and try again.';
    }
    return $translated;
}, 10, 2 );
```

### [​](https://developer.surecart.com/documentation/actions-filters/errors#surecart/translated_errors) `surecart/translated_errors`

Filter the WP_Error object containing all translated error messages.

```
add_filter( 'surecart/translated_errors', function( $wp_error ) {
    foreach ( $wp_error->get_error_codes() as $code ) {
        $message = $wp_error->get_error_message( $code );
        $wp_error->remove( $code );
        $wp_error->add( $code, $message . ' Need help? Contact support.' );
    }
    return $wp_error;
} );
```

## [​](https://developer.surecart.com/documentation/actions-filters/errors#common-error-codes) Common Error Codes

| Code                                            | Default Message                                            |
| ----------------------------------------------- | ---------------------------------------------------------- |
| `checkout.discount.promotion_code.invalid_code` | Invalid promotion code.                                    |
| `checkout.discount.coupon.expired`              | This coupon has expired.                                   |
| `checkout.line_items.not_purchasable`           | Some items in your cart have reached their purchase limit. |
| `checkout.product.out_of_stock`                 | This product is out of stock.                              |
| `checkout.price.exceeds_purchase_limit`         | You have exceeded the purchase limit for this product.     |
| `checkout.shipping_address.postal_code.invalid` | Your postal code is not valid.                             |
