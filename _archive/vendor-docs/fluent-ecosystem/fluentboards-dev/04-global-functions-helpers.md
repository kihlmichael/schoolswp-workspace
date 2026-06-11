# Section Global Functions & Helper Utilities

Source : dev.fluentboards.com
Date compile : 2026-05-24

---

## Boards API Function
Source file : `src/global-functions/boards-api-function.md`

# Boards API Function

The Boards API provides various methods to interact with board-related data. You can use these methods to retrieve, create, and manage boards, stages, and labels in your custom PHP snippets or plugins.

## Initialization
To initialize the Boards API, use the following code:
```php 
$boardsApi = FluentBoardsApi('boards');
```
`FluentBoardsApi('boards')` returns an instance of the `FluentBoards\App\Api\Classes\Boards` class.

## Methods

### getBoards()
The `getBoards` method retrieves a list of boards accessible by the current user. You can optionally include related data and specify sorting options.

**Parameters**
- `$with` (array): An array of relationships to include (optional).
- `$sortBy` (string): The column to sort by (default: title).
- `$sortOrder` (string): The sorting order (asc or desc, default: asc).

**Return** 
- An array of `Board` models.

**Example**
```php
$boards = $boardsApi->getBoards(['stages'], 'created_at', 'desc');
```

### getStagesByBoard()
The `getStagesByBoard` method retrieves stages associated with a specific board.

**Parameters**
- `$board_id` (int|string): The ID of the board.


**Return**
- An array of `Stage` models.

**Example**
```php
$stages = $boardsApi->getStagesByBoard(1);
```

### create()
The `create` method creates a new board with the provided data. It also creates default labels and stages for the board.

**Parameters**
- `$data` (array): The board data, including `title` (required).

**Return**
- The created `Board` model or `false` if creation fails.

**Example**
```php
$newBoard = $boardsApi->create([
    'title' => 'New Project Board',
    'description' => 'A board for managing new projects'
]);
```

### getStages()
The `getStages` method retrieves stages associated with a specific board, excluding archived stages.

**Parameters**
- `$board_id` (int|string): The ID of the board.

**Return**
- An array of `Stage` models.

**Example**
```php
$stages = $boardsApi->getStages(1);
```

### getInstance()
The `getInstance` method returns the raw `Board` model instance, allowing you to use all the methods of the query builder or ORM.

**Return**
- The `Board` model instance.

**Example**
```php
$boardInstance = $boardsApi->getInstance();
$board = $boardInstance->where('title', 'like', '%Project%')->first();
```

### getLabels()
The `getLabels` method retrieves labels associated with a specific board.

**Parameters**
- `$boardId` (int): The ID of the board.

**Return**
- An array of `Label` models or `false` if the board is not found or the user lacks access.

**Example**
```php
$labels = $boardsApi->getLabels(1);
```

### createLabel()
The `createLabel` method creates a new label for a specific board.

**Parameters**
- `$boardId` (int): The ID of the board.
- `$data` (array): The label data, including `bg_color` (required) and `color` (optional).

**Return**
- The created `Label` model or `false` if creation fails.

**Example**
```php
$newLabel = $boardsApi->createLabel(1, [
    'bg_color' => '#ff5733',
    'color' => '#ffffff',
    'title' => 'High Priority'
]);
```

---

## Global-Functions / Index
Source file : `src/global-functions/index.md`

## Global Functions

FluentBoards provides a set of global functions that can be used throughout the plugin.
In this article, we are documenting few useful functions that you may use. For full understanding, please check the `app/functions/helpers.php` file 

[[toc]]


### fluent_boards_user_avatar
Generate a user avatar URL based on the user's email.

**Parameters**
- `$email`: (string): The user's email address.
- `$name` (string, optional): The user's name to be used as a fallback if no Gravatar is found.

**Return**
- `string`: The URL of the user's avatar.

**Example**
```php
$avatarUrl = fluent_boards_user_avatar('user@example.com', 'John Doe');
```

### fluent_boards_page_url
Get the URL of the FluentBoards admin page.

**Return**
- `string`: The URL of the FluentBoards admin page.

**Example**
```php
$pageUrl = fluent_boards_page_url();
```

### fluent_boards_get_pref_settings
Get the URL of the FluentBoards admin page.

**Parameters**
- `$cached` (boolean, optional): Whether to use cached settings. Defaults to `true`.

**Return**
- `array`: An associative array of preference settings.

**Example**
```php
$settings = fluent_boards_get_pref_settings();
```

### fluent_boards_site_logo
Get the site logo URL.

**Return**
- `string`: The URL of the site's logo.

**Example**
```php
$logoUrl = fluent_boards_site_logo();
```

### fluent_boards_get_option
Get the site logo URL.

**Parameters**
- `$key` (string): The option key.
- `$default` (mixed, optional): The default value to return if the option does not exist. Defaults to `null`.

**Return**
- `mixed`: The value of the option or the default value.

**Example**
```php
$optionValue = fluent_boards_get_option('some_option_key', 'default_value');
```

### fluent_boards_update_option
Get the site logo URL.

**Parameters**
- `key` (string): The option key.
- `$value` (mixed): The value to set for the option.

