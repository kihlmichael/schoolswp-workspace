# FluentCart Developer Docs - Database Models (Part 3/8)

Tous les modèles Eloquent exposés par FluentCart : orders, customers, products, subscriptions, coupons, licenses, taxes, shipping, etc.

---

## Customer Addresses Model | FluentCart Developer Docs

**URL** : https://dev.fluentcart.com/database/models/customer-addresses

[Skip to content](https://dev.fluentcart.com/database/models/customer-addresses#VPContent)

# Customer Addresses Model [​](https://dev.fluentcart.com/database/models/customer-addresses\#customer-addresses-model)

| DB Table Name | {wp\_db\_prefix}\_fct\_customer\_addresses |
| --- | --- |
| Schema | [Check Schema](https://dev.fluentcart.com/database/schema.html#fct-customer-addresses-table) |
| Source File | fluent-cart/app/Models/CustomerAddresses.php |
| Name Space | FluentCart\\App\\Models |
| Class | FluentCart\\App\\Models\\CustomerAddresses |

## Traits [​](https://dev.fluentcart.com/database/models/customer-addresses\#traits)

| Trait | Description |
| --- | --- |
| CanSearch | Provides `search()`, `groupSearch()`, `whereLike()`, `whereBeginsWith()`, `whereEndsWith()` query scopes |

## Attributes [​](https://dev.fluentcart.com/database/models/customer-addresses\#attributes)

| Attribute | Data Type | Comment |
| --- | --- | --- |
| id | Integer | Primary Key |
| customer\_id | Integer | Reference to customer |
| is\_primary | Boolean | Whether this is the primary address |
| type | String | Address type (billing, shipping, etc.) |
| status | String | Address status (active, archived) |
| label | String | Address label/name |
| name | String | Full name |
| address\_1 | String | Primary address line |
| address\_2 | String | Secondary address line |
| city | String | City |
| state | String | State/Province |
| postcode | String | Postal/ZIP code |
| country | String | Country code |
| phone | String | Phone number |
| email | String | Email address |
| meta | JSON NULL | Stored as JSON string, auto-encoded/decoded via mutator/accessor |
| company\_name | Virtual | Stored inside `meta->other_data.company_name`, accessible as a virtual attribute via mutator/accessor |
| created\_at | Date Time | Creation timestamp |
| updated\_at | Date Time | Last update timestamp |

## Appended Attributes [​](https://dev.fluentcart.com/database/models/customer-addresses\#appended-attributes)

The following attributes are appended to every model serialization (e.g. `toArray()`, `toJson()`):

| Attribute | Type | Description |
| --- | --- | --- |
| formatted\_address | Array | Full formatted address with resolved country/state names, full address string, etc. |
| company\_name | String | Company name extracted from `meta->other_data.company_name` |

## Usage [​](https://dev.fluentcart.com/database/models/customer-addresses\#usage)

Please check [Model Basic](https://dev.fluentcart.com/database/models.html) for Common methods.

### Accessing Attributes [​](https://dev.fluentcart.com/database/models/customer-addresses\#accessing-attributes)

php

```
$customerAddress = FluentCart\App\Models\CustomerAddresses::find(1);

$customerAddress->id; // returns id
$customerAddress->customer_id; // returns customer ID
$customerAddress->is_primary; // returns primary status
$customerAddress->type; // returns address type
$customerAddress->company_name; // returns company name from meta
$customerAddress->formatted_address; // returns formatted address array
```

## Scopes [​](https://dev.fluentcart.com/database/models/customer-addresses\#scopes)

This model has the following scopes that you can use

### ofActive() [​](https://dev.fluentcart.com/database/models/customer-addresses\#ofactive)

Filter active addresses

- Parameters
  - none

#### Usage: [​](https://dev.fluentcart.com/database/models/customer-addresses\#usage-1)

php

```
// Get all active addresses
$activeAddresses = FluentCart\App\Models\CustomerAddresses::ofActive()->get();
```

### ofArchived() [​](https://dev.fluentcart.com/database/models/customer-addresses\#ofarchived)

Filter archived addresses

- Parameters
  - none

#### Usage: [​](https://dev.fluentcart.com/database/models/customer-addresses\#usage-2)

php

```
// Get all archived addresses
$archivedAddresses = FluentCart\App\Models\CustomerAddresses::ofArchived()->get();
```

### search($params) from CanSearch [​](https://dev.fluentcart.com/database/models/customer-addresses\#search-params)

Search addresses by parameters. Supports operators: `=`, `between`, `like_all`, `in`, `not_in`, `is_null`, `is_not_null`, and more.

- Parameters
  - `$params` (Array) - Search parameters

#### Usage: [​](https://dev.fluentcart.com/database/models/customer-addresses\#usage-3)

php

```
$addresses = FluentCart\App\Models\CustomerAddresses::search([\
    'country' => ['value' => 'US', 'operator' => '=']\
])->get();
```

## Relations [​](https://dev.fluentcart.com/database/models/customer-addresses\#relations)

This model has the following relationships that you can use

### customer [​](https://dev.fluentcart.com/database/models/customer-addresses\#customer)

Access the associated customer

- return `FluentCart\App\Models\Customer` Model (BelongsTo)

#### Example: [​](https://dev.fluentcart.com/database/models/customer-addresses\#example)

php

```
// Accessing Customer
$customer = $customerAddress->customer;

// For Filtering by customer relationship
$customerAddresses = FluentCart\App\Models\CustomerAddresses::whereHas('customer', function($query) {
    $query->where('status', 'active');
})->get();
```

## Methods [​](https://dev.fluentcart.com/database/models/customer-addresses\#methods)

Along with Global Model methods, this model has few helper methods.

### setMetaAttribute($value) [​](https://dev.fluentcart.com/database/models/customer-addresses\#setmetaattribute-value)

Set meta value with automatic JSON encoding (mutator). Called when setting `$address->meta = [...]`.

- Parameters
  - `$value` \- mixed (array or other value)
- Returns `void`

#### Usage [​](https://dev.fluentcart.com/database/models/customer-addresses\#usage-4)

php

```
$customerAddress->meta = ['other_data' => ['company_name' => 'Acme Inc']];
// Automatically JSON encodes the value
```

### getMetaAttribute($value) [​](https://dev.fluentcart.com/database/models/customer-addresses\#getmetaattribute-value)

Get meta value with automatic JSON decoding (accessor). Called when accessing `$address->meta`.

- Parameters
  - `$value` \- string (raw JSON from database)
- Returns `array`

#### Usage [​](https://dev.fluentcart.com/database/models/customer-addresses\#usage-5)

php

```
$meta = $customerAddress->meta; // Returns decoded array
```

### setCompanyNameAttribute($value) [​](https://dev.fluentcart.com/database/models/customer-addresses\#setcompanynameattribute-value)

Set the company name inside the `meta` JSON field at `other_data.company_name` (mutator). Called when setting `$address->company_name = '...'`.

- Parameters
  - `$value` \- string
- Returns `void`

#### Usage [​](https://dev.fluentcart.com/database/models/customer-addresses\#usage-6)

php

```
$customerAddress->company_name = 'Acme Inc';
// Stores the value inside meta->other_data.company_name
```

### getCompanyNameAttribute() [​](https://dev.fluentcart.com/database/models/customer-addresses\#getcompanynameattribute)

Get the company name from the `meta` JSON field at `other_data.company_name` (accessor).

- Parameters
  - none
- Returns `string` (empty string if not set)

#### Usage [​](https://dev.fluentcart.com/database/models/customer-addresses\#usage-7)

php

```
$companyName = $customerAddress->company_name; // Returns company name or ''
```

### getFormattedAddressAttribute() [​](https://dev.fluentcart.com/database/models/customer-addresses\#getformattedaddressattribute)

Get formatted address as array (accessor). This is an appended attribute available as `$address->formatted_address`.

- Parameters
  - none
- Returns `array`

The returned array contains:

| Key | Description |
| --- | --- |
| country | Full country name (resolved from country code) |
| state | Full state name (resolved from state code) |
| city | City |
| postcode | Postal/ZIP code |
| address\_1 | Primary address line |
| address\_2 | Secondary address line |
| type | Address type |
| name | Full name |
| first\_name | First name |
| last\_name | Last name |
| full\_name | Full name |
| company\_name | Company name |
| label | Address label |
| phone | Phone number |
| full\_address | Comma-separated full address string |

#### Usage [​](https://dev.fluentcart.com/database/models/customer-addresses\#usage-8)

php

```
$formattedAddress = $customerAddress->formatted_address;
echo $formattedAddress['full_address']; // "Acme Inc, 123 Main St, New York, NY, United States"
echo $formattedAddress['country']; // "United States"
```

### getFormattedDataForCheckout($prefix) [​](https://dev.fluentcart.com/database/models/customer-addresses\#getformatteddataforcheckout-prefix)

Get address data formatted for checkout forms with a configurable field prefix.

- Parameters
  - `$prefix` \- string (default: `'billing_'`)
- Returns `array`

The returned array keys are prefixed with the given `$prefix`:

| Key (with default prefix) | Value |
| --- | --- |
| billing\_full\_name | Name |
| billing\_address\_1 | Address line 1 |
| billing\_address\_2 | Address line 2 |
| billing\_city | City |
| billing\_state | State |
| billing\_phone | Phone |
| billing\_postcode | Postcode |
| billing\_country | Country |
| billing\_company\_name | Company name |

#### Usage [​](https://dev.fluentcart.com/database/models/customer-addresses\#usage-9)

php

```
$billingData = $customerAddress->getFormattedDataForCheckout(); // Uses 'billing_' prefix
$shippingData = $customerAddress->getFormattedDataForCheckout('shipping_'); // Uses 'shipping_' prefix
```

## Usage Examples [​](https://dev.fluentcart.com/database/models/customer-addresses\#usage-examples)

### Get Customer Addresses [​](https://dev.fluentcart.com/database/models/customer-addresses\#get-customer-addresses)

php

```
$customer = FluentCart\App\Models\Customer::find(123);
$addresses = $customer->addresses;

foreach ($addresses as $address) {
    echo "Address Type: " . $address->type;
    echo "Label: " . $address->label;
    echo "Is Primary: " . ($address->is_primary ? 'Yes' : 'No');
}
```

### Get Active Addresses [​](https://dev.fluentcart.com/database/models/customer-addresses\#get-active-addresses)

php

```
$activeAddresses = FluentCart\App\Models\CustomerAddresses::ofActive()->get();
```

### Get Primary Address [​](https://dev.fluentcart.com/database/models/customer-addresses\#get-primary-address)

php

```
$primaryAddress = FluentCart\App\Models\CustomerAddresses::where('customer_id', 123)
    ->where('is_primary', true)
    ->first();
```

### Create Customer Address [​](https://dev.fluentcart.com/database/models/customer-addresses\#create-customer-address)

php

```
$customerAddress = FluentCart\App\Models\CustomerAddresses::create([\
    'customer_id' => 123,\
    'is_primary' => true,\
    'type' => 'billing',\
    'status' => 'active',\
    'label' => 'Home Address',\
    'name' => 'John Doe',\
    'address_1' => '123 Main Street',\
    'city' => 'New York',\
    'state' => 'NY',\
    'postcode' => '10001',\
    'country' => 'US',\
    'phone' => '+1-555-123-4567',\
    'email' => 'john@example.com',\
    'company_name' => 'Acme Inc'\
]);
```

### Get Formatted Address [​](https://dev.fluentcart.com/database/models/customer-addresses\#get-formatted-address)

php

```
$address = FluentCart\App\Models\CustomerAddresses::find(1);
$formatted = $address->formatted_address;
// Returns array with formatted address components including full_address string
echo $formatted['full_address'];
```

### Get Checkout-Formatted Data [​](https://dev.fluentcart.com/database/models/customer-addresses\#get-checkout-formatted-data)

php

```
$address = FluentCart\App\Models\CustomerAddresses::find(1);
$billingFields = $address->getFormattedDataForCheckout('billing_');
$shippingFields = $address->getFormattedDataForCheckout('shipping_');
```

### Archive Address [​](https://dev.fluentcart.com/database/models/customer-addresses\#archive-address)

php

```
$address = FluentCart\App\Models\CustomerAddresses::find(1);
$address->status = 'archived';
$address->save();
```

* * *

Was this article helpful?

### Comments

Sign in to comment:

No comments yet. Be the first to share your thoughts!

Today

Hi! I’m your AI assistant. How can I assist you today?

Just now

Powered by **FluentBot**


---

---

## Customer Meta Model | FluentCart Developer Docs

**URL** : https://dev.fluentcart.com/database/models/customer-meta

[Skip to content](https://dev.fluentcart.com/database/models/customer-meta#VPContent)

# Customer Meta Model [​](https://dev.fluentcart.com/database/models/customer-meta\#customer-meta-model)

| DB Table Name | {wp\_db\_prefix}\_fct\_customer\_meta |
| --- | --- |
| Schema | [Check Schema](https://dev.fluentcart.com/database/schema.html#fct-customer-meta-table) |
| Source File | fluent-cart/app/Models/CustomerMeta.php |
| Name Space | FluentCart\\App\\Models |
| Class | FluentCart\\App\\Models\\CustomerMeta |

## Attributes [​](https://dev.fluentcart.com/database/models/customer-meta\#attributes)

| Attribute | Data Type | Comment |
| --- | --- | --- |
| id | Integer | Primary Key (guarded) |
| customer\_id | Integer | Reference to customer |
| meta\_key | String | Meta key name |
| meta\_value | Text | Meta value (JSON encoded for arrays/objects, auto-encoded/decoded via mutator/accessor) |
| created\_at | Date Time | Creation timestamp |
| updated\_at | Date Time | Last update timestamp |

## Usage [​](https://dev.fluentcart.com/database/models/customer-meta\#usage)

Please check [Model Basic](https://dev.fluentcart.com/database/models.html) for Common methods.

### Accessing Attributes [​](https://dev.fluentcart.com/database/models/customer-meta\#accessing-attributes)

php

```
$customerMeta = FluentCart\App\Models\CustomerMeta::find(1);

$customerMeta->id; // returns id
$customerMeta->customer_id; // returns customer ID
$customerMeta->meta_key; // returns meta key
$customerMeta->meta_value; // returns meta value (auto-decoded if JSON)
```

## Relations [​](https://dev.fluentcart.com/database/models/customer-meta\#relations)

This model has the following relationships that you can use

### customer [​](https://dev.fluentcart.com/database/models/customer-meta\#customer)

Access the associated customer

- return `FluentCart\App\Models\Customer` Model (BelongsTo)

#### Example: [​](https://dev.fluentcart.com/database/models/customer-meta\#example)

php

```
// Accessing Customer
$customer = $customerMeta->customer;

// For Filtering by customer relationship
$customerMetas = FluentCart\App\Models\CustomerMeta::whereHas('customer', function($query) {
    $query->where('status', 'active');
})->get();
```

## Methods [​](https://dev.fluentcart.com/database/models/customer-meta\#methods)

Along with Global Model methods, this model has few helper methods.

### setMetaValueAttribute($value) [​](https://dev.fluentcart.com/database/models/customer-meta\#setmetavalueattribute-value)

Set meta value with automatic JSON encoding (mutator). Arrays and objects are encoded with `JSON_UNESCAPED_UNICODE | JSON_UNESCAPED_SLASHES` flags.

- Parameters
  - `$value` \- mixed (array, object, or string)
- Returns `void`

#### Usage [​](https://dev.fluentcart.com/database/models/customer-meta\#usage-1)

php

```
$customerMeta->meta_value = ['preferences' => 'value', 'settings' => ['key' => 'value']];
// Automatically JSON encodes arrays and objects
```

### getMetaValueAttribute($value) [​](https://dev.fluentcart.com/database/models/customer-meta\#getmetavalueattribute-value)

Get meta value with automatic JSON decoding (accessor). If the stored string is valid JSON, it returns the decoded array. Otherwise, returns the raw string value.

- Parameters
  - `$value` \- mixed
- Returns `mixed` (decoded array if valid JSON, otherwise original value)

#### Usage [​](https://dev.fluentcart.com/database/models/customer-meta\#usage-2)

php

```
$metaValue = $customerMeta->meta_value; // Returns decoded value (array, object, or string)
```

## Usage Examples [​](https://dev.fluentcart.com/database/models/customer-meta\#usage-examples)

### Get Customer Meta [​](https://dev.fluentcart.com/database/models/customer-meta\#get-customer-meta)

php

```
$customer = FluentCart\App\Models\Customer::find(123);
$meta = $customer->customer_meta;

foreach ($meta as $metaItem) {
    echo "Key: " . $metaItem->meta_key;
    echo "Value: " . print_r($metaItem->meta_value, true);
}
```

### Create Customer Meta [​](https://dev.fluentcart.com/database/models/customer-meta\#create-customer-meta)

php

```
$customerMeta = FluentCart\App\Models\CustomerMeta::create([\
    'customer_id' => 123,\
    'meta_key' => 'preferences',\
    'meta_value' => 'newsletter_subscribed'\
]);
```

### Store Complex Customer Data [​](https://dev.fluentcart.com/database/models/customer-meta\#store-complex-customer-data)

php

```
$customerMeta = FluentCart\App\Models\CustomerMeta::create([\
    'customer_id' => 123,\
    'meta_key' => 'shopping_preferences',\
    'meta_value' => [\
        'newsletter' => true,\
        'sms_notifications' => false,\
        'preferred_categories' => ['electronics', 'books'],\
        'shipping_preference' => 'standard'\
    ]\
]);
```

### Get Meta by Key [​](https://dev.fluentcart.com/database/models/customer-meta\#get-meta-by-key)

php

```
$meta = FluentCart\App\Models\CustomerMeta::where('customer_id', 123)
    ->where('meta_key', 'preferences')
    ->first();

if ($meta) {
    echo "Preferences: " . $meta->meta_value;
}
```

### Update Customer Meta [​](https://dev.fluentcart.com/database/models/customer-meta\#update-customer-meta)

php

```
$meta = FluentCart\App\Models\CustomerMeta::find(1);
$meta->meta_value = ['updated' => true, 'timestamp' => now()];
$meta->save();
```

### Get All Meta for Customer [​](https://dev.fluentcart.com/database/models/customer-meta\#get-all-meta-for-customer)

php

```
$customerMetas = FluentCart\App\Models\CustomerMeta::where('customer_id', 123)->get();
```

* * *

Was this article helpful?

### Comments

Sign in to comment:

No comments yet. Be the first to share your thoughts!

Today

Hi! I’m your AI assistant. How can I assist you today?

Just now

Powered by **FluentBot**


---

---

## Dynamic Model | FluentCart Developer Docs

**URL** : https://dev.fluentcart.com/database/models/dynamic-model

[Skip to content](https://dev.fluentcart.com/database/models/dynamic-model#VPContent)

# Dynamic Model [​](https://dev.fluentcart.com/database/models/dynamic-model\#dynamic-model)

| DB Table Name | Dynamic (set via constructor) |
| --- | --- |
| Schema | [Check Schema](https://dev.fluentcart.com/database/schema.html) |
| Source File | fluent-cart/app/Models/DynamicModel.php |
| Name Space | FluentCart\\App\\Models |
| Class | FluentCart\\App\\Models\\DynamicModel |

## Traits [​](https://dev.fluentcart.com/database/models/dynamic-model\#traits)

- **CanSearch** (`FluentCart\App\Models\Concerns\CanSearch`) \- Provides `search()`, `groupSearch()`, `whereLike()`, `whereBeginsWith()`, and `whereEndsWith()` query scopes.

## Attributes [​](https://dev.fluentcart.com/database/models/dynamic-model\#attributes)

| Attribute | Data Type | Comment |
| --- | --- | --- |
| id | Integer | Primary Key (default) |
| \* | Mixed | All attributes are fillable (guarded = \[\]) |
| created\_at | Date Time | Creation timestamp (if table has timestamps) |
| updated\_at | Date Time | Last update timestamp (if table has timestamps) |

## Guarded Attributes [​](https://dev.fluentcart.com/database/models/dynamic-model\#guarded-attributes)

No attributes are guarded (`$guarded = []`). All attributes are mass-assignable.

## Usage [​](https://dev.fluentcart.com/database/models/dynamic-model\#usage)

Please check [Model Basic](https://dev.fluentcart.com/database/models.html) for Common methods.

### Accessing Attributes [​](https://dev.fluentcart.com/database/models/dynamic-model\#accessing-attributes)

php

```
$dynamicModel = new FluentCart\App\Models\DynamicModel([], 'custom_table');

$dynamicModel->id; // returns id
$dynamicModel->any_field; // returns any field from the table
```

## Methods [​](https://dev.fluentcart.com/database/models/dynamic-model\#methods)

Along with Global Model methods, this model has few helper methods.

### \_\_construct($attributes = \[\], $table = null) [​](https://dev.fluentcart.com/database/models/dynamic-model\#construct-attributes-table-null)

Dynamic model constructor. Calls the parent constructor with the given attributes and then sets the table name to the provided value.

- Parameters
  - $attributes - array (default: \[\])
  - $table - string\|null (default: null)
- Returns `void`

#### Usage [​](https://dev.fluentcart.com/database/models/dynamic-model\#usage-1)

php

```
// Create dynamic model for custom table
$dynamicModel = new FluentCart\App\Models\DynamicModel([], 'custom_table');

// Create dynamic model with initial data
$dynamicModel = new FluentCart\App\Models\DynamicModel([\
    'name' => 'Test',\
    'value' => 'Example'\
], 'custom_table');
```

## Usage Examples [​](https://dev.fluentcart.com/database/models/dynamic-model\#usage-examples)

### Create Dynamic Model [​](https://dev.fluentcart.com/database/models/dynamic-model\#create-dynamic-model)

php

```
// Create dynamic model for a custom table
$dynamicModel = new FluentCart\App\Models\DynamicModel([], 'my_custom_table');

// Set table and create instance
$dynamicModel->setTable('my_custom_table');
```

### Use Dynamic Model with Custom Table [​](https://dev.fluentcart.com/database/models/dynamic-model\#use-dynamic-model-with-custom-table)

php

```
// Create dynamic model for custom table
$dynamicModel = new FluentCart\App\Models\DynamicModel([], 'custom_analytics');

// Create record
$dynamicModel->create([\
    'event_name' => 'page_view',\
    'user_id' => 123,\
    'timestamp' => now(),\
    'metadata' => json_encode(['page' => '/products', 'source' => 'google'])\
]);
```

### Query Dynamic Table [​](https://dev.fluentcart.com/database/models/dynamic-model\#query-dynamic-table)

php

```
// Create dynamic model for custom table
$dynamicModel = new FluentCart\App\Models\DynamicModel([], 'custom_analytics');

// Get all records
$records = $dynamicModel->all();

// Get specific records
$pageViews = $dynamicModel->where('event_name', 'page_view')->get();

// Get recent records
$recentEvents = $dynamicModel->where('timestamp', '>=', now()->subDays(7))->get();
```

### Update Dynamic Table [​](https://dev.fluentcart.com/database/models/dynamic-model\#update-dynamic-table)

php

```
// Create dynamic model for custom table
$dynamicModel = new FluentCart\App\Models\DynamicModel([], 'custom_analytics');

// Update record
$dynamicModel->where('id', 1)->update([\
    'metadata' => json_encode(['updated' => true])\
]);
```

### Delete from Dynamic Table [​](https://dev.fluentcart.com/database/models/dynamic-model\#delete-from-dynamic-table)

php

```
// Create dynamic model for custom table
$dynamicModel = new FluentCart\App\Models\DynamicModel([], 'custom_analytics');

// Delete record
$dynamicModel->where('id', 1)->delete();

// Delete multiple records
$dynamicModel->where('event_name', 'old_event')->delete();
```

### Use CanSearch Trait Scopes [​](https://dev.fluentcart.com/database/models/dynamic-model\#use-cansearch-trait-scopes)

php

```
// Create dynamic model for custom table
$dynamicModel = new FluentCart\App\Models\DynamicModel([], 'custom_analytics');

// Search with the search scope (from CanSearch trait)
$results = $dynamicModel->search([\
    'event_name' => ['column' => 'event_name', 'operator' => 'like_all', 'value' => 'page_view']\
])->get();

// Use whereLike scope
$results = $dynamicModel->whereLike('event_name', 'page')->get();
```

### Dynamic Model for Temporary Tables [​](https://dev.fluentcart.com/database/models/dynamic-model\#dynamic-model-for-temporary-tables)

php

```
// Create dynamic model for temporary table
$tempModel = new FluentCart\App\Models\DynamicModel([], 'temp_import_data');

// Use for data processing
$tempModel->create([\
    'import_id' => 123,\
    'row_data' => json_encode(['name' => 'Product', 'price' => 29.99]),\
    'status' => 'pending'\
]);
```

* * *

Was this article helpful?

### Comments

Sign in to comment:

No comments yet. Be the first to share your thoughts!

Today

Hi! I’m your AI assistant. How can I assist you today?

Just now

Powered by **FluentBot**


---

---

## Label Model | FluentCart Developer Docs

**URL** : https://dev.fluentcart.com/database/models/label

[Skip to content](https://dev.fluentcart.com/database/models/label#VPContent)

# Label Model [​](https://dev.fluentcart.com/database/models/label\#label-model)

| DB Table Name | {wp\_db\_prefix}\_fct\_label |
| --- | --- |
| Schema | [Check Schema](https://dev.fluentcart.com/database/schema.html#fct-label-table) |
| Source File | fluent-cart/app/Models/Label.php |
| Name Space | FluentCart\\App\\Models |
| Class | FluentCart\\App\\Models\\Label |

## Attributes [​](https://dev.fluentcart.com/database/models/label\#attributes)

| Attribute | Data Type | Comment |
| --- | --- | --- |
| id | Integer | Primary Key |
| value | Mixed | Label value (serialized) |
| created\_at | Date Time | Creation timestamp |
| updated\_at | Date Time | Last update timestamp |

## Casts [​](https://dev.fluentcart.com/database/models/label\#casts)

| Attribute | Cast Type |
| --- | --- |
| id | integer |

## Usage [​](https://dev.fluentcart.com/database/models/label\#usage)

Please check [Model Basic](https://dev.fluentcart.com/database/models.html) for Common methods.

### Accessing Attributes [​](https://dev.fluentcart.com/database/models/label\#accessing-attributes)

php

```
$label = FluentCart\App\Models\Label::find(1);

$label->id; // returns id
$label->value; // returns label value
```

## Methods [​](https://dev.fluentcart.com/database/models/label\#methods)

Along with Global Model methods, this model has few helper methods.

### setValueAttribute($value) [​](https://dev.fluentcart.com/database/models/label\#setvalueattribute-value)

Set value with automatic serialization (mutator). Uses WordPress `maybe_serialize()` to serialize arrays and objects before storing.

- Parameters
  - $value - mixed
- Returns `void`

#### Usage [​](https://dev.fluentcart.com/database/models/label\#usage-1)

php

```
$label->value = ['name' => 'VIP Customer', 'color' => 'gold'];
// Automatically serializes the value using maybe_serialize()
```

### getValueAttribute($value) [​](https://dev.fluentcart.com/database/models/label\#getvalueattribute-value)

Get value with automatic unserialization (accessor). Uses WordPress `maybe_unserialize()` to unserialize stored values.

- Parameters
  - $value - mixed
- Returns `mixed`

#### Usage [​](https://dev.fluentcart.com/database/models/label\#usage-2)

php

```
$value = $label->value; // Returns unserialized value
```

## Usage Examples [​](https://dev.fluentcart.com/database/models/label\#usage-examples)

### Get Labels [​](https://dev.fluentcart.com/database/models/label\#get-labels)

php

```
$label = FluentCart\App\Models\Label::find(1);
echo "Label ID: " . $label->id;
echo "Label Value: " . print_r($label->value, true);
```

### Create Label [​](https://dev.fluentcart.com/database/models/label\#create-label)

php

```
$label = FluentCart\App\Models\Label::create([\
    'value' => [\
        'name' => 'VIP Customer',\
        'color' => 'gold',\
        'description' => 'High-value customer'\
    ]\
]);
```

### Get All Labels [​](https://dev.fluentcart.com/database/models/label\#get-all-labels)

php

```
$labels = FluentCart\App\Models\Label::all();

foreach ($labels as $label) {
    $value = $label->value;
    if (is_array($value) && isset($value['name'])) {
        echo "Label: " . $value['name'];
    }
}
```

### Update Label [​](https://dev.fluentcart.com/database/models/label\#update-label)

php

```
$label = FluentCart\App\Models\Label::find(1);
$label->update([\
    'value' => [\
        'name' => 'Premium Customer',\
        'color' => 'platinum',\
        'description' => 'Premium tier customer'\
    ]\
]);
```

### Get Labels by Value [​](https://dev.fluentcart.com/database/models/label\#get-labels-by-value)

php

```
$labels = FluentCart\App\Models\Label::all();

foreach ($labels as $label) {
    $value = $label->value;
    if (is_array($value) && isset($value['color']) && $value['color'] === 'gold') {
        echo "Gold Label: " . $value['name'];
    }
}
```

### Delete Label [​](https://dev.fluentcart.com/database/models/label\#delete-label)

php

```
$label = FluentCart\App\Models\Label::find(1);
$label->delete();
```

### Create Simple Label [​](https://dev.fluentcart.com/database/models/label\#create-simple-label)

php

```
$label = FluentCart\App\Models\Label::create([\
    'value' => 'New Customer'\
]);
```

### Get Labels Ordered by ID [​](https://dev.fluentcart.com/database/models/label\#get-labels-ordered-by-id)

php

```
$orderedLabels = FluentCart\App\Models\Label::orderBy('id', 'asc')->get();
```

* * *

Today

Hi! I’m your AI assistant. How can I assist you today?

Just now

Powered by **FluentBot**


---

---

## Label Relationship Model | FluentCart Developer Docs

**URL** : https://dev.fluentcart.com/database/models/label-relationship

[Skip to content](https://dev.fluentcart.com/database/models/label-relationship#VPContent)

# Label Relationship Model [​](https://dev.fluentcart.com/database/models/label-relationship\#label-relationship-model)

| DB Table Name | {wp\_db\_prefix}\_fct\_label\_relationships |
| --- | --- |
| Schema | [Check Schema](https://dev.fluentcart.com/database/schema.html#fct-label-relationships-table) |
| Source File | fluent-cart/app/Models/LabelRelationship.php |
| Name Space | FluentCart\\App\\Models |
| Class | FluentCart\\App\\Models\\LabelRelationship |

## Attributes [​](https://dev.fluentcart.com/database/models/label-relationship\#attributes)

| Attribute | Data Type | Comment |
| --- | --- | --- |
| id | Integer | Primary Key |
| label\_id | Integer | Reference to label |
| labelable\_id | Integer | ID of the labeled object |
| labelable\_type | String | Type of the labeled object (Order, Customer, etc.) |
| created\_at | Date Time | Creation timestamp |
| updated\_at | Date Time | Last update timestamp |

## Casts [​](https://dev.fluentcart.com/database/models/label-relationship\#casts)

| Attribute | Cast Type |
| --- | --- |
| label\_id | integer |

## Usage [​](https://dev.fluentcart.com/database/models/label-relationship\#usage)

Please check [Model Basic](https://dev.fluentcart.com/database/models.html) for Common methods.

### Accessing Attributes [​](https://dev.fluentcart.com/database/models/label-relationship\#accessing-attributes)

php

```
$labelRelationship = FluentCart\App\Models\LabelRelationship::find(1);

$labelRelationship->id; // returns id
$labelRelationship->label_id; // returns label ID
$labelRelationship->labelable_id; // returns labeled object ID
$labelRelationship->labelable_type; // returns labeled object type
```

## Relations [​](https://dev.fluentcart.com/database/models/label-relationship\#relations)

This model has the following relationships that you can use

### labelable [​](https://dev.fluentcart.com/database/models/label-relationship\#labelable)

Access the labeled object (polymorphic `morphTo` relationship)

- return `mixed` (Order, Customer, or other labeled models)

#### Example: [​](https://dev.fluentcart.com/database/models/label-relationship\#example)

php

```
// Accessing Labeled Object
$labeledObject = $labelRelationship->labelable;

// For Filtering by labeled object type
$orderLabels = FluentCart\App\Models\LabelRelationship::where('labelable_type', 'Order')->get();
$customerLabels = FluentCart\App\Models\LabelRelationship::where('labelable_type', 'Customer')->get();
```

## Usage Examples [​](https://dev.fluentcart.com/database/models/label-relationship\#usage-examples)

### Get Label Relationships [​](https://dev.fluentcart.com/database/models/label-relationship\#get-label-relationships)

php

```
$labelRelationship = FluentCart\App\Models\LabelRelationship::find(1);
echo "Label ID: " . $labelRelationship->label_id;
echo "Object Type: " . $labelRelationship->labelable_type;
echo "Object ID: " . $labelRelationship->labelable_id;
```

### Create Label Relationship [​](https://dev.fluentcart.com/database/models/label-relationship\#create-label-relationship)

php

```
$labelRelationship = FluentCart\App\Models\LabelRelationship::create([\
    'label_id' => 1,\
    'labelable_id' => 123,\
    'labelable_type' => 'Order'\
]);
```

### Get All Label Relationships [​](https://dev.fluentcart.com/database/models/label-relationship\#get-all-label-relationships)

php

```
$labelRelationships = FluentCart\App\Models\LabelRelationship::all();

foreach ($labelRelationships as $relationship) {
    echo "Label ID: " . $relationship->label_id;
    echo "Object: " . $relationship->labelable_type . " #" . $relationship->labelable_id;
}
```

### Get Label Relationships by Type [​](https://dev.fluentcart.com/database/models/label-relationship\#get-label-relationships-by-type)

php

```
$orderLabels = FluentCart\App\Models\LabelRelationship::where('labelable_type', 'Order')->get();
$customerLabels = FluentCart\App\Models\LabelRelationship::where('labelable_type', 'Customer')->get();
```

### Get Label Relationships with Labeled Objects [​](https://dev.fluentcart.com/database/models/label-relationship\#get-label-relationships-with-labeled-objects)

php

```
$labelRelationships = FluentCart\App\Models\LabelRelationship::all();

foreach ($labelRelationships as $relationship) {
    $labeledObject = $relationship->labelable;
    echo "Labeled Object: " . get_class($labeledObject) . " #" . $labeledObject->id;
}
```

### Get Labels for Specific Object [​](https://dev.fluentcart.com/database/models/label-relationship\#get-labels-for-specific-object)

php

```
$orderLabels = FluentCart\App\Models\LabelRelationship::where('labelable_type', 'Order')
    ->where('labelable_id', 123)
    ->get();
```

### Get Labels for Specific Label [​](https://dev.fluentcart.com/database/models/label-relationship\#get-labels-for-specific-label)

php

```
$labelRelationships = FluentCart\App\Models\LabelRelationship::where('label_id', 1)->get();

foreach ($labelRelationships as $relationship) {
    echo "Object: " . $relationship->labelable_type . " #" . $relationship->labelable_id;
}
```

### Update Label Relationship [​](https://dev.fluentcart.com/database/models/label-relationship\#update-label-relationship)

php

```
$labelRelationship = FluentCart\App\Models\LabelRelationship::find(1);
$labelRelationship->update([\
    'label_id' => 2\
]);
```

### Delete Label Relationship [​](https://dev.fluentcart.com/database/models/label-relationship\#delete-label-relationship)

php

```
$labelRelationship = FluentCart\App\Models\LabelRelationship::find(1);
$labelRelationship->delete();
```

### Get Label Relationships for Multiple Objects [​](https://dev.fluentcart.com/database/models/label-relationship\#get-label-relationships-for-multiple-objects)

php

```
$labelRelationships = FluentCart\App\Models\LabelRelationship::where('labelable_type', 'Order')
    ->whereIn('labelable_id', [123, 124, 125])
    ->get();
```

* * *

Today

Hi! I’m your AI assistant. How can I assist you today?

Just now

Powered by **FluentBot**


---

---

## License Model | FluentCart Developer Docs

**URL** : https://dev.fluentcart.com/database/models/license

[Skip to content](https://dev.fluentcart.com/database/models/license#VPContent)

Pro

# License Model [​](https://dev.fluentcart.com/database/models/license\#license-model)

| DB Table Name | {wp\_db\_prefix}\_fct\_licenses |
| --- | --- |
| Schema | [Check Schema](https://dev.fluentcart.com/database/schema.html#fct-licenses-table) |
| Source File | fluent-cart-pro/app/Modules/Licensing/Models/License.php |
| Name Space | FluentCartPro\\App\\Modules\\Licensing\\Models |
| Class | FluentCartPro\\App\\Modules\\Licensing\\Models\\License |
| Plugin | FluentCart Pro |

## Properties [​](https://dev.fluentcart.com/database/models/license\#properties)

- **Table**: `fct_licenses`
- **Primary Key**: `id`
- **Guarded**: `['id']`
- **Fillable**: `['status', 'limit', 'activation_count', 'license_key', 'product_id', 'variation_id', 'order_id', 'parent_id', 'customer_id', 'expiration_date', 'last_reminder_sent', 'last_reminder_type', 'subscription_id', 'config']`
- **Traits**: `CanSearch`

## Attributes [​](https://dev.fluentcart.com/database/models/license\#attributes)

| Attribute | Data Type | Comment |
| --- | --- | --- |
| id | Integer | Primary Key |
| status | String | License status (active, inactive, expired, disabled) |
| limit | Integer | Activation limit (0 = unlimited) |
| activation\_count | Integer | Current activation count |
| license\_key | String | Unique license key |
| product\_id | Integer | Reference to product |
| variation\_id | Integer | Reference to product variation |
| order\_id | Integer | Reference to order |
| parent\_id | Integer | Parent license ID (for renewals) |
| customer\_id | Integer | Reference to customer |
| expiration\_date | Date Time | License expiration date (null = lifetime) |
| last\_reminder\_sent | Date Time | Last reminder sent date |
| last\_reminder\_type | String | Last reminder type |
| subscription\_id | Integer | Reference to subscription |
| config | JSON | License configuration (auto-cast via accessor/mutator) |
| created\_at | Date Time | Creation timestamp |
| updated\_at | Date Time | Last update timestamp |

## Usage [​](https://dev.fluentcart.com/database/models/license\#usage)

Please check [Model Basic](https://dev.fluentcart.com/database/models.html) for Common methods.

### Accessing Attributes [​](https://dev.fluentcart.com/database/models/license\#accessing-attributes)

php

```
$license = FluentCartPro\App\Modules\Licensing\Models\License::find(1);

$license->id; // returns id
$license->license_key; // returns license key
$license->status; // returns status
$license->activation_count; // returns activation count
$license->limit; // returns activation limit
$license->config; // returns config as array (auto-decoded)
```

## Scopes [​](https://dev.fluentcart.com/database/models/license\#scopes)

This model has the following scopes that you can use

### scopeSearch($query, $search) [​](https://dev.fluentcart.com/database/models/license\#scopesearch-query-search)

Search licenses by license key, order ID, product title, or customer name/email

- Parameters
  - $search - string

#### Usage: [​](https://dev.fluentcart.com/database/models/license\#usage-1)

php

```
// Search across license key, order ID, product title, customer name/email
$licenses = FluentCartPro\App\Modules\Licensing\Models\License::search('example@email.com')->get();
```

### scopeStatus($query, $status) [​](https://dev.fluentcart.com/database/models/license\#scopestatus-query-status)

Filter licenses by status with smart logic. Supports: `active`, `expired`, `disabled`, `inactive`. Passing `'all'` or empty value returns all licenses.

- Parameters
  - $status - string

#### Usage: [​](https://dev.fluentcart.com/database/models/license\#usage-2)

php

```
// Get active licenses (not expired, status is 'active')
$licenses = FluentCartPro\App\Modules\Licensing\Models\License::status('active')->get();

// Get expired licenses (expiration_date < now)
$licenses = FluentCartPro\App\Modules\Licensing\Models\License::status('expired')->get();

// Get inactive licenses (status 'active' but no activations)
$licenses = FluentCartPro\App\Modules\Licensing\Models\License::status('inactive')->get();

// Get disabled licenses
$licenses = FluentCartPro\App\Modules\Licensing\Models\License::status('disabled')->get();
```

### scopeProducts($query, $productIds) [​](https://dev.fluentcart.com/database/models/license\#scopeproducts-query-productids)

Filter licenses by product IDs

- Parameters
  - $productIds - array

#### Usage: [​](https://dev.fluentcart.com/database/models/license\#usage-3)

php

```
// Get all licenses for specific products
$licenses = FluentCartPro\App\Modules\Licensing\Models\License::products([1, 2, 3])->get();
```

## Relations [​](https://dev.fluentcart.com/database/models/license\#relations)

This model has the following relationships that you can use

### customer [​](https://dev.fluentcart.com/database/models/license\#customer)

Access the associated customer (BelongsTo)

- return `FluentCart\App\Models\Customer` Model

#### Example: [​](https://dev.fluentcart.com/database/models/license\#example)

php

```
// Accessing Customer
$customer = $license->customer;

// For Filtering by customer relationship
$licenses = FluentCartPro\App\Modules\Licensing\Models\License::whereHas('customer', function($query) {
    $query->where('email', 'customer@example.com');
})->get();
```

### order [​](https://dev.fluentcart.com/database/models/license\#order)

Access the associated order (BelongsTo)

- return `FluentCart\App\Models\Order` Model

#### Example: [​](https://dev.fluentcart.com/database/models/license\#example-1)

php

```
// Accessing Order
$order = $license->order;

// For Filtering by order relationship
$licenses = FluentCartPro\App\Modules\Licensing\Models\License::whereHas('order', function($query) {
    $query->where('status', 'completed');
})->get();
```

### product [​](https://dev.fluentcart.com/database/models/license\#product)

Access the associated product (BelongsTo)

- return `FluentCart\App\Models\Product` Model

#### Example: [​](https://dev.fluentcart.com/database/models/license\#example-2)

php

```
// Accessing Product
$product = $license->product;

// For Filtering by product relationship
$licenses = FluentCartPro\App\Modules\Licensing\Models\License::whereHas('product', function($query) {
    $query->where('post_status', 'publish');
})->get();
```

### variation [​](https://dev.fluentcart.com/database/models/license\#variation)

Access the associated product variation (BelongsTo)

- return `FluentCart\App\Models\ProductVariation` Model

#### Example: [​](https://dev.fluentcart.com/database/models/license\#example-3)

php

```
// Accessing Product Variation
$variation = $license->variation;
```

### productVariant [​](https://dev.fluentcart.com/database/models/license\#productvariant)

Alias for variation - access the associated product variation (BelongsTo)

- return `FluentCart\App\Models\ProductVariation` Model

#### Example: [​](https://dev.fluentcart.com/database/models/license\#example-4)

php

```
// Accessing Product Variant
$variant = $license->productVariant;
```

### productDetails [​](https://dev.fluentcart.com/database/models/license\#productdetails)

Access the associated product details (BelongsTo)

- return `FluentCart\App\Models\ProductDetail` Model

#### Example: [​](https://dev.fluentcart.com/database/models/license\#example-5)

php

```
// Accessing Product Details
$details = $license->productDetails;
```

### subscription [​](https://dev.fluentcart.com/database/models/license\#subscription)

Access the associated subscription (BelongsTo)

- return `FluentCart\App\Models\Subscription` Model

#### Example: [​](https://dev.fluentcart.com/database/models/license\#example-6)

php

```
// Accessing Subscription
$subscription = $license->subscription;

// For Filtering by subscription relationship
$licenses = FluentCartPro\App\Modules\Licensing\Models\License::whereHas('subscription', function($query) {
    $query->where('status', 'active');
})->get();
```

### activations [​](https://dev.fluentcart.com/database/models/license\#activations)

Access license activations (HasMany)

- return `FluentCartPro\App\Modules\Licensing\Models\LicenseActivation` Collection

#### Example: [​](https://dev.fluentcart.com/database/models/license\#example-7)

php

```
// Accessing Activations
$activations = $license->activations;

// For Filtering by activations relationship
$licenses = FluentCartPro\App\Modules\Licensing\Models\License::whereHas('activations', function($query) {
    $query->where('status', 'active');
})->get();
```

### labels [​](https://dev.fluentcart.com/database/models/license\#labels)

Access license labels (MorphMany)

- return `FluentCart\App\Models\LabelRelationship` Collection

#### Example: [​](https://dev.fluentcart.com/database/models/license\#example-8)

php

```
// Accessing Labels
$labels = $license->labels;
```

## Methods [​](https://dev.fluentcart.com/database/models/license\#methods)

Along with Global Model methods, this model has few helper methods.

### getConfigAttribute($value) [​](https://dev.fluentcart.com/database/models/license\#getconfigattribute-value)

Get config as array (accessor). Returns empty array if value is null or not valid JSON.

- Parameters
  - $value - mixed
- Returns `array`

#### Usage [​](https://dev.fluentcart.com/database/models/license\#usage-4)

php

```
$config = $license->config; // Returns array
```

### setConfigAttribute($value) [​](https://dev.fluentcart.com/database/models/license\#setconfigattribute-value)

Set config from array (mutator). Non-array or falsy values are stored as empty array JSON.

- Parameters
  - $value - array\|null
- Returns `void`

#### Usage [​](https://dev.fluentcart.com/database/models/license\#usage-5)

php

```
$license->config = ['auto_renew' => true, 'max_sites' => 5];
```

### isActive() [​](https://dev.fluentcart.com/database/models/license\#isactive)

Check if license is active. Returns true if status is `active` or `inactive`.

- Parameters
  - none
- Returns `boolean`

#### Usage [​](https://dev.fluentcart.com/database/models/license\#usage-6)

php

```
$isActive = $license->isActive();
```

### isExpired() [​](https://dev.fluentcart.com/database/models/license\#isexpired)

Check if license is expired. Takes into account the configurable grace period from `LicenseHelper::getLicenseGracePeriodDays()`.

- Parameters
  - none
- Returns `boolean`

#### Usage [​](https://dev.fluentcart.com/database/models/license\#usage-7)

php

```
$isExpired = $license->isExpired();
```

### isValid() [​](https://dev.fluentcart.com/database/models/license\#isvalid)

Check if license is both not expired and active.

- Parameters
  - none
- Returns `boolean`

#### Usage [​](https://dev.fluentcart.com/database/models/license\#usage-8)

php

```
$isValid = $license->isValid();
```

### getPublicStatus() [​](https://dev.fluentcart.com/database/models/license\#getpublicstatus)

Get the public-facing status string. Returns `'valid'`, `'expired'`, or `'invalid'`.

- Parameters
  - none
- Returns `string`

#### Usage [​](https://dev.fluentcart.com/database/models/license\#usage-9)

php

```
$publicStatus = $license->getPublicStatus();
```

### getHumanReadableStatus() [​](https://dev.fluentcart.com/database/models/license\#gethumanreadablestatus)

Get human readable status. Returns `'active'` for both `active` and `inactive` statuses, otherwise returns the raw status.

- Parameters
  - none
- Returns `string`

#### Usage [​](https://dev.fluentcart.com/database/models/license\#usage-10)

php

```
$readableStatus = $license->getHumanReadableStatus();
```

### getActivationLimit() [​](https://dev.fluentcart.com/database/models/license\#getactivationlimit)

Get remaining activation count. Returns `'unlimited'` if limit is 0 (unlimited), otherwise returns the number of remaining activations.

- Parameters
  - none
- Returns `string|integer` \- `'unlimited'` or remaining activation count

#### Usage [​](https://dev.fluentcart.com/database/models/license\#usage-11)

php

```
$remaining = $license->getActivationLimit();
```

### hasActivationLeft() [​](https://dev.fluentcart.com/database/models/license\#hasactivationleft)

Check if there are any activations remaining.

- Parameters
  - none
- Returns `boolean`

#### Usage [​](https://dev.fluentcart.com/database/models/license\#usage-12)

php

```
$hasLeft = $license->hasActivationLeft();
```

### updateLicenseStatus($newStatus) [​](https://dev.fluentcart.com/database/models/license\#updatelicensestatus-newstatus)

Update the license status and fire action hooks. Does nothing if the new status is the same as current.

- Parameters
  - $newStatus - string
- Returns `$this`

**Actions Triggered:**

- `fluent_cart_sl/license_status_updated`
- `fluent_cart_sl/license_status_updated_to_{$newStatus}`

#### Usage [​](https://dev.fluentcart.com/database/models/license\#usage-13)

php

```
$license->updateLicenseStatus('disabled');
```

### increaseActivationCount() [​](https://dev.fluentcart.com/database/models/license\#increaseactivationcount)

Increment the activation count by 1 and fire an action hook.

- Parameters
  - none
- Returns `$this`

**Actions Triggered:**

- `fluent_cart_sl/license_limit_increased`

#### Usage [​](https://dev.fluentcart.com/database/models/license\#usage-14)

php

```
$license->increaseActivationCount();
```

### decreaseActivationCount() [​](https://dev.fluentcart.com/database/models/license\#decreaseactivationcount)

Decrement the activation count by 1. Does nothing if count is already 0.

- Parameters
  - none
- Returns `$this`

**Actions Triggered:**

- `fluent_cart_sl/license_limit_decreased`

#### Usage [​](https://dev.fluentcart.com/database/models/license\#usage-15)

php

```
$license->decreaseActivationCount();
```

### increaseLimit($newLimit) [​](https://dev.fluentcart.com/database/models/license\#increaselimit-newlimit)

Set a new activation limit. Passing `'unlimited'` or `0` sets the limit to 0 (unlimited).

- Parameters
  - $newLimit - integer\|string
- Returns `$this`

**Actions Triggered:**

- `fluent_cart_sl/license_limit_increased`

#### Usage [​](https://dev.fluentcart.com/database/models/license\#usage-16)

php

```
$license->increaseLimit(10);
$license->increaseLimit('unlimited');
```

### regenerateKey() [​](https://dev.fluentcart.com/database/models/license\#regeneratekey)

Generate a new license key using `UUID::licensesKey()` and fire an action hook.

- Parameters
  - none
- Returns `$this`

**Actions Triggered:**

- `fluent_cart_sl/license_key_regenerated`

#### Usage [​](https://dev.fluentcart.com/database/models/license\#usage-17)

php

```
$license->regenerateKey();
```

### extendValidity($newDate) [​](https://dev.fluentcart.com/database/models/license\#extendvalidity-newdate)

Extend the license expiration date. Passing `'lifetime'` or `null` removes the expiration (lifetime license). Automatically re-activates the license if status is not `active` or `inactive`.

- Parameters
  - $newDate - string\|null (`'lifetime'`, `null`, or a date string)
- Returns `$this`

**Actions Triggered:**

- `fluent_cart_sl/license_validity_extended`

#### Usage [​](https://dev.fluentcart.com/database/models/license\#usage-18)

php

```
$license->extendValidity('2025-12-31');
$license->extendValidity('lifetime'); // Make lifetime
```

### recountActivations() [​](https://dev.fluentcart.com/database/models/license\#recountactivations)

Recount active (non-local) activations and update the `activation_count`. If status is `inactive`, it is set to `active`.

- Parameters
  - none
- Returns `$this`

#### Usage [​](https://dev.fluentcart.com/database/models/license\#usage-19)

php

```
$license->recountActivations();
```

### getDownloads() [​](https://dev.fluentcart.com/database/models/license\#getdownloads)

Get downloadable files associated with the license. Resolves downloads based on product and variation, with download URLs generated via `Helper::generateDownloadFileLink()`.

- Parameters
  - none
- Returns `Collection|array`

#### Usage [​](https://dev.fluentcart.com/database/models/license\#usage-20)

php

```
$downloads = $license->getDownloads();
foreach ($downloads as $download) {
    echo $download->product_title;
    echo $download->download_url;
}
```

### getPreviousOrders() [​](https://dev.fluentcart.com/database/models/license\#getpreviousorders)

Get previous orders associated with this license from the `prev_order_ids` config key.

- Parameters
  - none
- Returns `Collection|array`

#### Usage [​](https://dev.fluentcart.com/database/models/license\#usage-21)

php

```
$previousOrders = $license->getPreviousOrders();
```

### getRenewalUrl() [​](https://dev.fluentcart.com/database/models/license\#getrenewalurl)

Get the renewal URL for an expired license with a subscription. Returns empty string if not expired or no subscription.

- Parameters
  - none
- Returns `string`

#### Usage [​](https://dev.fluentcart.com/database/models/license\#usage-22)

php

```
$renewalUrl = $license->getRenewalUrl();
```

### hasUpgrades() [​](https://dev.fluentcart.com/database/models/license\#hasupgrades)

Check if the license has available upgrade paths. Returns false if the license is not active, or if the order item is a bundle payment type.

- Parameters
  - none
- Returns `boolean`

#### Usage [​](https://dev.fluentcart.com/database/models/license\#usage-23)

php

```
if ($license->hasUpgrades()) {
    // Show upgrade options
}
```

## License Statuses [​](https://dev.fluentcart.com/database/models/license\#license-statuses)

License statuses used in FluentCart Pro:

- `active` \- License is active and can be used
- `inactive` \- License is active but has no activations
- `expired` \- License has expired (derived from expiration\_date)
- `disabled` \- License is disabled

## Usage Examples [​](https://dev.fluentcart.com/database/models/license\#usage-examples)

### Get Customer Licenses [​](https://dev.fluentcart.com/database/models/license\#get-customer-licenses)

php

```
$customer = FluentCart\App\Models\Customer::find(123);
$licenses = $customer->licenses()->status('active')->get();

foreach ($licenses as $license) {
    echo "License: " . $license->license_key . " - " . $license->status;
}
```

### Search Licenses [​](https://dev.fluentcart.com/database/models/license\#search-licenses)

php

```
$licenses = FluentCartPro\App\Modules\Licensing\Models\License::search('example.com')
    ->status('active')
    ->get();
```

### Check License Activation [​](https://dev.fluentcart.com/database/models/license\#check-license-activation)

php

```
$license = FluentCartPro\App\Modules\Licensing\Models\License::find(1);

if ($license->hasActivationLeft()) {
    echo "Remaining activations: " . $license->getActivationLimit();
} else {
    echo "No activations remaining";
}
```

### Get License with Relationships [​](https://dev.fluentcart.com/database/models/license\#get-license-with-relationships)

php

```
$license = FluentCartPro\App\Modules\Licensing\Models\License::with([\
    'customer',\
    'product',\
    'order',\
    'activations'\
])->find(1);
```

### Filter by Products [​](https://dev.fluentcart.com/database/models/license\#filter-by-products)

php

```
$licenses = FluentCartPro\App\Modules\Licensing\Models\License::products([1, 2, 3])
    ->status('active')
    ->get();
```

* * *

**Plugin**: FluentCart Pro

Today

Hi! I’m your AI assistant. How can I assist you today?

Just now

Powered by **FluentBot**


---

---

## License Activation Model | FluentCart Developer Docs

**URL** : https://dev.fluentcart.com/database/models/license-activation

[Skip to content](https://dev.fluentcart.com/database/models/license-activation#VPContent)

Pro

# License Activation Model [​](https://dev.fluentcart.com/database/models/license-activation\#license-activation-model)

| DB Table Name | {wp\_db\_prefix}\_fct\_license\_activations |
| --- | --- |
| Schema | [Check Schema](https://dev.fluentcart.com/database/schema.html#fct-license-activations-table) |
| Source File | fluent-cart-pro/app/Modules/Licensing/Models/LicenseActivation.php |
| Name Space | FluentCartPro\\App\\Modules\\Licensing\\Models |
| Class | FluentCartPro\\App\\Modules\\Licensing\\Models\\LicenseActivation |
| Plugin | FluentCart Pro |

## Properties [​](https://dev.fluentcart.com/database/models/license-activation\#properties)

- **Table**: `fct_license_activations`
- **Primary Key**: `id`
- **Guarded**: `['id']`
- **Fillable**: `['site_id', 'license_id', 'status', 'is_local', 'product_id', 'last_update_date', 'last_update_version', 'variation_id', 'activation_method', 'activation_hash']`

## Attributes [​](https://dev.fluentcart.com/database/models/license-activation\#attributes)

| Attribute | Data Type | Comment |
| --- | --- | --- |
| id | Integer | Primary Key |
| site\_id | Integer | Foreign key to license sites |
| license\_id | Integer | Foreign key to licenses |
| status | String | Activation status |
| is\_local | Boolean | Whether this is a local activation |
| product\_id | Integer | Associated product ID |
| last\_update\_date | DateTime | Last update timestamp |
| last\_update\_version | String | Last update version |
| variation\_id | Integer | Product variation ID |
| activation\_method | String | Method used for activation |
| activation\_hash | String | Unique activation hash |
| created\_at | DateTime | Creation timestamp |
| updated\_at | DateTime | Last update timestamp |

## Usage [​](https://dev.fluentcart.com/database/models/license-activation\#usage)

Please check [Model Basic](https://dev.fluentcart.com/database/models.html) for Common methods.

### Accessing Attributes [​](https://dev.fluentcart.com/database/models/license-activation\#accessing-attributes)

php

```
$activation = FluentCartPro\App\Modules\Licensing\Models\LicenseActivation::find(1);

$activation->id; // returns id
$activation->license_id; // returns license ID
$activation->site_id; // returns site ID
$activation->status; // returns status
$activation->is_local; // returns whether local
$activation->activation_hash; // returns activation hash
```

## Relations [​](https://dev.fluentcart.com/database/models/license-activation\#relations)

This model has the following relationships that you can use

### license [​](https://dev.fluentcart.com/database/models/license-activation\#license)

Access the associated license (BelongsTo)

- return `FluentCartPro\App\Modules\Licensing\Models\License` Model

#### Example: [​](https://dev.fluentcart.com/database/models/license-activation\#example)

php

```
// Accessing License
$license = $activation->license;

// For Filtering by license relationship
$activations = FluentCartPro\App\Modules\Licensing\Models\LicenseActivation::whereHas('license', function($query) {
    $query->where('status', 'active');
})->get();
```

### site [​](https://dev.fluentcart.com/database/models/license-activation\#site)

Access the associated license site (BelongsTo)

- return `FluentCartPro\App\Modules\Licensing\Models\LicenseSite` Model

#### Example: [​](https://dev.fluentcart.com/database/models/license-activation\#example-1)

php

```
// Accessing Site
$site = $activation->site;

// For Filtering by site relationship
$activations = FluentCartPro\App\Modules\Licensing\Models\LicenseActivation::whereHas('site', function($query) {
    $query->where('site_url', 'like', '%example.com%');
})->get();
```

## Methods [​](https://dev.fluentcart.com/database/models/license-activation\#methods)

Along with Global Model methods, this model has few helper methods.

### updateStatus($newStatus) [​](https://dev.fluentcart.com/database/models/license-activation\#updatestatus-newstatus)

Updates the activation status and triggers related action hooks.

- Parameters
  - $newStatus - string - New status value
- Returns `$this` \- Current model instance

**Actions Triggered:**

- `fluent_cart_sl/license_activation_status_updated`
- `fluent_cart_sl/license_activation_status_updated_to_{$newStatus}`

#### Usage [​](https://dev.fluentcart.com/database/models/license-activation\#usage-1)

php

```
$activation = FluentCartPro\App\Modules\Licensing\Models\LicenseActivation::find(1);
$activation->updateStatus('active');
```

## Usage Examples [​](https://dev.fluentcart.com/database/models/license-activation\#usage-examples)

### Creating License Activation [​](https://dev.fluentcart.com/database/models/license-activation\#creating-license-activation)

php

```
use FluentCartPro\App\Modules\Licensing\Models\LicenseActivation;

$activation = LicenseActivation::create([\
    'site_id' => 1,\
    'license_id' => 123,\
    'status' => 'active',\
    'is_local' => false,\
    'product_id' => 456,\
    'variation_id' => 789,\
    'activation_method' => 'api',\
    'activation_hash' => 'unique_hash_here'\
]);
```

### Querying Activations [​](https://dev.fluentcart.com/database/models/license-activation\#querying-activations)

php

```
// Get all activations for a license
$activations = LicenseActivation::where('license_id', 123)->get();

// Get active activations
$activeActivations = LicenseActivation::where('status', 'active')->get();

// Get non-local active activations
$remoteActivations = LicenseActivation::where('status', 'active')
    ->where('is_local', '!=', 1)
    ->get();

// Get activations with license relationship
$activationsWithLicense = LicenseActivation::with('license')->get();

// Get activations with site relationship
$activationsWithSite = LicenseActivation::with('site')->get();
```

### Updating Activation Status [​](https://dev.fluentcart.com/database/models/license-activation\#updating-activation-status)

php

```
$activation = LicenseActivation::find(1);

// Update status (triggers action hooks)
$activation->updateStatus('inactive');

// Direct status update (no action hooks)
$activation->status = 'inactive';
$activation->save();
```

## Related Documentation [​](https://dev.fluentcart.com/database/models/license-activation\#related-documentation)

- [License Model](https://dev.fluentcart.com/database/models/license.html) \- Main license model
- [License Site Model](https://dev.fluentcart.com/database/models/license-site.html) \- Licensed site management
- [License Meta Model](https://dev.fluentcart.com/database/models/license-meta.html) \- License metadata

* * *

**Plugin**: FluentCart Pro

Was this article helpful?

### Comments

Sign in to comment:

No comments yet. Be the first to share your thoughts!

Today

Hi! I’m your AI assistant. How can I assist you today?

Just now

Powered by **FluentBot**


---

---

## License Meta Model | FluentCart Developer Docs

**URL** : https://dev.fluentcart.com/database/models/license-meta

[Skip to content](https://dev.fluentcart.com/database/models/license-meta#VPContent)

Pro

# License Meta Model [​](https://dev.fluentcart.com/database/models/license-meta\#license-meta-model)

| DB Table Name | {wp\_db\_prefix}\_fct\_license\_meta |
| --- | --- |
| Schema | [Check Schema](https://dev.fluentcart.com/database/schema.html#fct-license-meta-table) |
| Source File | fluent-cart-pro/app/Modules/Licensing/Models/LicenseMeta.php |
| Name Space | FluentCartPro\\App\\Modules\\Licensing\\Models |
| Class | FluentCartPro\\App\\Modules\\Licensing\\Models\\LicenseMeta |
| Plugin | FluentCart Pro |

## Properties [​](https://dev.fluentcart.com/database/models/license-meta\#properties)

- **Table**: `fct_license_meta`
- **Primary Key**: `id`
- **Guarded**: `['id']`
- **Fillable**: `['object_id', 'object_type', 'meta_key', 'meta_value']`

Note on Schema

The fillable attributes use `object_id` and `object_type` (not `license_id`). This is a polymorphic-style meta table that can store meta for different object types.

## Attributes [​](https://dev.fluentcart.com/database/models/license-meta\#attributes)

| Attribute | Data Type | Comment |
| --- | --- | --- |
| id | Integer | Primary Key |
| object\_id | Integer | Reference to the parent object (e.g., license ID) |
| object\_type | String | Type of the parent object |
| meta\_key | String | Meta key name |
| meta\_value | Text | Meta value (auto JSON encode/decode via accessor/mutator) |
| created\_at | Date Time | Creation timestamp |
| updated\_at | Date Time | Last update timestamp |

## Usage [​](https://dev.fluentcart.com/database/models/license-meta\#usage)

Please check [Model Basic](https://dev.fluentcart.com/database/models.html) for Common methods.

### Accessing Attributes [​](https://dev.fluentcart.com/database/models/license-meta\#accessing-attributes)

php

```
$licenseMeta = FluentCartPro\App\Modules\Licensing\Models\LicenseMeta::find(1);

$licenseMeta->id; // returns id
$licenseMeta->object_id; // returns object ID
$licenseMeta->object_type; // returns object type
$licenseMeta->meta_key; // returns meta key
$licenseMeta->meta_value; // returns meta value (auto-decoded from JSON if applicable)
```

## Methods [​](https://dev.fluentcart.com/database/models/license-meta\#methods)

Along with Global Model methods, this model has few helper methods.

### getMetaValueAttribute($value) [​](https://dev.fluentcart.com/database/models/license-meta\#getmetavalueattribute-value)

Get meta value with automatic JSON decoding (accessor). If the stored value is a JSON string, it is decoded to an array. Otherwise returns the original value.

- Parameters
  - $value - mixed
- Returns `mixed` \- array if valid JSON string, otherwise original value

#### Usage [​](https://dev.fluentcart.com/database/models/license-meta\#usage-1)

php

```
$metaValue = $licenseMeta->meta_value; // Returns array if JSON, original value otherwise
```

### setMetaValueAttribute($value) [​](https://dev.fluentcart.com/database/models/license-meta\#setmetavalueattribute-value)

Set meta value with automatic JSON encoding (mutator). Arrays and objects are JSON encoded before storage.

- Parameters
  - $value - array\|object\|string
- Returns `void`

#### Usage [​](https://dev.fluentcart.com/database/models/license-meta\#usage-2)

php

```
// Set array value (will be JSON encoded)
$licenseMeta->meta_value = ['site_url' => 'https://example.com', 'activated_at' => '2024-01-01'];

// Set string value (stored as-is)
$licenseMeta->meta_value = 'simple string value';
```

## Usage Examples [​](https://dev.fluentcart.com/database/models/license-meta\#usage-examples)

### Get License Meta [​](https://dev.fluentcart.com/database/models/license-meta\#get-license-meta)

php

```
$licenseMeta = FluentCartPro\App\Modules\Licensing\Models\LicenseMeta::where('object_id', 123)
    ->where('meta_key', 'activation_data')
    ->first();

if ($licenseMeta) {
    $data = $licenseMeta->meta_value; // Returns array (auto-decoded)
}
```

### Set License Custom Meta [​](https://dev.fluentcart.com/database/models/license-meta\#set-license-custom-meta)

php

```
FluentCartPro\App\Modules\Licensing\Models\LicenseMeta::updateOrCreate(
    [\
        'object_id' => 123,\
        'object_type' => 'license',\
        'meta_key' => 'custom_field'\
    ],
    [\
        'meta_value' => ['value' => 'custom data', 'type' => 'text']\
    ]
);
```

### Get All Meta for an Object [​](https://dev.fluentcart.com/database/models/license-meta\#get-all-meta-for-an-object)

php

```
$metaData = FluentCartPro\App\Modules\Licensing\Models\LicenseMeta::where('object_id', 123)
    ->where('object_type', 'license')
    ->pluck('meta_value', 'meta_key')
    ->toArray();
```

### Create License Meta [​](https://dev.fluentcart.com/database/models/license-meta\#create-license-meta)

php

```
$licenseMeta = FluentCartPro\App\Modules\Licensing\Models\LicenseMeta::create([\
    'object_id' => 123,\
    'object_type' => 'license',\
    'meta_key' => 'renewal_info',\
    'meta_value' => ['auto_renew' => true, 'next_date' => '2025-01-01']\
]);
```

### Update License Meta [​](https://dev.fluentcart.com/database/models/license-meta\#update-license-meta)

php

```
$licenseMeta = FluentCartPro\App\Modules\Licensing\Models\LicenseMeta::find(1);
$licenseMeta->update([\
    'meta_value' => ['updated_value' => true]\
]);
```

### Get Meta by Key [​](https://dev.fluentcart.com/database/models/license-meta\#get-meta-by-key)

php

```
$activationMetas = FluentCartPro\App\Modules\Licensing\Models\LicenseMeta::where('meta_key', 'activation_data')->get();
```

### Delete License Meta [​](https://dev.fluentcart.com/database/models/license-meta\#delete-license-meta)

php

```
$licenseMeta = FluentCartPro\App\Modules\Licensing\Models\LicenseMeta::find(1);
$licenseMeta->delete();
```

* * *

**Plugin**: FluentCart Pro

Was this article helpful?

### Comments

Sign in to comment:

No comments yet. Be the first to share your thoughts!

Today

Hi! I’m your AI assistant. How can I assist you today?

Just now

Powered by **FluentBot**


---

---

