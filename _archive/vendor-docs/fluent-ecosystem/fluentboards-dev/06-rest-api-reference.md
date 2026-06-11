# Section REST API Reference Guide

Source : dev.fluentboards.com
Date compile : 2026-05-24


---

## Activities API
Source file : `src/rest-api/activities.md`

# Activities API

> **Note:** This documentation is under development. The Activities API allows you to retrieve activity logs and audit trails.

## Overview

The Activities API provides endpoints for retrieving activity logs, audit trails, and user activity history in Fluent Boards.

## Base Endpoint

```
/fluent-boards/v2/activities
```

## Available Endpoints

### List Activities
- **GET** `/activities`
- **GET** `/boards/{board_id}/activities`
- **GET** `/boards/{board_id}/tasks/{task_id}/activities`

### Get Activity
- **GET** `/activities/{activity_id}`

### Get User Activities
- **GET** `/users/{user_id}/activities`

### Get Activity Summary
- **GET** `/activities/summary`

### Export Activities
- **POST** `/activities/export`

## Activity Object

```json
{
  "id": 123,
  "user_id": 789,
  "action": "task_created",
  "resource_type": "task",
  "resource_id": 456,
  "description": "Created task 'Design Homepage'",
  "metadata": {
    "task_title": "Design Homepage",
    "project_id": 123,
    "priority": "high"
  },
  "ip_address": "192.168.1.1",
  "user_agent": "Mozilla/5.0...",
  "created_at": "2024-01-15T10:30:00Z"
}
```

## Activity Types

### Project Activities
- `project_created` - Project creation
- `project_updated` - Project updates
- `project_archived` - Project archival
- `project_restored` - Project restoration
- `project_deleted` - Project deletion

### Task Activities
- `task_created` - Task creation
- `task_updated` - Task updates
- `task_moved` - Task movement
- `task_assigned` - Task assignment
- `task_completed` - Task completion
- `task_deleted` - Task deletion

### User Activities
- `user_joined` - User joined project
- `user_left` - User left project
- `role_changed` - User role changes
- `permission_updated` - Permission updates

## Features

- Comprehensive audit trail
- Real-time activity feed
- Activity filtering
- Export capabilities
- Activity analytics
- Privacy controls

---

*This documentation will be expanded with detailed examples and complete API reference.*

---

## Admin API
Source file : `src/rest-api/admin.md`

# Admin API

> **Note:** This documentation is under development. The Admin API provides endpoints for platform administration and management.

## Overview

The Admin API provides endpoints for managing Fluent Boards platform configuration, system settings, and administrative functions.

## Base Endpoint

```
/fluent-boards/v2/admin
```

## Available Endpoints

### System Information
- **GET** `/admin/system-info`

### Platform Statistics
- **GET** `/admin/statistics`

### User Management
- **GET** `/admin/users`
- **POST** `/admin/users`
- **PUT** `/admin/users/{user_id}`
- **DELETE** `/admin/users/{user_id}`

### Project Management
- **GET** `/admin/projects`
- **POST** `/admin/projects`
- **PUT** `/admin/projects/{project_id}`
- **DELETE** `/admin/projects/{project_id}`

### System Maintenance
- **POST** `/admin/maintenance/clear-cache`
- **POST** `/admin/maintenance/optimize-database`
- **POST** `/admin/maintenance/backup`

### License Management
- **GET** `/admin/license`
- **POST** `/admin/license/activate`
- **POST** `/admin/license/deactivate`

## System Info Object

```json
{
  "version": "2.0.0",
  "php_version": "8.1.0",
  "wordpress_version": "6.4.0",
  "database_version": "1.0.0",
  "total_projects": 25,
  "total_users": 150,
  "total_tasks": 1250,
  "storage_used": "2.5GB",
  "last_backup": "2024-01-15T10:30:00Z"
}
```

## Statistics Object

```json
{
  "projects": {
    "total": 25,
    "active": 20,
    "archived": 5
  },
  "tasks": {
    "total": 1250,
    "completed": 800,
    "pending": 300,
    "in_progress": 150
  },
  "users": {
    "total": 150,
    "active": 120,
    "inactive": 30
  },
  "storage": {
    "used": "2.5GB",
    "available": "47.5GB",
    "attachments": "1.2GB"
  }
}
```

## Features

- System monitoring
- User administration
- Project management
- Maintenance tools
- License management
- Performance analytics

---

*This documentation will be expanded with detailed examples and complete API reference.*

---

## Attachments
Source file : `src/rest-api/attachments.md`

# Attachments

Manage task file attachments and generated links.

## Attachment Object

Based on the model, an attachment has the following properties:

| Property | Type | Description |
|----------|------|-------------|
| `id` | integer | Unique identifier for the attachment |
| `file_hash` | string | Unique hash used for secure link generation |
| `object_type` | string | Where it’s attached (e.g., `TASK_ATTACHMENT`, `TASK_DESCRIPTION`, `COMMENT_IMAGE`) |
| `object_id` | integer | Related object ID (e.g., task ID) |
| `attachment_type` | string | MIME type (e.g., `image/png`, `text/csv`) or `url` for external links |
| `file_path` | string | Absolute path on disk (may be hidden) |
| `full_url` | string | Public URL when `attachment_type` is `url`; otherwise file URL |
| `file_size` | string | File size text (e.g., `512 KB`) |
| `settings` | object | Additional metadata (serialized in DB) |
| `secure_url` | string | Time-based secure link for downloading (computed) |
| `title` | string | Original file name or provided title |
| `driver` | string | Storage driver (e.g., `local`) |
| `status` | string | Attachment status (e.g., `ACTIVE`) |
| `created_at` | string | Creation timestamp (ISO 8601) |
| `updated_at` | string | Last update timestamp (ISO 8601) |

Notes
- `secure_url` is generated from `file_hash` and is safe to share for direct downloads.
- The query includes `fbs=1`, `fbs_attachment`, and a time-based `secure_sign`.

## List Task Attachments

Return attachments for a task.

**HTTP Request**
```
GET /wp-json/fluent-boards/v2/projects/{board_id}/tasks/{task_id}/attachment
```

### Example Request

```bash
curl "https://yourdomain.com/wp-json/fluent-boards/v2/projects/{board_id}/tasks/{task_id}/attachment" \
  -H "Authorization: Basic API_USERNAME:API_PASSWORD"
```

### Example Response

```json
{
  "attachments": [
    {
      "id": 101,
      "object_id": "123",
      "object_type": "TASK",
      "attachment_type": "text/csv",
      "file_path": "/var/www/yourdomain.com/wp-content/uploads/fluent-boards/board_1/1711111111-report.csv",
      "full_url": "https://yourdomain.com/wp-content/uploads/fluent-boards/board_1/1711111111-report.csv",
      "settings": "",
      "title": "report.csv",
      "file_hash": "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
      "driver": "local",
      "status": "ACTIVE",
      "file_size": "2 KB",
      "created_at": "2025-07-16T08:01:33+00:00",
      "updated_at": "2025-07-16T08:01:33+00:00",
      "secure_url": "https://yourdomain.com/index.php?fbs=1&fbs_attachment=aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa&secure_sign=bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb"
    },
    {
      "id": 102,
      "object_id": "123",
      "object_type": "TASK",
      "attachment_type": "image/png",
      "file_path": "/var/www/yourdomain.com/wp-content/uploads/fluent-boards/board_1/1712222222-design.png",
      "full_url": "https://yourdomain.com/wp-content/uploads/fluent-boards/board_1/1712222222-design.png",
      "settings": "",
      "title": "design.png",
      "file_hash": "cccccccccccccccccccccccccccccccc",
      "driver": "local",
      "status": "ACTIVE",
      "file_size": "420 KB",
      "created_at": "2025-08-08T06:19:03+00:00",
      "updated_at": "2025-08-08T06:19:03+00:00",
      "secure_url": "https://yourdomain.com/index.php?fbs=1&fbs_attachment=cccccccccccccccccccccccccccccccc&secure_sign=dddddddddddddddddddddddddddddddd"
    },
  ]
}
```

## Add Task Attachment (Upload)

Upload one or more files and attach them to a task.

**HTTP Request**
```
POST /wp-json/fluent-boards/v2/projects/{board_id}/tasks/{task_id}/add-task-attachment-file
```

### Example Request

```bash
curl "https://yourdomain.com/wp-json/fluent-boards/v2/projects/{board_id}/tasks/{task_id}/add-task-attachment-file" \
  -X POST \
  -H "Authorization: Basic API_USERNAME:API_PASSWORD" \
  -F "file[]=@/path/to/unnamed-3.png" \
  -F "file[]=@/path/to/unnamed-4.png" \
  -F "file[]=@/path/to/Untitled-drawing.png"
```

Form data
- file[] (binary): Repeat to upload multiple files

### Example Response

```json
{
  "message": "Task attachment has been added",
  "attachments": [
    {
      "object_id": 123,
      "object_type": "TASK",
      "attachment_type": "image/png",
      "title": "unnamed-3.png",
      "file_path": "/var/www/yourdomain.com/wp-content/uploads/fluent-boards/board_1/1714444444-unnamed-3.png",
      "full_url": "https://yourdomain.com/wp-content/uploads/fluent-boards/board_1/1714444444-unnamed-3.png",
      "file_size": "484 KB",
      "settings": "",
      "driver": "local",
      "file_hash": "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
      "updated_at": "2025-08-08T06:26:34+00:00",
      "created_at": "2025-08-08T06:26:34+00:00",
      "id": 201,
      "secure_url": "https://yourdomain.com/index.php?fbs=1&fbs_attachment=aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa&secure_sign=bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb"
    },
    {
      "object_id": 123,
      "object_type": "TASK",
      "attachment_type": "image/png",
      "title": "unnamed-4.png",
      "file_path": "/var/www/yourdomain.com/wp-content/uploads/fluent-boards/board_1/1714444444-unnamed-4.png",
      "full_url": "https://yourdomain.com/wp-content/uploads/fluent-boards/board_1/1714444444-unnamed-4.png",
      "file_size": "420 KB",
      "settings": "",
      "driver": "local",
      "file_hash": "cccccccccccccccccccccccccccccccc",
      "updated_at": "2025-08-08T06:26:34+00:00",
      "created_at": "2025-08-08T06:26:34+00:00",
      "id": 202,
      "secure_url": "https://yourdomain.com/index.php?fbs=1&fbs_attachment=cccccccccccccccccccccccccccccccc&secure_sign=dddddddddddddddddddddddddddddddd"
    },
    {
      "object_id": 123,
      "object_type": "TASK",
      "attachment_type": "image/png",
      "title": "Untitled-drawing.png",
      "file_path": "/var/www/yourdomain.com/wp-content/uploads/fluent-boards/board_1/1714444444-Untitled-drawing.png",
      "full_url": "https://yourdomain.com/wp-content/uploads/fluent-boards/board_1/1714444444-Untitled-drawing.png",
      "file_size": "582 KB",
      "settings": "",
      "driver": "local",
      "file_hash": "eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee",
      "updated_at": "2025-08-08T06:26:34+00:00",
      "created_at": "2025-08-08T06:26:34+00:00",
      "id": 203,
      "secure_url": "https://yourdomain.com/index.php?fbs=1&fbs_attachment=eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee&secure_sign=ffffffffffffffffffffffffffffffff"
    }
  ]
}
```

## Add Task Attachment (URL)

Attach an external URL to a task (no file upload).

**HTTP Request**
```
POST /wp-json/fluent-boards/v2/tasks/{task_id}/add-attachment
```

### Example Request

```bash
curl "https://yourdomain.com/wp-json/fluent-boards/v2/tasks/{task_id}/add-attachment" \
  -X POST \
  -H "Authorization: Basic API_USERNAME:API_PASSWORD" \
  -H "Content-Type: application/json" \
  -d '{
    "title": "Lorem ipsum",
    "url": "https://yourdomain.com/rest-api/attachments/#list-task-attachments"
  }'
```

### Example Response

```json
{
  "message": "Attachment has been added to task",
  "attachment": {
    "object_id": 123,
    "object_type": "TASK",
    "attachment_type": "url",
    "title": "Lorem ipsum",
    "file_path": null,
    "full_url": "https://yourdomain.com/rest-api/attachments/#list-task-attachments",
    "file_size": null,
    "settings": {
      "meta": {
        "errors": {
          "no_response": [
            "URL not found. Response returned a non-200 status code for this URL."
          ]
        },
        "error_data": {
          "no_response": {
            "status": 404
          }
        }
      }
    },
    "driver": "local",
    "file_hash": "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
    "updated_at": "2025-08-08T06:30:34+00:00",
    "created_at": "2025-08-08T06:30:34+00:00",
    "id": 301,
    "secure_url": "https://yourdomain.com/rest-api/attachments/#list-task-attachments"
  }
}
```

## Update Attachment

Update an attachment's title.

**HTTP Request**
```
PUT /wp-json/fluent-boards/v2/tasks/{task_id}/attachment-update/{attachment_id}
```

### Example Request

```bash
curl "https://yourdomain.com/wp-json/fluent-boards/v2/tasks/{task_id}/attachment-update/{attachment_id}" \
  -X PUT \
  -H "Authorization: Basic API_USERNAME:API_PASSWORD" \
  -H "Content-Type: application/json" \
  -d '{
    "title": "Board Documentation"
  }'
```

### Example Response

```json
{
  "message": "Task attachment has been updated",
  "attachment": {
    "id": 301,
    "object_id": "123",
    "object_type": "TASK",
    "attachment_type": "url",
    "file_path": null,
    "full_url": "https://yourdomain.com/rest-api/attachments/#list-task-attachments",
    "settings": {
      "meta": {
        "errors": {
          "no_response": [
            "URL not found. Response returned a non-200 status code for this URL."
          ]
        },
        "error_data": {
          "no_response": {
            "status": 404
          }
        }
      }
    },
    "title": "Board Documentation",
    "file_hash": "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
    "driver": "local",
    "status": "ACTIVE",
    "file_size": null,
    "created_at": "2025-08-08T06:30:34+00:00",
    "updated_at": "2025-08-08T06:34:04+00:00",
    "secure_url": "https://yourdomain.com/rest-api/attachments/#list-task-attachments"
  }
}
```

## Delete Attachment

Remove an attachment from a task.

**HTTP Request**
```
DELETE /wp-json/fluent-boards/v2/tasks/{task_id}/attachment-delete/{attachment_id}
```

### Example Request

```bash
curl "https://yourdomain.com/wp-json/fluent-boards/v2/tasks/{task_id}/attachment-delete/{attachment_id}" \
  -X DELETE \
  -H "Authorization: Basic API_USERNAME:API_PASSWORD"
```

### Example Response

```json
{
  "message": "Task attachment has been deleted",
  "attachments": [
    {
      "id": 401,
      "object_id": "123",
      "object_type": "TASK",
      "attachment_type": "text/csv",
      "file_path": "/var/www/yourdomain.com/wp-content/uploads/fluent-boards/board_1/1711111111-report.csv",
      "full_url": "https://yourdomain.com/wp-content/uploads/fluent-boards/board_1/1711111111-report.csv",
      "settings": "",
      "title": "report.csv",
      "file_hash": "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
      "driver": "local",
      "status": "ACTIVE",
      "file_size": "2 KB",
      "created_at": "2025-07-16T08:01:33+00:00",
      "updated_at": "2025-07-16T08:01:33+00:00",
      "secure_url": "https://yourdomain.com/index.php?fbs=1&fbs_attachment=aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa&secure_sign=bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb"
    },
    {
      "id": 402,
      "object_id": "123",
      "object_type": "TASK",
      "attachment_type": "image/png",
      "file_path": "/var/www/yourdomain.com/wp-content/uploads/fluent-boards/board_1/1712222222-design.png",
      "full_url": "https://yourdomain.com/wp-content/uploads/fluent-boards/board_1/1712222222-design.png",
      "settings": "",
      "title": "design.png",
      "file_hash": "cccccccccccccccccccccccccccccccc",
      "driver": "local",
      "status": "ACTIVE",
      "file_size": "420 KB",
      "created_at": "2025-08-08T06:19:03+00:00",
      "updated_at": "2025-08-08T06:19:03+00:00",
      "secure_url": "https://yourdomain.com/index.php?fbs=1&fbs_attachment=cccccccccccccccccccccccccccccccc&secure_sign=dddddddddddddddddddddddddddddddd"
    }
  ]
}
```

---

## Authentication
Source file : `src/rest-api/authentication.md`

# Authentication

FluentBoards uses WordPress Application Passwords for REST API authentication. This is the standard WordPress authentication method that provides secure, non-interactive access to the REST API.

## Creating Application Passwords

### Step 1: Access User Profile

1. Log in to your WordPress admin dashboard
2. Navigate to `Users → Profile` (or `Users → All Users` and click on your user)
3. Scroll down to the "Application Passwords" section

### Step 2: Create New Application Password

1. In the "Application Passwords" section, enter a name for your application (e.g., "Fluent Boards API")
2. Click "Add New Application Password"

![WordPress Application Passwords](/assets/img/wordpress-app-passwords.png)

### Step 3: Save Your Credentials

After creating the application password, WordPress will display:
- **Username**: Your WordPress username
- **Application Password**: A generated password (e.g., "oqYd hptb PnKC XHur CJbG 01UW")

![Generated Application Password](/assets/img/wordpress-generated-password.png)

::: warning Important
Save these credentials immediately! The application password cannot be retrieved later and will only be shown once.
:::

::: tip Note
Application passwords are different from your regular WordPress password and are specifically designed for API access. They can be easily revoked if needed.
:::

## Authentication Methods

### Basic Authentication (Recommended)

Use HTTP Basic Authentication with your API credentials:

```bash
curl "https://yourdomain.com/wp-json/fluent-boards/v2/projects" \
  -H "Authorization: Basic $(echo -n 'API_USERNAME:API_PASSWORD' | base64)"
```

### Cookie Authentication (Not Recommended for API)

For testing only, you can use cookie authentication, but this is not recommended for API access:

```bash
curl "https://yourdomain.com/wp-json/fluent-boards/v2/projects" \
  -H "Cookie: wordpress_logged_in_xxx=your_cookie_value"
```

::: warning Security Notice
Never use cookie authentication for API access in production. Always use Application Passwords with proper Authorization headers.
:::

## Example API Call

Here's a complete example of making an authenticated API request:

```bash
curl "https://yourdomain.com/wp-json/fluent-boards/v2/projects" \
  -H "Authorization: Basic API_USERNAME:API_PASSWORD" \
  -H "Content-Type: application/json"
```

### Response

```json
{
  "data": [
    {
      "id": 1,
      "title": "Project Alpha",
      "description": "Main project board",
      "status": "active",
      "created_at": "2024-01-15T10:30:00Z",
      "updated_at": "2024-01-15T10:30:00Z"
    }
  ],
  "message": "Success",
  "total": 1,
  "current_page": 1,
  "per_page": 15
}
```

## Programming Language Examples

### PHP

```php
<?php
$username = 'your_api_username';
$password = 'your_api_password';
$url = 'https://yourdomain.com/wp-json/fluent-boards/v2/projects';

$ch = curl_init();
curl_setopt($ch, CURLOPT_URL, $url);
curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
curl_setopt($ch, CURLOPT_USERPWD, "$username:$password");
curl_setopt($ch, CURLOPT_HTTPHEADER, [
    'Content-Type: application/json'
]);

$response = curl_exec($ch);
curl_close($ch);

$data = json_decode($response, true);
?>
```

### JavaScript (Node.js)

```javascript
const axios = require('axios');

const apiCredentials = Buffer.from('API_USERNAME:API_PASSWORD').toString('base64');

const config = {
  headers: {
    'Authorization': `Basic ${apiCredentials}`,
    'Content-Type': 'application/json'
  }
};

axios.get('https://yourdomain.com/wp-json/fluent-boards/v2/projects', config)
  .then(response => {
    console.log(response.data);
  })
  .catch(error => {
    console.error('Error:', error.response.data);
  });
```

### Python

```python
import requests
from requests.auth import HTTPBasicAuth

username = 'your_api_username'
password = 'your_api_password'
url = 'https://yourdomain.com/wp-json/fluent-boards/v2/projects'

response = requests.get(
    url,
    auth=HTTPBasicAuth(username, password),
    headers={'Content-Type': 'application/json'}
)

if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print(f"Error: {response.status_code}")
    print(response.text)
```

### Ruby

```ruby
require 'net/http'
require 'uri'
require 'base64'

username = 'your_api_username'
password = 'your_api_password'
url = URI('https://yourdomain.com/wp-json/fluent-boards/v2/projects')

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Get.new(url)
request['Authorization'] = "Basic #{Base64.strict_encode64("#{username}:#{password}")}"
request['Content-Type'] = 'application/json'

response = http.request(request)
puts response.body
```

## Testing Your Authentication

To verify your credentials are working, make a simple API call:

```bash
curl "https://yourdomain.com/wp-json/fluent-boards/v2/projects" \
  -H "Authorization: Basic API_USERNAME:API_PASSWORD"
```

If successful, you'll receive a JSON response with your projects data.

## Troubleshooting

### Common Issues

**401 Unauthorized Error**
- Verify your username and application password are correct
- Ensure the application password hasn't been revoked
- Check that the user account has proper permissions
- Verify that FluentBoards is properly installed and activated

**403 Forbidden Error**  
- The user account may lack necessary permissions
- Verify the account has appropriate WordPress capabilities
- Check if the user has access to FluentBoards features

**404 Not Found Error**
- Verify the API endpoint URL is correct
- Ensure FluentBoards is installed and the REST API is enabled
- Check your WordPress permalink structure

### Permission Requirements

Your API user account needs these minimum permissions:
- **WordPress Administrator role**: Full access to all endpoints
- **Appropriate capabilities**: Required for the specific operations you're performing
- **FluentBoards access**: User must have access to FluentBoards features

## Security Best Practices

1. **Use HTTPS**: Always make API calls over secure connections
2. **Rotate Credentials**: Regularly update your API credentials
3. **Limit Permissions**: Grant only the minimum required permissions
4. **Monitor Usage**: Track API usage for unusual activity
5. **Secure Storage**: Never commit credentials to version control
6. **Dedicated Accounts**: Use dedicated user accounts for API access, not your main admin account

## Managing Application Passwords

### View Existing Application Passwords

In your WordPress user profile, you can see all existing application passwords:
- Application name and creation date
- Last used date (if available)
- Management options

### Revoke Application Passwords

To revoke an application password:
1. Go to `Users → Profile` in WordPress admin
2. Scroll to the "Application Passwords" section
3. Click "Revoke" next to the application password you want to remove
4. Confirm the revocation

::: warning Important
Revoking an application password is permanent and cannot be undone. Any applications using that password will lose access immediately.
:::

### Best Practices for Application Passwords

1. **Use descriptive names**: Name your application passwords clearly (e.g., "Mobile App", "Third-party Integration")
2. **Regular rotation**: Periodically revoke and recreate application passwords
3. **One per application**: Create separate application passwords for different applications
4. **Monitor usage**: Check the "Last Used" information to identify unused passwords

## Next Steps

Now that you have authentication set up, you can:
- [Manage Boards](/rest-api/boards)
- [Handle Tasks](/rest-api/tasks)
- [Work with Stages](/rest-api/stages)
- [Access Users & Members](/rest-api/users)
- [Manage Labels](/rest-api/labels)
- [Set up Webhooks](/rest-api/webhooks)

---

## Boards
Source file : `src/rest-api/boards.md`

# Boards

The Boards API allows you to manage boards in Fluent Boards. You can create, read, update, and delete boards, as well as manage their members, stages, and settings.
## List All Boards

Retrieve a paginated list of boards.

**HTTP Request**
```
GET /wp-json/fluent-boards/v2/projects
```

### Example Request

```bash
curl "https://yourdomain.com/wp-json/fluent-boards/v2/projects?per_page=10&page=1" \
  -H "Authorization: Basic API_USERNAME:API_PASSWORD"
```

### Parameters

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `per_page` | integer | 10 | Number of boards per page |
| `page` | integer | 1 | Page number for pagination |
| `search` | string | - | Search boards by title |
| `type` | string | - | Filter by board type (to-do, roadmap) |
| `order_by` | string | id | Sort field (id, title, created_at) |
| `order_type` | string | DESC | Sort direction (ASC, DESC) |


### Example Response

