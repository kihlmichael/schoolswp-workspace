# Section Core Business Modules & Logic

Source : dev.fluentboards.com
Date compile : 2026-05-24


---

## Board
Source file : `src/modules/boards.md`

# Board
In FluentBoards, a board is the central organizational structure that acts as a digital workspace where all tasks, ideas,
and projects are visualized and managed. It’s essentially the canvas on which you can plan, organize, and track the progress of your work.

## Creating a board
If you want to create a board:
```php
FluentBoardsApi('boards')->create($boardData);
```
`FluentBoardsApi()` this is fluent-boards global api function. You need to pass `'boards'` argument to access all board related api.
`create()` method is used to create a new board. This function takes `$boardData` as an argument which must be an associative array.

```php
$boardData = [
    'title'           => 'Test Board',
    'description'     => 'test board description',
];
```
`$boardData` can have `title` and `description` initially but `title` is required.

## Getting boards
```php
FluentBoardsApi('boards')->getBoards();
```
`getBoards()` method is used to get boards. This method can have some optional parameters

**Parameters**
- $with `array` - default value empty array `[]`
- $sortBy `string` - default value `'title'`
- $sortOrder `string` - default value `'asc'`

**Return** `array`

## Getting stages of a board
```php
FluentBoardsApi('boards')->getStages($boardId);
```
**Parameters**
- $boardId `int` required

## Getting labels of a board
```php
FluentBoardsApi('boards')->getLabels($boardId);
```
**Parameters**
- $boardId `int` required

## Creating label of a board
```php
FluentBoardsApi('boards')->createLabel($boardId, $labelData);
```
**Parameters**
- $boardId `int` required
- $labelData `array` required

```php
$labelData = [
    'bg_color'  => '#4bce97',
    'color'     => '#1B2533',
    'title'     => 'important'
];
```
Here `bg_color` indicates background color of label, `color` indicates text color and `title` indicates title of the label. `bg_color` is required.

---

## Automation
Source file : `src/modules/index.md`

# Automation

The automation module is a powerful tool for creating and managing complex workflows. It allows you to create workflows
that can be triggered by different events and run some actions till the workflow reaches to a benchmark. FLuentCRM provides a set of predefined
events that you can use to trigger
your workflows. You can also create your own custom action and trigger to reach a benchmark. Now, you can see there are three
different types of automation in FluentCRM. They are trigger, action and benchmark. We will go through each of them one by one.
## Trigger vs Action vs Benchmark
### Trigger
When a user or subscriber does something it's a trigger. Let's say a user subscribes to your newsletter. This is a trigger.
Trigger is the first step of an automation. It's the event that starts the automation.
### Action
When your application does something it's an action.
An action is a task that you want to perform when a trigger happens. For example,
when a user subscribes to your newsletter, you can send a welcome email to the user. This is an action.
You can also create a custom action to perform any task you want. For example, you can create an action that will add a tag to a user when they subscribe to your newsletter.

### Benchmark
A benchmark is goal or target that you want to reach. For example, when a user clicks on a link in your email then it's a benchmark.

---

## Navigation Modules
Source file : `src/modules/navigation-modules.md`



---

## Stage
Source file : `src/modules/stages.md`

#  Stage
In FLuentBoards, each board is made up of one or more stages. These stages are normally arranged side by side on the board,
allowing you to see your entire workflow at a glance.

## Creating a stage
If you want to create a stage in a board:
```php
FluentBoardsApi('stages')->create($stageData);
```
`FluentBoardsApi()` this is fluent-boards global api function. You need to pass `'stages'` argument to access all stage related api.
`create()` method is used to create a new stage. This function takes `$stageData` as an argument which must be an associative array.

```php
$taskData = [
    'title'       => 'Test Stage',
    'board_id'    => 1,
    'status'      => 'open'
];
```
- `$taskData['title']` `string` required
- `$taskData['board_id']` `integer` required
- `$taskData['status']` `string` values: `'open'` or `'closed'`, default: `'open'`

