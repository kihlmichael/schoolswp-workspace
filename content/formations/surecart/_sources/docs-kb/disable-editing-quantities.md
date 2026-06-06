---
source_url: https://surecart.com/docs/disable-editing-quantities
source: surecart-kb
scraped: true
---

/ [Knowledge Base](https://surecart.com/docs/)/ [Checkout](https://surecart.com/docs-category/checkout/)/How to Disable Editing Quantities in Your Checkout Form

# How to Disable Editing Quantities in Your Checkout Form

This document explains how to disable quantity editing in a SureCart checkout form, preventing customers from increasing or decreasing product quantities during checkout.

### **Requirements**

- WordPress admin access
- SureCart installed and activated
- An existing checkout form

### **Quantity Editing Overview**

By default, SureCart allows customers to adjust product quantities directly in the order summary during checkout.

When quantity editing is disabled:

- The **+** and **−** controls are hidden
- Customers cannot change product quantities from the checkout form

### **Disable Quantity Editing in the Checkout Form**

Follow the steps below to disable quantity editing.

However, if you prefer to restrict this feature for your customers, SureCart also provides you an option to disable it.

If you disable this feature, the above **'+'** and **'-'** icons won't show up for your customers. In this article, we'll show you exactly how you can do it.

- Go to **WordPress Dashboard → SureCart → Checkout**.
- Open the checkout form you want to edit.
- Select the **Order Summary** block.
- Open the **List View** to locate the block structure.
- Expand **Totals**.
- Select **Line Items**.
- In the settings panel on the right, disable the **Editable** option.
- Click **Update** to save the changes.

### **Expected Outcome**

After completing these steps, customers will no longer see quantity controls in the order summary and will not be able to change product quantities during checkout.

### **Notes and Limitations**

- Existing orders are not affected by this change.
- Disabling quantity editing applies only to the checkout form being edited.
- Customers can still modify quantities before reaching checkout, depending on your store flow.

### **FAQ**

**Does disabling quantity editing remove products from the checkout?**

No. It only prevents customers from changing quantities in the order summary.

**Can I re-enable quantity editing later?**

Yes. You can re-enable the **Editable** option at any time.

**Does this affect all checkout forms?**

No. Quantity editing is configured per checkout form.
