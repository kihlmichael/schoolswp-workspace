---
source_url: https://surecart.com/docs/initial-troubleshooting
source: surecart-kb
scraped: true
---

# SureCart Troubleshooting Guide: Resolve Common Issues Quickly and Easily

While we're always ready to help you with anything that you need help with by opening a ticket, before reaching out for support, try these quick troubleshooting steps to resolve common SureCart issues.

These simple steps can solve up to 80% of common problems, saving you time and getting you back to using SureCart smoothly.

These steps can help with issues related to:

- **Display and layout:** How SureCart appears on your WordPress site.
- **Browser errors:** Issues specific to your web browser.
- **Functionality:** Any problem with how SureCart functions on your site.

## Initial Troubleshooting Steps:

1. **Check Troubleshooting Guides:** We have identified the most common issues our customers face. You can see them on the **Troubleshooting** category.
2. **Update SureCart:** Ensure you're using the latest version for optimal performance.
3. **Clear Cache:** Clear your browser cache, cookies, and WordPress site cache to eliminate temporary data causing conflicts.
4. **Clear SureCart Account Cache:** You can try to clear your SureCart account cache by going to SureCart > Settings and clicking on the "Clear Account Cache" in the top-right corner.
5. **Try a different browser/device:** Rule out browser-specific issues.
6. **Disable caching on SureCart pages (if applicable):** If you use caching plugins, exclude SureCart pages and sections to prevent conflicts.
7. **Check for plugin conflicts:** Temporarily disable other plugins one by one to identify potential conflicts with SureCart. Do the same with your theme if necessary.
8. **Verify required pages:** Ensure essential pages like Shop, Checkout, Customer Dashboard, and Cart are not deleted or trashed. Restore them if needed.
9. **Recreate products/forms (if issue is specific):** If only one product or form has issues, try recreating it instead of duplicating.
10. **Customize CSS (optional):** Refer to SureCart's guide for proper CSS customization using ShadowDOM.
11. **Address translation issues:** Use the LocoTranslate plugin and follow SureCart's translation guide.
12. **Review settings:** Check related settings in SureCart and other plugins for potential conflicts.

**Remember**: Try steps one at a time, checking if the issue persists after each step to isolate the problem. Make minimal changes to your site to avoid causing further issues.

## Payment Issues and External Connections:

### **Refresh or Reconnect Payment Processors:**

- Go to your **SureCart App Dashboard** > **Settings** > **Payments**.
- Choose to **refresh** or **disconnect and reconnect** your payment processors if you're experiencing checkout issues.

### **Try Different Payment Processors:**

- Connect a different payment processor to see if the problem persists. This helps determine if the issue is specific to a processor or SureCart.

### **Verify Payment Processor Account:**

- Double-check that you've connected the **correct account** within your payment processor platform. Some platforms allow switching accounts, so ensure you're using the intended one.

### **Verify Connected SureCart Shop:**

- Ensure you've connected the **correct SureCart Shop** from the dashboard to your WordPress site.
- If you suspect an incorrect connection, simply **reconnect the Secret Token** on your WordPress site.

## Troubleshooting Advanced Issues

For issues related to webhooks, API, and other advanced functionalities:

**Resync Webhooks (for webhook failures):**

- Go to your **WordPress site** > **SureCart** > **Settings** > **Connection** > **Advanced Options**.
- Click on "**Resync Webhooks**".
- Return to your **SureCart Dashboard** and **retry the webhooks** to see if the issue persists.
