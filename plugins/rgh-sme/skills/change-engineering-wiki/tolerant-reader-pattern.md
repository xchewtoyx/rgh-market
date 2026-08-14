---
type: concept
title: Tolerant Reader Pattern
description: >
  Consumers of an API or data format should ignore unexpected or unknown
  fields rather than failing on them, so producers can add fields without
  breaking existing clients.
sources:
  - title: "Release It!"
    resource: "Release It!: Design and Deploy Production-Ready Software, 2nd Edition (Nygard), ch. 14"
---

# Tolerant Reader Pattern

The tolerant reader pattern (an application of Postel's law — "be
conservative in what you send, liberal in what you accept") requires
consumers to ignore fields they don't recognize in an API response or
message payload, instead of failing when the shape of the payload doesn't
exactly match what they expect.

This is what makes additive changes — new optional fields, new response
attributes — actually safe in practice under [semantic versioning](semantic-versioning.md):
the versioning scheme only classifies a change as non-breaking; the
tolerant reader is what makes that classification true for the actual
deployed consumers. A strict/eager reader (one that fails on unknown
fields) turns every additive change into a de facto breaking one for that
consumer, regardless of what the producer's version number claims.

Schemaless data stores rely on the same idea at the persistence layer: code
must tolerate reading records written under multiple prior schema versions
concurrently, which is the data-layer analogue described in
[expand-and-contract schema migration](expand-and-contract-schema-migration.md).
