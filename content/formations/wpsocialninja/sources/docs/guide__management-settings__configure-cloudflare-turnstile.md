---
source_url: "https://docs.wpsocialninja.com/guide/management-settings/configure-cloudflare-turnstile.html"
title: "Configure Cloudflare Turnstile | WP Social Ninja"
---

# Configure Cloudflare Turnstile | WP Social Ninja

WP Social Ninja now supports **Cloudflare Turnstile**, a user-friendly, privacy-focused alternative to traditional CAPTCHAs. This feature ensures your **Native Review Forms** remain protected from spam bots without requiring visitors to solve complex puzzles.

Follow these steps to set up and enable Turnstile on your website.

## Step 1: Generate Keys in Cloudflare [​](https://docs.wpsocialninja.com/guide/management-settings/configure-cloudflare-turnstile#step-1-generate-keys-in-cloudflare)

Before configuring the plugin, you must obtain your unique API keys from your Cloudflare account.

1.  Log in to your [Cloudflare dashboard](https://dash.cloudflare.com/login) and navigate to the **Turnstile** section under **Application Security**.
2.  Click **\+ Add Widget**.

![Add Widget](https://docs.wpsocialninja.com/assets/add-widget-1.CNm8w4HH.webp)

3.  Enter a **Widget Name** to identify it in the future.
4.  Click **\+ Add Hostnames** and enter your website’s domain (e.g., `crm-test-march08.wp1.site`).

![Hostnames](https://docs.wpsocialninja.com/assets/add-hostanme-2.UzIFFkSC.webp)

5.  Click **Add** and then **Add** again to confirm.

![Add](https://docs.wpsocialninja.com/assets/add-3.CzIA2nk2.webp)

6.  Select your preferred **Widget Mode**:
    *   **Managed (Recommended):** Cloudflare decides the best verification method based on traffic risk.
    *   **Non-interactive:** Shows a loading spinner; no user interaction is required.
    *   **Invisible:** Verification happens silently without any visual indication on the screen.
7.  Click **Create** to generate your **Site Key** and **Secret Key** and **Copy** these key.

![Create](https://docs.wpsocialninja.com/assets/create-4.BbHEZL9T.webp)

## Step 2: Configure Turnstile in WP Social Ninja [​](https://docs.wpsocialninja.com/guide/management-settings/configure-cloudflare-turnstile#step-2-configure-turnstile-in-wp-social-ninja)

Once you have your keys, you need to validate them within the plugin's global settings.

1.  From your WordPress dashboard, go to **WP Social Ninja → Settings → Reviews Platforms → Global Review Settings**.
2.  Locate the **Native Form CAPTCHA Settings** section.
3.  Paste your **Site Key** and **Secret Key** into the designated fields.
4.  Choose the **Theme** (Auto, Light, or Dark) and the **Appearance** (Managed, Always, or Interaction Only) for the widget.
5.  Complete the **Validation Preview** challenge to verify the keys are working.
6.  Once the status shows **"Turnstile settings validated and saved successfully,"** click **Validate & Save**.

![Configure Turnstile in WP Social Ninja](https://docs.wpsocialninja.com/assets/native-form-capcha-settings-5.AVN9v-6i.webp)

## Step 3: Enable Turnstile on Your Review Form [​](https://docs.wpsocialninja.com/guide/management-settings/configure-cloudflare-turnstile#step-3-enable-turnstile-on-your-review-form)

After the global configuration is complete, you must enable the protection on your individual forms.

1.  Go to **WP Social Ninja → [Review Forms](https://docs.wpsocialninja.com/guide/business-reviews/native-review-forms)** and open the form you wish to protect.
2.  In the right-hand editor panel, navigate to **General → Spam Protection**.
3.  Select **Turnstile** from the **CAPTCHA** dropdown menu.
4.  You will see a note confirming that **"Turnstile keys are managed from Global Review Settings"**.
5.  Click the **Save** button at the top right of the form builder to apply the changes.

![Review Form](https://docs.wpsocialninja.com/assets/turnstile-6.CQSEQuUv.webp)

NOTE

If you ever need to update your keys or change providers, you can click the **Turnstile Settings** link within the form builder to jump directly back to the global configuration page.
