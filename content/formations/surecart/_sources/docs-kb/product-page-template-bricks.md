---
source_url: https://surecart.com/docs/product-page-template-bricks
source: surecart-kb
scraped: true
---

/ [Knowledge Base](https://surecart.com/docs/)/ [Bricks Builder](https://surecart.com/docs-category/bricks-builder/)/How to Create a Product Page Template in Bricks Builder

# How to Create a Product Page Template in Bricks Builder

This document explains how to create and assign a custom product page template using Bricks Builder for SureCart products.

### **Requirements**

- WordPress admin access
- SureCart is installed and activated
- Bricks Builder installed and activated
- At least one published SureCart product

### **Configure SureCart Settings in Bricks Builder**

Before you begin designing your product page in Bricks Builder, you'll need to enable the SureCart Product post type in the Bricks Builder settings.

To do this, navigate to **Bricks > Settings**. Under the **General** tab, in the **Post types** section, activate the toggle for **SureCart Product**.

### **Creating SureCart Single Product Template**

To apply a consistent layout to all your product pages in Bricks, you need to create a SureCart Single Product template.

**Please note**: You can also create different layouts based on taxonomies and/or collections, but that is beyond the scope of this article.

To create the SureCart Single Product template, follow these steps:

- Go to **Bricks > Templates**;
- Click the **Add New Template** button.
- Give the template a name; in this case, "Product Template" (1).
- In the **Template type** dropdown, select **SureCart – Single Product** (2).
- Click the **Publish** button (3).
- Then click the **Edit with Bricks** button (4).
- Search for "section" in the elements panel (1).
- Click on the **Section** element to add it to the canvas (2).
- Click on the **Container** (1) in the Structure panel on the right.
- Click on the **Elements** button (2) to add a SureCart Element to the container.
- Search for "product" (1) in the elements panel for quicker selection.
- Click on the **Product Form** element (2) to add it to the container.

A pre-built product page layout is available to help adjust styles more efficiently.

- Click the **save** button to save your changes.
- Test the template on the frontend to confirm it is working as expected.

### Notes and Limitations

- SureCart elements such as Add to Cart, Collection Tags, Product Media, and others must be placed inside the Product Form or Product Card block.
- These elements will not function correctly if placed outside these containers.

### Expected Outcome

Once completed, SureCart products will use the custom Bricks product page template, displaying product information and purchase elements according to the configured layout.

### **FAQ**

**Why aren't my Add to Cart, Collection Tags, Product Media, and other elements working correctly?**

For SureCart elements to function properly, they must be placed inside the Product Form or Product Card block. Elements placed outside these containers will not work as expected.

**My Single Product template is not loading.**

This usually happens when multiple templates share overlapping conditions. If no specific condition is set, Bricks applies a catch-all condition that may conflict with other templates.

Review your existing templates and ensure there are no conflicting conditions. Also, confirm that the Product Form or Product Card wrapper is present in the template.
