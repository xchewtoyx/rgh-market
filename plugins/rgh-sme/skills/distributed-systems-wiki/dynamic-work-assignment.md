---
type: concept
title: Dynamic Work Assignment
description: >
  Workers pull work from a shared pool of small chunks instead of owning
  fixed partitions — bounding how much progress a single worker death loses.
sources:
  - title: Software Engineering at Google
    resource: "Software Engineering at Google (Winters, Manshreck, Wright), ch. 27"
---

# Dynamic Work Assignment

Parallel batch processing over [ephemeral compute
instances](ephemeral-compute-instances.md) fails badly under **static
assignment**: if each of 200 workers owns a fixed slice of 5,000 documents
and one worker dies halfway through, ~50 minutes of that worker's progress
is lost (in a 1M-document / 1 sec-per-doc job sharded 200 ways).

**Dynamic assignment** divides work into many small **chunks** (e.g. 1,000
chunks of 1,000 documents) in a shared queue or coordinator. Workers
complete a chunk, report results, and **pick up the next available chunk**.
A worker death loses at most the chunk in flight — the rest remain available
for surviving workers.

This matched Google's standard data-processing architecture of the Borg era
and is the batch-side analogue of request-level load balancing on serving
tiers: work is already subdivided into units small enough that any instance
can take the next one.

Contrast with **static sharding** on serving or storage tiers (100 servers
each holding 1% of a dataset): losing one server temporarily loses that
shard until recovery — the same bounded-loss problem dynamic assignment
solves for batch, but harder to fix when data locality matters. Hybrid
designs (dynamic work units for compute, [partitioning](partitioning.md)
for data) are common.

Pair with [idempotent](idempotency.md) chunk processing: a chunk may be
assigned twice if a worker dies after finishing but before reporting
completion.
