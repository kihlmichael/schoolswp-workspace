---
source_url: https://surecart.com/docs/surecart-abilities
source: surecart-kb
scraped: true
---

/ [Knowledge Base](https://surecart.com/docs/)/ [Integrations](https://surecart.com/docs-category/integrations/)/How to Get the Most Out of SureCart Abilities

# How to Get the Most Out of SureCart Abilities

This document explains how to use SureCart Abilities effectively to manage a store through AI assistants like Claude, ChatGPT, Cursor, and others. With Abilities enabled, common store operations can be completed in a single conversational request.

## **Quick Setup Reminder**

Before using Abilities, the MCP Adapter must be installed and an AI client connected. The full setup is available at WordPress Dashboard → SureCart → Settings → MCP.

## **Why Use Abilities**

Many routine store tasks involve repetitive UI navigation. With Abilities, these same tasks can be completed by describing the goal in plain language to an AI assistant.

The biggest gains come from tasks that require:

- Multiple steps across different sections of the admin
- Searching or filtering through long lists
- Performing the same action on several records
- Combining data from different parts of the store

## **Practical Use Cases**

### **Use Case 1: Extending a Subscription Renewal Date**

```
Find the active subscription for customer@example.com and extend the renewal date by 7 days.
```

### **Use Case 2: Creating an Invoice for a Custom Order**

```
Create an invoice for John Doe (johndoe@example.com) for the
"Premium Course" product, due on 2026-06-15, and send it to him.
```

### **Use Case 3: Reviewing Recent Store Performance**

```
Show me my store performance for the last 30 days.
Include total revenue, active subscriptions, and the top 5 products by sales.
```

### **Use Case 4: Bulk Coupon Creation for a Campaign**

```
Create three Black Friday coupons:
- BF10 for 10% off, valid Nov 24-28, max 500 uses
- BF20 for 20% off, valid Nov 25-27, max 200 uses
- BF30 for 30% off, valid Nov 26 only, max 50 uses
```

### **Use Case 5: Issuing a Partial Refund**

```
Issue a 50% refund on the most recent order for customer@example.com
with the reason "partial product issue".
```

## **Tips for Better Results**

- **Be Specific with Identifiers** — use customer email, full product name, dates in YYYY-MM-DD format
- **State the Goal, Not the Steps** — describe the desired outcome rather than each step
- **Specify Variants** — for products with multiple variants, include the variant name
- **Confirm Before Destructive Actions** — add "and confirm before applying" for deletions/refunds

## **Permissions and Safety**

The MCP settings page includes three permission toggles:

- **Enable Abilities** — Master switch for all AI access
- **Enable Edit Abilities** — Allows creating and modifying data
- **Enable Delete Abilities** — Allows permanent deletion of data

## **Notes and Limitations**

- AI assistants follow the permissions configured in MCP settings.
- Multi-variant products require the variant to be specified in the prompt.
- Destructive actions (deletions, refunds, cancellations) typically prompt for confirmation before execution.
