# Section Settings, Notifications & Confirmations

Source : docs.fluentforms.com
Date scrape : 2026-05-24

---

## How to Setup Admin/User Email Notifications
URL : https://fluentforms.com/docs/how-to-setup-admin-user-email-notifications/

**Fluent Forms** allows you to send email notifications to the admin and users every time someone fills out a form. You can also inform others besides admin or users (e.g., team members, support agents, moderators, etc.) when the form is filled out. 

This article will guide you through the process of setting up the **Admin/User Email Notification** in **Fluent Forms**.

## Email Notifications for Admin/User #

To learn how to set up admin/user email notifications, follow the steps below – 

First, go to **Forms** from the top navbar, and **open** the **Editor** page of your **desired form** by clicking the **Edit** button where you want to set the Email Notification.

![1. desired Form Editor 3 scaled 46115](https://fluentforms.com/wp-content/uploads/2024/12/1.-desired-Form-Editor-3-scaled.webp)

Now, go to **Settings & Integrations** from the top navbar and open the **Email Notifications** tab.

Here, you can see one **Admin Notification Email** is already created by default. You can use it by **enabling the toggle** button and edit by clicking the **Settings Icon**. 

Or, you can **Create** a new one by clicking the **\+ Add Notification** button. **For example** , I created a new notification to show you the whole process of adding email notifications for Admin/User. 

![2. Settings Integration Email Notification Add new notification 2 scaled 46115](https://fluentforms.com/wp-content/uploads/2024/12/2.-Settings-Integration-Email-Notification-Add-new-notification-2-scaled.webp)

Once you are on the **Email Notifications** page, fill in all the necessary settings as per your needs, click the **Save Notification** button, and your admin/user notification will be set.

![3. Email Notfications Page scaled 46115](https://fluentforms.com/wp-content/uploads/2024/12/3.-Email-Notfications-Page-scaled.webp)

**All the settings mentioned above are briefly explained below:**

> **Remember** , **all** **the** **settings** option functions the same for both the **Admin** and**User** email notifications **except** the **“Send To”** setting.

### A. Name #

Here, provide a name for your email notification to find it easily later. 

### B. Send To #

Here, you will get three options for setting up the **Email Notification**. These are:

  * **Enter Email:** Use this option to set up the email notification for the Admin.
  * **Select a Field:** Use this option to set up the email notification for the Users.
  * **Configure Routing:** Use this set up additional [Conditional Email Routing](https://fluentforms.com/docs/conditional-email-routing/)**.**


## Setup Admin Notification Using Enter Email #

By default, the `{wp.admin_email}` shortcode is available to send emails to the site admin. This shortcode will automatically use the default admin email set in your WordPress settings.

If you prefer to specify a different admin email manually, choose the **Enter Email** option in the **Send To** field and input the desired email address.

You can also send notifications to multiple recipients by separating email addresses with a comma (,).

![Email Notifications Admin scaled 46115](https://fluentforms.com/wp-content/uploads/2025/04/Email-Notifications-Admin-scaled.webp)

## Setup User Notification Using Select a Field #

Now, select the **Select a Field** option in the **Send To** field and define an **Email** input field in your form whose value will receive the confirmation email.

You can select the **Email** field by clicking the **drop-down arrow** beside the **Send To Field**.

![5. Select a Field option 46115](https://fluentforms.com/wp-content/uploads/2024/12/5.-Select-a-Field-option.webp)

### C. Subject #

Here, you can set a subject for your email notification. You can also add data from submitted entries through the input fields using the **Three-dot-icon** dropdown list in the right corner.

![6. Subject option 46115](https://fluentforms.com/wp-content/uploads/2024/12/6.-Subject-option.webp)

### D. Email Body #

Here, you can set the body for your email according to your requirements.

You can use the **Add Shortcodes** drop-down arrow on the right corner to add dynamic data.   
Also for advanced customization, you can edit the email body in **HTML Codes** through the **Text** tab.

![7. Email Body option 46115](https://fluentforms.com/wp-content/uploads/2024/12/7.-Email-Body-option.webp)

#### Send Email as Raw HTML Format #

Similar to the **Text** tab, this option lets you send the email body in **HTML format**. Here, click the**Note Icon** in the right corner to add the desired ShortCode/s.

![8. Send email as Raw HTML Format 46115](https://fluentforms.com/wp-content/uploads/2024/12/8.-Send-email-as-Raw-HTML-Format.webp)

### E. Conditional Logics #

Enabling this option allows you to set specific conditions for sending email notifications to the admin, ensuring notifications are sent only when the conditions are met.

> To learn more detail use of this Conditional Logics, read this [Documentation](https://fluentforms.com/docs/set-up-forms-with-conditional-logic-in-fluent-forms/).

![9. Conditional Logics 46115](https://fluentforms.com/wp-content/uploads/2024/12/9.-Conditional-Logics.webp)

### F. Media File Attachments #

**Fluent Forms** allows you to send **PDF/Image Attachment/s** to the email notification using the **Media File Attachments** option. Also, you can delete any file by clicking the Trash Icon anytime if needed.

> You should use SMTP so send the attachment via email otherwise, It may go to spam.

![10. Media File Attachments option 46115](https://fluentforms.com/wp-content/uploads/2024/12/10.-Media-File-Attachments-option.webp)

### G. Advanced #

Use this setting if you want to configure someone else who also needs to be notified of an entry submission (your teammates, support staff, etc).

  * **From Name & Email:** Here, you can specify the**sender name** and **email** in the **From Name** and **From Email** fields respectively. Plus, you can add different dynamic data by clicking **Shortcode** **Icon**.


  * **Reply To** : Here, you can **specify an email address for users to reply to the notification** , ensuring you receive their responses. If you leave this field blank, the user reply will be sent to the Default Email you set for your site. 


  * **BCC & CC**: Here, you can add an **email address in the CC or BCC** if you want to send a copy of the email to another person. Use a Comma in between each email address to add more than one receiver.


Finally, click the **Save Notification** button when you complete all the setup.

![11. Advanced option 46115](https://fluentforms.com/wp-content/uploads/2024/12/11.-Advanced-option.webp)

If you have any further questions, concerns, or suggestions, please do not hesitate to contact our [@support team](https://wpmanageninja.com/support-tickets/?utm_source=wpmn&utm_medium=home&utm_campaign=site#/).

---

## Setup Form Submission Confirmation Message in Fluent Forms
URL : https://fluentforms.com/docs/setup-form-submission-confirmation-message-in-fluent-forms/

**Fluent Forms** allows you to send a **Default/Customized** **Confirmation Message** after each form submission to let the users know their form was submitted successfully. This article will guide you through setting up the **Confirmation Message** in **Fluent Forms**.

## Confirmation Settings #

To set up a customized form submission confirmation message, follow the steps below – 

First, go to **Forms** from the top navbar, and open the **Editor** page of your desired form**** by clicking the **Edit** button where you want to set the notifications, or you can create a new form. 

![1. desired Form Editor 4 scaled 46165](https://fluentforms.com/wp-content/uploads/2024/12/1.-desired-Form-Editor-4-scaled.webp)

Now, go to **Settings & Integrations** from the top navbar and open the **Confirmation Settings** tab under the **Settings** option.

Here, you can see three **Confirmation Types** for setting up the**Confirmation Message**. These are:

  1. Same Page
  2. To a Page
  3. To a Custom URL


Once you complete the setup, click the **Save Settings** button to save all your changes.

![2. Confirmation Settings option scaled 46165](https://fluentforms.com/wp-content/uploads/2024/12/2.-Confirmation-Settings-option-scaled.webp)

**All three confirmation types mentioned above are briefly explained below:**

### 1\. Same page #

This option is selected by default. It enables you to show the confirmation message on the same page where the form is embedded.

**A. Message to show** : Here, you can see a default confirmation message. You can keep it or customize it as per your needs. You can also add **Shortcode/s** and**Media/s** in your confirmation message by using the **Add Media** and**Add Shortcodes** button in the right corner. Also for advanced customization, you can edit the message in **HTML Codes** through the **Text** tab.

**B. After Form Submission** : Here, you can select whether you want to **Hide** or **Reset** the Form after each form submission. 

Finally, click the **Save Settings** button to save all your changes.

![3. Same Page confirmation type 46165](https://fluentforms.com/wp-content/uploads/2024/12/3.-Same-Page-confirmation-type.webp)

### 2\. To a Page #

The option allows you to redirect your subscribers to a designated page on your website after they submit the form, enhancing their experience by guiding them to relevant content or further actions. This could be a**Customized Welcome Page** , your **Home Page** , or **Any Other Page** on your site. 

**A. Select Page:** Here, choose the desired page you want your subscriber to be redirected to after form submission by clicking the **Arrow Icon**. Here you will find your website’s all pages in this dropdown list.

**B. Redirect Query String** : Enabling this option allows you to pass the field data via a query string (checkbox, currently unchecked). Here also you can redirect queries through **Shortcode** by clicking the **Three-dot Icon** in the right corner.

**C. Redirection Message** : Here, you can customize the message displayed after form submission. You can also add **Shortcode/s** and**Media/s** in your confirmation message by using the **Add Media** and**Add Shortcodes** button in the right corner. Also for advanced customization, you can edit the message in **HTML Codes** through the **Text** tab.

Once you are done, click the **Save Settings** button to save all your changes.

![4. To a Page confirmation type 46165](https://fluentforms.com/wp-content/uploads/2024/12/4.-To-a-Page-confirmation-type.webp)

### 3\. To a Custom URL #

This confirmation type allows you to redirect your subscriber to a page/website that is not in your domain through a custom URL.

**A. Custom URL** : Here, put the desired **Outbound URL** where you want your subscriber redirected after form submission. Here you can also add **Shortcode/s** by clicking the left side **three-dot-icon.**

**B. Redirect Query String** : Enabling this option allows you to pass the field data via a query string (checkbox, currently unchecked). Here also you can redirect queries through **Shortcode** by clicking the **Three-dot Icon** in the right corner. 

Suppose you have a form with a field like **Name**. If you enable **Pass Field Data via Query String** , after the form submission, the URL could look like: https://yourwebsite.com/thank-you/?name=JohnDoe

  * Here, ‘name=JohnDoe’ is passed through the query string.
  * You can then use this information on the next page for personalization or tracking.


**C. Redirect Message** : Here, you can customize the message displayed after form submission. You can also add **Shortcode/s** and**Media/s** in your confirmation message by using the **Add Media** and**Add Shortcodes** button in the right corner. Also for advanced customization, you can edit the message in **HTML Codes** through the **Text** tab.

> If you want to pass data using a query string and automatically populate form fields on the redirected page, follow this [documentation](https://fluentforms.com/docs/set-default-form-value-from-url-parameters/).

Once you are done, click the **Save Settings** button to save all your changes.

![5. To a Custom URL confirmation Type 46165](https://fluentforms.com/wp-content/uploads/2024/12/5.-To-a-Custom-URL-confirmation-Type.webp)

If you have any further questions, concerns, or suggestions, please do not hesitate to contact our [@support team](https://wpmanageninja.com/support-tickets/?utm_source=wpmn&utm_medium=home&utm_campaign=site#/).

---

## Set up Forms with Conditional Logic in Fluent Forms
URL : https://fluentforms.com/docs/set-up-forms-with-conditional-logic-in-fluent-forms/

[Alternative Heading: Use Conditional Logic in Input Fields with Fluent Forms] 

**Fluent Forms** offers the **Conditional Logic** feature inside **Input Fields** to **display** /hide them based on specific conditions in your forms. This article will guide you through using **[Conditional Logic](https://fluentforms.com/docs/set-up-forms-with-conditional-logic-in-fluent-forms/)** in any **Input Fields** with**Fluent Forms**.

## Enabling Conditional Logic in a Field #

To learn how to use conditional logic in a specific form, follow the steps with the screenshots below – 

First, go to the **Forms** from the **Fluent Forms Navbar** or**WordPress Left Sidebar,** and **open** the **Editor** page of your **desired form** by clicking the **Edit** button where you want to use the **Conditional Logic** feature.

> If you do not have any existing forms, read [Create a Form from Scratch](https://fluentforms.com/docs/how-to-create-a-form-with-fluent-forms/) or [Create a Form using Templates](https://fluentforms.com/docs/using-and-customizing-pre-built-quick-forms-in-fluent-forms/) documentation to create a new one.

For example, I chose an existing form to show the whole process.

![1. Open Desired form scaled 46609](https://fluentforms.com/wp-content/uploads/2025/03/1.-Open-Desired-form-scaled.webp)

Once you open the **Editor** page, choose the desired **Input Field** that you want to **hide/display** based on the set condition/s. **For example** , I selected the [Payment Method](https://fluentforms.com/docs/add-payment-method-field-in-payment-forms/) field to show you the process.

Now, hover over the chosen field, click the **Pencil/Edit** Icon, and you’ll be taken to the **Input** **Customization** tab on the left side.

Then, open the **Advanced Options** by clicking the **Arrow Icon** , scroll down to **Conditional Logic** , and select the **Yes** button.

![2. Input Customization scaled 46609](https://fluentforms.com/wp-content/uploads/2025/03/2.-Input-Customization-scaled.webp)

## Conditional Match #

Once you enable the **Conditional Logic** option, a **Conditional Match** option will appear with Three major conditionals. These are:

**A. Any** : If you choose this option, the form user must meet at least one of the set conditions during form submission to trigger the specified actions. 

**B. All** : If you choose this option, the form user must meet all the set conditions during form submission to trigger the specified actions. 

**C. Group** : This advanced option allows you to **create multiple conditions within groups**. Unlike the “**Any** ” or “**All** ” options, which determine whether all or just one condition must be met, the “**Group** ” option lets you set one group of conditions against another using the “**OR** ” operator. This means that an action will be triggered if at least one group of conditions is met. “Also, you can **Name** your **Groups** according to your preference.

### Fields to set Conditions #

Once you select the **Conditional Match** , you can specify the **Parameter** , its **Operator** , and the corresponding **Value** to set condition/s.

In the “**Parameter** ” field (first field), select an **input field** that needs to correspond with the value provided in the “**Value** ” field (last field) and set an option in the “**Operator** ” field (middle field). The parameter will trigger the action if the condition is met. 

To add as many conditions as you need, click the **Plus Icon,** and to delete any conditions, click the **Minus Icon** in the right corner. 

Once you complete it, click the **Save Form** button to make the condition/s functional. To see the preview, click the **Preview & Design** button. 

![3. Conditional Match scaled 46609](https://fluentforms.com/wp-content/uploads/2025/03/3.-Conditional-Match-scaled.webp)

## Example of Each Conditional Match #

To provide you with an in-depth understanding, all three conditional matches are explained with detailed examples below – 

### A. Any Conditional Match #

**For example** , I selected **“Email”** and **“Payment Item”** as the parameters, used **“includes”** and **“equals”** as the operators, and entered **“@gmail.com”** and **“Fluent Forms”** as the corresponding values.

As I have selected the “**Any** ” conditional match here, when users either provide an email address containing **“@gmail.com”** or select**** the “**Fluent Forms”** product to submit the form, the **Payment Method** field will be visible to them. Otherwise, this field will remain hidden.

![4. Any conditional 46609](https://fluentforms.com/wp-content/uploads/2025/03/4.-Any-conditional.webp)

Here is a **preview** of a form where the user met one **(selecting Fluent Forms product)** condition. As a result, the **Payment Method** field is visible here. 

![5. Preview of Any condional scaled 46609](https://fluentforms.com/wp-content/uploads/2025/03/5.-Preview-of-Any-condional-scaled.webp)

### B. All Conditional Match #

**For example** , I selected **“Email”** and **“Payment Item”** as the parameters, used **“includes”** and **“equals”** as the operators, and entered **“@gmail.com”** and **“Fluent Forms”** as the corresponding values.

As I have selected the “**All** ” conditional match here, when users both provide an email address containing **“@gmail.com”** and select the “**Fluent Forms”** product to submit the form, the **Payment Method** field will be visible to them. Otherwise, this field will remain hidden. 

![6. All condional 46609](https://fluentforms.com/wp-content/uploads/2025/03/6.-All-condional.webp)

Here is a **preview** of a form where the user met all the **( providing email that includes @gmail.com and selecting Fluent Forms product)** conditions. As a result, the **Payment Method** field is visible here.

![7. Preview of All Conditional 46609](https://fluentforms.com/wp-content/uploads/2025/03/7.-Preview-of-All-Conditional.webp)

### C. Group Conditional Match #

Here, I selected the “Group” conditional match and set two different Groups of Conditions using the OR operator. So that, when users meet any one of the Group Conditions, the field will be visible in the form.

**For example** , in Group 1, I selected **“Email”** and **“Payment Item”** as the parameters, used **“includes”** and **“equals”** as the operators, and entered **“@gmail.com”** and **“Fluent Forms”** as the corresponding values.

On the contrary, in Group 2, I selected “**Name [First Name]** ”, **“Email”** and **“Payment Item”** as the parameters, used “**starts with** ”, **“includes”** and **“equals”** as the operators, and entered “**Z** ”, **“@gmail.com”** and **“Fluent Forms”** as the corresponding values.

As I have selected the “**Group** ” conditional match here, when users meet either the conditions in **Group 1**(i.e., provide an email address containing “**@gmail.com** ” and select the “**Fluent Forms** ” product) or the conditions in **Group 2** (i.e., enter a first name starting with “**Z** ,” provide an email address containing “**@yahoo.com** ,” and select the “**Fluent Forms** ” product), the **Payment Method** field will be visible to them. Otherwise, the field will remain hidden.

![8. Group Conditional 46609](https://fluentforms.com/wp-content/uploads/2025/03/8.-Group-Conditional.webp)

Here is a **preview** of a form where the user met**All Conditions** under**Group 1** **(** providing an email address including**“@gmail.com”** and**** selecting**** the**“Fluent Forms”** product**)**. As a result, the **Payment Method** field is visible here.

![9. Preview of Group one codinitional 46609](https://fluentforms.com/wp-content/uploads/2025/03/9.-Preview-of-Group-one-codinitional.webp)

Here is a **preview** of a form where the user met **All Conditions** under**Group 2** (entering first name starting**** with**“Z”** , providing an email address including**“@gmail.com”** , and selecting**** the**“Fluent Forms”** product) condition. As a result, the **Payment Method** field is visible here. 

![10. Preview of Group two Conditionals 46609](https://fluentforms.com/wp-content/uploads/2025/03/10.-Preview-of-Group-two-Conditionals.webp)

This way, you can easily use Conditional Logic in any field of Fluent Forms!   
If you have any further questions, concerns, or suggestions, please do not hesitate to contact our [support team](https://wpmanageninja.com/support-tickets/?utm_source=wpmn&utm_medium=home&utm_campaign=site#/). Thank you.

---
