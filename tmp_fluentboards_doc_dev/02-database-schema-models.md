# Section Database Schema & ORM Models

Source : dev.fluentboards.com
Date compile : 2026-05-24


---

## _Parts  /  _Funnel_Schema
Source file : `src/database/_parts\_funnel_schema.md`

<table>
<thead><tr><th>Column</th><td>Type</td><td>Comment</td></tr></thead>
<tbody><tr><th>id</th><td><span title="">bigint unsigned</span> <i>Auto Increment</i></td><td>
</td></tr><tr class="odd"><th>type</th><td><span title="utf8mb4_unicode_520_ci">varchar(50)</span> <span title="Default value">[<b>funnel</b>]</span></td><td>
</td></tr><tr><th>title</th><td><span title="utf8mb4_unicode_520_ci">varchar(192)</span></td><td>
</td></tr><tr class="odd"><th>trigger_name</th><td><span title="utf8mb4_unicode_520_ci">varchar(150)</span> <i>NULL</i></td><td>
</td></tr><tr><th>status</th><td><span title="utf8mb4_unicode_520_ci">varchar(50)</span> <i>NULL</i> <span title="Default value">[<b>draft</b>]</span></td><td>
</td></tr><tr class="odd"><th>conditions</th><td><span title="utf8mb4_unicode_520_ci">text</span> <i>NULL</i></td><td>
</td></tr><tr><th>settings</th><td><span title="utf8mb4_unicode_520_ci">text</span> <i>NULL</i></td><td>
</td></tr><tr class="odd"><th>created_by</th><td><span title="">bigint unsigned</span> <i>NULL</i></td><td>
</td></tr><tr><th>created_at</th><td><span title="">timestamp</span> <i>NULL</i></td><td>
</td></tr><tr class="odd"><th>updated_at</th><td><span title="">timestamp</span> <i>NULL</i></td><td>
</td></tr></tbody></table>

---

## _Parts  /  _Subscriber_Schema
Source file : `src/database/_parts\_subscriber_schema.md`

<table cellspacing="0" class="nowrap">
<thead><tr><th>Column</th><td>Type</td><td>Comment</td></tr></thead>
<tbody><tr><th>id</th><td><span title="">bigint unsigned</span> <i>Auto Increment</i></td><td>
</td></tr><tr class="odd"><th>user_id</th><td><span title="">bigint unsigned</span> <i>NULL</i></td><td>
</td></tr><tr><th>hash</th><td><span title="utf8mb4_unicode_520_ci">varchar(90)</span> <i>NULL</i></td><td>
</td></tr><tr class="odd"><th>contact_owner</th><td><span title="">bigint unsigned</span> <i>NULL</i></td><td>
</td></tr><tr><th>company_id</th><td><span title="">bigint unsigned</span> <i>NULL</i></td><td>
</td></tr><tr class="odd"><th>prefix</th><td><span title="utf8mb4_unicode_520_ci">varchar(192)</span> <i>NULL</i></td><td>
</td></tr><tr><th>first_name</th><td><span title="utf8mb4_unicode_520_ci">varchar(192)</span> <i>NULL</i></td><td>
</td></tr><tr class="odd"><th>last_name</th><td><span title="utf8mb4_unicode_520_ci">varchar(192)</span> <i>NULL</i></td><td>
</td></tr><tr><th>email</th><td><span title="utf8mb4_unicode_520_ci">varchar(190)</span></td><td>
</td></tr><tr class="odd"><th>timezone</th><td><span title="utf8mb4_unicode_520_ci">varchar(192)</span> <i>NULL</i></td><td>
</td></tr><tr><th>address_line_1</th><td><span title="utf8mb4_unicode_520_ci">varchar(192)</span> <i>NULL</i></td><td>
</td></tr><tr class="odd"><th>address_line_2</th><td><span title="utf8mb4_unicode_520_ci">varchar(192)</span> <i>NULL</i></td><td>
</td></tr><tr><th>postal_code</th><td><span title="utf8mb4_unicode_520_ci">varchar(192)</span> <i>NULL</i></td><td>
</td></tr><tr class="odd"><th>city</th><td><span title="utf8mb4_unicode_520_ci">varchar(192)</span> <i>NULL</i></td><td>
</td></tr><tr><th>state</th><td><span title="utf8mb4_unicode_520_ci">varchar(192)</span> <i>NULL</i></td><td>
</td></tr><tr class="odd"><th>country</th><td><span title="utf8mb4_unicode_520_ci">varchar(192)</span> <i>NULL</i></td><td>
</td></tr><tr><th>ip</th><td><span title="utf8mb4_unicode_520_ci">varchar(20)</span> <i>NULL</i></td><td>
</td></tr><tr class="odd"><th>latitude</th><td><span title="">decimal(10,8)</span> <i>NULL</i></td><td>
</td></tr><tr><th>longitude</th><td><span title="">decimal(10,8)</span> <i>NULL</i></td><td>
</td></tr><tr class="odd"><th>total_points</th><td><span title="">int unsigned</span> <span title="Default value">[<b>0</b>]</span></td><td>
</td></tr><tr><th>life_time_value</th><td><span title="">int unsigned</span> <span title="Default value">[<b>0</b>]</span></td><td>
</td></tr><tr class="odd"><th>phone</th><td><span title="utf8mb4_unicode_520_ci">varchar(50)</span> <i>NULL</i></td><td>
</td></tr><tr><th>status</th><td><span title="utf8mb4_unicode_520_ci">varchar(50)</span> <span title="Default value">[<b>subscribed</b>]</span></td><td>
</td></tr><tr class="odd"><th>contact_type</th><td><span title="utf8mb4_unicode_520_ci">varchar(50)</span> <i>NULL</i> <span title="Default value">[<b>lead</b>]</span></td><td>
</td></tr><tr><th>source</th><td><span title="utf8mb4_unicode_520_ci">varchar(50)</span> <i>NULL</i></td><td>
</td></tr><tr class="odd"><th>avatar</th><td><span title="utf8mb4_unicode_520_ci">varchar(192)</span> <i>NULL</i></td><td>
</td></tr><tr><th>date_of_birth</th><td><span title="">date</span> <i>NULL</i></td><td>
</td></tr><tr class="odd"><th>created_at</th><td><span title="">timestamp</span> <i>NULL</i></td><td>
</td></tr><tr><th>last_activity</th><td><span title="">timestamp</span> <i>NULL</i></td><td>
</td></tr><tr class="odd"><th>updated_at</th><td><span title="">timestamp</span> <i>NULL</i></td><td>
</td></tr></tbody></table>

---

## FluentBoards Database Schema
Source file : `src/database/index.md`

# FluentBoards Database Schema

<Badge type="tip" vertical="top" text="FluentBoards Core" /> <Badge type="warning" vertical="top" text="Advanced" />

FluentBoards use custom database tables to store all the Boards data. Here are the list of database tables and it's schema to
understand overall database design and related data attributes of each model.
## Schema Design
<img :src="$withBase('/assets/img/schema-design.png')" alt="Schema Design" />

## Database Tables


## _fbs_boards Table

This table stores the basic information of a board.

<table cellspacing="0" class="nowrap">
<thead><tr><th>Column</th><th>Type</th><th>Comment</th></tr></thead>
<tbody>
<tr><th>id</th><td>INT UNSIGNED <i>Auto Increment</i></td><td>Primary key of the board</td></tr>
<tr><th>parent_id</th><td>INT UNSIGNED <i>NULL</i></td><td>For SuperBoard like Project or Company, for sub-board etc.</td></tr>
<tr><th>title</th><td>TEXT <i>NULL</i></td><td>Title of the board, it can be longer than 255 characters.</td></tr>
<tr><th>description</th><td>LONGTEXT <i>NULL</i></td><td>Description of the board</td></tr>
<tr><th>type</th><td>VARCHAR(50) <i>NULL</i></td><td>Type of the board, e.g., to-do, sales-pipeline, roadmap, task, etc.</td></tr>
<tr><th>currency</th><td>VARCHAR(50) <i>NULL</i></td><td>Currency related to the board</td></tr>
<tr><th>background</th><td>TEXT <i>NULL</i></td><td>Serialized array for background settings</td></tr>
<tr><th>settings</th><td>TEXT <i>NULL</i></td><td>Serialized array for other board settings</td></tr>
<tr><th>created_by</th><td>INT UNSIGNED</td><td>ID of the user who created the board</td></tr>
<tr><th>archived_at</th><td>TIMESTAMP <i>NULL</i></td><td>Timestamp when the board was archived</td></tr>
<tr><th>created_at</th><td>TIMESTAMP <i>NULL</i></td><td>Timestamp when the board was created</td></tr>
<tr><th>updated_at</th><td>TIMESTAMP <i>NULL</i></td><td>Timestamp when the board was last updated</td></tr>
</tbody>
</table>


## _fbs_board_terms Table

This table is used for storing the board labels and stages.

<table cellspacing="0" class="nowrap">
<thead><tr><th>Column</th><th>Type</th><th>Comment</th></tr></thead>
<tbody>
<tr><th>id</th><td>INT UNSIGNED <i>Auto Increment</i></td><td>Primary key of the term</td></tr>
<tr><th>board_id</th><td>INT UNSIGNED</td><td>ID of the board associated with the term</td></tr>
<tr><th>title</th><td>VARCHAR(100) <i>NULL</i></td><td>Title of the stage or label. In case of a label, the title can be null with only a color.</td></tr>
<tr><th>slug</th><td>VARCHAR(100) <i>NULL</i></td><td>Slug of the stage or label</td></tr>
<tr><th>type</th><td>VARCHAR(50) NOT NULL DEFAULT 'stage'</td><td>Type of the term: 'stage' or 'label'</td></tr>
<tr><th>position</th><td>DECIMAL(10,2) NOT NULL DEFAULT '1'</td><td>Position of the stage or label. 1 = first, 2 = second, etc.</td></tr>
<tr><th>color</th><td>VARCHAR(50) <i>NULL</i></td><td>Text color of the stage or label</td></tr>
<tr><th>bg_color</th><td>VARCHAR(50) <i>NULL</i></td><td>Background color of the stage or label</td></tr>
<tr><th>settings</th><td>TEXT <i>NULL</i></td><td>Serialized settings for the term</td></tr>
<tr><th>archived_at</th><td>TIMESTAMP <i>NULL</i></td><td>Timestamp when the term was archived</td></tr>
<tr><th>created_at</th><td>TIMESTAMP <i>NULL</i></td><td>Timestamp when the term was created</td></tr>
<tr><th>updated_at</th><td>TIMESTAMP <i>NULL</i></td><td>Timestamp when the term was last updated</td></tr>
</tbody>
</table>

## _fbs_tasks Table

This table is used for managing tasks within the board.

<table cellspacing="0" class="nowrap">
<thead><tr><th>Column</th><th>Type</th><th>Comment</th></tr></thead>
<tbody>
<tr><th>id</th><td>INT UNSIGNED <i>Auto Increment</i></td><td>Primary key of the task</td></tr>
<tr><th>parent_id</th><td>INT UNSIGNED <i>NULL</i></td><td>Parent task ID if this is a subtask</td></tr>
<tr><th>board_id</th><td>INT UNSIGNED <i>NULL</i></td><td>ID of the board the task is in</td></tr>
<tr><th>crm_contact_id</th><td>BIGINT UNSIGNED <i>NULL</i></td><td>User ID, Contact ID, Deal ID, Subscriber ID, etc.</td></tr>
<tr><th>title</th><td>TEXT <i>NULL</i></td><td>Title or name of the task; it can be longer than 255 characters.</td></tr>
<tr><th>slug</th><td>VARCHAR(255) <i>NULL</i></td><td>Slug of the task</td></tr>
<tr><th>type</th><td>VARCHAR(50) <i>NULL</i></td><td>Type of the task, e.g., task, deal, idea, to-do, etc.</td></tr>
<tr><th>status</th><td>VARCHAR(50) <i>NULL</i> DEFAULT 'open'</td><td>Status of the task: open, completed; for boards: won or lost for pipelines</td></tr>
<tr><th>stage_id</th><td>INT UNSIGNED <i>NULL</i></td><td>ID of the stage the task is in</td></tr>
<tr><th>source</th><td>VARCHAR(50) <i>NULL</i> DEFAULT 'web'</td><td>Source of the task, e.g., web, funnel, contact-section, etc.</td></tr>
<tr><th>source_id</th><td>VARCHAR(255) <i>NULL</i></td><td>Source ID related to the task</td></tr>
<tr><th>priority</th><td>VARCHAR(50) <i>NULL</i> DEFAULT 'low'</td><td>Priority of the task: low, medium, high</td></tr>
<tr><th>description</th><td>LONGTEXT <i>NULL</i></td><td>Description of the task</td></tr>
<tr><th>lead_value</th><td>DECIMAL(10,2) DEFAULT 0.00</td><td>Lead value associated with the task</td></tr>
<tr><th>created_by</th><td>BIGINT UNSIGNED <i>NULL</i></td><td>ID of the user who created the task</td></tr>
<tr><th>position</th><td>DECIMAL(10,2) NOT NULL DEFAULT '1'</td><td>Position of the task within the board. 1 = first, 2 = second, etc.</td></tr>
<tr><th>comments_count</th><td>INT UNSIGNED <i>NULL</i> DEFAULT 0</td><td>Number of comments associated with the task</td></tr>
<tr><th>issue_number</th><td>INT UNSIGNED <i>NULL</i></td><td>Board-specific issue number to track the task</td></tr>
<tr><th>reminder_type</th><td>VARCHAR(100) <i>NULL</i> DEFAULT 'none'</td><td>Type of reminder set for the task</td></tr>
<tr><th>settings</th><td>TEXT <i>NULL</i></td><td>Serialized settings for the task</td></tr>
<tr><th>remind_at</th><td>TIMESTAMP <i>NULL</i></td><td>Timestamp when a reminder is set for the task</td></tr>
<tr><th>started_at</th><td>TIMESTAMP <i>NULL</i></td><td>Timestamp when the task was started</td></tr>
<tr><th>due_at</th><td>TIMESTAMP <i>NULL</i></td><td>Timestamp when the task is due</td></tr>
<tr><th>last_completed_at</th><td>TIMESTAMP <i>NULL</i></td><td>Timestamp when the task was last completed</td></tr>
<tr><th>archived_at</th><td>TIMESTAMP <i>NULL</i></td><td>Timestamp when the task was archived</td></tr>
<tr><th>created_at</th><td>TIMESTAMP <i>NULL</i></td><td>Timestamp when the task was created</td></tr>
<tr><th>updated_at</th><td>TIMESTAMP <i>NULL</i></td><td>Timestamp when the task was last updated</td></tr>
</tbody>
</table>


