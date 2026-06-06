# SureCart - Docs Developer + Affiliate Marketing


===== SOURCE: 00-introduction.md =====

---
source_url: https://developer.surecart.com
source: surecart-developer-docs
scraped: true
---

[Skip to main content](https://developer.surecart.com/#content-area)

> ## Documentation Index
>
> Fetch the complete documentation index at: [https://developer.surecart.com/llms.txt](https://developer.surecart.com/llms.txt)
>
> Use this file to discover all available pages before exploring further.

Welcome to the SureCart developer documentation. Here you'll find everything you need to integrate, extend, and customize SureCart for your WordPress site.

## [​](https://developer.surecart.com/#getting-started) Getting Started

[**Working with Data** \\
\\
Learn how to query and manipulate SureCart data using PHP models and Redux\\
queries.](https://developer.surecart.com/documentation/php-models)

[**Orders & Purchases** \\
\\
Understand how orders and purchases work and how to integrate with them.](https://developer.surecart.com/documentation/orders-and-purchases)

[**Actions & Filters** \\
\\
Extend SureCart functionality using WordPress hooks, actions, and filters.](https://developer.surecart.com/documentation/actions-reference)

[**API Reference** \\
\\
Complete REST API documentation for programmatic access to SureCart.](https://developer.surecart.com/api-reference/introduction)

## [​](https://developer.surecart.com/#extending-surecart) Extending SureCart

[**Cart & Checkout** \\
\\
Programmatically add items to the cart and checkout.](https://developer.surecart.com/documentation/add-to-cart)

[**Custom Loops** \\
\\
Create custom product loops and displays.](https://developer.surecart.com/documentation/custom-loops)

[**Admin UI** \\
\\
Extend and customize the admin interface.](https://developer.surecart.com/documentation/admin-ui)


===== SOURCE: api-reference-authentication.md =====

---
source_url: https://developer.surecart.com/api-reference/authentication
source: surecart-developer-docs
scraped: true
---

[Skip to main content](https://developer.surecart.com/api-reference/authentication#content-area)

> ## Documentation Index
>
> Fetch the complete documentation index at: [https://developer.surecart.com/llms.txt](https://developer.surecart.com/llms.txt)
>
> Use this file to discover all available pages before exploring further.

The SureCart API uses API keys to authenticate requests. You can view and manage your API keys in the SureCart platform dashboard.There are two types of API keys – public and secret. Your secret API key can be used to make requests to most API endpoints listed in this documentation. Your public API key can be used to make requests to any endpoints within the `Public Endpoints` group. Your public API key is designed to be used in client side code and can be exposed.Your API keys carry many privileges, so be sure to keep them secure! Do not share your secret API keys in publicly accessible areas such as GitHub, client-side code, and so forth.All API requests must be made over HTTPS. Calls made over plain HTTP will fail. API requests without authentication will also fail.


===== SOURCE: api-reference-errors.md =====

---
source_url: https://developer.surecart.com/api-reference/errors
source: surecart-developer-docs
scraped: true
---

[Skip to main content](https://developer.surecart.com/api-reference/errors#content-area)

> ## Documentation Index
>
> Fetch the complete documentation index at: [https://developer.surecart.com/llms.txt](https://developer.surecart.com/llms.txt)
>
> Use this file to discover all available pages before exploring further.

SureCart uses conventional HTTP response codes to indicate the success or failure of an API request. In general: codes in the 2xx range indicate success. Codes in the 4xx range indicate an error that failed given the information provided (e.g., a required parameter was omitted, a charge failed, etc.). Codes in the 5xx range indicate an error with SureCart's servers (these are rare).

### [​](https://developer.surecart.com/api-reference/errors#http-status-codes) HTTP Status Codes

These are all of the status codes that the SureCart API will return.

| HTTP Status                | Description                                                             |
| -------------------------- | ----------------------------------------------------------------------- |
| `200` OK                   | Everything worked as expected                                           |
| `400` Bad Request          | The request was unacceptable, often due to missing a required parameter |
| `401`Unauthorized          | Invalid API token provided                                              |
| `404` Not Found            | The requested resource doesn't exist                                    |
| `422` Unprocessable Entity | The request failed validation or was not allowed for another reason     |
| `500` Server Error         | Something went wrong on SureCart's end                                  |

### [​](https://developer.surecart.com/api-reference/errors#error-responses) Error Responses

All error responses will be formatted like the example below, and they will have at least the following keys:

- `http_status` – The HTTP status code – matching the HTTP response status.
- `type` – The type of error – more specific than the http_status.
- `code` – The unique code for the error – this should be used for translations.
- `message` – The human readable error message.

```
{
  "http_status": "unprocessable_entity",
  "type": "not_found",
  "code": "product.not_found",
  "message": "Unable to find product with id='e0e92d34-aed9-4bb8-9107-89309370c4b'",
  "validation_errors": {}
}
```

### [​](https://developer.surecart.com/api-reference/errors#validation-errors) Validation Errors

If an error is due to object validation a validation_errors key will also be set within the error response. The validation errors response will be formatted like the example below, and each validation error will have the following keys:

- `attribute` – The attribute the validation error is associated with.
- `type` – The type of validation error.
- `code` – The unique code for the validation error – this should be used for translations.
- `options` – Any options that apply to this error – these can be used for translation interpolation. (For example, a numerical validation error might have options for min and max.)
- `message` – The human readable validation error message.

```
{
  "type": "unprocessable_entity",
  "code": "product.invalid",
  "message": "Failed to save product",
  "validation_errors": [\
    {\
      "attribute": "name",\
      "type": "blank",\
      "code": "product.name.blank",\
      "options": {},\
      "message": "can't be blank"\
    }\
  ]
}
```


===== SOURCE: api-reference-expanding-responses.md =====

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


===== SOURCE: api-reference-introduction.md =====

---
source_url: https://developer.surecart.com/api-reference/introduction
source: surecart-developer-docs
scraped: true
---

[Skip to main content](https://developer.surecart.com/api-reference/introduction#content-area)

> ## Documentation Index
>
> Fetch the complete documentation index at: [https://developer.surecart.com/llms.txt](https://developer.surecart.com/llms.txt)
>
> Use this file to discover all available pages before exploring further.

The SureCart API is organized around REST. Our API has predictable resource-oriented URLs, accepts form-encoded request bodies, returns JSON-encoded responses, and uses standard HTTP response codes, authentication, and verbs.


===== SOURCE: api-reference-metadata.md =====

---
source_url: https://developer.surecart.com/api-reference/metadata
source: surecart-developer-docs
scraped: true
---

[Skip to main content](https://developer.surecart.com/api-reference/metadata#content-area)

> ## Documentation Index
>
> Fetch the complete documentation index at: [https://developer.surecart.com/llms.txt](https://developer.surecart.com/llms.txt)
>
> Use this file to discover all available pages before exploring further.

Some SureCart objects (i.e. Checkout and Product) have a metadata parameter. You can use this parameter to attach key-value data to these objects.You can specify up to 50 keys, with key names up to 40 characters long and values up to 500 characters long.Metadata is useful for storing additional, structured information on an object. Metadata is not used by SureCart and won't be seen by your users unless you choose to show it to them.Do not store any sensitive information (bank account numbers, card details, etc.) as metadata.


===== SOURCE: api-reference-modes.md =====

---
source_url: https://developer.surecart.com/api-reference/modes
source: surecart-developer-docs
scraped: true
---

[Skip to main content](https://developer.surecart.com/api-reference/modes#content-area)

> ## Documentation Index
>
> Fetch the complete documentation index at: [https://developer.surecart.com/llms.txt](https://developer.surecart.com/llms.txt)
>
> Use this file to discover all available pages before exploring further.

When creating `Checkout`, `PaymentIntent`, `Subscription`, etc. objects you can specify `live_mode`. If you set `live_mode=false` then all interactions with processors will be done in their respective live or sandbox modes. This allows you to create test charges, subscriptions, and run full checkout flows without charging real payment methods.


===== SOURCE: api-reference-pagination.md =====

---
source_url: https://developer.surecart.com/api-reference/pagination
source: surecart-developer-docs
scraped: true
---

[Skip to main content](https://developer.surecart.com/api-reference/pagination#content-area)

> ## Documentation Index
>
> Fetch the complete documentation index at: [https://developer.surecart.com/llms.txt](https://developer.surecart.com/llms.txt)
>
> Use this file to discover all available pages before exploring further.

SureCart utilizes offset-based pagination, and all top-level API resources have support for bulk fetches via "list" API methods. For instance, you can list products, prices, and customers. These list API methods share a common structure, taking at least these two parameters: `limit`, and `page`. The default pagination limit is `20` and the max is `100`.By default, all list API methods return collections sorted by `created_at` in `desc` order. The sort order can be adjusted by passing the `sort` parameter. The format for this parameter is `?sort=column:order` which allows you to specify the value to sort by and the order. For example, if you wanted to sort by `updated_at` in `asc` order you would set the parameter to `?sort=updated_at:asc`.All list API methods can be sorted by `created_at` and `updated_at` values. Some API endpoints can be sorted by other values, and these methods have further documentation on the sort parameter.


===== SOURCE: api-reference-rate-limiting.md =====

---
source_url: https://developer.surecart.com/api-reference/rate-limiting
source: surecart-developer-docs
scraped: true
---

[Skip to main content](https://developer.surecart.com/api-reference/rate-limiting#content-area)

> ## Documentation Index
>
> Fetch the complete documentation index at: [https://developer.surecart.com/llms.txt](https://developer.surecart.com/llms.txt)
>
> Use this file to discover all available pages before exploring further.

The SureCart API uses a number of safeguards against bursts of incoming traffic to help maximize its stability. If you send many requests in quick succession, you might see error responses with status code 429.

### [​](https://developer.surecart.com/api-reference/rate-limiting#api-limiters) API Limiters

We have several limiters in the API, including a rate limiter and a concurrency limiter. Treat the limits as maximums, and don't generate unnecessary load. To prevent abuse, we might reduce the limits.You can request a limit increase to enable a high-traffic application by contacting SureCart Support.

### [​](https://developer.surecart.com/api-reference/rate-limiting#rate-limits) Rate Limits

The basic rate limiter restricts the number of API requests as follows:Default Limit: 150 operations / 10 secondsSensitive Endpoints: 10 operations / 1 minutePublic Endpoints: 60 operations / 1 minuteSensitive endpoints include those that may trigger notifications or call third-party services. In general, these are endpoints that should not be called frequently.Public endpoints are those that are accessible with a public API key. For example, our license check endpoint.


===== SOURCE: api-reference-webhooks.md =====

---
source_url: https://developer.surecart.com/api-reference/webhooks
source: surecart-developer-docs
scraped: true
---

[Skip to main content](https://developer.surecart.com/api-reference/webhooks#content-area)

> ## Documentation Index
>
> Fetch the complete documentation index at: [https://developer.surecart.com/llms.txt](https://developer.surecart.com/llms.txt)
>
> Use this file to discover all available pages before exploring further.

SureCart uses webhooks to notify your application when an event happens in your account. Webhooks are particularly useful for asynchronous events like when a subscription is updated or a charge is refunded.You can create and manage your webhook endpoints through the API endpoints or within your dashboard. From your dashboard you can also see a log of recent events that have been sent.

### [​](https://developer.surecart.com/api-reference/webhooks#events) Events

Webhooks are triggered based on events. Events are our way of letting you know when something interesting happens in your account. When an interesting event occurs, we create a new `Event` object. For example, when an order is created, we create a `order.created` event.The request payload of each webhook will contain the `Event` object, which is structured like the following example.

```
{
  "id": "5bafe7b7-a4e3-4a7d-85e9-d8b512094b67",
  "object": "event",
  "data": {
    "object": {
      "id": "0d6edf76-98f3-441c-9c43-81a92e929988",
      "object": "order",
      "live_mode": true,
      "number": "0008",
      "order_type": "checkout",
      "statement_url": "https://app.surecart.com/statements/orders/0d6edf76-98f3-441c-9c43-81a92e929988",
      "status": "paid",
      "checkout": "f1a38ad4-f87d-4550-b2e0-91a128cadf06",
      "created_at": 1664479758,
      "updated_at": 1664479758
    }
  },
  "type": "order.created",
  "account": "b7cfbc09-371a-453e-ab29-2edf63de0dbe",
  "created_at": 1664479758
}
```

When listeneing for webhooks at your webhook endpoint you will want to look at the `event.type` value to determine what type of event your endpoint has received. For example, the above webhook is a `order.created` event.

### [​](https://developer.surecart.com/api-reference/webhooks#types-of-events) Types of Events

This is a list of all the types of events we currently send. We may add more at any time, so in developing and maintaining your code, you should not assume that only these types exist.You'll notice that these events follow a pattern: `resource.event`. Our goal is to design a consistent system that makes things easier to anticipate and code against.

#### [​](https://developer.surecart.com/api-reference/webhooks#abandoned-checkouts) Abandoned Checkouts

- `abandoned_checkout.created` \- Occurs when an abandoned checkout is created
- `abandoned_checkout.recovered` \- Occurs when an abandoned checkout is recovered

#### [​](https://developer.surecart.com/api-reference/webhooks#accounts) Accounts

- `account.updated` \- Occurs when a account is updated

#### [​](https://developer.surecart.com/api-reference/webhooks#activations) Activations

- `activation.created` \- Occurs when a license activation is created
- `activation.deleted` \- Occurs when a license activation is deleted
- `activation.updated` \- Occurs when a license activation is updated

### [​](https://developer.surecart.com/api-reference/webhooks#affiliations) Affiliations

- `affiliation.activated` \- Occurs when a affiliation is activated
- `affiliation.deactivated` \- Occurs when a affiliation is deactivated
- `affiliation.deleted` \- Occurs when a affiliation is deleted

#### [​](https://developer.surecart.com/api-reference/webhooks#affiliation-requests) Affiliation Requests

- `affiliation_request.approved` \- Occurs when a affiliation request's status changes to `approved`
- `affiliation_request.created` \- Occurs when a affiliation request is created
- `affiliation_request.denied` \- Occurs when a affiliation status changes to `denied`
- `affiliation_request.updated` \- Occurs when a affiliation request is updated

#### [​](https://developer.surecart.com/api-reference/webhooks#bumps) Bumps

- `bump_offer.accepted` \- Occurs when a bump is accepted

#### [​](https://developer.surecart.com/api-reference/webhooks#cancellation-acts) Cancellation Acts

- `cancellation_act.created` \- Occurs when a cancellation act is created
- `cancellation_act.updated` \- Occurs when a cancellation act is updated

#### [​](https://developer.surecart.com/api-reference/webhooks#customers) Customers

- `customer.created` \- Occurs when a customer is created
- `customer.updated` \- Occurs when a customer is updated

#### [​](https://developer.surecart.com/api-reference/webhooks#fulfillments) Fulfillments

- `fulfillment.created` \- Occurs when a fulfillment is created
- `fulfillment.deleted` \- Occurs when a fulfillment is deleted
- `fulfillment.updated` \- Occurs when a fulfillment is updated

#### [​](https://developer.surecart.com/api-reference/webhooks#invoices) Invoices

- `invoice.created` \- Occurs when an invoice is created
- `invoice.deleted` \- Occurs when an invoice is deleted
- `invoice.updated` \- Occurs when an invoice is updated
- `invoice.made_draft` \- Occurs when an invoice's status changes to `draft`
- `invoice.opened` \- Occurs when an invoice's status changes to `open`
- `invoice.paid` \- Occurs when an invoice's status changes to `paid`

#### [​](https://developer.surecart.com/api-reference/webhooks#orders) Orders

- `order.created` \- Occurs when an order is created
- `order.delivered` \- Occurs when an order's shipment status changes to `delivered`
- `order.fulfilled` \- Occurs when an order's fulfillment status changes to `fulfilled`
- `order.made_processing` \- Occurs when an order's status changes to `processing`
- `order.paid` \- Occurs when an order's status changes to `paid`
- `order.partially_fulfilled` \- Occurs when an order's fulfillment status changes to `partially_fulfilled`
- `order.partially_shipped` \- Occurs when an order's shipment status changes to `partially_shipped`
- `order.payment_failed` \- Occurs when an order's status changes to `payment_failed`
- `order.shipped` \- Occurs when an order's shipment status changes to `shipped`
- `order.unfulfilled` -Occurs when an order's fulfillment status changes to `unfulfilled`
- `order.unshipped` \- Occurs when an order's shipment status changes to `unshipped`
- `order.voided` \- Occurs when an order's status changes to `void`

#### [​](https://developer.surecart.com/api-reference/webhooks#payout-groups) Payout Groups

- `payout_group.created` \- Occurs when a payout group is created

#### [​](https://developer.surecart.com/api-reference/webhooks#payouts) Payouts

- `payout.created` \- Occurs when a payout is created
- `payout.completed` \- Occurs when a payout's status changes to `completed`
- `payout.made_processing` \- Occurs when a payout's status changes to `processing`

#### [​](https://developer.surecart.com/api-reference/webhooks#prices) Prices

- `price.created` \- Occurs when a price is created
- `price.deleted` \- Occurs when a price is deleted
- `price.updated` \- Occurs when a price is updated

#### [​](https://developer.surecart.com/api-reference/webhooks#products) Products

- `product.created` \- Occurs when a product is created
- `product.deleted` \- Occurs when a product is deleted
- `product.stock_adjusted` \- Occurs when the `stock` amount for a product is adjusted by an order, return, etc.
- `product.updated` \- Occurs when a product is updated
- `variant.stock_adjusted` \- Occurs when the `stock` amount for a product's variant is adjusted by an order, return, etc. (If a product has variants this webhook will be sent instead of `product.stock_adjusted`.)

#### [​](https://developer.surecart.com/api-reference/webhooks#purchases) Purchases

- `purchase.created` \- Occurs when a purchase is created
- `purchase.invoked` \- Occurs when a purchase is invoked
- `purchase.revoked` \- Occurs when a purchase is revoked
- `purchase.updated` \- Occurs when a purchase is updated

#### [​](https://developer.surecart.com/api-reference/webhooks#referrals) Referrals

- `referral.approved`\- Occurs when a referral's status changes to `approved`
- `referral.canceled`\- Occurs when a referral's status changes to `canceled`
- `referral.created`\- Occurs when a referral is created
- `referral.denied`\- Occurs when a referral's status changes to `denied`
- `referral.made_reviewing`\- Occurs when a referral's status changes to `reviewing`
- `referral.updated`\- Occurs when a referral is updated

#### [​](https://developer.surecart.com/api-reference/webhooks#refunds) Refunds

- `refund.created` \- Occurs when a refund is created
- `refund.succeeded` \- Occurs when a refund's status changes to `succeeded`

#### [​](https://developer.surecart.com/api-reference/webhooks#return-requests) Return Requests

- `return_request.completed` \- Occurs when a return request's status changes to `completed`
- `return_request.created` \- Occurs when a return request is created
- `return_request.deleted` \- Occurs when a return request is deleted
- `return_request.opened` \- Occurs when a return request's status changes to `open`
- `return_request.updated` \- Occurs when a return request is updated

#### [​](https://developer.surecart.com/api-reference/webhooks#subscriptions) Subscriptions

- `subscription.canceled` \- Occurs when a subscription's status changes to `canceled`
- `subscription.created` \- Occurs when a subscription is created
- `subscription.completed` \- Occurs when a subscription's status changes to `completed`
- `subscription.made_active` \- Occurs when a subscription's status changes to `active`
- `subscription.made_trialing` \- Occurs when a subscription's status changes to `trialing`
- `subscription.renewal_reminder_sent` \- Occurs when a subscription's renewal reminder is sent
- `subscription.renewed` \- Occurs when a subscription renews
- `subscription.set_to_cancel` \- Occurs when a subscription is set to cancel at the end of the current billing period
- `subscription.updated` \- Occurs when a subscription is updated

#### [​](https://developer.surecart.com/api-reference/webhooks#upsells) Upsells

- `upsell_offer.accepted` \- Occurs when a upsell is accepted
- `upsell_offer.declined` \- Occurs when a upsell is declined

### [​](https://developer.surecart.com/api-reference/webhooks#webhook-delivery-timeouts) Webhook Delivery Timeouts

SureCart expects webhook endpoints to acknowledge receipt of an event within **approximately 10 seconds**. If a response is not received within this time window, the delivery attempt is considered failed and will be retried based on our retry strategy.To ensure successful processing:

- Your endpoint should return a `2xx` HTTP status code as quickly as possible.
- Perform all time-consuming logic (e.g., database updates, third-party API calls) asynchronously in the background.
- Avoid long-running synchronous operations that could cause the request to time out.

Proper timeout handling helps ensure reliable event delivery and minimizes duplicate webhook attempts caused by delays.

### [​](https://developer.surecart.com/api-reference/webhooks#expanding-webhook-events) Expanding Webhook Events

All webhooks contain the parent resource of the corresponding event and do not expand any related objects. This keeps webhook payloads small and ensures unecessary data is not being sent.If you wish to expand a resource you will need to make a subsequent retrieve request with the expansions you need. [See the Expanding Responses documentation for more detail.](https://developer.surecart.com/reference/expanding-responses)

### [​](https://developer.surecart.com/api-reference/webhooks#webhook-signatures) Webhook Signatures

All webhooks include a signature in each request's `x-webhook-signature` header. This allows you to verify that the events were sent by us, and not by a third party. We generate signatures using a hash-based message authentication code (HMAC) with SHA-256.We generate a unique signing secret key for each endpoint. If you use multiple endpoints, you must use the unique signing secret for each one you want to verify signatures on. You can view the signing secret for each endpoint from within your dashboard, or you can retrive it from the API.

### [​](https://developer.surecart.com/api-reference/webhooks#preventing-replay-attacks) Preventing Replay Attacks

A replay attack is when an attacker intercepts a valid payload and its signature, then re-transmits them. To mitigate such attacks, we include a timestamp in the `x-webhook-timestamp` header. This timestamp is also part of the signed payload and verified by the signature, so an attacker cannot change the timestamp without invalidating the signature. If the signature is valid but the timestamp is too old, you can have your application reject the payload.We generate the timestamp and signature each time we send an event to your endpoint. If we retry an event (for example, your endpoint previously replied with a non-2xx status code), then we generate a new signature and timestamp for the new delivery attempt.

### [​](https://developer.surecart.com/api-reference/webhooks#verify-signatures) Verify Signatures

**Step 1: Extract Signature and Timestamp**

The `signature` is sent in the `x-webhook-signature` header, and the `timestamp` is sent in the `x-webhook-timestamp` header.

```
x-webhook-signature = "287ace7f0267943970dca9e895be11a739b532b85dfed8a3d147ca2d08267f48"
x-webhook-timestamp = "1641873601"
```

**Step 2: Prepare Signed Payload String**

The signed_payload string is created by concatenating the timestamp and the payload with the . character.**Step 3: Determine Expected Signature**

Compute an HMAC with the SHA256 hash function. Use the endpoint's signing secret as the key, and use the signed_payload string as the message.**Step 4: Compare Signatures**

Compare the signature in the header to the expected signature.

### [​](https://developer.surecart.com/api-reference/webhooks#event-ordering) Event Ordering

SureCart does not guarantee that webhook events will be delivered in the exact order they were triggered. For example, when a customer completes a checkout, the following events might be sent:

```
order.created

purchase.created

subscription.created
```

While these events are generated in a specific sequence, they may arrive at your webhook endpoint out of order due to network latency or retries.Your webhook handler should not rely on receiving events in a strict sequence. Instead, it should be designed to handle events independently and idempotently. If necessary, use the SureCart API to retrieve related objects (such as an order, purchase, or subscription) when processing an event. This ensures that your integration remains consistent even when events arrive asynchronously or out of order.

### [​](https://developer.surecart.com/api-reference/webhooks#handling-duplicate-events) Handling Duplicate Events

Webhook endpoints may occasionally receive the same event more than once. This can happen due to retries or network-related issues. To prevent processing duplicates, we recommend storing the unique id of each received event. Before acting on a new event, check if its ID has already been handled.In some cases, two distinct webhook events may reference the same underlying object. To identify true duplicates, compare both the `event -> type` and the `event -> data -> object -> id` fields. This helps ensure your system processes each meaningful event only once.

### [​](https://developer.surecart.com/api-reference/webhooks#subscribe-only-to-relevant-events) Subscribe Only to Relevant Events

To improve performance and reduce unnecessary load on your webhook endpoint, configure it to listen only to the events your integration actually needs. Subscribing to all available events increases overhead and may lead to unnecessary processing.You can configure which events your webhook receives directly from the SureCart Dashboard


===== SOURCE: documentation-actions-filters-admin.md =====

---
source_url: https://developer.surecart.com/documentation/actions-filters/admin
source: surecart-developer-docs
scraped: true
---

[Skip to main content](https://developer.surecart.com/documentation/actions-filters/admin#content-area)

> ## Documentation Index
>
> Fetch the complete documentation index at: [https://developer.surecart.com/llms.txt](https://developer.surecart.com/llms.txt)
>
> Use this file to discover all available pages before exploring further.

These filters allow you to customize the WordPress admin experience for SureCart.

## [​](https://developer.surecart.com/documentation/actions-filters/admin#menu-filters) Menu Filters

### [​](https://developer.surecart.com/documentation/actions-filters/admin#surecart_menu_priority) `surecart_menu_priority`

Filter the admin menu position. Lower numbers appear higher in the menu.

```
add_filter( 'surecart_menu_priority', function( $priority ) {
    return 5; // Move menu higher (closer to Dashboard)
} );

// Or move it lower
add_filter( 'surecart_menu_priority', function( $priority ) {
    return 80; // Move below Settings
} );
```

## [​](https://developer.surecart.com/documentation/actions-filters/admin#admin-bar-filters) Admin Bar Filters

### [​](https://developer.surecart.com/documentation/actions-filters/admin#surecart_show_admin_bar_visit_store) `surecart_show_admin_bar_visit_store`

Control whether "Visit Store" appears in the admin bar.

```
add_filter( 'surecart_show_admin_bar_visit_store', '__return_false' );

// Or show only for specific roles
add_filter( 'surecart_show_admin_bar_visit_store', function( $show ) {
    return current_user_can( 'manage_options' );
} );
```

### [​](https://developer.surecart.com/documentation/actions-filters/admin#surecart_show_admin_bar_new_content) `surecart_show_admin_bar_new_content`

Control whether "New" content menu appears in admin bar.

```
add_filter( 'surecart_show_admin_bar_new_content', '__return_false' );
```

### [​](https://developer.surecart.com/documentation/actions-filters/admin#surecart/help_widget/show) `surecart/help_widget/show`

Control when the help widget is shown.

```
add_filter( 'surecart/help_widget/show', function( $show ) {
    // Hide for non-admins
    return current_user_can( 'manage_options' );
} );

// Or always hide
add_filter( 'surecart/help_widget/show', '__return_false' );
```

### [​](https://developer.surecart.com/documentation/actions-filters/admin#surecart/help_widget/loaded) `surecart/help_widget/loaded`

Fired when the help widget is loaded in the admin. Use this to inject custom scripts or modify widget behavior.

```
add_action( 'surecart/help_widget/loaded', function() {
    // Add custom help resources or modify widget behavior
    ?>
    <script>
        // Customize help widget
    </script>
    <?php
} );
```

## [​](https://developer.surecart.com/documentation/actions-filters/admin#sync-filters) Sync Filters

### [​](https://developer.surecart.com/documentation/actions-filters/admin#surecart_get_post_type_post) `surecart_get_{post_type}_post`

Filter the synced post lookup result. Replace `{post_type}` with the actual post type (e.g., `sc_product`).

```
add_filter( 'surecart_get_sc_product_post', function( $post, $model_id, $service ) {
    // Custom post lookup logic
    return $post;
}, 10, 3 );
```

### [​](https://developer.surecart.com/documentation/actions-filters/admin#surecart_excluded_post_meta_keys) `surecart_excluded_post_meta_keys`

Filter meta keys excluded from sync.

```
add_filter( 'surecart_excluded_post_meta_keys', function( $keys ) {
    $keys[] = 'my_excluded_key';
    $keys[] = '_custom_meta';
    return $keys;
} );
```

## [​](https://developer.surecart.com/documentation/actions-filters/admin#use-cases) Use Cases

### [​](https://developer.surecart.com/documentation/actions-filters/admin#hide-admin-features-for-shop-managers) Hide Admin Features for Shop Managers

```
// Hide help widget for non-admins
add_filter( 'surecart/help_widget/show', function( $show ) {
    return current_user_can( 'manage_options' );
} );

// Hide admin bar links for shop managers
add_filter( 'surecart_show_admin_bar_new_content', function( $show ) {
    return current_user_can( 'manage_options' );
} );
```

### [​](https://developer.surecart.com/documentation/actions-filters/admin#simplify-admin-interface) Simplify Admin Interface

```
// Hide all dropdowns for a cleaner interface
add_filter( 'surecart/disable_product_collection_dropdown', '__return_true' );
add_filter( 'surecart/disable_fulfillment_dropdown', '__return_true' );
add_filter( 'surecart/disable_shipment_dropdown', '__return_true' );
```

### [​](https://developer.surecart.com/documentation/actions-filters/admin#customize-menu-position) Customize Menu Position

```
// Move SureCart menu right after Dashboard
add_filter( 'surecart_menu_priority', function( $priority ) {
    return 3;
} );
```

## [​](https://developer.surecart.com/documentation/actions-filters/admin#related) Related

## Templates

Hook into admin and template actions.

## Requests

Modify API requests and responses.


===== SOURCE: documentation-actions-filters-cart.md =====

---
source_url: https://developer.surecart.com/documentation/actions-filters/cart
source: surecart-developer-docs
scraped: true
---

[Skip to main content](https://developer.surecart.com/documentation/actions-filters/cart#content-area)

> ## Documentation Index
>
> Fetch the complete documentation index at: [https://developer.surecart.com/llms.txt](https://developer.surecart.com/llms.txt)
>
> Use this file to discover all available pages before exploring further.

These filters allow you to customize the cart experience.

## [​](https://developer.surecart.com/documentation/actions-filters/cart#sc_cart_menu_icon) `sc_cart_menu_icon`

Filter the cart menu icon.

Parameters: `$icon` (string) — The icon name/identifier. `$type` (string) — The icon type or position context.

```
add_filter( 'sc_cart_menu_icon', function( $icon, $type ) {
    return 'shopping-bag'; // Use a different icon
}, 10, 2 );
```

## [​](https://developer.surecart.com/documentation/actions-filters/cart#sc_cart_disabled) `sc_cart_disabled`

Disable the cart functionality entirely on specific pages or conditions.

```
add_filter( 'sc_cart_disabled', function( $disabled ) {
    // Disable cart on specific pages
    if ( is_page( 'landing-page' ) ) {
        return true;
    }
    return $disabled;
} );

// Or disable during maintenance
add_filter( 'sc_cart_disabled', function( $disabled ) {
    if ( get_option( 'maintenance_mode' ) ) {
        return true;
    }
    return $disabled;
} );
```

## [​](https://developer.surecart.com/documentation/actions-filters/cart#use-cases) Use Cases

### [​](https://developer.surecart.com/documentation/actions-filters/cart#hide-cart-on-landing-pages) Hide Cart on Landing Pages

```
add_filter( 'sc_cart_disabled', function( $disabled ) {
    // Hide cart on specific landing pages
    $landing_pages = [ 'promo', 'special-offer', 'webinar' ];

    foreach ( $landing_pages as $slug ) {
        if ( is_page( $slug ) ) {
            return true;
        }
    }

    return $disabled;
} );
```

### [​](https://developer.surecart.com/documentation/actions-filters/cart#disable-cart-for-logged-out-users) Disable Cart for Logged-Out Users

```
add_filter( 'sc_cart_disabled', function( $disabled ) {
    // Only show cart to logged-in users
    return ! is_user_logged_in();
} );
```


===== SOURCE: documentation-actions-filters-checkout.md =====

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


===== SOURCE: documentation-actions-filters-currency.md =====

---
source_url: https://developer.surecart.com/documentation/actions-filters/currency
source: surecart-developer-docs
scraped: true
---

[Skip to main content](https://developer.surecart.com/documentation/actions-filters/currency#content-area)

> ## Documentation Index
>
> Fetch the complete documentation index at: [https://developer.surecart.com/llms.txt](https://developer.surecart.com/llms.txt)
>
> Use this file to discover all available pages before exploring further.

These filters allow you to customize how currency amounts are formatted and displayed throughout SureCart.

## [​](https://developer.surecart.com/documentation/actions-filters/currency#surecart/currency/format) `surecart/currency/format`

Filter the formatted currency string. This is the final output that users see.

Parameters: `$formatted` (string) — The formatted currency string (e.g., "$19.99"). `$amount`(int) — The amount in cents.`$currency_code` (string) — The currency code (e.g., 'USD', 'EUR').

```
add_filter( 'surecart/currency/format', function( $formatted, $amount, $currency_code ) {
    // Add custom prefix
    return 'Price: ' . $formatted;
}, 10, 3 );
```

## [​](https://developer.surecart.com/documentation/actions-filters/currency#surecart/currency/locale) `surecart/currency/locale`

Filter the locale used for currency formatting.

```
add_filter( 'surecart/currency/locale', function( $locale ) {
    return get_locale();
} );
```

## [​](https://developer.surecart.com/documentation/actions-filters/currency#surecart/currency/max_cents) `surecart/currency/max_cents`

Filter the maximum number of decimal places shown.

```
add_filter( 'surecart/currency/max_cents', function( $decimals, $amount, $converted ) {
    // Always show 2 decimal places
    return 2;
}, 10, 3 );
```

## [​](https://developer.surecart.com/documentation/actions-filters/currency#surecart/currency/filter_url) `surecart/currency/filter_url`

Disable URL-based currency switching (for full-page caching compatibility).

```
add_filter( 'surecart/currency/filter_url', '__return_false' );
```

## [​](https://developer.surecart.com/documentation/actions-filters/currency#surecart/display_amount/free) `surecart/display_amount/free`

Filter the text displayed for $0 prices.

```
add_filter( 'surecart/display_amount/free', function( $text ) {
    return 'No Cost';
} );
```

## [​](https://developer.surecart.com/documentation/actions-filters/currency#surecart/currency_switcher/label) `surecart/currency_switcher/label`

Filter the currency switcher label text.

```
add_filter( 'surecart/currency_switcher/label', function( $label ) {
    return strtolower( $label );
} );
```


===== SOURCE: documentation-actions-filters-customers.md =====

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


===== SOURCE: documentation-actions-filters-errors.md =====

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


===== SOURCE: documentation-actions-filters-integrations.md =====

---
source_url: https://developer.surecart.com/documentation/actions-filters/integrations
source: surecart-developer-docs
scraped: true
---

[Skip to main content](https://developer.surecart.com/documentation/actions-filters/integrations#content-area)

> ## Documentation Index
>
> Fetch the complete documentation index at: [https://developer.surecart.com/llms.txt](https://developer.surecart.com/llms.txt)
>
> Use this file to discover all available pages before exploring further.

**These are low-level actions for integration configuration changes.**

If you are wanting to create a full purchase integration that handles granting access, refunds, upgrades, downgrades and more, please follow the [Purchase Integration Guide](https://developer.surecart.com/documentation/orders-and-purchases).

These actions fire when a merchant configures or removes product integrations in the SureCart admin. Product integrations are the automated actions that occur when a product is purchased—such as changing a user's WordPress role, enrolling them in a course, or adding them to a membership group.

## [​](https://developer.surecart.com/documentation/actions-filters/integrations#surecart/integrations/create) `surecart/integrations/create`

Fired when a merchant **adds** an integration to a product.

Parameters: `$params` (array) — The integration parameters including provider, model, and configuration.

```
add_action( 'surecart/integrations/create', function( $params ) {
    error_log( 'Integration created: ' . print_r( $params, true ) );

    if ( ! empty( $params['provider'] ) ) {
        wp_mail(
            get_option( 'admin_email' ),
            'New Product Integration Added',
            sprintf( 'A %s integration was added to a product.', $params['provider'] )
        );
    }
} );
```

## [​](https://developer.surecart.com/documentation/actions-filters/integrations#surecart/integrations/delete) `surecart/integrations/delete`

Fired when a merchant **removes** an integration from a product.

```
add_action( 'surecart/integrations/delete', function( $params ) {
    error_log( 'Integration deleted: ' . print_r( $params, true ) );
} );
```


===== SOURCE: documentation-actions-filters-login.md =====

---
source_url: https://developer.surecart.com/documentation/actions-filters/login
source: surecart-developer-docs
scraped: true
---

[Skip to main content](https://developer.surecart.com/documentation/actions-filters/login#content-area)

> ## Documentation Index
>
> Fetch the complete documentation index at: [https://developer.surecart.com/llms.txt](https://developer.surecart.com/llms.txt)
>
> Use this file to discover all available pages before exploring further.

These filters allow you to customize the login and authentication experience.

## [​](https://developer.surecart.com/documentation/actions-filters/login#sc_login_redirect_url) `sc_login_redirect_url`

Filter the redirect URL after login.

```
add_filter( 'sc_login_redirect_url', function( $url ) {
    // Redirect to custom dashboard
    return home_url( '/my-account/' );
} );

// Or redirect based on user role
add_filter( 'sc_login_redirect_url', function( $url ) {
    $user = wp_get_current_user();

    if ( in_array( 'subscriber', $user->roles ) ) {
        return home_url( '/member-dashboard/' );
    }

    return $url;
} );
```

## [​](https://developer.surecart.com/documentation/actions-filters/login#disable-password-nag) Disable Password Nag

Control whether new users see the password change nag after their account is created with a random, temporary password.

```
add_filter( 'get_user_metadata', function( $value, $object_id, $meta_key, $single ) {
    if ( 'default_password_nag' === $meta_key ) {
        return ''; // Return empty to prevent password nag from showing
    }
    return $value;
}, 10, 4 );
```

## [​](https://developer.surecart.com/documentation/actions-filters/login#use-cases) Use Cases

### Role-Based Redirects

```
add_filter( 'sc_login_redirect_url', function( $url ) {
    $user = wp_get_current_user();

    if ( in_array( 'administrator', $user->roles ) ) {
        return admin_url();
    }

    if ( in_array( 'sc_member', $user->roles ) ) {
        return home_url( '/members/' );
    }

    return home_url( '/my-account/' );
} );
```


===== SOURCE: documentation-actions-filters-media.md =====

---
source_url: https://developer.surecart.com/documentation/actions-filters/media
source: surecart-developer-docs
scraped: true
---

[Skip to main content](https://developer.surecart.com/documentation/actions-filters/media#content-area)

> ## Documentation Index
>
> Fetch the complete documentation index at: [https://developer.surecart.com/llms.txt](https://developer.surecart.com/llms.txt)
>
> Use this file to discover all available pages before exploring further.

These filters allow you to customize how media elements like videos and image galleries are displayed throughout SureCart.

## [​](https://developer.surecart.com/documentation/actions-filters/media#video-filters) Video Filters

### [​](https://developer.surecart.com/documentation/actions-filters/media#surecart/product-video-poster/size) `surecart/product-video-poster/size`

```
add_filter( 'surecart/product-video-poster/size', function( $size ) {
    return 'full';
} );
```

### [​](https://developer.surecart.com/documentation/actions-filters/media#surecart_video_html) `surecart_video_html`

Filter the video HTML output for complete customization.

Parameters: `$html` (string), `$video` (array — src, poster, dimensions), `$media` (object), `$metadata` (array — duration, codec, etc.)

```
add_filter( 'surecart_video_html', function( $html, $video, $media, $metadata ) {
    return sprintf(
        '<div class="custom-video-player" data-src="%s" data-poster="%s"></div>',
        esc_url( $video['src'] ),
        esc_url( $video['poster'] ?? '' )
    );
}, 10, 4 );
```

## [​](https://developer.surecart.com/documentation/actions-filters/media#image-gallery-filters) Image Gallery Filters

### [​](https://developer.surecart.com/documentation/actions-filters/media#surecart/image-slider/active-breakpoint) `surecart/image-slider/active-breakpoint`

```
add_filter( 'surecart/image-slider/active-breakpoint', function( $breakpoint ) {
    return 768;
} );
```

## Use Cases

### Custom Video Player Integration

```
add_filter( 'surecart_video_html', function( $html, $video, $media, $metadata ) {
    wp_enqueue_script( 'plyr' );
    wp_enqueue_style( 'plyr' );

    return sprintf(
        '<video class="plyr" playsinline controls data-poster="%s">
            <source src="%s" type="video/mp4" />
        </video>',
        esc_url( $video['poster'] ?? '' ),
        esc_url( $video['src'] )
    );
}, 10, 4 );
```


===== SOURCE: documentation-actions-filters-models.md =====

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


===== SOURCE: documentation-actions-filters-orders.md =====

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


===== SOURCE: documentation-actions-filters-prices.md =====

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


===== SOURCE: documentation-actions-filters-products.md =====

---
source_url: https://developer.surecart.com/documentation/actions-filters/products
source: surecart-developer-docs
scraped: true
---

[Skip to main content](https://developer.surecart.com/documentation/actions-filters/products#content-area)

> ## Documentation Index
>
> Fetch the complete documentation index at: [https://developer.surecart.com/llms.txt](https://developer.surecart.com/llms.txt)
>
> Use this file to discover all available pages before exploring further.

These hooks allow you to respond to product events and customize how products are displayed.

## [​](https://developer.surecart.com/documentation/actions-filters/products#actions) Actions

### `surecart/product_created`

```
add_action( 'surecart/product_created', function( $product, $data ) {
    wp_remote_post( SLACK_WEBHOOK_URL, [
        'body' => json_encode([ 'text' => sprintf( '🆕 New product created: %s', $product->name ) ]),
    ]);
}, 10, 2 );
```

### `surecart/product_updated`

```
add_action( 'surecart/product_updated', function( $product, $data ) {
    // Sync updated product info to external system
}, 10, 2 );
```

### `surecart/product_deleted`

```
add_action( 'surecart/product_deleted', function( $product, $data ) {
    wp_remote_request( 'https://api.crm.example.com/products/' . $product->id, [
        'method'  => 'DELETE',
        'headers' => [ 'Authorization' => 'Bearer ' . CRM_API_KEY ],
    ]);
}, 10, 2 );
```

### `surecart/product_stock_adjusted`

Fires when a product's stock level changes.

| Property          | Description                                         |
| ----------------- | --------------------------------------------------- |
| `stock`           | Total on-hand inventory count                       |
| `held_stock`      | Units purchased but not yet fulfilled/shipped       |
| `available_stock` | Units available for purchase (`stock - held_stock`) |

```
add_action( 'surecart/product_stock_adjusted', function( $product, $data ) {
    if ( $product->available_stock <= 5 && $product->available_stock > 0 ) {
        wp_remote_post( SLACK_WEBHOOK_URL, [
            'body' => json_encode([
                'text' => sprintf(
                    '⚠️ Low stock: %s has %d available (%d on hand, %d held)',
                    $product->name, $product->available_stock, $product->stock, $product->held_stock
                )
            ]),
        ]);
    }
}, 10, 2 );
```

## [​](https://developer.surecart.com/documentation/actions-filters/products#filters) Filters

### `surecart/product/replace_content_with_product_info_part`

```
add_filter( 'surecart/product/replace_content_with_product_info_part', '__return_false' );
```

### `sc_product_post_type_link_sc_collection`

Control which collection slug appears in product URLs when the permalink includes `%sc_collection%`.

```
add_filter( 'sc_product_post_type_link_sc_collection', function( $term, $terms, $post ) {
    // Use the first collection assigned to the product
    return $terms[0] ?? $term;
}, 10, 3 );
```

### `surecart/product-line-item-image/fallback_src`

```
add_filter( 'surecart/product-line-item-image/fallback_src', function( $src, $product ) {
    return get_template_directory_uri() . '/images/placeholder.png';
}, 10, 2 );
```

### `surecart_product_page_query_args`

```
add_filter( 'surecart_product_page_query_args', function( $args ) {
    if ( current_user_can( 'manage_options' ) ) {
        $args['post_status'] = [ 'publish', 'draft', 'private' ];
    }
    return $args;
} );
```


===== SOURCE: documentation-actions-filters-purchases.md =====

---
source_url: https://developer.surecart.com/documentation/actions-filters/purchases
source: surecart-developer-docs
scraped: true
---

[Skip to main content](https://developer.surecart.com/documentation/actions-filters/purchases#content-area)

> ## Documentation Index
>
> Fetch the complete documentation index at: [https://developer.surecart.com/llms.txt](https://developer.surecart.com/llms.txt)
>
> Use this file to discover all available pages before exploring further.

**Important: These are low-level filters for purchase events.**

If you are wanting to create a full purchase integration that handles refunds, upgrades, downgrades and more, please follow the [Purchase Integration Guide](https://developer.surecart.com/documentation/orders-and-purchases)

These actions are triggered throughout the purchase lifecycle, including:

- **Checkout** — When a customer completes a purchase
- **Refunds** — When a purchase is refunded and access is revoked
- **Upgrades/Downgrades** — When a customer switches to a different product
- **Quantity changes** — When a customer adjusts the quantity of their purchase
- **Subscription cancellations** — When a subscription ends and access is revoked
- **Subscription restorations** — When a canceled subscription is reactivated

## [​](https://developer.surecart.com/documentation/actions-filters/purchases#surecart/purchase_created) `surecart/purchase_created`

Fired when a new purchase is created after a successful checkout.

Parameters: `$purchase` (`\SureCart\Models\Purchase`) — contains product, customer, quantity, and other purchase details.

```
add_action( 'surecart/purchase_created', function( $purchase ) {
    $product = sc_get_product( $purchase->product );
    $user = $purchase->getWPUser();

    if ( empty($user) || empty($product->name) ) {
        return;
    }

    wp_mail(
        $user->user_email,
        'Welcome!',
        sprintf(
            "Hi %s, thank you for purchasing %s!",
            $user->display_name,
            $product->name
        )
    );
} );
```

## [​](https://developer.surecart.com/documentation/actions-filters/purchases#surecart/purchase_invoked) `surecart/purchase_invoked`

Fired when a purchase is invoked (access is granted). This happens when a subscription is restored, or when manually invoking access.

```
add_action( 'surecart/purchase_invoked', function( $purchase ) {
    $user = $purchase->getWPUser();
    if ( $user ) {
        wp_mail( $user->user_email, 'Access Restored', 'Your access has been restored.' );
    }
} );
```

## [​](https://developer.surecart.com/documentation/actions-filters/purchases#surecart/purchase_revoked) `surecart/purchase_revoked`

Fired when a purchase is revoked (access is removed). This happens when a subscription is canceled or when manually revoking access.

```
add_action( 'surecart/purchase_revoked', function( $purchase ) {
    $user = $purchase->getWPUser();
    if ( $user ) {
        wp_mail(
            $user->user_email,
            'Access Revoked',
            'Your subscription has been canceled and access has been removed.'
        );
    }
} );
```

## [​](https://developer.surecart.com/documentation/actions-filters/purchases#surecart/purchase_updated) `surecart/purchase_updated`

Fired when a purchase is updated, due to upgrade, downgrade, quantity change, or price change.

Parameters: `$purchase` (`\SureCart\Models\Purchase`), `$request` (object — webhook request with `data->object` and `data->previous_attributes`).

```
add_action( 'surecart/purchase_updated', function( $purchase, $request ) {
    $user = $purchase->getWPUser();
    if ( $user ) {
        wp_mail( $user->user_email, 'Purchase Updated', 'Your purchase has been successfully modified.' );
    }
}, 10, 2 );
```


===== SOURCE: documentation-actions-filters-requests.md =====

---
source_url: https://developer.surecart.com/documentation/actions-filters/requests
source: surecart-developer-docs
scraped: true
---

[Skip to main content](https://developer.surecart.com/documentation/actions-filters/requests#content-area)

> ## Documentation Index
>
> Fetch the complete documentation index at: [https://developer.surecart.com/llms.txt](https://developer.surecart.com/llms.txt)
>
> Use this file to discover all available pages before exploring further.

These filters allow you to intercept and modify data before it's sent to the SureCart API, and transform responses as they come back.

## [​](https://developer.surecart.com/documentation/actions-filters/requests#surecart/request/model) `surecart/request/model`

Filter the model instance before an API request is made.

Parameters: `$model` (Model instance being sent to the API), `$request` (WP_REST_Request).

```
// Add metadata to every checkout
add_filter( 'surecart/request/model', function( $model, $request ) {
    if ( ! $model instanceof \SureCart\Models\Checkout ) {
        return $model;
    }

    $model['metadata'] = array_merge(
        (array) ( $model['metadata'] ?? [] ),
        [
            'source'       => 'wordpress',
            'utm_source'   => $_GET['utm_source'] ?? null,
            'utm_medium'   => $_GET['utm_medium'] ?? null,
            'utm_campaign' => $_GET['utm_campaign'] ?? null,
        ]
    );

    return $model;
}, 10, 2 );
```

## [​](https://developer.surecart.com/documentation/actions-filters/requests#surecart/request/response) `surecart/request/response`

Filter the API response after it's received.

Parameters: `$response` (mixed), `$args` (array — HTTP request arguments), `$endpoint` (string).

```
add_filter( 'surecart/request/response', function( $response, $args, $endpoint ) {
    if ( strpos( $endpoint, 'customers' ) === false ) {
        return $response;
    }

    if ( is_object( $response ) && ! empty( $response->email ) ) {
        $wp_user = get_user_by( 'email', $response->email );
        if ( $wp_user ) {
            $response->wp_user_id = $wp_user->ID;
            $response->wp_roles = $wp_user->roles;
        }
    }

    return $response;
}, 10, 3 );
```

## [​](https://developer.surecart.com/documentation/actions-filters/requests#surecart/request/args) `surecart/request/args`

Filter the HTTP request arguments before sending.

```
add_filter( 'surecart/request/args', function( $args, $endpoint ) {
    if ( strpos( $endpoint, 'exports' ) !== false ) {
        $args['timeout'] = 120;
    }
    return $args;
}, 10, 2 );
```

## [​](https://developer.surecart.com/documentation/actions-filters/requests#surecart/request/endpoint) `surecart/request/endpoint`

Filter the API endpoint URL before the request is made.

```
add_filter( 'surecart/request/endpoint', function( $endpoint, $args ) {
    if ( defined( 'WP_DEBUG' ) && WP_DEBUG ) {
        error_log( 'SureCart API: ' . $endpoint );
    }
    return $endpoint;
}, 10, 2 );
```


===== SOURCE: documentation-actions-filters-seo.md =====

---
source_url: https://developer.surecart.com/documentation/actions-filters/seo
source: surecart-developer-docs
scraped: true
---

[Skip to main content](https://developer.surecart.com/documentation/actions-filters/seo#content-area)

> ## Documentation Index
>
> Fetch the complete documentation index at: [https://developer.surecart.com/llms.txt](https://developer.surecart.com/llms.txt)
>
> Use this file to discover all available pages before exploring further.

These filters allow you to customize SEO-related behavior in SureCart, including meta tags, Open Graph data, and structured data (JSON-LD schema).

## [​](https://developer.surecart.com/documentation/actions-filters/seo#meta-tags) Meta Tags

### `surecart/noindex_query_vars`

Filter the query variables that trigger a `noindex` meta tag on product pages.

```
add_filter( 'surecart/noindex_query_vars', function( $vars ) {
    $vars[] = 'ref';
    $vars[] = 'affiliate_id';
    $vars[] = 'utm_source';
    $vars[] = 'utm_medium';
    return $vars;
} );
```

### `sc_display_product_seo_meta`

Control whether SureCart outputs its built-in SEO meta tags for product pages. Return `false` when using a dedicated SEO plugin.

Parameters: `$display` (bool), `$product` (`\SureCart\Models\Product`).

```
// Disable for Yoast SEO
add_filter( 'sc_display_product_seo_meta', function( $display, $product ) {
    if ( defined( 'WPSEO_VERSION' ) ) {
        return false;
    }
    return $display;
}, 10, 2 );

// Disable for Rank Math
add_filter( 'sc_display_product_seo_meta', function( $display, $product ) {
    if ( class_exists( 'RankMath' ) ) {
        return false;
    }
    return $display;
}, 10, 2 );

// Disable entirely
add_filter( 'sc_display_product_seo_meta', '__return_false' );
```

### `surecart/og:image/size`

Filter the WordPress image size used for Open Graph and Twitter Card tags. Default: `'full'`.

```
add_filter( 'surecart/og:image/size', function( $size ) {
    return 'large';
} );
```

## [​](https://developer.surecart.com/documentation/actions-filters/seo#product-schema) Product Schema

### `sc_display_product_json_ld_schema`

Control whether JSON-LD schema markup is output for products. Disable when using a third-party SEO plugin that generates product schema.

```
add_filter( 'sc_display_product_json_ld_schema', '__return_false' );
```

## [​](https://developer.surecart.com/documentation/actions-filters/seo#yoast-seo-integration) Yoast SEO Integration

### `sc_wpseo_frontend_presenters`

Filter the Yoast SEO presenters that SureCart uses on product pages.

```
add_filter( 'sc_wpseo_frontend_presenters', function( $title_presenters, $presenters ) {
    // Use all available Yoast presenters
    return $presenters;
}, 10, 2 );
```


===== SOURCE: documentation-actions-filters-subscriptions.md =====

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


===== SOURCE: documentation-actions-filters-templates.md =====

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


===== SOURCE: documentation-actions-reference.md =====

---
source_url: https://developer.surecart.com/documentation/actions-reference
source: surecart-developer-docs
scraped: true
---

[Skip to main content](https://developer.surecart.com/documentation/actions-reference#content-area)

> ## Documentation Index
>
> Fetch the complete documentation index at: [https://developer.surecart.com/llms.txt](https://developer.surecart.com/llms.txt)
>
> Use this file to discover all available pages before exploring further.

SureCart provides extensive WordPress hooks (actions and filters) that allow you to extend and customize its functionality. Use these hooks to build integrations, modify behavior, and customize the shopping experience.

## [​](https://developer.surecart.com/documentation/actions-reference#actions-&-filters-by-topic) Actions & Filters by Topic

[**Purchases** \\
\\
Hook into purchase lifecycle events like creation, access grants, and\\
revocations.](https://developer.surecart.com/documentation/actions-filters/purchases)

[**Checkout** \\
\\
Validate checkout forms, customize payment modes, and track conversions.](https://developer.surecart.com/documentation/actions-filters/checkout)

[**Cart** \\
\\
Customize cart icon visibility and behavior.](https://developer.surecart.com/documentation/actions-filters/cart)

[**Login** \\
\\
Customize login redirects and authentication behavior.](https://developer.surecart.com/documentation/actions-filters/login)

[**Products** \\
\\
Respond to product creation, updates, deletion, and stock changes.](https://developer.surecart.com/documentation/actions-filters/products)

[**Prices** \\
\\
Hook into price creation, updates, and deletion events.](https://developer.surecart.com/documentation/actions-filters/prices)

[**Customers** \\
\\
Respond to customer profile updates and sync with external systems.](https://developer.surecart.com/documentation/actions-filters/customers)

[**Subscriptions** \\
\\
Hook into subscription renewals and lifecycle events.](https://developer.surecart.com/documentation/actions-filters/subscriptions)

[**Orders** \\
\\
Respond to orders, charges, refunds, and invoices.](https://developer.surecart.com/documentation/actions-filters/orders)

[**Models** \\
\\
Hook into model lifecycle events like create, update, and delete.](https://developer.surecart.com/documentation/actions-filters/models)

[**Integrations** \\
\\
Build integrations that respond to purchases and refunds.](https://developer.surecart.com/documentation/actions-filters/integrations)

[**Templates** \\
\\
Inject content into SureCart templates and admin pages.](https://developer.surecart.com/documentation/actions-filters/templates)

[**Requests** \\
\\
Modify API requests, endpoints, and responses.](https://developer.surecart.com/documentation/actions-filters/requests)

[**Currency** \\
\\
Customize currency formatting, locales, and display.](https://developer.surecart.com/documentation/actions-filters/currency)

[**Media** \\
\\
Customize media handling and image display.](https://developer.surecart.com/documentation/actions-filters/media)

[**Errors** \\
\\
Customize error handling and messages.](https://developer.surecart.com/documentation/actions-filters/errors)

[**Admin** \\
\\
Customize admin menus, toolbars, and list tables.](https://developer.surecart.com/documentation/actions-filters/admin)

[**SEO** \\
\\
Customize SEO metadata and structured data.](https://developer.surecart.com/documentation/actions-filters/seo)

## [​](https://developer.surecart.com/documentation/actions-reference#building-integrations) Building Integrations

[**Orders & Purchases Guide** \\
\\
Build full-featured integrations using SureCart's Integration class. Handles\\
purchases, refunds, upgrades, downgrades, and quantity changes automatically.](https://developer.surecart.com/documentation/orders-and-purchases)


===== SOURCE: documentation-add-to-cart.md =====

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


===== SOURCE: documentation-admin-ui.md =====

---
source_url: https://developer.surecart.com/documentation/admin-ui
source: surecart-developer-docs
scraped: true
---

[Skip to main content](https://developer.surecart.com/documentation/admin-ui#content-area)

> ## Documentation Index
>
> Fetch the complete documentation index at: [https://developer.surecart.com/llms.txt](https://developer.surecart.com/llms.txt)
>
> Use this file to discover all available pages before exploring further.

If you want to add custom UI elements to admin pages of SureCart like Order, Product, Customer, Affiliate pages etc. you can use this API to add either in the Main or the Sidebar area.

# [​](https://developer.surecart.com/documentation/admin-ui#page-metaboxes) Page Metaboxes

To add metaboxes to individual pages, you will need to register an addon, client-side using react.

### Registering an Addon

Call the `registerAddon` function from the global `window.surecart` object. Parameters: `name` (string, required), `settings` (object, required — `render` (HTML/React component), `scope` ("main" or "sidebar"), `title` (string)).

```
import SidebarComponent from "./SidebarComponent";

window.surecart.registerAddon("custom-sidebar", {
  render: () => <SidebarComponent />,
  scope: "sidebar",
  title: "Custom Sidebar Box",
});
```

### Getting Page Data

SureCart uses [WordPress Core Data](https://developer.wordpress.org/block-editor/reference-guides/data/data-core/) (WordPress' flavor of Redux).

#### Get The Current Page ID

```
const id = window.surecart.getCurrentPageId();
```

#### Querying an Order

```
import { useSelect } from "@wordpress/data";
import { store } from "@wordpress/core-data";

const order = useSelect(
  (select) =>
    select(store).getEntityRecord("surecart", "order", id, {
      expand: ["checkout"],
    }),
  [id]
);
```

#### Querying A Product

```
import { useSelect } from "@wordpress/data";
import { store } from "@wordpress/core-data";

const product = useSelect(
  (select) =>
    select(store).getEntityRecord("surecart", "product", id, {
      expand: ["prices", "variants"],
    }),
  [id]
);
```

# [​](https://developer.surecart.com/documentation/admin-ui#admin-list-tables) Admin List Tables

Add custom columns to list table views in its admin pages (Orders, Products, Invoices, etc.) using WordPress's `manage_{$post_type}_posts_columns` functions.

### Step 1 — Add the column

```
add_filter( 'manage_sc-products_columns', 'my_custom_column' );

function my_custom_column( $columns ) {
    $columns['metabox'] = 'Metabox';
    return $columns;
}
```

### Step 2 — Add the column content

`$data` is the model object for the current row.

```
add_action( 'manage_sc-products_custom_column', 'my_custom_column_content', 10, 2 );

function my_custom_column_content( $column_name, $data ) {
    if ( 'metabox' === $column_name ) {
        echo esc_html( $data->id );
    }
}
```

Pages available: `sc-orders`, `sc-products`, etc. (found in the URL `page` parameter).


===== SOURCE: documentation-custom-loops.md =====

---
source_url: https://developer.surecart.com/documentation/custom-loops
source: surecart-developer-docs
scraped: true
---

[Skip to main content](https://developer.surecart.com/documentation/custom-loops#content-area)

> ## Documentation Index
>
> Fetch the complete documentation index at: [https://developer.surecart.com/llms.txt](https://developer.surecart.com/llms.txt)
>
> Use this file to discover all available pages before exploring further.

Querying products utilizes the "WordPress Loop". Specify the `sc_product` post type in the query.

## [​](https://developer.surecart.com/documentation/custom-loops#simple-query-example) Simple Query Example

```
$products = new WP_Query(
  array(
    'post_type'      => 'sc_product',
    'posts_per_page' => 10,
  )
);
```

## [​](https://developer.surecart.com/documentation/custom-loops#getting-product-data-from-the-post) Getting Product Data From The Post

### In the loop

Use `sc_get_product()` after calling `$products->the_post()`:

```
$products = new WP_Query(
  array(
    'post_type'      => 'sc_product',
    'posts_per_page' => 10,
  )
);

if ( $products->have_posts() ) :
  while ( $products->have_posts() ) :
    $products->the_post();

    $product = sc_get_product();

    echo esc_html( $product->display_amount );

    if ( $product->is_out_of_stock ) {
      echo 'Out of stock!';
    }

    if ( $product->is_low_stock ) {
      echo 'Only ' . (int) $product->available_stock . ' left!';
    }
  endwhile;
endif;
```

### Outside the loop

```
$posts = get_posts(
  array(
    'post_type'      => 'sc_product',
    'posts_per_page' => 10,
  )
);

foreach($posts as $post) {
  $product = sc_get_product( $post );
  echo esc_html( $product->display_amount );
}
```

## [​](https://developer.surecart.com/documentation/custom-loops#querying-variant-options) Querying Variant Options

### Single variant option

```
$products = new WP_Query(
  [
    'post_type'      => 'sc_product',
    'posts_per_page' => 10,
    'variant_options' => [
      [
        'name' => 'Color',
        'values' => 'Orange'
      ]
    ]
  ]
);
```

### Multiple variant options (AND)

```
$products = new WP_Query(
  [
    'post_type'      => 'sc_product',
    'posts_per_page' => 10,
    'variant_options' => [
      'relation' => 'AND',
      [ 'name' => 'Color', 'values' => 'Orange' ],
      [ 'name' => 'Size', 'values' => 'Small' ]
    ]
  ]
);
```

### Multiple variant options (OR)

```
$products = new WP_Query(
  [
    'post_type'      => 'sc_product',
    'posts_per_page' => 10,
    'variant_options' => [
      'relation' => 'OR',
      [ 'name' => 'Color', 'values' => 'Orange' ],
      [ 'name' => 'Size', 'values' => ['Small', 'Medium'] ]
    ]
  ]
);
```


===== SOURCE: documentation-orders-and-purchases.md =====

---
source_url: https://developer.surecart.com/documentation/orders-and-purchases
source: surecart-developer-docs
scraped: true
---

[Skip to main content](https://developer.surecart.com/documentation/orders-and-purchases#content-area)

> ## Documentation Index
>
> Fetch the complete documentation index at: [https://developer.surecart.com/llms.txt](https://developer.surecart.com/llms.txt)
>
> Use this file to discover all available pages before exploring further.

Integrating with sophisticated pricing structures can be complex. SureCart abstracts away many of the complexities by extending an integration PHP class. You implement what you want to do when a purchase is created, invoked, or revoked.

## [​](https://developer.surecart.com/documentation/orders-and-purchases#purchases) Purchases

A purchase is the state of what a customer currently should have "access" to. It is tied 1:1 to a product, price, and optionally a variant.

# [​](https://developer.surecart.com/documentation/orders-and-purchases#purchase-lifecycle) Purchase Lifecycle

### Purchase Created

Created the first time a customer completes an order, or when upgrading/downgrading a subscription. Typically, this is when an integration provides "access" to something.

### Purchase Revoked

Can be revoked manually by the Merchant or automatically (subscription canceled/expired, or plan change). When a new purchase is created for an upgrade/downgrade, the old purchase is revoked.

### Purchase Invoked

A purchase is 'invoked' when a previously revoked purchase is un-revoked. Great for restoration scenarios — e.g., you only want to send a welcome email on first purchase, not on reinstatement.

## [​](https://developer.surecart.com/documentation/orders-and-purchases#example-creating-a-user-role-switcher) Example: Creating A User Role Switcher

### Step 1 — Extend IntegrationService

```
<?php

namespace MyPlugin\Integrations;

use SureCart\Integrations\Contracts\IntegrationInterface;
use SureCart\Integrations\Contracts\PurchaseSyncInterface;
use SureCart\Integrations\IntegrationService;

class UserRoleChangeIntegration extends IntegrationService implements IntegrationInterface, PurchaseSyncInterface {
}
```

### Step 2 — Set the integration details

```
public function getName() { return 'my-plugin/user-role-change'; }
public function getModel() { return 'product'; }
public function getLogo() { return esc_url_raw( trailingslashit( plugin_dir_url( __FILE__ ) ) . 'icon.svg' ); }
public function getLabel() { return __( 'Change WordPress User Role', 'surecart' ); }
public function getItemLabel() { return __( 'Change User Role', 'surecart' ); }
public function getItemHelp() { return __( 'Change the user role of the user who purchased the product.', 'surecart' ); }
```

### Step 3 — Populate the integration item chooser

`getItems()` must return arrays with `id` and `label`. `getItem($id)` returns a single item.

```
public function getItems( $items = [], $search = '' ) {
    $roles          = [];
    $editable_roles = wp_roles()->roles;
    foreach ( $editable_roles as $role => $details ) {
        $sub['id']      = esc_attr( $role );
        $sub['label']   = translate_user_role( $details['name'] );
        $roles[ $role ] = $sub;
    }
    return $roles;
}

public function getItem( $id ) {
    return [ 'id' => $id, 'label' => wp_roles()->get_names()[ $id ] ];
}
```

### Step 4 — Handle purchase lifecycle events

`$integration->integration_id` is the saved `id` from `getItem`/`getItems`.

```
public function onPurchaseCreated( $integration, $wp_user ) {
    $this->toggleRole( $integration->integration_id, $wp_user, true );
}

public function onPurchaseInvoked( $integration, $wp_user ) {
    $this->onPurchaseCreated( $integration, $wp_user );
}

public function onPurchaseRevoked( $integration, $wp_user ) {
    $this->toggleRole( $integration->integration_id, $wp_user, false );
}

public function toggleRole( $role, $wp_user, $add = true ) {
    $role_object = get_role( $role );
    if ( ! $role_object ) { return; }
    return $add ? $wp_user->add_role( $role ) : $wp_user->remove_role( $role );
}
```

Optional methods: `onPurchaseQuantityUpdated()`, `onPurchaseProductAdded()`, `onPurchaseProductRemoved()`. If not defined, `onPurchaseCreated`/`onPurchaseRevoked` are called as fallback.

### Step 5 — Bootstrap the integration

```
(new \MyPlugin\Integrations\UserRoleChangeIntegration())->bootstrap();
```


===== SOURCE: documentation-php-models.md =====

---
source_url: https://developer.surecart.com/documentation/php-models
source: surecart-developer-docs
scraped: true
---

[Skip to main content](https://developer.surecart.com/documentation/php-models#content-area)

> ## Documentation Index
>
> Fetch the complete documentation index at: [https://developer.surecart.com/llms.txt](https://developer.surecart.com/llms.txt)
>
> Use this file to discover all available pages before exploring further.

**PHP Models = API Interface** — The PHP models provide a fluent, Laravel-like interface to the SureCart REST API. Each model corresponds directly to an API resource.

**Blocking HTTP requests** — Each model query makes a synchronous HTTP request to the SureCart API. Use in: AJAX/REST handlers, admin dashboard pages, WP-CLI commands, cron jobs. Avoid in front-end page rendering.

# [​](https://developer.surecart.com/documentation/php-models#retrieving) Retrieving

### Find by ID

```
use SureCart\Models\Product;
$product = Product::find('8ba8d60f-5277-4e6b-807c-dee8166446d5');
```

### Get multiple

```
$products = Product::get();
foreach ($products as $product) {
    echo $product->name;
}
```

### Where (query by parameters — match API endpoint query params)

```
$archived_products = Product::where(['archived' => false])->get();
```

### Paginate

```
$products = Product::where(['archived' => false])->paginate(['per_page' => 20, 'page' => 2]);
```

Returns: `['object', 'pagination' => ['count', 'limit', 'page'], 'data' => [...]]`

### First

```
$product = Product::where(['archived' => false])->first();
```

### Refresh

```
$freshProduct = $product->fresh(); // re-fetch, doesn't affect existing instance
$product->refresh();               // re-hydrate existing instance
```

# [​](https://developer.surecart.com/documentation/php-models#expanding-relations) Expanding Relations

### Single relation

```
$prices = \SureCart\Models\Price::with(['product'])->paginate(['page' => 1]);
```

### List relations

```
$products = \SureCart\Models\Product::with(['prices'])->paginate(['page' => 1]);
```

### Recursive / nested expansion

```
$orders = \SureCart\Models\Order::with([
   'checkout',
   'checkout.line_items',
   'line_item.price',
   'price.product'
])->paginate(['page' => 1]);
```

Max depth: 2 levels, max 10 objects per request. Works on `get`, `paginate`, `create`, and `update`.

# [​](https://developer.surecart.com/documentation/php-models#inserting-updating-and-deleting) Inserting, Updating, and Deleting

```
// Create
$product = Product::create(['name' => 'iPhone', 'description' => '...']);

// Update (static)
Product::update(['id' => $product_id, 'name' => 'iPhone Pro']);

// Update (instance)
$product = Product::find($product_id);
$product->name = 'iPhone Pro';
$product->save();

// Delete
$product->delete();
// or
Product::delete($product_id);
```

# [​](https://developer.surecart.com/documentation/php-models#error-handling) Error Handling

```
$product = Product::find('invalid-id');
if (is_wp_error($product)) {
    $error_message = $product->get_error_message();
    return;
}
echo $product->name;
```

# [​](https://developer.surecart.com/documentation/php-models#utility-methods) Utility Methods

```
$product->toArray();       // Convert to array
$product->toObject();      // Convert to stdClass
$product['name'];          // Array access (equivalent to $product->name)
$product->isDirty();       // true if unsaved changes
$product->getDirty();      // ['name' => 'New Name']
```

# [​](https://developer.surecart.com/documentation/php-models#available-models) Available Models (namespace: `SureCart\Models`)

**Products:** `Product`, `Price`, `ProductCollection`, `ProductGroup`, `ProductMedia`, `Variant`, `VariantOption`, `Bump`, `Upsell`, `UpsellFunnel`, `Swap`, `Download`, `Coupon`, `Promotion`

**Customers:** `Customer`, `BalanceTransaction`

**Orders & Payments:** `Order`, `Checkout`, `AbandonedCheckout`, `LineItem`, `Purchase`, `Charge`, `Invoice`, `Refund`, `PaymentIntent`, `PaymentMethod`, `ManualPaymentMethod`, `Processor`, `Fee`, `Dispute`

**Subscriptions:** `Subscription`, `Period`, `CancellationAct`, `CancellationReason`

**Shipping & Fulfillment:** `Fulfillment`, `FulfillmentItem`, `ShippingMethod`, `ShippingProfile`, `ShippingRate`, `ShippingZone`, `ReturnRequest`, `ReturnItem`

**Tax:** `TaxRegistration`, `TaxZone`

**Licensing:** `License`, `Activation`

**Affiliates:** `Affiliation`, `AffiliationRequest`, `AffiliationProduct`, `Referral`, `ReferralItem`, `Payout`, `PayoutGroup`, `Click`

**Media:** `Media`

**Account & Settings:** `Account`, `Brand`, `Webhook`

**Reviews:** `Review`

**Other:** `Event`, `Export`


===== SOURCE: documentation-styling-checkout.md =====

---
source_url: https://developer.surecart.com/documentation/styling/checkout
source: surecart-developer-docs
scraped: true
---

[Skip to main content](https://developer.surecart.com/documentation/styling/checkout#content-area)

> ## Documentation Index
>
> Fetch the complete documentation index at: [https://developer.surecart.com/llms.txt](https://developer.surecart.com/llms.txt)
>
> Use this file to discover all available pages before exploring further.

SureCart checkout components use a [shadow DOM](https://developer.mozilla.org/en-US/docs/Web/Web_Components/Using_shadow_DOM) to encapsulate their styles. This protects against style conflicts and keeps components stable as internal HTML structure evolves.

Two customization methods: **CSS custom properties (variables)** for global style changes and **CSS parts** for fine-grained component styling.

## [​](https://developer.surecart.com/documentation/styling/checkout#css-variables) CSS Variables

Scope to `:root:root` to ensure specificity inside shadow DOM:

```
:root:root {
  /** Remove all border radiuses */
  --sc-border-radius-small: 0;
  --sc-border-radius-medium: 0;
  --sc-border-radius-large: 0;
  --sc-border-radius-x-large: 0;
}
```

### Key variable groups

**Colors:** `--sc-color-primary-500`, `--sc-color-gray-{50-950}`, `--sc-color-neutral-{50-950}`, `--sc-color-success-{50-950}`, `--sc-color-info-{50-950}`, `--sc-color-warning-{50-950}`, `--sc-color-danger-{50-950}`

**Border Radius:** `--sc-border-radius-small`, `--sc-border-radius-medium`, `--sc-border-radius-large`, `--sc-border-radius-x-large`, `--sc-border-radius-circle`, `--sc-border-radius-pill`

**Spacing:** `--sc-spacing-{xxx-small through xxxx-large}`

**Typography:** `--sc-font-sans`, `--sc-font-size-{xx-small through xxxx-large}`, `--sc-font-weight-{light/normal/semibold/bold}`

**Inputs:** `--sc-input-height-{small/medium/large}`, `--sc-input-border-color`, `--sc-input-border-color-focus`, `--sc-input-background-color`, etc.

## [​](https://developer.surecart.com/documentation/styling/checkout#css-parts) CSS Parts

CSS Parts allow targeting specific parts of a component's shadow DOM using `::part()`. Find available parts in the [Components Documentation](https://components.surecart.com/) under "Shadow Parts" for each component.

### Input/Text Field example

```
sc-input {
  --sc-font-sans: monospace;
  --sc-color-primary-500: #2dd4bf;
}
sc-input::part(base) {
  border: 1px solid black;
  box-shadow: 2px 2px #2dd4bf;
  border-radius: 0;
}
sc-input::part(label) {
  color: black;
  font-size: 14px;
  letter-spacing: 2px;
  text-transform: uppercase;
}
sc-input::part(base):hover {
  box-shadow: 5px 5px #2dd4bf;
}
```

### Button example

```
sc-button::part(base) {
  border-radius: 0;
  background: white;
  font-family: monospace;
  border: 1px solid black;
  box-shadow: 2px 2px #2dd4bf;
  color: black;
}
sc-button::part(base):hover {
  background: #2dd4bf;
}
```

### Shipping Address example

```
sc-order-shipping-address {
  --sc-font-sans: monospace;
  --sc-address-column-spacing: 1em;
  --sc-color-primary-500: #2dd4bf;
}
sc-order-shipping-address::part(input__base),
sc-order-shipping-address::part(select__base) {
  border: 1px solid black;
  border-radius: 0;
  box-shadow: 2px 2px #2dd4bf;
}
```


===== SOURCE: guides-variant-swatches.md =====

---
source_url: https://developer.surecart.com/guides/variant-swatches
source: surecart-developer-docs
scraped: true
---

# Variant Swatches

Guide: transform variant option pills into visual image swatches using variant images assigned to each variant.

Prerequisite: assign images to your variants first (see Variant Images documentation in the SureCart docs).

## How it works

The code hooks into render_block to intercept the surecart/product-variant-pill block. It replaces the text pill with a thumbnail from the variant's assigned image. Clicking a swatch updates the product gallery image.

## Implementation summary

Add to functions.php or a custom plugin. Set the variable at the top to your variant option name (default: "color").

Key steps in the implementation:

1. Hook into render_block with priority 10 and 3 arguments
2. Check blockName equals surecart/product-variant-pill and the block context name matches the target option
3. Call sc_get_product() to retrieve the current product
4. Filter product->gallery to find images whose variant_option metadata matches the pill value
5. Use WP_HTML_Tag_Processor to set a CSS background-image style on the pill div (56px x 56px by default)
6. Add CSS classes: sc-variant-color-swatch, plus data-wp-class attributes for selected and disabled states
7. Wrap in a flex column div (sc-variant-color-wrapper)

Full source code available at: https://developer.surecart.com/guides/variant-swatches

## Customization options

- Change variant option name: set the variable to "size", "material", etc.
- Show variant labels: uncomment the name div below each swatch
- Adjust swatch size: modify width and height in the inline style (default 56px)

## CSS for selected and disabled states

Selected swatch: add border-color and box-shadow using the brand green (#00824c).

Disabled/unavailable swatch: set opacity to 0.4 and cursor to not-allowed.

Target class names: sc-variant-color-swatch--selected and sc-variant-color-swatch--disabled.


===== SOURCE: affiliate-marketing.md =====

---
source_url: https://surecart.com/features/affiliate-marketing/
source: surecart-developer-docs
scraped: true
---

# Affiliate Platform — Start an Affiliate Program for Your Store

Everything you need to run an affiliate program for your WordPress store. Track referrals, manage commissions, handle payouts, and give affiliates their own dashboard, all built directly into SureCart's eCommerce platform.

## Commission Types

### Single Purchase Commissions

Pay affiliates a percentage of each sale or a fixed amount per order. If a refund happens before payout, commissions adjust automatically.

### Recurring Commissions

Give affiliates commission every time a customer renews their subscription. Helpful for memberships, SaaS and subscription products.

### Lifetime Commissions

Turn your affiliates into long-term growth partners by rewarding future purchases from their referred customers.

### Custom Affiliate Commissions

Set different commission rates for different products. Increase commission value for high-priority products or affiliates.

## Referral Tracking

Every affiliate gets their own referral link with built-in tracking for clicks, referrals, and conversions.

- Unique referral links
- Configurable referral windows
- First-click or last-click attribution
- Up to 10 landing page URLs
- External tracking script support

## Affiliate Portal

Affiliates can track clicks, referrals, commissions, and payout history from their own dashboard.

- Click tracking
- Referral tracking
- Payout history
- Profile management
- Custom portal branding
- Custom portal/domain support

## Payouts

See what every affiliate is owed, create individual or batch payouts, set minimum payout thresholds, and export payout data for accounting.

- Individual payouts
- Batch payouts
- Minimum payout thresholds
- Export payout records
- Centralized payout management

## Coupon Tracking

Track affiliate referrals through links and coupon codes together, making it easier to run creator and influencer campaigns.

- Affiliate-linked coupon codes
- Coupon attribution tracking
- Links + coupons work together
- Zero-commission referral tracking

## Advanced Management Features

**Affiliate Applications & Approval:** Approve affiliates automatically or manually. Add custom signup questions, collect payout emails, and require terms acceptance during onboarding.

**Attribution Beyond Clicks:** Manually assign affiliate credit to customers or subscriptions when needed, set referral attribution windows, and control how future purchases and renewals are attributed.

**Customize Affiliate Rules:** Set custom commission rates for affiliates or products, approve, deny or manage referrals, and control affiliate access.

## FAQ

**Do I need a separate affiliate plugin for WordPress?** No. SureCart includes affiliate management directly inside your eCommerce platform.

**Can affiliates earn recurring commissions for subscriptions?** Yes. SureCart supports recurring affiliate commissions for subscription renewals, memberships, SaaS products, and other recurring revenue businesses.

**Can I offer different commission rates for products or affiliates?** Yes. You can create custom commission rules for individual affiliates, specific products, or both.

**Can I track referrals with coupon codes?** Yes. You can assign coupon codes to affiliates and track referrals through both links and coupon codes together.

**What happens when an order is refunded?** If a refund happens before an affiliate payout is completed, the commission adjusts automatically.

**How do affiliate payouts work in SureCart?** You can create individual payouts or batch payouts directly from your dashboard and export payout data for accounting purposes.

**Can I set minimum payout thresholds?** Yes. SureCart lets you define minimum payout amounts before affiliates are included in batch payouts.


