---
type: concept
title: Compute/Storage Separation
description: >
  Decoupling how much data a platform can hold from how much processing
  power is applied to it, and why this is what let cloud warehouses absorb
  big-data-scale workloads.
sources:
  - title: Fundamentals of Data Engineering
    resource: "Fundamentals of Data Engineering (Reis, Housley), ch. 3"
---

Compute/storage separation means data lives durably in cheap, near-limitless
object storage while compute is spun up on demand against it, rather than
storage and compute being fixed together on the same cluster nodes. BigQuery
and Snowflake popularized this pattern for warehouses; it's also the
foundation data lakes were built on from the start.

This decoupling is what let cloud data warehouses absorb workloads that
previously required a dedicated Hadoop cluster — petabyte-scale queries and
rich semistructured/JSON data — without provisioning a fixed, always-on
cluster sized for peak load. It's also a precondition for
[ELT](etl-vs-elt.md): transformation compute can be scaled up only when a
transform job actually runs, and scaled back down (or to zero) afterward,
because the data it operates on isn't tied to that compute's lifetime.

For pipeline design, the practical consequence is that storage and compute
capacity can now be reasoned about and cost-managed independently — a
partitioning or retention decision (see
[data temperature tiering](data-temperature-tiering.md)) no longer implies a
matching compute commitment, and a compute-heavy transformation no longer
implies over-provisioning storage.

**What this replaced**: pre-cloud distributed databases split into two
architectures, both of which this pattern improves on. **Shared-disk**
architectures centralized storage and exposed it to multiple independent
compute clusters over a network — this let compute scale independently per
workload, but every cluster contending for the same central disk turned the
data itself into the bottleneck. **Shared-nothing** architectures (early
Redshift, Greenplum) instead bound disk to each compute cluster, avoiding
that contention, but at the cost of expensive cross-node data transfer for
any operation needing data that lived on another node, and no ability to
tune storage and compute independently — a data-science workload needing
heavy compute against a small dataset and a bulk ETL load needing the
opposite were stuck sharing the same fixed cluster shape. Modern cloud
warehouses combine shared-disk's centralized storage with shared-nothing's
per-workload compute sizing, without either one's downside.
