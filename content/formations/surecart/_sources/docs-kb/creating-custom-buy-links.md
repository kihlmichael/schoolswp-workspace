---
source_url: https://surecart.com/docs/creating-custom-buy-links
source: surecart-kb
scraped: true
---

# Creating Custom Buy Links

While SureCart provides copy/paste buy links when you create your product prices, sometimes you may want to create custom purchase links that allow your users to purchase a product.

You can even specify several different products or prices and the quantities for each. You can accomplish this using URL parameters.

### Creating The Link

In this section, we'll walk you through the process of creating custom purchase links for your products.

#### Finding the Price ID

The first step is to find the **price ID** that you want to use for the line item. You can do this by navigating to your Edit Product page and clicking on **Copy Links** next to the price.

This will open a new section that contains all of the links associated with your product. Next, click **Copy** next to the **Price ID** box.

#### Creating the URL

To add line items, you will want to use the _line_items_ parameter in the URL. The URL accepts multiple options, so it will follow the format:

```
https://yoursite.com/checkout?line_items[0][price_id]=5366e5a3
```

Replace 'https://yoursite.com/checkout?' with your actual WordPress site link.

Enter the price id you copied after "\[price_id\]= "

When you click on the newly created link, it will redirect you to the usual product page.

#### Changing the quantity

You can also specify the quantity of a line item in the URL as well. This would give the line item a quantity of "2".

```
https://yoursite.com/checkout?line_items[0][price_id]=5366e5a3&line_items[0][quantity]=2
```

#### Adding multiple items

You may want to add more than a single line item to the checkout. To do that, you can do this:

```
https://yoursite.com/checkout?line_items[0][price_id]=5366e5a3&line_items[1][price_id]=402d8e25
```

As you can see, we are adding an additional _line_items_ parameter, but instead of using the "key" \[0\], we are using \[1\] to indicate it's a separate line item.
