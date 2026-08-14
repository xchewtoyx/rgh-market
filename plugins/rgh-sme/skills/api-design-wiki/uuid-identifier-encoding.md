---
type: concept
title: UUID Identifier Encoding
description: >
  When RFC 4122 UUIDs fit internal storage but Base32-plus-checksum strings
  better serve the public wire format for density and typo detection.
sources:
  - title: API Design Patterns
    resource: "API Design Patterns (Geewax), ch. 6"
---

**UUIDs** (RFC 4122) offer 128-bit space, namespacing (v3/v5), and time ordering
(v1/v2) with negligible collision risk — familiar hyphenated hex on the wire.

Reasons not to expose raw UUID strings as the only customer-facing id:

- **Oversized** — 122 usable bits exceeds many APIs' lifetime volume; shorter
  [Crockford Base32](crockford-base32-identifier.md) strings improve usability.
- **Low density** — hex is 4 bits per character versus 5 for Base32 — painful
  when ids are read aloud or typed manually.
- **No checksum** — typos look like missing resources, not invalid ids; pair
  wire ids with [identifier checksum](identifier-checksum.md) instead.

**Hybrid:** generate UUIDs internally (random v4, or v3/v5/v1 when namespacing
or ordering helps), store in native UUID/binary columns when the database excels
at that, and **encode to Base32 plus checksum** for API responses and paths.
Recompute checksum on output; verify before lookup — same discipline as non-UUID
[resource identifiers](resource-identifier.md).
