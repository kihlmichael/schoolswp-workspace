---
source_url: https://surecart.com/docs/enable-upsell-funnels
source: surecart-kb
scraped: true
---

# How to Enable Upsell Funnels in SureCart

SureCart enables merchants to implement upsells to convince customers to purchase higher-tier product versions, increasing average order value.

## Upsells vs. Order Bumps

- **Upsells**: Offer pricier upgrades after checkout
- **Order Bumps**: Suggest product bundles during checkout

## Adding Upsell Funnels

1. Navigate to **SureCart > Products > Upsells**
2. Click **Add new** and name your upsell (internal name only, not visible to customers)

## Display Conditions

**Options:**
- Show after all product purchases
- Show after specific purchases only

**For Specific Purchases:**
- Click **Add A Condition**
- Select products by name or price from dropdown
- Add multiple conditions as needed

**Show Upsell Offer If** settings (for multiple cart items):
- **All of these are in the cart**: Upsell displays only if all selected products are present
- **Any of these items are in the cart**: Upsell displays if any selected item exists
- **None of these items are in the cart**: Upsell displays only if none are present

## Post Purchase Offer Section

Three components:

1. **Upsell Offer #1**: First upsell customers see after purchase
2. **Upsell Offer #2**: Secondary offer if customer accepts first upsell
3. **Downsell Offer**: Lower-priced alternative if customer rejects first upsell

## Customizing Upsell Offers

### Choose Upsell Title And Product

- Name the upsell (displays to customers at page top)
- Select product from dropdown or search bar

### Upsell Behavior

- **Skip if in order**: Don't show upsell if item already in customer's cart
- **Skip if purchased**: Don't display if customer previously purchased this item
- **Always show**: Display regardless of cart contents or purchase history

### Add To or Replace The Entire Order

**Add to the order:**
- Upsell adds on top of existing order; all previously selected products remain
- Example: T-shirt + hat upsell = cart contains T-shirt + hat

**Replace the entire order:**
- Upsell completely replaces customer's order; all existing cart items removed
- Example: Basic Plan replaced by Pro Plan upsell = cart contains only Pro Plan
- Note: Removes ALL items regardless of quantity

**When to use each:**
- Use **Add to order** to increase order value through product stacking
- Use **Replace entire order** for clear upgrades or alternatives (monthly to annual plan)

### Design The Upsell Offer

- Click **Edit** to customize default upsell template
- All elements are editable: countdown logo, CTA title, product media, typography
- Countdown Timer default: 30 minutes (adjustable)
- Click **Create Offer** to finalize

## Adjusting Upsell Priority

- Rating scale: 1 (lowest priority) to 5 (highest priority)
- When multiple upsells target same product, only highest priority displays

Click **Save Funnel** to apply all changes.

## Troubleshooting: Payment Method Compatibility with Mollie

**Issue:** iDEAL and Bancontact don't appear during checkout when upsell funnels are enabled.

**Reason:** Upsell funnels require payment methods supporting one-click/reusable payment intents. iDEAL and Bancontact support only one-time purchases.

**Solutions:**
- Business dependent on iDEAL/Bancontact: don't use upsell funnels for those products
- For recurring/upsell funnels: use reusable payment intent methods (credit cards, SEPA Direct Debit)

## Frequently Asked Questions

**Q: What happens to payment methods when upsell funnels are active?**
A: Only reusable payment methods display at checkout. SureCart automatically manages compatibility.

**Q: Why isn't my preferred payment method showing?**
A: Payment methods lacking reusable payment support won't appear in checkout containing active upsell funnels.
