# Section Actions & Filters Hooks

Source : dev.fluentboards.com
Date compile : 2026-05-24


---

## FluentBoards Action Hooks
Source file : `src/hooks/actions\index.md`

# FluentBoards Action Hooks

<Badge type="tip" vertical="top" text="FluentBoards Core" /> <Badge type="warning" vertical="top" text="Intermediate" />

FluentBoards has many interesting filter hooks that let developers change default settings and even extend FluentBoards with
new functionality.

## What are Action Hooks

Action hooks are used to run custom code when certain events occur.
 
## Available of Action Hooks in FluentBoard

### Board Specific
<hr />

::: details fluent_boards/board_created
This action runs when a board has been created

**Parameters**
- `$board` Board Model

**Usage:**
```php 
add_action('fluent_boards/board_created', function($board) {
   // Do whatever you want
}, 10, 1);
```
:::

::: details fluent_boards/board_find
This action runs when a board is invoked

**Parameters**
- `$board` Board Model

**Usage:**
```php 
add_action('fluent_boards/board_find', function($board) {
   // Do whatever you want
}, 10, 1);
```
:::

::: details fluent_boards/board_updated
This action runs when a board is updated

**Parameters**
- `$board` Board Model
- `$oldBoard` Board Model

**Usage:**
```php 
add_action('fluent_boards/board_updated', function($board, $oldBoard) {
   // Do whatever you want
}, 10, 2);
```
:::

::: details fluent_boards/board_label_created
This action runs when a label is created in a board

**Parameters**
- `$label` Label Model

**Usage:**
```php 
add_action('fluent_boards/board_label_created', function($label) {
   // Do whatever you want
}, 10, 1);
```
:::

::: details fluent_boards/board_label_updated
This action runs when a label is updated in a board

**Parameters**
- `$label` Label Model

**Usage:**
```php 
add_action('fluent_boards/board_label_updated', function($label) {
   // Do whatever you want
}, 10, 1);
```
:::

::: details fluent_boards/board_label_deleted
This action runs when a label is deleted in a board

**Parameters**
- `$label` Label Model

**Usage:**
```php 
add_action('fluent_boards/board_label_deleted', function($label) {
   // Do whatever you want
}, 10, 1);
```
:::

::: details fluent_boards/board_stages_reordered
This action runs when a stage is moved

**Parameters**
- `$boardId` `int` Board id
- `$stageIds` `array` List of stage ids

**Usage:**
```php 
add_action('fluent_boards/board_stages_reordered', function($boardId, $stageIds) {
   // Do whatever you want
}, 10, 2);
```
:::

::: details fluent_boards/stage_archived
This action runs when a stage is archived

**Parameters**
- `$boardId` `int` Board id
- `$stage` `object`  Stage object

**Usage:**
```php 
add_action('fluent_boards/stage_archived', function($boardId, $stage) {
   // Do whatever you want
}, 10, 2);
```
:::

::: details fluent_boards/board_member_added
This action runs when a member is added to board

**Parameters**
- `$boardId` `int` Board id
- `$boardMember` `object`  User object

**Usage:**
```php 
add_action('fluent_boards/board_member_added', function($boardId, $boardMember) {
   // Do whatever you want
}, 10, 2);
```
:::

::: details fluent_boards/task_archived
This action runs when a task is archived

**Parameters**
- `$task` `object` Task object

**Usage:**
```php 
add_action('fluent_boards/task_archived', function($task) {
   // Do whatever you want
}, 10, 1);
```
:::

::: details fluent_boards/stage_updated
This action runs when a stage's title or background color is updated

**Parameters**
- `$boardId` `int` Board id
- `$updatedStage` `object` Stage object after update
- `$oldStage` `object` Stage object before update

**Usage:**
```php 
add_action('fluent_boards/stage_updated', function($boardId, $updatedStage, $oldStage) {
   // Do whatever you want
}, 10, 3);
```
:::

### Task Specific
<hr />

::: details fluent_boards/task_created
This action runs when a task is created

**Parameters**
- `$task` `object` Task 

