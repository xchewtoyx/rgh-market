---
type: concept
title: Precision-Sensitive Number as String
description: >
  Serialize large integers and exact decimals as strings so clients parse with
  arbitrary-precision libraries instead of lossy native JSON numbers.
sources:
  - title: API Design Patterns
    resource: "API Design Patterns (Geewax), ch. 5"
---

Native JSON number parsing is unsafe for precision-sensitive values: integers
beyond `Number.MAX_SAFE_INTEGER` can compare equal after `JSON.parse`, and
floating-point arithmetic yields surprises (`0.1 + 0.2 ≠ 0.3` in IEEE-754
environments).

**Recommendation:** serialize such values as **strings** on the wire. Clients
must explicitly parse with an arbitrary-precision library (for example
Decimal.js) rather than relying on native numeric types. Apply the same rule
inside [atomic list fields](atomic-list-field.md) when list elements are
numeric but precision matters.

This pattern bridges numeric semantics with [string field bounds and
encoding](string-field-bounds-and-encoding.md) constraints on the serialized
form.
