---
source_url: https://surecart.com/docs/create-coupons
source: surecart-kb
scraped: true
---

# How To Create Coupons In SureCart

## Overview

SureCart enables merchants to create and manage discount coupons. The system supports various configuration options including discount types, duration settings, product restrictions, and redemption limits.

## Creating a New Coupon

Navigate to **SureCart > Coupons** in the WordPress dashboard and click **Add New**.

## Configuration Fields

**Coupon Name**: Internal identifier not visible to customers.

**Promotion Code**: Customer-facing code for checkout. Leave blank for automatic generation.

**Customer Restriction**: Optionally limit coupon to a specific customer via dropdown selection.

**Product Restrictions**: Restrict coupon to specific products, or leave blank for store-wide applicability. When a customer adds even just one of the products with the coupons restricted to the cart, the coupon is still applicable.

**Discount Amount**: Choose percentage or fixed dollar amount discount.

## Discount Duration Options

- **Forever**: Applies continuously
- **Once**: Single-use only
- **Multiple months**: Duration-based application varying by subscription type (monthly, weekly, or yearly subscriptions process differently)

## Redemption Limits

**Usage limit per coupon**: Maximum total uses across all customers

**Usage limit per customer**: Maximum uses per individual customer

**Minimum order subtotal**: Threshold amount required for coupon applicability

**End Date**: Expiration date and time (UTC+0)

Click **Create Coupon** to finalize.