**Return**
- `\FluentBoards\App\Models\Meta`: The updated `Meta` model instance.

**Example**
```php
$updatedOption = fluent_boards_update_option('some_option_key', 'new_value');
```

### fluentBoardsDb
Get the FluentBoards database instance.

**Return**
- `\FluentBoards\App\App`

**Example**
```php
$db = fluentBoardsDb();
```


This documentation provides a comprehensive overview of the global functions available in the `FluentBoards` plugin, including their usage, parameters, and return values.

---

## Stages API Function
Source file : `src/global-functions/stages-api-function.md`

# Stages API Function

The Stages API provides methods to interact with stage-related data in FluentBoards. This API allows you to retrieve, create, update, and manage stages, ensuring that operations are secured based on user permissions.

## Initialization
To initialize the Stages API, use the following code:

```php
$stagesApi = FluentBoardsApi('stages');
```
`FluentBoardsApi('stages')` returns an instance of the `FluentBoards\App\Api\Classes\Stages` class.

## Methods

### getStage()
The `getStage` method retrieves a single stage by its ID, optionally including related data.

**Parameters**
- `$id` (int|string): The ID of the stage.
- `$with` (array): An array of relationships to include (optional).

**Return** 
- A `Stage` model with the specified ID or `false` if the stage is not found or the user lacks permission.

**Example**
```php
$stage = $stagesApi->getStage(1, ['tasks']);
```

### getStagesByBoard()
The `getStagesByBoard` method retrieves all stages associated with a specific board, excluding archived stages.

**Parameters**
- `$boardId` (int|string): The ID of the board.
- `$with` (array): An array of relationships to include (optional).

**Return**
- An array of `Stage` models or `false` if the board ID is invalid or the user lacks permission.

**Example**
```php
$stages = $stagesApi->getStagesByBoard(1, ['tasks']);
```

### create()
The `create` method creates a new stage with the provided data.

**Parameters**
- `$data` (array): The stage data, including `title` and `board_id` (both required).

**Return**
- The created `Stage` model or `false` if creation fails due to missing data or permission issues.

**Example**
```php
$newStage = $stagesApi->create([
    'title' => 'Planning',
    'board_id' => 1
]);
```

### updateProperty()
The `updateProperty` method updates a specific property of a stage.

**Parameters**
- `$stageId` (int): The ID of the stage.
- `$property` (string): The property to update (title, status, or bg_color).
- `$value` (mixed): The new value for the property.

**Return**
- The updated `Stage` model or `false` if the property is not allowed or the user lacks permission.


**Example**
```php
$updatedStage = $stagesApi->updateProperty(1, 'title', 'In Progress');
```

### archiveStage()
The `archiveStage` method archives a specific stage by its ID.

**Parameters**
- `$stageId` (int|string): The ID of the stage.

**Return**
- The archived `Stage` model or `false` if the archive operation fails.


**Example**
```php
$archivedStage = $stagesApi->archiveStage(1);
```

### restoreStage()
The `restoreStage` method restores a previously archived stage by its ID.

**Parameters**
- `$stageId` (int|string): The ID of the stage.

**Return**
- The restored `Stage` model or `false` if the restore operation fails.


**Example**
```php
$restoredStage = $stagesApi->restoreStage(1);
```

### getInstance()
The `getInstance` method returns the raw `Stage` model instance, allowing you to use all the methods of the query builder or ORM.

**Return**
- The `Stage` model instance.


**Example**
```php
$stageInstance = $stagesApi->getInstance();
$stage = $stageInstance->where('title', 'like', '%To Do%')->first();
```

---

## Tasks API Function
Source file : `src/global-functions/tasks-api-function.md`

# Tasks API Function

The Tasks API provides methods to interact with task-related data in FluentBoards. This API allows you to retrieve, create, update, manage tasks, and handle task attachments, ensuring operations are secured based on user permissions.

## Initialization
To initialize the Tasks API, use the following code:
```php
$tasksApi = FluentBoardsApi('tasks');
```
`FluentBoardsApi('tasks')` returns an instance of the `FluentBoards\App\Api\Classes\Tasks` class.


## Methods

### getTasksByBoard()
The `getTasksByBoard` method retrieves all tasks associated with a specific board, excluding archived tasks.

**Parameters**
- `$board_id` (int|string): The ID of the board.
- `$with` (array): An array of relationships to include (optional).

**Return** 
- An array of `Task` models or `false` if the board ID is invalid or the user lacks permission.

**Example**
```php
$tasks = $tasksApi->getTasksByBoard(1, ['labels', 'assignees']);
```

### getTask()
The `getTask` method retrieves a single task by its ID.

**Parameters**
- `$id` (int|string): The ID of the task.

**Return**
- A `Task` model with the specified ID or `false` if the task is not found or the user lacks permission.

**Example**
```php
$task = $tasksApi->getTask(1);
```

### getTasksCreatedBy()
The `getTasksCreatedBy` method retrieves all tasks created by a specific user.

**Parameters**
- `$userId` (int|string): The ID of the user.
- `$with` (array): An array of relationships to include (optional).

**Return**
- An array of `Task` models or `false` if the user ID is invalid or the user lacks permission.

