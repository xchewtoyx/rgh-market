---
type: concept
title: Ratio Decomposition and Derived-Fact Materialization
description: >
  Load-time rules for handling computed metrics: materialize additive
  derived facts once in the pipeline, but store non-additive ratios as
  their separately additive components instead of the ratio itself.
sources:
  - title: "The Data Warehouse Toolkit: The Definitive Guide to Dimensional Modeling, 3rd Edition"
    resource: "The Data Warehouse Toolkit (Kimball, Ross), ch. 3"
---

A derived fact computed from other stored values (gross profit = extended
sales − extended cost) is still fully additive across every dimension, so
it should be computed once, consistently, during the load rather than left
for every downstream BI tool or analyst query to recompute independently.
Recomputing it ad hoc — in a view, a dashboard formula, a report query —
risks each consumer applying a slightly different calculation, which is a
[data quality](data-quality-dimensions.md) consistency failure that's
invisible until two reports disagree. A view that performs the calculation
is an acceptable substitute for physical materialization only if every
consumer is forced through that view with no ad hoc backdoor access to the
raw table; a shared [semantic/metrics layer](semantic-metrics-layer.md) is
the more general solution when the derivation logic is complex enough to
need central governance rather than a single computed column.

A **non-additive** metric — one that can't be correctly summed along any
dimension, such as gross margin (gross profit / extended sales) or a unit
price — cannot be materialized the same way. Summing per-row ratios or
unit prices across a rollup produces a meaningless number; the mathematically
correct aggregation is "ratio of the sums, not sum of the ratios" — sum the
numerator and denominator separately across whatever slice is being
reported, then divide once at the end. The load should therefore store the
numerator and denominator as their own additive facts and leave the
division to query or report time, rather than storing the ratio itself as a
column. Whether to also store the non-additive ratio for convenience (e.g.,
direct filtering or report printing) is a judgment call with limited value
outside those narrow uses, since it can't be re-aggregated correctly once
stored.

**Not every derived value belongs on the fact row, even when it's
additive.** A quarter-to-date or year-to-date running total is tempting to
precompute the same way a derived fact is, but it isn't actually true to
the fact table's own grain — summing or otherwise aggregating a to-date
column across rows produces overstated, nonsensical results, because each
row's to-date value already double-counts everything before it. Leave
running totals like this out of the loaded schema entirely and compute them
in the BI/query layer instead, where they can be scoped correctly to
whatever grouping a report actually needs.

A related but distinct trap applies to
[semi-additive facts](semi-additive-fact-aggregation.md) like inventory
levels or account balances: additive across every dimension except time, so
the correct time aggregation is an average over periods rather than a sum
or a naive row-count average. [Multi-currency fact
storage](multi-currency-fact-storage.md) is a further variant: the
local-currency value is additive only within one currency, which is why it's
paired with a fully-additive standardized-currency value computed once at
load time rather than left to per-report conversion.