```json
{
  "boards": {
  "current_page": 1,
  "data": [
    {
      "id": 1,
        "title": "Sample Board",
      "type": "to-do",
      "background": {
          "color": "#2196F3",
          "id": "solid_1"
        },
        "settings": {
          "tasks_count": 15
        },
        "completed_tasks_count": "5",
        "users": [
          {
            "ID": 1,
            "user_login": "admin",
            "display_name": "Admin User",
            "role": "Admin",
            "photo": "https://secure.gravatar.com/avatar/example?s=128&d=mm&r=g"
          }
        ],
        "stages": [
          {
            "id": 1,
            "title": "To Do",
            "position": "1.00"
          }
        ]
      }
    ],
    "per_page": 20,
    "total": 1
  },
  "folder_mapping": []
}
```


## Get a Single Board

Retrieve a specific board by ID.

**HTTP Request**
```
GET /wp-json/fluent-boards/v2/projects/{board_id}
```

### Example Request

```bash
curl "https://yourdomain.com/wp-json/fluent-boards/v2/projects/{board_id}" \
  -H "Authorization: Basic API_USERNAME:API_PASSWORD"
```


### Example Response

```json
{
  "board": {
    "id": 1,
    "title": "Sample Board",
    "type": "to-do",
    "background": {
      "color": "#2196F3",
      "id": "solid_1"
    },
    "settings": {
      "tasks_count": 15
    },
    "labelColor": {
      "green": "#4bce97",
      "blue": "#579dff",
      "red": "#f87168"
    },
    "labelColorText": {
      "green": "#1B2533",
      "blue": "#1B2533",
      "red": "#1B2533"
    },
    "users": [
      {
        "ID": 1,
        "user_login": "admin",
        "display_name": "Admin User",
        "role": "Admin"
      }
    ],
    "owner": {
      "ID": 1,
      "display_name": "Admin User"
    },
    "stages": [
      {
        "id": 1,
        "title": "To Do",
        "position": "1.00"
      },
      {
        "id": 2,
        "title": "In Progress",
        "position": "2.00"
      }
    ],
    "labels": [
      {
        "id": 1,
        "title": "bug",
        "bg_color": "#E6B0AA"
      },
      {
        "id": 2,
        "title": "feature",
        "bg_color": "#AED6F1"
      }
    ],
    "custom_fields": []
  }
}
```

## Create a Board

Create a new board.

**HTTP Request**
```
POST /wp-json/fluent-boards/v2/projects
```

### Request Body

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `board[title]` | string | Yes | Board title |
| `board[description]` | string | No | Board description |
| `board[type]` | string | Yes | Board type (to-do, roadmap) |
| `board[currency]` | string | No | Currency for the board |
| `folder_id` | integer | No | Folder ID to add board to (Pro feature) |
| `stages` | array | No | Custom stages for roadmap boards |

### Example Request

```bash
curl "https://yourdomain.com/wp-json/fluent-boards/v2/projects" \
  -X POST \
  -H "Authorization: Basic API_USERNAME:API_PASSWORD" \
  -H "Content-Type: application/json" \
  -d '{
    "board": {
      "title": "New Project Board",
      "description": "A new project board for development tasks",
      "type": "to-do"
    }
  }'
```

### Example Response

```json
{
  "message": "Board has been created successfully",
  "board": {
    "title": "New Project Board",
    "type": "to-do",
    "description": "A new project board for development tasks",
    "currency": "USD",
    "background": {
      "id": "solid_4",
      "is_image": false,
      "image_url": null,
      "color": "#5f27cd"
    },
    "created_by": 1,
    "id": 9,
    "meta": [],
    "isUserOnlyViewer": false
  }
}
```

## Update a Board

Update an existing board.

**HTTP Request**
```
PUT /wp-json/fluent-boards/v2/projects/{board_id}
```

### Example Request

```bash
curl "https://yourdomain.com/wp-json/fluent-boards/v2/projects/{board_id}" \
  -X PUT \
  -H "Authorization: Basic API_USERNAME:API_PASSWORD" \
  -H "Content-Type: application/json" \
  -d '{
    "title": "Updated Board Title",
    "description": "Updated board description"
  }'
```

### Request Body

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `title` | string | Yes | Board title |
| `description` | string | No | Board description |

### Example Request

```json
{
    "title": "Updated Board Title",
  "description": "Updated board description"
}
```

### Example Response

```json
{
  "message": "Board has been updated",
  "board": {
    "id": 9,
    "title": "Updated Board Title",
    "description": "Updated board description",
    "type": "to-do",
    "background": {
      "color": "#5f27cd"
    }
    // ... other board properties
  },
  "stages": [
    {
      "id": 96,
      "title": "Open",
      "position": "1.00"
      // ... other stage properties
    },
    {
      "id": 97,
      "title": "In Progress",
      "position": "2.00"
      // ... other stage properties
    },
    {
      "id": 98,
      "title": "Completed",
      "position": "3.00"
      // ... other stage properties
    }
  ]
}
```

## Delete a Board

Delete a board.

**HTTP Request**
```
DELETE /wp-json/fluent-boards/v2/projects/{board_id}
```

### Example Request

```bash
curl "https://yourdomain.com/wp-json/fluent-boards/v2/projects/{board_id}" \
  -X DELETE \
  -H "Authorization: Basic API_USERNAME:API_PASSWORD"
```


### Example Response

```json
{
  "message": "Board deleted successfully"
}
```

## Archive a Board

Archive a board .

**HTTP Request**
```
PUT /wp-json/fluent-boards/v2/projects/{board_id}/archive-board
```

### Example Request

```bash
curl "https://yourdomain.com/wp-json/fluent-boards/v2/projects/{board_id}/archive-board" \
  -X PUT \
  -H "Authorization: Basic API_USERNAME:API_PASSWORD"
```


### Example Response

```json
{
  "board": {
    "id": 9,
    "title": "Updated Board Title",
    "description": "Updated board description",
    "type": "to-do",
    "background": {
      "color": "#5f27cd"
    },
    "archived_at": "2025-08-06 06:40:05"
    // ... other board properties
  },
  "message": "Board has been archived successfully!"
}
```

## Restore a Board

Restore an archived board.

**HTTP Request**
```
PUT /wp-json/fluent-boards/v2/projects/{board_id}/restore-board
```

### Example Request

```bash
curl "https://yourdomain.com/wp-json/fluent-boards/v2/projects/{board_id}/restore-board" \
  -X PUT \
  -H "Authorization: Basic API_USERNAME:API_PASSWORD"
```


### Example Response

```json
{
  "board": {
    "id": 9,
    "title": "Updated Board Title",
    "description": "Updated board description",
    "type": "to-do",
    "background": {
      "color": "#5f27cd"
    },
    "archived_at": null
    // ... other board properties
  },
  "message": "Board has been restored successfully!"
}
```

## Duplicate a Board

Create a copy of an existing board.

**HTTP Request**
```
POST /wp-json/fluent-boards/v2/projects/{board_id}/duplicate-board
```

### Example Request

```bash
curl "https://yourdomain.com/wp-json/fluent-boards/v2/projects/{board_id}/duplicate-board" \
  -X POST \
  -H "Authorization: Basic API_USERNAME:API_PASSWORD" \
  -H "Content-Type: application/json" \
  -d '{
    "board": {"title": "Board Alpha - Copy"},
    "isWithTasks": "yes",
    "isWithLabels": "yes",
    "isWithTemplates": "no"
  }'
```

### Request Body

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `board[title]` | string | Yes | Title for the duplicated board |
| `isWithTasks` | string | No | Whether to include tasks ("yes" or "no") |
| `isWithLabels` | string | No | Whether to include labels ("yes" or "no") |
| `isWithTemplates` | string | No | Whether to include templates ("yes" or "no") |

### Example Request

```json
{
  "board": {
    "title": "Board Alpha - Copy"
  },
  "isWithTasks": "yes",
  "isWithLabels": "yes",
  "isWithTemplates": "no"
}
```

### Example Response

```json
{
  "board": {
    "id": 10,
    "title": "Board Alpha - Copy",
    "type": "to-do",
    "background": {
      "color": "#5f27cd"
    },
    "created_by": 1
    // ... other board properties
  }
}
```

## Get Board Members

Retrieve all members of a board.

**HTTP Request**
```
GET /wp-json/fluent-boards/v2/projects/{board_id}/users
```

### Example Request

```bash
curl "https://yourdomain.com/wp-json/fluent-boards/v2/projects/{board_id}/users" \
  -H "Authorization: Basic API_USERNAME:API_PASSWORD"
```


### Example Response

```json
{
  "users": [
    {
      "ID": 1,
      "display_name": "John Doe",
      "user_login": "john_doe",
      "email": "john@example.com",
      "photo": "https://secure.gravatar.com/avatar/...",
      "role": "member",
      "is_super": false,
      "is_wpadmin": true
    },
    {
      "ID": 2,
      "display_name": "Jane Smith",
      "user_login": "jane_smith",
      "email": "jane@example.com",
      "photo": "https://secure.gravatar.com/avatar/...",
      "role": "member",
      "is_super": false,
      "is_wpadmin": false
    }
  ],
  "global_admins": []
}
```

## Get Board Activities

Retrieve recent activities for a board.

**HTTP Request**
```
GET /wp-json/fluent-boards/v2/projects/{board_id}/activities
```

### Parameters

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `per_page` | integer | 20 | Number of activities per page |
| `page` | integer | 1 | Page number for pagination |

### Example Request

```bash
curl "https://yourdomain.com/wp-json/fluent-boards/v2/projects/{board_id}/activities?per_page=40&page=1" \
  -H "Authorization: Basic API_USERNAME:API_PASSWORD"
```


### Example Response

```json
{
  "activities": {
  "current_page": 1,
  "data": [
    {
        "id": 538,
        "object_id": "3",
        "object_type": "board_activity",
        "action": "deleted",
        "column": "task",
        "old_value": "Updated Task Title",
        "new_value": null,
        "description": null,
        "created_by": "1",
        "settings": null,
        "created_at": "2025-08-04T09:23:52+00:00",
        "user": {
          "ID": 1,
          "display_name": "John Doe",
          "user_login": "john_doe",
          "email": "john@example.com",
          "photo": "https://secure.gravatar.com/avatar/..."
        }
      },
      {
        "id": 533,
        "object_id": "3",
        "object_type": "board_activity",
        "action": "created",
        "column": "task",
        "old_value": null,
        "new_value": "New Task Title",
        "description": "on stage Feature Requests",
        "created_by": "1",
        "settings": {
          "task_id": 279
        },
        "created_at": "2025-08-04T09:00:39+00:00",
        "user": {
          "ID": 1,
          "display_name": "John Doe",
          "user_login": "john_doe",
          "email": "john@example.com",
          "photo": "https://secure.gravatar.com/avatar/..."
        }
      }
    ],
    "per_page": 40,
    "total": 94
    // ... other pagination properties
  }
}
```

## Error Responses

See [Common Error Responses](/rest-api/shared/error-responses) for standard error formats.

### Common Board-Specific Errors

- **404 Not Found** - Board not found
- **403 Forbidden** - You don't have permission to access this board
- **400 Bad Request** - Invalid board data or missing required fields

---

## Cloud Storage API
Source file : `src/rest-api/cloud-storage.md`

# Cloud Storage API

> **Note:** This is a Pro feature. The Cloud Storage API allows you to integrate with cloud storage providers.

## Overview

The Cloud Storage API provides endpoints for integrating with cloud storage providers like Google Drive, Dropbox, and OneDrive in Fluent Boards Pro.

## Base Endpoint

```
/fluent-boards/v2/cloud-storage
```

## Available Endpoints

### List Connected Services
- **GET** `/cloud-storage/services`

### Connect Service
- **POST** `/cloud-storage/connect`

### Disconnect Service
- **DELETE** `/cloud-storage/disconnect/{service_id}`

### List Files
- **GET** `/cloud-storage/{service_id}/files`

### Upload File
- **POST** `/cloud-storage/{service_id}/upload`

### Download File
- **GET** `/cloud-storage/{service_id}/download/{file_id}`

### Share File
- **POST** `/cloud-storage/{service_id}/share/{file_id}`

## Supported Services

- Google Drive
- Dropbox
- OneDrive
- Box
- Amazon S3

## Service Object

```json
{
  "id": 123,
  "service_type": "google_drive",
  "name": "My Google Drive",
  "account_email": "user@gmail.com",
  "is_connected": true,
  "storage_used": "2.5GB",
  "storage_limit": "15GB",
  "connected_at": "2024-01-15T10:30:00Z"
}
```

## Features

- Multi-service support
- File synchronization
- Automatic backups
- File sharing
- Version control
- Search capabilities

---

*This documentation will be expanded with detailed examples and complete API reference.*

---

## Comments
Source file : `src/rest-api/comments.md`

# Comments

The Comments API allows you to manage comments on tasks in Fluent Boards. You can create, read, update, and delete comments, as well as handle threaded replies and file attachments.

## List Task Comments

Retrieve all comments for a specific task.

**HTTP Request**
```
GET /wp-json/fluent-boards/v2/projects/{board_id}/tasks/{task_id}/comments
```

### Example Request

```bash
curl "https://yourdomain.com/wp-json/fluent-boards/v2/projects/{board_id}/tasks/{task_id}/comments?per_page=10&page=1&include_replies=true&include_images=true" \
  -H "Authorization: Basic API_USERNAME:API_PASSWORD"
```

### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `page` | integer | Page number for pagination (default: 1) |
| `per_page` | integer | Number of comments per page (default: 10) |
| `type` | string | Filter by comment type (e.g., 'comment') |
| `privacy` | string | Filter by privacy setting (e.g., 'private', 'public') |
| `include_replies` | boolean | Include threaded replies (default: true) |
| `include_images` | boolean | Include attached images (default: true) |

### Example Response

```json
{
  "comments": {
    "current_page": 1,
    "data": [
      {
        "id": 123,
        "board_id": "5",
        "task_id": "456",
        "parent_id": null,
        "type": "comment",
        "privacy": "private",
        "status": "published",
        "author_name": "John Doe",
        "author_email": "john.doe@example.com",
        "author_ip": "192.168.1.100",
        "description": "This is a comment on the task",
        "created_by": "789",
        "settings": {
          "raw_description": "This is a comment on the task",
          "mentioned_id": null
        },
        "created_at": "2024-01-15T10:30:00+00:00",
        "updated_at": "2024-01-15T10:30:00+00:00",
        "replies": [],
        "replies_count": 0,
        "avatar": "https://secure.gravatar.com/avatar/abc123def456?s=128&d=mm&r=g",
        "user": {
          "ID": 789,
          "user_login": "johndoe",
          "user_nicename": "john-doe",
          "user_email": "john.doe@example.com",
          "user_url": "https://example.com",
          "user_registered": "2023-01-15 10:30:00",
          "user_status": "0",
          "display_name": "John Doe",
          "photo": "https://secure.gravatar.com/avatar/abc123def456?s=128&d=mm&r=g"
        },
        "images": []
      }
    ],
    "first_page_url": "https://example.com/wp-json/fluent-boards/v2/projects/5/tasks/456/comments/?page=1",
    "from": 1,
    "last_page": 1,
    "last_page_url": "https://example.com/wp-json/fluent-boards/v2/projects/5/tasks/456/comments/?page=1",
    "links": [
      {
        "url": null,
        "label": "pagination.previous",
        "active": false
      },
      {
        "url": "https://example.com/wp-json/fluent-boards/v2/projects/5/tasks/456/comments/?page=1",
        "label": "1",
        "active": true
      },
      {
        "url": null,
        "label": "pagination.next",
        "active": false
      }
    ],
    "next_page_url": null,
    "path": "https://example.com/wp-json/fluent-boards/v2/projects/5/tasks/456/comments",
    "per_page": 10,
    "prev_page_url": null,
    "to": 1,
    "total": 1
  },
  "total": 1
}
```

## Create a Comment

Create a new comment on a task.

**HTTP Request**
```
POST /wp-json/fluent-boards/v2/projects/{board_id}/tasks/{task_id}/comments
```

### Example Request

```bash
curl "https://yourdomain.com/wp-json/fluent-boards/v2/projects/{board_id}/tasks/{task_id}/comments" \
  -X POST \
  -H "Authorization: Basic API_USERNAME:API_PASSWORD" \
  -H "Content-Type: application/json" \
  -d '{
    "comment": "Hey @johndoe, please review this design...",
    "parent_id": null,
    "comment_type": "comment",
    "comment_by": 789,
    "images": [1, 2],
    "mentionData": [789]
  }'
```

### Request Body

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `comment` | string | Yes* | The comment content (required unless images are provided) |
| `parent_id` | integer | No | ID of parent comment for threaded replies |
| `comment_type` | string | Yes | Comment type (must be 'comment') |
| `comment_by` | integer | No | User ID who created the comment (default: current user) |
| `images` | array | No | Array of image IDs to attach to the comment |
| `mentionData` | array | No | Array of user IDs to mention in the comment |

### Features

- **Auto-linking**: URLs in comments are automatically converted to clickable links
- **Mentions**: Use `mentionData` to mention users with `@username` format
- **Image Attachments**: Attach multiple images using image IDs
- **Threaded Replies**: Create replies by setting `parent_id`
- **Email Notifications**: Automatic email notifications to task assignees and mentioned users

### Example request data

**Request:**
```json
{
  "comment": "Hey @johndoe, please review this design at https://figma.com/file/abc123 and also check https://github.com/fluent-boards. I've attached the mockups below.",
  "parent_id": null,
  "comment_type": "comment",
  "comment_by": 789,
  "images": [1, 2],
  "mentionData": [789]
}
```

### Example response

**Response:**
```json
{
  "message": "Comment has been added",
  "comment": {
    "parent_id": null,
    "description": "Hey @johndoe, please review this design at <a class=\"fbs_link\" target=\"_blank\" rel=\"noopener noreferrer\" href=\"https://figma.com/file/abc123\">https://figma.com/file/abc123</a> and also check <a class=\"fbs_link\" target=\"_blank\" rel=\"noopener noreferrer\" href=\"https://github.com/fluent-boards.\">https://github.com/fluent-boards.</a> I've attached the mockups below.",
    "created_by": 789,
    "task_id": 456,
    "type": "comment",
    "board_id": 5,
    "settings": {
      "raw_description": "Hey @johndoe, please review this design at https://figma.com/file/abc123 and also check https://github.com/fluent-boards. I've attached the mockups below.",
      "mentioned_id": [789]
    },
    "privacy": "private",
    "author_email": "john.doe@example.com",
    "author_name": "John Doe",
    "updated_at": "2024-01-15T12:00:00+00:00",
    "created_at": "2024-01-15T12:00:00+00:00",
    "id": 123,
    "user": {
      "ID": 789,
      "user_login": "johndoe",
      "user_nicename": "john-doe",
      "user_email": "john.doe@example.com",
      "user_url": "https://example.com",
      "user_registered": "2023-01-15 10:30:00",
      "user_status": "0",
      "display_name": "John Doe",
      "photo": "https://secure.gravatar.com/avatar/abc123def456?s=128&d=mm&r=g"
    },
    "avatar": "https://secure.gravatar.com/avatar/abc123def456?s=128&d=mm&r=g",
    "task": {
      "id": 456,
      "parent_id": null,
      "board_id": "5",
      "crm_contact_id": null,
      "title": "Implement New Dashboard Features",
      "slug": "implement-new-dashboard-features",
      "type": "task",
      "status": "open",
      "stage_id": "25",
      "source": "web",
      "source_id": null,
      "priority": "medium",
      "description": "<p>Add new dashboard features including:</p>\n<ol>\n<li>Custom widgets</li>\n<li>Analytics charts</li>\n<li>User preferences</li>\n<li>Real-time updates</li>\n</ol>",
      "lead_value": "0.00",
      "created_by": "789",
      "position": "15.00",
      "comments_count": 3,
      "issue_number": null,
      "reminder_type": "none",
      "settings": {
        "subtask_count": 4,
        "attachment_count": 2,
        "subtask_completed_count": 1
      },
      "remind_at": null,
      "started_at": null,
      "due_at": "2024-02-15 23:59:00",
      "last_completed_at": null,
      "archived_at": null,
      "created_at": "2024-01-10T10:00:00+00:00",
      "updated_at": "2024-01-15T12:00:00+00:00",
      "meta": {
        "is_template": "no",
        "group_name": "Development Tasks"
      },
      "repeat_task_meta": null
    },
    "images": [
      {
        "id": 1,
        "object_id": "123",
        "object_type": "comment_image",
        "attachment_type": "image/png",
        "file_path": "/var/www/example.com/wp-content/uploads/fluent-boards/board_5/1705312800-design-mockup-1.png",
        "full_url": "https://example.com/wp-content/uploads/fluent-boards/board_5/1705312800-design-mockup-1.png",
        "settings": "",
        "title": "design-mockup-1.png",
        "file_hash": "abc123def456789ghi012jkl345mno678",
        "driver": "local",
        "status": "ACTIVE",
        "file_size": "512 KB",
        "created_at": "2024-01-15T11:55:00+00:00",
        "updated_at": "2024-01-15T12:00:00+00:00",
        "secure_url": "https://example.com/index.php?fbs=1&fbs_comment_image=abc123def456789ghi012jkl345mno678&secure_sign=def456ghi789012jkl345mno678pqr901"
      },
      {
        "id": 2,
        "object_id": "123",
        "object_type": "comment_image",
        "attachment_type": "image/png",
        "file_path": "/var/www/example.com/wp-content/uploads/fluent-boards/board_5/1705312860-design-mockup-2.png",
        "full_url": "https://example.com/wp-content/uploads/fluent-boards/board_5/1705312860-design-mockup-2.png",
        "settings": "",
        "title": "design-mockup-2.png",
        "file_hash": "def456ghi789012jkl345mno678pqr901",
        "driver": "local",
        "status": "ACTIVE",
        "file_size": "384 KB",
        "created_at": "2024-01-15T11:56:00+00:00",
        "updated_at": "2024-01-15T12:00:00+00:00",
        "secure_url": "https://example.com/index.php?fbs=1&fbs_comment_image=def456ghi789012jkl345mno678pqr901&secure_sign=ghi789jkl012345mno678pqr901stu234"
      }
    ],
    "replies": []
  }
}
```

### Features Demonstrated

- **Text Content**: Comment with multiple lines and context
- **User Mentions**: `@johndoe` and `@janesmith` with `mentionData` array
- **URL Auto-linking**: Multiple URLs automatically converted to clickable links
- **Image Attachments**: Multiple images with different file types
- **Threaded Comments**: `parent_id` for replies
- **Comment Type**: Specified as "comment" for top-level comments or "reply" for threaded replies
- **User Assignment**: Explicit `comment_by` parameter


## Update a Comment

Update an existing comment. Only the comment author can update their own comments.

**HTTP Request**
```
PUT /wp-json/fluent-boards/v2/projects/{board_id}/tasks/{task_id}/comments/{comment_id}
```

### Example Request

```bash
curl "https://yourdomain.com/wp-json/fluent-boards/v2/projects/{board_id}/tasks/{task_id}/comments/{comment_id}" \
  -X PUT \
  -H "Authorization: Basic API_USERNAME:API_PASSWORD" \
  -H "Content-Type: application/json" \
  -d '{
    "comment": "This is the updated comment content with https://example.com link",
    "images": [1, 2],
    "mentionData": [789]
  }'
```

### Request Body

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `comment` | string | Yes* | The updated comment content (required unless images are provided) |
| `images` | array | No | Array of image IDs to attach to the comment |
| `mentionData` | array | No | Array of user IDs to mention in the comment |

### Example Request Data

```json
{
  "comment": "This is the updated comment content with https://example.com link",
  "images": [1, 2],
  "mentionData": [789]
}
```

### Example Response

