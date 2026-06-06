---
source_url: "https://docs.wpsocialninja.com/guide/social-feeds/tiktok-feed-template.html"
title: "TikTok Feed Template | WP Social Ninja"
---

# TikTok Feed Template | WP Social Ninja

This is your creative control center, where you can design a beautiful and functional TikTok feed that perfectly matches your website.

When you first open the editor, you'll see three main tabs at the top of the settings panel on the right:

*   **General (This Guide):** This is the most important tab. It controls _what_ content is shown (your videos, your profile info, filters) and _how_ the feed functions (the layout, buttons, and links).
*   **Style:** This tab controls the "look and feel"—all the colors, fonts, and borders.
*   **Connection:** This tab is for managing the specific API connection for this template.

This guide will walk you through every single setting in the **General** tab in a simple, step-by-step way.

**What can you build with these settings?**

*   **A "Latest Videos" Slider:** Use the **Carousel** layout and set the **Post Order** to "Newest" to show your newest videos on your homepage.
*   **A Clean "Portfolio" Gallery:** Use the **Grid** layout, turn on **Equal Height**, and hide the **Description**, **Views**, and **Likes** to create a clean, professional-looking gallery of your work.

![Template Template](https://docs.wpsocialninja.com/assets/tiktok-template.BOWcbC93.webp)

## General Settings [​](https://docs.wpsocialninja.com/guide/social-feeds/tiktok-feed-template#general-settings)

Here is a detailed breakdown of each section within the **General** tab.

### 1\. Source [​](https://docs.wpsocialninja.com/guide/social-feeds/tiktok-feed-template#_1-source)

This is the very first and most important step. The Source settings tell WP Social Ninja where to get the TikTok videos from.

*   **Feed Type:** This dropdown menu lets you choose the kind of feed you want to create.
    *   **User Account Feed:** This is the most common choice. It will display the most recent videos from your own TikTok profile.
*   **Select Account(s):** If you've connected more than one TikTok account to WP Social Ninja, this dropdown is where you'll pick the one you want to use for this template.
*   **Fetch Feeds:** This is your manual "Refresh" button. If you've just posted a new video on TikTok and want to see it in your website preview right now, just click this button. It forces the plugin to check for new content immediately.

![Template Template](https://docs.wpsocialninja.com/assets/tiktok-template-2.BMMERawN.webp)

### 2\. Template [​](https://docs.wpsocialninja.com/guide/social-feeds/tiktok-feed-template#_2-template)

This section controls the visual structure and arrangement of your videos.

*   **Layout Type:** This is the foundational structure of your feed.
    *   **Grid:** This creates a clean, organized, multi-column grid. All video thumbnails are forced to be the same height, which creates a very neat and symmetrical look.
    *   **Carousel:** This displays your videos in a horizontal slider. Visitors can click or swipe through your posts. This is perfect for saving space on a homepage.
    *   **Masonry:** This is a "Pinterest-style" multi-column grid. Videos will have different heights (especially if you show the text caption), and the plugin will intelligently fit them together like bricks in a wall.
*   **Template:** These are pre-designed visual "skins" for your feed. Each template changes the styling of the video boxes, fonts, and layout. Click through them to see which one best matches your brand.
*   **Number of Columns:** This is a crucial setting for making your feed look good on all devices. You can set the number of columns you want to show on **Desktops**, **Tablets**, and **Mobile** phones.
    *   _Example: You might choose 4 columns for Desktop, 2 for Tablet, and 1 for Mobile. This ensures your feed is always easy to see and interact with, no matter the screen size._
*   **Columns Gap:** This controls the amount of empty space (in pixels) between each video in your feed. Increase this number to give your videos more "breathing room," or set it to `0` to have them all touch.

![Template Template](https://docs.wpsocialninja.com/assets/tiktok-template-3.C5kIO4fs.webp)

### 3\. Filters [​](https://docs.wpsocialninja.com/guide/social-feeds/tiktok-feed-template#_3-filters)

Filters are how you refine your feed to exclude content you don't want or only show content you do.

*   **Number of Feeds to Display:** This is the number of videos a visitor will see when the page first loads. (More videos can be loaded later using the **Pagination** settings, which we'll cover below).
*   **Post Order:** This lets you sort your videos.
    *   **Newest:** Shows newest videos first (this is the most common setting).
    *   **Oldest:** Shows oldest videos first.
    *   **Most Viewed:** Shows most viewed video.
    *   **Most Likes:** Shows most liked video.
    *   **Random:** Shuffles the videos in a new order every time the page loads.
*   **Show/Hide Posts with Keywords/Hashtags:** This is a very powerful filter. You can enter a comma-separated list of words or hashtags to either **only show** videos with those words, or **hide** videos with those words.
    *   _Example: If you want to hide all videos that mention a certain competitor, you could add their name to the "Hide" box._
*   **Hide Specific Feeds:** This allows you to manually hide one or more specific videos. To get a video's ID, open that video on TikTok, and copy the long string of numbers in the URL.

![Template Template](https://docs.wpsocialninja.com/assets/tiktok-template-4.DgvIFtSD.webp)

### 4\. Feed [​](https://docs.wpsocialninja.com/guide/social-feeds/tiktok-feed-template#_4-feed)

This section controls the content and links inside each individual video card.

*   **Open Post in:** This determines what happens when a visitor clicks on a video.
    *   **None:** The video is not clickable. This is for a "display-only" gallery.
    *   **TikTok:** The visitor will be taken to the original video on TikTok.com in a new browser tab.
    *   **Popup:** This is the best user experience. The video will open in a beautiful pop-up box on your own website, where it will play. This keeps visitors on your site longer.
*   **Display Toggles (On/Off Switches):**
    *   **Display Author Photo:** Shows your small, circular profile picture on each video.
    *   **Display Author Name:** Shows your TikTok username (e.g., @wpsocialninja) on each video.
    *   **Display Description:** Shows the text caption you wrote for that video.
    *   **Display Platform Icon:** Shows a small TikTok icon on each video.
    *   **Display Date:** Show the date with each video.
*   **Trim Description Words:** This sets a maximum word count for your video captions. If a caption is longer than this number, it will be cut off with a "Read More..." link. This is the key to keeping your feed looking clean and uniform.
*   **Equal Height:** This toggle is very important for the **Grid** layout. When toggled **on**, all video boxes are forced to the same height (based on the tallest one), creating a perfect, uniform grid. You should turn this **Off** if you are using the **Masonry** layout.
*   **Display Media:** This is the main switch for showing the actual video thumbnails. You will almost always want to keep this on. If you turn it off, your feed will only show text.

#### Views & Likes [​](https://docs.wpsocialninja.com/guide/social-feeds/tiktok-feed-template#views-likes)

This section lets you show or hide the social proof associated with each individual video.

*   **Display Views Count:** A simple On/Off toggle to show or hide how many views each video has.
*   **Display Likes Count:** A simple On/Off toggle to show or hide how many likes each video has.
    *   _Use Case: For a business, showing high view and like counts is great social proof. For a cleaner, more professional portfolio, you might turn these off._
*   **Display Comment Count:** A simple On/Off toggle to show the comment count in the template feed.

![Template Template](https://docs.wpsocialninja.com/assets/tiktok-template-5.U2EL_AWk.webp)

### 5\. Header [​](https://docs.wpsocialninja.com/guide/social-feeds/tiktok-feed-template#_5-header)

This section controls the large banner at the top of your entire feed, which displays your main TikTok profile information.

*   **Display Header:** This is the master On/Off switch for the entire header section. Turn it off if you just want to show the videos.
*   **Account to Display:** If your feed is showing videos from multiple accounts, this lets you choose which one account's info to show in the header.
*   **Display Toggles (On/Off Switches):** These let you build a "mini-profile" on your website.
    *   **Display Profile Photo** (Your main profile picture)
    *   **Display Account Name** (Your @username)
    *   **Display Description** (Your TikTok profile description)
    *   **Display Website** (The link in your profile)
    *   **Display Followers Count** (How many followers you have)
    *   **Display Following Count** (How many people you are following)
    *   **Display Likes Count:** This is a key TikTok metric. It shows the TOTAL number of likes your entire profile has ever received.

![Template Template](https://docs.wpsocialninja.com/assets/tiktok-template-6.DpKJ8hbs.webp)

### 6\. Follow Button [​](https://docs.wpsocialninja.com/guide/social-feeds/tiktok-feed-template#_6-follow-button)

This adds a "Follow" call-to-action button to your feed, helping you get more TikTok followers directly from your website visitors.

*   **Display FollowButton:** Toggles the button on or off.
*   **Follow Button Position:** You can place the button in the **Header** (at the top of the feed) or the **Footer** (at the bottom, after all the videos).
*   **Button Text:** You can customize the text on the button (e.g., "Follow Us on TikTok" or "See More on TikTok").

![Template Template](https://docs.wpsocialninja.com/assets/tiktok-template-7.BVuDpY0O.webp)

### 7\. Pagination [​](https://docs.wpsocialninja.com/guide/social-feeds/tiktok-feed-template#_7-pagination)

This is the new section you asked about. Pagination controls what happens when a visitor gets to the bottom of the initial set of videos.

*   **Pagination Type:** This lets you choose how users load more videos.
    *   **None:** The feed will only show the "Number of Feeds to Display" (from the **Filters** section) and that's it. There will be no way to load more videos.
    *   **Load More:** This will add a button at the bottom of your feed. When clicked, it will load the next set of videos. This is the most popular and user-friendly option.

![Template Template](https://docs.wpsocialninja.com/assets/tiktok-template-8.CkzpOzCa.webp)

## Next Steps [​](https://docs.wpsocialninja.com/guide/social-feeds/tiktok-feed-template#next-steps)

Now that you have configured all the General settings, your next step is to make your feed beautiful!

Click on the **Style** tab to customize all the colors, fonts, and borders.

When you are finished, click the **Save Template** button at the bottom.
