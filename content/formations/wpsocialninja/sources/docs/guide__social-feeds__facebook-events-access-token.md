---
source_url: "https://docs.wpsocialninja.com/guide/social-feeds/facebook-events-access-token.html"
title: "Facebook Events Access Token | WP Social Ninja"
---

# Facebook Events Access Token | WP Social Ninja

With WP Social Ninja, adding your Facebook Page events to your WordPress site is quick and simple. In this guide, we'll walk you through how to connect your Facebook Page with WP Social Ninja and display your events directly on your website.

## **Facebook Event Access Settings** [​](https://docs.wpsocialninja.com/guide/social-feeds/facebook-events-access-token#facebook-event-access-settings)

To access the Facebook Event Access settings in WP Social Ninja, navigate to the **Platform** tab from the top menu, then click the **Settings** icon.

![wpsn 1](https://docs.wpsocialninja.com/assets/event-access-token-1.DJeqRdGb.webp)

A pop-up for Facebook Configuration will now appear. From the dropdown, select **Connect Event Access Token**. You’ll see that both your **Facebook Page ID** and **Event Access Token** are required to connect your Facebook Events.

![wpsn 2](https://docs.wpsocialninja.com/assets/event-access-token-2.Brb6mPUp.webp)

Now, we'll walk you through how to connect your **Facebook Page Events** with **WP Social Ninja**. To get started, you'll first need to **create a Facebook App** to collect the required credentials.

## **Facebook App** [​](https://docs.wpsocialninja.com/guide/social-feeds/facebook-events-access-token#facebook-app)

To create a Facebook App, visit the [Facebook Developer](https://developers.facebook.com/) site. Log in to your account and click on the **My Apps** button from the top menu.

TIP

Note that, You must log in with your personal Facebook profile’s username and password. Businesses cannot register as developers on Facebook; only individuals may do so.

![fb event app 1](https://docs.wpsocialninja.com/assets/event-access-token-3.DrbWoapA.webp)

Now you’ll see the app creation page. Just click on the **Create App** button to get started.

![fb event app 2](https://docs.wpsocialninja.com/assets/event-access-token-4.T1XMLnCx.webp)

Give your app a name and enter a contact email. Once you’ve filled those in, click the **Next** button.

![fb event app 3](https://docs.wpsocialninja.com/assets/event-access-token-5.CBBzGAV8.webp)

In the **Use Cases** section, select **Others**, then proceed to the next step.

![fb event app 4](https://docs.wpsocialninja.com/assets/event-access-token-6.C9KZcssB.webp)

Next, select **Business** as your **App Type** and click on the **Next** button to proceed to the next page.

![fb event app 5](https://docs.wpsocialninja.com/assets/event-access-token-7.B8i3XrW7.webp)

You’ll now see the App details page. Here, you can make any changes if needed, or simply leave the information as it is. Once you're ready, click the **Create App** button to finalize.

A popup will appear asking you to re-enter your Facebook password for security. Type in your password and click the **Submit** button.

![fb event app 6](https://docs.wpsocialninja.com/assets/event-access-token-8.C8eRI2_C.webp)

## **Get the Credentials** [​](https://docs.wpsocialninja.com/guide/social-feeds/facebook-events-access-token#get-the-credentials)

Go to your [Meta App Developer Account](https://developers.facebook.com/apps/) and click on the App that you have created now.

Now the App development page will appear. From the left sidebar, go to **App Settings** and select **Basic**.

![fb event extra 2](https://docs.wpsocialninja.com/assets/event-access-token-9.CxCfyN_j.webp)

Next, go to the [API Explorer page](https://developers.facebook.com/tools/explorer/). First, choose the Meta **App** you created earlier. Then, in the **User or Page** dropdown, select **User Token** and enable the following permissions:

*   page\_events
    
*   pages\_read\_engagement
    
*   pages\_read\_user\_content
    
*   pages\_show\_list
    

After setting the permissions, click on the **Generate Access Token** button. Once the token is created, copy it and save it for later use.

![fb event extra 3](https://docs.wpsocialninja.com/assets/event-access-token-10.vskvb8cw.webp)

## **Long Lived Access Token** [​](https://docs.wpsocialninja.com/guide/social-feeds/facebook-events-access-token#long-lived-access-token)

Standard Facebook User Access Tokens expire quickly. To maintain a stable connection for your Facebook Events feed, you should convert your short-lived token into a long-lived one using Facebook's official tool.

Follow these steps to generate your token.

*   **Navigate to the Access Token Debugger**
    
    *   Go to the [Facebook Access Token Debugger](https://developers.facebook.com/tools/debug/accesstoken/) and log in to your Facebook account.
*   **Debug Your Current Token**
    
    *   Paste your existing **User Access Token** into the input field and click the **Debug** button.

![access token debugger 1](https://docs.wpsocialninja.com/assets/event-access-token-15.CHb0Sapp.webp)

*   **Extend the Token**
    *   On the results page, scroll to the bottom and click the **Extend Access Token** button.

![access token debugger 2](https://docs.wpsocialninja.com/assets/event-access-token-16.82kCqPV4.webp)

*   **Copy the New Token**
    *   A new, long-lived token will be generated. Copy this new token to use in WP Social Ninja.

![access token debugger 3](https://docs.wpsocialninja.com/assets/event-access-token-17.0HoCTGIj.webp)

*   This is your **Event Access Token**, paste it to the required field of the WP Social Ninja dashboard. And to get the **Page ID**, you need to go to the [**link**](https://wpsocialninja.com/access-token-generator/?id=facebook-feed).
    
*   Now, go to the **Facebook Feed** → click on the **Continue with Facebook** button & then a popup will appear.
    
*   Select Continue as – (your Facebook ID)
    

## **Configure Facebook Page Event with WP Social Ninja** [​](https://docs.wpsocialninja.com/guide/social-feeds/facebook-events-access-token#configure-facebook-page-event-with-wp-social-ninja)

Go back to your WP Social Ninja and open the **Facebook Event Access Configuration** settings. Paste the **Page ID and Long Lived Access Token** you copied earlier into the respective fields and click on the **Connect** button.

Next, click on the **Add New Template** button to set up and customize the template as per your preferences.

![fb event app 14](https://docs.wpsocialninja.com/assets/WPSN-18.DSY7i_7Z.webp)

INFO

Events created by a co-host of the Facebook Page will not appear in your feed. Facebook's API does not share data for events where the connected Page is only a co-host. To ensure an event shows up on your website, it must be created directly by the main Facebook Page itself.

This is how you can display your Facebook Page Events on your site. If you have any further questions or need assistance with this configuration, please don’t hesitate to contact [us](https://wpmanageninja.com/support-tickets).
