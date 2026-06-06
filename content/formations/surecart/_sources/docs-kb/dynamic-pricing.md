---
source_url: https://surecart.com/docs/dynamic-pricing
source: surecart-kb
scraped: true
---

/ [Knowledge Base](https://surecart.com/docs/)/ [Revenue Boosters](https://surecart.com/docs-category/revenue-booster/)/Dynamic Pricing

# Dynamic Pricing

This document explains what Dynamic Pricing is, how it works, and how to configure pricing rules using real-world examples.

Dynamic Pricing enables you to automatically apply discounts or fees during checkout based on specific conditions, such as cart value, product attributes, customer data, or shipping details.

## Requirements

- WordPress admin access
- SureCart installed and activated
- At least one published product
- Access to **SureCart → Promotions → Dynamic Pricing**

## Creating a Rule

Dynamic Pricing works through **rules**. Each rule defines:

- Where the pricing applies (Checkout, Line Item, or Shipping)
- When it applies in the purchase lifecycle (initial checkout, renewals, or both)
- Under which conditions it applies
- What adjustment is applied (discount or fee)

**Step-by-step:**

1. Go to **Promotions > Dynamic Pricing** and click **Add New**.
2. Enter a **Name** (internal reference) and **Display Name** (visible to customers).

## Using a Template Rule

SureCart provides pre-built templates for common use cases (e.g., Free Shipping Minimum, Subscription renewal discount).

When you create a rule using a template, the **When to Apply** option is automatically pre-selected based on the intended use case.

## When to Apply

This setting is **required** for all Dynamic Pricing rules.

- **All Transactions** — Applies to both initial checkout and future renewals/plan changes.
- **Initial checkout** — Applies only to the customer's first purchase.
- **Renewals & plan changes** — Applies to subscription renewals, upgrades, and downgrades.

## Adding Conditions

Conditions use logical AND/OR logic. Available attributes depend on the rule target (Line Item, Checkout, or Shipping).

**Line Item Schema attributes** include: Quantity, Subtotal Amount, SKU (Product/Variant), Product Name, Product Collection, WordPress User Role, Customer Order Count, Price Type, and more.

**Checkout Schema attributes** include: Subtotal Amount, Line Item Quantity, Order Type, Email, Shipping Amount, Selected Shipping Method Name, WordPress User Role, Customer Order Count, and more.

## Global Settings

Global Settings define how multiple discounts or fees are applied when more than one rule matches.

Available strategies:

- **All** — All matching rules apply
- **First** — Only the first matching rule applies
- **Smallest** — Only the smallest matching discount applies
- **Largest** — Only the largest matching discount applies

You can define different strategies for Checkout, Line items, and Shipping.

## FAQs

**Do Dynamic Pricing rules affect subscription renewals?**

It depends on the **When to Apply** setting. Choose Initial checkout, Renewals & plan changes, or All Transactions explicitly.

**What happens if multiple rules match?**

All matching rules are evaluated. The final behavior depends on your Global Settings configuration.

**Do Dynamic Pricing rules replace coupons?**

No. Dynamic Pricing applies automatically. Coupons require customer input and are managed separately.

**Can I schedule when a Dynamic Pricing rule is active?**

Yes. Each rule can have a start and end date.
