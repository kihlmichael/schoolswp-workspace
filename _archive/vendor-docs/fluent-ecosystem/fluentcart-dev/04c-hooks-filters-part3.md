# FluentCart Developer Docs - Hooks (Filters) (Part 3/6)

Tous les filtres WordPress exposés par FluentCart, groupés par domaine (cart & checkout, orders & payments, customers & subscriptions, products & pricing, settings & configuration, integrations & advanced).

---

## Integrations & Advanced | FluentCart Developer Docs

**URL** : https://dev.fluentcart.com/hooks/filters/integrations-and-advanced

[Skip to content](https://dev.fluentcart.com/hooks/filters/integrations-and-advanced#VPContent)

# Integrations & Advanced [​](https://dev.fluentcart.com/hooks/filters/integrations-and-advanced\#integrations-advanced)

All filters related to external integrations, file storage, templates, [License](https://dev.fluentcart.com/database/models/license.html) management, and advanced features.

* * *

## Integration Actions & Feeds [​](https://dev.fluentcart.com/hooks/filters/integrations-and-advanced\#integration-actions-feeds)

### ` order_integrations` [​](https://dev.fluentcart.com/hooks/filters/integrations-and-advanced\#order-integrations)

`fluent_cart/integration/order_integrations` - Filter all registered order integrations

**When it runs:** This filter is applied when retrieving the list of all registered order integrations. It is used across integration event handling, integration controllers, product integration setup, global settings, and addon modules.

**Parameters:**

- `$integrations` (array): Array of registered integrations (default `[]`)
php

```
$integrations = [\
      'mailchimp' => [\
          'title' => 'MailChimp',\
          'logo' => 'https://example.com/mailchimp-logo.png',\
          'enabled' => true\
      ]\
];
```


**Returns:**

- `$integrations` (array): The modified integrations array

**Source:**`IntegrationEventListener.php:54,247,386`, `IntegrationController.php:96,150`, `ProductIntegrationsController.php:18,48`, `GlobalIntegrationSettings.php:84`, `AddOnModule.php:16`

**Usage:**

php

```
add_filter('fluent_cart/integration/order_integrations', function ($integrations) {
    $integrations['custom_crm'] = [\
        'title'   => 'Custom CRM',\
        'logo'    => 'https://example.com/crm-logo.png',\
        'enabled' => true,\
    ];
    return $integrations;
});
```

### ` run_all_actions_on_async` [​](https://dev.fluentcart.com/hooks/filters/integrations-and-advanced\#run-all-actions-on-async)

`fluent_cart/integration/run_all_actions_on_async` - Force all integration actions to run asynchronously

**When it runs:** This filter controls whether integration actions should be dispatched asynchronously instead of running immediately during order processing.

**Parameters:**

- `$async` (bool): Whether to force async execution (default `false`)
- `$order` ( [Order](https://dev.fluentcart.com/database/models/order.html)): The order model
- `$hook` (string): The integration hook being fired

**Returns:**

- `$async` (bool): Whether to run actions asynchronously

**Source:**`IntegrationEventListener.php:145`

**Usage:**

php

```
add_filter('fluent_cart/integration/run_all_actions_on_async', function ($async, $order, $hook) {
    // Force async for large orders to avoid timeout
    if ($order->total > 100000) {
        return true;
    }
    return $async;
}, 10, 3);
```

### ` global_notification_types` [​](https://dev.fluentcart.com/hooks/filters/integrations-and-advanced\#global-notification-types)

`fluent_cart/integration/global_notification_types` - Filter available notification types

**When it runs:** This filter is applied when retrieving the list of available global notification types for integrations.

**Parameters:**

- `$types` (array): Array of notification types (default `[]`)
php

```
$types = [\
      'email' => [\
          'title' => 'Email Notification',\
          'description' => 'Send email notifications'\
      ]\
];
```


**Returns:**

- `$types` (array): The modified notification types array

**Source:**`GlobalIntegrationSettings.php:119`

**Usage:**

php

```
add_filter('fluent_cart/integration/global_notification_types', function ($types) {
    $types['sms'] = [\
        'title'       => 'SMS Notification',\
        'description' => 'Send SMS notifications on order events',\
    ];
    return $types;
});
```

### ` global_notification_feed_{$feed_key}` [​](https://dev.fluentcart.com/hooks/filters/integrations-and-advanced\#global-notification-feed-feed-key)

`fluent_cart/integration/global_notification_feed_{$feed_key}` - Filter notification feed data (DYNAMIC)

**When it runs:** This dynamic filter is applied when retrieving notification feed data for a specific feed key. The `{$feed_key}` portion is replaced with the actual feed identifier.

**Parameters:**

- `$feedData` (array): The notification feed data

**Returns:**

- `$feedData` (array): The modified feed data

**Source:**`GlobalIntegrationSettings.php:151`

**Usage:**

php

```
add_filter('fluent_cart/integration/global_notification_feed_email_alerts', function ($feedData) {
    // Modify email alert feed data
    $feedData['recipients'][] = 'extra-admin@example.com';
    return $feedData;
});
```

### ` get_global_integration_actions` [​](https://dev.fluentcart.com/hooks/filters/integrations-and-advanced\#get-global-integration-actions)

`fluent_cart/integration/get_global_integration_actions` - Filter global integration actions

**When it runs:** This filter is applied when retrieving available global integration actions that can be triggered by order events.

**Parameters:**

- `$actions` (array): Array of integration actions (default `[]`)
php

```
$actions = [\
      'mailchimp_subscribe' => [\
          'title' => 'Subscribe to MailChimp',\
          'enabled' => true\
      ]\
];
```


**Returns:**

- `$actions` (array): The modified integration actions array

**Source:**`GlobalIntegrationActionHandler.php:22`

**Usage:**

php

```
add_filter('fluent_cart/integration/get_global_integration_actions', function ($actions) {
    $actions['custom_webhook'] = [\
        'title'   => 'Fire Custom Webhook',\
        'enabled' => true,\
    ];
    return $actions;
});
```

### ` notifying_async_{$feedKey}` [​](https://dev.fluentcart.com/hooks/filters/integrations-and-advanced\#notifying-async-feedkey)

`fluent_cart/integration/notifying_async_{$feedKey}` - Control async notification per feed (DYNAMIC)

**When it runs:** This dynamic filter controls whether a specific notification feed should be dispatched asynchronously. The `{$feedKey}` is replaced with the actual feed key.

**Parameters:**

- `$async` (bool): Whether to process this notification asynchronously (default `true`)

**Returns:**

- `$async` (bool): Whether to use async processing

**Source:**`GlobalNotificationHandler.php:104`

**Usage:**

php

```
add_filter('fluent_cart/integration/notifying_async_email_alerts', function ($async) {
    // Force synchronous for email alerts
    return false;
});
```

* * *

## Integration Settings & Configuration [​](https://dev.fluentcart.com/hooks/filters/integrations-and-advanced\#integration-settings-configuration)

### ` global_integration_settings_{$key}` [​](https://dev.fluentcart.com/hooks/filters/integrations-and-advanced\#global-integration-settings-key)

`fluent_cart/integration/global_integration_settings_{$key}` - Filter integration settings (DYNAMIC)

**When it runs:** This dynamic filter is applied when retrieving settings for a specific integration. The `{$key}` is replaced with the integration key (e.g., `mailchimp`, `zapier`).

**Parameters:**

- `$settings` (array): The integration settings (default `[]`)

**Returns:**

- `$settings` (array): The modified settings array

**Source:**`GlobalIntegrationSettings.php:24`

**Usage:**

php

```
add_filter('fluent_cart/integration/global_integration_settings_mailchimp', function ($settings) {
    // Override MailChimp API key from environment
    $settings['api_key'] = defined('MAILCHIMP_API_KEY') ? MAILCHIMP_API_KEY : $settings['api_key'];
    return $settings;
});
```

### ` global_integration_fields_{$key}` [​](https://dev.fluentcart.com/hooks/filters/integrations-and-advanced\#global-integration-fields-key)

`fluent_cart/integration/global_integration_fields_{$key}` - Filter integration field definitions (DYNAMIC)

**When it runs:** This dynamic filter is applied when retrieving field definitions for a specific integration configuration form. The `{$key}` is replaced with the integration key.

**Parameters:**

- `$fields` (array): The field definitions (default `[]`)

**Returns:**

- `$fields` (array): The modified field definitions

**Source:**`GlobalIntegrationSettings.php:25`

**Usage:**

php

```
add_filter('fluent_cart/integration/global_integration_fields_mailchimp', function ($fields) {
    $fields[] = [\
        'key'   => 'double_optin',\
        'label' => 'Enable Double Opt-in',\
        'type'  => 'checkbox',\
    ];
    return $fields;
});
```

### ` get_integration_defaults_{$name}` [​](https://dev.fluentcart.com/hooks/filters/integrations-and-advanced\#get-integration-defaults-name)

`fluent_cart/integration/get_integration_defaults_{$name}` - Filter integration defaults (DYNAMIC)

**When it runs:** This dynamic filter is applied when retrieving default settings for a specific integration. The `{$name}` is replaced with the integration name.

**Parameters:**

- `$defaults` (array): The default settings values

**Returns:**

- `$defaults` (array): The modified defaults

**Source:**`GlobalIntegrationSettings.php:199,201`

**Usage:**

php

```
add_filter('fluent_cart/integration/get_integration_defaults_mailchimp', function ($defaults) {
    $defaults['list_id'] = 'default_list_123';
    $defaults['tags']    = ['fluentcart-customer'];
    return $defaults;
});
```

### ` get_integration_settings_fields_{$name}` [​](https://dev.fluentcart.com/hooks/filters/integrations-and-advanced\#get-integration-settings-fields-name)

`fluent_cart/integration/get_integration_settings_fields_{$name}` - Filter integration settings fields (DYNAMIC)

**When it runs:** This dynamic filter is applied when retrieving the settings field definitions for a specific integration. The `{$name}` is replaced with the integration name.

**Parameters:**

- `$fields` (array): The field definitions (default `[]`)

**Returns:**

- `$fields` (array): The modified field definitions

**Source:**`GlobalIntegrationSettings.php:204,276`, `IntegrationHelper.php:27`

**Usage:**

php

```
add_filter('fluent_cart/integration/get_integration_settings_fields_zapier', function ($fields) {
    $fields[] = [\
        'key'         => 'webhook_url',\
        'label'       => 'Webhook URL',\
        'type'        => 'url',\
        'required'    => true,\
        'placeholder' => 'https://hooks.zapier.com/...',\
    ];
    return $fields;
});
```

### ` save_integration_values_{$name}` [​](https://dev.fluentcart.com/hooks/filters/integrations-and-advanced\#save-integration-values-name)

`fluent_cart/integration/save_integration_values_{$name}` - Filter before saving integration data (DYNAMIC)

**When it runs:** This dynamic filter is applied just before integration settings are saved to the database. The `{$name}` is replaced with the integration name.

**Parameters:**

- `$integration` (Meta): The Meta model instance containing the integration data

**Returns:**

- `$integration` (Meta): The modified Meta model

**Source:**`GlobalIntegrationSettings.php:248`

**Usage:**

php

```
add_filter('fluent_cart/integration/save_integration_values_mailchimp', function ($integration) {
    // Encrypt API key before saving
    $value = $integration->value;
    if (!empty($value['api_key'])) {
        $value['api_key_encrypted'] = encrypt($value['api_key']);
    }
    $integration->value = $value;
    return $integration;
});
```

### ` get_integration_merge_fields_{$name}` [​](https://dev.fluentcart.com/hooks/filters/integrations-and-advanced\#get-integration-merge-fields-name)

`fluent_cart/integration/get_integration_merge_fields_{$name}` - Filter integration merge/mapping fields (DYNAMIC)

**When it runs:** This dynamic filter is applied when retrieving merge fields for a specific integration. These fields are used for mapping FluentCart data to external service fields.

**Parameters:**

- `$list` (array): The merge fields list
- `$listId` (string): The list or audience ID

**Returns:**

- `$list` (array): The modified merge fields

**Source:**`GlobalIntegrationSettings.php:369`

**Usage:**

php

```
add_filter('fluent_cart/integration/get_integration_merge_fields_mailchimp', function ($list, $listId) {
    $list[] = [\
        'key'   => 'COMPANY',\
        'label' => 'Company Name',\
        'type'  => 'text',\
    ];
    return $list;
}, 10, 2);
```

### ` integration_options_{$key}` [​](https://dev.fluentcart.com/hooks/filters/integrations-and-advanced\#integration-options-key)

`fluent_cart/integration/integration_options_{$key}` - Filter dynamic integration options (DYNAMIC)

**When it runs:** This dynamic filter is applied when retrieving option values for an integration dropdown or selection field. The `{$key}` is replaced with the option key.

**Parameters:**

- `$options` (array): The options array (default `[]`)

**Returns:**

- `$options` (array): The modified options

**Source:**`IntegrationController.php:302`

**Usage:**

php

```
add_filter('fluent_cart/integration/integration_options_mailchimp_lists', function ($options) {
    // Add a custom list option
    $options[] = [\
        'id'    => 'custom_list',\
        'title' => 'Custom Audience',\
    ];
    return $options;
});
```

### ` integration_saving_data_{$provider}` [​](https://dev.fluentcart.com/hooks/filters/integrations-and-advanced\#integration-saving-data-provider)

`fluent_cart/integration/integration_saving_data_{$provider}` - Filter integration data before validation (DYNAMIC)

**When it runs:** This dynamic filter is applied to integration data before it undergoes validation when saving. The `{$provider}` is replaced with the provider key.

**Parameters:**

- `$validatedData` (array): The validated integration data

**Returns:**

- `$validatedData` (array): The modified data

**Source:**`IntegrationHelper.php:62`

**Usage:**

php

```
add_filter('fluent_cart/integration/integration_saving_data_mailchimp', function ($validatedData) {
    // Normalize tags before saving
    if (!empty($validatedData['tags'])) {
        $validatedData['tags'] = array_map('strtolower', $validatedData['tags']);
    }
    return $validatedData;
});
```

### ` editing_integration_{$key}` [​](https://dev.fluentcart.com/hooks/filters/integrations-and-advanced\#editing-integration-key)

`fluent_cart/integration/editing_integration_{$key}` - Filter integration data when editing (DYNAMIC)

**When it runs:** This dynamic filter is applied when an integration is being loaded for editing in the admin UI.

**Parameters:**

- `$data` (array): The integration data for editing
- `$args` (array): Additional context arguments

**Returns:**

- `$data` (array): The modified integration data

**Source:**`IntegrationHelper.php:80`

**Usage:**

php

```
add_filter('fluent_cart/integration/editing_integration_mailchimp', function ($data, $args) {
    // Decrypt API key for display
    if (!empty($data['api_key_encrypted'])) {
        $data['api_key'] = decrypt($data['api_key_encrypted']);
    }
    return $data;
}, 10, 2);
```

* * *

## Integration Addons [​](https://dev.fluentcart.com/hooks/filters/integrations-and-advanced\#integration-addons)

### ` addons` [​](https://dev.fluentcart.com/hooks/filters/integrations-and-advanced\#addons)

`fluent_cart/integration/addons` - Filter the integration addons list

**When it runs:** This filter is applied when retrieving the list of available integration addons in the admin interface.

**Parameters:**

- `$addons` (array): Array of addon definitions

**Returns:**

- `$addons` (array): The modified addons array

**Source:**`AddonsController.php:87`

**Usage:**

php

```
add_filter('fluent_cart/integration/addons', function ($addons) {
    $addons['my_addon'] = [\
        'title'       => 'My Custom Addon',\
        'description' => 'Adds custom integration functionality',\
        'logo'        => 'https://example.com/addon-logo.png',\
        'enabled'     => true,\
    ];
    return $addons;
});
```

### ` installable_repo_plugins` [​](https://dev.fluentcart.com/hooks/filters/integrations-and-advanced\#installable-repo-plugins)

`fluent_cart/installable_repo_plugins` - Filter installable plugin recommendations

**When it runs:** This filter is applied when retrieving the list of recommended plugins that can be installed from within the FluentCart admin.

**Parameters:**

- `$plugins` (array): Array of installable plugin definitions

**Returns:**

- `$plugins` (array): The modified plugins array

**Source:**`AddonsController.php:121`, `GlobalIntegrationSettings.php:396`

**Usage:**

php

```
add_filter('fluent_cart/installable_repo_plugins', function ($plugins) {
    $plugins[] = [\
        'title'       => 'FluentCRM',\
        'slug'        => 'fluent-crm',\
        'description' => 'Email marketing automation',\
        'url'         => 'https://wordpress.org/plugins/fluent-crm/',\
    ];
    return $plugins;
});
```

* * *

## File Storage & Downloads [​](https://dev.fluentcart.com/hooks/filters/integrations-and-advanced\#file-storage-downloads)

### ` local_file_blocked_extensions` [​](https://dev.fluentcart.com/hooks/filters/integrations-and-advanced\#local-file-blocked-extensions)

`fluent_cart/local_file_blocked_extensions` - Filter blocked file extensions for local storage

**When it runs:** This filter is applied when validating a file upload to local storage, allowing you to modify the list of blocked file extensions.

**Parameters:**

- `$blockedExts` (array): Array of blocked file extensions
- `$localFilePath` (string): Local file path
- `$uploadToFilePath` (string): Target upload path
- `$fileInfo` (array): File information array
- Additional context parameters

**Returns:**

- `$blockedExts` (array): The modified blocked extensions array

**Source:**`LocalDriver.php:129`

**Usage:**

php

```
add_filter('fluent_cart/local_file_blocked_extensions', function ($blockedExts, $localFilePath, $uploadToFilePath, $fileInfo) {
    // Block additional extensions
    $blockedExts[] = 'svg';
    $blockedExts[] = 'webp';
    return $blockedExts;
}, 10, 4);
```

### ` download_expiration_minutes` [​](https://dev.fluentcart.com/hooks/filters/integrations-and-advanced\#download-expiration-minutes)

`fluent_cart/download_expiration_minutes` - Filter S3 download link expiration time

**When it runs:** This filter controls how long a pre-signed S3 download URL remains valid.

**Parameters:**

- `$expirationMinutes` (int): Expiration time in minutes
- `$context` (array): Context data
php

```
$context = [\
      'file_path' => 'products/my-file.zip',\
      'bucket'    => 'my-bucket',\
      'driver'    => 's3'\
];
```


**Returns:**

- `$expirationMinutes` (int): The modified expiration time in minutes

**Source:**`S3Driver.php:237,252`

**Usage:**

php

```
add_filter('fluent_cart/download_expiration_minutes', function ($expirationMinutes, $context) {
    // Extend expiration for large files
    if (str_ends_with($context['file_path'], '.zip')) {
        return 120; // 2 hours
    }
    return $expirationMinutes;
}, 10, 2);
```

### ` download_link_validity_in_minutes` [​](https://dev.fluentcart.com/hooks/filters/integrations-and-advanced\#download-link-validity-in-minutes)

`fluent_cart/download_link_validity_in_minutes` - Filter download link validity duration

**When it runs:** This filter controls how long a download link remains valid for customer-facing downloads.

**Parameters:**

- `$minutes` (int): Link validity in minutes (default `60`)
- `$context` (array): Context data
php

```
$context = [\
      'product_download' => $downloadModel,\
      'order_id'         => 123,\
      'is_admin'         => false\
];
```


**Returns:**

- `$minutes` (int): The modified validity in minutes

**Source:**`Helper.php:1430`

**Usage:**

php

```
add_filter('fluent_cart/download_link_validity_in_minutes', function ($minutes, $context) {
    // Give admins longer download windows
    if ($context['is_admin']) {
        return 1440; // 24 hours
    }
    return $minutes;
}, 10, 2);
```

### ` product_download/can_be_downloaded` [​](https://dev.fluentcart.com/hooks/filters/integrations-and-advanced\#product-download-can-be-downloaded)

`fluent_cart/product_download/can_be_downloaded` - Filter whether a file can be downloaded

**When it runs:** This filter is applied during download validation to determine if a customer is allowed to download a specific file.

**Parameters:**

- `$canDownload` (bool\|WP\_Error): Whether the file can be downloaded, or a WP\_Error with rejection reason

**Returns:**

- `$canDownload` (bool\|WP\_Error): The modified download permission

**Source:**`FileDownloader.php:95`

**Usage:**

php

```
add_filter('fluent_cart/product_download/can_be_downloaded', function ($canDownload) {
    // Block downloads during maintenance
    if (get_option('fluent_cart_maintenance_mode')) {
        return new \WP_Error('maintenance', 'Downloads are temporarily disabled during maintenance.');
    }
    return $canDownload;
});
```

### ` get_global_storage_settings_{$driver}` [​](https://dev.fluentcart.com/hooks/filters/integrations-and-advanced\#get-global-storage-settings-driver)

`fluent_cart/storage/get_global_storage_settings_{$driver}` - Filter storage driver settings (DYNAMIC)

**When it runs:** This dynamic filter is applied when retrieving settings for a specific storage driver. The `{$driver}` is replaced with the driver name (e.g., `s3`, `local`).

**Parameters:**

- `$settings` (array): The storage driver settings (default `[]`)

**Returns:**

- `$settings` (array): The modified settings

**Source:**`api/StorageDrivers.php:18`

**Usage:**

php

```
add_filter('fluent_cart/storage/get_global_storage_settings_s3', function ($settings) {
    // Override S3 settings from environment variables
    $settings['bucket'] = defined('S3_BUCKET') ? S3_BUCKET : $settings['bucket'];
    $settings['region'] = defined('S3_REGION') ? S3_REGION : $settings['region'];
    return $settings;
});
```

### ` get_global_storage_drivers` [​](https://dev.fluentcart.com/hooks/filters/integrations-and-advanced\#get-global-storage-drivers)

`fluent_cart/storage/get_global_storage_drivers` - Filter all available storage drivers

**When it runs:** This filter is applied when retrieving the list of all available storage drivers.

**Parameters:**

- `$drivers` (array): Array of storage driver definitions (default `[]`)

**Returns:**

- `$drivers` (array): The modified drivers array

**Source:**`StorageDrivers.php:28`

**Usage:**

php

```
add_filter('fluent_cart/storage/get_global_storage_drivers', function ($drivers) {
    $drivers['backblaze'] = [\
        'title'       => 'Backblaze B2',\
        'description' => 'Store files on Backblaze B2',\
        'handler'     => 'BackblazeDriver',\
    ];
    return $drivers;
});
```

### ` get_global_storage_driver_status_{$driver}` [​](https://dev.fluentcart.com/hooks/filters/integrations-and-advanced\#get-global-storage-driver-status-driver)

`fluent_cart/storage/get_global_storage_driver_status_{$driver}` - Filter storage driver status (DYNAMIC)

**When it runs:** This dynamic filter retrieves the connection status for a specific storage driver.

**Parameters:**

- `$status` (array): The driver status (default `[]`)

**Returns:**

- `$status` (array): The modified status array

**Source:**`StorageDrivers.php:65`

**Usage:**

php

```
add_filter('fluent_cart/storage/get_global_storage_driver_status_s3', function ($status) {
    $status['connected'] = true;
    $status['message']   = 'Connected to S3 bucket successfully';
    return $status;
});
```

### ` verify_driver_connect_info_{$driver}` [​](https://dev.fluentcart.com/hooks/filters/integrations-and-advanced\#verify-driver-connect-info-driver)

`fluent_cart/verify_driver_connect_info_{$driver}` - Filter driver connection verification (DYNAMIC)

**When it runs:** This dynamic filter is applied when verifying the connection info for a storage driver.

**Parameters:**

- `$settings` (array): The driver connection settings

**Returns:**

- `$settings` (array): The modified settings (may include error information)

**Source:**`StorageDrivers.php:79`

**Usage:**

php

```
add_filter('fluent_cart/verify_driver_connect_info_s3', function ($settings) {
    // Validate credentials before saving
    try {
        $client = new \Aws\S3\S3Client($settings);
        $client->listBuckets();
        $settings['verified'] = true;
    } catch (\Exception $e) {
        $settings['error'] = $e->getMessage();
    }
    return $settings;
});
```

### ` storage_settings_before_update_{$slug}` [​](https://dev.fluentcart.com/hooks/filters/integrations-and-advanced\#storage-settings-before-update-slug)

`fluent_cart/storage/storage_settings_before_update_{$slug}` - Filter storage settings before saving (DYNAMIC)

**When it runs:** This dynamic filter is applied just before storage driver settings are saved, allowing you to validate or modify them.

**Parameters:**

- `$settings` (array): The new settings to save
- `$oldSettings` (array): The previous settings

**Returns:**

- `$settings` (array): The modified settings

**Source:**`BaseStorageDriver.php:152`

**Usage:**

php

```
add_filter('fluent_cart/storage/storage_settings_before_update_s3', function ($settings, $oldSettings) {
    // Preserve the secret key if not provided in the update
    if (empty($settings['secret_key']) && !empty($oldSettings['secret_key'])) {
        $settings['secret_key'] = $oldSettings['secret_key'];
    }
    return $settings;
}, 10, 2);
```

* * *

## Localization & Address [​](https://dev.fluentcart.com/hooks/filters/integrations-and-advanced\#localization-address)

### ` country_state_options` [​](https://dev.fluentcart.com/hooks/filters/integrations-and-advanced\#country-state-options)

`fluent_cart/country_state_options` - Filter country and state options

**When it runs:** This filter is applied when retrieving country and state dropdown options for address forms.

**Parameters:**

- `$options` (array): The country/state options array

**Returns:**

- `$options` (array): The modified options

**Source:**`LocalizationManager.php:425`

**Usage:**

php

```
add_filter('fluent_cart/country_state_options', function ($options) {
    // Remove a country from the list
    unset($options['countries']['XX']);
    return $options;
});
```

### ` address/postcode/format` [​](https://dev.fluentcart.com/hooks/filters/integrations-and-advanced\#address-postcode-format)

`fluent_cart/address/postcode/format` - Filter postcode formatting

**When it runs:** This filter is applied when formatting a postcode value, typically during address validation.

**Parameters:**

- `$postcode` (string): The trimmed postcode value
- `$country` (string): The country code

**Returns:**

- `$postcode` (string): The formatted postcode

**Source:**`PostcodeVerification.php:53`

**Usage:**

php

```
add_filter('fluent_cart/address/postcode/format', function ($postcode, $country) {
    // Format UK postcodes with a space
    if ($country === 'GB' && strlen($postcode) > 3 && strpos($postcode, ' ') === false) {
        return substr($postcode, 0, -3) . ' ' . substr($postcode, -3);
    }
    return $postcode;
}, 10, 2);
```

### ` address/postcode/is_valid` [​](https://dev.fluentcart.com/hooks/filters/integrations-and-advanced\#address-postcode-is-valid)

`fluent_cart/address/postcode/is_valid` - Filter postcode validation result

**When it runs:** This filter is applied after postcode validation to allow custom validation rules.

**Parameters:**

- `$valid` (bool): Whether the postcode is valid
- `$postcode` (string): The postcode being validated
- `$country` (string): The country code

**Returns:**

- `$valid` (bool): The modified validation result

**Source:**`PostcodeVerification.php:154`

**Usage:**

php

```
add_filter('fluent_cart/address/postcode/is_valid', function ($valid, $postcode, $country) {
    // Add custom validation for specific country
    if ($country === 'XX') {
        return preg_match('/^\d{5}$/', $postcode) === 1;
    }
    return $valid;
}, 10, 3);
```

### ` util/countries` [​](https://dev.fluentcart.com/hooks/filters/integrations-and-advanced\#util-countries)

`fluent-cart/util/countries` - Filter the country list

**When it runs:** This filter is applied when retrieving the full list of countries.

> **Note:** This hook uses a non-standard hyphenated prefix (`fluent-cart/`) rather than the standard `fluent_cart/` convention. This is a legacy naming that may be standardized in a future release.

**Parameters:**

- `$options` (array): Array of country code => country name pairs

**Returns:**

- `$options` (array): The modified country list

**Source:**`Helper.php:1140`

**Usage:**

php

```
add_filter('fluent-cart/util/countries', function ($options) {
    // Limit to specific countries
    return array_intersect_key($options, array_flip(['US', 'CA', 'GB', 'AU']));
});
```

* * *

## Templates & Frontend [​](https://dev.fluentcart.com/hooks/filters/integrations-and-advanced\#templates-frontend)

### ` template/disable_taxonomy_fallback` [​](https://dev.fluentcart.com/hooks/filters/integrations-and-advanced\#template-disable-taxonomy-fallback)

`fluent_cart/template/disable_taxonomy_fallback` - Disable taxonomy fallback template

**When it runs:** This filter controls whether the taxonomy fallback template should be disabled.

**Parameters:**

- `$disable` (bool): Whether to disable taxonomy fallback (default `false`)

**Returns:**

- `$disable` (bool): The modified value

**Source:**`TemplateLoader.php:113`

**Usage:**

php

```
add_filter('fluent_cart/template/disable_taxonomy_fallback', function ($disable) {
    // Disable taxonomy fallback when using a custom theme
    return true;
});
```

### ` has_block_template` [​](https://dev.fluentcart.com/hooks/filters/integrations-and-advanced\#has-block-template)

`fluent_cart/has_block_template` - Filter block template existence check

**When it runs:** This filter is applied when checking if a block template exists for the current page.

**Parameters:**

- `$hasTemplate` (bool): Whether a block template exists

**Returns:**

- `$hasTemplate` (bool): The modified result

**Source:**`TemplateLoader.php:193`

**Usage:**

php

```
add_filter('fluent_cart/has_block_template', function ($hasTemplate) {
    // Force classic template rendering
    return false;
});
```

### ` template_loader_files` [​](https://dev.fluentcart.com/hooks/filters/integrations-and-advanced\#template-loader-files)

`fluent_cart/template_loader_files` - Filter template files to load

**When it runs:** This filter is applied when determining which template files should be loaded for the current request.

**Parameters:**

- `$files` (array): Array of template file paths (default `[]`)

**Returns:**

- `$files` (array): The modified template files array

**Source:**`TemplateLoader.php:206`

**Usage:**

php

```
add_filter('fluent_cart/template_loader_files', function ($files) {
    // Add custom template file
    $files[] = get_stylesheet_directory() . '/fluent-cart/custom-template.php';
    return $files;
});
```

### ` template_path` [​](https://dev.fluentcart.com/hooks/filters/integrations-and-advanced\#template-path)

`fluent_cart/template_path` - Filter theme template path

**When it runs:** This filter controls the directory path within a theme where FluentCart template overrides are located.

**Parameters:**

- `$path` (string): The template directory path (default `'fluent-cart/'`)

**Returns:**

- `$path` (string): The modified template path

**Source:**`TemplateLoader.php:248`

**Usage:**

php

```
add_filter('fluent_cart/template_path', function ($path) {
    // Use a custom directory for template overrides
    return 'my-store/templates/';
});
```

### ` fluent_cart_template_part_content` [​](https://dev.fluentcart.com/hooks/filters/integrations-and-advanced\#fluent-cart-template-part-content)

`fluent_cart_template_part_content` - Filter template part content

**When it runs:** This filter is applied to template part content before it is rendered, allowing you to modify the HTML content.

**Parameters:**

- `$content` (string): The template part content
- `$slug` (string): The template part slug
- `$args` (array): Template arguments

**Returns:**

- `$content` (string): The modified content

**Source:**`ProductModalTemplatePart.php:245`

**Usage:**

php

```
add_filter('fluent_cart_template_part_content', function ($content, $slug, $args) {
    if ($slug === 'product-card') {
        // Wrap content in a custom div
        $content = '<div class="custom-wrapper">' . $content . '</div>';
    }
    return $content;
}, 10, 3);
```

### ` fluent_cart_template_part_content_{$slug}` [​](https://dev.fluentcart.com/hooks/filters/integrations-and-advanced\#fluent-cart-template-part-content-slug)

`fluent_cart_template_part_content_{$slug}` - Filter template part content by slug (DYNAMIC)

**When it runs:** This dynamic filter is applied to a specific template part's content. The `{$slug}` is replaced with the template part slug.

**Parameters:**

- `$content` (string): The template part content
- `$args` (array): Template arguments

**Returns:**

- `$content` (string): The modified content

**Source:**`ProductModalTemplatePart.php:246`

**Usage:**

php

```
add_filter('fluent_cart_template_part_content_product-card', function ($content, $args) {
    // Append a badge to product card content
    $content .= '<span class="badge">New</span>';
    return $content;
}, 10, 2);
```

### ` fluent_cart_template_part_output` [​](https://dev.fluentcart.com/hooks/filters/integrations-and-advanced\#fluent-cart-template-part-output)

`fluent_cart_template_part_output` - Filter template part output

**When it runs:** This filter is applied to the final rendered output of a template part.

**Parameters:**

- `$output` (string): The rendered template part output

**Returns:**

- `$output` (string): The modified output

**Source:**`ProductModalTemplatePart.php:252`

**Usage:**

php

```
add_filter('fluent_cart_template_part_output', function ($output) {
    // Minify the output
    return preg_replace('/\s+/', ' ', $output);
});
```

### ` fluent_cart_template_part_output_{$slug}` [​](https://dev.fluentcart.com/hooks/filters/integrations-and-advanced\#fluent-cart-template-part-output-slug)

`fluent_cart_template_part_output_{$slug}` - Filter template part output by slug (DYNAMIC)

**When it runs:** This dynamic filter is applied to the final rendered output of a specific template part. The `{$slug}` is replaced with the template part slug.

**Parameters:**

- `$output` (string): The rendered output

**Returns:**

- `$output` (string): The modified output

**Source:**`ProductModalTemplatePart.php:253`

**Usage:**

php

```
add_filter('fluent_cart_template_part_output_product-modal', function ($output) {
    // Add data attributes to the modal output
    return str_replace('<div class="fct-modal"', '<div class="fct-modal" data-tracking="true"', $output);
});
```

### ` buttons/enable_floating_cart_button` [​](https://dev.fluentcart.com/hooks/filters/integrations-and-advanced\#buttons-enable-floating-cart-button)

`fluent_cart/buttons/enable_floating_cart_button` - Filter floating cart button visibility

**When it runs:** This filter controls whether the floating cart button is displayed on the frontend.

**Parameters:**

- `$enabled` (bool): Whether the floating cart button is enabled (default `true`)

**Returns:**

- `$enabled` (bool): The modified value

**Source:**`app/Hooks/Cart/CartLoader.php:41`

**Usage:**

php

```
add_filter('fluent_cart/buttons/enable_floating_cart_button', function ($enabled) {
    // Disable floating cart on specific pages
    if (is_page('landing-page')) {
        return false;
    }
    return $enabled;
});
```

* * *

## Widgets & Dashboard [​](https://dev.fluentcart.com/hooks/filters/integrations-and-advanced\#widgets-dashboard)

### ` {$widgetName}` [​](https://dev.fluentcart.com/hooks/filters/integrations-and-advanced\#widgetname)

`fluent_cart/{$widgetName}` - Filter widget data by name (DYNAMIC)

**When it runs:** This dynamic filter is applied when a dashboard widget retrieves its data. The `{$widgetName}` is replaced with the specific widget name.

**Parameters:**

- `$widgetData` (mixed): The widget data returned by `widgetData()` method

**Returns:**

- `$widgetData` (mixed): The modified widget data

**Source:**`app/Services/Widgets/BaseWidget.php:16`

**Usage:**

php

```
add_filter('fluent_cart/revenue_widget', function ($widgetData) {
    // Add custom metric to revenue widget
    $widgetData['custom_metric'] = calculate_custom_metric();
    return $widgetData;
});
```

### ` widgets/{$filter}` [​](https://dev.fluentcart.com/hooks/filters/integrations-and-advanced\#widgets-filter)

`fluent_cart/widgets/{$filter}` - Filter widget data by filter key (DYNAMIC)

**When it runs:** This dynamic filter is applied when retrieving widget data for a specific filter key in the widgets controller.

**Parameters:**

- `$result` (array): The widget result data (default `[]`)
- `$data` (array): The request data

**Returns:**

- `$result` (array): The modified widget data

**Source:**`WidgetsController.php:36`

**Usage:**

php

```
add_filter('fluent_cart/widgets/sales_overview', function ($result, $data) {
    $result['custom_chart'] = [\
        'labels' => ['Jan', 'Feb', 'Mar'],\
        'data'   => [100, 200, 150],\
    ];
    return $result;
}, 10, 2);
```

### ` promo_gateways` [​](https://dev.fluentcart.com/hooks/filters/integrations-and-advanced\#promo-gateways)

`fluent_cart/promo_gateways` - Filter promotional gateways

**When it runs:** This filter is applied when retrieving the list of promotional payment gateways shown in the admin.

**Parameters:**

- `$defaultGateways` (array): Array of default promotional gateways

**Returns:**

- `$defaultGateways` (array): The modified gateways array

**Source:**`PromoGatewaysHandler.php:36`

**Usage:**

php

```
add_filter('fluent_cart/promo_gateways', function ($gateways) {
    // Remove a promo gateway
    unset($gateways['example_gateway']);
    return $gateways;
});
```

### ` addon_gateways` [​](https://dev.fluentcart.com/hooks/filters/integrations-and-advanced\#addon-gateways)

`fluent_cart/addon_gateways` - Filter addon payment gateways

**When it runs:** This filter is applied when retrieving the list of addon payment gateways.

**Parameters:**

- `$defaultGateways` (array): Array of default addon gateways

**Returns:**

- `$defaultGateways` (array): The modified gateways array

**Source:**`AddonGatewaysHandler.php:36`

**Usage:**

php

```
add_filter('fluent_cart/addon_gateways', function ($gateways) {
    $gateways['custom_pay'] = [\
        'title'       => 'Custom Pay',\
        'description' => 'Custom payment gateway addon',\
        'is_active'   => true,\
    ];
    return $gateways;
});
```

* * *

## Advanced List Filters [​](https://dev.fluentcart.com/hooks/filters/integrations-and-advanced\#advanced-list-filters)

### ` {$filter}_list_filter_query` [​](https://dev.fluentcart.com/hooks/filters/integrations-and-advanced\#filter-list-filter-query)

`fluent_cart/{$filter}_list_filter_query` - Filter list filter query (DYNAMIC)

**When it runs:** This dynamic filter is applied when building database queries for filtered list pages (orders, customers, subscriptions, etc.). The `{$filter}` is replaced with the filter context name.

**Parameters:**

- `$query` (Builder): The Eloquent query builder instance

**Returns:**

- `$query` (Builder): The modified query builder

**Source:**`BaseFilter.php:962,971`

**Usage:**

php

```
add_filter('fluent_cart/orders_list_filter_query', function ($query) {
    // Only show orders from the last 30 days by default
    $query->where('created_at', '>=', gmdate('Y-m-d H:i:s', strtotime('-30 days')));
    return $query;
});
```

### ` {$filterName}_filter_options` [​](https://dev.fluentcart.com/hooks/filters/integrations-and-advanced\#filtername-filter-options)

`fluent_cart/{$filterName}_filter_options` - Filter options for list page filters (DYNAMIC)

**When it runs:** This dynamic filter is applied when retrieving available filter options for admin list pages.

**Parameters:**

- `$options` (array): The filter options array

**Returns:**

- `$options` (array): The modified filter options

**Source:**`BaseFilter.php:995`

**Usage:**

php

```
add_filter('fluent_cart/orders_filter_options', function ($options) {
    // Add a custom filter option
    $options['custom_status'] = [\
        'label'   => 'Custom Status',\
        'type'    => 'select',\
        'options' => ['pending_review' => 'Pending Review'],\
    ];
    return $options;
});
```

### ` {$filterName}_table_columns` [​](https://dev.fluentcart.com/hooks/filters/integrations-and-advanced\#filtername-table-columns)

`fluent_cart/{$filterName}_table_columns` - Filter table columns for list pages (DYNAMIC)

**When it runs:** This dynamic filter is applied when retrieving table column definitions for admin list pages.

**Parameters:**

- `$columns` (array): The table column definitions (default `[]`)

**Returns:**

- `$columns` (array): The modified columns array

**Source:**`BaseFilter.php:1038`

**Usage:**

php

```
add_filter('fluent_cart/orders_table_columns', function ($columns) {
    $columns['custom_field'] = [\
        'label'    => 'Custom Field',\
        'sortable' => true,\
        'width'    => '120px',\
    ];
    return $columns;
});
```

### ` advanced_filter_options_{$dataKey}` [​](https://dev.fluentcart.com/hooks/filters/integrations-and-advanced\#advanced-filter-options-datakey)

`fluent_cart/advanced_filter_options_{$dataKey}` - Filter advanced filter options (DYNAMIC)

**When it runs:** This dynamic filter is applied when retrieving options for the advanced filter UI. The `{$dataKey}` is replaced with the specific data key.

**Parameters:**

- `$options` (array): The filter options

**Returns:**

- `$options` (array): The modified options

**Source:**`AdvanceFilterController.php:46`

**Usage:**

php

```
add_filter('fluent_cart/advanced_filter_options_payment_methods', function ($options) {
    $options[] = [\
        'value' => 'custom_gateway',\
        'label' => 'Custom Gateway',\
    ];
    return $options;
});
```

* * *

## Plugin Installer [​](https://dev.fluentcart.com/hooks/filters/integrations-and-advanced\#plugin-installer)

### ` outside_addon/handle_cdn_install` [​](https://dev.fluentcart.com/hooks/filters/integrations-and-advanced\#outside-addon-handle-cdn-install)

`fluent_cart/outside_addon/handle_cdn_install` - Filter CDN addon installation

**When it runs:** This filter is applied when attempting to install an addon from a CDN source. Return a non-null value to handle the installation yourself.

**Parameters:**

- `$result` (mixed): Installation result (default `null`)

**Returns:**

- `$result` (mixed): The installation result, or `null` to use default handling

**Source:**`BackgroundInstaller.php:143`

**Usage:**

php

```
add_filter('fluent_cart/outside_addon/handle_cdn_install', function ($result) {
    // Handle custom CDN addon installation
    if ($result === null) {
        // Perform custom installation logic
        return ['success' => true, 'message' => 'Installed from custom CDN'];
    }
    return $result;
});
```

### ` outside_addon/handle_install` [​](https://dev.fluentcart.com/hooks/filters/integrations-and-advanced\#outside-addon-handle-install)

`fluent_cart/outside_addon/handle_install` - Filter external addon installation

**When it runs:** This filter is applied when installing an addon from an external source. Return a non-null value to handle the installation yourself.

**Parameters:**

- `$result` (mixed): Installation result (default `null`)

**Returns:**

- `$result` (mixed): The installation result, or `null` to use default handling

**Source:**`BackgroundInstaller.php:164`

**Usage:**

php

```
add_filter('fluent_cart/outside_addon/handle_install', function ($result) {
    // Handle custom external addon installation
    return ['success' => true, 'message' => 'Addon installed successfully'];
});
```

* * *

## Pro: Licensing API Pro [​](https://dev.fluentcart.com/hooks/filters/integrations-and-advanced\#pro-licensing-api)

### ` license/checking_error` [​](https://dev.fluentcart.com/hooks/filters/integrations-and-advanced\#license-checking-error)

`fluent_cart/license/checking_error`Pro - Filter license check error response

**When it runs:** This filter is applied when a license check encounters an error, allowing you to customize the error response.

**Parameters:**

- `$error` (array): The error response array

**Returns:**

- `$error` (array): The modified error response

**Source:**`LicenseApiHandler.php:45,56`

**Usage:**

php

```
add_filter('fluent_cart/license/checking_error', function ($error) {
    // Customize error message
    $error['message'] = 'Please contact support for license verification.';
    return $error;
});
```

### ` license/check_item_id` [​](https://dev.fluentcart.com/hooks/filters/integrations-and-advanced\#license-check-item-id)

`fluent_cart/license/check_item_id`Pro - Filter item ID validation during license check

**When it runs:** This filter controls whether the item ID should be validated during a license check API request.

**Parameters:**

- `$checkItemId` (bool): Whether to check the item ID (default `true`)

**Returns:**

- `$checkItemId` (bool): The modified value

**Source:**`LicenseApiHandler.php:54`

**Usage:**

php

```
add_filter('fluent_cart/license/check_item_id', function ($checkItemId) {
    // Skip item ID check for specific scenarios
    return false;
});
```

### ` license/check_license_response` [​](https://dev.fluentcart.com/hooks/filters/integrations-and-advanced\#license-check-license-response)

`fluent_cart/license/check_license_response`Pro - Filter license check API response

**When it runs:** This filter is applied to the license check API response before it is returned to the client.

**Parameters:**

- `$returnData` (array): The license check response data

**Returns:**

- `$returnData` (array): The modified response data

**Source:**`LicenseApiHandler.php:83`

**Usage:**

php

```
add_filter('fluent_cart/license/check_license_response', function ($returnData) {
    // Add custom data to the response
    $returnData['support_url'] = 'https://example.com/support';
    return $returnData;
});
```

### ` license/activate_license_response` [​](https://dev.fluentcart.com/hooks/filters/integrations-and-advanced\#license-activate-license-response)

`fluent_cart/license/activate_license_response`Pro - Filter license activation API response

**When it runs:** This filter is applied to the license activation API response before it is returned to the client.

**Parameters:**

- `$returnData` (array): The activation response data

**Returns:**

- `$returnData` (array): The modified response data

**Source:**`LicenseApiHandler.php:170,274`

**Usage:**

php

```
add_filter('fluent_cart/license/activate_license_response', function ($returnData) {
    // Add activation timestamp
    $returnData['activated_at'] = gmdate('Y-m-d H:i:s');
    return $returnData;
});
```

### ` license/deactivate_license_response` [​](https://dev.fluentcart.com/hooks/filters/integrations-and-advanced\#license-deactivate-license-response)

`fluent_cart/license/deactivate_license_response`Pro - Filter license deactivation API response

**When it runs:** This filter is applied to the license deactivation API response before it is returned to the client.

**Parameters:**

- `$returnData` (array): The deactivation response data

**Returns:**

- `$returnData` (array): The modified response data

**Source:**`LicenseApiHandler.php:356`

**Usage:**

php

```
add_filter('fluent_cart/license/deactivate_license_response', function ($returnData) {
    // Add deactivation notice
    $returnData['notice'] = 'License deactivated. You can reactivate on another site.';
    return $returnData;
});
```

### ` license/get_version_response` [​](https://dev.fluentcart.com/hooks/filters/integrations-and-advanced\#license-get-version-response)

`fluent_cart/license/get_version_response`Pro - Filter version check API response

**When it runs:** This filter is applied to the version check API response, allowing you to modify changelog or update information.

**Parameters:**

- `$changeLogData` (array): The version/changelog response data

**Returns:**

- `$changeLogData` (array): The modified response data

**Source:**`LicenseApiHandler.php:463`

**Usage:**

php

```
add_filter('fluent_cart/license/get_version_response', function ($changeLogData) {
    // Append custom changelog entry
    $changeLogData['sections']['changelog'] .= "\n* Custom patch applied";
    return $changeLogData;
});
```

### ` license/santized_url` [​](https://dev.fluentcart.com/hooks/filters/integrations-and-advanced\#license-santized-url)

`fluent_cart/license/santized_url`Pro - Filter sanitized URL for license validation

**When it runs:** This filter is applied when sanitizing a site URL during license activation or validation.

**Parameters:**

- `$url` (string): The sanitized URL
- `$originalUrl` (string): The original URL before sanitization

**Returns:**

- `$url` (string): The modified sanitized URL

**Source:**`LicenseHelper.php:36`

**Usage:**

php

```
add_filter('fluent_cart/license/santized_url', function ($url, $originalUrl) {
    // Normalize www subdomain
    return str_replace('://www.', '://', $url);
}, 10, 2);
```

* * *

## Pro: License Validation & Staging Pro [​](https://dev.fluentcart.com/hooks/filters/integrations-and-advanced\#pro-license-validation-staging)

### ` fluent_cart_sl/is_local_site` [​](https://dev.fluentcart.com/hooks/filters/integrations-and-advanced\#fluent-cart-sl-is-local-site)

`fluent_cart_sl/is_local_site`Pro - Filter local/staging site detection

**When it runs:** This filter is applied when determining if the current site is a local or staging environment for licensing purposes.

**Parameters:**

- `$isLocal` (bool): Whether the site is detected as local
- `$context` (array): Context data
php

```
$context = [\
      'url'  => 'https://staging.example.com',\
      'site' => 'staging.example.com'\
];
```


**Returns:**

- `$isLocal` (bool): The modified detection result

**Source:**`fluent-cart-pro/.../LicenseSite.php:69`

**Usage:**

php

```
add_filter('fluent_cart_sl/is_local_site', function ($isLocal, $context) {
    // Mark custom staging domains as local
    if (str_contains($context['url'], '.staging.')) {
        return true;
    }
    return $isLocal;
}, 10, 2);
```

### ` license/staging_subdomain_patterns` [​](https://dev.fluentcart.com/hooks/filters/integrations-and-advanced\#license-staging-subdomain-patterns)

`fluent_cart/license/staging_subdomain_patterns`Pro - Filter staging subdomain patterns

**When it runs:** This filter is applied when checking if a URL matches known staging subdomain patterns.

**Parameters:**

- `$patterns` (array): Array of subdomain patterns that indicate staging sites

**Returns:**

- `$patterns` (array): The modified patterns array

**Source:**`LicenseHelper.php:619`

**Usage:**

php

```
add_filter('fluent_cart/license/staging_subdomain_patterns', function ($patterns) {
    $patterns[] = 'dev-';
    $patterns[] = 'test-';
    return $patterns;
});
```

### ` license/staging_subfolder_patterns` [​](https://dev.fluentcart.com/hooks/filters/integrations-and-advanced\#license-staging-subfolder-patterns)

`fluent_cart/license/staging_subfolder_patterns`Pro - Filter staging subfolder patterns

**When it runs:** This filter is applied when checking if a URL matches known staging subfolder patterns.

**Parameters:**

- `$patterns` (array): Array of subfolder patterns that indicate staging sites

**Returns:**

- `$patterns` (array): The modified patterns array

**Source:**`LicenseHelper.php:620`

**Usage:**

php

```
add_filter('fluent_cart/license/staging_subfolder_patterns', function ($patterns) {
    $patterns[] = '/staging/';
    $patterns[] = '/test-site/';
    return $patterns;
});
```

### ` license/staging_domains` [​](https://dev.fluentcart.com/hooks/filters/integrations-and-advanced\#license-staging-domains)

`fluent_cart/license/staging_domains`Pro - Filter hosting provider staging domains

**When it runs:** This filter is applied when checking if a URL belongs to a known hosting provider's staging domain.

**Parameters:**

- `$domains` (array): Array of hosting provider staging domain patterns

**Returns:**

- `$domains` (array): The modified domains array

**Source:**`LicenseHelper.php:621`

**Usage:**

php

```
add_filter('fluent_cart/license/staging_domains', function ($domains) {
    $domains[] = 'mystaginghost.com';
    $domains[] = 'preview.myhost.io';
    return $domains;
});
```

### ` license/is_staging_site_result` [​](https://dev.fluentcart.com/hooks/filters/integrations-and-advanced\#license-is-staging-site-result)

`fluent_cart/license/is_staging_site_result`Pro - Filter final staging site detection result

**When it runs:** This filter is applied after all staging detection checks, providing the final determination of whether a site is a staging environment.

**Parameters:**

- `$isStaging` (bool): Whether the site is detected as staging (default `false`)
- `$url` (string): The site URL being checked

**Returns:**

- `$isStaging` (bool): The modified staging detection result

**Source:**`LicenseHelper.php:657`

**Usage:**

php

```
add_filter('fluent_cart/license/is_staging_site_result', function ($isStaging, $url) {
    // Override staging detection for specific domains
    if (str_contains($url, 'mycompany-staging.com')) {
        return true;
    }
    return $isStaging;
}, 10, 2);
```

* * *

## Pro: License Configuration Pro [​](https://dev.fluentcart.com/hooks/filters/integrations-and-advanced\#pro-license-configuration)

### ` license/validity_by_variation` [​](https://dev.fluentcart.com/hooks/filters/integrations-and-advanced\#license-validity-by-variation)

`fluent_cart/license/validity_by_variation`Pro - Filter license validity per variation

**When it runs:** This filter is applied when determining license validity settings for a specific product variation.

**Parameters:**

- `$validity` (array): The validity settings
- `$context` (array): Context data
php

```
$context = [\
      'variation' => $variationModel\
];
```


**Returns:**

- `$validity` (array): The modified validity settings

**Source:**`ProductLicenseController.php:74`

**Usage:**

php

```
add_filter('fluent_cart/license/validity_by_variation', function ($validity, $context) {
    // Set custom validity for premium variations
    $variation = $context['variation'];
    if ($variation->slug === 'premium') {
        $validity['duration'] = 365;
        $validity['unit']     = 'days';
    }
    return $validity;
}, 10, 2);
```

### ` licensing/delete_license_on_order_deleted` [​](https://dev.fluentcart.com/hooks/filters/integrations-and-advanced\#licensing-delete-license-on-order-deleted)

`fluent_cart/licensing/delete_license_on_order_deleted`Pro - Filter whether to delete license when order is deleted

**When it runs:** This filter controls whether associated licenses should be deleted when an order is deleted.

**Parameters:**

- `$delete` (bool): Whether to delete the license (default `true`)

**Returns:**

- `$delete` (bool): The modified value

**Source:**`license-actions.php:117`

**Usage:**

php

```
add_filter('fluent_cart/licensing/delete_license_on_order_deleted', function ($delete) {
    // Preserve licenses even when orders are deleted
    return false;
});
```

### ` licensing/revoke_license_on_payment_failed` [​](https://dev.fluentcart.com/hooks/filters/integrations-and-advanced\#licensing-revoke-license-on-payment-failed)

`fluent_cart/licensing/revoke_license_on_payment_failed`Pro - Filter whether to revoke license on payment failure

**When it runs:** This filter controls whether a license should be revoked when a payment fails.

**Parameters:**

- `$revoke` (bool): Whether to revoke the license (default `true`)

**Returns:**

- `$revoke` (bool): The modified value

**Source:**`LicenseGenerationHandler.php:123`

**Usage:**

php

```
add_filter('fluent_cart/licensing/revoke_license_on_payment_failed', function ($revoke) {
    // Give a grace period instead of immediate revocation
    return false;
});
```

### ` licensing/license_create_data` [​](https://dev.fluentcart.com/hooks/filters/integrations-and-advanced\#licensing-license-create-data)

`fluent_cart/licensing/license_create_data`Pro - Filter license creation data

**When it runs:** This filter is applied when constructing the data for a new license before it is saved to the database.

**Parameters:**

- `$data` (array): The license creation data
- `$context` (array): Context data
php

```
$context = [\
      'order'        => $orderModel,\
      'variation'    => $variationModel,\
      'subscription' => $subscriptionModel\
];
```


**Returns:**

- `$data` (array): The modified license data

**Source:**`LicenseGenerationHandler.php:521`

**Usage:**

php

```
add_filter('fluent_cart/licensing/license_create_data', function ($data, $context) {
    // Set custom activation limit based on variation
    $variation = $context['variation'];
    if ($variation->slug === 'enterprise') {
        $data['activation_limit'] = 100;
    }
    return $data;
}, 10, 2);
```

### ` license/expiration_date_by_variation` [​](https://dev.fluentcart.com/hooks/filters/integrations-and-advanced\#license-expiration-date-by-variation)

`fluent_cart/license/expiration_date_by_variation`Pro - Filter license expiration date

**When it runs:** This filter is applied when calculating the license expiration date for a specific product variation.

**Parameters:**

- `$timestamp` (int\|false): The expiration timestamp, or `false` for no expiration
- `$context` (array): Context data
php

```
$context = [\
      'variation'  => $variationModel,\
      'trial_days' => 14\
];
```


**Returns:**

- `$timestamp` (int\|false): The modified expiration timestamp

**Source:**`LicenseHelper.php:81`

**Usage:**

php

```
add_filter('fluent_cart/license/expiration_date_by_variation', function ($timestamp, $context) {
    // Add extra 30 days for trial users
    if ($context['trial_days'] > 0 && $timestamp) {
        return $timestamp + (30 * DAY_IN_SECONDS);
    }
    return $timestamp;
}, 10, 2);
```

### ` license/default_validity_by_variation` [​](https://dev.fluentcart.com/hooks/filters/integrations-and-advanced\#license-default-validity-by-variation)

`fluent_cart/license/default_validity_by_variation`Pro - Filter default license validity

**When it runs:** This filter is applied when retrieving the default license validity settings for a product variation.

**Parameters:**

- `$validity` (array): The default validity settings
php

```
$validity = [\
      'unit'  => 'years',\
      'value' => 1\
];
```

- `$context` (array): Context data
php

```
$context = [\
      'variation' => $variationModel\
];
```


**Returns:**

- `$validity` (array): The modified validity settings

**Source:**`LicenseHelper.php:418`

**Usage:**

php

```
add_filter('fluent_cart/license/default_validity_by_variation', function ($validity, $context) {
    // Set lifetime validity for specific variations
    $variation = $context['variation'];
    if ($variation->slug === 'lifetime') {
        return ['unit' => 'years', 'value' => 100];
    }
    return $validity;
}, 10, 2);
```

### ` license/grace_period_in_days` [​](https://dev.fluentcart.com/hooks/filters/integrations-and-advanced\#license-grace-period-in-days)

`fluent_cart/license/grace_period_in_days`Pro - Filter license grace period

**When it runs:** This filter controls the number of grace period days after a license expires before it is fully revoked.

**Parameters:**

- `$days` (int): The grace period in days (default `15`)

**Returns:**

- `$days` (int): The modified grace period

**Source:**`LicenseHelper.php:687`

**Usage:**

php

```
add_filter('fluent_cart/license/grace_period_in_days', function ($days) {
    // Extend grace period to 30 days
    return 30;
});
```

### ` fluent_cart_sl/generate_license_key` [​](https://dev.fluentcart.com/hooks/filters/integrations-and-advanced\#fluent-cart-sl-generate-license-key)

`fluent_cart_sl/generate_license_key`Pro - Filter license key generation

**When it runs:** This filter is applied when generating a new license key, allowing you to customize the key format.

**Parameters:**

- `$key` (string): The generated license key (MD5 hash by default)
- `$context` (array): Context data
php

```
$context = [\
      'data' => $licenseData\
];
```


**Returns:**

- `$key` (string): The modified license key

**Source:**`UUID.php:32`

**Usage:**

php

```
add_filter('fluent_cart_sl/generate_license_key', function ($key, $context) {
    // Use a formatted license key
    $key = strtoupper($key);
    return implode('-', str_split($key, 8));
}, 10, 2);
```

### ` fluent_cart_sl_encoded_package_url` [​](https://dev.fluentcart.com/hooks/filters/integrations-and-advanced\#fluent-cart-sl-encoded-package-url)

`fluent_cart_sl_encoded_package_url`Pro - Filter encoded download package URL

**When it runs:** This filter is applied to the encoded package download URL returned during update checks.

**Parameters:**

- `$package_url` (string): The encoded package URL

**Returns:**

- `$package_url` (string): The modified package URL

**Source:**`LicenseManager.php:152`

**Usage:**

php

```
add_filter('fluent_cart_sl_encoded_package_url', function ($package_url) {
    // Route downloads through a CDN
    return str_replace('https://example.com', 'https://cdn.example.com', $package_url);
});
```

### ` fluent_cart_sl/issue_license_data` [​](https://dev.fluentcart.com/hooks/filters/integrations-and-advanced\#fluent-cart-sl-issue-license-data)

`fluent_cart_sl/issue_license_data`Pro - Filter license issue data

**When it runs:** This filter is applied to license data when issuing a new license through the license manager.

**Parameters:**

- `$data` (array): The license issue data

**Returns:**

- `$data` (array): The modified license data

**Source:**`LicenseManager.php:257`

**Usage:**

php

```
add_filter('fluent_cart_sl/issue_license_data', function ($data) {
    // Set default activation limit
    if (empty($data['activation_limit'])) {
        $data['activation_limit'] = 5;
    }
    return $data;
});
```

### ` fluentcart/sanitize_user_meta` [​](https://dev.fluentcart.com/hooks/filters/integrations-and-advanced\#fluentcart-sanitize-user-meta)

`fluentcart/sanitize_user_meta`Pro - Filter user metadata sanitization

**When it runs:** This filter controls whether a specific user meta field should be sanitized during processing.

> **Note:** This hook uses a non-standard prefix (`fluentcart/`) rather than the standard `fluent_cart/` convention. This is a legacy naming that may be standardized in a future release.

**Parameters:**

- `$sanitize` (bool): Whether to sanitize the field (default `true`)
- `$metaFieldName` (string): The meta field name
- `$metaData` (mixed): The meta data value

**Returns:**

- `$sanitize` (bool): Whether to sanitize

**Source:**`WPUserConnect.php:219`

**Usage:**

php

```
add_filter('fluentcart/sanitize_user_meta', function ($sanitize, $metaFieldName, $metaData) {
    // Skip sanitization for specific fields
    if ($metaFieldName === 'custom_html_field') {
        return false;
    }
    return $sanitize;
}, 10, 3);
```

* * *

## Pro: Plugin Updater Pro [​](https://dev.fluentcart.com/hooks/filters/integrations-and-advanced\#pro-plugin-updater)

### ` fluent_sl/api_request_query_params` [​](https://dev.fluentcart.com/hooks/filters/integrations-and-advanced\#fluent-sl-api-request-query-params)

`fluent_sl/api_request_query_params`Pro - Filter API request query parameters

**When it runs:** This filter is applied when building query parameters for license API requests (update checks, activations, etc.).

**Parameters:**

- `$params` (array): The query parameters array

**Returns:**

- `$params` (array): The modified query parameters

**Source:**`PluginUpdater.php:234`

**Usage:**

php

```
add_filter('fluent_sl/api_request_query_params', function ($params) {
    // Add custom tracking parameter
    $params['php_version'] = phpversion();
    $params['wp_version']  = get_bloginfo('version');
    return $params;
});
```

### ` fluent_sl/updater_payload_{$slug}` [​](https://dev.fluentcart.com/hooks/filters/integrations-and-advanced\#fluent-sl-updater-payload-slug)

`fluent_sl/updater_payload_{$slug}`Pro - Filter update check payload (DYNAMIC)

**When it runs:** This dynamic filter is applied to the update check payload for a specific plugin slug. The `{$slug}` is replaced with the plugin's slug.

**Parameters:**

- `$payload` (array): The update check payload

**Returns:**

- `$payload` (array): The modified payload

**Source:**`PluginUpdater.php:251`

**Usage:**

php

```
add_filter('fluent_sl/updater_payload_fluent-cart-pro', function ($payload) {
    // Add environment info to update payload
    $payload['server_software'] = $_SERVER['SERVER_SOFTWARE'] ?? 'unknown';
    return $payload;
});
```

* * *

Today

Hi! I’m your AI assistant. How can I assist you today?

Just now

Powered by **FluentBot**


---

---

