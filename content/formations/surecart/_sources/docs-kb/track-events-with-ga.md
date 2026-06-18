---
source_url: https://surecart.com/docs/track-events-with-ga
source: surecart-kb
scraped: true
---

/ [Knowledge Base](https://surecart.com/docs/)/ [Integrations](https://surecart.com/docs-category/integrations/)/How to Track Add to Cart and Purchase Events with Google Analytics

# How to Track Add to Cart and Purchase Events with Google Analytics

Using Google Analytics, you can track the "Add to Cart" and "Purchase" events on your SureCart store.

This means that when someone adds a product to their cart or makes a purchase in your store, you can monitor and analyze these actions through Google Analytics.

This functionality is valuable for easily tracking customer behavior within your store so you can make data-driven decisions.

In this article, we'll see two ways to connect your SureCart to Google Analytics for tracking Add to Cart and Purchase events.

These methods are

- Using Google Site Kit plugin on your website.
- Using Google Tag Manager.

We are going to cover both in this article.

Regardless of the method, you need to have Google Analytics on your website, and the simplest way is by using the [Google Site Kit plugin](https://wordpress.org/plugins/google-site-kit/).

## Automatically Track the Events Using Site Kit Plugin

To automatically track the Add To Cart and Purchase events, Install and activate the Google Site Kit plugin on your website.

This plugin will display Google Analytics stats in your WordPress Admin area.

This method works effortlessly, without any complications. We recommend it only if you need to track Add To Cart and/or Purchase events due to its simplicity.

With this approach, whenever someone adds a product to their cart or makes a purchase, you can easily view this information in your Google Analytics statistics.

Now if you want to track additional events, you can connect your SureCart store with [Google Tag Manager](https://tagmanager.google.com/).

Consider this analogy: When you use SureCart with Google Analytics directly, it's like a phone that automatically dials your friend's number when you make a purchase.

However, if you're using Tag Manager, it's similar to having an intermediary that forwards your call to your friend after you've made a purchase. We'll assist you in setting up that call forwarding.

## Tracking the Custom Events Using Google Tag Manager

In this section, we'll walk you through the process of tracking different Google Analytics events in your SureCart store using Google Tag Manager.

If you haven't already, be sure to check out our article on [How to Track Events With Google Tag Manager](https://surecart.com/docs/custom-events-with-gtm/) so you can easily follow this guide.

Let's get started.

### **Setting Up Google Tag Manager (GTM) for Multi-Event Tracking with a Custom Trigger**

In this section, we are going to cover how to set up Google Tag Manager (GTM) to track the View Product event.

You can use the same steps to add other events like Search, Initiate Checkout, Start Trial, etc.

You can use the same trigger in Google Tag Manager (GTM) to track the events for Google Analytics, Facebook Pixel, or other platforms.

In GTM, [triggers](https://support.google.com/tagmanager/answer/7679316?hl=en) are used to determine when tags should fire based on certain conditions or events.

If you have an event on your website that you want to track, like View Product, you can create one custom event trigger for that event and then associate it with your Google Analytics tag.

Here's how you can do it:

**Step 1: Create your Google Tag Manager Account:**

Create a Google Tag Manager account and link it to your WordPress website. This is a straightforward process, just paste the provided GTM code snippet into your site header.

You can do this directly or utilize plugins like [HFCM](https://wordpress.org/plugins/header-footer-code-manager/) for assistance.

**Step 2: Create a Custom Event Trigger:**

- In your GTM container, go to **Triggers**.
- Click on the **New** button to create a new trigger.
- Provide a descriptive name for your trigger, such as "Event – View Product."

- Click on the **Trigger Configuration** section, then select **Custom Event** as the trigger type.

- Enter the event name in the **Event name** field exactly as it appears in your dataLayer push. For example, if it's "scProductViewed," type "scProductViewed."
- Under **This trigger fires on**, select **All Custom Events**.
- Click on the **Save Button** to save your changes.

Now that we have the trigger, we need to create the tags for Google Analytics.

### **Creating a Google Analytics Tag in Google Tag Manager for Event Tracking**

Now we are going to cover the steps to create the Google Analytics Tag using Google Tag Manager:

**Step 1: Create a New Tag and configure it:**

- In your GTM container, go to **Tags**
- Click the **New** button to create a new tag.
- Give your tag a descriptive name, like "GA4 – View Product"
- In the **Tag Configuration** section, select **Google Analytics → Analytics: GA4 Event** as the tag type.

**Step 2: Configure Google Analytics Settings:**

- Enter your GA4 **Measurement ID** and **Event Name** in their respective fields. To find your Measurement ID in your Google Analytics account, follow [these](https://support.google.com/analytics/answer/12270356?hl=en#:~:text=Find%20your%20measurement%20ID,row%20of%20the%20stream%20details.) steps.
- In the **Triggering** section, click to add a trigger.
- Choose the custom event trigger you created earlier (For example, "Event – View Product").

**Step 3: Save Your Tag and Publish Your Changes:**

- Click **Save** to save your Google Analytics Tag.
- After creating the tag and associating it with the trigger, click the **Submit**/ **Publish** button in the upper-right corner to publish your changes live.

By following these steps, you'll have set up the Google Analytics Tag in Google Tag Manager. GTM will fire when the **View Product** event occurs on your website.

Now you just need to replicate the same steps for all the events you want to track.

In this quick reference article, we've covered the essentials of tracking SureCart events in Google Analytics using Google Tag Manager (GTM).

If you encounter any issues or have questions during the importing process, don't hesitate to seek assistance from our support team. We are always ready to help and provide further guidance.
