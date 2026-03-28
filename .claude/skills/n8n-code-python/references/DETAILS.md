# Python Code Node — Detailed Reference

## Error Prevention - Top 5 Mistakes

### #1: Importing External Libraries (Python-Specific!)

```python
# ❌ WRONG: Trying to import external library
import requests  # ModuleNotFoundError!

# ✅ CORRECT: Use HTTP Request node or JavaScript
# Add HTTP Request node before Code node
# OR switch to JavaScript and use $helpers.httpRequest()
```

### #2: Empty Code or Missing Return

```python
# ❌ WRONG: No return statement
items = _input.all()
# Processing...
# Forgot to return!

# ✅ CORRECT: Always return data
items = _input.all()
# Processing...
return [{"json": item["json"]} for item in items]
```

### #3: Incorrect Return Format

```python
# ❌ WRONG: Returning dict instead of list
return {"json": {"result": "success"}}

# ✅ CORRECT: List wrapper required
return [{"json": {"result": "success"}}]
```

### #4: KeyError on Dictionary Access

```python
# ❌ WRONG: Direct access crashes if missing
name = _json["user"]["name"]  # KeyError!

# ✅ CORRECT: Use .get() for safe access
name = _json.get("user", {}).get("name", "Unknown")
```

### #5: Webhook Body Nesting

```python
# ❌ WRONG: Direct access to webhook data
email = _json["email"]  # KeyError!

# ✅ CORRECT: Webhook data under ["body"]
email = _json["body"]["email"]

# ✅ BETTER: Safe access with .get()
email = _json.get("body", {}).get("email", "no-email")
```

**See**: [ERROR_PATTERNS.md](ERROR_PATTERNS.md) for comprehensive error guide

---

## Standard Library Reference

### Most Useful Modules

```python
# JSON operations
import json
data = json.loads(json_string)
json_output = json.dumps({"key": "value"})

# Date/time
from datetime import datetime, timedelta
now = datetime.now()
tomorrow = now + timedelta(days=1)
formatted = now.strftime("%Y-%m-%d")

# Regular expressions
import re
matches = re.findall(r'\d+', text)
cleaned = re.sub(r'[^\w\s]', '', text)

# Base64 encoding
import base64
encoded = base64.b64encode(data).decode()
decoded = base64.b64decode(encoded)

# Hashing
import hashlib
hash_value = hashlib.sha256(text.encode()).hexdigest()

# URL parsing
import urllib.parse
params = urllib.parse.urlencode({"key": "value"})
parsed = urllib.parse.urlparse(url)

# Statistics
from statistics import mean, median, stdev
average = mean([1, 2, 3, 4, 5])
```

**See**: [STANDARD_LIBRARY.md](STANDARD_LIBRARY.md) for complete reference

---

## Best Practices

### 1. Always Use .get() for Dictionary Access

```python
# ✅ SAFE: Won't crash if field missing
value = item["json"].get("field", "default")

# ❌ RISKY: Crashes if field doesn't exist
value = item["json"]["field"]
```

### 2. Handle None/Null Values Explicitly

```python
# ✅ GOOD: Default to 0 if None
amount = item["json"].get("amount") or 0

# ✅ GOOD: Check for None explicitly
text = item["json"].get("text")
if text is None:
    text = ""
```

### 3. Use List Comprehensions for Filtering

```python
# ✅ PYTHONIC: List comprehension
valid = [item for item in items if item["json"].get("active")]

# ❌ VERBOSE: Manual loop
valid = []
for item in items:
    if item["json"].get("active"):
        valid.append(item)
```

### 4. Return Consistent Structure

```python
# ✅ CONSISTENT: Always list with "json" key
return [{"json": result}]  # Single result
return results  # Multiple results (already formatted)
return []  # No results
```

### 5. Debug with print() Statements

```python
# Debug statements appear in browser console (F12)
items = _input.all()
print(f"Processing {len(items)} items")
print(f"First item: {items[0] if items else 'None'}")
```

---

## When to Use Python vs JavaScript

### Use Python When:
- ✅ You need `statistics` module for statistical operations
- ✅ You're significantly more comfortable with Python syntax
- ✅ Your logic maps well to list comprehensions
- ✅ You need specific standard library functions

### Use JavaScript When:
- ✅ You need HTTP requests ($helpers.httpRequest())
- ✅ You need advanced date/time (DateTime/Luxon)
- ✅ You want better n8n integration
- ✅ **For 95% of use cases** (recommended)

### Consider Other Nodes When:
- ❌ Simple field mapping → Use **Set** node
- ❌ Basic filtering → Use **Filter** node
- ❌ Simple conditionals → Use **IF** or **Switch** node
- ❌ HTTP requests only → Use **HTTP Request** node

---

## Integration with Other Skills

### Works With:

**n8n Expression Syntax**:
- Expressions use `{{ }}` syntax in other nodes
- Code nodes use Python directly (no `{{ }}`)
- When to use expressions vs code

**n8n MCP Tools Expert**:
- How to find Code node: `search_nodes({query: "code"})`
- Get configuration help: `get_node_essentials("nodes-base.code")`
- Validate code: `validate_node_operation()`

**n8n Node Configuration**:
- Mode selection (All Items vs Each Item)
- Language selection (Python vs JavaScript)
- Understanding property dependencies

**n8n Workflow Patterns**:
- Code nodes in transformation step
- When to use Python vs JavaScript in patterns

**n8n Validation Expert**:
- Validate Code node configuration
- Handle validation errors
- Auto-fix common issues

**n8n Code JavaScript**:
- When to use JavaScript instead
- Comparison of JavaScript vs Python features
- Migration from Python to JavaScript

---

## Quick Reference Checklist

Before deploying Python Code nodes, verify:

- [ ] **Considered JavaScript first** - Using Python only when necessary
- [ ] **Code is not empty** - Must have meaningful logic
- [ ] **Return statement exists** - Must return list of dictionaries
- [ ] **Proper return format** - Each item: `{"json": {...}}`
- [ ] **Data access correct** - Using `_input.all()`, `_input.first()`, or `_input.item`
- [ ] **No external imports** - Only standard library (json, datetime, re, etc.)
- [ ] **Safe dictionary access** - Using `.get()` to avoid KeyError
- [ ] **Webhook data** - Access via `["body"]` if from webhook
- [ ] **Mode selection** - "All Items" for most cases
- [ ] **Output consistent** - All code paths return same structure

---

## Additional Resources

### Related Files
- [DATA_ACCESS.md](DATA_ACCESS.md) - Comprehensive Python data access patterns
- [COMMON_PATTERNS.md](COMMON_PATTERNS.md) - 10 Python patterns for n8n
- [ERROR_PATTERNS.md](ERROR_PATTERNS.md) - Top 5 errors and solutions
- [STANDARD_LIBRARY.md](STANDARD_LIBRARY.md) - Complete standard library reference

### n8n Documentation
- Code Node Guide: https://docs.n8n.io/code/code-node/
- Python in n8n: https://docs.n8n.io/code/builtin/python-modules/

---

**Ready to write Python in n8n Code nodes - but consider JavaScript first!** Use Python for specific needs, reference the error patterns guide to avoid common mistakes, and leverage the standard library effectively.
