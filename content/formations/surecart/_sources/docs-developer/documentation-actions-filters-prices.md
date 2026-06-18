---
source_url: https://developer.surecart.com/documentation/actions-filters/prices
source: surecart-developer-docs
scraped: true
---

[Skip to main content](https://developer.surecart.com/documentation/actions-filters/prices#content-area)

> ## Documentation Index
>
> Fetch the complete documentation index at: [https://developer.surecart.com/llms.txt](https://developer.surecart.com/llms.txt)
>
> Use this file to discover all available pages before exploring further.

These actions fire when prices are created, updated, or deleted. Prices in SureCart are similar to Stripe prices—they define the cost, currency, and billing interval for a product.

## `surecart/price_created`

Fires when a new price is created for a product.

Parameters: `$price` (`\SureCart\Models\Price`), `$data` (object — raw event data).

```
add_action( 'surecart/price_created', function( $price, $data ) {
    wp_remote_post( SLACK_WEBHOOK_URL, [
        'body' => json_encode([
            'text' => sprintf( '💰 New price created: %s (%s)', $price->name ?? $price->id, $price->display_amount )
        ]),
    ]);
}, 10, 2 );
```

## `surecart/price_updated`

```
add_action( 'surecart/price_updated', function( $price, $data ) {
    wp_remote_patch( 'https://api.accounting.example.com/prices/' . $price->id, [
        'headers' => [ 'Authorization' => 'Bearer ' . ACCOUNTING_API_KEY ],
        'body'    => json_encode([
            'amount'   => $price->amount,
            'currency' => $price->currency,
            'name'     => $price->name,
        ]),
    ]);
}, 10, 2 );
```

## `surecart/price_deleted`

```
add_action( 'surecart/price_deleted', function( $price, $data ) {
    wp_remote_request( 'https://api.billing.example.com/prices/' . $price->id, [
        'method'  => 'DELETE',
        'headers' => [ 'Authorization' => 'Bearer ' . BILLING_API_KEY ],
    ]);
}, 10, 2 );
```
