---
source_url: https://surecart.com/docs/custom-thank-you-page
source: surecart-kb
scraped: true
---

/ [Knowledge Base](https://surecart.com/docs/)/ [Checkout](https://surecart.com/docs-category/checkout/)/How To Set Up a Custom Thank You Page For a Form

# How To Set Up a Custom Thank You Page For a Form

This document explains how to create and assign a custom Thank You page for purchases made through a SureCart form, replacing the default post-purchase modal.

### **Requirements**

- An existing checkout form
- WordPress admin access
- SureCart installed and activated

### **Create a Custom Thank You Page**

Follow the steps below to create a custom Thank You page.

- Go to **WordPress Dashboard → Pages → All Pages**.
- Click **Add New**.
- Enter a name for the page.
- Design the page using the available SureCart blocks.

#### **Optional: Add an Order Confirmation Block**

You can include order details on the Thank You page.

- Click the **+** button to add a new block.
- Insert the **Order Confirmation** block.
- Customize the text, call-to-action, and layout as needed.
- Click **Publish** to save the page.

### **Assign the Custom Thank You Page to a Form**

After creating the page, assign it to a checkout form.

- Go to **WordPress Dashboard → SureCart → Custom Forms**.
- Select the form you want to edit.
- Click the form header to open the checkout form settings.
- Enable the **Thank You Page** option.
- Select the custom Thank You page you created.
- Click **Update** to save the changes.

### **Expected Outcome**

After completing these steps, customers who complete a purchase through the selected checkout form will be redirected to the custom Thank You page instead of seeing the default confirmation modal.

### **Notes and Limitations**

- The default modal will continue to appear for forms without a custom Thank You page assigned.
- The custom Thank You page applies only to the form where it is enabled.
- Existing orders are not affected by changes to the Thank You page configuration.

### **FAQ**

**Can I use a different Thank You page for each form?**

Yes. Each checkout form can have its own custom Thank You page.

**Does changing the Thank You page affect past purchases?**

No. Changes apply only to future purchases.

**Can I include order details on the Thank You page?**

Yes. The Order Confirmation block can be added to display order information.
