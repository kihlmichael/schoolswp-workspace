[Skip to content](https://fluentcrm.com/docs/advanced-features-settings#main)

Special [20% Discount](https://fluentcrm.com/deal/?utm_source=fcrmsite&utm_medium=banner&utm_campaign=special26&utm_id=special+deal) on Email Automation

[Start Automation](https://fluentcrm.com/deal/?utm_source=fcrmsite&utm_medium=banner&utm_campaign=special26&utm_id=special+deal)

All CategoriesGetting StartedGlobal SettingsFluentCRM EssentialsContactsEmailsFormsAutomationsEvent TrackingReportsPlugins Integration & AutomationMigrating from Other PlatformsBounce HandlersMiscellaneousDeveloper DocumentationFrequently Asked QuestionsChange Log

Popular Searchautomationtheunsubscribewebhookcustom

View Categories

6 min read

Table of Contents

- [Advanced Features Configuration](https://fluentcrm.com/docs/advanced-features-settings#advanced-features-configuration)
  - [Quick Contact Navigation](https://fluentcrm.com/docs/advanced-features-settings#quick-contact-navigation)
  - [Campaign Archives](https://fluentcrm.com/docs/advanced-features-settings#campaign-archives)
  - [Enabling the Global Campaign Archive](https://fluentcrm.com/docs/advanced-features-settings#enabling-the-global-campaign-archive)
  - [Use this shortcode in a page/post to list past campaigns](https://fluentcrm.com/docs/advanced-features-settings#use-this-shortcode-in-a-pagepost-to-list-past-campaigns)
  - [Advanced Campaign Archives with Shortcodes](https://fluentcrm.com/docs/advanced-features-settings#advanced-campaign-archives-with-shortcodes)
    - [Shortcode Parameters:](https://fluentcrm.com/docs/advanced-features-settings#shortcode-parameters)
  - [Date & Time Format](https://fluentcrm.com/docs/advanced-features-settings#date--time-format)
  - [Navigation](https://fluentcrm.com/docs/advanced-features-settings#navigation)
  - [Company Module](https://fluentcrm.com/docs/advanced-features-settings#company-module)
  - [Disable AI?](https://fluentcrm.com/docs/advanced-features-settings#disable-ai)
  - [Multi-Threading Email Sending?](https://fluentcrm.com/docs/advanced-features-settings#multithreading-email-sending)
  - [System Log](https://fluentcrm.com/docs/advanced-features-settings#system-log)

[FluentCRM](https://fluentcrm.com/) offers another **Advanced Features Configuration** under the **Global Settings** tab where you will find different advanced settings that you can **enable** or **disable** anytime as per your needs. This article will guide you through the process of using this Advanced Features Configuration.

## Advanced Features Configuration [\#](https://fluentcrm.com/docs/advanced-features-settings\#advanced-features-configuration)

To learn how to use **Advanced Feature Configuration**, follow the steps with screenshots below accordingly **–**

First, go to **Settings** from the top right corner of the **FluentCRM Navbar** and click the **Advanced Feature Config** settings option.

You will now get the advanced settings options inside the **Advanced Features Settings** page. These are:

- Quick Contact Navigation
- Campaign Archives
- Date & Time Format
- Navigation
- Company Module
- Disable AI?
- Multi-Threading Email Sending
- System Log

![advanced features configuration settings fluentcrm](https://fluentcrm.com/wp-content/uploads/2023/03/Advanced-Features-Configuration-Settings-FluentCRM-scaled.webp)

**A detailed explanation of the Settings mentioned above is given below –**

### Quick Contact Navigation [\#](https://fluentcrm.com/docs/advanced-features-settings\#quick-contact-navigation)

It’s a little navigation bar at the bottom of your contacts. You can make a direct call or mail from this navigation bar. Also, you can go to the next and the previous contacts from here.

To activate it, simply enable the **Quick Contact Navigation** checkbox inside the **Advanced Features Settings** page.

Then, you must click the **Update Settings** button to save the changes you’ve made.

![quick contact navigation](https://fluentcrm.com/wp-content/uploads/2023/03/Quick-Contact-Navigation.webp)

Here is the **Preview** of **Quick Contact Navigation**.

![preview of quick contact navigation](https://fluentcrm.com/wp-content/uploads/2023/03/Preview-of-Quick-contact-navigation.webp)

### Campaign Archives [\#](https://fluentcrm.com/docs/advanced-features-settings\#campaign-archives)

The Campaign Archives feature in FluentCRM allows you to display your past email campaigns on any page of your website. This is an excellent way to showcase your newsletters and create an accessible archive for your audience. You can display your campaigns by enabling the global archive settings or by using a flexible shortcode for more specific control.

### **Enabling the Global Campaign Archive** [\#](https://fluentcrm.com/docs/advanced-features-settings\#enabling-the-global-campaign-archive)

To get started with the basic archive functionality, you first need to enable it in the FluentCRM settings.

1. Navigate to your WordPress dashboard, go to **FluentCRM > Settings > Advanced Features**. You can also enable the **Campaign Archives** feature using the **Addons** section from your FluentCRM sidebar.
2. Find the **Enable** **Campaign Archive Frontend Feature** and check the box to enable it.
3. Upon enabling, a popup will appear with a general shortcode and settings.
4. From here, you can configure the global display settings:
   - **List the campaigns if the title match the provided keyword:** You can filter campaigns by keywords that appear in the campaign title.
   - **Select Campaigns:** Select the campaigns you want to show from the dropdown.
   - **Filter by Status:** Choose which types of campaigns you want to display (e.g., Archived, Published).
   - **Max Campaigns to list:** Set a limit for how many campaigns will be displayed on the archive page. The maximum is 50.
5. Click the **Update Settings** button to save your changes.

![fluentcrm campaign archive](https://fluentcrm.com/wp-content/uploads/2023/03/FluentCRM-Campaign-archive-scaled.webp)

### **Use this shortcode in a page/post to list past campaigns** [\#](https://fluentcrm.com/docs/advanced-features-settings\#use-this-shortcode-in-a-pagepost-to-list-past-campaigns)

Use this Shortcode into a Page/Post where you want to show your archived emails. You will see the results on your desired web page or you can preview them to see the result.

![campaign archives](https://fluentcrm.com/wp-content/uploads/2023/03/Campaign-Archives.webp)

Now, **paste** the **Shortcode** into a **Page/Post** where you want to show your archived emails. You will see the results on your desired web page or you can preview them to see the result.

![campaign archives shortcode in a page](https://fluentcrm.com/wp-content/uploads/2023/03/Campaign-Archives-Shortcode-in-a-Page.webp)

### **Advanced Campaign Archives with Shortcodes** [\#](https://fluentcrm.com/docs/advanced-features-settings\#advanced-campaign-archives-with-shortcodes)

For more granular control, you can use a powerful shortcode to display specific and multiple campaign archives. This method allows you to override the global settings on a case-by-case basis.

The shortcode format is as follows:

```
[[fluent_crm_campaign_archives ids="1101,5,1100" status="all" search="Summer" limit="10"]]
```

#### **Shortcode Parameters:** [\#](https://fluentcrm.com/docs/advanced-features-settings\#shortcode-parameters)

You can customize the archive display by using the following parameters within the shortcode:

- ids: (Optional) Specify the exact campaign IDs you want to display, separated by commas. If you use this parameter, only the campaigns with these IDs will be shown.
- status: (Optional) Filter the campaigns by their status. If this parameter is omitted, the status from your global settings will be used. Available statuses are:
  - all
  - draft
  - pending
  - archived
  - incomplete
  - purged
  - processing
  - pending-scheduled
  - scheduled
- search: (Optional) Display only the campaigns whose titles match a specific keyword.
- limit: (Optional) Set the maximum number of campaigns to display for this specific archive. The maximum limit is 50.

**Important Note:** If any of the parameters (ids, status, search, or limit) are not included in the shortcode, FluentCRM will automatically use the values you have configured in the global Campaign Archive settings. This allows for a flexible system where you can have a default archive and create custom ones as needed.

### Date & Time Format [\#](https://fluentcrm.com/docs/advanced-features-settings\#date--time-format)

This setting allows you to select the date and time format for the CRM plugin according to your needs. There are two formats for FluentCRM to view time in WordPress. These are:

1. **Date Time difference**: It will show your FluentCRM campaign, contact, and other times format like (EG: 1 hour ago)
2. **WordPress Default**: It will show the exact time of your FluentCRM activity. (EG: 5 January 2023, 14:15)

Once you select the desired date and time format, click the **Update Settings** button to save the changes you’ve made.

![date & time format](https://fluentcrm.com/wp-content/uploads/2023/03/Date-Time-Format.webp)

It will show up on your FluentCRM email campaign, contacts, and other places like this.

![preview of date & time format](https://fluentcrm.com/wp-content/uploads/2023/03/Preview-of-Date-Time-format-scaled.webp)

### Navigation [\#](https://fluentcrm.com/docs/advanced-features-settings\#navigation)

By enabling this option you will get a full Navigation for this CRM plugin in the left sidebar when you will click on the Fluent CRM from the WordPress Admin Panel.

Once you are done, click the **Update Settings** button to save the changes you’ve made.

![navigation](https://fluentcrm.com/wp-content/uploads/2023/03/Navigation.webp)

Here is the **Preview** of the **Navigation** Settings option.

![preview of navigation](https://fluentcrm.com/wp-content/uploads/2023/03/Preview-of-Navigation.webp)

### Company Module [\#](https://fluentcrm.com/docs/advanced-features-settings\#company-module)

Enabling the Company Module option allows you to add it to your **Contacts** section dropdown of the **Fluent CRM Navbar**. Also, fetch the company logo automatically by providing the website URL of the company.

> You can also enable the Company Module feature through the Addons section from the Fluent CRM Sidebar.
>
> To learn the process in detail, [click here](https://fluentcrm.com/docs/company-module/#activateenable-company-module).

Once you are done, click the **Update Settings** button to save the changes you’ve made.

![company module](https://fluentcrm.com/wp-content/uploads/2023/03/Company-Module.webp)

Here is the **Preview** of added **Company module** into the **Contacts** section dropdown and the **Company Logo** that is fetched automatically through the Website URL.

![preview of company module](https://fluentcrm.com/wp-content/uploads/2023/03/Preview-of-Company-Module-scaled.webp)

### Disable AI? [\#](https://fluentcrm.com/docs/advanced-features-settings\#disable-ai)

**Fluent CRM** has an **AI** **Prompts** feature inside the **Email Template** option for only **Image Generation**. You will find this option is already enabled which you can **Disable** anytime by clicking the checkbox.

Once you are done, click the **Update Settings** button to save the changes you’ve made.

![disable ai](https://fluentcrm.com/wp-content/uploads/2023/03/Disable-AI.webp)

Here is the **Preview** of the Image generating AI option which you can disable by clicking the **Disable AI** checkbox.

![preview of disable ai](https://fluentcrm.com/wp-content/uploads/2023/03/Preview-of-Disable-AI-scaled.webp)

### Multi-Threading Email Sending? [\#](https://fluentcrm.com/docs/advanced-features-settings\#multithreading-email-sending)

This setting option allows you to send the emails in a different process which will also make the sending speed around 2X.

To use this feature, ensure your server meets the requirements mentioned in the screenshot for optimal performance.

Once you are done, click the **Update Settings** button to save the changes you’ve made.

![multi threading email sending](https://fluentcrm.com/wp-content/uploads/2023/03/Multi-threading-email-sending.webp)

### System Log [\#](https://fluentcrm.com/docs/advanced-features-settings\#system-log)

Enable this option, if you want to add the System Log in your left sidebar under Settings. This System Logs are useful for debugging purposes.

Once you are done, click the **Update Settings** button to save the changes you’ve made.

![system log](https://fluentcrm.com/wp-content/uploads/2023/03/System-Log.webp)

Here is the **Preview** of the **System Logs** settings option.

![preview of system logs](https://fluentcrm.com/wp-content/uploads/2023/03/Preview-of-System-logs.webp)

If you have any further questions, concerns, or suggestions, please do not hesitate to contact our [@support team](https://wpmanageninja.com/support-tickets/?utm_source=wpmn&utm_medium=home&utm_campaign=site#/). Thank you.

##### What are your Feelings

#### Share This Article :

- [![Facebook](https://fluentcrm.com/wp-content/plugins/betterdocs/assets/images/social/facebook.svg?v=4.3.7)](https://www.facebook.com/sharer/sharer.php?u=https://fluentcrm.com/docs/advanced-features-settings/)
- [![X](https://fluentcrm.com/wp-content/plugins/betterdocs/assets/images/social/twitter.svg?v=4.3.7)](https://twitter.com/intent/tweet?url=https://fluentcrm.com/docs/advanced-features-settings/)
- [![LinkedIn](https://fluentcrm.com/wp-content/plugins/betterdocs/assets/images/social/linkedin.svg?v=4.3.7)](https://www.linkedin.com/shareArticle?mini=true&url=https://fluentcrm.com/docs/advanced-features-settings/)
- [![Pinterest](https://fluentcrm.com/wp-content/plugins/betterdocs/assets/images/social/pinterest.svg?v=4.3.7)](https://pinterest.com/pin/create/button/?url=https://fluentcrm.com/docs/advanced-features-settings/)

[Still stuck? How can we help?](https://fluentcrm.com/docs/advanced-features-settings#betterdocs-form-modal)

## How can we help?

Name: \*

Email: \*

Message: \*

Updated on June 19, 2025

[SMTP/Email & Bounce Handlers](https://fluentcrm.com/docs/smtp-bounce-handlers-settings/) [FluentCRM Global Settings](https://fluentcrm.com/docs/fluentcrm-global-settings/)

## 2 Comments

1. Hi there. Will archived email campaigns send if it is part of an automation?



I sent a campaign to current users, but want the same email to be triggered for future users. However, after the campaign is completed it is set to archive status. Can an archived email campaign be triggered to send?





[Reply](https://fluentcrm.com/docs/advanced-features-settings/?replytocom=4770#respond)

1. Yes, archived campaigns can be sent if you’ve set it to automate.





      [Reply](https://fluentcrm.com/docs/advanced-features-settings/?replytocom=4783#respond)

### Leave a Reply [Cancel reply](https://fluentcrm.com/docs/advanced-features-settings/\#respond)

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

Updates

First Name

Last Name

Email Address

Get the Free Blueprint

Sign Up for Our Newsletter

Mobile Blog Update Feed

Newsletter

SUBSCRIBE