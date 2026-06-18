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
