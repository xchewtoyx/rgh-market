---
type: concept
title: Vertical vs. Horizontal Scaling for Observability Datastores
description: Prefer scaling an observability datastore vertically (more cores/faster local disk on fewer nodes) before scaling horizontally, since network is typically the slowest layer in any distributed system, and treat replication (for durability) and sharding (for capacity) as two distinct concerns rather than one.
sources:
  - title: Observability Engineering, 2nd Edition
    resource: "Observability Engineering, 2nd Edition (Majors, Fong-Jones, Miranda), ch. 14"
---

For observability workloads specifically, vertical scaling (fully exploiting a single node's cores, memory, and fast local/NVMe storage) is usually the better first move over horizontal scaling, because network transfer between nodes is typically the slowest layer in any distributed system — a single sufficiently large node can outperform a poorly-tuned cluster of smaller ones for the same total resource cost.

When horizontal scaling is needed, it's useful to keep two distinct concerns separate rather than conflating them:

- **Replication** — for durability and high availability (surviving node loss), not for capacity.
- **Sharding** — for capacity (spreading data too large for one node across many), a shared-nothing partitioning strategy, typically routed through a proxy/fan-out layer keyed by a sharding key.

A further architectural option separates storage from compute entirely: a single logical shard's data lives on shared object storage, while many stateless compute replicas coordinate access to it — this enables fast scale-up/down and even "scale to zero" for compute, independent of how much data is retained. This mirrors the same storage/compute separation used in [decoupled ingestion and query](decoupled-ingestion-and-query.md) architectures.

The general decision-making principle: don't over-engineer a distributed architecture before you need one — a single well-tuned node is a better starting point than replicating a multi-service architecture built for a much larger scale than you're actually operating at.