**Example**
```php
$tasks = $tasksApi->getTasksCreatedBy(2, ['labels']);
```

### create()
The `create` method creates a new task with the provided data.

**Parameters**
- `$data` (array): The task data, including `title`, `board_id`, and `stage_id` (all required).


**Return**
- The created `Task` model or `false` if creation fails due to missing data or permission issues.

**Example**
```php
$newTask = $tasksApi->create([
    'title' => 'New Task',
    'board_id' => 1,
    'stage_id' => 2,
    'description' => 'Task description'
]);
```

### createTask()
The `createTask` method defines the required and optional fields for creating a task.

**Parameters**
- `$data` (array): Task data including `title`, `board_id`, `stage_id`, and other optional fields.

**Return**
- A Task `model` or `false` if creation fails.

**Example**
```php
$tasksApi->createTask([
    'title' => 'Task Title',
    'board_id' => 1,
    'stage_id' => 2,
    // Additional fields as necessary
]);
```

### addAssignees()
The `addAssignees` method adds one or more assignees to a task.

**Parameters**
- `$task_id` (int): The ID of the task.
- `$assignees` (array): An array of WP user IDs to be added as assignees.

**Return**
- `true` if assignees were successfully added, otherwise `false`.

**Example**
```php
$tasksApi->addAssignees(1, [3, 4]);
```

### removeAssignees()
The `removeAssignees` method removes one or more assignees from a task.

**Parameters**
- `$task_id` (int): The ID of the task.
- `$assignees` (array): An array of WP user IDs to be removed as assignees.


**Return**
- `true` if assignees were successfully removed, otherwise `false`.

**Example**
```php
$tasksApi->removeAssignees(1, [3]);
```

### attachLabels()
The `attachLabels` method attaches one or more labels to a task.

**Parameters**
- `$taskId` (int): The ID of the task.
- `$labelIds` (array): An array of label IDs to be attached.

**Return**
- `true` if labels were successfully attached, otherwise `false`.

**Example**
```php
$tasksApi->attachLabels(1, [5, 6]);
```

### removeLabels()
The `removeLabels` method removes one or more labels from a task.

**Parameters**
- `$taskId` (int): The ID of the task.
- `$labelIds` (array): An array of label IDs to be removed.

**Return**
- `true` if labels were successfully removed, otherwise `false`.

**Example**
```php
$tasksApi->removeLabels(1, [5]);
```

### changeStage()
The `changeStage` method updates the stage of a task.

**Parameters**
- `$task` (int|Task): The ID of the task or a `Task` model.
- `$stageId` (int): The ID of the new stage.

**Return**
- The updated `Task` model or `false` if the operation fails.

**Example**
```php
$tasksApi->changeStage(1, 3);
```

### updateProperty()
The `updateProperty` method updates a specific property of a task.

**Parameters**
- `$taskId` (int): The ID of the task.
- `$property` (string): The property to update (e.g., title, description, due_at).
- `$value` (mixed): The new value for the property.

**Return**
- The updated `Task` model or `false` if the property is not allowed or the user lacks permission.

**Example**
```php
$updatedTask = $tasksApi->updateProperty(1, 'title', 'Updated Task Title');
```

### createTaskAttachment()
The `createTaskAttachment` method creates an attachment for a task.

**Parameters**
- `$boardId` (int): The ID of the board.
- `$taskId` (int): The ID of the task.
- `$data` (array): The attachment data, including title and url (required).

**Return**
- The created `TaskAttachment` model or `false` if creation fails.

**Example**
```php
$attachment = $tasksApi->createTaskAttachment(1, 1, [
    'title' => 'Attachment Title',
    'url' => 'https://example.com/attachment.jpg'
]);
```

### deleteTaskAttachment()
The `deleteTaskAttachment` method deletes an attachment from a task.

**Parameters**
- `$boardId` (int): The ID of the board.
- `$taskId` (int): The ID of the task.
- `$attachmentId` (int): The ID of the attachment.

**Return**
- `true` if the attachment was successfully deleted, otherwise `false`.

**Example**
```php
$tasksApi->deleteTaskAttachment(1, 1, 1);
```

### getInstance()
The `getInstance` method returns the raw `Task` model instance, allowing you to use all the methods of the query builder or ORM.

**Return**
- The `Task` model instance.

**Example**
```php
$taskInstance = $tasksApi->getInstance();
$task = $taskInstance->where('title', 'like', '%Task%')->first();
```

---

## Array Helper aka Arr
Source file : `src/helpers/arr.md`

# Array Helper aka Arr

- Class with Namespace: `\FluentBoards\Framework\Support\Arr`
- Method Types: `static`

<a name="method-array-add"></a>
### `Arr::add()`

The `Arr::add` method adds a given key / value pair to an array if the given key doesn't already exist in the array:
```php 
use FluentBoards\Framework\Support\Arr;

$array = Arr::add(['name' => 'Desk'], 'price', 100);

// ['name' => 'Desk', 'price' => 100]
```
    

<a name="method-array-collapse"></a>
### `Arr::collapse()`