```json
{
  "message": "Comment has been updated",
  "comment": {
    "id": 4,
    "board_id": "3",
    "task_id": "85",
    "parent_id": null,
    "type": "comment",
    "privacy": "private",
    "status": "published",
    "author_name": "John Doe",
    "author_email": "john.doe@example.com",
    "author_ip": "",
    "description": "Hey <a class=\"fbs_mention\" href=\"https://example.com/projects#/member/789/tasks\">John Doe</a> , please review this design at <a class=\"fbs_link\" target=\"_blank\" rel=\"noopener noreferrer\" href=\"https://figma.com/file/abc123\">https://figma.com/file/abc123</a> and also check <a class=\"fbs_link\" target=\"_blank\" rel=\"noopener noreferrer\" href=\"https://github.com/fluent-boards.\">https://github.com/fluent-boards.</a> I've attached the mockups below.",
    "created_by": "789",
    "settings": {
      "raw_description": "Hey @johndoe , please review this design at https://figma.com/file/abc123 and also check https://github.com/fluent-boards. I've attached the mockups below.",
      "mentioned_id": ["789"]
    },
    "created_at": "2024-01-15T12:00:00+00:00",
    "updated_at": "2024-01-15T13:00:00+00:00",
    "avatar": "https://secure.gravatar.com/avatar/abc123def456?s=128&d=mm&r=g",
    "images": [
      {
        "id": 28,
        "object_id": "4",
        "object_type": "comment_image",
        "attachment_type": "image/png",
        "file_path": "/var/www/example.com/wp-content/uploads/fluent-boards/board_3/1705312800-updated-image.png",
        "full_url": "https://example.com/wp-content/uploads/fluent-boards/board_3/1705312800-updated-image.png",
        "settings": "",
        "title": "updated-image.png",
        "file_hash": "abc123def456789ghi012jkl345mno678",
        "driver": "local",
        "status": "ACTIVE",
        "file_size": "484 KB",
        "created_at": "2024-01-15T13:00:00+00:00",
        "updated_at": "2024-01-15T13:00:00+00:00",
        "secure_url": "https://example.com/index.php?fbs=1&fbs_comment_image=abc123def456789ghi012jkl345mno678&secure_sign=def456ghi789012jkl345mno678pqr901"
      }
    ],
    "replies": [],
    "user": {
      "ID": 789,
      "user_login": "johndoe",
      "user_nicename": "john-doe",
      "user_email": "john.doe@example.com",
      "user_url": "https://example.com",
      "user_registered": "2023-01-15 10:30:00",
      "user_status": "0",
      "display_name": "John Doe",
      "photo": "https://secure.gravatar.com/avatar/abc123def456?s=128&d=mm&r=g"
    }
  }
}
```

### Features

- **Authorization**: Only the comment author can update their own comments
- **Auto-linking**: URLs are automatically converted to clickable links
- **Mentions**: Support for user mentions with notifications
- **Image Attachments**: Can update or add new images to the comment
- **Settings Preservation**: Maintains existing settings while updating content

## Delete a Comment

Delete a comment. Only the comment author can delete their own comments.

**HTTP Request**
```
DELETE /wp-json/fluent-boards/v2/projects/{board_id}/tasks/comments/{comment_id}
```

### Example Request

```bash
curl "https://yourdomain.com/wp-json/fluent-boards/v2/projects/{board_id}/tasks/comments/{comment_id}" \
  -X DELETE \
  -H "Authorization: Basic API_USERNAME:API_PASSWORD"
```

### Example Response

```json
{
  "message": "Comment has been deleted"
}
```

### Features

- **Authorization**: Only the comment author can delete their own comments
- **Cascade Deletion**: Automatically deletes related replies and attached images
- **Task Counter**: Updates the task's comment count
- **Cleanup**: Removes all associated data and triggers cleanup actions

## Add Reply to Comment

Create a threaded reply to an existing comment. Replies use the same endpoint as creating comments, but with a `parent_id` parameter.

**HTTP Request**
```
POST /wp-json/fluent-boards/v2/projects/{board_id}/tasks/{task_id}/comments
```

### Example Request

```bash
curl "https://yourdomain.com/wp-json/fluent-boards/v2/projects/{board_id}/tasks/{task_id}/comments" \
  -X POST \
  -H "Authorization: Basic API_USERNAME:API_PASSWORD" \
  -H "Content-Type: application/json" \
  -d '{
    "comment": "This is a reply to the comment",
    "parent_id": 3,
    "comment_type": "reply",
    "comment_by": 789,
    "images": [],
    "mentionData": []
  }'
```

### Request Body

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `comment` | string | Yes* | The reply content (required unless images are provided) |
| `parent_id` | integer | Yes | ID of the parent comment to reply to |
| `comment_type` | string | Yes | Comment type (must be 'reply') |
| `comment_by` | integer | No | User ID who created the reply (default: current user) |
| `images` | array | No | Array of image IDs to attach to the reply |
| `mentionData` | array | No | Array of user IDs to mention in the reply |

### Example Request Data

```json
{
  "comment": "This is a reply to the comment",
  "parent_id": 3,
  "comment_type": "reply",
  "comment_by": 789,
  "images": [],
  "mentionData": []
}
```

### Example Response

```json
{
  "message": "Comment has been added",
  "comment": {
    "parent_id": 3,
    "description": "This is a reply to the comment",
    "created_by": 789,
    "task_id": 456,
    "type": "reply",
    "board_id": 5,
    "settings": {
      "raw_description": "This is a reply to the comment",
      "mentioned_id": null
    },
    "privacy": "private",
    "author_email": "john.doe@example.com",
    "author_name": "John Doe",
    "updated_at": "2024-01-15T14:00:00+00:00",
    "created_at": "2024-01-15T14:00:00+00:00",
    "id": 8,
    "user": {
      "ID": 789,
      "user_login": "johndoe",
      "user_nicename": "john-doe",
      "user_email": "john.doe@example.com",
      "user_url": "https://example.com",
      "user_registered": "2023-01-15 10:30:00",
      "user_status": "0",
      "display_name": "John Doe",
      "photo": "https://secure.gravatar.com/avatar/abc123def456?s=128&d=mm&r=g"
    },
    "avatar": "https://secure.gravatar.com/avatar/abc123def456?s=128&d=mm&r=g",
    "task": {
      "id": 456,
      "parent_id": null,
      "board_id": "5",
      "crm_contact_id": null,
      "title": "Implement New Dashboard Features",
      "slug": "implement-new-dashboard-features",
      "type": "task",
      "status": "open",
      "stage_id": "25",
      "source": "web",
      "source_id": null,
      "priority": "medium",
      "description": "<p>Add new dashboard features including:</p>\n<ol>\n<li>Custom widgets</li>\n<li>Analytics charts</li>\n<li>User preferences</li>\n<li>Real-time updates</li>\n</ol>",
      "lead_value": "0.00",
      "created_by": "789",
      "position": "15.00",
      "comments_count": "3",
      "issue_number": null,
      "reminder_type": "none",
      "settings": {
        "subtask_count": 4,
        "attachment_count": 2,
        "subtask_completed_count": 1
      },
      "remind_at": null,
      "started_at": null,
      "due_at": "2024-02-15 23:59:00",
      "last_completed_at": null,
      "archived_at": null,
      "created_at": "2024-01-10T10:00:00+00:00",
      "updated_at": "2024-01-15T14:00:00+00:00",
      "meta": {
        "is_template": "no",
        "group_name": "Development Tasks"
      },
      "repeat_task_meta": null
    }
  }
}
```

### Key Differences from Regular Comments

- **Parent ID**: Required `parent_id` parameter to specify which comment to reply to
- **Comment Type**: Automatically set to "reply" type
- **Threading**: Creates a parent-child relationship between comments
- **Notifications**: Sends notifications to the parent comment author
- **Same Endpoint**: Uses the same endpoint as creating comments

## Upload Images to Comment

Upload images that can be attached to comments. This endpoint uploads the image file and returns the image attachment data that can be used in comment creation.

**HTTP Request**
```
POST /wp-json/fluent-boards/v2/projects/{board_id}/tasks/{task_id}/comment-image-upload
```

### Example Request

```bash
curl "https://yourdomain.com/wp-json/fluent-boards/v2/projects/{board_id}/tasks/{task_id}/comment-image-upload" \
  -X POST \
  -H "Authorization: Basic API_USERNAME:API_PASSWORD" \
  -F "file=@/path/to/unnamed-3.png"
```

### Request Body

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `file` | file | Yes | Image file to upload (supports: JPEG, GIF, PNG, BMP, TIFF, WebP, AVIF, ICO, HEIC) |

### Example Response

```json
{
  "message": "attachment has been added",
  "imageAttachment": {
    "object_id": 0,
    "object_type": "comment_image",
    "attachment_type": "image/png",
    "title": "unnamed-3.png",
    "file_path": "1711111111-unnamed-3.png",
    "full_url": "https://yourdomain.com/wp-content/uploads/fluent-boards/board_1/1711111111-unnamed-3.png",
    "file_size": "484 KB",
    "settings": "",
    "driver": "local",
    "file_hash": "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
    "updated_at": "2025-08-08T06:56:07+00:00",
    "created_at": "2025-08-08T06:56:07+00:00",
    "id": 24,
    "public_url": "https://yourdomain.com/index.php?fbs=1&fbs_type=public_url&fbs_bid=1&fbs_comment_image=aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
    "secure_url": "https://yourdomain.com/index.php?fbs=1&fbs_comment_image=aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa&secure_sign=bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb"
  }
}
```


### Features

- **File Validation**: Validates image file types (JPEG, GIF, PNG, BMP, TIFF, WebP, AVIF, ICO, HEIC)
- **Secure URLs**: Provides both public and secure URLs for image access
- **File Metadata**: Includes file size, hash, and upload timestamps
- **Comment Integration**: Returns image ID that can be used in comment creation
- **Board Organization**: Images are organized by board ID in the file system

## Features

- **Threaded Comments**: Support for nested replies
- **File Attachments**: Upload images to comments
- **Privacy Controls**: Public and private comment visibility
- **User Integration**: Automatic user data population
- **Avatar Generation**: Dynamic avatar URLs based on email
- **Comment Counting**: Automatic task comment count updates

## Error Responses

See [Common Error Responses](/rest-api/shared/error-responses) for standard error formats.

### Common Comment-Specific Errors

- **404 Not Found** - Comment not found
- **403 Forbidden** - You don't have permission to manage this comment
- **400 Bad Request** - Invalid comment data or missing required fields
- **413 Payload Too Large** - Image file size exceeds limit

## Best Practices

1. **Use descriptive comments** - Provide clear, actionable feedback
2. **Respect privacy settings** - Be mindful of public vs private comments
3. **Use threading appropriately** - Keep replies organized and relevant
4. **Optimize images** - Compress images before uploading
5. **Regular cleanup** - Remove outdated or irrelevant comments

---

## Custom Fields
Source file : `src/rest-api/custom-fields.md`

# Custom Fields

The Custom Fields API allows you to define additional data fields for tasks on a board. These endpoints are available in Fluent Boards Pro.

## Base Endpoint

```
/fluent-boards/v2/projects/{board_id}/custom-fields
```

## Custom Field Object

Custom fields extend task data with additional structured information:

```json
{
  "id": 110,
  "board_id": "3",
  "title": "Loerm ipsum",
  "slug": "loerm-ipsum",
  "type": "custom-field",
  "position": "1.00",
  "color": null,
  "bg_color": null,
  "settings": {
    "custom_field_type": "text"
  },
  "archived_at": null,
  "created_at": "2025-08-08T10:56:47+00:00",
  "updated_at": "2025-08-08T10:56:47+00:00"
}
```

### Key Properties

| Property | Type | Description |
|----------|------|-------------|
| `id` | integer | Unique identifier for the custom field |
| `board_id` | string | ID of the board this field belongs to |
| `title` | string | Display label for the custom field |
| `slug` | string | URL-friendly identifier |
| `type` | string | Always "custom-field" |
| `position` | string | Position for ordering fields |
| `settings.custom_field_type` | string | Field type (text, select, checkbox, date, etc.) |
| `archived_at` | string or null | Archive timestamp (null if active) |

## List Board Custom Fields

Retrieve all custom fields defined for a specific board.

**HTTP Request**
```
GET /wp-json/fluent-boards/v2/projects/{board_id}/custom-fields
```

### Example Request

```bash
curl "https://yourdomain.com/wp-json/fluent-boards/v2/projects/{board_id}/custom-fields" \
  -H "Authorization: Basic API_USERNAME:API_PASSWORD"
```

### Example Response

```json
{
  "customFields": [
    {
      "id": 110,
      "board_id": "3",
      "title": "Loerm ipsum",
      "slug": "loerm-ipsum",
      "type": "custom-field",
      "position": "1.00",
      "color": null,
      "bg_color": null,
      "settings": {
        "custom_field_type": "text"
      },
      "archived_at": null,
      "created_at": "2025-08-08T10:56:47+00:00",
      "updated_at": "2025-08-08T10:56:47+00:00"
    }
  ]
}
```

## Create a Custom Field

Create a new custom field for a board.

**HTTP Request**
```
POST /wp-json/fluent-boards/v2/projects/{board_id}/custom-field
```

### Example Request

```bash
curl -X POST "https://yourdomain.com/wp-json/fluent-boards/v2/projects/{board_id}/custom-field" \
  -H "Authorization: Basic API_USERNAME:API_PASSWORD" \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "customField[title]=My custom filed&customField[type]=text"
```

### Request Body

| Field | Type | Required | Description |
|------|------|----------|-------------|
| `customField.title` | string | Yes | Field label |
| `customField.type` | string | Yes | One of supported types (stored as `settings.custom_field_type`) |
| `customField.options` | array[string] | No | Options for `select` type |

### Example Response

```json
{
  "customField": {
    "board_id": "3",
    "title": "My custom filed",
    "slug": "my-custom-filed",
    "settings": {
      "custom_field_type": "text"
    },
    "position": 2,
    "type": "custom-field",
    "updated_at": "2025-08-08T10:59:17+00:00",
    "created_at": "2025-08-08T10:59:17+00:00",
    "id": 111
  },
  "message": "Custom field has been successfully created"
}
```

## Update a Custom Field

Update an existing custom field.

**HTTP Request**
```
PUT /wp-json/fluent-boards/v2/projects/{board_id}/custom-field/{custom_field_id}
```

### Example Request

```bash
curl -X PUT "https://yourdomain.com/wp-json/fluent-boards/v2/projects/{board_id}/custom-field/{custom_field_id}" \
  -H "Authorization: Basic API_USERNAME:API_PASSWORD" \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "customField[title]=Custom text field&customField[type]=text"
```

### Request Body

| Field | Type | Required | Description |
|------|------|----------|-------------|
| `customField.title` | string | Yes | Field label |
| `customField.type` | string | Yes | One of supported types (stored as `settings.custom_field_type`) |
| `customField.options` | array[string] | No | Options for `select` type |

### Example Response

```json
{
  "customField": {
    "id": 111,
    "board_id": "3",
    "title": "Custom text field",
    "slug": "my-custom-filed",
    "type": "custom-field",
    "position": "2.00",
    "color": null,
    "bg_color": null,
    "settings": {
      "custom_field_type": "text"
    },
    "archived_at": null,
    "created_at": "2025-08-08T10:59:17+00:00",
    "updated_at": "2025-08-08T11:02:38+00:00"
  },
  "message": "Custom field has been updated successfully"
}
```

## Update Custom Field Position

Change the position/order of a custom field within the board.

**HTTP Request**
```
PUT /wp-json/fluent-boards/v2/projects/{board_id}/custom-field/{custom_field_id}/update-position
```

### Example Request

```bash
curl -X PUT "https://yourdomain.com/wp-json/fluent-boards/v2/projects/{board_id}/custom-field/{custom_field_id}/update-position" \
  -H "Authorization: Basic API_USERNAME:API_PASSWORD" \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "newIndex=1"
```

### Request Body

| Field | Type | Required | Description |
|------|------|----------|-------------|
| `newIndex` | integer | Yes | 1-based new position index |

### Example Response

```json
{
  "message": "Custom field position has been updated successfully"
}
```

## Delete a Custom Field

Remove a custom field from a board.

**HTTP Request**
```
DELETE /wp-json/fluent-boards/v2/projects/{board_id}/custom-field/{custom_field_id}
```

### Example Request

```bash
curl -X DELETE "https://yourdomain.com/wp-json/fluent-boards/v2/projects/{board_id}/custom-field/{custom_field_id}" \
  -H "Authorization: Basic API_USERNAME:API_PASSWORD"
```

### Example Response

```json
{
  "message": "Custom field has been deleted successfully"
}
```

## Get Custom Fields for a Task

Retrieve custom field values for a specific task.

**HTTP Request**
```
GET /wp-json/fluent-boards/v2/projects/{board_id}/tasks/{task_id}/custom-fields
```

### Example Request

```bash
curl "https://yourdomain.com/wp-json/fluent-boards/v2/projects/{board_id}/tasks/{task_id}/custom-fields" \
  -H "Authorization: Basic API_USERNAME:API_PASSWORD"
```

### Example Response

```json
{
  "customFields": [
    {
      "id": 99,
      "object_id": "85",
      "object_type": "task_custom_field",
      "foreign_id": "111",
      "settings": {
        "value": "Hello world"
      },
      "preferences": null
    }
  ]
}
```

## Save Custom Field Value for a Task

Set or update a custom field value for a specific task.

**HTTP Request**
```
POST /wp-json/fluent-boards/v2/projects/{board_id}/tasks/{task_id}/custom-fields
```

### Example Request

```bash
curl -X POST "https://yourdomain.com/wp-json/fluent-boards/v2/projects/{board_id}/tasks/{task_id}/custom-fields" \
  -H "Authorization: Basic API_USERNAME:API_PASSWORD" \
  -H "Content-Type: application/json" \
  -d '{
    "custom_field_id": 111,
    "value": "Lorem ipsum"
  }'
```

### Request Body

| Field | Type | Required | Description |
|------|------|----------|-------------|
| `custom_field_id` | integer | Yes | The custom field ID |
| `value` | string | Yes | Value to save; for `checkbox` send `true`/`false`; for `date` send a parseable date |

### Example Response

```json
{
  "customField": {
    "id": 111,
    "board_id": "3",
    "title": "Custom text field",
    "slug": "my-custom-filed",
    "type": "custom-field",
    "position": "0.50",
    "color": null,
    "bg_color": null,
    "settings": {
      "custom_field_type": "text"
    },
    "archived_at": null,
    "created_at": "2025-08-08T10:59:17+00:00",
    "updated_at": "2025-08-08T11:06:58+00:00"
  }
}
```

## Error Responses

See [Common Error Responses](/rest-api/shared/error-responses) for standard error formats.

### Common Custom Field-Specific Errors

- **404 Not Found** - Custom field or board not found
- **403 Forbidden** - You don't have permission to manage custom fields
- **400 Bad Request** - Invalid custom field data or missing required fields

---

## Extending the REST API
Source file : `src/rest-api/extend.md`

# Extending the REST API
<Badge type="tip" vertical="top" text="Fluent Framework" />

This guide shows how to add custom REST endpoints (routes, controllers, policies) to FluentBoards using the underlying Fluent Framework.

> If you only need to consume existing endpoints, see the main REST resources pages first.

## Registering a Custom Endpoint
(Coming from previous guide text – revise examples below to match your namespace/app.)

FluentBoards uses the WordPress REST API infrastructure, so any WP‑supported auth method (cookies+nonce, Application Passwords, OAuth layer you add) will work.

You can register routes, apply policies, and point to controller methods.

## Routing
```php
add_action( 'fluent_boards_loaded', function( $app ) {
    $app->router->prefix( 'my-prefix' )
        ->withPolicy( 'MyPlugin\\Policies\\MyPolicy' )
        ->group( function( $router ) {
            $router->get( '/', 'MyPlugin\\Controllers\\MyController@index' );
            // more routes go here
        } );
});
```
The above code registers a route that will be accessible at:
```
https://example.com/wp-json/fluent-boards/v2/my-prefix/
```
Base URL pattern:
```
https://example.com/wp-json/fluent-boards/v2/
```
NOTE: Ensure your classes autoload before the fluent_boards_loaded action fires.

```php
$app->router->post( '/your-url-path/', 'MyPlugin\\Controllers\\MyController@create');
```
### Route Parameters
```php
$app->router->get('/show/{id}', 'MyPlugin\\Controllers\\MyController@show')->int('id');
$app->router->get('/show/{id}/{name}', 'MyPlugin\\Controllers\\MyController@show')->int('id')->alpha('name');
```
Controller method will receive parameters directly.

### Available Router Methods
```php
$router->get($uri, $callback);
$router->post($uri, $callback);
$router->put($uri, $callback);
$router->patch($uri, $callback);
$router->delete($uri, $callback);
$router->any($uri, $callback); // any verb
```
## Controllers
```php
namespace MyPlugin\Controllers;
use FluentCrm\Framework\Http\Controller;
class MyController extends Controller {
    public function index() {
        return $this->sendSuccess(['ok' => true], 200);
    }
    public function create() {
        $data = $this->request->all();
        return $this->sendSuccess($data, 201);
    }
}
```
Key helper methods:
- send / sendSuccess / sendError
- request
- response

## Policies
```php
namespace MyPlugin\Policies;
use FluentCrm\App\Http\Policies\BasePolicy;
use FluentCrm\Framework\Request\Request;
class MyPolicy extends BasePolicy {
    public function verifyRequest(Request $request) {
        return current_user_can('manage_options');
    }
}
```
Return true to authorize. Add capability checks or custom logic.

## Directory Structure Example
```
my-plugin/
├── my-plugin.php
├── Policies/
│   └── MyPolicy.php
└── Controllers/
    └── MyController.php
```

## Next Steps
- Add more routes for CRUD.
- Introduce caching or permission layers.
- Emit action hooks inside controllers for other add‑ons.

> Tip: Keep your REST layer thin-move business logic into service classes so CLI, cron, or hooks can reuse it.

---

## Folders
Source file : `src/rest-api/folders.md`

# Folders

The Folders API allows you to group and organize boards in Fluent Boards. These endpoints are Pro-only and live under the admin prefix.

## Base Endpoint

```
/wp-json/fluent-boards/v2/admin/folders
```

```json
{
  "id": 11,
  "title": "Lorem Ipsum",
  "created_by": "1",
  "boards_ids": [
    3
  ]
}
```

## List Folders

Retrieve all folders in the system.

**HTTP Request**
```
GET /wp-json/fluent-boards/v2/admin/folders
```

### Example Request

```bash
curl "https://yourdomain.com/wp-json/fluent-boards/v2/admin/folders" \
  -H "Authorization: Basic API_USERNAME:API_PASSWORD"
```

### Example Response

```json
{
  "folders": [
    {
      "id": 11,
      "title": "Lorem Ipsum",
      "created_by": "1",
      "boards_ids": [
        3
      ]
    }
  ]
}
```

## Create a Folder

Create a new folder to organize boards.

**HTTP Request**
```
POST /wp-json/fluent-boards/v2/admin/folders
```

### Example Request

```bash
curl -X POST "https://yourdomain.com/wp-json/fluent-boards/v2/admin/folders" \
  -H "Authorization: Basic API_USERNAME:API_PASSWORD" \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "title=Development"
```

### Request Body

| Field | Type | Required | Description |
|------|------|----------|-------------|
| `title` | string | Yes | Folder title (max 50 chars) |

### Example Response

```json
{
  "message": "Folder has been created",
  "folder": {
    "id": 12,
    "title": "Development",
    "created_by": 1,
    "boards_ids": []
  }
}
```

## Update a Folder

Update an existing folder's title.

**HTTP Request**
```
PUT /wp-json/fluent-boards/v2/admin/folders/{folder_id}
```

### Example Request

```bash
curl -X PUT "https://yourdomain.com/wp-json/fluent-boards/v2/admin/folders/{folder_id}" \
  -H "Authorization: Basic API_USERNAME:API_PASSWORD" \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "title=Marketing"
```

### Request Body

| Field | Type | Required | Description |
|------|------|----------|-------------|
| `title` | string | Yes | New folder title |

### Example Response

```json
{
  "message": "Folder updated successfully",
  "folder": {
    "id": 11,
    "title": "Marketing",
    "created_by": "1",
    "boards_ids": []
  }
}
```

## Delete a Folder

Remove a folder from the system.

**HTTP Request**
```
DELETE /wp-json/fluent-boards/v2/admin/folders/{folder_id}
```

### Example Request

```bash
curl -X DELETE "https://yourdomain.com/wp-json/fluent-boards/v2/admin/folders/{folder_id}" \
  -H "Authorization: Basic API_USERNAME:API_PASSWORD"
```

### Example Response

```json
{
  "message": "Folder deleted successfully."
}
```

## Add Boards to Folder

Add one or more boards to a folder. This replaces any existing folder assignments.

**HTTP Request**
```
POST /wp-json/fluent-boards/v2/admin/folders/{folder_id}/add-board
```

### Example Request

```bash
curl -X POST "https://yourdomain.com/wp-json/fluent-boards/v2/admin/folders/{folder_id}/add-board" \
  -H "Authorization: Basic API_USERNAME:API_PASSWORD" \
  -H "Content-Type: application/json" \
  -d '{
    "board_ids": [2,7]
  }'
```

