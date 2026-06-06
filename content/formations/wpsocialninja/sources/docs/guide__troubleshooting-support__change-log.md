---
source_url: "https://docs.wpsocialninja.com/guide/troubleshooting-support/change-log.html"
title: "Change Log | WP Social Ninja"
---

# Change Log | WP Social Ninja

Stay updated with the latest improvements, new features, bug fixes, and performance enhancements in WP Social Ninja.

## WP Social Ninja v4.2.2 [​](https://docs.wpsocialninja.com/guide/troubleshooting-support/change-log#wp-social-ninja-v4-2-2)

_Released on May 22, 2026_

🔧 Improvements🔒 Security🐛 Bug fixes

md

```
• Improved translation coverage for admin UI strings
• Improved validation to prevent editing the wrong templates, widgets, or notifications
```

md

```
• Added extra security checks for YouTube video popup and Facebook album requests (Pro)
```

md

```
• Fixed reviewer avatar and notification popup platform icon images to include explicit dimensions, reducing layout shift on review template pages
• Fixed “Write a Review” button allowing save with a blank custom URL — the editor now validates and blocks save when the custom URL is empty
• Fixed “Write a Review” button not rendering on the frontend when a custom URL source was configured (Pro)
• Fixed FluentCart reviews not showing the Edit action in the admin review list (Pro)
• Removed incomplete “View Submissions” action from the native review form actions menu (Pro)
```

## WP Social Ninja v4.2.1 [​](https://docs.wpsocialninja.com/guide/troubleshooting-support/change-log#wp-social-ninja-v4-2-1)

_Released on April 24, 2026_

✨ Newly Added🔧 Improvements🐛 Bug fixes

md

```
• Added WP Social Ninja WP-CLI commands
```

md

```
• Unified Airbnb review ID deduplication
• Optimized database queries and improved security
```

md

```
• Fixed custom review images when optimization is enabled
• Fixed optimized image localization fallback
• Fixed review keyword filter matching
• Fixed YouTube GDPR error message shape
```

## WP Social Ninja v4.2.0 [​](https://docs.wpsocialninja.com/guide/troubleshooting-support/change-log#wp-social-ninja-v4-2-0)

_Released on April 17, 2026_

✨ Newly Added🔧 Improvements🐛 Bug fixes

md

```
• Native review form builder for FluentCart, WooCommerce, and Custom Sources, removing the need for additional plugins for basic review collection (Pro)
• FluentCart integration to collect and display product reviews with product sync, primary review hub support, and customizable “Write a Review” button via templates (Pro)
• Replaced default WooCommerce review fields with WP Social Ninja review forms, providing full control over form design and review display (Pro)
• Custom Source review forms via shortcode for easy embedding anywhere on the site (Pro)
```

md

```
• Improved FluentCart review drawer (slide-in) experience (Pro)
• Flexible rating click actions for WooCommerce (drawer/scroll) (Pro)
• Show review images toggle in the review template editor settings
• Enhanced performance with server-side search and async multi-select
• Optimized database queries and improved security
```

md

```
• Fixed YouTube channel “No videos found” issue
• Fixed YouTube header banner display issue
• Fixed Google Business Profile location name issue
• Fixed formatting issues in reviews and testimonials
• Fixed review auto-sync input update issue
```

## WP Social Ninja v4.1.0 [​](https://docs.wpsocialninja.com/guide/troubleshooting-support/change-log#wp-social-ninja-v4-1-0)

_Released on January 29, 2026_

✨ Newly Added🔧 Improvements🐛 Bug fixes

md

```
• Review Status Controls: Introduced Publish, Unpublish, and Spam states for better review management
• Advanced Review Moderation: Manual approval with intelligent auto-publishing rules based on rating, content length, and keywords
• Spam Management for Reviews: Mark and unmark reviews as spam, including bulk actions
• Advanced Style Options for Review & Feed Templates: Box shadow, border radius, hover effects, padding, and spacing controls (Pro)
• Device-Based Responsive Control for “Load More” behavior
• Advanced Product Review Schema with optimized structured data for improved SEO
• Clear Cache by Individual Feed Template for better control
• Facebook Event Sorting Options to display events in preferred order (Pro)
```