## _fbs_task_metas Table

This table is used for storing metadata related to tasks.

<table cellspacing="0" class="nowrap">
<thead><tr><th>Column</th><th>Type</th><th>Comment</th></tr></thead>
<tbody>
<tr><th>id</th><td>INT UNSIGNED <i>Auto Increment</i></td><td>Primary key of the task meta</td></tr>
<tr><th>task_id</th><td>INT UNSIGNED</td><td>ID of the associated task</td></tr>
<tr><th>key</th><td>VARCHAR(100)</td><td>Key for the meta information</td></tr>
<tr><th>value</th><td>LONGTEXT <i>NULL</i></td><td>Value of the meta information</td></tr>
<tr><th>created_at</th><td>TIMESTAMP <i>NULL</i></td><td>Timestamp when the meta was created</td></tr>
<tr><th>updated_at</th><td>TIMESTAMP <i>NULL</i></td><td>Timestamp when the meta was last updated</td></tr>
</tbody>
</table> 

## _fbs_attachments Table

This table stores information about attachments related to tasks.

<table cellspacing="0" class="nowrap">
<thead><tr><th>Column</th><th>Type</th><th>Comment</th></tr></thead>
<tbody>
<tr><th>id</th><td>INT UNSIGNED <i>Auto Increment</i></td><td>Primary key of the attachment</td></tr>
<tr><th>object_id</th><td>INT UNSIGNED</td><td>ID of the associated object (Task ID, Comment ID, or Board ID)</td></tr>
<tr><th>object_type</th><td>VARCHAR(100) <i>DEFAULT 'TASK'</i></td><td>Type of the object (TASK, COMMENT, BOARD)</td></tr>
<tr><th>attachment_type</th><td>VARCHAR(100) <i>NULL</i></td><td>Type of the attachment</td></tr>
<tr><th>file_path</th><td>TEXT <i>NULL</i></td><td>File path of the attachment</td></tr>
<tr><th>full_url</th><td>TEXT <i>NULL</i></td><td>Full URL of the attachment</td></tr>
<tr><th>settings</th><td>TEXT <i>NULL</i></td><td>Serialized settings</td></tr>
<tr><th>title</th><td>VARCHAR(192) <i>NULL</i></td><td>Title of the attachment</td></tr>
<tr><th>file_hash</th><td>VARCHAR(192) <i>NULL</i></td><td>File hash for verifying integrity</td></tr>
<tr><th>driver</th><td>VARCHAR(100) <i>DEFAULT 'local'</i></td><td>Storage driver (local, cloud, etc.)</td></tr>
<tr><th>status</th><td>VARCHAR(100) <i>DEFAULT 'ACTIVE'</i></td><td>Status of the attachment (ACTIVE, INACTIVE, DELETED)</td></tr>
<tr><th>file_size</th><td>VARCHAR(100) <i>NULL</i></td><td>Size of the file</td></tr>
<tr><th>created_at</th><td>TIMESTAMP <i>NULL</i></td><td>Timestamp when the attachment was created</td></tr>
<tr><th>updated_at</th><td>TIMESTAMP <i>NULL</i></td><td>Timestamp when the attachment was last updated</td></tr>
</tbody>
</table>

## _fbs_comments Table

This table stores comments, notes, and replies related to tasks on boards.

<table cellspacing="0" class="nowrap">
<thead><tr><th>Column</th><th>Type</th><th>Comment</th></tr></thead>
<tbody>
<tr><th>id</th><td>INT UNSIGNED <i>Auto Increment</i></td><td>Primary key of the comment</td></tr>
<tr><th>board_id</th><td>INT UNSIGNED</td><td>ID of the associated board</td></tr>
<tr><th>task_id</th><td>INT UNSIGNED</td><td>ID of the associated task</td></tr>
<tr><th>parent_id</th><td>BIGINT UNSIGNED <i>NULL</i></td><td>ID of the parent comment if it's a reply</td></tr>
<tr><th>type</th><td>VARCHAR(50) <i>DEFAULT 'comment'</i></td><td>Type of the entry (comment, note, reply)</td></tr>
<tr><th>privacy</th><td>VARCHAR(50) <i>DEFAULT 'public'</i></td><td>Privacy level of the comment (public, private)</td></tr>
<tr><th>status</th><td>VARCHAR(50) <i>DEFAULT 'published'</i></td><td>Status of the comment (published, draft, spam)</td></tr>
<tr><th>author_name</th><td>VARCHAR(192) <i>DEFAULT ''</i></td><td>Name of the comment author</td></tr>
<tr><th>author_email</th><td>VARCHAR(192) <i>DEFAULT ''</i></td><td>Email of the comment author</td></tr>
<tr><th>author_ip</th><td>VARCHAR(50) <i>DEFAULT ''</i></td><td>IP address of the comment author</td></tr>
<tr><th>description</th><td>TEXT <i>NULL</i></td><td>Content of the comment</td></tr>
<tr><th>created_by</th><td>BIGINT UNSIGNED <i>NULL</i></td><td>ID of the user who created the comment</td></tr>
<tr><th>created_at</th><td>TIMESTAMP <i>NULL</i></td><td>Timestamp when the comment was created</td></tr>
<tr><th>updated_at</th><td>TIMESTAMP <i>NULL</i></td><td>Timestamp when the comment was last updated</td></tr>
</tbody>
</table>

## _fbs_activities Table

This table stores activity logs for tasks, including changes and actions taken on various objects.

<table cellspacing="0" class="nowrap">
<thead><tr><th>Column</th><th>Type</th><th>Comment</th></tr></thead>
<tbody>
<tr><th>id</th><td>INT UNSIGNED <i>Auto Increment</i></td><td>Primary key of the activity log</td></tr>
<tr><th>object_id</th><td>INT UNSIGNED</td><td>ID of the associated object (e.g., Task ID)</td></tr>
<tr><th>object_type</th><td>VARCHAR(100)</td><td>Type of the object (e.g., Task, Comment, Board)</td></tr>
<tr><th>action</th><td>VARCHAR(50)</td><td>Action performed (e.g., create, update, delete)</td></tr>
<tr><th>column</th><td>VARCHAR(50) <i>NULL</i></td><td>The specific column that was changed (if applicable)</td></tr>
<tr><th>old_value</th><td>VARCHAR(50) <i>NULL</i></td><td>The old value before the change</td></tr>
<tr><th>new_value</th><td>VARCHAR(50) <i>NULL</i></td><td>The new value after the change</td></tr>
<tr><th>description</th><td>LONGTEXT <i>NULL</i></td><td>Description of the activity or change</td></tr>
<tr><th>created_by</th><td>BIGINT UNSIGNED <i>NULL</i></td><td>ID of the user who performed the action</td></tr>
<tr><th>settings</th><td>TEXT <i>NULL</i></td><td>Serialized array for additional settings or metadata</td></tr>
<tr><th>created_at</th><td>TIMESTAMP <i>NULL</i></td><td>Timestamp when the activity was created</td></tr>
<tr><th>updated_at</th><td>TIMESTAMP <i>NULL</i></td><td>Timestamp when the activity was last updated</td></tr>
</tbody>
</table>

## _fbs_notifications Table

This table is designed to store notifications related to task management, including various actions performed on tasks.

<table cellspacing="0" class="nowrap">
<thead><tr><th>Column</th><th>Type</th><th>Comment</th></tr></thead>
<tbody>
<tr><th>id</th><td>INT UNSIGNED <i>Auto Increment</i></td><td>Primary key of the notification</td></tr>
<tr><th>object_id</th><td>INT UNSIGNED</td><td>ID of the associated object (e.g., Task ID, Board ID)</td></tr>
<tr><th>object_type</th><td>VARCHAR(100)</td><td>Type of the object (e.g., Task, Comment, Board)</td></tr>
<tr><th>task_id</th><td>INT UNSIGNED <i>NULL</i></td><td>ID of the task associated with the notification (if applicable)</td></tr>
<tr><th>action</th><td>VARCHAR(255) <i>NULL</i></td><td>Action performed (e.g., task_created, priority_changed)</td></tr>
<tr><th>activity_by</th><td>BIGINT UNSIGNED</td><td>ID of the user who performed the action</td></tr>
<tr><th>description</th><td>LONGTEXT <i>NULL</i></td><td>Description of the notification or action</td></tr>
<tr><th>settings</th><td>TEXT <i>NULL</i></td><td>Serialized array for additional settings or metadata</td></tr>
<tr><th>created_at</th><td>TIMESTAMP <i>NULL</i></td><td>Timestamp when the notification was created</td></tr>
<tr><th>updated_at</th><td>TIMESTAMP <i>NULL</i></td><td>Timestamp when the notification was last updated</td></tr>
</tbody>
</table>

### Keys and Indexes:
- **`object_id`**: Index for the associated object ID.
- **`object_type`**: Index for the type of the associated object.
- **`activity_by`**: Index for the user who performed the action.

## _fbs_notification_users Table

This table is designed to track which users have received and read specific notifications.

<table cellspacing="0" class="nowrap">
<thead><tr><th>Column</th><th>Type</th><th>Comment</th></tr></thead>
<tbody>
<tr><th>id</th><td>INT UNSIGNED <i>Auto Increment</i></td><td>Primary key of the record</td></tr>
<tr><th>notification_id</th><td>INT UNSIGNED <i>NULL</i></td><td>ID of the related notification</td></tr>
<tr><th>user_id</th><td>BIGINT UNSIGNED</td><td>ID of the user who received the notification</td></tr>
<tr><th>marked_read_at</th><td>TIMESTAMP <i>NULL</i></td><td>Timestamp when the notification was marked as read</td></tr>
<tr><th>created_at</th><td>TIMESTAMP <i>NULL</i></td><td>Timestamp when the record was created</td></tr>
<tr><th>updated_at</th><td>TIMESTAMP <i>NULL</i></td><td>Timestamp when the record was last updated</td></tr>
</tbody>
</table>

### Keys and Indexes:
- **`notification_id`**: Index for the related notification ID.
- **`user_id`**: Index for the user ID who received the notification.

## _fbs_teams Table

This table stores information about teams within the system.

<table cellspacing="0" class="nowrap">
<thead><tr><th>Column</th><th>Type</th><th>Comment</th></tr></thead>
<tbody>
<tr><th>id</th><td>INT UNSIGNED <i>Auto Increment</i></td><td>Primary key of the record</td></tr>
<tr><th>parent_id</th><td>INT UNSIGNED <i>NULL</i></td><td>ID of the parent team if this is a sub-team</td></tr>
<tr><th>title</th><td>VARCHAR(100)</td><td>Name of the team</td></tr>
<tr><th>description</th><td>TEXT <i>NULL</i></td><td>Description of the team</td></tr>
<tr><th>type</th><td>VARCHAR(50)</td><td>Type of the team (e.g., project, department)</td></tr>
<tr><th>visibility</th><td>VARCHAR(50) <i>DEFAULT 'VISIBLE'</i></td><td>Visibility of the team (VISIBLE/SECRET)</td></tr>
<tr><th>notifications_enabled</th><td>TINYINT(1) <i>DEFAULT 1</i></td><td>Whether notifications are enabled for the team</td></tr>
<tr><th>settings</th><td>TEXT <i>NULL</i></td><td>Serialized settings for the team</td></tr>
<tr><th>created_by</th><td>BIGINT UNSIGNED</td><td>ID of the user who created the team</td></tr>
<tr><th>created_at</th><td>TIMESTAMP <i>NULL</i></td><td>Timestamp when the team was created</td></tr>
<tr><th>updated_at</th><td>TIMESTAMP <i>NULL</i></td><td>Timestamp when the team was last updated</td></tr>
</tbody>
</table>

### Keys and Indexes:
- **`type`**: Index for the type of team.
- **`visibility`**: Index for the visibility status of the team.
- **`created_by`**: Index for the ID of the user who created the team.
- **`parent_id`**: Index for the parent team ID.
- **`notifications_enabled`**: Index for the notification settings.
- **`title`**: Index for the team title.

## _fbs_metas Table

This table stores metadata associated with various objects in the system.

<table cellspacing="0" class="nowrap">
<thead><tr><th>Column</th><th>Type</th><th>Comment</th></tr></thead>
<tbody>
<tr><th>id</th><td>INT UNSIGNED <i>Auto Increment</i></td><td>Primary key of the record</td></tr>
<tr><th>object_id</th><td>INT UNSIGNED <i>NULL</i></td><td>ID of the associated object (e.g., task, comment)</td></tr>
<tr><th>object_type</th><td>VARCHAR(100)</td><td>Type of the object (e.g., task, comment)</td></tr>
<tr><th>key</th><td>VARCHAR(100) <i>NULL</i></td><td>Metadata key</td></tr>
<tr><th>value</th><td>LONGTEXT <i>NULL</i></td><td>Metadata value</td></tr>
<tr><th>created_at</th><td>TIMESTAMP <i>NULL</i></td><td>Timestamp when the metadata was created</td></tr>
<tr><th>updated_at</th><td>TIMESTAMP <i>NULL</i></td><td>Timestamp when the metadata was last updated</td></tr>
</tbody>
</table>

