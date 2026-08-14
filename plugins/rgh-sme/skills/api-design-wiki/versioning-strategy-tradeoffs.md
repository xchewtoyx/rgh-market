---
type: concept
title: Versioning Strategy Tradeoffs
description: >
  Design axes — granularity, stability, and user satisfaction — that every API
  versioning and compatibility policy must balance consciously.
sources:
  - title: API Design Patterns
    resource: "API Design Patterns (Geewax), ch. 24.4"
---

No versioning scheme satisfies every client. Choose deliberately along these axes:

## Granularity vs simplicity

Too many incompatible versions → precise pinning but chronological baggage — pinning
v47 to avoid v46 also accepts everything before v47. Too few versions (everything
compatible forever) → simple but may smuggle breaking drift. Target a **reasonable**
version count plus [deprecation patterns](aggressive-obsolescence.md) or
[lifecycle guarantees](limited-lifetime-guarantee.md).

## Stability vs new functionality

Perfect stability forbids even dependency security patches that might change behavior.
Maximum velocity pushes every fix and feature immediately — [backward compatibility
policy](backward-compatibility-policy.md) becomes critical. Enterprise users skew
stable; startups skew fresh features. Document where the API sits.

## Happiness vs ubiquity

Model users in four buckets: **cannot use**, **mad**, **okay**, **happy**. Maximizing
happy alone can expand cannot use; maximizing ubiquity can swell mad (works but
resented). Aim for low cannot use with a respectable happy share — no policy makes
everyone delighted.

These spectrums inform choice among [perpetual stability versioning](perpetual-stability-versioning.md),
[agile instability versioning](agile-instability-versioning.md), and
[semantic versioning for APIs](semantic-versioning-api.md) — the strategy labels
changes; the compatibility policy classifies them.