**Usage:**
```php 
add_action('fluent_boards/task_created', function($task) {
   // Do whatever you want
}, 10, 1);
```
:::

::: details fluent_boards/task_deleted
This action runs when a task is deleted

**Parameters**
- `$task` `object` Task

**Usage:**
```php 
add_action('fluent_boards/task_deleted', function($task) {
   // Do whatever you want
}, 10, 1);
```
:::

::: details fluent_boards/task_stage_updated
This action runs when stage of a task is updated

**Parameters**
- `$task` `object` Task
- `$oldStageId` `int` stage id

**Usage:**
```php 
add_action('fluent_boards/task_stage_updated', function($task, $oldStageId) {
   // Do whatever you want
}, 10, 2);
```
:::

::: details fluent_boards/comment_created
This action runs when comment is added to a task

**Parameters**
- `$comment` `object` Comment

**Usage:**
```php 
add_action('fluent_boards/comment_created', function($comment) {
   // Do whatever you want
}, 10, 1);
```
:::

::: details fluent_boards/comment_updated
This action runs when a comment is updated

**Parameters**
- `$comment` `object` Comment
- `$oldComment` `object` Comment before updated

**Usage:**
```php 
add_action('fluent_boards/comment_updated', function($comment, $oldComment) {
   // Do whatever you want
}, 10, 2);
```
:::

::: details fluent_boards/comment_deleted
This action runs when a comment is deleted

**Parameters**
- `$comment` `object` Comment

**Usage:**
```php 
add_action('fluent_boards/comment_deleted', function($comment) {
   // Do whatever you want
}, 10, 1);
```
:::

::: details fluent_boards/task_added_from_fluent_form
This action runs when a task is added from fluent form plugin

**Parameters**
- `$task` `object` Task

**Usage:**
```php 
add_action('fluent_boards/task_added_from_fluent_form', function($task) {
   // Do whatever you want
}, 10, 1);
```
:::

::: details fluent_boards/task_assignee_added
This action runs when a assignee is added to a task

**Parameters**
- `$task` `object` Task
- `$assigneeId` `int` id of the user

**Usage:**
```php 
add_action('fluent_boards/task_assignee_added', function($task, $assigneeId) {
   // Do whatever you want
}, 10, 2);
```
:::

::: details fluent_boards/task_assignee_removed
This action runs when a assignee is removed from a task

**Parameters**
- `$task` `object` Task
- `$assigneeId` `int` id of the user

**Usage:**
```php 
add_action('fluent_boards/task_assignee_removed', function($task, $assigneeId) {
   // Do whatever you want
}, 10, 2);
```
:::

::: details fluent_boards/task_start_date_changed
This action runs when start date of a task is changed

**Parameters**
- `$task` `object` Task
- `$oldStartDateValue` `datetime` format `YYYY-MM-DD HH:MM:SS`

**Usage:**
```php 
add_action('fluent_boards/task_start_date_changed', function($task, $oldStartDateValue) {
   // Do whatever you want
}, 10, 2);
```
:::

::: details fluent_boards/task_due_date_changed
This action runs when due date of a task is changed

**Parameters**
- `$task` `object` Task
- `$oldDueDateValue` `datetime` format `YYYY-MM-DD HH:MM:SS`

**Usage:**
```php 
add_action('fluent_boards/task_due_date_changed', function($task, $oldDueDateValue) {
   // Do whatever you want
}, 10, 2);
```
:::

::: details fluent_boards/task_deleted
This action runs when a task has been deleted

**Parameters**
- `$task` `object` Task

**Usage:**
```php 
add_action('fluent_boards/task_deleted', function($task) {
   // Do whatever you want
}, 10, 1);
```
:::

---

## Filters  /  _Dashboard_Filters
Source file : `src/hooks/filters\_dashboard_filters.md`

<explain-block title="fluent_crm/dashboard_stats">
If you want to add or remove dashboard stats cards then you can use this filter.

**Parameters**

- `$stats` Array - Dashboard stats cards as containing each `stat`

```php
$stat = [
    'title' => 'Stat Title',
    'count' => 1234,
    'route' => [
        'name' => 'dashboard' // fluentcrm route to reditect once click. Leave blank if not route
    ]
];
```

