---
source_url: https://developer.surecart.com/api-reference/expanding-responses
source: surecart-developer-docs
scraped: true
---

[Skip to main content](https://developer.surecart.com/api-reference/expanding-responses#content-area)

> ## Documentation Index
>
> Fetch the complete documentation index at: [https://developer.surecart.com/llms.txt](https://developer.surecart.com/llms.txt)
>
> Use this file to discover all available pages before exploring further.

Many objects allow you to request additional information as an expanded response by using the expand request parameter. This parameter is available on all API requests, and applies to the response of that request only.

### [​](https://developer.surecart.com/api-reference/expanding-responses#two-types-of-expandable-properties) Two Types of Expandable Properties

In many cases, a response contains the ID of a related object in its properties by default. For example, a `price` has an associated `product`. In others cases, there are expandable properties on a response that are not by default included in the response. For example, a list of all `prices` in the `product` response.

### [​](https://developer.surecart.com/api-reference/expanding-responses#how-to-expand-properties) How to Expand Properties

Properties that can be expanded into objects are noted in this documentation with the `Expandable` label. You can request these properties be expanded by using the `expand[]` request parameter.**Example Request:**

```
curl \
  -X GET https://api.surecart.com/v1/orders/0d6edf76-98f3-441c-9c43-81a92e929988 \
  -H "Authorization: Bearer YOUR-API-KEY" \
  -d "expand[]"="checkout" \
  -d "expand[]"="checkout.customer"
```

**Example Response:**

```
{
  "id": "0d6edf76-98f3-441c-9c43-81a92e929988",
  "object": "order",
  "live_mode": true,
  "number": "0008",
  "order_type": "checkout",
  "statement_url": "https://app.surecart.com/statements/orders/0d6edf76-98f3-441c-9c43-81a92e929988",
  "status": "paid",
  "checkout": {
    "id": "f1a38ad4-f87d-4550-b2e0-91a128cadf06",
    "object": "checkout",
    "abandoned_checkout_enabled": true,
    "amount_due": 1900,
    ...
    "customer": {
      "id": "9efd5506-3b69-47d5-9a1e-fbc718aaf148",
      "object": "customer",
      "billing_matches_shipping": true,
      "email": "test@example.com",
      "first_name": "Test",
      "indexed": true,
      "last_name": "Customer",
      "live_mode": true,
      "name": "Test Customer",
      "phone": null,
      "unsubscribed": false,
      "billing_address": null,
      "default_payment_method": "5dd6179f-ac0d-4532-b84b-cb6a168f6ace",
      "shipping_address": "3732e0ee-2b76-44a7-9525-580c22845781",
      "tax_identifier": null,
      "created_at": 1664390001,
      "updated_at": 1664479758
    },
    ...
    "created_at": 1664479197,
    "updated_at": 1664479757
  },
  "created_at": 1664479758,
  "updated_at": 1664479758
}
```

### [​](https://developer.surecart.com/api-reference/expanding-responses#expand-limits) Expand Limits

- You can use the expand request parameter on any endpoint which returns expandable fields, including list, create, and update endpoints.
- You can expand multiple objects at once by identifying multiple items in the expand request parameter.
- Expansions have a maximum depth of two levels, and you can expand up to 15 objects.

### [​](https://developer.surecart.com/api-reference/expanding-responses#expanding-recursively) Expanding Recursively

You can expand recursively by specifying nested expandable properties after a dot(.). For example, requesting to expand `checkout` and `checkout.customer` on a `order` will expand the checkout and the customer within the checkout.Expanding list requests are plural, but expanding objects within a list are singular. For example, if you wanted to retrieve a checkout's line items and each line item's price, you would pass list_items and list_item.price as expand parameters.
