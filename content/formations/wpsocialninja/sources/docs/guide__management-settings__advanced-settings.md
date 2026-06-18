---
source_url: "https://docs.wpsocialninja.com/guide/management-settings/advanced-settings.html"
title: "Advanced Settings | WP Social Ninja"
---

# Advanced Settings | WP Social Ninja

This guide will walk you through all the options on the **Advanced Settings** page. This is the main control center for your entire WP Social Ninja plugin, allowing you to manage global performance (Image Format), privacy (GDPR), and how your data is stored.

You can find this page by navigating to:

**WP Social Ninja → Settings → Advanced Settings**

## Settings [​](https://docs.wpsocialninja.com/guide/management-settings/advanced-settings#settings)

Here is a detailed explanation of each feature on this page.

### 1\. Image Format for Optimized Images (Recommended) [​](https://docs.wpsocialninja.com/guide/management-settings/advanced-settings#_1-image-format-for-optimized-images-recommended)

This section controls how the plugin handles images from all your feeds and reviews to make your site load faster.

**Optimize Image Format Type**

*   **What it is:** This is a powerful performance feature. It lets you choose the file format that WP Social Ninja will use to save optimized copies of your images (like Instagram photos, Google review avatars, etc.).
*   **How it works:** When the plugin fetches an image, it will automatically convert it to the format you select here and save it on your own server. This process (especially with **WebP**) creates much smaller image files, which makes your entire website load significantly faster for your visitors.
*   **Our Recommendation:** We strongly recommend selecting the **WebP** format. This is a modern image format created by Google that provides the best balance of high image quality and incredibly small file sizes.

### 2\. GDPR Compliance [​](https://docs.wpsocialninja.com/guide/management-settings/advanced-settings#_2-gdpr-compliance)

This section provides a simple but powerful tool to help you comply with the GDPR (General Data Protection Regulation), a European privacy law.

**GDPR (Toggle)**

*   **What it is:** This is your main privacy switch.
*   **How it works:** When you turn this toggle **On**, the plugin will change its behavior to better protect your users' privacy. Instead of loading images directly from external platforms (like Facebook, Google, or Instagram), the plugin will first save copies of those images locally to your own website's server.
*   **Why this is important:** This means your visitors' browsers won't have to connect to those external sites just to see an image. This helps you comply with data protection rules by preventing the automatic sharing of a user's data (like their IP address) with those third-party platforms.

### 3\. Manage Data [​](https://docs.wpsocialninja.com/guide/management-settings/advanced-settings#_3-manage-data)

This section contains a powerful tool for managing your plugin's data.

**Delete all Platform Data? (Button)**

*   **What it is:** This is a "Master Reset" button for your entire WP Social Ninja plugin.
*   **Important Warning:** Please be extremely careful with this button. This action is permanent and **cannot be undone**.
*   **What it does:** When you press this button, it will permanently and completely erase all data the plugin has saved from all platforms (Facebook, Instagram, X (Twitter) etc.). This includes:
    *   All of your connected accounts (you will have to reconnect every single platform).
    *   All of your cached feeds (all saved posts, tweets, and videos).
    *   All of your cached reviews.
    *   All optimized images that are stored on your server.
*   **Use Case:** You should only use this button if you are experiencing a major, unfixable problem and have been instructed by support to "start fresh," or if you are permanently uninstalling the plugin and want to make sure all its data is removed from your database.

![Advance Settings in General Settings](https://docs.wpsocialninja.com/assets/advance-settings-1.CXZG-ATN.webp)
