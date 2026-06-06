---
source_url: "https://docs.wpsocialninja.com/guide/business-reviews/airbnb-configuration"
title: "Airbnb Reviews | WP Social Ninja"
---

# Airbnb Reviews | WP Social Ninja

This guide provides step-by-step instructions for connecting your Airbnb reviews with WP Social Ninja. Because Airbnb does not offer an official public API for reviews, this process requires a manual workaround to find the necessary connection keys directly from your Airbnb listing page.

## **Connect Your Airbnb for Reviews** [​](https://docs.wpsocialninja.com/guide/business-reviews/airbnb-configuration#connect-your-airbnb-for-reviews)

This guide will show you how to connect your Airbnb reviews to WP Social Ninja.

#### **Why is this Manual Process Needed?** [​](https://docs.wpsocialninja.com/guide/business-reviews/airbnb-configuration#why-is-this-manual-process-needed)

Unlike other platforms, Airbnb does not offer a public API that allows plugins like WP Social Ninja to easily fetch reviews. The standard connection method may not work reliably.

To solve this, we will use a manual workaround. This process involves finding a unique **API Key** and **Secret Key** from your Airbnb listing page. By adding these keys to your WordPress site, you give WP Social Ninja the credentials it needs to securely and successfully fetch your reviews.

**Disclaimer**: This method uses Airbnb's internal development tools. Because it is not an official public solution, Airbnb may change these keys in the future, which could cause the connection to break. If this happens, you will need to repeat this process to get the new keys.

### **Step 1: Find Your API Key and Secret Key** [​](https://docs.wpsocialninja.com/guide/business-reviews/airbnb-configuration#step-1-find-your-api-key-and-secret-key)

In this step, we will use your browser's developer tools to find the required keys from your Airbnb listing page.

*   **Open Your Airbnb Listing**
    
    *   Using a desktop browser (like Chrome or Firefox), navigate to the Airbnb listing page (**Room** or **Experience**) that you want to get reviews from.
*   **Open Developer Tools**
    
    *   Right-click anywhere on the page and select **Inspect** from the menu. This will open the Developer Tools panel.
    *   In the Developer Tools panel, click on the **Network** tab.
*   The term you search for in the Network tab's **Filter** box depends on the type of listing and information you need. Use the appropriate term from the list below:
    
*   **For Room Reviews:** Search for **StaysPdpReviewsQuery**.
    
*   **For a Room's Business Info**: Search for **StaysPdpSections**.
    
*   **For Experience/Service Reviews**: Search for **ReviewsModalContentQuery**.
    

NOTE

To find `ReviewsModalContentQuery`, you must click on the **Show all reviews** button on the Airbnb page; only then will this request appear in the list.