**Usage:**

```php 
/*
* Add Own Stat
*/
add_filter('fluent_crm/dashboard_stats', function($stats) {
   $stats['my_stat_key'] = [
        'title' => 'Stat Title',
        'count' => 1234
   ];
   return $stats;
});
```
</explain-block>

<explain-block title="fluent_crm/quick_links">
if you want to customize quick links of FluentCRM Dashboard then use this hook.

**Parameters**

- `$links` Array - Dashboard stats cards as containing each `$link`

```php
$link = [
    'title' => 'Link Title',
    'url'   => 'https://domain.com/path-to-link',
    'icon'  => 'el-icon-user' // optional
]; 
```

**Usage:**

```php 
/*
* Add Own Link
*/
add_filter('fluent_crm/quick_links', function($links) {
   $links[] = [
        'title' => 'Link Title',
        'url'   => 'https://domain.com/path-to-link',
        'icon'  => 'el-icon-user' // optional
   ];
   return $links;
});
```
</explain-block>

<explain-block title="fluent_crm/dashboard_notices">
If you want to show notices to FluentCRM admin panel then you may use this hook.

**Parameters**

- `$notices` Flat Array

**Usage:**

```php 
/*
* Add Custom Notice
*/
add_filter('fluent_crm/dashboard_notices', function($notices) {
   $notices[] = '<p>My Custom Notice Here</p>';
   return $notices;
});
```
</explain-block>

<explain-block title="fluent_crm/sales_stats">
If you want to add custom sales stats on FluentCRM Dashboard widget then use this hook.


**Parameters**

- `$stats` Array

**Usage:**

```php 
/*
* Add Custom Sales Stat
*/
add_filter('fluent_crm/sales_stats', function($stats) {
  $stats[] = [
        'title' => 'Custom Stat Title',
        'content' => 'Stat Content'
  ];
  
  return $stats;
});
```
</explain-block>

---

## Filters  /  _Frontend_Filters
Source file : `src/hooks/filters\_frontend_filters.md`

<explain-block title="fluent_crm/unsubscribe_texts">
If you want to customize the labels on Unsubscribe page then you can use this filter hook.

**Parameters**

- `$texts` Array - Labels and texts of the unsubscribe page form
- `$subscriber` Subscriber Model - Current Subscriber who is unsubscribing now

```php
$texts = [
  'heading'             => __('Unsubscribe', 'fluent-crm'),
  'heading_description' => __('We\'re sorry to see you go!', 'fluent-crm'),
  'email_label'         => __('Your Email Address', 'fluent-crm'),
  'reason_label'        => __('Please let us know a reason', 'fluent-crm'),
  'button_text'         => __('Unsubscribe', 'fluent-crm')
];
```

**Usage:**

```php 
/*
* Alter Button Text of Unsubscribe form
*/
add_filter('fluent_crm/unsubscribe_texts', function($texts, $subscriber) {
   $texts['button_text'] = 'Unsubscribe (No email updates)';
   return $texts;
}, 10, 2);
```

</explain-block>

<explain-block title="fluent_crm/unsub_response_message">
After a contact unsubscribe and if you want to change the response message programmatically you may use this hook.

**Parameters**

- `$message` String - After Unsubscribe Response Message
- `$subscriber` Subscriber Model - Current Subscriber who is unsubscribing now

**Usage:**

```php 
/*
* Change Unsubscribe Response Text
*/
add_filter('fluent_crm/unsub_response_message', function($message, $subscriber) {
   return 'You are unsubscribed and no further email will be sent';
}, 10, 2);
```

</explain-block>

<explain-block title="fluent_crm/unsub_redirect_url">
After a contact unsubscribe and if you want to redirect the contact programmatically then you can use this hook

**Parameters**

- `$redirectUrl` String URL - After Unsubscribe Redirect URL
- `$subscriber` Subscriber Model - Current Subscriber who is unsubscribing now

**Usage:**

