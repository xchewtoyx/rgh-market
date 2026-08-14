---
type: concept
title: Timeouts and Failure Detection
description: >
  Timeouts are the only way to detect remote failure on an asynchronous
  network, and choosing them is a trade-off between slow detection and
  declaring live nodes dead.
sources:
  - title: Designing Data-Intensive Applications
    resource: "Designing Data-Intensive Applications (Kleppmann), ch. 8"
  - title: "Release It! (2nd ed.)"
    resource: "Release It!, 2nd ed. (Nygard), ch. 4"
---

# Timeouts and Failure Detection

On an [unreliable network](unreliable-networks.md) with unbounded delays,
there is no proof a remote node is dead — a timeout is the only failure
detector, and it is always a guess. This note covers choosing the timeout
threshold; see [heartbeat](heartbeat.md) for the sender-side liveness signal
the threshold is measured against, and its own failure modes (head-of-line
blocking, single-threaded processing delays, local pauses). The tuning
dilemma:

- **Long timeout:** slow failure detection; users wait, or a genuinely dead
  leader keeps its role too long.
- **Short timeout:** faster detection, but live-but-slow nodes are declared
  dead. Consequences are worse than they look: the "dead" node may still be
  processing (an action can end up performed twice — see
  [idempotency](idempotency.md)), and if the system is slow because of
  overload, failing over and re-transferring its work *adds* load — a cascade
  that can spiral toward total failure.

A principled choice needs latency assumptions: with network delay bounded by d
and processing time by r, a timeout of 2d + r would be safe — but asynchronous
networks have no bound on d, and
[process pauses](process-pauses.md) mean no bound on r either.

Practical approaches:

- Choose timeouts experimentally, from measured round-trip distributions.
- **Adaptive failure detectors** — e.g. the Phi-accrual detector used in
  Cassandra and Akka — continuously sample RTT and its variability and adjust
  the threshold automatically, outputting a suspicion level rather than a
  binary verdict.

Beware the defaults: raw sockets and many vendor client libraries ship with
*infinite* read timeouts (`SO_TIMEOUT = 0`), so a remote peer that hangs or
silently drops packets blocks the calling thread forever — and enough
blocked threads take down the caller's whole worker pool, feeding a
[cascade](cascading-failures.md). Every remote call needs an explicit
timeout, including the ones a library makes on your behalf, and a
[deliberate retry policy](retry-design.md) behind it. The same unbounded
wait during process startup instead of steady-state serving is a sharper
case still — see [blocking startup dependencies](blocking-startup-dependencies.md).

Failure declarations that carry authority (deposing a leader, reassigning
data) must not be made by one node's timeout alone but by
[majority agreement](truth-defined-by-majority.md).
