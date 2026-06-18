---
source_url: https://surecart.com/docs/third-steps
source: surecart-kb
scraped: true
---

/ [Knowledge Base](https://surecart.com/docs/)/ [Getting Started](https://surecart.com/docs-category/getting-started/)/Making a First Sale with SureCart

# Making a First Sale with SureCart

This document explains how to test the checkout flow using Test Mode and how to enable live payments to begin processing real orders.

## **Requirements**

- WordPress admin access
- SureCart plugin installed and activated
- At least one product created in SureCart
- A SureCart account connected to the store

## **Testing the Checkout in Test Mode**

### **Step 1: Open the Product**

- Go to **WordPress Dashboard → SureCart → Products**.
- Click the product name or the **Edit** link.

### **Step 2: Enable Test Mode**

- On the product editing page, locate the **Instant Checkout** dropdown menu in the top-right corner.
- Toggle the **Test Mode** option to activate it.
- Click **Save Product**.

**Note:** When Test Mode is enabled, the Instant Checkout displays a **Test Mode** badge and uses a test payment processor. Real payment methods are not available in this mode.

### **Step 3: Open the Instant Checkout Preview**

- Open the **Instant Checkout** dropdown menu again.
- Click **View** (or Preview if not published).

### **Step 4: Complete the Test Order**

- Enter a value in the **Name** field.
- Fill in the **Shipping Address** fields.
- Click **Purchase** to submit the test order.

**Expected outcome:** A **Thank you** confirmation modal appears. A test receipt is sent to the email address used in the order.

### **Step 5: Review the Test Order in the Customer Dashboard**

Click **Continue** in the confirmation modal to open the Customer Dashboard. The Customer Dashboard displays the test order under **Order History**.

### **Disabling Test Mode**

1. Open the product in **WordPress Dashboard → SureCart → Products**.
2. Open the **Instant Checkout** dropdown menu.
3. Toggle the **Test Mode** option off.
4. Click **Save Product**.

## **Enabling Live Payments**

To process real transactions, a payment processor must be connected: Stripe, PayPal, or Mollie.

## **Notes and Limitations**

- Test Mode transactions do not process real payments and do not generate live orders.
- Test Mode is configured per product.
- A receipt email is sent for both test and live orders.

## **Related Documentation**

- [Getting Started with SureCart](https://surecart.com/docs/getting-started/)
- [Next Steps After Getting Started with SureCart](https://surecart.com/docs/second-steps/)
- [How to Connect Stripe Payment Processor](https://surecart.com/docs/connect-stripe)
