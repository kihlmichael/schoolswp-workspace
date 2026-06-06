---
source_url: https://surecart.com/docs/conditional-block
source: surecart-kb
scraped: true
---

/ [Knowledge Base](https://surecart.com/docs/)/ [Checkout](https://surecart.com/docs-category/checkout/)/Create Advanced Checkouts With the Conditional Block

# Create Advanced Checkouts With the Conditional Block

This document explains how to use the Conditional block in SureCart to display checkout fields or messages based on specific conditions, such as customer location or selected products.

### **Requirements**

- WordPress admin access
- SureCart installed and activated
- An existing checkout form

### **What Is the Conditional Block**

The Conditional block allows checkout content to appear or remain hidden based on defined rules.

Conditions can be created using factors such as:

- Selected products
- Shipping country
- Order value
- Applied coupons
- Payment method

When the defined rules are met, the blocks inside the Conditional block are displayed during checkout.

### **Use Case: Show a Tax ID Field Based on Customer Country**

This example demonstrates how to display a Tax ID field only when the customer's shipping country matches specific values.

- Go to **WordPress Dashboard → SureCart → Checkout**.
- Open the checkout form you want to edit.
- Click the **+** icon to add a new block.
- Search for **Conditional** and add the Conditional block.
- Select the Conditional block and click **Add Conditions**.
- In the **Condition** dropdown, select **Shipping Country**.
- Choose the countries where the field should appear (for example, United States, India, and Brazil).
- Click **Set Rules**.
- Click the **+** icon inside the Conditional block.
- Search for **Tax** and insert the **Tax ID** or **VAT** field.
- Update the label if needed (for example, SSN, CPF, or Tax ID).
- Click **Update** to save the checkout form.

The Tax ID field will now appear only when customers from the selected countries reach the checkout.

### **Use Case: Show a Pre-Order or Backorder Notice**

You can also use the Conditional block to display messages for specific products, such as pre-order or backordered items.

- Go to **SureCart → Checkout**.
- Open the checkout form.
- Insert a **Conditional** block after the order summary.
- Add a condition based on **Product(s)**.
- Select the product that should trigger the message.
- Click **Set Rules**.
- Inside the Conditional block, insert a **Paragraph** block.
- Enter the message you want customers to see (for example, pre-order details or delivery expectations).
- Click **Update** to save your changes.

When the selected product is added to the cart, the message will appear during checkout.

### **Expected Outcome**

After configuring Conditional blocks, checkout fields and messages will appear dynamically based on the defined rules, providing a more context-aware checkout experience for customers.

### **Notes and Limitations**

- Conditional blocks only affect the content placed inside them.
- Conditions are evaluated in real time during checkout.
- Multiple Conditional blocks can be used in the same checkout form.

### **FAQ**

**Can I use multiple conditions in the same checkout form?**

Yes. You can add multiple Conditional blocks, each with its own set of rules.

**Do Conditional blocks affect existing orders?**

No. Conditions apply only during checkout and do not modify existing orders.

**Can Conditional blocks be used for non-product rules?**

Yes. Conditions can be based on factors such as shipping country, payment method, or order value.