### Keys and Indexes:
- **`object_id`**: Index for the ID of the associated object.

## _fbs_relations Table

This table manages relationships between different objects.

<table cellspacing="0" class="nowrap">
<thead><tr><th>Column</th><th>Type</th><th>Comment</th></tr></thead>
<tbody>
<tr><th>id</th><td>INT UNSIGNED <i>Auto Increment</i></td><td>Primary key of the record</td></tr>
<tr><th>object_id</th><td>INT UNSIGNED</td><td>ID of the primary object</td></tr>
<tr><th>object_type</th><td>VARCHAR(100)</td><td>Type of the primary object (e.g., task, comment)</td></tr>
<tr><th>foreign_id</th><td>INT UNSIGNED</td><td>ID of the related object</td></tr>
<tr><th>settings</th><td>TEXT <i>NULL</i></td><td>Serialized settings for the relationship</td></tr>
<tr><th>preferences</th><td>TEXT <i>NULL</i></td><td>Serialized preferences for the relationship</td></tr>
<tr><th>created_at</th><td>TIMESTAMP <i>NULL</i></td><td>Timestamp when the relationship was created</td></tr>
<tr><th>updated_at</th><td>TIMESTAMP <i>NULL</i></td><td>Timestamp when the relationship was last updated</td></tr>
</tbody>
</table>

### Keys and Indexes:
- **`object_type`**: Index for the type of the primary object.
- **`object_id`**: Index for the ID of the primary object.
- **`foreign_id`**: Index for the ID of the related object.

## _fbs_time_tracks Table

This table tracks time-related information for tasks.

<table cellspacing="0" class="nowrap">
<thead><tr><th>Column</th><th>Type</th><th>Comment</th></tr></thead>
<tbody>
<tr><th>id</th><td>INT UNSIGNED <i>Auto Increment</i></td><td>Primary key of the record</td></tr>
<tr><th>user_id</th><td>BIGINT UNSIGNED</td><td>ID of the user who tracked the time</td></tr>
<tr><th>board_id</th><td>INT UNSIGNED</td><td>ID of the board</td></tr>
<tr><th>task_id</th><td>INT UNSIGNED</td><td>ID of the task</td></tr>
<tr><th>started_at</th><td>TIMESTAMP <i>NULL</i></td><td>Timestamp when the time tracking started</td></tr>
<tr><th>completed_at</th><td>TIMESTAMP <i>NULL</i></td><td>Timestamp when the time tracking was completed</td></tr>
<tr><th>message</th><td>TEXT <i>NULL</i></td><td>Optional message or note related to the time tracking</td></tr>
<tr><th>status</th><td>VARCHAR(50) <i>NULL DEFAULT 'commited'</i></td><td>Status of the time track (e.g., committed)</td></tr>
<tr><th>working_minutes</th><td>INT UNSIGNED <i>NOT NULL DEFAULT 0</i></td><td>Total minutes worked</td></tr>
<tr><th>billable_minutes</th><td>INT UNSIGNED <i>NOT NULL DEFAULT 0</i></td><td>Minutes that are billable</td></tr>
<tr><th>is_manual</th><td>TINYINT(1) <i>NOT NULL DEFAULT 0</i></td><td>Indicates if the time track was entered manually</td></tr>
<tr><th>created_at</th><td>TIMESTAMP <i>NULL</i></td><td>Timestamp when the record was created</td></tr>
<tr><th>updated_at</th><td>TIMESTAMP <i>NULL</i></td><td>Timestamp when the record was last updated</td></tr>
</tbody>
</table>

### Keys and Indexes:
- **`user_id`**: Index for the ID of the user.
- **`status`**: Index for the status of the time track.
- **`task_id`**: Index for the ID of the task.
- **`board_id`**: Index for the ID of the board.


# _users Table

This table contains information about users, including login details, email, and registration data.

<table cellspacing="0" class="nowrap">
<thead><tr><th>Column</th><th>Type</th><th>Comment</th></tr></thead>
<tbody>
      <tr>
         <th>ID</th>
         <td>Integer</td>
         <td></td>
      </tr>
      <tr>
         <th>user_login</th>
         <td>String</td>
         <td></td>
      </tr>
      <tr>
         <th>user_pass</th>
         <td>String</td>
         <td></td>
      </tr>
      <tr>
         <th>user_nicename</th>
         <td>String</td>
         <td></td>
      </tr>
      <tr>
         <th>user_email</th>
         <td>String</td>
         <td></td>
      </tr>
      <tr>
         <th>user_url</th>
         <td>String</td>
         <td></td>
      </tr>
      <tr>
         <th>user_registered</th>
         <td>Date Time</td>
         <td></td>
      </tr>
      <tr>
         <th>user_activation_key</th>
         <td>String</td>
         <td></td>
      </tr>
      <tr>
         <th>user_status</th>
         <td>Integer</td>
         <td></td>
      </tr>
      <tr>
         <th>display_name</th>
         <td>String</td>
         <td></td>
      </tr>
   </tbody>
</table>

---

## Activity Model
Source file : `src/database/models\activity.md`

# Activity Model

| DB Table Name | {wp_db_prefix}_fbs_Activity                                            |
|---------------|-----------------------------------------------------------------------|
| Schema        | <a :href="$withBase('/database/#fbs-activities-table')">Check Schema</a> |
| Source File   | fluent-boards/app/Models/Activity.php                                    |
| Name Space    | FluentBoards\App\Models                                               |
| Class         | FluentBoards\App\Models\Activity                                         |

## Attributes
<table class="nowrap">
   <thead>
      <tr>
         <th>Attribute</th>
         <td>Data Type</td>
         <td>Activity</td>
      </tr>
   </thead>
    <tbody>
      <tr>
        <th>id</th>
        <td>INT UNSIGNED <i>Auto Increment</i></td>
        <td>Primary key of the activity log</td>
      </tr>
      <tr>
        <th>object_id</th>
        <td>INT UNSIGNED</td>
        <td>ID of the associated object (e.g., Task ID)</td>
      </tr>
      <tr>
        <th>object_type</th>
        <td>VARCHAR(100)</td>
        <td>Type of the object (e.g., Task, Comment, Board)</td>
      </tr>
      <tr>
        <th>action</th>
        <td>VARCHAR(50)</td>
        <td>Action performed (e.g., create, update, delete)</td>
      </tr>
      <tr>
        <th>column</th>
        <td>VARCHAR(50) <i>NULL</i></td>
        <td>The specific column that was changed (if applicable)</td>
      </tr>
      <tr>
        <th>old_value</th>
        <td>VARCHAR(50) <i>NULL</i></td>
        <td>The old value before the change</td>
      </tr>
      <tr>
        <th>new_value</th>
        <td>VARCHAR(50) <i>NULL</i></td>
        <td>The new value after the change</td>
      </tr>
      <tr>
        <th>description</th>
        <td>LONGTEXT <i>NULL</i></td>
        <td>Description of the activity or change</td>
      </tr>
      <tr>
        <th>created_by</th>
        <td>BIGINT UNSIGNED <i>NULL</i></td>
        <td>ID of the user who performed the action</td>
      </tr>
      <tr>
        <th>settings</th>
        <td>TEXT <i>NULL</i></td>
        <td>Serialized array for additional settings or metadata</td>
      </tr>
      <tr>
        <th>created_at</th>
        <td>TIMESTAMP <i>NULL</i></td>
        <td>Timestamp when the activity was created</td>
      </tr>
      <tr>
        <th>updated_at</th>
        <td>TIMESTAMP <i>NULL</i></td>
        <td>Timestamp when the activity was last updated</td>
      </tr>
    </tbody>
</table>

## Usage
Please check <a href="/database/models/">Model Basic</a> for Common methods.

### Accessing Attributes

```php 

$activity = FluentBoards\App\Models\Activity::find(1);

$activity->id; // returns id
$activity->action; // returns action
.......

```

## Scopes

This model has the following scopes that you can use

### type()
Filter activities by object type

#### Usage:

```php 
$activities = FluentBoards\App\Models\Activity::type('task')->get();
```

## Relations
This model has the following relationships that you can use

### board
Access the board associated with the activity

- return `FluentBoards\App\Models\Board` Model Collection

#### Example:
```php 
$board = $activity->board;
```

### task
Access the task associated with the activity

- return `FluentBoards\App\Models\Task` Model Collection

#### Example:
```php 
$task = $activity->task;
```

### user
Access the user who created the activity

- return `FluentBoards\App\Models\User` Model Collection

#### Example:
```php 
$user = $activity->user;
```

---

## Board Model
Source file : `src/database/models\board.md`

# Board Model

| DB Table Name | {wp_db_prefix}_fbs_boards                                             |
|---------------|-----------------------------------------------------------------------|
| Schema        | <a :href="$withBase('/database/#fbs-boards-table')">Check Schema</a> |
| Source File   | fluent-boards/app/Models/Board.php                                    |
| Name Space    | FluentBoards\App\Models                                               |
| Class         | FluentBoards\App\Models\Board                                         |

## Attributes
<table class="nowrap">
   <thead>
      <tr>
         <th>Attribute</th>
         <td>Data Type</td>
         <td>Comment</td>
      </tr>
   </thead>
   <tbody>
      <tr>
         <th>id</th>
         <td>INT UNSIGNED <i>Auto Increment</i></td>
         <td>Primary key of the board</td>
      </tr>
      <tr>
         <th>parent_id</th>
         <td>INT UNSIGNED <i>NULL</i></td>
         <td>For SuperBoard like Project or Company, for sub-board etc.</td>
      </tr>
      <tr> 
         <th>title</th>
         <td>TEXT <i>NULL</i>
         </td><td>Title of the board, it can be longer than 255 characters.</td>
      </tr>
      <tr> 
         <th>description</th>
         <td>LONGTEXT <i>NULL</i></td>
         <td>Description of the board</td>
      </tr>
      <tr>
         <th>type</th>
         <td>VARCHAR(50) <i>NULL</i></td>
         <td>Type of the board, e.g., to-do, sales-pipeline, roadmap, task, etc.</td>
      </tr>
      <tr>
         <th>currency</th>
         <td>VARCHAR(50) <i>NULL</i></td>
         <td>Currency related to the board</td>
      </tr>
      <tr>
         <th>background</th>
         <td>TEXT <i>NULL</i></td>
         <td>Serialized array for background settings</td>
      </tr>
      <tr>
         <th>settings</th>
         <td>TEXT <i>NULL</i></td>
         <td>Serialized array for other board settings</td>
      </tr>
      <tr>
         <th>created_by</th>
         <td>INT UNSIGNED</td>
         <td>ID of the user who created the board</td>
      </tr>
      <tr>
         <th>archived_at</th>
         <td>TIMESTAMP <i>NULL</i>
         </td><td>Timestamp when the board was archived</td>
      </tr>
      <tr>
         <th>created_at</th>
         <td>TIMESTAMP <i>NULL</i></td>
         <td>Timestamp when the board was created</td>
      </tr>
      <tr>
         <th>updated_at</th>
         <td>TIMESTAMP <i>NULL</i></td>
         <td>Timestamp when the board was last updated</td>
      </tr>
    </tbody>
</table>

## Usage
Please check <a href="/database/models/">Model Basic</a> for Common methods.

### Accessing Attributes

```php 

$board = FluentBoards\App\Models\Board::find(1);

$board->id; // returns id
$board->title; // returns title
.......
```

## Scopes

This model has the following scopes that you can use

### byAccessUser($userId)
Filter board by user id

- Parameters
    - $userId - numeric user id

#### Usage:

```php 
// Get all boards by user id
$bards = FluentBoards\App\Models\Board::byAccessUser($userId)->get();
```


## Relations
This model has the following relationships that you can use

### stages
Access the associated stages of a model

- return `FluentBoards\App\Models\Stage` Model Collection

#### Example:
```php 
// Accessing Stages
$boardStages = $board->stages;

// For Filtering by tags relationship

// Get Boards which has stage slug: completed
$boards = FluentBoards\App\Models\Board::whereHas('tasks', function ($query) {
                $query->where('type', 'task');
            })->get();

// Get Boards which does not have stage slug: completed
$campaigns = FluentBoards\App\Models\Board::whereDoesntHave('tasks', function ($query) {
                $query->where('type', 'task');
            })->get();

```

### tasks
Access all the associated tasks of a model

- return `FluentBoards\App\Models\Task` Model Collections

#### Example:
```php 
// Accessing board tasks
$boardTasks = $board->tasks;

// For Filtering by tags relationship

// Get Board which has task type: task
$boards = FluentBoards\App\Models\Board::whereHas('tasks', funtion($query) {
    $query->where('type', 'task');
})->get();

// Get Board which does not have task type: task
$boards = FluentBoards\App\Models\Board::whereDoesntHave('tasks', funtion($query) {
    $query->where('type', 'task');
})->get();
```

### users
Access all the associated users of a Board model

- return `FluentBoards\App\Models\User` Model Collections

#### Example:
```php 
// Accessing All the users of board
$campaignSubjects = $campaign->users;
```

<hr />

## Methods
Along with Global Model methods, this model has few helper methods.

### updateMeta($key, $value)

Update or create a meta entry for the board.

- Parameters
  - $key `string`
  - $key `string`
- Returns `array`

#### Usage
```php 
$meta = $board->updateMeta('enable_stage_change_email', $enable_stage_change_email);
```

---

## Comment Model
Source file : `src/database/models\comment.md`

# Comment Model

| DB Table Name | {wp_db_prefix}_fbs_comment                                            |
|---------------|-----------------------------------------------------------------------|
| Schema        | <a :href="$withBase('/database/#fbs-comments-table')">Check Schema</a> |
| Source File   | fluent-boards/app/Models/Comment.php                                    |
| Name Space    | FluentBoards\App\Models                                               |
| Class         | FluentBoards\App\Models\Comment                                         |

