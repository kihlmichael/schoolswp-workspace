[Skip to content](https://fluentcrm.com/docs/wp-fluent-forms-integration-with-fluentcrm#main)

Special [20% Discount](https://fluentcrm.com/deal/?utm_source=fcrmsite&utm_medium=banner&utm_campaign=special26&utm_id=special+deal) on Email Automation

[Start Automation](https://fluentcrm.com/deal/?utm_source=fcrmsite&utm_medium=banner&utm_campaign=special26&utm_id=special+deal)

All CategoriesGetting StartedGlobal SettingsFluentCRM EssentialsContactsEmailsFormsAutomationsEvent TrackingReportsPlugins Integration & AutomationMigrating from Other PlatformsBounce HandlersMiscellaneousDeveloper DocumentationFrequently Asked QuestionsChange Log

Popular Searchautomationtheunsubscribewebhookcustom

View Categories

4 min read

Table of Contents

- [Feed integration Settings for FluentCRM](https://fluentcrm.com/docs/wp-fluent-forms-integration-with-fluentcrm#feed-integration-settings-for-fluentcrm%C2%A0)
- [Integration Feed for FluentCRM in Forms](https://fluentcrm.com/docs/wp-fluent-forms-integration-with-fluentcrm#integration-feed-for-fluentcrm-in-forms)
  - [Configure FluentCRM Integration Feed](https://fluentcrm.com/docs/wp-fluent-forms-integration-with-fluentcrm#configure-fluentcrm-integration-feed)
- [Automation Triggers for Fluent Forms](https://fluentcrm.com/docs/wp-fluent-forms-integration-with-fluentcrm#automation-triggers-for-fluent-forms)
  - [Available Automation Triggers](https://fluentcrm.com/docs/wp-fluent-forms-integration-with-fluentcrm#available-automation-triggers)
    - [Subscription Canceled](https://fluentcrm.com/docs/wp-fluent-forms-integration-with-fluentcrm#subscription-canceled)
    - [Subscription Payment Received](https://fluentcrm.com/docs/wp-fluent-forms-integration-with-fluentcrm#subscription-payment-received)
    - [New Form Submission](https://fluentcrm.com/docs/wp-fluent-forms-integration-with-fluentcrm#new-form-submission)
- [FluentForm Subscriptions Widget in Contact Profile](https://fluentcrm.com/docs/wp-fluent-forms-integration-with-fluentcrm#fluentform-subscriptions-widget-in-contact-profile)

Fluent Forms integrates with FluentCRM to help you collect leads and gather valuable information about your prospects. The integration feed in Fluent Forms captures data from form submissions, and you’ll also have access to automation triggers that are based on user activities within the forms.

In this article, you’ll learn how to integrate FluentCRM with Fluent Forms and how it works.

> No additional settings are required to integrate FluentCRM with Fluent Forms. Simply install and activate both plugins on your site.

## **Feed integration Settings for FluentCRM** [\#](https://fluentcrm.com/docs/wp-fluent-forms-integration-with-fluentcrm\#feed-integration-settings-for-fluentcrm%C2%A0)

First, go to **Integrations** in the Fluent Forms navbar and search for **FluentCRM**. You’ll see the FluentCRM integration module simply toggle it to enable the FluentCRM module, which will activate the Feed Integration for FluentCRM in your forms.

![fluentfroms integation with fluentcrm 1](https://fluentcrm.com/wp-content/uploads/2021/02/FluentFroms-Integation-with-FluentCRM-1.png)

## **Integration Feed for FluentCRM in Forms** [\#](https://fluentcrm.com/docs/wp-fluent-forms-integration-with-fluentcrm\#integration-feed-for-fluentcrm-in-forms)

Go to **Forms** from the Fluent Forms navbar, and select the form you want to integrate with your FluentCRM.

If you do not have any existing forms, read [Create a Form from Scratch](https://fluentforms.com/wp-admin/post.php?post=45036&action=edit) or [Create a Form using Templates](https://fluentforms.com/wp-admin/post.php?post=45127&action=edit) documentation to create a new one.

Now go to the Forms **Settings and Integration** tab from the top menu bar and select **Configure Integration** from the left sidebar. After that, you will see the **Add New Integration** button click on it here you will see the **FluentCRM Integration Feed** in the dropdown menu.

![fluentfroms integation with fluentcrm 2](https://fluentcrm.com/wp-content/uploads/2021/02/FluentFroms-Integation-with-FluentCRM-2.png)

### Configure FluentCRM Integration Feed [\#](https://fluentcrm.com/docs/wp-fluent-forms-integration-with-fluentcrm\#configure-fluentcrm-integration-feed)

**A. Feed Name**: Here you need to enter a name for your FluentCRM integration feed.

**B. FluentCRM List:** Select the FluentCRM contact list you wish to integrate with. You can also change this anytime if needed.

**C. Primary Fields:** Use all the fields under this option to properly link your **FluentCRM** fields with the **Form Fields**. You can easily select the value for the form fields based on the **FluentCRM** fields using the **Shortcode**.

**D. Other fields:** You can map additional fields to Fluent Forms fields. To add multiple fields **Plus (+) Icon**.

**E. Contact Tag:** Hereselect one or multiple FluentCRM tags for the contact from your FluentCRM Contact tags.

**Enable Dynamic Tag Selection:** To apply tags based on submission values, enable dynamic tags by checking the **Enable Dynamic Tag Selection** option.

**Skip contact already exists in FluentCRM:** If you want to prevent duplicate contact in FluentCRM then check the checkboxes of **skip contact already exist in FluentCRM**.

**Skip name update if existing contact has old data:** If you want to retain existing contact names even if new data is submitted then check the checkboxes of **skip name update if existing contact have old data (per primary)** options.

**Enable Double Opt-In for a new Contact:** Enable this option to send a double opt-in email for new contacts.

**Enable Force subscribe if contact is not in subscribed status:** Here check the checkboxes to enable this to subscribe existing contacts that are not already subscribed.

**F. Conditional logic:** If you want to allow FluentCRM integration conditionally based on your submission values then **Enable Conditional Logic** options. To know more about this conditional logic read the [article](https://wpmanageninja.com/docs/fluent-form/advanced-features-functionalities-in-wp-fluent-form/conditional-logic-fluent-form/).

**G. Run Only on Events:** You will get this option only in the Subscription form. You’ll find three conditions here. If you want this integration feed to run only when one of these events occurs, select the event to trigger the feed accordingly. The available conditions are:

- **On Subscription Active**
- **On Subscription Cancel**
- **On Payment Refund**

**H. Remove Contact Tags:** If you want to remove a contact’s tags in FluentCRM, select the desired tags from the dropdown list.

**I. Status:** Enable this feed option to activate the integration.

After configuring the integration, Click the **Save Feed** button to finalize your FluentCRM integration.

![fluentfroms integation with fluentcrm 3](https://fluentcrm.com/wp-content/uploads/2021/02/FluentFroms-Integation-with-FluentCRM-3.png)

## **Automation Triggers for Fluent Forms** [\#](https://fluentcrm.com/docs/wp-fluent-forms-integration-with-fluentcrm\#automation-triggers-for-fluent-forms)

FluentCRM offers automation triggers for Fluent Forms, allowing you to automate actions based on user interactions. When you create a new automation in FluentCRM, you’ll find three automation triggers for Fluent Forms.

Go to **FluentCRM** and create a new automation. Select an **Automation Trigger** from the available Fluent Forms options then click the **Continue** button and build your automation funnel as needed.

If you want to know more about how to create an automation, check out our [documentation](https://fluentcrm.com/docs/automation-editor/) for detailed steps

### **Available Automation Triggers** [\#](https://fluentcrm.com/docs/wp-fluent-forms-integration-with-fluentcrm\#available-automation-triggers)

- **Subscription Canceled** This automation starts when a user cancels their subscription. It only applies to users who subscribed via Fluent Forms, and the cancellation must be done from the frontend by the user. If an admin cancels the subscription, this trigger won’t run.
- **Subscription Payment Received** This automation triggers when a user makes a subscription-based payment through Fluent Forms.
- **New Form Submission** This automation runs when a new form submission occurs.

![fluentfroms integation with fluentcrm 4](https://fluentcrm.com/wp-content/uploads/2021/02/FluentFroms-Integation-with-FluentCRM-4.png)

#### **Subscription Canceled** [\#](https://fluentcrm.com/docs/wp-fluent-forms-integration-with-fluentcrm\#subscription-canceled)

After selecting the **Subscription Canceled** automation trigger, a pop-up will appear where you need to provide some necessary details.

Next, choose the **Subscription Status** after this trigger action.

You can also specify if this automation should run for specific forms. To do this, select the desired forms from the **Target Forms** dropdown menu.

![fluentfroms integation with fluentcrm 5](https://fluentcrm.com/wp-content/uploads/2021/02/FluentFroms-Integation-with-FluentCRM-5.png)

#### **Subscription Payment Received** [\#](https://fluentcrm.com/docs/wp-fluent-forms-integration-with-fluentcrm\#subscription-payment-received)

After selecting the **Subscription Payment Received** automation trigger, a pop-up will appear where you need to enter the required details.

First, choose a form from the **Select Your Form** dropdown if you want this automation to run for a specific form.

Next, map your data to collect information from the form for automation.

Select the **Subscription Status** after this trigger action.

![fluentfroms integation with fluentcrm 6](https://fluentcrm.com/wp-content/uploads/2021/02/FluentFroms-Integation-with-FluentCRM-6.png)

#### **New Form Submission** [\#](https://fluentcrm.com/docs/wp-fluent-forms-integration-with-fluentcrm\#new-form-submission)

After selecting the **New From Submission** automation trigger, a pop-up will appear where you need to provide some necessary details.

Now choose a form from the **Select Your Form** dropdown if you want this automation to run for a specific form then map your data to collect information from the form for automation. Select the **Subscription Status** after this trigger action.

![fluentfroms integation with fluentcrm 7](https://fluentcrm.com/wp-content/uploads/2021/02/FluentFroms-Integation-with-FluentCRM-7.png)

## **FluentForm Subscriptions Widget in Contact Profile** [\#](https://fluentcrm.com/docs/wp-fluent-forms-integration-with-fluentcrm\#fluentform-subscriptions-widget-in-contact-profile)

A widget will appear in the FluentCRM contact’s profile for users who have subscribed via Fluent Forms.

![fluent forms subscriptions](https://fluentcrm.com/wp-content/uploads/2025/02/Screenshot-2025-02-11-at-12.51.55%E2%80%AFPM.webp)

If you have any further queries regarding this article please do not hesitate to contact our [@support team](https://wpmanageninja.com/support-tickets/?utm_source=wpmn&utm_medium=home&utm_campaign=site#/).

##### What are your Feelings

#### Share This Article :

- [![Facebook](https://fluentcrm.com/wp-content/plugins/betterdocs/assets/images/social/facebook.svg?v=4.3.7)](https://www.facebook.com/sharer/sharer.php?u=https://fluentcrm.com/docs/wp-fluent-forms-integration-with-fluentcrm/)
- [![X](https://fluentcrm.com/wp-content/plugins/betterdocs/assets/images/social/twitter.svg?v=4.3.7)](https://twitter.com/intent/tweet?url=https://fluentcrm.com/docs/wp-fluent-forms-integration-with-fluentcrm/)
- [![LinkedIn](https://fluentcrm.com/wp-content/plugins/betterdocs/assets/images/social/linkedin.svg?v=4.3.7)](https://www.linkedin.com/shareArticle?mini=true&url=https://fluentcrm.com/docs/wp-fluent-forms-integration-with-fluentcrm/)
- [![Pinterest](https://fluentcrm.com/wp-content/plugins/betterdocs/assets/images/social/pinterest.svg?v=4.3.7)](https://pinterest.com/pin/create/button/?url=https://fluentcrm.com/docs/wp-fluent-forms-integration-with-fluentcrm/)

[Still stuck? How can we help?](https://fluentcrm.com/docs/wp-fluent-forms-integration-with-fluentcrm#betterdocs-form-modal)

## How can we help?

Name: \*

Email: \*

Message: \*

Updated on February 25, 2025

[FluentAffiliate Integration with FluentCRM](https://fluentcrm.com/docs/fluentaffiliate-integration-with-fluentcrm/) [FluentCommunity integration with FluentCRM](https://fluentcrm.com/docs/fluentcommunity-integration-with-fluentcrm/)

## 5 Comments

1. how to update contact fields in fluent CRM from a form. I want to add the city of each contact from a Fluent form poll.





[Reply](https://fluentcrm.com/docs/wp-fluent-forms-integration-with-fluentcrm/?replytocom=5049#respond)

2. how update contact fields in fluent crm from a form?





[Reply](https://fluentcrm.com/docs/wp-fluent-forms-integration-with-fluentcrm/?replytocom=5048#respond)

3. what about how to move all the data from the other fields in fluent forms such as “check box, drop down, multiple choice, radio field etc”?





[Reply](https://fluentcrm.com/docs/wp-fluent-forms-integration-with-fluentcrm/?replytocom=2985#respond)

4. I may be making this more complex than it is, but I am wondering why do I need to get this complex?



\> All I want to do is create a form to collect a lead and send them a link to a download.



1\. I am looking at using FluentForms to create a form that pops up when the visitor clicks on a web link.


2\. Then FluentCRM to collect the name, email address, and tag it as a recipient of the offer.


3\. Then send a link to the given email address, which allows the user to download a free file.



THAT’s ALL!



But what I am reading – I need to get “Uncanny Automator” – Which REQUIRES that I create a USER ACCOUNT before I can do any of this.



Why? I DO NOT want to force the user to create a password for something this simple.



Is there simple way to do this?



Thanks,


Richard..





[Reply](https://fluentcrm.com/docs/wp-fluent-forms-integration-with-fluentcrm/?replytocom=2929#respond)

5. FluentCRM seems an awesome Tool, cant wait to test it for our B2B Hygiene Shop campaigns!





[Reply](https://fluentcrm.com/docs/wp-fluent-forms-integration-with-fluentcrm/?replytocom=2904#respond)


### Leave a Reply [Cancel reply](https://fluentcrm.com/docs/wp-fluent-forms-integration-with-fluentcrm/\#respond)

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

Newsletter

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

Newsletter

SUBSCRIBE