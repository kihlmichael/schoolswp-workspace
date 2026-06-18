---
source_url: https://surecart.com/docs/plugin-performance
source: surecart-kb
scraped: true
---

/ [Knowledge Base](https://surecart.com/docs/)/ [Settings](https://surecart.com/docs-category/settings/)/How to Change Your Plugin Performance Settings

# How to Change Your Plugin Performance Settings

If you aim to increase the load speed for products, shop, and checkout pages on your SureCart website, this guide is for you.

We're going to head into your WordPress to tweak some settings. Additionally, we'll guide you on integrating JavaScript with certain CDN providers where JavaScript is not enabled by default.

Let's get started!

### How to enable Plugin Performance in the SureCart Settings

In your WordPress website, within SureCart settings, you have the option to change the SureCart plugin performance by enabling the JavaScript ESM loader.

This JavaScript ESM loader is a tool or a method that enables loading and executing ECMA Script modules (ESM) in JavaScript environments. ESM has several benefits over the traditional CommonJS (CJS) modules, such as better performance, tree-shaking, and native browser support.

So, to enable this option in SureCart, follow the steps below:

- Go to the WordPress dashboard, and from SureCart, click on Settings.

- Click on the Advanced Tab.

- From the Performance section, toggle on the Use JavaScript ESM Loader and click on "Save" button.

After turning the ESM loader on, make sure to test your checkout forms in a private window on your browser. Because of browser caching, changes may not be applied immediately.

### How to Enable CORS Headers for JavaScript in Bunny.Net CDN

CORS headers, or Cross-Origin Resource Sharing headers, are HTTP headers used by web servers to define which origins (websites) are permitted to access a resource on a server. They provide a way for servers to overcome the default restrictions placed by the same-origin policy, a security measure that prevents web pages from making requests to a different domain than the one that served the web page. In essence, CORS headers allow web servers to specify who can access their resources and under what conditions, facilitating secure cross-origin requests in web applications.

Under the toggle switch of "Use JavaScript ESM loader" option, you can see a small note:

_This can slightly increase page load speed, but may require you to enable CORS headers for .js files on your CDN. Please check your checkout forms after you enable this option in a private browser window._

In the case of Cloudflare, JavaScript is pre-configured in the CORS headers. However, with certain CDNs, you must manually add the JavaScript in the CORS headers.

We'll take the example of Bunny CDN, where JavaScript is not automatically incorporated. It must be added to ensure the efficient working of the SureCart Performance – JavaScript ESM loader.

To add JavaScript to Bunny CDN's CORS headers, follow these steps.

- Log into your account from [Bunny CDN.](https://bunny.net/)

- Select the CDN tab and then click on the pull zones for which your website has been configured.

- Click on the Headers tab.

- Write "js" in the Extension List field, separated by a comma, and click the "Save" button to save the changes.

And that's it! This is how you can add CORS headers for JavaScript in Bunny.Net CDN.

We don't provide documentation for every CDN on adding JavaScript in CORS Headers; however, the process remains the same. You simply need to add ".js" to CORS headers in your CDN.

And if you get stuck, you can contact your CDN provider support for assistance.

Hope this helps you improve your website performance.

If you have any questions, do not hesitate to contact us!
