---
source_url: https://surecart.com/docs/filter-and-display-featured-products
source: surecart-kb
scraped: true
---

# How to Filter and Display Featured Products - SureCart

## Overview

This guide demonstrates how to use Bricks Builder to filter and display only featured SureCart products through query loop configuration.

## Steps

### 1. Enable Query Loop

In the Bricks Builder editor, toggle on the "Query loop" feature to allow dynamic filtering of product posts.

### 2. Select Post Type

Set "Post Type" to "SureCart Product" to ensure the loop retrieves SureCart products rather than standard WordPress posts.

### 3. Add Meta Query

- Locate "Meta Query" under the "Posts" query settings
- Click "+ Add Meta Query" to add a new filtering condition

### 4. Configure Meta Query Settings

Enter the following configuration to filter featured products:
- **Meta key:** featured
- **Meta value:** 1
- **Compare:** Equal
- **Type:** CHAR (or auto-detect if available)

### 5. Save and Test

- Save your changes in the editor
- Preview or check the live page to confirm only products marked as featured display correctly

## Result

The query loop will now display exclusively products with featured metadata set to 1, allowing you to highlight specific items in your store.

## Additional Resources

- Dynamic Data documentation for Bricks Builder
- SureCart Custom Fields customization options