md

```
• Optimized SQL queries for review counts, rating breakdowns, and business information
• Preserved manual review approval status during sync to prevent re-approving disabled reviews
• Improved WooCommerce template handling and business information processing (Pro)
• Improved Airbnb business information handling via the GraphQL API (Pro)
• Improved Facebook event feed handling and account filtering logic (Pro)
• Filtered out Instagram trial reels from account feeds
```

md

```
• Fixed an issue where WooCommerce product reviews were incorrectly inserted into non-review comments and processed as reviews (Pro)
• Fixed an issue where WP Social Ninja custom cron events could be automatically removed on certain server environments
• Resolved a masonry layout rendering issue (Pro)
• Fixed review count update issues when enabling or disabling reviews
• Fixed incorrect post ID usage in asset loading logic for WooCommerce products
• Fixed Chat Widget Viber configuration issue (Pro)
• Fixed time picker and date range type design issue
• Fixed review show/hide functionality based on keyword filtering (Pro)
```

## WP Social Ninja v4.0.2 [​](https://docs.wpsocialninja.com/guide/troubleshooting-support/change-log#wp-social-ninja-v4-0-2)

_Released on December 02, 2025_

🔒 Security

md

```
• Enhanced sanitization and permission validation for REST API requests
```

* * *

## WP Social Ninja v4.0.1 [​](https://docs.wpsocialninja.com/guide/troubleshooting-support/change-log#wp-social-ninja-v4-0-1)

_Released on December 02, 2025_

🔧 Improvements🐛 Bug fixes

md

```
• Added loader animation when switching layouts inside the Template Editor panel
```

md

```
• Fixed: HTML tags incorrectly printed in review content
• Fixed: Unpublished reviews were being displayed on the frontend
• Fixed: Reviewer name mapping issue in Fluent Forms integration (Pro)
• Fixed: Duplicate reviews appearing from Booking.com sources (Pro)
• Fixed: Custom image upload conflict caused by certain plugins (Pro)
• Fixed: Incorrect pro feature toggle behavior inside feed and review editors
```

* * *

## WP Social Ninja v4.0.0 [​](https://docs.wpsocialninja.com/guide/troubleshooting-support/change-log#wp-social-ninja-v4-0-0)

_Released on November 21, 2025_

✨ Newly Added🔧 Improvements🔒 Security🐛 Bug fixes

md

```
• Added smooth onboarding to simplify first-time setup
• Introduced Custom Sources to add and display reviews from any platform (Pro)
• Added Import & Export feature for Custom Sources (Pro)
• Added Screen Options to easily hide or show platforms
• Added Bulk Actions for templates, reviews, chat widgets, and notifications
• Introduced Dark Mode for the plugin dashboard
```

md

```
• Revamped UI and improved UX for modern and streamlined experience
• Improved overall performance
• Rebuilt WP Social Ninja Admin area using Vue 3 and Element Plus
```

md

```
• Security: Enhance HTML sanitization for user-generated content
• Security: Covered Plugin Check (PCP) Requirements for better security compliance
```

md

```
• Fixed Uncaught Error: Call to a member function get_ID() on null in actions.php when the woocommerce_comments called. (Pro)
• Fixed facebook event feed order issue (Pro)
```

* * *

## WP Social Ninja v3.20.3 [​](https://docs.wpsocialninja.com/guide/troubleshooting-support/change-log#wp-social-ninja-v3-20-3)

_Released on November 17, 2025_

🔧 Improvements

md

```
• Improved sanitization and escaping for imported reviews and feed content
```

* * *

## WP Social Ninja v3.20.2 [​](https://docs.wpsocialninja.com/guide/troubleshooting-support/change-log#wp-social-ninja-v3-20-2)

_Released on November 10, 2025_

🔧 Improvements🔒 Security🐛 Bug fixes