## Getting Stages of a Board
```php
FluentBoardsApi('stages')->getStagesByBoard($boardId, $with = []);
```

**Parameters**
- $boardId `int` required
- $with `array`

**Return** `array`

## Getting a task
```php
FluentBoardsApi('stages')->getStage($taskId, $with = []);
```

**Parameters**
- $taskId `int` required
- $with `array`

**Return** `object`

## Updating a stage
```php
FluentBoardsApi('stages')->updateProperty($stageId, $property, $value);
```

**Parameters**
- $stageId `int` required
- $property `string` required, possible values: `'title'` or `'status'` or `'bg_color'`
- $value `string` required

`$value` could be either a value of `title` or `status` or `bg_color`. For `title` it will be a regular 
string, for `status` it must be a string valued either 'open' or 'closed' and for `bg_color` will must be 
color hex code like `'#DAF7A6'`

**Return** `object`

## Archiving a stage
```php
FluentBoardsApi('stages')->archiveStage($stageId);
```

**Parameters**
- $stageId `int` required

**Return** `object`

## Restoring a archived stage
```php
FluentBoardsApi('stages')->restoreStage($stageId);
```

**Parameters**
- $stageId `int` required

**Return** `object`

---

## Task
Source file : `src/modules/tasks.md`

# Task
Tasks are the fundamental units of work within a board. They represent individual item that need to be managed, tracked, or completed.
Tasks are highly versatile and can be customized to hold all the information related to a specific work.

## Creating a Task
If you want to create a task:
```php
FluentBoardsApi('tasks')->create($taskData);
```
`FluentBoardsApi()` this is fluent-boards global api function. You need to pass `'tasks'` argument to access all task related api.
`create()` method is used to create a new task. This function takes `$taskData` as an argument which must be an associative array.

```php
$taskData = [
    'title'       => 'Test Task',
    'board_id'    => 1,
    'stage_id'    => 2,
    'priority'    => 'low',
    'status'      => 'open'
];
```
- `$taskData['title']` `string` required
- `$taskData['board_id']` `integer` required
- `$taskData['stage_id']` `integer` required
- `$taskData['priority']` `string`
- `$taskData['status']` `string`

## Getting Tasks of a Board
```php
FluentBoardsApi('tasks')->getTasksByBoard($boardId, $with = []);
```

**Parameters**
- $boardId `int` required
- $with `array` 

**Return** `array`

## Getting a task
```php
FluentBoardsApi('tasks')->getTask($taskId);
```

**Parameters**
- $taskId `int` required

**Return** `object`

## Getting tasks created by an user
```php
FluentBoardsApi('tasks')->getTasksCreatedBy($userId, $with = []);
```

**Parameters**
- $userId `int` required
- $with `array` 

**Return** `array`

## Adding assignees to a task
```php
FluentBoardsApi('tasks')->addAssignees($taskId, $assigneeIds = []);
```

**Parameters**
- $taskId `int` required
- $assigneeIds `array` required

**Return** `boolean`

## Removing assignees from a task
```php
FluentBoardsApi('tasks')->removeAssignees($taskId, $assigneeIds = []);
```

**Parameters**
- $taskId `int` required
- $assigneeIds `array` required

**Return** `boolean`

## Attaching labels to a task
```php
FluentBoardsApi('tasks')->attachLabels($taskId, $labelIds = []);
```

**Parameters**
- $taskId `int` required
- $labelIds `array` required

**Return** `boolean`

## Removing labels from a task
```php
FluentBoardsApi('tasks')->removeLabels($taskId, $labelIds = []);
```

**Parameters**
- $taskId `int` required
- $labelIds `array` required

**Return** `boolean`

---

## Trigger
Source file : `src/modules/trigger.md`

# Trigger
An event or action that initiates a specific automated response, that is what we call a trigger.
For example, when a user subscribes to a newsletter, this action is considered a trigger.
A trigger is the foundation of any automation process, it starts the series of actions that follows. The trigger is the first step of automation.

