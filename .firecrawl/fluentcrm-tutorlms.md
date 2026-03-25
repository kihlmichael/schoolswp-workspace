[Skip to content](https://fluentcrm.com/docs/tutorlms-integration-with-fluentcrm#main)

Special [20% Discount](https://fluentcrm.com/deal/?utm_source=fcrmsite&utm_medium=banner&utm_campaign=special26&utm_id=special+deal) on Email Automation

[Start Automation](https://fluentcrm.com/deal/?utm_source=fcrmsite&utm_medium=banner&utm_campaign=special26&utm_id=special+deal)

All CategoriesGetting StartedGlobal SettingsFluentCRM EssentialsContactsEmailsFormsAutomationsEvent TrackingReportsPlugins Integration & AutomationMigrating from Other PlatformsBounce HandlersMiscellaneousDeveloper DocumentationFrequently Asked QuestionsChange Log

Popular Searchautomationtheunsubscribewebhookcustom

View Categories

6 min read

Table of Contents

- [Integration Settings](https://fluentcrm.com/docs/tutorlms-integration-with-fluentcrm#integration-settings-)
- [Course Tag settings in TutorLMS](https://fluentcrm.com/docs/tutorlms-integration-with-fluentcrm#course-tag-settings-in-tutorlms)
- [TutorLMS Automation](https://fluentcrm.com/docs/tutorlms-integration-with-fluentcrm#tutorlms-automation)
- [Action Blocks](https://fluentcrm.com/docs/tutorlms-integration-with-fluentcrm#action-blocks)
- [Goals](https://fluentcrm.com/docs/tutorlms-integration-with-fluentcrm#goals)
- [Condition](https://fluentcrm.com/docs/tutorlms-integration-with-fluentcrm#condition)
- [Advanced Filtering Option in FluentCRM](https://fluentcrm.com/docs/tutorlms-integration-with-fluentcrm#advanced-filtering-option-in-fluentcrm)
- [Advanced Reports](https://fluentcrm.com/docs/tutorlms-integration-with-fluentcrm#advanced-reports)

TutorLMS is one of the most popular LMS plugins for WordPress. If you have created an eLearning course platform on WordPress using TutorLMS, FluentCRM can help you automate your course marketing with activity monitoring contact segmentation, email marketing, and more. Follow these simple steps to integrate FluentCRM with TutorLMS.

## Integration Settings [\#](https://fluentcrm.com/docs/tutorlms-integration-with-fluentcrm\#integration-settings-)

To enable the integration and sync TutorLMS with FluentCRM, go to **Settings** and select **Integration Settings** from the left sidebar, then choose TutorLMS. Here, you can assign a default list, tag, and contact status to update TutorLMS students’ information in FluentCRM, allowing you to segment contacts effectively. Use the dropdown menus to select the desired tags, lists, and statuses.

Click on the **Sync TutorLMS Students** button to update the existing student data and automatically segment future students based on the selected tag, list, and contact status.

![image](https://fluentcrm.com/wp-content/uploads/2021/07/image-66.png)

## Course Tag settings in TutorLMS [\#](https://fluentcrm.com/docs/tutorlms-integration-with-fluentcrm\#course-tag-settings-in-tutorlms)

FluentCRM allows you to capture your TutorLMS students as leads and automatically segment them based on course-specific tags. To do this, navigate to the **TutorLMS Course Edit** section then scroll down to find the **FluentCRM – Course Tag** option, and apply the appropriate tags to students enrolling in the course. This makes it easy to organize and target your communications within FluentCRM.

![fluentcrm tags for course](https://fluentcrm.com/wp-content/uploads/2021/07/FluentCRM-tags-for-course.webp)

## TutorLMS Automation [\#](https://fluentcrm.com/docs/tutorlms-integration-with-fluentcrm\#tutorlms-automation)

FluentCRM also lets you automate tasks such as sending behavioral emails, email sequences, contact property updates, and many more.

FluentCRM’s email marketing automation includes four major elements. These are:

1. **Triggers:** Triggers are essential for initiating email marketing automation. They can be behavior-based, or time-based. Learn more about FluentCRM’s [Triggers](https://fluentcrm.com/docs/fluentcrm-automation-triggers/).

2. **Action Blocks:** The actions that will be done throughout the funnel for example sending an email, adding the user to a list, etc. Learn everything about FluentCRM [Action Blocks](https://fluentcrm.com/docs/primary-automation-actions/).

3. **Goals:** Benchmarking the behavior of the users for example whether they purchased a product, clicked on a link, etc. Learn everything about FluentCRM [Benchmark Blocks](https://fluentcrm.com/docs/goals-or-benchmark-actions/).

4. **Conditionals:** Conditionals will let you set multiple paths based on if/else conditions. Learn more about [FluentCRM Conditionals](https://fluentcrm.com/docs/conditional-automation-actions/).

First, from your FluentCRM dashboard & go to the **Automation** from the navbar. Then click the **New Automation** button to add an automation funnel.

![new automation](https://fluentcrm.com/wp-content/uploads/2021/07/New-Automation.webp)

A pop-up window will appear, where you have to add an Internal Label and choose the trigger that will initiate an automation funnel. You can choose one from three available TutorLMS Triggers.

- **Enrollment in a Course:** This will let you trigger an automation funnel when someone enrolls in a TutorLMS course.
- **Student Completes a Course:** This will let you trigger an automation funnel when someone completes a TutorLMS course.
- **Students Complete a Lesson:** This will let you trigger an automation funnel when students complete a lesson.

Now select a trigger and click the **Continue** button.

![tutorlms trigger](https://fluentcrm.com/wp-content/uploads/2021/07/tutorlms-trigger.webp)

A new popup will appear, allowing you to customize the Automation’s name and Internal description. Next, select the desired **subscription status**.

In the **Condition** section, you can set specific rules for your automation funnel. For example, you can determine what happens if a contact already exists or doesn’t exist within the automation. You’ll have two options to choose from: **Update if Exists** or **Skip the Automation if Contact Already Exists**. This allows you to control how existing contacts are handled in your automated workflows.

If you want to restart automation for the same contacts then select **Restart the Automation Multiple Times for this Event** checkbox.

Click the **Save Setting** button to save all your changes.

![tutorlms trigger in fluentcrm](https://fluentcrm.com/wp-content/uploads/2021/07/TutorLms-trigger-in-FluentCRM.webp)

After setting up your trigger, you can design your marketing automation workflow using Actions, Goals, and Conditions.

## Action Blocks [\#](https://fluentcrm.com/docs/tutorlms-integration-with-fluentcrm\#action-blocks)

[Actions blocks](https://fluentcrm.com/docs/basics-of-automation-actions/) are tasks that you wish to trigger from your side. Click on the plus icon on the Automation Funnel page.

![tutorlms actions goal](https://fluentcrm.com/wp-content/uploads/2021/07/Tutorlms-actions-goal.webp)

Then you will notice a pop-up with a set of action blocks to choose from. You can select any type of action block to automate your workflows.

FluentCRM offers two specific action blocks designed for TutorLMS marketing automation.

**Enroll to Course:** The **Enroll To Course** action enrolls a contact to a specific LMS course.

**Remove From a Course:** The **Remove From a Course** action removes a contact from a specific LMS course

![tutorlms two trigger in fluentcrm](https://fluentcrm.com/wp-content/uploads/2021/07/TutorLMS-two-Trigger-in-FluentCRM.webp)

After selecting the TutorLMS actions a pop-up will appear from the right side. Here enter the Internal Lable name, Internal Description. Now choose the specific TutorLMS course for enrollment.

If you don’t want to enroll the existing WordPress users in the action then simply check this **Do not enroll the course if contact is not an existing WordPress user** option. Now click **Save Settings**.

![enroll action in tutorlms](https://fluentcrm.com/wp-content/uploads/2021/07/enroll-action-in-tutorlms.webp)

## Goals [\#](https://fluentcrm.com/docs/tutorlms-integration-with-fluentcrm\#goals)

[Goals blocks](https://fluentcrm.com/docs/goals-or-benchmark-actions/) are goal or action items that your user might do. They let you measure these steps and automate the funnel based on goal completion. Click on the plus icon(+) to open the pop-up to select the Goals.

![tutorlms goals in fluentcrm](https://fluentcrm.com/wp-content/uploads/2021/07/TutorLMS-goals-in-FluentCRM.webp)

Here you can choose any goals. In these Goals, you can add an internal label, specify the lists for the goal, set the condition when it will run, and choose Benchmark Type. After that click the **Save Settings** button.

![goal list apply](https://fluentcrm.com/wp-content/uploads/2021/07/goal-list-apply.webp)

## **Condition** [\#](https://fluentcrm.com/docs/tutorlms-integration-with-fluentcrm\#condition)

[Conditionals](https://fluentcrm.com/docs/conditional-automation-actions/) are conditional logic. If you want to automate different activities based on If/Else conditions, you can choose a conditional. For TutorLMS, FluentCRM allows you to automate different activities based on whether a student in the automation has enrolled in a course.

If you want to use other conditionals please check out this [documentation](https://fluentcrm.com/docs/conditional-automation-actions/).

![tutorlms conditional in fluentcrm](https://fluentcrm.com/wp-content/uploads/2021/07/TutorLMS-Conditional-in-FluentCRM.webp)

Once you’ve completed these steps, you’ll see a report of your course enrollment contacts, similar to the screenshot below.

![course contact details](https://fluentcrm.com/wp-content/uploads/2021/07/Course-Contact-details-1.webp)

## Advanced Filtering Option in FluentCRM [\#](https://fluentcrm.com/docs/tutorlms-integration-with-fluentcrm\#advanced-filtering-option-in-fluentcrm)

With the help of advanced filtering, you can use various key data points such as last **enrollment date**, **first enrollment data**, **courses enrolled**, **enrolled categories**, and **enrollment tags**. it can be as simple as checking whether a contact is a student or not. That makes it easy to send hyper-targeted emails and run automation.

Now you can filter your course data go to your FluentCRM contact section then click the Advanced filter to do filters. Next, click on the add button to start filtering data.

![start lms advanced filter](https://fluentcrm.com/wp-content/uploads/2021/07/start-LMS-Advanced-filter.webp)

Here you must select TutorLMS and then click any of the filter options. You can pick multiple options to filter your LMS data.

- Last Enrollment Date
- First Enrollment Date
- Enrollment Course
- Enrollment Categories
- Enrollment Tags
- Is a Student

After that click the Filter button to filter your TutorLMS data.

![advanced filtering tutorlms](https://fluentcrm.com/wp-content/uploads/2021/07/Advanced-Filtering-tutorlms.webp)

## Advanced Reports [\#](https://fluentcrm.com/docs/tutorlms-integration-with-fluentcrm\#advanced-reports)

To view your course enrollment report, go to the FluentCRM dashboard and select the **Reports** section from the top menu. Then, click the **TutorLMS** tab to access detailed information about your enrolled contacts and their courses.

![tutorlms reports](https://fluentcrm.com/wp-content/uploads/2021/07/TutorLMS-Reports.webp)

So here is the entire process of integrating TutorLMS with FluentCRM. If you have any questions then feel free to contact our [support](https://wpmanageninja.com/support-tickets/) team.

##### What are your Feelings

#### Share This Article :

- [![Facebook](https://fluentcrm.com/wp-content/plugins/betterdocs/assets/images/social/facebook.svg?v=4.3.7)](https://www.facebook.com/sharer/sharer.php?u=https://fluentcrm.com/docs/tutorlms-integration-with-fluentcrm/)
- [![X](https://fluentcrm.com/wp-content/plugins/betterdocs/assets/images/social/twitter.svg?v=4.3.7)](https://twitter.com/intent/tweet?url=https://fluentcrm.com/docs/tutorlms-integration-with-fluentcrm/)
- [![LinkedIn](https://fluentcrm.com/wp-content/plugins/betterdocs/assets/images/social/linkedin.svg?v=4.3.7)](https://www.linkedin.com/shareArticle?mini=true&url=https://fluentcrm.com/docs/tutorlms-integration-with-fluentcrm/)
- [![Pinterest](https://fluentcrm.com/wp-content/plugins/betterdocs/assets/images/social/pinterest.svg?v=4.3.7)](https://pinterest.com/pin/create/button/?url=https://fluentcrm.com/docs/tutorlms-integration-with-fluentcrm/)

[Still stuck? How can we help?](https://fluentcrm.com/docs/tutorlms-integration-with-fluentcrm#betterdocs-form-modal)

## How can we help?

Name: \*

Email: \*

Message: \*

Updated on December 3, 2024

[LifterLMS Integration with FluentCRM](https://fluentcrm.com/docs/lifterlms-integration-with-fluentcrm/) [LearnPress integration with FluentCRM](https://fluentcrm.com/docs/learpress-integration-with-fluentcrm/)

### Leave a Reply [Cancel reply](https://fluentcrm.com/docs/tutorlms-integration-with-fluentcrm/\#respond)

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

Contact

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

Subscribe

SUBSCRIBE