### Request Body

| Field | Type | Required | Description |
|------|------|----------|-------------|
| `board_ids` | array[integer] | Yes | Board IDs to add; replaces existing folder assignment |

### Example Response

```json
{
  "message": "Added to folder successfully!"
}
```

## Remove Board from Folder

Remove a specific board from a folder.

**HTTP Request**
```
POST /wp-json/fluent-boards/v2/admin/folders/{folder_id}/remove-board
```

### Example Request

```bash
curl -X POST "https://yourdomain.com/wp-json/fluent-boards/v2/admin/folders/{folder_id}/remove-board" \
  -H "Authorization: Basic API_USERNAME:API_PASSWORD" \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "board_id=7"
```

### Request Body

| Field | Type | Required | Description |
|------|------|----------|-------------|
| `board_id` | integer | Yes | Board ID to remove from folder |

### Example Response

```json
{
  "message": "Removed from folder successfully!"
}
```

## Error Responses

See [Common Error Responses](/rest-api/shared/error-responses) for standard error formats.

### Common Folder-Specific Errors

- **404 Not Found** - Folder not found
- **403 Forbidden** - You don't have permission to manage folders
- **400 Bad Request** - Invalid folder data or missing required fields

---

## Import/Export API
Source file : `src/rest-api/import-export.md`

# Import/Export API

> **Note:** This is a Pro feature. The Import/Export API allows you to import and export data from various sources.

## Overview

The Import/Export API provides endpoints for importing and exporting boards, tasks, and other data from various sources and formats in Fluent Boards Pro.

## Base Endpoint

```
/fluent-boards/v2/import-export
```

## Available Endpoints

### List Import Jobs
- **GET** `/import-export/imports`

### Start Import
- **POST** `/import-export/import`

### Get Import Status
- **GET** `/import-export/imports/{import_id}`

### Cancel Import
- **DELETE** `/import-export/imports/{import_id}`

### Export Data
- **POST** `/import-export/export`

### Get Export Status
- **GET** `/import-export/exports/{export_id}`

### Download Export
- **GET** `/import-export/exports/{export_id}/download`

## Supported Formats

### Import Formats
- CSV
- JSON
- XML
- Excel (.xlsx, .xls)
- Trello Export
- Asana Export
- Jira Export

### Export Formats
- CSV
- JSON
- Excel (.xlsx)
- PDF
- HTML

## Import Job Object

```json
{
  "id": 123,
  "type": "project_import",
  "status": "processing",
  "progress": 75,
  "total_items": 100,
  "processed_items": 75,
  "file_name": "boards.csv",
  "created_at": "2024-01-15T10:30:00Z",
  "updated_at": "2024-01-15T10:30:00Z"
}
```

## Features

- Bulk import/export
- Data validation
- Error handling
- Progress tracking
- Scheduled exports
- Template-based imports

---

*This documentation will be expanded with detailed examples and complete API reference.*

---

## Fluent Boards REST API
Source file : `src/rest-api/index.md`

# Fluent Boards REST API

Welcome to the Fluent Boards REST API documentation. This comprehensive guide will help you integrate with Fluent Boards using RESTful HTTP requests to manage boards, tasks, stages, and more.

## Overview

The Fluent Boards REST API provides programmatic access to your Fluent Boards data through standard HTTP methods. You can use this API to:

- **Manage Boards**: Create, read, update, and delete boards
- **Handle Tasks**: Manage tasks, subtasks, and task assignments
- **Control Stages**: Organize tasks with custom stages and workflows
## Base URL

All API requests should be made to:
```
https://yourdomain.com/wp-json/fluent-boards/v2
```

## Quick Start

