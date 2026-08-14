---
type: concept
title: Accessor Methods Should Hide Representation, Not Expose It
description: >
  A shallow accessor that returns an internal data structure leaks its
  representation to every caller; a deeper, type-specific accessor hides the
  representation and folds conversion logic into the interface instead.
sources:
  - title: A Philosophy of Software Design
    resource: "A Philosophy of Software Design (Ousterhout), ch. 5"
---

A common bad instinct, illustrated with HTTP request parameters:

```java
public Map<String, String> getParams() { return this.params; }
```

This leaks the internal representation (a `Map`), forces every caller into a
two-step retrieval (get the map, then look up the key), and creates an
implicit "don't mutate this" contract on the returned reference that nothing
enforces.

The deeper fix is a type-safe accessor pair (or family) instead:

```java
public String getParameter(String name) { ... }
public int getIntParameter(String name) { ... }
```

with further typed variants (`getDoubleParameter`, etc.) added as needed, each
throwing on a missing or unconvertible value. This hides the internal
representation entirely and folds string-to-type conversion into the
interface itself, so callers never see or depend on how parameters are
actually stored. This is [information hiding](information-hiding.md) applied
specifically to the shape of returned data, and it's the concrete pattern
behind avoiding the shallow-getter trap that ordinary encapsulation (marking a
field `private`) does not prevent.
