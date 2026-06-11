# FluentCart Developer Docs - Database Schema & Query Builder (Part 1/2)

Schéma de la base de données et patterns du query builder utilisé par FluentCart.

---

## Database Schema | FluentCart Developer Docs

**URL** : https://dev.fluentcart.com/database/schema

[Skip to content](https://dev.fluentcart.com/database/schema#VPContent)

# FluentCart Database Schema [​](https://dev.fluentcart.com/database/schema\#fluentcart-database-schema)

FluentCart uses custom database tables to store all the e-commerce data. Here are the list of database tables and their schema to understand overall database design and related data attributes of each model.

### Core Entity Relationships [​](https://dev.fluentcart.com/database/schema\#core-entity-relationships)

🔍 Interactive ER Diagram

Click on the diagram below to zoom in for better readability. The diagram shows the relationships between all FluentCart database tables.

fct\_customersbigintidPKbigintuser\_idFKfct\_ordersbigintidPKbigintparent\_idFKbigintcustomer\_idFKfct\_order\_itemsbigintidPKbigintorder\_idFKbigintpost\_idFKbigintobject\_idFKfct\_order\_transactionsbigintidPKbigintorder\_idFKbigintsubscription\_idFKfct\_subscriptionsbigintidPKbigintcustomer\_idFKbigintparent\_order\_idFKbigintproduct\_idFKbigintvariation\_idFKfct\_product\_detailsbigintidPKbigintpost\_idFKbigintdefault\_variation\_idFKfct\_product\_variationsbigintidPKbigintpost\_idFKfct\_customer\_addressesbigintidPKbigintcustomer\_idFKfct\_couponsbigintidPKfct\_applied\_couponsbigintidPKbigintorder\_idFKbigintcoupon\_idFKbigintcustomer\_idFKfct\_licensesbigintidPKbigintproduct\_idFKbigintcustomer\_idFKbigintorder\_idFKfct\_license\_activationsbigintidPKbigintsite\_idFKbigintlicense\_idFKbigintproduct\_idFKfct\_license\_sitesbigintidPKbigintlicense\_idFKfct\_cartsbigintcustomer\_idFKbigintuser\_idFKbigintorder\_idFKfct\_activitybigintidPKbigintmodule\_idFKbigintuser\_idFKcustomer\_idcustomer\_idcustomer\_idcustomer\_idcustomer\_idcustomer\_idorder\_idorder\_idparent\_order\_idorder\_idorder\_idorder\_idparent\_idpost\_idobject\_idproduct\_idvariation\_idproduct\_idcoupon\_idlicense\_idlicense\_idsite\_idsubscription\_id

### Schema Overview [​](https://dev.fluentcart.com/database/schema\#schema-overview)

The FluentCart database schema is built around these core concepts:

- **Orders & Transactions**: Complete order lifecycle management with payment tracking
- **Customers & Addresses**: Customer relationship management with multiple address support
- **Products & Variations**: Flexible product catalog with inventory management
- **Subscriptions**: Recurring billing and subscription lifecycle management
- **Coupons & Discounts**: Advanced discount system with conditions and stacking
- **Shipping & Tax**: Configurable shipping zones and tax rate management
- **Activity & Logging**: Comprehensive audit trail for all operations
- **Email Notifications**: Automated email templates and delivery system
- **Background Jobs**: Scheduled actions for automated processing
- **Cart Management**: Shopping cart persistence and checkout flow
- **Attributes & Labels**: Flexible product attributes and object tagging system
- **Webhooks**: External integration logging and delivery tracking
- **Licensing** (Pro): Software license management with activation tracking
- **Promotions** (Pro): Order promotion tracking and statistics

### Key Design Principles [​](https://dev.fluentcart.com/database/schema\#key-design-principles)

1. **Currency Precision**: All monetary values stored as BIGINT in cents to avoid floating-point precision issues
2. **Flexible Configuration**: JSON columns used for extensible configuration data
3. **Audit Trail**: Comprehensive activity logging for all important operations
4. **Referential Integrity**: Proper foreign key relationships maintained throughout
5. **Performance Optimization**: Strategic indexing on frequently queried columns
6. **Multi-tenancy Ready**: UUID-based public identifiers for external integrations

## Database Tables [​](https://dev.fluentcart.com/database/schema\#database-tables)

## fct\_customers Table [​](https://dev.fluentcart.com/database/schema\#fct-customers-table)

This table stores customer information and purchase history

| Column | Type | Comment |
| --- | --- | --- |
| id | BIGINT UNSIGNED _Auto Increment_ | Primary key |
| user\_id | BIGINT UNSIGNED NULL | WordPress user ID |
| contact\_id | BIGINT UNSIGNED NOT NULL DEFAULT '0' | Contact ID |
| email | VARCHAR(192) NOT NULL DEFAULT '' | Customer email |
| first\_name | VARCHAR(192) NOT NULL DEFAULT '' | First name |
| last\_name | VARCHAR(192) NOT NULL DEFAULT '' | Last name |
| status | VARCHAR(45) NULL DEFAULT 'active' | active, inactive, archived |
| purchase\_value | JSON NULL | Purchase value data |
| purchase\_count | BIGINT UNSIGNED NOT NULL DEFAULT '0' | Total number of purchases |
| ltv | BIGINT NOT NULL DEFAULT '0' | Lifetime value in cents |
| first\_purchase\_date | DATETIME NULL | First purchase date |
| last\_purchase\_date | DATETIME NULL | Last purchase date |
| aov | DECIMAL(18,2) NULL | Average order value |
| notes | LONGTEXT NOT NULL | Customer notes |
| uuid | VARCHAR(100) NULL DEFAULT '' | Unique identifier |
| country | VARCHAR(45) NULL | Country |
| city | VARCHAR(45) NULL | City |
| state | VARCHAR(45) NULL | State |
| postcode | VARCHAR(45) NULL | Postal code |
| created\_at | DATETIME NULL |  |
| updated\_at | DATETIME NULL |  |

Indexes:

- email
- user\_id

## fct\_orders Table [​](https://dev.fluentcart.com/database/schema\#fct-orders-table)

This table stores the basic information of an order

| Column | Type | Comment |
| --- | --- | --- |
| id | BIGINT UNSIGNED _Auto Increment_ | Primary key |
| status | VARCHAR(20) NOT NULL DEFAULT 'draft' | draft / pending / on-hold / processing / completed / failed / refunded / partial-refund |
| parent\_id | BIGINT UNSIGNED NULL | Parent order |
| receipt\_number | BIGINT UNSIGNED NULL |  |
| invoice\_no | VARCHAR(192) NULL DEFAULT '' |  |
| fulfillment\_type | VARCHAR(20) NULL DEFAULT 'physical' | physical, digital, service, mixed |
| type | VARCHAR(20) NOT NULL DEFAULT 'payment' | payment, renewal, refund |
| mode | ENUM('live', 'test') NOT NULL DEFAULT 'live' | live / test |
| shipping\_status | VARCHAR(20) NOT NULL DEFAULT '' | unshipped / shipped / delivered / unshippable |
| customer\_id | BIGINT UNSIGNED NULL |  |
| payment\_method | VARCHAR(100) NOT NULL |  |
| payment\_status | VARCHAR(20) NOT NULL DEFAULT '' |  |
| payment\_method\_title | VARCHAR(100) NOT NULL |  |
| currency | VARCHAR(10) NOT NULL |  |
| subtotal | BIGINT NOT NULL DEFAULT '0' | Amount in cents |
| discount\_tax | BIGINT NOT NULL DEFAULT '0' | Amount in cents |
| manual\_discount\_total | BIGINT NOT NULL DEFAULT '0' | Amount in cents |
| coupon\_discount\_total | BIGINT NOT NULL DEFAULT '0' | Amount in cents |
| shipping\_tax | BIGINT NOT NULL DEFAULT '0' | Amount in cents |
| shipping\_total | BIGINT NOT NULL DEFAULT '0' | Amount in cents |
| tax\_total | BIGINT NOT NULL DEFAULT '0' | Amount in cents |
| total\_amount | BIGINT NOT NULL DEFAULT '0' | Amount in cents |
| total\_paid | BIGINT NOT NULL DEFAULT '0' | Amount in cents |
| total\_refund | BIGINT NOT NULL DEFAULT '0' | Amount in cents |
| rate | DECIMAL(12,4) NOT NULL DEFAULT '1.0000' | Exchange rate |
| tax\_behavior | TINYINT(1) NOT NULL DEFAULT 0 | 0 => no\_tax, 1 => exclusive, 2 => inclusive |
| note | TEXT NOT NULL DEFAULT '' |  |
| ip\_address | TEXT NOT NULL DEFAULT '' |  |
| completed\_at | DATETIME NULL DEFAULT NULL |  |
| refunded\_at | DATETIME NULL DEFAULT NULL |  |
| uuid | VARCHAR(100) NOT NULL |  |
| config | JSON DEFAULT NULL |  |
| created\_at | DATETIME NULL |  |
| updated\_at | DATETIME NULL |  |

Indexes:

- invoice\_no (191)
- type
- customer\_id
- created\_at, completed\_at

## fct\_coupons Table [​](https://dev.fluentcart.com/database/schema\#fct-coupons-table)

This table stores coupon definitions and rules

| Column | Type | Comment |
| --- | --- | --- |
| id | BIGINT UNSIGNED _Auto Increment_ | Primary key |
| title | VARCHAR(200) NOT NULL | Coupon title |
| code | VARCHAR(50) NOT NULL UNIQUE | Coupon code (unique) |
| priority | INT DEFAULT NULL | Coupon priority |
| type | VARCHAR(20) NOT NULL | Coupon type |
| conditions | JSON NULL | Coupon conditions |
| amount | double NOT NULL | Discount amount |
| use\_count | INT DEFAULT 0 | Usage count |
| status | VARCHAR(20) NOT NULL | Coupon status |
| notes | LONGTEXT NOT NULL | Coupon notes |
| stackable | VARCHAR(3) NOT NULL DEFAULT 'no' | Stackable flag (yes/no) |
| show\_on\_checkout | VARCHAR(3) NOT NULL DEFAULT 'yes' | Show on checkout (yes/no) |
| start\_date | TIMESTAMP NULL | Start date |
| end\_date | TIMESTAMP NULL | End date |
| created\_at | DATETIME NULL |  |
| updated\_at | DATETIME NULL |  |

Indexes:

- code
- status

## fct\_order\_items Table [​](https://dev.fluentcart.com/database/schema\#fct-order-items-table)

This table stores individual items within orders

| Column | Type | Comment |
| --- | --- | --- |
| id | BIGINT(20) UNSIGNED _Auto Increment_ | Primary key |
| order\_id | BIGINT UNSIGNED NOT NULL DEFAULT '0' | Reference to order |
| post\_id | BIGINT UNSIGNED NOT NULL DEFAULT '0' | WordPress post ID (product) |
| fulfillment\_type | VARCHAR(20) NOT NULL DEFAULT 'physical' | physical, digital, service |
| payment\_type | VARCHAR(20) NOT NULL DEFAULT 'onetime' | onetime, subscription, signup\_fee |
| post\_title | TEXT NOT NULL | Product title |
| title | TEXT NOT NULL | Item title (variation) |
| object\_id | BIGINT UNSIGNED NULL DEFAULT NULL | Variation ID |
| cart\_index | BIGINT UNSIGNED NOT NULL DEFAULT '0' | Position in cart |
| quantity | INT NOT NULL DEFAULT '1' | Item quantity |
| unit\_price | BIGINT NOT NULL DEFAULT '0' | Price per unit in cents |
| cost | BIGINT NOT NULL DEFAULT '0' | Cost in cents |
| subtotal | BIGINT NOT NULL DEFAULT '0' | Line subtotal |
| tax\_amount | BIGINT NOT NULL DEFAULT '0' | Tax amount for this line |
| shipping\_charge | BIGINT NOT NULL DEFAULT '0' | Shipping charge |
| discount\_total | BIGINT NOT NULL DEFAULT '0' | Discount amount |
| line\_total | BIGINT NOT NULL DEFAULT '0' | Total line amount |
| refund\_total | BIGINT NOT NULL DEFAULT '0' | Refunded amount |
| rate | BIGINT NOT NULL DEFAULT '1' | Exchange rate |
| other\_info | JSON NULL | Additional item data |
| line\_meta | JSON NULL | Line-specific metadata |
| fulfilled\_quantity | INT NOT NULL DEFAULT '0' | Quantity fulfilled |
| referrer | TEXT NULL | Referral information |
| created\_at | DATETIME NULL |  |
| updated\_at | DATETIME NULL |  |

Indexes:

- order\_id, object\_id
- post\_id

## fct\_subscriptions Table [​](https://dev.fluentcart.com/database/schema\#fct-subscriptions-table)

This table stores subscription information and billing cycles

| Column | Type | Comment |
| --- | --- | --- |
| id | BIGINT UNSIGNED _Auto Increment_ | Primary key |
| uuid | VARCHAR(100) NOT NULL | Unique identifier |
| customer\_id | BIGINT(20) UNSIGNED NOT NULL | Reference to customer |
| parent\_order\_id | BIGINT(20) UNSIGNED NOT NULL | Initial order ID |
| product\_id | BIGINT(20) UNSIGNED NOT NULL | WordPress post ID |
| item\_name | TEXT NOT NULL | Subscription item name |
| quantity | INT NOT NULL DEFAULT '1' | Subscription quantity |
| variation\_id | BIGINT(20) UNSIGNED NOT NULL | Product variation ID |
| billing\_interval | VARCHAR(45) NULL | Billing interval (day, week, month, year) |
| signup\_fee | BIGINT UNSIGNED NOT NULL DEFAULT 0 | Signup fee in cents |
| initial\_tax\_total | BIGINT UNSIGNED NOT NULL DEFAULT 0 | Initial tax in cents |
| recurring\_amount | BIGINT UNSIGNED NOT NULL DEFAULT 0 | Recurring amount in cents |
| recurring\_tax\_total | BIGINT UNSIGNED NOT NULL DEFAULT 0 | Recurring tax in cents |
| recurring\_total | BIGINT UNSIGNED NOT NULL DEFAULT 0 | Total recurring in cents |
| bill\_times | BIGINT(20) UNSIGNED NOT NULL DEFAULT 0 | Total billing cycles |
| bill\_count | INT UNSIGNED NOT NULL DEFAULT 0 | Current billing count |
| expire\_at | DATETIME NULL | Expiration date |
| trial\_ends\_at | DATETIME NULL | Trial end date |
| canceled\_at | DATETIME NULL | Cancellation date |
| restored\_at | DATETIME NULL | Restoration date |
| collection\_method | ENUM('automatic', 'manual', 'system') NOT NULL DEFAULT 'automatic' | Payment collection method |
| next\_billing\_date | DATETIME NULL | Next billing date |
| trial\_days | INT(10) UNSIGNED NOT NULL DEFAULT 0 | Trial period in days |
| vendor\_customer\_id | VARCHAR(45) NULL | Payment gateway customer ID |
| vendor\_plan\_id | VARCHAR(45) NULL | Payment gateway plan ID |
| vendor\_subscription\_id | VARCHAR(45) NULL | Payment gateway subscription ID |
| status | VARCHAR(45) NULL | active, canceled, expired, pending, trialing |
| original\_plan | LONGTEXT NULL | Original plan data |
| vendor\_response | LONGTEXT NULL | Payment gateway response |
| current\_payment\_method | VARCHAR(45) NULL | Current payment method |
| config | JSON DEFAULT NULL | Subscription configuration |
| created\_at | DATETIME NULL |  |
| updated\_at | DATETIME NULL |  |

Indexes:

- parent\_order\_id

## fct\_order\_transactions Table [​](https://dev.fluentcart.com/database/schema\#fct-order-transactions-table)

This table stores payment transactions for orders

| Column | Type | Comment |
| --- | --- | --- |
| id | BIGINT(20) UNSIGNED _Auto Increment_ | Primary key |
| order\_id | BIGINT UNSIGNED NOT NULL DEFAULT '0' | Reference to order |
| order\_type | VARCHAR(100) NOT NULL DEFAULT '' |  |
| transaction\_type | VARCHAR(192) DEFAULT 'charge' | charge, refund, etc. |
| subscription\_id | INT(11) NULL | Reference to subscription |
| card\_last\_4 | INT(4) | Last 4 digits of card |
| card\_brand | VARCHAR(100) | Card brand |
| vendor\_charge\_id | VARCHAR(192) NOT NULL DEFAULT '' | Payment gateway transaction ID |
| payment\_method | VARCHAR(100) NOT NULL DEFAULT '' |  |
| payment\_mode | VARCHAR(100) NOT NULL DEFAULT '' | live, test |
| payment\_method\_type | VARCHAR(100) NOT NULL DEFAULT '' | card, bank, etc. |
| status | VARCHAR(20) NOT NULL DEFAULT '' | Transaction status |
| currency | VARCHAR(10) NOT NULL DEFAULT '' | Transaction currency |
| total | BIGINT NOT NULL DEFAULT '0' | Transaction amount in cents |
| rate | BIGINT NOT NULL DEFAULT '1' | Exchange rate |
| uuid | VARCHAR(100) NULL DEFAULT '' |  |
| meta | JSON DEFAULT NULL | Transaction metadata |
| created\_at | DATETIME NULL |  |
| updated\_at | DATETIME NULL |  |

Indexes:

- vendor\_charge\_id (64)
- payment\_method
- status
- order\_id

## fct\_order\_addresses Table [​](https://dev.fluentcart.com/database/schema\#fct-order-addresses-table)

This table stores order shipping and billing addresses

| Column | Type | Comment |
| --- | --- | --- |
| id | BIGINT(20) UNSIGNED _Auto Increment_ | Primary key |
| order\_id | BIGINT UNSIGNED NOT NULL | Reference to order |
| type | VARCHAR(20) NOT NULL DEFAULT 'billing' | billing, shipping |
| name | VARCHAR(192) NULL | Address name |
| address\_1 | VARCHAR(192) NULL | Address line 1 |
| address\_2 | VARCHAR(192) NULL | Address line 2 |
| city | VARCHAR(192) NULL | City |
| state | VARCHAR(192) NULL | State |
| postcode | VARCHAR(50) NULL | Postal code |
| country | VARCHAR(100) NULL | Country |
| created\_at | DATETIME NULL |  |
| updated\_at | DATETIME NULL |  |

## fct\_order\_operations Table [​](https://dev.fluentcart.com/database/schema\#fct-order-operations-table)

This table stores order operation logs and analytics

| Column | Type | Comment |
| --- | --- | --- |
| id | BIGINT UNSIGNED _Auto Increment_ | Primary key |
| order\_id | BIGINT(20) UNSIGNED NOT NULL | Reference to order |
| created\_via | VARCHAR(45) NULL | How the order was created |
| emails\_sent | TINYINT(1) NULL DEFAULT 0 | Emails sent flag |
| sales\_recorded | TINYINT(1) NULL DEFAULT 0 | Sales recorded flag |
| utm\_campaign | VARCHAR(192) NULL DEFAULT '' | UTM campaign tracking |
| utm\_term | VARCHAR(192) NULL DEFAULT '' | UTM term tracking |
| utm\_source | VARCHAR(192) NULL DEFAULT '' | UTM source tracking |
| utm\_medium | VARCHAR(192) NULL DEFAULT '' | UTM medium tracking |
| utm\_content | VARCHAR(192) NULL DEFAULT '' | UTM content tracking |
| utm\_id | VARCHAR(192) NULL DEFAULT '' | UTM ID tracking |
| cart\_hash | VARCHAR(192) NULL DEFAULT '' | Cart hash identifier |
| refer\_url | VARCHAR(192) NULL DEFAULT '' | Referral URL |
| meta | JSON DEFAULT NULL | Additional operation metadata |
| created\_at | DATETIME NULL |  |
| updated\_at | DATETIME NULL |  |

Indexes:

- order\_id

## fct\_order\_download\_permissions Table [​](https://dev.fluentcart.com/database/schema\#fct-order-download-permissions-table)

This table stores download permissions for orders

| Column | Type | Comment |
| --- | --- | --- |
| id | BIGINT UNSIGNED _Auto Increment_ | Primary key |
| order\_id | BIGINT(20) UNSIGNED NOT NULL | Reference to order |
| variation\_id | BIGINT(20) UNSIGNED NOT NULL | Reference to product variation |
| download\_id | BIGINT(20) UNSIGNED NOT NULL | Reference to download |
| download\_count | INT(11) NULL | Number of downloads |
| download\_limit | INT(11) NULL | Download limit |
| access\_expires | DATETIME NULL | Access expiration date |
| customer\_id | BIGINT(20) UNSIGNED NOT NULL | Reference to customer |
| created\_at | DATETIME NULL |  |
| updated\_at | DATETIME NULL |  |

Indexes:

- order\_id
- download\_id
- variation\_id

## fct\_product\_variations Table [​](https://dev.fluentcart.com/database/schema\#fct-product-variations-table)

This table stores product variations with pricing and inventory

| Column | Type | Comment |
| --- | --- | --- |
| id | BIGINT(20) UNSIGNED _Auto Increment_ | Primary key |
| post\_id | BIGINT(20) UNSIGNED NOT NULL | WordPress post ID |
| media\_id | BIGINT(20) UNSIGNED NULL | Media attachment ID |
| serial\_index | INT(5) NULL | Variation order |
| sold\_individually | TINYINT(1) UNSIGNED NULL DEFAULT 0 | Sold individually flag |
| variation\_title | VARCHAR(192) NOT NULL | Variation title |
| variation\_identifier | VARCHAR(100) NULL | SKU or identifier |
| manage\_stock | TINYINT(1) NULL DEFAULT 0 | Stock management enabled |
| payment\_type | VARCHAR(50) NULL | onetime, subscription |
| stock\_status | VARCHAR(30) NULL DEFAULT 'out-of-stock' | in-stock, out-of-stock, backorder |
| backorders | TINYINT(1) UNSIGNED NULL DEFAULT 0 | Backorders allowed |
| total\_stock | INT(11) NULL DEFAULT 0 | Total stock quantity |
| on\_hold | INT(11) NULL DEFAULT 0 | Stock on hold |
| committed | INT(11) NULL DEFAULT 0 | Committed stock |
| available | INT(11) NULL DEFAULT 0 | Available stock |
| fulfillment\_type | VARCHAR(100) NULL DEFAULT 'physical' | physical, digital, service, mixed |
| item\_status | VARCHAR(30) NULL DEFAULT 'active' | active, inactive |
| manage\_cost | VARCHAR(30) NULL DEFAULT 'false' | Cost management enabled |
| item\_price | double DEFAULT 0 NOT NULL | Variation price |
| item\_cost | double DEFAULT 0 NOT NULL | Variation cost |
| compare\_price | double DEFAULT 0 NULL | Compare at price |
| shipping\_class | BIGINT(20) NULL | Shipping class ID |
| other\_info | longtext NULL | Additional variation data |
| downloadable | VARCHAR(30) NULL DEFAULT 'false' | Downloadable flag |
| created\_at | DATETIME NULL |  |
| updated\_at | DATETIME NULL |  |

Indexes:

- post\_id
- stock\_status

## fct\_product\_details Table [​](https://dev.fluentcart.com/database/schema\#fct-product-details-table)

This table stores product configuration and settings

| Column | Type | Comment |
| --- | --- | --- |
| id | BIGINT(20) UNSIGNED _Auto Increment_ | Primary key |
| post\_id | BIGINT(20) UNSIGNED NOT NULL | WordPress post ID |
| fulfillment\_type | VARCHAR(100) NULL DEFAULT 'physical' | physical, digital, service, mixed |
| min\_price | double DEFAULT 0 NOT NULL | Minimum price |
| max\_price | double DEFAULT 0 NOT NULL | Maximum price |
| default\_variation\_id | BIGINT(20) UNSIGNED NULL | Default variation ID |
| default\_media | JSON NULL | Default media data |
| manage\_stock | TINYINT(1) NULL DEFAULT 0 | Stock management enabled |
| stock\_availability | VARCHAR(100) NULL DEFAULT 'in-stock' | in-stock, out-of-stock, backorder |
| variation\_type | VARCHAR(30) NULL DEFAULT 'simple' | simple, simple\_variation, advance\_variation |
| manage\_downloadable | TINYINT(1) NULL DEFAULT 0 | Downloadable management enabled |
| other\_info | JSON NULL | Additional product data |
| created\_at | DATETIME NULL |  |
| updated\_at | DATETIME NULL |  |

Indexes:

- post\_id
- stock\_availability

## fct\_product\_meta Table [​](https://dev.fluentcart.com/database/schema\#fct-product-meta-table)

This table stores product metadata

| Column | Type | Comment |
| --- | --- | --- |
| id | BIGINT UNSIGNED _Auto Increment_ | Primary key |
| object\_id | BIGINT UNSIGNED NOT NULL | Reference to product |
| object\_type | VARCHAR(192) NULL | Object type |
| meta\_key | VARCHAR(192) NOT NULL | Meta key |
| meta\_value | LONGTEXT NULL DEFAULT NULL | Meta value |
| created\_at | DATETIME NULL |  |
| updated\_at | DATETIME NULL |  |

Indexes:

- meta\_key

## fct\_applied\_coupons Table [​](https://dev.fluentcart.com/database/schema\#fct-applied-coupons-table)

This table stores applied coupons to orders

| Column | Type | Comment |
| --- | --- | --- |
| id | BIGINT UNSIGNED _Auto Increment_ | Primary key |
| order\_id | BIGINT UNSIGNED NOT NULL | Reference to order |
| coupon\_id | BIGINT UNSIGNED NULL | Reference to coupon |
| customer\_id | BIGINT UNSIGNED NULL | Reference to customer |
| code | VARCHAR(100) NOT NULL | Coupon code |
| amount | double NOT NULL | Discount amount |
| created\_at | DATETIME NULL |  |
| updated\_at | DATETIME NULL |  |

Indexes:

- code

## fct\_customer\_addresses Table [​](https://dev.fluentcart.com/database/schema\#fct-customer-addresses-table)

This table stores customer shipping and billing addresses

| Column | Type | Comment |
| --- | --- | --- |
| id | BIGINT UNSIGNED _Auto Increment_ | Primary key |
| customer\_id | BIGINT UNSIGNED NOT NULL | Reference to customer |
| is\_primary | TINYINT(1) NOT NULL DEFAULT 0 | Primary address flag |
| type | VARCHAR(20) NOT NULL DEFAULT 'billing' | billing, shipping |
| status | VARCHAR(20) NOT NULL DEFAULT 'active' | active, inactive |
| label | VARCHAR(50) NOT NULL DEFAULT '' | Address label |
| name | VARCHAR(192) NULL | Address name |
| address\_1 | VARCHAR(192) NULL | Address line 1 |
| address\_2 | VARCHAR(192) NULL | Address line 2 |
| city | VARCHAR(192) NULL | City |
| state | VARCHAR(192) NULL | State |
| phone | VARCHAR(192) NULL | Phone number |
| email | VARCHAR(192) NULL | Email address |
| postcode | VARCHAR(32) NULL | Postal code |
| country | VARCHAR(100) NULL | Country |
| created\_at | DATETIME NULL |  |
| updated\_at | DATETIME NULL |  |

Indexes:

- customer\_id, is\_primary
- type
- status

## fct\_customer\_meta Table [​](https://dev.fluentcart.com/database/schema\#fct-customer-meta-table)

This table stores customer metadata

| Column | Type | Comment |
| --- | --- | --- |
| id | BIGINT UNSIGNED _Auto Increment_ | Primary key |
| customer\_id | BIGINT UNSIGNED NULL DEFAULT NULL | Reference to customer |
| meta\_key | VARCHAR(192) NULL DEFAULT NULL | Meta key |
| meta\_value | LONGTEXT NULL DEFAULT NULL | Meta value |
| created\_at | DATETIME NULL |  |
| updated\_at | DATETIME NULL |  |

Indexes:

- meta\_key
- customer\_id

## fct\_carts Table [​](https://dev.fluentcart.com/database/schema\#fct-carts-table)

This table stores shopping cart data

| Column | Type | Comment |
| --- | --- | --- |
| customer\_id | BIGINT(20) UNSIGNED NULL | Reference to customer |
| user\_id | BIGINT(20) UNSIGNED NULL | Reference to WordPress user |
| order\_id | BIGINT(20) UNSIGNED NULL | Reference to order |
| cart\_hash | VARCHAR(192) NOT NULL UNIQUE | Unique cart identifier |
| checkout\_data | LONGTEXT NULL | Checkout form data |
| cart\_data | LONGTEXT NULL | Cart contents |
| utm\_data | LONGTEXT NULL | UTM tracking data |
| coupons | LONGTEXT NULL | Applied coupons |
| first\_name | VARCHAR(192) NULL | Customer first name |
| last\_name | VARCHAR(192) NULL | Customer last name |
| email | VARCHAR(192) NULL | Customer email |
| stage | VARCHAR(30) NULL DEFAULT 'draft' | draft, pending, in-complete, completed |
| cart\_group | VARCHAR(30) NULL DEFAULT 'global' | Cart group |
| user\_agent | VARCHAR(192) NULL | User agent string |
| ip\_address | VARCHAR(50) NULL | IP address |
| completed\_at | TIMESTAMP NULL | Completion timestamp |
| created\_at | DATETIME NULL |  |
| updated\_at | DATETIME NULL |  |
| deleted\_at | TIMESTAMP NULL | Soft delete timestamp |

## fct\_product\_downloads Table [​](https://dev.fluentcart.com/database/schema\#fct-product-downloads-table)

This table stores downloadable product files

| Column | Type | Comment |
| --- | --- | --- |
| id | BIGINT UNSIGNED _Auto Increment_ | Primary key |
| post\_id | BIGINT(20) UNSIGNED NOT NULL | WordPress post ID |
| product\_variation\_id | longtext NOT NULL | Product variation ID |
| download\_identifier | VARCHAR(100) NOT NULL UNIQUE | Unique download identifier |
| title | VARCHAR(192) NULL | Download title |
| type | VARCHAR(100) NULL | Download type |
| driver | VARCHAR(100) NULL DEFAULT 'local' | Storage driver |
| file\_name | VARCHAR(192) NULL | File name |
| file\_path | TEXT NULL | File path |
| file\_url | TEXT NULL | File URL |
| file\_size | TEXT NULL | File size |
| settings | TEXT NULL | Download settings |
| serial | INT NULL | Serial number |
| created\_at | DATETIME NULL |  |
| updated\_at | DATETIME NULL |  |

## fct\_subscription\_meta Table [​](https://dev.fluentcart.com/database/schema\#fct-subscription-meta-table)

This table stores subscription metadata

| Column | Type | Comment |
| --- | --- | --- |
| id | BIGINT UNSIGNED _Auto Increment_ | Primary key |
| subscription\_id | BIGINT UNSIGNED NULL DEFAULT NULL | Reference to subscription |
| meta\_key | VARCHAR(192) NULL DEFAULT NULL | Meta key |
| meta\_value | LONGTEXT NULL DEFAULT NULL | Meta value |
| created\_at | DATETIME NULL |  |
| updated\_at | DATETIME NULL |  |

Indexes:

- subscription\_id
- meta\_key

## fct\_activity Table [​](https://dev.fluentcart.com/database/schema\#fct-activity-table)

This table stores system activity and audit logs

| Column | Type | Comment |
| --- | --- | --- |
| id | BIGINT UNSIGNED _Auto Increment_ | Primary key |
| status | VARCHAR(20) NOT NULL DEFAULT 'info' | success / warning / failed / info |
| log\_type | VARCHAR(20) NOT NULL DEFAULT 'activity' | activity, api |
| module\_type | VARCHAR(100) NOT NULL DEFAULT 'order' | Full model path |
| module\_id | BIGINT NULL | Related record ID |
| module\_name | VARCHAR(192) NOT NULL DEFAULT 'order' | order, product, user, coupon, subscription, payment, refund, shipment, activity |
| user\_id | BIGINT UNSIGNED NULL | User who performed action |
| title | VARCHAR(192) NULL | Activity title |
| content | LONGTEXT NULL | Activity description |
| read\_status | VARCHAR(20) NOT NULL DEFAULT 'unread' | read, unread |
| created\_by | VARCHAR(100) NOT NULL DEFAULT 'FCT-BOT' | Creator identifier |
| created\_at | DATETIME NULL |  |
| updated\_at | DATETIME NULL |  |

Indexes:

- module\_id

## fct\_licenses Table (Pro Plugin) [​](https://dev.fluentcart.com/database/schema\#fct-licenses-table-pro-plugin)

This table stores software license management

| Column | Type | Comment |
| --- | --- | --- |
| id | bigint unsigned _Auto Increment_ |  |
| status | varchar(45) _NULL_ | active, inactive, expired |
| limit | bigint unsigned | Activation limit |
| activation\_count | bigint unsigned | Current activations |
| license\_key | varchar(192) _NULL_ | License key |
| product\_id | bigint unsigned | WordPress post ID |
| variation\_id | bigint unsigned | Variation ID |
| order\_id | bigint unsigned | Reference to fct\_orders |
| parent\_id | bigint unsigned _NULL_ | Parent license ID |
| customer\_id | bigint unsigned | Reference to fct\_customers |
| expiration\_date | datetime _NULL_ | License expiration |
| last\_reminder\_sent | datetime _NULL_ | Last reminder date |
| last\_reminder\_type | varchar(50) _NULL_ | Reminder type |
| subscription\_id | bigint unsigned | Associated subscription |
| config | json _NULL_ | License configuration |
| created\_at | timestamp _NULL_ |  |
| updated\_at | timestamp _NULL_ |  |

## fct\_license\_activations Table (Pro Plugin) [​](https://dev.fluentcart.com/database/schema\#fct-license-activations-table-pro-plugin)

This table stores license activation tracking

| Column | Type | Comment |
| --- | --- | --- |
| id | bigint unsigned _Auto Increment_ |  |
| site\_id | bigint unsigned | Reference to fct\_license\_sites |
| license\_id | bigint unsigned | Reference to fct\_licenses |
| status | varchar(45) _NULL_ | active, inactive |
| is\_local | tinyint _NULL_ | Local activation flag |
| product\_id | bigint unsigned | WordPress post ID |
| variation\_id | bigint unsigned | Variation ID |
| activation\_method | varchar(45) _NULL_ | key\_based, etc. |
| activation\_hash | varchar(99) _NULL_ | Activation hash |
| last\_update\_version | varchar(45) _NULL_ | Last update version |
| last\_update\_date | datetime _NULL_ | Last update date |
| created\_at | timestamp _NULL_ |  |
| updated\_at | timestamp _NULL_ |  |

## fct\_license\_sites Table (Pro Plugin) [​](https://dev.fluentcart.com/database/schema\#fct-license-sites-table-pro-plugin)

This table stores license site management

| Column | Type | Comment |
| --- | --- | --- |
| id | bigint unsigned _Auto Increment_ |  |
| license\_id | bigint unsigned | Reference to fct\_licenses |
| site\_url | varchar(255) | Site URL |
| site\_name | varchar(255) _NULL_ | Site name |
| status | varchar(45) _NULL_ | active, inactive |
| created\_at | timestamp _NULL_ |  |
| updated\_at | timestamp _NULL_ |  |

## fct\_shipping\_zones Table [​](https://dev.fluentcart.com/database/schema\#fct-shipping-zones-table)

This table stores shipping zones configuration

| Column | Type | Comment |
| --- | --- | --- |
| id | BIGINT UNSIGNED _Auto Increment_ | Primary key |
| name | VARCHAR(192) NOT NULL | Zone name |
| regions | LONGTEXT NULL | Zone regions (JSON) |
| order | INT UNSIGNED NOT NULL DEFAULT 0 | Display order |
| created\_at | DATETIME NULL |  |
| updated\_at | DATETIME NULL |  |

Indexes:

- order

## fct\_shipping\_methods Table [​](https://dev.fluentcart.com/database/schema\#fct-shipping-methods-table)

This table stores shipping methods within zones

| Column | Type | Comment |
| --- | --- | --- |
| id | BIGINT UNSIGNED _Auto Increment_ | Primary key |
| zone\_id | BIGINT UNSIGNED NOT NULL | Reference to shipping zone |
| title | VARCHAR(192) NOT NULL | Method title |
| type | VARCHAR(50) NOT NULL | Method type |
| settings | LONGTEXT NULL | Method settings |
| is\_enabled | TINYINT(1) NOT NULL DEFAULT 1 | Enabled flag |
| amount | BIGINT UNSIGNED NULL DEFAULT 0 | Shipping amount |
| order | INT UNSIGNED NOT NULL DEFAULT 0 | Display order |
| created\_at | DATETIME NULL |  |
| updated\_at | DATETIME NULL |  |

Indexes:

- zone\_id
- order

## fct\_shipping\_classes Table [​](https://dev.fluentcart.com/database/schema\#fct-shipping-classes-table)

This table stores shipping classes

| Column | Type | Comment |
| --- | --- | --- |
| id | BIGINT UNSIGNED _Auto Increment_ | Primary key |
| name | VARCHAR(192) NOT NULL | Class name |
| cost | DECIMAL(10,2) NOT NULL DEFAULT 0.00 | Shipping cost |
| per\_item | TINYINT(1) NOT NULL DEFAULT 0 | Per item flag |
| type | VARCHAR(20) NOT NULL DEFAULT 'fixed' | Class type |
| created\_at | DATETIME NULL |  |
| updated\_at | DATETIME NULL |  |

Indexes:

- name

## fct\_tax\_classes Table [​](https://dev.fluentcart.com/database/schema\#fct-tax-classes-table)

This table stores tax class definitions

| Column | Type | Comment |
| --- | --- | --- |
| id | BIGINT UNSIGNED _Auto Increment_ | Primary key |
| title | VARCHAR(192) NULL | Tax class title |
| slug | VARCHAR(100) NULL | Tax class slug |
| description | LONGTEXT NULL | Tax class description |
| meta | JSON DEFAULT NULL | Tax class metadata |
| created\_at | DATETIME NULL |  |
| updated\_at | DATETIME NULL |  |

## fct\_tax\_rates Table [​](https://dev.fluentcart.com/database/schema\#fct-tax-rates-table)

This table stores tax rate configurations

| Column | Type | Comment |
| --- | --- | --- |
| id | BIGINT UNSIGNED _Auto Increment_ | Primary key |
| class\_id | BIGINT UNSIGNED NOT NULL | Tax class ID |
| country | VARCHAR(45) NULL | Country code |
| state | VARCHAR(45) NULL | State code |
| postcode | TEXT NULL | Postal code (supports ranges) |
| city | VARCHAR(45) NULL | City |
| rate | VARCHAR(45) NULL | Tax rate |
| name | VARCHAR(45) NULL | Tax name |
| group | VARCHAR(45) NULL | Tax group |
| priority | INT UNSIGNED NULL DEFAULT 1 | Priority |
| is\_compound | TINYINT UNSIGNED NULL DEFAULT 0 | Compound tax flag |
| for\_shipping | TINYINT UNSIGNED NULL DEFAULT 0 | Apply to shipping |
| for\_order | TINYINT UNSIGNED NULL DEFAULT 0 | Apply to order |

Indexes:

- class\_id
- priority

## fct\_meta Table [​](https://dev.fluentcart.com/database/schema\#fct-meta-table)

This table stores generic metadata for various objects

| Column | Type | Comment |
| --- | --- | --- |
| id | BIGINT UNSIGNED _Auto Increment_ | Primary key |
| object\_type | VARCHAR(50) NOT NULL | Object type |
| object\_id | BIGINT NULL | Object ID |
| meta\_key | VARCHAR(192) NOT NULL | Meta key |
| meta\_value | LONGTEXT NULL | Meta value |
| created\_at | DATETIME NULL |  |
| updated\_at | DATETIME NULL |  |

Indexes:

- object\_type
- object\_id

## fct\_label Table [​](https://dev.fluentcart.com/database/schema\#fct-label-table)

This table stores labels for tagging objects

| Column | Type | Comment |
| --- | --- | --- |
| id | BIGINT UNSIGNED _Auto Increment_ | Primary key |
| value | VARCHAR(192) NOT NULL UNIQUE | Label value (unique) |
| created\_at | DATETIME NULL |  |
| updated\_at | DATETIME NULL |  |

## fct\_order\_meta Table [​](https://dev.fluentcart.com/database/schema\#fct-order-meta-table)

This table stores order metadata

| Column | Type | Comment |
| --- | --- | --- |
| id | BIGINT UNSIGNED _Auto Increment_ | Primary key |
| order\_id | BIGINT(20) NULL | Reference to order |
| meta\_key | VARCHAR(192) NOT NULL | Meta key |
| meta\_value | LONGTEXT NULL | Meta value |
| created\_at | DATETIME NULL |  |
| updated\_at | DATETIME NULL |  |

Indexes:

- order\_id

## fct\_order\_tax\_rate Table [​](https://dev.fluentcart.com/database/schema\#fct-order-tax-rate-table)

This table stores order tax rate information

| Column | Type | Comment |
| --- | --- | --- |
| id | BIGINT(20) UNSIGNED _Auto Increment_ | Primary key |
| order\_id | BIGINT(20) UNSIGNED NOT NULL | Reference to order |
| tax\_rate\_id | BIGINT(20) UNSIGNED NOT NULL | Reference to tax rate |
| shipping\_tax | BIGINT NULL | Shipping tax amount |
| order\_tax | BIGINT NULL | Order tax amount |
| total\_tax | BIGINT NULL | Total tax amount |
| meta | JSON DEFAULT NULL | Tax meta data |
| filed\_at | DATETIME NULL | Filed at |
| created\_at | DATETIME NULL |  |
| updated\_at | DATETIME NULL |  |

## fct\_webhook\_logger Table [​](https://dev.fluentcart.com/database/schema\#fct-webhook-logger-table)

This table stores webhook delivery logs and status

| Column | Type | Comment |
| --- | --- | --- |
| id | BIGINT UNSIGNED _Auto Increment_ | Primary key |
| source | VARCHAR(20) NOT NULL | Webhook source |
| event\_type | VARCHAR(100) NOT NULL | Event type |
| payload | LONGTEXT NULL | Webhook payload |
| status | VARCHAR(20) NOT NULL DEFAULT 'pending' | pending, sent, failed |
| created\_at | DATETIME NULL |  |
| updated\_at | DATETIME NULL |  |

## fct\_scheduled\_actions Table [​](https://dev.fluentcart.com/database/schema\#fct-scheduled-actions-table)

This table stores background job scheduling and execution

| Column | Type | Comment |
| --- | --- | --- |
| id | BIGINT UNSIGNED _Auto Increment_ | Primary key |
| scheduled\_at | DATETIME NULL | When to run the action |
| action | VARCHAR(192) NULL | Action to perform |
| status | VARCHAR(20) NULL | pending, processing, completed, failed |
| group | VARCHAR(100) NULL | order, subscription |
| object\_id | BIGINT UNSIGNED NULL DEFAULT NULL | Related object ID |
| object\_type | VARCHAR(100) NULL DEFAULT NULL | Object type |
| completed\_at | TIMESTAMP NULL | When action was completed |
| retry\_count | INT UNSIGNED DEFAULT 0 | Number of retries |
| data | JSON NULL | Action data |
| created\_at | DATETIME NULL |  |
| updated\_at | DATETIME NULL |  |
| response\_note | LONGTEXT NULL | Response or error message |

Indexes:

- scheduled\_at
- status

## fct\_atts\_groups Table [​](https://dev.fluentcart.com/database/schema\#fct-atts-groups-table)

This table stores attribute groups for product attributes

| Column | Type | Comment |
| --- | --- | --- |
| id | BIGINT(20) UNSIGNED _Auto Increment_ | Primary key |
| title | VARCHAR(192) NOT NULL UNIQUE | Group title |
| slug | VARCHAR(192) NOT NULL UNIQUE | Group slug |
| description | LONGTEXT NULL | Group description |
| settings | LONGTEXT NULL | Group settings |
| created\_at | DATETIME NULL |  |
| updated\_at | DATETIME NULL |  |

## fct\_atts\_terms Table [​](https://dev.fluentcart.com/database/schema\#fct-atts-terms-table)

This table stores attribute terms within groups

| Column | Type | Comment |
| --- | --- | --- |
| id | BIGINT(20) UNSIGNED _Auto Increment_ | Primary key |
| group\_id | BIGINT(20) UNSIGNED | Reference to attribute group |
| serial | INT(11) UNSIGNED | Term order |
| title | VARCHAR(192) NOT NULL | Term title |
| slug | VARCHAR(192) NOT NULL | Term slug |
| description | LONGTEXT NULL | Term description |
| settings | LONGTEXT NULL | Term settings |
| created\_at | DATETIME NULL |  |
| updated\_at | DATETIME NULL |  |

Indexes:

- group\_id

## fct\_atts\_relations Table [​](https://dev.fluentcart.com/database/schema\#fct-atts-relations-table)

This table stores relationships between attributes and objects

| Column | Type | Comment |
| --- | --- | --- |
| id | BIGINT(20) UNSIGNED _Auto Increment_ | Primary key |
| group\_id | BIGINT(20) UNSIGNED NOT NULL | Reference to attribute group |
| term\_id | BIGINT(20) UNSIGNED NOT NULL | Reference to attribute term |
| object\_id | BIGINT(20) UNSIGNED NOT NULL | Related object ID |
| created\_at | DATETIME NULL |  |
| updated\_at | DATETIME NULL |  |

Indexes:

- group\_id
- term\_id
- object\_id

## fct\_label\_relationships Table [​](https://dev.fluentcart.com/database/schema\#fct-label-relationships-table)

This table stores polymorphic relationships between labels and objects

| Column | Type | Comment |
| --- | --- | --- |
| id | BIGINT UNSIGNED _Auto Increment_ | Primary key |
| label\_id | BIGINT(20) NOT NULL | Reference to label |
| labelable\_id | BIGINT(20) NOT NULL | Related object ID |
| labelable\_type | VARCHAR(192) NOT NULL | Object type |
| created\_at | DATETIME NULL |  |
| updated\_at | DATETIME NULL |  |

Indexes:

- label\_id
- labelable\_id

## Pro Plugin Tables [​](https://dev.fluentcart.com/database/schema\#pro-plugin-tables)

### fct\_licenses Table [​](https://dev.fluentcart.com/database/schema\#fct-licenses-table)

This table stores software licenses (Pro feature)

| Column | Type | Comment |
| --- | --- | --- |
| id | bigint unsigned _Auto Increment_ |  |
| status | varchar(45) | active, inactive, expired |
| limit | int _NULL_ | Activation limit |
| license\_key | varchar(192) | License key |
| product\_id | bigint unsigned _NULL_ | Related product |
| customer\_id | bigint unsigned _NULL_ | License owner |
| order\_id | bigint unsigned _NULL_ | Related order |
| expiration\_date | datetime _NULL_ | License expiration |
| created\_at | datetime _NULL_ |  |
| updated\_at | datetime _NULL_ |  |

### fct\_license\_activations Table [​](https://dev.fluentcart.com/database/schema\#fct-license-activations-table)

This table stores license activation records (Pro feature)

| Column | Type | Comment |
| --- | --- | --- |
| id | bigint unsigned _Auto Increment_ |  |
| site\_id | bigint unsigned | Reference to license site |
| license\_id | bigint unsigned | Reference to license |
| status | varchar(45) | active, inactive |
| product\_id | bigint unsigned _NULL_ | Related product |
| activation\_hash | varchar(192) | Activation hash |
| created\_at | datetime _NULL_ |  |
| updated\_at | datetime _NULL_ |  |

### fct\_license\_sites Table [​](https://dev.fluentcart.com/database/schema\#fct-license-sites-table)

This table stores licensed sites (Pro feature)

| Column | Type | Comment |
| --- | --- | --- |
| id | bigint unsigned _Auto Increment_ |  |
| license\_id | bigint unsigned | Reference to license |
| site\_url | varchar(500) | Site URL |
| site\_name | varchar(192) _NULL_ | Site name |
| status | varchar(45) | active, inactive |
| created\_at | datetime _NULL_ |  |
| updated\_at | datetime _NULL_ |  |

### fct\_license\_meta Table [​](https://dev.fluentcart.com/database/schema\#fct-license-meta-table)

This table stores license metadata (Pro feature)

| Column | Type | Comment |
| --- | --- | --- |
| id | BIGINT UNSIGNED AUTO\_INCREMENT, PRIMARY KEY |  |
| object\_id | BIGINT UNSIGNED NULL DEFAULT NULL | Reference to object (license/activation/site) |
| object\_type | VARCHAR(100) NULL DEFAULT NULL | Can be: license / activation / site |
| meta\_key | VARCHAR(255) NULL DEFAULT NULL | Meta key |
| meta\_value | LONGTEXT NULL DEFAULT NULL | Meta value (JSON or string) |
| created\_at | TIMESTAMP NULL |  |
| updated\_at | TIMESTAMP NULL |  |

Indexes:

- meta\_key
- object\_type
- object\_id

### fct\_order\_promotions Table [​](https://dev.fluentcart.com/database/schema\#fct-order-promotions-table)

This table stores order promotion data (Pro feature)

| Column | Type | Comment |
| --- | --- | --- |
| id | BIGINT(20) UNSIGNED AUTO\_INCREMENT, PRIMARY KEY |  |
| hash | VARCHAR(100) NOT NULL |  |
| parent\_id | BIGINT(20) UNSIGNED NULL |  |
| type | VARCHAR(50) NOT NULL |  |
| status | VARCHAR(50) NOT NULL DEFAULT 'draft' |  |
| src\_object\_id | BIGINT(20) UNSIGNED NULL |  |
| src\_object\_type | VARCHAR(50) DEFAULT NULL |  |
| title | VARCHAR(194) DEFAULT NULL |  |
| description | TEXT DEFAULT NULL |  |
| conditions | JSON DEFAULT NULL |  |
| config | JSON DEFAULT NULL |  |
| priority | INT NOT NULL DEFAULT 1 |  |
| created\_at | DATETIME NULL |  |
| updated\_at | DATETIME NULL |  |

Indexes:

- (type, status, src\_object\_id, src\_object\_type)

### fct\_order\_promotion\_stats Table [​](https://dev.fluentcart.com/database/schema\#fct-order-promotion-stats-table)

This table stores promotion statistics (Pro feature)

| Column | Type | Comment |
| --- | --- | --- |
| id | BIGINT(20) UNSIGNED AUTO\_INCREMENT, PRIMARY KEY |  |
| promotion\_id | BIGINT(20) UNSIGNED NOT NULL |  |
| order\_id | BIGINT(20) UNSIGNED NOT NULL |  |
| object\_id | BIGINT(20) UNSIGNED NOT NULL |  |
| amount | BIGINT NOT NULL DEFAULT '0' |  |
| status | VARCHAR(50) NOT NULL DEFAULT 'offered' |  |
| created\_at | DATETIME NULL |  |
| updated\_at | DATETIME NULL |  |

Indexes:

- (promotion\_id, object\_id, order\_id)

* * *

Today

Hi! I’m your AI assistant. How can I assist you today?

Just now

Powered by **FluentBot**


---

---