## Attributes
<table class="nowrap">
   <thead>
      <tr>
         <th>Attribute</th>
         <td>Data Type</td>
         <td>Comment</td>
      </tr>
   </thead>
   <tbody>
      <tr>
        <th>id</th>
        <td>INT UNSIGNED <i>Auto Increment</i></td>
        <td>Primary key of the comment</td>
      </tr>
      <tr>
        <th>board_id</th>
        <td>INT UNSIGNED</td>
        <td>ID of the associated board</td>
      </tr>
      <tr>
        <th>task_id</th>
        <td>INT UNSIGNED</td>
        <td>ID of the associated task</td>
      </tr>
      <tr>
        <th>parent_id</th>
        <td>BIGINT UNSIGNED <i>NULL</i></td>
        <td>ID of the parent comment if it's a reply</td>
      </tr>
      <tr>
        <th>type</th>
        <td>VARCHAR(50) <i>DEFAULT 'comment'</i></td>
        <td>Type of the entry (comment, note, reply)</td>
      </tr>
      <tr>
        <th>privacy</th>
        <td>VARCHAR(50) <i>DEFAULT 'public'</i></td>
        <td>Privacy level of the comment (public, private)</td>
      </tr>
      <tr>
        <th>status</th>
        <td>VARCHAR(50) <i>DEFAULT 'published'</i></td>
        <td>Status of the comment (published, draft, spam)</td>
      </tr>
      <tr>
        <th>author_name</th>
        <td>VARCHAR(192) <i>DEFAULT ''</i></td>
        <td>Name of the comment author</td>
      </tr>
      <tr>
        <th>author_email</th>
        <td>VARCHAR(192) <i>DEFAULT ''</i></td>
        <td>Email of the comment author</td>
      </tr>
      <tr>
        <th>author_ip</th>
        <td>VARCHAR(50) <i>DEFAULT ''</i></td>
        <td>IP address of the comment author</td>
      </tr>
      <tr>
        <th>description</th>
        <td>TEXT <i>NULL</i></td>
        <td>Content of the comment</td>
      </tr>
      <tr>
        <th>created_by</th>
        <td>BIGINT UNSIGNED <i>NULL</i></td>
        <td>ID of the user who created the comment</td>
      </tr>
      <tr>
        <th>created_at</th>
        <td>TIMESTAMP <i>NULL</i></td>
        <td>Timestamp when the comment was created</td>
      </tr>
      <tr>
        <th>updated_at</th>
        <td>TIMESTAMP <i>NULL</i></td>
        <td>Timestamp when the comment was last updated</td>
      </tr>
    </tbody>
</table>

## Usage
Please check <a href="/database/models/">Model Basic</a> for Common methods.

### Accessing Attributes

```php 

$comment = FluentBoards\App\Models\Comment::find(1);

$comment->id; // returns id
$comment->author_name; // returns author_name
.......

```

## Relations
This model has the following relationships that you can use

### user
Access the user who created the comment

- return `FluentBoards\App\Models\User` Model Collection

#### Example:
```php 
$user = $comment->user;
```

### task
Access the associated task of the comment

- return `FluentBoards\App\Models\Task` Model Collection

#### Example:
```php 
$task = $comment->task;
```

### replies
Access the replies to the comment

- return `FluentBoards\App\Models\Comment` Model Collection

#### Example:
```php 
$replies = $comment->replies;
```

### parentComment
Access the parent comment if it exists

- return `FluentBoards\App\Models\Comment` Model Collection

#### Example:
```php 
$parent = $comment->parentComment;
```
### images
Access images associated with the comment

- return `FluentBoards\App\Models\CommentImage` Model Collection

#### Example:
```php 
$images = $comment->images;
```

---

## CustomField Model
Source file : `src/database/models\custom-field.md`

# CustomField Model

| DB Table Name | Inherits from `BoardTerm` {wp_db_prefix}_fbs_board_terms |
|---------------|------------------------------------------------------|
| Source File   | fluent-boards-pro/app/Models/CustomField.php         |
| Name Space    | FluentBoardsPro\App\Models                           |
| Class         | FluentBoardsPro\App\Models\CustomField               |


## Relations
This model has the following relationships that you can use

### tasks
Access tasks associated with the CustomField.

- return `FluentCustomFields\App\Models\Task` Model Collection

#### Example:
```php 
$customField = CustomField::find(1);
$tasks = $customField->tasks; // Retrieves tasks associated with this custom field
```

### board
Access board associated with the CustomField.

- return `FluentCustomFields\App\Models\Board` Model Collections

#### Example:
```php 
$customField = CustomField::find(1);
$board = $customField->board; // Retrieves the board associated with this custom field
```

<hr />

---

## Database Model Basic
Source file : `src/database/models\index.md`

# Database Model Basic

## Introduction
FluentBoards ORM provides a beautiful, simple ActiveRecord implementation for working with database tables. Each database table has a corresponding "Model" which is used to interact with that table. Models allow you to query for data in db tables, as well as insert new records into the table.

::: warning NOTE
FluentBoards offers helper functions and methods to interact with FluentBoards's database so you may use those things instead of Models directly. We are documenting these for our internal usage and very-high level usage by 3rd-party developers.
:::


## Built-in FluentBoards DB Models
All the built-in database models are available at

- `fluent-boards/app/Models/` (Free version)
- `fluent-boards-pro/app/Models/` (Pro version)

In this Article we will use `FluentBoards\App\Models\Board` model as an example.

## Retrieving Models
Think of each Eloquent model as a powerful query builder allowing you to fluently query the database table associated with the model. For example:

```php
<?php
 
$boards = FluentBoards\App\Models\Board::all();
 
foreach ($boards as $board) {
    echo $board->title;
}

```

### Adding Additional Constraints

The ORM all method will return all of the results in the model's table. Since each model serves as a query builder, you may also add constraints to queries, and then use the get method to retrieve the results:

```php 
$boards = FluentBoards\App\Models\Boards::where('type', 'to-do')
               ->orderBy('created_at', 'DESC')
               ->limit(10)
               ->skip(5)
               ->get();
```

## Retrieving Single Models / Aggregates

Of course, in addition to retrieving all of the records for a given table, you may also retrieve single records using find or first. Instead of returning a collection of models, these methods return a single model instance:

```php
// Retrieve a model by its primary key...
$board = FluentBoards\App\Models\Board::find(1);
 
// Retrieve the first model matching the query constraints...
$board = FluentBoards\App\Models\Board::where('type', 'to-do')->first();
```

You may also call the find method with an array of primary keys, which will return a collection of the matching records:

```php
$boards = FluentBoards\App\Models\Board::find([1,2,3]);
 ```

## Retrieving Aggregates

You may also use the count, sum, max, and other aggregate methods available. These methods return the appropriate scalar value instead of a full model instance:
```php
$count = FluentBoards\App\Models\Board::where('type', 'to-do')->count();

$max = FluentBoards\App\Models\Board::where('type', 'to-do')->max('id');
```

Available aggregate methods such as `count`, `max`, `min`, `avg`, and `sum`.


# Inserting & Updating Models

## Inserts
To create a new record in the database, create a new model instance, set attributes on the model, then call the save method:

```php 
$board = FluentBoards\App\Models\Board::create([
        'title' => 'My First Board',
        'description'  => 'This is my first board',    
]);
```

## Updates

You can update a model few different way. You can assign property and then call `save()` method

```php 
$board = FluentBoards\App\Models\Board::find(1);

$board->title = 'Updated Title';
$board->description = 'Updated Description';
$board->save();
```

You can also update with an array

```php 
$board = FluentBoards\App\Models\Board::find(1);

$board->update([
    'title' => 'Updated Title',
    'last_name' => 'Updated Description'
]);
```

# Accessing Attributes

You can just call the database table column name for accessing the attributes

```php 
$board = FluentBoards\App\Models\Board::find(1);

$title = $board->title;
$description = $board->description;
```

# Deleting Models

To delete a model, call the delete method on a model instance:

```php 
  $board = FluentBoards\App\Models\Board::find(1);
  $board->delete();
```

### Deleting Models By Query

Of course, you may also run a delete statement on a set of models. In this example, we will delete all flights that are marked as inactive. Like mass updates, mass deletes will not fire any model events for the models that are deleted:

```php
FluentBoards\App\Models\Board::where('type', 'to-do')->delete();
```

# Query Scopes
Scopes allow you to define common sets of constraints that you may easily re-use throughout application. For example, you may need to frequently retrieve all boards by given types.In FluentBoards Board model we already have this scope defined like this.

```php

    /**
     * Local scope to filter boards by search/query string
     * @param \FluentBoards\Framework\Database\Query\Builder $query
     * @param array $types
     * @return \FluentBoards\Framework\Database\Query\Builder $query
     */
    public function scopeFilterByType($query, $types)
    {
        if ($types) {
            $query->whereIn('type', $types);
        }

        return $query;
    }

```

Now say you want to get boards where types equal to-do and roadmap

```php 
$boards = FluentBoards\App\Models\Board::filterByType(['type', 'to-do'])->get();
```
Please note that, the first letter will be small case.

In the individual model documentation, you will find which FluentBoards models have scopes.

# Relationships
Database tables are often related to one another. For example, a board has multiple tasks, or multiple stages. FluentBoards ORM makes managing and working with these relationships easy.
Each Model has predefined relationships and you will find those in the individual model documentation.

```php 

$board = FluentBoards\App\Models\Board::find(1);

// These will return corresponding Tag and List collection
$tasks = $board->tasks;
$stage = $board->stages;

```

For a single relation like and `Task` belongs to a board

```php 

$task = FluentBoards\App\Models\Task::find(1);
$board = $task->board; // will return FluentBoards\App\Models\Board
```

---

## Label Model
Source file : `src/database/models\label.md`

# Label Model

| DB Table Name | {wp_db_prefix}_fbs_board_terms                                              |
|---------------|-----------------------------------------------------------------------------|
| Schema        | <a :href="$withBase('/database/#fbs-board-terms-table')">Check Schema</a> |
| Source File   | fluent-boards/app/Models/Label.php                                          |
| Name Space    | FluentBoards\App\Models                                                     |
| Class         | FluentBoards\App\Models\Label                                               |

## Attributes
<table class="nowrap">
   <thead>
      <tr>
         <th>Attribute</th>
         <td>Data Type</td>
         <td>Comment</td>
      </tr>
   </thead>
   <tbody>
     <tr>
        <th>id</th>
        <td>INT UNSIGNED <i>Auto Increment</i></td>
        <td>Primary key of the term</td>
     </tr>
     <tr>
        <th>board_id</th>
        <td>INT UNSIGNED</td>
        <td>ID of the board associated with the term</td>
     </tr>
     <tr>
        <th>title</th>
        <td>VARCHAR(100) <i>NULL</i></td>
        <td>Title of the stage or label. In case of a label, the title can be null with only a color.</td>
     </tr>
     <tr>
        <th>slug</th>
        <td>VARCHAR(100) <i>NULL</i></td>
        <td>Slug of the stage or label</td>
     </tr>
     <tr>
        <th>type</th>
        <td>VARCHAR(50) NOT NULL DEFAULT 'stage'</td>
        <td>Type of the term: 'stage' or 'label'</td>
     </tr>
     <tr>
        <th>position</th>
        <td>DECIMAL(10,2) NOT NULL DEFAULT '1'</td>
        <td>Position of the stage or label. 1 = first, 2 = second, etc.</td>
     </tr>
     <tr>
        <th>color</th>
        <td>VARCHAR(50) <i>NULL</i></td>
        <td>Text color of the stage or label</td>
     </tr>
     <tr>
        <th>bg_color</th>
        <td>VARCHAR(50) <i>NULL</i></td>
        <td>Background color of the stage or label</td>
     </tr>
     <tr>
        <th>settings</th>
        <td>TEXT <i>NULL</i>
        </td><td>Serialized settings for the term</td>
     </tr>
     <tr>
        <th>archived_at</th>
        <td>TIMESTAMP <i>NULL</i>
        </td><td>Timestamp when the term was archived</td>
     </tr>
     <tr>
        <th>created_at</th>
        <td>TIMESTAMP <i>NULL</i></td>
        <td>Timestamp when the term was created</td>
     </tr>
     <tr>
        <th>updated_at</th>
        <td>TIMESTAMP <i>NULL</i></td>
        <td>Timestamp when the term was last updated</td>
     </tr>
</tbody>
</table>

## Usage
Please check <a href="/database/models/">Model Basic</a> for Common methods.

### Accessing Attributes

```php 

$label = FluentBoards\App\Models\Label::find(1);

$label->id; // returns id
$label->title; // returns title
.......
```

## Relations
This model has the following relationships that you can use

### tasks
Access the associated tasks of a model

- return `FluentBoards\App\Models\Task` Model Collection

#### Example:
```php 
// Accessing Stages
$labelTasks = $label->tasks;

// For Filtering by tags relationship

// Get Labels which has task type: task
$lables = FluentBoards\App\Models\Label::whereHas('tasks', function ($query) {
                $query->where('type', 'task');
            })->get();

// Get Labels which does not have task type: task
$campaigns = FluentBoards\App\Models\Label::whereDoesntHave('tasks', function ($query) {
                $query->where('type', 'task');
            })->get();

```

---

## NotificationUser Model
Source file : `src/database/models\notification-user.md`

# NotificationUser Model

| DB Table Name | {wp_db_prefix}_fbs_NotificationUsers                                             |
|---------------|----------------------------------------------------------------------------------|
| Schema        | <a :href="$withBase('/database/#fbs-notification-users-table')">Check Schema</a> |
| Source File   | fluent-boards/app/Models/NotificationUser.php                                    |
| Name Space    | FluentBoards\App\Models                                               |
| Class         | FluentBoards\App\Models\NotificationUser                              |