md

```
• Improved Judge.me review import process and fixed review display issues inside the product reviews tab (Pro)
• Displayed place id for Airbnb business names to help distinguish between businesses with the same name (Pro)
• Displayed Airbnb business place id in the business selection dropdown to avoid confusion when multiple businesses share the same name (Pro)
• Added missing translator strings and translator comments
```

md

```
• Added additional permission checks for REST API requests to improve overall data handling security
```

md

```
• Fixed compatibility issue with the Facebook Event API (Pro)
```

* * *

## WP Social Ninja v3.20.1 [​](https://docs.wpsocialninja.com/guide/troubleshooting-support/change-log#wp-social-ninja-v3-20-1)

_Released on September 25, 2025_

🐛 Bug fixes

md

```
• Fixed media upload issue
• Resolved CSS conflict in notifications and badge reviews popup modal
• Fixed Facebook feed "Order by" and keyword/hashtag filtering issues
• Fixed PHP deprecated warnings by reordering optional and required parameters in Reviews Template
• Fixed Facebook reviews, PHP 8.1 compatibility issue caused by automatic conversion of false to array
```

* * *

## WP Social Ninja v3.20.0 [​](https://docs.wpsocialninja.com/guide/troubleshooting-support/change-log#wp-social-ninja-v3-20-0)

_Released on September 18, 2025_

✨ Newly Added🔧 Improvements🐛 Bug fixes

md

```
• Judge.me reviews migration import option (Pro)
• Fresh and modern "Polaris" Reviews Template (Pro)
• WooCommerce product reviews synchronization with WP Social Ninja (Pro)
• Advanced WooCommerce reviews customization — choose layouts, templates, form styles, and control visibility options (Pro)
• Social Ninja Reviews Template placement option in WooCommerce product settings (Pro)
• Reviews Form option in WooCommerce product settings to collect WooCommerce reviews using Fluent Forms (Pro)
• New header template for WooCommerce, fluent forms and custom reviews (Pro)
• Option to collect custom reviews using Fluent Forms (Pro)
• Review photo support — collect images along with review text via Fluent Forms (Pro)
• Fluent Forms review collection with approval support for custom and WooCommerce reviews (Pro)
• Fluent Forms Rating Field: You can now add rating fields in Fluent Forms without needing Fluent Forms Pro, if you have Social Ninja Pro
• Responsive Post Count Filter: Use the new "wpsocialreviews/responsive_post_count" filter to customize the number of posts displayed based on the device (desktop, tablet, or mobile)
• Fetch More Facebook Feed Attachments: Enable the "wpsocialreviews/facebook_feed_should_fetch_more_attachments" filter to include additional child attachment photos in your Facebook feeds
```

md

```
• Updated Swiper Library: Upgraded to version 8.4.7 to resolve conflicts with Power Pack ticker
• Improved Error Handling: Added encryption error detection for Facebook Reviews, Facebook Feed, and Instagram, with clear, user-friendly error messages (includes error code 999 for access token issues)
• Improved Facebook Feed Cache: Optimized cache handling for relative date ranges, making your feeds faster and more reliable (Pro)
• Improved Tripadvisor API configuration and cleared downloadReviewsUrl for non-business URL credentials for a seamless experience
• Improved button links and accessibility for Facebook feeds, making them easier to navigate
```

md

