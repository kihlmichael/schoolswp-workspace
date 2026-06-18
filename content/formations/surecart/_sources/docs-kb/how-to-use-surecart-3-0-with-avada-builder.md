---
source_url: https://surecart.com/docs/how-to-use-surecart-3-0-with-avada-builder
source: surecart-kb
scraped: true
---

# How to Use SureCart 3.0 with Avada Builder

## Overview

SureCart 3.0 requires additional configuration steps to maintain compatibility with the Avada Builder. Ensure you have installed Avada Builder before proceeding.

## Setting Up the Shop Page

1. Navigate to your Pages list and locate your Shop Page, or access it from the SureCart Sidebar
2. In the Page Attributes section on the right side, select "SureCart" as the template
3. Remove the `[sc_product_list]` block from the editor
4. Re-add the element using a Code Block instead
5. To ensure proper product image display, insert this CSS:

[code snippet omitted — see source_url]

6. Save and verify the shop page displays correctly on the frontend

## Configuring Product Detail Pages

1. When editing a product, select "SureCart Layout" as the template layout
2. Save the product
3. Add the following script via WP-Code or another header-footer script injection plugin:

[code snippet omitted — see source_url]

## Fixing Missing Product Thumbnails in Cart

If product thumbnails don't appear in the cart:

1. Go to **Avada > Performance** in your WordPress dashboard
2. Click the **Optimization** tab
3. Increase the **WordPress Big Image Size Threshold** setting (suggest 2500 or higher)
4. Change **Image Lazy Loading** from "Avada" to "WordPress"

These adjustments should restore proper thumbnail display in your cart.