## Attributes
<table class="nowrap">
   <thead>
      <tr>
         <th>Attribute</th>
         <td>Data Type</td>
         <td>Comment</td>
      </tr>
   </thead>
    <tbody>
      <tr>
        <th>id</th>
        <td>INT UNSIGNED <i>Auto Increment</i></td>
        <td>Primary key of the record</td>
      </tr>
      <tr>
        <th>notification_id</th>
        <td>INT UNSIGNED <i>NULL</i></td>
        <td>ID of the related notification</td>
      </tr>
      <tr>
        <th>user_id</th>
        <td>BIGINT UNSIGNED</td>
        <td>ID of the user who received the notification</td>
      </tr>
      <tr>
        <th>marked_read_at</th>
        <td>TIMESTAMP <i>NULL</i></td>
        <td>Timestamp when the notification was marked as read</td>
      </tr>
      <tr>
        <th>created_at</th>
        <td>TIMESTAMP <i>NULL</i></td>
        <td>Timestamp when the record was created</td>
      </tr>
      <tr>
        <th>updated_at</th>
        <td>TIMESTAMP <i>NULL</i></td>
        <td>Timestamp when the record was last updated</td>
      </tr>
    </tbody>
</table>

## Usage
Please check <a href="/database/models/">Model Basic</a> for Common methods.

### Accessing Attributes

```php 
$notificationUser = FluentBoards\App\Models\NotificationUser::find(1);

$notificationUser->id; // returns id
$notificationUser->user_id; // returns user_id
.......
```

## Relations
This model has the following relationships that you can use

### notification
Access the associated notification

- return `FluentNotificationUsers\App\Models\Notification` Model Collection

#### Example:
```php 
$notification = $notificationUser->notification;
```

---

## Notification Model
Source file : `src/database/models\notification.md`

# Notification Model

| DB Table Name | {wp_db_prefix}_fbs_notifications                                            |
|---------------|-----------------------------------------------------------------------------|
| Schema        | <a :href="$withBase('/database/#fbs-notifications-table')">Check Schema</a> |
| Source File   | fluent-boards/app/Models/Notification.php                            |
| Name Space    | FluentBoards\App\Models                                              |
| Class         | FluentBoards\App\Models\Notification                                 |

## Attributes
<table class="nowrap">
   <thead>
      <tr>
         <th>Attribute</th>
         <td>Data Type</td>
         <td>Comment</td>
      </tr>
   </thead>
   <tbody>
    <tr>
      <th>id</th>
      <td>INT UNSIGNED <i>Auto Increment</i></td>
      <td>Primary key of the notification</td>
    </tr>
    <tr>
      <th>object_id</th>
      <td>INT UNSIGNED</td>
      <td>ID of the associated object (e.g., Task ID, Board ID)</td>
    </tr>
    <tr>
      <th>object_type</th>
      <td>VARCHAR(100)</td>
      <td>Type of the object (e.g., Task, Comment, Board)</td>
    </tr>
    <tr>
      <th>task_id</th>
      <td>INT UNSIGNED <i>NULL</i></td>
      <td>ID of the task associated with the notification (if applicable)</td>
    </tr>
    <tr>
      <th>action</th>
      <td>VARCHAR(255) <i>NULL</i></td>
      <td>Action performed (e.g., task\_created, priority\_changed)</td>
    </tr>
    <tr>
      <th>activity_by</th>
      <td>BIGINT UNSIGNED</td>
      <td>ID of the user who performed the action</td>
    </tr>
    <tr>
      <th>description</th>
      <td>LONGTEXT <i>NULL</i></td>
      <td>Description of the notification or action</td>
    </tr>
    <tr>
      <th>settings</th>
      <td>TEXT <i>NULL</i></td>
      <td>Serialized array for additional settings or metadata</td>
    </tr>
    <tr>
      <th>created_at</th>
      <td>TIMESTAMP <i>NULL</i></td>
      <td>Timestamp when the notification was created</td>
    </tr>
    <tr>
      <th>updated_at</th>
      <td>TIMESTAMP <i>NULL</i></td>
      <td>Timestamp when the notification was last updated</td>
    </tr>
  </tbody>
</table>

## Usage
Please check <a href="/database/models/">Model Basic</a> for Common methods.

### Accessing Attributes

```php 

$notification = FluentBoards\App\Models\Notification::find(1);

$notification->id; // returns id
$notification->action; // returns action
.......
```

## Relations
This model has the following relationships that you can use

### activitist
Access the user who triggered the activity

- return `FluentNotifications\App\Models\User` Model Collection

#### Example:
```php 
$activitist = $notification->activitist;
```

### board
Access the board associated with the notification

- return `FluentNotifications\App\Models\Board` Model Collections

#### Example:
```php 
$board = $notification->board;
```

### task
Access the task associated with the notification

- return `FluentNotifications\App\Models\Task` Model Collections

#### Example:
```php 
$task = $notification->task;
```

### users
Access the users associated with the notification

- return `FluentNotifications\App\Models\User` Model Collections

#### Example:
```php 
$users = $notification->users;
```

<hr />

## Methods
Along with Global Model methods, this model has few helper methods.

### checkReadOrNot

Check if the notification has been read by the current user.

#### Usage
```php 
$isRead = $notification->checkReadOrNot();
```

---

## Stage Model
Source file : `src/database/models\stage.md`

# Stage Model

| DB Table Name | {wp_db_prefix}_fbs_board_terms                                              |
|---------------|-----------------------------------------------------------------------------|
| Schema        | <a :href="$withBase('/database/#fbs-board-terms-table')">Check Schema</a> |
| Source File   | fluent-boards/app/Models/Stage.php                                          |
| Name Space    | FluentBoards\App\Models                                                     |
| Class         | FluentBoards\App\Models\Stage                                               |

## Attributes
<table class="nowrap">
   <thead>
      <tr>
         <th>Attribute</th>
         <td>Data Type</td>
         <td>Comment</td>
      </tr>
   </thead>
   <tbody>
     <tr>
        <th>id</th>
        <td>INT UNSIGNED <i>Auto Increment</i></td>
        <td>Primary key of the term</td>
     </tr>
     <tr>
        <th>board_id</th>
        <td>INT UNSIGNED</td>
        <td>ID of the board associated with the term</td>
     </tr>
     <tr>
        <th>title</th>
        <td>VARCHAR(100) <i>NULL</i></td>
        <td>Title of the stage or label. In case of a label, the title can be null with only a color.</td>
     </tr>
     <tr>
        <th>slug</th>
        <td>VARCHAR(100) <i>NULL</i></td>
        <td>Slug of the stage or label</td>
     </tr>
     <tr>
        <th>type</th>
        <td>VARCHAR(50) NOT NULL DEFAULT 'stage'</td>
        <td>Type of the term: 'stage' or 'label'</td>
     </tr>
     <tr>
        <th>position</th>
        <td>DECIMAL(10,2) NOT NULL DEFAULT '1'</td>
        <td>Position of the stage or label. 1 = first, 2 = second, etc.</td>
     </tr>
     <tr>
        <th>color</th>
        <td>VARCHAR(50) <i>NULL</i></td>
        <td>Text color of the stage or label</td>
     </tr>
     <tr>
        <th>bg_color</th>
        <td>VARCHAR(50) <i>NULL</i></td>
        <td>Background color of the stage or label</td>
     </tr>
     <tr>
        <th>settings</th>
        <td>TEXT <i>NULL</i>
        </td><td>Serialized settings for the term</td>
     </tr>
     <tr>
        <th>archived_at</th>
        <td>TIMESTAMP <i>NULL</i>
        </td><td>Timestamp when the term was archived</td>
     </tr>
     <tr>
        <th>created_at</th>
        <td>TIMESTAMP <i>NULL</i></td>
        <td>Timestamp when the term was created</td>
     </tr>
     <tr>
        <th>updated_at</th>
        <td>TIMESTAMP <i>NULL</i></td>
        <td>Timestamp when the term was last updated</td>
     </tr>
</tbody>
</table>

## Usage
Please check <a href="/database/models/">Model Basic</a> for Common methods.

### Accessing Attributes

```php 

$stage = FluentBoards\App\Models\Stage::find(1);

$stage->id; // returns id
$stage->title; // returns title
.......
```

## Methods
Along with Global Model methods, this model has few helper methods.

### moveToNewPosition($newIndex)

Move the stage to a new position within the board. This method repositions the stage to the specified index within the board. If the new position is already taken, it reindexes the positions of all stages and retries the move operation.

- Parameters
  - $newIndex `numeric`
- Returns `array` updated stage

#### Usage
```php 
$stage->moveToNewPosition($position);
```

---

## TaskAttachment Model
Source file : `src/database/models\task-attachment.md`

# TaskAttachment Model

| DB Table Name | Inherits from `BoardTerm` {wp_db_prefix}_fbs_board_terms | 
|---------------|----------------------------------------------------------|
| Source File   | fluent-boards-pro/app/Models/TaskAttachment.php          |
| Name Space    | FluentBoardsPro\App\Models                            |
| Class         | FluentBoardsPro\App\Models\TaskAttachment                |


## Relations
This model has the following relationships that you can use

### tasks
Access task associated with the TaskAttachment.

- return `FluentTaskAttachments\App\Models\Task` Model Collection

#### Example:
```php 
$attachment = TaskAttachment::find(1);
$task = $attachment->task; // Retrieves the task associated with this attachment
```

<hr />

---

## TaskMeta Model
Source file : `src/database/models\task-meta.md`

# TaskMeta Model

| DB Table Name | {wp_db_prefix}_fbs_task_metas                                            |
|---------------|--------------------------------------------------------------------------|
| Schema        | <a :href="$withBase('/database/#fbs-task-metas-table')">Check Schema</a> |
| Source File   | fluent-boards/app/Models/TaskMeta.php                                    |
| Name Space    | FluentBoards\App\Models                                               |
| Class         | FluentBoards\App\Models\TaskMeta                                      |

## Attributes
<table class="nowrap">
   <thead>
      <tr>
         <th>Attribute</th>
         <td>Data Type</td>
         <td>Comment</td>
      </tr>
   </thead>
    <tbody>
      <tr>
        <th>id</th>
        <td>INT UNSIGNED <i>Auto Increment</i></td>
        <td>Primary key of the task meta</td>
      </tr>
      <tr>
        <th>task_id</th>
        <td>INT UNSIGNED</td>
        <td>ID of the associated task</td>
      </tr>
      <tr>
        <th>key</th>
        <td>VARCHAR(100)</td>
        <td>Key for the meta information</td>
      </tr>
      <tr>
        <th>value</th>
        <td>LONGTEXT <i>NULL</i></td>
        <td>Value of the meta information</td>
      </tr>
      <tr>
        <th>created_at</th>
        <td>TIMESTAMP <i>NULL</i></td>
        <td>Timestamp when the meta was created</td>
      </tr>
      <tr>
        <th>updated_at</th>
        <td>TIMESTAMP <i>NULL</i></td>
        <td>Timestamp when the meta was last updated</td>
      </tr>
    </tbody>
</table>

## Usage
Please check <a href="/database/models/">Model Basic</a> for Common methods.

### Accessing Attributes

```php 
$taskMeta = FluentBoards\App\Models\TaskMeta::find(1);

$taskMeta->id; // returns id
$taskMeta->key; // returns key
$taskMeta->value; // returns value (unserialized)
.......
```

## Relations
This model has the following relationships that you can use

### task
Access the associated task

- return `FluentTaskMetas\App\Models\Task` Model Collection

#### Example:
```php 
$task = $taskMeta->task;
```

---

## Task Model
Source file : `src/database/models\task.md`

# Task Model

| DB Table Name | {wp_db_prefix}_fbs_tasks                                            |
|---------------|---------------------------------------------------------------------|
| Schema        | <a :href="$withBase('/database/#fbs-tasks-table')">Check Schema</a> |
| Source File   | fluent-boards/app/Models/Task.php                                   |
| Name Space    | FluentBoards\App\Models                                             |
| Class         | FluentBoards\App\Models\Task                                        |

