[Skip to content](https://fluentcrm.com/docs/contact-statuses#main)

Special [20% Discount](https://fluentcrm.com/deal/?utm_source=fcrmsite&utm_medium=banner&utm_campaign=special26&utm_id=special+deal) on Email Automation

[Start Automation](https://fluentcrm.com/deal/?utm_source=fcrmsite&utm_medium=banner&utm_campaign=special26&utm_id=special+deal)

All CategoriesGetting StartedGlobal SettingsFluentCRM EssentialsContactsEmailsFormsAutomationsEvent TrackingReportsPlugins Integration & AutomationMigrating from Other PlatformsBounce HandlersMiscellaneousDeveloper DocumentationFrequently Asked QuestionsChange Log

Popular Searchautomationtheunsubscribewebhookcustom

View Categories

3 min read

Table of Contents

- [Contact Statuses in FluentCRM](https://fluentcrm.com/docs/contact-statuses#contact-statuses-in-fluentcrm)
  - [Subscribed Contacts](https://fluentcrm.com/docs/contact-statuses#subscribed-contacts)
  - [Pending Contacts](https://fluentcrm.com/docs/contact-statuses#pending-contacts)
  - [Unsubscribed Contacts](https://fluentcrm.com/docs/contact-statuses#unsubscribed-contacts)
  - [Bounced Contacts](https://fluentcrm.com/docs/contact-statuses#bounced-contacts)
  - [Complained Contacts](https://fluentcrm.com/docs/contact-statuses#complained-contacts)
  - [Transactional Contacts](https://fluentcrm.com/docs/contact-statuses#transactional-contacts)
- [Best Practices for Managing Contact Statuses](https://fluentcrm.com/docs/contact-statuses#best-practices-for-managing-contact-statuses)

## Contact Statuses in FluentCRM [\#](https://fluentcrm.com/docs/contact-statuses\#contact-statuses-in-fluentcrm)

FluentCRM offers a robust system for managing contact statuses, allowing you to control and segment your audience effectively. Understanding these statuses is crucial for proper contact management, email marketing, and automation.

In FluentCRM, a contact can have one of the following six statuses:

1. Subscribed
2. Pending
3. Unsubscribed
4. Bounced
5. Complained
6. Transactional

Let’s delve into each status to understand its implications and use cases.

### Subscribed Contacts [\#](https://fluentcrm.com/docs/contact-statuses\#subscribed-contacts)

**Status: subscribed**

- These are your active and engaged contacts.
- Subscribed contacts have explicitly opted in to receive your communications or you directly added as subscribed.
- You can send all types of emails (promotional and transactional) to these contacts.
- All automation workflows can be run for subscribed contacts.

**Key Points:**

- Ideal for your main email marketing efforts.
- These contacts form the core of your active audience.

### Pending Contacts [\#](https://fluentcrm.com/docs/contact-statuses\#pending-contacts)

**Status: pending**

- Contacts in this status are awaiting confirmation of their subscription.
- Typically, these contacts have signed up through a double opt-in process but haven’t confirmed their subscription yet.
- You cannot send campaign or promotional emails to pending contacts.
- Automation can be run for pending contacts if you enable that in the automation configuration, mainly focused on getting them to confirm their subscription. Please note that no email from the automation will be sent but other actions will run.

**Key Points:**

- Used in double opt-in processes to ensure subscriber intent.
- These contacts need to confirm their subscription to move to ‘subscribed’ status.

### Unsubscribed Contacts [\#](https://fluentcrm.com/docs/contact-statuses\#unsubscribed-contacts)

**Status: unsubscribed**

- These contacts have opted out of your communications.
- A contact can become unsubscribed by:

1. Clicking an unsubscribe link in an email.
2. Being manually unsubscribed by an admin.

- You should not send promotional emails to unsubscribed contacts.
- Automation can be run for pending contacts if you enable that in the automation configuration, mainly focused on getting them to confirm their subscription. Please note that no email from the automation will be sent but other actions will run.

**Key Points:**

- Respect this status to maintain a good sender reputation and comply with email regulations.

### Bounced Contacts [\#](https://fluentcrm.com/docs/contact-statuses\#bounced-contacts)

**Status: bounced**

- This status is applied to contacts whose email addresses have resulted in hard bounces.
- FluentCRM can automatically mark contacts as bounced when integrated with certain email service providers if you configure the bounce handler with your email-sending service.
- No emails will be sent to these contacts from FluentCRM unless resubscribed.

**Key Points:**

- Regularly clean your list by removing or attempting to update bounced contacts.
- Set up proper bounce handling in your email service provider integration.

### Complained Contacts [\#](https://fluentcrm.com/docs/contact-statuses\#complained-contacts)

**Status: complained**

- Contacts who have marked your emails as spam receive this status.
- This status helps protect your sender’s reputation.
- Avoid sending further communications to these contacts.

**Key Points:**

- Take complaints seriously and review your email practices if you receive many complaints.
- Consider removing these contacts from your list entirely.

### Transactional Contacts [\#](https://fluentcrm.com/docs/contact-statuses\#transactional-contacts)

**Status: transactional**

- This status is for contacts who should receive only transactional emails.
- Campaign emails will not be sent but emails from automation will be sent.
- You can set this status manually from bulk action or automation trigger. This is the default status for the WooCommerce Abandon Cart Module in FluentCRM

## Best Practices for Managing Contact Statuses [\#](https://fluentcrm.com/docs/contact-statuses\#best-practices-for-managing-contact-statuses)

1. Regularly review and clean your contact list.
2. Set up proper integrations for automatic status updates (especially for bounces and complaints).
3. Respect unsubscribe requests promptly.
4. Use segmentation based on status for targeted and appropriate communication.
5. Implement a re-engagement strategy for unengaged subscribers before they unsubscribe.

By effectively managing these statuses, you can maintain a healthy email list, improve deliverability, and ensure compliance with email marketing best practices and regulations.

##### What are your Feelings

#### Share This Article :

- [![Facebook](https://fluentcrm.com/wp-content/plugins/betterdocs/assets/images/social/facebook.svg?v=4.3.7)](https://www.facebook.com/sharer/sharer.php?u=https://fluentcrm.com/docs/contact-statuses/)
- [![X](https://fluentcrm.com/wp-content/plugins/betterdocs/assets/images/social/twitter.svg?v=4.3.7)](https://twitter.com/intent/tweet?url=https://fluentcrm.com/docs/contact-statuses/)
- [![LinkedIn](https://fluentcrm.com/wp-content/plugins/betterdocs/assets/images/social/linkedin.svg?v=4.3.7)](https://www.linkedin.com/shareArticle?mini=true&url=https://fluentcrm.com/docs/contact-statuses/)
- [![Pinterest](https://fluentcrm.com/wp-content/plugins/betterdocs/assets/images/social/pinterest.svg?v=4.3.7)](https://pinterest.com/pin/create/button/?url=https://fluentcrm.com/docs/contact-statuses/)

[Still stuck? How can we help?](https://fluentcrm.com/docs/contact-statuses#betterdocs-form-modal)

## How can we help?

Name: \*

Email: \*

Message: \*

Updated on August 11, 2024

[Contact Overview](https://fluentcrm.com/docs/contact-overview/) [Integrated Contact Overview](https://fluentcrm.com/docs/additional-integrated-contact-overview/)

### Leave a Reply [Cancel reply](https://fluentcrm.com/docs/contact-statuses/\#respond)

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

Updates

First Name

Last Name

Email Address

Get the Free Blueprint

Sign Up for Our Newsletter

Mobile Blog Update Feed

Newsletter

SUBSCRIBE