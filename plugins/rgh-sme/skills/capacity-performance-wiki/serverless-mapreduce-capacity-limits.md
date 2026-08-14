---
type: concept
title: Serverless MapReduce Capacity Limits
description: Functions-as-a-service platforms impose hard per-invocation limits on memory, ephemeral disk, and execution time that make serverless MapReduce viable only when the final reduced output fits in a single function's resources — mappers can subdivide work, but the reducer cannot.
sources:
  - title: "Serverless Design Patterns and Best Practices"
    resource: "Serverless Design Patterns and Best Practices (Brian Zambrano), ch. 8"
---

**Serverless MapReduce** — fanning out one mapper function per input shard, writing intermediate results to object storage, then running a reducer that loads all mapper output — fits naturally on a [functions-as-a-service](compute-purchasing-model-spectrum.md) billing model (pay only while functions run). It is viable only when the job's shape stays within three hard per-invocation ceilings that the platform enforces independently of how many mappers run in parallel.

## Viability Heuristic

Serverless MapReduce works when the **final post-reduction dataset is small** — on the order of a few hundred megabytes — so a **single reducer invocation** can download all intermediate files, aggregate them in memory, and write the result within one function's limits. Jobs whose reduced output or unique-key cardinality exceeds that envelope need a different platform (managed cluster, external aggregation store, or query engine over pre-structured data).

## The Three Hard Limits

| Limit | Typical FaaS constraint (AWS Lambda era) | Effect on MapReduce |
| :--- | :--- | :--- |
| **Memory** | Max ~3 GB per invocation | The reducer must hold the full aggregated result set (unique keys plus counts/values) in memory. High-cardinality keys blow this first. |
| **Ephemeral disk (`/tmp`)** | Max ~512 MB | Mappers/reducers that download input files to local disk before parsing cap per-file input size at the disk limit unless streaming directly from memory (which then competes with result-set memory). |
| **Execution time** | Max ~300 seconds | Mappers can dodge this by **subdividing input into more, smaller concurrent invocations** — the MapReduce fan-out pattern. The reducer has **no equivalent escape hatch**: it must load *all* mapper output in one invocation, so a slow or large reduce step simply cannot complete. |

## Worked Example: Unique-Key Cardinality vs. Memory

Counting unique IPv4 addresses with serverless MapReduce:

*   Lambda max memory ≈ 3,221,225,472 bytes.
*   Assume ~24 bytes per aggregated line in the reducer's in-memory structure.
*   Maximum unique keys ≈ 134 million (3,221,225,472 / 24).
*   Total possible IPv4 addresses ≈ 3.7 billion.

The job breaks down once unique-key cardinality approaches ~100 million — well before the theoretical address space is exhausted — because the reducer cannot partition its aggregation across multiple function invocations the way mappers partition input.

## Mapper Fan-Out vs. Reducer Trap

The asymmetry is structural in classic MapReduce on FaaS:

*   **Map phase:** embarrassingly parallel — add more input shards, launch more mapper invocations, each bounded by per-shard size and time limits.
*   **Reduce phase:** inherently serial for the final merge — one function must see every mapper's output to produce the complete result. This is the [reduce-phase single-node bottleneck](reduce-phase-single-node-bottleneck.md) expressed in serverless terms.

Coordination patterns (counting mapper `-done` marker files before reducing, writing an empty lock file at the final-results key to prevent duplicate reducers from racing) add correctness overhead but do not relax the resource ceilings.

## When to Move Off Serverless

Alternatives when any limit binds:

*   **External aggregation store (e.g., Redis):** mappers increment keyed counters directly, eliminating the S3 intermediate-file reduce step for simple counting — at the cost of a single store that must absorb high concurrent write rates from many functions and be cleared between runs.
*   **Query engine over structured object storage (e.g., Athena):** low operational overhead for ad hoc SQL over data already in columnar or well-structured form — but ETL to extract structure (e.g., parsing email headers from raw text) must happen as a separate prep step.
*   **Managed batch cluster (e.g., EMR):** pays for cluster uptime, not per-invocation limits — appropriate when reducer memory, disk, or time requirements exceed FaaS ceilings; clusters can be created and destroyed on demand via automation to approximate serverless economics for intermittent batch jobs.

See [compute purchasing model spectrum](compute-purchasing-model-spectrum.md) for the cost trade-off between per-invocation elasticity and persistent cluster capacity for batch workloads.
