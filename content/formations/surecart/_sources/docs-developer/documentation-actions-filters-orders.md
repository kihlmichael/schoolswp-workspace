---
source_url: https://developer.surecart.com/documentation/actions-filters/orders
source: surecart-developer-docs
scraped: true
---

[Skip to main content](https://developer.surecart.com/documentation/actions-filters/orders#content-area)

> ## Documentation Index
>
> Fetch the complete documentation index at: [https://developer.surecart.com/llms.txt](https://developer.surecart.com/llms.txt)
>
> Use this file to discover all available pages before exploring further.

These actions fire during order processing, payments, refunds, and invoicing.

## [​](https://developer.surecart.com/documentation/actions-filters/orders#order-actions) Order Actions

### `surecart/order_created`

```
add_action( 'surecart/order_created', function( $order, $data ) {
    error_log( sprintf( 'New order created: %s', $order ) );
}, 10, 2 );
```

### `surecart/order_updated`

```
add_action( 'surecart/order_updated', function( $order, $data ) {
    if ( $order->status === 'paid' ) {
        mark_order_complete_in_erp( $order->id );
    }
}, 10, 2 );
```

## [​](https://developer.surecart.com/documentation/actions-filters/orders#charge-actions) Charge Actions

### `surecart/charge_created`

```
add_action( 'surecart/charge_created', function( $charge, $data ) {
    error_log( sprintf( 'Payment received: %s for %d cents', $charge->id, $charge->amount ) );
    track_revenue( $charge->amount, $charge->currency );
}, 10, 2 );
```

## [​](https://developer.surecart.com/documentation/actions-filters/orders#refund-actions) Refund Actions

### `surecart/refund_created`

```
add_action( 'surecart/refund_created', function( $refund, $data ) {
    wp_mail(
        get_option( 'admin_email' ),
        'Refund Processed',
        sprintf( 'A refund of %d cents has been processed.', $refund->amount )
    );
}, 10, 2 );
```

## [​](https://developer.surecart.com/documentation/actions-filters/orders#invoice-actions) Invoice Actions

### `surecart/invoice_created`

Fires when an invoice is **manually** created by a user in the admin. Does NOT fire for automatic subscription invoices or checkout orders.

```
add_action( 'surecart/invoice_created', function( $invoice, $data ) {
    send_to_quickbooks( $invoice );
}, 10, 2 );
```