![airbnb review](https://docs.wpsocialninja.com/assets/show-all-review._gt24TUJ.webp)

After typing the correct term, refresh the page and click on the request that appears in the list to open its details.

TIP

You must find the secret keys from two different network requests: `StaysPdpReviewsQuery` and `StaysPdpSections` . Both are mandatory for the connection to work correctly.

### **For Room Reviews** (Required) [​](https://docs.wpsocialninja.com/guide/business-reviews/airbnb-configuration#for-room-reviews-required)

*   In the **Filter** box at the top of the Network tab, type StaysPdpReviewsQuery and press Enter.
    
*   Refresh your Airbnb listing page. You should see a file with the name StaysPdpReviewsQuery appear in the network requests list.
    
*   Click on the StaysPdpReviewsQuery file name to open its details.
    

**Copy the Required Keys**

You will need to find and copy three pieces of information from this file:

*   **The API Key:**
    *   In the details panel, click on the **Headers** tab.
    *   Scroll down until you find the **x-airbnb-api-key**.
    *   Copy the long string of characters next to it. This is your API Key.

![airbnb api 1](https://docs.wpsocialninja.com/assets/reviewsquery-1.68K8WfWg.webp)

**The Secret Key:**

*   Now, click on the **Payload** tab (it might also be called "Request").
*   Navigate through extensions → persistedQuery.
*   You will see a **sha256Hash**. Copy the long string of characters next to it. This is your Secret Key.

![airbnb api 2](https://docs.wpsocialninja.com/assets/reviewsquery-2.C1I82bDM.webp)

### Find the Keys for a Room's Business Info (Required) [​](https://docs.wpsocialninja.com/guide/business-reviews/airbnb-configuration#find-the-keys-for-a-room-s-business-info-required)

*   In the **Filter** box at the top of the Network tab, type **StaysPdpSections** and press Enter.
    
*   Refresh your Airbnb listing page. You should see a file with the name **StaysPdpSections** appear in the network requests list.
    
*   Click on the StaysPdpSections file name to open its details.
    

![api 1](https://docs.wpsocialninja.com/assets/sections-1.CzPqdIid.webp)

*   **The Secret Key:**

*   Now, click on the Payload tab (it might also be called "Request").
    *   Navigate through extensions → persistedQuery.
        
    *   You will see a sha256Hash. Copy the long string of characters next to it. This is your Secret Key.
        

![api 2](https://docs.wpsocialninja.com/assets/sections-2.CEXeE4ZT.webp)

### **Step 2: Add the Keys to Your WordPress Site** [​](https://docs.wpsocialninja.com/guide/business-reviews/airbnb-configuration#step-2-add-the-keys-to-your-wordpress-site)

To make these keys work, you need to add a small code snippet to your WordPress site. The safest and easiest way to do this is by using a **Code Snippets** plugin. We recommend [FluentSnippets](https://fluentsnippets.com/).

#### **Create a New Snippet** [​](https://docs.wpsocialninja.com/guide/business-reviews/airbnb-configuration#create-a-new-snippet)

Go to **FleuntSnippets → Add NewSnippet**.

*   Give your snippet a title, like "Airbnb API Keys for WP Social Ninja".
    
*   **Paste the Code**
    

Copy the code block below and paste it into the "Code" area of your new snippet.

**Add Your Keys**

*   Replace API Key you copied in Step 1.
    *   Replace with the Secret Key you copied in Step 1.

php

```
add_filter('wpsocialreviews/airbnb_api_key', function(){
    return 'paste_the_key_here';
});

// for rooms 
add_filter('wpsocialreviews/airbnb_rooms_api_secret_key', function(){
    return 'paste_the_key_here';
});

// for rooms business info 
add_filter('wpsocialreviews/airbnb_rooms_business_info_api_secret_key', function(){
    return 'paste_the_key_here';
}); 

// for experiences or services 
add_filter('wpsocialreviews/airbnb_experiences_api_secret_key', function(){
    return 'paste_the_key_here';
});
```

**Important: First Three Keys Are Required**

To ensure a complete and successful connection for your Airbnb, you **must** provide first three of the following keys in your code snippet. The integration will not work correctly without them.

*   **The Main API Key:** This is the master key for the connection.
    
*   **The Room Reviews Key:** This key specifically fetches the customer reviews.
    
*   **The Room Business Info Key:** This key fetches essential listing details.
    

Click the **Save Snippets and Activate** button at the top of the page.

## **Airbnb Configuration** [​](https://docs.wpsocialninja.com/guide/business-reviews/airbnb-configuration#airbnb-configuration)

To add **Airbnb Reviews** on your site, it is obvious that you need somehow to connect with the Airbnb server to fetch the reviews from their repositories; however, it is not a difficult task for the non-techies as we have created the easiest way to aggregate reviews.

To add Airbnb Reviews to your site, first, click on Airbnb.

![airbnb platform 1](https://docs.wpsocialninja.com/assets/airbnb-config-1.BoKXXGjt.webp)

Now paste your room, experience or business URL here.

![airbnb platform 2](https://docs.wpsocialninja.com/assets/airbnb-config-2.BXVcBBlc.webp)

You can find the URL in the address bar of your Airbnb room, experience, or business page, just like in the screenshot below.

![airbnb platform 3](https://docs.wpsocialninja.com/assets/room-url.kMU0CPvm.webp)

Paste the URL into the field and hit **Save**. Once connected, you’ll see your Airbnb account linked with Social Ninja. Next, click **Create a Template** to start displaying your Airbnb reviews.

![airbnb platform 4](https://docs.wpsocialninja.com/assets/airbnb-config-3.Ze5NFWWt.webp)

Your template is now ready! From here, you can customize it the way you like. For more details, check out this [documentation](https://docs.wpsocialninja.com/guide/business-reviews/template-style-connection) on template customization.

INFO

You can fetch up to **100 reviews** for each business on your site. If you're using the **free version of WP Social Ninja**, you can fetch a maximum of **5 Airbnb reviews**.

However, downloading reviews sometimes might take some time. If you want, you can delete this account by clicking on the **Cross** icon.

You can even include additional business accounts when clicking the **Add More Business** button. Just enter the business name the same way as before & click the **Save** button.
