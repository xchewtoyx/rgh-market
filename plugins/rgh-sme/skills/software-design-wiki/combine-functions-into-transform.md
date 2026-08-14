---
type: concept
title: Combine Functions into Transform
description: >
  A single function that takes source data and returns an enriched copy
  with every derived value pre-computed gives derivations one obvious,
  discoverable home — at the cost of silently going stale if the source
  mutates afterward.
sources:
  - title: "Refactoring: Improving the Design of Existing Code (2nd ed.)"
    resource: "Refactoring (Fowler, with Kent Beck), ch. 6"
---

An alternative to [Combine Functions into
Class](combine-functions-into-class.md) for the same underlying problem —
derived values computed redundantly in multiple places. Instead of a class,
use a single transformation function that takes the source data and returns
an enriched copy with every derived value pre-computed as a field. The
advantage over ad hoc extraction is discoverability: functions extracted
individually tend to scatter around a codebase where future readers won't
find them, whereas a transform function is one obvious, consistently
located place to look for — and add — derivations.

**The explicit tradeoff**: a transform bakes derived values in at transform
time, so if the source data is subsequently mutated, the derived fields
silently go stale. This makes a transform a poor fit whenever the source can
change after enrichment, and a much more natural fit with immutable data, or
in a read-only-consumption context such as preparing data to render on a
page. When that mutation risk is real, [Combine Functions into
Class](combine-functions-into-class.md) is the correct escape hatch instead,
since its methods recompute from live state rather than caching a snapshot.

**Mechanics**: create a transformation function that takes the record and
returns an equivalent (typically deep) copy — worth a test up front
confirming the original record is left unmodified. Then, function by
function: move a derivation's logic into the transform as a new field on
the result, updating client code to read that field instead ([Extract
Function](extract-function.md) first if the logic is non-trivial); test;
repeat.

Mutating the local accumulating result object directly *inside* the
transform function is a deliberate, scoped exception to a general preference
for immutability: "I'm prepared to go through the extra effort to support
[immutability] at boundaries, but will mutate within smaller scopes" — the
function's external contract (input untouched, a fresh object returned) is
what's protected, not every line inside it.
