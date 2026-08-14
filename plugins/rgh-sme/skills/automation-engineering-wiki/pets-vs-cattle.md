---
type: concept
title: Pets versus Cattle
description: >
  Managed compute treats replicas as interchangeable "cattle" that automation
  can replace without human nursing, which only works when every new instance
  can be stamped out with zero manual setup.
sources:
  - title: Software Engineering at Google
    resource: "Software Engineering at Google (Winters, Manshreck, Wright), ch. 27"
---

# Pets versus Cattle

A **pet** server, when broken, needs a human to diagnose it, tune it back
to health, and is painful to replace — maintenance burden grows at least
linearly with fleet size and often worse, because each pet accumulates
unique state, configuration, and history. A **cattle** replica is named
`replica001` through `replicaN`; when one fails, automation removes it
and stamps out a replacement with no SSH session to install packages or
set environment variables. The defining property is interchangeability: a
new instance is provably equivalent to any other, whether the unit of
stamp-out is a container image or a VM template.

This is the infrastructure-side expression of [uniformity as an automation
prerequisite](uniformity-as-automation-prerequisite.md): automation can
only replace instances it did not have to special-case during provisioning.
On a managed fleet the scheduler may kill and relocate any replica
unilaterally — for kernel updates, bad disks, rebalancing — and the
software author should neither know nor care why. That assumption breaks
for workloads that behave like pets inside a cattle-shaped shell: a
"leader" holding unreconstructable in-memory state, sharded data servers
where losing one host loses a static slice of the dataset, or servers
referenced by hostname elsewhere in the system.

Cattle alone is not enough for graceful operation under moderate churn.
Automatic recovery gets you back to a healthy fleet, but user-visible
errors during replacement still require deliberate design — [lame-duck mode
draining](lame-duck-mode-draining.md) when the scheduler signals intent
ahead of time, and [dynamic work
chunking](dynamic-work-chunking-for-failure-resilience.md) when batch work
would otherwise lose large static assignments on each failure. Serving jobs
that already shard work as individual requests across a load-balanced
cluster inherit much of this naturally; batch and stateful-serving patterns
do not.

Hardcoding hostnames — even as startup configuration — violates the cattle
model. Callers need a durable identifier the scheduler resolves to wherever
the target actually runs, with connections established at startup and
monitored in the background rather than on every request's critical path.
That indirection is what makes mid-request backend loss survivable only
when combined with retries and [idempotency for managed
compute](idempotency-in-automation.md).
