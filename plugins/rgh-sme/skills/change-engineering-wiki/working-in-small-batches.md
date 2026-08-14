---
type: concept
title: Working in Small Batches
description: >
  Reducing the size of each release lowers cycle time, shrinks blast
  radius, and shortens feedback loops, changing the economics of shipping
  changes.
sources:
  - title: Accelerate
    resource: "Accelerate: The Science of Lean Software and DevOps (Forsgren, Humble, Kim), ch. 4"
  - title: "Sources of Power: How People Make Decisions"
    resource: "Sources of Power: How People Make Decisions (Klein), ch. 16"
  - title: "Software Engineering at Google"
    resource: "Software Engineering at Google (Winters, Manshreck, Wright), ch. 26"
---

# Working in Small Batches

Reducing batch size — the amount of change bundled into a single release —
is a core Continuous Delivery principle borrowed from Lean manufacturing. It
lowers cycle time, accelerates feedback, minimizes rework, and changes the
economic cost curve of releasing changes: a smaller batch is cheaper to
verify, cheaper to reason about, and cheaper to
[roll back](rollback-vs-roll-forward.md) if it goes wrong, because there is
less surface area for the failure to hide in and less to lose by reverting
it.

[Deployment frequency](deployment-frequency.md) is the operational proxy for
batch size (deployment frequency ≈ 1 / batch size) — an organization cannot
increase deployment frequency without shrinking batch size, and shrinking
batch size is most of what makes higher deployment frequency safe rather
than merely fast.

Small batches also underlie [canary release](canary-release.md) practice:
a canary can only isolate one change's effect cleanly when that change is
small and self-contained, not an entangled bundle of unrelated work.

A large batch's risk also compounds multiplicatively, not additively, in
a way that's easy to underestimate from looking at each piece in
isolation: a release bundled from six independent changes, each
individually 90% likely to be safe, has only a 0.9⁶ ≈ 53% chance that the
whole bundle is safe — even though every individual piece "feels" low-risk.
Splitting the same six changes into six small releases doesn't change any
individual change's risk, but it stops that risk from compounding onto
everything shipped alongside it, and it isolates which one actually
caused a problem if something does go wrong.
