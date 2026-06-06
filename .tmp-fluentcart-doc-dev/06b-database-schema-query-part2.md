# FluentCart Developer Docs - Database Schema & Query Builder (Part 2/2)

Schéma de la base de données et patterns du query builder utilisé par FluentCart.

---

## Query Builder | FluentCart Developer Docs

**URL** : https://dev.fluentcart.com/database/query-builder

[Skip to content](https://dev.fluentcart.com/database/query-builder#VPContent)

# FluentCart Query Builder [​](https://dev.fluentcart.com/database/query-builder\#fluentcart-query-builder)

## Introduction [​](https://dev.fluentcart.com/database/query-builder\#introduction)

FluentCart uses an Eloquent-based ORM system compatible with Laravel's Eloquent ORM. You can interact with database tables through Model classes or using direct query builder methods.

TIP

FluentCart's ORM is compatible with Laravel Framework's Eloquent ORM. If you are familiar with Laravel's Eloquent, you will feel right at home using FluentCart's database system.

### Example Using Models [​](https://dev.fluentcart.com/database/query-builder\#example-using-models)

Here is an example using FluentCart models:

php

```
use FluentCart\App\Models\Order;

// Using the Order model
$orders = Order::where('payment_status', 'paid')
            ->whereBetween('created_at', ['2024-01-01 00:00:00', '2024-12-30 23:59:59'])
            ->when($customerId, function ($query) use ($customerId) {
                return $query->where('customer_id', $customerId);
            })
            ->orderBy('created_at', 'ASC')
            ->get();
```

### Example Using Query Builder [​](https://dev.fluentcart.com/database/query-builder\#example-using-query-builder)

You can also use the query builder directly:

php

```
use FluentCart\App\Models\Order;

$query = Order::query()
            ->select(['total_amount', 'status', 'payment_method'])
            ->where('payment_status', 'paid')
            ->whereBetween('created_at', ['2024-01-01 00:00:00', '2024-12-30 23:59:59'])
            ->when($customerId, function ($query) use ($customerId) {
                return $query->where('customer_id', $customerId);
            })
            ->orderBy('created_at', 'ASC');
```

## Retrieving Results [​](https://dev.fluentcart.com/database/query-builder\#retrieving-results)

### Retrieving All Rows From A Table [​](https://dev.fluentcart.com/database/query-builder\#retrieving-all-rows-from-a-table)

You can use the model's query builder to retrieve all rows from a table. The query builder provides a fluent interface for building database queries:

php

```
<?php

use FluentCart\App\Models\Order;

class OrderController extends Controller
{
    /**
     * Show a list of all the application's orders.
     *
     * @return Response
     */
    public function index()
    {
        $orders = Order::all();
        // or using query builder
        $orders = Order::query()->get();

        return [\
            'orders' => $orders\
        ];
    }
}
```

The `get` method returns a collection containing the results where each result is an instance of the Model object. You may access each column's value by accessing the column as a property of the object:

php

```
foreach ($orders as $order) {
    echo $order->total_amount;
}
```

### Retrieving A Single Row / Column From A Table [​](https://dev.fluentcart.com/database/query-builder\#retrieving-a-single-row-column-from-a-table)

If you just need to retrieve a single row from the database table, you may use the `first` method. This method will return a single Model object:

php

```
use FluentCart\App\Models\Order;

$order = Order::where('status', 'completed')->first();

echo $order->total_amount;
```

If you don't even need an entire row, you may extract a single value from a record using the `value` method. This method will return the value of the column directly:

php

```
use FluentCart\App\Models\Order;

$totalAmount = Order::where('status', 'completed')->value('total_amount');
```

### Retrieving A List Of Column Values [​](https://dev.fluentcart.com/database/query-builder\#retrieving-a-list-of-column-values)

If you would like to retrieve an array containing the values of a single column, you may use the `pluck` method. In this example, we'll retrieve an array of order IDs:

php

```
$orderIds = fluentCartDb()->table('fct_orders')->pluck('id');

foreach ($orderIds as $orderId) {
    echo $orderId;
}
```

You may also specify a custom key column for the returned Collection:

php

```
$orderIds = fluentCartDb()->table('fct_orders')->pluck('id', 'customer_id');

foreach ($orderIds as $customerId => $orderId) {
    echo $orderId;
}
```

### Chunking Results [​](https://dev.fluentcart.com/database/query-builder\#chunking-results)

If you need to work with thousands of database records, consider using the `chunk` method. This method retrieves a small chunk of the results at a time and feeds each chunk into a Closure for processing. This method is very useful for process thousands of records. For example, let's work with the entire `fct_orders` table in chunks of 100 records at a time:

php

```
fluentCartDb()->table('fct_orders')->orderBy('id')->chunk(100, function ($orders) {
    foreach ($orders as $order) {
        //
    }
});
```

You may stop further chunks from being processed by returning false from the Closure:

php

```
fluentCartDb()->table('fct_orders')->orderBy('id')->chunk(100, function ($orders) {
    // Process the records...

    return false;
});
```

### Aggregates [​](https://dev.fluentcart.com/database/query-builder\#aggregates)

The query builder also provides a variety of aggregate methods such as `count`, `max`, `min`, `avg`, and `sum`. You may call any of these methods after constructing your query:

php

```
$orders = fluentCartDb()->table('fct_orders')->count();

$maxAmount = fluentCartDb()->table('fct_orders')->max('total_amount');
```

Of course, you may combine these methods with other clauses:

php

```
$avgAmount = fluentCartDb()->table('fct_orders')
                ->where('payment_status', 'paid')
                ->avg('total_amount');
```

### Determining If Records Exist [​](https://dev.fluentcart.com/database/query-builder\#determining-if-records-exist)

Instead of using the `count` method to determine if any records exist that match your query's constraints, you may use the `exists`:

php

```
return fluentCartDb()->table('fct_orders')->where('payment_status', 'paid')->exists();
```

## Selects [​](https://dev.fluentcart.com/database/query-builder\#selects)

### Specifying A Select Clause [​](https://dev.fluentcart.com/database/query-builder\#specifying-a-select-clause)

Of course, you may not always want to select all columns from a database table. Using the `select` method, you can specify a custom `select` clause for the query:

php

```
$orders = fluentCartDb()->table('fct_orders')->select('status', 'total_amount as order_total')->get();
```

The `distinct` method allows you to force the query to return distinct results:

php

```
$orders = fluentCartDb()->table('fct_orders')->distinct()->get();
```

If you already have a query builder instance and wish to add a column to its existing select clause, you may use the `addSelect` method:

php

```
$query = fluentCartDb()->table('fct_orders')->select('status');

$orders = $query->addSelect('total_amount')->get();
```

## Raw Expressions [​](https://dev.fluentcart.com/database/query-builder\#raw-expressions)

Sometimes you may need to use a raw expression in a query. To create a raw expression, you may use the `raw` method:

php

```
$orders = fluentCartDb()->table('fct_orders')
                     ->select(fluentCartDb()->raw('count(*) as order_count, status'))
                     ->where('status', '<>', 'draft')
                     ->groupBy('status')
                     ->get();
```

### Raw Methods [​](https://dev.fluentcart.com/database/query-builder\#raw-methods)

Instead of using `fluentCartDb()->raw`, you may also use the following methods to insert a raw expression into various parts of your query.

#### `selectRaw` [​](https://dev.fluentcart.com/database/query-builder\#selectraw)

The `selectRaw` method can be used in place of `select(fluentCartDb()->raw(...))`. This method accepts an optional array of bindings as its second argument:

php

```
$orders = fluentCartDb()->table('fct_orders')
                ->selectRaw('total_amount * ? as price_with_tax', [1.0825])
                ->get();
```

#### `whereRaw / orWhereRaw` [​](https://dev.fluentcart.com/database/query-builder\#whereraw-orwhereraw)

The `whereRaw` and `orWhereRaw` methods can be used to inject a raw `where` clause into your query. These methods accept an optional array of bindings as their second argument:

php

```
$orders = fluentCartDb()->table('fct_orders')
                ->whereRaw('total_amount > (subtotal * 1.1)')
                ->get();
```

#### `havingRaw / orHavingRaw` [​](https://dev.fluentcart.com/database/query-builder\#havingraw-orhavingraw)

The `havingRaw` and `orHavingRaw` methods may be used to set a raw string as the value of the `having` clause. These methods accept an optional array of bindings as their second argument:

php

```
$orders = fluentCartDb()->table('fct_orders')
                ->select('customer_id', fluentCartDb()->raw('SUM(total_amount) as total'))
                ->groupBy('customer_id')
                ->havingRaw('SUM(total_amount) > ?', [1000])
                ->get();
```

#### `orderByRaw` [​](https://dev.fluentcart.com/database/query-builder\#orderbyraw)

The `orderByRaw` method may be used to set a raw string as the value of the `order by` clause:

php

```
$orders = fluentCartDb()->table('fct_orders')
                ->orderByRaw('FIELD(status, "pending", "processing", "completed")')
                ->get();
```

## Joins [​](https://dev.fluentcart.com/database/query-builder\#joins)

### Inner Join Statement [​](https://dev.fluentcart.com/database/query-builder\#inner-join-statement)

The query builder may also be used to write join statements. To perform a basic "inner join", you may use the `join` method on a query builder instance. The first argument passed to the `join` method is the name of the table you need to join to, while the remaining arguments specify the column constraints for the join. Of course, as you can see, you can join to multiple tables in a single query:

php

```
$orders = fluentCartDb()->table('fct_orders')
            ->join('fct_customers', 'fct_orders.customer_id', '=', 'fct_customers.id')
            ->join('fct_order_items', 'fct_orders.id', '=', 'fct_order_items.order_id')
            ->select('fct_orders.*', 'fct_customers.email', 'fct_customers.first_name')
            ->get();
```

### Left Join / Right Join Statement [​](https://dev.fluentcart.com/database/query-builder\#left-join-right-join-statement)

If you would like to perform a "left join" instead of an "inner join", use the `leftJoin` method. The `leftJoin` method has the same signature as the `join` method:

php

```
$orders = fluentCartDb()->table('fct_orders')
            ->leftJoin('fct_customers', 'fct_orders.customer_id', '=', 'fct_customers.id')
            ->get();
```

Similarly, you may use the `rightJoin` method to perform a "right join":

php

```
$orders = fluentCartDb()->table('fct_orders')
            ->rightJoin('fct_customers', 'fct_orders.customer_id', '=', 'fct_customers.id')
            ->get();
```

### Cross Join Statement [​](https://dev.fluentcart.com/database/query-builder\#cross-join-statement)

To perform a "cross join" use the `crossJoin` method with the name of the table you wish to cross join to. Cross joins generate a cartesian product between the first table and the joined table:

php

```
$products = fluentCartDb()->table('fct_product_details')
            ->crossJoin('fct_product_variations')
            ->get();
```

### Advanced Join Clauses [​](https://dev.fluentcart.com/database/query-builder\#advanced-join-clauses)

You may also specify more advanced join clauses. To get started, pass a `Closure` as the second argument into the `join` method. The `Closure` will receive a `JoinClause` object which allows you to specify constraints on the `join` clause:

php

```
fluentCartDb()->table('fct_orders')
        ->join('fct_customers', function ($join) {
            $join->on('fct_orders.customer_id', '=', 'fct_customers.id')
                 ->where('fct_customers.status', '=', 'active');
        })
        ->get();
```

### Subquery Joins [​](https://dev.fluentcart.com/database/query-builder\#subquery-joins)

You may use the `joinSub`, `leftJoinSub`, and `rightJoinSub` methods to join a query to a subquery. Each of these methods receive three arguments: the subquery, its table alias, and a Closure that defines the related columns:

php

```
$latestOrders = fluentCartDb()->table('fct_orders')
        ->select('customer_id', fluentCartDb()->raw('MAX(created_at) as last_order_date'))
        ->groupBy('customer_id');

$customers = fluentCartDb()->table('fct_customers')
        ->joinSub($latestOrders, 'latest_orders', function ($join) {
            $join->on('fct_customers.id', '=', 'latest_orders.customer_id');
        })->get();
```

## Unions [​](https://dev.fluentcart.com/database/query-builder\#unions)

The query builder also provides a quick way to "union" two or more queries together. For example, you may create an initial query and use the `union` method to union it with a second query:

php

```
$first = fluentCartDb()->table('fct_orders')
            ->whereNull('completed_at');

$orders = fluentCartDb()->table('fct_orders')
            ->whereNull('cancelled_at')
            ->union($first)
            ->get();
```

The `unionAll` method may also be used and has the same method signature as `union`. The difference between `union` and `unionAll` is that `unionAll` will not remove duplicate entries from your resultset.

## Where Clauses [​](https://dev.fluentcart.com/database/query-builder\#where-clauses)

### Simple Where Clauses [​](https://dev.fluentcart.com/database/query-builder\#simple-where-clauses)

You may use the `where` method on a query builder instance to add `where` clauses to the query. The most basic call to `where` requires three arguments. The first argument is the name of the column. The second argument is an operator, which can be any of the database's supported operators. Finally, the third argument is the value to evaluate against the column.

For example, here is a query that verifies the value of a "status" column equals "completed":

php

```
$orders = fluentCartDb()->table('fct_orders')->where('status', '=', 'completed')->get();
```

For convenience, if you want to verify that a column is equal to a given value, you may pass the value directly as the second argument to the `where` method:

php

```
$orders = fluentCartDb()->table('fct_orders')->where('status', 'completed')->get();
```

Of course, you may use a variety of other operators when writing a `where` clause:

php

```
$orders = fluentCartDb()->table('fct_orders')->where('total_amount', '>', 1000)->get();

$orders = fluentCartDb()->table('fct_orders')->where('total_amount', '>=', 1000)->get();

$orders = fluentCartDb()->table('fct_orders')->where('total_amount', '<', 1000)->get();

$orders = fluentCartDb()->table('fct_orders')->where('total_amount', '<=', 1000)->get();

$orders = fluentCartDb()->table('fct_orders')->where('status', '!=', 'draft')->get();

$orders = fluentCartDb()->table('fct_orders')->where('status', '<>', 'draft')->get();
```

### Or Statements [​](https://dev.fluentcart.com/database/query-builder\#or-statements)

You may chain where constraints together as well as add `or` clauses to the query. The `orWhere` method accepts the same arguments as the `where` method:

php

```
$orders = fluentCartDb()->table('fct_orders')
                    ->where('status', 'completed')
                    ->orWhere('payment_status', 'paid')
                    ->get();
```

### Additional Where Clauses [​](https://dev.fluentcart.com/database/query-builder\#additional-where-clauses)

#### whereBetween / orWhereBetween [​](https://dev.fluentcart.com/database/query-builder\#wherebetween-orwherebetween)

The `whereBetween` method verifies that a column's value is between two values:

php

```
$orders = fluentCartDb()->table('fct_orders')
                    ->whereBetween('total_amount', [100, 500])
                    ->get();
```

The `orWhereBetween` method verifies that a column's value is outside of two values:

php

```
$orders = fluentCartDb()->table('fct_orders')
                    ->whereNotBetween('total_amount', [100, 500])
                    ->get();
```

#### whereIn / whereNotIn / orWhereIn / orWhereNotIn [​](https://dev.fluentcart.com/database/query-builder\#wherein-wherenotin-orwherein-orwherenotin)

The `whereIn` method verifies that a given column's value is contained within the given array:

php

```
$orders = fluentCartDb()->table('fct_orders')
                    ->whereIn('status', ['pending', 'processing', 'completed'])
                    ->get();
```

The `whereNotIn` method verifies that the given column's value is not contained in the given array:

php

```
$orders = fluentCartDb()->table('fct_orders')
                    ->whereNotIn('status', ['cancelled', 'failed'])
                    ->get();
```

#### whereNull / whereNotNull / orWhereNull / orWhereNotNull [​](https://dev.fluentcart.com/database/query-builder\#wherenull-wherenotnull-orwherenull-orwherenotnull)

The `whereNull` method verifies that the value of the given column is `NULL`:

php

```
$orders = fluentCartDb()->table('fct_orders')
                    ->whereNull('completed_at')
                    ->get();
```

The `whereNotNull` method verifies that the column's value is not `NULL`:

php

```
$orders = fluentCartDb()->table('fct_orders')
                    ->whereNotNull('completed_at')
                    ->get();
```

#### whereDate / whereYear [​](https://dev.fluentcart.com/database/query-builder\#wheredate-whereyear)

The `whereDate` method may be used to compare a column's value against a date:

php

```
$orders = fluentCartDb()->table('fct_orders')
                ->whereDate('created_at', '2024-12-31')
                ->get();
```

The `whereYear` method may be used to compare a column's value against a specific year:

php

```
$orders = fluentCartDb()->table('fct_orders')
                ->whereYear('created_at', '2024')
                ->get();
```

### Parameter Grouping [​](https://dev.fluentcart.com/database/query-builder\#parameter-grouping)

Sometimes you may need to create more advanced where clauses such as "where exists" or nested parameter groupings. The FluentCart query builder can handle these as well. To get started, let's look at an example of grouping constraints within parenthesis:

php

```
fluentCartDb()->table('fct_orders')
            ->where('status', '=', 'completed')
            ->where(function ($query) {
                $query->where('total_amount', '>', 1000)
                      ->orWhere('payment_method', '=', 'stripe');
            })
            ->get();
```

As you can see, passing a `Closure` into the `where` method instructs the query builder to begin a constraint group. The `Closure` will receive a query builder instance which you can use to set the constraints that should be contained within the parenthesis group. The example above will produce the following SQL:

sql

```
select * from fct_orders where status = 'completed' and (total_amount > 1000 or payment_method = 'stripe')
```

### Where Exists Clauses [​](https://dev.fluentcart.com/database/query-builder\#where-exists-clauses)

The `whereExists` method allows you to write `where exists` SQL clauses. The `whereExists` method accepts a `Closure` argument, which will receive a query builder instance allowing you to define the query that should be placed inside the "exists" clause:

php

```
fluentCartDb()->table('fct_orders')
            ->whereExists(function ($query) {
                $query->select(fluentCartDb()->raw(1))
                      ->from('fct_order_items')
                      ->whereRaw('fct_order_items.order_id = fct_orders.id');
            })
            ->get();
```

The query above will produce the following SQL:

sql

```
select * from fct_orders
where exists (
    select 1 from fct_order_items where fct_order_items.order_id = fct_orders.id
)
```

### Ordering, Grouping, Limit, & Offset [​](https://dev.fluentcart.com/database/query-builder\#ordering-grouping-limit-offset)

#### orderBy [​](https://dev.fluentcart.com/database/query-builder\#orderby)

The `orderBy` method allows you to sort the result of the query by a given column. The first argument to the `orderBy` method should be the column you wish to sort by, while the second argument controls the direction of the sort and may be either `asc` or `desc`:

php

```
$orders = fluentCartDb()->table('fct_orders')
                 ->orderBy('created_at', 'DESC')
                ->get();
```

#### latest / oldest [​](https://dev.fluentcart.com/database/query-builder\#latest-oldest)

The `latest` and `oldest` methods allow you to easily order results by date. By default, result will be ordered by the `created_at` column. Or, you may pass the column name that you wish to sort by:

php

```
$orders = fluentCartDb()->table('fct_orders')
                 ->latest()
                ->get();
```

#### groupBy / having [​](https://dev.fluentcart.com/database/query-builder\#groupby-having)

The `groupBy` and `having` methods may be used to group the query results. The `having` method's signature is similar to that of the `where` method:

php

```
$orders = fluentCartDb()->table('fct_orders')
                ->groupBy('customer_id')
                ->having('customer_id', '>', 100)
                ->get();
```

You may pass multiple arguments to the `groupBy` method to group by multiple columns:

php

```
$orders = fluentCartDb()->table('fct_orders')
                ->groupBy('customer_id', 'status')
                ->having('customer_id', '>', 100)
                ->get();
```

#### skip / take [​](https://dev.fluentcart.com/database/query-builder\#skip-take)

To limit the number of results returned from the query, or to skip a given number of results in the query, you may use the `skip` and `take` methods:

php

```
$orders = fluentCartDb()->table('fct_orders')
                ->skip(10)
                ->take(5)
                ->get();
```

Alternatively, you may use the `limit` and `offset` methods:

php

```
$orders = fluentCartDb()->table('fct_orders')
                ->limit(10)
                ->offset(5)
                ->get();
```

### Conditional Clauses [​](https://dev.fluentcart.com/database/query-builder\#conditional-clauses)

Sometimes you may want clauses to apply to a query only when something else is true. For instance, you may only want to apply a `where` statement if a given input value is present on the incoming request. You may accomplish this using `when` method:

php

```
$customerId = $request->get('customer_id');

$orders = fluentCartDb()->table('fct_orders')
                ->when($customerId, function ($query, $customerId) {
                    return $query->where('customer_id', $customerId);
                })
                ->get();
```

The `when` method only executes the given `Closure` when the first parameter is `true`. If the first parameter is `false`, the Closure will not be executed.

You may pass another Closure as the third parameter to the `when` method. This Closure will execute if the first parameter evaluates as `false`. To illustrate how this feature may be used, we will use it to configure the default sorting of a query:

php

```
$sortBy = null;

$orders = fluentCartDb()->table('fct_orders')
                ->when($sortBy, function ($query, $sortBy) {
                    return $query->orderBy($sortBy);
                }, function ($query) {
                    return $query->orderBy('created_at');
                })
                ->get();
```

## Inserts [​](https://dev.fluentcart.com/database/query-builder\#inserts)

The query builder also provides an `insert` method for inserting records into the database table. The `insert` method accepts an array of column names and values:

php

```
fluentCartDb()->table('fct_orders')->insert(
    ['customer_id' => 1, 'status' => 'pending', 'total_amount' => 1000]
);
```

You may even insert several records into the table with a single call to `insert` by passing an array of arrays. Each array represents a row to be inserted into the table:

php

```
fluentCartDb()->table('fct_orders')->insert([\
    ['customer_id' => 1, 'status' => 'pending', 'total_amount' => 1000],\
    ['customer_id' => 2, 'status' => 'processing', 'total_amount' => 2000]\
]);
```

### Auto-Incrementing IDs [​](https://dev.fluentcart.com/database/query-builder\#auto-incrementing-ids)

If the table has an auto-incrementing id, use the `insertGetId` method to insert a record and then retrieve the ID:

php

```
fluentCartDb()->table('fct_orders')->insertGetId(
    ['customer_id' => 1, 'status' => 'pending', 'total_amount' => 1000]
);
```

## Updates [​](https://dev.fluentcart.com/database/query-builder\#updates)

Of course, in addition to inserting records into the database, the query builder can also update existing records using the `update` method. The `update` method, like the `insert` method, accepts an array of column and value pairs containing the columns to be updated. You may constrain the `update` query using `where` clauses:

php

```
fluentCartDb()->table('fct_orders')
            ->where('id', 1)
            ->update(['status' => 'completed']);
```

## Increment & Decrement [​](https://dev.fluentcart.com/database/query-builder\#increment-decrement)

The query builder also provides convenient methods for incrementing or decrementing the value of a given column. This is useful for updating stock quantities or order counts.

Both of these methods accept at least one argument: the column to modify. A second argument may optionally be passed to control the amount by which the column should be incremented or decremented:

php

```
// Decrement product stock when order is placed
fluentCartDb()->table('fct_product_variations')->decrement('available', 1);

// Increment order count for customer
fluentCartDb()->table('fct_customers')->increment('order_count');
```

You may also specify additional columns to update during the operation:

php

```
fluentCartDb()->table('fct_product_variations')->decrement('available', 1, ['updated_at' => now()]);
```

## Deletes [​](https://dev.fluentcart.com/database/query-builder\#deletes)

The query builder may also be used to delete records from the table via the `delete` method. You may constrain delete statements by adding where clauses before calling the `delete` method:

php

```
fluentCartDb()->table('fct_orders')->delete();

fluentCartDb()->table('fct_orders')->where('status', 'draft')->delete();
```

If you wish to truncate the entire table, which will remove all rows and reset the auto-incrementing ID to zero, you may use the `truncate` method:

php

```
fluentCartDb()->table('fct_orders')->truncate();
```

## FluentCart-Specific Query Examples [​](https://dev.fluentcart.com/database/query-builder\#fluentcart-specific-query-examples)

### Activity Logging Queries [​](https://dev.fluentcart.com/database/query-builder\#activity-logging-queries)

php

```
// Get all activities for a specific order
$orderActivities = fluentCartDb()->table('fct_activity')
    ->where('module_type', 'FluentCart\App\Models\Order')
    ->where('module_id', 123)
    ->orderBy('created_at', 'desc')
    ->get();

// Get failed activities in the last 24 hours
$failedActivities = fluentCartDb()->table('fct_activity')
    ->where('status', 'failed')
    ->where('created_at', '>=', now()->subDay())
    ->get();
```

### Attribute System Queries [​](https://dev.fluentcart.com/database/query-builder\#attribute-system-queries)

php

```
// Get all products with specific color attribute
$redProducts = fluentCartDb()->table('fct_atts_relations')
    ->join('fct_atts_terms', 'fct_atts_relations.term_id', '=', 'fct_atts_terms.id')
    ->join('fct_atts_groups', 'fct_atts_relations.group_id', '=', 'fct_atts_groups.id')
    ->where('fct_atts_groups.slug', 'color')
    ->where('fct_atts_terms.slug', 'red')
    ->pluck('object_id');

// Get all attribute groups with their terms
$attributeGroups = fluentCartDb()->table('fct_atts_groups')
    ->leftJoin('fct_atts_terms', 'fct_atts_groups.id', '=', 'fct_atts_terms.group_id')
    ->select('fct_atts_groups.*', 'fct_atts_terms.title as term_title')
    ->get();
```

### Label System Queries [​](https://dev.fluentcart.com/database/query-builder\#label-system-queries)

php

```
// Get all orders with 'featured' label
$featuredOrders = fluentCartDb()->table('fct_orders')
    ->join('fct_label_relationships', 'fct_orders.id', '=', 'fct_label_relationships.labelable_id')
    ->join('fct_label', 'fct_label_relationships.label_id', '=', 'fct_label.id')
    ->where('fct_label_relationships.labelable_type', 'FluentCart\App\Models\Order')
    ->where('fct_label.value', 'featured')
    ->get();

// Get all labels for a specific order
$orderLabels = fluentCartDb()->table('fct_label_relationships')
    ->join('fct_label', 'fct_label_relationships.label_id', '=', 'fct_label.id')
    ->where('fct_label_relationships.labelable_id', 123)
    ->where('fct_label_relationships.labelable_type', 'FluentCart\App\Models\Order')
    ->pluck('fct_label.value');
```

### Scheduled Actions Queries [​](https://dev.fluentcart.com/database/query-builder\#scheduled-actions-queries)

php

```
// Get all pending scheduled actions that are due
$dueActions = fluentCartDb()->table('fct_scheduled_actions')
    ->where('status', 'pending')
    ->where('scheduled_at', '<=', now())
    ->orderBy('scheduled_at', 'asc')
    ->get();

// Get failed actions that need retry
$failedActions = fluentCartDb()->table('fct_scheduled_actions')
    ->where('status', 'failed')
    ->where('retry_count', '<', 3)
    ->get();
```

### Pro Licensing Queries [​](https://dev.fluentcart.com/database/query-builder\#pro-licensing-queries)

php

```
// Get all active licenses for a customer
$customerLicenses = fluentCartDb()->table('fct_licenses')
    ->where('customer_id', 123)
    ->where('status', 'active')
    ->where('expiration_date', '>', now())
    ->get();

// Get license activation count
$activationCount = fluentCartDb()->table('fct_license_activations')
    ->where('license_id', 456)
    ->where('status', 'active')
    ->count();

// Get all sites for a license
$licenseSites = fluentCartDb()->table('fct_license_sites')
    ->where('license_id', 456)
    ->where('status', 'active')
    ->get();
```

### Webhook Logging Queries [​](https://dev.fluentcart.com/database/query-builder\#webhook-logging-queries)

php

```
// Get failed webhook deliveries
$failedWebhooks = fluentCartDb()->table('fct_webhook_logger')
    ->where('status', 'failed')
    ->where('created_at', '>=', now()->subDay())
    ->get();

// Get webhook delivery statistics
$webhookStats = fluentCartDb()->table('fct_webhook_logger')
    ->select('status', fluentCartDb()->raw('COUNT(*) as count'))
    ->where('created_at', '>=', now()->subWeek())
    ->groupBy('status')
    ->get();
```

### Complex E-commerce Queries [​](https://dev.fluentcart.com/database/query-builder\#complex-e-commerce-queries)

php

```
// Get customer lifetime value with order count
$customerStats = fluentCartDb()->table('fct_customers')
    ->leftJoin('fct_orders', 'fct_customers.id', '=', 'fct_orders.customer_id')
    ->select([\
        'fct_customers.id',\
        'fct_customers.email',\
        'fct_customers.first_name',\
        'fct_customers.last_name',\
        fluentCartDb()->raw('COUNT(fct_orders.id) as order_count'),\
        fluentCartDb()->raw('SUM(fct_orders.total_amount) as total_spent'),\
        fluentCartDb()->raw('AVG(fct_orders.total_amount) as avg_order_value')\
    ])
    ->where('fct_orders.payment_status', 'paid')
    ->groupBy('fct_customers.id', 'fct_customers.email', 'fct_customers.first_name', 'fct_customers.last_name')
    ->having('order_count', '>', 0)
    ->get();

// Get product sales report with variations
$productSales = fluentCartDb()->table('fct_order_items')
    ->join('fct_orders', 'fct_order_items.order_id', '=', 'fct_orders.id')
    ->leftJoin('fct_product_variations', 'fct_order_items.post_id', '=', 'fct_product_variations.post_id')
    ->select([\
        'fct_order_items.post_id',\
        'fct_product_variations.variation_title',\
        fluentCartDb()->raw('SUM(fct_order_items.quantity) as total_sold'),\
        fluentCartDb()->raw('SUM(fct_order_items.line_total) as total_revenue')\
    ])
    ->where('fct_orders.payment_status', 'paid')
    ->groupBy('fct_order_items.post_id', 'fct_product_variations.variation_title')
    ->orderBy('total_revenue', 'desc')
    ->get();
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

