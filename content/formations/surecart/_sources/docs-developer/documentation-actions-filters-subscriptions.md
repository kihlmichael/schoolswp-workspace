---
source_url: https://developer.surecart.com/documentation/actions-filters/subscriptions
source: surecart-developer-docs
scraped: true
---

[Skip to main content](https://developer.surecart.com/documentation/actions-filters/subscriptions#content-area)

> ## Documentation Index
>
> Fetch the complete documentation index at: [https://developer.surecart.com/llms.txt](https://developer.surecart.com/llms.txt)
>
> Use this file to discover all available pages before exploring further.

These actions fire during subscription lifecycle events like renewals.

For handling subscription cancellations and restorations that affect purchase access, see [Purchases](https://developer.surecart.com/documentation/actions-filters/purchases). The `surecart/purchase_revoked` and `surecart/purchase_invoked` actions fire when subscriptions are canceled or restored.

## [​](https://developer.surecart.com/documentation/actions-filters/subscriptions#surecart/subscription_renewed) `surecart/subscription_renewed`

Fires when a subscription successfully renews.

Parameters: `$subscription` (`\SureCart\Models\Subscription`), `$data` (object — raw event data).

```
add_action( 'surecart/subscription_renewed', function( $subscription, $data ) {
    $subscription = \SureCart\Models\Subscription::with(['customer'])->find( $subscription->id );

    wp_mail(
        $subscription->customer->email,
        'Subscription Renewed',
        'Thank you! Your subscription has been renewed.'
    );
}, 10, 2 );
```

## [​](https://developer.surecart.com/documentation/actions-filters/subscriptions#use-cases) Use Cases

### Send Renewal Thank You Email

```
add_action( 'surecart/subscription_renewed', function( $subscription, $data ) {
    $subscription = \SureCart\Models\Subscription::with(['customer', 'price', 'price.product'])->find( $subscription->id );

    $customer = $subscription->customer;
    $product = $subscription->price->product ?? null;
    $product_name = is_object( $product ) ? $product->name : 'your subscription';

    wp_mail(
        $customer->email,
        'Thank you for renewing!',
        sprintf(
            "Hi %s,\n\nYour subscription to %s has been renewed.\n\nNext renewal: %s",
            $customer->first_name ?? 'there',
            $product_name,
            ! empty( $subscription->current_period_end_at ) ? gmdate( 'F j, Y', $subscription->current_period_end_at ) : 'N/A'
        )
    );
}, 10, 2 );
```

### Notify Team of High-Value Renewals

```
add_action( 'surecart/subscription_renewed', function( $subscription, $data ) {
    $subscription = \SureCart\Models\Subscription::with(['customer', 'price'])->find( $subscription->id );
    $amount = $subscription->price->amount ?? 0;

    if ( $amount >= 50000 ) {
        wp_mail(
            'sales@example.com',
            'High-Value Renewal',
            sprintf( 'Customer %s just renewed for $%s!', $subscription->customer->email, number_format( $amount / 100, 2 ) )
        );
    }
}, 10, 2 );
```