```php 
/*
* Change Unsubscribe Redirect URL
*/
add_filter('fluent_crm/unsub_redirect_url', function($redirectUrl, $subscriber) {
   return 'https://domain.com/path-to-my-custom-redirect';
}, 10, 2);
```

</explain-block>

<explain-block title="fluent_crm/double_optin_options">
After Double Optin Confirmation, if you want to change the default behavior (like redirect to a different URL or show
different content) then you can use this filter hook

**Parameters**

- `$config` Array - Settings of the default response config including redirect URL
- `$subscriber` Subscriber Model - Current Subscriber who is unsubscribing now

```php
$config = [
  'after_confirmation_type' => 'redirect', // or message
  'after_confirm_message'     => 'MESSAGE_DEFINED_IN_SETTINGS',
  'after_conf_redirect_url'   => 'URL DEFINED IN SETTINGS',
];
```

**Usage:**

```php 
/*
* Redirect to custom URL after DOI confirmation
*/
add_filter('fluent_crm/double_optin_options', function($config, $subscriber) {
   $config['after_confirmation_type'] = 'redirect';
   $config['after_conf_redirect_url'] = 'https://domain.com/path-to-confirm-page';
   return $config;
}, 10, 2);
```
</explain-block>

<explain-block title="fluent_crm/pref_labels">
Manage Subscription Page Labels Filter Hook

**Parameters**

- `$labels` - Manage Subscription Page Labels

```php
$labels = [
    'first_name'      => __('First Name', 'fluent-crm'),
    'last_name'       => __('Last Name', 'fluent-crm'),
    'prefix'          => __('Title', 'fluent-crm'),
    'email'           => __('Email', 'fluent-crm'),
    'phone'           => __('Phone/Mobile', 'fluent-crm'),
    'dob'             => __('Date of Birth', 'fluent-crm'),
    'address_line_1'  => __('Address Line 1', 'fluent-crm'),
    'address_line_2'  => __('Address Line 2', 'fluent-crm'),
    'city'            => __('City', 'fluent-crm'),
    'state'           => __('State', 'fluent-crm'),
    'postal_code'     => __('ZIP Code', 'fluent-crm'),
    'country'         => __('Country', 'fluent-crm'),
    'update'          => __('Update info', 'fluent-crm'),
    'address_heading' => __('Address Information', 'fluent-crm'),
    'list_label'      => __('Mailing List Groups', 'fluent-crm'),
];
```

**Usage:**

```php 
/*
* Alter Labels of the form
*/
add_filter('fluent_crm/pref_labels', function($labels) {
    $labels['update'] = 'Update My Profile';
    return $labels;
});
```
</explain-block>

<explain-block title="fluent_crm/pref_form_fields">

Manage Subscription Shortcode Fields customization Hook

**Parameters**

- `$formFields` - Manage Subscription Form Fields Array
- `$subscriber` - Current Subscriber

**Usage:**

```php 

add_filter('fluent_crm/pref_form_fields', function($formFields, $subscriber) {
   // Customize the $formFields and return
   
   return $formFields;
}, 10, 2);
```
</explain-block>

<explain-block title="fluent_crm/show_unsubscribe_on_pref">
By Default FluentCRM does not show unsubscribe button on Manage Subscription Page

**Parameters**

- `$status` - Boolean

**Usage:**

```php 
// Show Unsubscribe Button on Manage Subscription Page
add_filter('fluent_crm/show_unsubscribe_on_pref', function($status) {
   return true;
});
```
</explain-block>

<explain-block title="fluent_crm/double_optin_email_subject">
You can customize the double optin email subject from settings page but if you want to alter that then you can use this hook.

**Parameters**

- `$emailSubject` - String
- `$subscriber` - Subscriber Model

**Usage:**

```php 
add_filter('fluent_crm/double_optin_email_subject', function($emailSubject, $subscriber) {
   // do you staff
   
   return $emailSubject;
}, 10, 2);
```
</explain-block>

<explain-block title="fluent_crm/double_optin_email_body">
You can customize the double optin email body from settings page but if you want to alter that then you can use this hook.

**Parameters**

- `$emailBody` - String
- `$subscriber` - Subscriber Model

