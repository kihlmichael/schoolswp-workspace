---
source_url: https://surecart.com/docs/adding-terms-conditions-in-checkout
source: surecart-kb
scraped: true
---

/ [Knowledge Base](https://surecart.com/docs/)/ [Checkout](https://surecart.com/docs-category/checkout/)/Adding Terms & Conditions to Your Checkout Form in SureCart

# Adding Terms & Conditions to Your Checkout Form in SureCart

This document explains how to add a Terms & Conditions checkbox to a SureCart checkout form, requiring customers to agree before completing their purchase.

### **Requirements**

- WordPress admin access
- SureCart installed and activated
- An existing checkout form

### **How to Add a Terms & Conditions Checkbox**

Follow the steps below to add a Terms & Conditions checkbox to your checkout form.

- Go to WordPress Dashboard → SureCart → Checkout Forms.
- Open the checkout form you want to edit.
- Insert a **Checkbox** block where you want the Terms & Conditions option to appear.
- Select the checkbox block.
- In the block settings panel on the right, enable the **Required** option.

Once enabled, customers will not be able to complete the checkout unless the checkbox is selected.

### **Customize the Checkbox Label**

You can customize the text displayed next to the checkbox.

- Double-click the checkbox label.
- Enter the text you want customers to see (for example, "I agree to the Terms & Conditions").

The checkbox label and value are saved with the order, creating a record of the customer's agreement.

### **Optional: Set the Checkbox as Checked by Default**

If needed, the checkbox can be pre-selected.

- Select the checkbox block.
- Enable the **Checked by default** option.

When enabled, the checkbox will be selected automatically when the checkout loads.

### **How to Link Your Terms & Conditions Page**

You can link the checkbox text to your Terms & Conditions page so customers can review it before agreeing.

- Select the text next to the checkbox.
- Click the **Link** icon in the toolbar.
- Enter the URL of your Terms & Conditions page.
  - Alternatively, use **Ctrl + K** to insert the link.
- Click **Update** to save your changes.

### **Expected Outcome**

After completing these steps, the checkout form will display a Terms & Conditions checkbox. Customers must agree to the terms before completing their purchase.

### Notes and Limitations

- The checkbox value is stored with the order for reference.
- If the checkbox is marked as required, checkout cannot be completed unless it is selected.

### **FAQ**

**What happens if the Terms & Conditions checkbox is not checked?**

If the checkbox is marked as required, the customer will not be able to complete the checkout until it is selected.

**Can I change the checkbox text after publishing the checkout?**

Yes. Updating the checkbox label affects future checkouts and does not modify existing orders.
