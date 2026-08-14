---
type: concept
title: Datacenter Load Balancing
description: >
  Inside the datacenter, RPC clients balance directly across backend tasks —
  deterministic subsetting tames the connection mesh, and load-aware picking
  beats round robin.
sources:
  - title: Site Reliability Engineering
    resource: "Site Reliability Engineering (Beyer et al.), ch. 20"
---

# Datacenter Load Balancing

Once traffic has passed the [global tiers](global-load-balancing.md),
service-to-service balancing inside the datacenter is typically **client
side**: the RPC library itself (Stubby/gRPC style) chooses which backend
task gets each request, informed by [service
discovery](service-discovery.md) — no middlebox on the hot path.

## Subsetting

N client tasks fully meshed to M backend tasks means N×M connections — the
[quadratic scaling trap](scaling-effects.md) in connection handles, memory,
and health-check traffic. **Deterministic subsetting** has each client open
connections to only a small fixed subset (e.g. k = 20) of backends, chosen
by a deterministic shuffle of the backend list seeded by client ID — so the
subsets of different clients spread evenly over backends (random selection
would leave some backends over- and under-subscribed). Deterministic also
means a client restart picks the *same* subset, avoiding connection churn.

## Picking within the subset

- **Round robin:** simplest, but blind — backends differ in hardware,
  co-tenancy, and per-request cost, so equal request counts produce unequal
  load.
- **Weighted round robin:** backends report utilization/capacity in RPC
  response metadata; clients skew the rotation accordingly. Feedback-driven
  and markedly better in practice.
- **Least-loaded (least active requests):** each client tracks its
  outstanding in-flight requests per backend and picks the least busy — a
  cheap local proxy for backend load. Caveat: it's the *client's* view
  only, and a backend failing fast can look attractively "idle"
  (few in-flight because it errors instantly) — load-aware picking must
  exclude unhealthy backends first.
- **Utilization limit:** each backend self-estimates its own remaining
  headroom (from live throughput or prior load-test data) and reports it
  outward, so picking is driven by the backend's own capacity claim rather
  than a client-side proxy for load.
- **Latency-based:** stop routing to a backend once its recently observed
  latency crosses a threshold — a direct, symptom-based cutoff rather than
  an inference from load, useful for catching backends that are degraded
  for reasons load counters miss (GC pause, disk contention).
- **Cascade (overflow):** send all traffic to one replica until it
  saturates, then start sending to the next — requires knowing each
  replica's capacity precisely (static config or load-test-derived), and is
  the same overflow shape [global load
  balancing](global-load-balancing.md) uses to spill traffic to another
  datacenter once the local one is full.

## Health probing

Clients actively probe their subset and remove unhealthy or slow backends
from rotation — client-side [failure
detection](timeouts-and-failure-detection.md), including states like
"lame duck" (backend asks not to receive new work while draining). The
eviction hazards apply: aggressive eviction under general slowness
concentrates load on the remainder and can [chain-react
](cascading-failures.md).

## Slow start for newly added backends

Naive least-loaded picking is dangerous the moment a *new* (or freshly
restarted) backend joins the pool: it reports zero in-flight requests, so a
least-loaded balancer reads it as the emptiest option and floods it with
disproportionate traffic — the one node in the pool with unwarmed caches and
no proven capacity gets hit hardest, and it typically falls over. That
crash returns its traffic to the survivors and, if the pool routinely
replaces instances (deploys, autoscaling), the next replacement repeats the
same cycle. **Slow start** fixes this by capping how much traffic *any*
newly added backend can receive per unit time, ramping it up only as it
proves itself. A widely retold case study: CNN.com's servers
crash-looped during the 9/11/2001 traffic surge because each freshly
rebooted backend was, by definition, least-loaded and absorbed all traffic
until it crashed too; the fix in the field was to boot the entire pool
simultaneously so load started even across all of them, and the
already-planned but not-yet-deployed load-balancer fix was exactly a
slow-start mechanism.
