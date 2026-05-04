# Fluent ecosystem MCP servers : nomenclature des tools

Inventaire des 5 serveurs MCP open-source publies par Carlos Rodera (https://github.com/carlosrodera/fluent-mcp-servers, MIT). Total : 174 tools en mode static, 15 en mode dynamic (3 meta-tools par serveur).

Auth : WordPress Application Passwords. Endpoint : https://schoolswp.com/wp-json/...

## Vue d'ensemble

| Plugin | Tools | Couverture metier |
| --- | --- | --- |
| FluentCRM | 40 | Contacts, listes, tags, campagnes, sequences, funnels, templates, reports, webhooks |
| Fluent Support | 50 | Tickets, customers, agents, mailbox, business hours, workflows, reports, products |
| Fluent Boards | 30 | Boards, tasks, stages, labels, comments, members, attachments |
| Fluent Community | 30 | Spaces, feeds, members, courses, notifications, comments |
| Fluent Affiliate | 24 | Affiliates, referrals, payouts, creatives, reports, settings |

---

## FluentCRM

### campaign (6 tools)

| Tool | RO | Description |
| --- | --- | --- |
| `fluentcrm_campaign_list` | v | List email campaigns with optional filtering by status. Returns campaign summaries including send stats. |
| `fluentcrm_campaign_get` | v | Get detailed information about a single campaign including its settings, recipients, email body, and performance stats. |
| `fluentcrm_campaign_create` |   | Create a new email campaign in draft status. You can specify the subject, body, recipients (by tags/lists), and template. |
| `fluentcrm_campaign_schedule` |   | Schedule a draft campaign for sending. You must specify the recipients (by tags/lists) and optionally a send date. If no date is given, the ... |
| `fluentcrm_campaign_pause` |   | Pause a currently sending (working) campaign. Can be resumed later. |
| `fluentcrm_campaign_resume` |   | Resume a paused campaign to continue sending. |

### contact (8 tools)

| Tool | RO | Description |
| --- | --- | --- |
| `fluentcrm_contact_list` | v | List CRM contacts (subscribers) with optional filtering by status, tags, lists, and search. Supports pagination. |
| `fluentcrm_contact_get` | v | Get detailed information about a single contact including their tags, lists, custom fields, and activity history. |
| `fluentcrm_contact_get_by_email` | v | Look up a contact by their email address. Returns the full contact record if found. |
| `fluentcrm_contact_create` |   | Create a new CRM contact. Email is required. You can assign tags and lists at creation time. |
| `fluentcrm_contact_update` |   | Update an existing contact. Pass only the fields you want to change. Does not modify tags or lists (use dedicated tag/list tools). |
| `fluentcrm_contact_delete` |   | Permanently delete a contact from the CRM. This removes all associated data including tags, lists, and activity history. |
| `fluentcrm_contact_add_tags` |   | Add one or more tags to a contact. Existing tags are preserved. |
| `fluentcrm_contact_remove_tags` |   | Remove one or more tags from a contact. |

### funnel (4 tools)

| Tool | RO | Description |
| --- | --- | --- |
| `fluentcrm_funnel_list` | v | List all automation funnels. Funnels are multi-step workflows triggered by events (signup, tag added, purchase, etc.). |
| `fluentcrm_funnel_get` | v | Get detailed information about a specific funnel including all its steps, triggers, and subscriber metrics. |
| `fluentcrm_funnel_create` |   | Create a new automation funnel. Funnels start in draft status. Add triggers and actions, then publish to activate. |
| `fluentcrm_funnel_trigger` |   | Manually trigger a funnel for a specific contact via the webhook endpoint. The contact will enter the funnel as if the trigger event had occ... |

### list (5 tools)

| Tool | RO | Description |
| --- | --- | --- |
| `fluentcrm_list_list` | v | List all CRM lists (mailing lists). Lists are used to organize contacts into groups for campaigns and segmentation. |
| `fluentcrm_list_create` |   | Create a new mailing list for organizing contacts. |
| `fluentcrm_list_update` |   | Update an existing list name, slug, or description. |
| `fluentcrm_list_delete` |   | Permanently delete a list. Contacts in this list are not deleted, but their association with this list is removed. |
| `fluentcrm_list_attach_contact` |   | Add one or more contacts to a mailing list by their subscriber IDs. |

### report (3 tools)

| Tool | RO | Description |
| --- | --- | --- |
| `fluentcrm_report_dashboard` | v | Get CRM dashboard statistics: total contacts, active subscribers, unsubscribed, emails sent, open rate, click rate, and more. |
| `fluentcrm_report_subscribers_growth` | v | Get subscriber growth trends over time. Shows new subscribers per day/week/month in the given date range. |
| `fluentcrm_report_campaign_stats` | v | Get aggregated campaign performance statistics: emails sent, opens, clicks, unsubscribes, bounces, and revenue attribution. |

### sequence (4 tools)

| Tool | RO | Description |
| --- | --- | --- |
| `fluentcrm_sequence_list` | v | List all email sequences (Pro). Sequences are automated multi-step email drip campaigns sent on a schedule. |
| `fluentcrm_sequence_get` | v | Get detailed information about a specific sequence including its emails, delays, and subscriber count. |
| `fluentcrm_sequence_add_subscriber` |   | Add one or more contacts to a sequence. They will start receiving the sequence emails from the beginning. |
| `fluentcrm_sequence_remove_subscriber` |   | Remove one or more contacts from a sequence. They will stop receiving further emails. |

### tag (5 tools)

| Tool | RO | Description |
| --- | --- | --- |
| `fluentcrm_tag_list` | v | List all CRM tags. Tags are used to categorize and segment contacts for targeted campaigns and automations. |
| `fluentcrm_tag_create` |   | Create a new CRM tag for categorizing contacts. |
| `fluentcrm_tag_update` |   | Update an existing tag name, slug, or description. |
| `fluentcrm_tag_delete` |   | Permanently delete a tag. Contacts that had this tag will have it removed, but the contacts themselves are not deleted. |
| `fluentcrm_tag_attach_to_contact` |   | Attach a tag to one or more contacts by their subscriber IDs. This is an alternative to fluentcrm_contact_add_tags when you want to work fro... |

### template (3 tools)

| Tool | RO | Description |
| --- | --- | --- |
| `fluentcrm_template_list` | v | List all email templates. Templates provide reusable email layouts and designs for campaigns. |
| `fluentcrm_template_get` | v | Get detailed information about a specific email template including its HTML body and design settings. |
| `fluentcrm_template_create` |   | Create a new email template with HTML content. Templates can be used across multiple campaigns. |

### webhook (2 tools)

| Tool | RO | Description |
| --- | --- | --- |
| `fluentcrm_webhook_list` | v | List all configured incoming webhooks. Webhooks allow external systems to create or update contacts and trigger automations in FluentCRM. |
| `fluentcrm_webhook_create` |   | Create a new incoming webhook endpoint. The webhook URL can be used by external systems to push data into FluentCRM (contacts, tags, lists, ... |

---

## Fluent Support

### activity (1 tools)

| Tool | RO | Description |
| --- | --- | --- |
| `fluentsupport_activity_list` | v | List recent activity log entries. Activities track all actions performed on tickets, customers, and agents (replies, status changes, assignm... |

### agent (5 tools)

| Tool | RO | Description |
| --- | --- | --- |
| `fluentsupport_agent_list` | v | List all support agents/staff members. Agents handle ticket responses and manage the helpdesk. |
| `fluentsupport_agent_get` | v | Get detailed information about a specific agent including their stats and settings. |
| `fluentsupport_agent_create` |   | Create a new support agent. The user_id must correspond to an existing WordPress user. |
| `fluentsupport_agent_update` |   | Update agent profile information such as name, email, or title. |
| `fluentsupport_agent_delete` |   | Remove an agent from the support team. This does not delete the underlying WordPress user. Open tickets may need to be reassigned. |

### customer (6 tools)

| Tool | RO | Description |
| --- | --- | --- |
| `fluentsupport_customer_list` | v | List support customers with optional search and pagination. Customers are the people who submit tickets. |
| `fluentsupport_customer_get` | v | Get detailed customer information including their support history, ticket count, and profile data. |
| `fluentsupport_customer_create` |   | Create a new support customer. Email is required and must be unique. The customer can then submit tickets. |
| `fluentsupport_customer_update` |   | Update customer profile fields. Fetches current state first to ensure required fields are preserved. |
| `fluentsupport_customer_delete` |   | Permanently delete a customer. This will NOT delete their tickets, but will disassociate them. |
| `fluentsupport_customer_tickets` | v | List all tickets submitted by a specific customer. Useful for viewing support history. |

### product (4 tools)

| Tool | RO | Description |
| --- | --- | --- |
| `fluentsupport_product_list` | v | List all products. Products can be associated with tickets to track which product a support request is about. |
| `fluentsupport_product_create` |   | Create a new product for ticket categorization. |
| `fluentsupport_product_update` |   | Update an existing product name or description. |
| `fluentsupport_product_delete` |   | Permanently delete a product. Existing ticket associations will be removed. |

### report (6 tools)

| Tool | RO | Description |
| --- | --- | --- |
| `fluentsupport_report_overall_stats` | v | Get overall support statistics: total tickets, open tickets, closed tickets, average response time, and resolution time. |
| `fluentsupport_report_ticket_growth` | v | Get ticket creation trends over time. Shows how many tickets were created per day, week, or month in the given date range. |
| `fluentsupport_report_resolve_stats` | v | Get ticket resolution statistics: average time to resolve, resolution rate, and breakdown by priority. |
| `fluentsupport_report_response_stats` | v | Get response time statistics: average first response time, average response time, and response count breakdown. |
| `fluentsupport_report_agent_stats` | v | Get per-agent performance metrics: tickets handled, average response time, resolution count, and satisfaction scores. |
| `fluentsupport_report_personal_stats` | v | Get personal support stats for the authenticated agent: your tickets, response times, and resolution metrics. |

### saved (5 tools)

| Tool | RO | Description |
| --- | --- | --- |
| `fluentsupport_saved_reply_list` | v | List all saved reply templates. Saved replies are pre-written response templates that agents can quickly insert when replying to tickets. |
| `fluentsupport_saved_reply_get` | v | Get full details of a specific saved reply template including its content. |
| `fluentsupport_saved_reply_create` |   | Create a new saved reply template. Use dynamic placeholders like {{customer.name}}, {{ticket.title}} for personalized responses. |
| `fluentsupport_saved_reply_update` |   | Update an existing saved reply template. Pass only the fields to change. |
| `fluentsupport_saved_reply_delete` |   | Permanently delete a saved reply template. |

### settings (2 tools)

| Tool | RO | Description |
| --- | --- | --- |
| `fluentsupport_settings_get` | v | Get Fluent Support general settings: business hours, email notifications, ticket defaults, and more. |
| `fluentsupport_settings_mailboxes` | v | List all configured mailboxes/inboxes. Mailboxes determine where incoming ticket emails are received. |

### tag (4 tools)

| Tool | RO | Description |
| --- | --- | --- |
| `fluentsupport_tag_list` | v | List all ticket tags. Tags help categorize and organize tickets for filtering and reporting. |
| `fluentsupport_tag_create` |   | Create a new ticket tag for categorizing tickets. |
| `fluentsupport_tag_update` |   | Update an existing tag name or description. |
| `fluentsupport_tag_delete` |   | Permanently delete a tag. Existing ticket associations will be removed. |

### ticket (12 tools)

| Tool | RO | Description |
| --- | --- | --- |
| `fluentsupport_ticket_list` | v | List support tickets with optional filtering by status, priority, agent, customer, and product. Supports pagination and search. |
| `fluentsupport_ticket_get` | v | Get detailed information about a single support ticket including its current status, priority, assigned agent, customer, tags, and conversat... |
| `fluentsupport_ticket_create` |   | Create a new support ticket. Requires a title, email (customer email), and content. Optionally assign an agent, priority, and product. |
| `fluentsupport_ticket_update` |   | Update ticket properties such as priority, agent assignment, product, or status. Pass only the fields you want to change. |
| `fluentsupport_ticket_reply` |   | Add a response/reply to a ticket. The content supports HTML. You can add internal notes by setting is_internal to true. |
| `fluentsupport_ticket_close` |   | Close an open ticket. Changes the ticket status to "closed". |
| `fluentsupport_ticket_reopen` |   | Reopen a closed ticket. Changes the ticket status back to "active". |
| `fluentsupport_ticket_delete` |   | Permanently delete a ticket. This action cannot be undone. All responses and attachments will also be deleted. |
| `fluentsupport_ticket_bulk_actions` |   | Perform bulk operations on multiple tickets. Supported actions: close, reopen, delete, assign_agent, change_priority. |
| `fluentsupport_ticket_responses` | v | Get all responses/replies for a specific ticket. Returns the full conversation thread including internal notes. |
| `fluentsupport_ticket_add_tag` |   | Add one or more tags to a ticket. |
| `fluentsupport_ticket_remove_tag` |   | Remove a tag from a ticket. |

### workflow (5 tools)

| Tool | RO | Description |
| --- | --- | --- |
| `fluentsupport_workflow_list` | v | List all automation workflows. Workflows automate ticket routing, auto-replies, SLA enforcement, and other support actions. |
| `fluentsupport_workflow_get` | v | Get detailed information about a specific workflow including its triggers, conditions, and actions. |
| `fluentsupport_workflow_create` |   | Create a new automation workflow. Define triggers, conditions, and actions to automate support processes. |
| `fluentsupport_workflow_update` |   | Update an existing workflow. Can modify triggers, conditions, actions, status, or metadata. |
| `fluentsupport_workflow_delete` |   | Permanently delete a workflow. Active workflows should be deactivated first. |

---

## Fluent Boards

### board (6 tools)

| Tool | RO | Description |
| --- | --- | --- |
| `fluentboards_board_list` | v | List all project boards with optional filtering by type, search, and pagination. Boards are the top-level containers for stages and tasks. |
| `fluentboards_board_get` | v | Get detailed information about a single board including its stages, settings, and metadata. |
| `fluentboards_board_create` |   | Create a new project board. Requires a title and type (to-do or roadmap). Optionally include a description, currency, folder, and initial st... |
| `fluentboards_board_update` |   | Update board properties such as title or description. Pass only the fields you want to change. |
| `fluentboards_board_delete` |   | Permanently delete a board. This action cannot be undone. All stages, tasks, and associated data will also be deleted. |
| `fluentboards_board_archive` |   | Archive a board. Archived boards can be restored later. |

### comment (3 tools)

| Tool | RO | Description |
| --- | --- | --- |
| `fluentboards_comment_list` | v | List all comments for a specific task. Returns the conversation thread including replies. |
| `fluentboards_comment_create` |   | Add a new comment to a task. Supports threaded replies via parent_id. |
| `fluentboards_comment_delete` |   | Delete a comment from a task. This also removes any threaded replies and attachments. |

### label (5 tools)

| Tool | RO | Description |
| --- | --- | --- |
| `fluentboards_label_list` | v | List all labels for a specific board. Labels help categorize and visually tag tasks. |
| `fluentboards_label_create` |   | Create a new label for a board. Requires a color and background color in hex format. Optionally provide a label title. |
| `fluentboards_label_update` |   | Update an existing label. You can change its title, text color, or background color. |
| `fluentboards_label_delete` |   | Permanently delete a label from a board. Existing task associations will be removed. |
| `fluentboards_label_assign_to_task` |   | Assign a label to a task on a board. |

### member (3 tools)

| Tool | RO | Description |
| --- | --- | --- |
| `fluentboards_member_list` | v | List all members of a specific board including their roles (admin, member, viewer). |
| `fluentboards_member_add` |   | Add a user to a board as a member or viewer. The user must already exist in WordPress. |
| `fluentboards_member_remove` |   | Remove a user from a board. Their task assignments on this board may need reassignment. |

### stage (5 tools)

| Tool | RO | Description |
| --- | --- | --- |
| `fluentboards_stage_list` | v | List archived stages for a board. Active stages are returned as part of the board details (use board_get). This endpoint returns only archiv... |
| `fluentboards_stage_create` |   | Create a new stage (column) on a board. The stage is added at the end by default, or at the specified position. |
| `fluentboards_stage_update` |   | Update stage properties such as title or settings. |
| `fluentboards_stage_delete` |   | Archive (soft-delete) a stage. The stage and its tasks are hidden but can be restored later. |
| `fluentboards_stage_reorder` |   | Update the positions of multiple stages at once. Pass an array of stage IDs in the desired order. |

### task (8 tools)

| Tool | RO | Description |
| --- | --- | --- |
| `fluentboards_task_list` | v | List all tasks for a specific board. Returns tasks across all stages with their status, priority, assignees, and metadata. |
| `fluentboards_task_get` | v | Get detailed information about a single task including its description, assignees, labels, subtasks, and activity history. |
| `fluentboards_task_create` |   | Create a new task on a board. Requires a title, board_id, and stage_id. Optionally set priority, CRM contact, or mark as template. |
| `fluentboards_task_update` |   | Update a specific property of a task. Supported properties: title, description, status, priority, due_at, started_at, assignees, archived_at... |
| `fluentboards_task_delete` |   | Permanently delete a task. This action cannot be undone. All subtasks, comments, and attachments will also be deleted. |
| `fluentboards_task_move_stage` |   | Move a task to a different stage within the same board, or to a stage in a different board. Optionally set the position within the target st... |
| `fluentboards_task_clone` |   | Create a copy of an existing task. Choose which elements to include: assignees, subtasks, labels, attachments, and comments. |
| `fluentboards_task_close` |   | Close (complete) a task by setting its status to "closed" and recording the completion timestamp. |

---

## Fluent Community

### analytics (2 tools)

| Tool | RO | Description |
| --- | --- | --- |
| `fluentcommunity_analytics_stats` | v | Get overall community statistics: total members, total spaces, total posts, total comments, active members, new sign-ups, and engagement met... |
| `fluentcommunity_analytics_activity` | v | Get community activity trends over time: posts created, comments made, new members, and reactions. Useful for tracking engagement and growth... |

### comment (4 tools)

| Tool | RO | Description |
| --- | --- | --- |
| `fluentcommunity_comment_list` | v | List comments for a specific post/feed. Returns comment content, author info, and nested replies. Supports pagination. |
| `fluentcommunity_comment_create` |   | Add a comment to a post/feed. Supports threaded replies by specifying a parent_id for the comment being replied to. |
| `fluentcommunity_comment_update` |   | Update the content of an existing comment. Only the comment author or administrators can update a comment. |
| `fluentcommunity_comment_delete` |   | Permanently delete a comment. If the comment has replies, they will also be removed. This action cannot be undone. |

### course (4 tools)

| Tool | RO | Description |
| --- | --- | --- |
| `fluentcommunity_course_list` | v | List all courses in the community. Courses are structured learning paths with lessons and optional quizzes. Supports pagination. |
| `fluentcommunity_course_get` | v | Get detailed information about a specific course including its lessons, enrollment count, progress tracking, and metadata. |
| `fluentcommunity_course_enroll_user` |   | Enroll a user in a course. The user will gain access to all published lessons within the course. |
| `fluentcommunity_course_unenroll_user` |   | Remove a user's enrollment from a course. Their progress data may be retained but they will lose access to lessons. |

### feed (6 tools)

| Tool | RO | Description |
| --- | --- | --- |
| `fluentcommunity_feed_list` | v | List community posts/feeds with optional filtering by space, author, and status. Supports pagination and search. Returns post content, autho... |
| `fluentcommunity_feed_get` | v | Get detailed information about a single post including its full content, author, reactions, comments, and metadata. |
| `fluentcommunity_feed_create` |   | Create a new post/feed in a community space. Requires a space_id and message content. Posts can be published immediately or saved as drafts. |
| `fluentcommunity_feed_update` |   | Update an existing post. Can modify content, title, status, pinned state, or comment settings. Pass only the fields you want to change. |
| `fluentcommunity_feed_delete` |   | Permanently delete a post and all its associated comments. This action cannot be undone. |
| `fluentcommunity_feed_search` | v | Search across all community posts by keyword. Returns matching posts with relevance ranking. More targeted than feed_list with search parame... |

### member (5 tools)

| Tool | RO | Description |
| --- | --- | --- |
| `fluentcommunity_member_list` | v | List community members with optional search and pagination. Shows member profiles, roles, and activity status. |
| `fluentcommunity_member_get` | v | Get detailed profile information about a specific community member including their activity, spaces, and role. |
| `fluentcommunity_member_add_to_space` |   | Add a user to a community space. The user must be a WordPress user. You can optionally set their role within the space. |
| `fluentcommunity_member_remove_from_space` |   | Remove a user from a community space. The user will lose access to the space content if it is private or secret. |
| `fluentcommunity_member_update_role` |   | Change a member's role within a specific space. Roles control permissions: member (read/post), moderator (manage posts/comments), admin (ful... |

### notification (2 tools)

| Tool | RO | Description |
| --- | --- | --- |
| `fluentcommunity_notification_list` | v | List notifications for the authenticated user. Shows mentions, replies, reactions, and other community activity notifications. Supports pagi... |
| `fluentcommunity_notification_mark_read` |   | Mark one or more notifications as read. Pass specific notification IDs or omit to mark all unread notifications as read. |

### settings (2 tools)

| Tool | RO | Description |
| --- | --- | --- |
| `fluentcommunity_settings_get` | v | Get Fluent Community configuration settings: general settings, registration options, email notifications, storage configuration, and authent... |
| `fluentcommunity_settings_update` |   | Update Fluent Community configuration settings. Pass a settings group and the key-value pairs to update. Only provided fields will be change... |

### space (5 tools)

| Tool | RO | Description |
| --- | --- | --- |
| `fluentcommunity_space_list` | v | List all community spaces (groups/forums). Spaces are the main containers for posts and discussions. Supports pagination and search. |
| `fluentcommunity_space_get` | v | Get detailed information about a specific space including its settings, member count, privacy level, and description. |
| `fluentcommunity_space_create` |   | Create a new community space. Spaces can be public (anyone can join), private (invite-only), or secret (hidden from non-members). |
| `fluentcommunity_space_update` |   | Update space properties such as title, description, privacy level, or status. Pass only the fields you want to change. |
| `fluentcommunity_space_delete` |   | Permanently delete a space. This will remove all posts, comments, and member associations within the space. This action cannot be undone. |

---

## Fluent Affiliate

### affiliate (6 tools)

| Tool | RO | Description |
| --- | --- | --- |
| `fluentaffiliate_affiliate_list` | v | List all affiliates with optional filtering by status, search, and pagination. Returns affiliate profiles including earnings, referral count... |
| `fluentaffiliate_affiliate_get` | v | Get detailed information about a single affiliate including their profile, earnings summary, referral stats, payout history, and visit data. |
| `fluentaffiliate_affiliate_create` |   | Create a new affiliate. Requires a WordPress user ID or email. The affiliate will be associated with the given user account. |
| `fluentaffiliate_affiliate_update` |   | Update affiliate profile fields such as payment email, status, or referral URL. Pass only the fields you want to change. |
| `fluentaffiliate_affiliate_delete` |   | Permanently delete an affiliate. This removes the affiliate record but does not delete the WordPress user account. Existing referrals may be... |
| `fluentaffiliate_affiliate_update_status` |   | Change the status of an affiliate (approve, reject, block, or reactivate). Use this for affiliate application management. |

### payout (4 tools)

| Tool | RO | Description |
| --- | --- | --- |
| `fluentaffiliate_payout_list` | v | List all payout records with optional filtering by status, affiliate, and date range. Shows payout amounts, methods, and processing status. |
| `fluentaffiliate_payout_get` | v | Get detailed information about a specific payout including the affiliate, amount, payment method, status, and associated transactions. |
| `fluentaffiliate_payout_process` |   | Process a payout for one or more affiliates. This marks approved referrals as paid and creates a payout record. Provide affiliate IDs to inc... |
| `fluentaffiliate_payout_validate_config` | v | Validate that the payout configuration is correctly set up before processing payouts. Checks payment method settings, minimum thresholds, an... |

### portal (3 tools)

| Tool | RO | Description |
| --- | --- | --- |
| `fluentaffiliate_portal_stats` | v | Get affiliate portal statistics for the authenticated user: their total earnings, unpaid balance, referral count, visit count, and conversio... |
| `fluentaffiliate_portal_referrals` | v | Get the referral list from the affiliate portal perspective. Shows the affiliate their own referrals with status, amounts, and dates. |
| `fluentaffiliate_portal_transactions` | v | Get payout transactions from the affiliate portal perspective. Shows the affiliate their payment history including amounts, dates, and payme... |

### referral (4 tools)

| Tool | RO | Description |
| --- | --- | --- |
| `fluentaffiliate_referral_list` | v | List all referrals with optional filtering by affiliate, status, type, and date range. Returns referral details including commission amounts... |
| `fluentaffiliate_referral_get` | v | Get detailed information about a single referral including the associated affiliate, order reference, commission amount, and status. |
| `fluentaffiliate_referral_create` |   | Manually create a new referral record. Useful for crediting affiliates for offline sales or custom referral scenarios. |
| `fluentaffiliate_referral_delete` |   | Permanently delete a referral record. This cannot be undone. The affiliate earnings will be adjusted accordingly. |

### report (3 tools)

| Tool | RO | Description |
| --- | --- | --- |
| `fluentaffiliate_report_dashboard_stats` | v | Get affiliate program dashboard statistics: total affiliates, total referrals, total earnings, unpaid commissions, total visits, and convers... |
| `fluentaffiliate_report_dashboard_chart` | v | Get chart data for the affiliate dashboard showing referral and visit trends over time. Useful for visualizing affiliate program performance... |
| `fluentaffiliate_report_commerce` | v | Get commerce-specific reports for the affiliate program including revenue attributed to affiliates, top-performing affiliates, and product-l... |

### settings (3 tools)

| Tool | RO | Description |
| --- | --- | --- |
| `fluentaffiliate_settings_referral_config` | v | Get the current referral configuration including commission rates, referral types, cookie duration, and tracking settings. |
| `fluentaffiliate_settings_update_referral_config` |   | Update referral configuration settings such as default commission rate, commission type (percentage or flat), cookie duration, and tracking ... |
| `fluentaffiliate_settings_email_config` | v | Get the current email notification settings for the affiliate program: notification templates, triggers, and recipient configuration. |

### visit (1 tools)

| Tool | RO | Description |
| --- | --- | --- |
| `fluentaffiliate_visit_list` | v | List affiliate link visits/clicks with optional filtering by affiliate, date range, and pagination. Shows referral URL, landing page, IP (if... |

---

## Notes

- Mode static : tous les tools listes sont exposes au boot (boueffe le contexte).
- Mode dynamic (recommande, configure dans .mcp.json schoolsWP) : seuls 3 meta-tools par serveur sont charges (search_tools, describe_tools, execute_tool). Reduction ~96%% des tokens au boot.
- Dans le mode dynamic, l'agent decouvre les tools via search_tools, recupere les schemas via describe_tools, puis appelle execute_tool avec le name et les arguments.
- RO (read-only) : tools marques readOnlyHint=true par le serveur. Aucun side-effect cote WordPress, safe pour les agents qui inspectent.
