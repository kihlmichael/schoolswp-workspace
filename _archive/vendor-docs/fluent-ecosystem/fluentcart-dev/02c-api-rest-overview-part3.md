# FluentCart Developer Docs - REST API Overview (Part 3/4)

Overview de l'API REST FluentCart : authentification, orders, products, customers, subscriptions, licensing, order-bump, roles & permissions.

---

## Products API | FluentCart Developer Docs

**URL** : https://dev.fluentcart.com/api/products

[Skip to content](https://dev.fluentcart.com/api/products#VPContent)

# Products API [​](https://dev.fluentcart.com/api/products\#products-api)

The Products API provides comprehensive endpoints for managing products in FluentCart. This includes creating, reading, updating, and deleting products, as well as managing product variations, attributes, and integrations.

## Base URL [​](https://dev.fluentcart.com/api/products\#base-url)

```
https://yoursite.com/wp-json/fluent-cart/v2/products
```

## Authentication [​](https://dev.fluentcart.com/api/products\#authentication)

All endpoints require authentication and appropriate permissions:

- **Authentication**: WordPress Application Password or Cookie

## List Products [​](https://dev.fluentcart.com/api/products\#list-products)

**GET**`/products`

Retrieve a paginated list of products with optional filtering and searching.

### Parameters [​](https://dev.fluentcart.com/api/products\#parameters)

| Parameter | Type | Description | Default |
| --- | --- | --- | --- |
| `filter_type` | string | Product filter type (simple/advanced) | simple |
| `per_page` | integer | Number of products per page | 10 |
| `page` | integer | Current page number | 1 |
| `sort_by` | string | Field to sort products by | ID |
| `sort_type` | string | Sort order (ASC/DESC) | DESC |
| `with[]` | array | Related data to include (e.g., detail, variants). **➕ show options**: <br>- `detail` - include the product detail object<br>- `detail.variants.media` - include variant media nested under product detail<br>- `variants:post_id,available` - include variants but only with the `post_id` and `available` fields<br>- `categories` - include product categories<br>**Example:**`?with[]=detail&with[]=detail.variants.media&with[]=variants:post_id,available&with[]=categories` | - |
| `search` | string | Search keyword | - |
| `active_view` | string | Current active view or context. **➕ options**: <br>- `draft` - draft products<br>- `physical` - physical product view<br>- `publish` - published products<br>- `digital` - digital product view<br>- `subscribable` - subscription-capable products<br>**Example:**`active_view=draft` | all |
| `user_tz` | string | User’s timezone for GMT conversion | Asia/Dhaka |
| `advanced_filters` | json | Advanced relation-based filters. Provide an array of rule objects (see example below). | - |

> `advanced_filters` expects an array of rule-groups. Each inner array is a group of rules combined with AND. Multiple groups are combined with OR.
>
> Example boolean interpretation:
>
> ` [[A, B], [C]] -> (A AND B) OR (C)`

### Search by Name [​](https://dev.fluentcart.com/api/products\#search-by-name)

Use the `search` query parameter to match product title/content. This is the simplest way to find products by name.

Example:

`GET /wp-json/fluent-cart/v2/products?search=zipper+hoodie`

(Use `advanced_filters` only when you need relation-based rules; name search is simpler via `search`.)

### Search by Order Count [​](https://dev.fluentcart.com/api/products\#search-by-order-count)

Find products based on related order items count or presence.

Payload example (single rule group - AND group with one rule):

json

```
[\
  [\
    {\
      "source": ["order","has"],\
      "filter_type": "relation",\
      "relation": "orderItems",\
      "operator": "!=",\
      "value": 1\
    }\
  ]\
]
```

UI mapping: Order Count -> `source[0] = "order"`, `relation = "orderItems"`, operators map from UI labels (e.g. "Doesn't equal" -> `!=`).

### Search by Variation Count [​](https://dev.fluentcart.com/api/products\#search-by-variation-count)

Find products by number of variants.

Example: products with less than 1 variant

json

```
[\
  [\
    {\
      "source": ["variations","has"],\
      "filter_type": "relation",\
      "relation": "variants",\
      "operator": "<",\
      "value": 1\
    }\
  ]\
]
```

### Search by Variant ID [​](https://dev.fluentcart.com/api/products\#search-by-variant-id)

Check if a product's variants include a specific variation item (by ID).

Example: variation items includes ID 185

json

```
{
  "filter_type": "advanced",
  "advanced_filters": [\
    [\
      {\
        "source": ["variations", "variation_items"],\
        "filter_type": "relation",\
        "operator": "contains",\
        "value": [185],\
        "column": "id",\
        "relation": "variants"\
      }\
    ]\
  ]
}
```

### Search by Variation Type [​](https://dev.fluentcart.com/api/products\#search-by-variation-type)

Filter products by variation type field (e.g. `simple`, `simple_variations`).

Example: variation\_type equals "simple"

json

```
[\
  [\
    {\
      "source": ["variations","variation_type"],\
      "filter_type": "relation",\
      "relation": "detail",\
      "column": "variation_type",\
      "operator": "=",\
      "value": "simple"\
    }\
  ]\
]
```

### Search by Categories [​](https://dev.fluentcart.com/api/products\#search-by-categories)

Check product membership in product categories (use term IDs).

Example: product in category ID 2

json

```
[\
  [\
    {\
      "source": ["taxonomy","product-categories"],\
      "filter_type": "relation",\
      "relation": "wpTerms",\
      "column": "term_id",\
      "operator": "contains",\
      "value": [2]\
    }\
  ]\
]
```

### Combining multiple rules (AND / OR) [​](https://dev.fluentcart.com/api/products\#combining-multiple-rules-and-or)

Rules are grouped into inner arrays (AND) and the top-level array groups those with OR. Use multiple rules inside an inner array to require all of them (AND). Use multiple inner arrays to create alternative groups (OR).

Simple example: (A AND B) OR C

json

```
[\
  [ A, B ],\
  [ C ]\
]
```

Real example (two groups - shown as OR):

json

```
[\
  [\
    {"source":["order","has"],"filter_type":"relation","operator":"!=","value":1,"relation":"orderItems"},\
    {"source":["variations","has"],"filter_type":"relation","operator":"<","value":1,"relation":"variants"}\
  ],\
  [\
    {"source":["taxonomy","product-categories"],"filter_type":"relation","operator":"contains","value":[2],"column":"term_id","relation":"wpTerms"}\
  ]\
]
```

Operator quick mapping (UI → payload): Doesn't equal=`!=`, Less Than=`<`, Greater Than=`>`, Is=`=`, Includes=`contains`.

#### Response [​](https://dev.fluentcart.com/api/products\#response)

json

```
{
  "products": {
    "current_page": 1,
    "data": [\
      {\
        "ID": 74,\
        "post_author": "1",\
        "post_date": "2025-09-24 05:12:35",\
        "post_date_gmt": "2025-09-24 05:12:35",\
        "post_content": "This stylish zipper hoodie is designed for versatility and comfort. Featuring a full-length zipper, it is easy to layer over t-shirts or under coats during cooler months. The hood offers added warmth, while the lightweight yet durable material ensures long-lasting wear. Ideal for casual outings, gym sessions, or simply lounging around, this hoodie provides a modern twist to the classic design.",\
        "post_title": "Zipper Hoodie",\
        "post_excerpt": "A stylish zipper hoodie with modern detailing, perfect for casual wear and layering during cooler months.",\
        "post_status": "publish",\
        "comment_status": "open",\
        "ping_status": "closed",\
        "post_password": "",\
        "post_name": "zipper-hoodie-24-09-2025-05:12:35",\
        "to_ping": "",\
        "pinged": "",\
        "post_modified": "2025-09-24 05:12:35",\
        "post_modified_gmt": "2025-09-24 05:12:35",\
        "post_content_filtered": "",\
        "post_parent": "0",\
        "guid": "https://yoursite.com/?items=zipper-hoodie-24-09-2025-05:12:35",\
        "menu_order": "0",\
        "post_type": "fluent-products",\
        "post_mime_type": "",\
        "comment_count": "0",\
        "view_url": "https://yoursite.com/item/zipper-hoodie-24-09-2025-05:12:35/",\
        "edit_url": "https://yoursite.com/wp-admin/post.php?post=74&action=edit"\
      }\
    ],
    "first_page_url": "https://yoursite.com/wp-json/fluent-cart/v2/products/?page=1",
    "from": 1,
    "last_page": 10,
    "last_page_url": "https://yoursite.com/wp-json/fluent-cart/v2/products/?page=10",
    "links": [\
      {\
        "url": null,\
        "label": "pagination.previous",\
        "active": false\
      },\
      {\
        "url": "https://yoursite.com/wp-json/fluent-cart/v2/products/?page=1",\
        "label": "1",\
        "active": true\
      },\
      {\
        "url": "https://yoursite.com/wp-json/fluent-cart/v2/products/?page=2",\
        "label": "2",\
        "active": false\
      }\
    ],
    "next_page_url": "https://yoursite.com/wp-json/fluent-cart/v2/products/?page=2",
    "path": "https://yoursite.com/wp-json/fluent-cart/v2/products",
    "per_page": 1,
    "prev_page_url": null,
    "to": 1,
    "total": 10
  }
}
```

## Product Details [​](https://dev.fluentcart.com/api/products\#product-details)

json

```
{
    "product": {
        "ID": 7529385,
        "post_author": "5",
        "post_date": "2025-10-11 11:50:31",
        "post_date_gmt": "2025-10-11 11:50:31",
        "post_content": "",
        "post_title": "Sample Digital Product",
        "post_excerpt": "",
        "post_status": "draft",
        "comment_status": "closed",
        "ping_status": "closed",
        "post_password": "",
        "post_name": "sample-digital-product",
        "to_ping": "",
        "pinged": "",
        "post_modified": "2025-10-11 11:50:31",
        "post_modified_gmt": "2025-10-11 11:50:31",
        "post_content_filtered": "",
        "post_parent": "0",
        "guid": "https://cart.junior.ninja/?post_type=fluent-products&#038;p=7529385",
        "menu_order": "0",
        "post_type": "fluent-products",
        "post_mime_type": "",
        "comment_count": "0",
        "thumbnail": "https://cart.junior.ninja/wp-content/uploads/2025/06/white-navy-athletic-shoe-2.jpeg",
        "detail": {
            "id": 52,
            "post_id": 7529385,
            "fulfillment_type": "digital",
            "min_price": 2000,
            "max_price": 3000,
            "default_variation_id": "0",
            "default_media": null,
            "manage_stock": "1",
            "stock_availability": "in-stock",
            "variation_type": "simple_variations",
            "manage_downloadable": "1",
            "other_info": {
                "tax_class": null,
                "active_editor": null,
                "shipping_class": 3,
                "group_pricing_by": "payment_type",
                "sold_individually": "no",
                "use_pricing_table": "no"
            },
            "created_at": "2025-10-11T11:39:14+00:00",
            "updated_at": "2025-10-11T11:50:31+00:00",
            "featured_media": {
                "id": 7529266,
                "url": "https://cart.junior.ninja/wp-content/uploads/2025/06/white-navy-athletic-shoe-2.jpeg",
                "title": "white-navy-athletic-shoe-2"
            },
            "formatted_min_price": "&#36;20.00",
            "formatted_max_price": "&#36;30.00",
            "gallery_image": {
                "meta_id": "703",
                "post_id": 7529385,
                "meta_key": "fluent-products-gallery-image",
                "meta_value": [\
                    {\
                        "id": 7529266,\
                        "url": "https://cart.junior.ninja/wp-content/uploads/2025/06/white-navy-athletic-shoe-2.jpeg",\
                        "title": "white-navy-athletic-shoe-2"\
                    },\
                    {\
                        "id": 7529265,\
                        "url": "https://cart.junior.ninja/wp-content/uploads/2025/06/white-navy-athletic-shoe-1.jpeg",\
                        "title": "white-navy-athletic-shoe-1"\
                    },\
                    {\
                        "id": 7529260,\
                        "url": "https://cart.junior.ninja/wp-content/uploads/2025/06/unnamed-5.png",\
                        "title": "unnamed (5)"\
                    }\
                ]
            }
        }
    }
}
```

## Create Product [​](https://dev.fluentcart.com/api/products\#create-product)

**POST**`/products`

Create a new product.

#### Parameters [​](https://dev.fluentcart.com/api/products\#parameters-1)

When creating a product, the following parameters can be pass:

| Parameter | Type | Description | Required |
| --- | --- | --- | --- |
| `post_title` | string | Product title | Yes |
| `post_status` | string | Post status (e.g. `draft`, `publish`) | No (default: `draft`) |
| `detail.fulfillment_type` | string | Fulfillment type for the product (e.g. `digital`, `physical`) | Yes |

#### Request Body [​](https://dev.fluentcart.com/api/products\#request-body)

json

```
{
  "post_title": "Dynamic Product",
  "post_status": "draft",
  "detail": {
    "fulfillment_type": "digital",
  }
}
```

### Create Product Pricing (need update) [​](https://dev.fluentcart.com/api/products\#create-product-pricing-need-update)

### Get Product Details [​](https://dev.fluentcart.com/api/products\#get-product-details)

**GET**`/products/{product}`

Retrieve detailed information about a specific product.

#### Parameters [​](https://dev.fluentcart.com/api/products\#parameters-2)

| Parameter | Type | Description |
| --- | --- | --- |
| `product` | integer | Product ID |

#### Response [​](https://dev.fluentcart.com/api/products\#response-1)

json

```
{
  "success": true,
  "data": {
    "product": {
      "id": 33,
      "post_id": 7529108,
      "variations": [\
        {\
          "id": 145,\
          "post_id": 7529108,\
          "serial_index": 6,\
          "sold_individually": 0,\
          "variation_title": "Unlimited Sites Lifetime License",\
          "variation_identifier": "6",\
          "manage_stock": "0",\
          "payment_type": "onetime",\
          "stock_status": "in-stock",\
          "backorders": 0,\
          "total_stock": 0,\
          "on_hold": 0,\
          "committed": 0,\
          "available": 0,\
          "fulfillment_type": "digital",\
          "item_status": "active",\
          "manage_cost": "false",\
          "item_price": 129900,\
          "item_cost": 0,\
          "compare_price": 0,\
          "shipping_class": "0",\
          "other_info": {\
            "payment_type": "onetime"\
          },\
          "downloadable": "1",\
          "created_at": "2021-09-22T07:09:20+00:00",\
          "updated_at": "2025-06-06T14:36:34+00:00",\
          "thumbnail": null,\
          "formatted_total": "&#36;1,299.00",\
          "media": null\
        }\
      ],
      "detail": {
        "id": 33,
        "post_id": 7529108,
        "fulfillment_type": "digital",
        "min_price": 8900,
        "max_price": 129900,
        "default_variation_id": "145",
        "default_media": null,
        "manage_stock": "0",
        "stock_availability": "in-stock",
        "variation_type": "simple_variations",
        "manage_downloadable": "1",
        "other_info": {
          "group_pricing_by": "repeat_interval",
          "use_pricing_table": "yes"
        },
        "created_at": "2021-09-22T07:09:20+00:00",
        "updated_at": "2025-09-24T09:09:50+00:00",
        "featured_media": null,
        "gallery_image": {
          "meta_id": "63",
          "post_id": 7529108,
          "meta_key": "fluent-products-gallery-image",
          "meta_value": []
        }
      }
    }
  }
}
```

#### Error Response [​](https://dev.fluentcart.com/api/products\#error-response)

json

```
{
  "message": "Product not found",
  "data": null
}
```

#### Example Request [​](https://dev.fluentcart.com/api/products\#example-request)

bash

```
curl -X GET "https://yoursite.com/wp-json/fluent-cart/v2/products/33" \
  -H "Authorization: Basic dXNlcm5hbWU6YXBwbGljYXRpb25fcGFzc3dvcmQ="
```

## Update Product [​](https://dev.fluentcart.com/api/products\#update-product)

**PUT**`/products/{postId}/pricing`

Update product pricing information.

#### Parameters [​](https://dev.fluentcart.com/api/products\#parameters-3)

| Parameter | Type | Description |
| --- | --- | --- |
| `postId` | integer | Product ID |

#### Request Body [​](https://dev.fluentcart.com/api/products\#request-body-1)

json

```
{
  "price": 3000,
  "sale_price": 2500,
  "sku": "SP-001-UPDATED"
}
```

#### Response [​](https://dev.fluentcart.com/api/products\#response-2)

json

```
{
  "success": true,
  "data": {
    "product": {
      "id": 1,
      "price": 3000,
      "sale_price": 2500,
      "sku": "SP-001-UPDATED",
      "updated_at": "2024-01-01T11:00:00Z"
    }
  }
}
```

#### Example Request [​](https://dev.fluentcart.com/api/products\#example-request-1)

bash

```
curl -X PUT "https://yoursite.com/wp-json/fluent-cart/v1/products/1/pricing" \
  -H "Authorization: Basic dXNlcm5hbWU6YXBwbGljYXRpb25fcGFzc3dvcmQ=" \
  -H "Content-Type: application/json" \
  -d '{
    "price": 3000,
    "sale_price": 2500
  }'
```

## Delete Product [​](https://dev.fluentcart.com/api/products\#delete-product)

**DELETE**`/products/{product}`

Delete a product (soft delete).

#### Parameters [​](https://dev.fluentcart.com/api/products\#parameters-4)

| Parameter | Type | Description |
| --- | --- | --- |
| `product` | integer | Product ID |

#### Response [​](https://dev.fluentcart.com/api/products\#response-3)

json

```
{
  "success": true,
  "message": "Product deleted successfully"
}
```

#### Example Request [​](https://dev.fluentcart.com/api/products\#example-request-2)

bash

```
curl -X DELETE "https://yoursite.com/wp-json/fluent-cart/v1/products/1" \
  -H "Authorization: Basic dXNlcm5hbWU6YXBwbGljYXRpb25fcGFzc3dvcmQ="
```

### Set Product Image [​](https://dev.fluentcart.com/api/products\#set-product-image)

**GET**`/products/{variantId}/thumbnail`

Set product image for a variant.

#### Parameters [​](https://dev.fluentcart.com/api/products\#parameters-5)

| Parameter | Type | Description |
| --- | --- | --- |
| `variantId` | integer | Variant ID |

#### Response [​](https://dev.fluentcart.com/api/products\#response-4)

json

```
{
  "success": true,
  "data": {
    "image": {
      "id": 1,
      "url": "https://example.com/image.jpg",
      "alt": "Product image"
    }
  }
}
```

#### Example Request [​](https://dev.fluentcart.com/api/products\#example-request-3)

bash

```
curl -X GET "https://yoursite.com/wp-json/fluent-cart/v1/products/1/thumbnail" \
  -H "Authorization: Basic dXNlcm5hbWU6YXBwbGljYXRpb25fcGFzc3dvcmQ="
```

### Update Variant Option [​](https://dev.fluentcart.com/api/products\#update-variant-option)

**POST**`/products/{postId}/update-variant-option`

Update a product variant option.

#### Parameters [​](https://dev.fluentcart.com/api/products\#parameters-6)

| Parameter | Type | Description |
| --- | --- | --- |
| `postId` | integer | Product ID |

#### Request Body [​](https://dev.fluentcart.com/api/products\#request-body-2)

json

```
{
  "variant_id": 1,
  "option_name": "Size",
  "option_value": "Large"
}
```

#### Response [​](https://dev.fluentcart.com/api/products\#response-5)

json

```
{
  "success": true,
  "data": {
    "variant": {
      "id": 1,
      "options": {
        "Size": "Large"
      },
      "updated_at": "2024-01-01T11:00:00Z"
    }
  }
}
```

#### Example Request [​](https://dev.fluentcart.com/api/products\#example-request-4)

bash

```
curl -X POST "https://yoursite.com/wp-json/fluent-cart/v1/products/1/update-variant-option" \
  -H "Authorization: Basic dXNlcm5hbWU6YXBwbGljYXRpb25fcGFzc3dvcmQ=" \
  -H "Content-Type: application/json" \
  -d '{
    "variant_id": 1,
    "option_name": "Size",
    "option_value": "Large"
  }'
```

### Add Product Terms [​](https://dev.fluentcart.com/api/products\#add-product-terms)

**POST**`/products/add-product-terms`

Add terms (categories, tags) to a product.

#### Request Body [​](https://dev.fluentcart.com/api/products\#request-body-3)

json

```
{
  "product_id": 1,
  "terms": [\
    {\
      "taxonomy": "product_category",\
      "term_id": 1\
    },\
    {\
      "taxonomy": "product_tag",\
      "term_id": 2\
    }\
  ]
}
```

#### Response [​](https://dev.fluentcart.com/api/products\#response-6)

json

```
{
  "success": true,
  "data": {
    "product": {
      "id": 1,
      "terms": [\
        {\
          "taxonomy": "product_category",\
          "term_id": 1\
        },\
        {\
          "taxonomy": "product_tag",\
          "term_id": 2\
        }\
      ]
    }
  }
}
```

#### Example Request [​](https://dev.fluentcart.com/api/products\#example-request-5)

bash

```
curl -X POST "https://yoursite.com/wp-json/fluent-cart/v1/products/add-product-terms" \
  -H "Authorization: Basic dXNlcm5hbWU6YXBwbGljYXRpb25fcGFzc3dvcmQ=" \
  -H "Content-Type: application/json" \
  -d '{
    "product_id": 1,
    "terms": [\
      {\
        "taxonomy": "product_category",\
        "term_id": 1\
      }\
    ]
  }'
```

### Bulk Actions [​](https://dev.fluentcart.com/api/products\#bulk-actions)

**POST**`/products/do-bulk-action`

Perform bulk actions on multiple products.

#### Request Body [​](https://dev.fluentcart.com/api/products\#request-body-4)

json

```
{
  "action": "update_status",
  "product_ids": [1, 2, 3],
  "data": {
    "status": "draft"
  }
}
```

#### Available Actions [​](https://dev.fluentcart.com/api/products\#available-actions)

- `update_status` \- Update status of multiple products
- `delete` \- Delete multiple products
- `export` \- Export multiple products

#### Response [​](https://dev.fluentcart.com/api/products\#response-7)

json

```
{
  "success": true,
  "data": {
    "processed": 3,
    "failed": 0,
    "results": [\
      {\
        "product_id": 1,\
        "success": true\
      },\
      {\
        "product_id": 2,\
        "success": true\
      },\
      {\
        "product_id": 3,\
        "success": true\
      }\
    ]
  }
}
```

#### Example Request [​](https://dev.fluentcart.com/api/products\#example-request-6)

bash

```
curl -X POST "https://yoursite.com/wp-json/fluent-cart/v1/products/do-bulk-action" \
  -H "Authorization: Basic dXNlcm5hbWU6YXBwbGljYXRpb25fcGFzc3dvcmQ=" \
  -H "Content-Type: application/json" \
  -d '{
    "action": "update_status",
    "product_ids": [1, 2, 3],
    "data": {
      "status": "draft"
    }
  }'
```

## Product Variations [​](https://dev.fluentcart.com/api/products\#product-variations)

### List Variations [​](https://dev.fluentcart.com/api/products\#list-variations)

**GET**`/products/variants`

List all product variations.

#### Response [​](https://dev.fluentcart.com/api/products\#response-8)

json

```
{
  "success": true,
  "data": {
    "variations": [\
      {\
        "id": 1,\
        "product_id": 1,\
        "title": "Small",\
        "price": 2000,\
        "sku": "SP-001-S",\
        "stock_quantity": 50\
      }\
    ]
  }
}
```

#### Example Request [​](https://dev.fluentcart.com/api/products\#example-request-7)

bash

```
curl -X GET "https://yoursite.com/wp-json/fluent-cart/v1/products/variants" \
  -H "Authorization: Basic dXNlcm5hbWU6YXBwbGljYXRpb25fcGFzc3dvcmQ="
```

### Create Variation [​](https://dev.fluentcart.com/api/products\#create-variation)

**POST**`/products/variants`

Create a new product variation.

#### Request Body [​](https://dev.fluentcart.com/api/products\#request-body-5)

json

```
{
  "product_id": 1,
  "title": "Large",
  "price": 3000,
  "sku": "SP-001-L",
  "stock_quantity": 25,
  "options": {
    "Size": "Large",
    "Color": "Red"
  }
}
```

#### Response [​](https://dev.fluentcart.com/api/products\#response-9)

json

```
{
  "success": true,
  "data": {
    "variation": {
      "id": 2,
      "product_id": 1,
      "title": "Large",
      "price": 3000,
      "sku": "SP-001-L",
      "stock_quantity": 25,
      "created_at": "2024-01-01T10:00:00Z"
    }
  }
}
```

#### Example Request [​](https://dev.fluentcart.com/api/products\#example-request-8)

bash

```
curl -X POST "https://yoursite.com/wp-json/fluent-cart/v1/products/variants" \
  -H "Authorization: Basic dXNlcm5hbWU6YXBwbGljYXRpb25fcGFzc3dvcmQ=" \
  -H "Content-Type: application/json" \
  -d '{
    "product_id": 1,
    "title": "Large",
    "price": 3000,
    "sku": "SP-001-L"
  }'
```

## Rate Limiting [​](https://dev.fluentcart.com/api/products\#rate-limiting)

- **List operations**: 100 requests per hour
- **Create operations**: 50 requests per hour
- **Update operations**: 200 requests per hour
- **Delete operations**: 20 requests per hour

## Related Documentation [​](https://dev.fluentcart.com/api/products\#related-documentation)

- [Orders API](https://dev.fluentcart.com/api/orders.html) \- Order management endpoints
- [Customers API](https://dev.fluentcart.com/api/customers.html) \- Customer management endpoints
- [Database Models](https://dev.fluentcart.com/database/models.html) \- Product data models
- [Developer Hooks](https://dev.fluentcart.com/hooks/) \- Product-related hooks

Today

Hi! I’m your AI assistant. How can I assist you today?

Just now

Powered by **FluentBot**


---

---

## Roles & Permissions API (Pro) | FluentCart Developer Docs

**URL** : https://dev.fluentcart.com/api/roles-permissions

[Skip to content](https://dev.fluentcart.com/api/roles-permissions#VPContent)

# Roles & Permissions API (Pro) [​](https://dev.fluentcart.com/api/roles-permissions\#roles-permissions-api-pro)

The Roles & Permissions API allows you to manage user roles and capabilities within FluentCart Pro, enabling fine-grained access control for shop managers and other personnel.

## Base URL [​](https://dev.fluentcart.com/api/roles-permissions\#base-url)

All Roles & Permissions API endpoints are prefixed with the same base URL as the core API:

```
/wp-json/fluent-cart/v2/
```

## Authentication [​](https://dev.fluentcart.com/api/roles-permissions\#authentication)

All Roles & Permissions API endpoints require authentication with the `manage_fluent_cart_settings` capability.

## Role Management [​](https://dev.fluentcart.com/api/roles-permissions\#role-management)

### 1\. Get All Roles [​](https://dev.fluentcart.com/api/roles-permissions\#_1-get-all-roles)

Retrieve a list of all available FluentCart roles.

- **Endpoint:**`GET /wp-json/fluent-cart/v2/roles`
- **Authentication:** Requires `RolePolicy` permission.
- **Parameters:** None

**Example Request:**

bash

```
curl -X GET "http://localhost/wp-json/fluent-cart/v2/roles" \
-H "Authorization: Basic [YOUR_BASE64_ENCODED_CREDENTIALS]"
```

### 2\. Get Role Managers [​](https://dev.fluentcart.com/api/roles-permissions\#_2-get-role-managers)

Retrieve a list of users who can manage roles.

- **Endpoint:**`GET /wp-json/fluent-cart/v2/roles/managers`
- **Authentication:** Requires `RolePolicy` permission.
- **Parameters:** None

### 3\. Get User List [​](https://dev.fluentcart.com/api/roles-permissions\#_3-get-user-list)

Retrieve a list of users for role assignment.

- **Endpoint:**`GET /wp-json/fluent-cart/v2/roles/user-list`
- **Authentication:** Requires `RolePolicy` permission.
- **Parameters:** None

### 4\. Create Role [​](https://dev.fluentcart.com/api/roles-permissions\#_4-create-role)

Create a new custom role.

- **Endpoint:**`POST /wp-json/fluent-cart/v2/roles`
- **Authentication:** Requires `RolePolicy` permission.
- **Parameters:**
  - `title` (string, required): Role title
  - `description` (string, optional): Role description
  - `capabilities` (array, required): Array of capabilities

**Example Request:**

bash

```
curl -X POST "http://localhost/wp-json/fluent-cart/v2/roles" \
-H "Authorization: Basic [YOUR_BASE64_ENCODED_CREDENTIALS]" \
-H "Content-Type: application/json" \
-d '{
  "title": "Product Manager",
  "description": "Manages products and inventory",
  "capabilities": ["products/view", "products/manage"]
}'
```

### 5\. Get Role Details [​](https://dev.fluentcart.com/api/roles-permissions\#_5-get-role-details)

Retrieve details for a specific role.

- **Endpoint:**`GET /wp-json/fluent-cart/v2/roles/{key}`
- **Authentication:** Requires `RolePolicy` permission.
- **Parameters:**
  - `key` (string, required): Role key/identifier

### 6\. Update Role [​](https://dev.fluentcart.com/api/roles-permissions\#_6-update-role)

Update an existing role.

- **Endpoint:**`POST /wp-json/fluent-cart/v2/roles/{key}`
- **Authentication:** Requires `RolePolicy` permission.
- **Parameters:**
  - `key` (string, required): Role key/identifier
  - `title` (string, optional): Role title
  - `description` (string, optional): Role description
  - `capabilities` (array, optional): Array of capabilities

### 7\. Delete Role [​](https://dev.fluentcart.com/api/roles-permissions\#_7-delete-role)

Delete a custom role.

- **Endpoint:**`DELETE /wp-json/fluent-cart/v2/roles/{key}`
- **Authentication:** Requires `RolePolicy` permission.
- **Parameters:**
  - `key` (string, required): Role key/identifier

**Example Response:**

json

```
{
  "message": "Roles retrieved successfully",
  "roles": [\
    {\
      "title": "Shop Manager",\
      "description": "Manages all aspects of the shop, including products, orders, and customers."\
    },\
    {\
      "title": "Product Manager",\
      "description": "Manages products and inventory."\
    },\
    {\
      "title": "Order Manager",\
      "description": "Manages customer orders and fulfillment."\
    }\
  ]
}
```

### 2\. Assign Role to User [​](https://dev.fluentcart.com/api/roles-permissions\#_2-assign-role-to-user)

Assign a specific FluentCart role to a user.

- **Endpoint:**`POST /wp-json/fluent-cart/v2/roles`
- **Authentication:** Requires `manage_fluent_cart_settings` capability.
- **Parameters:**
  - `user_id` (int, required): The ID of the user.
  - `role_key` (string, required): The key of the role to assign (e.g., `shop_manager`, `product_manager`).

**Example Request:**

bash

```
curl -X POST "http://localhost/wp-json/fluent-cart/v2/roles" \
-H "Content-Type: application/json" \
-H "Authorization: Basic [YOUR_BASE64_ENCODED_CREDENTIALS]" \
-d '{
  "user_id": 1,
  "role_key": "shop_manager"
}'
```

**Example Response (Success):**

json

```
{
  "message": "Role synced successfully",
  "is_updated": true
}
```

**Example Response (Error - User Not Found):**

json

```
{
  "message": "User not found",
  "errors": [\
    {\
      "code": 404,\
      "message": "User not found"\
    }\
  ]
}
```

### 3\. Remove Role from User [​](https://dev.fluentcart.com/api/roles-permissions\#_3-remove-role-from-user)

Remove a specific FluentCart role from a user.

- **Endpoint:**`DELETE /wp-json/fluent-cart/v2/roles/{key}`
- **Authentication:** Requires `manage_fluent_cart_settings` capability.
- **Parameters:**
  - `key` (string, required): The key of the role to remove.
  - `user_id` (int, required): The ID of the user.

**Example Request:**

bash

```
curl -X DELETE "http://localhost/wp-json/fluent-cart/v2/roles/shop_manager" \
-H "Content-Type: application/json" \
-H "Authorization: Basic [YOUR_BASE64_ENCODED_CREDENTIALS]" \
-d '{
  "user_id": 1
}'
```

**Example Response (Success):**

json

```
{
  "message": "Role deleted successfully"
}
```

### 4\. Get Users with Shop Role (Managers) [​](https://dev.fluentcart.com/api/roles-permissions\#_4-get-users-with-shop-role-managers)

Retrieve a list of users who have a shop management role.

- **Endpoint:**`GET /wp-json/fluent-cart/v2/roles/managers`
- **Authentication:** Requires `manage_fluent_cart_settings` capability.
- **Parameters:** None

**Example Request:**

bash

```
curl -X GET "http://localhost/wp-json/fluent-cart/v2/roles/managers" \
-H "Authorization: Basic [YOUR_BASE64_ENCODED_CREDENTIALS]"
```

**Example Response:**

json

```
{
  "message": "Managers retrieved successfully",
  "managers": [\
    {\
      "ID": 1,\
      "display_name": "Admin User",\
      "user_email": "admin@example.com"\
    },\
    {\
      "ID": 5,\
      "display_name": "Shop Manager John",\
      "user_email": "john@example.com"\
    }\
  ]
}
```

### 5\. Get User List (for Role Assignment) [​](https://dev.fluentcart.com/api/roles-permissions\#_5-get-user-list-for-role-assignment)

Retrieve a paginated list of users, optionally filtered by search terms or IDs, excluding those with admin roles. This is useful for selecting users to assign roles to.

- **Endpoint:**`GET /wp-json/fluent-cart/v2/roles/user-list`
- **Authentication:** Requires `manage_fluent_cart_settings` capability.
- **Parameters:**
  - `search` (string, optional): Search term for display name or email.
  - `user_ids` (array\|string, optional): Comma-separated list of user IDs.
  - `per_page` (int, optional): Number of users per page (default: 10).
  - `page` (int, optional): Current page number (default: 1).

**Example Request (Search by email):**

bash

```
curl -X GET "http://localhost/wp-json/fluent-cart/v2/roles/user-list?search=john@example.com" \
-H "Authorization: Basic [YOUR_BASE64_ENCODED_CREDENTIALS]"
```

**Example Response:**

json

```
{
  "message": "Users retrieved successfully",
  "users": {
    "data": [\
      {\
        "ID": 5,\
        "name": "John Doe",\
        "email": "john@example.com"\
      }\
    ],
    "total": 1,
    "per_page": 10,
    "current_page": 1,
    "last_page": 1
  }
}
```

## Permission Management [​](https://dev.fluentcart.com/api/roles-permissions\#permission-management)

### Available Roles [​](https://dev.fluentcart.com/api/roles-permissions\#available-roles)

#### Shop Manager [​](https://dev.fluentcart.com/api/roles-permissions\#shop-manager)

- **Capabilities:** Full access to all FluentCart features
- **Description:** Manages all aspects of the shop, including products, orders, and customers.

#### Product Manager [​](https://dev.fluentcart.com/api/roles-permissions\#product-manager)

- **Capabilities:** Product management, inventory control
- **Description:** Manages products and inventory.

#### Order Manager [​](https://dev.fluentcart.com/api/roles-permissions\#order-manager)

- **Capabilities:** Order management, customer service
- **Description:** Manages customer orders and fulfillment.

#### Customer Service [​](https://dev.fluentcart.com/api/roles-permissions\#customer-service)

- **Capabilities:** Customer support, order assistance
- **Description:** Provides customer support and order assistance.

### Role Assignment [​](https://dev.fluentcart.com/api/roles-permissions\#role-assignment)

php

```
use FluentCart\App\Services\Permission\PermissionManager;

// Assign role to user
$isUpdated = PermissionManager::attachRole($userId, $roleKey);

if ($isUpdated instanceof \WP_Error) {
    echo "Error: " . $isUpdated->get_error_message();
} else {
    echo "Role assigned successfully";
}

// Remove role from user
$isUpdated = PermissionManager::detachRole($userId, $roleKey);

if ($isUpdated instanceof \WP_Error) {
    echo "Error: " . $isUpdated->get_error_message();
} else {
    echo "Role removed successfully";
}
```

### Get Users with Shop Roles [​](https://dev.fluentcart.com/api/roles-permissions\#get-users-with-shop-roles)

php

```
// Get all users with shop management roles
$managers = PermissionManager::getUsersWithShopRole();

foreach ($managers as $manager) {
    echo "Manager: " . $manager->display_name . " (" . $manager->user_email . ")\n";
}
```

## Role Hooks and Filters [​](https://dev.fluentcart.com/api/roles-permissions\#role-hooks-and-filters)

### Role Assignment Hooks [​](https://dev.fluentcart.com/api/roles-permissions\#role-assignment-hooks)

php

```
// Before role assignment
add_action('fluent_cart/role/before_assign', function($userId, $roleKey) {
    // Custom validation before assigning role
    if ($this->userHasConflictingRole($userId, $roleKey)) {
        return new \WP_Error('conflicting_role', 'User already has a conflicting role');
    }
}, 10, 2);

// After role assignment
add_action('fluent_cart/role/assigned', function($userId, $roleKey) {
    // Update user capabilities
    update_user_capabilities($userId, $roleKey);

    // Send role assignment notification
    wp_mail(
        get_userdata($userId)->user_email,
        'Role Assigned',
        "You have been assigned the role: {$roleKey}"
    );

    // Log role assignment
    error_log("Role assigned: {$roleKey} to user {$userId}");
}, 10, 2);

// Before role removal
add_action('fluent_cart/role/before_remove', function($userId, $roleKey) {
    // Check if user has pending tasks
    if ($this->userHasPendingTasks($userId)) {
        return new \WP_Error('pending_tasks', 'User has pending tasks that must be completed first');
    }
}, 10, 2);

// After role removal
add_action('fluent_cart/role/removed', function($userId, $roleKey) {
    // Remove user capabilities
    remove_user_capabilities($userId, $roleKey);

    // Log role removal
    error_log("Role removed: {$roleKey} from user {$userId}");

    // Notify administrators
    wp_mail(
        get_option('admin_email'),
        'Role Removed',
        "Role {$roleKey} has been removed from user {$userId}"
    );
}, 10, 2);
```

### Role Filters [​](https://dev.fluentcart.com/api/roles-permissions\#role-filters)

php

```
// Modify available roles
add_filter('fluent_cart/roles/available', function($roles) {
    // Add custom role
    $roles['custom_manager'] = [\
        'title' => 'Custom Manager',\
        'description' => 'Custom management role with specific capabilities',\
        'capabilities' => ['custom_capability_1', 'custom_capability_2']\
    ];

    return $roles;
});

// Modify role capabilities
add_filter('fluent_cart/role/capabilities', function($capabilities, $roleKey) {
    if ($roleKey === 'shop_manager') {
        // Add custom capability to shop manager
        $capabilities[] = 'custom_shop_capability';
    }

    return $capabilities;
}, 10, 2);

// Modify user list for role assignment
add_filter('fluent_cart/roles/user_list', function($users, $args) {
    // Filter out users who shouldn't be assigned roles
    return $users->filter(function($user) {
        return !$this->userIsExcluded($user->ID);
    });
}, 10, 2);
```

## Custom Role Development [​](https://dev.fluentcart.com/api/roles-permissions\#custom-role-development)

### Creating Custom Roles [​](https://dev.fluentcart.com/api/roles-permissions\#creating-custom-roles)

php

```
// Register custom role
add_action('fluent_cart/roles/register', function() {
    $customRole = new CustomRole();
    $customRole->register();
});

class CustomRole
{
    public function register()
    {
        // Define custom role
        $roleData = [\
            'title' => 'Custom Manager',\
            'description' => 'Custom management role with specific capabilities',\
            'capabilities' => [\
                'manage_products',\
                'view_orders',\
                'custom_capability'\
            ]\
        ];

        // Register role with PermissionManager
        PermissionManager::registerRole('custom_manager', $roleData);
    }
}
```

### Custom Role Capabilities [​](https://dev.fluentcart.com/api/roles-permissions\#custom-role-capabilities)

php

```
// Add custom capabilities
add_action('fluent_cart/roles/capabilities', function($capabilities) {
    $capabilities['custom_capability'] = [\
        'title' => 'Custom Capability',\
        'description' => 'Allows access to custom functionality'\
    ];

    return $capabilities;
});

// Check custom capability
add_filter('fluent_cart/user/can', function($can, $capability, $userId) {
    if ($capability === 'custom_capability') {
        return $this->userHasCustomCapability($userId);
    }

    return $can;
}, 10, 3);
```

## Error Handling [​](https://dev.fluentcart.com/api/roles-permissions\#error-handling)

### Common Error Responses [​](https://dev.fluentcart.com/api/roles-permissions\#common-error-responses)

#### User Not Found [​](https://dev.fluentcart.com/api/roles-permissions\#user-not-found)

json

```
{
  "message": "User not found",
  "errors": [\
    {\
      "code": 404,\
      "message": "User not found"\
    }\
  ]
}
```

#### Invalid Role [​](https://dev.fluentcart.com/api/roles-permissions\#invalid-role)

json

```
{
  "message": "Invalid role",
  "errors": [\
    {\
      "code": 400,\
      "message": "Invalid role"\
    }\
  ]
}
```

#### Permission Denied [​](https://dev.fluentcart.com/api/roles-permissions\#permission-denied)

json

```
{
  "message": "Permission denied",
  "errors": [\
    {\
      "code": 403,\
      "message": "Permission denied"\
    }\
  ]
}
```

#### Role Already Assigned [​](https://dev.fluentcart.com/api/roles-permissions\#role-already-assigned)

json

```
{
  "message": "Role already assigned",
  "errors": [\
    {\
      "code": 409,\
      "message": "Role already assigned"\
    }\
  ]
}
```

* * *

**Related Documentation:**

- [Licensing API](https://dev.fluentcart.com/api/licensing.html) \- Software license management
- [Order Bump API](https://dev.fluentcart.com/api/order-bump.html) \- Promotional features
- [REST API Overview](https://dev.fluentcart.com/api/) \- General API information

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

## Subscriptions API | FluentCart Developer Docs

**URL** : https://dev.fluentcart.com/api/subscriptions

[Skip to content](https://dev.fluentcart.com/api/subscriptions#VPContent)

# Subscriptions API [​](https://dev.fluentcart.com/api/subscriptions\#subscriptions-api)

The Subscriptions API provides comprehensive endpoints for managing subscriptions in FluentCart. This includes creating, reading, updating, and managing subscription lifecycle operations like cancellation, reactivation, and payment method updates.

## Base URL [​](https://dev.fluentcart.com/api/subscriptions\#base-url)

```
https://yoursite.com/wp-json/fluent-cart/v2/subscriptions
```

## Authentication [​](https://dev.fluentcart.com/api/subscriptions\#authentication)

All endpoints require authentication and appropriate permissions:

- **Authentication**: WordPress Application Password or Cookie
- **Policy**: `SubscriptionsPolicy` (Admin) / `CustomerFrontendPolicy` (Customer)
- **Permissions**: Various subscription-related permissions

## Admin Endpoints [​](https://dev.fluentcart.com/api/subscriptions\#admin-endpoints)

### List Subscriptions [​](https://dev.fluentcart.com/api/subscriptions\#list-subscriptions)

**GET**`/subscriptions`

Retrieve a paginated list of subscriptions with optional filtering and searching.

#### Parameters [​](https://dev.fluentcart.com/api/subscriptions\#parameters)

| Parameter | Type | Description | Default |
| --- | --- | --- | --- |
| `page` | integer | Page number | 1 |
| `per_page` | integer | Items per page (max 100) | 10 |
| `search` | string | Search query | - |
| `filters` | object | Filter options | - |
| `order_by` | string | Sort field | id |
| `order_type` | string | Sort direction (ASC/DESC) | DESC |

#### Filter Options [​](https://dev.fluentcart.com/api/subscriptions\#filter-options)

json

```
{
  "status": "active",
  "customer_id": 123,
  "product_id": 456,
  "date_from": "2024-01-01",
  "date_to": "2024-12-31"
}
```

#### Response [​](https://dev.fluentcart.com/api/subscriptions\#response)

json

```
{
  "success": true,
  "data": {
    "subscriptions": [\
      {\
        "id": 1,\
        "uuid": "sub_abc123",\
        "customer_id": 123,\
        "product_id": 456,\
        "variation_id": 789,\
        "status": "active",\
        "billing_cycle": "monthly",\
        "amount": 2500,\
        "currency": "USD",\
        "next_billing_date": "2024-02-01T00:00:00Z",\
        "created_at": "2024-01-01T10:00:00Z",\
        "customer": {\
          "id": 123,\
          "email": "customer@example.com",\
          "first_name": "John",\
          "last_name": "Doe"\
        },\
        "product": {\
          "id": 456,\
          "title": "Premium Plan",\
          "sku": "PREMIUM-001"\
        }\
      }\
    ],
    "pagination": {
      "current_page": 1,
      "per_page": 10,
      "total": 100,
      "total_pages": 10
    }
  }
}
```

#### Example Request [​](https://dev.fluentcart.com/api/subscriptions\#example-request)

bash

```
curl -X GET "https://yoursite.com/wp-json/fluent-cart/v1/subscriptions?page=1&per_page=20&search=premium" \
  -H "Authorization: Basic dXNlcm5hbWU6YXBwbGljYXRpb25fcGFzc3dvcmQ="
```

### Get Subscription Details [​](https://dev.fluentcart.com/api/subscriptions\#get-subscription-details)

**GET**`/subscriptions/{subscriptionOrderId}`

Retrieve detailed information about a specific subscription.

#### Parameters [​](https://dev.fluentcart.com/api/subscriptions\#parameters-1)

| Parameter | Type | Description |
| --- | --- | --- |
| `subscriptionOrderId` | integer | Subscription Order ID |

#### Response [​](https://dev.fluentcart.com/api/subscriptions\#response-1)

json

```
{
  "success": true,
  "data": {
    "subscription": {
      "id": 1,
      "uuid": "sub_abc123",
      "customer_id": 123,
      "product_id": 456,
      "variation_id": 789,
      "status": "active",
      "billing_cycle": "monthly",
      "amount": 2500,
      "currency": "USD",
      "next_billing_date": "2024-02-01T00:00:00Z",
      "created_at": "2024-01-01T10:00:00Z",
      "updated_at": "2024-01-15T14:30:00Z",
      "customer": {
        "id": 123,
        "email": "customer@example.com",
        "first_name": "John",
        "last_name": "Doe"
      },
      "product": {
        "id": 456,
        "title": "Premium Plan",
        "sku": "PREMIUM-001"
      },
      "order": {
        "id": 1,
        "status": "completed",
        "payment_status": "paid"
      },
      "transactions": [\
        {\
          "id": 1,\
          "amount": 2500,\
          "status": "succeeded",\
          "created_at": "2024-01-01T10:00:00Z"\
        }\
      ]
    }
  }
}
```

#### Example Request [​](https://dev.fluentcart.com/api/subscriptions\#example-request-1)

bash

```
curl -X GET "https://yoursite.com/wp-json/fluent-cart/v1/subscriptions/1" \
  -H "Authorization: Basic dXNlcm5hbWU6YXBwbGljYXRpb25fcGFzc3dvcmQ="
```

### Cancel Subscription [​](https://dev.fluentcart.com/api/subscriptions\#cancel-subscription)

**PUT**`/orders/{order}/subscriptions/{subscription}/cancel`

Cancel a subscription.

#### Parameters [​](https://dev.fluentcart.com/api/subscriptions\#parameters-2)

| Parameter | Type | Description |
| --- | --- | --- |
| `order` | integer | Order ID |
| `subscription` | integer | Subscription ID |

#### Request Body [​](https://dev.fluentcart.com/api/subscriptions\#request-body)

json

```
{
  "reason": "Customer requested cancellation",
  "cancel_immediately": false
}
```

#### Response [​](https://dev.fluentcart.com/api/subscriptions\#response-2)

json

```
{
  "success": true,
  "data": {
    "subscription": {
      "id": 1,
      "status": "cancelled",
      "cancelled_at": "2024-01-15T14:30:00Z",
      "cancellation_reason": "Customer requested cancellation"
    }
  }
}
```

#### Example Request [​](https://dev.fluentcart.com/api/subscriptions\#example-request-2)

bash

```
curl -X PUT "https://yoursite.com/wp-json/fluent-cart/v1/orders/1/subscriptions/1/cancel" \
  -H "Authorization: Basic dXNlcm5hbWU6YXBwbGljYXRpb25fcGFzc3dvcmQ=" \
  -H "Content-Type: application/json" \
  -d '{
    "reason": "Customer requested cancellation"
  }'
```

### Fetch Subscription [​](https://dev.fluentcart.com/api/subscriptions\#fetch-subscription)

**PUT**`/orders/{order}/subscriptions/{subscription}/fetch`

Fetch subscription data from payment gateway.

#### Parameters [​](https://dev.fluentcart.com/api/subscriptions\#parameters-3)

| Parameter | Type | Description |
| --- | --- | --- |
| `order` | integer | Order ID |
| `subscription` | integer | Subscription ID |

#### Response [​](https://dev.fluentcart.com/api/subscriptions\#response-3)

json

```
{
  "success": true,
  "data": {
    "subscription": {
      "id": 1,
      "status": "active",
      "next_billing_date": "2024-02-01T00:00:00Z",
      "updated_at": "2024-01-15T14:30:00Z"
    }
  }
}
```

#### Example Request [​](https://dev.fluentcart.com/api/subscriptions\#example-request-3)

bash

```
curl -X PUT "https://yoursite.com/wp-json/fluent-cart/v1/orders/1/subscriptions/1/fetch" \
  -H "Authorization: Basic dXNlcm5hbWU6YXBwbGljYXRpb25fcGFzc3dvcmQ="
```

### Reactivate Subscription [​](https://dev.fluentcart.com/api/subscriptions\#reactivate-subscription)

**PUT**`/orders/{order}/subscriptions/{subscription}/reactivate`

Reactivate a cancelled subscription.

#### Parameters [​](https://dev.fluentcart.com/api/subscriptions\#parameters-4)

| Parameter | Type | Description |
| --- | --- | --- |
| `order` | integer | Order ID |
| `subscription` | integer | Subscription ID |

#### Request Body [​](https://dev.fluentcart.com/api/subscriptions\#request-body-1)

json

```
{
  "reactivation_date": "2024-02-01T00:00:00Z"
}
```

#### Response [​](https://dev.fluentcart.com/api/subscriptions\#response-4)

json

```
{
  "success": true,
  "data": {
    "subscription": {
      "id": 1,
      "status": "active",
      "reactivated_at": "2024-01-15T14:30:00Z",
      "next_billing_date": "2024-02-01T00:00:00Z"
    }
  }
}
```

#### Example Request [​](https://dev.fluentcart.com/api/subscriptions\#example-request-4)

bash

```
curl -X PUT "https://yoursite.com/wp-json/fluent-cart/v1/orders/1/subscriptions/1/reactivate" \
  -H "Authorization: Basic dXNlcm5hbWU6YXBwbGljYXRpb25fcGFzc3dvcmQ=" \
  -H "Content-Type: application/json" \
  -d '{
    "reactivation_date": "2024-02-01T00:00:00Z"
  }'
```

### Pause Subscription [​](https://dev.fluentcart.com/api/subscriptions\#pause-subscription)

**PUT**`/orders/{order}/subscriptions/{subscription}/pause`

Pause a subscription.

#### Parameters [​](https://dev.fluentcart.com/api/subscriptions\#parameters-5)

| Parameter | Type | Description |
| --- | --- | --- |
| `order` | integer | Order ID |
| `subscription` | integer | Subscription ID |

#### Request Body [​](https://dev.fluentcart.com/api/subscriptions\#request-body-2)

json

```
{
  "pause_until": "2024-03-01T00:00:00Z",
  "reason": "Customer requested pause"
}
```

#### Response [​](https://dev.fluentcart.com/api/subscriptions\#response-5)

json

```
{
  "success": true,
  "data": {
    "subscription": {
      "id": 1,
      "status": "paused",
      "paused_at": "2024-01-15T14:30:00Z",
      "pause_until": "2024-03-01T00:00:00Z"
    }
  }
}
```

#### Example Request [​](https://dev.fluentcart.com/api/subscriptions\#example-request-5)

bash

```
curl -X PUT "https://yoursite.com/wp-json/fluent-cart/v1/orders/1/subscriptions/1/pause" \
  -H "Authorization: Basic dXNlcm5hbWU6YXBwbGljYXRpb25fcGFzc3dvcmQ=" \
  -H "Content-Type: application/json" \
  -d '{
    "pause_until": "2024-03-01T00:00:00Z",
    "reason": "Customer requested pause"
  }'
```

### Resume Subscription [​](https://dev.fluentcart.com/api/subscriptions\#resume-subscription)

**PUT**`/orders/{order}/subscriptions/{subscription}/resume`

Resume a paused subscription.

#### Parameters [​](https://dev.fluentcart.com/api/subscriptions\#parameters-6)

| Parameter | Type | Description |
| --- | --- | --- |
| `order` | integer | Order ID |
| `subscription` | integer | Subscription ID |

#### Response [​](https://dev.fluentcart.com/api/subscriptions\#response-6)

json

```
{
  "success": true,
  "data": {
    "subscription": {
      "id": 1,
      "status": "active",
      "resumed_at": "2024-01-15T14:30:00Z",
      "next_billing_date": "2024-02-01T00:00:00Z"
    }
  }
}
```

#### Example Request [​](https://dev.fluentcart.com/api/subscriptions\#example-request-6)

bash

```
curl -X PUT "https://yoursite.com/wp-json/fluent-cart/v1/orders/1/subscriptions/1/resume" \
  -H "Authorization: Basic dXNlcm5hbWU6YXBwbGljYXRpb25fcGFzc3dvcmQ="
```

## Customer Frontend Endpoints [​](https://dev.fluentcart.com/api/subscriptions\#customer-frontend-endpoints)

### Get Customer Subscriptions [​](https://dev.fluentcart.com/api/subscriptions\#get-customer-subscriptions)

**GET**`/customer-profile/subscriptions`

Get all subscriptions for the authenticated customer.

#### Response [​](https://dev.fluentcart.com/api/subscriptions\#response-7)

json

```
{
  "success": true,
  "data": {
    "subscriptions": [\
      {\
        "id": 1,\
        "uuid": "sub_abc123",\
        "product_id": 456,\
        "variation_id": 789,\
        "status": "active",\
        "billing_cycle": "monthly",\
        "amount": 2500,\
        "currency": "USD",\
        "next_billing_date": "2024-02-01T00:00:00Z",\
        "product": {\
          "id": 456,\
          "title": "Premium Plan",\
          "sku": "PREMIUM-001"\
        }\
      }\
    ]
  }
}
```

#### Example Request [​](https://dev.fluentcart.com/api/subscriptions\#example-request-7)

bash

```
curl -X GET "https://yoursite.com/wp-json/fluent-cart/v1/customer-profile/subscriptions" \
  -H "Authorization: Basic dXNlcm5hbWU6YXBwbGljYXRpb25fcGFzc3dvcmQ="
```

### Get Customer Subscription Details [​](https://dev.fluentcart.com/api/subscriptions\#get-customer-subscription-details)

**GET**`/customer-profile/subscriptions/{subscription_uuid}`

Get detailed information about a specific customer subscription.

#### Parameters [​](https://dev.fluentcart.com/api/subscriptions\#parameters-7)

| Parameter | Type | Description |
| --- | --- | --- |
| `subscription_uuid` | string | Subscription UUID |

#### Response [​](https://dev.fluentcart.com/api/subscriptions\#response-8)

json

```
{
  "success": true,
  "data": {
    "subscription": {
      "id": 1,
      "uuid": "sub_abc123",
      "product_id": 456,
      "variation_id": 789,
      "status": "active",
      "billing_cycle": "monthly",
      "amount": 2500,
      "currency": "USD",
      "next_billing_date": "2024-02-01T00:00:00Z",
      "created_at": "2024-01-01T10:00:00Z",
      "product": {
        "id": 456,
        "title": "Premium Plan",
        "sku": "PREMIUM-001"
      },
      "transactions": [\
        {\
          "id": 1,\
          "amount": 2500,\
          "status": "succeeded",\
          "created_at": "2024-01-01T10:00:00Z"\
        }\
      ]
    }
  }
}
```

#### Example Request [​](https://dev.fluentcart.com/api/subscriptions\#example-request-8)

bash

```
curl -X GET "https://yoursite.com/wp-json/fluent-cart/v1/customer-profile/subscriptions/sub_abc123" \
  -H "Authorization: Basic dXNlcm5hbWU6YXBwbGljYXRpb25fcGFzc3dvcmQ="
```

### Update Payment Method [​](https://dev.fluentcart.com/api/subscriptions\#update-payment-method)

**POST**`/customer-profile/subscriptions/{subscription_uuid}/update-payment-method`

Update the payment method for a subscription.

#### Parameters [​](https://dev.fluentcart.com/api/subscriptions\#parameters-8)

| Parameter | Type | Description |
| --- | --- | --- |
| `subscription_uuid` | string | Subscription UUID |

#### Request Body [​](https://dev.fluentcart.com/api/subscriptions\#request-body-3)

json

```
{
  "payment_method_id": "pm_1234567890",
  "payment_method_type": "card"
}
```

#### Response [​](https://dev.fluentcart.com/api/subscriptions\#response-9)

json

```
{
  "success": true,
  "data": {
    "subscription": {
      "id": 1,
      "payment_method_id": "pm_1234567890",
      "updated_at": "2024-01-15T14:30:00Z"
    }
  }
}
```

#### Example Request [​](https://dev.fluentcart.com/api/subscriptions\#example-request-9)

bash

```
curl -X POST "https://yoursite.com/wp-json/fluent-cart/v1/customer-profile/subscriptions/sub_abc123/update-payment-method" \
  -H "Authorization: Basic dXNlcm5hbWU6YXBwbGljYXRpb25fcGFzc3dvcmQ=" \
  -H "Content-Type: application/json" \
  -d '{
    "payment_method_id": "pm_1234567890",
    "payment_method_type": "card"
  }'
```

### Get or Create Plan [​](https://dev.fluentcart.com/api/subscriptions\#get-or-create-plan)

**POST**`/customer-profile/subscriptions/{subscription_uuid}/get-or-create-plan`

Get or create a subscription plan.

#### Parameters [​](https://dev.fluentcart.com/api/subscriptions\#parameters-9)

| Parameter | Type | Description |
| --- | --- | --- |
| `subscription_uuid` | string | Subscription UUID |

#### Request Body [​](https://dev.fluentcart.com/api/subscriptions\#request-body-4)

json

```
{
  "plan_id": "plan_1234567890",
  "amount": 2500,
  "billing_cycle": "monthly"
}
```

#### Response [​](https://dev.fluentcart.com/api/subscriptions\#response-10)

json

```
{
  "success": true,
  "data": {
    "plan": {
      "id": "plan_1234567890",
      "amount": 2500,
      "billing_cycle": "monthly",
      "created": false
    }
  }
}
```

#### Example Request [​](https://dev.fluentcart.com/api/subscriptions\#example-request-10)

bash

```
curl -X POST "https://yoursite.com/wp-json/fluent-cart/v1/customer-profile/subscriptions/sub_abc123/get-or-create-plan" \
  -H "Authorization: Basic dXNlcm5hbWU6YXBwbGljYXRpb25fcGFzc3dvcmQ=" \
  -H "Content-Type: application/json" \
  -d '{
    "plan_id": "plan_1234567890",
    "amount": 2500,
    "billing_cycle": "monthly"
  }'
```

### Switch Payment Method [​](https://dev.fluentcart.com/api/subscriptions\#switch-payment-method)

**POST**`/customer-profile/subscriptions/{subscription_uuid}/switch-payment-method`

Switch the payment method for a subscription.

#### Parameters [​](https://dev.fluentcart.com/api/subscriptions\#parameters-10)

| Parameter | Type | Description |
| --- | --- | --- |
| `subscription_uuid` | string | Subscription UUID |

#### Request Body [​](https://dev.fluentcart.com/api/subscriptions\#request-body-5)

json

```
{
  "new_payment_method_id": "pm_0987654321",
  "payment_method_type": "card"
}
```

#### Response [​](https://dev.fluentcart.com/api/subscriptions\#response-11)

json

```
{
  "success": true,
  "data": {
    "subscription": {
      "id": 1,
      "payment_method_id": "pm_0987654321",
      "updated_at": "2024-01-15T14:30:00Z"
    }
  }
}
```

#### Example Request [​](https://dev.fluentcart.com/api/subscriptions\#example-request-11)

bash

```
curl -X POST "https://yoursite.com/wp-json/fluent-cart/v1/customer-profile/subscriptions/sub_abc123/switch-payment-method" \
  -H "Authorization: Basic dXNlcm5hbWU6YXBwbGljYXRpb25fcGFzc3dvcmQ=" \
  -H "Content-Type: application/json" \
  -d '{
    "new_payment_method_id": "pm_0987654321",
    "payment_method_type": "card"
  }'
```

### Confirm Subscription Switch [​](https://dev.fluentcart.com/api/subscriptions\#confirm-subscription-switch)

**POST**`/customer-profile/subscriptions/{subscription_uuid}/confirm-subscription-switch`

Confirm a subscription payment method switch.

#### Parameters [​](https://dev.fluentcart.com/api/subscriptions\#parameters-11)

| Parameter | Type | Description |
| --- | --- | --- |
| `subscription_uuid` | string | Subscription UUID |

#### Request Body [​](https://dev.fluentcart.com/api/subscriptions\#request-body-6)

json

```
{
  "confirmation_token": "conf_1234567890"
}
```

#### Response [​](https://dev.fluentcart.com/api/subscriptions\#response-12)

json

```
{
  "success": true,
  "data": {
    "subscription": {
      "id": 1,
      "status": "active",
      "payment_method_switched": true,
      "updated_at": "2024-01-15T14:30:00Z"
    }
  }
}
```

#### Example Request [​](https://dev.fluentcart.com/api/subscriptions\#example-request-12)

bash

```
curl -X POST "https://yoursite.com/wp-json/fluent-cart/v1/customer-profile/subscriptions/sub_abc123/confirm-subscription-switch" \
  -H "Authorization: Basic dXNlcm5hbWU6YXBwbGljYXRpb25fcGFzc3dvcmQ=" \
  -H "Content-Type: application/json" \
  -d '{
    "confirmation_token": "conf_1234567890"
  }'
```

### Confirm Subscription Reactivation [​](https://dev.fluentcart.com/api/subscriptions\#confirm-subscription-reactivation)

**POST**`/customer-profile/subscriptions/{subscription_uuid}/confirm-subscription-reactivation`

Confirm a subscription reactivation.

#### Parameters [​](https://dev.fluentcart.com/api/subscriptions\#parameters-12)

| Parameter | Type | Description |
| --- | --- | --- |
| `subscription_uuid` | string | Subscription UUID |

#### Request Body [​](https://dev.fluentcart.com/api/subscriptions\#request-body-7)

json

```
{
  "reactivation_token": "react_1234567890"
}
```

#### Response [​](https://dev.fluentcart.com/api/subscriptions\#response-13)

json

```
{
  "success": true,
  "data": {
    "subscription": {
      "id": 1,
      "status": "active",
      "reactivated_at": "2024-01-15T14:30:00Z",
      "next_billing_date": "2024-02-01T00:00:00Z"
    }
  }
}
```

#### Example Request [​](https://dev.fluentcart.com/api/subscriptions\#example-request-13)

bash

```
curl -X POST "https://yoursite.com/wp-json/fluent-cart/v1/customer-profile/subscriptions/sub_abc123/confirm-subscription-reactivation" \
  -H "Authorization: Basic dXNlcm5hbWU6YXBwbGljYXRpb25fcGFzc3dvcmQ=" \
  -H "Content-Type: application/json" \
  -d '{
    "reactivation_token": "react_1234567890"
  }'
```

### Cancel Auto Renew [​](https://dev.fluentcart.com/api/subscriptions\#cancel-auto-renew)

**POST**`/customer-profile/subscriptions/{subscription_uuid}/cancel-auto-renew`

Cancel auto-renewal for a subscription.

#### Parameters [​](https://dev.fluentcart.com/api/subscriptions\#parameters-13)

| Parameter | Type | Description |
| --- | --- | --- |
| `subscription_uuid` | string | Subscription UUID |

#### Request Body [​](https://dev.fluentcart.com/api/subscriptions\#request-body-8)

json

```
{
  "reason": "Customer requested cancellation",
  "cancel_at_period_end": true
}
```

#### Response [​](https://dev.fluentcart.com/api/subscriptions\#response-14)

json

```
{
  "success": true,
  "data": {
    "subscription": {
      "id": 1,
      "auto_renew": false,
      "cancel_at_period_end": true,
      "cancellation_date": "2024-02-01T00:00:00Z",
      "updated_at": "2024-01-15T14:30:00Z"
    }
  }
}
```

#### Example Request [​](https://dev.fluentcart.com/api/subscriptions\#example-request-14)

bash

```
curl -X POST "https://yoursite.com/wp-json/fluent-cart/v1/customer-profile/subscriptions/sub_abc123/cancel-auto-renew" \
  -H "Authorization: Basic dXNlcm5hbWU6YXBwbGljYXRpb25fcGFzc3dvcmQ=" \
  -H "Content-Type: application/json" \
  -d '{
    "reason": "Customer requested cancellation",
    "cancel_at_period_end": true
  }'
```

## Error Handling [​](https://dev.fluentcart.com/api/subscriptions\#error-handling)

### Common Error Codes [​](https://dev.fluentcart.com/api/subscriptions\#common-error-codes)

| Code | Description |
| --- | --- |
| `subscription_not_found` | Subscription with specified ID not found |
| `invalid_subscription_status` | Subscription status does not allow this operation |
| `payment_method_invalid` | Payment method is invalid or expired |
| `insufficient_permissions` | User lacks required permissions |
| `validation_error` | Request data validation failed |
| `gateway_error` | Payment gateway error occurred |

### Error Response Example [​](https://dev.fluentcart.com/api/subscriptions\#error-response-example)

json

```
{
  "success": false,
  "error": {
    "code": "subscription_not_found",
    "message": "Subscription with ID 999 not found"
  }
}
```

## Rate Limiting [​](https://dev.fluentcart.com/api/subscriptions\#rate-limiting)

- **List operations**: 100 requests per hour
- **Create operations**: 50 requests per hour
- **Update operations**: 200 requests per hour
- **Cancel operations**: 20 requests per hour

## Related Documentation [​](https://dev.fluentcart.com/api/subscriptions\#related-documentation)

- [Orders API](https://dev.fluentcart.com/api/orders.html) \- Order management endpoints
- [Customers API](https://dev.fluentcart.com/api/customers.html) \- Customer management endpoints
- [Products API](https://dev.fluentcart.com/api/products.html) \- Product management endpoints
- [Database Models](https://dev.fluentcart.com/database/models.html) \- Subscription data models
- [Developer Hooks](https://dev.fluentcart.com/hooks/) \- Subscription-related hooks

## Next Steps [​](https://dev.fluentcart.com/api/subscriptions\#next-steps)

Continue with subscription management:

1. **[Orders API](https://dev.fluentcart.com/api/orders.html)** \- Manage subscription orders
2. **[Customers API](https://dev.fluentcart.com/api/customers.html)** \- Manage customer data
3. **[Products API](https://dev.fluentcart.com/api/products.html)** \- Manage subscription products
4. **[Database Models](https://dev.fluentcart.com/database/models.html)** \- Understand subscription data structure

## Previous/Next Navigation [​](https://dev.fluentcart.com/api/subscriptions\#previous-next-navigation)

- **Previous**: [Products API](https://dev.fluentcart.com/api/products.html) \- Product management endpoints
- **Next**: [Authentication Guide](https://dev.fluentcart.com/api/authentication.html) \- API authentication

* * *

Today

Hi! I’m your AI assistant. How can I assist you today?

Just now

Powered by **FluentBot**


---

---