**Usage:**

```php 
add_filter('fluent_crm/double_optin_email_body', function($emailBody, $subscriber) {
   // do you staff
   
   return $emailBody;
}, 10, 2);
```
</explain-block>

---

## Filters  /  _General_Filters
Source file : `src/hooks/filters\_general_filters.md`

<explain-block title="fluent_crm/disable_global_search">
By Default FluentCRM provides you a search bar when for easily search contacts and access FluentCRM pages. If you want to remove this feature you can use this hook

**Parameters**
- `$status` Boolean - Default false

**Usage:**
```php 
/*
* Disable FluentCRM search on admin bar
*/
add_filter('fluent_crm/disable_global_search', function($status) {
   return true;
});
```
</explain-block>

<explain-block title="fluent_crm/will_auto_unsubscribe">
By Default FluentCRM ask the reason to unsubscribe but if you want to disable that and automatically unsubscribe without showing the form then you can use this hook

**Parameters**
- `$status` enum - 'yes' or 'no', Default 'no'

**Usage:**
```php 
/*
* Automatically unsubscribe in one click 
*/
add_filter('fluent_crm/will_auto_unsubscribe', function($status) {
   return 'yes';
});
```
</explain-block>

<explain-block title="fluent_crm/will_use_cookie">
By Default FluentCRM set cookie when someone click a link to track further actions like purchase and track revenue for that email campaign / sequence / automation.

**Parameters**
- `$status` boolean

  **Usage:**
  ::: warning Attention
  If you use the code snippet, no revenue report will be recorded
    ```php 
     /*
     * Disable Cookie 
     */
     add_filter('fluent_crm/will_use_cookie', function($status) {
        return false;
     });
    ```
</explain-block>

<explain-block title="fluent_crm/is_simulated_mail">
If you want to simulate all email sending from FluentCRM then you can use this hook.

**Parameters**
- `$status` boolean
- `$data` Email Data
- `$headers` Email Headers
**Usage:**

**Attention**
If you use the code snippet, no email will be sent from FluentCRM

 ```php
    /*
    * Disable Email 
    */
    add_filter('fluent_crm/is_simulated_mail', function($status) {
       return true;
    });
```
</explain-block>

<explain-block title="fluent_crm/countries">
If you alter the country lists of FluentCRM then you may use this filter.

**Parameters**
- `$countries` Array

**Usage:**

```php 
add_filter('fluent_crm/countries', function($countires) {
  // Process the conutries
  
  return $countries;
}, 20); // priority need to be greated than 10
```
</explain-block>

---

## Filters  /  _Other_Filters
Source file : `src/hooks/filters\_other_filters.md`

<explain-block title="fluent_crm/enable_unsub_header">
By Default FluentCRM include unsubscribe header to marketing emails. If you don't want to include the unsubscribe-list header, you can use this hook.

**Parameters**
- `$status` Boolean - Default false

**Usage:**
```php 
/*
* Disable FluentCRM Unsubscribe-List header
*/
add_filter('fluent_crm/enable_unsub_header', function($status) {
   return false;
});
```
</explain-block>

<explain-block title="fluent_crm/email_headers">
If you want to add custom email (mime) header you can use this hook

**Parameters**
- `$headers` array 
- `$data` array - Email Data

**Usage:**
```php 
/*
* Add Custom Header to FluentCRM Email Mime
*/
add_filter('fluent_crm/email_headers', function($headers, $data) {
   // Add or remove headers
   
   return $headers;
}, 10, 2);
```
</explain-block>

<explain-block title="fluent_crm/enable_mailer_to_name">
By Default FluentCRM include name of the contact when sending emails for better deliverability, if you want to disable that, you can use this hook

**Parameters**
- `$status` Boolean - Default false

**Usage:**
```php 
/*
* Disable FluentCRM Name to Email
*/
add_filter('fluent_crm/enable_mailer_to_name', function($status) {
   return false;
});
```
</explain-block>

<explain-block title="fluent_crm/user_permissions">
You can customize the user's permission set from FluentCRM settings page. But if you want to customize that from code level you can use this hook.

