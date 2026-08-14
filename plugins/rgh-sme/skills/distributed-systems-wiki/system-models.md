---
type: concept
title: System Models
description: >
  The formal assumptions about timing and node failure under which a
  distributed algorithm's correctness is defined and proved.
sources:
  - title: Designing Data-Intensive Applications
    resource: "Designing Data-Intensive Applications (Kleppmann), ch. 8"
---

# System Models

An algorithm is only correct *relative to assumptions*. A system model states
those assumptions so correctness can be reasoned about — and so you can check
whether the model matches your actual environment.

## Timing models

- **Synchronous:** bounded network delay, bounded [process
  pauses](process-pauses.md), bounded clock error. Unrealistic — real systems
  have unbounded delays.
- **Partially synchronous:** behaves synchronously *most of the time*, but
  occasionally delays, pauses, and clock errors become arbitrarily large. The
  model that fits real datacenters, and the one most practical algorithms
  (including [consensus](consensus.md) implementations) target.
- **Asynchronous:** no timing assumptions at all, no clocks or timeouts. Very
  restrictive; few algorithms work here (see the
  [FLP result](consensus.md)).

## Node failure models

- **Crash-stop:** a failed node never returns.
- **Crash-recovery:** nodes crash and later restart, with stable storage
  surviving the crash but in-memory state lost. The usual practical model.
- **Byzantine:** nodes may do anything, including
  [lying](byzantine-faults.md).

## Safety and liveness

Correctness properties split into two kinds, held to different standards:

- **Safety** — "nothing bad happens." A violation happens at an identifiable
  moment and cannot be undone (a duplicate unique value, a fencing token that
  went backward). Safety must hold under **all** conditions, including total
  network partition and any number of crashes.
- **Liveness** — "something good *eventually* happens" (a request eventually
  gets a response; replicas [eventually converge](eventual-consistency.md)).
  Liveness may carry caveats — e.g. guaranteed only once the network heals or
  a majority is up.

Models are simplifications — real hardware corrupts "stable" storage, firmware
bugs revive supposedly-unique identifiers — so proofs establish confidence,
not certainty; the model's fit to reality still has to be judged.
