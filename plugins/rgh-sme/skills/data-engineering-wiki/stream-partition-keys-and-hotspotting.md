---
type: concept
title: Stream Partition Keys and Hotspotting
description: >
  Choosing a partition key that both groups related events together and
  spreads load evenly, and the hotspotting failure mode that happens when it
  doesn't.
sources:
  - title: Fundamentals of Data Engineering
    resource: "Fundamentals of Data Engineering (Reis, Housley), ch. 5"
---

Event-streaming platforms subdivide a topic into parallel partitions for
throughput, the way a freeway splits into lanes. Every message routes to a
partition based on a **partition key**, and the same key always lands in the
same partition — which is what makes a partition key a design decision, not
an implementation detail.

Two competing goals drive the choice:

- **Group what needs joint processing** into the same partition — e.g.,
  keying by IoT device ID so one consumer sees all of one device's messages
  in order, which matters when downstream logic needs per-entity ordering.
- **Spread load evenly** across partitions, so no single consumer becomes a
  bottleneck.

**Hotspotting** is what happens when a partition key correlates with a
skewed real-world distribution — for example, partitioning IoT data by US
state overloads the partitions for high-population states while starving
partitions for low-population ones, even though the key technically groups
data correctly. The key that looks like the "natural" grouping for
correctness is not automatically the key that balances load; both properties
have to be checked against the actual data distribution, not just the
schema.

This is a pipeline design decision made at ingestion time that's expensive to
change later, since consumers may already depend on the per-partition
ordering guarantee it produces — see also
[batch vs. streaming ingestion](batch-vs-streaming-ingestion.md) for the
broader decision this sits inside.
