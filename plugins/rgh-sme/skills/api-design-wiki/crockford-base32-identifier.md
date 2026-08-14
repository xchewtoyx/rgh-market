---
type: concept
title: Crockford Base32 Identifier
description: >
  A recommended ASCII encoding for resource ids with high density, forgiving
  decoding, and excluded confusable characters.
sources:
  - title: API Design Patterns
    resource: "API Design Patterns (Geewax), ch. 6"
---

**Crockford Base32** serializes random identifier bytes into ASCII using 32
symbols: `A–Z` and `0–9`, excluding URI-special characters and excluding `I`,
`L`, `O`, `U` (confusable with `1`/`0`, and `U` reduces accidental profanity).
Five bits of entropy per character — denser than decimal, more readable than
Base64 (which adds confusable `i`/`I`/`1`).

Decoding is case-insensitive and forgiving: lowercase `l` → `1`, `o` → `0`, etc.
Hyphens are decorative only — `abcde-12345` canonicalizes like `ABCDE12345`.

Pair with an [identifier checksum](identifier-checksum.md) suffix. Size the
random payload for expected catalog scale (for example ~120 bits / 25 characters
for billions of resources).

Used when generating [resource identifiers](resource-identifier.md) and
[revision identifiers](revision-identifier.md).
