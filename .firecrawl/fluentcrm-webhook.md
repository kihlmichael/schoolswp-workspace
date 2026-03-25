[Skip to content](https://fluentcrm.com/docs/webhook-integration/#main)

Special [20% Discount](https://fluentcrm.com/deal/?utm_source=fcrmsite&utm_medium=banner&utm_campaign=special26&utm_id=special+deal) on Email Automation

[Start Automation](https://fluentcrm.com/deal/?utm_source=fcrmsite&utm_medium=banner&utm_campaign=special26&utm_id=special+deal)

All CategoriesGetting StartedGlobal SettingsFluentCRM EssentialsContactsEmailsFormsAutomationsEvent TrackingReportsPlugins Integration & AutomationMigrating from Other PlatformsBounce HandlersMiscellaneousDeveloper DocumentationFrequently Asked QuestionsChange Log

Popular Searchautomationtheunsubscribewebhookcustom

View Categories

2 min read

Table of Contents

- [Incoming webhook](https://fluentcrm.com/docs/webhook-integration/#incoming-webhook)
  - [Additional Data](https://fluentcrm.com/docs/webhook-integration/#additional-data)
  - [Example POST request in postman](https://fluentcrm.com/docs/webhook-integration/#example-post-request-in-postman)
- [Outgoing Webhook](https://fluentcrm.com/docs/webhook-integration/#outgoing-webhook)

Webhooks let you send or receive data from any third-party service without writing code or running servers. FluentCRM comes with both incoming and outgoing webhooks.

### Incoming webhook [\#](https://fluentcrm.com/docs/webhook-integration/\#incoming-webhook)

Incoming webhooks let you collect contacts automatically from an external platform or server. To create an incoming webhook, go to **Settings**, select WebHook Settings from the left sidebar, and click on **Create Webhook.**

![](https://fluentcrm.com/wp-content/uploads/2021/04/Webhook-Settings-1024x583.png)

A pop up will appear and you will need to provide the required details. Give the Hook a name at first, Choose lists and tags (optional) for the user who will subscribe through the webhook, and finally give a subscription status to the user. Mostly you want to give the Subscribed status.

![](https://fluentcrm.com/wp-content/uploads/2020/12/Screenshot-2020-12-01-at-11.22.01-AM-1024x879.png)

#### Additional Data [\#](https://fluentcrm.com/docs/webhook-integration/\#additional-data)

In your webhook source send a post request to the generated URL. Send the data as key pair formdata or JSON object. You can specify the tags, lists, and status in the webhook source and that will overwrite the defined value in the feed

| Title | Data Key | Data Type |
| --- | --- | --- |
| Tags | tags | array ex: \[1,2,3\] |
| Lists | lists | array ex: \[5,6,7\] |
| Subscription Status | status | string ex: subscribed \| pending \| unsubscribed |

#### Example POST request in postman [\#](https://fluentcrm.com/docs/webhook-integration/\#example-post-request-in-postman)

Here is the example post request via postman

![](https://fluentcrm.com/wp-content/uploads/2020/12/Screenshot-2020-12-01-at-11.31.31-AM-1024x695.png)

* * *

### Outgoing Webhook [\#](https://fluentcrm.com/docs/webhook-integration/\#outgoing-webhook)

Outgoing webhooks let you send your subscriber data within the automation to external servers and platforms. To send data to external servers and platforms, go to **Automations**, create or open an automation funnel, and click the plus(+) button to see available actions. Then select **Outgoing Webhooks** from the available **Actions**.

![](https://fluentcrm.com/wp-content/uploads/2021/07/image-31-1024x700.png)

Next, select your **Data Send Method**, you can choose both **Get** and Post methods. Provide your **Webhook URL** and Select **Request Format**(you can do both **JSON** and **Form**).

Choose what data you want to send(you can send **Full Subscriber Data** or **Custom Data**) and select whether you want to **Request Header** or not.

![](https://fluentcrm.com/wp-content/uploads/2021/07/image-14-1024x767.png)

If you have a lot of tasks running, you may want to enable the option to **Send Webhook Data as Background Process** as well. Click **Save Settings** once you’re done!

##### What are your Feelings

#### Share This Article :

- [![Facebook](https://fluentcrm.com/wp-content/plugins/betterdocs/assets/images/social/facebook.svg?v=4.3.7)](https://www.facebook.com/sharer/sharer.php?u=https://fluentcrm.com/docs/webhook-integration/)
- [![X](https://fluentcrm.com/wp-content/plugins/betterdocs/assets/images/social/twitter.svg?v=4.3.7)](https://twitter.com/intent/tweet?url=https://fluentcrm.com/docs/webhook-integration/)
- [![LinkedIn](https://fluentcrm.com/wp-content/plugins/betterdocs/assets/images/social/linkedin.svg?v=4.3.7)](https://www.linkedin.com/shareArticle?mini=true&url=https://fluentcrm.com/docs/webhook-integration/)
- [![Pinterest](https://fluentcrm.com/wp-content/plugins/betterdocs/assets/images/social/pinterest.svg?v=4.3.7)](https://pinterest.com/pin/create/button/?url=https://fluentcrm.com/docs/webhook-integration/)

[Still stuck? How can we help?](https://fluentcrm.com/docs/webhook-integration/#betterdocs-form-modal)

## How can we help?

Name: \*

Email: \*

Message: \*

Updated on July 19, 2021

[BuddyBoss integration with FluentCRM](https://fluentcrm.com/docs/buddyboss-integration-with-fluentcrm/) [Zapier Integration with FluentCRM](https://fluentcrm.com/docs/zapier-integration-with-fluentcrm/)

## 29 Comments

1. How do we add tags based on logic?





[Reply](https://fluentcrm.com/docs/webhook-integration/comment-page-2/?replytocom=5757#respond)

1. Hi Matthew, not sure what you mean. Webhooks can pass the data and you can set which tag to add to the contact. If you mean adding tags based on if/else logic, you’ll need some custom development.





      [Reply](https://fluentcrm.com/docs/webhook-integration/comment-page-2/?replytocom=5792#respond)
2. This article needs updating – where are the tags in the outgoing webhook? how come the doc doesn’t show examples of the outgoing webhook JSON body it sends? If i select Custom Data for outgoing webhook – i cannot seem to find the TAGS available to send… any good CRM worth their salt will allow me to send a copy of the tags to an outgoing webhook. Please extend this documentation, and enhance the functionality of the outgoing webhook module to send tags, and list name information in both the full subscriber data and the custom data setup.





[Reply](https://fluentcrm.com/docs/webhook-integration/comment-page-2/?replytocom=5689#respond)

1. Hi Dan, we will be updating the doc shortly. Thanks for commenting. 🙂





      [Reply](https://fluentcrm.com/docs/webhook-integration/comment-page-2/?replytocom=5749#respond)
3. How to receive a webhook from manychat?





[Reply](https://fluentcrm.com/docs/webhook-integration/comment-page-2/?replytocom=4787#respond)

4. How can i see the response log of the webhook, so i can debug?



And how can i send a JSON with nest values?



Like:


{


keyA: valueA,


keyB:{


keyB1: valueB1,


keyB2: valueB2


}


}





[Reply](https://fluentcrm.com/docs/webhook-integration/comment-page-2/?replytocom=4736#respond)

5. heloo


How can I send multi-line text via outgoing webhook?





[Reply](https://fluentcrm.com/docs/webhook-integration/comment-page-2/?replytocom=4418#respond)

6. hello


i want send multi text field in outgoing webhook. but can sent single text line in outgoing webhook.


please help me.





[Reply](https://fluentcrm.com/docs/webhook-integration/comment-page-2/?replytocom=4378#respond)

7. Hi,


I want to send webhook that will add or update a contact tags. I’m using “Add a contact” in integration but it only adds new user. If the user is in my email list, it does nothing. This is the message: “Duplicate email: [Justtal91@gmai.com](mailto:Justtal91@gmai.com), please use different email address.”


how can make it update a user?





[Reply](https://fluentcrm.com/docs/webhook-integration/comment-page-2/?replytocom=3674#respond)

1. Hi Shanie, I’m not sure why it won’t update tags. Could you please submit a support ticket?





      [Reply](https://fluentcrm.com/docs/webhook-integration/comment-page-2/?replytocom=3731#respond)

      1. Nazir, I have a similar issue, trying to update birthdate.





         [Reply](https://fluentcrm.com/docs/webhook-integration/comment-page-2/?replytocom=4746#respond)

         1. Please submit a support ticket.





            [Reply](https://fluentcrm.com/docs/webhook-integration/comment-page-2/?replytocom=4748#respond)
8. Hi Fluent,



How can I trigger an email campaign to be resent? It’s fine if it doesn’t work with this interface and I have to call a PHP function through code, just tell me where I can find it in your codebase.



Thanks!


Kevin





[Reply](https://fluentcrm.com/docs/webhook-integration/comment-page-2/?replytocom=3293#respond)

9. Hi,


How to use FluentCRM webhook for jet engine form?


Kindly guide me





[Reply](https://fluentcrm.com/docs/webhook-integration/comment-page-2/?replytocom=3193#respond)


### Leave a Reply [Cancel reply](https://fluentcrm.com/docs/webhook-integration/\#respond)

Your email address will not be published.Required fields are marked \*

Comment \*

Name \*

Email \*

Save my name, email, and website in this browser for the next time I comment.

[![fluentcrm logo tagline color white](https://fluentcrm.com/wp-content/uploads/2023/07/fluentCRM-logo-tagline-color_white.svg)](https://fluentcrm.com/)

FluentCRM is a marketing automation plugin for WordPress. Our vision is to make email marketing affordable for small businesses

Subscribe to Our Newsletter

Footer Form

Notify

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

Newsletter

First Name

Last Name

Email Address

Get the Free Blueprint

Sign Up for Our Newsletter

Mobile Blog Update Feed

Subscribe

SUBSCRIBE