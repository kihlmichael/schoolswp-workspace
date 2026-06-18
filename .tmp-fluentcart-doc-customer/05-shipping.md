# Section Shipping

Source : docs.fluentcart.com
Date scrape : 2026-05-19

---

## Shipping Overview - FluentCart Documentation
URL : https://docs.fluentcart.com/guide/shipping/

[Skip to content](https://docs.fluentcart.com/guide/shipping/#VPContent)

# Shipping Overview [​](https://docs.fluentcart.com/guide/shipping/\#shipping-overview)

FluentCart’s powerful shipping system allows you to set up flexible shipping rules based on your customer’s location, what they’re buying, and how shipping costs are calculated. This easy guide will help you set up shipping for your store so your physical products are delivered correctly and on time.

With FluentCart Shipping, you can:

- **[Define Shipping Zones](https://docs.fluentcart.com/guide/shipping/configuring-shipping-zones)**: Group geographical areas to apply specific shipping rules.
- **[Create Flexible Shipping Methods](https://docs.fluentcart.com/guide/shipping/setting-up-shipping-methods)**: Offer various delivery options like Flat Rate, Free Shipping, or Local Pickup, with diverse pricing structures (per order, per item, per weight, or per value).
- **[Utilize Shipping Classes](https://docs.fluentcart.com/guide/shipping/understanding-shipping-classes)**: Group products with similar shipping characteristics (e.g., "Heavy Items," "Fragile Goods") to apply specific cost adjustments.
- **[Control Advanced Calculations](https://docs.fluentcart.com/guide/shipping/advanced-shipping-calculations)**: Configure how shipping costs are aggregated when customers purchase multiple products from different shipping classes.
- **[Manage Packages](https://docs.fluentcart.com/guide/shipping/packages)**: Define the boxes, envelopes, and soft packages you ship with so FluentCart can accurately calculate rates at checkout and pre-select the right packaging when fulfilling orders.

Today

Hi! I’m your AI assistant. How can I assist you today?

Just now

Powered by **FluentBot**

---

## Advanced Shipping Calculations - FluentCart Documentation
URL : https://docs.fluentcart.com/guide/shipping/advanced-shipping-calculations

[Skip to content](https://docs.fluentcart.com/guide/shipping/advanced-shipping-calculations#VPContent)

# Advanced Shipping Calculations [​](https://docs.fluentcart.com/guide/shipping/advanced-shipping-calculations\#advanced-shipping-calculations)

Understanding how FluentCart calculates shipping costs, especially when combining different shipping methods and shipping classes, is key to setting up accurate rates. This guide clarifies the "Class Aggregation" logic.

## How Shipping Costs are Calculated at Checkout [​](https://docs.fluentcart.com/guide/shipping/advanced-shipping-calculations\#how-shipping-costs-are-calculated-at-checkout)

When a customer proceeds to checkout, FluentCart dynamically calculates available shipping options based on their address and the contents of their cart.

The calculation follows these general steps:

1. **Zone Matching**: The customer's shipping address is matched to an [applicable shipping zone](https://docs.fluentcart.com/guide/shipping/configuring-shipping-zones).

2. **Method Selection**: All [shipping methods](https://docs.fluentcart.com/guide/shipping/setting-up-shipping-methods) configured for that zone become potential options.

3. **Base Method Cost**: For each applicable method, its base cost is calculated based on its "Rate Type" (e.g., a fixed amount, total items, or total order value).

4. **Shipping Class Contributions**: This is where the complexity comes in. For each product in the cart, its assigned [shipping class](https://docs.fluentcart.com/guide/shipping/understanding-shipping-classes) (if any) and its quantity are considered.

   - The "Cost Adjustment" for that shipping class is applied based on its "Cost Type" (`Per Item` or `Fixed Amount`).
   - These individual class contributions are then gathered.
5. **Class Aggregation (Crucial Step)**: If the cart contains products from _multiple distinct shipping classes_, the `Class Aggregation` setting of the _chosen shipping method_ dictates how these class contributions are combined into a single subtotal for shipping class adjustments.

   - **"Sum all class costs"**:

     - **Concept**: This option adds up the calculated cost for _each distinct shipping class_ present in the cart.
     - **Scenario**: Your cart contains:
       - Product A: `Quantity: 2`, `Shipping Class: Heavy Items` (Cost Adjustment: $15, Type: Per Item)
       - Product B: `Quantity: 1`, `Shipping Class: Small Envelopes` (Cost Adjustment: $5, Type: Per Item)
       - Product C: `Quantity: 3`, `Shipping Class: Fragile Items` (Cost Adjustment: $4, Type: Fixed Amount)
     - **Calculation**:
       - Contribution from "Heavy Items" = $15 (per item) \* 2 items = $30
       - Contribution from "Small Envelopes" = $5 (per item) \* 1 item = $5
       - Contribution from "Fragile Items" = $4 (fixed amount, applied once for the class) = $4
     - **Total Aggregated Class Cost** = $30 (Heavy) + $5 (Small) + $4 (Fragile) = **$39**.
   - **"Take highest class cost"**:

     - **Concept**: This option applies only the highest individual shipping cost derived from any _distinct shipping class_ present in the cart.
     - **Scenario**: Using the same cart as above:
       - Contribution from "Heavy Items" = $30
       - Contribution from "Small Envelopes" = $5
       - Contribution from "Fragile Items" = $4
     - **Total Aggregated Class Cost** = `MAX($30, $5, $4)` = **$30**.
6. **Final Shipping Cost**: The `Base Method Cost` (from step 3) is then added to the `Aggregated Class Cost` (from step 5) to determine the final shipping price for that particular method.


By understanding these calculation types, you can fine-tune your shipping strategy to accurately reflect the costs of delivering diverse products to your customers.

Today

Hi! I’m your AI assistant. How can I assist you today?

Just now

Powered by **FluentBot**

---

## Configuring Shipping Zones - FluentCart Documentation
URL : https://docs.fluentcart.com/guide/shipping/configuring-shipping-zones

[Skip to content](https://docs.fluentcart.com/guide/shipping/configuring-shipping-zones#VPContent)

# Configuring Shipping Zones [​](https://docs.fluentcart.com/guide/shipping/configuring-shipping-zones\#configuring-shipping-zones)

Shipping zones are geographical regions that allow you to define specific shipping methods and rates for your customers. By creating zones, you can customize shipping options for different countries or areas. This guide will walk you through setting up a new shipping zone.

## How to Add and Manage Shipping Zones [​](https://docs.fluentcart.com/guide/shipping/configuring-shipping-zones\#how-to-add-and-manage-shipping-zones)

### 1\. Navigate to Shipping Settings [​](https://docs.fluentcart.com/guide/shipping/configuring-shipping-zones\#_1-navigate-to-shipping-settings)

To begin, you must navigate to the shipping configuration area within FluentCart.

1. From the main WordPress dashboard, locate the **FluentCart** section in the left-hand navigation menu and click on **Settings**.
2. On the Settings page, select the **Shipping** tab from the left menu.
3. Ensure the **Shipping Zones** sub-tab is selected. This screen will display a list of all your existing shipping zones.

### 2\. Add a New Shipping Zone [​](https://docs.fluentcart.com/guide/shipping/configuring-shipping-zones\#_2-add-a-new-shipping-zone)

1. Click the dark **Add Shipping Zone** button located at the top right of the screen.
2. You will be taken to the "Add Shipping Zone" setup page.

![Screenshot of Configuring Shipping Zones](https://docs.fluentcart.com/images/shipping/Configuring-Shipping-Zones/FluentCart-Shipping-Category-1.webp)

### 3\. Name Your Zone and Define Coverage [​](https://docs.fluentcart.com/guide/shipping/configuring-shipping-zones\#_3-name-your-zone-and-define-coverage)

Now you are on the setup page for your new zone. Here, you will name your zone and precisely target where it applies using the new coverage settings:

**Zone Name:** Give your zone a descriptive name that is easy for you to remember internally. For example, "North America," "Europe," or "Local Customers."

**Coverage:** This powerful setting determines exactly which countries belong to this shipping zone. You have three flexible options to choose from:

- **Whole world:** Select this if the shipping methods in this zone apply globally to every single country and territory.

![Screenshot of Configuring Shipping Zones](https://docs.fluentcart.com/images/shipping/Configuring-Shipping-Zones/FluentCart-Shipping-Category-2.webp)

- **Selected countries only:** Select this to ship exclusively to specific countries. A _Countries_ dropdown box will appear below. You can search and check the boxes next to the specific countries you want to include (e.g., just the United States and Canada).

![Screenshot of Configuring Shipping Zones](https://docs.fluentcart.com/images/shipping/Configuring-Shipping-Zones/FluentCart-Shipping-Category-3.webp)

- **All countries except:** Select this if you ship globally but want to exclude a few specific places. Use the _Countries_ dropdown box to search and select the regions where you do not want to offer these shipping methods.

![Screenshot of Configuring Shipping Zones](https://docs.fluentcart.com/images/shipping/Configuring-Shipping-Zones/FluentCart-Shipping-Category-4.webp)

### 4\. Save Your Zone [​](https://docs.fluentcart.com/guide/shipping/configuring-shipping-zones\#_4-save-your-zone)

Once you are happy with the name and the coverage regions you have configured, simply click the **Save** button at the top right of the screen.

Your new shipping zone will now appear in your list of zones, and you can proceed to add specific [shipping methods](https://docs.fluentcart.com/guide/shipping/setting-up-shipping-methods) and rates to it!

> **INFO:** Customers will only see the shipping methods that are applicable to the zone their shipping address falls into during checkout.

Today

Hi! I’m your AI assistant. How can I assist you today?

Just now

Powered by **FluentBot**

---

## Managing Packages - FluentCart Documentation
URL : https://docs.fluentcart.com/guide/shipping/packages

[Skip to content](https://docs.fluentcart.com/guide/shipping/packages#VPContent)

# Managing Packages [​](https://docs.fluentcart.com/guide/shipping/packages\#managing-packages)

Packages in FluentCart let you define the physical boxes, envelopes, or soft packages you use to ship your products. By setting up your packaging ahead of time, FluentCart can accurately calculate shipping rates at checkout and pre-select the right package when you're fulfilling orders.

This guide walks you through adding, managing, and configuring your store's packages.

TIP

You can also add a new package directly from the product editor. When configuring a physical product's shipping details - under the **Pricing** panel in the **Shipping** section - you'll find a **Package** dropdown. If no packages have been created yet, simply open that dropdown and select the option to add a new one without leaving the product page.

The package you create will be saved to your store and available here in the Packages settings as well. See [Creating Physical Products](https://docs.fluentcart.com/guide/product-types-creation/creating-physical-products) for more details.

## Accessing Packages [​](https://docs.fluentcart.com/guide/shipping/packages\#accessing-packages)

To get started, navigate to **FluentCart Pro** \> **Settings** \> **Shipping** \> **Packages** from your WordPress dashboard.

You will see a list of all the packages you have already created. From here, you can add new packages or manage existing ones.

![Screenshot of Packages list](https://docs.fluentcart.com/images/shipping/packages/packages-1.webp)

## Adding a New Package [​](https://docs.fluentcart.com/guide/shipping/packages\#adding-a-new-package)

To add a new package, click the **Add Package** button in the top-right corner of the Packages screen. This will open the **Add package** modal where you can configure all the details for your new package.

![Screenshot of Add Package modal](https://docs.fluentcart.com/images/shipping/packages/packages-2.webp)

### Package Type [​](https://docs.fluentcart.com/guide/shipping/packages\#package-type)

Choose the physical type of packaging you use:

- **Box** - A rigid, box-shaped container. Ideal for most standard shipments.
- **Envelope** - A flat mailer or padded envelope. Best suited for thin or lightweight items.
- **Soft package** - A flexible bag or poly mailer. Useful for clothing, soft goods, or compressible items.

### Dimensions & Weight [​](https://docs.fluentcart.com/guide/shipping/packages\#dimensions-weight)

Enter the physical measurements of your empty package:

- **Length** - The longest dimension of the package.
- **Width** - The width of the package.
- **Height** - The height (or depth) of the package.
- **Weight (empty)** - The weight of the packaging itself when empty.

You can set the unit for dimensions (e.g., **in**, **cm**) and the unit for weight (e.g., **kg**, **lb**) using the dropdowns next to each field. Make sure these match the units configured in your store settings.

### Package Name [​](https://docs.fluentcart.com/guide/shipping/packages\#package-name)

Give your package a clear, descriptive name (e.g., "Small Box," "Large Envelope," "Medium Poly Mailer"). This name is used internally to help you identify packages when assigning them to products or reviewing orders.

### Use as Default Package [​](https://docs.fluentcart.com/guide/shipping/packages\#use-as-default-package)

Check **Use as default package** to make this package the store-wide default. The default package is used to calculate shipping rates at checkout and is pre-selected when assigning packages to products.

INFO

Only one package can be the store default at a time. Setting a new package as the default will automatically remove the default designation from the previously selected package.

Once you have filled in all the details, click **Add package** to save it. Your new package will now appear in the Packages list.

## Managing Existing Packages [​](https://docs.fluentcart.com/guide/shipping/packages\#managing-existing-packages)

Each package in your list has a three-dot menu ( **⋮**) on the right side. Click it to reveal the available actions:

![Screenshot of Package management options](https://docs.fluentcart.com/images/shipping/packages/packages-3.webp)

- **Edit** - Opens the package settings so you can update its name, type, dimensions, or weight.
- **Set as default** - Marks this package as the store default, which will be used for shipping rate calculations at checkout.
- **Delete** - Permanently removes the package from your store. Deleting a package cannot be undone.

Today

Hi! I’m your AI assistant. How can I assist you today?

Just now

Powered by **FluentBot**

---

## Setting Up Shipping Methods - FluentCart Documentation
URL : https://docs.fluentcart.com/guide/shipping/setting-up-shipping-methods

[Skip to content](https://docs.fluentcart.com/guide/shipping/setting-up-shipping-methods#VPContent)

# Setting Up Shipping Methods [​](https://docs.fluentcart.com/guide/shipping/setting-up-shipping-methods\#setting-up-shipping-methods)

Shipping methods are the different delivery options you offer to customers within a specific [**shipping zone**](https://docs.fluentcart.com/guide/shipping/configuring-shipping-zones). FluentCart allows you to create flexible shipping options, from flat rates to free shipping, ensuring you can meet your customers' needs.

This guide will show you how to add and configure shipping methods for your shipping zones.

### How to Add a Shipping Method [​](https://docs.fluentcart.com/guide/shipping/setting-up-shipping-methods\#how-to-add-a-shipping-method)

Before you can add a method, you must have already created a shipping zone.

1. From your WordPress dashboard, navigate to **FluentCart Pro** \> **Settings** \> **Shipping Zones**.
2. Click on the **Shipping Zones** sub-menu.
3. Find the shipping zone you want to add a method to and click on its name to edit it.
4. Inside the zone's settings, scroll down to the **Shipping Methods** section and click the **Add Shipping Method** button. You can also manage your existing shipping methods from this screen. To update a method's settings, click the Edit button located on the same row as its title.
5. This will open a pop-up window where you can configure the details of your new shipping method.

![Screenshot of Shipping Method](https://docs.fluentcart.com/images/shipping/setting-up-shipping-method/shipping-method-1.webp)

### Configuring the Shipping Method [​](https://docs.fluentcart.com/guide/shipping/setting-up-shipping-methods\#configuring-the-shipping-method)

This is where you define how your shipping option will work.

- **Enable Shipping Method:** This toggle at the top of the pop-up acts as the master switch for this specific method. If it's disabled, the method will be saved but won't appear as an option for customers at checkout.

- **Method Title:** Enter a clear and user-friendly name for this shipping option (e.g., "Standard Shipping," "Express Delivery," "Local Pickup"). This is the name your customers will see at checkout.

- **State:** (Optional) If this shipping method should only be available for specific states or provinces within the shipping zone's country, you can select them here. Leave it blank to have the method apply to the entire country.

- **Method Type:** Choose the type of shipping method you want to offer:

  - **Flat Rate:** This is a fixed-cost shipping option. Use this to set a single rate for delivery.
  - **Free Shipping:** As the name suggests, this option is free for the customer. It's an excellent incentive to encourage sales.
  - **Local Pickup:** This allows customers to pick up their order directly from your physical store or a designated location, bypassing shipping costs entirely.
- **Amount:** If you selected "Flat Rate," enter the cost for this shipping method here (e.g., enter **10** for $10.00). The Amount field hides automatically when **Configure Rate** is set to **Per Weight**, because the cost then comes from your weight tiers instead of a flat value.

- **Configure Rate**


This setting determines how the "Flat Rate" cost is calculated if a customer has multiple items in their cart.

- **Per Order:** Applies a single, fixed charge for the entire order, no matter how many items are purchased. This is the most common setup.
- **Per Item:** The shipping cost is multiplied by the number of items in the cart. For example, if the cost is $2 and a customer buys 3 items, the total shipping cost will be $6.
- **Percentage:** The shipping cost is calculated as a percentage of the total order price. For example, a 10% rate on a $50 order would result in a $5 shipping fee.
- **Per Weight:** Charges shipping based on the total weight of the cart, using a set of tiered rates you define (see **Weight Tiers** below). Ideal for carriers that price by weight brackets - light envelopes at one rate, medium parcels at another, heavy freight higher still.

#### Weight Tiers (Per-Weight Rates) [​](https://docs.fluentcart.com/guide/shipping/setting-up-shipping-methods\#weight-tiers-per-weight-rates)

When **Configure Rate** is set to **Per Weight**, a **Weight Tiers** editor appears in place of the fixed Amount field. Each tier defines a weight range and the shipping cost that applies when the cart's total weight falls inside that range.

Each row has three fields:

- **Min (weight)** - The lower bound of the tier, inclusive. Editable on every tier, including the first one (it does not have to start at `0`).
- **Max (weight)** - The upper bound of the tier. Must be greater than the tier's Min.
- **Cost** - The shipping amount charged when the cart's total weight lands inside this tier.

Click **Add Tier** to append a new row. A new tier defaults to `previous max + 0.01` for Min so you can chain ranges quickly, but every field stays editable.

**Flexible, non-contiguous ranges**

Tiers do not have to be continuous. You can leave gaps between ranges - for example, `0–10 kg`, then `15–20 kg` - when your carrier simply does not offer rates in the gap, or when weights in that gap should fall back to a different shipping method.

**Validation**

The editor validates tiers inline before you can save:

- A tier whose **Max** is less than or equal to its **Min** shows an error and the **Add Tier** button is disabled until fixed.
- A tier whose range **overlaps** an earlier tier (e.g., `0–10` followed by `8–15`) shows an error - overlapping ranges would create ambiguity when a cart weight fits both tiers.

Correct the highlighted tier and the error clears immediately, re-enabling the **Add Tier** button and the **Save** action.

#### How It Looks at Checkout [​](https://docs.fluentcart.com/guide/shipping/setting-up-shipping-methods\#how-it-looks-at-checkout)

Once saved, the shipping method appears under **Shipping Options** on the checkout page with the method title and its calculated cost. The Order summary on the right reflects the same amount under **Shipping**, so what the customer picks is exactly what they pay.

![Screenshot of the checkout page showing the shipping method under Shipping Options with its price, and the Order summary reflecting the Shipping line](https://docs.fluentcart.com/images/shipping/setting-up-shipping-method/shipping-method-checkout.webp)

- **Class Aggregation**

This advanced setting is for when a customer's cart contains products from different shipping classes (e.g., a small item and a bulky, oversized item). It tells FluentCart how to combine the shipping costs.

- **Combined Cost:** The shipping costs for each distinct shipping class in the cart are calculated and then added together to get the final total.
- **Highest Cost:** Only the single highest shipping cost among all the shipping classes present in the cart is applied.

INFO

The Configure Rate and Class Aggregation settings work together to give you precise control over your shipping fees. For a more detailed guide with advanced examples of how these calculations work, especially when a cart contains multiple items from different shipping classes, please see our documentation on [Advanced Shipping Calculations](https://docs.fluentcart.com/guide/shipping/advanced-shipping-calculations).

- **Description:**

You can add a short description for the shipping method. Depending on your theme, this might be displayed to the customer at checkout to provide more context (e.g., "Delivered in 3-5 business days").

![Screenshot of Shipping Method](https://docs.fluentcart.com/images/shipping/setting-up-shipping-method/shipping-method-2.webp)

Once you have configured all the details, click the **Save** button. Your new shipping method is now active and will be offered to customers in the selected shipping zone.

Today

Hi! I’m your AI assistant. How can I assist you today?

Just now

Powered by **FluentBot**

---

## Understanding and Using Shipping Classes - FluentCart Documentation
URL : https://docs.fluentcart.com/guide/shipping/understanding-shipping-classes

[Skip to content](https://docs.fluentcart.com/guide/shipping/understanding-shipping-classes#VPContent)

# Understanding and Using Shipping Classes [​](https://docs.fluentcart.com/guide/shipping/understanding-shipping-classes\#understanding-and-using-shipping-classes)

The most common use for a shipping class is to adjust the shipping cost for certain types of items. For example, you can create a:

- **Heavy Items** class to automatically add an extra fee to an order.
- **Fragile Goods** class to cover the cost of special handling and packaging.

This guide explains how to use Shipping Classes to group products with similar shipping needs, allowing you to apply special shipping rules to them.

## How to Add and Manage Shipping Classes [​](https://docs.fluentcart.com/guide/shipping/understanding-shipping-classes\#how-to-add-and-manage-shipping-classes)

1. **Navigate to Shipping Classes**:

   - From your WordPress dashboard, go to **FluentCart** \> **Settings**.
   - Click on the **Shipping** tab.
   - Select the **Shipping Classes** sub-tab.
2. **Add a New Shipping Class**:


   - Click the **"Add Shipping Class"** button.

![Screenshot of Shipping Classes](https://docs.fluentcart.com/images/shipping/understanding-shipping-classes/shipping-classes-1.webp)

3. **Define Class Details**:

   - **Class Name**: Give your shipping class a descriptive name (e.g., "Bulky Items").
   - **Cost**: Enter the numerical value for the additional cost associated with this class. This is an _adjustment_ that will be added to the base shipping method cost.
   - **Cost Type**: This defines how the "Cost Adjustment" is applied:
     - **Percentage**: The " **Cost Adjustment**" will be applied by percentage.
     - **Fixed Amount**: The " **Cost Adjustment**" will be applied by a fix amount.
   - **Apply to Qunatity**: Select this checkbox if you want the class to add per item charge if the buyer has multiple item of this product in the cart.
4. **Save the Shipping Class**:


   - Click the **"Save"** or **"Add Class"** button.

![Screenshot of Shipping Classes](https://docs.fluentcart.com/images/shipping/understanding-shipping-classes/shipping-classes-2.webp)

## Assigning Shipping Classes to Products [​](https://docs.fluentcart.com/guide/shipping/understanding-shipping-classes\#assigning-shipping-classes-to-products)

Once you have created your shipping classes, you need to assign them to your products.

1. **Edit a Product**:

   - Go to **FluentCart** \> **Products**.
   - Edit an existing product or create a new one.
2. **Select Shipping Class**:

   - On the product editing page, locate the **"Shipping Class"** dropdown or selector (usually under a "Shipping" or "Product Data" tab).
   - Choose the appropriate shipping class from the list.
3. **Update Product**:

   - Save your product to apply the assigned shipping class.

**Important Notes**:

- The actual final shipping cost will combine the shipping method's base rate with these shipping class adjustments, and then apply the "Class Aggregation" rule defined in the shipping method.

Today

Hi! I’m your AI assistant. How can I assist you today?

Just now

Powered by **FluentBot**

---