The `Arr::collapse` method collapses an array of arrays into a single array:
```php 
use FluentBoards\Framework\Support\Arr;

$array = Arr::collapse([[1, 2, 3], [4, 5, 6], [7, 8, 9]]);

// [1, 2, 3, 4, 5, 6, 7, 8, 9]
```

<a name="method-array-divide"></a>
### `Arr::divide()`

The `Arr::divide` method returns two arrays, one containing the keys, and the other containing the values of the given array:
```php 
use FluentBoards\Framework\Support\Arr;

[$keys, $values] = Arr::divide(['name' => 'Desk']);

// $keys: ['name']

// $values: ['Desk']
```

<a name="method-array-dot"></a>
### `Arr::dot()`

The `Arr::dot` method flattens a multi-dimensional array into a single level array that uses "dot" notation to indicate depth:
```php 
use FluentBoards\Framework\Support\Arr;

$array = ['products' => ['desk' => ['price' => 100]]];

$flattened = Arr::dot($array);

// ['products.desk.price' => 100]
```

<a name="method-array-except"></a>
### `Arr::except()`

The `Arr::except` method removes the given key / value pairs from an array:
```php 
use FluentBoards\Framework\Support\Arr;

$array = ['name' => 'Desk', 'price' => 100];

$filtered = Arr::except($array, ['price']);

// ['name' => 'Desk']
```
<a name="method-array-first"></a>
### `Arr::first()`

The `Arr::first` method returns the first element of an array passing a given truth test:
```php 
use FluentBoards\Framework\Support\Arr;

$array = [100, 200, 300];

$first = Arr::first($array, function ($value, $key) {
    return $value >= 150;
});

// 200
```
A default value may also be passed as the third parameter to the method. This value will be returned if no value passes the truth test:
```php 
use FluentBoards\Framework\Support\Arr;

$first = Arr::first($array, $callback, $default);
```

<a name="method-array-flatten"></a>
### `Arr::flatten()`

The `Arr::flatten` method flattens a multi-dimensional array into a single level array:

```php 
use FluentBoards\Framework\Support\Arr;

$array = ['name' => 'Joe', 'languages' => ['PHP', 'Ruby']];

$flattened = Arr::flatten($array);

// ['Joe', 'PHP', 'Ruby']
```

<a name="method-array-forget"></a>
### `Arr::forget()`

The `Arr::forget` method removes a given key / value pair from a deeply nested array using "dot" notation:

```php 
use FluentBoards\Framework\Support\Arr;

$array = ['products' => ['desk' => ['price' => 100]]];

Arr::forget($array, 'products.desk');

// ['products' => []]
```

<a name="method-array-get"></a>
### `Arr::get()`

The `Arr::get` method retrieves a value from a deeply nested array using "dot" notation:
```php 
use FluentBoards\Framework\Support\Arr;

$array = ['products' => ['desk' => ['price' => 100]]];

$price = Arr::get($array, 'products.desk.price');

// 100
```

The `Arr::get` method also accepts a default value, which will be returned if the specific key is not found:

```php 
use FluentBoards\Framework\Support\Arr;

$discount = Arr::get($array, 'products.desk.discount', 0);

// 0
```

<a name="method-array-has"></a>
### `Arr::has()`

The `Arr::has` method checks whether a given item or items exists in an array using "dot" notation:

```php 
use FluentBoards\Framework\Support\Arr;

$array = ['product' => ['name' => 'Desk', 'price' => 100]];

$contains = Arr::has($array, 'product.name');

// true

$contains = Arr::has($array, ['product.price', 'product.discount']);

// false
```

<a name="method-array-last"></a>
### `Arr::last()`

The `Arr::last` method returns the last element of an array passing a given truth test:
```php 
use FluentBoards\Framework\Support\Arr;

$array = [100, 200, 300, 110];

$last = Arr::last($array, function ($value, $key) {
    return $value >= 150;
});

// 300
```

A default value may be passed as the third argument to the method. This value will be returned if no value passes the truth test:
```php 
use FluentBoards\Framework\Support\Arr;

$last = Arr::last($array, $callback, $default);
```

<a name="method-array-only"></a>
### `Arr::only()`

The `Arr::only` method returns only the specified key / value pairs from the given array:
```php 
use FluentBoards\Framework\Support\Arr;

$array = ['name' => 'Desk', 'price' => 100, 'orders' => 10];

$slice = Arr::only($array, ['name', 'price']);

// ['name' => 'Desk', 'price' => 100]
```
<a name="method-array-pluck"></a>
### `Arr::pluck()`

The `Arr::pluck` method retrieves all of the values for a given key from an array:
```php 
use FluentBoards\Framework\Support\Arr;

$array = [
    ['developer' => ['id' => 1, 'name' => 'Jewel']],
    ['developer' => ['id' => 2, 'name' => 'Adre']],
];

$names = Arr::pluck($array, 'developer.name');

// ['Jewel', 'Adre']
```
You may also specify how you wish the resulting list to be keyed:
```php 
use FluentBoards\Framework\Support\Arr;

$names = Arr::pluck($array, 'developer.name', 'developer.id');

// [1 => 'Jewel', 2 => 'Adre']
```
<a name="method-array-prepend"></a>
### `Arr::prepend()`

