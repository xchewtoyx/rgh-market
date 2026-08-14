---
type: concept
title: Resource Identifier
description: >
  A permanent, unique, unpredictable string that addresses exactly one resource
  in an API collection and supports reliable lookup.
sources:
  - title: API Design Patterns
    resource: "API Design Patterns (Geewax), ch. 6"
---

An **identifier** is the bytes clients use to point to exactly one resource,
almost always for lookup (GET). Good identifiers share several properties:

- **Easy to use** — common case is single-resource fetch; avoid URI-special
  characters such as `/` inside the opaque segment when possible (collection
  prefix handles path structure).
- **Unique** — scoped deliberately: per resource type, per API, or globally.
  True global uniqueness is impractical in theory but achievable in practice
  with a large key space and honest clients.
- **Permanent** — never change once assigned; never reuse after delete
  (single-use forever). Reassigning `Book(id=1234)` after deletion makes stale
  references ambiguous depending on when they were recorded.
- **Fast to generate** — random ids must not require scanning all prior ids;
  collision probability must stay negligible via key-space size.
- **Unpredictable** — sequential ids enable enumeration attacks against weak
  access control; large random spaces make guessing infeasible.
- **Readable and verifiable** — avoid visually confusable glyphs; support
  [checksum validation](identifier-checksum.md) so "missing" differs from
  "never valid."

**Strings** beat integers and raw bytes for wire identifiers: more entropy per
HTTP character, familiar tooling, tunable readability. Use **ASCII**, not
Unicode, to avoid normalization ambiguities (combining characters vs
precomposed forms).

Recommended encoding: [Crockford Base32](crockford-base32-identifier.md).
Optional collection prefix (`books/abcde-...`) lets consumers infer type and
maps cleanly to URLs.

## Fixed size and scope

Prefer **fixed-length** ids for schema predictability. Type-scoped uniqueness
(~64 bits payload plus checksum, ~13 characters with Base32) suffices when ids
need only differ within one resource type. Globally unique everywhere targets
~120 bits (~25 characters with checksum) — parity with UUID payload size.

## Client-chosen ids

Avoid letting clients pick ids except deliberate sync scenarios ([standard method
contract](standard-method-contract.md) create). Risks: collision after delete
confuses users who expect reuse; PII embedded in "opaque" ids leaks via logs
and dashboards; non-cryptographic choices create predictable enumeration
surfaces.

## Generation and tomb-stoning

Generate with cryptographically secure random **bytes** then encode, or random
characters from the Base32 alphabet — `base32Length = ceil(bytes × 8 / 5)`.
[Permanent](resource-identifier.md) ids imply [soft deletion](soft-deletion.md)
or a taken-id registry so deleted values are never reassigned; a generate-and-check
loop against storage is acceptable when the key space is large enough. Hard-delete
mandates may require a Bloom filter or hash set of retired ids.

Do **not** persist the [checksum character](identifier-checksum.md) — recompute
on egress and verify on ingress so checksum algorithms can change without
migrations. Store as string (minus checksum), raw bytes, or integer primary key
depending on database strengths; Crockford Base32 preserves sort order for
string keys.

See [hierarchical resource identifier](hierarchical-resource-identifier.md)
for when parent segments belong in the id. For UUID trade-offs and hybrid
wire encoding, see [UUID identifier encoding](uuid-identifier-encoding.md).
