---
source_url: https://developer.surecart.com/api-reference/pagination
source: surecart-developer-docs
scraped: true
---

[Skip to main content](https://developer.surecart.com/api-reference/pagination#content-area)

> ## Documentation Index
>
> Fetch the complete documentation index at: [https://developer.surecart.com/llms.txt](https://developer.surecart.com/llms.txt)
>
> Use this file to discover all available pages before exploring further.

SureCart utilizes offset-based pagination, and all top-level API resources have support for bulk fetches via "list" API methods. For instance, you can list products, prices, and customers. These list API methods share a common structure, taking at least these two parameters: `limit`, and `page`. The default pagination limit is `20` and the max is `100`.By default, all list API methods return collections sorted by `created_at` in `desc` order. The sort order can be adjusted by passing the `sort` parameter. The format for this parameter is `?sort=column:order` which allows you to specify the value to sort by and the order. For example, if you wanted to sort by `updated_at` in `asc` order you would set the parameter to `?sort=updated_at:asc`.All list API methods can be sorted by `created_at` and `updated_at` values. Some API endpoints can be sorted by other values, and these methods have further documentation on the sort parameter.