## Attributes
<table class="nowrap">
   <thead>
      <tr>
         <th>Attribute</th>
         <td>Data Type</td>
         <td>Comment</td>
      </tr>
   </thead>
   <tbody>
      <tr>
         <th>id</th>
         <td>INT UNSIGNED <i>Auto Increment</i></td>
         <td>Primary key of the task</td>
      </tr>
      <tr>
         <th>parent_id</th>
         <td>INT UNSIGNED <i>NULL</i></td>
         <td>Parent task ID if this is a subtask</td>
      </tr>
      <tr>
         <th>board_id</th>
         <td>INT UNSIGNED <i>NULL</i></td>
         <td>ID of the board the task is in</td>
      </tr>
      <tr>
         <th>crm_contact_id</th>
         <td>BIGINT UNSIGNED <i>NULL</i></td>
         <td>User ID, Contact ID, Deal ID, Subscriber ID, etc.</td>
      </tr>
      <tr>
         <th>title</th>
         <td>TEXT <i>NULL</i></td>
         <td>Title or name of the task; it can be longer than 255 characters.</td>
      </tr>
      <tr>
         <th>slug</th>
         <td>VARCHAR(255) <i>NULL</i></td>
         <td>Slug of the task</td>
      </tr>
      <tr>
         <th>type</th>
         <td>VARCHAR(50) <i>NULL</i></td>
         <td>Type of the task, e.g., task, deal, idea, to-do, etc.</td>
      </tr>
      <tr>
         <th>status</th>
         <td>VARCHAR(50) <i>NULL</i> DEFAULT 'open'</td>
         <td>Status of the task: open, completed; for boards: won or lost for pipelines</td>
      </tr>
      <tr>
         <th>stage_id</th>
         <td>INT UNSIGNED <i>NULL</i></td>
         <td>ID of the stage the task is in</td>
      </tr>
      <tr>
         <th>source</th>
         <td>VARCHAR(50) <i>NULL</i> DEFAULT 'web'</td>
         <td>Source of the task, e.g., web, funnel, contact-section, etc.</td>
      </tr>
      <tr>
         <th>source_id</th>
         <td>VARCHAR(255) <i>NULL</i></td>
         <td>Source ID related to the task</td>
      </tr>
      <tr>
         <th>priority</th>
         <td>VARCHAR(50) <i>NULL</i> DEFAULT 'low'</td>
         <td>Priority of the task: low, medium, high</td>
      </tr>
      <tr>
         <th>description</th>
         <td>LONGTEXT <i>NULL</i></td>
         <td>Description of the task</td>
      </tr>
      <tr>
         <th>lead_value</th>
         <td>DECIMAL(10,2) DEFAULT 0.00</td>
         <td>Lead value associated with the task</td>
      </tr>
      <tr>
         <th>created_by</th>
         <td>BIGINT UNSIGNED <i>NULL</i></td>
         <td>ID of the user who created the task</td>
      </tr>
      <tr>
         <th>position</th>
         <td>DECIMAL(10,2) NOT NULL DEFAULT '1'</td>
         <td>Position of the task within the board. 1 = first, 2 = second, etc.</td>
      </tr>
      <tr>
         <th>comments_count</th>
         <td>INT UNSIGNED <i>NULL</i> DEFAULT 0</td>
         <td>Number of comments associated with the task</td>
      </tr>
      <tr>
         <th>issue_number</th>
         <td>INT UNSIGNED <i>NULL</i></td>
         <td>Board-specific issue number to track the task</td>
      </tr>
      <tr>
         <th>reminder_type</th>
         <td>VARCHAR(100) <i>NULL</i> DEFAULT 'none'</td>
         <td>Type of reminder set for the task</td>
      </tr>
      <tr>
         <th>settings</th>
         <td>TEXT <i>NULL</i></td>
         <td>Serialized settings for the task</td>
      </tr>
      <tr>
         <th>remind_at</th>
         <td>TIMESTAMP <i>NULL</i></td>
         <td>Timestamp when a reminder is set for the task</td>
      </tr>
      <tr>
         <th>started_at</th>
         <td>TIMESTAMP <i>NULL</i></td>
         <td>Timestamp when the task was started</td>
      </tr>
      <tr>
         <th>due_at</th>
         <td>TIMESTAMP <i>NULL</i></td>
         <td>Timestamp when the task is due</td>
      </tr>
      <tr>
         <th>last_completed_at</th>
         <td>TIMESTAMP <i>NULL</i></td>
         <td>Timestamp when the task was last completed</td>
      </tr>
      <tr>
         <th>archived_at</th>
         <td>TIMESTAMP <i>NULL</i></td>
         <td>Timestamp when the task was archived</td>
      </tr>
      <tr>
         <th>created_at</th>
         <td>TIMESTAMP <i>NULL</i></td>
         <td>Timestamp when the task was created</td>
      </tr>
      <tr>
         <th>updated_at</th>
         <td>TIMESTAMP <i>NULL</i></td>
         <td>Timestamp when the task was last updated</td>
      </tr>
   </tbody>
</table>
## Usage
Please check <a href="/database/models/">Model Basic</a> for Common methods.

### Accessing Attributes

```php 

$task = FluentBoards\App\Models\Task::find(1);

$task->id; // returns id
$task->title; // returns title
.......
```

## Scopes

This model has the following scopes that you can use

## Scopes

This model has the following scopes that you can use

### type($type)
Filter task by type

- Parameters
  - $type - `string` - Type of the task

#### Usage:

```php 
// Get all boards by user id
$task = FluentBoards\App\Models\Task::type('task')->get();
```

### upcoming()
To check is task upcoming

#### Usage:

```php 
// Is task upcoming
$upcoming = $task->upcoming();
```

### isOverdue()
To check is task overdue

#### Usage:

```php 
// Is task upcoming
$upcoming = $task->isOverdue();
```


## Relations
This model has the following relationships that you can use

### board
Access the associated stages of a model

- return `FluentBoards\App\Models\Board` Model Collection

#### Example:
```php 
// Accessing Board
$taskBoard = $task->board;

```

### stage
Access the associated stages of a task model

- return `FluentBoards\App\Models\Stage` Model Collection

#### Example:
```php 
// Accessing Stage
$taskStage = $task->stage;

```


### labels
Access all the associated labels of a task model

- return `FluentBoards\App\Models\Label` Model Collections

#### Example:
```php 
// Accessing task labels
$taskTasks = $task->labels;

// For Filtering by tags relationship

// Get Task which has label slug: green
$tasks = FluentBoards\App\Models\Task::whereHas('labels', funtion($query) {
    $query->where('slug', 'green');
})->get();

// Get Task which does not have label slug: green
$tasks = FluentBoards\App\Models\Board::whereDoesntHave('tasks', funtion($query) {
    $query->where('slug', 'green');
})->get();
```

### subtasks
Access all the associated subtasks of a task model

- return `FluentBoards\App\Models\Task` Model Collections

#### Example:
```php 
// Accessing task subtasks
$subtasks = $task->subtasks;

// For Filtering by tags relationship

// Get Tasks which has subtask status: open
$tasks = FluentBoards\App\Models\Task::whereHas('subtasks', funtion($query) {
    $query->where('status', 'open');
})->get();

// Get Tasks which does not have subtask status: open
$tasks = FluentBoards\App\Models\Board::whereDoesntHave('tasks', funtion($query) {
    $query->where('status', 'open');
})->get();
```

### parentTask
Access all the associated parentTask of a task model

- return `FluentBoards\App\Models\Task` Model Collections

#### Example:
```php 
// Accessing task subtasks
$parentTask = $task->parentTask;

```

### assignees
Access all the associated assignees of a task model

- return `FluentBoards\App\Models\User` Model Collections

#### Example:
```php 
// Accessing task assignees
$assignees = $task->assignees;

// For Filtering by assignees relationship

// Get Tasks which have assignee with id 1
$tasks = FluentBoards\App\Models\Task::whereHas('assignees', function($query) {
    $query->where('ID', 1);
})->get();

// Get Tasks which do not have assignee with id 1
$tasks = FluentBoards\App\Models\Task::whereDoesntHave('assignees', function($query) {
    $query->where('ID', 1);
})->get();
```

### watchers
Access all the associated watchers of a task model

- return `FluentBoards\App\Models\User` Model Collections

#### Example:
```php 
// Accessing task watchers
$watchers = $task->watchers;

// For filtering by watchers relationship

// Get Tasks which have a watcher with user id 1
$tasks = FluentBoards\App\Models\Task::whereHas('watchers', function($query) {
    $query->where('foreign_id', 1)
          ->where('object_type', Constant::OBJECT_TYPE_USER_TASK_WATCH);
})->get();

// Get Tasks which do not have a watcher with user id 1
$tasks = FluentBoards\App\Models\Task::whereDoesntHave('watchers', function($query) {
    $query->where('foreign_id', 1)
          ->where('object_type', Constant::OBJECT_TYPE_USER_TASK_WATCH);
})->get();

```

### attachments
Access all the associated attachments of a task model

- return `FluentBoards\App\Models\TaskAttachment` Model Collections

#### Example:
```php 
// Accessing task attachments
$attachments = $task->attachments;

// For filtering by attachments relationship

// Get Tasks which have attachments
$tasks = FluentBoards\App\Models\Task::whereHas('attachments', function($query) {
    $query->where('object_type', Constant::OBJECT_TYPE_TASK);
})->get();

// Get Tasks which do not have attachments
$tasks = FluentBoards\App\Models\Task::whereDoesntHave('attachments', function($query) {
    $query->where('object_type', Constant::OBJECT_TYPE_TASK);
})->get();

```

### comments
Access all the associated comments of a task model

- return `FluentBoards\App\Models\Comment` Model Collections

#### Example:
```php 
// Accessing task comments
$comments = $task->comments;

// For filtering by comments relationship

// Get Tasks which have comments
$tasks = FluentBoards\App\Models\Task::whereHas('comments', function($query) {
    $query->where('type', 'comment')
          ->where('parent_id', null);
})->get();

// Get Tasks which do not have comments
$tasks = FluentBoards\App\Models\Task::whereDoesntHave('comments', function($query) {
    $query->where('type', 'comment')
          ->where('parent_id', null);
})->get();

```

### public_comments
Access all the associated public_comments of a task model

- return `FluentBoards\App\Models\Comment` Model Collections

#### Example:
```php 
// Accessing public comments for a task
$publicComments = $task->public_comments;

// For filtering by public comments relationship

// Get Tasks which have public comments
$tasks = FluentBoards\App\Models\Task::whereHas('public_comments')->get();

// Get Tasks which do not have public comments
$tasks = FluentBoards\App\Models\Task::whereDoesntHave('public_comments')->get();

```

### activities
Access all the associated activities of a task model

- return `FluentBoards\App\Models\Activity` Model Collections

#### Example:
```php 
// Accessing task activities
$activities = $task->activities;

// For filtering by activities relationship

// Get Tasks which have activities
$tasks = FluentBoards\App\Models\Task::whereHas('activities', function($query) {
    $query->where('object_type', Constant::ACTIVITY_TASK);
})->get();

// Get Tasks which do not have activities
$tasks = FluentBoards\App\Models\Task::whereDoesntHave('activities', function($query) {
    $query->where('object_type', Constant::ACTIVITY_TASK);
})->get();

```

### customFields
Access all the associated customFields of a task model

- return `FluentBoards\App\Models\CustomField` Model Collections

#### Example:
```php 
// Accessing task custom fields
$customFields = $task->customFields;

// For filtering by custom fields relationship

// Get Tasks which have a custom field with a specific ID
$tasks = FluentBoards\App\Models\Task::whereHas('customFields', function($query) {
    $query->where('foreign_id', 1)
          ->where('object_type', ProConstant::TASK_CUSTOM_FIELD);
})->get();

// Get Tasks which do not have a custom field with a specific ID
$tasks = FluentBoards\App\Models\Task::whereDoesntHave('customFields', function($query) {
    $query->where('foreign_id', 1)
          ->where('object_type', ProConstant::TASK_CUSTOM_FIELD);
})->get();

```

### notifications
Access all the associated notifications of a task model

- return `FluentBoards\App\Models\Notification` Model Collections

#### Example:
```php 
// Accessing task notifications
$notifications = $task->notifications;

// For filtering by notifications relationship

// Get Tasks which have notifications
$tasks = FluentBoards\App\Models\Task::whereHas('notifications')->get();

// Get Tasks which do not have notifications
$tasks = FluentBoards\App\Models\Task::whereDoesntHave('notifications')->get();

```

### taskMeta
Access all the associated taskMeta of a task model

- return `FluentBoards\App\Models\TaskMeta` Model Collections

#### Example:
```php 
// Accessing task metadata
$taskMeta = $task->taskMeta;

// For filtering by task metadata relationship

// Get Tasks which have metadata
$tasks = FluentBoards\App\Models\Task::whereHas('taskMeta')->get();

// Get Tasks which do not have metadata
$tasks = FluentBoards\App\Models\Task::whereDoesntHave('taskMeta')->get();

```

## Methods
Along with Global Model methods, this model has few helper methods.

### createTask($data)

Create a new task.

- Parameters
  - $data `array`: An associative array containing the task data. The array may include keys for 'assignees' and 'labels', among others.
- Returns `Task`: The created task instance.

#### Usage
```php 
$data = [
    'title' => 'New Task Title', // required
    'description' => 'Description of the task', // optional
    'board_id' => 1, // required
    'stage_id' => 1, // required
];

$createdTask = $this->createTask($data);

```

### addOrRemoveAssignee($idToAddOrRemove)

Add or remove an assignee from the task based on their current assignment status.

- Parameters
  - $idToAddOrRemove `int`: The ID of the user to add or remove as an assignee.
- Returns `string`: The operation performed, either `'added'` or `'removed'`.

#### Usage
```php 
$idToModify = 123; // User ID to add or remove

$operation = $task->addOrRemoveAssignee($idToModify);

echo "The user was " . $operation . " as an assignee.";

```

### moveToNewPosition($newIndex)

Move the task to a new position in the list, adjusting the positions of other tasks as necessary.

- Parameters
  - $newIndex `int`: The new position index where the task should be moved. This index is 1-based.
- Returns `self`:  The updated task instance with the new position.

#### Usage
```php 
$newIndex = 3; // The desired new position of the task

$updatedTask = $task->moveToNewPosition($newIndex);

echo "The task has been moved to position " . $updatedTask->position;
```

### adjustSubtaskCount($subTaskParentId)

Adjust the subtask count for a given parent task by updating its settings.

- Parameters
  - $subTaskParentId `int`: The ID of the parent task whose subtask count needs to be updated.
- Returns `void`:  This method does not return a value.

#### Usage
```php 
$parentTaskId = 123; // The ID of the parent task

Task::adjustSubtaskCount($parentTaskId);
```
### updateMeta($key, $value)

Update an existing meta entry or create a new one for the task.

- Parameters
  - $key `string`: The key of the meta entry.
  - $value `mixed`: The value to associate with the key.
- Returns `TaskMeta`: The updated or newly created `TaskMeta` instance.

#### Usage
```php 
$key = 'is_template';
$value = 'yes';

$meta = $task->updateMeta($key, $value);

echo "Meta updated with key: " . $meta->key . " and value: " . $meta->value;

```

### getMeta($key, $default = null)

Retrieve the value of a meta entry for the task. If the meta entry does not exist, return a default value.

- Parameters
  - $key `string`: The key of the meta entry to retrieve.
  - $default `mixed`: The default value to return if the meta entry does not exist. Defaults to `null`.
