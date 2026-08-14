---
type: concept
title: Durability as an SLI
description: >
  Durability measures the probability that a known-healthy copy of data can
  still be found in the future, a distinct property from availability that
  needs its own SLI treatment because loss is usually unrecoverable.
sources:
  - title: Implementing Service Level Objectives
    resource: "Implementing Service Level Objectives (Hidalgo), ch. 11"
  - title: Database Reliability Engineering
    resource: "Database Reliability Engineering (Campbell, Majors), ch. 2"
---

Durability is distinct from availability: availability asks "can I access
this now?"; durability asks "does a healthy copy of this exist at all?" A
true durability failure is usually unrecoverable and persists forward into
users' futures, unlike a typical ephemeral availability blip — this asymmetry
justifies proportionally more prevention/containment investment for
data-critical systems than for a typical availability SLO.

Common framing: express durability as an acceptable data-loss window (e.g.
"no more than 2 seconds of data lost") rather than a bare percentage.
Industry benchmark: major cloud object stores publish durability figures like
11 nines annually.

**Practical instrumentation tip**: for an n-way-replicated store, track the
*time* data spends in a degraded-replica state (and its rate of change),
rather than only the current under-replicated percentage — this catches a
system approaching a tipping point before real loss occurs, rather than only
after the fact.

**Pitfall**: don't dismiss "metadata" (decryption keys, indices, permission
graphs) as unimportant to durability — users don't distinguish "your primary
data is safe" from "you can't find it for two weeks." Unavailability of the
means to locate data is functionally unavailability of the data itself.

Not all data warrants the same durability bar — legacy or reconstructible
data can reasonably run a lower bar than current, irreplaceable data.
Additionally, because [replication is not a backup](replication-is-not-a-backup.md),
data-critical systems must separate high-availability replication from
point-in-time recovery strategies to protect overall data durability.

**Durable is not the same as promptly recoverable**: a system can have
excellent durability — nothing is ever actually lost — while still having a
failure mode that leaves data inaccessible for a long stretch of time, e.g.
because recovery means falling back to much slower storage (tape) or copying
over a slow off-site link. Durability alone doesn't bound how long that
recovery takes; see [RTO/RPO](recovery-time-and-point-objectives.md) for the
target that does. This distinction also motivates a scoping question for
*derived* data specifically (data computed from other raw data already held
durably elsewhere): whether it's genuinely worth restoring the derived copy
at all, or cheaper/faster to recreate it from the raw data instead — a
call the durability target for the raw data underneath doesn't answer by
itself.

For a data or pipeline service, [availability](sli-types-by-service-category.md)
is in practice the product of durability, consistency, and read/write
performance together: data that exists (durable), reads the same everywhere
(consistent), and returns within an acceptable time (performant) is what
"available" cashes out to for that kind of service — a data-system analog of
how a request-driven service's availability, latency, and error-rate SLIs
interact rather than stand fully independent.
