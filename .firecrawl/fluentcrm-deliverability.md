[Skip to content](https://fluentcrm.com/docs/sending-emails-and-email-deliverability#main)

Special [20% Discount](https://fluentcrm.com/deal/?utm_source=fcrmsite&utm_medium=banner&utm_campaign=special26&utm_id=special+deal) on Email Automation

[Start Automation](https://fluentcrm.com/deal/?utm_source=fcrmsite&utm_medium=banner&utm_campaign=special26&utm_id=special+deal)

All CategoriesGetting StartedGlobal SettingsFluentCRM EssentialsContactsEmailsFormsAutomationsEvent TrackingReportsPlugins Integration & AutomationMigrating from Other PlatformsBounce HandlersMiscellaneousDeveloper DocumentationFrequently Asked QuestionsChange Log

Popular Searchautomationtheunsubscribewebhookcustom

View Categories

3 min read

Table of Contents

- [Configure an Email Delivery Service Provider](https://fluentcrm.com/docs/sending-emails-and-email-deliverability#configure-an-email-delivery-service-provider)
  - [FluentSMTP to Handle All Email Delivery](https://fluentcrm.com/docs/sending-emails-and-email-deliverability#fluentsmtp-to-handle-all-email-delivery)
  - [List of Configurable Delivery Providers](https://fluentcrm.com/docs/sending-emails-and-email-deliverability#list-of-delivery-providers)
  - [Example of Multiple Email Delivery Connections](https://fluentcrm.com/docs/sending-emails-and-email-deliverability#example-of-multiple-email-delivery-connections)
- [FluentCRM Email Processing](https://fluentcrm.com/docs/sending-emails-and-email-deliverability#fluentcrm-email-processing)
- [FluentCRM Email Scheduling](https://fluentcrm.com/docs/sending-emails-and-email-deliverability#fluentcrm-email-scheduling)
  - [Delay Emails in Automation](https://fluentcrm.com/docs/sending-emails-and-email-deliverability#delay-emails-in-automation)
- [Compare Cron Status](https://fluentcrm.com/docs/sending-emails-and-email-deliverability#compare-cron-status)

FluentCRM is an Email Marketing & Automation tool. It helps you launch Email Campaigns, Email sequences, and Email Automation to automate your marketing emails.

Using your hosting space for email isn’t a good idea. And using the hosting for sending PHP emails would most likely deplete the hosting resources. Thus, we suggest that you use a separate email service.

To learn more about various Email Delivery Providers and their overview, you may check out some of the blogs below:

## Configure an Email Delivery Service Provider [\#](https://fluentcrm.com/docs/sending-emails-and-email-deliverability\#configure-an-email-delivery-service-provider)

In order to use an email service, you need to use an SMTP plugin. There are plenty of SMTP plugins in the WordPress repository. But most of them offer slow email sending.

### FluentSMTP to Handle All Email Delivery [\#](https://fluentcrm.com/docs/sending-emails-and-email-deliverability\#fluentsmtp-to-handle-all-email-delivery)

That’s why we’ve created a free-for-lifetime SMTP plugin called FluentSMTP. In fact, it is the only SMTP plugin that allows multiple SMTP connections at the same time described here: **[Multiple SMTP Connections & Auto Routing](https://fluentsmtp.com/docs/using-multiple-smtp-drivers-with-fluent-smtp/).** This means, if you install FluentSMTP, you can use multiple email-sending services to cut down your email-sending costs. Some email services can be a bit costly. So if you have FluentSMTP, you can use the expensive email service for your marketing emails and the less expensive email service for not-so-important WordPress emails.

![fluent smtp wordpress](https://fluentcrm.com/wp-content/uploads/2023/01/fluent-smtp-wordpress.png)

For more about FluentSMTP, Configurations, and features please check the relevant documentation: [**Install and Activate FluentSMTP**](https://fluentsmtp.com/docs/installing-fluent-smtp/), [**Configurable Email Delivery Providers**](https://fluentsmtp.com/docs/configurable-email-delivery-providers/), and [**Introduction to FluentSMTP Dashboard**](https://fluentsmtp.com/docs/introduction-to-fluent-smtp-dashboard/)

Click the button to install FluentSMTP. Or, you can download and install FluentSMTP on your WordPress by clicking the button below:

[Download FluentSMTP](https://wordpress.org/plugins/fluent-smtp/)

### List of Configurable Delivery Providers [\#](https://fluentcrm.com/docs/sending-emails-and-email-deliverability\#list-of-delivery-providers)

There a lot of different Email Delivery Providers can be configured natively via API-based connection as listed below:

01. [Amazon SES API.](https://fluentsmtp.com/docs/set-up-amazon-ses-in-fluent-smtp/)
02. [Mailgun API.](https://fluentsmtp.com/docs/configure-mailgun-in-fluent-smtp-to-send-emails/)
03. [SendGrid API.](https://fluentsmtp.com/docs/set-up-the-sendgrid-driver-in-fluent-smtp/)
04. [Sendinblue API.](https://fluentsmtp.com/docs/setting-up-sendinblue-mailer-in-fluent-smtp/)
05. [SparkPost API.](https://fluentsmtp.com/docs/configure-sparkpost-in-fluent-smtp-to-send-emails/)
06. [Netcore API (formerly Pepipost).](https://fluentsmtp.com/docs/set-up-the-pepipost-mailer-in-fluent-smtp/)
07. [PostMark API.](https://fluentsmtp.com/docs/configure-postmark-in-fluent-smtp-to-send-emails/)
08. [Elastic Mail API.](https://fluentsmtp.com/docs/configure-elastic-email-in-fluent-smtp/)
09. [Gmail & Google Workspace OAuth API.](https://fluentsmtp.com/docs/connect-gmail-or-google-workspace-emails-with-fluentsmtp/)
10. [Outlook OAuth API.](https://fluentsmtp.com/docs/setup-outlook-with-fluentsmtp/)
11. [All Other SMTP.](https://fluentsmtp.com/docs/set-up-fluent-smtp-with-any-host-or-mailer/)

### Example of Multiple Email Delivery Connections [\#](https://fluentcrm.com/docs/sending-emails-and-email-deliverability\#example-of-multiple-email-delivery-connections)

Below is an example screenshot of multiple Email Delivery Connections based on various Delivery Providers:

![fluent smtp multiple connections](https://fluentcrm.com/wp-content/uploads/2023/01/fluent-smtp-multiple-connections.png)

## FluentCRM Email Processing [\#](https://fluentcrm.com/docs/sending-emails-and-email-deliverability\#fluentcrm-email-processing)

There are different places from where Emails can be sent such as **Test Emails** from [**Email Templates**](https://fluentcrm.com/docs/email-templates/), [**Email Campaigns**](https://fluentcrm.com/docs/setting-up-campaign/), [**Email Sequences**](https://fluentcrm.com/docs/email-sequence/), [**Automation Email Actions**](https://fluentcrm.com/docs/automation-email-actions/), [**Double Opt-in Settings**](https://fluentcrm.com/docs/global-double-opt-in-settings/), and [**Recurring Campaigns**](https://fluentcrm.com/docs/recurring-campaign/).

**Send the emails right now:** Once the scheduling is set to “right now,” the emails will begin processing. This process is a task where FluentCRM starts generating Emails against each subscriber with necessary headers and email content.

**Schedule the emails:** You can set specific dates and times for your email processing.

**Schedule emails within a specified date-time range:** Your emails will start processing between your specified time-date range.

![schedule the emails](https://fluentcrm.com/wp-content/uploads/2023/08/Schedule-the-emails.png)

The next step is to deliver the emails. It can be delivered through wp\_mail() directly or if you have a plugin like FluentSMTP. FluentSMTP takes emails from FluentCRM and then relays them to the Email Delivery Provider you configure in settings and used from FluentCRM.

Below is a screenshot of an Email campaign while sending a campaign. Please check the above links for specific features.

![flunetcrm email processing](https://fluentcrm.com/wp-content/uploads/2023/01/flunetcrm-email-processing.png)

## FluentCRM Email Scheduling [\#](https://fluentcrm.com/docs/sending-emails-and-email-deliverability\#fluentcrm-email-scheduling)

The emails can be scheduled or waited until a period of time from different places described below:

### Delay Emails in Automation [\#](https://fluentcrm.com/docs/sending-emails-and-email-deliverability\#delay-emails-in-automation)

Below is an example screenshot of Automation Emails waiting for 1 Day. For more about this please check: [**Wait X Days/Hours**](https://fluentcrm.com/docs/primary-automation-actions/#wait-x-days-hours)

![crm automation wait](https://fluentcrm.com/wp-content/uploads/2023/01/crm-automation-wait.png)

## Compare Cron Status [\#](https://fluentcrm.com/docs/sending-emails-and-email-deliverability\#compare-cron-status)

FluentCRM Cron Status runs 60 Seconds, 5 Minutes, and 60 Minutes Intervals.

That’s all about Email Sending from FluentCRM! Please read through our guidelines and documentation to learn in-depth knowledge about using and utilizing the features of FluentCRM.

##### What are your Feelings

#### Share This Article :

- [![Facebook](https://fluentcrm.com/wp-content/plugins/betterdocs/assets/images/social/facebook.svg?v=4.3.7)](https://www.facebook.com/sharer/sharer.php?u=https://fluentcrm.com/docs/sending-emails-and-email-deliverability/)
- [![X](https://fluentcrm.com/wp-content/plugins/betterdocs/assets/images/social/twitter.svg?v=4.3.7)](https://twitter.com/intent/tweet?url=https://fluentcrm.com/docs/sending-emails-and-email-deliverability/)
- [![LinkedIn](https://fluentcrm.com/wp-content/plugins/betterdocs/assets/images/social/linkedin.svg?v=4.3.7)](https://www.linkedin.com/shareArticle?mini=true&url=https://fluentcrm.com/docs/sending-emails-and-email-deliverability/)
- [![Pinterest](https://fluentcrm.com/wp-content/plugins/betterdocs/assets/images/social/pinterest.svg?v=4.3.7)](https://pinterest.com/pin/create/button/?url=https://fluentcrm.com/docs/sending-emails-and-email-deliverability/)

[Still stuck? How can we help?](https://fluentcrm.com/docs/sending-emails-and-email-deliverability#betterdocs-form-modal)

## How can we help?

Name: \*

Email: \*

Message: \*

Updated on December 21, 2023

[Cron Job: FluentCRM Cron with EasyCron](https://fluentcrm.com/docs/fluentcrm-cron-with-easycron/) [Troubleshoot: Guidelines on WordPress Error](https://fluentcrm.com/docs/troubleshoot-guidelines-on-wordpress-error/)

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

Updates

SUBSCRIBE