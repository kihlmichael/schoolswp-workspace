# Section Storage

Source : docs.fluentcart.com
Date scrape : 2026-05-19

---

## Storage in FluentCart - FluentCart Documentation
URL : https://docs.fluentcart.com/guide/storage/

[Skip to content](https://docs.fluentcart.com/guide/storage/#VPContent)

# Storage in FluentCart [​](https://docs.fluentcart.com/guide/storage/\#storage-in-fluentcart)

FluentCart ships with a built-in **Storage** layer that decides where your digital product files, downloadable assets, and related media are physically saved and served from. You can keep everything on your own server, or offload to a cloud storage provider for better performance, reliability, and scalability.

From your WordPress dashboard, you will find a dedicated **Storage** menu in the FluentCart sidebar, with a sub-menu for each supported cloud provider.

## Why Storage Matters [​](https://docs.fluentcart.com/guide/storage/\#why-storage-matters)

Every digital product you sell - a PDF, a software license archive, a video course file, a design asset - needs to live somewhere. The storage driver you choose here determines:

- **Where the file is stored** when it is uploaded (your server vs. a cloud bucket).
- **How the file is delivered** to the customer after purchase (direct from your server vs. served through the cloud provider).
- **How your site scales** as your file library grows (server disk vs. effectively unlimited cloud storage).

Digital Product Assets

When [creating or editing digital products](https://docs.fluentcart.com/guide/product-types-creation/creating-digital-products), the storage driver you configure here is where those downloadable files are actually saved.

## Supported Storage Providers [​](https://docs.fluentcart.com/guide/storage/\#supported-storage-providers)

FluentCart currently supports the following storage providers out of the box:

### Local Storage [​](https://docs.fluentcart.com/guide/storage/\#local-storage)

Files are saved directly on your website's server. This is the simplest option and is active by default, making it a good fit for smaller stores or early setups where files are light and traffic is manageable.

### Amazon S3 [​](https://docs.fluentcart.com/guide/storage/\#amazon-s3)

Amazon S3 is AWS's cloud object storage - the industry standard for offloading large file libraries from your web server. Choose S3 if you sell large digital files, want to keep your site fast under load, or already live inside the AWS ecosystem.

[Read the full Amazon S3 setup guide →](https://docs.fluentcart.com/guide/storage/s3)

### Cloudflare R2 [​](https://docs.fluentcart.com/guide/storage/\#cloudflare-r2)

Cloudflare R2 is Cloudflare's object storage - S3-compatible at the API level, but delivered through Cloudflare's global network with **zero egress fees**. Choose R2 if you have media-heavy downloads, international customers, or want predictable costs as traffic grows.

[Read the full Cloudflare R2 setup guide →](https://docs.fluentcart.com/guide/storage/r2)

## Provider List, Enable / Disable, and Edit [​](https://docs.fluentcart.com/guide/storage/\#provider-list-enable-disable-and-edit)

Inside the **Storage** menu, each provider is listed as a card with:

- An **Active / Inactive** toggle - flip a provider on or off without losing its configuration.
- An **Edit** button - update credentials, swap the bucket, or adjust security settings any time.
- A **connection status** banner once connected, with a **Check again** action to re-verify the connection on demand.

You can configure multiple providers and switch the active one as your needs change.

## Security Model [​](https://docs.fluentcart.com/guide/storage/\#security-model)

FluentCart takes credential safety seriously. Both S3 and R2 let you pick how credentials are stored:

- **Define in `wp-config.php`** _(Recommended)_ - keys live in your WordPress configuration file, never in the database. The UI detects the constants and locks the credential fields so nothing overrides them from the admin.
- **Store in the database** - available when you need UI-only configuration, with an explicit acknowledgement of the reduced security posture.

For Amazon S3, a dedicated **Security step** additionally lets you enforce _Block All Public Access_ and _Object Ownership_ on your bucket.

## Saving Changes [​](https://docs.fluentcart.com/guide/storage/\#saving-changes)

After any change to your Storage configuration, click the relevant **Save** button (`Save & Continue`, `Save Selected Bucket`, `Create New Bucket`, or `Save Settings`) to apply the change. FluentCart will verify the connection where applicable before marking the provider as connected.

Today

Hi! I’m your AI assistant. How can I assist you today?

Just now

Powered by **FluentBot**

---

## Amazon S3 - FluentCart Documentation
URL : https://docs.fluentcart.com/guide/storage/aws-s3

[Skip to content](https://docs.fluentcart.com/guide/storage/aws-s3#VPContent)

# Amazon S3 [​](https://docs.fluentcart.com/guide/storage/aws-s3\#amazon-s3)

Amazon S3 (Simple Storage Service) is AWS's cloud object storage service. Connecting S3 to FluentCart offloads your digital product files from your own web server into a dedicated, highly durable, globally available storage layer. Your site stays fast, your downloadable files stay safe, and your storage scales effectively without limit.

This guide walks you through the full setup - from getting AWS credentials, to picking or creating a bucket, to locking the bucket down with the right security settings.

## Obtaining AWS Access Keys [​](https://docs.fluentcart.com/guide/storage/aws-s3\#obtaining-aws-access-keys)

Before you open the FluentCart Storage screen, create a pair of S3 access keys in AWS. The walkthrough below uses the current (2026) AWS console layout and produces a dedicated IAM user scoped just for FluentCart - so you can rotate or revoke its keys any time without affecting the rest of your AWS account.

> **Already have access keys?** Skip this section and jump to [Accessing Amazon S3 Settings](https://docs.fluentcart.com/guide/storage/aws-s3#accessing-amazon-s3-settings).

### 1\. Open IAM and Start a New User [​](https://docs.fluentcart.com/guide/storage/aws-s3\#_1-open-iam-and-start-a-new-user)

1. Log in to the [AWS Management Console](https://aws.amazon.com/console/).
2. In the top search bar, type **IAM** and open the service.
3. In the IAM sidebar, expand **Access Management** and click **Users**.
4. Click the **Create user** button in the top-right.

![AWS IAM - Users list with Create user highlighted](https://docs.fluentcart.com/images/storage/s3/aws-iam-users-list.webp)

> **Tip:** IAM is a global service - you do not need to pick a region for user creation.

### 2\. Specify User Details [​](https://docs.fluentcart.com/guide/storage/aws-s3\#_2-specify-user-details)

Give the new user a recognisable name (for example, `fluentcart-s3`). Leave **Provide user access to the AWS Management Console** **unchecked** - FluentCart only needs programmatic (API) access, not a console login. Click **Next**.

![AWS IAM - Specify user details with a programmatic-only user](https://docs.fluentcart.com/images/storage/s3/aws-user-details.webp)

> **Why no console access?** A dedicated API-only user reduces your attack surface. If the key ever leaks, the attacker cannot log into the AWS console with it.

### 3\. Attach the S3 Policy [​](https://docs.fluentcart.com/guide/storage/aws-s3\#_3-attach-the-s3-policy)

On the **Set permissions** screen:

1. Choose **Attach policies directly**.
2. In the **Permissions policies** search box, type `s3full`.
3. Tick the row for **AmazonS3FullAccess**.
4. Click **Next**.

![AWS IAM - Attach AmazonS3FullAccess policy directly](https://docs.fluentcart.com/images/storage/s3/aws-attach-policy.webp)

> **Security-conscious alternative:** instead of `AmazonS3FullAccess`, you can create a custom policy scoped to a single bucket ARN with only the actions FluentCart uses (`s3:ListAllMyBuckets`, `s3:ListBucket`, `s3:CreateBucket`, `s3:PutObject`, `s3:GetObject`, `s3:DeleteObject`, `s3:PutBucketPublicAccessBlock`, `s3:PutBucketOwnershipControls`). The managed policy is simpler and is what this guide assumes.

### 4\. Review and Create the User [​](https://docs.fluentcart.com/guide/storage/aws-s3\#_4-review-and-create-the-user)

Double-check the user name and the attached policy. Tags are optional - you can skip them. Click **Create user**.

![AWS IAM - Review and create the new IAM user](https://docs.fluentcart.com/images/storage/s3/aws-review-create.webp)

### 5\. Open the New User's Security Credentials [​](https://docs.fluentcart.com/guide/storage/aws-s3\#_5-open-the-new-user-s-security-credentials)

Back on the **Users** list, click the user you just created (`fluentcart-s3`). On the user details page, open the **Security credentials** tab, scroll down to the **Access keys** section, and click **Create access key**.

![AWS IAM - User security credentials with Create access key](https://docs.fluentcart.com/images/storage/s3/aws-security-credentials.webp)

### 6\. Pick a Use Case for the Access Key [​](https://docs.fluentcart.com/guide/storage/aws-s3\#_6-pick-a-use-case-for-the-access-key)

AWS asks what the key will be used for. Choose **Third-party service** (FluentCart is a third-party application calling the S3 API on your behalf). AWS will surface a best-practice reminder - tick **I understand the above recommendation and want to proceed to create an access key**, then click **Next**.

![AWS IAM - Access key use case: Third-party service](https://docs.fluentcart.com/images/storage/s3/aws-access-key-usecase.webp)

You can leave the optional **description tag** blank, or add something like `fluentcart-production` if you manage keys across several environments. Click **Create access key**.

### 7\. Copy the Access Key and Secret Access Key [​](https://docs.fluentcart.com/guide/storage/aws-s3\#_7-copy-the-access-key-and-secret-access-key)

AWS now shows both values:

- **Access key** - the public ID.
- **Secret access key** - the private half. Click **Show** to reveal it.

![AWS IAM - Retrieve access key and secret access key](https://docs.fluentcart.com/images/storage/s3/aws-retrieve-keys.webp)

The secret is shown **only once**

This is the only moment AWS will ever display the secret access key in cleartext. Either copy both values immediately into FluentCart, or click **Download .csv file** to store them safely. If you lose the secret, you cannot recover it - you will have to delete this access key and create a new one.

Once you have both values, click **Done**.

### Credentials Recap [​](https://docs.fluentcart.com/guide/storage/aws-s3\#credentials-recap)

| FluentCart field | AWS value | Source step |
| --- | --- | --- |
| **Access Key** | Access key | Step 7 |
| **Secret Key** | Secret access key | Step 7 |
| IAM user name | e.g. `fluentcart-s3` | Step 2 |
| Attached policy | `AmazonS3FullAccess` | Step 3 |

Keep the two keys handy - you will paste them into FluentCart in the next section.

* * *

## Accessing Amazon S3 Settings [​](https://docs.fluentcart.com/guide/storage/aws-s3\#accessing-amazon-s3-settings)

From your WordPress dashboard:

1. Go to **FluentCart → Storage**.
2. Click **Amazon S3** in the sub-menu.

You will land on the Amazon S3 configuration wizard. Setup is split into three steps:

1. **Credential** - how FluentCart will authenticate to AWS.
2. **Bucket** - which S3 bucket will hold your files.
3. **Security** - bucket-level protections against unintended public access.

* * *

## Step 1 - Credential [​](https://docs.fluentcart.com/guide/storage/aws-s3\#step-1-%E2%80%94-credential)

FluentCart supports two ways to supply your AWS access keys.

### Method A - Define Access Keys in `wp-config.php` (Recommended) [​](https://docs.fluentcart.com/guide/storage/aws-s3\#method-a-%E2%80%94-define-access-keys-in-wp-config-php-recommended)

This is the most secure option. Your keys live in your WordPress configuration file, never in the database, and are not readable from the admin UI.

![Amazon S3 - Define access keys in wp-config.php](https://docs.fluentcart.com/images/storage/s3/credential-define.webp)

Copy the snippet below **near the top** of your `wp-config.php` (before the `/* That's all, stop editing! */` line) and replace the placeholder values with your real AWS keys:

php

```
define( 'FCT_S3_ACCESS_KEY', 'your-access-key-id' );
define( 'FCT_S3_SECRET_KEY', 'your-secret-access-key' );
```

Once FluentCart detects these constants, the credential fields in the UI are automatically locked, and the Connection Method card will tell you the keys have been picked up from your `wp-config.php`.

> **Heads up:** to later switch to a different method here, comment out or remove the `FCT_S3_ACCESS_KEY` and `FCT_S3_SECRET_KEY` defines from `wp-config.php` and reload the page.

### Method B - Store Access Keys in the Database [​](https://docs.fluentcart.com/guide/storage/aws-s3\#method-b-%E2%80%94-store-access-keys-in-the-database)

Available when you need UI-only configuration. Keys are saved to the database, which is inherently less secure than a file-based constant - an acknowledgement is shown before you proceed.

![Amazon S3 - Store access keys in the database](https://docs.fluentcart.com/images/storage/s3/credential-db.webp)

Select **"I understand the risks but I'd like to store access keys in the database."** Then enter:

- **Access Key** - your AWS Access Key ID.
- **Secret Key** - your AWS Secret Access Key.

Click **Save & Continue** to move on to the bucket step.

> **No access keys yet?** Head back to [Obtaining AWS Access Keys](https://docs.fluentcart.com/guide/storage/aws-s3#obtaining-aws-access-keys) above for the full IAM walkthrough.

* * *

## Step 2 - Bucket [​](https://docs.fluentcart.com/guide/storage/aws-s3\#step-2-%E2%80%94-bucket)

An S3 **bucket** is a named storage container inside your AWS account. FluentCart gives you three ways to pick or create one.

### Option 1 - Use Existing Bucket, Entered Manually [​](https://docs.fluentcart.com/guide/storage/aws-s3\#option-1-%E2%80%94-use-existing-bucket-entered-manually)

If you already know the exact name of the bucket you want to use, type it directly.

![Amazon S3 - Enter bucket name manually](https://docs.fluentcart.com/images/storage/s3/bucket-existing-manual.webp)

1. Select **Use Existing Bucket**.
2. Choose **Enter bucket name**.
3. Type the bucket name and click **Save Selected Bucket**.

### Option 2 - Use Existing Bucket, Browse From AWS [​](https://docs.fluentcart.com/guide/storage/aws-s3\#option-2-%E2%80%94-use-existing-bucket-browse-from-aws)

FluentCart can fetch the list of buckets attached to the connected AWS account so you can pick from a dropdown - no copy-pasting names, no typos.

![Amazon S3 - Browse existing buckets](https://docs.fluentcart.com/images/storage/s3/bucket-existing-browse.webp)

1. Select **Use Existing Bucket**.
2. Choose **Browse existing buckets**.
3. Click the refresh icon if you do not see a bucket you just created.
4. Click the bucket you want and click **Save Selected Bucket**.

### Option 3 - Create a New Bucket From the UI [​](https://docs.fluentcart.com/guide/storage/aws-s3\#option-3-%E2%80%94-create-a-new-bucket-from-the-ui)

No need to switch to the AWS console. FluentCart can create a fresh S3 bucket in the region you pick.

![Amazon S3 - Create a new bucket](https://docs.fluentcart.com/images/storage/s3/bucket-create-new.webp)

1. Select **Create New Bucket**.
2. Enter a **Bucket Name**. Bucket names must be unique across **all of AWS globally**, follow DNS-style naming (lowercase letters, numbers, hyphens), and cannot be reused after deletion for a while.
3. Choose a **Region** - pick the one geographically closest to most of your customers (for example, **US East (N. Virginia)** for the Americas, **EU (Frankfurt)** for Europe).
4. Click **Create New Bucket**. FluentCart will create the bucket in AWS and select it for you automatically.

> **Region tip:** once a bucket exists, its region is fixed. If you change your mind later, you create a new bucket in the new region and move your files over.

* * *

## Step 3 - Security [​](https://docs.fluentcart.com/guide/storage/aws-s3\#step-3-%E2%80%94-security)

This step configures two bucket-level protections on AWS.

![Amazon S3 - Security step with recommended toggles enabled](https://docs.fluentcart.com/images/storage/s3/security-enabled.webp)

### Block All Public Access [​](https://docs.fluentcart.com/guide/storage/aws-s3\#block-all-public-access)

Controls AWS's S3 _Block Public Access_ setting for this bucket. When enabled, AWS refuses any bucket policy or ACL that would expose objects publicly - even if something is misconfigured downstream.

- **Enabled (Recommended)** - your digital product files are kept private and only served through FluentCart's signed links.
- **Disabled** - required **only** if you explicitly need objects to be publicly reachable, which is unusual for paid digital goods.

### Object Ownership [​](https://docs.fluentcart.com/guide/storage/aws-s3\#object-ownership)

Controls who owns objects uploaded into the bucket.

- **Enforced (Recommended)** - the bucket owner (your AWS account) retains full control of all objects, regardless of who uploaded them. ACLs are effectively disabled.
- **Not enforced** - uploader can retain ownership via ACLs, which complicates permission management.

Both toggles are surfaced as first-class controls with clear recommendation labels:

![Amazon S3 - Security step with toggles disabled, not recommended](https://docs.fluentcart.com/images/storage/s3/security-disabled.webp)

Click **Save Settings** to finish.

* * *

## Connected State [​](https://docs.fluentcart.com/guide/storage/aws-s3\#connected-state)

Once all three steps are complete, the Amazon S3 card shows the provider as **Active**, with the bucket name, region, and security summary.

![Amazon S3 - Connected and ready to serve assets](https://docs.fluentcart.com/images/storage/s3/connected.webp)

What each element does:

- **Active toggle** - enable or disable this storage provider without losing its configuration.
- **Edit** - re-enter the wizard and change credentials, bucket, or security.
- **Bucket name link** - opens the bucket in the AWS console.
- **Region label** - the AWS region your bucket lives in.
- **Check again** - re-runs FluentCart's connection verification against S3 on demand.
- **Security Configuration cards** - quick visual of Block All Public Access + Object Ownership state.

* * *

## Managing Files [​](https://docs.fluentcart.com/guide/storage/aws-s3\#managing-files)

Once connected, all digital product uploads flow through your S3 bucket automatically. Inside the FluentCart file browser you can:

- **Upload** new assets directly to S3.
- **Browse and list** files already in the bucket.
- **Search** by filename.
- **Delete** files you no longer need.
- See a **provider badge** next to each file so you know at a glance whether an asset lives on S3, R2, or local storage.

## Editing an Existing S3 Connection [​](https://docs.fluentcart.com/guide/storage/aws-s3\#editing-an-existing-s3-connection)

Need to rotate your AWS keys, point FluentCart to a different bucket, or tighten the security settings?

1. From **FluentCart → Storage → Amazon S3**, click **Edit**.
2. Move through the Credential → Bucket → Security wizard again.
3. Only the fields you change need to be updated.

You do **not** need to disconnect and reconnect - existing assets stay referenced correctly.

## Enabling / Disabling the S3 Driver [​](https://docs.fluentcart.com/guide/storage/aws-s3\#enabling-disabling-the-s3-driver)

Use the **Active** toggle on the Amazon S3 card to turn the provider on or off. Turning S3 off does not delete any files from AWS - it only tells FluentCart to stop routing new uploads through it.

* * *

## Full `wp-config.php` Example [​](https://docs.fluentcart.com/guide/storage/aws-s3\#full-wp-config-php-example)

For teams standardising on Method A, here is a complete, paste-ready snippet:

php

```
// Add this near the top of wp-config.php, above
// the "That's all, stop editing!" line.
define( 'FCT_S3_ACCESS_KEY', 'AKIAEXAMPLEKEYID1234' );
define( 'FCT_S3_SECRET_KEY', 'wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY' );
```

Once saved, reload the Amazon S3 page in FluentCart and the credential fields will be locked and pre-filled from your config.

* * *

## Troubleshooting [​](https://docs.fluentcart.com/guide/storage/aws-s3\#troubleshooting)

**The connection test fails after I save credentials.**

- Double-check both keys were pasted without leading or trailing spaces.
- Confirm the IAM user has the `AmazonS3FullAccess` policy (or an equivalent that allows `s3:ListAllMyBuckets`, `s3:CreateBucket`, `s3:PutObject`, `s3:GetObject`, `s3:DeleteObject`).
- If you rotated keys recently, make sure the old key is deactivated and you are using the current one.

**"Browse existing buckets" shows nothing.**

- The IAM user lacks `s3:ListAllMyBuckets`.
- The account genuinely has no buckets yet - switch to **Create New Bucket**.

**Bucket creation fails with a name conflict.**

- Bucket names are globally unique across all AWS accounts. Try a more specific name (for example, `yourstore-fluentcart-assets`).

**Files upload but customers cannot download them.**

- _Block All Public Access_ is likely **Enabled** (good) - FluentCart serves files through signed URLs in this mode, so confirm your digital product is configured to use S3 as its storage driver.

**I defined `FCT_S3_ACCESS_KEY` / `FCT_S3_SECRET_KEY` but the UI still shows empty fields.**

- Confirm both constants are in `wp-config.php` (not in a plugin file) and load before FluentCart.
- Confirm the constant names match exactly - `FCT_S3_ACCESS_KEY` and `FCT_S3_SECRET_KEY`.

* * *

## FAQs [​](https://docs.fluentcart.com/guide/storage/aws-s3\#faqs)

**Can I run S3 and Cloudflare R2 at the same time?** Yes - you can configure both and switch which one is active.

**Is my secret key visible from the WordPress admin after I save it?** No. With Method A, keys live only in `wp-config.php`. With Method B, the secret is masked in the UI after save.

**Can I change the region later?** A bucket's region is fixed at creation. To move to a different region, create a new bucket in the new region and either re-upload or use S3's cross-region replication to migrate your existing files.

**Does FluentCart support server-side encryption?** AWS S3 default encryption (SSE-S3) applies at the bucket level. Enable it on the AWS side and FluentCart's uploads will be encrypted automatically.

**Do I have to use `AmazonS3FullAccess`?**`AmazonS3FullAccess` is the simplest policy and is what this guide uses. Security-conscious setups can scope a custom policy down to the specific bucket ARN and only the actions FluentCart uses.

Today

Hi! I’m your AI assistant. How can I assist you today?

Just now

Powered by **FluentBot**

---

## Cloudflare R2 - FluentCart Documentation
URL : https://docs.fluentcart.com/guide/storage/cloudflare-r2

[Skip to content](https://docs.fluentcart.com/guide/storage/cloudflare-r2#VPContent)

# Cloudflare R2 [​](https://docs.fluentcart.com/guide/storage/cloudflare-r2\#cloudflare-r2)

Cloudflare R2 is Cloudflare's object storage service. It speaks the same S3 API that Amazon S3 does, but delivers objects through Cloudflare's global network with **zero egress fees** - meaning you do not pay every time a customer downloads a file. For media-heavy digital products, large archives, or stores with a global customer base, R2 is often the most cost-effective choice.

FluentCart ships with a **native** R2 driver. This means R2 is a first-class storage provider with its own dedicated settings, bucket management, and UI - not an S3-compatible afterthought.

## Accessing Cloudflare R2 Settings [​](https://docs.fluentcart.com/guide/storage/cloudflare-r2\#accessing-cloudflare-r2-settings)

From your WordPress dashboard:

1. Go to **FluentCart → Storage**.
2. Click **Cloudflare R2** in the sub-menu.

R2 setup has two steps:

1. **Credential** - how FluentCart will authenticate to Cloudflare.
2. **Bucket** - which R2 bucket will hold your files.

> **Note:** R2's security model is handled at the token and bucket level on Cloudflare's side, so there is no separate in-app Security step like S3 has.

* * *

## Prerequisites [​](https://docs.fluentcart.com/guide/storage/cloudflare-r2\#prerequisites)

Before you connect R2 to FluentCart, you need:

- A **Cloudflare account** with **R2 enabled** (R2 must be opted into from your Cloudflare dashboard - it is free to enable).
- Your **Cloudflare Account ID**.
- An **R2 API token** with **Object Read & Write** permissions, which gives you an **Access Key ID** and **Secret Access Key**.

### Getting Credentials From Cloudflare [​](https://docs.fluentcart.com/guide/storage/cloudflare-r2\#getting-credentials-from-cloudflare)

FluentCart needs three values from your Cloudflare account to talk to R2:

- **Account ID** - identifies your Cloudflare account.
- **Access Key ID** - the public half of an R2 API token.
- **Secret Access Key** - the private half of that API token (shown only once).

The walkthrough below covers the full journey end-to-end.

#### 1\. Open R2 Object Storage [​](https://docs.fluentcart.com/guide/storage/cloudflare-r2\#_1-open-r2-object-storage)

1. Log in to your [Cloudflare dashboard](https://dash.cloudflare.com/).
2. From the left sidebar, expand **Storage & databases**, then click **R2 Object Storage**.
3. If this is your first time using R2, Cloudflare will ask you to accept the R2 terms and enable the service. Do that before continuing.

You should now see the **R2 Object Storage** overview, listing any existing buckets and usage stats.

#### 2\. Copy Your Account ID [​](https://docs.fluentcart.com/guide/storage/cloudflare-r2\#_2-copy-your-account-id)

Look at the right-hand side of the R2 overview page, under **Account Details**. Your **Account ID** is displayed as a long hex string - click the copy icon next to it to grab it.

![Cloudflare dashboard - Account ID location in R2 overview](https://docs.fluentcart.com/images/storage/r2/cloudflare-r2-id.webp)

Paste it somewhere safe for a moment; you will need it shortly when filling in FluentCart (Method B) or your `wp-config.php` (Method A).

#### 3\. Open the R2 API Tokens Page [​](https://docs.fluentcart.com/guide/storage/cloudflare-r2\#_3-open-the-r2-api-tokens-page)

Still on the R2 overview page, look inside the **Account Details** card for the **API Tokens** row and click the **Manage** button next to it.

![Cloudflare dashboard - Manage API Tokens button](https://docs.fluentcart.com/images/storage/r2/cloudflare-r2-id-manage.webp)

This opens the R2 API Tokens management page, where you will create a new token.

#### 4\. Create an Account API Token [​](https://docs.fluentcart.com/guide/storage/cloudflare-r2\#_4-create-an-account-api-token)

The API Tokens page splits into two sections:

- **Account API Tokens** - tokens tied to the Cloudflare account itself. They stay active even if the person who created them leaves the organization. **Use this for FluentCart on a production site.**
- **User API Tokens** - tokens tied to your individual Cloudflare user. They become inactive if you leave the organization. Only useful for personal or short-lived development setups.

Click **Create Account API token** (the recommended path for a real store).

![Cloudflare dashboard - Create Account API Token button](https://docs.fluentcart.com/images/storage/r2/cloudflare-r2-id-api.webp)

#### 5\. Configure Token Permissions [​](https://docs.fluentcart.com/guide/storage/cloudflare-r2\#_5-configure-token-permissions)

On the **Create Account API Token** page, fill in the following:

- **Token name** - give it something identifiable, for example `R2 Account Token for FluentCart`. This is just a label for your own bookkeeping.
- **Permissions** - select **Admin Read & Write**. This is the right level for FluentCart because it allows the full set of operations the plugin needs:
  - Listing buckets (so "Browse existing buckets" works in the UI)
  - Creating buckets (so "Create New Bucket" works in the UI)
  - Reading, writing, and deleting objects inside buckets (so uploads, downloads, and file management work)
- **TTL (Time to live)** - choose **Forever**. You do not want your store's storage driver to silently stop working when a token expires. If your security policy requires token rotation, pick a date you can actually track and set a calendar reminder to rotate the token before it expires.
- **Client IP Address Filtering** _(optional)_ - leave blank unless your store runs from a known, fixed set of server IPs. If you do restrict by IP, remember to add any load balancer or cron-runner IPs too, or uploads from background processes will fail.

![Cloudflare dashboard - Create Account API Token with Admin Read & Write and Forever TTL](https://docs.fluentcart.com/images/storage/r2/cloudflare-r2-bucket-api.webp)

> **Why "Admin Read & Write" rather than "Object Read & Write"?** _Object Read & Write_ only covers reading, writing, and listing objects in specific buckets. FluentCart additionally lets you list all your buckets and create new ones from its own UI - that needs the broader _Admin_ permission. If you prefer a narrower token, use _Object Read & Write_ scoped to your FluentCart bucket, but you will lose the bucket-browse and bucket-create conveniences in the plugin.

#### 6\. Save the Token and Copy the Keys [​](https://docs.fluentcart.com/guide/storage/cloudflare-r2\#_6-save-the-token-and-copy-the-keys)

Scroll to the bottom of the page and click **Create Account API Token** to generate it.

Cloudflare now shows your credentials once:

- **Access Key ID** - a short identifier.
- **Secret Access Key** - a long secret string.
- (Optionally a ready-made S3 endpoint URL - FluentCart does not need it, but feel free to note it down.)

> **Important:** the **Secret Access Key** is displayed **only once**. If you close the page without copying it, you will have to roll the token and create a new one. Copy both values right away, ideally into a password manager.

You now have all three values FluentCart needs:

| Value | Where it came from |
| --- | --- |
| Account ID | R2 overview → Account Details (step 2) |
| Access Key ID | Create Account API Token result (step 6) |
| Secret Access Key | Create Account API Token result (step 6) |

Head back to FluentCart and continue with Step 1 below.

![Cloudflare dashboard - Create Account API Token](https://docs.fluentcart.com/images/storage/r2/cloudflare-r2-api-created.webp)

* * *

## Step 1 - Credential [​](https://docs.fluentcart.com/guide/storage/cloudflare-r2\#step-1-%E2%80%94-credential)

FluentCart supports two ways to supply your R2 credentials.

### Method A - Define Access Keys in `wp-config.php` (Recommended) [​](https://docs.fluentcart.com/guide/storage/cloudflare-r2\#method-a-%E2%80%94-define-access-keys-in-wp-config-php-recommended)

The most secure option. Keys live in your WordPress configuration file, not in the database, and are not editable from the admin UI.

![Cloudflare R2 - Define access keys in wp-config.php](https://docs.fluentcart.com/images/storage/r2/credential-define.webp)

Copy the snippet below **near the top** of your `wp-config.php` (before the `/* That's all, stop editing! */` line) and replace the placeholder values with your real Cloudflare values:

php

```
define( 'FCT_R2_ACCOUNT_ID', 'your-account-id' );
define( 'FCT_R2_ACCESS_KEY', 'your-access-key-id' );
define( 'FCT_R2_SECRET_KEY', 'your-secret-access-key' );
```

Once FluentCart detects these constants, the credential fields lock automatically and the Connection Method card confirms the keys were picked up from `wp-config.php`. The in-app snippet includes a **Copy Snippet** button to make this paste-in friendlier.

> **Heads up:** to later switch to a different method here, comment out or remove the `FCT_R2_ACCOUNT_ID`, `FCT_R2_ACCESS_KEY`, and `FCT_R2_SECRET_KEY` defines from `wp-config.php` and reload the page.

### Method B - Store Access Keys in the Database [​](https://docs.fluentcart.com/guide/storage/cloudflare-r2\#method-b-%E2%80%94-store-access-keys-in-the-database)

Available when you need UI-only configuration. Keys are saved to the database; an explicit acknowledgement is required.

![Cloudflare R2 - Store access keys in the database](https://docs.fluentcart.com/images/storage/r2/credential-db.webp)

Select **"I understand the risks but I'd like to store access keys in the database anyway."** Then enter:

- **Account ID** - your Cloudflare Account ID.
- **Access Key ID** - from your R2 API token.
- **Secret Access Key** - from your R2 API token.

Click **Save & Continue** to move to the bucket step.

* * *

## Step 2 - Bucket [​](https://docs.fluentcart.com/guide/storage/cloudflare-r2\#step-2-%E2%80%94-bucket)

An R2 **bucket** is a named storage container inside your Cloudflare account. FluentCart gives you three ways to pick or create one.

### Option 1 - Use Existing Bucket, Entered Manually [​](https://docs.fluentcart.com/guide/storage/cloudflare-r2\#option-1-%E2%80%94-use-existing-bucket-entered-manually)

If you already know the name of the bucket you want to use, type it directly.

![Cloudflare R2 - Enter bucket name manually](https://docs.fluentcart.com/images/storage/r2/bucket-existing-manual.webp)

1. Select **Use Existing Bucket**.
2. Choose **Enter bucket name**.
3. Type the bucket name and click **Save Settings**.

### Option 2 - Use Existing Bucket, Browse From Cloudflare [​](https://docs.fluentcart.com/guide/storage/cloudflare-r2\#option-2-%E2%80%94-use-existing-bucket-browse-from-cloudflare)

FluentCart can fetch the buckets attached to your Cloudflare account so you can pick one from the list.

![Cloudflare R2 - Browse existing buckets](https://docs.fluentcart.com/images/storage/r2/bucket-existing-browse.webp)

1. Select **Use Existing Bucket**.
2. Choose **Browse existing buckets**.
3. Click the refresh icon if a bucket you just created is not visible.
4. Click the bucket you want, then **Save Settings**.

### Option 3 - Create a New Bucket From the UI [​](https://docs.fluentcart.com/guide/storage/cloudflare-r2\#option-3-%E2%80%94-create-a-new-bucket-from-the-ui)

No need to switch over to the Cloudflare dashboard. FluentCart can create a fresh R2 bucket in the jurisdiction you pick.

![Cloudflare R2 - Create a new bucket](https://docs.fluentcart.com/images/storage/r2/bucket-create-new.webp)

1. Select **Create New Bucket**.
2. Enter a **Bucket Name**. R2 bucket names must be **globally unique across all Cloudflare R2 accounts** - this is called out directly in the UI.
3. Choose a **Region / Jurisdiction** (see the table below). **Automatic** is a safe default and lets Cloudflare pick the best fit.
4. Click **Save Settings**. FluentCart creates the bucket in R2 and selects it automatically.

### Understanding R2 Jurisdictions [​](https://docs.fluentcart.com/guide/storage/cloudflare-r2\#understanding-r2-jurisdictions)

R2 lets you pin a bucket to a geographic jurisdiction for data residency, latency, or compliance reasons.

| Value | Label | When to pick it |
| --- | --- | --- |
| `auto` | Automatic | Default. Cloudflare chooses the best location based on where data is written. Best general-purpose choice. |
| `apac` | Asia-Pacific (APAC) | Most of your customers are in Asia-Pacific. |
| `eeur` | Eastern Europe (EEUR) | Customers or compliance requirements in Eastern Europe. |
| `enam` | Eastern North America (ENAM) | Customers primarily on the US East Coast / eastern Canada. |
| `weur` | Western Europe (WEUR) | Customers or GDPR-driven residency in Western Europe. |
| `wnam` | Western North America (WNAM) | Customers primarily on the US West Coast / western Canada. |
| `oc` | Oceania (OC) | Customers primarily in Australia / New Zealand. |

> **Tip:** a bucket's jurisdiction is fixed once created. If you later need a different jurisdiction, create a new bucket and migrate your files across.

* * *

## Connected State [​](https://docs.fluentcart.com/guide/storage/cloudflare-r2\#connected-state)

Once credentials are verified and a bucket is picked, the Cloudflare R2 card shows the provider as **Active**, with the bucket name and jurisdiction.

![Cloudflare R2 - Connected and ready to serve assets](https://docs.fluentcart.com/images/storage/r2/connected.webp)

What each element does:

- **Active toggle** - enable or disable this storage provider without losing its configuration.
- **Edit** - re-enter the wizard and change credentials or bucket.
- **Bucket name** - the R2 bucket your assets live in.
- **Jurisdiction label** (e.g. `ENAM`) - the R2 region this bucket is pinned to.
- **Check Connection** - re-runs FluentCart's connection verification against R2 on demand.

* * *

## Managing Files [​](https://docs.fluentcart.com/guide/storage/cloudflare-r2\#managing-files)

Once connected, all digital product uploads flow through your R2 bucket automatically. Inside the FluentCart file browser you can:

- **Upload** new assets directly to R2.
- **Browse and list** files already in the bucket.
- **Search** by filename.
- **Delete** files you no longer need.
- See a **provider badge** next to each file so you always know which storage driver an asset lives on.

## Editing an Existing R2 Connection [​](https://docs.fluentcart.com/guide/storage/cloudflare-r2\#editing-an-existing-r2-connection)

1. From **FluentCart → Storage → Cloudflare R2**, click **Edit**.
2. Move through the Credential → Bucket wizard again.
3. Only the fields you change need to be updated.

You do **not** need to disconnect and reconnect - existing assets stay referenced correctly.

## Enabling / Disabling the R2 Driver [​](https://docs.fluentcart.com/guide/storage/cloudflare-r2\#enabling-disabling-the-r2-driver)

Use the **Active** toggle on the Cloudflare R2 card to turn the provider on or off. Turning R2 off does not delete any files from Cloudflare - it only tells FluentCart to stop routing new uploads through it.

* * *

## Full `wp-config.php` Example [​](https://docs.fluentcart.com/guide/storage/cloudflare-r2\#full-wp-config-php-example)

For teams standardising on Method A, here is a complete, paste-ready snippet:

php

```
// Add this near the top of wp-config.php, above
// the "That's all, stop editing!" line.
define( 'FCT_R2_ACCOUNT_ID', '1a2b3c4d5e6f7g8h9i0j' );
define( 'FCT_R2_ACCESS_KEY', 'EXAMPLEACCESSKEYID12' );
define( 'FCT_R2_SECRET_KEY', 'EXAMPLE_SECRET_ACCESS_KEY_1234567890abcd' );
```

Once saved, reload the Cloudflare R2 page in FluentCart and the credential fields will be locked and pre-filled from your config.

* * *

## Troubleshooting [​](https://docs.fluentcart.com/guide/storage/cloudflare-r2\#troubleshooting)

**The connection fails with an authentication error.**

- Verify your **Account ID** is correct - it is a long hex string, not your email or account name.
- Confirm the **Access Key ID** and **Secret Access Key** were copied fully, with no extra spaces.
- Make sure the R2 API token has **Object Read & Write** permission.
- If you regenerated the token, the previous Access Key ID / Secret are invalid.

**"Browse existing buckets" is empty.**

- Your Cloudflare account has no R2 buckets yet - switch to **Create New Bucket**.
- The API token is scoped to a different set of buckets than the one you expect.

**Bucket creation fails with a name conflict.**

- R2 bucket names are globally unique across **all** Cloudflare accounts. Pick a more specific name (for example, `yourstore-fluentcart-assets`).

**Files upload but customers cannot download them.**

- Confirm the digital product is configured to use Cloudflare R2 as its storage driver.
- Confirm the API token still has **Object Read & Write** - read-only tokens will break downloads.

**I defined `FCT_R2_ACCOUNT_ID` / `FCT_R2_ACCESS_KEY` / `FCT_R2_SECRET_KEY` but the UI still shows empty fields.**

- Confirm all three constants are in `wp-config.php` (not inside a plugin or theme file) and load before FluentCart.
- Confirm the constant names match exactly - `FCT_R2_ACCOUNT_ID`, `FCT_R2_ACCESS_KEY`, and `FCT_R2_SECRET_KEY`.

* * *

## FAQs [​](https://docs.fluentcart.com/guide/storage/cloudflare-r2\#faqs)

**Can I run Cloudflare R2 and Amazon S3 at the same time?** Yes - you can configure both and switch which one is active.

**Can I change a bucket's jurisdiction after creation?** No. Jurisdiction is fixed at bucket creation. To change it, create a new bucket with the new jurisdiction and migrate your files across.

**Is my Secret Access Key visible in the admin after I save it?** No. With Method A the key lives only in `wp-config.php`. With Method B the Secret Access Key is masked after save.

**What does "Automatic" do for the jurisdiction?** Cloudflare picks the optimal location based on where the first write comes from, balancing latency and availability. It is the recommended default for most stores.

Today

Hi! I’m your AI assistant. How can I assist you today?

Just now

Powered by **FluentBot**

---

## 404 - FluentCart Documentation
URL : https://docs.fluentcart.com/guide/storage/r2

[Skip to content](https://docs.fluentcart.com/guide/storage/r2#VPContent)

404

# PAGE NOT FOUND

> But if you don't change your direction, and if you keep looking, you may end up where you are heading.

[Take me home](https://docs.fluentcart.com/)

Today

Hi! I’m your AI assistant. How can I assist you today?

Just now

Powered by **FluentBot**

---

## 404 - FluentCart Documentation
URL : https://docs.fluentcart.com/guide/storage/s3

[Skip to content](https://docs.fluentcart.com/guide/storage/s3#VPContent)

404

# PAGE NOT FOUND

> But if you don't change your direction, and if you keep looking, you may end up where you are heading.

[Take me home](https://docs.fluentcart.com/)

Today

Hi! I’m your AI assistant. How can I assist you today?

Just now

Powered by **FluentBot**

---
