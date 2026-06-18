---
source_url: "https://docs.wpsocialninja.com/guide/business-reviews/tripadvisor-configuration"
title: "Tripadvisor Reviews | WP Social Ninja"
---

# Tripadvisor Reviews | WP Social Ninja

WP Social Ninja integrates with TripAdvisor, allowing you to collect and display reviews from the platform to enhance your business's credibility.

It offers two methods for gathering TripAdvisor reviews: using a **Business URL** or through an **API key**. We recommend using the API method, as it allows for a more comprehensive and reliable data transfer. With the API, you can control the frequency and volume of data requests, ensuring a seamless and customizable review collection process.

In this article, we will guide you through the steps to obtain the TripAdvisor API from your TripAdvisor account and how to connect it to WP Social Ninja.

## **Get Tripadvisor Credentials** [​](https://docs.wpsocialninja.com/guide/business-reviews/tripadvisor-configuration#get-tripadvisor-credentials)

To obtain your TripAdvisor credentials, log in to your TripAdvisor [developer account](https://www.tripadvisor.com/developers). From the navigation bar, select **My API** and then click the **Create API Key** button.

![Tripadvisor API Configuration 1](https://docs.wpsocialninja.com/assets/Tripadvisor-1-scaled.Dl47VThK.webp)

TIP

TripAdvisor offers a free API key that allows up to 5,000 requests for local details, photos, or reviews but you have to provide billing details to get this free API. To access additional requests and features, you will need to upgrade to their paid plans. For more information, refer to their [_API documentation_](https://tripadvisor-content-api.readme.io/reference/overview)_._

To generate your API key, you will need to provide TripAdvisor with some information about your business.

![Tripadvisor API Configuration 2](https://docs.wpsocialninja.com/assets/Tripadvisor-2.DAM01Odv.webp)

Verifying your website is necessary for creating the API. Enter your website address and register it under your business to ensure a smooth API transfer.

In the API Key restriction section, input your domain name and click the **Save** button.

![Tripadvisor API Configuration 3](https://docs.wpsocialninja.com/assets/Tripadvisor-3.B_JFZEfU.webp)

Once you’ve completed the form, your API key will be generated and you will see the domain name you have registered for this API. Just click the **Copy to Clipboard** button to copy the API key.

![Tripadvisor API Configuration 4](https://docs.wpsocialninja.com/assets/image.CnX5yYHd.png)

## **Get the Place ID** [​](https://docs.wpsocialninja.com/guide/business-reviews/tripadvisor-configuration#get-the-place-id)

To set up TripAdvisor with WP Social Ninja, you'll need the **Place ID** from your TripAdvisor business profile. You can find it in the URL of your Business profile.

Look for an ID in the URL that starts with the letter 'd'—this is your Place ID. In this case, the actual Place ID is '752551,' excluding the 'd' prefix. Copy the code from the URL.

![Tripadvisor API Configuration 5](https://docs.wpsocialninja.com/assets/Tripadvisor-ID-scaled.DrODOZFp.webp)

## **Configuring Tripadvisor with WP Social Ninja** [​](https://docs.wpsocialninja.com/guide/business-reviews/tripadvisor-configuration#configuring-tripadvisor-with-wp-social-ninja)

After receiving your TripAdvisor credentials, navigate to your WP Social Ninja dashboard and select [Platform](https://docs.wpsocialninja.com/guide/getting-started/all-platforms-of-wp-social-ninja) from the navigation bar. Search for TripAdvisor and click on the **Settings** icon button.

![Tripadvisor API Configuration 6](https://docs.wpsocialninja.com/assets/tripadvisor-review-1.DplNadw7.webp)

A TripAdvisor configuration popup will appear. Select Credential Type: **API Key**, then paste your **API Key** and **ID** into the appropriate fields. Finally, click the **Save** button.

![Tripadvisor API Configuration 7](https://docs.wpsocialninja.com/assets/tripadvisor-review-2.rbZiG9Jx.webp)

TIP

WP Social Ninja will initially show the 5 most recent reviews from TripAdvisor, which will be stored locally on your site. The plugin will regularly check for new reviews and update your feed as they become available.
