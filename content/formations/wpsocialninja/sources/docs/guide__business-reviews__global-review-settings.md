---
source_url: "https://docs.wpsocialninja.com/guide/business-reviews/global-review-settings.html"
title: "Global Review Settings | WP Social Ninja"
---

# Global Review Settings | WP Social Ninja

The **Global Review Settings** panel allows you to manage the core performance and moderation rules for all your social reviews at once. These settings ensure that your website stays fast and that you have full control over how new feedback is displayed to your visitors.

## Accessing Global Review Settings [​](https://docs.wpsocialninja.com/guide/business-reviews/global-review-settings#accessing-global-review-settings)

To find these configuration options, navigate to your WordPress dashboard and go to **WP Social Ninja → Settings**. From the left sidebar, click on **Reviews Platforms** and then select **Global Review Settings**.

## Reviews Image Optimization [​](https://docs.wpsocialninja.com/guide/business-reviews/global-review-settings#reviews-image-optimization)

This section is dedicated to improving your website's performance by managing how review images are handled.

*   **Optimize Images**: Enabling this toggle allows the plugin to generate and store optimized versions of review images in multiple sizes using your local WordPress storage. This significantly improves loading speeds for your review templates.
    
*   **Reset Local Images**: Clicking the **Reset Image Storage** button will clear all locally stored images for the Reviews platform. Use this if your images are not appearing correctly or if you wish to refresh your local storage.
    

![Access Global Review Settings](https://docs.wpsocialninja.com/assets/access-global-review-settings.BTkAC0k-.webp)

## Review Publishing Settings [​](https://docs.wpsocialninja.com/guide/business-reviews/global-review-settings#review-publishing-settings)

Control how and when new reviews go live on your website with the **Review Publishing Mode**. There are three distinct modes available:

*   **Publish Automatically**: New reviews are fetched and displayed immediately without any manual intervention.
    
*   **Require Approval**: All incoming reviews are sent to the moderation panel first, where you must manually approve them before they appear on your site.
    
*   **Auto Publish with Filters**: This advanced mode allows you to set specific Conditional Publishing Rules to automate your moderation process.
    

NOTE

The Auto Publish with Filters feature is available in the Pro version.

### Conditional Publishing Rules [​](https://docs.wpsocialninja.com/guide/business-reviews/global-review-settings#conditional-publishing-rules)

When using the filtered publishing mode, you can define the following criteria:

*   **Minimum Rating Required**: Automatically publish reviews only if they meet a specific star rating (e.g., at least 3 stars).
    
*   **Blocked/Spam Words**: Enter specific keywords (separated by commas) that will trigger spam detection. Any review containing these words will be sent to moderation automatically.
    
*   **Minimum Review Length**: Set a character limit. Shorter, low-effort reviews will be held for moderation rather than being published instantly.
    

![Review Publishing Settings](https://docs.wpsocialninja.com/assets/review-publishing-settings-2.BNkqUznf.webp)

## AI Review Summarizer API Settings [​](https://docs.wpsocialninja.com/guide/business-reviews/global-review-settings#ai-review-summarizer-api-settings)

WP Social Ninja integrates with AI platforms to provide summarized versions of your reviews.

*   **Enable AI Review Summarizer**: Toggle this option to activate AI-powered review summaries.
    
*   **AI Platform & Model**: Select your preferred AI provider (e.g., OpenAI) and the specific model (e.g., gpt-4o) you wish to use.
    
*   **API Key**: Enter the unique API key provided by your selected AI platform to securely connect the service.
    

After setting up all the configurations to your preference, click on the **"Save Settings"** button located at the top right corner to apply the changes.

![AI Review Settings](https://docs.wpsocialninja.com/assets/ai-review-settings-3.BEpvu-wl.webp)
