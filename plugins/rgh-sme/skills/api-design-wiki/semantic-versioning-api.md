---
type: concept
title: Semantic Versioning for APIs
description: >
  A three-part major.minor.patch scheme that encodes whether a release is
  backward compatible, additive, or breaking.
sources:
  - title: Patterns for API Design
    resource: "Patterns for API Design (Zimmermann et al.), ch. 8"
---

**Semantic versioning** formats a [version identifier](version-identifier.md)
as `x.y.z`:

| Segment | Meaning | Example |
| --- | --- | --- |
| Major (`x`) | Incompatible breaking change | `1.3.1` → `2.0.0` |
| Minor (`y`) | Compatible new functionality | `1.2.5` → `1.3.0` |
| Patch (`z`) | Compatible bug fix or doc fix | `1.2.4` → `1.2.5` |

Example arc: ship search `1.0.0` → optional historic search `1.1.0` → bugfix
`1.1.1` → mandatory currency field (breaking) `2.0.0`.

The scheme defines **how numbers are assigned**, not where they appear on the
wire. It applies to client-visible API versions and to internal API revisions
(Higginbotham's version/revision distinction).

Plain sequential numbers hide compatibility branches (v1 compatible with v3
while v2 continues as v4). Commit ids avoid manual assignment but do not
express compatibility or deployment cadence.

Trade-offs: high clarity on impact, but every change must be classified —
sometimes genuinely hard, and mislabeled minor releases can smuggle breaking
changes. Variants: two-number `n.m`, or three numbers with patch hidden from
clients internally.

Replay and archive scenarios (Kafka logs, restored backups) may require strict
backward compatibility across all stored message versions.

Related schemes: Avro writer/reader schema pairing; SchemaVer (model/revision/
addition); vendor breaking-change policies.

Pairs with tolerant-reader client behavior for minor-version resilience and with
[lifecycle guarantee patterns](limited-lifetime-guarantee.md). Strategy context:
[perpetual stability versioning](perpetual-stability-versioning.md),
[agile instability versioning](agile-instability-versioning.md),
[versioning strategy tradeoffs](versioning-strategy-tradeoffs.md).
