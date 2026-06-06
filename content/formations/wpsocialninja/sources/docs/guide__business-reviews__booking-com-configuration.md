---
source_url: "https://docs.wpsocialninja.com/guide/business-reviews/booking-com-configuration"
title: "Booking.com Reviews | WP Social Ninja"
---

# Booking.com Reviews | WP Social Ninja

WP Social Ninja enables you to showcase reviews directly from your Booking.com business profile, adding credibility to your business and enhancing trust among potential customers. With this feature, you can create customized templates to make your reviews look more appealing and aligned with your website's style.

In this guide, we’ll walk you through the steps to display Booking.com reviews on your website.

TIP

You’ll need WP Social Ninja Pro to access and display Booking.com reviews on your site.

## **Enable Booking.com Platform** [​](https://docs.wpsocialninja.com/guide/business-reviews/booking-com-configuration#enable-booking-com-platform)

Navigate to your **WP Social Ninja** dashboard and select [Platform](https://docs.wpsocialninja.com/guide/getting-started/all-platforms-of-wp-social-ninja) from the navigation bar. Locate the **Booking Platform** and click on the **Settings** icon to configure it.

![booking review 1](https://docs.wpsocialninja.com/assets/booking-review-1.D_QmDkBz.webp)

## **Steps to Configure Booking.com Reviews** [​](https://docs.wpsocialninja.com/guide/business-reviews/booking-com-configuration#steps-to-configure-booking-com-reviews)

Before fetching reviews from Booking.com using your Business Profile URL, you need to complete three additional steps:

*   **Copy the Cookie AWS-WAF-Token Cookie Value from the Booking.com Site**
    
*   **Add the AWS-WAF-Token Cookie Value to a Snippet**
    

Below is a step-by-step guide to complete these settings:

## **Copy the Cookie AWS-WAF-Token** [​](https://docs.wpsocialninja.com/guide/business-reviews/booking-com-configuration#copy-the-cookie-aws-waf-token)

Open **Booking.com** and navigate to the business profile whose reviews you want to display on your website.

Access your browser's **Inspect** mode (usually by right-clicking on the page and selecting "Inspect").

In the Inspect mode, go to the **Application** tab and select **Cookies**.

Search for the **AWS-WAF-Token** in the cookies list then copy the value of the AWS-WAF-Token cookie and save it for later use.

![booking review 4](https://docs.wpsocialninja.com/assets/booking-review-2.mhFZVfE4.webp)

## **Add the AWS-WAF-Token in a Snippet** [​](https://docs.wpsocialninja.com/guide/business-reviews/booking-com-configuration#add-the-aws-waf-token-in-a-snippet)

To use the **AWS-WAF-Token** cookie value you copied earlier, you'll need to add it to your site using a code snippet. This can be done easily with a snippet plugin.

TIP

We recommend using **[FluentSnippet](https://fluentsnippets.com/)** on your WordPress site for a seamless experience. However, you can use any other snippet plugin of your choice.

Follow these steps to add the code snippet:

*   Open **FluentSnippet** and click on the **Create Snippet** button.

php

```

add_filter('wpsocialreviews/booking_header_request_cookie_set', function($headers) {

    $headers['cookie'] = 'aws-waf-token=(Cookie value goes here)';    return $headers;

});
```

*   In the code editor field, insert the code above:
    
*   Replace **Cookie value goes here** with the **AWS-WAF-Token** value you copied earlier.
    
*   Save the snippet to apply the changes.
    

![booking review 5](https://docs.wpsocialninja.com/assets/booking-review-3.CYifDbsm.webp)

## **Business URL from Booking** [​](https://docs.wpsocialninja.com/guide/business-reviews/booking-com-configuration#business-url-from-booking)

Navigate to your business profile on Booking.com and copy the **Business URL** directly from the address bar of your browser.

![booking review 6](https://docs.wpsocialninja.com/assets/booking-review-4.C3qT7xuT.webp)

Next, return to your **WP Social Ninja Booking Configuration** and paste the **Booking.com Business Profile URL** you copied earlier. Click on the **Save** button, and you’ll see that your business has been successfully added.

![booking review 2](https://docs.wpsocialninja.com/assets/booking-review-5.2EUWhCWM.webp)

If you wish to add another business profile, simply click on the **Add More Business** button and repeat the same steps.

To customize your **Booking.com Reviews Template**, click on the **Create a Template** button and start personalizing your [template](https://docs.wpsocialninja.com/guide/business-reviews/create-template). Keep in mind, if you don't create a template, your reviews won't be displayed, as the template won't be created automatically.

![booking review 7](https://docs.wpsocialninja.com/assets/booking-review-6.CNOVzlJL.webp)

That's how you can easily fetch your **Booking.com** business profile reviews on your site using **WP Social Ninja**.
