# n8n Node Configuration — Detailed Reference

## Operation-Specific Configuration

### Slack Node Examples

#### Post Message
```javascript
{
  "resource": "message",
  "operation": "post",
  "channel": "#general",      // Required
  "text": "Hello!",           // Required
  "attachments": [],          // Optional
  "blocks": []                // Optional
}
```

#### Update Message
```javascript
{
  "resource": "message",
  "operation": "update",
  "messageId": "1234567890",  // Required (different from post!)
  "text": "Updated!",         // Required
  "channel": "#general"       // Optional (can be inferred)
}
```

#### Create Channel
```javascript
{
  "resource": "channel",
  "operation": "create",
  "name": "new-channel",      // Required
  "isPrivate": false          // Optional
  // Note: text NOT required for this operation
}
```

### HTTP Request Node Examples

#### GET Request
```javascript
{
  "method": "GET",
  "url": "https://api.example.com/users",
  "authentication": "predefinedCredentialType",
  "nodeCredentialType": "httpHeaderAuth",
  "sendQuery": true,                    // Optional
  "queryParameters": {                  // Shows when sendQuery=true
    "parameters": [
      {
        "name": "limit",
        "value": "100"
      }
    ]
  }
}
```

#### POST with JSON
```javascript
{
  "method": "POST",
  "url": "https://api.example.com/users",
  "authentication": "none",
  "sendBody": true,                     // Required for POST
  "body": {                             // Required when sendBody=true
    "contentType": "json",
    "content": {
      "name": "John Doe",
      "email": "john@example.com"
    }
  }
}
```

### IF Node Examples

#### String Comparison (Binary)
```javascript
{
  "conditions": {
    "string": [
      {
        "value1": "={{$json.status}}",
        "operation": "equals",
        "value2": "active"              // Binary: needs value2
      }
    ]
  }
}
```

#### Empty Check (Unary)
```javascript
{
  "conditions": {
    "string": [
      {
        "value1": "={{$json.email}}",
        "operation": "isEmpty",
        // No value2 - unary operator
        "singleValue": true             // Auto-added by sanitization
      }
    ]
  }
}
```

---

## Handling Conditional Requirements

### Example: HTTP Request Body

**Scenario**: body field required, but only sometimes

**Rule**:
```
body is required when:
  - sendBody = true AND
  - method IN (POST, PUT, PATCH, DELETE)
```

**How to discover**:
```javascript
// Option 1: Read validation error
validate_node({...});
// Error: "body required when sendBody=true"

// Option 2: Search for the property
get_node({
  nodeType: "nodes-base.httpRequest",
  mode: "search_properties",
  propertyQuery: "body"
});
// Shows: body property with displayOptions rules

// Option 3: Try minimal config and iterate
// Start without body, validation will tell you if needed
```

### Example: IF Node singleValue

**Scenario**: singleValue property appears for unary operators

**Rule**:
```
singleValue should be true when:
  - operation IN (isEmpty, isNotEmpty, true, false)
```

**Good news**: Auto-sanitization fixes this!

**Manual check**:
```javascript
get_node({
  nodeType: "nodes-base.if",
  detail: "full"
});
// Shows complete schema with operator-specific rules
```

---

## Configuration Anti-Patterns

### ❌ Don't: Over-configure Upfront

**Bad**:
```javascript
// Adding every possible field
{
  "method": "GET",
  "url": "...",
  "sendQuery": false,
  "sendHeaders": false,
  "sendBody": false,
  "timeout": 10000,
  "ignoreResponseCode": false,
  // ... 20 more optional fields
}
```

**Good**:
```javascript
// Start minimal
{
  "method": "GET",
  "url": "...",
  "authentication": "none"
}
// Add fields only when needed
```

### ❌ Don't: Skip Validation

**Bad**:
```javascript
// Configure and deploy without validating
const config = {...};
n8n_update_partial_workflow({...});  // YOLO
```

**Good**:
```javascript
// Validate before deploying
const config = {...};
const result = validate_node({...});
if (result.valid) {
  n8n_update_partial_workflow({...});
}
```

### ❌ Don't: Ignore Operation Context

**Bad**:
```javascript
// Same config for all Slack operations
{
  "resource": "message",
  "operation": "post",
  "channel": "#general",
  "text": "..."
}

// Then switching operation without updating config
{
  "resource": "message",
  "operation": "update",  // Changed
  "channel": "#general",  // Wrong field for update!
  "text": "..."
}
```

**Good**:
```javascript
// Check requirements when changing operation
get_node({
  nodeType: "nodes-base.slack"
});
// See what update operation needs (messageId, not channel)
```

---

## Best Practices

### ✅ Do

1. **Start with get_node (standard detail)**
   - ~1-2K tokens response
   - Covers 95% of configuration needs
   - Default detail level

2. **Validate iteratively**
   - Configure → Validate → Fix → Repeat
   - Average 2-3 iterations is normal
   - Read validation errors carefully

3. **Use search_properties mode when stuck**
   - If field seems missing, search for it
   - Understand what controls field visibility
   - `get_node({mode: "search_properties", propertyQuery: "..."})`

4. **Respect operation context**
   - Different operations = different requirements
   - Always check get_node when changing operation
   - Don't assume configs are transferable

5. **Trust auto-sanitization**
   - Operator structure fixed automatically
   - Don't manually add/remove singleValue
   - IF/Switch metadata added on save

### ❌ Don't

1. **Jump to detail="full" immediately**
   - Try standard detail first
   - Only escalate if needed
   - Full schema is 3-8K tokens

2. **Configure blindly**
   - Always validate before deploying
   - Understand why fields are required
   - Use search_properties for conditional fields

3. **Copy configs without understanding**
   - Different operations need different fields
   - Validate after copying
   - Adjust for new context

4. **Manually fix auto-sanitization issues**
   - Let auto-sanitization handle operator structure
   - Focus on business logic
   - Save and let system fix structure

---

## Detailed References

For comprehensive guides on specific topics:

- **[DEPENDENCIES.md](DEPENDENCIES.md)** - Deep dive into property dependencies and displayOptions
- **[OPERATION_PATTERNS.md](OPERATION_PATTERNS.md)** - Common configuration patterns by node type

---

## Summary

**Configuration Strategy**:
1. Start with `get_node` (standard detail is default)
2. Configure required fields for operation
3. Validate configuration
4. Search properties if stuck
5. Iterate until valid (avg 2-3 cycles)
6. Deploy with confidence

**Key Principles**:
- **Operation-aware**: Different operations = different requirements
- **Progressive disclosure**: Start minimal, add as needed
- **Dependency-aware**: Understand field visibility rules
- **Validation-driven**: Let validation guide configuration

**Related Skills**:
- **n8n MCP Tools Expert** - How to use discovery tools correctly
- **n8n Validation Expert** - Interpret validation errors
- **n8n Expression Syntax** - Configure expression fields
- **n8n Workflow Patterns** - Apply patterns with proper configuration
