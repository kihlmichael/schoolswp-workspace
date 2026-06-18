---
source_url: https://surecart.com/docs/ideal-checkout-troubleshooting
source: surecart-kb
scraped: true
---

/ [Knowledge Base](https://surecart.com/docs/)/ [Troubleshooting](https://surecart.com/docs-category/troubleshooting/)/Why iDEAL Might Not Appear in Your Checkout

# Why iDEAL Might Not Appear in Your Checkout

If you don't see iDEAL as a payment option in SureCart, especially when offering subscriptions or recurring payments, don't worry.

This is a common issue and it's related to how Stripe handles certain payment methods.

Here's a simple explanation and how you can fix it.

## **Why iDEAL Doesn't Show for Subscriptions**

When you're offering subscriptions, Stripe only shows payment methods that can handle recurring payments.

Unfortunately, iDEAL doesn't support recurring payments directly. Instead, Stripe uses SEPA Direct Debit to manage these.

So, iDEAL won't show up when your customers check out for subscriptions. Instead, SEPA will be visible, and iDEAL options will only show up after your customers click on SEPA.

## **How to Get iDEAL to Show Up At Checkout For Subscriptions**

If iDEAL isn't showing for purchases, here are some steps to check:

1. When you are enabling Payment Methods on your Stripe Dashboard, make sure that SureCart is the profile you are modifying.

   To do that:
   - Go to **Settings** > **Payments**.
   - Go to **Payment methods** and select SureCart as the default profile here.

2. Double-check that iDEAL is enabled in both test mode and live mode. To do it:
   - Enable the **Test Mode** button, scroll down to iDEAL, and turn it on.
   - When enabling, turn on the **Recurring payments** button and click "Request access".
   - Switch back to the live mode and follow the same steps.

3. Enable SEPA and ensure your Stripe account is approved for SEPA Direct Debit.

## **Why SEPA Appears Instead of iDEAL for Recurring Payments**

For subscriptions, Stripe uses SEPA to handle recurring payments. That's why you see SEPA instead of iDEAL at checkout.

While it may look different, your customers should see the iDEAL options after clicking on SEPA.

If you've tried all the steps above and iDEAL still isn't showing, don't worry. Contact Stripe support or your payment provider for further assistance.

And if you have any questions about SureCart, we're always here to help!
