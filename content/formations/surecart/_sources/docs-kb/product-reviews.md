---
source_url: https://surecart.com/docs/product-reviews
source: surecart-kb
scraped: true
---

/ [Knowledge Base](https://surecart.com/docs/)/ [Products](https://surecart.com/docs-category/products/)/How to Enable and Configure Product Reviews

# How to Enable and Configure Product Reviews

This document explains how to enable Product Reviews in SureCart and configure the display of ratings on product pages.

**Important — Existing Stores Must Update Templates:** If your store was created before the Reviews feature was introduced, you must manually update your product templates. Reviews are not automatically added to existing templates.

## **Requirements**

- WordPress admin access
- SureCart installed and activated
- At least one published product

## **Enable Product Reviews**

1. Go to **WordPress Dashboard → SureCart → Settings → Reviews**.
2. Enable Product Reviews.
3. Click Save.

## **Product-Level Review Settings**

1. Go to **WordPress Dashboard → SureCart → Products**.
2. Click on the product to configure.
3. In the Reviews panel on the right sidebar:
   - Enable Reviews: Toggle to show or hide reviews for this product on the frontend
   - Review Request Email: Toggle to enable or disable automatic review request emails
4. Click Save Product.

## **Configure Review Settings**

### **Send Review Request Emails**

Sends an automatic email asking customers to leave a review after their order is fulfilled.

1. Go to **SureCart → Settings → Reviews**.
2. Enable **Send Review Request Email**.
3. Set the number of days under "When should we ask for a review?"
4. Click Save.

### **Verified Buyer Badge**

Displays a badge next to reviews from customers who purchased the specific product.

1. Go to **SureCart → Settings → Reviews**.
2. Enable **Verified Buyer**.
3. Click Save.

## **Managing Reviews**

All reviews are managed from: **SureCart → Products → Reviews**

From this screen, you can: Edit, Approve, Reject, or Delete reviews.

## **Displaying Reviews on Product Pages**

To display reviews on the frontend, add review blocks to your Single Product template.

Access via: **SureCart → Products → Edit (any product) → Template → Edit Product Template**

Available review blocks:

| Block                  | Description                                    | Typical Placement     |
| ---------------------- | ---------------------------------------------- | --------------------- |
| Star Rating            | Average star rating                            | Below product title   |
| Average Rating (Value) | Numeric rating value (e.g., 4.5)               | Alongside Star Rating |
| Reviews Count          | Total number of reviews                        | Next to Star Rating   |
| Product Review Summary | Full rating overview                           | Top of review section |
| Review Breakdown       | Distribution of ratings by star level          | Beside Summary        |
| Product Review List    | Individual reviews with filters and pagination | Main review section   |

## **Notes, Limitations, and Edge Cases**

- Reviews must be enabled globally before they can be displayed.
- Disabling reviews prevents new submissions but does not delete existing reviews.
- Review request emails only trigger after an order is marked as fulfilled.
- Existing stores must manually add review blocks to product templates.

## **Related Documentation**

- [How to Create a Product Page in SureCart](https://surecart.com/docs/create-product/)
- [Product Pages Guide](https://surecart.com/docs/product-pages-guide/)
