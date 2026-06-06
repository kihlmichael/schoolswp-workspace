---
source_url: https://surecart.com/docs/product-reviews-shortcodes
source: surecart-kb
scraped: true
---

/ [Knowledge Base](https://surecart.com/docs/)/ [Products](https://surecart.com/docs-category/products/)/How to Display Product Reviews Using Shortcodes

# How to Display Product Reviews Using Shortcodes

This document explains how to use SureCart product review shortcodes to display reviews on any page, including pages built with Divi, Beaver Builder, Oxygen, and other page builders that do not support the WordPress Block Editor.

## **Requirements**

- WordPress admin access
- SureCart installed and activated
- Reviews enabled on the product in SureCart
- The Product UUID, if the shortcodes will be placed on a non-product page (see _Finding the Product UUID_ below).

## **Finding the Product UUID**

All shortcodes accept an optional product_id attribute, which corresponds to the SureCart product UUID. The UUID is a string of letters, numbers, and hyphens (for example, eee96da1-be2b-488d-bd76-cdb0c96b118f).

When the shortcode placement requires the UUID:

- **On product pages:** The product_id attribute is optional. The shortcode automatically detects the current product.
- **On non-product pages (landing pages, custom pages, etc.):** The product_id attribute is required. Without it, the shortcode renders no output.

### **How to Locate the Product UUID**

1. Go to **WordPress Dashboard → SureCart → Products**.
2. Click the product to open the Edit Product page.
3. Look at the browser address bar. The UUID is the value of the id parameter at the end of the URL.

Example URL: /wp-admin/admin.php?page=sc-products&action=edit&id=eee96da1-be2b-488d-bd76-cdb0c96b118f. The UUID is the value after id=.

**Note:** The Product UUID is not the same as the WordPress post ID. The Product UUID is assigned by SureCart and is always a string of letters, numbers, and hyphens. Using a numeric WordPress post ID with the product_id attribute does not work.

## **Available Shortcodes**

### **sc_product_review_rating_stars**

Displays the average rating as filled, half, or empty stars.

**Basic usage:**

```
[sc_product_review_rating_stars]
```

**With attributes:**

```
[sc_product_review_rating_stars product_id="eee96da1-be2b-488d-bd76-cdb0c96b118f" size="24px" fill_color="#f59e0b" link_to_reviews="true"]
```

| **Attribute**   | **Type** | **Default**         | **Description**                                                                                            |
| --------------- | -------- | ------------------- | ---------------------------------------------------------------------------------------------------------- |
| product_id      | string   | —                   | Product UUID. Required on non-product pages. Auto-detected when the shortcode is placed on a product page. |
| size            | string   | 20px                | Size of each star icon.                                                                                    |
| fill_color      | string   | Theme primary color | Color for filled stars (for example, #f59e0b).                                                             |
| link_to_reviews | boolean  | false               | Wraps the stars in a link to the reviews section.                                                          |

### **sc_product_review_rating_value**

Displays the average rating as a numeric value (for example, 4.5).

### **sc_product_review_total_count**

Displays the total number of reviews (for example, 156 reviews).

### **sc_product_review_breakdown**

Displays a 5-star breakdown with progress bars showing the distribution of ratings.

### **sc_product_review_list**

Displays the full review experience, including a summary section, filter sidebar, individual reviews with pagination, and the Write a Review form modal.

### **sc_product_review_add_button**

Displays a Write a Review button that opens the review form modal. If the user is not logged in, the user is redirected to the customer dashboard to sign in first.

## **Notes and Limitations**

- Reviews must be enabled on the product in SureCart for any shortcode to render output.
- The product_id attribute uses the SureCart product UUID, not the WordPress post ID.
- These shortcodes use the WordPress Interactivity API.

## **Related Documentation**

- [How to Enable and Configure Product Reviews](https://surecart.com/docs/product-reviews/)
- [How to Import Reviews in SureCart](https://surecart.com/docs/how-to-import-reviews-in-surecart/)
- [All SureCart Shortcodes](https://surecart.com/docs/all-shortcodes/)