The `Arr::prepend` method will push an item onto the beginning of an array:
```php 
use FluentBoards\Framework\Support\Arr;

$array = ['one', 'two', 'three', 'four'];

$array = Arr::prepend($array, 'zero');

// ['zero', 'one', 'two', 'three', 'four']
```

If needed, you may specify the key that should be used for the value:
```php 
use FluentBoards\Framework\Support\Arr;

$array = ['price' => 100];

$array = Arr::prepend($array, 'Desk', 'name');

// ['name' => 'Desk', 'price' => 100]
```

<a name="method-array-pull"></a>
### `Arr::pull()`

The `Arr::pull` method returns and removes a key / value pair from an array:
```php 
use FluentBoards\Framework\Support\Arr;

$array = ['name' => 'Desk', 'price' => 100];

$name = Arr::pull($array, 'name');

// $name: Desk

// $array: ['price' => 100]
```

A default value may be passed as the third argument to the method. This value will be returned if the key doesn't exist:
```php 
use FluentBoards\Framework\Support\Arr;

$value = Arr::pull($array, $key, $default);
```
<a name="method-array-random"></a>
### `Arr::random()`

The `Arr::random` method returns a random value from an array:
```php 
use FluentBoards\Framework\Support\Arr;

$array = [1, 2, 3, 4, 5];

$random = Arr::random($array);

// 4 - (retrieved randomly)
```
You may also specify the number of items to return as an optional second argument. Note that providing this argument will return an array, even if only one item is desired:
```php 
use FluentBoards\Framework\Support\Arr;

$items = Arr::random($array, 2);

// [2, 5] - (retrieved randomly)
```

<a name="method-array-set"></a>
### `Arr::set()`

The `Arr::set` method sets a value within a deeply nested array using "dot" notation:
```php 
use FluentBoards\Framework\Support\Arr;

$array = ['products' => ['desk' => ['price' => 100]]];

Arr::set($array, 'products.desk.price', 200);

// ['products' => ['desk' => ['price' => 200]]]
```

<a name="method-array-sort"></a>
### `Arr::sort()`

The `Arr::sort` method sorts an array by its values:
```php 
use FluentBoards\Framework\Support\Arr;

$array = ['Desk', 'Table', 'Chair'];

$sorted = Arr::sort($array);

// ['Chair', 'Desk', 'Table']
```

You may also sort the array by the results of the given Closure:
```php 
use FluentBoards\Framework\Support\Arr;

$array = [
    ['name' => 'Desk'],
    ['name' => 'Table'],
    ['name' => 'Chair'],
];

$sorted = array_values(Arr::sort($array, function ($value) {
    return $value['name'];
}));

/*
    [
        ['name' => 'Chair'],
        ['name' => 'Desk'],
        ['name' => 'Table'],
    ]
*/
```
<a name="method-array-sort-recursive"></a>
### `Arr::sortRecursive()`

The `Arr::sortRecursive` method recursively sorts an array using the `sort` function for numeric sub=arrays and `ksort` for associative sub-arrays:
```php 
use FluentBoards\Framework\Support\Arr;

$array = [
    ['Roman', 'Taylor', 'Li'],
    ['PHP', 'Ruby', 'JavaScript'],
    ['one' => 1, 'two' => 2, 'three' => 3],
];

$sorted = Arr::sortRecursive($array);

/*
    [
        ['JavaScript', 'PHP', 'Ruby'],
        ['one' => 1, 'three' => 3, 'two' => 2],
        ['Li', 'Roman', 'Taylor'],
    ]
*/
```

<a name="method-array-where"></a>
### `Arr::where()`

The `Arr::where` method filters an array using the given Closure:
```php 
use FluentBoards\Framework\Support\Arr;

$array = [100, '200', 300, '400', 500];

$filtered = Arr::where($array, function ($value, $key) {
    return is_string($value);
});

// [1 => '200', 3 => '400']
```

---

## Helpers / Index
Source file : `src/helpers/index.md`

## Helper Classes

FluentBoards provides few helper classes that you can interact easily to build advanced functionalities on your plugin.
Many of these functions are used by the plugin itself; however, you are free to use them in your own addon if you find them convenient.

---

## FluentBoards Core Helper Class
Source file : `src/helpers/service_helper.md`

# FluentBoards Core Helper Class

- Class with Namespace: `\FluentBoards\App\Services\Helper`
- Method Types: `static`

# Methods

### Helper::snake_case($string)
Converts a given string to snake_case.

**Parameters**
- `$string` (string): The string to convert.

**Return**
- `string` (string): The snake_case version of the input string.

**Example**
```php
$snakeCase = Helper::snake_case('Hello World');
// Output: hello_world
```

### Helper::slugify($text, $id = '', $length = 20)
Generates a URL-friendly slug from a given text, optionally prepended with an ID and limited to a specified length.

**Parameters**
- `text` (string): The text to convert.
- `id` (string, optional): An optional ID to prepend.
- `length` (int, optional): The maximum length of the slug (default is 20).


**Return**
- (string): The generated slug.

**Example**
```php
$slug = Helper::slugify('Hello World', '12345', 10);
// Output: 12345-hello-w
```

