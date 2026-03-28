# n8n Validation Expert — Detailed Reference

## False Positives

### What Are They?
Validation warnings that are technically "wrong" but acceptable in your use case

### Common False Positives

#### 1. "Missing error handling"
**Warning**: No error handling configured

**When acceptable**:
- Simple workflows where failures are obvious
- Testing/development workflows
- Non-critical notifications

**When to fix**: Production workflows handling important data

#### 2. "No retry logic"
**Warning**: Node doesn't retry on failure

**When acceptable**:
- APIs with their own retry logic
- Idempotent operations
- Manual trigger workflows

**When to fix**: Flaky external services, production automation

#### 3. "Missing rate limiting"
**Warning**: No rate limiting for API calls

**When acceptable**:
- Internal APIs with no limits
- Low-volume workflows
- APIs with server-side rate limiting

**When to fix**: Public APIs, high-volume workflows

#### 4. "Unbounded query"
**Warning**: SELECT without LIMIT

**When acceptable**:
- Small known datasets
- Aggregation queries
- Development/testing

**When to fix**: Production queries on large tables

### Reducing False Positives

**Use `ai-friendly` profile**:
```javascript
validate_node({
  nodeType: "nodes-base.slack",
  config: {...},
  profile: "ai-friendly"  // Fewer false positives
})
```

---

## Validation Result Structure

### Complete Response
```javascript
{
  "valid": false,
  "errors": [
    {
      "type": "missing_required",
      "property": "channel",
      "message": "Channel name is required",
      "fix": "Provide a channel name (lowercase, no spaces)"
    }
  ],
  "warnings": [
    {
      "type": "best_practice",
      "property": "errorHandling",
      "message": "Slack API can have rate limits",
      "suggestion": "Add onError: 'continueRegularOutput'"
    }
  ],
  "suggestions": [
    {
      "type": "optimization",
      "message": "Consider using batch operations for multiple messages"
    }
  ],
  "summary": {
    "hasErrors": true,
    "errorCount": 1,
    "warningCount": 1,
    "suggestionCount": 1
  }
}
```

### How to Read It

#### 1. Check `valid` field
```javascript
if (result.valid) {
  // ✅ Configuration is valid
} else {
  // ❌ Has errors - must fix before deployment
}
```

#### 2. Fix errors first
```javascript
result.errors.forEach(error => {
  console.log(`Error in ${error.property}: ${error.message}`);
  console.log(`Fix: ${error.fix}`);
});
```

#### 3. Review warnings
```javascript
result.warnings.forEach(warning => {
  console.log(`Warning: ${warning.message}`);
  console.log(`Suggestion: ${warning.suggestion}`);
  // Decide if you need to address this
});
```

#### 4. Consider suggestions
```javascript
// Optional improvements
// Not required but may enhance workflow
```

---

## Workflow Validation

### validate_workflow (Structure)
**Validates entire workflow**, not just individual nodes

**Checks**:
1. **Node configurations** - Each node valid
2. **Connections** - No broken references
3. **Expressions** - Syntax and references valid
4. **Flow** - Logical workflow structure

**Example**:
```javascript
validate_workflow({
  workflow: {
    nodes: [...],
    connections: {...}
  },
  options: {
    validateNodes: true,
    validateConnections: true,
    validateExpressions: true,
    profile: "runtime"
  }
})
```

### Common Workflow Errors

#### 1. Broken Connections
```json
{
  "error": "Connection from 'Transform' to 'NonExistent' - target node not found"
}
```

**Fix**: Remove stale connection or create missing node

#### 2. Circular Dependencies
```json
{
  "error": "Circular dependency detected: Node A → Node B → Node A"
}
```

**Fix**: Restructure workflow to remove loop

#### 3. Multiple Start Nodes
```json
{
  "warning": "Multiple trigger nodes found - only one will execute"
}
```

**Fix**: Remove extra triggers or split into separate workflows

#### 4. Disconnected Nodes
```json
{
  "warning": "Node 'Transform' is not connected to workflow flow"
}
```

**Fix**: Connect node or remove if unused

---

## Recovery Strategies

### Strategy 1: Start Fresh
**When**: Configuration is severely broken

**Steps**:
1. Note required fields from `get_node`
2. Create minimal valid configuration
3. Add features incrementally
4. Validate after each addition

### Strategy 2: Binary Search
**When**: Workflow validates but executes incorrectly

**Steps**:
1. Remove half the nodes
2. Validate and test
3. If works: problem is in removed nodes
4. If fails: problem is in remaining nodes
5. Repeat until problem isolated

### Strategy 3: Clean Stale Connections
**When**: "Node not found" errors

**Steps**:
```javascript
n8n_update_partial_workflow({
  id: "workflow-id",
  operations: [{
    type: "cleanStaleConnections"
  }]
})
```

### Strategy 4: Use Auto-fix
**When**: Operator structure errors

**Steps**:
```javascript
n8n_autofix_workflow({
  id: "workflow-id",
  applyFixes: false  // Preview first
})

// Review fixes, then apply
n8n_autofix_workflow({
  id: "workflow-id",
  applyFixes: true
})
```

---

## Best Practices

### ✅ Do

- Validate after every significant change
- Read error messages completely
- Fix errors iteratively (one at a time)
- Use `runtime` profile for pre-deployment
- Check `valid` field before assuming success
- Trust auto-sanitization for operator issues
- Use `get_node` when unclear about requirements
- Document false positives you accept

### ❌ Don't

- Skip validation before activation
- Try to fix all errors at once
- Ignore error messages
- Use `strict` profile during development (too noisy)
- Assume validation passed (always check result)
- Manually fix auto-sanitization issues
- Deploy with unresolved errors
- Ignore all warnings (some are important!)

---

## Detailed Guides

For comprehensive error catalogs and false positive examples:

- **[ERROR_CATALOG.md](ERROR_CATALOG.md)** - Complete list of error types with examples
- **[FALSE_POSITIVES.md](FALSE_POSITIVES.md)** - When warnings are acceptable

---

## Summary

**Key Points**:
1. **Validation is iterative** (avg 2-3 cycles, 23s + 58s)
2. **Errors must be fixed**, warnings are optional
3. **Auto-sanitization** fixes operator structures automatically
4. **Use runtime profile** for balanced validation
5. **False positives exist** - learn to recognize them
6. **Read error messages** - they contain fix guidance

**Validation Process**:
1. Validate → Read errors → Fix → Validate again
2. Repeat until valid (usually 2-3 iterations)
3. Review warnings and decide if acceptable
4. Deploy with confidence

**Related Skills**:
- n8n MCP Tools Expert - Use validation tools correctly
- n8n Expression Syntax - Fix expression errors
- n8n Node Configuration - Understand required fields
