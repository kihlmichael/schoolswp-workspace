[Skip to content](https://fluentcrm.com/docs/smtp-bounce-handlers-settings/#main)

Special [20% Discount](https://fluentcrm.com/deal/?utm_source=fcrmsite&utm_medium=banner&utm_campaign=special26&utm_id=special+deal) on Email Automation

[Start Automation](https://fluentcrm.com/deal/?utm_source=fcrmsite&utm_medium=banner&utm_campaign=special26&utm_id=special+deal)

All CategoriesGetting StartedGlobal SettingsFluentCRM EssentialsContactsEmailsFormsAutomationsEvent TrackingReportsPlugins Integration & AutomationMigrating from Other PlatformsBounce HandlersMiscellaneousDeveloper DocumentationFrequently Asked QuestionsChange Log

Popular Searchautomationtheunsubscribewebhookcustom

View Categories

1 min read

Table of Contents

- [FluentSMTP Settings](https://fluentcrm.com/docs/smtp-bounce-handlers-settings/#fluent-smtp-settings)
- [Bounce Handlers](https://fluentcrm.com/docs/smtp-bounce-handlers-settings/#bounce-handlers)

FluentCRM uses the wp\_mail() function to broadcast all the emails that are PHP-based mailers. There are various ways to deliver emails from WordPress. The SMTP Protocol, API-based 3rd party delivery providers, and direct PHP-based sending require SMTP Port 25 to be opened from the WordPress hosting server. Below is a screenshot of when no SMTP plugins are used on the website.

![crm smtp initial](https://fluentcrm.com/wp-content/uploads/2022/07/crm_smtp_initial.png)

SMTP Plugins like **FluentSMTP** improves your WordPress mail by intercepting the wp\_mail and then connecting with your email service providers to ensure deliverability. It allows sending emails directly via SMTP. API-based providers like Google Workplace, Office365, Sendgrid, AWS SES, etc. When you install the FluentSMTP plugin on your website and configure email delivery connections you will see them listed in the FluentCRM SMTP Dashboard like the below screenshot.

## FluentSMTP Settings [\#](https://fluentcrm.com/docs/smtp-bounce-handlers-settings/\#fluent-smtp-settings)

![crm smtp](https://fluentcrm.com/wp-content/uploads/2022/07/crm_smtp.png)

## Bounce Handlers [\#](https://fluentcrm.com/docs/smtp-bounce-handlers-settings/\#bounce-handlers)

Bounce handlers allow you to manage bounced contacts without manual intervention. Generally, all your bounced emails are only reported within the service platform you’re using however, the ideal way to deal with bounced emails is to sync them with FluentCRM. This is why we recommend setting up bounce handlers.

To configure Bounce Handlers for available services please check each relevant documentation:

01. [Amazon SES](https://fluentcrm.com/docs/bounce-handler-with-amazon-ses/)
02. [Mailgun](https://fluentcrm.com/docs/bounce-handling-with-mailgun/)
03. [SendGrid](https://fluentcrm.com/docs/bounce-handling-with-sendgrid/)
04. [Pepipost](https://fluentcrm.com/docs/bounce-handling-with-pepipost/)
05. [PostMark](https://fluentcrm.com/docs/bounce-handling-with-postmark/)
06. [Sparkpost](https://fluentcrm.com/docs/bounce-handling-with-sparkpost/)
07. [SendGrid](https://fluentcrm.com/docs/bounce-handling-with-sendgrid/)
08. [Elastic Email](https://fluentcrm.com/docs/bounce-handling-with-elastic-email/)
09. [Postal Server](https://fluentcrm.com/docs/bounce-handling-with-postal-server/)
10. [SMTP2Go](https://fluentcrm.com/docs/bounce-handling-with-smtp2go/)
11. [Brevo (ex Sendinblue)](https://fluentcrm.com/docs/bounce-handling-with-brevo/)

For now, we only have these services integrated with our bounce handling system. More will be added in the future.

##### What are your Feelings

#### Share This Article :

- [![Facebook](https://fluentcrm.com/wp-content/plugins/betterdocs/assets/images/social/facebook.svg?v=4.3.7)](https://www.facebook.com/sharer/sharer.php?u=https://fluentcrm.com/docs/smtp-bounce-handlers-settings/)
- [![X](https://fluentcrm.com/wp-content/plugins/betterdocs/assets/images/social/twitter.svg?v=4.3.7)](https://twitter.com/intent/tweet?url=https://fluentcrm.com/docs/smtp-bounce-handlers-settings/)
- [![LinkedIn](https://fluentcrm.com/wp-content/plugins/betterdocs/assets/images/social/linkedin.svg?v=4.3.7)](https://www.linkedin.com/shareArticle?mini=true&url=https://fluentcrm.com/docs/smtp-bounce-handlers-settings/)
- [![Pinterest](https://fluentcrm.com/wp-content/plugins/betterdocs/assets/images/social/pinterest.svg?v=4.3.7)](https://pinterest.com/pin/create/button/?url=https://fluentcrm.com/docs/smtp-bounce-handlers-settings/)

[Still stuck? How can we help?](https://fluentcrm.com/docs/smtp-bounce-handlers-settings/#betterdocs-form-modal)

## How can we help?

Name: \*

Email: \*

Message: \*

Updated on February 17, 2025

[Compliance](https://fluentcrm.com/docs/global-compliance-settings/) [Advanced Features Settings](https://fluentcrm.com/docs/advanced-features-settings/)

## 19 Comments

1. I am using my own server SMTP, how are bounced emails handled like this? I don’t see an option for my own server’s smtp.





[Reply](https://fluentcrm.com/docs/smtp-bounce-handlers-settings/?replytocom=5625#respond)

1. Hi Tom, bounce handling is only available for specific services. But I think you can figure something out with our support if you really need it. [https://wpmanageninja.com/support-tickets/](https://wpmanageninja.com/support-tickets/)





      [Reply](https://fluentcrm.com/docs/smtp-bounce-handlers-settings/?replytocom=5678#respond)
2. I’m using WP Mail SMTP plugin. When I go to the FluentCRM SMTP Settings I’m prompted to install the FluentSMTP Plugin. Can I use my own SMTP service?





[Reply](https://fluentcrm.com/docs/smtp-bounce-handlers-settings/?replytocom=5571#respond)

1. Sure you can. FluentCRM SMTP Settings is only required for bounce handling, all you do is choose your email in the email settings to use any other SMTP.





      [Reply](https://fluentcrm.com/docs/smtp-bounce-handlers-settings/?replytocom=5677#respond)
3. I use FluentSMTP. Why do I need these other services for Bounce Handers? I configured Google Workspace to access my emails. I wish there was more information on this page. I’m not a program or designer so I’m figuring this stuff out.





[Reply](https://fluentcrm.com/docs/smtp-bounce-handlers-settings/?replytocom=5449#respond)

1. Hi Michael, Google Workspace doesn’t require bounce handlers. We’ll be updating this URL shortly. 🙂





      [Reply](https://fluentcrm.com/docs/smtp-bounce-handlers-settings/?replytocom=5508#respond)
4. I currently use SMTP2Go as my smtp plugin, will fluentcrm work with this??





[Reply](https://fluentcrm.com/docs/smtp-bounce-handlers-settings/?replytocom=5327#respond)

1. Yes, FluentCRM can blend with any other SMTP plugin. However, I suggest using FluentSMTP as it’s our **Fluent Ecosystem** product and you will get some extra benefits. Moreover, **FluentSMTP is a completely Free plugin** and it will stay as free for forever.





      [Reply](https://fluentcrm.com/docs/smtp-bounce-handlers-settings/?replytocom=5335#respond)

      1. But FluentSMTP still needs to be connected with a sending service. Right? Amazon SES for example is a sending service. But it’s very complex to set up. So I’d prefer to use SMTP2GO as a sending service instead. Why then should I still use FluentSMTP if SMTP2GO has its own plugin?





         [Reply](https://fluentcrm.com/docs/smtp-bounce-handlers-settings/?replytocom=5517#respond)

         1. Hi Marc, Didn’t test out SMTP2GO yet. Does it have all the features of FluentSMTP? Like Multiple connections, fallbacks, failure alerts, etc. ? Looks like Tanzil was referring to those as they enhance the user experience significantly. However, if you already have SMTP2GO, it’s wiser to stick with it unless you need some other features. 🙂





            [Reply](https://fluentcrm.com/docs/smtp-bounce-handlers-settings/?replytocom=5530#respond)
5. Will there be an integration for bounce handling with Mailjet?





[Reply](https://fluentcrm.com/docs/smtp-bounce-handlers-settings/?replytocom=5222#respond)

1. Hi Ben, Mailjet integration isn’t available yet. We may develop these SMTP connections in the future.





      [Reply](https://fluentcrm.com/docs/smtp-bounce-handlers-settings/?replytocom=5236#respond)
6. Hello, we presently use Mandrill and would welcome an integration to allow use to setup bounce handlers.





[Reply](https://fluentcrm.com/docs/smtp-bounce-handlers-settings/?replytocom=5129#respond)

1. I believe we have very few Mandrill users at this moment. If there is enough request, we’ll be integrating with Mandrill. 🙂





      [Reply](https://fluentcrm.com/docs/smtp-bounce-handlers-settings/?replytocom=5138#respond)
7. How do I setup Bounce emails for FluentSMTP when I am not use one of the listed services for Bounce? I do not see a generic SMTP for Bounce. We are currently using TurboSMTP.





[Reply](https://fluentcrm.com/docs/smtp-bounce-handlers-settings/?replytocom=5059#respond)

1. Hi Ivan, you can only setup bounce handlers for the SMTP providers we fully support. However, I’m taking this as a feature request so if we integrate with TurboSMTP, you will be able to handle bounce notifications.





      [Reply](https://fluentcrm.com/docs/smtp-bounce-handlers-settings/?replytocom=5063#respond)
8. I have SMTP on my site, do not need all those services, why there is no setup for that? it seems confusing that you have so beautiful product and when I get to this point, I get stuck.





[Reply](https://fluentcrm.com/docs/smtp-bounce-handlers-settings/?replytocom=5016#respond)

1. Hi Ben, Not sure where you’re stuck. FluentCRM will only show your configured email senders and we recommend that you setup bounce handlers to avoid spamming.





      [Reply](https://fluentcrm.com/docs/smtp-bounce-handlers-settings/?replytocom=5020#respond)
9. how to remove bounce handler? Currently have amazon ses, not using though.





[Reply](https://fluentcrm.com/docs/smtp-bounce-handlers-settings/?replytocom=4820#respond)


### Leave a Reply [Cancel reply](https://fluentcrm.com/docs/smtp-bounce-handlers-settings/\#respond)

Your email address will not be published.Required fields are marked \*

Comment \*

Name \*

Email \*

Save my name, email, and website in this browser for the next time I comment.

[![fluentcrm logo tagline color white](https://fluentcrm.com/wp-content/uploads/2023/07/fluentCRM-logo-tagline-color_white.svg)](https://fluentcrm.com/)

FluentCRM is a marketing automation plugin for WordPress. Our vision is to make email marketing affordable for small businesses

Subscribe to Our Newsletter

Footer Form

Updates

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

Notify

First Name

Last Name

Email Address

Get the Free Blueprint

Sign Up for Our Newsletter

Mobile Blog Update Feed

Notify

SUBSCRIBE