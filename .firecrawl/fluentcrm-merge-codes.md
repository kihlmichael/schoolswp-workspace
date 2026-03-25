[Skip to content](https://fluentcrm.com/docs/merge-codes-smart-codes-usage#main)

Special [20% Discount](https://fluentcrm.com/deal/?utm_source=fcrmsite&utm_medium=banner&utm_campaign=special26&utm_id=special+deal) on Email Automation

[Start Automation](https://fluentcrm.com/deal/?utm_source=fcrmsite&utm_medium=banner&utm_campaign=special26&utm_id=special+deal)

All CategoriesGetting StartedGlobal SettingsFluentCRM EssentialsContactsEmailsFormsAutomationsEvent TrackingReportsPlugins Integration & AutomationMigrating from Other PlatformsBounce HandlersMiscellaneousDeveloper DocumentationFrequently Asked QuestionsChange Log

Popular Searchautomationtheunsubscribewebhookcustom

View Categories

4 min read

Table of Contents

- [Basic Structure:](https://fluentcrm.com/docs/merge-codes-smart-codes-usage#basic-structure)
- [Usage:](https://fluentcrm.com/docs/merge-codes-smart-codes-usage#usage-)
- [Contact's Default Merge Codes](https://fluentcrm.com/docs/merge-codes-smart-codes-usage#contacts-default-merge-codes)
- [Other General Codes](https://fluentcrm.com/docs/merge-codes-smart-codes-usage#other-general-codes)
- [WP User Codes](https://fluentcrm.com/docs/merge-codes-smart-codes-usage#wp-user-codes)
- [Data Transformers](https://fluentcrm.com/docs/merge-codes-smart-codes-usage#data-transformers)

FluentCRM offers lots of dynamic merge codes for your email subject, the body that you can use to personalize your emails.

### Basic Structure: [\#](https://fluentcrm.com/docs/merge-codes-smart-codes-usage\#basic-structure)

Merge codes are structured as {{DataGroup.Property\|FallbackValue\|Transformer}}

- **DataGroup**: FluentCRM has different types of data group. Examples: contact, contact.custom, wp etc.
- **Property**: Each data groups offer many data values, and you can call that the property. For example: first\_name, last\_name, email
- **Fallback Value (Optional)**: This is an optional parameter. If the defined property is empty, the fallback value will be returned.
- **Transformer (optional):** Fluent Forms offers utility functions to transform the dynamic return value. For example: {{contact.first\_name\|Hi\|ucfirst}} will make this first letter of the first as uppercase.

### Usage: [\#](https://fluentcrm.com/docs/merge-codes-smart-codes-usage\#usage-)

Using merge is very easy. From your email composer, just type @ and then type the name or title of the merge code and you can see all of them.

![image](https://fluentcrm.com/wp-content/uploads/2022/05/image-1024x747.png)

You can see all the merge codes by clicking the {{ }} icon in your email composer’s top bar.

![image 1](https://fluentcrm.com/wp-content/uploads/2022/05/image-1-1024x250.png)

This will show a pop-up and you can copy any SmartCode you want and use it in your email body or subject.

![image 2](https://fluentcrm.com/wp-content/uploads/2022/05/image-2-1024x724.png)Merge code Lists

### Contact’s Default Merge Codes [\#](https://fluentcrm.com/docs/merge-codes-smart-codes-usage\#contacts-default-merge-codes)

| Code | Description |
| --- | --- |
| {{contact.full\_name}} | Full name of the contact |
| {{contact.prefix}} | Name Prefix of the contact |
| {{contact.first\_name}} | First Name of the contact |
| {{contact.last\_name}} | Last Name of the contact |
| {{contact.email}} | Email address |
| {{contact.id}} | Contact’s unique ID (Numeric) |
| {{contact.user\_id}} | Connected User ID of the contact |
| {{contact.address\_line\_1}} | Address Line 1 |
| {{contact.address\_line\_2}} | Address Line 2 |
| {{contact.city}} | Address City |
| {{contact.state}} | Address State |
| {{contact.postal\_code}} | Address Postal Code |
| {{contact.country}} | Address Country |
| {{contact.phone}} | Phone Number |
| {{contact.status}} | Contact’s Status |
| {{contact.date\_of\_birth}} | Date of Birth |
| {{contact.custom.CUSTOM\_FIELD\_SLUG}} | Custom Field value of the contact. Please replace CUSTOM\_FIELD\_SLUG with your defined slug of the field |

### Other General Codes [\#](https://fluentcrm.com/docs/merge-codes-smart-codes-usage\#other-general-codes)

| Code | Description |
| --- | --- |
| **{{crm.business\_name}}** | Business Name defined in FluentCRM Settings |
| **{{crm.business\_address}}** | Business Address defined in FluentCRM Settings |
| **{{wp.admin\_email}}** | Email Address defined in WordPress settings |
| **{{wp.url}}** | Your Website URL |
| {{other.date.+2 days}} | Dynamic Date Field. You can replace **+2 days** with your own date strings. it will return the date (WP Date Format) when parsing the data. |
| {{other.date\_format.Y-m-d}} | Current date field as your own date format. Support Y-m-d date formate. |
| ##crm.unsubscribe\_url## | Unsubscribe URL of the contact |
| ##crm.manage\_subscription\_url## | Manage Subscription page URL of the contact |
| ##web\_preview\_url## | Web preview Url of an email |
| {{crm.unsubscribe\_html\|Unsubscribe}} | This will return an unsubscribe link with HTML code and link text will be **Unsubscribe.** |
| ‘{{crm.manage\_subscription\_html\|Manage Preference}} | Manage Subscription Hyperlink HTML with link text “Manage Preference” |

### WP User Codes [\#](https://fluentcrm.com/docs/merge-codes-smart-codes-usage\#wp-user-codes)

If the contact is also your WordPress user then you can use the following merge codes in your email

| Code | Description |
| --- | --- |
| {{user.ANY\_USER\_PROPERY}} | example: get any user property from WP\_User Class. Example: user\_login, user\_first\_name etc. |
| {{user.meta.USER\_META\_KEY}} | access meta value of a user |
| {{user.password\_reset\_direct\_link}} | Direct Password Reset link of a user |

### Data Transformers [\#](https://fluentcrm.com/docs/merge-codes-smart-codes-usage\#data-transformers)

Using Data Transformers you can transform / Format a dynamic value easily. Here is the list of available transformers

| Transformer | Usage | Description |
| --- | --- | --- |
| **trim** | {{contact.first\_name\|There\|trim}} | if the **contact.first\_name** returns value and have space at first or after it will trim that. |
| **ucfirst** | {{contact.first\_name\|There\|ucfirst}} /<br>{{contact.first\_name\|\|ucfirst}} | If the contact.first\_name returns the first letter lowercase, it will make it uppercase of the first letter |
| **strtolower** | {{contact.first\_name\|There\|strtolower}} /<br>{{contact.first\_name\|\|strtolower}} | It will make the all the letters as lowercase |
| **strtoupper** | {{contact.first\_name\|There\|strtoupper}} /<br>{{contact.first\_name\|\|strtoupper}} | It will make the all the letters as uppercase |
| **ucwords** | {{contact.full\_name\|There\|ucwords}} /<br>{{contact.full\_name\|\|ucwords}} | This will make the first letter of each word uppercase. |
| **concat\_first** | {{contact.first\_name\|\|concat\_first\|Hello}} | if a contact’s first name is **John** then it will return as “Hello **John**” |
| **concat\_last** | {{contact.first\_last\|\|concat\_last\| **,**}} | Sometimes you need to add “,” after the first name if the name exists. This example will return **“John,”** if the first name exists . If first name does not exist then nothing will return. |
| **show\_if** | {{contact.full\_name\|\|show\_if\|First name exist}} | If contact’s full name exist then it will return “First name exist” |

##### What are your Feelings

#### Share This Article :

- [![Facebook](https://fluentcrm.com/wp-content/plugins/betterdocs/assets/images/social/facebook.svg?v=4.3.7)](https://www.facebook.com/sharer/sharer.php?u=https://fluentcrm.com/docs/merge-codes-smart-codes-usage/)
- [![X](https://fluentcrm.com/wp-content/plugins/betterdocs/assets/images/social/twitter.svg?v=4.3.7)](https://twitter.com/intent/tweet?url=https://fluentcrm.com/docs/merge-codes-smart-codes-usage/)
- [![LinkedIn](https://fluentcrm.com/wp-content/plugins/betterdocs/assets/images/social/linkedin.svg?v=4.3.7)](https://www.linkedin.com/shareArticle?mini=true&url=https://fluentcrm.com/docs/merge-codes-smart-codes-usage/)
- [![Pinterest](https://fluentcrm.com/wp-content/plugins/betterdocs/assets/images/social/pinterest.svg?v=4.3.7)](https://pinterest.com/pin/create/button/?url=https://fluentcrm.com/docs/merge-codes-smart-codes-usage/)

[Still stuck? How can we help?](https://fluentcrm.com/docs/merge-codes-smart-codes-usage#betterdocs-form-modal)

## How can we help?

Name: \*

Email: \*

Message: \*

Updated on August 23, 2024

[FluentCRM Contacts Status](https://fluentcrm.com/docs/fluentcrm-contacts-status/) [Cloudflare or Security Plugin Compatibility](https://fluentcrm.com/docs/cloudflare-or-security-plugin-compatibility/)

## 41 Comments

01. Can I enter a shortcode from Woocommerce to show products \[products\]? – it didn’t work by adding it to the text block.





    [Reply](https://fluentcrm.com/docs/merge-codes-smart-codes-usage/comment-page-2/?replytocom=5733#respond)

    1. WooCommerce shortcodes aren’t supported. However, if your merge codes doesn’t apply, please report the issue to our team.





       [Reply](https://fluentcrm.com/docs/merge-codes-smart-codes-usage/comment-page-2/?replytocom=5742#respond)
02. I want a smart code to asign woocommerce coupon codes on fluentcrm emails





    [Reply](https://fluentcrm.com/docs/merge-codes-smart-codes-usage/comment-page-2/?replytocom=5694#respond)

    1. It’s possible via Automation already. Are you looking for something different?





       [Reply](https://fluentcrm.com/docs/merge-codes-smart-codes-usage/comment-page-2/?replytocom=5752#respond)
03. Hello – Is there a way to call out the product the buyer purchased with a smart code in the email, such as {{order.product\_name}}?





    [Reply](https://fluentcrm.com/docs/merge-codes-smart-codes-usage/comment-page-2/?replytocom=5628#respond)

    1. Hi Michael, if you’re using WooCommerce automation, yes you can do this. Please check the Woo Current Order merge codes.





       [Reply](https://fluentcrm.com/docs/merge-codes-smart-codes-usage/comment-page-2/?replytocom=5681#respond)

       1. Hello, How do i assign my already created smart coupon by woocommerce in fluent crm so as to enable that my email pulls up that unique code which will be unique for every new user. Next is how can be bale to edit fluent email is confirmed page to enable full re-route to a much better UX/UI page





          [Reply](https://fluentcrm.com/docs/merge-codes-smart-codes-usage/comment-page-2/?replytocom=5693#respond)
04. Is it possible to add posts from custom post types as the latest post? If so how do I do it?





    [Reply](https://fluentcrm.com/docs/merge-codes-smart-codes-usage/comment-page-2/?replytocom=5513#respond)

    1. Custom post types isn’t available yet. We will see if it can be implemented. 🙂





       [Reply](https://fluentcrm.com/docs/merge-codes-smart-codes-usage/comment-page-2/?replytocom=5529#respond)

       1. We need this 🙂





          [Reply](https://fluentcrm.com/docs/merge-codes-smart-codes-usage/comment-page-2/?replytocom=5662#respond)
05. How can we had our product’s image using the WooCommerce mergecodes for abandoned carts? Is it possible to customize the look of it?





    [Reply](https://fluentcrm.com/docs/merge-codes-smart-codes-usage/comment-page-2/?replytocom=5448#respond)

    1. Hi Hubert, image merging isn’t available yet. I’m sure there will be some updates that fix it. 🙂





       [Reply](https://fluentcrm.com/docs/merge-codes-smart-codes-usage/comment-page-2/?replytocom=5507#respond)

       1. This should be done asap 🙁 it’s a serious issue for customizable product!





          [Reply](https://fluentcrm.com/docs/merge-codes-smart-codes-usage/comment-page-2/?replytocom=5607#respond)

          1. Hi Aus, this will take a few more weeks. In the meantime, you can discuss this in [our Community](https://community.wpmanageninja.com/portal/space/fluent-crm/home)





             [Reply](https://fluentcrm.com/docs/merge-codes-smart-codes-usage/comment-page-2/?replytocom=5610#respond)
06. how can I put a code for woocommerce products?





    [Reply](https://fluentcrm.com/docs/merge-codes-smart-codes-usage/comment-page-2/?replytocom=5251#respond)

    1. You can use WooCommerce mergecodes when using a WooCommerce automation trigger





       [Reply](https://fluentcrm.com/docs/merge-codes-smart-codes-usage/comment-page-2/?replytocom=5264#respond)
07. How can I merge the Primary Company that the contact is attached to? It’s not listed in the merge list anywhere and it’s a crucial field for our emails.





    [Reply](https://fluentcrm.com/docs/merge-codes-smart-codes-usage/comment-page-2/?replytocom=5221#respond)

    1. Hi Chelle, this feature isn’t available. We’ll add this shortly in the next version.





       [Reply](https://fluentcrm.com/docs/merge-codes-smart-codes-usage/comment-page-2/?replytocom=5237#respond)
08. I would like to be able to automatically populate today’s date in a date field whenever a contact passes through a particular automation. Is there a smart code for today’s date? or another way to auto-populate the current date to a field?





    [Reply](https://fluentcrm.com/docs/merge-codes-smart-codes-usage/comment-page-2/?replytocom=5213#respond)

    1. Not yet. We will add this in the next version.





       [Reply](https://fluentcrm.com/docs/merge-codes-smart-codes-usage/comment-page-2/?replytocom=5241#respond)
09. I would like to create a confirmation email template for the different purchase statuses. Is it possible to include product details (product name, quantity, price) using variables? I’ve only found options for order number/ID.”





    [Reply](https://fluentcrm.com/docs/merge-codes-smart-codes-usage/comment-page-2/?replytocom=5198#respond)

    1. Hi Zoltan, Yes, you can do that from automations if you use WooCommerce triggers (merge tags for WooCommerce stay hidden unless you’re using WooCommerce triggers). 🙂





       [Reply](https://fluentcrm.com/docs/merge-codes-smart-codes-usage/comment-page-2/?replytocom=5205#respond)
10. I don’t know if anyone has the same problem. Last time I asked how to use Fluentcrm and whether it was possible to send a notification of forgotten password. The customer service said it couldn’t be used.



    Later I found a method that can easily solve this problem with Elementor.



    First, you need to set up new Tags or Lists in Fluentcrm, and create a user in the automation area to add new Tags or Lists, and open it multiple times in the status field. After setting up, an email will be sent automatically, and the email will contain {{user.password\_reset\_direct\_link}}. (I don’t know if it’s necessary, but I have settings to automatically cancel Tags or Lists after sending.)



    And use Elementor’s pop-up window, and put in the “form”, just put the Email field. For the action after “Send”, click Fluentcrm and set the name you created in Tags or Lists. (A Fluentcrm field will appear, where you need to select Email)



    In this way, the website’s forgotten password email can be achieved.





    [Reply](https://fluentcrm.com/docs/merge-codes-smart-codes-usage/comment-page-2/?replytocom=5149#respond)


### Leave a Reply [Cancel reply](https://fluentcrm.com/docs/merge-codes-smart-codes-usage/\#respond)

Your email address will not be published.Required fields are marked \*

Comment \*

Name \*

Email \*

Save my name, email, and website in this browser for the next time I comment.

[![fluentcrm logo tagline color white](https://fluentcrm.com/wp-content/uploads/2023/07/fluentCRM-logo-tagline-color_white.svg)](https://fluentcrm.com/)

FluentCRM is a marketing automation plugin for WordPress. Our vision is to make email marketing affordable for small businesses

Subscribe to Our Newsletter

Footer Form

Subscribe

Subscribe

We won’t send you spam. Unsubscribe at any time.

SOCIAL

- [https://www.facebook.com/groups/fluentcrm/](https://www.facebook.com/fluentcrm)
- [#](https://twitter.com/fluentcrm)
- [LinkedIn](https://www.linkedin.com/company/fluentcrm)
- [YouTube](https://www.youtube.com/watch?v=8LO6NuL9Bhg&list=PLXpD0vT4thWG-ZPeM6cco7BS5cJY9bTjL)

- **COMPANY**
- [About Us](https://fluentcrm.com/about-us/)
- [Contact](https://fluentcrm.com/contact-us/)
- [Support](https://wpmanageninja.com/support-tickets/)
- [Affiliate Program](https://wpmanageninja.com/affiliate/)
- [Community](https://community.wpmanageninja.com/portal/space/fluent-crm/home)
- [Report an Issue](https://fluentcrm.com/security-and-vulnerability-disclosure-program/)
- [Brand Guideline](https://fluentcrm.com/resources/)

- **RESOURCES**
- [Our Vision](https://fluentcrm.com/fluentcrm-vision/)
- [Blog](https://fluentcrm.com/blog/)
- [Documentation](https://fluentcrm.com/docs/)
- [Free vs Pro](https://fluentcrm.com/free-vs-pro/)
- [FluentCRM 101](https://fluentcrm.com/fluentcrm-101/)

- **INTEGRATIONS**
- [WooCommerce](https://fluentcrm.com/integrations/woocommerce-marketing-automation/)
- [Fluent Forms](https://fluentcrm.com/integrations/fluent-forms-integration/)
- [PM Pro](https://fluentcrm.com/integrations/paid-memberships-pro-integration/)
- [BuddyBoss](https://fluentcrm.com/integrations/buddyboss-integration/)
- [EDD](https://fluentcrm.com/integrations/easy-digital-downloads-integration-fluentcrm/)
- [LearnPress](https://fluentcrm.com/integrations/learnpress-integration/)
- [LearnDash](https://fluentcrm.com/integrations/learndash-integration-fluentcrm/)
- [LifterLMS](https://fluentcrm.com/integrations/lifterlms/)

- **OUR PRODUCTS**
- [Fluent Forms](https://fluentforms.com/)
- [FluentBooking](https://fluentbooking.com/?utm_source=fcrm_site&utm_medium=fcrm_website&utm_campaign=fcrm_site&utm_id=fcrm&utm_content=link)
- [FluentBoards](https://fluentboards.com/)
- [Fluent Support](https://fluentsupport.com/)
- [FluentCommunity](https://fluentcommunity.co/)
- [FluentSnippets](https://fluentsnippets.com/)
- [FluentSMTP](https://fluentsmtp.com/?utm_source=fcrm_site&utm_medium=fcrm_website&utm_campaign=fcrm_site&utm_id=fcrm&utm_content=link)
- [Paymattic](https://paymattic.com/)
- [Ninja Tables](https://ninjatables.com/)
- [WP Social Ninja](https://wpsocialninja.com/)
- [AzonPress](https://azonpress.com/)
- [FluentCart](https://fluentcart.com/)

Copyright © 2025 [FluentCRM](https://fluentcrm.com/). A Brand of [WPManageNinja™](https://wpmanageninja.com/) [Affiliate](https://wpmanageninja.com/affiliate/) [Terms](https://wpmanageninja.com/terms-and-conditions/) [Privacy](https://wpmanageninja.com/privacy/)

![2025 11 17 06 00 pm 1763380818](https://fluentcrm.com/wp-content/uploads/2023/12/2025_11_17_06_00_PM_1763380818.webp)

Plugin Download Form

Newsletter

Please Enter Your Email Address to Download FluentCRM (Free)

By downloading FluentCRM, I agree to have this website save my email address for further communication.

DOWNLOAD

Forget Opens, Build Relationships

The Email

Marketing Blueprint

The average campaign gets 39% opens and $0.11 per subscriber. **_Top WordPress founders and influencers consistently pull 54%+ opens and $30K+ campaigns._** This guide shows you exactly how they do it, so you can, too!

Email Marketing Blueprint

Contact

First Name

Last Name

Email Address

Get the Free Blueprint

Sign Up for Our Newsletter

Mobile Blog Update Feed

Subscribe

SUBSCRIBE