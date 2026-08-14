---
type: concept
title: Header-to-Line Fact Allocation
description: >
  Distributing a measurement recorded only at a coarser grain (a header-level
  freight charge, an overhead cost) down to the finer grain of the fact rows
  it needs to be sliced by, using business-supplied rules.
sources:
  - title: "The Data Warehouse Toolkit: The Definitive Guide to Dimensional Modeling, 3rd Edition"
    resource: "The Data Warehouse Toolkit (Kimball, Ross), ch. 2"
---

Operational transaction systems commonly separate a header (an order, an
invoice) from its line items, and some measurements are only ever recorded
at the header level — a single freight or handling charge for the whole
order, say — while the fact table's grain is the line item. Leaving that
measurement at header grain means it can't be sliced or rolled up by the
same dimensions (product, promotion) that every other fact on the line-level
table supports.

**Allocation** is the load-time transformation that fixes this: distribute
the header-level value down across its constituent line rows using a
business-approved rule — proportional to line amount, proportional to
quantity, or some other agreed basis — so every line row ends up with its
own share of the header measurement, additive and sliceable the same way as
every other fact in the table. This is often the single most
politically-charged transformation in a pipeline, precisely because the
allocation *rule itself* is a business decision with real financial
consequences (it determines which product or customer looks more or less
profitable), not a technical one — get explicit, documented business sign-off
on the allocation basis before implementing it, and expect it to need
executive-level backing rather than being something the pipeline team
decides unilaterally.

Three tempting shortcuts avoid explicit allocation and should all be
rejected: repeating the unallocated header value on every line row (double-
or triple-counts it the moment anyone sums the fact across lines); storing
it only on the first or last line of each group (avoids overcounting, but
the value silently disappears from any report that filters by a product or
other line-level attribute that excludes that particular line); and flagging
a synthetic row with a sentinel key to carry the header value (forces every
downstream query to know about and filter out the decoder-ring row, which is
exactly the kind of hidden special case a load should never impose on
consumers).

The highest-value version of this technique is a **profit-and-loss fact
table**: allocating every cost component (cost of goods, marketing spend,
overhead) down to the grain of the atomic revenue transaction, so revenue
minus allocated costs yields a
[profit figure](ratio-decomposition-and-derived-fact-materialization.md)
sliceable by customer, product, promotion, or channel. It's also usually
the hardest transformation to build in an implementation, both because of the sign-off problem above and because
it typically requires pulling in cost data from several source systems that
were never designed to be joined at this grain — expect it to be a
later-phase deliverable rather than part of an initial build.
