---
type: concept
title: Runtime Fault-Detection Instrumentation Taxonomy
description: A checklist of the distinct mechanisms available for instrumenting a system to detect that something has gone wrong at runtime — beyond generic metrics/logs/traces — each catching a different class of fault.
sources:
  - title: "Software Architecture in Practice, 4th Edition"
    resource: "Software Architecture in Practice, 4th Edition (Bass, Clements, Kazman), ch. 4"
---

Detecting a fault before it becomes a user-visible failure requires more than emitting metrics and logs — it requires deliberately instrumenting specific detection mechanisms, each aimed at a different failure class. This is a checklist to consult when deciding what to instrument, not a single technique:

- **Ping/echo** — an asynchronous request/response pair sent between components purely to check reachability and round-trip delay, gated by a timeout threshold. Distinct from a [heartbeat](adaptive-liveness-detection-vs-fixed-timeouts.md) in who initiates: ping/echo is initiated by (or on behalf of) the component being checked; a heartbeat is a periodic message the monitored component sends unprompted.
- **Watchdog** — a periodically-reset counter or timer that a monitored process must "pet" (reset) on a schedule; if it lapses, the watchdog assumes the process has hung or died. A hardware- or OS-level fallback for detecting a component too broken to respond to its own health-check logic.
- **Condition monitoring** — validating design assumptions or invariants inside a running process (e.g. a checksum over an in-memory structure), rather than checking liveness from the outside. The check itself must stay simple enough to be provably correct, since a buggy health check is worse than none.
- **Sanity checking** — validity/reasonableness checks on a component's inputs or outputs at its interfaces, based on knowledge of what values should be possible given the component's internal state — catches corrupted or nonsensical data before it propagates, independent of whether the component reports itself healthy.
- **Voting** — comparing results from multiple redundant sources expected to agree, flagging disagreement as a fault. Only catches faults the redundancy is diverse enough to expose: identical replicas (**replication**) catch random hardware failure but not a shared implementation bug; independently-built implementations of the same spec (**functional redundancy**) also catch implementation bugs but not a shared specification error; independently-sourced *inputs* as well as implementations (**analytic redundancy** — e.g. computing aircraft altitude from barometric pressure, radar, and geometric look-down angle) is needed to catch a spec error too, at the cost of a voter sophisticated enough to weigh disagreeing sensors rather than just taking a majority vote.
- **Self-test** — a component (or its monitor) deliberately exercises the component's own logic to confirm correct operation, often reusing condition-monitoring checks like checksums.
- **Parameter fencing/typing** — placing a known bit pattern after variable-length data to detect memory overwrites, or tagging message parameters with an explicit type so a receiver can detect a sender/receiver content mismatch — narrow, implementation-level detection mechanisms worth knowing exist even though they're rarely the first tool reached for.

Which of these to instrument for a given component depends on which fault classes are plausible for it and how expensive false negatives are — a stateless HTTP service usually only needs ping/echo plus sanity-checked responses, while a component computing a safety- or correctness-critical value (financial calculations, control-system outputs) benefits from voting or condition monitoring specifically because those catch classes of fault that liveness checks alone cannot.
