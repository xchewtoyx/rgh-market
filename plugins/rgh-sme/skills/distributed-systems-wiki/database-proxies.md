---
type: concept
title: Database Proxies
description: >
  L4 vs. L7 proxy tiers between applications and datastores — read/write
  splitting, lag-aware routing, and failover redirection, at the cost of a
  new critical component.
sources:
  - title: Database Reliability Engineering
    resource: "Database Reliability Engineering (Campbell, Majors), ch. 12"
---

# Database Proxies

A proxy tier between application servers and the datastore centralizes
routing decisions that would otherwise live in every client. Two levels of
awareness:

- **L4 (transport):** routes on IP/port only. Minimal latency overhead, but
  blind to replication state and load — it can spread connections, not make
  data-aware choices.
- **L7 (protocol-aware):** understands the database protocol, enabling the
  useful behaviors: split reads from writes (writes to the
  [leader](single-leader-replication.md), reads to followers), pull
  [lagged replicas](replication-lag.md) out of rotation to bound stale
  reads, health-check and redirect around failures (cutting recovery time
  during [failover](leader-failover.md)), rewrite or filter queries, cache,
  and emit per-query metrics. Costs more latency and complexity.

Effects to weigh:

- **Availability:** health-check redirection shortens outages, but the proxy
  tier is itself a new single point of failure — it needs redundancy and
  care, or it merely relocates fragility.
- **Data integrity:** lag-aware routing reduces
  [replication-lag anomalies](replication-lag.md) without touching the
  application; conversely, a caching proxy with imperfect invalidation is a
  new stale-data source.
- **Scalability:** effective read distribution over a replica fleet, plus
  load shedding via connection queueing — deliberately capping concurrent
  database work often *raises* total throughput, at the price of queue
  latency.

A proxy is the same job as [partition request
routing](request-routing.md) but for replica selection rather than partition
location; in partitioned systems one tier often does both.
