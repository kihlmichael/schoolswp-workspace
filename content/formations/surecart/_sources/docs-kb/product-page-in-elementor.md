---
source_url: https://surecart.com/docs/product-page-in-elementor
source: surecart-kb
scraped: true
---

/ [Knowledge Base](https://surecart.com/docs/)/ [Elementor](https://surecart.com/docs-category/elementor/)/Product Page

# Product Page

Learn how to create stunning SureCart product pages using our native Elementor components. This guide will walk you through the complete setup process.

**Important**: Elementor Pro is required to create custom templates.

Let's get started!

### **First Steps**

Before creating your product page template, ensure proper integration by completing these initial setup steps:

- Navigate to Elementor > Settings
- Under Post Types, locate and check "SureCart Product"
- Click "Save Changes" to apply

- Navigate to the Features tab in Elementor settings
- Scroll down to locate the Container section

- Look for the green indicator dot next to "Container" in the Features list
- If the indicator is not green:
  - Click the dropdown menu and enable the feature
  - Click "Save Changes" to apply

You're now ready to build your SureCart product template with Elementor!

### **Creating a Product Template in Elementor**

Creating a SureCart product template follows the same process as other Elementor templates, with the key difference being the selection of the SureCart Product layout.

- Navigate to Templates > Theme Builder

- Click the Add New button (+) in the top-right corner of the Theme Builder interface

- Locate the SureCart Product card in the template options
- Click the plus icon (+) within the SureCart Product box to begin customization

SureCart offers two pre-designed product templates:

- Product Form (Left)
- Product Form (Right)

To implement your chosen template:

- Review both layout options
- Select the template that best suits your needs
- Click the Insert button beneath your preferred layout

The Structure panel provides access to all SureCart elements for customization, including:

- Product Form
- Product Name
- Pricing
- Product Description
- Price Selector
- Variant Pills
- Quantity
- Custom Amount
- Add to Cart Button
- Buy Now Button
- Product Media

**Note**: We won't cover the customizations in this documentation as it is outside its scope.

- When you're satisfied with your template design, click the Publish button in the top-right corner of the screen.

- A prompt will appear asking, "Where Do You Want to Display Your Template?" Click the Add Condition button to specify where your template will appear on your site.

To apply the template to all products (recommended for most cases):

- Select All Products from the dropdown menu
- Click Save & Close to confirm your selection

Preview your product page on the frontend to verify all elements appear as intended. In this example, we've implemented:

1. Right-aligned gallery layout
2. Truncated product description (30 characters with ellipsis)
3. Rounded variant pills for better visual appeal

That completes the product template setup! You can now explore individual SureCart Elements and Settings to further customize your template. If you'd like, share your template design with the community in our Facebook group.

### **Frequently Asked Questions**

**Why are my SureCart widgets not showing up, or why isn't the SureCart template being inserted in Elementor?**

SureCart widgets require specific elements to be enabled in Elementor's Element Manager. Ensure that the following elements are enabled:

– Post title

– Post Excerpt

– Text Editor

– Heading

– Container

– All SureCart blocks

Without these elements enabled, the SureCart Form Widget will not be inserted properly.

To configure these settings, go to **Elementor > Element Manager** and enable the required elements.

**Why isn't my template showing up on my product page?**

Here are a few reasons your template isn't showing up. Let's review some possibilities:

– Check if your product is set to the theme layout instead of the SureCart layout in the Template area of the edit product page.

– Verify that you don't have another template created for SureCart Product that takes precedence over the one you just created.

– Ensure you have selected the correct display condition for the template.

**Can I have different templates for different products?**

Yes! Create multiple templates and set specific display conditions for each product, product collection and others conditions.

**What does the warning "SureCart widgets must be placed inside a 'Product Form' container to function properly" mean?**

This warning indicates that your SureCart widgets, such as Product Name, Pricing, Add-to-cart and others, are not placed within the required "Product Form" container in your Elementor template. **Importantly, this notice is only visible to logged-in admins and will not be shown to regular site visitors or customers**.

To fix this, make sure that the main container holding your SureCart widgets in your Elementor Product template has the "Container Type" setting changed from "default" to "Product Form". This ensures that the widgets function correctly on your product page.
