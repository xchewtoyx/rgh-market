---
type: concept
title: Dynamic Work Chunking for Failure Resilience
description: >
  Batch work assigned in small, dynamically claimed chunks bounds how much
  progress a managed-compute scheduler can destroy when it kills a replica,
  instead of losing an entire static partition on every failure.
sources:
  - title: Software Engineering at Google
    resource: "Software Engineering at Google (Winters, Manshreck, Wright), ch. 27"
---

# Dynamic Work Chunking for Failure Resilience

On a [pets versus cattle](pets-vs-cattle.md) fleet, the scheduler may kill
any replica at any time. Static work assignment amplifies the damage: if
one million documents are split across two hundred workers with fixed
shards, losing one worker loses roughly one two-hundredth of the total
work — and under churn, failures repeat, each costing the full runtime of
that worker's static slice.

**Dynamic chunking** fixes this by dividing work into many small units
(one thousand chunks of one thousand documents, in the canonical example)
and having workers report results and pick up new chunks from a shared
queue. A killed worker loses at most the chunk it was processing when it
died, not an entire static partition. This pattern matched Google's
standard data-processing architecture of the era and is the batch-job
counterpart to how serving traffic is naturally split into individual
requests load-balanced across a cluster.

The design requirement is explicit: the processing architecture must
tolerate failure, not just the infrastructure. [Progressive compute
automation](progressive-compute-automation.md) can replace failed
processes automatically, but only chunking (or an equivalent dynamic
assignment scheme) keeps that replacement cheap in lost work. Workloads
that cannot be re-chunked — static shard assignments, leaders holding
unreplicated state — remain pet-like even when run on a cattle platform
and need different remediation strategies.

For long-running batch jobs, periodic checkpointing of partial state to
durable storage achieves a similar bound on lost progress when chunking
alone is insufficient.
