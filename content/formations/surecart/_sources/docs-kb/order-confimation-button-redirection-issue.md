---
source_url: https://surecart.com/docs/order-confimation-button-redirection-issue
source: surecart-kb
scraped: true
---

# Order Confirmation Button is Redirecting Users to the Homepage

## Issue Description

When customers complete a purchase and click the confirmation button in their email, they are redirected to the homepage instead of accessing the SureCart Customer Dashboard. This commonly occurs when using SEO plugins like RankMath.

## Solution

### Step 1: Verify Store URL Configuration

Navigate to **SureCart > Settings > Store Settings** and confirm the store URL is correctly mapped.

### Step 2: Access RankMath Settings

Open RankMath and click on General Settings.

### Step 3: Locate Redirections Tab

Scroll down to find the Redirections section.

### Step 4: Adjust Fallback Behavior

Change the FallBack Behaviour setting from "Homepage" to "Default 404 page."

### Step 5: Test and Save

Save your changes and test the order confirmation button again to verify proper functionality.

## Important Note

If you do not have RankMath installed but still experience this issue, review the redirection settings in whatever SEO plugin you are using, as similar redirect rules may apply.

## Additional Support

If the problem persists after following these steps, contact the SureCart Support Portal for further assistance.
