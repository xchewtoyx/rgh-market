---
type: concept
title: Incremental Combining vs. Raw Grouping
description: >
  Two ends of the streaming state spectrum — buffering all raw inputs versus
  maintaining compact associative accumulators — and when each suffices.
sources:
  - title: Streaming Systems
    resource: "Streaming Systems (Akidau, Chernyak, Lax), ch. 8"
---

Grouping in a streaming pipeline can persist state at two ends of a spectrum.
When neither suffices, see
[generalized streaming state API](generalized-streaming-state-api.md).

**Raw grouping** — append each arriving element to a list (`GroupByKey`
producing `Iterable<V>`). Every trigger firing emits a pane containing all
raw inputs. Simple and always correct, but worst on three axes: stores all
raw inputs for the window; with multiple trigger firings, re-sums inputs
already counted in earlier panes; if grouping is the checkpoint boundary,
failure forces recomputing sums for any retriggerings.

**Incremental combining** — combine inputs into partial aggregates
(accumulators) via an associative, commutative `CombineFn` (create, addInput,
mergeAccumulators, extractOutput). For a mean: accumulator is `(sum, count)`,
output is the float mean. Requires:

1. A **compact intermediate form** — accumulator stays much smaller than N
   raw inputs as N grows.
2. **Order-indifference** — commutativity and associativity so inputs can be
   combined one-by-one as they arrive and partial results merged in parallel
   across machines.

Enables **incrementalization** (spread computation over time, less buffering)
and **parallelization** (MapReduce Combiners, hot-key mitigation via partial
aggregates on many machines). Flume's **combiner lifting** automatically
partially lifts a post-shuffle combine into the preceding stage before the
network shuffle — the same idea, applied by the optimizer. Merging windows is O(1) on accumulators vs. O(N)
on raw lists.

**Shortcoming:** CombineFn fits sums, means, and similar aggregations but not
use cases needing finer per-record control — motivating
[generalized streaming state](generalized-streaming-state-api.md) for complex
logic (conversion attribution, custom session logic).

Choose raw grouping when correctness simplicity outweighs storage and
recomputation cost; choose incremental combining whenever the aggregation is
associative/commutative and state volume or trigger frequency matters. Both
are forms of [streaming persistent state](streaming-persistent-state.md).