## Creating a Trigger
Say, you are providing some courses on your plugin. You would like to trigger workflows when a user enrols to a course.
You can use the `course-enrolled` trigger to do that.
Create a class that extends `FluentCrm\App\Services\Funnel\BaseTrigger` class.
```php
<?php
namespace Your\Plugin\Name\Automation;
... 
use FluentCrm\App\Services\Funnel\BaseTrigger;

class CourseEnrolledTrigger extends BaseTrigger {


}
```
We need to override the default constructor method to set the trigger's properties.
Constructor of the class should have the following body:
```php

public function __construct()
{
    $this->triggerName = 'course-enrolled';
    $this->priority = 20;
    $this->actionArgNum = 1;
    parent::__construct();
}
```
The `triggerName` property is the name of the event that will trigger this workflow. For our case, let's name it `course-enrolled`.
The `priority` property is the priority of the action that will be added to the `add_action` function.
The `actionArgNum` property is the number of arguments that will be passed to the callback.
Finally, we need to call the parent constructor.

Now, we need to define getTrigger method. This method should return an array of the trigger settings.

```php
public function getTrigger()
{
    return [
        'category'    => __('Awesome Course', 'your-plugin'),
        'label'       => __('User enroll in a course', 'your-plugin'),
        'description' => __('The will start when a student enroll a course', 'your-plugin')
        'icon'        =>  'fc-icon-wp_new_user_signup',
    ];
}
```

Define the `getFunnelSettingsDefaults` method. This method should return an array of the default settings for the workflow.
```php

public function getFunnelSettingsDefaults()
{
    return [
        'subscription_status' => 'subscribed'
    ];
 }
```

Define the `getSettingsFields` method. This method should return an array of the settings fields that will be displayed in the workflow settings page.
You can customize settings as desired . Visit [Form Field Code Structure](/modules/form-field-code-structure/) for more information.

