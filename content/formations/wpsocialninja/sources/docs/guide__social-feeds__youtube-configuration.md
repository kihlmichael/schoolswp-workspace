---
source_url: "https://docs.wpsocialninja.com/guide/social-feeds/youtube-configuration"
title: "YouTube Configuration | WP Social Ninja"
---

# YouTube Configuration | WP Social Ninja

The YouTube Feed feature in WP Social Ninja allows you to easily connect your YouTube channel and display your videos, playlists, and channel details directly on your WordPress website. Once connected, your YouTube content updates automatically, keeping your site fresh and engaging.

In this guide, you’ll learn how to configure the YouTube platform and connect your channel using either of two methods: the **API Key (recommended for stability)** or **OAuth 2.0 (Connect via Google)**. Follow the steps below to complete the setup and start displaying your YouTube content on your site.

## Configure the YouTube Platform [​](https://docs.wpsocialninja.com/guide/social-feeds/youtube-configuration#configure-the-youtube-platform)

To get started, you’ll first need to configure the YouTube platform.

From your WordPress dashboard, navigate to **WP Social Ninja → [Platforms](https://docs.wpsocialninja.com/guide/getting-started/all-platforms-of-wp-social-ninja)**. Click the **Social Feeds** tab. Find **YouTube** in the list and click the **Connect** button.

A pop-up will appear with two connection types:

*   API Key (Recommended)
*   OAuth 2.0 (Connect Via Google)

This guide will explain both methods.

![Connecting the YouTube platform in WP Social Ninja](https://docs.wpsocialninja.com/assets/access-youtube-feed.9IgtCk42.webp)

## Method 1: API Key (Recommended) [​](https://docs.wpsocialninja.com/guide/social-feeds/youtube-configuration#method-1-api-key-recommended)

This is the most stable and recommended method. It requires you to create a free API Key from the Google Cloud Console.

### Get Your API Key from Google [​](https://docs.wpsocialninja.com/guide/social-feeds/youtube-configuration#get-your-api-key-from-google)

Go to the [Google Cloud Console](https://console.cloud.google.com/) and log in with your Google account. In the top menu, click the **Select a Project** dropdown. Here, a pop-up appears; click **New Project**.

![Creating a new project in Google Cloud Console](https://docs.wpsocialninja.com/assets/google-search-console.DkMe53c1.webp)

Enter a **Project name** (e.g., "WP Social Ninja") and click **Create**.

![Create Project Name](https://docs.wpsocialninja.com/assets/new-project.CERjuliO.webp)

Once the project is created, go to **APIs & Services → Credentials** from the main menu.

![Navigating to Credentials in Google Cloud Console](https://docs.wpsocialninja.com/assets/api-service.C133eYvQ.webp)

Now, click the **\+ Create Credentials** button at the top, and you will see an **API key** option.

![Creating a new API Key](https://docs.wpsocialninja.com/assets/api-keys.ClhgDFrb.webp)

Here, a new pop-up arrives. Enter the name of your API key and click on the **Create** button.

![Create API Key](https://docs.wpsocialninja.com/assets/create-api-key.BH5ErlKT.webp)

After that, a new pop-up will appear with your new key. Click the **Copy** icon.

![Copying the newly created API Key](https://docs.wpsocialninja.com/assets/copy-api-key.BT8WYoKs.webp)

In order to configure the YouTube Feed, you need to enable the **YouTube Data API v3** button; otherwise, the API Key will not work. Now, click on the **API Library** from the **APIs & Services** to enable the YouTube Data API v3.

![YouTube Data API v3 Library](https://docs.wpsocialninja.com/assets/api-library-new.BPh0q66Z.webp)

From the API Library, scroll down and select the **YouTube Data API v3**.

![Selecting the YouTube Data API v3 from the API Library](https://docs.wpsocialninja.com/assets/youtube-data-api-v3.D9P3CtNB.webp)

### Add the API Key to WP Social Ninja [​](https://docs.wpsocialninja.com/guide/social-feeds/youtube-configuration#add-the-api-key-to-wp-social-ninja)

Now, return to your WordPress dashboard and open the YouTube configuration pop-up. Select the **API Key (Recommended)** option. **Paste** your key into the **YouTube API Key** field. Click the **Save** button. Your YouTube account is now connected.

![Pasting the API Key into WP Social Ninja settings](https://docs.wpsocialninja.com/assets/save-api-key.qAN2F6gZ.webp)

You will get a successful message like the screenshot below:

![YouTube connection success message](https://docs.wpsocialninja.com/assets/youtube-successful.BJtW3Fai.webp)

## Method 2: OAuth 2.0 (Connect Via Google) [​](https://docs.wpsocialninja.com/guide/social-feeds/youtube-configuration#method-2-oauth-2-0-connect-via-google)

This is a fast method that uses a temporary access code.

First, select **OAuth 2.0 (Connect Via Google)** from the pop-up. Click the **Sign In and Get Google Access Code** button.

![Selecting the OAuth 2.0 connection method](https://docs.wpsocialninja.com/assets/0auth2.eRSGD4_g.webp)

A new Google pop-up window will appear. Choose the Google Account that manages your YouTube channel.

![Google account selection pop-up](https://docs.wpsocialninja.com/assets/choose-google-account.AV66vW-C.webp)

Next, click the **Continue** button to permit WP Social Ninja.

![Granting Google permissions to WP Social Ninja](https://docs.wpsocialninja.com/assets/sign-in-google-accounts.BpXLabEX.webp)

Google will give you an **Access Code**. **Copy** this code.

![Copying the Google Access Code](https://docs.wpsocialninja.com/assets/copy-access-key.kbcTjUlq.webp)

Return to the WP Social Ninja dashboard, paste the code into the **Access Code** field, and click **Save**.

![Pasting the Access Code into WP Social Ninja](https://docs.wpsocialninja.com/assets/save-api-key1.WX7dMpp0.webp)

Now that your YouTube account is connected, that’s it.
