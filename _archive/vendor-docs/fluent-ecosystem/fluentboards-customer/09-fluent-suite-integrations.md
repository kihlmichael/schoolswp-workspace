# Section Fluent Suite Integrations

Source : docs.fluentboards.com
Date scrape : 2026-05-24

---

## FluentBoards Integration With FluentCRM
URL : https://fluentboards.com/docs/fluentboards-integration-with-fluentcrm/

FluentCRM automatically integrates with FluentBoards. To manage the Tasks of your Projects both Fluent CRM and Fluent Boards offer you some features. 

In this article, we will be explaining those features. 

### **CRM Contacts in** Boards #

FluentBoards allows you to add FluentCRM contacts to your tasks. You can view all CRM contacts associated with your board’s tasks in the Boards menu. 

To view CRM contacts associated with tasks on a board, go to your board and click on the three-dot button in the top right corner to open the board menu. Then, select **Associate CRM Contacts** to see the CRM contacts linked to your board’s tasks.

![associate contact crm contact 1](https://fluentboards.com/wp-content/uploads/2024/05/Associate-Contact-CRM-Contact-1-scaled.webp)

Clicking on the **Arrow** icon button will reveal the tasks associated with those CRM contacts.

![associate with tasks 1 1](https://fluentboards.com/wp-content/uploads/2024/05/Associate-with-Tasks-1-1-scaled.webp)

### **Adding CRM Contacts to Tasks** #

To associate a CRM contact with your task, follow these steps:

Go to the task where you wish to add the CRM contact or create a new task. In the task pop-up, you’ll find the **CRM Contact** button. Click on this button to include the CRM contact in your board.

![How to add CRM contact on a task](https://fluentboards.com/wp-content/uploads/2024/10/Screenshot-2024-10-14-at-4.39.48 PM.webp)

## **Viewing Tasks and Boards Associated with FluentCRM Contacts** #

To observe tasks and boards linked with your FluentCRM contacts, follow these steps:

Head to the **All Contacts** section from the FluentCRM Dashboard. Open the specific contact that has been added to your board.

Select **FluentBoards** within the contact details. Here, you’ll discover all boards and tasks associated with this contact.

![crm contact fluentboards info](https://fluentboards.com/wp-content/uploads/2024/05/CRM-Contact-FluentBoards-Info-scaled.webp)

## FluentCRM Automation #

In Fluent CRM you will get some Automation based on your Board and Task changes. You will get two automation action triggers for boards in FluentCRM those are 

  * **Contact Added to Task:** This Automation will run when a contact will be added to a task. 
  * **Stage Changed:** This automation will run when the stage of a task changes. 


![automations fluentcrm](https://fluentboards.com/wp-content/uploads/2024/09/Automations-FluentCRM.webp)

## Automation Action #

Here you will get a **Create Task** action for your FluentBoards. You can set this **Create Task** action to create a new task in your FluentBoards.

![FluentBoards Task Create Action ](https://fluentboards.com/wp-content/uploads/2024/05/Edit-Funnel-FluentCRM.webp)

Now, a pop-up will appear where you can fill in the necessary details.

**A. Internal label:** Enter a unique and clear task name. 

**B. Internal Description:** Add a short description to help you or your team understand the purpose of this task within the automation setup.

**C. Select Board & its stage: **Choose the board where the task should be created. Then, select the specific stage where the task will be placed.

**D. Task Title:** Enter the task title. For additional options, you can insert dynamic shortcodes by clicking the **three-dot** icon.

**E. Due Date:** Set a due date for the task using the **plus (+)** or **minus (-)** icons to adjust the date as needed.

**F. Description:** You can write out the task details in the description field. For dynamic content, click on **Add Smartcode** to insert smart data automatically.

**G. Select Priority:** From the dropdown options, select the priority level for your task: **Low** , **Medium** , or **High**. If no priority is selected, it will default to **Low** automatically.

Once you have completed all the details, click the **Save Settings** button to save and apply your automation task to the board.

![create task](https://fluentboards.com/wp-content/uploads/2024/05/Create-Task-scaled.webp)

That’s all about FluentCRM integration with FluentBoards. If you have any further queries about this article feel free to [reach us](https://wpmanageninja.com/support-tickets/?utm_source=wpmn&utm_medium=home&utm_campaign=site#/).

---

## FluentBoards Integration with Fluent Forms
URL : https://fluentboards.com/docs/fluentboards-integration-with-fluent-forms/

Suppose you have a form on your website from where you want to add a task on your FluentBoards Board. Now you can easily add this task to your board with the Fluent Forms by following a very simple process. Here We will show you how you can configure this integration of FluentBorads with Fluent Form. 

## Enable FluentBoards Modules #

To integrate FluentBoards with Fluent Forms you need to go to the Fluent Forms **Integration** and then activate the **FluentBoards Module**. Toggle to enable the Fluent Boards Module. 

![fluentboards module in fluentform](https://fluentboards.com/wp-content/uploads/2024/05/FluentBoards-Module-in-FluentForm-scaled.webp)

## Integration with Form #

Now go to the Specific Form where you want to integrate the FluentBoards. Go to the **Settings & Integration** of that form and click on **Configure Integration**. 

Here you will find the **Add New Integration** button select it. Now you will see the **FluentBoards Integration** here, click on it to open the _FluentBoards Integration Feed_. 

![fluentboards integration with forms](https://fluentboards.com/wp-content/uploads/2024/05/FluentBoards-Integration-With-Forms-scaled.webp)

## Configure FluentBoards Integration Feed #

Now here you need to configure your **FluentBoards Integration Feed** to add a Task from your Fluent Forms to FluentBoard. 

**A. FluentBoards configuration:** In the FluentBoards configuration fields, you can select Board, Stage, Labels, Assignees, Priority, and FluentCRM Contact from the dropdown list.

**B. Task Title:** Here you can select a Fluent Forms field with the Shortcode to add as a Task Title.

**C. Submitter Name:** Select the user name field Shortcode to get the Submitter Name.

**D. Submitter Email:** You can gather the Submitter’s Email using Shortcode, which will be matched with a contact in the CRM. If the email belongs to a CRM contact, they will be automatically linked with the task.

**E. Description:** Description will be added as Task Description.

**F. Task Position:** You can select the Task Position in the stage from here.

**G. Due Date:** Set a due date for the task using the **Plus (+)** or **Minus (-)** icons to adjust the date as needed.

**H.** **FluentCRM:** Enable the **Create FluentCRM Contact** option to automatically create a new contact in FluentCRM if the submitter’s email does not already exist in your contact list.

**I.** **Files/Attachments:** Enable the **Map Files/Attachments To Task** option to automatically link uploaded files with the corresponding task during form submission.

**J. Conditional Logics:** Enable the **Conditional Logic** option to run this integration only when certain conditions are met based on the form submission values.

**K. Status:** Enable this feed if you want to create a Task with this Form.

Click on the **Save Feed** button to save this FluentBoards Integration Feed. 

![form integration setup](https://fluentboards.com/wp-content/uploads/2024/05/Form_Integration_Setup-793x1024.png)form integration setup

Now, your task will be automatically generated upon form submission and placed into the board and stage you’ve chosen.

If you have any further questions, concerns, or suggestions related to this integration please do not hesitate to contact our [@support team](https://wpmanageninja.com/support-tickets/?utm_source=wpmn&utm_medium=home&utm_campaign=site#/).

---

## FluentBoards Integration with FluentSupport
URL : https://fluentboards.com/docs/fluentboards-integration-with-fluentsupport/

You can create a task directly from your Fluent Support Tickets. If any Tickets come in your Fluent Support your support agent can add that Tickect as a task on your Fluent Boards. 

The integration of Fluent Board and Fluent Support is straightforward. You just need to install both plugins on your site. In this article, we will demonstrate the whole thing. 

## **Adding Task from Fluent Support Ticket** #

Go to the Fluent Support Tickets and then open the specific ticket you want to add to your FluentBoards task. 

In your ticket, you will see a three-dot button on the top right corner of your ticket. Now click on that **three-dot** button and you will see **Add Task to FluentBoards** select it.

![customer support ](https://fluentboards.com/wp-content/uploads/2024/05/Customer-Support-1-scaled.webp)

Your **Task Title** will be automatically chosen from your Ticket subject field and the Ticket description will be added as a task description. 

Here, you’ll find the option to choose the **Board** , **Stage** , **and Date** from the **Dropdown** menu, and the task will automatically be added to the bottom of that stage. Fluent Support Agents can only view the boards to which they have access.

![can t log into my account ](https://fluentboards.com/wp-content/uploads/2024/05/Can-t-Log-into-My-Account--scaled.webp)

> If the ticket opener is a FluentCRM User, they’ll be automatically linked to the task as an Associated CRM contact.

If you need to make further changes to the task, simply open it from your FluentBoards. From there, you can add assignees, set priorities, add labels, adjust dates, and make any other necessary adjustments.

![fluentboards task added from support ticket](https://fluentboards.com/wp-content/uploads/2024/05/FluentBoards-Dev-Team-FluentBoards-scaled.webp)

This outlines all the options available to integrate your Fluent support with Fluent Boards. If you have any additional questions regarding this integration, don’t hesitate to reach out to [us](https://wpmanageninja.com/support-tickets/?utm_source=wpmn&utm_medium=home&utm_campaign=site#/).

---
