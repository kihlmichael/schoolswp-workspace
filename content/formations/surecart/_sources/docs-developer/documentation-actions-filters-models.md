---
source_url: https://developer.surecart.com/documentation/actions-filters/models
source: surecart-developer-docs
scraped: true
---

[Skip to main content](https://developer.surecart.com/documentation/actions-filters/models#content-area)

> ## Documentation Index
>
> Fetch the complete documentation index at: [https://developer.surecart.com/llms.txt](https://developer.surecart.com/llms.txt)
>
> Use this file to discover all available pages before exploring further.

SureCart fires filters and actions when models are hydrated with data. These hooks allow you to modify model properties, add dynamic computed properties, or transform data as it's being populated into the model.

## [​](https://developer.surecart.com/documentation/actions-filters/models#surecart/object_name/attributes_set) `surecart/{object_name}/attributes_set`

Fired after all attributes are set on a model.

```
add_action( 'surecart/checkout/attributes_set', function( $checkout ) {
    $checkout->custom_total = $checkout->amount_due + $checkout->tax_amount;
} );

add_action( 'surecart/subscription/attributes_set', function( $subscription ) {
    $subscription->days_until_renewal = $subscription->current_period_end
        ? ceil( ( $subscription->current_period_end - time() ) / DAY_IN_SECONDS )
        : null;
} );
```

## [​](https://developer.surecart.com/documentation/actions-filters/models#surecart/object_name/attributes/key) `surecart/{object_name}/attributes/{key}`

Filter individual attribute values as they are being set on a model during hydration.

Parameters: `$value` (mixed), `$model` (Model instance). Returns: the filtered value.

```
add_filter( 'surecart/subscription/attributes/status', function( $value, $subscription ) {
    $subscription->status_label = ucfirst( str_replace( '_', ' ', $value ) );
    return $value;
}, 10, 2 );
```

## [​](https://developer.surecart.com/documentation/actions-filters/models#surecart/object_name/set_meta_data) `surecart/{object_name}/set_meta_data`

Filter metadata before it's set on a model during hydration.

```
add_filter( 'surecart/subscription/set_meta_data', function( $meta_data ) {
    $meta_data = (array) $meta_data;
    $meta_data['notification_preferences'] = $meta_data['notification_preferences'] ?? [
        'renewal_reminder' => true,
        'payment_failed'   => true,
    ];
    return (object) $meta_data;
} );
```

## [​](https://developer.surecart.com/documentation/actions-filters/models#available-models) Available Models

- `subscription`, `purchase`, `product`, `price`, `customer`, `order`, `checkout`, `charge`, `refund`, `invoice`, `coupon`
