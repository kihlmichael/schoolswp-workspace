---
source_url: https://surecart.com/docs/manage-customer-orders
source: surecart-kb
scraped: true
---

/ [Knowledge Base](https://surecart.com/docs/)/ [Orders](https://surecart.com/docs-category/orders/)/How to Manage Customer Orders with SureCart

# How to Manage Customer Orders with SureCart

## How to Find Your Orders

Navigate to **WordPress Dashboard → SureCart → Orders** to see the list of all orders.

## How to Sort & Look for Orders Based on Status

Use the filter at the top left corner to sort by: All, Paid, Processing, Failed, and Canceled. Additional filters for Fulfillment status and Shipment Status are also available.

## How to Search for a Specific Order

Search for any specific order using the order ID.

## How to See All Details of a Single Order

Click on any order to access detailed options including:

- **Fulfillment Status, Order Status, & Order Receipts/Invoice** — order number, creation date, payment status, fulfillment status. Download receipt or invoice from here.
- **Customer Details, Shipping & Tax information, & Purchases** — customer name, shipping/tax address, and purchased products.
- **Orders Under Processing** — manually created orders not yet paid will show a Processing section.
- **Subscription Details** — shows status (Active, Canceled, Paused), product name, renewal date, and creation date.

## How to Cancel an Order

Click the **Actions** button on the top right corner, then choose **Cancel Order**. Canceling prevents the customer from accessing the product, downloading files, or continuing subscriptions linked to it.

## How to Refund an Order

In the Charge section, click the refund button to issue a refund.

## How to Revoke an Order

In the Purchases section, click the **Revoke** button to cancel the purchase and any related subscriptions. This also removes access to LMS courses and download files.

## **How to Add or Update Additional Order Data**

SureCart allows editing order metadata from the **Edit Order** page using a JSON editor.

1. Go to **WordPress Dashboard → SureCart → Orders**.
2. Click the order to update.
3. Scroll to the **Additional Order Data** section.
4. Click **Add Custom Data**.
5. Enter valid JSON format:

```json
{
  "reference_number": "ABC-123"
}
```

6. Click **Save**.

### Limitations When Editing Metadata

- Existing metadata **cannot be removed** — only **updated or cleared**.
- The platform **merges** new metadata with existing data.

**Workarounds to clear a value:**

```json
{ "roles": [] }
{ "roles": false }
{ "roles": "" }
```

## **Notes and Limitations**

- Canceling or revoking an order may affect customer access to digital products, downloads, subscriptions, or connected LMS content.
- Additional Order Data is merged with existing metadata and cannot be fully removed once saved.
- Some actions (refunds, cancellations) depend on the connected payment processor's capabilities.
