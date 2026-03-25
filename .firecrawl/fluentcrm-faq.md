[Skip to content](https://fluentcrm.com/docs/frequently-asked-questions/#main)

Special [20% Discount](https://fluentcrm.com/deal/?utm_source=fcrmsite&utm_medium=banner&utm_campaign=special26&utm_id=special+deal) on Email Automation

[Start Automation](https://fluentcrm.com/deal/?utm_source=fcrmsite&utm_medium=banner&utm_campaign=special26&utm_id=special+deal)

All CategoriesGetting StartedGlobal SettingsFluentCRM EssentialsContactsEmailsFormsAutomationsEvent TrackingReportsPlugins Integration & AutomationMigrating from Other PlatformsBounce HandlersMiscellaneousDeveloper DocumentationFrequently Asked QuestionsChange Log

Popular Searchautomationtheunsubscribewebhookcustom

View Categories

3 min read

Table of Contents

- [My scheduled email/email sequence isn't being sent correctly, what should I do?](https://fluentcrm.com/docs/frequently-asked-questions/#my-scheduled-email-email-sequence-isn-t-being-sent-correctly-what-should-i-do)
- [Both FluentCRM and Fluent Forms have double opt-in, which one should I use?](https://fluentcrm.com/docs/frequently-asked-questions/#both-fluentcrm-and-fluent-forms-have-double-opt-in-which-one-should-i-use)
- [How can I store data in Custom Fields I've created in FluentCRM?](https://fluentcrm.com/docs/frequently-asked-questions/#both-fluentcrm-and-fluent-forms-have-double-opt-in-which-one-should-i-use)
- [Email Templates: Can I set alternate text in case there isn't a value for the dynamic tags I'm using?](https://fluentcrm.com/docs/frequently-asked-questions/#email-templates-can-i-set-alternate-text-in-case-there-isn-t-a-value-for-dynamic-tags-i-m-using)
- [How can I connect other WordPress form plugins with FluentCRM?](https://fluentcrm.com/docs/frequently-asked-questions/#how-can-i-connect-other-wordpress-form-plugins-with-fluentcrm)
- [Where can I get FluentCRM Tutorials?](https://fluentcrm.com/docs/frequently-asked-questions/#where-can-i-get-fluentcrm-tutorials)

**FluentCRM** is the **Email Marketing & CRM solution** for WordPress with loads of features and functionality. In order to help you make the most of this tool, we tried to cover as much as possible in our regular documentation. However, if you still have questions, this FAQ page is the perfect place to get your question answered.

## My scheduled email/email sequence isn’t being sent correctly, what should I do? [\#](https://fluentcrm.com/docs/frequently-asked-questions/\#my-scheduled-email-email-sequence-isn-t-being-sent-correctly-what-should-i-do)

The most common case we found for a few reported issues is CRON is not running for some reason(Go to **FluentCRM>Settings>Tools** and see when is the last time your CRON has been run.). This happens because WordPress CRON is quite unreliable. Check out [this doc](https://fluentcrm.com/docs/replace-wordpress-cron-with-a-real-cron-job/) to replace WordPress CRON with a real CRON job.

## Both FluentCRM and Fluent Forms have double opt-in, which one should I use? [\#](https://fluentcrm.com/docs/frequently-asked-questions/\#both-fluentcrm-and-fluent-forms-have-double-opt-in-which-one-should-i-use)

Double opt-in emails are a way to acquire ‘consent of subscription’ from users to send them emails. If you enable the double opt-in feature, both FluentCRM and Fluent Forms will require the user’s consent before they can process the data.

In order to effectively set up double opt-in with FluentCRM, you should leave the **Enable Double Opt-in Confirmation before Form Data Processing** option( **Form>Form Settings**) unchecked within Fluent Forms. This will ensure that your contact will receive the double opt-in email you’ve set up within FluentCRM. If you enable double opt-in in both Fluent Forms and FluentCRM, your system will send the double opt-in email twice, one from Fluent Forms and another from FluentCRM.

## How can I store data in Custom Fields I’ve created in FluentCRM? [\#](https://fluentcrm.com/docs/frequently-asked-questions/\#both-fluentcrm-and-fluent-forms-have-double-opt-in-which-one-should-i-use)

Once you’ve created custom fields, you’ll need to map the field data. For example, if you want to map Fluent Forms data inside FluentCRM, you need to go to **Form Settings** \> **FluentCRM Integration** and map the data fields. Alternatively, you can also map the data from the Automations.

![fluent forms custom fields mapping](https://fluentcrm.com/wp-content/uploads/2021/06/Screenshot-2024-08-12-at-10.25.31%E2%80%AFAM-1024x793.webp)

## Email Templates: Can I set alternate text in case there isn’t a value for the dynamic tags I’m using? [\#](https://fluentcrm.com/docs/frequently-asked-questions/\#email-templates-can-i-set-alternate-text-in-case-there-isn-t-a-value-for-dynamic-tags-i-m-using)

Yes, you can set alternate text for [merge codes](https://fluentcrm.com/docs/merge-codes-smart-codes-usage/) within email templates. In case there isn’t a value available for your dynamic tag, FluentCRM will automatically replace it with the alternate text you’ve provided.

Suppose you’re using a dynamic tag to pull off the contact’s name within your email template. In that case, the dynamic tag will be: **{{contact.first\_name}}**

In order to add an alternate text, simply add a pipe “ **\|**” symbol after the dynamic tag string and add your alternate text. For example, if you want to replace the contact’s name with “ **there**“, add the text after adding a pipe symbol **{{contact.first\_name\|there}}**. In case the contact’s first name isn’t available in the system, FluentCRM will replace the first name with “ **there**“.

This also works within double opt-in emails, subject lines and anywhere you can use a dynamic tag. So you can always use dynamic tags with confidence and replace them with alternate text if the value isn’t available.

## How can I connect other WordPress form plugins with FluentCRM? [\#](https://fluentcrm.com/docs/frequently-asked-questions/\#how-can-i-connect-other-wordpress-form-plugins-with-fluentcrm)

FluentCRM supports incoming webhooks. So if your form supports sending webhooks, you can integrate any form plugin with FluentCRM.

\* **Tutorial:** [How to Connect Any WordPress Forms with FluentCRM](https://fluentcrm.com/connect-wp-forms-ninja-forms-gravity-forms-or-any-forms-with-fluentcrm/)

## Where can I get FluentCRM Tutorials? [\#](https://fluentcrm.com/docs/frequently-asked-questions/\#where-can-i-get-fluentcrm-tutorials)

We regularly publish tutorials on [our blog](https://fluentcrm.com/category/tutorials/) and [Youtube channel](https://www.youtube.com/channel/UCiyeXfnGx9e06hXWf0Hz7ow). You can also follow us on [Twitter](https://twitter.com/fluentcrm?lang=en) or join our [Facebook group](https://www.facebook.com/groups/fluentcrm/).

##### What are your Feelings

#### Share This Article :

- [![Facebook](https://fluentcrm.com/wp-content/plugins/betterdocs/assets/images/social/facebook.svg?v=4.3.7)](https://www.facebook.com/sharer/sharer.php?u=https://fluentcrm.com/docs/frequently-asked-questions/)
- [![X](https://fluentcrm.com/wp-content/plugins/betterdocs/assets/images/social/twitter.svg?v=4.3.7)](https://twitter.com/intent/tweet?url=https://fluentcrm.com/docs/frequently-asked-questions/)
- [![LinkedIn](https://fluentcrm.com/wp-content/plugins/betterdocs/assets/images/social/linkedin.svg?v=4.3.7)](https://www.linkedin.com/shareArticle?mini=true&url=https://fluentcrm.com/docs/frequently-asked-questions/)
- [![Pinterest](https://fluentcrm.com/wp-content/plugins/betterdocs/assets/images/social/pinterest.svg?v=4.3.7)](https://pinterest.com/pin/create/button/?url=https://fluentcrm.com/docs/frequently-asked-questions/)

[Still stuck? How can we help?](https://fluentcrm.com/docs/frequently-asked-questions/#betterdocs-form-modal)

## How can we help?

Name: \*

Email: \*

Message: \*

Updated on August 12, 2024

[General Questions](https://fluentcrm.com/docs/frequently-asked-questions/) [General Questions](https://fluentcrm.com/docs/frequently-asked-questions/)

## 8 Comments

1. hello, I want to add the statistics and the tables they are shown to the interface on my website. How can I do that?





[Reply](https://fluentcrm.com/docs/frequently-asked-questions/?replytocom=4842#respond)

2. It seem contact’s birthday not query user although i already input correct Birth of date field in contact





[Reply](https://fluentcrm.com/docs/frequently-asked-questions/?replytocom=4691#respond)

3. Désolé mais je ne trouve pas les prix





[Reply](https://fluentcrm.com/docs/frequently-asked-questions/?replytocom=4398#respond)

4. Hi,


I migrate my website and now I get an 500 Internal Server Error. Unfortunately, I migrated first and then deactivated the license in my dashboard on your site. How can I reactivate FluentCRM pro? I guess I need to delete something in the mysql database?


Thanks and best regards,


Heiner





[Reply](https://fluentcrm.com/docs/frequently-asked-questions/?replytocom=1910#respond)

1. Hi Heiner, Just deactivate the license from your WPManageNinja account dashboard. I think that’ll do.





      [Reply](https://fluentcrm.com/docs/frequently-asked-questions/?replytocom=1914#respond)
5. Hello, how can I resend emails to those emails that didn’t open the mail I’ve send?





[Reply](https://fluentcrm.com/docs/frequently-asked-questions/?replytocom=1548#respond)

1. Hi David, We are developing a one-click resend functionality that’ll allow for sending such emails. For now, you can do this as a workaround on email campaign management.



      1\. Create a temporary tag.


      2\. Create an automation that triggers with that tag.


      3\. Open an archived campaign that you want to resend.


      4\. Select condition(didn’t open the email) and apply the temporary tag.





      [Reply](https://fluentcrm.com/docs/frequently-asked-questions/?replytocom=1549#respond)

      1. Is this live yet? If so, where? And if not, when?



         Will this apply to emails that live inside an Automation as well?





         [Reply](https://fluentcrm.com/docs/frequently-asked-questions/?replytocom=4703#respond)

### Leave a Reply [Cancel reply](https://fluentcrm.com/docs/frequently-asked-questions/\#respond)

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

Subscribe

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

Updates

SUBSCRIBE