**Parameters**
- `$permissions` Flat Array - Permission Array
- `$wpUser` \WP_User - WordPress User

**Usage:**
```php 
/*
* Customize Permissions
*/
add_filter('fluent_crm/user_permissions', function($permissions, $wpUser) {
   // Customize the permission for specific user and then return
   return $permissions;
}, 10, 2);
```
</explain-block>

<explain-block title="fluent_crm/default_email_design_template">
If you want to change the default email design template, you may use this hook.

**Parameters**
- `$designTemplateSlug` string - Default 'simple'

**Usage:**
```php 
/*
* Change Email Template Type to classic
*/
add_filter('fluent_crm/default_email_design_template', function($designTemplateSlug) {
   return 'classic';
});
```
</explain-block>

<explain-block title="fluent_crm/contact_name_prefixes">
By Default FluentCRM name prefixes are `Mr`, `Mrs` and `Ms`, You want to remove or add your own name prefixes here.

**Parameters**
- `$namePrefixes` array 

**Usage:**
```php 
/*
* Add More Name Prefixes
*/
add_filter('fluent_crm/contact_name_prefixes', function($namePrefixes) {
   $namePrefixes[] = 'Dr';
   $namePrefixes[] = 'Engg.';
   
   return $namePrefixes;
});
```
</explain-block>

<explain-block title="fluent_crm/woo_purchase_sidebar_html">
When you view a contact then it shows related woocommerce data for the contact. You may customize that here

**Parameters**
- `$sidebarHtml` string - HTML
- `$subscriber` Subscriber Model
- `$pageNumber` INT - Pagination Page Number

**Usage:**
```php 
/*
* Add Custom Data to sidebar HTML of Contact Woo Summary
*/
add_filter('fluent_crm/woo_purchase_sidebar_html', function($sidebarHtml, $subscriber, $pageNumber) {
   if(!$sidebarHtml) {
        return ''; // No info found
   }
   
   $sidebarHtml .= '<p>My custom info</p>';
}, 20, 3);
```
</explain-block>

<explain-block title="fluent_crm/edd_purchase_sidebar_html">
When you view a contact then it shows related Easy Digital Downloads data for the contact. You may customize that here

**Parameters**
- `$sidebarHtml` string - HTML
- `$subscriber` Subscriber Model
- `$pageNumber` INT - Pagination Page Number

**Usage:**
```php 
/*
* Add Custom Data to sidebar HTML of Contact EDD Summary
*/
add_filter('fluent_crm/edd_purchase_sidebar_html', function($sidebarHtml, $subscriber, $pageNumber) {
   if(!$sidebarHtml) {
        return ''; // No info found
   }
   
   $sidebarHtml .= '<p>My custom info</p>';
}, 20, 3);
```
</explain-block>

---

## Filters  /  _Webhook_Filters
Source file : `src/hooks/filters\_webhook_filters.md`

<explain-block title="fluent_crm/incoming_webhook_data">
If you want to intercept incoming Webhook before it's get validated and processed you can use this hook to format the data.

**Parameters**
- `$postData` array - Posted data on the webhook
- `$webhook` Webhook Model
- `$request` Request Object

**Usage:**
```php 
/*
* Customize Webhook data for webhook id: 1
*/
add_filter('fluent_crm/incoming_webhook_data', function($postedData, $webhook) {
   if($webhook->id != 1) {
        return $postedData;
   }
   
   // Customize your $postedData and return
   
    return $postedData;
}, 10, 3);
```
</explain-block>

<explain-block title="fluent_crm/webhook_contact_data">
FluentCRM Webhook data has been formatted at this point. If you want to alter the contact data and associated tags, lists, statuses, etc. You may use this hook

**Parameters**
- `$data` Array - Formatted Contact data that will be used to create or update a contact
- `$postedData` Array - Original Post Data
- `$webhook` Related Webhook Model

**Usage:**

```php 
add_filter('fluent_crm/webhook_contact_data', function($data, $postedData, $webhook) {
    // Customize the $data and return
    
    return $data;
}, 10, 3);
```
</explain-block>