```
• Fixed Airbnb reviews fetching issue & added support for Airbnb v3 (note: experiences and services business name & average rating not supported)
• Fixed accessibility issue with slider pagination (Pro)
• Fixed PHP deprecation issue (get_class() without arguments) for better compatibility with newer PHP versions
• Fixed error display for Facebook Reviews in the admin panel
• Fixed missing `<br>` tags in Instagram post captions on the frontend for better formatting
• Fixed Issue with Business Hours & Timezone Settings for WhatsApp Widget (Pro)
• Fixed input device activation for total posts/reviews in the editor's responsive mode, with better device key selection logic
• Fixed issues with uploading custom images (Pro)
• Fixed Chat Widget close button color change issue
• Fixed Chat Widget Template Config handling for array values, resolving a PHP 8.3 compatibility issue that caused a fatal error
• Fixed WooCommerce Template rating icon spacing and color issues
• Fixed Facebook feed album and single album image optimization and display issues (Pro)
• Fixed: Facebook feed now only shows public posts (subscriber-only posts are hidden)
• Fixed Facebook feed popup left arrow icon issue in the editor
• Fixed Instagram Feed posts hashtag links with umlauts being incorrectly generated
• Fixed Inline Instagram videos now pause other videos, preventing multiple from playing at once
• Fixed YouTube Feed live stream data update and fetch issues (Pro)
• Fixed YouTube Feed empty header display issue
• Fixed search functionality in the admin panel for all reviews
• Fixed syntax error in Reviews Template "Rigel" within the editor (Pro)
• Fixed sorting logic for feed and review posts to display them in the correct order
• Fixed reviews template CSS loading in the footer on the WooCommerce product page
• Resolved PHP maximum execution time exceeded error in the `feedsByRandom` method logic
```

* * *

## WP Social Ninja v3.19.1 [​](https://docs.wpsocialninja.com/guide/troubleshooting-support/change-log#wp-social-ninja-v3-19-1)

_Released on September 04, 2025_

🔒 Security

md

```
• Resolved a Twitter/X API credential issue in v1.1.0+ to enhance security and prevent potential misuse
```

* * *

## WP Social Ninja v3.19.0 [​](https://docs.wpsocialninja.com/guide/troubleshooting-support/change-log#wp-social-ninja-v3-19-0)

_Released on July 14, 2025_

✨ Newly Added� Improvements�🐛 Bug fixes⚠️ Notice

md

```
• Get Reviews via QR Code Module (Pro)
• Verified badge support for review platforms (Pro)
```

md

```
• Refactored rating stars and improved AI platform detection on notification popups (Pro)
• Updated Babel configuration for ES module support: Removed unused script from production version
• Improve Accessibility for reviews and Facebook feed buttons (Pro)
```

md

```
• Fixed Instagram account feeds max 100 feed limit issue
• Fixed Hashtag filter functionality for Facebook album and single album feeds (Pro)
• Fixed chat widget CSS selectors and added closing animation to chat box
• Fixed chat widget to correctly reflect the user's local timezone (Pro)
• Fixed TikTok feed disconnection issue by improving token management, adding a safety buffer for expiration checks, and enhancing error handling
```

md

```
• Airbnb review integration is temporarily unavailable due to changes in the external API. A notice has been added to the configuration screen
```

* * *

## WP Social Ninja v3.18.0 [​](https://docs.wpsocialninja.com/guide/troubleshooting-support/change-log#wp-social-ninja-v3-18-0)

_Released on May 29, 2025_

✨ Newly Added🔧 Improvements🐛 Bug fixes

md

```
• AI-powered summarizer for Reviews templates with customizable display options (Pro)
• Reviewer Name Format Option – Added setting to allow users to customize how reviewer names are displayed (Pro)
• Optimized Image Format Setting – Introduced an option to choose between JPG or WebP image formats for better optimization
```

md

```
• Star Rating Icon – Improved excessive DOM size for rating icons to enhance performance
```

md

```
• Edit Button Visibility – Resolved visibility issue with the Edit button on reviews templates
• Feed Popup Layout – Fixed height adjustment issue to ensure consistent layout in the feed popup
• "Write a Review" Button – Updated element type to prevent template layout breakage (Pro)
• Review Business Info & Button URL – Fixed issues related to displaying business info and custom "Write a Review" button URL (Pro)
• Reviews Popup Styling – Fixed issue with styling not updating in the notifications reviews popup (Pro)
• Fixed the restriction issue affecting optimized image URLs
• Fixed the no default translation string issue in translation settings
```

* * *

## WP Social Ninja v3.17.0 [​](https://docs.wpsocialninja.com/guide/troubleshooting-support/change-log#wp-social-ninja-v3-17-0)

