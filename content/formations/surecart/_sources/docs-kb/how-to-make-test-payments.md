---
source_url: https://surecart.com/docs/how-to-make-test-payments
source: surecart-kb
scraped: true
---

# How to Make Test Payments

SureCart's test payments feature lets you practice transactions without spending real money, ensuring your payment processes work accurately and reliably.

### Using SureCart's Built-In Test Processor

By default, SureCart's own test processor will be active on your store. When in use, you'll see a test payment option at checkout.

Please note that this test payment option is not intended for real transactions and should not be used in a live environment.

Since it's not a real payment option, you don't need to input any payment information when making a test purchase.

To disable it, head to SureCart **Settings** > **Payment Processors**, and click on any of the available processors. Access the **Test Processor** tab and click the "Disable" button on the top-right.

### Activating Test Mode for Payment Processors

SureCart allows you to activate test mode for multiple payment processors such as Stripe, PayPal, Paystack, and Mollie.

**Important Note**: The **Test Mode Restricted** setting allows you to control who can perform test orders. When enabled, only administrators can finalize test orders that create actual test order entries in your store.

To manage this setting: Go to **SureCart Settings** > **Advanced** tab > **Spam Protection & Security** > locate **Test Mode Restricted**.

Here's how you can enable the test mode:

- Navigate to the **Settings** section under **SureCart**.
- Navigate to the **Payment Processors** section.
- Select your preferred payment processor (e.g., Stripe).
- Access the "Connect" dropdown menu and select **Test Mode**.
- You can **skip this form** in test mode and avoid entering payment information.

### Activating Test Mode In Your Checkout

After activating test mode in your SureCart settings, proceed to enable it in your form:

- Navigate to the **Custom Forms** section under **SureCart**.
- Select the checkout form.
- Select the **Test** option from the dropdown.
- Click on the **Update** button in the top-right corner to apply these changes.

### **Activate Test Mode via Checkout Page Admin Bar**

To enable or disable test mode easily, access the admin bar on the checkout page while logged into your WordPress dashboard.

- Select any product, proceed to its checkout page, then access the dropdown menu and select **Test Mode**.

### **Previewing Test Mode On Your Checkout**

- Navigate to the shop page on your website and buy any product item.
- Proceed to checkout and fill in the test Stripe information. Since the payment is in test mode, you don't need to fill in real payment details.

If you are using the Stripe integration, use Stripe's test cards to test the transaction.

### **Clearing Test Data (Optional)**

- Navigate to SureCart **Settings**, then proceed to **Payment Processors**. Choose the previously used payment processor.
- Select **General** under Settings.
- Scroll down and click on the **Clear Test Data** button.

A new prompt will appear, instructing you to type the **CONFIRM** text message. Your test data will be automatically deleted in a few minutes.

This action is irreversible, so please be sure you are not deleting any real data.
