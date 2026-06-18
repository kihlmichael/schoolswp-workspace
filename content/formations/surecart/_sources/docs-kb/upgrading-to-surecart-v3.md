---
source_url: https://surecart.com/docs/upgrading-to-surecart-v3
source: surecart-kb
scraped: true
---

/ [Knowledge Base](https://surecart.com/docs/)/ [Migrating](https://surecart.com/docs-category/migrating/)/Upgrading to SureCart V3

# Upgrading to SureCart V3

Upgrading to SureCart V3 introduces powerful new features and enhanced functionality. However, due to significant structural changes, it's essential to carefully review your site afterward to ensure all elements look and function as expected.

This documentation provides a complete roadmap for upgrading to SureCart V3, including **essential steps to take before upgrading**, an **overview of new features and improvements**, and a **post-upgrade checklist** to help you verify key pages, resolve any style or layout issues, and identify potential conflicts with themes or plugins.

###### Important Note

SureCart V3 has undergone extensive testing, including a multi-month beta period where we tested the new version on over 100 stores. While we don't anticipate any major problems, **this is a significant update, so it's possible that some visual elements may appear different**.

Additionally, **caching** can sometimes interfere with updates, potentially causing display or functionality issues. To ensure that all changes are properly reflected, please **clear your site's cache post-upgrade**. For detailed guidance on managing caching, see our [SureCart Caching Documentation](https://surecart.com/docs/caching/).

### **Things to Do Before Upgrading:**

#### 1. Back Up Your Full Site

**Why is this important?** Backing up your entire site is essential before upgrading to prevent any potential data loss or issues during the process.

**How to do it?** Use a trusted WordPress backup plugin or your hosting provider's built-in backup tools to create a complete backup of your site.

**Helpful Resource:** You may also want to consult the [Migrating SureCart to Another WordPress Install](https://surecart.com/docs/migrate-to-another-wordpress-install/) guide, which provides detailed instructions on backing up and migrating your site safely.

#### 2. Test In A Staging Environment

Before applying the upgrade to your live site, test it in a staging environment. This helps you identify any issues with custom templates, plugins, or third-party integrations before affecting your customers.

### **Post-Upgrade Checklist**

After upgrading, use the following steps to verify your site and ensure everything is functioning as intended.

#### 1. Check The Shop Page

- **Why:** Changes to SureCart's structure and the removal of certain DOM elements may impact the display of the shop page.
- **What to Look For:** Inspect for any missing margins, spacing inconsistencies, or misaligned elements.
- **How to Fix:** Edit the shop page and review your layout settings. Remove any unnecessary **group blocks** that could be causing layout issues.

#### 2. Check Collection Archive Pages

- **Why:** Collection pages may be affected by layout changes in SureCart V3, especially if you're using custom styling or theme integrations.
- **What to Look For:** Check for consistent spacing, alignment, and that all collection items display correctly.

#### 3. Check Product Pages

- **Why:** Product pages may need adjustments due to changes in SureCart's DOM structure and functionality enhancements.
- **What to Look For:** Verify that all elements—such as product images, descriptions, prices, and variant selectors—are displayed and working correctly.

#### 4. Check Slide Out Cart

- **Why:** The cart experience is critical, and V3 changes could potentially impact the display or interaction of the cart.
- **What to Look For:** Add products to the cart and open the slide-out cart to ensure all items are visible, prices are correct, and buttons are working as expected.

#### 5. Check Add To Cart and Buy Buttons

- **Why:** These buttons were reworked to use your theme's styles for the **default WordPress button block**.
- **What to Look For:** Ensure your add to cart and buy buttons are styled to your liking. They may have changed in terms of color, size or width depending on your theme's styles.

### **New Features and Functionality in V3**

#### **WordPress Interactivity API Integration**

The Cart, Shop Page, and Product Page have been moved to the WordPress Interactivity API, providing a more dynamic user experience such as more block styling, easier CSS customizations, and more.

#### **SureCart Products as Custom Post Types**

SureCart products are now handled as Custom Post Types, offering benefits such as improved speed, greater customization options, compatibility with SEO plugins, and more. Includes Advanced Custom Fields and Metabox integration, post meta box integration, and improved usage in page builders and query loops.

#### **Product Images in WordPress Gallery**

All product images are now managed through the WordPress gallery, making it easier to organize and manage media.

#### **Flexible Product List Design**

The product list (shop page) is now composed of smaller blocks, giving you more flexibility in design and customization.

#### **Product List Patterns**

You can choose from **pre-made patterns (templates)** for your product list layout.

#### **New Product Filters**

Two additional filters have been introduced: Show products by taxonomy (SureCart Collection) and show products by keywords.

#### **New Default Sorting**

You can now set the default sorting order for your shop.

#### **New Sale Badge**

A sale badge has been added to products, providing a visual cue for discounted items.

#### **Automatic Layout Grid**

The new auto layout mode adjusts your product grid to fit different screen sizes, offering a responsive design without manual adjustments.

#### Native Bricks Builder Integration

- **Templates** for Bricks Builder: SureCart - Single Product and SureCart - Collection Archive.
- Compatibility with **ACSS** (Automatic CSS)
- Product loop
- About **20 dynamic data points** have been added for Bricks Builder integration.
- **12 native Bricks elements** were introduced, including: Product Form, Product Card, Add to Cart, Collection Tags, Product Media, Price Selector, Price Data, Product Data, Quantity, Sale Badge, Custom Amount, Product Variant Pills.

**IMPORTANT:** For SureCart elements (such as Add To Cart, Collection Tags, Product Media, etc.) to function properly, they must be placed within the Product Form or Product Card block wrappers.

### **Additional Considerations**

**Manual Checks:** After upgrading, manually review each key page on the frontend to confirm everything appears and works as expected.

**Caching Issues:** Caching can sometimes cause problems by serving outdated content or styles. After upgrading, be sure to clear your site's cache.

### **FAQ**

**What happens if I revert back to SureCart V2 after upgrading to V3?**

If you revert back to V2, the cart, shop page, and product page may break. This can be easily fixed by re-adding blocks or resetting the templates, but it's important to prepare for this in advance.

**Why aren't my Add to Cart, Collection Tags, Product Media, and other elements working correctly?**

For SureCart elements to work properly, they must be placed within the Product Form or Product Card block wrappers.

**Why does my store look or function incorrectly after upgrading to SureCart V3?**

Caching can sometimes cause display or functionality issues by serving outdated content after an update. If you notice any unexpected visuals or behaviors after upgrading, try clearing your site's cache.
