---
type: concept
title: Semantic Versioning
description: >
  The MAJOR.MINOR.PATCH versioning contract signals to consumers whether a
  release is safe to adopt automatically or requires a compatibility
  review.
sources:
  - title: "Release It!"
    resource: "Release It!: Design and Deploy Production-Ready Software, 2nd Edition (Nygard), ch. 14"
---

# Semantic Versioning

Semantic versioning (SemVer) is a `MAJOR.MINOR.PATCH` contract for
communicating the compatibility impact of a release to its consumers:

- `MAJOR`: breaking, incompatible API changes.
- `MINOR`: backward-compatible feature additions.
- `PATCH`: backward-compatible bug fixes.

It only functions as a safety signal if the API owner is disciplined about
what counts as non-breaking — adding optional parameters, adding new
response fields, or adding new endpoints are safe MINOR changes; anything a
consumer could break on (removing/renaming a field, tightening validation,
changing a field's type or meaning) is a MAJOR change requiring
[parallel API version coexistence](parallel-api-version-coexistence.md)
rather than an in-place cut.

Consumers reduce their own exposure to accidental breakage by implementing
the [tolerant reader pattern](tolerant-reader-pattern.md), which absorbs
some classes of "should have been non-breaking" change even when the
producer's versioning discipline slips.
