---
type: concept
title: Numeric Field Bounds
description: >
  Explicit min, max, and bit-width expectations for wire numbers so clients
  know allocation limits and arithmetic is meaningful.
sources:
  - title: API Design Patterns
    resource: "API Design Patterns (Geewax), ch. 5"
---

Numeric fields belong on the wire when values have genuine arithmetic meaning
(counts, weights, currency) — not when digits function as opaque tokens; those
belong in [string identifiers](resource-identifier.md).

Every numeric field needs explicit **upper and lower bounds** because storage
fixes bit width in advance (8-bit ≈ ±127, 32-bit ≈ ±2 billion, 64-bit ≈ ±9
quintillion; floats can reach 256-bit representations). Language runtimes
handle numbers unevenly — JavaScript has no true integer type; historical Python
split `int` and `long`. Receivers must know whether a magnitude is parseable
and how much space to allocate. Default internally to **64-bit integers** unless
a strong reason exists; err toward headroom.

**Default-value trap:** when primitives lack null, `0`/`0.0` cannot mean "pick
a default" without blocking intentional zero — surprising when zero is a
legitimate value. Document defaults explicitly instead of overloading zero.

When values exceed safe native parsing or need exact decimals, use
[precision-sensitive numbers as strings](precision-sensitive-number-as-string.md).
