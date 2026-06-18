---
source_url: https://surecart.com/docs/failed-payments-purchase-behavior
source: surecart-kb
scraped: true
---

# How to Set Up Failed Payment and Purchase Behavior for Subscriptions

## Overview

SureCart enables you to configure what happens when subscription payments fail. These settings are found in **SureCart > Settings > Subscriptions** and consist of two main components: failed payment handling and purchase behavior options.

## Failed Payments Setup

When a customer's subscription payment fails, their subscription status changes to "Past Due." SureCart's intelligent retry system attempts another payment within a specified timeframe.

**Configuration Options:**

You can select from a dropdown menu to specify how long a subscription remains active after failed payments:

- One week
- Two weeks
- Three weeks

After the selected duration expires without successful payment, the subscription is automatically canceled. This feature gives customers time to update payment methods while protecting your revenue.

## Purchase Behavior Setup

This premium feature (requires account upgrade) provides three configurable options:

### 1. Require Upfront Payment Method

Enables "no credit card required" free trials, allowing customers to access trial periods without providing payment information upfront.

### 2. Prevent Duplicate Trials

When enabled, this prevents customers from receiving multiple trial periods for the same product. Returning customers are charged full price instead of receiving another trial.

### 3. Purchase Revoke Behavior

Specifies when to cancel a user's purchase, offering two choices:

- Immediate cancellation
- Cancellation after all payment methods have been retried

## Access Location

All settings are configurable at **SureCart > Settings > Subscriptions**

**Note:** These features require a premium SureCart account upgrade.
