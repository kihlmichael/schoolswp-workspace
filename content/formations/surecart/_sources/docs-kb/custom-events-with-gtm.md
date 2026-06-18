---
source_url: https://surecart.com/docs/custom-events-with-gtm
source: surecart-kb
scraped: true
---

/ [Knowledge Base](https://surecart.com/docs/)/ [Integrations](https://surecart.com/docs-category/integrations/)/How to Track Custom Events with Google Tag Manager

# How to Track Custom Events with Google Tag Manager

In this article, we'll guide you through the process of sending tracking events from your SureCart store to Google Analytics using Google Tag Manager (GTM).

To connect SureCart with Google Analytics, you can use the [Google Site Kit plugin](https://wordpress.org/plugins/google-site-kit/) on your WordPress site.

### Why Connect SureCart with Facebook Pixel & Google Analytics?

Connecting SureCart with Facebook Pixel (FB Pixel) and Google Analytics (GA) is a great way to track your e-commerce sales and marketing performance.

With Facebook Pixel, you can track website visitors and their interactions with your Facebook ads, create more targeted ads, and optimize your campaigns.

Google Analytics provides insights into your website traffic, visitors' locations, purchase behaviors, etc. You can use this information to improve your website's performance and optimize your overall business strategy.

### **Events That Can Be Tracked**

SureCart automatically broadcasts the "Add To Cart" and "Purchase" events for Google Analytics. This means that if you want to track these events, you just need to install the Google Site Kit plugin on your WordPress. No additional configuration is needed.

Here's a list of additional events you can broadcast through a custom code:

| **Event**             | **Event Name**       | **Description**                                                        |
| --------------------- | -------------------- | ---------------------------------------------------------------------- |
| scAddedToCart         | Added to Cart        | Triggered when a customer adds an item to their shopping cart.         |
| scRemovedFromCart     | Removed from Cart    | Triggered when a customer removes an item from their shopping cart.    |
| scViewedCart          | Viewed Cart          | Triggered when a customer views their shopping cart.                   |
| scProductViewed       | Product Viewed       | Triggered when a customer views a product page.                        |
| scCheckoutInitiated   | Checkout Initiated   | Triggered when a customer begins the checkout process.                 |
| scCheckoutCompleted   | Checkout Completed   | Triggered when a customer successfully completes the checkout process. |
| scShippingInfoAdded   | Shipping Info Added  | Triggered when a customer adds or updates their shipping information.  |
| scPaymentInfoAdded    | Payment Info Added   | Triggered when a customer adds or updates their payment information.   |
| scTrialStarted        | Trial Started        | Triggered when a customer starts a free trial.                         |
| scSubscriptionStarted | Subscription Started | Triggered when a customer starts a paid subscription.                  |

### How to Connect SureCart Store to Google Analytics

If you did not connect your Google Analytics account with the Google Site Kit plugin upon installation, then you can follow the steps below.

- In the Site Kit setup wizard, you'll have an option to connect to Google Analytics. Click on the **Connect Service** button for Google Analytics.
- Follow the prompts to grant permission to access your Google Analytics account.
- Choose the Google Analytics property (website) you want to link to your WordPress site.
- Click **Configure Analytics** to finish the setup.

### How to Connect SureCart Store to Google Tag Manager

Once Google Analytics is connected to your Google Site plugin, go back to the Site Kit dashboard.

- From the **Settings**, navigate to **Connect More Services**.
- Locate **Tag Manager** in the list of services and click on it.
- Follow the prompts to grant permission to access your Google Tag Manager account.
- Select the Google Tag Manager container you want to use with your WordPress site.
- Click **Configure Tag Manager** to finish the setup.

After completing these steps, you should see a dashboard within Google Site Kit that displays information about your website's performance, including data from Google Analytics and Google Tag Manager.

From here, you will need to "forward" any events from Google Tag Manager to GA4. To do this add a new "Tag" to your workspace, then select your existing Google Analytics GA4 Pageview configuration tag, then use `{{Event}}` for the Event name.
