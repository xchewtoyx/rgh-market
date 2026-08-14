---
type: concept
title: Bulkhead Pattern
description: >
  Partitioning shared resources (thread pools, connection pools, or whole
  infrastructure clusters) per function or tenant so exhaustion in one
  partition cannot starve another.
sources:
  - title: Release It!
    resource: "Release It!: Design and Deploy Production-Ready Software, 2nd Edition (Nygard), ch. 2, ch. 3"
---

The bulkhead pattern, named for the partitioned compartments in a ship's
hull, isolates shared resources — thread pools, database connection pools, or
entire application server clusters — into separate partitions per function,
tenant, or criticality tier. If one partition exhausts its resources, the
failure is contained to that partition; other partitions keep serving
normally because they were never drawing from the same pool.

## Bulkhead vs. circuit breaker

The two patterns are complementary, not interchangeable:

- A [circuit breaker](circuit-breaker-pattern.md) stops a caller from
  continuing to call a dependency that has crossed a failure threshold — it
  protects the caller from a *known-bad* downstream.
- A bulkhead limits how much of a *shared* resource any single caller or
  function can consume in the first place — it protects unrelated callers
  from each other even when no individual call is failing outright, by making
  sure resource exhaustion in one path cannot cross into another.

This is a structural mitigation for [cascading failure](cascading-failure.md)
and a concrete instance of the broader principle that a
[hard dependency](hard-vs-soft-dependency.md) should never be created by
accident through resource sharing — a non-critical function should be
partitioned so it cannot become a hard dependency of the critical path just
by sitting on the same infrastructure.

## Worked example: shared infrastructure without partitioning

A production incident illustrates exactly the failure bulkheads are meant to
prevent. An airline ran its low-priority internal admin tools and its
passenger-facing check-in and booking systems on the same application server
clusters, the same containers, and the same database connection pool, with no
resource partitioning between them. An uncaught exception in a minor admin
function (a missing lookup-table entry for a rare discount code) left a
database connection and a thread unreleased; as more admin requests hit the
same defect, the shared connection pool and thread pool exhausted, and the
failure crossed straight into the passenger-facing systems that happened to
share the same pools — grounding flights fleet-wide over a change that only
touched an internal tool. Partitioning the admin tool onto separate server
clusters and a separate connection pool would have contained the
[fault-error-failure chain](fault-error-failure-chain.md) to the admin
function alone.
