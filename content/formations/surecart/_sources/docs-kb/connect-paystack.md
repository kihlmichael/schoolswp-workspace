---
source_url: https://surecart.com/docs/connect-paystack
source: surecart-kb
scraped: true
---

/ [Knowledge Base](https://surecart.com/docs/)/ [Integrations](https://surecart.com/docs-category/integrations/)/How to Connect Paystack Payment Processor

# How to Connect Paystack Payment Processor

If you're considering using Paystack to accept payments while selling on SureCart, this article is for you.

[Paystack](https://paystack.com/) is a service that helps businesses in Nigeria, Ghana, and South Africa securely receive payments from customers worldwide.

### **Know This Before You Connect Paystack with SureCart**

Paystack and Stripe don't work well together.

If you have Stripe and Paystack both active in SureCart, customers will only see the Stripe payment option during checkout.

To ensure a smooth payment process with Paystack, we suggest you disable Stripe before connecting your PayStack account.

If you're not sure how to disable a payment gateway, check out [this article](https://surecart.com/docs/how-to-disable-a-payment-processor/).

### **How to Begin The Setup**

When you're ready to connect SureCart and Paystack together, simply login to your WordPress admin area and follow these easy steps:

1. Go to the WordPress admin area and click on the SureCart dashboard.
2. Click on the Settings menu under SureCart settings that you see on the WordPress sidebar.
3. Click on Payment Processors in SureCart settings and you will see the Paystack listed as one of the payment processors.

#### **Connecting Paystack in Test Mode**

Before you connect the live Paystack payment processor, you can connect Paystack in test mode. This allows you to set up the payment processor in a safe testing environment.

1. Click on the **Paystack** option.
2. Click the "Paystack" tab.
3. Select "Test Mode" from the **Connect** button dropdown.
4. A pop-up window will appear.
5. To get your Test API Keys, go to your Paystack dashboard settings and click on the [API Keys & Webhooks](https://dashboard.paystack.com/#/settings/developer) tab.
6. Scroll to where it says "API Configuration - Test Mode", here you will find your Test Secret Key and Test Public Key. Copy these keys.
7. Go back to the SureCart screen and paste your Paystack Secret Key in the corresponding field.
8. Similarly, paste your Paystack Public Key in the corresponding field.
9. Copy the Webhook URL from the "Webhook Instructions" section, and then click on the "Create" button.
10. Return to your Paystack tab and paste your webhook URL in the corresponding field.

Once you've followed these steps, You will have Paystack connected with SureCart in the test mode.

#### **How to Connect Paystack in Live Mode**

After successfully setting up Paystack in test mode and ensuring a smooth payment process, it's time to move on to the live payment integration.

1. Click on the Paystack option.
2. Select the "Paystack" tab.
3. From the **Connect** dropdown, select "Live Mode".
4. Go to your Paystack dashboard settings and click on the [API Keys & Webhooks](https://dashboard.paystack.com/#/settings/developer) tab.
5. Scroll to where it says "API Configuration - Live Mode", and find your Live Secret Key and Live Public Key.
6. Go back to the SureCart tab and paste your Paystack Secret Key in the corresponding field.
7. Paste your Paystack Public Key in the corresponding field.
8. Copy the Webhook URL from the "Webhook Instructions" section, and then click on the "Create" button.
9. Return to your Paystack tab and paste your webhook URL in the corresponding field.

Once you have completed these steps, you will have successfully set up Paystack as your payment processor in live mode, and you can start accepting payments in Paystack via SureCart.

If you still have questions, don't hesitate to contact us. We'll be glad to help you with any questions or issues you may have.
