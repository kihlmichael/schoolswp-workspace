# FluentCart Developer Docs - Database Models (Part 6/8)

Tous les modèles Eloquent exposés par FluentCart : orders, customers, products, subscriptions, coupons, licenses, taxes, shipping, etc.

---

## Product Model | FluentCart Developer Docs

**URL** : https://dev.fluentcart.com/database/models/product

[Skip to content](https://dev.fluentcart.com/database/models/product#VPContent)

# Product Model [​](https://dev.fluentcart.com/database/models/product\#product-model)

| DB Table Name | {wp\_db\_prefix}\_posts (WordPress posts table) |
| --- | --- |
| Schema | [Check Schema](https://dev.fluentcart.com/database/schema.html#posts-table) |
| Source File | fluent-cart/app/Models/Product.php |
| Name Space | FluentCart\\App\\Models |
| Class | FluentCart\\App\\Models\\Product |

## Attributes [​](https://dev.fluentcart.com/database/models/product\#attributes)

| Attribute | Data Type | Comment |
| --- | --- | --- |
| ID | Integer | Primary Key (WordPress post ID) |
| post\_author | Integer | Post author ID |
| post\_date | Date Time | Post creation date |
| post\_date\_gmt | Date Time | Post creation date (GMT) |
| post\_content | Text | Post content |
| post\_title | String | Post title |
| post\_excerpt | Text | Post excerpt |
| post\_status | String | Post status (publish, draft, etc.) |
| comment\_status | String | Comment status |
| ping\_status | String | Ping status |
| post\_password | String | Post password (hidden) |
| post\_name | String | Post slug |
| to\_ping | Text | URLs to ping (hidden) |
| pinged | Text | URLs that have been pinged (hidden) |
| post\_modified | Date Time | Post last modified date |
| post\_modified\_gmt | Date Time | Post last modified date (GMT) |
| post\_content\_filtered | Text | Filtered post content (hidden) |
| post\_parent | Integer | Parent post ID (hidden) |
| guid | String | Global unique identifier |
| menu\_order | Integer | Menu order (hidden) |
| post\_type | String | Post type (`fluent-products`) |
| post\_mime\_type | String | Post MIME type (hidden) |
| comment\_count | Integer | Comment count (hidden) |

### Appended Attributes [​](https://dev.fluentcart.com/database/models/product\#appended-attributes)

| Attribute | Data Type | Comment |
| --- | --- | --- |
| thumbnail | String | Product thumbnail URL (from `getThumbnailAttribute()`) |

### Searchable Attributes [​](https://dev.fluentcart.com/database/models/product\#searchable-attributes)

| Attribute |
| --- |
| post\_title |
| post\_status |

## Usage [​](https://dev.fluentcart.com/database/models/product\#usage)

Please check [Model Basic](https://dev.fluentcart.com/database/models.html) for Common methods.

### Accessing Attributes [​](https://dev.fluentcart.com/database/models/product\#accessing-attributes)

php

```
$product = FluentCart\App\Models\Product::find(1);

$product->ID; // returns WordPress post ID
$product->post_title; // returns product title
$product->post_content; // returns product description
$product->post_status; // returns product status
$product->thumbnail; // returns thumbnail URL (appended attribute)
```

## Methods [​](https://dev.fluentcart.com/database/models/product\#methods)

Along with Global Model methods, this model has few helper methods.

### getHasSubscriptionAttribute() [​](https://dev.fluentcart.com/database/models/product\#gethassubscriptionattribute)

Check if product has subscription variants. Iterates over all variants and returns `true` if any variant has `payment_type` set to `subscription` in its `other_info`.

- Returns `Boolean` \- True if product has subscription variants

php

```
$product = FluentCart\App\Models\Product::find(1);
$hasSubscription = $product->has_subscription; // returns boolean
```

### getThumbnailAttribute() [​](https://dev.fluentcart.com/database/models/product\#getthumbnailattribute)

Get product thumbnail URL. Returns the featured media URL from the product detail, or a placeholder SVG if no featured media is set.

- Returns `String` \- Thumbnail URL or placeholder

php

```
$product = FluentCart\App\Models\Product::find(1);
$thumbnail = $product->thumbnail; // returns thumbnail URL
```

### getViewUrlAttribute() [​](https://dev.fluentcart.com/database/models/product\#getviewurlattribute)

Get product view URL

- Returns `String` \- Product permalink

php

```
$product = FluentCart\App\Models\Product::find(1);
$viewUrl = $product->view_url; // returns product URL
```

### getEditUrlAttribute() [​](https://dev.fluentcart.com/database/models/product\#getediturlattribute)

Get product edit URL in WordPress admin

- Returns `String` \- Edit URL

php

```
$product = FluentCart\App\Models\Product::find(1);
$editUrl = $product->edit_url; // returns edit URL
```

### getTagsAttribute() [​](https://dev.fluentcart.com/database/models/product\#gettagsattribute)

Get product tags via WordPress taxonomy `product-tags`.

- Returns `Array|false` \- Product tags (WP\_Term objects) or false if none

php

```
$product = FluentCart\App\Models\Product::find(1);
$tags = $product->tags; // returns product tags
```

### getCategoriesAttribute() [​](https://dev.fluentcart.com/database/models/product\#getcategoriesattribute)

Get product categories via WordPress taxonomy `product-categories`.

- Returns `Array|false` \- Product categories (WP\_Term objects) or false if none

php

```
$product = FluentCart\App\Models\Product::find(1);
$categories = $product->categories; // returns product categories
```

### getCategories() [​](https://dev.fluentcart.com/database/models/product\#getcategories)

Get product categories using `get_the_terms()` with taxonomy `product-categories`.

- Returns `Array|false|WP_Error` \- Product categories

php

```
$product = FluentCart\App\Models\Product::find(1);
$categories = $product->getCategories();
```

### getTags() [​](https://dev.fluentcart.com/database/models/product\#gettags)

Get product tags using `get_the_terms()` with taxonomy `product-tags`.

- Returns `Array|false|WP_Error` \- Product tags

php

```
$product = FluentCart\App\Models\Product::find(1);
$tags = $product->getTags();
```

### getMediaUrl($size = 'thumbnail') [​](https://dev.fluentcart.com/database/models/product\#getmediaurl-size-thumbnail)

Get product media URL using `get_the_post_thumbnail_url()`.

- Parameters: `$size` (String) - Image size (default: `'thumbnail'`)
- Returns `String|false` \- Media URL or false

php

```
$product = FluentCart\App\Models\Product::find(1);
$mediaUrl = $product->getMediaUrl('large'); // returns media URL
```

### images() [​](https://dev.fluentcart.com/database/models/product\#images)

Get all product images including featured image, gallery images, and variant images. Returns a structured array with image type, URL, alt text, and attachment ID.

- Returns `Array` \- Array of image arrays with keys: `type`, `url`, `alt`, `product_title`, `attachment_id` (and `variation_title`, `variation_id` for variant images)

php

```
$product = FluentCart\App\Models\Product::with('variants')->find(1);
$images = $product->images();

// Each image has the structure:
// ['type' => 'gallery_image|thumbnail|variation_image', 'url' => '...', 'alt' => '...', ...]
```

### isBundleProduct() [​](https://dev.fluentcart.com/database/models/product\#isbundleproduct)

Check if the product is a bundle product by looking at the `is_bundle_product` flag in the product detail's `other_info`.

- Returns `Boolean` \- True if bundle product

php

```
$product = FluentCart\App\Models\Product::with('detail')->find(1);
$isBundle = $product->isBundleProduct(); // returns boolean
```

### soldIndividually() [​](https://dev.fluentcart.com/database/models/product\#soldindividually)

Check if the product is sold individually (quantity limited to 1) by reading the `sold_individually` flag from the product detail's `other_info`.

- Returns `Boolean` \- True if sold individually

php

```
$product = FluentCart\App\Models\Product::with('detail')->find(1);
$isSoldIndividually = $product->soldIndividually(); // returns boolean
```

### isStock() [​](https://dev.fluentcart.com/database/models/product\#isstock)

Check if the product is in stock. Handles both regular and bundle products. For bundle products, it also checks stock status of all child variations.

- Returns `Boolean` \- True if in stock

php

```
$product = FluentCart\App\Models\Product::with(['detail', 'variants'])->find(1);
$inStock = $product->isStock(); // returns boolean
```

### getProductMeta($metaKey, $objectType = null, $default = null) [​](https://dev.fluentcart.com/database/models/product\#getproductmeta-metakey-objecttype-null-default-null)

Get product meta value from the `fct_meta` table via the `ProductMeta` model.

- Parameters:
  - `$metaKey` (String) - Meta key
  - `$objectType` (String\|null) - Object type filter (optional)
  - `$default` (Mixed) - Default value if not found (optional)
- Returns `Mixed` \- Meta value or default

php

```
$product = FluentCart\App\Models\Product::find(1);

// Without object type
$metaValue = $product->getProductMeta('custom_field', null, 'default');

// With object type
$metaValue = $product->getProductMeta('license_settings', 'product_integration');
```

### updateProductMeta($metaKey, $metaValue, $objectType = null) [​](https://dev.fluentcart.com/database/models/product\#updateproductmeta-metakey-metavalue-objecttype-null)

Update or create product meta value in the `fct_meta` table via the `ProductMeta` model. If the meta key already exists, updates it; otherwise creates a new entry.

- Parameters:
  - `$metaKey` (String) - Meta key
  - `$metaValue` (Mixed) - Meta value
  - `$objectType` (String\|null) - Object type (optional)
- Returns `FluentCart\App\Models\ProductMeta` \- The created or updated ProductMeta instance

php

```
$product = FluentCart\App\Models\Product::find(1);

// Without object type
$meta = $product->updateProductMeta('custom_field', 'new_value');

// With object type
$meta = $product->updateProductMeta('custom_field', 'new_value', 'product_integration');
```

### getTermByType($type) [​](https://dev.fluentcart.com/database/models/product\#gettermbytype-type)

Get term relationships for the product filtered by a specific taxonomy type. Joins through `term_taxonomy` and `terms` tables.

- Parameters: `$type` (String) - Taxonomy type (e.g., `'product-categories'`, `'product-tags'`)
- Returns `HasMany` \- Query builder with term data

php

```
$product = FluentCart\App\Models\Product::find(1);
$terms = $product->getTermByType('product-categories');
```

### duplicateProduct($productId, array $options = \[\]) [​](https://dev.fluentcart.com/database/models/product\#duplicateproduct-productid-array-options)

Static method that duplicates a product including its detail, variants, downloadable files, taxonomies, and post meta. The new product is created as a draft.

- Parameters:
  - `$productId` (Integer) - The ID of the product to duplicate
  - `$options`(Array) - Duplication options:
    - `import_stock_management` (Boolean) - Copy stock management settings (default: `false`)
    - `import_license_settings` (Boolean) - Copy license settings (default: `false`)
    - `import_downloadable_files` (Boolean) - Copy downloadable files (default: `false`)
- Returns `Integer` \- The new product ID
- Throws `RuntimeException` \- If product not found or duplication fails
- Fires action: `fluent_cart/product_duplicated`

php

```
use FluentCart\App\Models\Product;

// Basic duplication
$newProductId = Product::duplicateProduct(123);

// Duplication with options
$newProductId = Product::duplicateProduct(123, [\
    'import_stock_management' => true,\
    'import_license_settings' => true,\
    'import_downloadable_files' => true,\
]);
```

## Relations [​](https://dev.fluentcart.com/database/models/product\#relations)

This model has the following relationships that you can use

### detail [​](https://dev.fluentcart.com/database/models/product\#detail)

Access the product details.

- Returns `FluentCart\App\Models\ProductDetail` (HasOne)

php

```
$product = FluentCart\App\Models\Product::find(1);
$details = $product->detail;
```

### variants [​](https://dev.fluentcart.com/database/models/product\#variants)

Access the product variations.

- Returns `Collection` of `FluentCart\App\Models\ProductVariation` (HasMany)

php

```
$product = FluentCart\App\Models\Product::find(1);
$variants = $product->variants;
```

### downloadable\_files [​](https://dev.fluentcart.com/database/models/product\#downloadable-files)

Access the product downloads.

- Returns `Collection` of `FluentCart\App\Models\ProductDownload` (HasMany)

php

```
$product = FluentCart\App\Models\Product::find(1);
$downloads = $product->downloadable_files;
```

### postmeta [​](https://dev.fluentcart.com/database/models/product\#postmeta)

Access the product gallery image post meta. Filtered to only return the `fluent-products-gallery-image` meta key.

- Returns `FluentCart\App\Models\WpModels\PostMeta` (HasOne)

php

```
$product = FluentCart\App\Models\Product::find(1);
$postmeta = $product->postmeta;
```

### wp\_terms [​](https://dev.fluentcart.com/database/models/product\#wp-terms)

Access the WordPress term relationships for this product.

- Returns `Collection` of `FluentCart\App\Models\WpModels\TermRelationship` (HasMany)

php

```
$product = FluentCart\App\Models\Product::find(1);
$terms = $product->wp_terms;
```

### orderItems [​](https://dev.fluentcart.com/database/models/product\#orderitems)

Access the order items for this product.

- Returns `Collection` of `FluentCart\App\Models\OrderItem` (HasMany)

php

```
$product = FluentCart\App\Models\Product::find(1);
$orderItems = $product->orderItems;
```

### wpTerms() [​](https://dev.fluentcart.com/database/models/product\#wpterms)

Access the WordPress term taxonomies through the term relationships table (hasManyThrough).

- Returns `Collection` of `FluentCart\App\Models\WpModels\TermTaxonomy` (HasManyThrough)

php

```
$product = FluentCart\App\Models\Product::find(1);
$terms = $product->wpTerms;
```

### categories() [​](https://dev.fluentcart.com/database/models/product\#categories)

Get product categories relationship. Uses `getTermByType('product-categories')` internally.

- Returns `HasMany` with joined term data

php

```
$product = FluentCart\App\Models\Product::find(1);
$categories = $product->categories;
```

### tags() [​](https://dev.fluentcart.com/database/models/product\#tags)

Get product tags relationship. Uses `getTermByType('product-tags')` internally.

- Returns `HasMany` with joined term data

php

```
$product = FluentCart\App\Models\Product::find(1);
$tags = $product->tags;
```

### thumbUrl [​](https://dev.fluentcart.com/database/models/product\#thumburl)

Access the product thumbnail URL via post meta. Joins through `_thumbnail_id` meta key to get the `_wp_attached_file` value.

- Returns `FluentCart\App\Models\WpModels\PostMeta` with additional `image` attribute (HasOne)

php

```
$product = FluentCart\App\Models\Product::find(1);
$thumbUrl = $product->thumbUrl;
$imageFile = $thumbUrl->image; // relative file path
```

### licensesMeta [​](https://dev.fluentcart.com/database/models/product\#licensesmeta)

Access the license settings meta for this product. Filtered to `meta_key = 'license_settings'`.

- Returns `FluentCart\App\Models\ProductMeta` (HasOne)

php

```
$product = FluentCart\App\Models\Product::find(1);
$licenseMeta = $product->licensesMeta;
```

### integrations [​](https://dev.fluentcart.com/database/models/product\#integrations)

Access the product integration meta entries. Filtered to `object_type = 'product_integration'`.

- Returns `Collection` of `FluentCart\App\Models\ProductMeta` (HasMany)

php

```
$product = FluentCart\App\Models\Product::find(1);
$integrations = $product->integrations;
```

## Scopes [​](https://dev.fluentcart.com/database/models/product\#scopes)

This model has the following scopes that you can use

### published() [​](https://dev.fluentcart.com/database/models/product\#published)

Get only published products

php

```
$products = FluentCart\App\Models\Product::published()->get();
```

### statusOf($status) [​](https://dev.fluentcart.com/database/models/product\#statusof-status)

Get products by specific status

php

```
$products = FluentCart\App\Models\Product::statusOf('publish')->get();
```

### adminAll() [​](https://dev.fluentcart.com/database/models/product\#adminall)

Get all products for admin view (includes all admin-visible statuses)

php

```
$products = FluentCart\App\Models\Product::adminAll()->get();
```

### cartable() [​](https://dev.fluentcart.com/database/models/product\#cartable)

Get cartable products (excludes products with license meta and filters to non-subscription variants with media loaded)

php

```
$products = FluentCart\App\Models\Product::cartable()->get();
```

### applyCustomSortBy($sortKey, $sortType = 'DESC') [​](https://dev.fluentcart.com/database/models/product\#applycustomsortby-sortkey-sorttype-desc)

Apply custom sorting. Valid sort keys: `id`, `date`, `title`, `price`. When sorting by `price`, joins the `fct_product_details` table and sorts by `min_price`.

- Parameters: `$sortKey` (String) - Sort key (`id`\|`date`\|`title`\|`price`), `$sortType` (String) - Sort direction (`ASC`\|`DESC`)

php

```
$products = FluentCart\App\Models\Product::applyCustomSortBy('title', 'ASC')->get();
$products = FluentCart\App\Models\Product::applyCustomSortBy('price', 'DESC')->get();
```

### byVariantTypes($type) [​](https://dev.fluentcart.com/database/models/product\#byvarianttypes-type)

Filter by variant types. Valid types: `physical`, `digital`, `subscription`, `onetime`, `simple`, `variations`.

- Parameters: `$type` (String) - Variant type

php

```
$products = FluentCart\App\Models\Product::byVariantTypes('physical')->get();
$products = FluentCart\App\Models\Product::byVariantTypes('subscription')->get();
$products = FluentCart\App\Models\Product::byVariantTypes('simple')->get();
```

### filterByTaxonomy($taxonomies) [​](https://dev.fluentcart.com/database/models/product\#filterbytaxonomy-taxonomies)

Filter by taxonomies. Accepts an associative array where keys are taxonomy names and values are arrays of term IDs.

- Parameters: `$taxonomies` (Array) - Taxonomy filters

php

```
$products = FluentCart\App\Models\Product::filterByTaxonomy([\
    'product-categories' => [1, 2, 3],\
    'product-brands' => [4, 5, 6],\
])->get();
```

### bundle() [​](https://dev.fluentcart.com/database/models/product\#bundle)

Get only bundle products (products where `other_info->is_bundle_product` is `'yes'` in the product detail).

php

```
$products = FluentCart\App\Models\Product::bundle()->get();
```

### nonBundle() [​](https://dev.fluentcart.com/database/models/product\#nonbundle)

Get only non-bundle products (products where `other_info->is_bundle_product` is not `'yes'` or is null in the product detail).

php

```
$products = FluentCart\App\Models\Product::nonBundle()->get();
```

## Global Scope [​](https://dev.fluentcart.com/database/models/product\#global-scope)

The Product model applies a global scope that automatically filters queries to only include posts with `post_type = 'fluent-products'` and excludes `auto-draft` status. This scope is applied on all queries. Additionally, when creating a new Product, the `post_type` is automatically set to `fluent-products`.

## Usage Examples [​](https://dev.fluentcart.com/database/models/product\#usage-examples)

### Creating a Product [​](https://dev.fluentcart.com/database/models/product\#creating-a-product)

php

```
use FluentCart\App\Models\Product;

$product = Product::create([\
    'post_title' => 'Sample Product',\
    'post_content' => 'Product description',\
    'post_status' => 'publish',\
]);
// post_type is automatically set to 'fluent-products' via the creating event
```

### Retrieving Products [​](https://dev.fluentcart.com/database/models/product\#retrieving-products)

php

```
// Get all published products
$products = Product::published()->get();

// Get product by ID
$product = Product::find(1);

// Get products with variations
$products = Product::with('variants')->get();

// Get products with detail and variants
$products = Product::with(['detail', 'variants'])->get();
```

### Updating a Product [​](https://dev.fluentcart.com/database/models/product\#updating-a-product)

php

```
$product = Product::find(1);
$product->post_title = 'Updated Product Title';
$product->save();
```

### Deleting a Product [​](https://dev.fluentcart.com/database/models/product\#deleting-a-product)

php

```
$product = Product::find(1);
$product->delete();
```

* * *


---

---

## Product Detail Model | FluentCart Developer Docs

**URL** : https://dev.fluentcart.com/database/models/product-detail

[Skip to content](https://dev.fluentcart.com/database/models/product-detail#VPContent)

# Product Detail Model [​](https://dev.fluentcart.com/database/models/product-detail\#product-detail-model)

| DB Table Name | {wp\_db\_prefix}\_fct\_product\_details |
| --- | --- |
| Schema | [Check Schema](https://dev.fluentcart.com/database/schema.html#fct-product-details-table) |
| Source File | fluent-cart/app/Models/ProductDetail.php |
| Name Space | FluentCart\\App\\Models |
| Class | FluentCart\\App\\Models\\ProductDetail |

## Traits [​](https://dev.fluentcart.com/database/models/product-detail\#traits)

| Trait | Description |
| --- | --- |
| CanSearch | Adds search scope capabilities to the model |
| CanUpdateBatch | Adds batch update capabilities to the model |

## Attributes [​](https://dev.fluentcart.com/database/models/product-detail\#attributes)

| Attribute | Data Type | Comment |
| --- | --- | --- |
| id | Integer | Primary Key (guarded) |
| post\_id | Integer | Reference to WordPress post (product). Cast as `integer`. |
| fulfillment\_type | String | Fulfillment type (physical, digital) |
| min\_price | Double | Minimum price (cents). Cast as `double`. Dynamically computed from variants via accessor. |
| max\_price | Double | Maximum price (cents). Cast as `double`. Dynamically computed from variants via accessor. |
| default\_variation\_id | String | Default variation ID |
| variation\_type | String | Variation type (simple, variable) |
| stock\_availability | String | Stock availability quantity / status |
| other\_info | JSON | Additional product information (auto JSON encoded/decoded via mutator/accessor) |
| default\_media | JSON | Default media information (auto JSON encoded/decoded via mutator/accessor) |
| manage\_stock | String | Whether to manage stock |
| manage\_downloadable | String | Whether to manage downloadable files |
| created\_at | Date Time | Creation timestamp |
| updated\_at | Date Time | Last update timestamp |

## Fillable Attributes [​](https://dev.fluentcart.com/database/models/product-detail\#fillable-attributes)

The following attributes are mass-assignable:

`post_id`, `fulfillment_type`, `min_price`, `max_price`, `default_variation_id`, `variation_type`, `stock_availability`, `other_info`, `default_media`, `manage_stock`, `manage_downloadable`

The `id` attribute is guarded and cannot be mass-assigned.

## Casts [​](https://dev.fluentcart.com/database/models/product-detail\#casts)

| Attribute | Cast Type |
| --- | --- |
| post\_id | integer |
| min\_price | double |
| max\_price | double |

## Appends [​](https://dev.fluentcart.com/database/models/product-detail\#appends)

The following computed attributes are automatically appended to the model's array/JSON output:

| Appended Attribute | Description |
| --- | --- |
| featured\_media | First image from the gallery (via `getFeaturedMediaAttribute`) |
| formatted\_min\_price | Human-readable minimum price (via `getFormattedMinPriceAttribute`) |
| formatted\_max\_price | Human-readable maximum price (via `getFormattedMaxPriceAttribute`) |

## Usage [​](https://dev.fluentcart.com/database/models/product-detail\#usage)

Please check [Model Basic](https://dev.fluentcart.com/database/models.html) for Common methods.

### Accessing Attributes [​](https://dev.fluentcart.com/database/models/product-detail\#accessing-attributes)

php

```
$productDetail = FluentCart\App\Models\ProductDetail::find(1);

$productDetail->id; // returns id
$productDetail->post_id; // returns post ID (cast as integer)
$productDetail->min_price; // returns minimum price (dynamically computed from variants)
$productDetail->max_price; // returns maximum price (dynamically computed from variants)
$productDetail->featured_media; // returns first gallery image or null (appended)
$productDetail->formatted_min_price; // returns formatted min price string (appended)
$productDetail->formatted_max_price; // returns formatted max price string (appended)
```

## Relations [​](https://dev.fluentcart.com/database/models/product-detail\#relations)

This model has the following relationships that you can use

### product [​](https://dev.fluentcart.com/database/models/product-detail\#product)

Access the associated product (WordPress post). Linked via `post_id` to `ID` on the products table.

- Relationship type: `BelongsTo`
- return `FluentCart\App\Models\Product` Model

#### Example: [​](https://dev.fluentcart.com/database/models/product-detail\#example)

php

```
// Accessing Product
$product = $productDetail->product;

// For Filtering by product relationship
$productDetails = FluentCart\App\Models\ProductDetail::whereHas('product', function($query) {
    $query->where('post_status', 'publish');
})->get();
```

### galleryImage [​](https://dev.fluentcart.com/database/models/product-detail\#galleryimage)

Access the associated gallery image meta. This is a `HasOne` relation to `PostMeta` filtered by `meta_key = 'fluent-products-gallery-image'`, linked via `post_id`.

- Relationship type: `HasOne`
- return `FluentCart\App\Models\WpModels\PostMeta` Model

#### Example: [​](https://dev.fluentcart.com/database/models/product-detail\#example-1)

php

```
// Accessing Gallery Image
$galleryImage = $productDetail->galleryImage;
```

### variants [​](https://dev.fluentcart.com/database/models/product-detail\#variants)

Access all product variations, ordered by `serial_index` ascending. Linked via `post_id` on both tables.

- Relationship type: `HasMany`
- return `FluentCart\App\Models\ProductVariation` Model Collection

#### Example: [​](https://dev.fluentcart.com/database/models/product-detail\#example-2)

php

```
// Accessing Variants
$variants = $productDetail->variants;

// For Filtering by variants relationship
$productDetails = FluentCart\App\Models\ProductDetail::whereHas('variants', function($query) {
    $query->where('status', 'active');
})->get();
```

### attrMap [​](https://dev.fluentcart.com/database/models/product-detail\#attrmap)

Access all attribute relations. Linked via `object_id` (on `AttributeRelation`) to `id` (on `ProductDetail`).

When a `ProductDetail` record is deleted, all related `attrMap` records are automatically cascade-deleted via the model's `boot()` method.

- Relationship type: `HasMany`
- return `FluentCart\App\Models\AttributeRelation` Model Collection

#### Example: [​](https://dev.fluentcart.com/database/models/product-detail\#example-3)

php

```
// Accessing Attribute Relations
$attrMap = $productDetail->attrMap;
```

## Cascade Deletes [​](https://dev.fluentcart.com/database/models/product-detail\#cascade-deletes)

The model registers a `deleting` event in its `boot()` method. When a `ProductDetail` is deleted, all associated `attrMap` (AttributeRelation) records are automatically deleted:

php

```
// When you delete a ProductDetail, its attrMap relations are removed automatically
$productDetail->delete(); // Also deletes all related AttributeRelation records
```

## Methods [​](https://dev.fluentcart.com/database/models/product-detail\#methods)

Along with Global Model methods, this model has few helper methods.

### setOtherInfoAttribute($value) [​](https://dev.fluentcart.com/database/models/product-detail\#setotherinfoattribute-value)

Set other info with automatic JSON encoding (mutator). Arrays and objects are JSON encoded; strings are stored as-is.

- Parameters
  - $value - mixed (array, object, or string)
- Returns `void`

#### Usage [​](https://dev.fluentcart.com/database/models/product-detail\#usage-1)

php

```
$productDetail->other_info = ['custom_data' => 'value', 'settings' => ['key' => 'value']];
// Automatically JSON encodes arrays and objects
```

### getOtherInfoAttribute($value) [​](https://dev.fluentcart.com/database/models/product-detail\#getotherinfoattribute-value)

Get other info with automatic JSON decoding (accessor). Returns the decoded array or `null` if empty.

- Parameters
  - $value - mixed
- Returns `array|null`

#### Usage [​](https://dev.fluentcart.com/database/models/product-detail\#usage-2)

php

```
$otherInfo = $productDetail->other_info; // Returns decoded array or null
```

### setDefaultMediaAttribute($value) [​](https://dev.fluentcart.com/database/models/product-detail\#setdefaultmediaattribute-value)

Set default media with automatic JSON encoding (mutator). Arrays and objects are JSON encoded; strings are stored as-is.

- Parameters
  - $value - mixed (array, object, or string)
- Returns `void`

#### Usage [​](https://dev.fluentcart.com/database/models/product-detail\#usage-3)

php

```
$productDetail->default_media = ['url' => 'image.jpg', 'alt' => 'Product Image'];
// Automatically JSON encodes arrays and objects
```

### getDefaultMediaAttribute($value) [​](https://dev.fluentcart.com/database/models/product-detail\#getdefaultmediaattribute-value)

Get default media with automatic JSON decoding (accessor). Returns the decoded array or `null` if empty.

- Parameters
  - $value - mixed
- Returns `array|null`

#### Usage [​](https://dev.fluentcart.com/database/models/product-detail\#usage-4)

php

```
$defaultMedia = $productDetail->default_media; // Returns decoded array or null
```

### getMinPriceAttribute() [​](https://dev.fluentcart.com/database/models/product-detail\#getminpriceattribute)

Dynamic accessor that overrides the `min_price` database column. Instead of returning the stored value, it computes the minimum `item_price` from all associated variants.

- Parameters
  - none
- Returns `double|null`

#### Usage [​](https://dev.fluentcart.com/database/models/product-detail\#usage-5)

php

```
$minPrice = $productDetail->min_price; // Returns the minimum item_price across all variants
```

### getMaxPriceAttribute() [​](https://dev.fluentcart.com/database/models/product-detail\#getmaxpriceattribute)

Dynamic accessor that overrides the `max_price` database column. Instead of returning the stored value, it computes the maximum `item_price` from all associated variants.

- Parameters
  - none
- Returns `double|null`

#### Usage [​](https://dev.fluentcart.com/database/models/product-detail\#usage-6)

php

```
$maxPrice = $productDetail->max_price; // Returns the maximum item_price across all variants
```

### getFormattedMinPriceAttribute() [​](https://dev.fluentcart.com/database/models/product-detail\#getformattedminpriceattribute)

Get formatted minimum price (accessor). Uses `Helper::toDecimal()` to convert the min\_price (in cents) to a human-readable decimal string.

- Parameters
  - none
- Returns `string`

#### Usage [​](https://dev.fluentcart.com/database/models/product-detail\#usage-7)

php

```
$formattedMinPrice = $productDetail->formatted_min_price; // Returns formatted price string
```

### getFormattedMaxPriceAttribute() [​](https://dev.fluentcart.com/database/models/product-detail\#getformattedmaxpriceattribute)

Get formatted maximum price (accessor). Uses `Helper::toDecimal()` to convert the max\_price (in cents) to a human-readable decimal string.

- Parameters
  - none
- Returns `string`

#### Usage [​](https://dev.fluentcart.com/database/models/product-detail\#usage-8)

php

```
$formattedMaxPrice = $productDetail->formatted_max_price; // Returns formatted price string
```

### getFeaturedMediaAttribute() [​](https://dev.fluentcart.com/database/models/product-detail\#getfeaturedmediaattribute)

Get featured media from gallery (accessor). Returns the first element from the gallery image meta value, or `null` if the gallery is empty or not set.

- Parameters
  - none
- Returns `mixed|null`

#### Usage [​](https://dev.fluentcart.com/database/models/product-detail\#usage-9)

php

```
$featuredMedia = $productDetail->featured_media; // Returns first gallery image or null
```

### hasPriceVariation() [​](https://dev.fluentcart.com/database/models/product-detail\#haspricevariation)

Check if product has a price variation. Returns `true` only when the product's `variation_type` is `'simple'` **and**`max_price` differs from `min_price`.

- Parameters
  - none
- Returns `boolean`

#### Usage [​](https://dev.fluentcart.com/database/models/product-detail\#usage-10)

php

```
$hasVariation = $productDetail->hasPriceVariation();
// Returns true if variation_type is 'simple' AND min_price != max_price
```

### getStockAvailability($variationId = null) [​](https://dev.fluentcart.com/database/models/product-detail\#getstockavailability-variationid-null)

Get stock availability information. Returns an array describing stock status. The result is passed through the `fluent_cart/product_stock_availability` filter hook, allowing external modification.

- Parameters
  - $variationId - integer\|null (default: null)
- Returns `array` with keys: `manage_stock` (bool), `availability` (string), `class` (string), `available_quantity` (int\|null)

**Return scenarios:**

| Condition | manage\_stock | availability | class | available\_quantity |
| --- | --- | --- | --- | --- |
| `manage_stock` is falsy | `false` | "In Stock" | "in-stock" | `null` |
| `manage_stock` truthy, `stock_availability` truthy | `true` | "In Stock" | "in-stock" | `stock_availability` value |
| `manage_stock` truthy, `stock_availability` falsy | `true` | "Out of Stock" | "out-of-stock" | `stock_availability` value |

**Filter hook:**`fluent_cart/product_stock_availability`

- Receives: `$availability` array, `['detail' => $this, 'variation_id' => $variationId]`

#### Usage [​](https://dev.fluentcart.com/database/models/product-detail\#usage-11)

php

```
$stockInfo = $productDetail->getStockAvailability();
// Returns array with manage_stock, availability, class, available_quantity

// With a specific variation
$stockInfo = $productDetail->getStockAvailability($variationId);
```

## Usage Examples [​](https://dev.fluentcart.com/database/models/product-detail\#usage-examples)

### Get Product Details [​](https://dev.fluentcart.com/database/models/product-detail\#get-product-details)

php

```
$productDetail = FluentCart\App\Models\ProductDetail::find(1);
echo "Min Price: " . $productDetail->formatted_min_price;
echo "Max Price: " . $productDetail->formatted_max_price;
echo "Stock: " . $productDetail->getStockAvailability()['availability'];
```

### Get Product with Variations [​](https://dev.fluentcart.com/database/models/product-detail\#get-product-with-variations)

php

```
$productDetail = FluentCart\App\Models\ProductDetail::with(['product', 'variants'])->find(1);
$product = $productDetail->product;
$variants = $productDetail->variants;
```

### Create Product Detail [​](https://dev.fluentcart.com/database/models/product-detail\#create-product-detail)

php

```
$productDetail = FluentCart\App\Models\ProductDetail::create([\
    'post_id' => 123,\
    'fulfillment_type' => 'physical',\
    'min_price' => 19.99,\
    'max_price' => 29.99,\
    'variation_type' => 'simple',\
    'stock_availability' => 'in-stock',\
    'manage_stock' => '1',\
    'manage_downloadable' => '0'\
]);
```

### Check Stock Availability [​](https://dev.fluentcart.com/database/models/product-detail\#check-stock-availability)

php

```
$productDetail = FluentCart\App\Models\ProductDetail::find(1);
$stockInfo = $productDetail->getStockAvailability();

if ($stockInfo['manage_stock']) {
    echo "Stock: " . $stockInfo['available_quantity'];
} else {
    echo "Stock: " . $stockInfo['availability'];
}
```

### Get Featured Media [​](https://dev.fluentcart.com/database/models/product-detail\#get-featured-media)

php

```
$productDetail = FluentCart\App\Models\ProductDetail::find(1);
$featuredMedia = $productDetail->featured_media;

if ($featuredMedia) {
    echo "Featured Image: " . $featuredMedia['url'];
}
```

### Dynamic Price Computation [​](https://dev.fluentcart.com/database/models/product-detail\#dynamic-price-computation)

php

```
// min_price and max_price are dynamically computed from variants
$productDetail = FluentCart\App\Models\ProductDetail::find(1);

// These pull min/max item_price from the variants table, not the stored column values
$minPrice = $productDetail->min_price;
$maxPrice = $productDetail->max_price;

// Check if a simple product has a price range
if ($productDetail->hasPriceVariation()) {
    echo "Price range: $minPrice - $maxPrice";
}
```

* * *

Today

Hi! I’m your AI assistant. How can I assist you today?

Just now

Powered by **FluentBot**


---

---

## Product Download Model | FluentCart Developer Docs

**URL** : https://dev.fluentcart.com/database/models/product-download

[Skip to content](https://dev.fluentcart.com/database/models/product-download#VPContent)

# Product Download Model [​](https://dev.fluentcart.com/database/models/product-download\#product-download-model)

| DB Table Name | {wp\_db\_prefix}\_fct\_product\_downloads |
| --- | --- |
| Schema | [Check Schema](https://dev.fluentcart.com/database/schema.html#fct-product-downloads-table) |
| Source File | fluent-cart/app/Models/ProductDownload.php |
| Name Space | FluentCart\\App\\Models |
| Class | FluentCart\\App\\Models\\ProductDownload |

## Traits [​](https://dev.fluentcart.com/database/models/product-download\#traits)

| Trait | Description |
| --- | --- |
| CanSearch | Provides `search()`, `groupSearch()`, `whereLike()`, `whereBeginsWith()`, `whereEndsWith()` query scopes |

## Attributes [​](https://dev.fluentcart.com/database/models/product-download\#attributes)

| Attribute | Data Type | Comment |
| --- | --- | --- |
| id | Integer | Primary Key |
| post\_id | Integer | Reference to WordPress post (product) |
| product\_variation\_id | JSON | Product variation IDs (JSON encoded array, auto-encoded/decoded via mutator/accessor) |
| download\_identifier | String | Download identifier |
| title | String | Download title |
| type | String | Download type |
| driver | String | Storage driver |
| file\_name | String | File name |
| file\_path | String | File path |
| file\_url | String | File URL |
| file\_size | Integer | File size in bytes |
| settings | JSON | Download settings (auto-encoded/decoded via mutator/accessor) |
| serial | String | Serial number |
| created\_at | Date Time | Creation timestamp |
| updated\_at | Date Time | Last update timestamp |

## Usage [​](https://dev.fluentcart.com/database/models/product-download\#usage)

Please check [Model Basic](https://dev.fluentcart.com/database/models.html) for Common methods.

### Accessing Attributes [​](https://dev.fluentcart.com/database/models/product-download\#accessing-attributes)

php

```
$productDownload = FluentCart\App\Models\ProductDownload::find(1);

$productDownload->id; // returns id
$productDownload->post_id; // returns post ID
$productDownload->title; // returns download title
$productDownload->file_size; // returns file size
$productDownload->product_variation_id; // returns array of variation IDs
$productDownload->settings; // returns decoded settings array
```

## Scopes [​](https://dev.fluentcart.com/database/models/product-download\#scopes)

This model has the following scopes that you can use

### search($params) from CanSearch [​](https://dev.fluentcart.com/database/models/product-download\#search-params)

Search downloads by parameters. Supports operators: `=`, `between`, `like_all`, `in`, `not_in`, `is_null`, `is_not_null`, and more.

- Parameters
  - `$params` (Array) - Search parameters

#### Usage: [​](https://dev.fluentcart.com/database/models/product-download\#usage-1)

php

```
$downloads = FluentCart\App\Models\ProductDownload::search([\
    'type' => ['value' => 'pdf', 'operator' => '=']\
])->get();
```

## Relations [​](https://dev.fluentcart.com/database/models/product-download\#relations)

This model has the following relationships that you can use

### product [​](https://dev.fluentcart.com/database/models/product-download\#product)

Access the associated product (WordPress post)

- return `FluentCart\App\Models\Product` Model (BelongsTo via `post_id` -\> `ID`)

#### Example: [​](https://dev.fluentcart.com/database/models/product-download\#example)

php

```
// Accessing Product
$product = $productDownload->product;

// For Filtering by product relationship
$productDownloads = FluentCart\App\Models\ProductDownload::whereHas('product', function($query) {
    $query->where('post_status', 'publish');
})->get();
```

### download\_permissions [​](https://dev.fluentcart.com/database/models/product-download\#download-permissions)

Access all download permissions for this download

- return `FluentCart\App\Models\OrderDownloadPermission` Model Collection (HasMany via `download_id` -\> `id`)

#### Example: [​](https://dev.fluentcart.com/database/models/product-download\#example-1)

php

```
// Accessing Download Permissions
$permissions = $productDownload->download_permissions;

// For Filtering by download permissions relationship
$productDownloads = FluentCart\App\Models\ProductDownload::whereHas('download_permissions', function($query) {
    $query->where('download_count', '<', 'download_limit');
})->get();
```

## Methods [​](https://dev.fluentcart.com/database/models/product-download\#methods)

Along with Global Model methods, this model has few helper methods.

### setSettingsAttribute($settings) [​](https://dev.fluentcart.com/database/models/product-download\#setsettingsattribute-settings)

Set settings with automatic JSON encoding (mutator). Arrays and objects are encoded with `JSON_UNESCAPED_UNICODE | JSON_UNESCAPED_SLASHES` flags.

- Parameters
  - `$settings` \- mixed (array, object, or string)
- Returns `void`

#### Usage [​](https://dev.fluentcart.com/database/models/product-download\#usage-2)

php

```
$productDownload->settings = ['access_limit' => 5, 'expiry_days' => 30];
// Automatically JSON encodes arrays and objects
```

### getSettingsAttribute($settings) [​](https://dev.fluentcart.com/database/models/product-download\#getsettingsattribute-settings)

Get settings with automatic JSON decoding (accessor). If the stored string is valid JSON, it returns the decoded array. Otherwise, returns the raw value.

- Parameters
  - `$settings` \- mixed
- Returns `mixed`

#### Usage [​](https://dev.fluentcart.com/database/models/product-download\#usage-3)

php

```
$settings = $productDownload->settings; // Returns decoded value (array, object, or string)
```

### setProductVariationIdAttribute($variations) [​](https://dev.fluentcart.com/database/models/product-download\#setproductvariationidattribute-variations)

Set product variation IDs with automatic JSON encoding (mutator). Accepts an array of IDs, a single numeric ID (wrapped in an array), or defaults to an empty array.

- Parameters
  - `$variations` \- array\|int\|mixed
- Returns `void`

#### Usage [​](https://dev.fluentcart.com/database/models/product-download\#usage-4)

php

```
$productDownload->product_variation_id = [1, 2, 3];
// Automatically JSON encodes array

$productDownload->product_variation_id = 5;
// Automatically wraps in array: [5]
```

### getProductVariationIdAttribute($value) [​](https://dev.fluentcart.com/database/models/product-download\#getproductvariationidattribute-value)

Get product variation IDs with automatic JSON decoding (accessor). Always returns an array.

- Parameters
  - `$value` \- mixed
- Returns `array`

#### Usage [​](https://dev.fluentcart.com/database/models/product-download\#usage-5)

php

```
$variationIds = $productDownload->product_variation_id; // Returns array of variation IDs
```

### getSignedDownloadUrl() [​](https://dev.fluentcart.com/database/models/product-download\#getsigneddownloadurl)

Get signed download URL using the `DownloadService`. Generates a secure, time-limited URL for file access.

- Parameters
  - none
- Returns `string`

#### Usage [​](https://dev.fluentcart.com/database/models/product-download\#usage-6)

php

```
$downloadUrl = $productDownload->getSignedDownloadUrl();
echo "Download URL: " . $downloadUrl;
```

## Usage Examples [​](https://dev.fluentcart.com/database/models/product-download\#usage-examples)

### Get Product Downloads [​](https://dev.fluentcart.com/database/models/product-download\#get-product-downloads)

php

```
$productDownload = FluentCart\App\Models\ProductDownload::find(1);
echo "Title: " . $productDownload->title;
echo "File Size: " . $productDownload->file_size . " bytes";
echo "Download URL: " . $productDownload->getSignedDownloadUrl();
```

### Get Downloads for Product [​](https://dev.fluentcart.com/database/models/product-download\#get-downloads-for-product)

php

```
$product = FluentCart\App\Models\Product::find(123);
$downloads = $product->downloads;

foreach ($downloads as $download) {
    echo "Download: " . $download->title;
    echo "Type: " . $download->type;
}
```

### Create Product Download [​](https://dev.fluentcart.com/database/models/product-download\#create-product-download)

php

```
$productDownload = FluentCart\App\Models\ProductDownload::create([\
    'post_id' => 123,\
    'product_variation_id' => [1, 2],\
    'download_identifier' => 'unique-id-123',\
    'title' => 'Product Manual',\
    'type' => 'pdf',\
    'driver' => 'local',\
    'file_name' => 'manual.pdf',\
    'file_path' => '/uploads/manual.pdf',\
    'file_size' => 1024000,\
    'settings' => ['access_limit' => 5, 'expiry_days' => 30]\
]);
```

### Get Download Permissions [​](https://dev.fluentcart.com/database/models/product-download\#get-download-permissions)

php

```
$download = FluentCart\App\Models\ProductDownload::find(1);
$permissions = $download->download_permissions;

foreach ($permissions as $permission) {
    echo "Customer: " . $permission->customer_id;
    echo "Downloads Used: " . $permission->download_count;
}
```

### Get Signed Download URL [​](https://dev.fluentcart.com/database/models/product-download\#get-signed-download-url)

php

```
$download = FluentCart\App\Models\ProductDownload::find(1);
$signedUrl = $download->getSignedDownloadUrl();
// Use this URL for secure download access
```

### Get Downloads by Type [​](https://dev.fluentcart.com/database/models/product-download\#get-downloads-by-type)

php

```
$pdfDownloads = FluentCart\App\Models\ProductDownload::where('type', 'pdf')->get();
$zipDownloads = FluentCart\App\Models\ProductDownload::where('type', 'zip')->get();
```

* * *

Today

Hi! I’m your AI assistant. How can I assist you today?

Just now

Powered by **FluentBot**


---

---

## Product Meta Model | FluentCart Developer Docs

**URL** : https://dev.fluentcart.com/database/models/product-meta

[Skip to content](https://dev.fluentcart.com/database/models/product-meta#VPContent)

# Product Meta Model [​](https://dev.fluentcart.com/database/models/product-meta\#product-meta-model)

| DB Table Name | {wp\_db\_prefix}\_fct\_product\_meta |
| --- | --- |
| Schema | [Check Schema](https://dev.fluentcart.com/database/schema.html#fct-product-meta-table) |
| Source File | fluent-cart/app/Models/ProductMeta.php |
| Name Space | FluentCart\\App\\Models |
| Class | FluentCart\\App\\Models\\ProductMeta |

## Attributes [​](https://dev.fluentcart.com/database/models/product-meta\#attributes)

| Attribute | Data Type | Comment |
| --- | --- | --- |
| id | Integer | Primary Key (guarded) |
| object\_id | Integer | ID of the associated object |
| object\_type | String | Type of object (product, variation, etc.) |
| meta\_key | String | Meta key name |
| meta\_value | Text | Meta value (JSON encoded for arrays/objects, auto-encoded/decoded via mutator/accessor) |
| created\_at | Date Time | Creation timestamp |
| updated\_at | Date Time | Last update timestamp |

## Usage [​](https://dev.fluentcart.com/database/models/product-meta\#usage)

Please check [Model Basic](https://dev.fluentcart.com/database/models.html) for Common methods.

### Accessing Attributes [​](https://dev.fluentcart.com/database/models/product-meta\#accessing-attributes)

php

```
$productMeta = FluentCart\App\Models\ProductMeta::find(1);

$productMeta->id; // returns id
$productMeta->object_id; // returns object ID
$productMeta->object_type; // returns object type
$productMeta->meta_key; // returns meta key
$productMeta->meta_value; // returns meta value (auto-decoded if JSON)
```

## Relations [​](https://dev.fluentcart.com/database/models/product-meta\#relations)

This model does not define any relationships. It is a generic meta storage model that uses `object_id` and `object_type` to associate with different parent entities (products, variations, etc.).

## Methods [​](https://dev.fluentcart.com/database/models/product-meta\#methods)

Along with Global Model methods, this model has few helper methods.

### setMetaValueAttribute($meta\_value) [​](https://dev.fluentcart.com/database/models/product-meta\#setmetavalueattribute-meta-value)

Set meta value with automatic JSON encoding (mutator). Arrays and objects are encoded with `JSON_UNESCAPED_UNICODE | JSON_UNESCAPED_SLASHES` flags.

- Parameters
  - `$meta_value` \- mixed (array, object, or string)
- Returns `void`

#### Usage [​](https://dev.fluentcart.com/database/models/product-meta\#usage-1)

php

```
$productMeta->meta_value = ['custom_data' => 'value', 'settings' => ['key' => 'value']];
// Automatically JSON encodes arrays and objects
```

### getMetaValueAttribute($value) [​](https://dev.fluentcart.com/database/models/product-meta\#getmetavalueattribute-value)

Get meta value with automatic JSON decoding (accessor). If the stored string is valid JSON, it returns the decoded array. Otherwise, returns the raw string value.

- Parameters
  - `$value` \- mixed
- Returns `mixed` (decoded array if valid JSON, otherwise original value)

#### Usage [​](https://dev.fluentcart.com/database/models/product-meta\#usage-2)

php

```
$metaValue = $productMeta->meta_value; // Returns decoded value (array, object, or string)
```

## Usage Examples [​](https://dev.fluentcart.com/database/models/product-meta\#usage-examples)

### Get Product Meta [​](https://dev.fluentcart.com/database/models/product-meta\#get-product-meta)

php

```
$productMeta = FluentCart\App\Models\ProductMeta::where('object_type', 'product')
    ->where('object_id', 123)
    ->get();

foreach ($productMeta as $meta) {
    echo "Key: " . $meta->meta_key;
    echo "Value: " . print_r($meta->meta_value, true);
}
```

### Create Product Meta [​](https://dev.fluentcart.com/database/models/product-meta\#create-product-meta)

php

```
$productMeta = FluentCart\App\Models\ProductMeta::create([\
    'object_id' => 123,\
    'object_type' => 'product',\
    'meta_key' => 'custom_field',\
    'meta_value' => 'custom_value'\
]);
```

### Store Complex Product Data [​](https://dev.fluentcart.com/database/models/product-meta\#store-complex-product-data)

php

```
$productMeta = FluentCart\App\Models\ProductMeta::create([\
    'object_id' => 123,\
    'object_type' => 'variation',\
    'meta_key' => 'product_options',\
    'meta_value' => [\
        'color' => 'red',\
        'size' => 'large',\
        'customizations' => ['engraving' => 'Happy Birthday']\
    ]\
]);
```

### Get Meta by Key [​](https://dev.fluentcart.com/database/models/product-meta\#get-meta-by-key)

php

```
$meta = FluentCart\App\Models\ProductMeta::where('object_type', 'product')
    ->where('object_id', 123)
    ->where('meta_key', 'product_thumbnail')
    ->first();

if ($meta) {
    echo "Thumbnail: " . $meta->meta_value;
}
```

### Update Meta Value [​](https://dev.fluentcart.com/database/models/product-meta\#update-meta-value)

php

```
$meta = FluentCart\App\Models\ProductMeta::find(1);
$meta->meta_value = ['updated' => true, 'timestamp' => now()];
$meta->save();
```

### Get All Meta for Product [​](https://dev.fluentcart.com/database/models/product-meta\#get-all-meta-for-product)

php

```
$productMetas = FluentCart\App\Models\ProductMeta::where('object_type', 'product')
    ->where('object_id', 123)
    ->get();
```

### Get Meta for Variation [​](https://dev.fluentcart.com/database/models/product-meta\#get-meta-for-variation)

php

```
$variationMetas = FluentCart\App\Models\ProductMeta::where('object_type', 'variation')
    ->where('object_id', 456)
    ->get();
```

* * *

Today

Hi! I’m your AI assistant. How can I assist you today?

Just now

Powered by **FluentBot**


---

---

