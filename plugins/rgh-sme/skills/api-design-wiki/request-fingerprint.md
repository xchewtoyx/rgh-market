---
type: concept
title: Request Fingerprint
description: >
  A canonical string built from selected request parts that becomes the payload
  signed for request authentication, avoiding fragile raw-body signing.
sources:
  - title: API Design Patterns
    resource: "API Design Patterns (Geewax), ch. 30"
---

Signing only the request body is fragile. Serialization is not canonical —
JSON property order, encoding, and normalization can change bytes without
changing meaning, so signer and verifier disagree and signatures fail spuriously.
Many operations have no body (HTTP DELETE): the action lives in the method and
URL; other context lives in headers such as `Date`.

A **request fingerprint** is a deterministic string assembled from agreed
components, then signed. Typical components (table 30.1):

| Component | Source |
| --- | --- |
| HTTP method | First line |
| Path | First line |
| Host | Header |
| Request body | Body content (often hashed) |
| Date | Header (supports rejecting stale requests) |

Simplifications:

1. **Request target** — one field `(request-target)` = lowercase method +
   space + path, for example `patch /chatrooms/1`.
2. **Digest header** — hash the body (for example SHA-256, Base64, prefixed
   `SHA-256=...`) instead of signing a large payload inline.

Default header list: `(request-target)`, `host`, `date`, `digest`. Lowercase
each header name and join lines as `header: value` separated by `\n`. That
string is what gets signed.

The wire request must carry metadata so the server rebuilds the same
fingerprint — see [signature header](signature-header.md).
