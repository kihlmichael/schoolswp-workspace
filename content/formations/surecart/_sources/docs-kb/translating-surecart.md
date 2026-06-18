---
source_url: https://surecart.com/docs/translating-surecart
source: surecart-kb
scraped: true
---

/ [Knowledge Base](https://surecart.com/docs/)/ [Localization](https://surecart.com/docs-category/localization/)/How to Translate SureCart in Your Own Language

# How to Translate SureCart in Your Own Language

SureCart is 100% translation-ready and comes with .po / .mo files and also can be translated to any language that you want using software such as LocoTranslate or Poedit.

You can translate the words you see in the SureCart plugin on two sides of your store:

- The parts that you see as a customer on the Customer Dashboard or the Checkout page.
- The parts that are only seen by you as store owner on the Product Page, Subscriptions, and Settings.

So let's say you are looking to translate the texts on the checkout page to a different language from English, you can do that using any of the two methods mentioned in the article.

Let's understand both these methods!

### **Method 1: Using Loco Translate**

SureCart allows translating almost every text/string without much of an effort.

Let's see how LocoTranslate can help us with the process.

- Firstly, you need to install the Loco Translate plugin from the Plugins page > Add New.

- Upon installation, visit the Loco Translate Plugins and choose the SureCart option from the list to translate.

- Now, under the Overview tab, click on New Language.

- Here, select the language you want and set the location to **Custom**. Click on the "Start translating" button once you've made these changes.

- Now, you will be taken to the editor page. Loco Translate will fetch all the words and phrases that you can be translated and you can set the translation manually.

- Save the Translations, and view the text/string on the Instant Checkout page to see how your translation looks.

- Once the strings are translated, please make sure you clear the cache on your website and check the updated text/string on the front end.

That's it!

We were able to translate a text on the SureCart checkout form using the Loco Translate plugin.

### Method 2: Using The .pot File

The SureCart plugin provides a platform for String Translation for our users.

Our developers pull in all the validated translations once they reach above 80% on the platform during every plugin update.

If you are interested in helping us translate SureCart in any of your desired languages, please feel free to write to our [support team](https://surecart.com/support/open-a-ticket/).

Now, coming to the translation of strings using the .pot file, please follow these steps:

- Download the [SureCart plugin](https://wordpress.org/plugins/surecart/) on your computer. Next, double-click on the plugin zip file to extract it.
- Click on the plugin folder and look for the Languages folder.

- Under the Languages folder, you will find the surecart.pot file at the top of the folder. We will need this .pot file after installing the Poedit plugin on your system.

- Now, you will be required to install the [**Poedit app**](https://poedit.net/download) on your computer, you can find a free version for Windows and Mac.
- Upon installation, you will notice the application's home screen. Click on the **Create New** button.

- Here you will be redirected to the computer's file manager. Select the .pot file of the SureCart plugin which we found under the Languages folder.

- Choose the language you want to translate to from the dropdown menu. Click on the Ok button.

Now, Poedit will display all the text/strings as Source Text available for translation.

- Click or search using Ctrl+F for the string you want to translate and provide the Translation text in the Translation field.

- Once you are done translating the texts/strings, you can save the file using the Save button under the File menu at the top-left of the screen.

Here, it is important to note that, you have to save your file after the language name and country code.

Be sure to prefix the text domain before the [language code](https://wpastra.com/docs/complete-list-wordpress-locale-codes/). Also, capitalize the file name correctly as it is important here.

For language codes, please [refer to](https://wpastra.com/docs/complete-list-wordpress-locale-codes/) this list. And text domain can be found in the style.css file of the theme, or the main PHP file of the plugin.

Examples of file names for the SureCart plugin:

- For German: "surecart-de_DE.po" & "surecart-de_DE.mo"
- For French: "surecart-fr_FR.po" & "surecart-fr_FR.mo"

Note, that Poedit will save your files as .po and .mo files.

- Next, we simply need to place these files in the **/wp-content/languages/** directory. As we do not want to lose all the translations and edits we have done, we will upload the file in the above-mentioned folder on your computer.

By following the above steps, you will be able to successfully translate the strings/text in the SureCart.

We ensure all the texts in SureCart are made translatable, if you notice any of the texts are missing, please feel free to drop us a message using the below support.

If you still have any questions, please feel free to write to us via our [Support form](https://surecart.com/support/open-a-ticket/).
