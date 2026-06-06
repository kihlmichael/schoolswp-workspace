---
source_url: https://developer.surecart.com/documentation/actions-filters/customers
source: surecart-developer-docs
scraped: true
---

[Skip to main content](https://developer.surecart.com/documentation/actions-filters/customers#content-area)

> ## Documentation Index
>
> Fetch the complete documentation index at: [https://developer.surecart.com/llms.txt](https://developer.surecart.com/llms.txt)
>
> Use this file to discover all available pages before exploring further.

These actions fire when customer records are updated.

## [​](https://developer.surecart.com/documentation/actions-filters/customers#surecart/customer_updated) `surecart/customer_updated`

Fires when a customer's information is updated.

Parameters: `$customer` (`\SureCart\Models\Customer`) — The customer model object. `$data` (object) — The raw event data.

```
add_action( 'surecart/customer_updated', function( $customer, $data ) {
    // Sync customer to CRM
    sync_customer_to_crm( $customer );
}, 10, 2 );
```

## [​](https://developer.surecart.com/documentation/actions-filters/customers#use-cases) Use Cases

### Sync to CRM

```
add_action( 'surecart/customer_updated', function( $customer, $data ) {
    wp_remote_post( 'https://api.hubspot.com/contacts/v1/contact', [
        'body' => json_encode([
            'properties' => [
                [ 'property' => 'email', 'value' => $customer->email ],
                [ 'property' => 'firstname', 'value' => $customer->first_name ?? '' ],
                [ 'property' => 'lastname', 'value' => $customer->last_name ?? '' ],
                [ 'property' => 'phone', 'value' => $customer->phone ?? '' ],
            ]
        ]),
        'headers' => [
            'Authorization' => 'Bearer ' . HUBSPOT_API_KEY,
            'Content-Type' => 'application/json',
        ],
    ]);
}, 10, 2 );
```

### Sync WordPress User Profile

```
add_action( 'surecart/customer_updated', function( $customer, $data ) {
    $user = $customer->getUser();

    if ( $user ) {
        update_user_meta( $user->ID, 'billing_phone', $customer->phone ?? '' );

        if ( ! empty( $customer->name ) && $user->display_name !== $customer->name ) {
            wp_update_user([
                'ID'           => $user->ID,
                'display_name' => $customer->name,
            ]);
        }
    }
}, 10, 2 );
```
