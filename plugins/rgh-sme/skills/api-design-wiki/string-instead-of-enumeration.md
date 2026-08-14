---
type: concept
title: String Instead of Enumeration
description: >
  Prefer string-typed value fields over numeric enums on the wire so new values
  stay self-describing and clients tolerate unknown values gracefully.
sources:
  - title: API Design Patterns
    resource: "API Design Patterns (Geewax), ch. 5"
---

Numeric **enumerations** compress values and aid compile-time validation in
strongly typed languages, but they are a poor default for web API contracts.

Problems:

- Opaque on the wire — `eyeColor == 2` needs a lookup table in logs and
  debug traces; `"blue"` is self-describing.
- Evolution pain — server adds `Hazel = 4`; old clients see an unknown integer
  with no semantic hint. A new string `"hazel"` is still readable even if
  unhandled.
- Client library churn — integer enums often force regenerated stubs; strings
  can be forwarded as-is.

**Recommendation:** use string fields validated server-side. Especially when
values will grow over time or an external standard exists (MIME types like
`application/pdf` instead of a hand-rolled file-type enum).

Enforce allowed values in implementation and documentation, not by exposing
a closed numeric enum on the wire.
