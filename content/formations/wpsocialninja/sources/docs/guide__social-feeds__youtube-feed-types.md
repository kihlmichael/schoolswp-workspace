---
source_url: "https://docs.wpsocialninja.com/guide/social-feeds/youtube-feed-types.html"
title: "YouTube Feed Type | WP Social Ninja"
---

# YouTube Feed Type | WP Social Ninja

When you create a YouTube feed template, the most important setting is the **Feed Type**. This option controls what kind of content your feed will display. After you select YouTube as your platform in the template editor, you will see a Feed Type dropdown.

## **Feed Type** [​](https://docs.wpsocialninja.com/guide/social-feeds/youtube-feed-types#feed-type)

Currently, we have five Feed Types; **Channel**, **Playlist**, **Search**, **Specific Videos**, and **Live Streams**. You can select any Feed Type; for example, if you select **Channel**, then you need a **Channel ID** to fetch the YouTube Channel Feed on your website. Similarly, if you pick **Playlist,** then you need a **Playlist ID**.

## 1.Channel [​](https://docs.wpsocialninja.com/guide/social-feeds/youtube-feed-types#_1-channel)

This feed type displays the latest videos from a specific YouTube account.

### **How to Find Your Channel ID, Handle, or Username** [​](https://docs.wpsocialninja.com/guide/social-feeds/youtube-feed-types#how-to-find-your-channel-id-handle-or-username)

