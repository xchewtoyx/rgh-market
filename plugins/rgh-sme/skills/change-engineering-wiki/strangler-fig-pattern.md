---
type: concept
title: Strangler Fig Pattern
description: >
  Replace a legacy system by routing traffic to a new implementation one
  slice of functionality at a time, so the legacy system is decommissioned
  gradually instead of via a single high-risk cutover.
sources:
  - title: "Fundamentals of Data Engineering"
    resource: "Fundamentals of Data Engineering (Reis, Housley), ch. 3"
---

# Strangler Fig Pattern

Named by Martin Fowler after the strangler fig vine, which grows around a
host tree and gradually replaces it. Applied to system migration: instead
of a "big bang" rewrite — build the whole replacement, then cut over all
at once — insert a routing layer in front of the legacy system and migrate
one piece of functionality (one endpoint, one report, one data domain) at
a time. Each piece is redirected to the new implementation as it becomes
ready, while everything not yet migrated continues to flow through to the
legacy system unchanged. The legacy system shrinks in scope with each
migrated piece until nothing routes to it anymore and it can be retired.

This is the system-level, external-routing counterpart to [branch by
abstraction](branch-by-abstraction.md), which does the same
incremental-replacement trick inside a single codebase via an in-process
abstraction layer. The strangler fig pattern is what to reach for when the
component being replaced is a whole service, database, or system boundary
rather than a library or internal interface, and the routing layer is
external infrastructure (a reverse proxy, an API gateway, a load balancer)
rather than an abstract class or function pointer.

The core safety property is the same either way: every increment is small,
independently reversible (route that one piece back to the legacy system
if the new one misbehaves), and the system stays fully operational
throughout — the alternative all-at-once rewrite is explicitly higher-risk
precisely because it collapses every migrated piece's risk into one
irreversible cutover moment, with no partial-rollback option if something
is wrong. A full strangler migration is often not achievable in practice
for a large or business-critical legacy system — get buy-in for an
explicit exit plan up front, and be prepared for the legacy system to
persist in a shrunken, low-traffic form indefinitely rather than assuming
a hard end date for full retirement.
