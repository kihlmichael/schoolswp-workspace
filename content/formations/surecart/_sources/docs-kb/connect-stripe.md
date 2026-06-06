---
source_url: https://surecart.com/docs/connect-stripe
source: surecart-kb
scraped: true
---

/ [Knowledge Base](https://surecart.com/docs/)/ [Integrations](https://surecart.com/docs-category/integrations/)/How to Connect Stripe Payment Processor

# How to Connect Stripe Payment Processor

If you're considering using Stripe to accept payments while selling on SureCart, this article is for you.

Stripe is a renowned payment processing service that empowers businesses worldwide to securely receive payments from customers. It offers a wide range of features and tools to streamline payment collection, making it a popular choice for online businesses and e-commerce platforms.

In this article, we'll guide you through the process of connecting Stripe and SureCart, so you can effortlessly collect payments from your customers while selling on SureCart.

Let's get started!

## Connecting Your Stripe Account in SureCart

When you're ready to connect SureCart and Stripe together, simply log in to your WordPress admin area and follow these easy steps:

1. From the SureCart Dashboard, navigate to the Settings menu.

2. Then click on Payment Processors. This will open a screen with all available processors.

### Connecting In Live Mode

Live mode in SureCart enables real transactions to be processed using actual payment methods.

Here's how you can connect your Stripe with your SureCart store in live mode:

1. Click on the Stripe toggle to access the SureCart platform.

2. Click on the "Stripe" tab.

3. Access the **Connect** dropdown and select "Live Mode".

4. Enter your Stripe email address and click "Continue." Fill in your Password and Verification Code received on your mobile phone in the subsequent steps.

5. You will see a message indicating that you will be redirected to the SureCart platform.

6. After being redirected, you will see the Stripe account enabled here.

7. Now, head back to your WordPress page and refresh it. After doing so, you will notice a green tag indicating that you have successfully connected your Stripe account in live mode.

**Note**: Stripe might take some minutes to show up on your checkout. If it doesn't show up at all, please contact the Stripe support team.

### **Connecting In Test Mode**

You can also connect Stripe in test mode. This lets you check the payment system in a secure testing setup.

Follow these steps to connect the test processor:

1. Click on the Stripe toggle to open the SureCart platform.

2. Click on the Stripe tab here.

3. Select "Test Mode" from the **Connect** dropdown menu.

4. Since we are in the test mode, you can "skip this form".

5. After being redirected, you'll see that the Stripe test processor is enabled here.

6. Go to your WordPress page and refresh it. Once you do, you will see a green tag indicating that you have successfully connected your Stripe account in live mode.

Congratulations! You've successfully enabled Stripe in both Live and Test modes, and you're now ready to make sales, whether in live or test mode.

### **Verifying the SureCart Configuration in Stripe**

If you're facing issues displaying Stripe payment methods on your checkout, follow these steps:

- Login to your [Stripe account](https://dashboard.stripe.com/login).

- Click on the Settings icon and access the **Payments** tab.

- Under **Payment methods**, ensure you have the "SureCart configuration" selected as the default.

- You should now see the SureCart configuration set as the default.

Now, you can enable and use any of the available payment methods here!

### **Troubleshooting Checkout Errors**

If you still encounter checkout errors, follow these steps to troubleshoot:

- Click on the three dots and choose **Review transactions**.

Here, you'll be able to review how your payment methods appear. If any payment methods do not appear, this section will provide insights into the problem.

- Select the **Order amount and currency** tab.
- Enter the preferred location, amount, and currency.
- Click on the **Review** button.

- Stripe will show you the list of payment methods that do not appear and the reasons.

The first section also shows the payment methods that appear on checkout.

If the desired payment method is shown here but still doesn't appear on your checkout, here's what you can do:

- Go to **Transactions** and select any individual transaction.

- Copy the transaction ID.

- Go back to the Troubleshooting screen and select the **Transaction ID** tab.
- Paste the transaction ID that we copied and click the **Go** button.

This will show all payment methods that are displayed and not displayed for that particular transaction.

That covers everything you need to know to connect Stripe with SureCart. However, if you still have questions or encounter any issues, please don't hesitate to contact us.

We'll be glad to assist you with any inquiries or problems you may have.

### Frequently Asked Questions

**Can I Switch Payment Processors?**

Yes, you can switch to a different payment processor or connect a new Stripe account. It's important to understand how existing subscriptions and payment methods will be affected.

For detailed guidance, read: [Switching Payment Processors](https://surecart.com/docs/switching-payment-processors).

**Can I connect to a more than one Stripe account?**

You can connect multiple Stripe accounts, but only one can be active at a time.

To learn more about managing multiple accounts and the expected behavior of subscriptions, see: [Switching Payment Processors](https://surecart.com/docs/switching-payment-processors).
