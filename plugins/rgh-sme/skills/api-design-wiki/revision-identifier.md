---
type: concept
title: Revision Identifier
description: >
  An opaque identifier that uniquely labels one revision of a resource,
  sized smaller than primary resource ids because far fewer revisions exist
  per resource.
sources:
  - title: API Design Patterns
    resource: "API Design Patterns (Geewax), ch. 28"
---

Revision identifiers label individual snapshots. Three schemes appear in
practice: incrementing counters, timestamps, and random opaque strings.

Incrementing numbers imply chronological order independent of
`revisionCreateTime` and leave visible gaps after a revision is
[deleted](delete-revision.md) (for example 1, 2, 4), defeating the goal of
erasing a mistaken snapshot without a trace. Timestamps tolerate gaps but risk
collisions under high concurrent writes.

**Recommendation:** random opaque identifiers — a purposeless byte string
that only guarantees uniqueness. Revisions are far fewer per resource than
resources in the system, so a shorter identifier suffices (for example
13 Crockford Base32 characters / ~60 bits) compared with primary
[resource identifiers](resource-identifier.md). Include a
[checksum character](identifier-checksum.md) for the same reason as primary
ids: distinguish "not present" from "could never have been present."
