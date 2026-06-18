---
source_url: https://surecart.com/docs/track-events-with-fbpixels
source: surecart-kb
scraped: true
---

/ [Knowledge Base](https://surecart.com/docs/)/ [Integrations](https://surecart.com/docs-category/integrations/)/How to Track SureCart Events with Facebook Pixel

# How to Track SureCart Events with Facebook Pixel

If you want to track SureCart events, like purchase events or add-to-cart events, through Facebook pixel, we got you covered.

In this article, we are going to show you how to send tracking information to Facebook through Google Tag Manager (GTM) and also through custom code.

Let's get started.

### **Creating Custom Events Trigger in GTM & Facebook Pixel Tag**

In this section, we will guide you through the process of setting up Google Tag Manager (GTM) to track various events on your website.

To illustrate, let's consider the example of a "view product event" that should be triggered when a visitor views a specific product on your SureCart store.

The same steps can be applied to track other events such as Search, Initiate Checkout, Start Trial, and so on.

For example, if you have a specific event on your website that you want to track, like the View Product event, you can do it in two simple steps.

1. Create a Custom Event Trigger in Google Tag Manager.
2. Associate the Trigger with Your Facebook Pixel Tag.

We've described both the steps further.

#### Step 1: Create a Custom Event Trigger:

- In your GTM container, go to **Triggers**.
- Click the **New** button to create a new trigger.
- Give your trigger a descriptive name, like "Event - View Product".
- In the **Trigger Configuration** section, choose **Custom Event** as the trigger type.
- Enter the event name in the Event name field exactly as it appears in your dataLayer push. For example, if it's "scProductViewed," type "scProductViewed."
- Under **This trigger fires on**, select **All Custom Events**.
- Click on the **Save Button** to save your changes.

Now that we have the trigger, we need to create the tags for Facebook.

#### Step 2: Creating Facebook Pixel Tag in Google Tag Manager

Now, we are going to cover the steps to create a Facebook Tag using Google Tag Manager. Please follow the steps below to create a Facebook Pixel Tag.

- In your GTM container, go to **Tags**.
- Click the **New** button to create a new tag.
- Give your tag a descriptive name, like "Facebook - View Product".
- In the **Tag Configuration** section, select **Custom HTML** as the tag type.
- In the HTML field, paste the Facebook Pixel code that you get from Facebook.
- In the **Triggering** section, click to add a trigger.
- Choose the same custom event trigger you used for the Google Analytics tag (For example, "Event - View Product").
- Click **Save** to save your Facebook Pixel Tag.
- After creating the tag and associating it with the trigger, click the **Submit** or **Publish** button in the upper-right corner of GTM to publish your changes live.

By following these steps, you'll have set up the Facebook Pixel Tag in Google Tag Manager, and it will fire when the View Product event occurs on your website.

Now you just need to replicate the same steps for all the events you want to track.

### **Facebook Pixel Integration Through Custom Code**

You can track Facebook pixel events without Google Tag Manager if you prefer. To do this, you should add a bit of custom code to your site.

The easiest way to do this is to use a [free code snippets plugin](https://wordpress.org/plugins/code-snippets/), though you can do this in your theme or with a separate plugin too.

Our checkout component emits an event called scOrderPaid, which happens when a checkout is paid. This lets you listen for the event, and look at the checkout data to send to Facebook pixel.

So if you want to choose this method, you can simply add the custom code to your site's footer, listening for the `scCheckoutCompleted` event and calling `fbq('track', 'Purchase', {...})` with the checkout data.

In this quick reference article, we've covered the essentials of tracking SureCart events in Facebook Pixel using Google Tag Manager (GTM) and also straight with a custom code.

We hope this was helpful. If you run into any problems or have questions, reach out to our support team. We are always ready to help and provide further guidance.