In your web browser, go to [YouTube.com](https://www.youtube.com/). Search for the channel you want to display and click on its name to go to its main page. Look at the URL in your browser's address bar. **Copy** the correct part of the URL based on its format:

### Channel Handle [​](https://docs.wpsocialninja.com/guide/social-feeds/youtube-feed-types#channel-handle)

To find a Channel Handle:

*   **URL:** [https://www.youtube.com/@yourchannel](https://www.youtube.com/@yourchannel)
*   **Copy and paste:** @yourchannel

![Channel Handle](https://docs.wpsocialninja.com/assets/channel-handle.BoCbmHqL.webp)

After copying the channel handle, go to your **YouTube Template Source** options and paste the **Channel Handle** that you copied before. Then, click the **Save** button.

![Paste Channel Handle](https://docs.wpsocialninja.com/assets/paste-channel-handle.rZYjWzaR.webp)

### Channel ID [​](https://docs.wpsocialninja.com/guide/social-feeds/youtube-feed-types#channel-id)

To find a Channel ID:

*   **URL:** [https://www.youtube.com/channel/UCibcXdeKy8e04hYWf0Gz7ow](https://www.youtube.com/channel/UCibcXdeKy8e04hYWf0Gz7ow)
*   **Copy and paste:** UCibcXdeKy8e04hYWf0Gz7ow

Go to any YouTube channel page. Look at the **URL** in your browser. The **ID** is the long string of letters and numbers after youtube.com/channel/.

Example: [https://www.youtube.com/channel/UCiyeXfnGx9e06hXWf0Hz7ow](https://www.youtube.com/channel/UCiyeXfnGx9e06hXWf0Hz7ow). **Copy** this ID.

![Channel ID](https://docs.wpsocialninja.com/assets/channel-id.WegyCi7u.webp)

Now, **paste** it to insert the **Channel URL** and click on the Fetch Videos to fetch the Channel Videos. Then, click the **Save** button. Note that you are to select the URL after the channel, and the ID will look like “**UCiyeXfnGx9e06hXWf0Hz7ow”**.

![Youtube Channel ID](https://docs.wpsocialninja.com/assets/paste-channel-id.DIDHtt8y.webp)

### **Channel Username** [​](https://docs.wpsocialninja.com/guide/social-feeds/youtube-feed-types#channel-username)

To find a Username (for older channels):

*   **URL:** [https://www.youtube.com/user/your\_user\_name](https://www.youtube.com/user/your_user_name)
*   **Copy and paste:** your\_user\_name

### 2\. Playlist [​](https://docs.wpsocialninja.com/guide/social-feeds/youtube-feed-types#_2-playlist)

This feed type displays all videos from a single YouTube playlist.

*   **Feed Type:** Select Playlist.
*   **Playlist ID:** You must paste in the ID of the playlist.
*   **Total Feeds:** Set the number of videos you want to retrieve (e.g., "10").

Similar to Channel, to fetch the Playlist, you need the Playlist ID. You can do it in the following two steps:

#### Step 1 [​](https://docs.wpsocialninja.com/guide/social-feeds/youtube-feed-types#step-1)

To add **Playlist ID** from your Channel, click on your Channel and then click on the **YouTube Studio**.

![Youtube Studio](https://docs.wpsocialninja.com/assets/yotube-studio.KAKRh-vU.webp)

This will take you to the **Channel Dashboard**. From the left side, click on the **Playlists** to collect the **URL**.

![Copy URL](https://docs.wpsocialninja.com/assets/yotube-studio.KAKRh-vU.webp)

This will take you straight to the **WPManageNinja Channel Playlists**. Next, click the Playlist that you want to display on your website.

![Playlist URL](https://docs.wpsocialninja.com/assets/youtube-playlist-url.BW40Pb0g.webp)

Now copy the selected **URL** and insert it on the **Playlist ID**. Next, click on the **Fetch Videos** button.

Make sure you select the URL after the list= and the ID will look like “PLXpD0vT4thWEu4gAkLE0Eq7PRCFp\_8j2z”. After you have completed it, don’t forget to click on the **Save** button.

![Paste the Playlist ID](https://docs.wpsocialninja.com/assets/paste-playlist-id.hnQ9omgy.webp)

#### Step 2 [​](https://docs.wpsocialninja.com/guide/social-feeds/youtube-feed-types#step-2)

Go to the YouTube channel and click on the **Playlists** to obtain the **Playlist ID**.

![Playlist ID](https://docs.wpsocialninja.com/assets/playlist.Dv726z7-.webp)

This will take you straight to the **WPManageNinja Channel Playlists**. Next, click the **Playlist** that you want to display on your website.

In the screenshot, you can see the **URL**. Now copy the selected URL and insert it on the **Playlist ID**. Make sure you click on the **Fetch Videos**.

![Playlist URL](https://docs.wpsocialninja.com/assets/playlist-url1.BQD85zEa.webp)

Remember, select the URL after the list= and the ID will look like “**PLXpD0vT4thWF0mLcvKKSbt281wt1bMcfP**”. After that, click to the **Save** button. ![Playlist URL](https://docs.wpsocialninja.com/assets/save-playlist.Caxw_GKr.webp)

### 3\. Search Term [​](https://docs.wpsocialninja.com/guide/social-feeds/youtube-feed-types#_3-search-term)

This feed type displays videos that match a specific search keyword.

*   **Feed Type:** Select Search.
*   **Search Term:** Enter the keyword you want to search for (e.g., "WordPress Plugins"). The feed will show the top results for this term.

Once you select the **Search Feed, Search Term** will automatically appear. In this field, you need to fill up with the search term in order to fetch the videos to your YouTube feed.

For example, if you put **NinjaTables** on the Search Term and click on the **Fetch Videos**. The search result will display all the Ninjatables related videos. After that, click to the **Save** button.

![Search Term](https://docs.wpsocialninja.com/assets/search-term.DA0iFyJ_.webp)

### 4\. Specific Videos [​](https://docs.wpsocialninja.com/guide/social-feeds/youtube-feed-types#_4-specific-videos)

This feed type lets you hand-pick one or more specific videos to display.

*   **Feed Type:** Select Specific Videos.
*   **Video ID:** Paste in the ID of the video you want to show.

#### How to Find a Video ID [​](https://docs.wpsocialninja.com/guide/social-feeds/youtube-feed-types#how-to-find-a-video-id)

Now it’s time to select the **Feed Type: Specific Videos**. Similar to Search Feed, once you select the **Specific Videos,** the **Video ID** menu will appear.

In this field, you can select a particular video to fetch on your YouTube feed. To obtain a **Video ID,** go to **YouTube** and select the **Video**.

However, you can also add multiple videos to your Feed. To do that, add more videos after a comma on the **Video ID** section. For example, **nn0q2FOPfUA, rE8j6zFjKac&t=156s.**

For demonstration purposes, we will go with a single **Video ID**.

![Obtain Video ID](https://docs.wpsocialninja.com/assets/obtain-video-id.T_mgFTSf.webp)

From the **Video URL,** copy the selected **URL** and paste it to insert it on the **video ID**. After you have pasted the Video ID, click on the **Fetch Videos** to display the videos on the YouTube Feed.

Keep in mind, only select the ID after the **v=** and the Video ID looks like “**nn0q2FOPfUA**”. Click to the **Save** button.

NOTE

To add multiple videos, paste in multiple Video IDs separated by a comma (e.g., nn0q2FOPfUA,rE8j6zFjKac).

![youtube video id](https://docs.wpsocialninja.com/assets/video-id1.BYNR1ZgA.webp)

### 5\. Live Streams [​](https://docs.wpsocialninja.com/guide/social-feeds/youtube-feed-types#_5-live-streams)

This feed type allows you to display upcoming, live, or completed live streams from a specific channel.

*   **Feed Type:** Select Live Streams.
*   **Channel ID:** **Paste** in the Channel ID of the channel (see the "Channel" section above for how to find this).
*   **Event Type:** Choose what you want to show:
    *   **Completed:** Show recently finished live streams.
    *   **Upcoming:** Show scheduled live streams.
    *   **Live:** Will only show a video if one is currently live.
    *   **None:** Will not filter by event type.

After you have configured your feed type, you can continue to the **Filters** and **Settings** tabs to customize the layout. Click the **Save** button when you are finished.

![youtube live streams](https://docs.wpsocialninja.com/assets/youtube-live-streams.BOFUM3Ge.webp)
