---
source_url: https://surecart.com/docs/import-products-in-bulk
source: surecart-kb
scraped: true
---

# How to Import Products in Bulk With SureCart

## Overview

This guide walks you through importing products in bulk into SureCart using a CSV file. The process involves preparing your data file and uploading it through the SureCart platform.

## Important Notes

Migrating an eCommerce platform is a technical process and may require developer expertise, especially when dealing with custom setups or non-standard configurations.

SureCart support assists with documentation and product functionality questions. Hands-on migration work remains the responsibility of store owners or their developers.

## Preparing Your CSV File

### Download Template

Access the sample CSV file at: `https://app.surecart.com/imports/products/template.csv`

### Required Fields

The following fields are mandatory:

- **Slug** - unique identifier for URLs
- **Name** - product title
- **Currency** - ISO code (USD, EUR, etc.)
- **Amount** - price in minor units (e.g., $9.90 = 990)

### Field Reference Table

| Field               | Type     | Example      | Notes                               |
| ------------------- | -------- | ------------ | ----------------------------------- |
| Slug                | Text     | product-name | Lowercase, hyphens/underscores only |
| Name                | Text     | My Product   | Product title                       |
| Currency            | ISO Text | USD          | Currency code                       |
| Amount              | Integer  | 990          | Minor units (cents)                 |
| Description         | Text     | Brief text   | Supports basic formatting           |
| Status              | Text     | published    | Current product state               |
| Recurring Interval  | Text     | month        | Subscription frequency              |
| Trial Duration Days | Integer  | 14           | Days for trial period               |
| Shipping Enabled    | Boolean  | true/false   | Physical product shipping           |
| Tax Enabled         | Boolean  | true/false   | Apply taxes                         |
| metadata.tag        | Text     | summer-sale  | Custom tags, comma-separated        |

### CSV Preparation Tips

- Match your data column headers to template headers exactly
- Use lowercase letters, numbers, hyphens, and underscores only
- Avoid special characters in slug and metadata fields
- Place all product information in appropriate columns

## Import Process

### Step-by-Step Instructions

1. **Access Imports Menu** - Log into SureCart platform and click Imports
2. **Create New Import** - Click "New Import" button
3. **Select Products** - Choose "Products" from dropdown
4. **Download Template** - Click template CSV file link (optional reference)
5. **Upload File** - Drag and drop CSV or browse to select file
6. **Start Import** - Click Import button
7. **Monitor Status** - Status displays as "Pending" then "Completed"
8. **Verify Results** - Click status or rows to view detailed import information
9. **Access Products** - Find imported items in Products menu dashboard
10. **Enhance Data** - Add images, adjust status, and make final edits

### Processing Time

For small data sets with less than 1000 rows, it usually takes less than a minute. Email notification confirms when import completes.

## Post-Import Tasks

After successful import, enhance your products by:

- Adding product images
- Adjusting product status
- Creating product descriptions (rich formatting)
- Setting up variants and pricing options
- Configuring shipping and tax settings

## Metadata Import Feature

Custom metadata attributes can be imported using column headers with the `metadata.` prefix.

**Example columns:**

- `metadata.tag`
- `metadata.color`
- `metadata.collection`

Multiple tags can be assigned in a single field separated by commas.

## FAQ

**Q: What is the metadata import feature?**
Metadata allows importing custom attributes alongside products via CSV columns using the `metadata.` naming convention.

**Q: How do I add metadata fields?**
Add columns using format: `metadata.FieldName`. Each column becomes a custom attribute on the product.

**Q: Can I include multiple tags?**
Yes. Multiple tags in metadata.tag can be separated by commas within a single cell.
