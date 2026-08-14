---
type: concept
title: Identifier Checksum
description: >
  A trailing check character that distinguishes typos and invalid ids from ids
  that simply do not exist in the system.
sources:
  - title: API Design Patterns
    resource: "API Design Patterns (Geewax), ch. 6"
---

A [resource identifier](resource-identifier.md) should let callers separate:

- **Missing** — well-formed id that was deleted or never created.
- **Invalid** — could never have been valid (typo, corruption).

Append a **checksum character** derived from the rest of the id; recompute on
parse and reject mismatches before hitting storage.

With [Crockford Base32](crockford-base32-identifier.md): treat the payload as
an integer, divide by 37 (smallest prime above 32), map the remainder to a
Base37 digit using the spec's reserved checksum alphabet. The same approach
applies to shorter [revision identifiers](revision-identifier.md).

ISBN's final check digit is the real-world analogue.
