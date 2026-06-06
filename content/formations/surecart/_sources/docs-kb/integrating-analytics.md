---
source_url: https://surecart.com/docs/integrating-analytics
source: surecart-kb
scraped: true
---

/ [Knowledge Base](https://surecart.com/docs/)/ [Integrations](https://surecart.com/docs-category/integrations/)/General Support Guide for Integrating Analytics with Any Solution

# General Support Guide for Integrating Analytics with Any Solution

Many SureCart users want to integrate their store analytics with platforms beyond Google Analytics, such as Facebook Pixel, Fathom, or custom analytics solutions. SureCart provides flexibility for tracking a variety of events and data points to help store owners analyze their business performance across various platforms.

This guide will outline the general steps for integrating SureCart with any analytics platform.

### **Understanding the Basics**

SureCart automatically tracks several key events related to customer behavior in your store. These include:

- Add to Cart
- Checkout Initiated
- Purchase Completed
- Subscription Started

While SureCart offers built-in integrations for popular platforms like Google Analytics and Facebook Pixel, you can integrate other solutions by leveraging SureCart's ability to fire custom JavaScript events or send data to third-party platforms via webhooks or API connections.

### **General Steps for Analytics Integration**

**Step 1: Identify the Key Events to Track**

Decide which events are critical to your store. Some common events include:

- View Product
- Add to Cart
- Begin Checkout
- Purchase Completed
- Subscription Start

SureCart fires these events automatically, and you can listen to them or customize the events you want to track.

Here is a table for all the events that can be tracked in SureCart:

| **Event**             | **Event Name**       | **Description**                                                                       |
| --------------------- | -------------------- | ------------------------------------------------------------------------------------- |
| scAddedToCart         | Added to Cart        | Triggered when a customer adds an item to their shopping cart.                        |
| scRemovedFromCart     | Removed from Cart    | Triggered when a customer removes an item from their shopping cart.                   |
| scViewedCart          | Viewed Cart          | Triggered when a customer views their shopping cart.                                  |
| scProductViewed       | Product Viewed       | Triggered when a customer views a product page.                                       |
| scCheckoutInitiated   | Checkout Initiated   | Triggered when a customer begins the checkout process.                                |
| scCheckoutCompleted   | Checkout Completed   | Triggered when a customer successfully completes the checkout process.                |
| scShippingInfoAdded   | Shipping Info Added  | Triggered when a customer adds or updates their shipping information during checkout. |
| scPaymentInfoAdded    | Payment Info Added   | Triggered when a customer adds or updates their payment information during checkout.  |
| scTrialStarted        | Trial Started        | Triggered when a customer starts a free trial for a subscription-based product.       |
| scSubscriptionStarted | Subscription Started | Triggered when a customer starts a paid subscription for a product.                   |

**Step 2: Set Up Your Analytics Platform**

Each analytics platform will have a method for tracking events or actions on your site. Make sure your analytics platform is properly installed on your site, typically by embedding a tracking code snippet in the header of your WordPress site.

**Step 3: Listen for SureCart Events**

SureCart triggers several events when actions are performed by customers. You can use JavaScript event listeners to capture these events and send data to your preferred analytics platform.

For example, the following event listener captures when the checkout process is completed:

```javascript
window.addEventListener("scCheckoutCompleted", function (e) {
  const checkoutData = e.detail; // Checkout data is available here.
  // Use the data to send to your analytics platform
});
```

**Step 4: Send the Data to Your Analytics Platform**

Once you capture the event, the next step is to send the relevant data to your analytics platform. This can vary depending on the platform you're using. For example, for Facebook Pixel, Fathom, or custom solutions, use their respective JavaScript APIs or HTTP requests.

**Step 5: Test and Verify**

After setting up the event listeners and data-sending functions, perform actions on your SureCart store (like adding items to the cart or completing a purchase). Use your analytics platform's dashboard or logs to verify that the events are tracked correctly.

### **Additional Tools for Integration**

If you need more flexibility, consider the following options:

- **Webhooks**: SureCart supports sending data via webhooks, allowing you to push event data to a variety of endpoints. You can configure webhooks in SureCart's settings to notify your analytics solution when certain actions occur.

- **API Integrations**: If your analytics platform provides an API, you can integrate it directly with SureCart using custom code. Make API calls from your store to log events and track actions.

SureCart makes it easy to integrate with any analytics platform. By leveraging custom JavaScript and event listeners, you can capture essential user interactions and send them to your analytics solution of choice.

For more detailed tracking or custom requirements, consider working with a developer or using available SureCart webhooks to automate event tracking.

If you need help with specific integrations, check out SureCart's [Developer Documentation](https://developer.surecart.com/) or consult the community for support.