---

## FluentBoards Filter Hooks
Source file : `src/hooks/filters\index.md`

# FluentBoards Filter Hooks

<Badge type="tip" vertical="top" text="FluentBoards Core" /> <Badge type="warning" vertical="top" text="Intermediate" />

FluentBoards has many interesting filer hooks that let developers change default settings and even extend FluentBoards with new functionality.

## What are Filter Hooks

A hook is a feature that allows developers to manipulate functionality without modifying core files. A hook can help developers inject some functions or edit default settings.
  
Filter hooks are used to return modified values for certain parameters, based on different factors.

## Available Filter Hooks <hr/>

<explain-block title="fluent_boards/board_find">
When you find a board it returns a board object. But if you want to manipulate that board data and return
modified board object then you can use this filter.

**Parameters**
- `$board` Object

**Usage:**
```php 
/*
* Manipulate board object
*/
add_filter('fluent_boards/board_find', function($board) {
   return $board;
});
```
</explain-block>

<explain-block title="fluent_boards/before_create_board">
But if you want to modify board data before create that board then you can use this filter.

**Parameters**
- `$boardData` Object

**Usage:**
```php 
/*
* Manipulate board data before task create
*/
add_filter('fluent_boards/before_create_board', function($boardData) {
   return $boardData;
});
```
</explain-block>

<explain-block title="fluent_boards/before_task_create">
But if you want to modify task data before create that task then you can use this filter.

**Parameters**
- `$data` Object

**Usage:**
```php 
/*
* Manipulate task data before task create
*/
add_filter('fluent_boards/before_task_create', function($data) {
   return $data;
});
```
</explain-block>

<explain-block title="fluent_boards/uploaded_file_name_prefix">
But if you want to modify uploaded file name prefix then you can use this filter.

**Parameters**
- `$prefix` String

**Usage:**
```php 
/*
* Modify uploaded file name prefix
*/
add_filter('fluent_boards/uploaded_file_name_prefix', function($prefix) {
   return $prefix;
});
```
</explain-block>

<explain-block title="fluent_boards/incoming_webhook_data">
But if you want to modify incoming webhook data then you can use this filter.

**Parameters**
- `$postData` Array
- `$webhook` String

**Usage:**
```php 
/*
* Modify incoming webhook data
*/
add_filter('fluent_boards/incoming_webhook_data', function($postData, $webhook) {
   return $postData;
});
```
</explain-block>

<explain-block title="fluent_boards/webhook_task_data">
But if you want to modify webhook task data then you can use this filter.

**Parameters**
- `$postData` Array
- `$webhook` String

**Usage:**
```php 
/*
* Modify webhook task data
*/
add_filter('fluent_boards/webhook_task_data', function($postData, $webhook) {
   return $postData;
});
```
</explain-block>

<explain-block title="fluent_boards/site_logo">
But if you want to change site logo then you can use this filter.

**Parameters**
- `$logo_url` String

**Usage:**
```php 
/*
* Change site logo
*/
add_filter('fluent_boards/site_logo', function($logo_url) {
   return $logo_url;
});
```
</explain-block>

<explain-block title="fluent_boards/addons_settings">
But if you want to modify addon data in features and module settings then you can use this filter.

**Parameters**
- `$addOns` Array

**Usage:**
```php 
/*
* Modify addon data in features and module settings
*/
add_filter('fluent_boards/addons_settings', function($addOns) {
   return $addOns;
});
```
</explain-block>

<explain-block title="fluent_boards/accepted_plugins">
But if you want to modify accepted free plugins then you can use this filter.

**Parameters**
- `$acceptedFreePlugins` Array

**Usage:**
```php 
/*
* Modify accepted free plugins
*/
add_filter('fluent_boards/accepted_plugins', function($acceptedFreePlugins) {
   return $acceptedFreePlugins;
});
```
</explain-block>

<explain-block title="fluent_boards/save_general_settings">
But if you want to modify general settings before save then you can use this filter.

**Parameters**
- `$settings` Array

