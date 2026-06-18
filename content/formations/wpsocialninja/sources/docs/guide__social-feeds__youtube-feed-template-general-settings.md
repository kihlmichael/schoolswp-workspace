---
source_url: "https://docs.wpsocialninja.com/guide/social-feeds/youtube-feed-template-general-settings.html"
title: "YouTube Feed Template: General Settings"
---

# YouTube Feed Template: General Settings

When you create or edit a new YouTube feed template, you will land in the main Template Editor. This is where you control everything about your feed's content and appearance.

The editor is divided into three tabs:

*   **General (This Guide):** This tab controls the feed's content. You set the video source, filter the videos, and adjust functional settings like layout, video player behavior, and buttons.
*   **Style:** This tab controls the visual design. You can change colors, fonts, and spacing to match your brand.
*   **Connection:** This tab manages the API connection for this template. You can use this to re-authenticate your account or connect a new source if needed.

This guide will walk through every option in the **General** tab. So, let’s get started.

![Youtube Template General Settings](https://docs.wpsocialninja.com/assets/youtube-template.CsourJLK.webp)

> **Use Case:** You can use these settings to create powerful, specific feeds.
> 
> *   A vlogger can show their **Channel** feed, use the **Template** settings to create a **Masonry** grid, and use the **Filters** to show only their 5 most recent videos.
> *   A musician can create a feed showing only a specific **Playlist** of their new album.
> *   A brand can use the **Search** type to create a feed of all videos that mention their product's name.

## General Settings [​](https://docs.wpsocialninja.com/guide/social-feeds/youtube-feed-template-general-settings#general-settings)

Here is a breakdown of each section within the **General** tab.

### 1\. Source [​](https://docs.wpsocialninja.com/guide/social-feeds/youtube-feed-template-general-settings#_1-source)

This section is the most important setting in your template. It controls what content to fetch from YouTube by defining the video source and the total number of videos to retrieve.

*   **Feed Type:** This dropdown lets you choose the kind of content to display.
    *   **Channel:** Shows the latest videos from a specific YouTube account.
    *   **Playlist:** Shows all videos from a single, specific playlist.
    *   **Search:** Shows videos that match a specific keyword.
    *   **Specific Videos:** Lets you hand-pick one or more videos by ID.
    *   **Live Streams:** Shows upcoming, live, or completed live streams from a channel.
*   **Channel ID, Handle or Username:** (Appears if "Channel" is selected). You must enter the channel's Handle, ID, or Username.
    *   **Example (Handle):** `https://www.youtube.com/@yourchannel`
    *   **Example (ID):** `https://www.youtube.com/channel/UC...`
    *   **Example (Username):** `https://www.youtube.com/user/yourname`
*   **Total Feed:** Set the maximum number of videos to fetch from YouTube. The maximum is 200. (Note: This is different from the number of videos shown on first load, which is controlled by Pagination).

![Source settings for the YouTube feed](https://docs.wpsocialninja.com/assets/source.B5emRD_7.webp)

### 2\. Template [​](https://docs.wpsocialninja.com/guide/social-feeds/youtube-feed-template-general-settings#_2-template)

This section controls the foundational layout and visual structure of your YouTube feed. It allows you to set the layout type, choose a pre-designed skin, and define the responsive column structure.

*   **Layout Type:** This dropdown lets you choose the main structure for your feed. As shown in the image, the options are:
    
    *   **Grid:** A clean, multi-column grid where all video boxes are the same height.
    *   **Carousel:** A horizontal slider.
*   **Template:** These are pre-designed visual "skins" (e.g., Vega, Sirius, Polaris, Rigel).
    
*   **Number of Columns:** Set the number of columns for Desktop, Tablet, and Mobile.
    
*   **Columns Gap:** This controls the space (in pixels) between each video.
    

![Template layout settings for the YouTube feed](https://docs.wpsocialninja.com/assets/template.Bux6OaBU.webp)

#### Carousel Settings [​](https://docs.wpsocialninja.com/guide/social-feeds/youtube-feed-template-general-settings#carousel-settings)

When you set your Layout Type to **Carousel** in the **Template** section, this new panel appears. It allows you to customize the behavior and controls of the carousel slider.

![carousel Template](https://docs.wpsocialninja.com/assets/select-carousel.DZWoaxNL.webp)

*   **Autoplay:** This toggle enables or disables the automatic sliding of the carousel. Turn it **ON** if you want the carousel to slide automatically.
    
*   **Autoplay Speed:** This field sets the time (in milliseconds) between each automatic slide. For example, 3000 equals 3 seconds.
    
*   **Items To Show:** Use the slider to set how many video items are visible at one time in the carousel viewport (e.g., 3).
    
*   **Items To Scroll:** Use the slider to set how many items the carousel should slide at one time (e.g., 1)
    
*   **Navigation Type:** Displays clickable left/right arrows.
    
    *   **Dots:** Displays clickable dots at the bottom.
    *   **Arrows and Dots:** Displays both.
    *   **None:** Hides all navigation controls.
*   **Space Between:** This slider controls the amount of empty space (in px) between each video slide in the carousel.
    

![carousel Template Settings](https://docs.wpsocialninja.com/assets/carousel-settings.C1RBInA4.webp)

### 3\. Filters [​](https://docs.wpsocialninja.com/guide/social-feeds/youtube-feed-template-general-settings#_3-filters)

The Filters section helps you control which videos appear in your YouTube feed and how they’re displayed. You can refine, sort, or exclude content to ensure your feed only shows the most relevant videos.

**Options Explained:**

*   **Number of Videos to Display:** Set how many videos are shown when the feed first loads. You can increase or decrease the count to adjust the layout.
*   **Posts Order:** Choose how your videos are sorted in the feed.
    *   **Newest (Descending):** Displays the latest videos first (default).
    *   **Oldest (Ascending):** Displays the oldest videos first.
    *   **Random:** Shuffles video order for a varied feed each time the page loads.
*   **Show Posts Containing These Words or Hashtags:** Enter specific keywords or hashtags to only show videos that include them in their title or description. This is useful for focusing on a topic, campaign, or product-related videos.
*   **Hide Posts Containing These Words or Hashtags:** Add keywords or hashtags to exclude videos that contain those terms. Perfect for filtering out unrelated or off-topic content.
*   **Hide Specific Videos:** Enter the YouTube video IDs of any videos you don’t want displayed in your feed. This gives you precise control over what appears publicly.
*   **Cache Settings (Optional):** Set how often the plugin refreshes data from YouTube. You can choose time intervals like 6 hours, 12 hours, or 1 day to balance performance and freshness.

![Filter settings](https://docs.wpsocialninja.com/assets/filter.dgYVivXP.webp)

### 4\. Video [​](https://docs.wpsocialninja.com/guide/social-feeds/youtube-feed-template-general-settings#_4-video)

This section controls how individual video posts appear in your YouTube feed. It allows you to customize which video elements are shown and how the videos play when clicked.

**Options Explained:**

*   **Play Mode:** Determines how videos are played when a visitor clicks on them.
    *   **Popup:** Opens the video in a pop-up lightbox on your website (default and recommended for the best user experience).
    *   **In-line:** Plays the video directly inside the feed layout.
    *   **YouTube Player:** Redirects the visitor to watch the video on YouTube.
    *   _(Gallery mode available in Pro version)_
*   **Display Title:** Toggles the visibility of each video’s title.
*   **Trim Title Words:** Allows you to limit how many words appear in the video title (helpful for keeping your layout neat).
*   **Display Play Icon:** Enables or disables the play button overlay on the video thumbnail.
*   **Display Duration:** Shows or hides the video’s total length.
*   **Display Date:** Displays the date when the video was published.
*   **Display Views Counter:** Shows the total number of views for each video.
*   **Display Likes Counter:** Displays the total number of likes _(available in Pro version)_.
*   **Display Comments Counter:** Displays the number of comments on the video _(available in Pro version)_.
*   **Display Description:** Shows a short text description for each video, if available.
*   **Display Channel Name:** Toggles the visibility of the YouTube channel name under each video.
*   **Display Call To Action Button:** Adds a “Watch Now” button below the video, encouraging viewers to engage.

![Video content display settings](https://docs.wpsocialninja.com/assets/video.CqayQGgs.webp)

### 5\. Header [​](https://docs.wpsocialninja.com/guide/social-feeds/youtube-feed-template-general-settings#_5-header)

This section controls the main banner area that appears at the top of your entire YouTube feed. It allows you to customize how the channel header looks and what information is displayed.

*   **Show Header:** This is the main toggle that enables or disables the entire header section. Turn it off to hide the banner, logo, and all channel info.
*   **Display Banner:** Toggles the large channel banner image at the top of the header. You can also upload a custom banner image if desired.
*   **Display Logo:** Enables or disables the channel’s profile image (logo) within the header section.
*   **Display Name:** Shows or hides the YouTube channel’s name under the logo.
*   **Display Subscriber Counter:** Displays the total number of subscribers for the connected YouTube channel.
*   **Display Videos Counter:** Displays the total count of videos available on the channel.
*   **Display Views Counter:** Displays the total number of views across the entire channel.
*   **Display Description:** Enables the short description or channel bio text (if available).
*   **Display Subscribe Button:** Shows or hides a “Subscribe” button within the header, allowing users to subscribe directly from the feed.
*   **Upload Custom Banner:** Allows you to manually upload your own banner image to replace the default YouTube channel banner.

![Header settings for the YouTube feed](https://docs.wpsocialninja.com/assets/header.Bacvvcsv.webp)

### 6\. Subscribe Button [​](https://docs.wpsocialninja.com/guide/social-feeds/youtube-feed-template-general-settings#_6-subscribe-button)

This adds a "Follow" button at the top or bottom of your feed.

*   **Display Subscribe button:** click to the toogle button to show the subscribe button.
*   **Subscribe Button Position:** Choose where the button appears from the dropdown options: **Header** **Footer** or **Both**.
*   **Button Text:** Customize the text on the button (e.g., "Follow Us on YouTube").

![Subscribe Button settings for the YouTube feed](https://docs.wpsocialninja.com/assets/subscribe-button.CWu8AAFh.webp)

### 7\. Pagination [​](https://docs.wpsocialninja.com/guide/social-feeds/youtube-feed-template-general-settings#_7-pagination)

Pagination controls what happens when a visitor reaches the end of the first set of videos.

*   **Pagination Type:**
    *   **None:** The feed will only show the "Number of Feeds to Display." No more videos can be loaded.
    *   **Load More:** This adds a button at the bottom of your feed.
    *   **Prev Next:** This button allows the user to move forward or backward to the immediately following page in the sequence.

> **Example:**
> 
> *   You set **Number of Feeds to Display** (in Filters) to **8**.
> *   You set **Videos Per Page** (in Pagination) to **4**.
> *   When your page loads, visitors will see 8 videos.
> *   When they click "Load More," 4 new videos will appear (for a total of 12).

![Pagination settings for the YouTube feed](https://docs.wpsocialninja.com/assets/pagination.CSAlwzUI.webp)

## Next Steps [​](https://docs.wpsocialninja.com/guide/social-feeds/youtube-feed-template-general-settings#next-steps)

Now that you have configured all the General settings, your next step is to make your feed look great.

Click on the **Style** tab to customize the Colors, Fonts, and Spacing of your header, video posts, and buttons. Learn more about [YouTube configuration](https://docs.wpsocialninja.com/guide/social-feeds/youtube-configuration).

When you are finished, click the **Save** button.