1. [Explore available endpoints](/rest-api/boards)
2. [Make your first API call](/rest-api/boards#list-all-boards)


## Response Format

All API responses are returned in JSON format with consistent structure:

```json
{
  "data": {}, // Response data
  "message": "Success message",
  "total": 100, // For paginated responses
  "current_page": 1,
  "per_page": 15
}
```

## Error Handling

The API uses standard HTTP status codes and returns detailed error messages:

```json
{
  "code": "rest_invalid_param",
  "message": "Invalid parameter: title is required",
  "data": {
    "status": 400
  }
}
```

## Common HTTP Status Codes

| Code | Description |
|------|-------------|
| 200 | Success |
| 201 | Created |
| 400 | Bad Request |
| 401 | Unauthorized |
| 403 | Forbidden |
| 404 | Not Found |
| 422 | Validation Error |
| 500 | Internal Server Error |

## SDKs and Tools

While we don't provide official SDKs, the API works with any HTTP client library:
- **PHP**: Guzzle, cURL
- **JavaScript**: Axios, Fetch API
- **Python**: Requests
- **Ruby**: HTTParty
- Any language that supports HTTP requests

## Support

For support and assistance:

- **Documentation Issues**: [Submit a GitHub issue](https://github.com/WPManageNinja/fluent-boards-dev-doc/issues)
- **API Questions**: [Contact support](https://wpmanageninja.com/support-tickets/)
- **Feature Requests/Suggestions**: [Community forum](https://community.wpmanageninja.com/portal/space/fluent-boards/)

## What's Next?

Ready to start building? Begin with [Authentication](/rest-api/authentication) to set up your API access.

---

## Labels
Source file : `src/rest-api/labels.md`

# Labels

The Labels API allows you to manage task labels in Fluent Boards. You can create, read, update, and delete labels, as well as assign them to tasks.
## List All Labels

Retrieve all labels for a project.

**HTTP Request**
```
GET /wp-json/fluent-boards/v2/projects/{board_id}/labels
```

### Example Response

```json
{
  "labels": [
    {
      "id": 33,
      "board_id": "3",
      "title": "bugs",
      "slug": "",
      "type": "label",
      "position": "0.00",
      "color": null,
      "bg_color": "#E6B0AA",
      "settings": null,
      "archived_at": null,
      "created_at": "2024-12-24T08:43:51+00:00",
      "updated_at": "2024-12-24T08:43:51+00:00"
    },
    {
      "id": 34,
      "board_id": "3",
      "title": "",
      "slug": "",
      "type": "label",
      "position": "0.00",
      "color": null,
      "bg_color": "#D7BDE2",
      "settings": null,
      "archived_at": null,
      "created_at": "2024-12-24T08:43:51+00:00",
      "updated_at": "2024-12-24T08:43:51+00:00"
    },
    {
      "id": 35,
      "board_id": "3",
      "title": "improvement",
      "slug": "",
      "type": "label",
      "position": "0.00",
      "color": null,
      "bg_color": "#AED6F1",
      "settings": null,
      "archived_at": null,
      "created_at": "2024-12-24T08:43:51+00:00",
      "updated_at": "2024-12-24T08:43:51+00:00"
    }
  ]
}
```

## Create a Label

Create a new label for a project.

**HTTP Request**
```
POST /wp-json/fluent-boards/v2/projects/{board_id}/labels
```

### Request Body

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `label` | string | No | Label title |
| `color` | string | Yes | Label color (hex code) |
| `bg_color` | string | Yes | Label background color (hex code) |

### Example Request Data
```
{
  "label": "Documentation",
  "color": "#2196F3",
  "bg_color": "#0000FF"
}
```

### Example Response

```json
{
  "message": "Label has been created",
  "label": {
    "board_id": "3",
    "title": "Documentation",
    "bg_color": "#0000FF",
    "color": "#2196F3",
    "type": "label",
    "updated_at": "2025-08-07T06:12:24+00:00",
    "created_at": "2025-08-07T06:12:24+00:00",
    "id": 109
  }
}
```

## Update a Label

Update an existing label.

**HTTP Request**
```
PUT /wp-json/fluent-boards/v2/projects/{board_id}/labels/{label_id}
```

### Request Body

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `label` | string | No | Label title |
| `color` | string | No | Label color (hex code) |
| `bg_color` | string | Yes | Label background color (hex code) |

### Example Request Data

```
{
  "label": "Critical Bug",
  "color": "#D32F2F",
  "bg_color": "#D32F2F"
}
```

### Example Response

```json
{
  "message": "Label has been updated",
  "label": {
    "id": 62,
    "board_id": "5",
    "title": "Critical Bug",
    "slug": "",
    "type": "label",
    "position": "0.00",
    "color": "#FFFFFF",
    "bg_color": "#D32F2F",
    "settings": null,
    "archived_at": null,
    "created_at": "2025-07-15T07:06:48+00:00",
    "updated_at": "2025-08-07T06:23:43+00:00"
  }
}
```

## Delete a Label

Delete a label.

**HTTP Request**
```
DELETE /wp-json/fluent-boards/v2/projects/{board_id}/labels/{label_id}
```

### Example Response

```json
{
  "message": "Label has been deleted",
  "type": "success"
}
```

## Get Labels Used in Tasks

Retrieve labels that are currently assigned to tasks.

**HTTP Request**
```
GET /wp-json/fluent-boards/v2/projects/{board_id}/labels/used-in-tasks
```

### Example Response

```json
{
  "labels": [
    {
      "id": 33,
      "board_id": "3",
      "title": "bugs",
      "slug": "",
      "type": "label",
      "position": "0.00",
      "color": null,
      "bg_color": "#E6B0AA",
      "settings": null,
      "archived_at": null,
      "created_at": "2024-12-24T08:43:51+00:00",
      "updated_at": "2024-12-24T08:43:51+00:00"
    },
    {
      "id": 35,
      "board_id": "3",
      "title": "improvement",
      "slug": "",
      "type": "label",
      "position": "0.00",
      "color": null,
      "bg_color": "#AED6F1",
      "settings": null,
      "archived_at": null,
      "created_at": "2024-12-24T08:43:51+00:00",
      "updated_at": "2024-12-24T08:43:51+00:00"
    },
    {
      "id": 38,
      "board_id": "3",
      "title": "later",
      "slug": "",
      "type": "label",
      "position": "0.00",
      "color": null,
      "bg_color": "#658ca5",
      "settings": null,
      "archived_at": null,
      "created_at": "2024-12-24T08:43:51+00:00",
      "updated_at": "2024-12-24T08:43:51+00:00"
    }
  ]
}
```

## Get Task Labels

Retrieve all labels assigned to a specific task.

**HTTP Request**
```
GET /wp-json/fluent-boards/v2/projects/{board_id}/tasks/{task_id}/labels
```

### Example Response

```json
{
  "labels": [
    {
      "id": 33,
      "board_id": "3",
      "title": "bugs",
      "slug": "",
      "type": "label",
      "position": "0.00",
      "color": null,
      "bg_color": "#E6B0AA",
      "settings": null,
      "archived_at": null,
      "created_at": "2024-12-24T08:43:51+00:00",
      "updated_at": "2024-12-24T08:43:51+00:00",
      "pivot": {
        "object_id": "149",
        "foreign_id": "33",
        "settings": null,
        "created_at": "2024-12-24T08:43:53+00:00",
        "updated_at": "2024-12-24T08:43:53+00:00"
      }
    },
    {
      "id": 35,
      "board_id": "3",
      "title": "improvement",
      "slug": "",
      "type": "label",
      "position": "0.00",
      "color": null,
      "bg_color": "#AED6F1",
      "settings": null,
      "archived_at": null,
      "created_at": "2024-12-24T08:43:51+00:00",
      "updated_at": "2024-12-24T08:43:51+00:00",
      "pivot": {
        "object_id": "149",
        "foreign_id": "35",
        "settings": null,
        "created_at": "2024-12-24T08:43:53+00:00",
        "updated_at": "2024-12-24T08:43:53+00:00"
      }
    }
  ]
}
```

## Assign Labels to Task

Assign one or more labels to a task.

**HTTP Request**
```
POST /wp-json/fluent-boards/v2/projects/{board_id}/labels/task
```

### Request Body

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `taskId` | integer | Yes | The ID of the task |
| `labelId` | integer | Yes | The ID of the label to assign |

### Example Request Data

```
{
  "taskId": 149,
  "labelId": 33
}
```

### Example Response

```json
{
  "message": "Label has been added",
  "label": {
    "id": 33,
    "board_id": "3",
    "title": "bugs",
    "slug": "",
    "type": "label",
    "position": "0.00",
    "color": null,
    "bg_color": "#E6B0AA",
    "settings": null,
    "archived_at": null,
    "created_at": "2024-12-24T08:43:51+00:00",
    "updated_at": "2024-12-24T08:43:51+00:00",
    "pivot": {
      "object_id": "149",
      "foreign_id": "33",
      "settings": null,
      "created_at": "2025-08-07T06:34:51+00:00",
      "updated_at": "2025-08-07T06:34:51+00:00"
    }
  }
}
```

## Remove Label from Task

Remove a specific label from a task.

**HTTP Request**
```
DELETE /wp-json/fluent-boards/v2/projects/{board_id}/tasks/{task_id}/labels/{label_id}
```

### Example Response

```json
{
  "message": "Label has been deleted"
}
```

## Error Responses

See [Common Error Responses](/rest-api/shared/error-responses) for standard error formats.

### Common Label-Specific Errors

- **404 Not Found** - Label not found
- **403 Forbidden** - You don't have permission to manage labels
- **400 Bad Request** - Invalid label data or missing required fields

---

## Notifications API
Source file : `src/rest-api/notifications.md`

# Notifications API

> **Note:** This documentation is under development. The Notifications API allows you to manage and send notifications.

## Overview

The Notifications API provides endpoints for managing and sending notifications to users about project updates, task assignments, and other events in Fluent Boards.

## Base Endpoint

```
/fluent-boards/v2/notifications
```

## Available Endpoints

### List Notifications
- **GET** `/notifications`

### Get Notification
- **GET** `/notifications/{notification_id}`

### Mark as Read
- **PUT** `/notifications/{notification_id}/read`

### Mark All as Read
- **PUT** `/notifications/read-all`

### Delete Notification
- **DELETE** `/notifications/{notification_id}`

### Send Notification
- **POST** `/notifications/send`

### Get Notification Settings
- **GET** `/notifications/settings`

### Update Notification Settings
- **PUT** `/notifications/settings`

## Notification Object

```json
{
  "id": 123,
  "user_id": 789,
  "type": "task_assigned",
  "title": "New Task Assigned",
  "message": "You have been assigned to 'Design Homepage'",
  "data": {
    "task_id": 456,
    "project_id": 123,
    "assigned_by": 999
  },
  "is_read": false,
  "created_at": "2024-01-15T10:30:00Z"
}
```

## Notification Types

- `task_assigned` - Task assignment
- `task_completed` - Task completion
- `project_updated` - Project updates
- `comment_added` - New comments
- `due_date_approaching` - Due date reminders
- `mention` - User mentions
- `project_invitation` - Project invitations

## Features

- Real-time notifications
- Email integration
- Push notifications
- Custom notification templates
- Notification preferences
- Bulk operations

---

*This documentation will be expanded with detailed examples and complete API reference.*

---

## Permissions API
Source file : `src/rest-api/permissions.md`

# Permissions API

> **Note:** This documentation is under development. The Permissions API provides endpoints for managing user permissions and access control.

## Overview

The Permissions API provides endpoints for managing user permissions, roles, and access control across boards and system resources in Fluent Boards.

## Base Endpoint

```
/fluent-boards/v2/permissions
```

## Available Endpoints

### Get Permissions
- **GET** `/permissions`
- **GET** `/permissions/{user_id}`
- **GET** `/permissions/project/{project_id}`

### Update Permissions
- **PUT** `/permissions/{user_id}`
- **PUT** `/permissions/project/{project_id}/user/{user_id}`

### Role Management
- **GET** `/permissions/roles`
- **POST** `/permissions/roles`
- **PUT** `/permissions/roles/{role_id}`
- **DELETE** `/permissions/roles/{role_id}`

### Assign Roles
- **POST** `/permissions/assign-role`
- **DELETE** `/permissions/remove-role`

### Check Permissions
- **POST** `/permissions/check`

## Permission Types

### Project Permissions
- `view_project` - View project details
- `edit_project` - Edit project settings
- `delete_project` - Delete project
- `manage_members` - Add/remove project members
- `manage_tasks` - Create/edit/delete tasks
- `view_reports` - View project reports

### System Permissions
- `manage_users` - Manage all users
- `manage_projects` - Manage all boards
- `view_analytics` - View system analytics
- `manage_settings` - Manage system settings
- `manage_integrations` - Manage integrations

## Role Object

```json
{
  "id": 123,
  "name": "Project Manager",
  "description": "Can manage boards and tasks",
  "permissions": [
    "view_project",
    "edit_project",
    "manage_members",
    "manage_tasks",
    "view_reports"
  ],
  "is_system": false,
  "created_at": "2024-01-15T10:30:00Z",
  "updated_at": "2024-01-15T10:30:00Z"
}
```

## User Permissions Object

```json
{
  "user_id": 789,
  "global_permissions": [
    "view_analytics",
    "manage_projects"
  ],
  "project_permissions": {
    "123": [
      "view_project",
      "manage_tasks",
      "view_reports"
    ],
    "456": [
      "view_project",
      "edit_project",
      "manage_members"
    ]
  },
  "roles": [
    {
      "id": 123,
      "name": "Project Manager"
    }
  ]
}
```

## Features

- Granular permissions
- Role-based access control
- Project-specific permissions
- Permission inheritance
- Permission auditing
- Bulk permission management

---

*This documentation will be expanded with detailed examples and complete API reference.*

---

## Reports API
Source file : `src/rest-api/reports.md`

# Reports API

> **Note:** This documentation is under development. The Reports API allows you to generate and retrieve various reports and analytics.

## Overview

The Reports API provides endpoints for generating and retrieving various reports and analytics about boards, tasks, and team performance in Fluent Boards.

## Base Endpoint

```
/fluent-boards/v2/reports
```

## Available Endpoints

### List Available Reports
- **GET** `/reports`

### Generate Report
- **POST** `/reports/generate`

### Get Report
- **GET** `/reports/{report_id}`

### Download Report
- **GET** `/reports/{report_id}/download`

### Schedule Report
- **POST** `/reports/schedule`

### Get Scheduled Reports
- **GET** `/reports/scheduled`

### Delete Scheduled Report
- **DELETE** `/reports/scheduled/{schedule_id}`

## Report Types

### Project Reports
- Project Progress
- Task Completion
- Time Tracking
- Team Performance
- Resource Utilization

### Task Reports
- Task Status Distribution
- Task Priority Analysis
- Task Assignment Overview
- Task Completion Time
- Task Dependencies

### Time Reports
- Time Tracking Summary
- User Time Reports
- Project Time Analysis
- Overtime Reports
- Productivity Metrics

## Report Object

```json
{
  "id": 123,
  "name": "Project Progress Report",
  "type": "project_progress",
  "status": "completed",
  "generated_at": "2024-01-15T10:30:00Z",
  "download_url": "https://example.com/reports/123.pdf",
  "file_size": "2.5MB",
  "expires_at": "2024-02-15T10:30:00Z"
}
```

## Features

- Real-time data
- Custom date ranges
- Multiple export formats
- Automated scheduling
- Email delivery
- Interactive charts

---

*This documentation will be expanded with detailed examples and complete API reference.*

---

## Roadmaps
Source file : `src/rest-api/roadmaps.md`

# Roadmaps

Roadmaps are boards with type `roadmap`. This section documents the Roadmap model and the REST endpoints for public idea interactions and admin settings, organized similarly to boards.

## Base Path

```
/wp-json/fluent-boards/v2
```

## Roadmap Board Object

Roadmap boards use the same model as boards but are globally scoped to type `roadmap`.

### Properties

| Property | Type | Description |
|----------|------|-------------|
| `id` | integer | Roadmap board ID |
| `title` | string | Roadmap title |
| `type` | string | Always `roadmap` |
| `background` | object | Background config |
| `settings` | object | Board settings (serialized) |
| `created_by` | integer | Creator user ID |
| `stages` | array | Non-archived stages ordered by `position` |
| `meta` | object | Key-value metadata |

### Stage Visibility (Public States)

Roadmap boards can expose public stages. A simplified public state item:

```json
{ "id": 10, "slug": "planned", "label": "Planned", "stage_type": "planned" }
```


## List Ideas in a Stage

Parameters:
- `stage_id`: a numeric stage ID or the literal `all-ideas` to fetch ideas from all public stages.


**HTTP Request**
```
GET /wp-json/fluent-boards/v2/roadmaps/{board_id}/stages/{stage_id}/ideas
```

**Example Response (stage_id is numeric)**
```json
{
  "ideas": {
    "current_page": 1,
    "data": [
      {
        "id": 300,
        "board_id": 13,
        "title": "Example Idea",
        "type": "roadmap",
        "status": "open",
        "stage_id": 118,
        "author": { "name": "John Doe", "user_id": 1 },
        "isVoted": false,
        "vote_count": 0
      }
    ],
    "per_page": 20,
    "total": 2
  }
}
```

**Example Response (stage_id = all-ideas)**
```json
{
  "ideas": [ { "id": 202, "title": "Idea across public stages", "status": "open" } ]
}
```

## Create Idea

**HTTP Request**
```
POST /wp-json/fluent-boards/v2/roadmaps/{board_id}/ideas
```

**Request Body**

| Field | Type | Required | Description |
|------|------|----------|-------------|
| `idea[title]` | string | Yes | Idea title (max 192 chars) |
| `idea[description]` | string | Yes | Idea description (HTML allowed if authenticated) |
| `idea[author][name]` | string | Cond. | Required if unauthenticated |
| `idea[author][email]` | string | Cond. | Required if unauthenticated |

**Example Request**
```json
{
  "idea": {
    "title": "New Idea",
    "description": "Short description.",
    "author": { "name": "John Doe", "email": "john@example.com" }
  }
}
```

**Example Response**
```json
{
  "idea": { "id": 300, "title": "New Idea", "stage_id": 10, "type": "roadmap" },
  "message": "Idea has been created",
  "confirmation_text": "Thank you for your idea. Once it's reviewed, approved for planning by our team, we will notify you via email."
}
```

## Get Idea

**HTTP Request**
```
GET /wp-json/fluent-boards/v2/roadmaps/{board_id}/ideas/{task_id}
```

**Example Response**
```json
{
  "idea": {
    "id": 999,
    "board_id": 1,
    "title": "Example Idea",
    "slug": "example-idea",
    "type": "roadmap",
    "status": "open",
    "stage_id": 10,
    "stage": {
      "id": 10,
      "title": "Pending",
      "settings": { "is_public": false, "default_task_status": "open", "is_template": false }
    },
    "author": { "name": "John Doe", "avatar": "https://example.com/avatar.png", "user_id": 1 },
    "isVoted": false,
    "vote_count": 0,
    "comments_count": 0,
    "public_comments": [],
    "edit_link": "https://example.com/projects#/boards/1/tasks/999-example-idea"
  }
}
```

Notes:
- Comment sensitive fields (`author_email`, `author_ip`) are hidden.
- `badget` is set to `author` when the commenter is the idea author, or `admin` when the commenter has admin capability.


## Add Comment

**HTTP Request**
```
POST /wp-json/fluent-boards/v2/roadmaps/{board_id}/ideas/{idea_id}/comments
```

**Request Body**

| Field | Type | Required | Description |
|------|------|----------|-------------|
| `comment[message]` | string | Yes | Comment text (min 10 chars) |
| `comment[author][author_name]` | string | Conditional | Required if unauthenticated |
| `comment[author][author_email]` | string | Conditional | Required if unauthenticated |

**Example Request**
```json
{
  "comment": {
    "message": "Great idea! This would help a lot.",
    "author": { "author_name": "Jane Doe", "author_email": "jane@example.com" }
  }
}
```

**Example (form fields)**
```
comment[message]: Lorem Ipsum
comment[author][author_name]: Jane Doe
comment[author][author_email]: jane@example.com
```

**Example Response **
```json
{
  "message": "Your comment has been added",
  "comment": {
    "id": 10,
    "created_by": 1,
    "board_id": { "ref": "{board_id}" },
    "task_id": { "ref": "{idea_id}" },
    "type": "comment",
    "privacy": "public",
    "status": "published",
    "description": "<p>Lorem Ipsum</p>\n",
    "author_ip": "150.228.135.29",
    "author_email": "jane@example.com",
    "author_name": "Jane Doe",
    "avatar": "https://secure.gravatar.com/avatar/{hash}?s=128&d=mm&r=g",
    "created_at": "2025-08-12T03:46:14+00:00",
    "updated_at": "2025-08-12T03:46:14+00:00",
    "task": {
      "id": { "ref": "{idea_id}" },
      "board_id": { "ref": "{board_id}" },
      "title": "New task",
      "slug": "new-task",
      "type": "roadmap",
      "status": "open",
      "stage_id": 119,
      "created_by": 1,
      "comments_count": 2,
      "settings": {
        "integration_type": "feature",
        "author": { "email": "jane@example.com" }
      },
      "created_at": "2025-08-11T06:42:19+00:00",
      "updated_at": "2025-08-12T03:46:14+00:00",
      "meta": { "comments_count": "2" }
    }
  }
}
```

Notes:
- If authenticated, author info is taken from the current user; omit `author` fields.
- Message is sanitized and wrapped in paragraphs.
- If enabled in settings, the commenter may be added/updated in CRM.

## Delete Comment

**HTTP Request**
```
DELETE /wp-json/fluent-boards/v2/roadmaps/idea/comments/{comment_id}
```

**Path Parameters**
- `comment_id` (integer): The comment ID to delete.

**Example Response**
```json
{
  "message": "Comment has been deleted successfully"
}
```

## Vote Idea

Toggles an upvote for the current actor.

**HTTP Request**
```
POST /wp-json/fluent-boards/v2/roadmaps/vote-idea/{idea_id}
```

**Path Parameters**
- `idea_id` (integer): The idea ID to vote/unvote.

**Request Body**
- None

**Example Response (vote added)**
```json
{
  "isVoted": true,
  "new_count": 5
}
```

**Example Response (vote removed)**
```json
{
  "isVoted": false,
  "new_count": 4
}
```

## Day-wise Ideas

Returns counts of ideas created per day for a board. Requires board permission.

**HTTP Request**
```
GET /wp-json/fluent-boards/v2/roadmaps/{board_id}/day-wise-ideas
```

**Path Parameters**
- `board_id` (integer): Roadmap board ID.

**Example Response**
```json
{
  "dayWiseTasks": [
    { "date": "2025-08-10", "total": 3 },
    { "date": "2025-08-11", "total": 7 },
    { "date": "2025-08-12", "total": 2 }
  ]
}
```

## Popular Ideas

Returns ideas for a board with a computed `popular` count. Requires board permission.

**HTTP Request**
```
GET /wp-json/fluent-boards/v2/roadmaps/{board_id}/popular-ideas
```

**Path Parameters**
- `board_id` (integer): Roadmap board ID.

**Example Response**
```json
{
  "ideas": [
    { "id": 301, "title": "New task", "type": "roadmap", "popular": 12 },
    { "id": 302, "title": "Another idea", "type": "roadmap", "popular": 5 }
  ]
}
```

## Change Idea Stage

Updates an idea's stage. Requires board permission.

**HTTP Request**
```
POST /wp-json/fluent-boards/v2/roadmaps/{board_id}/idea/{idea_id}/change-stage
```

**Path Parameters**
- `board_id` (integer): Roadmap board ID
- `idea_id` (integer): Idea ID

**Request Body**

| Field | Type | Required | Description |
|------|------|----------|-------------|
| `stage_id` | integer | Yes | Target stage ID |

**Example Request**
```json
{ "stage_id": 119 }
```

**Example Response**
```json
{
  "idea": {
    "id": { "ref": "{idea_id}" },
    "board_id": { "ref": "{board_id}" },
    "stage_id": 119,
    "stage": { "id": 119, "title": "In Progress" }
  },
  "message": "Idea stage has been changed"
}
```

## Admin Endpoints

Require admin permissions.

- GET `/admin/roadmap/settings`
- POST `/admin/roadmap/settings`
- GET `/admin/roadmap/page-settings`
- POST `/admin/roadmap/page-settings`

## Get Settings

**HTTP Request**
```
GET /wp-json/fluent-boards/v2/admin/roadmap/settings
```

**Example Response**
```json
{ "settings": { "enabled": true } }
```

## Update Settings

**HTTP Request**
```
POST /wp-json/fluent-boards/v2/admin/roadmap/settings
```

**Example Request**
```json
{
  "settings": {
    "enable_new_idea_submission": "yes",
    "new_idea_require_auth": "no",
    "enable_new_comment_submission": "yes",
    "new_idea_comment_require_auth": "no",
    "enable_new_vote_submission": "yes",
    "new_idea_vote_require_auth": "no"
  }
}
```

**Example Response**
```json
{
  "message": "Settings has been updated successfully",
  "settings": { /* updated settings */ }
}
```

## Get/Update Page Settings

## Error Responses

See [Common Error Responses](/rest-api/shared/error-responses) for standard error formats.

### Common Roadmap-Specific Errors

- 404 Not Found - Roadmap board or idea not found
- 403 Forbidden - You don't have permission for this action
- 400 Bad Request - Invalid data or missing required fields

## Next Steps

- Boards - Manage roadmap board metadata and members
- Tasks - Manage idea tasks (internal)

**HTTP Requests**
```
GET  /wp-json/fluent-boards/v2/admin/roadmap/page-settings
POST /wp-json/fluent-boards/v2/admin/roadmap/page-settings
```

**Update Example Request**
```json
{
  "selectedPages": {
    "{roadmap_id}": 123
  }
}
```

**Example Response**
```json
{
  "message": "Roadmap Board & Page Mapping Updated Successfully",
  "page_settings": [ { "roadmap_id": 1, "page_id": 123 } ]
}
```

Notes:
- Roadmap boards are filtered at the model level to `type = roadmap`.
- Use placeholders `{board_id}`, `{stage_id}`, `{task_id}`, `{idea_id}`, `{comment_id}`.

---

## Settings API
Source file : `src/rest-api/settings.md`

# Settings API

> **Note:** This documentation is under development. The Settings API provides endpoints for managing platform settings and configuration.

## Overview

The Settings API provides endpoints for managing Fluent Boards platform settings, user preferences, and system configuration.

## Base Endpoint

```
/fluent-boards/v2/settings
```

## Available Endpoints

### Get Settings
- **GET** `/settings`
- **GET** `/settings/{setting_group}`

### Update Settings
- **PUT** `/settings`
- **PUT** `/settings/{setting_group}`

### Reset Settings
- **POST** `/settings/reset`

### Export Settings
- **GET** `/settings/export`

### Import Settings
- **POST** `/settings/import`

## Setting Groups

### General Settings
- `general` - General platform settings
- `appearance` - UI and appearance settings
- `notifications` - Notification preferences
- `security` - Security and privacy settings

### Project Settings
- `projects` - Default board settings
- `tasks` - Default task settings
- `stages` - Default stage settings
- `labels` - Label configuration

### Integration Settings
- `integrations` - Third-party integrations
- `webhooks` - Webhook configuration
- `api` - API settings and limits

## Settings Object

```json
{
  "general": {
    "site_name": "Fluent Boards",
    "timezone": "UTC",
    "date_format": "Y-m-d",
    "time_format": "H:i:s",
    "language": "en"
  },
  "appearance": {
    "theme": "light",
    "primary_color": "#7742e6",
    "sidebar_collapsed": false,
    "compact_mode": false
  },
  "notifications": {
    "email_notifications": true,
    "push_notifications": true,
    "task_assignments": true,
    "project_updates": true,
    "due_date_reminders": true
  },
  "security": {
    "session_timeout": 3600,
    "password_policy": "strong",
    "two_factor_auth": false,
    "ip_whitelist": []
  }
}
```

## Features

- Hierarchical settings
- Setting validation
- Import/export functionality
- Setting inheritance
- User-specific overrides
- Setting history

---

*This documentation will be expanded with detailed examples and complete API reference.*

---

## Base Endpoint
Source file : `src/rest-api/shared\base-endpoint.md`

# Base Endpoint

All API requests for this resource should be made to:

```
/fluent-boards/v2/{resource}
```

**Base URL:** `https://yourdomain.com/wp-json/fluent-boards/v2/{resource}`

**Authentication:** All endpoints require Basic Authentication with WordPress credentials

**Content-Type:** `application/json` for POST/PUT requests

---

## Shared  /  Development Note
Source file : `src/rest-api/shared\development-note.md`

> **Note:** This documentation is under development. The API endpoints and features described here are subject to change as the Fluent Boards platform evolves.

## Overview

This API provides endpoints for managing [RESOURCE_NAME] in Fluent Boards.

## Base Endpoint

```
/fluent-boards/v2/[RESOURCE_PATH]
```

## Available Endpoints

[ENDPOINT_LIST]

## Features

[FEATURE_LIST]

---

*This documentation will be expanded with detailed examples and complete API reference.*

---

## Common Error Responses
Source file : `src/rest-api/shared\error-responses.md`

# Common Error Responses

All Fluent Boards API endpoints may return the following standard error responses:

## 400 Bad Request

```json
{
  "code": "rest_invalid_param",
  "message": "Invalid parameter: title is required",
  "data": {
    "status": 400
  }
}
```

## 401 Unauthorized

```json
{
  "code": "rest_unauthorized",
  "message": "Authentication required",
  "data": {
    "status": 401
  }
}
```

## 403 Forbidden

```json
{
  "code": "rest_forbidden",
  "message": "You don't have permission to access this resource",
  "data": {
    "status": 403
  }
}
```

## 404 Not Found

```json
{
  "code": "rest_not_found",
  "message": "Resource not found",
  "data": {
    "status": 404
  }
}
```

## 422 Validation Error

```json
{
  "code": "rest_invalid_param",
  "message": "Validation failed",
  "data": {
    "status": 422,
    "params": {
      "title": "Title is required"
    }
  }
}
```

## 500 Internal Server Error

```json
{
  "code": "rest_server_error",
  "message": "Internal server error",
  "data": {
    "status": 500
  }
}
```

## Error Response Format

All error responses follow this structure:

| Field | Type | Description |
|-------|------|-------------|
| `code` | string | Error code identifier |
| `message` | string | Human-readable error message |
| `data.status` | integer | HTTP status code |
| `data.params` | object | Validation errors (422 only) |

## Common Error Codes

- `rest_invalid_param` - Invalid or missing parameters
- `rest_unauthorized` - Authentication required
- `rest_forbidden` - Insufficient permissions
- `rest_not_found` - Resource not found
- `rest_server_error` - Internal server error

---

## Shared  /  Next Steps
Source file : `src/rest-api/shared\next-steps.md`

## Next Steps

- [Manage Boards](/rest-api/boards) - Work with board management
- [Handle Tasks](/rest-api/tasks) - Manage tasks and assignments
- [Organize Stages](/rest-api/stages) - Manage project workflows
- [User Management](/rest-api/users) - Handle team members and permissions
- [Labels](/rest-api/labels) - Organize tasks with labels
- [Time Tracking](/rest-api/time-tracking) - Track time on tasks
- [Webhooks](/rest-api/webhooks) - Set up integrations and automation

---

## Shared  /  Pro Feature Note
Source file : `src/rest-api/shared\pro-feature-note.md`

> **Note:** This is a Pro feature. The [FEATURE_NAME] API allows you to [FEATURE_DESCRIPTION].

## Overview

The [FEATURE_NAME] API provides endpoints for [FEATURE_OVERVIEW] in Fluent Boards Pro.

## Base Endpoint

```
/fluent-boards/v2/[RESOURCE_PATH]
```

## Available Endpoints

[ENDPOINT_LIST]

## Features

[FEATURE_LIST]

---

*This documentation will be expanded with detailed examples and complete API reference.*

---

## Stages
Source file : `src/rest-api/stages.md`

# Stages

The Stages API allows you to manage board stages and workflows in Fluent Boards. You can create, read, update, and delete stages, as well as manage their tasks and positions.

## Create a Stage

Create a new stage. The stage will be positioned at the end of the board by default, or at the specified position if provided.

**HTTP Request**
```
POST /wp-json/fluent-boards/v2/projects/{board_id}/stage-create
```

### Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `title` | string | Yes | Stage title |
| `position` | numeric | No | Position within the board |
| `status` | string | No | Default task status (defaults to 'open') |

### Example Request

```bash
curl "https://yourdomain.com/wp-json/fluent-boards/v2/projects/{board_id}/stage-create" \
  -X POST \
  -H "Authorization: Basic API_USERNAME:API_PASSWORD" \
  -H "Content-Type: application/json" \
  -d '{
    "title": "Review",
    "position": 3,
    "status": "open"
  }'
```


### Example Response

```json
{
  "updatedStages": [
    {
      "id": 107,
      "board_id": "10",
      "title": "Review",
      "slug": null,
      "type": "stage",
      "position": "2.50",
      "color": null,
      "bg_color": null,
      "settings": {
        "default_task_status": "open",
        "default_task_assignees": []
      },
      "archived_at": null,
      "created_at": "2025-08-06T10:45:32+00:00",
      "updated_at": "2025-08-06T10:45:32+00:00"
    }
  ],
  "message": "stage has been created"
}
```

## Update a Stage

Update an existing stage.

**HTTP Request**
```
PUT /wp-json/fluent-boards/v2/projects/{board_id}/update-stage/{stage_id}
```

### Parameters
### Example Request

```bash
curl "https://yourdomain.com/wp-json/fluent-boards/v2/projects/{board_id}/update-stage/{stage_id}" \
  -X PUT \
  -H "Authorization: Basic API_USERNAME:API_PASSWORD" \
  -H "Content-Type: application/json" \
  -d '{
    "title": "In Development",
    "settings": {"default_task_status": "open"}
  }'
```

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `title` | string | No | Stage title |
| `settings` | object | No | Stage settings object |


### Example Response

```json
{
  "data": {
    "id": 2,
    "title": "In Development",
    "board_id": 1,
    "position": 2.0,
    "type": "stage",
    "settings": {
      "default_task_status": "open",
      "is_template": false
    },
    "archived_at": null,
    "created_by": 1,
    "created_at": "2023-01-15 10:30:00",
    "updated_at": "2023-02-15 16:00:00"
  },
  "message": "Stage updated successfully"
}
```

## Archive a Stage

Archive a stage (soft delete).

**HTTP Request**
```
PUT /wp-json/fluent-boards/v2/projects/{board_id}/archive-stage/{stage_id}
```

### Example Request

```bash
curl "https://yourdomain.com/wp-json/fluent-boards/v2/projects/{board_id}/archive-stage/{stage_id}" \
  -X PUT \
  -H "Authorization: Basic API_USERNAME:API_PASSWORD"
```

### Example Response

```json
{
  "updatedStage": {
    "id": 107,
    "board_id": "10",
    "title": "Review",
    "slug": null,
    "type": "stage",
    "position": 0,
    "color": null,
    "bg_color": null,
    "settings": {
      "default_task_status": "open",
      "default_task_assignees": []
    },
    "archived_at": "2025-08-06 11:18:56",
    "created_at": "2025-08-06T10:45:32+00:00",
    "updated_at": "2025-08-06T11:18:56+00:00"
  },
  "message": "Stage has been archived"
}
```

## Restore a Stage

Restore an archived stage.

**HTTP Request**
```
PUT /wp-json/fluent-boards/v2/projects/{board_id}/restore-stage/{stage_id}
```

### Example Request

```bash
curl "https://yourdomain.com/wp-json/fluent-boards/v2/projects/{board_id}/restore-stage/{stage_id}" \
  -X PUT \
  -H "Authorization: Basic API_USERNAME:API_PASSWORD"
```

### Example Response

```json
{
  "success": true,
  "updatedStage": {
    "id": 107,
    "board_id": "10",
    "title": "Review",
    "slug": null,
    "type": "stage",
    "position": 4,
    "color": null,
    "bg_color": null,
    "settings": {
      "default_task_status": "open",
      "default_task_assignees": []
    },
    "archived_at": null,
    "created_at": "2025-08-06T10:45:32+00:00",
    "updated_at": "2025-08-06T11:21:13+00:00"
  },
  "message": "Stage has been restored"
}
```

## Re-position Stages

Update the positions of multiple stages at once. This endpoint can trigger automatic reindexing of stage positions for optimal ordering.

**HTTP Request**
```
PUT /wp-json/fluent-boards/v2/projects/{board_id}/re-position-stages
```

### Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `list` | array | Yes | Array of stage IDs in the desired order |

### Example Request

```bash
curl "https://yourdomain.com/wp-json/fluent-boards/v2/projects/{board_id}/re-position-stages" \
  -X PUT \
  -H "Authorization: Basic API_USERNAME:API_PASSWORD" \
  -H "Content-Type: application/json" \
  -d '{
    "list": [107, 106, 105, 104]
  }'
```

### Example Response

```json
{
  "message": "Stages Reordered",
  "updatedStages": [
    {
      "id": 104,
      "board_id": "10",
      "title": "Open",
      "slug": "open",
      "type": "stage",
      "position": "1.88",
      "color": null,
      "bg_color": null,
      "settings": {
        "default_task_status": "open"
      },
      "archived_at": null,
      "created_at": "2025-08-06T06:46:17+00:00",
      "updated_at": "2025-08-06T11:31:45+00:00"
    },
    {
      "id": 105,
      "board_id": "10",
      "title": "In Progress",
      "slug": "in-progress",
      "type": "stage",
      "position": "0.88",
      "color": null,
      "bg_color": null,
      "settings": {
        "default_task_status": "open"
      },
      "archived_at": null,
      "created_at": "2025-08-06T06:46:17+00:00",
      "updated_at": "2025-08-06T11:31:45+00:00"
    },
    // ... other stages
  ]
}
```

## Archive All Tasks in Stage

Archive all tasks within a specific stage. This will set the position to 0 and mark all tasks as archived with a timestamp.

**HTTP Request**
```
PUT /wp-json/fluent-boards/v2/projects/{board_id}/stage/{stage_id}/archive-all-task
```

### Example Request

```bash
curl "https://yourdomain.com/wp-json/fluent-boards/v2/projects/{board_id}/stage/{stage_id}/archive-all-task" \
  -X PUT \
  -H "Authorization: Basic API_USERNAME:API_PASSWORD"
```
### Example Response

```json
{
  "message": "Tasks have been archived",
  "updatedTasks": [
    {
      "id": 282,
      "parent_id": null,
      "board_id": "9",
      "crm_contact_id": null,
      "title": "New task",
      "slug": "new-task",
      "type": "task",
      "position": 0,
      "archived_at": "2025-08-06 11:36:48",
      // ... other task properties
    }
    // ... other updated tasks
  ]
}
```

## Sort Tasks in Stage

Sort tasks within a specific stage by various criteria. The system will automatically update task positions based on the sort order and return the sorted tasks with additional computed properties.

**HTTP Request**
```
PUT /wp-json/fluent-boards/v2/projects/{board_id}/stage/{stage_id}/sort-task
```

### Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `order` | string | Yes | Sort field (priority, due_at, position, created_at, title) |
| `orderBy` | string | Yes | Sort direction (ASC, DESC) |


### Example Request

```bash
curl "https://yourdomain.com/wp-json/fluent-boards/v2/projects/{board_id}/stage/{stage_id}/sort-task" \
  -X PUT \
  -H "Authorization: Basic API_USERNAME:API_PASSWORD" \
  -H "Content-Type: application/json" \
  -d '{
    "order": "title",
    "orderBy": "DESC"
  }'
```

### Example Response

```json
{
  "message": "Tasks has been sorted",
  "updatedTasks": [
    {
      "id": 248,
      "title": "Code REfacotor , Security Validation Checks",
      "stage_id": "78",
      "position": 1,
      "isOverdue": false,
      "isUpcoming": false,
      "is_watching": false
      // ... other task properties
    },
    // ... other tasks
  ]
}
```

## Get Archived Stages

Retrieve archived stages for a board. Supports pagination and can return all archived stages or paginated results.

**HTTP Request**
```
GET /wp-json/fluent-boards/v2/projects/{board_id}/archived-stages
```

### Parameters
### Example Request

```bash
curl "https://yourdomain.com/wp-json/fluent-boards/v2/projects/{board_id}/archived-stages?per_page=30&page=1" \
  -H "Authorization: Basic API_USERNAME:API_PASSWORD"
```

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `noPagination` | boolean | false | If true, returns all archived stages without pagination |
| `per_page` | integer | 30 | Number of stages per page (when pagination is enabled) |
| `page` | integer | 1 | Page number (when pagination is enabled) |

### Example Response

```json
{
  "stages": {
    "current_page": 1,
    "data": [
      {
        "id": 5,
        "board_id": "1",
        "title": "Old Stage",
        "slug": "old-stage",
        "type": "stage",
        "position": "0.00",
        "color": null,
        "bg_color": null,
        "settings": {
          "default_task_status": "open"
        },
        "archived_at": "2023-02-10 12:00:00",
        "created_at": "2023-01-15T10:30:00+00:00",
        "updated_at": "2023-02-10T12:00:00+00:00"
      }
    ],
    "from": 1,
    "to": 1,
    "total": 1,
    "per_page": 30,
    "current_page": 1,
    "last_page": 1,
    "first_page_url": "https://yourdomain.com/wp-json/fluent-boards/v2/projects/1/archived-stages/?page=1",
    "last_page_url": "https://yourdomain.com/wp-json/fluent-boards/v2/projects/1/archived-stages/?page=1",
    "next_page_url": null,
    "prev_page_url": null,
    "path": "https://yourdomain.com/wp-json/fluent-boards/v2/projects/1/archived-stages",
    "links": [
      {
        "url": null,
        "label": "pagination.previous",
        "active": false
      },
      {
        "url": "https://yourdomain.com/wp-json/fluent-boards/v2/projects/1/archived-stages/?page=1",
        "label": "1",
        "active": true
      },
      {
        "url": null,
        "label": "pagination.next",
        "active": false
      }
    ]
  }
}
```

## Get Stage Task Available Positions

Get available positions for tasks within a stage.

**HTTP Request**
```
GET /wp-json/fluent-boards/v2/projects/{board_id}/stage-task-available-positions/{stage_id}
```

### Example Request

```bash
curl "https://yourdomain.com/wp-json/fluent-boards/v2/projects/{board_id}/stage-task-available-positions/{stage_id}" \
  -H "Authorization: Basic API_USERNAME:API_PASSWORD"
```
### Example Response

```json
{
  "data": {
    "stage_id": 2,
    "available_positions": [1, 2, 3, 4, 5],
    "current_task_count": 3
  }
}
```

## Error Responses

See [Common Error Responses](/rest-api/shared/error-responses) for standard error formats.

### Common Stage-Specific Errors

- **404 Not Found** - Stage not found
- **403 Forbidden** - You don't have permission to access this stage
- **400 Bad Request** - Invalid stage data or missing required fields

---

## Subtasks
Source file : `src/rest-api/subtasks.md`

# Subtasks

The Subtasks API allows you to manage subtasks within main tasks in Fluent Boards. Subtasks are regular tasks with a `parent_id` field that references their parent task, organized in groups for better organization.

## Base Endpoint

```
/fluent-boards/v2/projects/{board_id}/tasks/{task_id}/subtasks
```


```json
{
  "id": 123,
  "parent_id": "456",
  "board_id": "3",
  "crm_contact_id": null,
  "title": "Create wireframes",
  "slug": "create-wireframes",
  "type": "task",
  "status": "closed",
  "stage_id": "25",
  "source": "web",
  "source_id": null,
  "priority": "low",
  "description": "Design wireframes for the new feature",
  "lead_value": "0.00",
  "created_by": "1",
  "position": "1.00",
  "comments_count": "0",
  "issue_number": null,
  "reminder_type": "none",
  "settings": {
    "cover": {
      "backgroundColor": null
    },
    "subtask_count": null
  },
  "remind_at": null,
  "started_at": null,
  "due_at": null,
  "last_completed_at": "2024-01-15 08:01:43",
  "archived_at": null,
  "created_at": "2024-01-15T08:43:52+00:00",
  "updated_at": "2024-01-15T08:01:43+00:00",
  "meta": {
    "subtask_group_id": "127"
  },
  "repeat_task_meta": null,
  "assignees": []
}
```

### List Subtasks

Retrieve all subtasks for a parent task, organized by groups.

**HTTP Request**
```
GET /wp-json/fluent-boards/v2/projects/{board_id}/tasks/{task_id}/subtasks
```

### Example Request

```bash
curl "https://yourdomain.com/wp-json/fluent-boards/v2/projects/{board_id}/tasks/{task_id}/subtasks" \
  -H "Authorization: Basic API_USERNAME:API_PASSWORD"
```

### Example Response

```json
{
  "subtaskGroups": [
    {
      "id": 127,
      "task_id": 456,
      "subtasks": [
        {
          "id": 123,
          "parent_id": "456",
          "board_id": "3",
          "crm_contact_id": null,
          "title": "Create wireframes",
          "slug": "create-wireframes",
          "type": "task",
          "status": "closed",
          "stage_id": "25",
          "source": "web",
          "source_id": null,
          "priority": "low",
          "description": "Design wireframes for the new feature",
          "lead_value": "0.00",
          "created_by": "1",
          "position": "1.00",
          "comments_count": "0",
          "issue_number": null,
          "reminder_type": "none",
          "settings": {
            "cover": {
              "backgroundColor": null
            },
            "subtask_count": null
          },
          "remind_at": null,
          "started_at": null,
          "due_at": null,
          "last_completed_at": "2024-01-15 08:01:43",
          "archived_at": null,
          "created_at": "2024-01-15T08:43:52+00:00",
          "updated_at": "2024-01-15T08:01:43+00:00",
          "meta": {
            "subtask_group_id": "127"
          },
          "repeat_task_meta": null,
          "assignees": []
        }
      ],
      "value": "Design Phase"
    }
  ]
}
```

## Create a Subtask

Create a new subtask within a parent task.

**HTTP Request**
```
POST /wp-json/fluent-boards/v2/projects/{board_id}/tasks/{task_id}/subtasks
```

### Example Request

```bash
curl -X POST "https://yourdomain.com/wp-json/fluent-boards/v2/projects/{board_id}/tasks/{task_id}/subtasks" \
  -H "Authorization: Basic API_USERNAME:API_PASSWORD" \
  -H "Content-Type: application/json" \
  -d '{
    "title": "The new subtask",
    "group_id": 127,
    "due_at": null,
    "add_to_top": false
  }'
```

### Request Body

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `title` | string | Yes | Title of the subtask |
| `group_id` | int | Yes | ID of the subtask group |
| `due_at` | string or null | No | Due date-time in ISO 8601 format or null |
| `add_to_top` | boolean | No | If true, adds the subtask at the top of the group (default: false) |

### Example Response

```json
{
  "subtask": {
    "parent_id": 85,
    "title": "The new subtask",
    "board_id": "3",
    "status": "open",
    "priority": "low",
    "due_at": null,
    "position": 20,
    "created_by": 1,
    "type": "task",
    "slug": "the-new-subtask",
    "settings": {
      "cover": {
        "backgroundColor": ""
      },
      "subtask_count": 0,
      "attachment_count": 0,
      "subtask_completed_count": 0
    },
    "updated_at": "2025-08-08T04:12:47+00:00",
    "created_at": "2025-08-08T04:12:47+00:00",
    "id": 284,
    "assignees": [],
    "meta": {
      "subtask_group_id": "127"
    },
    "repeat_task_meta": null
  },
  "message": "Subtask has been added"
}
```

## Create a Subtask Group

Create a new group to organize subtasks.

**HTTP Request**
```
POST /wp-json/fluent-boards/v2/projects/{board_id}/tasks/{task_id}/subtask-group
```

### Example Request

```bash
curl -X POST "https://yourdomain.com/wp-json/fluent-boards/v2/projects/{board_id}/tasks/{task_id}/subtask-group" \
  -H "Authorization: Basic API_USERNAME:API_PASSWORD" \
  -H "Content-Type: application/json" \
  -d '{
    "title": "Design Phase"
  }'
```

### Request Body

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `title` | string | Yes | Name of the subtask group |

### Example Response

```json
{
  "subtaskGroup": {
    "id": 555,
    "task_id": 85,
    "key": "group_name",
    "value": "Design Phase",
    "created_at": "2025-08-08T04:12:47+00:00",
    "updated_at": "2025-08-08T04:12:47+00:00"
  },
  "message": "New Subtask group has been added"
}
```

## Update a Subtask Group

Update the title of a subtask group.

**HTTP Request**
```
PUT /wp-json/fluent-boards/v2/projects/{board_id}/tasks/{task_id}/subtask-group
```

### Example Request

```bash
curl -X PUT "https://yourdomain.com/wp-json/fluent-boards/v2/projects/{board_id}/tasks/{task_id}/subtask-group" \
  -H "Authorization: Basic API_USERNAME:API_PASSWORD" \
  -H "Content-Type: application/json" \
  -d '{
    "group_id": 555,
    "title": "Execution Phase"
  }'
```

### Request Body

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `title` | string | Yes | New title for the group |
| `group_id` | int | Yes | ID of the group to update |

### Example Response

```json
{
  "subtaskGroup": {
    "id": 555,
    "task_id": 85,
    "key": "group_name",
    "value": "Execution Phase",
    "created_at": "2025-08-08T04:12:47+00:00",
    "updated_at": "2025-08-08T05:10:12+00:00"
  },
  "message": "Subtask group title has been added"
}
```

## Delete a Subtask Group

Delete a subtask group and its subtasks.

**HTTP Request**
```
DELETE /wp-json/fluent-boards/v2/projects/{board_id}/tasks/{task_id}/subtask-group
```

### Example Request

```bash
curl -X DELETE "https://yourdomain.com/wp-json/fluent-boards/v2/projects/{board_id}/tasks/{task_id}/subtask-group" \
  -H "Authorization: Basic API_USERNAME:API_PASSWORD" \
  -H "Content-Type: application/json" \
  -d '{
    "group_id": 555
  }'
```

### Request Body

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `group_id` | int | Yes | ID of the group to delete |

### Example Response

```json
{
  "message": "Subtask group has been deleted"
}
```

## Delete a Subtask

Delete a subtask.

**HTTP Request**
```
DELETE /wp-json/fluent-boards/v2/projects/{board_id}/tasks/{task_id}/delete-subtask
```

**Note:** `task_id` in the path is the subtask ID to delete. No request body is required.

### Example Request

```bash
curl -X DELETE "https://yourdomain.com/wp-json/fluent-boards/v2/projects/{board_id}/tasks/{task_id}/delete-subtask" \
  -H "Authorization: Basic API_USERNAME:API_PASSWORD"
```

### Example Response

```json
{
  "deletedSubtask": {
    "id": 284,
    "parent_id": "85",
    "board_id": "3",
    "crm_contact_id": null,
    "title": "The new subtask",
    "slug": "the-new-subtask",
    "type": "task",
    "status": "open",
    "stage_id": null,
    "source": "web",
    "source_id": null,
    "priority": "low",
    "description": null,
    "lead_value": "0.00",
    "created_by": "1",
    "position": "20.00",
    "comments_count": "0",
    "issue_number": null,
    "reminder_type": "none",
    "settings": {
      "cover": {
        "backgroundColor": ""
      },
      "subtask_count": 0,
      "attachment_count": 0,
      "subtask_completed_count": 0
    },
    "remind_at": null,
    "started_at": null,
    "due_at": null,
    "last_completed_at": null,
    "archived_at": null,
    "created_at": "2025-08-08T04:12:47+00:00",
    "updated_at": "2025-08-08T04:12:47+00:00",
    "subtask_group_id": "127",
    "meta": [],
    "repeat_task_meta": null
  },
  "changedSubtasks": [],
  "message": "Task has been deleted"
}
```

## Move Subtask to Group

Move a subtask from one group to another.

**HTTP Request**
```
POST /wp-json/fluent-boards/v2/projects/{board_id}/tasks/{task_id}/move-subtask
```

### Example Request

```bash
curl -X POST "https://yourdomain.com/wp-json/fluent-boards/v2/projects/{board_id}/tasks/{task_id}/move-subtask" \
  -H "Authorization: Basic API_USERNAME:API_PASSWORD" \
  -H "Content-Type: application/json" \
  -d '{
    "group_id": 127,
    "subtask_id": 284
  }'
```

### Request Body

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `group_id` | int | Yes | Target group ID |
| `subtask_id` | int or int[] | Yes | ID of the subtask to move (or an array of IDs) |

### Example Response

```json
{
  "subtask": {
    "id": 284,
    "parent_id": 85,
    "position": 21,
    "assignees": []
  },
  "message": "Subtask has been moved"
}
```

## Update Subtask Position

Move a subtask within its current group or to another group and update its position.

**HTTP Request**
```
PUT /wp-json/fluent-boards/v2/projects/{board_id}/tasks/update-subtask-position/{subtask_id}
```

**Note:** `{subtask_id}` is the subtask being repositioned. If `newSubtasksGroupId` is omitted, the API infers the current group from the subtask meta.

### Example Request

```bash
curl -X PUT "https://yourdomain.com/wp-json/fluent-boards/v2/projects/{board_id}/tasks/update-subtask-position/{subtask_id}" \
  -H "Authorization: Basic API_USERNAME:API_PASSWORD" \
  -H "Content-Type: application/json" \
  -d '{
    "newPosition": 1,
    "newSubtasksGroupId": 198
  }'
```

### Request Body

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `newPosition` | int | Yes | New position in the group |
| `newSubtasksGroupId` | int | Yes | Group ID (can be same or different) |

### Behavior

- If `newPosition` is 1, the subtask is placed at the top; the API uses fractional positions under the hood and may reindex if needed.
- If `newSubtasksGroupId` differs from the current group, the subtask is moved to the new group and positioned there.
- Response includes `changedSubtasks`: subtasks under the same parent updated within the last minute (with `assignees`).

### Example Response

```json
{
  "changedSubtasks": [
    {
      "id": 285,
      "parent_id": "85",
      "board_id": "3",
      "crm_contact_id": null,
      "title": "Hello Subtask",
      "slug": "hello-subtask",
      "type": "task",
      "status": "open",
      "stage_id": null,
      "source": "web",
      "source_id": null,
      "priority": "low",
      "description": null,
      "lead_value": "0.00",
      "created_by": "1",
      "position": "1.00",
      "comments_count": "0",
      "issue_number": null,
      "reminder_type": "none",
      "settings": {
        "cover": {
          "backgroundColor": ""
        },
        "subtask_count": 0,
        "attachment_count": 0,
        "subtask_completed_count": 0
      },
      "remind_at": null,
      "started_at": null,
      "due_at": null,
      "last_completed_at": null,
      "archived_at": null,
      "created_at": "2025-08-08T04:49:24+00:00",
      "updated_at": "2025-08-08T04:49:28+00:00",
      "meta": {
        "subtask_group_id": "198"
      },
      "repeat_task_meta": null,
      "assignees": []
    }
  ]
}
```

## Convert Task to Subtask

Convert an existing task to a subtask.

**HTTP Request**
```
PUT /wp-json/fluent-boards/v2/projects/{board_id}/tasks/{task_id}/convert-to-subtask
```

### Example Request

```bash
curl -X PUT "https://yourdomain.com/wp-json/fluent-boards/v2/projects/{board_id}/tasks/{task_id}/convert-to-subtask" \
  -H "Authorization: Basic API_USERNAME:API_PASSWORD" \
  -H "Content-Type: application/json" \
  -d '{
    "parent_id": 133,
    "assigneeId": 1
  }'
```

### Request Body

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `parent_id` | int | Yes | ID of the parent task |
| `assigneeId` | int | No | User ID to assign |
| `subtaskGroupId` | int | No | Group ID to place the subtask |

### Behavior

- Sets the task's `parent_id` and clears `stage_id`.
- If `subtaskGroupId` is provided, links the new subtask to that group; otherwise a "Default Subtask Group" is created on the parent task and the subtask is added there.
- If `assigneeId` is provided, assigns the user to the new subtask.
- Removes existing notifications for the converted task.

### Example Response

```json
{
  "message": "Task has been converted to subtask",
  "parentTask": {
    "id": 133,
    "parent_id": null,
    "board_id": "3",
    "crm_contact_id": null,
    "title": "task activity check .",
    "slug": "task-activity-check",
    "type": "task",
    "status": "open",
    "stage_id": "26",
    "source": "web",
    "source_id": null,
    "priority": "low",
    "description": "",
    "lead_value": "0.00",
    "created_by": "1",
    "position": "0.50",
    "comments_count": "0",
    "issue_number": null,
    "reminder_type": "none",
    "settings": {
      "cover": {
        "backgroundColor": ""
      },
      "subtask_count": 0,
      "attachment_count": 0,
      "subtask_completed_count": 0
    },
    "remind_at": null,
    "started_at": null,
    "due_at": null,
    "last_completed_at": null,
    "archived_at": null,
    "created_at": "2024-12-24T08:43:53+00:00",
    "updated_at": "2025-01-28T03:15:14+00:00",
    "meta": {
      "is_template": "no",
      "group_name": "Default Subtask Group"
    },
    "repeat_task_meta": null,
    "watchers": []
  }
}
```

## Move Subtask to Board

Convert a subtask back to a regular task and move it to a specific stage.

**HTTP Request**
```
PUT /wp-json/fluent-boards/v2/projects/{board_id}/tasks/{task_id}/move-to-board
```

**Note:** `{task_id}` in this route refers to the subtask ID you are converting back to a regular task and moving to the specified stage.

### Example Request

```bash
curl -X PUT "https://yourdomain.com/wp-json/fluent-boards/v2/projects/{board_id}/tasks/{task_id}/move-to-board" \
  -H "Authorization: Basic API_USERNAME:API_PASSWORD" \
  -H "Content-Type: application/json" \
  -d '{
    "stage_id": 26
  }'
```

### Request Body

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `stage_id` | int | Yes | Stage ID where the task should be moved |

### Example Response

```json
{
  "moveSubtask": {
    "id": 283,
    "parent_id": null,
    "board_id": "3",
    "crm_contact_id": null,
    "title": "Design Homepage (Cloned)",
    "slug": "customizable-dashboard-view-settings",
    "type": "task",
    "status": "open",
    "stage_id": "26",
    "source": "web",
    "source_id": null,
    "priority": "low",
    "description": "<p>It will on a Kanban Page/Table view Page. </p>\n<ol>\n<li>Label</li>\n<li>Priority</li>\n<li>Due Date</li>\n<li> </li>\n</ol>",
    "lead_value": "0.00",
    "created_by": "1",
    "position": 0.25,
    "comments_count": "0",
    "issue_number": null,
    "reminder_type": "none",
    "settings": {
      "cover": {
        "backgroundColor": ""
      },
      "subtask_count": 0,
      "attachment_count": 0,
      "subtask_completed_count": 0
    },
    "remind_at": null,
    "started_at": null,
    "due_at": "2025-07-04 23:45:00",
    "last_completed_at": null,
    "archived_at": null,
    "created_at": "2025-08-06T10:00:02+00:00",
    "updated_at": "2025-08-08T04:56:17+00:00",
    "meta": {
      "is_template": "no"
    },
    "repeat_task_meta": null
  },
  "changedSubtasks": []
}
```

## Clone a Subtask

Create a copy of an existing subtask.

**HTTP Request**
```
POST /wp-json/fluent-boards/v2/projects/{board_id}/tasks/{task_id}/clone-subtask
```

**Note:** `{task_id}` in this route refers to the subtask ID you want to clone.

### Example Request

```bash
curl -X POST "https://yourdomain.com/wp-json/fluent-boards/v2/projects/{board_id}/tasks/{task_id}/clone-subtask" \
  -H "Authorization: Basic API_USERNAME:API_PASSWORD"
```

### Behavior

- Title is suffixed with ` (cloned)`
- Retains `started_at` and `due_at`
- Keeps the same subtask group membership
- Copies assignees and watchers
- Places the clone between the original and the next subtask by position, or at the end if none exists

### Example Response

```json
{
  "subtask": {
    "parent_id": "133",
    "board_id": "3",
    "crm_contact_id": null,
    "title": "Lorem ipsum (cloned)",
    "slug": "lorem-ipsum",
    "type": "task",
    "status": "open",
    "stage_id": null,
    "source": "web",
    "source_id": null,
    "priority": "low",
    "description": null,
    "lead_value": "0.00",
    "created_by": "1",
    "position": 2,
    "comments_count": "0",
    "issue_number": null,
    "reminder_type": "none",
    "settings": {
      "cover": {
        "backgroundColor": ""
      },
      "subtask_count": 0,
      "attachment_count": 0,
      "subtask_completed_count": 0
    },
    "remind_at": null,
    "started_at": null,
    "due_at": null,
    "last_completed_at": null,
    "archived_at": null,
    "updated_at": "2025-08-08T05:02:40+00:00",
    "created_at": "2025-08-08T05:02:40+00:00",
    "id": 287,
    "meta": {
      "subtask_group_id": "200"
    },
    "repeat_task_meta": null,
    "assignees": []
  },
  "message": "Subtask has been cloned successfully"
}
```

## Error Responses

See [Common Error Responses](/rest-api/shared/error-responses) for standard error formats.

### Common Subtask-Specific Errors

- **404 Not Found** - Subtask or parent task not found
- **403 Forbidden** - You don't have permission to access this subtask
- **400 Bad Request** - Invalid subtask data or missing required fields

---

## Tasks
Source file : `src/rest-api/tasks.md`

# Tasks

The Tasks API allows you to manage tasks within boards in Fluent Boards. You can create, read, update, and delete tasks, as well as manage their assignments, labels, and status.

## List All Tasks

Retrieve a paginated list of tasks.

**HTTP Request**
```
GET /wp-json/fluent-boards/v2/projects/{board_id}/tasks
```

### Example Request

```bash
curl "https://yourdomain.com/wp-json/fluent-boards/v2/projects/{board_id}/tasks" \
  -H "Authorization: Basic API_USERNAME:API_PASSWORD"
```


### Example Response

```json
{
  "tasks": [
    {
      "id": 1,
      "title": "Design Homepage",
      "slug": "design-homepage",
      "board_id": "3",
      "stage_id": "30",
      "status": "closed",
      "priority": "low",
      "position": "17.00",
      "created_by": "1",
      "meta": {
        "is_template": "no"
      }
      // ... other task properties
    },
    {
      "id": 2,
      "title": "Security Validation",
      "slug": "security-validation",
      "board_id": "3",
      "stage_id": "28",
      "status": "open",
      "priority": "low",
      "position": "1.00",
      "created_by": "1",
      "meta": {
        "is_template": "no"
      }
      // ... other task properties
    }
    // ... other tasks
  ]
}
```


## Get a Single Task

Retrieve a specific task by ID.

**HTTP Request**
```
GET /wp-json/fluent-boards/v2/projects/{board_id}/tasks/{task_id}
```

### Example Request

```bash
curl "https://yourdomain.com/wp-json/fluent-boards/v2/projects/{board_id}/tasks/{task_id}" \
  -H "Authorization: Basic API_USERNAME:API_PASSWORD"
```


### Example Response

```json
{
  "task": {
    "id": 1,
    "title": "Design Homepage",
    "slug": "design-homepage",
    "board_id": "3",
    "stage_id": "25",
    "status": "open",
    "priority": "low",
    "description": "<p>Create new homepage design</p>",
    "created_by": "1",
    "position": "23.00",
    "settings": {
      "subtask_count": 5,
      "attachment_count": 1,
      "subtask_completed_count": 2
    },
    "due_at": "2025-07-04 23:45:00",
    "isOverdue": true,
    "nextStage": "In Progress",
    "meta": {
      "is_template": "no"
    },
    "assignees": [
      {
        "ID": 1,
        "display_name": "John Doe",
        "email": "john@example.com"
        // ... other properties
      }
    ],
    "attachments": [
      {
        "id": 24,
        "title": "document.csv",
        "file_size": "2 KB"
        // ... other properties
      }
    ],
    "board": {
      "id": 3,
      "title": "Sample Board",
      "type": "to-do"
      // ... other properties
    },
    "stage": {
      "id": 25,
      "title": "Planned"
      // ... other properties
    },
    "labels": [
      {
        "id": 38,
        "title": "later",
        "bg_color": "#658ca5"
        // ... other properties
      }
    ]
    // ... other task properties
  }
}
```

## Create a Task

Create a new task.

**HTTP Request**
```
POST /wp-json/fluent-boards/v2/projects/{board_id}/tasks
```


### Request Body

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `task[title]` | string | Yes | Task title |
| `task[board_id]` | integer | Yes | Board ID |
| `task[stage_id]` | integer | Yes | Stage ID |
| `task[priority]` | string | No | Task priority (low, medium, high) |
| `task[crm_contact_id]` | integer | No | Associated FluentCRM contact ID |
| `task[is_template]` | string | No | Whether task is a template (yes) |

### Example Request

```bash
curl "https://yourdomain.com/wp-json/fluent-boards/v2/projects/{board_id}/tasks" \
  -X POST \
  -H "Authorization: Basic API_USERNAME:API_PASSWORD" \
  -H "Content-Type: application/json" \
  -d '{
    "task": {
      "title": "New Task",
      "board_id": 10,
      "stage_id": 104,
      "is_template": "no"
    }
  }'
```

### Example Response

```json
{
  "task": {
    "id": 281,
    "title": "New Task",
    "slug": "new-task",
    "board_id": "10",
    "stage_id": 104,
    "status": "open",
    "position": 1,
    "created_by": 1,
    "type": "task",
    "settings": {
      "cover": {
        "backgroundColor": ""
      },
      "subtask_count": 0,
      "attachment_count": 0,
      "subtask_completed_count": 0
    },
    "meta": [],
    "repeat_task_meta": null,
    "stage": {
      // ... stage properties
    },
    "board": {
      // ... board properties
    }
    // ... other task properties
  },
  "message": "Task has been successfully created",
  "updatedTasks": [
    // updated tasks
  ]
}
```

## Update Task Properties

Update specific properties of an existing task.

**HTTP Request**
```
PUT /wp-json/fluent-boards/v2/projects/{board_id}/tasks/{task_id}
```

### Supported Properties

| Property | Type | Description |
|----------|------|-------------|
| `title` | string | Task title |
| `description` | string | Task description |
| `status` | string | Task status (open, closed) |
| `priority` | string | Task priority (low, medium, high) |
| `due_at` | string | Due date and time |
| `started_at` | string | Start date |
| `assignees` | array | Array of user IDs |
| `crm_contact_id` | integer | Associated FluentCRM contact ID |
| `parent_id` | integer | Parent task ID for subtasks |
| `is_watching` | boolean | Whether user is watching the task |
| `archived_at` | string | Archive timestamp |
| `last_completed_at` | string | Completion timestamp |
| `board_id` | integer | Board ID |
| `type` | string | Task type |
| `reminder_type` | string | Reminder type |
| `remind_at` | string | Reminder timestamp |
| `settings` | object | Task settings |
| `is_template` | string | Whether task is a template |

### Example Request

```bash
curl "https://yourdomain.com/wp-json/fluent-boards/v2/projects/{board_id}/tasks/{task_id}" \
  -X PUT \
  -H "Authorization: Basic API_USERNAME:API_PASSWORD" \
  -H "Content-Type: application/json" \
  -d '{
    "property": "title",
    "value": "Updated Task Title"
  }'
```

### Example Response

```json
{
  "message": "Task has been updated",
  "task": {
    "id": 281,
    "title": "Updated Task Title",
    "slug": "new-task",
    "board_id": "10",
    "stage_id": "104",
    "status": "open",
    "priority": "low",
    "updated_at": "2025-08-06T08:29:04+00:00"
    // ... other task properties
  },
  "updatedTasks": [
    // ... updated tasks
  ]
}
```

## Delete a Task

Delete a task.

**HTTP Request**
```
DELETE /wp-json/fluent-boards/v2/projects/{board_id}/tasks/{task_id}
```

### Example Request

```bash
curl "https://yourdomain.com/wp-json/fluent-boards/v2/projects/{board_id}/tasks/{task_id}" \
  -X DELETE \
  -H "Authorization: Basic API_USERNAME:API_PASSWORD"
```


### Example Response

```json
{
  "updatedTasks": [],
  "message": "Task has been deleted"
}
```

## Move a Task

Move a task to a different stage.

**HTTP Request**
```
PUT /wp-json/fluent-boards/v2/projects/{board_id}/tasks/{task_id}/move-task
```


### Request Body

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `newStageId` | integer | Yes | Target stage ID |
| `newIndex` | integer | No | Position within the stage |
| `newBoardId` | integer | No | Target board ID (for moving between boards) |

### Example Request

```bash
curl "https://yourdomain.com/wp-json/fluent-boards/v2/projects/{board_id}/tasks/{task_id}/move-task" \
  -X PUT \
  -H "Authorization: Basic API_USERNAME:API_PASSWORD" \
  -H "Content-Type: application/json" \
  -d '{
    "newStageId": 96,
    "newIndex": 1,
    "newBoardId": 9
  }'
```

### Example Response

```json
{
  "message": "Task has been updated",
  "task": {
    "id": 282,
    "parent_id": null,
    "board_id": 9,
    "crm_contact_id": null,
    "title": "New task",
    "slug": "new-task",
    "type": "task",
    "status": "open",
    "stage_id": 96,
    "position": 1,
    // ... other task properties
  },
  "updatedTasks": [
    // ... updated tasks
  ],
  "last_updated": "2025-08-06 09:36:40"
}
```

## Clone a Task

Create a copy of an existing task.

**HTTP Request**
```
POST /wp-json/fluent-boards/v2/projects/{board_id}/tasks/{task_id}/clone-task
```


### Request Body

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `title` | string | Yes | Title for the cloned task |
| `stage_id` | integer | Yes | Target stage ID |
| `assignee` | boolean | Yes | Whether to clone assignees |
| `subtask` | boolean | Yes | Whether to clone subtasks (Pro only) |
| `label` | boolean | Yes | Whether to clone labels|
| `attachment` | boolean | Yes | Whether to clone attachments (Pro only) |
| `comment` | boolean | Yes | Whether to clone comments |

### Example Request

```bash
curl "https://yourdomain.com/wp-json/fluent-boards/v2/projects/{board_id}/tasks/{task_id}/clone-task" \
  -X POST \
  -H "Authorization: Basic API_USERNAME:API_PASSWORD" \
  -H "Content-Type: application/json" \
  -d '{
    "title": "Design Homepage (Cloned)",
    "stage_id": 29,
    "assignee": true,
    "subtask": false,
    "label": true,
    "attachment": false,
    "comment": true
  }'
```

## Get Task Comments

Retrieve comments for a specific task.

**HTTP Request**
```
GET /wp-json/fluent-boards/v2/projects/{board_id}/tasks/{task_id}/comments
```

### Example Request

```bash
curl "https://yourdomain.com/wp-json/fluent-boards/v2/projects/{board_id}/tasks/{task_id}/comments" \
  -H "Authorization: Basic API_USERNAME:API_PASSWORD"
```

### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `filter` | string | Sort order for comments (latest, oldest) |


### Example Response

```json
{
  "comments": {
    "current_page": 1,
    "data": [
      {
        "id": 3,
        "board_id": "3",
        "task_id": "85",
        "parent_id": null,
        "type": "comment",
        "privacy": "private",
        "status": "published",
        "author_name": "John Doe",
        "author_email": "john@example.com",
        "author_ip": "",
        "description": "Hello world",
        "created_by": "1",
        "settings": {
          "raw_description": "Hello world",
          "mentioned_id": null
        },
        "created_at": "2025-08-06T10:10:27+00:00",
        "updated_at": "2025-08-06T10:10:27+00:00",
        "replies": [],
        "replies_count": 0,
        "avatar": "https://example.com/avatar.jpg",
        "user": {
          "ID": 1,
          "user_login": "johndoe",
          "user_nicename": "john-doe",
          "user_email": "john@example.com",
          "user_url": "https://example.com",
          "user_registered": "2024-01-01 00:00:00",
          "user_status": "0",
          "display_name": "John Doe",
          "photo": "https://example.com/avatar.jpg"
        },
        "images": []
      }
    ],
    "first_page_url": "https://example.com/wp-json/fluent-boards/v2/projects/3/tasks/85/comments/?page=1",
    "from": 1,
    "last_page": 1,
    "last_page_url": "https://example.com/wp-json/fluent-boards/v2/projects/3/tasks/85/comments/?page=1",
    "links": [
      {
        "url": null,
        "label": "pagination.previous",
        "active": false
      },
      {
        "url": "https://example.com/wp-json/fluent-boards/v2/projects/3/tasks/85/comments/?page=1",
        "label": "1",
        "active": true
      },
      {
        "url": null,
        "label": "pagination.next",
        "active": false
      }
    ],
    "next_page_url": null,
    "path": "https://example.com/wp-json/fluent-boards/v2/projects/3/tasks/85/comments",
    "per_page": 10,
    "prev_page_url": null,
    "to": 1,
    "total": 1
  },
  "total": 1
}
```

## Get Task Activities

Retrieve recent activities for a specific task.

**HTTP Request**
```
GET /wp-json/fluent-boards/v2/projects/{board_id}/tasks/{task_id}/activities
```

### Example Request

```bash
curl "https://yourdomain.com/wp-json/fluent-boards/v2/projects/{board_id}/tasks/{task_id}/activities" \
  -H "Authorization: Basic API_USERNAME:API_PASSWORD"
```

### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `filter` | string | Sort order for activities (newest, oldest) |


### Example Response

```json
{
  "activities": {
    "current_page": 1,
    "data": [
      {
        "id": 120,
        "object_id": "85",
        "object_type": "task_activity",
        "action": "created",
        "column": "task",
        "old_value": null,
        "new_value": "Sample Task Title",
        "created_at": "2024-12-24T08:43:52+00:00",
        "user": {
          "ID": 1,
          "display_name": "John Doe",
          "user_email": "john@example.com"
        }
      },
      {
        "id": 372,
        "object_id": "85",
        "object_type": "task_activity",
        "action": "joined",
        "column": "task",
        "old_value": null,
        "new_value": null,
        "created_at": "2025-07-16T08:01:16+00:00",
        "user": {
          "ID": 1,
          "display_name": "John Doe",
          "user_email": "john@example.com"
        }
      },
      {
        "id": 373,
        "object_id": "85",
        "object_type": "task_activity",
        "action": "added",
        "column": "assignee",
        "old_value": null,
        "new_value": "Jane Smith",
        "created_at": "2025-07-16T08:01:17+00:00",
        "user": {
          "ID": 1,
          "display_name": "John Doe",
          "user_email": "john@example.com"
        }
      }
    ],
    "per_page": 15,
    "total": 13,
    "from": 1,
    "to": 13,
    "last_page": 1
    // ... pagination URLs and links
  }
}
```

## Error Responses

See [Common Error Responses](/rest-api/shared/error-responses) for standard error formats.

### Common Task-Specific Errors

- **404 Not Found** - Task not found
- **403 Forbidden** - You don't have permission to access this task
- **400 Bad Request** - Invalid task data or missing required fields

---

## Templates (Pro)
Source file : `src/rest-api/templates.md`

# Templates (Pro)

Endpoints to list template stages and tasks, toggle stage template status, and create a task from a template.

Base path for all endpoints below:
```
/wp-json/fluent-boards/v2
```

## List Template Stages

**HTTP Request**
```
GET /wp-json/fluent-boards/v2/projects/template-stages
```

### Example Response
```json
{
  "stages": [
    {
      "id": 10,
      "title": "Backlog",
      "board_id": 2,
      "settings": {
        "default_task_status": "open",
        "is_template": true
      },
      "board": {
        "id": 2,
        "title": "Example Board",
        "type": "to-do"
      }
    }
  ]
}
```

## List Template Tasks

**HTTP Request**
```
GET /wp-json/fluent-boards/v2/projects/get-template-tasks
```

### Example Response
```json
[
  {
    "id": 101,
    "board_id": 1,
    "title": "Example Template Task",
    "status": "open",
    "stage_id": 10,
    "meta": { "is_template": "yes" },
    "assignees": [ { "ID": 1, "display_name": "John Doe" } ],
    "labels": [ { "id": 7, "title": "bug", "bg_color": "#999999" } ]
  }
]
```

## Toggle Stage Template

Marks/unmarks a stage as a template.

**HTTP Request**
```
PUT /wp-json/fluent-boards/v2/projects/{board_id}/stage/{stage_id}/update-stage-template
```

### Example Response
```json
{
  "stage": {
    "id": 12,
    "board_id": 1,
    "title": "To Do",
    "type": "stage",
    "position": "1.00",
    "settings": { "default_task_status": "open", "is_template": false },
    "created_at": "2025-01-01T00:00:00+00:00",
    "updated_at": "2025-01-01T00:00:00+00:00"
  },
  "message": "Stage updated successfully"
}
```

## Import Stages From Board

Import one or more stages from another board into the current board.

**HTTP Request**
```
POST /wp-json/fluent-boards/v2/projects/{board_id}/import-from-board
```

### Request Body

| Field | Type | Required | Description |
|------|------|----------|-------------|
| `selectedStages[]` | array[integer] | Yes | Stage IDs to import |
| `position` | integer | No | Insert starting position (optional) |

### Example Response
```json
{
  "message": "Import successfully"
}
```


## Create Task From Template

Creates a new task by cloning a template task and optionally copying related data.

**HTTP Request**
```
POST /wp-json/fluent-boards/v2/projects/{board_id}/tasks/{task_id}/task-create-from-template
```

### Request Body

| Field | Type | Required | Description |
|------|------|----------|-------------|
| `title` | string | Yes | Title for the new task |
| `board_id` | integer | Yes | Target board ID |
| `stage_id` | integer | Yes | Target stage ID |
| `assignee` | boolean/string | Yes | Copy assignees from template (`true`/`false`) |
| `subtask` | boolean/string | Yes | Copy subtasks (`true`/`false`) |
| `label` | boolean/string | Yes | Copy labels (`true`/`false`) |
| `attachment` | boolean/string | Yes | Copy attachments (`true`/`false`) |

### Example Request
```json
{
  "title": "Example Task",
  "board_id": 1,
  "stage_id": 10,
  "assignee": "true",
  "subtask": "true",
  "label": "true",
  "attachment": "true"
}
```

### Example Response
```json
{
  "task": {
    "id": 999,
    "board_id": 1,
    "stage_id": 10,
    "title": "Example Task",
    "settings": { "subtask_count": 2, "attachment_count": 1 },
    "assignees": [ { "ID": 1, "display_name": "John Doe" } ],
    "labels": [ { "id": 7, "title": "bug" } ],
    "attachments": [ { "id": 1, "attachment_type": "image/png", "secure_url": "..." } ]
  },
  "message": "Task has been successfully created",
  "updatedTasks": [ { "id": 999, "stage_id": 10 } ]
}
```

Notes:
- Paths use `projects` and placeholders `{board_id}` and `{task_id}`.
- All endpoints are Pro-only and require authentication/permissions.

---

## Time Tracking
Source file : `src/rest-api/time-tracking.md`

# Time Tracking

The Time Tracking API allows you to manage time tracking for tasks in Fluent Boards. You can commit manual time entries, update or delete tracks, and generate time reports.

## Time Track Object

A time track represents a time tracking session for a task.

### Properties

| Property | Type | Description |
|----------|------|-------------|
| `id` | integer | Unique identifier for the time track |
| `task_id` | integer | ID of the task being tracked |
| `board_id` | integer | ID of the board/project |
| `user_id` | integer | ID of the user tracking time |
| `started_at` | string | Start time of the tracking session |
| `completed_at` | string | End time of the tracking session |
| `status` | string | Status of the time track (active, paused, completed) |
| `working_minutes` | integer | Worked minutes (system-calculated or committed) |
| `billable_minutes` | integer | Billable minutes |
| `is_manual` | integer | 1 if manually committed; 0 if auto-tracked |
| `message` | string | Description/notes of the work |
| `created_at` | string | Creation timestamp |
| `updated_at` | string | Last update timestamp |

### Status Values

- `active` - Currently tracking time
- `paused` - Time tracking is paused
- `completed` - Time tracking session completed
- `commited` - Time entry manually committed

## Get Time Tracks for a Task

Retrieve all time tracks for a specific task.

**HTTP Request**
```
GET /wp-json/fluent-boards/v2/projects/{board_id}/tasks/{task_id}/time-tracks
```

### Example Request

```bash
curl "https://yourdomain.com/wp-json/fluent-boards/v2/projects/1/tasks/1/time-tracks" \
  -H "Authorization: Basic API_USERNAME:API_PASSWORD"
```

### Example Response

```json
{
  "tracks": [
    {
      "id": 1,
      "task_id": 1,
      "board_id": 1,
      "user_id": 1,
      "started_at": "2025-08-06 10:00:00",
      "completed_at": "2025-08-06 12:00:00",
      "status": "completed",
      "working_minutes": 120,
      "billable_minutes": 0,
      "is_manual": 0,
      "message": "Design work on homepage",
      "created_at": "2025-08-06 10:00:00",
      "updated_at": "2025-08-06 12:00:00",
      "user": {
        "ID": 1,
        "display_name": "John Doe",
        "user_email": "john@example.com"
      }
    },
    {
      "id": 2,
      "task_id": 1,
      "board_id": 1,
      "user_id": 1,
      "started_at": "2025-08-06 14:00:00",
      "completed_at": null,
      "status": "active",
      "working_minutes": 0,
      "billable_minutes": 0,
      "is_manual": 0,
      "message": "Continued design work",
      "created_at": "2025-08-06 14:00:00",
      "updated_at": "2025-08-06 14:00:00",
      "user": {
        "ID": 1,
        "display_name": "John Doe",
        "user_email": "john@example.com"
      }
    }
  ],
  "estimated_minutes": 60
}
```


## Commit Time Tracking (Manual Entry)

Create a manual time track entry.

**HTTP Request**
```
POST /wp-json/fluent-boards/v2/projects/{board_id}/tasks/{task_id}/time-tracks
```

### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `board_id` | integer | The ID of the project |
| `task_id` | integer | The ID of the task |

### Request Body

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `billable_minutes` | integer | Yes | Total billable minutes |
| `message` | string | No | Description/notes |
| `completed_at` | string | No | End time (YYYY-MM-DD HH:MM:SS; timezone suffix allowed) |
| `started_at` | string | No | Start time (YYYY-MM-DD HH:MM:SS) |

### Example Request

```bash
curl -X POST "https://yourdomain.com/wp-json/fluent-boards/v2/projects/{board_id}/tasks/{task_id}/time-tracks" \
  -H "Authorization: Basic API_USERNAME:API_PASSWORD" \
  -H "Content-Type: application/json" \
  -d '{
    "billable_minutes": 60,
    "message": "Lorem ipsum",
    "completed_at": "2025-08-08"
  }'
```

### Example Response

```json
{
  "track": {
    "status": "commited",
    "completed_at": "2025-08-08 00:00:00",
    "billable_minutes": 60,
    "working_minutes": 60,
    "message": "Lorem ipsum",
    "user_id": 1,
    "board_id": "7",
    "is_manual": 1,
    "task_id": "272",
    "started_at": "2025-08-08 08:57:05",
    "updated_at": "2025-08-08T08:57:05+00:00",
    "created_at": "2025-08-08T08:57:05+00:00",
    "id": 2,
    "user": {
      "ID": 1,
      "user_login": "saikatcdas55Cancrie",
      "user_nicename": "saikat-c-das",
      "user_email": "saikatcdas@gmail.com",
      "user_url": "http://saikatcdas.com",
      "user_registered": "2024-08-28 03:33:23",
      "user_status": "0",
      "display_name": "Saikat Chandra Das",
      "photo": "https://secure.gravatar.com/avatar/628af4ad6672a9298e1e76af147689ba889521e9f7a65ac212ea70bdc2e8c6a1?s=128&d=mm&r=g"
    }
  },
  "message": "You have successfully submitted your working time"
}
```

## Update Time Estimation

Update the estimated time for a task.

**HTTP Request**
```
POST /wp-json/fluent-boards/v2/projects/{board_id}/tasks/{task_id}/time-tracks/estimated-time
```

### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `board_id` | integer | The ID of the project |
| `task_id` | integer | The ID of the task |

### Request Body

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `estimated_minutes` | integer | Yes | Estimated time in minutes |

### Example Request

```bash
curl -X POST "https://yourdomain.com/wp-json/fluent-boards/v2/projects/1/tasks/1/time-tracks/estimated-time" \
  -H "Authorization: Basic API_USERNAME:API_PASSWORD" \
  -H "Content-Type: application/json" \
  -d '{
    "estimated_minutes": 60
  }'
```

### Example Response

```json
{
  "message": "Estimated time has been updated"
}
```

## Delete a Time Track

Delete a specific time tracking session.

**HTTP Request**
```
DELETE /wp-json/fluent-boards/v2/projects/{board_id}/tasks/{task_id}/time-tracks/{track_id}
```

### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `board_id` | integer | The ID of the project |
| `task_id` | integer | The ID of the task |
| `track_id` | integer | The ID of the time track |

### Example Request

```bash
curl -X DELETE "https://yourdomain.com/wp-json/fluent-boards/v2/projects/1/tasks/1/time-tracks/1" \
  -H "Authorization: Basic API_USERNAME:API_PASSWORD"
```

### Example Response

```json
{
  "success": true,
  "message": "Selected time track has been deleted"
}
```

## Update a Time Track

Update an existing time tracking session.

**HTTP Request**
```
PUT /wp-json/fluent-boards/v2/projects/{board_id}/tasks/{task_id}/time-tracks/commit/{track_id}
```

### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `board_id` | integer | The ID of the project |
| `task_id` | integer | The ID of the task |
| `track_id` | integer | The ID of the time track |

### Request Body

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `billable_minutes` | integer | Yes | Billable minutes (also used as working minutes) |
| `message` | string | No | Description/notes of the work done |
| `completed_at` | string | No | End time |
| `started_at` | string | No | Start time |

### Example Request

```bash
curl -X PUT "https://yourdomain.com/wp-json/fluent-boards/v2/projects/1/tasks/1/time-tracks/commit/1" \
  -H "Authorization: Basic API_USERNAME:API_PASSWORD" \
  -H "Content-Type: application/json" \
  -d '{
    "billable_minutes": 90,
    "message": "Updated description for design work",
    "completed_at": "2025-08-08 12:00:00"
  }'
```

### Example Response

```json
{
  "success": true,
  "message": "Selected Time-track has been updated"
}
```

## Get Timesheet Reports

### By Tasks

Get timesheet data organized by tasks.

**HTTP Request**
```
GET /wp-json/fluent-boards/v2/projects/timesheet/by-tasks
```

### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `board_id` | integer | Filter by project ID |
| `date_range[]` | string[] | Array with two dates: start and end (YYYY-MM-DD) |

### Example Request

```bash
curl "https://yourdomain.com/wp-json/fluent-boards/v2/projects/timesheet/by-tasks?board_id=3&date_range[]=2025-08-01&date_range[]=2025-08-08" \
  -H "Authorization: Basic API_USERNAME:API_PASSWORD"
```

### Example Response

```json
{
  "tasks": [],
  "date_labels": [
    "2025-08-01",
    "2025-08-02",
    "2025-08-03",
    "2025-08-04",
    "2025-08-05",
    "2025-08-06",
    "2025-08-07",
    "2025-08-08"
  ],
  "totalMinutes": 0,
  "time_sheets": [],
  "date_range": [
    "2025-08-01 00:00:00",
    "2025-08-08 23:59:59"
  ]
}
```

### By Users

Get timesheet data organized by users.

**HTTP Request**
```
GET /wp-json/fluent-boards/v2/projects/timesheet/by-users
```

### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `board_id` | integer | Filter by project ID |
| `date_range[]` | string[] | Array with two dates: start and end (YYYY-MM-DD) |

### Example Request

```bash
curl "https://yourdomain.com/wp-json/fluent-boards/v2/projects/timesheet/by-users?board_id=3&date_range[]=2025-08-01&date_range[]=2025-08-08" \
  -H "Authorization: Basic API_USERNAME:API_PASSWORD"
```

### Example Response

```json
{
  "users": [],
  "date_labels": [
    "2025-08-01",
    "2025-08-02",
    "2025-08-03",
    "2025-08-04",
    "2025-08-05",
    "2025-08-06",
    "2025-08-07",
    "2025-08-08"
  ],
  "totalMinutes": 0,
  "time_sheets": [],
  "date_range": [
    "2025-08-01 09:16:56",
    "2025-08-08 23:59:59"
  ]
}
```

## Error Responses

See [Common Error Responses](/rest-api/shared/error-responses) for standard error formats.

### Common Time Tracking-Specific Errors

- **404 Not Found** - Time track not found
- **403 Forbidden** - You don't have permission to access this time track
- **400 Bad Request** - Invalid time tracking data or missing required fields

## Next Steps

- [Manage Tasks](/rest-api/tasks) - Work with tasks and time tracking
- [Board Management](/rest-api/boards) - Handle board time tracking
- [Reports](/rest-api/reports) - Generate comprehensive reports
- [User Management](/rest-api/users) - Manage user time tracking

---

## Users & Members
Source file : `src/rest-api/users.md`

# Users & Members

The Users & Members API allows you to manage board members, permissions, and user roles in Fluent Boards. You can add, remove, and manage user permissions across projects.

::: warning Note
Endpoints labeled "Pro" require Fluent Boards Pro.
:::

## List All Users

Retrieve all users in the system with their board memberships and roles.

**HTTP Request**
```
GET /wp-json/fluent-boards/v2/fluent-boards-users
```

### Example Request

```bash
curl "https://yourdomain.com/wp-json/fluent-boards/v2/fluent-boards-users" \
  -H "Authorization: Basic API_USERNAME:API_PASSWORD"
```


### Example Response

```json
{
  "users": [
    {
      "ID": 1,
      "display_name": "John Doe",
      "photo": "https://secure.gravatar.com/avatar/example1?s=128&d=mm&r=g",
      "email": "john@example.com",
      "boards": [
        {
          "id": 1,
          "title": "Project Alpha",
          "role": "admin"
        },
        {
          "id": 2,
          "title": "Project Beta",
          "role": "member"
        }
      ],
      "is_super": false,
      "is_wpadmin": true
    },
    {
      "ID": 2,
      "display_name": "Jane Smith",
      "photo": "https://secure.gravatar.com/avatar/example2?s=128&d=mm&r=g",
      "email": "jane@example.com",
      "boards": [
        {
          "id": 1,
          "title": "Project Alpha",
          "role": "member"
        }
      ],
      "is_super": false,
      "is_wpadmin": false
    }
  ],
  "boards": [
    {
      "id": 1,
      "title": "Project Alpha",
      "meta": {
        "custom_field_positions": "yes"
      },
      "isUserOnlyViewer": false
    },
    {
      "id": 2,
      "title": "Project Beta",
      "meta": {
        "custom_field_positions": "yes"
      },
      "isUserOnlyViewer": false
    }
  ]
}
```

## Search Users

Search for users by display name. Returns users who are members of boards and match the search criteria.

**HTTP Request**
```
GET /wp-json/fluent-boards/v2/search-fluent-boards-users
```

### Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `searchInput` | string | Search term for user display name |

### Example Request

```bash
curl "https://yourdomain.com/wp-json/fluent-boards/v2/search-fluent-boards-users" \
  -H "Authorization: Basic API_USERNAME:API_PASSWORD" \
  -H "Content-Type: application/json" \
  -d '{
    "searchInput": "john"
  }'
```


### Example Response

```json
[
  {
    "ID": 1,
    "user_login": "johndoe",
    "user_nicename": "john-doe",
    "user_email": "john@example.com",
    "user_url": "http://example.com",
    "user_registered": "2024-01-15 10:30:00",
    "user_status": "0",
    "display_name": "John Doe",
    "photo": "https://secure.gravatar.com/avatar/example1?s=128&d=mm&r=g",
    "which_boards": [
      {
        "id": 1,
        "parent_id": null,
        "title": "Project Alpha",
        "description": "Main project board",
        "type": "to-do",
        "currency": "USD",
        "background": {
          "id": "solid_1",
          "is_image": false,
          "image_url": null,
          "color": "#2196F3"
        },
        "settings": {
          "tasks_count": 25
        },
        "created_by": "1",
        "archived_at": null,
        "meta": {
          "custom_field_positions": "yes"
        },
        "isUserOnlyViewer": false,
        "pivot": {
          "foreign_id": "1",
          "object_id": "1",
          "settings": "a:1:{s:8:\"is_admin\";b:1;}",
          "preferences": "a:7:{s:19:\"email_after_comment\";b:1;s:23:\"email_after_task_assign\";b:1;s:29:\"email_after_task_stage_change\";b:1;s:32:\"email_after_task_due_date_change\";b:1;s:28:\"email_after_remove_from_task\";b:1;s:24:\"email_after_task_archive\";b:1;s:22:\"dashboard_notification\";b:1;}",
          "created_at": "2024-01-15T10:30:00+00:00",
          "updated_at": "2024-01-15T10:30:00+00:00"
        }
      }
    ],
    "is_wpadmin": true,
    "is_super": false
  },
  {
    "ID": 2,
    "user_login": "janesmith",
    "user_nicename": "jane-smith",
    "user_email": "jane@example.com",
    "user_url": "",
    "user_registered": "2024-02-01 09:15:00",
    "user_status": "0",
    "display_name": "Jane Smith",
    "photo": "https://secure.gravatar.com/avatar/example2?s=128&d=mm&r=g",
    "which_boards": [
      {
        "id": 2,
        "parent_id": null,
        "title": "Project Beta",
        "description": "Secondary project board",
        "type": "to-do",
        "currency": "USD",
        "background": {
          "id": "solid_2",
          "is_image": false,
          "image_url": null,
          "color": "#4CAF50"
        },
        "settings": {
          "tasks_count": 15
        },
        "created_by": "1",
        "archived_at": null,
        "meta": {
          "custom_field_positions": "yes"
        },
        "isUserOnlyViewer": false,
        "pivot": {
          "foreign_id": "2",
          "object_id": "2",
          "settings": "a:1:{s:8:\"is_admin\";b:0;}",
          "preferences": "a:7:{s:19:\"email_after_comment\";b:1;s:23:\"email_after_task_assign\";b:1;s:29:\"email_after_task_stage_change\";b:1;s:32:\"email_after_task_due_date_change\";b:1;s:28:\"email_after_remove_from_task\";b:1;s:24:\"email_after_task_archive\";b:1;s:22:\"dashboard_notification\";b:1;}",
          "created_at": "2024-02-01T09:15:00+00:00",
          "updated_at": "2024-02-01T09:15:00+00:00"
        }
      }
    ],
    "all_boards": null,
    "is_super": false,
    "is_wpadmin": false
  }
]
```

## Get Project Members

Retrieve all members of a specific project.

**HTTP Request**
```
GET /wp-json/fluent-boards/v2/projects/{board_id}/users
```

### Example Request

```bash
curl "https://yourdomain.com/wp-json/fluent-boards/v2/projects/{board_id}/users" \
  -H "Authorization: Basic API_USERNAME:API_PASSWORD"
```


### Example Response

```json
{
  "users": [
    {
      "ID": 1,
      "display_name": "John Doe",
      "user_login": "johndoe",
      "email": "john@example.com",
      "photo": "https://secure.gravatar.com/avatar/example1?s=128&d=mm&r=g",
      "role": "admin",
      "is_super": false,
      "is_wpadmin": true
    },
    {
      "ID": 2,
      "display_name": "Jane Smith",
      "user_login": "janesmith",
      "email": "jane@example.com",
      "photo": "https://secure.gravatar.com/avatar/example2?s=128&d=mm&r=g",
      "role": "member",
      "is_super": false,
      "is_wpadmin": false
    }
  ],
  "global_admins": []
}
```

## Add Members to Project

Add a single user to a project. The user can be added as a regular member or as a viewer only.

**HTTP Request**
```
POST /wp-json/fluent-boards/v2/projects/{board_id}/add-members
```

### Request Body

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `memberId` | integer | Yes | ID of the user to add |
| `isViewerOnly` | string | No | Set to 'yes' to add as viewer only |


### Example Request

```bash
curl "https://yourdomain.com/wp-json/fluent-boards/v2/projects/{board_id}/add-members" \
  -X POST \
  -H "Authorization: Basic API_USERNAME:API_PASSWORD" \
  -H "Content-Type: application/json" \
  -d '{
    "memberId": 5,
    "isViewerOnly": "yes"
  }'
```

### Example Response

```json
{
  "message": "Member added successfully",
  "member": {
    "ID": 5,
    "user_login": "janesmith",
    "user_nicename": "jane-smith",
    "user_email": "jane@example.com",
    "user_url": "",
    "user_registered": "2024-02-01 09:15:00",
    "user_status": "0",
    "display_name": "Jane Smith",
    "photo": "https://secure.gravatar.com/avatar/example5?s=128&d=mm&r=g"
  }
}
```

## Remove User from Project

Remove a user from a project.

**HTTP Request**
```
POST /wp-json/fluent-boards/v2/projects/{board_id}/user/{user_id}/remove
```

### Example Request

```bash
curl "https://yourdomain.com/wp-json/fluent-boards/v2/projects/{board_id}/user/{user_id}/remove" \
  -X POST \
  -H "Authorization: Basic API_USERNAME:API_PASSWORD"
```

### Example Response

```json
{
  "message": "Member removed successfully"
}
```

## Make User Manager

Promote a user to manager role in a project. This gives the user administrative privileges for the specific board. **Note:** The user must already be a member of the board before they can be promoted to manager.

> Pro

**HTTP Request**
```
POST /wp-json/fluent-boards/v2/projects/{board_id}/user/{user_id}/make-manager
```

### Example Request

```bash
curl "https://yourdomain.com/wp-json/fluent-boards/v2/projects/{board_id}/user/{user_id}/make-manager" \
  -X POST \
  -H "Authorization: Basic API_USERNAME:API_PASSWORD"
```


### Example Response

```json
{
  "message": "Role updated successfully",
  "member": {
    "ID": 5,
    "user_login": "janesmith",
    "user_nicename": "jane-smith",
    "user_email": "jane@example.com",
    "user_url": "",
    "user_registered": "2024-02-01 09:15:00",
    "user_status": "0",
    "display_name": "Jane Smith",
    "is_admin": true,
    "is_board_admin": true,
    "photo": "https://secure.gravatar.com/avatar/example5?s=128&d=mm&r=g"
  }
}
```

## Remove Manager Role

Remove manager role from a user.

> Pro

**HTTP Request**
```
POST /wp-json/fluent-boards/v2/projects/{board_id}/user/{user_id}/remove-manager
```

### Example Request

```bash
curl "https://yourdomain.com/wp-json/fluent-boards/v2/projects/{board_id}/user/{user_id}/remove-manager" \
  -X POST \
  -H "Authorization: Basic API_USERNAME:API_PASSWORD"
```


### Example Response

```json
{
  "message": "Role updated successfully",
  "member": {
    "ID": 5,
    "user_login": "janesmith",
    "user_nicename": "jane-smith",
    "user_email": "jane@example.com",
    "user_url": "",
    "user_registered": "2024-02-01 09:15:00",
    "user_status": "0",
    "display_name": "Jane Smith",
    "is_admin": false,
    "is_board_admin": false,
    "photo": "https://secure.gravatar.com/avatar/example5?s=128&d=mm&r=g"
  }
}
```

## Make User Member

Set a user's role to member in a project. This endpoint can convert admins to regular members (removing admin privileges) or upgrade viewers to members (increasing permissions). Members have full access to tasks and boards. **Note:** The user must already be a board viewer or manager before they can be converted to a member.

> Pro

**HTTP Request**
```
POST /wp-json/fluent-boards/v2/projects/{board_id}/user/{user_id}/make-member
```

### Example Request

```bash
curl "https://yourdomain.com/wp-json/fluent-boards/v2/projects/{board_id}/user/{user_id}/make-member" \
  -X POST \
  -H "Authorization: Basic API_USERNAME:API_PASSWORD"
```


### Example Response

```json
{
  "message": "Role updated successfully",
  "member": {
    "ID": 5,
    "user_login": "janesmith",
    "user_nicename": "jane-smith",
    "user_email": "jane@example.com",
    "user_url": "",
    "user_registered": "2024-02-01 09:15:00",
    "user_status": "0",
    "display_name": "Jane Smith",
    "is_admin": false,
    "is_board_admin": false,
    "photo": "https://secure.gravatar.com/avatar/example5?s=128&d=mm&r=g"
  }
}
```

## Make User Viewer

Set a user's role to viewer in a project. This endpoint can convert admins or members to viewers (reducing permissions). Viewers have read-only access to tasks and boards. **Note:** The user must already be a board member or manager before they can be converted to a viewer.

> Pro

**HTTP Request**
```
POST /wp-json/fluent-boards/v2/projects/{board_id}/user/{user_id}/make-viewer
```

### Example Request

```bash
curl "https://yourdomain.com/wp-json/fluent-boards/v2/projects/{board_id}/user/{user_id}/make-viewer" \
  -X POST \
  -H "Authorization: Basic API_USERNAME:API_PASSWORD"
```


### Example Response

```json
{
  "message": "Role updated successfully",
  "member": {
    "ID": 5,
    "user_login": "janesmith",
    "user_nicename": "jane-smith",
    "user_email": "jane@example.com",
    "user_url": "",
    "user_registered": "2024-02-01 09:15:00",
    "user_status": "0",
    "display_name": "Jane Smith",
    "is_admin": false,
    "is_board_admin": false,
    "photo": "https://secure.gravatar.com/avatar/example5?s=128&d=mm&r=g"
  }
}
```

<!-- ## Get User Permissions

Retrieve user permissions for a specific board. Returns the user's role and permissions for the specified board.

**HTTP Request**
```
GET /wp-json/fluent-boards/v2/get-user-permissions
```

### Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `boardId` | integer | Yes | The ID of the board |
| `userId` | integer | Yes | The ID of the user |


### Example Response

```json
{
  "success": true,
  "board_id": 1,
  "user_id": 2,
  "is_admin": false,
  "permissions": {
    "manage_tasks": true,
    "view_projects": true,
    "create_tasks": true,
    "edit_tasks": true
  },
  "status": "ACTIVE"
}
```

## Update User Permissions

Update user permissions globally.

**HTTP Request**
```
PUT /wp-json/fluent-boards/v2/update-user-permissions
```

### Request Body

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `user_id` | integer | Yes | The ID of the user |
| `permissions` | object | Yes | Object with permission keys and boolean values |


### Example Response

```json
{
  "data": {
    "user_id": 2,
    "permissions": {
      "manage_projects": false,
      "manage_tasks": true,
      "manage_users": false,
      "view_reports": true
    }
  },
  "message": "User permissions updated successfully"
}
``` -->

<!-- ## Set Permission All Board Admin

Set a user as admin for all boards.

**HTTP Request**
```
POST /wp-json/fluent-boards/v2/set-permission-all-board-admin
```

### Request Body

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `user_id` | integer | Yes | The ID of the user |


### Example Response

```json
{
  "message": "User set as admin for all boards successfully"
}
``` -->

## Remove User from Board

Remove a user from a specific board.

**HTTP Request**
```
DELETE /wp-json/fluent-boards/v2/remove-user-from-board
```

### Request Body

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `boardId` | integer | Yes | The ID of the board |
| `userId` | integer | Yes | The ID of the user |

### Example Request

```bash
curl "https://yourdomain.com/wp-json/fluent-boards/v2/remove-user-from-board" \
  -X DELETE \
  -H "Authorization: Basic API_USERNAME:API_PASSWORD" \
  -H "Content-Type: application/json" \
  -d '{
    "boardId": 3,
    "userId": 5
  }'
```

### Example Response

```json
{
  "message": "User Removed from Board successfully!"
}
```

## Sync Board Roles

Synchronize user roles across multiple boards. This endpoint allows you to update or remove user roles from multiple boards in a single request. **Note:** Super admin users cannot have their roles synced.

> Pro

**HTTP Request**
```
POST /wp-json/fluent-boards/v2/managers/roles/{user_id}
```

### Request Body

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `roles` | object | Yes | Object with board_id as key and role as value. Valid roles: `admin`, `member`, `viewer`. Empty values will remove the user from that board. |

### Example Request

```bash
curl "https://yourdomain.com/wp-json/fluent-boards/v2/managers/roles/{user_id}" \
  -X POST \
  -H "Authorization: Basic API_USERNAME:API_PASSWORD" \
  -H "Content-Type: application/json" \
  -d '{
    "roles": {
      "1": "admin",
      "2": "member",
      "3": "viewer"
    }
  }'
```

### Example Response

```json
{
  "message": "User roles has been synced successfully."
}
```

## Get Project Assignees

Get all users who can be assigned to tasks in a project.

**HTTP Request**
```
GET /wp-json/fluent-boards/v2/projects/{board_id}/assignees
```

### Example Request

```bash
curl "https://yourdomain.com/wp-json/fluent-boards/v2/projects/{board_id}/assignees" \
  -H "Authorization: Basic API_USERNAME:API_PASSWORD"
```


### Example Response

```json
{
  "data": [
    {
      "ID": 1,
      "user_login": "john_doe",
      "user_nicename": "john-doe",
      "user_email": "john.doe@example.com",
      "user_url": "https://example.com",
      "user_registered": "2024-01-15 10:30:00",
      "user_status": "0",
      "display_name": "John Doe",
      "photo": "https://secure.gravatar.com/avatar/example123?s=128&d=mm&r=g",
      "pivot": {
        "object_id": "3",
        "foreign_id": "1",
        "settings": "a:1:{s:8:\"is_admin\";b:0;}",
        "preferences": "a:6:{s:19:\"email_after_comment\";b:0;s:29:\"email_after_task_stage_change\";b:0;s:23:\"email_after_task_assign\";b:0;s:32:\"email_after_task_due_date_change\";b:0;s:28:\"email_after_remove_from_task\";b:0;s:24:\"email_after_task_archive\";b:0;}",
        "created_at": "2025-01-15T10:30:00+00:00",
        "updated_at": "2025-01-20T14:45:00+00:00"
      }
    },
    {
      "ID": 2,
      "user_login": "jane_smith",
      "user_nicename": "jane-smith",
      "user_email": "jane.smith@example.com",
      "user_url": "https://janesmith.com",
      "user_registered": "2024-02-20 09:15:00",
      "user_status": "0",
      "display_name": "Jane Smith",
      "photo": "https://secure.gravatar.com/avatar/example456?s=128&d=mm&r=g",
      "pivot": {
        "object_id": "3",
        "foreign_id": "2",
        "settings": "a:1:{s:8:\"is_admin\";b:1;}",
        "preferences": "a:6:{s:19:\"email_after_comment\";b:1;s:29:\"email_after_task_stage_change\";b:1;s:23:\"email_after_task_assign\";b:1;s:32:\"email_after_task_due_date_change\";b:1;s:28:\"email_after_remove_from_task\";b:0;s:24:\"email_after_task_archive\";b:0;}",
        "created_at": "2025-01-10T08:00:00+00:00",
        "updated_at": "2025-01-18T16:30:00+00:00"
      }
    }
  ]
}
```

## Error Responses

See [Common Error Responses](/rest-api/shared/error-responses) for standard error formats.

### Common User-Specific Errors

- **404 Not Found** - User not found
- **403 Forbidden** - You don't have permission to manage users
- **400 Bad Request** - Invalid user data or missing required fields

---

## Webhooks
Source file : `src/rest-api/webhooks.md`

# Webhooks

The Webhooks API allows you to set up and manage webhook integrations in Fluent Boards. You can create, read, update, and delete webhooks to receive real-time notifications when events occur in your boards.

## Webhook Object

A webhook represents an integration endpoint that receives notifications when events occur.

## List All Webhooks

Retrieve a paginated list of webhooks.

**HTTP Request**
```
GET /wp-json/fluent-boards/v2/webhooks
```

### Parameters

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| `search` | string | No | ''(empty string) | Search term to filter webhooks by name. |


### Example Response

```json
{
    "webhooks": [
        {
            "id": 11,
            "object_id": null,
            "object_type": "webhook",
            "key": "8771db3e-094b-464f-bd16-e5a55eac5c80",
            "value": {
                "name": "Slack test",
                "board": "2",
                "stage": "15",
                "query_timestamp": "1756199331378",
                "url": "https://bipulkarmokar.wp1.site/?fbs=1&route=task&hash=8771db3e-094b-464f-bd16-e5a55eac5c80"
            },
            "created_at": "2025-08-26T09:08:52+00:00",
            "updated_at": "2025-08-26T09:08:52+00:00"
        },
        {
            "id": 9,
            "object_id": null,
            "object_type": "webhook",
            "key": "b3c51ea0-ef5c-4d72-a335-6bede48c31e4",
            "value": {
                "name": "Webhook Test",
                "board": "2",
                "stage": "14",
                "query_timestamp": "1756199191548",
                "url": "https://bipulkarmokar.wp1.site/?fbs=1&route=task&hash=b3c51ea0-ef5c-4d72-a335-6bede48c31e4"
            },
            "created_at": "2025-08-21T04:30:47+00:00",
            "updated_at": "2025-08-26T09:06:32+00:00"
        }
    ],
    "fields": [
        {
            "key": "title",
            "field": {
                "field": "Title",
                "type": "text",
                "rules": "required",
                "description": "Title of the task."
            }
        },
        {
            "key": "stage",
            "field": {
                "field": "Stage",
                "type": "int|text",
                "rules": "optional",
                "description": "The stage of the task, which can be an ID, title, or slug. Example: 1 | \"open\" | \"Open\""
            }
        },
        {
            "key": "parent_id",
            "field": {
                "field": "Parent Task",
                "type": "int",
                "rules": "optional",
                "description": "Parent Task ID of the subtask. Example: 1"
            }
        },
        {
            "key": "status",
            "field": {
                "field": "Status",
                "type": "text",
                "rules": "optional",
                "description": "The status of the task (open | closed). Example: \"closed\""
            }
        },
        {
            "key": "description",
            "field": {
                "field": "Description",
                "type": "textarea",
                "rules": "optional",
                "description": "Description of the task"
            }
        },
        {
            "key": "priority",
            "field": {
                "field": "Priority",
                "type": "text",
                "rules": "optional",
                "description": "Priority of the task (low | medium | high). Example: \"medium\" "
            }
        },
        {
            "key": "due_at",
            "field": {
                "field": "Due Date",
                "type": "date",
                "rules": "optional",
                "description": "The due date of the task in the format YYYY-MM-DD hh:mm. Example: 2099-12-31 23:59:59"
            }
        },
        {
            "key": "started_at",
            "field": {
                "field": "Start Date",
                "type": "date",
                "rules": "optional",
                "description": "The start date of the task in the format YYYY-MM-DD. Example: 2099-12-31"
            }
        },
        {
            "key": "source",
            "field": {
                "field": "Source",
                "type": "text",
                "rules": "optional",
                "description": "The source of the task. Example: \"jira\""
            }
        },
        {
            "key": "source_id",
            "field": {
                "field": "Source Id",
                "type": "text|int",
                "rules": "optional",
                "description": "The source Id of the task (if any). Example: \"bcy664fh177\""
            }
        },
        {
            "key": "crm_contact_id",
            "field": {
                "field": "CRM Contact Id",
                "type": "int",
                "rules": "optional",
                "description": "The ID of the associated FluentCRM contact. Example: 6465"
            }
        },
        {
            "key": "contact_email",
            "field": {
                "field": "CRM Contact Email",
                "type": "text",
                "rules": "optional",
                "description": "The email of the associated CRM contact. Example: \"john.doe@example.com\""
            }
        },
        {
            "key": "contact_first_name",
            "field": {
                "field": "Contact First Name",
                "type": "text",
                "rules": "optional",
                "description": "Associated CRM Contact First Name. Example: \"John\""
            }
        },
        {
            "key": "contact_last_name",
            "field": {
                "field": "Contact Last Name",
                "type": "text",
                "rules": "optional",
                "description": "Associated CRM Contact Last Name"
            }
        },
        {
            "key": "labels",
            "field": {
                "field": "Labels",
                "type": "text|int",
                "rules": "optional",
                "description": "An array of label IDs or titles. Example: [1, \"feature\", 44]"
            }
        },
        {
            "key": "assignees",
            "field": {
                "field": "Assignees",
                "type": "text|int",
                "rules": "optional",
                "description": "An array of WP User IDs. Example: [1,2,44]"
            }
        }
    ]
}
```

## Create a Webhook

Create a new webhook.

**HTTP Request**
```
POST /wp-json/fluent-boards/v2/webhooks
```

### Request Body

| Parameter     | Type    | Required | Description                           |
|---------------|---------|----------|---------------------------------------|
| `name`        | string  | Yes | Webhook name                          |
| `board`       | integer | Yes | Board ID                              |
| `stage`       | Integer | Yes | Stage ID                              |


### Example Response

```json
{
  "id": 13,
  "webhook": {
    "name": "Gmail",
    "board": "2",
    "stage": "15",
    "url": "https://bipulkarmokar.wp1.site/?fbs=1&route=task&hash=8db17df2-f13b-477a-bebf-62bd41622c6a"
  },
  "webhooks": [
    {
      "id": 13,
      "object_id": null,
      "object_type": "webhook",
      "key": "8db17df2-f13b-477a-bebf-62bd41622c6a",
      "value": {
        "name": "Gmail",
        "board": "2",
        "stage": "15",
        "url": "https://bipulkarmokar.wp1.site/?fbs=1&route=task&hash=8db17df2-f13b-477a-bebf-62bd41622c6a"
      },
      "created_at": "2025-08-26T09:22:33+00:00",
      "updated_at": "2025-08-26T09:22:33+00:00"
    },
    {
      "id": 12,
      "object_id": null,
      "object_type": "webhook",
      "key": "d5f02242-c894-4725-9b81-cc141ca4ee08",
      "value": {
        "name": "Discord",
        "board": "2",
        "stage": "15",
        "query_timestamp": "1756200073976",
        "url": "https://bipulkarmokar.wp1.site/?fbs=1&route=task&hash=d5f02242-c894-4725-9b81-cc141ca4ee08"
      },
      "created_at": "2025-08-26T09:21:14+00:00",
      "updated_at": "2025-08-26T09:21:14+00:00"
    },
    {
      "id": 11,
      "object_id": null,
      "object_type": "webhook",
      "key": "8771db3e-094b-464f-bd16-e5a55eac5c80",
      "value": {
        "name": "Slack test",
        "board": "2",
        "stage": "15",
        "query_timestamp": "1756199331378",
        "url": "https://bipulkarmokar.wp1.site/?fbs=1&route=task&hash=8771db3e-094b-464f-bd16-e5a55eac5c80"
      },
      "created_at": "2025-08-26T09:08:52+00:00",
      "updated_at": "2025-08-26T09:08:52+00:00"
    },
    {
      "id": 9,
      "object_id": null,
      "object_type": "webhook",
      "key": "b3c51ea0-ef5c-4d72-a335-6bede48c31e4",
      "value": {
        "name": "Webhook Test",
        "board": "2",
        "stage": "14",
        "query_timestamp": "1756199191548",
        "url": "https://bipulkarmokar.wp1.site/?fbs=1&route=task&hash=b3c51ea0-ef5c-4d72-a335-6bede48c31e4"
      },
      "created_at": "2025-08-21T04:30:47+00:00",
      "updated_at": "2025-08-26T09:06:32+00:00"
    }
  ],
  "message": "Successfully Created the WebHook"
}
```

## Delete a Webhook

Delete a webhook.

**HTTP Request**
```
DELETE /wp-json/fluent-boards/v2/webhooks/{id}
```

### Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `id` | integer | Yes | The ID of the webhook |


### Example Response

```json
{
    "webhooks": [
        {
            "id": 12,
            "object_id": null,
            "object_type": "webhook",
            "key": "d5f02242-c894-4725-9b81-cc141ca4ee08",
            "value": {
                "name": "Discord",
                "board": "2",
                "stage": "15",
                "query_timestamp": "1756200073976",
                "url": "https://bipulkarmokar.wp1.site/?fbs=1&route=task&hash=d5f02242-c894-4725-9b81-cc141ca4ee08"
            },
            "created_at": "2025-08-26T09:21:14+00:00",
            "updated_at": "2025-08-26T09:21:14+00:00"
        },
        {
            "id": 11,
            "object_id": null,
            "object_type": "webhook",
            "key": "8771db3e-094b-464f-bd16-e5a55eac5c80",
            "value": {
                "name": "Slack test",
                "board": "2",
                "stage": "15",
                "query_timestamp": "1756199331378",
                "url": "https://bipulkarmokar.wp1.site/?fbs=1&route=task&hash=8771db3e-094b-464f-bd16-e5a55eac5c80"
            },
            "created_at": "2025-08-26T09:08:52+00:00",
            "updated_at": "2025-08-26T09:08:52+00:00"
        },
        {
            "id": 9,
            "object_id": null,
            "object_type": "webhook",
            "key": "b3c51ea0-ef5c-4d72-a335-6bede48c31e4",
            "value": {
                "name": "Webhook Test",
                "board": "2",
                "stage": "14",
                "query_timestamp": "1756199191548",
                "url": "https://bipulkarmokar.wp1.site/?fbs=1&route=task&hash=b3c51ea0-ef5c-4d72-a335-6bede48c31e4"
            },
            "created_at": "2025-08-21T04:30:47+00:00",
            "updated_at": "2025-08-26T09:06:32+00:00"
        }
    ],
    "message": "Successfully deleted the webhook"
}
```

---
