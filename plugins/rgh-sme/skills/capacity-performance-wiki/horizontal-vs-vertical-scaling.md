---
type: concept
title: Horizontal vs. Vertical Scaling
description: The two fundamental strategies for adding capacity — a bigger single machine (vertical) or more machines sharing the load (horizontal) — and the trade-offs that determine which one a system can actually use.
sources:
  - title: "Designing Data-Intensive Applications"
    resource: "Designing Data-Intensive Applications (Martin Kleppmann), ch. 1"
  - title: "Database Reliability Engineering"
    resource: "Database Reliability Engineering (Laine Campbell, Charity Majors), ch. 1"
---

When a system needs more capacity, there are two fundamental directions to add it:

*   **Vertical scaling (scale up):** move the workload to a more powerful single machine — more CPU, more memory, faster storage.
*   **Horizontal scaling (scale out):** distribute the workload across additional machines in a shared-nothing architecture.

Most pragmatic production architectures mix both: scaling up individual nodes as far as it remains cost-effective, and scaling out once a single machine's ceiling is reached or redundancy is required.

## Why Horizontal Scaling Is Harder Than It Sounds

Vertical scaling is architecturally simple — the application code does not need to change, only the hardware underneath it. Horizontal scaling's difficulty depends heavily on whether the thing being scaled is stateless or stateful:

*   **Stateless services** (e.g., an application server holding no data between requests) distribute trivially — any node can serve any request, so adding nodes is close to a linear capacity gain, limited mainly by a load balancer's ability to distribute traffic evenly.
*   **Stateful data systems** (e.g., a database or a queue holding data that must persist and remain consistent) distributing horizontally introduces substantial complexity: data must be partitioned across nodes, replicated for durability, and kept consistent under concurrent writes and node failures — problems that do not exist when everything lives on one machine. This complexity, not raw hardware limits, is often what actually caps how far a stateful system's horizontal scaling can practically go before operational risk outweighs the added capacity.

    This also limits *autoscaling* specifically: adding instances to a stateful pool only adds usable capacity if load is actually redistributed across the new instances. If routing sends a given piece of state's traffic to the same backend regardless of pool size (e.g., naive hashing that doesn't account for pool changes), horizontal autoscaling adds instances that never receive a proportional share of load — the pool grows but effective capacity doesn't. Intelligent, pool-size-aware task routing (e.g., consistent hashing) is a prerequisite for horizontal autoscaling to help a stateful system at all. Vertical autoscaling (resizing existing instances) can absorb short-lived hotspots without this requirement, but risks leaving the pool with unevenly sized instances if used as a general strategy rather than a targeted one.

## Two More Pathways: Functional Partitioning and Sharding

Horizontal and vertical scaling both assume the workload itself stays a single, undivided thing that just gets more or bigger resources. Two further pathways instead **split the workload**:

*   **Functional partitioning:** split by *what* the workload does — different responsibilities (e.g., a users service, an orders service, a search index) move onto separate, independently scaled resource pools. Each partition can then be scaled (vertically or horizontally) according to its own demand, rather than the whole system sharing one capacity profile.
*   **Sharding:** split by *which subset of data* the workload touches — an otherwise-identical workload is partitioned by a key (user ID, account ID, geographic region) so that each shard handles only its own slice of data and traffic. This is what makes horizontal scaling viable for stateful systems in the first place: instead of every node needing to hold or coordinate over all the data, each node only needs its own shard. How many shards (partitions) a system creates, and whether that count is fixed or adapts over time, directly determines how far horizontal scaling can go — see [fixed partition count as a scaling ceiling](fixed-partition-count-scaling-ceiling.md).

In practice these four pathways combine: a system might shard a stateful data tier (sharding) while running each functional service (functional partitioning) on an independently horizontally-scaled pool of stateless workers (horizontal scaling), with individual nodes sized vertically for their workload's resource profile.

A related but distinct pathway available to data platforms specifically is separating storage capacity from compute capacity entirely, so each can scale on its own axis rather than being tied to the same physical unit — see [disaggregated storage-compute architecture](disaggregated-storage-compute-architecture.md).

## Elasticity vs. Manual Scaling

A separate axis from horizontal/vertical is *how* capacity changes are triggered:

*   **Elastic (automatic) scaling:** capacity is added or removed automatically in response to measured load. Useful when load is unpredictable or highly variable, since it avoids paying for peak capacity around the clock — but it adds operational complexity and can behave unexpectedly under load patterns the automation wasn't tuned for. The policies that decide *when and how much* to scale are a capacity-engineering concern; the mechanism that carries out the scaling action is an implementation concern.
*   **Manual scaling:** capacity changes are made deliberately by an operator. Simpler and more predictable, at the cost of slower response to load changes and the operational burden of someone deciding when to act.

A system's choice between these is a trade-off between operational simplicity and responsiveness to load, independent of whether the scaling itself is horizontal or vertical.
