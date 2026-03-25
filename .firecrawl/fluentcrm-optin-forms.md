[Skip to content](https://fluentcrm.com/docs/opt-in-forms-fluent-forms-basic-configuration#main)

Special [20% Discount](https://fluentcrm.com/deal/?utm_source=fcrmsite&utm_medium=banner&utm_campaign=special26&utm_id=special+deal) on Email Automation

[Start Automation](https://fluentcrm.com/deal/?utm_source=fcrmsite&utm_medium=banner&utm_campaign=special26&utm_id=special+deal)

All CategoriesGetting StartedGlobal SettingsFluentCRM EssentialsContactsEmailsFormsAutomationsEvent TrackingReportsPlugins Integration & AutomationMigrating from Other PlatformsBounce HandlersMiscellaneousDeveloper DocumentationFrequently Asked QuestionsChange Log

Popular Searchautomationtheunsubscribewebhookcustom

View Categories

5 min read

Table of Contents

- [Activating Fluent Forms](https://fluentcrm.com/docs/opt-in-forms-fluent-forms-basic-configuration#activating-fluent-forms)
- [Create Subscription Form](https://fluentcrm.com/docs/opt-in-forms-fluent-forms-basic-configuration#create-subscription-form)
  - [Templates](https://fluentcrm.com/docs/opt-in-forms-fluent-forms-basic-configuration#templates)
  - [Mapping List & Tags](https://fluentcrm.com/docs/opt-in-forms-fluent-forms-basic-configuration#mapping-list-tags)
- [Form Actions](https://fluentcrm.com/docs/opt-in-forms-fluent-forms-basic-configuration#form-actions)
  - [Preview](https://fluentcrm.com/docs/opt-in-forms-fluent-forms-basic-configuration#preview)
  - [Edit Form](https://fluentcrm.com/docs/opt-in-forms-fluent-forms-basic-configuration#edit-form)
  - [Edit Connection](https://fluentcrm.com/docs/opt-in-forms-fluent-forms-basic-configuration#edit-connection)
  - [Actions from Fluent Forms](https://fluentcrm.com/docs/opt-in-forms-fluent-forms-basic-configuration#actions-from-fluent-forms)
- [Form Submission](https://fluentcrm.com/docs/opt-in-forms-fluent-forms-basic-configuration#form-submission)
  - [Embedding Subscription Form](https://fluentcrm.com/docs/opt-in-forms-fluent-forms-basic-configuration#embedding-subscription-form)
  - [Entry in Fluent Forms](https://fluentcrm.com/docs/opt-in-forms-fluent-forms-basic-configuration#entry-in-fluent-forms)
    - [Feed Status](https://fluentcrm.com/docs/opt-in-forms-fluent-forms-basic-configuration#feed-status)
  - [Contact in FluentCRM](https://fluentcrm.com/docs/opt-in-forms-fluent-forms-basic-configuration#contact-in-fluentcrm)

You might wonder if it is possible to integrate with FluentCRM and manage those users and run automation, email campaigns, email sequences, etc. Below you will see 2 examples of subscription forms that can connect with FluentCRM.

Fluent Forms Integration with FluentCRM \| An Advanced Tutorial - YouTube

Tap to unmute

[Fluent Forms Integration with FluentCRM \| An Advanced Tutorial](https://www.youtube.com/watch?v=E_jbKCBsA6o) [WPManageNinja](https://www.youtube.com/channel/UCiyeXfnGx9e06hXWf0Hz7ow)

![thumbnail-image](https://yt3.ggpht.com/3_hd8hibVMrQj6Sd1A42V1hNV_-ENLWUn7AgO2DM0lInabqZRcbfIMt4U8_Kyv-owOaQ5DZQvWE=s68-c-k-c0x00ffffff-no-rj)

WPManageNinja11.8K subscribers

[Watch on](https://www.youtube.com/watch?v=E_jbKCBsA6o)

![crm form2](https://fluentcrm.com/wp-content/uploads/2020/09/crm_form2.png)

![crm form3](https://fluentcrm.com/wp-content/uploads/2020/09/crm_form3.png)

One of the best features of FluentCRM is that it has native integration with [**Fluent Forms**](https://wordpress.org/plugins/fluentform/) which is also a popular Subscriptions and Payment Form Plugin for WordPress. FluentCRM uses this plugin to handle the default subscriptions of Contacts in FluentCRM.

[![form wp](https://fluentcrm.com/wp-content/uploads/2020/09/form_wp.png)](https://wordpress.org/plugins/fluentform/)

The good news is you can customize the Subscriptions as you want in Fluent Forms and connect the form with FluentCRM. If you want to add more people to your marketing campaign, you can create a landing page including a form. Your audience can fill up the form and they will get a double opt-in email and register as a contact for your email marketing campaigns.

## Activating Fluent Forms [\#](https://fluentcrm.com/docs/opt-in-forms-fluent-forms-basic-configuration\#activating-fluent-forms)

To get started with Subscription Forms in FluentCRM, go to the FluentCRM **Dashboard ➜ Forms**, Click on the **Activate Fluent Forms Integration** button, and wait for the confirmation. This will install the Fluent Forms plugin in the background.

![crm form activate](https://fluentcrm.com/wp-content/uploads/2020/09/crm_form_activate.png)

## Create Subscription Form [\#](https://fluentcrm.com/docs/opt-in-forms-fluent-forms-basic-configuration\#create-subscription-form)

Once the plugin is installed, you will see a success message on the top right corner of the dashboard as shown in the below screenshot.

![crm form activated new](https://fluentcrm.com/wp-content/uploads/2020/09/crm_form_activated_new.png)

Now you can create your first subscription form by clicking on the red button saying **Create Your First Form** or the blue **Create a New Form** button. A popup will appear, and you will see a list of templates ready for you, pick any template you wish.

![crm form select template](https://fluentcrm.com/wp-content/uploads/2020/09/crm_form_select_template.png)

### Templates [\#](https://fluentcrm.com/docs/opt-in-forms-fluent-forms-basic-configuration\#templates)

The templates offered while creating the form look like below:

![crm form 1](https://fluentcrm.com/wp-content/uploads/2020/09/crm_form_1.png)Template 1![crm form 2](https://fluentcrm.com/wp-content/uploads/2020/09/crm_form_2.png)Template 2![crm form 3](https://fluentcrm.com/wp-content/uploads/2020/09/crm_form_3.png)Template 3

You might want to use the 3rd template as it is a regular and common use case for subscription forms that include both Name & Email.

### Mapping List & Tags [\#](https://fluentcrm.com/docs/opt-in-forms-fluent-forms-basic-configuration\#mapping-list-tags)

Now it’s time to fill in the Form Title, Select the **[List](https://fluentcrm.com/docs/segment-your-audience/#Lists)** and **[Tags](https://fluentcrm.com/docs/segment-your-audience/#Tags)** you want to map with FluentCRM. It is required to create the List and tags before creating the form. Check the checkbox **Enable [Double Opt-in Confirmation](https://fluentcrm.com/docs/global-double-opt-in-settings/)** for new contacts so that FluentCRM will send a double opt-in email to the user as soon as the form is submitted to confirm their subscription. Now click on the **Create Form** button.

You will also see a message saying “ _This form will be created in Fluent Forms and you can customize it_ anytime” which means the form is customizable and you can design and configure settings later at any time. We made a dedicated guide on that in [Fluent Forms Advanced Configuration](https://fluentcrm.com/docs/opt-in-forms-advanced-configuration/)

![crm form create new](https://fluentcrm.com/wp-content/uploads/2020/09/crm_form_create_new.png)

The form will be created with an active feed with FluentCRM, all the submitted entries will be added to your assigned [Lists](https://fluentcrm.com/docs/segment-your-audience/#Lists) and [T](https://fluentcrm.com/docs/segment-your-audience/#1-toc-title) [ags.](https://fluentcrm.com/docs/segment-your-audience/#Tags)

## Form Actions [\#](https://fluentcrm.com/docs/opt-in-forms-fluent-forms-basic-configuration\#form-actions)

Once the form is created you will a success message on the top right corner of the dashboard. Now you can **Preview the Form**, **Edit the Form** and also **Edit the Connection with FluentCRM** feed by clicking on each link.

![crm form created](https://fluentcrm.com/wp-content/uploads/2020/09/crm_form_created.png)

### Preview [\#](https://fluentcrm.com/docs/opt-in-forms-fluent-forms-basic-configuration\#preview)

When the form is created you will be provided with a shortcode of Fluent Forms to use the form on any Page or Post. To Preview the Form how it looks like click on the **Preview The Form** Button.

### Edit Form [\#](https://fluentcrm.com/docs/opt-in-forms-fluent-forms-basic-configuration\#edit-form)

You can also Edit the Form Fields, and add more fields from various types of fields. This will take you to the Fluent Forms Editor directly.

### Edit Connection [\#](https://fluentcrm.com/docs/opt-in-forms-fluent-forms-basic-configuration\#edit-connection)

This is the FluentCRM Feed Integration settings that connect the Fluent Form with FluentCRM. More about this is discussed in [Fluent Forms Advanced Configuration](https://fluentcrm.com/docs/opt-in-forms-advanced-configuration/).

If you close the popup window, you can anytime do these actions from the Forms Dashboard as shown in the below screenshot.

![crm form list](https://fluentcrm.com/wp-content/uploads/2020/09/crm_form_list.png)

### Actions from Fluent Forms [\#](https://fluentcrm.com/docs/opt-in-forms-fluent-forms-basic-configuration\#actions-from-fluent-forms)

The above options are the exact same from the Fluent Forms dashboard as below:

![form actions](https://fluentcrm.com/wp-content/uploads/2020/09/form_actions.png)

## Form Submission [\#](https://fluentcrm.com/docs/opt-in-forms-fluent-forms-basic-configuration\#form-submission)

Now it is time to add the form to a Page or Post and then test the submission.

### Embedding Subscription Form [\#](https://fluentcrm.com/docs/opt-in-forms-fluent-forms-basic-configuration\#embedding-subscription-form)

To use the form we need to use the shortcode or even a Gutenberg Editor Block that will let us select the Fluent Form on any page or post. In this tutorial we will be adding the form on a new page as below:

![crm form embed (1)](https://fluentcrm.com/wp-content/uploads/2020/09/crm_form_embed-1.png)

After publishing the page with the form only we will see a page similar to the screenshot below:

![crm form on page](https://fluentcrm.com/wp-content/uploads/2020/09/crm_form_on_page.png)

We could also create a page and add the form’s shortcode to the page in a paragraph or shortcode block, or use the shortcode in the sidebar widget or within a post.

### Entry in Fluent Forms [\#](https://fluentcrm.com/docs/opt-in-forms-fluent-forms-basic-configuration\#entry-in-fluent-forms)

Now let’s test our form by submitting a test name and an email address and then Go to **Fluent Forms >** either **All entries** or the **Form specific Entries** and check the entry that is submitted.

![crm form submitted](https://fluentcrm.com/wp-content/uploads/2020/09/crm_form_submitted.png)

After submitting the form with test details check the entry in the Fluent Forms dashboard. You will see the entry details as shown below:

![crm form entry feed](https://fluentcrm.com/wp-content/uploads/2020/09/crm_form_entry_feed.png)

#### Feed Status [\#](https://fluentcrm.com/docs/opt-in-forms-fluent-forms-basic-configuration\#feed-status)

**Important:** The **Submission Logs** section is very important working with any feeds like FluentCRM in this case. If you ever see any unwanted behavior or the form does not submit the contact to FluentCRM, please check the entry if it is submitted and then this section to check if it shows a _success_ message or not. It will also log the reason if it fails to submit the contact into FluentCRM.

### Contact in FluentCRM [\#](https://fluentcrm.com/docs/opt-in-forms-fluent-forms-basic-configuration\#contact-in-fluentcrm)

Since the entry shows a success message for the FluentCRM feed, let’s check the FluentCRM contacts to see if our test form submission successfully added the contact or not. Go to **FluentCRM  ➜ Contacts** or the [Contacts Dashboard](https://fluentcrm.com/docs/contacts-dashboard/) and you should see the contact as shown in the below screenshot.

![crm form contact entered](https://fluentcrm.com/wp-content/uploads/2020/09/crm_form_contact_entered.png)

That’s all for the Subscription Form and collecting contact information into FluentCRM. To go beyond please check [Fluent Forms Advanced Configuration](https://fluentcrm.com/docs/opt-in-forms-advanced-configuration/) for further and advanced configuration.

##### What are your Feelings

#### Share This Article :

- [![Facebook](https://fluentcrm.com/wp-content/plugins/betterdocs/assets/images/social/facebook.svg?v=4.3.7)](https://www.facebook.com/sharer/sharer.php?u=https://fluentcrm.com/docs/opt-in-forms-fluent-forms-basic-configuration/)
- [![X](https://fluentcrm.com/wp-content/plugins/betterdocs/assets/images/social/twitter.svg?v=4.3.7)](https://twitter.com/intent/tweet?url=https://fluentcrm.com/docs/opt-in-forms-fluent-forms-basic-configuration/)
- [![LinkedIn](https://fluentcrm.com/wp-content/plugins/betterdocs/assets/images/social/linkedin.svg?v=4.3.7)](https://www.linkedin.com/shareArticle?mini=true&url=https://fluentcrm.com/docs/opt-in-forms-fluent-forms-basic-configuration/)
- [![Pinterest](https://fluentcrm.com/wp-content/plugins/betterdocs/assets/images/social/pinterest.svg?v=4.3.7)](https://pinterest.com/pin/create/button/?url=https://fluentcrm.com/docs/opt-in-forms-fluent-forms-basic-configuration/)

[Still stuck? How can we help?](https://fluentcrm.com/docs/opt-in-forms-fluent-forms-basic-configuration#betterdocs-form-modal)

## How can we help?

Name: \*

Email: \*

Message: \*

Updated on November 7, 2022

[Capturing Leads Remotely from Fluent Forms](https://fluentcrm.com/docs/capturing-leads-through-fluent-forms-webhook/) [Fluent Forms Advanced Configuration](https://fluentcrm.com/docs/opt-in-forms-advanced-configuration/)

## 15 Comments

1. when using fluentcrm and fluent forms, how can I add Elementor forms or double opt in?





[Reply](https://fluentcrm.com/docs/opt-in-forms-fluent-forms-basic-configuration/?replytocom=4655#respond)

1. You can add Elementor forms when using Elementor and integrate with FluentCRM. For double opt-in, just keep the double opt-in email enabled in settings.





      [Reply](https://fluentcrm.com/docs/opt-in-forms-fluent-forms-basic-configuration/?replytocom=4663#respond)
2. Hello,



I cannot get FluentCRM to send the confirmation link. I do not know whether 3 of my email providers has blocked those messages. My campaigns have been working so I am not sure where the problem lies. I have received them in previous tests however.



Any help would be appreciated.



Thank you.





[Reply](https://fluentcrm.com/docs/opt-in-forms-fluent-forms-basic-configuration/?replytocom=4617#respond)

1. Having the same problem, followed all documentation….





      [Reply](https://fluentcrm.com/docs/opt-in-forms-fluent-forms-basic-configuration/?replytocom=4994#respond)
3. Hi,


Is it possible to activate DOI only if the subscriber has checked a respective DOI-checkbox in the form? Let’s say somebody is subscribing to a paid training, which I want to let him do regardless of a Newsletter Opt In. So if he doesn’t check the “yes I want your Newsletter” checkbox, I want to integrate him in fluent CRM (as pending forever?) but he shouldn’t receive any DOI-confirmation mail.


Thanks and regards,


Roger





[Reply](https://fluentcrm.com/docs/opt-in-forms-fluent-forms-basic-configuration/?replytocom=1815#respond)

1. Yes, it’s possible via conditional logic(Form>Edit integration).





      [Reply](https://fluentcrm.com/docs/opt-in-forms-fluent-forms-basic-configuration/?replytocom=1833#respond)
4. How check birthday to send email?





[Reply](https://fluentcrm.com/docs/opt-in-forms-fluent-forms-basic-configuration/?replytocom=1632#respond)

1. Hi Nguyen Vu, We are already working on this kind of automation. You can expect to see these soon. 🙂





      [Reply](https://fluentcrm.com/docs/opt-in-forms-fluent-forms-basic-configuration/?replytocom=1636#respond)
5. Hi Nazir,


thank you very much for the helpfull link. Now we are a pro licenced user of fluentCrM too.


Greetings


Jan





[Reply](https://fluentcrm.com/docs/opt-in-forms-fluent-forms-basic-configuration/?replytocom=1525#respond)

6. Hi,



how to change bg-color in global emails. Opt-in Emails in mostly all solutions look so unpro boring. More styling options corresponding to the Companys Corporate Identity is prefered. Maybe FluentForms/FluentCRM will be the winner in this case soon.



Greetings





[Reply](https://fluentcrm.com/docs/opt-in-forms-fluent-forms-basic-configuration/?replytocom=1522#respond)

1. Although a workaround, I believe the best way to achieve this is to design an opt-in email using Stripo, switch to text mode in FluentCRM, and select RAW HTML design template. Don’t forget to use the shortcode as the confirmation link though!





      [Reply](https://fluentcrm.com/docs/opt-in-forms-fluent-forms-basic-configuration/?replytocom=1524#respond)
7. I’m using Bloom by Elegant Themes for my opt-in and I have Double Opt-in set inside of FluentCRM. While it does send a confirmation link, I can’t see any difference between users who do or do not click the link.



Users get added to my list before clicking the confirmation link. I do not see any benchmark or trigger I can use in an automation to tell if they did or did not click the confirmation link.



Can you direct me to any other documentation about this, without referencing Fluent Forms?





[Reply](https://fluentcrm.com/docs/opt-in-forms-fluent-forms-basic-configuration/?replytocom=350#respond)

1. Hi William, FluentCRM differentiates confirmed and unconfirmed contacts as **Subscribers** and **Pending**. This status will change based on whether the contact has clicked on your confirmation link or not. Please check this doc: [https://fluentcrm.com/docs/types-of-contact-status/](https://fluentcrm.com/docs/types-of-contact-status/)





      [Reply](https://fluentcrm.com/docs/opt-in-forms-fluent-forms-basic-configuration/?replytocom=356#respond)

      1. Sorry, I forgot to follow-up. The reason I didn’t see a difference is due to a bug in Bloom. They send everything over as Subscribed. I made them aware of the problem, as none of the leads came in Pending. Sadly, they have not ETA to fix and it doesn’t seem to be high on their agenda.





         [Reply](https://fluentcrm.com/docs/opt-in-forms-fluent-forms-basic-configuration/?replytocom=479#respond)

         1. I haven’t used bloom yet. But in that case, you can take advantage of our dynamic segmentation. Here’s what I suggest, use dynamic segments to find your new contacts and mark them as pending contacts. Then you can trigger a double opt-in email for them. I know it’s somewhat manual work but at this moment, this is what I can suggest instead of using Fluent Forms.





            [Reply](https://fluentcrm.com/docs/opt-in-forms-fluent-forms-basic-configuration/?replytocom=483#respond)

### Leave a Reply [Cancel reply](https://fluentcrm.com/docs/opt-in-forms-fluent-forms-basic-configuration/\#respond)

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

Contact

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

Newsletter

SUBSCRIBE