---
type: concept
title: String Field Bounds and Encoding
description: >
  Max-length limits, UTF-8 encoding, and Unicode normalization rules for wire
  strings, with stricter requirements for identifier-bearing values.
sources:
  - title: API Design Patterns
    resource: "API Design Patterns (Geewax), ch. 5"
---

Strings are the most versatile wire type: names, addresses, long text, Base64
binary payloads, [precision-sensitive numbers](precision-sensitive-number-as-string.md),
and [resource identifiers](resource-identifier.md).

**Bounds:** declare explicit max length so receivers allocate storage. Err
generous — raising limits later is uncomfortable. Length is measured in
characters/code points, but budget storage as **UTF-32** (4 bytes per
character) for capacity planning because bytes-on-disk do not map 1:1 to
visible characters. On overflow: **reject** input; do not truncate — truncation
is surprising and forces per-field inconsistency about truncate-vs-reject.

**Defaults:** empty string vs missing vs null follows
[missing versus null policy](missing-versus-null-policy.md). If `""` is never
semantically valid, it can signal "use default"; for enumerated string fields,
an explicit `"default"` sentinel is clearer.

**Encoding:** standardize on **UTF-8** for all string content. Unicode
**normalization** matters: the same visible character (for example "è") can have
multiple byte representations (precomposed vs base+combining accent). Low
stakes for free text; critical for identifiers where byte-different forms could
resolve to different resources. Reject strings not in UTF-8 **Normalization
Form C** for identifier-bearing fields — a hard requirement, not a guideline.
[Map field keys](map-field-bounds-and-defaults.md) follow the same rule.