_Released on May 06, 2025_

✨ Newly Added🔧 Improvements🐛 Bug fixes🗑️ Deprecation

md

```
• SMS chat widget (Pro)
• Microsoft Teams chat widget (Pro)
• Instagram DM chat widget (Pro)
• Support for Facebook Single Photo Album via Album ID (Pro)
• Support for Facebook Specific Video Playlist via Playlist URL (Pro)
• Option to show Fluent Forms or custom URLs in Reviews business info/badge section (Pro)
• Support for YouTube feed – users can now collect feeds using channel handle, username, or channel ID
• WhatsApp Pro is now available in the Free version (other Pro features remain locked)
• Prefilled support for SMS and WhatsApp widgets (layout types: box and icons) (Pro)
• Official 3:4 aspect ratio support for Instagram templates
• Enhanced WeChat widget (Pro)
```

md

```
• Improved Facebook Events API integration – users can now collect Facebook event feeds (Pro)
• Improved: User can display likes, comments count and header bio text, fullname for instagram business basic account
• Updated Twitter/X official logo on twitter template
```

md

```
• Resolved issue with multiple Fluent Forms overlapping in the chat widget (Pro)
• Fixed issues with editing and deleting chat widgets
• Resolved Oxygen Builder escaping issue
• Fixed manual Instagram connection issue
• Fixed issue with reviews media URLs when image optimization is enabled
• Resolved "Load More" issue in reviews (Pro)
• Fixed Instagram account feed video media URL issue
```

md

```
• Removed Skype from the chat widget due to Microsoft discontinuing support for Skype integration
```

* * *

## WP Social Ninja v3.16.2 [​](https://docs.wpsocialninja.com/guide/troubleshooting-support/change-log#wp-social-ninja-v3-16-2)

_Released on March 11, 2025_

🔒 Security🔧 Improvements

md

```
• Improve data escaping and overall plugin security
• Restricted direct access to plugin upload directory for better protection
```

md

```
• Improved Queries performance
```

* * *

## WP Social Ninja v3.16.1 [​](https://docs.wpsocialninja.com/guide/troubleshooting-support/change-log#wp-social-ninja-v3-16-1)

_Released on February 19, 2025_

🐛 Bug fixes

md

```
• Fixed a critical issue where the sort() function was incorrectly applied to a string instead of an array in the Facebook Helper
```

* * *

## WP Social Ninja v3.16.0 [​](https://docs.wpsocialninja.com/guide/troubleshooting-support/change-log#wp-social-ninja-v3-16-0)

_Released on February 18, 2025_

✨ Newly Added🔧 Improvements🐛 Bug fixes

md

```
• Support for exporting and importing: Testimonials, Feed and reviews templates, Notification popups & Chat widgets (Pro)
• Full platform data deletion option to enhance user control and ensure compliance with data privacy standards (Pro)
• Now supports displaying Facebook timeline feeds as a Facebook photo feed (Pro)
• Image optimization support for the reviews slider (Pro)
• Introduced 4:5 aspect ratio for Instagram feed images
```

md

```
• Improved WhatsApp pre-filled message functionality for smoother user interaction (Pro)
• Improved Facebook Feed Template responsiveness to ensure optimal display across devices
```

md

```
• Resolved reviewer image inconsistencies in testimonials and custom reviews (Pro)
• Fixed CSS conflicts with Elementor Pro's Swiper component (Pro)
• Resolved issues with fetching reviews from Booking.com (Pro)
• Fixed missing Facebook business details display issues (Pro)
• Remove unnecessary string from reviewer image url (Pro)
• Fixed Booking.com reviews fetch issues (Pro)
• Fixed an issue causing unknown Facebook API error messages
• Fixed image resizing issue where only the first feed template was processing images, while other templates were not resizing them correctly. Now, all templates handle image resizing properly
• Addressed missing Instagram video display problems
• Fixed YouTube feed image size modifications not applying correctly when using add_filter
• Updated Twitter/X official logo
• Fixed Facebook feed alt tag empty issue to improve accessibility
• Ensured Read More/Read Less truncates HTML content correctly
• Refactored Avatar & Cover assignments to prevent undefined key issues
• Fixed Instagram video carousel album thumbnail visibility issues
```