### Helper::createActivity($data)
Creates an activity log entry in the database.

**Parameters**
- `$data` (array): The activity data to save.

**Return**
- (Activity): The created activity.

**Example**
```php
$activity_data = ['action' => 'Task Created', 'details' => 'Task ID 123 created.'];
$activity = Helper::createActivity($activity_data);
// Output: An instance of the Activity model with the created data.
```

### Helper::getFormattedStagesByBoardId($boardId)
Get the formatted stages for a board.

**Parameters**
- `$boardId` (int): The ID of the board.

**Return**
- (array): An associative array of formatted stages.

**Example**
```php
$formatted_stages = Helper::getFormattedStagesByBoardId(1);
// Output: [
//     ['id' => '1', 'title' => 'Board A - Stage 1'],
//     ['id' => '2', 'title' => 'Board A - Stage 2'],
// ]
```

### Helper::getStagesByBoardId($boardId)
Get the stages for a board.

**Parameters**
- `$boardId` (int): The ID of the board.

**Return**
- (array): An associative array of stages.

**Example**
```php
$stages = Helper::getStagesByBoardId(1);
// Output: An array of stage objects related to the board with ID 1.
```

### Helper::formateStage($stages)
Format the stages for display.

**Parameters**
- `$stages` (array): An array of stages.

**Return**
- (array): An associative array of formatted stages.

**Example**
```php
$stages = [
    (object) ['id' => 1, 'board' => (object) ['title' => 'Board A'], 'title' => 'Stage 1'],
    (object) ['id' => 2, 'board' => (object) ['title' => 'Board A'], 'title' => 'Stage 2'],
];
$formatted_stages = Helper::formateStage($stages);
// Output: [
//     ['id' => '1', 'title' => 'Board A - Stage 1'],
//     ['id' => '2', 'title' => 'Board A - Stage 2'],
// ]
```

### Helper::getIdTitleArray($data)
Get an associative array of IDs and titles from a collection.

**Parameters**
- `$data` (Collection): The collection to extract IDs and titles from.

**Return**
- (array): An associative array of IDs and titles.

**Example**
```php
$collection = collect([
    (object) ['id' => 1, 'title' => 'Item 1'],
    (object) ['id' => 2, 'title' => 'Item 2'],
]);
$id_title_array = Helper::getIdTitleArray($collection);
// Output: [1 => 'Item 1', 2 => 'Item 2']
```

### Helper::getTaskUrl($taskId, $boardId)
The `Helper::getTaskUrl($taskId, $boardId)` method generates the URL for a specific task within a board.

**Parameters**
- `$taskId` (int): The ID of the task.
- `$boardId` (int): The ID of the board.

**Return**
- (string): The URL of the task.

**Example**
```php
$taskId = 15;
$boardId = 3;
$taskUrl = Helper::getTaskUrl($taskId, $boardId);

// Output: 'https://example.com/boards/3/tasks/15'
```

### Helper::getTaskUrlByTask($task)
The `Helper::getTaskUrlByTask($task)` method generates the URL for a task object.

**Parameters**
- `$task` (Task): The task object.

**Return**
- (string): The URL of the task.

**Example**
```php
$task = (object) ['id' => 15, 'board_id' => 3];
$taskUrl = Helper::getTaskUrlByTask($task);

// Output: 'https://example.com/boards/3/tasks/15'
```

### Helper::getBoardUrl($boardId)
The `Helper::getBoardUrl($boardId)` method generates the URL for a specific board.

**Parameters**
- `$boardId` (int): The ID of the board.

**Return**
- (string): The URL of the board.

**Example**
```php
$boardId = 3;
$boardUrl = Helper::getBoardUrl($boardId);

// Output: 'https://example.com/boards/3'
```

### Helper::crm_contact($id)
The `Helper::crm_contact($id)` method retrieves the CRM contact details for a given ID.

**Parameters**
- `$id` (int): The ID of the CRM contact.

**Return**
- (array): The contact details.

**Example**
```php
$contactId = 100;
$contactDetails = Helper::crm_contact($contactId);

// Output: 
/*
[
    'id' => 100,
    'email' => 'contact@example.com',
    'first_name' => 'John',
    'last_name' => 'Doe',
    ...
]
*/
```

### Helper::getStagesByBoardGroup()
The `Helper::getStagesByBoardGroup()` method retrieves the stages for a board group.

**Return**
- (array): An associative array of stages.

**Example**
```php
$stageGroups = Helper::getStagesByBoardGroup();

// Output: 
/*
[
    [
        'title' => 'Board A',
        'slug' => 'aaa_1',
        'options' => [ ...stages... ]
    ],
    [
        'title' => 'Board B',
        'slug' => 'aaa_2',
        'options' => [ ...stages... ]
    ],
    ...
]
*/
```

### Helper::getBoards()
The `Helper::getBoards()` method retrieves all boards.

**Return**
- (array): An array of boards.

**Example**
```php
$boards = Helper::getBoards();

// Output: A collection of Board objects ordered by creation date.
```

### Helper::getStage($stageId)
The `Helper::getStage($stageId)` method retrieves a stage by its ID.

**Parameters**
- `$stageId` (int): The ID of the stage.

