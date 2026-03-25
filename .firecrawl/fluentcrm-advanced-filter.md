[Skip to content](https://fluentcrm.com/docs/advanced-filter#main)

Special [20% Discount](https://fluentcrm.com/deal/?utm_source=fcrmsite&utm_medium=banner&utm_campaign=special26&utm_id=special+deal) on Email Automation

[Start Automation](https://fluentcrm.com/deal/?utm_source=fcrmsite&utm_medium=banner&utm_campaign=special26&utm_id=special+deal)

All CategoriesGetting StartedGlobal SettingsFluentCRM EssentialsContactsEmailsFormsAutomationsEvent TrackingReportsPlugins Integration & AutomationMigrating from Other PlatformsBounce HandlersMiscellaneousDeveloper DocumentationFrequently Asked QuestionsChange Log

Popular Searchautomationtheunsubscribewebhookcustom

View Categories

11 min read

Table of Contents

- [General Properties](https://fluentcrm.com/docs/advanced-filter#general-properties)
  - [Contact](https://fluentcrm.com/docs/advanced-filter#contact)
  - [Contact Segment](https://fluentcrm.com/docs/advanced-filter#contact-segment)
  - [Contact Activities](https://fluentcrm.com/docs/advanced-filter#contact-activities)
- [Custom Field Properties](https://fluentcrm.com/docs/advanced-filter#custom-field-properties)
- [Integrated Properties](https://fluentcrm.com/docs/advanced-filter#integrated-properties)
  - [Woocommerce](https://fluentcrm.com/docs/advanced-filter#woocommerce)
  - [LearnDash](https://fluentcrm.com/docs/advanced-filter#learndash)
- [Filter Conditions](https://fluentcrm.com/docs/advanced-filter#filter-conditions)
  - [Textual Conditions](https://fluentcrm.com/docs/advanced-filter#textual-conditions)
  - [Date-Based Conditions](https://fluentcrm.com/docs/advanced-filter#date-based-conditions)
  - [Choice-Based Conditions](https://fluentcrm.com/docs/advanced-filter#choice-based-conditions)
  - [Numeric Conditions](https://fluentcrm.com/docs/advanced-filter#numeric-conditions)
  - [Contact Segment - Tag](https://fluentcrm.com/docs/advanced-filter#contact-segment--tag)
  - [Contact Activities](https://fluentcrm.com/docs/advanced-filter#contact-activities)
  - [WooCommerce Conditions](https://fluentcrm.com/docs/advanced-filter#woocommerce-conditions-)
  - [Contact Activities - Automation Activities](https://fluentcrm.com/docs/advanced-filter#contact-activities--automation-activities%C2%A0)
  - [Activities - Email Sequence](https://fluentcrm.com/docs/advanced-filter#activities--email-sequence)
- [Example Usage](https://fluentcrm.com/docs/advanced-filter#example-usage)

As we have seen and learned about the [**Contacts Dashboard**](https://fluentcrm.com/docs/contacts-dashboard/) and also the [**General & Dynamic Segmentation**](https://fluentcrm.com/docs/segment-your-audience/) of the FluentCRM contacts, we have noticed that there is an Advanced Filtering option available in the FluentCRM. This option offers powerful filtering by various contact data that are either static or dynamically changed upon Contact and FluentCRM activities. In this tutorial, we will evaluate and demonstrate Advanced Filtering to learn and assimilate this feature. The **No. 7** from the introduction to **[Contacts Dashboard](https://fluentcrm.com/docs/contacts-dashboard/)** we have seen the Advanced Filter option. **Toggling On** this feature will activate the **Advanced Filtering** and we will see more options similar to the screenshot below.

![contacts fluentcrm 7](https://fluentcrm.com/wp-content/uploads/2023/08/Contacts-FluentCRM-7.png)

The default options will let you **Add Data Fields** as **AND**& **OR** conditions as you wish to set, **Filter** them if you are confirmed, **Delete Data Fileds** by Delete Button(Recycle bin icon), or **Clear Filters** as well. Now Click on the **\+ Add** button to get started. This will provide a few groups of data and we will be exploring them one by one below.

## General Properties [\#](https://fluentcrm.com/docs/advanced-filter\#general-properties)

There are 3 types of general properties. 2 of them are contact properties and 1 other property is based on the activities inside the FluentCRM.

### Contact [\#](https://fluentcrm.com/docs/advanced-filter\#contact)

![contacts fluentcrm 1 1](https://fluentcrm.com/wp-content/uploads/2023/08/Contacts-FluentCRM-1-1.png)

The available data properties and their short descriptions are:

01. **General Properties:** This is a general searchable filter that will let you filter by **Email**, **First Name**, **Last Name**, **Address Line 1**& **2**, **Postal Code**, **City**, **State**, **Country**, **Phone**, and **Status** with this single parameter.
02. **First Name:** First Name of the contact.
03. **Last Name:** Last Name of the contact.
04. **Email Address:** Email Address of the contact. This is false the minimum required field to add a contact in the FleuntCRM.
05. **Address Line 1:** The primary address field and also the minimum or default field to store the address information of the contact.
06. **Address Line 2:** Alternative field to store additional address information.
07. **City:** City of the contact.
08. **State:** State of the contact.
09. **Postal Code:** Postal Code information of the contact.
10. **Country:** Country of the contact.
11. **Phone/ Mobile:** Phone or Mobile Number that may contain or not contain the country code depending on how you added the information.
12. **WP User ID:** The WordPress User ID of the contact if the contact is present in the WordPress user list.
13. **Name Prefix(Title):** Mr, Mrs, and Ms depending on the person’s designation.
14. **Source:** The source of the contact like Woocommerce, Fluent Forms, or other sources. You can also update or add source information while [importing the user](https://fluentcrm.com/docs/import-contacts-into-fluentcrm/#Importing-Contacts-from-CSV-File). If you are using a [CSV file to import](https://fluentcrm.com/docs/import-contacts-into-fluentcrm/#Importing-Contacts-from-CSV-File) please add a source column in the CSV file.
15. **Last Activity:** The Last Activity field in FluentCRM provides a consolidated view of WordPress user logins and interactions with email campaigns, such as email click activities.
16. **Created At:** The date and time when the user was created in the FluentCRM.

### Contact Segment [\#](https://fluentcrm.com/docs/advanced-filter\#contact-segment)

![contacts fluentcrm 2 1](https://fluentcrm.com/wp-content/uploads/2023/08/Contacts-FluentCRM-2-1.png)

The available data properties and their short descriptions are:

1. **Status:** [**Subscription Status**](https://fluentcrm.com/docs/fluentcrm-contacts-status/) of the contact.
2. **Type:** The contact type of the user is either **Customer** or **Lead**.
3. **Tags:** Tags that are available in the FluentCRM.
4. **Lists:** Lists that are available in the FluentCRM.

### Contact Activities [\#](https://fluentcrm.com/docs/advanced-filter\#contact-activities)

![contacts fluentcrm 3 1](https://fluentcrm.com/wp-content/uploads/2023/08/Contacts-FluentCRM-3-1.png)

The available data properties and their short descriptions are:

1. **Last Email Sent:** The last date of the email sent to contacts.
2. **Last Email Open:** The last date when the contacts opened any email sent to them.
3. **Last Email Clicked:** The last date when the contacts clicked any links from emails sent to them.

## Custom Field Properties [\#](https://fluentcrm.com/docs/advanced-filter\#custom-field-properties)

![contacts fluentcrm 4 1](https://fluentcrm.com/wp-content/uploads/2023/08/Contacts-FluentCRM-4-1.png)

This is a user-defined option that is configured in [**Custom Contact Fields Settings**](https://fluentcrm.com/docs/global-custom-contact-fields/). All the available custom contact fields will be listed in this option to let you apply to filter based on the custom contact field properties.

## Integrated Properties [\#](https://fluentcrm.com/docs/advanced-filter\#integrated-properties)

FluentCRM integrates with popular WordPress plugins like Woocommerce, LearnDash, LifterLMS, Easy Digital Downloads, etc. Plugin Specific Data Properties are discussed below:

### Woocommerce [\#](https://fluentcrm.com/docs/advanced-filter\#woocommerce)

![contacts fluentcrm](https://fluentcrm.com/wp-content/uploads/2022/01/Contacts-FluentCRM-scaled.webp)

The available data properties and their short descriptions are:

1. **Total Order Count:** Total orders against the customer.
2. **Total Order Value:** Total order value from different orders.
3. **Last Order Date:** The last date when the customer ordered any product.
4. **First Order Date:** The first date when the customer orders any product.
5. **Purchased Products:** All the purchased products against a customer.
6. **Purchased Categories:** All the Product Categories that are assigned to the products and available in the orders for the customer.
7. **Purchased Tags:** Product Tags assigned to purchased products available in the orders against the customer.
8. **Used Coupons:** Any used coupons in the purchased order against the customer.
9. **Purchased Product Variations**: Filter contacts based on their purchased WooCommerce product variations.

### LearnDash [\#](https://fluentcrm.com/docs/advanced-filter\#learndash)

![contacts fluentcrm 8](https://fluentcrm.com/wp-content/uploads/2023/08/Contacts-FluentCRM-8.png)

The available data properties and their short descriptions are:

1. **Last Enrollment Date:** The last date of enrollment for any courses against the contact.
2. **First Enrollment Date:** The first date of enrollment for any courses against the contact.
3. **Enrollment Courses:** The Courses that are available on the Enrolled List for any contact.
4. **Enrollment Groups:** The Groups that are available on the Enrolled List for any contact.
5. **Enrollment Categories:** The Categories that are available on the Enrolled List for any contact.
6. **Enrollment Tags:** The Tags that are available on the Enrolled List for any contact.

## Filter Conditions [\#](https://fluentcrm.com/docs/advanced-filter\#filter-conditions)

All of the above **Data Properties** can be used to filter out contacts depending on the available data. There are various conditions that can be applied to those available data such as **Equal**, **Does not equal**, **Includes**, **Does not Include**, **Before**, **After**, etc. and they are discussed below:

### Textual Conditions [\#](https://fluentcrm.com/docs/advanced-filter\#textual-conditions)

![contacts fluentcrm 9](https://fluentcrm.com/wp-content/uploads/2023/08/Contacts-FluentCRM-9.png)

The available conditional properties that can be applied with the filter are:

**Equal:** Give a value, for an item to be displayed in the view, its property value must include the same text that was supplied.

**For example,** if you input “London” then **FluentCRM** will filter the contact or contacts that have or contain “London” against that **Text-based** Contact Field.

**Does not equal:** Give a value, for an item to be displayed in the view, its property value cannot include the precise text that was supplied. There will also be records that have no value for the property.

**For example,** if you input “London” **then FluentCRM** will filter the contact or contacts that don’t contain “London” against that **Text-based** Contact Field.

**Includes:** You’ll see results that correspond to your input and comparable outcomes.

**E.g.:** When you enter “Regular,” all the results that match the word or a particular letter in the term will be shown.

**Does not include:** Doesn’t include means that the word or letter you type will not be shown.

**E.g.:** When you enter “Regular,” neither the matching results nor those that include a letter from the word “Regular” will be displayed.

**Empty:** Empty is for an option that shows the empty field results. **For example,** Your contact text information contains an empty area that will display the outcome of the selected contact or contacts.

**Not Empty:** Not empty will show the result of that field is not empty. **E.g.:** not empty will display the information from the fields that are filled with data.

### Date-Based Conditions [\#](https://fluentcrm.com/docs/advanced-filter\#date-based-conditions)

![contacts fluentcrm 1 2](https://fluentcrm.com/wp-content/uploads/2023/08/Contacts-FluentCRM-1-2.png)

The available conditional properties that can be applied with the filter are:

**Before:** It will filter to be displayed on the previous days of your given date. **E.g.:** When you enter the date 20-Feb-2023, FluentCRM will provide the results of counting the days backward.

**After:** The next days of the specified date will be displayed after filtering.

**In the date:** In this filter, only the matches of your specified day will be shown.

**Before days:** Through this filter, you can see the results before the specified number of days. **E.g.:** FluentCRM will display the outcome of any contacts you made earlier than seven days ago.

**Within days:** This filter will show results for the specified number of days you want to see.

### Choice-Based Conditions [\#](https://fluentcrm.com/docs/advanced-filter\#choice-based-conditions)

![contacts fluentcrm 2 ](https://fluentcrm.com/wp-content/uploads/2023/08/Contacts-FluentCRM-2-2.png)

The available conditional properties that can be applied with the filter are:

**Includes in:** This filter will display your inputs as choices, from which you must choose to filter your results.

**Not includes in:** Doesn’t include will not show the result of the option you selected it will show the other results you input in the field.

### Numeric Conditions [\#](https://fluentcrm.com/docs/advanced-filter\#numeric-conditions)

![contacts fluentcrm ](https://fluentcrm.com/wp-content/uploads/2023/08/Contacts-FluentCRM-3-2.png)

The available conditional properties that can be applied with the filter are:

**Greater than:** Showing results for numbers more significant than the number you provided. **E.g.:** You have been given the number five thousand now it will show a larger number than five thousand.

**Less than:** Showing results for numbers less than the number you provided. **E.g.:** You have been given the number five thousand now it will show a smaller number than five thousand.

**Equal:** Equal will show you the outcome which is in the same number you have provided. **E.g.:** ifyou gave the number input five thousand the outcome only shows the contact or contacts that match this number.

**Does not equal:** Doesn’t equal will display contacts that differ from the number you entered.

**Empty:** Empty is for an option that shows the empty field results.

**Not empty:** Not empty will show the result that the field is not empty.

### **Contact Segment – Tag** [\#](https://fluentcrm.com/docs/advanced-filter\#contact-segment--tag)

![contacts fluentcrm](https://fluentcrm.com/wp-content/uploads/2023/03/Contacts-FluentCRM.png)

The available conditional properties that can be applied with the filter are:

**Include:** It will show you the contacts that match your input tags. **For example,** if you have selected the tag “Shirt” it will show you the results of contacts that have the tag “Shirt”.

**Does not Include (In any):** Doesn’t show the result on the tag you have included on your field. **For example,** if you have selected the tag “Student” it will show you the results of contacts that don’t have the tag “Student”.

**Includes of all:** will display the contacts for you according to the tag you entered. **For example,** if you input two tags like “Shirt” and “T-shirt” you will see the contacts that have these two tags.

**Includes none of (Match all):** Includes only the tags you have given and will not show in the result.

### **Contact Activities** [\#](https://fluentcrm.com/docs/advanced-filter\#contact-activities)

![contacts fluentcrm ](https://fluentcrm.com/wp-content/uploads/2023/03/Contacts-FluentCRM-2-1.png)

The available conditional properties that can be applied with the filter are:

**Link Clicked:** The link clicked will show the result of those who clicked the link you have been sent with your email.

**Did not clicks:** This filter will show the contacts who didn’t click the link of your email.

**Opened:** It will show the contacts who opened your email.

**Did not open yet:** It will show the contacts who still don’t open your email.

**In (Email Sent):** Show the result of contacts to whom you sent the emails.

**Not in (Regardless of status):** Shows the result of contact or contacts you didn’t send emails to.

### **WooCommerc** eConditions [\#](https://fluentcrm.com/docs/advanced-filter\#woocommerce-conditions-)

The WooCommerce advance filter will only show when the WooCommerce plugin will be activated.

![contacts fluentcrm ](https://fluentcrm.com/wp-content/uploads/2023/03/Contacts-FluentCRM-1.png)

**Include:** It will show you the contacts that match your input tags. **For example,** if you have selected the tag “T-Shirt” it will show you the results of contacts that have the tag “T-Shirt”.

**Does not Include(In any):** Doesn’t show the result on the tag you have included on your field. **For example,** if you have selected the tag “Hoodie” it will show you the results of contacts that don’t have the tag “Hoodie”.

**Includes of all:** will display the contacts for you according to the tag you entered. **For example,** if you input two tags like “Cap” and “T-Shirt” you will see the contacts that have these two tags.

**Includes none of (Match all):** Includes only the tags you have given and will not show in the result.

**Greater than:** Showing results for numbers greater than the number you provided. **E.g.:** You have been given the number five thousand now it will show a larger number than five thousand.

**Less than:** Showing results for numbers less than the number you provided. **E.g.:** You have been given the number five thousand now it will show a smaller number than five thousand.

**Equal:** Equal will show you the outcome which is in the same number you have provided. **E.g.:** ifyou gave the number input five thousand the outcome only shows the contact or contacts that match this number.

**Does not equal:** Doesn’t equal will display contacts that differ from the number you entered.

**Before:** It will filter to be displayed on the previous days of your given date. **E.g.:** When you enter the date 05-Feb-2023, FluentCRM will provide the results of counting the days backward.

**After:** The next days of the specified date will be displayed after filtering.

**In the date:** In this filter, only the matches of your specified day will be shown.

**Before days:** Through this filter, you can see the results before the specified number of days. **E.g.:** FluentCRM will display the outcome of any contacts you made earlier than seven days ago.

**Within days:** This filter will show results for the specified number of days you want to see.

**Yes:** This will show the contacts who are customers of Woocommerce.

**No:** This will show the contacts who are not customers of Woocommerce.

### **Contact Activities – Automation Activities** [\#](https://fluentcrm.com/docs/advanced-filter\#contact-activities--automation-activities%C2%A0)

**Status Complete:** Contacts whose automation has been finished and who have received emails will be filtered by the status complete.

**Status Active:** This will show you the result of contacts who are subscribed contacts and under the Active automation

**Status Cancelled:** It will show the result of the manually canceled automation contacts.

**Status waiting:** The contacts who aren’t subscribers yet but are under automation.

**In ( Regardless of status):** In this filter, you will see the contacts of automation.

**Not in (Regardless of status):** With this filter, you can find out the contacts who aren’t in the automation.

### **Activities – Email Sequence** [\#](https://fluentcrm.com/docs/advanced-filter\#activities--email-sequence)

**Status Completed:** Status Complete will filter the contacts of the completed email sequence and the email that has been sent to them.

**Status Active:** This will only show the active contacts under this email sequence.

**Status Cancelled:** It will show you the contacts who are not in the email sequence.

**In (Regardless of status):** Will show the contacts who were in an email sequence.

**Not in (Regardless of status):** Will show the contact or contacts who aren’t in the email sequence.

## Example Usage [\#](https://fluentcrm.com/docs/advanced-filter\#example-usage)

The same exact filtering method can also be applied in the Email Campaign Setup as well as the below screenshot. Below is an example of using 3 different data and using **AND** with **OR** condition to demonstrate how flexible the advanced filtering of FluentCRM.

![crm campaign subscribers advanced filter](https://fluentcrm.com/wp-content/uploads/2022/01/crm_campaign_subscribers_advanced_filter.png)

##### What are your Feelings

#### Share This Article :

- [![Facebook](https://fluentcrm.com/wp-content/plugins/betterdocs/assets/images/social/facebook.svg?v=4.3.7)](https://www.facebook.com/sharer/sharer.php?u=https://fluentcrm.com/docs/advanced-filter/)
- [![X](https://fluentcrm.com/wp-content/plugins/betterdocs/assets/images/social/twitter.svg?v=4.3.7)](https://twitter.com/intent/tweet?url=https://fluentcrm.com/docs/advanced-filter/)
- [![LinkedIn](https://fluentcrm.com/wp-content/plugins/betterdocs/assets/images/social/linkedin.svg?v=4.3.7)](https://www.linkedin.com/shareArticle?mini=true&url=https://fluentcrm.com/docs/advanced-filter/)
- [![Pinterest](https://fluentcrm.com/wp-content/plugins/betterdocs/assets/images/social/pinterest.svg?v=4.3.7)](https://pinterest.com/pin/create/button/?url=https://fluentcrm.com/docs/advanced-filter/)

[Still stuck? How can we help?](https://fluentcrm.com/docs/advanced-filter#betterdocs-form-modal)

## How can we help?

Name: \*

Email: \*

Message: \*

Updated on August 19, 2024

[Contacts Dashboard](https://fluentcrm.com/docs/contacts-dashboard/) [Contact Overview](https://fluentcrm.com/docs/contact-overview/)

## 10 Comments

1. I want to exclude people who have bought product A or Product B. How do I do this in dynamic segments?





[Reply](https://fluentcrm.com/docs/advanced-filter/?replytocom=16737#respond)

2. So – I want to do a very simple thing. I open a list and I want to see who is subscribed and who isn’t. I therefore click the status button to sort that list by status. And BINGO – the list is gone and I am again working with the entire database of customers.



Ufff





[Reply](https://fluentcrm.com/docs/advanced-filter/?replytocom=4637#respond)

1. Hi Carla, looks like this is a site-specific issue. Please reach out to our support for help.





      [Reply](https://fluentcrm.com/docs/advanced-filter/?replytocom=4642#respond)
3. Hi Nazir,



I want use the advanced filter with woocommerce, but I can’t choose any, the choise are not active. How can?



With regards,





[Reply](https://fluentcrm.com/docs/advanced-filter/?replytocom=4579#respond)

1. Hi Anneke, Please go to Settings>integration settings and activate WooCommerce sync.





      [Reply](https://fluentcrm.com/docs/advanced-filter/?replytocom=4587#respond)
4. Hello,


i can’t see custom fields option in order to filter people who accepted ” i want to subscribe to the boletin” checkbox to move them all to another list. Or maybe there is a way to add an contact to a diferent list on form submit when an user confirm an checkbox ? I mean, i have one automatization when an user submit the form to add him to a X list, what i want to do is if the user also check a checbox to acept sucribing to our newsletter then add the contact to the list number 2, if user doesn’t acept the checkbox, just add him to the first list



Thank you





[Reply](https://fluentcrm.com/docs/advanced-filter/?replytocom=4021#respond)

1. Hey Sebastian, you may use our dynamic tagging feature(requires Fluent Forms): [https://fluentcrm.com/segment-fluentcrm-contacts-using-dynamic-tags/](https://fluentcrm.com/segment-fluentcrm-contacts-using-dynamic-tags/)





      [Reply](https://fluentcrm.com/docs/advanced-filter/?replytocom=4067#respond)
5. Hello I have issue with advanced filter.


I had created custom fields Radio Choice type or Select List type with the same result trying filter Clients.


Values (Europe, Noth America, Asia …)


I modified a client and indicated North America on those fields.


I use advanced filter, choose one of these Custom fileds and choose “includes in”, value North América and none customer appears as a result.



What I am doing wrong?





[Reply](https://fluentcrm.com/docs/advanced-filter/?replytocom=3797#respond)

6. Was this Advanced Filtering slider removed? I don’t see it on the Contacts page.





[Reply](https://fluentcrm.com/docs/advanced-filter/?replytocom=1928#respond)

1. Hi Zat, Please update to the new version and you should see the slider.





      [Reply](https://fluentcrm.com/docs/advanced-filter/?replytocom=2780#respond)

### Leave a Reply [Cancel reply](https://fluentcrm.com/docs/advanced-filter/\#respond)

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

Newsletter

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

Newsletter

SUBSCRIBE