* * *

## WP Social Ninja v3.15.1 [​](https://docs.wpsocialninja.com/guide/troubleshooting-support/change-log#wp-social-ninja-v3-15-1)

_Released on December 05, 2024_

🐛 Bug fixes

md

```
• PHP Fatal Error caused by missing 'Optimize Images' table
• Issue with the 'Template Source Empty' error displaying incorrectly
```

* * *

## WP Social Ninja v3.15.0 [​](https://docs.wpsocialninja.com/guide/troubleshooting-support/change-log#wp-social-ninja-v3-15-0)

_Released on December 04, 2024_

⚠️ Action Required✨ Newly Added🔧 Improvements🐛 Bug fixes

md

```
• If you have a personal account connection, please reconnect your account before December 2024 after updating to version 3.15.0 or higher
```

md

```
• Optimize Images settings option in Settings → Advanced Settings → Optimize Reviews Image Settings. This feature automatically stores local copies of Reviews images on your server
• Optimize Images settings option in Settings → Feed Platforms → YouTube Settings. This feature automatically stores local copies of YouTube feed images on your server
• YouTube Feed GDPR compliant settings option in Settings → Advanced Settings
• Optimize Images reset option in Settings → Feed Platforms → YouTube Settings
• Optimize Image resolution settings option in Template Editor → Feed/Settings → Images Resolution
• Option to configure pre-filled messages for WhatsApp
• Address field option for schema snippets
• Ability to reorder chat widget channels
```

md

```
• Improved support for collecting language-specific reviews from Tripadvisor and Booking reviews
```

md

```
• Fixed an issue with Instagram feed accessibility
• Fixed an issue with Fluent Forms business info display
• Fixed a TikTok feed filter issue on mobile devices
• Fixed TikTok popup responsiveness issues
• Fixed responsive styling for reviews header ratings
• Fixed the disappearing date styling option for review platforms
• Fixed empty business info appearing in Google Reviews configuration
• Fixed a dependency issue with the widget for the wp-block-editor
```

* * *

## WP Social Ninja v3.14.2 [​](https://docs.wpsocialninja.com/guide/troubleshooting-support/change-log#wp-social-ninja-v3-14-2)

_Released on October 07, 2024_

🐛 Bug fixes

md

```
• Fixed unknown error message display issue
• Fixed reviews rating icon color display issue
• Remove unnecessary animated bg class from free version
• Fixed optimize profile photo invalid url issue
• Fixed instagram feed multiple hashtag issue (Pro)
• Fixed Facebook Feed album photos popup issue (Pro)
• Fixed Facebook album feed popup slider changes issue (Pro)
```

* * *

## WP Social Ninja v3.14.1 [​](https://docs.wpsocialninja.com/guide/troubleshooting-support/change-log#wp-social-ninja-v3-14-1)

_Released on September 23, 2024_

🔧 Improvements🐛 Bug fixes

md

```
• Updated TikTok Feed Template 2 to be GDPR-compliant and optimized for image loading (Pro)
```

md

```
• Resolved an issue where database tables were not being created for subsites if the wp social ninja was installed after the subsites were created. Tables will now correctly generate for both the main site and all subsites, regardless of installation time
• Preloader in feed templates not disappearing after storing images locally has been resolved. Preloader now correctly disappears after images are successfully stored
• Fixed PHP 8.3 compatibility issue, which caused a fatal error due to a null argument being passed to array_keys() in the ShortcodeHandler.php file
• Corrected the issue with the "Filter Number of Feeds to Display" limit for feeds, ensuring that the specified limit now works as intended
• Addressed an issue with the feed display limit, ensuring it now functions correctly
• Fixed post URL popup and redirection issue in Facebook feed template
• Resolved an issue where the "Posts Order by Most Popular" and "Posts Order by Least Popular" options in Facebook feeds were not functioning correctly. Filters now work as expected, displaying posts based on popularity (Pro)
• Fixed the average rating display to show a maximum of one decimal number (Pro)
```