**Return**
- (Stage): The stage object.

**Example**
```php
$stageId = 5;
$stage = Helper::getStage($stageId);

// Output: A Stage object corresponding to the given stage ID.
```

### Helper::getBoardByStageId($stageId)
The `Helper::getBoardByStageId($stageId)` method retrieves the board associated with a stage.

**Parameters**
- `$stageId` (int): The ID of the stage.

**Return**
- (Board): The board object.

**Example**
```php
$stageId = 7;
$board = Helper::getBoardByStageId($stageId);

// Output: The Board object associated with the given stage ID.
```

### Helper::getPriorityOptions()
The `Helper::getPriorityOptions()` method retrieves the priority options.

**Return**
- (array): An array of priority options.

**Example**
```php
$priorityOptions = Helper::getPriorityOptions();

// Output: 
/*
[
    ['id' => 'low', 'title' => 'Low'],
    ['id' => 'medium', 'title' => 'Medium'],
    ['id' => 'high', 'title' => 'High'],
]
*/
```

### Helper::dueDateConversion($due_time, $unit)
The `Helper::dueDateConversion($due_time, $unit)` method converts a due date to a specific unit.

**Parameters**
- $due_time (int): The amount of time until the due date.
- $unit (string): The unit of time (e.g., 'days', 'hours').

**Return**
- (string): The formatted due date.

**Example**
```php
$due_time = 3;
$unit = 'days';
$dueDate = Helper::dueDateConversion($due_time, $unit);

// Output: '2024-09-01 00:00:00' (based on the current date)
```

### Helper::searchWordPressUsers($searchQuery, $limit = 20)
The `Helper::searchWordPressUsers($searchQuery, $limit = 20)` method searches for WordPress users by login, email, nicename, first name, or last name.

**Parameters**
- $searchQuery (string): The search term.
- $limit (int, optional): The maximum number of results to return. Defaults to 20.

**Return**
- (array): An array of user objects.

**Example**
```php
$searchQuery = 'John';
$users = Helper::searchWordPressUsers($searchQuery, 10);

// Output: A list of user objects matching the search query.
```

This documentation focuses on the functional aspects of each method, providing examples to demonstrate how they can be used in practice.

---

## String Helper aka Str
Source file : `src/helpers/str.md`

# String Helper aka Str

- Class with Namespace: `\FluentBoards\Framework\Support\Str`
- Method Types: `static`


<a name="method-camel-case"></a>
### `Str::camel()`

The `Str::camel` method converts the given string to `camelCase`:

```php 
    use FluentBoards\Framework\Support\Str;

    $converted = Str::camel('foo_bar');

    // fooBar
```

<a name="method-ends-with"></a>
### `Str::endsWith()`

The `Str::endsWith` method determines if the given string ends with the given value:

```php 
    use FluentBoards\Framework\Support\Str;

    $result = Str::endsWith('This is my name', 'name');

    // true
```

<a name="method-kebab-case"></a>
### `Str::kebab()`

The `Str::kebab` method converts the given string to `kebab-case`:

```php 
    use FluentBoards\Framework\Support\Str;

    $converted = Str::kebab('fooBar');

    // foo-bar
```

<a name="method-preg-replace-array"></a>
### `preg_replace_array()`

The `preg_replace_array` function replaces a given pattern in the string sequentially using an array:

```php 
    $string = 'The event will take place between :start and :end';

    $replaced = preg_replace_array('/:[a-z_]+/', ['8:30', '9:00'], $string);

    // The event will take place between 8:30 and 9:00
```

<a name="method-snake-case"></a>
### `Str::snake()`

The `Str::snake` method converts the given string to `snake_case`:

```php 
    use FluentBoards\Framework\Support\Str;

    $converted = Str::snake('fooBar');

    // foo_bar
```

<a name="method-starts-with"></a>
### `Str::startsWith()`

The `Str::startsWith` method determines if the given string begins with the given value:

```php 
    use FluentBoards\Framework\Support\Str;

    $result = Str::startsWith('This is my name', 'This');

    // true
```

<a name="method-str-after"></a>
### `Str::after()`

The `Str::after` method returns everything after the given value in a string:

```php 
    use FluentBoards\Framework\Support\Str;

    $slice = Str::after('This is my name', 'This is');

    // ' my name'
```

<a name="method-str-before"></a>
### `Str::before()`

The `Str::before` method returns everything before the given value in a string:
```php 
    use FluentBoards\Framework\Support\Str;

    $slice = Str::before('This is my name', 'my name');

    // 'This is '
```

<a name="method-str-contains"></a>
### `Str::contains()`

The `Str::contains` method determines if the given string contains the given value (case sensitive):

```php 
    use FluentBoards\Framework\Support\Str;

    $contains = Str::contains('This is my name', 'my');

    // true
```

You may also pass an array of values to determine if the given string contains any of the values:

```php 
    use FluentBoards\Framework\Support\Str;

    $contains = Str::contains('This is my name', ['my', 'foo']);

    // true
```

<a name="method-str-finish"></a>
### `Str::finish()`

The `Str::finish` method adds a single instance of the given value to a string if it does not already end with the value:

