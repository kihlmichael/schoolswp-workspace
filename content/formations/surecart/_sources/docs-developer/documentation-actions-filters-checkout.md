---
source_url: https://developer.surecart.com/documentation/actions-filters/checkout
source: surecart-developer-docs
scraped: true
---

[Skip to main content](https://developer.surecart.com/documentation/actions-filters/checkout#content-area)

> ## Documentation Index
>
> Fetch the complete documentation index at: [https://developer.surecart.com/llms.txt](https://developer.surecart.com/llms.txt)
>
> Use this file to discover all available pages before exploring further.

These hooks allow you to respond to checkout events and customize the checkout experience.

## [​](https://developer.surecart.com/documentation/actions-filters/checkout#actions) Actions

Actions are triggered during the checkout process and when orders are confirmed. This is at the end, after payment is successuflly confirmed by the processor.

### [​](https://developer.surecart.com/documentation/actions-filters/checkout#surecart/checkout_confirmed) `surecart/checkout_confirmed`

Fired after an order is confirmed and all purchases have been processed. Use this for post-checkout operations like analytics tracking, external notifications, or custom logging.

Parameters: `$checkout` (`\SureCart\Models\Checkout`) — The checkout model object containing order details. `$request` (`\WP_REST_Request`) — The REST API request object.

```
add_action( 'surecart/checkout_confirmed', function( $checkout, $request ) {
    // Fetch the checkout with customer relation loaded.
    $checkout = \SureCart\Models\Checkout::with(['customer'])->find( $checkout->id );

    // Access order details
    $order_id = $checkout->id;
    $total = $checkout->total_amount;

    // Track conversion
    if ( function_exists( 'track_conversion' ) ) {
        track_conversion( $order_id, $total );
    }

    // Send to external system
    wp_remote_post( 'https://api.example.com/orders', [
        'body' => [
            'order_id' => $order_id,
            'total' => $total,
            'customer_email' => $checkout->customer->email,
        ]
    ]);
}, 10, 2 );
```

## [​](https://developer.surecart.com/documentation/actions-filters/checkout#filters) Filters

### [​](https://developer.surecart.com/documentation/actions-filters/checkout#form-validation) Form Validation

#### [​](https://developer.surecart.com/documentation/actions-filters/checkout#surecart/checkout/validate) `surecart/checkout/validate`

Add custom server-side validation to checkout forms.

```
add_filter( 'surecart/checkout/validate', function( $errors, $args, $request ) {
    // Require a custom field
    if ( empty( $args['metadata']['company_name'] ) ) {
        $errors->add( 'company_required', 'Company name is required.' );
    }

    return $errors;
}, 10, 3 );
```

### [​](https://developer.surecart.com/documentation/actions-filters/checkout#payment-mode) Payment Mode

#### [​](https://developer.surecart.com/documentation/actions-filters/checkout#surecart/payments/mode) `surecart/payments/mode`

```
add_filter( 'surecart/payments/mode', function( $mode ) {
    // Force test mode for admins
    if ( current_user_can( 'manage_options' ) ) {
        return 'test';
    }
    return $mode;
} );
```

## [​](https://developer.surecart.com/documentation/actions-filters/checkout#javascript-filters) JavaScript Filters

SureCart provides JavaScript filters using the WordPress hooks system (`wp.hooks`) to customize the Stripe Payment Element.

### Payment Method Order

```
wp.hooks.addFilter(
  "surecart_stripe_payment_element_payment_method_order",
  "my-customization",
  (paymentMethodOrder, checkout) => {
    return ["card", "us_bank_account", "klarna"];
  }
);
```

### Wallet Visibility

```
wp.hooks.addFilter(
  "surecart_stripe_payment_element_wallets",
  "my-customization",
  (wallets, checkout) => {
    return {
      applePay: "auto",
      googlePay: "auto",
      link: "never",
    };
  }
);
```

### Address Countries

```
wp.hooks.addFilter(
  "surecart_address_countries",
  "my-customization",
  (countries) => {
    return [
      { value: "US", label: "United States" },
      { value: "CA", label: "Canada" },
      { value: "GB", label: "United Kingdom" },
    ];
  }
);
```
