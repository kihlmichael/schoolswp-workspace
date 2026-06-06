---
source_url: "https://docs.wpsocialninja.com/guide/troubleshooting-support/facebook-feeds-not-updating.html"
title: "Facebook Feeds Not Updating or Missing Posts"
---

# Facebook Feeds Not Updating or Missing Posts

If your Facebook feed in WPSocialNinja isn’t updating or some posts are missing, it could be due to one of the following reasons. Below, we’ll explain the causes and provide potential solutions to help you resolve the issue.

## 1\. Posts Are Shared from a Personal Profile or Non-Public Facebook Page [​](https://docs.wpsocialninja.com/guide/troubleshooting-support/facebook-feeds-not-updating#_1-posts-are-shared-from-a-personal-profile-or-non-public-facebook-page)

If your Facebook feed isn't showing the most recent posts or some posts are missing, it's likely because those posts were shared from a personal Facebook profile or a non-public Facebook page.

### Why Does This Happen? [​](https://docs.wpsocialninja.com/guide/troubleshooting-support/facebook-feeds-not-updating#why-does-this-happen)

WP Social Ninja can only display posts that the Facebook API provides. If a post is private, restricted, or removed, it won’t be retrievable through the API

Facebook only allows us to fetch posts that are publicly available through the Page API. If a post is missing, it's usually because of one of these reasons:

Privacy settings – The page owner shared it with a limited audience (e.g., certain countries, age groups, or followers only).

Targeted/boosted posts – Posts that are only promoted or targeted to a specific audience may not appear in the API.

### Solution [​](https://docs.wpsocialninja.com/guide/troubleshooting-support/facebook-feeds-not-updating#solution)

Re-post the content directly to your Facebook page: Instead of sharing posts from personal profiles or restricted pages, re-post the content as your own post on your Facebook page. This ensures the content originates from your page and will display in your WPSocialNinja feed.

Share posts from public sources: If you share posts from other public Facebook pages or sources, they will appear in your feed. Avoid sharing from personal profiles or restricted pages.

## 2\. Some Posts Are Being Filtered Out [​](https://docs.wpsocialninja.com/guide/troubleshooting-support/facebook-feeds-not-updating#_2-some-posts-are-being-filtered-out)

If certain posts are missing, it could be due to filtering settings in WPSocialNinja.

### Check the Following Settings [​](https://docs.wpsocialninja.com/guide/troubleshooting-support/facebook-feeds-not-updating#check-the-following-settings)

Go to WPSocialNinja and then select [Templates](https://docs.wpsocialninja.com/guide/getting-started/templates-overview) from the navbar. Now, find the [Facebook Feed Template](https://docs.wpsocialninja.com/guide/social-feeds/facebook-customization) where you're facing the issue. Click on the **Edit** button of that feed to open its settings options.

![image](https://docs.wpsocialninja.com/assets/facebook-feed-1.BgNi6jA0.webp)

Filters: Under the **General** section, you'll find the **Filter** option for your posts. Check the filter settings for Post Types under the **Display Posts With** dropdown menu.

Below this, you'll also see some additional settings, make sure to check if you've applied any filters that exclude posts with specific words or phrases.

![image](https://docs.wpsocialninja.com/assets/facebook-feed-2.Xy-T7c3o.webp)

## 3\. Missing Posts Have Audience Restrictions [​](https://docs.wpsocialninja.com/guide/troubleshooting-support/facebook-feeds-not-updating#_3-missing-posts-have-audience-restrictions)

Facebook allows you to set audience restrictions on posts, which can prevent them from being displayed outside of Facebook.

### Solution [​](https://docs.wpsocialninja.com/guide/troubleshooting-support/facebook-feeds-not-updating#solution-1)

Ensure that the missing posts are set to “**Public**”. When creating a post, check the audience setting and select the globe icon to make it publicly visible.

## 4\. Aggressive Caching Plugin Settings [​](https://docs.wpsocialninja.com/guide/troubleshooting-support/facebook-feeds-not-updating#_4-aggressive-caching-plugin-settings)

If you’re using a caching plugin on your WordPress site, it might be causing delays in updating your Facebook feed.

### Solution [​](https://docs.wpsocialninja.com/guide/troubleshooting-support/facebook-feeds-not-updating#solution-2)

Clear your cache: Go to your caching plugin settings and clear the cache.

Adjust caching settings: Ensure your caching plugin isn’t overly aggressive. You may need to exclude the WPSocialNinja feed from caching or adjust the Cache Timeout or TTL.

### Additional Tips [​](https://docs.wpsocialninja.com/guide/troubleshooting-support/facebook-feeds-not-updating#additional-tips)

Reconnect Your Facebook Account: Sometimes, reconnecting your [Facebook account](https://docs.wpsocialninja.com/guide/social-feeds/facebook-integration) in WPSocialNinja can resolve feed issues.

Check Facebook API Limits: Facebook imposes API limits on how often data can be fetched. If your feed isn't updating, wait a few minutes and check again.
