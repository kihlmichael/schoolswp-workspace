[Skip to content](https://fluentcrm.com/docs/global-double-opt-in-settings#main)

Special [20% Discount](https://fluentcrm.com/deal/?utm_source=fcrmsite&utm_medium=banner&utm_campaign=special26&utm_id=special+deal) on Email Automation

[Start Automation](https://fluentcrm.com/deal/?utm_source=fcrmsite&utm_medium=banner&utm_campaign=special26&utm_id=special+deal)

All CategoriesGetting StartedGlobal SettingsFluentCRM EssentialsContactsEmailsFormsAutomationsEvent TrackingReportsPlugins Integration & AutomationMigrating from Other PlatformsBounce HandlersMiscellaneousDeveloper DocumentationFrequently Asked QuestionsChange Log

Popular Searchautomationtheunsubscribewebhookcustom

View Categories

2 min read

Table of Contents

- [Email Subject & Body](https://fluentcrm.com/docs/global-double-opt-in-settings#email-subject-&-body)
- [Design Template](https://fluentcrm.com/docs/global-double-opt-in-settings#design-template)
- [After Confirmation Actions](https://fluentcrm.com/docs/global-double-opt-in-settings#after-confirmation-actions)
  - [Show Message](https://fluentcrm.com/docs/global-double-opt-in-settings#after-confirmation-actions)
  - [Redirect to an URL](https://fluentcrm.com/docs/global-double-opt-in-settings#after-confirmation-actions)

## Email Subject & Body [\#](https://fluentcrm.com/docs/global-double-opt-in-settings\#email-subject-&-body)

The double opt-in email feature of FluentCRM acts as an extra layer of confirmation to verify each email address is a verified user and FluentCRM can add the email address to your contact list. Contacts that are added via form submissions, automation funnels, or by selecting the WooCommmerce subscription checkbox will automatically receive a double opt-in email to confirm their subscription if this setting is enabled.

![crm double opt in email body](https://fluentcrm.com/wp-content/uploads/2022/07/crm_double_opt_in_email_body.png)

- **Email Subject:** Give an appropriate subject for the email to the recipient.
- **Email Body:** Write the email body for the double opt-in email. There will be a default one. You can customize it as you want. Use the SmartCode from the dropdown to create a customized one. But using the SmartCode **#activate\_link#** for a **Plain Text Email** or **{{crm.activate\_button\|Confirm Subscription}}** for **HTML Email** with a button to click for the subscription is mandatory because it contains the activation URL.

## Design Template [\#](https://fluentcrm.com/docs/global-double-opt-in-settings\#design-template)

Select the email Design Template for this double-opt-in email. You can choose from four different options.

![crm double opt in email body design template](https://fluentcrm.com/wp-content/uploads/2022/07/crm_double_opt_in_email_body_design_template.png)

## **After Confirmation Actions** [\#](https://fluentcrm.com/docs/global-double-opt-in-settings\#after-confirmation-actions)

### **Show Message** [\#](https://fluentcrm.com/docs/global-double-opt-in-settings\#after-confirmation-actions)

Select the confirmation message for the user. When they will click on the subscription confirmation button they will land on this page.

![crm double opt in after confirmation show message](https://fluentcrm.com/wp-content/uploads/2022/07/crm_double_opt_in_after_confirmation_show_message.png)

\* **Note:** If you’re using Fluent Forms, leave the **Enable Double Opt-in Confirmation before the Form Data Processing** option( **Form -> Form Settings**) unchecked to send the above double opt-in email template to your contacts. If you enable both Fluent Forms and FluentCRM double opt-in, your system will send the Fluent Forms double opt-in email template to your contacts.

### **Redirect to an URL** [\#](https://fluentcrm.com/docs/global-double-opt-in-settings\#after-confirmation-actions)

If you want to redirect your user to a specific URL then you can use this option to confirm the subscription and immediately automatically redirect to your desired URL, Landing Page, or anywhere you want.

![crm double opt in after confirmation redirect](https://fluentcrm.com/wp-content/uploads/2022/07/crm_double_opt_in_after_confirmation_redirect.png)

Below is an example screenshot of what the Double Opt-in Emails look like in the recipient’s mailbox.

![crm double opt in email](https://fluentcrm.com/wp-content/uploads/2022/07/crm_double_opt_in_email.png)

And when the user clicks on the **Subscription Confirmation Button** and you configure it to **show a message after confirmation** they will see a message like thebelow:

![crm double opt in confirmed](https://fluentcrm.com/wp-content/uploads/2022/07/crm_double_opt_in_confirmed.png)

That’s all for Double Opt-in Confirmation Email Settings!

##### What are your Feelings

#### Share This Article :

- [![Facebook](https://fluentcrm.com/wp-content/plugins/betterdocs/assets/images/social/facebook.svg?v=4.3.7)](https://www.facebook.com/sharer/sharer.php?u=https://fluentcrm.com/docs/global-double-opt-in-settings/)
- [![X](https://fluentcrm.com/wp-content/plugins/betterdocs/assets/images/social/twitter.svg?v=4.3.7)](https://twitter.com/intent/tweet?url=https://fluentcrm.com/docs/global-double-opt-in-settings/)
- [![LinkedIn](https://fluentcrm.com/wp-content/plugins/betterdocs/assets/images/social/linkedin.svg?v=4.3.7)](https://www.linkedin.com/shareArticle?mini=true&url=https://fluentcrm.com/docs/global-double-opt-in-settings/)
- [![Pinterest](https://fluentcrm.com/wp-content/plugins/betterdocs/assets/images/social/pinterest.svg?v=4.3.7)](https://pinterest.com/pin/create/button/?url=https://fluentcrm.com/docs/global-double-opt-in-settings/)

[Still stuck? How can we help?](https://fluentcrm.com/docs/global-double-opt-in-settings#betterdocs-form-modal)

## How can we help?

Name: \*

Email: \*

Message: \*

Updated on August 11, 2022

[Abandoned Cart Settings](https://fluentcrm.com/docs/abandoned-cart-settings/) [Incoming Webhooks](https://fluentcrm.com/docs/global-incoming-webhooks/)

## 32 Comments

1. Hello, I run my website in German and English. Therefore, I want to send an English newsletter to those who subscribe to my English form and a German newsletter to those who subscribe to my German form. Now there is only one Double Opt-In e-mail I can set up.


How can I have two different emails sent out for each case?



Many thanks!





[Reply](https://fluentcrm.com/docs/global-double-opt-in-settings/comment-page-2/?replytocom=5758#respond)

1. Hey Nino, you can setup list based double opt in now: [https://fluentcrm.com/fluentcrm-2-9-6/#listbased-double-optin](https://fluentcrm.com/fluentcrm-2-9-6/#listbased-double-optin)





      [Reply](https://fluentcrm.com/docs/global-double-opt-in-settings/comment-page-2/?replytocom=5793#respond)
2. Hi there. Is there a shortcode for the double opt in “subscription confirmed” page? It would be great if we could style that page having the ability to use s shortcode.





[Reply](https://fluentcrm.com/docs/global-double-opt-in-settings/comment-page-2/?replytocom=4956#respond)

1. Hi there, thank you for messaging. Here is the shortcode – \[fluentcrm\_pref\]. You can style your page based on your preference.





      [Reply](https://fluentcrm.com/docs/global-double-opt-in-settings/comment-page-2/?replytocom=4962#respond)

### Leave a Reply [Cancel reply](https://fluentcrm.com/docs/global-double-opt-in-settings/\#respond)

Your email address will not be published.Required fields are marked \*

Comment \*

Name \*

Email \*

Save my name, email, and website in this browser for the next time I comment.

[![fluentcrm logo tagline color white](https://fluentcrm.com/wp-content/uploads/2023/07/fluentCRM-logo-tagline-color_white.svg)](https://fluentcrm.com/)

FluentCRM is a marketing automation plugin for WordPress. Our vision is to make email marketing affordable for small businesses

Subscribe to Our Newsletter

Footer Form

Newsletter

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

Contact

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

Notify

SUBSCRIBE