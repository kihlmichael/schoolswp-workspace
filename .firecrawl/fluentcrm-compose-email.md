[Skip to content](https://fluentcrm.com/docs/compose-email-in-fluentcrm/#main)

Special [20% Discount](https://fluentcrm.com/deal/?utm_source=fcrmsite&utm_medium=banner&utm_campaign=special26&utm_id=special+deal) on Email Automation

[Start Automation](https://fluentcrm.com/deal/?utm_source=fcrmsite&utm_medium=banner&utm_campaign=special26&utm_id=special+deal)

All CategoriesGetting StartedGlobal SettingsFluentCRM EssentialsContactsEmailsFormsAutomationsEvent TrackingReportsPlugins Integration & AutomationMigrating from Other PlatformsBounce HandlersMiscellaneousDeveloper DocumentationFrequently Asked QuestionsChange Log

Popular Searchautomationtheunsubscribewebhookcustom

View Categories

3 min read

Table of Contents

- [Email Editor](https://fluentcrm.com/docs/compose-email-in-fluentcrm/#email-editor)
  - [Email Styling Settings](https://fluentcrm.com/docs/compose-email-in-fluentcrm/#email-styling-settings)
  - [Template Type](https://fluentcrm.com/docs/compose-email-in-fluentcrm/#template-type)
    - [Simple Boxed](https://fluentcrm.com/docs/compose-email-in-fluentcrm/#simple-boxed)
    - [Plain Centered](https://fluentcrm.com/docs/compose-email-in-fluentcrm/#plain-centered)
    - [Plain Left](https://fluentcrm.com/docs/compose-email-in-fluentcrm/#plain-left)
    - [Classic Editor](https://fluentcrm.com/docs/compose-email-in-fluentcrm/#classic-editor)
    - [Raw HTML](https://fluentcrm.com/docs/compose-email-in-fluentcrm/#raw-html)
  - [Blocks](https://fluentcrm.com/docs/compose-email-in-fluentcrm/#blocks)
  - [Smart Codes/ Dynamic Tags](https://fluentcrm.com/docs/compose-email-in-fluentcrm/#smart-codes-dynamic-tags)
  - [Use Email Template](https://fluentcrm.com/docs/compose-email-in-fluentcrm/#use-email-template)
  - [Preview Composed Email](https://fluentcrm.com/docs/compose-email-in-fluentcrm/#preview-composed-email)
  - [Advanced Features](https://fluentcrm.com/docs/compose-email-in-fluentcrm/#advanced-features)
    - [Forward Slash \[ / \]](https://fluentcrm.com/docs/compose-email-in-fluentcrm/#forward-slash)
    - [At Sign \[ @ \]](https://fluentcrm.com/docs/compose-email-in-fluentcrm/#at-sign)
  - [Sending test Email](https://fluentcrm.com/docs/compose-email-in-fluentcrm/#sending-test-email)

The main step of email marketing and sending out emails is to compose or prepare the Email Content when the contacts are ready. In this tutorial, we will be learning and exploring email editing or composing emails in FluentCRM.

How to Create an Email Templates in FluentCRM - YouTube

Tap to unmute

[How to Create an Email Templates in FluentCRM](https://www.youtube.com/watch?v=LfY6o1esuCE) [WPManageNinja](https://www.youtube.com/channel/UCiyeXfnGx9e06hXWf0Hz7ow)

WPManageNinja11.8K subscribers

[Watch on](https://www.youtube.com/watch?v=LfY6o1esuCE)

## Email Editor [\#](https://fluentcrm.com/docs/compose-email-in-fluentcrm/\#email-editor)

As we have seen above that there are different places Emails can be composed and sent. Now we will be exploring features of the FluentCRM to edit or compose an email in those places.

> **Important:** FluentCRM uses Gutenberg Editor as the default Email Editor. The features of the email editor and available blocks to use in the email is limited as per Gutenberg features and limitations.

### Email Styling Settings [\#](https://fluentcrm.com/docs/compose-email-in-fluentcrm/\#email-styling-settings)

![crm email emailstyling](https://fluentcrm.com/wp-content/uploads/2022/08/crm_email_emailstyling.png)

This setting is available for all template types except RAW HTML. The available options are:

1. **Body Background Color:** The background color for the Email Body.
2. **Content Background Color:** The background color for the Content Section only.
3. **Default Content Color:** The text color for the content.
4. **Content Max Width (px):** Maximum width for the content
5. **Footer Text Color:** Text color for footer.
6. **Default Link Color:** The link text color.
7. **Content Font Family:** Font Family for the whole content.
8. **Headings Font Family:** Font Family for the Header of the email content.
9. **Disable Default Email Footer:** There is a global [Email Footer Settings](https://fluentcrm.com/docs/global-email-settings/#Email-Footer-Settings). you can turn off the global footer by checking this option.

### Template Type [\#](https://fluentcrm.com/docs/compose-email-in-fluentcrm/\#template-type)

#### Simple Boxed [\#](https://fluentcrm.com/docs/compose-email-in-fluentcrm/\#simple-boxed)

![crm email editor template simple boxed](https://fluentcrm.com/wp-content/uploads/2022/08/crm_email_editor_template_simple_boxed.png)

This is the default template and also works for most of the use cases.

#### Plain Centered [\#](https://fluentcrm.com/docs/compose-email-in-fluentcrm/\#plain-centered)

![crm email editor template plain centered](https://fluentcrm.com/wp-content/uploads/2022/08/crm_email_editor_template_plain_centered.png)

Simple and content centered which is almost close to the default template option.

#### Plain Left [\#](https://fluentcrm.com/docs/compose-email-in-fluentcrm/\#plain-left)

![crm email editor template plain left](https://fluentcrm.com/wp-content/uploads/2022/08/crm_email_editor_template_plain_left.png)

This template aligns the whole email content to the left.

#### Classic Editor [\#](https://fluentcrm.com/docs/compose-email-in-fluentcrm/\#classic-editor)

![crm email editor template classic editor](https://fluentcrm.com/wp-content/uploads/2022/08/crm_email_editor_template_classic_editor.png)

If you are familiar with the legacy WordPress Classic Editor, this option is for you. You can have more control over the content rather than the Gutenberg Editor.

#### Raw HTML [\#](https://fluentcrm.com/docs/compose-email-in-fluentcrm/\#raw-html)

FluentCRM’s **Raw HTML** Email Editor allows advanced users to create fully customized email templates. This is especially useful if you want to import templates from external sources or code the email body using **HTML**.

![raw html](https://fluentcrm.com/wp-content/uploads/2022/08/RAW-HTML-1-scaled.webp)

However, when using the Raw HTML editor, the **Global Footer**, which typically includes essential links like **Unsubscribe** and **Manage Email Subscription**, is not automatically added. You will need to manually insert these links into your template.

To do this, go to the **Settings** tab and click on **Email Settings**. Scroll to the **Email Footer Settings** section, where you can edit or insert the **Unsubscribe** or **Manage Email** **Subscription** links.

![unsubscribe or manage email subscription](https://fluentcrm.com/wp-content/uploads/2022/08/Unsubscribe-or-Manage-email-subscription-scaled.webp)

### Blocks [\#](https://fluentcrm.com/docs/compose-email-in-fluentcrm/\#blocks)

There are a number of Content Blocks available in the FluentCRM to be used in the email contents. More about these are discussed in **[Content Blocks in FluentCRM Email Editor](https://fluentcrm.com/docs/content-blocks-in-fluentcrm-email-editor/)**

### Smart Codes/ Dynamic Tags [\#](https://fluentcrm.com/docs/compose-email-in-fluentcrm/\#smart-codes-dynamic-tags)

There are a number of SmartCode available in the FluentCRM to be used in the email contents. More about these are discussed in **[SmartCodes in FluentCRM Email Editor](https://fluentcrm.com/docs/smartcodes-in-fluentcrm-email-editor/).**

### Use Email Template [\#](https://fluentcrm.com/docs/compose-email-in-fluentcrm/\#use-email-template)

This option is very helpful when you already have composed another email template and use that in the current email as a template or if you want to use a base template and extend or customize it into a new template.

You will see the **Template ID Number**, **Template Title**, and an **Action Button** to click to **Import** the template you want.

![crm email editor import template](https://fluentcrm.com/wp-content/uploads/2022/08/crm_email_editor_import_template.png)

### Preview Composed Email [\#](https://fluentcrm.com/docs/compose-email-in-fluentcrm/\#preview-composed-email)

One of the most helpful features of FluentCRM is the **Preview**. By clicking on the Eye button you can preview the composed email to see how it may look in the recipient’s email client. Please remember that there are numerous email clients that are Web, Desktop or Mobile based. The email content you composed may look slightly different on different devices. You should add mobile device-specific CSS codes too so that the email content looks better on Mobile devices as well.

> **Important:** FluentCRM uses Gutenberg Block Editor that comes with WordPress by default. Few features and customizations are Guteberg dependent and limited by its features.

![crm email editor preview](https://fluentcrm.com/wp-content/uploads/2022/08/crm_email_editor_preview.png)

### Advanced Features [\#](https://fluentcrm.com/docs/compose-email-in-fluentcrm/\#advanced-features)

To create or compose a new email content or template FluentCRM provides you with a few more advanced features.

#### Forward Slash \[ **/** \] [\#](https://fluentcrm.com/docs/compose-email-in-fluentcrm/\#forward-slash)

![crm email editor slash](https://fluentcrm.com/wp-content/uploads/2022/08/crm_email_editor_slash.png)

By using a forward slash ( / ) in the content you will be able to use available block types used in the email content such as **Image, heading, List, Buttons, Classic Editor, Columns, Group, Row, and Stack**.

#### At Sign \[ **@** \] [\#](https://fluentcrm.com/docs/compose-email-in-fluentcrm/\#at-sign)

![crm email editor at](https://fluentcrm.com/wp-content/uploads/2022/08/crm_email_editor_at.png)

There are some places where you might want to use Customer or Contact Data available in FluentCRM. You can quickly add such data via ShortCode and typing @ in the Email editor will offer you with such Contact Data such as **Full Name, First Name, Last Name, Contact Email, Contact ID, User ID, Address Line 1, Address Line 2, City, etc.**

### Sending test Email [\#](https://fluentcrm.com/docs/compose-email-in-fluentcrm/\#sending-test-email)

Once you are done composing the email content you should test the email content to your own email to see how they are rendered in Email Client. **Remember that,** Using ShortCodes that fetch contact data will not be rendered in the test email as the test email will not have generated email that assigns an email with the relevant contact by unique parameters and renders the contact data.

![crm email sequence send test email](https://fluentcrm.com/wp-content/uploads/2022/08/crm_email_sequence_send_test_email.png)

For best email delivery of the composed emails in FluentCRM, please consider using an SMTP Plugin like FluentSMTP. You should also be careful with the content to not be filtered by Spam Filters and mark your email as a Spam and this might get your email rejected or land in the Spam Folder of the Email Clients.

##### What are your Feelings

#### Share This Article :

- [![Facebook](https://fluentcrm.com/wp-content/plugins/betterdocs/assets/images/social/facebook.svg?v=4.3.7)](https://www.facebook.com/sharer/sharer.php?u=https://fluentcrm.com/docs/compose-email-in-fluentcrm/)
- [![X](https://fluentcrm.com/wp-content/plugins/betterdocs/assets/images/social/twitter.svg?v=4.3.7)](https://twitter.com/intent/tweet?url=https://fluentcrm.com/docs/compose-email-in-fluentcrm/)
- [![LinkedIn](https://fluentcrm.com/wp-content/plugins/betterdocs/assets/images/social/linkedin.svg?v=4.3.7)](https://www.linkedin.com/shareArticle?mini=true&url=https://fluentcrm.com/docs/compose-email-in-fluentcrm/)
- [![Pinterest](https://fluentcrm.com/wp-content/plugins/betterdocs/assets/images/social/pinterest.svg?v=4.3.7)](https://pinterest.com/pin/create/button/?url=https://fluentcrm.com/docs/compose-email-in-fluentcrm/)

[Still stuck? How can we help?](https://fluentcrm.com/docs/compose-email-in-fluentcrm/#betterdocs-form-modal)

## How can we help?

Name: \*

Email: \*

Message: \*

Updated on October 8, 2024

[Overview of Emails from FluentCRM](https://fluentcrm.com/docs/overview-of-emails-from-fluentcrm/) [Content Blocks in Email Editor](https://fluentcrm.com/docs/content-blocks-in-fluentcrm-email-editor/)

## 22 Comments

1. I am moving from Mailpoet to Fluent CRM but the ease at which you can add different products or posts in Mailpoet makes me think that this was a mistake… Is there a way to add posts and design them automatically to a section of the email. And I am not talking about the last posts, but all different posts and also projects.


And in the visual editor (which I prefer) I can’t even add latest posts (or am I mistaken?)





[Reply](https://fluentcrm.com/docs/compose-email-in-fluentcrm/comment-page-2/?replytocom=5778#respond)

1. Hey Jonas, I think we have the latest posts and product blocks for easy accesss in the block editor. The drag and drop editor is more for simplicity but we’ll do some modifications to the block editor so you can have a better experience. Hope it helps.





      [Reply](https://fluentcrm.com/docs/compose-email-in-fluentcrm/comment-page-2/?replytocom=5784#respond)

### Leave a Reply [Cancel reply](https://fluentcrm.com/docs/compose-email-in-fluentcrm/\#respond)

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

Subscribe

SUBSCRIBE