- Returns `mixed`: The value of the meta entry if it exists, otherwise the default value.

#### Usage
```php 
$key = 'is_template';
$default = 'yes';

$value = $task->getMeta($key, $default);

echo "The meta value is: " . $value;

```

### close()

Mark the task as closed by updating its status and setting the completion time.

- Parameters
  - None.
- Returns `self`: The updated task instance.

#### Usage
```php 
$task = $task->close();

echo "The task has been closed and its status is now: " . $task->status;

```

### reopen()

Reopen the task by changing its status to open and clearing the completion time.

- Parameters
  - None.
- Returns `self`: The updated task instance.

#### Usage
```php 
$task = $task->reopen();

echo "The task has been reopened and its status is now: " . $task->status;

```

---

## Team Model
Source file : `src/database/models\team.md`

# Team Model

| DB Table Name | {wp_db_prefix}_fbs_teams                                            |
|---------------|---------------------------------------------------------------------|
| Schema        | <a :href="$withBase('/database/#fbs-teams-table')">Check Schema</a> |
| Source File   | fluent-boards/app/Models/Team.php                                   |
| Name Space    | FluentBoards\App\Models                                              |
| Class         | FluentBoards\App\Models\Team                                         |

## Attributes
<table class="nowrap">
   <thead>
      <tr>
         <th>Attribute</th>
         <td>Data Type</td>
         <td>Comment</td>
      </tr>
   </thead>
    <tbody>
      <tr>
        <th>id</th>
        <td>INT UNSIGNED <i>Auto Increment</i></td>
        <td>Primary key of the record</td>
      </tr>
      <tr>
        <th>parent_id</th>
        <td>INT UNSIGNED <i>NULL</i></td>
        <td>ID of the parent team if this is a sub-team</td>
      </tr>
      <tr>
        <th>title</th>
        <td>VARCHAR(100)</td>
        <td>Name of the team</td>
      </tr>
      <tr>
        <th>description</th>
        <td>TEXT <i>NULL</i></td>
        <td>Description of the team</td>
      </tr>
      <tr>
        <th>type</th>
        <td>VARCHAR(50)</td>
        <td>Type of the team (e.g., project, department)</td>
      </tr>
      <tr>
        <th>visibility</th>
        <td>VARCHAR(50) <i>DEFAULT 'VISIBLE'</i></td>
        <td>Visibility of the team (VISIBLE/SECRET)</td>
      </tr>
      <tr>
        <th>notifications_enabled</th>
        <td>TINYINT(1) <i>DEFAULT 1</i></td>
        <td>Whether notifications are enabled for the team</td>
      </tr>
      <tr>
        <th>settings</th>
        <td>TEXT <i>NULL</i></td>
        <td>Serialized settings for the team</td>
      </tr>
      <tr>
        <th>created_by</th>
        <td>BIGINT UNSIGNED</td>
        <td>ID of the user who created the team</td>
      </tr>
      <tr>
        <th>created_at</th>
        <td>TIMESTAMP <i>NULL</i></td>
        <td>Timestamp when the team was created</td>
      </tr>
      <tr>
        <th>updated_at</th>
        <td>TIMESTAMP <i>NULL</i></td>
        <td>Timestamp when the team was last updated</td>
      </tr>
    </tbody>
</table>

## Usage
Please check <a href="/database/models/">Model Basic</a> for Common methods.

### Accessing Attributes

```php 
$team = FluentBoards\App\Models\Team::find(1);

$team->id; // returns id
$team->name; // returns name
$team->settings; // returns settings (unserialized)
.......
```

## Relations
This model has the following relationships that you can use

### parent
Access the parent team, if any

- return `FluentTeams\App\Models\Team` Model Collection

#### Example:
```php 
$parentTeam = $team->parent;
```

---

## User Model
Source file : `src/database/models\user.md`

# User Model

| DB Table Name | {wp_db_prefix}_users                                            |
|---------------|-----------------------------------------------------------------|
| Schema        | <a :href="$withBase('/database/#users-table')">Check Schema</a> |
| Source File   | fluent-boards/app/Models/User.php                               |
| Name Space    | FluentBoards\App\Models                                          |
| Class         | FluentBoards\App\Models\User                                     |

## Attributes
<table class="nowrap">
   <thead>
      <tr>
         <th>Attribute</th>
         <td>Data Type</td>
         <td>Comment</td>
      </tr>
   </thead>
   <tbody>
      <tr>
         <th>ID</th>
         <td>Integer</td>
         <td></td>
      </tr>
      <tr>
         <th>user_login</th>
         <td>String</td>
         <td></td>
      </tr>
      <tr>
         <th>user_pass</th>
         <td>String</td>
         <td></td>
      </tr>
      <tr>
         <th>user_nicename</th>
         <td>String</td>
         <td></td>
      </tr>
      <tr>
         <th>user_email</th>
         <td>String</td>
         <td></td>
      </tr>
      <tr>
         <th>user_url</th>
         <td>String</td>
         <td></td>
      </tr>
      <tr>
         <th>user_registered</th>
         <td>Date Time</td>
         <td></td>
      </tr>
      <tr>
         <th>user_activation_key</th>
         <td>String</td>
         <td></td>
      </tr>
      <tr>
         <th>user_status</th>
         <td>Integer</td>
         <td></td>
      </tr>
      <tr>
         <th>display_name</th>
         <td>String</td>
         <td></td>
      </tr>
   </tbody>
</table>

## Usage
Please check <a href="/database/models/">Model Basic</a> for Common methods.

### Accessing Attributes

```php 

$user = FluentBoards\App\Models\User::find(1);

$user->ID; // returns user ID
$user->user_email; // returns email
.......
```


## Relations
This model has the following relationships that you can use

### tasks
Access tasks associated with the user.

- return `FluentUsers\App\Models\Task` Model Collection

#### Example:
```php 
$userTasks = $user->tasks;
```

### watchingTasks
Access tasks that the user is watching.

- return `FluentUsers\App\Models\Task` Model Collections

#### Example:
```php 
$watchingTasks = $user->watchingTasks;
```

### highPriorityTasks
Access all the associated users of a User model

- return `FluentUsers\App\Models\Task` Model Collections

#### Example:
```php 
$highPriorityTasks = $user->highPriorityTasks;
```

### overDueTasks
Access overdue tasks associated with the user.

- return `FluentUsers\App\Models\Task` Model Collections

#### Example:
```php 
$overDueTasks = $user->overDueTasks;
```

### upcomingTasks
Access upcoming tasks associated with the user.

- return `FluentUsers\App\Models\Task` Model Collections

#### Example:
```php 
$upcomingTasks = $user->upcomingTasks;
```


### upcomingWithoutDuedate
Access upcoming tasks without a due date.

- return `FluentUsers\App\Models\Task` Model Collections

#### Example:
```php 
$upcomingTasksNoDueDate = $user->upcomingWithoutDuedate;
```


### boards
Access boards associated with the user.

- return `FluentUsers\App\Models\Board` Model Collections

#### Example:
```php 
$userBoards = $user->boards;
```

### whichBoards
Access boards where the user has a specific relationship.

- return `FluentUsers\App\Models\Board` Model Collections

#### Example:
```php 
$userWhichBoards = $user->whichBoards;
```

### notifications
Access notifications associated with the user.

- return `FluentUsers\App\Models\Notification` Model Collections

#### Example:
```php 
$userNotifications = $user->notifications;
```

<hr />

---

## Webhook Model
Source file : `src/database/models\webhook.md`

# Webhook Model

| DB Table Name | Inherits from the `Meta` model {wp_db_prefix}_fbs_metas |
|---------------|---------------------------------------------------------|
| Source File   | fluent-boards/app/Models/Webhook.php                    |
| Name Space    | FluentBoards\App\Models                               |
| Class         | FluentBoards\App\Models\Webhook                       |

## Attributes
* object_id: The ID of the object associated with the webhook.
* object_type: The type of the object, which is always 'webhook' for this model.
* key: A unique identifier for the webhook, generated using wp_generate_uuid4().
* value: Stores the data associated with the webhook, including the URL.


## Methods
Along with Global Model methods, this model has few helper methods.


### getFields
This method returns an array of fields that are mappable in tasks.

#### Example:
```php 
$fields = $webhook->getFields();
```


### getSchema
Returns a schema array for the webhook, which includes the `name` and `url`.

#### Example:
```php 
$schema = $webhook->getSchema();
```

### store($data)
Creates a new webhook record with the provided data. The URL is auto-generated using the site URL and a unique hash.

- Parameters
    - $key `$data`
- Returns `array` of the newly created webhook.

#### Example:
```php 
$newWebhook = Webhook::store($data);
```

### saveChanges($newData)
Updates the webhook's `value` field with new data, excluding certain keys like `id` and `url`, and then saves the changes.

- Parameters
    - $newData `array`
- Returns `void` // No return value

#### Example:
```php 
$webhook->saveChanges($newData);
```
```

---

## FluentBoards Query Builder
Source file : `src/database/query-builder.md`

# FluentBoards Query Builder


## Introduction
Fluent's database query builder provides a convenient, fluent interface to creating and running database queries. It can be used to perform most database operations in your application.

::: tip

Our Query Builder is compatible the PHP Laravel Framework's Query Builder. If you are familiar with Laravel's Query Builder, you will feel right at home using the FluentBoards' Query Builder.
:::
### Example
Here is an example Fluent Query Builder 

```php
$query = fluentBoardsDb()->table('fbs_boards')
            ->orderBy('title', 'ASC')
            ->first();
```


# Retrieving Results

### Retrieving All Rows From A Table
You may use the `table` method on the `fluentBoardsDb` function to begin a query. The `table` method returns a fluent query builder instance for the given table, allowing you to chain more constraints onto the query and then finally get the results using the `get` method:

```php
<?php
 
namespace FluentBoards\App\Http\Controllers;
 
class TaskController extends Controller
{
    /**
     * Show a list of all the tasks
     *
     * @return Response
     */
    public function index()
    {
        $tasks = fluentBoardsDb()->table('fbs_tasks')->get();
 
        return [
            'tasks' => $tasks
        ];   
    }
}
```
The `get` method returns an array containing the results where each result is an instance of the PHP stdClass object. You may access each column's value by accessing the column as a property of the object:

```php
foreach ($tasks as $task) {
    echo $task->title;
    echo $task->status;
}
```

### Retrieving A Single Row / Column From A Table
If you just need to retrieve a single row from the database table, you may use the `first` method. This method will return a single stdClass object:

```php
$task = FluentBoardsDb()->table('fbs_tasks')->where('board_id', 1)->first();
 
echo $task->title;
```

If you don't even need an entire row, you may extract a single value from a record using the `value` method. This method will return the value of the column directly:
```php
$taskTitle = FluentBoardsDb()->table('fbs_tasks')->where('board_id', 1)->value('title');
```

### Retrieving A List Of Column Values
If you would like to retrieve an array containing the values of a single column, you may use the `pluck` method. In this example, we'll retrieve an array of title:

```php
$boards = FluentBoardsDb()->table('fbs_boards')->pluck('title');
 
foreach ($boards as $board) {
    echo $board;
}
```

You may also specify a custom key column for the returned Collection:
```php
$boards = FluentBoardsDb()->table('fbs_boards')->pluck('title', 'id');
 
foreach ($boards as $id => $title) {
    echo $title;
}
```

### Chunking Results
If you need to work with thousands of database records, consider using the `chunk` method. This method retrieves a small chunk of the results at a time and feeds each chunk into a Closure for processing. This method is very useful for process thousands of records. For example, let's work with the entire `fbs_boards` table in chunks of 10 records at a time:
```php
FluentBoardsDb()->table('fbs_boards')->orderBy('id')->chunk(10, function ($boards) {
    foreach ($boards as $board) {
        //
    }
});
```

You may stop further chunks from being processed by returning false from the Closure:
```php
FluentBoardsDb()->table('fbs_boards')->orderBy('id')->chunk(10, function ($boards) {
    // Process the records...
    
    return false;
});
```

### Aggregates
The query builder also provides a variety of aggregate methods such as `count`, `max`, `min`, `avg`, and `sum`. You may call any of these methods after constructing your query:
```php
$tasks = FluentBoardsDb()->table('fbs_tasks')->count();
```


### Determining If Records Exist
Instead of using the `count` method to determine if any records exist that match your query's constraints, you may use the `exists`:
```php
return FluentBoardsDb()->table('fbs_tasks')->where('id', 1)->exists();
```


## Selects

### Specifying A Select Clause
Of course, you may not always want to select all columns from a database table. Using the `select` method, you can specify a custom `select` clause for the query:
```php
$boards = FluentBoardsDb()->table('fbs_boards')->select('id', 'title')->get();
```

The `distinct` method allows you to force the query to return distinct results:
```php
$tasks = FluentBoardsDb()->table('fbs_tasks')->distinct()->get();
```

If you already have a query builder instance and wish to add a column to its existing select clause, you may use the `addSelect` method:
```php
$query = FluentBoardsDb()->table('fbs_tasks')->select('id');
 
$tasks = $query->addSelect('title')->get();
```


## Raw Expressions
Sometimes you may need to use a raw expression in a query. To create a raw expression, you may use the `raw` method:
```php
$tasks = FluentBoardsDb()->table('fbs_tasks')
                     ->select(FluentBoardsDb()->raw('count(*) as comments_count, type'))
                     ->where('type', 'task')
                     ->groupBy('type')
                     ->get();
```

### Raw Methods
Instead of using `FluentBoardsDb()->raw`, you may also use the following methods to insert a raw expression into various parts of your query.

#### `selectRaw`
The `selectRaw` method can be used in place of `select(FluentBoardsDb()->raw(...))`. This method accepts an optional array of bindings as its second argument:
```php
$tasks = FluentBoardsDb()->table('fbs_tasks')
                ->selectRaw('comments_count as total_comments')
                ->get();
