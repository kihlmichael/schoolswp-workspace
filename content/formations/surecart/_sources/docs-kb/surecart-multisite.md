---
source_url: https://surecart.com/docs/surecart-multisite
source: surecart-kb
scraped: true
---

# Using SureCart on a WordPress Multisite

Setting up SureCart on a WordPress Multisite can be a little different compared to a normal WordPress site. To make sure it works perfectly, you'll need to follow a few key steps.

### Recommended Setup

The first thing to know is that SureCart works best with a **subdomain-based Multisite setup**. This means your sites will look like "store.example.com", not "example.com/store".

SureCart is designed to run independently on each subsite. If you try using a subfolder-based multisite or activate the plugin across the entire network, it can lead to conflicts or unexpected issues.

You should also **avoid network activating SureCart**. Instead, only activate the plugin on the specific subsite where you plan to run your store.

### What to Do If You're Using a Subfolder-Based Multisite or Already Activated SureCart on the Network

If you've already set up your multisite using subfolders (e.g., "example.com/store") or activated SureCart network-wide, follow these steps:

- **Switch to a Subdomain Setup**: First, you must convert your Multisite setup from subfolders to subdomains. WordPress has plenty of guides to help you make the switch.
- **Deactivate SureCart from the Network**: Once you've updated to a subdomain-based setup, log in to the Network Admin area and deactivate SureCart from the entire network.
- **Clean Up Unnecessary Pages**: SureCart might have created pages like the **Customer Dashboard** and **Checkout page** on the main site or other subsites. You should delete these to prevent any leftover configuration issues.
- **Reactivate SureCart Only Where Needed**: Go to the specific subsite where you want the store and activate SureCart there only.

### Why Does All This Matter?

SureCart is built to work in a specific way for Multisites. When you stick to a subdomain setup and activate the plugin only on the store subsite, you'll avoid configuration problems, plugin conflicts, and unexpected errors.

If you don't follow these steps, you might notice issues like pages not working correctly, features behaving oddly, or even the store not loading as expected.
