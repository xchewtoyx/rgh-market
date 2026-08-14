---
type: concept
title: Kimball Bus vs. Inmon CIF — Two Ways to Build a Multi-Mart Warehouse
description: >
  The two classic disciplined answers to data marts multiplying without
  coordination — a centralized normalized warehouse marts are dependently
  derived from, versus independent marts held consistent by a conformed
  dimension bus — and why they've converged in practice.
sources:
  - title: Deciphering Data Architectures
    resource: "Deciphering Data Architectures (Serra), ch. 8"
---

[Stand-alone data marts that accumulate without coordination](stovepipe-mart-etl-redundancy.md)
are a known failure mode: redundant extraction against the same sources, and
contradictory numbers when each mart's ETL applies slightly different
business rules to the same underlying facts. Two named architectures are the
classic disciplined answers to that failure mode, and they solve it in
opposite directions:

**Inmon's top-down approach** loads raw source data into staging, then into
a centralized, normalized (typically 3NF), atomic-grain **enterprise data
warehouse (EDW)** — sometimes called a corporate information factory (CIF)
— that end users never query directly. Department-specific **dependent data
marts** are then built *only* from the EDW, never from source systems
directly (a hub-and-spoke shape). Consistency comes structurally: because
every mart is derived from the same single physical repository, marts can't
diverge in the way stand-alone marts do — there's exactly one shared
extraction and one shared set of transformation rules upstream of every
mart. The cost is real: data typically exists in three physical copies
(EDW, mart, and any downstream cube), each needing storage and its own
refresh cycle, and nothing is queryable by end users until the EDW modeling
work is substantially done.

**Kimball's bottom-up approach** skips the centralized physical EDW
entirely. Raw source data still lands in staging, but from there it loads
directly into **independent data marts** — each built around one business
process, dimensionally modeled, sourced and owned separately. Consistency
across marts comes not from physical centralization but from
[conformed dimensions](conformed-dimension-publish-subscribe.md): the same
dimension (customer, product, date) is deliberately built to identical
structure and content everywhere it appears, governed by a shared
**EDW bus matrix** — an up-front architectural plan mapping every business
process against the conformed dimensions it uses — even though each mart's
data still physically lives and loads separately. Data is copied only
twice (staging → mart, or once if a mart is exposed via a database view
rather than materialized), and marts become queryable as soon as each is individually built rather than
waiting for one central model to be complete.

**The trade-off isn't "structured vs. unstructured" — both require real
up-front design.** The EDW bus matrix is exactly as much deliberate
enterprise-wide planning as an Inmon-style normalized model; Kimball's
method is "bottom-up" only in build *order* (one business process, then
the next), not in skipping design. The genuine difference is where
consistency gets enforced: Inmon enforces it once, physically, at the
center; Kimball enforces it by discipline, repeatedly, at every mart that
touches a shared dimension — which is more scalable across many marts but
depends on that discipline actually holding, whereas Inmon's physical
centralization makes divergence structurally harder regardless of
discipline.

**Choosing between them** comes down to how many sources feed the warehouse
and how urgently marts need to ship: a small number of sources with a need
for fast initial reporting favors skipping the physical EDW; many sources
feeding many marts, where per-mart ETL refresh and reconciliation overhead
would otherwise multiply, favors paying the physical-EDW cost once to
avoid repeatedly paying a smaller version of it in every mart's own
pipeline. In practice the two have converged: a Kimball-style bus can add a
physical normalized layer for the same consistency benefits an EDW buys,
and an Inmon-style CIF can expose dimensionally-modeled marts directly
instead of purely normalized ones — the pattern worth borrowing from
either is whichever piece addresses the specific reconciliation or
speed-to-market pressure a given platform is actually under, not a
strict, exclusive choice of one named methodology.
