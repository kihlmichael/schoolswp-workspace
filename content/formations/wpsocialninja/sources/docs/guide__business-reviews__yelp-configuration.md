---
source_url: "https://docs.wpsocialninja.com/guide/business-reviews/yelp-configuration"
title: "Yelp Reviews | WP Social Ninja"
---

# Yelp Reviews | WP Social Ninja

This guide will show you how to connect your Yelp Business Page to WP Social Ninja's **Business Reviews** feature.

Yelp uses an API Key to connect. This is a simple key that you generate on Yelp's developer website. This guide will walk you through the entire process, step-by-step.

> **Use Case:** This is essential for restaurants, cafes, local shops, and service-based businesses. By connecting Yelp, you can display your valuable, high-star reviews directly on your website, building instant trust and credibility with new customers.

## Part 1: Start the Connection [​](https://docs.wpsocialninja.com/guide/business-reviews/yelp-configuration#part-1-start-the-connection)

First, let's start inside your WordPress dashboard to see what you need.

1.  From your WordPress dashboard, navigate to **WP Social Ninja** in the left-hand menu, and then click on [Platforms](https://docs.wpsocialninja.com/guide/getting-started/all-platforms-of-wp-social-ninja).
2.  On the "Platforms" page, find the **Yelp** row in the Business Review section then click the **Settings icon** button with it.

![Yelp Configuration for Review](https://docs.wpsocialninja.com/assets/yelp-business-review-1.CC-pC9SK.webp)

A pop-up window will appear with fields labeled **API Key** & **Place ID**. This is the things you need to get from Yelp.

![Yelp Configuration for Review](https://docs.wpsocialninja.com/assets/yelp-business-review-2.DyAk7yTH.webp)

## Part 2: Yelp API Key [​](https://docs.wpsocialninja.com/guide/business-reviews/yelp-configuration#part-2-yelp-api-key)

Now, let's go to Yelp's developer portal to generate your key.

### Step 1: Go to Yelp Developers [​](https://docs.wpsocialninja.com/guide/business-reviews/yelp-configuration#step-1-go-to-yelp-developers)

In a new browser tab, go to the [**Yelp Developers website**](https://www.yelp.com/developers) and log in to your [Yelp account](https://www.yelp.com/developers/v3/manage_app) (the one associated with your business page).

### Step 2: Create App [​](https://docs.wpsocialninja.com/guide/business-reviews/yelp-configuration#step-2-create-app)

Once login go to the **Manage App** section and create an App by filling in the required information:

*   **App Name:** Give it a name you'll recognize, like "My Website Reviews."
*   **Industry:** Select the industry that best fits your business.
*   **Your Contact Email:** Enter your email address.
*   **Description:** Write a brief description, such as "Connecting Yelp reviews to my website."

Click the **Create App** button.

Yelp will immediately take you to a "Success!" page. On this page, you will see your new **API Key**. This is the key you need! Copy the API Key to your clipboard.

INFO

Yelp’s Fusion API no longer provides reviews for free. To fetch Yelp reviews in WP Social Ninja, you need a **Yelp Pro plan**:

*   **Pro Enhanced** → Up to **3 review excerpts per business**.
    
*   **Pro Premium** → Up to **7 review excerpts per business**.
    

These limits are controlled by Yelp, not WP Social Ninja. [Check Yelp Plan and Pricing](https://business.yelp.com/data/products/fusion/).

![Yelp Configuration for Review](https://docs.wpsocialninja.com/assets/yelp-business-review-3.F1l6XhLi.webp)

## Part 3: Get Your Place ID (Add Your Business) [​](https://docs.wpsocialninja.com/guide/business-reviews/yelp-configuration#part-3-get-your-place-id-add-your-business)

Now you must add your specific business. To do this, you need your business's **Place ID**.

### Step 1: Find Your Yelp Place ID [​](https://docs.wpsocialninja.com/guide/business-reviews/yelp-configuration#step-1-find-your-yelp-place-id)

Your Place ID is simply the unique part of your business's URL on Yelp.com.

1.  Go to **Yelp.com** in your browser.
2.  Search for your business name and city.
3.  Click on your business from the search results to open its main page.
4.  Look at the URL in your browser's address bar. Your Place ID is the text that comes after `https://www.yelp.com/biz/`.

> **Example URL:** `https://www.yelp.com/biz/bocconcino-san-francisco`**Your Place ID:** `bocconcino-san-francisco`

Carefully copy this **Place ID**.

![Yelp Configuration for Review](https://docs.wpsocialninja.com/assets/yelp-business-review-4.BGn4wbPW.webp)

## Part 4: Connect Your Yelp Account [​](https://docs.wpsocialninja.com/guide/business-reviews/yelp-configuration#part-4-connect-your-yelp-account)

Now for the final, easy step.

### Paste Your API Key & Place ID [​](https://docs.wpsocialninja.com/guide/business-reviews/yelp-configuration#paste-your-api-key-place-id)

1.  Go back to your WordPress dashboard (where you still have the WP Social Ninja pop-up open from Part 1).
2.  Paste the **API Key** you just copied into the "API Key" field.
3.  Then Paste your **Place ID** (e.g., `bocconcino-san-francisco`) into the field.
4.  Now click on the **Save** button.

![Yelp Configuration for Review](https://docs.wpsocialninja.com/assets/yelp-business-review-5.BVe1cKcZ.webp)

Your business is now fully connected and will begin to sync reviews.

The **Yelp** row will now show a green "Connected" status.

![Yelp Configuration for Review](https://docs.wpsocialninja.com/assets/yelp-business-review-6.CsoraOSO.webp)

## Next Steps [​](https://docs.wpsocialninja.com/guide/business-reviews/yelp-configuration#next-steps)

Congratulations! Your Yelp account is fully connected.

Now that your account is set up, you're ready for the fun part:

*   Click the **Add New Template** button to go to the template editor and start designing your **Business Reviews** template for Yelp.