```php
public function getSettingsFields($funnel)
{
    return [
        'title'     => __('User enroll in a course', 'your-plugin'),
        'sub_title' => __('This will start when a student enroll a course', 'your-plugin'),
        'fields'    => [
            'subscription_status' => [
                'type'        => 'option_selectors',
                'option_key'  => 'editable_statuses',
                'is_multiple' => false,
                'label'       => __('Subscription Status', 'your-plugin'),
                'placeholder' => __('Select Status', 'your-plugin')
            ]
        ]
    ];
}
```
There should be an option to select the particular courses for which the workflow should be triggered.
This can be done by adding `getConditionFields` method.
```php
public function getConditionFields($funnel)
{
    $courseOptions = [
        [
            'id'    => '2',
            'title' => 'Think like a pro in JavaScript'
        ],
        [
            'id'    => '3',
            'title' => 'Master in wordpress plugin development'
        ]
    ];
    return [
        'update_type'  => [
            'type'    => 'radio',
            'label'   => __('If Contact Already Exist?', 'your-plugin'),
            'help'    => __('Please specify what will happen if the subscriber already exist in the database', 'your-plugin'),
            'options' => FunnelHelper::getUpdateOptions()
        ],
        'course_ids'   => [
            'type'        => 'multi-select',
            'label'       => __('Target Courses', 'your-plugin'),
            'help'        => __('Select for which Courses this automation will run', 'your-plugin'),
            'options'     => $courseOptions,
            'inline_help' => __('Keep it blank to run to any Course Enrollment', 'your-plugin')
        ],
        'run_multiple' => [
            'type'        => 'yes_no_check',
            'label'       => '',
            'check_label' => __('Restart the Automation Multiple times for a contact for this event. (Only enable if you want to restart automation for the same contact)', 'fluentcampaign-pro'),
            'inline_help' => __('If you enable, then it will restart the automation for a contact if the contact already in the automation. Otherwise, It will just skip if already exist', 'fluentcampaign-pro')
        ]
    ];
}
```
Let's populate some default values for condition fields with `getConditionDefaults` method.
```php
public function getConditionDefaults()
{
    return [
        'update_type'  => 'update', // skip_all_actions, skip_update_if_exist
        'course_ids'   => [],
        'run_multiple' => 'no'
    ];
}
```
The `handle` method needs to be defined in order for it to be called when the trigger event occurs. We are almost finished with this process.
The method takes two arguments. The first argument is the funnel object and second argument is the array of the arguments that are passed to the callback.
Note that, we must prepare subscriber data.
```php
// ... 
public function handle($funnel, $originalArgs)
{
    // separate the arguments
    $enrollmentReference = $originalArgs[0];
    $courseId = $originalArgs[1];
    $userId = $originalArgs[2];

    // get the funnel settings and conditions
    $settings = $funnel->settings;
    $conditions = $funnel->conditions;
    
    // prepare the subscriber data
    $subscriberData = [
        'email' => '', // required
        'first_name' => '',
        'last_name' => '',
        'status' => $settings['subscription_status']
    ];
    // or, you may use the FluentCRM helper function to prepare the subscriber data
    $subscriberData = FunnelHelper::prepareUserData($userId);

    // check if this funnel is able to process this course and run the automation
    if(!$this->isProcessable($funnel, $courseId, $subscriberData)) {
        return false;
    }
    
    // finally start funnel sequence for this subscriber
    (new \FluentCrm\App\Services\Funnel\FunnelProcessor())->startFunnelSequence($funnel, $subscriberData, [
        'source_trigger_name' => $this->triggerName,
        'source_ref_id' => $courseId // optional
    ]);
    
}
// ...
```
```php
// ...
// check if this funnel is able to process this course and run the automation
private function isProcessable($funnel, $courseId, $subscriberData)
{
    $conditions = $funnel->conditions;
    // check update_type
    $updateType = Arr::get($conditions, 'update_type');
    $subscriber = FunnelHelper::getSubscriber($subscriberData['email']);
    if ($subscriber && $updateType == 'skip_all_if_exist') {
        return false;
    }
    // check the products ids
    if($conditions['course_ids'] && !in_array($courseId, $conditions['course_ids'])) {
        return false;
    }
     // check run_only_one
    if ($subscriber && FunnelHelper::ifAlreadyInFunnel($funnel->id, $subscriber->id)) {
        $multipleRun = Arr::get($conditions, 'run_multiple') == 'yes';
        if ($multipleRun) {
            FunnelHelper::removeSubscribersFromFunnel($funnel->id, [$subscriber->id]);
        } else {
            return false;
        }
    }
    return true;
}
// ...
```
Everything is set and ready to go. Let's look at the full source code.
```php
<?php
namespace Your\Plugin\Name\Automation;
... 
use FluentCrm\App\Services\Funnel\BaseTrigger;
use FluentCrm\App\Services\Funnel\FunnelHelper;
use FluentCrm\Framework\Support\Arr;
use FluentCrm\App\Services\Funnel\FunnelProcessor;

class CourseEnrolledTrigger extends BaseTrigger {

    public function __construct()
    {
        $this->triggerName = 'course-enrolled';
        $this->priority = 20;
        $this->actionArgNum = 3;
        parent::__construct();
    }
    
    public function getTrigger()
    {
        return [
            'category'    => __('Awesome Course', 'your-plugin'),
            'label'       => __('User enroll in a course', 'your-plugin'),
            'description' => __('The will start when a student enroll a course', 'your-plugin')
            'icon'        =>  'fc-icon-wp_new_user_signup',
        ];
    }
    
    public function getFunnelSettingsDefaults()
    {
        return [
            'subscription_status' => 'subscribed'
        ];
     }
     
    public function getSettingsFields($funnel)
    {
        return [
            'title'     => __('User enroll in a course', 'your-plugin'),
            'sub_title' => __('This will start when a student enroll a course', 'your-plugin'),
            'fields'    => [
                'subscription_status' => [
                    'type'        => 'option_selectors',
                    'option_key'  => 'editable_statuses',
                    'is_multiple' => false,
                    'label'       => __('Subscription Status', 'your-plugin'),
                    'placeholder' => __('Select Status', 'your-plugin')
                ]
            ]
        ];
    }
    
    public function getConditionFields($funnel)
    {
        $courseOptions = [
            [
                'id'    => '2',
                'title' => 'Think like a pro in JavaScript'
            ],
            [
                'id'    => '3',
                'title' => 'Master in wordpress plugin development'
            ]
        ];
        return [
            'update_type'  => [
                'type'    => 'radio',
                'label'   => __('If Contact Already Exist?', 'your-plugin'),
                'help'    => __('Please specify what will happen if the subscriber already exist in the database', 'your-plugin'),
                'options' => FunnelHelper::getUpdateOptions()
            ],
            'course_ids'   => [
                'type'        => 'multi-select',
                'label'       => __('Target Courses', 'your-plugin'),
                'help'        => __('Select for which Courses this automation will run', 'your-plugin'),
                'options'     => $courseOptions,
                'inline_help' => __('Keep it blank to run to any Course Enrollment', 'your-plugin')
            ],
            'run_multiple' => [
                'type'        => 'yes_no_check',
                'label'       => '',
                'check_label' => __('Restart the Automation Multiple times for a contact for this event. (Only enable if you want to restart automation for the same contact)', 'fluentcampaign-pro'),
                'inline_help' => __('If you enable, then it will restart the automation for a contact if the contact already in the automation. Otherwise, It will just skip if already exist', 'fluentcampaign-pro')
            ]
        ];
    }
    
    public function getConditionDefaults()
    {
        return [
            'update_type'  => 'update', // skip_all_actions, skip_update_if_exist
            'course_ids'   => [],
            'run_multiple' => 'no'
        ];
    }
    
    public function handle($funnel, $originalArgs)
    {
        // separate the arguments
        $enrollmentReference = $originalArgs[0];
        $courseId = $originalArgs[1];
        $userId = $originalArgs[2];
    
        // get the funnel settings and conditions
        $settings = $funnel->settings;
        $conditions = $funnel->conditions;
        
        // prepare the subscriber data
        $subscriberData = [
            'email' => '', // required
            'first_name' => '',
            'last_name' => '',
            'status' => $settings['subscription_status']
        ];
        // you may use the helper function to prepare the subscriber data
        $subscriberData = FunnelHelper::prepareUserData($userId);
    
        // check if this funnel is able to process this course and run the automation
        if(!$this->isProcessable($funnel, $courseId, $subscriberData)) {
            return false;
        }
        
        // finally start funnel sequence for this subscriber
        (new \FluentCrm\App\Services\Funnel\FunnelProcessor())->startFunnelSequence($funnel, $subscriberData, [
            'source_trigger_name' => $this->triggerName,
            'source_ref_id' => $courseId // optional
        ]);
    }
    
    // check if this funnel is able to process this course and run the automation
    private function isProcessable($funnel, $courseId, $subscriberData)
    {
        $conditions = $funnel->conditions;
        // check update_type
        $updateType = Arr::get($conditions, 'update_type');
        $subscriber = FunnelHelper::getSubscriber($subscriberData['email']);
        if ($subscriber && $updateType == 'skip_all_if_exist') {
            return false;
        }
        // check the products ids
        if($conditions['course_ids'] && !in_array($courseId, $conditions['course_ids'])) {
            return false;
        }
         // check run_only_one
        if ($subscriber && FunnelHelper::ifAlreadyInFunnel($funnel->id, $subscriber->id)) {
            $multipleRun = Arr::get($conditions, 'run_multiple') == 'yes';
            if ($multipleRun) {
                FunnelHelper::removeSubscribersFromFunnel($funnel->id, [$subscriber->id]);
            } else {
                return false;
            }
        }
        return true;
    }

}
```
## Registering the Trigger
All set! Your trigger is ready to use.
Call the class to register the workflow.
```php
add_action('fluent_crm/after_init', function () {
    new Your\Plugin\Name\Automation\CourseEnrolledTrigger();
});
```

---
