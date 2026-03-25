[Skip to content](https://fluentcrm.com/docs/global-email-settings#main)

Special [20% Discount](https://fluentcrm.com/deal/?utm_source=fcrmsite&utm_medium=banner&utm_campaign=special26&utm_id=special+deal) on Email Automation

[Start Automation](https://fluentcrm.com/deal/?utm_source=fcrmsite&utm_medium=banner&utm_campaign=special26&utm_id=special+deal)

All CategoriesGetting StartedGlobal SettingsFluentCRM EssentialsContactsEmailsFormsAutomationsEvent TrackingReportsPlugins Integration & AutomationMigrating from Other PlatformsBounce HandlersMiscellaneousDeveloper DocumentationFrequently Asked QuestionsChange Log

Popular Searchautomationtheunsubscribewebhookcustom

View Categories

5 min read

Table of Contents

- [Default Settings](https://fluentcrm.com/docs/global-email-settings#default-settings)
- [Email Footer Settings](https://fluentcrm.com/docs/global-email-settings#email-footer-settings)
  - [Available SmartCodes:](https://fluentcrm.com/docs/global-email-settings#available-smartcodes)
    - [Contact](https://fluentcrm.com/docs/global-email-settings#contact)
    - [Custom Fields](https://fluentcrm.com/docs/global-email-settings#custom-fields)
    - [General](https://fluentcrm.com/docs/global-email-settings#general)
- [Email Preference Settings](https://fluentcrm.com/docs/global-email-settings#email-preference-settings)
  - [List Subscriptions](https://fluentcrm.com/docs/global-email-settings#list-subscriptions)
  - [Email Preference Shortcode](https://fluentcrm.com/docs/global-email-settings#email-preference-shortcode)
    - [Adding on a Page](https://fluentcrm.com/docs/global-email-settings#adding-on-a-page)
    - [Adding on a Fluent Forms Notification](https://fluentcrm.com/docs/global-email-settings#adding-on-a-fluent-forms-notification)

The Email Settings define the default Mail From email address and Names that will be visible to the recipients of the Fluent CRM communication emails sent. Available options are discussed below:

## Default Settings [\#](https://fluentcrm.com/docs/global-email-settings\#default-settings)

![crm email settings default](https://fluentcrm.com/wp-content/uploads/2022/07/crm_email_settings_default.png)

|     |     |
| --- | --- |
| **Option Name** | **Description** |
| **From Name** | The Name that is visible to the recipient as Sender Name. When you send marketing emails to your subscribers, the “From Name” (also known as the email Sender name) tells the recipients who sent them the email. It is very important and a determining factor for the email you will send whether your email will be opened, or get ignored by the recipients. Often it is the company name, or perhaps the product name or service name people have signed up to learn about. |
| **From Email Address** | The Name that is visible to the recipient is Sender’s Email Address. This is limited to the number of available configured connections in SMTP Plugins if installed like FluentSMTP. This is the email address the user will see when they open the email. There are a number of things to follow when choosing the “From Email” address. Always avoid using free webmail addresses, and also avoid the no-reply address. Use a valid email address that also matches your SMTP email address or this will cause an email delivery issue. |
| **Reply to Name** | The Name that identifies the Name of the entity that will receive the reply to the sent email. |
| **Reply to Email** | The email that will receive the reply of the sent email. |
| **Maximum Email Limit Per Second** | The maximum number of emails attempted per second. It can be lower due to a lot of factors like site performance, security or firewall limits, rules, the number of connections allowed from the remote mail server that delivers the emails, or by default WordPress hosting if no SMTP plugin is installed and configured. |

The above settings will only apply if there is no SMTP Plugin installed and uses the default mailing system. If an SMTP plugin is installed like FluentSMTP and that does not force the Sender Name and Email Address as below then the above settings will be in effect.

![crm smtp email default settings](https://fluentcrm.com/wp-content/uploads/2022/07/crm_smtp_email_default_settings.png)

But if you have any SMTP plugin installed on your website which takes over the email delivery of the website then you will be able to select your configured email addresses or connections or delivery method from **From Email Address** option as below:

![crm email settings dropdwon address](https://fluentcrm.com/wp-content/uploads/2022/07/crm_email_settings_dropdwon_address.png)

Below is an example of the **From Name** and **From Email Address** shown in Gmail Web Client.

![crm email defaults preview](https://fluentcrm.com/wp-content/uploads/2022/07/crm_email_defaults_preview.png)**An example email sent from FluentCRM to show you how the From Name & From Email will show in the inbox.**

## Email Footer Settings [\#](https://fluentcrm.com/docs/global-email-settings\#email-footer-settings)

![crm business settings email footer](https://fluentcrm.com/wp-content/uploads/2022/07/crm_business_settings_email_footer.png)

**Email Footer Text**: The footer section usually contains information about the sender’s unsubscribe link or forward the email. You should provide your business address {{crm.business\_address}} and manage the subscription/unsubscribe URL for the best user experience.

**Smartcode in Footer:** {{crm.business\_name}}, {{crm.business\_address}}, ##crm.manage\_subscription\_url##, ##crm.unsubscribe\_url## will be replaced with dynamic values. It is recommended to keep the texts as default aligned. Your provided email design template will align the texts.

### **Available SmartCodes:** [\#](https://fluentcrm.com/docs/global-email-settings\#available-smartcodes)

#### Contact [\#](https://fluentcrm.com/docs/global-email-settings\#contact)

![crm email settigns smartcodes contact](https://fluentcrm.com/wp-content/uploads/2022/07/crm_email_settigns_SmartCodes_contact.png)

|     |     |
| --- | --- |
| **Data Field Name** | **Smart Code** |
| Full Name | {{contact.full\_name}} |
| Name Prefix | {{contact.prefix}} |
| First Name | {{contact.first\_name}} |
| Last Name | {{contact.last\_name}} |
| Contact Email | {{contact.email}} |
| Contact ID | {{contact.id}} |
| User ID | {{contact.user\_id}} |
| Address Line 1 | {{contact.address\_line\_1}} |
| Address Line 2 | {{contact.address\_line\_2}} |
| City | {{contact.city}} |
| State | {{contact.state}} |
| Postal Code | {{contact.postal\_code}} |
| Country | {{contact.country}} |
| Phone | {{contact.phone}} |
| Status | {{contact.status}} |
| Date of Birth | {{contact.date\_of\_birth}} |

#### Custom Fields [\#](https://fluentcrm.com/docs/global-email-settings\#custom-fields)

![crm email settigns smartcodes customfields](https://fluentcrm.com/wp-content/uploads/2022/07/crm_email_settigns_SmartCodes_customFields.png)

Custom Fields are dependent on the FLuentCRM Settings. You can add as many Custom Fields as you want and then they will be available here. The generic **Data Field Name** will be as you set in the **Label** while creation and **SmartCode** will recognize the **slug** value of the custom field as below:

![custom fields fluentcrm datetime 1](https://fluentcrm.com/wp-content/uploads/2022/07/Custom-Fields-FluentCRM__DateTime-1.png)

The above example screenshot will represent **Data Field Name** as “ **Date and Time**” & **SmartCode** would be **{{contact.custom.date\_time}}**

#### General [\#](https://fluentcrm.com/docs/global-email-settings\#general)

![crm email settigns smartcodes general](https://fluentcrm.com/wp-content/uploads/2022/07/crm_email_settigns_SmartCodes_general.png)

|     |     |
| --- | --- |
| **Data Field Name** | **Smart Code** |
| Business Name | {{crm.business\_name}} |
| Business Address | {{crm.business\_address}} |
| Admin Email | {{wp.admin\_email}} |
| Site URL | {{wp.url}} |
| Dynamic Date <br>(example: +2Days from Now) | {{other.date.+2 days}} |
| Unsubscribe URL | ##crm.unsubscribe\_url## |
| Manage Subscription URL | ##crm.manage\_subscription\_url## |
| View on Browser URL | ##web\_preview\_url## |
| Unsubscribe | {{crm.unsubscribe\_html\|Unsubscribe}} |
| Manage Subscription <br>Hyperlink HTML | {{crm.manage\_subscription\_html\|Manage Preference}} |

## Email Preference Settings [\#](https://fluentcrm.com/docs/global-email-settings\#email-preference-settings)

Using The **##crm.manage\_subscription\_url##** SmartCode lets the user manage their subscriptions along with the Lists if defined in **Email Preference Settings**.

![crm email settings manage subscriptions email](https://fluentcrm.com/wp-content/uploads/2022/07/crm_email_settings_manage_subscriptions_email.png)

Below is an example email of using this SmartCode where the user will see a link saying **Manage Email Subscriptions** and this will take the user to a page similar to the below screenshot.

![crm email settings manage subscriptions](https://fluentcrm.com/wp-content/uploads/2022/07/crm_email_settings_manage_subscriptions.png)

The screenshot below represents the available options of the preferences:

![crm settings email preference](https://fluentcrm.com/wp-content/uploads/2022/08/crm_settings_email_preference.png)

### List Subscriptions [\#](https://fluentcrm.com/docs/global-email-settings\#list-subscriptions)

|     |     |
| --- | --- |
| **Option Name** | **Description** |
| **No, Contact can not manage list subscriptions** | Default Option. This will not let the user manage their list subscription or do not offer any lists to select. |
| **Contact only see and manage the following list of subscriptions** | This will allow admins to select specific lists for users to manage their list subscriptions. It can be all lists or a number of lists. |
| **Contact can see all lists and manage subscriptions** | This will allow the user to see all the lists and select any or all of the list’s subscriptions. |

### Email Preference Shortcode [\#](https://fluentcrm.com/docs/global-email-settings\#email-preference-shortcode)

Please use the shortcode  to show the form for your subscribers to let them manage these options themselves:

1. Name Prefix
2. First Name
3. Last Name
4. Phone
5. Date of Birth
6. Address Field
7. Lists that they are allowed to manage their subscription.

The above shortcode renders the management form on a page as below screenshot:

![crm email preference page](https://fluentcrm.com/wp-content/uploads/2022/08/crm_email_preference_Page.png)

#### Adding on a Page [\#](https://fluentcrm.com/docs/global-email-settings\#adding-on-a-page)

![crm email preference page add](https://fluentcrm.com/wp-content/uploads/2022/08/crm_email_preference_Page_Add.png)

#### Adding on a Fluent Forms Notification [\#](https://fluentcrm.com/docs/global-email-settings\#adding-on-a-fluent-forms-notification)

This can also be used in a Fluent Forms Form Submission Notification as below:

![crm form confirmation email preference](https://fluentcrm.com/wp-content/uploads/2022/08/crm_form_confirmation_email_preference.png)

##### What are your Feelings

#### Share This Article :

- [![Facebook](https://fluentcrm.com/wp-content/plugins/betterdocs/assets/images/social/facebook.svg?v=4.3.7)](https://www.facebook.com/sharer/sharer.php?u=https://fluentcrm.com/docs/global-email-settings/)
- [![X](https://fluentcrm.com/wp-content/plugins/betterdocs/assets/images/social/twitter.svg?v=4.3.7)](https://twitter.com/intent/tweet?url=https://fluentcrm.com/docs/global-email-settings/)
- [![LinkedIn](https://fluentcrm.com/wp-content/plugins/betterdocs/assets/images/social/linkedin.svg?v=4.3.7)](https://www.linkedin.com/shareArticle?mini=true&url=https://fluentcrm.com/docs/global-email-settings/)
- [![Pinterest](https://fluentcrm.com/wp-content/plugins/betterdocs/assets/images/social/pinterest.svg?v=4.3.7)](https://pinterest.com/pin/create/button/?url=https://fluentcrm.com/docs/global-email-settings/)

[Still stuck? How can we help?](https://fluentcrm.com/docs/global-email-settings#betterdocs-form-modal)

## How can we help?

Name: \*

Email: \*

Message: \*

Updated on December 21, 2023

[Business Settings](https://fluentcrm.com/docs/global-business-settings/) [General Settings](https://fluentcrm.com/docs/global-general-settings/)

## 20 Comments

1. I am not able to send a “single” manual email to any of my contacts from the crm. There is no email button. All my automated emails are working and smtp is set up. test emails work. but can not send a manual email. The envelope at the bottom of the contact page in the crm does nothing when I click on it.





[Reply](https://fluentcrm.com/docs/global-email-settings/comment-page-2/?replytocom=5769#respond)

1. Hi Joe, Looks like a site specific issue. Please contact support.





      [Reply](https://fluentcrm.com/docs/global-email-settings/comment-page-2/?replytocom=5791#respond)

### Leave a Reply [Cancel reply](https://fluentcrm.com/docs/global-email-settings/\#respond)

Your email address will not be published.Required fields are marked \*

Comment \*

Name \*

Email \*

Save my name, email, and website in this browser for the next time I comment.

[![fluentcrm logo tagline color white](https://fluentcrm.com/wp-content/uploads/2023/07/fluentCRM-logo-tagline-color_white.svg)](https://fluentcrm.com/)

FluentCRM is a marketing automation plugin for WordPress. Our vision is to make email marketing affordable for small businesses

Subscribe to Our Newsletter

Footer Form

Contact

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

Notify

Please Enter Your Email Address to Download FluentCRM (Free)

By downloading FluentCRM, I agree to have this website save my email address for further communication.

DOWNLOAD

Forget Opens, Build Relationships

The Email

Marketing Blueprint

The average campaign gets 39% opens and $0.11 per subscriber. **_Top WordPress founders and influencers consistently pull 54%+ opens and $30K+ campaigns._** This guide shows you exactly how they do it, so you can, too!

Email Marketing Blueprint

Subscribe

First Name

Last Name

Email Address

Get the Free Blueprint

Sign Up for Our Newsletter

Mobile Blog Update Feed

Notify

SUBSCRIBE