**Usage:**
```php 
/*
* Modify general settings before save
*/
add_filter('fluent_boards/save_general_settings', function($settings) {
   return $settings;
});
```
</explain-block>

<explain-block title="fluent_boards/email_footer">
But if you want to modify email footer then you can use this filter.

**Parameters**
- `$footer_text` String

**Usage:**
```php 
/*
* Modify email footer
*/
add_filter('fluent_boards/email_footer', function($footer_text) {
   return $footer_text;
});
```
</explain-block>

<explain-block title="fluent_boards/email_header">
But if you want to modify email header then you can use this filter.

**Parameters**
- `$email_header` String

**Usage:**
```php 
/*
* Modify email header
*/
add_filter('fluent_boards/email_header', function($email_header) {
   return $email_header;
});
```
</explain-block>

<explain-block title="fluent_boards/task_priorities">
If you want to modify task priorities then you can use this filter.

**Parameters**
- `$priorities` Array - 'high', 'medium', 'low'

**Usage:**
```php
/*
* Modify task priorities
*/
add_filter('fluent_boards/task_priorities', function($priorities) {
    $priorities['urgent'] = __('Urgent', 'fluent-boards');
    return $priorities;
});
```
</explain-block>

<explain-block title="fluent_boards/task_tabs">
If you want to modify the order of activity, comment log in task modal then you can use this filter.

**Parameters**
- `$tabs` Array - 'all', 'comment', 'activity'

**Usage:**
```php
/*
* Modify task tabs
*/
add_filter('fluent_boards/task_tabs', function($tabs) {
    $reorderedTabs = [
        'activity' => $tabs['activity'], //1st 
        'comment' => $tabs['comment'], //2nd
        'all' => $tabs['all'], //3rd  
    ];
    
    return $reorderedTabs;
});
```
</explain-block>


<explain-block title="fluent_boards/board_menu_items">
Modify board menu items. This filter runs when the board menu is loaded and allows you to customize the sidebar menu that appears on the right side of the board.

**Parameters**
- `$menuItems` Array - Array of existing menu items with their properties (key, label, type, position, etc.)
- `$board_id` Integer - The current board ID

**Menu Item Structure:**
```php
[
    'key' => 'unique_identifier',        // Required: Unique key for the menu item
    'label' => 'Menu Label',             // Required: Display text
    'type' => 'default|custom',          // Required: Item type
    'position' => 13,                    // Optional: Position in menu (lower = higher)
    'icon' => '<svg>...</svg>',          // Required for custom items: SVG icon HTML
    'html' => '<div>Content</div>',      // Required for custom items: HTML content
    'width' => '500px',                  // Optional: Modal/drawer width
    'render_in' => 'drawer|modal',       // Optional: 'drawer' (default) or 'modal' to open as popup modal
    'role' => 'manager|admin'            // Optional: Required user role
]
```

**Usage:**
```php
/*
* Modify board menu items
*/
add_filter('fluent_boards/board_menu_items', function($menuItems, $board_id) {
   // Add custom menu item (will open in drawer by default)
   $menuItems['my_custom_item'] = [
       'key' => 'my_custom_item',
       'label' => 'My Custom Item',
       'type' => 'custom',
       'position' => 13,
       'icon' => '<svg width="16" height="16" viewBox="0 0 16 16" fill="currentColor"><path d="M8 1a7 7 0 100 14A7 7 0 008 1zM3.5 8a4.5 4.5 0 119 0 4.5 4.5 0 01-9 0z"/></svg>',
       'html' => '<div>Custom content</div>', // Required for custom items
       'width' => '500px',
       'render_in' => 'drawer' // or 'modal' for popup modal
   ];
   
   return $menuItems;
}, 10, 2);
```

</explain-block>

<explain-block title="fluent_boards/menu_items">
If you want to modify the menu items ( add new menu or remove/replace existing ones) in FluentBoards, you can use this filter.

**Parameters**
- `$menuItems` Array

**Usage:**
```php
/*
* Modify menu items
*/
add_filter('fluent_boards/menu_items', function($menuItems) {
   // your modification logic here

   return $menuItems;
});
```
</explain-block>

---
