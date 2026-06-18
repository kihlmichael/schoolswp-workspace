---
source_url: https://surecart.com/docs/migrate-to-surecart
source: surecart-kb
scraped: true
---

/ [Knowledge Base](https://surecart.com/docs/)/ [Migrating](https://surecart.com/docs-category/migrating/)/How to Migrate from Other Platforms to SureCart

# How to Migrate from Other Platforms to SureCart

This document outlines the recommended sequence of steps to migrate an existing eCommerce store from another platform to SureCart. Each step links to a detailed guide for that specific stage of the migration.

## **Migration Overview**

The migration process is divided into the following steps. Following them in order is recommended, since some steps depend on data created in earlier ones.

1. Set up the store
2. Configure branding and notifications
3. Connect payment processors
4. Import customers
5. Import products
6. Import purchases
7. Import active subscriptions
8. Synchronize WordPress users with SureCart

## **Step 1: Set Up the Store**

- Install and activate SureCart. Refer to [How to Install SureCart](https://surecart.com/docs/installing-surecart/).
- Configure store details (name, currency, address, and others). Refer to [How to Update Store Details](https://surecart.com/docs/update-store-details/).

## **Step 2: Configure Branding and Notifications**

- Configure brand colors and logo. Refer to [How to Set Up Branding in SureCart](https://surecart.com/docs/set-up-your-branding/).
- Configure customer email notifications. Refer to [How to Manage Customer Email Notifications](https://surecart.com/docs/customer-email-notifications/).

## **Step 3: Connect Payment Processors**

SureCart supports: Stripe, PayPal, Mollie, Paystack, Razorpay.

## **Step 4: Import Customers**

Customer data is imported via a CSV file. Refer to [How to Import Customers in Bulk](https://surecart.com/docs/import-customers-in-bulk/).

## **Step 5: Import Products**

Product data is imported via a CSV file. Refer to [How to Import Products in Bulk](https://surecart.com/docs/import-products-in-bulk/).

## **Step 6: Import Purchases**

Historical purchase data is imported via a CSV file. Refer to [How to Import Purchases in Bulk](https://surecart.com/docs/import-purchases-in-bulk-surecart/).

## **Step 7: Import Active Subscriptions**

Active subscriptions are imported via a CSV file. Refer to [How to Import Subscriptions in Bulk](https://surecart.com/docs/import-subscriptions-in-bulk/).

## **Step 8: Synchronize WordPress Users with SureCart**

Run the user sync from the SureCart settings. Refer to [How to Sync WordPress Users with SureCart](https://surecart.com/docs/sync-users-with-surecart/).

## **Notes and Limitations**

- The migration order matters. Customers must be imported before purchases and subscriptions, and products must exist before purchases or subscriptions can reference them.
- CSV files must follow the format specified in each bulk import guide.
- Saved payment method transfer is supported only when migrating from Stripe.
- Testing the migration in a staging environment before applying it to a live store is recommended.
