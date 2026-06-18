---
source_url: https://surecart.com/docs/product-pages-guide
source: surecart-kb
scraped: true
---

# Product Pages Guide

Product pages are an important part of your SureCart online store, and customizing them can enhance your overall customer experience.

This is the individual product page that shows up when you click on a particular product.

If you're using a page builder like **Elementor** or **Bricks Builder** to customize your product pages, dedicated step-by-step guides are available.

### **Customizing Product Permalinks**

Permalinks are like personalized address links for each product on your website. They help people find and access specific products easily.

- Navigate to the **Permalinks** section in your WordPress dashboard under **Settings** to customize product permalinks.

### **Product Template Customization**

When a customer clicks on an individual product, they are directed to a page that SureCart allows them to customize.

- To edit individual products, navigate to the desired product from your WordPress dashboard.
- To personalize your product page, click in the **Edit Template** button within the Template section.

The options may vary depending on your WordPress theme, Classic or FSE Theme.

#### Add New Template

With SureCart, you can create a brand-new template for your product page. Click on the **Add new template** icon and give it a name.

Click on the **Edit template** button to start customizing your product page.

In the editor, click on the **List view** icon to view various customization options.

#### **Editing the Product Title**

Upon selecting the **Product Title**, a mini editor block will appear on the right-hand side with basic title customization settings: text position, alignment, heading levels, and more.

#### **Customizing Product Price Choices**

These are the prices associated with your product. You can customize how these prices are displayed — choose the number of columns, display format, edit product prices, and edit the **sale text**.

#### **Editing Product Description**

You can change the text, experiment with background colors, try different fonts, adjust margins and spacing, align the product description, and more.

#### **Customizing Product Variants**

SureCart's Product Variants feature allows you to offer different color options for your product. You can modify the text color, background, and font for indicating the color of the variant. You can also adjust margin and padding settings.

#### **Customizing Pricing Options**

These are the pricing options available for your product (e.g., one-time payment or subscription). You can add/remove pricing options by adjusting the columns section, decide whether to show or hide the price numbers, and change the label.

#### **Product Quantity and Add to Cart/Purchase Buttons**

You can modify product quantity label as well as the wording for the Add to Cart and Buy Now buttons. You can also edit the terminologies for "out of stock" and "unavailable" labels.

#### **Change Product Featured Image**

With image customization, you can:

- Adjust the image mode to **Gallery or Slideshow view**
- Activate **Auto Height** that allows the image to fit to the page according to its height
- Set your desired maximum image width
- Easily control the number of thumbnails on display

### **Product Page Shortcodes**

If you prefer creating product pages in your page builders theme builder feature, you can use the following shortcodes:

```
[sc_product_description] - The product description
[sc_product_price] - The currently selected price
[sc_product_variant_choices] – Displays the variant choices of a product that contains variants
[sc_product_price_choices] - Shows the pricing choice of a product
[sc_product_media] - The product image or slideshow
[sc_product_quantity] - The product quantity selector
[sc_product_cart_button] - The add to cart button
```

**Important Note**: The ID parameter in SureCart shortcodes won't work in SureCart version 3 and above. Starting in version 3, SureCart uses WordPress Interactivity API. Please update your shortcodes to work with the new version.
