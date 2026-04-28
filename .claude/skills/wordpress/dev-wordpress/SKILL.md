---
name: dev-wordpress
description: Développement WordPress expert conforme aux standards modernes (blocs, thèmes, plugins, REST API, Interactivity API). Utilise ce skill pour tout développement WordPress, création de blocs/plugins/thèmes ou guidance de code suivant les bonnes pratiques WordPress 6.9+.
compatibility: WordPress 6.9+ (PHP 7.2.24+). Filesystem-based agent with bash + node. Some workflows require WP-CLI.
user-invocable: true
metadata:
  brand: schoolsWP
  version: 1.0.0
  based-on: WordPress/agent-skills
---

# schoolsWP Dev Skills

Expert WordPress development knowledge aligned with modern standards. This skill ensures AI assistants provide up-to-date, best-practice WordPress development guidance instead of generic or legacy patterns.

## When to Use

Invoke this skill when the user:

- Develops **WordPress blocks** (Gutenberg): creation, registration, attributes, InnerBlocks
- Builds **block themes**: theme.json, template parts, patterns, style variations
- Creates **plugins**: hooks, activation/deactivation, Settings API, admin UI
- Works with **REST API**: custom endpoints, authentication, permissions
- Uses **Interactivity API**: client-side reactivity, state management
- Needs **WP-CLI** commands or operational guidance
- Asks about **performance** optimization for WordPress
- Requires **security** best practices (nonces, capabilities, sanitization, escaping)

## Inputs Required

Before proceeding, gather:

| Input | Required | Description |
|-------|----------|-------------|
| `repo_root` | Yes | Absolute path to the project root |
| `wp_version` | Recommended | Target WordPress version (default: 6.9+) |
| `php_version` | Recommended | Target PHP version (default: 8.0+) |
| `context` | Yes | Block, plugin, theme, or API development |

## Core Principles

### 1. Modern WordPress First

Always prefer modern WordPress patterns:

- **Blocks over shortcodes**: Use Gutenberg blocks, not legacy shortcodes
- **block.json over PHP registration**: Declarative block metadata
- **theme.json over functions.php**: Configuration over code
- **Interactivity API over jQuery**: Native WordPress reactivity
- **REST API over admin-ajax**: Modern API patterns

### 2. Standards Compliance

- Follow [WordPress Coding Standards](https://developer.wordpress.org/coding-standards/)
- Use PHPStan/PHPCS for static analysis
- Escape output, sanitize input, validate data
- Apply principle of least privilege for capabilities

### 3. Performance by Default

- Lazy load scripts and styles
- Use block.json `viewScript`/`editorScript` for automatic enqueuing
- Leverage theme.json for CSS generation
- Avoid render-blocking resources

## Procedure

### Step 0: Triage and Context

1. Identify the development context (block, plugin, theme, API)
2. Check existing codebase structure
3. Determine WordPress and PHP version targets
4. Review existing patterns in the project

### Step 1: Block Development

When creating or modifying blocks:

```
1. Use `@wordpress/create-block` for scaffolding
2. Ensure apiVersion: 3 in block.json
3. Choose appropriate model:
   - Static: Server-rendered, no save function
   - Dynamic: Server-rendered with render.php
   - Interactive: Client-side with Interactivity API
4. Register via block.json (not PHP)
5. Use InnerBlocks for composition
```

Reference: [references/block-development.md](references/block-development.md)

### Step 2: Plugin Development

When creating plugins:

```
1. Single entry point with plugin header
2. Namespace all code (PSR-4 autoloading preferred)
3. Hooks: actions and filters, not global functions
4. Activation/deactivation/uninstall hooks properly
5. Settings API for options pages
6. Capabilities for access control
```

Reference: [references/plugin-development.md](references/plugin-development.md)

### Step 3: Theme Development

When creating block themes:

```
1. theme.json as single source of truth
2. Templates in /templates directory
3. Template parts in /parts directory
4. Patterns in /patterns directory
5. style.css for metadata only (styles in theme.json)
6. No functions.php unless absolutely necessary
```

Reference: [references/theme-development.md](references/theme-development.md)

### Step 4: REST API

When working with REST API:

```
1. Register routes in rest_api_init hook
2. Use permission_callback for all endpoints
3. Validate and sanitize with registered arguments
4. Return WP_REST_Response or WP_Error
5. Version your API (v1, v2, etc.)
```

Reference: [references/rest-api.md](references/rest-api.md)

### Step 5: Security Checklist

Every WordPress code must:

- [ ] Escape all output (`esc_html`, `esc_attr`, `esc_url`, `wp_kses`)
- [ ] Sanitize all input (`sanitize_text_field`, `absint`, etc.)
- [ ] Verify nonces for form submissions
- [ ] Check capabilities before actions
- [ ] Use prepared statements for database queries

## Verification

Before considering work complete:

| Check | Method |
|-------|--------|
| No PHP errors | `wp_debug` enabled, clean logs |
| Coding standards | PHPCS with WordPress ruleset |
| Static analysis | PHPStan level 6+ |
| Block validation | Block renders correctly in editor and frontend |
| Security | All inputs sanitized, outputs escaped |
| Performance | No render-blocking, lazy-loaded assets |

## Failure Modes / Debugging

| Issue | Diagnostic | Solution |
|-------|------------|----------|
| Block not appearing | Check `block.json` registration | Verify `register_block_type` path |
| REST endpoint 403 | Permission callback failing | Check `current_user_can()` logic |
| Theme.json not applying | JSON syntax error | Validate with JSON linter |
| Interactivity not working | Missing `wp-interactivity` dependency | Add to `viewScriptModule` |

## Escalation

When this skill is insufficient:

1. Consult [WordPress Developer Documentation](https://developer.wordpress.org/)
2. Check [WordPress GitHub](https://github.com/WordPress/gutenberg) for latest patterns
3. Reference [Block Editor Handbook](https://developer.wordpress.org/block-editor/)
4. Ask in [WordPress Slack](https://make.wordpress.org/chat/) #core-editor

## Related Skills

- `n8n-workflow-patterns` for WordPress automation workflows
- `04_WordPress` for content management procedures
- `05_Branding` for schoolsWP content guidelines

---

**schoolsWP Dev Skills** — Modern WordPress development, the schoolsWP way.
