---
type: concept
title: Physical Resource Limits as the Root Cause of Distribution
description: >
  A single server's request capacity is bounded by four physical resources —
  CPU, memory, network, disk — and distribution exists to give a workload
  physically separate copies of each.
sources:
  - title: Patterns of Distributed Systems
    resource: "Patterns of Distributed Systems (Joshi), ch. 1, Why Distribute?"
---

# Physical Resource Limits as the Root Cause of Distribution

Every server's capacity to process requests is ultimately bounded by four
physical resources: **CPU, memory, network, and disk**. Worked example: at
1 Gbps network bandwidth, 1 KB records cap throughput around 125,000
requests/second; 5 KB records cap it around 25,000 — the network alone sets
a hard ceiling before CPU or disk are even considered. Disk imposes a similar
raw bandwidth ceiling, further reduced by the software layer serializing
concurrent reads, writes, and transactions. CPU saturation queues any excess
work. Memory is the fourth limit even though storage engines use indexes
specifically to avoid loading everything into RAM: request patterns that scan
more data than usual still hit it.

When any one of these four resources saturates, requests **queue** for their
share, and queuing time compounds — throughput and end-user latency both
degrade exactly when the system needs to scale to serve more load. The only
structural fix is to **divide the work across multiple servers** so each gets
a physically separate CPU, memory pool, network link, and disk — this is the
one-sentence justification underneath every partitioning and replication
technique in this domain: it doesn't remove work, it gives the work more
physically independent resources to run on. See [scale-up vs.
scale-out](scale-up-vs-scale-out.md) for the resulting stateless/stateful
design split, [partitioning](partitioning.md) for dividing data itself once a
single node's resources are insufficient, and [scaling
effects](scaling-effects.md) for how naive distribution topologies
re-introduce their own bottleneck at a different resource (e.g. an O(N²) mesh
saturating network/CPU on coordination instead of on the workload).