```

#### `whereRaw / orWhereRaw`
The `whereRaw` and `orWhereRaw` methods can be used to inject a raw `where` clause into your query. These methods accept an optional array of bindings as their second argument:
```php
$boards = FluentBoardsDb()->table('fbs_boards')
    ->whereRaw('LOWER(title) LIKE ?', ['%' . strtolower($query) . '%'])
    ->orWhereRaw('id LIKE ?', ['%' . $query . '%'])
    ->get();


```

#### `havingRaw / orHavingRaw`
The `havingRaw` and `orHavingRaw` methods may be used to set a raw string as the value of the `having` clause. These methods accept an optional array of bindings as their second argument:
```php
$tasks = FluentBoardsDb()->table('fbs_tasks')
                ->groupBy('type')
                ->havingRaw('SUM(comments_count) > ?', [0])
                ->get();
```

#### `orderByRaw`
The `orderByRaw` method may be used to set a raw string as the value of the `order by` clause:
```php
$tasks = FluentBoardsDb()->table('fbs_tasks')
                ->orderByRaw('updated_at - created_at DESC')
                ->get();
```


## Joins

### Inner Join Clause
The query builder may also be used to write join statements. To perform a basic "inner join", you may use the `join` method on a query builder instance. The first argument passed to the `join` method is the name of the table you need to join to, while the remaining arguments specify the column constraints for the join. Of course, as you can see, you can join to multiple tables in a single query:
```php
$boards = FluentBoardsDb()->table('fbs_boards')
            ->join('users', 'users.id', '=', 'fbs_boards.created_by')
            ->select('fbs_boards.*', 'users.user_email')
            ->get();
```

### left Join Clause
If you would like to perform a "left join" instead of an "inner join", use the `leftJoin` method. The leftJoin method has the same signature as the join method:
```php
$boards = FluentBoardsDb()->table('fbs_boards')
            ->leftJoin('users', 'users.ID', '=', 'fbs_boards.created_by')
            ->get();
```

### Cross Join Clause
To perform a "cross join" use the `crossJoin` method with the name of the table you wish to cross join to. Cross joins generate a cartesian product between the first table and the joined table:
```php
$boards = FluentBoardsDb()->table('fbs_boards')
            ->crossJoin('users')
            ->get();
```

### Advanced Join Clauses
You may also specify more advanced join clauses. To get started, pass a `Closure` as the second argument into the `join` method. The `Closure` will receive a `JoinClause` object which allows you to specify constraints on the `join` clause:
```php
FluentBoardsDb()->table('fbs_boards')
        ->join('users', function ($join) {
            $join->on('fbs_boards.created_by', '=', 'users.ID')->orOn(...);
        })
        ->get();
```

If you would like to use a "where" style clause on your joins, you may use the `where` and `orWhere` methods on a join. Instead of comparing two columns, these methods will compare the column against a value:
```php
FluentBoardsDb()->table('fbs_boards')
        ->join('users', function ($join) {
            $join->on('fbs_boards.created_by', '=', 'users.ID')
                 ->where('users.ID', '>', 5);
        })
        ->get();
```


## Unions

The query builder also provides a quick way to "union" two queries together. For example, you may create an initial query and use the `union` method to union it with a second query:
```php
$first = FluentBoardsDb()->table('fbs_boards')
            ->whereNull('archived_at');
 
$boards = FluentBoardsDb()->table('fbs_boards')
            ->where('type', 'to-do')
            ->union($first)
            ->get();
```


## Where Clauses

### Simple Where Clauses
You may use the `where` method on a query builder instance to add `where` clauses to the query. The most basic call to where requires three arguments. The first argument is the name of the column. The second argument is an operator, which can be any of the database's supported operators. Finally, the third argument is the value to evaluate against the column.
For example, here is a query that verifies the value of the "title" column is equal to 'Fluent Boards':
```php
$boards = FluentBoardsDb()->table('fbs_boards')->where('title', '=', 'Fluent Boards')->get();
```

For convenience, if you want to verify that a column is equal to a given value, you may pass the value directly as the second argument to the where method:
```php
$boards = FluentBoardsDb()->table('fbs_boards')->where('title', 'Fluent Boards')->get();
```

Of course, you may use a variety of other operators when writing a where clause:
```php
$boards = FluentBoardsDb()->table('fbs_boards')
                ->where('type', '=', 'to-do')
                ->get();

 
$boards = FluentBoardsDb()->table('fbs_boards')
                ->where('title', 'like', 'T%')
                ->get();
```

You may also pass an array of conditions to the where function:
```php
$boards = FluentBoardsDb()->table('fbs_boards')->where([
    ['type', '=', 'to-do'],
    ['title', 'like', 'T%'],
])->get();
```

### Or Statements
You may chain where constraints together as well as add or clauses to the query. The `orWhere` method accepts the same arguments as the `where` method:
```php
$boards = FluentBoardsDb()->table('fbs_boards')
                    ->where('title', 'like', 'fluentBoards%')
                    ->orWhere('title', 'fluentBoards')
                    ->get();
```

### Additional Where Clauses
#### whereBetween
The `whereBetween` method verifies that a column's value is between two values:
```php
$tasks = FluentBoardsDb()->table('fbs_tasks')
             ->whereBetween('board_id', [1, 10])->get();
```

#### whereNotBetween
The `whereNotBetween` method verifies that a column's value lies outside two values:
```php
$tasks = FluentBoardsDb()->table('fbs_tasks')
             ->whereNotBetween('board_id', [1, 10])->get();
```

#### whereIn / whereNotIn
The `whereIn` method verifies that a given column's value is contained within the given array:
```php
$boards = FluentBoardsDb()->table('fbs_boards')
                    ->whereIn('id', [1, 2, 3])
                    ->get();
```

The `whereNotIn` method verifies that the given column's value is not contained in the given array:
```php
$boards = FluentBoardsDb()->table('fbs_boards')
                    ->whereNotIn('id', [1, 2, 3])
                    ->get();
```

#### whereNull / whereNotNull
The `whereNull` method verifies that the value of the given column is NULL:
```php
$boards = FluentBoardsDb()->table('fbs_boards')
                    ->whereNull('archived_at')
                    ->get();
```

The `whereNotNull` method verifies that the column's value is not NULL:
```php
$boards = FluentBoardsDb()->table('fbs_boards')
                    ->whereNotNull('updated_at')
                    ->get();
```

#### whereDate / whereMonth / whereDay / whereYear / whereTime
The `whereDate` method may be used to compare a column's value against a date:
```php
$boards = FluentBoardsDb()->table('fbs_boards')
                ->whereDate('created_at', '2016-12-31')
                ->get();
```

The `whereMonth` method may be used to compare a column's value against a specific month of a year:
```php
$boards = FluentBoardsDb()->table('fbs_boards')
                ->whereMonth('created_at', '12')
                ->get();
```

The `whereDay` method may be used to compare a column's value against a specific day of a month:
```php
$boards = FluentBoardsDb()->table('fbs_boards')
                ->whereDay('created_at', '21')
                ->get();
```

The `whereYear` method may be used to compare a column's value against a specific year:
```php
$boards = FluentBoardsDb()->table('fbs_boards')
                ->whereYear('created_at', '2022')
                ->get();
```

The `whereTime` method may be used to compare a column's value against a specific time:
```php
$boards = FluentBoardsDb()->table('fbs_boards')
                ->whereTime('created_at', '11:20:45')
                ->get();
```

The `whereTimestamp` method may be used to compare a column's value against a specific time:
```php
$boards = FluentBoardsDb()->table('fbs_boards')
                ->whereTimestamp('created_at', '2022-11-21 11:20:45')
                ->get();
```

You may also pass a comparison operator to the method:
```php
$boards = FluentBoardsDb()->table('fbs_boards')
                 ->whereColumn('updated_at', '>', 'created_at')
                ->get();
```

The `whereColumn` method can also be passed an array of multiple conditions. These conditions will be joined using the and operator:
```php
$boards = FluentBoardsDb()->table('fbs_boards')
                 ->whereColumn([
                    ['title', '=', 'Fluent Boards'],
                    ['updated_at', '>', 'created_at']
                ])->get();
```


The query above will produce the following SQL:
```sql
select * from fbs_tasks
where exists (
    select 1 from fbs_boards where fbs_boards.id = fbs_tasks.board_id
)
```


### Ordering, Grouping, Limit, & Offset

#### orderBy
The `orderBy` method allows you to sort the result of the query by a given column. The first argument to the `orderBy` method should be the column you wish to sort by, while the second argument controls the direction of the sort and may be either `asc` or `desc`:
```php
$boards = FluentBoardsDb()->table('fbs_boards')
                 ->orderBy('created_at', 'DESC')
                ->get();
```

#### latest / oldest
The `latest` and `oldest` methods allow you to easily order results by date. By default, result will be ordered by the `created_at` column. Or, you may pass the column name that you wish to sort by:
```php
$boards = FluentBoardsDb()->table('fbs_boards')
                 ->latest()
                ->get();
```

#### inRandomOrder
The `inRandomOrder` method may be used to sort the query results randomly. For example, you may use this method to fetch a random user:
```php
$boards = FluentBoardsDb()->table('fbs_boards')
                 ->inRandomOrder()
                ->get();
```

#### groupBy / having
The `groupBy` and `having` methods may be used to group the query results. The `having` method's signature is similar to that of the `where` method:
```php
$boards = FluentBoardsDb()->table('fbs_boards')
                ->groupBy('id')
                ->having('id', '>', 10)
                ->get();
```
You may pass multiple arguments to the `groupBy` method to group by multiple columns:
```php
$boards = FluentBoardsDb()->table('fbs_boards')
                ->groupBy('id', 'type')
                ->having('id', '>', 100)
                ->get();
```

#### skip / take
To limit the number of results returned from the query, or to skip a given number of results in the query, you may use the `skip` and `take` methods:
```php
$boards = FluentBoardsDb()->table('fbs_boards')
                ->skip(10)
                ->take(5)
                ->get();
```
Alternatively, you may use the `limit` and `offset` methods:
```php
$boards = FluentBoardsDb()->table('fbs_boards')
                ->limit(10)
                ->offset(5)
                ->get();
```


### Conditional Clauses
Sometimes you may want clauses to apply to a query only when something else is true. For instance, you may only want to apply a `where` statement if a given input value is present on the incoming request. You may accomplish this using `when` method:
```php
$user = $request->get('user');
 
$boards = FluentBoardsDb()->table('fbs_boards')
                ->when($user, function ($query, $user) {
                    return $query->where('created_by', $user.ID);
                })
                ->get();
```
The `when` method only executes the given `Closure` when the first parameter is `true`. If the first parameter is `false`, the Closure will not be executed.

You may pass another Closure as the third parameter to the `when` method. This Closure will execute if the first parameter evaluates as `false`. To illustrate how this feature may be used, we will use it to configure the default sorting of a query:
```php
$sortBy = null;
 
$boards = FluentBoardsDb()->table('fbs_boards')
                ->when($sortBy, function ($query, $sortBy) {
                    return $query->orderBy($sortBy);
                }, function ($query) {
                    return $query->orderBy('created_at');
                })
                ->get();
```


### Inserts

The query builder also provides an `insert` method for inserting records into the database table. The `insert` method accepts an array of column names and values:
```php
FluentBoardsDb()->table('fbs_boards')->insert(
    ['title' => 'Board 1', 'description' => 'This is board 1', 'type' => 'to-do']
);
```
You may even insert several records into the table with a single call to `insert` by passing an array of arrays. Each array represents a row to be inserted into the table:
```php
FluentBoardsDb()->table('fbs_boards')->insert([
    ['title' => 'Board 1', 'description' => 'This is board 1', 'type' => 'to-do'],
    ['title' => 'Board 2', 'description' => 'This is board 2', 'type' => 'to-do'],
]);
```

#### Auto-Incrementing IDs
If the table has an auto-incrementing id, use the `insertGetId` method to insert a record and then retrieve the ID:
```php
FluentBoardsDb()->table('fbs_boards')->insertGetId(
    ['title' => 'Board 1', 'description' => 'This is board 1']
);
```


### Updates

Of course, in addition to inserting records into the database, the query builder can also update existing records using the `update` method. The `update` method, like the `insert` method, accepts an array of column and value pairs containing the columns to be updated. You may constrain the `update` query using `where` clauses:
```php
FluentBoardsDb()->table('fbs_boards')
            ->where('id', 1)
            ->update(['title' => 'Board no. 1']);
```


### Increment & Decrement

The query builder also provides convenient methods for incrementing or decrementing the value of a given column. This is a shortcut, providing a more expressive and terse interface compared to manually writing the `update` statement.

Both of these methods accept at least one argument: the column to modify. A second argument may optionally be passed to control the amount by which the column should be incremented or decremented:
```php
FluentBoardsDb()->table('fbs_tasks')->increment('comments_count');
 
FluentBoardsDb()->table('fbs_tasks')->increment('comments_count', 5);
 
FluentBoardsDb()->table('fbs_tasks')->decrement('comments_count');
 
FluentBoardsDb()->table('fbs_tasks')->decrement('comments_count', 5);
```
You may also specify additional columns to update during the operation:
```php
FluentBoardsDb()->table('fbs_tasks')->increment('comments_count', 1, ['comments_count' => '5']);
```


### Deletes

The query builder may also be used to delete records from the table via the `delete` method. You may constrain delete statements by adding where clauses before calling the `delete` method:
```php
FluentBoardsDb()->table('fbs_tasks')->delete();
 
FluentBoardsDb()->table('fbs_tasks')->where('comments_count', '>', 5)->delete();
```
If you wish to truncate the entire table, which will remove all rows and reset the auto-incrementing ID to zero, you may use the `truncate` method:
```php
FluentBoardsDb()->table('fbs_tasks')->truncate();
```

---
