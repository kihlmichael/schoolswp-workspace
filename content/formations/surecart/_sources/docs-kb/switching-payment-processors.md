---
source_url: https://surecart.com/docs/switching-payment-processors
source: surecart-kb
scraped: true
---

/ [Knowledge Base](https://surecart.com/docs/)/ [Payments](https://surecart.com/docs-category/payments/)/Switching Payment Processors

# Switching Payment Processors

When switching payment processors or connecting new accounts in SureCart, it's important to understand how subscriptions and payment methods will be impacted. This guide will walk you through the key points to consider and how to manage existing and new payment methods.

#### Key Concepts:

- **Active Mode (Test/Live):** While you can connect multiple Stripe accounts, you cannot have more than one mode (Test or Live) active at the same time. For example, you can have Live mode from one account active while Test mode is active on another.

- **inactive Processor**: A processor can be disabled while still connected to SureCart. In this state, it will not accept new payment methods, but existing subscriptions linked to that processor will continue to renew normally.

### Managing Existing Subscriptions

- **New Payment Methods**: When a new processor is activated, all new payment methods and subscriptions will be linked to that processor. However, existing subscriptions will continue using the payment method stored with the previous processor.
- **Existing Subscriptions**: Even if a processor is disabled, existing payment methods connected to it will still be charged. This ensures a smooth transition for ongoing subscriptions without service disruption.

### How to Change Processors in SureCart:

1. Go to the **Processors** page in your SureCart dashboard.

1. You can enable or disable processors as needed. When a processor is disabled, it will still handle renewals for existing subscriptions, but new payment methods will not be associated with it.
1. If you want all new payment methods to go to a new processor, ensure the new processor is **active** and the previous one is **disabled**. Remember, only one **mode** (Test or Live) can be active at a time.

For further assistance with migrating or managing payment processors, contact SureCart support.