```php 
    use FluentBoards\Framework\Support\Str;

    $adjusted = Str::finish('this/string', '/');

    // this/string/

    $adjusted = Str::finish('this/string/', '/');

    // this/string/
```

<a name="method-str-is"></a>
### `Str::is()`

The `Str::is` method determines if a given string matches a given pattern. Asterisks may be used to indicate wildcards:

```php 
    use FluentBoards\Framework\Support\Str;

    $matches = Str::is('foo*', 'foobar');

    // true

    $matches = Str::is('baz*', 'foobar');

    // false
```

<a name="method-str-limit"></a>
### `Str::limit()`

The `Str::limit` method truncates the given string at the specified length:

```php 
    use FluentBoards\Framework\Support\Str;

    $truncated = Str::limit('The quick brown fox jumps over the lazy dog', 20);

    // The quick brown fox...
```

You may also pass a third argument to change the string that will be appended to the end:

```php 
    use FluentBoards\Framework\Support\Str;

    $truncated = Str::limit('The quick brown fox jumps over the lazy dog', 20, ' (...)');

    // The quick brown fox (...)
```

<a name="method-str-ordered-uuid"></a>
### `Str::orderedUuid()`

The `Str::orderedUuid` method generates a "timestamp first" UUID that may be efficiently stored in an indexed database column:

```php 
    use FluentBoards\Framework\Support\Str;

    return (string) Str::orderedUuid();
```

<a name="method-str-plural"></a>
### `Str::plural()`

The `Str::plural` method converts a string to its plural form. This function currently only supports the English language:

```php 
    use FluentBoards\Framework\Support\Str;

    $plural = Str::plural('car');

    // cars

    $plural = Str::plural('child');

    // children
```

You may provide an integer as a second argument to the function to retrieve the singular or plural form of the string:

```php 
    use FluentBoards\Framework\Support\Str;

    $plural = Str::plural('child', 2);

    // children

    $plural = Str::plural('child', 1);

    // child
```

<a name="method-str-random"></a>
### `Str::random()`

The `Str::random` method generates a random string of the specified length. This function uses PHP's `random_bytes` function:

```php 
    use FluentBoards\Framework\Support\Str;

    $random = Str::random(40);
```

<a name="method-str-replace-array"></a>
### `Str::replaceArray()`

The `Str::replaceArray` method replaces a given value in the string sequentially using an array:

```php 
    use FluentBoards\Framework\Support\Str;

    $string = 'The event will take place between ? and ?';

    $replaced = Str::replaceArray('?', ['8:30', '9:00'], $string);

    // The event will take place between 8:30 and 9:00
```

<a name="method-str-replace-first"></a>
### `Str::replaceFirst()`

The `Str::replaceFirst` method replaces the first occurrence of a given value in a string:

```php 
    use FluentBoards\Framework\Support\Str;

    $replaced = Str::replaceFirst('the', 'a', 'the quick brown fox jumps over the lazy dog');

    // a quick brown fox jumps over the lazy dog
```

<a name="method-str-replace-last"></a>
### `Str::replaceLast()`

The `Str::replaceLast` method replaces the last occurrence of a given value in a string:

```php 
    use FluentBoards\Framework\Support\Str;

    $replaced = Str::replaceLast('the', 'a', 'the quick brown fox jumps over the lazy dog');

    // the quick brown fox jumps over a lazy dog
```

<a name="method-str-singular"></a>
### `Str::singular()`

The `Str::singular` method converts a string to its singular form. This function currently only supports the English language:

```php 
    use FluentBoards\Framework\Support\Str;

    $singular = Str::singular('cars');

    // car

    $singular = Str::singular('children');

    // child
```

<a name="method-str-slug"></a>
### `Str::slug()`

The `Str::slug` method generates a URL friendly "slug" from the given string:

```php 
    use FluentBoards\Framework\Support\Str;

    $slug = Str::slug('Laravel 5 Framework', '-');

    // laravel-5-framework
```

<a name="method-str-start"></a>
### `Str::start()`

The `Str::start` method adds a single instance of the given value to a string if it does not already start with the value:

```php 
    use FluentBoards\Framework\Support\Str;

    $adjusted = Str::start('this/string', '/');

    // /this/string

    $adjusted = Str::start('/this/string', '/');

    // /this/string
```

<a name="method-studly-case"></a>
### `Str::studly()`

The `Str::studly` method converts the given string to `StudlyCase`:

```php 
    use FluentBoards\Framework\Support\Str;

    $converted = Str::studly('foo_bar');

    // FooBar
```

<a name="method-title-case"></a>
### `Str::title()`

The `Str::title` method converts the given string to `Title Case`:

```php 
    use FluentBoards\Framework\Support\Str;

    $converted = Str::title('a nice title uses the correct case');

    // A Nice Title Uses The Correct Case
```

If the specified translation key does not exist, the `trans` function will return the given key. So, using the example above, the `trans` function would return `messages.welcome` if the translation key does not exist.

<a name="method-str-uuid"></a>
### `Str::uuid()`

The `Str::uuid` method generates a UUID (version 4):

```php 
    use FluentBoards\Framework\Support\Str;

    return (string) Str::uuid();
```

---
