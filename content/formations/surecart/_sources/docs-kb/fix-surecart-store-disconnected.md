---
source_url: https://surecart.com/docs/fix-surecart-store-disconnected
source: surecart-kb
scraped: true
---

# Fix – SureCart store disconnected

There are some situations when the SureCart store is often disconnected from the website. This can happen if you have a plugin that is regenerating WordPress salts – we use this salt to securely store the API token in the database (so it's not in clear text). However, regenerating WordPress salts will cause a disconnection. Often this is caused by security plugins.

The fix is to add a line to your wp-config.php file that will hard-code your api token there. Can you add this:

```
define( 'SURECART_API_TOKEN', 'your_api_token' );
```

Make sure it's above this line:

```
/* That's all, stop editing! Happy publishing. */
```
