---
source_url: https://surecart.com/docs/import-from-woocommerce
source: surecart-kb
scraped: true
---

/ [Knowledge Base](https://surecart.com/docs/)/ [Migrating](https://surecart.com/docs-category/migrating/)/How to Import Products from WooCommerce into SureCart

# How to Import Products from WooCommerce into SureCart

This document explains how to import existing WooCommerce products into SureCart. Two paths are available: a guided setup for new SureCart users and a manual import for stores that already have SureCart installed.

## **Requirements**

- WordPress admin access
- SureCart version 4.3.0 or higher, installed and activated
- WooCommerce installed and activated on the same WordPress site
- At least one product available in the WooCommerce store

## **Supported Product Types**

The following SureCart product types are supported during import:

- **One time** products
- **Installment** products
- **Subscription** products

Subscription product imports have been tested with the **WooCommerce Subscriptions** extension. Other product types in WooCommerce are skipped during the import.

## **Path 1: Import During SureCart Setup (New Users)**

1. Go to **WordPress Dashboard → Plugins → Installed Plugins**.
2. Locate **SureCart** and click **Get Started**.
3. On the welcome screen, click **Create New Store**.
4. On the **Confirm Store Details** screen, set the **Brand Color** and **Store Currency**, then click **Continue**.
5. On the **Confirm Email for Store Notifications** screen, enter the email address, then click **Continue**.
6. On the **Select A Starting Point** screen, choose **Import Products from Woo**.
7. Complete the remaining setup steps to finalize the store.

**Expected Outcome:** The import runs in the background once setup is complete. After it finishes, the imported products appear under **WordPress Dashboard → SureCart → Products**, and a confirmation notice is shown: _"SureCart: WooCommerce products import complete."_

## **Path 2: Import on an Existing SureCart Store**

1. Ensure **WooCommerce** is installed and activated.
2. Go to **WordPress Dashboard → SureCart → Settings**.
3. Open the **Advanced** tab.
4. Scroll to the **Syncing** section.
5. On the **WooCommerce Products** row, click **Import**.
6. In the dialog, review the number of products detected.
7. Click **Import Products** to start the import.

**Expected Outcome:** A confirmation message appears: _"WooCommerce import started in the background."_ Once finished, the imported products appear under **WordPress Dashboard → SureCart → Products**.

## **Notes and Limitations**

- The import runs in the background and may take a few minutes.
- Only One time, Installment, and Subscription product types are imported. Other WooCommerce product types are skipped.
- Products that have already been imported are automatically skipped on subsequent runs.
- WooCommerce customers and orders are not included in this import. Only products are imported.

## **FAQ**

**Are WooCommerce customers and orders imported along with the products?**

No. Only products are imported.

**Can the import be run more than once?**

Yes. Only new or previously unimported products are added.

**What happens to products that already exist in SureCart?**

Products already imported are detected and skipped. The import does not create duplicates.
