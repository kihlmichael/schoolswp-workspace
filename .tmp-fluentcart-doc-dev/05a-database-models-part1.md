# FluentCart Developer Docs - Database Models (Part 1/8)

Tous les modèles Eloquent exposés par FluentCart : orders, customers, products, subscriptions, coupons, licenses, taxes, shipping, etc.

---

## Database Models | FluentCart Developer Docs

**URL** : https://dev.fluentcart.com/database/models

[Skip to content](https://dev.fluentcart.com/database/models#VPContent)

# Database Model Basic [​](https://dev.fluentcart.com/database/models\#database-model-basic)

## Introduction [​](https://dev.fluentcart.com/database/models\#introduction)

FluentCart ORM provides a beautiful, simple ActiveRecord implementation for working with database tables. Each database table has a corresponding "Model" which is used to interact with that table. Models allow you to query for data in db tables, as well as insert new records into the table.

NOTE

FluentCart offers helper functions and methods to interact with FluentCart's database so you may use those things instead of Models directly. We are documenting these for our internal usage and very-high level usage by 3rd-party developers.

## Built-in FluentCart DB Models [​](https://dev.fluentcart.com/database/models\#built-in-fluentcart-db-models)

All the built-in database models are available at

- `fluent-cart/app/Models/` (Core version)
- `fluent-cart-pro/app/Models/` (Pro version)

In this Article we will use `FluentCart\App\Models\Order` model as an example.

## Retrieving Models [​](https://dev.fluentcart.com/database/models\#retrieving-models)

Think of each Eloquent model as a powerful query builder allowing you to fluently query the database table associated with the model. For example:

php

```
<?php

$orders = FluentCart\App\Models\Order::all();

foreach ($orders as $order) {
    echo $order->total_amount;
}
```

### Adding Additional Constraints [​](https://dev.fluentcart.com/database/models\#adding-additional-constraints)

The ORM all method will return all of the results in the model's table. Since each model serves as a query builder, you may also add constraints to queries, and then use the get method to retrieve the results:

php

```
$orders = FluentCart\App\Models\Order::where('status', 'completed')
           ->orderBy('created_at', 'DESC')
           ->limit(10)
           ->skip(5)
           ->get();
```

## Retrieving Single Models / Aggregates [​](https://dev.fluentcart.com/database/models\#retrieving-single-models-aggregates)

Of course, in addition to retrieving all of the records for a given table, you may also retrieve single records using find or first. Instead of returning a collection of models, these methods return a single model instance:

php

```
// Retrieve a model by its primary key...
$order = FluentCart\App\Models\Order::find(1);

// Retrieve the first model matching the query constraints...
$order = FluentCart\App\Models\Order::where('status', 'pending')->first();
```

You may also call the find method with an array of primary keys, which will return a collection of the matching records:

php

```
$orders = FluentCart\App\Models\Order::find([1,2,3]);
```

## Retrieving Aggregates [​](https://dev.fluentcart.com/database/models\#retrieving-aggregates)

You may also use the count, sum, max, and other aggregate methods available. These methods return the appropriate scalar value instead of a full model instance:

php

```
$count = FluentCart\App\Models\Order::where('status', 'completed')->count();

$max = FluentCart\App\Models\Order::where('status', 'completed')->max('total_amount');
```

Available aggregate methods such as `count`, `max`, `min`, `avg`, and `sum`.

## Inserting & Updating Models [​](https://dev.fluentcart.com/database/models\#inserting-updating-models)

### Inserts [​](https://dev.fluentcart.com/database/models\#inserts)

To create a new record in the database, create a new model instance, set attributes on the model, then call the save method:

php

```
$order = FluentCart\App\Models\Order::create([\
    'customer_id' => 1,\
    'status' => 'pending',\
    'payment_method' => 'stripe',\
    'currency' => 'USD',\
    'total_amount' => Helper::toCent(99.99)\
]);
```

### Updates [​](https://dev.fluentcart.com/database/models\#updates)

You can update a model few different way. You can assign property and then call `save()` method

php

```
$order = FluentCart\App\Models\Order::find(1);

$order->status = 'completed';
$order->completed_at = now();
$order->save();
```

You can also update with an array

php

```
$order = FluentCart\App\Models\Order::find(1);

$order->update([\
    'status' => 'completed',\
    'completed_at' => now()\
]);
```

## Accessing Attributes [​](https://dev.fluentcart.com/database/models\#accessing-attributes)

You can just call the database table column name for accessing the attributes

php

```
$order = FluentCart\App\Models\Order::find(1);

$status = $order->status;
$totalAmount = $order->total_amount;
$customerId = $order->customer_id;
```

## Deleting Models [​](https://dev.fluentcart.com/database/models\#deleting-models)

To delete a model, call the delete method on a model instance:

php

```
$order = FluentCart\App\Models\Order::find(1);
$order->delete();
```

### Deleting Models By Query [​](https://dev.fluentcart.com/database/models\#deleting-models-by-query)

Of course, you may also run a delete statement on a set of models. In this example, we will delete all orders that are marked as draft. Like mass updates, mass deletes will not fire any model events for the models that are deleted:

php

```
FluentCart\App\Models\Order::where('status', 'draft')->delete();
```

## Query Scopes [​](https://dev.fluentcart.com/database/models\#query-scopes)

Scopes allow you to define common sets of constraints that you may easily re-use throughout application. For example, you may need to frequently retrieve all orders by given statuses. In FluentCart Order model we already have this scope defined like this.

php

```
/**
 * Local scope to filter orders by status
 * @param \FluentCart\Framework\Database\Query\Builder $query
 * @param string $status
 * @return \FluentCart\Framework\Database\Query\Builder $query
 */
public function scopeOfStatus($query, $status)
{
    return $query->where('status', $status);
}
```

Now say you want to get orders where status equal completed

php

```
$orders = FluentCart\App\Models\Order::ofStatus('completed')->get();
```

Please note that, the first letter will be small case.

In the individual model documentation, you will find which FluentCart models have scopes.

## Relationships [​](https://dev.fluentcart.com/database/models\#relationships)

Database tables are often related to one another. For example, a customer has multiple orders, or an order has multiple order items. FluentCart ORM makes managing and working with these relationships easy. Each Model has predefined relationships and you will find those in the individual model documentation.

php

```
$customer = FluentCart\App\Models\Customer::find(1);

// These will return corresponding Order and Subscription collections
$customerOrders = $customer->orders;
$customerSubscriptions = $customer->subscriptions;
```

For a single relation like an `OrderItem` belongs to an order

php

```
$orderItem = FluentCart\App\Models\OrderItem::find(1);
$order = $orderItem->order; // will return FluentCart\App\Models\Order
```

## Available Models [​](https://dev.fluentcart.com/database/models\#available-models)

### Core Models [​](https://dev.fluentcart.com/database/models\#core-models)

#### Order Models [​](https://dev.fluentcart.com/database/models\#order-models)

- **[Order Model](https://dev.fluentcart.com/database/models/order.html)** \- Main order management
- **[OrderItem Model](https://dev.fluentcart.com/database/models/order-item.html)** \- Individual order items
- **[OrderTransaction Model](https://dev.fluentcart.com/database/models/order-transaction.html)** \- Payment transactions
- **[OrderAddress Model](https://dev.fluentcart.com/database/models/order-address.html)** \- Order addresses
- **[OrderMeta Model](https://dev.fluentcart.com/database/models/order-meta.html)** \- Order metadata
- **[OrderOperation Model](https://dev.fluentcart.com/database/models/order-operation.html)** \- Order operations
- **[OrderTaxRate Model](https://dev.fluentcart.com/database/models/order-tax-rate.html)** \- Tax calculations
- **[OrderDownloadPermission Model](https://dev.fluentcart.com/database/models/order-download-permission.html)** \- Download permissions

#### Customer Models [​](https://dev.fluentcart.com/database/models\#customer-models)

- **[Customer Model](https://dev.fluentcart.com/database/models/customer.html)** \- Customer management
- **[CustomerAddresses Model](https://dev.fluentcart.com/database/models/customer-addresses.html)** \- Customer addresses
- **[CustomerMeta Model](https://dev.fluentcart.com/database/models/customer-meta.html)** \- Customer metadata

#### Product Models [​](https://dev.fluentcart.com/database/models\#product-models)

- **[Product Model](https://dev.fluentcart.com/database/models/product.html)** \- Product management
- **[ProductDetail Model](https://dev.fluentcart.com/database/models/product-detail.html)** \- Product details
- **[ProductVariation Model](https://dev.fluentcart.com/database/models/product-variation.html)** \- Product variations
- **[ProductMeta Model](https://dev.fluentcart.com/database/models/product-meta.html)** \- Product metadata
- **[ProductDownload Model](https://dev.fluentcart.com/database/models/product-download.html)** \- Product downloads

#### Subscription Models [​](https://dev.fluentcart.com/database/models\#subscription-models)

- **[Subscription Model](https://dev.fluentcart.com/database/models/subscription.html)** \- Subscription management
- **[SubscriptionMeta Model](https://dev.fluentcart.com/database/models/subscription-meta.html)** \- Subscription metadata

#### Cart & Coupon Models [​](https://dev.fluentcart.com/database/models\#cart-coupon-models)

- **[Cart Model](https://dev.fluentcart.com/database/models/cart.html)** \- Shopping cart management
- **[Coupon Model](https://dev.fluentcart.com/database/models/coupon.html)** \- Coupon management
- **[AppliedCoupon Model](https://dev.fluentcart.com/database/models/applied-coupon.html)** \- Applied coupons

#### System Models [​](https://dev.fluentcart.com/database/models\#system-models)

- **[Activity Model](https://dev.fluentcart.com/database/models/activity.html)** \- Activity logging and audit trails
- **[ScheduledAction Model](https://dev.fluentcart.com/database/models/scheduled-action.html)** \- Background job scheduling
- **[Meta Model](https://dev.fluentcart.com/database/models/meta.html)** \- Generic metadata storage
- **[User Model](https://dev.fluentcart.com/database/models/user.html)** \- WordPress user integration
- **[DynamicModel Model](https://dev.fluentcart.com/database/models/dynamic-model.html)** \- Dynamic model functionality

#### Attribute System Models [​](https://dev.fluentcart.com/database/models\#attribute-system-models)

- **[AttributeGroup Model](https://dev.fluentcart.com/database/models/attribute-group.html)** \- Attribute groups (e.g., Color, Size)
- **[AttributeTerm Model](https://dev.fluentcart.com/database/models/attribute-term.html)** \- Attribute terms within groups
- **[AttributeRelation Model](https://dev.fluentcart.com/database/models/attribute-relation.html)** \- Attribute relationships

#### Shipping & Tax Models [​](https://dev.fluentcart.com/database/models\#shipping-tax-models)

- **[ShippingZone Model](https://dev.fluentcart.com/database/models/shipping-zone.html)** \- Shipping zones and regions
- **[ShippingMethod Model](https://dev.fluentcart.com/database/models/shipping-method.html)** \- Shipping methods and rates
- **[ShippingClass Model](https://dev.fluentcart.com/database/models/shipping-class.html)** \- Shipping classes and rules
- **[TaxClass Model](https://dev.fluentcart.com/database/models/tax-class.html)** \- Tax classes and categories
- **[TaxRate Model](https://dev.fluentcart.com/database/models/tax-rate.html)** \- Tax rates and calculations

#### Label System Models [​](https://dev.fluentcart.com/database/models\#label-system-models)

- **[Label Model](https://dev.fluentcart.com/database/models/label.html)** \- Customer labeling system
- **[LabelRelationship Model](https://dev.fluentcart.com/database/models/label-relationship.html)** \- Polymorphic label relationships

### Pro Plugin Models [​](https://dev.fluentcart.com/database/models\#pro-plugin-models)

#### Licensing Models [​](https://dev.fluentcart.com/database/models\#licensing-models)

- **[License Model](https://dev.fluentcart.com/database/models/license.html)** \- Software licenses
- **[LicenseActivation Model](https://dev.fluentcart.com/database/models/license-activation.html)** \- License activations
- **[LicenseSite Model](https://dev.fluentcart.com/database/models/license-site.html)** \- Licensed sites
- **[LicenseMeta Model](https://dev.fluentcart.com/database/models/license-meta.html)** \- License metadata

#### Promotional Models [​](https://dev.fluentcart.com/database/models\#promotional-models)

- **[OrderPromotion Model](https://dev.fluentcart.com/database/models/order-promotion.html)** \- Order promotions
- **[OrderPromotionStat Model](https://dev.fluentcart.com/database/models/order-promotion-stat.html)** \- Promotion statistics

#### User Management Models [​](https://dev.fluentcart.com/database/models\#user-management-models)

- **[UserMeta Model](https://dev.fluentcart.com/database/models/user-meta.html)** \- User metadata

## Model Usage Examples [​](https://dev.fluentcart.com/database/models\#model-usage-examples)

### Activity Logging [​](https://dev.fluentcart.com/database/models\#activity-logging)

php

```
// Create activity log
$activity = FluentCart\App\Models\Activity::create([\
    'status' => 'success',\
    'log_type' => 'activity',\
    'module_type' => 'FluentCart\App\Models\Order',\
    'module_id' => 123,\
    'module_name' => 'order',\
    'title' => 'Order Status Updated',\
    'content' => 'Order status changed from pending to completed',\
    'user_id' => 1,\
    'created_by' => 'admin'\
]);

// Get activity logs for an order
$orderActivities = FluentCart\App\Models\Activity::where('module_type', 'FluentCart\App\Models\Order')
    ->where('module_id', 123)
    ->orderBy('created_at', 'desc')
    ->get();
```

### Attribute Management [​](https://dev.fluentcart.com/database/models\#attribute-management)

php

```
// Create attribute group
$colorGroup = FluentCart\App\Models\AttributeGroup::create([\
    'title' => 'Color',\
    'slug' => 'color',\
    'description' => 'Product color attributes'\
]);

// Add terms to group
$redTerm = FluentCart\App\Models\AttributeTerm::create([\
    'group_id' => $colorGroup->id,\
    'title' => 'Red',\
    'slug' => 'red'\
]);

// Relate attribute to product
FluentCart\App\Models\AttributeRelation::create([\
    'group_id' => $colorGroup->id,\
    'term_id' => $redTerm->id,\
    'object_id' => 456 // Product ID\
]);
```

### Label System [​](https://dev.fluentcart.com/database/models\#label-system)

php

```
// Create label
$label = FluentCart\App\Models\Label::create([\
    'value' => 'featured'\
]);

// Tag an order with label
FluentCart\App\Models\LabelRelationship::create([\
    'label_id' => $label->id,\
    'labelable_id' => 123,\
    'labelable_type' => 'FluentCart\App\Models\Order'\
]);

// Get all orders with 'featured' label
$featuredOrders = FluentCart\App\Models\Order::whereHas('labels', function($query) {
    $query->where('value', 'featured');
})->get();
```

### Scheduled Actions [​](https://dev.fluentcart.com/database/models\#scheduled-actions)

php

```
// Schedule a background job
FluentCart\App\Models\ScheduledAction::create([\
    'scheduled_at' => now()->addMinutes(30),\
    'action' => 'send_order_confirmation',\
    'status' => 'pending',\
    'group' => 'order',\
    'object_id' => 123,\
    'object_type' => 'FluentCart\App\Models\Order',\
    'data' => ['email' => 'customer@example.com']\
]);

// Get pending scheduled actions
$pendingActions = FluentCart\App\Models\ScheduledAction::where('status', 'pending')
    ->where('scheduled_at', '<=', now())
    ->get();
```

### Pro Licensing [​](https://dev.fluentcart.com/database/models\#pro-licensing)

php

```
// Create license
$license = FluentCartPro\App\Modules\Licensing\Models\License::create([\
    'status' => 'active',\
    'limit' => 5,\
    'license_key' => 'ABC123-DEF456-GHI789',\
    'product_id' => 456,\
    'customer_id' => 789,\
    'order_id' => 123,\
    'expiration_date' => now()->addYear()\
]);

// Activate license on site
FluentCartPro\App\Modules\Licensing\Models\LicenseActivation::create([\
    'site_id' => 1,\
    'license_id' => $license->id,\
    'status' => 'active',\
    'product_id' => 456,\
    'activation_hash' => 'unique_hash_here'\
]);
```

* * *

Today

Hi! I’m your AI assistant. How can I assist you today?

Just now

Powered by **FluentBot**


---

---

## Activity Model | FluentCart Developer Docs

**URL** : https://dev.fluentcart.com/database/models/activity

[Skip to content](https://dev.fluentcart.com/database/models/activity#VPContent)

# Activity Model [​](https://dev.fluentcart.com/database/models/activity\#activity-model)

| DB Table Name | {wp\_db\_prefix}\_fct\_activity |
| --- | --- |
| Schema | [Check Schema](https://dev.fluentcart.com/database/schema.html#fct-activity-table) |
| Source File | fluent-cart/app/Models/Activity.php |
| Name Space | FluentCart\\App\\Models |
| Class | FluentCart\\App\\Models\\Activity |

## Traits [​](https://dev.fluentcart.com/database/models/activity\#traits)

| Trait | Description |
| --- | --- |
| CanSearch | Provides `search()`, `groupSearch()`, `whereLike()`, `whereBeginsWith()`, `whereEndsWith()` query scopes |

## Attributes [​](https://dev.fluentcart.com/database/models/activity\#attributes)

| Attribute | Data Type | Comment |
| --- | --- | --- |
| id | Integer | Primary Key (guarded) |
| status | String | Activity status (success, warning, failed, info) |
| log\_type | String | Log type (activity, api, etc.) |
| module\_id | Integer | Module ID (cast to integer) |
| module\_type | String | Module type (full model path) |
| module\_name | String | Module name (order, product, user, etc.) |
| title | String | Activity title |
| content | Text | Activity content |
| user\_id | Integer | User ID |
| read\_status | String | Read status (read, unread) |
| created\_by | String | Created by (FCT-BOT, username) |
| created\_at | Date Time | Creation timestamp |
| updated\_at | Date Time | Last update timestamp |

## Casts [​](https://dev.fluentcart.com/database/models/activity\#casts)

| Attribute | Cast Type |
| --- | --- |
| module\_id | integer |

## Usage [​](https://dev.fluentcart.com/database/models/activity\#usage)

Please check [Model Basic](https://dev.fluentcart.com/database/models.html) for Common methods.

### Accessing Attributes [​](https://dev.fluentcart.com/database/models/activity\#accessing-attributes)

php

```
$activity = FluentCart\App\Models\Activity::find(1);

$activity->id; // returns activity ID
$activity->status; // returns activity status
$activity->title; // returns activity title
$activity->content; // returns activity content
$activity->module_name; // returns module name
$activity->module_id; // returns module ID (always cast to integer)
```

## Relations [​](https://dev.fluentcart.com/database/models/activity\#relations)

This model has the following relationships that you can use

### activity [​](https://dev.fluentcart.com/database/models/activity\#activity)

Access the parent activity model (polymorphic). Uses `module_type` and `module_id` columns for polymorphic resolution.

- Returns `MorphTo` \- Polymorphic relationship

php

```
$activity = FluentCart\App\Models\Activity::find(1);
$parentModel = $activity->activity; // Returns the related model (Order, Product, etc.)
```

### user [​](https://dev.fluentcart.com/database/models/activity\#user)

Access the user who performed the activity. Returns a limited set of columns (`ID`, `display_name`, `user_email`) for performance.

- Returns `FluentCart\App\Models\User` Model (HasOne via `user_id` -\> `ID`)
- Selected columns: `ID`, `display_name`, `user_email`

php

```
$activity = FluentCart\App\Models\Activity::find(1);
$user = $activity->user;

if ($user) {
    echo $user->display_name;
    echo $user->user_email;
}
```

## Scopes [​](https://dev.fluentcart.com/database/models/activity\#scopes)

This model has the following scopes that you can use

This model uses the `CanSearch` trait which provides search functionality.

### search($params) from CanSearch [​](https://dev.fluentcart.com/database/models/activity\#search-params)

Search activities by parameters. Supports operators: `=`, `between`, `like_all`, `in`, `not_in`, `is_null`, `is_not_null`, and more.

- Parameters: `$params` (Array) - Search parameters

php

```
$activities = FluentCart\App\Models\Activity::search([\
    'status' => ['value' => 'success', 'operator' => '=']\
])->get();

// Multiple search criteria
$activities = FluentCart\App\Models\Activity::search([\
    'module_name' => ['value' => 'order', 'operator' => '='],\
    'status' => ['value' => 'success', 'operator' => '=']\
])->get();
```

## Usage Examples [​](https://dev.fluentcart.com/database/models/activity\#usage-examples)

### Creating an Activity [​](https://dev.fluentcart.com/database/models/activity\#creating-an-activity)

php

```
use FluentCart\App\Models\Activity;

$activity = Activity::create([\
    'status' => 'success',\
    'log_type' => 'activity',\
    'module_type' => 'FluentCart\App\Models\Order',\
    'module_id' => 123,\
    'module_name' => 'order',\
    'user_id' => 1,\
    'title' => 'Order Status Updated',\
    'content' => 'Order status changed from pending to completed',\
    'created_by' => 'admin'\
]);
```

### Retrieving Activities [​](https://dev.fluentcart.com/database/models/activity\#retrieving-activities)

php

```
// Get activity by ID
$activity = Activity::find(1);

// Get activities by status
$activities = Activity::where('status', 'success')->get();

// Get activities by module
$activities = Activity::where('module_name', 'order')->get();

// Get unread activities
$activities = Activity::where('read_status', 'unread')->get();
```

### Loading Activity with User [​](https://dev.fluentcart.com/database/models/activity\#loading-activity-with-user)

php

```
$activity = Activity::with('user')->find(1);
echo $activity->user->display_name; // Only ID, display_name, user_email are loaded
```

### Updating an Activity [​](https://dev.fluentcart.com/database/models/activity\#updating-an-activity)

php

```
$activity = Activity::find(1);
$activity->read_status = 'read';
$activity->save();
```

### Deleting an Activity [​](https://dev.fluentcart.com/database/models/activity\#deleting-an-activity)

php

```
$activity = Activity::find(1);
$activity->delete();
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

## Applied Coupon Model | FluentCart Developer Docs

**URL** : https://dev.fluentcart.com/database/models/applied-coupon

[Skip to content](https://dev.fluentcart.com/database/models/applied-coupon#VPContent)

# Applied Coupon Model [​](https://dev.fluentcart.com/database/models/applied-coupon\#applied-coupon-model)

| DB Table Name | {wp\_db\_prefix}\_fct\_applied\_coupons |
| --- | --- |
| Schema | [Check Schema](https://dev.fluentcart.com/database/schema.html#fct-applied-coupons-table) |
| Source File | fluent-cart/app/Models/AppliedCoupon.php |
| Name Space | FluentCart\\App\\Models |
| Class | FluentCart\\App\\Models\\AppliedCoupon |

## Traits [​](https://dev.fluentcart.com/database/models/applied-coupon\#traits)

- **CanUpdateBatch** \- Provides `batchUpdate()` scope for batch updating multiple records

## Attributes [​](https://dev.fluentcart.com/database/models/applied-coupon\#attributes)

| Attribute | Data Type | Comment |
| --- | --- | --- |
| id | Integer | Primary Key (guarded) |
| order\_id | Integer | Reference to order |
| coupon\_id | Integer | Reference to coupon |
| code | String | Coupon code |
| amount | Decimal | Discount amount applied (in cents) |
| settings | JSON | (Dynamic/Meta) Coupon settings, may not be a physical DB column |
| other\_info | JSON | (Dynamic/Meta) Additional coupon information (buy/get product IDs), may not be a physical DB column |
| categories | JSON | (Dynamic/Meta) Product categories, may not be a physical DB column |
| products | JSON | (Dynamic/Meta) Product IDs (stored as integers), may not be a physical DB column |
| created\_at | Date Time | Creation timestamp |
| updated\_at | Date Time | Last update timestamp |

> **Note:** Some fields above (settings, other\_info, categories, products) are handled as dynamic/meta properties in the model and may not exist as physical columns in the database schema. They are available via accessors/mutators for developer convenience. The `id` column is both guarded and declared as `$primaryKey`.

## Usage [​](https://dev.fluentcart.com/database/models/applied-coupon\#usage)

Please check [Model Basic](https://dev.fluentcart.com/database/models.html) for Common methods.

### Accessing Attributes [​](https://dev.fluentcart.com/database/models/applied-coupon\#accessing-attributes)

php

```
$appliedCoupon = FluentCart\App\Models\AppliedCoupon::find(1);

$appliedCoupon->id; // returns id
$appliedCoupon->order_id; // returns order ID
$appliedCoupon->coupon_id; // returns coupon ID
$appliedCoupon->code; // returns coupon code
$appliedCoupon->amount; // returns discount amount
```

## Scopes [​](https://dev.fluentcart.com/database/models/applied-coupon\#scopes)

This model has the following scopes via the `CanUpdateBatch` trait.

### batchUpdate($values, $index = null) [​](https://dev.fluentcart.com/database/models/applied-coupon\#batchupdate-values-index-null)

Batch update multiple records at once. Uses the primary key as the default index column.

- Parameters
  - $values - array of records to update
  - $index - string\|null (default: primary key)

#### Usage: [​](https://dev.fluentcart.com/database/models/applied-coupon\#usage-1)

php

```
FluentCart\App\Models\AppliedCoupon::batchUpdate([\
    ['id' => 1, 'amount' => 500],\
    ['id' => 2, 'amount' => 1000],\
]);
```

## Relations [​](https://dev.fluentcart.com/database/models/applied-coupon\#relations)

This model has the following relationships that you can use

### order [​](https://dev.fluentcart.com/database/models/applied-coupon\#order)

Access the associated order

- return `FluentCart\App\Models\Order` Model

#### Example: [​](https://dev.fluentcart.com/database/models/applied-coupon\#example)

php

```
// Accessing Order
$order = $appliedCoupon->order;

// For Filtering by order relationship
$appliedCoupons = FluentCart\App\Models\AppliedCoupon::whereHas('order', function($query) {
    $query->where('status', 'completed');
})->get();
```

### coupon [​](https://dev.fluentcart.com/database/models/applied-coupon\#coupon)

Access the associated coupon. This relationship uses `code` as the foreign key and `id` as the owner key on the `Coupon` model.

- return `FluentCart\App\Models\Coupon` Model

#### Example: [​](https://dev.fluentcart.com/database/models/applied-coupon\#example-1)

php

```
// Accessing Coupon
$coupon = $appliedCoupon->coupon;

// For Filtering by coupon relationship
$appliedCoupons = FluentCart\App\Models\AppliedCoupon::whereHas('coupon', function($query) {
    $query->where('status', 'active');
})->get();
```

## Methods [​](https://dev.fluentcart.com/database/models/applied-coupon\#methods)

Along with Global Model methods, this model has few helper methods.

### setSettingsAttribute($value) [​](https://dev.fluentcart.com/database/models/applied-coupon\#setsettingsattribute-value)

Set settings with automatic JSON encoding (mutator). Uses `JSON_UNESCAPED_UNICODE | JSON_UNESCAPED_SLASHES` flags. Stores the encoded value in the `meta_value` column.

- Parameters
  - $value - mixed (array, object, or string)
- Returns `void`

#### Usage [​](https://dev.fluentcart.com/database/models/applied-coupon\#usage-2)

php

```
$appliedCoupon->settings = ['discount_type' => 'percentage', 'value' => 10];
// Automatically JSON encodes arrays and objects
```

### getSettingsAttribute($value) [​](https://dev.fluentcart.com/database/models/applied-coupon\#getsettingsattribute-value)

Get settings with automatic JSON decoding (accessor). Returns decoded array if valid JSON, otherwise returns the original value.

- Parameters
  - $value - mixed
- Returns `mixed`

#### Usage [​](https://dev.fluentcart.com/database/models/applied-coupon\#usage-3)

php

```
$settings = $appliedCoupon->settings; // Returns decoded value (array, object, or string)
```

### setOtherInfoAttribute($value) [​](https://dev.fluentcart.com/database/models/applied-coupon\#setotherinfoattribute-value)

Set other info with automatic JSON encoding and product ID conversion (mutator). Accepts JSON strings, arrays, or objects. Automatically converts `buy_products` and `get_products` arrays to integer values.

- Parameters
  - $value - mixed (array, object, or JSON string)
- Returns `void`

#### Usage [​](https://dev.fluentcart.com/database/models/applied-coupon\#usage-4)

php

```
$appliedCoupon->other_info = [\
    'buy_products' => [1, 2, 3],\
    'get_products' => [4, 5, 6]\
];
// Automatically JSON encodes and converts product IDs to integers
```

### getOtherInfoAttribute($value) [​](https://dev.fluentcart.com/database/models/applied-coupon\#getotherinfoattribute-value)

Get other info with automatic JSON decoding (accessor). Returns empty array if value is empty.

- Parameters
  - $value - mixed
- Returns `array`

#### Usage [​](https://dev.fluentcart.com/database/models/applied-coupon\#usage-5)

php

```
$otherInfo = $appliedCoupon->other_info; // Returns decoded array or empty array
```

### setCategoriesAttribute($value) [​](https://dev.fluentcart.com/database/models/applied-coupon\#setcategoriesattribute-value)

Set categories with automatic JSON encoding (mutator). Arrays and objects are JSON-encoded; other types result in an empty JSON array.

- Parameters
  - $value - mixed (array, object, or string)
- Returns `void`

#### Usage [​](https://dev.fluentcart.com/database/models/applied-coupon\#usage-6)

php

```
$appliedCoupon->categories = ['electronics', 'books', 'clothing'];
// Automatically JSON encodes arrays and objects
```

### getCategoriesAttribute($value) [​](https://dev.fluentcart.com/database/models/applied-coupon\#getcategoriesattribute-value)

Get categories with automatic JSON decoding (accessor). Returns empty array if value is empty.

- Parameters
  - $value - mixed
- Returns `array`

#### Usage [​](https://dev.fluentcart.com/database/models/applied-coupon\#usage-7)

php

```
$categories = $appliedCoupon->categories; // Returns decoded array or empty array
```

### setProductsAttribute($value) [​](https://dev.fluentcart.com/database/models/applied-coupon\#setproductsattribute-value)

Set products with automatic JSON encoding and integer conversion (mutator). Each item in the array is converted to an integer via `intval()`. Non-array/object values result in an empty JSON array.

- Parameters
  - $value - mixed (array, object, or string)
- Returns `void`

#### Usage [​](https://dev.fluentcart.com/database/models/applied-coupon\#usage-8)

php

```
$appliedCoupon->products = [1, 2, 3, 4, 5];
// Automatically JSON encodes and converts to integers
```

### getProductsAttribute($value) [​](https://dev.fluentcart.com/database/models/applied-coupon\#getproductsattribute-value)

Get products with automatic JSON decoding (accessor). Returns empty array if value is empty.

- Parameters
  - $value - mixed
- Returns `array`

#### Usage [​](https://dev.fluentcart.com/database/models/applied-coupon\#usage-9)

php

```
$products = $appliedCoupon->products; // Returns decoded array of integers or empty array
```

## Usage Examples [​](https://dev.fluentcart.com/database/models/applied-coupon\#usage-examples)

### Get Applied Coupons [​](https://dev.fluentcart.com/database/models/applied-coupon\#get-applied-coupons)

php

```
$appliedCoupon = FluentCart\App\Models\AppliedCoupon::find(1);
echo "Coupon Code: " . $appliedCoupon->code;
echo "Discount Amount: " . $appliedCoupon->amount;
echo "Order ID: " . $appliedCoupon->order_id;
```

### Get Coupons Applied to Order [​](https://dev.fluentcart.com/database/models/applied-coupon\#get-coupons-applied-to-order)

php

```
$order = FluentCart\App\Models\Order::find(123);
$appliedCoupons = $order->applied_coupons;

foreach ($appliedCoupons as $appliedCoupon) {
    echo "Coupon: " . $appliedCoupon->code;
    echo "Discount: " . $appliedCoupon->amount;
}
```

### Create Applied Coupon [​](https://dev.fluentcart.com/database/models/applied-coupon\#create-applied-coupon)

php

```
$appliedCoupon = FluentCart\App\Models\AppliedCoupon::create([\
    'order_id' => 123,\
    'coupon_id' => 5,\
    'code' => 'SAVE10',\
    'amount' => 1000,\
]);
```

### Get Coupon Details [​](https://dev.fluentcart.com/database/models/applied-coupon\#get-coupon-details)

php

```
$appliedCoupon = FluentCart\App\Models\AppliedCoupon::with(['order', 'coupon'])->find(1);
$order = $appliedCoupon->order;
$coupon = $appliedCoupon->coupon;
```

### Get Applied Coupons by Code [​](https://dev.fluentcart.com/database/models/applied-coupon\#get-applied-coupons-by-code)

php

```
$appliedCoupons = FluentCart\App\Models\AppliedCoupon::where('code', 'SAVE10')->get();
```

### Get Applied Coupons for Date Range [​](https://dev.fluentcart.com/database/models/applied-coupon\#get-applied-coupons-for-date-range)

php

```
$appliedCoupons = FluentCart\App\Models\AppliedCoupon::whereBetween('created_at', ['2024-01-01', '2024-01-31'])->get();
```

### Batch Update Coupon Amounts [​](https://dev.fluentcart.com/database/models/applied-coupon\#batch-update-coupon-amounts)

php

```
FluentCart\App\Models\AppliedCoupon::batchUpdate([\
    ['id' => 1, 'amount' => 500],\
    ['id' => 2, 'amount' => 1500],\
    ['id' => 3, 'amount' => 2000],\
]);
```

* * *

Today

Hi! I’m your AI assistant. How can I assist you today?

Just now

Powered by **FluentBot**


---

---

## Attribute Group Model | FluentCart Developer Docs

**URL** : https://dev.fluentcart.com/database/models/attribute-group

[Skip to content](https://dev.fluentcart.com/database/models/attribute-group#VPContent)

# Attribute Group Model [​](https://dev.fluentcart.com/database/models/attribute-group\#attribute-group-model)

| DB Table Name | {wp\_db\_prefix}\_fct\_atts\_groups |
| --- | --- |
| Schema | [Check Schema](https://dev.fluentcart.com/database/schema.html#fct-atts-groups-table) |
| Source File | fluent-cart/app/Models/AttributeGroup.php |
| Name Space | FluentCart\\App\\Models |
| Class | FluentCart\\App\\Models\\AttributeGroup |

## Traits [​](https://dev.fluentcart.com/database/models/attribute-group\#traits)

- **CanSearch** (`FluentCart\App\Models\Concerns\CanSearch`) \- Provides `search()`, `groupSearch()`, `whereLike()`, `whereBeginsWith()`, and `whereEndsWith()` query scopes.

## Attributes [​](https://dev.fluentcart.com/database/models/attribute-group\#attributes)

| Attribute | Data Type | Comment |
| --- | --- | --- |
| id | Integer | Primary Key |
| title | String | Attribute group title (e.g., Color, Size) |
| slug | String | Attribute group slug |
| description | Text | Attribute group description |
| settings | JSON | Attribute group settings |
| created\_at | Date Time | Creation timestamp |
| updated\_at | Date Time | Last update timestamp |

## Boot Events [​](https://dev.fluentcart.com/database/models/attribute-group\#boot-events)

The model registers a `deleting` event in the `boot()` method that automatically deletes all associated terms when an attribute group is deleted:

php

```
static::deleting(function ($model) {
    $model->terms()->delete();
});
```

## Usage [​](https://dev.fluentcart.com/database/models/attribute-group\#usage)

Please check [Model Basic](https://dev.fluentcart.com/database/models.html) for Common methods.

### Accessing Attributes [​](https://dev.fluentcart.com/database/models/attribute-group\#accessing-attributes)

php

```
$attributeGroup = FluentCart\App\Models\AttributeGroup::find(1);

$attributeGroup->id; // returns id
$attributeGroup->title; // returns title
$attributeGroup->slug; // returns slug
$attributeGroup->description; // returns description
$attributeGroup->settings; // returns settings (auto-decoded from JSON)
```

## Scopes [​](https://dev.fluentcart.com/database/models/attribute-group\#scopes)

This model has the following scopes that you can use

### applyCustomFilters($filters) [​](https://dev.fluentcart.com/database/models/attribute-group\#applycustomfilters-filters)

Apply custom filters to the query. Accepts filters for any fillable attribute plus a special `terms_count` filter for filtering by the number of associated terms. Supported operators: `includes` (LIKE), `not_includes` (NOT LIKE), `gt` (>), `lt` (<), and standard SQL comparison operators for `terms_count`.

- Parameters
  - $filters - array of filter arrays, each with `value` and `operator` keys

#### Usage: [​](https://dev.fluentcart.com/database/models/attribute-group\#usage-1)

php

```
// Apply custom filters
$filteredGroups = FluentCart\App\Models\AttributeGroup::applyCustomFilters([\
    'title' => ['value' => 'Color', 'operator' => 'includes'],\
    'terms_count' => ['value' => 5, 'operator' => 'gt']\
])->get();
```

## Relations [​](https://dev.fluentcart.com/database/models/attribute-group\#relations)

This model has the following relationships that you can use

### terms [​](https://dev.fluentcart.com/database/models/attribute-group\#terms)

Access all attribute terms in this group (`hasMany`)

- return `FluentCart\App\Models\AttributeTerm` Model Collection

#### Example: [​](https://dev.fluentcart.com/database/models/attribute-group\#example)

php

```
// Accessing Terms
$terms = $attributeGroup->terms;

// For Filtering by terms relationship
$attributeGroups = FluentCart\App\Models\AttributeGroup::whereHas('terms', function($query) {
    $query->where('title', 'Red');
})->get();
```

### usedTerms [​](https://dev.fluentcart.com/database/models/attribute-group\#usedterms)

Access all used attribute relations for this group (`hasMany`). Returns `AttributeRelation` records linked by `group_id`.

- return `FluentCart\App\Models\AttributeRelation` Model Collection

#### Example: [​](https://dev.fluentcart.com/database/models/attribute-group\#example-1)

php

```
// Accessing Used Terms
$usedTerms = $attributeGroup->usedTerms;

// For Filtering by used terms relationship
$attributeGroups = FluentCart\App\Models\AttributeGroup::whereHas('usedTerms', function($query) {
    $query->where('term_id', 5);
})->get();
```

## Methods [​](https://dev.fluentcart.com/database/models/attribute-group\#methods)

Along with Global Model methods, this model has few helper methods.

### setSettingsAttribute($value) [​](https://dev.fluentcart.com/database/models/attribute-group\#setsettingsattribute-value)

Set settings with automatic JSON encoding (mutator). If the value is an array, it is JSON-encoded with `JSON_UNESCAPED_UNICODE | JSON_UNESCAPED_SLASHES` flags.

- Parameters
  - $value - mixed (array or string)
- Returns `void`

#### Usage [​](https://dev.fluentcart.com/database/models/attribute-group\#usage-2)

php

```
$attributeGroup->settings = ['display_type' => 'dropdown', 'required' => true];
// Automatically JSON encodes arrays
```

### getSettingsAttribute($value) [​](https://dev.fluentcart.com/database/models/attribute-group\#getsettingsattribute-value)

Get settings with automatic JSON decoding (accessor). If the stored value is a string, it attempts to JSON-decode it. Returns the original string if decoding fails.

- Parameters
  - $value - mixed
- Returns `mixed`

#### Usage [​](https://dev.fluentcart.com/database/models/attribute-group\#usage-3)

php

```
$settings = $attributeGroup->settings; // Returns decoded value (array or string)
```

## Usage Examples [​](https://dev.fluentcart.com/database/models/attribute-group\#usage-examples)

### Get Attribute Groups [​](https://dev.fluentcart.com/database/models/attribute-group\#get-attribute-groups)

php

```
$attributeGroup = FluentCart\App\Models\AttributeGroup::find(1);
echo "Title: " . $attributeGroup->title;
echo "Slug: " . $attributeGroup->slug;
echo "Description: " . $attributeGroup->description;
```

### Create Attribute Group [​](https://dev.fluentcart.com/database/models/attribute-group\#create-attribute-group)

php

```
$attributeGroup = FluentCart\App\Models\AttributeGroup::create([\
    'title' => 'Color',\
    'slug' => 'color',\
    'description' => 'Product color variations',\
    'settings' => [\
        'display_type' => 'dropdown',\
        'required' => true,\
        'multiple' => false\
    ]\
]);
```

### Get Attribute Groups with Terms [​](https://dev.fluentcart.com/database/models/attribute-group\#get-attribute-groups-with-terms)

php

```
$attributeGroups = FluentCart\App\Models\AttributeGroup::with('terms')->get();

foreach ($attributeGroups as $group) {
    echo "Group: " . $group->title;
    foreach ($group->terms as $term) {
        echo "  - Term: " . $term->title;
    }
}
```

### Apply Custom Filters [​](https://dev.fluentcart.com/database/models/attribute-group\#apply-custom-filters)

php

```
$filters = [\
    'title' => ['value' => 'Color', 'operator' => 'includes'],\
    'terms_count' => ['value' => 3, 'operator' => 'gt']\
];

$filteredGroups = FluentCart\App\Models\AttributeGroup::applyCustomFilters($filters)->get();
```

### Get Groups by Title [​](https://dev.fluentcart.com/database/models/attribute-group\#get-groups-by-title)

php

```
$colorGroups = FluentCart\App\Models\AttributeGroup::where('title', 'Color')->get();
$sizeGroups = FluentCart\App\Models\AttributeGroup::where('title', 'Size')->get();
```

### Get Groups with Term Count [​](https://dev.fluentcart.com/database/models/attribute-group\#get-groups-with-term-count)

php

```
$groupsWithCounts = FluentCart\App\Models\AttributeGroup::withCount('terms')->get();

foreach ($groupsWithCounts as $group) {
    echo "Group: " . $group->title . " (" . $group->terms_count . " terms)";
}
```

### Update Attribute Group [​](https://dev.fluentcart.com/database/models/attribute-group\#update-attribute-group)

php

```
$attributeGroup = FluentCart\App\Models\AttributeGroup::find(1);
$attributeGroup->update([\
    'description' => 'Updated description',\
    'settings' => ['display_type' => 'radio', 'required' => false]\
]);
```

### Delete Attribute Group (with Terms) [​](https://dev.fluentcart.com/database/models/attribute-group\#delete-attribute-group-with-terms)

php

```
$attributeGroup = FluentCart\App\Models\AttributeGroup::find(1);
$attributeGroup->delete(); // Automatically deletes associated terms via boot() deleting event
```

### Use CanSearch Trait Scopes [​](https://dev.fluentcart.com/database/models/attribute-group\#use-cansearch-trait-scopes)

php

```
// Search with the search scope (from CanSearch trait)
$groups = FluentCart\App\Models\AttributeGroup::search([\
    'title' => ['column' => 'title', 'operator' => 'like_all', 'value' => 'Color']\
])->get();

// Use whereLike scope
$groups = FluentCart\App\Models\AttributeGroup::whereLike('title', 'Col')->get();
```

* * *

Today

Hi! I’m your AI assistant. How can I assist you today?

Just now

Powered by **FluentBot**


---

---

## Attribute Relation Model | FluentCart Developer Docs

**URL** : https://dev.fluentcart.com/database/models/attribute-relation

[Skip to content](https://dev.fluentcart.com/database/models/attribute-relation#VPContent)

# Attribute Relation Model [​](https://dev.fluentcart.com/database/models/attribute-relation\#attribute-relation-model)

| DB Table Name | {wp\_db\_prefix}\_fct\_atts\_relations |
| --- | --- |
| Schema | [Check Schema](https://dev.fluentcart.com/database/schema.html#fct-atts-relations-table) |
| Source File | fluent-cart/app/Models/AttributeRelation.php |
| Name Space | FluentCart\\App\\Models |
| Class | FluentCart\\App\\Models\\AttributeRelation |

## Attributes [​](https://dev.fluentcart.com/database/models/attribute-relation\#attributes)

| Attribute | Data Type | Comment |
| --- | --- | --- |
| id | Integer | Primary Key |
| group\_id | Integer | Reference to attribute group |
| term\_id | Integer | Reference to attribute term |
| object\_id | Integer | Reference to product detail (variation) |
| created\_at | Date Time | Creation timestamp |
| updated\_at | Date Time | Last update timestamp |

## Usage [​](https://dev.fluentcart.com/database/models/attribute-relation\#usage)

Please check [Model Basic](https://dev.fluentcart.com/database/models.html) for Common methods.

### Accessing Attributes [​](https://dev.fluentcart.com/database/models/attribute-relation\#accessing-attributes)

php

```
$attributeRelation = FluentCart\App\Models\AttributeRelation::find(1);

$attributeRelation->id; // returns id
$attributeRelation->group_id; // returns group ID
$attributeRelation->term_id; // returns term ID
$attributeRelation->object_id; // returns object ID (product detail ID)
```

## Relations [​](https://dev.fluentcart.com/database/models/attribute-relation\#relations)

This model has the following relationships that you can use

### group [​](https://dev.fluentcart.com/database/models/attribute-relation\#group)

Access the associated attribute group (`belongsTo`)

- return `FluentCart\App\Models\AttributeGroup` Model

#### Example: [​](https://dev.fluentcart.com/database/models/attribute-relation\#example)

php

```
// Accessing Group
$group = $attributeRelation->group;

// For Filtering by group relationship
$attributeRelations = FluentCart\App\Models\AttributeRelation::whereHas('group', function($query) {
    $query->where('title', 'Color');
})->get();
```

### term [​](https://dev.fluentcart.com/database/models/attribute-relation\#term)

Access the associated attribute term (`belongsTo`)

- return `FluentCart\App\Models\AttributeTerm` Model

#### Example: [​](https://dev.fluentcart.com/database/models/attribute-relation\#example-1)

php

```
// Accessing Term
$term = $attributeRelation->term;

// For Filtering by term relationship
$attributeRelations = FluentCart\App\Models\AttributeRelation::whereHas('term', function($query) {
    $query->where('title', 'Red');
})->get();
```

### productDetails [​](https://dev.fluentcart.com/database/models/attribute-relation\#productdetails)

Access the associated product detail (`belongsTo`). Links via `object_id` to `ProductDetail.id`.

- return `FluentCart\App\Models\ProductDetail` Model

#### Example: [​](https://dev.fluentcart.com/database/models/attribute-relation\#example-2)

php

```
// Accessing Product Detail
$productDetail = $attributeRelation->productDetails;

// For Filtering by product detail relationship
$attributeRelations = FluentCart\App\Models\AttributeRelation::whereHas('productDetails', function($query) {
    $query->where('fulfillment_type', 'physical');
})->get();
```

## Usage Examples [​](https://dev.fluentcart.com/database/models/attribute-relation\#usage-examples)

### Get Attribute Relations [​](https://dev.fluentcart.com/database/models/attribute-relation\#get-attribute-relations)

php

```
$attributeRelation = FluentCart\App\Models\AttributeRelation::find(1);
echo "Group ID: " . $attributeRelation->group_id;
echo "Term ID: " . $attributeRelation->term_id;
echo "Object ID: " . $attributeRelation->object_id;
```

### Create Attribute Relation [​](https://dev.fluentcart.com/database/models/attribute-relation\#create-attribute-relation)

php

```
$attributeRelation = FluentCart\App\Models\AttributeRelation::create([\
    'group_id' => 1,  // Color group\
    'term_id' => 5,   // Red term\
    'object_id' => 123 // Product detail ID\
]);
```

### Get Relations with Group and Term Information [​](https://dev.fluentcart.com/database/models/attribute-relation\#get-relations-with-group-and-term-information)

php

```
$attributeRelations = FluentCart\App\Models\AttributeRelation::with(['group', 'term'])->get();

foreach ($attributeRelations as $relation) {
    echo "Group: " . $relation->group->title;
    echo "Term: " . $relation->term->title;
    echo "Object ID: " . $relation->object_id;
}
```

### Get Relations by Group [​](https://dev.fluentcart.com/database/models/attribute-relation\#get-relations-by-group)

php

```
$colorRelations = FluentCart\App\Models\AttributeRelation::where('group_id', 1)->get();
$sizeRelations = FluentCart\App\Models\AttributeRelation::where('group_id', 2)->get();
```

### Get Relations by Term [​](https://dev.fluentcart.com/database/models/attribute-relation\#get-relations-by-term)

php

```
$redRelations = FluentCart\App\Models\AttributeRelation::where('term_id', 5)->get();
$smallRelations = FluentCart\App\Models\AttributeRelation::where('term_id', 10)->get();
```

### Get Relations for Product [​](https://dev.fluentcart.com/database/models/attribute-relation\#get-relations-for-product)

php

```
$productRelations = FluentCart\App\Models\AttributeRelation::where('object_id', 123)->get();

foreach ($productRelations as $relation) {
    echo "Attribute: " . $relation->group->title . " - " . $relation->term->title;
}
```

### Get Relations with Product Details [​](https://dev.fluentcart.com/database/models/attribute-relation\#get-relations-with-product-details)

php

```
$relationsWithProducts = FluentCart\App\Models\AttributeRelation::with(['group', 'term', 'productDetails'])->get();

foreach ($relationsWithProducts as $relation) {
    echo "Product: " . $relation->productDetails->id;
    echo "Attribute: " . $relation->group->title . " - " . $relation->term->title;
}
```

### Delete Attribute Relation [​](https://dev.fluentcart.com/database/models/attribute-relation\#delete-attribute-relation)

php

```
$attributeRelation = FluentCart\App\Models\AttributeRelation::find(1);
$attributeRelation->delete();
```

### Get Relations by Multiple Terms [​](https://dev.fluentcart.com/database/models/attribute-relation\#get-relations-by-multiple-terms)

php

```
$redOrBlueRelations = FluentCart\App\Models\AttributeRelation::whereIn('term_id', [5, 6])->get();
```

### Get Relations for Multiple Products [​](https://dev.fluentcart.com/database/models/attribute-relation\#get-relations-for-multiple-products)

php

```
$multiProductRelations = FluentCart\App\Models\AttributeRelation::whereIn('object_id', [123, 124, 125])->get();
```

* * *

Today

Hi! I’m your AI assistant. How can I assist you today?

Just now

Powered by **FluentBot**


---

---

## Attribute Term Model | FluentCart Developer Docs

**URL** : https://dev.fluentcart.com/database/models/attribute-term

[Skip to content](https://dev.fluentcart.com/database/models/attribute-term#VPContent)

# Attribute Term Model [​](https://dev.fluentcart.com/database/models/attribute-term\#attribute-term-model)

| DB Table Name | {wp\_db\_prefix}\_fct\_atts\_terms |
| --- | --- |
| Schema | [Check Schema](https://dev.fluentcart.com/database/schema.html#fct-atts-terms-table) |
| Source File | fluent-cart/app/Models/AttributeTerm.php |
| Name Space | FluentCart\\App\\Models |
| Class | FluentCart\\App\\Models\\AttributeTerm |

## Traits [​](https://dev.fluentcart.com/database/models/attribute-term\#traits)

- **CanSearch** (`FluentCart\App\Models\Concerns\CanSearch`) \- Provides `search()`, `groupSearch()`, `whereLike()`, `whereBeginsWith()`, and `whereEndsWith()` query scopes.

## Attributes [​](https://dev.fluentcart.com/database/models/attribute-term\#attributes)

| Attribute | Data Type | Comment |
| --- | --- | --- |
| id | Integer | Primary Key |
| group\_id | Integer | Reference to attribute group |
| serial | Integer | Serial number for ordering |
| title | String | Attribute term title (e.g., Red, Small, Large) |
| slug | String | Attribute term slug |
| description | Text | Attribute term description |
| settings | JSON | Attribute term settings |
| created\_at | Date Time | Creation timestamp |
| updated\_at | Date Time | Last update timestamp |

## Usage [​](https://dev.fluentcart.com/database/models/attribute-term\#usage)

Please check [Model Basic](https://dev.fluentcart.com/database/models.html) for Common methods.

### Accessing Attributes [​](https://dev.fluentcart.com/database/models/attribute-term\#accessing-attributes)

php

```
$attributeTerm = FluentCart\App\Models\AttributeTerm::find(1);

$attributeTerm->id; // returns id
$attributeTerm->group_id; // returns group ID
$attributeTerm->serial; // returns serial number
$attributeTerm->title; // returns title
$attributeTerm->slug; // returns slug
$attributeTerm->description; // returns description
$attributeTerm->settings; // returns settings (auto-decoded from JSON)
```

## Scopes [​](https://dev.fluentcart.com/database/models/attribute-term\#scopes)

This model has the following scopes that you can use

### applyCustomFilters($filters) [​](https://dev.fluentcart.com/database/models/attribute-term\#applycustomfilters-filters)

Apply custom filters to the query. Accepts filters for any fillable attribute (`group_id`, `serial`, `title`, `slug`, `description`, `settings`). Supported operators: `includes` (LIKE), `not_includes` (NOT LIKE), `gt` (>), `lt` (<), and standard SQL comparison operators.

- Parameters
  - $filters - array of filter arrays, each with `value` and `operator` keys

#### Usage: [​](https://dev.fluentcart.com/database/models/attribute-term\#usage-1)

php

```
// Apply custom filters
$filteredTerms = FluentCart\App\Models\AttributeTerm::applyCustomFilters([\
    'title' => ['value' => 'Red', 'operator' => 'includes'],\
    'group_id' => ['value' => 1, 'operator' => '=']\
])->get();
```

## Relations [​](https://dev.fluentcart.com/database/models/attribute-term\#relations)

This model has the following relationships that you can use

### group [​](https://dev.fluentcart.com/database/models/attribute-term\#group)

Access the associated attribute group (`belongsTo`)

- return `FluentCart\App\Models\AttributeGroup` Model

#### Example: [​](https://dev.fluentcart.com/database/models/attribute-term\#example)

php

```
// Accessing Group
$group = $attributeTerm->group;

// For Filtering by group relationship
$attributeTerms = FluentCart\App\Models\AttributeTerm::whereHas('group', function($query) {
    $query->where('title', 'Color');
})->get();
```

## Methods [​](https://dev.fluentcart.com/database/models/attribute-term\#methods)

Along with Global Model methods, this model has few helper methods.

### setSettingsAttribute($value) [​](https://dev.fluentcart.com/database/models/attribute-term\#setsettingsattribute-value)

Set settings with automatic JSON encoding (mutator). If the value is an array or object, it is JSON-encoded with `JSON_UNESCAPED_UNICODE | JSON_UNESCAPED_SLASHES` flags.

- Parameters
  - $value - mixed (array, object, or string)
- Returns `void`

#### Usage [​](https://dev.fluentcart.com/database/models/attribute-term\#usage-2)

php

```
$attributeTerm->settings = ['color_code' => '#FF0000', 'display_order' => 1];
// Automatically JSON encodes arrays and objects
```

### getSettingsAttribute($value) [​](https://dev.fluentcart.com/database/models/attribute-term\#getsettingsattribute-value)

Get settings with automatic JSON decoding (accessor). If the stored value is a string, it attempts to JSON-decode it. Returns the original string if decoding fails.

- Parameters
  - $value - mixed
- Returns `mixed`

#### Usage [​](https://dev.fluentcart.com/database/models/attribute-term\#usage-3)

php

```
$settings = $attributeTerm->settings; // Returns decoded value (array, object, or string)
```

## Usage Examples [​](https://dev.fluentcart.com/database/models/attribute-term\#usage-examples)

### Get Attribute Terms [​](https://dev.fluentcart.com/database/models/attribute-term\#get-attribute-terms)

php

```
$attributeTerm = FluentCart\App\Models\AttributeTerm::find(1);
echo "Title: " . $attributeTerm->title;
echo "Slug: " . $attributeTerm->slug;
echo "Group ID: " . $attributeTerm->group_id;
```

### Create Attribute Term [​](https://dev.fluentcart.com/database/models/attribute-term\#create-attribute-term)

php

```
$attributeTerm = FluentCart\App\Models\AttributeTerm::create([\
    'group_id' => 1,\
    'serial' => 1,\
    'title' => 'Red',\
    'slug' => 'red',\
    'description' => 'Red color variant',\
    'settings' => [\
        'color_code' => '#FF0000',\
        'display_order' => 1,\
        'is_default' => false\
    ]\
]);
```

### Get Terms by Group [​](https://dev.fluentcart.com/database/models/attribute-term\#get-terms-by-group)

php

```
$colorTerms = FluentCart\App\Models\AttributeTerm::where('group_id', 1)->get();
$sizeTerms = FluentCart\App\Models\AttributeTerm::where('group_id', 2)->get();
```

### Get Terms with Group Information [​](https://dev.fluentcart.com/database/models/attribute-term\#get-terms-with-group-information)

php

```
$attributeTerms = FluentCart\App\Models\AttributeTerm::with('group')->get();

foreach ($attributeTerms as $term) {
    echo "Term: " . $term->title;
    echo "Group: " . $term->group->title;
}
```

### Apply Custom Filters [​](https://dev.fluentcart.com/database/models/attribute-term\#apply-custom-filters)

php

```
$filters = [\
    'title' => ['value' => 'Red', 'operator' => 'includes'],\
    'group_id' => ['value' => 1, 'operator' => '=']\
];

$filteredTerms = FluentCart\App\Models\AttributeTerm::applyCustomFilters($filters)->get();
```

### Get Terms Ordered by Serial [​](https://dev.fluentcart.com/database/models/attribute-term\#get-terms-ordered-by-serial)

php

```
$orderedTerms = FluentCart\App\Models\AttributeTerm::where('group_id', 1)
    ->orderBy('serial', 'asc')
    ->get();
```

### Update Attribute Term [​](https://dev.fluentcart.com/database/models/attribute-term\#update-attribute-term)

php

```
$attributeTerm = FluentCart\App\Models\AttributeTerm::find(1);
$attributeTerm->update([\
    'title' => 'Bright Red',\
    'settings' => ['color_code' => '#CC0000', 'display_order' => 2]\
]);
```

### Get Terms with Settings [​](https://dev.fluentcart.com/database/models/attribute-term\#get-terms-with-settings)

php

```
$termsWithSettings = FluentCart\App\Models\AttributeTerm::where('group_id', 1)->get();

foreach ($termsWithSettings as $term) {
    $settings = $term->settings;
    if (isset($settings['color_code'])) {
        echo "Term: " . $term->title . " - Color: " . $settings['color_code'];
    }
}
```

### Use CanSearch Trait Scopes [​](https://dev.fluentcart.com/database/models/attribute-term\#use-cansearch-trait-scopes)

php

```
// Search with the search scope (from CanSearch trait)
$terms = FluentCart\App\Models\AttributeTerm::search([\
    'title' => ['column' => 'title', 'operator' => 'like_all', 'value' => 'Red']\
])->get();

// Use whereLike scope
$terms = FluentCart\App\Models\AttributeTerm::whereLike('title', 'Re')->get();
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

