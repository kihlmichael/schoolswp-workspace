---
source_url: "https://docs.wpsocialninja.com/guide/import-export-migration/migrate-from-judge-me.html"
title: "Migrate from Judge.me | WP Social Ninja"
---

# Migrate from Judge.me | WP Social Ninja

This guide provides a step by step process for transferring your WooCommerce product reviews from Judge.me directly into WP Social Ninja.

#### **Step 1: Export Reviews from Judge.me** [​](https://docs.wpsocialninja.com/guide/import-export-migration/migrate-from-judge-me#step-1-export-reviews-from-judge-me)

First, you need to export your existing reviews from your Judge.me [account](http://judge.me/).

*   Log in to your **Judge.me** dashboard where you manage your product reviews.
    
*   Click the **Export Reviews** button. This will download a CSV file containing all your review data.
    

![judgeme export](https://docs.wpsocialninja.com/assets/judgeme-export-scaled.CdmVH4Kw.webp)

For detailed steps on exporting Judge.me, please refer to this [documentation](https://judge.me/help/en/articles/8236266-exporting-reviews).

#### **Step 2: Import Reviews into WP Social Ninja** [​](https://docs.wpsocialninja.com/guide/import-export-migration/migrate-from-judge-me#step-2-import-reviews-into-wp-social-ninja)

Next, you need to import the CSV file into WP Social Ninja.

*   From your WordPress dashboard, navigate to **WP Social Ninja → Tools**.
    
*   Select the **Import** tab.
    
*   In the **Import** section, click the dropdown menu and select **Judge.me Reviews**.
    
*   Click **Choose File** and upload the CSV file you just downloaded from Judge.me.
    
*   Click the **Import** button to begin the migration process.
    

![judgeme import](https://docs.wpsocialninja.com/assets/judgme-import.BZG9I3To.webp)

**Note:** Please be aware of the following when migrating:

*   **Same Site Migration:** If you are importing reviews on the **same site** you exported from, no changes are needed in the CSV file.
    
*   **Different Site Migration:** If you are moving reviews to a **different site**, you have to manually edit the CSV file before importing. Ensure the product IDs in the file match the corresponding WooCommerce product IDs on your new site. If the IDs do not match, the reviews will not be linked to the correct products.
    

#### **Step 3: Verify Your Reviews** [​](https://docs.wpsocialninja.com/guide/import-export-migration/migrate-from-judge-me#step-3-verify-your-reviews)

Once the import is complete, go to the **All Reviews** section in WP Social Ninja. You will find all your migrated Judge.me reviews displayed there and associated with your WooCommerce products.

To learn more about collecting reviews from WooCommerce, see this documentation.