* * *

## WP Social Ninja v3.14.0 [​](https://docs.wpsocialninja.com/guide/troubleshooting-support/change-log#wp-social-ninja-v3-14-0)

_Released on September 18, 2024_

✨ Newly Added🔧 Improvements🐛 Bug fixes

md

```
• Tripadvisor reviews API (Pro)
• Field for Facebook feed followers count (in addition to likes count) and fixed the issue with undefined media URLs (Pro)
• Optimize Images settings option in Settings → Feed Platforms → Facebook,TikTok Settings. This feature automatically stores local copies of Facebook,TikTok feed images on your server
• Facebook,TikTok Feed GDPR compliant settings option in Settings → Advanced Settings
• Optimize Images reset option in Settings → Feed Platforms → Facebook,TikTok Settings
• Optimize Image resolution settings option in Template Editor → Feed → Images Resolution
• Warning notice in the wp social ninja admin area to alert you about critical issues with your Facebook,TikTok Feed and Facebook Reviews
• Email notification alerts for critical Facebook,TikTok Feed and Facebook Reviews issues. You will receive an email notification if there's an unresolved issue with an Facebook,TikTok feed or Facebook Reviews on your website
```

md

```
• Improved Instagram image optimization by fixing the issue with multiple avatar downloads and ensuring images load from local storage
```

md

```
• Fixed the review rating problem so you see the exact rating every time
• Fixed the Instagram feed animation issue so that images of different sizes and resolutions display perfectly on the screen
• Fixed the problem of missing Instagram videos – now all videos will be shown properly
• Fixed the Instagram videos display issue in the free version so videos can now play directly from the template
• Fixed the issue with Instagram popup images overlapping, which will ensure images and text display correctly without any glitches (Pro)
• Fixed Airbnb business info issue, which will show details in the header including ratings & number of reviews (Pro)
• Fixed the spacing issue in the Instagram feed carousels so images are now properly aligned (Pro)
• Fixed fallback average rating and total rating issue of schema snippet for reviews template (Pro)
• Fixed review content read more and less excerpt issue (Pro)
• Fixed the Facebook album layout issue so users won't see any stretched images (Pro)
• Fixed and improved the feed slider so images no longer flash (Pro)
```

* * *

## WP Social Ninja v3.13.1 [​](https://docs.wpsocialninja.com/guide/troubleshooting-support/change-log#wp-social-ninja-v3-13-1)

_Released on April 03, 2024_

🐛 Bug fixes

md

```
• Resolved Facebook Pages and Instagram account connectivity problems
• Fixed the string translation issue in the editor
```

* * *

## WP Social Ninja v3.13.0 [​](https://docs.wpsocialninja.com/guide/troubleshooting-support/change-log#wp-social-ninja-v3-13-0)

_Released on March 12, 2024_

✨ Newly Added🔧 Improvements🐛 Bug fixes

md

```
• TikTok Feed
• TikTok Feed Elementor Widget
• TikTok Feed Oxygen Widget
• TikTok Feed Beaver Widget
```

md

```
• Chat widget improvements
```

md

```
• Fixed chat widget query limit issue
• Fixed Airbnb reviews fetching issue
• Addressed ${var} deprecation issue in PHP 8.2
• Addressed translation text issue in editor panel
```

* * *

_For older versions and complete history, please refer to the plugin's admin changelog or contact support._

* * *

## Additional Links [​](https://docs.wpsocialninja.com/guide/troubleshooting-support/change-log#additional-links)

*   [Getting Started Guide](https://docs.wpsocialninja.com/guide/getting-started/getting-started-with-wp-social-ninja)
*   [Support & Troubleshooting](https://docs.wpsocialninja.com/guide/troubleshooting-support/facebook-feeds-not-updating)
