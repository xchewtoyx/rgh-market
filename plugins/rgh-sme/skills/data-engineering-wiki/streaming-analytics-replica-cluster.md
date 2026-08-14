---
type: concept
title: Streaming Analytics Replica Cluster
description: >
  Running a separate, consumer-fed copy of a streaming cluster dedicated to
  batch loading and ad hoc analysis, so offline consumption never competes
  with the live production stream.
sources:
  - title: "Kafka: a Distributed Messaging System for Log Processing"
    resource: "Kafka: a Distributed Messaging System for Log Processing (Kreps, Narkhede, Rao), §4"
---

The same isolation instinct behind a database's
[read replica for analytics offload](read-replicas-for-analytics-offload.md)
applies to a [log-based message broker](log-based-message-broker.md), but
through a different mechanism: rather than a synchronously replicated
database copy, a dedicated **analytics cluster** runs alongside the
production clusters and populates itself by running its own consumers
against them, pulling data across from wherever the live clusters actually
run (often co-located with production services, close to whatever generates
the events) into a cluster located near the batch infrastructure that
actually needs the data (a Hadoop cluster or warehouse loader).

This gets a pipeline two things a shared cluster wouldn't: heavy batch-load
jobs and ad hoc exploratory queries run against the analytics cluster
without adding read load to the clusters serving live production
consumers, and the analytics cluster's own consumer offset just tracks how
far replication has caught up — restarting or rebalancing it doesn't
threaten the production stream's own delivery guarantees, since it's
reading a copy, not the original.

The cost is the same as any replication topology: an extra hop of latency
(replication has to catch up before analytics jobs see new data) and the
operational overhead of running and monitoring a second cluster — worthwhile
specifically once batch and ad hoc analytical read volume is large enough
that it would otherwise compete with the production consumers the live
cluster exists to serve.
