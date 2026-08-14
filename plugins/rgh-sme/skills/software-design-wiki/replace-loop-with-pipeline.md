---
type: concept
title: "Refactoring: Replace Loop with Pipeline"
description: >
  Peel each piece of an imperative loop's behavior off into a chained
  collection-pipeline stage one at a time, so the final code reads
  top-to-bottom as data flowing through named transformations instead of
  several concerns interleaved procedurally in one loop body.
sources:
  - title: "Refactoring: Improving the Design of Existing Code (2nd ed.)"
    resource: "Refactoring (Fowler, with Kent Beck), ch. 8"
---

Collection pipelines — chained `map`/`filter`/`reduce`-style operations,
each consuming and emitting a collection — are a clearer alternative to
imperative loops for describing processing over a collection: reading a
pipeline top-to-bottom shows how data flows through each transformation
stage, versus a loop body where multiple concerns are interleaved
procedurally. See [imperative loops as a code smell](loops-vs-pipelines.md)
for when this substitution is worth making.

**Mechanics**: introduce a new variable to hold the loop's source
collection (may start as a plain copy of an existing variable). Starting
from the top of the loop body, replace each piece of behavior with a
corresponding pipeline operation chained onto the derivation of that
collection variable, testing after each individual change — a header-skip
becomes a `slice`, a blank-line filter becomes a `filter`, a per-line
transform becomes a `map`, and so on, each peeled out one at a time. Once
every behavior has been peeled out of the loop body this way, delete the
now-empty loop; if it was populating an accumulator, assign the pipeline's
final result directly to that accumulator instead.

Renaming intermediate pipeline variables to fit their new meaning, and
tidying the pipeline's visual layout, are best deferred until after the
mechanical transformation is safely complete and tested — don't try to
combine the structural change with a naming cleanup in the same step. An
intermediate variable that's technically redundant can still be worth
keeping if its name usefully documents what the value represents at that
stage of the pipeline. This refactoring frequently follows
[Split Loop](split-loop.md), once a loop has been reduced to doing exactly
one thing.
